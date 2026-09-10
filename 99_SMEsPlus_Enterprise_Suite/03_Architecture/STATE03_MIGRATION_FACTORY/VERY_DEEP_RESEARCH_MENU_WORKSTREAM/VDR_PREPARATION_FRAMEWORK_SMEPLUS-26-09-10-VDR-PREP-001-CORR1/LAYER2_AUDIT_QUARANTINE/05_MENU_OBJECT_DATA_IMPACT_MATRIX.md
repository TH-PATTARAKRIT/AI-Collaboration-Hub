# 05_MENU_OBJECT_DATA_IMPACT_MATRIX.md
# Register 05 — Object / Data Impact Matrix (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. Population and boundary

**OWNED objects: 86.** **BOUNDARY objects: 10** (consumed or extended, lifecycle owned elsewhere).

The boundary set is published because a boundary described in prose is not a boundary:

| Boundary object | Lifecycle owned by | Inventory's relationship |
|-----------------|--------------------|--------------------------|
| product template / product / product category / product attribute | Product master domain | extended and consumed |
| unit of measure | Shared reference master | consumed |
| barcode nomenclature | Barcode domain | consumed |
| shipping carrier / carrier postcode prefix | Delivery domain | extended and consumed |
| configuration-settings object | Platform | extended |
| one country e-document credential object | Localisation | consumed |

**Rule applied: `stop at one hop and publish the complement`.** Relational closure to fixpoint
degenerates to 1,559 objects / 1,071 modules — see `00_SOURCE_LEARNING_MASTER_LIST.md` §7.

Composition: **47 persistent** · **31 transient (wizard)** · **8 abstract/report**.

---

## 2. Matrix

