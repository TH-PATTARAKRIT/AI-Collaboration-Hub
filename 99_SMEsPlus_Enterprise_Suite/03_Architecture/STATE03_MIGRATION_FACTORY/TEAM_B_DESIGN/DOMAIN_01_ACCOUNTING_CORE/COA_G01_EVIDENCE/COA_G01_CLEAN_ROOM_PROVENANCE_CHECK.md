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
