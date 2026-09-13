![BRAN Banner](assets/Branbannerorg.png)

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/Ler%20em-Portugu%C3%AAs-blue.svg?style=for-the-badge" alt="Ler em Português"></a>
  <a href="https://github.com/BRAN-Org"><img src="https://img.shields.io/badge/Databases-2-green?style=for-the-badge&logo=database" alt="Databases"></a>
  <a href="https://www.budapestopenaccessinitiative.org/"><img src="https://img.shields.io/badge/BOAI-Signatory-orange.svg?style=for-the-badge" alt="BOAI Signatory"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-GPLv3%20%7C%20CC%20BY--NC--SA%204.0-blue?style=for-the-badge" alt="GPLv3 | CC BY-NC-SA 4.0 License"></a>
</p>

## About Us & Our Mission
**BRAN Org** (**Brazilian Research Archive Network**) is an independent organization dedicated to building open infrastructure for academic and scientific information in **Brazil**.

We map **academic data that is already public**, but lacks APIs or easy programmatic access. Our work is to collect, clean, and provide this information in open and standardized formats through public APIs and open-source tools, lowering technical barriers for researchers and boosting quantitative studies on Brazilian scientific output.

## Our Goals
- **Map Brazilian Sources**: Identify public academic collections, repositories, and databases that lack programmatic access.
- **Structure Public Data**: Convert raw or fragmented data into clean, standardized formats ready for analysis.
- **Create Open APIs**: Provide public, accessible endpoints for integration into research and software.
- **Develop Tools**: Build open-source packages and applications focused on quantitative scientific analysis.

## Our Projects

### Databases & Collections

Public catalog of bibliometric databases from Brazilian scientific output, provided in open formats (`JSON`/`CSV`), featuring a free REST API and interactive dashboard for analysis.

| Repository | Official Event | Records | Data Reliability |
| :--- | :--- | :---: | :---: |
| [abec-open-database](https://github.com/BRAN-Org/abec-open-database) | [ABEC Meeting](https://www.abecbrasil.org.br/) | **259 Articles** (2013-2025) | [🟠 In Curation](#-data-reliability-levels) |
| [ebbc-open-database](https://github.com/BRAN-Org/ebbc-open-database) | [EBBC](https://ebbc.ibict.br/) | **643 Articles** (2012-2024) | [🟡 Source Faithful (Limitations)](#-data-reliability-levels) |

<details>
<summary><b>Data Reliability Levels</b></summary>
<br>

To ensure academic transparency and scientific rigor, every **BRAN Org** dataset features a data reliability tier:

- 🟢 **Green (100% Audited & Complete)**: Fully extracted, validated, and sanitized. Contains all fundamental metadata (title, authors, affiliations, abstracts, DOIs, and PDF links) without known structural gaps.
- 🔵 **Blue (High Fidelity with Sparse Source Omissions)**: Complete coverage of editions/years and DOIs, containing only rare metadata gaps inherited directly from the official website in specific editions.
- 🟡 **Yellow (100% Faithful to Source with Native Limitations)**: 100% of articles available online on the official website were extracted without loss, but the official source presents native limitations (e.g., lack of DOIs in proceedings or missing early historical proceedings not digitized online). *(Ex: `ebbc-open-database`)*.
- 🟠 **Orange (In Curation / Processing)**: Extraction completed successfully, but the collection is undergoing curation, schema validation, and metadata sanitation. *(Ex: `abec-open-database`)*.
- 🔴 **Red (Unaudited Data / Low Reliability)**: Unaudited raw records or high incidence of extraction errors. Requires caution for direct analytical use.

</details>



## How to Contribute
We invite researchers, developers, and open science enthusiasts to collaborate with us:
- **Suggest Data Sources**: Know a public Brazilian academic dataset that needs an API? [Submit your suggestion via Google Form](https://forms.google.com/sua-url-de-sugestao-aqui).
- **Develop & Improve**: Collaborate on building and improving our open-source APIs and tools on GitHub.
- **Open Issues**: Send feedback, report bugs, or share ideas directly in our repositories.
- **Share**: Spread the word about our open tools to the research community.

## Principles
Our work is guided by international Open Science principles and declarations:

- **[FAIR Principles](https://www.go-fair.org/fair-principles/)**: Commitment to making data **Findable, Accessible, Interoperable, and Reusable**.
- **[Budapest Open Access Initiative (BOAI)](https://www.budapestopenaccessinitiative.org/)**: Alignment with landmark Open Access guidelines advocating for free use, distribution, and reuse of scientific knowledge.
- **Scientific Data Protection (CC BY-NC-SA 4.0)**: Free access for non-commercial academic research, with explicit restrictions against scraping/ingestion for commercial AI model training.
- **Open Source & Copyleft (GPLv3)**: Keeping our codebase 100% open under GNU GPLv3, ensuring derived tools remain open source.
- **Transparency**: Open and auditable workflows for data collection, cleaning, and documentation.

## Contact
- **Contact Form**: [Send us a message via Google Form](https://forms.google.com/sua-url-de-contato-aqui)
- **Email**: [gabrielngama@gmail.com](mailto:gabrielngama@gmail.com)
- **GitHub**: [BRAN-Org](https://github.com/BRAN-Org)
- Questions or suggestions? Open an [Issue](https://github.com/BRAN-Org/.github/issues) in our repository.