| Object | Kind | Fields | required | computed | stored-computed | related | Views | Constraints | Behaviours | company scope |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| `amazon.account` | Model | 22 | 5 | 5 | 1 | 0 | 4 | 0 | 17 | yes |
| `confirm.stock.sms` | TransientModel | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | n/a |
| `expiry.picking.confirmation` | TransientModel | 6 | 1 | 2 | 0 | 0 | 2 | 0 | 2 | n/a |
| `fsm.stock.tracking.line` | TransientModel | 9 | 1 | 2 | 0 | 0 | 1 | 0 | 1 | yes |
| `l10n_mx_edi.customs.document.type` | Model | 3 | 3 | 0 | 0 | 0 | 1 | 1 | 0 | **NO** |
| `l10n_mx_edi.customs.regime` | Model | 3 | 3 | 0 | 0 | 0 | 1 | 1 | 0 | **NO** |
| `l10n_pe_edi.vehicle` | Model | 7 | 2 | 0 | 0 | 0 | 3 | 0 | 1 | yes |
| `l10n_tr.nilvera.trailer.plate` | Model | 2 | 1 | 0 | 0 | 0 | 2 | 1 | 0 | **NO** |
| `lazada.order.item` | Model | 4 | 3 | 0 | 0 | 0 | 0 | 0 | 2 | **NO** |
| `lazada.shop` | Model | 25 | 8 | 3 | 0 | 0 | 3 | 1 | 11 | yes |
| `lot.label.layout` | TransientModel | 3 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | n/a |
| `mrp.bom` | Model | 36 | 6 | 8 | 0 | 1 | 15 | 1 | 31 | yes |
| `mrp.bom.byproduct` | Model | 11 | 3 | 1 | 1 | 3 | 1 | 0 | 2 | yes |
| `mrp.bom.line` | Model | 17 | 4 | 3 | 0 | 6 | 1 | 1 | 10 | yes |
| `mrp.mps.forecast.details` | TransientModel | 9 | 0 | 7 | 0 | 0 | 1 | 0 | 4 | n/a |
| `mrp.mps.forecast.suggestion` | TransientModel | 8 | 2 | 3 | 0 | 1 | 1 | 0 | 3 | n/a |
| `mrp.product.forecast` | Model | 6 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | **NO** |
| `mrp.production` | Model | 115 | 9 | 67 | 18 | 9 | 32 | 2 | 123 | yes |
| `mrp.production.group` | Model | 4 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | **NO** |
| `mrp.production.schedule` | Model | 17 | 3 | 3 | 2 | 3 | 2 | 1 | 8 | yes |
| `mrp.routing.workcenter` | Model | 27 | 3 | 9 | 0 | 3 | 9 | 0 | 13 | yes |
| `mrp.unbuild` | Model | 16 | 6 | 6 | 6 | 3 | 5 | 1 | 9 | yes |
| `mrp.workorder` | Model | 85 | 3 | 33 | 10 | 23 | 25 | 0 | 62 | yes |
| `picking.label.type` | TransientModel | 3 | 1 | 0 | 0 | 0 | 1 | 0 | 0 | n/a |
| `pos.session` | Model | 42 | 3 | 9 | 1 | 4 | 7 | 0 | 21 | yes |
| `product.removal` | Model | 2 | 2 | 0 | 0 | 0 | 1 | 0 | 0 | **NO** |
| `product.replenish` | TransientModel | 11 | 7 | 3 | 1 | 1 | 2 | 0 | 11 | yes |
| `product.value` | Model | 13 | 4 | 4 | 1 | 2 | 1 | 0 | 2 | yes |
| `quality.check.wizard` | TransientModel | 35 | 2 | 4 | 1 | 28 | 3 | 0 | 9 | n/a |
| `repair.order` | Model | 52 | 10 | 25 | 11 | 5 | 10 | 0 | 50 | yes |
| `report.stock.label_lot_template_view` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `report.stock.label_product_product_view` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `report.stock.quantity` | Model | 7 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | yes |
| `report.stock.report_reception` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | n/a |
| `report.stock.report_stock_rule` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `shopee.shop` | Model | 20 | 7 | 3 | 0 | 0 | 3 | 0 | 11 | yes |
| `stock.add.to.wave` | TransientModel | 5 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | n/a |
| `stock.backorder.confirmation` | TransientModel | 5 | 0 | 2 | 0 | 0 | 2 | 0 | 2 | n/a |
| `stock.backorder.confirmation.line` | TransientModel | 3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `stock.forecasted_product_product` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | n/a |
| `stock.forecasted_product_template` | AbstractModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `stock.inventory.adjustment.name` | TransientModel | 5 | 0 | 1 | 0 | 0 | 2 | 0 | 1 | n/a |
| `stock.inventory.conflict` | TransientModel | 2 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | n/a |
| `stock.inventory.warning` | TransientModel | 1 | 0 | 0 | 0 | 0 | 2 | 0 | 2 | n/a |
| `stock.landed.cost` | Model | 18 | 4 | 1 | 1 | 2 | 9 | 1 | 9 | yes |
| `stock.location` | Model | 31 | 2 | 12 | 4 | 0 | 9 | 3 | 17 | yes |
| `stock.lot` | Model | 39 | 2 | 26 | 7 | 5 | 16 | 0 | 28 | yes |
| `stock.move` | Model | 135 | 8 | 53 | 23 | 20 | 29 | 1 | 119 | yes |
| `stock.move.line` | Model | 79 | 5 | 25 | 8 | 34 | 32 | 1 | 55 | yes |
| `stock.orderpoint.snooze` | TransientModel | 3 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | n/a |
| `stock.package` | Model | 30 | 1 | 18 | 3 | 1 | 7 | 0 | 21 | yes |
| `stock.package.destination` | TransientModel | 3 | 2 | 1 | 0 | 0 | 1 | 0 | 2 | n/a |
| `stock.package.history` | Model | 13 | 4 | 0 | 0 | 1 | 2 | 0 | 1 | yes |
| `stock.package.type` | Model | 36 | 2 | 4 | 1 | 1 | 8 | 5 | 10 | yes |
| `stock.picking` | Model | 254 | 4 | 90 | 25 | 35 | 73 | 2 | 154 | yes |
| `stock.picking.batch` | Model | 58 | 3 | 31 | 9 | 7 | 24 | 0 | 54 | yes |
| `stock.picking.type` | Model | 129 | 13 | 40 | 12 | 2 | 26 | 0 | 39 | yes |
| `stock.put.in.pack` | TransientModel | 15 | 0 | 5 | 2 | 4 | 3 | 0 | 6 | n/a |
| `stock.putaway.rule` | Model | 10 | 3 | 1 | 1 | 0 | 2 | 0 | 5 | yes |
| `stock.quant` | Model | 42 | 4 | 11 | 3 | 17 | 23 | 0 | 39 | yes |
| `stock.quant.relocate` | TransientModel | 9 | 0 | 5 | 1 | 1 | 1 | 0 | 5 | yes |
| `stock.quantity.history` | TransientModel | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | n/a |
| `stock.reference` | Model | 7 | 1 | 1 | 0 | 0 | 6 | 0 | 0 | **NO** |
| `stock.replenish.mixin` | AbstractModel | 6 | 0 | 3 | 0 | 0 | 0 | 0 | 3 | n/a |
| `stock.replenishment.info` | TransientModel | 18 | 4 | 7 | 2 | 8 | 3 | 0 | 7 | n/a |
| `stock.replenishment.option` | TransientModel | 10 | 0 | 3 | 0 | 4 | 2 | 0 | 3 | n/a |
| `stock.report` | Model | 18 | 0 | 0 | 0 | 0 | 6 | 0 | 1 | yes |
| `stock.request.count` | TransientModel | 4 | 1 | 1 | 0 | 0 | 1 | 0 | 1 | n/a |
| `stock.return.picking` | TransientModel | 10 | 0 | 5 | 2 | 3 | 4 | 0 | 10 | yes |
| `stock.return.picking.line` | TransientModel | 8 | 2 | 1 | 0 | 2 | 0 | 0 | 1 | n/a |
| `stock.route` | Model | 17 | 1 | 1 | 0 | 0 | 5 | 0 | 5 | yes |
| `stock.rule` | Model | 24 | 7 | 2 | 0 | 2 | 7 | 0 | 8 | yes |
| `stock.rules.report` | TransientModel | 5 | 4 | 0 | 0 | 0 | 2 | 0 | 1 | n/a |
| `stock.scrap` | Model | 25 | 7 | 5 | 4 | 4 | 11 | 0 | 14 | yes |
| `stock.scrap.reason.tag` | Model | 3 | 1 | 0 | 0 | 0 | 0 | 1 | 0 | **NO** |
| `stock.storage.category` | Model | 9 | 2 | 3 | 0 | 0 | 2 | 1 | 1 | yes |
| `stock.storage.category.capacity` | Model | 6 | 2 | 0 | 0 | 2 | 1 | 3 | 0 | yes |
| `stock.traceability.report` | TransientModel | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | n/a |
| `stock.valuation.adjustment.lines` | Model | 12 | 3 | 2 | 2 | 1 | 0 | 0 | 2 | **NO** |
| `stock.warehouse` | Model | 62 | 8 | 2 | 0 | 4 | 11 | 3 | 12 | yes |
| `stock.warehouse.orderpoint` | Model | 43 | 8 | 25 | 5 | 5 | 10 | 1 | 39 | yes |
| `stock.warn.insufficient.qty` | AbstractModel | 5 | 4 | 1 | 0 | 0 | 1 | 0 | 2 | n/a |
| `stock.warn.insufficient.qty.repair` | TransientModel | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | n/a |
| `stock.warn.insufficient.qty.scrap` | TransientModel | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 2 | n/a |
| `stock.warn.insufficient.qty.unbuild` | TransientModel | 1 | 0 | 0 | 0 | 0 | 1 | 0 | 1 | n/a |
| `stock_barcode.cancel.operation` | TransientModel | 4 | 0 | 0 | 0 | 2 | 2 | 0 | 2 | n/a |
---

