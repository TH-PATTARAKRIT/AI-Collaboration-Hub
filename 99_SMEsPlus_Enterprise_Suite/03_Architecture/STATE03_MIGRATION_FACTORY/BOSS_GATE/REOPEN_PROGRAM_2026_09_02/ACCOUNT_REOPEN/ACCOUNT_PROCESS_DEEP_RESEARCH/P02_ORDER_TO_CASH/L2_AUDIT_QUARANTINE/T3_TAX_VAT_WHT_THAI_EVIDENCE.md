# T3 EVIDENCE EXTRACT — TAX: VAT, WHT, TAX POINT, TAX PERIOD, THAI LOCALISATION

`LAYER 2 — AUDIT QUARANTINE` · Parallel research track T3 · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Reference root: `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons`

## §0 DENOMINATOR

| Element | Declaration |
|---|---|
| POPULATION | The reference addons root — **791 module directories**, 797 top-level entries. |
| PATH SET (primary) | `account/`, `account_reports/`, `account_accountant/`, `sale/`, `l10n_th/`, `l10n_th_reports/` |
| PATH SET (negative sweep) | The **entire** root, recursive, all file types unless a narrower include is stated per claim. |
| UNIT | Q1–Q5, Q7, Q8: one code site (`path:line`). Q2: one field definition. Q6: one file. |
| METHOD | Read-only shell inspection. **Runtime behaviour was not executed** — every statement is static-source derived. |
| DECLARED EXCLUSIONS | Translation catalogues excluded from counts where noted; test directories excluded from field enumeration but **retained** for the withholding negative sweep. |

## §1 What date drives the tax report for a customer invoice

- **There is no separate tax-point / tax-date field** on the accounting document or its lines. — `FACT VERIFIED`
- The tax report filters on the line's date, which is a **stored related of the document's accounting date**,
  not the document date — `account/models/account_move_line.py:70-71`; report scope domain
  `account_reports/models/account_report.py:801`, injected into every report query at `:2074`. — `FACT VERIFIED`
- The document date is also stored on the line (`account/models/account_move_line.py:75-76`) but is **not
  referenced by the generic tax report handler** (zero hits). — `FACT VERIFIED`
- **The silent VAT-period shift is real.** Posting overwrites the accounting date when a lock date is violated
  and does **not** touch the document date — `account/models/account_move.py:4933-4936`; target computed at
  `:5674`, then for a sale document `min(today, end of month or year)` at `:5675-5681`. — `FACT VERIFIED`
- For sale documents the shift happens **only at post time**, not at draft-compute time — the draft compute
  calls the shifting helper only for non-sale documents (`account/models/account_move.py:806-808`). — `FACT VERIFIED`
- **Consequence for O2C:** a customer invoice whose document date falls at or before an effective lock date is
  posted with a **later accounting date**, and because the tax report keys on the accounting date, **the VAT
  falls into the later tax period while the printed tax invoice still shows the original date.** The user is
  warned in the UI before posting (`account/models/account_move.py:676`, text at `:5713-5717`) but nothing
  blocks it. — `SUPPORTED INTERPRETATION`
- The tax lock date is consulted only when the document actually affects the tax report — the
  tax-affecting predicate is at `account/models/account_move_line.py:1269-1271`, routed through
  `account/models/company.py:646-660`, `:619`. — `FACT VERIFIED`

## §2 Lock dates — complete enumeration

**DENOMINATOR** — POPULATION: every field definition in the root matching `lock_date = fields\.` in `*.py`,
test directories excluded. PATH SET: whole root. UNIT: one field definition.
**Result: 22 definitions across 4 files** — of which **5** are the substantive stored company lock dates,
5 are computed per-user mirrors, 6 belong to the lock-exception model, and 6 are transient wizard fields.

The canonical list is a module constant — `account/models/company.py:54-63`: four soft lock dates plus one
hard lock date.

| # | Lock date | Definition | Effect | Bypass |
|---|---|---|---|---|
| 1 | Global | `account/models/company.py:73` | any entry at or before the date is postponed per journal sequence; enters the user-effective computation unconditionally (`:572`) | soft exception |
| 2 | Tax return | `:78` | consulted **only** when the document bears tax (`:619`); blocks post-hoc edits to tax-bearing posted lines (`account/models/account_move_line.py:1273-1288`) | soft exception |
| 3 | Sale | `:84` | applied only to sale journals (`:573-574`) | soft exception |
| 4 | Purchase | `:89` | applied only to purchase journals (`:575-576`) | soft exception |
| 5 | **Hard** | `:94` | irreversible | **none** |

