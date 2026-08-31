> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 1/2 — Shared Master Canonical Boundary Model

# 04 — SHARED MASTER CANONICAL BOUNDARY MODEL

## 00 — Purpose

Defines, for each Shared Master concept, exactly what Sales/Inventory/Purchase may read, what (if anything) they
may write, and where TEAM B independently departs from treating the reference system's coupling as a target
requirement.

## 01 — Party

- **Canonical shape**: one Party concept covering every external/internal actor; a role (customer/vendor/contact)
  is a usage classification, not a distinct identity. Parties may be hierarchical (a legal entity with sub-
  contacts for delivery/invoice/other addressing).
- **Read access**: Sales and Purchase both read Party for identity, addressing, and the party-specific commercial
  defaults each domain needs (see below). Neither may create a new Party as a side effect of a transaction without
  an explicit, auditable "register new party" action — TEAM B flags this as a control requirement, since evidence
  shows the reference system readily lets `product.supplierinfo`-equivalent vendor data accumulate opportunistically at commitment time (§03 below), which is acceptable only for *reference/price* data, never for the Party identity itself.
- **Directional-property pattern (independent design requirement)**: evidence shows Sales and Purchase repeatedly
  read *different* party-held defaults for structurally the same decision (pricing source, tax candidacy, payment
  term, currency). TEAM B does not treat this as an accident to normalize away — a customer-facing default and a
  vendor-facing default are genuinely different business facts about the same Party record, and a target design
  must carry both without collapsing them into one ambiguous "default" field.
- **Explicit non-goal**: the reference system's tenant/multi-brand/multi-HQ columns on Party
  (`parent_company_id`/`brand_id`/`hq_brand_id`/`is_hq_brand`/`store_type_id`) have zero declaring source anywhere
  in evidence. TEAM B does **not** design a multi-brand/HQ capability into this canonical model — carried forward
  as an Unknown (see [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md)), not invented.
- **Thai Tax-Branch is not a structural boundary**: a Party may carry a Thailand tax-branch identifier as a legal/
  VAT attribute. TEAM B explicitly separates this from Company/Branch (§06) — conflating the two would misrepresent
  both concepts.

## 02 — Product / Service

- **Canonical shape**: one Product/Service concept; "goods" vs. "service" vs. "bundle" is a type attribute, not a
  separate model. Whether a product is stock-tracked is a derived consequence of type, not an independent flag a
  user sets in contradiction to type (TEAM B closes the reference system's `is_storable`-vs-`type` ambiguity here:
  **stock-tracking eligibility is derived from type, full stop** — a target design should not expose it as a
  separately overridable flag, since evidence found no confirmed real-world case where they diverge and doing so
  would reintroduce exactly the kind of two-switches-for-one-decision ambiguity evidence flags as a risk).
- **Read access**: Sales, Inventory, and Purchase all read Product identity and its policy defaults
  (billing-policy field, tax candidacy, UOM). Only Inventory may write the "is this product currently trackable in
  stock" derived state; only Purchase, at commitment time, may opportunistically extend the Vendor Price Reference
  (§03) for this product — never the Product master record itself.
