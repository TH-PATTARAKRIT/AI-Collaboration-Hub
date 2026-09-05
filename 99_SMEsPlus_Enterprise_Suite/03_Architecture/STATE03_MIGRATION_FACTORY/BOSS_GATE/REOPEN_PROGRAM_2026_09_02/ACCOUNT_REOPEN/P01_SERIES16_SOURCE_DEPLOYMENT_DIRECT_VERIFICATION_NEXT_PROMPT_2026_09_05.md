# [SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001]
# P01 Procure-to-Pay — Series-16 Same-Generation Source ↔ Deployment Direct Verification / L99999.99999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Program: Parallel Business Process Accounting Deep Research
Process: P01 — Procure-to-Pay
Execution Mode: CONTINUE EXISTING OLD P01 SESSION
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Working Branch: `research/account-p01-procure-to-pay-2026-09-04-001`
Baseline Commit: `f76e443df3b3e7c9545ca731f0d963a96d636ca0`
Boss: Sole Final Approver

## 2. MODEL / EFFORT FOR THIS EXECUTION ENVELOPE

Use exactly:

- Model: **Claude Opus 5**
- Effort: **HIGH**

ONE PROMPT = ONE FIXED MODEL/EFFORT EXECUTION ENVELOPE.
Do not dynamically change model or effort inside this run.

Reason: this round requires same-generation forensic reconciliation across source, deployed database, configuration, accounting semantics, valuation policy, Procure-to-Pay event flow, correction/reversal behaviour, and cross-process implications. It is materially semantic, not mechanical.

## 3. ABSOLUTE CONTINUATION RULE

NEW PROMPT != NEW SESSION.

Continue the existing P01 research lineage.

DO NOT:
- reset P01;
- restart from L1;
- discard prior evidence;
- discard ERR-P01-23;
- discard S18-B-07;
- silently rewrite prior false absences;
- search external sources for Series-16 during this run;
- re-run the completed wide source census;
- repeat unchanged work without material delta;
- ask Boss for routine continuation approval.

Preserve every prior wrong finding beside its correction.

## 4. MATERIAL DELTA THAT TRIGGERS THIS RUN

The current P01 branch establishes that the Series-16 blocker changed from:

`UNOBTAINABLE / VERIFIED ABSENCE`

to:

`SOURCE EXISTS ON THIS HOST / READABLE / UNREAD`.

Current evidence states:
- a readable Series-16 source estate exists locally;
- approximately 955 addons are present;
- `purchase/models/purchase.py` exists;
- Series-16 is the deployment in the estate with substantial real accounting history, including approximately 183,590 journal entries;
- prior statements that the Series-16 core was absent from the estate were false;
- prior probe methodology was insufficiently bounded: a bounded empty probe is an unfinished measurement, not a negative finding;
- the prior broad scan was OVERBROAD but successfully proved that the local estate contains the material source needed for targeted verification.

These facts must be re-derived from authoritative P01 files and the baseline commit before use.

## 5. EVIDENCE ESTATE FIRST — NO EXTERNAL SERIES-16 SEARCH

For this run, Series-16 research MUST use the evidence already present on the Boss-controlled host / declared P01 evidence estate.

Do not search the public web, external repositories, external downloads, or third-party mirrors for Series-16 source.

External acquisition is prohibited unless ALL of the following become true in a later separately authorized run:
1. the declared local evidence roots have been enumerated completely;
2. the exact target module/file is proven absent from those roots;
3. the absence is independently challenged;
4. the evidence gap is documented;
5. Boss explicitly authorizes external acquisition.

Current state does NOT satisfy those conditions because the required Series-16 source exists locally.

## 6. COMMON EXECUTION CONSTITUTION

Apply throughout this prompt:

