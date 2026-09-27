# GROUP_STRUCTURE_V2_CORE — CANDIDATE Compilation (2026-09-28)

**STATUS: CANDIDATE — NOT BOSS-APPROVED, DO NOT TREAT AS CANONICAL.**

This file and its companion `GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` are a
compiled-from-evidence draft only. They are not the controlled `GROUP_STRUCTURE_V2_CORE.tsv`
roster (historical SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`,
299 rows), which remains **NOT PRESENT** in this repository. Nothing in the candidate TSV
converts any HOLD-SHARED group into ELIGIBLE, ACTIVE-ROSTER, or Formal-Coverage status.
Question authoring, A2 Blind Runtime, Reconciliation, A3, MASTER consolidation, and Formal
Coverage all remain governed exactly as before this compilation — see
`OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md`, which this candidate does not supersede or
weaken in any way. This document exists solely so the Boss has one consolidated, traceable
artifact to review, correct, or freeze — not to pre-empt that review.

No module name in the candidate TSV was invented, guessed, prefix-matched, category-matched,
dependency-inferred, or filled in to reach a target count. Every row is either (a) a module
name that a real, already-committed A1/RED TEAM evidence document explicitly states belongs to
a named group, or (b) an explicit GAP marker recording that a group's governed count is known
but its named-module evidence could not be found in the repository. Where a source document
itself labels a finding "candidate," "not credited," or "no canonical membership credit," this
compilation preserves that same caveat in the `notes` column rather than upgrading it to a firm
claim.

## What this is built from

Read in full for this compilation:

- `GMVQ/OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md` (the standing HOLD notice)
- `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md` (governed group counts, cross-check table)
- `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/` (all 23 files — the already-frozen G01 roster)
- `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` (Boss-frozen G01 module list, cross-checked byte-for-byte against the 23 Lane A Pass-1 files — exact match)
- `A1_SOURCE_EVIDENCE_LANE/G01_G04_RED_TEAM_STATIC_CHECKPOINT_R14_20260925.md` and R2/R3/R4/R5/R6/R9/R11 in the same directory
- `A1_SOURCE_EVIDENCE_LANE/G05_G08_A1_PARALLEL_STATIC_INTAKE_V1.00.md`
- `A1_SOURCE_EVIDENCE_LANE/G05_G08_RED_TEAM_A1_STATIC_DELTA_R10/R4/R3_20260925.md` and `G05_G08_RED_TEAM_A1_CHECKPOINT_R2_20260925.md`
- `A1_SOURCE_EVIDENCE_LANE/G09_G12/A1_G09_G12_PARALLEL_STATIC_CHECKPOINT_20260924.md` (including its R10/R11 delta pointers and RT status note)
- `A1_SOURCE_EVIDENCE_LANE/G13_G16_A1_ROSTER_RECONCILIATION_AND_STATIC_INTAKE_V1.00.md`
- `A1_SOURCE_EVIDENCE_LANE/G13_G16_RED_TEAM_A1_STATIC_DELTA_R4_20260925.md`
- `A1_SOURCE_EVIDENCE_LANE/G13_G16_RED_TEAM_PARALLEL_CHECKPOINT_20260925.md`

## Totals versus the historical/current targets

| Denominator | Value | Candidate rows found | Coverage |
|---|---:|---:|---:|
| Historical `GROUP_STRUCTURE_V2_CORE.tsv` (299 modules, installed set) | 299 | 40 named modules | ~13% |
| Current 247-module study scope (`MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) | 247 | 40 named modules | ~16% |

These percentages are descriptive only, not a Formal Coverage claim. Formal Coverage remains
NOT AUTHORIZED because no Canonical Function-ID denominator is Boss-frozen — nothing here
changes that.

The TSV has **54 total rows**: 40 rows name an actual module technical name (32 `CONFIRMED`,
8 `DERIVED`), and 14 rows are `GAP` placeholders — one per group that still has unresolved
membership, recording how many of that group's governed count remain unnamed rather than
inventing names to fill them.

## Per-group breakdown

