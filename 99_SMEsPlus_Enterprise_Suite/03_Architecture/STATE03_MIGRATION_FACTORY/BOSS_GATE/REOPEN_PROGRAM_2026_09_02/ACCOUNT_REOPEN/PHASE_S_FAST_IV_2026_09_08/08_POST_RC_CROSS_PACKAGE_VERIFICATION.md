# 08 — POST-RC CROSS-PACKAGE VERIFICATION

**Precondition for this section (prompt §13):** *"After all required RCs have terminal states…"*
All six RCs have a terminal state — **`RC-HOLD`, six of six**. The section is therefore entered, but
**every sweep whose input is an RC result is unreachable**, because there are no RC results. Those
are recorded `NOT REACHABLE`, not `CLEAN`. `[[smeplus-deep-research-negative-claim-standard]]`:
**NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST**, and a sweep not run is not a sweep that passed.

## 1. Sweeps executed, each with a control capable of failing

### 1.1 Moving-head substitution — **EXECUTED, 6 of 6 clean**

Prompt §6 requires that *"no moving `origin/<branch>` head silently substitutes for a declared pin."*
Tested for every frozen ref, not only `RC-02`'s.

| Frozen pin | Declared branch | Verdict |
|---|---|---|
| `2079a25` | `corr/p09-phase-s-final-2026-09-07-001` | **HEAD == PIN** |
| `9d4ecdc` | `corr/p11-phase-s-remediation-2026-09-07-001` | **HEAD == PIN** |
| `692ea27` | `corr/p06-iev-phase-s-final-2026-09-07-001` | **HEAD == PIN** |
| `b5f5a21` | `corr/p06-source-phase-s-final-2026-09-07-001` | **HEAD == PIN** |
| `e368d11` | `corr/p08-phase-s-rc05-prep-2026-09-07-001` | **HEAD == PIN** |
| `d685176` | `corr/p08-iev-phase-s-final-2026-09-07-001` | **HEAD == PIN** |

**Both failure limbs were proved reachable before the result was believed** — a check whose failure
branch cannot fire returns a clean verdict on every input (`[[smeplus-control-that-cannot-detect-its-failure]]`):

| Limb | Control input | Fired? |
|---|---|---|
| `PIN NOT ON BRANCH` | `6cb9946` against `origin/SMEsPlus` | **YES** — correctly reports not-an-ancestor |
| `PIN is ANCESTOR of head (head MOVED)` | `0941161^` = `2e2b8de` against the remediation branch | **YES** — correctly reports the head has moved past it |

**This is a verifier-side integrity result about pin stability. It is not `RC-02` evidence** — the
`RC-02` requirement is that the *instrument consumes* its pins, which is a different claim and
**was not tested** (`02_` §2).

### 1.2 P07 read-only closure impact — **EXECUTED, unmoved**

`research/account-p07-th-tax-compliance-2026-09-04-001` head =
`ee2be30ebf155e241510b3c7133c69419eb060a0`, identical to the value recorded by the prior verifier
lineage on 2026-09-07. **P07 has not moved and no P07 mutation has become necessary.**
`PHASE S HOLD — P07 OWNER ACTION REQUIRED` is **NOT** raised.

## 2. Sweeps not reachable, with the exact reason

| Prompt §13 sweep | State | Reason |
|---|---|---|
| superseded/withdrawn claims still consumed as current | **NOT REACHABLE** | the authoritative withdrawal set is `RC-06`'s `F-02` output; `RC-06` not run |
| stale SHA / currentness references | **PARTIAL** — §1.1 covers pin stability only; the in-document currentness sweep is `RC-02`'s `CO-F-01` limb, not run |
| handoff sent vs handoff actually received | **NOT REACHABLE** | `RC-06` limb, not run |
| duplicate root defects vs manifestations | **NOT REACHABLE** | requires terminal RC findings |
| contradiction propagation (incl. `:45` vs `:54`) | **NOT REACHABLE** | `RC-04` not run; the contradiction is declared-open by design at `b5f5a21` |
| P07 read-only closure impact | **EXECUTED** | §1.2 |
| Veto lifting dependencies | **PREPARED, NOT TESTED** | `09_` |
| Boss-only decision dependencies | **EXECUTED** | `11_` §3 |
| `P11-E-49`-shaped manifest defect sweep | **NOT REACHABLE, AND REGISTERED AS A STANDING LEAD** | handoff §3 offers it as *"not swept here — outside the remit"*; it is outside this session's remit too, and it is now **outside two remits in a row**, which is how a lead becomes invisible |

## 3. One observation the sweeps did surface

**`P11-E-49` has now been deferred by three consecutive sessions** — the remediation session
(*"outside the remit"*), the 2026-09-07 verifier lineage, and this one. Prompt §6 permits preserving
it *"as a registered lead unless the Phase S closure criteria require a bounded cross-package
sweep."* Closure criterion 3 (*no material evidence-integrity defect remains unbounded or
unclassified*) is the criterion that would require it. **It is registered, not swept, and
`10_` records criterion 3 as FALSE partly on that basis** — so the deferral is visible in the closure
test rather than resolved by silence.
