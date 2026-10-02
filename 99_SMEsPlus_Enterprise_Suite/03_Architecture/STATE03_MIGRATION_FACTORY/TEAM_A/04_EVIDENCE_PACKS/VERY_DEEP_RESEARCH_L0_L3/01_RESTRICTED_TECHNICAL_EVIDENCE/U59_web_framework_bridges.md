# U59 — web framework Python controllers and bridge modules (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U59
- Modules: web (Python server side), web_hierarchy, web_tour, web_unsplash
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST for web (U21 breadth-only). JS/OWL static not studied. Focus on Python controllers, models, RPC endpoints. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U59-01 Home controller and web client bootstrap

### D1 — Entry route and session guard
The `Home` controller at `web/controllers/home.py:34` defines the root (`/`) route which checks session uid and internal-user status before redirecting either to `/web/login_successful` or to `/odoo`. The `/web`, `/odoo`, and `/scoped_app` multi-pattern route at line 46 enforces `ensure_db()`, checks `security.check_session`, raises `SessionExpiredException` if the session is invalid, and calls `request.update_env(user=request.session.uid)` to restore the ORM user context before rendering the webclient bootstrap QWeb template.

### D2 — Webclient rendering context
`IrHttp.webclient_rendering_context()` at `web/models/ir_http.py:71` returns a dict with `color_scheme` and `session_info`. The `web_client()` controller computes an HMAC `browser_cache_secret` from `_session_token_get_values()` and injects it into `session_info` before rendering `web.webclient_bootstrap`.

### D3 — Login flow
The `/web/login` route at `home.py:103` uses `auth='none'` and `readonly=False`. On POST it extracts `login`, `password`, `type` from `CREDENTIAL_PARAMS` (line 31), optionally calls `_should_captcha_login` and `_verify_request_recaptcha_token`, then calls `request.session.authenticate()`. On success it redirects via `_get_login_redirect_url`. The response sets `Cache-Control: no-cache` and `X-Frame-Options: SAMEORIGIN`.

### D4 — Health check
`/web/health` at `home.py:173` accepts optional `db_server_status` parameter. With the flag it opens a postgres cursor via `odoo.sql_db.db_connect('postgres').cursor().close()` and reports status pass/fail in JSON. The route uses `save_session=False`.

### D5 — Menu loading endpoint
`/web/webclient/load_menus` at `home.py:85` calls `request.env["ir.ui.menu"].load_web_menus(request.session.debug)` and returns `Cache-Control: no-store` JSON. `IrUiMenu.load_web_menus()` at `web/models/ir_ui_menu.py:12` builds a `web_menus` dict keyed by menu id, resolving the app action by walking down child menus until an `action_id` is found.

---

## CAP-U59-02 Session controller

### D1 — session_info endpoint
`/web/session/get_session_info` at `web/controllers/session.py:25` is `type='jsonrpc'`, `auth='user'`, `readonly=True`. It calls `request.session.touch()` and returns `request.env['ir.http'].session_info()`.

### D2 — authenticate endpoint
`/web/session/authenticate` at `session.py:31` accepts `db`, `login`, `password`. It filters the database through `http.db_filter`, creates a cursor if the db differs from the request db, calls `request.session.authenticate(env, credential)`, and returns `ir.http.session_info()` for the authenticated user. Returns `{'uid': None}` if uid changed during MFA flows.

### D3 — modules, destroy, logout
`/web/session/modules` at `session.py:64` returns `list(request.env.registry._init_modules)`. `/web/session/destroy` at line 84 calls `request.session.logout()`. `/web/session/logout` at line 88 is `auth='none'`, `readonly=True` and redirects to `/odoo`.

### D4 — session_info content
`IrHttp.session_info()` at `web/models/ir_http.py:84` returns fields including: `uid`, `is_system`, `is_admin`, `is_public`, `is_internal_user`, `user_context`, `db`, `registry_hash` (HMAC over `registry_sequence`), `user_settings` (from `res.users.settings._find_or_create_for_user`), `server_version`, `name`, `username`, `partner_id`, `web.base.url`, `active_ids_limit`, `max_file_upload_size`, `home_action_id`, `currencies`, `bundle_params`, `test_mode`, `view_info`, and `groups` dict with `base.group_allow_export` check. For internal users it additionally includes `user_companies` dict with `current_company`, `allowed_companies`, and `disallowed_ancestor_companies`.

---

## CAP-U59-03 Dataset / call_kw RPC endpoint

### D1 — call_kw route
`DataSet.call_kw()` at `web/controllers/dataset.py:29` serves `/web/dataset/call_kw` and `/web/dataset/call_kw/<path:path>` as `type='jsonrpc'`, `auth='user'`. The `readonly` callback `_call_kw_readonly` at line 15 introspects the model class MRO to find the method's `_readonly` attribute. It delegates to `odoo.service.model.call_kw(request.env[model], method, args, kwargs)`.

### D2 — call_button route
`DataSet.call_button()` at `dataset.py:34` serves `/web/dataset/call_button`. After `call_kw`, if the return is a non-empty dict action, it passes the result through `clean_action(action, env=request.env)`.

---

## CAP-U59-04 Binary / attachment serving

### D1 — /web/content routes
`Binary.content_common()` at `web/controllers/binary.py:72` serves `/web/content` with multiple URL patterns accepting `xmlid`, `model`, `id`, `field`. It calls `ir.binary._find_record()` and `ir.binary._get_stream_from()`. With `unique=True` it sets `immutable=True` and `max_age=http.STATIC_CACHE_LONG`. With `access_token` present it marks the stream as public.

### D2 — /web/image routes
`Binary.content_image()` at `binary.py:185` serves 18 URL patterns. It calls `ir.binary._get_image_stream_from()` with `width`, `height`, and `crop` parameters. On `UserError` with `download=False` it falls back to `web.image_placeholder`. The route uses `save_session=False`.

### D3 — Asset serving
`Binary.content_assets()` at `binary.py:93` serves `/web/assets/<unique>/<filename>`. When `unique == 'debug'` it enters debug mode. It searches `ir.attachment` for pre-built bundles, falling back to generating via `ir.qweb._get_asset_bundle()`. Immutable caching is set when unique is not `'debug'`.

### D4 — Company logo
`Binary.company_logo()` at `binary.py:263` serves `/web/binary/company_logo`, `/logo`, `/logo.png`. When no db is found it returns the static `web/static/img/logo.png`. With a db it executes a direct SQL query on `res_company` or joins through `res_users` to fetch `logo_web` and `write_date`.

### D5 — File upload
`Binary.upload_attachment()` at `binary.py:219` serves `/web/binary/upload_attachment` as `type='http'`, `auth='user'`. It creates `ir.attachment` records with `name`, `raw`, `res_model`, `res_id` from the uploaded file list, calls `_post_add_create()`, and returns JSON or JavaScript callback output.

