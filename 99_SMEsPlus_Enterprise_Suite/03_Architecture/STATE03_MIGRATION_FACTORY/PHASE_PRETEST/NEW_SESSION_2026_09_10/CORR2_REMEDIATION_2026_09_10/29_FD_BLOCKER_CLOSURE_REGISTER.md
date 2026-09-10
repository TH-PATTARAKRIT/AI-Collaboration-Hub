# 29 — FUNCTIONAL-DESIGN BLOCKER CLOSURE REGISTER

# `22 IDENTIFIED · 2 CLOSED · 19 OPEN · 1 BLOCKED · WAS 11`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§19` of the ruling prompt — *"Do not inherit `11` after corrections. Recompute from named
members."* · Boss: **SOLE FINAL APPROVER**

> **`11` was not inherited.** The register is rebuilt from the `16` business semantics (`28_`) and the
> `4` authority blocks, and reconciled against the previous `11` member by member at §3.

---

## 1. THE REGISTER

**Legend — Dimension:** `A` Source presence · `E` Semantic completeness · `F` Cross-module ·
`G` Control · `I` Isolation · `J` Migration · `L` Assurance.

| ID | Blocker | Missing semantic / control | Dim. | Cov. | Floor | Crit. | Owner | Correction required | Evidence | **Status** |
|---|---|---|:-:|---:|---:|:-:|---|---|---|---|
| **`FD-01`** | Orphan outputs and input | `BS-01` | `A` | — | `96 %` | **Y** | SMEs Core / Arch. | name a consumer per output, a producer per input | `10_` §2 #1; `XMC-H-09` | **OPEN** |
| **`FD-02`** | Corrected-entry link absent | `BS-02` | `E` | — | `96 %` | **Y** | SMEs Core | define the link | `O-1`; `X-11` | **OPEN** |
| **`FD-03`** | Reversal after downstream consumption | `BS-03` | `E` | — | `96 %` | **Y** | SMEs Core | define the outcome per consuming boundary | `O-3` | **OPEN** |
| **`FD-04`** | **No accounting-period object** → `BC-12` has no contract row | `BS-04` | `F`,`E` | **`0 %`** | `96 %` | **Y** | Arch. / Contract Semantics | create the object, then a contract row addressed to all subledgers | `XMC-H-12`; `X-19`; **`17_` §2.4 expressly refuses to discharge it** | **OPEN — ruled not discharged** |
| **`FD-05`** | **Idempotency identity absent** → `MF-03` undecidable; replay can duplicate an opening balance | `BS-05` | `J` | **`0 %`** | `96 %` | **Y** | SMEs Core | specify element `15` | `25_` §6; `CORR1-F-03` (restored, `24_`) | **OPEN — RESTORED** |
| **`FD-06`** | `FIFO` layer granularity absent from `HX-24` | `BS-06` | `J` | — | `96 %` | **Y** | SMEs Core | carry layers, or rule `FIFO` out of migration scope | `CORE-07` / `CORR1-F-02` (restored, `24_`) | **OPEN — RESTORED** |
| **`FD-07`** | **Goods receipt not item-matched to bill** — the `BC-17` chain | `BS-07` | `F`,`K` | **`0 %`** | `96 %` | **Y** | SMEs Core / Arch. | a receipt↔bill matching identity | `21_` §4; `X-01` *"swept suspense account, not item-matched"* | **OPEN — NEW** |
| **`FD-08`** | Transfer neutrality has **no independent check** | `BS-08` | `G` | **`0 %`** | **`100 %`** | **Y** | SMEs Core / Arch. | specify the rule **and** a check that fires when it is defeated | `SA06-F-05`; `R4-F-18`; `CORR2-CND-01`, `CORR2-CFG-02` | **OPEN — NEW** |
| **`FD-09`** | Demand-approval gate mechanism absent; `BC-03` bypasses it | `BS-09` | `G` | — | **`100 %`** | **Y** | SMEs Core | specify the gate and every entry path's relation to it | `XMC-H-03`; `X-12` | **OPEN — NEW** |
| **`FD-10`** | Reservation can be **silently reduced** | `BS-10` | `G` | — | **`100 %`** | **Y** | SMEs Core | enumerate reduction and release acts, each recorded | `X-12` | **OPEN — NEW** |
| **`FD-11`** | Supply Nature *make* rule undetermined | `BS-11` | `E` | — | `96 %` | **Y** | SMEs Core | state the rule with retained inputs | `XMC-H-02`; `ND-01` | **OPEN — NEW** |
| **`FD-12`** | **Quality object absent** | `BS-12` | `E`,`F` | **`0 %`** | `96 %` | **Y** | SMEs Core | create the object | `XMC-H-14` — `0` blobs | **OPEN — NEW** |
| **`FD-13`** | Service performance has no event record; `3` cost rows from `1` duration | `BS-13` | `E` | — | `96 %` | **Y** | SMEs Core | a performance event; a deterministic derivation | `XMC-H-17` | **OPEN — NEW** |
| **`FD-14`** | **Element `10` absent** — tenant/company isolation semantic | `BS-14` | **`I`** | **`0 %`** | **`100 %`** | **Y** | SMEs Core / Arch. | specify element `10`; state `8` testable isolation propositions | `X-15`; `SA10-F-05` two lock-defeat paths | **OPEN — `ZT-06`, BLOCKS §25** |
| **`FD-15`** | Consumable expensing point undetermined | `BS-15` | `E` | — | `96 %` | **Y** | SMEs Core (or Boss) | determine receipt vs issue; re-derive `32A_`'s row | `32A_` §3 declared basis | **OPEN — NEW** |
| **`FD-16`** | Standard-cost independence from migration untested | `BS-16` | `J` | — | `96 %` | **Y** | SMEs Core | state the cutover origin; test the asymmetry | `CORR2-MF-02` | **OPEN — NEW** |
| **`FD-17`** | `SC-SMT-01` — `Average` return-reversal residual | authority | `E` | — | `96 %` | **Y** | **BOSS** | Boss decision; **not re-asked** | `SC-BD-05` §8.1; `27_` `C-08-AC` | **OPEN — BOSS** |
| **`FD-18`** | `CORE-03` — veto limb-`2` re-wording | authority | `L` | — | **`100 %`** | **Y** | **AAS+ EXTERNAL** | issuer-authored record | `36_` `X-02`; `0` AAS+ records | **BLOCKED — RESTORED** |
| **`FD-19`** | Tax substitution rule base is a **black box** | authority | `A` | — | `96 %` | **Y** | **Thai statutory EXTERNAL** | statutory evidence | `XMC-H-11`; `CFG-06` | **OPEN — NEW, EXTERNAL** |
| **`FD-20`** | Normal-capacity register absent; `POH-D-02` withheld | authority | `E` | — | `96 %` | **Y** | **BOSS + statutory** | statutory evidence, then election | `L3`; `CFG-08`; `SC-60` | **OPEN — NEW, EXTERNAL** |

