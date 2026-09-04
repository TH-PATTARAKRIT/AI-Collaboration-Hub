# 06 — ACCOUNT WAVE A — UNKNOWN CLASSIFICATION REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room
Required by `SMEPLUS-DR-MC-001` §9 output 5 · governs `MC-06`

---

## 1. The parent count of 41 does not reconcile

`G10` §4 records *"Remaining unknown count: **41** = 31 carried from `C13` §6, less 4 closed, plus 14
newly opened."* The arithmetic is sound (31 − 4 + 14 = 41). **Every input term fails verification:**

| Term | Finding |
|---|---|
| "31 carried from `C13` §6" | **CONTRADICTED.** `C13` §6 holds **8 rows / 14 items**. The figure originates at `C10`, which attributes it to *"`C13` §6 **plus the gap register**"* — `G10` dropped the second half of its own source |
| 31 reconstructible from any package table | **NOT PROVEN.** Register `21`'s own count table totals **28**; 28 + `C13` §6's 7 non-Thai items = 35. No combination yields 31 |
| "less 4 closed" | **CLASSIFICATION ERROR.** The 4 are `SB-05`, `FX-08`, `FX-07`, `B-05`. `G10` §2 records all four as **confirmed defects** promoted to blockers `GB-01`…`GB-03`. Netting a promoted defect out of the open-unknown count moves it in the gate's favour |
| "plus 14 newly opened" | **NOT PROVEN.** No file enumerates 14 new unknowns; `G06`, `G09`, `GR1`, `GR2` carry theirs in prose only |
| Register `21` completeness | **CONTRADICTED.** **5 orphan ids** — `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03` — are cited in files `01`–`26` and have **no row** in the register (`GAP-H01` does appear) |

**Independent enumeration this round yields ≥53 open unknowns by id, plus 4 wrongly netted out.
41 is understated and was never enumerated.** The population `P-25` is therefore `HOLD`, and this
register is the first enumeration of it.

## 2. Classification

Classes per the round instruction. `GATING` = Wave A cannot pass a research gate while it stands.

### 2.1 `GATING` — must close or the gate stays on `HOLD`

| id | Unknown | Why gating | Source |
|---|---|---|---|
| `MCU-01` | Whether the control-suppression flags are externally reachable | Governs the severity of the entry-balance tolerance-zero item; needs an **executed test** | `21`, `C09` |
| `MCU-02` | No general accounting-event identity or provenance carrier | Ledger identity; Boss design decision | `21`, `G06 RS-01` |
| `MCU-03` | Event identity and idempotency model | As above | `21` |
| `MCU-04` | **Report definitions carry no company dimension** | Verified **adversely** as a cross-tenant defect by the final review, yet still carried as a *medium* open unknown, not as a defect | `C13`, `GR2` |
| `MCU-05` | **A reviewer-declared tolerance-zero candidate that left no trace** — cross-company rate resolution in raw SQL, outside every record rule, with an undeclared par fallback | Registered by the final reviewer as a `Tolerance = 0` candidate; appears in **no** blocker, **no** tolerance-zero list, and **no** file outside the review that raised it | `GR1` |
| `MCU-06` | Rate-precedence inference (ordering of null vs own-company rows) never executed | **Load-bearing** for the severity of the null-company crossing; labelled `INFERENCE` on both sides | `GR1`, `MCE-007` |
| `MCU-07` | Whether shipped or localization data contains null-company rate rows | Decides whether the crossing is reachable **out of the box** | `GR1` |
| `MCU-08` | Whether the module carrying the approval engine is in the SMEsPlus reference baseline | Decides the scope of the approval-bypass finding | `GR1` |
| `MCU-09` | Whether a null-company tax-repartition row is reachable | Would carry a tax split **and an account** across companies | `GR2` |
| `MCU-10` | Lock-exception creation path — a lock-control object with **no record rule** | Control over the control | `GR2`, `MCE-004` |
| `MCU-11` | Report company scope is a caller-supplied parameter with no defence in depth | Violates the package's own readiness criterion 3 | `GR2` |
| `MCU-12` | **58.1% of the package has never had the negative-claim control applied** | Method-gating; `MC-05` | `MCE-011`, file `07` |
| `MCU-13` | **`FX-08` requires targeted re-verification** against a model-level constraint that forbids branch-scoped rate rows — a constraint **no round enumerated** | `FX-08` is one of the four blockers reported **closed with evidence** and is the basis of `GB-03` | `MCX-02` |
| `MCU-14` | **Wrong opening provenance** — taxonomy class with zero instances, never searched | Squarely Wave A; opening balances interact with merge-driven history rewrite | file `08` |
| `MCU-15` | **Wrong reversal lineage** — taxonomy class with zero instances, never searched | Squarely Wave A; reversal linkage is optional and severable | file `08` |
| `MCU-16` | **The exposure surface is 192 sites in three mechanism populations, of which 9 are assessed** | This *is* `GB-04`, now quantified | file `03` |
| `MCU-17` | **No correction-propagation channel exists.** No correction from the final round reaches any Layer 1 register it contradicts | Contradicted affirmative claims stand live in the canonical artefacts at the gate baseline | file `10`, `MCE-010` |

