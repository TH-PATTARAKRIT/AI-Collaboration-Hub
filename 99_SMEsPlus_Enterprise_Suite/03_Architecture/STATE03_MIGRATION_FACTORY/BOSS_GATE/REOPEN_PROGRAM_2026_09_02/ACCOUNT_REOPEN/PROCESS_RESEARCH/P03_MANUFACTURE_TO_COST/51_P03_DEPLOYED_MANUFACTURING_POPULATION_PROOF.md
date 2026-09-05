# 51 — DEPLOYED MANUFACTURING POPULATION PROOF

**LAYER 2 — AUDIT QUARANTINE.** All evidence read-only. Reproduction:
`evidence/P03R_EXECUTED_OUTPUT.txt`, `evidence/pop.py`, `evidence/val.py`.

---

## 1. Declared enumeration

| Element | Declaration |
|---|---|
| **POPULATION** | Every PostgreSQL dump ≥1 MB under `/Volumes/iMacSys` and `~/Downloads` |
| **PATTERN** | `find … \( -name "*.dump" -o -name "*.sql.gz" -o -name "*.backup" \) -size +1M`, then per-table `COPY`-block row counts |
| **PATH SET** | those two roots |
| **UNIT** | one database dump file; within a database, one table row |
| **RESULT** | 4 distinct databases, **4 now readable** (was 3) |

## 2. The four databases

| Database | MOs | Work centres | Routing ops | Work orders | Time logs | Companies | Modules |
|---|---|---|---|---|---|---|---|
| **`iSMEs`** | **10,764** | 0 | 0 | 0 | 0 | 1 | 190 |
| **`iTEST02`** | 163 | **60** | **154** | **204** | **27** | 1 | **453** |
| `BK12MAY26` | 0 | 0 | 0 | 0 | 0 | 44 | 251 |
| `iEVING` | 0 | 1 BOM | 0 | 0 | 0 | 44 | not read |

## 3. Verification of the round-3 headline claim

Round 3 asserted: *9,807 completed MOs, material cost present, zero work centres, routing
operations, work orders and time logs.* Re-derived:

| Claim | Verified? | Evidence |
|---|---|---|
| 10,764 MO rows | **YES** | enumerated |
| 9,807 in state `done` | **YES** | `done 9807, cancel 873, confirmed 54, draft 22, progress 2, to_close 6` |
| single company | **YES** | `{'1': 10764}` |
| zero work centres / routing / work orders / time logs | **YES for `iSMEs`** | all four tables empty |
| **"material cost present"** | **PARTLY — and it was an inference, now measured** | §4 |
| date range | **NOT SUPPORTED** — `date_start` is **null on all 10,764 rows**; the valuation ledger spans 2023-10-03 → 2026-07-11, a different measure | §5 |

## 4. Correcting "material cost present" — it was inferred, not measured

Round 3 counted valuation rows and inferred material cost reached the orders. Measured:

| Measure | Result |
|---|---|
| done finished moves | 13,284 |
| …**with** a valuation layer | **13,235** — so **49 done finished moves carry no valuation at all** |
| …with a **non-zero** valuation | **13,004** — so **280 carry a zero value** |
| done raw moves | 30,067 |
| …with a valuation layer | **28,681** — **1,386 consumption moves carry no valuation** |

> **`P03R-F-02`. "Material cost present" is true in aggregate and false in detail.** 49 of
> 13,284 completed finished-goods moves have **no valuation record**, and 280 more are
> valued at **zero**. On the input side 1,386 of 30,067 component consumptions are
> unvalued. `FACT VERIFIED`.

Round 3's claim was an inference stated as a measurement. Recorded as `RE-P03-16`.

## 5. The date range that cannot be stated

`mrp_production.date_start` is **null on every one of the 10,764 rows**. The MO date range
therefore cannot be derived from that column. The valuation-ledger range
(2023-10-03 → 2026-07-11) is a **different measure** and is not substituted for it.

Recorded rather than quietly replaced — `smeplus-executed-not-quoted-rule`.

## 6. Configuration and version

| Attribute | `iSMEs` | `iTEST02` |
|---|---|---|
| Valuation table present | yes — 74,982 rows | **no `stock_valuation_layer` table** |
| Manufacturing accounting | `mrp_account`, `mrp_account_enterprise` | both, **plus** work-order, HR-account, project, accountant, subcontracting |
| Work-order module | **absent** | present |
| Implication | conversion cost **cannot** post | conversion cost **can and does** post |

`iTEST02`'s missing valuation table indicates a **different schema generation** from
`iSMEs`. The two are not the same product version, and no finding is carried between them
without saying so. Recorded as `UNR-P03-11`.

## 7. Conclusion

> **The deployed population does not support a single statement about "the deployment".**
> One database manufactures at scale with the conversion-cost apparatus absent; another has
> it fully installed and lightly used. Any P03 conclusion must name which.
