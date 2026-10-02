> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Business Trace | Documentation-Tier | WHAT/WHY/BUSINESS RULE/STATE/DATA CONCEPT/CONTROL/DEPENDENCY/EVENT/RISK/UNKNOWN only

# 06 — BUSINESS RULE REGISTER (Gx2)

Evidence tier for every row: Documentation Evidence (Odoo 19 official documentation, search-grounded). See `19_PROVENANCE_REGISTER.md`.

---

### SDV-F01 — Delivery routing configuration

- **WHAT**: A warehouse's outgoing shipments can be configured as one, two, or three physical steps (pick → pack → ship, with intermediate output locations).
- **WHY**: Businesses using a removal strategy (FIFO/LIFO/FEFO) or needing a distinct packing zone benefit from explicit intermediate steps rather than a single direct move.
- **BUSINESS RULE**: One-step is the documented default for both incoming and outgoing shipments; multi-step is an explicit warehouse-level configuration choice (mirrors GRV-F01).
- **STATE**: Configuration set once, applies to subsequent deliveries at that warehouse.
- **DATA CONCEPT**: A delivery order is a movement instruction between named location roles (stock → optional pack/output → customer location).
- **CONTROL**: Gated behind the same Multi-Step Routes feature toggle as receipts.
- **DEPENDENCY**: SDV-F02 behaves differently depending on this configuration.
- **EVENT**: None beyond "configuration changed."
- **RISK**: None specific beyond GRV-F01's mirrored risk.
- **UNKNOWN**: Whether removal-strategy choice (FIFO/LIFO/FEFO) is itself independently configurable from step count, or coupled — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

---

### SDV-F02 — Physical delivery execution

- **WHAT**: A user confirms ("validates") that a quantity of goods has been shipped/delivered, moving that quantity from a stock-owned location to the customer.
- **WHY**: Mirrors GRV-F02 — a deliberate act converts "reserved/allocated" stock into a departed fact, triggering downstream invoicing and valuation.
- **BUSINESS RULE**: Validation is a discrete action; the delivery order carries a demanded and a delivered quantity, which may differ.
- **STATE**: Draft/reserved → (picked/packed, if multi-step) → done.
- **DATA CONCEPT**: Delivered quantity is tracked separately from ordered quantity on the originating Sales Order.
- **CONTROL**: Only a validated (done) delivery is authoritative for SDV-F04 (invoicing policy) and SDV-F05 (COGS).
- **DEPENDENCY**: Feeds SDV-F04 and SDV-F05 once done.
- **EVENT**: "Delivery validated."
- **RISK**: Incorrect delivered quantity propagates into invoicing and valuation.
- **UNKNOWN**: Guard conditions preventing double-processing — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

---

### SDV-F03 — Partial delivery / backorder handling

- **WHAT**: When delivered quantity is less than ordered, the shortfall is trackable as a linked backorder rather than silently lost.
- **WHY**: Real deliveries are frequently partial (stock shortage, staged fulfillment).
- **BUSINESS RULE**: Documentation states that once a quotation is confirmed, Odoo automatically tracks both delivered and invoiced quantities against the order, and that "both partial and complete deliveries are tracked" with backorders created for the remainder — this is described more as an automatic tracking mechanism than GRV-F03's more action-gated backorder description; **this is a documentation-tier nuance, not yet confirmed as identical mechanics to the purchase side.**
- **STATE**: Original delivery → done (for delivered portion) + linked backorder in draft for the remainder.
- **DATA CONCEPT**: Backorder retains linkage to originating Sales Order.
- **CONTROL**: Delivered-quantity tracking is the input to SDV-F04's "Invoice what is delivered" policy.
- **DEPENDENCY**: SDV-F04 must use the actual delivered quantity, not the ordered quantity, under that policy.
- **EVENT**: "Backorder created" (delivery side).
- **RISK**: If SDV-F03's more "automatic" framing and GRV-F03's more "action-gated" framing describe genuinely different mechanics (rather than just different documentation emphasis), a design assuming one mirrors the other would be wrong — flagged as `GAP-SDV-02`, not resolved here.
- **UNKNOWN**: Exact trigger mechanics, same caveat as above.

---

### SDV-F04 — Invoicing policy (ordered vs. delivered quantities)

