# MCC_E00 — FX RATE-TABLE PRIMARY EVIDENCE (LAYER 2 / AUDIT QUARANTINE)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Branch `research/account-wave-a-mcc-2026-09-04-001`
Parent commit `33cdc6fa009c4eafcca543c253ccad19e97fd0dc`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Contains `file:line` citations and vendor tokens
> against a reference ERP source tree. Boss / PMO / AI-Audit visible only. MUST NOT be transcribed
> into any Layer 1 file, Team B design input, or downstream reference package. The Layer 1
> derivatives are `MCC_A` … `MCC_K`, which are vendor-token free.
> **`DR-NC-06` lineage rule: `MCE00` and `MCE02` are NOT edited. This file governs where it conflicts
> with either, for the specific claims it addresses and no others.**

---

## MCC-E-000 — Evidence source registry, re-tested this session

| Ref | Source | Location | Access |
|---|---|---|---|
| `SRC-A` | Reference ERP Enterprise, v18 line, build 20250608 — accounting addon | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/account/` | Read, verified |
| `SRC-C` | Framework base models, security, views, data | `.../odoo/addons/base/` | Read, verified |
| `SRC-E` | ORM core | `.../odoo/models.py` (7,615 lines) | Read, verified |
| `SRC-F` | Primary addon tree — bounding only | `.../odoo/addons/` — **791** directories, **790** with a manifest | Read, verified |
| **`SRC-G`** | **Archive addon tree — NEW, named by no prior round** | `.../odoo/addons_archive/` — **961** directories, **450** of them `*__dup_*` duplicates | Read, verified |
| `SRC-H` | Cross-version: v18 post-20260605, v19 community, v19 e-20260312, v19 e-20260417 | see `MCC-E-009` | Read, verified |
| `SRC-J` | Project custom addon sets, v18 line — three copies | `ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons`, `.../Odoo18/t8master/custom/addons`, `CLAUDE AI/MIGRATION/ODOO18/18.0.4_smeplus_v2/addons` | Read, verified |

**Access correction of record.** `MCE-000` declared `SRC-F` as the whole-tree bounding surface and
gave it as `addons/` alone. **`SRC-G` sits in the same deployment root and was never searched by any
round.** Every whole-tree negative claim in the programme is scoped to `SRC-F` only. Re-tests of the
four class-`A` claims over `SRC-G` are at `MCC-E-002`.

---

## MCC-E-001 — The rate-table surface: declared pattern, proven path set

**Pattern.** Files matching `res\.currency\.rate|res_currency_rate|model_res_currency_rate`, in
`.py` `.xml` `.csv`, excluding `/tests/`, `test_*`, `/i18n/`, `*__dup_*`.
**Path set.** `SRC-F` (791 dirs) + `SRC-G` (961 dirs) + framework core.

```
grep -rlE "res\.currency\.rate|res_currency_rate|model_res_currency_rate" \
  <root>/addons <root>/addons_archive <root> \
  --include='*.py' --include='*.xml' --include='*.csv' \
