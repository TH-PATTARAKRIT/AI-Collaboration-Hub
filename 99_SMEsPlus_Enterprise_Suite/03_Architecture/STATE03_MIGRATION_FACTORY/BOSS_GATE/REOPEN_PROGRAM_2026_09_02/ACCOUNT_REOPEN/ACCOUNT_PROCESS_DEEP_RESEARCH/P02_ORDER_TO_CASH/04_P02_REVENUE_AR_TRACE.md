# 04 — P02 REVENUE → RECEIVABLE FORENSIC TRACE

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 0. The Question This File Answers

> **When does revenue arise, when does the receivable arise, and who owns each?**

Answer: **both arise at exactly one moment — the posting of a customer invoice — and both are owned
by that invoice.** This is the *cleanest* part of P02. The defects are not in *when* revenue arises;
they are in *what date it is stamped with*, *which accounts it lands in*, and *how many times the
same commercial fact can travel this path*.

## 1. The Trace, Hop By Hop

```
 [H1] Order line          price, discount, tax set, currency          <-- COMMERCIAL TRUTH
        |
 [H2] Billable quantity   f(invoice policy, delivered, invoiced)      <-- see file 02
        |
 [H3] Invoice line        quantity + price + discount + tax, copied verbatim from H1
        |
 [H4] Invoice post        --> Dr Receivable  / Cr Revenue / Cr Output tax   <-- GL EFFECT
        |                     (+ Dr Cost of Sales / Cr Interim -- see file 03)
        |
 [H5] Receivable subledger line, carrying two residuals
        |
 [H6] Settlement + reconciliation                                     <-- see file 09
```

## 2. H1 → H3: What Is Copied, And What Is Frozen

**`FACT VERIFIED`** — the invoice line is built by copying the order line's price, discount and tax
set verbatim, and linking back to the order line — `EV-P02-058`.

The commercial terms are therefore **frozen at order time**, not re-derived at invoice time. Three
consequences, each `FACT VERIFIED`:

| Frozen at order time | Consequence |
|---|---|
| Unit price and discount | A price-list change between order and invoice has no effect. Correct. |
| **Tax set** | A change to the customer's tax treatment between order and invoice has **no effect** on the eventual invoice — `EV-P02-059`. |
| Fiscal position (header) | Copied from the order's stored value — `EV-P02-060`. |

**`FACT VERIFIED` — P02-F-26.** The tax recomputation trigger on the order line **does not include
the fiscal position**, and the equivalent trigger on the invoice line does not include the document's
fiscal position either — `EV-P02-059`. Changing a customer's tax treatment after order confirmation
therefore changes nothing automatically; a **manual button** must be pressed, and pressing it posts a
note recording which position was applied — `EV-P02-061`.

**`SUPPORTED INTERPRETATION` — P02-F-27.** This is a defensible design (commercial terms should not
mutate under the customer's feet), but it means the tax charged on an invoice is **the tax that was
correct when the order was taken**, not the tax that is correct when the supply occurs. For a
long-lived order spanning a rate change or a customer's registration change, that is a substantive
question, not a technicality.

**`HOLD — STATUTORY EVIDENCE REQUIRED` — P02-S-02.** Which of the two dates governs the applicable
VAT rate and treatment under Thai law is a statutory question. Routed to the Accounting-Tax track.

## 3. H4: The Revenue And Receivable Entry

### 3.1 Revenue account derivation

`FACT VERIFIED` `EV-P02-026`. Resolution order for a product line on a customer invoice:

1. the product's (or its category's) **income** account;
2. if the line has **no product** but has a partner — the account **most frequently used** for that
   partner, company, document type and journal in the past;
3. if still empty — the account used by the previous two lines of the same type, if they agree;
4. otherwise the journal's default account.

Then the fiscal position remaps the result.

**`FACT VERIFIED` — P02-F-28 (STATISTICAL ACCOUNT SELECTION).** Step 2 selects a general-ledger
account by **historical frequency**. This is a convenience heuristic in an interactive context; as a
posting rule it means the account a line lands in is a function of what other users happened to do
before, and it is not reproducible from the transaction alone.

**`DESIGN CANDIDATE` DC-04-01.** SMEsPlus must not select a posting account by frequency. Account
derivation must be a total function of (product or service class, fiscal position, company, scope) —
deterministic, replayable, and explainable on the journal item itself.

### 3.2 Receivable account derivation

`FACT VERIFIED` `EV-P02-026`. Resolution order:

1. a receivable account already present on the same document;
2. the **commercial partner's** receivable property (per company);
3. the **company's own partner** receivable property;
4. otherwise, the **first non-deprecated receivable account of the company**, selected by a raw
   ordering with no business meaning.

Then the fiscal position remaps the result.

**`FACT VERIFIED` — P02-F-29 (ARBITRARY-FALLBACK CONTROL ACCOUNT).** Step 4 will post a customer
receivable to whichever receivable account the database returns first. It cannot fail; it can only be
wrong. Under a chart with more than one receivable account — and the Thai chart ships **two**, an
ordinary receivable and a point-of-sale receivable (`EV-P02-044`) — this fallback is materially
reachable.

