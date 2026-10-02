# U116 — Purchase Agreements: Business Knowledge
## Date: 2026-10-02
## Module: purchase_requisition (Display: "Purchase Agreements")
## Status: GATE-PENDING — DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

---

## What This Module Does

The Purchase Agreements module lets a company set up formal agreements with vendors before any actual purchase orders are created. Instead of negotiating prices and terms each time a purchase order is placed, buyers can define the agreed terms once in an "agreement" record and then reference that agreement when creating purchase orders later.

The module ships as part of the Community edition of Odoo 19. It is not restricted to Enterprise.

---

## Two Types of Agreement

There are exactly two types of agreement:

**Blanket Order** — A long-term agreement with a specific vendor for a set of products at fixed prices. The buyer commits to buy certain products from that vendor at the agreed price over a defined time period. When purchase orders are created under a blanket order, the system automatically applies those pre-negotiated prices and creates vendor pricelist entries.

**Purchase Template** — A reusable shopping list that pre-fills a purchase order with standard products and quantities. Unlike a blanket order, a purchase template is not vendor-specific and does not lock in prices. It is simply a shortcut to avoid re-entering the same list of items repeatedly.

---

## Agreement Lifecycle

An agreement moves through four stages:

1. **Draft** — The agreement is being set up. Product lines can be added, prices set, and dates configured. The agreement can be edited freely. It can be deleted at this stage.

2. **Confirmed** — The agreement is active. For blanket orders, all lines must have a price greater than zero and a quantity greater than zero before confirmation is allowed. When a blanket order is confirmed, the system writes vendor pricelist entries for each product line so that future purchase orders automatically see the agreed price.

3. **Closed** — The agreement has been fulfilled or is no longer needed. Before an agreement can be closed, all purchase orders linked to it must have moved past the quotation stage (no open or pending orders allowed).

4. **Cancelled** — The agreement is inactive. Any draft purchase orders linked to it are automatically cancelled. The agreement can be returned to draft from the confirmed state if needed.

---

## Blanket Order Pricing

When a blanket order is confirmed, the system creates a vendor pricelist entry for each product line. This means that any subsequent purchase order placed with that vendor will automatically see the agreed price for those products — without needing to reference the agreement manually.

If a line is added to an already-confirmed blanket order, the pricelist entry is created immediately. If a price is changed on a confirmed blanket order line, the corresponding pricelist entry is updated automatically. Prices of zero or below are not permitted on a confirmed blanket order.

When a purchase order is linked to an agreement, the system filters the available vendor prices to show only those from that specific agreement, preventing prices from other agreements from leaking in.

---

## Purchase Template Pricing

For purchase templates, the system can auto-suggest prices from vendor pricelists when a vendor is selected while the agreement is still in draft. There is no price lock-in, and no pricelist entries are created. The template simply provides a convenient default list of products and quantities.

---

## Creating a Purchase Order from an Agreement

A buyer selects an agreement on a new purchase order. The system then:
- Copies the vendor, payment terms, currency, and delivery dates from the agreement
- Creates purchase order lines from the agreement's product lines
- For blanket orders, sets the quantity on each line to zero (the buyer enters the actual quantity)
- For purchase templates, copies the quantity from the template lines

The agreement's reference number appears in the purchase order's origin field.

---

## Alternative Purchase Orders (Call for Tenders)

This feature allows buyers to obtain competing offers from different vendors before committing to a purchase. It must be enabled in the configuration settings.

When enabled, a buyer can create one or more "alternative" purchase orders from an existing request for quotation — each going to a different vendor for the same products. All the alternatives are grouped together so they can be compared side by side.

The comparison view shows lines grouped by product, and the system can highlight:
- The vendor with the lowest total price per product
- The vendor with the lowest unit price
- The vendor with the earliest promised delivery date

When the buyer is ready to commit, they confirm the winning purchase order. Before confirmation, if other alternative quotations are still open, a warning appears asking whether to cancel those alternatives or leave them open.

---

## Reference Numbering

Blanket orders are numbered with the prefix **BO** followed by a five-digit number (e.g. BO00001). Purchase templates use the prefix **PT** (e.g. PT00001). Numbering is shared across all companies.

---

## Access and Security

- **Purchase Users** can create, read, edit, and delete agreements and their lines.
- **Purchase Managers** can only read agreements (not create or modify).
- Each agreement and its lines are restricted to the company the buyer belongs to. In a multi-company setup, users in company A cannot see company B's agreements.
- The duplicate blanket order check warns buyers when a confirmed blanket order already exists for the same vendor and company, so they are not accidentally creating overlapping agreements.

---

## Key Constraints and Business Rules

- An agreement cannot be confirmed without at least one product line.
- Blanket order lines must have both a price and a quantity greater than zero before confirmation.
- An agreement cannot be deleted unless it is in draft or cancelled state.
- The agreement type and company cannot be changed once the agreement has been confirmed.
- An agreement cannot be closed if any linked purchase order is still in a quotation or pending approval state.
- End date must not be earlier than start date.
