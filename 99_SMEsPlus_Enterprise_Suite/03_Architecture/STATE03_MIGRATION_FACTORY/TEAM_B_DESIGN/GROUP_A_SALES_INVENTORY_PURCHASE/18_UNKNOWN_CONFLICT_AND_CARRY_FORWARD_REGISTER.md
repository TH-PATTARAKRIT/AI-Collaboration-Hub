> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B (Independent Canonical Domain Design)
> Phase 11/16 — Unknown / Conflict / Carry-Forward Consolidation

# 18 — UNKNOWN, CONFLICT AND CARRY-FORWARD REGISTER

## 00 — Classification Vocabulary (Governing Prompt §16)

`RESOLVED BY APPROVED EVIDENCE` | `NOT MATERIAL TO CURRENT DESIGN` | `CONTROLLED CARRY-FORWARD` |
`DESIGN DECISION BLOCKED AT THIS POINT` | `OUT-OF-SCOPE — REGISTER ONLY`

## 01 — The Six Mandatory Carry-Forwards (Governing Prompt §16) — Full Disposition

| # | Carry-forward | Classification | Disposition |
|---|---|---|---|
| 1 | Internal workflow/permission semantics of `sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve` | `CONTROLLED CARRY-FORWARD` | Vendor-neutral shape designed in [13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §03; internal logic explicitly `HOLD`, per Boss Gate §4.1. Resolvable only by obtaining the three modules' source code — a PMO/Boss action item, not a TEAM B research gap. |
| 2 | `account.fiscal.position` base logic | `CONTROLLED CARRY-FORWARD` | Fact-of-substitution designed as an interface requirement in [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md) §06; algorithm itself out of scope (Accounting Core domain) regardless of whether it is ever resolved. |
| 3 | Orphaned `res.partner` multi-brand/multi-HQ columns | `CONTROLLED CARRY-FORWARD` | Not designed into the canonical Party concept ([04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §01) — no multi-brand/HQ capability invented. If a real multi-brand/HQ requirement is later confirmed by evidence, it is new scope for a future session, not an extension of this one. |
| 4 | Two uncoordinated Thai branch implementations | `CONTROLLED CARRY-FORWARD` | TBRAC-classified in [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) §01 item 1; canonical Party design treats Tax-Branch as one attribute, explicitly not designed to accommodate two competing sources of truth. |
| 5 | Remaining Medium/Low gaps from Team A's Unknown/Conflict/Evidence Gap Register | See §02 below — full item-by-item disposition | None silently dropped |
| 6 | Real-user validation items from TBRAC evidence | `CONTROLLED CARRY-FORWARD` | Fully consolidated in [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) |

## 02 — Team A's Remaining High/Medium/Low Items — Full Disposition

| Team A # | Item | Team A tier | TEAM B classification | Disposition |
|---|---|---|---|---|
| High #4 | `account.fiscal.position` base model | High | `CONTROLLED CARRY-FORWARD` | Same as §01 item 2 — duplicate reference, single disposition |
| High #5 | Orphaned `res.partner` multi-brand/HQ columns | High | `CONTROLLED CARRY-FORWARD` | Same as §01 item 3 |
| High #8 | Two uncoordinated Thai branch modules | High | `CONTROLLED CARRY-FORWARD` | Same as §01 item 4 |
| Medium #10 | `stock_move.is_in`/`is_out` column semantics | Medium | `NOT MATERIAL TO CURRENT DESIGN` | Implementation-level compute detail; the business fact it would support (movement direction) is already covered by the canonical Movement Instruction's source/destination model ([05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §01) |
| Medium #11 | `returned_move_ids` field definition | Medium | `NOT MATERIAL TO CURRENT DESIGN` | The business fact (Reversal traceability) is independently designed and elevated to a first-class requirement in [05](05_INVENTORY_CORE_CANONICAL_DESIGN.md) §05, regardless of the reference field's exact definition |
| Medium #12 | `produce_line_ids` (likely MRP) | Medium | `OUT-OF-SCOPE — REGISTER ONLY` | Manufacturing domain, not researched or designed by GROUP A |
| Medium #13 | Owning module for `sale_order_line.is_service` | Medium | `NOT MATERIAL TO CURRENT DESIGN` | Stock-vs-service determination is independently designed from the Product type attribute ([04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §02), not from this column |
| Medium #14 | `product.type` literal `'product'` value alongside `'consu'` | Medium | `NOT MATERIAL TO CURRENT DESIGN` | Canonical Product type design ([04](04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md) §02) does not depend on this unexplained legacy value |
| Medium #15 | Owning module for remaining `purchase_order_line` unexplained columns | Medium | `NOT MATERIAL TO CURRENT DESIGN` | The material ones (`sale_line_id`, `purchase_request_id`) were resolved in evidence and are designed in [08](08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md) §09 and [07](07_PURCHASE_CANONICAL_DESIGN.md) §04; remaining unnamed columns carry no known business-semantic weight |
| Medium #16 | Full contents of `stock_dropshipping/models/stock.py` | Medium | `NOT MATERIAL TO CURRENT DESIGN` | Dropship is already designed at the business-semantic level ([07](07_PURCHASE_CANONICAL_DESIGN.md) §06) as a destination-substitution routing variant; the exact reference implementation detail is not needed at this design level |
| Medium #17 | `stock.rule.Procurement` field typing | Medium (already closed in evidence) | `RESOLVED BY APPROVED EVIDENCE` | Noted for completeness only — evidence itself already closed this before TEAM B began |
| Medium #18 | WHT PND form-code correctness | Medium | `OUT-OF-SCOPE — REGISTER ONLY` | Accounting Core's own domain, per [15](15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md) §07 |
| Medium #19 | Whether Thai district/sub-district address data reaches delivery workflow | Medium | `CONTROLLED CARRY-FORWARD` | Consolidated in [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) §01 item 5 |
| Low #20 | MRP/Repair/Purchase-Requisition extension columns on movement tables | Low | `OUT-OF-SCOPE — REGISTER ONLY` | Manufacturing/Repair domain |
| Low #21 | `stock_warehouse` MRP/repair/subcontracting extension columns | Low | `OUT-OF-SCOPE — REGISTER ONLY` | Same |
| Low #22 | `product_template` unexplained manufacturing/cold-chain columns | Low | `OUT-OF-SCOPE — REGISTER ONLY` | Not material to the Sales/Inventory/Purchase core design; likely a different vertical entirely |
| Low #23 | `num2words` Thai-locale linguistic/legal correctness | Low | `OUT-OF-SCOPE — REGISTER ONLY` | Accounting Core presentation layer |

## 03 — New Open Items TEAM B Itself Introduced During Design (Not in Team A's Register)

These arose from TEAM B's own independent design reasoning and are registered here per the same discipline —
Unknown is not failure, invented certainty is:

| # | Item | Classification | Disposition |
|---|---|---|---|
| N1 | Which single "Invoiced quantity" definition (any-non-cancelled vs. posted-only) SMEsPlus adopts as canonical | `CONTROLLED CARRY-FORWARD` | TEAM B recorded a reasoned recommendation (posted-only) in [11](11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md) §04 but does not treat it as decided — requires Boss/business confirmation |
| N2 | Default value for the Over-Fulfillment/Over-Billing Policy (block/warn/allow) | `CONTROLLED CARRY-FORWARD` | Policy *shape* is designed ([12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §02/§03); default value deferred to Boss/business |
| N3 | Default value for the Sales Confirmation Gate Policy (credit exposure / inventory availability) | `CONTROLLED CARRY-FORWARD` | Policy shape designed ([13](13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md) §04); default deferred |
| N4 | Whether SMEsPlus should offer a Sales-initiated RMA affordance beyond the Inventory-owned Reversal entry point | `CONTROLLED CARRY-FORWARD` | Explicitly not decided; see [16](16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md) §04 |
| N5 | Cross-company handoff mechanism for a single logical transaction spanning multiple Legal Companies within one Tenant | `NOT MATERIAL TO CURRENT DESIGN` (at this evidence depth) | Only thin DB-level evidence exists (`08` §02, never functionally traced); not designed — see [14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md) §06 |
| N6 | Late supply / SLA breach / missing-document exception handling | `CONTROLLED CARRY-FORWARD` | `NOT OBSERVED` in evidence and no business need identified independently; registered rather than invented, per [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §13 |
| N7 | Wrong-item/wrong-quantity as a distinct exception mechanism (vs. covered by edit-in-place + Reversal) | `NOT MATERIAL TO CURRENT DESIGN` | Existing mechanisms judged sufficient; no additional capability designed — [12](12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §16 |

## 04 — Note on the Tenant Concept

TEAM B's addition of Tenant as a SaaS-native boundary layer above Legal Company
([14](14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md) §02) is **not** an Unknown or a carry-forward — it is a
new capability requirement TEAM B introduced because the evidence package (sourced from a single-customer
deployment) had no occasion to address SaaS multi-tenancy at all. It is noted here for completeness so a future
reviewer does not mistake its absence from Team A's evidence for an oversight.

## 05 — No Silent Drops — Completeness Statement

Every item in Team A's `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` (3 originally-Critical, now 0 open;
3 High; 10 Medium; 4 Low) has an explicit disposition above. Every item in the governing prompt's mandatory
six-item carry-forward list (§16) has an explicit disposition. Every new Unknown TEAM B's own design reasoning
surfaced is registered in §03, not resolved by invention.
