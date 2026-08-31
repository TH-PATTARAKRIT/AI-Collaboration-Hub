# STATE03 FREEZE EVIDENCE PACK — PART 2: FINDINGS REGISTER (S1–S11)

Consolidated from STEP040304R2 (S1–S6) and STEP040304R4 (S7–S11). No finding is new here.

| ID | Finding | Domain | Evidence | Freeze impact |
|---|---|---|---|---|
| S1 | Thai statutory reporting is NOT source-observable | Evidence | l10n_th_withholding_tax -> l10n_th_reports (OEEL-1) -> account_reports (OEEL-1) | **OPEN DEPENDENCY** |
| S2 | WHT is recognised at payment, not invoice | Transaction model | wt_tax_id on account.move.line AND account.payment; PND query filters payment_state | Posting engine |
| S3 | Thai party identity exceeds a generic partner model | Data model | l10n_th_partner.branch, name_company; PND emits branch_number | Party model |
| S4 | Statutory reference data must be versioned data, not code | Reference data | PND maps income type from literal rates; cert carries a richer, unreconciled list | Reference-data architecture |
| S5 | Tenancy must be tenant -> legal entity -> tax branch | Tenancy | company_id on all Thai models; Thai filing is per branch | Tenancy model |
| S6 | Payment gateway independent of storefront | Service decomposition | payment_2c2p depends on website_sale | Service boundaries |
| S7 | Tenant-administrable, data-driven RBAC | Authorisation | dynamic.access.right by module/model, users M2M, menu detail | **Authorisation architecture** |
| S8 | One request/approval abstraction, not per-document copies | Service decomposition | identical _STATES duplicated in purchase_request and advance_expense_request | Workflow service |
| S9 | The journal entry is the extension hotspot | Core accounting | account.move extended 10x, account.move.line 8x across Boss Extra | Core model design |
| S10 | Audit trail/activity is a platform service | Platform | tracking=True on request states; mail 83 decls; cert inherits mail.thread | Platform layer |
| S11 | Print layout is configuration data | Documents | cheque.setting 76 fields; ir.actions.report extended 6x | Rendering service |

## FUNCTIONAL REQUIREMENTS BASELINE (C1–C8, from STEP040304R4)
The Boss Extra set is the closest thing in this evidence base to a written requirements
statement — it is what had to be built because stock Odoo did not do it.
| ID | Capability | Why it matters |
|---|---|---|
| C1 | Purchase requisition with approval, procurement-linked, Thai urgency vocabulary | No stock equivalent |
| C2 | Employee advance-and-clear cycle (เงินทดรองจ่าย) | Thai accounting workflow, posts to journal |
| C3 | Data-driven access control | Basis of S7 |
| C4 | Cheque printing, 76-field layout config | Basis of S11 |
| C5 | Fiscal period abstraction (date_range) | Feeds Thai WHT reporting, supports S5 |
| C6 | Sales dimensions: brand / channel / office | Analytical model |
| C7 | Backup config, courier, Monday sync, Thai titles, customer product info, audit report | Supporting |
| C8 | Extension hotspots: account.move 10x, res.partner 8x, product.template 8x | Basis of S9 |

## THAILAND FUNCTIONAL EVIDENCE (FE1–FE8, from STEP040304)
WHT master data model · WHT bound to both invoice line and payment · WHT certificate as a
statutory document (PND1/PND3/PND3a/PND53, draft->done->cancel, signature, Thai RD income
types) · PND report field set including tax branch · Thai party identity · Thai baht
amount-in-words · SMEsPlus VAT report hook · PromptPay.

## DATABASE-DERIVED CONFIRMATION (STEP040304R3C)
WHT rates actually configured are exactly {1, 2, 3, 5} — matching the hardcoded PND map,
which is why the S4 defect never surfaced in practice. Income type is encoded in a NAME
STRING ("1% WH C T"), and corporate vs personal withholding is split across two GL accounts
— the PND53 / PND3 distinction expressed as configuration. Direct support for S4.
