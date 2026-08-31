# 05 — High H2 (GRPA-H5): Orphaned Partner Brand/HQ Columns — Independent Verdict

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently test GRPA-H5's classification, evidence, and Gate impact via source-wide search and DB metadata forensics | Independent Evidence Reviewer | `ir_model_data` provenance query against a disposable PG18 restore | 2026-09-01 | Boss | **PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED (owning module now identified)** | Reclassified from "unknown ownership" to "known module, source absent" — same character as the already-registered SAAS-05 finding |

## TEAM A's claim (A14 Part 1, GRPA-H5)

Orphaned `res.partner` columns `brand_id`, `parent_company_id`, `hq_brand_id`, `is_hq_brand`, `store_type_id`, `bh_parent_company_code`, plus 13 `x_studio_*` fields — "Evidence Sought: Owning module for each column. Evidence Found: Not found; best candidate for future dump-forensics resolution... Status: `EVIDENCE_MISSING`."

## What this review found

### Step 1 — source-wide search (no DB access needed)

Grepped every named column across the **entire** authorized source tree (`01 ACCOUNT/` + `02 OTHER/` + `addons_extra/`, 93,866+ files): zero hits for `hq_brand_id`, `is_hq_brand`, `bh_parent_company_code` in any Python model file. `brand_id`/`parent_company_id`/`store_type_id` returned hits, but every one is a false positive in an unrelated module (payment providers, `l10n_it_reports`, `account_peppol`, MRP subcontracting tests) — none is the `res.partner` brand/HQ concept TEAM A is asking about. This independently corroborates the "no owning module in source" half of TEAM A's finding.

### Step 2 — DB metadata forensics (the step TEAM A's own package could not perform, and GROUP A's frozen forensics did not ask)

Restored the dump into a disposable PG18 container (see [09](09_IER003_DATABASE_DUMP_REVERIFICATION_REPORT.md) for the full restore account) and queried **`ir_model_data`** — Odoo's own field-provenance table, which records which installed module registered each field, independent of whether that module's Python source is present on this machine:

```sql
SELECT d.module, f.name
FROM ir_model_fields f
JOIN ir_model_data d ON d.model='ir.model.fields' AND d.res_id=f.id
JOIN ir_model m ON f.model_id = m.id
WHERE m.model='res.partner'
  AND f.name IN ('brand_id','parent_company_id','hq_brand_id','is_hq_brand','store_type_id','bh_parent_company_code','hq_brand_count');
```

**Result: all seven fields are registered by one module — `bh_parent_company`.** `ir_module_module` confirms this module is `state='installed'`, `author='BHPRO'`, `latest_version='19.0.1.4.7'`, `summary="Manage parent companies, brands, and link contacts/sales orders to them."`

A follow-up search confirmed `bh_parent_company`'s Python source is **not present anywhere** on the authorized local machine (`find ... -iname "*bh_parent_company*"` → zero hits).

## Why this changes the finding without fully closing it

TEAM A's evidence-sought question was literally "owning module for each column." That question **is now answered**: the owning module's name, author, and stated purpose are known with certainty, directly from the customer's own installed-module registry — this is not an inference from field-naming patterns, it is Odoo's own authoritative provenance record. What remains genuinely unknown is the module's **internal logic** (validation rules, how `is_hq_brand`/`hq_brand_id` relate structurally, what `store_type_id` points to) — because its source code is absent from this machine, exactly the same structural situation as the three approval modules already registered as SAAS-05 (source absent, business-fact usage observable, internal logic unavailable to read).

This is a **materially different** disposition from "unknown ownership, DB forensics needed" — it is now "ownership known, vendor/customer source acquisition needed," which changes the next action from a research task to a sourcing/access task.

## Independent verdict

**`PARTIALLY VERIFIED — TARGETED CORRECTION REQUIRED`**

- Evidence read: source-wide grep (this review) + `ir_model_data`/`ir_module_module` provenance query (this review) + GROUP A's original column enumeration (reused, corroborated).
- What remains unknown: `bh_parent_company`'s internal model/field relationships and business-validation logic — genuinely unavailable without obtaining the module's source from the customer/vendor or from a live install where its code can be introspected.
- **Inventory Gate blocking: NO** — this is party/CRM master-data structure, not a Stock Truth fact. Confirmed directly (no `stock.*`/`product.*` model references `bh_parent_company`'s fields anywhere in source).
- Accounting interface impact: None found.
- Dependent-module impact: Party/CRM master data only — reaffirms TEAM A's own classification.
- SaaS/tenant impact: Medium, as TEAM A assessed — an undocumented multi-brand/multi-HQ pattern implemented via a customer-specific module is exactly the kind of structure a migration/multi-tenant design must not assume is universal.
- Migration impact: Medium, unchanged — but now actionable: a migration extraction can query `ir_model_data` the same way this review did, for **any** customer-specific module, to recover field provenance even when source is unavailable.
- **Next owner / next action**: `CROSS-DOMAIN CARRY-FORWARD — NOT AN INVENTORY GATE BLOCKER`. Obtaining `bh_parent_company`'s source (from the customer or BHPRO, the stated author) is an external sourcing action, not a Team A Inventory research task — registered as an external dependency in [16](16_IER003_BOSS_GATE_RECOMMENDATION.md).

No Unknown was converted to a Fact beyond what the evidence supports — the module's *name and purpose* are now facts; its *internal logic* remains an honestly disclosed unknown.
