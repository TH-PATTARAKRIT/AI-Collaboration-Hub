# 00D_PRIOR_RESEARCH_RECONCILIATION_MATRIX.md
# Workstream D — Prior Research Reconciliation Matrix (Inventory)

Session `[SMEPLUS-26-09-10-VDR-PREP-002]` · Owner: **LESA + VDR Team**
**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Prior corpus — declared, not described

| Attribute | Value |
|-----------|-------|
| Prior execution | `[SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]` |
| Branch | `audit/inventory-deep-research-r4-l12-2026-09-04-001` |
| Corpus | 26 files, **5,193 lines**, registers `L1`–`L12` plus coverage, object-impact, handoff, valuation-dependency, escalation, risk, PMO and closure |
| Prior menu scope | **29 menus**, `INV-M01`–`INV-M29` |
| Prior function scope | **41 functions**, `INV-F-01`–`INV-F-41` |
| Prior status | *"29 of 29 menus traced through L1–L12, 0 deferred"* |
| Adjacent corpus also read | MTI ruling-conformance execution, 14 files |

**The prior work is genuine and substantial. Nothing below withdraws it.** What is reconciled is its
**scope** against a derived population, and its **dimensions** against the three the current standard
requires.

---

## 2. Scope reconciliation — 29 prior menus against 62 derived nodes

| | Count |
|---|---:|
| Prior R4 menus | 29 |
| Current derived menu nodes | **62** |
| Current nodes that map to a prior menu | **29** — corrected from 32; three mapped nodes are grouping containers |
| Current nodes with **no** prior coverage | **30** |
| — of which grouping containers (no function) | **17** — corrected from 14 |
| — of which **action-bearing and never in prior scope** | **16** |
| — of those 16, **live on an observed deployment** | **10** |
| Prior menus with no current counterpart | **3** — corrected from 1: the valuation report, the product-packaging master and the unit-of-measure **category** master. The latter two study objects that do not exist in the target generation |

### The ten live, action-bearing menus prior research never covered

| Menu | What it is | Why it matters |
|------|-----------|----------------|
| **Batch transfers** | grouped picking execution | named explicitly in the commissioning prompt's own Inventory scope list |
| **Wave transfers** | wave picking execution | same |
| **Packages** | package-level stock handling | same |
| **Operation-type Overview** | the operational dashboard — the default landing surface | the most-used screen in the application |
| **Manufacturing orders (inside Inventory)** | production orders displayed in the Inventory application | the one true cross-module co-owner (`00B` `FO-F-03`) |
| **Master Production Schedule** | forward production planning | named in the prompt's scope list |
| **Stock references** | reference/identity surface | identity is a Critical Area |
| **Delivery carriers** · **Delivery postcode prefixes** | shipping method configuration | changes delivery workflow |
| **Reset linked printers** | device management | a *reset* action inside Inventory |

**`INV-M14` — the valuation report menu — has no counterpart in the target generation.** That is not a
mapping failure; it is the generation change. See §5.

---

## 3. Dimension reconciliation — measured, with positive controls

The current standard requires **PROCESS + CONFIGURATION + OPTIONAL FUNCTION** before any function may
be called research-complete. The prior corpus was measured for each.

| Dimension | Occurrences | Files (of 26) | Positive control | Control fires? |
|-----------|------------:|--------------:|------------------|:--------------:|
| PROCESS | 278 | 22 | *trigger* — 57 | **yes** |
| CONFIGURATION | 363 | 24 | *configuration* — 148 | **yes** |
| **OPTIONAL FUNCTION** | **0** | **0** | *toggle* — **0** | **n/a — the word never appears** |
| RUNTIME REACHABILITY | 21 | 10 | *installed* — **0** | **no** |
| INPUT | 74 | 18 | *input* — 62 | yes |
| OUTPUT | 232 | 22 | *output* — 113 | yes |

### RC-F-01 — **WITHDRAWN. THE ZERO WAS A TERM-LIST ARTEFACT.** (**CRITICAL RETRACTION**)

> **Published:** *"Zero occurrences, across 5,193 lines… None of that surface exists in the prior
> research at all."* **This was false, and it was the premise of this register's headline.**

The prior corpus discusses optional functions continuously — **in its own vocabulary, which the
measurement's term list did not contain.** It calls them **capability switches**.

| Term | Occurrences | Files (of 26) |
|---|---:|---:|
| *capability* | **56** | **17** |
| *optional* | 48 | 11 |
| *conditional* | 25 | 12 |
| *capability switch* | 6 | 3 |
| *visible only* · *Hidden unless* · *switched off* | 16 | 3 |

It contains a **dedicated function** — *"Change a capability switch"* — with all eight process
dimensions filled, including *"State transition: capability on ↔ off"*, *"Quantity impact: enabling
traceability where untracked stock already exists leaves balances with no batch identity"* and
*"Cost impact: enabling or disabling valuation changes whether value events are produced at all"*.
It contains a **dedicated menu study of the switch panel** — *"Required fields: none; it is a switch
panel"*, *"Optional fields: every capability switch"*, *"Visibility rules: switches reveal dependent
switches; some cannot be turned off once data exists"* — rated **configuration risk HIGH**, with a
named open gap against it.

