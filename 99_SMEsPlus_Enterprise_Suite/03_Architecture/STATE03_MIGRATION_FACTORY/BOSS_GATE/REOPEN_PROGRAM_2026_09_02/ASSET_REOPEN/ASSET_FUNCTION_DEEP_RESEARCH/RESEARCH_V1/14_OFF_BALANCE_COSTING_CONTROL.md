# 14 — Off-Balance Costing Control

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `DESIGN CANDIDATE ANALYSIS`

---

## 1. Scope

Per governing brief section on the off-balance accounting model: verify how/whether the reference ERP has an analogous non-GL-impacting internal costing mechanism, and specify SMEsPlus-target controls for the Boss's proposed Dr Internal Equipment Usage Cost / Cr Internal Equipment Usage Offset pairing (both Off-Balance account type) as a `DESIGN CANDIDATE`.

## 2. Does the Reference ERP Have an Analogous Mechanism?

No dedicated documentation search this session located a named "Off-Balance account type" or equivalent memo/statistical-posting concept in the reference ERP's asset, equipment, or manufacturing documentation specifically. This session's research effort on this specific point was narrower than on other files (time-boxed given the scale of the overall package) — this file does **not** claim a thorough negative-evidence search was completed to the same depth as, e.g., file `04`'s Equipment↔Asset link search. `UNRESOLVED / EVIDENCE REQUIRED`, explicitly flagged as an area needing a dedicated follow-up search before this file's absence-finding is treated with the same confidence as file `04`'s or file `06`'s.

General double-entry accounting systems (this is general professional knowledge, not reference-ERP-specific evidence) commonly support a "statistical" or "off-balance-sheet" journal/account type for exactly this purpose — tracking quantities or notional values that must not hit the financial statements (e.g., operating lease commitments pre-IFRS 16, consigned inventory, contingent liabilities). Whether the reference ERP specifically implements this pattern was not confirmed either way in this session.

## 3. Boss's Proposed Design — Restated

Dr **Internal Equipment Usage Cost** (Off-Balance type) / Cr **Internal Equipment Usage Offset** (Off-Balance type), for the post-depreciation internal usage amount computed per file `13`.

## 4. SMEsPlus-Target Controls (Design Candidate)

`DESIGN CANDIDATE` throughout — none of the following is adopted from confirmed reference-ERP precedent (§2), all is original control design responding to the Boss's stated intent:

1. **No cross-entry to financial accounts.** Both legs of the entry must be tagged with an account type that is structurally excluded from balance-sheet and P&L reports and from any trial-balance total that feeds statutory output — not merely "an account nobody looks at," but one the reporting engine itself cannot include.
2. **No BS/P&L impact, verified structurally, not procedurally.** The control should not rely on "nobody will post to a real account by mistake" — the account-type flag itself should make it structurally impossible for a report definition to sum an Off-Balance account into a statutory total.
3. **Full audit trail**, carrying explicit references to: source Asset, source Equipment, source Work Center, consuming Manufacturing Order (or equivalent internal consumer), the accounting/costing period, the computed rate (and which base per file `13` §3 was used), the usage quantity/driver, and the source Asset Model (so a later policy question — "which Asset Models are contributing off-balance cost and by what rule" — is answerable without reverse-engineering postings).
4. **Reversibility / period-boundedness.** Given this is a notional, non-cash, non-statutory charge, each period's off-balance entry should be independently reviewable and, if the underlying Asset is disposed of or the Equipment is decommissioned, cleanly terminated without leaving an orphaned running balance that has no real-world referent.
5. **Segregation from any statutory audit trail requirement** — because this is not a statutory record, it should not be represented to auditors or regulators as one; its purpose (internal management costing visibility) should be explicit in its own labeling, distinct from GL account naming conventions used for real financial accounts, to avoid confusing a future reviewer (including SMEsPlus's own future engineers) into treating it as a financial-statement input.

## 5. Classification

`DESIGN CANDIDATE`. This file explicitly does not confirm or deny a reference-ERP precedent with full confidence (§2) and does not claim the control list in §4 is exhaustive or Boss-approved in its specifics — it is offered as the control-shape a `HOLD`-conscious design would need, for Boss review in file `26`.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
