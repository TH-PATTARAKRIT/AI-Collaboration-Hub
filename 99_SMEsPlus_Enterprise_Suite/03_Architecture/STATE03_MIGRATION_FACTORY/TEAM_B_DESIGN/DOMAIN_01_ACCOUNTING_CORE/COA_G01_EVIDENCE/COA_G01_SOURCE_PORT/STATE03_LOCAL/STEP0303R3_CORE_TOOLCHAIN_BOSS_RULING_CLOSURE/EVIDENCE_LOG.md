# STEP0303R3 — EVIDENCE LOG

Nature: ruling closure and packaging. No new research, no scope expansion, no source read.

## E1. INPUTS
- STEP0303 matrix §2.1–§2.7 and Thai annex T1–T9 (recommendations, previously unruled)
- STEP0303R2 outputs — 11 deliverables on disk; open gate A1 / OPEN-01
- STATE03 freeze declaration — baseline S2–S11, S1 open
- Boss rulings R1–R7 as supplied verbatim in prompt §4

## E2. TEMPLATE CHECK — TEMPLATE_NOT_FOUND (second occurrence)
Re-searched the project root to depth 7 for `.dotx`, `.dotm`, and `.docx` matching
templ/standard/house: none. No `.docx` created since STEP0303R2. All `template*` directories
remain Odoo source. Two `.docx` deliverables not generated; producing them would require
inventing layout, which §7 and Governance Rule 15 forbid.
`python-docx` 1.2.0 remains available — generation is immediate once a template is supplied.
Cumulative outstanding: **5 .docx across STEP0303R2 (3) and STEP0303R3 (2).**

## E3. EVIDENCE UNDERPINNING THE EVIDENCE_CONFIRMED ROWS
| Item | Evidence |
|---|---|
| CT-02 relational transactional datastore | 1,395 tables / 6,682 constraints / 5,141 FK edges; S2, S9 |
| CT-03 decimal money | WHT computed rate*base/100; statutory filing correctness |
| CT-04 effective-dated reference data | S4 — rates change by decree |
| CT-05 / CT-06 data-driven RBAC, branch-scoped | S7 (dynamic.access.right), S5 (per-branch filing) |
| CT-08 one approval abstraction | S8 — identical `_STATES` duplicated across two modules |
| CT-11 audit as platform service | S10 — tracking on state fields; cert inherits mail thread |
| CT-13 / CT-14 layout as config, Thai shaping | S11 — cheque.setting 76 fields; annex T3 |
| CT-16 XLSX statutory output | WHT report declares xlsxwriter/xlrd |
| CT-19 payment gateway independent | S6 — payment_2c2p depended on website_sale |
| CT-30 statutory golden-file tests | S1/S4 — statutory correctness not assertable by unit tests |

## E4. CLASSIFICATION COUNTS (CORE_TOOLCHAIN_BASELINE_PLANNING_ONLY.csv, 30 rows)
EVIDENCE_CONFIRMED 12 · BOSS_APPROVED_PLANNING_BASELINE 17 · JUDGMENT_RECOMMENDED 1.
Nothing marked EVIDENCE_CONFIRMED without a cited evidence basis.

## E5. GOVERNANCE POSITION
Rule 1 evidence — held. Rule 2 never skip gate — the STEP0303R2 open gate is now closed by
ruling, not bypassed. Rule 3 Boss sole approver — only supplied rulings recorded.
Rules 4–6 clean room, no scope expansion, no new workstream — held.
Rules 7–9 no development, no repo/source files, nothing selected beyond recorded rulings — held.
Rules 10–11 no reopened research, no proprietary body read — held.
Rules 12–13 PDPA guardrail only, not a blocker — held.
Rule 14 classification separation — held. Rule 15 template — TEMPLATE_NOT_FOUND reported.
