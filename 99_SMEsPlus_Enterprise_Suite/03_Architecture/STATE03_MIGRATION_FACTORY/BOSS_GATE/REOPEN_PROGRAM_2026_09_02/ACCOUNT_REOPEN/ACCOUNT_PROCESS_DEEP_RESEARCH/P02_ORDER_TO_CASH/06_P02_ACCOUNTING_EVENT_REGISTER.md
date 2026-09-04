# 06 — P02 ACCOUNTING EVENT REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. Denominator Declaration

- **POPULATION** — every code path in the O2C spine that creates or posts a journal entry.
- **PATTERN** — every construction of an accounting document, and every posting call, reachable from
  the O2C business events BE-01 … BE-24 of `05_P02_BUSINESS_EVENT_REGISTER.md`.
- **PATH SET** — as declared in `14_P02_EVIDENCE_MANIFEST.md` §2.
- **UNIT** — one accounting event (one distinct journal-entry-producing occurrence).
- **RESULT — 13 accounting events (AE-01 … AE-13).**
- **Declared incompleteness:** entries produced by modules outside the path set are **NOT YET SEARCHED**.
  Specifically excluded by declaration: subscription revenue, point of sale, e-commerce, deferred-revenue
  and landed-cost modules.

## 1. Register

| ID | Accounting event | Trigger | Date used | Journal | Conditional on | Tag |
|---|---|---|---|---|---|---|
| AE-01 | **Inventory relief on outflow** | movement completion with a picked line | **three branches** — a forced-period date if present, else the linked accounting line's date, else **today**. The ordinary delivery case is the third: today, not the movement's own date. Corrected after independent challenge. | stock journal from the product category | storable **and** real-time valuation **and** not owner-restricted | `FACT VERIFIED` `EV-P02-093`, `EV-P02-023` |
| AE-02 | **Revenue + receivable + output tax** | customer-invoice post | accounting date, silently movable | sale journal | — | `FACT VERIFIED` `EV-P02-026` |
| AE-03 | **Cost of sales** | customer-invoice post, **same document as AE-02** | same as AE-02 | same as AE-02 | split recognition on **and** storable **and** real-time valuation | `FACT VERIFIED` `EV-P02-015`, `EV-P02-018` |
| AE-04 | Interim-account matching | immediately after AE-02/AE-03 post | n/a — matching, not an entry | n/a | account reconcilable **and** real-time valuation **and** a linked completed customer-direction movement | `FACT VERIFIED` `EV-P02-041` |
| AE-05 | **Inventory restoration on return** | return movement completion | **today** | stock journal | as AE-01 | `FACT VERIFIED` T1 §1 |
| AE-06 | **Revenue + receivable + tax reversal** | credit-note post | reversal date, silently movable | sale journal | — | `FACT VERIFIED` T1 §2 |
| AE-07 | **Cost-of-sales reversal** | credit-note post | as AE-06 | as AE-06 | as AE-03 | `FACT VERIFIED` T1 §3 |
| AE-08 | **Receipt** | payment post | payment date | payment journal | **the payment method line has an outstanding account** — otherwise **no entry is produced at all** | `FACT VERIFIED` T2 §1 |
| AE-09 | **Realised exchange difference** | reconciliation | the exchange journal's lock-adjusted date, raised to the later line date — **not the settlement date** | exchange journal | a currency difference exists | `FACT VERIFIED` T2 §3 |
| AE-10 | **Cash-basis tax** | reconciliation involving a receivable/payable line | later of the two document dates, **jumping to today if that is on or before the fiscal lock** | cash-basis journal | company cash-basis switch **and** per-tax on-payment exigibility — **neither is set by the Thai data** | `FACT VERIFIED` T3 §4 |
| AE-11 | **Write-off** | payment register or reconcile wizard | **payment date** (register) or **silently re-dated past the lock** (reconcile wizard) | payment journal / a general journal | user action | `FACT VERIFIED` T2 §6 |
| AE-12 | **Down-payment recognition** | down-payment invoice post | as AE-02 | sale journal | — | `FACT VERIFIED` T2 §4 |
| AE-13 | Reversal of a derived entry on unmatching | destruction of matching rows | **re-dated forward through the lock helper** | as the original | AE-09 or AE-10 existed | `FACT VERIFIED` T2 §7 |

## 2. The Date Question, Consolidated

The directive requires the accounting event to be traced to a date. P02 uses **six different date rules**
across 13 accounting events. This is the consolidated answer:

| Rule | Events | Consequence |
|---|---|---|
| **Today (system clock)** — the third of three branches, and the ordinary case | AE-01, AE-05 | Inventory relief is dated when the record was validated, **not when the goods moved**. A picking validated on the 3rd for goods that left on the 1st books on the 3rd. The other two branches — a forced-period date, and the linked accounting line's date — are reachable and were originally omitted. `FACT VERIFIED` `EV-P02-093` |
| **Accounting date, silently movable past a lock** | AE-02, AE-03, AE-06, AE-07, AE-12 | Revenue, tax and cost land in a later period than the document says. `FACT VERIFIED` `EV-P02-013` |
| **Payment date** | AE-08, AE-11 (register) | — |
| **Exchange-journal lock-adjusted date, raised to the later line date** | AE-09 | The realised gain or loss is **not** dated on the settlement. `FACT VERIFIED` T2 §3 |
| **Later of two document dates, else today** | AE-10 | And the lock consulted **excludes the tax lock**, so a cash-basis tax entry can be dated into a period already closed for tax. `FACT VERIFIED` T3 §4 |
| **Silently re-dated past the lock** | AE-11 (reconcile wizard), AE-13 | — |

