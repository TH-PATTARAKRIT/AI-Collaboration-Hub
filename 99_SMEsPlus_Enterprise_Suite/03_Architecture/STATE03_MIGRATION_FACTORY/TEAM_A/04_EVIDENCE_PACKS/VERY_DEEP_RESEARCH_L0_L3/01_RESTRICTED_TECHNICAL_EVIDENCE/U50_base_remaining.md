# U50 — base remaining: ir_module, ir_ui_view, ir_qweb, ir_http, mail-server, filters, exports (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U50
- Modules: base (remaining unread areas)
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — reading areas of base/models/ and base/wizard/ not covered in U01. Source evidence only; RT flags for runtime unknowns. No redoing U01 work.

---

## CAP-U50-01 — Module Management and State Machine (ir.module.module)

### D1 Business purpose and process semantics
The `ir.module.module` model is the central registry for all Odoo add-on packages. It tracks installation state, inter-module dependencies, exclusions, version information, and auto-install eligibility. Business users and system administrators interact via the Apps menu to install, upgrade, or remove modules. The system enforces that only an admin-level user can trigger module operations.

### D2 Architecture, data and object relationships
- `ir.module.module` is the primary model; `ir.module.category` provides hierarchical grouping.
- `ir.module.module.dependency` stores each module's declared dependency list.
- `ir.module.module.exclusion` stores declared incompatibilities between modules.
- State machine has six legal values: `uninstallable`, `uninstalled`, `installed`, `to upgrade`, `to remove`, `to install`.
- The `auto_install` flag on the module record controls whether the system automatically installs the module when all its `auto_install_required` dependencies are satisfied.

### D3 Source, technical and workflow logic
- `STATES` constant at line 140 defines the six states.
- `assert_log_admin_access` decorator (lines 57-73) guards all install/upgrade/uninstall entry points; raises `AccessDenied` if `env.is_admin()` is False.
- `button_install` (line 408) iterates auto-installable modules in a loop; uses `must_install` closure that checks `dep.auto_install_required` and country restrictions.
- `_state_update` (line 378) recurses depth-first through dependency graph with `level` guard (raises `UserError` at level < 1).
- `button_upgrade` (line 704) cascades through dependent installed modules and marks them `to upgrade`.
- `downstream_dependencies` (line 532) and `upstream_dependencies` (line 557) use raw SQL recursive queries against `ir_module_module_dependency`.
- `_button_immediate_function` (line 599) acquires an `EXCLUSIVE MODE` lock on `ir_module_module` and also locks `ir_cron` to prevent concurrent operations.
- `update_list` (line 788) iterates `modules.Manifest.all_addon_manifests()` and syncs installed/uninstalled states.
- `module_uninstall` (line 508) calls `ir.model.data._module_data_uninstall` then sets state to `uninstalled`.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'ir.module.module'` at `ir_module.py:159` |
| D2 | State machine | `STATES` list at `ir_module.py:140-147` (six values) |
| D3 | Admin guard | `assert_log_admin_access` decorator `ir_module.py:57-73` |
| D4 | Auto-install logic | `must_install` closure in `button_install` `ir_module.py:418-422` |
| D5 | Dependency recursion | `_state_update` with `level` param `ir_module.py:378-405` |
| D6 | Concurrent lock | `LOCK ir_module_module IN EXCLUSIVE MODE` `ir_module.py:619` |
| D7 | Downstream deps | `downstream_dependencies` SQL query `ir_module.py:542-548` |
| D8 | Upstream deps | `upstream_dependencies` SQL query `ir_module.py:567-574` |
| D9 | Module uninstall | `module_uninstall` calls `_module_data_uninstall` `ir_module.py:514` |
| D10 | List update | `update_list` iterates `Manifest.all_addon_manifests()` `ir_module.py:797` |

---

## CAP-U50-02 — View Inheritance and Architecture Combining (ir.ui.view)

### D1 Business purpose and process semantics
`ir.ui.view` stores all UI view definitions (form, list, kanban, search, qweb, etc.) in the database. View inheritance allows modules to extend or override parent view architectures using xpath or field-name locators. The system supports soft and hard reset of broken views, COW (copy-on-write) for website views, and partial validation during module upgrades.

### D2 Architecture, data and object relationships
- Primary fields: `arch_db` (stored XML blob), `arch_fs` (filesystem path for dev-xml mode), `arch_prev` (previous arch for soft reset), `arch_updated` (dirty flag).
- `inherit_id` links an extension view to its parent; `mode` field controls whether the view is `primary` or `extension`.
- `group_ids` M2M to `res.groups` restricts view visibility.
- `IrUiViewCustom` (`ir.ui.view.custom`) stores per-user dashboard/view customisations.
- Inheritance tree is traversed by `_get_inheriting_views` using a recursive CTE SQL query.

### D3 Source, technical and workflow logic
- `_compute_arch` (line 209) reads from file in dev-xml mode when `arch_updated` is False, otherwise falls back to `arch_db`.
- `_inverse_arch` (line 247) writes `arch_db` and stores relative `arch_fs` path from `install_filename` context.
- `_check_xml` (line 427) verifies inheritance resolves correctly, validates combined arch with `valid_view`, and raises `ValidationError` for invalid views.
- `_check_groups` constraint (line 537) forbids `group_ids` on extension views (must use group attributes in arch).
- `_check_000_inheritance` (line 545) prevents recursive `inherit_id` cycles.
- `_get_inheriting_views` (line 724) uses a recursive CTE joining `ir_ui_view_inherits` ordered by `priority, id`.
- `locate_node` (line 867) delegates to `odoo.tools.template_inheritance.locate_node`.
- `reset_arch` (line 279) implements soft (from `arch_prev`) and hard (from `arch_fs`) reset.
- `_check_view_access` (line 803) checks `group_ids` intersection with user groups; raises `AccessError` for private views.
- `VIEW_MODIFIERS` constant at line 34 defines `column_invisible`, `invisible`, `readonly`, `required`.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'ir.ui.view'` at `ir_ui_view.py:141` |
| D2 | Arch storage fields | `arch_db`, `arch_fs`, `arch_prev`, `arch_updated` declared `ir_ui_view.py:162-166` |
| D3 | Arch compute | `_compute_arch` reads file in dev-xml mode `ir_ui_view.py:209-245` |
| D4 | Inheritance mode | `mode` field with `primary`/`extension` values `ir_ui_view.py:177-188` |
| D5 | Recursive CTE query | `_get_inheriting_views` SQL WITH RECURSIVE `ir_ui_view.py:742-762` |
| D6 | XML validation | `_check_xml` with `valid_view` call `ir_ui_view.py:427-534` |
| D7 | Group access check | `_check_view_access` group intersection `ir_ui_view.py:803-819` |
| D8 | Soft/hard reset | `reset_arch` modes `ir_ui_view.py:279-293` |
| D9 | Cycle prevention | `_check_000_inheritance` with `_has_cycle` `ir_ui_view.py:545-550` |
| D10 | Custom views | `ir.ui.view.custom` with per-user ref `ir_ui_view.py:66-78` |

---

## CAP-U50-03 — QWeb Template Rendering Engine (ir.qweb)

### D1 Business purpose and process semantics
QWeb is Odoo's XML-based template engine used to generate HTML pages, email bodies, PDF reports, and UI components. It compiles XML templates into Python generator functions at compile time (cached via ORM cache), then executes those functions at render time. This separation ensures compile cost is paid once.

### D2 Architecture, data and object relationships
- `IrQweb` (abstract model) with `_name = 'ir.qweb'` provides `_render` and `_compile`.
- Output is `MarkupSafe` format to prevent XSS injection.
- Compiled functions are cached via ORM cache keyed on template ref and options.
- `AssetsBundle` (imported at line 411) handles JavaScript/CSS bundling called from `t-call-assets`.
- Security: compiled expressions validated against `_SAFE_QWEB_OPCODES` allowlist (line 423-465).

