# STATE03 Sales Delta Intake — Cross-Workstream Check Against GROUP_01_SALES_INVENTORY_PURCHASE

Document ID: `STATE03-SALES-DELTA-INTAKE`
Version: 1.0
Date: 2026-09-29
Authority: Boss's "STATE03 M3 Shared Master Then Sales Delta Continuation" §2
Status: `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`

## Purpose

Per Boss's explicit instruction, before studying any Sales function this session performs a cross-workstream delta intake against the pre-existing `GROUP_01_SALES_INVENTORY_PURCHASE` research track (session series `SMEPLUS-26-08-3x-MIG-A-GRPA-SIP-*`, branch `claude/group-a-sales-inventory-purchase-dr002`, terminal status `TEAM A EVIDENCE GATE CANDIDATE — READY FOR INDEPENDENT REVIEW`). Read read-only (`git fetch` + `git show <branch>:<path>`, no checkout, no merge) — this session has no write/merge access to that branch and does not need any to read it for delta-intake purposes.

## Method

Read `03_SALES_CAPABILITY_MODEL.md` (Phase 3, 289 lines, source-code+DB-tier evidence: `sale/models/sale_order.py` read in full, 2299 lines; `sale_order_line.py` in full, 1819 lines; `sale_stock` overrides; test files) in full, plus the relevant summary sections of `01_SHARED_MASTER_DEPENDENCY_MAP.md` (Pricing/Pricelist), `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`, and `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`.

## Delta intake against Boss's 4 Sales priority areas