**`FACT VERIFIED` — P02-F-35 (HEADLINE).** **No single date rule governs the accounting events of one
business process.** The same shipment can produce an inventory-relief entry dated on validation day, a
revenue entry dated in a later period than the tax invoice shows, and a cost entry dated with the
revenue rather than with the goods. The three are never required to agree, and nothing detects when they
do not.

**`DESIGN CANDIDATE` DC-06-01.** SMEsPlus must define **one** accounting-date rule per accounting event
class, declared, and every event must carry both the **occurrence date** (when the business fact
happened) and the **recognition date** (which period it is reported in), with any difference between
them being an explicit, recorded, authorised act — never a silent side effect of a lock date or a
system clock.

## 3. Events That Do Not Exist

Stated per the Negative Claim Control.

| Expected accounting event | Classification | Search boundary |
|---|---|---|
| **Year-end profit-and-loss → retained-earnings closing entry** | `NOT FOUND IN SEARCHED SCOPE` | Six patterns over the whole reference addon root, translations and tests excluded. The only closing-entry generator found is for VAT. **Localisation modules were not separately enumerated as their own denominator** (T4 §10 open item). |
| **Deferred / unearned revenue on billing before delivery** | `NOT FOUND IN SEARCHED SCOPE` | Invoice-line account derivation, order-to-invoice preparation and the down-payment path, in the sales and accounting modules. Deferred-revenue and subscription modules **not searched**. |
| **Bad-debt provision / impairment / allowance** | `NOT FOUND IN SEARCHED SCOPE` | Case-insensitive `bad.?debt|doubtful|allowance for` over all source and data files in the population; 2 hits, both unrelated. **The terms "provision", "impairment" and "credit loss" were not searched.** |
| **Withholding-tax accrual or certificate event on a customer receipt** | `VERIFIED ABSENCE` within the Thai localisation | No withholding certificate model, no withholding sequence, and no flag anywhere in the 791-module root; the sale-side withholding taxes carry no report tags, so customer-withheld tax reaches neither statutory report. T3 §5 |
| **An exception event for delivered-not-invoiced ageing** | `NOT YET SEARCHED` | Reporting layers were out of scope for the tracks run in this session. Must be searched before this claim is used. |

## 4. Double-Posting Attack Results

| Attack | Result | Tag |
|---|---|---|
| **Double inventory relief** on one outflow | **Blocked procedurally, not structurally.** The already-completed check is a filter within one call, not a database constraint; there is **no uniqueness key** on (movement, valuation layer). A completed movement cannot be cancelled or reversed, and the only path back is a return, which is a *new* event with its own entry. Corrected after independent challenge, which noted the package applied a stricter standard to cost-of-sales than to this. | `FACT VERIFIED` `EV-P02-022`, T1 §6 |
| **Double cost of sales** on one invoice | **No idempotency guard exists.** Protection is ordering-dependent, not structural. Residual exposure detailed in `03_P02_DELIVERY_COGS_TRACE.md` §6. | `FACT VERIFIED` (absence) / `UNRESOLVED — EVIDENCE REQUIRED` (exploitability) |
| **Double revenue** on one order | **Defaulted, not blocked**, through the order path — the billable quantity supplies the invoice line's *default* quantity and **no constraint ties an invoice line to an order line's remainder** (`EV-P02-066`); the quantity is editable on the draft. Not addressed at all through a manual invoice or a hand-made credit note. A duplicate **detector** covering customer invoices does exist — same company, partner, type, total and date — but **no code path consults it for a sale document**, and its database index is created for purchase documents only. | `FACT VERIFIED` `04_P02_REVENUE_AR_TRACE.md` §4, §11 |
| **Double tax** | Follows revenue exactly — same document, same lines. **No independent tax duplication path found** in the searched scope. | `NOT FOUND IN SEARCHED SCOPE` |
| **Double settlement** | Matching consumes the smaller residual, so a second match against a settled line allocates zero. **Blocked by arithmetic.** But matching rows are **freely destructible across a closed period**, so the *state* is not durable. | `FACT VERIFIED` T2 §2, §7 |
| **Double valuation** of one physical unit | **Reachable.** The unit is valued once by the outflow layer and again, independently, by the invoice-post cost re-derivation, with a standard-price top-up when the layers are insufficient. The two are reconciled by **balance matching in a clearing account**, not by identity. | `FACT VERIFIED` `03_P02_DELIVERY_COGS_TRACE.md` §1, §4 |

**`FACT VERIFIED` — P02-F-36.** Of the six attacks, **two are structurally blocked** (inventory relief,
settlement arithmetic), **one is blocked only along the happy path** (revenue via the order),
**one has no guard at all** (cost of sales), **one is unexamined outside the searched scope** (tax), and
**one succeeds by design** (double valuation, reconciled after the fact rather than prevented).