```
TOTAL IN THE REGISTER   20
  OPEN                  19    (FD-01..FD-17, FD-19, FD-20)
  BLOCKED (external)     1    FD-18
  CHECK  19 + 1          20   OK
CLOSED, NOT IN THE REGISTER  2   -- SS2
```

---

## 2. THE `2` CLOSED — both by `BOSS-CORR1-01`

| Was | Blocker | Closed because |
|---|---|---|
| `10_` #4 | *"`4` gap-carrying handoffs **outside the declared boundary set**"* | **`BOSS-CORR1-01` (c)** brings `XMC-H-13`, `-14`, `-17`, `-18` **inside** as `BC-13`…`BC-16`, and adds `BC-17`. **`0` gap-carrying flows remain outside.** The blocker was *"designers cannot know their own scope"*; **scope is now declared.** The flows are still gaps — they are now `FD-12`, `FD-13`, `FD-05`, `FD-07` and `BC-13`'s reconciliation hazard — **but they are inside the denominator and named** |
| `10_` #5 | **`B4′` × `B9′` tension** (`B7-F-08`) | `B9′` admitted `MF-01`/`MF-02` onto `XMC-H-18`, which `B4′` excluded. **`XMC-H-18` is now `BC-16`, inside the set. The contradiction has no subject** |

```
20 in the register  +  2 closed  =  22 accounted
of the previous 11: 2 CLOSED · 8 CARRIED · 1 MERGED (see SS3)
```

---

## 3. RECONCILIATION AGAINST THE PREVIOUS `11` — member by member

**`§19`: *"No blocker may disappear because its source file was superseded."***

| `10_` # | Was | **Now** | Disposition |
|---:|---|---|---|
| `1` | orphan outputs + input | **`FD-01`** | CARRIED |
| `2` | `O-1` corrected-entry link | **`FD-02`** | CARRIED |
| `3` | `O-3` reversal after consumption | **`FD-03`** | CARRIED |
| `4` | gap-carrying flows outside the set | — | **CLOSED** — `BOSS-CORR1-01` |
| `5` | `B4′` × `B9′` tension | — | **CLOSED** — `BOSS-CORR1-01` |
| `6` | declared class `12` uncovered | **`FD-04`** | CARRIED — and `17_` §2.4 **expressly refuses to discharge it** |
| `7` | flow population not established | **`FD-05`** | **MERGED with `9`.** `IR`/`AR` memberships are **SOUND** (my path-set error, `26_` §2); what remains is `MF-03`, which turns on element `15` — the same semantic as `9` |
| `8` | `CORR1-F-02` `FIFO` layers | **`FD-06`** | CARRIED |
| `9` | `CORR1-F-03` idempotency | **`FD-05`** | **MERGED with `7`** |
| `10` | `CORE-03` limb-`2` | **`FD-18`** | CARRIED — BLOCKED |
| `11` | `SC-SMT-01` | **`FD-17`** | CARRIED — BOSS |

