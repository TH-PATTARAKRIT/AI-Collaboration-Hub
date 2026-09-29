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

> **RESOLUTION UPDATE (2026-09-29)**: `GAP-MFG-01` partially closed. This round opened the previously-unread forum thread (title only before now) and cross-checked it against a secondary Odoo-partner source. The two sources describe **different Odoo versions**, and are recorded here as a disclosed tension, not silently reconciled into one story — this is exactly the kind of version-drift a documentation-tier round must flag, not resolve on its own authority.

- **WHAT (pre-Odoo-19 behavior, per the forum thread — community tier, V1)**: When a manufacturing order consumes a component that isn't physically in stock yet (negative on-hand quantity), Odoo values that consumption at an estimated cost. Once the component is later actually received (procurement/inventory adjustment), Odoo posts a **"Revaluation of WH/MO/XXX (negative inventory)"** journal entry that reconciles the earlier estimated cost against the now-known real cost, hitting the inventory account and the WIP account (the account configured on the virtual production location).
- **WHAT (Odoo 19 specifically, per a secondary Odoo-partner source describing the "New Stock Valuation in Odoo 19" changes — blog tier, not official docs, V1)**: this source states Odoo 19 changed manufacturing valuation so that **raw-material cost is only accounted for when the vendor bill is posted**, and that **Odoo 19 no longer automatically creates the expense-revaluation entries described above the way older versions did**.
- **WHY THIS MATTERS BEYOND MFG-F05 ITSELF**: if the second source is accurate, it would be a *fifth* data point consistent with (not contradicting) the already-flagged, **`Material Finding — Independently Unverified`** valuation-timing reconciliation (`STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`) — no separate negative-inventory catch-up needed because ordinary vendor-bill-time posting already covers it. **This is recorded as additional evidence for that same open, Boss-flagged, audit-pending item — explicitly not as a sixth self-confirmation that would compound the same single-session-resolves-its-own-conflict pattern Boss already flagged.** `CHATGPT_AUDIT` should treat this MFG-F05 finding as part of the same package it is already reviewing (`STATE03_CHATGPT_AUDIT_PACKAGE_BGQ03.md` §2.3), not a separate item.
- **BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: not distinguishable from the version tension above without either an official Odoo 19 documentation page (not a blog) or AWT runtime confirmation — neither obtained this round.
- **RISK**: Real financial-control risk either way — negative-inventory-during-manufacturing is a genuine C1-adjacent scenario; getting the version wrong (assuming 19 behaves like 17/18, or vice versa) would misstate expected postings.
- **UNKNOWN**: Whether Odoo 19 truly dropped the automatic revaluation entry, or whether it still exists for some negative-inventory paths (e.g., non-automated valuation categories) and only changed for the automated/FIFO-Average path the blog source describes — `DOCUMENTATION/SOURCE/RUNTIME VERIFICATION REQUIRED`, not assumed either way. Criticality remains **C1 (provisional)** pending this resolution, per the Function Register's own caveat.

> **ADDENDUM (2026-09-29, further search this round)**: official Odoo 19 documentation (`inventory_valuation/operations_valuation.html`) confirms a *general* negative-stock rule: when stock goes negative (e.g., a sale before its receipt is recorded), Odoo values the outbound move at the product's last known cost, and the resulting negative stock value is included in the **Stock Variation** account in the Accounting app. This corroborates the "no separate named revaluation entry, value flows through the ordinary financial-transaction-time posting" reading — but it describes the general/delivery-side case, not specifically the manufacturing-order consumption scenario the forum thread names (`WH/MO/XXX`). **Not upgraded to V2** — still short of directly confirming or denying the MO-specific entry. Source added to `19_PROVENANCE_REGISTER.md` (`EV-MFG-07`).
