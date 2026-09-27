# G01 PLATFORM_BASE — Lane A Pass-1 — `base`

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T4 (refill) |
| Group | G01 PLATFORM_BASE |
| Module | `base` (exact governed roster member) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, path `odoo/addons/base/` |
| Retrieval | raw.githubusercontent.com at anchor commit; blob SHA-1 via `git hash-object` on local copies |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (breadth pass; ORM core under `odoo/orm`/`odoo/api.py`/`odoo/http.py` is outside the module path and not read — see Gaps) |

Clean-room note: neutral WHAT / WHY / RISK abstractions only. Identifiers are pointers, not copy recommendations. Source presence does not prove runtime reachability. No QIDs answered. No Formal Coverage or percentage claims.

## 0. Carried-forward evidence (R14, not re-studied)

Pointer: `../G01_G04_RED_TEAM_STATIC_CHECKPOINT_R14_20260925.md` (lines 31-34).

| Path (under odoo/addons/base/) | git blob SHA-1 | Status |
|---|---|---|
| `models/ir_attachment.py` | 905ae118b8c8e5050fdc33eb1631c88e3926b888 | carried forward by pointer |
| `models/ir_sequence.py` | 920e0b2347f850b60c1bf8b392f82a2c7f964272 | carried forward by pointer |
| `models/res_currency.py` | 015ca78353c734949545d4364f500d4d57f32d9f | carried forward by pointer |
| `models/res_lang.py` | 563b4eff214fbd9940661b9f76ee3a3aa571c76c | carried forward by pointer |

## 1. Evidence Pointer Table (new this pass)

| # | Path (under odoo/addons/base/) | git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | `__manifest__.py` | 5250c85200522dd16459e5b845a8017bb958a1c1 | Identity, data load order, demo, licence, hooks |
| E2 | `models/__init__.py` | d748881f7eea3eae1e8b8b89d2bc90d4f9e9c379 | Model inventory (discovery) |
| E3 | `models/res_users.py` | 9d42d77ae8ec19028c99b3c668294569ded3a86a | Users, credentials, login throttle, identity re-check, API keys, multi-company group sync, password wizards |
| E4 | `models/res_company.py` | 86aa2fb0f6974bdf0f541efb2c871b37a43c140c | Company hierarchy (parent/branches), root-delegated fields, archive rules, accessible branches |
| E5 | `models/res_partner.py` | 502616ef7cb343716ce083465d390a04d0168b9c | Partner company scoping, commercial entity, sync, share flag |
| E6 | `models/res_groups.py` | e69accc22b676fccb5d0372e5312f259b1599f6b | Groups, implication graph, disjoint user-type groups, API-key duration |
| E7 | `models/res_groups_privilege.py` | 2beef468fe9da079b551d8def5bdb21bf81967b3 | Privilege grouping of groups under categories |
| E8 | `models/ir_model.py` | ca0c48b566843ece9948c8c5e7f759714a3faf8e | Model/field registry, ACL model (`ir.model.access`) and its check |
| E9 | `models/ir_rule.py` | e64f4e2c88209836d39f2bfe163469def41b71c0 | Record rule model and domain combination |
| E10 | `models/ir_cron.py` | e8762b920da6a68fd655dccf1a936671838c561d | Scheduler: acquisition/locking, run identity, progress, failure/deactivation |
| E11 | `models/ir_config_parameter.py` | 21c82bf62ed0fec4b4307c935f8a2b4ebaff4321 | System parameters: access, cache, protected keys |
| E12 | `models/ir_actions.py` | 45d06ee4210b6e5559c6c96ab82ddc238a891a52 | Action types; server-action execution and access gate |
| E13 | `models/ir_http.py` | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | Route auth levels (none/public/user/bearer), dispatch |
| E14 | `models/res_users_settings.py` | 3aeed6ec46bc0b0be871973923e6f5114b1ed788 | Per-user settings record |
| E15 | `models/res_users_deletion.py` | d6c1118d1a805aee3ba36392c922cdef14f95829 | Deferred portal-user deletion queue |
| E16 | `models/res_device.py` | 024373541e712686b4dbe3ea86e66ee090f3fcc7 | Device/session log and revocation |
| E17 | `security/base_groups.xml` | 2cd6d3d44b9757420bbd014f68131cf4eb7fe6fd | Core groups and implications |
| E18 | `security/base_security.xml` | 63195795684ed8d3c873e6a5a67324dd07482333 | Record rules incl. multi-company rules |
| E19 | `security/ir.model.access.csv` | 29785e02c9795cd27a0b6b5652853d03995b9c35 | ACL rows (147 lines) |
| E20 | `data/ir_cron_data.xml` | 0676236bea129b4f4d5c0994eeb3c6a47701f203 | Base scheduled jobs |
| E21 | `data/ir_config_parameter_data.xml` | 847602ca6046f49c3068549b9222b3a48c3ef79d | Seeded parameter |
| E22 | `data/res_users_data.xml` | 3cca8531297cdc922a247796457548f608ac7cf8 | Seed users (fetched; structural only) |
| E23 | `data/res_company_data.xml` | 407f9ba6bde968435f451bac88f45a88f55ca451 | Seed main company (fetched; structural only) |

