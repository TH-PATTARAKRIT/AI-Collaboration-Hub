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
| Object-level access grants | **180** rows over 78 objects | 104 grant create · **59 grant delete** · **0 grant access without naming a group** |
| Row-level rules on OWNED objects | **46** | **34** are company-scoping rules; **16** admit a null company |
| Elements gated by group in the UI | 633 | see Register 02 |
| Persistent objects | 47 | 37 carry a company field · **10 do not** |
| Persistent objects with **no row-level rule at all** | **13 of 47 (27.7%)** | corrected by challenge — see `SS-F-02` |

---

## 3. Findings

### SS-F-01 — CORRECTED — Core inventory structures are deliberately visible across companies (**CRITICAL**)
**Sixteen** rules admit a null-company record. This register published **nine**, then **ten**; the
correct figure is **sixteen**. Two independent instrument defects, both in the same finding:

| Defect | Missed | Recorded as |
|--------|-------:|-------------|
| the predicate matched the **syntax** *"in my companies + no-company"* while the claim was about the **semantics**; an equivalent explicit disjunction was not matched | 1 | `CORR-F-26` |
| the extractor read only **one of the two declaration forms** the platform accepts for a rule's target object | 6 | `CORR-F-27` |

The objects governed this way are **not** only configuration. They include **location, on-hand
quantity, replenishment rule, route, package and storage category** — and also **lot / serial numbers**
and **movement lines**, which are transactional and traceability-bearing.

> **The correction made this finding materially worse, and it came from challenge, not from the
> producer.** A lot number visible across companies is a traceability boundary failure, not a shared
> configuration convenience.

**A record created with no company is therefore visible to every company in the database.**

This is a deliberate reference-system pattern for shared configuration, and it is a **direct
contradiction of the SMEsPlus principle that no lower-level relationship may weaken an upper-level
boundary** — because a null-company record is precisely a record that has opted out of the boundary.

**Disposition: `CRITICAL GAP`.** SMEsPlus must decide explicitly whether a null-scope record may exist
at all. Raised as `BOSS-DEC-04`. **This register's candidate position is that the behaviour must not
be inherited by default; the decision is Boss's and is open.**

### SS-F-10 — A shipped location is cross-company visible, cross-company editable, and valued by nobody (**CRITICAL**) — *found by challenge*
Three facts the package held separately compose into one it did not state:

1. The valuation predicate is *"has a company **and** is an internal or transit location"* — so a
   **company-less location is never valued, by construction**.
2. The domain **ships** an `Inter-company transit` location with **usage = transit** and an
   **explicitly empty company**. Its on-hand quantities inherit the location's company, so they are
   company-less too, and the null-company rule (`SS-F-01`) makes them visible to **every** company.
3. The physical-counting screen's domain is *internal or transit* — so those quantities appear on
   **every company's counting screen** and are editable there.

**Stock held in that location is therefore simultaneously visible to every company, editable from
every company's counting screen, and carried at value by no company.**

**Precisely bounded — the record ships archived.** It is inactive out of the box, so this is a
**latent** state, not an out-of-the-box one. It becomes live exactly when inter-company transfers are
enabled — which is the circumstance in which it matters. Two further shipped locations also carry an
empty company but have supplier/customer usage, so they are outside both the valuation predicate and
the counting screen.

**This is the clearest single argument in the Pilot for `BOSS-DEC-04`**, and it was not visible from
any single register.

### SS-F-11 — One valuation-bearing object is unisolated at every level (**CRITICAL**) — *found by challenge*
`OD-F-02` recorded 10 persistent objects with no company field as *ten undischarged dispositions*, and
hedged that *"at least one is a valuation-adjustment object where it is not obviously correct"*.

That hedge is now closable, and it closes as a **defect, not a disposition**: the valuation-adjustment
line object declares **no company field**, carries **no row-level rule**, and its **parent document
also carries no row-level rule** — the parent declares a required company but nothing filters on it.
**The chain is unisolated at every level.** `SS-F-02`'s framing of "isolation by association" is too
generous here: there is no association to be isolated by.

### SS-F-02 — WITHDRAWN AND REPLACED — 27.7%, not 46.8%, and the core movement objects **are** scoped

> **This register published, as its highest-severity structural finding, that 22 of 47 persistent
> objects (46.8%) carry no row-level isolation — naming the movement document, the movement, the
> movement line and the lot among them. That was wrong.** Each of those four carries a company-scoping
> rule in the target generation. The finding was produced by an extractor that could read only one of
> the two declaration forms the platform accepts, and it was falsified by independent challenge.

