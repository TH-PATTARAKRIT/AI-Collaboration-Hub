# 06 — Residual Count and Severity Recomputation

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Independently recompute open Inventory research blockers; challenge all 21 residual Medium/Low items for severity misclassification | Claude (IDR-007) | This artifact; primary source spot-checks on 3 items | 2026-09-01 | Self | Count recomputation matches CORR-005 exactly; zero items warrant elevation; one item's evidence framing found to be more conservative than reality | No elevation-worthy blocker found — does not change readiness |

## Part A — Count recomputation (not copied)

Recomputed directly from `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` Part 1 + Part 2 (the itemized rows), independently of CORR-005's own arithmetic in the same file's "Mechanical count reconciliation" section.

**Open Inventory research blockers:**

| Severity | Items (independently enumerated by ID) | Count |
|---|---|---|
| Critical | (none open — 3 pre-existing, all re-confirmed resolved) | **0** |
| High | (none — all 5 reconciled to RESOLVED or CONTROLLED CARRY-FORWARD; see file 03) | **0** |
| Medium | GRPA-M11, M12, M13, M14, M15, M16, M18, M19 (8) + N-DB-01, N-CONC-01, N-A7-01, N-A7-02, N-A7-04, N-A12-01 (6) | **14** |
| Low | GRPA-L20, L21, L22, L23 (4) + N-A13-01, N-A5-02, N-A5-03 (3) | **7** |
| **Total** | | **21** |

This independently-enumerated total (**21**, 0/0/14/7) matches CORR-005's own View 1 total exactly (`03_CORR005_RESIDUAL_BLOCKER_AND_CARRY_FORWARD_REGISTER.md` L19). The match was reached by counting the actual ID list twice (once from Part 1's tables, once from Part 2's table) rather than by re-stating the arithmetic already printed in the register.

**Controlled carry-forwards (View 2, not counted above):** 4 rows / 3 distinct items — GRPA-H5(H2) → 1 row, GRPA-H8(H3) → 2 rows, N-A13-02 residual → 1 row. Independently re-counted from the actual table in `03_CORR005_...md` L23-32: confirmed 4 rows.

## Part B — Severity challenge of all 21 open items

Every open Medium and Low item was individually reviewed for whether it should be elevated given its stated impact on: Stock Truth, quantity conservation, reservation integrity, state lifecycle, cut-off, tenant/company isolation, migration continuity, accounting handoff integrity, or clean-room/compliance boundary. The objective was to find real misclassifications, not to manufacture or artificially avoid them.

