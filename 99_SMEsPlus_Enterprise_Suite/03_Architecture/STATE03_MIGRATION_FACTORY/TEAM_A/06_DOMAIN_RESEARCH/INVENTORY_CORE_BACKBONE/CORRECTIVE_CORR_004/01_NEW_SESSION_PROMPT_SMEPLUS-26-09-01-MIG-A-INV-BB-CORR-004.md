# [SMEPLUS-26-09-01-MIG-A-INV-BB-CORR-004]
# Inventory Core H2/H3 Targeted Source, Regulatory & Evidence Reconciliation / TEAM A / L999.999

## SINGLE END-TO-END SELF-STARTING TEAM A CORRECTIVE PROMPT

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Execution Team: `TEAM A — Source Learning / Business Evidence Extraction`  
Workstream: `Inventory Core Backbone — H2/H3 Targeted Corrective Closure`  
Mode: `READ ONLY / EVIDENCE-FIRST / DELTA-FIRST / CLEAN-ROOM`  
Control Level: `/L999.999`  
Boss: `Sole Final Approver`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Governance Branch: `SMEsPlus`  
Canonical Governance Baseline at Prompt Creation: `daa459a22f376f6f3371bfcd226ed76039918cb0`  
Frozen TEAM A DR-002 Commit: `b31597fafa318c2edd9047ad89c128e4ace2e7cb`  
Frozen Independent Review IER-003 Commit: `45c749eae826642872ccc2dc09f0f714932c5b8e`  
Additional Source Research Note Commit: `e4387af5dc64e882e78614cb72c6ba9f1d87d133`  
Five-Unit Readiness Commit: `daa459a22f376f6f3371bfcd226ed76039918cb0`  
Execution Branch: `claude/inventory-core-backbone-h2-h3-corr004`  
Jira: `ERPPLUS-137` — preserve fields; comment only if connector is available.

This is the only execution instruction for this session.

`ONE SESSION = ONE END-TO-END PROMPT.`

Execution flags:

`AUTO-CONTINUE`  
`AUTO-COMMIT/PUSH EVIDENCE`  
`NO ROUTINE CONFIRMATION`  
`ASK BOSS ONLY ON TRUE STOP CONDITIONS`

Do not ask Boss for separate START / CONTINUE / NEXT / COMMIT / PUSH instructions.

---

## 1. Mission

Perform a narrow TEAM A corrective reconciliation for the two remaining Inventory High items from IER-003:

- `H2 / GRPA-H5 — Partner Brand/HQ / bh_parent_company`
- `H3 / GRPA-H8 — Thai Branch representation conflict`

Goal:

`Close both items at the Inventory Evidence Gate level if, and only if, the evidence supports that disposition, while preserving any valid cross-domain, migration, customer-specific, regulatory or real-user-validation carry-forward.`

Do not repeat full Inventory DR-002.

Do not create target architecture.

Do not self-approve the Inventory Evidence Gate.

---

## 2. Mandatory Inputs — Read Before Acting

### 2.1 TEAM A DR-002 frozen evidence

Commit:

`b31597fafa318c2edd9047ad89c128e4ace2e7cb`

Path:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/EXECUTION/`

At minimum read:

- `A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md`
- `A10_SAAS_TENANT_COMPANY_WAREHOUSE_RISK_REGISTER.md`
- `A11_THAILAND_BUSINESS_REALITY_AND_REGULATORY_REGISTER.md`
- `A12_MIGRATION_PROVENANCE_AND_CONTINUITY_EVIDENCE.md`
- `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
- `A15_MATERIAL_UNKNOWN_EXHAUSTION_REPORT.md`
- `A16_ACCOUNTING_X_INVENTORY_CROSS_PROOF_INPUT_PACK.md`
- `A18_TEAM_A_INVENTORY_DEEP_RESEARCH_FINAL_REPORT.md`
- `A19_INVENTORY_DEEP_RESEARCH_SHA256_MANIFEST.txt`
- `A20_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md`

### 2.2 IER-003 frozen independent review

Commit:

`45c749eae826642872ccc2dc09f0f714932c5b8e`

Path:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/IER_003/EXECUTION/`

Mandatory:

- `05_IER003_HIGH_H2_PARTNER_BRAND_HQ_FORENSIC_REVIEW.md`
- `06_IER003_HIGH_H3_THAI_BRANCH_TBRAC_REVIEW.md`
- `09_IER003_DATABASE_DUMP_REVERIFICATION_REPORT.md`
- `13_IER003_FINDING_AND_GATE_IMPACT_REGISTER.md`
- `14_IER003_TARGETED_TEAM_A_CORRECTIVE_RECOMMENDATION.md`
- `16_IER003_BOSS_GATE_RECOMMENDATION.md`

### 2.3 Additional source/regulatory research note

Read canonical file:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/INVENTORY_CORE_BACKBONE/INVENTORY_H2_H3_ADDITIONAL_SOURCE_RESEARCH_2026_09_01.md`

