# A16 — Accounting × Inventory Cross-Proof Input Pack

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Provide Inventory-side evidence inputs for the 10 mandatory Lane C Cross-Proof scenarios (Roadmap §6) | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending); Cross-Proof itself is a separate, later, mandatory backbone gate | INPUT PACK ONLY — not the Cross-Proof itself | Feeds `LANE C — Accounting x Inventory Cross-Proof — MANDATORY BACKBONE GATE`; does not substitute for it |

This is **not** the Cross-Proof. Per the Roadmap (§6/Lane C), the Cross-Proof is a separate, later, controlled-teams-plus-independent-verification exercise. This document assembles the Inventory-side evidence each of the 10 mandatory scenarios will need, drawn from A3–A13.

| # | Scenario | Inventory-side evidence available | Accounting-side evidence needed (not provided here) | Readiness |
|---|---|---|---|---|
| 1 | Stockable Purchase Receipt → Stock Truth → Valuation Handoff → Accounting effect | A8 §2 (receipt handoff), A9 §4 (`_set_value()` on `is_in` moves, `_create_account_move()`) | Confirmation that the resulting `account.move` posts to the correct Thailand-COA accounts | **Inventory side ready**; Accounting side pending |
| 2 | Stockable Sales Delivery → Stock Truth → Cost/Valuation Handoff → Accounting effect | A8 §1 (delivery handoff), A9 §4 (COGS via `_run_fifo()`/standard cost, anglo-saxon COGS lines) | Same as above, plus AR/revenue-recognition timing alignment | **Inventory side ready**; Accounting side pending |
| 3 | Return/Reversal → Stock reversal → Financial correction/reversal interface | A4 §6 (return mechanism, `origin_returned_move_id`), A9 §2 (`value`/`value_manual` recompute on the return move) | Confirmation of how a reversal `account.move` relates to the original posting (credit-note vs. reversing entry) | **Inventory side ready**; Accounting side pending |
| 4 | Inventory Adjustment → Quantity difference → controlled financial interface | A7 (adjustment mechanism, `inventory_diff_quantity`) — **PARTIALLY VERIFIED**, exact posting method not traced (N-A7-02) | Confirmation of which account absorbs adjustment variances | **Inventory side PARTIAL** — N-A7-02 should be closed before this scenario is executed with full confidence |
| 5 | Partial Receipt/Partial Delivery → quantity and financial timing consistency | A3 §5, A4 §6, A8 §5 (backorder mechanics, all three domains) | Confirmation of partial-invoice timing rules | **Inventory side ready**; Accounting side pending |
| 6 | Period/Cut-off → Inventory physical date vs. Accounting effective/recorded date | **`RESOLVED` (CORR-005, 2026-09-01)** — `stock/models/stock_move.py:28-31,149,193` date fields + `stock_account/models/stock_picking.py`'s `_is_date_in_lock_period()` lock-period constraint, verified by IER-003; originally `EVIDENCE_MISSING` (N-A7-03/N-A9-02, not traced this pass) | Accounting's own period-lock mechanism | **Inventory side ready** (was: NOT READY) |
| 7 | Manufacturing Raw Material consumption → WIP/production fact → Finished Goods → financial valuation interface | A8 §3 (full MRP handoff trace, `_post_inventory()`) | Confirmation of WIP account treatment | **Inventory side ready**; Accounting side pending |
| 8 | Stockable vs. Consumable vs. Service routing proof | A5 §4 (full `type`/`is_storable` gating chain, three independent code-path confirmations) | Confirmation of financial-effect routing for non-stockable classes (Roadmap §4 table) | **Inventory side ready — this is the most thoroughly evidenced scenario in this pack** |
| 9 | Multi-company/Tenant isolation at Inventory-to-Accounting handoff | A10 (risk register); enforcement mechanism **`VERIFIED WITH CONDITIONS` (CORR-005, 2026-09-01)** — comprehensive company-scoped `ir.rule` enforcement confirmed in `stock/security/stock_security.xml`, verified by IER-003; originally `EVIDENCE_MISSING` (N-A13-02) | Accounting's own company-scoping enforcement | **Inventory side ready; Accounting side still pending** (was: NOT READY — enforcement mechanism unverified on both sides) |
| 10 | Reconciliation identity/provenance from Stock Fact to Financial Fact | A9 §2/§6 (`account_move_id` link), A13 §9 (invariant candidate, not independently tested against data) | Accounting's own trial-balance reconciliation process | **Inventory side evidenced but not independently tested against real data (DB restore blocked)** |

## Summary

Original DR-002 (2026-08-31) disposition: 6 of 10 scenarios had Inventory-side evidence ready; 1 (#4) was partial; 2 (#6, #9) were genuinely not ready; 1 (#10) had evidence but lacked empirical test confirmation.

> **CORR-005 update (2026-09-01)**: Scenarios #6 and #9's Inventory-side gaps are now closed per IER-003 (see rows above). **8 of 10** scenarios now have Inventory-side evidence ready; **1 (#4)** remains partial (N-A7-02, out of the five-High scope, unchanged); **1 (#10)** still has evidence but lacks empirical test confirmation (DB restore was blocked for TEAM A's own pass; IER-003's own restore is not treated as re-opening this Team-A-scoped empirical test per DELTA-FIRST). Accounting-side evidence for scenarios #1, #2, #3, #5, #6, #7, #9 remains pending regardless — this pack supplies Inventory-side evidence only; the Cross-Proof itself is a separate, later, mandatory gate that this reconciliation does not execute or authorize.

No Accounting internals, posting rules, or GL/COA structure are designed or invented in this pack — it assembles Inventory-side evidence only, per the authority boundary restated throughout A9.

No Evidence = No Progress. No Backbone Reconciliation = No Dependent Design Freeze.
