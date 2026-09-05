# EXPERT B — LEADERSHIP DATABASE DESIGN — ADVERSARIAL CHALLENGE OF THE S18 EVIDENCE BASE

Role scope: **the evidence base, not the findings.** Read-only. No database written, no source
modified, no Odoo server run, nothing installed.

Status: COMPLETE. All three assignments executed. Written incrementally (Assignment 3 first, then 1,
then 2) so partial results would survive an interruption. Consolidated position at the end.

---

## ASSIGNMENT 3 — EXTRACTION COMPLETENESS, PER ARTEFACT

### Declared scope of this audit
- **POPULATION**: every `.sql` extract artefact reachable from the evidence base.
- **PATH SET**: `<s18>/*.sql` **and** `<s18>/../idemo_*.sql`. Both globs declared, both executed.
- **PATTERN**: `^COPY public\.("?)([A-Za-z0-9_]+)\1 \((.*)\) FROM stdin;` — the same regex `pgc.py`
  uses, so the audit sees exactly what the parser sees.
- **UNIT**: one COPY block (not one file). A file may carry 0, 1 or many blocks; reporting per file
  would have hidden the 5 files that carry none.
- **ENUMERATED**: 64 files. **REPORTED**: 64 files / 59 COPY blocks. 64 = 59 + 5 zero-block files.
  The script prints its own enumeration count and its own block count so the two can be reconciled
  (`FILE COUNT ENUMERATED: 64` … `BLOCKS REPORTED: 59  FILES ENUMERATED: 64`).

Command: `/usr/bin/python3 expB/audit3.py` (script at `<s18>/expB/audit3.py`).
It re-derives, per block: raw data-line count between `COPY …` and `\.`; the count `pgc.load()`
returns; the declared column count; and how many raw lines have a field count != the column count.

### Result — every block reconciles

| metric | result |
|---|---|
| blocks where `RAWLINES != PARSED` | **0 of 59** |
| rows where field count != column count (`BADFLD`) | **0** across all 59 blocks |
| blocks whose `MAXFLD` or `MINFLD` differs from `NCOL` | **0 of 59** (excluding the 7 empty blocks, where both are 0 by construction) |
| blocks with an unterminated COPY (i.e. truncated at EOF) | **0 of 59** |
| files lacking pg_restore's closing `\unrestrict` trailer | **0 of 64** |

The `\unrestrict <token>` line is the last thing `pg_restore -f` writes. Every one of the 64 files
has it (`tail -c 200` on each). A file truncated mid-COPY could not carry that trailer. Combined
with 59/59 terminated `\.` markers, **no artefact in this evidence base was silently truncated.**

