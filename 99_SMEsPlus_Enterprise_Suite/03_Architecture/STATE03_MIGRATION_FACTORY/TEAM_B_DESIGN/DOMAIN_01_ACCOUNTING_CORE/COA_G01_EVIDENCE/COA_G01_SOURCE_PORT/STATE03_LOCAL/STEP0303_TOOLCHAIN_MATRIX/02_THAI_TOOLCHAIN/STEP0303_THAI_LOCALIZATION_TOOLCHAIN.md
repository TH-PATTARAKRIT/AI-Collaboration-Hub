# STEP0303 ANNEX — THAI LOCALIZATION TOOLCHAIN REQUIREMENTS

Every requirement here is **evidence-derived [E]** from the approved 134-module scope.
These are the Thailand-specific capabilities a Node.js build must provide and which a
generic ERP toolchain will not supply by default.

## T1 — BUDDHIST ERA DATES ARE A STATUTORY REQUIREMENT
Evidence: `l10n_th_withholding_tax_report/models/report_withholding_tax.py:93` and `:105` —
`year_thai = int(date.strftime(...)) + 543`.
Thai statutory documents carry **พ.ศ. (Buddhist Era)** years, CE + 543. This project's own
files use it: `03 DATABASE/V2.0/ChatGPT Image 29 มิ.ย. 2569 …png` — 2569 B.E. = 2026 CE.

REQUIREMENT: a dual-calendar date service. Every statutory-facing date needs a B.E.
rendering; internal storage stays ISO/Gregorian. This is a formatting and validation
concern, not a storage one — do NOT store B.E. years.

CAUTION FROM THE EVIDENCE: the reference implementation documents its own limit —
*"ไม่รองรับปีก่อน พ.ศ. 2484"* (unsupported before B.E. 2484), because Thailand moved its
new-year date. Historical dates before 1941 CE are not a naive +543 conversion.

## T2 — THAI DATE/TIME FORMATTING IS A 433-LINE PROBLEM
Evidence: `dev_print_cheque/report/thainlp.py` — 433 lines, a vendored copy of PyThaiNLP's
`thai_strftime`, providing Thai weekday and month names plus B.E. year for `%a %A %b %B %y %Y %c`.
REQUIREMENT: a Thai date-formatting capability with Thai month/weekday names. Node's `Intl`
with `th-TH-u-ca-buddhist` covers much of this — **verify against the statutory forms**
rather than assuming parity with the vendored implementation.

## T3 — THAI TEXT SHAPING AND LINE BREAKING IN PRINTED OUTPUT
Thai script has **no spaces between words**, combines above/below-baseline marks, and
requires dictionary-based word segmentation to break lines correctly.
Evidence of the need: cheque printing (`dev_print_cheque`, 76-field layout), the WHT
certificate form (`l10n_th_withholding_tax_cert_form/reports/layout.xml`), and Thai-language
statutory income-type strings in the certificate model.
REQUIREMENT: a rendering path with a real text engine and embedded Thai fonts. This is the
strongest technical reason behind the §2.5 recommendation for HTML→PDF via headless
Chromium: naive PDF primitives break Thai lines mid-word and misplace tone marks.

## T4 — THAI AMOUNT IN WORDS
Evidence: `l10n_th_amount_to_text/models/res_currency.py` overrides `amount_to_text`, gated
on `lang_code == "th_TH"`, using `num2words(lang="th")` plus a Thai currency-name map
(ดอลลาร์ / ยูโร / เซนต์), with an English fallback on `NotImplementedError`.
REQUIREMENT: Thai number-to-words for cheques, WHT certificates and tax invoices, with a
graceful fallback. Note the reference implementation handles satang (fractional) separately
from baht — a Node equivalent must be validated on fractional amounts.

## T5 — PROMPTPAY QR
Evidence: `invoice_promptpay` declares external dependency `promptpay` and renders a QR into
the invoice report.
REQUIREMENT: EMVCo-compatible PromptPay payload generation plus QR rendering.

## T6 — STATUTORY OUTPUT IS SPREADSHEET AS WELL AS PDF
Evidence: `l10n_th_withholding_tax_report` declares `xlsxwriter` and `xlrd`, depends on
`report_xlsx_helper`, and ships an XLSX report with a period wizard.
REQUIREMENT: XLSX generation is a first-class output format, not an export convenience.

## T7 — THAI PARTY IDENTITY AND ADDRESS HIERARCHY
Evidence: `l10n_th_partner` adds `branch` (Tax Branch) and `name_company`;
`partner_company_type` adds Thai legal titles; `l10n_th_base_location` + `base_location`
add `res.city.zip` for the Thai address hierarchy, imported from GeoNames.
REQUIREMENT: tax ID + tax branch code + Thai legal title + Thai/English name pair, and a
province/district/subdistrict/postcode hierarchy. Supports frozen findings S3 and S5.

## T8 — PYTHON DEPENDENCIES NEEDING NODE EQUIVALENTS
Declared `external_dependencies` across the approved Boss Extra scope — each needs a
verified Node equivalent, or a deliberate decision to do without:
| Python dep | Purpose (evidence) | Node equivalent status |
|---|---|---|
| num2words | Thai amount in words (T4) | must verify Thai + satang support |
| promptpay | PromptPay QR (T5) | must verify EMVCo payload correctness |
| xlsxwriter / xlrd | statutory XLSX output (T6) | mature options exist |
| redis | session store (`wk_redis_session`) | direct equivalent |
| boto3 / dropbox / paramiko | backup targets (`auto_database_backup`) | direct equivalents |
| openai | AI module in reference scope | direct equivalent |

## T9 — COLLATION AND SEARCH
Not directly evidenced, flagged as a known risk **[J]**: Thai sorting and search need an
ICU-aware collation, and Thai text search needs segmentation. Verify at implementation;
do not assume default database collation is adequate for Thai name ordering.
