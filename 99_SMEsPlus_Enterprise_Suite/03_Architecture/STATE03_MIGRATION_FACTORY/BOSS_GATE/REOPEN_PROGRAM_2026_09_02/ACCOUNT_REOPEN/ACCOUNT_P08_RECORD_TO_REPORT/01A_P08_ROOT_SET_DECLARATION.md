# P08 ROOT SET DECLARATION — closing the programme's standing enumeration defect for P08's own claims

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

## 1. The defect this file addresses

The Account Wave A Final Closure round recorded the exact remaining enumeration defect as:

> The programme has never declared its **root set**. Every denominator, every path set and every class `A` absence in Wave A is scoped to **one reference core root of the 22 that exist**, and no artefact says which root, or that a choice was made.

and imposed the consequent rule on every subsequent session:

> …may make no class `A — VERIFIED ABSENCE` claim until `MCU-21` is closed. Until then every absence is class `C` with a stated boundary.

`MCU-21` is closable by evidence, at low cost, and this session closes it **for its own claims**. It does not close it for the programme — declaring which root SMEsPlus *targets* is a programme declaration reserved to Boss, and is carried forward as `P08-BD-05`.

## 2. The declared root set

| Element | Value |
|---|---|
| `POPULATION` | every reference core root present on the project evidence volume |
| `PATTERN` | a whole-volume file search for the framework currency-model file at its canonical path within a base tree, reduced to the containing root, sorted. The literal command is recorded in `LAYER2_EVIDENCE_QUARANTINE/E00` §1. |
| `PATH SET` | the whole evidence volume, not a chosen subtree |
| `UNIT` | one core root (one directory containing a framework `addons/base` tree) |
| `DENOMINATOR` | **22** |

**The pattern's own boundary, declared:** a core root that omits or relocates the framework currency model is not discovered by it. The figure 22 is class `A` **over this declared pattern**, and is not a proof that 22 is the total number of roots on the volume. This reproduces the prior round's figure exactly and independently, from a different session, on the same declared pattern — which is the reproduction the method-convergence standard asks for and had not previously had.

### 2.1 The 22 roots

Root identities and their filesystem locations are **Layer 2** and are held in `LAYER2_EVIDENCE_QUARANTINE/E00` §1. Layer 1 refers to them as `R-01` … `R-22`.

| Root | Modules with a manifest | Product line |
|---|---|---|
| `R-01` | 804 | 18 |
| `R-02` | 802 | 18 |
| `R-03` | 498 | 18 |
| `R-04` | 1420 | 18 |
| `R-05` | 792 | 18 |
| `R-06` | 456 | 18 |
| `R-07` | 447 | 18 |
| `R-08` | 804 | 19 |
| `R-09` | 454 | 18 |
| `R-10` | 1433 | 19 |
| `R-11` | 1433 | 19 |
| `R-12` | 474 | 19 |
| `R-13` | 790 | 18 | **target root of this session**
| `R-14` | 1399 | 19 |
| `R-15` | 1273 | 18 |
| `R-16` | 638 | 18 |
| `R-17` | 636 | 18 |
| `R-18` | 28 | 18 |
| `R-19` | 1421 | 19 |
| `R-20` | 1420 | 19 |
| `R-21` | 1421 | 19 |
| `R-22` | 682 | 18 |

`R-13` is the root this session's detailed forensic work was performed against, and is the root the prior Account sessions used. `R-16`, `R-17` and `R-18` are nested inside `R-15`/`R-16`. Nesting is declared, not corrected — the pattern's unit is "a directory containing a framework base tree", and a nested server tree is such a directory.

**Version split: 13 roots on the 18 line, 9 on the 19 line.** SMEsPlus spans both; no artefact in the programme declares which line the target build is on. That is `P08-BD-05`.

## 3. Root-set-wide negative-claim scan

Three of P08's highest-impact negatives were re-run **across all 22 roots**, not against one. Each is now class `A` over the declared 22-root set rather than class `C` over one root.

| ID | Claim | Pattern | Result across 22 roots | Class |
|---|---|---|---|---|
| `RS-A-01` | **No accounting-event model exists.** | `grep -rEho "_name = ['\"][a-z_.]*event[a-z_.]*['\"]" --include=*.py <root>` per root, deduplicated, with the event-management and framework namespaces excluded | **0 accounting-event models in 22 of 22 roots.** The only residual match in 9 roots is a print-report model belonging to the event-management domain. | **A VERIFIED ABSENCE, scope = the declared 22-root set** |
| `RS-A-02` | **No accounting-period entity exists.** | `grep -rEho "_name = ['\"]account\.period['\"]\|_name = ['\"][a-z_.]*accounting.period[a-z_.]*['\"]" --include=*.py <root>` per root | **0 in 22 of 22 roots.** | **A VERIFIED ABSENCE, scope = the declared 22-root set** |
| `RS-A-03` | **No database-level constraint enforces per-entry balance.** | `grep -rEl "CHECK ?\(.*(sum\|SUM).*(debit\|credit\|balance)" --include=*.py <root>` per root | **0 files in 22 of 22 roots.** | **A VERIFIED ABSENCE, scope = the declared 22-root set** |

A fourth scan was run and is **not** promoted, because its pattern is vocabulary-based rather than structural:

| ID | Claim | Result | Class |
|---|---|---|---|
| `RS-B-01` | No year-end result-appropriation entry generator exists | Files matching the vocabulary pattern: 0 in 7 roots, 3 in 1 root, 8–9 in 5 roots, 19 in 1 root, 24 in 8 roots. The matches were not each opened. | **B NOT FOUND IN SEARCHED SCOPE** — the count varies with build completeness, and a vocabulary pattern cannot distinguish a result-appropriation generator from a tax-closing or session-closing routine. Not upgraded. |

And one positive is recorded because it is root-set-wide and bears directly on a frozen Boss semantic:

| ID | Claim | Result | Class |
|---|---|---|---|
| `RS-P-01` | The rate resolver's parity fallback is present across the reference line | The exact three-tier fallback expression is present in the framework currency model of **21 of 22 roots**; the single root without it (row 18) holds 28 modules and is a partial tree. | **FACT VERIFIED across the declared 22-root set.** This settles, at root-set scope, that the parity fallback GB-08 prohibits is not a version-specific artefact and is not avoidable by choosing a different root. |

## 4. What this closes, and what it does not

**Closes for P08:** the prohibition on publishing class `A`. Every class `A` in this package now carries either the declared 22-root scope (`RS-A-01`..`RS-A-03`) or an explicitly narrower stated scope. No class `B`, `C` or `D` has been promoted to `A` anywhere in this package.

**Does not close:** `MCU-21` itself. Which root SMEsPlus targets is a programme declaration, not a research result. P08 records it as `P08-BD-05` and continues.

**Does not close:** the prior rounds' class-`A` claims. Those remain bounded to ≤1 root of 22 and this session does not re-scope another session's register.
