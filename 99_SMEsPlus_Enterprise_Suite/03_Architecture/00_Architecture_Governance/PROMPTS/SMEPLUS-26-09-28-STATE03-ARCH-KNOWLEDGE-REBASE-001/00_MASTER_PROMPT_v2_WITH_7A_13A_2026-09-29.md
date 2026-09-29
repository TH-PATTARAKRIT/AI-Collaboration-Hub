# MASTER PROMPT — Claude Code
## SMEsPlus ENTERPRISE SUITE / STATE 03 Deep Study Execution

**Session:** `SMEPLUS-26-09-28-STATE03-ARCH-KNOWLEDGE-REBASE-001`  
**Execution model:** Claude Code, Sonnet 5, high reasoning  
**Authority:** Research and controlled documentation only. Boss remains the sole final approver.

---

## 1. Mission

Execute the complete **STATE 03 — Architecture & Knowledge Acquisition** rebase and Deep Study method for SMEsPlus Enterprise Suite.

Your work is to study the Odoo Community reference deeply enough to produce trustworthy, clean-room-neutral knowledge for future STATE 04 consideration. Do **not** reset prior valid work without Material Delta. Re-audit and carry forward evidence when it meets this prompt's evidence standard.

STATE 03 is not Functional Design, SaaS target design, UX/UI, Figma, coding, CI/CD, deployment, production validation, or a question/percentage factory.

## 2. Non-negotiable boundaries

1. Reference scope is Odoo Community. Treat Enterprise, proprietary, custom and third-party behavior as separately classified reference conditions; never silently treat them as Community baseline.
2. Study reference behavior, source, configuration, data and runtime only in authorized research environments.
3. Never modify production, shared data, reference source, installed modules, database configuration, or records outside a disposable/isolated test environment.
4. Never implement or design SMEsPlus target schema, workflow, UI, API, ORM, code, event bus or SaaS architecture.
5. Do not copy or transmit vendor code, source identifiers, model/table/field/method names, SQL, physical ERD, UI, XML/view definitions, workflow implementation, or formula expressions into clean outputs.
6. Never claim whole-module completion from source reading, a demo walkthrough, one trace, question count, coverage %, or a happy path.
7. No Evidence = No Progress. Unknown is valid; unsupported certainty is not.

## 3. The State 03 knowledge objective

For each applicable module and function, discover and reconcile:

- business purpose, actor, trigger, outcome and lifecycle;
- state transition, rule, validation, exception, cancellation and reversal;
- Core / Optional / Conditional reference classification and configuration impact;
- business objects, relationships, ownership and data lifecycle;
- effective source/workflow behavior, override/extension, automation and dependency;
- cross-module handoff, inventory/financial/control/event/integration implication;
- company/data scope, authority, audit and security semantics;
- evidence confidence, contradiction and unknowns.

The allowed output language is: **WHAT, WHY, BUSINESS RULE, STATE, DATA CONCEPT, CONTROL, DEPENDENCY, EVENT, RISK, UNKNOWN.**

## 4. Eight mandatory Deep Study controls

Apply all eight controls. They are one operating method, not separate frameworks.

1. **Module Function Universe** — versioned inventory of capability, function, configuration variant, handoff and scope status.
2. **Three-Track Reconciliation** — reconcile Business/Process, Effective Reference Behavior, and Data/Control impact for each function.
3. **Criticality Matrix** — C1/C2/C3/C4 classification with an evidence-based reason.
4. **Environment Fingerprint / Configuration Profile** — reproducible context for each critical trace.
5. **Trace-to-Decision-Point** — trace to authorization, validation, transition, handoff and side-effect decision points; never line-by-line framework noise by default.
6. **Control Applicability Matrix** — financial, inventory, authority, period/reversal, company/data scope, audit/event, automation/integration: Applicable / Not Applicable / Unknown with evidence.
7. **Risk-based Negative / Reversal Validation** — proportional, safe, resettable validation of material failure paths.
8. **Abstract & Sanitize Gate** — restrict technical evidence and produce a neutral clean-room pack.

## 5. Verification target and exception policy

Use Verification Accuracy (V) without averaging:

- **Function target:** V4. Documented exception floor: V3.
- **C1/Critical target:** V5. Documented exception floor: V4.

If below target, record: required target, actual level, available/missing evidence, cause, risk/design impact, status (`Non-blocking`, `Targeted Validation Needed`, or `Blocking Unknown`), owner and next action.

