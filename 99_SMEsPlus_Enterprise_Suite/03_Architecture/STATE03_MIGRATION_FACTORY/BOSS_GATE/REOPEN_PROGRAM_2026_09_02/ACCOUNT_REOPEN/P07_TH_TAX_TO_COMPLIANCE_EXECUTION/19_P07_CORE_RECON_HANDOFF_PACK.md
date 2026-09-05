# P07 — CORE ACCOUNTING RECONCILIATION HANDOFF PACK

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Process: `P07 — Thailand Tax-to-Compliance`
Classification: **`LAYER 1 — CLEAN ROOM`**
Date: `2026-09-04`

## 0. Clean-Room Status of This File

This is the **only** file in the P07 package cleared for downstream reference use. It
carries no vendor model, field, path, module or menu name, and no source citation. Every
statement here is a business, legal or accounting statement. The Layer-2 evidence, with
its citations, stays in files `01`–`18` and `20` and is Boss / PMO / AI-Audit only.

Thai terminology is used only where the statute names a thing; those names are legal terms,
not vendor tokens.

## 1. What P07 Establishes

Thailand's tax rules place a transaction in a tax period by the moment the **tax liability
arises** — the tax point. For goods this is delivery, or earlier if ownership transfers,
payment is received, or a tax invoice is issued. For services it is receipt of payment,
unless a tax invoice is issued or the service is used first. For withholding tax it is the
**moment of payment**, with remittance due within seven days and a certificate due
immediately on each withholding.

The system as researched places a transaction in a tax period by its **accounting date**.

Everything else in this pack follows from that single inversion. It is not a defect in one
report; it is a question of which process owns the tax period.

## 2. The Nine Positions the Reconciliation Must Take

| # | Position required | Why it cannot be deferred |
|---|---|---|
| `POS-1` | The tax period of a transaction is determined by its tax point, and the tax point is a first-class attribute of the tax fact — not the accounting date, and not a free-text date beside it. | The monthly VAT return, the net input/output computation, and both statutory tax registers are all defined per tax month. |
| `POS-2` | The tax point is derived per transaction class — goods, services, import, credit note, debit note, withholding — not entered once on a document header. | The statutory rule differs by class, and one header date cannot express six rules. |
| `POS-3` | Withholding tax is anchored to the payment: the fact reported, the amount reported, and the period reported must all come from the payment on which tax was actually withheld. | Today the withholding is reported from the source bill, on the bill's date, at an amount recomputed from a rate rather than read from the ledger. |
| `POS-4` | A partial payment withholds on the amount paid. | Today a first partial payment causes the whole document's withholding to be reported. |
| `POS-5` | The payee's legal personality (natural person or juristic person) is a typed master-data attribute, and the withholding form and income category are typed attributes of the withholding definition. | Today the form is inferred from a contact-structure flag and from a substring of a translatable label; the income category is inferred from the tax rate. |
| `POS-6` | The tax invoice is a document object with its own identity, its own number, an issuance moment, a copy, and immutability once issued — and credit and debit notes reference the tax invoice they adjust. | Without a document object, the statutory reference requirement on adjustments cannot be met at all, and no issuance can be evidenced. |
| `POS-7` | The filing unit is the **place of business**, and the branch attribute of the filing entity is distinct from the branch attribute of a counterparty. | The return is filed per place of business unless a consolidation approval exists. Today three different branch attributes are used interchangeably, and no statutory report examined in this research reads the filing entity's own attribute. |
| `POS-8` | Exactly one mechanism records a withholding, and exactly one implementation produces each statutory register. | Two withholding mechanisms and two register implementations coexist. No rule of precedence was found in the material examined. Where both withholding mechanisms are active on one payment, the platform silently discards one of the two entries **after** the payment amount has already been reduced by the other. The two register implementations can return different totals for the same month. |
| `POS-9` | A filed figure is fixed by a filing record, and any later change that would alter it is visible as an adjustment. | At least seven ordinary, non-privileged master-data or payment actions change the content of an already-filed statutory report without touching the ledger. Two of them rewrite monetary amounts and statutory classifications. The reported figure is a render-time computation over live master data, so no filed figure is reproducible. |

## 3. What Reaches No Statutory Report Today

Three tax-bearing outcomes are recorded in the ledger and appear in no Thai statutory
report produced by the researched system:

1. **Withholding suffered on our own sales** — tax our customers withhold when paying us.
   It is posted to a receivable-side tax-credit account and carries no reporting
   classification at all.
2. **Zero-rated and exempt portions of a mixed-rate invoice** — excluded from the main
   register by one rule and from the zero-rate register by another.
3. **Supplies with no counterparty record**, which is precisely the abbreviated
   (retail) tax invoice case the statute provides for.

A fourth outcome is reported, but from the wrong document on the wrong date: withholding
recorded at payment is reported through the originating bill.

## 4. Obligations Named But Not Servable

The chart of accounts provisions an account for withholding on payments abroad, and names
the remittance form in its description, in both languages. No tax definition, no
classification, no report, no certificate type and no filing entry exists for it. A posting
can be made to that account, and no means of filing it was found anywhere in the material
examined.

The same shape, less severely, applies to withholding on employment income and to one
further certificate variant.

## 5. Two Capabilities Unprovisioned on Frameworks That Exist

Both were established by comparing Thailand against the full population of country
localisations present in the same source set, not by inspecting Thailand alone.

