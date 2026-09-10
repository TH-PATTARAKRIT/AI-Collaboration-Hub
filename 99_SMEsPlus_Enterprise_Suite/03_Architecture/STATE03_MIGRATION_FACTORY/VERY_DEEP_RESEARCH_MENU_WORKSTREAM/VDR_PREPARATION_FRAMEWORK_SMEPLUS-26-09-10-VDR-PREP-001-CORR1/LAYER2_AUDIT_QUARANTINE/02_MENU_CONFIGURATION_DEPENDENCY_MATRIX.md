# 02_MENU_CONFIGURATION_DEPENDENCY_MATRIX.md
# Register 02 — Configuration Dependency Matrix (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE** · Generation: **R1 (series-19)**

---

## 1. What this register measures

`MENU COVERAGE != FUNCTION COVERAGE.` This register measures the mechanism by which functionality
**appears and disappears** — the join between a configuration switch, the security group it activates,
and the concrete UI and rule elements that group controls.

| Clause | Declaration |
|--------|-------------|
| **POPULATION** | Every element in the Inventory domain carrying a visibility gate: any XML element **at any depth inside a view definition**, plus menu nodes and record rules |
| **PATTERN** | `groups` attribute on any element inside a view's arch; `groups` on menu nodes; `groups` on record rules; joined to `implied_group` on configuration-settings fields |
| **PATH SET** | R1, Inventory module set = 149 modules |
| **UNIT** | One gated element occurrence = one row of the join; one security group = one row of the matrix |
| **ELIGIBILITY** | 149/149 modules processed |

### Instrument defect found and repaired during the Pilot — **CORR-F-07**

The first instrument read `groups` only on `<button>` and `<field>` elements. That yielded **87**
gated elements across 14 groups.

The repaired instrument reads `groups` on **any element at any depth** inside a view arch. It yields
**633 gated elements across 43 groups**, distributed over **12 different element kinds**
(`field`, `button`, `div`, `filter`, `page`, `group`, `label`, `span`, `notebook`, `widget`, `t`, `p`).

> **The first instrument missed 86.3% of the configuration-dependent UI surface, and it returned a
> plausible, non-zero, internally consistent number while doing so.** No self-review would have caught
> it; it was caught by asking "can this predicate reach the thing it claims to count?"

---

## 2. The matrix

Occurrences: **650** (some elements carry more than one group). Distinct gated elements: **633**.

