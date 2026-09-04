# P06_AAS_PLUS.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Function:** adversarial synthesis over the whole P06 package, preserving dissent, with veto authority over onward reliance.

**Reading instruction:** cite §3 and §6 of this file. Do **not** cite the package's headline tables — the corrections are here, in the AAS-03 challenge, and in each register's own §8. This instruction is repeated because the programme has twice found that summaries silently upgrade what the bodies qualified.

---

## 1. What P06 actually established

Stripped to its load-bearing claims, this package establishes four things, and each is stronger than the individual findings that compose it.

**1. The canonical question has an answer, and the answer is "no."**
The directive asked whether payment state, accounting posting state, bank confirmation state and reconciliation state can be determined independently. **They cannot.** There are two stored states, one configuration-dependent derivation, and — for bank confirmation — **no concept at all**. This is not a set of defects to be patched; it is the shape of the reference model, and the target must author all four as separately written facts.

**2. The bank half of the process runs entirely on unmodified reference behaviour.**
Twelve custom modules were examined in the P06 scope. **All twelve return NOT FOUND for `account.bank.statement`** (CMD-F-15). Every custom extension in this estate works on the payment side. The bank-event and reconciliation halves — where all seven confirmed attack defects live — have never been touched, reviewed or adapted by this project.
**That is the most consequential structural fact in the package**, and it emerged from a denominator table, not from any single finding.

**3. The identity system fails open, in the same direction, at every layer.**
Four of seven ingestion doors attach no identity. Three enforcement points each treat a null identity as "not a duplicate." A detection wizard exists whose queries prove the identities it searches for can repeat. The provider reference — the one key a bank or provider settlement report will use — is unconstrained, unindexed, never searched, and overwritten by the last callback received.
**The consistency of the direction is the finding.** A system that fails open once has a bug; a system that fails open at every layer has a design assumption.

**4. Unsettled money has a home but no clock.**
Suspense, transit, cheques-in-flight and money-on-account are all either `asset_current` — structurally invisible to the only ageing report that exists — or have no object at all. The reference knows where to put money it cannot explain. It has no mechanism for noticing that it is still there.

---

## 2. What P06 did not establish, stated before anything else

- **No runtime or database evidence.** Every runtime claim is second-hand through one CSV extract. Five open items are answerable only against data.
- **No sibling package was read.** Every cross-process ownership assignment is a proposal. `P06-B-03`, **PEER DEPENDENCY OPEN**.
- **No statutory Thai position.** WHT, cheque practice, e-payment recordkeeping, retention: all **HOLD**.
- **No deployment attribution.** Four custom copies, byte-identical in Python. Nothing here says what is running.
- **42 of 60 settlement cells uncharacterised**, and now explicitly bounded as such.
- **The custom approval estate was not searched** — which downgraded one of the package's own findings at challenge (AAS2-C-04).

---

## 3. AAS+ findings — where the package is weaker than it reads

**AASP-F-01 — The package's strongest evidence class is its zero-hit denominators, and that is also its most fragile.**
Roughly a third of the material findings rest on a declared zero. Each carries POPULATION, PATTERN, PATH SET and UNIT, which is the correct discipline. But the programme's own history records that **two of three origin failures were naming-variant misses** — searching `account.fiscalyear` when the model is `account.fiscal.year`. This package hit that class of error at least once and caught it: the reconciliation stream searched `_check_fiscalyear_lock_date` and found nothing, then located `_check_fiscal_lock_dates`. **It was caught because the searcher kept looking. There is no systematic control that would have caught it otherwise.**
**AAS+ position:** every Class-A negative in this package should be treated as *provisionally* Class A until a second, independently-worded search confirms it. That second pass was not run. `P06-B-40`.

**AASP-F-02 — One finding was downgraded at challenge, and it was downgraded for exactly the reason AASP-F-01 predicts.**
`P06-B-22` (no approval control on write-offs) declared three search scopes, all inside the reference tree, and missed three custom approval modules sitting in the same estate. **Class A → Class B.** This is not a hypothetical weakness; it is a demonstrated one, found by challenge rather than by the author.
**And it is the second finding in this package that an independent pass caught and the producing pass did not** — the first being the ingestion-door denominator (REV-E-01).

