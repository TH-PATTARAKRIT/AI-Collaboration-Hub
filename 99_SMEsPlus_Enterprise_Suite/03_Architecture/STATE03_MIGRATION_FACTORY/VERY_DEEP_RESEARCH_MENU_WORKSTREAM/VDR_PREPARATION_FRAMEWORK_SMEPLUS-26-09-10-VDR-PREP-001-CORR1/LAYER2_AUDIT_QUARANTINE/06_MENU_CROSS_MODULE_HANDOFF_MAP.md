# 06_MENU_CROSS_MODULE_HANDOFF_MAP.md
# Register 06 — Cross-Module Handoff Map (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. Population

| Clause | Declaration |
|--------|-------------|
| **POPULATION** | Every declared relational field crossing the OWNED boundary in either direction |
| **PATTERN** | AST field census over **all 1,433 modules** of R1 (not only the Inventory module set — the inbound direction is owned by other domains and would be invisible from inside) |
| **UNIT** | One declared relational field = one edge |
| **ELIGIBILITY** | 1,433 modules, 16,206 code files, 27,660 field declarations, 0 parse failures |

**63 external objects are referenced by Inventory. 68 external objects reference Inventory.
90 distinct external objects participate.**

### Method note — why the census had to be system-wide
An inbound edge is declared by the *other* domain's module. A handoff map built only from the domain's
own modules is structurally blind to every inbound dependency — that is, to everything that would break
if the domain changed. This is `CORR-F-09`.

---

## 2. Map

| External object | Outbound refs (Inventory → it) | Inbound refs (it → Inventory) | Direction | Owning domain (by declaring module) |
|---|--:|--:|---|---|
| `res.company` | 35 | 6 | both | account, base, l10n_au_hr_payroll_api, l10n_it_riba, |
| `product.product` | 31 | 7 | both | documents_product, point_of_sale, product |
| `res.partner` | 30 | 6 | both | account_avatax, base, bus, equity, l10n_tr_nilvera,  |
| `uom.uom` | 25 | 1 | both | point_of_sale, uom |
| `quality.check` | 13 | 11 | both | quality |
| `product.template` | 12 | 7 | both | documents_product, point_of_sale, product, website_s |
| `res.users` | 16 | 2 | both | base, bus, l10n_au_hr_payroll_api, point_of_sale |
| `delivery.carrier` | 2 | 15 | both | delivery, website_sale |
| `sale.order.line` | 5 | 9 | both | pos_sale, sale, sale_timesheet_enterprise |
| `sale.order` | 7 | 7 | both | account_avatax_sale, pos_sale, sale, sale_external_t |
| `account.move` | 6 | 7 | both | account, account_avatax, account_external_tax, accou |
| `product.category` | 7 | 5 | both | point_of_sale, product |
| `quality.alert` | 4 | 6 | both | quality |
| `hr.employee` | 7 | 1 | both | documents_hr, hr, hr_expense_stripe, l10n_au_hr_payr |
| `product.template.attribute.value` | 8 | 0 | outbound | point_of_sale, pos_enterprise, product |
| `purchase.order.line` | 3 | 4 | both | purchase |
| `res.currency` | 7 | 0 | outbound | base, point_of_sale |
| `pos.order` | 3 | 4 | both | l10n_br_edi_pos, point_of_sale, pos_avatax |
| `helpdesk.ticket` | 3 | 3 | both | helpdesk, helpdesk_timesheet |
| `pos.config` | 1 | 5 | both | point_of_sale, pos_hr |
| `mrp.eco` | 2 | 4 | both | mrp_plm |
| `ir.attachment` | 6 | 0 | outbound | base, bus |
| `purchase.order` | 3 | 3 | both | purchase |
| `quality.point` | 2 | 3 | both | quality |
| `ir.sequence` | 5 | 0 | outbound | base |
| `mrp.workcenter` | 3 | 2 | both | mrp, mrp_account, mrp_maintenance, mrp_workorder |
| `account.analytic.line` | 4 | 0 | outbound | analytic, timesheet_grid |
| `crm.team` | 4 | 0 | outbound | crm, sales_team |
| `fsm.stock.tracking` | 2 | 2 | both | industry_fsm_stock |
| `l10n_ro_edi.document` | 2 | 2 | both | l10n_ro_edi |
| `rental.order.wizard.line` | 0 | 4 | inbound | sale_renting |
| `iot.device` | 3 | 1 | both | iot, pos_iot |
| `mrp.eco.bom.change` | 0 | 4 | inbound | mrp_plm |
| `l10n_latam.document.type` | 4 | 0 | outbound | l10n_cl_edi_pos, l10n_latam_invoice_document, l10n_p |
| `res.country` | 3 | 0 | outbound | base, point_of_sale, pos_self_order |
| `mrp.workcenter.productivity` | 1 | 2 | both | mrp |
| `l10n_uy_edi.document` | 2 | 1 | both | l10n_uy_edi |
| `product.supplierinfo` | 3 | 0 | outbound | product |
| `amazon.marketplace` | 3 | 0 | outbound | sale_amazon |
| `project.project` | 3 | 0 | outbound | documents_project, project, timesheet_grid |
| `maintenance.request` | 1 | 2 | both | maintenance |
| `stock.landed.cost.lines` | 2 | 1 | both | stock_landed_costs |
| `mrp.production.serials` | 0 | 2 | inbound | mrp |
| `website` | 1 | 1 | both | website |
| `amazon.offer` | 1 | 1 | both | sale_amazon |
| `lazada.item` | 1 | 1 | both | sale_lazada |
| `pos.payment.method` | 1 | 1 | both | point_of_sale |
| `account.payment` | 1 | 1 | both | account |
| `mrp_production.additional.workorder` | 0 | 2 | inbound | mrp_workorder |
| `shopee.account` | 1 | 1 | both | sale_shopee |
| `purchase.requisition` | 0 | 2 | inbound | purchase_requisition |
| `l10n.in.ewaybill` | 1 | 1 | both | l10n_in_ewaybill |
| `account.journal` | 2 | 0 | outbound | account |
| `l10n_mx_edi.document` | 1 | 1 | both | l10n_mx_edi |
| `shopee.item` | 1 | 1 | both | sale_shopee |
| `account.analytic.account` | 0 | 2 | inbound | analytic |
| `account.bank.statement.line` | 1 | 1 | both | account, account_accountant, account_accountant_batc |
| `purchase.requisition.line` | 1 | 1 | both | purchase_requisition |
| `l10n_uy_edi.addenda` | 2 | 0 | outbound | l10n_uy_edi |
| `l10n_cl.edi.reference` | 1 | 1 | both | l10n_cl_edi |
| `fleet.vehicle` | 2 | 0 | outbound | documents_fleet, fleet |
| `pos.payment` | 0 | 1 | inbound | point_of_sale |
| `mrp.eco.routing.change` | 0 | 1 | inbound | mrp_plm |
| `mrp.production.split` | 0 | 1 | inbound | mrp |
| `res.config.settings` | 0 | 1 | inbound | base |
| `mrp.consumption.warning` | 0 | 1 | inbound | mrp |
| `mrp.production.backorder` | 0 | 1 | inbound | mrp |
| `stock.picking.to.batch` | 0 | 1 | inbound | stock_picking_batch |
| `quality.point.test_type` | 1 | 0 | outbound | quality |
| `propose.change` | 0 | 1 | inbound | mrp_workorder |
| `account.account` | 1 | 0 | outbound | account, l10n_dk, point_of_sale |
| `fleet.vehicle.model.category` | 1 | 0 | outbound | fleet |
| `pos.daily.sales.reports.wizard` | 0 | 1 | inbound | point_of_sale |
| `product.label.layout` | 0 | 1 | inbound | product |
| `sale.report` | 0 | 1 | inbound | sale |
| `sale.rental.report` | 0 | 1 | inbound | sale_renting |
| `account.intrastat.code` | 1 | 0 | outbound | account_intrastat |
| `report.pos.order` | 0 | 1 | inbound | point_of_sale |
| `mrp.production.backorder.line` | 0 | 1 | inbound | mrp |
| `resource.calendar` | 1 | 0 | outbound | resource |
| `mrp.account.wip.accounting` | 0 | 1 | inbound | mrp_account |
| `resource.calendar.leaves` | 1 | 0 | outbound | resource |
| `mrp.consumption.warning.line` | 0 | 1 | inbound | mrp |
| `repair.tags` | 1 | 0 | outbound | repair |
| `mrp.report` | 0 | 1 | inbound | mrp_account_enterprise |
| `approval.product.line` | 0 | 1 | inbound | approvals |
| `purchase.report` | 0 | 1 | inbound | purchase |
| `change.production.qty` | 0 | 1 | inbound | mrp |
| `maintenance.equipment` | 0 | 1 | inbound | maintenance |
| `account.tax` | 1 | 0 | outbound | account, point_of_sale |
---

