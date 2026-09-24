# Member Guide & Technical Governance — BRAN Org

This document outlines internal operations, role distribution, and development workflows for members of **BRAN Org**.

BRAN is not limited to dataset archives and APIs: we engineer tools, software libraries, CLI utilities, web systems, and open software infrastructure, alongside maintaining initiatives dedicated to the preservation, integrity, and accessibility of Brazilian scientific output. We operate with pragmatic engineering, technical rigor, and zero corporate overhead.

---

## 1. Operating Principles

All contributions and projects hosted under the organization must respect three core pillars:

1. **Rigor & Reproducibility**: All software, tools, and pipelines must be testable, modular, and locally reproducible, supported by concise setup instructions and dependency declarations.
2. **Inviolability of Data & Truth**: For initiatives handling scientific records and metadata, never deduce, infer, or hallucinate missing values. Fields not present at the origin must remain strictly `null`.
3. **Auditability & Security**: No tool, library, or dataset reaches production without empirical validation, automated testing, and technical approval.

---

## 2. Roles & Technical Responsibilities

At BRAN, responsibilities are clearly delineated across maintainers, developers, and auditors. New members join with a scoped footprint, while critical infrastructure and core library governance remain under designated core members:

### 2.1. Core Project Maintainers
- **Scope**: Technical and architectural leadership of specific repositories, tools, or libraries within the organization.
- **Responsibilities**:
  - Define technical architecture, design standards, and dependency management.
  - Hold final approval authority on Pull Requests and direct merges into `main`.
  - Oversee semantic versioning (SemVer), releases, and changelogs.
  - Maintain organization-level secrets, deployment keys, and core CI/CD infrastructure.
  - Direct access to and maintenance of shared foundational libraries and tools belong strictly to authorized core maintainers.

### 2.2. Software Engineers & Tool Developers
- **Scope**: End-to-end engineering and evolution of tools, CLIs, libraries, APIs, automation workflows, and web applications.
- **Responsibilities**:
  - Build robust features with readable, modular code resilient to runtime errors (handling timeouts, network partitions, and corrupted data gracefully).
  - Author developer-oriented documentation (how to run, environment variables, reproducible usage examples).
  - Ensure automated test coverage for critical paths prior to PR submission.
  - Operate within feature or `development` branches, without direct write access to production.

### 2.3. Technical & Integrity Auditors
- **Scope**: Rigorous inspection, empirical validation, schema compliance, security review, and integrity assurance of codebase and data assets.
- **Responsibilities**:
  - **Code Audits**: Enforce technical guidelines, code hygiene, absence of exposed credentials, and security best practices.
  - **Data Audits**: Cross-reference samples against primary sources, assert consistency against canonical schemas (`scripts/validate_data.py`), verify cryptographic provenance (`provenance.json`), and ensure zero data inference.
  - Possess technical authority to block or request revisions on any PR violating verification criteria.

### 2.4. New Members & Initial Scope
- **Scope**: Onboarded with limited permissions and a defined operational scope.
- **Responsibilities**:
  - Work under maintainer guidance on designated repositories or development branches.
  - Do not have direct access to package publishing keys, infrastructure settings, or direct-merge permissions on `main`.
  - Expanded permissions are granted gradually based on proven technical consistency.

---

## 3. Onboarding New Members

Formal membership is neither automatic nor open to casual contributions. Minor bug fixes, documentation adjustments, or suggestions should be made externally through standard Pull Requests, Issues, or public discussions.

### Membership Criteria:
1. **Demonstrated Technical Ability**: Prospective members must be vetted and show a verified track record of delivering substantial, sustained technical contributions to tools, software, or auditing pipelines.
2. **Prior Assessment**: Membership requires established consistency, code literacy, and strict adherence to open-source software principles and data integrity.
3. **Limited Initial Footprint**: Newly admitted members are granted focused permissions restricted to their immediate project branch. Global access and core tool governance remain reserved for designated maintainers.
4. **Onboarding Steps**:
   - Read this guide, `CONTRIBUTING.md`, and the technical documentation of the target project.
   - Configure local dev environments, validation scripts, and testing suites.
   - Coordinate initial scope directly with the target project's core maintainer.

---

## 4. Proposing a New Tool or Project (RFC)

Members may propose new tools, libraries, standalone utilities, or datasets by opening an **RFC / Project Proposal** Issue in the relevant repository or the `.github` tracker.

The proposal must address 4 core questions:

1. **Problem & Purpose**: What concrete engineering problem or data gap does this project solve? Why should it live under the BRAN Org umbrella?
2. **Architecture & Feasibility**: What technical stack, dependencies, and interfaces (CLI, library, API, UI) will be used? Are there technical bottlenecks or maintenance risks?
3. **Leadership & Maintenance**: Who will act as the lead maintainer responsible for the project's lifecycle? Is this a stable tool or an actively expanding system?
4. **Modularity & Reuse**: Does it serve multiple projects across the organization or solve a widespread challenge for researchers and developers? Can it be published as a reusable package?

---

## 5. Git Workflow & Release Policies

- **Branching Strategy**:
  - `main`: Production and release branch. Direct commits are restricted.
  - `development` / feature branches: Active development branches.
- **Pull Requests**:
  - Must provide a clear technical summary of changes and resolved problems.
  - Must pass 100% of automated CI checks (unit tests, linting, cryptographic assertions, schema validations).
  - Require formal approval from at least one maintainer or auditor.
- **Commit Standards**: Enforce strict Conventional Commits (`feat:`, `fix:`, `refactor:`, `docs:`, `test:`, `chore:`). Zero generic or AI-generated commit fluff.

---

## 6. Internal Collaboration & Communication

- **Channels**: Architecture discussions, design choices, and RFCs must be preserved publicly on Issues, Pull Requests, and GitHub Discussions for traceable provenance.
- **Tone**: Direct, technical, and respectful. Focus on code quality and tool utility.
- **Bandwidth Transparency**: As a community open-source initiative, we value clear and transparent communication regarding availability and committed tasks.

---

## 7. Inactivity & Friendly Offboarding

- **Communicating Pauses**: If taking time off due to personal or professional commitments, inform project maintainers so responsibilities can be reassigned smoothly.
- **Frictionless Offboarding**: Departing members retain public attribution for their historical contributions.
- **Access Hygiene**: Accounts inactive for more than 6 months without prior notice may have write permissions revoked as a standard operational precaution, easily reinstated upon return.
