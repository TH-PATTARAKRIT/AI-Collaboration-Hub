# P07 — STATUTORY SOURCE REGISTER

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Process: `P07 — Thailand Tax-to-Compliance`
Branch: `research/account-p07-th-tax-compliance-2026-09-04-001`
Baseline: `origin/SMEsPlus @ 88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad`
Classification: `LAYER 2 — AUDIT QUARANTINE` (see §6)
Date: `2026-09-04`

## 1. Register Purpose and Evidence Rule

This register is the **only** admissible basis in this package for a statement of Thai
law. The Common Execution Constitution requires the separation of:

| Band | Meaning | May ground a legal claim |
|---|---|---|
| `LAW` | Revenue Code section text | YES |
| `REGULATION` | Royal Decree / Ministerial Regulation | YES |
| `RD-REQ` | Revenue Department requirement (DG Notification, DG Order, RD form, RD guidance page) | YES |
| `STD` | Accounting standard (TAS/TFRS) | YES, for accounting only |
| `PRACTICE` | Common market practice | NO |
| `REF-ERP` | Reference ERP behaviour | NO |
| `SMEPLUS` | SMEsPlus design policy | NO |

**Directive compliance:** no row in this register was derived from reference ERP
configuration. Where a needed legal point could not be retrieved from an
authoritative source in this session it is recorded as
`HOLD — STATUTORY EVIDENCE REQUIRED` in §4 and is **not** used anywhere in this
package to support a conclusion.

## 2. Retrieved Statutory Sources (LAW / REGULATION / RD-REQ)

Retrieval method: direct fetch of the Revenue Department English publication of the
Revenue Code at `www.rd.go.th/english/*` on 2026-09-04. Each row records the section,
the operative rule as published, and the page from which it was read.

