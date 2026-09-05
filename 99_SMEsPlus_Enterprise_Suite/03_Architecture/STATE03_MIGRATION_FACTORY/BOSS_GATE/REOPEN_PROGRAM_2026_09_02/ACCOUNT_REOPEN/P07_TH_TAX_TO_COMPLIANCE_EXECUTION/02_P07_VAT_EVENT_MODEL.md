# P07 — VAT EVENT MODEL

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. The Canonical Chain Required by the Constitution

    Source Business Event
      -> Tax Trigger
      -> Tax Base
      -> Tax Calculation
      -> Tax Document
      -> Tax Accounting Event
      -> Journal
      -> Tax Report
      -> Filing / Adjustment / Close

with the invariant:

    ONE TAX FACT -> ONE CANONICAL TAX EVENT -> ONE ACCOUNTING EFFECT

This file traces that chain for VAT twice: as the statute requires it (§2), and as the
declared source set implements it (§3). §4 states where the two diverge and §5 states
where the invariant is broken.

## 2. Statutory VAT Event Chain

| Link | Statutory content | Source |
|---|---|---|
| Source business event | Sale of goods; provision of services; importation | `S-01` `S-02` `S-03` |
| Tax trigger (tax point) | **Goods**: delivery, or earlier of ownership transfer / payment / tax-invoice issuance. **Services**: receipt of payment, or earlier of tax-invoice issuance / use of service. **Import**: payment of import duty or Customs entry. Special classes by Ministerial Regulation. | `S-01` `S-02` `S-03` `S-04` |
| Tax base | Total value received or receivable, including excise, excluding output tax | `S-05` |
| Tax calculation | Rate per s.80 (10%, reduced to 7% by Royal Decree); zero rate per s.80/1; exempt per s.81 | `S-06` `S-07` `S-35` |
| Tax document | Tax invoice with own serial number, issued **immediately at the tax point**; abbreviated tax invoice for retail; debit note; credit note | `S-19` `S-20` `S-22` `S-23` `S-24` |
| Tax accounting event | Output tax charged to the purchaser at the tax point; input tax recorded on receipt of a compliant tax invoice | `S-10` `S-11` |
| Journal | Not prescribed by the Revenue Code; governed by accounting standard | — |
| Tax report | Output tax report and input tax report, entered within 3 working days | `S-25` |
| Filing / adjustment / close | Monthly return by the 15th of the following month, **per place of business**; net = output − input for the tax month; credit/debit notes adjust in the month issued or received; excess credit carried forward or refunded | `S-15` `S-09` `S-13` `S-14` `S-18` |

### 2A. Supplies Without Consideration — Absent From the First Issue of This File

This section was added after peer evidence from P04 caused this session to retrieve
s.77/1(8) and (9), which it had not read. **The first issue of this event model treated
every source business event as consideration-based** — a sale, a service or an import — and
was wrong to.

Verified at `rd.go.th/5205.html`: `ขาย` is `จำหน่าย จ่าย โอนสินค้าไม่ว่าจะมีประโยชน์หรือ
ค่าตอบแทนหรือไม่`, and `สินค้า` is tangible **and** intangible property not limited to goods
held for resale. So the following are supplies, and each is a link in the chain of §1 that
this package had no row for:

| Act | Limb | Output-tax event in the declared set |
|---|---|---|
| Donation or free transfer | the plain words of `S-36` | none found |
| Conditional sale, ownership not yet passed | (ก) | none found |
| Delivery to an agent for resale | (ข) | none found |
| Export | (ค) | zero-rated tax exists, but see `P07-F-05` for whether it reaches a register |
| Applying goods otherwise than to the direct conduct of the business | (ง), bounded by Director-General criteria — **held at `P07-U-23`** | none found |
| Goods short against the stock report | (จ) | none found |
| Goods remaining on cessation of business | (ฉ) | none found |

`P07-F-58` — the researched system recognises output tax only where a consideration-bearing
document exists. Five of the seven limbs above have no representation at all, and the
disposal path that would carry the first of them produces no tax document. The **extent** of
limb (ง) is held; the **existence** of the definitional gap is verified and is not held.

## 3. Implemented VAT Event Chain in the Declared Source Set