| grep -v "/tests/" | grep -v "/test_" | grep -v "/i18n/" | grep -v "__dup_" | sort -u
```

**Result — 20 files:**

| # | File | Layer |
|---|---|---|
| 1 | `base/models/res_currency.py` | model, resolvers, constraint |
| 2 | `base/security/base_security.xml` | record rule |
| 3 | `base/security/ir.model.access.csv` | access rows |
| 4 | `base/views/res_currency_views.xml` | form/list |
| 5 | `base/data/res_currency_rate_demo.xml` | demo data |
| 6 | `base/__manifest__.py` | data-file placement |
| 7 | `account/models/res_currency.py` | reporting currency table |
| 8 | `account/security/ir.model.access.csv` | access row (widening) |
| 9 | `account/report/account_invoice_report.py` | dependency map |
| 10 | `account_reports/models/account_multicurrency_revaluation_report.py` | unrealised FX |
| 11 | `currency_rate_live/models/res_config_settings.py` | external writer + cron |
| 12 | `spreadsheet/models/res_currency_rate.py` | client-callable endpoint |
| 13 | `spreadsheet/models/__init__.py` | registration |
| 14 | `sale_subscription/report/sale_order_log_report.py` | independent raw SQL |
| 15 | `addons_archive/l10n_eg_edi_eta/models/res_currency_rate.py` | localisation model extension |
| 16 | `addons_archive/l10n_eg_edi_eta/models/__init__.py` | registration |
| 17 | `addons_archive/l10n_uy/demo/res_currency_rate_demo.xml` | localisation demo data |
| 18 | `addons_archive/l10n_uy/__manifest__.py` | placement |
| 19 | `addons_archive/l10n_uy_edi/demo/res_currency_rate_demo.xml` | localisation demo data |
| 20 | `addons_archive/l10n_uy_edi/__manifest__.py` | placement |

**Prior-round comparison.** `MCE-007` enumerated rules over an undeclared path set and reached 6.
`MCX-03` reached ≥9. Neither enumerated the surface. **Files 14–20 appear in no prior round.**

**Pattern-completeness tests executed** (a declared pattern is not a proven one):

| False-negative mode | Command | Result |
|---|---|---|
| Reached via `currency.rate_ids` rather than the model name | `grep -rn "\.rate_ids\b" <SRC-F> <SRC-G> --include='*.py' --include='*.xml' \| grep -v tests \| grep -v __dup_ \| grep -v res_currency.py` | **10 hits, all unrelated models**: `l10n_ch_hr_payroll/models/l10n_ch_{additional_accident,sickness,accident}_insurance.py`, `l10n_be_account_disallowed_expenses_fleet/models/fleet_vehicle.py`, `l10n_ch_hr_payroll_elm_transmission/report/l10n_ch_master_data_report.xml`. **No miss.** |
| Named in a non-scanned extension | same roots, `--include='*.sql' --include='*.yml' --include='*.yaml' --include='*.js'` | **0 hits** |
| Reached by external id | `grep -rn "base.rate[A-Z]" <SRC-F> --include='*.py' --include='*.xml'` | **0 hits** |

**False positives of this round's own first pass** (recorded because a pattern's error rate is part
of its declaration): adding the token `rate_ids` returned
`account_disallowed_expenses/models/account_disallowed_expenses.py:15` and
`hr_payroll/models/hr_payroll_headcount.py:90,119` — unrelated models on both.

---

## MCC-E-002 — The four class-`A` claims, re-tested over `SRC-G`

| Claim | Original scope | Re-test over `SRC-G` (961 dirs) | Outcome |
|---|---|---|---|
| No `ir.rule` XML record anywhere targets either reconciliation model | `SRC-F` | `grep -rn "model_account_partial_reconcile\|model_account_full_reconcile" <SRC-G>` excluding access CSVs and `i18n` → **0** | **SURVIVES and STRENGTHENS.** Scope now 1,752 directories |
| No raw-SQL write to the rate table | this round | `grep -rniE "(insert into\|update)[[:space:]]+res_currency_rate"` over `SRC-F` + `SRC-G` → **0** | **HOLDS** |
| No override of the rate constraint | this round | `grep -rn "_check_company_id" <SRC-G> --include='*.py'` excluding tests → **0** | **HOLDS** |
| The rate-table surface is 14 files | this round, **first pass** | extending to `SRC-G` → **20** | **INVALIDATED BY ITS AUTHOR, SAME ROUND.** See `MCC_B` §3.2 |

---

## MCC-E-003 — The rate model, read at source

`SRC-C base/models/res_currency.py`

| Line | Element | Verbatim / effect |
|---|---|---|
| `335` | `class CurrencyRate(models.Model)` · `_name = "res.currency.rate"` | — |
| `340` | `_check_company_domain = models.check_company_domain_parent_of` | ancestors + null are admissible |
| `365-366` | `company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company.root_id)` | **not `required`**; default is the ROOT |
| `368-371` | `_sql_constraints`: `('unique_name_per_day', 'unique (name,currency_id,company_id)', …)`, `('currency_rate_check', 'CHECK (rate>0)', …)` | rate is strictly positive; uniqueness is 3-column |
| `389-396` | `_get_latest_rate` — `x.company_id == (self.company_id or self.env.company.root_id)` | **EXCLUDES null** |
| `399-405` | `_get_last_rates_for_companies` — `x.rate and x.company_id == company or not x.company_id` | **INCLUDES null** |
| `458-462` | `@api.constrains('company_id')` `_check_company_id`: `if rate.company_id.sudo().parent_id: raise ValidationError("Currency rates should only be created for main companies")` | **forbids a branch-scoped row** |

`SRC-E odoo/models.py:188-204` — `check_company_domain_parent_of` returns
`['|', ('company_id','=',False), ('company_id','parent_of', companies)]` (string form) or, for a
recordset, `[('company_id','in', [<every ancestor id>] + [False])]`.

---

## MCC-E-004 — Operator precedence in `_get_last_rates_for_companies` — a defect in its own right

`SRC-C base/models/res_currency.py:399-405`, verbatim:

```python
def _get_last_rates_for_companies(self, companies):
    return {
        company: company.sudo().currency_id.rate_ids.filtered(lambda x: (
            x.rate
            and x.company_id == company or not x.company_id
        )).sorted('name')[-1:].rate or 1
        for company in companies
    }