| ID | Band | Instrument | Operative rule as published | Source page |
|---|---|---|---|---|
| `S-01` | LAW | Revenue Code s.78 | VAT liability on **sale of goods** arises at the time of **delivery**, except that where transfer of ownership, receipt of payment, or issuance of a tax invoice occurs earlier, liability arises at that earlier event. | rd.go.th/english/37719.html |
| `S-02` | LAW | Revenue Code s.78/1 | VAT liability on **provision of services** arises at the time of **receipt of payment**, unless a tax invoice is issued, or the service is used, earlier. | rd.go.th/english/37719.html |
| `S-03` | LAW | Revenue Code s.78/2 | VAT liability on **importation** arises at the time of payment of import duty (or on entry at Customs where duty-exempt). | rd.go.th/english/37719.html |
| `S-04` | LAW | Revenue Code s.78/3 | Special tax-point rules are set by Ministerial Regulation for incorporeal goods, vending machines, credit-card sales and certain contracts. | rd.go.th/english/37719.html |
| `S-05` | LAW | Revenue Code s.79 | Tax base = total value received or receivable, including excise, excluding the output tax itself. | rd.go.th/english/37719.html |
| `S-06` | LAW | Revenue Code s.80 | The VAT rate is **10.00%** for sale of goods, provision of services and importation; "the rate under paragraph 1 may be reduced by Royal Decree but the rate for each sale of goods, provision of services or importation shall be the same rate." | rd.go.th/english/37732.html |
| `S-07` | LAW | Revenue Code s.80/1 | **Zero rate** applies to enumerated businesses, incl. export of goods not exempt under s.81(3) and services performed in Thailand and used abroad. | rd.go.th/english/37732.html |
| `S-08` | LAW | Revenue Code s.80/2 | 2.5% rate applies in calculating VAT under s.82/16 (small-operator regime). | rd.go.th/english/37732.html |
| `S-09` | LAW | Revenue Code s.82/3 | Tax payable = output tax **less** input tax **of each tax month**. | rd.go.th/english/37732.html |
| `S-10` | LAW | Revenue Code s.82/4 | A VAT registrant shall charge VAT from the purchaser **at the time tax liability takes place**. | rd.go.th/english/37732.html |
| `S-11` | LAW | Revenue Code s.82/5 | Six categories of input tax are **not deductible**, incl. absence of a tax invoice and a tax invoice with incomplete particulars. | rd.go.th/english/37732.html |
| `S-12` | LAW | Revenue Code s.82/6 | A registrant carrying on both VAT and non-VAT business shall **allocate** input tax. | rd.go.th/english/37732.html |
| `S-13` | LAW | Revenue Code s.82/9 | On a **debit note**, the issuer includes the increased output tax in the VAT calculation **in the tax month in which the debit note is issued**; the recipient treats it as input tax **in the tax month in which it is received**. | rd.go.th/english/37732.html |
| `S-14` | LAW | Revenue Code s.82/10 | On a **credit note**, the issuer deducts the decreased output tax **in the tax month in which the credit note is issued**; the recipient deducts from input tax **in the tax month in which it is received**. | rd.go.th/english/37732.html |
| `S-15` | LAW | Revenue Code s.83 | Monthly return on the basis of the **tax month**, filed with payment **within the 15th day of the following month**; filed at the local Amphur office where the place of business is located; where there are several places of business, **filing and payment shall be made separately by each place of business** unless the Director-General approves consolidated filing. | rd.go.th/english/37735.html |
| `S-16` | LAW | Revenue Code s.83/1 | Royal Decree may permit periodic filing, each period not exceeding 3 months. | rd.go.th/english/37735.html |
| `S-17` | LAW | Revenue Code s.83/6 | The payer must remit VAT for services of a foreign provider and for unregistered temporary operators in Thailand (self-assessed VAT). | rd.go.th/english/37735.html |
| `S-18` | LAW | Revenue Code s.84 | Excess tax credit of a tax month may be carried forward per Royal Decree, or refund claimed at the time of return filing. | rd.go.th/english/37735.html |
| `S-19` | LAW | Revenue Code s.86 | "VAT registrant shall **immediately** issue tax invoice and its copy for every sale of goods or provision of service **at the time the tax liability taking place**." | rd.go.th/english/37741.html |
| `S-20` | LAW | Revenue Code s.86/4 | Mandatory tax-invoice particulars: the word "tax invoice" in a prominent place; issuer name, address and taxpayer identification number; purchaser particulars; **serial number of the tax invoice (and of the book, if any)**; description, type, category, quantity and value; **VAT amount clearly separated** from value; **date of issuance**; and other particulars prescribed by the Director-General. | rd.go.th/english/37741.html |
| `S-21` | LAW | Revenue Code s.86/5 | The Director-General may prescribe alternative particulars for specified goods and categories. | rd.go.th/english/37741.html |
| `S-22` | LAW | Revenue Code s.86/6 | **Abbreviated tax invoice** permitted for retail business; price shown is inclusive of VAT; simplified particulars. | rd.go.th/english/37741.html |
| `S-23` | LAW | Revenue Code s.86/9 | **Debit note**: issue in the same tax month as the causing event, or the following month in case of necessity; must **reference the original tax invoice number**, show the difference in value, and state the tax on the difference. | rd.go.th/english/37741.html |
| `S-24` | LAW | Revenue Code s.86/10 | **Credit note**: same timing rule; must reference the original tax invoice, show the difference in value, and state the amount of VAT being credited. | rd.go.th/english/37741.html |
| `S-25` | LAW | Revenue Code s.87 | A VAT registrant shall make (1) an **output tax report**, (2) an **input tax report**, (3) a goods and raw material report; entries are required **within 3 working days** from the date of acquisition or disposition of the goods or service. | rd.go.th/english/37747.html |
| `S-26` | LAW | Revenue Code s.87/3 | Tax invoices, reports and copies shall be kept at the place of business for **at least 5 years** from the date of return filing or report making. | rd.go.th/english/37747.html |
| `S-27` | LAW | Revenue Code s.89 | Fines: **twice the tax** shown for failure to issue a tax invoice (item 5); **twice the tax** computed on the unreported or incorrectly reported base for report failures (item 10). | rd.go.th/english/37747.html |
| `S-28` | LAW | Revenue Code s.3 Tredecim | The Director-General is empowered to order a payer of assessable income under s.40, who is not otherwise obliged to withhold under Title 2, to **withhold tax at source** under Ministerial Regulation. | rd.go.th/english/37695.html |
| `S-29` | LAW | Revenue Code s.3 Quattuordecim | Where withholding is required by the Revenue Code, the person required shall withhold at source and remit to the Revenue Department. | rd.go.th/english/37695.html |
| `S-30` | LAW | Revenue Code s.50 | A person, partnership, company, association or body of persons paying assessable income under s.40 shall withhold income tax **at every time of payment**. | rd.go.th/english/37749.html |
| `S-31` | LAW | Revenue Code s.50 bis | The withholder shall issue a **withholding tax certificate in duplicate, each copy having the same contents**. For s.50(1) employment income: by 15 February of the following year, or within one month of termination. For the other cases (incl. s.3 Tredecim): **immediately every time tax is withheld**. | rd.go.th/english/37749.html |
| `S-32` | LAW | Revenue Code s.52 | The withholder shall remit at the Amphur office **within 7 days from the date of payment**; for registered transfers of immovable property, at the time of registration. | rd.go.th/english/37749.html |
| `S-33` | LAW | Revenue Code s.59 | The withholder shall **file a return indicating the tax withheld of each individual person** deriving assessable income. | rd.go.th/english/37749.html |
| `S-34` | RD-REQ | RD guidance, "Value Added Tax" | "VAT taxable period is a calendar month. VAT return therefore must be filed on a monthly basis" within 15 days of the following month; excess input tax refundable in cash or as tax credit; refund claim within 3 years from the last day of the filing date; **each place of business must file and pay separately unless the Director-General approves otherwise**. | rd.go.th/english/6043.html |
| `S-35` | REGULATION | Royal Decrees reducing the s.80 rate | The 10% statutory rate has been reduced to **7%** by successive Royal Decrees since 1992. The reduction in force at the date of this package runs to **30 September 2026**; the Thai Cabinet approved a further one-year extension on **27 July 2026** and the Revenue Department issued a confirming notice on **2 August 2026**, extending 7% from **1 October 2026 to 30 September 2027**. | Secondary reporting of Cabinet/RD action — see `U-04` |