| Link | Implementation | Evidence |
|---|---|---|
| Source business event | Customer invoice / vendor bill / miscellaneous entry | base application |
| Tax trigger | **None.** The trigger is document posting; the period attribute is the move's accounting date. A tax-point-bearing field exists but does not drive selection. | `smesplus_tax_period_date/models/tax_period.py:23`, `:36`; `smesplus_account_reports/models/account_generic_tax_report.py:26` |
| Tax base | Repartition-engine base (`tdr.base_amount`) on the main reports; `account_move_line.balance` on the zero-rate reports; `price_subtotal` in the withholding path | `account_generic_tax_report.py:49`, `:250`, `:420` |
| Tax calculation | Base application tax engine, driven by `account.tax` template rows | `l10n_th/data/template/account.tax-th.csv` |
| Tax document | Print-time title substitution to the literal `Tax Invoice`; no document object, no number, no issuance event | `l10n_th/views/report_invoice.xml:14-16`; `l10n_th/models/account_move.py:7-11` |
| Tax accounting event | Tax line on the accounting move, tagged with the report tags carried by the tax's repartition lines | base application; tags from `account.tax-th.csv` |
| Journal | Output tax to the VAT payable account, input tax to the VAT receivable account, per template | `account.tax.group-th.csv` (`tax_payable_account_id`, `tax_receivable_account_id`) |
| Tax report | **Two parallel implementations** of the s.87 books — see §6 | `l10n_th_reports`, `l10n_th_reports_ext`, `smesplus_account_reports` |
| Filing / adjustment / close | One `account.return.type` record; no branch filing unit; credit notes netted by sign; no original-invoice reference | `l10n_th_reports/data/account_return_data.xml:4-8`; `account_generic_tax_report.py:87` |

## 4. Divergence Table

