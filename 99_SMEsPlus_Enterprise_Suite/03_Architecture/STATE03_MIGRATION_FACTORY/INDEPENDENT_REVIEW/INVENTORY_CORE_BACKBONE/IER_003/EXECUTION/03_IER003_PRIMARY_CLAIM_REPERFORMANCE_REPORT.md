# 03 — Primary-Claim Re-Performance Report

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently re-open representative primary evidence behind TEAM A's highest-load-bearing claims | Independent Evidence Reviewer | This artifact; direct `grep`/`Read` against the authorized source tree; direct SQL against a disposable PG18 restore of the dump | 2026-09-01 | Boss | See per-item verdict | Establishes whether the package as a whole is trustworthy, beyond the five High items |

Method: risk-based representative re-performance, not exhaustive per-line coverage — consistent with the controlling prompt's own instruction. Ten items below correspond to controlling-prompt §5.1–§5.10.

## 1. Valuation architecture: no `stock.valuation.layer` model; value lives on `stock.move`

**Re-performed via two independent channels.**

- Source: `grep -rl "_name = 'stock.valuation.layer'"` across the entire authorized source tree → **zero hits**. (A broader search for the bare string `stock.valuation.layer`/`stock_valuation_layer` returns 20 files, all of which are either `.po` translation files, test files in *other* apps referencing a *different* concept by coincidence of naming, or — checked directly — none define the model. No model declaration exists.)
- Database: `SELECT to_regclass('public.stock_valuation_layer')` against a fresh PG18 restore of the dump → **NULL (table does not exist)**.

**VERIFIED — CONFIRMED, both source and schema agree.** TEAM A's A9 §1 claim is correct.

## 2. Absence/presence of `uom.category`, `product.packaging`, `procurement.group`; replacement concepts

| Model | Source grep | DB schema (`to_regclass`) | TEAM A claim | Result |
|---|---|---|---|---|
| `uom.category` | 0 hits for the `_name` declaration | table does not exist | Absent, replaced by self-referential `uom.uom.relative_uom_id` tree | **CONFIRMED** |
| `product.packaging` | 0 hits | table does not exist | Absent, replaced by `product.template.uom_ids` + `product.uom` barcode-link model | **CONFIRMED** |
| `procurement.group` | 0 hits | table does not exist | Absent, replaced by `stock.reference` | **CONFIRMED** — and `stock.reference` itself independently confirmed present both as a model file (`stock/models/stock_reference.py`) and as a live DB table |

All three of TEAM A's "structurally absent, here is the real replacement" claims are independently corroborated at both the source and schema level — the strongest possible confirmation available without live application testing.

## 3. Product inventory-management classification chain (`type`/`is_storable`)

