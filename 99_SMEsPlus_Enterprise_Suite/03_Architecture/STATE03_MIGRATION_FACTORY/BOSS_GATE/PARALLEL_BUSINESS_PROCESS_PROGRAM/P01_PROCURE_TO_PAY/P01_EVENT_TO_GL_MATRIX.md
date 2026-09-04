# P01 — EVENT TO GENERAL LEDGER MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Account names below are **role names**, not chart-of-account codes. They describe what the
account does in the pattern, not what any particular company calls it.

Legend for the Source column: `SRC` = read from reference source; `INF` = inferred from the
composition of two or more verified mechanisms and **not** independently confirmed.

---

## 1. STORABLE ITEM, CONTINUOUS VALUATION, CLEARING MODEL ON

| # | Event | Debit | Credit | Date used | Source |
|---|---|---|---|---|---|
| 1 | Order approved | — | — | — | SRC `EV-P01-01` |
| 2 | Goods received | Inventory Valuation | Goods-Received Clearing | **Context override, else linked-bill-line date, else system today** `EV-P01-06` | SRC |
| 3 | Vendor bill posted | Goods-Received Clearing | Accounts Payable | Bill date | SRC `EV-P01-09` |
| 3a | …plus tax | Recoverable Purchase Tax | Accounts Payable | Bill date | UNRESOLVED |
| 4 | Clearing matched | (reconciliation, no new amounts) | | | SRC `EV-P01-10` — **conditional on the clearing account being flagged reconcilable** |
| 5 | Price difference, goods still on hand | Inventory Valuation (layer correction) | — | Bill date | SRC `EV-P01-15` |
| 6 | Price difference, goods already consumed | Item Expense | Goods-Received Clearing | Bill date | SRC `EV-P01-14` |
| 6x | …**where the item has no expense account** | **nothing is posted** | | | SRC `EV-P01-14` |
| 7 | Payment | Accounts Payable | Outstanding Payments | Payment date | SRC `EV-P01-20` |
| 7x | …**where no outstanding account is configured** | **no entry at all** | | | SRC `EV-P01-20` |
| 8 | Bank statement matched | Outstanding Payments | Bank | Statement date | SRC |
| 9 | FX difference | Exchange Loss *or* Exchange Gain | Accounts Payable | Settlement date | SRC `EV-P01-21` |

## 2. STORABLE ITEM, PERIODIC VALUATION

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Goods received | — **no journal entry**; a valuation layer is written but not posted | | SRC `EV-P01-05` |
| 2 | Vendor bill posted | Item Expense | Accounts Payable | SRC |
| 3 | Price difference | **none — the mechanism is gated on continuous valuation** | | SRC `EV-P01-15` |

The whole clearing / three-way bridge disappears. Inventory value and ledger value are
reconciled only by a periodic manual procedure, which was **not searched in this session
(class C)**.

## 3. CONSUMABLE ITEM

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Goods received | — **no valuation layer and no journal entry** | | SRC `EV-P01-04` |
| 2 | Vendor bill posted | Item Expense | Accounts Payable | SRC |

## 4. SERVICE PURCHASE

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Service rendered | **no document, no event** | | INF — see `BE-P01-05`, class B |
| 2 | Vendor bill posted | Item Expense | Accounts Payable | SRC |

## 5. ASSET PURCHASE

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Vendor bill posted, line account carries the asset flag | Asset (per the line's ledger account) | Accounts Payable | SRC `EV-P01-18` |
| 2 | Asset record auto-created at posting, with elevated privilege | (no additional amounts) | | SRC `EV-P01-18` |
| 3 | Bill reset to draft | **still-draft assets are deleted** | | SRC `EV-P01-19` |
| ⚠ | **If the item is also storable and continuously valued, the line's account has already been replaced by the clearing account before the asset rule reads it** | | | INF — `CONTRA-P01-04`, runtime evidence required |

## 6. ORDER-STAGE ACCRUAL (parallel path)

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Accrual raised from an order | Item Expense (per line) | Accrual Liability (single globalised counterpart) | SRC `EV-P01-16` |
| 2 | Automatic reversal at the stated reversal date | Accrual Liability | Item Expense | SRC `EV-P01-16` |
| ⚠ | **No back-link and no note is written to the order** | | | SRC `EV-P01-17` |

## 7. RETURN TO VENDOR

| # | Event | Debit | Credit | Source |
|---|---|---|---|---|
| 1 | Goods returned (storable, continuous) | Goods-Received Clearing | Inventory Valuation | SRC |
| 2 | Vendor credit note | Accounts Payable | Goods-Received Clearing | UNRESOLVED — assigned to Functional Design expert |

---

## 8. WHAT THE MATRIX SHOWS

1. **Five different ledger patterns hide behind one document set.** The pattern is chosen by
   item and company configuration, never by the business event.
2. **The bill is the only universal accounting event in P01** — class **B**, bounded by the
   journal-entry creation-site population, which is declared a floor and not a total. Every
   upstream effect found is conditional.
3. **Three silent-drop paths exist**: no expense account → price difference vanishes; no
   outstanding account → payment entry vanishes; clearing account not flagged reconcilable →
   the bridge never closes and nothing complains.
4. **The receipt entry's date is not the receipt's date.**
5. **One correction path deletes rather than reverses.**

Items 3, 4 and 5 are the P01 findings that a clean-room design must consciously reject rather
than inherit.

---

## 9. NOT COVERED BY THIS MATRIX

Tax (`AE-P01-17`), withholding (`AE-P01-18`), landed cost (`AE-P01-19`), advance payments and
down payments (`BE-P01-14`), subcontract purchase, and intercompany purchase. Each is
**class C — not yet searched by this document**; several were assigned to experts and are
reported in `P01_AAS03_EXPERT_CHALLENGE.md`. An empty cell in this matrix means unsearched,
never absent.
