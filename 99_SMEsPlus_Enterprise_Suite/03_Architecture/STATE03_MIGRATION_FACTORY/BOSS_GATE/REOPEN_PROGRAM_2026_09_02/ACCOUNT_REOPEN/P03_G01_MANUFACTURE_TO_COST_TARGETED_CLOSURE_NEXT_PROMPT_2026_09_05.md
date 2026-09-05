# [SMEPLUS-26-09-05-G01-P03-M2C-TARGETED-CLOSURE-001]
# G01-P03 Manufacture-to-Cost — P01 Delta Intake, Valuation Integrity, Equipment Cost Causality & Targeted Closure / L99999.99999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Parallel Group: **G01 — Supply / Cost / Payable**
Process: **P03 — Manufacture-to-Cost**
Execution Mode: **CONTINUE EXISTING OLD P03 SESSION**
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Working Branch: `research/account-p03-manufacture-to-cost-2026-09-04-001`
P03 Baseline Commit: `7fca09aedb99b58204ece63432bec0292a5df4ab`
P01 authoritative branch: `research/account-p01-procure-to-pay-2026-09-04-001`
P01 minimum evidence baseline: `a02ec8b6628daf145c03fa49397448a7f29605ea`
P01 closure-control prompt commit: `fb4259ce9906023402645158a2ab6c48814acf90`
Boss: **Sole Final Approver**

## 2. MODEL / EFFORT — FIXED FOR THIS EXECUTION ENVELOPE

Use exactly:
- **Model: Claude Opus 5**
- **Effort: HIGH**

One Prompt = One fixed Model/Effort execution envelope.
Do not change model or effort inside this run.

Reason: this is a bounded but high-risk Manufacture-to-Cost reconciliation involving purchase-price differences, RM/WIP/FG valuation, subsidiary-vs-GL divergence, kit/phantom behavior, equipment cost causality, fixed-overhead attribution and cross-process accounting ownership.

## 3. PRECONDITION — G01 ORDER

G01 is sequential inside the lane while G02 may run in parallel.

Before substantive P03 work:
1. fetch/resolve the current remote HEAD of the P01 branch;
2. verify whether the controlled P01 closure produced a published `P01_TO_P03_HANDOFF.md` or equivalent explicit P01->P03 handoff;
3. consume the latest published P01 handoff if present;
4. if the handoff is absent, do NOT wait idle and do NOT invent it. Record `P01 HANDOFF NOT YET PUBLISHED`, preserve the minimum delta from `a02ec8...`, and stop before claiming G01-P03 closure unless all P01-dependent questions can be proven independently.

Do not modify P01 from P03.

## 4. COMMON EXECUTION CONSTITUTION — MANDATORY

No Evidence = No Progress.
Never Skip Gate.
Boss = Sole Final Approver.
Scope-aware Everywhere.
Old Session First.
No repeated work without Material Delta.
Peer Position != Boss Decision.
UNRESOLVED != ADOPTED.
Recommendation != Canonical Boundary.
Independent Review != Truth.
No silent correction; preserve all revision lineage.

Every material object/operation must determine applicable scope first:
- PLATFORM
- TENANT
- COMPANY

Do NOT blanket-enforce Tenant + Company on every operation.

## 5. CONTINUATION — DO NOT RESET P03

This is NOT another full P03 Deep Research round.
Do NOT restart L1-L6.
Do NOT discard existing files/evidence.
Do NOT re-run broad source/database census without Material Delta.

Preserve P03 baseline findings from `7fca09...`, including:
- P03R-F-01 subsidiary valuation ledger vs GL divergence;
- 30 extreme valuation rows up to approximately +/-1.5e21 and the recorded -48.7% inventory distortion;
- manufacturing as amplifier, not proven origin, of the corruption;
- 1 live / 11 latent / 3 unreachable classification at that baseline;
- work-centre rate + real-time valuation never coexisting in examined deployments;
- prior AAS+ veto and PMO HOLD;
- all RE-P03 / DC / DEP / UNR / TZ lineage.

Only reopen a baseline conclusion when NEW material evidence directly affects it.

## 6. MANDATORY P01 DELTA INTAKE

Reconcile the latest published P01 facts into P03 without changing their evidence classification.

### 6.1 Purchase price differences
Current P01 evidence says the earlier exposure was inverted:
- price differences are observed capitalised into inventory on roughly 1,100–1,300 occasions;
- no purchase-price-variance line reaches P&L in the observed path;
- exact counts `1,123` vs `1,267` remain unreconciled because UNIT/PREDICATE may differ.

P03 must determine, with evidence:
- where those amounts can flow once RM enters manufacturing;
- whether RM valuation differences propagate to WIP / Semi / FG / COGS;
- whether propagation preserves traceable lineage or merely embeds changed unit cost;
- whether the P03R-F-01 divergence intersects the same valuation/revaluation mechanisms or is independent;
- whether any existing conclusion risks double-counting or zeroing the same economic effect.

Do NOT assume P01 variance = P03 corruption.
Prove or keep separate.

