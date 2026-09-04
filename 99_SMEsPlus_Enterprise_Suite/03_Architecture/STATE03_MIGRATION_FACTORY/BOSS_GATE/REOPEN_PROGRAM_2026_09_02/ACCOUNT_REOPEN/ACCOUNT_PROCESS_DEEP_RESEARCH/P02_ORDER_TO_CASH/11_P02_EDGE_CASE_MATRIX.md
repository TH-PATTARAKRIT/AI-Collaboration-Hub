# 11 — P02 EDGE CASE MATRIX

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

The directive requires every lifecycle verb to be researched:
CREATE · CONFIRM · POST · PARTIAL · CANCEL · REVERSE · RETURN · REFUND · CORRECT · BACKDATE ·
CLOSE · REOPEN · LOCKED PERIOD.

## 1. Lifecycle Verb Matrix

| Verb | Order | Delivery | Invoice | Payment | Matching |
|---|---|---|---|---|---|
| **CREATE** | free | from the order line, via the routing rule | free (manual or from the order) | free | implicit in registering a payment |
| **CONFIRM** | overwrites the order date with the system clock | validation with a company check | n/a | n/a | n/a |
| **POST** | n/a | completion, gated on a **picked** marker | **the single densest control point in P02** | may produce **no entry at all** | may emit FX and cash-basis entries |
| **PARTIAL** | n/a | backorder, consistent by construction | partial billing reduces billable quantity; **drafts count** | partial allocation consumes the smaller residual | leaves **two** residuals |
| **CANCEL** | reversible to draft | **impossible once complete** | destroys the cost lines | resets and unmatches | destroys matching rows, **even across a closed period** |
| **REVERSE** | n/a | **only via a return** | credit note — **four different cost bases** | payment reversal | reverses derived entries, re-dated forward |
| **RETURN** | n/a | inbound movement; value depends on the costing method | **no automatic invoice consequence** | n/a | n/a |
| **REFUND** | n/a | n/a | credit note ≠ refund | a payment in the opposite direction | ordinary matching |
| **CORRECT** | free | **quantity correctable on a completed movement**, creating new layers dated **today** | reset to draft, edit, re-post — **cost may change value** | edit blocked once matched, **with a carve-out** | destroy and redo |
| **BACKDATE** | confirmation cannot be backdated | **the valuation entry is always dated today** | the document date is free; **the accounting date may be moved forward silently** | free | derived entries re-dated forward |
| **CLOSE** | n/a | **the stock side has no concept of a lock date** | blocked only for four transitions | — | **not gated at all** |
| **REOPEN** | unlock a locked order — a free boolean | n/a | reset to draft unless hashed | reset to draft | free |
| **LOCKED PERIOD** | n/a | **no reference to a lock date anywhere on the stock side** | **redirect, not bar** | — | **no gate** |

## 2. Partial Delivery / Partial Invoice / Backorder

| Case | Behaviour | Tag |
|---|---|---|
| Partial delivery under delivery-based billing | Billable quantity rises with each completed outflow; the split preserves the total; the remainder is not re-procured. **Consistent by construction.** | `FACT VERIFIED` T1 §7 |
| Partial delivery under order-based billing | Billable quantity is **unaffected by delivery entirely**. | `FACT VERIFIED` `EV-P02-004` |
| Backorder in ask mode | The user is asked; the remainder is split. | `FACT VERIFIED` T1 §7 |
| **Backorder in never mode** | **The undelivered remainder is cancelled outright.** Delivered quantity permanently reports the short quantity while the ordered quantity still shows the full order, leaving billable quantity short **with no document trail beyond the cancelled movements**. | `SUPPORTED INTERPRETATION` T1 §7 |
| Partial invoice | Every non-cancelled invoice, **including drafts**, reduces billable quantity. | `FACT VERIFIED` `EV-P02-005` |
| Partial payment | Consumes the smaller of the two residuals; leaves a pair. | `FACT VERIFIED` T2 §2 |

## 3. Over-Delivery

**`FACT VERIFIED` — P02-F-13 (restated).** Two opposite behaviours from one physical event:

- under **order-based** billing, over-delivery is **capped** and surfaced as an upselling status;
- under **delivery-based** billing, over-delivery is **billed without comment**, above the ordered
  quantity.

## 4. Cancellation And Reversal

