# NEXT ACTION PLAN — SMEsPlus Enterprise Suite Repository Audit

**Document ID:** SMEPLUS-AUDIT-NEXT-ACTION-001
**Audit Date:** 2026-07-05
**Principle applied:** flag blockers once, get a Boss decision, proceed immediately — no looping on confirmations.

---

## Sequence 1 — Repository Hygiene (must clear before anything else; no content risk, pure structural fix)

| Step | Action | Owner | Depends On | Evidence to Produce |
|---|---|---|---|---|
| 1.1 | Boss decision: approve deletion of the 9 self-nested duplicate folders (GAP-01) | Boss (via Executive Secretary AI decision pack) | This audit | Boss approval record |
| 1.2 | Delete the 9 nested duplicate folders; log the removal in `ARCHITECTURE_DECISION_LOG.md` | Executive Secretary AI | 1.1 | Updated decision log entry, before/after `find` diff |
| 1.3 | Boss decision: confirm `02_Functional_Design_v2/` was never divergently edited and can be deleted (GAP-02) | Boss | This audit's `diff -rq` evidence | Boss approval record |
| 1.4 | Delete `02_Functional_Design_v2/`; log in decision log | Diagrams Flowcharts Mindmaps AI | 1.3 | Updated decision log entry |
| 1.5 | Rewrite root `README.md` folder map and status table to match actual structure (GAP-03, GAP-04) | Executive Secretary AI | none | Updated `README.md` |
| 1.6 | Rewrite `SMEPLUS_REGISTRY.yaml` to include all real top-level folders and owners | Executive Secretary AI | 1.5 | Updated `SMEPLUS_REGISTRY.yaml` |
| 1.7 | Fix `01_SaaS_Foundation/DB/README.md` — extract the clean README text already embedded in the file, replace file content entirely (GAP-05) | Database Design AI | none | Clean `DB/README.md` |
| 1.8 | Rename `01_SaaS_Foundation/API/OPENAPI_FOUNDATION_v0.1.yaml` to `.md` (or add explicit placeholder-YAML policy note) (GAP-09) | Enterprise Architect AI | none | Renamed/annotated file |
| 1.9 | Remove the redundant root-level copy of `SMEPLUS Architecture Office Workplan v0.1.pdf` (D-11), keeping the `Enterprise_Standards/` copy | Enterprise Architect AI | none | Single remaining copy |

**Gate impact of Sequence 1:** clears Repository Structure Gate from AMBER toward PASS. No functional content changes.

---

## Sequence 2 — Functional Design Authority Resolution (must clear before FDS can move from Draft/In-Review to Approved Baseline)

| Step | Action | Owner | Depends On | Evidence to Produce |
|---|---|---|---|---|
| 2.1 | Boss/PMO ruling: which file is the authoritative Requirement Catalog — `FDS Requirement Catalog.md` or `FDS_REQUIREMENT_CATALOG.md` (GAP-06) | PMO AI → Boss | This audit's content diff | Ruling recorded in `FDS/01_DOCUMENT_CONTROL.md` |
| 2.2 | Archive or delete the non-authoritative catalog file | Functional Specification AI | 2.1 | Updated `FDS/` folder |
| 2.3 | Rename `FDS Traceability Index.md` and `FDS Phase 2 Quality Gate.md` to underscore convention (GAP-07) | Functional Specification AI | 2.1 (do together to minimize churn) | Renamed files matching `DOCUMENT_NAMING_STANDARD.md` |
| 2.4 | PMO AI confirms or rejects the NEW requirements in `FDS_MODULE.md`, `FDS_REPORTING.md`, `FDS_CONFIGURATION.md` (GAP-10) | PMO AI | none | Updated Traceability Matrix reflecting MATCHED/PARTIAL/GAP/NEW/RETIRE status for each |
| 2.5 | Confirm whether `SMEPLUS-FUNCTIONAL-DESIGN-MATCHING-MATRIX-v0.2.md` is an intentional lightweight summary or an accidental content-loss regression relative to the nested v0.1 (GAP-11); rename if it's a summary, restore detail if it's a regression | Enterprise Architect AI / PMO AI | none | Clarified matrix, single authoritative version chain |
| 2.6 | Register `V2.0/` package and confirm relationship to the current baseline, particularly the already-closed evidence CSVs (GAP-12) | Executive Secretary AI | none | Registry entry, cross-reference note in `DOCUMENT_MAP.md` |
| 2.7 | Assign root-level operational notes (`GITHUB_PUSH_INSTRUCTIONS.md`, `MODULE_EXPANSION_PLAN.md`, `PUSH_READY.md`, `SYNC_GUIDE.md`) to a registered folder (GAP-13) | PMO AI | none | Updated registries |

**Gate impact of Sequence 2:** allows FDS to move from Draft/In-Review toward Approved Baseline, which is the single blocking dependency named inside every SDS/API/DB/UX placeholder file.

---

## Sequence 3 — Registry Completion (parallelizable with Sequence 2)

| Step | Action | Owner | Evidence to Produce |
|---|---|---|---|
| 3.1 | Register `01_SaaS_Foundation/ADR/`, `QA/`, `SECURITY/`, `DEPLOYMENT/`, `DEVOPS/` in `FOLDER_REGISTRY.yaml` / `DOCUMENT_REGISTRY.yaml` (GAP-08) | PMO AI / Boss | Updated registries; each folder README updated to remove "pending registration" wording |
| 3.2 | Declare the four dual-format `.md`/`.pdf` pairs in the registry as source + rendered copy (GAP-14) | PMO AI | Registry annotation |
| 3.3 | Clean up or properly title the stray screenshot in `02_Functional_Design/` (GAP-15) | Functional Specification AI | Renamed or removed asset |

---

## Sequence 4 — Only After Sequences 1–3 Close: Re-open SDS/API/DB/UX/QA Work

| Step | Action | Owner | Depends On |
|---|---|---|---|
| 4.1 | Boss approves FDS Approved Baseline status | Boss | Sequence 2 complete |
| 4.2 | Database Design AI begins ERD work, unblocking `DB/` and `SDS/ERD_FOUNDATION_v0.1.md` | Database Design AI | 4.1 |
| 4.3 | Functional Specification AI / Enterprise Architect AI author real SDS content | Functional Specification AI, Enterprise Architect AI | 4.1, 4.2 |
| 4.4 | Author real `API/OPENAPI_FOUNDATION_v0.1` content once SDS data model is approved | Enterprise Architect AI | 4.3 |
| 4.5 | QA UAT AI begins test planning against the approved FDS/SDS for SaaS Foundation scope, keeping it clearly distinguished from the existing `08_Testing_Evidence/` iTEST02 dump-analysis evidence | QA UAT AI | 4.1 |
| 4.6 | Re-run this repository audit to confirm Build Gate can move from HOLD toward PASS/AMBER | Any AI role, PMO-witnessed | 4.1–4.5 |

---

## Immediate Blockers Requiring a Boss Decision Right Now

1. Approve deletion of the 9 self-nested duplicate folders and the `02_Functional_Design_v2` tree (Sequence 1.1, 1.3).
2. Rule on Requirement Catalog authority (Sequence 2.1).
3. Confirm/reject the three NEW domain requirements (Sequence 2.4).

Everything else in Sequences 1 and 3 can proceed immediately without further Boss input, per the project's own control rule of flagging blockers once and proceeding on resolution.
