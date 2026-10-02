# U102 — Migration Scripts — Hook Patterns (L3/L10) — P0
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
**Unit**: U102
**Phase**: Third-Pass — P0 GAP-033 Close
**Scope**: Migration script infrastructure, pre/post/end_migrate hooks, field rename patterns, SQL migration, init hooks
**Modules surveyed**: account, stock, mrp, sale, purchase, analytic, project, hr_expense, hr_holidays, website_hr_recruitment, l10n_de, l10n_mx, l10n_fr_account, l10n_nl, l10n_br (migrations/ and upgrades/ subdirectories)
**Function-IDs targeted**: NEW:U102-F01 through U102-F28
**L-levels**: L3, L10
**Proof layers**: P1
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: None (first migration study)

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U102-001 | U102-F01 | odoo/modules/migration.py:58-88 | class MigrationManager | INFRA | always | VERIFIED | `MigrationManager` class manages migration of modules; migration files must be Python files containing `migrate(cr, installed_version)` function, placed under `migrations/<version>/` or `upgrades/<version>/` subdirectories | NR-U102-001 |
| U102-002 | U102-F02 | odoo/modules/migration.py:63-66 | class MigrationManager docstring | INFRA | always | VERIFIED | Three stages are supported: `pre-` scripts run before module init, `post-` scripts run after module init, `end-` scripts run after ALL modules have been updated | NR-U102-002 |
| U102-003 | U102-F03 | odoo/modules/migration.py:69-70 | class MigrationManager docstring | INFRA | always | VERIFIED | A special folder named `0.0.0` contains scripts run on any version change; in `pre` stage `0.0.0` scripts run first; in `post`/`end` stages they run last | NR-U102-003 |
| U102-004 | U102-F04 | odoo/modules/migration.py:138-141 | MigrationManager._get_files | INFRA | pkg load_state == 'to upgrade' | VERIFIED | Migration script discovery checks two subdirectory paths per module: `<module>/migrations/` (key: `module`) and `<module>/upgrades/` (key: `module_upgrades`); external scripts also loaded from `odoo.upgrade.<pkg>` namespace | NR-U102-004 |
| U102-005 | U102-F05 | odoo/modules/migration.py:218-253 | exec_script | INFRA | always | VERIFIED | `exec_script(cr, installed_version, pyfile, addon, stage, version)` loads each migration Python file and calls `mod.migrate(cr, installed_version)`; valid `migrate` signatures are `(cr, version)` or `(_cr, _version)` positional-only variants | NR-U102-005 |
| U102-006 | U102-F06 | odoo/modules/migration.py:238-250 | exec_script | INFRA | always | VERIFIED | `exec_script` enforces that every migration file exposes a `migrate` function; absence raises `AttributeError`; wrong signature raises `TypeError` | NR-U102-006 |
| U102-007 | U102-F07 | odoo/modules/migration.py:31-55 | VERSION_RE | INFRA | always | VERIFIED | `VERSION_RE` regex validates version directory names; accepts `x.0` format (e.g. `19.0`), multi-digit server versions, and module-only versions (e.g. `1.4`, `9.0.1.2`); `tests` folder is explicitly excluded | NR-U102-007 |
| U102-008 | U102-F08 | odoo/modules/migration.py:192-209 | migrate_module._compare | INFRA | version comparison | VERIFIED | Scripts for a given version directory execute only when the installed version is less than the target version (`parsed_installed_version < parse_version(full_version) <= current_version`); major-less versions compare only module version parts | NR-U102-008 |
| U102-009 | U102-F09 | odoo/addons/purchase/migrations/9.0.1.2/pre-create-properties.py:33-37 | migrate() | PATTERN | pre stage | VERIFIED | `purchase` module version `9.0.1.2` pre-migration: `migrate(cr, version)` calls `convert_field()` twice to migrate `res.partner.property_purchase_currency_id` and `product.template.property_account_creditor_price_difference` from relational columns to `ir.property` records, then drops the source columns via `ALTER TABLE ... DROP COLUMN ... CASCADE` | NR-U102-009 |
| U102-010 | U102-F10 | odoo/addons/purchase/migrations/9.0.1.2/pre-create-properties.py:3-31 | convert_field() | PATTERN | pre stage | VERIFIED | `convert_field(cr, model, field, target_model)` first checks column existence via `information_schema.columns` query; if absent returns early; otherwise inserts `ir.property` rows then drops the column — a safe idempotency guard | NR-U102-010 |
| U102-011 | U102-F11 | odoo/addons/project/migrations/1.4/post-migrate.py:1-7 | migrate() | PATTERN | post stage | VERIFIED | `project` module version `1.4` post-migration: imports `api, SUPERUSER_ID`; creates `api.Environment(cr, SUPERUSER_ID, {})` and calls `env.ref()` to activate a mail template record | NR-U102-011 |
| U102-012 | U102-F12 | odoo/addons/analytic/migrations/1.2/pre-migrate.py:1-31 | migrate() | PATTERN | pre stage | VERIFIED | `analytic` module version `1.2` pre-migration: imports `odoo.tools.sql`; uses `cr.execute()` with parameterised SQL to query `ir_config_parameter` and `account_analytic_plan`; calls `sql.drop_constraint()` and `sql.add_foreign_key()` to change FK constraint ON DELETE from SET NULL to RESTRICT across dynamic column names | NR-U102-012 |
| U102-013 | U102-F13 | odoo/addons/hr_expense/migrations/2.1/pre-migrate.py:1-28 | migrate() | PATTERN | pre stage | VERIFIED | `hr_expense` module version `2.1` pre-migration: uses `api.Environment` to resolve XML IDs with `raise_if_not_found=False`; then executes parameterised `UPDATE mail_message_subtype SET "default" = false WHERE id in %s` — mixed ORM+SQL pattern | NR-U102-013 |
| U102-014 | U102-F14 | odoo/addons/website_hr_recruitment/migrations/17.0.1.1/pre-migrate.py:1-13 | migrate() | PATTERN | pre stage | VERIFIED | `website_hr_recruitment` version `17.0.1.1` (server-versioned migration): `migrate(cr, version)` uses `cr.execute()` with `REGEXP_REPLACE` on `ir_ui_view.arch_db` (jsonb column cast to text) to strip a CSRF token div — direct SQL regex on view XML | NR-U102-014 |
| U102-015 | U102-F15 | odoo/addons/l10n_de/migrations/2.0/pre-migrate.py:14-57 | migrate() | PATTERN | pre stage | VERIFIED | `l10n_de` version `2.0` pre-migration: local helper `rename_tag(cr, old_tag, new_tag)` issues `UPDATE ir_model_data SET name=... WHERE module='l10n_de' AND name=...`; `migrate()` also issues `DELETE FROM ir_model_data` to prevent ORM removal of in-use records before renaming tags | NR-U102-015 |
| U102-016 | U102-F16 | odoo/addons/l10n_de/migrations/1.1/post-migrate_update_amls.py:1-39 | migrate() | PATTERN | post stage | VERIFIED | `l10n_de` version `1.1` post-migration: creates `api.Environment`; resolves account tags via `env['account.account.tag']._get_tax_tags()`; executes parameterised `UPDATE account_account_tag_account_move_line_rel` to remap tag foreign keys — ORM lookup + direct SQL update on many2many relation table | NR-U102-016 |
| U102-017 | U102-F17 | odoo/addons/l10n_de/migrations/3.0/pre-migrate.py:1-22 | migrate() | PATTERN | pre stage | VERIFIED | `l10n_de` version `3.0` pre-migration: creates `api.Environment(cr, SUPERUSER_ID, {})`; resolves report/column refs with `raise_if_not_found=False`; executes `DELETE FROM account_report_column`, `DELETE FROM account_report_line`, and `UPDATE account_report_line SET code = NULL` | NR-U102-017 |
| U102-018 | U102-F18 | odoo/addons/l10n_mx/migrations/2.4/post-migrate.py:1-19 | migrate() | PATTERN | post stage | VERIFIED | `l10n_mx` version `2.4` post-migration: imports `odoo.fields.Domain`; searches companies with `chart_template == 'mx'`; uses `Domain.AND` + `Domain.OR` composition to build domain; calls `env['account.account'].with_company(company).search(domain)` and writes `account_type` — ORM-only post-migrate with domain API | NR-U102-018 |
| U102-019 | U102-F19 | odoo/addons/l10n_mx/migrations/2.2/end-migrate.py:1-7 | migrate() | PATTERN | end stage | VERIFIED | `l10n_mx` version `2.2` end-migration: calls `env['account.chart.template'].try_loading('mx', company, force_create=False)` for each company — `end-` stage pattern for chart template reload after all modules settled | NR-U102-019 |
| U102-020 | U102-F20 | odoo/addons/l10n_fr_account/migrations/2.1/end-migrate_update_taxes.py:1-8 | migrate() | PATTERN | end stage | VERIFIED | `l10n_fr_account` version `2.1` end-migration: `migrate()` iterates companies with `chart_template == 'fr'` and calls `try_loading('fr', company, force_create=False)` — same end-stage chart reload pattern as l10n_mx | NR-U102-020 |
| U102-021 | U102-F21 | odoo/addons/project/upgrades/1.3/pre-migrate.py:1-14 | migrate() | PATTERN | pre stage | VERIFIED | `project` module uses `upgrades/` directory (not `migrations/`); version `1.3` pre-migrate executes `UPDATE ir_model_access ... FROM ir_model_data ... WHERE d.module = 'project'` to fix an access rule — `upgrades/` is an equally valid path for module-level migration scripts | NR-U102-021 |
| U102-022 | U102-F22 | odoo/addons/hr_holidays/upgrades/1.6/pre-migrate.py:1-13 | migrate() | PATTERN | pre stage | VERIFIED | `hr_holidays` version `1.6` under `upgrades/`: updates `ir.rule.domain_force` via parameterised SQL join with `ir_model_data` — demonstrates `upgrades/` as valid alternative to `migrations/` for multi-company domain rule correction | NR-U102-022 |
| U102-023 | U102-F23 | odoo/addons/stock/__init__.py:11-15 | pre_init_hook | HOOK | install | VERIFIED | `stock` module `pre_init_hook(env)` (declared in `__manifest__` as `'pre_init_hook': 'pre_init_hook'`) runs before module XML data loads; searches `ir.model.data` for stock-model entries and unlinks them — a workaround for stale model data | NR-U102-023 |
| U102-024 | U102-F24 | odoo/addons/stock/__init__.py:17-25 | _assign_default_mail_template_picking_id | HOOK | post-install | VERIFIED | `stock` module `post_init_hook` function `_assign_default_mail_template_picking_id(env)` searches companies missing `stock_mail_confirmation_template_id` and assigns `env.ref('stock.mail_template_data_delivery_confirmation')` | NR-U102-024 |
| U102-025 | U102-F25 | odoo/addons/stock/__init__.py:27-29 | uninstall_hook | HOOK | uninstall | VERIFIED | `stock` module `uninstall_hook(env)` unlinks all `stock.picking.type` sequences — cleans up sequence records that belong to picking types when module is removed | NR-U102-025 |
| U102-026 | U102-F26 | odoo/addons/account/__init__.py:22-24 | _account_post_init | HOOK | post-install | VERIFIED | `account` module `post_init_hook` `_account_post_init(env)` calls `_set_fiscal_country(env)` (computes `account_tax_fiscal_country` on all companies) and `_create_batch_payment_sequence(env)` (creates batch payment sequences for companies missing one) | NR-U102-026 |
| U102-027 | U102-F27 | odoo/addons/mrp/__init__.py:10-16 | _pre_init_mrp | HOOK | pre-install | VERIFIED | `mrp` module `pre_init_hook` `_pre_init_mrp(env)` issues two direct `env.cr.execute()` `ALTER TABLE "stock_move" ADD COLUMN` statements to add `unit_factor double precision` and `manual_consumption boolean` before ORM initialisation — prevents ORM-computed-stored-field slowness on large tables | NR-U102-027 |
| U102-028 | U102-F28 | odoo/addons/mrp/__init__.py:18-24 | _create_warehouse_data | HOOK | post-install | VERIFIED | `mrp` module `post_init_hook` `_create_warehouse_data(env)` searches warehouses with `manufacture_pull_id == False` and writes `{'manufacture_to_resupply': True}` — backfills warehouse data for warehouses that existed before mrp was installed | NR-U102-028 |
| U102-029 | U102-F29 | odoo/addons/sale/__init__.py:13-30 | _post_init_hook | HOOK | post-install | VERIFIED | `sale` module `post_init_hook` `_post_init_hook(env)` calls `_synchronize_crons(env)` (syncs cron active state from `ir.config_parameter`) and `_setup_downpayment_account(env)` (sets downpayment account from chart template data per company) | NR-U102-029 |
| U102-030 | U102-F30 | odoo/tools/sql.py:338-356 | column_exists | UTIL | any migration | VERIFIED | `odoo.tools.sql.column_exists(cr, tablename, columnname)` queries `pg_attribute` join `pg_class`/`pg_namespace` to detect column existence; used in migration scripts as idempotency guard before structural changes | NR-U102-030 |
| U102-031 | U102-F31 | odoo/tools/sql.py:377-385 | rename_column | UTIL | any migration | VERIFIED | `odoo.tools.sql.rename_column(cr, tablename, columnname1, columnname2)` executes `ALTER TABLE ... RENAME COLUMN` using `SQL.identifier()` for safe quoting | NR-U102-031 |
| U102-032 | U102-F32 | odoo/tools/sql.py:499-517 | drop_constraint / add_foreign_key | UTIL | any migration | VERIFIED | `sql.drop_constraint(cr, tablename, constraintname)` and `sql.add_foreign_key(cr, tablename1, columnname1, tablename2, columnname2, ondelete)` provide safe wrappers for constraint DDL operations used in migration scripts | NR-U102-032 |

