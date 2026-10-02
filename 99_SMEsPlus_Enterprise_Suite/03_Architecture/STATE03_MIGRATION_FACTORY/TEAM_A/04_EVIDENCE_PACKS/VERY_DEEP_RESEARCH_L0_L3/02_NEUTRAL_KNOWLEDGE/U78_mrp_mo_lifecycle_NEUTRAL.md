# U78 Neutral Knowledge — MRP MO Lifecycle
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U78-001 | A Bill of Materials record has a type field with two base values: manufacture (for regular production) and kit (phantom explosion for sales/delivery). |
| NR-U78-002 | BOM component lines are stored as child records linked to the parent BOM; each line carries product, quantity, and unit of measure. |
| NR-U78-003 | When the subcontracting module is installed, a third BOM type becomes available: subcontracting, indicating the finished product is produced by an external supplier. |
| NR-U78-004 | A subcontracting BOM specifies a list of permitted supplier partners who can perform the subcontracted work. |
| NR-U78-005 | A Manufacturing Order passes through the states: Draft, Confirmed, In Progress, To Close, Done, and Cancelled. The state is computed and stored. |
| NR-U78-006 | Confirming a Manufacturing Order confirms all component demand moves and finished goods demand moves; it triggers stock replenishment for any components forecasted as insufficient. |
| NR-U78-007 | Only draft Manufacturing Orders transition to Confirmed on the confirm action; orders already in progress (e.g. backorders) retain their current state. |
| NR-U78-008 | Component demand on a Manufacturing Order is represented as individual stock movement records linked to the order; no separate transfer document is created for components. |
| NR-U78-009 | Raw material stock movements route from the source stock location to the production (WIP) location of the product. |
| NR-U78-010 | Finished goods stock movements route from the production (WIP) location to the destination finished goods location. |
| NR-U78-011 | Reserving components on a Manufacturing Order triggers the standard stock reservation mechanism on the component demand moves. |
| NR-U78-012 | Setting the quantity to produce on a Manufacturing Order proportionally updates the quantity on each component and finished goods move, based on the ratio of (qty producing minus qty already produced) times the per-unit factor from the BOM. |
| NR-U78-013 | Closing a Manufacturing Order (Mark as Done) posts component moves first, then prices the finished goods move, then posts the finished goods move; optionally splits a backorder for unproduced quantity. |
| NR-U78-014 | After component moves are posted, the finished goods move price per unit is calculated before the finished goods move is posted; this ensures the correct valuation is captured. |
| NR-U78-015 | When closed, the Manufacturing Order receives a locked flag, a finished date, and a Done status. Remaining unposted moves with no quantity done are force-set to Done with zero quantity rather than cancelled. |
| NR-U78-016 | In base manufacturing (without the accounting module), the cost calculation for finished goods is a no-op; the accounting module provides the real implementation. |
| NR-U78-017 | With the manufacturing accounting module installed, the finished goods price per unit is set to the total actual cost (component values plus workcenter costs plus any extra unit cost) divided by produced quantity, for products using average or FIFO costing. |
| NR-U78-018 | For products using standard costing, the finished goods price per unit is set to the product standard price regardless of actual consumed cost; no explicit production variance journal entry is created. |
| NR-U78-019 | The standard stock accounting module overrides the stock movement posting: it sets the monetary value on outgoing moves before posting, then sets the value on incoming moves after posting, then creates the accounting journal entry. |
| NR-U78-020 | An accounting journal entry for a stock movement is created only when the product uses real-time perpetual valuation, the move quantity is non-zero, and at least one of the source or destination location has a valuation account configured. |
| NR-U78-021 | When the destination location carries a valuation account (such as the production WIP location), the component consumption journal entry debits that location account and credits the product stock valuation account. |
| NR-U78-022 | When the source location carries a valuation account (such as the production WIP location acting as source for finished goods), the finished goods journal entry debits the product stock valuation account and credits the WIP location account. |
| NR-U78-023 | The production location's valuation account field is the WIP account for manufacturing accounting; it must be explicitly configured on the production location for component and finished goods journal entries to be generated. |
| NR-U78-024 | The company carries two WIP-related account fields: a Production WIP Account (for in-progress inventory) and a Production WIP Overhead Account (for workcenter overhead). Both are defined in the inventory accounting module. |
| NR-U78-025 | When the manufacturing accounting module is installed, a labour journal entry is created at MO close: it debits the production location valuation account (WIP) and credits the workcenter expense account (or the product expense account as fallback). |
| NR-U78-026 | A separate WIP accounting wizard allows manual posting of period-end WIP entries: it creates a journal entry debiting the WIP account and crediting the stock valuation account and overhead account for the value of in-progress component consumption and workcenter time; the entry auto-reverses on the next day. |
| NR-U78-027 | The WIP wizard only produces meaningful entries for Manufacturing Orders in confirmed, in-progress, or to-close states; done or cancelled orders yield zero-value entries. |
| NR-U78-028 | Manufacturing Orders carry a link to their associated WIP journal entries for traceability; journal entries carry a reverse link to the Manufacturing Orders they were based on. |
| NR-U78-029 | Total Manufacturing Order cost for AVCO/FIFO pricing = sum of component move values + sum of workcenter labour costs + the extra unit cost field multiplied by produced quantity. |
| NR-U78-030 | The manufacturing accounting module adds an extra unit cost field to the Manufacturing Order; for subcontracting it is populated from the supplier invoice or purchase order line. |
| NR-U78-031 | For standard-costing scenarios, no production variance account entry is created at MO close. Any difference between actual consumed cost and finished goods standard price remains absorbed in the stock valuation account balances without an isolated variance posting. |
| NR-U78-032 | The subcontracting module exists in Odoo 19 Community. It adds the subcontract BOM type, a subcontracting location per partner, and automatically creates a linked Manufacturing Order when a supplier receipt for a subcontracted product is confirmed. |
| NR-U78-033 | When a receipt move for a subcontracted product is confirmed, the system sets the is-subcontract flag on the move, changes the source location to the partner subcontracting location, and immediately creates and confirms a linked Manufacturing Order. |
| NR-U78-034 | For subcontracting, the finished goods stock movement of the MO is linked to the supplier receipt movement via a destination-move relationship, so receiving the goods from the supplier also completes the MO finished goods step. |
| NR-U78-035 | The subcontracting accounting module exists in Odoo 19 Community. It adjusts the finished goods price calculation for subcontracted MOs by incorporating the supplier service cost from the bill or purchase order. |
| NR-U78-036 | For subcontracted AVCO/FIFO products, the finished goods value is reduced by the extra cost already captured in the receipt move value, avoiding double-counting the supplier fee. |
| NR-U78-037 | Component and finished goods movements on a Manufacturing Order share the same operation type (manufacturing operation); they are not routed through separate picking documents—component moves use the raw material production linkage directly. |
| NR-U78-038 | The BOM consumption policy ('flexible', 'flexible with warning', 'blocked') controls whether users can close an MO with actual component quantities differing from BOM-expected quantities, and whether a warning is shown. |