| ID | Topic | Stated severity | Elevation-relevant factor(s) present? | IDR-007 assessment |
|---|---|---|---|---|
| GRPA-M11 | `returned_move_ids` field never located | Medium | None claimed | Documentation/traceability gap only, no evidence of a conservation or integrity defect. **No elevation.** |
| GRPA-M12 | `produce_line_ids` (MRP) not located | Medium | None claimed | Module-location gap (likely a subcontracting extension not read). **No elevation.** |
| GRPA-M13 | `sale_order_line.is_service` owning module unknown | Medium | None — Sales-domain classification field | Arguably lower than Medium, not higher. **No elevation.** |
| GRPA-M14 | `product.type` literal `'product'` — legacy data question | Medium | **Migration continuity** (possible unmapped legacy value) | Real material factor, but blocked by an *environmental* limitation (DB restore blocked, A2), not by unresolved architecture risk to current Stock Truth. Correctly Medium; flagged as the most migration-relevant open Medium item for Boss's attention. **No elevation — but recommend Migration prioritize this in its own gap-closure queue.** |
| GRPA-M15 | Purchase-order-line unexplained columns, owning module unknown | Medium | None — Purchase-domain, not Inventory-owned | **No elevation.** |
| GRPA-M16 | `stock_dropshipping/models/stock.py` full contents unread | Medium | Possible — dropshipping touches quantity flow | No evidence of an actual conflict/defect was found, only an unread module. **No elevation** — but this is the item this review would most recommend prioritizing in a future Inventory research pass, since dropshipping directly intersects Stock Truth. |
| GRPA-M18 | Thai WHT PND form-code correctness | Medium | None — Accounting/Tax domain, regulatory | **No elevation.** |
| GRPA-M19 | Thai district/sub-district address reaching delivery | Medium | None — delivery/carrier, out of Inventory scope | **No elevation.** |
| N-DB-01 | DB re-verification blocked | Medium | None — explicitly labeled environmental, not a source-evidence gap | **No elevation.** |
| N-CONC-01 | No DB-level row-locking evidence traced for quant reservation | Medium | **Reservation integrity, tenant/company isolation under concurrency** — explicitly named in this item's own SaaS/Tenant Impact column as "High" | **Independently spot-checked against primary source** (see Part C below). Finding: real locking evidence *does* exist in the primary source and is readily discoverable, which the register did not cite. This makes the register's "not traced" framing *more conservative than the actual evidence supports* — if anything this argues toward eventual closure, not elevation. **No elevation** — but see the citation-accuracy note in Part C. |
| N-A7-01 | Count-in-progress freeze state unknown | Medium | **State lifecycle, quantity conservation** during physical counts | Spot-checked (Part C) — inconclusive, no freeze-state field found in the grep performed, consistent with remaining genuinely unresolved. **No elevation**, correctly Medium (uncertain, not confirmed-absent). |
| N-A7-02 | `inventory_diff_quantity` → posted `stock.move` method not traced | Low-Medium | None beyond what's already disclosed (inferred, not confirmed) | **No elevation.** |
| N-A7-04 | Stock freeze/lock beyond count-in-progress unknown | Low-Medium | Same class as N-A7-01 | **No elevation.** |
| N-A12-01 | Cross-year/fiscal-year-boundary continuity unknown | Medium | Migration continuity, accounting handoff | Correctly Medium; requires a joint Accounting session, already disclosed as such. **No elevation.** |
| GRPA-L20/L21/L22 | Extension-module columns (MRP/repair/purchase-req; warehouse; cold-chain) | Low | None | **No elevation.** |
| GRPA-L23 | `num2words` Thai-locale correctness | Low | None — presentation layer | **No elevation.** |
| N-A13-01 | `qty_available._inverse_qty_available()` not read in full | Low | Possible — quantity conservation during manual edits | Standard, well-established Odoo computed/inverse field pattern; DR-002's own materiality column already marks this Low. Spot-check attempted (grep for the inverse method in `stock_quant.py`) found nothing — the method most likely lives in `product.py`/`product_template.py`, not `stock_quant.py`, so DR-002's own file guess may be imprecise, but this does not change the severity call. **No elevation.** |
| N-A5-02 | Expiration-date handling (`product_expiry`) unresearched | Low-Medium | None currently — disclosed as perishable-goods-specific | **No elevation.** |
| N-A5-03 | Owner/consignment workflow unresearched | Low-Medium | None currently | **No elevation.** |

**Result: zero of 21 open Medium/Low items warrant elevation to Critical/High.** No real Critical/High item was found hiding in the residual register.

## Part C — Independent primary-source spot-checks (3 items, performed to inform the challenge above, not merely to trust the register's own "evidence found" column)

1. **N-CONC-01** (row-locking for quant reservation): `grep`'d `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/stock/models/stock_quant.py` directly. Found, at line 1082, inside `_update_available_quantity`: `quant = quants.try_lock_for_update(allow_referencing=True, limit=1)`. This is a genuine row-locking helper call in the actual reservation-adjacent code path. **This is new information this review surfaced that neither DR-002, IER-003, nor CORR-005 cited** — the register's "Not traced (time-boxed scope)" / `EVIDENCE_MISSING` framing for N-CONC-01 is therefore more conservative than what a two-minute grep of the already-authorized primary source shows. This is not a Gate-blocking discrepancy (if anything it argues the concern is closer to answered, not further open), and this review is not authorized to perform new primary research and formally resolve a Medium item outside CORR-005's five-High reconciliation scope — but it is reported here as a citation-accuracy note worth a future Team A follow-up pass.
2. **N-A7-01** (count-in-progress freeze state): grep of `stock_quant.py` found `inventory_quantity_set`, `inventory_diff_quantity`, and `action_apply_inventory` — fields that track whether a count value has been *entered*, but no evidence of a *lock/freeze* preventing concurrent normal stock moves during an active count. Consistent with the item remaining genuinely `EVIDENCE_MISSING` — no correction needed.
3. **N-A13-01** (`_inverse_qty_available`): not found in `stock_quant.py` by direct grep — likely misfiled to the wrong module in DR-002's own citation (product-level field, not quant-level). Noted above; does not change severity.

## Verdict

Residual counts (0 Critical / 0 High / 14 Medium / 7 Low = 21 open blockers, plus 4 carry-forward rows across 3 items) are **independently reconfirmed, correctly classified, and controlled**. No material Critical/High Inventory research blocker was found concealed in the Medium/Low tier.
