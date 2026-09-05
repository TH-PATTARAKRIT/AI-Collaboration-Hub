# CLOSE_2 — AAS-03 Expert 2 (Leadership Database Design)
Targeted challenge on CLOSURE.md (baseline `a02ec8b`). READ-ONLY. Two assignments only.
Evidence: `s16/T_*.sql`, `s16/schema_full.sql`, `s16/src/`, archive `~/Downloads/iSMEs_2026-07-11_05-03-27.dump`.

---

## ASSIGNMENT 1 — C-5 COUNT RECONCILIATION

### Verdict: arithmetic **SUPPORTED**; interpretation **CHALLENGED** (materially wrong)

**Arithmetic reproduces exactly.** Independent parse of `T_stock_valuation_layer.sql`
(`stream.py`, no reuse of the package's numbers):

```
TOTAL LAYERS: 74982
price_diff_value IS NOT NULL: 1267
  == 0.00 : 144
  != 0.00 : 1123 (of which negative: 123)
NULL: 73715
unparseable: {}
```

1,267 / 1,123 / 144 / 74,982 all confirmed. **No DB default** on the column
(`schema_full.sql:68782`: `price_diff_value double precision,` — no `DEFAULT`, no `ALTER … SET DEFAULT`),
so NOT NULL does mean application code wrote a value. The table in C-5 is correct as far as it goes.

### CHALLENGED: "144 layers where the engine ran and produced exactly ฿0.00"

That gloss is falsified by the engine's own source and by the rows.

`src/stock_account/models/account_move.py:360-362` — the engine **refuses to create a layer at all**
when the correction is nil:

```python
unit_valuation_difference = price_unit - layers_price_unit[layer]
if float_is_zero(unit_valuation_difference * qty_to_correct, precision_rounding=self.company_id.currency_id.rounding):
    continue
```

`layers_to_correct[layer]` is assigned only *after* that guard, and `_prepare_in_invoice_svl_vals`
iterates only `layers_correction`. **By construction no SVL row can exist with a zero correction.**

Confirmed in data — and with a positive control that the predicate can fire:

```
of the 1267 price-diff layers, value==0.00 on 0
POSITIVE CONTROL: layers with value==0.00 anywhere in the 74,982 population: 3865
```

The 144 carry real money:

```
144 zero-price_diff layers: sum(value) = -5,957,842.04   abs-sum = 12,764,989.32
   min=-4,703,359.50  max=923,692.00
144 zero rows value field: {'value!=0': 144}
```

**The two columns measure different deltas** (`account_move.py:363-365`):
- `value` ← `unit_valuation_difference = price_unit − layers_price_unit[layer]` → **bill price vs the
  receipt layer's own recorded unit cost**
- `price_diff_value` ← `price_difference_curr = po_pu_curr − self._get_gross_unit_price()` → **PO price
  vs bill gross price**, in invoice currency

So `price_diff_value = 0` means *the bill agreed with the PO*. It does **not** mean the engine produced
nothing. On all 144 the bill matched the PO **and the receipt layer was still valued at a different unit
cost** — ฿12,764,989.32 of absolute inventory-value correction, net −฿5,957,842.04, posted with
`account_move_id`, `account_move_line_id` and `stock_valuation_layer_id` all SET and `stock_move_id` NULL
on 144 of 144.

**FX is excluded as the explanation** (this was the obvious alternative):

```
distinct account_move_id: zero-group 128  nonzero-group 644  overlap 0
zero-group move currency:    {('132','THB'): 127, ('1','EUR'): 1}
nonzero-group move currency: {('132','THB'): 644}
company id=1 currency_id=132      # res_currency 132 = THB ฿
```

771 of 772 moves are billed in the company's own currency, so `value` and `price_diff_value` are both
THB and diverge for a **structural** reason, not a conversion one.

**Why this matters to C-2, not just to C-5.** The 144 are the population where billing was correct and
**valuation was wrong** — the exact signature of the C-2 cost-explosion root cause
(`purchase_stock/.../_get_price_unit`). C-5 files them as the benign residue. They are the diagnostic
subset. The same divergence appears at scale inside the 1,123:

```
 id=27396 value=-496,791,493,239,011,648.00  price_diff_value=949,239,810
 id=27395 value=-437,690,355,155,325,440.00  price_diff_value=836,312,850
 id=27193 value=-10,954,387,437.50           price_diff_value=460,998,540
 count |value|>1e9 : 3      (sum(value) over the 1,123 = -9.34e17)
```

Opposite sign, ~9 orders of magnitude apart, same currency.

**Requested correction to C-5 (arithmetic unchanged):** replace *"144 layers where the engine ran and
produced exactly ฿0.00"* with *"144 layers where the PO-vs-bill price delta was ฿0.00 while the
bill-vs-layer valuation delta was not — ฿12,764,989.32 absolute, net −฿5,957,842.04 of inventory value
corrected on bills that matched their PO exactly."* And add a fourth column to the C-5 table: `value`,
which is non-zero on 1,267 of 1,267.

---

## ASSIGNMENT 2 — C-9 HONESTY ABOUT ITS OWN LIMITS

### Verdict: **RISKY**. C-9 discloses the 6.3% correctly but understates it as a bound on *negatives*.
### At least two unextracted tables bear on *surviving positive* C-2 conclusions.

C-9 says "Every negative is bounded by this." True but too narrow. The tables below are unopened and
would test **claims C-2 asserts affirmatively**. Row counts are from the archive, extracted now:

**Positive control for these counts** — the extractor distinguishes *absent* from *empty*:
`stock_valuation_adjustment_lines` → `COPYhdr=1 rows=0` (exists, empty);
`account_move_line_purchase_line_rel` → `COPYhdr=0 rows=0` (does not exist).
A row count below is therefore a measured population, not a tool artefact.

| Unextracted table | Rows | Which C-2 claim it tests | What it would test |
|---|---|---|---|
| **`mail_tracking_value`** | **571,522** | "Correction is immutable reversal: 5,115 pairs"; "No period lock of any kind on 169,143 posted entries"; "฿21,556,228.06 posted **after** it was zeroed" | The only field-level change log in the estate. Tracked `field_desc` histogram includes **Number 54,143**, **Date 42,202**, **Untaxed Amount 42,049**, **Account 5,955**, **Label 3,084**. A tracked change to `Number` or `Date` on an entry already `posted` is a direct counter-example to "immutable reversal" and to "no lock of any kind" — and is the *only* way to date the `WHT3%` zeroing event rather than infer it. C-2 asserts a temporal ordering ("posted after it was zeroed") from a table that does not record when the zeroing happened. |
| **`account_fiscal_year`** | **4** | "**No period lock of any kind** on 169,143 posted entries" | Not empty. `Y2023-2024` (2023-10-01→2024-09-30), `Y2024-2025`, `งบเพิ่มเติม 25` (2025-10-01→2025-12-31), `Y2026`. C-2's negative was drawn from `res_company` lock-date fields only. "Of any kind" is a universal claim over a population that was never enumerated; a defined fiscal-year structure is a second locking surface that was not looked at. |
| `res_currency_rate` / `res_currency` | 2,039 / 167 | C-5, C-4 inverted-exposure | Retired as an explanation by my Assignment-1 test (771/772 moves are THB), but only because I ran it. The package could not have known this without opening them. `ir_config_parameter` also shows a custom live-rate feed, **`scgl_currency_rate_live.bot_client_id`** — a non-standard writer into rates that nobody has enumerated. |
| `ir_model_data` | 107,873 | C-4 ("the only `product.category` configuring 1173 is category 10"); C-6 | Resolves which module owns each configured record. C-4's "only" is an enumeration over `ir_property` + `product_category`; `ir_model_data` is how you check whether a module re-creates or re-points that configuration on upgrade. |
| `stock_valuation_adjustment_lines` | **0** | C-2 receipt→valuation coverage | Genuinely empty — landed cost is not a competing writer here. Reported so the negative is on the record with its control. |

**The strongest single argument against freezing** is `mail_tracking_value` at 571,522 rows. Three
surviving C-2 conclusions — immutability of correction, absence of any period lock, and the *after*
in the WHT finding — are claims about **what happened to records over time**, and the estate's only
record of what happened to records over time has never been opened in six rounds. This is not a
bounded negative; it is an affirmative claim resting on an unexamined authority.

Note also that C-9's own framing collides with the package's method control C-8: C-8 establishes that a
non-writer can change behaviour, which *widens* what must be enumerated, while C-9 bounds only negatives.

---

## STATE

| Item | State |
|---|---|
| C-5 counts 1,267 / 1,123 / 144 / 74,982 | **SUPPORTED** — reproduced independently |
| C-5 "the engine ran and produced exactly ฿0.00" | **CHALLENGED** — falsified by `account_move.py:360-362` guard and by 144/144 `value != 0` |
| C-5 completeness (`value` column absent from the table) | **MISSING** |
| C-9 disclosure of 6.3% | **SUPPORTED** as disclosed |
| C-9 "every negative is bounded by this" as a sufficient limit | **RISKY** — understates; positives are bounded too |
| C-2 "no period lock of any kind" | **CHALLENGED** — `account_fiscal_year` has 4 rows, never enumerated |
| C-2 "posted after it was zeroed" (WHT) | **EVIDENCE NEEDED NEXT** — no artefact in the extracted 41 dates the zeroing |
| C-2 "correction is immutable reversal" | **EVIDENCE NEEDED NEXT** — untested against 571,522 tracking rows |

## EVIDENCE NEEDED NEXT (ordered, all cheap)
1. Extract `mail_tracking_value` + `mail_message` (`mail_message` supplies `model`/`res_id`); join to the
   169,143 posted `account_move` ids and filter `field_desc` in (`Number`,`Date`,`Account`,`Label`,
   `Untaxed Amount`). Any hit with `create_date` > the move's posting date falsifies two C-2 claims.
2. From the same table, isolate the `WHT3%` rate record's value change and read its date and `create_uid`.
   This either evidences or withdraws the word "after" in C-2.
3. Reconcile `account_fiscal_year` (4 rows) against `res_company` lock dates before restating
   "no period lock of any kind".
4. Restate C-5 with the `value` column and reclassify the 144 as the bill-correct/valuation-wrong subset
   of the C-2 cost-explosion population.
5. State a selection rule for `GAP-P01-07` — 41 of 651 with no rule cannot be audited for what it omits.

## COMMANDS RUN (reproducible)
```
python3 stream.py-based counts over s16/T_stock_valuation_layer.sql   # C-5 counts, currency join, controls
awk '/^CREATE TABLE public.stock_valuation_layer /,/^\);/' s16/schema_full.sql
grep -n "price_diff" s16/schema_full.sql
sed -n '330,410p' s16/src/stock_account/models/account_move.py
/opt/homebrew/opt/postgresql@18/bin/pg_restore -t <t> --data-only -f /tmp/X_<t>.sql \
    ~/Downloads/iSMEs_2026-07-11_05-03-27.dump      # t in: res_currency res_currency_rate
    # ir_config_parameter stock_valuation_adjustment_lines account_fiscal_year mail_tracking_value
    # ir_model_data account_tax_repartition_line account_move_line_purchase_line_rel
awk '/FROM stdin;/{f=1;next} /^\\\.$/{f=0} f' /tmp/X_<t>.sql | wc -l
```
No file in `s16/` was modified. Extractions written to `/tmp/X_*.sql` only.