## 3. Findings

### OD-F-01 — 36.0% of the domain's objects are wizards, not records (**design-relevant**)
31 of 86 objects are transient. They hold user intent for the duration of one interaction and are then
discarded. **A migration or data-model design that treats the object census as the table census would
create 31 tables that should not exist**, and — more seriously — would miss that 31 business
interactions currently have **no persistent record of having occurred**. Whether SMEsPlus should
persist any of them is a design question, raised as `BOSS-DEC-05`.

### OD-F-02 — PARTLY CLOSED — 10 persistent objects declare no company scope, and one of them closes as a defect (**CRITICAL**)
Of 47 persistent objects, 10 declare no company field. Nine remain **undischarged dispositions** —
reference data where global scope may be correct.

**The tenth closes as a defect.** Independent challenge followed the valuation-adjustment line object
through every isolation layer: it declares **no company field**, carries **no row-level rule**, and its
**parent document also carries no row-level rule** — the parent declares a required company but nothing
filters on it. **The chain is unisolated at every level**, so there is no association for
"isolation by association" to work through. Carried to Register 07 `SS-F-11`.

The hedge in the original text — *"at least one is a valuation-adjustment object where it is not
obviously correct"* — was correct and was left open when one query would have closed it.
**A hedge is not a disposition.**

