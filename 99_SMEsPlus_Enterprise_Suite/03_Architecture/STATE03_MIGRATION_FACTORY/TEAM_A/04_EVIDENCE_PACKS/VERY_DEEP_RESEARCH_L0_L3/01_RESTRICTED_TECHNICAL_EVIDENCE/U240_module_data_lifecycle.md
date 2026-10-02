# U240 — ir.module.module and ir.model.data Lifecycle — Restricted Technical Evidence

**RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**

| Item | Value |
|---|---|
| Unit | U240 |
| Group | module_data_lifecycle |
| Source revision | odoo 19.0.post20260921, Community only |
| Research date | 2026-10-03 |
| Status | DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION |
| Pointer base | addons pointers are relative to `odoo/addons/`; core pointers start with `odoo/` |
| Claims table | `02_NEUTRAL_KNOWLEDGE/U240_module_data_lifecycle_NEUTRAL.md` (26 claims, U240-C01..C26) |

## 0. Conventions

- OBSERVED = read in the v19 source at the cited path:line.
- RT = behaviour that needs execution to confirm; not executed (Odoo was never started).
- UNKNOWN — EVIDENCE INSUFFICIENT = not determinable from source read.
- PRIOR-VERSION-KNOWLEDGE = comparison with v16/v17 from memory, not verified in this tree.
- No V-levels, coverage percentages or Gate PASS wording are assigned.
- Manifest prevalence numbers come from a read-only scripted AST scan over `odoo/addons/*/__manifest__.py` (692 manifests, 0 parse errors, run 2026-10-03; script kept in the session scratchpad, not committed). They have no path:line pointer.

## 0.1 Scope and not read

Read: `odoo/modules/{loading,module,db,module_graph,migration}.py`, `odoo/orm/registry.py`, relevant parts of `odoo/orm/models.py`, `odoo/orm/fields_relational.py`, `odoo/orm/environments.py`, `odoo/tools/convert.py`, `odoo/import_xml.rng`, `base/models/{ir_module,ir_model,ir_ui_view}.py`, `base/wizard/*module*`, `base/data/base_data.sql`, `base/__manifest__.py`, `base/__init__.py`, `l10n_th` manifest/init/models, `account/models/{chart_template,ir_module}.py`. Not read: Enterprise, Extra, OEEL modules (the license list in ir_module.py is only quoted). Not read: `load_openerp_module` code after line 523 (traceback hints for circular imports). Migration-script patterns belong to U102.

## 1. Architecture map

- Loading code lives in `odoo/modules/` (`loading.py` 633 lines, `migration.py` 254, `module.py`, `module_graph.py` 318, `db.py` 201) and `odoo/orm/registry.py` (1296 lines). `odoo/modules/registry/__init__.py:3` only re-exports `DummyRLock, Registry, _REGISTRY_CACHES, _CACHES_BY_KEY`.
- ORM-side models: `ir.module.category` (ir_module.py:76), `ir.module.module` (157), `ir.module.module.dependency` (1000), `ir.module.module.exclusion` (1066); `ir.model.data` (ir_model.py:2226).
- `_allow_sudo_commands = False` is set on all five (ir_module.py:80, 163, 1004, 1069; ir_model.py:2240). Semantics: `odoo/orm/models.py:457-462` (default True; disables relational commands through sudo/with_user environments) consumed in `odoo/orm/fields_relational.py:772-777`.
- Admin guard: `assert_log_admin_access` (ir_module.py:57-73) denies non-admin with a warning and AccessDenied (68-70), logs ALLOW otherwise (71). It decorates `button_install` 407, `button_immediate_install` 476, `button_reset_state` 495, `button_immediate_uninstall` 660, `button_uninstall` 669, `button_uninstall_wizard` 683, `button_immediate_upgrade` 695, `button_upgrade` 703, `update_list` 786.

## 2. Manifest handling (`odoo/modules/module.py`)

- `MANIFEST_NAMES = ['__manifest__.py']` 53. `_DEFAULT_MANIFEST` 56-96 (mandatory fields comment: author, license, name). Defaults: application False 62, bootstrap 63, assets 64, auto_install False 65, category 'Uncategorized' 66, cloc_exclude 67, configurator_snippets 68, configurator_snippets_addons 69, countries [] 70, data 71, demo 72, demo_xml 73, depends 74, description 75, external_dependencies 76, init_xml 77, installable True 78, images 79, images_preview_theme 80, kpi_providers 81, live_test_url 82, new_page_templates 83, post_init_hook '' 84, post_load '' 85, pre_init_hook '' 86, sequence 100 87, summary 88, test 89, theme_customizations 90, update_xml 91, uninstall_hook '' 92, version '1.0' 93, web 94, website 95. `excludes` is not in the defaults (read by `.get('excludes', [])` at ir_module.py:827).
- `Manifest` class 176; `__init__` 180-186; `description` 199-210; `version` 212-217; `__getitem__` deep-copies 231-234; `check_manifest_dependencies` 246-265 (python deps via `check_python_external_dependency`, binaries via `tools.find_in_path`, raises `MissingDependency`); `for_addon` 287-300; `_from_path` 302-315 (`ast.literal_eval`); `all_addon_manifests` 317-331 (sorted by name; first addons path wins duplicates); `get_module_path` 334-344.
- `_load_manifest` def 415: author default with warning 424-430; license default 'LGPL-3' with warning 432-434; base depends [] 436-437; empty depends -> ['base'] 438-440; auto_install handling 445-458 (comment: "special case: [] to always install the module" 445-449; iterable branch asserts triggers are dependencies 450-456; truthy non-iterable -> `set(depends)` 457-458); version through `adapt_version` 460-464; failing `check_version` -> warning and `installable=False` 465-467. `load_manifest` deprecated "Since 19.0" 399-401. `adapt_version` 550-566; `check_version` 569-579; `MissingDependency` 582-585; `check_python_external_dependency` 588-614.
- Resulting `Manifest['auto_install']` is False or a set of trigger dependency names (a set of all dependencies when True).

### 2.1 Manifest prevalence (scripted scan, OBSERVED 2026-10-03; method stated, no line pointer)

