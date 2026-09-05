# G01-P01 CONTROLLED RESEARCH SCOPE FREEZE — CLOSURE PACKAGE (frozen for targeted challenge)

Baseline `a02ec8b`. This is NOT a new research round. It freezes the CURRENT RESEARCH SCOPE against CURRENT
EVIDENCE, reconciles deltas, and routes unresolved facts to owners. It is NOT Final Freeze, NOT PASS, NOT
merge authority, NOT design approval. Boss may reopen on Material Delta.

## C-1 THE CLAIM UNDER CHALLENGE
> Broad P01 research can safely stop now. No further whole-estate source/database sweep from P01 is justified
> without Material Delta.

Support offered: six rounds executed; the series-16 deployment (the only one with real accounting history,
183,590 journal entries) has been read; source and deployment have been reconciled same-generation on series
16, 18 and 19; the remaining questions are owned by other processes or need external/statutory evidence.

## C-2 WHAT SURVIVES (authoritative)
- Receipt→valuation→GL executes in series 16: **57,863 of 74,982** layers linked; policy is a genuine mixed
  population (15 of 30 categories `real_time`); coverage control 0 of 74,982 unresolved.
- GRNI account 39 `2900000`: **13,666 POSTED items, posted-only net −฿7,048,692.08**. (All-states
  ฿72,097,814.25 WITHDRAWN.) `reconcile='f'` — a swept suspense account, not an item-matched bridge.
- Correction is immutable reversal: 5,115 pairs, 0 unresolvable originals.
- No period lock of any kind on 169,143 posted entries.
- AP 97.89% reconciled; open residual splits posted −฿98,745,661.71 / cancelled −฿18,153,699.21 /
  draft +฿13,382,674.68.
- WHT: 5,201 certificates; a rate record **named `WHT3%` valued `0`** used by 2,038 payments, with
  ฿21,556,228.06 posted after it was zeroed — amounts hand-entered, not computed.
- Cost-explosion root cause is **`purchase_stock/models/stock_move.py::_get_price_unit`** — no zero-guard on
  `remaining_qty`, unsigned `invoice_lines` summation, no cancelled-bill filter; entry condition
  `qty_invoiced > qty_received`. **P01's own path. Conditions live.**

## C-3 WITHDRAWN / SUPERSEDED (lineage preserved, nothing deleted)
| Withdrawn | Now |
|---|---|
| GRN net ฿72,097,814.25 | all-states; posted-only **−฿7,048,692.08** (opposite sign) |
| "price-difference engine never fired" | it fires; see C-4 |
| Residual B = 1,209 policy violations | bill-created price-difference layers (1,194 have no stock move) |
| "policy change refuted by time distribution" | the change happened; `ir_property` cannot see reverted rows |
| "the general ledger is intact and sane" | 8 posted items > ฿1bn; ฿39.2m misallocated WIP/Semi Product |
| cost explosion owned by P03 | owned by **P01** |
| BE leakage = 30 rows in one column | materially wider; extent disputed between experts |

## C-4 ACCOUNT 1173 — CLOSED ON EVIDENCE
`purchase_price_diff 16.0.1.1` **is installed**. Gate at `models/account_move_line.py:10` is
`if self.product_id.cost_method == 'standard':`. The only `product.category` configuring account 1173 is
category 10, whose `property_cost_method` is **`fifo`**. Independently the caller returns early on
`not company_id.anglo_saxon_accounting`, and that flag is **FALSE**. **Two sufficient gates — an empty 1173
proves nothing.** (6 further configured rows exist at `product.template` level.)

**Inverted exposure:** purchase price differences are **capitalised into inventory** and **no
purchase-price-variance line reaches the P&L** in the observed path.

## C-5 THE 1,123 vs 1,267 COUNT — RESOLVED THIS RUN
| Count | UNIT | PREDICATE | POPULATION |
|---|---|---|---|
| **1,267** | one valuation layer | `price_diff_value` **IS NOT NULL** (includes 0.00) — *the engine fired* | all 74,982 layers |
| **1,123** | one valuation layer | `price_diff_value` **non-zero** — *the correction was material* | all 74,982 layers |

**1,267 − 1,123 = 144** layers where the engine ran and produced exactly ฿0.00. **Both counts are correct and
measure different things. Not forced, not averaged.**

## C-6 `purchase_mrp` KIT GAP — LATENT HERE
`purchase_mrp 16.0.1.0` (installed) overrides `_get_stock_valuation_layers` to filter layers to the bill
line's own product, with the source comment *"Do not handle the invoice correction for kit. It has to be done
manually."* **Latent in this deployment**: 983 BoMs all `type='normal'`, zero phantom BoMs, **0 of 10,490 PO
lines reference a kit.** Routed to **P03** for environments where kits are used. **No conclusion is implied
for deployments not measured.**

## C-7 THE HIGHEST-RANKED OPEN ITEM — `S16-B-05`
`stock_valuation_layer.account_move_id` is **`ON DELETE SET NULL`** (schema-verified; controls: 584 CASCADE /
1,741 SET NULL present). `om_data_remove 16.0.1.0.1` is **installed** and performs raw `DELETE` + `commit()`
— no ORM, no lock check, no company filter, no log. **A journal-entry deletion reproduces the "0 of N linked"
signature P01 published for series-18 (0 of 47,801) and series-19 (0 of 14,441).** Neither finding is
overturned — series-18's periodic policy was proved positively — but **the alternative was never excluded.**
Owner: **P06 + P11.**

## C-8 METHOD CONTROL FOR DOWNSTREAM
**An installed module that modifies a writer's INPUT can materially change behaviour without being a writer.**
`purchase_mrp` alters what `_prepare_in_invoice_svl_vals` receives while containing no assignment to
`account_move_id`. A writer enumeration scoped to writers is correct and **not sufficient**.

## C-9 KNOWN LIMITS OF THIS PACKAGE
- **41 of 651 tables extracted (6.3%)**, no stated selection rule (`GAP-P01-07`). Every negative is bounded by this.
- The round-5 "freeze" was declared and not enforced — 15 files entered during review (`NEAR-MISS-P01-09`).
- Nothing has been executed at runtime in any of six rounds.
- Statutory questions: none answered; six routed to P07.
- Two expert disagreements preserved: BE-leakage extent; certificate/payment gap denominators.
