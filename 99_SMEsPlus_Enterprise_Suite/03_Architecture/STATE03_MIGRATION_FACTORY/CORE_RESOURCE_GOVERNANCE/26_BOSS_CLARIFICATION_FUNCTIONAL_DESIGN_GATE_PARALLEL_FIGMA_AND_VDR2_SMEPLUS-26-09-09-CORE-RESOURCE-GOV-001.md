# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# BOSS CLARIFICATION — Functional Design Gate Starts Parallel Figma + Very Deep Research #2

## Decision Status
BOSS CLARIFICATION — EFFECTIVE IMMEDIATELY

## Clarified Lifecycle Intent
Boss clarifies that `Very Deep Research #2` belongs at the `FUNCTIONAL DESIGN GATE` transition as a second verification / gap-fill stream running in parallel with Figma work after Functional Design has passed its Gate.

The research questions for Very Deep Research #2 are NOT expected to be invented during Functional Design authoring. The principal sources of the missing-knowledge / study agenda are the findings produced earlier by `Phase SA` and `Phase Pre-Matrix Test`.

Those phases are responsible for exposing what remains unclear, incomplete, contradictory, under-evidenced, or insufficiently understood and therefore what must be researched further.

## Canonical Flow

`EARLY DEEP RESEARCH / LEARNING`
`-> PHASE SA`
`-> PHASE PRE-MATRIX TEST`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> if PASS:`
`   |- FIGMA / UX DESIGN PROCEEDS IN PARALLEL`
`   |- VERY DEEP RESEARCH #2 PROCEEDS IN PARALLEL`
`      using the open questions / gaps / study targets identified by Phase SA + Phase Pre-Matrix Test`
`-> CONTROLLED DELTA FEEDBACK`
`-> NEXT CONTROLLED HANDOFF / PHASE`

## Purpose of Very Deep Research #2

Very Deep Research #2 is a `Second Verification / Gap-Fill` cycle. Its purpose is to:

- close residual knowledge gaps identified by Phase SA and Phase Pre-Matrix Test;
- verify supplementary / secondary functions and controls;
- collect missed operational details and edge cases;
- confirm or challenge assumptions that did not justify blocking Functional Design;
- produce controlled ADD / REDUCE / REFINE / REMOVE recommendations;
- preserve evidence lineage from SA / Pre-Matrix findings through Functional Design and into the second verification cycle.

It is NOT a general blocker for Figma after Functional Design Gate PASS.

## Figma Parallelism Rule

`FUNCTIONAL DESIGN GATE PASS -> FIGMA MAY PROCEED.`

At the same time:

`FUNCTIONAL DESIGN GATE PASS -> VERY DEEP RESEARCH #2 MAY PROCEED IN PARALLEL.`

The two streams are intentionally parallel so UI/UX design is not delayed by non-material research completion.

## Delta Handling

### Non-Material Delta
Examples: supplementary function, additional field/control, reduced field, refined rule, minor interaction impact, secondary edge case.

Disposition:

`CONTROLLED DELTA -> UPDATE AFFECTED FUNCTIONAL DESIGN / FIGMA ARTIFACT ONLY -> NO GENERAL RESET`

### Material Delta
If Very Deep Research #2 discovers a finding that invalidates a foundational Functional Design assumption, primary workflow, accounting/legal control, security boundary, data-integrity invariant, or other material behavior:

`MATERIAL DELTA -> CONTROLLED RE-ENTRY FOR AFFECTED SCOPE ONLY -> RE-VERIFY -> RE-HANDOFF`

The entire module / project is not automatically reset or blocked.

## Governance Meaning

Phase SA + Phase Pre-Matrix Test act as the principal detectors of unresolved knowledge before Functional Design is released.

Functional Design Gate determines whether the design is sufficiently clear and stable for Figma to begin.

Very Deep Research #2 then acts as the second-pass verification stream that closes the residual, mostly non-primary gaps while Figma proceeds.

## Canonical Rules

`SA + PRE-MATRIX IDENTIFY WHAT WE STILL NEED TO LEARN.`

`FUNCTIONAL DESIGN GATE DECIDES WHETHER FIGMA MAY PROCEED.`

`FIGMA + VERY DEEP RESEARCH #2 RUN IN PARALLEL AFTER FUNCTIONAL DESIGN GATE PASS.`

`NO DOWNSTREAM GUESSING.`

`NO EVIDENCE = NO PROGRESS.`

`NO REPEATED QUESTION WITHOUT MATERIAL DELTA.`

Boss remains the sole Final Approver.
