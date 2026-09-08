# ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` Part F · deliverable **8 of 12**
**Surfaces:** P06 `a533fe9` · P08 `ca577be` · P09 `ab8c013` · P11 `79e1369` · P07 `ee2be30` **READ-ONLY**
**Classification:** LAYER 1 — clean-room. **No vendor model, field, table, module or path name appears in this file.**

---

## 0. What this pack is — and the one thing it is for

**Evidence and handoff readiness only. This is NOT Phase SA design.** No schema, no contract, no architecture, no implementation. Every element below is a **business/accounting semantic and an ownership statement**, derived from evidence already published at the SHAs above.

> ### The purpose is to stop Account blocking the programme.
>
> **Account has unresolved research history. Almost none of it is interface-shaped.** A module whose handoff semantics are settled must not wait because a different question about the same package is open. **This pack separates the two, interface by interface, so the rest of the programme can move where Account is genuinely ready and wait only where it genuinely must.**
>
> **There is no global Account HOLD in this pack, and that is a deliberate correction of the prior posture.**

## 1. The three classifications, and what each obliges

| Classification | Meaning | What Phase SA may do |
|---|---|---|
| **`ACCOUNT-HANDOFF-READY`** | every minimum semantic is established and owned; nothing outstanding blocks the interface | proceed |
| **`ACCOUNT-HANDOFF-READY-WITH-DELTA`** | the interface is usable; **named** attributes are unresolved and are listed with their owner and smallest next action | **proceed around the named delta**, which must be carried visibly |
| **`ACCOUNT-HANDOFF-EXTERNAL-DECISION-PENDING`** | a **decision outside Account's authority** — Boss, or a statutory/legal authority — determines the interface | proceed on everything else; **this attribute waits for a decision, not for more research** |

**A classification is per interface, never per package.** No interface is downgraded because a *different* interface is unresolved.

---

## 2. Interface readiness — eleven interfaces

| # | Interface | Classification | The single thing that decides it |
|---|---|---|---|
| 1 | **Procure-to-Pay / Purchase** | `READY-WITH-DELTA` | goods-received-not-invoiced position and correction-by-reversal are established and measured; **price-difference disposition is the delta** — most differences never reach the ledger |
| 2 | **Order-to-Cash / Sales** | `READY-WITH-DELTA` | the revenue-side handoff semantics are established; **cost-of-sale recognition is the delta** and it belongs to the Inventory/COGS interface below, not here |
| 3 | **Inventory / COGS** | `EXTERNAL-DECISION-PENDING` | **the valuation method is one configuration decision with five downstream consequences.** It is a **business policy decision**, not a research gap — no further evidence changes it |
| 4 | **Manufacturing / WIP / FG / COGS** | `READY-WITH-DELTA` | the manufacturing cost position is established and measured; **conversion cost arriving at zero is the delta**, with a fixed-overhead injection path that has no owner |
| 5 | **Expense-to-Pay** | `READY-WITH-DELTA` | the expense position is established; **two co-installed withholding subsystems are the delta** — which is authoritative is a Tax-interface decision (see 8) |
| 6 | **Asset / Depreciation** | `READY-WITH-DELTA` | capitalisation and depreciation semantics are established; **derecognition and the analytic effect of depreciation are the delta** |
| 7 | **Bank / Payment / Reconciliation** | `READY-WITH-DELTA` | settlement and bank-event semantics are established and handed over under **seven preserved vetoes**; **the settlement event's own date is the delta** — Account requires it and cannot source it |
| 8 | **Thailand Tax Compliance** | **`EXTERNAL-DECISION-PENDING`** | **one routed question:** *whether a tax-reporting grouping may span companies, and within what security boundary.* **Boss-owned. Not answerable from evidence** |
| 9 | **Plan-to-Analyze / Analytic dimensions** | `READY-WITH-DELTA` | the analytic dimension is established as a **schema, not data**; **reconcile on gross per cost object, never on a net** — the net is measured to be misleading |
| 10 | **Deferred / Time-based Recognition** | `READY-WITH-DELTA` | recognition semantics are established; **the recognition event collapsed into the posting act is the delta**, and it is the same root as the timing gap in §4 |
| 11 | **Core Reconciliation / Record-to-Report** | `READY-WITH-DELTA` | the ledger contract, posting semantics and the four-extract balance result are established; **accounting-event identity and the absence of a period object are the deltas** |