| # | Statutory link | Implemented as | Consequence |
|---|---|---|---|
| `V-D-01` | Tax point is an **event**, distinct from the accounting date | Accounting date | A supply whose tax point falls in month M but which is booked in month M−1 is reported in M−1. The system cannot represent the difference even though it stores a field for it. |
| `V-D-02` | Services: tax point is **receipt of payment** | Posting of the invoice | Service supplies are systematically reported on an accrual basis where the statute prescribes a payment basis, unless cash-basis tax exigibility is configured on every service tax. The reports do honour `tax_exigible` (`account_generic_tax_report.py:59`), so cash-basis configuration is the only available mechanism; whether it is applied is a configuration question, recorded as `P07-U-16`. |
| `V-D-03` | Tax invoice is a numbered statutory document issued at the tax point | Print rendering of the accounting document | No issuance timestamp, no serial number distinct from the journal sequence, no copy, no reissue, no cancellation of a document (only reversal of an accounting entry). |
| `V-D-04` | Credit / debit note adjusts in the month **issued / received**, referencing the original tax invoice | Reversal entry netted by sign in the same report population | The adjustment is not identifiable as an adjustment, is not linked to the original tax invoice, and is placed by accounting date rather than by note date. |
| `V-D-05` | Filing is **per place of business** | Per company, optionally grouped across companies as a tax unit | The statutory filing unit is not representable. |
| `V-D-06` | Zero-rated (s.80/1) and exempt (s.81) are distinct classes | Both selected by `amount_tax = 0` at **move** level | On a mixed-rate invoice the zero-rated and exempt portions appear on neither the main report (excluded by the group-name predicate) nor the zero report (excluded because the move's total tax is non-zero). |

## 5. Where `ONE TAX FACT -> ONE CANONICAL TAX EVENT -> ONE ACCOUNTING EFFECT` Is Broken

| # | Break | Evidence |
|---|---|---|
| `V-I-01` | **One tax fact, two report implementations.** The same statutory output/input tax books are produced by two independent code paths with different selection logic, different column semantics and different branch sources: the vendor XLSX generator as overridden by SMEsPlus, and the SMEsPlus dynamic reports. Neither is declared canonical. | `l10n_th_reports/models/tax_report_vat.py:58` vs `l10n_th_reports_ext/models/tax_report_vat.py:11` vs `smesplus_account_reports/models/account_generic_tax_report.py:23` |
| `V-I-02` | **One tax fact, two period attributes.** The period a supply belongs to is determined by the accounting date, while a second period attribute is stored on the move and shown next to it on the same report row. A reader of that report sees two dates and no rule for which governs. | `account_generic_tax_report.py:26` (selection) vs `:38`, `:102-108` (display) |
| `V-I-03` | **One canonical event, two base amounts.** The main reports take the base from the tax repartition detail; the zero-rate reports take it from the raw line balance. The repeated move-header `amount_tax` on the zero reports is numerically inert, because `amount_tax = 0` is itself the row predicate (`:283`, `:454`) — this was over-stated in an earlier draft and is corrected here. The **live** defect on the same SQL is on the base side: the inner join to `account_move_line_account_tax_rel` (`:254`, `:425`) emits one row per (line × tax) each carrying the line's full `balance`, and every row is accumulated (`:299`, `:472`), so a base line carrying two taxes double-counts the statutory base. Latent on the shipped Thai template, where adding a second tax makes `amount_tax` non-zero. | `account_generic_tax_report.py:49-50` vs `:250-254`, `:420-425` |
| `V-I-04` | **Row inclusion depends on a translation mapping rather than on the tax fact.** A row reaches the statutory report only if the raw stored value of its tax group's name equals the dict `{'en_US': 'VAT 7%'}`. See §5.1 — this is materially worse than a mutable-label dependency. | `account_generic_tax_report.py:45`, `:88` |

### 5.1 `V-I-04` in Full — Why It Is a Total-Loss Failure, Not a Selective One

The predicate compares a Python dict literal against a value selected raw from the
database:

- `account_generic_tax_report.py:45` selects `atg.name AS group_name` with no language
  context and no `->>` extraction, so the driver returns the whole stored value.
- `account.tax.group.name` is declared `fields.Char(required=True, translate=True)`
  (`account/models/account_tax.py:32`), so that stored value is a **translation mapping**,
  not a string. This is why the author of the predicate had to write a dict literal at all.
- The Thai chart template ships a Thai name for that group: `account.tax.group-th.csv`
  carries a `name@th_TH` column whose value for `tax_group_vat_7` is
  `ภาษีมูลค่าเพิ่ม 7%`.
- `chart_template._load_translations` (`account/models/chart_template.py:1475-1534`, via
  `_get_field_translation` at `:1452`) imports those `@lang` values into the stored mapping
  when the language is installed.

Consequently, on a Thai-language deployment the stored value carries **two** entries and
the equality against a single-entry dict is false for **every** row. `res` stays empty, so
the handler emits not even a total line (`:144`). Both the Sale VAT Report and the Purchase
VAT Report — the s.87 statutory books — render **no data at all**, silently, with no error.

The base application demonstrates the correct handling of exactly this hazard elsewhere:
`account/models/account_account_tag.py:84` deliberately forces `with_context(lang='en_US')`
before comparing tag names.

Boundary and class: **VERIFIED against a deployed database of the declared generation** — the stored value is `{"en_US": "VAT 7%", "th_TH": "ภาษีมูลค่าเพิ่ม 7%"}` and all five tax groups carry Thai translations (`22 §4.1`). This paragraph read "derived from source, not executed (`P07-U-02`)" until `REV-E-25`. The trigger condition
is "Thai is an installed language on the deployment", which is the expected condition for a
Thai tenant. Recorded as `P07-F-01`, and it is the highest-severity finding in this package.

**Qualified — `P07-F-72`, `P07-F-73`, `22 §17`.** Severity stays `S1`, but the **basis has
changed from realised to prospective with a measured magnitude**. The published trigger
(*installing Thai*) is **refuted**: Thai is active in 4 of 5 deployed identities and only 1
carries the translation. The real condition is the chart template loading **while Thai is
already active** — install order. And the defect fires only in an identity holding **2–3**
VAT-bearing tax lines, while the two deployments holding **5,202** and **32,672** do not fire.
The exposure is what one install ordering would put outside the s.87 registers, not what has
been lost.

## 6. The Two Parallel Report Implementations

| Attribute | Vendor generator (+ SMEsPlus override) | SMEsPlus dynamic reports |
|---|---|---|
| Entry point | XLSX export buttons on the Thai tax report | Dedicated `account.report` records |
| Selection | `strict_range` + membership of the report's base/tax tags | `strict_range` + tax-detail query + literal tax-group-name equality |
| Partner handling | Partnerless rows retained with the caption `Selling goods or providing services` | Partnerless rows **dropped** by an inner join on `res_partner` |
| Branch source | `l10n_th_branch_name` (from `company_registry`), plus `partner.branch` added by the override | `company_registry` |
| Tax-point column | none (override adds "Bill Date" = invoice date, relabels the selection date "Accounting Date") | "Tax Period Date" column, not used for selection |
| Zero / exempt | Included if the tags match | Excluded from the main report; separate report keyed on move-level `amount_tax = 0` |
| Licence of the inherited base | `OEEL-1` (Enterprise) | inherits `account_reports` (Enterprise) |

Both are in the declared source set and both are installable. Selecting between them is a
design decision that has not been recorded anywhere in the declared set.

## 7. Negative Claims Made in This File

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-06` | No tax-point determination logic for VAT was found. | `B — NOT FOUND IN SEARCHED SCOPE` | PATH SET of `13 §2`; patterns of `13 §4`; all 15 modules of `13 §5` read for tax-date handling |
| `P07-N-07` | No import tax point and no s.78/3 special tax point were found. | `B — NOT FOUND IN SEARCHED SCOPE` | as above |
| `P07-N-08` | No self-assessed VAT mechanism (s.83/6) was found in the Thai modules. | `B — NOT FOUND IN SEARCHED SCOPE` | Thai module population only; the base application's reverse-charge facilities were **not** examined |

None of these is stated as "does not exist".
