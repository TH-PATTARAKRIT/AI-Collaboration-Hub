# [SMEPLUS-26-09-06-G01-P03-M2C-BOUNDED-DEEP-CLOSURE-002]
# G01-P03 Manufacture-to-Cost — Bounded-Deep Closure, Recursive Challenger Convergence & Controlled Handoff / L99999.99999

## 1. PROJECT IDENTITY

Project: **SMEsPlus ENTERPRISE SUITE**
Parallel Group: **G01 — Supply / Cost / Payable**
Process: **P03 — Manufacture-to-Cost**
Execution Mode: **CONTINUE EXISTING OLD P03 SESSION**
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Working Branch: `research/account-p03-manufacture-to-cost-2026-09-04-001`
P03 Evidence Baseline Commit: `7fca09aedb99b58204ece63432bec0292a5df4ab`
Previous P03 Closure Prompt Commit: `c088f2f40cc1ee0e5881720192027991cd94eb80`
P01 Authoritative Closure Commit: `b820b29b13f351ec21c724c05ea9aa8da2a15e14`
Common Closure Execution Constitution v1 Commit: `48ee264fd74dcb0dee378789e56d028ad8bb6110`
Boss: **Sole Final Approver**

This prompt **supersedes the prior P03 closure prompt as execution control only**.
It does NOT erase, reset, replace or invalidate prior P03 evidence.
Preserve complete lineage.

## 2. MODEL / EFFORT — FIXED

Use exactly:
- **Model: Claude Opus 5**
- **Effort: HIGH**

One Prompt = One fixed Model/Effort execution envelope.
Do not change model or effort inside this run.

Reason: this is a bounded but deep Manufacture-to-Cost closure involving valuation integrity, RM/WIP/FG causality, purchase revaluation, subsidiary-vs-GL divergence, fixed overhead, equipment usage causality, deployed-code identity and cross-process accounting boundaries.

## 3. BOSS CLOSURE INTENT — CANONICAL

The required behavior is:

`Closure`
`-> Challenger finds a gap`
`-> deepen INSIDE the declared P03 closure scope`
`-> material delta`
`-> re-challenge corrected result`
`-> reconcile`
`-> repeat while genuine material in-scope delta exists`
`-> terminal disposition`
`-> STOP.`

The key rule is:

> **Closure may become deeper, but it may never become wider.**

A challenger is allowed to force another evidence pass when it finds a real material gap.
However, the new pass must stay inside the same declared Closure Question or a directly-derived subquestion required to answer it.

Do NOT convert a closure gap into a whole-estate sweep, another whole-domain Deep Research round, or research owned by another Pxx.

### Definition of "deep until we know everything"
For this prompt, completeness means **everything materially necessary to answer the declared P03 Closure Question Set** is known, contradicted, explicitly unavailable, routed to a named owner, or prepared for Boss decision.

It does NOT mean universal knowledge of every ERP module, every database, every backup, every version or every adjacent process.

## 4. COMMON EXECUTION CONSTITUTION — MANDATORY / EMBEDDED

No Evidence = No Progress.
Never Skip Gate.
Boss = Sole Final Approver.
Scope-aware Everywhere.
Old Session First.
No repeated work without Material Delta.
No Material Delta = No New Research Round.
Sufficient Evidence = Stop Searching.
Peer Position != Boss Decision.
UNRESOLVED != ADOPTED.
Recommendation != Canonical Boundary.
Independent Review != Truth.
No silent correction; preserve complete revision lineage.

Every material object, operation, access path, configuration, reference, report and mutation must determine applicable scope first:
- PLATFORM
- TENANT
- COMPANY

Do NOT blanket-enforce Tenant + Company on every operation.

### Closure-specific constitutional rule
A Closure Prompt may:
- remain at the same evidence/search scope; or
- narrow to a more precise causal/evidence path.

A Closure Prompt may NOT broaden beyond its declared domain, evidence population or cross-process interface merely because a challenger found a gap.

## 5. PRECONDITION — CONSUME P01 FINAL HANDOFF, DO NOT RESEARCH P01

Before substantive P03 closure work:
1. fetch/verify remote P01 authoritative closure commit `b820b29b13f351ec21c724c05ea9aa8da2a15e14`;
2. locate and consume the latest published P01->P03 handoff and relevant P01 evidence registers;
3. verify every P01 claim used by P03 against the published handoff/evidence, not memory or an older P01 prompt;
4. record the exact P01 handoff SHA/path consumed;
5. do NOT modify or reopen P01 from P03.

