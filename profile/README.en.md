![BRAN Banner](https://raw.githubusercontent.com/BRAN-Org/.github/main/assets/f2cb99aa-7e97-4e88-9a6c-eb55d56cd888.png)

<p align="center">
 <a href="README.md"><img src="https://img.shields.io/badge/Ler%20em-Portugu%C3%AAs-blue.svg?style=for-the-badge" alt="Ler em Português"></a>
 <a href="https://github.com/BRAN-Org"><img src="https://img.shields.io/badge/Databases-2-green?style=for-the-badge&logo=database" alt="Databases"></a>
 <a href="https://www.budapestopenaccessinitiative.org/"><img src="https://img.shields.io/badge/BOAI-Signatory-orange.svg?style=for-the-badge" alt="BOAI Signatory"></a>
 <a href="../LICENSE"><img src="https://img.shields.io/badge/License-GPLv3%20%7C%20CC%20BY--NC--SA%204.0-blue?style=for-the-badge" alt="GPLv3 | CC BY-NC-SA 4.0 License"></a>
</p>

<p align="center">
 <b>BRAN Org</b> (Brazilian Research Archive Network) is an independent data infrastructure collective dedicated to rescuing, standardizing, and preserving Brazilian scientific proceedings and collections through open data, public REST APIs, and auditable canonical schemas.
</p>

<p align="center">
 <b><a href="https://github.com/BRAN-Org/.github/blob/main/ABOUT.en.md">Learn more about our story, mission, and vision in ABOUT.en.md</a></b>
</p>

---

### Databases & Collections

Public catalog of bibliometric databases from Brazilian scientific output, provided in open formats (`JSON`/`CSV`), featuring a free REST API and interactive dashboard for analysis.

| Repository | Official Event | Records | Data Reliability |
| :--- | :--- | :---: | :---: |
| [abec-open-database](https://github.com/BRAN-Org/abec-open-database) | [ABEC Meeting](https://www.abecbrasil.org.br/) | **259 Articles** (2013-2025) | [🟠 Under Investigation](#-data-reliability-levels) |
| [ebbc-open-database](https://github.com/BRAN-Org/ebbc-open-database) | [EBBC](https://ebbc.inf.br) | **643 Articles** (2012-2024) | [🟡 Faithful to Source (Incomplete Coverage)](#-data-reliability-levels) |

<details>
<summary><b>Data Reliability Levels</b></summary>
<br>

To ensure academic transparency and methodological rigor, each **BRAN Org** dataset receives an explicit reliability classification:

- 🟢 **Audited & Validated**: Data audited and formally validated in collaboration with official event organizers or organizing committee.
- 🟡 **Faithful to Source / Incomplete Coverage**: The dataset faithfully mirrors all public records available on the official site, but the original collection contains known gaps (e.g. non-digitized historical proceedings, absent DOIs at the source, or missing editions). *(Ex: `ebbc-open-database`)*.
- 🟠 **Under Investigation**: Extracted data actively undergoing technical integrity audits, curation, or awaiting formal responses from the organizing institution. *(Ex: `abec-open-database`)*.
- 🔴 **Unaudited**: Raw or newly extracted datasets that have not yet undergone integrity checks.

> **Official Methodological Note:** 
> *BRAN strictly preserves primary source fidelity and never hallucinates missing information. Gaps and anomalies found on official portals are documented in audit logs and addressed through active investigation and direct contact with organizing institutions.*

</details>

---

### Standards, Schemas & Tools

Beyond bibliometric collections, we maintain canonical standards and open-source tooling for research infrastructure:

| Repository | Type | Description |
| :--- | :--- | :--- |
| [schemas](https://github.com/BRAN-Org/schemas) | JSON Standards | Canonical v1 schemas (`article`, `provenance`, `event`) with automated CI validation. |
| [bibliolatam](https://github.com/BRAN-Org/bibliolatam) | Python/R Library | Normalization, cleaning, and parsing of Latin American bibliographic metadata. |
| [bran-web-database-template](https://github.com/BRAN-Org/bran-web-database-template) | Template & API | Reference architecture for deploying public REST APIs and dashboards with zero external runtime dependencies. |

---

## Get Involved

This community has a [Code of Conduct](https://github.com/BRAN-Org/.github/blob/main/CODE_OF_CONDUCT.md). You must follow it when interacting with the community.

- **For questions or support:** see [SUPPORT.en.md](https://github.com/BRAN-Org/.github/blob/main/SUPPORT.en.md) or send a message via our [Contact Form](https://forms.gle/qhVXZpaRo26MLuUm8).
- **To help or contribute:** see [CONTRIBUTING.en.md](https://github.com/BRAN-Org/.github/blob/main/CONTRIBUTING.en.md).
- **To submit datasets or collections:** fill out the [Dataset Submission Form](https://forms.gle/jNBuP1mjyUXc6v1fA).