| Capability | Framework present in the platform | Thai provisioning | Peer baseline |
|---|---|---|---|
| Filing records with statutory deadlines, filing states and compliance checks | yes, fully featured | one generically-named return, no deadline, no workflow; the two principal withholding returns are not registered at all | 118 country localisations provision it |
| Tax mapping (fiscal position) — export customers, non-registered vendors, exempt or promoted entities, overseas payees | yes | none provisioned, and the mapping filter is switched off on all four statutory registers | 94 of the 126 country chart sets that define a chart provision it |

The overseas-payee case is the same obligation as §4: the mapping that would route it does
not exist either.

## 6. Minimum Data Contract P07 Requires From the Other Processes

| From | Element |
|---|---|
| Purchase | Tax point per line, typed by transaction class; vendor legal personality as a typed attribute |
| Sales | Tax point per line; delivery and ownership-transfer moments; tax-invoice document identity |
| Expense | Input-tax deductibility classification at the expense line |
| Payment | Payment date as the withholding anchor; allocation per document; reversal linkage; one currency-conversion policy |
| General Ledger and Close | Acceptance that a tax fact and its accounting entry may fall in different periods; a tax-period state distinct from the accounting close; confirmation of the month-end tax settlement mechanism |
| Deferred Recognition | An explicit rule that deferral affects recognition timing only and never tax-period membership |
| Cross-process reconciliation | A ruling on whether a tax-reporting grouping may span companies, and within what security boundary |

## 7. Legal Questions That Must Be Answered Before Design

These are held open. No position in §2 depends on them, but four design decisions do.

1. The instrument and conditions under which input tax may be claimed in a later tax month
   than the tax invoice date. This is the legal basis for a purchase-side tax point that
   differs from the document date.
2. The prescribed format and column set of the two statutory tax registers.
3. The statutory code set for the condition of withholding, and the authoritative mapping
   from income category to withholding form and rate.
4. The requirements governing a substitute tax invoice and original/copy marking.

## 8. Standing Structural Risk

Two statutory registers admit a transaction only when a rate-bearing descriptive label
matches a fixed stored value exactly. Three separate events make that match fail, and in
every one of them the register returns **no data at all**, silently, with no error and no
warning:

1. **Loading the Thai chart of accounts while the Thai language is already active.** The
   label is a translatable text, and when the chart is loaded into a system where Thai is
   already switched on, the label is stored in both languages in a way the comparison does
   not tolerate.

   **Corrected against the deployed databases.** An earlier issue of this pack said the
   trigger was *presenting the system in Thai*. That is **wrong**: Thai is switched on in
   four of the five systems examined and only **one** of them carries the two-language
   label — including a system with several thousand records set to Thai. Switching the
   language on afterwards does not change labels already stored. What separates the one
   affected system from the others is the **order** in which the language and the chart of
   accounts were set up, which is not visible in the system afterwards. This is the immediate trigger, not a remote one,
   and it is the most serious finding of this research. **Measured prevalence: the failing
   stored value is present in 1 of the 4 same-generation deployed databases examined
   (15 database snapshots, 7 distinct databases, 4 of the current generation).** The other
   three function correctly.

   **And the exposure is prospective, not realised — with a measured size.** The one affected
   system carries **two or three** taxed lines, so nothing of consequence has yet been lost
   there. The two systems holding real volume — **5,202** and **32,672** taxed lines — are
   the ones **not** affected. So the defect currently fires only where there is nothing to
   lose, and every system with something to lose is one set-up ordering away from it. That is
   the reason it is ranked where it is. That distribution is the reason the finding is ranked where it
   is rather than the reason to discount it: a fault that is silent in three systems out of
   four cannot be found by exercising a system that works, and the three working systems are
   the ones not yet presented in Thai.
2. **Renaming the label**, which is an ordinary configuration action available to a normal
   accounting user.
3. **A change in the rate of value added tax.** The reduced rate currently in force is a
   temporary reduction of the statutory rate, granted by decree and renewed annually with a
   fixed expiry. The reduction in force at the date of this pack has been extended by one
   year and is not about to lapse — but any design that encodes the current rate into a
   selection rule inherits that annual expiry.

The design consequence is the same for all three: **statutory inclusion must be decided by
what a transaction is, never by what a label says.** A related defect follows the same
pattern — the zero-rated and exempt tax definitions carry no group of their own, so they
adopt the first one available, which is a withholding group rather than a value-added-tax one.

   **Corrected against the deployed databases.** The consequence is **not** a wrong posting.
   A tax whose rate is zero produces no tax line, and a group's control account is reached
   only through one, so nothing has ever posted to the withholding accounts by this route:
   **zero such lines in both deployments carrying real transaction volume**, measured against
   controls of 5,202 and 33,114 genuine tax lines. The live consequence is in **reporting**:
   in the larger of those deployments **15,973 posted lines carry one of these taxes**, and
   because the group is not a value-added-tax group, any statutory register that selects by
   group cannot see them as taxable supplies. The misposting risk remains **conditional** on
   any of these rates ceasing to be zero.

## 9. Terminal State

**READY FOR CORE ACCOUNTING RECONCILIATION.**

This states that P07 has produced the tax positions, the data contract and the open legal
questions the core accounting reconciliation needs in order to proceed. It is **not** a
gate outcome, not a pass, not a design authorisation, and not permission to implement. The
research gate assessment is `RECOMMEND HOLD` and is recorded in the Layer-2 package; the
Boss is the sole final approver.
