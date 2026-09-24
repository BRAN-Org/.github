# Member Guide & Internal Operations — BRAN Org

This document defines internal operations, technical responsibilities, and workflows for members of **BRAN Org**. Our goal is to maintain an open and auditable infrastructure for Brazilian scientific data, operating with technical pragmatism and avoiding unnecessary corporate overhead.

---

## 1. Core Principles

All member activities within the organization are governed by three non-negotiable rules:

1. **Inviolability of Primary Sources**: Never guess, deduce, or artificially populate missing metadata from the origin. If an article or event lacks a DOI, abstract, or affiliation, the field must remain strictly `null`.
2. **Responsible & Ethical Scraping**: Extraction scripts must operate with a minimum rate limit of 1.5 to 2.0 seconds between requests and use the official `User-Agent` (`BRAN-Org-Harvester/1.0 (+https://github.com/BRAN-Org)`).
3. **Auditability & Reproducibility**: No dataset reaches production without a provenance manifest (`provenance.json`), cryptographic integrity validation, and passing schema checks against canonical JSON Schemas.

---

## 2. Onboarding New Members

Formal membership in the organization is neither automatic nor open to casual contributions. Minor or sporadic contributions (small fixes, metadata adjustments, or suggestions) should be made externally via Pull Requests, Issues, or submission forms.

### Membership Criteria:
1. **Significant Contribution Capacity**: Prospective members must be thoroughly evaluated and demonstrate proven technical capability to deliver substantial, continuous contributions aligned with BRAN Org's methodology.
2. **Prior Assessment**: Membership requires verification of technical track record, adherence to organizational practices, and unyielding commitment to ethical scraping and data integrity.
3. **Limited Initial Responsibilities**: New members join with a deliberately restricted scope and limited permissions. Critical responsibilities — such as access management, core infrastructure, release management, and maintaining shared tools and libraries — are exclusively reserved for designated core members.
4. **Onboarding Steps**:
   - Mandatory reading of this guide, `CONTRIBUTING.md`, and `ABOUT.en.md` in the `.github` repo.
   - Local environment setup with Python 3.10+, Node.js (if applicable), and schema validation tools (`scripts/validate_data.py`).
   - Initial write access restricted to development branches (`development`) or specific repositories undergoing active curation.

---

## 3. Roles & Responsibilities

At BRAN, roles represent operational workstreams. New members operate with limited responsibilities, while maintenance of core tools, libraries, and infrastructure remains strictly under designated core members:

### 3.1. Tool Engineering & Harvesters
- **Role**: Builds and maintains scrapers, extraction scripts (OAI-PMH, PDFs via GROBID/pdfplumber, HTML pages), sanitization pipelines, and visualization APIs.
- **Responsibilities**:
  - Ensure harvesters gracefully handle network timeouts, drops, and corrupted formats.
  - Write readable, modular code with lean technical documentation (how to run, required variables).
  - Never couple presentation/UI logic into final dataset repositories; always use the base template (`bran-web-database-template`).
  - Access to and maintenance of shared libraries and organization-wide core tools are restricted to authorized core members.

### 3.2. Data Stewardship & Auditing
- **Role**: Inspects collected dataset quality, flags anomalies, calculates coverage metrics, and defines repository reliability levels.
- **Responsibilities**:
  - Audit extracted samples directly against primary proceedings and official event portals.
  - Maintain the `provenance.json` manifest with harvest timestamps, SHA-256 hashes, and missing metadata metrics.
  - Assign and review official reliability tiers (Verified & Audited, High Source Fidelity, Faithful to Source, In Curation, Unaudited).

### 3.3. Technical Review (Code & Data Review)
- **Role**: Reviews code PRs and dataset changes prior to merging into main branches.
- **Responsibilities**:
  - **Code Review**: Verify code hygiene, absence of leaked credentials, rate limiting compliance, and clean logging.
  - **Data Review**: Check out branches locally and execute validation suites (`python3 scripts/validate_data.py`). Inspect `git diff` to ensure fields were not inadvertently overwritten or deleted.
  - Enforce Conventional Commits standards without generic messages.

### 3.4. Infrastructure, Schemas & CI/CD
- **Role**: Maintains GitHub Actions workflows, cryptographic integrity checks, and data contracts (canonical JSON Schemas). This domain is restricted to designated core members.
- **Responsibilities**:
  - Ensure CI pipelines never silence errors or mask schema breaking changes.
  - Maintain semantic versioning and consistency across schema definitions (`schemas/article.vX.schema.json`).

### 3.5. Community Triage & Support
- **Role**: Monitors community Issues, researcher inquiries, and reported data discrepancies.
- **Responsibilities**:
  - Technically investigate reported discrepancies against original sources.
  - Respond politely, objectively, and transparently.

---

## 4. Proposing a New Tool or Dataset (RFC)

Before writing code for a new project or database, members must open an **RFC / Proposal** Issue in the organization (`.github` or the relevant discussion board).

The proposal must answer 4 direct questions:

1. **Source & Significance**: What is the scientific archive? Is it public? Why does it need a structured database or open API (e.g. trapped in non-indexed PDFs or legacy portals)?
2. **Technical Feasibility**: What is the primary source (OJS, DSpace, static HTML)? Is the volume manageable? Is there any risk of downtime or IP blocking?
3. **Maintenance Cost**: Is this a closed historical archive or a recurring annual event requiring updates? Who will lead initial curation?
4. **Tool Scope**: For utility tools, does it solve a recurring challenge across multiple BRAN datasets or is it overly bespoke? Should it be integrated into an existing repo or require a new one?

---

## 5. Git Workflow & Branching Policies

To protect public data catalog stability:

- **Protected Main**: The `main` branch is stable and represents production. Direct commits to `main` on dataset or template repos are restricted.
- **Development Branch**: All development and data updates must pass through `development` prior to merging into `main`.
- **Pull Requests**:
  - Must include a concise summary of changes.
  - Must pass all automated CI checks (`validate_data.py` and cryptographic assertions).
  - Require approval from at least one independent reviewer.
- **Commit Standards**: Strict Conventional Commits (`feat:`, `fix(data):`, `fix(code):`, `docs:`, `chore:`).

---

## 6. Internal Collaboration & Communication

- **Channels**: Project discussions, technical choices, and reviews take place publicly via Issues, Pull Requests, and GitHub Discussions for transparency. Short coordination may occur in designated internal chat spaces.
- **Tone**: Pragmatic, direct, and respectful. Focus on technical data quality and code reliability.
- **Respect for Bandwidth**: BRAN is maintained by volunteers dedicating personal time to open science. We value transparent commitments over arbitrary deadlines.

---

## 7. Inactivity & Friendly Offboarding

- **Stepping Back**: If a member needs to pause due to academic, professional, or personal commitments, a quick heads-up allows the team to reassign tasks without friction.
- **Frictionless Offboarding**: Members choosing to step down remain credited in project records for their contributions.
- **Access Hygiene**: Accounts inactive for over 6 months without prior notice may have write permissions revoked as a standard security precaution, readily restored upon return.
