# STEP040304R2 — Q7: FINDINGS THAT FEED STATE03 ARCHITECTURE FREEZE

RESTATEMENT NOTICE. STEP040304 findings AF1–AF8 were written before the §2 identity
correction, and were phrased as if SMEsPlus would deploy Odoo. Under a clean-room Node.js
SaaS target, several of them mean something different. They are restated here as S1–S6.
Where the meaning changed, the change is stated explicitly.

---

## S1 — THAI STATUTORY REPORTING IS NOT SOURCE-OBSERVABLE **[FREEZE-BLOCKING]**
Restates AF1 + AF7. **Meaning changed.**
Was: "SMEsPlus needs an Odoo Enterprise licence."
Now: SMEsPlus will not ship Odoo at all, so licensing is irrelevant. What matters is that
the reference implementation of Thai statutory reporting lives in proprietary code
(`l10n_th_reports` OEEL-1 -> `account_reports` OEEL-1) that clean-room rules forbid reading.

Evidence: `l10n_th_withholding_tax` depends on `l10n_th_reports`; `l10n_th_reports_ext`
(SMEsPlus's own) extends the abstract `l10n_th.tax.report.handler` defined inside it.

ARCHITECTURAL CONSEQUENCE: the Thai PND/VAT report specification **cannot be derived from
source**. It must be built from (a) Thai Revenue Department published forms and rules,
(b) black-box observation of the reference system, (c) the `iTEST02` database dump.
STATE03 must not assume a source-derived reporting spec exists. This is the single largest
evidence dependency in the Thailand scope.

## S2 — WHT IS RECOGNISED AT PAYMENT, NOT AT INVOICE **[FREEZE-RELEVANT]**
Restates AF5. Meaning unchanged and now more important.
Evidence: `wt_tax_id` on both `account.move.line` and `account.payment`; the PND query
selects WHT rows filtered `payment_id IS NULL AND payment_state != 'not_paid'`.
ARCHITECTURAL CONSEQUENCE: the SMEsPlus accounting core must model WHT as a
**payment-time event** with a link back to the originating invoice line. This constrains
the transaction model, the posting engine and the period-close design. It is a baseline
data-architecture decision, not an implementation detail.

## S3 — THAI PARTY IDENTITY EXCEEDS A GENERIC PARTNER MODEL **[FREEZE-RELEVANT]**
Restates AF4. **Meaning changed.**
Was: "depends on an OCA module." Now: no dependency exists — SMEsPlus builds its own.
Evidence: `l10n_th_partner` adds `branch` ("Tax Branch") and `name_company`; the PND query
emits `branch_number` and a company-title join.
ARCHITECTURAL CONSEQUENCE: the multi-tenant party model must carry, as first-class
attributes: tax ID, **tax branch code**, legal company title (Thai), and Thai/English name
pairs. Retrofitting branch onto a generic contact model later is expensive. Freeze this now.

## S4 — STATUTORY REFERENCE DATA MUST BE DATA, NOT CODE **[FREEZE-RELEVANT]**
Restates AF2 + AF3. **Meaning changed — from "a bug in Odoo" to "a design rule for us."**
Evidence: the reference PND query derives income type from literal tax rates
(-1 Transportation, -2 Advertising, -3 Service, -5 Rental, else empty) and hardcodes
`wht_condition = '1'`, while the certificate model carries a far richer Thai RD income-type
list and a `TAX_PAYER` selection the report cannot express. The two disagree.

ARCHITECTURAL CONSEQUENCE: SMEsPlus must model WHT income types, rates, and WHT conditions
as **versioned reference data with effective dates**, owned by one authority and shared by
both certificate and filing outputs. The reference system's defect — two vocabularies for
one concept — is a direct instruction on what the SMEsPlus data architecture must avoid.
This is the clearest example in this pack of learning from a benchmark's weakness.

## S5 — MULTI-TENANT AND THAI COMPLIANCE INTERACT **[FREEZE-RELEVANT]**
Derived from the scope, not from a single module.
Every Thai model observed is company-scoped (`company_id` on `account.withholding.tax`,
on cert and cert line). Thai filings are per legal entity AND per tax branch.
ARCHITECTURAL CONSEQUENCE: the SaaS tenancy model needs at least three levels —
tenant -> legal entity (company) -> tax branch — because a Thai filing is produced at
branch level. A two-level tenant/company model will not satisfy Thai filing.

## S6 — THE eCOMMERCE COUPLING IS A PACKAGING ARTEFACT TO BE TESTED **[FREEZE-RELEVANT]**
Restates Q5. **Meaning changed.**
Was: "these modules cannot be moved." Now: SMEsPlus builds neither, so the question is
whether the coupling reflects a real requirement.
Evidence: `payment_2c2p` (Thai payment gateway) depends on `website_sale`.
ARCHITECTURAL CONSEQUENCE: STATE03 must decide whether Thai online payment (2C2P) is a
**backend payment-service capability** or an eCommerce capability. In the reference system
it is the latter, almost certainly for packaging reasons. For a Node.js SaaS the natural
answer is a payment-gateway service independent of any storefront. Recommend freezing
"payment gateway is a backend service" and NOT inheriting the reference coupling.

---

## SUMMARY — Q7 FEED TO STATE03
| ID | Finding | Freeze impact |
|---|---|---|
| S1 | Thai statutory reporting not source-observable | BLOCKING — needs alternative evidence route |
| S2 | WHT recognised at payment | Transaction/posting model |
| S3 | Thai identity: tax ID + branch + Thai title | Party/data model |
| S4 | Statutory reference data must be versioned data | Reference-data architecture |
| S5 | Tenant -> company -> tax branch | Tenancy model |
| S6 | Payment gateway independent of storefront | Service decomposition |
