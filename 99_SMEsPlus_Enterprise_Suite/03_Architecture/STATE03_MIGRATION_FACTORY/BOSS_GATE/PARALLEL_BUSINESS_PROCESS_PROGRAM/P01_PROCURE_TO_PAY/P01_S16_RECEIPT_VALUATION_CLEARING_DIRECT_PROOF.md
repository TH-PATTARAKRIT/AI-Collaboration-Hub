# P01 — SERIES-16 PURCHASE → RECEIPT → VALUATION / CLEARING DIRECT PROOF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-03`
Deployment: `45a8e08e` (`iSMEs`, SWR), 1 company, archive 2026-07-11.


> ### CORRECTED BY AAS-03 EXPERT 2 — VERIFIED INDEPENDENTLY BEFORE ADOPTION
>
> Three headline figures in this document were wrong and are struck below:
> **(1)** the GRNI balance was an **all-states** figure; posted-only it is **−฿7,048,692.08**, the
> **opposite sign**; **(2)** *"the price-difference engine has never fired"* is **CONTRADICTED** —
> **1,123 layers carry ฿2,246,313,274.64** of `price_diff_value`; **(3)** the periodic-layers-that-posted
> residual is the **vendor-bill price-difference population**, not a policy leak.
> Every correction was re-derived here before acceptance. See `P01_S16_AAS03_FOUR_EXPERT_CHALLENGE.md`.

---

## 1. WHY THIS DOCUMENT MATTERS MORE THAN THE TWO BEFORE IT

P01 has now measured the receipt→valuation→GL path in three generations:

| Deployment | Valuation layers | …carrying a journal entry |
|---|---|---|
| Series-19 estate (`E-1`) | 14,441 movements | **0** |
| Series-18 OCC (`551ab874`) | 47,801 | **0** |
| **Series-16 SWR (`45a8e08e`)** | **74,982** | **57,863 — 77.2%** |

**Two rounds of this programme reasoned about a mechanism that had never once been observed working.**
Here it works. This deployment is the **positive control** the whole valuation line of enquiry was missing:
it proves the instrument can register a link, that the source path does post, and that the two published zeros
were about configuration and policy rather than about a mechanism that does not exist.

---

## 2. WHERE THE POLICY LIVES IN THIS GENERATION

Series 16 stores company-dependent values in **`ir_property`** — **13,331 rows** in this deployment.

**The jsonb columns used in series 18 do not exist here, and `ir_property` does not exist in series 18.**
Storage location is generation-specific, and reading the wrong one produces a false zero
(`ERR-P01-19`). Both the global and per-record scopes of `ir_property` were read.

| Field | Global row | Per-record rows |
|---|---|---|
| `property_valuation` | **1 — `manual_periodic`** | **15 — `real_time`** |
| `property_cost_method` | 1 — `standard` | 18 `fifo`, 8 `average` |
| `property_stock_journal` | **1 — `account.journal,8`** | none |
| `property_stock_account_input_categ_id` | 1 — NULL | 11 → `account.account,39`; 2 → 1160; 1 → 1156; 1 → 1161; **6 explicitly NULL** |
| `property_stock_account_output_categ_id` | 1 — NULL | 6 → 1156; 2 → 1160; 2 → 1162; 1 each → 22 / 1159 / 1163; 6 NULL |
| `property_stock_valuation_account_id` | — | 9 → 1062; 2 → 1069; 1 each → 1286 / 5 / 1289 / 1067; 6 NULL |
| `property_account_creditor_price_difference_categ` | — | **1 → `account.account,1173`** |

---

## 3. A MIXED POPULATION — THE FIRST IN THIS PROGRAMME

There are **30 product categories**. The global default is `manual_periodic`; **15 categories override to
`real_time`**; the other 15 inherit periodic.

**Every prior P01 policy statement was about a uniform population** — series 18 was periodic on 126 of 126
categories across 4 of 4 companies. **This deployment is genuinely mixed, and that is what makes it
evidentially valuable**: the same database, the same code, the same period, two policies — an internal
control no cross-deployment comparison can supply.

---

## 4. THE DISCRIMINATING TEST

