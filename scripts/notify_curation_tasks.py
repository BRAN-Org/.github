#!/usr/bin/env python3
"""
BRAN Org - CRONA Bot: Notificador de Curadoria via GitHub Issues.
Inspeciona tarefas ativas do mês conforme o curation-schedule.yml,
audita status de saúde da base e abre issues de checklist com deduplicação
diretamente nos repositórios alvo marcando o mantenedor responsável.
"""

import sys
import os
import argparse
import subprocess
import json
from datetime import datetime, timezone

from generate_calendar import load_schedule, get_active_tasks, DEFAULT_SCHEDULE_PATH


def run_gh_command(cmd_args):
    """Executa comando da CLI gh e retorna stdout."""
    res = subprocess.run(
        ["gh"] + cmd_args,
        capture_output=True,
        text=True,
        check=False
    )
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def check_existing_issue(repo: str, title_prefix: str, year: int) -> bool:
    """Verifica se já existe uma issue aberta ou fechada com o mesmo ciclo."""
    search_term = f"{title_prefix} {year}"
    code, out, err = run_gh_command([
        "issue", "list",
        "--repo", repo,
        "--state", "all",
        "--search", search_term,
        "--json", "number,title"
    ])
    if code != 0:
        print(f"Aviso ao consultar issues existentes em {repo}: {err}")
        return False
    
    try:
        issues = json.loads(out)
        for issue in issues:
            title = issue.get("title", "")
            if title_prefix.lower() in title.lower() and str(year) in title:
                print(f"Issue existente detectada em {repo}: #{issue.get('number')} - '{title}'")
                return True
    except Exception as e:
        print(f"Erro ao analisar issues existentes: {e}")
        return False
    
    return False


def create_issue(repo: str, title: str, body: str, labels: list, assignee: str, dry_run: bool = False):
    if dry_run:
        print(f"\n[DRY RUN] CRONA criaria Issue:")
        print(f"Repo: {repo}")
        print(f"Título: {title}")
        print(f"Assignee: {assignee}")
        print(f"Labels: {', '.join(labels)}")
        print(f"Corpo:\n{body}\n")
        return True
    
    cmd = [
        "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
    ]
    if assignee:
        cmd.extend(["--assignee", assignee])
    for label in labels:
        cmd.extend(["--label", label])
        
    code, out, err = run_gh_command(cmd)
    if code != 0:
        # Se falhar por causa de label inexistente, tenta sem labels
        if "label" in err.lower():
            print(f"Aviso com labels, tentando sem labels: {err}")
            cmd_fallback = [
                "issue", "create",
                "--repo", repo,
                "--title", title,
                "--body", body,
            ]
            if assignee:
                cmd_fallback.extend(["--assignee", assignee])
            code_fb, out_fb, err_fb = run_gh_command(cmd_fallback)
            if code_fb == 0:
                print(f"Issue criada com sucesso: {out_fb}")
                return True
            else:
                print(f"Erro ao criar issue (fallback): {err_fb}")
                return False
        else:
            print(f"Erro ao criar issue: {err}")
            return False
            
    print(f"Issue criada com sucesso: {out}")
    return True


def fetch_database_provenance(repo: str):
    """Tenta obter o provenance.json da branch principal do repositório para enriquecer a issue."""
    raw_url = f"https://raw.githubusercontent.com/{repo}/main/provenance.json"
    try:
        import urllib.request
        req = urllib.request.Request(raw_url, headers={"User-Agent": "BRAN-CronaBot/1.0"})
        with urllib.request.urlopen(req, timeout=5) as resp:
            if resp.status == 200:
                return json.loads(resp.read().decode("utf-8"))
    except Exception:
        pass
    return None


