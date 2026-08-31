# STEP040304R2 — SCOPE RECONCILIATION (Q1–Q6)

Reconciliation and packaging only. No new Deep Research. No files moved in this step.

## PROJECT IDENTITY (§2 correction, applied throughout)
SMEsPlus is a **new 100% clean-room SaaS ERP**, multi-tenant, **Node.js** backend.
Odoo / Salesforce / SAP B1 are **reference and benchmark only**.
Odoo source and the DB dump are evidence instruments to prove business behaviour, data
structure, functional scope, dependency boundaries, Thai localization requirements, and
risks. **This is not preparation to build or extend Odoo modules.**

## Q1 — FINAL BACKEND ERP LEARNING SCOPE AFTER V2 HOLD
| Location | Modules | Role |
|---|---|---|
| 03_LEARNING (active folder) | 729 | backend-only corpus after V2 hold |
| addons_extra (Boss Extra) | 69 | SMEsPlus/partner customisations, all in active scope |
| Quarantine R1 (accounting non-TH) | 262 | out of scope |
| Quarantine R2A (non-TH localization) | 315 | out of scope |
| V2 hold (website/eCommerce/theme) | 127 | deferred to Version 2 |
| **TOTAL** | **1,502** | reconciles exactly to the STEP040301 index |

## Q2 — MODULES IN ACTIVE RESEARCH SCOPE
**134 modules.**
| Group | Modules |
|---|---|
| THAILAND_CORE | 2 |
| BOSS_EXTRA | 69 |
| CORE_DEPENDENCY | 63 |
Location split: 65 in 03_LEARNING + 69 in addons_extra = 134. Verified present 134/134.
The other 664 modules in 03_LEARNING are retained and available but are OUTSIDE active
research scope — they were never approved for study and have not been researched.

## Q3 — SOURCE-READABLE CLEAN-ROOM MODULES
**115 modules.** Learning method: read structure and behaviour to produce specifications.
No code copied, cloned, transcribed or reused — findings are behaviour statements with
file:line citations only.
Includes the 12 Boss Extra modules relabeled `BOSS_EXTRA_IN_SCOPE` under Boss ruling.

## Q4 — BLACK-BOX ONLY MODULES
**19 modules** — 11 OPL-1 (Boss Extra) + 8 OEEL-1 (Odoo Enterprise).
Method: manifest metadata + observed runtime behaviour ONLY. No .py/.xml/.js body read.
Thailand-relevant among them: `l10n_th_reports` (Thai statutory reports) and
`bm_thai_rd_vat_company_search` (Thai RD VAT lookup).
Observation plan: STEP040304_DEEP_RESEARCH/03_BLACK_BOX_OBSERVATION/

## Q5 — BACKEND DEPENDENCIES THAT CANNOT MOVE DESPITE WEBSITE NAMING
**6 modules**, all CORE_DEPENDENCY, all source-readable, all retained in 03_LEARNING:
`website`, `website_links`, `website_mail`, `website_payment`, `website_sale`,
`website_sale_loyalty`

Reason — three Boss Extra modules require them:
| Boss Extra module | requires |
|---|---|
| payment_2c2p (Thai 2C2P payment gateway) | website_sale -> website_payment -> website |
| smesplus_so_section_bydivision | website_sale, website_sale_loyalty -> website_links |
| product_brand_sale | website, website_sale |

Interpretation for a clean-room build: these are NOT a reason to build an eCommerce module.
They are evidence that in the REFERENCE system, Thai online payment (2C2P) and two SMEsPlus
customisations were implemented on top of the eCommerce stack. SMEsPlus must decide whether
that coupling is inherent to the business requirement or an artefact of Odoo's packaging.
See STATE03 finding S6.

## Q6 — HELD FOR VERSION 2
**127 modules** (81 website, 30 theme, 14 website-extension, 2 by category),
12,627 files, 272,194,946 bytes, in STEP040304R1_WEBSITE_V2_HOLD/01_HELD_MODULES.
Fully reversible: 02_EVIDENCE/RESTORE_WEBSITE_V2.sh. Nothing deleted.
