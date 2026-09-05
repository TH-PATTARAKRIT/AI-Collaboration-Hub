# P07 — AAS+ CONSOLIDATION

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Status: `PROVISIONAL / NON-CANONICAL` per `SMEPLUS-DR-EXIT-8C-001` §9
Date: `2026-09-04`

## 1. Standing of This File

`SMEPLUS-DR-EXIT-8C-001` §9 permits AAS+ to explore in parallel only as
`PROVISIONAL / NON-CANONICAL` while the parent Very Deep Research is incomplete. P07 is
incomplete: `EC-07` requires two consecutive clean independent passes and this is one pass
with one challenge round. **Nothing in this file is implementation authority.** No design is
proposed; what follows is consolidation of what the evidence forces, and what it does not.

## 2. The Single Structural Cause

Twelve of the nineteen `S1` findings reduce to one cause:

> **P07 owns tax-period membership, and the implementation delegates it to P08's accounting
> date.**

Thai law places a transaction in a tax month by its tax point (`S-01` … `S-04`, `S-30`).
The system places it by the accounting date. Once that substitution is made, the following
are not separate defects but consequences:

- services reported on an accrual basis where the statute prescribes payment (`V-D-02`);
- withholding reported in the month of the bill rather than the month of payment
  (`P07-F-11`);
- credit and debit notes landing in the month of the original rather than the month of the
  note (`P07-C-13`);
- a tax-point field that exists, is displayed, and cannot act (`P07-F-02`, `P07-F-03`);
- an excess-VAT carry-forward that looks back over a period defined by a user setting
  rather than by statute (`P07-F-40`).

Correcting any one of them in isolation leaves the cause in place. This is the position
that the core accounting reconciliation must settle first, because every other P07 decision
is downstream of it.

## 3. The Second Cause: Statutory Output Is a Render, Not a Record

The second cluster is independent of the first and equally structural:

> **Every statutory output in P07 is computed at render time from live master data, and no
> filed figure is stored.**

Consequences, all evidenced: at least eight ordinary non-privileged actions rewrite an
already-filed report (`08 §4`); the PND amount is recomputed from a rate rather than read
from the ledger (`P07-F-10`); the same tax fact yields three different computed amounts
(`03 §7.2`); row inclusion in a statutory register depends on a translatable label
(`P07-F-01`); and a filing record with a statutory deadline exists in the platform and is
not provisioned for Thailand (`P07-F-37`).

A tax authority asking "reproduce the return you filed in March" cannot be answered by this
system. That is the shortest statement of the second cause.

## 4. What the Evidence Forces, and What It Leaves Open

### 4.1 Forced by evidence

| # | Position | Forced by |
|---|---|---|
| 1 | The tax point must be an attribute of the tax fact and the sole selector of tax-period membership. | `P07-F-02`, `P07-F-03`, `P07-F-40`, `04 §5` |
| 2 | The withholding fact reported must be the withholding fact posted. | `P07-F-10`, `P07-F-11`, `P07-F-12`, `P07-F-53`, `03 §7.2` |
| 3 | Form and income classification must be typed attributes, not inferred from rate, tag text or a contact flag. | `P07-F-13`, `P07-F-15`, `03 §4.2` — the data model provides no typed attribute, so hardening the predicate cannot fix it |
| 4 | A filed figure must be fixed by a filing record. | `P07-F-36`, `P07-F-37`, `08 §4` |
| 5 | The tax invoice must be a document object. | `P07-F-26`, `P07-F-46`, and decisively `P07-F-47` — it **was** one in the prior generation |
| 6 | Statutory row inclusion must not depend on a translatable or user-editable label. | `P07-F-01`, `P07-F-42` |
| 7 | The `PLATFORM` statutory catalogue and the `COMPANY` financial binding must be separable. | `P07-F-18`, `P07-F-30`, `20 §4` |

### 4.2 Not forced — and therefore not decided here

| # | Question | Why P07 cannot decide it |
|---|---|---|
| 1 | Which of the two s.87 register implementations is canonical. | Both are installable, neither is declared; the choice has licensing consequences (`P07-D-07`, `P07-D-28`). Boss decision. |
| 2 | Which withholding framework is canonical. | The vendor framework has better primitives (a real tax line, its own sequence) and no Thai statutory output; the third-party one has the statutory output and is inert on a fresh install (`P07-F-51`). Boss decision. |
| 3 | Which extra-addon set is canonical. | Three same-generation roots exist outside the declared set, two of them supersets (`13 §2.1`). Until fixed, `P07-F-20` cannot be closed. Boss decision. |
| 4 | Whether the deferred input-tax claim is lawful in the form the tax-period field implies. | `P07-U-03`, `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| 5 | The statutory condition-of-withholding codes and the income-category-to-form mapping. | `P07-U-09`, `P07-U-10`, both held. |

## 5. Veto

`AASR-P07-VETO-01` — **No implementation may begin on the Thai tax-point design until
`P07-U-03` is closed with authoritative evidence.**

Reason: position 1 of §4.1 is forced, but the *purchase-side* form of it — a tax period
that legitimately differs from the invoice date — is exactly what `P07-U-03` governs. Building
the mechanism before the legal rule is established risks encoding a deferral the statute
does not permit, in the one place where the system already has a field for it. This veto is
narrow: it blocks the purchase-side deferral mechanism only, and does not block work on
positions 2 through 7.

## 6. Where AAS+ Disagrees With the Session Author

Recorded so the disagreement is visible rather than smoothed over.

| # | Author position | AAS+ position |
|---|---|---|
| 1 | `P07-F-01` is the highest-severity finding. | **Agreed, but for the reason the reviewers gave, not the author's.** The author's rate-lapse framing (`19 §8`) is a real but slow risk. The immediate risk is that installing the Thai language empties both registers. The Layer-1 file still leads with the slower risk and should be re-read with `P07-F-01` in front of it. |
| 2 | `P07-F-42` is `INF`. | **Agreed and retained as `INF`.** Two reviewers reached it independently and the chain is complete, but step 6 depends on record-creation order at load. It should not be reported as verified until `P07-U-20` is executed. Resisting the upgrade is the point. |
| 3 | The package is bounded by `EC-01`. | **Partly.** `PATH SET` is proven; `PATTERN` and `UNIT` were asserted and not executed (`16 §7`). `EC-01` should not be claimed. |

## 7. Handoff Position

P07 has produced what the core accounting reconciliation needs: the statutory basis, the
two structural causes, the seven forced positions, the five undecidable questions, and a
data contract (`10 §6`). It has **not** produced a converged research baseline, and under
`SMEPLUS-DR-EXIT-8C-001` it cannot, in one pass.

AAS+ recommendation to PMO: `RECOMMEND HOLD`, with the handoff released for
reconciliation work that does not depend on the held items.
