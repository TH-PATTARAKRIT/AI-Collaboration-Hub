# 09 — PRE-TEST COVERAGE THRESHOLD MATRIX

# `DID EVERY APPLICABLE DIMENSION MEET ITS FLOOR?  NO`

## `CHECKPOINT J · CHECKPOINT K`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **`§4`: `96 %` is a MINIMUM FLOOR PER APPLICABLE AREA / DIMENSION — not an average, not a blend, not a
> compensation mechanism. `§5`: Critical / Zero-Tolerance = `100 %`, no exception.**
> **No aggregate figure appears in this file. Every cell stands alone.**

---

## 1. THE PHASE RULE, APPLIED PRECISELY — `§11`

`§11` forbids demanding proof at a phase where the proof cannot exist. **It does not excuse a missing
specification.** The distinction below is the analytic spine of this matrix:

| For any dimension | The **POPULATION** (what must be reachable) | The **MEASUREMENT** (whether it is reachable) |
|---|---|---|
| Class | **`S` / `D`** — a specification artefact | **`I` / `C`** — needs a build |
| Can it exist at Pre-Test? | **YES** | **NO** |
| So at Pre-Test | **it MUST exist, and its absence is a Pre-Test failure** | **it is phase-placed downstream, and `0 %` is not a Pre-Test failure** |

> **A dimension with a valid population and a `0 %` measurement is correctly deferred.
> A dimension with NO population is not deferred — it is unspecified, and that is a Pre-Test defect.**
>
> **This distinction is what separates `RUNTIME REACHABILITY` (population valid, measurement deferred)
> from `CONFIGURATION` and `OPTIONAL FUNCTION` REACHABILITY (no population at all).**

---

## 2. DIMENSION `A` — SOURCE PRESENCE COVERAGE

*Does the required function / configuration / control / semantic exist in the authoritative source
population?* **Measurable now. Floor applies now.**

| Area | Function / control | Denominator | Named membership | Numerator | **Coverage** | Floor | Crit. | Evidence | Verdict |
|---|---|---:|:--:|---:|---:|---:|:--:|---|---|
| Cross-module boundaries | classes reached by a contract row | `12` | **YES** | `11` | **`91.7 %`** | `96 %` | **Y** | `06_` §3 | **HOLD** |
| Cross-module boundaries | contract rows reaching a class | `10` | **YES** | `9` | **`90.0 %`** | `96 %` | **Y** | `06_` §3 | **HOLD** |
| Cross-module boundaries | applicable `XMC-H` rows contract-sufficient | `16` | **YES** | **`0`** | **`0 %`** | `96 %` | **Y** | `SA_CORR3_08` | **HOLD** |
| Cross-module boundaries | contract rows **contract-compliant** | `10` | **YES** | **`0`** | **`0 %`** | `96 %` | **Y** | `SA_CORR4_02` §5, its own words | **HOLD** |
| Cross-module boundaries | `N/A` rows carrying their defeating condition | `2` | **YES** | **`0`** | **`0 %`** | `100 %` | **Y** | `06_` §4 | **HOLD** |
| Material flow | `IR` membership enumerated | `20` | **NO** | `6` | **`30.0 %`** | `96 %` | **Y** | `08_` row `9` | **HOLD** |
| Material flow | `AR` membership enumerated | `30` | **NO** | `10` | **`33.3 %`** | `96 %` | **Y** | `08_` row `11` | **HOLD** |
| Material flow | `MF-03` discriminators tested | `6` recorded | **YES** | `1` | **`16.7 %`** | `96 %` | **Y** | `07_` §3 | **HOLD** |
| Gate constitution | re-placements on external authority | `4` | **YES** | `3` | **`75.0 %`** | `96 %` | **Y** | `03_` §1 | **HOLD** |
| Gate constitution | governing clauses applied (`SC-54` cl. `2`,`3`,`5`) | `3` | **YES** | `2` | **`66.7 %`** | `96 %` | **Y** | `04A_` §5 | **HOLD** |
| Gate constitution | exit conditions satisfied | **`14`** | **YES** | `5` | **`35.7 %`** | `96 %` | **Y** | `03_` §3 | **HOLD** |
| Readiness | scenarios `WRITABLE` | `22` | **YES** | `18` | **`81.8 %`** | `96 %` | **Y** | `04_` §3, re-extracted | **HOLD** |
| Denominator governance | denominators with sound named membership | `21` | **YES** | `10` | **`47.6 %`** | `100 %` (`ZT-03`) | **Y** | `08_` §3 | **HOLD** |
| Boss governance | open Boss decisions correctly carried | `4` | **YES** | `1` | **`25.0 %`** | `100 %` (`ZT-09`) | **Y** | `05_` §5 | **HOLD** |
| Obligation governance | `CORR1` open obligations carried into the successor | `3` | **YES** | **`0`** | **`0 %`** | `100 %` | **Y** | `10_` §2 | **HOLD** |
| Obligation governance | identifiers free of redefinition | `1` (`CORE-07`) | **YES** | **`0`** | **`0 %`** | `100 %` | **Y** | `10_` §2 | **HOLD** |
| Business semantics | FD blockers closed | `11` | **YES** | **`0`** | **`0 %`** | `96 %` | **Y** | `10_` §3 | **HOLD** |
| Authority evidence | ruling acts with a durable artefact | `1` (`R-D-01`) | **YES** | **`0`** | **`0 %`** | `100 %` (`ZT-08`) | **Y** | `04A_` §2 | **HOLD** |
| Evidence integrity | manifest entries verifying | `15` | **YES** | `15` | **`100 %`** | `96 %` | **Y** | `01_` §3, controls fire | **MEETS FLOOR** |
| Evidence integrity | package files covered by a manifest | `16` | **YES** | `15` + `1` self-ref | **`100 %`** | `96 %` | **Y** | set-difference | **MEETS FLOOR** |
| Evidence integrity | canonical artefacts modified by an audit channel | `0` violations | **YES** | `0` | **`100 %`** (`ZT-01`) | `100 %` | **Y** | `git diff --name-status` | **MEETS FLOOR** |
| Veto governance | vetoes self-discharged | `0` violations | **YES** | `0` | **`100 %`** (`ZT-02`) | `100 %` | **Y** | `07_AAS_V02`; `01_` §3 | **MEETS FLOOR** |
| Disposition | `PT-16` §11 items disposed | `8` | **YES** | `8` | **`100 %`** | `96 %` | **Y** | `08_` row `14` of `03_` | **MEETS FLOOR** |
| Finding intake | Round-2 findings dispositioned | `17` | **YES** | `17` | **`100 %`** | `96 %` | **Y** | `01_` §4 | **MEETS FLOOR** |
| Finding intake | Round-1 findings dispositioned | `18` | **YES** | `18` | **`100 %`** | `96 %` | **Y** | `02_` recovery register | **MEETS FLOOR** |