def main():
    parser = argparse.ArgumentParser(description="CRONA Bot - Notificador de tarefas e auditorias de curadoria")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho do curation-schedule.yml")
    parser.add_argument("--year", type=int, help="Ano de referência (padrão: ano atual)")
    parser.add_argument("--month", type=int, help="Mês de referência (padrão: mês atual 1-12)")
    parser.add_argument("--repo", help="Forçar repositório específico em vez do repositório configurado na base")
    parser.add_argument("--target-db-repos", action="store_true", default=True, help="Abre a issue diretamente no repositório da database (padrão)")
    parser.add_argument("--assignee", help="Assignee da issue (sobrescreve o default)")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simula a criação das issues")
    
    args = parser.parse_args()
    
    now = datetime.now()
    year = args.year if args.year is not None else now.year
    month = args.month if args.month is not None else now.month
    
    schedule_data = load_schedule(args.schedule)
    settings = schedule_data.get("settings", {})
    default_assignee = settings.get("default_assignee", "GabrielBaiano")
    assignee = args.assignee or default_assignee
    
    tasks = get_active_tasks(schedule_data, year, month)
    print(f"🤖 CRONA: Verificando tarefas ativas para {month:02d}/{year}...")
    
    if not tasks:
        print("🤖 CRONA: Nenhuma tarefa de curadoria prevista para este mês no calendário.")
        return
    
    print(f"🤖 CRONA: Encontradas {len(tasks)} tarefas potenciais:")
    for t in tasks:
        print(f"- {t['name']} ({t.get('repo')})")
        
    for task in tasks:
        short_name = task["short_name"]
        target_repo = args.repo or (task.get("repo") if args.target_db_repos else "BRAN-Org/calendar_config")
        title_prefix = f"[CRONA/Curadoria] {short_name}"
        title = f"{title_prefix}: Verificação de Anais e Auditoria ({year})"
        
        # Deduplicação
        if not args.dry_run and check_existing_issue(target_repo, title_prefix, year):
            print(f"Ignorando '{short_name}' ({year}): Issue para este ciclo já existe em {target_repo}.")
            continue
            
        checklist_str = "\n".join([f"- [ ] {item}" for item in task.get("checklist", [])])
        
        # Enriquecimento com provenance.json
        provenance = fetch_database_provenance(task.get("repo", ""))
        prov_info = ""
        cold_storage_alert = ""
        cold_storage_task = ""
        if provenance:
            health = provenance.get("health_level", "NÃO INFORMADO")
            records = provenance.get("total_records", "N/A")
            doi_rate = provenance.get("doi_resolution_rate")
            doi_rate_str = f"{doi_rate * 100:.1f}%" if doi_rate is not None else "Ainda não auditado"
            last_audit = provenance.get("last_audit_at", "N/A")
            prov_info = f"""
### 📊 Status de Integridade da Base (Última Auditoria)
- **Nível de Saúde:** `{health}`
- **Total de Registros:** `{records}`
- **Taxa de Resolução de DOIs:** `{doi_rate_str}`
- **Última Auditoria:** `{last_audit}`
"""
            cold_storage = provenance.get("cold_storage", {})
            if cold_storage.get("pdf_corpus_pending"):
                cold_storage_alert = """
> ⚠️ **Preservação de PDFs Pendente (Cold Storage)**:
> O acervo de dados e metadados está sincronizado no Zenodo, mas o arquivo completo de PDFs de texto completo precisa ser sincronizado localmente via `npm run data:zenodo:full`.
"""
                cold_storage_task = "- [ ] ⚠️ Sincronizar pacote completo de PDFs (Cold Storage) com o Zenodo (Pendente upload local via `npm run data:zenodo:full`)\n"

        mention_str = f"@{assignee}" if assignee else "equipe de curadoria"
        suggested_calver = f"v{year}.{month:02d}"

        body = f"""## 🤖 Alerta de Curadoria CRONA: {task['name']} ({year})

Olá {mention_str}! Segundo o [Calendário Oficial de Curadoria da BRAN Org](https://github.com/BRAN-Org/calendar_config), o mês **{month:02d}/{year}** é a janela programada para verificar atualizações no evento **{short_name}**.

**Janela de Verificação:** Mês {month:02d}/{year}  
**Versão do Ciclo Sugerida:** `{suggested_calver}` (Padrão CalVer da BRAN Org)  
**Repositório Oficial:** [{task['repo']}](https://github.com/{task['repo']})  
**Portal Primário:** [{task['url']}]({task['url']})  
{prov_info}{cold_storage_alert}
### 🎯 Objetivo do Ciclo
{task['description']}

### 📋 Checklist Operacional Recomendado
{checklist_str}
- [ ] Executar auditoria de DOIs e integridade com a CRONA (`crona_audit_engine.py` ou `npm run data:audit`)
- [ ] Confirmar integridade do pacote no Zenodo ao publicar a Release `{suggested_calver}`
{cold_storage_task}
---
*Esta issue foi gerada automaticamente pelo **CRONA Bot** (@crona-bot) via `calendar_config/curation-schedule.yml`.*
"""
        create_issue(
            repo=target_repo,
            title=title,
            body=body,
            labels=task.get("labels", ["curation"]),
            assignee=assignee,
            dry_run=args.dry_run
        )


if __name__ == "__main__":
    main()
