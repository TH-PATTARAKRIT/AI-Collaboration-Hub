# P11 — UNIFIED DOUBLE-COUNTING REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Model 15 of 15 · CP-08 Double-Counting Attack · **the mandatory attack**

> **Recommendation only. Boss is the sole Final Approver.**
> **Do not hide collision.**

---

## 1. Method, and the negative-claim boundary declared before any finding

Eleven mandated attack classes plus the six additional collision classes are each run against the
`PEER-PUBLISHED` evidence base. For each, the register states **the mechanism**, **whether a guard
exists**, and **the evidence class of the "no guard" claim**.

> ### Negative-claim boundary — declared once, applies to every row.
> P11 read **no reference source code**. Every "no guard exists" statement below is **inherited** from
> a peer package and carries **that package's** search boundary. Under `MCU-21` **not one of those
> packages has declared which of 22 reference core roots it searched.**
>
> Therefore **every negative claim in this register is class `C — NOT FOUND IN SEARCHED SCOPE`,
> where the scope is itself undeclared.** None is class `A — VERIFIED ABSENCE`, and none is written
> as one. Where a guard's absence is instead established from a **design** artefact — a missing
> contract element, a missing model — that is stated separately and is stronger, because it does not
> depend on any root.

---

## 2. The root cause, stated once

> ## Every double-counting class below reduces to one absence.
>
> **There is no accounting-event identity** (`UAE-29`, `GAP-B02`, `XM-01`). The same business event
> posted twice produces two equally valid entries and **nothing detects it**. Number uniqueness is
> asserted at posting and does not compare business facts.
>
> Reinforced independently from the design side, and this half does **not** depend on any reference
> root: the Boss-approved handoff contract's **element 15 — deterministic idempotency identity —
> fails on 10 of 10 material handoffs** (`RISK-C02`, `SL-07` `16` §3.1), and **element 14 —
> migration/replay batch identity — fails on 10 of 10** (`GAP-FS-08`).
>
> `XM-01` is recorded in `SL-01` `05` §4 as **the most serious carried risk, because it has no partial
> mitigation.** P11 confirms that assessment across all ten processes and does not soften it.

---

## 3. The eleven mandated attack classes

