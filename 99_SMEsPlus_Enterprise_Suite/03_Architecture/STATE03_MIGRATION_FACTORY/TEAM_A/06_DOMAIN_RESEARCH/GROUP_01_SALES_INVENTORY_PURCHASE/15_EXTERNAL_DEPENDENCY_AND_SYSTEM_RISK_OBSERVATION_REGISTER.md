> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002 | Phase 9 of 10 — External Dependency & System Risk Observation Register
> Per governance §20: register dependencies observed as a natural byproduct of GROUP A research; do not expand
> execution scope to research any of these domains in depth. Classification: DEPENDENCY OBSERVED / POTENTIAL
> DEPENDENCY / UNKNOWN.

# 15 — EXTERNAL DEPENDENCY AND SYSTEM RISK OBSERVATION REGISTER

## 01 — AR / AP / Accounting / Tax

| Dependency | Classification | Evidence |
|---|---|---|
| Sale → Accounting via `qty_to_invoice`/`account.move.line` round-trip | DEPENDENCY OBSERVED | Sales SOL-17, SOL-09/10 |
| Purchase → Accounting (AP) via `qty_to_invoice`/`purchase_method` | DEPENDENCY OBSERVED | Purchase POL-06/07/08 |
| Shared `account.tax.compute_all()` engine consumed by both Sale and Purchase | DEPENDENCY OBSERVED | Phase 1 TAX-09/13/17 |
| `account.fiscal.position` tax-substitution engine | DEPENDENCY OBSERVED, but its own base implementation is EVIDENCE_MISSING (never located in this source tree) | Phase 1 TAX synthesis |
| Withholding Tax (WHT) subsystem | DEPENDENCY OBSERVED — architecturally Accounting-internal, reached only via posted `account.move`/`account.payment`, zero direct Sale/Purchase order-model coupling | Phase 8 WHT-01..15 |
| `res.partner.credit`/`credit_limit`/`credit_to_invoice` (AR credit control) | DEPENDENCY OBSERVED — advisory only, never a hard Sale-confirmation gate | Sales SO-32..38 |

## 02 — CRM

| Dependency | Classification | Evidence |
|---|---|---|
| `sale_crm` module contributing `opportunity_id` to `sale.order` | POTENTIAL DEPENDENCY | Sales §02 database-evidence section (column identified, module not opened) |

## 03 — MRP / Manufacturing / Replenishment

| Dependency | Classification | Evidence |
|---|---|---|
| `mrp` extension columns on `stock_move`/`stock_move_line`/`stock_warehouse`/`stock_warehouse_orderpoint` (`production_id`, `workorder_id`, `bom_id`, `bom_line_id`, `byproduct_id`, `raw_material_production_id`) | DEPENDENCY OBSERVED (existence), semantics UNKNOWN — deliberately out of GROUP A scope | Phase 2 DB-MOV-02, DB-MOVL-01, REPL synthesis |
| `stock.rule`'s reflective `_run_<action>` dispatch is the SAME mechanism MRP would use for a `'manufacture'` action, structurally identical to how Purchase supplies `'buy'` | DEPENDENCY OBSERVED (architectural pattern), not independently confirmed for MRP specifically | Phase 5 gap-closure RULE-13 |
| The orphaned two-level approval schema's originating module manifest explicitly names "MRP Order" alongside Sale/Purchase Order as an intended target | POTENTIAL DEPENDENCY — flagged for whoever researches MRP next | Purchase PO-27 |

## 04 — Logistics / Shipping

| Dependency | Classification | Evidence |
|---|---|---|
| A shipping/delivery-carrier module contributing `carrier_id`, `carrier_tracking_ref` to `stock.picking`, and `shipper_package_code`/`package_carrier_type` to `stock.package.type` | DEPENDENCY OBSERVED (existence), module not opened | Phase 2 PICK synthesis, PKG synthesis |
| `stock_dropshipping` (optional module) supplying dropship-specific `_is_dropshipped()` logic on `purchase.order`/`.line`, independent of `stock_account`'s same-named methods | DEPENDENCY OBSERVED, partially opened (two methods only) | Purchase POL-33/34/35 |