692 Community manifests. Keys present: application 34; auto_install 402 (True 252, non-empty list 150, empty list 0, absent 290); bootstrap 3; countries 157; demo 248; external_dependencies 5; installable 259 (installable false in 2); kpi_providers 1; post_init_hook 94; pre_init_hook 6; uninstall_hook 62. ZERO manifests carry post_load, excludes, init_xml, update_xml, demo_xml, test, web or cloc_exclude. pre_init_hook users: mrp:58 `_pre_init_mrp`, hr_timesheet:50 `_pre_init_hook`, l10n_dk_nemhandel:39 `_pre_init_nemhandel`, l10n_fr_pdp:38 `_pre_init_pdp`, stock:94 `pre_init_hook`, sale_management:73 `pre_init_hook`. uninstall_hook examples: stock:96, mrp:60, website:225, project:69 `_project_uninstall_hook`, point_of_sale:11, hr_timesheet:52 `_uninstall_hook`, l10n_eu_oss:28 `l10n_eu_oss_uninstall`, stock_sms:21 `_reset_sms_text_confirmation`, account_peppol_response:25 `_account_peppol_response_uninstall`, plus many payment providers.

## 3. DB bootstrap (`odoo/modules/db.py`)

- `is_initialized` 20-26; `initialize(cr)` def 29 creates base tables from `base/data/base_data.sql` (38-45), loops `Manifest.all_addon_manifests()` 47, `create_categories` 49-50, status 'uninstalled'/'uninstallable' by `installable` 52-55, raw INSERT into ir_module_module 57-68 (includes `web` column 59/65 and `info['auto_install'] is not False` 64), xmlid INSERT `module_<name>` with noupdate True 72-76, dependency INSERT with `auto_install_required = d in (info['auto_install'] or ())` 77-83.
- `skip_auto_install` option keeps only base 'to install' 85-89. Recursive auto-install SQL 91-124: first SELECT 95-107 selects modules with `auto_install`, state not in ('to install','uninstallable') and no dependency that is missing or (auto_install_required and not 'to install'); NO countries test; second SELECT 112-119; loop ends when empty 122-123; UPDATE to 'to install' 124.
- RT-flag: a manifest `auto_install: []` would have no required dependencies and be selected as soon as all dependencies exist by the SQL, while `button_install.must_install` (ir_module.py:418-422) would never select it (the `states` set built from required dependencies would be empty, so the `'to install' in states` test is false). Zero Community manifests use an empty list.
- `create_categories` 127-159 (xmlid `module_category_<path>` 140; comment "search via xml_id (because some categories are renamed)" 141; INSERT noupdate True 153-154). `has_unaccent` 168, `has_trigram` 192.
- `web`: no ORM field on ir.module.module; column exists in base_data.sql:63 and is filled in db.py:59/65; `_DEFAULT_MANIFEST` has it (module.py:94); no Community manifest sets it.

## 4. ir.module.module

### 4.1 States and fields
- `STATES` ir_module.py:140-147: uninstallable 'Uninstallable', uninstalled 'Not Installed', installed 'Installed', to upgrade 'To be upgraded', to remove 'To be removed', to install 'To be installed'. `DEP_STATES = STATES + [('unknown','Unknown')]` 997.
- Class 157-163: `_name` 158, `_rec_name = "shortdesc"` 159, `_description = "Module"` 161, `_order = 'application desc,sequence,name'` 162.
- Fields 274-335: name 'Technical Name' readonly required 274; category_id Many2one ir.module.category 275; shortdesc 276; summary 277; description 278; description_html compute 279; author 280; maintainer 281; contributors 282; website 283; comment 285-288 ("attention: Incorrect field names !!": installed_version = latest on disk; latest_version = installed in database; published_version = repository); installed_version labelled 'Latest Version' computed `_get_latest_version` 289; latest_version labelled 'Installed Version' 290; published_version 291; url 293; sequence 100 294; dependencies_id 295-296; country_ids M2M res.country relation `module_country` 297; exclusion_ids 298-299; auto_install 'Automatic Installation' 300-303; state default 'uninstallable' 304; demo default False 305; license Selection 306-317 default 'LGPL-3' with ten keys: GPL-2, GPL-2 or any later version, GPL-3, GPL-3 or any later version, AGPL-3, LGPL-3, Other OSI approved licence, OEEL-1, OPL-1, Other proprietary; menus_by_module / reports_by_module / views_by_module stored computed Text 318-320; application 321; icon 322; icon_image 323; icon_flag 324 (`_get_icon_image` 270-272 uses manifest countries when exactly one); to_buy default False 325; has_iap compute 326, `_compute_has_iap` 333-335.
- `_name_uniq` 328-331 message "The name of the module must be unique!".
- `_unlink_except_installed` 337-341 (`@api.ondelete(at_uninstall=False)`); `unlink` 343-345; `_get_modules_to_load_domain` 347-349.

### 4.2 Category model (ir_module.py:76-104)
`ir.module.category`: name 82, parent_id 83, child_ids 84, module_ids 85, privilege_ids (res.groups.privilege) 86, description 87, sequence 88, visible default True 89, exclusive 90, xml_id computed 91 (`_compute_xml_id` 93-99). `_order = 'sequence, name, id'` 79. `_check_parent_not_circular` 101-104 message "Error ! You cannot create recursive categories." `_update_category` 863-878 (ancestry-loop fix with warning 870-872, delegates to `modules.db.create_categories` 877).

### 4.3 Dependency and exclusion models (ir_module.py:995-1105)
- Dependency: name indexed 1007; module_id cascade 1010; depend_id computed/searchable 1013-1014; state computed 1015 (`_compute_state` 1039-1042 `depend_id.state or 'unknown'`); auto_install_required default True 1017-1020; `_log_access = False` 1003 (inserts manual); `_compute_depend` 1022-1031; `_search_depend` 1033-1037 (only `in`/`any`); `all_dependencies` 1044-1063.
- Exclusion: name 1072; module_id cascade 1075; exclusion_id computed 1078-1079; state 1080; `_compute_exclusion` 1082-1091; `_search_exclusion` 1093-1097; `_compute_state` 1099-1102. No `_log_access = False` on exclusion.
- Dependency state derivation: only through the linked module's state; missing -> 'unknown'.

