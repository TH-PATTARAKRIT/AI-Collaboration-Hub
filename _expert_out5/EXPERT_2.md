# AAS-03 EXPERT 2 — LEADERSHIP DATABASE DESIGN
## Adversarial challenge of the frozen P01 SERIES-16 findings brief
Scope: **the evidence base and the population, not the conclusions.** Read-only throughout.
No database was written, no source modified, nothing installed, no server run, no external network use.

---

## 0. DECLARED BOUNDARIES

| Rung | Declaration |
|---|---|
| **POPULATION** | The 41 `T_*.sql` COPY extracts in `s16/`, all derived from `~/Downloads/iSMEs_2026-07-11_05-03-27.dump`. Row-level populations are declared per finding. |
| **PATTERN** | `^COPY public\.("?)([A-Za-z0-9_]+)\1 \((.*)\) FROM stdin;` … terminated by a line equal to `\.`; field separator TAB; `\N` = NULL. |
| **PATH SET** | `/private/tmp/claude-501/…/scratchpad/s16/T_*.sql` (41 files, enumerated by `glob('T_*.sql')`, not by an author list). The dump itself was not re-extracted; see E2-13 for what that leaves open. |
| **UNIT** | Declared per finding. The units in play are: SVL **row**, journal **item** (`account_move_line`), journal **entry** (`account_move`), **ir_property row**, **column** (for the date sweep), and **file** (for the instrument audit). These are NOT interchangeable and several of the brief's defects are exactly a unit/predicate slip. |

**Instrument.** I did not use `s16/pgc.py` for any measurement. I wrote `s16/e2/p2.py`, which differs structurally in the one respect that matters: it resolves columns **by position with an explicit index lookup that raises `KeyError` on an absent column**, and it **counts** rows whose field count differs from the header instead of padding them. Cross-checks were additionally run in `awk` (`s16/e2/audit.awk`) with no float conversion and no Python at all.

---

## 1. INSTRUMENT AUDIT (prerequisite to every number below)

```
$ for f in T_*.sql; do awk -f e2/audit.awk "$f"; done
T_account_move.sql           cols=85 rows=183590 terminated=1 fieldcount_hist{85:183590 }
T_account_move_line.sql      cols=67 rows=447384 terminated=1 fieldcount_hist{67:447384 }
T_stock_valuation_layer.sql  cols=19 rows=74982  terminated=1 fieldcount_hist{19:74982 }
T_product_product.sql        cols=14 rows=5101   terminated=1 fieldcount_hist{14:5101 }
T_product_template.sql       cols=56 rows=3949   terminated=1 fieldcount_hist{56:3949 }
T_product_category.sql       cols=13 rows=30     terminated=1 fieldcount_hist{13:30 }
T_ir_model_fields.sql        cols=35 rows=11992  terminated=1 fieldcount_hist{35:11992 }
T_ir_property.sql            cols=16 rows=13331  terminated=1 fieldcount_hist{16:13331 }
T_account_account.sql        cols=24 rows=339    terminated=1 fieldcount_hist{24:339 }
T_stock_move.sql             cols=63 rows=103949 terminated=1 fieldcount_hist{63:103949 }
… (all 41 files: exactly one COPY block each, all terminated, single-valued field-count histogram)
```

**Every file has exactly one COPY block, is properly terminated by `\.`, and has a single-valued field-count histogram.** Column alignment is therefore sound in all 41 files, and the extraction is complete (not truncated) in all 41.

### E2-12 — CHALLENGED: the brief's account of its own worst defect is wrong

The brief's correction #4 states: *"I joined on `stock_valuation_layer.categ_id` — a column that does not exist in series 16. **My parser padded it with nulls** and the result looked plausible."*

Two parts of that are not what happened.

**(a) The padding branch never fired — anywhere.** `pgc.py`'s pad/truncate line is `if len(vals) != len(cols): vals = (vals + [None]*len(cols))[:len(cols)]`. The histogram above shows **zero rows in any of the 41 files** have a field count differing from the header. The stated mechanism is untriggered.

The real mechanism is `dict(zip(cols, vals))` + an unchecked `.get()`:

```
$ python3 -c "... from pgc import load; c,r=load('T_stock_valuation_layer.sql'); print(repr(r[0].get('categ_id')))"
None    <-- SILENT None, no exception       (len(cols)=19)

$ python3 -c "... from p2 import Tbl; Tbl('T_stock_valuation_layer.sql').col('categ_id')"
KeyError: COLUMN 'categ_id' DOES NOT EXIST in stock_valuation_layer. Available: ['id','company_id','product_id', …]
```

This matters because **the correction the brief applied does not cover the defect class**. It fixed one join. Every other `.get()` on every other table in the package has the same silent-None failure mode and no control was added for it. The class-level fix is a parser that raises, which is what I used for every number in this report.

