# A10 — SaaS / Tenant / Company / Warehouse Boundary Risk Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Classify source company scoping, cross-company leakage risk, warehouse/location scoping, tenant assumptions, unsafe shared config, security observations, migration tenant/company resolution requirements | Claude (Team A, DR-002) | This artifact | 2026-08-31 | Independent Evidence Review (pending) | VERIFIED (source-negative and source-positive findings) | Source behavior never proves SMEsPlus SaaS isolation — advisory risk register only |

**Governing rule restated (DR-002 §7/A10)**: *Source behavior never proves SMEsPlus SaaS isolation.* Every row below is a risk observation about the reference source, not a claim about SMEsPlus's own multi-tenant safety.

## Risk register

| ID | Risk | Evidence | Character | Severity | SaaS/Tenant Implication |
|---|---|---|---|---|---|
| SAAS-01 | `company_id` is the **only** organizational scope on `stock.move` — no branch-level or tenant-level field exists in the core movement model | `stock/models/stock_move.py` (this pass, confirming GROUP A MOV-46) | source code direct | Medium | A SMEsPlus multi-tenant design cannot assume the reference source's own field set provides tenant isolation "for free" — tenant scoping would be an entirely new invariant SMEsPlus must design and enforce, not inherited |
| SAAS-02 | "Branch" in this codebase's Thai-localization layer is implemented as a **child `res.company` record**, structurally unconnected to warehouse/location; a separate "Thai Tax Branch" `Char` field on `res.partner` has **zero** structural link to that company hierarchy | GROUP A Scenario 11 finding (frozen evidence, reused DELTA-FIRST, unrebutted) | source code direct + independent review corroboration | High | If SMEsPlus intends real branch-aware inventory (a named Thailand requirement per the Roadmap's Thai-branch context note), the reference source offers **two independent, uncoordinated** implementations of "branch" — neither is a ready-made pattern to adopt as-is |
| SAAS-03 | No DB CHECK constraint or unique index enforces `stock.quant` bin uniqueness or non-negative quantity at the database layer (A2, A13) — all such guarantees are Python/ORM-layer only | Database direct (GROUP A DB forensics, independently re-verified) | database direct | High | A SaaS platform serving concurrent tenants against a shared or per-tenant database cannot rely on this codebase's own constraint set for data integrity; SMEsPlus must design its own DB-level guarantees, not assume the reference architecture's application-layer-only approach is safe at SaaS scale |
| SAAS-04 | Warehouse configuration (`reception_steps`/`delivery_steps`) is a **code generator** that rebuilds the `stock.rule`/`stock.route` graph on write, not static reference data | This pass (`stock/models/stock_warehouse.py`) | source code direct | Low-Medium | Any migration/provisioning tooling that copies warehouse config between tenants must replicate the generation logic, not just copy rows — a genuine SaaS-provisioning complexity, not a security risk per se |
| SAAS-05 | Three approval modules gate whether a Purchase commitment (and thus an expected physical receipt) proceeds; their internal permission/workflow logic remains unresolved (source absent from the entire local volume, confirmed by both GROUP A and this pass's own module-landscape scan, A1) | GROUP A frozen evidence + this pass's A1 confirmation | negative evidence (confirmed absence) | Medium | Any migration of a customer using these approval modules must treat their authorization logic as an unknown black box, not assume default Odoo purchase-approval semantics apply |
| SAAS-06 | The customer dataset shows **at least 3 instances of uncoordinated, duplicate/parallel Thai-specific customizations** within one build (per GROUP A's Gate Candidate Report red flag #3, reused DELTA-FIRST) | GROUP A frozen evidence | source + DB direct | Medium | A pattern-level signal, not proof: customizations in this vendor ecosystem tend to accrete without central coordination — SMEsPlus multi-tenant design should not assume a single "the Thai way" exists even within one reference implementation |
| SAAS-07 | `product.template.type`/`is_storable`/`tracking` gating logic (A5 §4) is implemented via Python `if`/branching on string literals (`type != 'consu'`) rather than a dedicated enforced invariant — confirmed independently in `sale_stock`, `stock`, and `stock_account` | This pass (multiple files) | source code direct | Low | Migration technical-debt risk (also registered in the External Dependency register, GROUP A §10), not itself a SaaS-isolation risk — included here for completeness since it touches the same gating logic SAAS-03 depends on |
| SAAS-08 | No `procurement.group`/tenant-scoped grouping model exists (A6 §4) — grouping is via `stock.reference`, itself only scoped by `company_id` on the linking documents | This pass (new finding) | source code direct | Low-Medium | Reinforces SAAS-01: cross-domain grouping in this codebase inherits whatever scoping the linking document (`sale.order`/`purchase.order`/`mrp.production`) already has — no independent grouping-level tenant boundary exists to inherit |

## Migration tenant/company resolution requirements (Mandatory Question #15, SaaS portion)

Per the above, a future migration must resolve, independently of source assumptions:
1. Which SMEsPlus tenant/company a given source `company_id`/"branch" record maps to (two uncoordinated source "branch" concepts, per SAAS-02, means this mapping cannot be automatic).
2. What DB-level integrity guarantees SMEsPlus will enforce that the source does not (SAAS-03).
3. How warehouse/route configuration is regenerated (not merely copied) per tenant (SAAS-04).

## Explicit non-claims

This register does **not** claim the reference source is insecure, does **not** claim SMEsPlus inherits any of these risks automatically, and does **not** propose SaaS tenancy implementation, schema, API, ORM, or runtime isolation design — all of which are explicitly out of DR-002 scope (§13 Hard Prohibitions) and deferred to COA-G04S / the SaaS Architecture Freeze gates named in the Learning Priority Matrix.

No Evidence = No Progress. Source behavior never proves SMEsPlus SaaS isolation.
