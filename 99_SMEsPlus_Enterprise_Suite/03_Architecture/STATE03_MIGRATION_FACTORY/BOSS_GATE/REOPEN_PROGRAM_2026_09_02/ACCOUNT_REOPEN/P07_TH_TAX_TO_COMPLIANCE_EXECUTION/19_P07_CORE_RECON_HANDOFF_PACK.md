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
| `POS-7` | The filing unit is the **place of business**, and the branch attribute of the filing entity is distinct from the branch attribute of a counterparty. | The return is filed per place of business unless a consolidation approval exists. Today three different branch attributes are used interchangeably and the filing entity's own attribute is read by nothing. |
| `POS-8` | Exactly one mechanism records a withholding, and exactly one implementation produces each statutory register. | Two withholding mechanisms and two register implementations currently coexist with no rule of precedence; the two register implementations can return different totals for the same month. |
| `POS-9` | A filed figure is fixed by a filing record, and any later change that would alter it is visible as an adjustment. | Four ordinary, non-privileged master-data or payment actions currently change the content of an already-filed statutory report without touching the ledger and without leaving a trace. |

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
can be made to that account and can never be filed from the system.

The same shape, less severely, applies to withholding on employment income and to one
further certificate variant.

## 5. Two Capabilities Unprovisioned on Frameworks That Exist

Both were established by comparing Thailand against the full population of country
localisations present in the same source set, not by inspecting Thailand alone.

| Capability | Framework present in the platform | Thai provisioning | Peer baseline |
|---|---|---|---|
| Filing records with statutory deadlines, filing states and compliance checks | yes, fully featured | one generically-named return, no deadline, no workflow; the two principal withholding returns are not registered at all | 118 country localisations provision it |
| Tax mapping (fiscal position) — export customers, non-registered vendors, exempt or promoted entities, overseas payees | yes | none whatsoever | 113 of 138 country chart sets provision it |

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

These are held open. No position in §2 depends on them, but three design decisions do.

1. The instrument and conditions under which input tax may be claimed in a later tax month
   than the tax invoice date. This is the legal basis for a purchase-side tax point that
   differs from the document date.
2. The prescribed format and column set of the two statutory tax registers.
3. The statutory code set for the condition of withholding, and the authoritative mapping
   from income category to withholding form and rate.
4. The requirements governing a substitute tax invoice and original/copy marking.

## 8. Standing Structural Risk

The reduced rate of value added tax currently in force is a **temporary reduction of the
statutory rate, granted by decree and renewed annually with a fixed expiry**. The reduction
in force at the date of this pack has been extended by one year and is not about to lapse.

The risk is structural, not calendar-driven: one statutory register admits a transaction
only if a rate-bearing label matches a fixed literal. A future reversion to the statutory
rate, or a rename of that label, empties the register with no error and no warning. Any
design that encodes the current rate into a selection rule inherits an annual expiry.

## 9. Terminal State

**READY FOR CORE ACCOUNTING RECONCILIATION.**

This states that P07 has produced the tax positions, the data contract and the open legal
questions the core accounting reconciliation needs in order to proceed. It is **not** a
gate outcome, not a pass, not a design authorisation, and not permission to implement. The
research gate assessment is `RECOMMEND HOLD` and is recorded in the Layer-2 package; the
Boss is the sole final approver.
