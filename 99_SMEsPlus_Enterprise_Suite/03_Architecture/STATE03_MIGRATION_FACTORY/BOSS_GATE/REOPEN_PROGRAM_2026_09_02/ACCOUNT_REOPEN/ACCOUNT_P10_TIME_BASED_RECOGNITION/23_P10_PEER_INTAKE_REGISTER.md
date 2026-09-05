# P10 — PEER INTAKE REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001` (continuation of `…-REV2-001`) · Layer 1
Governing discipline: **verify before adopting; refine a peer's route rather than inherit it; correct a peer's record when their package will otherwise carry the error.**

---

## 0. Correction `P10-R-09` — the process taxonomy was mis-assigned in the parent package

The parent package's `10_P10_CROSS_PROCESS_OWNERSHIP.md` repeatedly names **`P04` as "A2R (the ledger)"** and routes the ledger, period close, lock dates, the fiscal calendar and FX policy to it.

That is wrong. Verified against the peer branch set actually published:

| Process | What it actually is | What the parent package assumed |
|---------|---------------------|---------------------------------|
| `P04` | **Acquire-to-Retire** — the fixed-asset lifecycle, including depreciation | "the ledger" |
| `P08` | **Record-to-Report** — the general ledger, journal posting, period close, currency, reporting | not addressed at all |
| `P09` | **Plan-to-Analyze** — management accounting, analytic, budget | not addressed at all |

Consequence: every dependency the parent routed to `P04` as ledger-owner (`X-04`, `X-05`, `X-06`, and obligations `Y-01`, `Y-02`) was addressed to the wrong process, and the two processes that P10 overlaps most — the asset process, which runs a competing recognition engine, and the analytic process, which carries recognition attribution — were not addressed at all. The dependency register is restated in `37`.

**Found by:** this continuation, on enumerating the peer branch set. Not by the parent's four challenges — none was scoped at the process taxonomy.

Compounding fact from `P11`: **`P11-F-04` — the `P01`–`P11` process taxonomy does not exist in the canonical repository.** The parent package inferred it from folder names. A taxonomy that is not written down is not a denominator; that is why the inference failed. Recorded as `P10-U-19`.

## 1. What Was Taken In

| # | From | Item | P10 action | Verification performed by P10 |
|---|------|------|-----------|-------------------------------|
| `IN-01` | `P04` `1636df4` | Locked-period entries are **silently re-dated, not refused**, in the accounting core's generic posting routine, so it hits every programmatic post product-wide — *"deferred recognition too"* | **ADOPTED and UPGRADED** | Yes — see `IN-02` |
| `IN-02` | `P04` | Positive control: an asset test asserts a charge scheduled `2020-12-31` posting as `2021-07-31` under a `2021-06-30` fiscal-year lock | **ADOPTED after independent re-read of the test body** | **Verified line by line.** The assertion is exactly as P04 states |
| `IN-03` | `P04` / `P11` `T0-13` | A financial effect may not cross a scope boundary silently; close condition **refuse OR record an attributable trace**; widened by `P04-F-68` to need no tenant boundary and no hierarchy — a single company suffices | **ADOPTED**, and it **changes P10's veto** — see `32` | Verified that the widening applies to P10: P10's own worst scenario is single-company |
| `IN-04` | `P04` / `P09` `9a3bded` | Depreciation writes the analytic allocation onto **both** rows of the entry with opposite-signed amounts and no account-type filter, so the two management records are mirror images that **net to zero**; mandatory-plan validation is restricted to product-type rows so programmatic posts skip it | **ADOPTED as a mechanism, then INDEPENDENTLY RE-DERIVED for P10's own mechanism** — see `P10-F-38` | **Verified from P10's own primary source.** The deferral generator has the identical shape |
| `IN-05` | `P08` `4bdf8a2` | **No accounting-event object exists** in any of the 22 declared roots, so `ONE FACT → ONE ACCOUNTING EFFECT` is unenforceable | **ADOPTED — and it relocates P10's central design element.** See `27` | Consistent with P10's own independent finding of no recognition-event identity, at a different layer |
| `IN-06` | `P08` | **Closing a period is moving a date**; the irrevocable lock **relocates rather than refuses** on the posting path, and the product's own test asserts a full annual charge crossing a fiscal year | **ADOPTED** | Same positive control as `IN-02`, reached independently by two processes |
| `IN-07` | `P08` | A posted journal item is editable in place; the double-entry balance invariant is a caller-supplied request parameter with no database-level enforcement in 22 of 22 roots | **ADOPTED as context**, not load-bearing for P10 | Not re-derived — carried as peer-supplied |
| `IN-08` | `P09` `16f884f` | An analytic plan has **no company field at all** — plans are database-global; the allocation payload is absent from every lock-date list, every integrity-hash list and the tracked-field set | **ADOPTED** | Not re-derived — carried as peer-supplied, class `B` |
| `IN-09` | `P09` `MA-11` | *A company-scoped attribution requirement shall never be enforced through a tenant-scoped structure* | **ADOPTED as a P10 design constraint** | Position, not a fact — adopted as such |
| `IN-10` | `P11` `SCP-08` | The semantics of an absent scope value must be defined; **"unset" may never mean "all"** | **ADOPTED into `33`** | Position |
| `IN-11` | `P11` `SCP-09` | A scope determination taken against behaviour the programme is obliged to change must record its **expiry trigger** | **ADOPTED into `33`** — P10 had no expiry triggers at all | Position |
| `IN-12` | `P11` `D-5` | *The accounting-event identity* is already a named Boss decision | **ADOPTED — P10 withdraws a competing decision and feeds `D-5` instead.** See `27` §5 | Verified that `D-5` and P10's event-identity question are the same question at two layers |
| `IN-13` | `P11` `P11-F-04` | The process taxonomy does not exist in the canonical repository | **ADOPTED** — it explains `P10-R-09` | Confirmed by P10's own failure |
| `IN-14` | `P08` | The root-set defect was closed for **only 3 of ~23** class-`A` claims; the rest must be read as class `C` | **ADOPTED AS AN INTAKE CONSTRAINT** | This is why `IN-07` and `IN-08` are carried as peer-supplied and are not used as sole support for any P10 gate movement |

