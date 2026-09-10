# 00B_FUNCTIONAL_OWNERSHIP_MATRIX.md
# Workstream B — Functional Ownership Matrix (Inventory)

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Owner: **LESA**
**LAYER 2 — AUDIT QUARANTINE.** Boss / PMO / AI-Audit only.
Generation basis: **R1 (series-19, content-verified)**; deployment basis: **two series-19 deployments**.

---

## 1. The question this matrix answers

> *Do not assume a function belongs to Inventory merely because it creates a stock movement, because
> Inventory displays it, because Inventory receives its output, or because a related menu is visible.*

The prior Pilot derived a **mechanical** module boundary of 149 modules and correctly refused to trim
it by hand, routing the scope question to Boss as `BOSS-DEC-02`. **This matrix supplies the evidence
that decision was missing.**

---

## 2. Derivation — primary owner is derived, not asserted

| Clause | Declaration |
|--------|-------------|
| **POPULATION** | the 96 objects of the Pilot's adopted family (86 owned + 10 boundary) |
| **PATTERN** | for each object, the set of modules that **declare** it (`_name`); the **primary** declarer is the one every other declarer **transitively depends on**, computed from the parsed dependency graph of all 1,433 modules |
| **PATH SET** | R1, 1,433 manifests parsed |
| **UNIT** | one object = one row |
| **ELIGIBILITY** | all 96; **0 unresolved** — every object has exactly one dependency-root declarer |

**Why the dependency graph and not the module name.** A first attempt ranked declaring modules
alphabetically and produced wrong owners — it attributed the product object to a documents module and
the unit-of-measure object to a point-of-sale module, purely because those names sort first. The
dependency graph is the only mechanical statement of *which module defines a thing and which extends
it*. Recorded as instrument correction `CORR-F-31`.

**Two supporting axes, both measured:**
- **`carries stock quantity`** — the object declares a field from the quantity vocabulary.
- **`carries financial field`** — the object declares a relation to an accounting object, or a value /
  price / total field.

**And one prior ruling is honoured rather than re-derived.** The prior R4 deep research established,
and Boss approved, principle `P-07`: **Inventory emits facts; Accounting decides postings.** No
Inventory object below writes a journal entry or selects an account. Where a row shows a financial
field, that is **the fact Inventory emits**, never a posting Inventory performs.

---

## 3. Ownership distribution

| Ownership class | Objects | Share |
|-----------------|--------:|------:|
| **PRIMARY OWNER** — Inventory defines the object and its lifecycle | **60** | 62.5% |
| **DEPENDENT MODULE** — another cluster defines it; Inventory neither displays nor moves quantity through it | 13 | 13.5% |
| **CONSUMING MODULE** — Inventory displays it but does not define it and moves no quantity through it | 10 | 10.4% |
| **TRIGGERING MODULE** — another cluster defines it, it carries stock quantity, Inventory does not display it | 7 | 7.3% |
| **OPTIONAL MODULE** — country localisation objects, present only where that localisation is installed | 5 | 5.2% |
| **CROSS-MODULE CO-OWNER** — displayed by Inventory **and** carries stock quantity **and** carries financial fields | **1** | 1.0% |
| | **96** | |

**No object is `UNRESOLVED OWNERSHIP`.** The dependency-root rule resolved all 96.

## 4. Cluster answers — the ten questions of §5

| Cluster | Objects | Does Inventory OWN it? | Relationship | Should it be in the Inventory VDR population? |
|---------|--------:|------------------------|--------------|-----------------------------------------------|
| **INVENTORY** | 60 | **Yes** | primary owner | **Yes — this is the subject** |
| **MANUFACTURING** | 13 | **No** | 7 of the 13 carry stock quantity; **1 (the production order) is displayed inside the Inventory application and carries both quantity and financial fields** | **Cross-module handoff target, except the production order, which is a genuine co-ownership** |
| **PRODUCT** | 5 | No | consuming — product, template, category, attribute, unit of measure | **No — this is `VDR-MD-03` / `VDR-MD-04`, an upstream master-data subject** |
| **LOCALISATION** | 5 | No | optional-module dependent; **none installed on either observed deployment** | **No — configuration-dependent, out of the baseline population** |
| **SALES CHANNEL** | 4 | No | triggering — marketplace accounts and shops that drive stock synchronisation | **Handoff target** |
| **DELIVERY** | 2 | No | consuming — carrier and postcode prefix, displayed in the Inventory application | **Handoff target** |
| **REPAIR** | 2 | No | triggering — the repair order carries stock quantity | **Handoff target** |
| **QUALITY** | 1 | No | dependent | **Handoff target** |
| **FIELD SERVICE** | 1 | No | triggering — carries stock quantity | **Handoff target** |
| **BARCODE** | 1 | No | consuming — nomenclature displayed in the Inventory application | **Handoff target** |
| **POS** | **1** | No | dependent — the session object only | **No** |
| **PLATFORM** | 1 | No | the configuration-settings object, extended by everyone | **No — boundary object** |