Treat this as an evidence-routing note, not as an answer key. Re-perform or corroborate what can be re-performed.

### 2.4 Five-Unit readiness

Read:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/INVENTORY_CORE_BACKBONE/INVENTORY_H2_H3_CORR004_PRE_PROMPT_FIVE_UNIT_CHALLENGE.md`

---

## 3. H2 — Required Reconciliation

### 3.1 Re-open all available local evidence

Search the authorized source tree again for:

- `bh_parent_company`
- `bh_brand`
- `bh_store_type`
- `brand_id`
- `parent_company_id`
- `hq_brand_id`
- `is_hq_brand`
- `store_type_id`
- `bh_parent_company_code`
- `hq_partner_id`

If the vendor Python source now exists anywhere under the authorized project/source roots, read it fully and record exact paths/lines.

If it does not exist, do not keep retrying indefinitely. Record the absence with reproducible search evidence.

### 3.2 Re-perform database/schema structure

Using the existing dump or existing extracted schema evidence, confirm where possible:

- `bh_brand.parent_company_id -> bh_parent_company`
- `bh_brand.company_id -> res_company`
- `bh_brand.hq_partner_id -> res_partner`
- `bh_store_type.brand_id -> bh_brand`
- `bh_store_type.parent_company_id -> bh_parent_company`
- `bh_store_type.company_id -> res_company`
- key `bh_parent_company` fields/counters relevant to interpreting the hierarchy.

Do not infer Python behavior from foreign keys.

### 3.3 H2 required conclusion

Separate exactly:

1. **FACT — module ownership/provenance**
2. **FACT — database structural relationships**
3. **UNKNOWN — unavailable vendor internal Python logic**
4. **Inventory Gate impact**
5. **Partner/CRM/Migration carry-forward**
6. **SaaS/tenant relevance**

H2 may be marked:

`CLOSED FOR INVENTORY EVIDENCE GATE / CONTROLLED CROSS-DOMAIN CARRY-FORWARD`

only if the evidence still supports that:

- it is not a Stock Truth fact;
- ownership and structural relationships are materially understood;
- remaining unknowns are vendor-internal / migration / Partner-domain questions rather than Inventory research gaps.

Do not declare the vendor logic itself resolved if source remains absent.

---

## 4. H3 — Required Source and Regulatory Reconciliation

### 4.1 Re-open the customer/local source

Read fully the local files corresponding to:

- official/local `l10n_th` partner branch logic;
- local `addons_extra/l10n_th_partner` partner/company branch logic;
- any branch-related company hierarchy extensions actually present.

Record exact source version/provenance where available.

### 4.2 Version-aware source comparison

Corroborate the evidence that:

- older OCA `l10n_th_partner` versions used an independent `res.partner.branch` field;
- current OCA 18 uses `company_registry` for Branch on partner/company;
- Odoo 18 `l10n_th` computes Thai branch display from `company_registry`.

If network access is unavailable, use the canonical additional-research note as routed evidence and explicitly label the limitation.

Do not claim that current OCA/Odoo behavior is the SMEsPlus target architecture.

### 4.3 Thai regulatory evidence

Use authoritative Thai Revenue Department evidence for the legal/business fact underneath H3.

Minimum authoritative reference:

`Revenue Department — VAT Notification No. 39, clauses 8–9`

`https://www.rd.go.th/3400.html`

Verify and record at minimum:

- Head Office identification including `00000` as an allowed code representation;
- branch identification according to VAT registration / place of business;
- whether the regulatory source requires branch identity on the tax invoice;
- whether it requires branch to be modeled as a child legal company.

Do not make legal-compliance approval claims. Use `REGULATORY EVIDENCE VERIFIED` only for the exact proposition supported by the cited source.

### 4.4 Customer-practice boundary

Keep separate:

- Thai statutory/business fact;
- legacy Odoo/OCA implementation choices;
- this customer's actual operational field usage;
- future SMEsPlus target design.

Do not claim customer operational usage unless supported by DB usage, transaction linkage, configuration, or real-user evidence.

### 4.5 H3 required conclusion

H3 may be marked:

`CLOSED FOR INVENTORY EVIDENCE GATE / CONTROLLED THAILAND-MIGRATION CARRY-FORWARD`

only if evidence supports all of the following:

1. statutory branch identity is materially established;
2. dual legacy fields are a version/implementation coexistence issue, not two mandatory Stock Truth concepts;
3. no core Inventory fact directly depends on selecting one legacy field as canonical;
4. real-user validation is preserved only for migration/customer-use interpretation, not silently converted into fact;
5. Accounting/Tax retains ownership of tax-document branch semantics;
6. future SaaS/Branch canonical design remains independent and clean-room.

