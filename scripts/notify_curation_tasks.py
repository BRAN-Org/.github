#!/usr/bin/env python3
"""
BRAN Org - Notificador de Curadoria via GitHub Issues.
Inspeciona tarefas ativas do mês e abre issues de checklist com deduplicação.
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
        print(f"Aviso ao consultar issues existentes: {err}")
        return False
    
    try:
        issues = json.loads(out)
        for issue in issues:
            title = issue.get("title", "")
            if title_prefix.lower() in title.lower() and str(year) in title:
                print(f"Issue existente detectada: #{issue.get('number')} - '{title}'")
                return True
    except Exception as e:
        print(f"Erro ao analisar issues existentes: {e}")
        return False
    
    return False


def create_issue(repo: str, title: str, body: str, labels: list, assignee: str, dry_run: bool = False):
    if dry_run:
        print(f"\n[DRY RUN] Criaria Issue:")
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


def main():
    parser = argparse.ArgumentParser(description="Notificador de tarefas de curadoria BRAN")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho do curation-schedule.yml")
    parser.add_argument("--year", type=int, help="Ano de referência (padrão: ano atual)")
    parser.add_argument("--month", type=int, help="Mês de referência (padrão: mês atual 1-12)")
    parser.add_argument("--repo", default=os.getenv("GITHUB_REPOSITORY", "BRAN-Org/.github"), help="Repositório alvo")
    parser.add_argument("--assignee", help="Assignee da issue")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simula a criação das issues")
    
    args = parser.parse_args()
    
    now = datetime.now()
    year = args.year if args.year is not None else now.year
    month = args.month if args.month is not None else now.month
    
    schedule_data = load_schedule(args.schedule)
    settings = schedule_data.get("settings", {})
    assignee = args.assignee or settings.get("default_assignee", "GabrielBaiano")
    
    tasks = get_active_tasks(schedule_data, year, month)
    print(f"Verificando tarefas para {month:02d}/{year} no repositório {args.repo}...")
    
    if not tasks:
        print("Nenhuma tarefa de curadoria prevista para este mês.")
        return
    
    print(f"Encontradas {len(tasks)} tarefas potenciais:")
    for t in tasks:
        print(f"- {t['name']}")
        
    for task in tasks:
        short_name = task["short_name"]
        title_prefix = f"[Curadoria] {short_name}"
        title = f"{title_prefix}: Verificação de Anais e Integridade ({year})"
        
        # Deduplicação
        if not args.dry_run and check_existing_issue(args.repo, title_prefix, year):
            print(f"Ignorando '{short_name}' ({year}): Issue para este ciclo já existe.")
            continue
            
        checklist_str = "\n".join([f"- [ ] {item}" for item in task.get("checklist", [])])
        
        body = f"""## Ciclo de Curadoria: {task['name']} ({year})

**Janela de Verificação:** Mês {month:02d}/{year}  
**Repositório:** [{task['repo']}](https://github.com/{task['repo']})  
**Fonte Oficial:** [{task['url']}]({task['url']})  

### Objetivo
{task['description']}

### Checklist Operacional
{checklist_str}

---
*Esta issue foi aberta automaticamente pelo workflow de [Calendário de Curadoria da BRAN Org](CALENDAR.md).*
"""
        create_issue(
            repo=args.repo,
            title=title,
            body=body,
            labels=task.get("labels", ["curation"]),
            assignee=assignee,
            dry_run=args.dry_run
        )


if __name__ == "__main__":
    main()