| Object | Can it be cancelled after taking effect? | What is destroyed |
|---|---|---|
| Order | yes — status only | nothing financial |
| **Completed delivery** | **NO** — the strongest control in P02 | — |
| Posted invoice | yes, to draft or to cancelled | **the cost-of-sales lines**; revenue lines are retained as content |
| Payment | yes | matching on every invoice it touched |
| **Matching** | **yes, freely, across a closed period** | the settlement history itself |

**`FACT VERIFIED` — P02-F-47.** The durability ordering is inverted relative to accounting importance:
**the physical event is immutable, the accounting event is reversible, and the settlement history is
freely destructible.**

## 5. Correction And Backdating

| Case | Finding | Tag |
|---|---|---|
| Correcting a completed movement's quantity | Permitted. Produces **new** correction layers and a **new** journal entry — nothing is amended in place. Correct design. | `FACT VERIFIED` T1 §6 |
| **The date of that correction entry** | **Today** — not the movement it corrects. A correction made on the 30th books in a different period from the movement. | `FACT VERIFIED` T1 C8 |
| **The date of the original valuation entry** | **Today** — not the movement's own date. A picking validated on the 3rd for goods that left on the 1st books on the 3rd. | `FACT VERIFIED` T4 §8 |
| Re-pointing a completed movement's locations across the valuation boundary | **Blocked.** | `FACT VERIFIED` T1 §6 |
| Backdating an invoice | The document date is free. The accounting date **may be silently moved forward**. | `FACT VERIFIED` `EV-P02-013` |
| **Backdating a stock valuation entry** | The **only** path is a user-writable accounting-date field on the inventory-adjustment route, which has **no constraint and no lock comparison**. Complete denominator: **8 lines, 3 files; not one tests a lock date.** | `FACT VERIFIED` T4 §8 |

## 6. Locked Period — The Consolidated Finding

**`FACT VERIFIED` — P02-F-48 (TOLERANCE-ZERO CANDIDATE, HEADLINE).**
**The reference's lock date is a period REDIRECT, not a period BAR.**

What it actually blocks (T4 §6a) — **four transitions only**, every one conditioned on the document
already being posted:

1. changing the name or date of an already-posted document;
2. un-posting one;
3. writing a date into the locked period on a document that is or becomes posted;
4. tax-affecting line edits on a posted document.

**Document creation performs no lock check whatsoever.** A draft entry dated inside a locked period can
be created freely.

What it silently reschedules instead of blocking (T4 §6b) — **four paths**: posting, document
duplication, cash-basis tax entries, and the computed accounting date on purchase documents. The user is
**warned, not stopped**, and the warning is not retained on the document.

Who can override (T4 §6c) — **three mechanisms**:

| Mechanism | Reach | Control |
|---|---|---|
| A lock exception record | the four soft locks | an accounting-manager group; **an exception with no user applies to everyone and one with no end date is permanent** — the code says so in its own comments |
| **A context sentinel that skips the check entirely** | **every lock including the hard lock** | **none — it is disabled by construction, not by permission.** Complete denominator: 5 lines, 3 files, **2 use sites, both in partner merge** |
| Moving the lock date itself | the four soft locks | **soft lock dates can be moved backwards freely** |

And **the stock side has no concept of a lock date at all** — zero matches across the inventory,
inventory-accounting, sales and sales-inventory modules.

**`FACT VERIFIED` — P02-F-49.** The consequence for P02 specifically: **where a lock date shifts a
valuation entry, the inventory valuation report and the general ledger disagree for that period, and
nothing detects or reports the divergence.** The valuation layer has **no accounting date of its own** —
its only temporal key is its creation timestamp, which is also what valuation reporting is keyed on,
while the ledger is keyed on the accounting date that posting may have moved.

**`DESIGN CANDIDATE` DC-11-01.** In SMEsPlus a period close must **bar at create**, not redirect at post;
must gate the **matching state** as well as the entries; must have **no context-level bypass**; must
require any exception to be **scoped, time-bounded, attributed and audited**; and must extend to the
valuation side, which currently does not participate in close at all.

## 7. Thai Statutory Edge Cases — All Held

Eight questions, each with named sources, each `HOLD — STATUTORY EVIDENCE REQUIRED`. Full three-layer
separation — what the code does / what the localisation asserts / what the law requires — is in
`L2_AUDIT_QUARANTINE/T3_TAX_VAT_WHT_THAI_EVIDENCE.md` §9.

