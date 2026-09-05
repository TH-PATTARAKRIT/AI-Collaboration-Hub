# P07 — TAX DOCUMENT MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Statutory Document Classes and Their Realisation

A statutory tax document is an object with an identity, an issuance moment, required
particulars, a retention obligation and a controlled lifecycle. The matrix asks, for each
class, whether such an object exists in the declared source set.

| # | Statutory document | Source | Object exists | Own number | Issuance event | Required particulars enforced | Lifecycle controlled | Realisation |
|---|---|---|---|---|---|---|---|---|
| `D-01` | Tax invoice (ใบกำกับภาษี) | `S-19` `S-20` | **no** | no | no | no | no | Print-time substitution of the invoice title with the literal `Tax Invoice`, selected when the company's fiscal country is TH (`l10n_th/views/report_invoice.xml:14-16`; `l10n_th/models/account_move.py:7-11`) |
| `D-02` | Abbreviated tax invoice (ใบกำกับภาษีอย่างย่อ) | `S-22` | **no** | no | no | no | no | Not selected by the declared patterns as a class. The vendor tax report anticipates the partnerless case with the caption `Selling goods or providing services` (`l10n_th_reports/models/tax_report_vat.py:153-154`); the SMEsPlus reports remove that path (`P07-F-04`) |
| `D-03` | Debit note (ใบเพิ่มหนี้) | `S-23` `S-13` | **no** | no | no | no | no | Not selected by the declared patterns in the Thai modules |
| `D-04` | Credit note (ใบลดหนี้) | `S-24` `S-14` | partial | no | no | no | accounting reversal only | Base-application reversal document; no Thai note class, no original-tax-invoice reference in any Thai report |
| `D-05` | Substitute tax invoice (ใบแทนใบกำกับภาษี) | held at `P07-U-08` | **no** | — | — | — | — | Not selected by the declared patterns |
| `D-06` | Withholding tax certificate (หนังสือรับรองการหักภาษี ณ ที่จ่าย) | `S-31` | **yes** | computed `name` | user-initiated wizard | partial | draft / done / cancel, with a cancel-and-replace reference | `l10n_th_withholding_tax_cert`; print form in `l10n_th_withholding_tax_cert_form` |
| `D-07` | Output tax report / Input tax report (รายงานภาษีขาย / ภาษีซื้อ) | `S-25` | as reports, not as records | n/a | n/a | column set not validated against `P07-U-07` | none | Two parallel implementations — see `07_P07_TAX_REPORT_TRACEABILITY.md` |
| `D-08` | VAT return (ภ.พ.30) | `S-15` | partial | n/a | n/a | structure present as report lines 1–12 | one `account.return.type` | `l10n_th/data/account_tax_report_data.xml`; `l10n_th_reports/data/account_return_data.xml:4-8` |
| `D-09` | PND 3 / PND 53 return | `S-33` | export only | n/a | n/a | 16 columns emitted, four defective (`W-K-01`, `W-K-02`, `W-K-05`, and the amount per `W-C-03`) | none | CSV export buttons on two report definitions |
| `D-10` | PND 1 / PND 3a / PND 54 return | `S-33` | **no** | — | — | — | — | See the provisioning matrix at `03 §4.1`: PND 54 has a general-ledger account and nothing else |

## 2. The Tax Invoice Is Not an Object

`D-01` is the most consequential row, so its evidence is set out in full.

The whole of the Thai tax-invoice implementation in the declared source set is:

1. `l10n_th/models/account_move.py:7-11` — when the company's fiscal country is `TH`,
   `_get_name_invoice_report` returns the Thai template instead of the base template.
2. `l10n_th/views/report_invoice.xml:14-16` — that template replaces the `invoice_title`
   node with the literal string `Tax Invoice`.
3. `l10n_th/views/report_invoice.xml:4-13` — it inserts the partner's derived branch label
   after the partner's tax identification number in three address blocks.
4. `l10n_th/views/report_invoice.xml:19-36` — a separate `Commercial Invoice` report, and
   `l10n_th/models/ir_actions_report.py:8-13`, which restricts that report to invoices.