### The decisive result for `BOSS-DEC-02`

The mechanical module boundary drew in the manufacturing, quality, point-of-sale, repair,
field-service and delivery clusters. **By ownership, those six clusters together own 20 objects, and
the point-of-sale cluster owns exactly one.**

> **The point-of-sale cluster entered the 149-module boundary because its modules *extend* Inventory
> objects, not because it *owns* any.** Module extension is not ownership. This is the single clearest
> demonstration that a module-extension boundary over-states a domain.

**`BOSS-DEC-02` now has an evidenced recommendation** — see
`VDR_FUNCTIONAL_OWNERSHIP_RECONCILIATION_REPORT.md` §4. It remains **Boss's decision**.

## 5. Non-Inventory objects that carry stock quantity — the co-ownership candidates

These 8 objects are defined outside Inventory and **move or hold stock quantity**. They are where a
naive boundary either wrongly includes a whole cluster or wrongly excludes a real dependency.

| Object | Cluster | Displayed by Inventory | Financial | Installed |
|--------|---------|:---:|:---:|---|
| production order | MANUFACTURING | **yes** | **yes** | yes |
| bill of materials · its lines · its by-products | MANUFACTURING | — | — | yes |
| manufacturing teardown order | MANUFACTURING | — | — | yes |
| master-schedule forecast suggestion | MANUFACTURING | — | — | yes |
| repair order | REPAIR | — | — | yes |
| field-service stock tracking line | FIELD SERVICE | — | — | yes |

**Only the production order is a true co-owner.** The other seven are **triggering** objects: they
cause Inventory facts without being Inventory.

## 6. Matrix