- **WHAT**: A product-level setting determines whether a customer can be invoiced as soon as a sales order is confirmed ("ordered quantities") or only after delivery is validated ("delivered quantities").
- **WHY**: Businesses selling large physical quantities that may not ship all at once need invoicing tied to actual fulfillment, not just the promise of it.
- **BUSINESS RULE**: Under "delivered quantities," **the product must be delivered before an invoice can be created** — this is a structural, not merely informational, gate (contrast with GRV-F06's three-way match, which is informational-only per its documentation). This is itself a material finding: the sales-side financial control is described as *harder* than the purchase-side one.
- **STATE**: Quotation → Sales Order (confirmed) → [if delivered-quantities policy] delivery validated → invoiceable.
- **DATA CONCEPT**: Both delivered and invoiced quantities are tracked per order line.
- **CONTROL**: Configured per-product under Sales → Products → Invoicing Policy.
- **DEPENDENCY**: Requires SDV-F02/F03 (actual delivered quantity) as its gating input.
- **EVENT**: "Invoice becomes creatable" once delivery validated.
- **RISK**: A design assuming sales-side and purchase-side financial-control gates are equally "soft" would be wrong per this finding — GRV-F06 (purchase) is informational, SDV-F04 (sales, delivered-quantities mode) is structural.
- **UNKNOWN**: Whether the structural gate can be overridden by a role/permission — `SOURCE/RUNTIME VERIFICATION REQUIRED`.

---

### SDV-F05 — COGS / valuation timing at delivery

- **WHAT**: Whether/when a delivery creates an accounting-relevant COGS entry.
- **WHY**: Mirror of GRV-F04 on the outbound side — same perpetual/periodic and costing-method dependence.
- **BUSINESS RULE — MATERIAL CONTRADICTION, NOT RESOLVED HERE**: One set of documentation pages states perpetual (automatic) valuation posts "in real time whenever stock enters or leaves the warehouse" (the claim recorded in Gx1's `GRV-F04`). A different, more specific set of Odoo 19 pages states: *"Since Odoo 19, the Perpetual method impacts the stock valuation account at the invoice level"* and *"Odoo 19 no longer creates journal entries upon the physical receipt or delivery of goods... this responsibility shifted from warehouse operations to the accounting team,"* posting instead "at the time of the financial transaction (vendor bill / customer invoice)," with a **Stock Variation account acting as a buffer** until an accrual/closing process reconciles it. **Both claims are genuine Odoo 19 documentation-tier findings; they were not reconciled against each other before now.** See `GAP-SDV-01`.
- **STATE**: Delivery validated → (documented uncertainty: immediate COGS entry, OR deferred to invoice/accrual-close time via the Stock Variation buffer account).
- **DATA CONCEPT**: A "Stock Variation" account distinct from the final Stock Valuation account — a buffer for delivered-not-yet-invoiced (and received-not-yet-billed) value.
- **CONTROL**: Whichever timing is correct, it is a configuration/version fact, not something a design should hard-code either way without runtime confirmation.
- **DEPENDENCY**: SDV-F04 (invoicing policy) may itself be the missing link — if COGS truly posts "at invoicing," then the *invoicing policy* (which gates when an invoice can even be created) directly gates COGS timing too, which would make GRV-F04 and SDV-F05 two faces of one already-partially-answered question rather than two independent unknowns. This hypothesis is recorded, not confirmed.
- **EVENT**: "COGS posted" — timing unconfirmed.
- **RISK**: This is the single highest-value open question across both Gx1 and Gx2 for financial-control design discussions — must not be silently assumed either way.
- **UNKNOWN**: Full runtime resolution required; see `AWT_BACKLOG.md` for the plan, and `GRV-F04`'s own `AWT_BACKLOG.md` entry in Gx1 (updated to cross-reference this finding).

---

### SDV-F06 — Return via Reverse Transfer (pre-invoice)

- **WHAT**: Before an invoice is sent/validated, a customer return is processed via a "Reverse Transfer" generated from the original delivery order.
- **WHY**: Simple case — nothing financial has been finalized yet, so only the stock movement needs reversing.
- **BUSINESS RULE**: The Reverse Transfer defaults to the originally validated quantities (editable); confirming it generates a new incoming warehouse operation for the returned goods, which the warehouse validates separately; the original Sales Order's Delivered quantity then updates to reflect the net (delivered minus returned).
- **STATE**: Validated delivery → Reverse Transfer created (draft) → validated → original order's delivered-quantity reduced.
- **DATA CONCEPT**: The reversal is its own tracked warehouse operation, linked back to the original delivery, not an in-place edit of it.
- **CONTROL**: Requires the Inventory app; available only while no invoice has been sent/validated for the returned quantity.
- **DEPENDENCY**: Directly feeds back into SDV-F04 (delivered quantity used for "delivered quantities" invoicing) and SDV-F05 (valuation reversal).
- **EVENT**: "Return validated" — reduces net delivered quantity.
- **RISK**: If attempted after invoicing, documentation states this mechanism alone is **insufficient** (see SDV-F07) — a design must not treat Reverse Transfer as universally sufficient for all returns.
- **UNKNOWN**: Exact valuation reversal entries this creates — cross-references GAP-SDV-01.

---

### SDV-F07 — Return after invoicing, via Credit Note

- **WHAT**: When a customer returns goods after an invoice has already been sent/paid, Reverse Transfer alone is documented as insufficient; a Credit Note is used in conjunction with it.
- **WHY**: A validated/sent invoice cannot be edited — the financial correction needs its own instrument (a credit note), separate from the stock-level reversal.
- **BUSINESS RULE**: Documentation explicitly states: "Reverse Transfers can be used in conjunction with Credit Notes to complete the customer's return" for the post-invoice case.
- **STATE**: Invoice validated/sent → Reverse Transfer (stock) + Credit Note (financial) both required → both validated.
- **DATA CONCEPT**: Two linked-but-separate instruments: one for Stock Truth reversal, one for Financial Truth reversal — a clean illustration of the Backbone Roadmap's own "Inventory owns stock truth, Accounting owns financial truth" boundary rule, observed here as a documented mechanism rather than asserted architecturally.
- **CONTROL**: Financial correction requires its own document (Credit Note), distinct from the stock-level Reverse Transfer — this is this Gx's clearest evidence yet for the general "reversal after posting requires a dedicated financial-correction instrument, not just an inventory-side undo" pattern the Backbone Roadmap anticipates for Lane C scenario 3.
- **DEPENDENCY**: Requires SDV-F06's mechanism as its stock-side half.
- **EVENT**: "Credit Note issued" + "Return validated."
- **RISK**: A design providing only inventory-level reversal (no credit-note-equivalent instrument) would be incomplete for any post-invoice return.
- **UNKNOWN**: Whether/how the credit note's amount is derived automatically from the original invoice/valuation, or requires manual entry — `SOURCE/RUNTIME VERIFICATION REQUIRED`.