**Join path:** `stock_valuation_layer.product_id` → `product_product.product_tmpl_id` →
`product_template.categ_id` → policy from `ir_property`.
**COVERAGE CONTROL: 0 of 74,982 layers had an unresolvable category.**

| Effective policy | Journal entry | No journal entry |
|---|---|---|
| **`real_time`** | **56,654** | 1,044 |
| **`manual_periodic`** | 1,209 | **16,075** |

**The policy explains the overwhelming majority in both directions** — 98.2% of real_time layers post,
93.0% of periodic layers do not. That is the same causal claim the series-18 round made from a uniform
population, now demonstrated **within one database against a live counter-population**.

### 4.1 The first test I ran was wrong, and it looked right

The first attempt joined on **`stock_valuation_layer.categ_id`**. That column **does not exist in series 16** —
the table has 19 columns and `categ_id` is not among them; it belongs to a later generation. The parser padded
the missing column with nulls, every one of the 74,982 rows classified as `manual_periodic`, and the result
was internally plausible:

```
   manual_periodic  UNLINKED  17119
   manual_periodic  linked    57863
   unlinked DESPITE real_time: 0
```

A 57,863-row "positive control" sat right beside it and did not protect against it, because the failure was
not in whether rows were read but in **whether the predicate could see its input**.

**The defect is cross-generation schema assumption**: the series-18 column set was carried into a series-16
table. It is recorded as `ERR-P01-42` and it is the reason §4 states its join path and coverage control explicitly.

---

## 5. THE TWO RESIDUALS — BOTH REAL, NEITHER EXPLAINED BY POLICY

### 5.1 Residual A — 296 layers that should have posted and did not

`real_time`, **non-zero value**, no journal entry: **296**.
A further **748** real_time layers carry `value = 0.00` and are correctly skipped by the
`currency_id.is_zero(value)` guard, so they are excluded rather than counted.

### 5.2 ~~Residual B — layers that posted under a policy that should not post~~ — **EXPLAINED, NOT ANOMALOUS**

`manual_periodic` **with** a journal entry: **1,209**, across 9 product categories.

**These are not receipts and the policy gate never applied to them.** Re-derived:

| Property | Count | Share |
|---|---|---|
| **No `stock_move_id` at all** | **1,194** | **98.8%** |
| Carry a non-zero `price_diff_value` | 1,047 | 86.6% |
| Their journal entry is an `in_invoice` | 1,172 | 97.0% |

**Residual B is the vendor-bill price-difference population.** A price-difference layer is created *by the
bill*, carries no stock move, and is linked to the bill's own entry — so the valuation gate at
`_validate_accounting_entries`, which acts on layers *from stock moves*, is simply not on its path.

**Causation was reversed for 98.8% of the population.** I read "periodic category + has a journal entry"
as a policy violation without asking what the layers *were*.

### 5.3 Policy change was tested as the explanation and is NOT supported

The obvious benign explanation is that a category's policy changed after the layers were written —
`ir_property` holds current state, not history.

**Tested by time distribution.** All 15 `real_time` `ir_property` rows were written between
**2023-09-15** and **2023-12-08**. If the residuals were pre-change artefacts they would cluster before that.
They do not:

| Year | Residual A | Residual B | All layers that year |
|---|---|---|---|
| 2023 | 31 | 123 | 2,786 |
| 2024 | 126 | 471 | 35,918 |
| 2025 | 108 | 463 | 24,942 |
| 2026 | 31 | 152 | 11,336 |

**Both residuals track total volume across all four years, including two full years after the last policy
write.** Policy change does not account for them.

**CLASSIFICATION: `UNRESOLVED — EVIDENCE REQUIRED`.** `ir_property` cannot evidence its own history, so
history is not *excluded* — but it is not supported either, and these are not dismissed as artefacts.
Enumerating every writer of `stock_valuation_layer.account_move_id` in the deployed code was issued as a
disproof assignment to AAS-03 Expert 4.

---

## 6. THE CLEARING BRIDGE — CONFIGURED **AND** EXECUTED

For the first time in this programme, the goods-received clearing account is not merely configured.

**Account 39 = `2900000 Goods Receipt Note(GRN)`, `liability_current`.**