Important correction lineage to verify from final P01 evidence before use:
- earlier kit-specific interpretation of `purchase_mrp` was corrected; the relevant filter must be read as implemented, not from docstring wording;
- the `_get_stock_valuation_layers` chain was bounded by direct read and includes `stock_account`, `stock_landed_costs`, and `purchase_mrp` participants; the overrides found are narrowing filters;
- a third landed-cost participant must be considered where landed costs are actually exercised;
- the final P01 accounting disposition of purchase-price differences must be consumed from the latest handoff, because earlier intermediate wording about "capitalised into inventory / no P&L variance" was corrected before P01 closure.

Do not carry superseded P01 wording into P03.

## 6. P03 DECLARED CLOSURE SCOPE — FROZEN AGAINST BROADENING

P03 closure is limited to the Manufacture-to-Cost causal and accounting boundary:

`Purchase/Receipt Cost Truth`
`-> RM Valuation`
`-> Consumption`
`-> WIP`
`-> Semi/FG`
`-> Production Completion`
`-> Delivery/COGS interface`
`-> GL / Subsidiary Ledger / Management Cost reconciliation interface`

Allowed adjacent interfaces only where directly necessary:
- P01 purchase/revaluation input into manufacturing cost;
- P04/Asset equipment/depreciation input boundary;
- Inventory valuation input/output boundary;
- P08 financial reporting/reconciliation handoff;
- P11 accounting reconciliation handoff.

P03 may inspect those interfaces only enough to determine Manufacture-to-Cost causality and ownership.
P03 must NOT execute P01, P04, Inventory, P08 or P11 research programmes.

## 7. DECLARED P03 CLOSURE QUESTION SET

Create `P03_CLOSURE_QUESTION_REGISTER.md` with these IDs and terminal disposition for every one.

### CQ-P03-01 — P01 purchase/revaluation delta entering manufacturing
Determine exactly:
- what economic amount/event is produced by the final P01 mechanism;
- exact unit/predicate/denominator used;
- whether and how that amount changes RM valuation;
- whether the effect reaches manufacturing at all;
- whether prior counts/units differ and why.

Do not inherit intermediate P01 wording without verifying the final handoff.

### CQ-P03-02 — Stock valuation-layer filter chain
For the load-bearing `_get_stock_valuation_layers` path, determine:
- exact participant chain;
- exact predicates/filters;
- MRO/order effect;
- whether any dropped layer can be reintroduced later;
- the meaning of the already identified live dropped rows;
- landed-cost participation only where exercised;
- source identity and deployed identity for load-bearing implementations.

No whole-addon-tree sweep.
Only direct participant/dependency paths proven by code/evidence.

### CQ-P03-03 — RM -> WIP -> Semi/FG -> COGS propagation
Determine for every material cost delta entering RM:
- when it propagates;
- by which event/function/model;
- whether lineage is preserved explicitly or only embedded in changed unit cost;
- whether reversal/unbuild/return reverses the same economic effect;
- whether duplicate, zero or stranded cost can arise.

Trace business fact and accounting fact separately.

### CQ-P03-04 — P03R-F-01 subsidiary valuation vs GL divergence
Close the causal understanding of the known extreme valuation rows:
- origin event family;
- first divergence point;
- identity/provenance to receipt/bill revaluation and production events;
- why referenced GL entries are sane while subsidiary valuation rows are extreme;
- role of manufacturing as origin vs amplifier;
- cancellation/reversal/unbuild behavior;
- correction blast-radius risk;
- controls SMEsPlus would need to prevent/reconcile such divergence.

NO repair execution.
NO database write.

### CQ-P03-05 — Fixed-overhead injection boundary
For each current cost component in scope:
- depreciation;
- planned maintenance;
- repair where evidence exists;
- energy;
- indirect labour;

Determine:
- source mechanism present/absent;
- configured/exercised state;
- operational driver/event;
- target cost object;
- financial vs managerial boundary;
- whether lack of path is source gap, configuration gap, deployment gap, or design candidate.

Do not expand into a full maintenance, energy or HR domain review.

### CQ-P03-06 — Operation -> Equipment -> Cost causality
Within Manufacture-to-Cost only, determine:
- what Source proves for Operation -> Work Center;
- whether Source proves Operation -> Specific Equipment;
- whether Work Center membership can or cannot establish actual machine usage;
- exact evidence boundary for equipment usage cost entering MO/WIP/FG;
- integration boundary to Asset/Equipment research.

