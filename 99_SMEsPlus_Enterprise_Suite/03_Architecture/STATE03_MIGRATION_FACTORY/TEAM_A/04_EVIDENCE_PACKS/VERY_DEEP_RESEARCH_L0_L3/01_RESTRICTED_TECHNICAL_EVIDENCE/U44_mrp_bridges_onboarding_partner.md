# U44 — mrp bridges, onboarding, partner autocomplete, partnership

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

| Field | Value |
|---|---|
| Unit | U44 |
| Modules | mrp, mrp_landed_costs, mrp_product_expiry, mrp_repair, mrp_subcontracting_account, mrp_subcontracting_dropshipping, mrp_subcontracting_landed_costs, mrp_subcontracting_purchase, mrp_subcontracting_repair, onboarding, partner_autocomplete, partnership |
| Source revision | 19.0.post20260921 |
| Date | 2026-10-02 |

## 0. Notes
- Source evidence only; behaviour not run (RT). DB reconciliation is config counts only (itest19c_research: 1 company, standard cost, periodic valuation, anglo-saxon off, 1 warehouse, no transactions, demo off, 356 modules installed).
- Version facts respected: no valuation-layer model, no procurement-group model, no UoM categories, no in-payment state, no immediate-transfer wizard.
- Prior evidence read first and not redone: U14 (mrp), U15 (bridges), U18 (partner autocomplete, partnership), U21 (onboarding). Where this unit disagrees, the claim carries CONTRA.
- Pointers are module-relative; claim anchors are verbatim (case-insensitive) within ±3 lines. Claim statements in the table are technical; the neutral file holds the plain-language counterparts.
- Contradiction/limits noted vs earlier units: U14 listed QWeb and static as unread; U44 read the report actions and the production QWeb template only (see MODULE STATUS TABLE).

## CAP-U44-01 Landed costs on production orders and subcontract receipts

- Modules: mrp_landed_costs, mrp_subcontracting_landed_costs
- Function-ID: GRV-F05
- Function: Spread additional cost over finished moves of selected manufacturing orders; for subcontract receipts redirect the target to the origin moves.
- Claims: VDR-U44-C001, VDR-U44-C002, VDR-U44-C003, VDR-U44-C004, VDR-U44-C005, VDR-U44-C006, VDR-U44-C007, VDR-U44-C008, VDR-U44-C009, VDR-U44-C010, VDR-U44-C011, VDR-U44-C012, VDR-U44-C013, VDR-U44-C014, VDR-U44-C015

### D1/D2/D3
D1: user enters landed cost, picks target type 'manufacturing' and orders. D2: `_get_targeted_move_ids` unions base targets with finished moves minus zero-cost-share by-products; subcontracting bridge swaps subcontract moves for `move_orig_ids`. D3: core `button_validate` allocates per line and posts the entry (core stock_landed_costs, not re-read here).

### State diagram
```
draft -> done [button_validate, only from draft]
target_model != manufacturing -> mrp_production_ids cleared [onchange]
draft -> error [validate with empty target]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C001 to VDR-U44-C015; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C001 to VDR-U44-C015; covered in D1/D2/D3 and claims |

### DB reconciliation
mrp_landed_costs/mrp_subcontracting_landed_costs: 1 view each, 1 selection value; no ACL/rule/cron/automation (source and DB agree). Landed costs in DB: 0.

### Unknown / RT
- Standard-cost products refused by core (RT)
- Allocation arithmetic and entry posting live in stock_landed_costs, not read here

## CAP-U44-02 Subcontracting valuation and portal analytic access

- Modules: mrp_subcontracting_account
- Function-ID: BRP-F03
- Function: Add subcontract price to BoM cost; reduce finished-move value by extra cost for non-standard products; portal analytic record rules.
- Claims: VDR-U44-C016, VDR-U44-C017, VDR-U44-C018, VDR-U44-C019, VDR-U44-C020, VDR-U44-C021, VDR-U44-C022, VDR-U44-C023, VDR-U44-C024, VDR-U44-C025, VDR-U44-C026, VDR-U44-C027, VDR-U44-C028

### D1/D2/D3
D1: BoM costing, MO close, journal entry value, portal read of analytic data. D2: `_compute_bom_price`, `_cal_price`, `_get_aml_value` overrides; two ir.rule + two ACL rows. D3: extra_cost on production -> value on journal item.

### State diagram
```
MO open -> MO done [close; extra_cost set only if last done receipt is a subcontract receipt]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C016 to VDR-U44-C028; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C016 to VDR-U44-C028; covered in D1/D2/D3 and claims |

### DB reconciliation
2 ACL + 2 rules in source and DB. 0 cron/automation/template.

### Unknown / RT
- bom_ids on analytic accounts populated? (RT)
- Standard-cost DB means value override inactive (RT)

## CAP-U44-03 Purchase and subcontracting bridge (resupply, lead time, demand, report)

- Modules: mrp_subcontracting_purchase
- Function-ID: BRP-F03
- Function: PO shows resupply transfers, picking shows source PO, lead-time formula, demand domain, notification, report overrides, valuation helpers.
- Claims: VDR-U44-C029, VDR-U44-C030, VDR-U44-C031, VDR-U44-C032, VDR-U44-C033, VDR-U44-C034, VDR-U44-C035, VDR-U44-C036, VDR-U44-C037, VDR-U44-C038, VDR-U44-C039, VDR-U44-C040, VDR-U44-C041, VDR-U44-C042, VDR-U44-C043, VDR-U44-C044, VDR-U44-C045

### D1/D2/D3
D1: PO form, picking form, replenishment, bill matching, BoM overview. D2: overrides of purchase.order, stock.picking, stock.rule, product.product, account.move.line, stock.move, BoM report. D3: po_to_notify context to stock.rule notification.

### State diagram
```
no state of its own; participates in PO draft -> purchase [confirm creates receipt and subcontract MO in mrp_subcontracting, not re-read]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C029 to VDR-U44-C045; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C029 to VDR-U44-C045; covered in D1/D2/D3 and claims |

### DB reconciliation
2 views in DB, 1 demo file not loaded; no ACL/rules/cron.

### Unknown / RT
- Standard-cost valuation paths not exercised (RT)
- `_merge`/report subtleties for subcontract BoM in mrp_subcontracting not re-read

## CAP-U44-04 Dropship subcontracting

- Modules: mrp_subcontracting_dropshipping
- Function-ID: BRP-F03
- Function: Per-company DSC operation type, buy rules, warehouse MTO pull rule, PO destination/partner logic and classification of flows.
- Claims: VDR-U44-C046, VDR-U44-C047, VDR-U44-C048, VDR-U44-C049, VDR-U44-C050, VDR-U44-C051, VDR-U44-C052, VDR-U44-C053, VDR-U44-C054, VDR-U44-C055, VDR-U44-C056, VDR-U44-C057, VDR-U44-C058, VDR-U44-C059, VDR-U44-C060, VDR-U44-C061, VDR-U44-C062, VDR-U44-C063, VDR-U44-C064, VDR-U44-C065, VDR-U44-C066

### D1/D2/D3
D1: install, warehouse flag change, PO creation, replenishment. D2: res.company, stock.warehouse, purchase.order, stock.rule, stock.move, stock.picking, stock.orderpoint overrides and one noupdate data file. D3: warehouse flag -> rule active -> route/picking-type active.

### State diagram
```
warehouse subcontracting_to_resupply False -> True [write; pull rule unarchived]
route active -> route archived [no active pull rule]
dropship picking type active -> archived [no active pull rule for company]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C046 to VDR-U44-C066; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C046 to VDR-U44-C066; covered in D1/D2/D3 and claims |

### DB reconciliation
Source: 1 view, 1 ir.model.inherit; DB: same. Warehouse flag true; types DS, DSC active, SBC inactive; route has 3 rules.

### Unknown / RT
- Tuple at stock_picking.py:33 (RT)
- Install data enables resupply on all warehouses (noupdate)

## CAP-U44-05 Expiry confirmation and repair bridges

- Modules: mrp_product_expiry, mrp_repair, mrp_subcontracting_repair
- Function-ID: FUNCTION MAPPING REQUIRED
- Function: Confirm before closing MO with expired lots; explode kit parts in repair orders; counts between MO and repair; empty subcontracting-repair bridge.
- Claims: VDR-U44-C067, VDR-U44-C068, VDR-U44-C069, VDR-U44-C070, VDR-U44-C071, VDR-U44-C072, VDR-U44-C073, VDR-U44-C074, VDR-U44-C075, VDR-U44-C076, VDR-U44-C077, VDR-U44-C078, VDR-U44-C079, VDR-U44-C080, VDR-U44-C081, VDR-U44-C082, VDR-U44-C083

### D1/D2/D3
D1: MO close, repair create/edit, smart buttons. D2: `pre_button_mark_done`, wizard `confirm_produce`, repair `action_explode`, stock.move phantom values. D3: skip_expired context flag; repair_id propagation.