| id | Class | Mechanism by which it can occur | Guard? | Evidence & class |
|---|---|---|---|---|
| `DC-01` | **DOUBLE POSTING** | The same business event handed to the ledger twice — by retry, by replay, by two users, by a re-run producer job. Two entries, two numbers, both valid | **none** | `XM-01`, `GAP-C03` (`C`); element 15 fails 10/10 (**design-side, root-independent**) |
| `DC-02` | **DOUBLE INVENTORY VALUATION** | A receipt valued at receipt **and** revalued at bill, with no linkage; `JT-03` leaves perpetual-vs-periodic posture undecided, and **the reference ERP has no single stable pattern across versions to imitate** | **none determined** | `SL-07` `17` §4 `JT-03`; `SL-17` |
| `DC-03` | **DOUBLE COGS** | Perpetual cost-release entries **and** a periodic cost-of-sales computation both running. `JT-03` undecided means both postures are reachable in design; `JT-04` undecided means the release point itself is unfixed | **none determined** | `JT-03`, `JT-04` `NOT DECIDABLE` |
| `DC-03b` | **COGS OVERSTATEMENT by classification collapse** — *not* a double count, listed here because it is routinely mistaken for one | The periodic computation **silently mislabels every non-sale stock reduction as cost of sales** unless scrap, shrinkage, write-down and adjustment are separately identified and subtracted first | **Inventory-owned and NOT blocked** — R4 names it a non-blocked obligation | `SL-07` `16` §5; `L5-09` semantic collapse |
| `DC-04` | **DOUBLE REVENUE** | Invoice-before-delivery (`UBE-14`) and delivery-based recognition are both reachable; no event identity links the two documents as one business fact | **none** | `BC-01` §2.4; `XM-01` |
| `DC-05` | **DOUBLE AP** | Goods-received-not-invoiced accrual (`UBE-02`) plus the vendor bill (`UBE-04`), where the clearing link is the missing element. Element 12 — *original event identity* — and element 15 both fail on the receipt handoff | **none determined** | `SL-07` `16` §3; `BC-02` elements 12, 15 |
| `DC-06` | **DOUBLE AR** | Invoice plus a re-issued invoice for the same delivery; credit-note auto-matching covers the cancelling case only | **partial** — auto-match where a credit note cancels | `SL-01` `08` Part 2 |
| `DC-07` | **DOUBLE TAX** | Accrual tax on the document **and** cash-basis tax on settlement (`AE-13`). `M-02` (FX) is explicitly **auto-reversed on unmatch**; **`M-03` (cash-basis tax) is not stated to be.** Its register row reads *"Reconciliation: not itself reconciled"* and *"Reversal: the generated entries can be reversed but cannot be reset to draft."* Unmatch-then-rematch is therefore a candidate double recognition | **`UNRESOLVED — EVIDENCE REQUIRED`** | `SL-01` `08` `M-02` vs `M-03` — **a gap between two rows of one table, visible only when they are read against each other.** `P11-DERIVED`. **NEW at P11** |
| `DC-08` | **DOUBLE DEPRECIATION** | One physical machine represented by several asset records — *"a duplicated machine's cost pool doubles, silently"* | **none** | `SL-13` `22` `BLK-02` `HOLD — UAT REQUIRED`, closes on query `Q-02` |
| `DC-09` | **DOUBLE COST ABSORPTION** | TAS 2 ¶12 **requires** factory depreciation to enter conversion cost. Today link 3 posts depreciation to an **expense account** and links 5, 7, 8, 11 — the machine cost pool, the operation-equipment field, the rate derivation, the machine-level time log — are **ABSENT**. Building absorption **without relieving the expense line** charges the same depreciation twice: once to period expense, once into inventory | **none — the relief mechanism does not exist because absorption does not exist** | `SL-13` `08` §1 links 3, 5, 7, 8, 11, 18; `BLK-03` `CLOSED — EVIDENCE VERIFIED`; TAS 2 ¶12–13 |
| `DC-10` | **DOUBLE RECOGNITION (schedules)** | Deferred revenue/cost release (`UAE-25`) — **producer contract not established at all**, so no duplicate-schedule guard can be asserted either way | `UNKNOWN — EVIDENCE REQUIRED` | `SL-01` `05` §1 |
| `DC-11` | **DOUBLE SETTLEMENT** | **Over-reconciliation** — the matching record is **unconstrained against the item it matches**; residual, reconciled state and payment state are **stored-computed and capable of drifting from their inputs** | **none** | `T0-05` `UNRESOLVED`; `COR-09`; `SL-01` `06` §3 |

### 3.1 `DC-09` in full — the one that will be built wrong

`DC-09` is singled out because it is the only class in this register where **the correct action creates
the risk**. The other ten are risks of doing nothing.

`BLK-03` is `CLOSED — EVIDENCE VERIFIED`, and the finding **exceeds the question**: under TAS 2 ¶12
per ประกาศสภาวิชาชีพบัญชี ที่ 34/2562, absorption of factory-asset depreciation into conversion cost is
**required, not merely permitted**. So SMEsPlus must build the absorption path that the reference model
lacks.

The moment that path exists, the depreciation entry has **two** destinations:

1. the expense account, via link 3, which **works today**; and
2. the inventory conversion cost, via the rate, which must be built.

**Nothing in the evidence base describes a relief entry between them**, because no package has ever
had both halves in view at once: the Asset package traced the chain and found the front absent; the
Inventory package's valuation questions are `JT`-blocked; Wave A withheld both patterns as producer
work. `DC-09` is visible only from P11's vantage point, and it is recorded as **NEW at P11**.

Compounding it, three further facts sit on the same path and each is independently open:
`BLK-07` decides the **rate basis** (normal capacity vs actual hours — only one complies with
TAS 2 ¶13); absorption occurs **only under FIFO/average costing** and never under standard costing;
and the ledger half occurs **only under perpetual valuation**. A design that assumes machine cost
reaches inventory will be **silently wrong for every standard-costed product**.

---

## 4. The six additional collision classes