| Measure | All states *(as first published)* | **POSTED ONLY — the correct basis** |
|---|---|---|
| Journal items | 13,736 | **13,666** |
| Debits | ฿6,558,441,923.88 | ฿6,383,424,831.18 |
| Credits | ฿6,486,344,109.63 | ฿6,390,473,523.26 |
| **Net** | ~~฿72,097,814.25~~ | **−฿7,048,692.08** |

**The published ฿72,097,814.25 was an all-states figure and it is withdrawn.** On a posted-only basis
the GRN account nets to **−฿7,048,692.08** — the **opposite sign** and an order of magnitude smaller.

**70 journal items carry the entire difference**: 53 on cancelled moves (net +฿76,422,354.13) and
17 on draft moves (net +฿2,724,152.20). **One cancelled entry alone carries ฿90,351,213.15** in credit.

| State | Items | Net |
|---|---|---|
| `posted` | 13,666 | **−฿7,048,692.08** |
| `cancel` | 53 | +฿76,422,354.13 |
| `draft` | 17 | +฿2,724,152.20 |

**The same missing `parent_state` filter runs through every total in this section**, including the
6,653-line / ฿4,516,394,611.47 bill relief — of which **฿175,017,092.70 sits on cancelled or draft bills**.
Those totals are **all-states figures** and must be read as such until re-derived.

**Why this is worse than a missing control**: the AP analysis in
`P01_S16_VENDOR_ADVANCE_PAYMENT_SETTLEMENT.md §4.1` **does** split by move state, in the same package,
in the same run. **The control existed and was applied inconsistently.**

**The bridge closes**: receipts credit the GRN liability, vendor bills debit it. The residual ฿72.1M is the
uncleared position at the archive date — goods received whose bills have not yet relieved the liability.

Compare the series-18 OCC deployment, where the same account role was configured on 171 of 504
(category, company) pairs and carried **0 items**, leaving ฿30,080,689.78 of received-not-invoiced
**outside the ledger entirely**. Here the equivalent exposure is **inside** it.

*Whether ฿72.1M is a correct carrying amount, timing, or an accumulation of unmatched items is a question for
P08 and P11 — see `P01_S16_P11_HANDOFF.md`. P01 measures it; P01 does not adjudicate it.*

### 6.1 Valuation accounts are all live

| Account | Role | Items |
|---|---|---|
| 1062 `1141001` Raw material | asset_current | 22,561 |
| 1068 `1147001` Work in progress | asset_current | 39,935 |
| 1289 `1148002` Semi Product | asset_current | 10,993 |
| 1286 `1145000` Inventory ByProduct | asset_current | 4,695 |
| 1156 `4010002` Consumption of raw materials | expense_direct_cost | 3,338 |
| 1160 `4010006` Consumption of semi-finished | expense_direct_cost | 807 |

*Positive controls for the counter:* 447,384 journal items across **262 distinct accounts**; largest are
1068 (39,935), 1117 (29,042), 1083 (27,366), 33 (22,978).

### 6.2 The price-difference engine is configured and has never fired

**Account 1173 = `4310005 Purchase price variance` carries 0 journal items in 447,384 — that count stands.**

> ### ~~The price-difference engine is configured and has never fired~~ — **CONTRADICTED**
>
> **1,123 valuation layers carry a non-zero `price_diff_value`, totalling ฿2,246,313,274.64.**
> The engine fires constantly. Account 1173 is empty because **six product-level overrides** route the
> price difference to six *other* accounts — one of them named **`9999991 Dummy Service`** — and the most
> recent of those was configured **four days before this archive was taken**.
>
> **The defect was mine and it is the unmeasured-consequence class**: I measured *one account's item count*
> and published a conclusion about *the engine*. `price_diff_value` sits on the very table I had already
> parsed 74,982 rows of, and I did not look at it.

This is a stronger result than the series-18 equivalent. There, the price-difference engine could not fire
because the valuation gate was closed for every product. **Here the gate is open for 15 categories, 56,654
layers post through it, and the variance account still never receives a single item.**

**CLASSIFICATION: `CONFIGURED BUT UNEXERCISED` — and, unlike series 18, not explained by policy.**
Whether purchase price differences are genuinely always zero, are absorbed elsewhere, or are not being
computed is `UNRESOLVED — EVIDENCE REQUIRED`; disproof was assigned to AAS-03 Expert 1.

