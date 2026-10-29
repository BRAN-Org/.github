# Manual de Uso e Governança: CRONA Bot (@crona-bot)

> **Guia Operacional para Membros, Curadores e Desenvolvedores da BRAN Org**

A **CRONA** é a GitHub App oficial da **BRAN Org** responsável pela governança temporal, auditoria de integridade de dados, conformidade científica e integração com o Zenodo em todos os repositórios de bases de dados acadêmicas (`*-open-database`) e no repositório central de calendário (`calendar_config`). Inspirada em **Crona / Chromie** (*World of Warcraft*), ela vigia anomalias nos dados e mantém as linhas do tempo dos acervos em perfeita ordem ao lado de Brann Bronzebeard.

---

## 1. Padrão Oficial de Versionamento de Bases de Dados (`CalVer: vYYYY.MM`)

Repositórios de bases de dados acadêmicas da BRAN Org **não utilizam SemVer tradicional** (como `v1.2.3`), pois datasets e anais científicos representam marcos temporais de publicação e curadoria.

### 1.1 Regras de Nomenclatura de Versão
- **Formato Canônico**: `vYYYY.MM`  
  Exemplo: **`v2026.10`** (Acervo curado na janela de Outubro de 2026).
- **Revisões Intra-mês (Micro/Patch)**: `vYYYY.MM.PATCH`  
  Se houver correções de metadados, reprocessamento de DOIs ou sanificação de títulos dentro do mesmo mês:
  - Primeira revisão: **`v2026.10.1`**
  - Segunda revisão: **`v2026.10.2`**
- **Sintaxe Estrita da Tag**:
  - Prefixo obrigatório `v` minúsculo.
  - Ano com 4 dígitos (`YYYY`).
  - Ponto separador (`.`).
  - Mês obrigatoriamente com 2 dígitos (`01` a `12`).
  - Ponto e número incremental apenas se houver revisão no mesmo mês.
  - **Expressão Regular Oficial**: `^v(20[2-9][0-9])\.(0[1-9]|1[0-2])(\.[0-9]+)?$`

---

## 1.2 Taxonomia Oficial de Identificadores Acadêmicos

Todo artigo acadêmico catalogado na BRAN Org **deve possuir obrigatoriamente um identificador rastreável**. Registros órfãos (sem `id` e sem `doi`) violam o schema canônico (`article.v1.schema.json`) e têm o Pull Request reprovado automaticamente pela CRONA.

A CRONA categoriza e reporta os identificadores nas seguintes classes:

1. **`DOI` (Digital Object Identifier)**: Identificador persistente formal (prefixo `10.xxxx/...`). A CRONA audita via rede se o link está ativo (200 OK) ou se é inativo na fonte primária (soft fail).
2. **`OJS_INTERNAL_ID` (Identificador Nativo OJS/PKP)**: ID numérico sequencial da submissão no Open Journal/Conference Systems (ex: `id: "51"` que mapeia para `/article/view/51` no ENANCIB).
3. **`CANONICAL_SLUG` (Slug Estruturado de Acervo Histórico)**: Código unívoco e determinístico baseado na matriz da edição para acervos pré-OJS ou estáticos (ex: `dgz-v00-n00-a01` no DataGramaZero).
4. **`HANDLE_SYSTEM` (CNRI Handle / DSpace)**: Identificador persistente de repositórios universitários (ex: `hdl:20.500.11959/1269`).
5. **`CONTENT_HASH` (Hash Criptográfico de Proveniência)**: Hash SHA-256 do arquivo fonte bruto quando inexiste código na editora.
6. **`PERMALINK_URI` (URI / URL Canônica Direta)**: Endereço web direto da publicação ou PDF catalogado.

---

## 2. Funções e Automações da CRONA

### 2.1 Governança Temporal (Diária e Mensal)
- **Rotina Diária (06:00 UTC)**: A CRONA varre o repositório `calendar_config`, recalcula o avanço dos dias e regera automaticamente os arquivos visuais (`calendar.ics` e os badges SVG dos 12 meses) para manter os ponteiros do dia em dia.
- **Rotina Mensal (Dia 1º de cada mês)**:
  1. Cruza a data atual com a matriz do `curation-schedule.yml`.
  2. Identifica se há eventos com janela aberta de novos anais (EBBC, ENANCIB, ABEC, DataGramaZero).
  3. Inspeciona a saúde atual da base (nível de integridade, contagem e taxa de DOIs).
  4. Sugere a versão do ciclo no padrão `vYYYY.MM`.
  5. Abre a issue de curadoria **diretamente no repositório da base** com o checklist operacional do ciclo.

### 2.2 Guarda e Triagem de Pull Requests (Bases de Dados)
Em qualquer Pull Request que altere arquivos em `data/*.json`, `provenance.json` ou `schemas/`:

```text
[PR Aberto]
   ├── Fork Externo? ───────────► [CRONA fecha o PR e orienta abrir Issue]
   └── Branch Interna (Membro):
         ├── Sintaxe JSON Inválida? ──► [Nível 1: Erro Fatal - Interrompe pipeline e alerta linha/coluna]
         ├── Schema com Erros? ──────► [Nível 2: Review com comentários inline nas linhas do JSON]
         └── 100% Conforme? ─────────► [Nível 3: Submete APPROVE formal + Resumo de DOIs]
```

