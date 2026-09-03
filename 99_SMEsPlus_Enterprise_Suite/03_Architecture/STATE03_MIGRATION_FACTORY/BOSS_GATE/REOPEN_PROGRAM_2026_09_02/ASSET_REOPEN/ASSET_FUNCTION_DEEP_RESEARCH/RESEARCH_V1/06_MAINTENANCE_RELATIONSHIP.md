# 06 — Maintenance Cost Relationship (Direct Challenge)

Session: `SMEPLUS-26-09-03-ASSET-FUNCTION-DR-001` | Status: `EVIDENCE COLLECTION — CHALLENGE, NOT ASSUMPTION`

---

## 1. The Question, Stated Directly

Per governing brief research object 03: does maintenance cost actually enter Equipment Cost / Work Center Cost / WIP / MO / Product Cost in the reference ERP, or is it tracked independently? This file does not assume integration and actively looks for evidence against it as well as for it.

## 2. What Is Documented

- **Work Center cost mechanism (confirmed, file `12`/`04` cross-reference)**: a Work Center has a documented "Cost per hour" concept composed of a per-workcenter rate and/or a per-employee rate (with individual employee hourly-cost override), which feeds the calculated cost of a manufacturing operation performed at that work center. This is a **labor/machine-time-rate** mechanism, not a maintenance-cost mechanism.
- **Maintenance Request cost fields**: no official documentation page located in this session's retrieval describes a cost/amount field on a Maintenance Request record itself (e.g., "cost of this repair," "parts cost," "technician labor cost"). This is a negative finding — the search specifically looked for this and did not find it documented as a native field.
- **No documented linkage** was found between a Maintenance Request (even where a cost might be manually tracked via linked purchase orders for spare parts, which is plausible but not documented as a structured feature) and the Work Center's Cost per Hour field, a Manufacturing Order's cost breakdown, or a Product's cost. No "maintenance cost automatically raises the work center rate" mechanism, no "maintenance cost automatically posts to WIP" mechanism, and no "maintenance cost automatically absorbs into product cost" mechanism was located.

## 3. Finding

`CONTRADICTED (of the assumption that maintenance cost automatically integrates into Equipment/Work Center/WIP/MO/Product cost)`. On the evidence retrieved, maintenance cost in the reference ERP appears to be **tracked independently** of the manufacturing costing stack — at most, maintenance-related purchases (spare parts, external repair invoices) would flow through the general purchasing/expense accounting path like any other vendor bill, landing in whatever expense account that bill's product/account configuration points to, with no documented automatic bridge into Work Center cost-per-hour or Manufacturing Order cost. This is consistent with, and reinforces, the file `04` finding that Equipment and the fixed-asset Asset concept are not natively linked either — the reference ERP's maintenance domain appears designed as an operational/scheduling tool first, with cost accounting treated as a separate, largely unconnected concern.

This should not be read as certainty of absence in every version and configuration of the reference ERP — it is a documentation-search negative finding, reasonably corroborated by the absence of any positive counter-evidence across the queries run, but not a claim that no such feature could exist in some edition or add-on module not surfaced by this session's searches.

## 4. Accounting Meaning

If confirmed (independent verification recommended before final design), this means: any SMEsPlus design that assumes maintenance cost flows automatically into production/product cost is **not adapting a reference-ERP pattern** — it would be new design work, and moreover would need its own explicit mechanism (e.g., a maintenance-cost allocation rule) since none exists to study. This directly informs Hypothesis A (file `21`) evaluation: Hypothesis A is about *depreciation* flowing into production cost, a related but distinct question from maintenance cost — the two should not be conflated. Maintenance cost integration is evidenced as weaker/absent; depreciation-to-production-cost integration is addressed separately in files `11`–`13`.

## 5. SMEsPlus Candidate Semantics (Layer C)

`DESIGN CANDIDATE`: if SMEsPlus wants maintenance cost visible in Equipment/Work Center/product costing (a reasonable operational-management goal, distinct from statutory financial accounting), it should be built as an explicit, separately-controlled internal costing feature — analogous in spirit to the Off-Balance internal usage costing candidate in file `14` — rather than assumed to piggyback on any reference-ERP mechanism, because none was found to piggyback on.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