- **The hard lock admits no exception** — excluded from the soft list and from the exception model's
  selection, which lists exactly four values (`account/models/account_lock_exception.py:52-57`); its
  user-mirror ignores exceptions entirely (`account/models/company.py:397-401`). — `FACT VERIFIED`
- **It cannot be lowered or removed** — `account/models/company.py:496-499`; duplicated in the wizard
  (`account_accountant/wizard/account_change_lock_date.py:235-236`). — `FACT VERIFIED`
- **Who can bypass a soft lock:** an exception row lowers the effective lock for a specific user (or for
  everyone) until an end datetime — `account/models/company.py:545-552`, `:556-560`. — `FACT VERIFIED`
- **Who may create one:** the accounting-manager group by ACL (`account/security/ir.model.access.csv:19`;
  ordinary users read-only at `:18`) and by explicit wizard gate
  (`account_accountant/wizard/account_change_lock_date.py:352`, `:361`); revocation gated at
  `account/models/account_lock_exception.py:260`. Creation is audit-logged to the company record with tracking
  values (`:219-231`). — `FACT VERIFIED`
- **Two further bypasses of the date/sequence constraint** (not of the lock itself): a system parameter
  disabling the alignment check below a cut-off date (`account/models/sequence_mixin.py:158-170`), and an
  override restricting the check to posted, non-quick-edit documents (`account/models/account_move.py:3475-3477`). — `FACT VERIFIED`
- **The tax lock date is set automatically by the tax closing** —
  `account_reports/models/account_move.py:132-133`, gated on the accounting-manager group at `:127-128`. — `FACT VERIFIED`
- Tax-protected field set — `account/models/account_move_line.py:3365-3372`. — `FACT VERIFIED`
- Pre-conditions to raising a lock: no draft entries in the period for the hard lock
  (`account/models/company.py:501-516`); no unreconciled bank statement lines for global/hard (`:520-528`);
  lock dates cannot be set in the future (`account_accountant/wizard/account_change_lock_date.py:245-246`). — `FACT VERIFIED`

## §3 VAT computation on a sale

- Price-include is a **two-tier resolution** — company default plus per-tax override
  (`account/models/account_tax.py:157-158`, effective value at `:284-289`). — `FACT VERIFIED`
- **Tax is computed on the post-discount unit price** — `account/models/account_tax.py:1383`, passed in at
  `:1385-1390`. The order line's discount is copied verbatim to the invoice line
  (`sale/models/sale_order_line.py:1404`). — `FACT VERIFIED`
- The rounding method lives on the company, **defaulting to round-per-line**
  (`account/models/company.py:125-128`); exposed read-only on the document and its lines
  (`account/models/account_move.py:368-369`, `account/models/account_move_line.py:376-377`). — `FACT VERIFIED`
- Consumption points — `account/models/account_tax.py:1388`, `:1401`, `:1407`; kernel at `:1015`, `:1070`. — `FACT VERIFIED`
- **Where the round-globally difference lands** — `account/models/account_tax.py:1429`, in two dispatch steps:
  the tax-line-level delta is pushed onto the **largest** contributing bucket (`:1644-1646`), and the residual
  per-tax delta is distributed one currency-rounding unit at a time across base lines sorted by descending
  tax-inclusive total (`:1683-1697`, worked example at `:1647-1653`). — `FACT VERIFIED`
- **`CONTRADICTED`** — the rounding-type line on the accounting document is **not** the tax-rounding-difference
  line. It is the **cash rounding** line, produced only when a cash-rounding rule is set
  (`account/models/account_move.py:2620`), with two strategies: attach to the largest existing tax line,
  inheriting its account, repartition and **tax tags** (`:2623-2639`), or post to a dedicated gain/loss account
  with tax cleared (`:2641-2650`). Removing the setting unlinks the line (`:2658-2662`).
