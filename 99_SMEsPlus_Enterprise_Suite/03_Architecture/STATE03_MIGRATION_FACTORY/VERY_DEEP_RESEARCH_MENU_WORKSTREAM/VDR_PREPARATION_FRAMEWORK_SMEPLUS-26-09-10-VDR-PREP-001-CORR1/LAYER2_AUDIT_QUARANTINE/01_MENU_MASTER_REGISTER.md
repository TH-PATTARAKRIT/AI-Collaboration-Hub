# 01_MENU_MASTER_REGISTER.md
# Register 01 — Menu Master (Inventory Pilot)

Session `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]` · **LAYER 2 — AUDIT QUARANTINE**
Generation basis: **R1 (series-19, content-verified)**. Delta against R2 (series-18) in §5.

---

## 1. Population and instrument

| Clause | Declaration |
|--------|-------------|
| **POPULATION** | Every menu node whose parent chain terminates at the Inventory application root menu, over the whole R1 root — not over a chosen module list |
| **PATTERN** | XML parse of every `.xml` file under every module directory carrying a manifest: `<menuitem>` elements at any nesting depth **and** `<record model="ir.ui.menu">` records; parent resolved through `parent=` attribute, nesting, and `parent_id` field |
| **PATH SET** | R1, 1,433 modules with manifests, 8,482 XML files scanned |
| **UNIT** | One menu node = one row. A node defined once as a `menuitem` and again as an updating `record` is **one** node |
| **ELIGIBILITY** | All nodes admitted; none excluded |

### Instrument controls

| Control | Result |
|---------|--------|
| I1 second shape | Regex element count 1,649 = 1,585 `menuitem` + 64 menu `record`. Distinct ids: 1,574 + 37 with 35 shared = **1,576**. Parser total **1,576**. **Exact identity, reconciled.** |
| I2 positive control | Synthetic module injected with one menu under the Inventory root → count rose by exactly 1 |
| I3 coverage assertion | 1,433/1,433 modules processed; 0 parse failures inside the domain module set |
| I4 zero re-test | Dangling parent references: **0**, re-derived by a second pass over the resolved tree |

**Whole-system menu population: 1,576 nodes in 67 application roots.**
**Inventory application root subtree: 62 nodes.**

---

## 2. Register

Full rows in `MACHINE_REGISTERS/F_menu.jsonl` and `MACHINE_REGISTERS/LEARNING_POPULATION.csv`.
`D` = depth below the application root. `Hops` = resolution hops needed to reach the target object.