Below V3 for a Function, or below V4 for C1, is `Blocking Unknown` unless Boss explicitly authorizes an exception.

## 6. Deep Study procedure per Function

1. Define Function ID, neutral name, purpose, scope and C1–C4 criticality.
2. Freeze the applicable reference context: release/build, module/extension matrix, configuration, company, role, locale/timezone/currency, fixture and reset procedure.
3. Perform Business Trace: actor, trigger, preconditions, state/lifecycle, rule, exception and outcome.
4. Discover effective behavior: configuration, extensions/overrides, automation/scheduled activity and technical decision points.
5. Capture neutral domain/data semantics: object, ownership, relationship, lifecycle and business impact.
6. Capture applicable SaaS/control semantics: company/data scope, authority, approval/execute/post/reverse distinction, audit/event and integration behavior.
7. Trace cross-module handoffs and applicable inventory, financial, reconciliation or control effects.
8. Run targeted runtime/white-box validation proportionate to criticality. C1 requires Full AWT; C2 requires targeted AWT when risk warrants it.
9. Test material negative/reversal cases safely. Use isolated fixtures only.
10. Reconcile all tracks. Never infer away a contradiction.
11. Separate restricted evidence from neutral knowledge; run the 03.7 sanitizer review.
12. Update actual V, unknowns, evidence pointers and readiness status.

## 7. AWT constraints

For C1/C2, use Atomic White-box Trace only to establish material facts. Capture:

- UI/business observation, effective configuration and actor context;
- decision points for authorization, validation, state transition and handoff;
- targeted before/after business-data impact, not raw SQL noise;
- applicable financial/inventory/control/event impact;
- applicable automation, scheduled action, integration, retry/failure behavior;
- at least one material negative, reversal or integrity scenario for C1 and applicable C2.

Do not require breakpointing every line. Do not enable unrestricted SQL statement logging by default. Prefer targeted before/after snapshots and controlled request-level tracing. Use full database logging only if essential, time-boxed, masked and disposable.

## 7A. Mandatory Source Code Study

Source code study is mandatory in STATE 03 wherever source is authorized and available. Its purpose is **Function Discovery and effective-behavior verification**, never implementation reuse.

For every C1/C2 Function and every C3/C4 Function where source is needed to resolve a material doubt, study and index:

1. module manifest, declared dependency and feature/configuration entry points;
2. model/service/action that receives the business trigger;
3. decision-point logic for authorization, validation, state transition, cross-module handoff and material side effect;
4. effective extension/override/inheritance chain from installed modules, rather than the base addon alone;
5. compute/onchange/constraint behavior that materially changes the business outcome;
6. scheduled action, automation, procurement/rule engine, integration or notification behavior that can occur after the user action;
7. security and company/context conditions that materially change permitted behavior.

Create a **Restricted Source Study Index** containing source evidence pointers, effective-extension map, configuration dependency, observed behavior and unresolved contradiction. Do not copy source bodies or source-like pseudocode. If source is unavailable, inaccessible or not demonstrably applicable to the running reference, record `Black-box / Unavailable`; use controlled behavior/configuration evidence where possible and apply the V exception policy.

## 8. Pilot: Golden Trace Template

Execute first as the controlled pilot:

`Goods Receipt Validation — Movement, Valuation, and Financial-Control Effects`

Before beginning, create a Pilot Configuration Profile containing:

- release/build and installed/extension module matrix;
- company, role, test fixture and reset procedure;
- costing method, inventory valuation, relevant accounting/journal/category configuration and automation;
- in-scope/excluded variants, including price variance and landed-cost treatment.

For the Pilot, select applicable negative scenarios from: partial quantity/backorder/reservation, accounting/category prerequisite gap, UoM/currency/cost/rounding mismatch, role/company scope denial, cancellation/reversal after partial execution.

Do not assume a particular behavior. Record observed reference facts and conditions only.

## 9. GMVQ challenge use

Use GMVQ only as a **Challenge Question Source**:

`GMVQ question → function/control hypothesis → trace/validate → Confirmed / Contradicted / Conditional / Unknown`

Do not set a number of GMVQ questions, create a denominator, or claim percentage coverage. Continue only while a question reveals a Material Doubt. A Material Doubt ends when it is validated to target V, evidenced as Not Applicable, or registered transparently as an Unknown.

## 10. Clean Room execution

Maintain two strictly separate artifact types:

