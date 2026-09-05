# P10 ↔ P04 — ASSET / TIME-BASED RECOGNITION RECONCILIATION

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1
Peer: `P04` Acquire-to-Retire, head `1636df4`, terminal `READY FOR CORE ACCOUNTING RECONCILIATION` with costing veto and PMO conditions not discharged.

**Boss ruling honoured throughout:** *never assume asset depreciation and deferred recognition share an implementation merely because both use schedules.* This reconciliation tests the two against each other on evidence produced independently by two processes.

---

## 1. Reconciliation Result — Summary

| Question | Result |
|----------|--------|
| Do P04 and P10 contradict each other on any material fact? | **No contradiction found.** Four facts were reached independently by both and agree |
| Did the reconciliation produce anything neither had alone? | **Yes — one new defect (`P10-F-38`) and one evidence-class upgrade (`P10-F-05` → executed positive control)** |
| Is the P04/P10 boundary settled? | **Partly.** The object boundary is settled; the *shared-mechanism* boundary is now the open question, and it has moved to `P08` |

## 2. The Four Independent Agreements

Both processes reached these separately, from different starting points, without seeing each other's work.

| # | Fact | P04's route | P10's route |
|---|------|-------------|-------------|
| `AG-1` | A locked-period entry is **silently re-dated, not refused**, by the generic posting routine, so it affects every programmatic post product-wide | From the asset board, with an executed test as its control | From the deferral generator, by reading the shared posting layer |
| `AG-2` | Disposal, by contrast, is **hard-refused** | Asset disposal path | Same path, reached while comparing lock guards across mechanisms |
| `AG-3` | The values driving the schedule are **UI-enforced only**, so every import or script bypasses them | Three of four asset values | Deferral eligibility enforced only by a form-level reaction, never as a stored constraint |
| `AG-4` | Attribution written onto a programmatic recognition post **nets to zero** | Depreciation, verified and published to `P09` | Deferral, re-derived independently here — `P10-F-38` |

> **CORRECTED — `34` `W-20`.** These are **not** four independent confirmations. `AG-1` and `AG-2` are one shared code path read by two processes, which is corroboration of a reading, not convergence of two implementations. Only **`AG-3` and `AG-4`** are genuine independent-implementation convergences, and `AG-4` is the stronger of the two.

## 3. `P10-F-38` — The New Finding

**Deferral recognition attribution nets to zero on the validation path, by the same mechanism P04 verified for depreciation.**

> **CORRECTED after the fresh challenge round — see `34` `W-02`, `W-03`, `W-04`.** As first written this section claimed the shape for *every* pair the engine creates, called the two records "mirror images", and classed the netting as unreproduced inference. All three were wrong in P10's favour or against it.

On the **validation path**, each recognition pair — the initial full-deferral leg and each period's recognition leg — writes **the same source-line attribution onto both rows, with opposite-signed amounts** (`E-P10-011`, and the pair construction at the two live generation sites). Because the analytic amount is linear and homogeneous in the balance, the two records cancel exactly. Six candidate breakers were tested under challenge — account-type filter, line-type filter, zero-amount skip, plan-level branch, sign convention, rounding — and **none breaks it**.

On the **grouped path the shape does not hold**: that path builds two *different* distributions, weighted differently and keyed on different grouping keys, and a vendor test asserts that behaviour.

They are **not** mirror images: the two records carry **different general accounts**, so they cancel at the analytic-account level and **not** under any grouping by general account.

Consequences, stated at P10's scope:
1. A deferred cost **reaches a cost object and leaves it in the same posting**. The recognition is attributable at line level and contributes nothing at balance level.
2. The mandatory-attribution gate does not bind it — **but not for the reason P10 first gave.** `34` `W-05`: deferral lines *are* product-type rows and pass that filter. The gate is inert because it requires a context key that only user-interface buttons supply. Same conclusion, different mechanism — and the difference matters, because a fix aimed at the stated cause would not close the hole.
3. Combined with `P09`'s finding that the allocation payload is absent from every lock-date list, every integrity-hash list and the tracked-field set, the attribution on a **posted, hashed, locked** recognition entry is freely editable and untracked.

Class: `VERIFIED FACT` for the code shape and, after `34` `W-04`, **also for the netting** — an executed vendor test asserts the same-distribution-on-both-rows shape on the validation path. Bounded to the declared reference root.

**`P10-F-41` is WITHDRAWN — class `E`, CONTRADICTED** (`34` `W-01`). P10 claimed the deferral test suite had no attribution coverage at all and self-certified it class `A`. Two dedicated attribution tests exist, one asserting exactly the shape described above. The claim was formed from one of the two test files and asserted over both.

## 4. `P10-F-39` — The Evidence Upgrade

The parent package carried the silent re-dating as a **source-verified inference**. P04 supplied a positive control and P10 re-read it line by line:

> An asset with a `2021-06-30` fiscal-year lock has a charge scheduled for `2020-12-31`. On validation it posts as **`2021-07-31`**. The product's own test asserts this as correct behaviour.

Two things follow, and the second is worse than the first:

1. The re-dating is **specified, not incidental**. It is not a defect of implementation; it is the intended behaviour of the posting layer, and any design that assumes it can be corrected as a bug is wrong about its status.
2. In that assertion, the `2020` charge and the `2021` charge **both land in fiscal year 2021**. FY2020 shows no charge; FY2021 shows two. **The vendor's own test suite asserts a fiscal-year misstatement as correct.**

`P10-F-05` is therefore raised from `INFERENCE` to `VERIFIED FACT with an executed positive control`, and its owner is `P08`, not P10 and not P04.

