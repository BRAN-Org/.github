# 🤝 Guia de Contribuição da BRAN Org (Brazilian Research Archive Network)

Ficamos muito felizes pelo seu interesse em contribuir com a **BRAN Org**! Nossa missão é construir infraestrutura aberta e de alta fidelidade para a informação acadêmica e científica no Brasil.

Para garantir que nosso acervo permaneça **rigoroso, transparente, auditável e livre de alucinações**, todas as contribuições devem seguir as diretrizes abaixo.

---

## 📜 Princípios e Compromisso com a Verdade

1. **Inviolabilidade dos Dados**:
   - Nunca altere, deduza ou preencha dados acadêmicos com estimativas. Se um artigo ou anais de evento não apresenta DOI, ORCID, resumo ou filiação na fonte original, esse campo DEVE ser mantido como `null` ou `missing`.
2. **Scraping Ético e Responsável**:
   - Ao escrever scrapers para acervos universitários ou plataformas de eventos brasileiras, implemente obrigatoriamente *rate limiting* (delay mínimo de 1 a 2 segundos entre requisições HTTP).
   - Identifique a requisição com o `User-Agent` oficial da organização:
     `BRAN-Org-Harvester/1.0 (+https://github.com/BRAN-Org)`
3. **Conformidade Obrigatória com Schemas**:
   - Todo dataset submetido deve passar 100% na validação contra os esquemas oficiais em `/schemas/` (`article.v1.schema.json`, `event.v1.schema.json`, `provenance.v1.schema.json`).

---

## 🛠️ Como Contribuir

### 1. Submetendo uma Nova Fonte ou Acervo
1. Abra uma Issue usando o template **`Nova Fonte Acadêmica`**.
2. Forneça a URL pública do evento ou periódico, indicando a plataforma de origem (DSpace, OJS, HTML estático, etc.).
3. Indique se os dados exigem parser de PDF (`GROBID`/`pdfplumber`) ou harvester OAI-PMH.

### 2. Contribuindo com Código ou Dados
1. Faça um Fork do repositório correspondente.
2. Crie uma branch descritiva no padrão *Conventional Commits*:
   - `feat/novo-harvester-abec-2024`
   - `fix/correcao-regex-doi`
   - `docs/atualizar-readme`
3. Execute a validação local dos dados antes de submeter o Pull Request:
   ```bash
   python3 scripts/validate_data.py
   ```
4. Abra um Pull Request utilizando nosso **PR Template**. Os Bots de CI/CD validarão automaticamente seus dados e código contra os schemas oficiais.

---

## 🏷️ Mensagens de Commit (Conventional Commits)

Utilizamos commits padronizados para geração automática de releases e CHANGELOG:

- `feat:` Novas funcionalidades, harvesters ou acervos integrados.
- `fix:` Correção em regex, parsers ou erros de rotas/esquemas.
- `docs:` Alterações em documentação, README ou guias.
- `chore:` Dependências, automações CI/CD e scripts internos.

---

## ❓ Precisa de Ajuda?

Fique à vontade para abrir uma [Issue](https://github.com/BRAN-Org/.github/issues) ou entrar em contato direto com os mantenedores da organização. Obrigado por fortalecer a ciência aberta brasileira! 🇧🇷✨
