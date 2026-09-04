# 15 — UNKNOWN → DESIGN IMPACT REGISTER

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> Classification per the mandate: **blocks design · does not block design · requires later Wave ·
> requires Boss decision · requires external/statutory evidence.**
>
> *If an unknown can materially alter semantics, control, tenant isolation, financial integrity, or
> migration continuity, the affected design component remains `HOLD`.*

---

## 1. The unknown universe — and why it cannot be stated as one number

`MCC_D` established two facts that this register must carry rather than smooth over:

| # | Fact |
|---|---|
| `MCC-D-01` | The parent's `59` is **a count of allocated id slots, not an enumeration** — for 31 of the 59 no statement of the unknown exists, only a range and a shared one-line description |
| `MCC-D-02` | `41` and `59` count **two differently-keyed populations** — register `21` keys `GAP-*`/`TX-*`/`CL-*` (28 rows, reconciling exactly); file `06` introduced `MCU-*` with **no mapping to the old scheme in any file** |

> **No arithmetic reconciles them, because they are not two counts of one population.**
> This register therefore reports **by consequence, not by total**, and states
> `PERCENTAGE NOT REPORTABLE — DENOMINATOR NOT VERIFIED` where a percentage would be invented.

| Class | Count | Confidence |
|---|---|---|
| Gating unknowns at the parent's last statement | **17** | membership **almost entirely different** from the 17 it began with |
| Trajectory | **17 → 11 → 18 → 17** | **oscillating, not converging** — the parent said so itself |
| Tolerance-zero boundaries | **10 registered · 12 known** | **zero resolved.** Two returned by the parent's challenge are recorded **only in `MCC_J`, which does not exist** |
| Blockers | **8** | `GB-08` new; `GB-02` widened twice; `GB-07` widened on a new axis |
| Orphan unclassified ids | **5** | `GAP-A03` `GAP-A04` `GAP-C01` `GAP-G01` `GAP-H03` |

---

## 2. `BLOCKS DESIGN` — the component is `HOLD`

| Unknown | Component held | Why it is material |
|---|---|---|
| `GB-01` cross-company/tenant crossing | `D-33` tenant identity · `D-10` measurement scope · `12` whole file | **tenant isolation** — a `Tolerance = 0` candidate |
| `GB-02` cross-company rewrite of a posted fact | `D-31` · `CB-05` · `T-05` class | **financial integrity** — widened twice, most recently to admit cross-branch reconciliation, exchange posting and a raw-SQL settlement write |
| `GB-03` null-company rate row | `D-10` · `T-01` class | **semantics + isolation** — 6 resolvers admit it, 6 refuse it; creatable by a routine accounting role; **widened again on the version SMEsPlus targets** |
| `GB-04` / `MCU-16` exposure | `D-34` · every isolation claim | **9 of 192 assessed (4.7%)**, over a path set short by 962 modules |
| `GB-07` / `MCU-18` unsearched module tree | `D-01` `D-04` `D-23` | **every whole-tree negative claim in the programme is scoped to the primary tree only.** Three `PROVISIONAL`/`PROVISIONAL` designs rest on class-`B` negatives |
| `GB-08` / `MCU-20` v19 instability | `D-30` · **all of file `10`** | **semantics** — v19 adds an 11th resolver outside every record rule, converting at *today*, with a 4th fallback |
| `T0-07` rate fallbacks | `D-09` (strengthens, does not block) | 4 distinct fallback semantics, 8 raw-SQL reads, 3 modules |
| `T0-08` entry identity | `D-14` `D-26` `JR-05` `L-5` `T-18` | **integrity** — empty constraint definition, journal-scoped index, log-line degradation, number-blanking escape |
| `T0-09` declared-but-non-executing controls | `D-32` `T-16` | **control** — 16 declarations **present in the view layer, absent at write**; population floor **30 across 4 files**, 1 named; **`T0-09` is NOT bounded** (`G-C6`, `G-C7`); `CR-07` |
| `T0-10` lock exception | `D-08` `D-27` · `11 §5` | **control** — the control over the lock has no record rule, caller-supplied company, revocation on group membership alone |
| `MCU-04` + `MCU-11` report scope | `L-9` `T-19` | **reporting integrity** — no company dimension; caller-supplied scope with no defence in depth |
| `MCU-01` suppression reachability | `D-02` `T-07` | **immutability** — and `G-C5` contradicts the "only consumers" scope: **seven** consumers across two modules, one performing a **period reassignment on a posted deferral reversal** |
| `MCU-19` migrated rate rows | `D-35` | **migration continuity** — *"one `SELECT` answers it"*, unrun |
| `MCU-33/34/35` concurrency, idempotency, completeness | `D-24` · `03 §5` | **identity** — the source *states* the behaviour statically: unmet uniqueness condition → *"sequence numbers may not be unique"* |

