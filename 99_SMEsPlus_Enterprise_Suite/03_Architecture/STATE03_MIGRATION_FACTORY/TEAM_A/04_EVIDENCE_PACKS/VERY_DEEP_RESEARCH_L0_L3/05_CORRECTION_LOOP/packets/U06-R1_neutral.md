# Correction packet U06-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer for Odoo 19 Community: no vendor structure. Supplements the neutral statements of the purchase order unit; supersedes nothing.

## Starting a vendor bill from a purchase order

- **WHAT:** A vendor bill is started from a purchase order through a small number of entry points. The order screen itself has no dedicated create-bill button; its header offers an upload action for a bill file once the order is confirmed, and a statistic button that only opens bills that already exist. [N-U06R1-001]
- **WHAT:** In the list of purchase orders, a list-header action creates bills for the selected orders. It is always shown, whatever the state of the selected orders, and it groups the result into one bill per company, vendor and currency. [N-U06R1-002]
- **WHAT:** In the list of requests for quotation, the list controller offers an upload action for a bill file for the selected orders. The list header of that list has no create-bills action. [N-U06R1-003]
- **BUSINESS RULE:** An uploaded bill file is stored first, then the bill is created and filled from the document, the file is attached to the bill, and the bill opens. Several selected orders may be used only if they belong to one vendor; otherwise the action is refused, both in the screen and again on the server. [N-U06R1-004]
- **BUSINESS RULE:** On a draft vendor bill, a purchase user can use an auto-complete field to load a previous bill or a purchase order; the order header values and all order lines not yet linked to the bill are copied in, each line taking the quantity still to be billed and the order price. [N-U06R1-005]
- **BUSINESS RULE:** A matching screen lets users pair order lines with bill lines. It is reachable from a statistic button on the order (invoicing role) and from one on the bill (purchase role). Selecting only order lines and pressing the match action creates a draft bill containing them; selecting both pairs lines by product, links them, adds the leftovers or deletes the leftover selected bill lines. Adding bill lines to an order requires the purchase role. [N-U06R1-006]
- **BUSINESS RULE:** After a bill file has been imported into an empty bill, the system tries to link the bill to purchase orders from the origin text. Candidate orders must be confirmed, in the same company, and not fully billed; a reference match with an equal total (tolerance of two hundredths) replaces the lines with order lines, other match kinds keep bill lines and adjust quantities, and a last-resort match uses the vendor and the total. Failures are logged and ignored. [N-U06R1-007]
- **DEPENDENCY:** The opposite direction also exists: selected bill lines can be turned into a new purchase order that is confirmed at once and linked back to those lines. [N-U06R1-008]
- **RISK:** A guided tour step still points to a create-bill button on the order screen that does not exist; the effect is not confirmed. The effect of the list-header action on orders that are not confirmed is not confirmed either. [N-U06R1-017]

## Where the vendor price comes from on a bill

- **BUSINESS RULE:** A product added by hand to a vendor bill gets the product cost as its default price, not the price in the vendor price list. [N-U06R1-009]
- **BUSINESS RULE:** The vendor price lookup used by the product catalog on a bill belongs to the accounting side and was already recorded under the product unit; the purchase order unit owns only the order-side lookup. The bill-side lookup returns the raw vendor price and minimum quantity, whereas the order-side lookup returns the discounted price converted to the order currency and unit. A bill created from an order carries the order line price, not a new lookup. [N-U06R1-010]

## Receipt validation acknowledges the order

- **BUSINESS RULE:** Validating a stock transfer that is linked to a purchase order marks that order as acknowledged by the vendor, before the transfer itself is processed, with elevated rights, so the person validating the receipt does not need purchase rights. The same mark is set manually by an Acknowledge button on the confirmed order, and by the vendor opening an acknowledge link on the portal. It is not restricted by transfer type in the source, so returns and drop shipments may also set it; this is not confirmed. [N-U06R1-011]
- **DEPENDENCY:** The mark controls the reminder mail selection (only confirmed, not acknowledged orders with reminders enabled and not purely services are reminded) and the not-acknowledged counters and filters of the purchase dashboard and search. [N-U06R1-012]

## Roles and segregation of duties

- **CONSTRAINT:** Posting a vendor bill requires the invoicing role, or an automated process running with full rights. The bill screen's Confirm button is restricted to that role, and a purchase document without a bill date cannot be posted. [N-U06R1-013]
- **CONSTRAINT:** The purchase user role can create, edit and delete vendor bills and their lines, limited by rule to vendor document types; it does not include the invoicing role, so a pure buyer can prepare bills but not post them. The invoicing role can read and edit purchase orders but not create or delete them. Creating bills from an order uses the caller's own rights, so both roles can do it. [N-U06R1-014]
- **OPTIONALITY:** Automatic posting of vendor bills happens only when the company enables it, the vendor is set to always auto-post, there is no abnormal amount warning, no tamper-protection restriction and no suspected duplicate; it is triggered from bill files received through a journal, not from the upload on the order screen. The user under which it runs is not confirmed. [N-U06R1-015]
- **CONSTRAINT:** Approval of large orders needs the purchase administrator role when two-step validation is configured. The system compares no creator with poster: separation of duties between buying, receiving, billing and posting rests only on role membership, with the exception that one buyer can create and confirm an order from bill lines in one step. [N-U06R1-016]
- **UNKNOWN:** Whether the list-header action on unconfirmed orders produces a bill or an error, whether return transfers acknowledge the order, which user runs automatic posting, and whether the stale tour step is exercised require runtime confirmation. [N-U06R1-017]
