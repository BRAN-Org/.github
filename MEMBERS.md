# Guia de Membros e Governança Técnica — BRAN Org

Este documento estabelece o funcionamento interno, a divisão de papéis e o fluxo de trabalho para os membros da **BRAN Org**. 

A BRAN não se limita a acervos e APIs: desenvolvemos ferramentas, bibliotecas, utilitários CLI, sistemas web e infraestrutura aberta de software, além de manter projetos dedicados à preservação, integridade e acesso à produção científica brasileira. Operamos com engenharia pragmática, rigor técnico e sem burocracias corporativas desnecessárias.

---

## 1. Princípios Operacionais

Toda contribuição e projeto sob o guarda-chuva da organização deve respeitar três pilares:

1. **Rigor e Reprodutibilidade**: Todo software, ferramenta ou pipeline desenvolvido deve ser testável, modular e reproduzível localmente, com documentação clara de setup e dependências.
2. **Inviolabilidade do Dado e da Verdade**: Em projetos que envolvem dados e metadados, nunca deduza, infira ou invente valores ausentes na fonte de origem. Campos inexistentes na origem permanecem estritamente `null`.
3. **Auditabilidade e Segurança**: Nenhuma ferramenta ou base de dados é promovida a release sem validação empírica de integridade, testes automatizados e aprovação técnica.

---

## 2. Estrutura de Papéis e Responsabilidades

Na BRAN, as responsabilidades são divididas de forma objetiva entre mantedores, desenvolvedores e auditores. Novos membros ingressam com escopo delimitado, enquanto a infraestrutura crítica e governança de bibliotecas centrais permanecem sob membros pontuais:

### 2.1. Mantedores Principais de Projetos (Core Maintainers)
- **Escopo**: Liderança técnica e arquitetural de ferramentas, bibliotecas ou repositórios específicos da organização.
- **Responsabilidades**:
  - Definir arquitetura técnica, padrões de design e gestão de dependências do repositório.
  - Autoridade para aprovação final de Pull Requests e merge na branch `main`.
  - Gerenciamento de releases, versionamento semântico (SemVer) e changelogs.
  - Manutenção e guarda de credenciais, configurações globais e infraestrutura de CI/CD.
  - Acesso e manutenção de bibliotecas estruturais e ferramentas compartilhadas da organização cabem exclusivamente a mantedores pontuais autorizados.

### 2.2. Desenvolvedores (Software Engineers / Tool Developers)
- **Escopo**: Engenharia, construção e evolução de ferramentas, CLIs, bibliotecas, APIs, automações e aplicações web.
- **Responsabilidades**:
  - Desenvolver funcionalidades de ponta a ponta com código legível, modular e resiliente a falhas (ex: tratamento robusto de timeouts, erros de rede e formatos corrompidos).
  - Escrever documentação técnica enxuta orientada a desenvolvedores (como executar, variáveis de ambiente, exemplos práticos de uso).
  - Garantir cobertura de testes para fluxos críticos antes de submeter alterações.
  - Atuar em branches de desenvolvimento (`development` ou feature branches), sem intervenção direta em produção.

### 2.3. Auditores Técnicos e de Integridade (Technical & Data Auditors)
- **Escopo**: Averiguação, auditoria empírica de qualidade, conformidade de schemas, segurança e integridade de acervos e código.
- **Responsabilidades**:
  - **Auditoria de Código**: Verificar aderência aos padrões técnicos, higiene do código, ausência de credenciais expostas e boas práticas de segurança.
  - **Auditoria de Dados e Acervos**: Confrontar amostras com fontes primárias, verificar consistência contra schemas canônicos (`scripts/validate_data.py`), auditar manifestos de proveniência (`provenance.json`) e garantir ausência de dados deduzidos.
  - Têm autoridade técnica para reprovar ou solicitar correções em qualquer PR que apresente inconsistências ou viole critérios de validação.

### 2.4. Novos Membros e Escopo Inicial
- **Escopo**: Ingressam com escopo delimitado e permissões restritas.
- **Responsabilidades**:
  - Atuam sob a orientação de mantedores em repositórios específicos ou branches de desenvolvimento.
  - Não possuem acesso direto a chaves de publicação de bibliotecas, configurações de infraestrutura ou permissão de merge direto na `main`.
  - A ampliação de responsabilidades ocorre de forma gradual conforme a consistência das entregas técnicas.

