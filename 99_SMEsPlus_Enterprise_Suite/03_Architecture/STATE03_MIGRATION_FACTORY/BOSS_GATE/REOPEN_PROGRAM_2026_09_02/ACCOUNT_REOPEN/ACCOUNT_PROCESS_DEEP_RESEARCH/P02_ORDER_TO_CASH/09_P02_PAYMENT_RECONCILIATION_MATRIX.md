# 09 — P02 PAYMENT / SETTLEMENT / RECONCILIATION MATRIX

> ## ⚠ GENERATION BANNER — `C-35`, RAISED BY AAS-03 EXPERT 3 AND CONFIRMED AGAINST SOURCE
>
> **Every Thai-localisation negative in this file was established against the v18 root only, and the
> v19 Thai chart is a different artefact: 144 accounts, not 27** (verified: `l10n_th/data/template/
> account.account-th.csv`, 27 data rows in v18 vs **144** in v19).
>
> Confirmed refutations in the v19 root — all inside P02's own declared PATH SET:
>
> | v19 evidence | Refutes |
> |---|---|
> | `account.account-th.csv:57` `212400 Advances from Customers` + `models/template_th.py:16` `downpayment_account_id` | "no chart template supplies the down-payment account" (`P02-F-33`) |
> | `account.account-th.csv:58` `213100 Undue Output VAT`; `:9` `112190 Allowance for Doubtful Accounts` | 3 of the 4 "absent roles" (`P02-F-38`) |
> | `models/template_th.py:15` `property_stock_valuation_account_id` = `113100`, `:40` `account_stock_valuation_id` | "the Thai chart supplies none of the three stock accounts" (`C-01`/`RE-03`) |
> | `models/template_th.py:41` `tax_exigibility: 'True'` (absent entirely from v18) | "cash basis is not enabled by the Thai data" (`AE-10`) |
>
> **The general rule, which the package had not stated:** *P02's localisation negatives are
> single-generation negatives about a generation that no deployment runs.* That is sharper than the
> 189-module `SOURCE GAP`, because it needs no unreadable code to bite — the refutations sit in a root
> P02 itself declared.
>
> **What survives both roots:** the *Outbound Stock (Goods Delivered)* role is absent from both;
> `P02-F-50` (sale-side withholding reaches no report) — and Expert 3 strengthened it against the
> readable custom estate; `P02-F-51` (accounting date printed under "Invoice Date"); and `P02-F-52`'s
> first clause (4 of 6 VAT taxes carry an empty tax group).


