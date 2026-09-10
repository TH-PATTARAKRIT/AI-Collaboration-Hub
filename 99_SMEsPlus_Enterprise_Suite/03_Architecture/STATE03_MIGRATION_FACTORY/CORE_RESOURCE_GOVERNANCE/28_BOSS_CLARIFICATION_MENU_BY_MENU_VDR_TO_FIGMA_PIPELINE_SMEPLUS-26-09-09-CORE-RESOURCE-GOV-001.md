# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# BOSS CLARIFICATION — Menu-by-Menu Very Deep Research to Figma Delivery Pipeline

## Decision Status
BOSS CLARIFICATION — EFFECTIVE IMMEDIATELY

## Boss Intent
Boss clarifies that the design and research lifecycle shall progress by concrete functional subject / menu / master-data area, not only by a broad module-level batch.

When SMEsPlus is ready to design a specific area, that area shall first receive dedicated Very Deep Research sufficient to establish its working knowledge, controls, missing questions and evidence baseline. The resulting evidence then enters the controlled phase pipeline before release to Figma.

Examples include:
- Master Data — Customer & Vendor
- Master Data — Product
- Purchase menus / functions
- Inventory / Warehouse menus / functions
- Sales menus / functions
- Accounting menus / functions
- Expenses menus / functions
- other functional subjects and menu groups as scheduled.

## Canonical Per-Subject Pipeline

For each menu, master-data area, function group or bounded functional subject:

`VERY DEEP RESEARCH / LEARNING FOR THE SUBJECT`
`-> PHASE S`
`-> PHASE SA`
`-> PHASE PRE-MATRIX TEST`
`-> PHASE HANDOFF GATE`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> FIGMA / UX DESIGN`

The purpose is to allow SMEsPlus to complete and release Figma-ready work incrementally by bounded subject rather than wait for every module and menu in the whole ERP to finish together.

## Example — Master Data

### Customer & Vendor
`VDR — CUSTOMER & VENDOR`
`-> PHASE S`
`-> PHASE SA`
`-> PRE-MATRIX TEST`
`-> HANDOFF GATE`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> FIGMA`

### Product
`VDR — PRODUCT`
`-> PHASE S`
`-> PHASE SA`
`-> PRE-MATRIX TEST`
`-> HANDOFF GATE`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> FIGMA`

The same pattern applies to later menu/function subjects.

## Relationship to VDR #2 / #3 / Later Rounds
This clarification does NOT remove the previously approved second and later verification rounds.

There are two distinct research uses:

1. `SUBJECT BASELINE VERY DEEP RESEARCH` — occurs before the subject enters Phase S and provides the primary learning/evidence package used by Phase S, Phase SA, Pre-Matrix Test and Functional Design.
2. `LATER VERIFICATION VERY DEEP RESEARCH` — VDR #2 / #3 / #4 or later may occur after the subject has progressed, to close residual gaps, confirm findings, test additional functions, or respond to Material Delta identified by Phase SA / Pre-Matrix / Functional Design / Figma / later evidence.

Later VDR rounds build on the prior verified evidence and do not reset the subject.

## Phase Responsibilities

### Very Deep Research
Establish the deepest practical knowledge currently available for the bounded subject and produce traceable evidence.

### Phase S
Structure / normalize the research evidence into controlled semantic learning suitable for downstream synthesis.

### Phase SA
Synthesize architecture / functional meaning, ownership, boundaries, controls, dependencies and unresolved questions.

### Phase Pre-Matrix Test
Challenge completeness and detect missing knowledge, contradiction, unsupported assumptions and downstream-readiness gaps.

### Phase Handoff Gate
Assure that downstream teams receive clear PASS / CONDITIONAL / HOLD / OPEN / DEFERRED states, evidence pointers and controlled carry-forward items.

### Functional Design
Turn the assured subject knowledge into a usable functional specification.

### Functional Design Gate
Decide whether the subject is sufficiently clear and stable for Figma.

### Figma
Design the screen / interaction / visual workflow from the approved Functional Design and controlled deltas.

## Figma Menu Coverage Implication
The Figma Menu Coverage Register shall be driven by this per-subject pipeline.

A menu or screen may enter Figma only when its own bounded subject has reached the required Functional Design Gate disposition. Other subjects may continue in Very Deep Research or earlier phases independently.

Therefore:

`FIGMA IS RELEASED BY READY SUBJECT / MENU, NOT ONLY BY WHOLE-ERP COMPLETION.`

`NO MENU TO FIGMA WITHOUT TRACEABLE RESEARCH + PHASE EVIDENCE.`

`NO DOWNSTREAM GUESSING.`

## Controlled Parallelism
Different subjects may be at different lifecycle positions at the same time.

Example:
- Customer & Vendor may already be in Figma.
- Product may be in Functional Design.
- Purchase may be in Pre-Matrix Test.
- Inventory may be in Phase SA.
- Accounting may still be in Very Deep Research.

This is valid provided each subject preserves its own evidence lineage and never skips its required Gate.

## Governance
- `No Evidence = No Progress.`
- `Never Skip Gate.`
- `No repeated question without material delta.`
- `Clear Handoff Before Next Phase.`
- `No Phase Handoff Without Independent Assurance.`
- A later VDR round does not invalidate previously verified work unless Material Delta is proven.
- Material Delta triggers Controlled Re-entry only for affected scope.
- No source-code implementation, merge, deployment or production authorization is created by this clarification.

## Supersession / Clarification Effect
This record clarifies the interpretation of Records 26 and 27.

The earlier statement that VDR #2 may proceed in parallel with Figma remains valid for later verification rounds. However, for a new bounded menu / function / master-data subject, the primary Very Deep Research baseline occurs BEFORE Phase S and before that subject can progress through Phase SA, Pre-Matrix Test, Handoff, Functional Design and Figma.

Boss remains the sole Final Approver.