Carry Boss-approved policy inputs without converting them into benchmark facts:
- productive depreciation allocation -> WIP/FG;
- nonproductive depreciation -> named operational cause;
- no unclassified depreciation;
- continuous post-depreciation internal usage has no residual cap;
- financial depreciation != managerial/internal usage allocation;
- Work Center membership alone != cost absorption;
- off-balance tracking must not be cross-posted as financial WIP.

Do NOT redesign the Asset domain in P03.

### CQ-P03-07 — Work Center rate / valuation-policy reachability
Resolve current evidence that work-centre rates and real-time/perpetual valuation have not coexisted in examined deployments:
- denominator;
- exact deployed populations examined;
- whether this is genuine absence, configuration separation, evidence-population limitation or unreachable path;
- whether any P03 mechanism depends on their coexistence.

No new estate-wide database census.

### CQ-P03-08 — Scope ownership
For every material P03 object touched by this closure, determine applicable scope from evidence:
- PLATFORM / TENANT / COMPANY.

Pay particular attention to:
- work centers;
- manufacturing orders/operations;
- equipment references;
- valuation/accounting facts;
- shared/master configuration where relevant.

Do not infer Company scope merely because an accounting effect is Company-scoped.
Do not infer Tenant scope merely because a master object is shared.

### CQ-P03-09 — Cross-process ownership and handoff
Every material surviving finding must have an owner:
- P03-owned;
- P08-owned;
- P11-owned;
- P04/Asset-owned;
- Inventory-owned;
- Boss Decision Required.

P03 must publish exact handoffs and stop at ownership boundaries.

### CQ-P03-10 — Evidence integrity / terminality
Verify:
- no load-bearing negative relies on undeclared search boundaries;
- denominators and units are explicit;
- prior contradictions are preserved;
- all background tasks are completed/dispositioned;
- checkpoint and auto-resume are current;
- remote publication is verified.

## 8. BOUNDED DEEPENING PROTOCOL

For every CQ-P03-xx, use this loop:

### STEP A — Current evidence statement
State the current answer and evidence classification.

### STEP B — Direct causal proof
Trace only the minimum models/functions/events/data required to support or refute that answer.

### STEP C — Four AAS-03 challenges
Run four independent challenges against the current answer.

### STEP D — Material Delta Test
For each challenge result, classify:

- `A — IN-SCOPE DERIVED SUBQUESTION`
- `B — SAME-SCOPE MATERIAL CONTRADICTION`
- `C — CROSS-PROCESS / OUT-OF-SCOPE`
- `D — MUTATION / EXTERNAL / BOSS DECISION REQUIRED`
- `E — NON-MATERIAL / CORROBORATIVE ONLY`

### STEP E — Recursive deepening only for A/B
If A or B is material:
- create Material Delta ID;
- name affected Closure Question ID;
- state why previous evidence is insufficient;
- declare the exact bounded evidence surface;
- declare expected stop condition;
- deepen only there;
- correct/re-derive the answer;
- re-challenge the corrected answer.

Repeat while genuine A/B material delta exists.

For C/D/E:
- route/hold/disposition;
- do not broaden research.

There is NO arbitrary challenge-round limit while a real material in-scope delta continues to exist.
But there is also NO permission for an in-scope delta to become a whole-estate sweep.

## 9. SEARCH-SURFACE CLAMP — MANDATORY

Every material search must log BEFORE execution:
- Closure Question ID;
- purpose;
- exact module/model/function or DB population;
- path/root boundary;
- denominator unit;
- stop condition.

Allowed source expansion:
- modules already evidenced in P01/P03;
- direct imported/inherited/called dependencies proven by the load-bearing path;
- a newly named module only when evidence proves it participates directly in a declared CQ.

Adding a module does NOT authorise scanning the whole addons tree.

Forbidden by default:
- `find all` across the entire host;
- complete `/Volumes` walk;
- complete Google Drive / CloudStorage walk;
- backup/archive census unrelated to a CQ;
- all-version census without a CQ-specific denominator;
- full P01/P04/P08/P11 investigation.

If a broad population is genuinely required by a declared CQ, document why no narrower route can answer it before executing.

## 10. NEGATIVE-CLAIM / DENOMINATOR CONTROL

Every load-bearing negative must include:
- denominator population;
- selection unit;
- path/source set;
- version/generation boundary;
- positive control;
- failure control where applicable;
- blind spots;
- whether instruments are genuinely independent.

