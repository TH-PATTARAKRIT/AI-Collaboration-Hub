# P04 → P05 HANDOFF (Expense-to-Pay)

**LAYER 2.** Published, not executed. **P04 does not research P05.**

| # | Evidence | Question for P05 | Materiality |
|---|---|---|---|
| 1 | `maintenance` models contain **zero** references to `account.move` or `account.analytic`; the only cost carrier is one `Float` on the equipment | When a repair is paid as a vendor bill, does anything connect that expense back to the equipment it repaired? **P04 asserts only that the asset/maintenance side has no link** | **High** — it is the whole cause side of the Boss's non-productive attribution policy |
| 2 | Equipment is created by **validating a goods receipt** for a product flagged *Is Equipment* (`consu`, serial-tracked). No asset, no depreciation | How is that receipt expensed, and under which account? P04 establishes only that the asset engine is not involved | **High** — determines whether `P04-F-151` double-counting is reachable |
| 3 | `P04-F-151`: nothing tests whether the value behind an asset↔equipment link was already expensed | Does P05 have a control that would catch expense-then-capitalise? | **High** |
| 4 | `P04-F-149`: the equipment status transition `eqp → tass` has **no reverse anywhere**; disposal of the asset does not release the equipment | Who owns a stranded equipment record after the asset is disposed? It is a maintenance-owned object left in a terminal state | **Medium** — operational, not ledger |

**P04 asks nothing to be decided.** These are P05's to answer or decline.
