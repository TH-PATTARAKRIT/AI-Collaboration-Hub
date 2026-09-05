# [SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001]
# G01-P01 Procure-to-Pay — Controlled Research Scope Freeze, Evidence Reconciliation & Cross-Process Handoff / L99999.99999

## 1. PROJECT IDENTITY

Project: SMEsPlus ENTERPRISE SUITE
Parallel Group: **G01 — Supply / Cost / Payable**
Process: **P01 — Procure-to-Pay**
Execution Mode: **CONTINUE EXISTING OLD P01 SESSION**
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Working Branch: `research/account-p01-procure-to-pay-2026-09-04-001`
Baseline Commit: `a02ec8b6628daf145c03fa49397448a7f29605ea`
Boss: **Sole Final Approver**

## 2. MODEL / EFFORT — FIXED FOR THIS EXECUTION ENVELOPE

Use exactly:
- **Model: Claude Opus 5**
- **Effort: MEDIUM**

One Prompt = One fixed Model/Effort execution envelope.
Do not switch model or effort inside this run.

Reason: the remaining P01 work is primarily evidence reconciliation, ownership routing, checkpointing and handoff. It is meaning-sensitive but does not justify another broad forensic sweep.

## 3. PURPOSE

This is NOT another Deep Research round.
This is NOT a reset.
This is NOT a whole-domain or canonical freeze.

The purpose is to stop P01 from becoming endless research by formally freezing the **CURRENT RESEARCH SCOPE AGAINST CURRENT EVIDENCE**, reconciling the latest material deltas, and routing every unresolved fact to its correct downstream owner.

Canonical interpretation:

`CONTROLLED RESEARCH SCOPE FREEZE` means:
- no new broad source/database/estate sweep from P01 without Material Delta;
- current evidence and limitations are preserved;
- unresolved cross-process matters remain OPEN and are routed;
- Boss may reopen P01 later if materially new evidence arrives;
- this is NOT Final Freeze, NOT PASS, NOT merge authority, and NOT design approval.

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
No silent correction; preserve revision lineage.

Every material object/operation must determine applicable scope first:
- PLATFORM
- TENANT
- COMPANY

Do NOT blanket-enforce Tenant + Company on every operation.

## 5. PRESERVE AND RECONCILE LATEST P01 FACTS

Treat Baseline Commit `a02ec8b...` as the starting evidence state and verify remote HEAD before work.

Mandatory current deltas to preserve:

1. **Account 1173 disagreement closed on evidence**
   - `purchase_price_diff 16.0.1.1` is installed;
   - writer gate requires `cost_method == 'standard'`;
   - the relevant category is FIFO;
   - `anglo_saxon_accounting == FALSE` independently causes the caller to return early;
   - therefore an empty account 1173 is expected under this configuration and proves no failure by itself.

2. **Purchase price difference exposure is inverted from the earlier published interpretation**
   - observed evidence indicates price differences are capitalised into inventory on roughly 1,100–1,300 occasions;
   - no purchase-price-variance line reaches P&L in the observed path;
   - route accounting/reporting consequences to **P08 and P11**.

3. **`purchase_mrp` kit correction gap**
   - `_get_stock_valuation_layers` is modified and the source explicitly says invoice correction for kit is manual;
   - current P01 deployment shows zero phantom/kit activity, so the exposure is LATENT here;
   - route to **P03 Manufacture-to-Cost** for environments/processes where kits are used.

4. **1,123 vs 1,267 count disagreement**
   - preserve both measurements;
   - do NOT force reconciliation by arithmetic or name similarity;
   - identify UNIT / PREDICATE / POPULATION for each;
   - if the difference can be resolved cheaply from already-open evidence, resolve it;
   - otherwise preserve as `UNRESOLVED — UNIT/PREDICATE RECONCILIATION REQUIRED` and route to P08/P11 only if material.

5. **Writer enumeration method lesson**
   - installed modules that modify a writer's input may materially change behavior without being writers themselves;
   - record this as method control for downstream P03/P08/P11.

## 6. REQUIRED HANDOFFS

Create or update controlled handoff records with exact evidence locators.

### 6.1 P01 -> P03
Must include:
- kit/phantom purchase price-difference correction behavior;
- exact source module/function locator;
- current deployment evidence showing latent/not exercised here;
- question P03 must answer for RM/WIP/FG and Manufacture-to-Cost;
- no implied conclusion for deployments not measured.

