# Account × Inventory Interface Question Register

Per Hard Stop Condition #1 and CP-04, Account×Inventory items are registered here and routed to Joint Session — **never** used to claim Account-only or Inventory-only closure.

## Design-boundary finding (resolved at the principle level)

`B03_DOMAIN_BOUNDARY_MODEL.md` §3 ("Upstream/Downstream Seams") and §4 ("Explicitly Out of Scope"), `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`:

> Inventory / Costing owns valuation methodology (FIFO, weighted-average, standard cost) as "the result of a valuation method decided elsewhere." Accounting Core owns only committing the resulting value movement as a balanced Entry (CAP-02). Inventory valuation methodology is explicitly listed as out of scope for Accounting Core.

This is a clean, unambiguous split at the principle level: **Inventory decides the number; Accounting records it.**

## What is NOT yet resolved (genuine open items, not assumed closed)

1. **Landed cost, returns, and inventory adjustments** — no scenario-level trace was found showing how these specific transaction types cross the boundary in practice (only the general principle was evidenced).
2. **Structural cross-contamination inside `ISOLATED_ACCOUNT_CORR5` itself** — the "Account-only" worktree designated by Boss for this investigation contains real Inventory content: `00_Architecture_Governance/STATE03_ACCOUNTING_INVENTORY_BACKBONE_EVIDENCE_CHAIN_INDEX.md`, `..._EXECUTION_ROADMAP.md`, `STATE03_INVENTORY_DEEP_RESEARCH_MATERIAL_UNKNOWN_EXHAUSTION_AMENDMENT.md`, a `GROUP_A_SALES_INVENTORY_PURCHASE` folder under multiple domains, and `TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE`. Per the Full Reopen Program commit (`42e04e6`), this appears to be **intentional** — Accounting is explicitly tracked as the dependency root for Inventory's backbone work, and a Joint track was authorized by name — but it was not confirmed with Boss as intentional versus incidental drift in this session.
3. **The real WHT branch's diff also touched Inventory-adjacent Special-Team material** (`INDEPENDENT_REVIEW/.../IDR_007/`, `CORR_006_BOSS_HIGH_REPROOF/`, `TEAM_A/06_DOMAIN_RESEARCH/INVENTORY_CORE_BACKBONE/`) — 41 of the 180 changed files on that branch are Inventory-domain research, not Account/WHT substance. This is disclosed, not hidden, but means the "Account WHT" branch is not purely Account-scoped either.

## Classification

**`PENDING JOINT SESSION`** — the boundary principle is sound and reusable, but a scenario-level Joint session (landed cost / returns / adjustments) plus a Boss confirmation on whether the Account↔Inventory backbone cross-references inside `ISOLATED_ACCOUNT_CORR5` are intentional design tracking or worktree drift, are both required before this interface can be called fully closed.

## Next controlled action

1. Boss to confirm: is Inventory-backbone content inside the Account worktree intentional (per the Full Reopen Program's Joint track) or should it be relocated?
2. Schedule a Joint Account×Inventory session specifically to trace landed-cost, return, and adjustment postings against the CAP-02 boundary.