**AASP-F-03 — The scope correction changed conclusions, which means the pre-correction conclusions were scope-naive.**
CORR1 produced three downgrades, one re-scope and one entirely new HIGH contradiction (C-11, the payment token). C-11 was **invisible** under the earlier wording because "tenant and company everywhere" collapses the ownership/availability distinction that reveals it.
**AAS+ position:** the correction did not merely re-label findings; it found one. Any part of this package written before the correction and *not* listed in the Scope Matrix §5 revalidation carries a residual risk of the same blindness. The revalidation scan covered the token `tenant` and found two instances. **It did not scan for the deeper pattern — findings that assume a single boundary without naming it.** That scan was not designed and not run. `P06-B-41`.

**AASP-F-04 — The severity ranking across seven confirmed defects is asserted, not derived.**
The package classifies seven attacks as CONFIRMED DEFECT but supplies no ranking method. AAS-03 asked which would be retracted first and got an ordered answer, which is a proxy for confidence, not for impact.
**AAS+ position:** the gate needs an impact ranking, and this package cannot supply one without knowing the deployed configuration. **What it can supply is the precondition for each defect**, and those preconditions differ enormously: A1's CSV/QIF vector requires only that someone import a file twice; A6 requires a locked period and a user with unreconcile rights; A4b requires a partner with no company. **Recommendation: rank by precondition reachability, not by accounting magnitude**, and do that ranking after the deployment questions are answered.

**AASP-F-05 — The package repeatedly reports a control that "exists by accident" and then does not rely on it. That is correct, and it should be stated as a design principle rather than a series of caveats.**
RM-F-30 (lock date blocks widget validation as a side effect of line deletion), EGL-F-06 (suspense is correctly forced but never aged), EC-F-09 (transit balance is the only transfer control). In each case the reference has something that *behaves like* a control without *being* one.
**AAS+ position:** the target design's acceptance criterion should be explicit — **a control that cannot be named, tested and attributed to a requirement is not a control.** Four of this package's requirements exist only because an accidental behaviour was mistaken for one.

**AASP-F-06 — Two of the package's most useful artefacts are not on the required deliverable list.**
The Scope Ownership Matrix (produced by CORR1) and the Custom Module Delta (produced because the evidence would otherwise have dispersed). The required list would have lost the entire v14→v18 treasury regression — three not-migrated modules including the whole post-dated-cheque capability — because no required file owns it.
**AAS+ position:** this is a gap in the deliverable specification, not in the execution, and it should be fed back. `P06-B-42`.

**AASP-F-07 — The package asserts a positive design pattern exactly once, and it is worth more than several of the defects.**
`scgl_advance_expense_request` (EC-F-06) is the only object in the entire P06 evidence set with a first-class model, an approval state machine, computed exposure fields (`amount_residual`, `amount_toclear`, `is_clear`) and explicit clearing wizards. **It is a custom module, and it is better designed than the platform capability it substitutes for.**
**AAS+ position:** carry it forward as the reference shape for every unsettled-money object in the target — money-on-account, cheques-in-flight, transit, and unidentified receipts. A deep-research package that only enumerates defects has not finished the job.

---

## 4. Where AAS+ disagrees with the package

| # | Package position | AAS+ position | Status |
|---|---|---|---|
| 1 | A6 (lock dates do not gate reconciliation) is the strongest finding | **Agreed as evidence, but its consequence is understated.** The package frames it as "corrections after close are possible." The sharper framing is: **the reconciliation relation is outside the entire period-close regime**, so a signed-off bank reconciliation is not a durable fact at all. | **Escalated, not disputed** |
| 2 | C-01 (`is_matched` true with no statement) is a HIGH contradiction | **Agreed, and it is more than a contradiction — it is the reason blocker `P06-B-06` exists.** These should be linked; a reader of C-01 alone would treat it as a labelling bug. | **Linkage required** |
| 3 | The seven confirmed defects are the headline | **Disagree on emphasis.** The headline is CMD-F-15 — that no custom module has ever touched the bank side. The defects are consequences of that neglect. | **Dissent preserved** |
| 4 | A4a downgrade to HOLD is correct | **Agreed, but the HOLD is doing too much work.** Three separate blockers now depend on the same unanswered `root_id` question. **One query answers all three.** It should be the first thing the next session runs. | **Agreed with priority** |