### 6.2 P01 -> P08
Must include:
- purchase price differences capitalised into inventory;
- absence of observed P&L variance posting in this path;
- financial-statement / period-close / ledger implications requiring R2R reconciliation;
- any account-role/override boundary relevant to R2R.

### 6.3 P01 -> P11
Must include:
- authoritative P01 findings that survive;
- withdrawn/superseded findings;
- unresolved counts and exact reason;
- Boss decisions, if any;
- P03/P08 dependencies;
- current terminal recommendation.

## 7. FOUR AAS-03 CHALLENGES — TARGETED ONLY

Do NOT re-run full P01 challenges.
Run four short independent challenges only on the closure/handoff package:

1. Leader Functional Design
2. Leadership Database Design
3. Lead Integration & Localization
4. Lead Code & UI Architect

Each states:
- supported;
- missing;
- risky;
- challenged;
- evidence needed next.

At least one expert must try to disprove the claim that broad P01 research can safely stop now.
At least one must test whether the P01->P03 kit handoff preserves the correct boundary.
At least one must test the P01->P08/P11 price-difference handoff for semantic overstatement.

Preserve dissent. No expert declares whole-process PASS/FAIL.

## 8. AAS+ / PMO CLOSURE

AAS+ must reconcile the four targeted challenge outputs.
PMO must answer only:
- Is currently obtainable P01 work exhausted?
- Are all remaining dependencies named and owned?
- Is any load-bearing background task still running?
- Is any required evidence local-only/unpublished?
- Is a new broad P01 sweep justified by Material Delta? If NO, freeze current research scope.

Do not improve status simply because more files were written.

## 9. REQUIRED DELIVERABLES

Create/update as needed:
- `P01_CONTROLLED_RESEARCH_SCOPE_FREEZE.md`
- `P01_TO_P03_HANDOFF.md`
- `P01_TO_P08_HANDOFF.md`
- `P01_TO_P11_HANDOFF.md`
- `P01_FINAL_OPEN_DEPENDENCY_REGISTER.md`
- updated Contradiction Register
- updated Revision/Error Log
- updated Source Link Register
- updated Evidence Manifest
- `P01_CHECKPOINT_REGISTER.md`
- `P01_AUTO_RESUME_STATE.md`

Do not overwrite historical wrong findings; mark superseded/corrected with lineage.

## 10. CHECKPOINTS + AUTO-RESUME

CP-01 — baseline/remote-head verification
CP-02 — latest P01 facts reconciled
CP-03 — P01->P03 handoff complete
CP-04 — P01->P08 handoff complete
CP-05 — P01->P11 handoff complete
CP-06 — four targeted AAS-03 challenges complete
CP-07 — AAS+ / PMO closure assessment complete
CP-08 — terminality audit + publication complete

Auto-continue between checkpoints without Boss interaction.
At each material checkpoint update resume state.

## 11. TERMINALITY STANDARD

Before terminal reporting verify:
- all load-bearing background tasks = completed/dispositioned;
- git working tree has no required uncommitted evidence;
- commit pushed;
- remote HEAD verified;
- all open dependencies have named owner and exact next action;
- no P03/P08/P11 work was started from P01;
- no merge to `SMEsPlus` occurred.

## 12. TERMINAL STATE

Use exactly one:

A. `G01-P01 READY FOR CONTROLLED HANDOFF — RESEARCH SCOPE FROZEN FOR CURRENT EVIDENCE / OPEN DEPENDENCIES ROUTED`

B. `G01-P01 MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR NAMED DEPENDENCY`

C. `G01-P01 EVIDENCE INTEGRITY FAILURE — CORRECTION REQUIRED`

No PASS.
No whole-domain Final Freeze.
No merge.
No implementation authorisation.

## 13. FINAL REPORT

Report:
- branch;
- final commit SHA;
- direct GitHub link;
- terminal state;
- P03 handoff status;
- P08 handoff status;
- P11 handoff status;
- remaining dependencies;
- targeted AAS+ / PMO result;
- background task count;
- whether any mutation occurred.

## 14. STOP RULE

When all currently executable closure/handoff work is exhausted:

COMMIT
-> PUSH
-> VERIFY REMOTE
-> UPDATE CHECKPOINT
-> UPDATE AUTO_RESUME_STATE
-> PRODUCE TERMINAL REPORT
-> STOP.

Do not wait idle.
Do not start P03 automatically.
Do not start P08.
Do not start P11.
Do not merge.
