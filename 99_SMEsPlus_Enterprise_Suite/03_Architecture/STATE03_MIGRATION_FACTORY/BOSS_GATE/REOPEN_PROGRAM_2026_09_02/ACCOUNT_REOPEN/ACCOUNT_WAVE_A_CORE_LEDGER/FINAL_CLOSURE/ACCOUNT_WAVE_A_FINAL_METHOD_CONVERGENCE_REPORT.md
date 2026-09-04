# ACCOUNT WAVE A — FINAL METHOD CONVERGENCE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` (`aad8a1e`) · Standard `SMEPLUS-DR-MC-001`

> **Recommendation only. Boss is the sole Final Approver.**
> Figures resolve against `MCC_00_CANONICAL_FIGURES_REGISTER.md`, **except where this file records
> `MCC_00` itself as defective — see §3.**

---

## 1. Panel completion — the precondition

The round instruction §6 forbids marking a finding complete while a panel is still running. **This was
tested mechanically, not assumed.**

| Panel | Session | State | Evidence |
|---|---|---|---|
| Wave A Core / CORR1 / GAPCLOSE / MC / MCC expert + audit panels | `…-CORE`, `…-CORR1`, `…-GAPCLOSE`, `…-MC`, `…-MCC` | **FINISHED** — all committed | commits `f8bc069` … `aad8a1e` |
| **AAS+ Post-Very-Deep Redesign** | **`SMEPLUS-26-09-04-ACCOUNT-WAVE-A-AASR-001`** | **RUNNING when this session began; TERMINAL at 13:56** | see below |

**The AAS+ panel was live during this session's first 12 minutes.** Observed directly:

| Time | Observation |
|---|---|
| 13:44 | 20 files modified within the preceding 4 minutes |
| 13:44 | `18_ACCOUNT_WAVE_A_INDEPENDENT_DESIGN_VETO_REPORT.md` **appears mid-session** |
| 13:52–13:56 | `19_…PROVISIONAL_SYNTHESIS_REPORT.md`, `21_…EVIDENCE_MANIFEST_SHA256.md` written |
| 13:56 → 14:01 | **zero writes**; package closes at **24 files** with a manifest and a declared terminal state |

**Terminal state returned by that panel** (its own words, quoted as data, not adopted as a finding):

> `ACCOUNT WAVE A — PROVISIONAL PARALLEL SYNTHESIS · AAS+ OUTPUT IS NOT CANONICAL`
> `AWAITING PARENT CONVERGENCE, REGISTER CLOSURE AND DELTA REVALIDATION`

with `AASR-VETO-01` **upheld** against its own dependency register.

> **Consequence for this report.** The precondition is now **met** — but it was **not met when this
> session started**, and the panel's result is *itself* a non-convergence signal: an independent
> downstream consumer of the Wave A evidence base **could not use it** and said so.

### `FC-P1` — the AAS+ panel independently reproduced `GB-06`

Its `V-SYS-2` records that a package *"consumed the parent's findings but not the parent's
**corrections** to them"* — missing `CORR1/C04` (`NC-01`…`NC-24`, 11 claims class `E`) and `MCC_G §8`
(`G-C1`…`G-C8`). **A second, independent session, on a different task, hit the same failure mode
`GB-06` names.** This is corroboration of `GB-06`, obtained without asking for it.

---

## 2. Fixed-point criteria

| Criterion | Parent (`MCC`) | **This round** | Movement |
|---|---|---|---|
| Two consecutive independent passes return **no** material delta | `NOT MET` | **`NOT MET`** | This round returned **4 new material findings** (`FC-F1`…`FC-F4`) plus 3 claim corrections (`FC-C1`, `FC-C2`, `FC-A1`) |
| The bounding denominator is stable between passes | `NOT MET` | **`NOT MET`, and worse** | §5 |
| Independent reviewers reach the same disposition | `PARTIALLY MET` | **`PARTIALLY MET`** | `MCU-04` re-verified to the **same** disposition `MCC_00` reached; but by a **different route**, and it found `MCC_00` defective on the way |
| The package can carry its own corrections | `NOT MET` | **`NOT MET`** | `FC-F1` — the mechanism built to fix this failed on first use |