### 6.2 Kit / phantom / purchase_mrp correction gap
P01 found source behavior stating kit invoice correction must be handled manually and found the path latent in its current deployment.

P03 must determine:
- exact relationship to kit/phantom BoM semantics;
- purchase -> receipt -> components -> MO/WIP/FG accounting path where applicable;
- whether the manual correction can be lost, duplicated, or capitalised incorrectly when manufacturing consumes the items;
- whether any examined P03 deployment actually uses kit/phantom/subcontract behavior;
- live / latent / unreachable classification with denominator.

Do not turn a P01 latent finding into a P03 live defect without deployed evidence.

## 7. MANUFACTURE-TO-COST CAUSAL CHAIN — TARGETED REVALIDATION

Trace only the material chains affected by current deltas:

`Purchase/Receipt Cost Truth`
-> `RM Valuation`
-> `Consumption`
-> `WIP`
-> `Semi/FG`
-> `Production Completion`
-> `Delivery/COGS`
-> `GL / Management Cost / Reconciliation`

For each link classify:
- FACT VERIFIED
- SUPPORTED INTERPRETATION
- DESIGN CANDIDATE
- CONTRADICTED
- UNRESOLVED — EVIDENCE REQUIRED

Separate:
- costing method;
- valuation policy;
- operational quantity/event truth;
- financial posting;
- management allocation.

## 8. FIXED OVERHEAD / ASSET / EQUIPMENT COSTING — BOSS POLICY INPUT

Carry forward Boss-approved Asset/Equipment policies as controlled design inputs, not benchmark facts:

1. Every active-period depreciation amount must be fully attributed.
   - productive -> WIP/FG;
   - non-productive -> named operational cause;
   - no unclassified depreciation.
2. Continuous internal equipment usage after full depreciation has no residual-value cap and does not consume financial residual book value.
3. Financial depreciation and managerial/internal allocation are separate truths.
4. Work Center membership alone is NOT evidence of machine cost absorption.
5. Cost causality target:
   `Routing -> Operation -> Equipment Actually Used -> Equipment Usage Cost -> MO/WIP/FG`.
6. Source evidence previously confirms Operation -> Work Center but not Operation -> Specific Equipment; preserve this as a source gap unless new evidence changes it.
7. Productive allocation methods approved as options: Machine Hour / Work Center Hour / Production Quantity; no mandatory default.

P03 must NOT redesign Asset architecture.
P03 must answer only Manufacture-to-Cost implications and exact integration boundary.

## 9. FIXED OVERHEAD INJECTION GAP

Reconcile the existing P03 claim that depreciation / planned maintenance / energy / indirect labour lack a verified injection path into inventory.

For each cost component:
- source mechanism found/not found;
- deployed mechanism exercised/not exercised;
- operational driver/event;
- target cost object (Operation/MO/WIP/FG/nonproductive cause);
- financial vs managerial ledger boundary;
- source gap vs configuration gap vs deployment gap vs SMEsPlus design candidate.

Do not invent a posting path.
Do not use Work Center membership as a substitute for actual equipment/operation causality.

## 10. P03R-F-01 VALUATION/GL DIVERGENCE — TARGETED CLOSURE

Do not perform unsafe correction.

Revalidate only what is necessary to answer:
- exact origin event family of the extreme rows;
- why named journal entries exist with sane values while valuation rows carry extreme values;
- whether reversal/unbuild rows explain arithmetic cancellation but not semantic correctness;
- whether purchase/bill revaluation and manufacturing consumption share identifiers that establish provenance;
- whether any repair would release enormous values because rows nearly cancel;
- what controls SMEsPlus requires to prevent subsidiary/GL divergence.

No database mutation.
No repair execution.
No production correction.

If remediation requires write testing, prepare a bounded authorisation package; do not execute without explicit Boss authorisation.

## 11. DEPLOYED CODE IDENTITY / CUSTOM OVERRIDES

For each load-bearing P03 mechanism, identify where evidence permits:
- installed module;
- source identity;
- custom override / extension;
- function or input modifier;
- deployed evidence;
- generation;
- scope.

Explicitly include modules that alter writer inputs even when they are not writers themselves.

Use statuses:
- MATCH VERIFIED
- PARTIAL MATCH
- SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED
- SOURCE MISSING
- DEPLOYED CODE IDENTITY UNRESOLVED

## 12. CROSS-PROCESS ROUTING

Create/update explicit handoffs:

### P03 -> P08
Route:
- valuation/GL divergence;
- price-difference capitalization and financial-statement implications;
- period-close/reconciliation control requirements.

### P03 -> P11
Route:
- surviving Manufacture-to-Cost truths;
- P01/P03 contradictions or convergence;
- unresolved ownership/policy decisions;
- subsidiary-vs-GL integrity requirements.

### P03 -> Asset/Inventory tracks
Route only integration boundaries:
- Operation/Equipment causal gap;
- WIP/FG costing interface;
- valuation lineage requirements.

