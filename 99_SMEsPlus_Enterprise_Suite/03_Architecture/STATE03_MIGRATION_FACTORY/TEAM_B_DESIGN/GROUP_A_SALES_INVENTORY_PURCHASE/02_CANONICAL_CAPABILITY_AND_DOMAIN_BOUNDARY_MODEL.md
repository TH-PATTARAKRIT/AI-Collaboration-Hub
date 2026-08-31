> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 1 — Canonical Capability / Domain Boundary Design

# 02 — CANONICAL CAPABILITY AND DOMAIN BOUNDARY MODEL

## 00 — Method

Capabilities below are named from the business need each evidence cluster in
[01_TEAM_B_SCOPE_BASELINE_AND_INPUT_REGISTER.md](01_TEAM_B_SCOPE_BASELINE_AND_INPUT_REGISTER.md)'s evidence
package proves exists, not from the reference system's model/module names. Domain boundaries are drawn on
**who may originate the fact**, per governance's ownership test — a domain "owns" a capability if it is the only
domain permitted to create/mutate the underlying fact; another domain that only reads or reacts is a *consumer*,
not a co-owner.

## 01 — Four Domains, One Backbone

TEAM B independently confirms the governing prompt's framing: Sales, Inventory, and Purchase are not three
independent modules but three specialized views over one integrated commercial–supply–inventory backbone, with a
fourth, non-optional participant — Shared Master — supplying the identities every transaction refers to. This
conclusion is evidence-driven, not assumed: `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` and
`06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` show every material fact in one domain either originates a
handoff into another or consumes one — there is no isolable sub-scope.

```
                     ┌─────────────────────┐
                     │   SHARED MASTER      │  (Party, Product, UOM, Price/Vendor-Price,
                     │  (identity + terms)  │   Tax Rule, Payment Term, Currency, Sequence,
                     └─────────┬───────────┘   Warehouse/Location, Company/Branch, Dimension)
                               │ referenced by
              ┌────────────────┼────────────────┐
              ▼                ▼                 ▼
      ┌───────────────┐ ┌───────────────┐ ┌───────────────┐
      │  COMMERCIAL    │ │  PHYSICAL      │ │  SUPPLY        │
      │  DEMAND        │ │  FULFILLMENT   │ │  COMMITMENT    │
      │  (Sales)       │ │  (Inventory)   │ │  (Purchase)    │
      └───────┬────────┘ └───────┬────────┘ └───────┬────────┘
              │  commitment→demand │ demand→commitment │
              └─────────────────►│◄─────────────────┘
                                  │
                                  ▼
                     ┌─────────────────────┐
                     │  FINANCIAL HANDOFF    │  (interface only — Accounting Core owns
                     │  (interface boundary) │   everything past this line)
                     └─────────────────────┘
```

## 02 — Canonical Capability Register