```
SOURCE PRESENCE ROWS               25   (counted from the table above, not asserted)
MEET THEIR FLOOR                    7   — all of them integrity, disposition or "0 violations" controls
BELOW THEIR FLOOR                  18
CHECK  7 + 18                      25   OK
```

> **Every row that meets its floor measures whether the package was *handled* correctly.
> Every row that fails measures whether the *subject matter* is specified.
> The programme's controls are working; the architecture underneath them is not yet specified.**

---

## 3. DIMENSION `B` — RUNTIME REACHABILITY COVERAGE

*Can the function/control actually be reached and executed in the intended runtime context?*

| Area | Denominator | Named membership | Numerator | **Coverage** | Population class | Measurement class | Phase placement | Verdict |
|---|---:|:--:|---:|---:|---|---|---|---|
| `EC-04` runtime boundaries | `3` | **YES** | **`0`** | **`0 %`** | `S` — exists | **`I`** | **State 8-Criteria Exit Gate** (`SC-54` cl. 3) | **DEFERRED — correctly** |
| `48`-item verification | `48` | **YES** — `22+18+7+1`, decomposed | **`0 PASS`** | **`0 %`** | `S` — exists | **`I`** | **Build / Test** (`SA17` §2b) | **DEFERRED — correctly** |
| Canonical scenarios runtime-verified | `22` | **YES** — `X-01…X-22` | **`0`** | **`0 %`** | `S` — exists | **`I`** | **Build / Test** | **DEFERRED — correctly** |
| `E2E-04` traversal | `1` | **YES** | **`0`** | **`0 %`** | `S` — exists | **`I`** | Build / Test | **DEFERRED — correctly** |
| `PTX` exit controls satisfied | `11` | **YES** — `PTX-01…-11` | **`0`** | **`0 %`** | `S` — exists | **`I`** | Build / Test | **DEFERRED — correctly** |
| **`MF-01`/`MF-02` idempotency on re-run** | `1` | **YES** — `CORR1-F-03` | **`0`** | **`0 %`** | `S` — **DROPPED (`10_` §2)** | **`I`** | Build / Test | **`HOLD` — the obligation was deleted, not deferred** |