### 4.4 Discovery
`update_list` (decorators 786-787; def 788-822): `res = [0, 0]` 789; per manifest 796-799; existing module updates only differing truthy values 801-808, resets 'uninstallable' to 'uninstalled' when installable 807-808, counts update when manifest version newer than `latest_version` 809-810; new module created 816-818; `_update_from_terp` 820 -> `_update_dependencies` 825 (raw INSERT/DELETE 830-841, `auto_install_required = (name = any(%s))` 838), `_update_countries` 826 (843-851), `_update_exclusions` 827 (853-861), `_update_category` 828. `get_values_from_terp` 752-769 (description dedent, author default 'Unknown', license default 'LGPL-3', sequence 100, `auto_install ... is not False` 764, `to_buy: False`). `create` 771-783 writes xmlid `module_<name>` in base with noupdate True (779) and clears the stable cache (782). `_get_id` cached with `@tools.ormcache('name', cache='stable')` 907-908.

### 4.5 State machine
- `_state_update(newstate, states_to_update, level=100)` ir_module.py:378-405: level < 1 -> UserError "Recursion error in modules dependencies!" 379-380; modules not in `states_to_update` skipped 382-384; dependency 'unknown' -> UserError 389-393; dependency already at newstate goes to `ready_mods` (unused afterwards) else recursed 394-400; module itself checked with `check_external_dependencies` 404 then written 405.
- `check_external_dependencies(module_name, newstate='to install')` 351-376: returns when module not available; `manifest.check_manifest_dependencies()`; `MissingDependency` -> UserError texts differ for 'to install', 'to upgrade' and other states, with apt hint 365-374.
- `button_install` 407-474: auto_domain 411; `install_states` 417; `must_install` 418-422 (`states = {dep.state for dep in dependencies_id if dep.auto_install_required}`; `states <= install_states and 'to install' in states and (not module.country_ids or module.country_ids & company_countries)`); loop 424-434 (`skip_auto_install` -> `modules = None` 431-432); exclusion check 439-448 ("Modules ... are incompatible"); exclusive-category closure check 451-472; returns `dict(ACTION_DICT, name=_('Install'))` 474.
- `button_immediate_install` 476-493: logs 'User #%d triggered module installation' 484; sets `request.allowed_company_ids` 491-492 (comment 485-490 on chart-of-accounts allowed companies); calls `_button_immediate_function(registry[...].button_install)` 493.
- `button_reset_state` 495+ (to install -> uninstalled; to upgrade/to remove -> installed). `check_module_update` 503-505.
- `button_upgrade` 703-750 (see claim C07 and details: base selected -> all installed except 'studio_customization' by name string 716-720; dependents appended 729-735; 'to upgrade' write 737; unknown dependency error 744-745; uninstalled dependencies scheduled with `button_install` 746-749; action 'Apply Schedule Upgrade' 750). `button_immediate_upgrade` 695-701.
- `button_uninstall` 669-681: server_wide_modules refused 671-673; wrong states refused 674-678; `(self + downstream_dependencies()).write({'state': 'to remove'})` 679-680; action 'Uninstall' 681. `button_uninstall_wizard` 683-693 (act_window to `base.module.uninstall`). `button_immediate_uninstall` 660-667.
- Closures: `downstream_dependencies(known_deps=None, exclude_states=('uninstalled','uninstallable','to remove'))` 532-555 (recursive SQL 542-554); `upstream_dependencies(..., exclude_states=('installed','uninstallable','to remove'))` 557-580. `next` 582-597 (open `ir.actions.todo` else act_url '/odoo').
- `module_uninstall` 507-517: `_module_data_uninstall(modules_to_remove)` 514; write state 'uninstalled', latest_version False 516. `_remove_copied_views` 519-530 (domain `key =like name + '.%'` 528; context active_test False + MODULE_UNINSTALL_FLAG 529).

### 4.6 Immediate runner and registry reload (ir_module.py:599-658)
Refuses when registry not ready or `_init` 600-601; refuses during tests (`modules.module.current_test`) 603-609; `SET LOCAL lock_timeout = '3s'` 611; pending-operation UserError 614-616; `LOCK ir_module_module IN EXCLUSIVE MODE` 619 (OperationalError -> rollback + UserError 620-623); `SELECT FROM ir_cron FOR UPDATE` 629 (comment 626-628; failure -> rollback + UserError about scheduled action 630-634); `function(self)` 635; commit 637; `Registry.new(dbname, update_module=True)` 638; commit 639; request registry reset 640-643; `cr.reset()` 644; `next()` 648; reload action with first root menu 652-658.

Registry reload triggers (OBSERVED): `_button_immediate_function` ir_module.py:638; wizard `base_module_upgrade.py:66`; `force_demo` loading.py:109-112; `load_modules` STEP 5 recursion loading.py:553-555; `check_signaling` registry sequence mismatch registry.py:1112-1115. `IrModel.unlink` and `IrModelFields.unlink` reload only when not MODULE_UNINSTALL_FLAG (ir_model.py:384-389, 1017-1023). After an update build `registry_invalidated = bool(update_module)` (registry.py:219) and `signal_changes()` (220) inserts into `orm_signaling_registry` (1143-1151) so other workers reload.

### 4.7 Wizards
`base_module_uninstall.py` (`_name` 8; `module_ids` 12-16; `_get_modules` 22-24; `action_uninstall` 63-65 -> `button_immediate_uninstall`); `base_module_upgrade.py` (`get_module_list` 12-15; `upgrade_module_cancel` 40-46; `upgrade_module` 48-69, SQL recheck 52-62, commit 65, `Registry.new(update_module=True)` 66, `cr.reset()` 67; `config` 71-73); `base_module_update.py` (`update_module` 14-18 -> `update_list`); `ir_demo.py` (`install_demo` 11-19 -> `force_demo` line 14). No `button_install_cancel`, `button_upgrade_cancel` or `install_from_urls` in ir_module.py.

### 4.8 Account addon extension of the module model
`account/models/ir_module.py` extends ir.module.module (`_inherit` 24-25; `account_templates` 27; `write` 62-84 sets `registry._auto_install_template = try_loading` 83; `_register_hook` 97-104; `module_uninstall` 106-115 sets `companies.chart_template = False` 112 then calls super 115).
## 5. ir.model.data (`base/models/ir_model.py`, class 2226)

### 5.1 Fields and constraints
Docstring 2227-2236; `_name` 2237; `_order = 'module, model, name'` 2239. Fields: name 'External Identifier' required 2242-2244; complete_name computed 2245 (`_compute_complete_name` 2256-2259 joins module and name with a dot); model 'Model Name' required 2246; module default '' required 2247; res_id Many2oneReference 2248; noupdate 'Non Updatable' default False 2249; reference computed unstored 2250 (`_compute_reference` 2261-2264). Constraints: `_name_nospaces` CHECK 2252; `_module_name_uniq_index = models.UniqueIndex('(module, name)')` 2253; `_model_res_id_index = models.Index('(model, res_id)')` 2254. `_compute_display_name` 2266-2277. There are NO `date_init`/`date_update` fields; create_date/write_date exist as ORM log-access columns (also base_data.sql:82-83).