```

Python binds this as `((x.rate and (x.company_id == company)) or (not x.company_id))`.
**The `x.rate` truthiness guard applies only to the company-scoped branch.** A company-less row is
admitted regardless of its rate value. In this build a zero rate is excluded by the check constraint
at `:370`, so the reachable consequence is confined to **precedence being different from apparent
intent** rather than to a zero-rate admission — but the same expression is unchanged in v19
(`:410-417`), and the guard is load-bearing the moment the check constraint is relaxed or a NULL rate
becomes reachable.

**Class: `VERIFIED FACT` (source) · `NOT PROVEN` (runtime consequence in this build) · latent.**

---

## MCC-E-005 — The fourteen company-scoping expressions over one rate table

| # | Site | Expression | Nulls | Record rules | R/W | In `MCE-007`'s 6? | In `MCX-03`'s ≥9? |
|---|---|---|---|---|---|---|---|
| 1 | `base/security/base_security.xml:62-66` | `['\|',('company_id','parent_of',company_ids),('company_id','=',False)]` | **incl** | is the rule | R | yes | yes |
| 2 | `base/models/res_currency.py:130` `_get_rates` main | `('company_id','in',(False, company.root_id.id))` | **incl** | apply | R | yes | yes |
| 3 | `base/models/res_currency.py:134` `_get_rates` fallback | same, ordered ASC — the **earliest rate ever** | **incl** | apply | R | **no** | **no** |
| 4 | `base/models/res_currency.py:365-366` | default `env.company.root_id` | n/a | n/a | W | yes (rule 5) | yes |
| 5 | `base/models/res_currency.py:389-396` `_get_latest_rate` | `== (self.company_id or env.company.root_id)` | **excl** | apply | R | no | yes (8) |
| 6 | `base/models/res_currency.py:399-405` `_get_last_rates_for_companies` | `== company or not x.company_id` | **incl** | apply | R | yes | yes (9) |
| 7 | `base/models/res_currency.py:294-308` `_select_companies_rates` | `JOIN res_company c ON (r.company_id is null or r.company_id = c.id)`, `COALESCE(r.company_id, c.id)` | **incl, and attributes each null row to EVERY company** | **bypassed** | R | yes | yes |
| 8 | `base/models/res_currency.py:458-462` `_check_company_id` | root-only write constraint | n/a | n/a | W | **no** | yes (7) |
| 9 | `account/models/res_currency.py:180-183` `_get_table_builder_current` | `rate.company_id = <main_company.root_id.id>` | **excl** | **bypassed** | R | partly (rule 6, misattributed) | no |
| 10 | `account/models/res_currency.py:208-211` `_get_table_builder_closing` | same | **excl** | **bypassed** | R | no | no |
| 11 | `account/models/res_currency.py:254-258` `_get_table_builder_historical` | same | **excl** | **bypassed** | R | no | no |
| 12 | `account/models/res_currency.py:294-321` `_get_table_builder_average` | same, 3 predicates | **excl** | **bypassed** | R | no | no |
| 13 | `account/models/res_currency.py:229` `_get_currency_table_fiscal_year_bounds` | `_check_company_domain(main_company)` → ancestors + null | **incl** | apply | R | **misattributed as "the accounting currency table"** | no |
| 14 | `sale_subscription/report/sale_order_log_report.py:78-81` | `rcr.company_id IS NULL OR (rcr.company_id = <main_company_id> AND rcr.name <= CURRENT_DATE)` | **incl** | **bypassed** | R | no | no |

**Totals: 14 expressions · 6 INCLUDE nulls · 6 EXCLUDE nulls · 2 write-side.**
**Raw-SQL (record-rule-bypassing) read sites over the rate table: 8** — items 7, 9, 10, 11, 12, 14
plus the two additional predicates inside item 12. **Raw-SQL WRITE sites: 0.**

`MCC-E-005a` — **correction to `MCE-008`.** `MCE-008` states the accounting currency table is
"the separate path at `account/models/res_currency.py:218-240`". Line `229` is inside
`_get_currency_table_fiscal_year_bounds`, which locates the **earliest** rate row to bound fiscal
years. The currency table's own rate selection is items 9–12, and it uses the **opposite** null
semantics to line `229`. **`MCE-008`'s correction of `AC-02` stands; its replacement attribution is
corrected here.**

---

## MCC-E-006 — `_compute_current_rate`: a latent internal divergence

`SRC-C base/models/res_currency.py:150-158`:

```python
def _compute_current_rate(self):
    date = self._context.get('date') or fields.Date.context_today(self)
    company = self.env['res.company'].browse(self._context.get('company_id')) or self.env.company   # 152
    to_currency = self.browse(self.env.context.get('to_currency')) or company.currency_id           # 153
    currency_rates = (self + to_currency)._get_rates(self.env.company, date)                        # 155
