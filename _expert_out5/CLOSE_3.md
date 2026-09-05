# CLOSE_3 — AAS-03 Expert 3 (Lead Integration & Localization)
## TARGETED CHALLENGE: the P01 → P08/P11 price-difference handoff sentence

**Scope.** One sentence only, C-4 last paragraph:
> "purchase price differences are **capitalised into inventory** and **no purchase-price-variance line
> reaches the P&L** in the observed path."

Read-only. No statutory statement is made anywhere below. No PASS/FAIL.

**Headline: CHALLENGED — the sentence is overstated in three independent ways and falsified in one.**

---

## 0. EVIDENCE BASE AND COVERAGE (declared, not described)

| Artefact | Rows parsed | Malformed | Coverage |
|---|---|---|---|
| `T_stock_valuation_layer.sql` | 74,982 | 0 | 74,982 / 74,982 |
| `T_account_move.sql` | 183,590 | 0 | all; 772 / 772 wanted ids resolved |
| `T_account_move_line.sql` | 447,384 | 0 | full scan |
| `T_account_account.sql` / `T_account_journal.sql` / `T_ir_property.sql` / `T_product_category.sql` | 339 / — / — / 30 | 0 | full |

Scripts executed (retained): `/tmp/e3_svl.py`, `/tmp/e3_b.py`…`/tmp/e3_k.py`.
Source read: `s16/src/stock_account/models/account_move.py`, `s16/src/stock_account/models/stock_move.py`,
`s16/src/stock_account/models/stock_valuation_layer.py`.

**Inherited limit that binds every negative below:** `GAP-P01-07` — 41 of 651 tables. I add no new tables.

---

## 1. "CAPITALISED INTO INVENTORY" — **CHALLENGED (materially wrong for 92.7% of the population)**

### 1.1 The mechanism (source, executed against data)

`stock_account/models/account_move.py:371-396 _prepare_in_invoice_svl_vals` sets
`common_svl_vals['account_move_id'] = self.move_id.id` — **the vendor bill**. The correction layer is born
pointing at the bill, with `quantity=0, unit_cost=0`, carrying only `value` and `price_diff_value`.

`_post` (line 67) then calls `stock_valuation_layer._validate_accounting_entries()`
(`stock_valuation_layer.py:43-56`), which **skips any layer whose product is not `real_time`**. Only when it
does *not* skip does `stock_move._prepare_account_move_vals` (`stock_move.py:517-527`) write
`'stock_valuation_layer_ids': [(6, None, [svl_id])]`, and because
`account_move.stock_valuation_layer_ids` is `One2many('stock.valuation.layer', 'account_move_id')`
(`account_move.py:12`) that write **overwrites `svl.account_move_id` with the valuation entry**.

**So `svl.account_move_id` is a decisive discriminator: still-the-bill = no GL entry was ever made;
STJ entry = one was.** This is directly observable, and it is *not* confusable with the C-7 deletion
alternative — `ON DELETE SET NULL` would leave the column **NULL**, not pointing at a live posted bill.

### 1.2 Measured

```
price_diff_value IS NOT NULL                      1,267   (reproduces C-5)
price_diff_value non-zero                         1,123   (reproduces C-5)
distinct account_move_id                            772   (fan-in up to 19; 0 shared with non-pd layers)
  → journal AP  'Vendor Bills'   680 moves  →  1,175 layers   NO GL ENTRY
  → journal STJ 'Inventory Val.'  92 moves  →     92 layers   GL ENTRY EXISTS
all 772 moves: state = posted
```

