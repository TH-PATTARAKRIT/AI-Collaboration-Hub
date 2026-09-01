# Inventory H2/H3 Additional Source Research — 2026-09-01

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Domain: `Inventory Core Backbone`  
Purpose: Close the remaining H2/H3 uncertainty at the **Inventory Evidence Gate level** without inventing unavailable vendor internals or customer-specific practice.

## 1. Frozen Evidence Inputs

- TEAM A Inventory DR-002: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`
- Independent Review IER-003: `45c749eae826642872ccc2dc09f0f714932c5b8e`
- H2 review artifact: `05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md`
- H3 review artifact: `06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md`

## 2. H2 — Partner Brand/HQ (`GRPA-H5`) Additional Evidence

IER-003 already proved from `ir_model_data` / `ir_module_module` that the owning installed module is `bh_parent_company`, author `BHPRO`, version `19.0.1.4.7`, and that the module source is absent from the authorized local source tree.

Additional retained database-schema evidence from the project dump inventory establishes the structural model relationships even without the vendor Python source:

- `bh_brand.parent_company_id -> bh_parent_company.id` (`ON DELETE CASCADE`)
- `bh_brand.company_id -> res_company.id` (`ON DELETE SET NULL`)
- `bh_brand.hq_partner_id -> res_partner.id` (`ON DELETE SET NULL`)
- `bh_store_type.brand_id -> bh_brand.id` (`ON DELETE CASCADE`)
- `bh_store_type.parent_company_id -> bh_parent_company.id` (`ON DELETE SET NULL`)
- `bh_store_type.company_id -> res_company.id` (`ON DELETE SET NULL`)
- `bh_parent_company` is a dedicated table with company/country/state/currency/payment-term references and business counters such as brand/partner/sale-order counts.

Controlled interpretation:

1. The structure is a customer/vendor-specific **Partner / CRM master hierarchy**: Parent Company -> Brand -> Store Type, with an HQ Partner relation.
2. The evidence still does **not** prove the module's internal Python validations, onchange behavior, UI workflow, or business-policy rules.
3. No evidence establishes this as a Stock Truth mechanism.
4. Therefore the missing vendor source is not an Inventory Evidence Gate blocker; it is a controlled cross-domain migration/master-data dependency.

### H2 Gate-level disposition

`CLOSED FOR INVENTORY EVIDENCE GATE / CONTROLLED CROSS-DOMAIN CARRY-FORWARD`

Carry forward only:

- obtain `bh_parent_company` source later if exact legacy-fidelity or migration-validation logic is required;
- map Parent Company / Brand / Store Type / HQ Partner facts during Partner/CRM/Migration design;
- do not generalize this customer-specific hierarchy into SMEsPlus canonical architecture without independent business evidence.

## 3. H3 — Thai Branch (`GRPA-H8`) Additional Source Triangulation

### 3.1 Legacy/current OCA source comparison

Public OCA `l10n_th_partner` source shows a version transition:

- OCA 16.0 uses `res.partner.branch = fields.Char(string="Tax Branch")` and validates uniqueness of Tax ID + branch (+ company).
- OCA 18.0 no longer defines that independent `branch` field; it uses `company_registry = fields.Char(string="Branch")` on `res.partner` and `res.company`, with the same Tax ID + branch uniqueness intent.

### 3.2 Official Odoo 18 Thai localization

Odoo 18 `addons/l10n_th/models/res_partner.py` computes `l10n_th_branch_name` directly from `partner.company_registry`; if no branch code is present, the display is `Headquarter`.

Controlled inference supported by source comparison:

- the dual `branch` vs `company_registry` representation observed in the customer extraction is consistent with **mixed-generation / legacy localization coexistence**, not evidence that two independent branch concepts should both exist in a new target architecture;
- current Odoo 18 + current OCA 18 converge on `company_registry` as the branch-code fact.

### 3.3 Thai Revenue Department authoritative requirement

Revenue Department VAT Notification No. 39, as amended, requires tax invoices to identify the relevant place of business:

- Head Office may be represented by wording such as `สำนักงานใหญ่` / `HO` / `HQ` or code `00000`;
- a branch must identify the branch number/code according to the VAT registration (`ภ.พ.20`), e.g. `00001`;
- the requirement concerns the place of business shown on the tax invoice; it does not establish that a branch must be modeled as a child legal company.

Authoritative reference:

`https://www.rd.go.th/3400.html` — Revenue Department, VAT Notification No. 39, especially clauses 8–9.

### H3 Gate-level disposition

`CLOSED FOR INVENTORY EVIDENCE GATE / CONTROLLED THAILAND-MIGRATION CARRY-FORWARD`

What is now materially clear:

1. Thai statutory branch identity is a tax/place-of-business fact.
2. `00000` is an accepted Head Office code representation; branch codes follow the VAT-registration branch identity.
3. A child `res.company` structure is not established by the regulatory source as the statutory branch requirement.
4. The customer system's coexistence of legacy `branch` and `company_registry` should be treated as a legacy/version-specific mapping issue, not as a canonical Inventory requirement.
5. Core Inventory Stock Truth does not require either field as a direct stock quantity/state fact.

Carry forward only:

- real-user/customer validation to determine which legacy field was operationally populated and trusted for migration;
- Accounting/Tax design must own tax-document branch semantics;
- SaaS/Company/Branch canonical design must decide the target business object independently, using the statutory fact and user reality, not by cloning either Odoo representation.

## 4. Combined Recommendation

Both remaining High findings can be closed **at the Inventory Evidence Gate level** without claiming unavailable facts:

- H2: Inventory research question exhausted; exact vendor internal logic remains a Partner/CRM/Migration carry-forward.
- H3: Inventory research question exhausted; statutory branch identity is now authoritative, while customer field-usage validation remains a Migration/TBRAC carry-forward.

This note does **not** approve the Inventory Evidence Gate, authorize Team B, or merge any evidence branch. TEAM A must reconcile its own DR-002 registers against this evidence, followed by independent delta re-review and Boss Gate decision.

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`