New blob count: 23 (+4 carried forward = 27 referenced).

## 2. Findings by Card Section

### 2.1 Manifest
1. `base` is the kernel module: category Hidden, `auto_install` true, `post_init_hook` declared, licence LGPL-3, no `depends` key (E1).
2. Data load order places groups and record rules (E17, E18) before views, and the ACL CSV (E19) last in the data list (E1). WHY: ACL rows reference models/groups created earlier. RISK: none observed statically.
3. Demo data declared separately (users, partners, banks, currency rates) (E1).

### 2.2 Data
4. Scheduled jobs seeded: daily internal auto-vacuum and daily portal-user deletion GC with batch size 50 (E20, E15).
5. Seeded parameters: max email size (noupdate) (E21); portal user template pointer via parameter `base.template_portal_user_id` (E17).
6. Protected auto-initialised parameters: database secret, uuid, creation date; they cannot be renamed or deleted (E11 `_default_parameters`, `write`, `unlink_default_parameters`).
7. Core groups (E17): internal user role, administrator role (implies access-rights manager and HTML-sanitize bypass; root and admin users linked), access-rights manager (implies internal user), portal role, public role, multi-company, multi-currency, technical features, export-allowed, contact-creation; a noupdate "default access for new users" group. Internal-user group carries an API-key max duration of 90 days.

### 2.3 Business rules / exceptions
8. Users: login unique (E3 `_login_key`); default company must be within allowed companies for active users (E3 `_check_user_company`); a user cannot sit in more than one user-type group (internal/portal/public) (E3 `_check_disjoint_groups`, E6 `_get_user_type_groups`); at least one administrator must remain (E3 `_check_at_least_one_administrator`).
9. Users write guards: cannot activate superuser; cannot deactivate self; admin, template and public users cannot be deleted (E3 `write`, `_unlink_except_master_data`).
10. Self-service write: a user editing only self-writeable fields is elevated (sudo) for that write; a self-chosen default company outside allowed companies is silently dropped (E3 `write`, `SELF_WRITEABLE_FIELDS`). RISK: silent drop, not an error.
11. Changing a user's default company re-points a company-bound linked partner to the new company (E3 `write`). Partner company change is rejected if incompatible with its users' companies and cascades to child contacts (E5 `write`).
12. Multi-company group auto-sync: the multi-company group is added when a user has more than one allowed company and removed when one or fewer (E3 `UsersMultiCompany` create/write/new).
13. Passwords: hashed with PBKDF2-SHA512, rounds = max(600000, parameter `password.hashing.rounds`) (E3 `MIN_ROUNDS`, `_crypt_context`); plaintext rows found at init are re-hashed (E3 `init`); empty passwords rejected (E3 `_change_password`, `_check_uid_passwd`); own password must go through the change wizard, not the admin field (E3 `_set_new_password`).
14. Login throttle: per source IP, in-process (not shared between workers), cooldown after N failures for D seconds; parameters `base.login_cooldown_after` (default 5; 0 disables) and `base.login_cooldown_duration` (default 60) (E3 `_assert_can_auth`, `_on_login_cooldown`). RISK: per-worker counter; proxy misconfiguration collapses sources.
15. Identity re-check: sensitive actions (API-key wizard, revoke devices, change own password, key removal) require a password re-check within the last 10 minutes and are refused outside HTTP (E3 `check_identity`).
16. API keys: random key stored hashed with an 8-hex-char lookup index; expiration mandatory unless sudo/admin; max duration = highest group `api_key_duration`; no past dates; programmatic generation requires admin or parameter `base.enable_programmatic_api_keys`; removal only by owner or system user (E3 `ResUsersApikeys`, E6 `api_key_duration`). RPC password check falls back to API key match; a hook allows forcing API-key-only RPC (E3 `_check_credentials`, `_rpc_api_keys_only`).
17. Company hierarchy: parent/branch via stored parent path; hierarchy immutable after creation; duplication forbidden; archiving a company archives its branches; cannot archive a company that is default company of active users; root-delegated fields (currency) forced identical on branches and propagated on root change (E4 `write`, `copy`, `_check_active`, `_check_root_delegated_fields`, `_get_company_root_delegated_field_names`).
18. Partner commercial entity: a company partner or a parentless partner is its own commercial entity, otherwise inherits the parent's; VAT is the synced commercial field, company registry/industry are commercial fields propagated to descendants (E5 `_compute_commercial_partner`, `_synced_commercial_fields`, `_commercial_fields`). A company-type partner representing a company must carry that same company (E5 `_check_partner_company`). Partners linked to active users cannot be archived/deleted (E5 `write`/`unlink` guards).
19. Record rules: cannot target the rule model itself; domain validated at save; at least one permission must be set (E9 constraints).
20. Scheduler write/delete refused while the job is running (row lock) (E10 `write`, `_unlink_unless_running`); manual run refused if already executing (E10 `method_direct_trigger`).

