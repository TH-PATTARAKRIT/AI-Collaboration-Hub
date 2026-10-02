# U74 Neutral Knowledge — Three-Way Match
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U74-001 | The bill control policy field is defined on the product configuration form as a selection with two values, stored and precomputed, and editable by the user. |
| NR-U74-002 | The first policy value controls billing based on what was ordered from the supplier — the confirmed purchase quantity on the order line. |
| NR-U74-003 | The second policy value controls billing based on what was actually received from the supplier — quantities confirmed through goods receipt. |
| NR-U74-004 | When a product has no explicit policy set, the system applies whatever the current system-wide default is at compute time; if no default is configured, received-quantity is used. |
| NR-U74-005 | Products of the service type are forced to use the ordered-quantity billing policy regardless of system defaults. |
| NR-U74-006 | Non-service products inherit the system-wide default billing policy, which falls back to received-quantity unless an administrator has set a different default. |
| NR-U74-007 | The billed quantity field on a purchase order line is a stored computed field that accumulates totals from all linked vendor bill lines. |
| NR-U74-008 | The billed quantity is recomputed whenever the state or quantity on any linked bill line changes, or when the received quantity or order state changes. |
| NR-U74-009 | The billed quantity computation delegates to a helper that iterates all linked bill lines and accumulates UoM-converted quantities by line. |
| NR-U74-010 | Only bill lines whose parent document is not in a cancelled state are counted; both draft-state and posted bill lines contribute to the billed quantity total. |
| NR-U74-011 | Bill lines from vendor bills (incoming purchases) add their UoM-converted quantity to the billed quantity total. |
| NR-U74-012 | Bill lines from credit notes (refunds) subtract their UoM-converted quantity from the billed quantity total. |
| NR-U74-013 | When the policy is ordered-quantity, the quantity still to be billed equals the ordered quantity minus the already-billed quantity. |
| NR-U74-014 | When the policy is received-quantity, the quantity still to be billed equals the received quantity minus the already-billed quantity — this is the three-way cap. |
| NR-U74-015 | The received quantity field on a purchase order line is a stored computed field that runs with elevated privileges and supports a manual inverse. |
| NR-U74-016 | When creating a vendor bill from a purchase order, each bill line is populated with a quantity equal to the quantity still to invoice; for credit notes the sign is reversed. |
| NR-U74-017 | The billing status on a purchase order is a stored computed selection with three possible values reflecting the current billing state of the order. |
| NR-U74-018 | A purchase order that is not in confirmed state is unconditionally assigned a billing status of nothing to bill, without evaluating individual line quantities. |
| NR-U74-019 | A confirmed purchase order where at least one line has a nonzero quantity still to bill receives a billing status of waiting for bills. |
| NR-U74-020 | A confirmed purchase order where all lines have zero quantity still to bill and at least one bill exists receives a billing status of fully billed. |
| NR-U74-021 | For storable consumable products, the received-quantity method is automatically set to use the stock-operations mechanism instead of manual entry. |
| NR-U74-022 | A dedicated field on each purchase order line holds the full set of associated stock operations, establishing the link between goods receipts and the originating order line. |
| NR-U74-023 | Storable consumable products have their received-quantity method set to stock-operations during the method-computation pass. |
| NR-U74-024 | The received quantity computation for the stock-operations method is triggered by changes to the state, unit of measure, and quantity of any associated stock operation. |
| NR-U74-025 | Only stock operations that have been fully validated — in the done state — contribute quantities to the received total; pending or cancelled operations are excluded. |
| NR-U74-026 | Stock operations classified as purchase returns subtract from the received quantity total when they are marked for refund or have no originating return source. |
| NR-U74-027 | Normal incoming done stock operations add their UoM-converted quantity to the received total using half-up rounding. |
| NR-U74-028 | A dedicated field on each stock operation stores a direct foreign-key link back to the originating purchase order line, forming the cross-module chain from goods receipt to purchase order. |
| NR-U74-029 | When creating vendor bill lines from a purchase order, the quantity placed on each bill line is taken from the quantity-still-to-invoice, with sign reversal for credit notes. |
| NR-U74-030 | The system configuration page references an optional add-on module for hard three-way matching of purchases, receipts, and bills, but that module is not present in the Community edition of this codebase. |
| NR-U74-031 | In the Community edition, if the ordered quantity on a purchase line falls below the already-billed quantity, the system creates a soft activity warning on the vendor bill rather than raising a hard error; bill posting is not blocked. |
| NR-U74-032 | A helper filters the stock operations linked to a purchase order line to those matching the line product, and optionally restricts to operations on or before a specified accrual date. |