## 5. The Object Boundary — Settled

| Element | Owner | Basis |
|---------|-------|-------|
| The asset object, its lifecycle, its residual value, its disposal | **`P04`** | Uncontested; P04's package establishes it |
| The deferral, accrual and prepayment objects and their lifecycles | **`P10`** | Uncontested; P04 does not claim them |
| The depreciation *schedule* as an instance of time-based recognition | **Shared question** — see §6 | Both processes model it |
| The recognition *event* | **Neither, today** — see `27` | `P08` has established that no accounting-event object exists at all |

## 6. The Boundary That Moved

The parent package framed the design question as *asset engine versus deferral engine, and whether a kernel should span them*. The reconciliation has moved it.

> **CORRECTED — `34` `W-19`. This was P10's most damaging error against its own case.**

`AG-1` is a property of the shared posting layer: neither `P04` nor `P10` owns the code that re-dates.

`AG-4` is **not**. The identical-attribution-on-both-legs is constructed by **the deferral generator itself** and, independently, by **the asset engine itself**; the shared posting layer does not build it. So `AG-4` is **two independent mechanism-level implementations of the same wrong shape** — which is the strongest available evidence *for* a shared allocation layer, and P10 had handed it to `P08` as a posting-layer property.

So the corrected statement is narrower:

> **A shared recognition layer would not have prevented the silent re-date, which is below the kernel line. It would have prevented the attribution defect, which is not.**

This does not settle the kernel question — it **re-scopes** it. The kernel's value was argued in the parent package on auditability, correction behaviour and period-close behaviour. Of those three, **period-close behaviour is now demonstrably not a kernel matter**, and auditability depends on an event object that `P08` has shown does not exist anywhere. What remains genuinely kernel-shaped is the correction algebra and the allocation-convention library. The kernel case is **narrower after reconciliation than before it**, and `30` argues that adversarially.

## 7. Comparison Matrix — Delta Only

> **CORRECTED — `34` `W-07`.** This sentence was false when written. `27` §2 had silently reversed axis 3 of that very table: `08` §2 axis 3 records that a depreciation entry carries **the object link and a period beginning date**, and `27` §2 reduced it to "the asset link, not the period". The parent table was right and the new one was wrong; the parent table stands and `27` §2 is corrected.

Nothing in `P04`'s package contradicts the thirteen-axis comparison. Two axes gain peer confirmation:

| Axis | Parent finding | P04 confirmation |
|------|----------------|------------------|
| 12 — lock-date guards of its own | Asset has explicit guards on mutation and disposal; deferral has one only on the unused path | Confirmed: disposal hard-refuses while the board silently re-dates |
| 11 — catch-up | Asset catch-up is a stub entry cut at the modification date | Consistent with P04's modification account |

One axis is **superseded by the reconciliation**: axis 13, foreign currency. Both mechanisms were recorded as unable to express one. P04 does not contradict this, but `P08` owns the currency model and P10 has not yet reconciled against it — recorded as `PEER DEPENDENCY OPEN`, `D-13`.

## 8. Open Between P04 and P10

| # | Item | Status |
|---|------|--------|
| `PR-04-01` | Does P04 accept that depreciation is an instance of time-based recognition for kernel purposes, or does it hold depreciation as an asset-internal concern? | `PEER DEPENDENCY OPEN` — P04's package was read for facts, not for a kernel position |
| `PR-04-02` | The reference product's asset object is named for **asset and revenue recognition together** and still carries deferred-revenue commentary. Does P04 read that as history or as a design signal? | `PEER DEPENDENCY OPEN` |
| `PR-04-03` | `P04-B-25` — corporate income tax on disposal gain — **has no owner in the P01–P11 wave**. P10 confirms it is not a P10 item | Recorded; escalated by P04 already |


---

## 9. `P10-F-38` — the accounting significance, settled

`66` Challenge C §3.2 argued both readings and settled it. P10 accepts the settlement.

**The counter-reading** — that a pair netting to zero is the correct representation of a reclassification with no lifetime cost-object effect — **is defeated**, and by a short argument: correct the emission so only the profit-and-loss leg carries the attribution, re-run the arithmetic, and the total is unchanged and correctly phased. **The corrected treatment does not double-count.** So the both-legs shape buys nothing.

**What it costs is the entire time dimension.** The analytic balance is summed over all lines for the account with no general-account or account-type restriction, optionally bounded by dates — and **both legs of a pair carry the same date**. So the netting **survives period bounding**: a period-scoped analytic report shows **zero movement** from the whole deferral machinery. Cumulatively the cost object is right; **by period it is exactly as wrong as it would be with no deferral at all.**

> P10 is a **time-based recognition** process. A defect that preserves the total and destroys the phasing is the defect that matters most here. The earlier phrasing — *"contributes nothing at balance level"* — understates it: the failure is at **period** level, which is the level P10 owns.

**New refinement, verified:** the analytic balance splits debit and credit by the **sign** of the amount before netting, so each pair adds its full amount to **both** sides. A twelve-month deferral inflates a cost object's gross analytic turnover by roughly twice the base plus the sum of the periods while leaving its balance unmoved. **Any control reconciling analytic turnover to ledger turnover breaks; any control reconciling balances passes.**

**And the instance count is three, not two.** The accrual wizard is a **third** mechanism-level implementation of the same idea — it writes an attribution onto the balance-sheet leg — and it fails **differently**: its counterpart distribution is weighted over a denominator that includes lines with nothing to accrue and skips lines with no distribution, so it sums to **less than 100%** and neither matches nor cancels. Independent re-implementation of one wrong idea did not even fail the same way twice.