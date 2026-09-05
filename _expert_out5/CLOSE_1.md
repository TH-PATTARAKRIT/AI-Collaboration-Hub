# CLOSE_1 — AAS-03 EXPERT 1 (Leader Functional Design) — TARGETED CHALLENGE TO C-1

**VERDICT: C-1 CHALLENGED.** Material Delta exists and is measurable from evidence already on disk. A further
P01 sweep IS justified — but a *narrow, named* one, not another whole-estate round.

Baseline read: `brief/CLOSURE.md`, `brief/FINDINGS.md`. All figures below executed this run against
`s16/T_*.sql` via `s16/stream.py`. No writes, no installs.

---

## THE CASE AGAINST C-1 — ONE SENTENCE
Six rounds established **what the GRNI account is**; not one round established **what is in it**. Decomposed
by originating business transaction, the published headline **13,666 posted items / −฿7,048,692.08** on
account 39 is a mixture of six sources, and **only 45% of its gross movement is purchase-order driven.**

## D-1 THE DECOMPOSITION THE PACKAGE NEVER RAN (coverage control exact)
Posted `account_move_line` on `account_id=39`, classified by origin
(bill w/ `purchase_line_id` → PO bill; bill w/o → non-PO; else joined via
`stock_valuation_layer.account_move_id` → `stock_move` class; else UNCLASSIFIED):

| ORIGIN CLASS | items | net THB |
|---|---:|---:|
| `in_invoice` **PO-linked** | 6,297 | 4,071,687,860.09 |
| stock: receipt (picking type 1) | 5,306 | −3,395,870,854.60 |
| **UNCLASSIFIED manual `entry`** | **51** | **−1,742,591,244.82** |
| stock: picking type 2 = `WH/OUT/…` outgoing | 665 | 708,164,653.64 |
| `in_invoice` **non-PO** | 298 | 269,689,658.68 |
| stock: return move | 112 | 98,319,140.75 |
| **stock: inventory adjustment** | **716** | **−68,436,934.23** |
| stock: picking type 3 (PRODUCTION IN PROCESS) | 8 | 45,054,545.50 |
| stock: SVL whose `stock_move` is **not `done`** | 182 | 17,891,023.03 |
| `in_refund` PO / non-PO / type 5 | 31 | −10,956,540.12 |
| **TOTAL (coverage control)** | **13,666** | **−7,048,692.08** |

**Positive control:** the total reproduces C-2's published 13,666 / −฿7,048,692.08 **to the digit**, with zero
residual outside the named classes. The decomposition is therefore complete over the published population, not
a sample. **SUPPORTED.**

## D-2 ฿1.74 BILLION OF MANUAL RECLASSIFICATION — THE SINGLE LARGEST ITEM, UNMENTIONED
The 51 UNCLASSIFIED items are **28 posted journal entries**, 38 items in journal 3 `MISC` and 13 in journal 8
`STJ`, with no vendor bill, no purchase order and no valuation layer. Their own `ref` text (operator-written,
Thai) is the evidence:

- `DEPRE2024010058` 2024-01-31 **−฿192,100,097.69** — *"ปรับปรุงบัญชี 2900000 Goods Receipt Note(GRN) WH/N
  เดือน 1/2024 **เนื่องจากผูกผังบัญชีผิด**"* → "adjusting account 2900000 GRN for month 1/2024 **because the
  chart-of-accounts mapping was wrong**". The same wording recurs on 2023-10, 2023-11, 2023-12, 2024-02, 2024-03.
- `DEPRE2023090003` 2023-09-30 **−฿274,297,054.03** — opening-balance restatement for FY2566.
- `DEPRE2024020038` **−฿259,411,100.50** and `DEPRE2024010057` **−฿255,957,446.40** — reclassifications of
  `4010008 Consumption of finished goods rice`, again *เนื่องจากผูกผังบัญชีผิด*.

**Why this is Material Delta, not a re-audit of settled ground:** S16-03 recorded that `ir_property` "records
current state, not history — so history cannot be excluded" and C-3 withdrew the refutation on exactly that
basis. These 28 entries are the **dated, valued, operator-attested trace of the account-mapping history that
`ir_property` cannot show**, and they were sitting in an already-extracted table for six rounds. They do not
overturn a published finding; they **make an open question answerable**. **SUPPORTED / EVIDENCE NEEDED NEXT.**

## D-3 SCRAP AND INVENTORY ADJUSTMENT POST INTO THE PURCHASE CLEARING ACCOUNT — MECHANISM PROVEN
`stock_account/models/stock_move.py:380-384`:
```
def _get_src_account(self, accounts_data):
    return self.location_id.valuation_out_account_id.id or accounts_data['stock_input'].id
def _get_dest_account(self, accounts_data):
    return self.location_dest_id.valuation_in_account_id.id or accounts_data['stock_output'].id
```
`stock_location`: id **14 `Virtual Locations/Inventory adjustment`** and id **16 `Virtual Locations/Scrap`**
both carry `valuation_in_account_id = NULL` **and** `valuation_out_account_id = NULL`.
*Positive control on the extraction:* id **15 `Virtual Locations/Production` carries 1068 / 1068** — the
column is populated where configured, so the nulls are configuration, not a parse failure.

Consequence, measured on `state='done'` moves:

| business state | done moves | SVL | SVL w/ journal entry | GL effect |
|---|---:|---:|---:|---|
| inventory adjustment | 3,010 | 2,993 | 2,818 | **Cr GRNI 39 ฿68,436,934.23**; Dr/Cr 1062, 1069, 1156, 1160, 1286, 1289 |
| scrap | 2,291 | 2,291 | 2,257 | Cr 1062 `Raw material` ฿1,032,471.56 / **Dr 1156 `4010002 Consumption of raw materials packaging`** |
| return move | 477 | **287** | 256 | Dr GRNI 39 ฿98,319,140.75 |
| `Returns` operation type 6 (incoming) | 177 | 174 | 167 | Dr 1069 ฿114,489,440.29 / Cr 1162 ฿78,089,209.70 |
| PO return (`origin_returned_move_id` + `purchase_line_id`) | — | 84 | 84 | Dr 39 ฿128,635,133.34 / Cr 1062 ฿128,734,632.09 |

Two accounting conclusions the six rounds could not have reached:
1. **The GRNI control account is not a purchase control account.** ฿68.4m of it is inventory adjustment and
   ฿708.2m is `WH/OUT/…` outgoing movement. C-2's "a swept suspense account, not an item-matched bridge" is
   correct but understates it: it is **swept by non-purchase traffic**, so no GRNI ageing, cut-off or
   three-way-match assertion can be built on it as designed. **CHALLENGED (C-2 scope, not C-2 truth).**
2. **There is no inventory-loss account.** 2,257 scrap entries expense to `4010002 Consumption of raw
   materials packaging` / `4010007`, i.e. **scrap is indistinguishable from normal consumption in the P&L**,
   and rice raw material (1062) is being expensed to a *packaging* consumption line. **SUPPORTED.**
3. **190 of 477 done return moves produced no valuation layer at all** (477 moves → 287 SVL). Returns are
   partially outside the valuation subledger. **RISKY — cause not established this run.**

## D-4 NON-PO PURCHASING — 73.21%, AND IT REACHES GRNI
Posted `in_invoice` moves = **36,867**; **9,878 PO-linked / 26,989 non-PO = 73.21% non-PO by count.**
(Unit = one vendor bill; a bill is PO-linked if **any** of its lines carries `purchase_line_id`.)

**298 non-PO bill lines debit GRNI account 39 for ฿269,689,658.68.** These bills have no purchase-order line,
therefore no receipt to match, therefore `purchase_stock::_get_price_unit` and the whole price-difference
correction path **cannot execute on them by construction** — they are not "the engine did not fire", they are
outside the engine's domain. The C-5 population (1,267 / 1,123 of 74,982 layers) and the C-4 inverted-exposure
conclusion are both scoped to the PO path and are **silent on 73% of vendor bills by count**. That silence is
not a defect in C-4/C-5; it is an **undeclared scope boundary** on their conclusions.
**MISSING (scope declaration), EVIDENCE NEEDED NEXT.**

## D-5 WHERE THE CASE FOR A SWEEP FAILS — REPORTED AS FOUND
I could not make the Material Delta case on two of the states I was asked to press:

- **Advances / prepayments: NOT material.** Supplier `account_payment` posted, non-internal, unreconciled =
  **9 payments, −฿1,534,955.07** (against 14,258 posted-reconciled, −฿4,713,485,002.86). There is no unapplied
  vendor-advance population worth a round. **SUPPORTED (negative).**
- **Returns do not currently drive the cost-explosion condition.** A `to_refund` return decrements
  `qty_received`, which is the entry condition `qty_invoiced > qty_received` in C-2. Measured: **76 PO lines
  carry a done `to_refund='t'` return move; 49 PO lines satisfy `qty_invoiced > qty_received`; the
  intersection is 0.** The return→explosion path is **latent, not live**. What *is* live: **18 of those 49
  lines have `qty_received = 0.000000`** — the exact zero-denominator subset for the missing `remaining_qty`
  zero-guard, at unit prices up to ฿3,271,028.04. That sharpens C-2's "conditions live" from 49 to a named
  18-line firing set. **SUPPORTED.**

## WHAT CONVINCED ME, AND WHAT DID NOT
What did **not** convince me that broad research must continue: the six rounds' *source* work is sound and I
found nothing suggesting another whole-estate sweep would repay itself. C-1's direction is right.

What convinced me C-1 is **premature as written**: every finding above came from tables **already extracted**,
by asking one question the package never asked — *what business transaction created this row?* C-9 concedes
"41 of 651 tables (6.3%), no stated selection rule" bounds every negative; D-1 shows the extracted 6.3% was
itself not exhausted. **Stopping is defensible; stopping while the largest single item in your own headline
account is unclassified is not.**

## EVIDENCE NEEDED NEXT (narrow, named, ~1 round, no new extraction for items 1–4)
1. Read the 28 `MISC`/`STJ` reclassification entries in full (both legs) — resolve the account-mapping history
   `ir_property` cannot show. Closes the C-3 "policy change" and S16-03 residual questions.
2. Classify **all 262 accounts** the way D-1 classified account 39; the same contamination is likely on 1062,
   1069, 1156, 1160, 1162, 1286, 1289.
3. Establish the **non-PO bill accounting path** end to end (26,989 bills): which of them should have been PO,
   and what governs the 298 that reach GRNI.
4. Explain the **190 done return moves with no valuation layer**, and the **182 GRNI items whose SVL points at
   a non-`done` stock move**.
5. Configuration ruling (owner: functional design, not research): locations 14 and 16 need
   `valuation_in/out_account_id`, and a scrap/inventory-loss account must exist. This is a **design decision**,
   not a research gap — it is mine to raise, and Boss's to settle.

**Nothing above overturns a published C-2..C-8 finding. Every item is additive.**