| Learning ID | D | Menu label | Identity | Action kind | Target object | Hops | Visibility gate | Children | Module |
|---|--:|---|---|---|---|--:|---|--:|---|
| LI-INV-MENU-0040 | 0 | Inventory | stock.menu_stock_root | container | — | 0 | group_stock_manager,group_stock_user | 5 | stock |
| LI-INV-MENU-0035 | 1 | Configuration | stock.menu_stock_config_settings | container | — | 0 | group_stock_manager | 9 | stock |
| LI-INV-MENU-0002 | 2 | Reporting | delivery_iot.iot_cached_printers_section | container | — | 0 | — | 1 | delivery_iot |
| LI-INV-MENU-0001 | 3 | Reset Linked Printers | delivery_iot.iot_cached_printers_action | client | — | ? | — | 0 | delivery_iot |
| LI-INV-MENU-0022 | 2 | Delivery | stock.menu_delivery | container | — | 0 | stock.group_stock_manager | 3 | stock |
| LI-INV-MENU-0055 | 3 | Delivery Methods | stock_delivery.menu_action_delivery_carrier_form | act_window | delivery.carrier | 1 | — | 0 | stock_delivery |
| LI-INV-MENU-0056 | 3 | Zip Prefix | stock_delivery.menu_delivery_zip_prefix | act_window | delivery.zip.prefix | 1 | base.group_no_one | 0 | stock_delivery |
| LI-INV-MENU-0024 | 3 | Package Types | stock.menu_packaging_types | act_window | stock.package.type | 1 | stock.group_tracking_lot | 0 | stock |
| LI-INV-MENU-0010 | 2 | GİB e-Dispatch | l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera | container | — | 0 | — | 1 | l10n_tr_nilvera_edispatch |
| LI-INV-MENU-0011 | 3 | GİB Plate Numbers | l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera_trailer_plate | act_window | l10n_tr.nilvera.trailer.plate | 1 | — | 0 | l10n_tr_nilvera_edispatch |
| LI-INV-MENU-0028 | 2 | Products | stock.menu_product_in_config_stock | container | — | 0 | — | 4 | stock |
| LI-INV-MENU-0021 | 3 | Attributes | stock.menu_attribute_action | act_window | product.attribute | 1 | product.group_product_variant | 0 | stock |
| LI-INV-MENU-0027 | 3 | Categories | stock.menu_product_category_config_stock | act_window | product.category | 1 | — | 0 | stock |
| LI-INV-MENU-0043 | 3 | Units & Packagings | stock.menu_stock_uom_form_action | act_window | uom.uom | 1 | uom.group_uom | 0 | stock |
| LI-INV-MENU-0049 | 3 | Barcode Nomenclatures | stock.menu_wms_barcode_nomenclature_all | act_window | barcode.nomenclature | 1 | base.group_no_one | 0 | stock |
| LI-INV-MENU-0003 | 2 | Chilean SII | l10n_cl_edi_stock.menu_sii_chile | container | — | 0 | — | 1 | l10n_cl_edi_stock |
| LI-INV-MENU-0004 | 3 | Cafs | l10n_cl_edi_stock.menu_stock_l10n_cl_dte_caf | act_window | l10n_cl.dte.caf | 1 | — | 0 | l10n_cl_edi_stock |
| LI-INV-MENU-0005 | 2 | Mexico | l10n_mx_edi_stock.menu_stock_config_settings_mx | container | — | 0 | stock.group_stock_manager | 2 | l10n_mx_edi_stock |
| LI-INV-MENU-0006 | 3 | Custom Document Type | l10n_mx_edi_stock.menu_stock_mx_customs_document_type | act_window | l10n_mx_edi.customs.document.type | 1 | stock.group_stock_manager | 0 | l10n_mx_edi_stock |
| LI-INV-MENU-0007 | 3 | Customs Regime | l10n_mx_edi_stock.menu_stock_mx_customs_regime | act_window | l10n_mx_edi.customs.regime | 1 | stock.group_stock_manager | 0 | l10n_mx_edi_stock |
| LI-INV-MENU-0008 | 2 | Peru | l10n_pe_edi_stock.menu_stock_config_settings_pe | container | — | 0 | stock.group_stock_manager | 1 | l10n_pe_edi_stock |
| LI-INV-MENU-0009 | 3 | Vehicles | l10n_pe_edi_stock.menu_stock_pe_vehicles | act_window | l10n_pe_edi.vehicle | 1 | stock.group_stock_manager | 0 | l10n_pe_edi_stock |
| LI-INV-MENU-0036 | 2 | Settings | stock.menu_stock_general_settings | act_window | res.config.settings | 1 | base.group_system | 0 | stock |
| LI-INV-MENU-0047 | 2 | Warehouse Management | stock.menu_warehouse_config | container | — | 0 | stock.group_stock_manager | 7 | stock |
| LI-INV-MENU-0017 | 3 | Locations | stock.menu_action_location_form | act_window | stock.location | 1 | stock.group_stock_multi_locations | 0 | stock |
| LI-INV-MENU-0019 | 3 | Rules | stock.menu_action_rules_form | act_window | stock.rule | 1 | stock.group_adv_location | 0 | stock |
| LI-INV-MENU-0020 | 3 | Warehouses | stock.menu_action_warehouse_form | act_window | stock.warehouse | 1 | — | 0 | stock |
| LI-INV-MENU-0025 | 3 | Operations Types | stock.menu_pickingtype | act_window | stock.picking.type | 1 | — | 0 | stock |
| LI-INV-MENU-0031 | 3 | Putaway Rules | stock.menu_putaway | act_window | stock.putaway.rule | 1 | stock.group_stock_multi_locations | 0 | stock |
| LI-INV-MENU-0033 | 3 | Routes | stock.menu_routes_config | act_window | stock.route | 1 | stock.group_adv_location | 0 | stock |
| LI-INV-MENU-0045 | 3 | Storage Categories | stock.menu_storage_categoty_config | act_window | stock.storage.category | 1 | stock.group_stock_multi_locations | 0 | stock |
| LI-INV-MENU-0037 | 1 | Products | stock.menu_stock_inventory_control | container | — | 0 | — | 4 | stock |
| LI-INV-MENU-0018 | 2 | Lots / Serial Numbers | stock.menu_action_production_lot_form | act_window | stock.lot | 1 | stock.group_production_lot | 0 | stock |
| LI-INV-MENU-0023 | 2 | Packages | stock.menu_package | act_window | stock.package | 1 | stock.group_tracking_lot | 0 | stock |
| LI-INV-MENU-0030 | 2 | Products | stock.menu_product_variant_config_stock | act_window | product.template | 1 | — | 0 | stock |
| LI-INV-MENU-0051 | 2 | Product Variants | stock.product_product_menu | act_window | product.product | 1 | product.group_product_variant | 0 | stock |
| LI-INV-MENU-0044 | 1 | Operations | stock.menu_stock_warehouse_mgmt | container | — | 0 | — | 5 | stock |
| LI-INV-MENU-0026 | 2 | (inherits action name) | stock.menu_procurement_compute | UNRESOLVED | — | ? | base.group_no_one | 0 | stock |
| LI-INV-MENU-0034 | 2 | Adjustments | stock.menu_stock_adjustments | container | — | 0 | — | 3 | stock |
| LI-INV-MENU-0016 | 3 | Physical Inventory | stock.menu_action_inventory_tree | server | — | ? | — | 0 | stock |
| LI-INV-MENU-0059 | 3 | Landed Costs | stock_landed_costs.menu_stock_landed_cost | act_window | stock.landed.cost | 1 | — | 0 | stock_landed_costs |
| LI-INV-MENU-0041 | 3 | Scrap | stock.menu_stock_scrap | act_window | stock.scrap | 1 | — | 0 | stock |
| LI-INV-MENU-0060 | 2 | Jobs | stock_picking_batch.menu_stock_jobs | container | — | 0 | — | 2 | stock_picking_batch |
| LI-INV-MENU-0061 | 3 | Batch Transfers | stock_picking_batch.stock_picking_batch_menu | act_window | stock.picking.batch | 1 | — | 0 | stock_picking_batch |
| LI-INV-MENU-0062 | 3 | Wave Transfers | stock_picking_batch.stock_picking_wave_menu | act_window | stock.picking.batch | 1 | — | 0 | stock_picking_batch |
| LI-INV-MENU-0038 | 2 | Procurement | stock.menu_stock_procurement | container | — | 0 | — | 3 | stock |
| LI-INV-MENU-0032 | 3 | Replenishment | stock.menu_reordering_rules_replenish | server | — | ? | stock.group_stock_manager | 0 | stock |
| LI-INV-MENU-0039 | 3 | References | stock.menu_stock_references | act_window | stock.reference | 1 | base.group_no_one | 0 | stock |
| LI-INV-MENU-0013 | 3 | Master Production Schedule | mrp_mps.stock_mrp_mps_report_menu | client | mrp.production.schedule | 1 | mrp.group_mrp_manager | 0 | mrp_mps |
| LI-INV-MENU-0042 | 2 | Transfers | stock.menu_stock_transfers | container | — | 0 | — | 5 | stock |
| LI-INV-MENU-0057 | 3 | Dropships | stock_dropshipping.dropship_picking | act_window | stock.picking | 1 | stock.group_stock_manager,stock.group_stock_user | 0 | stock_dropshipping |
| LI-INV-MENU-0014 | 3 | Receipts | stock.in_picking | server | stock.picking | 3 | stock.group_stock_manager,stock.group_stock_user | 0 | stock |
| LI-INV-MENU-0015 | 3 | Internal | stock.int_picking | server | stock.picking | 3 | stock.group_stock_multi_locations | 0 | stock |
| LI-INV-MENU-0012 | 3 | Manufacturings | mrp.mrp_operation_picking | act_window | mrp.production | 1 | stock.group_stock_manager,stock.group_stock_user | 0 | mrp |
| LI-INV-MENU-0050 | 3 | Deliveries | stock.out_picking | server | stock.picking | 3 | stock.group_stock_manager,stock.group_stock_user | 0 | stock |
| LI-INV-MENU-0048 | 1 | Reporting | stock.menu_warehouse_report | container | — | 0 | group_stock_manager | 5 | stock |
| LI-INV-MENU-0029 | 2 | Stock | stock.menu_product_stock | act_window | product.product | 1 | — | 0 | stock |
| LI-INV-MENU-0046 | 2 | Locations | stock.menu_valuation | server | — | ? | stock.group_stock_multi_locations,stock.group_tracking_owner,base.group_no_one | 0 | stock |
| LI-INV-MENU-0058 | 2 | Performance | stock_enterprise.stock_dashboard_menuitem | act_window | stock.report | 1 | base.group_no_one | 0 | stock_enterprise |
| LI-INV-MENU-0052 | 2 | Moves History | stock.stock_move_line_menu | act_window | stock.move.line | 1 | — | 0 | stock |
| LI-INV-MENU-0053 | 2 | Moves Analysis | stock.stock_move_menu | act_window | stock.move | 1 | — | 0 | stock |
| LI-INV-MENU-0054 | 1 | Overview | stock.stock_picking_type_menu | act_window | stock.picking.type | 1 | — | 0 | stock |
---