**Two interfaces are `EXTERNAL-DECISION-PENDING`. Nine are usable now with named deltas. Zero are blocked on Account research.**

---

## 3. Minimum Input / Output semantics — reconciled from existing evidence

**Business and accounting semantics with ownership only. No implementation schema is invented.**

| Element | Semantic | Direction | Owner boundary | Readiness |
|---|---|---|---|---|
| **Tenant identity** | the isolation boundary above company; **missing scope must deny, never default** | `SHARED CONTRACT` | platform | **READY** — but see `§5 G-07` |
| **Company identity** | every object with a financial effect has **exactly one** owning company; where it cannot be proven, the operation is denied | `SHARED CONTRACT` | platform / Account | **READY** |
| **Source business event identity** | the identity of the real-world act, distinct from any document | `INPUT TO ACCOUNT` | source process | **DELTA `G-01`** — established as **absent as a platform property**; **eight processes depend on it** |
| **Source document / reference identity** | the document the source process issues | `INPUT TO ACCOUNT` | source process | **READY** |
| **Event / effective date** | when the business act occurred | `INPUT TO ACCOUNT` | source process | **READY** |
| **Accounting date** | the date the ledger effect is dated to; **not derivable from the posting act** | `SHARED CONTRACT` | Account | **DELTA `G-02`** — evidence shows it **system-derived** in at least one estate generation |
| **Tax point / tax date** | distinct from the accounting date when statute requires | `SHARED CONTRACT` | Tax | **EXTERNAL `G-03`** |
| **Recognition trigger** | what causes a ledger effect to exist | `SHARED CONTRACT` | Account + source | **DELTA `G-04`** — **recognition is collapsed into posting**; the estate reliably carries **one** of four distinct times |
| **Amount** | the monetary quantity | `INPUT TO ACCOUNT` | source process | **READY** |
| **Currency & measurement context** | the currency and the frame the amount is measured in | `SHARED CONTRACT` | Account | **DELTA `G-05`** — the balance assertion is **reporting-currency only**; a transaction-currency frame is a separate, non-zero measurement |
| **Valuation / cost context** | the basis on which a quantity becomes an amount | `INPUT TO ACCOUNT` | Inventory / Manufacturing | **EXTERNAL `G-06`** — one configuration decision, five consequences |
| **Counterparty** | the party the effect faces, where one exists | `INPUT TO ACCOUNT` | source process | **READY** |
| **Analytic / dimension attribution** | management attribution, **not a financial fact** | `SHARED CONTRACT` | Account (P09) | **DELTA `G-08`** — attribution must be consumed **gross per cost object**, never net |
| **Settlement / reconciliation linkage** | which effects discharge which | `SHARED CONTRACT` | Account (P06/P11) | **DELTA `G-09`** — the settlement event's **own date** is required and unsourced |
| **Reversal / correction lineage** | how an effect is undone without being erased | `OUTPUT FROM ACCOUNT` | Account | **DELTA `G-10`** — immutable reversal measures clean; **a deletion path bypasses it and leaves no trace by design** |
| **Posting eligibility / hold reason** | why an effect may not post yet, stated positively | `OUTPUT FROM ACCOUNT` | Account | **READY** |
| **Accounting effect status** | draft / posted / cancelled, and what each permits | `OUTPUT FROM ACCOUNT` | Account | **READY** |
| **Source owner process** | which process authored the fact | `INPUT TO ACCOUNT` | source process | **READY** |
| **Account owner boundary** | **a ledger consequence does not transfer lifecycle ownership to Account** | `SHARED CONTRACT` | Account | **READY** — the single most reusable statement in this pack |
| **Period / cut-off membership** | which accounting period an effect belongs to | `SHARED CONTRACT` | Account | **DELTA `G-11`** — **no accounting-period object**; no company observed closing |
| **Statutory grouping scope** | whether a reporting grouping may span companies | `NOT ACCOUNT-OWNED` | **Boss** | **EXTERNAL `G-12`** |