---

## 3. Entrada e Onboarding de Novos Membros

A admissão formal como membro da organização não é automática nem aberta a qualquer contribuição casual. Pequenas correções, ajustes pontuais de documentação ou sugestões devem ser feitos externamente via Pull Requests, Issues ou discussões públicas.

### Critérios de Ingresso:
1. **Capacidade Técnica Comprovada**: Novos membros devem ser previamente apurados e demonstrar capacidade real de realizar contribuições significativas e contínuas para ferramentas, código ou auditoria da organização.
2. **Avaliação Prévia**: A entrada exige histórico de contribuições sólidas e alinhamento prático com os princípios de software livre, integridade e rigor técnico da BRAN Org.
3. **Responsabilidades Limitadas no Ingresso**: Membros recém-admitidos recebem permissões focadas na sua frente de atuação imediata (ex: branches `development` de projetos em andamento). Gestão de acessos globais, ferramentas críticas e bibliotecas nucleares permanecem sob a tutela de membros pontuais.
4. **Passo a Passo de Onboarding**:
   - Leitura deste guia, do `CONTRIBUTING.md` e da documentação técnica do projeto em que for atuar.
   - Configuração do ambiente local de desenvolvimento e suítes de validação/testes.
   - Alinhamento inicial com o mantenedor principal do projeto de destino.

---

## 4. Como Propor uma Nova Ferramenta ou Projeto

Membros podem propor novas ferramentas, bibliotecas, utilitários ou novas bases abrindo uma Issue do tipo **RFC / Proposta de Projeto** no repositório correspondente ou no repositório `.github`.

A proposta técnica deve responder a 4 pontos objetivos:

1. **Problema e Propósito**: Qual é a dor ou necessidade real que essa ferramenta/projeto resolve? Por que deve fazer parte do ecossistema da BRAN Org?
2. **Arquitetura e Viabilidade**: Qual stack, bibliotecas e dependências serão adotadas? Como será a interface (CLI, biblioteca, API, web)? Há riscos de manutenção ou gargalos técnicos?
3. **Liderança e Manutenção**: Quem atuará como mantenedor principal responsável pela sustentabilidade do projeto? É uma ferramenta estável de escopo fechado ou demandará evolução contínua?
4. **Modularidade e Reuso**: A ferramenta atende a múltiplos projetos da organização ou resolve uma dor comum a outros pesquisadores e desenvolvedores? Ela pode ser publicada como pacote reutilizável?

---

## 5. Fluxo de Trabalho Git e Políticas de Release

- **Branching**:
  - `main`: Estável, reflete a versão em produção ou release oficial. Commits diretos são bloqueados.
  - `development` / feature branches: Onde o desenvolvimento ativo acontece.
- **Pull Requests**:
  - Devem conter descrição técnica clara do problema resolvido e das alterações realizadas.
  - Devem passar com 100% de sucesso nos workflows de CI (testes unitários, linting, asserções criptográficas e schemas).
  - Devem receber aprovação de ao menos um mantenedor ou auditor responsável.
- **Padrão de Commit**: Uso estrito de Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`). Proibido mensagens genéricas ou textos de IA.

---

## 6. Comunicação Interna e Conduta

- **Canais**: Decisões de design, RFCs e discussões de arquitetura devem ser registradas em Issues, Pull Requests ou GitHub Discussions para manter rastreabilidade histórica.
- **Postura**: Direta, focada na solução técnica e respeitosa. O foco é a qualidade do software e a utilidade dos projetos entregues.
- **Transparência de Tempo**: Como projeto comunitário, valorizamos a comunicação clara sobre disponibilidade e entregas assumidas.

---

## 7. Inatividade e Transição Amigável (Offboarding)

- **Comunicação de Pausas**: Se precisar se afastar temporariamente por motivos pessoais, acadêmicos ou profissionais, comunique aos mantenedores para redistribuição de frentes.
- **Offboarding Sem Atrito**: Membros que se desligam da organização têm suas contribuições reconhecidas no histórico dos projetos.
- **Segurança Operacional**: Contas inativas por mais de 6 meses sem comunicação prévia terão permissões de escrita revogadas preventivamente, podendo ser reativadas mediante retorno.
