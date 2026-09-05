# 50 — P05 TX-01 SCREEN vs CSV DIVERGENCE

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E10`, `CP-P05E11`

## 1. Denominator Verified on the Target Platform

Round 2 measured `iSMEs` **v16**: 5,426 of 5,863 = 92.55%. **Re-measured on `idemo18_uat`, Odoo 18 —
the platform the source analysis was actually conducted against:**

| Measure | `iSMEs` v16 | **`idemo18_uat` v18** |
|---|---|---|
| `account_move_line` rows | 447,384 | **40,353** |
| WHT configuration codes | 7 | **40** |
| Distinct WHT accounts | **1** (`1137`) | **4** (`65`, `103`, `141`, `179`) |
| Companies | 1 | **4** (codes split 8/16/8/8) |
| Lines on a WHT account | 5,863 | **358** |
| — **WITH** `tax_line_id` | 437 | **0** |
| — **WITHOUT** `tax_line_id` | 5,426 | **358** |
| **% carrying no `tax_line_id`** | **92.55%** | **100.00%** |
| `display_type` of those lines | `product` | **`product` (all 358)** |

**On the v18 target the divergence is total.** Every line posted to a withholding account is a
`product`-type line with a null `tax_line_id`.

Query definition, declared: numerator = `account_move_line` rows whose `account_id` ∈
`{account_withholding_tax.account_id}` and whose `tax_line_id` is NULL; denominator = the same set
without the NULL condition. Extraction: `pg_restore --data-only --table=...`, COPY block parsed on the
column order in its own header. Read-only.

## 2. Correction to Round 2

`TX-01a` claimed *"all seven withholding codes point at one GL account, so the account cannot
discriminate rate or income type; and `WHT3%` is configured with a rate of 0."*

**That is `iSMEs` v16-specific and does NOT generalise.** On v18 there are **four** WHT accounts across
four companies, and the rate distribution is 1/2/3/5 × 10 codes each — **no zero-rate code**.
`TX-01a` is re-bounded to `iSMEs` v16 only. `RE-23`.

## 3. The Chain — Screen vs CSV

| Stage | Screen (on-report) | CSV export |
|---|---|---|
| Journal item | same rows | same rows |
| WHT account | same | same |
| `tax_line_id` | **not consulted** | **join key** |
| Predicate | `engine="tax_tags"` — sums by `tax_tag_ids` (`l10n_th/data/account_tax_report_data.xml`) | `JOIN account_tax tax ON tax.id = account_move_line.tax_line_id` — an **inner** join (`l10n_th_reports/models/tax_report_pnd.py:57`) |
| Custom WHT line carries `tax_tag_ids`? | **yes** — planted at `l10n_th_withholding_tax/wizard/account_payment_register.py:21-25` | irrelevant to the join |
| Custom WHT line carries `tax_line_id`? | irrelevant | **no** |
| Result | line **included** | line **excluded** |

**Structural proof the eligibility predicates differ, and why the null is guaranteed:**
`account_move_line.tax_line_id` is declared `related='tax_repartition_line_id.tax_id', store=True,
precompute=True` (`account/models/account_move_line.py:206-211`). It is **not independently settable**.
Neither the custom module nor core's write-off construction
(`account/wizard/account_payment_register.py:1018-1024`, whose vals dict contains only `name`,
`account_id`, `partner_id`, `currency_id`, `amount_currency`, `balance`) ever sets
`tax_repartition_line_id`. **The null is overdetermined, not incidental.**

## 4. Classification

| Aspect | Class |
|---|---|
| Source behaviour — two different eligibility predicates | **DIVERGENCE VERIFIED** |
| ORM structural guarantee of the null | **DIVERGENCE VERIFIED** |
| Database population, v18 target | **DIVERGENCE VERIFIED — 358 of 358, 100.00%** |
| Database population, v16 | **DIVERGENCE VERIFIED — 5,426 of 5,863, 92.55%** |
| Report behaviour (screen renders the tag-based total) | **VERIFIED from source**; not executed — no rendering was observed |
| Export behaviour (CSV omits the rows) | **VERIFIED from source**; not executed |
| **Thai statutory consequence** | **`HOLD — STATUTORY EVIDENCE REQUIRED`, class **D — UNKNOWN**. P07 owns it. P05 asserts nothing.** |

**Overall: `DIVERGENCE VERIFIED` — and not configuration- or version-dependent.** It reproduces at
v16 and v18, under one-account and four-account configurations, single-company and multi-company.
The only variation is magnitude: 92.55% → **100.00%**.

## 5. What Is Still Not Proven

Neither the screen render nor the CSV file was produced — that needs a running instance
(`HOLD — RUNTIME EVIDENCE REQUIRED`, class **C — NOT YET SEARCHED**, boundary: no instance was run).
The divergence is established from source, from the ORM field definition, and from the data on both
platforms. **The rendered artefacts are inference, and are labelled as such.**

*Class letters added per AAS-03 Challenge D: the mandate requires every negative claim to carry an
A–E letter, and this file previously used bare `HOLD` language without one.*
