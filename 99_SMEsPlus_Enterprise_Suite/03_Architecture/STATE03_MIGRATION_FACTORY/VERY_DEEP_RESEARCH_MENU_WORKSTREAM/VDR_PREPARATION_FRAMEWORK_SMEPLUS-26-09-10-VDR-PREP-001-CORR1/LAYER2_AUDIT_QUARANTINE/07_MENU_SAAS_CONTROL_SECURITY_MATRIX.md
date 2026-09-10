# 07_MENU_SAAS_CONTROL_SECURITY_MATRIX.md
# Register 07 — SaaS Control & Security Matrix (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**
**Every item in this register is a Critical Area item and must reach 100% before any Gate.**

---

## 1. SMEsPlus SaaS principles applied

```
TENANT   = customer / security boundary
COMPANY  = legal / accounting / business boundary
Unrelated independent companies      = separate tenants by default
Business relationship                != shared tenant
Multi-tenant membership              != multi-tenant execution context
No lower-level relationship may weaken an upper-level security boundary
Reference behaviour                  != SMEsPlus behaviour
```

The reference system has **companies**. It has **no tenant concept at all**. Therefore **every row of
this register is evidence about the company boundary only**, and **nothing in it constitutes evidence
about tenant isolation.** That is stated first because the most likely misreading of this register is
to treat company isolation as a tenant-isolation precedent.

---

## 2. Measured control surface

| Control layer | Population | Measured |
|---------------|-----------:|----------|
| Security groups declared by the domain module set | 44 | 17 by the core inventory module; the rest by manufacturing, point-of-sale, work-order, lifecycle-management, expiry and pricing modules |
| Object-level access grants | 176 rows over 78 objects | 104 grant create · **59 grant delete** · **0 grant access without naming a group** |
| Row-level rules on OWNED objects | 28 | 17 are company-scoping rules |
| Elements gated by group in the UI | 633 | see Register 02 |
| Persistent objects | 47 | 37 carry a company field · **10 do not** |
| Persistent objects with **no row-level rule at all** | **22 of 47 (46.8%)** | |

---

## 3. Findings

### SS-F-01 — Core inventory structures are deliberately visible across companies (**CRITICAL**)
Nine company-scoping rules are written as *"belongs to one of my companies **or belongs to no
company**"*. The objects governed this way include **location, on-hand quantity, replenishment rule,
route, package and storage category** — i.e. the structural spine of the domain.

**A record created with no company is therefore visible to every company in the database.**

This is a deliberate reference-system pattern for shared configuration, and it is a **direct
contradiction of the SMEsPlus principle that no lower-level relationship may weaken an upper-level
boundary** — because a null-company record is precisely a record that has opted out of the boundary.

**Disposition: `CRITICAL GAP`.** SMEsPlus must decide explicitly whether a null-scope record may exist
at all. Raised as `BOSS-DEC-04`. **This behaviour must not be inherited by default.**

### SS-F-02 — 46.8% of persistent objects have no row-level isolation (**CRITICAL**)
22 of 47 persistent objects carry no record rule. Whatever isolation they have comes from object-level
grants and from the objects they hang off — that is, **isolation by association, not by construction**.

For a single-database multi-tenant SaaS this is the highest-severity structural finding in the Pilot.
**SMEsPlus cannot adopt isolation-by-association**; the boundary must be constructed per object.
Raised as `CRITICAL-GAP-02`.

### SS-F-03 — 10 persistent objects declare no company field
Carried from Register 05 `OD-F-02`. Each of the 10 needs an explicit disposition:
*reference data, correctly global* · *scoped by its parent* · *defect*. **None of the three may be
assumed.** Recorded as 10 undischarged dispositions, not as 10 defects.

### SS-F-04 — Delete is granted on one third of access rows
59 of 176 grants permit deletion. For a domain that carries quantity, ownership and valuation, which of
these deletions must be impossible in SMEsPlus — as opposed to merely restricted — is an
**immutability** decision. Raised as `BOSS-DEC-07`.