### 2.3 Auditoria Contínua de DOIs e Proveniência
- Varre de forma assíncrona os DOIs dos artigos contra a **DOI Foundation** (`https://doi.org/<doi>`) e a API da **CrossRef**.
- **Soft Fail**: Links mortos na fonte primária (HTTP 404, 500 ou indisponíveis) **não bloqueiam** o merge. Eles são documentados em tabela para registro histórico e atualizam o campo `doi_resolution_rate` no `provenance.json`.
- A cada merge na branch `main`, a CRONA comita a atualização criptográfica do `provenance.json` assinada oficialmente como `crona-bot[bot]`.

### 2.4 Watchdog de Proteção de Branches e Alerta Automático
A integridade da base depende de a branch `main` nunca receber commits diretos sem PR:
- **Auditoria de Branches**: A CRONA inspeciona se a branch `main` de todos os repositórios `*-open-database` (e do template) possui branch protection ativada.
- **Abertura de Issue**: Caso uma base esteja desprotegida, a CRONA abre uma issue no repositório (`[CRONA/Segurança] Proteção de Branch Ausente na Main`) com as instruções e comandos exatos de mitigação.
- **Auto-resolução**: Assim que a proteção for ativada, a CRONA detecta na varredura seguinte e fecha a issue automaticamente com mensagem de conformidade.

---

## 3. Sincronização com Zenodo e Gestão de Cold Storage

A CRONA gerencia a sincronização de preservação digital de longo prazo no **Zenodo** mantendo a integridade dos dados e sem estourar limites de rede.

### 3.1 Atualização Automática de Pacotes via Release Tag
Ao publicar uma **Release no GitHub** com tag no padrão `vYYYY.MM`:
1. A CRONA acorda no GitHub Actions e valida a sintaxe da versão.
2. Gera o bundle de ciência aberta da base:
   - `<dataset>.csv` (tabela canônica)
   - `<dataset>.bib` (BibTeX)
   - `<dataset>.ris` (Zotero/VOSviewer)
   - `<dataset>.sqlite` (SQLite indexado com busca FTS5)
   - `datapackage.json` e `<dataset>-zenodo.zip` (metadados).
3. Acessa o depósito da base no Zenodo (via secret `ZENODO_TOKEN`) e **substitui os pacotes de dados no bucket do depósito**, mantendo o DOI estável.

### 3.2 Gestão de Cold Storage de PDFs (Aviso de Pendência)
Como o acervo bruto de PDFs (ex: 3.7 GB do ENANCIB) vive apenas localmente e está no `.gitignore` para não inflar o Git:
- **Marcação no `provenance.json`**: A CRONA registra no manifesto se o pacote pesado de PDFs está pendente de envio:
  ```json
  "cold_storage": {
    "metadata_synced_at": "2026-10-29T15:30:00Z",
    "zenodo_deposit_status": "UPDATED",
    "pdf_corpus_pending": true,
    "notes": "Metadados e SQLite sincronizados. Pacote de PDFs pendente de sincronização local."
  }
  ```
- **Alerta nas Issues Mensais**: Se `pdf_corpus_pending` for `true`, a CRONA adiciona um aviso destacado na issue mensal:
  > ⚠️ **Preservação de PDFs Pendente**: O acervo de dados está atualizado no Zenodo, mas o arquivo completo de PDFs de texto completo precisa ser sincronizado localmente.
  > - [ ] Sincronizar pacote completo de PDFs com o Zenodo (`npm run data:zenodo:full`)
- **Nas Notas da Release**: A CRONA adiciona:
  - `Status Zenodo: Metadados Atualizados ✅`
  - `Pacote de PDFs: Sincronização Local Pendente ⏳`

---

## 4. Manual de Operação para Membros e Curadores

### Como Publicar uma Nova Versão da Base
1. Conclua a curadoria na branch interna e faça o merge na `main` com aprovação da CRONA.
2. Crie e envie a tag no padrão `vYYYY.MM`:
   ```bash
   git tag v2026.10
   git push origin v2026.10
   ```
3. Acesse `Releases -> Draft a new release`, selecione a tag `v2026.10` e publique.
4. A CRONA atualizará o Zenodo automaticamente.

### Como Enviar o Pacote Pesado de PDFs Localmente
Quando você raspar ou atualizar PDFs brutos na sua máquina:
```bash
npm run data:zenodo:full
```
O script empacotará os PDFs locais e enviará diretamente ao bucket do Zenodo via streaming, alterando `pdf_corpus_pending` para `false`.

### Como Usar o Adiamento (Snooze de 20 Dias)
Se os anais do evento atrasarem:
1. Abra a issue mensal criada pela CRONA.
2. Marque o checkbox:
   - `[x] Ainda não foram disponibilizados os anais da edição (lembrar/reabrir em 20 dias)`
3. A CRONA registrará o adiamento e reabrirá a issue automaticamente com nova notificação após 20 dias.
