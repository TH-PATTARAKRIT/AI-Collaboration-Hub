# P01 → P08 (RECORD-TO-REPORT) — CONTROLLED HANDOFF

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001`
Checkpoint `CP-04` · Baseline `a02ec8b` · Deployment `45a8e08e` (`iSMEs`, SWR, 1 company, 183,590 moves)

> **P01 measures. P08 judges.** Nothing below is a reporting conclusion, an accounting-policy position, or a
> Boss decision. P01 has not started P08 work.

---

## 1. THE PRINCIPAL ITEM — PRICE DIFFERENCES CAPITALISED, NO P&L VARIANCE OBSERVED

**Observed in this deployment, in the path P01 traced:**

| Measure | Value | Predicate |
|---|---|---|
| Valuation layers where the price-difference engine **fired** | **1,267** | `price_diff_value IS NOT NULL` (includes 0.00) |
| …where the correction was **material** | **1,123** | `price_diff_value` non-zero |
| …where it ran and produced exactly ฿0.00 | **144** | the difference between the two |
| Total material price difference | **฿2,246,313,274.64** | sum over the 1,123 |
| Journal items on `1173 4310005 Purchase price variance` | **0 of 447,384** | exact match on `account_id` |

**Account 1173 being empty is NOT a defect and NOT evidence of a failure.** Two independent sufficient gates:

1. `purchase_price_diff 16.0.1.1` is installed; its writer gate is
   `purchase_price_diff/models/account_move_line.py:10` — **`if self.product_id.cost_method == 'standard':`** —
   and the **only** `product.category` configuring account 1173 (category 10) has
   `property_cost_method = 'fifo'`.
2. Independently the caller returns early on `not move.company_id.anglo_saxon_accounting`, and that flag is
   **FALSE** on the only company.

*(6 further price-difference account rows are configured at `product.template` level.)*

### 1.1 THE SENTENCE P01 FIRST WROTE HERE WAS FALSE IN BOTH HALVES — REPLACED

P01 drafted: *"purchase price differences are capitalised into inventory and no purchase-price-variance line
reaches the P&L in the observed path."* **AAS-03 Expert 3 falsified both clauses; re-derived here.**

| Where the 1,267 price-difference layers actually point | Layers |
|---|---|
| Still at the **vendor bill** (`AP` journal) — **no GL valuation entry was ever made** | **1,175 (92.7%)** |
| At an **`STJ` Inventory Valuation** entry — a GL entry exists | **92 (7.3%)** |

*Mechanism: `_prepare_in_invoice_svl_vals` is born pointing at the bill; only when
`_validate_accounting_entries` does **not** skip the product (i.e. it is `real_time`) does the valuation entry
overwrite `svl.account_move_id`. **The field is therefore a decisive discriminator** — and it is not
confusable with the `S16-B-05` deletion hypothesis, which would leave it **NULL**, not pointing at a live
posted bill.*

**The 92 that did post move inventory DOWN, not up:**

| Account | Type | Net |
|---|---|---|
| `1141001 Raw material` | asset_current | **−฿7,267,712.95** |
| `2900000 Goods Receipt Note(GRN)` | liability_current | +฿7,270,276.79 |
| **`4010002 Consumption of raw materials`** | **expense_direct_cost** | **−฿2,563.84** |

**"Capitalised" asserts an increase in carried inventory. The observed net is a ฿7.27m reduction** — P08 and
P11 would have planned a reconciliation in the wrong direction.

**And a P&L line does exist.** `stock_move.py:380` `_get_src_account` falls back to the category's
`stock_input`, which is **not constrained to be a balance-sheet account** — **4 of 22 configured categories
point it at a P&L expense account**, and it fired twice in-path for −฿2,563.84.
*Positive control: the same detector returns 9,148 P&L lines across the whole `STJ` journal, so "2" is a
measurement, not a dead query.*

**For the 1,175 with no GL entry, the price sits in the P&L by construction** — a `manual_periodic` product
produces no receipt entry and no GRNI leg, so the vendor bill debits its own line account at the billed
price. Resolving those lines: **1,016 expense + 66 income + 90 asset + 3 liability — 1,082 of 1,175 (92.1%)
on a P&L account.**

> ### THE REPLACEMENT STATEMENT P08 AND P11 SHOULD CARRY
>
> In this deployment the price-difference engine fired on **1,267** valuation layers. **92** — products in the
> 15 `real_time` categories — produced an `STJ` journal entry, netting **−฿7,267,712.95 against
> `1141001 Raw material`** and **+฿7,270,276.79 against `2900000 GRN`**, with **2 lines landing on the P&L
> account `4010002`**; **5 of those 92 carry an `svl.value` their own entry does not carry.** The remaining
> **1,175 produced no journal entry of any kind** — their products are `manual_periodic` — and **1,082 of
> them sit on a vendor-bill line posted to a P&L account.** A separately-identified purchase-price-variance
> line does not exist **because `anglo_saxon_accounting` is FALSE** — that is **not** evidence that purchase
> price differences are kept out of the P&L. Products in the **4 categories inheriting
> `cost_method='standard'`** are outside this statement entirely.

**Recorded as `ERR-P01-49`.**

### 1.2 "In the observed path" was a description, not a declared set

The phrase bounded nothing. Three bounds it silently contained: the engine **cannot fire on `standard`-cost
products at all** (`account_move.py:59`), and **4 of 30 categories inherit `standard`**; **anglo-saxon is off
company-wide**, which is the actual reason no named variance line exists; and **one company** was observed
while the sentence was written as a system property.

---

## 2. THE CLEARING ACCOUNT IS A SWEPT SUSPENSE ACCOUNT

| Measure | Value |
|---|---|
| Account **39 `2900000 Goods Receipt Note(GRN)`**, `liability_current` | — |
| **POSTED** journal items | **13,666** |
| **POSTED-only net** | **−฿7,048,692.08** |
| Cancelled items / net | 53 / +฿76,422,354.13 |
| Draft items / net | 17 / +฿2,724,152.20 |
| All-states net *(withdrawn as a published figure)* | ~~฿72,097,814.25~~ |
| `reconcile` flag | **`'f'`** — positive control: 29 of 339 accounts are `'t'` |
| Manual `MISC` sweeps out of the account | **39 items, ฿1.9bn**, driving it to exactly ฿0.00 on five occasions |
| Bill lines relieving it (all states) | 6,653, Dr ฿4,516,394,611.47 — **฿175,017,092.70 of it on cancelled/draft bills** |

**Consequences for R2R:**
- **No receipt is ever matched to its bill at item level** — the account cannot reconcile.
- Two legs can never match by construction: **non-PO bills Dr ฿269,689,658.68**, **vendor returns Dr
  ฿129,086,326.14 against only ฿16.5m of refund credits**.
- **A published GRNI figure inverted in sign under the correct state basis.** See §5.

---

## 3. PERIOD, CUT-OFF AND DATE INTEGRITY

| Item | Measurement |
|---|---|
| **Period locks — now enumerated across every surface in the archive, not one** | Three surfaces exist and all were checked: `res_company.period_lock_date` / `fiscalyear_lock_date` / `tax_lock_date` — **all NULL**; the lock-date wizard table `account_change_lock_date` — **0 rows**; `account_fiscal_year` — **4 rows** (Y2023-2024, Y2024-2025, งบเพิ่มเติม 25, Y2026). **A fiscal year defines period boundaries, not a lock.** Corrected phrasing: **no lock date is set anywhere, on 169,143 posted entries** — and that is now proven by enumeration rather than asserted from one table |
| Bills posted **earlier** than their own invoice date | **5,601 of 36,865 (15.19%)**, p10 = −6 days, min −105 |
| Bills in a **different month** from their invoice date | **2,037 (5.53%)** |
| Bills posted > 31 days after | 25 |
| **Buddhist-era dates** | **materially wider than the 30 P01 first published.** Two experts disagree on extent: **484 values across 14 columns in 11 tables** (+11 at year 8202) vs **12 (table, column) pairs across 7 tables — 120 posted journal items and 120 analytic lines**. **Both far exceed 30; neither is adopted over the other** |
| BE mechanism | dates are **typed, not converted** — no installed module writes or converts them; `th_TH` active, all 178 BE picking dates end `17:00:00` (midnight Bangkok in UTC), correct CE `create_date`s beside them |
| BE origin (the 30 `account_move` cases) | **cash-basis VAT entries derived from posted vendor bills** — they originate in the P2P chain |
| BE effect | the entries are **balanced**, so **the trial balance still balances**; they touch Input VAT ฿7,396.98, Undue VAT ฿7,396.98, Dummy Service ฿211,342.14, and are **invisible to every period-bounded query** |

---

## 4. AP RESOLUTION AND ITS STATE BASIS

| Measure | Value |
|---|---|
| AP journal items (11 payable accounts) | **54,137** |
| Reconciled | **52,996 — 97.89%** |
| Positive control | of those 52,996, **0** carry a non-zero `amount_residual` |
| Open items | **1,141** |
| — `posted` | 539, **−฿98,745,661.71** |
| — **`cancel`** | **559, −฿18,153,699.21** (280 of them from 2023) |
| — `draft` | 43, **+฿13,382,674.68** |

> **A ฿4.77 million spread between two defensible readings of the same field** — posted-only
> −฿98,745,661.71 against all-states −฿103,516,686.24 — **with no lock date and no period close to fix
> either.** Which basis any given report uses **was not established**, and that is the question for P08.

**P01 makes no claim that ฿18.15m is owed.** `amount_residual` on a cancelled document may simply be stale.

---

## 5. A METHOD CONTROL P08 SHOULD ADOPT FROM P01's OWN FAILURE

> **Every aggregate over journal items must declare its state basis in the same line as the number.**

P01 published the GRNI balance as **฿72,097,814.25**. On a posted-only basis it is **−฿7,048,692.08** —
**the opposite sign**. Seventy cancelled and draft items carried the entire published figure.

The control existed: the AP analysis in §4 splits by state *in the same package and the same run*.
**It was applied where it was thought of, and that is not a control.** Corroborating source fact:
`account_reports/models/account_report.py` shows **no Odoo report ever includes cancelled lines**, so an
all-states total corresponds to nothing a user can see.

---

## 6. OTHER ITEMS FOR R2R

| Item | Measurement |
|---|---|
| **Subledger vs ledger divergence** | 30 valuation layers to ±1.5e21; divergence **฿6,462,975,089,678,637.13** — and **invisible in aggregate**: `SUM(value)` over all 74,982 layers is **฿205,490,835.88**. Only a row-level magnitude test finds it |
| **The ledger is NOT clean either** | **8 posted journal items exceed ฿1bn**, incl. `STJ2023110741` at **฿19,784,867,370.00**; a partial revaluation reversal leaves **≈฿39.2m misallocated between WIP and Semi Product** |
| Ten vendor bills outside the AP subledger | payment-term line on `218001` (9, ฿1,788.27) and `221002` (1, ฿11,181.00); total ฿12,969.27 — invisible to an ageing keyed on `liability_payable` |
| Bills with no resolvable account type | 67 journal items |
| Bills with no payable line | 1 of 37,055 |
| Manual valuation interventions | **2,486**, of which **1,354 post to the GL** |
| Inventory entries not dated on their stock move | **33.31%** |
| `stock_landed_costs` | installed, **0 rows** |

---

## 7. LIMITS

- **41 of 651 tables extracted (6.3%)**, no declared selection rule (`GAP-P01-07`). Every negative is bounded by it.
- Nothing executed at runtime in six rounds.
- Thai statutory questions: **none answered**, six routed to **P07**. P01 states no position on Thai law.
- `S16-B-05` (see `P01_TO_P11_HANDOFF.md`) may bear on any zero-link reading P08 inherits from earlier rounds.
