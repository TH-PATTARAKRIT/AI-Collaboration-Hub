# 34 — `CORR1` RECONCILED MATRIX

## `ALL DENOMINATORS RESTATED WITH NAMED MEMBERSHIP`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]` · Boss: **SOLE FINAL APPROVER**

---

## 1. The controlled denominators

| Denominator | Before | **`CORR1`** | Membership named? | Moved by |
|---|---|---|:--:|---|
| Readiness split | `19 / 2 / 1` | **`18 / 4 / 0`** | **YES — `27_` §4** | re-derivation |
| Declared boundary classes | `12` | **`12` — unamended** | YES — `22_` §1 | **`0` — SMEs Core may not enlarge it** |
| `XMC-H` handoff rows | `18` | **`18`** | YES | — |
| `SA_CORR4_02` contract rows | `10` | **`10`** | YES — `28_` §1 | — |
| **Boundaries outside the declared set** | not measured | **`6`** (`4` `C` + `2` `B`) | **YES — `28_` §2.1** | **`28_`** |
| Canonical vetoes | `7` · `0` discharged | **`7` · `0` discharged** | YES — `07_` §1 | — |
| `PTX` controls | `11` · `0` satisfied | **`11` · `0` satisfied** | YES | — |
| `IR` flows | `20` · `14` reconciled | **`20` · `14`** | YES | — |
| `AR` flows | `30` · `15` reconciled | **`30` · `15`** | YES | — |
| Verification items | `48` · `0 PASS` | **`48` · `0 PASS`** | YES — `11_` §1 | — |
| `EC-04` | `0 / 3` | **`0 / 3`** — re-placed to the State gate | YES | `32_` |
| `EC-07` | `0 / 2` | **`0 / 2`** — re-placed to the State gate | YES | `32_` |
| Exit conditions | `8 of 17` | **`7 of 17`** (`7 of 14` Pre-Test-owned) | **YES — `31_` §2** | recount |
| FD blockers | `3` | **`3` business semantics + `1` scope declaration** | YES — `31_` §3 | `28_` |
| Open Boss decisions | `1` | **`3`** — §2 | YES — `35_` | `26_`, `28_` |
| SMEs Core obligations | `3` | **`4`** (`CORE-04` discharged, `CORE-06` discharged, `CORE-05` specified, **`CORE-07` new**) | YES — `35_` §3 | `28_`, `29_`, `32A_` |
| External-authority items | `13` | **`14`** | YES — `36_` | `29_` §6.3 |

---

## 2. Open Boss decisions — `1 → 3`

**`22_` §4 reported *"Open Boss decisions: `7` → `1`."* That count was low.**

| # | Item | Origin | Why Boss |
|---:|---|---|---|
| `1` | **`POH-D-02`** — Thai statutory tax consequences of the absorption method | `B1`, withheld | statutory authority is required and no Boss act can supply it |
| `2` | **`SC-SMT-01`** — reconciliation-control design for the `Average`-costing original-cost reversal residual | `SC-BD-05` §8.1 / `SC-03` | disposition **`BOSS-ONLY DECISION`**; `09_JT05` §5 assigns it to **Boss** at primary text; **it gates scenarios `8` and `9` (`27_`)** |
| `3` | **`BOSS-CORR1-01`** — boundary denominator correction | `28_` §4 | `B4′` is a Boss declaration; only its issuer may amend its membership |

> **`SC-SMT-01` was carried as an *obligation* (`SC-11` §6 #3, `PT-11` L109 `OPEN`) and was never counted
> as an open Boss **decision**, though `SC-03` classifies it as one. `B7-F-04` surfaced it by its
> consequence. The count is corrected to `3`.**

---

## 3. Readiness — restated

| Class | Members | n |
|---|---|---:|
| `WRITABLE` | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `10`, `11`, `12`, `13`, `14`, `15`, `18`, `19`, `20`, `21`, `22` | **`18`** |
| `GATED` | `8`, `9` (`SC-SMT-01`) · `16`, `17` (`B-6`) | **`4`** |
| `NOT ESTABLISHED` | — | **`0`** |

**`0 of 22` runtime-verified — UNCHANGED. `B5′` remains `NO RULING`; `18/4/0` is a derivation, not authority.**

---

## 4. `B7-F-14` — the `PT-S-01` measurement, restated with a declared path set

**As published (`PT-01` §5.2):** *"`VAT` `0` and `WHT` `0` in **all three scenario registers**"* — the
three were never named.

**Restated. PATH SET, declared:**

| Register | Role | `VAT` (whole word) | `WHT` | `dropship` (control) |
|---|---|---:|---:|---:|
| `SA15_…FINAL_CONTROLLED_V2` | `E2E-01`…`-18` | `0` | `0` | `1` |
| `SA17_…FINAL_CONTROLLED_V2` | Pre-Test handoff baseline | `0` | `0` | `2` |
| **`SA_CORR5_10_22_SCENARIO_FINAL_RECONCILIATION`** | **`X-01`…`X-22` dimension grades — the register that defines the `22`** | **`2`** | **`2`** | `1` |

> **The claim as published is FALSE against the third register.** Corrected statement:
>
> **`VAT` and `WHT` are absent from both end-to-end scenario registers and appear twice each in the
> 22-scenario dimension register — in both cases as statutory period references inside `S` markers
> (`XMC-C-A16`'s VAT/WHT return-period interaction; `DESTRUCTION_FOR_TAX`), never as a scenario carrying
> a tax determination.**
>
> **`PT-S-01` stands** — no scenario carries a statutory tax determination — **on a corrected measurement
> with a named path set. The `48` denominator is unchanged.**

---

## 5. Package-integrity corrections

| ID | As published | **Corrected** |
|---|---|---|
| `B7-F-15` | `25_` §1: manifest has *"`23` entries"* | **`24` entries**, verifying `24 of 24 OK` with a firing positive control |
| `B7-F-16` | `23_` §5: *"Artefacts `24` — `01_`…`23_` + manifest"* | the manifest's `24` entries are **`01_`…`23_` + `25_`**; `23_` §5's `24` is `01_`…`23_` + the manifest. **Two different sets of the same size.** The `CORR1` manifest (`37_`) lists its own membership explicitly to prevent the recurrence |
| `B7-F-17` | `22_` §8: *"Total **`5` denominators**"* | **`6` distinct denominators moved across `5` rulings** — boundary, veto, open Boss decisions, `PTX`, `IR`, `AR`. Unit stated ≠ unit counted |
| `B7-F-18` | `23_` §6: *"`5` moved on rulings, `8` did not"* | **`6` moved, `7` did not** — the veto count moved `6 → 7`; *"`YES (count only)`"* is still moved |

**`0` originals edited. All four remain Audit Lineage; this section supersedes them.**

---

## 6. Checkpoint

> **`17` denominators restated, **every one with named membership** · readiness **`18/4/0`** ·
> **open Boss decisions corrected `1 → 3`** — `SC-SMT-01` was an obligation that was always a decision ·
> exit conditions **`7 of 17`** · `B7-F-14`'s measurement restated with a declared path set and `PT-S-01`
> preserved · `4` integrity corrections applied · **`EC-04 0/3`, `EC-07 0/2`, `0 of 48`, `0 of 11`,
> `7` vetoes `0` discharged, `0 of 22` verified — ALL UNCHANGED.**