> # **FIXED POINT: `NOT REACHED`.**
> Three consecutive rounds — `MC`, `MCC`, `FC` — each returned material new findings on first
> independent contact. **The rate of new findings is not decaying.**

---

## 3. `MCC_00` — the governing register is internally inconsistent

> ### `FC-F1` — `VERIFIED DEFECT` in the canonical figures register.

| Section | What it says |
|---|---|
| `MCC_00` §2 dispositions | Closes **`MCU-15`** *and* **`MCU-04`**, both beyond `MCC_D` §3's eight |
| `MCC_00` §1 counts | *"Gating unknowns closed by this round: **9**"* · *"**9 of 17 (52.9%)**"* |

Derivation, stated so it can be checked:

```
MCC_D §3 closures                                   = 8   (MCU-05,06,07,08,09,10,13,14)
+ MCC_00 §2 closes MCU-15                           = 9
+ MCC_00 §2 closes MCU-04                           = 10
MCC_00 §1 publishes                                 = 9      ← off by one
```

**Correct value on the evidence: `10 of 17` closed (58.8%); `7` inherited unknowns remaining.**

**`MCC_00` governs by rule and this file does not overwrite it.** The correction is carried to Boss as
an open item. **This is `GB-06`'s fourth consecutive instance**, and the most damaging of the four,
because it is inside the mechanism created to end the other three:

| # | Instance | Round |
|---|---|---|
| 1 | Correction channel absent | inherited (`MCU-17`) |
| 2 | `J-16` — `MCU-15`'s closure propagated to 2 files of 5, in the round that specified the rule | `MCC` |
| 3 | **`FC-F1` — `MCC_00`'s own §1 and §2 disagree** | **`MCC`, found by `FC`** |
| 4 | `V-SYS-2` — a sibling session consumed findings but not corrections | `AASR`, independent |

---

## 4. `MC-01` … `MC-10` — final status

| Test | `MC` | `MCC` | **`FC` FINAL** | Basis |
|---|---|---|---|---|
| `MC-01` Population Boundedness | `NOT MET` | `NOT MET` | **`NOT MET`** | `FC-F4` — the **root set** was never enumerated. 1 root of **22** |
| `MC-02` Systematic Enumeration | `PARTIALLY` | `PARTIALLY` | **`PARTIALLY MET`** | Method is sound and reproduced the parent's own figure exactly (§5); the *scope* it was applied to was not |
| `MC-03` Independent Delta | `NOT MET` | `NOT MET` | **`NOT MET`** | 4 new material findings on first independent contact |
| `MC-04` Repeatability | `PARTIALLY` | `PARTIALLY` | **`MET`** ▲ | **The only criterion that improves.** §5 |
| `MC-05` Negative Claim Compliance | `NOT MET` | `NOT MET` | **`NOT MET`** | Every class `A` absence in the programme is bounded to ≤1 of 22 roots |
| `MC-06` Unknown Classification | `MET` → `NOT MET` | `NOT MET` | **`NOT MET`** | `FC-F1` — the register that classifies them miscounts them |
| `MC-07` Contradiction Closure | `NOT MET` | `NOT MET` | **`NOT MET`** | `FC-F1`, and `V-SYS-2` independently |
| `MC-08` Tolerance-Zero Closure | `NOT MET` | `NOT MET` (7→12) | **`NOT MET`** | **12 boundaries, 0 resolved.** No new boundary opened by this round |
| `MC-09` Evidence Lineage | `PARTIALLY` ▲ | `PARTIALLY` | **`PARTIALLY MET`** | Lineage is complete and machine-checkable; `MCC_L`'s *"prompt NOT COMMITTED"* is contradicted (§6) |
| `MC-10` New-Finding Delta | `NOT MET` | `NOT MET` | **`NOT MET`** | Not close |

