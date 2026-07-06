# SMEsPlus State-Based AI Execution Control Framework

Status: Active Control Standard  
Owner: PMO / Architecture Governance / AI Governance  
Applies To: All SMEsPlus project states  
Rule: No Evidence = No Progress

## Purpose

This framework defines how AI agents, Claude, ChatGPT, Copilot, automation agents, reviewers, and implementation teams must operate in each project state.

AI must not execute open-ended work. Every state must define input, allowed AI scope, prohibited actions, review criteria, required output, evidence path, owner, reviewer, gate result, and handoff rule.

## Core Rule

```text
AI cannot start without State Criteria.
AI cannot claim progress without evidence.
AI cannot move work to the next state without gate approval.
AI cannot override PMO, Architecture, QA, Security, or Boss approval.
```

## Folder Contents

```text
STATE_AI_EXECUTION_STANDARD.md
STATE_GATE_MATRIX.md
STATE_INPUT_OUTPUT_RULE.md
STATE_EVIDENCE_RULE.md
STATE_HANDOFF_RULE.md
STATE_PROMPT_GUARDRAIL.md
templates/
```

## Required State Control Files

Every state must maintain the following control set:

```text
STATE_XX_INPUT_PACKAGE.md
STATE_XX_AI_EXECUTION_CRITERIA.md
STATE_XX_GATE_CHECKLIST.md
STATE_XX_EVIDENCE_REGISTER.md
STATE_XX_HANDOFF_REPORT.md
```

## Gate Status

```text
PASS  = evidence complete, reviewed, and approved
HOLD  = evidence exists but incomplete, not reviewed, or pending approval
FAIL  = evidence missing, incorrect, inaccessible, or contradicts the claim
FROZEN = critical governance, legal, security, production, or traceability breach
```

## Current Enforcement

This framework is mandatory before AI execution in any state, including Functional Design, UX/UI Design, Development, Testing, Infrastructure, Production Operations, Knowledge Base, and Current Execution Context.
