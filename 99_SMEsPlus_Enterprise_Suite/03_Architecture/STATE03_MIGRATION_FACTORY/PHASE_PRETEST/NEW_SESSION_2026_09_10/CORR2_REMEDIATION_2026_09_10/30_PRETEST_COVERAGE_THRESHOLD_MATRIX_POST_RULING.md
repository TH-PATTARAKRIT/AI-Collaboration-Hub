# 30 — PRE-TEST COVERAGE THRESHOLD MATRIX · POST-RULING

# `12 DIMENSIONS · 0 MEET EVERY FLOOR · 12 HOLD`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Authority: `§6`, `§7`, `§8` of the ruling prompt · **Supersedes `09_`** · Boss: **SOLE FINAL APPROVER**

> **`§6`: per-dimension floors. No averaging, no weighted compensation, no aggregate that hides a failed
> dimension. `§7`: the `12` dimensions are evaluated separately and MUST NOT be collapsed.**
> **No aggregate score appears in this file.**

---

## 1. PHASE RULE — `§8`, applied to every row

```
POPULATION (what must hold)      class S/D  ->  MUST exist at Pre-Test; absence is a CURRENT-PHASE FAILURE
MEASUREMENT (whether it holds)   class C/I  ->  CANNOT exist pre-build; 0% is NOT a current-phase failure
                                                PROVIDED the deferral carries all 6 contract elements (19_ SS4)
```

**Statuses used:** `PASS AT CURRENT PHASE` · `HOLD AT CURRENT PHASE` ·
`DEFERRED WITH VALID DOWNSTREAM CONTRACT` · `UNMEASURABLE — INVALID POPULATION` ·
`N/A — AUTHORITY SUPPORTED ONLY`.

---

## 2. `ZT-03` PRECONDITION — THE `25` CANONICAL DENOMINATORS, EACH WITH NAMED MEMBERSHIP

| # | Denominator | Value | Named membership | Source |
|---:|---|---:|---|---|
| `D-01` | Boundary classes | **`17`** | `BC-01`…`BC-17`, each labelled | `20_` §1 |
| `D-02` | `XMC-H` rows | `18` | `-01`…`-18` | `SA_CORR3_08` L213–230 |
| `D-03` | Conditional applicability items | `2` | `XMC-H-15`, `-16` | `20_` §4 |
| `D-04` | Contract rows | `10` | rows `1`…`10` | `SA_CORR4_02` §5 |
| `D-05` | Canonical vetoes | `7` | ratified set | `B3′` |
| `D-06` | `PTX` exit controls | `11` | `PTX-01`…`-11` | `B6`; `11` distinct ids in `2` files |
| `D-07` | `IR` flows | **`20`** | `IR-01`…`IR-18` **+ `MF-01`, `MF-02`** | `SA_CORR2_05`; `B9′` |
| `D-08` | `IR` reconciled | `14` | **`IR-01`…`IR-14`** | `26_` §2.1 |
| `D-09` | `AR` flows | **`30`** | `AR-01`…`AR-29` **+ `MF-01`** | `SA_CORR2_06`; `B9′` |
| `D-10` | `AR` reconciled | `15` | `AR-01`…`-06`, `-07`*, `-08`*, `-09`*, `-10`, `-13`, `-14`, `-15`, `-16`, `-28` (* `NO POSTING BY DESIGN`) | `26_` §2.1 |
| `D-11` | Verification items | `48` | `X-01`…`X-22` (`22`) + `E2E-01`…`-18` (`18`) + `PT-S-01`…`-07` (`7`) + `PT-C-01` (`1`) | `11_` §1, with an author-chosen flag per sub-population |
| `D-12` | `EC-04` boundaries | `3` | the three | `8C-CLARIFICATION-01` |
| `D-13` | `EC-07` passes | `2` | pass `1`, pass `2` — **neither performed** | `SC-AUTH-02` Reading C |
| `D-14` | Canonical scenarios | `22` | `X-01`…`X-22`, each named | `PT01`; `04_` §3 |
| `D-15` | Pre-Test exit conditions | **`14`** | `{1,2,3,4,5,6,7,8,11,13,14,15,16,17}` | `31_` |
| `D-16` | Open Boss decisions | **`4`** | `POH-D-02`, `SC-SMT-01`, `BOSS-CORR1-01`, `BOSS-CORR2-RD01` | `05_`; `13_` |
| `D-17` | FD blockers in the register | **`20`** | `FD-01`…`FD-20` | `29_` §1 |
| `D-18` | Business semantics | **`16`** | `BS-01`…`BS-16` | `28_` §2 |
| `D-19` | B-7 Round-1 findings | `18` | `B7-F-01`…`-18` | `5bd36d62` |
| `D-20` | B-7 Round-2 findings | `17` | `R2-F-01`…`-17` | `d878a603`; `01_` |
| `D-21` | SMEs Core obligations | **`9`** | `CORE-01`…`-08` + `CORR1-F-03` | `24_` §4 |
| `D-22` | External-authority items | `14` | **`X-01`…`X-13` + `X-15`** — *not* `X-01`…`X-14` | `36_` §2 |
| `D-23` | Configuration items | **`12`** | `CFG-01`…`CFG-12` | `22_` §3 |
| `D-24` | Optional functions | **`8`** | `OPT-01`…`OPT-08` | `23_` §3 |
| `D-25` | Critical / zero-tolerance controls | `9` | `ZT-01`…`ZT-09` | `27_` §1 |

