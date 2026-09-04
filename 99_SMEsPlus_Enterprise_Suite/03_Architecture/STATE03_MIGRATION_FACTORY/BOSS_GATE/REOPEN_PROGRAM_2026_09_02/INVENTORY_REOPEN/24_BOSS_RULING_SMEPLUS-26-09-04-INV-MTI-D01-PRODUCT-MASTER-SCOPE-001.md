# [SMEPLUS-26-09-04-INV-MTI-D01-PRODUCT-MASTER-SCOPE-001]
# Boss Ruling — MTI-D-01 Product Master Scope

Project: `SMEsPlus ENTERPRISE SUITE`  
STATE: `STATE03 — Architecture`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Ruling Branch: `ruling/inventory-mti-d01-product-master-scope-2026-09-04-001`  
Source Design Branch: `design/inventory-multitenant-invariant-set-2026-09-04-001`  
Source Design Tip: `dcb92278769d6a8239a5183ec4890e230a7caf68`  
Control Level: `/L9999.9999`  
Boss: `Sole Final Approver`  
Status: `BOSS RULING RECORDED — MTI-D-01 DECIDED — NOT DEVELOPMENT FINAL GATE`

---

## 1. Ruling

Boss rules `MTI-D-01` as:

`OPTION B — Company-owned Product Master / tenant-company scoped product identity`

The SMEsPlus Inventory product master must be scoped so each tenant/company sees and operates only its own product, configuration, inventory, valuation context, routes, rules, packaging, lots/serials, and reports.

No tenant/company may see, select, search, report, infer, or operate another tenant/company's product records.

Duplication across tenants/companies is acceptable and must not be treated as a defect.

---

## 2. Business Reason

Boss confirms that the purpose of SaaS tenant separation is operational and legal separation per customer/company.

Example given by Boss:

- Company A does transport business with 1% withholding tax condition.
- Company B says it is hired transport service with no 1% withholding tax condition.

Even where product/service names look similar, the business meaning, tax treatment, customer practice, reporting need, and operating control may differ. Therefore product identity must not be shared merely to reduce duplicate records.

---

## 3. Binding Interpretation

This ruling means:

1. Product identity is scoped by tenant/company context.
2. Product code/name/barcode/UoM similarity must never create shared identity across tenants/companies.
3. Cross-tenant product deduplication is not a requirement.
4. Cross-company product deduplication is not a default requirement.
5. Any cross-company or group-level comparison must use an explicit controlled mapping layer, not a shared product master.
6. Inventory, Sale, Purchase, Manufacturing, Accounting, Reporting, Approval, and Document modules must consume product identity through tenant/company context.
7. Migration may preserve duplicate products across tenants/companies when that reflects source business reality.
8. Reporting may aggregate only after an explicit authorized mapping exists.

---

## 4. Impact On Prior Package

This ruling supersedes the earlier AAS+ recommendation that preferred tenant-level product master with company-level attachment.

Affected decision:

- `MTI-D-01` moves from `OPEN / BOSS RULING REQUIRED` to `BOSS RULED — OPTION B`.

Unaffected items:

- `MTI-D-02` authorization granularity remains open.
- `MTI-D-03` tenant-changeable boundary remains open.
- `RISK-U03 / GAP-FS-10` remains open because the capability is not built or verified.
- `0 of 8` L9 proofs remains unchanged.
- `0 of 22` cross-proof scenarios remains unchanged.
- Accounting COGS dependency remains `HOLD`.
- No development is authorized.

---

## 5. Required Carry-forward For Next Prompt

Any next Inventory prompt must carry this ruling exactly:

`MTI-D-01 = OPTION B — Company-owned Product Master / tenant-company scoped product identity.`

Any design output must avoid language that treats product duplication across tenants/companies as a defect.

Any future group-level product analysis must introduce a separate controlled mapping/provenance object and must not collapse product identity by code, name, barcode, UoM, or category similarity alone.

---

## 6. Non-Authorization Lock

This ruling does not authorize:

- Team B development.
- Team C development.
- Source code implementation.
- Database implementation.
- Schema freeze.
- Merge to canonical branch.
- Production.
- Release.
- Final Solution PASS.
- Development Final Gate.

Boss remains the sole Final Approver.

---

`No Evidence = No Progress.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`
