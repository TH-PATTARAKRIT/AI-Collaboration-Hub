> Domain: SALES_DELIVERY_VALIDATION_PILOT (Gx2) | Challenge Question Set (CQS) Log | Master Prompt §9 — adversarial verification, not a quota

# CHALLENGE QUESTION SET (CQS) LOG (Gx2)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-SDV-01 | Does "Invoice what is delivered" merely *recommend* invoicing after delivery, or *require* it? | "Sales-side financial control is informational, like Gx1's 3-way match" | **Contradicted** | Documentation states the product "must be delivered before an invoice can be created" under this policy — a structural gate, not informational (EV-SDV-06). |
| CQS-SDV-02 | Does perpetual/automatic valuation post a journal entry at the moment of physical delivery? | Carried forward from Gx1's GRV-F04 finding | **Contradicted / Conditional — Material Delta** | Odoo-19-specific documentation states perpetual valuation posts "at invoice level," not at physical movement, via a Stock Variation buffer account (EV-SDV-04). This directly conflicts with the more generic claim recorded in Gx1. Neither claim is dismissed — logged as `GAP-SDV-01`, Evidence Conflict, pending runtime resolution. |
| CQS-SDV-03 | Is a customer return always processed the same way regardless of invoice status? | "One return mechanism covers all cases" | **Contradicted** | Documentation explicitly splits pre-invoice (Reverse Transfer alone) from post-invoice (Reverse Transfer + Credit Note) cases (EV-SDV-07). |
| CQS-SDV-04 | Is delivery-side backorder creation triggered by the same explicit user action as Gx1's purchase-side backorder (edit + validate)? | "Backorder mechanics are identical on both sides" | **Unknown / Conditional** | Documentation describes delivery-side tracking in more automatic-sounding terms ("Odoo automatically adds... delivered and invoiced quantities... both partial and complete deliveries are tracked") without the same explicit edit-then-validate narrative Gx1 found. Not confirmed as a real mechanical difference vs. just different documentation emphasis — logged as `GAP-SDV-02`. |
| CQS-SDV-05 | Does the Credit Note's amount in a post-invoice return get derived automatically, or require manual re-entry of the return value? | Assumed: automatic, mirroring the invoice it corrects | **Unknown** | No documentation evidence found either way this round — logged as an open UNKNOWN in `06_BUSINESS_RULE_REGISTER.md` SDV-F07, not force-closed. |

## Status

`CLOSED (documentation-tier)`: CQS-SDV-01, CQS-SDV-03.
`OPEN (Evidence Conflict — highest priority)`: CQS-SDV-02 (`GAP-SDV-01`).
`OPEN (Targeted Validation Needed)`: CQS-SDV-04 (`GAP-SDV-02`), CQS-SDV-05.

No round cap, no quota — CQS-SDV-02 is the single most consequential open question across both Gx1 and Gx2 and is carried into both pilots' AWT backlogs.