---

## 7. A 15-ORDER-OF-MAGNITUDE SUBLEDGER / LEDGER DIVERGENCE

**30 valuation layers carry `|value| > 1e12`**, reaching **±1.5 × 10²¹ THB**, with per-unit costs such as
**744,082,316,162.43** and **−352,468,555,154.38** — for milled rice. Negative unit costs are themselves invalid.
**Those two are illustrative, not extreme: the true maximum is `|unit_cost|` = ฿52,616,504,567,828,624**
(layer 27394) — the figures first published understated the peak by a factor of ~70,713.
They arise on `WH/MO/…` manufacturing and `UB/…` unbuild documents.

Excluding those 30 rows, the whole table sums to **฿400,338,755.98**.

**And the corruption is invisible in aggregate.** `SUM(value)` over all 74,982 rows — *including* the 30 —
is **฿205,490,835.88**: the extreme positives and negatives very nearly cancel. **No total, and no
balance-sheet inventory figure, will reveal this.** Only a row-level magnitude test finds it, which is why
it survived to be found in round six.

**25 of the 30 carry a journal entry and all 25 are POSTED**, dated 2024-08-17 … 2024-08-31.

### 7.1 The claim I nearly published, and what the evidence actually shows

The obvious inference — *quadrillions were posted to the general ledger* — is **false**, and it was checked
before publication. Those 25 entries carry **50 journal items that balance exactly**:

| Measure | Value |
|---|---|
| Total debits | **฿31,622,699.37** |
| Total credits | **฿31,622,699.37** |
| Raw material (1062) | +6,607,206.36 |
| Work in progress (1068) | −3,828,200.44 |
| Semi Product (1289) | −3,517,056.32 |
| Inventory ByProduct (1286) | +482,308.21 |
| GRN (39) | +255,742.20 |

**The general ledger is intact and sane. The inventory subledger is not.**

> **FACT VERIFIED: on these 30 rows the inventory subledger and the general ledger disagree by roughly
> fifteen orders of magnitude.** The GL says ฿31.6M moved; `stock_valuation_layer` says up to ±1.5 × 10²¹.

Any inventory valuation report, stock-ageing or cost analysis reading the subledger returns a figure
unrelated to the ledger. Any reconciliation between them fails by construction.

**CLASSIFICATION: `FACT VERIFIED` as to the divergence. Root cause `UNRESOLVED — EVIDENCE REQUIRED`** —
the shape (negative unit costs on manufacturing and unbuild documents) is consistent with a cost computation
over a near-zero or negative quantity, but that is `SUPPORTED INTERPRETATION`, not fact, and the manufacturing
cost path belongs to peer process **P03**. Routed there and to **P08**; P01 does not adjudicate it.

---

## 8. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| Valuation → GL path executes in this generation | **FACT VERIFIED** — 57,863 of 74,982 |
| Policy is a genuine mixed population, 15 real_time / 15 periodic of 30 categories | **FACT VERIFIED**, both `ir_property` scopes read |
| Policy explains the linkage split | **FACT VERIFIED** — 98.2% / 93.0%, coverage control 0 unresolved |
| 296 real_time non-zero layers unposted | **UNRESOLVED — EVIDENCE REQUIRED** |
| 1,209 periodic layers posted, 9 categories | **UNRESOLVED — EVIDENCE REQUIRED** |
| Policy change as the residual explanation | **CONTRADICTED** by time distribution |
| GRNI clearing account configured **and** executed | **FACT VERIFIED** — 13,736 items, net ฿72,097,814.25 |
| Vendor bills relieve the GRNI liability | **FACT VERIFIED** — 6,653 lines, ฿4,516,394,611.47 Dr |
| Purchase price variance account never used | **FACT VERIFIED**, with positive controls; cause **UNRESOLVED** |
| 30 layers diverge from the GL by ~10¹⁵ | **FACT VERIFIED**; root cause **UNRESOLVED**, routed to P03/P08 |
| GL corrupted by the extreme values | **CONTRADICTED** — the 25 posted entries balance at ฿31,622,699.37 |
