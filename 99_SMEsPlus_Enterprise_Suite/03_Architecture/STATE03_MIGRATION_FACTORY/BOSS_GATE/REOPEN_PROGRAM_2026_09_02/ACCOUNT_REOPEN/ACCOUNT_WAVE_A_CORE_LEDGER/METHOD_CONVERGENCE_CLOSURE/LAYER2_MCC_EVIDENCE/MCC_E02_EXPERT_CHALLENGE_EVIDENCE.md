# MCC_E02 — EXPERT AND AUDIT CHALLENGE: PRIMARY EVIDENCE (LAYER 2)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Vendor tokens and `file:line` citations.
> **`DR-NC-06`: `MCC_E00` and `MCC_E01` are NOT edited. This file governs where it conflicts with
> either, for the claims it addresses and no others.**
> Every line below was **re-read at primary source by this session** before the finding was accepted.
> `SRC` = `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/`.
> `V18P` = `/Volumes/iMacSys/ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605/odoo/`.
> `V19E` = `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/SMEsPlus19/odoo-19.0+e.20260312/odoo/`.

---

## `E02-01` — `J-07`: a referential action manufactures the company-less rate row

| Site | Content |
|---|---|
| `SRC/addons/base/models/res_currency.py:365-366` | `company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.root_id)` — **no `required`, no `ondelete`** |
| `SRC/fields.py:3189-3197` | `if not self.ondelete: … self.ondelete = 'restrict' if self.required else 'set null'` |
| `SRC/fields.py:3232-3235` | `model.pool.add_foreign_key(model._table, self.name, comodel._table, 'id', self.ondelete or 'set null', …)` |
| `SRC/addons/base/models/res_company.py:339-346` | `def unlink(self):` → `res = super().unlink(); self.env.registry.clear_cache(); return res` — **no guard** |
| `SRC/addons/account/models/company.py` | **no `unlink` override, no `@api.ondelete` hook** — token search returns 0 |
| Counter-fact | `SRC/addons/base/models/res_company.py:37` — `parent_id = fields.Many2one('res.company', … ondelete='restrict')`. A branch cannot be promoted to a root by deleting its parent; the database refuses |
| Second referential write | `SRC/addons/base/models/res_currency.py:364` — the currency relation declares `ondelete="cascade"`, so deleting a currency **deletes** its rate rows at the database layer |

**Disposition: `VERIFIED DEFECT`.** `NOT PROVEN` as to the deployed schema (no database executed).
**`MCC_E00 §MCC-E-010`, `MCC_B` §7 and `MCC_C` §4.3 are all enumerations of WRITE PATHS and none
contains a referential action.**

## `E02-02` — `J-06`: the balance assertion is context-suppressible. **`T0-12`.**

`SRC/addons/account/models/account_move.py:2330-2337`:
```python
@contextmanager
def _check_balanced(self, container):
    with self._disable_recursion(container, 'check_move_validity', default=True, target=False) as disabled:
        yield
        if disabled:
            return
```
Production consumers, whole `addons` tree, tests excluded — **3**:
`SRC/addons/point_of_sale/models/pos_session.py:439`, `:442`, `:985`.
`grep -rn "check_move_validity" SRC/addons --include='*.py' | grep -v /tests/` → **4 hits**: the
control plus the three consumers. **Disposition: `VERIFIED DEFECT`.**

## `E02-03` — `J-05`: the balance invariant is one-dimensional. **`T0-11`.**

`SRC/addons/account/models/account_move.py:2364-2375` `_get_unbalanced_moves`:
```sql
JOIN res_company company ON company.id = move.company_id
JOIN res_currency currency ON currency.id = company.currency_id
GROUP BY line.move_id, currency.decimal_places
HAVING ROUND(SUM(line.balance), currency.decimal_places) != 0
```
`amount_currency` appears nowhere. The only constraint touching it is
`SRC/addons/account/models/account_move_line.py:435-448` `check_amount_currency_balance_sign`, which
constrains the **sign** relationship, never a sum. **Disposition: `VERIFIED DEFECT`.**

## `E02-04` — `J-01`: the currency table translates a different measurement object

