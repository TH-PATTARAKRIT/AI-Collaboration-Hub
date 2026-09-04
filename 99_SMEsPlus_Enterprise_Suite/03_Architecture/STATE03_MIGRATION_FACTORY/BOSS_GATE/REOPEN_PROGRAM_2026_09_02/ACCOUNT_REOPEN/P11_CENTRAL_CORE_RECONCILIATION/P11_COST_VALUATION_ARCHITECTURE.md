# P11 — UNIFIED COST / VALUATION ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 6 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Position

> ## This is the most blocked layer in the system, and its blockage is **not** caused by `P01`–`P10`.
>
> Six of the fifteen unpopulated producer rows in the event-to-GL matrix are blocked here, and every
> one is blocked on a **decision that research has already been run against and failed to close**:
> `JT-01`, `JT-02`, `JT-03`, `JT-04`, `JT-05`, `JT-08`, `BLK-07`.
>
> **Ten of ten Inventory dependency areas remain `LOCKED`.** Zero of the twelve Joint decisions has
> been closed by any of the four executed COGS packages. The Joint Closure branch is a **governance
> container only — four files, no closure deliverable, no joint cross-proof, no verdict.**

## 2. The named missing inputs — why more research will not help

`SL-07` `17` §3 states the remedy precisely, and P11 endorses it without amendment:

> *"Commissioning the research again would achieve nothing; the named missing inputs are
> **business-SME input**, **Thai statutory confirmation**, and **live reference-instance access**."*

| Blocked decision | Missing input | Who can supply it |
|---|---|---|
| `JT-01` valuation-policy ownership | 8 named sub-facts, 2 requiring live-instance access | UAT + Boss |
| `JT-02` costing methods & change rules | resolution of the price-difference account-scope contradiction | Boss |
| `JT-03` continuous vs periodic | **no stable reference pattern exists across versions — imitation is unavailable** | Boss design decision |
| `JT-04` COGS at dispatch or invoice | `SME-Q-03`, `TH-NEW-01`, 2 documentation sub-facts | **Business SME — no AI may answer on the business's behalf** |
| `JT-05` return cost basis | `SME-Q-02`, `TH-NEW-02`, a live FIFO-return test | Business SME + UAT |
| `JT-08` landed cost | 3 incompatible reference behaviours, one a documented failure mode; **Audit VETO retained** | Boss |
| `BLK-07` absorption rate basis | genuinely ambiguous between two readings of `BD-02`; **only one complies with TAS 2 ¶13** | Boss |

## 3. Where the layers actually break — cross-process

| id | Break | Consequence | Class |
|---|---|---|---|
| `CV-01` | **Costing method is a company-scoped property of the product category, and the category simultaneously owns reporting, put-away and costing** | One configuration object controls three unrelated concerns across three processes. Structural root of `GAP-FS-02` | `FACT VERIFIED` (`R4-F-10`) |
| `CV-02` | **Absorption is conditional on costing method**: under standard costing, work-centre cost **never** enters finished-goods value | A design assuming machine cost reaches inventory is **silently wrong for every standard-costed product** | `FACT VERIFIED` (`SL-13` `08` §3) |
| `CV-03` | **The ledger half of absorption is conditional on valuation posture**: under periodic valuation no labour entry exists | `JT-03` therefore governs whether absorption reaches the ledger at all | `FACT VERIFIED` |
| `CV-04` | **Two divergent cost figures**: valuation/ledger struck once at completion; analytic recomputed on every duration change. **Neither reads the rate stored on the work order.** Nothing reconciles them | Any order spanning a month end produces two different machine costs for the same work — **and a monthly-derived rate changes every month by construction** | `FACT VERIFIED` (`SL-13` `08` §5) |
| `CV-05` | **Fixed overhead is allocated on a variable-overhead mechanism** — cost = actual hours × rate. Halve the hours and the per-hour charge doubles | **TAS 2 ¶13 forbids exactly this**: the amount allocated per unit shall not increase when production falls or ceases. For the depreciation component the reference mechanism **does not comply** | `FACT VERIFIED` + statutory |
| `CV-06` | **Normal capacity does not exist; absorbed-vs-actual variance does not exist** (`links 18`, `19`) | TAS 2 ¶13 compliance is **unprovable**, not merely unproven | `NOT FOUND IN SEARCHED SCOPE` |
| `CV-07` | **The financial entry date defaults to the processing date, not the physical event date** | Handoff elements 3 and 4 genuinely diverge and **cannot be collapsed** | `FACT VERIFIED` (`R4-F`) |
| `CV-08` | **Retroactive cost compensation is sequenced by record creation order, not by effective date** | Back-dated entry can attribute cost to the **wrong period** | `FACT VERIFIED` (`R4-F-20`, escalated `L13-01`) |
| `CV-09` | **Depreciation day convention**: two conventions — 30/360 default and real calendar — selected by **one untracked setting**. February differs by **−8.00%**; the full first year differs by **−0.05%** | An 8% February error recurs every year, permanently, and **the annual reconciliation that would normally catch a systematic error will never catch it** | `FACT VERIFIED` as arithmetic; engine transcription `SOURCE-SUPPORTED INTERPRETATION` |
| `CV-10` | **Scrap has no salvage concept and no approval state** | Dependency area 7 has **no reference pattern to adopt** — original design work | `NOT FOUND IN SEARCHED SCOPE` (`R4-F-03`, `R4-F-04`) |
| `CV-11` | **Weight- and volume-based landed-cost allocation distorts silently** when those product attributes are unmaintained | A data-quality condition produces a valuation error with no signal | `FACT VERIFIED` (`R4-F-05`) |