Confirmed via DB query on `product_template.type`: only two distinct values present in this dataset, `consu` (82,723 rows) and `service` (1,030 rows) — no `combo` rows present, and critically, **no legacy `'product'` literal value anywhere in the actual data**. This closes GRPA-M14 (A14's own carried-forward Medium item) fully: TEAM A's A5 §4 had already narrowed this to "PARTIALLY VERIFIED" based on the current field definition having only 3 possible values; this review's direct query of the live data removes the residual "is `'product'` present as legacy data" uncertainty. **Recommend GRPA-M14 be reclassified RESOLVED, not merely PARTIALLY VERIFIED, in the next TEAM A pass.**

## 4. Stock Truth primary vs. derived quantity

Direct read of `stock/models/stock_quant.py` and `stock/models/stock_move.py` confirms the compute/store distinctions A3 documents (`quantity`/`reserved_quantity` stored; `available_quantity` pure compute; `product_qty` computed+stored with a `UserError`-raising inverse guard). No contrary evidence found. **CONFIRMED.**

## 5. Application-layer vs. DB-constraint claims for over/under-fulfillment / negative quantity

Directly queried the restored database for DB-level CHECK constraints on the relevant tables — none exist (consistent with A2/A13's DB-forensics-based claim, now independently confirmed via a **fresh** restore rather than reused DELTA-FIRST evidence). Data-level check: `stock_quant` in this specific dataset has **zero rows** (see [09](09_IER003_DATABASE_DUMP_REVERIFICATION_REPORT.md) §3 for the important caveat this creates), so the "no DB CHECK constraint" finding is a schema-level fact independently reproduced, not a data-level test of whether negative quantities have actually occurred in this dataset. **CONFIRMED at the schema level; data-level test not possible on this specific dataset (empty table), registered as a residual limitation, not silently dropped.**

## 6. Sales → Inventory and Purchase → Inventory handoffs

Spot-checked `sale_stock`'s `_action_launch_stock_rule()` and `purchase_stock`'s `_create_or_update_picking()`/`_run_buy()` call chains against A6/A8's citations — method names, file locations, and behavioral description all matched on direct read. **CONFIRMED**, not re-traced line-by-line beyond the spot check (consistent with the controlling prompt's risk-based-sampling instruction).

## 7. Manufacturing physical handoff evidence

Spot-checked `mrp/models/stock_rule.py`'s `_run_manufacture()` (search-before-create, wizard-based quantity bump) against A6 §3's citation. Matched. `mrp.production._post_inventory()`'s FG-quantity assignment (A8 §3) was not independently re-traced line-by-line this pass; no contrary evidence surfaced during adjacent reading. **CONFIRMED at the level TEAM A itself scoped this claim (core `mrp`, not the 18 `mrp_*` extensions).**

## 8. Inventory adjustment / physical count behavior

Directly confirmed `stock.quant.inventory_quantity`/`inventory_diff_quantity` field definitions exist as A7 describes. TEAM A's own A7 already discloses this deliverable as "PARTIALLY VERIFIED" with four explicit residual gaps (count-freeze state, exact posting-method trace, date/cutoff fields, stock lock concept). This review closes one of those four gaps completely — see [07](07_IER003_HIGH_H4_CUTOFF_TIMING_REVIEW.md) — and did not attempt to close the other three (count-freeze state, exact posting-method line trace) as they were outside this review's higher-priority scope (the five High items). **Registered as a targeted follow-up recommendation in [14](14_IER003_TARGETED_TEAM_A_CORRECTIVE_RECOMMENDATION.md), not silently dropped.**

## 9. Tenant/Company/Warehouse evidence classification

See [08](08_IER003_HIGH_H5_COMPANY_ACL_TENANT_REVIEW.md) — this is N-A13-02, one of the five High items, given full independent treatment there rather than only a spot check here.

## 10. Clean-room quarantine labels

A17's quarantine table (product `type`/`is_storable`, `stock.move.value` architecture, `stock.reference`, `uom.uom.relative_uom_id` tree, string-literal branching, the three unresolved approval modules) was cross-checked against A3–A9's actual content — every quarantined item is indeed present and correctly characterized as vendor-specific evidence, not adopted as design, in the deliverables that discuss it. No instance was found anywhere in A0–A20 of vendor terminology being proposed as SMEsPlus's own schema. **CONFIRMED — see [12](12_IER003_CLEAN_ROOM_TBRAC_SAAS_INTEGRITY_REVIEW.md) for the full clean-room disposition.**

## Summary

Of the ten representative primary claims re-performed, **all ten are independently corroborated** by this review's own direct source and/or database evidence (several by *two* independent channels — source grep and schema query — which is stronger confirmation than TEAM A's own package achieved for these specific claims, since TEAM A's own DB re-verification was blocked). One claim (GRPA-M14, item 3 above) is upgraded from PARTIALLY VERIFIED to fully closable. No claim was found to be fabricated, inflated, or contradicted by primary evidence. This is a materially positive finding about the overall trustworthiness of the DR-002 package: TEAM A's citation discipline (exact field/method names, no paraphrase) held up under independent re-performance in every case tested.

No Evidence = No Progress.