1. **Restricted Reference Evidence Annex** — technical/source traces, identifiers, SQL/data delta, screenshots, source pointers and configuration detail. Research-only access.
2. **Neutral Function Knowledge Pack** — business purpose/rule/state/exception, neutral data and control semantics, dependency/event implication, evidence ID and unknowns. The only artifact eligible for STATE 04 consideration.

Perform term replacement and structural-neutrality review. A neutral pack must not contain Odoo identifiers, source-like logic, physical design, copied UI or implementation expression. The sanitizer reviewer must not be the original technical-trace author for that item.

## 11. Required documentation outputs

Locate existing controlled STATE 03 document conventions first. Do not invent or rename canonical State/Step names. Place new artifacts only under the existing controlled STATE 03 structure; if no safe canonical location is discoverable, report the blocker and propose the exact path rather than guessing.

Create or update, as applicable:

1. STATE03 Deep Study Register — module/function universe, criticality, actual/target V, status and owner.
2. Function Knowledge Records — one record per applicable Function.
3. Configuration and Environment Fingerprints — for C1/C2 traces.
4. AWT Packs — only for functions requiring AWT.
5. Control Applicability Matrix.
6. GMVQ Challenge Log — selected questions, outcome and evidence pointer.
7. Restricted Reference Evidence Annex index.
8. Clean-Room Neutral Function Knowledge Packs.
9. Unknown / Contradiction / Targeted Validation Register.
10. Pilot Completion Report — evidence, findings, method defects, reusable Golden Trace Template and recommendation for controlled expansion.

## 12. Required execution order

### Phase A — Discover and preserve

1. Inspect repository/controlled documents and identify existing STATE 03 artifacts, evidence pointers, module inventories and prior valid work.
2. Produce a carry-forward/re-audit matrix. Mark each artifact `Reusable`, `Needs Reconciliation`, `Insufficient for V Target`, or `Unavailable`.
3. Establish the Module Function Universe and Criticality Matrix without claiming a frozen formal denominator.

### Phase B — Pilot and independent challenge

4. Prepare the Pilot Configuration Profile and run the Goods Receipt Pilot.
5. Use selected GMVQ questions to challenge every material pilot claim.
6. Produce restricted evidence and an independently sanitized Neutral Pilot Knowledge Pack.
7. Report whether the method is fit for expansion; list every method defect and blocker.

### Phase C — Controlled expansion

8. Expand module-by-module, starting with C1/C2 functions and applying proportional depth to C3/C4.
9. Update actual V and Unknown status per Function. Never replace an actual level with an average or a percentage.
10. Produce controlled STATE 03 handoff candidates only when the relevant neutral pack meets target or documented exception policy.

## 13. Completion and reporting rules

- Report factual progress at every material checkpoint: files/path, evidence ID, actual V, unknowns and blockers.
- Do not report `DONE`, `100%`, `FDS-ready`, or STATE transition approval without the required evidence and Boss approval.
- A function may be `Design-Ready Candidate`, `Ready with Decision`, `Targeted Validation Needed`, or `Blocking Unknown`; do not open STATE 04 or make its decisions.
- When access to source, database or runtime is unavailable, record `Black-box / Unavailable` with impact; do not fabricate evidence or bypass access controls.
- Stop and report if work would require production changes, destructive actions outside a disposable environment, authority escalation, target design, code changes or Clean-Room boundary breach.

## 13A. Next-Phase Gate

Do not start STATE 04 or any subsequent phase automatically.

STATE 03 may be proposed for Boss review only when:

1. every applicable module/function has an actual V level, target and exception status recorded;
2. C1 functions meet V5 or an explicitly documented V4 exception with Control Review;
3. every remaining Unknown is classified with material impact, owner and next action; no design-blocking unknown is hidden;
4. required source studies, configuration profiles, proportional AWT and control checks are complete or transparently exceptioned;
5. every candidate handoff has passed 03.7 Abstract & Sanitize; and
6. the consolidated STATE 03 Closure / Handoff Recommendation is complete for Boss decision.

Only after Boss approval may the project proceed to the Next Phase. Until then, continue only STATE 03 targeted validation and controlled documentation.

## 14. First response required from Claude Code

Before substantive execution, return only:

1. discovered repository root and existing controlled STATE 03 locations;
2. available source/runtime/database evidence and access constraints;
3. carry-forward candidates and material gaps;
4. exact proposed controlled artifact paths;
5. Pilot feasibility and any blocking authorization/environment requirement.

Then proceed autonomously through Phase A and Phase B only when the required research environment and controlled artifact path are available. Do not start Phase C expansion until the Pilot Completion Report is produced and reviewed.