Per-block table (`RAWLINES` = lines in the file's own COPY block; `PARSED` = rows `pgc.load` returns):

```
A_account_account.sql            account_account                        658    658  17col  0 bad
A_account_move.sql               account_move                        15,522 15,522  95col  0 bad
A_account_tax.sql                account_tax                             80     80  25col  0 bad
A_account_tax_purchase_order_line_rel.sql  ..._rel                   13,191 13,191   2col  0 bad
A_ir_default.sql                 ir_default                              54     54  10col  0 bad
A_ir_model_data.sql              ir_model_data                      225,529 225,529 11col  0 bad
A_ir_model_fields.sql            ir_model_fields                     19,431 19,431  46col  0 bad
A_ir_module_module.sql           ir_module_module                     1,369  1,369  31col  0 bad
A_product_product.sql            product_product                      3,724  3,724  15col  0 bad
A_res_company.sql                res_company                              4      4 204col  0 bad
A_sel.sql                        ir_model_fields_selection            3,503  3,503   9col  0 bad
A_stock_location.sql             stock_location                          86     86  27col  0 bad
A_stock_valuation_layer.sql      stock_valuation_layer               47,801 47,801  20col  0 bad
C_account_accrued_orders_wizard.sql        (same)                        0      0  12col  0 bad
C_account_automatic_entry_wizard.sql       (same)                        0      0  12col  0 bad
C_account_journal_account_reconcile_model_rel.sql (same)                  0      0   2col  0 bad
C_account_reconcile_model.sql    account_reconcile_model                 16     16  34col  0 bad
C_account_reconcile_model_line.sql (same)                                 8      8  16col  0 bad
C_account_transfer_model.sql     account_transfer_model                   0      0  12col  0 bad
C_account_transfer_model_account_account_rel.sql   *** NO COPY BLOCK ***
C_account_transfer_model_line.sql account_transfer_model_line              0      0   9col  0 bad
C_account_transfer_model_line_account_analytic_account_rel.sql *** NO COPY BLOCK ***
C_account_withholding_tax.sql    account_withholding_tax                 40     40  12col  0 bad
C_create_withholding_tax_cert.sql (same)                                  0      0   9col  0 bad
C_ir_act_window.sql              ir_act_window                          905    905  24col  0 bad
C_ir_cron.sql                    ir_cron                                 66     66  16col  0 bad
C_ir_model_data.sql              ir_model_data                      225,529 225,529 11col  0 bad
C_ir_model_fields.sql            ir_model_fields                     19,431 19,431  46col  0 bad
C_mrp_production.sql             mrp_production                       5,549  5,549  41col  0 bad
C_res_groups.sql                 res_groups                             139    139  11col  0 bad
C_res_groups_users_rel.sql       res_groups_users_rel                 2,472  2,472   2col  0 bad
C_stock_landed_cost.sql                            *** NO COPY BLOCK ***
C_withholding_tax_cert.sql       withholding_tax_cert                   332    332  21col  0 bad
C_withholding_tax_cert_line.sql  withholding_tax_cert_line              348    348  14col  0 bad
C_withholding_tax_report.sql     withholding_tax_report                   0      0  10col  0 bad
T_account_full_reconcile.sql     account_full_reconcile               2,343  2,343   6col  0 bad
T_account_journal.sql            account_journal                         60     60  33col  0 bad
T_account_move_line.sql          account_move_line                   40,353 40,353  64col  0 bad
T_account_partial_reconcile.sql  account_partial_reconcile            5,071  5,071  16col  0 bad
T_account_payment.sql            account_payment                      3,508  3,508  35col  0 bad
T_ir_config_parameter.sql        ir_config_parameter                     56     56   7col  0 bad
T_pcrel.sql                                        *** NO COPY BLOCK ***
T_product_category.sql           product_category                       126    126  29col  0 bad
T_product_template.sql           product_template                     3,724  3,724  70col  0 bad
T_purchase_order.sql             purchase_order                      13,887 13,887  41col  0 bad
T_purchase_order_line.sql        purchase_order_line                 21,102 21,102  39col  0 bad
T_purchase_request.sql           purchase_request                     1,043  1,043  17col  0 bad
T_purchase_request_line.sql      purchase_request_line                3,398  3,398  30col  0 bad
T_res_users.sql                  res_users                               47     47  33col  0 bad
T_scglrel.sql                    scgl_product_category_company_rel       32     32   2col  0 bad
T_stock_move.sql                 stock_move                          51,081 51,081  65col  0 bad
T_stock_picking.sql              stock_picking                       11,663 11,663  39col  0 bad
T_stock_picking_type.sql         stock_picking_type                      48     48  52col  0 bad
T_stock_quant.sql                stock_quant                          2,462  2,462  21col  0 bad
X_aml.sql                        account_move_line                   40,353 40,353  64col  0 bad
../idemo_account_move.sql        account_move                        15,522 15,522  95col  0 bad
../idemo_acct.sql                account_account                        658    658  17col  0 bad
../idemo_ir_default.sql          ir_default                              54     54  10col  0 bad
../idemo_ir_property.sql                           *** NO COPY BLOCK ***
../idemo_irmf.sql                ir_model_fields                     19,431 19,431  46col  0 bad
../idemo_mods.sql                ir_module_module                     1,369  1,369  31col  0 bad
../idemo_product_category.sql    product_category                       126    126  29col  0 bad
../idemo_res_company.sql         res_company                              4      4 204col  0 bad
../idemo_stock_valuation_layer.sql stock_valuation_layer             47,801 47,801  20col  0 bad
```

### B-3.1 — CHALLENGED: five artefacts are 718-byte shells, and two of them name tables that do not exist

Five files carry **no COPY block at all** and are byte-identical in structure (718 bytes, header +
`\restrict`/`\unrestrict` only, no `COPY`, no `\.`):

```
C_account_transfer_model_account_account_rel.sql               718
C_account_transfer_model_line_account_analytic_account_rel.sql 718
C_stock_landed_cost.sql                                        718
T_pcrel.sql                                                    718
../idemo_ir_property.sql                                       718
```

**The discriminator, and it is available in-run.** A table that exists in the archive but holds zero
rows does NOT produce a 718-byte shell — it produces a COPY block with the column list and no data
lines. This run contains **seven** natural positive controls of exactly that:
`account_accrued_orders_wizard` (12 cols, 0 rows), `account_automatic_entry_wizard` (12/0),
`account_journal_account_reconcile_model_rel` (2/0), `account_transfer_model` (12/0),
`account_transfer_model_line` (9/0), `create_withholding_tax_cert` (9/0),
`withholding_tax_report` (10/0). Therefore:

> **718 bytes / no COPY block ⟺ the `-t` name matched nothing in the archive.**
> It never means "the table is empty." The two are distinguishable and the run had the evidence to
> distinguish them.

Checked against the archive TOC (POPULATION: the 1,122 `TABLE public …` definitions and the 1,122
`TABLE DATA public …` entries in `TOC.txt`; PATTERN: `grep -E 'TABLE public [a-z_]*<stem>[a-z_]*'`,
substring, case-insensitive where noted):

- `account_transfer_model_account_account_rel` — **does not exist.** The transfer-model relation
  tables that DO exist are `account_analytic_account_account_transfer_model_line_rel` (TOC 291 /
  TABLE DATA 17896) and `account_transfer_model_line_res_partner_rel` (TOC 507 / TABLE DATA 18112).
  Neither was extracted.
- `account_transfer_model_line_account_analytic_account_rel` — **does not exist.** Same two real
  names as above. Odoo builds m2m relation table names by joining the two sides *alphabetically*;
  both attempted names have the sides in the wrong order, which is why both missed.
- `product_category_company_rel` (`T_pcrel.sql`) — **does not exist**; the real table is
  `scgl_product_category_company_rel` (TOC 1818 / TABLE DATA 15312), later extracted successfully as
  `T_scglrel.sql` (32 rows).
- `stock_landed_cost` — **does not exist.** `grep -in 'landed' TOC.txt` returns exactly one line, and
  it is a COMMENT on `res_config_settings.module_stock_landed_costs`, not a table.
  → the brief's bounded absence at S18 "Bounded absences" is **SUPPORTED**.
- `ir_property` — **does not exist.** `grep -in 'ir_propert' TOC.txt` returns nothing at all.
  → the brief's bounded absence is **SUPPORTED**.

**Consequence for the brief.** No *published* claim rests on the two transfer-model shells or on
`T_pcrel.sql`, so nothing in FINDINGS.md is falsified by this. But the run generated three
zero-yielding extracts from mistyped table names and **did not detect any of them**. S18-13 records
one false zero (wrong *column* names on the scgl rel table); it does not record that the same table
was also first missed by a wrong *table* name, nor that two transfer-model relation tables were
missed the same way and never re-attempted. The defect class in S18-13 is therefore **wider than the
brief states**: it is wrong-name-at-two-levels, and the run's own count of it is 1 where the artefacts
show 4.

### B-3.2 — RISKY: `pgc.py` has two latent defects that did not fire here

Both are in the parser the whole evidence base depends on. Neither changed any number in this run —
I measured that — but both are silent by construction.

1. **Silent field-count repair.** `pgc.py` lines: `if len(vals) != len(cols): vals = (vals +
   [None]*len(cols))[:len(cols)]`. A short row is padded with `None` and a long row is truncated,
   with no counter, no warning and no return value the caller can inspect. A padded row is
   indistinguishable from a row of genuine NULLs — which is precisely the shape of every negative
   claim in this brief (`account_move_id` non-null = 0 of 47,801). **Measured: 0 rows in 0 of 59
   blocks hit this branch**, so no published count is affected. The risk is that the instrument
   cannot report its own failure.
2. **Unescape order corrupts literal backslashes.** `p.replace('\\t','\t').replace('\\n','\n')
   .replace('\\r','\r').replace('\\\\','\\')` unescapes the doubled backslash **last**. A value
   containing a real backslash followed by `n` is emitted by COPY as `\\n` (three chars); the first
   replacement consumes the second backslash plus the `n` and yields backslash+newline instead of
   backslash+`n`. Correct order is to split on `\` and decode left-to-right, or to unescape `\\`
   first via a single pass. This does not change field counts (the corruption is inside a field), so
   it cannot alter any row count; it can alter the *content* of a text/jsonb field.
   **Not measured as fired**; flagged because the brief reads jsonb text out of
   `product_category.property_valuation` and reads `stock_valuation_layer.description` strings.

### B-3.3 — SUPPORTED: the duplicate artefacts are genuine duplicates, not divergent extracts

`T_account_move_line.sql` and `X_aml.sql` are both 18,155,413 bytes; `A_ir_model_data.sql` and
`C_ir_model_data.sql` both 27,914,048; `A_ir_model_fields.sql` / `C_ir_model_fields.sql` /
`../idemo_irmf.sql` all 5,961,660; and the `A_*` / `../idemo_*` pairs match byte-for-byte in size.
Each pair parses to identical row and column counts (table above). The only per-file difference is
pg_restore 18's random `\restrict` token, which differs on every invocation. So re-extraction was
reproducible: **the same table extracted twice from the same archive yielded the same data both
times.** That is a real, if modest, reproducibility control the run did not claim.

### B-3.4 — SUPPORTED: the TOC denominator

`TOC.txt` header declares `TOC Entries: 23232`. Enumerating the printed list by entry type:
COMMENT 11,064 / FK CONSTRAINT 4,227 / CONSTRAINT 1,272 / INDEX 1,263 / TABLE DATA 1,122 /
TABLE 1,122 / SEQUENCE SET 825 / SEQUENCE 825 / DEFAULT 736 / SEQUENCE OWNED BY 731 / VIEW 26 /
RULE 11 / TEXT SEARCH DICTIONARY 1 / TEXT SEARCH CONFIGURATION 1 / EXTENSION 1 / ACL 1
= **23,228 printed**, against 23,232 declared. The 4-entry gap is pg_restore's non-printed internal
entries (ENCODING, STDSTRINGS, SEARCHPATH and the archive's own header entry), which `-l` counts but
does not list. **`TABLE = TABLE DATA = 1,122` exactly**, and `tables.txt` holds 1,122 lines, so the
brief's stated denominator is internally consistent and reconciles to the archive header.
`MATERIALIZED VIEW` count is 0, so no data hides behind a matview.


---

## ASSIGNMENT 1 — DISPROVE THE SERIES-18 DEPLOYMENT IDENTITY

**Attempt: failed. The identity survives — but on different evidence than the brief offers, and one
of the brief's supporting instruments is demonstrably unreliable in this very database.**

### B-1.1 — CHALLENGED (as an instrument): `latest_version` cannot carry this claim alone

`ir_module_module.latest_version` is an ordinary `character varying` column (confirmed in the
schema). Odoo writes it at module load. It can misreport in at least four ways, none of which the
brief excludes:

1. **Plain UPDATE.** Nothing constrains it. A single SQL statement sets all 361 rows to `18.0.x`.
2. **Restore of an older database into newer code without an upgrade.** The value stays at the old
   series until `-u` runs. This *fails safe* (it would read 14.0), so it is not the risk here.
3. **The reverse: a newer database served by older code.** `latest_version` keeps the higher value.
4. **Partial migration.** Odoo upgrades module-by-module; a run that aborts leaves a mixture. Here
   there is no mixture — `Counter` over all 1,369 rows gives exactly `{'18.0': 361, NULL: 1008}`
   (1,008 NULL = 1,005 uninstalled + 3 uninstallable), and `published_version` is NULL on all 1,369.
   Uniformity is consistent with a clean upgrade *and* with a bulk UPDATE; it does not discriminate.

So the brief's S18-01 line "All 361 installed carry `latest_version` beginning `18.0`" is factually
reproduced (I re-derived it) but is **not sufficient** to establish the series. An independent
instrument is required.

### B-1.2 — SUPPORTED: the *schema* is that instrument, and it says series 18

Data can be forged; a column cannot be conjured by the data that sits in it. Odoo's `_auto_init`
creates and renames columns from the Python model definitions of the code that is actually running.
I extracted the complete schema:

```
/opt/homebrew/opt/postgresql@18/bin/pg_restore --schema-only -f SCHEMA.sql \
  ~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump
  -> rc=0, stderr empty (0 bytes), 5,219,881 bytes
grep -c '^CREATE TABLE public\.' SCHEMA.sql  -> 1122
```

1,122 `CREATE TABLE` — reconciling exactly to the TOC's 1,122 `TABLE` and 1,122 `TABLE DATA` entries
and to `tables.txt`'s 1,122 lines. **POPULATION for every schema claim below = these 1,122 tables;
PATTERN = literal substring / `^    <colname> ` anchored column match over `SCHEMA.sql`; UNIT = one
column or one table.**

**Series-18-specific shape present (each of these is a rename or an addition, so a leftover column
cannot explain it):**

| observation | command / evidence | implication |
|---|---|---|
| `account_move.origin_payment_id integer` present; `account_move.payment_id` **absent** | `./tbl.sh account_move \| grep payment_id` → `origin_payment_id integer`, `payment_state`, `payment_state_before_switch` only | the 18.0 rename `payment_id`→`origin_payment_id` **was applied**, and left no orphan |
| `product_template.is_storable boolean` present; `detailed_type` absent from **all 1,122 tables** (`grep -cE '^    detailed_type ' SCHEMA.sql` → **0**) | direct | 18.0 replaced `detailed_type` with `is_storable` |
| `product_template.lot_valuated boolean` and `stock_valuation_layer.lot_id integer` present | `./tbl.sh stock_valuation_layer` | per-lot valuation, an 18.0 `stock_account` addition |
| `product_category.property_stock_account_production_cost_id jsonb` present | `./tbl.sh product_category` | 18.0 `mrp_account` addition |
| `mail_canned_response` present, `mail_shortcode` **absent** | table-existence sweep | 18.0 rename |
| `account_move_send_wizard` **and** `account_move_send_batch_wizard` both present | table-existence sweep | 18.0 send-flow split |
| five `base_cache_signaling_{assets,default,groups,routing,templates}` sequences, not a single `base_cache_signaling` | `grep -inE 'cache_signaling' SCHEMA.sql` and TOC 2062-2066 | 18.0 split the cache-signalling sequence per cache |

**Series ≥ 17 shape present (rules out 14/15/16):** `ir_property` table absent from all 1,122
(`grep -in 'ir_propert' TOC.txt` → **no output at all**); `stock_lot` present and
`stock_production_lot` absent; `account_account.code_store jsonb` present (exactly 1 occurrence
of that column name in the whole schema); every company-dependent property is a **jsonb column on
the record** (`product_category.property_valuation jsonb`, `property_cost_method jsonb`,
`property_stock_journal jsonb`, `property_stock_account_input_categ_id jsonb`, …), which is the
17.0 storage model and is precisely what S18-02 relies on.

**Series 19 shape ABSENT (rules out the version above):** `res_groups_privilege` — the model Odoo 19
introduces alongside `res.groups.privilege_id` — is **not among the 1,122 tables**.
*Positive control that this table-existence probe can return PRESENT:* the same loop, same syntax,
returned `PRESENT` for `stock_lot`, `mail_canned_response`, `account_move_send_wizard`,
`account_move_send_batch_wizard`, `product_packaging`, `uom_uom`, `uom_category`,
`account_bank_statement_line`, `account_asset`, `res_users_settings` in the same execution.

**Conclusion.** The schema is internally consistent with exactly one series, 18.0, and inconsistent
with 14, 15, 16, 17 and 19. This is an instrument the data cannot fake, and it agrees with
`latest_version`. **The series-18 deployment identity is SUPPORTED — by the schema, not by
`latest_version`.**

*Caveat I am declaring rather than hiding:* the version-to-feature mapping above is my own
attribution of each column to an Odoo release. Corroboration against the reference source trees was
requested in parallel and is recorded under EVIDENCE REQUIRED NEXT. Nothing in the mapping is needed
for the *internal consistency* argument (no `payment_id`/`origin_payment_id` pair, no
`detailed_type`/`is_storable` pair — the schema has been migrated cleanly, not accreted), but the
absolute series label does depend on it.

### B-1.3 — SUPPORTED: no migration residue anywhere in the schema

Sweep over `SCHEMA.sql` (POPULATION 1,122 tables + all their columns; PATTERN case-insensitive
substring; UNIT one line):

```
'legacy'      -> 0 hits          'openupgrade' -> 0 hits
'migration'   -> 0 hits          '_14_0'/'_15_0'/'_16_0'/'_17_0' -> 0 hits each
```

OpenUpgrade renames dropped columns to `<name>_legacy_<ver>` and adds its own bookkeeping tables;
none exist. Combined with the absence of paired old/new column names (B-1.2), **this database was
not upgraded in place from series 14.** That matters, because it removes the scenario in which v14
code once ran against these tables.

### B-1.4 — **THE DECISIVE FINDING. What the `v14 2026:` markers and journal 45 actually prove: nothing about which code wrote the rows — and the brief's dating instrument is forged in 94% of the table**

`ir_config_parameter` (56 rows, `T_ir_config_parameter.sql`):

```
database.uuid        = 551ab874-9acb-11f1-b150-6ec7a480be3d  (create=2026-08-18 06:08:59.75533)
database.secret      = 58871b73-...                          (create=2026-08-18 06:08:59.75533)
database.create_date = 2026-08-18 06:09:12                   (create=2026-08-18 06:08:59.75533)
web.base.url         = https://occ.smeplus.cloud             (write =2026-08-25 17:17:00.665447)
```

`ir_module_module` write timestamps for the core stack: `mail` 2026-08-18 06:09:27, `product`
06:09:35, `stock` 06:09:58, `purchase` 06:10:05, `purchase_stock` 06:10:14 — a dependency-ordered
install sequence beginning **fifteen seconds after the database was created**, all at `18.0.x`.
Installed-module `write_date` by day: 08-18 ×138, 08-19 ×32, 08-23 ×2, 08-24 ×16, 08-25 ×11,
08-26 ×2, 08-27 ×3, 08-28 ×8, 08-29 ×149.

> **`idemo18_uat` is a database that was CREATED on 2026-08-18 as a series-18 database.**
> It is not a series-14 database that was upgraded. There is no series-14 code in its history.

Now the markers. `stock_valuation_layer` (47,801 rows, `A_stock_valuation_layer.sql`), partitioned
by description — the partition reproduces the brief's counts **exactly**:

```
v14 2026:* + 'Opening rebalance*'   45,978     (brief: 45,978)
'Migration correction: ...'             11     (brief: 11)
residual                             1,812     (brief: 1,812 "native v18 runtime output")
                                    ------
                                    47,801
```

But apply a *timestamp-shape* instrument the brief never used:

| sub-population | `create_date` at exactly `00:00:00` | `create_date` **earlier than the database itself** | `write_date` span | `create_uid` |
|---|---|---|---|---|
| v14 / Opening (45,978) | **45,978 = 100 %** | **44,947 = 97.8 %** | 2026-08-25 **22:25:52 → 22:27:29** (97 seconds) | `1` on all 45,978 |
| Migration correction (11) | 0 % | 0 % | 2026-08-25 22:16:28 → 2026-08-29 10:22:48 | `1` on all 11 |
| residual (1,812) | 0 % | 0 % | 2026-08-25 12:19:13 → 2026-08-29 10:23:34 | `1`×1,253, `114`×383, `102`×172, `117`×4 |

**44,947 rows carry a `create_date` strictly earlier than `database.create_date`.** A row cannot
have been created before its database existed. Therefore:

1. **`create_date` on those rows is a carried business date, not a write timestamp.** Every one of
   the 45,978 sits at midnight — a date coerced to a timestamp, the signature of a loader that sets
   `create_date` explicitly. Their real insert time is the `write_date`: **a single 97-second bulk
   load on 2026-08-25 22:25:52–22:27:29, as user 1.**
2. **The `v14 2026:` prefix and journal 45 `MIG26 "COA Migration 2026"` are descriptive strings
   about the *provenance of the business event*, written INTO a series-18 database by series-18 code
   running a migration load.** They are not evidence that series-14 code ever touched this database
   — and B-1.3 shows it never did. Anyone reading the brief's S18-04 phrase "carry v14-migration
   descriptions" as "were written by v14" would be wrong, and the brief does not close that door.
3. **A live methodological defect in the brief.** S18-04 defines its discriminating set — the 1,812
   "native v18" layers — partly by *when they were created*: "created 2026-08-25..2026-08-29". That
   range is correct (I reproduce 2026-08-25 12:19:13 → 2026-08-29 10:23:34). But **`create_date` is
   a demonstrably settable field in this database, forged on 94 % of this very table.** Using it to
   certify a sub-population as "native" is using an instrument whose failure mode has already fired
   at scale in the same column. The brief does not note this and offers no defence.

**The defence exists, and I supply it — the finding survives on better evidence.** Three properties
separate the 1,812 from any bulk load, none of which a loader that carries dates would reproduce:
- `create_date == write_date` on **1,640 of 1,812**, at sub-second resolution — an ORM `create()`.
- `create_uid` spread over **four distinct users** (1, 114, 102, 117); every loaded row is user `1`.
- `write_date` spread over **four days including timestamps outside the 97-second load window**, and
  the earliest residual `create_date` (2026-08-25 12:19:13) *precedes* the load by ten hours.

On that basis the residual really is native runtime output, and S18-04's conclusion —
**0 of those 1,812 natively-created layers carries an `account_move_id`** (independently re-derived,
see B-2.1) — stands. My challenge is to the *reasoning*, not the *result*.

### B-1.5 — MISSING: three instruments named in the assignment yield nothing, and one is a real empty

- **`ir_logging`** — the strongest possible witness to which code ran (it stores the server's own
  `path`, `func`, `line`). Extracted: `pg_restore -t ir_logging --data-only` → 948 bytes, rc=0, empty
  stderr. It **has a COPY block with all 13 columns and zero data rows**. By the B-3.1 discriminator
  this is a *genuine empty table*, not a failed extraction. **ir_logging contributes no evidence
  either way**, and no argument may be built on its silence.
- **`ir_cron_trigger`** — same: COPY block present, 7 columns, 0 rows.
- **`base_registry_signaling`** — a sequence, not a table. Value recovered via a TOC list file
  (`pg_restore -L seqlist.txt`): `setval('public.base_registry_signaling', 123, true)`, with
  `base_cache_signaling_default` at 229, `_assets` 13, `_templates` 25, `_groups` 11, `_routing` 1.
  123 registry invalidations is consistent with ~2 weeks of module installs and proves the registry
  was rebuilt many times; it carries **no series information** and cannot support or refute the
  identity. I record it so the next reader does not re-run it expecting more.
- **`ir_module_module_dependency`** — 2,997 rows, 4 columns, extracted cleanly. Structural only; it
  states dependencies, not versions.
- **`ir_model_data` (225,529 rows) / `ir_model_fields` (19,431 rows)** — extracted and integrity-
  checked (Assignment 3), but I did **not** mine them for series-specific field names, because the
  schema (B-1.2) already answers the question with a stronger instrument: `ir_model_fields` is ORM
  bookkeeping and is itself writable, whereas a physical column is not. Declared as not-done rather
  than implied-clean.

### B-1.6 — SUPPORTED, with a caveat the brief should carry: `database.uuid`

`database.uuid = 551ab874-9acb-11f1-b150-6ec7a480be3d`, created 2026-08-18 06:08:59. This is a
**version-1 (time-based) UUID**: the `11f1` in the third group is version nibble `1`. Its embedded
timestamp is therefore self-consistent with an 2026-08-18 creation and it is **not** a copy of an
older database's uuid. That independently corroborates B-1.4's "this database was created on
2026-08-18". Per the archive-denominator rule, the uuid remains the correct key for census work, and
the brief's note that it is not among the five in the P04 census means **this is a sixth deployment**
— which is a scope fact the P04 census now under-counts.


### B-1.7 — SELF-CORRECTION of B-1.2, against primary source

I sent my version-to-feature mapping for verification against the reference source trees rather than
leaving it as my own assertion. **It came back with two of my discriminators wrong.** Recording the
correction rather than quietly editing the table, per this programme's revision-log rule.

Source PATH SET actually searched: `/Volumes` (mounted: `ChatGPT Installer`, `iMac`, `iMacSys`) and
`/Users`, `find -maxdepth 8 -name release.py -path "*odoo*"` plus a second
`find -maxdepth 10 -type d -name stock_account` sweep to catch addons-only trees whose `release.py`
is absent. **15 full trees resolved: 9 at `version_info = (18, 0, 0, FINAL, 0, '')`, 6 at
`(19, 0, 0, FINAL, 0, '')`.** Findings uniform per series across all trees.

| my claim in B-1.2 | verdict against source | corrected status |
|---|---|---|
| `origin_payment_id` is an 18.0 marker | **WRONG.** Present in 18.0 (`account/models/account_move.py:211`) **and** 19.0 (`:206`) | rules out ≤17 only; **not** an 18-vs-19 discriminator |
| `lot_valuated` is an 18.0 marker | **WRONG.** Present in 18.0 (`stock_account/models/product.py:18`) **and** 19.0 (`:32`) | rules out ≤17 only; **not** an 18-vs-19 discriminator |
| absence of `detailed_type` is an 18.0 marker | partly wrong — absent from Python in **both** 18.0 and 19.0 | rules out ≤17 only |
| absence of `res_groups_privilege` rules out 19 | **CONFIRMED, and it is the cleanest discriminator.** `privilege_id = fields.Many2one('res.groups.privilege', …)` at `base/models/res_groups.py:36` in 19.0; **0 matches across all 9 18.0 trees** | stands |

So my 18-vs-19 case reduced to **one** schema discriminator. That is thin, so I obtained two more —
both stronger than anything in B-1.2, because they are the *running code's own self-description*:

**(i) `res_groups` has no `privilege_id` column.** Full column list from `SCHEMA.sql`:
`id, name jsonb, category_id, color, create_uid, write_uid, comment jsonb, share, create_date,
write_date, api_key_duration` + the `api_key_duration >= 0` check constraint. **No `privilege_id`.**
19.0 also reorders `res.groups._order` to `'privilege_id, sequence, name, id'` and adds a
`UNIQUE (privilege_id, name)` constraint — neither is in this schema.

**(ii) THE DECISIVE ONE — `ir_model_fields_selection` records the literal `fields.Selection` keys of
the code that loaded.** These rows are regenerated by the ORM from the Python source at every module
load; they are not business data and no migration writes them. In this database
(`A_sel.sql`, 3,503 rows, joined to `ir_model_fields` id 7646, `model=product.category`,
`name=property_valuation`, `ttype=selection`):

```
key='manual_periodic'  label={"en_US": "Manual",    "th_TH": "ด้วยตัวเอง"}
key='real_time'        label={"en_US": "Automated", "th_TH": "อัตโนมัติ"}
```

Against source:

```
18.0  stock_account/models/product.py:954
        property_valuation = fields.Selection([
            ('manual_periodic', 'Manual'),
            ('real_time', 'Automated')], string='Inventory Valuation', company_dependent=True, ...

19.0  stock_account/models/product.py:666
        property_valuation = fields.Selection(
            string="Inventory Valuation",
            selection=[('periodic', 'Periodic (at closing)'),
                       ('real_time', 'Perpetual (at invoicing)')], company_dependent=True, ...
```

**Character-exact match to 18.0 on both keys and both English labels; incompatible with 19.0 on
both.** 19.0 renamed the key itself (`manual_periodic` → `periodic`), so a 19.0 registry physically
cannot contain the string `manual_periodic` for this field. *Positive control in the same query:*
the sibling field `property_cost_method` (id 7647) returned its three keys `standard` / `fifo` /
`average` with full labels, so the join was live and could have returned different values.

This also **independently validates the brief's S18-02**, whose `ir_default` value is the string
`"manual_periodic"` — a value that is only a legal selection key in series 18.

**Net effect on the identity claim: STRENGTHENED, not weakened.** Two of my four schema markers were
bad and are withdrawn; the identity now rests on (a) `res_groups_privilege` / `privilege_id` absent,
(b) `ir_model_fields_selection` matching the 18.0 selection literal character-for-character,
(c) `manual_periodic` present as live data, (d) B-1.4's creation timeline, (e) B-1.3's absence of any
migration residue, (f) `ir_property` absent / `stock_lot` present / `code_store` present ruling out
≤16. **VERDICT: `idemo18_uat` IS a series-18 deployment. I could not disprove it.**

### B-1.8 — RISKY (citation reproducibility, affects the brief not the identity)

The brief cites source as `R1:` and `R3:` without pinning a build. The sweep found **9 distinct 18.0
trees and 6 distinct 19.0 trees** on this host, and their line numbers differ: the brief cites the
18.0 selection literal at `stock_account/models/product.py:915-917`, while
`odoo-18.0.post20260605` has it at `:954`. Same code, different build, ~39 lines apart. Two further
points a reader should not inherit:
- The brief's S18-06 claim "v18 `stock_account/models/` contains no `account_move_line.py`" is
  **CONFIRMED across all 9 18.0 trees**, and the file **is** present in all 6 19.0 trees. Solid.
- 19.0's `stock_account/models/` additionally carries `account_account.py`, `product_value.py`,
  `stock_picking_type.py`; 18.0 uniquely carries `stock_valuation_layer.py` and
  `template_generic_coa.py`. So the directory listing itself is a series discriminator, and the
  brief's "15 files, none named that" is consistent with it.
- Unrelated but load-bearing for anyone extending this work: `is_storable` is **not** defined in
  `addons/product/`. It lives in `stock/models/product.py` (18.0 `:704`, 19.0 `:821`). Any spec that
  points it at `product/models/product_template.py` is wrong for both series.

**EVIDENCE REQUIRED NEXT (Assignment 1):** pin `R1`/`R3` to one tree path + build string each, and
re-cite S18-02/S18-03/S18-06 line numbers against that pinned tree.


---

## ASSIGNMENT 2 — FIND ANOTHER FALSE-ZERO EXTRACTION RISK

**Method.** I re-derived every zero asserted in FINDINGS.md by a **structurally different** route from
the one that produced it. The brief's zeros all came from `pgc.load()` → Python dict → `Counter`.
My route is `awk -F'\t'` over the raw COPY block **by field position**, with the field index resolved
from *the file's own COPY header* rather than assumed — harness at `<s18>/expB/awkzero.sh`.
That harness is built so the S18-13 defect cannot recur silently:

```
  !! COLUMN '<name>' NOT IN HEADER -- would have been a silent zero
```

A misspelled column raises, it does not return 0. Every count below is printed beside a positive
control drawn from the **same pass over the same bytes**.

### B-2.1 — SUPPORTED (the headline zero), by three independent routes

```
$ ./expB/awkzero.sh A_stock_valuation_layer.sql account_move_id account_move_line_id \
      stock_move_id company_id product_id lot_id stock_valuation_layer_id
COPYHDR COLS: id,company_id,product_id,categ_id,stock_valuation_layer_id,stock_move_id,
              account_move_id,account_move_line_id,lot_id,create_uid,write_uid,description,...
  col#7 account_move_id      : rows=47801  nonNULL=0      NULL=47801  (empty-string=0)
  col#8 account_move_line_id : rows=47801  nonNULL=0      NULL=47801  (empty-string=0)
  col#6 stock_move_id        : rows=47801  nonNULL=44935  NULL=2866   <- POSITIVE CONTROL
  col#2 company_id           : rows=47801  nonNULL=47801  NULL=0      <- POSITIVE CONTROL
  col#3 product_id           : rows=47801  nonNULL=47801  NULL=0      <- POSITIVE CONTROL
  col#5 stock_valuation_layer_id : rows=47801 nonNULL=2   NULL=47799  <- POSITIVE CONTROL (a *sparse*
                                   non-zero: proves the counter resolves 2 hits in 47,801, not just bulk)
```

Re-run against `../idemo_stock_valuation_layer.sql` — a **separately produced extract of the same
table** — returned identical figures (0 / 0 / 44,935). `nonNULL=44935` matches the brief exactly.
NULL vs empty-string is separated explicitly: `empty-string=0`, so this is genuine SQL NULL, not `''`.
And B-1.4 partitions the table three ways and finds `account_move_id` non-null = **0 in every
sub-population including the 1,812 native ones**. **Three routes, one answer. SUPPORTED.**

### B-2.2 — SUPPORTED: the jsonb zeros, with a populated-jsonb positive control

The named risk was jsonb quoting — SQL `NULL` vs `'{}'` vs `'null'` vs a populated object. Resolved
by enumerating **every distinct raw value** across all 126 rows rather than testing a predicate:

```
property_valuation      : 1 distinct value  -> 126 x None                         (awk: nonNULL=0)
property_stock_journal  : 1 distinct value  -> 126 x None                         (awk: nonNULL=0)
property_cost_method    : 2 -> 108 x None, 18 x '{"1": "average"}'                (awk: nonNULL=18)
property_stock_account_input_categ_id  : 2 -> 111 None, 15 '{"1":176,"2":62,"3":100,"4":138}'
property_stock_account_output_categ_id : 2 -> 111 None, 15 '{"1":701,"2":702,"3":703,"4":704}'
property_stock_valuation_account_id    : 10 distinct -> 111 None, 15 populated
```

The populated columns are the positive control: the same instrument, same pass, **does** resolve
jsonb objects, and resolves ten distinct shapes in one column. So `property_valuation` NULL on
126/126 and `property_stock_journal` NULL on 126/126 are real. **S18-02 and the S18-05 journal claim:
SUPPORTED.**

### B-2.3 — SUPPORTED and WIDENED: the account/journal execution test

```
awk -F'\t' ... T_account_move_line.sql          (40,353 rows; account_id = field 7, journal_id = field 3)
GRNI input accounts   176 -> 0    62 -> 0    100 -> 0    138 -> 0
STJ journals           16 -> 0    24 -> 0     32 -> 0     40 -> 0
POSITIVE CONTROLS: 143 distinct non-null account_id present; 22 distinct journal_id present
                   top accounts 186=4049, 211=3522, 169=2940   <- exact match to the brief
                   top journals  45=8226,  33=7707,   9=4504   <- exact match to the brief
account 169 (130000 Inventory): 2,940 items, journal_id=45 on ALL 2,940, no other journal
```

**A count correction to the brief.** S18-05 states "144 distinct accounts do appear". The correct
figure is **143 accounts**; 144 is the number of distinct *values* in the column, of which one is the
NULL bucket covering 71 rows that carry no account at all. Count unit conflated with population — the
value has no effect on any conclusion, but the register should say 143.

**A widening the brief missed.** S18-05 tests only the GRNI **input** account. The same 15 categories
also configure, in the same jsonb, an **output** account and a **stock-valuation** account. I tested
them:

```
output accounts       701 -> 0    702 -> 0    703 -> 0    704 -> 0
valuation accounts     55 -> 0   481 -> 0    598 -> 0     93 -> 0   131 -> 0        (companies 2,3,4)
valuation account     169 -> 2,940 items, ALL of them in journal 45 "COA Migration 2026"  (company 1)
```

So the "configured, not executed" finding is **three times wider** than S18-05 states — input, output
**and** valuation accounts are all configured and all unreached by native posting. And it carries a
company asymmetry the brief does not report: company 1's valuation account is the only one of the
twelve with any journal item, and every one of those items is migration output.

### B-2.4 — SUPPORTED, with the absent-row semantics enumerated exhaustively

The named risk was "NULL vs empty vs `false` vs absent-row". Rather than query for rows, I dumped
**all 54 `ir_default` rows** and joined them to `ir_model_fields` for readable names — so an absent
row is visible as a gap in a complete listing, not inferred from a zero:

```
property_valuation                        co=NULL  -> "manual_periodic"   [ONE row, global. No company row.]
property_cost_method                      co=NULL  -> "standard"
property_stock_account_input_categ_id     co1->176   co2->false   co3->false   co4 = NO ROW
property_stock_account_output_categ_id    co1->701   co2->false   co3->false   co4 = NO ROW
property_stock_valuation_account_id       co1->169   co2->false   co3->false   co4 = NO ROW
property_stock_account_production_cost_id co1->false co2->false   co3->false   co4 = NO ROW
property_stock_journal                    co1->40    co2->16      co3->24      co4->32
```

S18-05's exact claim — "company 1 -> 176; companies 2 and 3 explicitly `false`; company 4 no row" —
is **SUPPORTED**, and now proven by exhaustive enumeration rather than by a query that could have
missed a row. Note the three value *encodings* live in one column and a naive comparison would
conflate them: ids are bare (`176`), booleans are bare (`false`), strings are **jsonb-quoted**
(`"manual_periodic"`). A predicate written as `value == 'manual_periodic'` returns zero against
`"manual_periodic"` — a false zero of exactly the S18-13 shape, one quote-mark wide. The brief
writes the quoted form correctly.

Two additions: company 4 has **no row for any of the four stock accounts** yet **does** have one for
`property_stock_journal` (32) and for income/expense categories — the gap is selective, not wholesale.
And `property_stock_account_production_cost_id` is `false` for company **1** as well, so that account
is unset in all four companies.

### B-2.5 — SUPPORTED and strengthened: the accrual zero

S18-07 asserts "0 of 15,522 moves carry 'accru' in `ref`". `'accru'` is lowercase; Thai-language
install; obvious case-sensitivity trap. Tested:

```
substring 'accru' (as the brief ran it) : 0        'Accru': 0     'ACCRU': 0
'accru' CASE-INSENSITIVE                : 0        Thai 'ค้างจ่าย': 0
non-empty ref (POSITIVE CONTROL)        : 15,434   <- exact match to the brief
NULL ref: 12   empty-string ref: 76     (12 + 76 + 15,434 = 15,522, reconciles)
WIDENED: no field of any of the 95 columns, on any of the 15,522 rows, contains 'accru'
         case-insensitively. Columns with 'accru' in the NAME: none.
```

The trap did not fire. I widened the search from one column to all 95 and it still holds.
Corroborating and independent: `account_accrued_orders_wizard` has a COPY block with 12 columns and
**0 rows** — the accrual wizard has no records. (Weak on its own: wizard records are transient. Worth
recording, not worth relying on.) **SUPPORTED.**

### B-2.6 — SUPPORTED: the remaining zeros

```
res_company (4 rows, 204 cols), by field position:
  fiscalyear_lock_date  nonNULL=0/4      tax_lock_date   nonNULL=0/4
  sale_lock_date        nonNULL=0/4      purchase_lock_date nonNULL=0/4
  hard_lock_date        nonNULL=0/4
  POSITIVE CONTROLS in the same pass: anglo_saxon_accounting nonNULL=4/4 (co1='t'; co2,3,4='f'),
  po_lock 4/4 ('edit'), currency_id 4/4 (=133), name 4/4, parent_id 0/4
```
S18-09 and the S18-06 anglo-saxon line: **SUPPORTED**.

```
11 'Migration correction' layers: stock_move_id non-null = 0, account_move_id non-null = 0   (S18-04)
layers with no stock move overall: 2,866                                    (brief: 2,866)  MATCH
layers with value exactly 0.00:    1,205, single repr '0.00'                (brief: 1,205)  MATCH
scgl_product_category_company_rel: 32 rows, 16 distinct categories, 110 of 126 uncovered,
  companies {1:9, 2:9, 3:7, 4:7}; scgl_allow_purchase='t' on 126/126;
  15 GRNI-configured categories, 3 of them also in the rel table               (brief: 3 of 15) MATCH
```
S18-12: **SUPPORTED**. (Minor addition: `scgl_allow_sale` is `'f'` on 1 of 126 — the only non-vacuous
flag in the module; the brief reports only the purchase flag.)

### B-2.7 — CHALLENGED: a `-t` vector that did NOT fire here but is live for the next reader

The assignment names "a `-t` pattern matching a different or partitioned table". I tested the vector:

- **No declarative partitioning.** All 3 `PARTITION` occurrences in `SCHEMA.sql` are window-function
  `PARTITION BY` clauses inside views; there is no `PARTITION OF` / `PARTITION BY RANGE` table.
- **Single schema.** `CREATE SCHEMA` count = 0; all 1,122 TOC `TABLE` entries are `TABLE public …`,
  so `-t <name>` cannot collide across schemas.
- **`-t` behaved as an exact match in every extraction.** Assignment 3 shows each of the 59 files
  contains exactly one COPY block and it is the intended table — `-t account_move` did not also pull
  `account_move_line`.
- **BUT: PostgreSQL table inheritance is present.** `INHERITS (public.ir_actions)` on **five**
  children: `ir_act_client`, `ir_act_report_xml`, `ir_act_server`, `ir_act_url`, `ir_act_window`.
  pg_dump emits each child's own rows separately, so nothing was double-counted or lost here (the run
  extracted the child `ir_act_window`, 905 rows, correctly). **The live risk is for anyone who later
  extracts the parent:** `-t ir_actions` yields only the parent's own tuples, while `SELECT * FROM
  ir_actions` on a live server returns all five children's rows too. A "0 server actions" conclusion
  drawn from `-t ir_actions` would be a false zero, and the discriminator — 718 bytes vs an empty
  COPY block (B-3.1) — would **not** catch it, because the extract would be non-empty and look fine.
  No claim in FINDINGS.md depends on this. Recording it as an unfired vector.

### B-2.8 — **CHALLENGED: S18-08's discriminating test, as written, is false**

Every *number* in S18-08 reproduces exactly. The *stated test* does not.

```
posted in_invoice moves            : 1,879     (brief: 1,879)   MATCH
date != invoice_date               : 1,667     (brief: 1,667)   MATCH
median delta                       : +13       (brief: +13)     MATCH
max delta                          : +30       (brief: +30)     MATCH
NEGATIVE deltas                    : 0         (brief: "never negative")  SUPPORTED
   POSITIVE CONTROL - full delta spread present: 0->212, 1->68, 2->37, 3->63, 4->73, 5->65,
   6->67, 7->70, ... 27->53, 28->43, 29->34, 30->20. min=0, max=30, no missing/NULL dates.
accounting date = last day of month (calendar-aware) : 1,747   (brief: 1,747)   MATCH
accounting day 25                                    :   124   (brief:   124)   MATCH
```

But S18-08 states: **"all 1,879 are in the same month"**.

```
accounting-date months of the 1,879 posted vendor bills:
  2026-01 268 | 2026-02 377 | 2026-03 305 | 2026-04 189 | 2026-05 251
  2026-06 173 | 2026-07 184 | 2026-08 132
                                        -> EIGHT distinct months, not one.
```

As written the sentence is **false**, and it is the load-bearing half of the test used to **withdraw
a candidate finding before publication**. A reader auditing the withdrawal against the data would
find the stated basis contradicted and would be entitled to reinstate the finding.

**The withdrawal is nonetheless correct** — I found the measurement the brief must have meant and ran
it. The discriminating question is not whether all bills sit in one month, but whether each bill's
accounting date sits in the same month as *its own* invoice date:

```
accounting date in the SAME calendar month as that bill's invoice_date : 1,879 of 1,879  (100%)
accounting date in a LATER month than its invoice_date                 :     0
```

Zero bills cross a period boundary. Combined with 1,747/1,879 landing on the last day of their own
month, "month-end posting convention, not a period-cutoff violation" is **SUPPORTED** — on the
same-month-as-its-own-invoice-date test, which is what S18-08 should say. **This is a wording defect
that inverts the meaning of the only test justifying a withdrawal, in a package whose numbers are
otherwise exact. It must be corrected before publication.**

### B-2.9 — CHALLENGED: "4/4" is asserted over two companies that have never transacted

S18-02 concludes "Every product in all four companies resolves to `manual_periodic`. **126/126, 4/4**."
The resolution logic is sound (B-2.2, B-2.4). But the denominator `4/4` invites the reader to treat
four equal companies. They are not:

| | co 1 | co 2 | co 3 | co 4 |
|---|---|---|---|---|
| account_move | 9,733 | 5,789 | **0** | **0** |
| stock_valuation_layer | 25,978 | 21,823 | **0** | **0** |
| stock_move | 26,868 | 24,213 | **0** | **0** |
| purchase_order | 8,969 | 4,918 | **0** | **0** |
| res_users whose default company it is | 29 | 13 | 5 | **0** |
| product_template owned | 161 | 83 | 1 | **0** |

Companies 3 and 4 are **empty shells**, and company 4 has **no users at all** — a fact no section of
the brief reports. Every company-scoped zero in FINDINGS.md (S18-01, S18-05's "companies 2, 3, 4
resolve to no account", S18-06's anglo-saxon FALSE on 2/3/4) is therefore **measured** for companies
1–2 and **merely configured** for 3–4. That is not a false zero — the figures are right — but it is a
population claim whose two never-transacted members carry no evidential weight and should not be
counted as confirmations. The correct statement is "126/126 categories; measured in 2 transacting
companies, configured identically in 2 that have never transacted."

Read the other way, companies 3 and 4 are the **never-transacted negative control this evidence base
already contains and does not use**: a policy that produced zero GL linkage in two live companies and
also zero rows in two dormant ones is exactly the spread that should be published beside the zero.


---

## CONSOLIDATED POSITION

*Verdicts are perspectives on the evidence base, not adjudications of the findings. Where I disagree
with the brief I have kept both readings visible rather than replacing one with the other.*

### SUPPORTED

| id | claim |
|---|---|
| B-1.2 / B-1.7 | `idemo18_uat` **is** a series-18 deployment. I could not disprove it. It rests on `res_groups` having no `privilege_id`, `res_groups_privilege` absent from all 1,122 tables, and `ir_model_fields_selection` matching the 18.0 `fields.Selection` literal character-for-character (`manual_periodic`/"Manual", `real_time`/"Automated") where 19.0 has `periodic`/"Periodic (at closing)". |
| B-1.3 | No migration residue anywhere: `legacy` / `openupgrade` / `migration` / `_1[4-7]_0` all return **0** over the full schema. This database was never upgraded in place from an earlier series. |
| B-1.4 | The database was **created** 2026-08-18 06:09:12 as series 18; core modules installed 15 seconds later in dependency order at `18.0.x`. |
| B-1.6 | `database.uuid` is a v1 time-based UUID self-consistent with 2026-08-18; not a copied uuid. It is a **sixth** deployment the P04 census does not carry. |
| B-2.1 | SVL `account_move_id` / `account_move_line_id` non-null = **0 of 47,801** — three independent routes, four positive controls including a sparse 2-in-47,801. |
| B-2.2 | `property_valuation` and `property_stock_journal` jsonb NULL on 126/126, with a populated-jsonb positive control resolving ten distinct object shapes in the same pass. |
| B-2.3 | Accounts 176/62/100/138 and journals 16/24/32/40 carry **0** items in 40,353; account 169's 2,940 items are **all** in journal 45. Top-3 accounts and top-3 journals match the brief exactly. |
| B-2.4 | The `ir_default` layout in S18-05 is exactly right, proven by exhaustive enumeration of all 54 rows rather than by a query. |
| B-2.5 | The accrual zero holds under case-insensitive search, Thai search, and widening from `ref` to all 95 columns. |
| B-2.6 | All five lock dates NULL on 4/4; anglo-saxon co1 `t` / co2,3,4 `f`; 2,866 no-move layers; 1,205 zero-value layers; scgl rel 32 rows / 16 categories / 3 of 15 GRNI. |
| B-2.8 | S18-08's *withdrawal* is correct: **0 of 1,879** posted vendor bills cross a period boundary, and 1,747 land on the last day of their own month. |
| B-3.1 | The bounded absences of `ir_property` and `stock_landed_cost*` are real, and the 718-byte-vs-empty-COPY-block discriminator proves it. |
| B-3.3 / B-3.4 | Duplicate extracts are byte-consistent and reproduce identically; the 1,122 denominator reconciles across TOC, `tables.txt` and `SCHEMA.sql`. |

### CHALLENGED

1. **B-1.1 — `latest_version` cannot carry the deployment identity.** It is an ordinary `varchar`,
   settable by one UPDATE, and its uniformity is equally consistent with a clean upgrade and a bulk
   overwrite. S18-01 offers it as the identity evidence. The identity is true; the stated evidence is
   insufficient. Replace it with B-1.7's instruments.
2. **B-1.4 — `create_date` is forged on 94 % of `stock_valuation_layer`, and S18-04 uses `create_date`
   to certify its discriminating set.** 44,947 rows carry a `create_date` strictly earlier than the
   database's own creation; all 45,978 loaded rows sit at exactly `00:00:00`; their true insert time
   is a single 97-second `write_date` window on 2026-08-25 22:25:52–22:27:29 as user 1. **The result
   survives** — the 1,812 native layers are distinguishable by `create_date == write_date` at
   sub-second resolution on 1,640 of them, four distinct `create_uid`s, and write times outside the
   load window — but the brief's *reasoning* does not, and the defence is mine, not the brief's.
3. **B-1.4 — the `v14 2026:` markers and journal 45 prove nothing about which code wrote the rows.**
   Given B-1.3, no series-14 code ever ran against this database. They are provenance strings written
   *into* a series-18 database by series-18 code executing a data load. Any reading of "carry
   v14-migration descriptions" as "were written by v14" is unsupported, and the brief leaves it open.
4. **B-2.8 — S18-08's discriminating test as written is false.** "All 1,879 are in the same month" —
   they span **eight** months (2026-01 … 2026-08). This is the load-bearing half of the only test
   justifying withdrawing a candidate finding. Every number around it is exact; the sentence is not.
   It must be restated as "each bill's accounting date is in the same month as **its own**
   `invoice_date` — 1,879 of 1,879, 0 crossing a period boundary."
5. **B-2.9 — "4/4" counts two never-transacted companies as confirmations.** Companies 3 and 4 have
   zero moves, zero layers, zero stock moves, zero purchase orders; company 4 has **zero users**. The
   figures are right; the population claim over-reaches. They are also the never-transacted control
   this evidence base already contains and does not use.
6. **B-3.1 — the S18-13 defect class is four instances, not one.** Three extracts targeted table
   names absent from the archive (`account_transfer_model_account_account_rel`,
   `account_transfer_model_line_account_analytic_account_rel`, `product_category_company_rel`) and
   the run detected none of them. The two real transfer-model relation tables —
   `account_analytic_account_account_transfer_model_line_rel` and
   `account_transfer_model_line_res_partner_rel` — were never extracted.
7. **B-2.3 — "144 distinct accounts" is 143 accounts plus a NULL bucket** covering 71 account-less rows.

### RISKY

- **B-3.2 — `pgc.py` silently repairs field-count mismatches** (`vals = (vals + [None]*len(cols))
  [:len(cols)]`), with no counter and no signal. A padded row is indistinguishable from genuine NULLs
  — the exact shape of every negative in this brief. **Measured as never having fired: 0 rows in 0 of
  59 blocks.** The risk is that the instrument cannot report its own failure.
- **B-3.2 — `pgc.py` unescapes `\\` last**, so a literal backslash followed by `n` decodes to
  backslash+newline. Cannot change field counts; can change jsonb/description *content*. Not measured
  as fired.
- **B-2.7 — five tables INHERIT `ir_actions`.** `-t ir_actions` would return only parent tuples while
  a live `SELECT` returns all children — a false zero the 718-byte discriminator cannot catch,
  because the extract would look healthy. Unfired; live for the next reader.
- **B-1.8 — `R1`/`R3` are unpinned.** Nine 18.0 trees and six 19.0 trees exist on this host and their
  line numbers differ (the brief cites the 18.0 selection literal at `:915-917`; one 18.0 build has
  it at `:954`). A build string is not a code identity.

### MISSING

- **B-1.5 — `ir_logging` is empty** (COPY block, 13 columns, **0 rows**), and so is `ir_cron_trigger`.
  The best available witness to which code ran contributes nothing. No argument may rest on its
  silence, in either direction.
- **B-1.5 — `base_registry_signaling` = 123** (cache sequences 229/13/25/11/1). Recovered, but it
  carries no series information. Recorded so it is not re-run in hope.
- **B-1.5 — I did not mine `ir_model_data` (225,529 rows) or `ir_model_fields` (19,431 rows) for
  series-specific model/field names.** The schema answered the question with a stronger instrument.
  Declared as not-done, not implied-clean.
- The brief's source-side claims (S18-06 code absence, S18-11 module/source population, S18-12's "does
  not touch `property_*`") are **outside my evidence-base scope**; I checked only that S18-06's
  "no `account_move_line.py` in v18 `stock_account/models/`" is corroborated across all 9 18.0 trees
  and contradicted in all 6 19.0 trees.

### EVIDENCE REQUIRED NEXT

1. Restate S18-08's discriminating test (B-2.8). **Blocking** — it currently reads as its own negation.
2. Re-base S18-04's sub-population on `write_date` + `create_uid` + `create==write`, and record that
   `create_date` is loader-set on 45,978 of 47,801 rows (B-1.4). **Blocking for S18-04's method.**
3. Replace S18-01's identity evidence with B-1.7's instruments (B-1.1).
4. Extract the two real transfer-model relation tables and re-run any claim that touched them; audit
   the run's remaining extracts for further name misses (B-3.1).
5. Test whether the **output** and **valuation** accounts belong in S18-05 — I show they do, and that
   S18-05 is three times wider than stated (B-2.3).
6. Pin `R1`/`R3` to one tree path plus build string and re-cite S18-02/03/06 line numbers (B-1.8).
7. Restate every company-scoped denominator as "2 transacting + 2 never-transacted" (B-2.9).
8. Add the P04 census entry for `database.uuid = 551ab874-…`; it is a sixth deployment (B-1.6).
9. Fix `pgc.py`'s silent field-count repair and unescape order, or record them as accepted (B-3.2).

### Scope and honesty notes

- Read-only throughout. No database written, no source modified, no Odoo server run, nothing
  installed. Every command was `pg_restore -f`, `grep`, `awk`, `find`, `sed`, `python3` reads.
- **I got things wrong and corrected them in place rather than silently:** two of my four series-18
  schema discriminators (`origin_payment_id`, `lot_valuated`) were bad and are withdrawn (B-1.7); I
  misread `journal_id` as field 8 when it is field 3, which produced a nonsense journal table that I
  re-ran against the correct index (B-2.3).
- My Odoo version-to-feature attributions were **not** taken from my own knowledge as final; they
  were checked against 15 source trees on this host, and that check is what caught my two errors.
- Where the brief and I disagree, both readings are stated. In every case but B-3.1's four-versus-one
  count and B-2.3's 143-versus-144, **the brief's numbers reproduce exactly** — the defects I found
  are in instruments, wording and population framing, not arithmetic.

