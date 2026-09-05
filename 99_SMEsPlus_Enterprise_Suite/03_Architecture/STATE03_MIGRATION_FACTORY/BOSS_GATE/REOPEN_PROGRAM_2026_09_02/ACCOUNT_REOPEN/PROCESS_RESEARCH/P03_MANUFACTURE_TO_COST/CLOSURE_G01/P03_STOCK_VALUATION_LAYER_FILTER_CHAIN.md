# P03 — STOCK VALUATION-LAYER FILTER CHAIN

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-02`. Bounded to the declared participant path.
No addon-tree sweep.

---

## 1. Search clamp, logged before execution

| Field | Value |
|---|---|
| CQ | `CQ-P03-02` |
| Purpose | enumerate every participant in the filter chain, and establish whether **manufacturing participates** |
| Population | `def _get_stock_valuation_layers` across the series-18 and series-19 addons roots; and separately every `mrp*` module |
| Unit | one method definition |
| Stop | participant list complete per series; `mrp*` participation settled |

## 2. The chain, per series — executed

| Series | Participants | Source |
|---|---|---|
| **16** | **3** — `stock_account` (base) · `stock_landed_costs` · `purchase_mrp` | **P01**, direct read |
| **18** | **3** — `stock_account/models/account_move.py:294` · `stock_landed_costs/models/account_move.py:80` · `purchase_mrp/models/account_move.py:10` | **P03**, this round |
| **19** | **0** — `purchase_mrp/models/account_move.py` **does not exist**, and `stock_account/models/account_move.py` contains **no** `stock_valuation_layer` reference at all | **P03**, this round |

**Positive control for the series-19 zero:** the v19 root holds **1,427 modules**,
`stock_account/models/account_move.py` **exists**, and a `_cal_price` probe on the same tree
returns 2 hits. The zero is a real absence, not a broken test.

**A wording correction this file made to itself after challenge (`CC-02`).** The first draft
said the mechanism was *"removed"* in series 19. **It was restructured, not removed.** The
price-difference *concept* survives — `property_price_difference_account_id` is still declared
on the product category (`stock_account/models/product.py:38, 159, 670`). What is gone is the
**`_get_stock_valuation_layers` filter-chain implementation** and its participants. Saying
"removed" would have told a reader the correction no longer exists, which is false.

> **Two sessions, two series, the same three participants.** P03 reproduced P01's series-16
> chain shape in series 18 without having read P01's method. This is independent
> corroboration of the chain's structure.

## 3. Does manufacturing participate? — the P03-side question

> **NO. No `mrp*` module defines `_get_stock_valuation_layers` in either available series.**

Applying the method control P01 handed over — *an installed module that modifies a writer's
INPUT can change behaviour without being a writer* — P03 checked participation, not
authorship. Manufacturing does neither: it **neither writes** the correction **nor filters**
its input.

**Consequence:** the price-difference correction mechanism, its unconditional product-mismatch
filter, and its 13 live dropped rows are **entirely outside P03's boundary**. P01 retains
them, correctly.

## 4. The kit question P01 hands P03 — disposed

> *Where phantom BoMs exist, does the kit purchase price difference reach RM/WIP/FG cost at
> all, and is the "manual" correction a defined procedure or an assumption in a comment?*

**Part 1 — is it a defined procedure?** No. The whole of the module's stated handling is a
two-line docstring — *"Do not handle the invoice correction for kit. It has to be done
manually"* — and P01 established that the code beneath it contains **no kit predicate at
all**. There is **no procedure, no wizard, no report, no flag and no reconciliation surface**
naming a manual correction. `FACT VERIFIED` (series 18, read directly; series 16 per P01).

**Part 2 — does it reach RM/WIP/FG?** **Not in any examined deployment**, and for a reason
that does not depend on the filter:

| Control | Result |
|---|---|
| Moves with `bom_line_id` **and** `purchase_line_id` — the receipt-time kit fingerprint | **0** (P01, history-visible) |
| Done purchase moves whose product ≠ PO-line product | **0 of 13,297** (P01) |
| Phantom BoMs in `iSMEs` | **0 of 983** (P01, current-state) |

**No kit has ever been purchased in the deployment.** So the kit branch of the question is
**unreachable in evidence**, and the general branch belongs to P01.

**Disposition:** `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE` for part 1;
**`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** for part 2, because no deployment has ever
purchased a kit and none can be constructed read-only.

**P03 does not re-run the kit census on the series-18/19 deployments** as P01 suggests. Those
deployments hold **10 journal entries** and **32 GL lines** respectively; a census there
cannot produce material evidence, and running it would spend the round on a corroborative
path. Recorded as a rejected delta in `P03_MATERIAL_DELTA_REGISTER.md`.

## 5. Dropped layers — can any be reintroduced?

**No.** Both overrides are `.filtered()` narrowings of their super's result, so:

- narrowings **commute** — MRO order cannot change the final set;
- a narrowing **cannot reintroduce** a dropped element;
- there is **no fourth participant** in series 16 or 18.

P01 established this; P03 re-derived the participant list independently and reaches the same
structural conclusion. **A layer dropped by the product-mismatch filter is dropped for good.**

## 6. Landed-cost participation

`stock_landed_costs` drops landed-cost layers from the correction. P03 measured
`stock_landed_cost` = **0 rows** in both manufacturing databases, so it is **inert in
evidence** — and it is **live wherever landed costs are used**, which P03 carries forward
rather than dismissing.

## 7. Disposition

> **`CQ-P03-02` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, with the boundary that the
> chain itself is **P01-owned** and the series-16 reading is P01's, not reproducible in P03's
> path set (`MD-01`, `MD-06`).
>
> **P03's own answer is a clean negative: manufacturing is not a participant in this chain,
> in either available series.**
