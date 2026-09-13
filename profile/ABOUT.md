# Sobre a BRAN Org

## Quem somos e Nossa missão

A **BRAN Org** (**Brazilian Research Archive Network**) é uma organização independente dedicada a construir infraestrutura aberta para a informação acadêmica e científica no **Brasil**.

Mapeamos **dados acadêmicos que já são públicos**, mas que não oferecem APIs ou formas fáceis de acesso programático. Nosso trabalho é coletar, tratar e disponibilizar essas informações em formatos abertos e padronizados, por meio de APIs públicas e ferramentas *open-source*, reduzindo barreiras técnicas para pesquisadores e impulsionando os estudos sobre a produção científica brasileira.

---

## Nossos objetivos

- **Mapear fontes brasileiras**: Identificar acervos, repositórios e bases acadêmicas públicas que carecem de acesso programático.
- **Estruturar dados públicos**: Converter dados brutos ou fragmentados em formatos limpos, padronizados e prontos para análise.
- **Criar APIs abertas**: Disponibilizar endpoints públicos e acessíveis para integração em pesquisas e aplicações.
- **Desenvolver ferramentas**: Construir pacotes e aplicações voltadas à análise quantitativa da produção científica.

---

## Nossos projetos

### Bases de Dados & Acervos

Catálogo público de bases de dados bibliométricos da produção científica brasileira, disponibilizadas em formatos abertos (`JSON`/`CSV`), com API REST gratuita e dashboard interativo para análise.

