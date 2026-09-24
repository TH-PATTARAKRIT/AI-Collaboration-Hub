# SMEsPlus Community19 — G05-G08 RED TEAM A1 Checkpoint R2

**Date:** 2026-09-25 (Asia/Bangkok)  
**Stations:** G05 INVENTORY / G06 MANUFACTURING / G07 PURCHASE / G08 SALES  
**Lane:** A1 Source Evidence only  
**Question Gate:** CLOSED for G05-G08 in the current governed GMVQ tree  
**Downstream:** NO A2 / NO Reconciliation / NO A3 / NO MASTER  
**Formal Coverage:** PROHIBITED until Boss freezes the Canonical Function-ID denominator

## 1. Control state

All four stations are ACTIVE in A1 and run independently. No station is marked merely QUEUED. Exact governed group counts remain G05=14, G06=12, G07=9, G08=31. The controlled mapping artifact remains `GROUP_STRUCTURE_V2_CORE.tsv`, SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`.

The row-level TSV is still not exposed by the accessible GitHub evidence surface. The authorized desktop source device is offline in this run, so the local `19.0-20260921` package and any local copy of the canonical TSV cannot be re-read. Exact remaining technical membership therefore stays OPEN; no module name is inferred from prefixes, categories, dependency intuition or historical examples.

Public Odoo `19.0` source is used only as reproducible A1 static evidence for already-verified anchors `stock`, `mrp`, `purchase`, `sale`. This does not prove byte identity with the governed local package.

`CURRENT-SOURCE PACKAGE RE-ANCHOR PENDING`

Source Presence != Runtime Reachability. No Evidence = No Progress.

## 2. Question Gate re-check

Current governed GitHub directory `01_Governance/COMMUNITY19/GMVQ` contains only:

- `G01_PLATFORM_BASE/`
- `GMVQ_BOSS_OVERNIGHT_G01_G16_AUTHORING_ORDER_20260924.md`
- `GMVQ_BOSS_STANDING_EXECUTION_AUTHORIZATION_20260922.md`

No governed G05, G06, G07 or G08 question-bank directory is present. Therefore each station remains:

`A1 ACTIVE -> WAIT QUESTION`

No QID was authored, inferred, answered or used to start runtime work.

## 3. G05 INVENTORY — deeper A1 source delta

Verified source objects:

- `addons/stock/models/stock_picking.py` blob `0f107f24103ab7372f8758608d3711aa514c069c`
- `addons/stock/models/stock_quant.py` blob `0004256d8ba0872d932de3ecf94bcdb0d4d2644e`
- `addons/stock/models/stock_rule.py` blob `f4eb81cb35a75b3c5620e52630b77d835919102a`

Static findings:

1. `stock.picking` lifecycle is explicitly computed as `draft`, `waiting`, `confirmed`, `assigned`, `done`, `cancel`.
2. Picking validation is not a single write: `button_validate()` confirms draft transfers, performs sanity checks, invokes pre-validation hooks/wizards, then calls `_action_done()`.
3. `_action_done()` performs company checking, completes eligible stock moves, writes completion timestamp, triggers downstream assignment for incoming/internal moves, and supports a `cancel_backorder` context path.
4. Operation type controls backorder policy through `ask / always / never`; therefore residual-quantity handling is configuration-sensitive at source level.
5. `stock.quant` separates physical quantity, reserved quantity and available quantity. Inventory count uses `inventory_quantity`, computed difference and scheduled count date.
6. Inventory adjustment refuses silent overwrite of stale counts: `action_apply_inventory()` routes outdated quants to an inventory-conflict wizard before `_apply_inventory()`.
7. Quant relocation is source-guarded to positive quantities belonging to a single company in one relocation action.
8. Serial-number checking explicitly scopes duplicate/location checks by product, lot and company where the lot is company-bound.
9. `_update_available_quantity()` requires either quantity or reserved quantity and gathers the exact product/location/lot/package/owner quant set before changing stock truth.
10. `stock.rule` explicitly distinguishes pull, push and pull+push actions; supply method distinguishes make-to-stock, make-to-order and MTS-else-MTO.

A1 contradiction/gap retained: none of these source paths prove runtime negative-stock policy, actual reservation reachability, backorder wizard configuration, inventory adjustment authorization, or valuation posting in the governed runtime.

## 4. G06 MANUFACTURING — deeper A1 source delta

Verified source objects:

- `addons/mrp/models/mrp_bom.py` blob `a0450106417750f515a7fd4f65917d5954a8d2b4`
- `addons/mrp/models/mrp_workorder.py` blob `505f35b578f629ade78d156395cc08965810dad6`

Static findings:

1. `mrp.bom` is company-aware (`_check_company_auto=True`) and supports `normal` manufacturing BoMs and `phantom` kits.
2. Manufacturing readiness is configurable as `all_available` or `asap` for first-operation availability.
3. Flexible consumption policy is explicit: `flexible`, `warning`, `strict`; source help states strict mode limits closing when consumption differs from BoM, except for manager authority.
4. BoM operation dependencies are represented explicitly and may influence planning/workorder status.
5. `_check_bom_cycle()` recursively rejects BoM component cycles with `ValidationError`.
6. BoM line quantity has a database constraint requiring quantity >= 0; zero is allowed for optional lines.
7. `mrp.workorder` lifecycle is `blocked`, `ready`, `progress`, `done`, `cancel` and inherits company from its Manufacturing Order.
8. Workorder dependency edges are explicit through `blocked_by_workorder_ids` / `needed_by_workorder_ids`.
9. `button_start()` blocks start when the workcenter is blocked and rejects start of completed/cancelled workorders.
10. `button_finish()` marks unfinished workorders done after deriving quantities and marking linked component/byproduct moves picked.

A1 contradiction/gap retained: source rules expose configurable readiness, flexible consumption and operation dependency behavior, but no runtime claim is allowed about which settings are enabled, who is a manager, whether workcenters are configured, or whether accounting/cost effects execute.

## 5. G07 PURCHASE — deeper A1 source delta

Verified source objects:

- `addons/purchase/models/purchase_order.py` blob `0c9e20192ec6320128cabf1665bc1493a1cf7c88`
- `addons/purchase/models/res_company.py` blob `75fc64c615246f84cf65e94794b0d51de1e921dd`
- `addons/purchase/models/res_config_settings.py` blob `e50d040ad89ab30ff4ec7be89562df99f67f3713`

Static findings:

1. `button_confirm()` accepts only draft/sent orders, runs a confirmation error gate and analytic distribution validation, then branches through `_approval_allowed()`.
2. If approval is allowed, `button_approve()` writes `state='purchase'` and confirmation date. Otherwise confirmation writes `state='to approve'`.
3. Confirmed PO locking is company-configurable; `po_lock='lock'` marks approved purchase orders locked.
4. Company configuration exposes one-step vs two-step Purchase approval and a monetary double-validation threshold (source default 5000 in company currency).
5. Purchase settings expose `po_order_approval`, minimum approval amount, lock-confirmed-orders, Purchase warnings, receipt reminder, and optional 3-way matching / purchase agreements / grid-entry modules.
6. `button_cancel()` refuses cancellation of locked POs and refuses cancellation when linked vendor bills are neither draft nor cancelled.

A1 contradiction/gap retained: source proves the approval/locking mechanism exists, but not the governed runtime setting, threshold, approver membership, receipt generation, bill matching behavior or actual state reachability.

## 6. G08 SALES — deeper A1 source delta

Verified source objects:

- `addons/sale/models/sale_order.py` blob `baeaa41b7deb60e67a04788e2f5f80c8f5ceabf2`
- `addons/sale/models/res_company.py` blob `a2e2d18792c688a7a5b813a7bb9b984c7e072a0e`

Static findings:

1. Sales confirmation runs `_confirmation_error_message()` before confirmation, rejects orders outside draft/sent state and rejects non-display/non-downpayment lines without a product.
2. `action_confirm()` validates analytic distribution, writes confirmation values (`state='sale'`, confirmation date), calls extension hook `_action_confirm()`, and optionally locks via the Sales auto-done feature.
3. Base `sale` intentionally leaves `_action_confirm()` as an extension point; therefore delivery/project/manufacturing side-effects must be proven in bridge modules, not attributed to base `sale`.
4. Cancellation rejects locked orders, then cancels related draft invoices and sets Sales Order state to cancel.
5. Company configuration exposes online signature, online payment, prepayment percentage and default quotation validity.
6. Quotation validity has a non-negative database constraint; online-payment prepayment percentage is constrained to >0 and <=100%.
7. Order-level signature/payment requirements are computed from the company configuration.

A1 contradiction/gap retained: source proves base Sales confirmation and configurable portal-sign/payment controls, but does not prove portal reachability, payment provider availability, signature completion, invoice posting, delivery creation or any extension hook outcome in runtime.

## 7. Cross-station reconciliation delta

The deeper source pass strengthens three controls:

- Inventory execution is a multi-step stateful path with conflict/backorder/reservation controls; a menu or model presence cannot substitute for runtime proof.
- Manufacturing has its own readiness, dependency and consumption policy states layered on stock movements; one lifecycle cannot be reduced to Inventory alone.
- Purchase and Sales base modules both contain extension/control seams. Source proves the seam exists; it does not prove the downstream bridge module is governed in the same group or is runtime-reachable.

Exact G05/G06/G07/G08 roster membership remains the critical A1 unresolved dependency. Bridge candidates are not promoted into a group until the canonical roster row is recovered.

## 8. Station disposition

| Station | A1 | Question Gate | A2 | Reconciliation | A3 | MASTER |
|---|---|---|---|---|---|---|
| G05 INVENTORY | ACTIVE — deeper delta verified | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G06 MANUFACTURING | ACTIVE — deeper delta verified | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G07 PURCHASE | ACTIVE — deeper delta verified | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |
| G08 SALES | ACTIVE — deeper delta verified | WAIT QUESTION | BLOCKED | BLOCKED | BLOCKED | BLOCKED |

No Formal Coverage percentage is produced. No Research-Complete claim is made.
