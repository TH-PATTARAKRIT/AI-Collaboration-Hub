# A18 — Team A Inventory Deep Research Final Report

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Synthesize the full DR-002 Account-grade Inventory Deep Research pass into one executive report | Claude (Team A, session `SMEPLUS-26-08-31-MIG-A-INV-BB-DR-002`) | This folder (`INVENTORY_CORE_BACKBONE/DEEP_RESEARCH_DR002/EXECUTION/`) | 2026-08-31 | Independent Evidence Review (required next); Boss (sole Final Approver) | **HOLD / EVIDENCE REQUIRED — MATERIAL UNKNOWN EXHAUSTION NOT ACHIEVED** | Boss Inventory Evidence Gate decision remains PENDING; blocks Team B Inventory design |

## 1. What this session did

1. Verified all frozen governing commits and documents before making any change (A0).
2. Built a focused Inventory source map across the 93,866-file authorized source tree (A1).
3. Attempted independent DB/dump forensics; the attempt was blocked by this session's own sandbox controls (not by source inaccessibility); reused GROUP A's own independently-corroborated forensics DELTA-FIRST instead (A2).
4. Dispatched three parallel, read-only primary-source research passes against the real Odoo source (`stock`/`stock_account`/`stock_landed_costs`; `product`/`uom`; `sale_stock`/`purchase_stock`/`mrp`), producing exact field/method-level citations for quantity semantics, state/event lifecycle, warehouse/location/product/UOM/traceability, routes/procurement/replenishment, adjustment/count, cross-domain physical handoffs, and — the deliverable the Boss Amendment specifically mandated deepening — the Inventory↔Accounting valuation interface (A3–A9).
5. Produced a SaaS/tenant/company/warehouse risk register, a Thailand triangulation register (reusing GROUP A's own register, adding no unsourced Thailand claims), a migration/provenance register, and a cross-domain invariant candidate register (A10–A13).
6. Consolidated a single canonical Unknown/Conflict/Evidence Gap register carrying forward GROUP A's own open items by exact ID, reconciling two of them against this pass's fresh findings, and adding this pass's own new items with full mandatory fields (A14).
7. Evaluated Material Unknown Exhaustion against the Amendment's own criteria and reached an honest `HOLD` disposition (A15).
8. Assembled an Inventory-side evidence pack for the future mandatory Accounting × Inventory Cross-Proof (A16).
9. Confirmed clean-room discipline was maintained throughout (A17).
10. Did **not** design Team B target architecture, Accounting internals, GL/COA/posting rules, database schema, or any production code. Did **not** authorize COA-G0x, PMO, Team B, Team C, Development, Release, or Production.

## 2. Central findings (most consequential, ranked)

1. **No `stock.valuation.layer` model exists in this checkout** — valuation lives directly on `stock.move` (`value`, `value_manual`, `remaining_qty`, `remaining_value`) plus a `product.value` audit model. This is the single most material discovery of this pass, directly answering the Amendment's mandate to deepen the valuation interface beyond GROUP A's "interface observation only" scope (A9).
2. **No `uom.category` model and no `product.packaging` model exist** — `uom.uom` is a self-referential conversion tree; packaging is represented via `product.template.uom_ids` + a `product.uom` barcode-link model (A5).
3. **No `procurement.group` model exists** — grouping/origin-tracking uses a `stock.reference` model instead (A6).
4. **Product classification is a two-field system**: `type` (`consu`/`service`/`combo`) gates whether a stock move is even created; `is_storable` (settable only when `type=='consu'`) gates reservation, forecast, and valuation eligibility (A5).
5. **Over/under-fulfillment, negative-quantity prevention, and quant-bin uniqueness are enforced entirely at the application layer, with zero DB CHECK constraints** — independently corroborated via two separate evidence paths (this pass's own source reading + GROUP A's DB forensics) (A2, A13).
6. **Timing/cutoff evidence is genuinely missing** — this is the single highest-priority follow-up item, directly blocking full confidence in the mandatory Cross-Proof scenario 6 (A7, A9, A15, A16).
7. **Tenant-isolation enforcement mechanism (record rules/ACLs) was not read this pass** — `company_id` is confirmed as the only scoping field, but whether/how it is actually enforced remains open (A10, A13, A16).

## 3. Coverage summary

22 of 22 mandatory research domains have explicit coverage; 19 reached direct evidenced findings, 3 reached an honestly registered gap rather than fabricated closure (A15 §1). 21/21 mandatory deliverables exist in this folder.

## 4. Unknown/Conflict/Gap summary

0 Critical open, 5 High open (all explicitly blocking with disclosed materiality, not silently carried), 14 Medium open, 7 Low open. 1 GROUP A Medium item newly resolved this pass; 1 GROUP A Medium item independently re-corroborated; 3 GROUP A Critical items independently re-corroborated as already resolved (A14, A15 §2).

## 5. Relationship to the frozen GROUP A package

This pass explicitly does **not** restart or discard the GROUP A Sales+Inventory+Purchase evidence (`8b0993d`), which is itself already Independent-Evidence-Reviewed (`PASS/VERIFIED`) and Boss-Approved (`bd9b87f`) for progression to Team B Design at the **combined Sales+Inventory+Purchase** scope. This DR-002 pass is the Amendment-mandated, **Inventory-specific**, deeper research layer that sits on top of that approved baseline — it does not reopen, contradict, or invalidate the GROUP A Boss Gate decision. Where this pass's fresh source reading corroborates GROUP A's findings (the large majority of cases), that corroboration is noted explicitly rather than silently assumed. Where this pass's findings newly resolve or narrow a GROUP A open item, that is likewise noted explicitly (A14).

## 6. Terminal statement

**`TEAM A INVENTORY DEEP RESEARCH — HOLD / EVIDENCE REQUIRED — MATERIAL UNKNOWN EXHAUSTION NOT ACHIEVED`**

This is the honest, evidence-supported disposition per DR-002 §11 and the Amendment §4 exhaustion standard (full reasoning in A15). This is not a claim of failure or clean-room violation — no such violation was found (A17) — and it is not a claim that no progress was made: substantial, precisely-cited primary research was produced, one Critical-tier structural discovery was made, and the Amendment's specific valuation-deepening mandate was substantively delivered. It is a claim that five High-severity items remain genuinely, explicitly open and that closing them (particularly N-A7-03/N-A9-02 timing/cutoff and N-A13-02 tenant-isolation enforcement) is the honest prerequisite before this package could instead claim `MATERIAL UNKNOWN EXHAUSTION ACHIEVED`.

`COA-G01`/other Accounting Gate statuses are unaffected by this report — this is a Team A Inventory research deliverable, not an Accounting Gate action.

`TEAM B INVENTORY DESIGN = NOT AUTHORIZED.` `TEAM C / DEVELOPMENT = NOT AUTHORIZED.` `PMO VERIFICATION = PENDING.` `BOSS INVENTORY EVIDENCE GATE = PENDING.`

No Evidence = No Progress. No Material Unknown Exhaustion = No Inventory Evidence Gate PASS. Never Skip Gate. Boss is the sole Final Approver.
