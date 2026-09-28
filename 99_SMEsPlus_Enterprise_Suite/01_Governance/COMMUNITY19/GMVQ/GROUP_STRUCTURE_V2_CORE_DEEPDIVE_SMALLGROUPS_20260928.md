# GROUP_STRUCTURE_V2_CORE — Deep-Dive Evidence Search: Smallest G-Groups (2026-09-28)

**STATUS: RESEARCH NOTE ONLY — NOT A ROSTER, NOT BOSS-APPROVED.**

This document does **not** modify `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` or its
README. It is a second, deeper evidence pass targeting the smallest governed groups
(by governed module count, excluding G11 which is already fully DERIVED): G04=9, G07=9,
G02=11, G03=11, G09=11, G15=11, G06=12, G10=13. The goal was to find any explicit
module↔group pairing the first compilation pass missed — never to invent, guess,
prefix-match, category-guess, or dependency-infer one.

## Method

1. Read `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` and its README in full.
2. Re-read, in full (not grep-only), every source document the candidate TSV/README cites
   for these groups:
   - `A1_SOURCE_EVIDENCE_LANE/G01_G04_RED_TEAM_STATIC_CHECKPOINT_R2/R3/R4/R5/R6/R9/R11/R14_2026092[4-5].md` (8 files, all read in full)
   - `A1_SOURCE_EVIDENCE_LANE/G05_G08_A1_PARALLEL_STATIC_INTAKE_V1.00.md`
   - `A1_SOURCE_EVIDENCE_LANE/G05_G08_RED_TEAM_A1_CHECKPOINT_R2_20260925.md`
   - `A1_SOURCE_EVIDENCE_LANE/G05_G08_RED_TEAM_A1_STATIC_DELTA_R3/R4/R10_20260925.md`
   - `A1_SOURCE_EVIDENCE_LANE/G09_G12/A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md` (including its embedded RED TEAM delta section)
   - `A1_SOURCE_EVIDENCE_LANE/G09_G12/R10_DELTA_POINTER_20260925_0914.md`, `R11_DELTA_POINTER_20260925_1016.md`, `RT_STATUS_20260925_0115.md`
   - `A1_SOURCE_EVIDENCE_LANE/G13_G16_A1_ROSTER_RECONCILIATION_AND_STATIC_INTAKE_V1.00.md`
   - `A1_SOURCE_EVIDENCE_LANE/G13_G16_RED_TEAM_A1_STATIC_DELTA_R4_20260925.md`, `R6_20260925.md`
   - `A1_SOURCE_EVIDENCE_LANE/G13_G16_RED_TEAM_PARALLEL_CHECKPOINT_20260925.md`
   - `GMVQ/OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md`
   - `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md` and its `_C1B`/`_C1C`/`_C2_FINAL` variants
   - `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928_INSTALL_CROSSCHECK.md`
   - `A1_SOURCE_EVIDENCE_LANE/A1_SOURCE_STUDY_INDEX_20260924.md`, `A1_PARALLEL_EXECUTION_CORRECTION_20260924.md`, `FAST_LEARNING_MODEL_BOSS_APPROVAL_20260925.md`
3. Grepped the entire `99_SMEsPlus_Enterprise_Suite` tree (not just the A1 evidence lane) for
   the literal strings `IDENTITY_ACCESS`, `MASTER_DATA`, `ACCOUNT_BASE`, `ACCOUNT_PROCESS`,
   `DASHBOARD_REPORT` (the exact governed group names for G02/G03/G04/G10/G15), and for
   `G02`/`G03`/`G04`/`G06`/`G09`/`G10`/`G15` as bare tokens, to check whether any functional
   design, architecture, or Phase-2.5 knowledge-consolidation document outside the A1 evidence
   lane names these groups from a different angle. This surfaced one additional hit outside the
   already-cited A1/GMVQ set: `03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/AI_OWNER_ASSIGNMENT_MATRIX.md`
   (read in full — see G02 section below for why it does not count).
4. Checked `07_Output_From_AI/Phase_2.5_Knowledge_Consolidation/*.md`,
   `01_SaaS_Foundation/FDS/Domains/FDS_MODULE.md`, `00_Architecture_Office/Reference_Architecture/SMEPLUS-BUSINESS-CAPABILITY-MODEL-v0.1.md`,
   `16_Learning_Analysis/*.md`, and `17_Functional_Specification_Factory/*` for the exact
   governed group names — no matches for `IDENTITY_ACCESS`, `MASTER_DATA`, `ACCOUNT_BASE`,
   `ACCOUNT_PROCESS`, or `DASHBOARD_REPORT` were found in any of them.