### State diagram
```
MO to_close -> MO done [button_mark_done; interrupted once by wizard when expired lot]
repair part (kit) -> component parts [create/write action_explode]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C067 to VDR-U44-C083; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Automation | see claims VDR-U44-C067 to VDR-U44-C083; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C067 to VDR-U44-C083; covered in D1/D2/D3 and claims |

### DB reconciliation
Expiry: 1 view; repair: 2 views; subcontracting_repair: none. No ACL/rule/cron.

### Unknown / RT
- workorder branch of wizard unreachable here (RT)
- Repair kit price duplication

## CAP-U44-06 BoM Overview report

- Modules: mrp
- Function-ID: BRP-F09
- Function: Component tree with availability, lead time, cost and by-product shares.
- Claims: VDR-U44-C084, VDR-U44-C085, VDR-U44-C086, VDR-U44-C087, VDR-U44-C088, VDR-U44-C089, VDR-U44-C090, VDR-U44-C091, VDR-U44-C092, VDR-U44-C093, VDR-U44-C094, VDR-U44-C095, VDR-U44-C096, VDR-U44-C097, VDR-U44-C098

### D1/D2/D3
D1: report screen or PDF per BoM. D2: `report.mrp.report_bom_structure` abstract model; subcontracting overrides. D3: product stock/forecast + route rules -> lines; days_to_prepare_mo written back to BoM.

### State diagram
```
no state machine (read-only report); availability: available -> expected -> estimated -> unavailable [decision cascade, not transitions]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C084 to VDR-U44-C098; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C084 to VDR-U44-C098; covered in D1/D2/D3 and claims |

### DB reconciliation
No mrp_bom rows in DB; report actions seeded as ir.actions.report (not counted).

### Unknown / RT
- _merge_components double add (RT)
- Static JS/XML and bom_structure QWeb unread

## CAP-U44-07 MO Overview report and printed production documents

- Modules: mrp
- Function-ID: MFG-F04
- Function: Cost comparison, state labels, replenishment lines and printed order/label/work-order documents.
- Claims: VDR-U44-C099, VDR-U44-C100, VDR-U44-C101, VDR-U44-C102, VDR-U44-C103, VDR-U44-C104, VDR-U44-C105, VDR-U44-C106, VDR-U44-C107, VDR-U44-C108, VDR-U44-C109, VDR-U44-C110, VDR-U44-C111, VDR-U44-C112, VDR-U44-C113, VDR-U44-C114, VDR-U44-C115, VDR-U44-C116

### D1/D2/D3
D1: overview screen/PDF, printed documents. D2: `report.mrp.report_mo_overview`, QWeb order sheet, label templates, report actions. D3: moves/pickings/POs linked to order -> lines.

### State diagram
```
MO draft -> confirmed -> progress -> to_close -> done (core state field, not changed here); display state 'Not Ready' substitution for draft/confirmed
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C099 to VDR-U44-C116; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C099 to VDR-U44-C116; covered in D1/D2/D3 and claims |

### DB reconciliation
6 report actions in source; DB ir.actions.report not counted.

### Unknown / RT
- Static JS/XML, other QWeb templates unread
- Overview not bound to print menu

## CAP-U44-08 Onboarding steps and panels

- Modules: onboarding
- Function-ID: FUNCTION MAPPING REQUIRED
- Function: Per-company onboarding progress with step states, panel close, and consumer in accounting.
- Claims: VDR-U44-C117, VDR-U44-C118, VDR-U44-C119, VDR-U44-C120, VDR-U44-C121, VDR-U44-C122, VDR-U44-C123, VDR-U44-C124, VDR-U44-C125, VDR-U44-C126, VDR-U44-C127, VDR-U44-C128, VDR-U44-C129, VDR-U44-C130, VDR-U44-C131, VDR-U44-C132, VDR-U44-C133, VDR-U44-C134, VDR-U44-C135, VDR-U44-C136, VDR-U44-C137, VDR-U44-C138, VDR-U44-C139, VDR-U44-C140, VDR-U44-C141, VDR-U44-C142

### D1/D2/D3
D1: panel shown on dashboard; user completes steps; closes panel. D2: four models, constraints, unique indexes, ACL zero for non-admin. D3: account consumers call action_validate_step and create progress.

### State diagram
```
not_done -> just_done [action_set_just_done]
just_done -> done [state fetched for rendering]
onboarding not_done -> done [all steps just_done or done]
open -> closed [close action]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C117 to VDR-U44-C142; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C117 to VDR-U44-C142; covered in D1/D2/D3 and claims |

### DB reconciliation
Source: 12 ACL (8 zero, 4 system) = DB; 3 constraints = DB; 1 onboarding, 5 steps, 1 progress, 0 progress_step in DB.

### Unknown / RT
- Route name has no controller (RT)
- account_invoice onboarding not present in DB
- Panel JS/XML unread

## CAP-U44-09 Partner autocomplete and enrichment (outbound data)

- Modules: partner_autocomplete
- Function-ID: FUNCTION MAPPING REQUIRED
- Function: Suggestions and enrichment from an IAP service; fallback to VIES; company auto-enrichment.
- Claims: VDR-U44-C143, VDR-U44-C144, VDR-U44-C145, VDR-U44-C146, VDR-U44-C147, VDR-U44-C148, VDR-U44-C149, VDR-U44-C150, VDR-U44-C151, VDR-U44-C152, VDR-U44-C153, VDR-U44-C154, VDR-U44-C155, VDR-U44-C156, VDR-U44-C157, VDR-U44-C158, VDR-U44-C159, VDR-U44-C160, VDR-U44-C161, VDR-U44-C162, VDR-U44-C163, VDR-U44-C164, VDR-U44-C165, VDR-U44-C166, VDR-U44-C167, VDR-U44-C168, VDR-U44-C169, VDR-U44-C170, VDR-U44-C171, VDR-U44-C172, VDR-U44-C173, VDR-U44-C174, VDR-U44-C175, VDR-U44-C176

### D1/D2/D3
D1: typing in name/VAT fields; company creation; settings. D2: iap.autocomplete.api, res.partner, res.company, ir.http, settings; JS widget. D3: query -> `iap_jsonrpc` -> response -> format -> record write and chatter note.

