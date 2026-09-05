# P10 — LOCKED-PERIOD RECOGNITION AND CORRECTION BEHAVIOUR

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` · Layer 1

---

## 1. The Positive Control

The parent package carried the silent re-date as a source-verified inference. It is now carried as **verified against the product's own executed specification**, supplied by `P04` and re-read line by line by P10:

> With a fiscal-year lock at mid-2021, an asset charge scheduled for the last day of **2020** posts, on validation, dated the last day of **July 2021**. The test asserts this as the expected result.

This satisfies the programme's standing rule that an evidence claim needs a **positive control** — a case where the mechanism demonstrably fires. It also settles the status question: the behaviour is **specified**, not accidental.

The second-order reading is the damaging one: in that same assertion, the 2020 charge and the 2021 charge both land in fiscal 2021. **One fiscal year shows nothing and the next shows double, and the vendor's own suite asserts it as correct.**

## 2. Test Coverage — the inversion

| Path | Lock behaviour | Executed test? | Deployed usage |
|------|----------------|----------------|----------------|
| Grouped generation | **Refuses**, with an explicit error | **Yes** — a dedicated test asserts the refusal | **Zero of 44 companies** |
| Validation generation | **Silently re-dates** via the shared posting layer | **CORRECTED, `34` `W-33`.** A test *does* exercise generation into a locked period on this path — it asserts the entry **count** and **nothing about the resulting dates** | All 44 companies **in each of the two databases first examined** — but see the lock row below |
| Asset board | Silently re-dates | **Yes** — and the test asserts the re-dating as correct | n/a to P10 |
| Asset disposal | **Hard-refuses** | Present | n/a to P10 |

`P10-F-40`, **restated after `34` `W-33` — and the restatement is stronger than the original**:

> The vendor's suite **runs the live path under a lock and declines to assert where the money lands.** The refusal behaviour, used by no deployed company, has a test asserting its outcome. The re-dating behaviour, which every deployed company is configured for, has a test that exercises it and asserts only how many entries appear.

The original wording — "no test at all", "no evidence whatsoever" — was over-broad and is withdrawn.

**And the exposure claim is corrected, `34` `W-11`.** A lock violation requires a lock. P10 verified the company table of all four deployed archives: **three carry no lock date on any company (44 + 44 + 1); the fourth carries four.** So the re-date cannot fire in the three databases P10 used to argue live exposure, and can fire only in the one P10 had wrongly excluded.

## 3. Correction Behaviour — reconciled across mechanisms

| | Deferral, validation path | Deferral, grouped path | Asset | Loan |
|---|---|---|---|---|
| In-flight modification | None — only teardown of the source document | n/a — regenerated each run | Pause, resume, revalue, change duration, dispose | Reset and re-confirm |
| Catch-up | **None** | **Structural** — cumulative from an unbounded earliest date, so a wrong or skipped period is absorbed by the next run | A **stub entry cut at the modification date**, then prospective re-derivation | Full re-derivation |
| What stands | Nothing is guaranteed to stand | Everything stands; the position is restated | Posted entries stand | Nothing stands |
| Locked-period interaction | Teardown reverses rather than deletes, and the **reversal is re-dated into a different month from the entry it reverses** | Refuses | Guards on mutation and disposal | None of its own |

Two consequences P10 records:

1. **The most correction-resilient behaviour is on the path nobody uses.** The cumulative grouped model self-heals; the validation model cannot correct at all without disturbing closed periods. The deployed estate runs the fragile one.
2. **A corrective reversal can land in a different period from the entry it corrects.** So a correction made under a lock does not restore the period it was meant to fix — it books the reversal somewhere else. This compounds §1: the original was mis-periodised silently, and the correction is mis-periodised silently too.

## 4. Reopen

No mechanism re-derives suppressed or re-dated recognition when a period is reopened (class `A`, scope = the module set searched in the parent round). Combined with §1, the misstatement is **permanent in the direction that matters**: reopening the period does not put the amount back.

One aggravating interaction, carried from the parent round at class `B`: an entry whose date was moved out of its period is no longer matched by the already-generated detector for that period, so the grouped generator could regenerate it once the period reopens.

## 5. Scope Determination

| Question | Answer |
|----------|--------|
| Who owns the constraint? | `P08` — it is the posting layer's lock |
| Who owns the semantic being damaged? | `P10` — the recognition period |
| Who owns the object that would carry the fix? | `P08`, via obligation `OB-02`; and `P08`/`D-5` for the event itself |
| Which scope is the effect in? | **COMPANY.** `P04-F-68` established that no tenant boundary and no company hierarchy is needed — a single company suffices |

## 6. Status

The behaviour is **fully characterised**. Nothing further can be learned about it from source. What remains is a decision (`28`) and a ledger change (`OB-02`/`OB-03`), both outside P10's authority.

One item of evidence is still obtainable and has not been obtained: whether any entry in the deployed archives actually carries a date inconsistent with its schedule. Recorded as `P10-U-20`, `ROUTED`.
