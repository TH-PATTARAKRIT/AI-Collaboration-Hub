# ACCOUNT WAVE A — FINAL GATING UNKNOWN REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Layer 1 clean-room
Supersedes nothing. Reconciles `MCC_D` §2/§3/§5/§8 and `MCC_00` §1/§2.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The arithmetic, reconciled

`MCC_D` §8 restates the round's result. That restatement is **internally coherent** and reproduces to
17:

| Line | Count |
|---|---|
| `CLOSED` this round | **9** (8 from §3, + `MCU-15` from §8) |
| `REMAINS GATING` from the inherited 17 | **8** |
| Reclassified **into** gating by the adversarial pass | **+4** |
| Reverted to `UNKNOWN` from out-of-scope | **+2** |
| New gating from the fixed-point passes | **+3** |
| **Standing gating total** | **8 + 4 + 2 + 3 = 17** ✓ |

**`MCC_00` §2 then closes a tenth id — `MCU-04` — and no count was re-derived.** Applying that closure
through the same arithmetic:

| Line | Corrected |
|---|---|
| `CLOSED` this round | **10** |
| `REMAINS GATING` from the inherited 17 | **7** |
| +4, +2, +3 | unchanged |
| **Standing gating total** | **7 + 4 + 2 + 3 = `16`** |

> ### `FC-F1` — three published figures are affected, not one.
>
> | Figure | `MCC_00` publishes | **Corrected** |
> |---|---|---|
> | Gating unknowns closed by the `MCC` round | `9` | **`10`** |
> | Closed as a proportion | `9 of 17 (52.9%)` | **`10 of 17 (58.8%)`** |
> | **Standing gating total** | **`17`** | **`16`** |
>
> **`MCC_00` governs by rule. This file does not overwrite it.** The correction is carried to Boss as
> an open item — see `ACCOUNT_WAVE_A_FINAL_RESEARCH_GATE_REPORT.md`.
>
> The `MCC` round's own comment on the figure 17 — *"the number returning to its starting value is a
> coincidence and is reported as one"* — is **no longer true of the corrected figure. It is 16.**
> The coincidence was an artefact of the miscount.

---

## 2. Inherited set — final disposition of all 17

| id | Subject | `MCC_D` §2 | **FC FINAL** |
|---|---|---|---|
| `MCU-01` | Runtime behaviour never executed against a live instance | `REMAINS GATING` | **`REMAINS GATING — HOLD`** · needs an executed test |
| `MCU-02` | Ledger identity — Boss design decision | `REMAINS GATING` | **`REMAINS GATING — BOSS DECISION`** · `GB-01`-class; no research closes it |
| `MCU-03` | (as `MCU-02` class) | `REMAINS GATING` | **`REMAINS GATING — BOSS DECISION`** |
| **`MCU-04`** | **Report definitions carry no company dimension** | `REMAINS GATING` | **`CLOSED — VERIFIED DEFECT`** · re-verified from primary source this round · `ACCOUNT_WAVE_A_MCU04_FINAL_DISPOSITION.md` |
| `MCU-05` | The lost tolerance-zero candidate (= `T0-07`) | `CLOSED — VERIFIED` | **`CLOSED — VERIFIED`** (unknown answered; `T0-07` unresolved) |
| `MCU-06` | Rate precedence: null vs own-company rows | `CLOSED — VERIFIED` | **`CLOSED — VERIFIED`** · reproduced this round at `models.py` order-rendering |
| `MCU-07` | Demo/seed rate rows | `CLOSED — VERIFIED` | **`CLOSED — VERIFIED`** on the `MCC_D` §7.1-corrected mechanism |
| `MCU-08` | Scope of a finding | `CLOSED — RESCOPED NON-GATING` | **`CLOSED — RESCOPED NON-GATING`** |
| `MCU-09` | — | `CLOSED — VERIFIED SAFE` | **`CLOSED — VERIFIED SAFE`** · rests on one round's evidence only; stated so |
| `MCU-10` | Lock-exception cross-company path | `CLOSED — VERIFIED DEFECT` | **`CLOSED — VERIFIED DEFECT`** → `T0-10` |
| **`MCU-11`** | **Caller-supplied company on a conversion endpoint, no access check, par on denial** | `REMAINS GATING` | **`REMAINS GATING — HOLD`** · **NOT closed by `MCU-04`.** Different mechanism; the merge aggregated symptom, not mechanism |
| `MCU-12` | Negative-claim control never applied to 58.1% of the package | `REMAINS GATING` | **`REMAINS GATING — HOLD`** · reason **restated**, see `…FINAL_NEGATIVE_CLAIM_COMPLIANCE.md` |
| `MCU-13` | `FX-08` targeted re-verification | `CLOSED — VERIFIED` | **`CLOSED — VERIFIED`** · `FX-08` → `PARTIALLY VERIFIED` |
| `MCU-14` | Wrong opening provenance | `CLOSED — VERIFIED DEFECT` | **`CLOSED — VERIFIED DEFECT`** (`BW-30`) on the §7.1-corrected mechanism (the **date**, not the company) |
| `MCU-15` | Wrong reversal lineage | `REMAINS GATING` → §8 `CLOSED` | **`CLOSED — VERIFIED DEFECT`** (`BW-35`) |
| `MCU-16` | Exposure surface 192 sites, 9 assessed (= `GB-04`) | `REMAINS GATING` | **`REMAINS GATING — HOLD`** · **and the bound must now be restated over the 22-root set, not the corrected tree** |
| `MCU-17` | No correction-propagation channel | `REMAINS GATING` | **`REMAINS GATING — HOLD`** · **and it got worse.** `FC-F1` and `V-SYS-2` are two further instances |