- No Evidence = No Progress.
- Never Skip Gate.
- Boss = Sole Final Approver.
- Scope-aware Everywhere.
- Old Session First.
- No repeated question without material delta.
- Recommendation != Boss Decision.
- Peer Position != Boss Decision.
- UNRESOLVED != ADOPTED.
- Negative finding requires a declared denominator and a functioning positive control.
- A bounded probe returning empty is an unfinished measurement, not a negative.
- Same observed value != same accounting semantics.
- Same zero != same defect.
- Source existence != deployed activation.
- Configuration existence != execution proof.
- Database row existence != business-semantic correctness.

## 7. PRIMARY RESEARCH QUESTION

Determine, using SAME-GENERATION Series-16 evidence:

> How does the Procure-to-Pay business process actually behave from source mechanism through deployed configuration, accounting event creation, valuation/clearing treatment, Vendor Bill/AP recognition, payment/settlement, correction/reversal, and Thai-localization implications?

The target is not to describe generic ERP behaviour.
The target is to prove what the Series-16 source + Series-16 deployed database actually support.

## 8. REQUIRED TRACE MODEL

Use the canonical SMEsPlus forensic trace:

`Module → Model → Field Relation → Function/Event → Database → Accounting Effect`

FK/schema is supporting physical evidence only.
Do not make FK-first conclusions.

For every material finding, capture:
- source module;
- source file;
- class/function/method;
- model/field relations;
- trigger/event;
- configuration dependency;
- database population evidence;
- accounting effect;
- scope ownership;
- evidence classification;
- contradiction if any.

## 9. TARGETED SERIES-16 WORKSTREAMS

### S16-01 — Source Estate Identity & Module Activation

Verify the exact local Series-16 source roots relevant to P01.
Do not rebuild a whole-host index.

Target at minimum:
- purchase core;
- stock/inventory valuation dependencies;
- account/accounting dependencies;
- purchase request/custom approval path if deployed;
- landed cost/subcontract modules if materially reachable;
- Thai WHT/localization modules where applicable;
- custom modules referenced by current P01 findings.

For each module distinguish:
- source present;
- installed in Series-16 deployment;
- configured;
- exercised by transaction evidence;
- latent/unexercised;
- not determinable.

Deliverable: `P01_S16_MODULE_SOURCE_DEPLOYMENT_MATRIX.md`

### S16-02 — Purchase → Receipt → Valuation / Clearing

Trace same-generation source and database for:

`Purchase Order → Receipt → Inventory / Valuation Event → Clearing / Interim behaviour`

Determine:
- what source method creates or suppresses accounting/valuation effect;
- valuation policy/configuration prerequisites;
- product/category/account dependencies;
- whether goods-received clearing / stock input / interim accounts are configured;
- whether they are executed in real transaction history;
- whether Periodic vs Perpetual changes the observed result;
- whether identical zero-link populations are expected policy or defect.

Do not infer behaviour from zero counts alone.

Deliverable: `P01_S16_RECEIPT_VALUATION_CLEARING_DIRECT_PROOF.md`

### S16-03 — Receipt → Vendor Bill → AP

Trace:

`Receipt / Procurement Fact → Vendor Bill → Journal Items → AP Liability`

Determine:
- source linkage between purchase/receipt and bill;
- matching/quantity/price semantics supported by evidence;
- bill posting function;
- accounts selected;
- company/scope resolution;
- whether clearing/interim balances are relieved;
- whether source event identity survives into accounting lineage;
- what semantic information is lost.

Deliverable: `P01_S16_RECEIPT_TO_VENDOR_BILL_AP_TRACE.md`

### S16-04 — Vendor Advance / Partial Payment / Settlement

Reconcile P01 with P05 material where applicable.

Trace:
- vendor advance/down payment;
- partial payment;
- WHT on payment if applicable;
- reconciliation;
- final bill deduction;
- residual payable;
- settlement lineage.

Preserve P01/P05 disagreement unless same-generation evidence resolves it.

Deliverable: `P01_S16_VENDOR_ADVANCE_PAYMENT_SETTLEMENT.md`

### S16-05 — Thai WHT / PND Applicability

