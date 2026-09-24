# Guia de Membros e Operação Interna — BRAN Org

Este documento estabelece o funcionamento interno, as responsabilidades operacionais e o fluxo de trabalho para os membros da **BRAN Org**. Nosso objetivo é manter uma infraestrutura aberta e auditável para dados científicos brasileiros, operando com pragmatismo técnico e sem burocracias corporativas desnecessárias.

---

## 1. Princípios Básicos

Toda atuação de membros na organização é regida por três regras inegociáveis:

1. **Inviolabilidade da Fonte Primária**: Nunca deduza, infira ou preencha metadados ausentes na origem. Se o artigo ou evento não possui DOI, resumo ou afiliação, o campo permanece estritamente `null`.
2. **Coleta Responsável e Ética**: Scripts de extração devem operar com *rate limit* mínimo de 1.5 a 2.0 segundos entre requisições e utilizar o `User-Agent` oficial (`BRAN-Org-Harvester/1.0 (+https://github.com/BRAN-Org)`).
3. **Auditabilidade e Reprodutibilidade**: Nenhuma base de dados entra em produção sem manifesto de proveniência (`provenance.json`), validação de integridade criptográfica e aprovação em schema JSON Schema.

---

## 2. Entrada e Onboarding de Novos Membros

A BRAN não adota processos seletivos corporativos. O ingresso é baseado em contribuição prática, interesse legítimo em ciência aberta e alinhamento com nossas diretrizes técnicas.

### Como funciona o ingresso:
1. **Primeiro Contato / Contribuição Inicial**: O colaborador demonstra interesse abrindo uma Issue técnica, propondo uma correção auditada de dados ou enviando um PR em repositórios abertos (como templates ou scripts auxiliares).
2. **Convite para a Organização**: Membros ativos podem convidar colaboradores que demonstraram consistência técnica e respeito às regras de coleta/sanitização.
3. **Passo a Passo de Onboarding**:
   - Leitura obrigatória deste guia, do `CONTRIBUTING.md` e do `ABOUT.md`.
   - Configuração do ambiente local com Python 3.10+, Node.js (se aplicável) e as ferramentas de validação de schema (`scripts/validate_data.py`).
   - Acesso inicial concedido com permissão de escrita focada em branches de desenvolvimento (`development`) ou repositórios específicos em fase de curadoria.

---

## 3. Papéis e Responsabilidades

Na BRAN, papéis não são cargos hierárquicos rígidos, mas sim frentes de atuação que qualquer membro pode assumir conforme a demanda e disponibilidade:

### 3.1. Desenvolvimento e Engenharia de Ferramentas
- **O que faz**: Constrói e mantém scrapers, scripts de extração (OAI-PMH, PDFs via GROBID/pdfplumber, páginas HTML), pipelines de sanitização e APIs de visualização.
- **Responsabilidades**:
  - Garantir que extratores tratem falhas de rede, timeouts e formatos corrompidos com elegância.
  - Escrever código legível, modular e com documentação técnica enxuta (como rodar, variáveis necessárias).
  - Nunca acoplar regras de interface aos repositórios de dados finais; sempre utilizar o repositório de template (`bran-web-database-template`).

### 3.2. Curadoria e Auditoria de Dados (Data Stewards)
- **O que faz**: Inspeciona a qualidade dos acervos coletados, verifica anomalias, calcula métricas de cobertura e determina o nível de confiabilidade do repositório.
- **Responsabilidades**:
  - Confrontar amostras de dados extraídos diretamente com os anais e páginas originais do evento.
  - Atualizar o manifesto `provenance.json` com datas de coleta, hashes SHA-256 e contadores de metadados ausentes.
  - Atribuir e revisar a taxonomia de confiabilidade oficial (Verificado e Auditado, Alta Fidelidade, Fiel à Fonte, Em Curadoria, Não Auditado).

### 3.3. Revisão Técnica (Code & Data Review)
- **O que faz**: Avalia Pull Requests de código e de alterações em bases de dados antes do merge em branches principais.
- **Responsabilidades**:
  - **Revisão de Código**: Checar aderência a padrões, ausência de credenciais expostas, respeito ao rate limit e clareza de logs.
  - **Revisão de Dados**: Baixar o branch localmente e rodar a suíte de validação (`python3 scripts/validate_data.py`). Inspecionar o `git diff` para garantir que campos não foram sobrescritos ou apagados indevidamente.
  - Garantir que mensagens de commit sigam o formato Conventional Commits sem ruídos ou mensagens genéricas.