| Group | Name | Governed count | Named modules found | Status |
|---|---|---:|---:|---|
| G01 | PLATFORM_BASE | 23 | 23 (all CONFIRMED) | **FULLY EVIDENCED** — already Boss-frozen (FREEZE_W1-STD.json); matches exactly |
| G02 | IDENTITY_ACCESS | 11 | 0 | GAP — candidate leads only (auth_password_policy, auth_oauth, auth_totp, auth_passkey, auth_ldap), explicitly "NO CANONICAL MEMBERSHIP CREDIT" in source |
| G03 | MASTER_DATA | 11 | 3 (CONFIRMED: product, uom, analytic) | PARTIAL — 8 of 11 rows still GAP |
| G04 | ACCOUNT_BASE | 9 | 0 | GAP — `account` boundary examined but explicitly not attributable to ACCOUNT_BASE vs ACCOUNT_PROCESS without the roster |
| G05 | INVENTORY | 14 | 1 (CONFIRMED: stock) | PARTIAL — 13 of 14 rows still GAP |
| G06 | MANUFACTURING | 12 | 1 (CONFIRMED: mrp) | PARTIAL — 11 of 12 rows still GAP |
| G07 | PURCHASE | 9 | 1 (CONFIRMED: purchase) | PARTIAL — 8 of 9 rows still GAP |
| G08 | SALES | 31 | 1 (CONFIRMED: sale) | PARTIAL — 30 of 31 rows still GAP |
| G09 | CRM | 11 | 1 (CONFIRMED: crm) | PARTIAL — 10 of 11 rows still GAP |
| G10 | ACCOUNT_PROCESS | 13 | 0 | GAP — `account` explicitly examined as a cross-group process anchor only; source states ownership by G10 is NOT claimed |
| G11 | EVENTS | 8 | 8 (all DERIVED) | FULL COUNT MATCH, but reconstructed from a historical "event* (8)" rule + registry, explicitly labelled CANDIDATE/not yet roster-certified — not CONFIRMED |
| G12 | PROJECT_SERVICES | 20 | 1 (CONFIRMED: project) | PARTIAL — 19 of 20 rows still GAP (hr_timesheet/sale_project/sale_timesheet named as bridge candidates only, not credited) |
| G13 | PEOPLE | 29 | 0 | GAP — source-trace leads only (hr, hr_attendance, hr_holidays, hr_expense, hr_recruitment), explicitly not promoted as roster |
| G14 | COLLABORATION | 16 | 0 | GAP — "no module is credited to G14" per source |
| G15 | DASHBOARD_REPORT | 11 | 0 | GAP — "no module is credited to G15" per source |
| G16 | TECHNICAL_INTEGRATION | 19 | 0 | GAP — "no module is credited to G16"; historical 20→19 one-row delta remains unresolved and is not guessed here |

**Fully evidenced:** G01 only.
**Full count reconstructed but still candidate-grade:** G11 (all 8 rows DERIVED, not CONFIRMED).
**Partially evidenced (single named anchor module out of a larger governed count):** G03, G05, G06, G07, G08, G09, G12.
**Entirely unevidenced (GAP for the whole governed count):** G02, G04, G10, G13, G14, G15, G16.

## Why some anchor rows are marked CONFIRMED even though the group is mostly GAP

`source_confidence` in the TSV is scored per row, not per group. Several A1/RED TEAM documents
explicitly pair one specific module name with a specific group in prose (for example: *"G05
INVENTORY — verified source anchor `stock`"*, or *"Anchor module: `crm`"* under the G09 CRM
heading). That single pairing meets the CONFIRMED bar for that one row even though the same
source document is explicit that the remaining members of that group's governed count are
**not** established and must not be inferred. Each such row's `notes` column quotes the
source language and states the remaining-count GAP explicitly, so a CONFIRMED row for one
module never overstates the group's overall roster completeness.

## What this candidate does NOT do

- It does not reduce, soften, or reinterpret the standing HOLD-SHARED status on G02–G16 set by
  `OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md`.
- It does not authorize GMVQ question authoring, A2 Blind Runtime, Reconciliation, A3, or
  MASTER for any group beyond what was already authorized before this compilation.
- It does not resolve the historical G16 20→19 module delta, the G02 11-row auth-family
  candidate question, or the G09/G10/G12 exact-roster recovery — those remain open exactly as
  the underlying evidence documents describe them.
- It is not a substitute for recovering the actual `GROUP_STRUCTURE_V2_CORE.tsv` bytes (or a
  Boss-issued superseding 247-row roster) from the offline authorized desktop device or another
  controlled source.

## What would resolve this

Recovery of the controlled `GROUP_STRUCTURE_V2_CORE.tsv` row-level bytes (or a Boss-issued
superseding roster artifact with path, revision/date, SHA-256, module count, and exact
membership), so MASTER and GMVQ can replace every `GAP` and `DERIVED` row in this candidate
with a Boss-approved, row-level CONFIRMED membership record — or an explicit Boss ruling on
this candidate itself.