### D6 — Sign fonts
`Binary.get_fonts()` at `binary.py:316` serves `/web/sign/get_fonts` as `type='jsonrpc'`, `auth='none'`. Returns base64-encoded font files from `web/static/fonts/sign` filtered to `.ttf`, `.otf`, `.woff`, `.woff2`.

---

## CAP-U59-05 Export controllers

### D1 — CSV export
`CSVExport.web_export_csv()` at `web/controllers/export.py:640` serves `/web/export/csv` as `type='http'`, `auth='user'`. Calls `ExportFormat.base()` which parses `model`, `fields`, `ids`, `domain`, `import_compat` from JSON params. With groupby it builds a `GroupsTreeNode` tree from `formatted_read_group` and `export_data`. Without groupby it batches through `split_every(PREFETCH_MAX, records.ids)`.

### D2 — XLSX export
`ExcelExport.web_export_xlsx()` at `export.py:688` serves `/web/export/xlsx`. `ExportXlsxWriter` at line 167 creates an xlsxwriter workbook with styles for `date_style`, `datetime_style`, `float_style`, `monetary_style`. `GroupExportXlsxWriter` at line 248 writes hierarchical group headers with aggregated values.

### D3 — Export formats
`Export.formats()` at `export.py:291` serves `/web/export/formats` as `type='jsonrpc'`, `readonly=True`. Returns `[{'tag': 'xlsx', ...}, {'tag': 'csv', ...}]` with an xlsx error if `xlsxwriter` is not installed.

### D4 — Export field enumeration
`Export.get_fields()` at `export.py:364` serves `/web/export/get_fields` as `type='jsonrpc'`, `auth='user'`, `readonly=True`. Calls `fields_get()` with attributes including `exportable`, `readonly`, `definition_record`. Filters out non-exportable and readonly fields in import_compat mode. Calls `_get_property_fields()` for dynamic property field expansion.

---

## CAP-U59-06 Report controller

### D1 — Report render routes
`ReportController.report_routes()` at `web/controllers/report.py:27` serves `/report/<converter>/<reportname>` and `/report/<converter>/<reportname>/<docids>`. Dispatches to `ir.actions.report._render_qweb_html`, `_render_qweb_pdf`, or `_render_qweb_text`. Route uses `website=True`, `readonly=True`.

### D2 — Report download
`ReportController.report_download()` at `report.py:92` serves `/report/download` as `type='http'`, `auth='user'`. Parses `data` JSON to extract URL and type. For `qweb-pdf` / `qweb-text` it extracts reportname and docids and calls `report_routes()`. Evaluates `print_report_name` via `safe_eval` for custom filename.

### D3 — Barcode
`ReportController.report_barcode()` at `report.py:55` serves `/report/barcode` and `/report/barcode/<barcode_type>/<path:value>` as `auth='public'`, `readonly=True`. Calls `ir.actions.report.barcode()` and returns `image/png` with immutable caching.

---

## CAP-U59-07 Web client translation and version

### D1 — Bootstrap translations
`WebClient.bootstrap_translations()` at `web/controllers/webclient.py:18` serves `/web/webclient/bootstrap_translations` as `type='jsonrpc'`, `auth='none'`. Reads locale PO files for `manifest.bootstrap` modules, returning only messages with `JAVASCRIPT_TRANSLATION_COMMENT`.

### D2 — Full translations
`WebClient.translations()` at `webclient.py:46` serves `/web/webclient/translations` as `type='http'`, `auth='public'`. Uses hash comparison against `ir.http._get_web_translations_hash()`. If hash differs, calls `_get_translations_for_webclient()`. Returns JSON with `Cache-Control: public, max-age=<STATIC_CACHE_LONG>`.

### D3 — Bundle definition
`WebClient.bundle()` at `webclient.py:100` serves `/web/bundle/<bundle_name>`. Calls `ir.qweb._get_asset_nodes()` and returns JSON list of `{type, src}` dicts.

### D4 — Version info
`WebClient.version_info()` at `webclient.py:88` serves `/web/webclient/version_info` as `type='jsonrpc'`, `auth='none'`. Returns `odoo.service.common.exp_version()`.

---

## CAP-U59-08 Domain validation

### D1 — /web/domain/validate
`Domain.validate()` at `web/controllers/domain.py:13` serves `/web/domain/validate` as `type='jsonrpc'`, `auth='user'`. Returns `True` if the domain is valid for the model. Validates by calling `model.sudo()._search(domain)` then executing `EXPLAIN <query>` via `SQL("EXPLAIN %s", query.select())` with `mute_logger`.

---

## CAP-U59-09 Action controller

### D1 — /web/action/load
`Action.load()` at `web/controllers/action.py:22` serves `/web/action/load` as `type='jsonrpc'`, `auth='user'`, `readonly=True`. Resolves numeric id, xmlid (dot notation), or path to an action. For `ir.actions.act_window` calls `_get_action_dict()`. All results pass through `clean_action(result, env=request.env)`.

### D2 — /web/action/run
`Action.run()` at `action.py:53` serves `/web/action/run` as `type='jsonrpc'`, `auth='user'`. Browses `ir.actions.server` and calls `action.run()`. Result passes through `clean_action`.

### D3 — /web/action/load_breadcrumbs
`Action.load_breadcrumbs()` at `action.py:61` serves `/web/action/load_breadcrumbs` as `type='jsonrpc'`, `auth='user'`, `readonly=True`. Accepts a list of action descriptors, resolves each to a display name via `load()` or direct `browse()`, handling `MissingActionError`, `MissingError`, `AccessError` per entry.

---

## CAP-U59-10 Webclient models — web_read / web_save / web_search_read

### D1 — web_read
`Base.web_read()` at `web/models/models.py:109` is decorated `@api.readonly`. For `many2one` fields with nested `fields` spec it calls `co_records.web_read(extra_fields)`. For `one2many`/`many2many` it respects `field_spec.get('order')`, `field_spec.get('limit')`, and access checks via `ir.model.access.check`. For `reference`/`many2one_reference` it checks `co_record.exists()` and handles `AccessError`. For `properties` type fields it resolves `many2one` and `many2many` property values recursively.

### D2 — web_search_read
`Base.web_search_read()` at `models.py:66` calls `self.search_fetch(domain, specification.keys(), ...)` then `records.web_read(specification)` and returns `{length, records}` from `_format_web_search_read_results()`. Length is determined by `search_count` only when `limit_reached` and not `count_limit_reached`.

### D3 — web_save
`Base.web_save()` at `models.py:90` calls `self.write(vals)` for existing records or `self.create(vals)` for new ones. With `next_id` it re-browses to that id. Returns `self.with_context(bin_size=True).web_read(specification)`.