| Security group | Elements gated | Where (element kinds) | Activated by settings toggle |
|---|--:|---|---|
| `stock.group_stock_multi_locations` | 94 | field×60, filter×10, div×10, menu×5, span×4, button×2, group×1, page×1, p×1 | group_stock_multi_locations |
| `uom.group_uom` | 76 | field×72, div×3, menu×1 | **none — role/technical group** |
| `base.group_multi_company` | 65 | field×63, filter×2 | **none — role/technical group** |
| `stock.group_production_lot` | 65 | field×41, div×12, group×3, label×2, button×2, menux×2, filter×1, p×1, menu×1 | group_stock_production_lot |
| `base.group_no_one` | 50 | field×23, button×6, menu×6, menux×5, page×3, group×2, label×1, div×1, t×1, notebook×1, filter×1 | **none — role/technical group** |
| `stock.group_tracking_lot` | 50 | field×30, div×7, button×7, group×2, menu×2, filter×1, page×1 | group_stock_tracking_lot |
| `stock.group_stock_manager` | 25 | menu×15, button×5, field×3, menux×2 | **none — role/technical group** |
| `mrp.group_mrp_routings` | 23 | menux×9, field×7, page×3, button×3, filter×1 | group_mrp_routings |
| `stock.group_tracking_owner` | 22 | field×16, div×3, filter×1, p×1, menu×1 | group_stock_tracking_owner |
| `stock.group_stock_multi_warehouses` | 19 | field×14, filter×3, notebook×1, group×1 | **none — role/technical group** |
| `product.group_product_variant` | 17 | field×10, menux×5, menu×2 | **none — role/technical group** |
| `point_of_sale.group_pos_manager` | 14 | menux×14 | **none — role/technical group** |
| `stock.group_stock_user` | 13 | button×5, menu×5, menux×3 | **none — role/technical group** |
| `base.group_user` | 12 | button×11, menux×1 | **none — role/technical group** |
| `base.group_portal` | 11 | rule×11 | **none — role/technical group** |
| `quality.group_quality_user` | 10 | button×9, menux×1 | **none — role/technical group** |
| `stock.group_adv_location` | 9 | field×5, menu×2, notebook×1, group×1 | group_stock_adv_location |
| `mrp.group_mrp_manager` | 7 | menux×3, button×2, page×1, menu×1 | **none — role/technical group** |
| `stock.group_reception_report` | 7 | button×4, field×3 | group_stock_reception_report |
| `point_of_sale.group_pos_user` | 6 | menux×6 | **none — role/technical group** |
| `mrp.group_mrp_user` | 5 | button×2, menux×2, filter×1 | **none — role/technical group** |
| `project.group_project_user` | 5 | field×4, button×1 | **none — role/technical group** |
| `mrp.group_mrp_reception_report` | 4 | field×3, button×1 | group_mrp_reception_report |
| `mrp_plm.group_plm_user` | 4 | button×2, field×1, menux×1 | **none — role/technical group** |
| `quality.group_quality_manager` | 4 | menux×4 | **none — role/technical group** |
| `sales_team.group_sale_manager` | 4 | menux×3, button×1 | **none — role/technical group** |
| `account.group_account_readonly` | 3 | button×2, field×1 | **none — role/technical group** |
| `base.group_system` | 3 | menux×2, menu×1 | **none — role/technical group** |
| `mrp_workorder.group_mrp_wo_shop_floor` | 3 | button×2, menux×1 | group_mrp_wo_shop_floor |
| `stock.group_stock_sign_delivery` | 3 | widget×2, field×1 | group_stock_sign_delivery |
| `mrp.group_mrp_byproducts` | 2 | page×2 | group_mrp_byproducts |
| `mrp.group_mrp_workorder_dependencies` | 2 | field×2 | group_mrp_workorder_dependencies |
| `mrp_plm.group_plm_manager` | 2 | menux×2 | **none — role/technical group** |
| `purchase.group_purchase_user` | 2 | button×2 | **none — role/technical group** |
| `account.group_account_user` | 1 | button×1 | **none — role/technical group** |
| `analytic.group_analytic_accounting` | 1 | field×1 | **none — role/technical group** |
| `helpdesk.group_helpdesk_user` | 1 | button×1 | **none — role/technical group** |
| `maintenance.group_equipment_manager` | 1 | menux×1 | **none — role/technical group** |
| `mrp_workorder.group_mrp_wo_tablet_timer` | 1 | span×1 | group_mrp_wo_tablet_timer |
| `point_of_sale.group_pos_preset` | 1 | menux×1 | group_pos_preset |
| `product.group_product_pricelist` | 1 | menux×1 | **none — role/technical group** |
| `sales_team.group_sale_salesman` | 1 | button×1 | **none — role/technical group** |
| `website.group_multi_website` | 1 | field×1 | **none — role/technical group** |
| `mrp.group_unlocked_by_default` | 0 | — | group_unlocked_by_default |
| `product_expiry.group_expiry_date_on_delivery_slip` | 0 | — | group_expiry_date_on_delivery_slip |
| `sale_stock_renting.group_rental_stock_picking` | 0 | — | group_rental_stock_picking |
| `stock.group_lot_on_delivery_slip` | 0 | — | group_lot_on_delivery_slip |
| `stock.group_stock_lot_print_gs1` | 0 | — | group_stock_lot_print_gs1 |
| `stock.group_warning_stock` | 0 | — | group_warning_stock |
| `stock_account.group_lot_on_invoice` | 0 | — | group_lot_on_invoice |
---