| Object | Kind | Primary functional owner (module) | How derived | Cluster | Ownership class | Shown in Inventory app | Carries stock quantity | Carries financial field | Installed on an observed deployment |
|---|---|---|---|---|---|:--:|:--:|:--:|---|
| `barcode.nomenclature` | ? | `barcodes` | SOLE DECLARER | BARCODE | **CONSUMING MODULE** | yes | — | — | **no** |
| `delivery.carrier` | ? | `delivery` | DEPENDENCY ROOT | DELIVERY | **CONSUMING MODULE** | yes | — | — | **no** |
| `delivery.zip.prefix` | ? | `delivery` | SOLE DECLARER | DELIVERY | **CONSUMING MODULE** | yes | — | — | **no** |
| `fsm.stock.tracking.line` | TransientModel | `industry_fsm_stock` | SOLE DECLARER | FIELD_SERVICE | **TRIGGERING MODULE** | — | yes | — | yes |
| `confirm.stock.sms` | TransientModel | `stock_sms` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `expiry.picking.confirmation` | TransientModel | `product_expiry` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `lot.label.layout` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `picking.label.type` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `product.removal` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `product.replenish` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `product.value` | Model | `stock_account` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | yes | yes |
| `report.stock.label_lot_template_view` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `report.stock.label_product_product_view` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `report.stock.quantity` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `report.stock.report_reception` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `report.stock.report_stock_rule` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.add.to.wave` | TransientModel | `stock_picking_batch` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.backorder.confirmation` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.backorder.confirmation.line` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.forecasted_product_product` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.forecasted_product_template` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.inventory.adjustment.name` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.inventory.conflict` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.inventory.warning` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.landed.cost` | Model | `stock_landed_costs` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | yes | yes |
| `stock.location` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | yes | yes |
| `stock.lot` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | yes | yes | yes |
| `stock.move` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | yes | yes | yes |
| `stock.move.line` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | yes | — | yes |
| `stock.orderpoint.snooze` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.package` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | yes | yes |
| `stock.package.destination` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.package.history` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.package.type` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.picking` | Model | `stock` | DEPENDENCY ROOT | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.picking.batch` | Model | `stock_picking_batch` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.picking.type` | Model | `stock` | DEPENDENCY ROOT | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.put.in.pack` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.putaway.rule` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.quant` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | yes | yes |
| `stock.quant.relocate` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.quantity.history` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.reference` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.replenish.mixin` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.replenishment.info` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.replenishment.option` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.report` | Model | `stock_enterprise` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | yes | — | yes |
| `stock.request.count` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.return.picking` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.return.picking.line` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `stock.route` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.rule` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.rules.report` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.scrap` | Model | `stock` | DEPENDENCY ROOT | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.scrap.reason.tag` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.storage.category` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.storage.category.capacity` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `stock.traceability.report` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.valuation.adjustment.lines` | Model | `stock_landed_costs` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `stock.warehouse` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | yes | — | — | yes |
| `stock.warehouse.orderpoint` | Model | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock.warn.insufficient.qty` | AbstractModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | yes | — | yes |
| `stock.warn.insufficient.qty.scrap` | TransientModel | `stock` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `stock_barcode.cancel.operation` | TransientModel | `stock_barcode` | SOLE DECLARER | INVENTORY | **PRIMARY OWNER** | — | — | — | yes |
| `l10n_cl.dte.caf` | ? | `l10n_cl_edi` | SOLE DECLARER | LOCALISATION | **OPTIONAL MODULE** | yes | — | — | **no** |
| `l10n_mx_edi.customs.document.type` | Model | `l10n_mx_edi_stock` | SOLE DECLARER | LOCALISATION | **OPTIONAL MODULE** | yes | — | — | **no** |
| `l10n_mx_edi.customs.regime` | Model | `l10n_mx_edi_stock` | SOLE DECLARER | LOCALISATION | **OPTIONAL MODULE** | yes | — | — | **no** |
| `l10n_pe_edi.vehicle` | Model | `l10n_pe_edi_stock` | SOLE DECLARER | LOCALISATION | **OPTIONAL MODULE** | yes | — | — | **no** |
| `l10n_tr.nilvera.trailer.plate` | Model | `l10n_tr_nilvera_edispatch` | SOLE DECLARER | LOCALISATION | **OPTIONAL MODULE** | yes | — | — | **no** |
| `mrp.bom` | Model | `mrp` | DEPENDENCY ROOT | MANUFACTURING | **TRIGGERING MODULE** | — | yes | — | yes |
| `mrp.bom.byproduct` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **TRIGGERING MODULE** | — | yes | — | yes |
| `mrp.bom.line` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **TRIGGERING MODULE** | — | yes | — | yes |
| `mrp.mps.forecast.details` | TransientModel | `mrp_mps` | SOLE DECLARER | MANUFACTURING | **DEPENDENT MODULE** | — | — | — | yes |
| `mrp.mps.forecast.suggestion` | TransientModel | `mrp_mps` | SOLE DECLARER | MANUFACTURING | **TRIGGERING MODULE** | — | yes | — | yes |
| `mrp.product.forecast` | Model | `mrp_mps` | SOLE DECLARER | MANUFACTURING | **DEPENDENT MODULE** | — | — | — | yes |
| `mrp.production` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **CROSS-MODULE CO-OWNER** | yes | yes | yes | yes |
| `mrp.production.group` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **DEPENDENT MODULE** | — | — | — | yes |
| `mrp.production.schedule` | Model | `mrp_mps` | SOLE DECLARER | MANUFACTURING | **CONSUMING MODULE** | yes | — | — | yes |
| `mrp.routing.workcenter` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **DEPENDENT MODULE** | — | — | — | yes |
| `mrp.unbuild` | Model | `mrp` | SOLE DECLARER | MANUFACTURING | **TRIGGERING MODULE** | — | yes | — | yes |
| `mrp.workorder` | Model | `mrp` | DEPENDENCY ROOT | MANUFACTURING | **DEPENDENT MODULE** | — | — | yes | yes |
| `stock.warn.insufficient.qty.unbuild` | TransientModel | `mrp` | SOLE DECLARER | MANUFACTURING | **DEPENDENT MODULE** | — | — | — | yes |
| `res.config.settings` | ? | `base` | SOLE DECLARER | PLATFORM | **CONSUMING MODULE** | yes | — | yes | **no** |
| `pos.session` | Model | `point_of_sale` | SOLE DECLARER | POS | **DEPENDENT MODULE** | — | — | yes | yes |
| `product.attribute` | ? | `product` | DEPENDENCY ROOT | PRODUCT | **CONSUMING MODULE** | yes | — | — | **no** |
| `product.category` | ? | `product` | DEPENDENCY ROOT | PRODUCT | **CONSUMING MODULE** | yes | — | yes | **no** |
| `product.product` | ? | `product` | DEPENDENCY ROOT | PRODUCT | **CONSUMING MODULE** | yes | — | yes | **no** |
| `product.template` | ? | `product` | DEPENDENCY ROOT | PRODUCT | **CONSUMING MODULE** | yes | — | yes | **no** |
| `uom.uom` | ? | `uom` | DEPENDENCY ROOT | PRODUCT | **CONSUMING MODULE** | yes | — | — | **no** |
| `quality.check.wizard` | TransientModel | `quality_control` | SOLE DECLARER | QUALITY | **DEPENDENT MODULE** | — | — | — | yes |
| `repair.order` | Model | `repair` | SOLE DECLARER | REPAIR | **TRIGGERING MODULE** | — | yes | — | yes |
| `stock.warn.insufficient.qty.repair` | TransientModel | `repair` | SOLE DECLARER | REPAIR | **DEPENDENT MODULE** | — | — | — | yes |
| `amazon.account` | Model | `sale_amazon` | SOLE DECLARER | SALES_CHANNEL | **DEPENDENT MODULE** | — | — | — | **no** |
| `lazada.order.item` | Model | `sale_lazada` | SOLE DECLARER | SALES_CHANNEL | **DEPENDENT MODULE** | — | — | — | yes |
| `lazada.shop` | Model | `sale_lazada` | SOLE DECLARER | SALES_CHANNEL | **DEPENDENT MODULE** | — | — | — | yes |
| `shopee.shop` | Model | `sale_shopee` | SOLE DECLARER | SALES_CHANNEL | **DEPENDENT MODULE** | — | — | — | yes |
---

