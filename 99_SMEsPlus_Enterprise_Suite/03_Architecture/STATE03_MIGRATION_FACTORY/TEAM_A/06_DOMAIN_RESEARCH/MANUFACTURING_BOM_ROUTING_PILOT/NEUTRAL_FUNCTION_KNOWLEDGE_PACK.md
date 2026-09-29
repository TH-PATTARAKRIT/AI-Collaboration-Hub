> Domain: MANUFACTURING_BOM_ROUTING_PILOT | Neutral Function Knowledge Pack | Clean-Room boundary: eligible for STATE04 consideration only after STATE04's own separate authorization

# NEUTRAL FUNCTION KNOWLEDGE PACK

Per Master Prompt §10: this is the sanitized companion to `06_BUSINESS_RULE_REGISTER.md` (the Restricted Reference Evidence Annex, which retains evidence URLs/pointers and is research-only access). This pack contains business purpose, business rules, neutral state/event/data concepts, dependency, risk, and Unknowns only — no evidence URLs, no Odoo menu paths, no field-level identifiers, no source code, no schema/ORM structure. It is not itself an authorization for STATE04, Functional Design, or any target-system decision.

### BRP-F01 — Production-routing classification

- **Business purpose**: A product must be classified into one of three production models before it can be built, bundled, or outsourced.
- **Business rule**: Exactly one classification applies per product-build definition — in-house build, pre-bundled set of parts, or externally-produced.
- **Neutral state**: Classification set → downstream production/financial treatment follows automatically from that classification.
- **Data concept**: The classification is a property of the build definition itself, not a separate configuration record.
- **Dependency**: Every other function in this pack is a specialization of one of the three classifications this function selects between.
- **Risk**: Misclassifying a product's production model creates unnecessary process overhead (treating a bundle as a build) or, in the outsourced case, a financial-control risk (see below).
- **Unknown**: Whether the classification can be changed once other business documents already rely on it.

### BRP-F02 — Bundled-product handling (no separate production step)

- **Business purpose**: Some products are sold as an assembled set of parts without an independent production event.
- **Business rule**: A bundled product carries no independent value of its own — its value is entirely the sum of its parts.
- **Neutral state**: Sale of the bundle → the parts move directly; no intermediate production-state machine.
- **Data concept**: The bundle is a sellable identity layered over its components, not a separately valued object.
- **Risk**: Low for value integrity (value simply follows the parts); the risk is process misclassification (see BRP-F01).
- **Unknown**: Behavior when a bundle also requires a light production step before it can ship (a hybrid case).

### BRP-F03 — Outsourced production

> **Conditional Reference Finding — requires version, installed-module, location/ownership, costing/valuation configuration, and evidence-pointer scope. Not a universal accounting statement; not SMEsPlus target behavior.**

- **Business purpose**: Production of a product (or its components) is carried out by an external party rather than in-house.
- **Business rule**: Materials sent to the external party for production remain the sending organization's own asset value throughout the outsourced-production window; this is achieved by treating the external party's premises as an internal location for asset-ownership purposes, not an external one. When production completes and the external party's own service/fee is billed, that fee becomes part of the finished item's recorded value.
- **Neutral state**: Materials at home → materials at external-party location (ownership unchanged) → external party's output returns, service fee recorded into the item's value.
- **Data concept**: A location-ownership distinction (internal vs. external), not a partner-type distinction, is the control point that preserves value continuity.
- **Control**: A financial-control-significant configuration choice — how the external party's location is classified determines whether value continuity holds.
- **Dependency**: The returned item's completion event is the analog of an in-house build's completion event for financial-recording purposes.
- **Risk**: **Material** — if the external-party location were ever classified as external rather than internal, value would incorrectly leave the books during the outsourced-production window, understating recorded asset value.
- **Unknown**: The precise mechanism by which the external party's fee is separated from component value in the recorded figure.

### BRP-F04 — Production-resource cost rate

- **Business purpose**: Production consumes not just materials but time at a resource (a station, a machine, a bench), which has its own cost.
- **Business rule**: A named production resource carries a cost-per-time-unit rate; a production step must reference a resource to be costed.
- **Neutral state**: Resource defined, rate set → referenced by one or more production steps → consumed at execution time.
- **Data concept**: A shared, reusable resource — one resource can serve many production steps; a rate change affects all future, not past, costed steps.
- **Dependency**: Feeds the overall production-cost computation as one of its inputs.
- **Risk**: A stale or misconfigured rate silently misvalues every future production step using that resource — cumulative, not a single-transaction error.
- **Unknown**: Whether the rate supports time-based variation (e.g., differential rates by shift).

### BRP-F05 — Production step sequencing

- **Business purpose**: A single build often requires more than one production step in sequence.
- **Business rule**: Each step names its resource and an expected duration; steps combine to determine total production time and cost.
- **Neutral state**: Steps defined → each becomes a trackable unit of work at build-execution time.
- **Data concept**: A step belongs to one build definition; a resource (BRP-F04) is shared across many.
- **Dependency**: Combines with BRP-F04's rate to produce the labor/operations-cost component of total production cost.
- **Risk**: An inaccurate expected duration misprices every build using that sequence, compounding with any resource-rate error.
- **Unknown**: Behavior when step sequencing is not used at all; whether actual-versus-expected duration is tracked.

## Clean-Room compliance statement

No source code, method name, table/field name, ORM relationship, physical schema, UI element, or menu path appears above. No SMEsPlus target design, schema, workflow, or architecture decision is implied or authorized by this pack. This pack is Odoo-reference learning input only, per the Master Prompt's Clean-Room boundary (§10), and is not itself eligible for STATE04 use until STATE04 is separately authorized.