### SS-F-05 — Only 32 of 1,846 fields are change-tracked (1.7%)
Carried from Register 05 `OD-F-04`. **The reference system's audit trail is opt-in and sparse.**
An SMEsPlus audit design cannot be derived from it; it must be specified.

### SS-F-06 — The domain's visible shape is governed by 43 groups, 29 of which are roles
Carried from Register 02 `CD-F-01`. **Configuration and role are two independent axes** and both
determine what a user sees. A tenant-administration design that exposes only the configuration axis
leaves 67.4% of the gating surface unmanageable by the tenant.

### SS-F-07 — Cross-domain groups govern Inventory surface
Groups owned by accounting, sales, purchase, project, helpdesk, quality, manufacturing, point-of-sale,
website and analytic domains gate Inventory elements. In a multi-tenant product, **a domain whose
visibility is partly governed by another domain's role model cannot be certified in isolation.**
This constrains the parent workstream's bounded-subject model and is raised as `BOSS-DEC-02`.

### SS-F-08 — No evidence of any tenant concept was found, and that is a positive finding
The reference system's isolation vocabulary is entirely company-based. **Scope of this negative:**
R1, the 149-module Inventory set, the declared-record and declared-field census.
**It is not a claim about the whole reference system.** It is sufficient, however, to establish that
**SMEsPlus tenant isolation has no reference precedent and must be designed from first principles** —
which is the safe conclusion in either case.

### SS-F-09 — There is no segregation-of-duties approval mechanism on Inventory objects, and the near-miss is instructive
A three-form test was run over the 149-module set with a positive control.

| Form | Query | Result |
|------|-------|--------|
| 1 | approval-vocabulary scan over all module files | **238 files match** |
| 2 | declared fields on OWNED objects matching approval vocabulary | **23 fields** |
| 3 | positive control — same scan against a domain known to carry approval | **79 files — the pattern fires** |

**Form 1's 238 hits would have supported the opposite headline in either direction**, which is why
the classification, not the count, is the finding. Reading the 23 declared fields, the
approval-adjacent surface resolves into four things, **none of which is an internal approval control**:

1. **Regulatory e-document authorisation** — codes, numbers and dates issued by a tax authority
   (4 country localisations). External authorisation, not internal.
2. **Recipient signature capture** on the outbound document (`signature`, `is_signed`), itself gated
   by a configuration toggle. Evidence of receipt, not authorisation to act.
3. **Operational validation flags** on the operation type (barcode completeness checks). Guards, not
   approvals.
4. **Confirmation wizards** (backorder). A dialog, not a second party.

**Conclusion, with its scope attached:** within R1 and the 149-module Inventory set, **the domain's
own objects carry no maker-checker or delegated-authority mechanism.** Approval for the documents that
*trigger* inventory movement lives upstream in the purchase and sales domains and is out of this
subject's boundary.

**A first draft of this register recorded "zero approval mechanisms found". That statement was false
and was caught by the mandatory zero re-test (`VDR_COVERAGE_RULE.md` §3, control I4) before
publication.** Recorded here rather than silently corrected, because the value of the control is the
evidence that it fires.

---

## 4. Coverage state — Critical Areas

| Critical Area | Population established | Verified | State |
|---------------|-----------------------|----------|-------|
| Security | yes (44 / 176 / 28 / 633) | population only | **NOT 100%** |
| Tenant Isolation | **no reference population exists** | — | **NOT APPLICABLE TO REFERENCE — SMEsPlus-original design required** |
| Company Isolation | yes (17 scoping rules, 10 unscoped objects) | population only | **NOT 100%** |
| Approval Control | yes — see `SS-F-09`; **no segregation-of-duties mechanism located** | 0 | **`GAP-INV-07`** |
| Audit Trail | yes (32 tracked fields) | population only | **NOT 100%** |
| Identity / Immutability | not measured | 0 | **declared gap** |
| Data Integrity | yes (32 constraints) | population only | **NOT 100%** |
| Stock Ownership / Quantity / Valuation | population only; valuation object changed generation (`OD-F-05`) | 0 | **`CRITICAL-GAP-01`** |
| Financial Posting / Cross-Module Financial Handoff | thin declared surface; code-created postings unmeasured (`XM-F-02`) | 0 | **`GAP-INV-06`** |
| Period Close / Reversal | not measured in this domain | 0 | **declared gap** |