Do not force WHT into stock purchase where business/tax conditions do not apply.

Where Series-16 evidence supports withholding:
- identify source module;
- identify object/event that creates withholding;
- identify payment vs bill timing;
- certificate path;
- PND mapping;
- partial-payment behaviour;
- export/report lineage;
- company/scope ownership.

Separate:
`Source Behaviour`
from
`Thai Statutory Requirement`.

If statutory interpretation cannot be proven from approved primary authority already in the estate, classify as `UNRESOLVED — STATUTORY EVIDENCE REQUIRED`; do not invent.

Deliverable: `P01_S16_WHT_STATUTORY_BEHAVIOUR_BOUNDARY.md`

### S16-06 — Correction / Cancellation / Reversal

Trace posted-document correction for:
- Purchase Order-related accounting facts;
- Receipt reversal/return;
- Vendor Bill reset/cancel/reversal;
- Payment cancellation;
- reconciliation unwind.

Determine whether correction is:
- immutable reversal;
- destructive delete;
- reset/rewrite;
- date relocation;
- mixed/path-dependent.

Record period-lock interaction.

Deliverable: `P01_S16_CORRECTION_REVERSAL_INTEGRITY.md`

### S16-07 — Period Close / Cut-off

Test the accounting semantics around:
- receipt before bill;
- bill before/after close;
- receipt in one period and bill in another;
- clearing/interim carry-forward;
- re-dating behaviour;
- lock-date enforcement vs relocation;
- late bill / late correction.

Do not treat soft re-date as hard refusal.

Deliverable: `P01_S16_PERIOD_CLOSE_CUTOFF_MATRIX.md`

### S16-08 — Source ↔ DB Same-Generation Contradiction Register

For every material source mechanism, classify deployment evidence as:
- ACTIVE AND EXERCISED;
- ACTIVE BUT UNEXERCISED;
- CONFIGURED BUT UNEXERCISED;
- SOURCE PRESENT / MODULE NOT INSTALLED;
- DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION;
- NOT DETERMINABLE.

Deliverable: `P01_S16_SOURCE_DB_CONTRADICTION_REGISTER.md`

## 10. REQUIRED BUSINESS PROCESS VIEW

After forensic verification, reconstruct the real Series-16 Procure-to-Pay process using evidence only:

`Need / Request`
→ `Purchase Order`
→ `Receipt`
→ `Inventory / Expense / Valuation Effect`
→ `Clearing / Interim State`
→ `Vendor Bill`
→ `AP`
→ `Payment`
→ `WHT if applicable`
→ `Reconciliation / Settlement`
→ `Correction / Return / Reversal`
→ `Period Close / Reporting`

For each step state:
- Business Fact;
- operational source object;
- accounting event;
- GL/financial effect;
- scope;
- status of evidence.

Deliverable: `P01_S16_BUSINESS_PROCESS_ACCOUNTING_MAP.md`

## 11. ACCOUNTING SEMANTIC CLASSIFICATION

Every material conclusion must be one of:

- FACT VERIFIED
- SUPPORTED INTERPRETATION
- DESIGN CANDIDATE
- CONTRADICTED
- UNRESOLVED — EVIDENCE REQUIRED

Do not upgrade interpretations to facts.
Do not downgrade contradictions to differences of opinion.

## 12. FOUR AAS-03 INDEPENDENT EXPERT CHALLENGES

Run four independent challenges after the primary evidence package is complete.

### Expert 1 — Leader Functional Design
Challenge:
- real Procure-to-Pay business flow;
- missing business states;
- receipt/bill/payment semantics;
- returns/corrections;
- user/business reality.

### Expert 2 — Leadership Database Design
Challenge:
- population denominator;
- same-generation database identity;
- lineage loss;
- destructive corrections;
- company/scope isolation;
- source↔DB inconsistencies.

### Expert 3 — Lead Integration & Localization
Challenge:
- Thai WHT/PND;
- tax/localization boundaries;
- external payment/settlement dependencies;
- cross-module handoffs;
- version-specific localization variance.

