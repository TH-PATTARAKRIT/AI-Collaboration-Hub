# A0 — Governance / Baseline Verification

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Verify governing documents, source paths, frozen prior evidence, and DB/quarantine boundaries before Inventory Deep Research begins | Claude (Team A, DR-002 pass, directive `SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002`) | This artifact | 2026-08-31 | Independent Evidence Review (pending); Boss (sole Final Approver) | VERIFIED | Establishes the frozen baseline this entire package builds on |

## 1. Governing documents — read in full, current canonical versions confirmed

| Document | Path | Verified |
|---|---|---|
| Project Constitution v1.4 | `00_Project_Governance/PROJECT_CONSTITUTION.md` | Read in full — 16 Core Principles, Authority Model, Standard Execution Flow, Gate Rule confirmed |
| STATE03+ Pre-Prompt Independent Challenge Rule v1.1 | `00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md` | Read in full — Five-Unit Challenge, Prompt Risk Classification, No-Answer-Key Rule confirmed |
| Lifecycle Evidence Preservation & Chain of Custody Standard v1.0 | `00_Project_Governance/LIFECYCLE_EVIDENCE_PRESERVATION_AND_CHAIN_OF_CUSTODY_STANDARD.md` | Read in full — 17-item Lifecycle Evidence Chain, Preservation Status vocabulary, Working Branch Rule confirmed |
| STATE03 Enterprise Module Learning Priority Matrix | `03_Architecture/00_Architecture_Governance/STATE03_ENTERPRISE_MODULE_LEARNING_PRIORITY_MATRIX.csv` | Read in full — 90 rows, Wave 2 `Inventory / Warehouse` confirmed with dependency `Product+UOM+Location+Company`, `Valuation design waits for COA contract` |
| STATE03 Accounting ⇐ Inventory Backbone Execution Roadmap | `03_Architecture/00_Architecture_Governance/STATE03_ACCOUNTING_INVENTORY_BACKBONE_EXECUTION_ROADMAP.md` | Read in full — Lane B (Inventory, START NOW, DELTA-FIRST), Lane C (Cross-Proof, 10 scenarios), 7 Anti-Bottleneck Rules confirmed |
| STATE03 Inventory Deep Research Material Unknown Exhaustion Amendment | `03_Architecture/00_Architecture_Governance/STATE03_INVENTORY_DEEP_RESEARCH_MATERIAL_UNKNOWN_EXHAUSTION_AMENDMENT.md` (commit `39f78e50a4d9589d18fc1dce130254bb397ee3cd`) | Read in full — supersedes prior `INV-BB-R01`, mandates Account-grade rigor, 9-value Thailand evidence vocabulary confirmed |
| DR-002 Pre-Prompt Readiness | `TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md` (commit `0397307bad8567755f3bd877907bccb329af9434`) | Read in full — `READY — TEAM A ACCOUNT-GRADE INVENTORY DEEP RESEARCH MAY START` |

## 2. Source paths — verified

- Authorized primary source (READ ONLY): `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/ACCOUNT/01 ACCOUNT/SOURCE CODE` — confirmed to exist, 93,866 files.
- `01 ACCOUNT/` subfolder contains **only** `account_*`-prefixed Accounting Core modules (62 folders) — no Inventory-relevant modules live here.
- `02 OTHER/` subfolder (1,378 module folders) contains the actual Inventory-relevant core: `stock`, `stock_account`, `stock_landed_costs`, `stock_barcode*`, `stock_picking_batch`, `product`, `uom`, `sale_stock`, `purchase_stock`, `mrp` and its 18 `mrp_*` extensions, `delivery*`, `barcodes*`. This corrects an implicit assumption in the DR-002 prompt's phrasing ("01 ACCOUNT/SOURCE CODE" as if Inventory modules live directly under `01 ACCOUNT`) — the actual Inventory module set is under `02 OTHER`, within the same authorized read-only root.
- Database dump present: `iTEST02_2026-06-14_14-41-19.dump` (65,444,053 bytes, PostgreSQL custom-format archive, `pg_dump` archive version 1.16). Same file GROUP A's Independent Evidence Review used (confirmed identical size).