### D4 — web_save_multi
`Base.web_save_multi()` at `models.py:99` validates `len(self) == len(vals_list)`, writes each record individually via `record.write(val)`, returns `web_read`.

### D5 — web_resequence
`Base.web_resequence()` at `models.py:322` writes incremental `sequence` values from `offset` to each record, returns `web_read`.

### D6 — web_name_search
`Base.web_name_search()` at `models.py:52` calls `name_search()` then `web_read(specification)`. For single-field `display_name` spec it returns a minimal list with `__formatted_display_name` from context `formatted_display_name=True`.

---

## CAP-U59-11 web_read_group and grouped data

### D1 — web_read_group
`Base.web_read_group()` at `models.py:349` is `@api.readonly`. Accepts `domain`, `groupby`, `aggregates`, `limit`, `offset`, `order`, `auto_unfold`, `opening_info`, `unfold_read_specification`, `unfold_read_default_limit`, `groupby_read_specification`. Calls `_formatted_read_group_with_length()`, then `_open_groups()` to determine which groups to unfold. For the last groupby level it schedules `web_search_read` calls batched via `self.browse().union(*recordset_groups)` and `all_records.web_read()`. Returns `{groups, length}`.

### D2 — formatted_read_group
`Base.formatted_read_group()` at `models.py:800` wraps `_read_group()`. Applies `_web_read_group_expand()` when `read_group_expand` context is set and field has `group_expand`. Applies `_web_read_group_fill_temporal()` when `fill_temporal` context is set. Returns formatted list via `_web_read_group_format()`.

### D3 — temporal filling
`Base._web_read_group_fill_temporal()` at `models.py:970` fills date/datetime holes in a grouped result. Accepts `fill_from`, `fill_to`, `min_groups` parameters. Uses `date_utils.date_range()` and locale-aware week handling. Handles timezone via `pytz` for datetime fields.

### D4 — formatted_read_grouping_sets
`Base.formatted_read_grouping_sets()` at `models.py:700` is a multi-groupby variant calling `_read_grouping_sets()`. Applies group_expand and fill_temporal per grouping set. Returns list-of-list of dicts.

### D5 — read_progress_bar
`Base.read_progress_bar()` at `models.py:1370` is `@api.readonly`. Accepts `domain`, `group_by`, `progress_bar` with `field`, `colors`, `sum` keys. Uses `formatted_read_group([group_by, progress_bar['field']], ['__count'])` to build color-keyed counts per group.

---

## CAP-U59-12 Search panel methods

### D1 — search_panel_select_range
`Base.search_panel_select_range()` at `models.py:1646` serves category panels. Supports `many2one` and `selection` fields. For `many2one` with `hierarchize=True` and `_parent_name` present, returns `parent_field` and calls `_search_panel_sanitized_parent_hierarchy()`. Returns `{'error_msg': ...}` when limit is reached.

### D2 — search_panel_select_multi_range
`Base.search_panel_select_multi_range()` at `models.py:1787` serves filter panels. Supports `many2one`, `many2many`, `selection`. With `group_by` parameter reads the groupby field value and label. Returns `{'error_msg': ...}` when limit is reached.

### D3 — _search_panel_field_image
`Base._search_panel_field_image()` at `models.py:1403` handles `enable_counters`, `only_counters`, `expand` flags. Calls `_search_panel_domain_image()` and optionally `_search_panel_global_counters()`.

---

## CAP-U59-13 ir.http model extensions

### D1 — Debug mode handling
`IrHttp._handle_debug()` at `web/models/ir_http.py:51` sets `request.session.debug` from the `debug` query param. Allowed modes defined at line 24: `['', '1', 'assets', 'tests']`. Multiple modes can be comma-separated.

### D2 — Bot detection
`IrHttp.is_a_bot()` at `ir_http.py:38` checks user-agent against a list of known bot strings including `bot`, `crawl`, `slurp`, `spider`, `curl`, `wget`, as well as `chatgpt-user`, `claude-user`, `perplexity-user`.

### D3 — Frontend session info
`IrHttp.get_frontend_session_info()` at `ir_http.py:175` returns a subset of session fields suitable for frontend pages: `is_admin`, `is_system`, `is_public`, `is_internal_user`, `uid`, `registry_hash`, `is_frontend`, `show_effect`, `currencies`, `quick_login`, `bundle_params`, `test_mode`.

### D4 — Cookie sanitization
`IrHttp._sanitize_cookies()` at `ir_http.py:45` replaces commas in `cids` cookie value with hyphens. Post-logout, `_post_logout()` at line 67 clears the `cids` cookie via `max_age=0`.

---

## CAP-U59-14 ir.ui.view extension for view info

### D1 — get_view_info
`IrUiView.get_view_info()` at `web/models/ir_ui_view.py:9` returns a dict of view types from `fields_get(['type'], ['selection'])`, excluding `qweb`, with `icon` and `multi_record` properties. Default view icons: `list` → `oi oi-view-list`, `form` → `fa fa-address-card`, `graph` → `fa fa-area-chart`, `pivot` → `oi oi-view-pivot`, `kanban` → `oi oi-view-kanban`, `calendar` → `fa fa-calendar`, `search` → `oi oi-search`.

---

## CAP-U59-15 res.users.settings — embedded actions

### D1 — embedded_actions_config_ids
`ResUsersSettings` at `web/models/res_users_settings.py:4` inherits `res.users.settings` and adds `embedded_actions_config_ids` as `One2many` to `res.users.settings.embedded.action`.

### D2 — set_embedded_actions_setting
`ResUsersSettings.set_embedded_actions_setting()` at line 20 accepts `action_id`, `res_id`, `vals`. Stores `embedded_actions_order` and `embedded_actions_visibility` as comma-separated string. Searches for existing config before creating.

---

## CAP-U59-16 Misc controllers

### D1 — Profiling
`Profiling.profile()` at `web/controllers/profiling.py:12` serves `/web/set_profiling` as `auth='public'`. Calls `ir.profile.set_profiling()`. `/web/speedscope/<profile>` at line 27 serves speedscope visualization, with optional memory profile view via `web.view_memory` template.

### D2 — View custom edit
`View.edit_custom()` at `web/controllers/view.py:11` serves `/web/view/edit_custom` as `type='jsonrpc'`, `auth='user'`. Verifies `custom_view.user_id == request.env.user` before writing arch.

### D3 — Pivot XLSX export
`TableExporter.export_xlsx()` at `web/controllers/pivot.py:16` serves `/web/pivot/export_xlsx` as `type='http'`, `auth='user'`, `readonly=True`. Parses JSON pivot data to write col group headers, measure headers, and row data to an xlsxwriter workbook.

