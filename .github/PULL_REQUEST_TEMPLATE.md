## 📌 Descrição da Alteração

Forneça um resumo claro das mudanças propostas neste Pull Request.

- [ ] Novo harvester / scraper adicionado
- [ ] Atualização/Inclusão de um novo acervo de dados
- [ ] Correção de bug em parser ou regex
- [ ] Melhoria de documentação ou automação CI/CD

---

## 🛡️ Checklist do Compromisso com a Verdade e Integridade

Antes de submeter este Pull Request, confirme se os itens abaixo foram cumpridos:

- [ ] **Branch de Destino**: O Pull Request tem como destino obrigatoriamente a branch **`development`** (PRs para `main` serão rejeitados).
- [ ] Os dados submetidos passaram **100%** na validação contra os esquemas oficiais em `/schemas/`.
- [ ] Nenhum dado ausente na fonte original foi alucinado ou preenchido arbitrariamente (campos sem informação permanecem como `null`).
- [ ] O manifesto de proveniência (`provenance.json`) foi atualizado com a URL original, timestamp de coleta e total de registros.
- [ ] O código do scraper respeita as regras de *rate limiting* (delay mínimo entre requisições) e `User-Agent`.
- [ ] O arquivo `CHANGELOG.md` foi atualizado no padrão BRAN Org.

---

## 🔗 Fonte Original dos Dados
- **URL do Evento / Periódico**: 
- **Plataforma de Origem**: (ex: DSpace, OJS, HTML estático, PDF proceedings)