### 5.2 Lookup and cache path
- `_xmlid_lookup` (`@api.model` 2280, `@tools.ormcache('xmlid')` 2281, def 2282): split at first '.' 2286; SELECT model,res_id 2287-2288; ValueError "External ID not found in the system" when no row or falsy res_id 2290-2291.
- `_xmlid_to_res_model_res_id` 2295-2302 (returns (False, False) unless raise requested); `_xmlid_to_res_id` 2305-2307; `check_object_reference` 2310-2319 (docstring 2311-2312 says ValueError, code raises AccessError 2317-2318, otherwise returns (model, False)).
- `env.ref` (`odoo/orm/environments.py:158`): `_xmlid_to_res_model_res_id` 166-168, `exists()` 170-173, ValueError "No record found for unique ID %s. It may have been deleted." 175.
- Cache hygiene: `write` clears cache 2336; `unlink` clears 2344; `create` clears only the 'groups' cache for res.groups 2331-2332; `_update_xmlids` primes the cache 2404.
- `_lookup_xmlids(xml_ids, model)` 2349-2374: groups by prefix, SELECT d.id, d.module, d.name, d.model, d.res_id, d.noupdate, r.id with LEFT JOIN on the target table 2365-2369, batched with `split_every(cr.IN_MAX, ...)` 2370.
- Behaviour when the referenced record no longer exists: the lookup returns the stale row (the cached lookup does not test the target); `env.ref` then fails `exists()`; the loader (`_load_records`) deletes the stale ir.model.data row and recreates the record (models.py:5180-5182); `_process_end` deletes the stale row (ir_model.py:2711-2712).

### 5.3 Create/update of xmlids (`_update_xmlids`, 2376-2421; query builder 2434-2451)
Rows `(prefix, suffix, record._name, record.id, noupdate)` 2389-2392; batches 2394; INSERT 2440; `ON CONFLICT (module, name)` 2442; `DO UPDATE SET (model, res_id, write_date)` 2443-2444; `WHERE (res_id != EXCLUDED.res_id OR model != EXCLUDED.model) {and_where}` 2445 with `AND NOT ir_model_data.noupdate` when `update` is true 2450; `RETURNING` 2446. noupdate is written only on INSERT, never changed on conflict. Cache priming 2404; `cache_invalidated.add('default')` when create_date != write_date 2405-2411; failure log 2414; `loaded_xmlids.update` 2418; res.groups cache 2420-2421. `_build_insert_xmlids_values` 2425-2432 (comment: overridden in web_studio, name only). `_load_xmlid` 2454-2461 (marks loaded and returns record).

### 5.4 `_load_records` decision (`odoo/orm/models.py`)
`_load_records_write` 5098-5113; `_load_records_create` 5115-5119; `_load_records(data_list, update=False)` 5121 (docstring 5122-5129; `imd = env['ir.model.data'].sudo()` 5132).

| Situation | init mode (update False) | update mode (update True) | Pointer |
|---|---|---|---|
| no xml_id, `vals` has id | write | write | 5155-5157 |
| no xml_id, no id | create | ValidationError "Cannot update a record without specifying its id or xml_id" | 5158-5161 |
| xml_id with no ir.model.data row | create | create | 5163-5166 |
| row model differs | ValidationError | ValidationError | 5168-5173 |
| row + target exists, noupdate flag false | write | write | 5175-5179 |
| row + target exists, stored noupdate true | write (flag ignored) | skip write, row still passed to `_update_xmlids` | 5178-5179 |
| row exists, target missing | delete stale row, create | delete stale row, create | 5180-5182 |

Also: foreign-prefix warning "Creating record %s in module %s." 5188-5194 (suppressed by context `foreign_record_to_create`); `import_file` guard 5196-5205 (for creations with xml_id and no noupdate flag whose prefix is an existing module name -> UserError recommending `__import__`); `_inherits` parent xmlids `f"{xml_id}_{parent_model.replace('.', '_')}"` carrying the noupdate flag 5212-5220; `imd._update_xmlids(imd_data_list, update)` 5224; returns records in input order 5226. `BaseModel.load` def 895 (mode default 'init' 914, current_module default '__import__' 915, noupdate 916, data dict 962, `_load_records(data_list, mode == 'update')` 972).

### 5.5 Cleanup for xmlids not refreshed (`_process_end`, 2641-2719)
Docstring 2643-2649; early return when no modules or `import_partial` 2650-2651; context MODULE_UNINSTALL_FLAG 2654; query `SELECT id, module || '.' || name, model, res_id FROM ir_model_data WHERE module IN %s AND res_id IS NOT NULL AND COALESCE(noupdate, false) != %s ORDER BY id DESC` with True 2657-2660; skip loaded xmlids 2662-2663; unknown model skip 2665-2667; `_inherits` child protection 2669-2693; other-xmlid-only handling 2695-2703; log 'Deleting %s@%s (%s)' 2705; record unlink with `module` context via `_process_end_unlink_record` 2706-2710 (2637-2639); missing record -> bad id 2711-2712; unlink bad ids 2713-2714; `_create_all_specific_views(modules)` 2717; `loaded_xmlids.clear()` 2719. `toggle_noupdate` 2721-2726 (check_access('write') 2724; flips all xmlids of the record 2725-2726). Net rule: records whose xmlid is flagged noupdate are never removed by this cleanup, even when a newer version no longer ships them.

### 5.6 Reflection xmlids
`_reflect_models` 446-483 (xmlid only when `model._module == module` 478-480; `_update_xmlids` 483); fields 1270-1272; selections 1610-1612; constraints `'%s.constraint_%s'` 2005 and 2009-2011. Helpers `model_xmlid` 63-65, `field_xmlid` 68-70, `selection_xmlid` 73-77. `MODULE_UNINSTALL_FLAG = '_force_unlink'` 36.