- **Two distinct rounding residues therefore exist and land in different places:** the round-globally tax
  delta is absorbed **inside the tax amounts themselves** (no dedicated line, no separate account), while the
  cash-rounding residue gets its own line which, under the first strategy, **carries tax tags and so reaches
  the tax report** (`:2635`). — `SUPPORTED INTERPRETATION`

## §4 Cash-basis VAT — central for Thailand

- The switch is two-level: a company master switch (`account/models/company.py:219`) plus a per-tax
  exigibility selection defaulting to on-invoice (`account/models/account_tax.py:180-185`). — `FACT VERIFIED`
- The not-yet-exigible tax sits in the tax's **own transition account**
  (`account/models/account_tax.py:186-190`), substituted for the real tax account at line-creation time
  (`:2920-2921`). — `FACT VERIFIED`
- **The entry is created only during reconciliation**, and only when a receivable or payable line is involved
  — `account/models/account_move_line.py:2545-2552`; skipped entirely under the cancelling-reversal or
  no-cash-basis contexts. — `FACT VERIFIED`
- **How it is dated** — `account/models/account_partial_reconcile.py:512-517`: the later of the two document
  dates (`:79-85`), **jumping to today** if that date is on or before the fiscal lock. **The lock consulted is
  the fiscal/hard/journal-type lock — NOT the tax lock date.** — `FACT VERIFIED`
- **Consequence:** a cash-basis entry can be dated into a period already closed for tax purposes; the
  write-time tax-lock check (`account/models/account_move.py:3236`) is the only backstop. — `SUPPORTED INTERPRETATION`
- The tax report excludes non-exigible lines — `account_reports/models/account_report.py:2082-2083`; domain at
  `account/models/account_move_line.py:3340-3353`; the cash-basis entry is itself always exigible (`:3348`). — `FACT VERIFIED`
- **The Thai tax reports inherit the exigibility filter** — the generic tax report sets it
  (`account/data/account_reports_data.xml:11`) and all three Thai reports declare it as their root
  (`l10n_th/data/account_tax_report_data.xml:5`, `:176`, `:238`), the field being computed from the root
  (`account/models/account_report.py:47-49`). — `FACT VERIFIED`
- **A cash-basis entry can never be reset to draft** — `account/models/account_move.py:5348-5350`. — `FACT VERIFIED`
- **The delivered Thai tax data does NOT enable cash basis.** The Thai tax template CSV has 13 columns and
  **no exigibility column**, so all **18** Thai taxes take the on-invoice default; no transition account is set
  for any Thai tax, and the 27-account Thai chart contains no cash-basis transition account. — `FACT VERIFIED`

## §5 Withholding tax

**SEARCH SCOPE FOR THIS SECTION: the whole addons root, recursive.**

- **There is no dedicated withholding mechanism. Withholding is modelled as an ordinary tax with a negative
  percentage.** In the Thai tax template, **12 of the 18 taxes are withholding**, all percentage-type with a
  negative amount. — `FACT VERIFIED`
  - Purchase-side, company payee (PND53 family): 1%, 2%, 3%, 5% —
    `l10n_th/data/template/account.tax-th.csv:26,30,34,38`; base repartition tagged as PND53 income, tax
    repartition tagged PND53, posted to the withholding liability account.
  - Purchase-side, individual payee (PND3 family): 1%, 2%, 3%, 5% — `:42,46,50,54`, tagged PND3.
  - **Sale-side (withholding suffered on our own receipts): 1%, 2%, 3%, 5%** — `:58,62,66,70`, tax-excluded,
    posted to the withholding **asset** account.
- The two withholding accounts: withholding income tax, code 1520, current asset
  (`l10n_th/data/template/account.account-th.csv:9`); withholding tax, code 2320, current liability (`:15`). — `FACT VERIFIED`
- **The sale-side withholding taxes carry NO tax tags.** All four have empty tag cells (`:58-73`), whereas all
  eight purchase-side withholding taxes are tagged. — `FACT VERIFIED`
- **Material consequence for O2C:** the PND report handlers select rows **exclusively by tag**
  (`l10n_th_reports/models/tax_report_pnd.py:98`, `:135`). Because the sale-side withholding taxes carry no
  tags, **customer-side withholding does not appear on either PND report.** The PND reports cover only
  withholding the company itself withholds and remits. — `SUPPORTED INTERPRETATION`
