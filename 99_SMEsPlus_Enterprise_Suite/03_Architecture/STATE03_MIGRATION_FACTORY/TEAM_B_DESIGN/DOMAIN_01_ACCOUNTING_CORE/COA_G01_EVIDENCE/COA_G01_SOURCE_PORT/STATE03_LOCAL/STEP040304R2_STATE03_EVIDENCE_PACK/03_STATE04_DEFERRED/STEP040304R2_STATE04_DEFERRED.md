# STEP040304R2 — Q8: FINDINGS THAT STAY IN STATE04 / DEVELOPMENT / FUTURE DESIGN

These must NOT enter the STATE03 architecture freeze. They are implementation-level,
evidence-gap, or hygiene items.

## D1 — `account_payment_multi_deduction` MISSING (was AF6) — EVIDENCE GAP
`l10n_th_withholding_tax_multi` requires it; it is absent from all 1,502 supplied modules.
The ONLY unresolved dependency in the entire scope. Boss ruling: HOLD.
STATE04 action: obtain the module, or specify multi-deduction WHT from RD rules and the DB
dump instead. Does NOT block the architecture freeze — multi-deduction is a behaviour
variant within the S2/S4 model, not a new architectural concept.

## D2 — WHT CONDITION / TAX PAYER VALUE SET — DESIGN DETAIL
The specific enumerations (PND1/PND3/PND3a/PND53, withholding vs paid_one_time, the Thai
RD income-type list) are functional specification content. They are captured in
STEP040304 FE3 and belong to functional design, not to the architecture baseline.
S4 freezes the PRINCIPLE (versioned reference data); D2 carries the VALUES.

## D3 — REPORT COLUMN SETS — FUNCTIONAL SPEC
The PND output field list (vat, title, name, street, street2, city, state_name, zip,
branch_number, date, tax_amount, tax_base_amount, wht_amount, wht_condition, tax_type)
is evidence of required report content. It informs functional design; it does not
constrain the architecture beyond S3/S5.

## D4 — DEAD FILE IN REFERENCE SOURCE (was AF8) — EVIDENCE HYGIENE
`l10n_th_withholding_tax_report/models/report_withholding_tax copy.py` exists but is not
imported. Relevance under clean-room: it is an UNRELIABLE EVIDENCE SOURCE. Any behaviour
seen only in that file must not be treated as reference behaviour. No other impact —
SMEsPlus ships none of this code.

## D5 — UNRESEARCHED SCOPE — COVERAGE GAP
STEP040304 researched the Thailand functional domain (14 modules) plus interpretive
context. NOT yet researched: the non-Thai Boss Extra modules (approvals, printing,
sequences, product/UoM, purchase/sale extensions) and the 63 core dependencies.
STATE04 action: a follow-on step for the non-Thai Boss Extra set. This is a COVERAGE gap,
not a defect, and it is bounded and known.

## D6 — 664 RETAINED, UNAPPROVED MODULES
03_LEARNING holds 664 modules outside the approved 134. Available, never studied.
STATE04 action: leave dormant unless a specific evidence need arises; do not expand scope
silently.