### Expert 4 — Lead Code & UI Architect
Challenge:
- actual source call paths;
- method overrides;
- hidden configuration dependencies;
- inactive/latent mechanisms;
- UI text vs code behaviour;
- custom module collisions.

Each expert must state:
- What is supported;
- What is missing;
- What is risky;
- What is challenged;
- Evidence needed next.

Experts do NOT issue PASS/FAIL.
Preserve disagreement.

Deliverable: `P01_S16_AAS03_FOUR_EXPERT_CHALLENGE.md`

## 13. AAS+ CONSOLIDATION / VETO

AAS+ must consolidate:
- agreements;
- disagreements;
- contradictions;
- denominator defects;
- scope defects;
- false negative risks;
- policy-vs-defect distinctions;
- cross-process conflicts with P03/P05/P06/P07/P08/P09/P10/P11.

AAS+ may recommend HOLD/VETO but may not decide Boss-only architecture policy.

Deliverable: `P01_S16_AAS_PLUS_CONSOLIDATION.md`

## 14. PMO REVIEW

PMO must verify:
- all claimed evidence exists;
- source locator is reproducible;
- database identity is declared;
- denominator is explicit;
- changed findings have revision lineage;
- no old wrong finding is deleted;
- no external Series-16 acquisition occurred;
- all peer dependencies are named;
- gate movement is evidence-based only.

Deliverable: `P01_S16_PMO_REVIEW.md`

## 15. PEER DELTA / P11 HANDOFF

Consume peer evidence DELTA-ONLY using last-consumed SHAs.
Do not reread unchanged peer packages.

Route material P01 Series-16 deltas to P11 when they affect:
- accounting source of truth;
- clearing/interim semantics;
- period close;
- WHT;
- correction/reversal;
- scope ownership;
- event identity;
- same-generation vs cross-generation interpretation;
- Boss Decision Package.

Deliverable: `P01_S16_P11_HANDOFF.md`

## 16. CHECKPOINT + AUTO-RESUME

Maintain/update:
- `P01_CHECKPOINT_REGISTER.md`
- `P01_AUTO_RESUME_STATE.md`

Checkpoint statuses:
- NOT STARTED
- IN PROGRESS
- COMPLETE — EVIDENCE VERIFIED
- PARTIAL — RESUMABLE
- BLOCKED — EXTERNAL DEPENDENCY
- BLOCKED — TOOL / PERMISSION
- BLOCKED — EVIDENCE REQUIRED
- SUPERSEDED — MATERIAL DELTA

Checkpoints:

CP-P01S16-00 — Baseline / branch / prior revision lineage verified
CP-P01S16-01 — Local Series-16 source roots targeted and verified
CP-P01S16-02 — Module source↔deployment matrix complete
CP-P01S16-03 — Purchase→Receipt→Valuation/Clearing proof complete
CP-P01S16-04 — Receipt→Vendor Bill→AP proof complete
CP-P01S16-05 — Vendor advance/payment/settlement proof complete
CP-P01S16-06 — Thai WHT boundary proof complete
CP-P01S16-07 — Correction/reversal proof complete
CP-P01S16-08 — Period close/cut-off proof complete
CP-P01S16-09 — Same-generation contradiction register complete
CP-P01S16-10 — Business process accounting map complete
CP-P01S16-11 — AAS-03 four-expert challenge complete
CP-P01S16-12 — AAS+ consolidation complete
CP-P01S16-13 — PMO review complete
CP-P01S16-14 — P11 handoff complete
CP-P01S16-FINAL — Commit/push verified, resume state current

AUTO-CONTINUE after every completed internal checkpoint.
Do not ask Boss to continue.

## 17. EVENT-DRIVEN / NO-IDLE-TOKEN RULE

When currently executable work is exhausted:

