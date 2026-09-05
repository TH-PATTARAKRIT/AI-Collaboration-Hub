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
| S16-C-04 | Goods-received clearing account carries the receipt-side liability | account 39, **13,736 items**, net ฿72,097,814.25 | **ACTIVE AND EXERCISED** |
| S16-C-05 | Vendor bill relieves the clearing account | **6,653** bill lines, Dr ฿4,516,394,611.47 | **ACTIVE AND EXERCISED** |
| S16-C-06 | Stock journal receives valuation entries | `property_stock_journal` global → `account.journal,8`; valuation accounts carry 22,561 / 39,935 / 10,993 / 4,695 items | **ACTIVE AND EXERCISED** |
| S16-C-07 | Price-difference posting to the creditor price-difference account | account 1173 `4310005 Purchase price variance` **configured**, **0 items of 447,384** | **CONFIGURED BUT UNEXERCISED** |
| S16-C-08 | Landed-cost allocation onto valuation layers (`stock_valuation_layer.stock_landed_cost_id` exists) | `stock_landed_cost` table: **0 rows**; module installed at 16.0.1.1 | **ACTIVE BUT UNEXERCISED** |
| S16-C-09 | Anglo-saxon COGS lines at invoice | `anglo_saxon_accounting = FALSE` on the only company | **CONFIGURED OFF — NOT REACHABLE** |
| S16-C-10 | Period-lock enforcement / silent re-dating | all three lock dates NULL | **NOT REACHABLE — NO LOCK CONFIGURED** |
| S16-C-11 | Immutable reversal via `reversed_entry_id` | **5,115** pairs, 0 unresolvable originals | **ACTIVE AND EXERCISED** |
| S16-C-12 | Thai withholding certificate generation | **5,201** certs, 5,191 done; `account_payment.wt_tax_id` present | **ACTIVE AND EXERCISED** |
| S16-C-13 | `om_data_remove` deletion capability (peer P06: deletes ledger data) | installed at 16.0.1.0.1 | **NOT DETERMINABLE — under challenge** |
| **S16-C-14** | **Valuation value and its journal entry represent the same economic event** | **30 layers up to ±1.5e21 against balanced GL entries totalling ฿31,622,699.37** | **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** |
| **S16-C-15** | **Policy gate is the sole determinant of whether a layer posts** | **296** real_time non-zero layers unposted; **1,209** periodic layers posted across 9 categories; time distribution refutes policy change | **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** |
| S16-C-16 | A vendor bill always carries a payable line | 37,054 payable items against 37,055 bills | **NOT DETERMINABLE — single-row anomaly, unprobed** |
| S16-C-17 | Every journal item resolves to an account type | **67** vendor-bill items with none | **NOT DETERMINABLE — unprobed** |
| S16-C-18 | Accounting dates are Gregorian | **30** posted moves dated year 2567, 1 `invoice_date` 2568 | **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** |

---

## SUMMARY

| Classification | Count |
|---|---|
| ACTIVE AND EXERCISED | **8** |
| CONFIGURED BUT UNEXERCISED | 1 |
| ACTIVE BUT UNEXERCISED | 1 |
| NOT REACHABLE (configuration off / absent) | 2 |
| **DATABASE EVIDENCE CONTRADICTS SOURCE EXPECTATION** | **3** |
| NOT DETERMINABLE | 3 |
| **Total** | **18** |

**Eight mechanisms are observed working.** That is the largest set of positively-confirmed accounting
mechanisms in P01's history, and it comes from the deployment the package spent four rounds unable to read.

**Three contradictions are open** — S16-C-14, S16-C-15 and S16-C-18. None is closed by this round.