| ID | Question | Sources named |
|---|---|---|
| S-01 | Which date is the VAT tax point, and may a tax invoice bearing one date be declared in a later period? | Revenue Code ss.78, 78/1, 86, 86/4 and the notifications thereunder |
| S-02 | Is VAT on services due on receipt, and is an accrual-only configuration compliant? | Revenue Code s.78/1(1), s.82/3 |
| S-03 | May the accounting-system invoice serve as the tax invoice, and what are its mandatory particulars and branch numbering? | Revenue Code s.86/4 and the tax-invoice notification |
| S-04 | Do the shipped reports correspond to the statutory filing forms? | Revenue Department forms P.P.30, P.N.D.3, P.N.D.53 and their e-filing specifications |
| S-05 | Is the hard-coded withholding condition correct, is the rate→income-type mapping exhaustive, and are the rates current? | Revenue Code ss.3 tredecim, 50, 69 bis, 69 ter; Departmental Instruction Tor.Por. 4/2528 as amended |
| S-06 | Must a withholding certificate be issued and retained, and how is customer-withheld tax evidenced and claimed? | Revenue Code s.50 bis and the certificate notification |
| S-07 | Does Thai law require gap-less, immutable, sequentially numbered tax invoices? | Revenue Code s.86/4(2), s.87; Accounting Act B.E. 2543 |
| S-08 | Is 7% the currently effective standard rate, and must other rates be reported separately? | Revenue Code s.80 and the current Royal Decree |

**The one O2C-specific tax finding that is not statutory but structural:**

**`FACT VERIFIED` — P02-F-50.** The **sale-side** withholding taxes carry **no report tags**, while all
eight purchase-side ones do. Because the statutory withholding reports select rows **exclusively by tag**,
**withholding suffered on the company's own receipts appears on neither report.** This is a code fact, not
a legal one, and it is asymmetric within the localisation itself.

## 7a. Discount And Promotion

The directive names discount and promotion explicitly. Findings:

| Case | Behaviour | Tag |
|---|---|---|
| **Line discount** | A percentage on the order line, **stored and writable**, copied verbatim to the invoice line. Tax is computed on the **post-discount** unit price, so revenue and tax share one base. | `FACT VERIFIED` `EV-P02-058`, `EV-P02-062`, `EV-P02-078` |
| **Whole-order discount** | Applied as a **separate order line** carrying a company-configured discount product, constrained to be a **service billed on ordered quantity**. | `FACT VERIFIED` `EV-P02-079` |
| **The accounting consequence of that constraint** | Because the discount product is a **service billed on order**, a whole-order discount is billable **immediately and in full**, independent of what has been delivered. Under delivery-based billing this means **the discount can be recognised before the revenue it discounts.** | `SUPPORTED INTERPRETATION` |
| **The guard that exists** | A discount line is flagged as one that should **not be invoiced alone**, and an order whose only billable lines are such lines is reported as having nothing to bill. | `FACT VERIFIED` `EV-P02-080` |
| **What the guard does not cover** | It prevents a discount-only invoice. It does **not** prevent a partial delivery invoice from carrying the **whole** discount, because the discount line's billable quantity is not proportioned to delivery. | `SUPPORTED INTERPRETATION` |
| **Which account the discount hits** | The discount product's own income account — so a discount is **negative revenue on a possibly different account**, not a reduction of the revenue line it discounts. | `FACT VERIFIED` `EV-P02-026` |
| **Promotions and loyalty** | **NOT YET SEARCHED.** The loyalty and promotion modules are outside the declared path set. **This is a declared exclusion, not a verified absence**, and promotions are a plausible source of further O2C accounting events. | `NOT YET SEARCHED` |

**`DESIGN CANDIDATE` DC-11-02.** A discount is a **modification of the revenue of specific obligations**,
not an independent service line. In SMEsPlus it must be proportioned to the obligations it discounts and
must reduce the revenue of those obligations, so that a partial delivery carries a partial discount and
the discount cannot be recognised before the revenue.

## 8. Multi-Company And Intercompany Edge Cases

