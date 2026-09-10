# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# BOSS DIRECTION — Figma Menu Coverage Register & Continuous Very Deep Research Alignment

## Decision Status
BOSS DIRECTION — EFFECTIVE IMMEDIATELY

## Boss Intent
SMEsPlus will re-verify core operating modules multiple times, not only once or twice, because the objective is to achieve the most complete and robust operating system possible.

Initial examples include, but are not limited to:
- Purchase
- Inventory / Warehouse
- Sales
- Accounting
- Expenses
- and other functional modules as they enter the same lifecycle.

The Figma design stream MUST therefore maintain a menu/screen coverage structure that remains traceable to continuing Very Deep Research findings.

## Canonical Rule
`FUNCTIONAL DESIGN GATE PASS -> FIGMA MAY PROCEED.`

`VERY DEEP RESEARCH MAY RECUR MULTIPLE TIMES BY MODULE.`

`FIGMA MENU COVERAGE MUST REMAIN TRACEABLE TO EVERY CONTROLLED RESEARCH DELTA.`

`NO SILENT MENU OR SCREEN CHANGE.`

## Required Artifact — Figma Menu Coverage Register
SMEs Core and the relevant domain team shall maintain a living `Figma Menu Coverage Register` for each module.

Minimum fields:
1. Module / Domain
2. Menu Group / Parent Menu
3. Function / Menu Name
4. Screen / View Type
5. Functional Design Reference
6. Figma Reference / Frame Reference when available
7. Very Deep Research Round
8. Research Finding / Evidence Reference
9. Delta Type: CONFIRM / ADD / REDUCE / REFINE / REMOVE
10. Impact Class: NON-MATERIAL / MATERIAL
11. Gate / Assurance Status
12. Owner
13. Last Verified Date / Evidence Version
14. Open Gap / Next Research Target

## Menu Classification
The register should separate at least:
- Primary operational menus
- Transaction menus
- Master data menus
- Approval / control menus
- Reporting / analytics menus
- Configuration / setup menus
- Supporting actions that do not require a persistent standalone menu

Not every discovered function must become a new menu. SMEs Core + Figma must decide whether the function belongs as a menu, action, tab, smart button, inline control, configuration, report, or background behavior based on evidence and UX simplicity.

## Research-to-Figma Delta Flow
`PHASE SA + PHASE PRE-MATRIX TEST`
`-> GAP / UNKNOWN / RESEARCH TARGET REGISTER`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> if PASS: FIGMA + VERY DEEP RESEARCH N run in parallel`
`-> VDR FINDING`
`-> CLASSIFY CONFIRM / ADD / REDUCE / REFINE / REMOVE`
`-> UPDATE FIGMA MENU COVERAGE REGISTER`
`-> UPDATE ONLY AFFECTED FIGMA / FUNCTIONAL ARTIFACT`
`-> INDEPENDENT ASSURANCE`
`-> NEXT HANDOFF GATE`

## Multiple Verification Rounds
The process MUST support `VDR #2`, `VDR #3`, `VDR #4`, or later rounds when justified by material learning needs.

A new round is not a reset. Each round builds on prior verified evidence and must preserve lineage.

`NO REPEATED QUESTION WITHOUT MATERIAL DELTA.`

A later VDR round may:
- confirm the existing design;
- add a secondary function;
- refine or simplify a menu/screen;
- remove unnecessary UI;
- strengthen controls;
- uncover a Material Delta requiring Controlled Re-entry for affected scope only.

## Figma Stability Principle
Figma should not be treated as frozen after the first approved screen design. It is a controlled design baseline that may receive evidence-backed deltas.

At the same time, research must not create uncontrolled UX churn.

Therefore:
- Non-material findings -> controlled update only.
- Material findings -> affected-scope Controlled Re-entry and re-assurance.
- Unaffected menus/screens continue normally.
- No whole-module redesign unless evidence proves the whole-module baseline is invalid.

## Initial Coverage Queue
Initial high-priority modules for menu coverage alignment include:
1. Purchase
2. Inventory / Warehouse
3. Sales
4. Accounting
5. Expenses

Additional modules are added according to Functional Design readiness, Phase SA / Pre-Matrix findings, dependency order, and SMEs Core domain-team ownership. This list is a starting queue, not a frozen final module inventory.

## Assurance
Before a VDR-derived menu/screen delta is handed downstream, the applicable Phase Assurance controls remain mandatory:
- Entrance Contract
- Proof Obligations
- Evidence State
- Independent Challenge
- Controlled Re-entry where required
- Exit Contract
- Phase Handoff Gate

## Governing Principles
`CLEAR HANDOFF BEFORE NEXT PHASE.`
`NO DOWNSTREAM GUESSING.`
`NO PHASE HANDOFF WITHOUT INDEPENDENT ASSURANCE.`
`NO EVIDENCE = NO PROGRESS.`
`NEVER SKIP GATE.`

> Understand deeply. Prove objectively. Challenge independently. Recommend explicitly. Decide with traceability. Execute with control.

Boss remains the sole Final Approver.