## 3. Findings

### XM-F-01 — Inventory is referenced by more of the system than it references
68 external objects point **into** Inventory against 63 it points **out** to. **Inventory is a
dependency hub, not a leaf.** Any SMEsPlus decision to change an Inventory object's identity,
lifecycle or scoping has a blast radius owned by other domains.

### XM-F-02 — The accounting boundary is thin and specific (**CRITICAL**)
Direct declared references from Inventory objects to accounting objects are few and named:
a movement carries a journal-entry reference and analytic lines; a landed-cost document carries a
journal, a journal entry and a vendor bill; a location carries a valuation account; a production
document carries work-in-progress entries; a work step carries three separate analytic-line
collections.

**The financial handoff is therefore concentrated in a small number of fields, each of which is a
Critical Area item.** This is a favourable finding for design — the surface is small — and a dangerous
one for research, because a *small* surface is easy to believe is *complete*.
**No claim of completeness is made here:** the declared-field census cannot see postings created in
code without a stored reference. Declared as `GAP-INV-06`, size unmeasured.

### XM-F-03 — Manufacturing, quality, point-of-sale, repair and delivery are inside the mechanical boundary
The mechanically-derived module set (149) draws in the manufacturing, quality, point-of-sale, repair,
field-service and delivery clusters, because they extend Inventory objects. **Whether the SMEsPlus
Inventory research subject includes them is a scope decision, not a derivation.**
Raised as `BOSS-DEC-02` with the derived set published so the decision is made against evidence.

### XM-F-04 — The heaviest external couplings are to master data, not to transactions
Company, product, partner, unit-of-measure and user account for the largest edge counts in both
directions. This confirms the parent workstream's sequencing instinct — the master-data subjects
(`VDR-MD-02`, `VDR-MD-03`, `VDR-MD-04`) are genuine prerequisites, and this register supplies the
evidence for that ordering rather than assuming it.

### XM-F-05 — Sales and purchase couple to Inventory in both directions at line level
Order lines on both sides reference Inventory objects and are referenced by them. Bidirectional
line-level coupling is where partial delivery, backorder, over-receipt and return semantics live.
These are `VDR-PUR-06`, `VDR-SAL-04` and `VDR-INV-02/03/04` and they cannot be researched
independently of one another.