**Corrected census** — whole root, both declaration forms, re-derived independently by the producer
after the challenge named the defect:

| | published | corrected |
|---|---:|---:|
| rules on OWNED objects | 28 | **46** (29 in one form, **17 in the form the extractor could not read**) |
| company-scoping rules | 17 | **34** |
| distinct OWNED objects carrying a rule | 25 | **34** |
| persistent objects with **no** rule | 22 of 47 (46.8%) | **13 of 47 (27.7%)** |

The 13 that genuinely carry no rule are reference-data and forecast objects — **plus one that
matters**: the valuation-adjustment line (`SS-F-11`).

**The residual finding is real, but smaller and differently shaped.** 27.7% of persistent objects have
no row-level isolation, and whatever isolation they have is by association. **SMEsPlus still cannot
adopt isolation-by-association** — but the reference system is materially better isolated than this
register claimed, and a SMEsPlus design argued from the 46.8% figure would have been argued from a
false premise. `CRITICAL-GAP-02` is **re-stated at the corrected magnitude**, not withdrawn.

**Method lesson — the single most important instrument finding of the Pilot.** The defect was
invisible to the producer's own second-shape control, because **the producer's second instrument
shared the first one's accessor**. An independent challenger, writing from scratch, reproduced the
wrong number **exactly** and said so — then found the defect anyway. *An exact match between two
instruments that share a blind spot is corroboration of nothing.* Recorded as `CORR-F-27`.

### SS-F-03 — 10 persistent objects declare no company field
Carried from Register 05 `OD-F-02`. Each of the 10 needs an explicit disposition:
*reference data, correctly global* · *scoped by its parent* · *defect*. **None of the three may be
assumed.** Recorded as 10 undischarged dispositions, not as 10 defects.

### SS-F-04 — Delete is granted on one third of access rows
59 of 176 grants permit deletion. For a domain that carries quantity, ownership and valuation, which of
these deletions must be impossible in SMEsPlus — as opposed to merely restricted — is an
**immutability** decision. Raised as `BOSS-DEC-07`.

**This count is an upper bound, not the effective permission.** Code-level deletion guards override
grants: two were read in full and each refuses deletion of a completed document despite a grant that
permits it (Register 04 `FN-F-04`). **The effective delete surface is smaller than 59 by an unmeasured
amount.** Recorded as `GAP-INV-13`.

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
| Security | yes — 44 groups / **180** grants / **46** rules / 633 gated elements | population only | **NOT 100%** |
| Tenant Isolation | **no reference population exists** | — | **NOT APPLICABLE TO REFERENCE — SMEsPlus-original design required** |
| Company Isolation | yes — **34** scoping rules, **16** admitting null company (`SS-F-01`), 10 objects with no company field, **13** with no rule, 1 unisolated valuation chain (`SS-F-11`), 1 shipped cross-company location (`SS-F-10`) | population only | **NOT 100%** |
| Approval Control | yes — see `SS-F-09`; **no segregation-of-duties mechanism located** | 0 | **`GAP-INV-07`** |
| Audit Trail | yes (32 tracked fields) | population only | **NOT 100%** |
| Identity / Immutability | partial — 15 deletion guards located, **2 read in full** (`SR-09`); identity not opened | 2 objects | **NOT 100%** |
| Data Integrity | yes (32 constraints) | population only | **NOT 100%** |
| Stock Ownership / Quantity / Valuation | population only; valuation object changed generation (`OD-F-05`) | 0 | **`CRITICAL-GAP-01`** |
| Financial Posting / Cross-Module Financial Handoff | thin declared surface; code-created postings unmeasured (`XM-F-02`) | 0 | **`GAP-INV-06`** |
| Period Close | not opened | 0 | **NOT 100%** |
| Reversal | **established for 2 of 86 objects** — terminal by construction, no cancel / no reverse / deletion refused (`SR-09`) | 2 objects | **NOT 100%** |

**No Critical Area is at 100%. Under `VDR_COVERAGE_RULE.md` §6 this alone forces `HOLD`,
irrespective of any overall percentage.**

---

## Appendix A — Row-level rules on OWNED objects (**46**, both declaration forms)

