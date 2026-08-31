> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 9 — SaaS / Multi-Company / Tenant Boundary Design

# 14 — SAAS / MULTI-COMPANY / TENANT BOUNDARY MODEL

## 00 — Independent Framing

TEAM B does not copy the reference system's tenant/company context handling as target design by default (governing
prompt §13.8). What follows is independently reasoned from the evidenced facts about scoping, then explicitly
extended to name a Tenant concept the reference evidence never needed to address (single-customer, on-premise-
style deployment) but SMEsPlus, as a SaaS product, does.

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

- **Independent decision**: TEAM B introduces Tenant as the top-level SaaS isolation boundary, above Legal
  Company, because the evidence package — being sourced from a single customer's on-premise-style deployment —
  never had to model this and provides no evidence either way. This is registered as a **new capability
  requirement**, not inferred from evidence, and is flagged as such.
- All Shared Master, Commercial, Physical, and Supply facts are Tenant-scoped as an outer boundary; no fact of any
  kind may be visible or referenceable across Tenants under any configuration. This is a harder rule than the
  Company/Branch access-scoping below — Tenant isolation has no "accessible branches" equivalent that crosses it.

## 03 — Legal Company / Branch

- Adopted from evidence unmodified (`01` §12, `04` §02): a Branch is a child Legal Company record, not a
  separate structural entity. Currency must match across a hierarchy (root-delegated). Hierarchy position is
  immutable after creation. Both Sales and Purchase resolve an "accessible branches" set for the acting session
  and reject lines referencing a product/party outside it.
- **TEAM B adds one explicit requirement not directly evidenced but required for SaaS completeness**: the
  accessible-branch resolution must itself be Tenant-scoped first, Company-hierarchy-scoped second — i.e., cross-
  tenant leakage through an accessible-branches computation must be structurally impossible, not merely
  policy-prevented.

## 04 — Warehouse / Stock Location

- Adopted unmodified from [04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §05: Warehouse is company-owned and
  immutable-after-creation; Location is optionally shared. A Commercial or Supply Commitment line for a purely
  non-physical (service) product never needs a Warehouse reference.

## 05 — Shared vs. Company-Owned Master Facts

| Concept | Sharing default | Rationale |
|---|---|---|
| Party | Optionally company-scoped (nullable = shared) | Evidenced: a Party can be a group-wide customer/vendor |
| Product/Service | Optionally company-scoped (template-level nullable) | Same pattern |
| Product Classification | Not company-scoped (shared) | Evidenced: no company column found |
| UOM | Not company-scoped (global) | Evidenced |
| Sales Price Rule | Optionally company-scoped | Evidenced |
| Vendor Price Reference | Company-scoped (via the commitment that extends it) | Evidenced |
| Tax Rule | Required company + jurisdiction scope | Evidenced (NOT NULL in reference) |
| Payment Term | Optionally company-scoped | Evidenced |
| Currency | Not company-scoped (global); Rate is company-scoped, settable only at the root of a branch hierarchy | Evidenced |
| Document Sequence | Optionally company-scoped | Evidenced |
| Cost Dimension | Definitions shareable; usage on a posted line always company-attributed | Evidenced |

TEAM B adopts this table as the canonical sharing-default matrix — a deliberate, itemized decision rather than a
blanket "everything is company-scoped" or "everything is shared" default, because evidence shows the reference
system's own choices here are neither uniform nor arbitrary (e.g., Tax Rule's hard company-scoping reflects a
real jurisdictional necessity that Product Classification's global sharing does not need to replicate).

## 06 — Cross-Company Handoff

- Where a single logical transaction spans more than one Legal Company within a Tenant (e.g., an inter-company
  supply chain), TEAM B does not design a specific mechanism in this session — evidence for this scenario is thin
  (only indirectly implied by DB-level inter-company columns, `08` §02, never functionally traced). Registered as
  `NOT MATERIAL TO CURRENT DESIGN` at this session's evidence depth, not designed further; see
  [18](18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md).

## 07 — TBRAC Discipline Applied to This File

No claim in this file elevates any specific company/branch/warehouse convention to "how Thai businesses structure
themselves" — see [16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md)
for the explicit `Unknown / Requires Real-User Validation` classification of that question (evidence item 9 in the
Team A Thailand register), carried forward unresolved here.