- **Withholding has no document identity of its own.** No withholding-certificate model, no
  withholding-specific sequence, no flag: the patterns `is_withholding` and `withholding_sequence` return
  **zero hits root-wide** (all file types), and **no module directory matches** `*withhold*` or `*wht*`. — `FACT VERIFIED`
- Total footprint of the token `withhold` (case-insensitive) root-wide is 7 modules; excluding translation
  catalogues the accounting-module hits are two unit tests exercising a negative tax and a subtotal label, plus
  one boilerplate paragraph in the default terms-and-conditions template. The remaining hits are an unrelated
  country-state code. — `FACT VERIFIED`
- **The only structural support for presenting withholding separately is the tax-group preceding-subtotal
  label** (`account/models/account_tax.py:57`, consumed at `:2311-2315`). The Thai chart defines five tax
  groups and **sets no preceding subtotal on any of them** (the CSV carries only id, name and country). — `FACT VERIFIED`

## §6 Thai localisation modules — complete enumeration

**DENOMINATOR** — POPULATION: every file under the two module directories. PATTERN: `find -type f`.
UNIT: one file. **Result: 17 + 10 = 27 files.** No sub-selection.

### Base Thai accounting module (17 files)

Auto-installs with the accounting module. Contents:
- Chart template: four property accounts and company defaults including the Thai fiscal country and the
  default sale and purchase taxes (`l10n_th/models/template_th.py:11-16`, `:18-31`).
- **Exactly one new partner field** — a computed, non-stored branch name rendering either
  `"Branch <company registry>"` or `"Headquarter"`, empty for non-Thai or non-company partners
  (`l10n_th/models/res_partner.py:8-16`).
- One accounting-document override — the invoice report template selection when the fiscal country is Thai
  (`l10n_th/models/account_move.py:6-10`).
- A report guard restricting the commercial-invoice PDF to invoices (`l10n_th/models/ir_actions_report.py:8-13`).
- Payment QR support: proxy types, a 13-digit tax-ID and 10-digit mobile format constraint
  (`l10n_th/models/res_bank.py:11-14`, `:16-26`, `:34-`).
- **Three report records** — a VAT return, PND53 and PND3 — all rooted on the generic tax report, country-gated.
- **27 accounts, 5 tax groups, 18 taxes.**

**The VAT return structure** (`l10n_th/data/account_tax_report_data.xml`, fiscal-position filter enabled at
`:7`) has 12 numbered lines in four blocks: Output Tax (lines 1–5, `:16-69`), Input Tax (6–7, `:71-99`),
Value Added Tax (8–10, `:101-140`), Net Tax (11–12, `:142-171`). — `FACT VERIFIED`

**The PND reports** (`:174-231`, `:233-`) each have four tag-driven lines: total income, total remittance,
surcharge, and an aggregated total. — `FACT VERIFIED`

**The "Tax Invoice" document title** is emitted for a **posted customer invoice** when the fiscal country is
Thai — `l10n_th/views/report_invoice.xml:14-19`. The same template injects the branch name after the partner
tax number in all three address blocks (`:4-13`). A separate commercial-invoice PDF action exists (`:31-39`). — `FACT VERIFIED`

### Thai accounting reports module (10 files)

Enterprise-licensed, auto-installing, depending on the base Thai module and the reporting engine.
- Binds custom handlers onto the three existing reports — **it defines no new report records**.
- Three abstract handler models for the PND family; a 16-column CSV export; no dynamic lines.
- One handler adding two spreadsheet buttons, sales and purchase tax reports, gated on the Thai fiscal country.

**The PND export uses the accounting date, and derives the withholding amount arithmetically rather than
reading the posted tax line** — `l10n_th_reports/models/tax_report_pnd.py:43`, `:46`. — `FACT VERIFIED`

**Two hard-coded values in the PND export:** the withholding condition is the literal `'1'` (`:47`), and the
income type is a rate-based mapping — 1%→Transportation, 2%→Advertising, 3%→Service, 5%→Rental, otherwise
empty (`:48-54`). The PND53 export hard-codes a Thai title string (`:98`); PND3 passes no title (`:135`). — `FACT VERIFIED`