### 5.7 `__export__` and `__import__`
`__ensure_xml_id` (`odoo/orm/models.py:599-676`): `modname = '__export__'` 617; existing SELECT 619-628; new names `'%s_%s_%s' % (r._table, r.id, uuid.uuid4().hex[:8])` 641-648; `cr.copy_from(table='ir_model_data', columns=['module','model','name','res_id'])` 649-670; invalidate 671; returns pairs 673-676. noupdate is not set (column default applies). `__import__` appears as default `current_module` in `load` (915) and in the import_file guard (5204). A rename helper for xmlids is ABSENT within grep scope (`odoo/orm`, `odoo/modules`, `odoo/tools`, `odoo/addons/base/models`): only `rename_column` for DB columns at `odoo/tools/sql.py:377` and the category-rename comment db.py:141.

## 6. Converter (`odoo/tools/convert.py`, 795 lines)

- `ConvertMode = Literal['init','update']` 36; `_get_eval_context` 43-56; `_eval_xml` 76; `nodeattr2bool` 211-217; `xml_import` 219; `__init__(env, module, idref, mode, noupdate=False, xml_filename='')` 645-652; `_tags` 653-662 (record, delete, function, menuitem, template, asset and every `DATA_ROOTS`); `DATA_ROOTS = ['odoo','data','openerp']` 667; `parse` 664-666.
- Tags: `_tag_delete` 251-270 (no noupdate gating; failed search or missing id -> warning); `_tag_function` 272-276 (returns when `self.noupdate and self.mode != 'init'` 273-274); `_tag_menuitem` 278-337 (`'noupdate': self.noupdate` 333, `_load_records([data], self.mode == 'update')` 335); `_tag_record` 339-470; `_tag_template` 472-546; `_tag_asset` 548-586; `_tag_root` 598-629 (`self._noupdate.append(nodeattr2bool(el, 'noupdate', self.noupdate))` 605; ParseError wrapping 607-625).
- `_tag_record` rules: gate `if self.noupdate and self.mode != 'init':` 360 (comment 357-359 notes a second check in `_load_records` using the stored flag); no id -> return 362-363; existing xmlid -> idref filled for it and nested `.//record[@id]` 365-376; `elif not forcecreate (default True)` -> return 377-379; foreign-prefix branch 382-390 (forcecreate default False there 386; under noupdate and explicit forcecreate false returns 387-389; else raises "Cannot update missing record" 390); ref resolution 421-429 (unresolved ref raises when forcecreate true, default; with forcecreate false warns "Skipping creation of ..." and returns None); data dict `dict(xml_id=xid, values=res, noupdate=self.noupdate)` 460; `_load_records([data], self.mode == 'update')` 463; sub-records 468-469.
- Schema: `odoo/import_xml.rng` record define 143-157 (attributes id, forcecreate, model; no noupdate); template 159+ with forcecreate 164; root `odoo_openerp_data` 268-291 with optional `noupdate` 275 and `auto_sequence` 276 on odoo/openerp/data only. noupdate granularity is therefore the container element only.
- `convert_file(env, module, filename, idref, mode='update', noupdate=False, kind=None, pathname=None)` 670-700: `kind` deprecated 680-685; extension lower-cased 688; `.csv` 691-692, `.sql` 693-694, `.xml` 695-696, `.js` ignored 697-698, else ValueError 699-700.
- `convert_csv_import` 707-762: default mode 'init' 713; model from file stem before first '-' 721-722; guard `if not (mode == 'init' or 'id' in fields)` logs "Import specification does not contain 'id' and we are in init mode, Cannot continue." and returns 726-728 (message says init mode while the guard fires in update mode); '@' translation columns stripped 730-736; empty lines dropped 740-743; context mode/module/install_mode/install_module/install_filename/noupdate 745-752; `.load(fields, datas)` 753; errors -> Exception "Module loading %(module)s failed: file %(file)s could not be processed" 754-762. `convert_xml_import` 765-795 (RelaxNG 775-788).

## 7. Load orchestration (`odoo/modules/loading.py`, 633 lines)

### 7.1 Data vs demo
`load_data` 41-61 (docstring 42-46; `keys = ('init_xml','data') if kind == 'data' else ('demo',)` 47; init_xml deprecation 51-52; duplicate-file warning 54-55; `convert_file(..., noupdate=kind == 'demo')` 59). `load_demo` 64-86 (condition `manifest.get('demo') or manifest.get('demo_xml')` 70; savepoint 72; superuser context `install_demo=True` 73; `return True` 74 also when no demo files; failure warning 77-79, `base.demo_failure_todo` + `ir.demo_failure` 81-85, False 86). `force_demo` 89-112. `demo_installable` (module_graph.py:201-203) = all dependencies have demo true; base demo uses `new_db_demo` (loading.py:411). So the demo flag is true for any module whose demo loading did not fail, including modules without demo files.

### 7.2 Per-module phases (`load_module_graph` def 115; docstring 123-130)
`MigrationManager(env.cr, graph)` 137; loop 148; skip modules in `_init_modules` 152-153; `update_operation` 159-164 ('install' if state 'to install', 'upgrade' if 'to upgrade', 'reinit' if in `_reinit_modules`; None otherwise). Order:
1. pre-migrate (`migrate_module(package,'pre')`) for upgrade or forced scripts 170-174 (incremental `_setup_models__` unless base);
2. `env.flush_all()` 175-176;
3. `load_openerp_module` 178 (post_load, no args);
4. install only: `pre_init_hook` 181-185, called with `env`;
5. `registry.load(package)` 187; `init_models(..., update_operation == 'install')` 189-194; model checks 195-206; `module._check()` 211-212;
6. data: install -> `load_data(env, idref, 'init', kind='data')` 217 then demo 218-219; upgrade/reinit -> `module.write(get_values_from_terp(manifest))` 222, `mode = 'update' if upgrade else 'init'` 223, `load_data` 224, demo if `package.demo` 225-226; `UPDATE ir_module_module SET demo` 227-228;
7. post-migrate 230; translations 232-234; `_init_modules.add` 236-237;
8. install only: `post_init_hook` 241-243 called with `env`;
9. upgrade: `_validate_module_views` 244-246; no-access-rule warning 248-263; `updated_modules.append` 265; `module.write({'state':'installed','latest_version':ver})` 267-269; flush + commit 271-273; tests 275-293.
Consequence: install and reinit use mode 'init' (noupdate protection not applied by `_tag_record`; stored-flag skip not applied by `_load_records`), upgrade uses 'update' (both checks apply).