---

## Structural Findings

### Migration Directory Discovery (VERIFIED)
The following primary target modules do NOT have `migrations/` or `upgrades/` directories in this 19.0 source tree:
- `account/` — no migrations dir
- `stock/` — no migrations dir
- `mrp/` — no migrations dir
- `sale/` — no migrations dir
- `hr/` — no migrations dir

These modules use `pre_init_hook` / `post_init_hook` / `uninstall_hook` declared in `__manifest__.py` instead.

Modules WITH migrations directories:
- `analytic/migrations/1.2/` — pre-migrate.py
- `hr_expense/migrations/2.1/` — pre-migrate.py
- `project/migrations/1.4/` — post-migrate.py
- `purchase/migrations/9.0.1.2/` — pre-create-properties.py
- `website_hr_recruitment/migrations/17.0.1.1/` — pre-migrate.py
- Numerous `l10n_*` modules with multiple versions

Modules WITH upgrades directories:
- `project/upgrades/1.3/` — pre-migrate.py
- `hr_holidays/upgrades/1.6/` — pre-migrate.py
- `project_sms/upgrades/`, `hr_timesheet_attendance/upgrades/`, `point_of_sale/upgrades/`, `l10n_es/upgrades/`

### odoo.upgrade Namespace
`odoo/upgrade/` directory exists but contains only `.gitkeep` — it is a placeholder for external (OpenUpgrade/Enterprise) upgrade scripts not present in Community source.
