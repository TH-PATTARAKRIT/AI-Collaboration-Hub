# P01 — SERIES-16 PROCURE-TO-PAY BUSINESS PROCESS / ACCOUNTING MAP

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-10`
Deployment `45a8e08e` (`iSMEs`, `swr.smeplus.asia`), **1 company — a rice miller**, 183,590 journal entries.

**Reconstructed from evidence only.** Every step names its operational object, its accounting event, its GL
effect and the status of the evidence. Scope is `COMPANY` throughout — this deployment has one company, so no
tenant or platform scope question arises here and none is asserted.

---

## THE CHAIN

| # | Business fact | Operational object | Accounting event | GL / financial effect | Evidence status |
|---|---|---|---|---|---|
| 1 | A need is raised and approved | `purchase_request` — **2,163**, **2,147 approved**, 5 rejected | **none** | none | **FACT VERIFIED**; source is outside the core trees, located via the host index |
| 2 | An order is placed | `purchase_order` — **5,881**, 5,756 confirmed | **none** | none | **FACT VERIFIED** — no journal entry references a purchase order |
| 3 | Goods arrive | `stock_picking` — **20,098**, **18,218 done** | valuation layer created | none yet | **FACT VERIFIED** |
| 4 | Inventory is valued | `stock_valuation_layer` — **74,982** | **posts for `real_time` categories only** | Dr inventory / Cr GRN | **FACT VERIFIED** — 56,654 of 57,698 real_time layers post |
| 5 | …and does not, for periodic categories | 17,284 periodic layers | **suppressed by design** | none | **FACT VERIFIED** — 16,075 unposted |
| 6 | The obligation is carried between receipt and bill | account **39 `2900000 Goods Receipt Note(GRN)`**, `liability_current` | **13,736 items** | Cr ฿6,486,344,109.63 / Dr ฿6,558,441,923.88 → **net ฿72,097,814.25** | **FACT VERIFIED** |
| 7 | The vendor bills | `account_move` `in_invoice` — **37,055** (36,867 posted) | expense/asset + payable, **and relief of the GRN liability** | **6,653 bill lines Dr ฿4,516,394,611.47** to account 39 | **FACT VERIFIED** |
| 8 | The liability is recognised | payable items — **37,054** | — | AP | **FACT VERIFIED**; one bill carries no payable line |
| 9 | Payment is made | `account_payment` — **19,575 supplier** | — | cash / bank | **FACT VERIFIED** |
| 10 | Tax is withheld on some payments | **4,941 (25.24%)** carry `wt_tax_id`; **5,201** certificates, pnd53 4,437 / pnd3 751 / pnd1 13 | certificate raised | withholding | **FACT VERIFIED** as behaviour; **statutory correctness → P07** |
| 11 | Items are matched off | `account_partial_reconcile` / `account_full_reconcile` | reconciliation | AP settlement | **NOT MEASURED this round** |
| 12 | Errors are corrected | **5,115** moves carry `reversed_entry_id`; 1,866 cancelled | **immutable reversal** | reversing entry | **FACT VERIFIED** |
| 13 | Periods close | **no lock date of any kind is configured** | — | — | **FACT VERIFIED — NO CONTROL EXISTS** |

---

## WHAT THIS CHAIN GETS RIGHT

Steps 4, 6 and 7 are the receipt→valuation→clearing→bill bridge that P01 traced in source for four rounds and
had never observed operating. **Here it operates**: inventory is valued at receipt, the obligation is carried in
a named reconcilable liability account, and the vendor bill relieves it. **Eight distinct accounting mechanisms
are confirmed working** (`P01_S16_SOURCE_DB_CONTRADICTION_REGISTER.md`).

## WHERE IT BREAKS, AND HOW BADLY

| Break | Magnitude | Owner |
|---|---|---|
| **Subledger and ledger disagree by ~10¹⁵** on 30 valuation layers (up to ±1.5e21 against balanced GL entries of ฿31,622,699.37) | 30 of 74,982 rows; distorts any inventory valuation report | **P03** (manufacturing cost path) and **P08** |
| **296** real_time non-zero layers never posted; **1,209** periodic layers posted anyway | policy-change explanation **refuted** by time distribution | P01 — open |
| **Purchase price variance account configured, 0 items in 447,384** — and here the valuation gate is *open* | cause unknown | P01 — open |
| **No period lock of any kind**, with 169,143 posted entries | no control | **P08** |
| **5,601 of 36,865 posted bills (15.19%)** dated **earlier** than their own invoice date; 2,037 (5.53%) in a different month | cut-off | **P08** |
| **30 posted moves dated year 2567** (BE), 1 `invoice_date` 2568 | invisible to every period query | **P08** |
| **1,407 of 5,201 withholding certificates** carry no payment link | 27.05% | **P07**, **P11** |
| Landed costs **installed and never used** — 0 rows | latent | P01 — noted |
| Receipt→bill identity is **document text, not a foreign key** | structural | **P11** |

---

## THE SHAPE OF THIS BUSINESS, WHICH GOVERNS EVERY RATIO ABOVE

**37,055 vendor bills against 5,881 purchase orders — a 6:1 ratio.** Most purchasing in this deployment does
not pass through a purchase order at all.

Consequences that must travel with every figure in this package:
- The three-way-match position (**79 lines received-not-invoiced, ฿12,678,776.50**) is measured on PO lines and
  therefore describes **a minority of purchasing**. It is not a whole-business control statistic.
- The GRN residual (**฿72,097,814.25**) is an order of magnitude larger than that PO-line position, which is
  consistent with the same asymmetry but **is not explained by this package**.
- Comparisons with the series-18 OCC deployment (4 companies, 1,904 bills, 13,887 orders — the inverse ratio)
  are comparisons between **different businesses**, not between generations alone.

---

## SCOPE

`SCOPE = COMPANY` for every row above. One company, `anglo_saxon_accounting = FALSE`, all three lock dates
NULL. No `PLATFORM` or `TENANT` scope claim is made, and none of the multi-company ownership findings from the
series-18 and series-19 deployments is asserted here — **they were measured in populations this deployment does
not share.**