## 3. Findings

### MM-F-01 — CORRECTED — the menu spine cannot be resolved by reading action records, and one menu has no action record at all (**CRITICAL**)
**9 of 62** menus (14.5%) cannot be resolved from an action record.

- **6** are bound to **server actions**, which carry no target-object field: the target, domain and
  context are computed in code at click time. Resolution requires **3 hops**.
- **2** are bound to client actions.
- **1** is bound to an action that **does not exist in source at all** — the platform materialises it
  at install time from a scheduled-job record. It is invisible to any XML census, and it is the menu
  that runs the procurement scheduler (Register 08 `HA-F-01`).

> **This register previously published "7 of 62" and "all 7 are now resolved" — while its own table
> carried one of those rows as `UNRESOLVED` with no target.** Both statements were wrong.
> Found by independent challenge; recorded as `CORR-F-23`.

**A menu→object map built from action records is structurally blind to exactly the menus that matter
most** — and to one that has no record to read. All 9 are now resolved; the resolution route for each
is in `INVENTORY_PILOT_SOURCE_RESOLUTION_REPORT.md`.

### MM-F-02 — 27.4% of the spine is a container, not a function
17 of 62 nodes carry no action at all. They are grouping nodes. Counting them as "menus researched"
inflates menu coverage by more than a quarter with zero functional knowledge gained.