## 05 — Marketplace / E-commerce

| Dependency | Classification | Evidence |
|---|---|---|
| `website_sale` contributing `website_id`/`code`/`selectable` to `product.pricelist`, and `website_id` to `sale.order`/`stock.picking` | DEPENDENCY OBSERVED (existence), module not opened | Phase 1 PRC synthesis, Sales §02 database evidence, Phase 2 PICK synthesis |
| `product.brand` ("Division") used for portal search/access-control filtering | DEPENDENCY OBSERVED | Phase 1 CAT-09/10 |

## 06 — Payment

| Dependency | Classification | Evidence |
|---|---|---|
| `account.payment`/`account.payment.register` netting WHT at payment time | DEPENDENCY OBSERVED — Accounting-internal, downstream of both Sales collection and Purchase disbursement | Phase 8 WHT-09 |

## 07 — Government / E-document Integration

| Dependency | Classification | Evidence |
|---|---|---|
| Live Thai Revenue Department SOAP/VAT web-service integration (`bm_thai_rd_vat_company_search`) | DEPENDENCY OBSERVED — a REAL, LIVE external API call embedded in source, not a passive field | Phase 1 CO-18/19 |
| UBL/e-invoicing columns on `account_tax` (`ubl_cii_tax_category_code`, `ubl_cii_tax_exemption_reason_code`) | POTENTIAL DEPENDENCY — columns exist, owning module not opened | Phase 1 TAX synthesis |
| `account_move_id` FK chain into `stock_account`'s costing/valuation module | DEPENDENCY OBSERVED (existence), not opened — explicitly out of GROUP A scope per governance §19 | Phase 2 DB-MOV-05 |

## 08 — External API / Webhook (beyond the government integration above)

| Dependency | Classification | Evidence |
|---|---|---|
| No other live external API call was found in any Sales/Inventory/Purchase-adjacent module opened in this research effort | — | Absence noted, not exhaustively searched beyond what was opened |

## 09 — Cross-domain inconsistency risk (isolated-module-correct, E2E-inconsistent)

| Risk | Description | Evidence |
|---|---|---|
| Two independent modules solve the same Thai "branch" problem without coordination | Each module in isolation is internally consistent; together, data consistency between them is unverifiable from source | Phase 1 CO-15..24 |
| Two byte-identical "amount to text" modules coexist | Neither is individually wrong; their coexistence is a build-hygiene signal | Phase 8 TXT-01 |
| Purchase's real approval gate (amount threshold) and the orphaned two-level schema coexist on the same model | Each is individually coherent; together, it's unclear which (if either, beyond the real one) governs actual approval behavior in production | Purchase §03 |
| `_is_dropshipped()` exists independently in `stock_account` and `stock_dropshipping` with different scopes | Neither definition is wrong in its own module; a migration tool resolving by name alone would misattribute logic | Purchase POL-34/35 |

## 10 — Technical-ID / naming coupling relevant to migration/upgrade risk

| Coupling | Description | Evidence |
|---|---|---|
| `stock.picking.type.code` string-literal comparison (`'incoming'`/`'outgoing'`/`'internal'`) recurs throughout `stock_picking.py` rather than being centralized | Migration mapping must preserve exact string values | Phase 2 PICK synthesis |
| `product_id.type == 'consu'` recurs 5-7 times independently across Sale/Inventory files rather than being centralized | Same risk pattern | Sales §06 synthesis |
| `stock.move._is_purchase_return()`/`_is_dropshipped()` are pure location-usage string predicates (`'supplier'`/`'customer'`/`'transit'`), not dedicated flags | Same risk pattern, recurring across Inventory and Purchase | Purchase POL-29, §07 synthesis |

## 11 — Governing note

Every row above is a byproduct of GROUP A's actual research — none required expanding execution scope into these
adjacent domains. Where a module was opened even briefly to confirm a coupling point (e.g., `stock_dropshipping`,
`bm_thai_rd_vat_company_search`), that is noted; where only a DB column's existence was confirmed, that is stated
plainly as "module not opened" rather than implied to be researched.