### D4 — Model definitions
`Model.get_model_definitions()` at `web/controllers/model.py:8` serves `/web/model/get_definitions` as `auth='user'`, `methods=['POST']`. Calls `ir.model._get_definitions(model_names)`.

### D5 — Webmanifest
`web/controllers/webmanifest.py` (not fully read — RT for full content) — RT: expected to serve PWA manifest JSON.

---

## CAP-U59-17 web_tour module

### D1 — web_tour.tour model
`Web_TourTour` at `web_tour/models/tour.py:6` is `_name='web_tour.tour'`, ordered by `sequence, name, id`. Fields: `name` (required, unique constraint), `step_ids` (One2many to `web_tour.tour.step`), `url` (default `/odoo`), `rainbow_man_message` (Html, translatable), `sequence` (default 1000), `custom` (Boolean), `user_consumed_ids` (Many2many to `res.users`).

### D2 — Tour consumption
`Web_TourTour.consume()` at `tour.py:31` accepts `tourName`. If the user is internal, searches for the tour and links the current user via `Command.link()` to `user_consumed_ids`. Returns `get_current_tour()`.

### D3 — get_current_tour
`Web_TourTour.get_current_tour()` at `tour.py:38` returns the first unconsumed, non-custom tour for the user if `tour_enabled` is set. Searches `[("custom", "=", False), ("user_consumed_ids", "not in", self.env.user.id)]` and calls `_get_tour_json()` on the first result.

### D4 — _get_tour_json
`Web_TourTour._get_tour_json()` at `tour.py:49` reads `name`, `url`, `custom` fields, adds `steps` from `step_ids.get_steps_json()` and `rainbowManMessage`.

### D5 — export_js_file
`Web_TourTour.export_js_file()` at `tour.py:61` generates a JavaScript module string importing from `@web/core/registry` and creates an `ir.attachment` with mimetype `application/javascript`. Returns `ir.actions.act_url` to download.

### D6 — web_tour.tour.step model
`Web_TourTourStep` at `tour.py:83` is `_name='web_tour.tour.step'`, ordered by `sequence, id`. Fields: `trigger` (Char, required), `content` (Char), `tooltip_position` (Selection: bottom/top/right/left, default bottom), `tour_id` (Many2one, cascade), `run` (Char), `sequence` (Integer).

### D7 — get_steps_json
`Web_TourTourStep.get_steps_json()` at `tour.py:100` reads `trigger`, `content`, `run`, `tooltip_position` and renames `tooltip_position` to `tooltipPosition`. Omits `content` when empty.

### D8 — tour_enabled on res.users
`ResUsers.tour_enabled` at `web_tour/models/res_users.py:7` is a stored computed Boolean. `_compute_tour_enabled()` at line 9 sets it True only for admin users when `demo_modules_count == 0` and not in test mode.

### D9 — switch_tour_enabled
`ResUsers.switch_tour_enabled()` at `tour/res_users.py:16` is `@api.model`. Sets `self.env.user.sudo().tour_enabled = val` and returns the new value.

### D10 — Session info injection
`IrHttp.session_info()` at `web_tour/models/ir_http.py:7` inherits super and adds `tour_enabled` from `self.env.user.tour_enabled` and `current_tour` from `env["web_tour.tour"].get_current_tour()`.

---

## CAP-U59-18 web_hierarchy module

### D1 — hierarchy view type registration
`IrUiView` at `web_hierarchy/models/ir_ui_view.py:23` adds `('hierarchy', "Hierarchy")` to the `type` field selection. `_is_qweb_based_view()` returns True for `hierarchy` type.

### D2 — hierarchy view validation
`IrUiView._validate_tag_hierarchy()` at `ir_ui_view.py:31` validates that the hierarchy view contains at most one `templates` tag. Children must be `field` or `templates`. Valid attributes are defined in `HIERARCHY_VALID_ATTRIBUTES` at line 7.

### D3 — hierarchy view icon
`IrUiView._get_view_info()` at `ir_ui_view.py:56` returns `{'hierarchy': {'icon': 'fa fa-share-alt fa-rotate-90'}}` merged with `super()._get_view_info()`.

### D4 — hierarchy_read method
`Base.hierarchy_read()` at `web_hierarchy/models/models.py:10` accepts `domain`, `specification`, `parent_field`, `child_field`, `order`. For a single record it also fetches the parent and siblings. For multiple records it uses `_read_group([(parent_field, 'in', records.ids)], (parent_field,), ('id:array_agg',))` to build a `children_ids_per_record_id` dict. Calls `records.web_read(specification)` and injects `__child_ids__` key.

### D5 — hierarchy view mode registration
`IrActionsAct_WindowView` at `web_hierarchy/models/ir_actions.py:6` adds `('hierarchy', 'Hierarchy')` to `view_mode` field with `ondelete='cascade'`.

---

## CAP-U59-19 web_unsplash module

### D1 — Unsplash config settings
`ResConfigSettings` at `web_unsplash/models/res_config_settings.py:6` adds `unsplash_access_key` (config_parameter `unsplash.access_key`) and `unsplash_app_id` (config_parameter `unsplash.app_id`).

### D2 — Image search endpoint
`Web_Unsplash.fetch_unsplash_images()` at `web_unsplash/controllers/main.py:130` serves `/web_unsplash/fetch_images` as `type='jsonrpc'`, `auth='user'`. Retrieves `access_key` and `app_id` from system parameters. If missing, checks `_can_manage_unsplash_settings()` to distinguish `no_access` vs `key_not_found` errors. Calls `https://api.unsplash.com/search/photos/` with params including `client_id`.

### D3 — Image save/attachment endpoint
`Web_Unsplash.save_unsplash_url()` at `main.py:44` serves `/web_unsplash/attachment/add` as `type='jsonrpc'`, `auth='user'`, `methods=['POST']`. Accepts `unsplashurls` dict, downloads images via `requests.get()`, processes via `image_process(image, verify_resolution=True)`, creates `ir.attachment` records via `HTML_Editor._attachment_create()`, sets `url` to `/unsplash/<key>/<query>` format via sudo to bypass serving protection, and calls `_notify_download()` on each image.

### D4 — get_app_id endpoint
`Web_Unsplash.get_unsplash_app_id()` at `main.py:147` serves `/web_unsplash/get_app_id` as `type='jsonrpc'`, `auth='public'`. Returns `ir.config_parameter('unsplash.app_id')` via sudo.

### D5 — save_unsplash endpoint
`Web_Unsplash.save_unsplash()` at `main.py:151` serves `/web_unsplash/save_unsplash` as `type='jsonrpc'`, `auth='user'`. Checks `_can_manage_unsplash_settings()`. Sets `unsplash.app_id` and `unsplash.access_key` via `ir.config_parameter.sudo().set_param()`. Raises `NotFound` if unauthorized.