**14 unknowns hold 20 design components.**

---

## 3. `REQUIRES BOSS DECISION` — not a research gap

| Item | Question | Held component |
|---|---|---|
| `GB-01` | Is the tenant boundary above the company group, or is the company group the tenant? | `D-33` |
| `D-22` | Does SMEsPlus post a year-end result transfer, or derive the result at report time? | `11 §6` |
| `CL-05` | Does a parent's irreversible lock cascade to subsidiaries? | `CB-03` |
| `D-28` | Is each dimension a **fact** (immutable, part of the event) or an **attribution** (restatable)? | `04 §4` |
| `GAP-E01` | Write-off policy semantics | `08 §3` |
| `MCU-08` | Is the approval engine in the SMEsPlus module baseline? | `D-25` |

**Six decisions. None is answerable by more research**, and four of them gate design components
directly. This is the highest-value list in the package for Boss.

---

## 4. `REQUIRES LATER WAVE`

| Item | Wave | Wave A obligation retained |
|---|---|---|
| Tax point content and tax-period semantics | `WAVE-D TAX` | **Wave A must carry the tax-point field** (`09 §1`) — the carrier is Wave A's, the content is not |
| Statutory extracts, Thai localisation | `WAVE-D TAX` | boundary only |
| Consolidation translation | `WAVE-G REPORTING` | derived-rate model retained (`FXD-01`) |
| Bank-flow semantics | `WAVE-H` | **mechanism stays in Wave A** — `MCU-56` split, and `G-C5` widened it: **seven** suppression consumers across two modules, one reassigning the period of a posted deferral reversal — Wave A's problem |

---

## 5. `REQUIRES EXTERNAL / STATUTORY EVIDENCE`

| Item | Status |
|---|---|
| Thai VAT tax-point rules driving field 4 of `09 §1` | `HOLD / EVIDENCE REQUIRED` — routed to the Accounting-Tax track per standing clean-room rules |
| Retained-earnings statutory treatment | `HOLD / EVIDENCE REQUIRED` |
| Whether statutory retention obliges tamper-evidence to survive migration | `HOLD / EVIDENCE REQUIRED` — bears on `D-14` |

**All three are `UNVALIDATED` and none is used as design authority anywhere in this package.**

---

## 6. `DOES NOT BLOCK DESIGN`

| Item | Why it does not block |
|---|---|
| `GAP-S01` template rollback | The rollback design is invention either way; absence of a reference mechanism changes nothing |
| `GAP-H02` rate-correction traceability | `FXD-06`/`FX-07` state the requirement; the reference's behaviour is not needed |
| `MCU-19b` pre-v18 baseline constraint | class `C`, and **must never be reported as "the constraint has always existed"** |
| Delivery-date behaviour | class `B`; the design carries the field regardless |

---

## 7. Orphan ids — a defect of the register itself

`GAP-A03` `GAP-A04` `GAP-C01` `GAP-G01` `GAP-H03` are cited across files `01`–`26` but are
**unclassified in the unknown register**.

Two of them are load-bearing here:

| Orphan | Bears on | Consequence |
|---|---|---|
| `GAP-A03` comparative reporting across a chart change | `D-21` temporal validity | a `PROVISIONAL` design rests on an unclassified unknown |
| `GAP-G01` who closed, when, on what basis | `D-06` close artefact · `L-10` | the question *"can the ledger say who closed the period?"* has never been classified |

**Classifying the five orphans is the cheapest open item in the whole package** and it is not on the
parent's stated worklist.
