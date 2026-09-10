# 06 — PRODUCT CLASSIFICATION TIE-BREAK

## `BOSS DECISION ITEM PREPARED — NOT SELF-APPROVED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-CORRECTIVE-CLOSURE-001]` · Boss: **SOLE FINAL APPROVER**

> **§9: *"Do not create semantics unsupported by the approved architecture. If a Boss ruling is required,
> prepare a precise Decision Item. Do not self-approve it."***

---

## 1. The defect, at primary text

`X-18` (`SA_CORR3_06`), verbatim:

> **`STRUCTURAL`** — ***"two-axis classification tie-break undefined; `BD-ACC-01` presumes a physical fact
> and is silent for services."***

**Two axes exist and their precedence is undefined:**

| Axis | What it decides | Authority |
|---|---|---|
| **Axis 1 — product KIND** | storable / consumable / service | `HX-28`: *"product kind as a business fact (goods against service)"* |
| **Axis 2 — product CATEGORY** | **valuation policy, values and method version** | **`BD-ACC-03A`/`03B` — RULED, Product Category owns it** |

> **When the two disagree — a service in a category carrying a valuation policy, or a consumable in a
> stocked category — nothing states which wins.**

---

## 2. Per-classification state

| Classification | Inventory applicability | COGS applicability | Accounting authority | State |
|---|---|---|---|---|
| **Storable / Goods** | full | **at the physical movement** (`JT-04` RULED) | `BD-ACC-01` + `BD-ACC-03A` | **DEFINED** |
| **Raw material** | full | consumption → WIP | `X-16` | **DEFINED as a route**; **overhead injection path absent** (`R-22`) |
| **WIP** | full | accumulation | `X-16` | **DEFINED as a route**; **no variance mechanism, `1 of 9`** |
| **Finished goods** | full | FG receipt → COGS on delivery | `JT-04` RULED | **DEFINED** |
| **Consumable** | movement, **immediate expense** | expense, not COGS | `X-18` | **PARTIAL** — the kind is named; the tie-break with Axis 2 is not |
| **Expense / non-stock** | none | expense | `E2E-10` | **PARTIAL** |
| **SERVICE** | **see §3** | **see §3** | **`BD-ACC-01` IS SILENT** | **UNDEFINED** |

---

## 3. Service — the six proofs §9 demands

| # | Question | What evidence establishes | Verdict |
|---:|---|---|---|
| 1 | **Inventory applicability** | `E2E-08` produces *"a recognition event **with no stock movement**"*; `IR-17` *consumption by a service or project* is **`PARTIAL`** | **NO stock movement on the sell side; the consumption side is `PARTIAL`** |
| 2 | **COGS applicability** | **`ND-09`** — a cross-module fulfilment producing revenue **must** produce a cost recognition bound to the same identity **or an explicit recorded determination that it does not** | **NOT DETERMINED.** `ND-09` demands one of two outcomes and **neither has been recorded for services** |
| 3 | **Delivery semantics** | `XMC-C-C2` specifies **asserter, time, basis, obligation**; the trigger is *"a human assertion with no independent operational event"* | **DEFINED — and it rests on a human assertion**, carried as a bounded risk |
| 4 | **Invoice-policy interaction** | `E2E-08` routes Service → completion evidence → AR; `SA17` records required inputs as **none** | **DEFINED at route level** |
| 5 | **Accounting treatment** | **`BD-ACC-01` presumes a physical fact and is SILENT for services** | **UNDEFINED — the core defect** |
| 6 | **Classification authority** | `BD-ACC-03A` gives **Product Category** the valuation policy; `HX-28` makes **product kind** a business fact | **TWO AUTHORITIES, NO PRECEDENCE** |

> **`3 of 6` defined, `1` defined-with-risk, **`2` undefined** — and the two undefined ones (accounting
> treatment, classification authority) are exactly what Functional Design would have to invent.**

---

## 4. What SMEs Core may and may not do here

| | |
|---|---|
| **May** | state the defect, enumerate the axes, name the authorities, prepare the decision |
| **May NOT** | choose the precedence. **`BD-ACC-01` and `BD-ACC-03A` are both `CLOSED / BOSS APPROVED` and *"not re-openable"*. Deciding which governs a case neither anticipated is a Boss act** |
| **Rejected option** | inferring the rule from the reference system — `PT-10` §5 records `0` such inferences and this round adds none |

---

## 5. `DECISION ITEM CC-D-01` — prepared for Boss

```
CC-D-01  PRODUCT CLASSIFICATION TIE-BREAK AND SERVICE ACCOUNTING TREATMENT

QUESTION (two parts, one principle):

 (a) PRECEDENCE. When product KIND (storable / consumable / service) and product
     CATEGORY (BD-ACC-03A valuation policy) imply different accounting treatment,
     which axis governs?

       Option 1  KIND governs; CATEGORY supplies policy only where KIND admits valuation.
       Option 2  CATEGORY governs; KIND is descriptive.
       Option 3  KIND governs admissibility, CATEGORY governs measurement — with an
                 explicit refusal rule where CATEGORY carries a policy KIND cannot use.
       Option 4  Another boundary Boss states.

 (b) SERVICE under ND-09. ND-09 requires a cross-module fulfilment producing revenue
     to produce EITHER a cost recognition bound to the same identity OR an explicit
     recorded determination that none arises. For services, neither exists.

       Option A  Services produce a bound cost recognition (from IR-17 consumption).
       Option B  Services carry a RECORDED DETERMINATION that no cost recognition arises.
       Option C  Split by whether IR-17 consumption occurred.

WHY BOSS: BD-ACC-01 (CLOSED / BOSS APPROVED, not re-openable) is silent for services;
BD-ACC-03A (RULED) assigns valuation authority to Product Category. Choosing between
two standing Boss rulings for a case neither addresses is not a SMEs Core act.

SMEs Core RECOMMENDATION: NONE OFFERED.
Preparing a recommendation would require selecting between two closed Boss rulings.
Boss may direct SMEs Core to produce one.

BLOCKS: X-18, E2E-08, PT-S-01 expected values, and Functional Design entry (PT-16 §1 item 5).
```

---

## 6. Checkpoint

> **`7` classifications assessed · Service tested on all `6` required proofs: **`3` defined, `1` with a
> named risk, `2` UNDEFINED** · the undefined pair is precisely *accounting treatment* and *classification
> authority* · **`CC-D-01` prepared as a precise Boss Decision Item with `0` SMEs Core recommendation**,
> because recommending would mean choosing between two standing, non-re-openable Boss rulings ·
> `0` semantics invented.**

