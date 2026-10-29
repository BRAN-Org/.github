#!/usr/bin/env python3
"""
BRAN Org - CRONA Bot: Watchdog de Proteção de Branches e Governança de Bases de Dados.
Audita periodicamente todos os repositórios de bases de dados acadêmicas (e template) da organização.
Verifica se a branch 'main' possui proteção ativada e se o fluxo do crona-guard.yml está presente.
Se desprotegido, abre issue alertando o mantenedor responsável com passos de correção.
Se a proteção for restabelecida, fecha automaticamente a issue aberta anteriormente.
"""

import sys
import os
import argparse
import subprocess
import json
import yaml

DEFAULT_SCHEDULE_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "curation-schedule.yml")


def run_gh_command(cmd_args):
    """Executa comando da CLI gh e retorna (returncode, stdout, stderr)."""
    res = subprocess.run(
        ["gh"] + cmd_args,
        capture_output=True,
        text=True,
        check=False
    )
    return res.returncode, res.stdout.strip(), res.stderr.strip()


def get_target_repositories(schedule_path: str):
    """Obtém a lista consolidada de repositórios de bases de dados a partir do calendário e da org."""
    repos = set()
    if os.path.exists(schedule_path):
        with open(schedule_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
            for task in data.get("tasks", []):
                r = task.get("repo")
                if r:
                    repos.add(r.strip())

    # Adiciona sempre o template e bases canônicas
    repos.add("BRAN-Org/bran-web-database-template")
    repos.add("BRAN-Org/ebbc-open-database")
    repos.add("BRAN-Org/enancib-open-database")
    repos.add("BRAN-Org/abec-open-database")
    repos.add("BRAN-Org/datagramazero-open-database")

    # Tenta listar dinamicamente via CLI gh todos os repos que terminam com -open-database
    code, out, _ = run_gh_command(["repo", "list", "BRAN-Org", "--json", "nameWithOwner,isArchived", "--limit", "100"])
    if code == 0:
        try:
            repo_list = json.loads(out)
            for item in repo_list:
                name = item.get("nameWithOwner", "")
                if not item.get("isArchived") and ("-open-database" in name or name.endswith("-database-template")):
                    repos.add(name)
        except Exception:
            pass

    return sorted(list(repos))


def check_branch_protection(repo: str, branch: str = "main"):
    """Consulta os metadados da branch para verificar se a proteção está ativada."""
    code, out, err = run_gh_command(["api", f"/repos/{repo}/branches/{branch}"])
    if code != 0:
        return False, f"Erro ao acessar branch: {err}"
    try:
        data = json.loads(out)
        is_protected = data.get("protected", False)
        return is_protected, None
    except Exception as e:
        return False, str(e)


def check_guard_workflow(repo: str):
    """Verifica se o workflow crona-guard.yml existe no repositório."""
    code, _, _ = run_gh_command(["api", f"/repos/{repo}/contents/.github/workflows/crona-guard.yml"])
    return code == 0


def find_existing_protection_issue(repo: str, marker: str = "[CRONA/Segurança]"):
    """Busca issue aberta existente sobre segurança/proteção."""
    code, out, _ = run_gh_command([
        "issue", "list",
        "--repo", repo,
        "--state", "open",
        "--search", marker,
        "--json", "number,title"
    ])
    if code != 0:
        return None
    try:
        issues = json.loads(out)
        for iss in issues:
            if marker.lower() in iss.get("title", "").lower():
                return iss.get("number")
    except Exception:
        pass
    return None


def create_protection_alert_issue(repo: str, assignee: str, dry_run: bool = False):
    """Abre issue de alerta com instruções técnicas de mitigação."""
    title = "[CRONA/Segurança] Proteção de Branch Ausente na Main"
    body = f"""## Proteção de Branch Ausente na Main

> *"A branch main está desprotegida... commits diretos podem quebrar a integridade e o histórico do acervo."*

A branch principal (`main`) de [{repo}](https://github.com/{repo}) está atualmente sem regras de proteção ativadas.

### Risco
Sem proteção de branch na `main`:
1. Commits diretos podem entrar sem passar por Pull Request (`git push origin main`), pulando a validação de schema e checagem de DOIs.
2. Force pushes acidentais (`git push --force`) podem sobrescrever o histórico canônico de proveniência (`provenance.json`).
3. O review de integridade da base deixa de ser um requisito vinculante para inclusão de novos dados.

### Como Resolver via CLI (`gh`)

```bash
gh api -X PUT /repos/{repo}/branches/main/protection \\
  --input - <<< '{{
    "required_status_checks": null,
    "enforce_admins": false,
    "required_pull_request_reviews": {{
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": false,
      "required_approving_review_count": 0
    }},
    "restrictions": null,
    "allow_force_pushes": false,
    "allow_deletions": false
  }}'
```

### Ou via Interface do GitHub (Settings)
1. Acesse: **Settings** -> **Branches** -> **Add branch protection rule**.
2. **Branch name pattern**: `main`.
3. Marque `Require a pull request before merging`.
4. Desmarque `Allow force pushes` e `Allow deletions`.
5. Salve as alterações.
"""
    if dry_run:
        print(f"\n[DRY RUN] CRONA abriria issue de alerta em {repo}:")
        print(f"Título: {title}")
        print(f"Assignee: {assignee}")
        return True

    cmd = [
        "issue", "create",
        "--repo", repo,
        "--title", title,
        "--body", body,
    ]
    if assignee:
        cmd.extend(["--assignee", assignee])

    code, out, err = run_gh_command(cmd)
    if code == 0:
        print(f"   Issue de alerta #{out} criada em {repo}.")
        return True
    else:
        print(f"   Falha ao criar issue em {repo}: {err}")
        return False


def close_protection_alert_issue(repo: str, issue_number: int, dry_run: bool = False):
    """Fecha a issue de alerta informando que a proteção foi restabelecida."""
    msg = "Proteção de branch restabelecida na main. Repositório seguro e em conformidade."
    if dry_run:
        print(f"\n[DRY RUN] CRONA fecharia issue #{issue_number} em {repo}.")
        return True

    run_gh_command(["issue", "comment", str(issue_number), "--repo", repo, "--body", msg])
    code, out, err = run_gh_command(["issue", "close", str(issue_number), "--repo", repo, "--reason", "completed"])
    if code == 0:
        print(f"   ✓ Issue de alerta #{issue_number} em {repo} fechada automaticamente.")
        return True
    else:
        print(f"   Aviso ao fechar issue #{issue_number}: {err}")
        return False


def main():
    parser = argparse.ArgumentParser(description="CRONA Bot - Watchdog de Proteção de Branches de Bases de Dados")
    parser.add_argument("--schedule", default=DEFAULT_SCHEDULE_PATH, help="Caminho do curation-schedule.yml")
    parser.add_argument("--assignee", default=None, help="Usuário a ser marcado nas issues (opcional)")
    parser.add_argument("--dry-run", action="store_true", help="Apenas simula a checagem sem abrir issues reais")

    args = parser.parse_args()

    repos = get_target_repositories(args.schedule)
    print("=" * 65)
    print("CRONA: Watchdog de Proteção de Branches")
    print(f"Total de repositórios auditados: {len(repos)}")
    print("=" * 65)

    all_secure = True
    for repo in repos:
        print(f"\nAuditando [{repo}]...")
        is_protected, err = check_branch_protection(repo, "main")
        has_guard = check_guard_workflow(repo)

        existing_issue = find_existing_protection_issue(repo)

        if not is_protected:
            all_secure = False
            print(f"   ⚠️  Branch 'main' NÃO ESTÁ PROTEGIDA!")
            if existing_issue:
                print(f"   ℹ️  Issue de alerta #{existing_issue} já está aberta. Sem duplicidade.")
            else:
                create_protection_alert_issue(repo, args.assignee, args.dry_run)
        else:
            print(f"   ✓ Branch 'main' protegida.")
            if existing_issue:
                print(f"   🎉 Proteção restabelecida! Fechando issue #{existing_issue}...")
                close_protection_alert_issue(repo, existing_issue, args.dry_run)

        if not has_guard:
            print(f"   ⚠️  Aviso: Workflow crona-guard.yml ausente em .github/workflows/")
        else:
            print(f"   ✓ crona-guard.yml ativo.")

    print("\n" + "=" * 65)
    if all_secure:
        print("✨ Todos os repositórios de bases de dados estão devidamente protegidos!")
    else:
        print("⚠️  Alguns repositórios necessitam de ajuste de branch protection.")
    print("=" * 65)


if __name__ == "__main__":
    main()