## 7. Findings

### FO-F-01 — Inventory owns 62.5% of the objects its mechanical boundary contains (**CRITICAL for scope**)
60 of 96. The remaining 36 belong to eight other clusters. A research population built on module
extension therefore over-states the subject by **60%** in object terms.

### FO-F-02 — Module extension is not ownership, and the point-of-sale cluster proves it
The point-of-sale cluster contributed **34 of the 149 modules** in the mechanical boundary — the
largest single contributor, ahead of Inventory's own 21 — and **owns exactly one object**. Its modules
extend the operation-type, the product and the unit-of-measure objects; extending is not owning.

Composition of the mechanical 149-module boundary, by the cluster its module name places it in:

| Cluster | Modules | Objects owned |
|---------|--------:|--------------:|
| POS | **34** | **1** |
| LOCALISATION | 21 | 5 |
| **INVENTORY** | **21** | **60** |
| MANUFACTURING | 17 | 13 |
| DELIVERY | 15 | 2 |
| SALES | 13 | 4 |
| PROJECT | 8 | 0 |
| QUALITY | 7 | 1 |
| PURCHASE | 4 | 0 |
| REPAIR | 3 | 2 |
| WEBSITE · MESSAGING · HELPDESK · FIELD SERVICE | 6 | 1 |
| | **149** | **96** |

> **Inventory contributes 14% of the modules and owns 63% of the objects. The point-of-sale cluster
> contributes 23% of the modules and owns 1%.** The two columns measure different things, and a
> research population built on the first is not a population of the second.

Two caveats stated rather than glossed: this table clusters modules by **name**, which is a weaker
instrument than the dependency-root derivation used for the object column — 13 of the 34 point-of-sale
modules are country-localisation modules and could equally be counted under LOCALISATION. The
**object** column carries no such ambiguity, and the argument rests on it.

### FO-F-03 — Exactly one genuine cross-module co-ownership exists
The **production order** is displayed inside the Inventory application, carries stock quantity, and
carries financial fields. It cannot be assigned to one side. **It must be researched jointly** by the
Inventory and Manufacturing subjects, with one named owner for each of its facts — not researched
twice and not assumed.

### FO-F-04 — Seven objects trigger Inventory facts without being visible in Inventory
Bills of materials and their lines and by-products, the teardown order, the master-schedule
suggestion, the repair order and the field-service tracking line all carry stock quantity and appear
nowhere in the Inventory application. **A menu-driven population cannot see any of them** — which is
`MENU COVERAGE != FUNCTION COVERAGE` restated as an ownership fact.

### FO-F-05 — The prior programme already ruled on the financial ownership boundary and it holds
Principle `P-07` — *Inventory emits facts; Accounting decides postings* — was established by the prior
R4 deep research and approved. This matrix **independently corroborates it**: the 7 Inventory objects
carrying financial fields carry **values and account references**, and the posting decision lives in
the accounting domain. **Nothing here supersedes `P-07`; it is confirmed.**

### FO-F-06 — Five objects are optional-module dependent and are installed nowhere observed
The country-localisation objects exist in source and are absent from both observed deployments.
**They are `SOURCE PRESENT / RUNTIME UNREACHABLE` in every deployment measured** — see `00C`.
They should be excluded from the applicable baseline population and re-admitted per tenant.