```
DENOMINATORS                  25
WITH NAMED MEMBERSHIP         25
WITHOUT                        0
ZT-03 COVERAGE            25/25 = 100 %      FLOOR 100 %      MEETS
```

**Two are declared FLOORS, not proven exhaustive, and say so on their face:** `D-23` and `D-24`
(`22_` §2, `23_` §2). **A declared floor with a published bound is a named membership; an undeclared
bound is not.** `D-17` and `D-18` inherit the same bound, since `12` of the `20` blockers derive from
them.

---

## 3. THE `12` DIMENSIONS

### `A` — SOURCE PRESENCE

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Classes reached by a contract row | `17` | `12` | **`70.6 %`** | `96 %` | **HOLD** |
| Classes with an `XMC-H` row | `17` | `16` | **`94.1 %`** | `96 %` | **HOLD** |
| Applicable `XMC-H` rows contract-sufficient | `16` | `0` | **`0 %`** | `96 %` | **HOLD** |
| Contract rows contract-compliant | `10` | `0` | **`0 %`** | `96 %` | **HOLD** |
| Contract rows reaching a class | `10` | `10` | `100 %` | `96 %` | PASS |
| Readiness rows `WRITABLE` | `22` | `18` | **`81.8 %`** | `96 %` | **HOLD** — `B5′` unruled, `PROVISIONAL` |
| Denominators with named membership | `25` | `25` | `100 %` | `100 %` | PASS |
| Manifest integrity | `16` | `16` | `100 %` | `96 %` | PASS |
| Tax substitution rule base evidenced | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — external |
| **`A` VERDICT** | | | | | **`HOLD`** |

### `B` — RUNTIME REACHABILITY

| Measure | Denom. | Num. | Cov. | Status |
|---|---:|---:|---:|---|
| `EC-04` boundaries closed | `3` | `0` | `0 %` | **DEFERRED — valid contract** |
| `48`-item verification `PASS` | `48` | `0` | `0 %` | **DEFERRED — valid contract** |
| Scenarios runtime-verified | `22` | `0` | `0 %` | **DEFERRED — valid contract** |
| `E2E-04` traversal | `1` | `0` | `0 %` | **DEFERRED — valid contract** |
| `PTX` controls satisfied | `11` | `0` | `0 %` | **DEFERRED — valid contract** |
| Migration replay idempotency | `1` | `0` | `0 %` | **HOLD — semantic missing (`BS-05`), not merely unbuilt** |
| **`B` VERDICT** | | | | **`HOLD`** — `5` valid deferrals, **`1` blocked on a specification** |

### `C` — CONFIGURATION REACHABILITY

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Config items with a complete semantic contract | `12` | `5` | **`41.7 %`** | `96 %` | **HOLD** |
| Config items with a named future gate + contract | `12` | `12` | `100 %` | `96 %` | PASS |
| Non-configurable exclusions with an authority | `4` | `4` | `100 %` | `100 %` | PASS |
| Configuration reachability **measured** | `12` | `0` | `0 %` | — | DEFERRED — valid contract |
| **`C` VERDICT** | | | | | **`HOLD`** — was `UNMEASURABLE` |