**No Critical Area is at 100%. Under `VDR_COVERAGE_RULE.md` §6 this alone forces `HOLD`,
irrespective of any overall percentage.**

---

## Appendix A — Row-level rules on OWNED objects (28)

| Learning ID | Record rule | Object | Restricted to groups | Domain | Module |
|---|---|---|---|---|---|
| LI-INV-RULE-0014 | Amazon Account multi-company | `amazon.account` | GLOBAL (all users) | `['|', ('company_id', '=', False),             ('company_id', 'in', company_ids)]` | sale_amazon |
| LI-INV-RULE-0001 | Vehicles PE | `l10n_pe_edi.vehicle` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | l10n_pe_edi_stock |
| LI-INV-RULE-0015 | Lazada Shop multi-company | `lazada.shop` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | sale_lazada |
| LI-INV-RULE-0004 | MRP BoMs Subcontractor | `mrp.bom` | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.bom_ids.ids)]` | mrp_subcontracting |
| LI-INV-RULE-0003 | MRP BoM Lines Subcontractor | `mrp.bom.line` | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.bom_ids.bom_line_ids.ids)]` | mrp_subcontracting |
| LI-INV-RULE-0007 | MRP Productions Subcontractor | `mrp.production` | [(4, ref('base.group_portal'))] | `[('subcontractor_id', '=', user.partner_id.commercial_partner_id.id)]` | mrp_subcontracting |
| LI-INV-RULE-0002 | MPS multi-company | `mrp.production.schedule` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | mrp_mps |
| LI-INV-RULE-0013 | Point Of Sale Session | `pos.session` | GLOBAL (all users) | `[('config_id.company_id', 'in', company_ids)]` | point_of_sale |
| LI-INV-RULE-0019 | report_stock_quantity_flow multi-company | `report.stock.quantity` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0016 | Shopee Shop multi-company | `shopee.shop` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | sale_shopee |
| LI-INV-RULE-0008 | Stock Locations Subcontractor | `stock.location` | [(4, ref('base.group_portal'))] | `[             '|',                 '|',                     '|',                         '` | mrp_subcontracting |
| LI-INV-RULE-0020 | Location multi-company | `stock.location` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0009 | Stock Lot Subcontractor | `stock.lot` | [(4, ref('base.group_portal'))] | `[         '|',             '|',                 ('product_id', 'in', user.partner_id.comme` | mrp_subcontracting |
| LI-INV-RULE-0011 | Stock Moves Subcontractor | `stock.move` | [(4, ref('base.group_portal'))] | `[         '|',              '|',                 ('production_id.subcontractor_id', '=', u` | mrp_subcontracting |
| LI-INV-RULE-0010 | Stock Move Lines Subcontractor | `stock.move.line` | [(4, ref('base.group_portal'))] | `[         '|',              '|',                 ('move_id.production_id.subcontractor_id'` | mrp_subcontracting |
| LI-INV-RULE-0022 | stock_package multi-company | `stock.package` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0005 | Stock Pickings Subcontractor | `stock.picking` | [(4, ref('base.group_portal'))] | `[('partner_id.commercial_partner_id', '=', user.partner_id.commercial_partner_id.id)]` | mrp_subcontracting |
| LI-INV-RULE-0017 | Portal Follower Transfers | `stock.picking` | [(4, ref('base.group_portal'))] | `['|', ('partner_id', '=', user.partner_id.id), ('sale_id.partner_id', '=', user.partner_id` | sale_stock |
| LI-INV-RULE-0028 | stock.picking.batch multi-company | `stock.picking.batch` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock_picking_batch |
| LI-INV-RULE-0006 | Stock Picking Types Subcontractor | `stock.picking.type` | [(4, ref('base.group_portal'))] | `['|', ('id', 'in', user.partner_id.commercial_partner_id.picking_ids.picking_type_id.ids),` | mrp_subcontracting |
| LI-INV-RULE-0023 | stock_quant multi-company | `stock.quant` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0027 | Stock Report multi-company | `stock.report` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock_enterprise |
| LI-INV-RULE-0021 | stock_route multi-company | `stock.route` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0018 | product_pulled_flow multi-company | `stock.rule` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0024 | stock_scrap_company multi-company | `stock.scrap` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0025 | stock_storage_category multi-company | `stock.storage.category` | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0012 | Warehouses Subcontractor | `stock.warehouse` | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.picking_ids.picking_type_id.warehouse_` | mrp_subcontracting |
| LI-INV-RULE-0026 | Warehouse multi-company | `stock.warehouse` | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
## Appendix B — Object-level access grants, by object (78 objects, 176 rows)

| Object | Access grants | Groups granted create | Groups granted delete | Unrestricted (no group) |
|---|--:|---|---|---|
| `amazon.account` | 1 | group_sale_manager | group_sale_manager | 0 |
| `confirm.stock.sms` | 1 | group_stock_user | — | 0 |
| `expiry.picking.confirmation` | 1 | group_stock_user | — | 0 |
| `fsm.stock.tracking.line` | 2 | group_stock_user | group_stock_user | 0 |
| `l10n_mx_edi.customs.document.type` | 1 | group_stock_user | group_stock_user | 0 |
| `l10n_mx_edi.customs.regime` | 1 | group_stock_user | group_stock_user | 0 |
| `l10n_pe_edi.vehicle` | 2 | group_stock_manager | group_stock_manager | 0 |
| `l10n_tr.nilvera.trailer.plate` | 1 | group_stock_user | group_stock_user | 0 |
| `lazada.order.item` | 3 | group_sale_manager | group_sale_manager | 0 |
| `lazada.shop` | 1 | group_sale_manager | group_sale_manager | 0 |
| `lot.label.layout` | 1 | group_stock_user | — | 0 |
| `mrp.bom` | 10 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.bom.byproduct` | 2 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.bom.line` | 10 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.mps.forecast.details` | 1 | group_mrp_user | — | 0 |
| `mrp.mps.forecast.suggestion` | 1 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.product.forecast` | 2 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.production` | 5 | group_mrp_user, group_sale_salesman | group_mrp_user | 0 |
| `mrp.production.group` | 1 | group_mrp_user | — | 0 |
| `mrp.production.schedule` | 2 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.routing.workcenter` | 2 | group_mrp_manager | group_mrp_manager | 0 |
| `mrp.unbuild` | 2 | group_mrp_user, group_mrp_manager | group_mrp_user, group_mrp_manager | 0 |
| `mrp.workorder` | 3 | group_mrp_user, group_mrp_manager, group_sale_salesman | group_mrp_user, group_mrp_manager | 0 |
| `picking.label.type` | 1 | group_stock_user | — | 0 |
| `pos.session` | 1 | group_pos_user | — | 0 |
| `product.removal` | 1 | — | — | 0 |
| `product.replenish` | 1 | group_stock_user | — | 0 |
| `product.value` | 1 | group_stock_manager | group_stock_manager | 0 |
| `quality.check.wizard` | 1 | group_quality_user | — | 0 |
| `repair.order` | 2 | group_stock_user | group_stock_user | 0 |
| `report.stock.quantity` | 1 | — | — | 0 |
| `shopee.shop` | 1 | group_sale_manager | group_sale_manager | 0 |
| `stock.add.to.wave` | 1 | group_stock_user | — | 0 |
| `stock.backorder.confirmation` | 1 | group_stock_user | — | 0 |
| `stock.backorder.confirmation.line` | 1 | group_stock_user | — | 0 |
| `stock.inventory.adjustment.name` | 2 | group_stock_manager, group_stock_user | — | 0 |
| `stock.inventory.conflict` | 1 | group_stock_manager | — | 0 |
| `stock.inventory.warning` | 1 | group_stock_manager | — | 0 |
| `stock.landed.cost` | 1 | group_stock_manager | group_stock_manager | 0 |
| `stock.location` | 9 | group_stock_manager | group_stock_manager | 0 |
| `stock.lot` | 2 | group_portal, group_stock_user | group_stock_user | 0 |
| `stock.move` | 12 | group_mrp_user, group_portal, group_pos_user, group_purchase_user, group_purchase_manager, group_sale_salesman, group_sale_manager, group_stock_manager, group_stock_user, group_account_invoice | group_mrp_user, group_pos_user, group_purchase_manager, group_sale_manager, group_stock_manager | 0 |
| `stock.move.line` | 4 | group_portal, group_stock_manager, group_stock_user, group_user | group_portal, group_stock_manager, group_stock_user, group_user | 0 |
| `stock.orderpoint.snooze` | 1 | group_stock_user | group_stock_user | 0 |
| `stock.package` | 3 | group_stock_manager, group_stock_user | group_stock_manager, group_stock_user | 0 |
| `stock.package.destination` | 1 | group_stock_user | — | 0 |
| `stock.package.history` | 1 | group_stock_user | — | 0 |
| `stock.package.type` | 3 | group_stock_manager | group_stock_manager | 0 |
| `stock.picking` | 12 | group_pos_user, group_purchase_user, group_purchase_manager, group_sale_salesman, group_sale_manager, group_stock_user, group_stock_manager, group_account_invoice | group_pos_user, group_purchase_user, group_purchase_manager, group_sale_manager, group_stock_user, group_stock_manager | 0 |
| `stock.picking.batch` | 1 | group_stock_user | group_stock_user | 0 |
| `stock.picking.type` | 4 | group_stock_manager | group_stock_manager | 0 |
| `stock.put.in.pack` | 1 | group_stock_user | — | 0 |
| `stock.putaway.rule` | 2 | group_stock_manager | group_stock_manager | 0 |
| `stock.quant` | 2 | group_stock_user | — | 0 |
| `stock.quant.relocate` | 1 | group_stock_manager | — | 0 |
| `stock.quantity.history` | 1 | group_stock_user | — | 0 |
| `stock.reference` | 1 | group_user | — | 0 |
| `stock.replenishment.info` | 1 | group_stock_manager | — | 0 |
| `stock.replenishment.option` | 1 | group_stock_user | — | 0 |
| `stock.report` | 1 | — | — | 0 |
| `stock.request.count` | 1 | group_stock_manager | — | 0 |
| `stock.return.picking` | 1 | group_stock_user | — | 0 |
| `stock.return.picking.line` | 1 | group_stock_user | group_stock_user | 0 |
| `stock.route` | 2 | group_stock_manager | group_stock_manager | 0 |
| `stock.rule` | 5 | group_sale_manager, group_stock_manager | group_sale_manager, group_stock_manager | 0 |
| `stock.rules.report` | 1 | group_stock_user | — | 0 |
| `stock.scrap` | 2 | group_stock_user, group_stock_manager | group_stock_manager | 0 |
| `stock.scrap.reason.tag` | 2 | group_stock_user, group_stock_manager | group_stock_manager | 0 |
| `stock.storage.category` | 2 | group_stock_manager | group_stock_manager | 0 |
| `stock.storage.category.capacity` | 2 | group_stock_manager | group_stock_manager | 0 |
| `stock.traceability.report` | 1 | group_stock_user | — | 0 |
| `stock.valuation.adjustment.lines` | 1 | group_stock_manager | group_stock_manager | 0 |
| `stock.warehouse` | 8 | group_stock_manager | group_stock_manager | 0 |
| `stock.warehouse.orderpoint` | 5 | group_stock_manager | group_stock_manager | 0 |
| `stock.warn.insufficient.qty.repair` | 1 | group_stock_user | — | 0 |
| `stock.warn.insufficient.qty.scrap` | 1 | group_stock_user | — | 0 |
| `stock.warn.insufficient.qty.unbuild` | 1 | group_mrp_user | — | 0 |
| `stock_barcode.cancel.operation` | 1 | group_stock_user | — | 0 |