**Inherited: 10 closed · 7 remaining.**

---

## 3. Opened by the `MCC` round

| id | Unknown | Class | **FC FINAL** |
|---|---|---|---|
| `MCU-18` | Is the archive module tree on the deployment's module path? | `GATING` | **`REMAINS GATING`** · **widened by `FC-F4`: the question is now which of 22 roots is on the module path, not which of 2 trees** |
| `MCU-19` | Does any migrated/restored database hold a rate row whose company has a parent? | `GATING` | **`REMAINS GATING`** · needs a database, not a source tree |
| `MCU-19b` | Did the pre-v18 baseline carry the branch-rate constraint? | `NON-GATING`, class `C` | **`CLOSED — RESCOPED`.** The premise *"no v16/v14 framework core exists in the searched roots"* is **contradicted** by `FC-F4`: 22 roots exist, several are pre-`post20260605` v18 lines. The question is answerable and is folded into `MCU-18` |
| `MCU-20` | v19 ORM-core rate resolver: raw SQL, no record rule, `today`-dated, 4th fallback | opened | **`REMAINS GATING`** · **reproduced independently this round**; feeds `GB-08` §2.2 |

---

## 4. Opened by THIS round

| id | Unknown | Class | Gating? |
|---|---|---|---|
| **`MCU-21`** | **Which reference core root does SMEsPlus target?** 22 exist; **none is declared** | `B — SEARCHED, NOT ANSWERABLE FROM SOURCE` | **GATING.** It is a programme declaration, not a research result. **Every behavioural conclusion in Wave A is bounded by it** |
| **`MCU-22`** | Does a record rule on `account.report` exist in any of the **16 unsearched roots**? | `C — NOT YET SEARCHED`, boundary declared | **NON-GATING** — it can only *reduce* `MCU-04`'s blast radius, not overturn it (`FC-R1`) |

---

## 5. Standing gating set — final

| Bucket | Count | Ids |
|---|---|---|
| Inherited, still gating | **7** | `MCU-01`, `MCU-02`, `MCU-03`, `MCU-11`, `MCU-12`, `MCU-16`, `MCU-17` |
| Reclassified into gating by the adversarial pass | **4** | per `MCC_D` §8 |
| Reverted to `UNKNOWN` from out-of-scope | **2** | per `MCC_D` §8 |
| New gating from the fixed-point passes | **3** | incl. `MCU-18`, `MCU-19`, `MCU-20` |
| **New gating from THIS round** | **1** | **`MCU-21`** |
| **STANDING GATING TOTAL** | **`17`** | 16 corrected + `MCU-21` |

> **The corrected total returns to 17 — but by a different route and with different membership.**
> `MCU-04` closed; `MCU-21` opened. **This is stated as the coincidence it is**, exactly as the `MCC`
> round stated its own.

---

## 6. Are any of these NOT Wave-A-gating?

Required by closure criterion 3 — *closed, or explicitly proven non-Wave-A gating.*

| id | Test: does it determine ledger identity, measurement, period control or integrity? | Verdict |
|---|---|---|
| `MCU-01` | Measurement — it is the only route to executed behaviour | **WAVE A GATING** |
| `MCU-02`, `MCU-03` | Ledger identity | **WAVE A GATING — Boss decision** |
| `MCU-11` | Integrity / tenant isolation | **WAVE A GATING** |
| `MCU-12` | None directly — it is a **method** control | **NOT ledger-gating. GATE-gating**, via `MC-05` |
| `MCU-16` | Integrity — exposure surface | **WAVE A GATING**, mechanical |
| `MCU-17` | None directly — **method** control | **NOT ledger-gating. GATE-gating**, via `MC-07` |
| `MCU-18` | Measurement — which code is loaded | **WAVE A GATING** |
| `MCU-19` | Measurement — data state | **WAVE A GATING** |
| `MCU-20` | Measurement — a displayed monetary total | **WAVE A GATING** |
| **`MCU-21`** | **All four.** It selects the source of truth for every one | **WAVE A GATING — and it is the parent of `MCU-18`, `MCU-19b` and `GB-08`** |
| `MCU-22` | None — bounded, reduces blast radius only | **NOT GATING** |

**No unknown is routed to a later Wave.** The routing-abuse re-test is re-run and returns clean.

**8 of the 17 are ledger-gating. 2 are gate-gating method controls. `MCU-21` is both, and is the root
of three others.**

---

## 7. What would close the set

| Cost | Items | Work |
|---|---|---|
| **Hours, mechanical** | `MCU-21`, `MCU-12`, `MCU-16`, `MCU-17`, `MCU-18`, `MCU-22` | Declare the root set; re-scope existing bounded patterns; clear the correction backlog. **No new research** |
| **Days, needs a running instance** | `MCU-01`, `MCU-19` | Stand up a root+branch instance with divergent rate rows |
| **Boss decision, no research closes it** | `MCU-02`, `MCU-03`, and `GB-08` via `MCU-21` | — |
| **Bounded further search** | `MCU-11`, `MCU-20` | Both mechanisms are known; the surface is not enumerated |

> **`MCU-21` is first, and it is cheap.** It is a **declaration**, and closing it re-scopes `MCU-18`,
> `MCU-19b`, `GB-07`, `GB-08` and every class `A` absence in the programme at the same time.