| Repositório | Evento Oficial | Registros | Confiabilidade |
| :--- | :--- | :---: | :---: |
| [abec-open-database](https://github.com/BRAN-Org/abec-open-database) | [ABEC Meeting](https://www.abecbrasil.org.br/) | **259 Artigos** (2013-2025) | [🟠 Em Curadoria](#-níveis-de-confiabilidade-dos-dados) |
| [ebbc-open-database](https://github.com/BRAN-Org/ebbc-open-database) | [EBBC](https://ebbc.inf.br) | **643 Artigos** (2012-2024) | [🟡 Fiel à Fonte (Limitações)](#-níveis-de-confiabilidade-dos-dados) |

<details>
<summary><b>Níveis de Confiabilidade dos Dados</b></summary>
<br>

Para assegurar transparência acadêmica e rigor científico, cada repositório da **BRAN Org** possui uma marcação de confiabilidade e integridade dos dados:

- 🟢 **Verde (100% Auditado & Completo)**: Dados totalmente extraídos, validados e higienizados. Contém todos os metadados fundamentais (título, autores, afiliações, resumos, DOIs e links para PDF) sem lacunas conhecidas.
- 🔵 **Azul (Alta Fidelidade com Omissões Esparsas da Fonte)**: Cobertura completa de edições/anos e DOIs, contendo apenas raras ausências de metadados herdadas do próprio site oficial em edições específicas.
- 🟡 **Amarelo (100% Fiel à Fonte com Limitações da Origem)**: 100% dos artigos disponibilizados online pelo evento foram extraídos sem perdas, porém a fonte oficial apresenta limitações nativas (ex: ausência de DOIs nos anais do evento ou falta dos primeiros anais históricos que não estão digitalizados online). *(Ex: `ebbc-open-database`)*.
- 🟠 **Laranja (Em Curadoria / Processamento)**: Extração realizada com sucesso, mas o acervo ainda passa por etapas de curadoria, validação de schema e saneamento de metadados. *(Ex: `abec-open-database`)*.
- 🔴 **Vermelho (Dados Não Auditados / Baixa Confiabilidade)**: Registros brutos não auditados ou com alta incidência de falhas de extração. Requer cautela no uso analítico direto.

</details>

---

## Nossa História e Visão

### 1. A Origem do Nome BRAN

Caso você esteja se perguntando sobre a inspiração por trás da sigla **BRAN** (**Brazilian Research Archive Network**), o nome é uma referência a **Brann Bronzebeard**, personagem do jogo *World of Warcraft*.

![Brann Bronzebeard em ação](../assets/brann_bronzebeard_ingame.png)

No jogo, Brann é um arqueólogo e pesquisador dedicado a explorar ruínas esquecidas, resgatar registros históricos e compartilhar suas descobertas abertamente. Essa ideia traduz a nossa missão no mundo real: resgatar acervos e dados acadêmicos brasileiros que estão desestruturados ou esquecidos na web e torná-los acessíveis a todos.

---

### 2. Um Pequeno Passo para a Ciência Brasileira

No cenário científico internacional, pesquisadores e cientistas de dados dispõem de ecossistemas altamente integrados e elegantes para a análise de metadados acadêmicos (como *Crossref*, *OpenAlex*, *Semantic Scholar*, *PubMed* e *Web of Science*). Nesses ambientes, APIs REST robustas, esquemas estruturados em JSON e identificadores persistentes (DOIs) são o padrão estabelecido.

No **Brasil**, porém, existe um contraste desafiador. Embora periódicos de grande porte possuam boa indexação, uma parte vital do conhecimento produzido no país permanece em um vácuo de infraestrutura tecnológica:

* **Anais de Eventos e Congressos**: Milhares de conferências e simpósios nacionais publicam seus anais em páginas estáticas, portais legados ou PDFs isolados, desprovidos de padronização, DOIs ou acesso programático.
* **Periódicos Regionais e Institucionais**: Revistas científicas de menor porte enfrentam severas barreiras orçamentárias e técnicas para implementar e manter plataformas modernas de metadados.

A **BRAN Org** surge para dar um passo concreto no fortalecimento desse ecossistema, atuando em duas frentes complementares:

1. **Estruturação e Rastreabilidade para Eventos e Revistas**: Oferecemos suporte a organizadores e editores regionais ao converter acervos desestruturados em dados limpos, padronizados e com preservação digital assegurada.
2. **Acessibilidade Direta para Pesquisa Científica**: Eliminamos a necessidade de construir *scrapers* complexos e manuais, fornecendo aos pesquisadores de bibliometria e cientometria bases abertas (`JSON`/`CSV`) e APIs REST gratuitas para análise imediata da produção acadêmica nacional.

---

### 3. Olhando Além dos Grandes: O Complemento às Plataformas Nacionais (Ex: Projeto Laguna)

Grandes iniciativas de infraestrutura científica no Brasil — como a **Plataforma Lattes**, o sistema **Sucupira/CAPES**, o **BDTD/IBICT** ou o **Projeto Laguna** — cumprem um papel fundamental na centralização dos currículos de pesquisadores, no acompanhamento da pós-graduação e no mapeamento de periódicos de alto impacto.

Contudo, devido ao escopo massivo e às prioridades institucionais desses grandes portais, parcelas expressivas da memória científica brasileira acabam ficando à margem do sistema:

* **Produção Regional e Acadêmica Inicial**: Trabalhos apresentados em congressos regionais, encontros de iniciação científica (PIBIC) e simpósios de sociedades acadêmicas locais raramente integram os indexadores centrais.
* **Acervos Históricos e "Órfãos"**: Edições históricas de eventos que mudaram de domínio ou cujas comissões organizadoras se desfizeram ao longo dos anos.

A atuação da **BRAN Org** é estritamente simbiótica. Não buscamos concorrer com as grandes plataformas nacionais, mas sim **resgatar, organizar e preservar a literatura acadêmica que fica de fora dos grandes portais** — garantindo que a pesquisa regional, emergente e histórica do Brasil tenha a visibilidade, a organização e a rastreabilidade que merece.

---

### 4. O Horizonte: Preparando o Terreno para a Unificação de Dados no Brasil

Almejamos que o trabalho da **BRAN Org** sirva como base e catalisador para iniciativas ainda maiores no futuro. 

Ao adotar os **Princípios FAIR** (*Findable, Accessible, Interoperable, Reusable*), a **Declaração BOAI** e licenças estritamente abertas, estamos construindo uma infraestrutura modular e interoperável. Nosso horizonte é preparar a informação acadêmica brasileira para integrar ou fundamentar **projetos nacionais mais amplos de unificação de bases de dados científicos**, conectando ilhas de informação em uma rede coesa, transparente e soberana de conhecimento aberto.