### D3 Source, technical and workflow logic
- Directive processing order defined by `_directives_eval_order`; dispatched through `_compile_directive_[name]` methods.
- `t-if`/`t-elif`/`t-else`: Python `if` blocks; sibling structure checked at compile time (`ir_qweb.py:139-172`).
- `t-foreach`/`t-as`: loop compiled to Python `for`; loop variables `*_value`, `*_index`, `*_size`, `*_first`, `*_last` injected into `values` dict (`ir_qweb.py:193-201`).
- `t-groups`: calls `has_group` on `res.users` at render time (`ir_qweb.py:186-190`).
- `t-call`: copies `values` dict, renders inner content to `T_CALL_SLOT='0'`, compiles called template (`ir_qweb.py:239-256`).
- `t-out`: outputs MarkupSafe value; `t-esc` and `t-raw` are deprecated aliases (`ir_qweb.py:278-309`).
- `t-set`: updates `values` dict with `t-value` expression or node content (`ir_qweb.py:312-317`).
- `_SAFE_QWEB_OPCODES` constant at line 423 is a whitelist of Python bytecodes allowed in compiled expressions.
- `MALICIOUS_SCHEMES` regex at line 491 blocks `javascript:` URLs except `history.back()`.
- `T_CALL_SLOT = '0'` at line 486 is the magic slot name for `t-call` inner content.
- `VOID_ELEMENTS` frozenset at line 472 lists self-closing HTML elements.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Compile-then-render | `_compile` returns function, `_render` calls it `ir_qweb.py:70-71` |
| D2 | MarkupSafe output | documented at `ir_qweb.py:50-53` |
| D3 | ORM cache | compiled function is orm cached `ir_qweb.py:43-44` |
| D4 | t-if directive | Python if block compiled `ir_qweb.py:139-172` |
| D5 | t-foreach loop variables | `*_value`, `*_index`, etc. injected `ir_qweb.py:200-201` |
| D6 | t-groups security | calls `has_group` `ir_qweb.py:186-190` |
| D7 | Safe opcode allowlist | `_SAFE_QWEB_OPCODES` `ir_qweb.py:423-465` |
| D8 | XSS URL block | `MALICIOUS_SCHEMES` regex `ir_qweb.py:491` |
| D9 | t-call slot | `T_CALL_SLOT = '0'` `ir_qweb.py:486` |
| D10 | Asset bundling | `t-call-assets` calls `_get_asset_nodes` `ir_qweb.py:273-278` |

---

## CAP-U50-04 — HTTP Routing Layer (ir.http)

### D1 Business purpose and process semantics
`ir.http` is the abstract model that manages Odoo's HTTP routing map. It provides authentication methods (`user`, `public`, `none`, `bearer`), URL slug generation, custom Werkzeug converters for ORM models, and pre/post dispatch hooks. All web controllers register via the `@route` decorator and are compiled into the routing map through this model.

### D2 Architecture, data and object relationships
- `IrHttp` is `models.AbstractModel` with `_name = 'ir.http'`.
- `ModelConverter` and `ModelsConverter` are Werkzeug converters that look up ORM records from URL segments.
- `FasterRule` is a subclass of `werkzeug.routing.Rule` that lazily compiles route builders.
- `routing_map` method is cached via `@tools.ormcache('key', cache='routing')`.

### D3 Source, technical and workflow logic
- `_auth_method_bearer` (line 212) validates API key via `res.users.apikeys._check_credentials(scope='rpc', key=token)` and checks Sec-Fetch headers for CSRF protection when no Bearer token.
- `_auth_method_user` (line 255) raises `SessionExpiredException` if uid is None or in public users list.
- `_authenticate_explicit` (line 276) calls `security.check_session` to validate session, then dispatches to the appropriate auth method.
- `_pre_dispatch` (line 298) reads `web.max_file_upload_size` from `ir.config_parameter`, updates language context, and pre-checks record access for model converter args.
- `routing_map` (line 385) builds the Werkzeug `Map` from all installed module routes; cached per routing key.
- `_serve_fallback` (line 371) serves static content from `ir.attachment` records.
- `_slugify_one` (line 143) converts strings to URL-safe slugs using python-slugify if available, otherwise Unicode normalisation + regex.
- `_slug` (line 182) returns `str(value.id)` for ORM records.
- `ModelConverter.to_python` (line 72) browses the ORM record using `_unslug` to extract the integer ID.
- `EXTENSION_TO_WEB_MIMETYPES` dict at line 45 maps file extensions to MIME types.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Abstract model | `models.AbstractModel` `ir_http.py:138-139` |
| D2 | Routing map cache | `@tools.ormcache('key', cache='routing')` `ir_http.py:384` |
| D3 | Bearer auth + CSRF | `_auth_method_bearer` `ir_http.py:212-252` |
| D4 | Session validation | `security.check_session` call `ir_http.py:279` |
| D5 | Pre-dispatch | file upload limit + lang context `ir_http.py:298-344` |
| D6 | Model URL converter | `ModelConverter.to_python` `ir_http.py:72-75` |
| D7 | Slug generation | `_slugify_one` Unicode normalisation `ir_http.py:143-163` |
| D8 | Attachment fallback | `_serve_fallback` via `ir.attachment` `ir_http.py:371-375` |
| D9 | Lazy rule compile | `FasterRule` subclass `ir_http.py:128-135` |
| D10 | MIME map | `EXTENSION_TO_WEB_MIMETYPES` `ir_http.py:45-53` |

---

## CAP-U50-05 — Outgoing Mail Server (ir.mail_server)

### D1 Business purpose and process semantics
`ir.mail_server` stores SMTP server configuration for outgoing email delivery. It supports login, certificate, and CLI authentication modes, and five encryption options (none, starttls, starttls_strict, ssl, ssl_strict). The `from_filter` field restricts which sender addresses/domains can use a given server. The system selects the best-matching server automatically when no explicit server ID is passed.

### D2 Architecture, data and object relationships
- `IrMail_Server` with `_order = 'sequence, id'`; lower sequence = higher priority.
- `smtp_authentication` selection: `login`, `certificate`, `cli`.
- `smtp_encryption` selection: five options; `starttls_strict` and `ssl_strict` validate the remote certificate.
- `smtp_ssl_certificate` and `smtp_ssl_private_key` binary fields stored in DB (not as attachments).
- `max_email_size` float field in megabytes; falls back to `base.default_max_email_size` config param (default 10 MB).

### D3 Source, technical and workflow logic
- `_connect__` (line 378) returns a live `smtplib.SMTP` or `smtplib.SMTP_SSL` object; returns `None` in test mode.
- Certificate auth (lines 430-451) uses `PyOpenSSLContext`; strict variants set `VERIFY_PEER | VERIFY_FAIL_IF_NO_PEER_CERT` with a custom hostname callback.
- `_find_mail_server` (line 859) applies a priority waterfall: (1) exact from-address match, (2) domain match, (3) notifications email match, (4) first server without filter, (5) CLI config.
- `_prepare_email_message__` (line 664) computes `smtp_from` considering bounce address and `notifications_email`; calls `_alter_message__` to clean up BCC, X-Forge-To, X-Msg-To-Add headers.
- `send_email` (line 784) opens SMTP connection if not pre-established, calls `smtp.send_message`, then quits unless `smtp_session` was provided by caller.
- `IdentificationFieldsNoFoldPolicy` class (line 62) prevents folding of `message-id`, `in-reply-to`, `references` headers to preserve thread tracking.
- `SMTP_TIMEOUT = 60` at line 45; applied to all `smtplib.SMTP` constructor calls.
- `_disable_send` (line 373) returns True during tests (`modules.module.current_test`) or registry init (`pool._init`).
- `_match_from_filter` (line 941) accepts full email or domain-only from-filter entries.
- Archive prevention in `write` (line 215): raises `UserError` if archiving a server that is still referenced.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model ordering | `_order = 'sequence, id'` `ir_mail_server.py:128` |
| D2 | Encryption options | five-value `smtp_encryption` selection `ir_mail_server.py:155-168` |
| D3 | Cert auth with verify | `PyOpenSSLContext` + `VERIFY_PEER` `ir_mail_server.py:432-437` |
| D4 | Test mode skip | `_disable_send` checks `current_test` `ir_mail_server.py:373-376` |
| D5 | Server selection waterfall | 5-step priority in `_find_mail_server` `ir_mail_server.py:859-933` |
| D6 | RFC header no-fold | `IdentificationFieldsNoFoldPolicy` `ir_mail_server.py:62-73` |
| D7 | SMTP timeout | `SMTP_TIMEOUT = 60` `ir_mail_server.py:45` |
| D8 | From-address rewrite | `encapsulate_email` call `ir_mail_server.py:696` |
| D9 | BCC cleanup | `del message['Bcc']` in `_alter_message__` `ir_mail_server.py:743` |
| D10 | Archive guard | `write` checks `_active_usages_compute` `ir_mail_server.py:215-248` |

---

## CAP-U50-06 — Saved Search Filters (ir.filters)

### D1 Business purpose and process semantics
`ir.filters` stores user-defined or shared search filter presets for any model. Filters capture a domain, sort order, and context. They can be private to specific users (via M2M `user_ids`) or visible to all users. Filters can be scoped to a specific menu action or to embedded actions with parent record IDs.

### D2 Architecture, data and object relationships
- `domain` and `context` stored as text (JSON-serialisable string).
- `sort` field stored as JSON array (validated by DB constraint `_check_sort_json`).
- `action_id` optional FK to `ir.actions.actions` for action-scoped filters.
- `embedded_action_id` FK to `ir.embedded.actions` for embedded view filters.
- `embedded_parent_res_id` integer stores the parent record ID; only valid when `embedded_action_id` is set (enforced by `_check_res_id_only_when_embedded_action` constraint).
- Composite index on `(model_id, action_id, embedded_action_id, embedded_parent_res_id)` at line 28.

