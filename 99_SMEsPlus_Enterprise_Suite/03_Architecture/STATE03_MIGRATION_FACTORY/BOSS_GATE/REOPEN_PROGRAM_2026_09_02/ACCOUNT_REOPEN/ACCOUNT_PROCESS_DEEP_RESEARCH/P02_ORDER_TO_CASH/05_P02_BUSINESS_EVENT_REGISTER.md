# 05 — P02 BUSINESS EVENT REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Denominator Declaration

- **POPULATION** — every state transition or user action in the O2C spine that changes a business fact
  a downstream accounting or reporting consumer can observe.
- **PATTERN** — derived from three enumerable sources, each itself a complete denominator:
  (a) the order status enumeration (**4 values**, `EV-P02-035`);
  (b) the movement status enumeration (**6 values**, `EV-P02-039`);
  (c) the accounting-document state transitions reachable from the posting, draft, cancel and reversal
  routines (`EV-P02-029`, `EV-P02-017`, `EV-P02-054`).
- **PATH SET** — sales, sales-inventory, inventory, inventory-accounting and accounting modules of the
  reference tree, as enumerated in `14_P02_EVIDENCE_MANIFEST.md` §2.
- **UNIT** — one business event.
- **RESULT — 24 events (BE-01 … BE-24).** The set is bounded by the three enumerations above **plus**
  the settlement events contributed by track T2 and the return events contributed by track T1.
  **Declared incompleteness:** events contributed by modules outside the path set — subscriptions,
  point of sale, e-commerce, rental, projects, manufacturing — are **NOT YET SEARCHED** and are excluded
  by declaration, not by evidence. Any of those could add an O2C-relevant event.

## 1. Register

Legend for **Identity**: does the event produce a durable, immutable record that says *this happened,
once, at this moment*?

| ID | Business event | Canonical owner | Accounting effect | Identity | Mutable after? | Tag |
|---|---|---|---|---|---|---|
| BE-01 | Quotation raised | order (draft) | none | no — same record as the order | fully | `FACT VERIFIED` |
| BE-02 | Quotation sent | order (sent) | none | no — status only | fully | `FACT VERIFIED` |
| BE-03 | Order confirmed | order (sale) | **none** | partial — status + a date overwritten by the system clock | terms remain editable | `FACT VERIFIED` `EV-P02-001` |
| BE-04 | Order locked / unlocked | order | none | **no — a reversible boolean, not a state** | freely | `FACT VERIFIED` `EV-P02-037` |
| BE-05 | Order cancelled | order (cancel) | none directly | status only | reversible to draft | `FACT VERIFIED` |
| BE-06 | Order line added / changed after confirmation | order line | none directly; **launches procurement** | none | freely | `FACT VERIFIED` `EV-P02-033` |
| BE-07 | Reservation / allocation | movement | none | held by inventory, not by P02 | freely until done | `DEPENDENCY OPEN` — Inventory owns |
| BE-08 | **Goods physically leave** | movement reaching done **with a picked line** | **YES — inventory relief** | layer, keyed only by its creation timestamp | quantity correctable, creating new layers | `FACT VERIFIED` `EV-P02-022` |
| BE-09 | Goods leave with **no** picked line | movement reaching done | **NONE** | none | — | `FACT VERIFIED` `EV-P02-022` |
| BE-10 | Delivered quantity asserted directly | order line field | none directly; **drives billable quantity** | none | see §3a | `FACT VERIFIED` `EV-P02-002`, `EV-P02-070`, `EV-P02-071` |
| BE-11 | Backorder created | movement split | none | new movement records | — | `FACT VERIFIED` T1 §7 |
| BE-12 | Remainder cancelled (never-backorder) | movement | none | cancelled movements only | — | `SUPPORTED INTERPRETATION` T1 §7 |
| BE-13 | Draft customer invoice raised | accounting document (draft) | **none** — but **consumes billable quantity** | none | freely | `FACT VERIFIED` `EV-P02-005` |
| BE-14 | **Customer invoice posted** | accounting document (posted) | **YES — revenue, receivable, tax, and cost of sales** | document number + optional integrity hash | name/date locked only under hash or lock date | `FACT VERIFIED` `EV-P02-015`, T3 §8 |
| BE-15 | Invoice reset to draft | accounting document | **cost lines destroyed**; revenue lines retained as content | number retained unless cleared | renumberable when unhashed | `FACT VERIFIED` `EV-P02-017`, T3 §8 |
| BE-16 | Invoice cancelled | accounting document (cancel) | cost lines destroyed | — | — | `FACT VERIFIED` `EV-P02-017` |
| BE-17 | **Physical return received** | movement (customer → internal) | **YES — inventory restored** | layer | — | `FACT VERIFIED` T1 §1 |
| BE-18 | **Credit note posted** | accounting document (credit note) | **YES — revenue, receivable, tax and cost reversed** | document number | — | `FACT VERIFIED` T1 §3 |
| BE-19 | Refund-intent flag set on a return | movement field | none directly; **reduces delivered quantity** | none | freely, but **hidden from ordinary users** | `FACT VERIFIED` T1 §4b |
| BE-20 | **Customer payment received** | payment record | **YES — receivable relieved into an outstanding account** (or **no entry at all** in one configuration) | payment record | draft/cancel reachable | `FACT VERIFIED` T2 §1 |
| BE-21 | **Settlement matched (reconciliation)** | matching rows between two lines | **realised exchange difference, and cash-basis tax if enabled** | matching rows | **freely destroyed, even across a closed period** | `FACT VERIFIED` T2 §7 |
| BE-22 | Bank statement reconciled | statement line | **YES — outstanding account cleared to bank** | statement line | — | `SUPPORTED INTERPRETATION` T2 §5 |
| BE-23 | **Down payment invoiced** | accounting document | **YES — a liability *or* immediate revenue, by configuration** | document number | — | `FACT VERIFIED` T2 §4 |
| BE-24 | Write-off applied | payment or reconcile wizard | **YES — receivable written to a user-chosen account** | journal line | — | `FACT VERIFIED` T2 §6 |

