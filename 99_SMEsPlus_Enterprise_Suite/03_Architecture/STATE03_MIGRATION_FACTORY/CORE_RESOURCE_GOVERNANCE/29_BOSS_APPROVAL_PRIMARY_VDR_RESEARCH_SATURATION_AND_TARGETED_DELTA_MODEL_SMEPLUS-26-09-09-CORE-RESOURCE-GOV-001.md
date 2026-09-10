# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# BOSS APPROVAL — Primary Very Deep Research, Research Saturation & Targeted Delta Model

## Decision Status
BOSS APPROVED — EFFECTIVE IMMEDIATELY

## Boss Approval
Boss approves the SMEs Core recommendation to reduce repeated full-scope Very Deep Research by making the first bounded-subject research cycle substantially deeper, multi-layered, independently challenged, and explicitly completeness-tested before the subject proceeds downstream.

Boss rationale: the more rigorously SMEsPlus challenges the subject, the more gaps are likely to be found earlier, and the earlier those gaps are found the faster they can be corrected before they become downstream ambiguity or rework. Multiple assurance layers are therefore desirable when each layer has a distinct proof purpose and does not merely repeat the same question.

## Canonical Research Strategy

`ONE PRIMARY DEEP BASELINE — MANY TARGETED DELTAS, NOT MANY FULL RESTARTS.`

For every bounded subject / menu / master-data area / function group:

`RESEARCH CONTRACT`
`-> PRIMARY VERY DEEP RESEARCH`
`-> INTERNAL MULTI-PASS RESEARCH`
`-> COMPLETENESS MATRIX`
`-> SPECIALIST REVIEW`
`-> INDEPENDENT ADVERSARIAL CHALLENGE`
`-> CORRECTION / TARGETED RESEARCH IF REQUIRED`
`-> RESEARCH SUFFICIENCY / SATURATION GATE`
`-> PHASE S`
`-> PHASE SA`
`-> PHASE PRE-MATRIX TEST`
`-> TARGETED DELTA VDR ONLY WHERE A GAP IS PROVEN`
`-> PHASE HANDOFF GATE`
`-> FUNCTIONAL DESIGN`
`-> FUNCTIONAL DESIGN GATE`
`-> FIGMA / UX DESIGN`

This strengthens and does not replace the previously approved Menu-by-Menu VDR-to-Figma pipeline.

## 1. Research Contract — Mandatory Before Primary VDR
Before Claude Fible or another approved research agent begins Primary VDR, SMEs Core / the responsible Domain Team MUST define a Research Contract for the bounded subject.

The Research Contract must define at minimum:
- bounded subject / menu / master-data area;
- business purpose and lifecycle;
- known upstream / downstream dependencies;
- required evidence sources and evidence quality expectations;
- proof obligations;
- coverage domains to be investigated;
- known assumptions and unknowns;
- required cross-module / cross-domain checks;
- expected UX / Figma implications;
- explicit out-of-scope items;
- completion / saturation criteria;
- independent challenge requirements.

A prompt that merely asks an AI to “research as deeply as possible” is not sufficient governance.

## 2. Primary VDR — Full-Scope Bounded Subject Research
Primary VDR is the principal deep-study cycle for a new bounded subject before that subject enters Phase S.

It must attempt to understand the subject from normal business behavior down to detailed rules, controls, failure modes, and UI implications.

Coverage should include, as applicable:
- business purpose and lifecycle;
- menu / screen / action / workflow behavior;
- fields, defaults, mandatory rules and validation;
- roles, permissions, approval and segregation of duties;
- identity, data ownership, duplication and merge rules;
- active / inactive / archive / delete behavior;
- tax, accounting and financial impacts;
- cross-module handoffs;
- tenant / organization root / company / branch implications;
- SaaS and multi-company behavior;
- configuration vs transaction behavior;
- documents, attachment, communication and evidence;
- import / export / API / integration behavior;
- migration and historical-data behavior;
- reporting, search, filter and audit trail;
- exception, reversal, concurrency and failure behavior;
- security / privacy / sensitive-data implications;
- reconciliation and end-to-end proof;
- UX / Figma implications;
- what must never happen;
- remaining unknowns.

## 3. Internal Multi-Pass Research Within One Primary VDR
Primary VDR may contain many internal passes while remaining one governed research cycle.

Recommended internal passes include:

`PASS A — Normal Process / Happy Path`
`PASS B — Data / State / Validation`
`PASS C — Roles / Controls / Audit`
`PASS D — Cross-Module / Cross-Domain Relationships`
`PASS E — Exception / Failure / Reversal / Concurrency`
`PASS F — SaaS / Tenant / Multi-Company / Company Context`
`PASS G — Migration / Historical / Reconciliation`
`PASS H — UX / Menu / Field / Interaction Implications`
`PASS I — Adversarial Missing-Scenario Attack`
`PASS J — Contradiction / Evidence Reconciliation`

Additional passes may be added when the bounded subject requires specialist depth.

