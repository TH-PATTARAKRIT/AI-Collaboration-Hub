# COA-G01 Round 2 — Workbook Provenance and Row Lineage

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Reconcile primary workbook file identity, extraction method, row lineage and limitations | Claude (session SMEPLUS-26-08-30-COA-G01R2-001) | `COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`; whole-volume filesystem search | 2026-08-31 | ChatGPT Independent Review (pending); Boss (pending) | **HOLD / EVIDENCE REQUIRED — primary file unrecoverable from this environment** | Closes AR record E-03; reconfirms R-07 |

## 1. File identity

| Field | Value | Evidence character |
|---|---|---|
| Filename | `Account_Odoo18_19 sent 270369.xlsx` | Source Observation (as recorded in the inventory document) |
| Boss-designated tab | `Odoo18` | Boss Ruling (which tab is authoritative) |
| Google Drive file ID | `1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f` | Source Observation |
| Source URL | `https://docs.google.com/spreadsheets/d/1KoprCep3eeYy49OcV0TTFQOlc1zq9m2f/edit` | Source Observation |
| Content hash (SHA-256 or other) of the workbook itself | **None recorded anywhere** | Unclassified/Missing |
| Local copy on this filesystem | **None found** | Unclassified/Missing |

## 2. Extraction method (as documented)

The inventory document (commit `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`) describes the extraction as reading the workbook "through its full serialized row range" via what it calls a "connector text projection" — no named tool (no `pandas`, `openpyxl`, Google Sheets API version, or export format is cited). An unlabeled leading row-index column is treated as projection metadata, not a data column. **This is a real limitation**: the extraction method is not independently reproducible from the documentation alone; a future auditor with Drive access would need to re-derive the same projection method, not merely re-open the file.

## 3. Row lineage

- Header row present; data rows indexed **0–388** → **389 total data rows**.
- 5 business columns: `id`, `name`, `reconcile`, `code`, `account_type`.
- 14 distinct `account_type` labels observed across the 389 rows.
- Row-level spot values (row 0, row 11, rows 385–388) are quoted in the `COA_STANDARD` reconciliation documents but originate from the same single extraction pass — they are not independently re-derivable evidence, they are excerpts of the same primary claim.

## 4. This session's independent verification attempt

A whole-volume filesystem search (`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/`, all subfolders including `ACCOUNT/`, `06 MIGRATION FACTORY/`, `GROUP A/`, and the git clone) for filenames containing `Odoo18` or `270369` found **exactly one match**: the markdown inventory document itself. **No `.xlsx` file, no Google Drive sync cache, and no other trace of the workbook exists anywhere on this volume.** The only `.xlsx` files present under `ACCOUNT/` are generic Odoo import/demo templates (`coa_import_template.xlsx`, `aml_import_template.xlsx`, `test.xlsx`) — unrelated to the Boss-approved workbook.

This independently reconfirms Round 1's own finding, registered as `COA_G01_OPEN_UNKNOWN_REGISTER.md` item **N-01**.

## 5. Effect on commit `c530138`'s "direct re-verification" claim

`c530138` (see `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`) states the workbook was *"directly re-verified in connected Drive during G01 execution"* and quotes rows 0, 11, and 385–388. This session:

- did not have Drive-connector access invoked at any point in its own investigation of this claim (Google Drive is not among this session's connected tools);
- found no updated extraction artifact, hash, or log accompanying that claim;
- therefore **can neither confirm nor refute** the claim.

Per the user's explicit control treatment, this claim is **not used as Gate closure evidence**. The row values it quotes are consistent with (not contradictory to) the original 389-row/14-type extraction already on record, so this session does not flag a *numeric* conflict — only an *unverified-source* conflict (see `COA_G01_SOURCE_CONFLICT_REGISTER.md` C-07).

## 6. What this reconciliation does NOT claim

Per `DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`'s own "What Is Not Yet Claimed" section (reaffirmed, not re-litigated, by this session): this document does not prove or approve duplicate-account disposition, final numbering ranges, final canonical Account Type IDs, final account-by-account mapping, Balance Sheet/P&L correctness for every row, VAT/WHT dependency mapping for every row, multi-company extension policy, or exact final Thai COA content. All such work is COA-G02/G03/G05/G06 scope.

## 7. Recommended remediation (not authorized to execute by this session)

1. Boss to provide either (a) direct, controlled access to the source `.xlsx` for this session to independently extract and hash, or (b) an explicit ruling that the Google Drive link is the permanent system of record and no local copy is required.
2. If (a): re-run extraction with a named, reproducible tool and record a SHA-256 of the workbook file itself (not just the markdown describing it).
3. Any future claim of "re-verification" of this workbook should be accompanied by an updated extraction artifact and hash, not asserted inline in a design document.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