**`DESIGN CANDIDATE` DC-04-02.** A missing receivable control account must be a **hard stop**, never a
silent selection.

### 3.3 Tax

Covered in `L2_AUDIT_QUARANTINE/T3_TAX_VAT_WHT_THAI_EVIDENCE.md` §3. The two points that belong in the
revenue trace:

- **`FACT VERIFIED`** — tax is computed on the **post-discount** unit price (`EV-P02-062`), so revenue
  and tax share one base. Correct.
- **`FACT VERIFIED`** — under global rounding, the rounding difference is absorbed **inside the tax
  amounts themselves**, pushed onto the largest contributing bucket and then distributed one currency
  unit at a time across base lines ordered by descending total (`EV-P02-063`). There is no separate
  rounding line and no separate account. The rounding-type line that does exist on a document is the
  **cash-rounding** line, a different mechanism entirely (`EV-P02-064`) — and under its default
  strategy it **carries tax tags and therefore reaches the VAT return** (`EV-P02-065`).

**`CONTRADICTED` — P02-C-02.** The common reading that the rounding line on an invoice is the
tax-rounding residue is wrong. Two different residues exist, produced by two different mechanisms, and
only one of them is visible as a line.

### 3.4 Date

Two dates, resolved by different rules, analysed in `01_P02_PROCESS_MAP.md` S7. The revenue-specific
restatement:

**`FACT VERIFIED` — P02-F-30.** If the document date is blank at posting it is **set to the system's
current date** for a customer invoice, whereas for a vendor bill a blank date is a hard error
(`EV-P02-012`). Revenue's date of record is therefore machine-asserted on the sales side and
human-asserted on the purchase side. The standard order-to-invoice entry point cannot supply the date
at all — its date argument is documented as unused (`EV-P02-010`).

**`DESIGN CANDIDATE` DC-04-03.** The date on which revenue is recognised must be an **explicit,
required, human-asserted input** with the same rigour on both sides of the ledger. A system clock is
not an assertion.

## 4. The Double-Revenue Attack

Four independent attempts, each with its evidenced outcome.

| # | Attack | Outcome | Tag | Evidence |
|---|---|---|---|---|
| 1 | Invoice the same order line twice from the order | **Blocked.** Billable quantity is reduced by every non-cancelled invoice, including **drafts**. | `FACT VERIFIED` | `EV-P02-005`, `EV-P02-004` |
| 2 | Invoice the order, then raise a manual invoice for the same goods | **Not blocked.** A manual customer invoice has no relationship to the order and no counter constrains it. | `FACT VERIFIED` | `EV-P02-066` |
| 3 | Post, reset to draft, post again | **Blocked** for revenue: the same document cannot be posted twice while posted, and re-posting re-derives the same lines. **Not equivalent for cost** — see `03_P02_DELIVERY_COGS_TRACE.md` §7. | `FACT VERIFIED` | `EV-P02-054`, `EV-P02-017` |
| 4 | Credit-note the invoice, then re-invoice the order | **Reachable, and asymmetric.** A credit note raised **through the reversal path or from the order** carries the order-line link and restores billable quantity, so re-invoicing is intended. A credit note raised **by hand in Accounting** does **not** carry the link, does **not** restore billable quantity, and the order continues to read as fully invoiced while its revenue has been reversed. | `FACT VERIFIED` | T1 §5 |

**`FACT VERIFIED` — P02-F-31 (HEADLINE FOR THIS FILE).** The double-revenue control is **entirely
order-centric**. It lives in a counter on the order line. Every path that does not go through the
order — a manual invoice, a hand-made credit note — is outside the control. The receivable ledger
itself has **no** duplicate-recognition control at all.

**`DESIGN CANDIDATE` DC-04-04.** The duplicate-revenue control must sit on the **economic obligation**
(the shipped/performed unit), not on the order document. Every revenue-recognising document must
consume from the same obligation ledger, whatever route created it.

## 5. Order ↔ Invoice Identity

**`FACT VERIFIED` — P02-F-07 (restated with consequence).** Invoices are, by default, **merged across
sale orders** grouped by (company, partner, currency) — `EV-P02-009`, `EV-P02-010`. The originating
order references are then joined into a **comma-separated free-text field** on the header. The only
structural link is the per-line relation.

Consequences:

- Header-level "which order produced this invoice" is a **character field**, not a relation
  (`EV-P02-072`). A header-level *view* of the source orders **is** derivable — a computed, non-stored
  count traverses line → order-line link → order (`EV-P02-073`) — but it is a traversal through the line
  link, not a stored header relation. **Any database-level join at header level is a join on text.**
  `FACT VERIFIED`
- One invoice can carry revenue belonging to several commercial commitments, with different delivery
  states, different fiscal positions at origin, and different cost-recognition consequences.
  `SUPPORTED INTERPRETATION`
- **Grouping is silent and is the default.** The caller must explicitly ask *not* to group.
  `FACT VERIFIED` `EV-P02-010`