**The prior corpus's optional-function coverage is better than this session's own delta produced.**

**Cause — this framework's own catalogued defect, committed by its author.** The measurement searched
for the *current* vocabulary. **The positive control was the word `toggle`, drawn from the same wrong
vocabulary, so it could not fire — and its silence was read as confirmation instead of as the warning
it was.** Recorded as `CORR-F-37`: *a positive control drawn from the same vocabulary as the search
term tests nothing; it must be drawn from the corpus being searched.*

**Withdrawn with it:** `GAP-INV-19`, the `COMPLETE = 0` headline, and the stated delta on all
`PARTIAL` rows.

### RC-F-02 — The prior corpus has no runtime dimension, and could not have had one
21 weak hits and a **zero positive control**. Prior research is a source study throughout. This is not
a criticism — no runtime evidence base had been established at the time — but it means **every prior
conclusion carries the same `UNMEASURED` reachability bound the current Pilot carried until this
session**.

### RC-F-03 — Boss's premise about prior emphasis is **refined, not simply confirmed**
The commissioning prompt states that prior research emphasised INPUT and OUTPUT over PROCESS.
**Measured: OUTPUT 232 against INPUT 74 — output emphasis is 3.1×, so the input/output asymmetry is
real and larger than stated.** But **PROCESS 278 and CONFIGURATION 363 both exceed OUTPUT.**

> **The prior corpus is not process-thin.** Its L3 register alone carries 230 process-signal
> occurrences across eight declared dimensions per function — trigger, preconditions, postconditions,
> state transition, quantity impact, cost impact, output, audit evidence.
> **The real gaps are optional function (zero) and runtime reachability (zero), not process.**

Stating this plainly matters: a delta programme aimed at "process internals" would be aimed at the one
dimension prior research actually covered well.

---

## 4. Reconciliation status roll-up

| Status | Menus | Meaning |
|--------|------:|---------|
| `PARTIAL` | **29** | prior L1–L12 coverage exists **including the optional dimension**; the **runtime** dimension is absent |
| `MISSING` | **16** | action-bearing, never in prior scope — **10 of them live** |
| `NOT APPLICABLE` | **17** | grouping containers, no function |
| `COMPLETE` | **NOT DETERMINABLE** | the register carries **one ordinal status per row** and cannot represent three independent dimensions. The previous `0` was true of every possible content of the file — `CORR-F-38` |
| `OUTDATED` | **3** | see §2 |
| `CONTRADICTED` | **0** | no prior conclusion is contradicted by current evidence |
| `UNVERIFIED` | see §5 | the valuation conclusions |

**The `COMPLETE = 0` headline is withdrawn on two independent grounds.** Its premise was false
(`RC-F-01`), and it was **unfalsifiable by construction**: a register with one ordinal status per row
cannot record an item satisfying three dimensions, so the zero was a property of the schema, not an
observation about the domain.

**What replaces it:** the prior corpus covers process, configuration **and** optional function for the
29 menus in its scope. What it does not cover is **runtime reachability** — a dimension that did not
exist as a control when it was written, and which this session has now measured.

---

## 5. Valuation / COGS prior conclusions — §17 classification

Prior conclusions are **preserved as audit lineage** and **not silently replaced**.

| Prior conclusion | Classification | Evidence |
|------------------|----------------|----------|
| `P-07` — *Inventory emits facts; Accounting decides postings* | **VALID** | independently corroborated by `00B` `FO-F-05`: the 7 Inventory objects carrying financial fields carry values and account references, not posting decisions |
| `P-02` / `IV-05` — a completed movement fact is immutable; corrections are new reversing facts | **VALID** | corroborated by `SR-09`: the write-off and teardown documents are terminal by construction — no cancel state, no reverse method, deletion refused once complete |
| 19 menus carry a `DEPENDENCY: ACCOUNTING COGS GAP` lock, `JT-01`…`JT-12` | **PARTIAL** | the dependency is real and unchanged; **the object it was reasoned about has been replaced** — see the next row |
| The valuation ledger is the per-movement valuation record | **SUPERSEDED** | the object has **0 declarations** in the target generation, and on a real series-19 deployment its table **does not exist**. Its replacement holds 85,832 rows of which **0 carry a movement reference** |
| `INV-M14` — the valuation report menu | **OUTDATED** | no counterpart in the target generation |
| Conclusions derived from per-movement valuation-layer behaviour | **UNVERIFIED in the target generation** | they were true of series 18; no evidence establishes them for series 19 |

**No prior valuation conclusion is marked CONTRADICTED.** They were correct for the generation they
were derived from. The correct disposition is `SUPERSEDED` / `UNVERIFIED`, and `BOSS-DEC-01` decides
whether re-derivation is required before they may support a SMEsPlus design.

---

## 6. Matrix