## 2. What P10 Refused to Inherit

| # | Item | Why refused |
|---|------|-------------|
| `RF-01` | P08's class-`A` claims outside the 3 whose root set was re-run | Their own package says the rest are class `C` until re-run. Adopting them as `A` would be the restatement-upgrade the negative-claim standard prohibits |
| `RF-02` | P11's synthesis conclusions | P11's own terminal state records that it reconciled against **0 of 10** peer packages at synthesis. Its *positions* (`SCP-08`, `SCP-09`, `T0-13`, `D-5`) are adopted; its *reconciliation* is not, because P10 was not among its inputs |
| `RF-03` | Any peer's count of anything | The programme has now had counts corrected in at least four processes on unit-versus-population grounds. P10 cites peer counts only with the peer's own unit attached |

## 3. What P10 Returns to Peers

| # | To | Item |
|---|-----|------|
| `OUT-01` | `P08` | `P10-F-38`: the attribution nets-to-zero defect P04 found in depreciation is **also present in deferred recognition**, by the same mechanism, verified from P10's own source. It is therefore not an asset defect — it is a property of every programmatic recognition post, and P08 owns the posting layer |
| `OUT-02` | `P09` | The same, addressed to the analytic owner: **two** recognition mechanisms are now confirmed to produce mirror-image attribution that nets to zero. P09's eleven-defect root cause gains a second confirming instance |
| `OUT-03` | `P08` | `P10-F-40`: the **untested** path is the live one. The lock refusal is covered by an executed test on the grouped generation path, which **zero deployed companies use**; the silent re-date on the validation path — which **all 44 deployed companies use** — has no test |
| `OUT-04` | `P04` | P10 confirms `P04-B-31` from a second, independent mechanism, and supplies the deployment fact that makes it live rather than theoretical |
| `OUT-05` | `P11` | P10's event-identity forensic (`27`) as input to `D-5`, and P10's three-option classification of the period-versus-posting-date question (`28`) as input to `D-12`/`T0-13` |
| `OUT-06` | `P04`, `P08`, `P09`, `P11` | Correction `P10-R-09`: the parent P10 package mis-assigned the process taxonomy and addressed ledger obligations to the asset process. Any peer that ingested the parent's `10_P10_CROSS_PROCESS_OWNERSHIP.md` should re-read it against `37` |

## 4. Intake Integrity Statement

Of 14 items taken in, **4 were independently re-verified by P10 against primary source** (`IN-02`, `IN-03`, `IN-04`, `IN-12`), **4 are adopted positions** rather than facts (`IN-09`, `IN-10`, `IN-11`, and the `T0-13` close condition), and **6 are carried as peer-supplied, class `B`**, and are never the sole support for a P10 gate movement.

One item — `IN-04` — was not merely adopted: P10 re-derived the same mechanism in its own domain from its own source and produced a **new finding the peer could not have produced**, because the peer was not looking at the deferral generator. That is the intake discipline working as intended, and it is the only new defect this continuation found.
