# Contributing Guide — BRAN Org

<p align="center">
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/Leia%20em-Portugu%C3%AAs-green.svg?style=for-the-badge" alt="Leia em Português"></a>
</p>

Thank you for your interest in contributing to **BRAN Org** (**Brazilian Research Archive Network**). Our mission is to recover, structure, and preserve Brazilian scientific and bibliometric memory under the principles of open science, transparency, and public utility.

The entire academic and technical community—researchers, librarians, data scientists, and software engineers—is welcome to contribute.

---

## Ways to Contribute

### 1. Data Inconsistency Reporting & Corrections

If you identify a data error, truncated title, missing DOI, or divergence from the primary source in one of our open datasets:

1. Navigate to the dataset repository (e.g., [`ebbc-open-database`](https://github.com/BRAN-Org/ebbc-open-database) or [`abec-open-database`](https://github.com/BRAN-Org/abec-open-database)).
2. Open an **Issue** specifying the discrepancy and **provide the official primary source URL** where the correct record is published.
3. *Notice regarding dataset Pull Requests*: To preserve scientific integrity and rigorous provenance tracking (`provenance.json`), dataset repositories do not accept arbitrary direct file modifications via external PRs. Verified corrections are audited and applied by maintainers against primary sources.

### 2. Suggesting & Submitting New Proceedings / Datasets

If you organize an academic conference, represent a scientific society, or possess historical proceedings at risk of link rot:

- Submit proceedings details through the **[Dataset Submission Form](https://forms.gle/jNBuP1mjyUXc6v1fA)**.
- Or start a discussion via **[.github Issues](https://github.com/BRAN-Org/.github/issues)** outlining the event, estimated paper count, and source URLs.

### 3. Code & Tooling Contributions

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
5. Submit a Pull Request detailing the changes, the problem solved, and verification output.

---

## Golden Rule: Source Data Inviolability

Across all tools, parsers, and enrichments:
- **Never infer, guess, or invent values missing from the primary source.**
- Fields not provided in the original publication must strictly remain `null` (or `NA`).
- Compliance details are available in our [Data Security Policy (SECURITY.en.md)](SECURITY.en.md) and [Code of Conduct (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md).

---

## Code of Conduct

All interactions across issues, pull requests, and discussions are governed by our [Code of Conduct (CODE_OF_CONDUCT.md)](CODE_OF_CONDUCT.md). We maintain a respectful, welcoming, and technical environment.