| # | Capability | Owning domain | Business need it answers | Evidence basis |
|---|---|---|---|---|
| C1 | Party Identity Management | Shared Master | "Who are we transacting with, and what is their commercial relationship to us?" | `01` §02 PTY |
| C2 | Product/Service Definition | Shared Master | "What can we sell, buy, or hold in stock?" | `01` §03 PRD |
| C3 | Product Classification | Shared Master | "How do products group for policy and reporting defaults?" | `01` §04 CAT |
| C4 | Unit-of-Measure Conversion | Shared Master | "How do we count/convert quantities consistently?" | `01` §05 UOM |
| C5 | Sales Price Determination | Shared Master (consumed by Sales only) | "What should we charge, given product/qty/date/customer?" | `01` §06 PRC; confirmed Purchase-absent |
| C6 | Vendor Price Reference | Shared Master (consumed by Purchase only) | "What has this vendor historically charged for this product/qty?" | `01` §06 PRC-22..25 |
| C7 | Tax Determination | Shared Master (interface to Accounting) | "What tax applies to this line, for this direction of trade?" | `01` §07 TAX |
| C8 | Payment Term Application | Shared Master | "How does a total split into due installments?" | `01` §08 PAY |
| C9 | Currency & Rate Reference | Shared Master | "What currency and rate governs this transaction?" | `01` §09 CUR |
| C10 | Document Numbering | Shared Master | "What is this document's durable reference number?" | `01` §10 SEQ |
| C11 | Warehouse/Location Structure | Shared Master | "Where, physically, can stock exist?" | `01` §11 WH |
| C12 | Company/Branch Structure | Shared Master | "What legal/tenant boundary does this transaction belong to?" | `01` §12 CO |
| C13 | Cost Dimension Tagging | Shared Master | "What cross-cutting cost dimension does this line's value belong to?" | `01` §13 AN |
| C14 | Commercial Quotation & Commitment | Sales | "Can we promise this, and has the customer agreed?" | `03` §02 |
| C15 | Sales Fulfillment Tracking | Sales | "How much of the promise has actually been delivered?" | `03` §03 |
| C16 | Sales Billing Eligibility | Sales (interface to Accounting) | "How much of this order is billable right now?" | `03` §03 SOL-11/12 |
| C17 | Sales Commercial Exception Handling | Sales | "What happens when a commitment is cancelled or under-delivered?" | `03` §04/§07 |
| C18 | Physical Stock Position | Inventory | "What do we actually have, where, right now?" | `02` §03 |
| C19 | Movement Instruction & Execution | Inventory | "What is planned to move, and what actually moved?" | `02` §02 |
| C20 | Transfer Operation Management | Inventory | "What operational document groups this movement for a warehouse worker?" | `02` §04 |
| C21 | Reservation / Availability-to-Promise | Inventory | "What is safe to promise as a new claim on stock?" | `02` §03 |
| C22 | Fulfillment Continuation (Backorder) | Inventory | "What happens to the unfulfilled remainder of a transfer?" | `02` §05 |
| C23 | Reversal (Return) | Inventory | "How do we reverse a physically-completed transfer, traceably?" | `02` §06 |
| C24 | Traceability Unit Management (Lot/Serial) | Inventory | "Can we trace this unit forward/backward?" | `02` §07 |
| C25 | Handling Unit Management (Package) | Inventory | "What travels together, and what did travel together historically?" | `02` §08 |
| C26 | Supply Need Signaling | Inventory | "When do we need more, and how much?" | `02` §09 |
| C27 | Put-Away Placement | Inventory | "Exactly where within a zone does arriving stock go?" | `02` §10 |
| C28 | Internal Demand Capture | Purchase | "What does someone inside the company need, before any vendor is chosen?" | `04` §05 |
| C29 | Supply Commitment (RFQ→PO) | Purchase | "Have we committed to buy this, from whom, at what terms?" | `04` §02 |
| C30 | Purchase Approval Control | Purchase | "Is this commitment authorized at this value/level?" | `04` §02 PO-06; §03 |
| C31 | Multi-Vendor Comparison | Purchase | "Which of several competing offers do we accept?" | `04` §06 |
| C32 | Standing Supply Agreement | Purchase | "What pre-negotiated terms/template applies across many future orders?" | `04` §06 PREQS |
| C33 | Purchase Receipt Tracking | Purchase | "How much of what we committed to buy has arrived?" | `04` §07 |
| C34 | Purchase Billing Eligibility | Purchase (interface to Accounting) | "How much of this order is billable to us right now?" | `04` §07 POL-06/07/08 |
| C35 | Financial Handoff | Interface boundary (Accounting owns the far side) | "What must Accounting know to post this transaction?" | `07` §03; `15` |

## 03 — Domain Boundary Rules (independently derived)