`SRC/addons/account/models/res_currency.py:103-104`:
```python
domestic_currency_companies = companies.filtered(lambda x: x.currency_id == main_company.currency_id)
other_companies = companies - domestic_currency_companies
```
`:180-183` (and identically `:208-211`, `:254-258`, `:294-300`):
```sql
LEFT JOIN res_currency_rate rate
    ON rate.currency_id = other_company.currency_id
```
**The join is on the COMPANY's currency, never on the journal item's transaction currency.**
`:144-167` emits **rate 1** for every company sharing the consolidating company's currency;
`:53-59` short-circuits the whole table to unit rates when `len(companies.currency_id) == 1`.
**Disposition: `BW-28` WITHDRAWN as registered.**

## `E02-05` — `J-04`: whole-entity par consolidation. **`BW-28a`, `T0-07` headline.**

`SRC/addons/account/models/res_currency.py:178` and `:206`:
`CASE WHEN rate.id IS NOT NULL THEN %(main_company_unit_factor)s / rate.rate ELSE 1 END`, under a
`LEFT JOIN`. Third substitution at `:307`: `COALESCE(out_period_rate.rate, 1.0)`, inside the
day-weighted average union — it contaminates a **blended** rate. **Disposition: `VERIFIED DEFECT`.**

## `E02-06` — `J-02`: the detective control exists and its rate is user-overridable

`SRC/addons/account_reports/models/account_multicurrency_revaluation_report.py`:
`:41` default rate from `_get_rates`; **`:52-54`** the override —
`float(previous_options['currency_rates'][str(currency_id.id)]['rate'])` when supplied;
`:63-65` `options['custom_rate'] = any(...)`; `:74-75` the warning;
`:248-254` and `:331-333` the per-line retranslation difference;
`:165-172` drill-through to the rate model. Coverage boundary: `:307`/`:340` exclude income and
expense account types; `:315-320` honour a per-account exclusion table toggled by one button at
`:156-159`. **Disposition: `MCC_G` `BW-28`'s class-`A` "no detecting control" is CONTRADICTED.**

## `E02-07` — `J-03`: the empty constraint definition is a delegation idiom

`SRC/models.py:3520-3529`:
```python
if current_definition:
    sql.drop_constraint(cr, self._table, conname)
if not definition:
    # virtual constraint (e.g. implemented by a custom index)
    self.pool.post_init(sql.check_index_exist, cr, conname)
```
`SRC/tools/sql.py:544-545`: `def check_index_exist(cr, indexname): assert index_exists(cr, indexname), …`
Paired index: `SRC/addons/account/models/account_move.py:730-735` —
`CREATE UNIQUE INDEX account_move_unique_name ON account_move(name, journal_id) WHERE (state = 'posted' AND name != '/')`.
**Disposition: `T0-09` instance 2 FALLS.** The defect at that site is the index's **scope**.

## `E02-08` — `T0-08` verified element by element

| Element | Site | Result |
|---|---|---|
| Empty constraint definition | `account_move.py:713-715` | verified — but see `E02-07`; it is an idiom |
| Index scoped by journal, posted-only, `'/'`-excluded | `account_move.py:730-735` | verified, **weaker than stated** |
| Conditional lock | `account_move.py:2377-2379` | verified |
| *"missing index degrades to a log line"* | `SRC/tools/sql.py:544-545` | **CONTRADICTED — it asserts** |
| Wizard blanks the number to escape the partial index | `account_resequence.py:160-163`, `moves_to_rename.name = False; moves_to_rename.flush_recordset(["name"])`, with the in-code comment on the constraint; hash guard at `:157-159` blocks only date ordering | verified |
| Database-wide key disabling number/date alignment | `sequence_mixin.py:154-161` | verified |
| **Seventh, unstated** | `account_move.py:3252-3255` — a manager violating the journal's override regex is let through and the code then **permanently disables the journal's regex** | **NEW** |
| **Seventh-and-a-half** | `sequence_mixin.py:127-128` `_must_check_constrains_date_sequence()` — an override hook disabling the alignment constraint model-wide | **NEW** |

**Disposition: `T0-08` JUSTIFIED and net UNDERSTATED.**

## `E02-09` — `J-08`: the lock-date wizard's company field is inert

