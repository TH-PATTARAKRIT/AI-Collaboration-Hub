# MCC_00 — CANONICAL FIGURES REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room

> ## THIS FILE IS THE SINGLE SOURCE OF TRUTH FOR EVERY PUBLISHED FIGURE IN THIS PACKAGE.
>
> **Where any other file in this package states a figure that differs from a row below, THIS FILE
> GOVERNS.** No other file is edited to match; per `DR-NC-06` the superseded text stands, and the
> difference is visible.
>
> **Why this file exists.** The independent audit panel found that this round's own last correction —
> the closure of `MCU-15` — was appended to two files and not propagated to three others, so the
> package simultaneously published two closure counts, two case floors, and two contradictory
> dispositions of one id. **That happened in the round that specified the correction-propagation rule,
> hours after specifying it, while propagating its own correction.** It is recorded as `J-16`.
>
> **The lesson is not "try harder".** It is that `ER-CORE-3` must be executed by a **mechanism**, and
> a single governing register that every consumer resolves against is the cheapest mechanism there is.
> This file is that mechanism, created in response to the finding, and it is proposed to the standard
> in `MCC_K` §4 clause 6.

---

## 1. Counts

| Figure | **CANONICAL** | Superseded values still standing in the package, and where |
|---|---|---|
| Gating unknowns **closed by this round** | **9** | `8` — `MCC_E` §6, `MCC_H` §2 |
| Gating unknowns closed, as a proportion | **9 of 17 (52.9%)** | `8 of 17 (47.1%)` — `MCC_E` §6 |
| **Standing** gating total after all passes | **17** | `18` — `MCC_D` §7.5 (superseded by `MCC_D` §8) |
| Balanced-but-wrong **classes searched** | **19 of 19** | `18 of 19` — `MCC_G` §2 row *wrong reversal lineage*, §6 |
| Balanced-but-wrong register floor, **established under `MCC_G` §1's own four-question test** | **32** | `35` — `MCC_G` §6; `36` — `MCC_G` §7 |
| Balanced-but-wrong register floor, **asserted** (test not applied to 4 cases) | **36** | — |
| Tolerance-zero boundaries | **12** | `10` — `MCC_G` §4, `MCC_D` §7.3, `ACCOUNT_WAVE_A_MCC_MASTER_RECONCILIATION` §5 |
| Tolerance-zero boundaries **resolved** | **0** | — |
| Rate-table surface | **20 files** | `14` — `MCC_B` §3.2 first pass (self-corrected in the same section) |
| Rate-table company-scoping **sites** | **14** | — |
| Rate-table company-scoping **distinct expressions** | **12** | — the unit differs, not the population; see `MCC_E` `MCC-E-03` |
| Rate-table **record-rule-bypassing READ** sites | **10** | `8` — `MCC_C` §8, `MCC_E00` `MCC-E-005`. 8 raw-SQL **plus 2 elevated ORM readers** |
| Configuration keys in the accounting addon | **7 keys / 10 call sites** over the **whole addon**; **6 keys / 8 sites** over `models/`+`wizard/` | `6, complete` — `MCC_E` §3.1, `MCC_E` §4. **3 material either way** |
| `set_param` sites in the accounting addon | **1** | `zero` — `MCC_E` §3.1 |
| Modules **outside** the primary addon tree | **962 manifested** (959 archive + 3 directly under the source root) | `961 directories` — `MCC_B` §3.2, `MCC_E00` `MCC-E-000` |
| Localisation modules — **primary tree** | **2**, both Thai | — |
| Localisation modules — **archive tree, distinct** | **454** (904 raw, **450 duplicate copies excluded by this round's own pattern**) | `904` — `MCC_B` §13 `B-2`, `MCC_E01` `MCCX-03` |
| Localisation denominator | **456** | `906` — as above |
| Thai localisation modules in the **unsearched** tree | **0** | — |
| Privilege-elevation sites (`models/`, declared pattern) | **93** | `94` — `MCC_E` §2 (self-corrected at `MCC_E` §8 `E-C1`) |
| Wave A models over the 18-file surface | **22** | `21` — inherited `P-13`, published as source-derived |
| Storage-constraint tuples, Wave A surface | **9 in 6 blocks** | `11` — inherited, still published in two parent registers |
| Migration directories, primary tree | **4** Python (+1 JavaScript test directory) | `5` — `MCC_E00` `MCC-E-010` item 9 |
| Migration directories, archive tree | **70**, searched by the challenge, **conclusion holds** | not stated — `MCC_E00` bounded to the primary tree while `MCC_F` `F-03` asserted "every root" |
| `MC-01` … `MC-10` | **8 not met · 2 partially met · 0 met** | — |

## 2. Dispositions

| id | **CANONICAL** | Superseded |
|---|---|---|
| `MCU-15` | **`CLOSED — VERIFIED DEFECT`** (`BW-35`) | `REMAINS GATING — HOLD`, class `C` — `MCC_D` §2, `MCC_G` §2 |
| `MCU-04` | **`CLOSED — VERIFIED DEFECT`** — `MCC_J` `J-11` | `REMAINS GATING — HOLD` — `MCC_D` §2 |
| `BW-16` | **WITHDRAWN** | — |
| `BW-28` | **WITHDRAWN**, replaced by `BW-28a` — `MCC_J` `J-01`, `J-04` | `VERIFIED DEFECT` — `MCC_G` §3 |
| `BW-35` | **`VERIFIED DEFECT`**, class `A` **over the corrected path set, on the audit panel's evidence** — `MCC_J` `J-C4` | class `A` on this round's path set — `MCC_G` §7 |
| `T0-09` | **`UNRESOLVED`, 2 instances (the 16 inert guards; the inert wizard company field), NOT bounded** | *"two bounded instances"* incl. the empty constraint definition — `MCC_G` §4. **That instance falls** — `MCC_J` `J-03` |
| `FX-08` | **`PARTIALLY VERIFIED`** | — unchanged, independently confirmed by two panels |
| `GB-03` | **`PARTIAL`** | — unchanged |

## 3. Tolerance-zero boundaries — the canonical list of 12

| id | Boundary | Status |
|---|---|---|
| `T0-01` | Entry balance | **UNRESOLVED** |
| `T0-02` | Posting without a measurement | **UNRESOLVED** |
| `T0-03` | Deletion or rewrite of a posted fact | **UNRESOLVED** |
| `T0-04` | Tenant isolation | **UNRESOLVED** |
| `T0-05` | Over-reconciliation | **UNRESOLVED** |
| `T0-06` | Cross-company rewrite of a posted fact | **UNRESOLVED** |
| `T0-07` | Cross-company rate resolution outside every record rule, with undeclared fallbacks | **UNRESOLVED** — 10 bypassing readers, **five** fallback semantics, headline instance now `BW-28a` |
| `T0-08` | Entry identity | **UNRESOLVED** — 5 of 6 claimed mechanisms verify, 1 contradicted, **2 further found**; net **understated** |
| `T0-09` | Declared-but-inert control | **UNRESOLVED** — 2 instances, **not bounded**; floor of 30 such declarations across 4 files |
| `T0-10` | Cross-company creation and revocation of the lock exception | **UNRESOLVED** — **wider than registered**: one record against a root relaxes the whole tree, for everyone, forever, from a create right alone |
| **`T0-11`** | **The entry-balance invariant is enforced in ONE currency dimension only** | **NEW — `MCC_J` `J-05`. UNRESOLVED** |
| **`T0-12`** | **The balance assertion itself is suppressible by context; 3 shipped production consumers** | **NEW — `MCC_J` `J-06`. UNRESOLVED. `unbalanced-and-posted` is reachable** |

**12 boundaries. 0 resolved. `CONDITIONAL PASS` is unavailable by rule.**