What follows from this, each item checked against `S-19`/`S-20`:

| Statutory particular or property | Status |
|---|---|
| The word "tax invoice" in a prominent place | **present and correctly translated.** An earlier draft called this a hard-coded English literal; that was refuted during independent challenge — `l10n_th/i18n/th.po:126-127` maps `Tax Invoice` to `ใบกำกับภาษี` as a view term, and the template renders under the partner's language (`report_invoice.xml:22-23`). This statutory particular is **satisfied**. |
| Serial number of the tax invoice | **the accounting document name is used** — written directly into the column headed `Tax Invoice No.` (`l10n_th_reports/models/tax_report_vat.py:148` under the header at `:113`); no tax-invoice sequence and no book number was found (`P07-N-01`) |
| Date of issuance | the invoice date is printed; no record of the moment of issuance was found — class `B`, boundary: the 15 modules of `13 §5` read in full for document handling |
| VAT clearly separated | inherited from the base layout |
| Issuer and purchaser identification, including branch | printed, but from an inconsistently-sourced branch (`P07-F-06`) |
| Copy | `S-19` requires the invoice **and its copy**; no copy object or copy marking was selected |
| Issued immediately at the tax point | no issuance event was found — class `B`, same boundary as the row above — so compliance cannot be evidenced either way |
| Immutability once issued | the underlying accounting document governs; a re-print produces a new rendering with no version identity |

Because no such object was found within the boundary declared above, four downstream
requirements are structurally unavailable rather than merely unimplemented:
original-invoice reference on credit and debit notes (`S-23` `S-24`), the
abbreviated-invoice class (`S-22`), the substitute invoice (`P07-U-08`), and any per-document
retention or issuance audit trail (`S-26`).

### 2.1 The Substitution Covers One Title State of Thirteen

The Thai template replaces only the `invoice_title` node. In the base layout
(`account/views/report_invoice.xml:62-110`) that node fires solely for
`move_type == 'out_invoice'` **and** `state == 'posted'`. Its siblings —
`draft_invoice_title`, `cancelled_invoice_title`, `credit_note_title`,
`vendor_bill_title`, `proforma_invoice_title` and the remaining variants — are untouched.
A draft, cancelled, pro-forma, credit-note or vendor-bill rendering under a Thai company
therefore prints the base wording. By comparison `l10n_zm_account/views/report_invoice.xml:9-24`
replaces six. `P07-F-46`.

### 2.2 This Is a Regression, Not a Greenfield Gap

`P07-N-03` records that four Thai tax-document modules exist in the v14 tree and not in the
declared set. Connecting that to `D-01` changes what the finding means. In the excluded v14
tree, `l10n_th_tax_invoice/models/account_move.py:14` declares a first-class model
`account.move.tax.invoice` carrying `tax_invoice_number` (`:18`), `tax_invoice_date`
(`:19`), `period_date` (`:17`), `report_late_mo` (`:20`) and `reversing_id` / `reversed_id`
(`:74`, `:77`); and `l10n_th_tax_invoice/models/account.py:9-15` adds a
`taxinv_sequence_id` to the journal.

**Every capability this matrix finds structurally absent — document object, own number, own
sequence, own document date, own tax period, cancel-by-reference — existed as a first-class
model in the prior generation of this product line.** `D-01`, `A-04` and `A-13` are
therefore a **regression**, and their remediation is a restoration rather than a design
from nothing. `P07-F-47`. Boundary: the v14 tree enumerated at `13 §2.1`; whether the
capability was deliberately dropped, superseded, or lost in migration is `P07-U-18`.

## 3. The Withholding Certificate Is an Object — Assessed on Its Merits

`D-06` is the only statutory document in the declared set that is modelled as a record.
It is therefore assessed against `S-31` rather than dismissed.