## 3. Findings

### CD-F-01 — Only 14 of 43 gating groups are reachable from a configuration screen (**CRITICAL**)
**29 of the 43 groups that control what an Inventory user can see are role or technical groups with
no settings toggle at all.** Visibility is therefore governed by two independent mechanisms —
*configuration* and *role assignment* — and only one of them is visible on a settings page.

A design that models "feature on/off" as a single configuration axis will be wrong for 67.4% of the
gating surface.

### CD-F-02 — The largest single gate is a configuration toggle, not a role
One toggle (multi-location) alone controls **94 elements across 9 element kinds**, including 5 menu
nodes. Turning one switch changes the Inventory application's shape more than any role does.

### CD-F-03 — RESOLVED — 7 toggles take effect outside the screen-element surface entirely (**CRITICAL for method**)
Seven group-toggles activate groups that gate **no** screen element. A system-wide trace of every
non-test reference to each group resolves all seven, and **none of them is inert**:

| Effect surface | Toggles | What that means |
|----------------|--------:|-----------------|
| **Printed / report templates** — lot barcode label, delivery slip, customer invoice, country delivery guide | **4** | the toggle changes what is **printed**, not what is on screen |
| **Runtime code tests** — a code branch asks at run time whether the user holds the group | **3** | the toggle changes **behaviour**, with no declarative trace anywhere |
| | **7** | |

One of the three runtime-code toggles **additionally** gates an element on the **partner** view — a
boundary object, outside the owned set and therefore outside this register's element census. That is a
second surface for an already-counted toggle, not an eighth toggle.

**Method consequence:** a configuration-dependency register whose population is *screen elements* is
structurally incapable of seeing 7 of 21 group-toggles. **Printed output and runtime code are effect
surfaces in their own right and had no place in the original nine-register design.**
Recorded as framework correction `CORR-F-21`; resolution evidence at
`INVENTORY_PILOT_SOURCE_RESOLUTION_REPORT.md` `SR-08`.

**The first draft of this finding said the effect was "expressed somewhere other than element-level
gating" and left it open. That sentence was true, unfalsifiable and useless.** Resolving it took one
targeted trace and changed a `SOURCE RESOLUTION REQUIRED` into a framework correction.

### CD-F-04 — Gating is invisible at the register level for whole classes of element
Access-control grants (176), actions (200), views (492 at record level), constraints (32),
scheduled jobs (26) and behavioural overrides (614) carry **no** element-level gate. Their conditional
behaviour, where it exists, is entirely in code. **Any claim that "configuration coverage is complete"
based on element gating alone is false by construction for 1,540 of 4,339 Learning Items.**

### CD-F-05 — Cross-domain groups gate Inventory surface
Groups owned by the accounting, sales, purchase, project, helpdesk, quality, manufacturing,
point-of-sale, website and analytic domains all gate Inventory elements. **The Inventory application's
visible shape is partly owned by other domains' security models.** For a multi-tenant product this is
a boundary question, not a convenience.

### CD-F-06 — A settings screen writes to another object 138 times out of 237
The dominant toggle class stores its value on a *different* object (company, warehouse, product,
product category). The screen that appears to hold the setting does not hold the state.
**The audit trail, the company scoping and the change control of a setting therefore belong to the
object that stores it, not to the screen.** This is a design-relevant asymmetry, recorded here and
carried into Register 07.

---

## 4. Coverage state

| Dimension | Population | Verified (`S3`) | Coverage |
|-----------|-----------:|----------------:|---------:|
| Gate → element join | 633 elements / 43 groups | 633 / 43 | **100% of the mechanism** |
| Toggle → gate join | 21 group-toggles | 14 joined at element level + 7 resolved to non-element surfaces | **100%** |
| Conditional behaviour expressed in code | not enumerated | 0 | **0% — declared gap** |

The third row is the honest limit of this register. It is carried into the coverage dashboard as a
declared blind spot with its size stated, not as a footnote.