### D3 Source, technical and workflow logic
- `get_filters` (line 99) returns filters visible to the current user: `user_ids in [uid, False]` with action domain.
- `_get_action_domain` (line 89) constructs the domain for action-scoped vs global filters.
- `_sanitize_shared_context` (line 43) strips `default_*` keys from context when a filter is shared with users other than the owner, using `clean_context` from `odoo.tools.misc`.
- `_get_eval_domain` (line 82) uses `ast.literal_eval` on the stored domain string.
- `model_id` field uses `selection='_list_all_models'` (not a M2O): executes raw SQL against `ir_model` to list all models in the current language.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'ir.filters'` `ir_filters.py:9` |
| D2 | Domain storage | `domain = fields.Text(default='[]')` `ir_filters.py:15` |
| D3 | Sort JSON constraint | `CHECK(sort IS NULL OR jsonb_typeof...)` `ir_filters.py:38-41` |
| D4 | Embedded res_id guard | `CHECK(NOT (embedded_parent_res_id...))` `ir_filters.py:34-37` |
| D5 | Context sanitisation | `_sanitize_shared_context` strips defaults `ir_filters.py:43-49` |
| D6 | Visibility query | `user_ids in [uid, False]` in `get_filters` `ir_filters.py:116-118` |
| D7 | Composite index | `(model_id, action_id, embedded_action_id, ...)` `ir_filters.py:28-30` |
| D8 | Domain eval | `ast.literal_eval(self.domain)` `ir_filters.py:84` |
| D9 | Model list | raw SQL against `ir_model` in `_list_all_models` `ir_filters.py:54-58` |
| D10 | Action domain | `_get_action_domain` three-part condition `ir_filters.py:89-96` |

---

## CAP-U50-07 — Export Templates (ir.exports)

### D1 Business purpose and process semantics
`ir.exports` and `ir.exports.line` store reusable field-selection templates for the data export wizard. A user can save a column list for a given model and reuse it across sessions.

### D2 Architecture, data and object relationships
- `ir.exports`: `name` (label), `resource` (model technical name, indexed).
- `ir.exports.line`: `name` (field path), `export_id` FK with cascade delete, `copy=True` on the relation.

### D3 Source, technical and workflow logic
- The models are purely declarative; no custom methods beyond ORM defaults.
- `export_fields` One2many with `copy=True` ensures field list is duplicated when record is duplicated.
- `resource` field is indexed for efficient lookup by model name.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'ir.exports'` `ir_exports.py:7` |
| D2 | Line model | `_name = 'ir.exports.line'` `ir_exports.py:17` |
| D3 | Resource index | `resource = fields.Char(index=True)` `ir_exports.py:13` |
| D4 | Copy on duplicate | `export_fields` with `copy=True` `ir_exports.py:14` |
| D5 | Cascade delete | `ondelete='cascade'` on `export_id` `ir_exports.py:23` |
| D6 | Line order | `_order = 'id'` `ir_exports.py:20` |
| D7 | No custom logic | file has no methods beyond field declarations (verified lines 1-24) |
| D8 | Field path storage | `name = fields.Char(string='Field Name')` `ir_exports.py:22` |
| D9 | Export name | `name = fields.Char(string='Export Name')` `ir_exports.py:12` |
| D10 | Minimal footprint | 24-line file with two pure models `ir_exports.py:1-24` |

---

## CAP-U50-08 — Profiling Records (ir.profile)

### D1 Business purpose and process semantics
`ir.profile` stores execution profiling sessions captured by the Odoo profiler (enabled via dev-mode or `/web/profile_config`). Records include SQL traces, async/sync execution traces, QWeb rendering data, and memory RSS measurements. Records are automatically purged after 30 days.

### D2 Architecture, data and object relationships
- `_log_access = False` (line 24): no `create_uid`/`write_uid` foreign key to `res.users`.
- Fields: `session`, `name`, `duration`, `cpu_duration`, `sql`, `sql_count`, `traces_async`, `traces_sync`, `qweb`, `others`, `entry_count`.
- `speedscope` binary computed field that serialises to Speedscope format.
- `speedscope_url` text field computed as a URL to open in browser.

### D3 Source, technical and workflow logic
- `_gc_profile` (line 52) is decorated `@api.autovacuum`; removes records older than 30 days; returns `(count, bool)` tuple indicating whether more records remain.
- `_has_memory_traces` (line 60) checks JSON in `traces_async` for `memory` key presence.
- `_get_memory_data` (line 70) returns baselined RSS memory points from `traces_async` JSON.
- `_compute_speedscope` (line 95) calls `_generate_speedscope` with parsed context params; base64-encodes the result.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | No log access | `_log_access = False` `ir_profile.py:24` |
| D2 | GC autovacuum | `@api.autovacuum` 30-day cleanup `ir_profile.py:52-58` |
| D3 | Memory traces | `_has_memory_traces` checks `traces_async` JSON `ir_profile.py:60-68` |
| D4 | Speedscope output | `_compute_speedscope` base64 encodes `ir_profile.py:95-100` |
| D5 | Config URL | `/web/profile_config/{id}` pattern `ir_profile.py:91-92` |
| D6 | Fields prefetch=False | `sql`, `traces_async`, etc. `ir_profile.py:38-44` |
| D7 | Session index | `session = fields.Char(index=True)` `ir_profile.py:31` |
| D8 | Duration fields | `duration`, `cpu_duration` with digits=(9,3) `ir_profile.py:32-35` |
| D9 | GC return tuple | returns `(len, len == GC_UNLINK_LIMIT)` `ir_profile.py:57-58` |
| D10 | Memory baseline | `baseline = mem` first entry `ir_profile.py:81-85` |

---

## CAP-U50-09 — Country and State Reference Data (res.country)

### D1 Business purpose and process semantics
`res.country` provides the canonical ISO 3166-1 country registry. Each country has a two-letter ISO code, optional phone code, associated currency, address format template, and optional custom address input view. Country groups allow geographic aggregations.

### D2 Architecture, data and object relationships
- `res.country` links to `res.currency` (currency_id) and `ir.ui.view` (address_view_id).
- `res.country.state` (One2many) stores subdivisions.
- `res.country.group` (Many2many) for groupings.
- Unique constraints on both `name` and `code`.
- `FLAG_MAPPING` dict (line 13) remaps non-standard territory codes to their flag country codes.
- `NO_FLAG_COUNTRIES` list (line 26) excludes Antarctica and Svalbard.