### State diagram
```
company iap_enrich_auto_done False -> True [first enrichment attempt by a system user]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Configuration | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C143 to VDR-U44-C176; covered in D1/D2/D3 and claims |

### DB reconciliation
1 iap.service + 2 views = DB; 0 IAP accounts; no config parameters; company flag true.

### Unknown / RT
- Vendor service contract (RT)
- Token creation (RT)
- Worldwide country handling (RT)

## CAP-U44-10 Partnership grades and price lists

- Modules: partnership
- Function-ID: FUNCTION MAPPING REQUIRED
- Function: Gold/Silver/Bronze levels, forced price list, membership products, grade set on confirmation.
- Claims: VDR-U44-C177, VDR-U44-C178, VDR-U44-C179, VDR-U44-C180, VDR-U44-C181, VDR-U44-C182, VDR-U44-C183, VDR-U44-C184, VDR-U44-C185, VDR-U44-C186, VDR-U44-C187, VDR-U44-C188, VDR-U44-C189, VDR-U44-C190, VDR-U44-C191, VDR-U44-C192, VDR-U44-C193

### D1/D2/D3
D1: contact form, product setup, sale order confirmation, settings. D2: res.partner.grade, res.partner write, product.template, sale.order, company/settings. D3: product grade -> order assigned grade -> commercial partner grade -> forced price list property.

### State diagram
```
partner grade none -> Gold/Silver/Bronze [write or order confirmation]
grade X -> grade Y [later confirmation, no downgrade guard]
```

### Ten-dimension table
| Dimension | Finding |
|---|---|
| Function | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| State | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Trigger | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Control flow | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Data flow | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Inheritance | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Security | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Automation | see claims VDR-U44-C177 to VDR-U44-C193; NOT APPLICABLE — thin bridge, no behaviour of its own |
| Configuration | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |
| Cross-module | see claims VDR-U44-C177 to VDR-U44-C193; covered in D1/D2/D3 and claims |

### DB reconciliation
4 ACL, 3 grades, 3 act_window, 2 menus, 9 views = DB; 0 graded partners.

### Unknown / RT
- Price-list property per company (RT)
- Cancellation leaves level

## MODULE STATUS TABLE

| Module | Matrix status before | U44 claims | Capabilities covered | Assessment |
|---|---|---|---|---|
| mrp | PARTIAL | 33 | CAP-U44-06, CAP-U44-07 | PARTIAL — BoM and MO overview Python read fully, production QWeb template and report actions read; unread: bom_structure/mo_overview/workorder/zebra/delivery-slip/reception/rule QWeb, stock_forecasted.py, static JS and XML |
| mrp_landed_costs | PARTIAL | 7 | CAP-U44-01 | L3-READY (RT items listed) |
| mrp_product_expiry | PARTIAL | 7 | CAP-U44-05 | L3-READY (RT items listed) |
| mrp_repair | PARTIAL | 9 | CAP-U44-05 | L3-READY (RT items listed) |
| mrp_subcontracting_account | PARTIAL | 13 | CAP-U44-02 | L3-READY (RT items listed) |
| mrp_subcontracting_dropshipping | PARTIAL | 21 | CAP-U44-04 | L3-READY (RT items listed) |
| mrp_subcontracting_landed_costs | PARTIAL | 4 | CAP-U44-01 | L3-READY (RT items listed) |
| mrp_subcontracting_purchase | PARTIAL | 17 | CAP-U44-03 | L3-READY (RT items listed) |
| mrp_subcontracting_repair | PARTIAL | 1 | CAP-U44-05 | L3-READY (no code; manifest only) |
| onboarding | PARTIAL | 26 | CAP-U44-08 | L3-READY (RT items listed; panel static JS/XML unread) |
| partner_autocomplete | PARTIAL | 34 | CAP-U44-09 | L3-READY (server and core JS read; vendor contract and token creation RT) |
| partnership | PARTIAL | 17 | CAP-U44-10 | L3-READY (RT items listed) |

(mrp_subcontracting_repair has zero claims about code except the manifest claim; its count includes that one.)

## CLAIMS

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U44-C001 | GRV-F05 | mrp_landed_costs/__manifest__.py:13 | 'depends': ['stock_landed_costs', 'mrp'], | FACT | module installed | — | The bridge depends on the landed-cost module and manufacturing and is flagged to install automatically when both are present; it ships one view file and no access rows, rules, data records, crons or automations. | N-U44-001 |
| VDR-U44-C002 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:11 | Manufacturing Orders | FACT | always | — | Adds a fourth value, manufacturing, to the landed-cost target selection; when the module is removed, records holding that value fall back to the default value. | N-U44-001 |
| VDR-U44-C003 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:13 | mrp_production_ids = fields.Many2many( | FACT | always | — | A many-to-many field links a landed-cost record to manufacturing orders; the field is restricted to the stock-manager group and is not copied on duplicate. | N-U44-001 |
| VDR-U44-C004 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:15 | groups='stock.group_stock_manager' | FACT | always | — | Field-level group restriction: only stock managers can see or set the manufacturing-order selection (INFERENCE for effect on the form: the view file was not opened in this pass). | N-U44-013 |
| VDR-U44-C005 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:21 | self.mrp_production_ids = False | FACT | user changes target in the form | — | Changing the target type to anything other than manufacturing clears the selected manufacturing orders. | N-U44-004 |
| VDR-U44-C006 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:26 | self.mrp_production_ids.move_finished_ids | FACT | target = manufacturing | — | The moves receiving the landed cost are the standard targets united with the finished-product moves of the selected manufacturing orders. | N-U44-005 |
| VDR-U44-C007 | GRV-F05 | mrp_landed_costs/models/stock_landed_cost.py:27 | move_byproduct_ids.filtered(lambda move: not move.cost_share) | OBSERVATION | target = manufacturing | — | By-product moves without a cost share are subtracted from the finished-move set (set subtraction binds tighter than union in the expression, so the subtraction applies only to the manufacturing-order moves); by-products with a cost share stay targeted. | N-U44-006 |
| VDR-U44-C008 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:161 | cost_method not in ('fifo', 'average') | FACT | validation of any landed cost | RT | Core landed-cost allocation skips moves whose product does not use first-in-first-out or average costing; if no targeted move qualifies the user receives an error. The restored database uses standard cost, so manufacturing-order landed costs would be refused for current products (runtime behaviour not exercised). | N-U44-014 |
| VDR-U44-C009 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:103 | def button_validate(self): | FACT | always | — | Validation is the core landed-cost action; the bridge adds no state of its own and inherits the draft to done flow (draft only validates; line sums must match the cost lines). | N-U44-010 |
| VDR-U44-C010 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:250 | Only draft landed costs can be | FACT | always | — | A landed cost that is not in draft cannot be validated again. | N-U44-010 |
| VDR-U44-C011 | GRV-F05 | stock_landed_costs/models/stock_landed_cost.py:254 | Please define %s on which those | FACT | validation with empty target | — | Validation without any selected document raises an error naming the target type chosen. | N-U44-007 |
| VDR-U44-C012 | GRV-F05 | mrp_subcontracting_landed_costs/__manifest__.py:10 | associated picking reference in the search | FACT | module installed | — | The subcontracting landed-cost bridge describes itself as a search aid that shows the associated transfer reference; it also contains one view file and no data, access or automation records. | N-U44-002 |
| VDR-U44-C013 | GRV-F05 | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:14 | if move.is_subcontract: | FACT | landed cost targets include subcontract receipt moves | — | For each targeted move that is a subcontract move the allocation is redirected to the moves feeding it; all other moves are kept. | N-U44-008 |
| VDR-U44-C014 | GRV-F05 | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:15 | target_moves_ids.update(move.move_orig_ids.ids) | FACT | as above | — | The substitute set is the origin moves of the subcontract move, so cost lands on the subcontracting production side rather than the receipt itself. | N-U44-008 |
| VDR-U44-C015 | GRV-F05 | mrp_subcontracting_landed_costs/models/stock_landed_cost.py:12 | target_moves_ids = OrderedSet() | OBSERVATION | as above | — | Order of the target set is preserved and duplicates are removed, because an ordered set is used to collect ids. | N-U44-009 |
| VDR-U44-C016 | BRP-F03 | mrp_subcontracting_account/__manifest__.py:11 | 'depends': ['mrp_subcontracting', 'mrp_account'], | FACT | module installed | — | The valuation bridge depends on subcontracting and manufacturing accounting and installs automatically with both; it ships a rule file and an access file only. | N-U44-015 |
| VDR-U44-C017 | BRP-F03 | mrp_subcontracting_account/models/product_product.py:14 | if bom and bom.type == 'subcontract': | FACT | BoM cost computation for a subcontract BoM | — | The computed BoM price of a subcontract BoM is the standard computed price plus the price of the best-matching supplier line for the BoM quantity, unit and listed subcontractors. | N-U44-017 |
| VDR-U44-C018 | BRP-F03 | mrp_subcontracting_account/models/product_product.py:17 | seller.currency_id._convert(seller.price | FACT | seller found | — | The supplier price is converted from the supplier line currency into the current company currency at today's date, then converted from the supplier line unit to the product unit. | N-U44-017 |
| VDR-U44-C019 | BRP-F03 | mrp_subcontracting_account/models/mrp_production.py:10 | def _cal_price(self, consumed_moves): | FACT | closing a subcontracting production order | — | Before the standard cost calculation of the production order, the bridge looks at the last done receipt fed by the finished move; if that receipt is a subcontract receipt it sets the production order extra cost. | N-U44-018 |
| VDR-U44-C020 | BRP-F03 | mrp_subcontracting_account/models/mrp_production.py:21 | self.extra_cost = (bill_data['value'] + po_data['value']) / | FACT | billed or quoted amounts exist | — | Extra cost per unit is the billed value plus the not-yet-billed purchase quotation value divided by the received quantity. | N-U44-018 |
| VDR-U44-C021 | BRP-F03 | mrp_subcontracting_account/models/mrp_production.py:19 | self.extra_cost = last_done_receipt.price_unit | FACT | no bill and no quotation value | — | When neither a vendor bill nor a priced purchase line value is available, extra cost falls back to the receipt unit price. | N-U44-018 |
| VDR-U44-C022 | BRP-F03 | mrp_subcontracting_account/models/stock_move.py:16 | value -= self.production_id.extra_cost | FACT | finished move of a subcontract production whose product is not standard cost | RT | For finished moves that feed a done subcontract receipt and whose product is not at standard cost, the journal-entry value is reduced by extra cost times the quantity in product unit, so the subcontracting service stays outside the finished-goods component of the value. Standard-cost products are excluded, which matches the restored database; effect on posted entries not exercised. | N-U44-019 |
| VDR-U44-C023 | BRP-F03 | mrp_subcontracting_account/models/stock_move.py:14 | self.product_id.cost_method != "standard" | FACT | as above | RT | The adjustment never applies to standard-cost products, the only costing method in the restored database, so for current configuration this override is inactive. | N-U44-019 |
| VDR-U44-C024 | BRP-F03 | mrp_subcontracting_account/security/mrp_subcontracting_account_security.xml:7 | user.partner_id.commercial_partner_id.bom_ids.ids | FACT | portal user | RT | A portal record rule on analytic accounts lets a portal user see accounts whose BoM list intersects the BoMs of the user's commercial partner. The restored database holds both rules (non-global, portal group). | N-U44-022 |
| VDR-U44-C025 | BRP-F03 | mrp_subcontracting_account/security/mrp_subcontracting_account_security.xml:14 | [('account_id.bom_ids', 'in' | FACT | portal user | RT | A second portal rule restricts analytic lines the same way through the line's analytic account. | N-U44-022 |
| VDR-U44-C026 | BRP-F03 | mrp_subcontracting_account/security/ir.model.access.csv:2 | access_subcontracting_portal_analytic_account | FACT | portal user | — | Portal group receives read-only access to analytic accounts. | N-U44-022 |
| VDR-U44-C027 | BRP-F03 | mrp_subcontracting_account/security/ir.model.access.csv:3 | access_subcontracting_portal_analytic_line | FACT | portal user | — | Portal group receives read and write, but not create or delete, access to analytic lines. The restored database holds exactly these two access rows and two rules for this module. | N-U44-022 |
| VDR-U44-C028 | BRP-F03 | mrp_subcontracting_account/security/mrp_subcontracting_account_security.xml:7 | 'bom_ids', 'in' | UNKNOWN | — | RT | Whether the BoM list on an analytic account is ever populated is not shown by the files read; if it stays empty the two portal rules match nothing and portal subcontractors see no analytic data. Needs a runtime check. | N-U44-023 |
| VDR-U44-C029 | BRP-F03 | mrp_subcontracting_purchase/__manifest__.py:11 | 'depends': ['mrp_subcontracting', 'purchase_mrp'], | FACT | module installed | — | The purchase bridge depends on subcontracting and the purchase-manufacturing bridge, installs automatically, and has two view files plus a demo file (demo data is not loaded in the restored database). | N-U44-024 |
| VDR-U44-C030 | BRP-F03 | mrp_subcontracting_purchase/models/purchase_order.py:25 | subcontracted_productions.picking_ids | FACT | purchase order with subcontract moves | — | A purchase order counts, as resupply transfers, the transfers of the production orders that feed its subcontract receipt moves; a smart button opens them. | N-U44-024 |
| VDR-U44-C031 | BRP-F03 | mrp_subcontracting_purchase/models/purchase_order.py:30 | production.with_context(active_test=False).picking_type_id.active | OBSERVATION | linked production orders listed from a purchase order | — | Production orders whose operation type is archived are dropped from the list unless the caller asks to keep them. | N-U44-026 |
| VDR-U44-C032 | BRP-F03 | mrp_subcontracting_purchase/models/stock_picking.py:40 | return moves_subcontracted.purchase_line_id.order_id | FACT | transfer with subcontract moves | — | A transfer shows its source purchase orders through its subcontract moves; the button opens one order directly or a list. | N-U44-024 |
| VDR-U44-C033 | BRP-F03 | mrp_subcontracting_purchase/models/stock_picking.py:44 | res['po_to_notify'] = self.move_ids.purchase_line_id.order_id | FACT | subcontract production confirmation | — | The purchase orders behind the transfer are placed in the context used when the subcontract production is created. | N-U44-027 |
| VDR-U44-C034 | BRP-F03 | mrp_subcontracting_purchase/models/stock_rule.py:60 | origin_order = self.env.context.get('po_to_notify') | FACT | procurement exception during subcontract production | — | When a procurement exception is raised for a component, the product responsible and the purchaser of the originating order are notified through a vendor notification. | N-U44-027 |
| VDR-U44-C035 | BRP-F03 | mrp_subcontracting_purchase/models/stock_rule.py:32 | if seller.delay >= bom.produce_delay + bom.days_to_prepare_mo: | FACT | buy rule with subcontract BoM | — | Delay is the larger of vendor lead time and manufacturing lead time plus days to prepare the production order, with the purchase delay added; the comment in the code states the same formula. | N-U44-028 |
| VDR-U44-C036 | BRP-F03 | mrp_subcontracting_purchase/models/stock_rule.py:49 | delays['purchase_delay'] += days_to_order | FACT | manufacturing path longer than vendor lead time | — | On the manufacturing branch days to prepare are added to both total delay and purchase delay so the purchase order is dated correctly. | N-U44-028 |
| VDR-U44-C037 | BRP-F03 | mrp_subcontracting_purchase/models/stock_rule.py:13 | if not product.sudo().bom_ids: | FACT | product without any BoM, no buy rule, or no supplier | — | Products without a BoM, rules that are not buy rules, products without a supplier and products without a matching subcontract BoM fall back to the standard lead-time logic. | N-U44-028 |
| VDR-U44-C038 | BRP-F03 | mrp_subcontracting_purchase/models/product_product.py:12 | subcontracting_location_ids = self.env.companies.subcontracting_location_id.child_internal_location_ids.ids | FACT | monthly demand computation | — | Monthly demand also counts moves going into subcontracting locations, but ignores moves leaving them, so resupply to subcontractors is treated as demand. | N-U44-029 |
| VDR-U44-C039 | BRP-F03 | mrp_subcontracting_purchase/models/stock_move.py:12 | return res or self._is_subcontract_return() | FACT | valuation of returns | — | A return of a subcontract receipt is also treated as a purchase return. | N-U44-030 |
| VDR-U44-C040 | BRP-F03 | mrp_subcontracting_purchase/models/stock_move.py:31 | value = (self.price_unit - old_extra + | FACT | finished move of a subcontract production with a done subcontract receipt | RT | The finished-product move value is recomputed from the move unit price, minus the old extra cost, plus the new extra cost taken from bills and quotations, times the quantity. | N-U44-031 |
| VDR-U44-C041 | BRP-F03 | mrp_subcontracting_purchase/models/account_move_line.py:11 | if self.product_id.cost_method == 'standard' and self.purchase_line_id: | FACT | vendor bill line for a standard-cost subcontracted product | RT | For standard-cost products the price-difference computation adds the component cost of the subcontract production (sum of raw-move values converted at the latest raw-move date) divided by the quantity of done production orders; this is the only standard-cost handling in the subcontracting bridges and is not exercised at runtime. | N-U44-032 |
| VDR-U44-C042 | BRP-F03 | mrp_subcontracting_purchase/models/account_move_line.py:29 | set(mo.move_finished_ids.filtered(lambda mf: mf.product_id | FACT | bill line matching | — | A bill line also matches the finished moves of the subcontract production of its purchase moves, not only the receipt moves. | N-U44-032 |
| VDR-U44-C043 | BRP-F03 | mrp_subcontracting_purchase/report/mrp_report_bom_structure.py:12 | return super()._is_buy_route(rules, product, bom) and (not | FACT | BoM overview report | — | In the BoM overview a subcontract BoM is never reported as a plain buy route. | N-U44-033 |
| VDR-U44-C044 | BRP-F03 | mrp_subcontracting_purchase/report/mrp_report_bom_structure.py:19 | extra_delay = route_info['bom'].company_id.days_to_purchase | FACT | subcontract route with resupply delay | — | Subcontract resupply in the BoM overview always adds the company days-to-purchase and reports the state as estimated. | N-U44-033 |
| VDR-U44-C045 | BRP-F03 | mrp_subcontracting_purchase/__manifest__.py:17 | 'data/mrp_subcontracting_purchase_demo.xml', | OBSERVATION | demo loading | — | Demo data would be loaded only on demo databases; the restored database has demo disabled. | N-U44-024 |
| VDR-U44-C046 | BRP-F03 | mrp_subcontracting_dropshipping/__manifest__.py:12 | 'depends': ['mrp_subcontracting', 'stock_dropshipping'], | FACT | module installed | — | The dropship bridge depends on subcontracting and dropshipping, installs automatically, and loads one data file and one purchase view. | N-U44-036 |
| VDR-U44-C047 | BRP-F03 | mrp_subcontracting_dropshipping/data/mrp_subcontracting_dropshipping_data.xml:11 | {'subcontracting_to_resupply': True} | FACT | module installation | — | At installation, every existing warehouse is switched to supply components to subcontractors; the file is a noupdate block so it is not reapplied on upgrade. The restored database shows its single warehouse with this flag on. | N-U44-038 |
| VDR-U44-C048 | BRP-F03 | mrp_subcontracting_dropshipping/data/mrp_subcontracting_dropshipping_data.xml:6 | _create_missing_subcontracting_dropshipping_picking_type | FACT | module installation | — | The data file also creates, for companies without them, a dropship-subcontractor sequence, an operation type and the buy rules; the database shows both operation types active and the buy rule present. | N-U44-036 |
| VDR-U44-C049 | BRP-F03 | mrp_subcontracting_dropshipping/models/res_company.py:39 | 'sequence_code': 'DSC', | FACT | company creation or installation | — | A company-level operation type named Dropship Subcontractor with code dropship and prefix DSC is created, going from the vendor location to the company subcontracting location, with no warehouse. | N-U44-036 |
| VDR-U44-C050 | BRP-F03 | mrp_subcontracting_dropshipping/models/res_company.py:61 | 'action': 'buy', | FACT | company creation or installation | — | A buy rule supplier to subcontracting location, make-to-stock, is placed on the dropship route for each company that already has a matching operation type. | N-U44-036 |
| VDR-U44-C051 | BRP-F03 | mrp_subcontracting_dropshipping/models/res_company.py:104 | def _create_per_company_picking_types(self): | FACT | new company creation | — | New companies receive the sequence, operation type and rules through the per-company creation hooks, so each company has its own dropship-subcontractor operation type. | N-U44-036 |
| VDR-U44-C052 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_warehouse.py:74 | 'procure_method': 'make_to_order', | FACT | warehouse with subcontractor resupply | — | Each warehouse gets a make-to-order pull rule on the dropship route from the subcontracting location to production, using the subcontracting operation type, active only while the warehouse supplies subcontractors. | N-U44-039 |
| VDR-U44-C053 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_warehouse.py:28 | self._update_dropship_subcontract_rules() | FACT | warehouse flag changed | — | Switching the resupply flag archives or restores the warehouse dropship rules; the global route and company operation type are archived when no active pull rules remain. | N-U44-040 |
| VDR-U44-C054 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_warehouse.py:64 | route_id.active = bool(all_rules.filtered(lambda r: r.action == | FACT | warehouse change | — | The shared dropship route stays active only while at least one active pull rule exists on it; the operation type of a company follows the same test per company. | N-U44-040 |
| VDR-U44-C055 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_replenish_mixin.py:12 | ('id', '!=', self.env.ref('stock_dropshipping.route_drop_shipping' | FACT | manual replenishment wizard | — | The dropship route is removed from the routes a user may choose in the manual replenishment dialog. | N-U44-041 |
| VDR-U44-C056 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_move.py:18 | # subcontractor -> customer | FACT | move classification | — | A move is also classed as dropshipped when it runs from a subcontractor location to a customer, or from a vendor into a subcontractor location of the move partner. | N-U44-042 |
| VDR-U44-C057 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_move.py:37 | def _is_dropshipped_returned(self): | FACT | return classification | — | A return from a customer into the subcontractor location of the partner is classed as a dropshipped return and therefore as a purchase return. | N-U44-042 |
| VDR-U44-C058 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_move.py:46 | valuation_without_extra | FACT | valuation of a dropshipped subcontract receipt | RT | For a dropshipped subcontract receipt tied to a purchase line, the account value is taken from the finished move of the subcontract production instead of the receipt, unless the valuation-without-extra context is set. | N-U44-043 |
| VDR-U44-C059 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_picking.py:12 | p.location_dest_id.is_subcontract() and p.location_id.usage == 'supplier' | FACT | transfer classification | — | A transfer from a vendor to a subcontracting location is flagged as dropship. | N-U44-042 |
| VDR-U44-C060 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_picking.py:18 | return subcontract_move.sale_line_id.order_id.warehouse_id | FACT | subcontract move linked to a sales line | — | The warehouse used for the subcontract production is the warehouse of the sales order when the move came from a sales line. | N-U44-049 |
| VDR-U44-C061 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_picking.py:33 | res['picking_type_id'] = default_warehouse.subcontracting_type_id.id, | FACT | subcontract move delivered to a customer or subcontracting location | RT | When no operation type is found for the new production order, the first warehouse of the company supplies the subcontracting operation type. The line ends in a comma, so the assigned value is a one-element tuple rather than a plain id; whether the ORM accepts it was not tested. | N-U44-049 |
| VDR-U44-C062 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_rule.py:16 | values[0]['partner_id'] = move.raw_material_production_id.subcontractor_id.id | FACT | buy rule for component going to subcontracting location | — | The purchase order created for a component bound for a subcontracting location gets the subcontractor of the destination production as its delivery partner. | N-U44-044 |
| VDR-U44-C063 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_rule.py:22 | domain += (('dest_address_id', '=', values.get('partner_id')),) | FACT | purchase order merging | — | Existing draft purchase orders are only reused when their delivery address equals the subcontractor, so subcontractor deliveries are never merged across subcontractors. | N-U44-044 |
| VDR-U44-C064 | BRP-F03 | mrp_subcontracting_dropshipping/models/purchase.py:37 | return self.dest_address_id.property_stock_subcontractor.id | FACT | purchase order whose operation type delivers to a subcontracting location | — | The delivery location of such a purchase order is the subcontractor location of the delivery address; one subcontractor on the location fills the address automatically. | N-U44-045 |
| VDR-U44-C065 | BRP-F03 | mrp_subcontracting_dropshipping/models/purchase.py:31 | Please note this purchase order is | FACT | user picks an operation type delivering to a subcontracting location | — | A warning is shown when the chosen operation type delivers into a subcontracting location. | N-U44-045 |
| VDR-U44-C066 | BRP-F03 | mrp_subcontracting_dropshipping/models/stock_orderpoint.py:13 | vals['partner_id'] = self.location_id.subcontractor_ids.id | FACT | reorder rule on a subcontracting location with a single subcontractor | — | Replenishment values for a reorder rule on a subcontracting location include the single subcontractor of that location as partner. | N-U44-046 |
| VDR-U44-C067 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/__manifest__.py:12 | 'depends': ['mrp', 'product_expiry'], | FACT | module installed | — | The expiry bridge is declared as a technical module, depends on manufacturing and product expiry, installs automatically and loads one wizard view. | N-U44-050 |
| VDR-U44-C068 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/models/mrp_production.py:21 | ml.lot_id.product_expiry_alert | FACT | before closing a manufacturing order | — | Before the production order is marked done, the system gathers the lots on consumed component lines whose expiry alert is set. | N-U44-054 |
| VDR-U44-C069 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/models/mrp_production.py:26 | 'res_model': 'expiry.picking.confirmation', | FACT | expired lots found | — | If any such lot exists, closing is interrupted and a confirmation dialog opens instead of proceeding. | N-U44-054 |
| VDR-U44-C070 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/models/mrp_production.py:19 | self.env.context.get('skip_expired') | FACT | second pass after confirmation | — | The check is skipped when the confirmation dialog has already been accepted, so the dialog appears once. | N-U44-055 |
| VDR-U44-C071 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/wizard/confirm_expiry.py:38 | return self.production_ids.with_context(ctx).button_mark_done() | FACT | user accepts dialog | — | Accepting the dialog reruns the closing action with the skip flag set; declining leaves the order unchanged. | N-U44-055 |
| VDR-U44-C072 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/wizard/confirm_expiry.py:17 | self.show_lots = len(self.lot_ids) > 1 | FACT | dialog display | — | With one expired lot the lot and product are named in the message; with several, a list of lots is shown. | N-U44-056 |
| VDR-U44-C073 | FUNCTION MAPPING REQUIRED | mrp_product_expiry/wizard/confirm_expiry.py:43 | return self.workorder_id.with_context(ctx).record_production() | OBSERVATION | dialog opened from a work order | RT | The dialog has a work-order branch that would record production, but no override in this module opens it for a work order; within the files read the branch is not reachable from this module (another module not read may open it). | N-U44-062 |
| VDR-U44-C074 | FUNCTION MAPPING REQUIRED | mrp_repair/__manifest__.py:9 | 'depends': ['repair', 'mrp'], | FACT | module installed | — | The repair bridge depends on repair and manufacturing, installs automatically and ships two view files that add smart buttons only. | N-U44-051 |
| VDR-U44-C075 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:23 | orders.action_explode() | FACT | repair order creation or edit | — | On every create and every write of a repair order the part lines are scanned and kit products are exploded. | N-U44-057 |
| VDR-U44-C076 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:35 | bom_type='phantom')[op.product_id] | FACT | repair part line is a product with a kit BoM | — | A repair part line whose product has a kit-type BoM is replaced by one line per kit component, quantities scaled by the BoM factor; service components are skipped. | N-U44-057 |
| VDR-U44-C077 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:45 | self.env['stock.move'].browse(lines_to_unlink_ids).sudo().unlink() | FACT | as above | — | The original kit line is deleted with elevated rights and the component lines are created in draft state. | N-U44-057 |
| VDR-U44-C078 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:87 | 'price_unit': self.price_unit, | FACT | as above | — | Each component line copies the unit price of the kit line as is, so a kit price is repeated on every component; line type, locations and repair link are also copied. | N-U44-061 |
| VDR-U44-C079 | FUNCTION MAPPING REQUIRED | mrp_repair/models/stock_move.py:10 | vals['repair_id'] = self.repair_id.id | FACT | kit explosion in stock moves | — | The standard kit explosion of stock moves keeps the repair link on the exploded moves. | N-U44-057 |
| VDR-U44-C080 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:18 | repair.production_count = len(repair.reference_ids.production_ids) | FACT | repair order display | — | A repair order counts the production orders reached through its references; the smart button opens one order or a list and is visible only to manufacturing users and outside draft. | N-U44-051 |
| VDR-U44-C081 | FUNCTION MAPPING REQUIRED | mrp_repair/models/production.py:18 | production.repair_count = len(production.move_dest_ids.repair_id) | FACT | production order display | — | A production order counts the repair orders reached through its destination moves; the button is for stock users. | N-U44-051 |
| VDR-U44-C082 | FUNCTION MAPPING REQUIRED | mrp_repair/models/repair.py:73 | 'search_default_bom_parts': bool(product_ids) | FACT | adding parts from the catalog | — | When adding repair parts from the product catalog, a filter limited to parts of the repaired product's BoM is switched on if a BoM exists. | N-U44-058 |
| VDR-U44-C083 | FUNCTION MAPPING REQUIRED | mrp_subcontracting_repair/__manifest__.py:12 | 'mrp_subcontracting', 'repair' | FACT | module installed | — | The subcontracting-repair bridge declares only dependencies on subcontracting and repair and installs automatically; its Python package is empty and it ships no data, so it carries no behaviour of its own in this release. | N-U44-052 |
| VDR-U44-C084 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:27 | def _compute_current_production_capacity(self, bom_data): | FACT | BoM overview | — | Producible quantity is the smallest, over storable components, of free stock divided by quantity per BoM, rounded down, multiplied by the BoM output quantity. | N-U44-065 |
| VDR-U44-C085 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:298 | %(qty)s Ready To Produce | FACT | top-level line | — | The status text for the top-level line says how many units are ready to produce, or that none is ready. | N-U44-065 |
| VDR-U44-C086 | MFG-F04 | mrp/report/mrp_report_bom_structure.py:337 | bom_line.product_id.with_company(company).standard_price | FACT | component line | RT | Each component's cost is its standard price in the BoM-line unit multiplied by the line quantity, rounded in the currency of the parent BoM company; the cost is therefore always the standard price, whatever the product costing method. | N-U44-066 |
| VDR-U44-C087 | MFG-F04 | mrp/report/mrp_report_bom_structure.py:318 | bom_report_line['bom_cost'] += bom_report_line['operations_cost'] | FACT | BoM with operations | — | BoM cost adds operations cost to the sum of component costs. | N-U44-066 |
| VDR-U44-C088 | BRP-F08 | mrp/report/mrp_report_bom_structure.py:325 | bom_report_line['bom_cost'] *= bom_report_line['cost_share'] | FACT | BoM with by-products | — | The cost is then multiplied by the main product's share, which is one minus the by-product cost portions rounded to four decimals. | N-U44-067 |
| VDR-U44-C089 | BRP-F08 | mrp/report/mrp_report_bom_structure.py:442 | 'bom_cost': company.currency_id.round(total * cost_share), | FACT | by-product line | — | Each by-product line receives total cost times its share percentage divided by one hundred. | N-U44-067 |
| VDR-U44-C090 | MFG-F04 | mrp/report/mrp_report_bom_structure.py:471 | self.env.company.currency_id.round(op.cost) | OBSERVATION | operation line | — | Operation cost is rounded with the user's current company currency rather than the BoM company currency, unlike component lines; with one company and one currency this has no effect. | N-U44-073 |
| VDR-U44-C091 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:640 | 'lead_time': bom.produce_delay + rules_delay + bom.days_to_prepare_mo, | FACT | manufacture route | — | Route lead time is manufacturing lead time plus rule delays plus days to prepare; the separate manufacture delay leaves out days to prepare. | N-U44-068 |
| VDR-U44-C092 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:731 | # This component isn't available right | FACT | availability estimate | — | If any component can neither be taken from stock nor resupplied, the whole product is reported as not resupplyable, otherwise the longest component delay is used. | N-U44-068 |
| VDR-U44-C093 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:722 | return ('estimated', produce_delay) | FACT | availability estimate | — | For a manufacture route the resupply availability is estimated (manufacture delay plus longest component delay) or unavailable; the available and expected states come from the stock availability function read earlier (not re-anchored here). | N-U44-069 |
| VDR-U44-C094 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:756 | component_1["base_bom_line_qty"] = component_1["quantity"] + qty | OBSERVATION | same component appearing twice in the structure | RT | When two lines of the same component are merged, the per-BoM quantity is set to the already-updated total plus the second quantity, which looks like double counting of the second quantity; effect on the producible quantity not tested. | N-U44-074 |
| VDR-U44-C095 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:621 | def _need_special_rules(self, product_info, parent_bom=False, parent_product=False): | FACT | BoM overview | — | Two special-rule hooks return false in manufacturing core and are overridden by the subcontracting module (not re-read here). | N-U44-070 |
| VDR-U44-C096 | BRP-F09 | mrp/report/mrp_report_bom_structure.py:62 | def _get_pdf_doc(self, bom_id, data, quantity, product_variant_id=None): | FACT | printing | — | The printed version builds the same data structure and flattens it into lines, honouring which lines were unfolded on screen. | N-U44-063 |
| VDR-U44-C097 | BRP-F09 | mrp/report/mrp_report_views_main.xml:20 | 'Bom Overview - %s' % object.display_name | FACT | report menu | — | A printable BoM Overview report is bound to the BoM model. | N-U44-063 |
| VDR-U44-C098 | BRP-F09 | mrp/models/mrp_bom.py:341 | bom.days_to_prepare_mo = self.env['report.mrp.report_bom_structure']._get_max_component_delay | FACT | BoM computation | — | The BoM model reuses the overview report to compute days to prepare, the longest component delay, so the report logic also drives planning. | N-U44-071 |
| VDR-U44-C099 | MFG-F04 | mrp/report/mrp_report_mo_overview.py:486 | total_mo_cost = total_bom_cost = total_real_cost = | FACT | MO overview | — | Three parallel cost totals are kept for every manufacturing order: expected from the order, expected from the BoM, and real. | N-U44-077 |
| VDR-U44-C100 | MFG-F04 | mrp/report/mrp_report_mo_overview.py:535 | if move_raw.picked else 0 | FACT | component line | — | Real component cost counts only quantities that were picked. | N-U44-077 |
| VDR-U44-C101 | MFG-F04 | mrp/report/mrp_report_mo_overview.py:385 | hourly_cost = workorder.costs_hour or workorder.workcenter_id.costs_hour | FACT | done order operations | — | Operation cost of a work order is its duration in hours times the work order's hourly cost, falling back to the work center's hourly cost. | N-U44-078 |
| VDR-U44-C102 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:258 | Not Ready | FACT | draft or confirmed order | — | For orders still draft or confirmed the displayed state is replaced by Not Ready, a count of ready units, or Ready, from reserved plus free component quantities. | N-U44-085 |
| VDR-U44-C103 | MFG-F04 | mrp/report/mrp_report_mo_overview.py:274 | elif compare > 0: | FACT | cost comparison | — | A figure is flagged as danger when the current value exceeds the expected one and as success when it is lower; equal or unknown gives no flag. | N-U44-079 |
| VDR-U44-C104 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:709 | To Order | FACT | components short of supply | — | Shortfalls that no document covers appear as an extra To Order line and the component state becomes to order. | N-U44-080 |
| VDR-U44-C105 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:766 | In Transit | FACT | components in transit | — | Stock moving between locations toward the order appears as an In Transit line. | N-U44-080 |
| VDR-U44-C106 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:918 | if move.production_id: | FACT | replenishment origin | — | The origin of a replenishment document is looked up only through the production order of the origin move; origins from other applications are added by overrides. | N-U44-086 |
| VDR-U44-C107 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:970 | def _get_extra_replenishments(self, product): | FACT | replenishment lines | — | A hook for additional replenishment sources returns nothing in manufacturing core. | N-U44-086 |
| VDR-U44-C108 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:591 | receipt['date'] > mo_planned_start | FACT | receipt date check | — | A receipt later than the planned start of the order is flagged danger. | N-U44-081 |
| VDR-U44-C109 | MFG-F04 | mrp/report/mrp_report_mo_overview.py:144 | if production.state != 'done' or not | FACT | cost breakdown | — | A per-product cost breakdown exists only for done orders that have by-products. | N-U44-082 |
| VDR-U44-C110 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:980 | related_bom = self.env['mrp.bom']._bom_find(product)[product] | FACT | replenishment through manufacturing | — | Resupply by manufacturing finds the BoM of the product and uses the manufacturing lead time and rule delays as delay. | N-U44-083 |
| VDR-U44-C111 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_mo_overview.py:65 | doc['unfolded_ids'] = set(json.loads(data.get('unfoldedIds', '[]'))) | FACT | printing | — | The printed overview honours the unfolded lines and which columns the user showed on screen. | N-U44-075 |
| VDR-U44-C112 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_views_main.xml:30 | 'MO Overview - %s' % object.display_name | FACT | report menu | — | A printable MO Overview report is declared for production orders but has no binding to the action menu of the model in the data file, so it is only reachable from the overview screen. | N-U44-075 |
| VDR-U44-C113 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_production_templates.xml:55 | t-if="o.workorder_ids" groups="mrp.group_mrp_routings" | FACT | printing a production order | — | The printed production order lists operations only when the order has work orders and the viewer belongs to the routing group; actual duration appears while in progress or to close, and a barcode column is shown. | N-U44-088 |
| VDR-U44-C114 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_production_templates.xml:148 | print 1 label per 1 uom | OBSERVATION | finished product labels | RT | The finished-product label sheet prints one label per unit for products that share the unit reference, otherwise one label per line; the comment still mentions unit categories, which no longer exist in this release, while the code tests a common reference. | N-U44-084 |
| VDR-U44-C115 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_production_templates.xml:140 | <t t-set='nRows' t-value='12'/> | FACT | label sheet | — | The label sheet has twelve rows and four columns per page. | N-U44-084 |
| VDR-U44-C116 | FUNCTION MAPPING REQUIRED | mrp/report/mrp_report_views_main.xml:34 | Finished Product Label (ZPL) | FACT | report menu | — | Five printable documents are declared: production order, BoM overview, MO overview, finished product label in ZPL and in PDF, and work order (six records in total). | N-U44-075 |
| VDR-U44-C117 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress.py:8 | ('not_done', 'Not done'), | FACT | always | — | Progress has three states: not done, just done and done. | N-U44-096 |
| VDR-U44-C118 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress_step.py:30 | not_done.step_state = 'just_done' | FACT | a step is completed | — | Completing a step moves only a not-done step to just-done; a step already just-done or done is untouched and the call reports nothing changed. | N-U44-096 |
| VDR-U44-C119 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress_step.py:25 | was_just_done.step_state = 'done' | FACT | panel rendering | — | Just-done steps become done when the panel state is next fetched, so the just-done marker is displayed once. | N-U44-096 |
| VDR-U44-C120 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding_step.py:105 | return "JUST_DONE" if step.action_set_just_done() else "WAS_DONE" | FACT | validation by identifier | — | Validating a step by identifier returns not found, just done or was done; unknown identifiers are quiet. | N-U44-090 |
| VDR-U44-C121 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding_step.py:104 | return "NOT_FOUND" | FACT | validation by identifier | — | A missing step identifier does not raise an error. | N-U44-090 |
| VDR-U44-C122 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress.py:36 | != len(progress.onboarding_id.step_ids) | FACT | progress computation | — | The onboarding is done when the number of steps that are just-done or done equals the number of steps; otherwise not done. The value is stored and recomputed when steps change. | N-U44-097 |
| VDR-U44-C123 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress.py:75 | onboarding_states_values['onboarding_state'] = 'closed' | FACT | panel rendering | — | A closed panel reports closed; a done onboarding reports just done only in the render in which a step was consolidated, otherwise done. | N-U44-097 |
| VDR-U44-C124 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress.py:47 | self.is_onboarding_closed = True | FACT | user closes panel | — | Closing the panel only sets a flag on the progress record; toggle visibility flips it. | N-U44-098 |
| VDR-U44-C125 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:52 | lambda o: o.progress_ids.company_id or (True in | FACT | always | — | An onboarding is per company if any progress has a company or any step is per company; it stays per company even after such steps are removed. | N-U44-093 |
| VDR-U44-C126 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding_step.py:44 | is_per_company = fields.Boolean('Is per company', default=True) | FACT | always | — | Steps are per company by default. | N-U44-093 |
| VDR-U44-C127 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:61 | progress.company_id.id in {False, self.env.company.id} | FACT | reading progress | — | Current progress is the record with no company or with the active company; if none exists the onboarding reads as not done with the panel open. | N-U44-094 |
| VDR-U44-C128 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_progress.py:28 | _onboarding_company_uniq = models.UniqueIndex | FACT | always | — | At most one progress record exists per onboarding and company; one with no company counts as company zero. | N-U44-103 |
| VDR-U44-C129 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:40 | _route_name_uniq = models.Constraint( | FACT | always | — | The one-word route name of an onboarding must be unique. | N-U44-103 |
| VDR-U44-C130 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:14 | `/onboarding/{route_name}` | OBSERVATION | always | RT | A comment says the route name defines an HTTP path, but no controller exists in the module's source tree in this release; the name is used as a lookup key by other modules instead. | N-U44-105 |
| VDR-U44-C131 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding_step.py:69 | An "Opening Action" is required for | FACT | linking a step to an onboarding | — | A step cannot be attached to an onboarding unless it names an opening action. | N-U44-102 |
| VDR-U44-C132 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding_step.py:86 | steps_changing_is_per_company.progress_ids.unlink() | FACT | admin switches a step between per company and shared | — | Changing a step between per-company and shared deletes the step's progress, so completed steps become not done again. | N-U44-091 |
| VDR-U44-C133 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:101 | onboardings_to_refresh_progress.progress_ids.unlink() | FACT | per-company switch | — | Switching an onboarding to per-company deletes its shared progress and recreates it for the current company only. | N-U44-091 |
| VDR-U44-C134 | FUNCTION MAPPING REQUIRED | onboarding/models/onboarding_onboarding.py:116 | 'company_id': self.env.company.id if onboarding.is_per_company else False, | FACT | creating progress | — | New progress records are created for the active company, or with no company when shared. | N-U44-093 |
| VDR-U44-C135 | FUNCTION MAPPING REQUIRED | onboarding/security/ir.model.access.csv:2 | access_onboarding_all,onboarding.onboarding.all | FACT | always | — | Twelve access rows exist: for each of the four models one row with no group and one for ordinary internal users, both with no permission, and one for system administrators with full permission. | N-U44-104 |
| VDR-U44-C136 | FUNCTION MAPPING REQUIRED | onboarding/security/ir.model.access.csv:4 | access_onboarding_manager,onboarding.onboarding.manager | FACT | always | — | Only system administrators can read these models directly; the restored database holds the same twelve rows. | N-U44-104 |
| VDR-U44-C137 | FUNCTION MAPPING REQUIRED | account/models/company.py:464 | onboardings = self.env['onboarding.onboarding'].sudo().search | FACT | account setup | — | The accounting consumer reads onboarding data with elevated rights so ordinary users still see their panel and complete steps through it. | N-U44-095 |
| VDR-U44-C138 | FUNCTION MAPPING REQUIRED | account/models/company.py:462 | 'account_dashboard', | FACT | chart of accounts loading | — | Accounting creates progress records only for the accounting-dashboard onboarding when a chart is loaded; the restored database holds one onboarding, five steps and one not-done progress for its single company. | N-U44-100 |
| VDR-U44-C139 | FUNCTION MAPPING REQUIRED | account/models/account_journal_dashboard.py:694 | 'sale': 'account_invoice', | OBSERVATION | journal dashboard | RT | The sales-journal dashboard looks for an onboarding with route account_invoice, but the restored database holds no such onboarding, so that part of the dashboard has nothing to show. | N-U44-105 |
| VDR-U44-C140 | FUNCTION MAPPING REQUIRED | account/models/onboarding_onboarding_step.py:40 | not self.env.company.external_report_layout_id | FACT | document layout step | — | The document-layout step is marked done only when the company has a report layout set. | N-U44-092 |
| VDR-U44-C141 | FUNCTION MAPPING REQUIRED | account/models/company.py:958 | if self.street: | FACT | company data step | — | The company-data step is marked done only when the company has a street filled in. | N-U44-092 |
| VDR-U44-C142 | FUNCTION MAPPING REQUIRED | account/models/company.py:954 | action_validate_step('account.onboarding_onboarding_step_sales_tax') | FACT | sales tax step | — | The sales-tax step is marked done when its save action is called, with no check of the chosen taxes. | N-U44-092 |
| VDR-U44-C143 | FUNCTION MAPPING REQUIRED | partner_autocomplete/__manifest__.py:21 | 'auto_install': True, | FACT | module installed | — | Partner autocomplete depends only on the IAP mail bridge and installs automatically; it loads company and settings views and the IAP service record. | N-U44-106 |
| VDR-U44-C144 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:16 | _DEFAULT_ENDPOINT = 'https://partner-autocomplete.odoo.com' | FACT | always | — | Requests go to a fixed vendor-hosted service, overridable by a system parameter naming another base address. The restored database holds no such parameter, so the default applies. | N-U44-117 |
| VDR-U44-C145 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:33 | 'iap.partner_autocomplete.endpoint' | FACT | always | — | The base address can be changed by a system parameter. | N-U44-117 |
| VDR-U44-C146 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:26 | 'db_uuid': self.env['ir.config_parameter'].sudo().get_param('database.uuid'), | FACT | every call to the service | RT | Every request adds the database unique identifier, the application version, the user's language, the account token, and the active company's country code and postal code. | N-U44-118 |
| VDR-U44-C147 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:31 | 'zip': self.env.company.zip, | FACT | every call to the service | — | The company's postal code and country code accompany every query, whoever the user is. | N-U44-118 |
| VDR-U44-C148 | FUNCTION MAPPING REQUIRED | iap/tools/iap_tools.py:119 | req = requests.post(url, json=payload, timeout=timeout) | FACT | every call to the service | RT | The call is an outbound HTTPS JSON-RPC post with a random request identifier and a timeout of fifteen seconds by default; failures are converted into errors. | N-U44-119 |
| VDR-U44-C149 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:20 | if modules.module.current_test: | FACT | automated tests | — | During automated tests no call is made and the answer is treated as insufficient credit. | N-U44-119 |
| VDR-U44-C150 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:24 | raise ValueError(_('No account token')) | FACT | no account token | — | Without an account token the call is refused locally; the caller converts that to a no-account-token error. | N-U44-116 |
| VDR-U44-C151 | FUNCTION MAPPING REQUIRED | iap/models/iap_account.py:162 | No service exists with the provided | FACT | first use | RT | When no account exists for the service, one is created (the token is then fetched from the vendor service); the restored database holds no IAP account yet. | N-U44-120 |
| VDR-U44-C152 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/iap_autocomplete_api.py:46 | return False, 'Insufficient Credit' | FACT | service failure | — | Errors are mapped to a result pair with a message: insufficient credit, the error text for network or access failures, or no account token. | N-U44-108 |
| VDR-U44-C153 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:90 | 'search_by_name' | FACT | user types a company name | — | A name search sends the typed text and the country code of the chosen country; an id of zero (the browser's worldwide choice) yields no country code, so no country filter is sent. | N-U44-121 |
| VDR-U44-C154 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:87 | if query_country_id is False: | OBSERVATION | name search with no country given | RT | Only an explicit False (not zero) falls back to the active company country; the inline comment says zero purposely means no country filter. How the vendor service treats a missing country was not verified. | N-U44-125 |
| VDR-U44-C155 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:106 | 'search_by_vat' | FACT | user types a tax number | — | A tax number search sends the typed number and country code. | N-U44-121 |
| VDR-U44-C156 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:118 | vies_result = check_vies(vat, timeout=timeout) | FACT | vendor search fails or returns nothing for a tax number | RT | If the vendor service fails or returns no results for a tax number, the number is sent to the public European VIES check instead, which is a second outside destination; a valid answer with a real name yields one suggestion built from the returned name and address. | N-U44-122 |
| VDR-U44-C157 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:177 | 'enrich_by_duns' | FACT | user picks a suggestion | — | Selecting a suggestion triggers enrichment by D-U-N-S number, by Indian GST number, or (for companies) by web domain. | N-U44-123 |
| VDR-U44-C158 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:184 | 'enrich_by_gst' | FACT | user picks a suggestion with a GST number | — | GST enrichment is chosen by the browser when the query looks like a fifteen-character GST pattern. | N-U44-123 |
| VDR-U44-C159 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:191 | 'enrich_by_domain' | FACT | company enrichment | — | Company enrichment sends only the web domain. | N-U44-124 |
| VDR-U44-C160 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:150 | 'error_message': 'Insufficient Credit' | FACT | enrichment response | — | An enrichment answer can carry insufficient-credit, unable-to-enrich (stated as no credit consumed) or the transport error message. | N-U44-108 |
| VDR-U44-C161 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:167 | self.env['ir.module.module']._get('base_vat').state == 'installed' | FACT | after enrichment | RT | The returned tax number is validated against local rules only when the tax-number validation module is installed; it is not installed in the restored database, so returned numbers are not checked. | N-U44-113 |
| VDR-U44-C162 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:22 | country = self.env['res.country'].search([['code', '=ilike', country_code]]) | FACT | response formatting | — | Returned country, state, industry and language codes are matched to local records by code and then name; city matching happens only if the extended-address module is installed (not installed here). | N-U44-109 |
| VDR-U44-C163 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:43 | if self.env.user._is_system() and self.env.registry.ready | FACT | company creation by an administrator | — | Automatic company enrichment runs only when the current user is a system user, the registry is ready, and demo is not loading; it happens once, after which the company is marked done. | N-U44-110 |
| VDR-U44-C164 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:25 | res.sudo().iap_enrich_auto_done = True | FACT | automated tests | — | During tests companies are marked done without calling the service. | N-U44-110 |
| VDR-U44-C165 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:94 | if company_domain and company_domain not in | FACT | company enrichment | — | The domain comes from the company e-mail unless that is a free mail provider, otherwise from the website, excluding local test names. | N-U44-124 |
| VDR-U44-C166 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:12 | COMPANY_AC_TIMEOUT = 5 | FACT | company enrichment | — | Company enrichment uses a five-second timeout. | N-U44-119 |
| VDR-U44-C167 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:64 | (field == 'image_1920' or not self.partner_id[field]) | FACT | company enrichment | — | Enrichment writes only fields that are empty on the company contact, and always the logo, so existing data are not overwritten except the logo. | N-U44-111 |
| VDR-U44-C168 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/ir_http.py:14 | session_info['iap_company_enrich'] = not self.env.user.company_id.iap_enrich_auto_done | FACT | administrator opens the web client | — | The web client is told, for administrators only, whether the user's company still needs enrichment. | N-U44-110 |
| VDR-U44-C169 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_company.py:36 | node.set('widget', 'field_partner_autocomplete') | FACT | company and contact forms | — | On company and contact forms the name, tax number and D-U-N-S fields are switched to the autocomplete widget. | N-U44-106 |
| VDR-U44-C170 | FUNCTION MAPPING REQUIRED | partner_autocomplete/static/src/js/partner_autocomplete_fieldchar.js:27 | return request && request.length > 2; | FACT | user types | — | Suggestions start only after more than two characters have been typed; a previous empty result for a shorter prefix suppresses further requests. | N-U44-121 |
| VDR-U44-C171 | FUNCTION MAPPING REQUIRED | partner_autocomplete/static/src/js/partner_autocomplete_core.js:146 | value.startsWith(lastNoResultsQuery) | FACT | user types | — | A query that starts with an earlier empty-result query is not sent, which reduces outside calls. | N-U44-121 |
| VDR-U44-C172 | FUNCTION MAPPING REQUIRED | partner_autocomplete/static/src/js/partner_autocomplete_core.js:36 | checkVATNumber(sanitizeVAT(value)) | FACT | user types | — | Format check of tax numbers runs in the browser with a bundled library before any outside call. | N-U44-106 |
| VDR-U44-C173 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:251 | 'iap_mail.enrich_company_by_dnb' | FACT | after enrichment of a contact | — | After enrichment a note is posted on the contact with its contact data, logo and the supplier's activity tags; the note stays on the record. | N-U44-112 |
| VDR-U44-C174 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_partner.py:214 | self.env['res.partner.category'].create({'name': tag_name}) | FACT | after enrichment | — | Activity codes from the service create contact tags when no tag of the same name exists, without limit on how many tags the service may add. | N-U44-112 |
| VDR-U44-C175 | FUNCTION MAPPING REQUIRED | partner_autocomplete/models/res_config_settings.py:13 | self.env['iap.account'].get_credits('partner_autocomplete') <= 0 | FACT | opening general settings | RT | Opening general settings asks the vendor service for the credit balance, which is a further outside call; a buy-credit link opens the vendor page. | N-U44-120 |
| VDR-U44-C176 | FUNCTION MAPPING REQUIRED | partner_autocomplete/data/iap_service_data.xml:6 | technical_name">partner_autocomplete | FACT | installation | — | One service record named Partner Autocomplete counting in whole enrichments is seeded; the restored database holds four IAP service records in total and no IAP account. | N-U44-106 |
| VDR-U44-C177 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner_grade.py:15 | default_pricelist_id = fields.Many2one('product.pricelist') | FACT | always | — | A partner grade has name, sequence, active flag, company and an optional default price list; the count of graded contacts is computed. | N-U44-126 |
| VDR-U44-C178 | FUNCTION MAPPING REQUIRED | partnership/data/res_partner_grade_data.xml:4 | <field name="name">Gold</field> | FACT | installation | — | Three grades are seeded: Gold, Silver and Bronze, sequences one, two and three, none with a price list; the restored database holds them, active, with no graded contacts. | N-U44-126 |
| VDR-U44-C179 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner.py:15 | if grade.default_pricelist_id: | FACT | setting a grade on a contact | — | When a contact is given a grade that has a default price list, the contact's own price list is forced to that list. | N-U44-128 |
| VDR-U44-C180 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner.py:17 | if pricelist and pricelist != grade.default_pricelist_id.id: | FACT | same write also sets a different price list | — | If the same change also supplies a different price list, the change is refused with an error saying two different price lists were given. | N-U44-135 |
| VDR-U44-C181 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner.py:23 | vals['specific_property_product_pricelist'] = grade.default_pricelist_id.id | FACT | grade with price list | RT | The forced price list is the company-specific price list setting of the contact, which is stored per company; the contact's other-company settings are unaffected (INFERENCE from the base product module, not exercised). | N-U44-128 |
| VDR-U44-C182 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner.py:24 | return super().write(vals) | OBSERVATION | grade removed or changed later | RT | Removing or changing a grade later does not restore the earlier price list; only setting a grade runs the rule. | N-U44-138 |
| VDR-U44-C183 | FUNCTION MAPPING REQUIRED | partnership/models/res_partner.py:10 | grade_id = fields.Many2one('res.partner.grade', 'Partner Level', tracking=True | FACT | grade change | — | Changes of a contact's level are tracked in its history. | N-U44-131 |
| VDR-U44-C184 | FUNCTION MAPPING REQUIRED | partnership/models/product_template.py:10 | selection_add=[('partnership', 'Membership / Partnership')] | FACT | product setup | — | A service product can be set to a membership or partnership type with an assigned level; it counts among the types saleable on orders. | N-U44-126 |
| VDR-U44-C185 | FUNCTION MAPPING REQUIRED | partnership/models/product_template.py:16 | return super()._get_saleable_tracking_types() + ['partnership'] | FACT | product setup | — | The membership type is added to the saleable service types. | N-U44-126 |
| VDR-U44-C186 | FUNCTION MAPPING REQUIRED | partnership/models/sale_order.py:25 | so.assigned_grade_id = partnership_lines.mapped('product_id.grade_id')[:1] | FACT | order lines | — | An order's assigned level is the level of its first membership line. | N-U44-129 |
| VDR-U44-C187 | FUNCTION MAPPING REQUIRED | partnership/models/sale_order.py:12 | @api.constrains('order_line') | FACT | editing order lines | — | A check on the order lines refuses an order whose products carry more than one different level; the message talks about confirming, but the check fires when lines change, not at confirmation. | N-U44-136 |
| VDR-U44-C188 | FUNCTION MAPPING REQUIRED | partnership/models/sale_order.py:36 | so.partner_id.commercial_partner_id.grade_id = so.assigned_grade_id | FACT | order confirmation | — | On confirmation the commercial partner of the customer receives the order's level; there are no dates, no expiry and no check against the current level, so a later lower-level order replaces a higher level. | N-U44-130 |
| VDR-U44-C189 | FUNCTION MAPPING REQUIRED | partnership/models/sale_order.py:32 | def _add_partnership(self): | OBSERVATION | membership lifecycle | — | The module has no cancellation, renewal, expiry or refund handling: cancelling an order leaves the level in place, and confirming a membership twice leaves one level. | N-U44-131 |
| VDR-U44-C190 | FUNCTION MAPPING REQUIRED | partnership/models/res_company.py:11 | Name used to refer to affiliates | OBSERVATION | settings | — | The company stores a label for members; the default is Members and it is translatable. | N-U44-126 |
| VDR-U44-C191 | FUNCTION MAPPING REQUIRED | partnership/models/res_config_settings.py:15 | crm_menu.name = self.partnership_label | FACT | settings change | — | Editing the label in settings renames the customer-relationship menu item immediately, shared by all users, even before the settings are saved (the rename is inside an on-change). | N-U44-132 |
| VDR-U44-C192 | FUNCTION MAPPING REQUIRED | partnership/models/product_pricelist.py:14 | domain=[('specific_property_product_pricelist', 'in', self.ids)], | FACT | price list form | — | A price list shows how many contacts use it as their specific price list. | N-U44-126 |
| VDR-U44-C193 | FUNCTION MAPPING REQUIRED | partnership/security/ir.model.access.csv:4 | access_res_partner_grade_manager | FACT | always | — | Four access rows: ordinary users read only, system administrators full, sales managers full, salespeople read, write and create without delete. The restored database holds the same four. | N-U44-137 |