```

Line `152` honours a context company; line `155` **ignores it** and passes `self.env.company`.
Reading `.rate` with `context['company_id']` set therefore selects the target currency by one company
and the rate by another.

**Reachability tested.** `grep -rn "with_context(company_id=" <SRC-F> --include='*.py' | grep -v /tests/`
→ **3 sites**, all on sequence and product models; **none reads a currency rate**. The normal entry
point `_get_conversion_rate` (`:266-271`) uses `with_company(company)`, which sets `env.company`, so
that path is consistent.

**Disposition: `VERIFIED FACT` (source) · `NOT REACHABLE FROM ANY SHIPPED CALLER` within `SRC-F`,
class `B` · LATENT.** Material for SMEsPlus because a custom report or an SMEsPlus module setting
`company_id` in context would hit it silently.

---

## MCC-E-007 — Shipped data: closes `MCU-07`

**Pattern:** every `res.currency.rate` record in `.xml` and `.csv` across `SRC-F` + `SRC-G`, with its
manifest placement resolved to `data` (always loaded) or `demo` (loaded only with demo data).

| File | Records | `company_id` present | Placement |
|---|---|---|---|
| `base/data/res_currency_rate_demo.xml` | **162** | **0 — every row is NULL-company** | `base/__manifest__.py:81`, inside `'demo'` |
| `addons_archive/l10n_uy/demo/res_currency_rate_demo.xml` | 1 | 1 — `base.demo_company_uy` | `__manifest__.py:53`, `'demo'` |
| `addons_archive/l10n_uy_edi/demo/res_currency_rate_demo.xml` | 2 | 2 — `base.demo_company_uy` | `__manifest__.py:48`, `'demo'` |
| **Any file in a `'data'` list** | **0** | — | — |

> **`MCU-07` CLOSED — VERIFIED.**
> **A production database created without demo data ships ZERO rate rows and therefore zero
> null-company rate rows.** A database created **with** demo data ships **162 null-company rate rows**
> — one per currency — every one of which is admitted by the record rule's explicit `False` disjunct
> and consumed by all six null-including resolvers, for every company in the database.
> **No localisation module ships a rate row into `data`.** Class `A — verified absence within
> `SRC-F` + `SRC-G`, `.xml`/`.csv`, manifest-resolved.

**Migration and onboarding consequence.** SMEsPlus onboarding that clones or seeds from a
demo-enabled template carries all 162 rows. They are invisible in the accounting UI's company filter
because they have no company.

---

## MCC-E-008 — Access and reachability of the rate table, by verb

