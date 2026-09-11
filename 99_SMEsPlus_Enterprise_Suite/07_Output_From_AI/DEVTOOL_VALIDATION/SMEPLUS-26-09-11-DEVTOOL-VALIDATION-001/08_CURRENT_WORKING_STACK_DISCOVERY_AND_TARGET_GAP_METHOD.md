# [SMEPLUS-26-09-11-DEVTOOL-VALIDATION-001]
## Current Working Stack Discovery & Target-Gap Method

Status: ACTIVE METHOD CORRECTION
Owner: SSA
Co-Owner: PSPA
Final Approver: Boss

## Boss Direction
Do not select the most powerful tool in isolation. First understand the actual SMEsPlus project road, workflow and constraints. A high-end tool that does not fit the operating environment has no selection value.

## Selection Order
1. Inventory what SMEsPlus already uses.
2. Map the actual Prompt-to-Execution workflow.
3. Classify each current component by verified operating status.
4. Identify pain points, manual work, latency, reliability, governance and evidence gaps.
5. Define target capability for each gap.
6. Search only for tools that close a material target gap.
7. Challenge incumbent vs supplement/replacement on the same mission.
8. Prefer supplement over replacement when the existing tool is fit-for-purpose and replacement benefit is not material.
9. Freeze only after runtime evidence and Boss Final Gate.

## Current Workflow Hypothesis To Verify
Business / VDR / Architecture Input
-> Controlled Prompt
-> Jira / Work Package
-> Make or other Automation / Orchestrator
-> AI Engineering Tool
-> GitHub Branch / PR
-> CI / Test
-> Runtime / Playwright Evidence
-> Independent Review
-> Gate / Boss Decision

This is a hypothesis until each edge is verified with current evidence.

## Required Classification Per Component
- VERIFIED WORKING
- WORKING WITH LIMITATIONS
- DOCUMENTED / NOT RUNTIME VERIFIED
- PARTIAL
- BLOCKED
- NOT IN USE

## Mission Families
A. Prompt Intake & Routing
B. Work Orchestration / Automation
C. Backend Engineering
D. Frontend Engineering
E. Source / PR / CI Control
F. Test & Runtime Evidence
G. Security / Compliance
H. Observability / Operations
I. PMO / Traceability

## Core Decision Rule
Unused Feature = 0 Selection Value.
Fit-for-purpose current capability is preserved unless a challenger proves material improvement in the actual SMEsPlus mission.

## Replacement Rule
Do not replace a working component because another tool is more powerful.
Replace only when evidence shows a material gain in at least one required outcome without unacceptable regression in governance, cost, integration or operational complexity.

## Supplement Rule
A new tool is admissible only if it closes a material capability gap that cannot be solved adequately by the current stack with lower total complexity.

## Governance
No Evidence = No Progress.
Current Tool != Automatic Winner.
New Tool != Automatic Improvement.
Feature Count != Value.
Mission Fit + Constraint Fit + Evidence = Selection Basis.
Boss remains sole Final Approver.