**Counts: `INPUT TO ACCOUNT` 7 · `OUTPUT FROM ACCOUNT` 3 · `SHARED CONTRACT` 10 · `NOT ACCOUNT-OWNED` 1.**

---

## 4. One root under several deltas — stated once, not eleven times

**`G-01` (event identity), `G-04` (recognition trigger) and `G-11` (period membership) are three faces of one thing:** the estate carries the **posting act** reliably and the **accounting event** not at all.

> Four distinct times exist in the business — **occurrence, recognition, posting, settlement** — and the evidence shows the estate reliably carrying **one of them**. Where the other three are needed, they are **derived from the posting act**, which is why an accounting date can be system-derived, a recognition trigger can be indistinguishable from a posting trigger, and a period can have no object of its own.

**Phase SA can proceed around this** by treating event identity, recognition trigger and period membership as **first-class inputs it must be given**, rather than as attributes it can derive. **That is a design instruction this pack is not authorised to make, and a boundary statement it is.**

---

## 5. Gap discipline — every gap, with an owner and a smallest next action

**A gap is not a research invitation.** No entry below says *"more research required"*.

| id | Interface | Exact missing semantic / decision | Owner | Can Phase SA proceed around it? | Smallest next action |
|---|---|---|---|---|---|
| `G-01` | 11, and 8 processes | **accounting-event identity as a first-class property** | **Boss** (design) | **YES** — carry it as a required input | Boss decision `BD-ACC-01`: is event identity a platform property? |
| `G-02` | 11 | accounting date must be **supplied**, not derived from the posting act | Account | **YES** | state it as a required input in the SA contract |
| `G-03` | 8 | tax point as a carrier distinct from the accounting date | Tax | **YES** | Tax names the carrier; no new research |
| `G-04` | 10, 11 | recognition trigger distinct from the posting act | **Boss** (design) | **YES** | folded into `BD-ACC-01` |
| `G-05` | 11 | the currency frame a balance assertion is made in | Account | **YES** | declare *reporting currency* on every balance statement |
| `G-06` | 3, 4 | the valuation-method policy decision | **Boss** (business policy) | **partly** — costing outputs wait; every other interface proceeds | Boss decision `BD-ACC-03` |
| `G-07` | all | **the estate is not homogeneous in its custom access-rights layer** (`P08-F-NEW-01`) | **Boss** | **YES** | Boss decides whether the isolation baseline is re-established before Phase SA — **not an Account research task** |
| `G-08` | 9 | attribution consumed **gross per cost object** | Account | **YES** | state it in the SA contract; the measurement already exists |
| `G-09` | 7, 11 | the settlement event's **own** date | Bank / source | **YES** | Bank names the carrier |
| `G-10` | 11 | a path that destroys ledger facts outside the correction model | **Boss** | **YES** — it is an operational control, not an interface attribute | Boss decision on the destructive path |
| `G-11` | 11 | accounting-period membership as an object | **Boss** (design) | **YES** | folded into `BD-ACC-01` |
| `G-12` | 8 | **may a tax-reporting grouping span companies, and under what security boundary** | **Boss** | **YES for every non-statutory interface** | Boss decision `BD-ACC-02` |

**Twelve gaps. Eleven can be proceeded around. One — `G-06` — partly gates its own two interfaces and nothing else.**

---

## 6. What this pack does NOT do

- **No Phase SA design, no schema, no contract, no architecture, no field list for implementation.**
- **No statutory determination.** Thai statutory claims remain `HOLD / EVIDENCE REQUIRED` and route to the Accounting-Tax track.
- **No Veto discharged.** Readiness is about interface semantics; a veto is about authorisation, and they are not the same axis. **An interface can be `READY` under a preserved veto**, because the veto restrains *implementation*, not *description*.
- **No claim that Account research is complete.** It is not. **This pack asserts only that the unfinished parts are, with two named exceptions, not interface-shaped.**