**The spreadsheet VAT reports use the accounting date, filter on posted state, and count only the 7% tax
group** — `l10n_th_reports/models/tax_report_vat.py:62`, `:66`, `:124-134`, `:138`. The header prints company
name, tax number and branch name (`:107`); the columns include a tax-invoice number mapped to the document
name (`:114`, `:136`). — `FACT VERIFIED`

**`UNRESOLVED — EVIDENCE REQUIRED`** — whether the 12-line VAT return is the intended statutory filing form.
The identifying tokens return **zero hits** across all 27 files. The mapping is asserted nowhere in code.

## §7 Fiscal position remapping — order time vs invoice time

- The fiscal-position models live in the accounting module's partner file, not a dedicated file
  (`account/models/partner.py:150`, `:157`, `:246`, `:301`). — `FACT VERIFIED`
- **Remapping is a pure dictionary substitution** (`account/models/partner.py:150-155`, `:157-158`); unmapped
  taxes and accounts pass through unchanged, and one source tax may map to several destination taxes. — `FACT VERIFIED`
- Resolution order (`:246-286`): intra-union same-prefix collapse; then a **manually set** position on the
  delivery or invoicing partner **always wins** (`:270-275`); otherwise the highest-ranked auto-apply position
  (`:281-286`, ranking at `:225-242`). — `FACT VERIFIED`
- **Capture is at ORDER time for the taxes, and the order's stored position is copied to the invoice:**
  - order-line taxes are computed once through the order's position
    (`sale/models/sale_order_line.py:534`, `:531`, `:522`) and the recompute trigger
    (`:507`) **does not include the fiscal position**;
  - invoice lines copy the order-line taxes verbatim (`:1407`);
  - the header position is copied from the order's stored value (`sale/models/sale_order.py:1418`). — `FACT VERIFIED`
- The order's position is a stored computed field with manual override
  (`sale/models/sale_order.py:177-184`), recomputed on partner/company changes (`:403`) — **the customer's
  position property is not in that dependency list**. — `FACT VERIFIED`
- **Direct answer: changing a customer's fiscal position after order confirmation does NOT change the tax on
  the eventual invoice**, for three independent reasons: (a) the order's position is not recomputed;
  (b) even if it were, the order line's tax compute does not depend on it; (c) the invoice line copies the
  frozen tax set. The same holds on the invoice side — the invoice-line tax compute depends on product and
  unit only (`account/models/account_move_line.py:869`), **not** on the document's fiscal position, even though
  the underlying helper would apply the mapping if it ran (`:898-899`). — `SUPPORTED INTERPRETATION`
- The change is only ever applied by an **explicit user action**: both models set a warning flag rather than
  recomputing (`sale/models/sale_order.py:419-420`, `:876-881`; `account/models/account_move.py:2211-2213`),
  and the actual recompute is a manual button that posts a chatter message naming the position used
  (`sale/models/sale_order.py:1327-1340`, `:1333-1334`). — `FACT VERIFIED`
- **After posting the position is frozen** — it is in the unmodifiable-field set for posted documents
  (`account/models/account_move.py:3247`, raising at `:3250`), unless a skip flag is set in context. — `FACT VERIFIED`
- A country-consistency constraint exists (`account/models/account_move.py:2411-2422`). — `FACT VERIFIED`

## §8 Sequence and tax-invoice-number integrity

- Uniqueness is enforced by a **partial unique index scoped to posted documents per journal** —
  `account/models/account_move.py:713-715`, index created at `:730-735`; sequence index field at `:93`;
  the mixin warns if no unique index covers the sequence field (`account/models/sequence_mixin.py:81-86`). — `FACT VERIFIED`
- **Numbering is NOT gapless by construction. Gaps are detected and reported, not prevented** —
  `account/models/account_move.py:927-935`, invoked from write at `:3257-3258`. — `FACT VERIFIED`
- The date/sequence alignment constraint (`account/models/sequence_mixin.py:159-179`) is **skipped for draft
  documents and quick-edit mode** (`account/models/account_move.py:3475-3477`), and can be globally relaxed by
  a configuration parameter (`account/models/sequence_mixin.py:158-161`, `:170`). — `FACT VERIFIED`
- The name is not recomputed once posted (`account/models/account_move.py:894-911`, `:903`; the
  posted-before flag set at `:4959`, not copied `:294`). — `FACT VERIFIED`

