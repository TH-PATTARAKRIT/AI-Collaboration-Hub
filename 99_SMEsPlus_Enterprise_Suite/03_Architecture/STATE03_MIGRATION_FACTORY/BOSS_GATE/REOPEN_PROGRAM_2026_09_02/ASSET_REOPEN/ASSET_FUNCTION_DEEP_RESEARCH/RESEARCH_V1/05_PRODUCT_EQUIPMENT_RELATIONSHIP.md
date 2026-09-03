# 05 — Product ↔ Equipment Relationship

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — LINEAGE CHALLENGE`

---

## 1. Scope and the Central Question

Governing brief research object 01 asks whether a Product → Purchase → Receipt → Equipment → Asset lineage exists in the reference ERP, or whether this session should prove it does not exist that way. This file addresses that directly rather than assuming the lineage.

## 2. Finding: The Lineage Is Not Evidenced As an Automatic Pipeline

`CONTRADICTED (of the assumption of an automatic Product→Equipment→Asset pipeline)`. No official documentation page located in this session describes a workflow where purchasing a product, receiving it, and some system trigger automatically creates an Equipment record and/or a fixed-asset Asset record. What was found instead:

- **Product → Asset**: the reference ERP's asset (fixed-asset) documentation describes assets typically originating from a vendor bill line where the line's product/account is configured such that the bill posts to an asset-type account rather than an immediate expense — at which point the reference ERP is documented to prompt or allow creating an Asset record from that bill line. This is a **Product/Bill → Asset** path, evidenced.
- **Product → Equipment**: no documented automatic trigger. Equipment records are documented as manually created (Maintenance app → Equipment → New), independent of any purchase/receipt event, though a Product field may optionally be set on an Equipment record in some deployments (see file `04` — not confirmed native).
- **Equipment → Asset**: no documented link at all (file `04` §2).

So the lineage the governing brief asks about is best evidenced as **two separate, non-integrated paths** — Product/Bill→Asset (evidenced, financial-side) and manual Equipment creation (evidenced, operational-side) — not a single connected pipeline. This is itself the material finding, not a research gap: the reference ERP's own documented design keeps "this is a fixed asset for depreciation purposes" and "this is a piece of maintainable equipment" as structurally separate concepts unless a business manually reconciles them (or installs a third-party bridge, per file `04`).

## 3. Product Type Constraints

`SUPPORTED INTERPRETATION`: the reference ERP's product-type distinction (broadly: storable/trackable goods vs. consumable vs. service, terminology generalized per clean-room rule) governs whether a product participates in inventory valuation at all. A product that is not stock-tracked would have no "receipt" event in the inventory sense, which would rule out an inventory-triggered Equipment/Asset creation for that product type. This reasoning is drawn from the reference ERP's well-documented general product-type behavior (established across many other files in the sibling COGS research), applied here by extension; it was not re-confirmed specifically for the equipment/asset creation path in this session. `UNRESOLVED / EVIDENCE REQUIRED` as applied specifically to this lineage question.

## 4. Capitalization Trigger

`SUPPORTED INTERPRETATION`: the documented Product/Bill → Asset path is configuration-driven (the vendor bill line's account determines asset-vs-expense treatment), which functions as a capitalization trigger, but it is manual/configuration-based rather than a policy-driven automatic capitalization-threshold feature (e.g., "any purchase over $X automatically becomes an asset"). No documented capitalization-threshold feature (a dollar amount below which an asset purchase is auto-expensed) was located. `UNRESOLVED / EVIDENCE REQUIRED` on whether any such threshold feature exists.

## 5. Automatic vs. Manual Asset Creation

`SUPPORTED INTERPRETATION`, per §2: Asset creation from a qualifying vendor bill line is documented as prompted/facilitated by the system but still requires a user action (not silently automatic without any confirmation step) in the versions of documentation reviewed. Equipment creation is documented as fully manual. Neither is evidenced as a background/automatic process triggered purely by a receipt event with no user involvement.

## 6. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`: SMEsPlus should not assume it can inherit an automatic Product→Equipment→Asset pipeline from the reference ERP, because none exists there to inherit. If SMEsPlus wants this lineage (which the governing brief's later objects — Asset↔Equipment↔Work Center lineage, manufacturing cost integration — strongly suggest it will need), it is **original design work**, not adaptation of a reference-ERP pattern. This is flagged to file `23` (Fit/Gap Register) as `EXTEND` at best, more accurately `REJECT the assumption of precedent, ADOPT SEMANTICS only for the two separate sub-paths that do exist (Product/Bill→Asset; manual Equipment creation), and build the connecting logic new`.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