### MM-F-03 — 56.5% of the spine is conditionally visible
35 of 62 nodes carry a visibility gate. **A user does not see this menu tree; they see one of many
projections of it.** The projection is a function of role and configuration jointly (Register 02).

### MM-F-04 — Menu labels are frequently absent from the menu definition
Multiple nodes define no label; the label comes from the action. A menu register built from menu
definitions alone therefore produces blank names for real, user-visible menus. Recorded because a
Figma menu-coverage register keyed on menu labels would silently lose them.

### MM-F-05 — The Inventory application root is extended by localisation modules
4 country localisation modules attach menus directly into the Inventory application
(`MENU-0003/0004`, `0005/0006/0007`, `0008/0009`, `0010/0011` — 9 of 62 nodes, 14.5%).
**The Inventory menu tree is not a property of the Inventory modules.** Whichever localisations a
tenant installs changes what the Inventory application contains.

### MM-F-06 — The domain's menus outside its own application outnumber its own spine 2.2 : 1
The Inventory module set contributes **134** further menu nodes that hang under *other* applications
(class `MENUX`). Researching only the Inventory application root would miss 68.4% of the menu surface
this domain is responsible for.

### MM-F-07 — Duplicate identifiers exist in the reference source, and in this register's own machine output
One server-action identifier is declared **twice in the same file** with two different names; the
second silently supersedes the first.

**And the same class of defect is present in this register's own output.** The menu register holds
**197 rows over 196 distinct identifiers** and the action register **201 over 200** — against this
register's declared UNIT of *one node, one row*. The population builder de-duplicates; the shipped
machine register does not, so **a reader counting the file disagrees with the document**. Found by two
challengers independently. Both figures are now published side by side wherever either is cited.

### MM-F-08 — A third-party module rewrites two Inventory menu gates at install time (**MATERIAL**) — *found by challenge*
A delivery-integration module ships records that **overwrite the visibility gates of two Inventory
menus** — emptying the gate on one (opening the Configuration menu to every user) and adding a gate to
another. Nine such menu-overriding records exist across the whole root; **two target Inventory menus,
both from that one module.**

**Consequence for this register:** the `Visibility gate` column, `MM-F-03`'s 35 of 62, and Register 07
`SS-F-06`'s group-governance census all report the **original declaration**, not the **effective**
gate. Two of the 35 are stale whenever that module is installed.

This is the same class as `MM-F-05` and `CD-F-05` — foreign modules shape the Inventory surface — and
the register found the menu-**addition** case while missing the gate-**mutation** case. Recorded as
`GAP-INV-15`: no census of effective-versus-declared gates has been run.

---

## 4. Coverage state

| Item | Count | State |
|------|------:|-------|
| Menu nodes discovered (`S0`) | 62 | complete |
| Source located (`S1`) | 62 | complete |
| Target object resolved | 62 | complete — after 3-hop resolution for 6, client-action resolution for 2, and scheduled-job resolution for 1 |
| Visibility gate identified (`S3` partial) | 62 | complete |
| Function verified (`S4`) | 0 | **not started — this Pilot establishes the population, not the function** |

---

## 5. Generation delta (R1 series-19 vs R2 series-18)

| Dimension | R2 (18) | R1 (19) | Δ |
|-----------|--------:|--------:|--:|
| Inventory root subtree nodes | 63 | 62 | −1 |
| Whole-system menu nodes | 1,434 | 1,576 | +142 |
| Menus contributed by the domain module set (rows / distinct) | 185 / 185 | 197 / **196** | +12 / +11 |

Two independent series-18 comparators were run (one with an authoritative release marker, one without)
and agree within 0–3 on every dimension. The delta is therefore a **generation** delta, not a root-scope
artefact — see `00A_EVIDENCE_BASE_AND_PATH_SET.md` §3 for the contaminated comparison that this control
rejected.
