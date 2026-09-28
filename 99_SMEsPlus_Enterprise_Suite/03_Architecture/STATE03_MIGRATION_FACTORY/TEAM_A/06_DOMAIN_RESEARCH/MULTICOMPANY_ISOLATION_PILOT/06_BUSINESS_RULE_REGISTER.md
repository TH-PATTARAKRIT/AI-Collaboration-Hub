> Domain: MULTICOMPANY_ISOLATION_PILOT (Gx9) | Business Trace | Documentation-Tier

# 06 — BUSINESS RULE REGISTER (Gx9)

### MCT-F01 — Warehouse-company binding

- **WHAT**: Every warehouse has a required, single Company field; users are also linked to a company.
- **WHY**: A hard structural tenant boundary — stock, and the people who can act on it, must belong to a defined company.
- **BUSINESS RULE**: "Warehouse is linked with the company and the users are also linked with the company" — a strict single-parent relationship, not a many-to-many.
- **STATE / DATA CONCEPT**: Company is a required field at warehouse-creation time, not optional or default.
- **CONTROL**: This is the outermost tenant-isolation boundary this Deep Study has found — everything else (valuation, WIP, product routing) happens *within* a company context this boundary establishes.
- **DEPENDENCY**: Upstream of every other Gx — every function this Deep Study has documented implicitly happens inside one company's boundary, which this function is the first to name explicitly.
- **EVENT**: N/A — a structural constraint, not an event.
- **RISK**: None identified at the structural level — the risk surfaces at the next layer down (see MCT-F05).
- **UNKNOWN**: Whether a warehouse's company can be changed after creation (with existing transaction history) — not evidenced this round.

### MCT-F02 — Inter-company transaction automation

- **WHAT**: A per-company-pair "Inter-Company Transactions" setting, once enabled, offers four independently selectable automations: create vendor bill (from a confirmed cross-company invoice/credit note), create sales order (from a confirmed cross-company PO), create purchase order (from a confirmed cross-company SO), and synchronize stock moves.
- **WHY**: Businesses running multiple legal entities that trade with each other need the "other side" of each transaction created automatically rather than manually re-entered.
- **BUSINESS RULE**: Each of the four behaviors is independently toggle-able — a business can, for example, sync stock moves without auto-creating bills, or vice versa.
- **STATE**: Transaction confirmed in Company A → (if enabled) counterpart auto-created in Company B.
- **DATA CONCEPT**: This is a genuine cross-tenant-boundary automation — the only mechanism this Deep Study has found that deliberately crosses the MCT-F01 boundary rather than respecting it.
- **CONTROL**: Opt-in per company-pair, per behavior — not a global multi-company setting.
- **DEPENDENCY**: Directly composes with every prior Gx's valuation-timing findings — an inter-company stock-move sync presumably carries its own valuation implications on each side, not evidenced this round.
- **EVENT**: "Counterpart document auto-created."
- **RISK**: A design assuming multi-company always means strict isolation would miss this deliberate, configurable crossing mechanism — the two concepts (tenant isolation and inter-company automation) coexist by design, not by contradiction.
- **UNKNOWN**: Whether the auto-created counterpart's valuation/costing is independently computed in the receiving company, or copied from the originating company — not evidenced this round; directly relevant to the whole valuation-timing thread.

### MCT-F03 — Shared vs. per-company Chart of Accounts

- **WHAT**: Each company can have its own Chart of Accounts, or accounts can be shared across companies.
- **WHY**: Sharing accounts is documented as "useful when viewing consolidation reports" — i.e., a deliberate trade-off between per-company autonomy and consolidation simplicity.
- **BUSINESS RULE / STATE / DATA CONCEPT**: A configuration choice, not a fixed architecture — this Deep Study should not assume one model when reasoning about any given company's accounts.
- **CONTROL**: Directly affects MCT-F04 (consolidation).
- **DEPENDENCY**: Feeds MCT-F04.
- **EVENT**: N/A.
- **RISK**: A design that hard-codes "each company has entirely separate accounts" (or the opposite) would be wrong — both are valid, chosen configurations.
- **UNKNOWN**: Mechanics of what happens to existing entries if accounts are un-shared after being shared — not evidenced.

### MCT-F04 — Consolidation reporting

- **WHAT**: Combines financial data from multiple separate companies into one unified view.
- **WHY**: Group-level financial reporting needs a single picture even when legal entities are separate.
- **BUSINESS RULE / STATE / DATA CONCEPT / CONTROL / DEPENDENCY / EVENT**: A reporting function, not itself a control — depends on MCT-F03's account-sharing configuration.
- **RISK**: None identified — reporting-only.
- **UNKNOWN**: Whether consolidation handles inter-company eliminations (removing double-counted inter-company transactions from MCT-F02) automatically — not evidenced, and a materially important question for any group with active inter-company automation.

### MCT-F05 — Warehouse-level user access control

- **WHAT**: Restricting a specific user (who already belongs to the right company) to one specific warehouse within that company is **not** a native, single-field "assign user to warehouse" setting — it must be built manually via record rules and per-warehouse security groups (one group per warehouse, users allocated to the right group).
- **WHY**: Company-level isolation (MCT-F01) is coarse; a company may have several warehouses whose users should not see/act on each other's stock, which requires a finer-grained mechanism than the company boundary alone provides.
- **BUSINESS RULE**: Multiple independent community sources (a forum thread specifically asking "how to assign a user to a specific warehouse," and multiple third-party marketplace apps solving exactly this) corroborate that this is not solved by a built-in field — it is a genuine configuration/administration task, or requires a paid add-on.
- **STATE / DATA CONCEPT**: A "warehouse access group" is a manually-created artifact, not a system default.
- **CONTROL**: This is the clearest **authority-control gap** this Deep Study has found: company-level tenant isolation is structural and automatic (MCT-F01); warehouse-level isolation within a company is possible but requires deliberate, manual security configuration, with a real ecosystem of third-party apps existing specifically because the native path is not simple.
- **DEPENDENCY**: Builds on MCT-F01; independent of MCT-F02/F03/F04.
- **EVENT**: N/A.
- **RISK**: A design assuming "assign this user to this warehouse" is a simple native field, the way "assign this warehouse to this company" is, would be wrong — this is a materially different (and materially harder) configuration task.
- **UNKNOWN**: Exact native record-rule model behind this (is there a documented `stock.warehouse` security pattern, or is it entirely bespoke per-installation) — official documentation for this specific gap was not found this round, only forum/marketplace corroboration.
