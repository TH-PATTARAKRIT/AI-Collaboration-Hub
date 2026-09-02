# 12 — NEXT CONTROLLED PROMPT PACKS

| Field | Value |
|---|---|
| Source | `22_NEXT_PROMPT_RECOMMENDATION.md` §2; this package's `02`–`11` |
| Purpose | Give each routed item in this package a ready identifier and a minimal prompt-pack skeleton, so Boss can authorize each as a **separate controlled session** without re-deriving scope from scratch |
| Rule | `None may be merged into another without a Boss decision` (governing prompt §3; source `22` §1). Each pack below is a distinct future prompt — none is authorized by this document. |

| Pack ID | Depends on this package's decisions | Suggested session prompt ID | Consumes | Produces | Owner to commission |
|---|---|---|---|---|---|
| `PP-01` | `ACC-DEC-001..017` (Boss decision batch resolved) | `SMEPLUS-26-09-0X-ACC-BOSS-DECISION-RESOLUTION-001` | This package's decision forms (`02`–`05`, `11`), completed | Signed decision record for every `ACC-DEC-*` row | Boss (self-executes, or commissions a session to formalize the paper trail) |
| `PP-02` | `ACC-DEC-018` (COA-G01 unblock) | `SMEPLUS-26-09-0X-COA-G01-UNBLOCK-001` | `09_COA_G01_UNBLOCK_ROUTING_PACK.md` | Restored evidence, N-05/C-03 resolution, CORR5 independent re-audit output, PMO checklist sign-off | Boss / PMO / independent (ChatGPT Audit role) reviewer |
| `PP-03` | `ACC-DEC-014` (legal-tax commissioning) | `SMEPLUS-26-09-0X-ACC-LEGAL-TAX-REVIEW-001` | `06_LEGAL_TAX_REVIEW_BRIEF.md` | Authoritative citations for WHT/VAT/CIT/DBD-NPAE items, in the evidence-field format | Licensed Thai tax/accounting adviser (UNASSIGNED) |
| `PP-04` | `ACC-DEC-019` (Joint Session 3 convening) | `SMEPLUS-26-09-0X-ACC-INV-JOINT-SESSION-3-001` (Jira `ERPPLUS-140`) | `07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md`, Inventory reopen's own file 20 | Resolution of `G-1`, `G-2`, `G-3`, `G-5`, `G-6`, return-basis conflict, posting-architecture fork, and remaining agenda items | Boss (convene) / Joint (Account + Inventory) |
| `PP-05` | `ACC-DEC-015` (naming acceptance) | `SMEPLUS-26-09-0X-ACC-TBRAC-NAMING-VALIDATION-001` | `08_TBRAC_THAI_NAMING_VALIDATION_BRIEF.md` | Per-item TBRAC verdicts, corrected mistranslated labels, technical-vs-display name mapping | TBRAC panel (UNASSIGNED) |
| `PP-06` | `ACC-DEC-004`/`005` scope rulings | `SMEPLUS-26-09-0X-ACC-AR-AP-ASSET-RESEARCH-001` | `10` §A | AR/AP aging, allowance/write-off, asset roll-forward, deferral-schedule findings; unblocks `MG-C11` | Team A research (UNASSIGNED) |
| `PP-07` | `ACC-DEC-007` owner assignment | `SMEPLUS-26-09-0X-ACC-TREASURY-CASH-BANK-001` | `10` §B | Bank journal, statement-format, reconciliation, PromptPay, PDPA findings | Treasury (UNASSIGNED) |
| `PP-08` | `PP-02` + `PP-03` complete | `SMEPLUS-26-09-0X-ACC-FIN-STATEMENT-TAXONOMY-COA-G05-001` | `10` §C | Canonical-account-to-NPAE-statement-line mapping; Off-Balance rule design | Team B (once `COA-G01`–`G04` clear) |
| `PP-09` | `ACC-DEC-017` | `SMEPLUS-26-09-0X-ACC-REOPEN-G-A3-LINEAGE-001` (only if Option A selected in `11`) | `11` | Recreated 18-deliverable package, or formal closure record if Option B/C selected instead | Boss / assigned executor |
| `PP-10` | `ACC-DEC-016` | *(governance action, not necessarily a new AI session)* | `11` | Merge or index action per Boss's selected option | Boss / repo owner |

## Explicit sequencing constraint (from governing prompt §3, item on what must NOT be the next prompt, mirrored from source `22` §3)

No pack above authorizes:

- Team B functional/UX design of accounting menus from this package alone (blocked until `COA-G01` clears and Thai statutory evidence exists)
- Team C / development / production work
- Treating benchmark (Odoo) behaviour as approved SMEsPlus behaviour
- Closing Inventory-owned or Joint items from the Account side (applies to `PP-04`)

## How to use this file

Boss picks one or more `PP-*` rows to authorize as the next session(s). Each row is self-contained enough to become that session's opening brief. This file does not itself commission anything.