### 2.4 Security (access model; multi-company mechanism)
21. Two layers: model-level ACL (`ir.model.access`) then record rules (`ir.rule`). Superuser mode bypasses both: ACL check returns true and rule lookup returns none when the environment is in superuser mode (E8 `check`, E9 `_get_rules`).
22. ACL evaluation: allowed-model set per user and mode = union over rows that are active, grant the mode, and have no group or a group of the user (incl. implied groups); cached per uid+mode and cleared on ACL or user-group changes (E8 `_get_allowed_models`, `call_cache_clearing_methods`; E3 `write`). Group-less granting rows are flagged deprecated with a warning (E8 `create`).
23. Record-rule evaluation (E9 `_compute_domain`): rules matching model+mode are split into **global** (no groups; computed flag) and **group** rules (only those whose groups intersect the user's groups). Result = AND of every global domain AND (OR of applicable group domains). Rules of `_inherits` parents are ANDed in through the delegation field. Evaluation context exposes `user`, `company_ids` (companies currently activated by the user via the company switcher, described as filtered/trusted) and `company_id`. Cache key includes uid, superuser flag, model, mode and the `allowed_company_ids` context value. Failure diagnostics treat group rules as a single OR block and each global rule individually (E9 `_get_failing`).
24. Multi-company rule mechanism (E18): shared/master data use **global** rules keyed on the active company set with ancestor semantics: partner visible if its partner is internal-user-linked, or its company is a parent-of an active company, or it has no company; the same parent-of-or-empty pattern applies to partner bank accounts and currency rates. Users: global rule shows internal users always and share users only if they belong to an active company. Companies: **group** rules (non-global) restrict internal/portal/public users to active companies while access-rights managers see all (OR of group rules lets the manager rule win). WHY: branches see parent-company records; root/branches linkage via parent path (E4). RISK: parent-of means records of a branch are not visible from the parent company unless the branch is also active.
25. Partner model declares automatic company-consistency checking with parent-of semantics (E5 `_check_company_auto`, `_check_company_domain`); users define their own company-domain helper (E3 `_check_company_domain`). Enforcement code lives in ORM core (Gap G1).
26. Accessible-branch helper: branches of a company intersected with the active company set; superuser (e.g. cron) falls back to the company itself (E4 `__accessible_branches`).
27. Key ACLs (E19): scheduler, server actions, config parameters restricted to administrator role (full CRUD); ACL, rule, group, user, company, model registry managed by access-rights manager; internal/portal/public read on users, companies, partners; partner write/create/delete only for contact-creation group; API keys readable by internal and portal users (row-limited by E18 rules: own keys; admins all; public none). Administrator group appears in 52 ACL rows.
28. Other rules (E18): per-user ownership rules for user logs, defaults, personal view customisations, filters, identity-check and password wizards, user settings, devices and device logs; portal/public users see only partners within their commercial entity (read-only) and portal users only users of their commercial entity.
29. Config parameters: `get_param` checks read ACL (administrator only per E19); values are cached by key; framework code routinely reads them in sudo (E11, E3 `_on_login_cooldown`, E13 `_pre_dispatch`). RISK: any sudo reader bypasses the ACL.
30. Server actions guard (E12 `_can_execute_action_on_records`): if the action has groups, the caller must belong to one; otherwise the caller needs model write ACL and write-rule access on the target records (real records only). Code actions are syntax/safety-checked at save (E12 `_check_python_code`); actions with warnings refuse to run (E12 `_run`).

### 2.5 UI surfaces (names only, from E1 data list)
31. Menus/views for: actions, assets, system parameters, scheduled actions and triggers, filters, mail servers, models/fields, attachments, record rules, sequences, menus, views, defaults, logging, modules (+update/upgrade/uninstall/language wizards), partner merge, profiling, companies, languages, partners, banks, countries, currencies, groups, users, API keys, devices, identity check, settings, paper formats.

### 2.6 Jobs / config
32. Scheduler run identity: each job runs in a new environment with the job's configured scheduler user (default = creator) — not superuser mode (E10 `_run_job`, `user_id`); the job's linked server action is run via `run()` in that environment (E10 `_callback`).
33. Locking: jobs acquired with row-level skip-locked selection so parallel workers do not double-run; ready jobs ordered by failure count, priority, id (E10 `_acquire_one_job`, `_get_all_ready_jobs`).
34. Batching/progress: a run loops at least 10 iterations / 10 seconds while progress is reported; progress records track done/remaining and a deactivate flag (E10 constants, `_commit_progress`).
35. Failure handling: 3 consecutive timeouts count as failure; deactivation after ≥5 consecutive failures AND ≥7 days since first failure, with admin notification; success resets counters; module-state/version mismatch defers execution up to 5 hours (E10 constants, `_update_failure_count`, `_check_modules_state`).
36. Rescheduling adds the interval in the user's timezone to keep wall-clock hour across DST (E10 `_reschedule_later`). Toggling a job is suppressed on neutralized databases (E10 `toggle`).
37. Config keys observed: `password.hashing.rounds`, `base.login_cooldown_after`, `base.login_cooldown_duration`, `base.enable_programmatic_api_keys`, `base.template_portal_user_id`, `base.default_max_email_size`, `database.secret/uuid/create_date`, `database.is_neutralized`.

## 3. Cross-module edges

38. **Server action execution identity (resolves base_automation Lane A Gap G4, source level):** `run()` builds the evaluation environment from the environment of the recordset on which `run()` is called; the access gate (item 30) is evaluated in that same environment; the runner is then invoked on a sudo'd action record (E12 `run`, `_run`, `_get_eval_context`). Consequences read from source:
    - Code actions: executed with the **caller's** environment (`env`, `record(s)`) — i.e. the triggering user, unless the caller itself was already in superuser mode.
    - Update/create/duplicate actions: record lookups are made through the action's own (sudo'd) environment, so the write/create/copy is performed in **superuser mode** after the caller-level gate has passed (E12 `_run_action_object_write/_create/_copy`).
    - Multi actions: children are iterated from the sudo'd parent and each child's `run()` therefore evaluates and gates in **superuser mode** (E12 `_run_action_multi`).
    - Sudo preserves the uid, so audit fields/`user` in code refer to the calling user.
    - Hence if base_automation calls `run()` on actions iterated under sudo (per its Lane A item 22), code actions would execute in superuser mode with the triggering uid. RISK: privilege elevation for any rule-triggered action. Needs runtime proof (A1/PROOF).
    - Scheduled actions run as the configured scheduler user, non-elevated at entry (item 32).
