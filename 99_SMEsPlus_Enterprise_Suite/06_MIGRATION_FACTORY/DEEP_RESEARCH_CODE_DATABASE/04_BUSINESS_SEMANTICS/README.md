# 04 — Business Semantics

Purpose: express business meaning independently from implementation and prepare evidence-backed inputs for later clean-room design.

## Required Semantic Record

For every important business object or process, identify:

- Business entity and purpose
- Actors and authority
- Input facts and output facts
- Lifecycle and status meaning
- Business rules and validations
- Dependencies and cross-domain effects
- Accounting consequences
- Inventory consequences
- Approval implications
- Statutory / localization relevance
- Historical-data relevance
- Migration requirement
- Edge cases and failure modes

## Required Analytical Layers

1. Observed behavior
2. Inferred business semantic
3. Domain invariant or mathematical rule
4. Unverified assumption, if any
5. Independent target-design candidate, only after clean-room review

## Blueprint Outputs

Evidence-backed semantic findings may later support:

- Mathematical models
- State machines and domain events
- Vendor-neutral conceptual/logical ERDs
- DDD aggregates and bounded contexts
- Use cases and domain services
- API contracts and DTOs

No target-design statement is valid unless its source semantics, clean-room transformation, and independent rationale are recorded.

All detailed findings must be registered in `99_EVIDENCE_REGISTER/BUSINESS_SEMANTIC_REGISTER.csv`.