### 7.3 Whole-system steps (`load_modules` def 340; docstring 350-359)
`initialize_sys_path` 363; `SET SESSION lock_timeout = '15s'` 370; uninitialised DB: error "Database %s not initialized, you can force it with `-i base`" 373 or `modules_db.initialize` 376; base reinit/upgrade 377-381; STEP 1 base graph 383-412; STEP 2 module list refresh 423-448 (`update_list` 427; `_check_module_names` 429, 326-337; `button_install` 431-434; `button_upgrade` 436-439; reinit with downstream dependencies 441-444); STEP 3 loop 450-468 (states include 'to install' only when update_module 453-456; breaks when `updated_modules` unchanged 467-468); `registry.loaded = True` 487; STEP 3.5 end-migrate 497-501; STEP 3.6 `finalize_constraints` 509-510; STEP 4 512-530 (`_check_removed_columns` 518; `_process_end(registry.updated_modules)` 523; autovacuum cron trigger 524-528); STEP 5 uninstall 532-556 ('to remove' select 536-537; reversed packages 539; `uninstall_hook` 541 called as `getattr(py_module, uninstall_hook)(env)` 544 then flush 545; `module_uninstall()` 548; commit 551; recursive `Registry.new` 553-555); STEP 5.5 558-572; STEP 6 `_validate_custom_views` 574-581; STEP 9 `_register_hook` 588-595; STEP 10 `check_null_constraints` 597-598; `base.partially_updated_database` 600-608. Failure: `reset_modules_state` 611-632 (to remove/to upgrade -> installed, to install -> uninstalled, warning 632) invoked from `Registry.new` on exception (registry.py:198-200).
- Graph ordering (`module_graph.py`): `ModuleNode` 137-203 (`order_name` 165-172, `depth` 174-181, `phase` 183-199); `ModuleGraph` 206-317 sorts by (phase, depth, name).
- Registry: `Registry.new` 115-127 (docstring 128-149); `init` 152; `setup_signaling` 163; `partially_updated_database` check 174-176; `update_module = True` when install/upgrade/reinit lists 182-183; `load_modules` 189-197; `_init = False` 215; `ready = True` 217; `signal_changes` 220; `load` 375-405; `init_models` 750-804; `finalize_constraints` 738-748.
- Migration runner (U102 owns patterns): `migration.py` `VERSION_RE` 31-55; `MigrationManager` 58-215 (`0.0.0` first in pre and last in post/end); `migrate_module` def 149 (early return unless `load_state == 'to upgrade'` or forced 151-152); `compare` 196-209 (installed < script <= manifest); `exec_script` 223-253.

## 8. Hooks

| Hook | Manifest key | Signature | When | Pointer |
|---|---|---|---|---|
| post_load | `post_load` | `fn()` no args | on first import of the package in the process, before models/data, server-wide | module.py:492-516 |
| pre_init_hook | `pre_init_hook` | `fn(env)` | install only, after pre-migrate and before models are loaded | loading.py:181-185 |
| post_init_hook | `post_init_hook` | `fn(env)` | install only, after data, post-migrate and translations | loading.py:241-243 |
| uninstall_hook | `uninstall_hook` | `fn(env)` | STEP 5 before `module_uninstall()` data removal, then flush | loading.py:541-548 |

Prevalence: post_load 0, pre_init_hook 6, post_init_hook 94, uninstall_hook 62 of 692 (scripted scan). `base/__manifest__.py:96` `'post_init_hook': 'post_init'`; `base/__init__.py:9-11` `post_init(env)` calls `env['ir.config_parameter'].init(force=True)`. `load_openerp_module` details: def 492, docstring 493-499, `qualname` 501, early return when already in `sys.modules` 502-503, import 506, comment 508-510, `manifest` 511, `getattr(sys.modules[qualname], post_load)()` 512-513, `except AttributeError` 515 logs "Couldn't load module %s" 516, then circular-import hint analysis 517-523+ (remainder not read).

## 9. Uninstall (`_module_data_uninstall`, ir_model.py:2464-2635)

Docstring 2465-2473; `is_system()` AccessError 2476-2477; context MODULE_UNINSTALL_FLAG + `prefetch_fields=False` 2481; `module_data = self.search([('module','in',modules_to_remove)], order='id DESC')` 2490 (no noupdate filter); classification into model_ids, field_ids, selection_ids, constraint_ids, records_items 2491-2501; `delete(records)` helper 2534-2580 (skips records that have xmlids of other modules 2537-2543; orphan ir.model.fields xmlids 2547-2559; keeps `id` and LOG_ACCESS columns of logged models 2560-2565; savepoint + unlink 2567-2572; failure -> single record added to undeletable, otherwise recursive halving 2573-2580); ordinary records grouped by model first 2582-2589; copied views via `modules._remove_copied_views()` 2591-2597; constraints 2600; selections 2606 (comment 2602-2605); fields 2607; relations then `relations._module_data_uninstall()` 2608-2609; models 2612; log 2615; undeletable re-examination 2617-2633; `module_data.unlink()` 2635. Ordering: data -> copied views -> constraints -> selections -> fields -> relations -> models -> xmlid rows.
- Drop rules: `IrModel._drop_table` 333-353 (abstract skipped 337-338; DROP VIEW 343; DROP TABLE CASCADE 345; warning 346-350); `IrModel.unlink` 362-391; `IrModelFields._drop_column` 864-897 (MAGIC_COLUMNS skipped 870-871; `ALTER TABLE ... DROP COLUMN ... CASCADE` 878-880; manual m2m tables 881-895); `_prepare_update` 899-908 ("This column contains module data and cannot be removed!" 908 unless flag 906-907); `IrModelFields.unlink` 988-1025; `IrModelFieldsSelection._unlink_if_manual` 1732-1741, `unlink` 1743-1755; `IrModelConstraint` 1858-1936 (unique (name, module) 1878-1879); `IrModelRelation._module_data_uninstall` 2030-2057 (skip when another module owns 2042-2047; DROP TABLE CASCADE 2056).
- Restrictions: server-wide modules cannot be uninstalled (ir_module.py:671-673); only 'installed'/'to upgrade' modules (674-678); downstream dependencies are scheduled with them (679-680); module record itself deletion blocked while installed (337-341).
- noupdate interplay: uninstall removes records regardless of the noupdate flag (2490); the flag only protects records during upgrade cleanup (`_process_end` 2657-2660).

## 10. Migration-relevant xmlid facts and why noupdate matters

