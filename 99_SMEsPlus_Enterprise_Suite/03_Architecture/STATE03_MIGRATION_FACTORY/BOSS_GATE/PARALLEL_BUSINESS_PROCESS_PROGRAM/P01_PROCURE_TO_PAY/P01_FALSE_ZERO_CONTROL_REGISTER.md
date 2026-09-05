# P01 — FALSE-ZERO CONTROL REGISTER

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-11`

Governing rule: **a well-formed zero is not self-authenticating evidence.** Every zero this run
publishes carries a positive control — a query proving the same instrument can return non-zero —
and, where the zero is load-bearing, a second, structurally different derivation.

---

## 1. TOOL AND EXTRACTION CAPABILITY

| Item | Value |
|---|---|
| Archive | `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`, CUSTOM, dump version 1.16-0 |
| Restore binary used | `/opt/homebrew/opt/postgresql@18/bin/pg_restore` — **18.6** |
| Other binary present | `/opt/homebrew/opt/postgresql@16/bin/pg_restore` — 16.15 (**cannot read format 1.16**) |
| Extraction | `pg_restore -t <table> --data-only -f <outfile> <dump>` |
| Known failure | **piping** the restore output yields **0 bytes** — always write to a file |
| Producer | pg_dump **17.9**, which quotes reserved column names (`"json_value"` in `ir_default`) |
| Parser | `s18/pgc.py` — strips quotes from every column name, maps `\N` to NULL, unescapes `\t \n \r \\` |

The 16-series binary is recorded so no future round repeats `ERR-P01-15`: **enumerate the
instruments present, not the one that failed.**

---

## 2. EVERY ZERO PUBLISHED THIS RUN, WITH ITS CONTROL

| # | Zero claimed | Query / unit | Positive control | Second derivation |
|---|---|---|---|---|
| Z1 | `stock_valuation_layer.account_move_id` non-null = **0 / 47,801** | one SVL row | same parse, same rows: `stock_move_id` non-null **44,935**, `company_id` **47,801**, `product_id` **47,801** | **synthetic injection** — §3 |
| Z2 | `stock_valuation_layer.account_move_line_id` non-null = **0 / 47,801** | one SVL row | as Z1 | — |
| Z3 | Journal items on accounts 176 / 62 / 100 / 138 = **0 each** | one `account_move_line` row, population 40,353 | same counter: **144** distinct accounts appear; 186 → 4,049; 211 → 3,522; 169 → 2,940; 343 → 2,408 | account 169 returns 2,940 from the identical expression |
| Z4 | Journal items in journals 16 / 24 / 32 / 40 (`STJ`) = **0 each** | one `account_move_line` row | same counter: journal 45 → 8,226; 33 → 7,707; 9 → 4,504; 34 → 4,202 | — |
| Z5 | Journal entries with `accru` in `ref` = **0 / 15,522** | one `account_move` row | **15,434 of 15,522** have a non-empty `ref`, and their content is legible — the `v14 …` migration markers were read from this same field | — |
| Z6 | `property_valuation` jsonb set = **0 / 126** categories | one `product_category` row | same parse, same rows: `property_stock_account_input_categ_id` set on **15**, `property_account_expense_categ_id` set on **30–32** per company | `ir_default` read independently — one global row, `"manual_periodic"` |
| Z7 | `property_stock_journal` jsonb set = **0 / 126** | one `product_category` row | as Z6 | `ir_default` returns four company rows (16/24/32/40) |
| Z8 | `price_diff_value` non-zero = **0 / 47,801** | one SVL row | as Z1 | — |
| Z9 | Vendor bill lines posting to a valuation or clearing account = **0 / 3,375** | one bill product line | same counter: 186 → 1,062; 72 → 966; 287 → 345; 414 → 224 | account-type histogram over the same lines returns 8 non-zero types |
| Z10 | Companies 3 and 4: `account_move` = **0**, `stock_valuation_layer` = **0** | one row | same counters return 9,733 / 5,789 and 25,978 / 21,823 for companies 1 and 2 | — |
| Z11 | Bills posted in a different month from `invoice_date` = **0 / 1,879** | one posted bill | the same comparison returns **1,667** differing at day granularity | day-of-month histogram: 1,747 on month-end, 124 on day 25 |
| Z12 | `ir_property` table = **absent** | one TABLE definition, population 1,122 | the same TOC listing returns 1,122 present tables, including all 27 P2P tables sought | `grep -E "TABLE public (ir_property\|stock_landed_cost)"` returns nothing while `grep -c " TABLE public "` returns 1,122 |
| Z13 | `stock_landed_cost*` tables = **absent** | as Z12 | as Z12 | — |
| Z14 | `purchase_request` source copy at `18.0.1.10.0` = **0 of 16 copies** | one module directory | the same sweep returns 16 copies and **7 distinct** version strings | — |

---

## 3. SYNTHETIC INJECTION CONTROL ON THE LOAD-BEARING ZERO

Z1 is the zero this entire run turns on. A positive control on *neighbouring columns* proves the
parse works; it does not prove that **that column** would register a value if one existed.

**Control performed.** In memory, one parsed row's `account_move_id` was set to a non-null value
and the same counting expression re-run:

```
account_move_id non-null: 0
SYNTHETIC INJECTION -> non-null account_move_id now: 1
```

The predicate can fire. **The zero is a measurement, not a silence.** No database was written to;
the injection was applied to the parsed in-memory structure only.

---

## 4. FALSE ZERO CAUGHT INSIDE THIS RUN — `NEAR-MISS-P01-05`

**What happened.** `scgl_product_category_company_rel` was queried with assumed column names
`product_category_id` and `res_company_id`. The aggregate returned a clean, well-formed
`Counter()` — zero rows by company, and "0 categories scoped" would have followed.

**The truth.** The real columns are `category_id` and `company_id`. The table holds **32 rows
covering 16 categories across 4 companies.**

**Why it was caught.** The row count (`rows: 32`) was printed **beside** the aggregate. The
aggregate said zero; the count said 32; the contradiction was visible in one line of output.

**The consequence had it not been caught.** The finding in
`P01_S18_RECEIPT_VALUATION_ACCOUNTING_TRACE.md §6` would have read *"no category carries any
company scope"* instead of *"110 of 126 carry none"* — a stronger claim, in the same direction,
and wrong.

**Rule adopted.** Never publish an aggregate without the row count of the set it aggregates over,
in the same output. A key-error zero and a real zero are indistinguishable in the aggregate alone,
and only the second is evidence.

---

## 4A. THE DEFECT CLASS IS WIDER THAN §4 STATED — AND THE RUN'S OWN COUNT OF IT WAS 1 OF 4

§4 records **one** false zero, from wrong **column** names. AAS-03 Expert B, auditing the evidence
base rather than the findings, found that the same run produced **four** zero-yielding extracts from
wrong names, at **two** levels, and **detected none of them at the time**.

### 4A.1 The discriminator that was available all along

A `pg_restore -t <name>` whose pattern matches nothing writes a **718-byte shell** — header plus the
`\restrict`/`\unrestrict` tokens, **no `COPY` block at all**. A table that exists and holds zero
rows writes a **COPY block with its full column list and no data lines**. These are trivially
distinguishable, and this run contains **seven** natural positive controls of the second kind:
`account_accrued_orders_wizard` (12 columns, 0 rows), `account_automatic_entry_wizard` (12/0),
`account_journal_account_reconcile_model_rel` (2/0), `account_transfer_model` (12/0),
`account_transfer_model_line` (9/0), `create_withholding_tax_cert` (9/0),
`withholding_tax_report` (10/0).

> **718 bytes with no COPY block ⟺ the `-t` name matched nothing.**
> **It never means "the table is empty."** Byte size alone reports both identically — which is the
> fourth evidence-defect class: *a control that cannot detect its own failure*.

### 4A.2 The four wrong names

| Attempted name | Reality | Detected at the time? |
|---|---|---|
| `product_category_company_rel` | does not exist; the real table is **`scgl_product_category_company_rel`** (TOC 1818) | **no** — it was retried under the right name for an unrelated reason, then hit the **column**-name error of §4 |
| `account_transfer_model_account_account_rel` | does not exist. The real relation tables are `account_analytic_account_account_transfer_model_line_rel` and `account_transfer_model_line_res_partner_rel` | **no** |
| `account_transfer_model_line_account_analytic_account_rel` | does not exist — same two real names | **no** |
| `stock_landed_cost` | does not exist — **and here the zero was the right answer** | the absence was separately confirmed against the TOC |

The two transfer-model misses share a cause worth recording: **the ORM builds many-to-many relation
table names by joining the two sides alphabetically**, and both guesses had the sides in the wrong
order. A guessed relation-table name is a guess about an ordering rule, not a name.

### 4A.3 What this changes

**No published claim is falsified by any of it** — nothing in this package rests on the two
transfer-model extracts, and `T_pcrel.sql`'s successor was read correctly. But:

- the **same table** was missed twice, first by a wrong table name and then by wrong column names,
  and the first miss was never recorded;
- the defect class in §4 is **wrong-name-at-two-levels**, not wrong-column-names;
- **the run's own count of its false zeros was 1 where the artefacts show 4.** A register that
  undercounts its own defect class by four-fold is itself a finding.

**Rule adopted.** After every extraction, assert the presence of a `COPY` block — not a non-zero
byte count. An extract with no COPY block is a **failed name match** and must be re-attempted or
recorded as such, never carried forward as a zero.

## 4B. TWO LATENT DEFECTS IN THE PARSER THE WHOLE EVIDENCE BASE DEPENDS ON

Both found by Expert B in `pgc.py`. **Both measured as not having fired in this run**; both are
silent by construction, which is the point.

1. **Silent field-count repair.** `if len(vals) != len(cols): vals = (vals + [None]*len(cols))[:len(cols)]`
   pads a short row with `None` and truncates a long one, with no counter, no warning and nothing
   the caller can inspect. **A padded row is indistinguishable from a row of genuine NULLs** — which
   is exactly the shape of every negative in this package. *Measured: **0 rows across all 59 COPY
   blocks** hit this branch, so no published count is affected.* The risk is structural: the
   instrument cannot report its own failure.
2. **Unescape order corrupts literal backslashes.** The chain
   `.replace('\\t','\t').replace('\\n','\n').replace('\\r','\r').replace('\\\\','\\')`
   decodes the doubled backslash **last**. A value holding a real backslash followed by `n` is
   emitted by COPY as three characters, and the first replacement consumes the wrong pair. This
   cannot change a field **count**, so no row count is affected — but it can change field
   **content**, and this package reads jsonb text out of `product_category` and description strings
   out of `stock_valuation_layer`. *Not measured as fired.*

**Both are recorded rather than fixed**, because changing the parser mid-run would invalidate every
count already taken against it. The fix belongs to the next round, together with a re-run.

## 4C. A REPRODUCIBILITY CONTROL THE RUN DID NOT CLAIM

Expert B extracted several tables a second time, independently. `T_account_move_line.sql` and its
re-extraction are both **18,155,413 bytes**; the `ir_model_data` pair both **27,914,048**; the three
`ir_model_fields` copies all **5,961,660**. Each pair parses to identical row and column counts. The
**only** per-file difference is pg_restore 18's random `\restrict` session token, which differs on
every invocation.

**The same table extracted twice from the same archive yields the same data both times.** Modest,
but it is a real control on the extraction step and it had not been claimed.

## 4D. THE ARCHIVE DENOMINATOR RECONCILES TO THE ARCHIVE'S OWN HEADER

`TOC.txt` declares `TOC Entries: 23232`. Enumerated by entry type: COMMENT 11,064 · FK CONSTRAINT
4,227 · CONSTRAINT 1,272 · INDEX 1,263 · **TABLE DATA 1,122** · **TABLE 1,122** · SEQUENCE SET 825 ·
SEQUENCE 825 · DEFAULT 736 · SEQUENCE OWNED BY 731 · VIEW 26 · RULE 11 · TEXT SEARCH DICTIONARY 1 ·
TEXT SEARCH CONFIGURATION 1 · EXTENSION 1 · ACL 1 = **23,228 printed**. The 4-entry gap is
pg_restore's non-printed internal entries (ENCODING, STDSTRINGS, SEARCHPATH, and the archive header),
which `-l` counts but does not list.

**`TABLE = TABLE DATA = 1,122` exactly**, and `tables.txt` holds 1,122 lines. `MATERIALIZED VIEW`
count is **0**, so no data hides behind a matview. The denominator used for every bounded absence in
this package reconciles to the archive's own header.

## 5. LIMITS OF THE VERSION INSTRUMENT

`ir_module_module.latest_version` is the only stored version instrument in an Odoo-lineage
database. Its known limits:

- it records the version of the module **as last installed or updated**, which is not necessarily
  the version of the code **currently on disk** at the deployment;
- a database restored into a different codebase carries the old value until a module update runs;
- it cannot distinguish two builds sharing a version string.

Disproving the series-18 identity — including attacking this instrument directly — was issued as a
primary disproof assignment to AAS-03 Expert B. The outcome is recorded in
`P01_S18_AAS03_FRESH_CHALLENGE.md`. Until then the identity is `FACT VERIFIED` **with the
instrument's limits stated**, which is not the same as unconditional.

---

## 6. NULL vs EMPTY vs `false` vs ABSENT-ROW

Four states are distinguished throughout and are not merged:

| State | Example in this run | Meaning |
|---|---|---|
| Column NULL | `property_valuation` jsonb on 126/126 categories | no per-record override; resolution falls through to `ir_default` |
| `ir_default` row with value `false` | `property_stock_account_input_categ_id`, companies 2 and 3 | **deliberately un-set** at company level |
| `ir_default` row absent | same field, company 4 | never configured |
| Value present | same field, company 1 → 176 | configured |

Companies 2, 3 and 4 have the **same effect** for the 111 unconfigured categories and **different
provenance**. Reporting them identically would erase evidence about intent.

---

## 7. A FALSE **POSITIVE**, RECORDED FOR SYMMETRY — `NEAR-MISS-P01-06`

The controls in this register defend against zeros. This run also produced a non-zero that was
wrong in the other direction, and it is registered here because the class is the same.

**Candidate:** 1,667 of 1,879 posted vendor bills have `date != invoice_date`, median +13 days,
max +30, never negative — read as systematic late posting and a cutoff risk.

**Discriminating test:** re-express at month granularity and at day-of-month. **0 of 1,879** cross
a month boundary; **1,747 of 1,879** carry a month-end accounting date.

**Result:** a month-end posting convention. The candidate finding was **withdrawn before
publication.**

**Rule:** a difference statistic needs the unit its *claim* is about. The claim was about periods;
the statistic was in days. Aggregate direction is not evidence of the thing the aggregate is
being used to argue.

---

## 8. RESIDUAL RISK

| Risk | Status |
|---|---|
| A zero produced by a `-t` pattern matching the wrong table, or by a partitioned table | Assigned to AAS-03 Expert B; each `T_*.sql` file's parsed row count is to be reconciled against its own COPY block |
| Per-artefact extraction completeness (a loop silently processing a subset) | Assigned to Expert B, reported **per artefact**, not in aggregate |
| A second writer of `stock_valuation_layer.account_move_id` that this run did not enumerate | Assigned to Expert A |
| The estate census remaining incomplete (six identities is a **floor**) | Open — see `P01_POPULATION_SELECTION_METHOD_AUDIT.md §3` |
