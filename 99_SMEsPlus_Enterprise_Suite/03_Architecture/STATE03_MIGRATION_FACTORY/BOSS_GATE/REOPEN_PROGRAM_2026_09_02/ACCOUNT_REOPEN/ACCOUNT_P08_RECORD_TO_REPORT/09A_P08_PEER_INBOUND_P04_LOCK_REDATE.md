# P08 — INBOUND PEER FINDING FROM P04 (ACQUIRE-TO-RETIRE), VERIFIED AND ACCEPTED

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`
Origin: P04 — Acquire-to-Retire, branch `research/account-p04-acquire-to-retire-2026-09-04-001`, files 04 §4, 10 §8, 11 §3.
Handling: **verified independently by P08 against primary source before acceptance.** `Independent Review != Truth. Verified Evidence = Truth Basis.`

## 1. The finding

`P08-PEER-01` — **The irrevocable lock relocates rather than refuses, on the posting path.**

P08 had already established that posting silently moves an entry's accounting date forward when the requested date violates a lock. P08 had **not** established which locks participate. P04 asserts the irrevocable lock does. **Verified: it does.**

The violation lookup used by the posting routine is called with the hard-lock flag **set** (`EV-CL-17`). The routine then overwrites the entry's date with the accounting date derived from the last violated lock, and the subsequent check passes because the date has already been mutated. The violation is resolved by moving the entry, not by refusing it.

`FACT VERIFIED`. This is a **material sharpening** of `JPM-04` and `PC-02`, and it is recorded as a revision rather than as a restatement, because the prior wording left the irrevocable lock's behaviour on this path unstated and would have been read as "the irrevocable lock is the one control that refuses".

## 2. The reference product asserts this behaviour in its own test

P04 reported a product test that asserts the relocation. **Verified, and the verified case is stronger than the paraphrase.** With a fiscal-year lock set mid-year, a depreciation entry dated **31 December of the prior year** is asserted to post as **31 July of the following year** — carrying a full annual charge across a fiscal-year boundary into the wrong year. The depreciation schedule still shows the right number of entries; the charge has migrated. `EV-CL-18`.

That the behaviour is **asserted by a product test** rather than merely permitted by the code raises its evidential standing: it is intended behaviour, not an oversight.

## 3. The contrast inside one module

`P08-PEER-02` — **One control, two opposite behaviours.** The same fiscal lock date **hard-refuses** an asset re-evaluation with an explicit error (`EV-CL-19`), while the posting path **relocates**. `FACT VERIFIED`.

This is the sharpest available illustration of the package's general finding: the lock is not a property of the period, it is a condition each code path chooses how to honour. A period has no state to be in, so there is nothing for the paths to agree about.

## 4. Correction to P08's own kernel model

`P08-PEER-03` — **P08's statement that "there is no subledger, only a projection" was too broad, and is corrected here.**

P08 established that the **partner** subledger is a projection of journal items net of the matching graph. P04 reports, correctly, that the **fixed-asset register is a genuinely separate store**, and that nothing reconciles it to the ledger. The same is true of the inventory valuation record.

**Corrected position:**

| Subsidiary record | Nature | Reconciled to the ledger? |
|---|---|---|
| Partner open items | a **projection** of ledger facts and the matching graph | not applicable — it is the same data |
| **Fixed-asset register** | a **separate store** with its own values and its own lifecycle | **no mechanism found** |
| **Inventory valuation record** | a **separate store** | **no mechanism found** |

`A VERIFIED ABSENCE` is **not** claimed for the reconciliation mechanism — P08 did not run that search. Class **`C NOT YET SEARCHED`** for P08's own scope; P04 reports six mechanisms that can break agreement and nothing that detects any of them, which P08 records as a peer finding and does not restate as its own verified result.

**Consequence for `03_P08_ACCOUNTING_KERNEL_MODEL.md`:** `KRN-03` ("the general ledger is not a store; it is a reading") stands. `KRN-06` stands for the partner dimension. What must be added is that **where a genuine subsidiary store does exist, the kernel provides no reconciliation obligation at all** — no periodic proof, no control-account tie-out, no exception. That is a gap in the kernel, not in the asset module, and P08 owns it.

New requirement: `P08-RQ-KRN-01` — *every subsidiary store that carries an independently maintained value must have a stated control-account relationship and a periodic proof that the two agree, and the failure of that proof must be an accounting event.*

## 5. Item re-opened on P08 by P04

`P08-PEER-04` — **The tax-book / tax written-down-value gap.** P04 re-registers this as `P04-B-13` with owner P08, noting a prior Asset package called it the largest single functional gap for a Thai deployment and that it then fell out of every later register without being closed.

**P08 accepts the item and re-frames it as a kernel question, because that is where it belongs:**

> The kernel currently assumes **one measurement basis per fact**. A tax book is a **second measurement basis over the same facts** — same events, same instructions, different valuation rule. Any kernel that cannot carry more than one basis cannot produce a tax position without duplicating the ledger.

New requirement: `P08-RQ-KRN-02` — *the financial fact carries its measurement basis, and the kernel supports more than one basis over one set of accounting events, without duplicating the events.*

New Boss decision: `P08-BD-11` — *how many measurement bases must SMEsPlus carry, and are they parallel books, parallel valuations on one fact, or a derived adjustment layer?* This is normative and no amount of research resolves it.

**Statutory half held.** That Thai statutory depreciation rates are ceilings, and that book and tax therefore diverge by design, is a statement about Thai law. It is `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track, and is **not** relied upon by any P08 conclusion. What P08 relies on is only the structural point: a system that carries one basis cannot express two.

## 6. Cross-session corroboration recorded

`P08-PEER-05` — P04 independently reached, from a different starting point and a different module, two conclusions P08 reached in this session: **no profit-and-loss year-close entry exists**, and **retained-earnings reallocation happens inside the report result and never in the ledger**. Two independent sessions converging on the same finding from different evidence is recorded as corroboration.

It is **not** recorded as closure. Both sessions searched the same product line, and a shared blind spot would produce exactly this agreement. The claim's class is unchanged: `A VERIFIED ABSENCE` within P08's stated target-root scope, and `B NOT FOUND IN SEARCHED SCOPE` at the 22-root level, per `RS-B-01`.

## 7. Dispositions

| ID | Disposition |
|---|---|
| `P08-PEER-01` | **ACCEPTED, VERIFIED.** Sharpens `JPM-04`, `PC-02`. Logged in `21_P08_REVISION_LOG.md` §5 |
| `P08-PEER-02` | **ACCEPTED, VERIFIED.** Added to `17_P08_CONTRADICTION_REGISTER.md` as `P08-CONTRA-16` |
| `P08-PEER-03` | **ACCEPTED, and it corrects P08.** New requirement `P08-RQ-KRN-01`; the reconciliation-mechanism absence is class `C` for P08 |
| `P08-PEER-04` | **ACCEPTED as a kernel question.** New requirement `P08-RQ-KRN-02`; new decision `P08-BD-11`; statutory half `HOLD` |
| `P08-PEER-05` | **CORROBORATION RECORDED.** No class change |

No permission, approval or authority was taken from the peer message. It supplied evidence, which P08 verified before using.