1. What happens to xmlids of records a newer version no longer ships: for non-noupdate xmlids of an updated module, `_process_end` deletes the target record (or only the xmlid row when the record has another xmlid, or when the record is gone) unless the xmlid was reloaded in this run (ir_model.py:2655-2712). Noupdate xmlids are skipped by the query (2657-2660) and survive as orphaned data. `_process_end` runs only when `registry.updated_modules` is non-empty (loading.py:513, 523).
2. Why noupdate matters for customer-modified records (OBSERVED mechanism):
   - Views: noupdate-flagged views are validated separately after upgrade (`ir_ui_view.py:2568-2593`, comment 2586-2587 "retrieve the views with an XML id that has not been checked yet, i.e., the views with noupdate=True on their xml id"); the view write override updates copy-on-write specific views only for unmodified fields, "mimic the noupdate behavior on views having an ir.model.data" (2612-2617; inherit_id special case 2626-2631); `_load_records_write_on_cow` 2634-2643.
   - Record rules and other security data: `base/security/base_security.xml:3` `<data noupdate="1">` wraps ir.rule records (e.g. `res_partner_rule` 12); `account/security/account_security.xml:3` `<data noupdate="0">` and `:109` `<data noupdate="1">` (rules 111-126).
   - Mail templates: `account/data/mail_template_data.xml:4-6` comment "Mail template are declared in a NOUPDATE block so users can freely customize/delete them", `<data noupdate="1">` at 6.
   - Chart-template records: all written with `noupdate: True` (account/models/chart_template.py:692-697).
3. Two independent noupdate checks exist: the converter gate (convert.py:360) and the stored-flag test in `_load_records` (models.py:5178-5179).
4. noupdate is stored only at first insert (ir_model.py:2442-2445, 2450); changing the container attribute later does not change existing rows; `toggle_noupdate` (2721-2726) is the explicit way.
5. `ir.ui.view` helpers: `_validate_module_views` decorator 2568, def 2569, docstring 2570-2572, `assert self.pool._init` 2573, names from `pool.loaded_xmlids` 2575-2582, SELECT with `AND md.noupdate` 2588-2593, `_check_xml()` 2595; `_create_all_specific_views` base `pass` 2597-2599; `_get_specific_views` 2601-2610.
6. xmlid rename helper ABSENT (see 5.7). `__export__`/`__import__` PRESENT (see 5.7).

## 11. Thai relevance

### 11.1 `l10n_th/__manifest__.py` (30 lines, read in full)
Line 1 license comment; `{` 2; name 'Thailand - Accounting' 3; icon `/account/static/description/l10n.png` 4; `'countries': ['th']` 5; `'version': '2.0'` 6; category 'Accounting/Localizations/Account Charts' 7; description 8-13; author 'Almacom (http://almacom.co.th/)' 14; website 15; depends `['account_qr_code_emv','account']` 16-19; `'auto_install': ['account']` 20; data `['data/account_tax_report_data.xml','views/report_invoice.xml']` 21-24; demo `['demo/demo_company.xml']` 25-27; `'post_init_hook': '_preserve_tag_on_taxes'` 28; license 'LGPL-3' 29; `}` 30.
- `l10n_th/__init__.py` (7 lines): `from . import models` 2; `def _preserve_tag_on_taxes(env):` 4; local import of `preserve_existing_tags_on_taxes` from `odoo.addons.account.models.chart_template` 5; call `preserve_existing_tags_on_taxes(env, 'l10n_th')` 6.
- `account/models/chart_template.py:46-50`: `preserve_existing_tags_on_taxes` (docstring 47; `update ir_model_data set noupdate = 't' where id in %s` at 50). This is the only Thai hook touching xmlids.
- ABSENT hooks: pre_init_hook, uninstall_hook, post_load keys are not in the manifest. Directory proof: `l10n_th` = `__init__.py __manifest__.py data demo i18n models tests views`; `l10n_th/data` = `account_tax_report_data.xml template`; `l10n_th/data/template` = `account.account-th.csv account.asset-th.csv account.tax-th.csv account.tax.group-th.csv`. No hook module or file other than `__init__.py` exists.
- `l10n_th/models/template_th.py`: `@template('th')` 9, `def _get_th_template_data` 10; `@template('th', 'res.company')` 19, `def _get_th_res_company` 20 (`'account_fiscal_country_id': 'base.th'` 23; `'tax_exigibility': 'True'` 41). `data/account_tax_report_data.xml` root `<odoo auto_sequence="1">`.
- RT inference: with `auto_install: ['account']` only `account` has `auto_install_required` true (`account_qr_code_emv` does not); together with `countries: ['th']`, `button_install.must_install` needs a company whose country is Thailand; the fresh-DB bootstrap SQL (db.py:95-107) does not evaluate countries.

### 11.2 `account` chart-template loading (pointer level)
`get_python_translation` 39; `template` decorator 53-70; `_get_chart_template_mapping` 98; `try_loading` 140-171; `_load` 173-255 (admin AccessError 183-184; `button_immediate_install()` for an uninstalled chart module 191-193; `_pre_reload_data` 234; `_pre_load_data` 236; `_load_data` 237; `_post_load_data` 238; `_load_translations` 239; demo 245-253); `_pre_reload_data` def 265 (xmlid re-pointing through `_update_xmlids` with `'noupdate': True` 302-306, 439-443; `skip_update` 451-455; obsolete tax xmlids unlinked 457-461); `_load_data` def 562 (docstring 563-572); body 670-698: `created_records = {}` 673; loop 674; `all_records_vals = []` 675; per xml_id 676; strip '@' and `__translation_module__` keys 678-680; comment 682; `self.ref(xml_id, raise_if_not_found=False)` -> id 683-684; int ids -> `record_vals['id']` and no xml_id 686-688; else `self.company_xmlid(xml_id)` 689-690; record dict with `'noupdate': True` 692-696 (695); `_load_records(all_records_vals)` in `en_US` context 697 (update default False); return 698. `_post_load_data` 700; `_get_chart_template_data` 821; `company_xmlid` 1226-1230 (`f"account.{company.id}_{xmlid}"`); `ref` 1232-1236; `_get_parent_template` 1238; `_parse_csv` 1305 (opens `{module}/data/template/{model}{-template}.csv` through `file_open` at 1330, not through the converter).
- Result: Thai chart records live under the `account` module prefix with company id, always noupdate, loaded with update False; the manifest `data` list carries only the tax report and an invoice report view.

## 12. Migration flags

