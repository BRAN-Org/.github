# Guia de Contribuição — BRAN Org

<p align="center">
  <a href="CONTRIBUTING.en.md"><img src="https://img.shields.io/badge/Read%20in-English-blue.svg?style=for-the-badge" alt="Read in English"></a>
</p>

Agradecemos o interesse em colaborar com a **BRAN Org** (**Brazilian Research Archive Network**). Nossa missão é resgatar, estruturar e preservar a memória científica e bibliométrica do Brasil sob os princípios de ciência aberta, transparência e utilidade pública.

Toda a comunidade acadêmica e técnica — pesquisadores, bibliotecários, cientistas de dados e desenvolvedores — é bem-vinda para contribuir.

---

## Governança Automatizada: Bots CRONA e BRAN

A organização opera com dois bots oficiais para manter a integridade científica e o ciclo de vida dos repositórios:

- **CRONA (`@crona-bot`)**: Guardiã dos repositórios de dados (`*-open-database`) e governança temporal (`calendar_config`). Realiza testes de resolução de DOIs, validação estrita de esquemas JSON, atualização diária do calendário e auditoria contínua de proveniência.
- **BRAN (`@bran-bot`)**: Guardião dos repositórios de software e infraestrutura (`bibliolatam`, `schemas`, ferramentas e templates). Gerencia testes automatizados, padronização de commits semânticos e sincronização de código.

---

## Formas de Contribuição

### 1. Correção e Apontamento de Erros em Dados
Se você identificou uma inconsistência, título cortado, DOI ausente na extração ou metadado divergente da fonte original em uma de nossas bases:

1. Acesse o repositório específico do dataset (ex: [`ebbc-open-database`](https://github.com/BRAN-Org/ebbc-open-database) ou [`abec-open-database`](https://github.com/BRAN-Org/abec-open-database)).
2. Abra uma **Issue** detalhando o erro e, **obrigatoriamente**, forneça o link da publicação oficial na fonte primária onde o dado correto está disponível.
3. **Política de Pull Requests em Dados**: Para garantir a inviolabilidade científica e a rastreabilidade da proveniência (`provenance.json`), repositórios de bases de dados **não aceitam alterações diretas via Pull Request de forks externos**. Qualquer PR externo em arquivos de dados é automaticamente encerrado pela **CRONA**, orientando a abertura de uma Issue para curadoria canônica.

### 2. Fluxo de Curadoria Interna de Dados (Mantenedores e Curadores)
Para curadores que enviam novos anais ou correções em branches internas da organização:
- **Nível 1 (Erro Fatal)**: Se o arquivo JSON contiver erros de sintaxe (malformado), a CRONA interrompe o pipeline e solicita a correção do arquivo.
- **Nível 2 (Erros de Schema)**: Se campos obrigatórios estiverem ausentes ou fora de especificação, a CRONA insere comentários *inline* de Code Review diretamente nas linhas com erro no PR.
- **Nível 3 (Aprovação Automática)**: Se a estrutura e o schema estiverem 100% em conformidade, a CRONA submete uma revisão de **`APPROVE`** formal no PR e publica o relatório de integridade de DOIs (sem bloquear por links caídos na origem). O mantenedor pode então realizar o merge.

### 3. Sugestão e Submissão de Novos Acervos
Se você organiza um evento acadêmico, representa uma sociedade científica ou possui anais e acervos históricos que correm risco de desaparecimento digital (*link rot*):

- Submeta a indicação através do **[Formulário de Submissão de Datasets](https://forms.gle/jNBuP1mjyUXc6v1fA)**.
- Ou abra uma discussão via **[Issues do .github](https://github.com/BRAN-Org/.github/issues)** descrevendo o evento, volume aproximado de artigos e links disponíveis.

### 4. Contribuição com Código e Ferramentas Abertas
Desenvolvemos softwares, analisadores e bibliotecas livres (como o pacote [`bibliolatam`](https://github.com/BRAN-Org/bibliolatam), o repositório [`schemas`](https://github.com/BRAN-Org/schemas) e templates de interface). Nesses repositórios, Pull Requests são muito bem-vindos.

#### Fluxo para Envio de Código:
1. Faça um Fork do repositório correspondente.
2. Crie uma branch para sua alteração (`git checkout -b feature/minha-melhoria` ou `git checkout -b fix/descricao-do-bug`).
3. Adicione ou atualize os testes automatizados cobrindo suas alterações.
4. Escreva commits semânticos objetivos ([Conventional Commits](https://www.conventionalcommits.org/)):
   - `feat:` nova funcionalidade ou parser.
   - `fix:` correção de bug em rotina existente.
   - `docs:` melhorias em documentação.
   - `test:` adição ou ajuste de suíte de testes.
5. O bot **BRAN** validará o formato do commit e executará as suites de testes (`testthat`/`pytest`). Estando verde, seu PR será revisado e mesclado.

---

## Regra de Ouro: Inviolabilidade do Dado de Origem

Em qualquer ferramenta, parser ou enriquecimento mantido pela BRAN:
- **Nunca invente, extrapole ou deduza valores ausentes na origem.**
- Campos não informados na publicação original devem permanecer estritamente `null` (ou `NA`).
- Detalhes de conformidade estão disponíveis na [Política de Segurança e Governança de Dados (SECURITY.md)](SECURITY.md) e no [Código de Conduta (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md).

---

## Código de Conduta

Ao interagir com a organização (Issues, PRs, fóruns ou formulários), você concorda em seguir nosso [Código de Conduta (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md). Mantemos um ambiente respeitoso, colaborativo e técnico.
