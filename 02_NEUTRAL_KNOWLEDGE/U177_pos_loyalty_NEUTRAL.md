# U177 — pos_loyalty: Loyalty Program and Coupon Integration with POS
**Unit**: U177 | **Module**: pos_loyalty | **Priority**: P2
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Module Architecture

The POS loyalty module installs automatically whenever both the base loyalty module and the point-of-sale module are present. It extends the shared loyalty data models (program, card, rule, reward) with POS-specific capabilities while leaving the underlying data structure unchanged. All four loyalty data models participate in the POS session data-loading protocol, meaning their records are pushed into the POS client cache when a session opens.

The base loyalty data lives in a single shared set of database tables used by multiple sales channels including POS, Sales Order, and eCommerce. Neither POS nor the Sales channel maintains its own private copy of program or card records — all channels read from and write to the same tables. When the Sales loyalty extension is installed, it adds sale-channel fields to the same shared program model.

## Program Filtering for POS

A helper method on the POS configuration model computes which loyalty programs are eligible for a given terminal. It applies six conditions simultaneously: the program must be marked as POS-eligible, the program must either be globally available (no terminals assigned) or explicitly linked to the current terminal, the program's start and end dates must include today, the program's pricelist restrictions must be compatible with the terminal's available pricelists, the program's currency must match the terminal's currency, and if the program has a usage cap, the cap must not yet be reached. This currency filter is the primary multi-company boundary enforcement at the POS layer.

Programs from the base loyalty module carry a company reference field. The POS currency match adds a practical second barrier preventing programs from one company entity from appearing in a terminal configured for a different currency.

## Program Types and Trigger Modes

Eight program types exist in the shared loyalty framework: coupons, gift cards, loyalty cards, promotions, electronic wallets, discount codes, buy-X-get-Y offers, and next-order coupons. The default type is promotion. Each type has a fixed set of default computed values for trigger mode, applicability scope, and portal visibility.

Trigger mode has exactly two values: automatic (customers qualify without any code entry) and code-required (customers must provide a code). There is no third trigger mode. The terms "on order" or "on reward" do not appear in the trigger field definition.

## Code Scanning and Coupon Lookup

When a cashier scans or types a code at the terminal, the server validates it against the terminal's eligible programs. The validation checks: that the code matches an existing card record linked to an eligible program, that the card has not expired, that the program's dates are current, that the program is under its usage cap, that at least one reward is reachable with the card's current balance, and that the terminal's active pricelist is compatible with the program. Validation returns either a success payload (carrying the card identity, program identity, current balance, and a display-formatted balance label) or an error payload with a human-readable message.

A separate method on the card model allows identifying a customer by their loyalty card barcode: it searches for a card with matching code and program type of "loyalty" and returns the associated customer record, enabling customer identification by card scan.

## Point Accumulation at Order Completion

Point accumulation and coupon creation happen in two server-side steps. Before the order is finalized, a validation method checks that all coupon IDs referenced by the POS client are still valid and have sufficient balance — it rejects the order if any coupon has been consumed or expired by a concurrent transaction. After the order record is written, a confirmation method processes the complete coupon state from the client.

The confirmation method handles three categories of coupons: existing gift cards (re-linked to the order partner and source order if not already assigned, and balance-adjusted), existing loyalty and wallet cards (merged onto the customer's existing card for the same program to prevent duplicates), and newly earned coupons (created as fresh card records with a generated or provided code, starting at zero balance, then incremented). Points are stored as a running balance on the card record, not as individual transaction lines — history lines record the issued and spent amounts separately per order for audit purposes.

## Reward Application at POS

Order lines associated with rewards carry a flag identifying them as reward lines, a reference to the reward record that generated them, a reference to the card used to claim the reward, a grouping code that links multiple lines belonging to the same multi-line reward, and a point cost figure recording how many points the reward consumed. Reward product data loaded into the POS session excludes product rewards where the reward product is inactive, preventing the POS from displaying unreachable rewards. Any text-search conditions in reward product filters are pre-resolved on the server to identifier lists before being sent to the POS client, which cannot perform text searches against the product catalogue.

## Gift Card Validation

The server enforces strict structural constraints on gift card programs before a POS session can open. A gift card program must have exactly one earning rule and exactly one reward. The earning rule must be configured to award one point per unit of currency spent. The reward must provide one unit of currency discount per point redeemed. The program must have an email template and a print report action configured. Any violation produces a specific error message identifying the program and the constraint breached.

A separate method checks the real-time validity of a gift card code for scanning purposes: it confirms the card exists, has not expired, has a positive balance, belongs to a gift card program, has no assigned customer, and has no prior order history. If the card does not exist at all, the method still returns a "valid" status, allowing the POS to proceed with creating a new gift card sale.

## Portal and Customer Visibility

Each program can be configured to display loyalty balance information in the customer-facing portal, POS receipts, and eCommerce checkout. A separate translatable label field provides the display name for the points unit (defaulting to "Points"). Both the visibility flag and the label are included in the session data payload sent to POS terminals. A portal-specific JavaScript component is included in the module's front-end assets for rendering the balance dialog in the web portal context.

## Reward Deletion Guard

Deleting a reward that is referenced by existing POS order lines is blocked: if any order line references the reward, the system archives the reward instead of deleting it. This preserves the referential integrity of historical order data while removing the reward from active use.

## Session Data Loading

Four loyalty model types are loaded into the POS session cache at session open: programs, rules, rewards, and cards. Programs are loaded with a sudoed read to bypass access rules. Cards are not loaded in bulk at session open (their load domain returns False); instead, individual cards are fetched on demand when a code is scanned or a customer is identified.

## History and Audit Trail

Each order interaction with loyalty programs produces history line records that record the card identity, the order reference (with the model name to support both POS and Sales orders), a description, the points issued, and the points used. This creates a complete per-order audit trail of loyalty point movements separate from the running card balance.