**(b) `categ_id` is not "a column that does not exist" — it is a field that exists and is not stored.** Schema authority, `ir_model_fields` (the deployment's own metadata, extracted at `T_ir_model_fields.sql`, 11,992 rows):

```
stock.valuation.layer field rows: 27
   categ_id        | ttype=many2one | store=f | related=product_id.categ_id
   product_tmpl_id | ttype=many2one | store=f | related=product_id.product_tmpl_id
   currency_id     | ttype=many2one | store=f | related=company_id.currency_id
   …
```

The distinction is load-bearing in two directions. Against the brief: "column does not exist" is the wrong negative — the correct one is "the field is `store=f`, so there is no SQL column". **For** the brief: Odoo's own definition of the field is `product_id.categ_id`, and `product_product` has no `categ_id` column either (delegated to the template), so the corrected join `SVL → product_product.product_tmpl_id → product_template.categ_id` **is** the resolution of the model's own related path. The corrected join is right for the right reason, which the brief did not establish.

---

## 2. ASSIGNMENT 1 — POPULATION AND DENOMINATOR OF THE HEADLINE SPLIT

### E2-04 — SUPPORTED (reproduced exactly, independent instrument)

Every join key was verified to exist in the series-16 schema before use (`product_product.product_tmpl_id` pos 3; `product_template.categ_id` pos 4; `product_category.id` pos 1; `ir_property.fields_id/res_id/value_text` pos 3/8/11).

```
GLOBAL default = manual_periodic | per-category rows = 15
CONTROL per-category res_ids not present in product_category: []

=== INDEPENDENT 4-WAY SPLIT (unit = stock_valuation_layer row; population = all 74,982) ===
   manual_periodic  linked       1209
   manual_periodic  unlinked    16075
   real_time        linked      56654
   real_time        unlinked     1044
   TOTAL classified: 74982
=== COVERAGE CONTROL (unresolved) ===
   0 unresolved across all four join hops
   classified+unresolved = 74982 vs table rows 74982
```

**56,654 / 1,044 / 1,209 / 16,075 reproduces to the row**, on a position-based, raise-on-missing-column instrument, with the coverage control at 0 across all four hops. Residual A decomposes to **748 value=0 / 296 value≠0**, also exactly as published.

### E2-16 — SUPPORTED: the denominator cannot be widened by a second policy carrier

The obvious way to break this denominator is a second place the policy could live. I enumerated every field on every model whose name contains `valuation` or `cost_method`, and every `fields_id` actually used in `ir_property`:

```
product.category  property_valuation  ttype=selection store=f related=None      <-- the only carrier
product.product   valuation           store=f related=categ_id.property_valuation
product.template  valuation           store=f related=categ_id.property_valuation
product.category  property_cost_method store=f related=None
stock.quant       cost_method         store=f related=product_categ_id.property_cost_method

=== ir_property usage by field (all 13,331 rows) ===  COVERAGE CONTROL unresolved fields_id: 0
      16  product.category  property_valuation
      27  product.category  property_cost_method
       1  product.category  property_stock_journal
       1  product.category  property_account_creditor_price_difference_categ
       6  product.template  property_account_creditor_price_difference     <-- see E2-02
    3208  product.product   standard_price
      …
```

`product.category.property_valuation` is the sole carrier; the product- and template-level `valuation` fields are unstored relateds pointing back at it. The population is correctly bounded. The 16 rows are 1 global (`company_id` NULL, `res_id` NULL, `manual_periodic`) + 15 per-category (`company_id`=1, `real_time`), matching S16-02.

### E2-15 — SUPPORTED and strengthened: the policy-change refutation

The brief refuted policy-change using `create_date` spread plus residual distribution, and conceded *"`ir_property` records current state, not history."* Two stronger probes were available and unused.

**(i) In-place modification probe, with a positive control:**
```
property_valuation rows whose write_date != create_date: 0   (of 16)
POSITIVE CONTROL — ir_property total=13331  write_date!=create_date=2112
```
The mechanism is demonstrably visible in this table (2,112 of 13,331 rows carry a later write), and **none of the 16 policy rows was ever rewritten**. That is a real negative with a working control, not an inference from spread.

**(ii) The subledger records method-change events directly:**
```
SVL descriptions matching 'aluation method change': 2 rows
  svl=542 create=2023-10-11 06:47:27 value=0.00 am=\N   "Valuation method change for product category All / Expenses …"
  svl=543 create=2023-10-11 06:47:27 value=0.00 am=1346 "Valuation method change for product category All / Expenses …"
  SUM(value) = 0.00
```
`ir_property` id=20935 (`product.category,6` → `real_time`) has `create_date = 2023-10-11 06:47:27.174339` — **the same timestamp**. One method-change event exists, it is dated 2023-10-11, it affected category 6, and it moved ฿0.00 of value. Category 6 carries 2 SVL rows in total.

**Residual caveat, preserved:** Odoo's `set_multi` deletes and re-inserts `ir_property` rows, so a *reverted* setting (real_time → periodic) would leave no row and no write_date. The two probes above narrow the exposure sharply but do not close it. This is a **narrow** negative and should be published as such.

### E2-03 — CHALLENGED (decisive): Residual B is not what the brief says it is

The brief presents Residual B as *"1,209 manual_periodic layers that **do** carry a journal entry, across 9 distinct categories"* — framed as valuation leaking into the GL. The mechanism probe reverses the direction of causation:

```
=== Residual B (1,209): what kind of account_move do they point at? ===
  move_type: {'in_invoice': 1172, 'entry': 37}
  state    : {'posted': 1209}
  price_diff_value: {'nonzero': 1047, 'zero/null': 162}
  ORPHAN account_move_id: 0
  stock_move_id NULL: 1194 of 1209

=== CONTROL: the 56,654 real_time LINKED layers — same probe ===
  move_type: {'entry': 56651, 'in_invoice': 3}
  stock_move_id NULL: 225
  ORPHAN account_move_id: 0
```
Description shapes confirm it: Residual B is `AP#### (…) - <item>` (vendor bill references); the real_time linked population is `WH/IN/…`, `WH/MO/…`, `STJ…` (stock documents).

**1,194 of 1,209 Residual-B layers have no stock move at all, and 1,172 point at a vendor bill.** They were not created by a stock movement that then posted to the GL; they were created **by the posting of the vendor bill**, which is why they carry its `account_move_id`. And 1,047 of them carry a non-zero `price_diff_value`.

Residual B is the **vendor-bill price-difference layer population**, not a policy leak. The category's `manual_periodic` setting is not the operative variable for these rows. The 9-category count is correct as an arithmetic fact and misleading as an explanation.

**Consequence for the brief's argument:** S16-03 uses Residual B as evidence that policy classification does not fully predict GL linkage. That inference does not survive — for 98.8% of Residual B the policy was never consulted. The genuinely unexplained sub-population is the **15 Residual-B rows that do have a stock move**, plus the **37 pointing at `entry` moves**, which have not been characterised by anyone.

---

## 3. ASSIGNMENT 2 — THE 15-ORDER-OF-MAGNITUDE DIVERGENCE

### E2-05 — SUPPORTED as real stored data; mechanism newly identified

**Not a parse, locale, or scientific-notation artefact.** Raw-text probe with no float conversion:
```
=== RAW TEXT PROBE (awk): scientific notation in SVL numeric columns 11-15,18 ===
  no [eE] in cols 11-15,18 (quantity,unit_cost,value,remaining_qty,remaining_value,price_diff_value)
=== POSITIVE CONTROL: [eE] anywhere in the SVL data block ===
  data lines containing [eE] anywhere: 35020
=== count of |value| with >=13 integer digits, by string length, no float parsing ===
  30
```
The control shows the detector fires on 35,020 lines; it finds no scientific notation in any numeric column. Re-derivation **by string length on the raw bytes** independently yields **exactly 30 rows**.

**Second, structurally different derivation — the IEEE-754 signature.** Every extreme `value` is *exactly* a representable float64, i.e. divisible by its own ULP:
```
  id=27394  |value|~2^70  ULP=2^18=262144   divisible=True   Decimal(float(value))==value: True
  id=27943  |value|~2^69  ULP=2^17=131072   divisible=True   True
  id=27942  |value|~2^68  ULP=2^16=65536    divisible=True   True
  id=27283  |value|~2^59  ULP=2^7 =128      divisible=True   True
  id=27485/27487 ~2^56    ULP=2^4 =16       divisible=True   True
  id=27498/27499 ~2^55    ULP=2^3 =8        divisible=True   True
```
**Internal consistency (`value` vs `quantity` × `unit_cost`):**
```
  id=27394  exact q*u = 1533508025629365246480   stored = 1533508025629365764096   rel.err = 3.375e-16
  id=27283  exact q*u = 736489898812312933       stored = 736489898812313344       rel.err = 5.578e-16
  id=27928  exact q*u = -89946158542346863       stored = -89946158542346320       rel.err = 6.040e-15
```
`value` agrees with `quantity × unit_cost` to within one to a few ULP in every case. **`value` is arithmetically correct. The corruption is entirely in `unit_cost`.**

**`remaining_value` is arithmetic noise, not money:**
```
  id=27394  remaining_value=-262144.00  ULP(value)=262144  ratio=1.00
  id=27487  remaining_value=-16.00      ULP(value)=16      ratio=1.00
  id=27499  remaining_value=-4.00       ULP(value)=8       ratio=0.50
  id=27283  remaining_value=24.00       ULP(value)=128     ratio=0.1875
```
`remaining_value = −262,144.00` is **exactly one ULP** at 1.5e21. It is the residue of catastrophic cancellation in the running FIFO/AVCO remainder, not a ฿262,144 balance. At these magnitudes the monetary field cannot represent satang: **the granularity of the stored subledger value on the largest row is ฿262,144.**

### E2-14 — CHALLENGED: the brief understates `unit_cost` by five orders of magnitude
The brief cites *"`unit_cost` values such as 744,082,316,162.43"*. Measured maxima over the 30:
```
  max |unit_cost| : 52616504567828624.00      (5.26e16, not 7.4e11)
  max |value|     : 1533508025629365764096.00 (1.53e21 — the brief's ±1.5e21 is correct)
```
The brief picked a mid-range example and presented it as the extreme. The `value` figure is right; the `unit_cost` figure is not.

### E2-17 — SUPPORTED: 25 of 30 posted, GL balanced — now measured with denominators
```
  extreme rows: 30 | with account_move_id: 25 | without: 5
  states: {'posted': 25}   linked move date range: 2024-08-17 .. 2024-08-31
  SVL create_date range (all 30): 2024-08-28 09:25:34 .. 2024-09-03 16:26:39
  distinct products in the 30: 4 ['11556','11630','11632','11633'] | companies: {'1': 30}
```
The brief asserts the GL is uncorrupted but never computes both sides. Reconciliation over the 56,654 account_moves the real_time layers point at:
```
  journal items on the 4 valuation accounts: 78022, NET Dr-Cr = 190,605,547.37
  Subledger SUM(value) real_time LINKED     = 6,462,975,280,284,184.50
  UNRECONCILED DIFFERENCE                   = -6,462,975,089,678,637.13
  SUM of all account nets over those moves (balance check) = 0.00
```
**The divergence is now a measured quantity (฿6.46 × 10^15) rather than an assertion, and the moves balance to 0.00** — S16-04's core conclusion holds and is strengthened.

### E2-06 — NEW: the correction was made in the subledger with no journal entry
```
=== The 5 extreme rows with NO journal entry ===
 svl=27953 stock_move=\N  value=-1073730548532915.38  "Product value manually modified (from -512276009011.16003 to …"
 svl=28043 stock_move=\N  value=-4692061736733489.00  "Product value manually modified (from 704992237516.1901 to 3…"
 svl=27992 stock_move=45156 value=-344714247016601.62 "Revaluation of UB/00444 (negative inventory)"
 svl=27991 stock_move=45152 value=-340484624353821.31 "Revaluation of UB/00443 (negative inventory)"
 svl=27998 stock_move=45156 value=-11983930878111.80  "Revaluation of UB/00444 (negative inventory)"
   SUM of unposted corrective layers = -6,462,975,087,514,939.11
```
The 25 erroneous layers **were** posted (with sane GL amounts). The 5 layers that reverse ฿6.46 × 10^15 of subledger value carry **`account_move_id` NULL — no journal entry whatsoever**. The subledger was repaired out of band. The "from −512,276,009,011.16" text also confirms the corrupted figure had been persisted as the product's cost.

### E2-07 — NEW: the corruption is invisible in aggregate (reachability)
```
  SUM(value)            all 74,982 : 205,490,835.87
  SUM(value)  excl the 30 extremes : 400,338,755.98      <-- the brief's figure, reproduced exactly
  rows with remaining_value NOT NULL: 31,755
  SUM(remaining_value)  all        : 206,274,224.42
  SUM(remaining_value) excl the 30 : 206,536,366.01
  => the 30 extremes contribute to remaining_value: -262,141.59
```
The brief reports the ฿400.3M *excluding* the 30 and leaves the impression the total is broken. **The total including all 74,982 rows is ฿205,490,835.87 — a plausible number.** The extremes very nearly cancel (net −฿194.8M). A report summing `SVL.value` shows nothing unusual. The stock-on-hand valuation (`remaining_value`) is distorted by **−฿262,141.59**, which is float-noise, not a business balance.

**This is the answer to "are the 30 rows reachable from any report": they are reachable, and they are camouflaged.** Aggregate-level monitoring cannot detect them. Only a row-level magnitude test finds them.

### E2-18 — CHALLENGED as a live risk; SUPPORTED as historical
```
=== Is the corrupt cost PERSISTED as product standard_price? ===
   product 11556  standard_price=37.17  write_date=2025-04-30
   product 11630  standard_price=41.59  write_date=2025-10-06
   product 11632  standard_price=19.81  write_date=2025-10-06
   product 11633  standard_price=16.36  write_date=2025-09-28
=== POSITIVE CONTROL: |standard_price| across ALL 3,208 products ===
   max=7.5e+05  p99=1.95e+04  median=26.64
   products with |standard_price| >= 1e6 : 0     >= 1e9 : 0
```
The cost master is currently sane for all four products and for the entire catalogue. The episode is bounded to **2024-08-17 … 2024-09-03** and is **historically latent, not currently live** at the cost-master level. The corrupted layers nonetheless remain in the subledger permanently.

---

## 4. ASSIGNMENT 3 — LINEAGE LOSS AND DESTRUCTIVE CORRECTION

### E2-01 — CHALLENGED (most consequential correction): the GRNI balance is a cancelled-item artefact

S16-05 publishes: *"Account 39 … **13,736 items, Dr ฿6,558,441,923.88 / Cr ฿6,486,344,109.63, net ฿72,097,814.25 outstanding**"* and *"Vendor bills relieve it: 6,653 bill lines debit account 39, ฿4,516,394,611.47 Dr."*

```
=== GRNI (account 39) by move_type x state (unit = journal item) ===
   entry        cancel   items=1     Dr=0.00            Cr=90,351,213.15    net=-90,351,213.15
   entry        posted   items=7043  Dr=2,042,047,312.41 Cr=6,379,500,983.14 net=-4,337,453,670.73
   in_invoice   cancel   items=41    Dr=172,292,940.50  Cr=0.00             net=+172,292,940.50
   in_invoice   draft    items=17    Dr=2,724,152.20    Cr=0.00             net=+2,724,152.20
   in_invoice   posted   items=6595  Dr=4,341,377,518.77 Cr=0.00            net=+4,341,377,518.77
   in_refund    cancel   items=11    Dr=0.00            Cr=5,519,373.22     net=-5,519,373.22
   in_refund    posted   items=28    Dr=0.00            Cr=10,972,540.12    net=-10,972,540.12
   ALL STATES TOTAL items=13736 Dr=6,558,441,923.88 Cr=6,486,344,109.63 net=72,097,814.25
```
The brief's figures reproduce **to the satang — as all-states totals.** There is no state filter anywhere in S16-05.

| | items | net on account 39 |
|---|---|---|
| Brief (all states) | 13,736 | **+฿72,097,814.25** |
| **Posted only** | **13,666** | **−฿7,048,692.08** |
| Cancelled + draft | 70 | +฿79,146,506.33 |

**The published GRNI position is composed entirely of 70 journal items on cancelled and draft moves.** The real posted balance is a **credit of ฿7,048,692.08** — the sign is opposite to what was published, and the magnitude differs by an order of magnitude. A single cancelled `entry` carries ฿90,351,213.15 of it.

The same unfiltered predicate runs through the rest of S16-05. Brief vs posted-only item counts: 1062 Raw material **22,561 → 22,559**; 1068 WIP **39,935 → 39,928**; 1289 Semi Product **10,993 → 10,988**; 1286 ByProduct **4,695 → 4,694**. And the bill-relief line: **6,653 / ฿4,516,394,611.47 is all-states; posted-only is 6,595 / ฿4,341,377,518.77** — ฿175,017,092.70 of the claimed relief sits on cancelled and draft bills.

**This is the direct answer to "what happens to GRNI items when a vendor bill is reset to draft or cancelled": the journal items are retained on the account.** They are excluded from a posted trial balance but included by any query that does not filter `parent_state`. The brief ran exactly such a query.

### E2-08 — NEW: 97.8% lineage loss from valuation layer to journal item
```
=== SVL integrity (population = 74,982) ===
   account_move_line_id NULL but account_move_id set: 56,596   (of 57,863 linked = 97.81%)
   stock_move_id NULL:                                 1,471
   product_id absent from product_product:                  0
   stock_move_id set but absent from stock_move:            0
   company_id NULL:                                         0
```
A valuation layer can be traced to a journal **entry** but, in 56,596 of 57,863 cases, **not to the journal item within it**. Sub-ledger-to-line reconciliation is unavailable for 97.8% of the linked population. Neither the brief nor S16-05's "GRNI bridge EXECUTED" conclusion accounts for this.

### E2-09 — NEW: valuation layers surviving cancelled journal entries
```
=== SVL -> account_move lineage (unit = SVL row; population = 74,982) ===
   move state=posted   57,854
   no account_move_id  17,119
   move state=cancel        9        <-- SUM(value) = -9,279,784.92
   move state=draft         0
   ORPHAN (move deleted)    0
     svl=57739 move=166611 STJ2025081400 value=-7,136,031.75  "Product Quantity Updated - คัดแล้ว-ข้าวหอมมะ…"
     svl=41917 move=132024 STJ2025011558 value=-2,106,768.89  "WH/MO/05486/SWR - คัดแล้ว-ข้าวพิษณุโลก"
     svl=37581 move=122935 STJ2024111872 value=-46,410.26     "WH/OUT/01378 - By Product-ปลายซีข้าวขาว"
     svl=543   move=1346   STJ2023100326 value=0.00           "Valuation method change for product category"
     … (9 rows total)
```
**9 valuation layers carrying ฿9,279,784.92 of subledger value point at journal entries that are cancelled.** The subledger still counts the value; the ledger does not. No layer points at a draft move, and **no `account_move_id` is orphaned** (0 dangling references) — so the failure mode here is cancellation, not deletion.

### E2-19 — SUPPORTED: reversals, with two states worth preserving
```
=== Reversals (unit = account_move row; population = 183,590) ===
   moves carrying reversed_entry_id : 5115          <-- brief: 5,115, reproduced
   their own state:  {'posted': 5057, 'cancel': 58}
   their move_type:  {'entry': 5024, 'in_refund': 85, 'out_refund': 6}
   state of the move they REVERSE: {'posted': 5061, 'cancel': 54}
   ORPHAN reversed_entry_id (target row absent): 0
```
**54 reversing entries reverse a move that is itself cancelled** (reversal and cancellation both applied to the same entry), and **58 reversing entries are themselves cancelled**. Reversal lineage is otherwise intact: no `reversed_entry_id` dangles.

### E2-20 — SUPPORTED: no orphaned journal items, and the null-account rows are benign
```
=== account_move_line (population = 447,384) ===
   move_id with no account_move row     : 0
   company_id NULL                      : 0
   account_id NULL                      : 889
   product_id pointing at absent product: 0
=== the 889: what display_type? ===
   {'line_note': 827, 'line_section': 62}   total 889
```
The 889 account-less journal items are **all** presentation rows (`line_note` / `line_section`), which by design carry no account. Closed as benign with the discriminating field, not by assumption.

---

## 5. ASSIGNMENT 4 — COMPANY / SCOPE ISOLATION

Sweep across every extracted table that has a `company_id` column (unit = row; PATH SET = all 41 `T_*.sql`):
```
   account_account       339      {'1': 339}
   account_analytic_line 339382   {'1': 339382}
   account_move          183590   {'1': 183590}
   account_move_line     447384   {'1': 447384}
   account_partial_reconcile 63773 {'1': 63773}
   stock_valuation_layer 74982    {'1': 74982}
   stock_move            103949   {'1': 103949}
   … (all other tables: {'1': n})
   ir_property           13331    {'\N': 8, '1': 13323}      <-- NULL company_id
   product_template      3949     {'\N': 3949}               <-- NULL company_id (ALL rows)
   stock_location        28       {'\N': 6, '1': 22}         <-- NULL company_id
   stock_quant           27196    {'1': 16901, '\N': 10295}  <-- NULL company_id (37.9%)
```

### E2-11 — closed as design-inherent, with a discriminating control
```
=== stock_quant: NULL company_id vs location usage (population = 27,196) ===
   company_id 1     usage=production  12624
   company_id NULL  usage=supplier     5931
   company_id NULL  usage=customer     4364
   company_id 1     usage=inventory    2574
   company_id 1     usage=internal     1678
   company_id 1     usage=customer        25
   CONTROL: quants with NULL company_id in an INTERNAL location? 0
   CONTROL: quants with company_id=1 in a non-internal location? 15,223
=== stock_location rows with NULL company_id ===
   id=1 view Physical Locations | id=2 view Partners | id=3 view Virtual Locations
   id=4 supplier Partners/Vendors | id=5 customer Partners/Customers | id=6 transit Inter-company transit
```
All 10,295 company-less quants sit in the six company-less virtual locations (vendor/customer), which is Odoo's design. **Zero company-less quants in an internal location.** The 8 company-less `ir_property` rows are the global defaults, also by design. Not a defect — but stated with the control rather than assumed.

### E2-21 — RISKY (latent): the policy is company-scoped, its subject is not
**All 3,949 `product_template` rows have `company_id` NULL**, while all 15 `property_valuation` rows that decide their valuation policy carry `company_id = 1`. Products are global; the policy that governs them is company-specific. With one company this resolves unambiguously — `res_company` has exactly 1 row, and `account_move`, `account_move_line`, `stock_valuation_layer`, `stock_move` are 100% company 1, so **no cross-company reference and no company-ambiguous transaction exists today.** If a second company is ever added, every product silently inherits the *global* `manual_periodic` default rather than the 15 `real_time` settings, and 56,654 layers' worth of behaviour changes with no configuration edit. Latent, not live.

---

## 6. ASSIGNMENT 5 — BUDDHIST-ERA DATES

### E2-10 — CHALLENGED: the extent is far larger than 30 rows in one column

S16-07 reports *"30 `account_move` rows are dated year `2567`"*. Sweep of **every date-shaped value in every column of every one of the 41 extracted tables**:
```
PATTERN ^(\d{4})-(\d{2})-(\d{2}) ; BE flagged when year >= 2400 ; PATH SET = s16/T_*.sql (41 files)
  account_analytic_line      date                   {2567: 120}
  account_move               date                   {2567: 30}          <-- the only one the brief found
  account_move               invoice_date           {2568: 1}
  account_move               tax_period             {2568: 4, 2567: 3}
  account_move_line          date                   {2567: 120}
  mrp_production             date_planned_finished  {8202: 1}
  mrp_production             date_planned_start     {8202: 1}
  purchase_order             date_planned           {2568: 2}
  purchase_order_line        date_planned           {2524: 1, 2568: 5}
  purchase_request_line      date_required          {2524: 1, 2568: 6}
  stock_move                 date                   {8202: 6, 2566: 2, 2567: 3}
  stock_move                 date_deadline          {8202: 3, 2524: 1, 2568: 5}
  stock_picking              date_deadline          {2568: 2}
  stock_picking              scheduled_date         {2566: 44, 2567: 132, 2568: 2}

=== POSITIVE CONTROL: year histogram of ALL date-shaped values ===
   distinct years seen: 43, min=1072 max=8202, total date-shaped values=5,146,366
   years < 2015: {1072:2, 1902:1, 1966:4, 1967:7, 2005:48, 2006:565, 2007:804, 2008:1014,
                  2009:1122, 2010:1294, 2011:1408, 2012:1318, 2013:1360, 2014:1486}
   years > 2030: {2031:3360, …, 2038:52, 2524:3, 2566:46, 2567:408, 2568:27, 8202:11}
```
**484 Buddhist-era values across 14 columns in 11 tables**, not 30 in 1 column — a 16× understatement of the affected column count. Plus **11 values at year 8202** (6 in `stock_move.date`, 3 in `stock_move.date_deadline`, 2 in `mrp_production`), which is a *different* corruption class the brief does not mention at all, and 14 values before 1970 (years 1072, 1902, 1966, 1967).

The brief's separate figure of **1,733 `account_move` rows dated before 2015 reproduces exactly.** The 2031–2038 population (≈10,000 values) is consistent with legitimate forward-dated maturities and is **not** claimed as a defect here.

### E2-22 — NEW: the leakage is bidirectional, and it lands on the Thai tax period
```
=== The 30 BE-dated account_move rows ===
  states: {'posted': 30} | types: {'entry': 30}
  journals: {('CABA','Cash Basis Taxes','general'): 30}      <-- all 30 in ONE journal
  date range: 2567-04-10 .. 2567-11-15 | name prefixes: CABA25670 (20), CABA25671 (10)
  tax_period values: {'2024-04-10':7, '2024-04-11':6, '2024-11-15':6, '2024-04-17':2, '2024-11-14':2, None:7}
```
All 30 are **cash-basis VAT entries** (`CABA`). Their own `tax_period` is correct Gregorian for 23 of 30 and NULL for 7.

The inverse defect also exists — **7 moves have a Buddhist-era `tax_period` with a correct Gregorian `date`**, and 1 has a BE `invoice_date`:
```
   id=152786 AP2025060322      date=2025-06-12 tax_period=2568-06-12 posted
   id=95343  JRCSH12024070137  date=2024-07-22 tax_period=2567-07-19 posted
   id=84860  JRCSH12024050189  date=2024-05-29 tax_period=2567-05-13 posted
   id=145538 AP2025040943      date=2025-04-30 tax_period=2568-04-30 posted
   id=158028 AP2025070411      date=2025-07-16 tax_period=2568-07-16 posted
   id=161986 AP2025080004      date=2025-08-01 tax_period=2568-08-01 posted
   id=123216 JRCSH12024120029  date=2024-12-06 tax_period=2567-12-02 posted
   BE invoice_date: id=171584 AP2025100170 date=2025-10-09 invoice_date=2568-10-09 posted
```
So a report keyed on `date` misses the first 30; a VAT report keyed on `tax_period` misses these 7. **There is no single column that is reliably Gregorian.**

### E2-23 — what a fiscal-year query does with them, measured
```
=== GL impact of the BE-dated journal ITEMS (unit = account_move_line) ===
  BE-dated journal items: 120  Dr=226,136.10 Cr=226,136.10 net=0.00
     acct 1281  9999991 Dummy Service   items=60 Dr=211,342.14 Cr=211,342.14 net=0.00
     acct 1084  1154002 Undue Vat       items=30 Dr=7,396.98   Cr=7,396.98   net=0.00
     acct 1083  1154001 Input VAT       items=30 Dr=7,396.98   Cr=7,396.98   net=0.00
```
A fiscal-year query is `date BETWEEN '2024-01-01' AND '2024-12-31'`. `2567-04-10` sorts after `2024-12-31`, so these rows are **silently excluded from FY2024 and from every period, ageing and lock-date computation**, while remaining in all-time balances. All three lock dates are NULL (`period_lock_date`, `fiscalyear_lock_date`, `tax_lock_date` — verified on the single `res_company` row), so nothing blocks further posting into those pseudo-periods.

Because each entry balances, **the trial balance still balances** — the defect is invisible to the one control most likely to be run. What is wrong is **per-account, per-period**: ฿7,396.98 of Input VAT and ฿7,396.98 of Undue VAT reclassification never lands in a filed period, and ฿211,342.14 moves through an account literally named **"Dummy Service"**. The money is small; the class of defect (posted, balanced, period-invisible, unlockable) is not.

Beyond the GL: `account_analytic_line.date` carries the same 120 BE values, so **analytic period reporting is affected identically**; `stock_picking.scheduled_date` carries 178, the largest single BE population, affecting delivery scheduling and ageing.

---

## 7. THE FINDING THAT MOVED FURTHEST FROM THE BRIEF

### E2-02 — CHALLENGED (decisive): "the price-difference engine has never fired" conflates an account with an engine

S16-05 publishes: *"`1173 4310005 Purchase price variance`: **CONFIGURED, 0 items**. The price-difference engine is wired and **has never fired** in 183,590 journal entries."*

The first sentence is SUPPORTED — verified across all states, not just posted:
```
   account id=1173  4310005  Purchase price variance  (expense_direct_cost)
       NO JOURNAL ITEMS AT ALL (any state)
```
The second sentence is contradicted by the deployment's own data:
```
=== price_diff_value (stock_valuation_layer, population = 74,982) ===
   nonzero rows: 1,123   SUM = ฿2,246,313,274.64
   excluding the 30 extreme-value rows: 1,121 rows, SUM = ฿460,760,614.64
   inside the 30 extremes:                   2 rows, SUM = ฿1,785,552,660
   |price_diff_value| median=฿28.65  p90=฿400  max=฿460,998,540
```
**The engine fired 1,123 times and computed ฿2,246,313,274.64 of purchase price difference.** It is stored in the subledger. Account 1173 received none of it.

The reason the brief could not see this is a denominator it did not enumerate. It reports one price-difference carrier; there are seven:
```
   product.category   res_id=product.category,10    -> account.account,1173   company=1 create=2023-09-22
   product.template   res_id=product.template,11819 -> account.account,1281   company=1 create=2024-08-13
   product.template   res_id=product.template,12033 -> account.account,1207   company=1 create=2024-11-22
   product.template   res_id=product.template,12104 -> account.account,1134   company=1 create=2025-01-04
   product.template   res_id=product.template,7960  -> account.account,1233   company=1 create=2025-10-24
   product.template   res_id=product.template,12640 -> account.account,1353   company=1 create=2026-02-27
   product.template   res_id=product.template,12770 -> account.account,1301   company=1 create=2026-07-07
```
Six **product-level** `property_account_creditor_price_difference` overrides route price differences to **six different accounts, none of which is 1173**. They were configured continuously from 2024-08-13 to **2026-07-07 — four days before the dump was taken**, so this is live, ongoing configuration activity, not legacy.

One of those destinations is **account 1281 = `9999991 Dummy Service`** — the same account that absorbs ฿211,342.14 of the Buddhist-era cash-basis entries (E2-23).

**Corrected statement:** the price-difference engine is configured, has fired 1,123 times for ฿2.25bn, and its output is systematically routed away from the designated variance account by per-product overrides — one of which points at a dummy account. That is a materially different finding from "wired and never fired", and it inverts the control conclusion: the exposure is not a dormant feature, it is an active feature with no visibility at the account it was designed to report through.

---

## 8. EVIDENCE-BASE INTEGRITY

### E2-13 — RISKY: the "frozen" evidence directory was written to during this review
```
$ stat -f '%Sm %z %N' -t '%F %T' T_*.sql | sort
2026-09-05 19:19:25  … T_stock_valuation_layer.sql, T_account_move.sql, T_stock_move.sql, …  (24 files)
2026-09-05 19:24:32  488080 T_product_product.sql
2026-09-05 19:29:33  … T_account_tax.sql, T_mrp_bom.sql, T_stock_location.sql, …            (13 files)
2026-09-05 19:29:34  … T_hr_expense.sql, T_hr_expense_sheet.sql                              (2 files)
2026-09-05 19:29:39  … T_mrp_production.sql, T_stock_move_line.sql, T_account_analytic_line.sql (3 files)
```
The brief file `brief/FINDINGS.md` is stamped 19:28. My first directory listing showed 26 `T_*.sql`; my second, minutes later, showed 41. **15 files were created after the package was frozen and after this review opened.** The package is being reviewed against a directory that at least one other party is still writing to.

Nothing I measured is invalidated: every table I used for a headline number (`stock_valuation_layer`, `account_move`, `account_move_line`, `product_*`, `ir_property`, `ir_model_fields`, `stock_move`, `account_account`) is stamped 19:19–19:24, i.e. pre-freeze, and all 41 files are single-block, column-aligned and properly terminated under the audit in §1. But **"frozen package" is not currently a true description of this directory**, and any two reviewers quoting "the evidence base" may not be quoting the same set. This should be resolved by content-hashing the package before the next round rather than by trusting the label.

### E2-24 — MISSING: the extraction is not verified against the archive TOC
`TOC.txt` lists 651 `TABLE DATA` entries; `tables.txt` has 651 lines; 41 tables are extracted (6.3%). I did **not** re-extract from `~/Downloads/iSMEs_2026-07-11_05-03-27.dump` and therefore did not verify that each `T_*.sql` matches what `pg_restore` produces today, nor that the 41 chosen tables are the right sub-population for the claims made. **This is a bounded, unfinished measurement, not a negative result.** In particular, no claim in the brief or in this report about "the whole database" is entitled to rest on a 6.3% table sample without a stated selection rule.

---

## 9. STATUS SUMMARY

### SUPPORTED
- **E2-04** Headline split **56,654 / 1,044 / 1,209 / 16,075** reproduces to the row on an independent, position-based, raise-on-missing-column instrument; coverage control 0 unresolved across all four join hops. Residual A **748 zero / 296 non-zero** also exact.
- **E2-16** `product.category.property_valuation` is the sole policy carrier (verified against `ir_model_fields`, 0 unresolved `fields_id` in all 13,331 `ir_property` rows). The denominator cannot be widened.
- **E2-05 / E2-17** The 30 extreme rows are genuine stored data, re-derived by two structurally different methods (raw string length in `awk`; ULP divisibility in `Decimal`), with a working positive control against scientific notation. 25 posted, GL balances to **0.00**. S16-04's central conclusion holds and is now measured (**฿6,462,975,089,678,637.13** unreconciled) rather than asserted.
- **E2-15** Policy-change refutation strengthened: 0 of 16 `property_valuation` rows ever rewritten, against a positive control of 2,112 of 13,331; the single method-change event is dated 2023-10-11 and moved ฿0.00.
- **E2-19 / E2-20** 5,115 reversals with 0 dangling `reversed_entry_id`; 0 orphaned journal items; the 889 account-less journal items are all `line_note`/`line_section`.
- **E2-11** Company-less quants (10,295) are entirely explained by location usage; 0 in internal locations.
- Simple populations all reproduce exactly: 183,590 moves (posted 169,143 / draft 12,581 / cancel 1,866), 447,384 journal items, 74,982 layers, 1,733 pre-2015 moves, 5,201 WHT certificates (5,191/5/5), 0 landed costs, 0 reversal-wizard rows, 10,490 PO lines, 22,468 payments, 190 installed modules (1 NULL version), `anglo_saxon_accounting = f`, all three lock dates NULL.
- **E2-02(a)** Account 1173 has **0 journal items in any state**.

### CHALLENGED
- **E2-01 (highest consequence)** The GRNI headline **฿72,097,814.25 outstanding** is an all-states figure composed entirely of 70 cancelled/draft journal items. **Posted-only net is −฿7,048,692.08** — opposite sign, order of magnitude smaller. The same missing state filter runs through every S16-05 count (1062/1068/1289/1286 item counts, and the 6,653-line / ฿4,516,394,611.47 bill-relief figure, of which ฿175,017,092.70 is on cancelled and draft bills). The comparison drawn to the series-18 OCC estate rests on the unfiltered number.
- **E2-02** *"The price-difference engine … has never fired"* is contradicted: **1,123 layers carry ฿2,246,313,274.64 of `price_diff_value`**, routed away from account 1173 by **6 unenumerated product-level overrides** to 6 other accounts, one of them "Dummy Service", the most recent configured 4 days before the dump.
- **E2-03** Residual B is the **vendor-bill price-difference population**, not a policy leak: 1,172/1,209 point at `in_invoice`, 1,194/1,209 have no stock move, 1,047/1,209 carry non-zero `price_diff_value`. The causal direction in S16-03 is reversed for 98.8% of the population.
- **E2-10** Buddhist-era leakage is **484 values across 14 columns in 11 tables**, not 30 in 1 column; plus 11 values at year **8202** (an unmentioned second corruption class) and 14 pre-1970 values.
- **E2-22** The leakage is **bidirectional**: 30 moves have a BE `date` with a correct `tax_period`; 7 moves have a BE `tax_period` with a correct `date`; 1 has a BE `invoice_date`. No column is reliably Gregorian.
- **E2-14** `unit_cost` maximum is **฿52,616,504,567,828,624**, not the ฿744,082,316,162.43 cited — understated by five orders of magnitude.
- **E2-12** The brief's stated cause of its own defect #4 is wrong. The padding branch never fires in any of the 41 files (field-count histogram single-valued everywhere); the mechanism is a silent `.get()` on an absent dict key, which the applied correction does not address as a class. And `categ_id` **exists** on the model as `store=f, related=product_id.categ_id`.

### MISSING
- **E2-06** The 5 corrective layers that reverse ฿6.46 × 10^15 of subledger value carry **no journal entry at all** — the subledger was repaired out of band. Unreported.
- **E2-07** `SUM(value)` over all 74,982 rows is **฿205,490,835.87** — the corruption near-cancels and is **invisible in aggregate**. The distortion to on-hand valuation is **−฿262,141.59**, which is float noise (one ULP), not a business balance. Unreported, and it is the answer to report-reachability.
- **E2-08** **56,596 of 57,863 linked layers (97.81%) have `account_move_line_id` NULL** — no subledger-to-journal-item traceability. Unreported.
- **E2-09** **9 layers carrying ฿9,279,784.92 point at cancelled journal entries.** Unreported.
- **E2-23** The BE-dated items land on **Input VAT ฿7,396.98, Undue VAT ฿7,396.98 and "Dummy Service" ฿211,342.14**, each netting to zero, so the trial balance still balances and the defect is invisible to the most likely control. Unreported.
- **E2-24** No verification of the 41 extracts against `pg_restore` output, and no stated selection rule for choosing 41 of 651 tables. A bounded, unfinished measurement.

### RISKY
- **E2-13** The frozen evidence directory received **15 new files during this review** (19:29 vs a 19:28 freeze). Nothing I measured is affected (all my source tables predate the freeze and are column-aligned and terminated under the §1 audit), but the package is not content-stable and two reviewers may not be quoting the same evidence base.
- **E2-18** The extreme-cost episode is bounded to 2024-08-17…2024-09-03 and the cost master is currently sane (max `standard_price` ฿750,000 across all 3,208; none ≥ ฿1e6). **Historically latent, not live** — but the corrupted layers are permanent in the subledger and the aggregate camouflage (E2-07) means no routine control would surface a recurrence.
- **E2-21** All 3,949 product templates are company-less while the 15 policy rows are company-scoped. With one company this is unambiguous and no cross-company reference exists anywhere (verified across every table with a `company_id`). Adding a second company silently re-resolves 56,654 layers' worth of behaviour to the global `manual_periodic` default with no configuration edit.
- Monetary values in this deployment are computed in float64 and stored to a monetary column. At the magnitudes reached in 2024-08 the representable granularity was **฿262,144**. The storage type is sound; the computation path is not precision-safe at scale.

### EVIDENCE REQUIRED NEXT
1. **Re-run every aggregate in S16-05 and S16-06 with an explicit `parent_state = 'posted'` predicate, and publish both figures side by side.** E2-01 shows at least six published totals change, one of them by a sign flip. This is the single highest-value next step.
2. **Characterise the 15 Residual-B layers that do have a stock move, and the 37 that point at `entry` moves.** After E2-03 removes the bill-side population, these ~52 rows are the only genuinely unexplained part of Residual B and nobody has looked at them.
3. **Trace the ฿2,246,313,274.64 of `price_diff_value` to the accounts that actually received it** — join the 1,123 layers to their `account_move_id` and enumerate the debit accounts. Establish specifically what account 1281 "Dummy Service" holds and why a price-difference override points at it. Sample the single ฿460,998,540 outlier.
4. **Content-hash the evidence package and re-extract all 41 tables from the dump**, comparing byte-for-byte, before any further round. State the selection rule for 41 of 651 tables (E2-13, E2-24).
5. **Resolve the 9 cancelled-move layers (฿9,279,784.92) and the 54 reverse-a-cancelled-move entries** — determine whether the cancellations were period-lock evasions, noting all three lock dates are NULL.
6. **Extend the BE sweep to the remaining 610 unextracted tables**, and separately investigate the 11 year-8202 values in `stock_move` and `mrp_production` — a distinct corruption class with no diagnosis at all.
7. **Determine why `account_move_line_id` is NULL on 97.81% of linked layers** — whether Odoo 16 simply does not populate it, or whether it was populated and lost. This decides whether E2-08 is a design limitation or a data-loss event, and the two have very different remediation costs.

---

## 10. PRESERVED DISAGREEMENT

I did not break the brief's central conclusions, and I want that recorded as plainly as the corrections.

The 4-way split is exact. The 30 extreme rows are real, and the GL was not corrupted — I confirmed both by structurally independent methods, and the balance check returned 0.00. The policy-change refutation is stronger than the brief argued, not weaker. Account 1173 really does hold zero items. Every simple population count reproduces to the row.

**Every material defect I found is in an aggregation predicate or an interpretation, never in a reasoning step and never in a count of things.** The brief counted rows correctly and then summed them over the wrong set (E2-01, all states rather than posted), described the wrong causal direction over a correct count (E2-03), named the wrong mechanism for a correctly identified defect (E2-12), and drew a conclusion about an engine from an observation about an account (E2-02). The instrument was sound; the population statements attached to it were not.

Where I disagree with the brief's own self-assessment: its "Method defects committed and corrected inside this run" section presents defect #4 as caught and closed. The mechanism it names never occurred, so the class is not closed, and E2-02 and E2-01 are the same class recurring — a predicate that returns a plausible number over a set nobody declared.

Two things I could not close and am not claiming: whether a valuation policy was ever set and reverted (deleted `ir_property` rows leave no trace — E2-15 narrows this, it does not eliminate it), and whether the 41 extracted tables are the right sub-population for any whole-database claim (E2-24). Both are unfinished measurements, not negative results.