### D3 Source, technical and workflow logic
- `name_search` (line 90) prioritises exact ISO code (2-char) matching before name ilike search using `Domain` combining.
- `address_format` default (line 52) uses Python `%(key)s` substitution pattern for address rendering.
- `address_view_id` domain restricts to `res.partner` form views only.
- `country_group_codes` computed as JSON field.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'res.country'` `res_country.py:33` |
| D2 | ISO code size | `code = fields.Char(size=2)` `res_country.py:42` |
| D3 | Unique constraints | `_name_uniq` and `_code_uniq` `res_country.py:80-87` |
| D4 | Address format | `%(street)s` pattern default `res_country.py:52` |
| D5 | Code-first search | `name_search` checks 2-char code first `res_country.py:94-97` |
| D6 | Flag mapping | `FLAG_MAPPING` dict `res_country.py:13-24` |
| D7 | No-flag list | `NO_FLAG_COUNTRIES` `res_country.py:26-29` |
| D8 | Address view domain | restricted to `res.partner` form `res_country.py:53-58` |
| D9 | State required | `state_required = fields.Boolean(default=False)` `res_country.py:77` |
| D10 | VAT label | `vat_label = fields.Char(translate=True)` `res_country.py:75` |

---

## CAP-U50-10 — Currency and Exchange Rates (res.currency)

### D1 Business purpose and process semantics
`res.currency` stores ISO 4217 currencies. Each currency has a rounding factor that determines decimal places for amounts, a symbol with configurable position, and time-series exchange rates via `res.currency.rate`. The system automatically activates the `group_multi_currency` group when more than one active currency exists.

### D2 Architecture, data and object relationships
- `rate_ids` One2many to `res.currency.rate` (stores historical rates).
- `decimal_places` computed from `rounding` field.
- `_toggle_group_multi_currency` auto-enables/disables `base.group_multi_currency`.
- Unique constraint on `name`; rounding factor must be > 0.

### D3 Source, technical and workflow logic
- `_get_rates` (line 120) uses a CTE-based SQL query joining `res.currency.rate` with COALESCE fallback when no rate exists for the exact date.
- `_compute_current_rate` (line 148) is context-dependent on `to_currency`, `date`, `company`, `company_id`.
- `create`/`unlink`/`write` (lines 58-81) all clear the `stable` registry cache and call `_toggle_group_multi_currency`.
- `_check_company_currency_stays_active` constraint (line 108) prevents deactivating a currency that is set on a company; skipped during install or when `force_deactivate` context flag is set.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | ISO code field | `name = fields.Char(size=3)` `res_currency.py:27` |
| D2 | Rounding constraint | `CHECK (rounding>0)` `res_currency.py:53-56` |
| D3 | Multi-currency toggle | `_toggle_group_multi_currency` on create/write/unlink `res_currency.py:83-92` |
| D4 | Rate SQL query | COALESCE fallback in `_get_rates` `res_currency.py:130-138` |
| D5 | Rate context deps | `@api.depends_context('to_currency','date','company')` `res_currency.py:147` |
| D6 | Company currency guard | `_check_company_currency_stays_active` `res_currency.py:108-118` |
| D7 | Registry cache clear | `clear_cache('stable')` on all mutations `res_currency.py:63,70,77` |
| D8 | Symbol position | `position` selection `after`/`before` `res_currency.py:42-43` |
| D9 | Decimal places | computed from rounding `res_currency.py:39-40` |
| D10 | Numeric ISO code | `iso_numeric = fields.Integer` `res_currency.py:28` |

---

## CAP-U50-11 — Decimal Precision (decimal.precision)

### D1 Business purpose and process semantics
`decimal.precision` allows system administrators to configure the number of decimal places used for specific numeric applications (e.g., "Product Price", "Stock Weight"). It is a named configuration table; each application name must be unique. Reducing precision triggers an onchange warning because existing data is not backfilled.

### D2 Architecture, data and object relationships
- Simple model with `name` (usage key) and `digits` (integer, default 2).
- Unique constraint on `name`.
- `precision_get` is ORM-cached via `@tools.ormcache('application', cache='stable')`.

### D3 Source, technical and workflow logic
- `precision_get` (line 22) flushes the model then executes raw SQL to retrieve `digits`; returns 2 if not found.
- All mutations (create, write, unlink) call `self.env.registry.clear_cache('stable')` to invalidate the ormcache.
- `_onchange_digits_warning` (line 45) raises a UI warning when digits is reduced, noting that existing data is not updated.

### Ten-dimension table
| Dim | Dimension | Source evidence |
|-----|-----------|-----------------|
| D1 | Model identity | `_name = 'decimal.precision'` `decimal_precision.py:9` |
| D2 | Cached lookup | `@tools.ormcache('application', cache='stable')` `decimal_precision.py:22` |
| D3 | Raw SQL query | `SELECT digits FROM decimal_precision WHERE name=%s` `decimal_precision.py:25-26` |
| D4 | Default digits | returns `2` if not found `decimal_precision.py:27` |
| D5 | Cache invalidation | `clear_cache('stable')` in create/write/unlink `decimal_precision.py:31-43` |
| D6 | Unique name | `models.Constraint('unique (name)')` `decimal_precision.py:16-19` |
| D7 | Reduce warning | `_onchange_digits_warning` `decimal_precision.py:45-60` |
| D8 | Flush before query | `self.flush_model(['name', 'digits'])` `decimal_precision.py:24` |
| D9 | Default digits value | `default=2` on `digits` field `decimal_precision.py:14` |
| D10 | No backfill | warning text states existing data not updated `decimal_precision.py:52-60` |

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U50-C001 | module-states | `base/models/ir_module.py:140` | STATES = | FACT | always | — | Module state machine has exactly six states: uninstallable, uninstalled, installed, to upgrade, to remove, to install | N-U50-001 |
| VDR-U50-C002 | module-admin-guard | `base/models/ir_module.py:57` | `def assert_log_admin_access` | FACT | always | — | All module operations (install/upgrade/uninstall) are guarded by a decorator that raises AccessDenied if `env.is_admin()` is False | N-U50-002 |
| VDR-U50-C003 | module-admin-guard | `base/models/ir_module.py:68` | `if not self.env.is_admin():` | FACT | always | — | The guard logs a DENY warning with user login, user ID, and remote IP before raising AccessDenied | N-U50-002 |
| VDR-U50-C004 | module-install | `base/models/ir_module.py:408` | `def button_install(self):` | FACT | always | — | button_install triggers auto-install evaluation in a while loop until no more modules qualify | N-U50-003 |
| VDR-U50-C005 | module-install | `base/models/ir_module.py:418` | `def must_install(module):` | FACT | always | — | Auto-install requires all `auto_install_required` dependencies to be in install_states and at least one to be 'to install' | N-U50-003 |
| VDR-U50-C006 | module-install | `base/models/ir_module.py:421` | `not module.country_ids or module.country_ids & company_countries` | FACT | always | — | Country-specific modules auto-install only when at least one company belongs to one of the module's target countries | N-U50-003 |
| VDR-U50-C007 | module-install | `base/models/ir_module.py:431` | `if config.get('skip_auto_install'):` | FACT | config-dependent | — | A `skip_auto_install` config flag disables the auto-install loop | N-U50-003 |
| VDR-U50-C008 | module-exclusion | `base/models/ir_module.py:441` | `if exclusion.name in install_names:` | FACT | always | — | button_install raises UserError if any two modules being installed have declared mutual exclusions | N-U50-004 |
| VDR-U50-C009 | module-exclusion | `base/models/ir_module.py:458` | `exclusives = self.env['ir.module.category'].search` | FACT | always | — | Exclusive category check prevents installing two modules from the same exclusive category unless one is a dependency of the other | N-U50-004 |
| VDR-U50-C010 | module-state-recurse | `base/models/ir_module.py:378` | `def _state_update(self, newstate, states_to_update, level=100):` | FACT | always | — | _state_update recurses through dependency tree with a level counter; raises UserError at level < 1 to prevent infinite loops | N-U50-005 |
| VDR-U50-C011 | module-lock | `base/models/ir_module.py:619` | `self.env.cr.execute("LOCK ir_module_module IN EXCLUSIVE MODE")` | FACT | always | — | Immediate install/upgrade/uninstall acquires an EXCLUSIVE MODE table lock to prevent concurrent module operations | N-U50-006 |
| VDR-U50-C012 | module-lock | `base/models/ir_module.py:629` | `self.env.cr.execute("SELECT FROM ir_cron FOR UPDATE")` | FACT | always | — | Module operations also lock ir_cron to prevent conflicts with running scheduled actions | N-U50-006 |
| VDR-U50-C013 | module-lock | `base/models/ir_module.py:611` | `self.env.cr.execute("SET LOCAL lock_timeout = '3s'")` | FACT | always | — | A 3-second lock timeout is set before attempting the exclusive lock | N-U50-006 |
| VDR-U50-C014 | module-downstream | `base/models/ir_module.py:542` | `query = """ SELECT DISTINCT m.id` | FACT | always | — | downstream_dependencies uses a raw SQL recursive query joining ir_module_module_dependency | N-U50-005 |
| VDR-U50-C015 | module-uninstall | `base/models/ir_module.py:514` | `self.env['ir.model.data']._module_data_uninstall(modules_to_remove)` | FACT | always | — | Module uninstall delegates full DB cleanup to ir.model.data._module_data_uninstall | N-U50-007 |
| VDR-U50-C016 | module-update-list | `base/models/ir_module.py:797` | `for manifest in modules.Manifest.all_addon_manifests():` | FACT | always | — | update_list iterates all addon manifests on disk and creates or updates corresponding ir.module.module records | N-U50-008 |
| VDR-U50-C017 | module-version-check | `base/models/ir_module.py:809` | `if parse_version(terp.get('version', default_version)) > parse_version(mod.latest_version` | FACT | always | — | update_list increments the update counter when the disk version is greater than the installed version | N-U50-008 |
| VDR-U50-C018 | module-translations | `base/models/ir_module.py:976` | `translation_importer = TranslationImporter(self.env.cr, verbose=False)` | FACT | always | — | _load_module_terms loads PO files via TranslationImporter; also loads data file translations | N-U50-009 |
| VDR-U50-C019 | module-installed-cache | `base/models/ir_module.py:914` | `@tools.ormcache(cache='stable')` | FACT | always | — | _installed method returns a dict {name: id} of all installed modules, cached in the stable ORM cache | N-U50-008 |
| VDR-U50-C020 | view-arch-storage | `base/models/ir_ui_view.py:162` | `arch_db = fields.Text(string='Arch Blob', translate=xml_translate` | FACT | always | — | arch_db is the primary stored field for view XML using xml_translate for translation support | N-U50-010 |
| VDR-U50-C021 | view-arch-storage | `base/models/ir_ui_view.py:164` | `arch_fs = fields.Char(string='Arch Filename'` | FACT | always | — | arch_fs stores the relative module/path to the XML file; used in dev-xml mode to read arch directly from disk | N-U50-010 |
| VDR-U50-C022 | view-arch-compute | `base/models/ir_ui_view.py:224` | `read_file = self.env.context.get('read_arch_from_file') or` | FACT | always | — | _compute_arch reads from file when context has read_arch_from_file or dev_mode contains 'xml' AND arch_updated is False | N-U50-010 |
| VDR-U50-C023 | view-arch-inverse | `base/models/ir_ui_view.py:251` | `if 'install_filename' in self.env.context:` | FACT | always | — | When writing arch during module installation, arch_fs is set to the relative resource path | N-U50-010 |
| VDR-U50-C024 | view-inheritance-mode | `base/models/ir_ui_view.py:177` | `mode = fields.Selection([('primary', "Base view"), ('extension', "Extension View")]` | FACT | always | — | mode field controls whether a view with inherit_id is a primary (fully resolved) or extension view | N-U50-011 |
| VDR-U50-C025 | view-inheritance-tree | `base/models/ir_ui_view.py:742` | `WITH RECURSIVE ir_ui_view_inherits AS (` | FACT | always | — | _get_inheriting_views uses a PostgreSQL WITH RECURSIVE CTE to traverse the inheritance tree | N-U50-011 |
| VDR-U50-C026 | view-inheritance-order | `base/models/ir_ui_view.py:763` | `ORDER BY v.priority, v.id` | FACT | always | — | Inheriting views are applied in order of priority then database ID; studio views have priority=99 to load last | N-U50-011 |
| VDR-U50-C027 | view-group-check | `base/models/ir_ui_view.py:809` | `if set(self.group_ids.ids) & set(self.env.user._get_group_ids()):` | FACT | always | — | _check_view_access grants access when the user belongs to at least one of the view's groups | N-U50-012 |
| VDR-U50-C028 | view-group-check | `base/models/ir_ui_view.py:817` | `error = _("View '%(name)s' is private"` | FACT | always | — | A view with no group_ids raises AccessError as 'private' to any user attempting access | N-U50-012 |
| VDR-U50-C029 | view-extension-groups | `base/models/ir_ui_view.py:537` | @api.constrains('group_ids', 'inherit_id', 'mode') | FACT | always | — | Constraint _check_groups forbids group_ids on extension views; groups must be specified as arch attributes instead | N-U50-012 |
| VDR-U50-C030 | view-reset | `base/models/ir_ui_view.py:285` | `if mode == 'soft':` | FACT | always | — | Soft reset restores arch from arch_prev field; hard reset reads arch from arch_fs file | N-U50-013 |
| VDR-U50-C031 | view-validation | `base/models/ir_ui_view.py:493` | `if combined_arch.xpath('//*[@attrs]') or combined_arch.xpath('//*[@states]'):` | FACT | always | — | Since version 17.0, attrs and states attributes in views are no longer supported and raise ValidationError | N-U50-013 |
| VDR-U50-C032 | view-cycle | `base/models/ir_ui_view.py:545` | `def _check_000_inheritance(self):` | FACT | always | — | Constraint named with leading zeros to ensure it runs first alphabetically, preventing infinite loops in _get_combined_arch | N-U50-011 |
| VDR-U50-C033 | view-qweb-key | `base/models/ir_ui_view.py:556` | `"CHECK (type != 'qweb' OR key IS NOT NULL)"` | FACT | always | — | DB constraint requires that all qweb-type views have a non-null key field | N-U50-011 |
| VDR-U50-C034 | view-custom | `base/models/ir_ui_view.py:66` | `_name = 'ir.ui.view.custom'` | FACT | always | — | ir.ui.view.custom stores per-user architecture customizations linked to a base view | N-U50-013 |
| VDR-U50-C035 | view-modifiers | `base/models/ir_ui_view.py:34` | `VIEW_MODIFIERS = ('column_invisible', 'invisible', 'readonly', 'required')` | FACT | always | — | Four recognized view modifier attributes defined as a module-level constant | N-U50-013 |
| VDR-U50-C036 | qweb-compile-cache | `base/models/ir_qweb.py:43` | function is only | FACT | always | — | QWeb compiled functions are ORM-cached; compile cost is amortised across renderings | N-U50-014 |
| VDR-U50-C037 | qweb-markup | `base/models/ir_qweb.py:50` | page. | FACT | always | — | All QWeb rendering output is MarkupSafe-escaped, preventing XSS from untrusted input | N-U50-014 |
| VDR-U50-C038 | qweb-directives | `base/models/ir_qweb.py:80` | ┃  ┃    ┗━► t-foreach | FACT | always | — | Directive processing order is controlled by _directives_eval_order; t-groups, t-foreach and t-if have defined ordering | N-U50-015 |
| VDR-U50-C039 | qweb-foreach | `base/models/ir_qweb.py:200` | `these are (``*_value``, ``*_index``, ``*_size``,` | FACT | always | — | t-foreach injects six loop variables into the values dict: *_value, *_index, *_size, *_first, *_last | N-U50-015 |
| VDR-U50-C040 | qweb-groups | `base/models/ir_qweb.py:186` | ``t-groups`` (``groups`` is an alias) | FACT | always | — | t-groups directive generates code that calls has_group at render time; groups prefixed with ! are prohibited groups | N-U50-015 |
| VDR-U50-C041 | qweb-t-call | `base/models/ir_qweb.py:239` | `Serves the called template in place of the current ``t-call`` node.` | FACT | always | — | t-call copies values dict, renders inner content to slot '0', then compiles and executes the target template | N-U50-015 |
| VDR-U50-C042 | qweb-t-out | `base/models/ir_qweb.py:282` | `Output the given value or if falsy, display the content as default value.` | FACT | always | — | t-out outputs MarkupSafe value; node content is used as default when expression is falsy | N-U50-015 |
| VDR-U50-C043 | qweb-deprecated | `base/models/ir_qweb.py:305` | Deprecated, please use ``t-out`` | FACT | always | — | Both t-esc and t-raw are deprecated in favour of t-out | N-U50-015 |
| VDR-U50-C044 | qweb-safe-opcodes | `base/models/ir_qweb.py:423` | `_SAFE_QWEB_OPCODES = _EXPR_OPCODES.union(to_opcodes([` | FACT | always | — | Compiled QWeb expressions are validated against a whitelist of Python bytecodes to prevent code injection | N-U50-016 |
| VDR-U50-C045 | qweb-xss | `base/models/ir_qweb.py:491` | `MALICIOUS_SCHEMES = re.compile(r'javascript:(?!((window\.)?)history\.back\(\)$)'` | FACT | always | — | A regex blocks javascript: URL schemes except history.back() usage | N-U50-016 |
| VDR-U50-C046 | qweb-void-elements | `base/models/ir_qweb.py:472` | `VOID_ELEMENTS = frozenset([` | FACT | always | — | Self-closing HTML elements (area, base, br, etc.) are tracked so QWeb does not emit closing tags for them | N-U50-015 |
| VDR-U50-C047 | qweb-assets | `base/models/ir_qweb.py:273` | `The generated code call the ``_get_asset_nodes`` method` | FACT | always | — | t-call-assets generates asset tags by calling _get_asset_nodes; integrates with AssetsBundle | N-U50-017 |
| VDR-U50-C048 | qweb-t-set | `base/models/ir_qweb.py:312` | `The generated code update the key ``values`` dictionary equal to the value` | FACT | always | — | t-set updates a key in the values dict using t-value expression, t-valuef format string, or rendered node content | N-U50-015 |
| VDR-U50-C049 | http-abstract | `base/models/ir_http.py:138` | `class IrHttp(models.AbstractModel):` | FACT | always | — | ir.http is defined as AbstractModel; it provides no database table | N-U50-018 |
| VDR-U50-C050 | http-routing-cache | `base/models/ir_http.py:384` | `@tools.ormcache('key', cache='routing')` | FACT | always | — | routing_map is ORM-cached in the 'routing' cache, keyed by a key string | N-U50-018 |
| VDR-U50-C051 | http-bearer | `base/models/ir_http.py:212` | `def _auth_method_bearer(cls):` | FACT | always | — | Bearer authentication validates the token via res.users.apikeys._check_credentials with scope='rpc' | N-U50-019 |
| VDR-U50-C052 | http-bearer-csrf | `base/models/ir_http.py:223` | `def check_sec_headers():` | FACT | always | — | When no Bearer token, browser-based requests are protected by checking Sec-Fetch-Dest, Sec-Fetch-Mode, Sec-Fetch-Site, Sec-Fetch-User headers | N-U50-019 |
| VDR-U50-C053 | http-bearer-stateless | `base/models/ir_http.py:245` | `request.session.can_save = False  # stateless` | FACT | always | — | When authenticating via Bearer API key, the session is marked cannot-save (stateless mode) | N-U50-019 |
| VDR-U50-C054 | http-auth-user | `base/models/ir_http.py:256` | `if request.env.uid in [None] + cls._get_public_users():` | FACT | always | — | _auth_method_user raises SessionExpiredException if uid is None or belongs to the public user list | N-U50-019 |
| VDR-U50-C055 | http-session-check | `base/models/ir_http.py:279` | `if not security.check_session(request.session, request.env, request):` | FACT | always | — | _authenticate_explicit validates the session via security.check_session before dispatching to the auth method | N-U50-019 |
| VDR-U50-C056 | http-upload-limit | `base/models/ir_http.py:306` | `key = 'web.max_file_upload_size'` | FACT | always | — | Pre-dispatch reads web.max_file_upload_size ICP and applies it as the request upload limit | N-U50-018 |
| VDR-U50-C057 | http-lang-context | `base/models/ir_http.py:320` | `request.update_context(lang=get_lang(env).code)` | FACT | always | — | Pre-dispatch updates the request context with the validated language code | N-U50-018 |
| VDR-U50-C058 | http-access-check | `base/models/ir_http.py:336` | `args[key].check_access('read')` | FACT | always | — | Pre-dispatch calls check_access('read') on all ORM model converter arguments before invoking the endpoint | N-U50-018 |
| VDR-U50-C059 | http-fallback | `base/models/ir_http.py:371` | `attach = model.sudo()._get_serve_attachment(request.httprequest.path)` | FACT | always | — | _serve_fallback looks up ir.attachment by request path to serve static binary assets | N-U50-018 |
| VDR-U50-C060 | http-slug | `base/models/ir_http.py:182` | def _slug | FACT | always | — | _slug returns str(value.id) for ORM records; integer ID only, no name included by default | N-U50-018 |
| VDR-U50-C061 | http-model-converter | `base/models/ir_http.py:72` | `def to_python(self, value: str) -> models.BaseModel:` | FACT | always | — | ModelConverter.to_python browses the ORM record from URL integer ID using a placeholder uid (RequestUID) | N-U50-018 |
| VDR-U50-C062 | http-lazy-rule | `base/models/ir_http.py:128` | `class FasterRule(werkzeug.routing.Rule):` | FACT | always | — | FasterRule makes _compile_builder lazy to speed up routing map generation | N-U50-018 |
| VDR-U50-C063 | smtp-model-order | `base/models/ir_mail_server.py:128` | `_order = 'sequence, id'` | FACT | always | — | Mail servers are ordered by sequence (ascending), with lower sequence meaning higher priority | N-U50-020 |
| VDR-U50-C064 | smtp-auth-modes | `base/models/ir_mail_server.py:147` | smtp_authentication = fields.Selection | FACT | always | — | Three authentication modes: login (username/password), certificate (SSL client cert), cli (command-line config) | N-U50-020 |
| VDR-U50-C065 | smtp-encryption | `base/models/ir_mail_server.py:155` | smtp_encryption | FACT | always | — | Five encryption options including strict variants that validate server certificate | N-U50-020 |
| VDR-U50-C066 | smtp-cert-auth | `base/models/ir_mail_server.py:432` | ssl_context._ctx.set_verify | FACT | always | — | ssl_strict and starttls_strict modes use PyOpenSSL VERIFY_PEER with a custom hostname verification callback | N-U50-020 |
| VDR-U50-C067 | smtp-test-disable | `base/models/ir_mail_server.py:373` | `return modules.module.current_test or cls.pool._init` | FACT | always | — | _disable_send returns True during automated tests and during registry initialisation | N-U50-021 |
| VDR-U50-C068 | smtp-timeout | `base/models/ir_mail_server.py:45` | `SMTP_TIMEOUT = 60` | FACT | always | — | All SMTP connections use a 60-second socket timeout | N-U50-020 |
| VDR-U50-C069 | smtp-server-select | `base/models/ir_mail_server.py:887` | `if mail_server := first_match(email_from_normalized, email_normalize):` | FACT | always | — | Server selection waterfall: exact address match → domain match → notifications email → first without filter → CLI config | N-U50-022 |
| VDR-U50-C070 | smtp-from-rewrite | `base/models/ir_mail_server.py:696` | `smtp_from = encapsulate_email(message['From'], notifications_email)` | FACT | always | — | When smtp_from equals the notifications email but the From header differs, the original From is encapsulated to avoid spoofing | N-U50-022 |
| VDR-U50-C071 | smtp-no-fold | `base/models/ir_mail_server.py:62` | `class IdentificationFieldsNoFoldPolicy(email.policy.EmailPolicy):` | FACT | always | — | Custom email policy prevents line-folding of message-id, in-reply-to and references headers | N-U50-022 |
| VDR-U50-C072 | smtp-bcc-cleanup | `base/models/ir_mail_server.py:743` | `del message['Bcc']` | FACT | always | — | BCC header is deleted before sending to prevent blind recipients appearing in message headers | N-U50-022 |
| VDR-U50-C073 | smtp-bounce | `base/models/ir_mail_server.py:680` | `bounce_address = self.env.context.get('domain_bounce_address') or message['Return-Path']` | FACT | always | — | Bounce address is taken from context, then Return-Path header, then default bounce address, then From | N-U50-022 |
| VDR-U50-C074 | smtp-max-size | `base/models/ir_mail_server.py:260` | `return float(self.env['ir.config_parameter'].sudo().get_param('base.default_max_email_size', '10'))` | FACT | always | — | Default max email size is 10 MB from config param base.default_max_email_size | N-U50-020 |
| VDR-U50-C075 | smtp-archive-guard | `base/models/ir_mail_server.py:215` | `if not vals.get('active', True):` | FACT | always | — | Archiving a mail server raises UserError if it is still referenced by other records | N-U50-020 |
| VDR-U50-C076 | smtp-html-alt | `base/models/ir_mail_server.py:610` | `if subtype == 'html' and not body_alternative:` | FACT | always | — | HTML emails automatically get a plaintext alternative generated via html2plaintext | N-U50-022 |
| VDR-U50-C077 | filters-domain-text | `base/models/ir_filters.py:15` | `domain = fields.Text(default='[]', required=True)` | FACT | always | — | Filter domain is stored as a text JSON-serialisable string, default is empty list | N-U50-023 |
| VDR-U50-C078 | filters-user-share | `base/models/ir_filters.py:14` | user_ids = fields.Many2many | FACT | always | — | Empty user_ids means filter is shared with all users; non-empty restricts to specific users | N-U50-023 |
| VDR-U50-C079 | filters-sort-json | `base/models/ir_filters.py:38` | `"CHECK(sort IS NULL OR jsonb_typeof(sort::jsonb) = 'array')"` | FACT | always | — | sort field is validated at DB level as a JSON array | N-U50-023 |
| VDR-U50-C080 | filters-context-sanitize | `base/models/ir_filters.py:43` | `def _sanitize_shared_context(self):` | FACT | always | — | When a filter is shared, default_* context keys are stripped to prevent exposing per-user defaults to other users | N-U50-023 |
| VDR-U50-C081 | filters-action-domain | `base/models/ir_filters.py:89` | `def _get_action_domain(self, action_id=None` | FACT | always | — | get_filters scopes visibility to action (action_id), embedded action, and embedded parent record ID | N-U50-023 |
| VDR-U50-C082 | filters-model-select | `base/models/ir_filters.py:52` | `def _list_all_models(self):` | FACT | always | — | model_id uses a dynamic selection populated by raw SQL against ir_model, returning models in current language | N-U50-023 |
| VDR-U50-C083 | filters-index | `base/models/ir_filters.py:28` | _get_filters_index = models.Index | FACT | always | — | Composite B-tree index on four filter-lookup columns | N-U50-023 |
| VDR-U50-C084 | filters-res-id-constraint | `base/models/ir_filters.py:34` | `'CHECK(NOT (embedded_parent_res_id IS NOT NULL AND embedded_action_id IS NULL))'` | FACT | always | — | DB constraint ensures embedded_parent_res_id can only be set when embedded_action_id is also set | N-U50-023 |
| VDR-U50-C085 | filters-visibility | `base/models/ir_filters.py:116` | `action_domain + [('model_id', '=', model), ('user_ids', 'in', [self.env.uid, False])]` | FACT | always | — | get_filters combines action domain with user visibility: private (uid) or global (False) | N-U50-023 |
| VDR-U50-C086 | exports-simple | `base/models/ir_exports.py:7` | `_name = 'ir.exports'` | FACT | always | — | ir.exports is a minimal declarative model with name and resource fields only | N-U50-024 |
| VDR-U50-C087 | exports-resource-index | `base/models/ir_exports.py:13` | `resource = fields.Char(index=True)` | FACT | always | — | resource field (model technical name) is indexed for fast lookup | N-U50-024 |
| VDR-U50-C088 | exports-copy | `base/models/ir_exports.py:14` | export_fields = | FACT | always | — | Lines are deep-copied when duplicating an export template | N-U50-024 |
| VDR-U50-C089 | profile-no-log-access | `base/models/ir_profile.py:24` | `_log_access = False` | FACT | always | — | ir.profile disables standard create_uid/write_uid foreign key to avoid loading res.users | N-U50-025 |
| VDR-U50-C090 | profile-autovacuum | `base/models/ir_profile.py:52` | `@api.autovacuum` | FACT | always | — | _gc_profile is called automatically by the autovacuum cron and removes profiles older than 30 days | N-U50-025 |
| VDR-U50-C091 | profile-gc-limit | `base/models/ir_profile.py:56` | `records = self.sudo().search(domain, limit=GC_UNLINK_LIMIT)` | FACT | always | — | Autovacuum uses GC_UNLINK_LIMIT to batch deletions; returns True if more records remain | N-U50-025 |
| VDR-U50-C092 | profile-speedscope | `base/models/ir_profile.py:95` | `def _compute_speedscope(self):` | FACT | always | — | ir.profile can export to Speedscope format via _generate_speedscope method | N-U50-025 |
| VDR-U50-C093 | country-iso-code | `base/models/res_country.py:42` | required=True | FACT | always | — | Country code is exactly 2 characters (ISO 3166-1 alpha-2) | N-U50-026 |
| VDR-U50-C094 | country-name-search | `base/models/res_country.py:94` | `if not operator in Domain.NEGATIVE_OPERATORS and name and len(name) == 2:` | FACT | always | — | name_search tries exact 2-character code lookup first before falling back to name ilike | N-U50-026 |
| VDR-U50-C095 | country-address-format | `base/models/res_country.py:52` | `default='%(street)s\n%(street2)s\n%(city)s %(state_code)s %(zip)s\n%(country_name)s'` | FACT | always | — | Default address format uses Python %(key)s substitution with named fields | N-U50-026 |
| VDR-U50-C096 | country-flag-map | `base/models/res_country.py:13` | FLAG_MAPPING = | FACT | always | — | Overseas territories without their own flag are mapped to their administrative country's flag | N-U50-026 |
| VDR-U50-C097 | country-address-view | `base/models/res_country.py:53` | address_view_id = fields.Many2one | FACT | always | — | address_view_id allows a country to override the standard address input form for res.partner | N-U50-026 |
| VDR-U50-C098 | currency-iso3 | `base/models/res_currency.py:27` | `name = fields.Char(string='Currency', size=3` | FACT | always | — | Currency name field holds the 3-character ISO 4217 code | N-U50-027 |
| VDR-U50-C099 | currency-rounding | `base/models/res_currency.py:53` | `'CHECK (rounding>0)'` | FACT | always | — | DB constraint requires rounding factor > 0 | N-U50-027 |
| VDR-U50-C100 | currency-multi-toggle | `base/models/res_currency.py:83` | `def _toggle_group_multi_currency(self):` | FACT | always | — | Multi-currency group is auto-enabled when more than 1 active currency exists, disabled otherwise | N-U50-027 |
| VDR-U50-C101 | currency-rate-sql | `base/models/res_currency.py:130` | rate_query.add_where | FACT | always | — | Exchange rate lookup falls back through: exact-date rate, oldest-date rate, then 1.0 | N-U50-027 |
| VDR-U50-C102 | currency-company-guard | `base/models/res_currency.py:117` | `if self.env['res.company'].search_count([('currency_id', 'in', currencies.ids)], limit=1):` | FACT | always | — | Deactivating a currency used by any company raises UserError | N-U50-027 |
| VDR-U50-C103 | currency-stable-cache | `base/models/res_currency.py:63` | `self.env.registry.clear_cache('stable')` | FACT | always | — | All currency mutations clear the stable registry cache | N-U50-027 |
| VDR-U50-C104 | dp-ormcache | `base/models/decimal_precision.py:22` | `@tools.ormcache('application', cache='stable')` | FACT | always | — | precision_get is ORM-cached per application name in the stable cache | N-U50-028 |
| VDR-U50-C105 | dp-raw-sql | `base/models/decimal_precision.py:25` | `self.env.cr.execute('select digits from decimal_precision where name=%s', (application,))` | FACT | always | — | precision_get uses raw SQL to retrieve digits after flushing the model | N-U50-028 |
| VDR-U50-C106 | dp-default | `base/models/decimal_precision.py:27` | `return res[0] if res else 2` | FACT | always | — | precision_get returns 2 as default when no record exists for the application name | N-U50-028 |
| VDR-U50-C107 | dp-cache-inval | `base/models/decimal_precision.py:31` | `self.env.registry.clear_cache('stable')` | FACT | always | — | create, write, unlink all clear the stable cache to invalidate precision_get results | N-U50-028 |
| VDR-U50-C108 | dp-reduce-warning | `base/models/decimal_precision.py:47` | `if self.digits < self._origin.digits:` | FACT | always | — | Reducing decimal precision triggers an onchange warning noting existing data is not backfilled | N-U50-028 |
| VDR-U50-C109 | view-priority-default | `base/models/ir_ui_view.py:148` | `priority = fields.Integer(string='Sequence', default=16` | FACT | always | — | View priority defaults to 16; lower value means the view is combined earlier | N-U50-011 |
| VDR-U50-C110 | view-key-index | `base/models/ir_ui_view.py:147` | `key = fields.Char(index='btree_not_null')` | FACT | always | — | key field uses btree_not_null index type, indexing only non-null values | N-U50-011 |
| VDR-U50-C111 | module-category | `base/models/ir_module.py:77` | `_name = 'ir.module.category'` | FACT | always | — | ir.module.category provides hierarchical module groupings with optional exclusive flag | N-U50-001 |
| VDR-U50-C112 | module-category-exclusive | `base/models/ir_module.py:459` | `exclusives = self.env['ir.module.category'].search([('exclusive', '=', True)])` | FACT | always | — | Exclusive categories prevent installing more than one module from the category unless one depends on the other | N-U50-004 |
| VDR-U50-C113 | module-allow-sudo | `base/models/ir_module.py:163` | `_allow_sudo_commands = False` | FACT | always | — | ir.module.module sets _allow_sudo_commands = False | N-U50-001 |
| VDR-U50-C114 | smtp-cert-check | `base/models/ir_mail_server.py:206` | `def _check_smtp_ssl_files(self):` | FACT | always | — | Constraint verifies both ssl_certificate and ssl_private_key are present when authentication is 'certificate' | N-U50-020 |
| VDR-U50-C115 | smtp-cert-db-storage | `base/models/ir_mail_server.py:169` | smtp_ssl_certificate = fields.Binary | FACT | always | — | SSL certificate and private key are stored in the database (attachment=False), not as ir.attachment records | N-U50-020 |
| VDR-U50-C116 | smtp-send-flow | `base/models/ir_mail_server.py:820` | smtp = smtp_session | FACT | always | — | send_email opens connection, prepares message, calls smtp.send_message, then quits (unless session was pre-established) | N-U50-022 |
| VDR-U50-C117 | http-public-auth | `base/models/ir_http.py:265` | `def _auth_method_public(cls):` | FACT | always | — | _auth_method_public sets uid to base.public_user when uid is None, allowing anonymous access | N-U50-019 |
| VDR-U50-C118 | http-none-auth | `base/models/ir_http.py:259` | `def _auth_method_none(cls):` | FACT | always | — | _auth_method_none sets uid to None in the environment, allowing completely unauthenticated access | N-U50-019 |
| VDR-U50-C119 | view-model-index | `base/models/ir_ui_view.py:146` | `model = fields.Char(index=True)` | FACT | always | — | model field is indexed for efficient view lookup by model name | N-U50-010 |
| VDR-U50-C120 | view-inherited-children | `base/models/ir_ui_view.py:170` | `inherit_children_ids = fields.One2many('ir.ui.view', 'inherit_id'` | FACT | always | — | inherit_children_ids provides the inverse of inherit_id, listing all direct child views | N-U50-011 |
| VDR-U50-C121 | module-dep-auto-install | `base/models/ir_module.py:838` | `self.env.cr.execute('UPDATE ir_module_module_dependency SET auto_install_required = (name = any(%s)) WHERE module_id = %s'` | FACT | always | — | _update_dependencies sets auto_install_required flag on individual dependency rows | N-U50-003 |
| VDR-U50-C122 | module-countries | `base/models/ir_module.py:297` | `country_ids = fields.Many2many('res.country', 'module_country', 'module_id', 'country_id')` | FACT | always | — | Modules can be restricted to specific countries via country_ids M2M | N-U50-001 |
| VDR-U50-C123 | smtp-from-filter-parse | `base/models/ir_mail_server.py:961` | `def _parse_from_filter(self, from_filter):` | FACT | always | — | from_filter is comma-separated; _parse_from_filter splits and strips whitespace from each entry | N-U50-020 |
| VDR-U50-C124 | smtp-conn-ehlo | `base/models/ir_mail_server.py:521` | `connection.ehlo_or_helo_if_needed()` | FACT | always | — | After authentication, ehlo_or_helo_if_needed is called to ensure EHLO/HELO has been sent | N-U50-020 |
| VDR-U50-C125 | filters-get-filters | `base/models/ir_filters.py:99` | `def get_filters(self, model, action_id=None` | FACT | always | — | get_filters applies user_context from res.users.context_get before searching | N-U50-023 |
| VDR-U50-C126 | http-dispatch-captcha | `base/models/ir_http.py:350` | `captcha = endpoint.routing.get('captcha')` | FACT | always | — | _dispatch checks for a captcha requirement on the endpoint routing dict before calling the handler | N-U50-018 |
| VDR-U50-C127 | view-create-type-detect | `base/models/ir_ui_view.py:608` | `values['type'] = etree.fromstring(values.get('arch') or values.get('arch_base')).tag` | FACT | always | — | When no type is specified, view type is inferred from the root XML tag of the arch | N-U50-010 |
| VDR-U50-C128 | view-qweb-key-gen | `base/models/ir_ui_view.py:621` | `values['key'] = "gen_key.%s" % str(uuid.uuid4())[:6]` | FACT | always | — | QWeb views without an explicit key get an auto-generated key based on a UUID prefix | N-U50-011 |
| VDR-U50-C129 | view-write-custom-drop | `base/models/ir_ui_view.py:652` | `custom_view = self.env['ir.ui.view.custom'].sudo().search([('ref_id', 'in', self.ids)])` | FACT | always | — | When a base view is modified, all per-user custom versions of that view are deleted | N-U50-013 |
| VDR-U50-C130 | view-cache-invalidate | `base/models/ir_ui_view.py:639` | `self.env.registry.clear_cache('templates')` | FACT | always | — | create and write and unlink all clear the 'templates' registry cache | N-U50-013 |
| VDR-U50-C131 | module-button-immediate | `base/models/ir_module.py:484` | _logger.info('User | FACT | always | — | button_immediate_install passes allowed_company_ids to the request to support chart-of-accounts installation in the correct company | N-U50-006 |
| VDR-U50-C132 | module-next-action | `base/models/ir_module.py:582` | `def next(self):` | FACT | always | — | After module operations, next() looks for open ir.actions.todo records and executes them, or redirects to /odoo | N-U50-006 |
| VDR-U50-C133 | qweb-t-lang | `base/models/ir_qweb.py:258` | ``t-lang`` | FACT | always | — | t-lang directive combined with t-call renders the target template in a different language context | N-U50-015 |
| VDR-U50-C134 | smtp-skip-to | `base/models/ir_mail_server.py:768` | `skip_to_lst = self.env.context.get('send_smtp_skip_to') or []` | FACT | always | — | send_smtp_skip_to context key provides a blocklist of recipient addresses to exclude from SMTP TO | N-U50-022 |
| VDR-U50-C135 | smtp-validated-to | `base/models/ir_mail_server.py:765` | `validated_to = self.env.context.get('send_validated_to') or []` | FACT | always | — | send_validated_to context key restricts SMTP TO to a pre-validated list of addresses | N-U50-022 |
| VDR-U50-C136 | currency-install-mode | `base/models/res_currency.py:110` | `if self.env.context.get('install_mode') or self.env.context.get('force_deactivate'):` | FACT | always | — | Company currency deactivation check is skipped during installation mode and with force_deactivate context flag | N-U50-027 |
| VDR-U50-C137 | view-invalid-locators | `base/models/ir_ui_view.py:205` | `invalid_locators = fields.Json(compute='_compute_invalid_locators')` | FACT | always | — | invalid_locators computed JSON field identifies xpath/field specs that cannot be anchored in the parent view | N-U50-011 |
| VDR-U50-C138 | module-info-field-names | `base/models/ir_module.py:285` | `# attention: Incorrect field names !!` | FACT | always | — | Documented inconsistency: installed_version stores disk version, latest_version stores DB version (inverted naming convention) | N-U50-008 |
| VDR-U50-C139 | filters-embedded-copy | `base/models/ir_filters.py:60` | `def copy_data(self, default=None):` | FACT | always | — | copy_data removes embedded_parent_res_id=0 from copied values to avoid triggering the embedded constraint | N-U50-023 |
| VDR-U50-C140 | http-cors-bypass | `base/models/ir_http.py:272` | `auth = 'none' if http.is_cors_preflight(request, endpoint) else endpoint.routing['auth']` | FACT | always | — | CORS preflight requests bypass endpoint authentication (forced to auth='none') | N-U50-019 |
| VDR-U50-C141 | module-views-compute | `base/models/ir_module.py:218` | `def _get_views(self):` | FACT | always | — | views_by_module, reports_by_module, menus_by_module are computed from ir.model.data for installed modules | N-U50-001 |
| VDR-U50-C142 | smtp-from-filter-doc | `base/models/ir_mail_server.py:141` | from_filter = fields.Char | FACT | always | — | from_filter accepts comma-separated full email addresses or domain names | N-U50-020 |
| VDR-U50-C143 | view-compute-defaults | `base/models/ir_ui_view.py:562` | `def _compute_defaults(self, values):` | FACT | always | — | _compute_defaults auto-sets mode to 'extension' when inherit_id is provided and view has no existing inherit_id | N-U50-011 |
| VDR-U50-C144 | view-arch-prev | `base/models/ir_ui_view.py:657` | `vals['arch_prev'] = self.arch_db` | FACT | always | — | On write, the current arch_db is saved to arch_prev before overwriting, enabling soft reset | N-U50-013 |
| VDR-U50-C145 | module-test-block | `base/models/ir_module.py:603` | `if modules.module.current_test:` | FACT | always | — | button_immediate_function raises RuntimeError if called during tests to prevent non-transactional module operations | N-U50-006 |
| VDR-U50-C146 | smtp-idna | `base/models/ir_mail_server.py:514` | `smtp_user = local + at + idna.encode(domain).decode('ascii')` | FACT | always | — | SMTP usernames with international domain names are IDNA-encoded before authentication | N-U50-020 |
| VDR-U50-C147 | smtp-conn-store | `base/models/ir_mail_server.py:525` | `connection.from_filter = from_filter` | FACT | always | — | The SMTP connection object has from_filter and smtp_from stored as instance attributes for later use in _prepare_email_message__ | N-U50-020 |
| VDR-U50-C148 | view-warning-info | `base/models/ir_ui_view.py:190` | `warning_info = fields.Html(string="Warning information", compute='_compute_warning_info')` | FACT | always | — | warning_info is a computed HTML field that surfaces view validation errors to the UI without blocking saves | N-U50-013 |
| VDR-U50-C149 | http-routing-options | `base/models/ir_http.py:397` | `routing['methods'] = [*routing['methods'], 'OPTIONS']` | FACT | always | — | OPTIONS method is automatically added to every route's allowed methods list for CORS preflight support | N-U50-018 |
| VDR-U50-C150 | dp-unique | `base/models/decimal_precision.py:16` | _name_uniq = models.Constraint | FACT | always | — | decimal.precision enforces unique application names; only one precision value per usage key | N-U50-028 |
| VDR-U50-C151 | profile-memory-baseline | `base/models/ir_profile.py:81` | `if baseline is None:` | FACT | always | — | Memory data is baselined to the first recorded RSS value so charts show relative memory usage | N-U50-025 |
| VDR-U50-C152 | smtp-debug-log | `base/models/ir_mail_server.py:54` | `smtplib.SMTP._print_debug = _print_debug` | FACT | always | — | smtplib's internal debug printer is monkey-patched to route through Python logging at DEBUG level | N-U50-020 |
| VDR-U50-C153 | module-reg-clear | `base/models/ir_module.py:344` | `self.env.registry.clear_cache('stable')` | FACT | always | — | Module record unlink clears the stable registry cache | N-U50-001 |
| VDR-U50-C154 | module-to-install-check | `base/models/ir_module.py:614` | `if self.search_count([('state', 'in', ('to install', 'to upgrade', 'to remove'))], limit=1):` | FACT | always | — | _button_immediate_function raises UserError if any module operation is already in progress | N-U50-006 |
| VDR-U50-C155 | http-signed-int | `base/models/ir_http.py:97` | `class SignedIntConverter(NumberConverter):` | FACT | always | — | A custom Werkzeug converter for signed integers (including negative) is registered | N-U50-018 |
