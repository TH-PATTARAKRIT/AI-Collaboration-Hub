# DOMAIN_01 ACCOUNTING CORE — TEAM B DESIGN EVIDENCE PACK

| Field | Value |
|---|---|
| Project | SMEsPlus ENTERPRISE SUITE |
| STATE | STATE03 — Architecture |
| Workstream | SMEsPlus Migration Factory |
| Board | Board06 — Data & Canonical Model |
| Domain | DOMAIN_01 — Accounting Core |
| Team | Team B — Independent Clean-Room Design |
| Directive | SMEPLUS-26-08-29-MIG-B-D01-E2E-001 |
| Date | 2026-08-29 |
| Executor | Claude Sonnet 5 |

## 1. Executive Summary

Team B independently designed the Accounting Core domain for SMEsPlus across eighteen
mandatory phases (B0–B17), starting only from Team A's audited, sanitized candidate input —
never from vendor source. The design's central thread addresses the single weakness Team A's
independent research identified as most severe: the reference system permits a committed,
even externally-reported, financial fact to be silently returned to an editable state and
altered, with no forced trace. This design closes that gap structurally (a Consumption Gate,
[B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §4) rather than procedurally, and applies the
same discipline — measured advancement, not imitation — across nine further capability areas
([B12](B12_REFERENCE_TO_ADVANCEMENT_DESIGN.md)). An internal red-team pass
([B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md)) found and fixed six real design gaps before
this pack was assembled. Clean-room provenance was independently verified twice
([B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md), [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §8):
zero critical vendor-derived design risk.

## 2. Authorized Input

`TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/13_TEAM_B_CANDIDATE_INPUT.md`,
authorized by `TEAM_B_HANDOFF/DOMAIN_01_ACCOUNTING_CORE_E_TEAM_B_HANDOFF_AUTHORIZATION.md`
(commit `2314a786d9a1918f4cf4de3da7c2f8b85d3c98fe`), itself gated by
`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_D_BOSS_GATE_DECISION_PACK.md` (commit
`512da309b0bbe597a1343ce386302d8f870d1fcf`). Full verification chain, including the
governance discrepancy this session found and resolved against the live authoritative
repository, is recorded in
[B00](B00_GOVERNANCE_AND_HANDOFF_VERIFICATION.md).

## 3. Scope

DOMAIN_01 Accounting Core only. Conceptual/domain design. No code, no physical schema, no
ORM, no migration implementation, no API. See
[B03](B03_DOMAIN_BOUNDARY_MODEL.md) §4/§4a for the explicit out-of-scope boundary and the
inter-company-transaction clarification added during red-team review.

## 4. Independent Design Principles

`Understand the reference deeply. Rebuild independently. Improve measurably.` Applied
concretely: every capability (§6) was defined from business responsibility first, checked
against — and in three documented respects diverges from — the reference system's actual
module shape ([B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md) §3).

## 5. Capability Model

Nine capabilities: Chart of Accounts Governance, Financial Fact Capture & Commitment,
Correction & Reversal, Period Control, Company/Entity Boundary Enforcement, Currency
Recognition & Remeasurement, Regulated Document Integrity, Audit Trail & Evidence Provision,
Period-End Carry-Forward. Full definitions, ownership, and dependency graph:
[B02](B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md).

## 6. Domain Boundaries

Boundary statement, nine conceptual objects (Financial Fact, Entry, Line, Posting, Ledger,
Period, Currency Context, Correction/Reversal, Audit Evidence), eleven neighbor seams, and
explicit out-of-scope list: [B03](B03_DOMAIN_BOUNDARY_MODEL.md).

## 7. Lifecycle / Event Model

Four states (DRAFT, COMMITTED, VOIDED, SUPERSEDED — the last a Team B addition), nine forced
event types, and the Consumption Gate — the domain's central original design contribution,
extending Team A's neutral observation into an actual enforced mechanism:
[B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md).

## 8. Invariant Baseline

Ten invariants (BINV-01..10): six independently re-evaluated from Team A's INV-01..06, four
newly added (Consumption Record Permanence, Audit Evidence Independence, Account Category
Immutability, Carry-Forward Correctness). All six mandated coverage areas confirmed:
[B05](B05_ACCOUNTING_INVARIANT_BASELINE.md).

## 9. Business Rule Baseline

Fifteen rules (BR-01..15): thirteen restated from Team A's GR-01..13 in this domain's own
vocabulary — three explicitly strengthened past the reference system's observed weaknesses
(BR-05 no bypass, BR-07 no mutation of consumed facts, BR-13 full deprecation guard) — plus
two new rules (BR-14 Amendment, BR-15 Consumption recording):
[B06](B06_BUSINESS_RULE_BASELINE.md).

## 10. Conceptual Information Model

Eleven conceptual entities, cardinality rules tied to specific invariants, three identity
principles (no source-ID reuse; identity independent of display numbers; Audit Events
identified by append-only sequence alone), amended during red-team review to add Normal
Balance Side and tenant/company-scoped Audit Event identity:
[B07](B07_CONCEPTUAL_INFORMATION_MODEL.md).

## 11. Accounting & Mathematical Design Principles

Ten principles (MP-01..10) covering all eleven mandated areas, including an explicit proof
that the accounting equation is a corollary of per-entry balance (not a separate check), a
proof that a constructed reversal is automatically balanced, and a proposed rounding policy
where Team A's evidence left the question open (flagged for gate confirmation):
[B08](B08_ACCOUNTING_MATHEMATICAL_DESIGN_PRINCIPLES.md).

## 12. Control / Audit Design Objectives

Thirteen objectives (CO-01..13, the last two added during red-team review) covering all
twelve mandated areas plus an explicit residual scope boundary (infrastructure-level bypass
is outside this domain's control-design reach):
[B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md).

## 13. Migration Requirements

Thirteen canonical, source-neutral requirements (MG-C01..13, the last added during red-team
review to cover source-side unposted activity at cutover): [B10](B10_CANONICAL_MIGRATION_REQUIREMENTS.md).

## 14. Exception Model

Eighteen scenarios, six requiring genuinely new design (wrong tenant, duplicate detection,
future posting, missing reference, concurrency, partial failure) because Team A's evidence
either declined to analyze them or found the reference system's own answer unproven:
[B11](B11_EXCEPTION_FAILURE_MODEL.md).

## 15. Advancement Design

Nine advancement items (AD-01..09, the last identified independently by Team B, not present
in Team A's ADV-01..08), each with a chosen design mechanism and a measurement criterion:
[B12](B12_REFERENCE_TO_ADVANCEMENT_DESIGN.md).

## 16. Design Options / Trade-offs

Six significant decisions formally compared across eight dimensions each, with Team-B-only
recommendations explicitly marked not-yet-approved: [B13](B13_DESIGN_OPTION_TRADEOFF_REGISTER.md).

## 17. Clean-Room Provenance

Every material decision mapped to Accounting Standard / Regulatory Requirement / Industry
Principle / Cross-ERP Pattern / Team A Fact / Migration Requirement / Independent Reasoning.
Three vendor-adjacent terms individually reviewed and confirmed traceability-only.
**Critical Vendor-Derived Design Risk = 0**: [B14](B14_CLEAN_ROOM_PROVENANCE_MATRIX.md).

## 18. Traceability

Full chains traced end-to-end for three exemplar threads; one ID-space collision and one
rule-interaction gap found and resolved explicitly (not silently); zero orphan critical
decisions, zero circular definitions, zero regulatory overreach:
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md).

## 19. Residual Unknowns

Team A's full 20-item residual register carries forward unchanged, incorporated by reference
([B01](B01_AUTHORIZED_INPUT_REGISTER.md) §11). This domain's design does not depend on any of
them resolving in a particular direction (see [B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6 for
the two items — OQ-01, OQ-02 — explicitly checked against this design's dependencies).

## 20. Assumptions

Six Team B design assumptions requiring gate confirmation, consolidated in
[B15](B15_DESIGN_TRACEABILITY_MATRIX.md) §6: rounding method (round-half-up), period-close as
automatic consumption trigger, chart-of-accounts template/instance structure, audit-trail
tamper-evidence scope beyond evidenced legal requirement, flexible correction shape, and the
CO-02/CO-06 configuration-coupling rule found during traceability review.

## 21. Red-Team Findings

Ten personas engaged; six real, substantive gaps found and fixed (not merely noted); two
areas checked and confirmed already-adequate without padding; two areas confirmed correctly
out of this phase's scope. Full record, including the fixes' exact text:
[B16](B16_TEAM_B_INTERNAL_RED_TEAM_REVIEW.md).

## 22. Acceptance Criteria

```
B0–B16 evidence artifacts completed          : YES (17 of 17 prior phases)
Authorized Input fully registered            : YES (B01)
Critical invariants traceable                : YES (B05, B15)
Critical rules traceable                     : YES (B06, B15)
Conceptual design complete                   : YES (B07)
Math/accounting principles defined           : YES (B08)
Lifecycle/events coherent                    : YES (B04)
Control objectives defined                   : YES (B09)
Migration requirements defined               : YES (B10)
Critical exceptions analyzed                 : YES (B11)
Advancement criteria measurable              : YES (B12)
Design options documented                    : YES (B13)
Critical Vendor-Derived Design Risk = 0      : YES (B14)
Critical orphan design decisions = 0         : YES (B15)
Class G items still visible                  : YES (B01 §11, B15 §6, this section §19)
Regulatory scope not overstated              : YES (B09 CO-07/CO-11, B15 §7)
Internal Red-Team completed                  : YES (B16)
```

## 23. Measured Advancement Criteria (summary — full detail in B12)

| Item | Reference-system status | This design's target |
|---|---|---|
| AD-01 Balance guarantee | Suppressible, app-only, 0 DB triggers | Structurally non-optional |
| AD-03 Period control mechanisms | 8+ independent, disagreeing controls | 1 authoritative answer + 1 logged override path |
| AD-04 Consumed-fact correction | Both sound and unsound paths coexist, unforced | 100% additive for consumed facts, structurally enforced |
| AD-06 Monetary representation | 3 independently-writable columns, structurally-possible disagreement | 2 authoritative values, derived views only |
| AD-09 Multi-tenant safety | Not evaluated (single-deployment reference) | 0 capabilities requiring cross-tenant shared state |

**Evidence Pack complete. Proceeding to self-review (G) and Final Gate Candidate (H).**
