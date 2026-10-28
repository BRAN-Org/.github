# Manual de Uso e Governança: CRONA Bot (@crona-bot)

> **Guia Operacional para Membros, Curadores e Desenvolvedores da BRAN Org**

A **CRONA** é a GitHub App oficial da **BRAN Org** responsável pela governança temporal, auditoria de integridade de dados e conformidade científica em todos os repositórios de bases de dados acadêmicas (`*-open-database`) e no repositório central de calendário (`calendar_config`).

---

## 1. Funções e Automações da CRONA

### 1.1 Governança Temporal (Diária e Mensal)
- **Rotina Diária (06:00 UTC)**: A CRONA varre o repositório `calendar_config`, recalcula o avanço dos dias e regera automaticamente os arquivos visuais (`calendar.ics` e os badges SVG dos 12 meses) para manter os ponteiros do dia em dia.
- **Rotina Mensal (Dia 1º de cada mês)**:
  1. Cruza a data atual com a matriz do `curation-schedule.yml`.
  2. Identifica se há eventos com janela aberta de novos anais (EBBC, ENANCIB, ABEC, DataGramaZero).
  3. Inspeciona a saúde atual da base (nível de integridade, contagem e taxa de DOIs).
  4. Abre a issue de curadoria **diretamente no repositório da base**, atribuindo e mencionando o mantenedor responsável (ex: `@GabrielBaiano`).

### 1.2 Guarda e Triagem de Pull Requests (Bases de Dados)
Em qualquer Pull Request que altere arquivos em `data/*.json`, `provenance.json` ou `schemas/`:

```text
[PR Aberto]
   ├── Fork Externo? ───────────► [CRONA fecha o PR e orienta abrir Issue]
   └── Branch Interna (Membro):
         ├── Sintaxe JSON Inválida? ──► [Nível 1: Erro Fatal - Interrompe pipeline e alerta linha/coluna]
         ├── Schema com Erros? ──────► [Nível 2: Review com comentários inline nas linhas do JSON]
         └── 100% Conforme? ─────────► [Nível 3: Submete APPROVE formal + Resumo de DOIs]
```

### 1.3 Auditoria Contínua de DOIs e Proveniência
- Varre de forma assíncrona os DOIs dos artigos contra a **DOI Foundation** (`https://doi.org/<doi>`) e a API da **CrossRef**.
- **Soft Fail**: Links mortos na fonte primária (HTTP 404, 500 ou indisponíveis) **não bloqueiam** o merge. Eles são documentados em tabela para registro histórico e atualizam o campo `doi_resolution_rate` no `provenance.json`.
- A cada merge na branch `main`, a CRONA comita a atualização criptográfica do `provenance.json` assinada oficialmente como `crona-bot[bot]`.

---

## 2. Manual de Uso para Membros e Curadores

### Como Enviar Dados Novos ou Correções
1. Crie uma branch a partir da `main` no próprio repositório da base (ou fork de membro da org):
   ```bash
   git checkout -b curadoria/edicao-2026 main
   ```
2. Adicione os novos arquivos JSON em `data/` ou edite os existentes.
3. Antes de abrir o PR, execute a auditoria localmente:
   ```bash
   npm run data:audit
   ```
   *O comando executará exatamente o mesmo motor que a CRONA executa na nuvem.*
4. Abra o Pull Request para a branch `main`.
5. A CRONA analisará seu PR automaticamente:
   - Se houver inconsistências de schema, leia os **comentários inline** deixados por ela no diff do código e faça os ajustes necessários.
   - Assim que tudo estiver corrigido, a CRONA atualizará o comentário e dará **`APPROVE` verde**.
   - Você (ou outro mantenedor) pode clicar imediatamente no botão de **Merge**.

### Como Utilizar o Adiamento (Snooze de 20 Dias) nas Issues Mensais
Quando um evento acadêmico atrasa a publicação dos anais na internet:
1. Abra a issue mensal criada pela CRONA no repositório da base.
2. No checklist operacional, marque a opção:
   - `[x] Ainda não foram disponibilizados os anais da edição (lembrar/reabrir em 20 dias)`
3. A CRONA registrará o adiamento e reabrirá a issue automaticamente com uma nova notificação após o prazo de 20 dias.

---

## 3. Comandos Úteis do Motor Local

Para rodar auditorias manuais específicas via linha de comando:

```bash
# Testar dataset completo contra o schema de artigos
python3 scripts/crona_audit_engine.py --file data/ebbc_articles.json --schema schemas/article.v1.schema.json

# Testar apenas uma amostra de 30 DOIs (execução rápida)
python3 scripts/crona_audit_engine.py --file data/ebbc_articles.json --sample 30

# Rodar auditoria e salvar relatório em Markdown
python3 scripts/crona_audit_engine.py --file data/ebbc_articles.json --output-md relatorio.md

# Atualizar formalmente o provenance.json com a taxa de resolução
python3 scripts/crona_audit_engine.py --file data/ebbc_articles.json --provenance provenance.json --update-provenance
```

---

## 4. Política de Segurança e Credenciais

- A CRONA autentica-se exclusivamente via chave privada RSA (`.pem`) associada ao seu GitHub App ID.
- Os secrets `CRONA_APP_ID` e `CRONA_PRIVATE_KEY` são gerenciados no nível da organização (`BRAN-Org`) e protegidos contra vazamento em logs públicos do GitHub Actions.
- Contribuidores externos não possuem acesso às chaves nem permissão para disparar commits de auditoria.