---

## 5. Reliance assessment

| Dimension | Assessment |
|---|---|
| Evidence quality | **Strong.** First-hand source reading, `file:line` plus verbatim quotes throughout, denominators declared. |
| Denominator discipline | **Strong but not independently verified** — AASP-F-01, AASP-F-02. |
| Negative-claim discipline | **Applied, and it found four defects in the package's own wording.** One further downgrade came from challenge. |
| Self-correction | **Demonstrated four times**, twice by independent passes rather than by the author. |
| Scope discipline | **Applied mid-session under CORR1**, producing three downgrades and one new finding. Residual risk in AASP-F-03. |
| Runtime corroboration | **Absent.** Single largest limitation. |
| Cross-process reconciliation | **Absent.** PEER DEPENDENCY OPEN. |
| Statutory position | **Not taken.** Correctly HOLD. |

---

## 6. AAS+ veto

**AASP-VETO-01 — RELIANCE VETO on any onward use of this package as a *specification*.**
This package is admissible as **evidence for a decision**. It is **not** admissible as a design specification, and specifically:
- No requirement in it may be treated as settled while `P06-B-27` (the `root_id` question) is open, because three blockers depend on it.
- No Class-A negative may be relied upon until the second independently-worded search of AASP-F-01 is run.
- `P06-B-22` may not be cited at its original strength; it is Class B.
- No cross-process ownership assignment may be treated as agreed until the sibling packages are read.

**AASP-VETO-02 — VETO on any implementation start for P06.**
Independent of the Boss's own prohibition, AAS+ records its own veto and its own reason: **the target cannot implement four independent states, an owned bank-confirmation fact, and a company-scoped identity system while the boundary those things are scoped to is undetermined.** Implementation before `P06-B-27` closes would build the same ambiguity into new code.

**Conditions to lift AASP-VETO-01:** (a) `P06-B-27` answered; (b) the second negative-claim search run; (c) at least the P01, P02 and P05 packages read and reconciled.
**Conditions to lift AASP-VETO-02:** all of the above, plus a Boss decision on the seven confirmed defects and the statutory HOLDs.

**These vetoes are recorded, not exercised against anything.** No implementation was attempted and none was proposed.

---

## 7. Dissent register

Carried forward unresolved, per the standing requirement that AAS+ preserves rather than resolves dissent:

| ID | Dissent | Parties |
|---|---|---|
| DIS-01 | Currency rate scope: TENANT (package) vs global/PLATFORM (implementation) | package ↔ reference |
| DIS-02 | Batch-rejection wizard: unreachable vs incomplete checkout | unresolved, both recorded |
| DIS-03 | `root_id`: company boundary or not | unresolved, blocks 3 items |
| DIS-04 | Custom vendor advance: expensed asset or correctly configured | data-dependent |
| DIS-05 | Package headline: seven defects (package) vs the untouched bank side (AAS+) | AAS+ ↔ package |
| DIS-06 | A6 framing: "corrections possible" (package) vs "bank reconciliation is not a durable fact" (AAS+) | AAS+ ↔ package |

---

## 8. AAS+ position on terminal state

The session's declared terminal is **READY FOR CORE ACCOUNTING RECONCILIATION**. AAS+ assesses that the package **is** ready to be handed to Core Accounting Reconciliation as evidence — the handoff pack states its own limitations, the blockers are enumerated with owners, and the open items carry classes.

AAS+ records that readiness-to-hand-off is **not** readiness-to-rely, and the two must not be conflated in any downstream summary. The distinction is exactly what AASP-VETO-01 protects.

---

# End
