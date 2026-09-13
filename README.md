![BRAN Banner](assets/Branbannerorg.png)

<p align="center">
  <a href="README.en.md"><img src="https://img.shields.io/badge/Read%20in-English-blue.svg?style=for-the-badge" alt="Read in English"></a>
  <a href="https://github.com/BRAN-Org"><img src="https://img.shields.io/badge/Bases%20de%20Dados-2-green?style=for-the-badge&logo=database" alt="Bases de Dados"></a>
  <a href="https://www.budapestopenaccessinitiative.org/"><img src="https://img.shields.io/badge/BOAI-Signatory-orange.svg?style=for-the-badge" alt="BOAI Signatory"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licen%C3%A7a-GPLv3%20%7C%20CC%20BY--NC--SA%204.0-blue?style=for-the-badge" alt="Licença GPLv3 | CC BY-NC-SA 4.0"></a>
</p>

## Quem somos e Nossa missão
A **BRAN Org** é uma organização independente dedicada a construir infraestrutura aberta para a informação acadêmica e científica no **Brasil**.

Mapeamos **dados acadêmicos que já são públicos**, mas que não oferecem APIs ou formas fáceis de acesso programático. Nosso trabalho é coletar, tratar e disponibilizar essas informações em formatos abertos e padronizados, por meio de APIs públicas e ferramentas *open-source*, reduzindo barreiras técnicas para pesquisadores e impulsionando os estudos sobre a produção científica brasileira.

## Nossos objetivos
- **Mapear fontes brasileiras**: Identificar acervos, repositórios e bases acadêmicas públicas que carecem de acesso programático.
- **Estruturar dados públicos**: Converter dados brutos ou fragmentados em formatos limpos, padronizados e prontos para análise.
- **Criar APIs abertas**: Disponibilizar endpoints públicos e acessíveis para integração em pesquisas e aplicações.
- **Desenvolver ferramentas**: Construir pacotes e aplicações voltadas à análise quantitativa da produção científica.

## Nossos projetos

### Bases de Dados & Acervos

| Repositório | Evento Oficial | Registros | Confiabilidade |
| :--- | :--- | :---: | :---: |
| [abec-open-database](https://github.com/BRAN-Org/abec-open-database) | [ABEC Meeting](https://www.abecbrasil.org.br/) | **259 Artigos** (2013-2025) | [🟠 Em Curadoria](#-níveis-de-confiabilidade-dos-dados) |
| [ebbc-open-database](https://github.com/BRAN-Org/ebbc-open-database) | [EBBC](https://ebbc.ibict.br/) | **643 Artigos** (2012-2024) | [🟡 Fiel à Fonte (Limitações)](#-níveis-de-confiabilidade-dos-dados) |

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



## Como contribuir
Convidamos pesquisadores, desenvolvedores e entusiastas da ciência aberta a colaborar conosco:
- **Sugerir fontes de dados**: Conhece uma base acadêmica brasileira pública que precisa de uma API? [Envie sua sugestão pelo formulário](https://forms.google.com/sua-url-de-sugestao-aqui).
- **Desenvolver e aprimorar**: Colaborar no desenvolvimento das nossas APIs e ferramentas no GitHub.
- **Abrir Issues**: Enviar feedbacks, correções de bugs ou idéias diretamente nos nossos repositórios.
- **Divulgar**: Compartilhar nossas ferramentas com pesquisadores e a comunidade acadêmica.

## Princípios
Nossa atuação é guiada pelos princípios e declarações internacionais de Ciência Aberta:

- **[Princípios FAIR](https://www.go-fair.org/fair-principles/)**: Compromisso em disponibilizar dados **Localizáveis, Acessíveis, Interoperáveis e Reutilizáveis** (*Findable, Accessible, Interoperable, Reusable*).
- **[Budapest Open Access Initiative (BOAI)](https://www.budapestopenaccessinitiative.org/)**: Alinhamento com as diretrizes históricas de Acesso Aberto para o livre uso, distribuição e reutilização do conhecimento científico.
- **Proteção dos Dados Científicos (CC BY-NC-SA 4.0)**: Acesso livre para pesquisa acadêmica não-comercial, com restrição expressa contra raspagem/ingestão para treino comercial de modelos de Inteligência Artificial sem autorização.
- **Software Livre & Copyleft (GPLv3)**: Código-fonte 100% aberto sob a licença GNU GPLv3, garantindo que qualquer melhoria ou ferramenta derivada permaneça aberta.
- **Transparência**: Processos de coleta, tratamento e documentação abertos e auditáveis pela comunidade.

## Contato
- **Formulário de Contato**: [Envie uma mensagem pelo formulário](https://forms.google.com/sua-url-de-contato-aqui)
- **E-mail**: [gabrielngama@gmail.com](mailto:gabrielngama@gmail.com)
- **GitHub**: [BRAN-Org](https://github.com/BRAN-Org)
- Dúvidas ou sugestões? Abra uma [Issue](https://github.com/BRAN-Org/.github/issues) em nosso repositório.