The purpose is to create layered inspection without falsely treating repeated full research rounds as progress.

## 4. Completeness Matrix — Mandatory
Before Primary VDR can exit, a Completeness Matrix must state the coverage status of every material research domain.

Allowed states should clearly distinguish, as applicable:
- VERIFIED
- PARTIALLY VERIFIED
- OPEN
- CONTRADICTION
- INSUFFICIENT EVIDENCE
- OUT OF SCOPE
- DEFERRED WITH OWNER / TRIGGER

Unknowns may not be silently omitted.

## 5. Independent Adversarial Challenge
The research-producing agent/team may not be the sole authority declaring the research sufficiently complete.

Independent Challenge must actively attempt to find:
- missing scenarios;
- contradiction between evidence sources;
- hidden assumptions;
- unhandled cross-module effects;
- missing controls;
- data-integrity risks;
- legal / accounting / tax risks where applicable;
- tenant / company boundary errors;
- UX implications not surfaced by the research;
- cases in which the proposed behavior would fail, be ambiguous, or become irreversible.

Challenge should ask: `If this research or design is wrong, where is it most likely to be wrong?`

## 6. Research Sufficiency / Saturation Gate
Primary VDR does not need to prove that future learning is impossible. It must prove that the bounded subject is sufficiently understood for the next phase and that residual unknowns are explicit, owned, and non-blocking or correctly held.

The Gate may dispose as:
- PASS
- CONDITIONAL PASS
- HOLD
- TARGETED RESEARCH REQUIRED

No PASS merely because the prompt finished or the document became large.

## 7. Three Research Modes
Canonical terminology:

### PRIMARY VDR
Full-scope deep study of a new bounded subject before Phase S.

### TARGETED DELTA VDR
Narrow additional research triggered by a proven Gap, contradiction, unknown, new requirement, new evidence, or downstream challenge.

It MUST reference the triggering finding and affected scope.

### RE-VALIDATION VDR
Broader revalidation only when material new evidence shows that the prior research baseline may no longer be reliable across a wider scope.

Re-validation is not the default and requires a material-delta reason.

## 8. Relationship to Phase S / SA / Pre-Matrix

`PRIMARY VDR`
= learn the bounded subject as deeply and practically as possible.

`PHASE S`
= structure and normalize the research evidence into controlled semantic knowledge.

`PHASE SA`
= synthesize architecture / functional meaning, ownership, boundaries, controls, dependencies and unresolved questions.

`PHASE PRE-MATRIX TEST`
= attempt to falsify completeness, expose contradiction, identify missing knowledge, and challenge downstream readiness.

If Phase SA or Pre-Matrix finds a Gap, the default is:

`FINDING -> TARGETED DELTA VDR -> CORRECTION -> FRESH CHALLENGE -> RETURN TO AFFECTED GATE`

not a full-scope VDR restart.

## 9. Relationship to Figma Menu Coverage
Each research subject must remain traceable into Functional Design and Figma.

Where practical, the chain should be:

`RESEARCH SUBJECT ID`
`-> COVERAGE ITEM`
`-> EVIDENCE / FINDING`
`-> PHASE S / SA / PRE-MATRIX REFERENCES`
`-> FUNCTIONAL DESIGN REFERENCE`
`-> FIGMA FRAME / SCREEN REFERENCE`

Later Targeted Delta VDR must identify exactly which Functional Design / Figma artifact is affected.

`NO SILENT MENU OR SCREEN CHANGE.`

## 10. Anti-Loop / Anti-Waste Controls
Multiple layers are approved, but repeated work without a distinct purpose is not.

Mandatory controls:
- `No repeated question without material delta.`
- each layer must state its distinct objective / proof obligation;
- existing verified evidence must be reused and preserved;
- new research must identify what is genuinely new or unresolved;
- no reset of prior verified work without material evidence;
- no arbitrary VDR #2/#3/#4 full rerun merely because a previous round exists;
- evidence lineage must remain intact;
- unresolved items must carry owner, status, trigger and impact.

## Canonical Principles

`DO THE BROADEST THINKING BEFORE THE DEEPEST RESEARCH.`

`DO THE DEEPEST PRIMARY RESEARCH ONCE.`

`CHALLENGE IT HARD.`

`RESEARCH AGAIN ONLY WHERE EVIDENCE PROVES A GAP.`

`ONE PRIMARY DEEP BASELINE — MANY TARGETED DELTAS, NOT MANY FULL RESTARTS.`

`RESEARCH UNTIL THE NEXT TEAM NO LONGER NEEDS TO GUESS.`

`NO EVIDENCE = NO PROGRESS.`

`NEVER SKIP GATE.`

`CLEAR HANDOFF BEFORE NEXT PHASE.`

`NO PHASE HANDOFF WITHOUT INDEPENDENT ASSURANCE.`

## Governance Boundary
This approval strengthens research governance and downstream assurance. It does NOT authorize source-code implementation, merge, deployment, production, or any mechanism not separately approved through its required Gate.

Boss remains the sole Final Approver.