| # | Priority area | Existing coverage (pointer) | Classification | Note |
|---|---|---|---|---|
| 1 | Quotation/order commitment and pricing basis | `SO-01`, `SO-04`, `SO-05`, `SO-08`, `SO-12`–`19`, `SO-21`–`23`, `SO-28`, `SO-29`, `SO-32`/`33`/`36` (order lifecycle, locking, credit-limit advisory-only, confirmation gate = state+product only); Phase 1's `PRC-*` (Pricing/Pricelist: Sale-only, Purchase has none) | **Carry-forward** | Source-code-tier (file+line), test-confirmed (`SO-36`). Strictly higher tier than this session's own WebSearch-documentation ceiling (V2) |
| 2 | Delivery policy, reservation, fulfillment handoff | `SOL-05`/`06` (delivered-qty dispatch: manual/analytic/stock_move), `SVS-06` (`type=='consu'` master gate for stock-move creation), `PDEL-01`–`05` (`delivery_status`, `qty_to_deliver`, `effective_date`) | **Carry-forward** | Directly answers, at source tier, questions this Deep Study's own `Gx2`/`Gx5` pilots addressed at documentation tier only |
| 3 | Invoicing basis, credit note/return, customer-payment/reconciliation handoff | `SOL-11`/`12` (`qty_to_invoice` branches on `invoice_policy` — the entire order-vs-delivery billing mechanism), `SOL-08`–`10` (`qty_invoiced` vs. `qty_invoiced_posted`, not interchangeable), `SRET-02`/`04`–`08` (**no Sale-side Return feature exists at all** — closes that track's own Phase 2 open question) | **Carry-forward** | Item 3 (no Sale-side Return) is a material, test/grep-confirmed negative finding this session's own method (public WebSearch of generic Odoo docs) could not have produced with equal confidence, since it depends on this specific codebase's actual absence of a feature, not a documented behavior |
| 4 | Approval/role/data-scope, optionality, exception, cross-module controls | `SO-43`/§08 item 1 (two-level manager-approval DB schema — **CLOSED** via `CORR-003` dump forensics, identified as 3 real installed modules); `CANC-04`/`05`/`08`/`13`/`14`/`17` (cancellation spares done pickings, test-confirmed); Phase 1's Company/Branch (`CO-*`) | **Carry-forward** | The approval-schema closure specifically required row-level DB dump forensics (`CORR-003`) — a method this session has no access to and could not reproduce |

**Result: 0 new or materially-changed Function-IDs added to the current STATE03 register for Sales this round.** Every one of Boss's 4 priority areas is already covered, at a strictly higher evidence tier (source-code + DB, in several cases test-confirmed) than this session's own WebSearch-documentation ceiling. Per the delta-first rule, this session **does not restart, copy, or create a competing Sales register** — the above table is retained here as the pointer/classification record, and the existing track's own files remain the evidence of record.

## Items classified `OUT OF CURRENT ACCESS / DEPENDENCY` (not a global hold)

The referenced track itself carries a small number of still-open items relevant to Sales that require the **same** source/DB access this session also lacks (not resolvable by WebSearch of public Odoo documentation, since several are SMEsPlus-specific custom-module or dump-forensics questions):

- `stock.picking.action_cancel()`'s exact cascade behavior (referenced from `CANC-17`'s own Unknown).
- Owning module of `sale_order_line.is_service` and related unexplained columns (`project_id`, `task_id`, `fsm_lot_id` — likely `sale_project`/`industry_fsm`/`sale_timesheet`, not opened by that track either).
- `qty_to_deliver`'s over-delivery sign/clamping behavior.
- `res.partner` multi-brand/HQ orphaned columns (that track's own High #5) and the two uncoordinated Thai "branch" modules (High #8) — both flagged there as resolvable only by the same dump-forensics technique used for the (now-closed) approval-schema question, not by this session's method.

Per Boss's instruction, these are recorded as `OUT OF CURRENT ACCESS / DEPENDENCY` and are **not treated as a global hold** — this session continues to the next unrelated `READY` function rather than waiting on them. No source/DB evidence is simulated or guessed for any of them.

## Non-negotiable checks performed

- No competing Sales universe/register/denominator created.
- No restart of the referenced track's own research.
- No Formal Coverage, Gate PASS, or Team B/Functional Design authorization claimed anywhere in this document.
- Status remains `CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION`.

## Follow-on rollup check — Purchase and Inventory (2026-09-29, same day, per "continue with the next unrelated READY function")

Rather than leave the §Conclusion's original hedge ("very likely true of Purchase and Inventory") unverified, this session read the rollup indexes (not full line-level detail, given the Sales table above already establishes the pattern) of `02_INVENTORY_CAPABILITY_MODEL.md` (Phase 2) and `04_PURCHASE_CAPABILITY_MODEL.md` (Phase 4):

| Priority area (from Boss's Sales list, extended) | Existing coverage | Classification |
|---|---|---|
| Inventory — Movement, Reservation/Quantities, Picking/Transfer, Backorder, Return, Lot/Serial, Package, Replenishment, Put-away (9 concepts, Phase 2 rollup) | Full `stock.move`/`stock.move.line`/`stock.quant`/`stock.picking` state-machine evidence, source-code+DB tier | **Carry-forward** |
| Purchase — PO lifecycle (5 states), confirmation dispatch, real amount-threshold approval gate (test-confirmed), the orphaned two-level approval schema (cross-model, closed via `CORR-003`), Purchase Request/Requisition, receipt/billing-gate dispatch, return-to-vendor, backorder, dropship (13 concepts, Phase 4 rollup) | Same tier, same track | **Carry-forward** |

**Confirmed, not merely hedged**: Sales, Purchase, and Inventory — 3 of Boss's 6-item core-module priority order — are all fully Carry-forward from `GROUP_01_SALES_INVENTORY_PURCHASE`, at a strictly higher evidence tier than this session can produce via WebSearch. No new Function-ID added for either. This is rollup-level confirmation (concept-list match), not the same exhaustive per-ID table as the Sales section above — if Boss or `CHATGPT_AUDIT` needs line-level delta-intake detail for Purchase/Inventory equal to the Sales table, that is flagged here as not yet done, not silently assumed equivalent.

## Follow-on check — O2C/P2P cross-module reconciliation (2026-09-29, same day)

`05_INTEGRATED_E2E_LIFECYCLE_MAP.md` (Phase 5) assembles 12 governance-required E2E scenarios (Buy→Receipt→Stock→Sell→Reserve/Fulfill→Deliver read in full for Scenario 1) strictly from Phases 1–4's already-cited evidence IDs plus a small targeted gap-closure pass (`RULE-*`/`SLID-*` for `stock.rule`/MTO-dropship chaining). Evidence status is stated explicitly per step, with genuine gaps (e.g., the exact `make_to_order` re-trigger call site) marked `EVIDENCE_MISSING` rather than assumed. **Classification: Carry-forward.** This closes priority #6 (O2C/P2P) — also fully covered, same track, same tier.

## Conclusion

Per this delta intake, **5 of Boss's 6 core-module priorities are fully Carry-forward** from `GROUP_01_SALES_INVENTORY_PURCHASE` (Sales #2, Purchase #3, Inventory #4, O2C/P2P #6) or `DOMAIN_01_ACCOUNTING_CORE` (Accounting #5, separate track/gate, not duplicated or re-checked in line-level detail this round) — all at a strictly higher evidence tier (source-code + DB, several test-confirmed) than this session's own WebSearch-documentation ceiling. Priority #1 (Shared Master Data) is 3-of-4-functions Carry-forward via the same track's Phase 1, with `SMD-F04` (Access Rights/Groups) as this session's one confirmed-genuine contribution. **No new or materially-changed Sales/Purchase/Inventory/O2C-P2P Function-ID is added to the STATE03 register this round** — every priority area already has a higher-tier answer of record, cited here by pointer. Per Boss's own instruction ("do not treat it as a global hold... continue with the next unrelated READY function"), and because no further unrelated READY function within this session's own genuine-evidence-tier authority currently exists inside the core-module priority order, research reach naturally returns to whatever the next Boss-designated or self-selected genuinely-new-scope item is (M2 Quality's own remaining items, once Manufacturing/optional priority is reached, or a further Wave 0/1 item not yet delta-checked).