## 4. The statutory floor — closed, and it raises the bar

`BLK-03` and `BLK-04` are **`CLOSED — EVIDENCE VERIFIED`** and both cut against convenience:

- **TAS 2 ¶12** (ประกาศสภาวิชาชีพบัญชี ที่ 34/2562): fixed production overhead — **expressly including
  depreciation and maintenance of factory buildings, factory equipment and right-of-use assets used in
  production** — forms part of the conversion cost of inventories. **Absorption is required, not merely
  permitted.**
- **TAS 2 ¶13**: unallocated production overhead is recognised as an **expense in the period incurred**,
  and the per-unit allocation **shall not increase** when production falls or ceases.
- **ประกาศกรมพัฒนาธุรกิจการค้า แบบ 2**: an exhaustive text search of all four prescribed statements
  returns **no** off-balance / memorandum / *นอกงบดุล* line item. **Off-balance amounts have no statutory
  presentation surface.**

**Consequence:** SMEsPlus must build absorption. `DC-09` — double cost absorption — is therefore not a
hypothetical; it is the risk created by the required work, and it is unguarded because the relief
mechanism does not exist in anything the programme has read.

## 5. Positions

| id | Position | Basis |
|---|---|---|
| `CVP-01` | **Absorption is mandatory and must be built with an explicit relief of the period-expense line, posted as its own accounting event.** Neither half may be implicit | `DC-09`, TAS 2 ¶12 |
| `CVP-02` | **The absorption rate uses normal capacity.** The actual-hours reading is `REJECTED — INVALID ASSUMPTION` — it breaches TAS 2 ¶13, is undefined at zero output, and capitalises idleness into inventory | `BLK-07`, `SL-13` `22` §6 |
| `CVP-03` | **Absorbed-vs-actual variance is a first-class accounting event** (`UAE-31`) with a named owner, or TAS 2 ¶13 compliance cannot be evidenced | `CV-06` |
| `CVP-04` | **Physical event date and financial recognition date are two stored values, never collapsed** | `CV-07`, contract elements 3 and 4 |
| `CVP-05` | **Cost ordering is by effective date, not by record creation order** | `CV-08` |
| `CVP-06` | **Every asset records its day convention explicitly, per asset, regardless of what the live data shows** | `CV-09`; `SL-13` `19` §2 |
| `CVP-07` | **Every non-sale stock reduction carries a classification distinguishing it from a sale** — this is Inventory-owned, **not COGS-gated**, and it is what prevents the periodic computation from silently mislabelling scrap, shrinkage, write-down and adjustment as cost of sales | `DC-03b`, `L5-09` |
