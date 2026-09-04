# 15 — P03 CROSS-INVENTORY RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.** Very Expert extension: *Cross-Inventory Reconciliation*.

---

## 1. The three quantities that must agree

For manufacturing, three independent measures of the same economic reality exist:

| # | Measure | Source |
|---|---|---|
| **A** | Sum of valuation-layer values for the MO's moves | Inventory valuation |
| **B** | Net movement on the production account | General ledger |
| **C** | Analytic cost attributed to the MO | Analytic accounting |

## 2. Do they agree?

| Pair | Agree? | Reason |
|---|---|---|
| **A vs B** | **No** | B additionally carries the `_post_labour` entry and both residues from `DC-03` / `DC-04`. A carries only what became inventory value |
| **B vs C** | **No** | C uses a different duration **and** a different cost content — `DC-05`. Also C exists only in part: employee analytic is inert without the Project bridge — `DC-10` |
| **A vs C** | **No** | Transitively, and additionally because C is signed negative by construction (`mrp_account/models/mrp_workorder.py:46`) while A is a valuation |

**None of the three pairs reconciles.** `FACT VERIFIED`.

## 3. Why this matters more than it appears

The reference product provides a reconciliation surface — `action_view_stock_valuation_layers`
(`mrp_account/models/mrp_production.py:30-38`) shows the MO's raw, finished and scrap
layers together. It reconciles **A to itself**. It does not touch B or C.

> The only reconciliation view offered is over the one measure that was never in doubt.

`FACT VERIFIED`.

## 4. Boundary with the Inventory track — what P03 does not claim

Inventory valuation method behaviour, tenant isolation of valuation, and the 50 invariants
of `smeplus-inventory-mt-invariant-set-status` are **owned by the Inventory track**. P03
asserts nothing about them.

What P03 asserts is narrower and is its own: **measure A is an input to P03 and an output
of Inventory, and P03 consumes it without re-deriving it** —
`mrp_account/models/mrp_production.py:54` sums
`consumed_moves.sudo().stock_valuation_layer_ids.mapped('value')` and does no valuation of
its own on the input side.

That is the correct dependency direction and P03 records it as sound. It is the one
structural thing in the reference manufacturing cost model that this session found
unambiguously right.

## 5. The `sudo()` observation

`mrp_account/models/mrp_production.py:54` and `:92` both use `sudo()`.

- At `:54`, to read valuation layers the acting user may not have access to.
- At `:92`, to create the labour journal entry.

Both are defensible — costing must not depend on the operator's ledger rights. **But
`:92`'s `sudo()` combines with `DC-11`'s missing company context**: an elevated create,
with accounts resolved in the wrong company, and no record rule to stop it.

`SUPPORTED INTERPRETATION`: the two defects compound. The `sudo()` alone is not a finding;
the pair is, and it is recorded as raising `DC-11`'s severity to Critical rather than as a
separate item.

## 6. Reconciliation queries handed to Core Accounting

These are the five queries `24_P03_CORE_RECON_HANDOFF_PACK.md` §4 carries forward. They are
listed here with the finding each is designed to detect:

| ID | Query | Detects |
|---|---|---|
| `RQ-01` | Production-account balance by company and period, decomposed by MO | `DC-03`, `DC-04`, and their netting — `10` §4 |
| `RQ-02` | Labour absorption entries whose credit account is a COGS account | `DC-07` |
| `RQ-03` | Labour entries whose date differs from the MO's finished-move date | `DC-09` |
| `RQ-04` | Work orders whose costed hours exceed their overlap-merged hours | `DC-01` |
| `RQ-05` | Journal entries whose company differs from the originating MO's company | `DC-11` |

**No result for any of these is inferred, estimated or assumed anywhere in this package.**