Do not settle another process's unresolved decision inside P03.

## 13. FOUR AAS-03 FRESH CHALLENGES — NEW DELTA ONLY

Run four independent challenges:

1. Leader Functional Design
   - attack RM -> WIP -> FG economic causality and kit/phantom semantics.
2. Leadership Database Design
   - attack P03R-F-01 provenance, identity, subsidiary/GL reconciliation and denominator.
3. Lead Integration & Localization
   - attack P01->P03 handoff, valuation/period/tax/localization boundaries and cross-process ownership.
4. Lead Code & UI Architect
   - attack deployed-code identity, input-modifying overrides, Operation/Equipment gaps and source/runtime reachability.

Each must state:
- supported;
- missing;
- risky;
- challenged;
- evidence needed next.

At least one expert must actively try to disprove any proposed relation between P01 price differences and P03R-F-01.
At least one expert must attack the kit/phantom denominator.
At least one expert must challenge whether a fixed-overhead injection path is genuinely absent or merely outside declared source scope.

Preserve disagreement.

## 14. AAS+ / PMO TARGETED CLOSURE

AAS+ reconciles the four challenges and preserves dissent.

PMO reassesses only material P03 exit criteria affected by this round.
Do not improve status because more work was done.
Downgrade if evidence quality worsens.

Answer explicitly:
- Is P03 evidence sufficient for controlled G01 handoff?
- Which blockers are P03-owned vs P01/P08/P11/Asset/Inventory-owned?
- Is any broad P03 research still justified?
- Are any load-bearing background tasks still alive?

## 15. REQUIRED DELIVERABLES

Create/update as evidence requires:
- `P03_P01_DELTA_INTAKE_REGISTER.md`
- `P03_PRICE_DIFFERENCE_TO_MFG_TRACE.md`
- `P03_KIT_PHANTOM_COST_CORRECTION_TRACE.md`
- `P03_VALUATION_GL_DIVERGENCE_CLOSURE.md`
- `P03_FIXED_OVERHEAD_INJECTION_MATRIX.md`
- `P03_EQUIPMENT_OPERATION_COST_CAUSALITY.md`
- `P03_DEPLOYED_CODE_IDENTITY_DELTA.md`
- `P03_TO_P08_HANDOFF.md`
- `P03_TO_P11_HANDOFF.md`
- updated Contradiction Register
- updated Revision/Error Log
- updated Source Link Register
- updated Evidence Manifest
- `P03_CHECKPOINT_REGISTER.md`
- `P03_AUTO_RESUME_STATE.md`

Preserve old files and lineage.

## 16. CHECKPOINTS + AUTO-RESUME

CP-01 — P03 baseline and P01 final handoff verified
CP-02 — P01 price-difference delta reconciled
CP-03 — kit/phantom/manufacturing delta reconciled
CP-04 — P03R-F-01 targeted provenance closure
CP-05 — fixed-overhead/equipment causality boundary completed
CP-06 — deployed-code identity delta completed
CP-07 — four AAS-03 challenges completed
CP-08 — AAS+ / PMO targeted closure completed
CP-09 — P08/P11 handoffs completed
CP-10 — terminality audit / remote publication completed

Auto-continue through executable checkpoints.
Do not ask Boss for routine intermediate approval.
Do not wait idle on an external dependency.

AUTO_RESUME_STATE must record exact next action and blockers.

## 17. TERMINALITY STANDARD

Before terminal reporting verify:
- no load-bearing background tasks remain undispositioned;
- all required evidence is committed;
- push completed;
- remote HEAD = intended final commit;
- every remaining HOLD has named owner/dependency;
- P08/P11/Asset/Inventory were not executed from P03;
- no merge to `SMEsPlus`;
- no database/environment mutation occurred unless separately Boss-authorised.

## 18. TERMINAL STATES — ONLY THESE

A. `G01-P03 READY FOR CONTROLLED HANDOFF — OPEN HOLDS NAMED`

B. `G01-P03 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`

C. `G01-P03 EVIDENCE INTEGRITY FAILURE — CORRECTION REQUIRED`

No PASS.
No Final Freeze.
No merge.
No implementation authorisation.

## 19. FINAL REPORT

Report concisely:
- P03 branch;
- final commit SHA;
- direct GitHub link;
- terminal state;
- P01 handoff SHA consumed;
- P01 price-difference disposition;
- kit/phantom disposition;
- P03R-F-01 disposition;
- fixed-overhead/equipment causality disposition;
- exact open holds and owners;
- P08/P11 handoff status;
- PMO recommendation;
- background task count;
- whether any write/mutation occurred.

## 20. STOP RULE

When all currently executable P03 work is exhausted:

COMMIT
-> PUSH
-> VERIFY REMOTE
-> UPDATE CHECKPOINT
-> UPDATE AUTO_RESUME_STATE
-> PRODUCE TERMINAL REPORT
-> STOP.

Do not wait idle.
Do not start P05 or P04 automatically.
Do not start P08/P11.
Do not merge.
