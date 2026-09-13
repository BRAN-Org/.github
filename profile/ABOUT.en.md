# About BRAN Org

## About Us & Our Mission

**BRAN Org** (**Brazilian Research Archive Network**) is an independent organization dedicated to building open infrastructure for academic and scientific information in **Brazil**.

We map **academic data that is already public**, but lacks APIs or easy programmatic access. Our work is to collect, clean, and provide this information in open and standardized formats through public APIs and open-source tools, lowering technical barriers for researchers and boosting quantitative studies on Brazilian scientific output.

---

## Our Goals

- **Map Brazilian Sources**: Identify public academic collections, repositories, and databases that lack programmatic access.
- **Structure Public Data**: Convert raw or fragmented data into clean, standardized formats ready for analysis.
- **Create Open APIs**: Provide public, accessible endpoints for integration into research and software.
- **Develop Tools**: Build open-source packages and applications focused on quantitative scientific analysis.

---

## Our Projects

### Databases & Collections

Public catalog of bibliometric databases from Brazilian scientific output, provided in open formats (`JSON`/`CSV`), featuring a free REST API and interactive dashboard for analysis.

| Repository | Official Event | Records | Data Reliability |
| :--- | :--- | :---: | :---: |
| [abec-open-database](https://github.com/BRAN-Org/abec-open-database) | [ABEC Meeting](https://www.abecbrasil.org.br/) | **259 Articles** (2013-2025) | [🟠 In Curation](#-data-reliability-levels) |
| [ebbc-open-database](https://github.com/BRAN-Org/ebbc-open-database) | [EBBC](https://ebbc.inf.br) | **643 Articles** (2012-2024) | [🟡 Source Faithful (Limitations)](#-data-reliability-levels) |

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

---

## Our Story and Vision

### 1. The Origin of the Name BRAN

If you're wondering about the inspiration behind the acronym **BRAN** (**Brazilian Research Archive Network**), the name is a nod to **Brann Bronzebeard**, a character from *World of Warcraft*.

![Brann Bronzebeard in action](../assets/brann_bronzebeard_ingame.png)

In the game, Brann is an archaeologist and researcher dedicated to exploring forgotten ruins, rescuing historical records, and sharing his discoveries openly. This directly reflects our real-world mission: excavating fragmented or forgotten Brazilian academic data and making it accessible to everyone.

---

### 2. A Small Step for Brazilian Science

In the international scientific arena, researchers and data scientists benefit from highly integrated and elegant ecosystems for academic metadata analysis (such as *Crossref*, *OpenAlex*, *Semantic Scholar*, *PubMed*, and *Web of Science*). In those environments, robust REST APIs, structured JSON schemas, and persistent identifiers (DOIs) are the established standard.

In **Brazil**, however, there is a challenging contrast. While major publications enjoy proper indexing, a vital portion of the nation's scientific output remains in a technological infrastructure void:

* **Conference Proceedings & Symposia**: Thousands of national conferences publish their proceedings on static web pages, legacy portals, or isolated PDFs lacking standardization, DOIs, or programmatic access.
* **Regional & Institutional Journals**: Smaller scientific journals face severe budget and technical constraints to implement and maintain modern metadata platforms.

**BRAN Org** emerges to take a concrete step toward strengthening this ecosystem through two complementary fronts:

1. **Structuring & Traceability for Events and Journals**: We support regional organizers and editors by converting unstructured archives into clean, standardized datasets with guaranteed digital preservation.
2. **Direct Accessibility for Scientific Research**: We eliminate the need to build complex manual web scrapers, equipping bibliometric and scientometric researchers with open datasets (`JSON`/`CSV`) and free REST APIs for immediate quantitative analysis.

---

### 3. Looking Beyond the Mainstream: Complementing National Platforms (e.g., Projeto Laguna)

Major national scientific infrastructure initiatives in Brazil — such as **Plataforma Lattes**, **Sucupira/CAPES**, **BDTD/IBICT**, or **Projeto Laguna** — play an essential role in centralizing researcher CVs, tracking graduate output, and indexing high-impact journals.

However, due to the massive scope and institutional priorities of these major portals, significant portions of Brazilian scientific memory remain outside the core system:

* **Regional & Early-Career Output**: Papers presented at regional conferences, undergraduate research meetings (PIBIC), and local academic society symposia rarely reach central indexers.
* **Historical & "Orphan" Archives**: Older conference editions whose web domains expired or whose organizing committees dissolved over time.

**BRAN Org**'s work is strictly symbiotic. We do not compete with major national platforms; instead, we **rescue, structure, and preserve the academic literature that falls outside mainstream portals** — ensuring that Brazil's regional, emerging, and historical research gains the visibility, organization, and digital preservation it deserves.

---

### 4. The Horizon: Preparing the Ground for Unified Data in Brazil

We aspire for **BRAN Org**'s work to serve as a foundation and catalyst for even broader future initiatives.

By adhering to the **FAIR Principles** (*Findable, Accessible, Interoperable, Reusable*), the **BOAI Declaration**, and strictly open-source licenses, we are building a modular, interoperable infrastructure. Our horizon is to prepare Brazilian academic information to integrate into or catalyze **larger national projects aimed at unifying scientific databases across Brazil**, connecting islands of information into a cohesive, transparent, and sovereign open knowledge network.
