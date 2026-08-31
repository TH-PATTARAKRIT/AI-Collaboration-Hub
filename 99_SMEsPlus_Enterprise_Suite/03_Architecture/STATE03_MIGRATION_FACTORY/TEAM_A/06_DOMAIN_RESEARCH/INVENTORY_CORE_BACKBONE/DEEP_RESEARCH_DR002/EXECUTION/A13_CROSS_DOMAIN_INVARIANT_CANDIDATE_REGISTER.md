# A13 — Cross-Domain Invariant / Future Test Candidate Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Create evidence-backed invariant candidates for later design/testing (not test execution) | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (source-based candidates) | Feeds future EXPERT IDTM test-matrix design; no test execution performed here |

These are **research candidates**, not proven SMEsPlus invariants and not executed tests, per DR-002 §7/A13 and the Project Constitution's IDTM boundary (Team A may identify candidates; only EXPERT IDTM executes formal test matrices).

## 1. Quantity conservation

**Candidate**: `on-hand(t) = on-hand(t-1) + Σ(done moves into location) − Σ(done moves out of location)`, evaluated per `(product, location, lot, package, owner)` bin.
**Evidence for**: `stock.move.line._synchronize_quant()` is the single choke point for all quant mutation (A3 §6) — no other code path was found that mutates `stock.quant.quantity`.
**Evidence against enforcement**: no DB CHECK constraint or trigger enforces this — it is a property of the application code always calling through the one choke point, not a database-guaranteed invariant (A2, A10 SAAS-03).

## 2. No unauthorized stock mutation

**Candidate**: `stock.quant.quantity`/`reserved_quantity` should only change via `_synchronize_quant()`/`_update_reserved_quantity()`.
**Evidence for**: confirmed as the only mutation paths found in the `stock`/`stock_account` models read this pass.
**Evidence against enforcement**: any direct SQL write (or a future ORM method this research did not read) could bypass this — not database-enforced (same gap as #1).

## 3. No duplicate movement effect from replay

**Candidate**: re-running a confirm/procurement/receipt operation on an already-processed record should not create a second physical movement effect.
**Evidence for**: multiple quantity-remaining-based guards exist across Sale, Purchase, and the rule-dispatch layer (A6 §5) — `_action_confirm()`'s `if state != 'draft': continue`, `_get_qty_procurement()` guards, and search-before-create at `_run_buy()`/`_run_manufacture()`.
**Evidence against**: **no unified idempotency-key mechanism exists** — every guard is a quantity-remaining computation, which is not mathematically equivalent to a hard idempotency guarantee under all possible concurrent-retry interleavings. This candidate is therefore `PARTIALLY SUPPORTED`, not `VERIFIED`.

## 4. On-hand derived consistently from executed stock facts

**Candidate**: `product.qty_available` should always equal the sum of `stock.quant.quantity` for that product across all locations in scope.
**Evidence for**: `qty_available`'s compute depends on `stock_move_ids.product_qty/.state/.quantity`, i.e. it is derived from the same move data that also drives quant mutation.
**Evidence against enforcement**: `product.qty_available` has an **inverse** (`_inverse_qty_available`) allowing direct manual edits (A3 §2) — a real, source-confirmed path where the derived-looking field can itself trigger a write, which is architecturally unusual and worth flagging for any future test design (which side is "source of truth" in that moment is not obvious without reading the inverse method's exact body, which this pass did not do in full — registered as N-A13-01 in A14).

## 5. Tenant/company isolation

**Candidate**: no Inventory record should be readable/writable across `company_id` boundaries without explicit multi-company sharing configuration.
**Evidence**: `company_id` is the only scoping field on `stock.move` (A10 SAAS-01) — this candidate cannot be verified as *enforced* from source reading alone (record-rule/ACL definitions were not read this pass); registered as **`EVIDENCE_MISSING — RECORD RULES NOT YET READ`** in A14 (N-A13-02), not assumed either way.

## 6. Lot/serial product consistency

**Candidate**: a `stock.move.line` for a tracked product should always carry a lot/serial matching the product's own `tracking` setting.
**Evidence for**: `has_tracking` is a related field mirroring `product_id.tracking` directly on `stock.move` — the data model makes the relationship explicit and readable, suggesting (not proving) the application enforces consistency.
**Evidence against enforcement**: no DB constraint found; not independently tested against dump data (A2 restore blocked).

## 7. No impossible state transitions

**Candidate**: a `stock.move` should never move backward through its state machine (e.g. `done` → `assigned`) except via the explicit cancel/return/backorder-split mechanisms.
**Evidence for**: every transition method read this pass (`_action_confirm`, `_action_assign`, `_action_cancel`, `_action_done`) only ever advances state forward or to `cancel`; no method was found that resets a `done` move's state directly (consistent with A4 §6's "no un-confirm" finding).
**Evidence against**: not exhaustively verified against every method in `stock_move.py` (2,200+ lines; this pass read the state-machine-relevant methods specifically, not every method in the file).

## 8. Cross-domain handoff provenance

**Candidate**: every `stock.move` generated from a commercial document should carry a traceable link back to that document (`sale_line_id`, `purchase_line_id`, `raw_material_production_id`/`production_id`).
**Evidence for**: confirmed present on all three integration modules read this pass (A8).
**Evidence against**: `_merge_moves()` can combine multiple originating moves into one record (A4 §2, GROUP A MOV-40) — meaning cardinality between a commercial line and its stock moves is not guaranteed 1:1, a genuine nuance for any provenance-tracing test design.

## 9. Inventory-to-Accounting reconciliation identity

**Candidate**: the sum of `stock.move.value` for all valued, done moves affecting a product should reconcile to that product's Accounting-side stock valuation account balance.
**Evidence for**: `account_move_id` provides the explicit link (A9 §2); `_create_account_move()` is the single choke point creating the journal entry from `stock.move.value` (A9 §4).
**Evidence against enforcement**: this reconciliation was not independently tested against real data this pass (DB restore blocked, A2) — this is exactly Lane C Cross-Proof scenario 10 ("Reconciliation identity / provenance from Stock Fact to Financial Fact"), registered as a mandatory future test, not yet executed.

## 10. GROUP A's own carried-forward "NOT enforced anywhere" findings (reused DELTA-FIRST, independently corroborated this pass)

| Invariant candidate | Enforcement status |
|---|---|
| Delivered/received quantity never exceeds ordered/demanded quantity | **NOT enforced anywhere** — independently re-confirmed this pass by direct reading of `purchase.order.line._compute_qty_received()` (no ceiling), consistent with GROUP A's DB-forensics-corroborated finding |
| Stock quantities never go negative | **NOT enforced anywhere** (no DB CHECK) |
| One row per `(product, location, lot, package, owner)` bin in `stock.quant` | **NOT enforced anywhere** (no unique index; `_merge_quants()` cleans up after the fact) |
| `state` field only holds a declared Selection value | **NOT enforced anywhere** at the DB layer (no DB CHECK/ENUM) |

These four are the strongest, most consequential invariant-gap candidates in the entire register — each independently corroborated by both GROUP A's DB forensics and this pass's own source reading, via two different evidence paths reaching the same conclusion.

No test execution was performed. These candidates are inputs to a future formal test matrix, not a substitute for one.

No Evidence = No Progress. DELTA-FIRST.
