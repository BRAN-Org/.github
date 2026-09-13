![BRAN Banner](assets/f2cb99aa-7e97-4e88-9a6c-eb55d56cd888.png)

<p align="center">
  <a href="README.en.md"><img src="https://img.shields.io/badge/Read%20in-English-blue.svg?style=for-the-badge" alt="Read in English"></a>
  <a href="https://github.com/BRAN-Org"><img src="https://img.shields.io/badge/Bases%20de%20Dados-2-green?style=for-the-badge&logo=database" alt="Bases de Dados"></a>
  <a href="https://www.budapestopenaccessinitiative.org/"><img src="https://img.shields.io/badge/BOAI-Signatory-orange.svg?style=for-the-badge" alt="BOAI Signatory"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/Licen%C3%A7a-GPLv3%20%7C%20CC%20BY--NC--SA%204.0-blue?style=for-the-badge" alt="Licença GPLv3 | CC BY-NC-SA 4.0"></a>
</p>

👉 **[Quer saber mais sobre a gente, nossa história, missão, objetivos e visão completa? Acesse o nosso ABOUT.md!](ABOUT.md)**

---

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

## 🤝 Participe

Esta comunidade possui um [Código de Conduta](CODE_OF_CONDUCT.md). Você deve segui-lo ao interagir com a comunidade.

- **Para dúvidas ou suporte:** veja o [SUPPORT.md](SUPPORT.md) ou envie uma mensagem através do [Formulário de Contato](https://forms.google.com/sua-url-de-sugestao-aqui).
- **Para ajudar ou contribuir:** veja o [CONTRIBUTING.md](CONTRIBUTING.md).