Rules:
- Empty result != absence.
- Same zero != same cause.
- Source present != installed.
- Installed != configured.
- Configured != exercised.
- Exercised != economically correct.
- Current-state census may not reveal historical/reverted facts.

## 11. P03R-F-01 SAFETY VETO

Because known valuation rows include extreme values and near-cancellation behavior:
- do not repair;
- do not write;
- do not post;
- do not restore into a writable environment;
- do not run a correction experiment without a separate bounded Boss authorisation.

Read-only reconstruction is permitted.

If write/runtime proof is necessary, create:
`P03_BOSS_RUNTIME_AUTHORISATION_PACK.md`
with:
- exact question;
- why read-only proof is insufficient;
- exact disposable environment;
- exact mutation;
- expected evidence;
- rollback/disposal method;
- explicit exclusions.

Then HOLD that CQ only.
Continue other CQs.

## 12. FOUR AAS-03 CHALLENGERS — REQUIRED FOR EVERY MATERIAL CORRECTED ANSWER

Use the four official perspectives:

1. **Leader Functional Design**
   Attack business-event causality, RM/WIP/FG propagation, reversal/unbuild semantics and cost completeness.

2. **Leadership Database Design**
   Attack identifiers, lineage, valuation/GL reconciliation, units, denominators, historical-state visibility and corruption propagation.

3. **Lead Integration & Localization**
   Attack P01->P03 handoff truth, accounting-period/tax/localisation interfaces, cross-process ownership and scope boundaries.

4. **Lead Code & UI Architect**
   Attack deployed-code identity, inheritance/MRO, input-modifying overrides, reachability, source gaps, operation/equipment implementation boundaries.

Each must report:
- SUPPORTED
- MISSING
- RISKY
- CHALLENGED
- EVIDENCE NEEDED NEXT

At least one must actively attempt to disprove:
- the current explanation of P03R-F-01;
- the current interpretation of the valuation-layer filter chain;
- the current fixed-overhead injection-gap conclusion.

Preserve dissent.
Do not force consensus.

## 13. BACKGROUND TASK GOVERNANCE

Every background task must record:
- Task ID;
- CQ ID;
- command/objective;
- path/population boundary;
- start time;
- load-bearing vs corroborative;
- stop condition.

If a stronger direct route settles the question, disposition redundant corroborative tasks.
Do not wait hours on a CloudStorage/global grep after the CQ is already settled.

If a task is suspiciously long-running or non-progressing, perform a non-destructive health check before action.

Terminal report requires:
`BACKGROUND TASKS = 0 RUNNING`
or every remaining task explicitly dispositioned before publication.

## 14. REQUIRED TERMINAL DISPOSITION — NO VAGUE OPEN ITEMS

Every CQ-P03-xx must end as exactly one of:
- `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`
- `CONTRADICTED — CORRECTED AND CLOSED FOR CURRENT EVIDENCE`
- `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`
- `BOSS DECISION REQUIRED — DECISION PACKAGE READY`
- `EXTERNAL / CROSS-PROCESS OWNER — HANDOFF PUBLISHED`
- `OUT OF SCOPE — ROUTED WITH EVIDENCE`

Do not leave `OPEN`, `TBD`, or `needs more research` without exact evidence/owner/action.

## 15. DELIVERABLES

Create/update as required by actual evidence:

Core closure control:
- `P03_CLOSURE_QUESTION_REGISTER.md`
- `P03_BOUNDED_DEEPENING_LOG.md`
- `P03_CHALLENGE_CONVERGENCE_REGISTER.md`
- `P03_MATERIAL_DELTA_REGISTER.md`

Causal/evidence:
- `P03_P01_FINAL_HANDOFF_INTAKE.md`
- `P03_PRICE_DIFFERENCE_TO_MFG_TRACE.md`
- `P03_STOCK_VALUATION_LAYER_FILTER_CHAIN.md`
- `P03_RM_WIP_FG_COGS_CAUSAL_TRACE.md`
- `P03_VALUATION_GL_DIVERGENCE_CLOSURE.md`
- `P03_FIXED_OVERHEAD_INJECTION_MATRIX.md`
- `P03_EQUIPMENT_OPERATION_COST_CAUSALITY.md`
- `P03_WORKCENTER_VALUATION_REACHABILITY.md`
- `P03_SCOPE_OWNERSHIP_MATRIX.md`
- `P03_DEPLOYED_CODE_IDENTITY_DELTA.md`

