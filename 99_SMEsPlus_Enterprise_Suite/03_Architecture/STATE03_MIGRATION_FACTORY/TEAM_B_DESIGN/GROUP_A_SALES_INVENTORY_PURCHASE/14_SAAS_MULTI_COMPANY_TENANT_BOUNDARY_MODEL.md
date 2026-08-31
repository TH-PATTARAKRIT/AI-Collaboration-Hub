> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 9 — SaaS / Multi-Company / Tenant Boundary Design

# 14 — SAAS / MULTI-COMPANY / TENANT BOUNDARY MODEL

## 00 — Independent Framing

TEAM B does not copy the reference system's tenant/company context handling as target design by default (governing
prompt §13.8). What follows is independently reasoned from the evidenced facts about scoping, then explicitly
extended to name a Tenant concept the reference evidence never needed to address (single-customer, on-premise-
style deployment) but SMEsPlus, as a SaaS product, does.

**CORR-008 closure (`FV006-SAAS-001`, `FV006-SAAS-003`, `FV006-XDF-006`, `FV006-GAP-007`) — mandate vs. structure,
stated once and applied throughout this file.** Formal IBPV FV-006 independently confirmed (by direct grep of
`00_Project_Governance/`, not on TEAM B's word) that two distinct things are true, and must not be conflated:

1. **The requirement that a Tenant concept exist is an existing, Boss-controlled, approved-baseline SaaS
   invariant** — traceable to `State_01_Project_Identity/STATE01_PROJECT_CHARTER_v1.0.md` §5 ("SaaS Foundation
   and tenant control"), `State_01_Project_Identity/STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md` (Product Boundary,
   "tenant/company/user control"), and `ARCHITECTURE_GOVERNANCE_STANDARD.md` ("Multi-Tenant by Design," an
   approved Architecture Principle). All three are Boss-approved baseline documents. **This requirement is not
   being re-decided by CORR-008 and Boss has directed that it not be re-litigated per module** — SMEsPlus is
   multi-tenant SaaS by approved mandate, full stop.
2. **The specific structural shape this file defines to satisfy that mandate** — Tenant as a hard layer above
   Legal Company, its sharing/isolation mechanics (§02–§05 below) — **has no approved-baseline counterpart to
   verify against.** No governance document defines what a Tenant *is* structurally, its relation to Legal
   Company, or its isolation mechanics; this file is the first artifact in the corpus to attempt that definition,
   and says so itself (§02). This is a genuine TEAM B design elaboration, not an inherited or independently
   re-verified structural baseline.

CORR-008 does not ask "should SMEsPlus be multi-tenant" (item 1 is settled). It asks TEAM B to stop presenting
item 2's specific structural choices with the same weight as item 1's mandate, and instead classify each material
statement in this file honestly. §08 below is the full classification; every section from here down is corrected
to be internally consistent with that classification. The full statement-by-statement reconciliation, including
every other GROUP A file that references Tenant/Company/Branch scope, is recorded in the dedicated evidence
artifact
[23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md](CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md).

## 01 — Canonical Boundary Layers (Top to Bottom)

```
Tenant                — a SMEsPlus customer account; not evidenced in the reference system at all (SaaS-native
                         concept TEAM B adds independently, since Odoo-derived evidence has no tenant layer above
                         Company — it assumes one deployment per customer)
  └─ Legal Company      — "Company/Branch" hierarchy per 04 §06; currency must match across the hierarchy;
     (+ child Branches)   hierarchy position immutable after creation; access-scoped via accessible-branch resolution
       └─ Warehouse      — company-owned, immutable after creation, per-company-unique identity
          └─ Location    — optionally shared across companies (nullable company scope)
```

Party's Thai Tax-Branch attribute and any other jurisdiction-specific registration identifier are **not** a layer
in this hierarchy — they are attributes on a Party record, fully orthogonal to Tenant/Company/Warehouse/Location.
Restated here because SaaS multi-tenancy is exactly where conflating "tenant boundary" with "tax registration
identifier" would cause real harm (e.g., leaking one tenant's tax-branch data model into another's).

## 02 — Tenant (SMEsPlus-Native Addition)

- **Classification (per §00): the need for a Tenant layer = `EXISTING BOSS-CONTROLLED SAAS INVARIANT`; the
  specific shape below = `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE`.** TEAM B introduces Tenant as
  the top-level SaaS isolation boundary, above Legal Company, because the evidence package — being sourced from a
  single customer's on-premise-style deployment — never had to model this and provides no evidence either way for
  the structural shape. The *decision to add a Tenant layer at all* satisfies an approved mandate (§00 item 1);
  the *specific shape* (a hard layer strictly above Legal Company, with the isolation mechanics below) is TEAM
  B's own reasoned design, registered as a **new capability requirement**, not inferred from evidence, and
  flagged as such — consistent with, not contradicting, the approved mandate.
- All Shared Master, Commercial, Physical, and Supply facts are Tenant-scoped as an outer boundary; no fact of any
  kind may be visible or referenceable across Tenants under any configuration. This is a harder rule than the
  Company/Branch access-scoping below — Tenant isolation has no "accessible branches" equivalent that crosses it.
  **(`TEAM B CANONICAL DESIGN CHOICE` — the absolute no-crossing rule itself is not separately evidenced, but is
  the direct, necessary consequence of the approved "Multi-Tenant by Design" principle combined with the
  project's zero-tolerance tenant-leakage defect policy — see
  [23](CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md) for the full traceability
  chain.)**

## 03 — Legal Company / Branch

- **Classification: `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION`.** Adopted from evidence unmodified (`01`
  §12, `04` §02): a Branch is a child Legal Company record, not a separate structural entity. Currency must match
  across a hierarchy (root-delegated). Hierarchy position is immutable after creation. Both Sales and Purchase
  resolve an "accessible branches" set for the acting session and reject lines referencing a product/party
  outside it. Unlike the Tenant layer (§02), this layer is cited to specific Team A evidence sections and is not
  an independently-asserted new capability — Formal IBPV FV-006 (`FV006-SAAS-002`) found this citation-complete,
  not contradicted, subject only to a future session independently re-opening files `01` and `04` to confirm the
  citations themselves (a verification-completeness note, not a design defect — unchanged by CORR-008).
- **TEAM B adds one explicit requirement not directly evidenced but required for SaaS completeness**
  (`TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE`): the accessible-branch resolution must itself be
  Tenant-scoped first, Company-hierarchy-scoped second — i.e., cross-tenant leakage through an accessible-branches
  computation must be structurally impossible, not merely policy-prevented. This is the concrete mechanism by
  which the mandatory cross-module invariant restated in §00 ("Tenant context is mandatory for tenant-facing
  operations; Tenant + Company context is mandatory for company-scoped operations") is enforced at the one place
  Sales and Purchase actually touch Company/Branch scope.

## 04 — Warehouse / Stock Location

- Adopted unmodified from [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §05: Warehouse is company-owned and
  immutable-after-creation; Location is optionally shared. A Commercial or Supply Commitment line for a purely
  non-physical (service) product never needs a Warehouse reference.

## 05 — Shared vs. Company-Owned Master Facts

**CORR-008 closure (`FV006-SAAS-003`) — reading rule for every row below.** §02's absolute rule ("no fact of any
kind may be visible or referenceable across Tenants under any configuration") governs this table even though the
"Sharing default" column below does not repeat it on every line. **Every value in the "Sharing default" column
describes sharing *within* one Tenant only.** "Not company-scoped (shared)" and "Not company-scoped (global)"
mean shared/global *within the Tenant that owns the record* — never across Tenants. A future implementer reading
this table in isolation must apply Tenant-scoping first, in every row, before applying whatever
company-scoping/sharing default the row states; this is now stated explicitly at the point of use, closing the
gap Formal IBPV FV-006 found between §02's blanket rule and this table's per-row silence on it.

| Concept | Sharing default (always within-Tenant — see rule above) | Rationale |
|---|---|---|
| Party | Optionally company-scoped (nullable = shared, within Tenant) | Evidenced: a Party can be a group-wide customer/vendor, within the owning Tenant |
| Product/Service | Optionally company-scoped (template-level nullable, within Tenant) | Same pattern |
| Product Classification | Not company-scoped (shared within Tenant) | Evidenced: no company column found |
| UOM | Not company-scoped (global within Tenant) | Evidenced |
| Sales Price Rule | Optionally company-scoped (within Tenant) | Evidenced |
| Vendor Price Reference | Company-scoped (via the commitment that extends it; that Company is always within one Tenant) | Evidenced |
| Tax Rule | Required company + jurisdiction scope (within Tenant) | Evidenced (NOT NULL in reference) |
| Payment Term | Optionally company-scoped (within Tenant) | Evidenced |
| Currency | Not company-scoped (global within Tenant); Rate is company-scoped, settable only at the root of a branch hierarchy (that hierarchy is always within one Tenant) | Evidenced |
| Document Sequence | Optionally company-scoped (within Tenant) | Evidenced |
| Cost Dimension | Definitions shareable (within Tenant); usage on a posted line always company-attributed | Evidenced |

TEAM B adopts this table as the canonical sharing-default matrix — a deliberate, itemized decision rather than a
blanket "everything is company-scoped" or "everything is shared" default, because evidence shows the reference
system's own choices here are neither uniform nor arbitrary (e.g., Tax Rule's hard company-scoping reflects a
real jurisdictional necessity that Product Classification's global sharing does not need to replicate). The
"Sharing default" and "Rationale" columns are `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` (each cites the
underlying evidence item); the "always within-Tenant" qualifier applied to every row is the same
`TEAM B CANONICAL DESIGN CHOICE` already classified in §02, restated here per row rather than left implicit.

## 06 — Cross-Company Handoff

- **Classification: `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION`.** Where a single logical transaction
  spans more than one Legal Company within a Tenant (e.g., an inter-company supply chain), TEAM B does not design
  a specific mechanism in this session — evidence for this scenario is thin (only indirectly implied by DB-level
  inter-company columns, `08` §02, never functionally traced). Registered as `NOT MATERIAL TO CURRENT DESIGN` at
  this session's evidence depth, not designed further; see
  [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md). Formal IBPV FV-006 (`FV006-SAAS-004`) independently
  confirmed this as correct scope discipline (declining to design past a real evidence gap), not a defect —
  unchanged by CORR-008.

## 07 — TBRAC Discipline Applied to This File

No claim in this file elevates any specific company/branch/warehouse convention to "how Thai businesses structure
themselves" — see [16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md)
for the explicit `Unknown / Requires Real-User Validation` classification of that question (evidence item 9 in the
Team A Thailand register), carried forward unresolved here.

## 08 — SaaS/Tenant Statement Classification Table (CORR-008 closure, `FV006-SAAS-001`/`003`, `FV006-XDF-006`,
`FV006-GAP-007`)

Every material Tenant/Company-scope statement in this file, classified per §00's five-category scheme. This is
the summary view for this file specifically; the full cross-file sweep covering every other GROUP A artifact that
uses Tenant/Company/Branch scope is in
[23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md](CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md).

| # | Statement | Location | Classification |
|---|---|---|---|
| 1 | A Tenant concept must exist as the top-level SaaS isolation boundary | §02 | `EXISTING BOSS-CONTROLLED SAAS INVARIANT` |
| 2 | Tenant sits as a hard layer strictly above Legal Company; no fact crosses Tenants under any configuration | §01, §02 | `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE` |
| 3 | Accessible-branch resolution is Tenant-scoped first, Company-hierarchy-scoped second | §03 | `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE` |
| 4 | Legal Company is a "Company/Branch" hierarchy; Branch is a child Company record; currency matches across hierarchy; hierarchy position immutable | §03 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` |
| 5 | Warehouse is company-owned and immutable-after-creation; Location optionally shared | §04 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` |
| 6 | Per-concept sharing defaults (Party, Product/Service, Product Classification, UOM, Sales Price Rule, Vendor Price Reference, Tax Rule, Payment Term, Currency, Document Sequence, Cost Dimension) | §05 | `EVIDENCE-SUPPORTED GROUP A DESIGN ELABORATION` (sharing default itself) + `TEAM B CANONICAL DESIGN CHOICE` (the "always within-Tenant" qualifier applied to every row) |
| 7 | Cross-company handoff mechanism within one Tenant | §06 | `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION` |
| 8 | Whether real Thai SME businesses actually structure themselves per the Company/Branch hierarchy modeled here | §07 (cross-ref [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md)) | `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION` |

**No statement in this file is classified `DESIGN DECISION BLOCKED AT THIS POINT`.** Every material Tenant
structural rule this file needs is either traceable to an approved invariant, cited to Group A evidence, or an
explicitly-labeled TEAM B design choice with stated rationale — none requires a new material structural decision
that cannot currently be made safely. This directly answers the Formal IBPV traceability defect
(`FV006-SAAS-001`, `FV006-XDF-006`, `FV006-GAP-007`): the *requirement* was always traceable; what was missing
was this classification making clear that the *structural shape* is TEAM B's own reasoned elaboration, not a
second, independently-verified baseline fact. That gap is closed by this section and by
[23](CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md).