## 3. Derived Statutory Positions Used in This Package

These are the only inferences drawn from §2, and each is traceable to its sources.

| ID | Position | From |
|---|---|---|
| `P-01` | The Thai **VAT tax point is event-based and, for services, payment-based**; it is *not* definitionally the accounting date of a ledger entry. | `S-01` `S-02` `S-03` |
| `P-02` | The period in which a supply belongs for VAT purposes is the **tax month of the tax point** (s.82/3 computes per tax month; s.83 files per tax month). | `S-09` `S-15` |
| `P-03` | A credit or debit note belongs to the tax month in which it is **issued** (issuer) or **received** (recipient) — not to the tax month of the original invoice. | `S-13` `S-14` `S-23` `S-24` |
| `P-04` | The statutory **Output Tax Report** and **Input Tax Report** are mandatory books of record in their own right, distinct from the VAT return. | `S-25` |
| `P-05` | A tax invoice must carry its **own serial number** and the word "tax invoice", and must be issued at the tax point. | `S-19` `S-20` |
| `P-06` | The **abbreviated tax invoice** is a distinct statutory document class with VAT-inclusive pricing and reduced particulars. | `S-22` |
| `P-07` | The **WHT tax point is the moment of payment**, and remittance is due within 7 days; the certificate is due **immediately on each withholding** (non-employment income). | `S-30` `S-31` `S-32` |
| `P-08` | WHT reporting is **per payee per payment**, not per invoice. | `S-33` |
| `P-09` | The 7% rate is a **Royal-Decree reduction of a 10% statutory rate with a fixed expiry date, renewed annually**. A system that hard-binds behaviour to the literal "7%" is bound to a temporary instrument. | `S-06` `S-35` |
| `P-10` | VAT filing is **per place of business (branch)** by default; consolidated filing is an exception requiring DG approval. Branch identity is therefore a filing-unit attribute, not decoration. | `S-15` `S-34` |

## 4. HOLD — STATUTORY EVIDENCE REQUIRED

Not used to support any conclusion in this package.

| ID | Question | Why it matters to P07 | Status |
|---|---|---|---|
| `U-03` | The precise instrument and conditions permitting **input tax to be claimed in a later tax month** than the tax invoice date (commonly stated as the following 6 tax months), and its interaction with s.82/5(2). | This is the principal business justification for a *tax period date distinct from the accounting date* on the purchase side. Without it, the design intent of that field cannot be legally grounded. | `HOLD — STATUTORY EVIDENCE REQUIRED`. Secondary sources assert a six-month window and a three-year refund limit; no Director-General Notification text was retrieved. |
| `U-04` | The **Royal Decree number** currently granting the 7% rate and the decree implementing the 1 Oct 2026 – 30 Sep 2027 extension. | Fixes the exact expiry against which the rate-literal dependency (`P07-F-01`) must be scheduled. | `HOLD — STATUTORY EVIDENCE REQUIRED`. Cabinet date (27 Jul 2026) and RD notice date (2 Aug 2026) obtained from secondary reporting only. |
| `U-07` | The Director-General requirements governing the **prescribed format and column set** of the s.87 output/input tax reports. | Determines whether the reports produced by the system are format-compliant, not merely arithmetically complete. | `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| `U-08` | The statutory basis and required particulars of the **substitute tax invoice** (ใบแทนใบกำกับภาษี) and of copy/original marking. | Determines whether the absence of these document classes is a gap or a non-requirement. | `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| `U-09` | The prescribed **condition-of-withholding codes** (withheld at source / borne by payer permanently / borne by payer once) and their required use on PND schedules and on the s.50 bis certificate. | `P07-F-14` observes a hard-coded condition value; the statutory code set must be confirmed before the gap is sized. | `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| `U-10` | The authoritative mapping of **s.40 income categories to PND form and to withholding rate**, including the rates outside {1%, 2%, 3%, 5%}. | `P07-F-13` finds income type derived from rate; the correct mapping is needed to specify the replacement. | `HOLD — STATUTORY EVIDENCE REQUIRED`. |

## 5. Rejected Source

| Claim encountered | Where | Disposition |
|---|---|---|
| "PND53 withholding tax returns form is used for **service** invoices, while PND3 is used for **rental** invoices where the payee is a juristic person." | Commercial blog surfaced during retrieval | **REJECTED.** Contradicts `S-30`/`S-33` and the RD form set: the PND3 / PND53 split is by **payee legal personality** (natural person vs juristic person), not by income description. Recorded to demonstrate that `PRACTICE`-band material was encountered and excluded, not silently absorbed. |

## 6. Classification and Clean-Room Note

This register is `LAYER 2 — AUDIT QUARANTINE`. It contains statutory citations (which are
public and Layer-1 safe) and is referenced by Layer-2 evidence files that carry reference
ERP identifiers. The Layer-1 clean-room transfer of P07 is
`19_P07_CORE_RECON_HANDOFF_PACK.md`, which restates the requirements in neutral
vocabulary with no vendor model, field, path or menu name.