39. HTTP auth levels (E13): `none` (no user), `public` (falls back to public user), `user` (rejects missing or public user), `bearer` (API key in Authorization header with global scope, stateless session; key/session user mismatch refused; interactive use requires browser Sec-Fetch headers). Session validity checked before each dispatch; unexpected auth errors map to access denied. Edge to `web`/`http_routing` controllers and `odoo/http.py`.
40. Partner/user/company models are the tenancy anchor for every G01 module (mail, portal, resource, auth_signup, digest); portal template user and deletion GC are edges to `portal`/`auth_signup`.
41. Company creation may auto-install localisation modules when a country is set (E4 `install_l10n_modules`) — edge to l10n groups outside G01.

## 4. Evidence gaps

- G1: ORM enforcement of `_check_company_auto` / company-consistency, `check_access`, `sudo`/`with_user` semantics, and derivation of `env.companies` from `allowed_company_ids` live in `odoo/orm/*` and `odoo/api.py` — outside `odoo/addons/base/`, not read.
- G2: `security.check_session`, session token handling and request lifecycle live in `odoo/http.py`/`odoo/service/security.py` — not read.
- G3: API-key credential helper `_check_apikey_credentials` is imported from outside the read scope (expiry enforcement at check time not verified).
- G4: `res_users_apikeys.py` does not exist at the anchor (HTTP 404); API keys live in E3.
- G5: Views XML, wizards, `ir_ui_menu`, `ir_ui_view`, `ir_module`, `ir_autovacuum`, `ir_mail_server`, `ir_filters`, `ir_default`, `res_config`, reports, controllers-free assets and tests not read (breadth pass).
- G6: E22/E23 fetched and hashed but only structurally inspected.
- G7: Base_automation call-site (whether `run()` is invoked on sudo'd actions) is asserted by the base_automation Lane A file, not re-verified here.

## 5. Limitations

- Static source only; no runtime, no database. Source presence ≠ runtime reachability; module overrides (e.g. 2FA, mail) may change identity/credential behaviour.
- Structural/grep-led reading of very large files (E3, E5, E8, E12); unlisted methods not analysed.
- No QIDs answered; no Formal Coverage; clean-room abstractions only; git not touched.