### Can a posted customer invoice be reset to draft and renumbered?

- **Reset to draft is permitted by default**, with four blocking conditions
  (`account/models/account_move.py:5275-5276`, `:5277-5278`, `:5317-5351`), the decisive one being
  `:5351-5352` — a locked (hashed) entry cannot be reset. — `FACT VERIFIED`
- **Renumbering after reset is blocked when the document is hashed** — write refuses any change to the
  integrity-hash fields (`account/models/account_move.py:3208-3214`), and for hash versions 2–4 that field
  list **includes the document name** (`:3837-3838`; version 1 omits it). The same guard exists on lines
  (`account/models/account_move_line.py:1554-1563`). — `FACT VERIFIED`
- **Hashing is opt-in per journal** (`account/models/account_move.py:317`); it runs on transition to posted
  (`:3287`), the hash domain filters journals with the restrict mode on (`:3859`), and the secured flag is
  simply "has a hash" (`:953-956`). A user may also force-hash (`:5354-5355`). — `FACT VERIFIED`
- Additional renumbering guards independent of hashing: journal cannot be changed on a document posted before
  or bearing a sequence number unless the name is first cleared (`:3215-3227`); changing name or date on a
  posted document triggers the fiscal and tax lock checks (`:3230-3236`), as does un-posting (`:3238-3241`);
  a name not matching the journal's override pattern is refused for non-managers (`:3253-3256`); deletion
  requires no hash, a date after the fiscal lock, and no audit-trail protection (`:4806-4809`). — `FACT VERIFIED`
- **Bulk renumbering exists as a manager-only wizard** (`account/wizard/account_resequence.py:155-171`, ACL at
  `account/security/ir.model.access.csv:126`). It refuses **date-ordered** resequencing on a hashed journal
  (`:157-159`) — **the keep-order branch is not blocked by that check.** — `FACT VERIFIED`
- **Direct answer: yes by default.** On a journal without hash restriction and with no lock date covering the
  document, a posted customer invoice can be reset to draft, have its name cleared, and be re-posted under a
  new number — leaving a gap that surfaces only through the gap-detection field. It is blocked **only** when
  the document is hashed, or when its date falls at or before an effective fiscal or tax lock date. — `SUPPORTED INTERPRETATION`

## §9 STATUTORY SEPARATION

For every Thai-law-adjacent item, layer (c) is outside this track's authority and is held.

| # | (a) WHAT THE CODE DOES | (b) WHAT THE LOCALISATION ASSERTS | (c) THAI LAW / STANDARD — `HOLD — STATUTORY EVIDENCE REQUIRED` |
|---|---|---|---|
| T3-S1 | Tax reporting keys on the accounting date; posting can push that date forward past a lock while the document date is unchanged. | Nothing — the localisation adds no tax-point field and no override of the date logic; its reports read the accounting date. | Which date constitutes the VAT tax point for goods vs services, and whether an accounting date differing from the tax-invoice date is admissible. Sources to read: **Revenue Code Part 4 (VAT) ss.78, 78/1, 86, 86/4** and Revenue Department notifications thereunder. |
| T3-S2 | All 18 Thai taxes take the on-invoice default; cash-basis machinery exists in core but is not enabled by the Thai data. | The localisation ships **no** cash-basis VAT configuration. | Whether VAT on services is due on receipt of payment, and whether an accrual-only configuration is compliant. Sources: **Revenue Code s.78/1(1), s.82/3** and Revenue Department guidance on the service tax point. |
| T3-S3 | The printed title is the literal "Tax Invoice" for a posted customer invoice in a Thai company; the branch is rendered from the company registry. | Asserts by construction that a posted customer invoice **is** the tax invoice, and that the company registry is the branch identifier. | Mandatory particulars of a full tax invoice, branch-number format, and whether the accounting-system invoice may serve as the tax invoice. Sources: **Revenue Code s.86/4** and the notification on tax-invoice particulars and branch numbering. |
| T3-S4 | Three reports: a 12-line VAT return and two withholding CSV exports; the VAT line numbering mirrors a return-form layout. | Names them "Tax Report", "PND53", "PND3". The statutory form identifiers appear **nowhere**. | Whether the 12-line report corresponds to the statutory VAT return form, and whether the CSV layouts are accepted e-filing formats. Sources: **Revenue Department forms P.P.30, P.N.D.3, P.N.D.53** and their current e-filing specifications. |
| T3-S5 | The withholding condition is hard-coded to `'1'`; the income type is derived from the rate. Rates ship as 1/2/3/5%. | Asserts a fixed remittance condition and a rate→income-type mapping. | Whether that condition is correct in all cases, whether the mapping is exhaustive, and whether the rates are current. Sources: **Revenue Code ss.3 tredecim, 50, 69 bis, 69 ter**; Revenue Departmental Instruction **Tor.Por. 4/2528** as amended. |
| T3-S6 | Sale-side withholding taxes carry no tags, so customer-withheld tax reaches neither report. No certificate model or sequence exists anywhere in the tree. | Provides only the two accounts and the negative-rate taxes; makes no claim about certificates. | Whether a withholding certificate must be issued and retained, its numbering and particulars, and how tax withheld by customers is evidenced and claimed. Sources: **Revenue Code s.50 bis** and the notification prescribing the certificate form. |
| T3-S7 | Renumbering a posted invoice is blocked only by hashing or lock dates. Journal hashing is off unless enabled. | The localisation sets no journal hashing, no name-override pattern, and no default lock dates. | Whether Thai law requires gap-less, immutable, sequentially numbered tax invoices and prohibits renumbering. Sources: **Revenue Code s.86/4(2), s.87**; **Accounting Act B.E. 2543** retention provisions. |
| T3-S8 | 7% throughout; the spreadsheet report counts only the 7% group. | Asserts 7% as the standard rate and treats it as the only rate worth reporting. | Whether 7% is the currently effective standard rate and whether other rates must be reported separately. Sources: **Revenue Code s.80** and the current Royal Decree reducing the rate. |