**`DESIGN CANDIDATE` DC-04-05.** Consolidated billing is a legitimate business requirement, but the
consolidated document must be a **first-class object with structural links to every source
obligation**, not a header string. Grouping must be an explicit, recorded decision, never a default.

## 6. H5: The Receivable Subledger Line

**`FACT VERIFIED`** — the receivable line carries **two residuals**, one in company currency and one in
the line's own currency, and counts as settled only when **both** are zero (`EV-P02-067`). Under
multi-currency the two can disagree, and that disagreement is precisely the state the exchange
difference entry exists to clear.

**`FACT VERIFIED`** — residuals are computed **only** for lines on reconcilable accounts (plus
cash and credit-card types); every other line is hard-set to zero (`EV-P02-068`). Residual is not a
general property of a journal item.

**`SUPPORTED INTERPRETATION` — P02-F-32.** Any receivable ageing, dunning or exposure report that reads
one residual and not the other will disagree with the settled flag in exactly the multi-currency cases
— i.e. exactly where the exposure matters most.

## 7. Answers To The Directive's Explicit Questions

| Question | Answer | Tag |
|---|---|---|
| **When does revenue arise?** | At customer-invoice post. Never before — order confirmation and delivery have no revenue effect. | `FACT VERIFIED` |
| **When does the receivable arise?** | At the same instant, from the same document. | `FACT VERIFIED` |
| **Who owns the revenue event?** | The customer invoice. | `FACT VERIFIED` |
| **What date is revenue recognised on?** | The accounting date, which may be silently later than the document date the customer is shown. | `FACT VERIFIED` |
| **Can revenue arise without a shipment?** | Yes — under invoice-on-order (the platform default for goods), and via any manual invoice. | `FACT VERIFIED` |
| **Can a shipment occur without revenue?** | Yes — delivered-not-invoiced is an ordinary, uncontrolled state with no ageing and no exception report. | `FACT VERIFIED` |
| **Is revenue reversed when goods come back?** | **Only if somebody raises a credit note.** A physical return has no revenue effect of its own. | `FACT VERIFIED` |

## 8. Deferred / Unearned Revenue

**`NOT FOUND IN SEARCHED SCOPE` — P02-N-01.** No mechanism was found that recognises a liability for
billed-but-not-yet-delivered goods in the O2C path. Under invoice-on-order the credit goes straight to
the revenue account. Search boundary: the invoice-line account derivation, the order-to-invoice
preparation, and the down-payment path, in the sales and accounting modules. **Not searched:** deferred
revenue / subscription-revenue modules, which exist in the reference tree and may provide this
separately.

**`BOSS CONTROLLED DECISION` — P02-B-02.** Whether SMEsPlus recognises revenue on billing or on
performance is a revenue-recognition policy decision with statutory consequences (TFRS 15 / TAS 18
lineage). It cannot be inherited from a reference ERP's default. Routed to the Accounting-Tax track and
to Core Accounting Reconciliation.

## 9. Down Payments / Customer Deposits — Revenue Consequence

Full evidence in `L2_AUDIT_QUARANTINE/T2_PAYMENT_RECONCILIATION_EVIDENCE.md` §4. The revenue-trace
statement:

**`FACT VERIFIED` — P02-F-33 (TOLERANCE-ZERO CANDIDATE).** A customer down payment produces a **real
posted customer invoice**, and the account it credits is resolved as
`down-payment account, or else the income account`. If the down-payment property is not configured,
**the deposit is recognised as immediate revenue.** In the reference tree as shipped, no chart template
supplies that property, so the fallback is the live path.

The final invoice then reverses the down payment as a **negative line on the same account** — so
liability treatment and revenue treatment reach the same final balance and differ **entirely in the
interim period's reported revenue**. `SUPPORTED INTERPRETATION`.

**`DESIGN CANDIDATE` DC-04-06.** In SMEsPlus a customer advance must be a **contract liability by
construction**, not by configuration. The account must not be resolvable to revenue, and the release of
the liability must be an explicit accounting event, not a negative line inheriting the deposit's account.

## 10. Negative Claims

| Claim | Classification | Search boundary |
|---|---|---|
| Order confirmation creates no revenue and no receivable | `NOT FOUND IN SEARCHED SCOPE` | Confirmation routine and its extension point; no accounting-document creation reached. Localisation and third-party extensions not searched. |
| No unearned-revenue mechanism exists in the O2C path | `NOT FOUND IN SEARCHED SCOPE` | Invoice-line account derivation, order-to-invoice preparation, down-payment path — sales and accounting modules only. Deferred-revenue and subscription modules **not** searched. |
| The receivable ledger has no duplicate-recognition control | `NOT FOUND IN SEARCHED SCOPE` | The posting routine and its overrides, plus the document-level constraint set. Searched for uniqueness constraints on (partner, amount, date) and for any duplicate-invoice detection; the only detection found is an advisory abnormal-amount/date warning that is **disabled by default** (`EV-P02-069`). |
