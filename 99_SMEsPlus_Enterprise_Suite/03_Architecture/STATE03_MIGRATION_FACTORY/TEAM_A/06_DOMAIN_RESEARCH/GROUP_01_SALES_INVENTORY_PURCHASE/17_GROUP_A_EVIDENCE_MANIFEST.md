> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Evidence Manifest
> SHA-256 computed directly against each committed file at manifest-creation time. Branch: `claude/group-a-sales-inventory-purchase-dr002`.

# 17 — GROUP A EVIDENCE MANIFEST

## 01 — Deliverable files (this folder)

| # | File | SHA-256 |
|---|---|---|
| 01 | `01_SHARED_MASTER_DEPENDENCY_MAP.md` | `47ae338f59170f31eeba9eed208dedc98e82ac2aa1d42e88ca14fd331e3459d6` |
| 02 | `02_INVENTORY_CAPABILITY_MODEL.md` | `068f1a911da9dec6e6a4a4cdbf77bed824b6debd70e0275a1e73c82b7b182f40` |
| 03 | `03_SALES_CAPABILITY_MODEL.md` | `28817fb0ad2d8006d153b46c8992aafb96e553138f329481d2440b56bbaa8d33` |
| 04 | `04_PURCHASE_CAPABILITY_MODEL.md` | `1c93049ad1405336cdca84c203b9fb670fb5645f6a918834c9937c7e9cbd9396` |
| 05 | `05_INTEGRATED_E2E_LIFECYCLE_MAP.md` | `307fcc80a9ec2d33f2a999ab1ce0c71622bf4858e1075a3f7f0a5b6bedc08e01` |
| 06 | `06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` | `b5be96883a56a7ad6fa3d32cef549a2d8e4048b5e094d36b064bde240192f313` |
| 07 | `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` | `0332afd710be3f81b007049b239814170da0d9fba48ab90c97238f98c3744508` |
| 08 | `08_SOURCE_DATABASE_SEMANTIC_TRACEABILITY_MATRIX.md` | `635c559d91b40c5dfd562735640fb178a99e23492eb846bf04e04e1dc5caac01` |
| 09 | `09_QUANTITY_SEMANTICS_REGISTER.md` | `4103c7df8bbd0cfe876aee08ec4702418cacd757d886d2c3b90ac71fe481527a` |
| 10 | `10_EXCEPTION_PARTIAL_RETURN_CANCELLATION_MATRIX.md` | `0aacc4945c945de0c90c01df0f5b4d73760d9c14f60a2db20d7794b21f932a3b` |
| 11 | `11_THAILAND_BUSINESS_REALITY_AND_VARIATION_REGISTER.md` | `12b642a7dbe6fb0e591407b3e589f1a4c029855e6b38988487993a260b485979` |
| 12 | `12_PERSONA_USER_FITNESS_OBSERVATION_MATRIX.md` | `0a8a045fc559f8b41ca1b860a9f9761fce126b804736c236f49a79938b79b15c` |
| 13 | `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` | `de9f7b7493f0242ad8d93c597aeb17454a026e1591145d354a8c4d3f82832967` |
| 14 | `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` | `1dc82098df594b5547db51b298a521ad758e8f033dc8bbfbfddb9432e618e91a` |
| 15 | `15_EXTERNAL_DEPENDENCY_AND_SYSTEM_RISK_OBSERVATION_REGISTER.md` | `e64222957b9aa067d77c8588083a63307408c09713a0ccc3cae9de5c084da61f` |
| 16 | `16_FIT_GAP_CANDIDATE_PACK.md` | `65f43d42d6323ec6d141fd97ac55b6e847c8f957294de33b9c5c5403cc0756fa` |
| 00a | `00_NEW_SESSION_PROMPT_..._GRP01-SIP-DR-001.md` (prior session prompt, prompt-only, no deliverable) | `bccfd7b3035cbf37ec5d14d669a37486612fb766bf6d9c0f2681f1f4f4ba1811` |
| 00b | `00_NEW_SESSION_PROMPT_..._GRPA-SIP-DR-002.md` (this session's prompt) | `2ec2a714083354a91cf07f041afbf57e0721a998f2a5d7cd717c0138f2a4e7e4` |

## 01a — Integrity coverage note (added in corrective session CORR-003)

The table above lists SHA-256 for the 16 content deliverables (01-16) plus the two session-prompt files (00a/00b)
— **18 rows, all independently verifiable** (`shasum -a 256 <file>`). This manifest (17) and the Evidence Gate
Report (18) are not, and cannot be, listed with a self-hash here, since a file's hash cannot include its own
final content. File 19 (`19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`) and this file's own final version are covered
instead by the separate external manifest `20_GROUP_A_FINAL_SHA256_MANIFEST.txt`, which lists files 01-19
(excluding itself, per the same self-hash limitation). Any statement elsewhere in this evidence chain reading
"18/18 SHA-256 verified" without this qualification has been corrected — see
`18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md` §08.

## 02 — Primary evidence sources consumed (local, not committed to this repo)

| Source | Location | Role |
|---|---|---|
| Odoo-19 source tree | `ACCOUNT/01 ACCOUNT/SOURCE CODE/` (`01 ACCOUNT/`, `02 OTHER/`, `addons_extra/`) on the local project volume | Primary evidence for all model/method/field citations |
| Database schema extraction | `ACCOUNT/01 ACCOUNT/iTEST02_2026-06-14_14-41-19.dump` → schema-only SQL extracted via `pg_restore --schema-only` (libpq 18.4, no live DB required) to a scratch file (`schema_only.sql`, ~214,294 lines) | Primary evidence for all DB table/column/constraint citations, Phases 1-8 |
| Database **full** (schema+data) extraction — **added in CORR-003** | Same dump, restored in full into a local scratch PostgreSQL 16 instance (`initdb`/`pg_restore -j4`, 18 unrelated errors on an AI-embedding table ignored), queried directly via `psql`, then the instance was stopped and is not persisted | Primary evidence for row-level/metadata forensics resolving the orphaned approval schema (Critical #1) — see `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` |
| `DOMAIN_01_ACCOUNTING_CORE/` (already-existing, separate domain research) | `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/` | Style precedent; DELTA-FIRST reuse source for Tax/Payment-Term baseline check (Phase 1) |

## 03 — Deliverables required by governance §22 not produced as separate files (consolidated instead)

Per the governing prompt's own allowance ("File names may be normalized... semantic deliverables must not be
omitted without written justification"), all 16 semantic deliverables ARE present as separate files above — no
consolidation or omission occurred for #01–16. This manifest (#17) and the closing gate report (#18) complete the
required 18-item set.

## 04 — Branch / commit trail

| Commit (message summary) | What it added |
|---|---|
| `research(group-a): add Phase 1 Shared Master Dependency Map...` | File 01 |
| `research(group-a): add Phase 2 Inventory Capability Model...` | File 02 |
| `research(group-a): add Phase 3 Sales Capability Model...` | File 03 |
| `research(group-a): add Phase 4 Purchase Capability Model...` | File 04 |
| `research(group-a): add Phase 5-6 cross-module E2E, event/dependency map, fact ownership, and exception matrix` | Files 05, 06, 07, 10 |
| `research(group-a): add Phase 7 Quantity Semantics Register and Source-DB Traceability Matrix` | Files 08, 09 |
| `research(group-a): add Phase 8 Thailand Business Reality Register and Persona/User Fitness Matrix` | Files 11, 12 |
| (this commit) | Files 13, 14, 15, 16, 17, 18 |

All commits are on `claude/group-a-sales-inventory-purchase-dr002`, pushed to
`https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub`. No commit has been merged into `SMEsPlus` — that
decision belongs to the project's existing Boss Gate / PMO Verification process (see
`03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/`, `PMO_VERIFICATION/` precedent from Domain 01).

## 05 — Integrity note

SHA-256 values above were computed directly against the files as committed (`shasum -a 256`), not asserted from
memory. Re-verification: `shasum -a 256 <file>` against any file in this folder should reproduce the value shown.