## §10 NEGATIVE CLAIMS (each with search scope)

1. **No dedicated withholding mechanism** — not found in the entire root (791 module dirs, all file types,
   recursive) under `is_withholding`, `withholding_sequence`. `VERIFIED ABSENCE` within the population.
2. **No module dedicated to withholding** — not found among the 791 top-level directories under the name globs
   `*withhold*`, `*wht*`. `VERIFIED ABSENCE` within the population.
3. **No withholding certificate model** — not found in the 27 Thai-localisation files under `-i withhold` and
   the withholding acronym. `VERIFIED ABSENCE` within the two modules.
4. **No separate tax-point / tax-date field** — not found in the four primary path-set modules (`*.py`,
   `*.xml`) under `tax_date` excluding the tax-lock field, nor root-wide under `date_tax\b` in `*.py`.
   `NOT FOUND IN SEARCHED SCOPE`
5. **A dedicated fiscal-position model file is absent** from the accounting module's model directory; the
   models reside in the partner file. `VERIFIED ABSENCE` of the file only.
6. **No document-date reference in the generic tax report handler** — zero hits in that file.
   `VERIFIED ABSENCE` within the file.
7. **No statutory VAT-return form identifier** — not found in the 27 Thai-localisation files (all types) under
   the form-name and Thai-script patterns. `VERIFIED ABSENCE` within the two modules.
8. **No exigibility column in the Thai tax template** — not found in that CSV's 13-column header; consequently
   no Thai tax is configured for cash-basis VAT. `VERIFIED ABSENCE` within the file.
9. **No preceding-subtotal set on any Thai tax group** — the CSV carries only id, name and country, 5 data
   rows. `VERIFIED ABSENCE` within the file.
10. **No new report records in the Thai reports module** — the data file only attaches handlers to the three
    reports already defined. `VERIFIED ABSENCE` within the file.
11. **No Thai override of the accounting-date, posting or lock-date logic** — not found in the five Thai model
    modules under the relevant patterns; the only accounting-document override is the report-template
    selection. `VERIFIED ABSENCE` within the module.
12. **The fiscal position is not a dependency of tax recomputation** — absent from the declared dependencies of
    both the invoice-line and order-line tax computes. `VERIFIED ABSENCE` within those declarations.
13. **The tax lock date is not consulted when dating a cash-basis entry** — the dating code uses the
    fiscal/hard/journal-type lock only. `VERIFIED ABSENCE` within that code site.
