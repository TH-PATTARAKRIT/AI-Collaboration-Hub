> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx7)

### MFG-F01 — Raw material consumption → WIP transfer

- **WHAT**: When components are consumed by a manufacturing order, Odoo automatically creates an accounting entry moving their value from the stock valuation account to a WIP account.
- **WHY**: The components physically leave raw-material stock and become part of an in-progress product — their value needs a financial home during that in-between state.
- **BUSINESS RULE**: Automatic — but **only when the product category uses Automated (real-time) valuation**; consistent with Gx1's finding that Manual valuation defers everything to the accounting team instead.
- **STATE**: Component in stock → consumed by MO → value in WIP account.
- **DATA CONCEPT**: WIP account is a distinct ledger account from both the component's stock valuation account and the finished good's valuation account — a genuine three-account chain (component valuation → WIP → finished-good valuation), not a two-account swap.
- **CONTROL**: Requires configured Stock Input/Output/Valuation accounts on the category AND a "Production Account" (the WIP account) set on the Production location.
- **DEPENDENCY**: Feeds MFG-F02.
- **EVENT**: "Component consumed, value moved to WIP."
- **RISK**: If the Production location's Production Account is unconfigured, WIP posting may not occur correctly — not evidenced in detail, but implied by the configuration requirement being explicit.
- **UNKNOWN**: Exact behavior if Production Account is unset — blocked, defaulted, or silently skipped — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### MFG-F02 — Finished goods completion → valuation transfer

- **WHAT**: When the MO completes, value transfers from WIP to the finished good's own valuation account, plus the cost of work-center/labor operations.
- **WHY**: The finished product now exists as its own stockable item with its own cost basis, which must include everything that went into making it.
- **BUSINESS RULE**: "Finished goods usually raise total inventory value: consumed component value is returned to inventory as part of the finished good, plus the cost of the work performed" — i.e., total system-wide inventory value is not conserved across a manufacturing event; it increases by the labor/operations cost added.
- **STATE**: WIP (components' value + accruing labor) → MO marked Done → finished good valued at full cost.
- **DATA CONCEPT**: Finished-good cost = Σ(component costs, each at its own costing method) + Σ(work-center/labor cost).
- **CONTROL**: Same Automated-valuation gating as MFG-F01.
- **DEPENDENCY**: Depends on MFG-F01 and MFG-F04 (cost computation).
- **EVENT**: "MO Done, finished good valued."
- **RISK**: A design assuming manufacturing conserves total inventory value (in = out) would be wrong — value genuinely increases through labor/operations cost.
- **UNKNOWN**: Exact treatment of a *partially* completed MO's finished-good valuation (if any goods are produced before full MO completion) — not evidenced this round.

### MFG-F03 — Manual interim WIP posting/reversal

- **WHAT**: For manufacturing that spans a reporting boundary, users can manually trigger a "Post WIP Accounting Entry" reflecting the real cost of components/work-centers/labor already incurred at that point, and later reverse it.
- **WHY**: An MO that takes weeks might otherwise show zero WIP value on an interim balance sheet if the only automatic postings happen at consumption-start and completion-end.
- **BUSINESS RULE**: This is explicitly a **manual, optional** action distinct from the automatic MFG-F01/F02 postings — not triggered automatically at any interim milestone.
- **STATE**: MO in progress → manual Post WIP action → interim WIP value on the books → (implied) reversed once the MO actually completes and MFG-F02's real transfer occurs, to avoid double-counting.
- **DATA CONCEPT**: A postable-and-reversible interim entry, analogous in spirit to Gx6's period-close accrual (self-cancelling), but manually triggered per-MO rather than automatically at period boundaries.
- **CONTROL**: Requires the same WIP/WIP-Overhead account configuration as MFG-F01/F02.
- **DEPENDENCY**: Independent of, but must reconcile with, MFG-F01/F02's automatic postings.
- **EVENT**: "Interim WIP entry posted" / "reversed."
- **RISK**: If a business relies on this manual action but forgets to trigger it, interim financial statements would understate WIP value for long-running orders — an operational-discipline risk, not a system gap.
- **UNKNOWN**: Whether reversal is itself manual or automatic upon MO completion — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

### MFG-F04 — MO cost computation

- **WHAT**: The MO's total cost is computed from its BOM: component cost × quantity (per each component's own costing method) plus the cost of completing the necessary operations (work-center time, labor).
- **WHY**: Needed as the input to MFG-F02's finished-good valuation.
- **BUSINESS RULE / STATE / DATA CONCEPT**: A computed, not directly posted, value — feeds the postings in MFG-F01/F02 rather than posting anything itself.
- **CONTROL**: Depends on BOM configuration and work-center cost rates (not detailed this round).
- **DEPENDENCY**: Feeds MFG-F02.
- **EVENT**: N/A — a computation, not an event.
- **RISK**: An incorrect or stale BOM/work-center cost rate would misvalue every finished good produced under it.
- **UNKNOWN**: Work-center cost-rate mechanics (per-hour, per-unit, overhead allocation) — not evidenced this round.

### MFG-F05 — Negative-inventory / revaluation entries during an MO

- **WHAT / WHY / BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: Not evidenced this round — this function is flagged from a forum thread *title* only ("Why does Odoo system generate journal entry Revaluation of WH/MO/XXX (negative inventory)…"), which was not opened/read.
- **RISK**: Unknown, but the title alone suggests negative-stock scenarios during manufacturing trigger some kind of revaluation entry distinct from MFG-F01/F02's normal flow — worth a dedicated follow-up.
- **UNKNOWN**: Everything — this is an explicitly incomplete, forum-title-only lead, not a documentation-tier finding. Recorded transparently as such rather than embellished.