- **SKU/identifier generation**: TEAM B requires exactly **one** authoritative mechanism for auto-generating a
  product's short identifier, owned by Product/Service itself. Evidence shows two independent, uncoordinated
  generators coexisting in the reference system — TEAM B classifies this as a defect pattern, not a feature, and
  it is not carried into this canonical model (see [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md)
  Decision on Fit-Gap candidate #9).

## 03 — Product Classification, UOM, Sales Price Rule, Vendor Price Reference

- **Product Classification**: hierarchical; carries both taxonomy and inventory-policy-default roles (see
  [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md) §05 for why these are catalogued separately). Read by
  all three domains; written only by Shared Master administration.
- **UOM**: a self-referential conversion family (TEAM B adopts this pattern deliberately — it is simpler than a
  separate category-plus-members model and evidence shows the reference system's own downstream code had to
  rebuild "same family" grouping logic to compensate for a prior category model's removal; a target design should
  keep the grouping *explicit and queryable*, not purely emergent from tree walking, to avoid repeating that
  compensating-code pattern). Conversion ratios become immutable once referenced by any commitment or physical
  fact.
- **Sales Price Rule**: read-only by Sales at commitment time; resolves product/category/variant scope, quantity
  break, validity window, and currency into a price. Not consumed by Purchase (§05 of
  [03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md)).
- **Vendor Price Reference**: read by Purchase at commitment time to select a default unit price/lead-time per
  vendor/quantity-break; **written (extended) by Purchase** when a commitment references a vendor/product pair not
  yet on file — the one narrow, evidenced exception to "Shared Master never mutated by a transaction domain." TEAM
  B keeps this exception narrow and explicit: only the vendor-price *reference* record may be extended this way,
  never Product, Party, or any other master concept.

## 04 — Tax Rule, Payment Term, Currency, Sequence

- **Tax Rule**: direction-scoped (a rule may apply to sales-direction, purchase-direction, or neither). Both Sales
  and Purchase determine tax candidacy from the Product's direction-specific tax linkage, then apply a
  substitution step keyed by Party (and, for Purchase, Company). **The substitution engine's internal logic is a
  Controlled Carry-Forward Unknown** (see §11 of the governing prompt and
  [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md)) — TEAM B designs only the fact that a substitution step
  exists and must be invoked, not its internal resolution algorithm.
- **Payment Term**: one shared concept; Sales resolves it from the customer-facing default, Purchase from the
  vendor-facing default (the directional-property pattern, §01). Once applied to a commitment, the specific
  installment schedule is copied onto that commitment as a historical fact, not left as a live reference — TEAM B
  adopts this snapshot pattern deliberately (a later change to the Party's default must never retroactively alter
  an already-committed order's terms).
- **Currency / Exchange Rate**: Currency itself is a global reference; Rate is a dated, company-scoped physical
  fact. TEAM B requires the transaction currency and rate to be **frozen (snapshotted) at commitment time** on
  both Sales and Purchase commitments — adopting the evidenced pattern on both sides deliberately, since a live
  re-lookup would let a historical commitment's value drift. TEAM B explicitly flags the reference system's
  silent no-rate-found→parity fallback as **not** something to carry forward: a target design must treat a
  missing rate as a data-quality exception to surface, not silently default to 1.0.
- **Document Sequence**: one numbering service, referenced by every commitment-type document needing a durable
  reference number. TEAM B requires **one consistent empty-sequence fallback behavior** across Sales and Purchase
  (the reference system's two different literal sentinels are an inconsistency, not a business rule — see
  [17](17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md) Decision on Fit-Gap candidate #11).

## 05 — Warehouse / Stock Location

- Warehouse is company-owned and immutable-after-creation; Location is optionally company-scoped (nullable =
  shared). Base Commercial-Demand and Supply-Commitment capabilities have **no inherent coupling** to
  Warehouse/Location — that coupling exists only where physical fulfillment is in play (i.e., wherever a
  commitment line results in a Movement Instruction). TEAM B adopts this as a boundary rule: a Commercial Demand
  or Supply Commitment line for a pure service never needs a Warehouse reference at all.

## 06 — Company / Branch — and the Explicit Non-Conflation with Thai Tax-Branch

- **Company/Branch is a legal-entity/tenant hierarchy.** A "Branch" in this canonical model is a child Company
  record — not a separate structural entity, not a warehouse, and not the Thai tax-branch identifier on Party. All
  three are evidenced as genuinely disjoint concepts in the reference system, and TEAM B keeps them disjoint here
  deliberately, because conflating any two of them would misrepresent a real business distinction:
  1. **Company/Branch** — legal/tenant boundary; governs access scoping, and currency must match across the
     hierarchy.
  2. **Warehouse/Location** — physical structure; company-owned but not a branch itself.
  3. **Thai Tax-Branch** — a VAT/Revenue-Department registration attribute on a Party, unrelated to either of the
     above.
- **Access scoping**: both Sales and Purchase commitment lines must resolve against an "accessible branch" set for
  the acting company context — TEAM B adopts this pattern from evidence (a symmetric, identically-shaped
  constraint on both domains) as a canonical cross-domain control requirement, detailed further in
  [14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md).

## 07 — Cost Dimension (Analytic)

- One shared, hierarchical dimension concept; definitions may be shared across companies, but usage on any posted
  commercial or supply line is always company-attributed. Both Sales and Purchase lines carry an optional
  percentage-split allocation across one or more dimension values. TEAM B adopts this symmetric pattern from
  evidence without modification — it is the one Shared Master concept where Sales and Purchase evidence showed
  **zero** asymmetry.

## 08 — General Archival / Non-Deletion Rule (CORR-008 closure, `FV006-DFO-005`)

TEAM A's own evidence independently shows the reference system already protects at least three Shared Master
concepts against deletion/deactivation once referenced by a transaction: `UOM-06` (protected UoMs "cannot be
deleted, only archived"), `PAY-07` (payment-term deletion "blocked if any `account.move` still references the
term"), `CUR-08` ("a currency used by any company cannot be deactivated"). This canonical model previously carried
that protection forward only for UOM's conversion ratio ([03](03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md)
§01) and Warehouse's owning-company assignment, with no general rule stated for Party, Product/Service, Tax Rule,
Payment Term, Currency, or Document Sequence — a completeness gap Formal IBPV FV-006 Deliverable 06 found bears
directly on audit-history integrity, since a hard-deleted master record referenced by a historical Commitment,
Physical, or Control/Financial-Handoff fact would leave that historical record with a dangling or ambiguous
reference.

**General rule**: any Shared Master concept in this file (Party, Product/Service, Product Classification, UOM,
Sales Price Rule, Vendor Price Reference, Tax Rule, Payment Term, Currency, Document Sequence, Cost Dimension,
Warehouse/Location, Company/Branch) that has been referenced by at least one historical Commitment, Physical, or
Control/Financial-Handoff fact **must never be hard-deleted**. Once so referenced, the concept transitions to an
**Archived/Retired** status — it becomes unavailable for selection on new transactions but remains permanently
resolvable for every historical fact that already references it. This generalizes, uniformly across every
Shared Master concept, the specific protections already evidenced for UOM, Payment Term, and Currency, and
extends the same discipline to the concepts that previously had no stated rule.

- **Scope**: every Shared Master concept listed in §09's Summary Boundary Table below.
- **Owner**: Shared Master administration (the same owner that already governs create/maintain actions for each
  concept, per §09) — no transaction domain (Sales/Purchase/Inventory) gains a new write path from this rule.
- **Archive/retire semantics**: an Archived/Retired record is excluded from selection lists for new commitments
  but is not otherwise altered — every field a historical fact already snapshotted or referenced remains exactly
  as it was.
- **Reference preservation**: a historical Commitment, Physical, or Control/Financial-Handoff fact's reference to
  an Archived/Retired master record remains fully resolvable indefinitely; this rule never breaks a link that
  already exists at the moment of archival.
- **Legitimate exceptions**: TEAM B identifies none. A Shared Master concept record with **zero** historical
  references (never selected on any Commitment, Physical, or Control/Financial-Handoff fact) may still be deleted
  outright — the rule above binds only once a historical reference exists.

## 09 — Summary Boundary Table

| Shared Master concept | Written by | Read by |
|---|---|---|
| Party | Shared Master admin (identity); no transaction domain writes it | Sales, Inventory, Purchase |
| Product/Service | Shared Master admin (identity); Inventory (stock-trackability derived state) | Sales, Inventory, Purchase |
| Product Classification | Shared Master admin | Sales (transitively), Inventory, Purchase (transitively) |
| UOM | Shared Master admin (immutable once referenced) | Sales, Inventory, Purchase |
| Sales Price Rule | Shared Master admin / Sales pricing admin | Sales only |
| Vendor Price Reference | Shared Master admin; opportunistically extended by Purchase at commitment | Purchase only |
| Tax Rule | Shared Master admin (Accounting-adjacent) | Sales, Purchase (interface to Accounting) |
| Payment Term | Shared Master admin | Sales, Purchase (snapshotted onto commitment) |
| Currency / Rate | Shared Master admin (Rate: root-company only) | Sales, Purchase (snapshotted onto commitment) |
| Document Sequence | Shared Master admin | Sales, Purchase, Inventory (any document needing a reference number) |
| Warehouse / Location | Shared Master / Inventory admin | Inventory directly; Sales/Purchase only where a line has physical fulfillment |
| Company / Branch | Shared Master admin (hierarchy immutable after creation) | All domains, for access scoping |
| Cost Dimension | Shared Master admin | Sales, Purchase (symmetric) |
