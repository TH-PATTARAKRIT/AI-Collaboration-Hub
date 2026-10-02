# U162 NEUTRAL — Purchase and Manufacturing Replenishment Integration

**Unit:** U162 | **Group:** G07/G08 | **Priority:** P1  
**Module status:** PRESENT  
**Neutral-ref range:** REF-U162-N01 through REF-U162-N25

---

## Overview

This unit covers the integration layer between the procurement-to-purchase pathway and the manufacturing order system. When a manufacturing order requires components that are not in stock, the system can automatically generate purchase requests addressed to external suppliers. The integration module activates automatically whenever both the manufacturing and purchase-with-stock modules are present. It adds bidirectional navigation between purchase requests and manufacturing orders, and ensures that when a purchase receipt is validated, the components become immediately available to the manufacturing order.

---

## Neutral Reference Index

**REF-U162-N01** — The integration addon declares its dependency on both the manufacturing core module and the purchase-with-inventory module, and is designed to activate automatically whenever both prerequisites are installed.

**REF-U162-N02** — A manufacturing order record gains an integer counter showing how many purchase requests are linked to it. This counter is visible only to users who have purchase access rights.

**REF-U162-N03** — The purchase-request counter on a manufacturing order is recalculated whenever the set of reference documents or their associated purchase records changes.

**REF-U162-N04** — The system identifies which purchase requests belong to a manufacturing order by following the chain of raw-component stock movements (including their upstream origin movements) to the purchase order lines that were created to fulfill them, then resolving those lines back to their parent purchase orders.

**REF-U162-N05** — When navigating upstream documents for a raw-component movement, the system uses the set of purchase order lines that created that movement as the navigation key if no other key is found.

**REF-U162-N06** — When manufacturing orders are merged, the sets of purchase order lines linked to each raw-component movement are consolidated per bill-of-materials line and re-applied to the merged order.

**REF-U162-N07** — A purchase order record gains an integer counter showing how many manufacturing orders originated it. This counter is visible only to users who have manufacturing access rights.

**REF-U162-N08** — The system identifies which manufacturing orders originated a purchase order by traversing from the purchase order lines to their destination stock movements, then resolving those movements to the manufacturing orders they feed as raw material.

**REF-U162-N09** — When a buy replenishment fails to find a matching supplier, the system notifies both the product's responsible party and the manufacturing order's assigned user by posting a message that includes mentions of all relevant parties.

**REF-U162-N10** — Each warehouse configuration stores a direct reference to the pull rule responsible for triggering purchase orders. This reference allows the system to quickly locate the buy rule without searching through all rules.

**REF-U162-N11** — The buy pull rule is configured with the warehouse's incoming reception operation type. Whether cancellation propagates depends on whether reception uses a single step or multiple steps.

**REF-U162-N12** — When procurement requests arrive for the buy route, the system groups them by a consolidation key and searches for an existing draft purchase request matching that key. If none exists, a new purchase request is created using elevated internal permissions to avoid access-right problems for users who lack purchase module access.

**REF-U162-N13** — For each buy procurement, the system resolves a matching supplier from the product's vendor pricelist. If the procurement originates from a replenishment rule and no supplier is found, the failure is raised as a user-visible exception. If the procurement originates elsewhere and no supplier is found, the downstream movement is switched back to the take-from-stock method.

**REF-U162-N14** — Buy procurements are consolidated into the same purchase request when they share the same vendor, draft status, reception operation type, company, buyer, and currency. The vendor's grouping preference can further constrain consolidation by day or week.

**REF-U162-N15** — A new purchase request header is built from the first procurement's supplier information, including the fiscal position, payment terms, and currency, and is created under elevated internal permissions.

**REF-U162-N16** — Each purchase order line carries a many-to-many relationship pointing to the downstream stock movements it was created to fulfill. This relationship uses the same database join table as the inverse relationship on the stock movement side.

**REF-U162-N17** — When a new purchase order line is created from a procurement request, the raw-component movement identifiers from the manufacturing order are written into the line's set of destination movements, establishing the purchase-to-manufacturing link.

**REF-U162-N18** — Each stock movement (including raw-component movements on manufacturing orders) carries an inverse many-to-many relationship back to the purchase order lines that were created to fulfill it.

**REF-U162-N19** — When a manufacturing order is confirmed, all raw-component movements have their supply method adjusted (from the default stock-taking method to the order-driven method if a matching route rule exists), then all movements are confirmed, and finally the scheduler is triggered on the raw-component movements.

**REF-U162-N20** — After confirming the manufacturing order's movements, the system explicitly triggers the automatic replenishment scheduler on the raw-component movements to activate any matching reorder rules.

**REF-U162-N21** — Raw-component movements on manufacturing orders are created with the stock-taking supply method as their default. The route-adjustment step during order confirmation may switch individual movements to the order-driven method when the product's configured route points to a buy or manufacture pull rule.

**REF-U162-N22** — The top-level scheduler entry point delegates to an internal task runner that sequentially: recomputes all reorder-rule quantities, processes all pending reorder rules to generate buy procurements, and then batch-assigns waiting stock movements.

**REF-U162-N23** — The scheduler task runner recalculates reorder-point quantities and deadlines, invokes the reorder-rule confirmation step to create purchase requests, and then iterates over confirmed stock-taking movements in batches to assign available stock.

**REF-U162-N24** — For each reorder rule whose quantity-to-order exceeds zero, the system builds a procurement object and passes it to the routing engine. Procurement failures are recorded as activities on the product template rather than blocking the entire run.

**REF-U162-N25** — When a purchase receipt is validated, the system immediately calls the stock-reservation routine on all downstream movements that were linked to the incoming receipt movements. This step automatically reserves the received components for the manufacturing order without requiring a separate manual reservation action.