**`RUNTIME REACHABILITY = 0 % across every population, and `5 of 6` are correctly phase-placed.**

> **`0 %` here is NOT a Pre-Test failure.** No build exists. `SA17` §2b: *"nothing may be read as testing
> tenant isolation until an implementation exists."* **Demanding this proof at Pre-Test is the circular
> gate defect `03_` §5 resolves.**
>
> **The sixth row IS a Pre-Test failure** — not because the measurement is missing, but because the
> **obligation that would carry it downstream was dropped** (`10_` §2). **A deferred obligation must still
> exist.**

---

## 4. DIMENSIONS `C` AND `D` — CONFIGURATION AND OPTIONAL-FUNCTION REACHABILITY

### `C` — Configuration Reachability

*Can the required configuration be found, reached, selected, activated, persisted and applied under the
intended tenant/company/business context?*

```
POPULATION : configurations declared in scope as requiring reachability
UNIT       : configuration item
PATTERN    : 'configuration reachab' | 'config path' | 'activation path' | 'persist.*configuration'
PATH SET   : NEW_SESSION_2026_09_10/**  at c91d5840   (80 files)

DECLARED CONFIGURATION-REACHABILITY POPULATION            0 files
POSITIVE CONTROL — files mentioning 'configuration'       9 files      THE INSTRUMENT FIRES
```

### `D` — Optional Function Reachability

```
POPULATION : optional functions declared inside approved scope
PATTERN    : 'optional function' | 'enable condition' | 'OPTIONAL FUNCTION REACHAB'

DECLARED OPTIONAL-FUNCTION INVENTORY                       0 files
POSITIVE CONTROL — files mentioning 'optional'             3 files      THE INSTRUMENT FIRES
  and none of the 3 is an inventory: one concerns COMPANY scope,
  one a regex bolding artefact, one says an item "is not thereby optional"
```

| Dimension | Denominator | Numerator | Coverage | Verdict |
|---|---|---|---|---|
| **`C` Configuration Reachability** | **UNDECLARED** | — | **NOT MEASURABLE** | **HOLD** |
| **`D` Optional Function Reachability** | **UNDECLARED** | — | **NOT MEASURABLE** | **HOLD** |

**`CORR2-COV-01` — MATERIAL.**

> **`§9`: no percentage is valid without `DENOMINATOR + NAMED MEMBERSHIP + NUMERATOR + EVIDENCE`.
> These two dimensions have no denominator, so no percentage can be computed — and a dimension that
> cannot be measured cannot meet a floor.**
>
> **This is not a phase-placement case.** The **measurement** is `C`/`I`-class and rightly deferred.
> **The population is `S`/`D`-class and could exist today.** `§25` requires, for every optional function
> in scope: enable condition, configuration path, runtime path, owner, business consequence, disabled
> behaviour, evidence. **`0 of 7` exist because `0` optional functions are declared.**
>
> **`§24`: this may not be recorded as `N/A`.** An unsupported `N/A` counts as **UNRESOLVED** and stays
> in the denominator. **Two applicable dimensions are unspecified, and that is a Pre-Test defect.**

---

## 5. DIMENSION `G` — CRITICAL / ZERO-TOLERANCE CONTROL COVERAGE · `§5`, `§23`

**The `9` controls are constituted here as a named, closed set.** `§23` requires an attempt to falsify
every claimed `100 %`. **Each attempt is recorded.**

| ID | Critical control | Required | Denom. | Numer. | **Coverage** | Falsification attempt | **Verdict** |
|---|---|---:|---:|---:|---:|---|---|
| **`ZT-01`** | No canonical artefact overwritten by an audit channel | `100 %` | `0` violations | `0` | **`100 %`** | `git diff --name-status 8674f735 c91d5840` → changes confined to the package path; `0` `PT-xx`, `0` `CORRECTIVE_CLOSURE` artefacts modified. **Attack FAILED** | **MEETS** |
| **`ZT-02`** | No veto self-discharged | `100 %` | `0` violations | `0` | **`100 %`** | `3` instrument shapes + a synthetic injection that fires; `0` AAS+-authored records; `7` vetoes, `0` discharged. **Attack FAILED** | **MEETS** |
| **`ZT-03`** | Every denominator has named membership | `100 %` | `21` | `10` | **`47.6 %`** | attack **SUCCEEDED** — `11` defective, `8` classes (`08_`) | **`HOLD`** |
| **`ZT-04`** | No unsupported or conditional `N/A` | `100 %` | `2` | `0` | **`0 %`** | attack **SUCCEEDED** — both `N/A`s are configuration-defeasible and the condition is dropped (`06_` §4) | **`HOLD`** |
| **`ZT-05`** | Independent assurance established | `100 %` | `2` passes | `0` | **`0 %`** | attack **SUCCEEDED** — **neither B-7 round is independent** (`02_`) | **`HOLD`** |
| **`ZT-06`** | Tenant / company isolation proven | `100 %` | `48` | `0` | **`0 %`** | not falsifiable at this phase — **population valid, measurement `I`-class, phase-placed to Build/Test** | **`HOLD` — DEFERRED** |
| **`ZT-07`** | Evidence integrity — immutable and verifiable | `100 %` | `15` | `15` | **`100 %`** | one-byte corruption control **fires**; addition-blindness demonstrated and answered by set-difference; coverage complete. **Attack FAILED** | **MEETS** |
| **`ZT-08`** | No authority act without a durable artefact | `100 %` | `1` | `0` | **`0 %`** | attack **SUCCEEDED** — `R-D-01`, searched across `194` branches, positive control fires at `9` (`04A_`) | **`HOLD`** |
| **`ZT-09`** | No Boss-reserved obligation leaves the count without a closure act | `100 %` | `4` | `1` | **`25.0 %`** | attack **SUCCEEDED** — `3` open decisions uncounted, `0` closures recorded (`05_`) | **`HOLD`** |

```
CRITICAL CONTROLS            9
AT 100 %                     3    ZT-01, ZT-02, ZT-07
BELOW 100 %                  6    ZT-03, ZT-04, ZT-05, ZT-06, ZT-08, ZT-09
FALSIFICATION SUCCEEDED      5    ZT-03, ZT-04, ZT-05, ZT-08, ZT-09
FALSIFICATION FAILED         3    ZT-01, ZT-02, ZT-07   -- published as evidence
NOT FALSIFIABLE AT PHASE     1    ZT-06
```

> **`§5`: no critical claim passes at `99 %`, `99.9 %` or `99.99 %`. `6 of 9` are below `100 %`, and
> `5` were falsified by direct attack. `HOLD` on the critical dimension alone.**
>
> **The `3` that hold are the package's real achievement and are recorded as such: `0` canonical writes,
> `0` self-discharged vetoes, `100 %` evidence integrity with firing controls.**

---

## 6. `CHECKPOINT K` — EVERY `< 96 %` AND EVERY CRITICAL `< 100 %`, ISOLATED

**Applicable non-critical dimensions below `96 %` — `18`**, all in §2, none compensable by any other cell.

**Critical / Zero-Tolerance below `100 %` — `6`:**

| ID | Coverage | Gap to floor | Closable below Boss? | By |
|---|---:|---:|---|---|
| `ZT-03` named membership | `47.6 %` | `52.4` pts | **YES** | SMEs Core / Architecture — enumerate `IR`/`AR`, fix `4` memberships |
| `ZT-04` `N/A` support | `0 %` | `100` pts | **YES** | carry the defeating condition in the row |
| `ZT-05` independent assurance | `0 %` | `100` pts | **YES** — apparatus | `16_` rerun under a proven identity |
| `ZT-06` tenant/company isolation | `0 %` | `100` pts | **NO — phase** | Build / Test |
| `ZT-08` authority artefact | `0 %` | `100` pts | **NO — Boss** | **`BOSS-CORR2-RD01`** |
| `ZT-09` Boss-decision count | `25.0 %` | `75` pts | **YES** — the count | the `4` decisions themselves are Boss's |

**`4 of 6` are closable below Boss. `1` is phase-bound. `1` is irreducibly Boss's.**

---

## 7. THE ROLL-UP — `AREA → FUNCTION → DIMENSION → COVERAGE → THRESHOLD → PASS/HOLD`

**No cell is averaged into another. A row passes only if every dimension applicable to it passes.**

| Area | `A` Source | `B` Runtime | `C` Config | `D` Optional | `G` Critical | **Area verdict** |
|---|---:|---:|---:|---:|---:|---|
| Cross-module boundary contracts | **`0 – 91.7 %`** | `0 %` deferred | **NOT MEASURABLE** | **NOT MEASURABLE** | `ZT-03`,`ZT-04` fail | **`HOLD`** |
| Material flow register | **`16.7 – 33.3 %`** | `0 %` deferred | **NOT MEASURABLE** | **NOT MEASURABLE** | `ZT-03` fails | **`HOLD`** |
| Gate constitution / exit criteria | **`35.7 – 75.0 %`** | `0 %` deferred | n/a | n/a | `ZT-08` fails | **`HOLD`** |
| Readiness scenarios | **`81.8 %`** | `0 %` deferred | **NOT MEASURABLE** | **NOT MEASURABLE** | — | **`HOLD`** |
| Verification (`48`) | `100 %` membership | `0 %` deferred | **NOT MEASURABLE** | **NOT MEASURABLE** | `ZT-06` deferred | **`HOLD`** |
| Veto & authority governance | **`0 %`** (`R-D-01`) | n/a | n/a | n/a | `ZT-02` **MEETS**, `ZT-08` fails | **`HOLD`** |
| Boss decision governance | **`25.0 %`** | n/a | n/a | n/a | `ZT-09` fails | **`HOLD`** |
| Obligation governance | **`0 %`** | n/a | n/a | n/a | — | **`HOLD`** |
| Independent assurance | **`0 %`** | n/a | n/a | n/a | `ZT-05` fails | **`HOLD`** |
| Business semantics / FD blockers | **`0 %`** — `0 of 11` closed | n/a | n/a | n/a | — | **`HOLD`** |
| **Evidence integrity** | **`100 %`** | n/a | n/a | n/a | `ZT-01`,`ZT-07` **MEET** | **MEETS FLOOR** |
| **Finding intake & disposition** | **`100 %`** | n/a | n/a | n/a | — | **MEETS FLOOR** |

**`12` areas · `2` meet every applicable floor · `10` `HOLD`.**

**No compensation was applied anywhere.** `§4`: a score above `96 %` in one dimension cannot offset
another below it. **Evidence integrity at `100 %` offsets nothing.**

---

## 8. THE REQUIRED ANSWER — `§20`

> ## **DID EVERY APPLICABLE AREA / DIMENSION MEET ITS FLOOR?**
>
> # `NO`

| Dimension | Result |
|---|---|
| **`A` SOURCE PRESENCE** | **`18 of 25` rows below `96 %`.** Lowest `0 %`, highest failing `91.7 %` |
| **`B` RUNTIME REACHABILITY** | **`0 %` on all `6` populations.** `5` correctly phase-placed; **`1` is a dropped obligation, not a deferral** |
| **`C` CONFIGURATION REACHABILITY** | **NOT MEASURABLE — no declared population.** `HOLD` |
| **`D` OPTIONAL FUNCTION REACHABILITY** | **NOT MEASURABLE — no declared inventory.** `HOLD` |
| **`G` CRITICAL / ZERO-TOLERANCE** | **`6 of 9` below `100 %`; `5` falsified by direct attack.** `HOLD` |

**`§7` applied throughout: `SOURCE PRESENCE ≠ RUNTIME REACHABILITY ≠ CONFIGURATION REACHABILITY ≠
FUNCTION COMPLETE`. No row in this matrix uses source presence as evidence for any other dimension.**

**`§8` — `FUNCTION RESEARCH-COMPLETE`: `0` functions qualify.** Condition `4` (all applicable
non-critical dimensions `≥ 96 %`) fails everywhere; condition `5` (critical `= 100 %`) fails in `6`
places; condition `7` (no missing business semantic) fails on **`9` inventions** (`10_` §4).

---

## 9. CHECKPOINT

> ## `CHECKPOINT J — COVERAGE THRESHOLD MATRIX COMPLETED`
> ## `CHECKPOINT K — ALL <96 % AND ALL CRITICAL <100 % ISOLATED`
>
> `5` dimensions measured **separately, never collapsed** · `25` source-presence rows · `6` runtime
> populations · **`2` dimensions with no declared population at all (`CORR2-COV-01`)** ·
> `9` critical controls constituted, **`5` falsified by direct attack, `3` attacks failed and are
> published** · `18` non-critical rows `< 96 %` · `6` critical `< 100 %` · `12` areas, `2` meeting
> every floor · **`0` averaging · `0` compensation · `0` source presence used as runtime proof ·
> `0` unsupported `N/A`** ·
> **ANSWER: `NO`. NO DOWNSTREAM HANDOFF.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