| Grant | Group | R | W | C | U | Source |
|---|---|---|---|---|---|---|
| `access_res_currency_rate_public` | public | 1 | 0 | 0 | 0 | `base/security/ir.model.access.csv:60` |
| `access_res_currency_rate_portal` | portal | 1 | 0 | 0 | 0 | `:61` |
| `access_res_currency_rate_employee` | internal user | 1 | 0 | 0 | 0 | `:62` |
| `access_res_currency_rate_group_system` | system | 1 | 1 | 1 | 1 | `:64` |
| **`access_res_currency_rate_account_manager`** | **accounting manager** | **1** | **1** | **1** | **1** | **`account/security/ir.model.access.csv:7`** |

**Record rule** — `base/security/base_security.xml:62-66`, `res_currency_rate_rule`, no group
restriction, so it is **global**: `['|', ('company_id','parent_of',company_ids), ('company_id','=',False)]`.

| Verb | Reachable by | Bounded by |
|---|---|---|
| READ | public, portal, employee, accounting manager, system | the global record rule |
| WRITE / CREATE / UNLINK | **accounting manager**, system | the same rule; the company field is editable in the form at `base/views/res_currency_views.xml:20,44,169`, gated only by `base.group_multi_company` |
| INDIRECT WRITE — external feed | `currency_rate_live/models/res_config_settings.py:290`, `create({... 'company_id': company.id})` | iterated companies |
| INDIRECT WRITE — scheduled | `:1326-1332` `run_update_currency`, domain includes `('parent_id','=',False)` — **root companies only** | cron |
| INDIRECT WRITE — manual settings button | `:1374-1376` `update_currency_rates_manually` → `self.company_id.update_currency_rates()`, `self.company_id` is the **acting** company | see `MCC-E-010` |
| INDIRECT READ — client RPC | `spreadsheet/models/res_currency_rate.py:8-18`, `_get_rate_for_spreadsheet(..., company_id=None)`, caller-supplied id, `browse()` without an access check | the record rule, which returns **par** rather than an error when it denies |

**`AC-01` re-verified: CONFIRMED.** The accounting addon widens the framework grant from
system-only write to a routine business role. **New this round:** the framework additionally grants
**READ to the public and portal roles**, which no prior round recorded.

---

## MCC-E-009 — Cross-version stability

| Tree | LOC | `_check_company_id` | `_get_rates` root+null | default root | uniqueness | precedence defect `MCC-E-004` |
|---|---|---|---|---|---|---|
| v18 e-20250608 (`SRC-A`/`SRC-C`) | 489 | `:459-462` | `:130`,`:134` | `:366` | `:369` `_sql_constraints` | present `:399-405` |
| v18 post-20260605 | 492 | present | present | `:369` | `_sql_constraints` | present |
| v19 community | 503 | `:470-473` | `:128`,`:132` | `:373` | `models.Constraint` (new API) | present `:410-417` |
| v19 e-20260312 | 503 | present | present | `:373` | `models.Constraint` | present |
| v19 e-20260417 | 503 | present | present | `:373` | `models.Constraint` | present |
| **v16 / v14** | — | — | — | — | — | — |

> **`VERIFIED`: the rate-table company-scoping model is STABLE across the v18 and v19 lines**, in
> every element tested. Only the constraint-declaration API changed (`_sql_constraints` list →
> `models.Constraint` descriptor); the SQL text is identical.
>
> **`C — NOT YET SEARCHED`: no v16 or v14 framework core exists in the searched roots.**
> `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo16/` and `.../Odoo14/` contain **project custom addons
> only**, not a core tree. **The pre-v18 baseline is therefore NOT established, and the residual at
> `MCC_C` §7 — rows predating the constraint, carried in by upgrade — cannot be closed from the
> sources available here.** This is `NOT SEARCHED`, not absence.

---

## MCC-E-010 — Bypass enumeration, executed