**Important scoping note on the many `COA_G01`…`COA_G11`/`COA_G02_CORR1` etc. files found under
`03_Architecture/STATE03_MIGRATION_FACTORY/` (BOSS_GATE, CHATGPT_AUDIT, TEAM_B_DESIGN,
CORE_RESOURCE_GOVERNANCE, PMO_VERIFICATION):** these use a **completely different, unrelated
`G01`–`G11` numbering** — internal stage/gate labels for the Accounting Core (COA) domain
migration-factory workflow (e.g. "COA_G02_BASE_KERNEL_DISCOVERY", "COA_G03_CANONICAL_
CONSOLIDATION_REGISTER") and a separate resource-governance gate sequence ("G8_COST_TO_SERVE",
"G9_WHOLE_PACKAGE_SPECIALIST_REVIEW", "G10_PMO_EVIDENCE_INDEX", "G11_BOSS_FINAL_DECISION").
These are NOT the Group Structure V2 G01–G16 module-governance groups this task is about, and
none of them was read as if it were — checking a sample of file names and their surrounding
directory context (COA_G0x directories under DOMAIN_01_ACCOUNTING_CORE, and the sequential
G2/G8/G9/G10/G11 gate-numbered files under CORE_RESOURCE_GOVERNANCE) confirmed this is a
same-token, different-namespace collision, not evidence about GROUP_STRUCTURE_V2_CORE group
membership. No pairing was extracted from these files.

## Findings by group

### G02 IDENTITY_ACCESS (governed count 11)
**No additional evidence found beyond what's already in the candidate TSV.**

All eight G01_G04 checkpoint files (R2–R14) were re-read in full. The 11-name candidate
auth-family reconstruction (`auth_ldap`, `auth_oauth`, `auth_passkey`, `auth_passkey_portal`,
`auth_password_policy`, `auth_password_policy_portal`, `auth_password_policy_signup`,
`auth_timeout`, `auth_totp`, `auth_totp_mail`, `auth_totp_portal`) is repeated verbatim across
R3, R4, R5, R6, R9, R11 and R14, and is explicitly re-stated as "CANDIDATE ONLY / NO CANONICAL
MEMBERSHIP CREDIT" or "NO CANONICAL MEMBERSHIP CREDIT" in every one of those re-statements —
it never crosses into an explicit "belongs to G02 / IDENTITY_ACCESS" sentence. `OVQDT_G02_G16_
ROSTER_HOLD_20260925_1521.md` confirms the same HOLD. The one repo-wide hit outside the A1
lane, `AI_OWNER_ASSIGNMENT_MATRIX.md` (ARC-WP-009, "Identity and Access Architecture Concept",
output file `IDENTITY_ACCESS_ARCHITECTURE.md`), is a planned architecture *work-package* name,
not a module roster — it does not name any technical module at all, so it cannot resolve any
G02 row and is not counted as new evidence.