### D6 — _can_manage_unsplash_settings
`ResUsers._can_manage_unsplash_settings()` at `web_unsplash/models/res_users.py:9` returns True if the user has `base.group_erp_manager` or `website.group_website_restricted_editor` group (both checked via sudo).

### D7 — Download notification
`Web_Unsplash._notify_download()` at `main.py:25` sends a GET request to the Unsplash download URL with `client_id` param. Validates the URL starts with `https://api.unsplash.com/photos/` unless in test mode. Errors are logged but not raised.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U59-C001 | CAP-U59-01 | web/controllers/home.py:34 | `class Home(http.Controller):` | FACT | — | — | Home controller inherits http.Controller | N-U59-001 |
| VDR-U59-C002 | CAP-U59-01 | web/controllers/home.py:36 | `@http.route('/', type='http', auth="none")` | FACT | — | — | Root route uses auth=none | N-U59-001 |
| VDR-U59-C003 | CAP-U59-01 | web/controllers/home.py:46 | `@http.route(['/web', '/odoo', '/odoo/<path:subpath>', '/scoped_app/<path:subpath>'], type='http', auth="none", readonly=_web_client_readonly)` | FACT | — | — | Web client route covers /web, /odoo, /scoped_app paths | N-U59-001 |
| VDR-U59-C004 | CAP-U59-01 | web/controllers/home.py:55 | `if not security.check_session(request.session, request.env, request):` | FACT | — | — | Session validity is checked via security.check_session | N-U59-002 |
| VDR-U59-C005 | CAP-U59-01 | web/controllers/home.py:56 | `raise http.SessionExpiredException("Session expired")` | FACT | — | — | Expired sessions raise SessionExpiredException | N-U59-002 |
| VDR-U59-C006 | CAP-U59-01 | web/controllers/home.py:67 | `request.env.user._on_webclient_bootstrap()` | FACT | — | — | _on_webclient_bootstrap is called on every web client load | N-U59-001 |
| VDR-U59-C007 | CAP-U59-01 | web/controllers/home.py:74 | `session_info['browser_cache_secret'] = hmac(request.env(su=True), "browser_cache_key", hmac_payload)` | FACT | — | — | browser_cache_secret HMAC is injected into session_info in webclient page only | N-U59-002 |
| VDR-U59-C008 | CAP-U59-01 | web/controllers/home.py:79 | `response.headers['Cache-Control'] = 'no-store'` | FACT | — | — | Webclient bootstrap response sets Cache-Control: no-store | N-U59-002 |
| VDR-U59-C009 | CAP-U59-01 | web/controllers/home.py:85 | `@http.route('/web/webclient/load_menus', type='http', auth='user', methods=['GET'], readonly=True)` | FACT | — | — | load_menus is GET, readonly=True, auth=user | N-U59-003 |
| VDR-U59-C010 | CAP-U59-01 | web/controllers/home.py:103 | `@http.route('/web/login', type='http', auth='none', readonly=False` | FACT | — | — | Login route explicitly sets readonly=False | N-U59-004 |
| VDR-U59-C011 | CAP-U59-01 | web/controllers/home.py:31 | `CREDENTIAL_PARAMS = ['login', 'password', 'type']` | FACT | — | — | Credential params are login, password, type | N-U59-004 |
| VDR-U59-C012 | CAP-U59-01 | web/controllers/home.py:129 | `credential.setdefault('type', 'password')` | FACT | — | — | Default credential type is password | N-U59-004 |
| VDR-U59-C013 | CAP-U59-01 | web/controllers/home.py:173 | `@http.route('/web/health', type='http', auth='none', save_session=False)` | FACT | — | — | Health check route uses save_session=False | N-U59-005 |
| VDR-U59-C014 | CAP-U59-01 | web/controllers/home.py:179 | `odoo.sql_db.db_connect('postgres').cursor().close()` | FACT | — | — | DB server health check connects to postgres directly | N-U59-005 |
| VDR-U59-C015 | CAP-U59-02 | web/controllers/session.py:25 | `@http.route('/web/session/get_session_info', type='jsonrpc', auth='user', readonly=True)` | FACT | — | — | get_session_info is jsonrpc, auth=user, readonly | N-U59-006 |
| VDR-U59-C016 | CAP-U59-02 | web/controllers/session.py:31 | `@http.route('/web/session/authenticate', type='jsonrpc', auth="none", readonly=False)` | FACT | — | — | authenticate route is auth=none, readonly=False | N-U59-006 |
| VDR-U59-C017 | CAP-U59-02 | web/controllers/session.py:47 | `if auth_info['uid'] != request.session.uid:` | FACT | — | — | MFA session mismatch returns uid=None | N-U59-006 |
| VDR-U59-C018 | CAP-U59-02 | web/controllers/session.py:64 | `@http.route('/web/session/modules', type='jsonrpc', auth='user', readonly=True)` | FACT | — | — | modules endpoint returns list(registry._init_modules) | N-U59-007 |
| VDR-U59-C019 | CAP-U59-02 | web/controllers/session.py:88 | `@http.route('/web/session/logout', type='http', auth='none', readonly=True)` | FACT | — | — | Logout route is auth=none, readonly=True | N-U59-007 |
| VDR-U59-C020 | CAP-U59-02 | web/models/ir_http.py:84 | `def session_info(self):` | FACT | — | — | session_info() is defined on IrHttp model | N-U59-006 |
| VDR-U59-C021 | CAP-U59-02 | web/models/ir_http.py:110 | `"registry_hash": hmac(self.env(su=True), "webclient-cache", self.env.registry.registry_sequence),` | FACT | — | — | registry_hash is HMAC of registry_sequence with "webclient-cache" key | N-U59-008 |
| VDR-U59-C022 | CAP-U59-02 | web/models/ir_http.py:134 | 'groups': | FACT | — | — | session_info includes groups dict with base.group_allow_export check | N-U59-006 |
| VDR-U59-C023 | CAP-U59-02 | web/models/ir_http.py:143 | `user_companies = self.env['res.company'].browse(user._get_company_ids()).sudo()` | FACT | — | — | Company hierarchy is fetched via sudo using _get_company_ids cache | N-U59-006 |
| VDR-U59-C024 | CAP-U59-03 | web/controllers/dataset.py:15 | `def _call_kw_readonly(self, rule, args):` | FACT | — | — | readonly flag determined dynamically by inspecting method._readonly attribute | N-U59-009 |
| VDR-U59-C025 | CAP-U59-03 | web/controllers/dataset.py:28 | `@http.route(['/web/dataset/call_kw', '/web/dataset/call_kw/<path:path>'], type='jsonrpc', auth="user", readonly=_call_kw_readonly)` | FACT | — | — | call_kw route is jsonrpc, auth=user | N-U59-009 |
| VDR-U59-C026 | CAP-U59-03 | web/controllers/dataset.py:32 | `return call_kw(request.env[model], method, args, kwargs)` | FACT | — | — | call_kw delegates to odoo.service.model.call_kw | N-U59-009 |
| VDR-U59-C027 | CAP-U59-03 | web/controllers/dataset.py:38 | `action = call_kw(request.env[model], method, args, kwargs)` | FACT | — | — | call_button executes call_kw and optionally passes result through clean_action | N-U59-009 |
| VDR-U59-C028 | CAP-U59-04 | web/controllers/binary.py:62 | @http.route | FACT | — | — | /web/content routes are auth=public, readonly | N-U59-010 |
| VDR-U59-C029 | CAP-U59-04 | web/controllers/binary.py:77 | `record = request.env['ir.binary']._find_record(xmlid, model, id and int(id), access_token, field=field)` | FACT | — | — | ir.binary._find_record resolves attachment/record by xmlid or id | N-U59-010 |
| VDR-U59-C030 | CAP-U59-04 | web/controllers/binary.py:85 | `send_file_kwargs['immutable'] = True` | FACT | — | — | unique parameter triggers immutable caching | N-U59-010 |
| VDR-U59-C031 | CAP-U59-04 | web/controllers/binary.py:183 | `], type='http', auth='public', readonly=True, save_session=False)` | FACT | — | — | /web/image routes use save_session=False | N-U59-010 |
| VDR-U59-C032 | CAP-U59-04 | web/controllers/binary.py:219 | `@http.route('/web/binary/upload_attachment', type='http', auth="user")` | FACT | — | — | upload_attachment is type=http, auth=user | N-U59-011 |
| VDR-U59-C033 | CAP-U59-04 | web/controllers/binary.py:237 | attachment = Model.create | FACT | — | — | Attachment creation uses raw content with res_model and res_id | N-U59-011 |
| VDR-U59-C034 | CAP-U59-04 | web/controllers/binary.py:275 | request.env.cr.execute | FACT | — | — | Company logo fetched via direct SQL joining res_users and res_company | N-U59-012 |
| VDR-U59-C035 | CAP-U59-05 | web/controllers/export.py:291 | `@http.route('/web/export/formats', type='jsonrpc', auth='user', readonly=True)` | FACT | — | — | Export formats endpoint is jsonrpc, readonly | N-U59-013 |
| VDR-U59-C036 | CAP-U59-05 | web/controllers/export.py:556 | `params = json.loads(data)` | FACT | — | — | Export base method parses data as JSON | N-U59-013 |
| VDR-U59-C037 | CAP-U59-05 | web/controllers/export.py:569 | `records = Model.browse(ids) if ids else Model.search(domain)` | FACT | — | — | Export either browses provided ids or searches domain | N-U59-013 |
| VDR-U59-C038 | CAP-U59-05 | web/controllers/export.py:615 | `for batch in split_every(PREFETCH_MAX, records.ids, Model.browse):` | FACT | — | — | Non-grouped export batches records by PREFETCH_MAX | N-U59-013 |
| VDR-U59-C039 | CAP-U59-05 | web/controllers/export.py:640 | `@http.route('/web/export/csv', type='http', auth='user')` | FACT | — | — | CSV export route is type=http | N-U59-013 |
| VDR-U59-C040 | CAP-U59-05 | web/controllers/export.py:688 | `@http.route('/web/export/xlsx', type='http', auth='user')` | FACT | — | — | XLSX export route is type=http | N-U59-013 |
| VDR-U59-C041 | CAP-U59-06 | web/controllers/report.py:23 | @http.route | FACT | — | — | Report routes use website=True, readonly=True | N-U59-014 |
| VDR-U59-C042 | CAP-U59-06 | web/controllers/report.py:39 | `html = report.with_context(context)._render_qweb_html(reportname, docids, data=data)[0]` | FACT | — | — | HTML converter calls ir.actions.report._render_qweb_html | N-U59-014 |
| VDR-U59-C043 | CAP-U59-06 | web/controllers/report.py:92 | `@http.route(['/report/download'], type='http', auth="user")` | FACT | — | — | Report download is type=http, auth=user | N-U59-014 |
| VDR-U59-C044 | CAP-U59-06 | web/controllers/report.py:136 | `report_name = safe_eval(report.print_report_name, {'object': obj, 'time': time})` | FACT | — | — | Custom report filename evaluated via safe_eval | N-U59-014 |
| VDR-U59-C045 | CAP-U59-07 | web/controllers/webclient.py:18 | `@http.route('/web/webclient/bootstrap_translations', type='jsonrpc', auth="none")` | FACT | — | — | bootstrap_translations is auth=none jsonrpc | N-U59-015 |
| VDR-U59-C046 | CAP-U59-07 | web/controllers/webclient.py:37 | `if manifest and manifest['bootstrap']:` | FACT | — | — | Only modules with bootstrap=True in manifest get translations loaded | N-U59-015 |
| VDR-U59-C047 | CAP-U59-07 | web/controllers/webclient.py:46 | `@http.route('/web/webclient/translations', type='http', auth='public', cors='*', readonly=True)` | FACT | — | — | Translations route is type=http, auth=public, cors=* | N-U59-015 |
| VDR-U59-C048 | CAP-U59-07 | web/controllers/webclient.py:64 | `current_hash = request.env["ir.http"].with_context(cache_translation_data=True)._get_web_translations_hash(mods, lang)` | FACT | — | — | Translations hash computed via ir.http._get_web_translations_hash with cache_translation_data context | N-U59-015 |
| VDR-U59-C049 | CAP-U59-07 | web/controllers/webclient.py:85 | `('Cache-Control', f'public, max-age={http.STATIC_CACHE_LONG}'),` | FACT | — | — | Translations cached with STATIC_CACHE_LONG max-age | N-U59-015 |
| VDR-U59-C050 | CAP-U59-08 | web/controllers/domain.py:31 | `sql = SQL("EXPLAIN %s", query.select())` | FACT | — | — | Domain validation uses EXPLAIN to verify SQL without executing | N-U59-016 |
| VDR-U59-C051 | CAP-U59-09 | web/controllers/action.py:22 | `@route('/web/action/load', type='jsonrpc', auth='user', readonly=True)` | FACT | — | — | action/load is jsonrpc, readonly | N-U59-017 |
| VDR-U59-C052 | CAP-U59-09 | web/controllers/action.py:48 | `result = request.env[action_type].sudo().browse([action_id])._get_action_dict()` | FACT | — | — | act_window actions loaded via sudo._get_action_dict() | N-U59-017 |
| VDR-U59-C053 | CAP-U59-09 | web/controllers/utils.py:23 | `def clean_action(action, env):` | FACT | — | — | clean_action filters action dict to readable_fields from env[action_type]._get_readable_fields() | N-U59-017 |
| VDR-U59-C054 | CAP-U59-10 | web/models/models.py:109 | `@api.readonly` | FACT | — | — | web_read is decorated @api.readonly | N-U59-018 |
| VDR-U59-C055 | CAP-U59-10 | web/models/models.py:113 | `if fields_to_read == ['id']:` | FACT | — | — | Optimisation: id-only reads skip database call | N-U59-018 |
| VDR-U59-C056 | CAP-U59-10 | web/models/models.py:117 | `values_list: list[dict] = self.read(fields_to_read, load=None)` | FACT | — | — | web_read calls self.read with load=None | N-U59-018 |
| VDR-U59-C057 | CAP-U59-10 | web/models/models.py:162 | elif field.type in ('one2many', 'many2many') | FACT | — | — | many2one without nested fields spec skips sub-read | N-U59-018 |
| VDR-U59-C058 | CAP-U59-10 | web/models/models.py:66 | `def web_search_read(self, domain, specification, offset=0, limit=None, order=None, count_limit=None):` | FACT | — | — | web_search_read accepts count_limit for capped length counting | N-U59-019 |
| VDR-U59-C059 | CAP-U59-10 | web/models/models.py:90 | `def web_save(self, vals, specification: dict[str, dict], next_id=None) -> list[dict]:` | FACT | — | — | web_save signature includes next_id for post-save navigation | N-U59-019 |
| VDR-U59-C060 | CAP-U59-10 | web/models/models.py:97 | `return self.with_context(bin_size=True).web_read(specification)` | FACT | — | — | web_save returns web_read result with bin_size=True | N-U59-019 |
| VDR-U59-C061 | CAP-U59-11 | web/models/models.py:349 | `def web_read_group(` | FACT | — | — | web_read_group is @api.model, @api.readonly | N-U59-020 |
| VDR-U59-C062 | CAP-U59-11 | web/models/models.py:419 | `if '__count' not in aggregates:` | FACT | — | — | __count aggregate automatically added by web_read_group | N-U59-020 |
| VDR-U59-C063 | CAP-U59-11 | web/models/models.py:599 | `max_number_opened_group = self.env.context.get('max_number_opened_groups') or MAX_NUMBER_OPENED_GROUPS` | FACT | — | — | max_number_opened_groups context key overrides default of 10 | N-U59-020 |
| VDR-U59-C064 | CAP-U59-11 | web/models/models.py:800 | `def formatted_read_group(` | FACT | — | — | formatted_read_group is @api.model, @api.readonly | N-U59-021 |
| VDR-U59-C065 | CAP-U59-11 | web/models/models.py:881 | `aggregates = tuple(agg.replace(':recordset', ':array_agg') for agg in aggregates)` | FACT | — | — | :recordset aggregate spec converted to :array_agg internally | N-U59-021 |
| VDR-U59-C066 | CAP-U59-11 | web/models/models.py:28 | `SEARCH_PANEL_ERROR_MESSAGE = _lt("Too many items to display.")` | FACT | — | — | SEARCH_PANEL_ERROR_MESSAGE uses LazyTranslate | N-U59-022 |
| VDR-U59-C067 | CAP-U59-11 | web/models/models.py:1370 | `def read_progress_bar(self, domain, group_by, progress_bar):` | FACT | — | — | read_progress_bar is @api.readonly | N-U59-022 |
| VDR-U59-C068 | CAP-U59-12 | web/models/models.py:1646 | `def search_panel_select_range(self, field_name, **kwargs):` | FACT | — | — | search_panel_select_range supports many2one and selection | N-U59-022 |
| VDR-U59-C069 | CAP-U59-12 | web/models/models.py:1787 | `def search_panel_select_multi_range(self, field_name, **kwargs):` | FACT | — | — | search_panel_select_multi_range supports many2one, many2many, selection | N-U59-022 |
| VDR-U59-C070 | CAP-U59-13 | web/models/ir_http.py:24 | `ALLOWED_DEBUG_MODES = ['', '1', 'assets', 'tests']` | FACT | — | — | Only four debug modes are allowed | N-U59-023 |
| VDR-U59-C071 | CAP-U59-13 | web/models/ir_http.py:30 | bots = | FACT | — | — | Bot detection list includes AI crawlers claude-user, chatgpt-user, perplexity-user | N-U59-023 |
| VDR-U59-C072 | CAP-U59-13 | web/models/ir_http.py:45 | `if cids := cookies.get('cids'):` | FACT | — | — | cids cookie value has commas replaced with hyphens on sanitization | N-U59-023 |
| VDR-U59-C073 | CAP-U59-14 | web/models/ir_ui_view.py:23 | `'list': {'icon': 'oi oi-view-list'},` | FACT | — | — | list view icon is oi oi-view-list | N-U59-024 |
| VDR-U59-C074 | CAP-U59-14 | web/models/ir_ui_view.py:24 | `'form': {'icon': 'fa fa-address-card', 'multi_record': False},` | FACT | — | — | form view has multi_record=False | N-U59-024 |
| VDR-U59-C075 | CAP-U59-15 | web/models/res_users_settings.py:7 | `embedded_actions_config_ids = fields.One2many('res.users.settings.embedded.action', 'user_setting_id')` | FACT | — | — | Embedded action configs linked to user settings via One2many | N-U59-025 |
| VDR-U59-C076 | CAP-U59-15 | web/models/res_users_settings.py:27 | `new_vals[field] = ','.join('false' if action_id is False else str(action_id) for action_id in value)` | FACT | — | — | embedded_actions_order and embedded_actions_visibility stored as comma-separated strings | N-U59-025 |
| VDR-U59-C077 | CAP-U59-17 | web_tour/models/tour.py:6 | `class Web_TourTour(models.Model):` | FACT | — | — | Tour model is web_tour.tour | N-U59-026 |
| VDR-U59-C078 | CAP-U59-17 | web_tour/models/tour.py:18 | `user_consumed_ids = fields.Many2many("res.users")` | FACT | — | — | Tour tracks consumed users via Many2many to res.users | N-U59-026 |
| VDR-U59-C079 | CAP-U59-17 | web_tour/models/tour.py:20 | _uniq_name = models.Constraint | FACT | — | — | Tour name has unique database constraint | N-U59-026 |
| VDR-U59-C080 | CAP-U59-17 | web_tour/models/tour.py:31 | `def consume(self, tourName):` | FACT | — | — | consume() is @api.model, links user via Command.link | N-U59-026 |
| VDR-U59-C081 | CAP-U59-17 | web_tour/models/tour.py:41 | `tours_to_run = self.search([("custom", "=", False), ("user_consumed_ids", "not in", self.env.user.id)])` | FACT | — | — | get_current_tour searches non-custom, non-consumed tours | N-U59-026 |
| VDR-U59-C082 | CAP-U59-17 | web_tour/models/tour.py:62 | `js_content = f"""import {{ registry }} from '@web/core/registry';` | FACT | — | — | export_js_file generates ES module import from @web/core/registry | N-U59-027 |
| VDR-U59-C083 | CAP-U59-17 | web_tour/models/tour.py:83 | `class Web_TourTourStep(models.Model):` | FACT | — | — | Tour step model is web_tour.tour.step | N-U59-026 |
| VDR-U59-C084 | CAP-U59-17 | web_tour/models/tour.py:88 | `trigger = fields.Char(required=True)` | FACT | — | — | Step trigger field is required | N-U59-026 |
| VDR-U59-C085 | CAP-U59-17 | web_tour/models/res_users.py:7 | `tour_enabled = fields.Boolean(compute='_compute_tour_enabled', store=True, readonly=False, string="Onboarding")` | FACT | — | — | tour_enabled is stored Boolean, labelled Onboarding | N-U59-028 |
| VDR-U59-C086 | CAP-U59-17 | web_tour/models/res_users.py:11 | `user.tour_enabled = user._is_admin() and demo_modules_count == 0 and not modules.module.current_test` | FACT | — | — | tour_enabled is True only for admin with no demo modules and not in test | N-U59-028 |
| VDR-U59-C087 | CAP-U59-17 | web_tour/models/ir_http.py:8 | `result["tour_enabled"] = self.env.user.tour_enabled` | FACT | — | — | tour_enabled injected into session_info by web_tour | N-U59-028 |
| VDR-U59-C088 | CAP-U59-17 | web_tour/models/ir_http.py:10 | `result['current_tour'] = self.env["web_tour.tour"].get_current_tour()` | FACT | — | — | current_tour injected into session_info by web_tour | N-U59-028 |
| VDR-U59-C089 | CAP-U59-18 | web_hierarchy/models/ir_ui_view.py:7 | `HIERARCHY_VALID_ATTRIBUTES = {` | FACT | — | — | Hierarchy view XML attributes are validated against a fixed set | N-U59-029 |
| VDR-U59-C090 | CAP-U59-18 | web_hierarchy/models/ir_ui_view.py:26 | `type = fields.Selection(selection_add=[('hierarchy', "Hierarchy")])` | FACT | — | — | web_hierarchy adds hierarchy type to ir.ui.view | N-U59-029 |
| VDR-U59-C091 | CAP-U59-18 | web_hierarchy/models/ir_ui_view.py:28 | `return super()._is_qweb_based_view(view_type) or view_type == "hierarchy"` | FACT | — | — | hierarchy view is treated as qweb-based | N-U59-029 |
| VDR-U59-C092 | CAP-U59-18 | web_hierarchy/models/models.py:10 | `def hierarchy_read(self, domain, specification, parent_field, child_field=None, order=None):` | FACT | — | — | hierarchy_read is an @api.model method on base | N-U59-030 |
| VDR-U59-C093 | CAP-U59-18 | web_hierarchy/models/models.py:36 | result = records.web_read(specification) | FACT | — | — | hierarchy_read injects __child_ids__ key into result | N-U59-030 |
| VDR-U59-C094 | CAP-U59-18 | web_hierarchy/models/ir_actions.py:9 | `view_mode = fields.Selection(selection_add=[('hierarchy', 'Hierarchy')], ondelete={'hierarchy': 'cascade'})` | FACT | — | — | hierarchy view mode added to ir.actions.act_window.view with cascade ondelete | N-U59-029 |
| VDR-U59-C095 | CAP-U59-18 | web_hierarchy/models/ir_ui_view.py:57 | return {'hierarchy | FACT | — | — | hierarchy view icon is fa fa-share-alt fa-rotate-90 | N-U59-029 |
| VDR-U59-C096 | CAP-U59-19 | web_unsplash/models/res_config_settings.py:9 | `unsplash_access_key = fields.Char("Access Key", config_parameter='unsplash.access_key')` | FACT | — | — | Unsplash access key stored in ir.config_parameter unsplash.access_key | N-U59-031 |
| VDR-U59-C097 | CAP-U59-19 | web_unsplash/models/res_config_settings.py:10 | `unsplash_app_id = fields.Char("Application ID", config_parameter='unsplash.app_id')` | FACT | — | — | Unsplash app id stored in ir.config_parameter unsplash.app_id | N-U59-031 |
| VDR-U59-C098 | CAP-U59-19 | web_unsplash/controllers/main.py:44 | `@http.route('/web_unsplash/attachment/add', type='jsonrpc', auth='user', methods=['POST'])` | FACT | — | — | Unsplash image save endpoint is jsonrpc POST auth=user | N-U59-031 |
| VDR-U59-C099 | CAP-U59-19 | web_unsplash/controllers/main.py:84 | `if not url.startswith(('https://images.unsplash.com/', 'https://plus.unsplash.com/')) and not modules.module.current_test:` | FACT | — | — | Unsplash image URLs validated against known prefixes unless in test mode | N-U59-031 |
| VDR-U59-C100 | CAP-U59-19 | web_unsplash/controllers/main.py:101 | `image = image_process(image, verify_resolution=True)` | FACT | — | — | Downloaded Unsplash images pass through image_process with verify_resolution=True | N-U59-031 |
| VDR-U59-C101 | CAP-U59-19 | web_unsplash/controllers/main.py:119 | `attachment.sudo().url = '/' + '/'.join(url_frags)` | FACT | — | — | Attachment URL set via sudo to bypass serving protection | N-U59-031 |
| VDR-U59-C102 | CAP-U59-19 | web_unsplash/controllers/main.py:130 | `@http.route("/web_unsplash/fetch_images", type='jsonrpc', auth="user")` | FACT | — | — | fetch_images is jsonrpc auth=user | N-U59-031 |
| VDR-U59-C103 | CAP-U59-19 | web_unsplash/controllers/main.py:139 | `response = requests.get('https://api.unsplash.com/search/photos/', params=url_encode(post))` | FACT | — | — | Image search proxied to api.unsplash.com/search/photos | N-U59-031 |
| VDR-U59-C104 | CAP-U59-19 | web_unsplash/controllers/main.py:147 | `@http.route("/web_unsplash/get_app_id", type='jsonrpc', auth="public")` | FACT | — | — | get_app_id endpoint is auth=public | N-U59-031 |
| VDR-U59-C105 | CAP-U59-19 | web_unsplash/models/res_users.py:15 | return (self.sudo | FACT | — | — | Unsplash settings manageable by ERP manager or website restricted editor | N-U59-031 |
