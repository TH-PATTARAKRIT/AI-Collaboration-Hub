# 59 — DENOMINATOR / COUNT REPAIR

**LAYER 2 — AUDIT QUARANTINE.**

Every count below states **UNIT · POPULATION · QUERY · RESULT · SOURCE**. Counts are not
compared until their units match.

---

## 1. The machine-cost monetisation counts — final reconciliation

| Unit | Population | Query | Result | Source |
|---|---|---|---|---|
| **U1** writer of inventory **conversion**-cost value | declared source root | functions writing FG/WIP carrying value from conversion cost | **2** | P03 `01` §3 |
| **U1′** writer of inventory value, **all** cost types | same | as above, materials/landed/by-product/unbuild included | **8** | P03 `28` §2 |
| **U2** monetisation path — own rate **or** driver **or** destination ledger | 6 modules | P04's declared sweep | **7** | **P04 branch** `06` §2.3 |
| **U3** posting artefact | same | separates valuation write from standalone entry | **9** | P04 `06` §2.3 |
| **U4** monetary computation | same | one arithmetic result | **6** | P04 `06` §2.3 |
| **U5** cost-injection mechanism, all cost types | declared source root | `28` §1 | **15** | P03 `28` |
| **U6** mechanism **live** in a deployment | 4 databases | reachability measured | **`iSMEs` 4 · `iTEST02` not separately enumerated** | `28` §3, `52` |

**`9` was never P04's figure under its own declared unit.** P04's message said nine; P04's
branch says **seven**, corrected under independent challenge before P03 cited it. P03 cited
the message. `RE-P03-11`, recorded in `22` §6 and unchanged.

## 2. The defect-population counts

| Unit | Population | Query | Result |
|---|---|---|---|
| `DC-*` defect ids | files `05`, `25` | `grep -oE '\`DC-[0-9]+\`' \| sort -u \| wc -l` | **15** |
| Exposure classes | the 15 above | `53` §1 row by row | **LIVE 5 · LATENT 7 · UNREACHABLE 2 · UNKNOWN 1 = 15** |
| Runtime findings `P03T-F-*` (round 3) | rounds 3 files | grep | **7** |
| Runtime findings `P03R-F-*` (round 4) | rounds 4 files | grep | enumerated in `23` |

## 3. The deployed-population counts

| Unit | Population | Result |
|---|---|---|
| database dump file | `/Volumes/iMacSys` + `~/Downloads`, ≥1 MB | **4 distinct, 4 readable** |
| MO row | `iSMEs` | 10,764 (done 9,807) |
| MO row | `iTEST02` | 163 (done 8) |
| work-centre row | `iSMEs` / `iTEST02` | **0 / 60** |
| work-centre row with no company | `iTEST02`, 60 rows | **0** |
| valuation row | `iSMEs` | 74,982, of which **30** corrupt |

## 4. Units that must never be mixed — recorded because two already were

| Confusion | Where it happened |
|---|---|
| **conversion**-cost writers (2) vs **all** inventory-value writers (8) | `27` §3 vs `28` §2 — flagged inline at the time, correct |
| a defect counted in two exposure classes | `53` §2 first draft — **caught pre-publication**, `RE-P03-17` |
| P04's message count (9) vs its branch count (7) | `25` §2 — **published wrong**, `RE-P03-11` |

## 5. Standing rule, restated and now enforced

> Every count states its unit **in the same sentence as the number**, and every register
> total is produced by running a query over the register, never by adding remembered
> subtotals.

`60` is the control that enforces it. It found one error in this round before publication.
