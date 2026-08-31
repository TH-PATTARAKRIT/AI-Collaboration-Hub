# COA-G01 — Clean-Room Provenance Check

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Verify clean-room provenance coverage specifically for COA-G01 evidence and the COA_STANDARD design artifacts | Claude (session SMEPLUS-26-08-30-COA-G01R-001) | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` | 2026-08-30 22:27 +0700 | ChatGPT Independent Review (pending); Boss (pending) | HOLD / EVIDENCE REQUIRED — coverage gap identified | Blocks claiming clean-room PASS specifically for COA_STANDARD/COA-G01 work; does not indicate any actual violation |

## What was checked

`B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` was read in full. It records:

- 16 matrix rows, each mapping a design decision to a provenance category and citation; every row's "Vendor-derived risk" column reads `NONE`.
- 3 additional rows reviewing vendor-specific terminology for whether it was adopted into design (all: "Adopted into design? No").
- Acceptance check: *"Critical Vendor-Derived Design Risk: 0... Acceptance criterion met — B14 = COMPLETE. Not a STOP condition."*

## Gap identified

The matrix contains **zero** citations of, or rows addressing, any of the three `COA_STANDARD` documents used as direct evidence in this COA-G01 remediation pass:

- `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`
- `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md`
- `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`

The phrase "Account Type" does not appear anywhere in B14. Exactly one row (of 16) touches Chart of Accounts at all, and it addresses only the template/instance sharing design option (citation `GAP-D01-05`), not Account Type taxonomy or the Odoo18 row/column extraction.

## Classification

This is recorded as a **coverage gap**, not a violation:

- No evidence exists that vendor source code, schema, ORM structure, or technical IDs were copied into the COA_STANDARD documents — but no evidence exists that this was *checked* either, for these three specific documents.
- The COA_STANDARD documents' own content (as read during this session) describes business facts (row counts, Account Type labels, column names as observed data) rather than asserting vendor architecture as SMEsPlus architecture, which is consistent with clean-room intent — but this session's role is to register the gap, not to self-certify clean-room compliance for documents it did not author.

## Status

**HOLD / EVIDENCE REQUIRED.** Overall project Critical Vendor-Derived Design Risk remains reported as 0 for everything B14 actually reviewed; that reported "0" does not extend to the COA_STANDARD documents, which require their own clean-room provenance pass before COA-G01 (or COA-G02/G03, which build directly on COA_STANDARD) can cite clean-room PASS as fully evidenced for Chart-of-Accounts work specifically.

## Recommended remediation (not authorized to execute by this session)

Either (a) extend `B14_CLEAN_ROOM_PROVENANCE_MATRIX.md` with dedicated rows for the three COA_STANDARD documents, or (b) create a dedicated `COA_CLEAN_ROOM_PROVENANCE_MATRIX.md` scoped to Chart-of-Accounts design work. This session does not choose between (a) and (b) — see `COA_G01_OPEN_UNKNOWN_REGISTER.md` item N-03.

## Round 2 update (2026-08-31): coverage gap has grown, not shrunk

A fourth document was added to `COA_STANDARD/` after this gap-check was originally written: `DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md` (commit `c530138`, part of the unverified self-declared package — see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07). B14 does not cover this file either — it postdates B14 entirely. The clean-room coverage gap identified in Round 1 is reconfirmed **and now spans 4 documents, not 3**. Status remains **HOLD / EVIDENCE REQUIRED**; the recommended remediation above is unchanged and still not executed.

## CORR1 (2026-08-31): executed document-level clean-room provenance review of all 4 `COA_STANDARD` documents

Per Boss correction directive `COA-G01R2-CORR1`, this section performs the actual review B14 never covered, rather than restating that the gap exists. Each document was read in full and checked against B14's own method: (a) does every material design decision map to a provenance category with a citation, (b) is vendor-specific terminology (technical field names, internal enum keys, ORM/schema structure) adopted into SMEsPlus's own target design anywhere in this document or the documents/artifacts that build on it, (c) is there a Critical Vendor-Derived Design Risk. Classification uses four values: `VERIFIED CLEAN-ROOM BOUNDARY`, `COVERAGE GAP`, `CONFLICTING EVIDENCE`, `EVIDENCE_MISSING`.

| Document | Finding | Classification | Rationale |
|---|---|---|---|
| `DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md` | Cites literal Odoo internal enumeration keys (`asset_receivable`, `liability_credit_card`, `off_balance`, etc. — the actual Selection-field technical values, per Team A `SE-17`) in a column explicitly labeled "Source key," always paired with an independent "Business-facing label" (Receivable, Credit Card, Off-Balance Sheet). Every downstream document that uses these concepts (`COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`, `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md`) uses only the business-facing labels — the snake_case vendor keys are never adopted as SMEsPlus identifiers anywhere in this evidence base. | **VERIFIED CLEAN-ROOM BOUNDARY** | Vendor technical keys are cited as evidence only, in an explicitly separated column, and are not carried forward as target identifiers. Residual recommendation (not a blocker): add a one-line explicit clean-room disclaimer to this document itself, since the discipline is followed but never stated in writing the way B14 states it for its own 16 rows. |
| `DOMAIN_01_COA_BASE_KERNEL_AND_AI_CONSOLIDATION_STANDARD.md` | Defines original methodology (Track A/Track B classification, 13 Do-Not-Merge rules, dimension-over-proliferation principle, 5-outcome classification model). No vendor source code, schema, table, or ORM structure is referenced — only generic evidence-source *paths* are named (e.g. `l10n_th/models/template_th.py`) as places to look, not structures to copy. | **VERIFIED CLEAN-ROOM BOUNDARY** | Content is original design methodology end-to-end; no vendor architecture citation of any kind beyond naming where evidence should be gathered from. |
| `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md` | The extraction's 5 business columns — `id`, `name`, `reconcile`, `code`, `account_type` — are identical to real Odoo ORM field names on `account.account` (Team A `SE-17`, `SE-19`, `SE-20`). No document in this evidence base proposes these as SMEsPlus's own database/schema field names — they describe the *source workbook's* column structure, which happens to mirror the vendor model it was exported from. But unlike document 1 above, this document does not explicitly separate "observed source column name" from "target design element" in writing. | **COVERAGE GAP** | On inspection, no vendor architecture is adopted as target design — but the document lacks the explicit disclaimer that would make this a confident `VERIFIED CLEAN-ROOM BOUNDARY` rather than an inference this reviewer had to draw. Recommend: add an explicit line stating these column names describe the source extraction only and are not proposed SMEsPlus schema. |
| `DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md` (commit `c530138`) | Restates the same business-facing-label pattern as documents 1 and 3 (no new vendor-architecture citation introduced). However, this document's own evidentiary status is independently compromised — see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07 (self-declared PASS, no independent review trail). | **CONFLICTING EVIDENCE** | Content review alone would support the same classification as document 3, but certifying this document's clean-room boundary as "verified" would lend it credibility this evidence base has explicitly withheld elsewhere. Its clean-room status is therefore tied to, and inherits, its general provenance status: unresolved. |

**Net effect on the overall Gate-level clean-room status:** 2 of 4 documents `VERIFIED CLEAN-ROOM BOUNDARY`, 1 `COVERAGE GAP` (now with a concrete, actionable one-line fix rather than an open-ended gap), 1 `CONFLICTING EVIDENCE` (tied to C-07, not independently resolvable without resolving C-07 first). This is genuine progress from Round 2's "zero rows reviewed" state, but the overall Gate-level clean-room status remains **HOLD / EVIDENCE REQUIRED** — not `PASS` — because two of the four documents do not yet clear the bar on their own terms (one needs a one-line disclaimer added and independently re-reviewed; the other cannot clear until its host commit's provenance issue is resolved).

## CORR1 late update (2026-08-31): the 4th document has since been removed by the repository owner

After the review above was written but before this correction pass was committed, commit `58ab36d6f8cd70843553de01be892e444ea7b784` ("Revert accidental WEBSITE-session write to SMEsPlus," pushed 2026-08-31 08:07:09 +0700, outside this session) deleted `DOMAIN_01_COA_G01_SOURCE_BASELINE_RECONCILIATION.md` (the `c530138` document, row 4 above) from `COA_STANDARD/`, confirming it was accidental cross-session content rather than a genuine COA-G01 artifact.

**Effect:** `COA_STANDARD/` now contains **3 documents again**, matching Round 1's original scope. The `CONFLICTING EVIDENCE` row above is retained in this document as a historical record of what was reviewed and why (the review was correct to withhold a clean classification), but it no longer describes a file present on the branch. The clean-room coverage gap for the **remaining 3 documents** is unchanged from the assessment above: 2 `VERIFIED CLEAN-ROOM BOUNDARY`, 1 `COVERAGE GAP` (the Odoo18 Tab Source Inventory document, needing the one-line disclaimer). B14 itself still does not cover any of the 3. Status remains **HOLD / EVIDENCE REQUIRED**.