```
PREVIOUS 11 :  2 CLOSED  ·  8 CARRIED  ·  1 MERGED into a carried blocker
CHECK  2 + 8 + 1 = 11   OK
NEW THIS ROUND : 12   -- enumerated at SS3.1
```

### 3.1 The arithmetic, stated so it can be re-derived rather than trusted

```
CARRIED from the previous 11 :  FD-01 FD-02 FD-03 FD-04 FD-05 FD-06 FD-17 FD-18      = 8
  (FD-05 absorbs both #7 and #9)
NEW this round               :  FD-07 FD-08 FD-09 FD-10 FD-11 FD-12
                                FD-13 FD-14 FD-15 FD-16 FD-19 FD-20                  = 12
CHECK  8 + 12                                                                        = 20  OK
CLOSED (not in the register) :  #4, #5                                               =  2
CHECK  previous 11 = 8 carried + 1 merged-into-carried + 2 closed                     = 11  OK
```

> **Correction made before publication:** §3's summary line first read *"NEW THIS ROUND: `10`"*.
> Counting the identifiers returns **`12`**. **Corrected, and the error left visible** per `§22`.

---

## 4. WHY THE COUNT ROSE `11 → 20`

**`12` new blockers, and none of them is a new defect.** All `12` were already recorded somewhere in the
corpus as gaps; they were **not in the blocker register because the dimension that would surface them
was not being measured**:

| Source of the new blockers | n | Made visible by |
|---|---:|---|
| Configuration Reachability population | `4` | `FD-08`, `FD-09`, `FD-10`, `FD-11` — `22_` §3's `7` incomplete items |
| Optional Function inventory | `4` | `FD-12`, `FD-13`, `FD-14`, `FD-15` — `23_` §3's `7` incomplete entries |
| Boundary expansion to `17` | `1` | `FD-07` — `BC-17`'s mandatory chain (`21_` §4) |
| Previously raised, never measured | `1` | `FD-16` — `CORR2-MF-02` |
| Config population, external authority | `2` | `FD-19`, `FD-20` |

> **`CORR2-FDC-01` — MATERIAL. `11 → 20` is a measurement improvement, not a regression.**
> `§12` and `§13` required populations that did not exist. **Declaring them made `12` pre-existing gaps
> countable.** The previous `11` was an undercount produced by four unmeasured dimensions, exactly as
> `23_` §4 and `28_` §3 independently found. **Reporting `11` after this work would have been the
> defect.**

---

## 5. THE CONTROLLING QUESTION

> ## **CAN FUNCTIONAL DESIGN BEGIN WITHOUT INVENTING MISSING BUSINESS SEMANTICS?**
>
> # `NO` — `19` open + `1` externally blocked · `16` semantics · `4` missing **objects**

**`4` blockers are missing objects rather than missing rules — `FD-04` (accounting period), `FD-05`
(idempotency identity), `FD-12` (Quality object), `FD-14` (element `10`).** A designer cannot route
around an object that does not exist.

**Ownership:** SMEs Core `14` · Architecture `6` · Boss `2` · External `3` *(a blocker may have more
than one owner; the sum exceeds `20` by design and the per-row Owner column governs)*.

---

## 6. COVERAGE

| Measure | Denominator | Named | Numerator | Coverage | Floor | Verdict |
|---|---:|:-:|---:|---:|---:|---|
| FD blockers closed | **`22` ever identified** | ✔ | `2` | **`9.1 %`** | `96 %` | **HOLD** |
| Blockers in the register with a named owner, evidence and correction | `20` | ✔ | `20` | **`100 %`** | `96 %` | **MEETS** |
| Blockers closable below Boss / external | `20` | ✔ | `16` | `80.0 %` | — | measurement |
| Blockers that are missing **objects** | `20` | ✔ | `4` | `20.0 %` | — | measurement |

---

## 7. CHECKPOINT

> **Recomputed from named members, **`11` not inherited** · **`22` ever identified — `2` CLOSED by
> `BOSS-CORR1-01`, `19` open, `1` externally blocked** · previous `11` reconciled member by
> member — `2` closed, `8` carried, `1` merged ✔ · **`12` new, and `CORR2-FDC-01`: all `12` are
> pre-existing gaps made countable by the two new populations and the boundary expansion** ·
> `4` are missing **objects** · this file's own *"new = `10`"* **corrected to `12` by counting** ·
> **`FD-14` blocks `§25` eligibility** · **FUNCTIONAL DESIGN NOT AUTHORIZED.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