### OD-F-03 — 168 stored computed values (**CRITICAL**)
168 fields are computed **and stored**. A stored computed value is a **cached derivation**: it can be
stale, it can disagree with its inputs, and it is what reports read. For a valuation- and
quantity-bearing domain this is the single largest correctness surface in the register.
Every SMEsPlus equivalent must have a declared recomputation trigger and a declared staleness policy.

### OD-F-04 — Only 32 fields are change-tracked
Out of 1,846 declared fields, 32 carry change tracking. **Audit is the exception, not the rule.**
Which Inventory fields require an immutable audit trail is a SMEsPlus decision that cannot be inherited;
raised as `BOSS-DEC-06`.

### OD-F-05 — CORRECTED — the inventory valuation object was **replaced between generations** (**CRITICAL**)
**The substantive claim is confirmed; two counts attached to it are withdrawn.**

**Confirmed, and reproduced independently by challenge:** series-18 declares an append-only
**valuation-layer ledger**. Series-19 declares it **zero times**. It is replaced by a narrower object
whose own source documentation describes it as *"the history of manual update of a value"*, with the
current value carried **on the movement itself**.

**Withdrawn:** the "72 referencing files" and "15 remaining references, 14 tests plus one model file"
figures. Neither is reproducible: the referencing count varies from 64 to 90 with the pattern and the
prune, and the *"one model file"* descriptor is wrong — the single non-test reference in series-19 is
an **XML comment in a demo-data file**. Both parties reproduce the **declaration count**, and the claim
now rests on that alone: **72-ish referencing files in one generation against 0 declarations in the
other** is the wrong way to say it; **0 declarations against a declared object** is the right way.

**Undeclared asymmetry, now declared:** only **134 of the 149 domain modules exist in the series-18
comparator** — 15 are series-19-only. Any cross-generation count is a 149-module population against a
134-module one unless explicitly intersected.

**Also missed by the original census:** series-19 carries **two new valuation reporting objects** that
this register's object census does not list, because both are abstract. They are the audit surface the
removed ledger used to be, and they belong in the evidence for `CRITICAL-GAP-01`.

**Consequence:** any Inventory-valuation or cost-of-goods finding in this programme derived from
series-18 valuation-ledger behaviour is **generation-bounded and does not describe the target
generation.** Raised as `CRITICAL-GAP-01` and `BOSS-DEC-01`.

### OD-F-07 — In the target generation the valuation figure is writable and its audit log is deletable (**CRITICAL**) — *found by challenge*
The series-18 ledger was append-only. In series-19:

- the movement's value is a **plain writable stored column** — no compute, no change-tracking, no
  constraint;
- overriding it writes one row to the replacement object — **that row is the only record the override
  happened**;
- the inventory-manager role is granted **create, write and delete** on that object;
- it carries **no row-level rule** and **no deletion guard**.

**An inventory manager can overwrite a movement's valuation and then delete the only record that it was
overwritten.** `OD-F-05` stops at "replaced by a narrower object". The narrower object *is* the audit
trail, and it is unprotected. **This is the evidence `BOSS-DEC-01` needs and did not have.**

### OD-F-06 — Constraint count nearly doubles between generations
R2 (series-18): 20 declared constraints. R1 (series-19): 32. Both comparators agree on 20.
**The enforced data-integrity rules of the target generation are materially different from the
generation most prior programme research was performed against.**