### 3.4. Infraestrutura, Schemas e CI/CD
- **O que faz**: Mantém os workflows de GitHub Actions, validações criptográficas de integridade e a evolução dos contratos de dados (JSON Schemas canônicos).
- **Responsabilidades**:
  - Assegurar que nenhum pipeline de CI silencie erros ou mascare quebras de schema.
  - Manter consistência e versionamento semântico nas definições de schema (`schemas/article.vX.schema.json`).

### 3.5. Triagem e Relação com a Comunidade
- **O que faz**: Monitora Issues abertas pelo público, dúvidas de pesquisadores e relatos de inconsistências em dados.
- **Responsabilidades**:
  - Verificar tecnicamente a procedência de apontamentos de erro enviados pela comunidade.
  - Responder de forma educada, objetiva e transparente, informando se a falha é do extrator ou limitação da própria publicação original.

---

## 4. Como Propor uma Nova Ferramenta ou Base de Dados

Antes de escrever código para um novo projeto ou base, o membro deve abrir uma Issue do tipo **RFC / Proposta** na organização (no repositório `.github` ou no repositório de discussão relevante).

A proposta deve responder a 4 perguntas objetivas:

1. **Origem e Relevância**: Qual é o acervo científico? Ele é público? Por que ele precisa de uma base estruturada ou API aberta (ex: está preso em PDFs não indexados ou em plataforma com navegação precária)?
2. **Viabilidade Técnica**: Qual é a fonte primária (OJS, DSpace, HTML estático)? O volume é tratável? Há risco de bloqueio ou sobrecarga na origem?
3. **Custo de Manutenção**: Trata-se de um evento encerrado (arquivo histórico) ou de um evento recorrente que precisará de novas extrações anuais? Quem será responsável pela curadoria inicial?
4. **Escopo da Ferramenta**: Se for uma nova ferramenta utilitária, ela resolve um problema comum a múltiplos acervos da BRAN ou é algo específico demais? Devemos integrá-la a um repositório existente ou criar um novo?

**Critério de Aprovação**: Pelo menos dois membros ativos devem concordar com a proposta antes da criação de um novo repositório ou início do desenvolvimento pesado. Isso evita "repositórios fantasmas" abandonados após o entusiasmo inicial.

---

## 5. Fluxo de Trabalho Git e Políticas de Branching

Para garantir a estabilidade do catálogo público:

- **Branches Protegidas**: A branch `main` é considerada estável e de produção. Commits diretos na `main` de repositórios de dados ou templates são restritos.
- **Branch `development`**: Todo desenvolvimento e ajuste de dados deve passar pela branch de homologação antes de ir para a `main`.
- **Pull Requests**:
  - Devem conter descrição concisa do que foi alterado.
  - Devem passar com sucesso por todos os checks de CI (`validate_data.py` e asserção criptográfica).
  - Devem conter aprovação de ao menos um revisor independente.
- **Padrão de Commit**: Uso estrito de Conventional Commits (`feat:`, `fix(data):`, `fix(code):`, `docs:`, `chore:`). Proibido mensagens vagas como "update", "fix bug" ou textos inflados gerados por IA.

---

## 6. Comunicação Interna e Conduta

- **Canais**: Discussões de projetos, decisões técnicas e revisões acontecem prioritariamente via Issues, Pull Requests e GitHub Discussions para manter histórico público e auditável. Assuntos pontuais ou coordenação rápida podem ocorrer no canal interno acordado pela equipe.
- **Tom de Comunicação**: Direto, respeitoso e pragmático. Foco na qualidade técnica dos dados e do código.
- **Respeito ao Tempo Alheio**: A BRAN é uma iniciativa mantida por pessoas dedicando seu tempo livre à ciência aberta. Não há cobranças de dedicação exclusiva, mas exige-se transparência com prazos e compromissos assumidos.

---

## 7. Inatividade e Transição Amigável (Offboarding)

- **Avisos de Pausa**: Se um membro precisar se afastar temporariamente por motivos acadêmicos, profissionais ou pessoais, basta comunicar aos demais membros para que tarefas em aberto sejam redistribuídas.
- **Offboarding Sem Atrito**: Membros que decidirem se desligar do projeto são agradecidos em nossa documentação histórica por suas contribuições.
- **Segurança de Acessos**: Membros inativos por mais de 6 meses sem comunicação prévia terão permissões de escrita revogadas por política básica de segurança da organização, podendo ser restabelecidas a qualquer momento mediante retorno.