## 2. Events That Create A Financial Fact

Per the correction's research requirement 6 and 7, the subset of BE-01…BE-24 that creates a financial
effect, and the scope that owns that effect:

| ID | Financial effect | Scope owning the effect | Evidence |
|---|---|---|---|
| BE-08 | inventory relieved | **COMPANY** | `EV-P02-023` |
| BE-14 | revenue, receivable, output tax, cost of sales | **COMPANY** | `EV-P02-015`, `EV-P02-026` |
| BE-17 | inventory restored | **COMPANY** | T1 §1 |
| BE-18 | revenue, receivable, tax and cost reversed | **COMPANY** | T1 §3 |
| BE-20 | receivable relieved into an outstanding account | **COMPANY** | T2 §1 |
| BE-21 | realised exchange difference; cash-basis tax | **COMPANY** | T2 §3, T3 §4 |
| BE-22 | outstanding account cleared to bank | **COMPANY** | T2 §5 |
| BE-23 | liability raised, or revenue recognised | **COMPANY** | T2 §4 |
| BE-24 | receivable written off | **COMPANY** | T2 §6 |

**All nine financial effects are COMPANY-scoped.** No P02 event creates a financial effect at
TENANT or PLATFORM scope. Full scope analysis, including the non-financial events, is in
`20_P02_SCOPE_OWNERSHIP_MATRIX.md`.

## 3. Events With No Identity — The Core Structural Defect

**`FACT VERIFIED` — P02-F-34.** Of the 24 events, **eleven produce no durable, immutable record of
their own occurrence**: BE-01, BE-02, BE-04, BE-06, BE-07, BE-09, BE-10, BE-13, BE-19, and the
identity-free halves of BE-03 and BE-11. They are observable only as *the current value of a field*, or
not at all.

The three that matter most for accounting:

| Event | Why the absence is material |
|---|---|
| **BE-09** (goods leave with no picked line) | An inventory outflow with **no financial record anywhere**. Undetectable by any accounting query, because there is nothing to query. |
| **BE-10** (delivered quantity asserted directly) | Under delivery-based invoicing this **directly determines how much revenue may be recognised**, and it leaves no trace distinguishing an asserted value from an outflow-derived one. Reachability is qualified in §3a. |
| **BE-19** (refund-intent flag) | Silently changes whether a physical return has any revenue consequence, defaults on, and is **hidden from ordinary users** (T1 §4b, C4). |