**17 `GATING` unknowns. None is closed by this round.** Three (`MCU-13`, `MCU-16`, `MCU-17`) are
**opened** by it.

### 2.2 `NON-GATING` — real, but do not block a Wave A research gate

| id | Unknown | Why non-gating |
|---|---|---|
| `MCU-20` … `MCU-24` | Close, period and tenancy **design** questions | Boss decisions awaiting direction, not missing evidence |
| `MCU-25` … `MCU-32` | Items closable by further reading (control-account concept, equity restrictions, reconciliation detail, bootstrap docs) | Bounded, low severity, no control implication |
| `MCU-33` … `MCU-35` | Concurrency, idempotency and completeness behaviour | **Gating for control *design*; non-gating for *research*.** They require executed tests against a running system, which is outside a research round |

### 2.3 `ROUTED TO LATER WAVE` — destination named, and the routing tested

**No Wave A blocker is routed.** Each item below was checked against the rule *"does this determine
ledger identity, measurement, period control or integrity?"* — all answer no.

| id | Unknown | Destination |
|---|---|---|
| `MCU-40` … `MCU-46` | Thai statutory positions — stock report, scrap destruction, withholding, year-end statutory close | **Wave D — Tax / Localization** (`HOLD / EVIDENCE REQUIRED`, candidate names unvalidated) |
| `MCU-47` | Tax semantics carried on the journal item | **Wave D** |
| `MCU-48` … `MCU-54` | Reporting and presentation semantics — reporting classification, off-balance exclusion, statement mapping | **Wave G — Financial Reporting** |
| `MCU-55` | Accrual and deferred recognition | **Wave F — Time-Based Recognition** |
| `MCU-56` | Bank-flow semantics and dual-ingestion de-duplication | **Wave H — Payments / Banking** |
| `MCU-57` | Analytic subledger semantics | **Wave E — Management Accounting** |
| `MCU-58` | Producer-side debit/credit patterns | **Waves B and C**, plus each producing Wave |

**Routing-abuse test result — one item recovered.** `MCU-04` (report definitions carry no company
dimension) was carried as a *medium* open unknown. It had already been **verified adversely** by the
final review as a cross-tenant defect editable by any tenant's accounting manager. It is
**reclassified `GATING`** and is not routed to Wave G, because the defect is in the boundary, not in
the reporting semantics.

### 2.4 `OUT OF SCOPE WITH EVIDENCE`

| id | Item | Evidence |
|---|---|---|
| `MCU-60` | An accounting-event object distinct from the journal entry | Positively established as **absent from the reference system**; `P-18` is unbounded by construction, not by omission |
| `MCU-61` | Deployment- and hosting-layer tenancy | No tenant entity exists in the accounting domain or the company model; SMEsPlus construct, decided at architecture level |

### 2.5 `UNCLASSIFIED` — cited but absent from every register

| id | Note |
|---|---|
| `GAP-A03`, `GAP-A04`, `GAP-C01`, `GAP-G01`, `GAP-H03` | Cited in files `01`–`26`; **no row in the unknown register**. Cannot be classified because no statement of them exists. **Must be written up before the next gate** |

## 3. Summary

| Class | Count |
|---|---|
| `GATING` | **17** |
| `NON-GATING` | 16 |
| `ROUTED TO LATER WAVE` | 19 |
| `OUT OF SCOPE WITH EVIDENCE` | 2 |
| `UNCLASSIFIED` — no register entry exists | 5 |
| **Total enumerated** | **59** |
| Parent reported | 41 |

## 4. Verdict on `MC-06`

> **`MC-06` UNKNOWN CLASSIFICATION — MET for the population enumerated here; the parent count of 41
> is CONTRADICTED and was never enumerable.**

Every unknown this round could identify is classified, every routed item has a named destination, and
the one item that was hidden by routing has been recovered. But **17 `GATING` unknowns stand and none
is closed**, so the standard's rule applies without qualification:

> *"For every `GATING` unknown, close it or remain `HOLD`."*

**`HOLD`.**