`SRC/addons/account_accountant/wizard/account_change_lock_date.py`:
`:18-23` `company_id = fields.Many2one(comodel_name='res.company', required=True, readonly=True, default=lambda self: self.env.company)`;
`:348` `self.env.company.sudo().write(lock_date_values)` — **the declared field is never read**;
`:350-361` `change_lock_date` gates only on `has_group('account.group_account_manager')`;
`:198` the draft-move check uses `self.env.company`, not `self.company_id`.
The file is in **neither** the 18-file nor the 26-file Wave A surface.
**Disposition: `VERIFIED DEFECT`. Third `T0-09` instance, on the period lock itself.**

## `E02-10` — `J-09`: the lock-exception path, corrected and widened

| Point | Site |
|---|---|
| The company read is **skipped** when the original-lock-date key is supplied | `SRC/addons/account/models/account_lock_exception.py:205-207` — `company = self.env['res.company'].browse(vals.get('company_id', self.env.company.id))` then `if 'company_lock_date' not in vals:` … |
| Revoke checks **group only**, then writes under elevation | `:258-267` — `if not self.env.user.has_group('account.group_account_manager'): raise …` then `record_sudo = record.sudo(); record_sudo.active = False` |
| **Ancestor propagation** — the material half | `SRC/addons/account/models/company.py:539-556` — `# We need to use sudo, since we might not have access to a parent company.` at `:539`; `for company in self.sudo().parent_ids:` at `:540`; `('user_id','=',None)` disjunct at `:549` |
| No user ⇒ everyone; no end datetime ⇒ forever | `account_lock_exception.py:37-42`, `:46-49` |
| Access: read + create, **no write, no unlink** | `SRC/addons/account/security/ir.model.access.csv:18-19` |
| No record rule, either tree | token search over both trees returns only the two access rows and the form view |
| Shipped UI hard-codes the acting company | `SRC/addons/account_accountant/wizard/account_change_lock_date.py:276-278`, created at `:357` |
| Hard lock is **not** exceptable | `SRC/addons/account/models/company.py:54-64` — `SOFT_LOCK_DATE_FIELDS` excludes it |

**Disposition: `VERIFIED DEFECT`, wider than registered. `MCC_D` §2's mechanism attribution is
CORRECTED — the company field is honoured by generic ORM create, because `readonly` is inert.**

## `E02-11` — `J-10`: the Thai statutory VAT export carries no company filter

`SRC/addons/l10n_th_reports/models/tax_report_vat.py:59-68`:
```python
def _l10n_th_print_tax_report(self, options, domain, origin_type='sale'):
    domain += [('date', '>=', date_from), ('date', '<=', date_to)]
    …
    moves = self.env['account.move'].search(domain)
```
Header: `:103-107` — `company = self.env.company; company_name = company.name; vat = company.vat or ''`,
then `company.partner_id.l10n_th_branch_name`.
Governing rule: `SRC/addons/account/security/account_security.xml:147-151` —
`[('company_id','in',company_ids)]`, i.e. the user's **active** companies.
Correct sibling in the same module: `tax_report_pnd.py:26` routes through the report engine's
`_get_report_query`, which applies the report's company ids.
**Disposition: `VERIFIED DEFECT` (mechanism) · `NOT PROVEN` (runtime).**

## `E02-12` — `J-11`: `account.report` has no company dimension and no record rule

`SRC/addons/account/models/account_report.py:25` `_name = "account.report"`; `:46` `country_id` — and
**no `company_id` declaration on that model**.
Access: `SRC/addons/account/security/ir.model.access.csv:136-138` — basic `1,0,0,0`, readonly
`1,0,0,0`, **`account.group_account_manager` `1,1,1,1`**.
`grep -rn 'ref="model_account_report"' SRC/addons --include='*.xml'` → **3 hits, 0 `ir.rule`**:
a cron `model_id` (`account_reports/data/report_send_cron.xml:4`) and a server action plus its binding
(`account_reports/views/account_report_view.xml:387-388`).
**Disposition: `VERIFIED DEFECT`. `MCU-04` is CLOSABLE.**

## `E02-13` — `J-C1`: the localisation denominator