| Learning ID | Record rule | Object | Declaration form | Restricted to groups | Domain | Module |
|---|---|---|---|---|---|---|
| LI-INV-RULE-0023 | Amazon Account multi-company | `amazon.account` | ref | GLOBAL (all users) | `['\|', ('company_id', '=', False), ('company_id', 'in', company_ids)]` | sale_amazon |
| LI-INV-RULE-0001 | Vehicles PE | `l10n_pe_edi.vehicle` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | l10n_pe_edi_stock |
| LI-INV-RULE-0024 | Lazada Shop multi-company | `lazada.shop` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | sale_lazada |
| LI-INV-RULE-0004 | mrp_bom multi-company | `mrp.bom` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | mrp |
| LI-INV-RULE-0011 | MRP BoMs Subcontractor | `mrp.bom` | ref | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.bom_ids.ids)]` | mrp_subcontracting |
| LI-INV-RULE-0002 | mrp_bom_byproduct multi-company | `mrp.bom.byproduct` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | mrp |
| LI-INV-RULE-0003 | mrp_bom_line multi-company | `mrp.bom.line` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | mrp |
| LI-INV-RULE-0010 | MRP BoM Lines Subcontractor | `mrp.bom.line` | ref | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.bom_ids.bom_line_ids.ids)]` | mrp_subcontracting |
| LI-INV-RULE-0005 | mrp_production multi-company | `mrp.production` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | mrp |
| LI-INV-RULE-0014 | MRP Productions Subcontractor | `mrp.production` | ref | [(4, ref('base.group_portal'))] | `[('subcontractor_id', '=', user.partner_id.commercial_partner_id.id)]` | mrp_subcontracting |
| LI-INV-RULE-0009 | MPS multi-company | `mrp.production.schedule` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | mrp_mps |
| LI-INV-RULE-0006 | mrp_routing_workcenter multi-company | `mrp.routing.workcenter` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | mrp |
| LI-INV-RULE-0007 | mrp_unbuild multi-company | `mrp.unbuild` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | mrp |
| LI-INV-RULE-0008 | mrp_workorder multi-company | `mrp.workorder` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | mrp |
| LI-INV-RULE-0021 | Point Of Sale Session | `pos.session` | ref | GLOBAL (all users) | `[('config_id.company_id', 'in', company_ids)]` | point_of_sale |
| LI-INV-RULE-0043 | Product Value multi-company | `product.value` | search | GLOBAL (all users) | `[('company_id','in', company_ids)]` | stock_account |
| LI-INV-RULE-0022 | repair order multi-company | `repair.order` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | repair |
| LI-INV-RULE-0028 | report_stock_quantity_flow multi-compa | `report.stock.quantity` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0025 | Shopee Shop multi-company | `shopee.shop` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | sale_shopee |
| LI-INV-RULE-0045 | stock_landed_cost multi-company | `stock.landed.cost` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock_landed_costs |
| LI-INV-RULE-0015 | Stock Locations Subcontractor | `stock.location` | ref | [(4, ref('base.group_portal'))] | `[ '\|', '\|', '\|', '\|', ('child_ids', 'in', user.partner_id.commercial_partner_id.picking_ids.location_id.id` | mrp_subcontracting |
| LI-INV-RULE-0029 | Location multi-company | `stock.location` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0016 | Stock Lot Subcontractor | `stock.lot` | ref | [(4, ref('base.group_portal'))] | `[ '\|', '\|', ('product_id', 'in', user.partner_id.commercial_partner_id.bom_ids.product_id.ids), ('product_id` | mrp_subcontracting |
| LI-INV-RULE-0036 | Stock Production Lot multi-company | `stock.lot` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0018 | Stock Moves Subcontractor | `stock.move` | ref | [(4, ref('base.group_portal'))] | `[ '\|', '\|', ('production_id.subcontractor_id', '=', user.partner_id.commercial_partner_id.id), ('move_orig_i` | mrp_subcontracting |
| LI-INV-RULE-0020 | Repair Line Subcontractor | `stock.move` | ref | [(4, ref('base.group_portal'))] | `[ '\|', '\|', ('product_id', 'in', user.partner_id.bom_ids.product_id.ids), ('product_id', 'in', user.partner_` | mrp_subcontracting_repair |
| LI-INV-RULE-0032 | stock_move multi-company | `stock.move` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0017 | Stock Move Lines Subcontractor | `stock.move.line` | ref | [(4, ref('base.group_portal'))] | `[ '\|', '\|', ('move_id.production_id.subcontractor_id', '=', user.partner_id.commercial_partner_id.id), ('mov` | mrp_subcontracting |
| LI-INV-RULE-0031 | stock_move_line multi-company | `stock.move.line` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0033 | stock_package multi-company | `stock.package` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0012 | Stock Pickings Subcontractor | `stock.picking` | ref | [(4, ref('base.group_portal'))] | `[('partner_id.commercial_partner_id', '=', user.partner_id.commercial_partner_id.id)]` | mrp_subcontracting |
| LI-INV-RULE-0026 | Portal Follower Transfers | `stock.picking` | ref | [(4, ref('base.group_portal'))] | `['\|', ('partner_id', '=', user.partner_id.id), ('sale_id.partner_id', '=', user.partner_id.id)]` | sale_stock |
| LI-INV-RULE-0034 | stock_picking multi-company | `stock.picking` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0046 | stock.picking.batch multi-company | `stock.picking.batch` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock_picking_batch |
| LI-INV-RULE-0013 | Stock Picking Types Subcontractor | `stock.picking.type` | ref | [(4, ref('base.group_portal'))] | `['\|', ('id', 'in', user.partner_id.commercial_partner_id.picking_ids.picking_type_id.ids), ('id', 'in', user.` | mrp_subcontracting |
| LI-INV-RULE-0035 | Stock Operation Type multi-company | `stock.picking.type` | search | GLOBAL (all users) | `[('company_id','in', company_ids)]` | stock |
| LI-INV-RULE-0037 | Stock Operation Type multi-company | `stock.putaway.rule` | search | GLOBAL (all users) | `[('company_id','in', company_ids)]` | stock |
| LI-INV-RULE-0038 | stock_quant multi-company | `stock.quant` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0044 | Stock Report multi-company | `stock.report` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock_enterprise |
| LI-INV-RULE-0030 | stock_route multi-company | `stock.route` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0027 | product_pulled_flow multi-company | `stock.rule` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0039 | stock_scrap_company multi-company | `stock.scrap` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0040 | stock_storage_category multi-company | `stock.storage.category` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids + [False])]` | stock |
| LI-INV-RULE-0019 | Warehouses Subcontractor | `stock.warehouse` | ref | [(4, ref('base.group_portal'))] | `[('id', 'in', user.partner_id.commercial_partner_id.picking_ids.picking_type_id.warehouse_id.ids)]` | mrp_subcontracting |
| LI-INV-RULE-0041 | Warehouse multi-company | `stock.warehouse` | ref | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |
| LI-INV-RULE-0042 | stock_warehouse.orderpoint multi-compa | `stock.warehouse.orderpoint` | search | GLOBAL (all users) | `[('company_id', 'in', company_ids)]` | stock |

## Appendix B — Object-level access grants, by object (78 objects, **180** rows)

| Object | Access grants | Groups granted create | Groups granted delete | Unrestricted (no group) |
|---|--:|---|---|--:|
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
| `stock.lot` | 3 | group_portal, group_stock_user | group_stock_user | 0 |
| `stock.move` | 13 | group_mrp_user, group_portal, group_pos_user, group_purchase_user, group_purchase_manager, group_sale_salesman, group_sale_manager, group_stock_manager, group_stock_user, group_account_invoice | group_mrp_user, group_pos_user, group_purchase_manager, group_sale_manager, group_stock_manager | 0 |
| `stock.move.line` | 5 | group_portal, group_stock_manager, group_stock_user, group_user | group_portal, group_stock_manager, group_stock_user, group_user | 0 |
| `stock.orderpoint.snooze` | 1 | group_stock_user | group_stock_user | 0 |
| `stock.package` | 3 | group_stock_manager, group_stock_user | group_stock_manager, group_stock_user | 0 |
| `stock.package.destination` | 1 | group_stock_user | — | 0 |
| `stock.package.history` | 1 | group_stock_user | — | 0 |
| `stock.package.type` | 3 | group_stock_manager | group_stock_manager | 0 |
| `stock.picking` | 13 | group_pos_user, group_purchase_user, group_purchase_manager, group_sale_salesman, group_sale_manager, group_stock_user, group_stock_manager, group_account_invoice | group_pos_user, group_purchase_user, group_purchase_manager, group_sale_manager, group_stock_user, group_stock_manager | 0 |
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
