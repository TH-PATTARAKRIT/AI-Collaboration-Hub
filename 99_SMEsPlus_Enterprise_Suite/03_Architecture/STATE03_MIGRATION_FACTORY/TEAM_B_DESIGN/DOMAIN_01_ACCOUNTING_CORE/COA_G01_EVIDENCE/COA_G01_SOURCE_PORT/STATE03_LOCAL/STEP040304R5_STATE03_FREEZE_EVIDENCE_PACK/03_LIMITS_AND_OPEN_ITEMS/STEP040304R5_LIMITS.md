# STATE03 FREEZE EVIDENCE PACK — PART 3: LIMITS AND OPEN ITEMS

Stated plainly, because a freeze built on overstated evidence is worse than a delayed freeze.

## L1 — PERMANENT LIMIT: 19 MODULES ARE BLACK-BOX FOREVER
11 OPL-1 (Boss Extra) + 8 OEEL-1 (Odoo Enterprise). Never parsed, at any point.
This is not a backlog item — clean-room rules make it permanent. Includes
`l10n_th_reports` (Thai statutory reports) and `bm_thai_rd_vat_company_search` (Thai RD
VAT lookup). Anything these do can only ever be learned by observed behaviour.

## L2 — OPEN DEPENDENCY: S1, AND ITS EVIDENCE ROUTES
S1 (Thai statutory reporting not source-observable) is the only freeze-blocking finding.
| Route | Status |
|---|---|
| (a) Thai Revenue Department published forms and rules | AVAILABLE — primary authority, not yet worked |
| (b) Black-box observation of a running reference system with purpose-entered data | AVAILABLE — **requires Boss authorisation, not yet given** |
| (c) The database dump | **STRUCK — CLOSED AS UNAVAILABLE** |

Route (c) was struck at STEP040304R3C on evidence: the dump holds 6 journal entries,
23 journal lines and **ZERO withholding tax certificates**. `iTEST02` is a configuration/UAT
database, not a production dataset. No further database work can change this; the
transactions were never entered.

## L3 — COVERAGE IS BACKEND-ONLY AND THAILAND-WEIGHTED
127 website/eCommerce/theme modules are held for Version 2 and were NOT researched.
664 modules remain in 03_LEARNING outside the approved scope and were never studied.
The freeze this pack supports covers **Thailand-driven and backend architecture decisions**.
A freeze claiming full ERP coverage is NOT supported by this evidence.

## L4 — SOURCE AND DUMP ARE DIFFERENT BUILDS
STEP040304R3B found bidirectional drift on `withholding_tax_cert`: source has `signature`
the dump lacks; the dump has `amount_pension_fund` / `amount_provident_fund` /
`amount_socialsecurity_fund` the source lacks. The rest of the Thai WHT core matches exactly.
RULE CARRIED FORWARD: source and dump are two SEPARATE evidence instruments. They are never
merged, and a field present in only one is never stated as confirmed behaviour.
The fund columns are empty (zero cert rows), so the PND1 payroll-WHT scope question must be
decided on schema evidence alone.

## L5 — GAP-1 CLOSED ONLY TO THE CLEAN-ROOM BOUNDARY
Boss Extra source-to-dump mapping was produced for 58 of 69 modules. The other 11 are
black-box and are structurally unmappable from source. Closed as far as the rules allow.

## L6 — ONE EVIDENCE-INTEGRITY DEFECT NOT YET CORRECTED
The V2.0 closure pack presents 14 CSV files but contains 13 distinct artefacts:
`Field_Level_Source_to_Dump_Mapping.csv` and `ORM_Field_Inventory_and_DB_Mapping.csv` are
byte-identical (SHA-256 a5667402…2d1bc8dc). Recommended corrected before the pack is cited
in a signed freeze. Boss ruling R5 at STEP040304R3A, still open.

## L7 — CARRIED-FORWARD ITEMS STILL UNANSWERED
| Origin | Item |
|---|---|
| STEP040302 | R4 generic WHT engine `l10n_account_withholding_tax` — admit as Thai dependency? |
| STEP040302R2A | 8 residual non-TH localization modules not matching the `l10n_*` prefix |
| STEP040304R3B | R2 PND1 payroll WHT in scope? (now decidable on schema alone — see L4) |
| STEP040304R3C | R2 authorise route (b)? |
| STEP040304R3A | R5 correct the duplicate artefact (see L6) |