| Measure | Verified |
|---|---|
| `SRC/addons` `l10n_*` | **2** — `l10n_th`, `l10n_th_reports` |
| `SRC/addons_archive` `l10n_*` raw | **904** |
| … of which `__dup_*` (excluded by this round's own declared pattern) | **450** |
| … distinct | **454** |
| **Correct denominator** | **456** |
| Thai modules in `SRC/addons_archive` | **0** |

**Disposition: `MCC_B` `B-2` and `MCC_E01 MCCX-03` are CORRECTED. The magnitude was overstated and the
risk direction for the actual deployment was inverted.**

## `E02-14` — `J-C2`: two rate readers bypass record rules by elevation

`SRC/addons/base/models/res_currency.py:393` — `return self.currency_id.rate_ids.sudo().filtered(…)`
`SRC/addons/base/models/res_currency.py:401` — `company.sudo().currency_id.rate_ids.filtered(…)`
**`MCC_E00 §MCC-E-005` rows 5 and 6 record "Record rules: apply". CORRECTED to BYPASSED.**
**`T0-07`'s record-rule-bypassing READ surface is 10, not 8** — 8 raw-SQL plus these 2.

## `E02-15` — `J-14`: the v19 aggregator, reachability corrected

`V19E/odoo/orm/models.py:1972-2004` — verified verbatim, including
`WHERE company_id IS NULL OR company_id = <root>` and the
`CASE WHEN name <= today … DESC / CASE WHEN name > today … ASC` future-rate ordering, and a **fifth**
fallback at `:2000-2004` — `SUM(%s / COALESCE(%s, 1.0))`.
**Zero occurrences in either v18 core** — reproduced.
Emission (opt-out, not opt-in): `V19E/odoo/addons/web/static/src/model/relational_model/utils.js:541-555`;
`views/pivot/pivot_model.js:1088-1091`; `views/graph/graph_model.js:334-339`;
`V19E/odoo/orm/fields_numeric.py:200` — `Monetary.aggregator = 'sum'`.
Suppression on single-currency groups: `utils.js:596-601`; `pivot_model.js:992-997`;
`graph_model.js:448-451`.
**Disposition: the query EXECUTES on essentially every grouped read; the wrong figure SURFACES only on
multi-currency groups.**

## `E02-16` — `J-C3`: migration directories

`find SRC/addons -type d -name migrations` → **5**, of which `spreadsheet/static/tests/migrations/`
is a JavaScript test directory → **4 Python**.
`find SRC/addons_archive -type d -name migrations` → **70**.
Token search over all 75 for the rate table and the hierarchy columns → **0**.
`SRC/upgrade/__init__.py` is a namespace stub; `SRC/upgrade_code/` holds 2 unrelated scripts.
**Conclusion holds over the widened path set. `MCC_E00 §MCC-E-010` item 9 and `MCC_F` `F-03` stated
two different scopes for one class-`A` claim; both are corrected here.**
**New class `C`:** the external upgrade namespace is populated at deployment time and was not searched
— and it is the exact carrier `MCC-C-R1` postulates.

## `E02-17` — `J-C4`: `BW-35`'s path set

`grep -rnE "reversed_entry_id|reversal_move_id" SRC/addons/account` (tests, i18n, static excluded)
→ **11** — reproduces.
Same pattern over `SRC/addons` + `SRC/addons_archive`, excluding the accounting addon and `__dup_`
→ **144 lines across 30+ modules**, including
`SRC/addons_archive/l10n_jo_edi/models/account_move.py:53`, which **redeclares the field**, and
`SRC/addons_archive/l10n_latam_invoice_document/wizards/account_move_reversal.py`, which overrides the
reversal wizard.
**The widened search was executed by the audit panel:** `grep` for a constraint on the field over both
trees → **0**.
**Disposition: the CONCLUSION survives and is re-established as class `A` over the corrected path set,
on the panel's evidence. `MCC_G` §7's class letter was not earned by its own path set.**

## `E02-18` — statement of what this file did NOT establish

1. **No live database.** Every referential-action, index and constraint statement is read from the
   source that would emit it. `E02-01` is `NOT PROVEN` as to the deployed schema.
2. **`SRC/addons_archive` was searched for the rate table, the reversal field, `l10n_*` names and
   migration directories only** — not for suppression tokens, elevation, `ondelete` or DDL.
3. **The three project custom addon sets were not searched by either panel.**
4. **Test fixtures were excluded from every pattern** by the round instruction — and they are
   frequently the only place a branch-company or company-less rate row is constructed, so the
   *reachability* evidence was excluded by the search design itself.
5. **Client-side code** was read only for the v19 aggregator's emission and suppression.
6. **The 64-file canonical baseline was not read by either panel.** `MCU-12` is unaffected.