> ### **7 not met · 2 partially met · 1 met.** Parent: 8 / 2 / 0.
>
> **One criterion moved up. None moved down. The aggregate did not converge.**

---

## 5. Denominator stability — the decisive section

### 5.1 The method was validated before it was used

Before extending the path set, this round applied **its own** manifest-counting method to the **parent
round's own declared root**:

| | Modules |
|---|---|
| `MCC_B` §3.2 declared: `addons/` **791** + `addons_archive/` **961** | **1,752** |
| This round counted at `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo` | **1,753** (= 1,752 + the root manifest) |

> **The two counts agree exactly.** `MC-04` Repeatability is therefore **`MET`** — the first `MET` in
> the programme's convergence history. What follows is a change of **path set**, not of method, and
> that distinction is what makes it citable.

### 5.2 The root set was never a denominator

Declared pattern: *every directory on the evidence volume containing
`addons/base/models/res_currency.py`.*

| Measure | Parent declared | **Discovered** |
|---|---|---|
| Reference core **roots** | **1** (implicitly) | **22** |
| Manifested modules in scope | **1,753** | **23,530 raw** across 22 roots |
| Trees inside the declared root | 3 (`addons/`, `addons_archive/`, core) | — |

> ### `FC-F4` — `GB-07` is confirmed and widened at the level above the one it was corrected at.
>
> The parent's lesson was: *"declare the pattern **AND prove the path set** — the proof of a path set is
> an enumeration of the source root, not a habit."* It applied that **inside** one root. **The choice of
> root remained a habit.** The correction moved the defect up one level; it did not remove it.
>
> **`MC-01` cannot be met until the path set is declared at programme level, once, over the root set.**

**Bound, stated:** 22 is the yield of **one** declared pattern. A core root that omits or relocates that
file is not discovered by it. **Class `A` over a declared pattern — not a proof that 22 is the total.**

### 5.3 The unit problem persists and is large

Over the six roots enumerated in detail: **9,457 raw** manifested modules resolve to **1,773 distinct
module names**. **81% of the raw count is duplicate copies.** The parent round identified `UNIT` as the
missing fourth element of a denominator; this quantifies how much it moves the answer.

---

## 6. Evidence lineage — one parent claim contradicted

`MCC_L_PUBLICATION_STATUS.md` §2 records:

> *"Prompt commit — **NOT COMMITTED.** The parent round committed its prompt (`56288c4`); this round's
> prompt was delivered in session and is **not** in the tree."*

**`CONTRADICTED.`** `git fetch` + `git log` over `origin/research/account-wave-a-mc-2026-09-04-001`:

| Commit | Content |
|---|---|
| `c32a924` | `account: add very-deep targeted method convergence closure prompt` — **the `MCC` prompt, 753 lines** |
| `c6aa32b` | `account: add AAS+ post-very-deep redesign prompt` — 459 lines |
| `b6cc260` | `account: add Wave A final closure and Wave B readiness prompt` — **this round's prompt**, 317 lines |

The `MCC` prompt **was** committed — to the **`mc`** branch on `origin`, not to the `mcc` branch. The
parent checked `git log` over **its own branch** and concluded absence. **This is the negative-claim
defect in miniature: a bounded search reported as an unbounded absence.**

> ### `FC-F5` — recorded as a lineage correction, non-material to any accounting finding.
> It is material to **`ER-CORE`**: the same failure mode appeared in a governance claim, where nobody
> was looking for it.

---

## 7. New material deltas returned by this round