### 12.1 OBSERVED in v19 source
| # | Flag | Evidence |
|---|---|---|
| F01 | ir.model.data has no `date_init`/`date_update` fields; only ORM log columns | ir_model.py:2242-2264, 2446; base_data.sql:79-91 |
| F02 | noupdate written only on INSERT of an xmlid row; conflict never changes it | ir_model.py:2442-2445, 2450 |
| F03 | Two independent noupdate checks (converter gate and stored flag) | convert.py:360; models.py:5178-5179 |
| F04 | noupdate is container-only; record accepts id/forcecreate/model only | import_xml.rng:143-157, 268-276; convert.py:605 |
| F05 | forcecreate only matters inside noupdate+update gate, foreign branch and unresolved refs | convert.py:377-379, 386-390, 426-429 |
| F06 | Constraints declared with `models.Constraint`/`UniqueIndex`/`Index` | ir_model.py:1878, 2252-2254; ir_module.py:328-331 |
| F07 | Version-field naming inversion on ir.module.module | ir_module.py:285-290; module_graph.py:155 |
| F08 | "Since 19.0" deprecations: `load_manifest`, `get_modules_with_version`, `convert_file` kind, `init_xml` key, `Registry.manage_changes` | module.py:399-401, 544-547; convert.py:680-685; loading.py:51-52; registry.py:1182-1190 |
| F09 | Fields/keys present: `country_ids`, `has_iap`, `icon_flag`, `to_buy`, dependency `auto_install_required`, category `privilege_ids`; manifest keys `countries`, `external_dependencies`, `post_load`, `bootstrap`, `cloc_exclude`, `kpi_providers`, `demo_xml`, `init_xml`, `update_xml`, `test` | ir_module.py:297, 324-326, 1017-1020, 86; module.py:56-96 |
| F10 | Bootstrap SQL ignores the countries condition used by `button_install` | db.py:95-107 vs ir_module.py:418-422 |
| F11 | `_remove_copied_views` is called inside `_module_data_uninstall` | ir_model.py:2596-2597; ir_module.py:519 |
| F12 | Chart-template xmlids written with noupdate True in `account.<company_id>_<xmlid>` form; l10n_th templates read by `_parse_csv`, not manifest data | chart_template.py:692-697, 1226-1230, 1305-1330 |
| F13 | xmlid rename helper ABSENT in grep scope; `__export__`/`__import__` present | sql.py:377; db.py:141; models.py:617, 915, 5204 |
| F14 | No `button_install_cancel`/`button_upgrade_cancel`/`install_from_urls` in ir_module.py | ir_module.py (whole file); wizard base_module_upgrade.py:40 |
| F15 | `check_object_reference` docstring says ValueError, code raises AccessError | ir_model.py:2311-2312, 2317-2318 |
| F16 | `button_upgrade` references the name string 'studio_customization'; no Enterprise file opened | ir_module.py:718, 733 |
| F17 | CSV guard message says init mode but fires in update mode | convert.py:726-727 |
| F18 | ORM `ir.module.module` has no `web` field but bootstrap column and `_DEFAULT_MANIFEST` key exist | base_data.sql:63; db.py:59, 65; module.py:94 |
| F19 | Hook prevalence: post_load 0, pre_init_hook 6, post_init_hook 94, uninstall_hook 62, excludes 0, init_xml 0 of 692 | scripted manifest scan |
| F20 | `load_demo` returns True also without demo files; `demo_installable` needs all dependencies demo | loading.py:70-74; module_graph.py:201-203 |
| F21 | Manifest handling moved to a `Manifest` class; `all_addon_manifests` sorted by name | module.py:176-186, 317-331 |
| F22 | Module-loading code split between `odoo/modules/` and `odoo/orm/registry.py` | loading.py; registry.py:115-220 |

### 12.2 PRIOR-VERSION-KNOWLEDGE (not verified in this tree)
- ir.model.data in earlier releases carried `date_init` and `date_update`; the release that removed them is not determinable from this tree (UNKNOWN — EVIDENCE INSUFFICIENT).
- Earlier releases defined constraints through `_sql_constraints` lists and `_auto_init` index creation; v19 uses the declarative objects (see F06).
- Earlier releases kept more of the loading logic inside `odoo/modules/loading.py` and `registry.py` under the `odoo/modules/registry` path; v19 re-exports from `odoo/orm/registry.py` (see F22).
- Earlier releases had `button_install_cancel`, `button_upgrade_cancel` and `install_from_urls` on ir.module.module (not verified here); see F14 for what v19 contains.

## 13. RT and UNKNOWN items

- RT: whether an empty-list auto_install manifest would be installed during fresh DB bootstrap (db.py SQL) but not by `button_install`; needs execution; zero Community manifests affected.
- RT: effective behaviour of the exclusive-category closure check with real module sets (ir_module.py:451-472).
- RT: demo-flag outcome when a demo file fails (loading.py:77-86) and the todo record content.
- RT: lock behaviour of `_button_immediate_function` under concurrent workers.
- UNKNOWN — EVIDENCE INSUFFICIENT: remainder of `load_openerp_module` after line 523; release in which ir.model.data date columns were dropped; whether any Extra or Enterprise module overrides `_build_insert_xmlids_values` (a comment at ir_model.py:2423-2424 names web_studio only).

## 14. Files read

`odoo/modules/loading.py`, `odoo/modules/module.py`, `odoo/modules/db.py`, `odoo/modules/module_graph.py`, `odoo/modules/migration.py`, `odoo/modules/registry/__init__.py`, `odoo/orm/registry.py`, `odoo/orm/models.py`, `odoo/orm/fields_relational.py`, `odoo/orm/environments.py`, `odoo/tools/convert.py`, `odoo/import_xml.rng`, `odoo/tools/sql.py` (rename_column pointer), `odoo/addons/base/models/ir_module.py`, `ir_model.py`, `ir_ui_view.py`, `base/wizard/base_module_uninstall.py`, `base_module_upgrade.py`, `base_module_update.py`, `ir_demo.py`, `base/data/base_data.sql`, `base/data/ir_cron_data.xml`, `base/__manifest__.py`, `base/__init__.py`, `base/security/base_security.xml`, `account/__manifest__ data` pointers (`account_security.xml`, `mail_template_data.xml`), `account/models/chart_template.py`, `account/models/ir_module.py`, `l10n_th/__manifest__.py`, `l10n_th/__init__.py`, `l10n_th/models/template_th.py`, `l10n_th/data/account_tax_report_data.xml`; all 692 Community `__manifest__.py` files via the scripted scan.