| Case | Finding | Tag |
|---|---|---|
| **Single-step cross-company delivery of a valued product** | **Refused at validation** with an explicit message. The strongest single boundary found. | `FACT VERIFIED` T4 §5 |
| The same for a **non-storable** or **manual-valuation** product | **The gate is never reached.** | `SUPPORTED INTERPRETATION` T4 §5 |
| Which company's accounts are used for a valuation entry | **Always the movement's own.** There is **no code path** in which the destination company's accounts are consulted. | `FACT VERIFIED` T4 §5 |
| **Matching across two legal entities** | **Permitted** where they share a root company. | `FACT VERIFIED` T4 §3 |
| Intercompany invoice pair — same total? | **No guarantee.** The untaxed amount is copied; **taxes are re-computed under the counterparty's fiscal position**, and nothing compares the totals afterwards. | `FACT VERIFIED` T4 §4 |
| Intercompany pair — same accounting date? | **No guarantee**, and the divergence is silent. | `SUPPORTED INTERPRETATION` T4 §4 |
| Intercompany pair — same rate? | **No.** Separate root companies read independent rate tables, and a missing rate silently yields 1.0. | `SUPPORTED INTERPRETATION` T4 §4 |
| Who executes the mirror | A configured user **defaulting to the superuser**, locating the counterparty with an **unscoped** search over the whole company table. | `FACT VERIFIED` T4 §4 |
| Rewriting a confirmed order's company | **Not guarded.** The form exposes the field with no read-only, in contrast to its neighbours; and **nothing re-companies the already-created pickings or invoices**. | `FACT VERIFIED` / `SUPPORTED INTERPRETATION` T4 §1 |

## 9. Complete Edge-Case Inventory — 34 Cases

| # | Case | Outcome | Class |
|---|---|---|---|
| 1 | Invoice before delivery | reachable; cost at standard price; permanent clearing residual | defect class |
| 2 | Delivery before invoice | intended shape | ok |
| 3 | Delivered, never invoiced | permanent clearing debit, no ageing | defect class |
| 4 | Billed, never delivered | permanent clearing credit at standard price | defect class |
| 5 | Outflow complete, no picked line | **no financial record at all** | tolerance-zero |
| 6 | Consumable product sold | no cost effect anywhere | by design, but silent |
| 7 | Owner-restricted stock sold | valuation excluded; **cost line still created** | defect class |
| 8 | Partial delivery, order billing | no billing effect | by design |
| 9 | Partial delivery, delivery billing | consistent | ok |
| 10 | Backorder, ask/always | consistent | ok |
| 11 | Backorder, never | short quantity, no trail | defect class |
| 12 | Over-delivery, order billing | capped, surfaced | ok |
| 13 | Over-delivery, delivery billing | billed silently | defect class |
| 14 | Draft invoice consumes billable quantity | blocks double invoicing | ok, but ordering-dependent |
| 15 | Manual invoice for ordered goods | **outside every control** | defect class |
| 16 | Invoices merged across orders | header provenance is free text | defect class |
| 17 | Reset to draft and re-post | cost may change value silently | defect class |
| 18 | Credit note, no return | cost reversed at today's standard price; unmatched debit | defect class |
| 19 | Return, no credit note | revenue never reversed | defect class |
| 20 | Return with the refund-intent flag off | no billing effect at all | defect class |
| 21 | Hand-made credit note | order still reads fully invoiced | defect class |
| 22 | Full reversal dated tomorrow | silently downgrades to a re-derived cost basis | defect class |
| 23 | Return of a return | cost-stable through one hop | ok |
| 24 | Inbound picking from the customer location with no origin link | **entry says return, layer says receipt** | contradiction |
| 25 | Down payment with no advances account | **revenue recognised on a deposit** | tolerance-zero |
| 26 | Overpayment | invisible unapplied credit; invoice reads paid | defect class |
| 27 | Underpayment | partial | ok |
| 28 | Missing exchange rate | **silent neighbouring rate, else 1.0** | tolerance-zero |
| 29 | Write-off to an arbitrary account | permitted | defect class |
| 30 | Unmatching across a closed period | **permitted, ungated** | tolerance-zero |
| 31 | Posting into a locked period | **silently redirected** | tolerance-zero |
| 32 | Partner merge inside a hard-locked period | **check disabled by construction** | tolerance-zero |
| 33 | Valuation entry re-dated by a lock | **valuation report and ledger disagree, undetected** | defect class |
| 34 | Cross-company single-step delivery | **refused** | ok |
| 35 | Whole-order discount on a partially delivered order | discount billable in full while revenue is not | defect class |
| 36 | Discount-only invoice | **prevented** | ok |
| 37 | Promotion / loyalty interaction | **NOT YET SEARCHED** — outside the declared path set | unknown |

**37 cases: 8 sound, 21 defect classes, 7 tolerance-zero candidates, 1 unknown.**
The seven tolerance-zero candidates are carried to `18_P02_PMO.md` §3 under EC-04.
**The one unknown (case 37) is a declared exclusion, not a verified absence**, and is recorded as such in
`14_P02_EVIDENCE_MANIFEST.md` §2.2.