### G03 MASTER_DATA (governed count 11)
**Re-confirms** the existing candidate TSV rows: `product`, `uom`, `analytic` are explicitly
anchored to MASTER_DATA in R11 ("Historical evidence explicitly anchors `product`, `uom`,
`analytic` to MASTER_DATA") and this anchor is deepened (not widened) with additional source
detail on `product.category`, `analytic.plan`, `analytic.distribution.model`, and
`product.product` in R11/R14 — none of that additional detail names a 4th module or pairs any
new module to MASTER_DATA. **No additional module↔group pairing found beyond product/uom/
analytic already in the candidate TSV.**

### G04 ACCOUNT_BASE (governed count 9)
**No additional evidence found beyond what's already in the candidate TSV.** Every checkpoint
(R2–R14) repeats the same finding: the `account` module boundary was examined ever more
deeply (lock exceptions, code mapping, account tags, account root) but every single round
explicitly states this source presence does **not** establish ACCOUNT_BASE vs ACCOUNT_PROCESS
ownership and that "source prefix alone is not used to assign rows." No module name is ever
paired with ACCOUNT_BASE / G04 in any of the eight checkpoint files.

### G06 MANUFACTURING (governed count 12)
**Re-confirms** the single existing anchor: `mrp` is explicitly named ("G06 MANUFACTURING —
verified source anchor `mrp`") in `G05_G08_A1_PARALLEL_STATIC_INTAKE_V1.00.md`. The three
RED TEAM delta rounds (R2 checkpoint, R3, R4, R10 — all read in full) deepen the `mrp` anchor
extensively (BoM/kit structure, workcenter state, workorder lifecycle, backorder/consumption-
warning wizards, UI/menu/controller/test surfaces) but never name a second module and never
pair any other module with MANUFACTURING/G06. **No additional module↔group pairing found.**

### G07 PURCHASE (governed count 9)
**Re-confirms** the single existing anchor: `purchase` is explicitly named ("G07 PURCHASE —
verified source anchor `purchase`"). The same four G05_G08 delta documents deepen the
`purchase` anchor (approval/locking mechanics, company settings, partner/invoice matching,
portal routes, tests) without ever naming or pairing a second module to PURCHASE/G07.
**No additional module↔group pairing found.**

### G09 CRM (governed count 11)
**Re-confirms** the single existing anchor: `crm` is explicitly named ("Anchor module: `crm`"
under the "G09 CRM - verified anchor extraction" heading) in
`A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md`. Its embedded RED TEAM delta section and
the separate R10/R11 delta pointer files (all read in full) add manifest/model detail (direct
dependencies of `crm` — `base_setup`, `sales_team`, `mail`, `calendar`, `resource`, `utm`,
`web_tour`, `contacts`, `digest`, `phone_validation` — plus `crm.lead` lifecycle/state detail,
and later "CRM partner materialization/sync and round-robin assignment") but these are manifest
**dependencies** of the `crm` module, not module↔G09 pairings for any *other* module — per the
task's own instruction, a dependency relationship must not be treated as, or converted into, a
group-membership pairing. **No additional module↔group pairing found beyond the `crm` anchor
already in the candidate TSV.**

### G10 ACCOUNT_PROCESS (governed count 13)
**No additional evidence found beyond what's already in the candidate TSV.** The same
`A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md` document (and its RED TEAM delta section)
examines the `account` module and `account.payment` model in real depth (payment lifecycle,
reconciliation, internal-transfer cross-reference) but is explicit and repeated on this point:
"This checkpoint does NOT claim that the `account` technical module itself is owned by G10
until the exact V2 roster row is retrieved" and later "This is process evidence only, not G10
ownership proof." No module is ever paired with ACCOUNT_PROCESS / G10 in any reviewed document.

### G15 DASHBOARD_REPORT (governed count 11)
**No additional evidence found beyond what's already in the candidate TSV.** The full
`G13_G16_A1_ROSTER_RECONCILIATION_AND_STATIC_INTAKE_V1.00.md` document states explicitly that
"Historical/preliminary inventories mention dashboard/report components, but they are
mixed-source and cannot establish current Community19 G15 membership" and "No module is
credited to G15 in this run without exact roster evidence." The one delta round that touches
G15 (`G13_G16_RED_TEAM_A1_STATIC_DELTA_R4_20260925.md`) adds static detail on
`odoo/addons/base/models/ir_actions.py` (the generic action/report-binding framework) as
"static evidence" for DASHBOARD_REPORT, but this is the shared `base` action-framework
infrastructure, not a named DASHBOARD_REPORT-family module, and the document does not state
that `ir_actions`/`base` itself belongs to G15. Repo-wide search for `DASHBOARD_REPORT` outside
the A1/GMVQ lane returned zero hits. **No module↔group pairing exists for G15 anywhere in the
repository.**

## Summary

| Group | Governed count | Outcome of this deeper pass |
|---|---:|---|
| G02 IDENTITY_ACCESS | 11 | Nothing new. Candidate 11-name auth list remains explicitly CANDIDATE ONLY / NO CREDIT everywhere it appears. |
| G03 MASTER_DATA | 11 | Nothing new. `product`/`uom`/`analytic` re-confirmed only; no 4th–11th name found. |
| G04 ACCOUNT_BASE | 9 | Nothing new. Zero modules ever paired to G04 in any reviewed document. |
| G06 MANUFACTURING | 12 | Nothing new. `mrp` re-confirmed only. |
| G07 PURCHASE | 9 | Nothing new. `purchase` re-confirmed only. |
| G09 CRM | 11 | Nothing new. `crm` re-confirmed only; its dependency list is not a group-membership pairing. |
| G10 ACCOUNT_PROCESS | 13 | Nothing new. Zero modules ever paired to G10 in any reviewed document. |
| G15 DASHBOARD_REPORT | 11 | Nothing new. Zero modules ever paired to G15 in any reviewed document. |

**New confirmed pairings found in this pass: 0.**
**Groups with "nothing new" outcome: 8 of 8** (all eight targeted groups).

No group among G02/G03/G04/G06/G07/G09/G10/G15 came closer to a fully resolved roster as a
result of this pass. The closest to resolved among this priority set remain the single-anchor
groups already in the candidate TSV — G03 (3 of 11 named: `product`, `uom`, `analytic`), and
G06/G07/G09 (1 of 12, 1 of 9, 1 of 11 named respectively: `mrp`, `purchase`, `crm`) — exactly
as recorded before this deep-dive. G02, G04, G10 and G15 remain at 0 of their governed counts.
The underlying blocker is unchanged: the row-level `GROUP_STRUCTURE_V2_CORE.tsv` bytes (SHA-256
`203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`) are still not present or
reachable anywhere in this repository or its connected evidence surfaces, and every source
document that touches these eight groups is internally consistent and explicit that no further
module name should be inferred, guessed, or credited without that artifact (or an equivalent
Boss-issued superseding roster).

## What would resolve this

Unchanged from the candidate TSV's README: recovery of the controlled
`GROUP_STRUCTURE_V2_CORE.tsv` row-level bytes, or a Boss-issued superseding roster artifact
with path, revision/date, SHA-256, module count, and exact membership.