COMMIT
→ PUSH
→ VERIFY REMOTE
→ UPDATE CHECKPOINT
→ UPDATE AUTO_RESUME_STATE
→ RECORD NEXT EXACT ACTION / EVENT
→ STOP.

Do not remain active waiting for:
- Boss;
- peers;
- external evidence;
- permissions;
- background filesystem scans;
- network/cloud storage.

If a secondary corroborative background task becomes BLOCKED_ON_IO and the load-bearing question is already settled by an independent stronger route:
- preserve diagnostics;
- disposition the secondary route;
- do not wait indefinitely;
- do not allow terminal verdict with undispositioned instrumentation.

## 18. PROHIBITED ACTIONS

Do NOT:
- merge to `SMEsPlus`;
- create implementation code;
- modify production;
- approve architecture;
- close Boss decisions;
- silently repair source code;
- alter deployed databases;
- create transactions merely to manufacture runtime evidence unless separately authorized;
- claim statutory compliance from source behaviour alone;
- search external Series-16 source while the local evidence estate remains sufficient.

## 19. SUCCESS CONDITION

Success does NOT require all P01 blockers to close.

Success requires:
- same-generation Series-16 source and deployment are directly reconciled;
- Purchase→Receipt→Bill→AP→Payment process is evidence-mapped;
- valuation/clearing behaviour is policy-sensitive and proven;
- source-present vs installed/configured/exercised is separated;
- correction/reversal and period-close behaviour are classified;
- Thai WHT boundary is evidence-safe;
- old false absence is preserved in revision lineage;
- all changed findings are reclassified honestly;
- AAS-03/AAS+/PMO complete;
- P11 receives material delta;
- checkpoint/resume state is current;
- no external Series-16 acquisition occurred.

## 20. TERMINAL STATES

Allowed terminal states:

`P01 SERIES-16 SAME-GENERATION DIRECT VERIFICATION — READY FOR CORE ACCOUNTING RECONCILIATION`

or

`P01 SERIES-16 SAME-GENERATION DIRECT VERIFICATION — MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR SPECIFIC SOURCE / DATABASE / POLICY / PEER / STATUTORY / BOSS DECISION`

Do NOT declare PASS, freeze, merge, implementation authorization, or Boss approval.

## 21. FINAL RESPONSE FORMAT

Report exactly:

SESSION: P01 — Procure-to-Pay
PROMPT: [SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001]
MODEL: Claude Opus 5
EFFORT: HIGH
BASELINE COMMIT: f76e443df3b3e7c9545ca731f0d963a96d636ca0
SERIES-16 SOURCE ROOTS: <count / paths / verified>
SERIES-16 MODULES: <source present / installed / configured / exercised / latent>
DEPLOYMENT ACCOUNTING POPULATION: <verified counts>
PURCHASE→RECEIPT: <status>
VALUATION / CLEARING: <status>
RECEIPT→BILL→AP: <status>
ADVANCE / PAYMENT / SETTLEMENT: <status>
THAI WHT: <status>
CORRECTION / REVERSAL: <status>
PERIOD CLOSE / CUT-OFF: <status>
SOURCE↔DB CONTRADICTIONS: <total / closed / open>
FINDINGS: <total / changed / withdrawn / contradicted / unresolved>
BLOCKERS: <total / closed / open / severity>
AAS-03: <status>
AAS+: <status>
PMO: <status>
P11 HANDOFF: <status / commit if published>
LAST VERIFIED CHECKPOINT: <ID>
CURRENT CHECKPOINT: <ID>
NEXT EXACT ACTION: <action or NONE>
RESUME MODE: AUTO
EVENT-DRIVEN STATE: <STOPPED / READY_TO_RESUME / COMPLETE>
BRANCH: research/account-p01-procure-to-pay-2026-09-04-001
FINAL COMMIT: <actual SHA>
DIRECT GITHUB LINK: <actual verified URL or PUBLICATION BLOCKED>
FINAL STATUS: <allowed terminal state>

Then STOP.
Do not start another research round.
Do not wait idle.