---

## 5. Mandatory TEAM A Corrective Updates

Update only the necessary TEAM A DR-002 files on the corrective branch. Preserve historical wording through explicit correction/supersession notes where appropriate.

At minimum reconcile:

- `A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md`
- `A10_SAAS_TENANT_COMPANY_WAREHOUSE_RISK_REGISTER.md`
- `A11_THAILAND_BUSINESS_REALITY_AND_REGULATORY_REGISTER.md`
- `A12_MIGRATION_PROVENANCE_AND_CONTINUITY_EVIDENCE.md`
- `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`
- `A15_MATERIAL_UNKNOWN_EXHAUSTION_REPORT.md`
- `A16_ACCOUNTING_X_INVENTORY_CROSS_PROOF_INPUT_PACK.md`
- `A18_TEAM_A_INVENTORY_DEEP_RESEARCH_FINAL_REPORT.md`
- `A20_SESSION_CLOSURE_SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002.md`

Do not rewrite unrelated findings.

Recompute mechanical residual counts after H2/H3 reclassification. Do not preserve stale `5 High` wording if the evidence no longer supports it.

---

## 6. Corrective Deliverables

Create under:

`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/CORRECTIVE_CORR_004/EXECUTION/`

Required:

1. `01_CORR004_PREFLIGHT_AND_EVIDENCE_INPUT_VERIFICATION.md`
2. `02_CORR004_H2_SOURCE_AND_SCHEMA_RECONCILIATION.md`
3. `03_CORR004_H3_SOURCE_VERSION_AND_THAI_REGULATORY_RECONCILIATION.md`
4. `04_CORR004_H2_H3_GATE_LEVEL_DISPOSITION_REGISTER.md`
5. `05_CORR004_TEAM_A_DR002_DELTA_CHANGE_REGISTER.md`
6. `06_CORR004_REVISED_UNKNOWN_COUNT_RECONCILIATION.md`
7. `07_CORR004_ACCOUNTING_MIGRATION_TBRAC_CARRY_FORWARD_REGISTER.md`
8. `08_CORR004_READY_FOR_INDEPENDENT_DELTA_REVIEW_REPORT.md`
9. `09_CORR004_SHA256_MANIFEST.txt`
10. `10_SESSION_SMEPLUS-26-09-01-MIG-A-INV-BB-CORR-004_CLOSURE.md`

Manifest must hash all mutable corrective artifacts and all modified DR-002 files, excluding itself from self-hash where necessary with accurate wording.

---

## 7. Clean-Room Controls

- Reference ERP/source behavior is learning/evidence only.
- No copy/clone/reuse of vendor implementation architecture.
- Do not turn `bh_parent_company`, Odoo `branch`, or `company_registry` into target design by default.
- Do not design SMEsPlus Inventory schema/workflow/API/UI.
- No Team B work.
- No Team C work.
- No merge to `SMEsPlus`.
- No production/live-system writes.

---

## 8. Stop Conditions

Ask Boss only if one of these occurs:

- destructive or live-system write becomes necessary;
- authorized source/dump cannot be accessed and the missing evidence is truly load-bearing;
- a material contradiction appears that cannot safely remain `CONFLICTING EVIDENCE`;
- scope expansion beyond H2/H3 is required;
- legal/license/clean-room boundary would be crossed;
- branch/credential/access conflict prevents safe evidence publication.

Non-blocking unknowns must be registered and carried forward, not escalated as routine questions.

---

## 9. Commit / Push Authority

Authorized:

- modify only the required TEAM A DR-002 evidence files on `claude/inventory-core-backbone-h2-h3-corr004`;
- create the 10 CORR-004 evidence deliverables;
- commit and push evidence to that dedicated branch;
- continue through completion without routine confirmation.

Forbidden:

- merge to `SMEsPlus`;
- modify IER-003 artifacts;
- modify Accounting evidence;
- authorize Team B or Development.

---

## 10. Required Terminal Status

If evidence supports gate-level closure of both H2 and H3 and all required reconciliations are complete:

`TEAM A INVENTORY H2/H3 TARGETED CLOSURE COMPLETE — READY FOR INDEPENDENT DELTA RE-REVIEW — INVENTORY EVIDENCE GATE NOT SELF-APPROVED`

If either item remains an Inventory research blocker:

`TEAM A INVENTORY H2/H3 CORRECTIVE REVIEW COMPLETE — HOLD / EVIDENCE REQUIRED — INVENTORY GATE NOT READY`

If evidence is genuinely unavailable:

`EVIDENCE MISSING — INVENTORY GATE NOT READY`

Never output `INVENTORY GATE PASS` or `TEAM B AUTHORIZED`.
