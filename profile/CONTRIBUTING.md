# 📘 Manual de Operações e Contribuição Interna — BRAN Org
> **Guia Exclusivo para Membros e Operadores Autorizados da BRAN Org**

Este documento é o **manual de instruções operacional** para membros com permissão de escrita e gestão na **BRAN Org**. Ele define os procedimentos de escavação, tratamento de dados, validação de schemas e manutenção dos repositórios da organização.

---

## 🏛️ 1. Princípios Operacionais e Compromisso com a Verdade

Como membro operador da BRAN Org, suas ações devem seguir rigorosamente 3 preceitos:

1. **Inviolabilidade do Dado de Origem**:
   - Nunca invente, deduza ou tente "adivinhar" metadados que não constam explicitamente no documento/site de origem.
   - Se um artigo não possui DOI, resumo, ORCID ou e-mail de autor na fonte original, esse campo DEVE permanecer registrado como `null`.
2. **Scraping Ético e Responsável**:
   - É obrigatório incluir um delay mínimo (*rate limiting*) de **1.5 a 2.0 segundos** entre requisições em scripts de coleta para não sobrecarregar servidores de universidades brasileiras.
   - O `User-Agent` de todas as requisições deve ser:
     `BRAN-Org-Harvester/1.0 (+https://github.com/BRAN-Org)`
3. **Auditabilidade Total**:
   - Toda alteração em base de dados deve vir acompanhada da atualização do manifesto `provenance.json` (com URL da fonte, data/hora ISO 8601 e hash dos dados brutos).

---

## ⛏️ 2. Workflow de Arqueologia e Ingestão de Dados

O ciclo de trabalho de um membro ao adicionar ou atualizar uma base de dados segue 5 etapas rígidas:

```text
[1. Coleta/Harvest] ➔ [2. Sanitização] ➔ [3. Validação de Schema] ➔ [4. Proveniência] ➔ [5. Commit & Release]
```

### Passo 1: Escavação (Harvesting)
- **OJS / DSpace**: Utilize o protocolo OAI-PMH via biblioteca `Sickle` em Python para extrair Dublin Core.
- **PDFs de Anais Legados**: Utilize `GROBID` ou `pdfplumber`/`marker-pdf` para estruturar título, autores e referências.
- **Páginas HTML Estáticas**: Utilize `BeautifulSoup4` ou `Playwright`/`Puppeteer` respeitando o *rate limiting*.

### Passo 2: Sanitização e Padronização
- Converta os registros brutos para o formato JSON padrão da BRAN Org.
- Limpe caracteres especiais invisíveis e garanta enquadramento em UTF-8.
- Garanta que DOIs sigam a expressão regular: `^10\.\d{4,9}/[-._;()/:A-Za-z0-9]+$`.

### Passo 3: Validação de Schemas
Antes de realizar commit, execute o script de asserção:
```bash
python3 scripts/validate_data.py
```
Nenhum dado pode ser comitado se houver falhas na validação contra `schemas/article.v1.schema.json` ou `schemas/event.v1.schema.json`.

### Passo 4: Atualização da Proveniência (`provenance.json`)
Preencha ou atualize o manifesto `provenance.json` no repositório de dados:
```json
{
  "dataset_id": "nome-do-dataset-v1",
  "source_url": "https://link-da-fonte-original.edu.br",
  "scraped_at": "2026-09-13T16:00:00Z",
  "extractor_name": "nome_do_script",
  "health_level": "BLUE",
  "total_records": 150,
  "missing_doi_count": 10
}
```

---

## 📥 3. Atendimento e Triagem de Issues do Público

Os repositórios de dados públicos (`abec-open-database`, `ebbc-open-database`, etc.) **NÃO aceitam PRs de terceiros**. O público contribui exclusivamente abrindo Issues.

### Procedimento do Membro ao Analisar uma Issue:
1. **Verificar a Evidência**: Acesse a URL da fonte original citada na Issue do usuário.
2. **Auditar o Dado**: Confirme se a inconsistência realmente existe ou se foi uma falha no script de raspagem.
3. **Corrigir no Scraper/Dataset**: Faça a correção necessária localmente.
4. **Validar e Comitar**: Rode o `validate_data.py`, atualize a proveniência e comite com a mensagem:
   `fix(data): 🐛 corrigir metadados do artigo X conforme issue #12`
5. **Fechar a Issue**: Responda ao usuário confirmando a correção e feche a Issue.

---

## 🎨 4. Alterações em Templates do Site e Aplicações

- **Regra Fundamental**: **JAMAIS** faça alterações de layout, componentes React/Vue/HTML, servidor backend (`server.js`) ou estilização diretamente em um repositório de base de dados final (ex: `abec-open-database`).
- **Procedimento**: Qualquer melhoria visual ou estrutural deve ser realizada no repositório **`abec-open-database_template`** (ou template correspondente).
- ⚠️ **Branch de Destino Obrigatória**: Todo Pull Request de desenvolvimento ou template DEVE ser direcionado à branch **`development`** (`base: development`). PRs diretos para a branch `main` serão rejeitados. O merge na `main` ocorre apenas após testes de homologação.

---

## 🏷️ 5. Padrão de Commits da Equipe (Conventional Commits)

- `feat:` Novo harvester, nova funcionalidade ou integração de novo evento.
- `fix(data):` Correção de metadados em base de dados existente.
- `fix(code):` Correção em scripts de raspagem ou validação.
- `docs:` Atualizações em documentações e manuais.
- `chore:` Manutenção de dependências e workflows de CI/CD.
