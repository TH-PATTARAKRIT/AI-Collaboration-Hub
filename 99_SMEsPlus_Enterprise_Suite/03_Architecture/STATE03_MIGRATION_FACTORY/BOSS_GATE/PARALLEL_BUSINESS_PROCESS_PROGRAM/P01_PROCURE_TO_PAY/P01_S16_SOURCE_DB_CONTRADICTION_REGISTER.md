# P01 — SERIES-16 SOURCE ↔ DATABASE CONTRADICTION REGISTER

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-09` · Deployment `45a8e08e` · Source: E-ENT `odoo-16.0+e.20230401` (144/144 version-matched)

Classification vocabulary is the prompt's: ACTIVE AND EXERCISED · ACTIVE BUT UNEXERCISED ·
CONFIGURED BUT UNEXERCISED · SOURCE PRESENT / MODULE NOT INSTALLED ·
DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION · NOT DETERMINABLE.

---

| # | Source mechanism | Deployment evidence | Classification |
|---|---|---|---|
| S16-C-01 | Valuation layer → journal entry, gated on `product.valuation == 'real_time'` | 56,654 of 57,698 real_time layers post | **ACTIVE AND EXERCISED** |
| S16-C-02 | Same gate suppresses posting under `manual_periodic` | 16,075 of 17,284 periodic layers do not post | **ACTIVE AND EXERCISED** |
| S16-C-03 | Zero-value guard `currency_id.is_zero(value)` skips a layer | 748 real_time layers at value 0.00, unposted | **ACTIVE AND EXERCISED** |
| S16-C-04 | Goods-received clearing account carries the receipt-side liability | account 39, **13,666 posted items, net −฿7,048,692.08** (the published ฿72,097,814.25 was all-states and is withdrawn) | **ACTIVE AND EXERCISED** |
| S16-C-05 | Vendor bill relieves the clearing account | **6,653** bill lines, Dr ฿4,516,394,611.47 — **all-states; ฿175,017,092.70 of it on cancelled/draft bills** | **ACTIVE AND EXERCISED** |
| S16-C-06 | Stock journal receives valuation entries | `property_stock_journal` global → `account.journal,8`; valuation accounts carry 22,561 / 39,935 / 10,993 / 4,695 items | **ACTIVE AND EXERCISED** |
| S16-C-07 | Price-difference posting to the creditor price-difference account | account 1173 carries 0 items — **but 1,123 layers carry ฿2,246,313,274.64 of `price_diff_value`, routed to six other accounts by product-level overrides, one named `9999991 Dummy Service`** | **~~CONFIGURED BUT UNEXERCISED~~ → ACTIVE AND EXERCISED, posting to an unenumerated account set** |
| S16-C-08 | Landed-cost allocation onto valuation layers (`stock_valuation_layer.stock_landed_cost_id` exists) | `stock_landed_cost` table: **0 rows**; module installed at 16.0.1.1 | **ACTIVE BUT UNEXERCISED** |
| S16-C-09 | Anglo-saxon COGS lines at invoice | `anglo_saxon_accounting = FALSE` on the only company | **CONFIGURED OFF — NOT REACHABLE** |
| S16-C-10 | Period-lock enforcement / silent re-dating | all three lock dates NULL | **NOT REACHABLE — NO LOCK CONFIGURED** |
| S16-C-11 | Immutable reversal via `reversed_entry_id` | **5,115** pairs, 0 unresolvable originals | **ACTIVE AND EXERCISED** |
| S16-C-12 | Thai withholding certificate generation | **5,201** certs, 5,191 done; `account_payment.wt_tax_id` present | **ACTIVE AND EXERCISED** |
| S16-C-13 | `om_data_remove` deletion capability (peer P06: deletes ledger data) | installed at 16.0.1.0.1 | **NOT DETERMINABLE — under challenge** |
| **S16-C-14** | **Valuation value and its journal entry represent the same economic event** | **30 layers up to ±1.5e21 against balanced GL entries totalling ฿31,622,699.37** | **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** |
| **S16-C-15** | **Policy gate is the sole determinant of whether a layer posts** | **296** real_time non-zero layers unposted — **still open**. The 1,209 periodic-posted layers are **CLOSED**: 1,194 (98.8%) have **no stock move** and 1,047 carry `price_diff_value` — they are bill-created price-difference layers the gate never governed | **NARROWED — half closed, 296 remain** |
| S16-C-16 | A vendor bill always carries a payable line | 37,054 payable items against 37,055 bills | **NOT DETERMINABLE — single-row anomaly, unprobed** |
| S16-C-17 | Every journal item resolves to an account type | **67** vendor-bill items with none | **NOT DETERMINABLE — unprobed** |
| S16-C-18 | Accounting dates are Gregorian | **484 Buddhist-era values across 14 columns in 11 tables** (not 30 in one), plus **11 values at year 8202**, an undiagnosed second class. **Bidirectional**: 30 moves have a BE `date` with a good `tax_period`, 7 the reverse. **No column is reliably Gregorian.** | **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION — far wider than published** |

---

## SUMMARY

| Classification | Count |
|---|---|
| ACTIVE AND EXERCISED | **9** |
| CONFIGURED BUT UNEXERCISED | **0** |
| ACTIVE BUT UNEXERCISED | 1 |
| NOT REACHABLE (configuration off / absent) | 2 |
| **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** | **2** |
| NARROWED (half closed) | 1 |
| NOT DETERMINABLE | 3 |
| **Total** | **18** |

**Eight mechanisms are observed working.** That is the largest set of positively-confirmed accounting
mechanisms in P01's history, and it comes from the deployment the package spent four rounds unable to read.

**Two contradictions stand and one is half-closed**, after AAS-03 Expert 2's challenge was verified and adopted:

- **S16-C-14** (subledger/ledger divergence) **stands and is sharper**: the divergence is
  **฿6,462,975,089,678,637.13**, the corruption is entirely in `unit_cost` (`value = quantity × unit_cost`
  to ~1 ULP), and it is **invisible in aggregate** — `SUM(value)` over all 74,982 rows is ฿205,490,835.88.
- **S16-C-15** is **half closed**: 1,209 of the 1,505 residual layers are explained as bill-created
  price-difference layers. **296 remain.**
- **S16-C-18** stands and is **16× wider** than published.

**One published classification was overturned outright**: S16-C-07 moves from `CONFIGURED BUT UNEXERCISED`
to `ACTIVE AND EXERCISED`. The programme's "configured but unexercised" count for this deployment is **zero**.