## 3. Repository / branch verification

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`, canonical branch `SMEsPlus`, confirmed reachable and up to date at commit `5df588dbb436a26ff4a8b72579d3beeb96c668b3` (includes this session's own Account CORR5 publication, Phase A of the same Boss Last Execution Prompt).
- This DR-002 execution runs from a fresh isolated clone (`ISOLATED_INVENTORY_DR002/`), on a **dedicated Team A execution branch** `claude/inventory-core-backbone-dr002`, created off `SMEsPlus` HEAD. Per DR-002 §14.7 and the Backbone Evidence Chain Index row 11 ("Dedicated DR-002 execution branch / execution folder"), this branch is **not** merged into `SMEsPlus` by this session — consistent with the frozen GROUP A precedent, whose own evidence (commit `8b0993d824cf726fa52edd687272ff54b0977c42`) likewise lives only on `claude/group-a-sales-inventory-purchase-dr002`, never merged to `SMEsPlus`.

## 4. Frozen prior evidence commits — independently verified to exist

| Commit | Content | Verified |
|---|---|---|
| `8b0993d824cf726fa52edd687272ff54b0977c42` | Frozen Team A GROUP A Sales+Inventory+Purchase evidence (18 deliverables + manifest) | EXISTS — reachable only via `origin/claude/group-a-sales-inventory-purchase-dr002`, not on `SMEsPlus` |
| `626873c3b924a0350dfd75cf52d276eff6414dd2` | Independent Evidence Review of the above | EXISTS — reachable only via `origin/audit/group-a-sip-evidence-review-004`, not on `SMEsPlus` |
| `bd9b87f959711d502d0108d6ef4dce098a3bec1a` | Boss Evidence Gate decision (`APPROVED`) | EXISTS — reachable on `SMEsPlus` (canonical, merged) |
| `39f78e50a4d9589d18fc1dce130254bb397ee3cd` | Boss Amendment elevating Inventory to Account-grade research | EXISTS — reachable on `SMEsPlus` |
| `4a5f86219aa8fe8942bc14354ae25d976b95af3b` | R01 → DR-002 Supersession Record | EXISTS — reachable on `SMEsPlus` |
| `0397307bad8567755f3bd877907bccb329af9434` | DR-002 Pre-Prompt Readiness | EXISTS — reachable on `SMEsPlus` |
| `b134bbdbd392f093559c17918d17f95ae315c36f` | DR-002 controlling prompt itself | EXISTS — reachable on `SMEsPlus` |

The two commits reachable only on non-`SMEsPlus` branches (`8b0993d`, `626873c`) are being **read as reference evidence only** (`git show <commit>:<path>`), per DR-002 §5's "Reuse, Do Not Restart" instruction — this session does not check out, edit, or push to those branches.

## 5. Prior R01 status

`SMEPLUS-26-08-31-MIG-A-INV-BB-R01` is confirmed `HISTORICAL / SUPERSEDED` per the Backbone Evidence Chain Index row 05-06 and the Supersession Record (`4a5f86219`). No concurrent R01 execution result was found in this clone or the frozen evidence lineage — nothing to DELTA-FIRST-ingest from R01 itself. The relevant DELTA-FIRST input is the **GROUP A** package (`8b0993d`), which the DR-002 prompt itself names as the frozen evidence to reuse (§5.1), not a standalone R01 result.

## 6. Two distinct "Inventory research" lineages — disambiguated

The frozen GROUP A package's own internal session ID is `SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002` (a **combined** Sales+Inventory+Purchase research pass, already through Boss Evidence Gate `APPROVED`). This current session's ID is `SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002` (an **Inventory-only**, Account-grade deepening pass, mandated by the Amendment specifically because the Amendment judged Inventory not yet researched to sufficient depth on its own). These are not the same package despite the shared "DR-002" suffix. This document and all subsequent A1–A20 deliverables build on the former (DELTA-FIRST) to produce the latter.

## 7. Clean-room / quarantine boundary — confirmed at baseline

- SMEsPlus is a 100% clean-room Node.js SaaS ERP; Odoo source is reference/learning/benchmark evidence only.
- No raw vendor source, schema, or dump is to be committed to GitHub — see `A17_CLEAN_ROOM_CLASSIFICATION_AND_QUARANTINE_REGISTER.md`.
- The authorized source path is read-only; this session made zero writes into the source tree at any point (confirmed: only `Read`/`Grep`/`Bash` read-only commands were issued against it).

## 8. Database/dump forensics availability — assessed at baseline (full detail in A2)

Local tooling present: `psql`/`pg_restore`/`pg_dump` 16.15 (Homebrew), Docker (daemon running). Local `pg_restore` cannot read the dump's archive format v1.16 (requires PostgreSQL 18-class tooling — consistent with GROUP A's own Independent Evidence Review finding that PG16 fails and PG18 succeeds on this exact file). A disposable-container restore was attempted this session; the container-provisioning step was blocked by this session's own sandbox permission controls (not a source-access or dump-integrity problem). See A2 for full disposition — this session reuses GROUP A's frozen, independently-re-verified DB forensics results (DELTA-FIRST) rather than re-running its own restore.

## 9. Progress control

`% Board = TBD / NO BOSS-APPROVED EVIDENCE-WEIGHTED DENOMINATOR`
`% STATE03 = TBD / NO BOSS-APPROVED EVIDENCE-WEIGHTED DENOMINATOR`
`% Inventory DR-002 STEP = TBD / NO BOSS-APPROVED EVIDENCE-WEIGHTED DENOMINATOR`

STEP Binding: `TBD / BASELINE LINKAGE REQUIRED — DO NOT INVENT` (per DR-002 header) — preserved as-is, not invented.

No Evidence = No Progress. DELTA-FIRST. Never Skip Gate. Boss = Sole Final Approver.
