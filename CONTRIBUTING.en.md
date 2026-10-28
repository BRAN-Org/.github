# Contributing Guide — BRAN Org

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Leia%20em-Portugu%C3%AAs-green.svg?style=for-the-badge" alt="Leia em Português"></a>
</p>

Thank you for your interest in contributing to **BRAN Org** (**Brazilian Research Archive Network**). Our mission is to recover, structure, and preserve Brazilian scientific and bibliometric memory under the principles of open science, transparency, and public utility.

The entire academic and technical community—researchers, librarians, data scientists, and software engineers—is welcome to contribute.

---

## Automated Governance: CRONA and BRAN Bots

The organization operates two official bots to preserve scientific integrity and manage lifecycle operations:

- **CRONA (`@crona-bot`)**: Guardian of academic dataset repositories (`*-open-database`) and temporal governance (`calendar_config`). Runs DOI resolution audits, strict JSON schema validation, daily calendar updates, and continuous provenance tracking. Operational manual available at [CRONA.md](CRONA.md).
- **BRAN (`@bran-bot`)**: Guardian of software and infrastructure repositories (`bibliolatam`, `schemas`, templates, and tools). Manages automated testing, Conventional Commits linting, and template synchronizations.

---

## Ways to Contribute

### 1. Data Inconsistency Reporting & Corrections
If you identify a data error, truncated title, missing DOI, or divergence from the primary source in one of our open datasets:

1. Navigate to the dataset repository (e.g., [`ebbc-open-database`](https://github.com/BRAN-Org/ebbc-open-database) or [`abec-open-database`](https://github.com/BRAN-Org/abec-open-database)).
2. Open an **Issue** specifying the discrepancy and **provide the official primary source URL** where the correct record is published.
3. **Data Pull Request Policy**: To preserve scientific integrity and rigorous provenance tracking (`provenance.json`), dataset repositories **do not accept direct data modifications via external fork Pull Requests**. Any external PR modifying data files is automatically closed by **CRONA**, directing the contributor to open an Issue for canonical curation.

### 2. Internal Curation Workflow (Maintainers and Curators)
For curators submitting new proceedings or corrections on internal organization branches:
- **Tier 1 (Fatal Error)**: If the JSON file contains syntax errors (malformed syntax), CRONA interrupts the pipeline and requests syntax fixes.
- **Tier 2 (Schema Inconsistencies)**: If required fields are missing or out of specification, CRONA submits an inline **Code Review** with comments directly on the affected lines in the PR.
- **Tier 3 (Automatic Approval)**: If structure and schema are 100% compliant, CRONA submits a formal **`APPROVE`** review on the PR along with the DOI integrity summary (without blocking for broken upstream DOIs). Maintainers can then proceed with the merge.

### 3. Suggesting & Submitting New Proceedings / Datasets
If you organize an academic conference, represent a scientific society, or possess historical proceedings at risk of link rot:

- Submit proceedings details through the **[Dataset Submission Form](https://forms.gle/jNBuP1mjyUXc6v1fA)**.
- Or start a discussion via **[.github Issues](https://github.com/BRAN-Org/.github/issues)** outlining the event, estimated paper count, and source URLs.

### 4. Code & Tooling Contributions
We build open-source software, analyzers, and libraries (such as the [`bibliolatam`](https://github.com/BRAN-Org/bibliolatam) package, the [`schemas`](https://github.com/BRAN-Org/schemas) repository, and database web templates). Pull requests are very welcome in these projects.

#### Code Contribution Workflow:
1. Fork the respective repository.
2. Create a feature branch (`git checkout -b feature/my-enhancement` or `git checkout -b fix/bug-description`).
3. Add or update automated test suites covering your changes.
4. Use concise Conventional Commits:
   - `feat:` new feature or parser.
   - `fix:` bugfix in existing routine.
   - `docs:` documentation improvements.
   - `test:` test suite updates.
5. **BRAN Bot** will validate commit formats and run test suites (`testthat`/`pytest`). Once green, your PR will be reviewed and merged.

---

## Golden Rule: Source Data Inviolability

Across all tools, parsers, and enrichments:
- **Never infer, guess, or invent values missing from the primary source.**
- Fields not provided in the original publication must strictly remain `null` (or `NA`).
- Compliance details are available in our [Data Security Policy (SECURITY.en.md)](SECURITY.en.md) and [Code of Conduct (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md).

---

## Code of Conduct

All interactions across issues, pull requests, and discussions are governed by our [Code of Conduct (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md). We maintain a respectful, welcoming, and technical environment.
