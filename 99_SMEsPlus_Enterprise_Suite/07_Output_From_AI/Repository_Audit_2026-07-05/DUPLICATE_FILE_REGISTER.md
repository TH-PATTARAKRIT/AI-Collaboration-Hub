# DUPLICATE FILE REGISTER — SMEsPlus Enterprise Suite Repository Audit

**Document ID:** SMEPLUS-AUDIT-DUPLICATE-REGISTER-001
**Audit Date:** 2026-07-05
**Method:** `find` full-tree enumeration + `diff -rq` byte comparison + `git log -1 --` provenance check per duplicate path.

## 1. Exact Duplicates (Confirmed Identical Content)

| Set | Path A | Path B | Comparison Result | Root Cause |
|---|---|---|---|---|
| D-01 | `02_Functional_Design/02_Functional_Design/` (13 files) | `02_Functional_Design/02_Functional_Design_v2/` (13 files) | `diff -rq` → **no differences on any file** | Unclear intent — `_v2` suggests revision but none occurred |
| D-02 | `01_AI_Handoff/` (content) | `01_AI_Handoff/01_AI_Handoff/` (self-nested copy) | Self-nested folder from upload | Zip root-folder name matched destination folder on GitHub web upload |
| D-03 | `03_Architecture_Decisions/` | `03_Architecture_Decisions/03_Architecture_Decisions/` | Self-nested folder | Same upload defect |
| D-04 | `04_Review_Gates/` | `04_Review_Gates/04_Review_Gates/` | Self-nested folder | Same upload defect |
| D-05 | `05_Prompts/` | `05_Prompts/05_Prompts/` | Self-nested folder | Same upload defect |
| D-06 | `06_Templates/` | `06_Templates/06_Templates/` | Self-nested folder | Same upload defect |
| D-07 | `08_Testing_Evidence/` | `08_Testing_Evidence/08_Testing_Evidence/` | Self-nested folder | Same upload defect |
| D-08 | `09_Security_Clean_Room/` | `09_Security_Clean_Room/09_Security_Clean_Room/` | Self-nested folder | Same upload defect |
| D-09 | `11_Diagrams/` | `11_Diagrams/11_Diagrams/` | Self-nested folder | Same upload defect |
| D-10 | `12_Traceability/Requirement_Matrix/` | `12_Traceability/Requirement_Matrix/12_Traceability/Requirement_Matrix/` | Self-nested folder (two levels deep) | Same upload defect |

**Provenance confirmation:** `git log --oneline -1 -- <path>` returns commit `b66b130 "Add files via upload"` for every nested duplicate in D-02 through D-10 — all nine originated from a single upload event, confirming a single systemic mistake rather than nine separate errors.

## 2. Near-Duplicates (Same Topic, Different Content — Authority Ambiguous)

| Set | File A | File B | Difference | Risk |
|---|---|---|---|---|
| N-01 | `01_SaaS_Foundation/FDS/FDS Requirement Catalog.md` (54 lines, status "Approved Baseline") | `01_SaaS_Foundation/FDS/FDS_REQUIREMENT_CATALOG.md` (186 lines, v1.0.0, different structure) | Different headers, different length, different status wording on line 1 of `diff` output | High — two documents both claim to be *the* Requirement Catalog; downstream readers may pick the wrong one |
| N-02 | `12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.2.md` (154 lines, 39 MATCHED/PARTIAL/GAP tags) | `12_Traceability/Requirement_Matrix/12_Traceability/Requirement_Matrix/SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.1.md` (743 lines, 67 tags) | v0.2 is ~80% shorter than v0.1 despite the higher version number | Medium-High — a "v0.2" implies superseding detail, but v0.2 has materially less evidence content than v0.1; if v0.1's detail is not preserved elsewhere, this is a silent evidence loss |
| N-03 | `12_Traceability/Requirement_Matrix/FUNCTIONAL-DESIGN-MATRIX-SUMMARY-v0.2.md` (top-level) | `12_Traceability/Requirement_Matrix/12_Traceability/Requirement_Matrix/FUNCTIONAL-DESIGN-MATRIX-SUMMARY.md` (nested, unversioned) | Same summary topic, one carries a version tag and one does not | Medium — same version-authority ambiguity as N-02, not yet content-diffed line by line |

## 3. Naming-Standard Violations (Space-Named Files Alongside Underscore Standard)

| File | Convention Violated | Sibling File Using Correct Convention |
|---|---|---|
| `01_SaaS_Foundation/FDS/FDS Requirement Catalog.md` | Uses spaces | `FDS_REQUIREMENT_CATALOG.md` |
| `01_SaaS_Foundation/FDS/FDS Traceability Index.md` | Uses spaces | (all other FDS files use `UPPER_SNAKE_CASE.md`) |
| `01_SaaS_Foundation/FDS/FDS Phase 2 Quality Gate.md` | Uses spaces | (all other FDS files use `UPPER_SNAKE_CASE.md`) |

Standard reference: `01_SaaS_Foundation/DOCUMENT_NAMING_STANDARD.md`.

## 4. Legitimate Dual-Format Pairs (Not True Duplicates — Flag Only for Registry Clarity)

These are `.md` source + `.pdf` rendered pairs covering the same content by design. Not a defect, but currently undeclared as pairs in any registry, which risks a future automated duplicate check flagging them incorrectly:

- `00_Architecture_Office/Enterprise_Standards/SMEPLUS-ENTERPRISE-STANDARDS-v0.1.md` ↔ `SMEPLUS Enterprise Architecture Standards v0.1.pdf`
- `00_Architecture_Office/Enterprise_Standards/SMEPLUS Architecture Office Workplan v0.1.pdf` ↔ (also duplicated one level up at `00_Architecture_Office/SMEPLUS Architecture Office Workplan v0.1.pdf` — this pair should be checked, as the same PDF filename appears at two different folder depths)
- `00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md` ↔ `SMEPLUS Business Capability Model v0.1.pdf`
- `00_Architecture_Office/Review_Checklists/SMEPLUS-ARCHITECTURE-REVIEW-GATE-v0.1.md` ↔ `SMEPLUS Architecture Review Gate v0.1.pdf`

**Additional confirmed exact duplicate (P1) — D-11:** `SMEPLUS Architecture Office Workplan v0.1.pdf` exists both at `00_Architecture_Office/` (root, 20,840 bytes) and `00_Architecture_Office/Enterprise_Standards/` (20,840 bytes) — `diff` confirms byte-for-byte identical. One copy is redundant; recommend keeping the `Enterprise_Standards/` copy (matches its declared document type) and removing the root-level copy.

## 5. Summary Counts

| Category | Count |
|---|---|
| Exact duplicate folder trees | 10 (9 self-nested + 1 `_v2` full tree) |
| Exact duplicate single files (outside folder trees) | 1 (D-11, confirmed) |
| Near-duplicate documents (ambiguous authority) | 3 |
| Naming-standard violations | 3 |
| Legitimate dual-format pairs needing registry declaration | 4 |