**Only 92 of 1,267 price-difference layers (7.3%) moved a general-ledger balance at all.**
For the other **1,175 (92.7%)** the amount exists solely in the `stock.valuation.layer` sub-ledger
(and in the parent layer's `remaining_value`, bumped in-Python at `account_move.py:390`). Nothing is
capitalised into an inventory **GL** account, because those products are `manual_periodic` and the stock
sub-system posts nothing for them at all.

Root cause confirmed by joining the layers' products to the effective valuation policy
(`ir_property`, global default `property_valuation='manual_periodic'`, 15 category overrides to `real_time`):

| Class | distinct products | effective policy |
|---|---|---|
| 92 with a GL entry | 28 | **27 `real_time`**, 1 `manual_periodic` |
| 1,175 with no GL entry | 425 | **422 `manual_periodic`**, 3 `real_time` |

*(the 1 + 3 crossovers are unexplained residue — see §5.3; they do not disturb the split.)*

### 1.3 Direction is also wrong

For the 92 entries that *did* post, the net effect on the inventory account is a **credit**:

```
184 GL lines on the 92 price-difference valuation entries
  1141001 Raw material            asset_current        92 lines   net −7,267,712.95   (inventory DOWN)
  2900000 Goods Receipt Note(GRN) liability_current    90 lines   net +7,270,276.79
  4010002 Consumption of raw ...  expense_direct_cost   2 lines   net    −2,563.84
```

"Capitalised" asserts an increase in carried inventory. The observed net is a **฿7.27m reduction** of
`1141001`, offset against the GRN suspense account. P08/P11 will plan a reconciliation in the wrong
direction on this wording.

### 1.4 The correction is not even self-consistent with its own entry

Comparing each of the 92 layers' `svl.value` against the amount actually posted on its own journal entry:

```
87 of 92 match to the cent   ← positive control: the comparator can return equality
 5 of 92 do not:
   svl 27396  |value| 496,791,493,239,011,648.00   GL     949,318.80
   svl 27395  |value| 437,690,355,155,325,440.00   GL     836,384.40
   svl 27193  |value|      10,954,387,437.50       GL     461,037.60
   svl 66823  |value|           4,703,359.50       GL   4,771,200.00
   svl 66824  |value|           3,963,960.00       GL   3,901,481.52
Sub-ledger vs GL divergence over the 92: −934,481,859,346,472,448.00
```

`create_date == write_date` on svl 27396/27395/27193 — the layer was **born** carrying a value its own
journal entry does not carry. This is the C-2 cost explosion arriving in the price-difference path.
Any P11 tie-out of `stock.valuation.layer` to the inventory GL that includes these rows will not close,
and the break is not caused by a missing entry.

---

## 2. "NO P&L VARIANCE LINE" — **CHALLENGED (falsified in the observed path; two live routes)**

### Route A — the price-difference valuation entry itself lands on a P&L account. **It happened.**

`stock_move.py:380` `_get_src_account` returns
`location.valuation_out_account_id or accounts_data['stock_input']`. The category input account is not
constrained to be a balance-sheet account, and here it is not:

```
ir_property, product.category, property_stock_account_input_categ_id : 22 rows
   → 2900000 (GRN, liability)   11
   → 4010006 / 4010002 / 4010007 (expense_direct_cost)   4      ← P&L
   → unset                       7
```

**4 of 22 configured categories route the credit leg of a purchase price difference straight to a P&L
expense account.** And it fired, twice, inside the very population the sentence describes:

```
move 2085  Dr 4010002 Consumption of raw materials packaging  736.16 / Cr 1141001 Raw material  736.16
move 4998  Dr 1141001 Raw material  3,300.00 / Cr 4010002 Consumption of raw materials packaging 3,300.00
```

Both are `in`-move price-difference corrections; both are posted; net **−฿2,563.84** to the P&L.
Small in money, fatal to an absolute sentence.

*Positive control for this detector:* the same predicate over the whole `STJ` journal returns **9,148**
P&L lines across 56,784 entries — it fires abundantly, so the "2" is a measurement, not a dead query.

### Route B — for the 1,175 bill-only layers the entire price sits in the P&L by construction

For a `manual_periodic` product there is no receipt entry, no GRNI leg and no valuation entry. The vendor
bill debits its own line account at the **billed** price. Resolving each layer's `account_move_line_id`:

```
bill-line account of the 1,175 no-GL price-difference layers (1,175 / 1,175 resolved)
   expense    1,016
   income        66   (3200090 'local discount')
   asset         90   (7180001 'Major Expense Job:MEJ')
   liability      3
```

**1,082 of 1,175 (92.1%) of these price differences sit on a bill line posted to a P&L account.** There is
no separately-labelled "purchase price variance" line — which is exactly why the sentence is dangerous:
P08/P11 will conclude the P&L is insulated from purchase price movement, when for 92.7% of the population
the *whole purchase price*, difference included, is expensed on the bill.

### Route C — the 16 categories the assignment names: **CONFIRMED and it cuts the other way**

```
ir_property, product.category, property_account_expense_categ_id : 27 rows
   → 2900000 GRN (liability)  16
   → P&L accounts             11
```

So 16 categories neutralise the bill's expense leg into the GRN suspense account, and **11 do not**.
The estate is a mixed population on this axis too; no single sentence covers it.

### Route D — revaluation / manual MISC: **EVIDENCE NEEDED NEXT, not cleared**

I did not find a purchase-price-difference amount arriving at the P&L by a manual `entry`. I did **not**
run a discriminating test for it, and I make **no** negative claim: `T_account_move`+`T_account_move_line`
are in scope but I have no predicate that identifies a *purchase price difference* on a manually-keyed
entry. Class-B negative under the deep-research standard. See §5.

---

## 3. "IN THE OBSERVED PATH" — **MISSING (a description, not a declared set)**

`observed path` is nowhere defined in CLOSURE.md. A downstream reader has no set to check against, and the
package's own §C-9 tells them the evidence is 6.3% of tables. Three bounds the phrase must carry and does not:

1. **The engine cannot fire on `standard`-cost products at all** — `account_move.py:59` filters
   `cost_method != 'standard'`. Global default `property_cost_method = 'standard'`; **26 of 30 categories
   override** (18 `fifo`, 8 `average`); **4 categories inherit `standard`** and are structurally invisible
   to this entire sentence.
2. **Anglo-saxon is off** (`res_company.anglo_saxon_accounting='f'`), so the *journal-line* engine that would
   have produced a named variance line is disabled company-wide. The sentence's "no variance line" is a
   restatement of that flag, not a finding about price differences.
3. **The single company observed.** `res_company` is one row here; the sentence is written as a system
   property.

Per the scope-stated-as-description defect: **declare POPULATION / PREDICATE / PATH SET / UNIT or delete
the clause.** As written, P08 and P11 will read it as a general statement about the system. It is not one.

---

## 4. WHT BOUNDARY — **SUPPORTED, with one routing defect**

- `withholding_tax_cert` = **5,201** rows (done 5,191 / cancel 5 / draft 5) — C-2 reproduces exactly.
- `account_withholding_tax`: 7 rows; **`WHT3%` carries `amount = 0`** — C-2 reproduces exactly.
- Statutory-wording sweep of CLOSURE.md (`grep -niE "thai|revenue department|law|statut|must |shall |PND"`)
  returns **2 hits, both procedural** (line 13 "need external/statutory evidence", line 84 "Statutory
  questions: none answered; six routed to P07"). **No statement of what Thai law requires appears in the
  package.** The boundary is correctly held.
- Nothing in this round touches WHT, so the boundary is unchanged by this round's findings.

**Defect (RISKY, not fatal):** C-9 says "six routed to P07" but **CLOSURE.md carries none of the six**.
They exist and are enumerated at `EXPERT_3.md:785-796` (items 1-6, keyed to E3-F-12, -16, -17, -18/-19,
-20, -23/-24). A recipient handed CLOSURE.md alone cannot verify the count, cannot check the routing, and
P07 cannot accept a handoff it cannot see. **Carry the six identifiers into C-9, or cite the anchor.**

---

## 5. WHAT I AM *NOT* CLAIMING

1. **§1.2 is a negative about GL entries.** Its positive control is that the identical field on 92 sibling
   layers *does* point at an STJ entry — the overwrite is observable when it occurs. It remains bounded by
   `GAP-P01-07` and by the fact that nothing was executed at runtime.
2. **§2 Route D is unrun.** "I found no manual route" is NOT "no manual route exists" (Class B).
3. **§1.2 residue.** 1 `manual_periodic` product in the GL class and 3 `real_time` products in the no-GL
   class are unexplained. I did not check `product.template`-level `ir_property` overrides (C-4 notes 6 such
   rows exist for a different field). Unresolved.
4. I have not established whether the 5 layer/GL divergences in §1.4 are new or already inside C-2's
   "8 posted items > ฿1bn". **They overlap by construction and must not be double-counted.**

---

## 6. PROPOSED REPLACEMENT SENTENCE (for C-4)

> In this deployment the price-difference correction engine fired on **1,267** valuation layers. **92**
> of them (products in the 15 `real_time` categories) produced a journal entry in the `STJ` Inventory
> Valuation journal, netting **−฿7,267,712.95 against `1141001 Raw material`** and **+฿7,270,276.79
> against `2900000 GRN`**, with **2 lines landing on the P&L account `4010002`**; **5** of those 92 layers
> carry an `svl.value` their own entry does not carry. The remaining **1,175** produced **no journal entry
> of any kind** — their products are `manual_periodic` — and **1,082 of them sit on a vendor-bill line
> posted to a P&L account**. A separately-identified purchase-price-variance line does not exist because
> `anglo_saxon_accounting` is `FALSE`; this is **not** evidence that purchase price differences are kept
> out of the P&L. Products in the 4 categories that inherit `cost_method='standard'` are outside this
> statement entirely.

---

## 7. VERDICTS

| # | Sub-question | Verdict |
|---|---|---|
| 1 | "capitalised into inventory" accurate? | **CHALLENGED** — true for 92 of 1,267 layers; false for 1,175; and directionally wrong (net inventory **credit** ฿7.27m) for the 92 |
| 2 | `price_diff_value` moves a GL balance? | **CHALLENGED** — 92.7% never reach the GL; and on 5 of the 92 that do, layer and entry disagree by up to 17 orders of magnitude |
| 3 | "no P&L variance line" too strong? | **CHALLENGED / falsified** — 2 posted lines on `4010002` in-path; 4 categories configure `stock_input` to a P&L account; 1,082 bill lines carry the difference to P&L |
| 4 | Route D (revaluation / manual MISC) | **EVIDENCE NEEDED NEXT** — no discriminating predicate run; no negative claimed |
| 5 | "in the observed path" bounds it? | **MISSING** — no POPULATION / PREDICATE / PATH SET / UNIT; 4 `standard` categories and the anglo-saxon flag are silently inside the phrase |
| 6 | WHT boundary correctly stated? | **SUPPORTED** — 5,201 certs and `WHT3%=0` reproduce; no statutory statement in the package |
| 7 | The six P07 items | **RISKY** — counted in C-9, enumerated only in `EXPERT_3.md:785-796`; not carriable by a CLOSURE-only recipient |

## 8. EVIDENCE NEEDED NEXT (ranked)

1. **A discriminating predicate for Route D.** Manual `entry` moves touching `2900000` **and** a P&L account
   with no `stock_valuation_layer_ids` and no `stock_move_id`. Needs `account_move.stock_move_id` +
   `stock_valuation_layer_ids` join across all 183,590 entries. Until run, §2 Route D stays open.
2. **`product.template`-level `property_valuation` / `property_cost_method` rows** — settles the 4 crossover
   products in §1.2 and bounds the "4 `standard` categories" claim in §3.
3. **Why 3 layers were created with a value their own entry contradicts** — the parent layers (27283,
   27102) carry `unit_cost` 15,685,015,415,021.04 and 712,186.25. This is the C-2 explosion inside the
   price-difference path; the reconciliation consequence has never been measured.
4. **`stock_landed_cost_id`** — a fourth route into the same layer/GL relationship, present as a column and
   untouched in six rounds.