### `D` — OPTIONAL FUNCTION REACHABILITY

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Optional functions with a complete contract | `8` | `1` | **`12.5 %`** | `96 %` | **HOLD** |
| With a named future gate + contract | `8` | `8` | `100 %` | `96 %` | PASS |
| Empty-set claims without authority | `0` | `0` | — | — | PASS |
| Reachability **measured** | `8` | `0` | `0 %` | — | DEFERRED — valid contract |
| **`D` VERDICT** | | | | | **`HOLD`** — was `UNMEASURABLE` |

### `E` — SEMANTIC COMPLETENESS

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Business semantics specified | `16` | **`0`** | **`0 %`** | `96 %` | **HOLD** |
| Business semantics **determined** (Pre-Test's own obligation) | `16` | `16` | `100 %` | `96 %` | PASS |
| Missing **objects** | `16` | `4` | — | — | measurement |
| **`E` VERDICT** | | | | | **`HOLD`** |

### `F` — CROSS-MODULE / HANDOFF

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Classes mapped in the crosswalk | `17` | `17` | `100 %` | `96 %` | PASS |
| Classes contract-sufficient | `17` | `2` | **`11.8 %`** | `96 %` | **HOLD** |
| `BC-17` mandatory chain legs proven | `4` | `0` | **`0 %`** | `96 %` | **HOLD** |
| Conditional items fully attributed | `2` | `2` | `100 %` | `100 %` | PASS |
| Gap-carrying flows outside the declared set | — | `0` base · `2` conditional | — | — | improved |
| **`F` VERDICT** | | | | | **`HOLD`** |

### `G` — CONTROL / INTERNAL CONTROL

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Critical controls at `100 %` | `9` | `7` | **`77.8 %`** | `100 %` | **HOLD** |
| Demand-approval gate specified | `1` | `0` | **`0 %`** | `100 %` | **HOLD** — `FD-09` |
| Reservation lifecycle specified | `1` | `0` | **`0 %`** | `100 %` | **HOLD** — `FD-10` |
| Transfer-neutrality independent check | `1` | `0` | **`0 %`** | `100 %` | **HOLD** — `FD-08` |
| Vetoes self-discharged | `0` viol. | `0` | `100 %` | `100 %` | PASS |
| **`G` VERDICT** | | | | | **`HOLD`** |

### `H` — DATA / IDENTITY / IMMUTABILITY

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Evidence integrity — manifests verify | `16` | `16` | `100 %` | `100 %` | PASS |
| Canonical artefacts overwritten | `0` viol. | `0` | `100 %` | `100 %` | PASS |
| Identifiers free of redefinition | `1` | `1` | `100 %` | `100 %` | PASS |
| Corrected-entry link exists | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-02` |
| Accounting-period object exists | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-04` |
| Idempotency identity exists | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-05` |
| Document numbering specified | `1` | `1` | `100 %` | `96 %` | PASS |
| **`H` VERDICT** | | | | | **`HOLD`** |

### `I` — TENANT / COMPANY ISOLATION

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Element `10` specified | `1` | **`0`** | **`0 %`** | **`100 %`** | **HOLD — `ZT-06`** |
| Isolation proofs stated | `8` | `0` | `0 %` | `100 %` | **HOLD** |
| Lock-defeat paths closed | `2` | `0` | `0 %` | `100 %` | **HOLD** |
| Cross-company statutory prohibition stated | `1` | `1` | `100 %` | `100 %` | PASS — `BD-ACC-02` |
| **`I` VERDICT** | | | | | **`HOLD` — and it is the dimension that blocks `§25`** |

### `J` — MIGRATION / HISTORICAL

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| `MF-03` classified | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `NOT DECIDABLE` |
| Migration elements suppliable (`14`, `15`) | `2` | `0` | **`0 %`** | `96 %` | **HOLD** |
| `FIFO` layer granularity in the payload | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-06` |
| Standard-cost independence tested | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-16` |
| Migration flows admitted to `IR`/`AR` | `3` | `3` | `100 %` | `96 %` | PASS — `B9′` |
| **`J` VERDICT** | | | | | **`HOLD`** |

### `K` — RECONCILIATION / END-TO-END

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| `IR` reconciled | `20` | `14` | **`70.0 %`** | `96 %` | **HOLD** |
| `AR` reconciled | `30` | `15` | **`50.0 %`** | `96 %` | **HOLD** |
| `E2E-04` traversable | `1` | `0` | `0 %` | — | DEFERRED — `I` limb |
| `BC-17` receipt→bill matching | `1` | `0` | **`0 %`** | `96 %` | **HOLD** — `FD-07` |
| **`K` VERDICT** | | | | | **`HOLD`** |

### `L` — ADVERSARIAL / ASSURANCE

| Measure | Denom. | Num. | **Cov.** | Floor | Status |
|---|---:|---:|---:|---:|---|
| Independent assurance passes | `2` | **`0`** | **`0 %`** | **`100 %`** | **HOLD — `ZT-05`** |
| Round-1 findings dispositioned | `18` | `18` | `100 %` | `96 %` | PASS |
| Round-2 findings dispositioned | `17` | `17` | `100 %` | `96 %` | PASS |
| Vetoes discharged by their issuer | `7` | `0` | — | — | `AAS-V-02` **NOT DISCHARGED** |
| Second-line challenges correctly classified | `2` | `2` | `100 %` | `100 %` | PASS |
| **`L` VERDICT** | | | | | **`HOLD`** |

---

## 4. DIMENSION ROLL-UP — no cell averaged into another

| Dim. | Name | Verdict | Worst measure |
|---|---|---|---|
| `A` | Source presence | **HOLD** | `0 %` — contract sufficiency / compliance |
| `B` | Runtime reachability | **HOLD** | `5` valid deferrals; `1` blocked on a missing specification |
| `C` | Configuration reachability | **HOLD** | `41.7 %` |
| `D` | Optional function reachability | **HOLD** | `12.5 %` |
| `E` | Semantic completeness | **HOLD** | `0 %` specified |
| `F` | Cross-module / handoff | **HOLD** | `11.8 %` contract-sufficient |
| `G` | Control / internal control | **HOLD** | `77.8 %` critical controls |
| `H` | Data / identity / immutability | **HOLD** | `3` missing objects |
| `I` | **Tenant / company isolation** | **HOLD** | `0 %` — element `10` |
| `J` | Migration / historical | **HOLD** | `0 %` — `MF-03` undecidable |
| `K` | Reconciliation / end-to-end | **HOLD** | `50.0 %` `AR` |
| `L` | Adversarial / assurance | **HOLD** | `0 %` — `ZT-05` |

```
DIMENSIONS                12
MEETING EVERY FLOOR        0
HOLD                      12
```

> **Correction before publication.** This file's headline first read *"`4` MEET THEIR FLOOR"*, counted
> from the `PASS` rows rather than from the dimension verdicts. **A dimension meets its floor only when
> EVERY measure inside it does. `0` do.** The headline is corrected to **`0 of 12`**, and the error is
> recorded here per `§22` — it is the precise defect `§6` forbids: **reading a passing sub-measure as a
> passing dimension.**

---

## 5. THE REQUIRED ANSWER

> ## **DID EVERY APPLICABLE AREA / DIMENSION MEET ITS FLOOR?**
>
> # `NO` — `0 of 12`

**`§7` obeyed: `12` dimensions reported separately, `0` collapsed, `0` averaged, `0` compensated.**
**`§7` of the CORR2 governance obeyed: source presence is used as evidence for no other dimension.**

**Movement since `09_`:** `UNMEASURABLE` **`2 → 0`** · critical controls at `100 %` **`3 → 7`** ·
denominators with named membership **`47.6 % → 100 %`** · **and `4` new failing measures appeared**
because two dimensions became measurable. **The package is materially more honest and is not closer to
passing.**

---

## 6. CHECKPOINT

> **`12` dimensions measured separately · **`0` meet every floor** · `25` denominators, **all with named
> membership — `ZT-03` `100 %`** · `2` `UNMEASURABLE` dimensions **closed** · `5` valid downstream
> deferrals, each with all `6` contract elements · **`1` deferral rejected as invalid** because its
> semantic is missing, not merely unbuilt · headline **corrected from `4` to `0`** by applying `§6`'s own
> rule to this file · **`0` averaging · `0` compensation · `0` source-presence substitution.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the SOLE FINAL APPROVER.**