`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Underlying evidence: `L2_AUDIT_QUARANTINE/T2_PAYMENT_RECONCILIATION_EVIDENCE.md`

## 0. The Directive's Question

> **How does payment differ from reconciliation?**

## 1. Four Distinct Events, Not One

| # | Event | Business meaning | Ledger effect |
|---|---|---|---|
| 1 | **Receipt** | the customer's money arrived somewhere | *Outstanding Receipts* debited, *Receivable* credited |
| 2 | **Allocation (matching)** | this money settles *that* debt | no entry — matching rows only; **may emit an exchange difference and a cash-basis tax entry** |
| 3 | **Bank confirmation** | the money is really in the bank | *Bank* debited, *Outstanding Receipts* credited |
| 4 | **Settlement state** | a *derived* summary of 1–3 | a computed field |

**`CONTRADICTED` — P02-F-43, CORRECTED.** The original wording was *"the reference process does keep
these separate, and does it well"*, tagged `FACT VERIFIED`. **That was wrong, and a peer process caught
it** — see `12_P02_CONTRADICTION_REGISTER.md` C-19 and `22` §11.

**Corrected statement — `FACT VERIFIED`: the separation exists ONLY in the outstanding-account
configuration.**

- Where the payment method line carries an outstanding account, the three steps are genuinely separable —
  create, post, then match — and matching is the step that changes the residual (T2 §1).
- Where it does not, **the payment produces no journal entry at all** (T2 §1), a payment booked straight
  to the bank account is **declared matched at creation** (T2 §5), and **the intermediate position does
  not exist**. The three events collapse into one.

The refuting evidence was **already in §2 of this same file**, two sections below the original claim.
Neither self-review, nor the independent challenge, nor the deployed-database pass caught the
inconsistency; a peer process reading P02 for its own purposes did.

**The design requirement is unchanged and is now the *only* safe reading:** collapsing "the customer paid"
into "the bank balance changed" destroys bank reconciliation, and SMEsPlus must make the intermediate
position **structural and non-optional** — which is `DC-09-01`, already stated below.

## 2. The Configuration That Breaks It

**`FACT VERIFIED` — P02-F-44 (SURPRISE, T2-S3).** **A payment may post no journal entry at all.** Entry
generation is filtered to payments that have an outstanding account, and an outstanding account is
force-assigned **only when the full-accounting module is absent**.

So the canonical "outstanding receipts then bank" narrative describes the **invoicing-only**
configuration. In the full-accounting configuration a payment may be booked **directly against the bank
account**, in which case:

- the intermediate state disappears entirely — the payment is declared matched at creation (T2 §5);
- the "money received but not yet cleared" position **does not exist**;
- bank reconciliation has nothing to reconcile.

**`DESIGN CANDIDATE` DC-09-01.** In SMEsPlus the outstanding/undeposited position must be
**structural and non-optional**. A receipt must always land in a clearing position and must always
require a separate bank-confirmation event to leave it.

## 3. Partial Settlement — Two Residuals, Not One

**`FACT VERIFIED` — T2 §2.** A receivable line carries **two** residuals — one in company currency, one
in its own currency — and is settled only when **both** are zero. A partial allocation carries **three**
amounts. Under multi-currency the two residuals can diverge, and that divergence is exactly the state the
exchange-difference entry exists to clear.

**`FACT VERIFIED` — T2 §2.** Residuals are computed **only** for lines on reconcilable accounts (plus
cash and credit-card types). Residual is not a general property of a journal item.

**`SUPPORTED INTERPRETATION` — P02-F-32.** Any ageing, dunning or exposure report reading one residual and
not the other will disagree with the settled flag **in exactly the multi-currency cases** — i.e. exactly
where the exposure matters most.

## 4. FX On Settlement — And The Silent Rate Fallback

**`FACT VERIFIED` — T2 §3.** Realised FX is recognised **at matching time**, not at receipt time, in the
company's exchange journal, with the account chosen by sign. **Its date is not the settlement date** — it
is the exchange journal's lock-adjusted date, raised to the later of the two line dates.

### The headline

**`FACT VERIFIED` — P02-F-45 (TOLERANCE-ZERO CANDIDATE).** Currency conversion has a **two-stage silent
fallback**:

1. the latest rate on or before the date; failing that,
2. **the earliest rate of ANY date, with no date filter at all**, ordered ascending; failing that,
3. the literal **1.0**.

**None of the three paths logs, warns, or raises.**

**`SUPPORTED INTERPRETATION` — T2-S2.** The dangerous arm is not the 1.0 — it is arm 2. *A company that
begins loading rates on 1 March will price every February settlement at the 1 March rate, silently.*
A 1:1 result is at least conspicuous. This is not.

**`SUPPORTED INTERPRETATION`** — this is the same defect class as the Account Wave A finding recorded
against the core ledger ("silent 1:1 FX fallback"). P02 does **not** re-adjudicate it; it confirms the
mechanism from the O2C side and adds arm 2, which is the more likely and less visible of the two.
**`HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` — P02-X-03**, routed to Core Accounting Reconciliation
alongside the existing Boss ruling on FX rate ownership and missing-rate policy.

**`FACT VERIFIED` — T2 §3.** Which date the rate lookup uses is **asymmetric**: for an invoice line it
uses the **document date**; for a payment or statement line no lookup happens at all — the rate is
back-derived from what was booked. And the payment register can **override the rate outright** through a
context key that takes precedence over every other branch.

**`DESIGN CANDIDATE` DC-09-02.** A missing rate must be a **hard stop**. Never a neighbouring rate, never
1.0. Every converted amount must record the rate used, its source, and its effective date on the journal
item itself.

## 5. Customer Deposits And Advances

**`FACT VERIFIED` — P02-F-33 (restated, TOLERANCE-ZERO CANDIDATE).** A down payment produces a **real
posted customer invoice**, and the account it credits is resolved as
*down-payment account, or else the income account*. If the down-payment property is unset —
**and no chart template in the reference tree supplies it** — the deposit is recognised as
**immediate revenue**.

The final invoice reverses it as a **negative line on the same account**. Liability treatment and revenue
treatment therefore reach the same final balance and differ **entirely in the interim period's reported
revenue**.

**`CONTRADICTED` — P02-C-03.** The down-payment state helper does **not** report whether a deposit has
been received. It reports only the parent document's draft/cancel status; a posted-and-unpaid and a
posted-and-paid down payment are indistinguishable through it.

## 6. Overpayment And Underpayment

| Case | Where the money sits | What the invoice says | Detection |
|---|---|---|---|
| **Under**payment | receivable, partially settled | *partial* | normal |
| **Over**payment | **an unapplied credit inside the receivable control account** — there is **no** customer-advances or unapplied-cash landing account in this path | **paid** | **the excess is invisible to the invoice's settlement state entirely; it lives only on the payment** |

**`FACT VERIFIED` — T2 §5, T2-S8.**

**`DESIGN CANDIDATE` DC-09-03.** Unapplied customer cash must be a **named position with its own ageing**,
not a net credit hidden inside the receivable control account.

## 7. Write-Off And Bad Debt

**`FACT VERIFIED` — T2 §6.**

- **The write-off account is unconstrained** — the only restriction is that it is not deprecated. Nothing
  prevents writing an unrecoverable receivable off to a **revenue** account, a liability, or another
  receivable.
- **Two mechanisms exist with different date behaviour**: the payment register forces the payment date;
  the reconcile wizard **silently re-dates past the lock** and only warns. *Same accounting event, two
  different period-assignment rules.*
- The write-off option is **hidden entirely** in the configuration where the payment method line has no
  outstanding account.

**`NOT FOUND IN SEARCHED SCOPE` — T2-N2.** No dedicated bad-debt, doubtful-debt or allowance mechanism was
found across the whole population under the declared pattern. **No provision matrix, no ageing-triggered
impairment, no allowance account, no reversal of provision on recovery.** Bad debt is a generic write-off
with a hand-picked account. Scope caveat retained: the terms *provision*, *impairment* and *credit loss*
were **not** searched.

**`DESIGN CANDIDATE` DC-09-04.** Impairment must be a **first-class accounting event** with a restricted
account role, an ageing trigger, and a defined reversal on recovery. A write-off to an arbitrary account
must not be reachable.

## 8. Unmatching — And The Period Hole

**`FACT VERIFIED` — P02-F-46 (TOLERANCE-ZERO CANDIDATE, T2 §7).** **The unreconcile path is not lock-date
gated.** The lock-date check has three call sites in the accounting document and line models and
**zero in the partial-reconciliation model.** Unlinking a matching row is not itself a lock violation.
Only the *consequential* reversal entries are re-dated forward.

**`SUPPORTED INTERPRETATION` — T2-S7.** The design treats the lock date as a constraint on **journal
entries**, not on **matching state**. **The audit trail of what was matched against what in a closed
period is mutable in a way the entries themselves are not.**

Two further findings on the same path:

- Resetting an accounting document to draft **removes matching on all its lines as a matter of course** —
  so resetting one payment unreconciles every invoice it touched. `FACT VERIFIED`
- The fiscal-lock check is **bypassable by a context sentinel**, whose only two use sites in the entire
  population are in **partner merge** — a contacts-role operation that rewrites fields on posted journal
  items inside a period protected by **every** lock date **including the hard lock**. `FACT VERIFIED`
  T4 §6(c).

**`SUPPORTED INTERPRETATION`.** This is the same defect the Account Wave A track recorded as *"hard lock
defeated by a contacts-role partner merge"*. P02 confirms it independently from the O2C side and
establishes its complete denominator: **5 lines, 3 files, 2 use sites.**
**`HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` — P02-X-04.**

**`DESIGN CANDIDATE` DC-09-05.** Matching and unmatching are **accounting events**, not metadata. They
must be period-controlled exactly as entries are, must emit their own immutable records, and no context
flag may disable that control.

## 9. Settlement-State Enumeration

The complete 7-value enumeration with the exact condition for each, and the proof that two of the seven
are never assigned by the computation, is in `L2_AUDIT_QUARANTINE/T2_PAYMENT_RECONCILIATION_EVIDENCE.md`
§8. Two structural points belong here:

- **`FACT VERIFIED`** — the reconciliation set feeding settlement state is filtered to **receivable and
  payable account types only**. Matching on any other account type is **invisible** to settlement state.
- **`FACT VERIFIED`** — the zero test uses company currency on a mixed-currency invoice, which is a
  **different test** from the one the settled flag performs. The two can disagree.

## 10. Answers To The Directive's Explicit Questions

| Question | Answer | Tag |
|---|---|---|
| **How does payment differ from reconciliation?** | Payment moves money into a clearing position and relieves the receivable control account. Reconciliation asserts *which debt* that money settles, and is the step that changes the residual. They are separate events with separate records — **except in the configuration where a payment produces no entry at all**. | `FACT VERIFIED` |
| **When is FX recognised?** | At reconciliation, on a date that is neither the invoice date nor the settlement date. | `FACT VERIFIED` |
| **Where does an overpayment live?** | As an unapplied credit inside the receivable control account, invisible to the invoice's settlement state. | `FACT VERIFIED` |
| **Is a customer deposit a liability?** | **Only if configured.** Otherwise it is revenue. | `FACT VERIFIED` |
| **Is there a bad-debt mechanism?** | Not found in the searched scope. Impairment is a generic write-off to an unconstrained account. | `NOT FOUND IN SEARCHED SCOPE` |
| **Does a locked period protect settlement history?** | **No.** Matching rows can be created and destroyed across a closed period. | `FACT VERIFIED` |
