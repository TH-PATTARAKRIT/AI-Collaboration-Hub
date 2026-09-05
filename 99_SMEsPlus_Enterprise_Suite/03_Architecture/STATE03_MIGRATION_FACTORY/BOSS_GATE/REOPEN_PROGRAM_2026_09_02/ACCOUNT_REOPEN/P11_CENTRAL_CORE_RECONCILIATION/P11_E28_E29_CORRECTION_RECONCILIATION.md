# P11 — C1 · E-28 / E-29 CORRECTION RECONCILIATION

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C01 · Layer 1 clean-room
Baseline `7f701cd` · Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` (continued, not restarted)

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Lineage — both entries stand, neither is rewritten

| Entry | State | Verified this run |
|---|---|---|
| `P11-E-28` — *"the evidence base was chosen by traversal order"* | **PRESERVED UNCHANGED** as the historical error | present at revision log, unedited since `eef2757` |
| `P11-E-29` — *"`P11-E-28` was over-broad; restated"* | **CONTROLLED CORRECTION** | present, cites `E-28` and does not delete it |

**`P11-G-03` satisfied:** the correction carries a visible marker at the point of correction, and the
original is retained above it.

## 2. What `E-29` actually corrected, restated exactly

`E-28` asserted two things. **One is true and one is irrelevant to the claim it was attached to.**

| Assertion in `E-28` | Verdict |
|---|---|
| *"P11 selected by traversal order"* | **TRUE and preserved.** P11 tested the first two dumps a `find` returned |
| *"the largest database was never opened"* | **TRUE and IRRELEVANT.** The claim `E-28` was attached to (`P11-F-09`) is a **readability** claim. Size does not bear on whether an archive opens |

**The material defect** is neither of those: **the ranking/selection unit was never declared**, so the
sample's adequacy was unknowable at the time. Re-verified this run: exactly **two** dump-format versions
exist (`1.14-0`, `1.16-0`); P11 tested one of each; **the sample was complete on the unit the claim
required, by accident rather than by design.**

## 3. Inheritance scan — which P11 findings inherited `E-28`'s over-broad wording

**Declared method.** `POPULATION` = every `.md` in the P11 package. `PATTERN` = literal search for the
over-broad formulations *"largest"*, *"never opened"*, *"traversal order"*, *"smallest"*, and for
citations of `P11-E-28` / `P11-F-11`. `PATH SET` = the package directory. `UNIT` = one occurrence.
Controls run before the scan.

| Artefact | Inherited wording? | Disposition |
|---|---|---|
| `P11_FINAL_BLOCKER_REGISTER.md` `P11-F-11` | **YES** — carried *"the largest dump on this host, 2.4× the next, was never opened"* | **REOPENED and corrected in §4** |
| `ACCOUNTING_BOSS_FINAL_GATE_PACK.md` `D-3b` | **NO** — already superseded to the unit-clause form at `7f701cd` | unchanged |
| `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` `P11-E-28` | **N/A** — it *is* the original | preserved |
| `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` `P11-M-04` | **NO** — states the ordering principle, not the size claim | unchanged |
| `P11-F-09`, `P11-F-10` | **NO** — `F-09` corrected at `P11-E-25`; `F-10` is the bias finding and is unit-aware | unchanged |
| All other findings (`P11-F-01`…`F-08`), all blockers, all tolerance-zero rows | **NO** — none cites `E-28` or its wording | unchanged |

> ### Exactly one finding inherited the over-broad wording: `P11-F-11`. It is reopened here and nowhere else.

## 4. `P11-F-11` — reopened and restated

**As published:** *"The finding applies to P11. The largest database — 2.4× the next — was never
opened."*

**Restated:**

> **`P11-F-11` (v2).** P11 selected its readability sample by **traversal order** and **declared no
> ranking unit**. For the readability claim the sample was **complete on the governing unit**
> (dump-format version: 2 of 2). **The defect is the undeclared unit, not the unopened file** — and it
> is material because the same undeclared selection, applied to a **population** or **configuration**
> claim, would have been wrong, which is exactly what it cost a peer (`P07-F-60`, withdrawn).

**What survives unchanged:** the peer instance, the `D-3b` consequence, and `P11-M-04`. **What is
withdrawn:** the implication that P11's sample was inadequate for the claim it supported.

## 5. Position

| Item | State |
|---|---|
| `P11-E-28` | **PRESERVED — HISTORICAL ERROR, UNCHANGED** |
| `P11-E-29` | **VERIFIED — CONTROLLED CORRECTION** |
| Findings inheriting the over-broad wording | **1** (`P11-F-11`), reopened and restated |
| Findings wrongly reopened | **0** — the scan bounded the blast radius rather than assuming it |
| Errors added by C1 | **0.** No new error; this is a scoped repair of a known one |