### 3a. BE-10 Qualified — Self-Correction Recorded

The first draft of this package stated that the delivered quantity is *directly user-writable*. On
re-derivation that is **too strong**, and the correction is recorded here rather than silently applied.

| Layer | Finding | Evidence |
|---|---|---|
| **Data layer** | The field is stored with its read-only attribute **cleared** — it is writable by any programmatic path: import, external interface, automation, scripted correction. | `EV-P02-002` |
| **Interface layer** | The field is rendered **read-only whenever the derivation method is not manual**, in both the form and the list view. | `EV-P02-070` |
| **Which method applies** | The derivation-method selection has **five** values, not two: `manual` and `analytic` in the base sales module, extended by `stock_move`, `milestones` and `timesheet`. Corrected after independent challenge. | `EV-P02-071`, `EV-P02-084` |

**Corrected statement — `FACT VERIFIED`, revised twice:**

- For **goods with inventory installed** (`stock_move`), the field is **not a second holder of the fact at
  all.** The interface blocks editing, and the compute **assigns** the outflow-derived value on every
  change to a linked movement's state, quantity or unit (`EV-P02-084`). A programmatic write is therefore
  **transient** — it survives only until the next dependency change. The field is a **materialised cache
  of the outflow ledger**, not a competing source of truth. The package's first two statements of this
  finding were both too strong; this is the third, and it is the one that matches the code.
- The **genuine** second holder exists only where the method has **no outflow behind it at all** —
  `manual` (services), `analytic` (expense re-invoicing), `milestones` and `timesheet`. For those the
  quantity governing revenue **is** a permanent human assertion, with no independent operational event
  and no event record.

**What survives the correction, and it is the part that matters:** for **services, expense re-invoicing,
milestones and timesheets** — a large share of SME revenue — the quantity that governs revenue
recognition has **no ledger behind it at all**. That is sharper and narrower than "the field competes with
the ledger", and it points at a different design question: **how is the performance of a service
evidenced?** The reference's answer is that it is not.

**`SUPPORTED INTERPRETATION`.** The interface read-only attribute is a **presentation control, not a data
control**. In a SaaS ERP with an external interface it is not a boundary at all.

**`DESIGN CANDIDATE` DC-05-01.** Every SMEsPlus business event that can influence a financial fact must
emit an immutable event record carrying: event type, occurrence timestamp, asserting actor, asserted
scope, the values asserted, and a link to whatever it consumed. "The current value of a field" is not an
event. Where a quantity **must** be human-asserted — services being the honest case — the assertion
itself is the event and must be recorded as one.

## 4. One Business Fact → One Canonical Event Owner: Verdict

| Business fact | Should have one owner | Actual owners found | Verdict |
|---|---|---|---|
| A commercial commitment exists | the order | the order | **holds** |
| Goods left the business | the outflow ledger | the outflow ledger **and** a writable field on the order line | **violated** — `EV-P02-002`; scope of the violation qualified in §3a |
| Goods were billed | the posted invoice set | a counter including drafts **and** a separate counter of posted only | **violated** — `EV-P02-005`, `EV-P02-006` |
| What the goods cost | the valuation layer | the layer **and** an independent re-derivation at invoice post | **violated** — `EV-P02-021` |
| The sale occurred on date D | one date | the document date **and** the accounting date, which may silently differ | **violated** — `EV-P02-013` |
| The customer paid | the payment | the payment, **or nothing at all** in one configuration | **violated** — T2 §1 |
| The debt is settled | the matching rows | matching rows, freely destructible across a closed period | **violated** — T2 §7 |
| Which order an invoice belongs to | a structural link | a per-line link **and** a header free-text field | **violated** — `EV-P02-009` |

**8 facts tested, 1 holds, 7 violated.** This is the evidence base for the PMO position in
`18_P02_PMO.md`.