| Property | Evidence | Assessment |
|---|---|---|
| Identity | `name` computed and stored, tracked (`withholding_tax_cert.py:77-82`) | present |
| Date | `date` computed and stored; separate `payment_date`, required, indexed (`:83-89`, `:114-119`) | present, and the **payment date is carried explicitly** — the correct statutory anchor under `S-30` |
| Issuer / payee | `company_partner_id`, `supplier_partner_id`, with related tax identifiers (`:131-172`) | present |
| Income type | **15**-value s.40 selection covering 40(1)–40(4)(b) sub-classes and 3 เตรส (`:16-64`), counted entry by entry | **the most statutorily faithful classification in the declared set** |
| Form type | `income_tax_form` over `pnd1`/`pnd3`/`pnd3a`/`pnd53` (`:9-14`, `:173-180`) | narrower than the chart provisions (`03 §4.1`) |
| Tax payer condition | `tax_payer` over `withholding` / `paid_one_time` (`:66`, `:188-195`) | two values; the statutory code set is held at `P07-U-09`, and the PND export ignores this field entirely (`W-K-02`) |
| Lifecycle | `draft` / `done` / `cancel`, with `ref_wt_cert_id` linking a replacement to the cancelled certificate (`:90-102`) | present, and cancellation is by reference rather than by deletion — the correct pattern |
| Duplicate copies | `S-31` requires issuance **in duplicate, each copy having the same contents** | **not modelled**; recorded as `P07-U-13` |
| Issuance timing | `S-31` requires issuance **immediately every time tax is withheld** | issuance is a user-initiated wizard, not an event consequence of the withholding |
| Company scope | `company_id` required with a record rule; line company related from the header (`:148-155`, `:403-405`) | correct scope (see `20 §5` row 13) |
| Deletion | full unlink granted to the billing group | **inconsistent with a 5-year retention obligation** (`S-26`, `P07-F-19`) |

The certificate contradicts the rest of the P07 surface in an instructive way: it holds
the correct income-type taxonomy, the correct date anchor and the correct cancellation
pattern, and **the statutory export does not read any of them**. The knowledge required to
file correctly is present in the system and is bypassed by the reporting layer.

## 4. Document-to-Event Binding

| Document | Bound to which event | Binding evidence | Gap |
|---|---|---|---|
| Tax invoice | none (rendering of a document) | — | no issuance event found — class `B`, boundary as `05 §2` |
| Credit note | accounting reversal | base application | not bound to a tax-note date or the original tax invoice |
| WHT certificate | payment and/or move, via `payment_id` / `move_id` with `ondelete="restrict"` (`withholding_tax_cert.py:103-130`) | present and protective | creation is manual, so a withholding can exist with no certificate |
| PND export | tag membership over a date range | both handlers | binds to the invoice, not to the withholding (`W-C-01`) |
| VAT report | tag membership over a date range | all four handlers | binds to the accounting date, not the tax point (`P07-F-02`) |

## 5. Negative Claims Made in This File

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-01` | No tax-invoice numbering sequence distinct from the accounting document sequence was found. | `A — VERIFIED ABSENCE WITHIN SCOPE` | PATH SET of `13 §2`; patterns `sequence`, `ir.sequence`, `tax_invoice` over the 15 modules of `13 §5`; plus full reading of `l10n_th` |
| `P07-N-14` | No abbreviated tax invoice, debit note or substitute tax invoice **class** was found in the Thai modules. | `B — NOT FOUND IN SEARCHED SCOPE` | Thai module population only; the base application's own document typology was not re-enumerated |
| `P07-N-03` | `l10n_th_tax_invoice`, `l10n_th_tax_report`, `l10n_th_expense_tax_invoice` and `l10n_th_expense_withholding_tax` are absent from the declared source set. | `A — VERIFIED ABSENCE WITHIN SCOPE`, and `E — CONTRADICTED` at volume scope: all four exist in the v14 and v12 trees enumerated in `13 §2.1`. | directory-name search across the declared set and across the volume |

`P07-N-03` is retained precisely because it is contradicted at the wider scope: four Thai
tax-document modules existed in an earlier generation of this product line and are not
present in the generation the Account module declares as its source. Whether they were
superseded, replaced, or dropped is `P07-U-18`.