| Learning ID | Menu identity | Label | Prior R4 coverage | Runtime | Prior PROCESS | Prior CONFIG | Prior OPTIONAL | Reconciliation status | Required delta |
|---|---|---|---|---|:--:|:--:|:--:|---|---|
| LI-INV-MENU-0001 | `delivery_iot.iot_cached_printers_action` | Reset Linked Printers | — | LIVE 1of2 | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0002 | `delivery_iot.iot_cached_printers_section` | Reporting | — | LIVE 1of2 | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0003 | `l10n_cl_edi_stock.menu_sii_chile` | Chilean SII | — | not installed | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0004 | `l10n_cl_edi_stock.menu_stock_l10n_cl_dte_caf` | Cafs | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0005 | `l10n_mx_edi_stock.menu_stock_config_settings_mx` | Mexico | — | not installed | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0006 | `l10n_mx_edi_stock.menu_stock_mx_customs_document_type` | Custom Document Type | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0007 | `l10n_mx_edi_stock.menu_stock_mx_customs_regime` | Customs Regime | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0008 | `l10n_pe_edi_stock.menu_stock_config_settings_pe` | Peru | — | not installed | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0009 | `l10n_pe_edi_stock.menu_stock_pe_vehicles` | Vehicles | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0010 | `l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera` | GİB e-Dispatch | — | not installed | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0011 | `l10n_tr_nilvera_edispatch.menu_l10n_tr_nilvera_trailer_plate` | GİB Plate Numbers | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0012 | `mrp.mrp_operation_picking` | Manufacturings | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0013 | `mrp_mps.stock_mrp_mps_report_menu` | Master Production Schedu | — | LIVE 1of2 | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0014 | `stock.in_picking` | Receipts | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0015 | `stock.int_picking` | Internal | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0016 | `stock.menu_action_inventory_tree` | Physical Inventory | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0017 | `stock.menu_action_location_form` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0018 | `stock.menu_action_production_lot_form` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0019 | `stock.menu_action_rules_form` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0020 | `stock.menu_action_warehouse_form` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0021 | `stock.menu_attribute_action` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0022 | `stock.menu_delivery` | Delivery | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0023 | `stock.menu_package` | Packages | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0024 | `stock.menu_packaging_types` | Package Types | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0025 | `stock.menu_pickingtype` | Operations Types | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0026 | `stock.menu_procurement_compute` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0027 | `stock.menu_product_category_config_stock` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0028 | `stock.menu_product_in_config_stock` | Products | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0029 | `stock.menu_product_stock` | Stock | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0030 | `stock.menu_product_variant_config_stock` | Products | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0031 | `stock.menu_putaway` | Putaway Rules | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0032 | `stock.menu_reordering_rules_replenish` | Replenishment | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0033 | `stock.menu_routes_config` | Routes | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0034 | `stock.menu_stock_adjustments` | Adjustments | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0035 | `stock.menu_stock_config_settings` | Configuration | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0036 | `stock.menu_stock_general_settings` | Settings | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0037 | `stock.menu_stock_inventory_control` | Products | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0038 | `stock.menu_stock_procurement` | Procurement | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0039 | `stock.menu_stock_references` | (from action) | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0040 | `stock.menu_stock_root` | Inventory | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0041 | `stock.menu_stock_scrap` | Scrap | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0042 | `stock.menu_stock_transfers` | Transfers | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0043 | `stock.menu_stock_uom_form_action` | Units & Packagings | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0044 | `stock.menu_stock_warehouse_mgmt` | Operations | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0045 | `stock.menu_storage_categoty_config` | Storage Categories | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0046 | `stock.menu_valuation` | Locations | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0047 | `stock.menu_warehouse_config` | Warehouse Management | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0048 | `stock.menu_warehouse_report` | Reporting | — | LIVE both | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0049 | `stock.menu_wms_barcode_nomenclature_all` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0050 | `stock.out_picking` | Deliveries | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0051 | `stock.product_product_menu` | Product Variants | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0052 | `stock.stock_move_line_menu` | (from action) | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0053 | `stock.stock_move_menu` | Moves Analysis | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0054 | `stock.stock_picking_type_menu` | Overview | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0055 | `stock_delivery.menu_action_delivery_carrier_form` | (from action) | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0056 | `stock_delivery.menu_delivery_zip_prefix` | (from action) | — | LIVE both | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0057 | `stock_dropshipping.dropship_picking` | Dropships | — | not installed | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0058 | `stock_enterprise.stock_dashboard_menuitem` | Performance | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0059 | `stock_landed_costs.menu_stock_landed_cost` | Landed Costs | yes | LIVE both | yes | yes | **no** | **PARTIAL** | optional-function + runtime dimensions |
| LI-INV-MENU-0060 | `stock_picking_batch.menu_stock_jobs` | Jobs | — | LIVE 1of2 | — | — | **no** | **NOT APPLICABLE** | none |
| LI-INV-MENU-0061 | `stock_picking_batch.stock_picking_batch_menu` | (from action) | — | LIVE 1of2 | — | — | **no** | **MISSING** | FULL five-dimension study |
| LI-INV-MENU-0062 | `stock_picking_batch.stock_picking_wave_menu` | (from action) | — | LIVE 1of2 | — | — | **no** | **MISSING** | FULL five-dimension study |