| id | Finding | Class | Severity |
|---|---|---|---|
| `FC-F1` | `MCC_00` §1 and §2 disagree by one closure | **`VERIFIED DEFECT`** in the governing register | **HIGH** — `GB-06`, 4th instance |
| `FC-F2` | Wave A rate research bound to a root where `Δ1` is **absent**, while `18.0.3_smeplus` has it **present** | **`VERIFIED FACT`** | **HIGH** — bounds every rate behavioural conclusion |
| `FC-F3` | `GB-08` understated: `Δ1` present in **5 of 22** roots, not one | **`VERIFIED FACT`** | **MEDIUM-HIGH** |
| `FC-F4` | Root set never enumerated: 1 of 22; 1,753 of 23,530 | **`VERIFIED FACT`** | **HIGH** — `GB-07`, `MC-01` |
| `FC-F5` | `MCC_L`'s *"prompt not committed"* is contradicted | **`CONTRADICTED`** | LOW material, HIGH methodological |
| `FC-C1` | `J-11` *"arbitrary server-side code"* — overstated | **CORRECTION** | LOW |
| `FC-C2` | `J-11` ordinary-user grant is not an escalation | **CORRECTION** | LOW |
| `FC-A1` | `MCU-04` amplified: the created `ir.ui.menu` has **no company field and no record rule** | **`VERIFIED DEFECT`**, widening | **MEDIUM** |

**New tolerance-zero boundaries opened: `0`.** First round in the programme's history to open none.

---

## 8. New material finding classes

**One.** `FC-F1` — *"a defect **inside** a correction mechanism, undetected by the round that shipped
it."* The prior taxonomy had *balanced-but-wrong* (the ledger reconciles and is wrong) and
*declared-but-inert* (`T0-09`, a control a reader sees and the machine does not). This is a third:
**a control that executes, is read, and is itself wrong.** `MCC_00` was read by every consumer in the
package and by the AAS+ panel; none checked it against itself.

---

## 9. Negative-claim compliance

See `ACCOUNT_WAVE_A_FINAL_NEGATIVE_CLAIM_COMPLIANCE.md`. Summary: **`MC-05` `NOT MET`**, and the reason
changed. It is no longer *"58.1% of the package unscanned"*; it is that **every class `A — VERIFIED
ABSENCE` in the programme is bounded to at most one root of 22**, and none says so.

---

## 10. Balanced-but-wrong taxonomy

**Unchanged by this round.** Floor **32** under `MCC_G` §1's own four-question test; **36** asserted;
**19 of 19** classes searched. No case added, none withdrawn. `T0-12` (`unbalanced-and-posted`) still
has **no cell** in the taxonomy. See `ACCOUNT_WAVE_A_FINAL_BALANCED_BUT_WRONG_REGISTER.md`.

---

## 11. Reviewer repeatability

| Measure | Result |
|---|---|
| Parent findings re-tested from primary source this round | **6** — `J-10`(class), `J-11`, `J-14`, `MCU-06`, `MCU-20`/`BW-31`, `GB-08` `Δ1` |
| Reproduced **exactly** | **5** |
| Reproduced with **correction** | **1** — `J-11` (`FC-C1`, `FC-C2` overstated; `FC-A1` understated) |
| Parent **counts** independently reproduced | **1 of 1** (§5.1) |

> **Reviewer repeatability is high and improving. It is method *scope* that fails, not method
> *execution*.** That distinction is the single most useful output of this round for the other modules.

---

## 12. The exact remaining enumeration defect

The instruction requires naming the defect rather than opening another broad round. **One defect, stated
once:**

> # The programme has never declared its **root set**.
>
> Every denominator, every path set and every class `A` absence in Wave A is scoped to **one reference
> core root of the 22 that exist**, and **no artefact says which root, or that a choice was made.**
>
> **Cost to close: hours, mechanical, no new research.** Declare the root set once, at programme level;
> state which root SMEsPlus targets; re-scope the existing class `A` absences to it; re-run the
> **bounded** patterns — they are already written — over the declared set.
>
> **This is not a reason to reopen Wave A research. It is a defined, cheap, schedulable task**, and it
> is the last thing standing between the method and `MC-01`.

---

## 13. Terminal state

> ## `ACCOUNT WAVE A — METHOD NOT CONVERGED`
> ## `ONE EXACT REMAINING ENUMERATION DEFECT: THE ROOT SET IS UNDECLARED`

**Not declared:** converged · final approved · Wave A closed · any gate movement · any implementation
authorisation.