| id | Collision | Finding | Class |
|---|---|---|---|
| `DC-12` | **Orphan financial facts / facts without provenance** | Fact `F7` provenance — **`PARTIALLY VERIFIED` per the governing CORR1 `C04`/`C11`, not *"not implemented at all"* as first published (`X2-F11`)**: a real database constraint exists, but only with an optional module installed, and it is **table-global rather than tenant-scoped**; the surviving claim is that *no general, mandatory carrier was found in the accounting module*. A manual journal to a control account creates a financial fact with no source. `AE-14` opening entries are ordinary entries with no migration identity — element 14 fails 10/10 | Design-side, **root-independent** |
| `DC-13` | **Cross-company leakage** | `T0-06` cross-company rewrite of a posted fact `UNRESOLVED`; `T0-10` cross-company creation and revocation of the lock exception `UNRESOLVED`, *wider than registered*; hard lock **cascades from every parent**, coupling entities a tenant may consider independent | `UNRESOLVED` ×3 |
| `DC-14` | **Cross-tenant leakage** | `T0-04` `UNRESOLVED`, with `MCU-04` closed as a **`VERIFIED DEFECT` on this boundary** and `FC-A1` adding the menu; `SB-01` **one configuration write disables a control for every tenant in the database**; `SB-02` identifier-arithmetic ceiling aliases at 10,000; `SB-03` hash chain cannot cross a tenancy boundary; `SB-04` control evidence leaves the tenant | `SB-01` is the **highest-severity** boundary failure in the inherited base |
| `DC-15` | **Closed-period mutation** | Finality is a **bare date with no object behind it** (`F6`); the lock exception is granted **and revoked by the same role**; **soft locks move backward freely with no distinct authority required**; `T0-03` deletion or rewrite of a posted fact `UNRESOLVED` | `UNRESOLVED` |
| `DC-16` | **Manual GL bypass of provenance** | With `F7` absent and no maker-checker (`UAE-30`), a manual entry can create, correct or contradict any subledger's assertion, and **nothing links it back**. `DC-16` is the mechanism by which every other class in this register can be reproduced by hand | Design-side, **root-independent** |
| `DC-17` | **Inconsistent reversal and reporting semantics** | Reversal lineage is a **`CLOSED — VERIFIED DEFECT`** (`MCU-15`/`BW-35`); `M-04` re-dating can place a reversal in a different **year** from its original; un-post destroys matching history and analytic lines; and on the reporting side `account.report.filter_multi_company` **reads as a company control and is a rendering option — the source comment says so** (`T0-09`, third instance, floor of 30 declarations across 4 files, **never bounded**) | Mixed |

---

## 5. `unbalanced-and-posted` — carried forward verbatim so it is not lost

`T0-12` is the single most severe open item in the inherited base and it is a double-counting concern
of a different kind — it defeats the invariant that would otherwise **detect** several classes above:

> The debit = credit assertion is itself **suppressible by context**, with **three shipped production
> consumers**. `unbalanced-and-posted` is **reachable**.
>
> The suppression key sits inside a bucket of **48 generic tokens that was counted and never
> assessed** — it is that bucket's most severe member, and **the bucket has still not been opened.**

**P11 does not re-route this to any process.** It is a named Wave A residual and remains one. It is
restated here because a double-counting register that assumed the balance invariant holds would be
building on a floor that is known to be openable.

---

## 6. Register position

| Measure | Count |
|---|---|
| Attack classes run | **17** (11 mandated + 6 additional) |
| Classes with **a guard that works** | **0** |
| Classes with a **partial** guard | **1** — `DC-06`, cancelling credit notes only |
| Classes whose absence is **root-independent** (design-side) | **4** — `DC-01` (element 15), `DC-05` (elements 12/15), `DC-12` (element 14, `F7`), `DC-16` |
| Classes **new at P11** | **2** — `DC-07`, `DC-09` |
| Classes resolved by this session | **0** |

> ### `0 of 17 double-counting classes has a working guard.`
>
> That figure is **not** a claim that SMEsPlus will double-count. It is a claim about the **evidence
> base P11 was given**: across twenty-one published packages, no artefact establishes a working guard
> for any of the seventeen. Four of the seventeen do not depend on the undeclared reference root at
> all — they are failures of the **design contract**, and those four are the ones that cannot be
> argued away by declaring the root.