Governance/handoff:
- updated Contradiction Register
- updated Revision/Error Log
- updated Source Link Register
- updated Evidence Manifest
- `P03_TO_P08_HANDOFF.md`
- `P03_TO_P11_HANDOFF.md`
- Asset/Inventory handoff where actually required
- `P03_CHECKPOINT_REGISTER.md`
- `P03_AUTO_RESUME_STATE.md`

Preserve all prior files and wrong/superseded findings in lineage.

## 16. CHECKPOINTS + AUTO-RESUME

CP-01 — baseline / P01 authoritative handoff / previous prompt supersession verified
CP-02 — Closure Question Register frozen
CP-03 — CQ01/CQ02 purchase + valuation-filter closure
CP-04 — CQ03 RM->WIP->FG->COGS closure
CP-05 — CQ04 P03R-F-01 bounded-deep closure
CP-06 — CQ05/CQ06 fixed overhead + equipment causality closure
CP-07 — CQ07/CQ08 reachability + scope closure
CP-08 — recursive challenger convergence complete for all material CQs
CP-09 — CQ09 cross-process handoffs published
CP-10 — CQ10 evidence integrity / background terminality / remote publication complete

Auto-continue through executable checkpoints.
Do not ask Boss for routine intermediate approval.
Do not wait idle on external dependencies.

AUTO_RESUME_STATE must record:
- current CQ;
- current Material Delta ID if any;
- exact bounded next action;
- exact blocker/owner;
- whether Boss action is required.

## 17. AAS+ / PMO CLOSURE GATE

After all CQs reach terminal disposition:

AAS+ must consolidate:
- agreements;
- dissents;
- contradictions corrected;
- unresolved named evidence;
- handoff ownership;
- any finding that changed severity/status during recursion.

PMO must answer:
1. Is the declared P03 Closure Question Set exhausted to maximum currently obtainable evidence?
2. Did any closure step broaden scope improperly?
3. Is every remaining dependency named and routed?
4. Is P03 ready to stop and hand off within G01?
5. Are any write/runtime authorisations still required?
6. Are all background tasks terminal/dispositioned?

Do not reward work volume with gate progress.
Downgrade if evidence quality deteriorates.

## 18. TERMINAL STATES — ONLY THESE

A. `G01-P03 BOUNDED-DEEP CLOSURE COMPLETE — READY FOR CONTROLLED HANDOFF — OPEN HOLDS NAMED`

B. `G01-P03 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`

C. `G01-P03 EVIDENCE INTEGRITY FAILURE — CORRECTION REQUIRED`

No PASS.
No Final Freeze.
No merge.
No implementation authorisation.

## 19. TERMINALITY AUDIT

Before terminal report verify all:
- every CQ-P03-01..10 has exactly one terminal disposition;
- every material derived subquestion has terminal disposition;
- all material challenger deltas are reconciled or named holds;
- no out-of-scope research was silently absorbed;
- all handoffs are published;
- background tasks = 0 running, or properly dispositioned before final publication;
- checkpoint current;
- AUTO_RESUME_STATE current;
- commit pushed;
- remote HEAD == intended final commit;
- no database/environment mutation occurred unless separately Boss-authorised;
- P01/P04/P08/P11/Inventory were not executed from P03;
- no merge to `SMEsPlus`.

## 20. FINAL REPORT

Report concisely but completely:
- Branch
- Final commit SHA
- Direct GitHub link
- P01 authoritative handoff SHA/path consumed
- Closure Constitution commit consumed
- CQ-P03-01..10 terminal disposition table
- material challenger corrections
- P03R-F-01 final disposition
- valuation-layer filter-chain final disposition
- RM/WIP/FG/COGS propagation disposition
- fixed-overhead/equipment causality disposition
- exact open holds + owners
- P08/P11/Asset/Inventory handoff status
- PMO recommendation
- background task count
- mutation status
- exact reason closure stopped

## 21. STOP RULE

When the declared Closure Question Set and all material in-scope derived subquestions are terminally dispositioned:

`COMMIT`
`-> PUSH`
`-> VERIFY REMOTE`
`-> UPDATE CHECKPOINT`
`-> UPDATE AUTO_RESUME_STATE`
`-> PRODUCE TERMINAL REPORT`
`-> STOP.`

Do not continue merely because more information might exist elsewhere.
Do not start P05/P04 automatically.
Do not start P08/P11.
Do not reopen P01.
Do not merge.

# BEGIN NOW

Continue the existing OLD P03 session.
Apply this prompt as the controlling closure instruction.
Deepen until the declared P03 closure questions are truly understood and terminally dispositioned.
Never broaden the closure scope.