| # | Candidate | Command / read | Result |
|---|---|---|---|
| 1 | raw-SQL `INSERT`/`UPDATE` on the rate table | `grep -rniE "(insert into\|update)[[:space:]]+res_currency_rate" <SRC-F> <SRC-G> --include='*.py'` | **0** |
| 2 | the 62 accounting raw-SQL sites | cross-checked against the rate-table site list | **none touches the rate table** |
| 3 | context flag skipping constraints | `SRC-E odoo/models.py:1622-1631` `_validate_fields(field_names, excluded_names=())` — no skip parameter; callers `:4813`, `:4836`, `:5052`, `:5275`, `:5285`; `grep -n "constraint" models.py \| grep -iE "skip\|disable\|bypass"` → **0** | **no skip exists** |
| 4 | write not validating | `:4813` `real_recs._validate_fields(vals, inverse_fields)` inside `write` | **fires whenever `company_id` is in vals** |
| 5 | create not validating | `:5274` `records._validate_fields(name for data in data_list for name in data['stored'])`; the field carries a default, so it is always in `stored` | **fires** |
| 6 | `sudo()` | constraints are user-independent | **no effect** |
| 7 | make the company a branch after the rows exist | `SRC-C base/models/res_company.py:365-366` — `if 'parent_id' in values: raise UserError(_("The company hierarchy cannot be changed."))` | **BLOCKED unconditionally** |
| 8 | raw-SQL write to `res_company` | `grep -rniE "(insert into\|update)[[:space:]]+res_company" <SRC-F> --include='*.py'` → **10 hits, all in `/tests/`, all on `currency_id`, none on `parent_id`** | **no non-test site** |
| 9 | migration scripts | 5 `migrations/` directories in `SRC-F`; `grep -rn "res_currency_rate" … \| grep -i "migrat\|upgrade"` → **0** | **none touches the rate table** |
| 10 | localisation / custom override of the constraint | `SRC-G` → 0; `SRC-J` (3 custom copies) → **no module touches the rate table at all** | **none** |
| 11 | data/XML loading | records load through ORM `create` | **constraint fires** |
| 12 | **module upgrade over pre-existing rows** | constraints are not re-run on existing rows at upgrade; no v16/v14 core available to establish whether such rows could pre-exist | **`D` — OPEN RESIDUAL** |

---

## MCC-E-011 — Company-currency root delegation: the structural control

| Line | Element |
|---|---|
| `base/models/res_company.py:95-103` | `_get_company_root_delegated_field_names` → `['currency_id']` |
| `account/models/company.py:281-287` | override → `+ ['fiscalyear_last_day', 'fiscalyear_last_month', 'account_storno', 'tax_exigibility']` |
| `base/models/res_company.py:310-312` | on **create**, delegated fields are copied from the parent into vals |
| `base/models/res_company.py:381-388` | on **write** to a root, delegated fields are propagated to every descendant |
| `base/models/res_company.py:416-424` | `@api.constrains(delegated + ['parent_id'])` `_check_root_delegated_fields` raises if a branch's value differs from its parent's |
| `base/models/res_company.py:244` | in the form view, delegated fields are set `readonly="parent_id != False"` |
| `base/models/res_company.py:22`, `:37`, `:115-118` | `_parent_store`; `parent_id` `ondelete='restrict'`; `root_id` computed from `parent_path` |

> **A branch company cannot hold a company currency different from its root's.** Four enforcement
> layers. **Consequence for `FX-08`:** resolving a branch's rates at root scope is not a scope
> mismatch — the branch's company currency *is* the root's, so the root's rate table is the
> semantically correct source. The `G03` scenario's economic premise does not hold on this build.
>
> **Also material and not previously recorded:** the **fiscal year definition** is likewise
> root-delegated, so a branch cannot close on a different fiscal calendar from its root.

---

## MCC-E-012 — Statement of what this file did NOT search

1. **No live database.** Every runtime statement is read from source. NULL-comparison behaviour under
   the three-column uniqueness rule (`MCC-E-003`, `:369`) remains `INFERENCE`.
2. **No v16 / v14 framework core** exists in the searched roots — `MCC-E-009`. The upgrade residual
   cannot be closed here.
3. **JavaScript / OWL client code** was searched only for the table name (0 hits), not read.
4. **Which of the three project custom addon copies deploys** is unknown; all three were searched and
   none touches the rate table, so the ambiguity does not affect the result.
5. **Whether `SRC-G` is on the runtime addons path** is a deployment configuration question. It is
   referenced by no code or config in the tree; the path is `tools.config['addons_path']`
   (`odoo/modules/module.py:132`), a runtime value. **`D — UNKNOWN`**, and raised as a new unknown.
6. **`.po` translation catalogues** were excluded by the declared pattern throughout.