1. **Shared Master is authoritative for identity and terms; it never originates a transaction.** No capability in
   C1–C13 creates a commercial commitment, a physical movement, or a financial posting by itself — every one of
   them exists to be *referenced* by C14–C35. This mirrors the evidence's own finding that Party/Product/UOM/Tax/
   Payment-Term/Currency/Sequence/Warehouse/Company/Dimension are each read-only inputs to Sales and Purchase,
   never mutated by them (only `product.supplierinfo`-equivalent vendor-price data is opportunistically *updated*
   by a Purchase confirmation — a narrow, evidenced exception recorded in [10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md](10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md)).
2. **Inventory is the sole owner of physical fact.** C18–C27 may be created or changed only by Inventory. Sales
   and Purchase may request a change (via a movement instruction) and may read the result, but neither may write
   `stock.quant`-equivalent state directly — confirmed as a negative finding in evidence (`06` §05: "Sale never
   reads or writes ... directly," "Purchase never reads or writes ... directly either"). TEAM B adopts this as a
   **hard domain-boundary rule**, not merely an observation: any future design that lets Sales or Purchase write
   physical stock state directly is a boundary violation.
3. **Sales and Purchase are symmetric in role, asymmetric in mechanism — the target design must decide which
   asymmetries are load-bearing business rules and which are accidents of the reference implementation.** Where
   evidence shows a real mechanism difference (e.g., Purchase's real amount-threshold approval gate vs. Sales'
   advisory-only credit warning), TEAM B treats it as a genuine business-semantic difference worth preserving
   unless a later phase's independent reasoning says otherwise (see
   [13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md)). Where evidence
   shows only an inconsistency with no functional rationale (e.g., differing empty-sequence fallback sentinels),
   TEAM B treats it as an implementation accident, not a business rule to replicate.
4. **The Commercial↔Supply relationship is indirect, mediated by Inventory's Supply Need Signal (C26), not a
   direct Sales→Purchase coupling.** Evidence confirms exactly one narrow, product-configuration-gated exception
   (a Sales line whose product is flagged for automatic subcontract/dropship purchase) where Sales writes a
   Purchase-side fact directly (`07` §05, "Sale line → auto-generated Purchase commitment"). TEAM B classifies
   this as a **scoped extension of the general rule, not a rebuttal of it** — see
   [08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) Scenario
   coverage.
5. **The Financial Handoff (C35) is a one-way interface, not a co-owned capability.** Sales and Purchase each own
   computing "how much is billable now" (C16/C34); Accounting owns everything past that point (posting, tax
   substitution, WHT, valuation). TEAM B does not design C35's far side — only the contract crossing it. See
   [15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md).

## 04 — External Domain Dependencies (registered, not expanded into)

Per governing prompt §7/§18, these are registered as dependencies without researching or designing them:

| External domain | Nature of dependency | Evidence |
|---|---|---|
| Accounting Core | Financial Handoff target; tax/fiscal-position computation engine; WHT subsystem | `15` §01, §06 |
| CRM | Potential `sale.order` origination dependency (`opportunity_id`-equivalent column observed, module not opened) | `15` §02 |
| Manufacturing/MRP | Shares the physical-movement ledger and the reflective replenishment-dispatch pattern; a "manufacture" fulfillment path is architecturally parallel to Purchase's "buy" path but was never researched | `15` §03 |
| Logistics/Shipping | Carrier/tracking reference on Transfer Operations; not researched | `15` §04 |
| E-commerce/Marketplace | Website-facing pricing/order/picking columns observed; not researched | `15` §05 |
| Payment | WHT netting at payment time; Accounting-internal, downstream of both Sales collection and Purchase disbursement | `15` §06 |
| Government/E-document | Live Thai Revenue-Department VAT lookup confirmed as a real external call embedded at the Party level; UBL/e-invoicing columns observed on Tax Rule | `15` §07 |

No capability above requires researching any of these domains further; each is a registered dependency for
whichever future TEAM B session designs that domain.

## 05 — What This Model Deliberately Does Not Decide

Domain boundaries above are drawn from *where a fact may originate*, which is evidence-supportable. They do not
yet decide internal shape (fields, states, exact event names) — that is Phases 2–11's work, recorded in the
remaining deliverables in this folder.
