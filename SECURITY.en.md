# Security Policy & Data Governance — BRAN Org

<p align="center">
  <a href="SECURITY.md"><img src="https://img.shields.io/badge/Leia%20em-Portugu%C3%AAs-green.svg?style=for-the-badge" alt="Leia em Português"></a>
</p>


**BRAN Org** enforces rigorous information security, software integrity, and data protection practices, aligned with international open standards and applicable legislation.

---

## 1. Data Governance & Integrity Principles

Our bibliometric collections and databases operate under formal quality and reproducibility guidelines:

- **FAIR Data Principles (Findable, Accessible, Interoperable, Reusable)**: All datasets are published in open, structured formats (`JSON`/`CSV`) with documented schemas, persistent identifiers, and explicit provenance metadata.
- **Source Inviolability (ISO 8000 / ISO/IEC 25012)**: Datasets strictly mirror public records provided by primary sources. No data is fabricated, guessed, or arbitrarily filled without audit trail documentation.
- **Cryptographic Integrity**: Every dataset release and distribution artifact is validated against canonical schemas and integrity checksums/hashes.

---

## 2. Privacy & Data Protection Compliance (LGPD)

Bibliometric metadata processing across BRAN Org projects complies with the **Brazilian General Data Protection Law (LGPD - Law No. 13,709/2018)**:

- **Strict Academic Public Scope**: Repositories process solely publicly available scientific metadata manifestly made public by authors and original academic events (e.g., author names for scientific attribution, titles, public affiliations, abstracts), pursuant to Arts. 7, § 4 and 11, II, "c" of the LGPD (research and open science activities).
- **Prohibition of Sensitive Data**: Storing personal sensitive data, civil identification numbers (such as CPF/SSN), private contact info (personal phone numbers), or credentials is strictly prohibited.
- **Data Subject Rights Channel**: Researchers wishing to request metadata corrections, affiliation updates, or record removals from BRAN mirrors can contact us directly at: **`gabrielngama@gmail.com`**. Requests are addressed promptly.

---

## 3. Code & Infrastructure Security (ISO/IEC 27001)

- **Secrets Hygiene**: Storing API tokens, credentials, or private keys in Git repositories is strictly prohibited. Automated CI scanners prevent secret leakage.
- **Branch Protection**: Central repositories enforce protected `main` branches requiring automated test pass and technical review.

---

## 4. Responsible Vulnerability Disclosure

If you discover a security vulnerability or accidental exposure in any repository of the organization, please **do not open a public issue**.

Send a confidential report to:
 **[gabrielngama@gmail.com](mailto:gabrielngama@gmail.com)**

### What to include in your report:
1. Clear description and scope of the vulnerability.
2. Reproducible steps or Proof of Concept (PoC).
3. Estimated impact assessment.

All communications are treated confidentially with swift triage and patching.

