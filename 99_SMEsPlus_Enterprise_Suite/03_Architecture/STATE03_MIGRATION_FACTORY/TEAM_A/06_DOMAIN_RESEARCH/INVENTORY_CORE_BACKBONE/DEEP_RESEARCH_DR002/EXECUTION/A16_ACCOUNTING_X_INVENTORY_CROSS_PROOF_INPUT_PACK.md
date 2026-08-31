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
| 6 | Period/Cut-off → Inventory physical date vs. Accounting effective/recorded date | **`EVIDENCE_MISSING` — N-A7-03/N-A9-02, not traced this pass** | Accounting's own period-lock mechanism | **NOT READY — this is the single most material gap blocking full Cross-Proof readiness; must be closed before scenario 6 is executed** |
| 7 | Manufacturing Raw Material consumption → WIP/production fact → Finished Goods → financial valuation interface | A8 §3 (full MRP handoff trace, `_post_inventory()`) | Confirmation of WIP account treatment | **Inventory side ready**; Accounting side pending |
| 8 | Stockable vs. Consumable vs. Service routing proof | A5 §4 (full `type`/`is_storable` gating chain, three independent code-path confirmations) | Confirmation of financial-effect routing for non-stockable classes (Roadmap §4 table) | **Inventory side ready — this is the most thoroughly evidenced scenario in this pack** |
| 9 | Multi-company/Tenant isolation at Inventory-to-Accounting handoff | A10 (risk register); enforcement mechanism itself `EVIDENCE_MISSING` (N-A13-02) | Accounting's own company-scoping enforcement | **NOT READY — enforcement mechanism unverified on both sides** |
| 10 | Reconciliation identity/provenance from Stock Fact to Financial Fact | A9 §2/§6 (`account_move_id` link), A13 §9 (invariant candidate, not independently tested against data) | Accounting's own trial-balance reconciliation process | **Inventory side evidenced but not independently tested against real data (DB restore blocked)** |

## Summary

**6 of 10** scenarios have Inventory-side evidence ready for the eventual Cross-Proof exercise; **1 (#4)** is partial; **2 (#6, #9)** are genuinely not ready and are the two highest-priority follow-up items this DR-002 pass identifies for whoever executes the Cross-Proof; **1 (#10)** has evidence but lacks empirical test confirmation. This mirrors A15's overall `HOLD` disposition — the Cross-Proof itself cannot be claimed ready to execute with full confidence until N-A7-03/N-A9-02 (timing/cutoff) and N-A13-02 (tenant-isolation enforcement) are closed.

No Accounting internals, posting rules, or GL/COA structure are designed or invented in this pack — it assembles Inventory-side evidence only, per the authority boundary restated throughout A9.

No Evidence = No Progress. No Backbone Reconciliation = No Dependent Design Freeze.
