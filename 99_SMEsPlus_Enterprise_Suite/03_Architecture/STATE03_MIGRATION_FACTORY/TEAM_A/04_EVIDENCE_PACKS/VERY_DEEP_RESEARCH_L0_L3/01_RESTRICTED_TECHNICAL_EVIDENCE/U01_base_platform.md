# U01 base_platform — Restricted Technical Evidence (L2/L3)

**RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**

- Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`
- Unit: U01 `base_platform`
- Modules owned: `base`, `base_setup`, `base_automation`
- Source revision: `19.0.post20260921` (Odoo Community only; `odoo-19.0.post20260921/odoo/addons`)
- Date: 2026-10-02
- Restored DB used for configuration/structure counts only (`itest19c_research`; 1 company, 356 installed modules, no transactions). No business data, partner/user/company identifying values or credential values were read or recorded.
- Claim ids `VDR-U01-C###`; neutral ids `N-U01-###` (see `02_NEUTRAL_KNOWLEDGE/U01_base_platform_NEUTRAL.md`).

## 0. Method, scope and honesty notes

1. Read in full (every line viewed): `base/models/ir_rule.py`, `res_company.py`, `res_groups.py`, `res_users.py`, `res_currency.py`, `res_bank.py`, `ir_sequence.py`, `ir_cron.py`, `ir_config_parameter.py`, `ir_default.py`, `res_config.py`, `ir_autovacuum.py`, `res_users_deletion.py`, `ir_logging.py` (head), `base/security/base_security.xml`, `base_groups.xml`, `ir.model.access.csv`, `base/wizard/base_partner_merge.py`, `base/wizard/base_language_install.py`, `base/data/ir_cron_data.xml`, `ir_config_parameter_data.xml`, `res_company_data.xml`, `res_users_data.xml`; `base_automation/models/*.py`, `controllers/main.py`, `data/base_automation_data.xml`, `security/ir.model.access.csv`; `base_setup/models/*.py`, `controllers/main.py`, `data/base_setup_data.xml`.
2. Read partly: `base/models/res_partner.py` (lines 184-1160 and merge-relevant parts), `ir_model.py` (access, data, selection-reflection parts 1832-1846 and 2080-2726 only), `ir_actions.py` (server actions 567-1260, bindings 156-225), `ir_attachment.py` (access parts 456-709, 711-830), `ir_ui_menu.py` (72-146), `res_lang.py` (110-128, 388-404).
3. NOT read (stated honestly): `base/models/ir_module.py`, `ir_ui_view.py`, `ir_qweb*.py`, `assetsbundle.py`, `ir_asset.py`, `ir_http.py`, `ir_mail_server.py`, `ir_filters.py`, `ir_exports.py`, `ir_profile.py`, `res_country.py`, `res_device.py` (only its autovacuum names grepped), `res_lang.py` beyond the lines above, `ir_actions_report.py`, `report_*`, `decimal_precision.py`, `properties_*`, all `base/views/*.xml`, `base/report`, `base/wizard/base_module_*`, `base_import_module`, `base_setup/controllers/kpi.py`, `base_setup/models/kpi_provider.py`, the web client JS beyond `web/static/src/core/user.js:57-86`, authentication modules (`auth_*`), and every translation file.
4. **Core framework facts (outside `odoo/addons`)** were read where the base module depends on them (`odoo/orm/models.py:169-185, 3375-3387, 4003-4103, 4132-4150, 4522, 4749, 5967-6031`; `odoo/orm/environments.py:61-72, 182-190, 208-283`; `odoo/orm/fields.py:1001-1030`; `odoo/orm/fields_relational.py:125-165`). The claim gate only resolves pointers under `odoo/addons`, so core facts appear in claims only as `INFERENCE` rows anchored on a base-module line and naming the core file:line in the statement; they are not mechanically verified by the gate.
5. No execution of any kind (no Odoo start). Items that need execution are tagged `RT`.
6. Function-IDs: the 53-entry index has no entry that matches U01 capabilities. `MCT-F01` (Warehouse-company binding) and `MCT-F05` (Warehouse-level user access control) are stock-specific; U01 only provides the generic company-scope and access mechanisms they rely on, so they are NOT mapped. All claims carry `FUNCTION MAPPING REQUIRED`.

**DISCOVERED SUPPORTING MODULES** (read only as far as needed): `web` (session_info, company cookie/context in `web/static/src/core/user.js`, `web/models/ir_http.py`), `mail` (admin notification on cron deactivation, extra server-action types, merge note), `sms` (SMS server action), `product` (pricing group on multi-currency, synced price list), `account` (commercial fields, currency decimals guard, root-delegated company fields, merge summable fields), `website` (rule evaluation context and cache key, merge visitors), `loyalty` (merge cards), `base_vat` (present in source, NOT installed in the DB). Core outside-addons files listed in note 4.

**CONTRADICTIONS WITH PRIOR EVIDENCE**: none found. The prior candidate (`MODULE_base.md`, sections A/C/E) was compared on multi-company mechanics, rules, cron, merge and group chain and agrees. One refinement (not a contradiction): the candidate says the partner merge writes a note; in `base` it only logs to the server log (C450) and the note is posted by `mail` when installed (C451). Count bases differ: B01 per-module row lists `db_ids` 4036 for `base`, whereas `ir_model_data` rows owned by `base` are 6680 here (this unit counts every metadata row); no CONTRA flag raised.

## CAP-U01-01 Multi-company data-scope mechanics

**Function-ID(s):** `FUNCTION MAPPING REQUIRED` (MCT-F01/MCT-F05 considered and rejected: stock-specific).

**D1 Business purpose and process semantics.** One database serves several companies. A company has an own contact record, currency, optional parent (branches). Users carry an allowed set of companies and a default; the browser activates a subset per session. Scoping hides other companies' records while records without company are shared. Branches see parent-company master data. Cross-company references between records are refused at save time.

**D2 Architecture / data / object relationships.**
- `res.company` (`_parent_store`, `parent_id`/`child_ids`, `partner_id` required, `currency_id` required) — C001-C005.
- `res.users.company_id` (default) and `company_ids` (allowed) via `res_company_users_rel`; `_get_company_ids` returns only active companies — C021-C025.
- Company-scoped base models: `res.partner` (optional `company_id`), `res.partner.bank` (related to holder company), `res.currency.rate` (root company or none), `ir.sequence` (optional), `ir.default` (optional), `ir.attachment` (stamp only) — C031, C036, C041, C043, C044.
- Core mechanisms used by these models: `_check_company_auto`, `_check_company_domain`, `check_company_domain_parent_of`, company-dependent fields (JSON per company id), `env.company`/`env.companies` from the `allowed_company_ids` context — C029, C030, C048, C052.
- Record rules implement the read-side filter (see CAP-U01-02).

**D3 Source / technical / workflow logic.**
- Client: activated company ids are held in cookie `cids` and context `allowed_company_ids` (first = current company) — C047; server session info lists user companies plus unauthorised ancestors — C046.
- Request: `env.companies` = context list (validated against `_get_company_ids` unless sudo) else all user companies — C048 (core).
- Read scoping: rules use `company_ids` (all activated) and `company_id` (current) — C048, C032, C082.
- Write scoping: `_check_company` compares company-checked relational fields with `_check_company_domain` (parent-of) and raises a UserError when inconsistent — C030.
- Branch semantics: root/branch tree via `parent_path`; currency delegated to root (`_get_company_root_delegated_field_names`, create copy, write push, constraint) — C011-C014; rates only on root companies — C267-C268; `_accessible_branches`, `_all_branches_selected` helpers — C018, C020.
- State diagram (company):
  - `(none) -> active [create; partner auto-created if absent; added to creator and superuser company_ids]`
  - `active -> archived [write active=False; branches archived too; refused if default company of an active user]`
  - `archived -> active [write active=True]`
  - `branch -> (parent changed) [refused: hierarchy immutable]`; `company -> copy [refused]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Create company (partner auto-made, linked to creator and superuser), optionally as branch with root currency; add to users' allowed set; user activates companies in the client; records created under first activated company | C006, C017, C012, C021, C047 |
| 2 | Reversal / negative | Archive cascades to branches and is blocked while default for active users; hierarchy cannot change; copy refused; cross-company link refused; user default company outside allowed set refused | C015, C016, C010, C009, C030, C023 |
| 3 | Multi-company / data scope | Shared when company empty; ancestor-or-self visible; branch records not visible from parent unless active; users rule and company rule exist; client sends allowed ids; server validates | C032, C029, C082, C086, C088, C047, C048 |
| 4 | Side effects / cross-module | Creating company with country installs localisation modules (`install_l10n_modules`, res_company.py:243-253 read, not claimed); multi-company display group toggled automatically; accounting adds root-delegated fields | C026, C027, C011 |
| 5 | Configuration / optionality | Single-company DBs need nothing; DB has 1 company, 0 branches; group toggling automatic | C053, C026, C027 |
| 6 | Validation / constraints | Unique name; hierarchy immutability; delegated field equality; default-company-in-allowed; active-user guard | C008, C010, C014, C023, C016 |
| 7 | Roles / permissions | Company record rules by group (employee/portal/public see activated; erp_manager sees all); ACL read for all, CRUD for erp_manager; create company needs erp_manager (csv 42-45) | C088, C089, C090 |
| 8 | Scheduled / automated | Crons run with no company context so env.companies = all user companies; superuser accessible-branch fallback | C050, C019 |
| 9 | Exception / failure | UserError "no company crossover is allowed"; AccessError on unauthorised activated companies; error text hints company switch | C030, C048, C049 |
| 10 | Accounting / audit / security | Company isolation depends on rules and `_check_company`; sudo bypasses both; attachments carry company but do not use it; company-dependent values stored per company | C044, C426, C052, C050 |

**DB reconciliation (config only).** `res_company`: 1 row, 0 with parent; seeded `main_company` with partner; currency THB while base seed says USD (C281). `res_company_users_rel`: 4 rows; 4 users all with `company_id` (C053-C054). Company-dependent fields: 63 registered overall, 23 on `res.*` (22 on `res.partner`, 1 on `res.users`) (C055). Rules that reference company ids: 144 overall, 7 owned by base (C102).

**Unknown / Runtime.** Company switcher client behaviour (C446, `RT`); data left behind when a company is removed from a user (C447, `RT`); effective scoping in non-base models (C449); whether the cron/automation/webhook elevated modes leak across companies on real data (`RT`).

## CAP-U01-02 Record rules engine

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Record rules give row-level restriction per model and per operation. Global rules (no group) apply to everyone and are AND-ed; group rules are OR-ed among the user's groups and the OR result is AND-ed with the globals. Superuser/sudo bypass rules. Base seeds 32 rules, 7 of which scope by company.

**D2.** `ir.rule` (`model_id`, `groups` m2m via `rule_group_rel`, `domain_force`, four perm flags, `active`, computed stored `global`), evaluated in `ir.rule._compute_domain` with `_get_rules` (SQL on rule/group tables) and `_eval_context`. Consumers: core `_check_access` (core orm/models.py:4132-4150) applies `Rule._compute_domain` after the model-level ACL check; searches inject the same domain. Parent (`_inherits`) models contribute their rules through the link field.

**D3 Logic.**
- `_get_rules(model, mode)`: su -> none; else active rules with `perm_<mode>` that are global or linked to a group of the user (C068, C069).
- `_compute_domain`: for parents, add rules of parent models; evaluate each applicable rule domain via `safe_eval` with `user`, `company_ids`, `company_id`; group rules need group membership (C072); empty domain -> TRUE (C073); globals AND; groups OR then AND (C074, C075). Cached by uid/su/model/mode/`allowed_company_ids` (+`website_id` with website installed) unless dev xml (C065, C066, C076).
- Create/write/unlink clear the registry cache (C077). Domain is validated at save (C064); at least one perm flag (C058); no rules on `ir.rule` (C063).
- Failure reporting: `_get_failing` and `_make_access_error`; detailed rule names only for technical-feature internal users (C078, C079, C049).
- State: `rule.active -> inactive [active unchecked]`; `inactive -> active`; `seeded rule deleted -> recreated [module update, only if not noupdate handling allows]` (C059; all 32 base rules are noupdate, C101).
- Evaluation order list: `request -> su? -> yes: allow` ; `-> ACL (ir.model.access) -> denied: AccessError` ; `-> ir.rule domain on records -> forbidden records: AccessError`.

**Rules declared in `base` (names = XML ids; ops = R/W/C/D flags; groups by id)** — all in a `noupdate="1"` block of `base_security.xml`; DB shows exactly these 32 rows owned by base (9 global, 23 group):

| XML id | Model | Scope | Domain summary | Ops | Claim |
|---|---|---|---|---|---|
| res_partner_rule | res.partner | global | not share-partner OR company ancestor-or-self of company_ids OR no company | RWCD | C081, C082 |
| res_partner_portal_public_rule | res.partner | portal+public | child_of own commercial partner | R | C083 |
| res_partner_bank_rule | res.partner.bank | global | company parent_of company_ids OR none | RWCD | C084 |
| res_currency_rate_rule | res.currency.rate | global | same | RWCD | C085 |
| res_users_rule | res.users | global | not share OR user company in company_ids | RWCD | C086 |
| res_users_rule_portal | res.users | portal | own commercial partner | RWCD | C087 |
| res_company_rule_employee / portal / public | res.company | user / portal / public | id in company_ids | RWCD | C088 |
| res_company_rule_erp_manager | res.company | erp_manager | always true | RWCD | C089 |
| api_key_public / api_key_user / api_key_admin | res.users.apikeys | public / portal+user / system | false / own / true | RWCD | C091-C093 |
| ir_filters_admin_all_rights_rule, ir_filters_employee_rule, ir_filters_portal_public_rule | ir.filters | erp_manager / user / portal+public | true / owner-or-shared / shared with user | RWCD | C094 |
| ir_default_user_rule, ir_default_system_rule | ir.default | user / system | own / true | WCD | C095 |
| res_users_settings_rule_user / admin | res.users.settings | user / system | own / true | RWCD | C096 |
| user_device, user_device_admin, user_device_logs, user_device_logs_admin | res.device(.log) | user / system | own / true | RWCD | C097 |
| res_users_log_rule | res.users.log | global | create_uid = user (read not restricted) | WCD | C098 |
| change_password_rule, change_password_own_rule, res_users_identity_check | wizards | global | create_uid = user | RWCD | C099 |
| ir_ui_view_custom_personal | ir.ui.view.custom | global | user_id = user | RWCD | (declared base_security.xml:50-54, not separately claimed) |
| embedded_action_user_delete_rule / admin | ir.embedded.actions | user / system | own-or-shared / true | WD | C100 |
| properties_base_definition_rule_admin | properties.base.definition | system | true | RWCD | (declared base_security.xml:256-261, not separately claimed) |

Company-isolation rules of base: `res_partner_rule`, `res_partner_bank_rule`, `res_currency_rate_rule`, `res_users_rule`, and the three `res_company_rule_*` for employee/portal/public (7 total with company id in the domain; DB confirms 7). Combination consequence: `res_company_rule_erp_manager` OR-ed with the employee rule gives managers all companies (C090).

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | User search/read: ACL grants, domain = AND(globals, OR(group rules)) filters the rows | C068-C075 |
| 2 | Reversal / negative | Records outside domain raise AccessError with rule hints for technical users; switching off a rule (`active`) disables it | C078, C079, C059 |
| 3 | Multi-company | Domains use `company_ids`/`company_id`; cache keyed by `allowed_company_ids`; parent-of semantics | C060, C065, C032, C084 |
| 4 | Side effects | Rule edits clear the whole registry cache; website adds a variable and key | C077, C066, C067 |
| 5 | Configuration / optionality | Rules can be edited by erp_manager (ACL csv 28); sudo and superuser bypass | C068, C080 |
| 6 | Validation | Domain validated on save, perm flag CHECK, no rule on rule model | C064, C058, C063 |
| 7 | Roles / permissions | 32 base rules: 9 global/23 group (DB-confirmed); only erp_manager and system hold CRUD on rules (csv 28 for erp_manager) | C102, C142 |
| 8 | Scheduled / automated | Cron and automation run elevated (superuser id / sudo) so rules do not apply | C342, C371, C372 |
| 9 | Exception / failure | AccessError text; cache invalidation on errors not applicable; unparsable domain blocked at save | C079, C064 |
| 10 | Accounting / audit / security | Rule semantics (OR among groups) means group stacking widens access; res_users_log read unrestricted | C090, C098 |

**DB reconciliation.** `ir_rule` total 544 (162 global, 382 group); base-owned 32 (9 global, 23 group), all noupdate (C101-C103). Names/models match the XML list above. Other modules own 512 rows (not studied, C104).

**Unknown / Runtime.** Performance of parent-of filters on big partner tables; rule evaluation under non-default session context (`RT`); other modules' rules (C104).

## CAP-U01-03 Access control (groups, ACL, field-level, menu/action visibility)

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Groups (with implication) define roles; ACL entries grant CRUD per model per group; three disjoint user types (internal/portal/public) separate staff from outsiders; menus, actions and fields can be hidden by group.

**D2.** `res.groups` (`implied_ids`, `all_implied_ids` via `SetDefinitions`, `privilege_id`, `api_key_duration`, `share`), `res.groups.privilege`, `res.users.group_ids`/`all_group_ids`, `ir.model.access` (model, group, 4 perms), `ir.ui.menu.group_ids`, `ir.actions.*` `group_ids`/bindings, field `groups` attribute (core). Seeded: 12 groups, 2 privileges (Export, Contact), 146 ACL rows.

**D3.**
- `check` order: su -> allow (C080); allowed-models SQL: active entries with perm and (group NULL or user's all_group_ids) (C115, C116); then record rules (C118 inference).
- Group implication transitive closure and SetDefinitions (C105, C106, C132); implication removal refused (C133).
- User-type exclusivity checked on user group_ids and on group implications (C107-C110).
- At least one system admin (C111, C112); `base.group_no_one` effective only in debug (C113, C114).
- Menus (C119, C120); contextual actions (C121, C122); server action groups (C374); field groups (C123, C124); self-readable/writable lists (C125).
- New user default groups = `group_user` + implied of `default_user_group` (C126, C127).
- State: `user.group_ids -> all_group_ids [closure]`; `user -> internal | portal | public [group membership; mutually exclusive]`; `group.implied_ids changed -> caches cleared [write]` (C131).

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Operation allowed when any group of user grants it, then rules filter rows | C115, C116, C118 |
| 2 | Reversal / negative | AccessError from ACL (message lists groups); removal of implied membership refused; disjoint types refused | C115, C133, C110 |
| 3 | Multi-company | Groups/ACL are global (no company); company scoping is only via rules | C102 |
| 4 | Side effects | Group writes clear access caches; settings switches change implied groups of all users; currency count toggles multi-currency group | C131, C395, C276 |
| 5 | Configuration / optionality | Default user group template, role selection, privileges, `api_key_duration` | C126, C134, C184 |
| 6 | Validation | Unique name per privilege, name cannot start with "-", settings-linked group not deletable, last admin protected | C130, C129, C128, C111 |
| 7 | Roles / permissions | Chain system -> erp_manager -> user; no_one implied; export and contact groups implied by system; seeded ACL per group: user 38, erp_manager 19, system 50, allow_export 1, partner_manager 9, portal 13, public 10, group-less 6 (all 0000) | C135-C138, C141, C145 |
| 8 | Scheduled / automated | n/a for ACL itself; cron runs as superuser | C342 |
| 9 | Exception / failure | `ACCESS_ERROR` messages; group-less granting entries warn | C115, C117 |
| 10 | Accounting / audit / security | erp_manager holds CRUD on rules, ACL, groups, users: privilege escalation path; template accounts must stay outside employee groups | C142, C140 |

**DB reconciliation.** `res_groups` 119 (12 base); `res_groups_privilege` 27 (2 base); `res_groups_implied_rel` 110 rows; `ir_model_access` 2010 (146 base, all updatable); six base ACL rows have no group (all four perms 0): attachment portal/public, model-inherit, view, default, users-deletion, user-settings (C144-C146, C141). Seeded group ids: 1 user, 2 erp_manager, 3 sanitize override, 4 system, 5 multi-company, 6 multi-currency, 7 technical, 8 export, 9 contact creation, 10 portal, 11 public, 12 default-user template.

**Unknown / Runtime.** Client-side hiding by group attributes in view XML (C147, `RT`); effective counts of other modules' groups and ACLs.

## CAP-U01-04 Users and authentication-related lifecycle (base only)

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`. Authentication modules (`auth_*`) deliberately out of scope.

**D1.** A user is a login attached to a contact. Lifecycle: create, set password, archive/restore, change own password with identity re-check, API keys, login cooldown, portal account self-deletion, company switching and flags (`share`, internal/portal/public).

**D2.** `res.users` (`_inherits` partner; `login` unique; `password` hashed; `company_id`/`company_ids`; `group_ids`/`all_group_ids`; `share` stored computed), `res.users.log`, `res.users.apikeys` (custom table, hash + index), `res.users.settings`, `res.users.deletion`, wizards `change.password.*`, `res.users.identitycheck`, `res.device`.

**D3.**
- Login: `_login` -> `_assert_can_auth` (cooldown by source address, in-memory) -> exact login search -> `_check_credentials` (hash verify, upgrade replacement, API key path for non-interactive) -> last login row -> `authenticate` may refresh `web.base.url` for admins (C153, C154, C156, C157, C175-C178, C191, C193).
- Sessions: token HMAC over id, login, password hash, active (+ database secret) (C179, C413).
- Passwords: field `new_password` forbidden on own user (C160); wizard + `check_identity` 10 min (C161, C162); empty refused (C158); help text (C159).
- Create/write: settings row, avatar, partner company sync, activation rules, safe self-writes as superuser (C165-C168, C190).
- Delete: protected accounts (C169); partner guard (C170, C171).
- Portal deletion: `_deactivate_portal_user` + deletion queue + cron (C172-C174).
- API keys: internal only, expiry rules, random hashed keys, programmatic gating, GC (C182-C189).
- State diagram:
  - `(none) -> active [create]`
  - `active -> archived [write active False; not for self; not superuser]`
  - `archived -> active [write active True; contact unarchived first]`
  - `portal active -> renamed+archived+queued [_deactivate_portal_user]`
  - `queued -> deleted | failed [cron _gc_portal_users batch 50]`
  - `login failures >= threshold -> cooldown [per source address, memory]`; `cooldown -> normal [duration elapsed or success]`

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Create user (contact auto-linked), set password via wizard, sign in, record login | C148, C160-C162, C180 |
| 2 | Reversal / negative | Archive (not self/superuser); portal self-deletion; API key removal with identity check | C167, C168, C173, C162 |
| 3 | Multi-company | `company_id` default must be in `company_ids`; self change of company only to own companies; multi-company group auto | C023, C190, C026, C027 |
| 4 | Side effects | Contact company sync on create/write; settings row; web base URL refresh by admin login | C040, C165, C191 |
| 5 | Configuration / optionality | Cooldown params (DB 10/60), programmatic key params, hashing rounds param, group `api_key_duration` | C175, C178, C188, C156, C184 |
| 6 | Validation | Unique login; admin presence; disjoint types; home action constraint; API key expiry | C153, C111, C110, C192, C185 |
| 7 | Roles / permissions | ACL: employees/portal/public read users; erp_manager CRUD; wizards by group; self lists | C164, C125, C092 |
| 8 | Scheduled / automated | Daily portal deletion; autovacuum of logs and expired keys | C174, C181, C187 |
| 9 | Exception / failure | AccessDenied on cooldown/wrong credential; UserError on forbidden state changes | C177, C167, C158 |
| 10 | Accounting / audit / security | Slow salted hash upgrade; session invalidation on password change; cooldown not shared between workers; seed default admin password | C155-C157, C179, C176, C197 |

**DB reconciliation.** `res_users`: 4 rows (1 active internal admin; 1 archived technical superuser; 2 archived external: public + portal template) (C198). Base seeds 4 users (3 noupdate, 1 updatable). ICP: `base.login_cooldown_after` 10, `base.login_cooldown_duration` 60 (C199). Admin default password change status NOT examined (C200).

**Unknown / Runtime.** C200 (`RT`), C448 (second-factor/passkey/oauth/signup deliberately unread), brute-force behaviour across workers (`RT`).

## CAP-U01-05 Partner master data

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Contact master data (person/company, address types), commercial-entity propagation, bank accounts, hierarchy, merge, archive. Duplicate control is soft.

**D2.** `res.partner` (parent_id/child_ids, type, is_company, commercial_partner_id stored recursive, vat, company_registry, barcode company-dependent, company_id, active, partner_share), `res.partner.bank` (unique sanitized number per holder), `res.bank`, `res.partner.category`, `res.partner.industry`; wizard `base.partner.merge.automatic.wizard` + `base.partner.merge.line`.

**D3.**
- `create/write` -> `_fields_sync(values)`: from parent (commercial fields, address), to parent (address, synced commercial), to children (`_children_sync`) (C211-C214).
- Constraints: name for type contact, no cycle, company match, barcode (C203, C205, C249, C222); soft hints for vat/registry (C217-C220, C255).
- Archive/delete guards with users (C170, C171, C231).
- Banks: sanitise, unique, archive-on-delete, find-or-create rules (C223-C230).
- Merge: `_merge` (limit 3, parent/child refusal, 1 user, email equality) -> company alignment of users -> bank merge -> FK update (savepoint, delete on conflict) -> reference fields (+company-dependent JSON) -> value merge (summable) -> delete sources (C232-C246).
- State: `active -> archived [write active=False; refused if user]`; `contact -> merged-away [wizard merge; sources deleted]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Create company then people with parent; vat/address sync; add bank account | C206, C211-C214, C223 |
| 2 | Reversal / negative | Archive (unless user); bank unlink = archive; merge irreversible; copy adds suffix | C170, C226, C244, C248 |
| 3 | Multi-company | Optional company on contact; child follows parent; company-dependent barcode and commercial fields; rule `res_partner_rule` | C031, C037-C039, C051, C082 |
| 4 | Side effects | Merge repoints foreign keys, attachments, followers, activities, messages, external ids; accounting rank sums; website visitors/loyalty cards | C239-C243, C452 |
| 5 | Configuration / optionality | base_vat not installed (no format validation); account/product extend commercial fields | C251, C209, C210 |
| 6 | Validation | Name, cycle, company match, barcode, bank unique; no unique vat/ref/email | C203, C205, C249, C222, C223, C221 |
| 7 | Roles / permissions | ACL: internal read, partner_manager CRUD, portal/public read; merge wizard by partner_manager; rule portal child_of own entity | C143, C247, C083 |
| 8 | Scheduled / automated | None in base for contacts (partner autocomplete etc. other modules) | — |
| 9 | Exception / failure | RedirectWarning on user-linked archive/delete; UserError on merge preconditions; unique-violation rows deleted during merge | C170, C232-C235, C239 |
| 10 | Accounting / audit / security | Tax id sync to commercial entity; duplicates possible; merge commits per group (automatic), note only with mail | C255, C246, C450, C451 |

**DB reconciliation.** 7 `res_partner` rows (5 base-seeded: main partner, admin partner, technical, public, template; 3 archived); 0 `res_partner_bank`; 22 company-dependent fields on contacts; base_vat not installed (C251-C252).

**Unknown / Runtime.** Contributions of address-extension/autocomplete/country modules (C253); merge under real data (`RT`); automatic merge interruption (C254, `RT`).

## CAP-U01-06 Currency and rates

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Currency catalogue with rounding, dated rates held at root-company level, conversion service and display helpers, multi-currency toggle.

**D2.** `res.currency` (name, rounding, decimal_places stored, active, rate_ids), `res.currency.rate` (name date, `rate` technical, `company_rate`/`inverse_company_rate` computed, `company_id`), company currency link.

**D3.** `_get_rates(company, date)` SQL: latest rate <= date for root-or-shared, else earliest, else 1.0 (C269-C271); `_compute_current_rate` ratio against target currency (C272); `_get_conversion_rate` resolves to root company (C268); `_convert` rounds (C273); constraints (C258-C259, C263-C264, C267); company-currency active guard (C274, C275); group toggle (C276, C277). No rate-fetch cron in base (C283, C280).
- State: `currency active -> archived [write; refused if company currency]`; `active count 1 -> >1 [group_user gets multi-currency group]`; `rate (date) -> superseded [newer dated rate]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Enter dated rate on root company; convert amounts with rounding | C265, C269, C273 |
| 2 | Reversal / negative | Currency of company cannot be deactivated; rate must be > 0; one per day | C274, C264, C263 |
| 3 | Multi-company | Rates only on root; branch uses root; rule parent-of | C267, C268, C085 |
| 4 | Side effects | Multi-currency group toggle; pricing archiving; accounting decimal guard | C276, C277, C278 |
| 5 | Configuration / optionality | DB 2 active currencies, no rates; no auto provider | C282, C283 |
| 6 | Validation | Code unique, rounding > 0, rate > 0, 20% warning | C258, C259, C264, C266 |
| 7 | Roles / permissions | Everyone reads; system writes | C279 |
| 8 | Scheduled / automated | None in base; spreadsheet reads rates only | C280, C283 |
| 9 | Exception / failure | No rate -> 1.0 silently | C271, C284 |
| 10 | Accounting / audit / security | Rounding rules `compare_amounts`/`is_zero`; accounting guards | C262, C278 |

**DB reconciliation.** 170 currencies, 2 active (THB, USD), rounding 0.01 / 2 decimals, 0 rates; company currency THB while seed USD (C281-C282).

**Unknown / Runtime.** Accounting revaluation (C285); behaviour at 1:1 fallback in real flows (`RT`).

## CAP-U01-07 Sequences and numbering

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Configurable numbering with prefix/suffix/padding/step, standard vs gap-free, date ranges, per company.

**D2.** `ir.sequence` (implementation, prefix, suffix, padding, number_next, number_increment, company_id, use_date_range), `ir.sequence.date_range`; PostgreSQL sequences `ir_sequence_NNN[_NNN]` for standard.

**D3.** `next_by_code(code)` -> sequences of current company or none, ordered by company -> `_next` -> (date range lookup/creation) -> `_next_do` -> nextval or no-gap row update with NOWAIT -> `get_next_char` prefix+padded+suffix (C042, C286-C296). Writes alter/drop/create DB sequences (C297, C298). ACL (C299, C300).
- State: `sequence standard <-> no_gap [write implementation: drop/create DB sequences]`; `no date range -> range created [first draw for a date]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Draw next number for code in current company, formatted with padding | C042, C291, C296 |
| 2 | Reversal / negative | Standard: gaps on rollback; no-gap: no gap on rollback; no sequence -> False | C286, C289, C296 |
| 3 | Multi-company | Company-specific wins; no ir.rule on sequences | C042, C304 |
| 4 | Side effects | PostgreSQL objects created/dropped on write | C287, C298 |
| 5 | Configuration / optionality | Date ranges, step, reset next number (admin) | C293-C295, C301, C302 |
| 6 | Validation | Step non-zero, placeholder validity, unique range per sequence | C297, C291 |
| 7 | Roles / permissions | Internal read; system CRUD | C300 |
| 8 | Scheduled / automated | None | — |
| 9 | Exception / failure | NOWAIT lock failure under concurrency; invalid placeholder UserError | C290, C291 |
| 10 | Accounting / audit / security | Gap-free flag exists but base does not decide who needs it; DB: 2 no-gap sequences | C303, C306 |

**DB reconciliation.** 34 sequences, none base-owned; 2 no-gap; 1 with date ranges; 0 `ir_sequence_date_range` rows; 13 without company; no ir.rule on ir.sequence (C303, C304).

**Unknown / Runtime.** C306 (legal gap-free requirement per app); NOWAIT behaviour under load (`RT`).

## CAP-U01-08 Scheduler framework

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Cron jobs execute server actions on an interval with failure tracking, concurrency control and triggers.

**D2.** `ir.cron` (delegates `ir.actions.server`; interval, nextcall, lastcall, priority, user_id, failure_count, first_failure_date, active), `ir.cron.trigger`, `ir.cron.progress`; base seeds `autovacuum_job` and `ir_cron_res_users_deletion`.

**D3.**
- Worker: `_process_jobs(db)` -> `_check_version`, `_get_all_ready_jobs`, `_check_modules_state`, `_process_jobs_loop` -> `_acquire_one_job` (SKIP LOCKED) -> `_process_job` (clear schedule, run, update failure, reschedule) (C310-C313, C327, C328).
- `_run_job`: loop until >= 10 runs and 10 s; progress API `_commit_progress`; statuses fully done / partially done / failed (C317, C318, C345).
- Failure: `_update_failure_count`, thresholds, admin notification (C319-C325, C341).
- Scheduling: `_reschedule_later` (user tz), `_reschedule_asap` (trigger) (C318, C326).
- Manual run `method_direct_trigger` (C329); locks on edit (C330); triggers `_trigger` and GC (C331, C332).
- State: `idle -> ready [nextcall passed or trigger]`; `ready -> running [acquired]`; `running -> fully_done -> idle [reschedule_later]`; `running -> partially_done -> ready [trigger now]`; `running -> failed -> idle [failure_count+1]`; `failed x5 over >7 days -> inactive [deactivate + notify]`.

**Crons seeded by `base` (DB, config only)**

| XML id | Name | Interval | Priority | Active | Owner user id | Model/method |
|---|---|---|---|---|---|---|
| base.autovacuum_job | Base: Auto-vacuum internal data | 1 day | 3 | yes | 1 | `ir.autovacuum._run_vacuum_cleaner` |
| base.ir_cron_res_users_deletion | Base: Portal Users Deletion | 1 day | 8 | yes | 1 | `res.users.deletion._gc_portal_users(batch_size=50)` |

DB total 54 crons (47 active), all owned by user id 1; per module: account 2, account_edi 1, auth_signup 1, base 2, base_automation 1 (inactive), calendar 1, crm 2, crm_iap_enrich 1, digest 1, event 1, event_crm 1, fleet 1, gamification 2, google_calendar 1, hr 2, hr_attendance 2, hr_expense 1, hr_holidays 2, hr_presence 1, hr_skills 1, hr_work_entry 1, mail 8, mail_group 1, mass_mailing 2, microsoft_calendar 1, payment 1, project 1, purchase 1, sale 2, sale_pdf_quote_builder 1, sms 1, snailmail 1, stock 1, stock_account 1, transifex 1, website 2, website_crm_iap_reveal 1 (counts derived from the DB list; other modules not studied).

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Ready job acquired, run as owner, committed, rescheduled by interval | C310-C316, C326 |
| 2 | Reversal / negative | Failed run rolled back; deactivation after 5 failures and 7 days | C316, C321, C322 |
| 3 | Multi-company | No company field; context has no `allowed_company_ids` | C314, C050 |
| 4 | Side effects | Admin channel notification (mail); triggers; progress rows; vacuum runs all registered cleanups | C324, C318, C337 |
| 5 | Configuration / optionality | Interval/priority/user editable; `toggle` on neutralised DB blocked | C308, C309, C333 |
| 6 | Validation | Interval > 0; code version and module state gates | C334, C327, C328 |
| 7 | Roles / permissions | System group only | C335 |
| 8 | Scheduled / automated | This capability; two base jobs | C336, C340 |
| 9 | Exception / failure | Timeout counter, logging, `_notify_admin` base is log-only | C319, C320, C323 |
| 10 | Accounting / audit / security | Jobs as superuser bypass rules; unattended deactivation | C342, C341 |

**DB reconciliation.** C340: 54 crons/47 active/all user 1; triggers 0; progress rows 50.

**Unknown / Runtime.** C343, C344 (`RT`): concurrency under multiple workers, update-time skipping, real cadence.

## CAP-U01-09 Server actions and automated actions

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Server actions are stored operations (update/create/duplicate/code/webhook/multi; mail/sms add more) run from menus, crons or automation rules. `base_automation` lets admins bind actions to events (create, write, delete, archive, state/stage/tag/user/priority, date-based, messages, UI change, webhook) with pre/post conditions.

**D2.** `ir.actions.server` (state, model_id, code (system group), group_ids, child_ids, history), `ir.actions.server.history`, `base.automation` (trigger, filter_pre_domain, filter_domain, trigger fields, trg_date*, action_server_ids, webhook_uuid, record_getter, last_run), cron `ir_cron_data_base_automation_check`.

**D3.**
- Hook install: `_register_hook` patches `create`, `write`, `_compute_field_value`, `unlink`, `message_post`, onchange methods per model; re-installed on rule change with registry invalidation (C381-C383).
- Event path: patched method -> `_get_actions` (sudo search) -> pre filter (sudo) -> original method -> post filter -> `_process` (done-dict guard, trigger fields check, sudo actions) -> `ir.actions.server.run` (permission check, then sudo run) (C349-C352, C371-C374).
- Time path: cron `_cron_process_time_based_actions` -> per rule search of due records -> `_process`; error handling and cron interval management (C357, C360-C364).
- Webhook path: public route -> sudo lookup by UUID -> `_execute_webhook` -> record_getter safe_eval -> `_process` (C359, C366-C370, C389).
- Failure: exception in action aborts the original operation; webhook errors return HTTP 500; time-based errors roll back that rule and continue (C357-C359).
- Code actions: safe_eval, syntax check, history (C375-C377); webhook action post-commit (C378).
- State: `rule active -> patched models [register_hook]`; `rule archived/deleted -> unpatched [unregister + registry flag]`; `record event -> pre ok -> write -> post ok -> actions run (once per record per chain)`; `cron inactive -> active [time rule exists]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Create/update a record, post-condition true, actions run | C349-C351, C372, C373 |
| 2 | Reversal / negative | Exception rolls back user's operation; recursion guard; deletions cannot use mail actions | C358, C351, C355 |
| 3 | Multi-company | No company field or rule on rules; actions elevated | C388, C371, C372 |
| 4 | Side effects | Patches model methods; mail/SMS actions via other modules; webhook post-commit | C381-C383, C380, C378 |
| 5 | Configuration / optionality | Rules optional; DB has 0; cron seeded inactive | C386, C387, C365 |
| 6 | Validation | Model match, on_change code-only, message trigger needs mail thread, delay positive (base_automation.py:300-304 read, not claimed) | C353-C356 |
| 7 | Roles / permissions | System group only for rules; action groups or write access for execution | C385, C374 |
| 8 | Scheduled / automated | Time-based cron adaptive 1 min-4 h | C360-C362 |
| 9 | Exception / failure | Webhook 500 / validation error; time-based final exception | C357-C359 |
| 10 | Accounting / audit / security | Public webhook secret = UUID; elevated execution; code execution by admin; call logging optional | C366-C369, C389, C375 |

**DB reconciliation.** `base_automation` table: 0 rows; base_automation ACL 1, rules 0, groups 0; cron exists inactive; `ir_act_server` 168 rows (114 plain, 54 cron), all `code` state, none with `usage='base_automation'` (C386, C387).

**Unknown / Runtime.** C390 (`RT`): live-change, message and time-based behaviour; performance under load; multi-worker reload.

## CAP-U01-10 Configuration parameters and settings flow

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** One settings screen translates field-naming conventions into module installs, group switches, global defaults, system parameters and company-level field edits; parameters are database-wide key/values.

**D2.** `res.config.settings` (transient; base_setup extends), `ir.config_parameter`, `ir.default`, `ir.module.module` (install), `res.groups` (implied), `res.company` (related fields); `base_setup` adds fields and endpoints.

**D3.** `default_get` reads current state from defaults/groups/modules/params (res_config.py:238-296, read; summarised in C391); `execute` -> admin check -> `set_values` (defaults, groups, params) -> install/uninstall modules last (C392, C395-C398); company-level via `company_id` related fields (C399); parameter semantics (C405, C408-C411).
- State: `settings form -> saved [execute]`; `module toggle on -> install [immediate]`; `toggle off -> uninstall wizard`; `param set False -> deleted`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Admin edits settings, `set_values`, optional module install, reload | C391, C392, C395-C398 |
| 2 | Reversal / negative | Uninstall wizard; group removal via `_remove_group`; copy refused | C396, C414, C394 |
| 3 | Multi-company | Company fields edit chosen company; modules, groups, defaults, params are database-wide | C399, C397, C398, C395 |
| 4 | Side effects | Group switches change all internal users' rights; module installs reload registry | C414, C396 |
| 5 | Configuration / optionality | Toggles in base_setup; auto_install; `show_effect`, profiling window | C400-C402, C406 |
| 6 | Validation | Admin check; protected default params | C392, C409 |
| 7 | Roles / permissions | Settings ACL system group; `execute` needs erp_manager; param table system group; endpoint erp_manager | C393, C392, C411, C407 |
| 8 | Scheduled / automated | None | — |
| 9 | Exception / failure | AccessError for non-admin; invalid int/float param converted to 0 with warning (res_config.py:278-289 read) | C392 |
| 10 | Accounting / audit / security | Secret parameters (database.secret) and web.base.url; group changes global | C413, C408, C414 |

**DB reconciliation.** 45 `ir_config_parameter` rows (list of keys reviewed; no secret values read); base_setup owns 0 ACL/0 rules/0 groups; base seeds 2 parameters (C412). `ir_default` has 22 rows (count only).

**Unknown / Runtime.** C415 (kpi controller/provider unread); invitation flow and module install (`RT`).

## CAP-U01-11 Attachments, external identifiers, translations and language activation

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

**D1.** Attachments obey the access of their record; external identifiers give module ownership and update safety (noupdate); languages are catalogue entries activated to load translations.

**D2.** `ir.attachment` (res_model/res_id/res_field, public, type url/binary, company_id, access_token, file store), `ir.model.data` (module, name, model, res_id, noupdate), `res.lang`, `base.language.install`.

**D3.**
- Attachment `_check_access` (ACL+rules first, then record/field access; public read; recordless creator/admin) (C416-C420); `_search` filters (C421); write/create checks (C424, C425); tokens (C423).
- External id upsert/noupdate/`_process_end`/uninstall (C429-C433); `toggle_noupdate` (C432).
- Language guards and install wizard (C435-C439); context language fallback (C440).
- State: `xmlid updatable -> non-updatable [toggle_noupdate or noupdate data]`; `lang inactive -> active [lang_install: translations loaded]`.

**Ten dimensions.**

| # | Dimension | Finding | Claims |
|---|---|---|---|
| 1 | Happy path | Upload attachment on accessible record; module data loads with identifiers; language installed | C416, C429-C431, C438 |
| 2 | Reversal / negative | Delete needs write on record; module uninstall deletes owned records; language deactivation guards | C420, C433, C437 |
| 3 | Multi-company | Attachment company stamped but unused for access | C044, C426 |
| 4 | Side effects | Language install updates translations for all installed modules; unlink cleans attachments and identifiers (core unlink read at orm/models.py:4231-4260, not claimed) | C438 |
| 5 | Configuration / optionality | Storage file/db; non-updatable flag; active languages | C441, C429, C435 |
| 6 | Validation | No self-attachment; identifier uniqueness/space; language uniqueness and at least one active | C425, C427, C428, C435, C436 |
| 7 | Roles / permissions | Attachment ACL internal full; identifiers erp_manager CRUD (csv 15), language install system | C422, C438, C439 |
| 8 | Scheduled / automated | Autovacuum of orphan files (`_gc_file_store`, not read in detail) | C445 |
| 9 | Exception / failure | AccessError messages for attachments; ValidationError for serving attachments | C416, C424 |
| 10 | Accounting / audit / security | Non-updatable seeded rules do not follow upgrades; attachment token exposure | C444, C423 |

**DB reconciliation.** `ir_model_data` 54300 rows (base 6680: 5386 updatable, 1294 non-updatable; base rules non-updatable, ACL updatable); `ir_attachment` 3576 rows; `res_lang` 93 rows, 1 active (en_US) (C442, C443).

**Unknown / Runtime.** C445 (token sharing and file-store GC), real behaviour of translation loading (`RT`).

## Runtime / AWT-required register (U01)

- RT-01 company switcher end-to-end (C446, C047); RT-02 mixed-company writes by elevated code (cron/automation/webhook) (C050, C342, C389); RT-03 cooldown across workers (C176); RT-04 default admin credential state (C200); RT-05 cron multi-worker/update behaviour (C343, C344); RT-06 automation under load/live-change (C390); RT-07 merge under real data and interruption (C253, C254); RT-08 no-gap sequence concurrency (C290); RT-09 attachment tokens/GC (C445); RT-10 client hiding by group attributes (C147).

## Claims table

Columns: `Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref`. `UNKNOWN` rows carry pointer `n/a`. Rows with `INFERENCE` that cite core `odoo/orm` lines name them inside the statement (those core lines are outside the gate's reach).

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U01-C001 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:36 | _parent_store = True | FACT | always | — | Company model keeps a materialised parent path so hierarchy operators (parent_of, child_of) and root lookup work on the company tree. | N-U01-002 |
| VDR-U01-C002 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:51 | parent_id = fields.Many2one | FACT | always | — | Company has a parent link (ondelete restrict); the inverse child_ids field (line 52) is labelled Branches, so a branch is a company with a parent. | N-U01-002 |
| VDR-U01-C003 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:57 | partner_id = fields.Many2one | FACT | always | — | Every company requires a related contact record (partner_id required, indexed). | N-U01-001 |
| VDR-U01-C004 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:48 | related='partner_id.name' | FACT | always | — | Company name is a stored related field on the contact name, writable from the company. | N-U01-001 |
| VDR-U01-C005 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:67 | currency_id = fields.Many2one | FACT | always | — | Company currency is required; default is the current user's company currency. | N-U01-001 |
| VDR-U01-C006 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:291 | create missing partners | FACT | always | — | On create, a company supplied without partner_id gets a new contact (is_company True) built from name, logo, email, phone, website, vat and country. | N-U01-004 |
| VDR-U01-C007 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:500 | Public user for | FACT | always | — | _get_public_user returns or lazily copies a public (anonymous) user per company, restricted to that single company. | N-U01-004 |
| VDR-U01-C008 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:99 | company name must be unique | FACT | always | — | SQL unique constraint on company name. | N-U01-020 |
| VDR-U01-C009 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:39 | Duplicating a company is not allowed | FACT | always | — | copy() on a company always raises UserError. | N-U01-011 |
| VDR-U01-C010 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:358 | hierarchy cannot be changed | FACT | always | — | write() raises UserError whenever parent_id is in the written values: the company hierarchy is immutable after creation. | N-U01-011 |
| VDR-U01-C011 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:119 | return ['currency_id'] | FACT | always | — | Base list of fields delegated to the root company contains only currency_id; other modules extend it (accounting adds fiscal-year and tax settings, per account/models/company.py:311). | N-U01-010 |
| VDR-U01-C012 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:317 | Copy delegated fields from root | FACT | always | — | On create of a branch, delegated fields not supplied are defaulted from the parent company values. | N-U01-010 |
| VDR-U01-C013 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:386 | Copy modified delegated fields | FACT | always | — | On write of a root company, changed delegated fields are written to all branches found with child_of search. | N-U01-010 |
| VDR-U01-C014 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:433 | same as it's root company | FACT | always | — | Constraint: a company with a parent must have the same value as its parent for every delegated field (error text refers to root company). | N-U01-010 |
| VDR-U01-C015 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:381 | Archiving a company should also archive | FACT | always | — | write(active=False) also sets child_ids.active False. | N-U01-012 |
| VDR-U01-C016 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:420 | cannot be archived because it is | FACT | always | — | Constraint on active: a company cannot be archived while it is the default company_id of any active user (search_count on res.users). | N-U01-012 |
| VDR-U01-C017 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:327 | browse(SUPERUSER_ID) | FACT | always | — | On create, the new companies are linked into company_ids of both the creating user and the superuser (the comment at line 325 states this is done to put users in the multi-company group). | N-U01-013 |
| VDR-U01-C018 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:445 | __accessible_branches | FACT | always | — | Computes the branches (self and descendants) that are present in env.companies, with an orm cache keyed by active companies, company id and uid. | N-U01-007 |
| VDR-U01-C019 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:456 | Accessible companies will always be the | FACT | always | — | For the superuser (for example inside a cron) with no accessible branch, the company itself is returned because the superuser bypasses record rules. | N-U01-023 |
| VDR-U01-C020 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:467 | _all_branches_selected | FACT | always | — | Helper telling whether all branches, and only those, of the companies in self are selected; intended for actions that only make sense for whole companies. | N-U01-002 |
| VDR-U01-C021 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:247 | res_company_users_rel | FACT | always | — | Allowed companies of a user are the many2many company_ids (relation table res_company_users_rel), defaulting to the current env companies. | N-U01-003 |
| VDR-U01-C022 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:245 | default=lambda self: self.env.company.id | FACT | always | — | Default company_id of a user is the current environment company; field is required and labelled the default company. | N-U01-003 |
| VDR-U01-C023 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:506 | is not in the allowed companies | FACT | always | — | Constraint (company_id, company_ids, active): an active user's default company must be among company_ids. | N-U01-009 |
| VDR-U01-C024 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:726 | _get_company_ids | FACT | always | — | Allowed company ids of a user are computed by searching res.company for active companies in which the user is listed, cached by user id. | N-U01-003 |
| VDR-U01-C025 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:728 | ('active', '=', True) | FACT | always | — | Archived companies are excluded from the user's allowed companies. | N-U01-003 |
| VDR-U01-C026 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1363 | company_count <= 1 and group_multi_company_id | FACT | always | — | On create, a user with at most one company has the Multi Companies group removed if present. | N-U01-016 |
| VDR-U01-C027 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1365 | company_count > 1 | FACT | always | — | A user with more than one company gets the Multi Companies group linked (also done on write of company_ids at 1371-1381 and on new() at 1385-1397). | N-U01-016 |
| VDR-U01-C028 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:632 | reset_cached_properties(env) | FACT | always | — | Writing company_id or company_ids resets the cached env.company and env.companies on every environment of the transaction that belongs to the user. | N-U01-003 |
| VDR-U01-C029 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:192 | check_company_domain_parent_of | INFERENCE | always | — | Contacts declare _check_company_domain = check_company_domain_parent_of; core orm/models.py:169-185 (outside addons, read) accepts a related record when its company is False or an ancestor-or-self (via parent_path) of the given companies, so parent-company records are usable from branches. | N-U01-007 |
| VDR-U01-C030 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:191 | _check_company_auto = True | INFERENCE | always | — | With _check_company_auto the core ORM runs _check_company on create and write (orm/models.py:4522 and 4749, outside addons) and raises UserError listing inconsistencies ending with the text that no company crossover is allowed (orm/models.py:4103). | N-U01-008 |
| VDR-U01-C031 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:285 | company_id: ResCompany | FACT | always | — | Contact company_id is an optional many2one; an empty value means a shared contact. | N-U01-006 |
| VDR-U01-C032 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:19 | 'parent_of', company_ids | INFERENCE | always | — | The global contact rule keeps contacts whose company is an ancestor-or-self of any company in company_ids, or which have no company, or are not partner_share (see CAP-02); thus parent records are visible from branches but branch records are not visible from a parent that is not itself active. | N-U01-007 |
| VDR-U01-C033 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:173 | Domain('company_ids', 'in', company_ids) | FACT | always | — | For res.users the company consistency domain is company_ids in the given companies (users are multi-company), instead of company_id. | N-U01-008 |
| VDR-U01-C034 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:351 | check_company_domain_parent_of | FACT | always | — | Currency rates use the parent-of company domain too. | N-U01-007 |
| VDR-U01-C035 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:78 | check_company_domain_parent_of | FACT | always | — | Partner bank accounts use the parent-of company domain. | N-U01-007 |
| VDR-U01-C036 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:101 | related='partner_id.company_id' | FACT | always | — | Bank account company_id is stored, related to the account holder's company and read-only. | N-U01-006 |
| VDR-U01-C037 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:599 | self.company_id = self.parent_id.company_id.id | FACT | always | — | Onchange of parent or company sets the contact company to the parent's company. | N-U01-014 |
| VDR-U01-C038 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:909 | not compatible with the companies | FACT | always | — | Writing company_id on a contact is refused with UserError when its users do not all share exactly that company; setting company False is always allowed. | N-U01-014 |
| VDR-U01-C039 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:911 | partner.child_ids.write | FACT | always | — | A company_id write on a contact is pushed to all its child contacts. | N-U01-014 |
| VDR-U01-C040 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:585 | if partner is global we keep | FACT | always | — | On user create, a contact that has a company takes the user's company; a contact with no company stays shared. | N-U01-087 |
| VDR-U01-C041 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:150 | company_id = fields.Many2one | FACT | always | — | Sequences carry an optional company, defaulting to env.company. | N-U01-021 |
| VDR-U01-C042 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:287 | ('company_id', 'in', [company_id, False]) | FACT | always | — | next_by_code searches sequences of the current company or with no company, ordered by company so that a company-specific one wins. | N-U01-021 |
| VDR-U01-C043 | FUNCTION MAPPING REQUIRED | base/models/ir_default.py:186 | d.company_id IS NULL | FACT | always | — | Defaults apply when their company is empty or equals the current company; rows are ordered by user, company, id so the most specific wins. | N-U01-021 |
| VDR-U01-C044 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:459 | company_id = fields.Many2one | FACT | always | — | Attachments carry a company (default env.company, change_default True). | N-U01-022 |
| VDR-U01-C045 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:269 | user_preference | INFERENCE | always | — | When the user_preference context key is set (default-company field of users), company name search is done as superuser restricted to the user's own companies, so users can pick any of their allowed companies even if rules would hide some. | N-U01-003 |
| VDR-U01-C046 | FUNCTION MAPPING REQUIRED | web/models/ir_http.py:144 | disallowed_ancestor_companies_sudo | FACT | module web installed | — | session_info lists the user's allowed companies plus ancestor companies the user lacks (as disallowed ancestors) so the client can render the tree. | N-U01-018 |
| VDR-U01-C047 | FUNCTION MAPPING REQUIRED | web/static/src/core/user.js:78 | allowed_company_ids | FACT | module web installed | RT | Client puts the activated company ids (first = current) into the request context key allowed_company_ids; the cids cookie is set at line 77. | N-U01-018 |
| VDR-U01-C048 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:49 | self.env.companies.ids | INFERENCE | always | — | Record-rule variable company_ids is env.companies; core orm/environments.py:246-278 (outside addons, read) returns the allowed_company_ids context or all user companies and raises AccessError for unauthorised ids unless in sudo. | N-U01-018 |
| VDR-U01-C049 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:246 | multi-company issue | FACT | always | — | Access error text suggests switching company when a failing rule mentions company_id and the user can reach the record company (lines 233-251). | N-U01-025 |
| VDR-U01-C050 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:482 | api.Environment(job_cr | INFERENCE | always | — | Cron jobs run in an Environment for the job user with no allowed_company_ids in context, so env.companies falls back to all companies of that user (core environments.py:262-278). | N-U01-024 |
| VDR-U01-C051 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:309 | company_dependent=True | FACT | always | — | Example of a company-dependent field in base: partner barcode. | N-U01-017 |
| VDR-U01-C052 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:1838 | stored as jsonb | INFERENCE | always | — | Company-dependent fields are stored as a JSON object keyed by company id; core orm/fields.py:1014-1019 builds PsycopgJson({company id: value}) and falls back to ir.default (orm/fields.py:1001-1012). | N-U01-017 |
| VDR-U01-C053 | FUNCTION MAPPING REQUIRED | base/data/res_company_data.xml:4 | id="main_company" | OBSERVATION | restored DB | — | DB shows one company, no branch (parent_id null count 0), seeded main company with partner main_partner; res_company_users_rel has 4 rows. | N-U01-016 |
| VDR-U01-C054 | FUNCTION MAPPING REQUIRED | base/data/res_users_data.xml:8 | company_ids | OBSERVATION | restored DB | — | Seed links both built-in users to the main company; DB: 4 users all have company_id set. | N-U01-013 |
| VDR-U01-C055 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:309 | company_dependent=True | OBSERVATION | restored DB | — | DB registers 63 company-dependent fields overall, 23 on res.* models (22 on res.partner from accounting, stock, sales, purchase, product, mail apps; 1 on res.users). | N-U01-017 |
| VDR-U01-C056 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:25 | rule_group_rel | FACT | always | — | Rules link to groups via many2many groups (table rule_group_rel). | N-U01-029 |
| VDR-U01-C057 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:30 | perm_unlink = fields.Boolean | FACT | always | — | Four operation flags perm_read, perm_write, perm_create, perm_unlink default True (lines 27-30). | N-U01-028 |
| VDR-U01-C058 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:34 | Rule must have at least one | FACT | always | — | SQL CHECK: at least one of the four perm flags is true. | N-U01-036 |
| VDR-U01-C059 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:23 | disable the record rule without deleting | FACT | always | — | Help text of active: unchecking disables the rule; deleting a native rule may re-create it on module reload. | N-U01-039 |
| VDR-U01-C060 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:50 | 'company_id': self.env.company.id | FACT | always | — | Evaluation context of rule domains exposes user, company_ids (activated companies) and company_id (current company). | N-U01-035 |
| VDR-U01-C061 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:48 | self.env.user.with_context({}) | FACT | always | — | The user variable is evaluated with an empty context, making domain evaluation independent of the context. | N-U01-035 |
| VDR-U01-C062 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:56 | rule['global'] = not rule.groups | FACT | always | — | A rule is global exactly when it has no groups (stored computed field global). | N-U01-029 |
| VDR-U01-C063 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:62 | Rules can not be applied on | FACT | always | — | Constraint forbids rules whose model is ir.rule. | N-U01-036 |
| VDR-U01-C064 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:74 | Invalid domain: %s | FACT | always | — | Active rules' domain_force is safe_eval'd with the eval context and validated against the target model on save; failures raise ValidationError. | N-U01-036 |
| VDR-U01-C065 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:78 | return ['allowed_company_ids'] | FACT | always | — | Context keys used to cache rule domains: allowed_company_ids only in base. | N-U01-040 |
| VDR-U01-C066 | FUNCTION MAPPING REQUIRED | website/models/ir_rule.py:29 | ['website_id'] | FACT | module website installed | — | The website module adds website_id to the cache keys of rule domains. | N-U01-041 |
| VDR-U01-C067 | FUNCTION MAPPING REQUIRED | website/models/ir_rule.py:24 | res['website'] = is_frontend | FACT | module website installed | — | The website module adds a website variable (current website on frontend requests) to the rule evaluation context. | N-U01-041 |
| VDR-U01-C068 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:120 | if self.env.su | FACT | always | — | _get_rules returns no rules in superuser mode. | N-U01-038 |
| VDR-U01-C069 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:126 | WHERE m.model = %s AND r.active | FACT | always | — | Rules for a model and mode are selected as active, with the perm flag of the mode, and either global or linked to a group of the user (user._get_group_ids at line 132). | N-U01-033 |
| VDR-U01-C070 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:144 | add rules for parent models | FACT | always | — | For each stored _inherits parent, the parent's rule domain is added as an any-domain on the link field to the global domains. | N-U01-037 |
| VDR-U01-C071 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:152 | if not rules | FACT | always | — | With no applicable rules, only parent-model domains (if any) are returned: no record-level restriction. | N-U01-034 |
| VDR-U01-C072 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:161 | not (rule.groups & user_groups) | FACT | always | — | Rules whose groups do not intersect the user's all_group_ids are skipped in _compute_domain. | N-U01-033 |
| VDR-U01-C073 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:164 | Domain.TRUE | FACT | always | — | A rule with empty domain_force evaluates to TRUE. | N-U01-034 |
| VDR-U01-C074 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:167 | global_domains.append(dom) | FACT | always | — | Global rule domains are accumulated for AND combination; group rule domains accumulated separately (lines 165-169). | N-U01-031 |
| VDR-U01-C075 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:172 | Domain.OR(group_domains) | FACT | always | — | Group rule domains are OR-ed together; the result is appended to the global list and everything is AND-ed (line 173). | N-U01-032 |
| VDR-U01-C076 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:137 | tools.ormcache | FACT | always | — | _compute_domain is cached by uid, su, model, mode and context key values, except when dev_mode contains xml. | N-U01-040 |
| VDR-U01-C077 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:187 | self.env.registry.clear_cache() | FACT | always | — | unlink, create and write of rules clear the whole registry cache (lines 187, 196, 206). | N-U01-052 |
| VDR-U01-C078 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:84 | Can return any global rule | FACT | always | — | _get_failing documents that group rules fail as a block (they are OR-ed) while each global rule can fail individually; used only to build access error messages. | N-U01-053 |
| VDR-U01-C079 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:253 | base.group_no_one | FACT | always | — | Detailed access error with failing record names and rule names is shown only to internal users in the technical-features group; others get a generic message. | N-U01-053 |
| VDR-U01-C080 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2165 | User root have all accesses | FACT | always | — | ir.model.access.check returns True in superuser mode (model-level bypass). | N-U01-038 |
| VDR-U01-C081 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:13 | res.partner company | FACT | always | — | Global rule res_partner_rule (no groups) on res.partner for all four operations. | N-U01-044 |
| VDR-U01-C082 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:19 | partner_share | FACT | always | — | res_partner_rule keeps contacts with partner_share False (contacts of internal users), or company ancestor-or-self of company_ids, or company empty; the XML comment at lines 15-18 states internal users' contacts are always visible so users stay selectable. | N-U01-045 |
| VDR-U01-C083 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:25 | child_of', user.commercial_partner_id.id | FACT | always | — | res_partner_portal_public_rule (groups portal and public) limits contacts to the child_of tree of the user's commercial partner and is read-only (create, unlink, write False at 27-29). | N-U01-046 |
| VDR-U01-C084 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:58 | company_id', 'parent_of', company_ids | FACT | always | — | res_partner_bank_rule is global with the parent-of company or shared filter (line 59). | N-U01-044 |
| VDR-U01-C085 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:65 | company_id', 'parent_of', company_ids | FACT | always | — | res_currency_rate_rule is global with the parent-of company or shared filter. | N-U01-044 |
| VDR-U01-C086 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:145 | 'company_ids', 'in', company_ids | FACT | always | — | Global user rule: a user record is visible when it is not a share user or when the user belongs to one of the activated companies. | N-U01-044 |
| VDR-U01-C087 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:152 | commercial_partner_id', '=', user.commercial_partner_id.id | FACT | always | — | Group rule for portal on res.users: portal users see users of their own commercial partner (and, being AND-ed with the global user rule, only those). | N-U01-046 |
| VDR-U01-C088 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:113 | company rule employee | FACT | always | — | Employees, portal and public (lines 105-125) each have a group rule on res.company with id in company_ids. | N-U01-049 |
| VDR-U01-C089 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:127 | company rule erp manager | FACT | always | — | The access-rights manager group has a rule on res.company with an always-true domain, so OR-ing makes them see all companies. | N-U01-049 |
| VDR-U01-C090 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:131 | [(1,'=',1)] | INFERENCE | always | — | Because erp_manager implies user (base_groups.xml:28) and group rules are OR-ed (ir_rule.py:172), a user in both groups gets the always-true company-record domain. | N-U01-050 |
| VDR-U01-C091 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:186 | Public users can't interact with keys | FACT | always | — | api_key_public rule uses an always-false domain for public users. | N-U01-047 |
| VDR-U01-C092 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:192 | Users can read and delete their | FACT | always | — | api_key_user rule (portal and internal groups) limits API keys to user_id = user.id. | N-U01-047 |
| VDR-U01-C093 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:201 | Administrators can view user keys to | FACT | always | — | api_key_admin rule (system group) is always-true. | N-U01-047 |
| VDR-U01-C094 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:87 | ir.filter: owner or global | FACT | always | — | Saved filters visible to internal users when user_ids contains False or the user; erp_manager has an always-true rule (lines 75-84); portal and public see filters shared with them (lines 97-102). | N-U01-048 |
| VDR-U01-C095 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:33 | Defaults: alter personal defaults | FACT | always | — | ir.default: internal users limited to own defaults (read excluded); system group always-true (lines 40-46). | N-U01-048 |
| VDR-U01-C096 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:174 | res.users.settings: access their own entries | FACT | always | — | User settings limited to own record for internal users; system group always-true (lines 162-171). | N-U01-048 |
| VDR-U01-C097 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:231 | Users can read only their own | FACT | always | — | Devices and device logs limited to own records for internal users; system group sees all (lines 230-254). | N-U01-048 |
| VDR-U01-C098 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:9 | perm_read | FACT | always | — | res_users_log_rule is global with create_uid = user.id but perm_read False, so read of login log rows is not restricted by this rule (XML comment at line 4 flags it as removable). | N-U01-048 |
| VDR-U01-C099 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:137 | create_uid', '=', user.id | FACT | always | — | Identity-check and password wizards (lines 134-138, 155-159, 68-72) are global rules limiting transient records to their creator. | N-U01-048 |
| VDR-U01-C100 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:211 | user_id', 'in', [user.id, False] | FACT | always | — | Embedded actions: internal users may write or delete only their own or shared ones; system group always-true (lines 208-227, read excluded). | N-U01-048 |
| VDR-U01-C101 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:3 | noupdate="1" | OBSERVATION | restored DB | — | All 32 base rules sit in a noupdate data block; DB confirms noupdate true for the 32 ir.rule rows owned by base. | N-U01-244 |
| VDR-U01-C102 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:15 | class IrRule | OBSERVATION | restored DB | — | DB: 32 ir_rule rows owned by base (9 global, 23 group); 544 rules overall (162 global, 382 group); 144 rules mention company_id/company_ids of which 7 belong to base and 139 are global overall; names match the XML ids in base_security.xml. | N-U01-043 |
| VDR-U01-C103 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:25 | rule_group_rel | OBSERVATION | restored DB | — | DB link table rule_group_rel: base group rules reference group ids 1 (user), 2 (erp_manager), 4 (system), 10 (portal), 11 (public); each company-record rule is tied to exactly one group. | N-U01-044 |
| VDR-U01-C104 | FUNCTION MAPPING REQUIRED | n/a | class IrRule | UNKNOWN | restored DB | — | Rules contributed by other applications (512 further rows) were not studied; effective scoping per business model must be read from each application's unit. | N-U01-054 |
| VDR-U01-C105 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:69 | implied_ids = fields.Many2many | FACT | always | — | Groups imply other groups through implied_ids (table res_groups_implied_rel) with computed transitive closure all_implied_ids. | N-U01-055 |
| VDR-U01-C106 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:365 | SetDefinitions | FACT | always | — | _get_group_definitions builds a SetDefinitions of all groups (supersets from implied_ids, disjoints) cached in the groups cache. | N-U01-055 |
| VDR-U01-C107 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:79 | A user may not belong to | FACT | always | — | Disjoint groups concept: user type groups cannot be combined. | N-U01-061 |
| VDR-U01-C108 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:284 | base.group_portal | FACT | always | — | User type groups are base.group_user, base.group_portal and base.group_public (_get_user_type_groups). | N-U01-057 |
| VDR-U01-C109 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:86 | _check_user_disjoint_groups | FACT | always | — | Constraint on implied_ids and implied_by_ids re-checks all users reachable by implication for disjoint-group violations. | N-U01-061 |
| VDR-U01-C110 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:545 | cannot be at the same time | FACT | always | — | Constraint on group_ids: user.all_group_ids may contain at most one of the user type groups. | N-U01-061 |
| VDR-U01-C111 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:555 | You must have at least an | FACT | always | — | Constraint on group_ids refuses a state where base.group_system has no user_ids. | N-U01-062 |
| VDR-U01-C112 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:552 | _init_modules | FACT | always | — | The administrator-presence check returns immediately while registry._init_modules is set (base being updated). | N-U01-062 |
| VDR-U01-C113 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1081 | base.group_no_one | FACT | always | — | has_group('base.group_no_one') is true only when the user is in the group and the request session is in debug mode. | N-U01-063 |
| VDR-U01-C114 | FUNCTION MAPPING REQUIRED | base/models/ir_ui_menu.py:79 | base.group_no_one | FACT | always | — | Menu visibility ignores the technical-features group unless debug is on. | N-U01-063 |
| VDR-U01-C115 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2173 | has_access = model in self._get_allowed_models(mode) | FACT | always | — | ir.model.access.check allows a mode when the model is in the user's allowed-model set for that mode; failure raises an access error unless raise_exception False. | N-U01-059 |
| VDR-U01-C116 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2154 | a.group_id IS NULL OR | FACT | always | — | Allowed models: active entries granting the mode whose group is NULL or among the user's all group ids; the union of entries applies (any grant suffices). | N-U01-059 |
| VDR-U01-C117 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2214 | deprecated feature | FACT | always | — | Creating an access entry with no group and any granting flag logs a warning that group-less granting entries are deprecated. | N-U01-059 |
| VDR-U01-C118 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:525 | res = super()._check_access(operation) | INFERENCE | always | — | Check order seen through the attachment override: base _check_access runs first (core orm/models.py:4132-4150, outside addons: superuser skip, then ir.model.access check, then ir.rule domain filter on real records), then attachment-specific checks are added. | N-U01-060 |
| VDR-U01-C119 | FUNCTION MAPPING REQUIRED | base/models/ir_ui_menu.py:85 | ('group_ids', 'in', tuple(group_ids)) | FACT | always | — | Menus visible to a user are those with no groups or with a group in the user's groups (searched without ir.rule). | N-U01-064 |
| VDR-U01-C120 | FUNCTION MAPPING REQUIRED | base/models/ir_ui_menu.py:127 | access.check(action[model_fname], 'read', False) | FACT | always | — | A menu with an action is visible only if its window or server or report action target model is readable by the user; ancestors of visible menus are made visible. | N-U01-064 |
| VDR-U01-C121 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:168 | the user may not perform this | FACT | always | — | get_bindings drops contextual actions whose groups the user does not hold. | N-U01-065 |
| VDR-U01-C122 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:176 | the user won't be able to | FACT | always | — | get_bindings also drops actions whose res_model the user cannot read. | N-U01-065 |
| VDR-U01-C123 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:643 | groups='base.group_system' | FACT | always | — | Field-level group restriction example: the code field of server actions is limited to system administrators. | N-U01-066 |
| VDR-U01-C124 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:571 | _has_field_access | FACT | always | — | res.users overrides field read access so that a user can read their own record for fields in the self-readable list (core base _has_field_access at orm/models.py:3375-3387, outside addons, checks field.groups via has_groups and treats NO_ACCESS as always forbidden). | N-U01-066 |
| VDR-U01-C125 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:189 | SELF_WRITEABLE_FIELDS | FACT | always | — | Own-record writable list in base: signature, action_id, company_id, email, name, image_1920, lang, tz, api_key_ids, phone; readable list at lines 176-186. | N-U01-067 |
| VDR-U01-C126 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:209 | default_user_group | FACT | always | — | Default groups for new users are base.group_user plus the groups implied by base.default_user_group when it exists. | N-U01-068 |
| VDR-U01-C127 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:114 | default_user_group | FACT | always | — | The default-access template group is declared in a noupdate block (lines 113-117). | N-U01-068 |
| VDR-U01-C128 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:119 | You cannot delete a group linked | FACT | always | — | ondelete guard: groups used as implied group by a settings field cannot be deleted. | N-U01-069 |
| VDR-U01-C129 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:186 | can not start with "-" | FACT | always | — | Group names cannot start with a minus sign (write guard). | N-U01-069 |
| VDR-U01-C130 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:39 | UNIQUE (privilege_id, name) | FACT | always | — | Group names are unique within a privilege. | N-U01-069 |
| VDR-U01-C131 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:193 | call_cache_clearing_methods | FACT | always | — | Writing groups clears access caches; implied-group changes clear the groups cache (line 199). | N-U01-070 |
| VDR-U01-C132 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:449 | user.group_ids.all_implied_ids | FACT | always | — | A user's all_group_ids is the transitive closure of the explicit group_ids. | N-U01-070 |
| VDR-U01-C133 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:236 | It is not possible to remove | FACT | always | — | Inverse of all_user_ids refuses removing a user from a group they hold only through implication. | N-U01-077 |
| VDR-U01-C134 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:432 | 'group_system' if user.has_group('base.group_system') | FACT | always | — | User role selection (User or Administrator) is computed from group_system then group_user membership; onchange swaps the groups (lines 437-444). | N-U01-071 |
| VDR-U01-C135 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:28 | Command.link(ref('group_user')) | FACT | always | — | group_erp_manager implies group_user. | N-U01-075 |
| VDR-U01-C136 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:38 | group_erp_manager | FACT | always | — | group_system implies group_erp_manager and group_sanitize_override. | N-U01-075 |
| VDR-U01-C137 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:58 | implied_by_ids | FACT | always | — | group_no_one is implied by group_user and group_system, so every employee has it but it is effective only in debug. | N-U01-063 |
| VDR-U01-C138 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:65 | res_groups_privilege_export | FACT | always | — | group_allow_export (Export privilege) and group_partner_manager (Contact privilege, line 72) are implied by group_system. | N-U01-074 |
| VDR-U01-C139 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:79 | Role / Portal | FACT | always | — | Portal and public groups (lines 78-91) are dedicated type groups; public_user and the portal template user are seeded at lines 93-104. | N-U01-078 |
| VDR-U01-C140 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:99 | Portal User Template | FACT | always | — | Template portal user is inactive, in the portal group only, referenced by a config parameter (lines 98-109). | N-U01-078 |
| VDR-U01-C141 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:13 | ir_model_inherit nobody | FACT | always | — | A group-less access entry with all four permissions 0 (the six such rows are at csv lines 4, 13, 35, 39, 87 and 97). | N-U01-059 |
| VDR-U01-C142 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:14 | access_ir_model_access_group_erp_manager | FACT | always | — | erp_manager has full CRUD on ir.model.access, ir.rule (line 28) and res.groups (line 67) and res.users (line 86). | N-U01-076 |
| VDR-U01-C143 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:74 | access_res_partner_portal | FACT | always | — | Portal and public get read-only model access on res.partner (public line 73); internal users read-only (line 76); only contact-creation group can write (line 75). | N-U01-046 |
| VDR-U01-C144 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:26 | group_erp_manager | OBSERVATION | restored DB | — | DB: 119 res_groups of which 12 owned by base (group_user, group_erp_manager, group_sanitize_override, group_system, group_multi_company, group_multi_currency, group_no_one, group_allow_export, group_partner_manager, group_portal, group_public, default_user_group); 27 privileges (2 base); 110 implied-rel rows. | N-U01-072 |
| VDR-U01-C145 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:2 | access_decimal_precision_config | OBSERVATION | restored DB | — | CSV has 146 data rows; DB has 146 ir_model_access rows owned by base (all updatable) and 2010 overall; base rows per group: user 38, erp_manager 19, system 50, allow_export 1, partner_manager 9, portal 13, public 10, group-less 6. | N-U01-073 |
| VDR-U01-C146 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:35 | group_system | OBSERVATION | restored DB | — | DB implied edges: group_system implies erp_manager, sanitize_override, no_one, export, partner_manager; erp_manager implies user; portal and public imply two groups each (type isolation seeds). | N-U01-075 |
| VDR-U01-C147 | FUNCTION MAPPING REQUIRED | n/a | base.group_no_one | UNKNOWN | n/a | RT | Client-side hiding of fields and buttons from group information (group attributes in views) was not read. | N-U01-079 |
| VDR-U01-C148 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:165 | _inherits = {'res.partner': 'partner_id'} | FACT | always | — | res.users delegates contact data to res.partner through partner_id. | N-U01-080 |
| VDR-U01-C149 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:214 | required=True, ondelete='restrict' | FACT | always | — | partner_id is required with restrict on delete (a user always has a contact; the contact cannot be deleted under it). | N-U01-080 |
| VDR-U01-C150 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:252 | related='partner_id.name', inherited=True | FACT | always | — | name, email and phone are related to the contact (lines 252-255) to bypass access when the user is readable but the partner is not. | N-U01-080 |
| VDR-U01-C151 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:463 | internal_users.share = False | FACT | always | — | share is computed and stored: False when all_group_ids contains group_user, otherwise True (external). | N-U01-081 |
| VDR-U01-C152 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1167 | has_group('base.group_user') | FACT | always | — | Internal means membership of base.group_user (_is_internal); portal and public tests at 1169-1175. | N-U01-081 |
| VDR-U01-C153 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:275 | You can not have two users | FACT | always | — | SQL UNIQUE on login (case-sensitive at database level). | N-U01-083 |
| VDR-U01-C154 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:750 | Domain('login', '=', login) | FACT | always | — | Login lookup is an exact match on login. | N-U01-083 |
| VDR-U01-C155 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:79 | MIN_ROUNDS = 600_000 | FACT | always | — | Minimum work factor of password hashing is 600,000 rounds. | N-U01-084 |
| VDR-U01-C156 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1211 | max(MIN_ROUNDS | FACT | always | — | Rounds are max of 600000 and the password.hashing.rounds parameter; default scheme pbkdf2_sha512 with plaintext only for verification and migration. | N-U01-084 |
| VDR-U01-C157 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:371 | replacement is not None | FACT | always | — | A successful password check that returns a replacement hash re-stores the password and refreshes the session token. | N-U01-084 |
| VDR-U01-C158 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:922 | Setting empty passwords is not allowed | FACT | always | — | _change_password refuses empty or blank passwords. | N-U01-084 |
| VDR-U01-C159 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:219 | Keep empty if you don't want | FACT | always | — | Field help for password: keep empty if the user must not be able to connect. | N-U01-084 |
| VDR-U01-C160 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:424 | Please use the change password wizard | FACT | always | — | Setting new_password on one's own user through the field raises UserError (own change must use the wizard). | N-U01-085 |
| VDR-U01-C161 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:100 | identity-check-last | FACT | always | — | check_identity decorator lets an action run when the session identity check is younger than 10 minutes (line 100), otherwise opens the identity-check wizard; refuses use outside an HTTP request (line 97). | N-U01-085 |
| VDR-U01-C162 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1003 | @check_identity | FACT | always | — | Own password change, API key wizard (line 1012), revoke all devices (1022) and API key removal (1556) are wrapped by check_identity. | N-U01-085 |
| VDR-U01-C163 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1482 | don't keep temporary passwords | FACT | always | — | The change-password wizard clears the temporary new_passwd values after use. | N-U01-086 |
| VDR-U01-C164 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:132 | access_change_password_wizard | FACT | always | — | Change-password wizard and its lines are accessible to erp_manager (lines 132-133). | N-U01-086 |
| VDR-U01-C165 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:584 | setting_vals.append | FACT | always | — | On create, internal users get a res.users.settings record. | N-U01-087 |
| VDR-U01-C166 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:591 | _avatar_generate_svg | FACT | always | — | Internal users without image get a generated initials avatar (lines 589-591). | N-U01-087 |
| VDR-U01-C167 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:598 | You cannot activate the superuser | FACT | always | — | write refuses activating the superuser (id 1) and refuses archiving the current user (line 600). | N-U01-088 |
| VDR-U01-C168 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:603 | unarchive partners before unarchiving the users | FACT | always | — | Activating a user first unarchives the related contact. | N-U01-088 |
| VDR-U01-C169 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:652 | You can not remove the admin | FACT | always | — | ondelete guard: superuser (652), user_admin (655), portal template user (658) and public user (660) cannot be deleted. | N-U01-089 |
| VDR-U01-C170 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:870 | cannot archive contacts linked to an | FACT | always | — | Archiving a contact that has a linked user raises RedirectWarning (or ValidationError without user write access). | N-U01-090 |
| VDR-U01-C171 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:956 | cannot delete contacts linked | FACT | always | — | Deleting a contact that has a linked user raises RedirectWarning or ValidationError. | N-U01-090 |
| VDR-U01-C172 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:946 | Only the portal users can delete | FACT | always | — | _deactivate_portal_user is refused for non-share (internal) users. | N-U01-091 |
| VDR-U01-C173 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:967 | api_key_ids._remove() | FACT | always | — | Portal self-deletion replaces login and clears password (lines 963-966), removes API keys, archives user then contact (979-985) and queues res.users.deletion (987). | N-U01-091 |
| VDR-U01-C174 | FUNCTION MAPPING REQUIRED | base/models/res_users_deletion.py:37 | batch_size=50 | FACT | always | — | The cron method _gc_portal_users deletes queued users in batches of 50 with progress commits, then tries to delete the contact (85-100) and keeps it on failure. | N-U01-091 |
| VDR-U01-C175 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1302 | base.login_cooldown_after | FACT | always | — | Cooldown threshold parameter, default 5 when absent (0 disables); duration parameter default 60 seconds (line 1306). | N-U01-092 |
| VDR-U01-C176 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1228 | not shared between workers | FACT | always | — | Docstring: login failure counters are not shared between workers nor thread-safe; stored in registry._login_failures by remote address (lines 1247-1253). | N-U01-105 |
| VDR-U01-C177 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1272 | Too many login failures | FACT | always | — | During cooldown an attempt raises AccessDenied without checking credentials. | N-U01-092 |
| VDR-U01-C178 | FUNCTION MAPPING REQUIRED | base/models/ir_config_parameter.py:23 | base.login_cooldown_after | FACT | always | — | At database creation the seeded cooldown values are 10 failures and 60 seconds (lines 23-24). | N-U01-092 |
| VDR-U01-C179 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:830 | return {'id', 'login', 'password', 'active'} | FACT | always | — | Session token fields: id, login, password hash, active; token is an HMAC of the session id keyed by these values plus database secret (lines 832-884); other modules extend the set. | N-U01-093 |
| VDR-U01-C180 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:746 | res.users.log | FACT | always | — | Each successful login creates a res.users.log row via _update_last_login. | N-U01-094 |
| VDR-U01-C181 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:144 | _gc_user_logs | FACT | always | — | Autovacuum deletes log rows older than the latest row of the same user. | N-U01-094 |
| VDR-U01-C182 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1836 | Only internal users can create API | FACT | always | — | check_access_make_key raises AccessError for non-internal users. | N-U01-095 |
| VDR-U01-C183 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1585 | max(group.api_key_duration | FACT | always | — | Maximum API key lifetime for non-system users is the max api_key_duration over their groups, falling back to 1 day; the expiry must be future and not exceed it (lines 1586-1589). | N-U01-095 |
| VDR-U01-C184 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:45 | api_key_duration | FACT | always | — | group_user carries api_key_duration 90 days. | N-U01-095 |
| VDR-U01-C185 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1584 | The API key must have an | FACT | always | — | Non-system users must set an expiry; system users may create keys without expiry (line 1581). | N-U01-095 |
| VDR-U01-C186 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1606 | binascii.hexlify(os.urandom(API_KEY_SIZE)) | FACT | always | — | Key is 20 random bytes in hex; only its pbkdf2 hash (line 1612) and an 8-hex index are stored. | N-U01-095 |
| VDR-U01-C187 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1715 | DELETE FROM %s | FACT | always | — | Autovacuum _gc_user_apikeys deletes keys with expiration in the past. | N-U01-095 |
| VDR-U01-C188 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1632 | base.enable_programmatic_api_keys | FACT | always | — | Programmatic key generation or revocation requires the parameter (default False) unless system user (1633). | N-U01-096 |
| VDR-U01-C189 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1516 | DEFAULT_PROGRAMMATIC_API_KEYS_LIMIT = 10 | FACT | always | — | Default cap of 10 live keys for programmatic creation; configurable by base.programmatic_api_keys_limit (line 1665). | N-U01-096 |
| VDR-U01-C190 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:612 | del vals['company_id'] | FACT | always | — | When a user writes only self-writable fields on themselves, a company_id not among their own companies is silently dropped, and the write is done as superuser. | N-U01-097 |
| VDR-U01-C191 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:807 | web.base.url.freeze | FACT | always | — | On successful authentication of a system user with a base_location, web.base.url is set from the request unless web.base.url.freeze is set. | N-U01-098 |
| VDR-U01-C192 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:516 | App Switcher | FACT | always | — | Home action constraint: not the app switcher, not a reload client action, not an act_window whose context needs active_id. | N-U01-103 |
| VDR-U01-C193 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:356 | _rpc_api_keys_only | FACT | always | — | _check_credentials: password checked for interactive logins; for non-interactive RPC an API key is accepted (line 387-394) and password use may be disabled by modules that return True from _rpc_api_keys_only. | N-U01-100 |
| VDR-U01-C194 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1313 | _mfa_type | FACT | always | — | Base MFA hooks return nothing; second factors come from auth_totp and similar modules (not studied). | N-U01-100 |
| VDR-U01-C195 | FUNCTION MAPPING REQUIRED | base_setup/models/res_users.py:17 | Discuss application | FACT | module base_setup installed | — | web_create_users (invitation by email) raises UserError when the email_normalized field (from the discussion app) is absent. | N-U01-101 |
| VDR-U01-C196 | FUNCTION MAPPING REQUIRED | mail/models/res_users.py:156 | SELF_READABLE_FIELDS | FACT | module mail installed | — | mail and other apps (hr, calendar, im_livechat, sale_stock, hr_holidays...) override SELF_READABLE_FIELDS or SELF_WRITEABLE_FIELDS to widen self access. | N-U01-102 |
| VDR-U01-C197 | FUNCTION MAPPING REQUIRED | base/data/res_users_data.xml:16 | <field name="password"> | FACT | always | — | Seed data assigns a literal default password to the administrator account when the database is initialised. | N-U01-104 |
| VDR-U01-C198 | FUNCTION MAPPING REQUIRED | base/data/res_users_data.xml:14 | id="user_admin" | OBSERVATION | restored DB | — | DB: 4 res_users: 1 active internal user (administrator), 1 archived internal (technical superuser), 2 archived external (public user and portal template); superuser and public contact are archived. | N-U01-089 |
| VDR-U01-C199 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:1303 | min_failures | OBSERVATION | restored DB | — | DB parameters: base.login_cooldown_after 10, base.login_cooldown_duration 60. | N-U01-092 |
| VDR-U01-C200 | FUNCTION MAPPING REQUIRED | n/a | from __future__ import annotations | UNKNOWN | n/a | RT | Whether the administrator default password was changed in the reference DB was not examined (credential values are out of scope); authentication modules (totp, passkey, oauth, ldap, signup) were not read. | N-U01-107 |
| VDR-U01-C201 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:255 | ('contact', 'Contact') | FACT | always | — | Address type selection: contact, invoice, delivery, other (default contact). | N-U01-109 |
| VDR-U01-C202 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:215 | parent_id: ResPartner | FACT | always | — | Contacts have parent_id (Related Company) and child_ids (line 217); is_company flag at line 277. | N-U01-109 |
| VDR-U01-C203 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:328 | Contacts require a name | FACT | always | — | SQL CHECK: name required when type is contact. | N-U01-112 |
| VDR-U01-C204 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:195 | _complete_name_displayed_types | FACT | always | — | Complete name shows the type label (invoice, delivery, other) when a child has no name. | N-U01-112 |
| VDR-U01-C205 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:549 | recursive Partner hierarchies | FACT | always | — | Constraint on parent_id: cycle detection. | N-U01-113 |
| VDR-U01-C206 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:520 | partner.parent_id.commercial_partner_id | FACT | always | — | commercial_partner_id is self for companies and parentless contacts, otherwise the parent's commercial partner (stored, recursive). | N-U01-114 |
| VDR-U01-C207 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:693 | ['company_registry', 'industry_id'] | FACT | always | — | Commercial fields are the synced ones plus company_registry and industry_id. | N-U01-115 |
| VDR-U01-C208 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:700 | return ['vat'] | FACT | always | — | Synced commercial fields in base: vat only. | N-U01-115 |
| VDR-U01-C209 | FUNCTION MAPPING REQUIRED | account/models/partner.py:718 | credit_limit | FACT | module account installed | — | Accounting adds payment terms, accounts, fiscal position and credit limit to commercial fields. | N-U01-115 |
| VDR-U01-C210 | FUNCTION MAPPING REQUIRED | product/models/res_partner.py:50 | specific_property_product_pricelist | FACT | module product installed | — | Product adds the specific price list to the synced commercial fields. | N-U01-115 |
| VDR-U01-C211 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:726 | _commercial_sync_from_company | FACT | always | — | When a parent commercial entity is set, commercial values are copied down to the child and its descendants; company-dependent ones are synced across companies (737-749). | N-U01-116 |
| VDR-U01-C212 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:801 | commercial_to_upstream | FACT | always | — | Synced commercial fields edited on a non-commercial contact are written up to its parent, which triggers downstream sync. | N-U01-116 |
| VDR-U01-C213 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:791 | address_to_upstream | FACT | always | — | For type contact children with a parent, address changes are written to the parent (and from there down to contact-type children, 823-827). | N-U01-116 |
| VDR-U01-C214 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:829 | _handle_first_contact_creation | FACT | always | — | First contact created under a parentless-address company copies its address to the company. | N-U01-116 |
| VDR-U01-C215 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:202 | Add the company of the parent | FACT | always | — | default_get takes the parent's company_id for a child contact. | N-U01-117 |
| VDR-U01-C216 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:420 | Synchronize sales rep with parent | FACT | always | — | A person without salesperson inherits the parent's user_id; lang is also taken from the parent (lines 397-405). | N-U01-117 |
| VDR-U01-C217 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:455 | active_test = False because | FACT | always | — | Duplicate vat detection searches including archived contacts (comment lines 455-456). | N-U01-118 |
| VDR-U01-C218 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:466 | EU_EXTRA_VAT_CODES | FACT | always | — | VAT duplicate search adds prefix variants for EU countries. | N-U01-118 |
| VDR-U01-C219 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:237 | You can use '/' to indicate | FACT | always | — | A single-character vat (slash) means no tax id and skips the duplicate check (line 459). | N-U01-118 |
| VDR-U01-C220 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:487 | same_company_registry_partner_id | FACT | always | — | Registry duplicate detection is a non-stored computed hint (company_registry equal, company same or empty). | N-U01-118 |
| VDR-U01-C221 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:326 | _check_name = models.Constraint | INFERENCE | always | — | The only hard constraints on contacts in base are the name check (326), parent cycle (546), company match (551) and barcode uniqueness (647); no unique constraint exists on vat, ref, email or name. | N-U01-118 |
| VDR-U01-C222 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:651 | Another partner already has this barcode | FACT | always | — | Constraint: partner barcode unique across partners (search_count > 1). | N-U01-119 |
| VDR-U01-C223 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:108 | Account Number/Partner must be unique | FACT | always | — | SQL unique (sanitized_acc_number, partner_id). | N-U01-120 |
| VDR-U01-C224 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:12 | re.sub(r'\W+', '', acc_number).upper() | FACT | always | — | Account numbers are sanitised (non-word characters removed, upper-cased) for storage and search. | N-U01-120 |
| VDR-U01-C225 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:94 | partner_id = fields.Many2one | FACT | always | — | Account holder is required, ondelete cascade, field domain restricts to companies or parentless contacts. | N-U01-120 |
| VDR-U01-C226 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:176 | we want to archive it | FACT | always | — | unlink on a bank account archives it instead of deleting. | N-U01-120 |
| VDR-U01-C227 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:95 | allow_out_payment | FACT | always | — | Send-money flag defaults False and is not copied. | N-U01-120 |
| VDR-U01-C228 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:887 | bank.acc_holder_name = vals['name'] | FACT | always | — | Renaming a contact updates bank account holder names that matched the old name. | N-U01-120 |
| VDR-U01-C229 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:210 | Please add your own bank account | FACT | always | — | _find_or_create_bank_account refuses to create accounts for the database's own company contacts unless allow_company_account_creation. | N-U01-121 |
| VDR-U01-C230 | FUNCTION MAPPING REQUIRED | base/models/res_bank.py:206 | child_of | FACT | always | — | It first searches (including archived) accounts under the commercial partner tree. | N-U01-121 |
| VDR-U01-C231 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:956 | cannot delete contacts linked | FACT | always | — | Delete guard on contacts with linked users (and archive guard at line 870). | N-U01-122 |
| VDR-U01-C232 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:428 | cannot merge more than 3 contacts | FACT | always | — | Merge refuses more than 3 contacts. | N-U01-123 |
| VDR-U01-C233 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:435 | cannot merge a contact with one | FACT | always | — | Merge refuses sets that contain a contact and one of its descendants. | N-U01-123 |
| VDR-U01-C234 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:439 | linked to more than one user | FACT | always | — | Merge refuses contacts linked to more than one user (including archived). | N-U01-123 |
| VDR-U01-C235 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:442 | All contacts must have the same | FACT | always | — | Different emails are refused unless extra_checks is False; is_admin() disables the check (line 419). | N-U01-123 |
| VDR-U01-C236 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:449 | ordered_partners[-1] | FACT | always | — | Default destination is the last of the ordered list; ordering key puts inactive first and newest first when reversed (line 561), so the last is the oldest active contact. | N-U01-123 |
| VDR-U01-C237 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:453 | Make the company of all related | FACT | always | — | If the destination has a company, all users of the merged contacts are linked to it and set to it as default company. | N-U01-124 |
| VDR-U01-C238 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:461 | _merge_bank_accounts(src_partners, dst_partner) | FACT | always | — | Bank accounts of sources are moved to the destination; duplicates (same sanitised number) are redirected and the source account deleted (396-410). | N-U01-124 |
| VDR-U01-C239 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:177 | updating fails, most likely due to | FACT | always | — | Foreign key repointing runs in savepoints; on unique violation the dependent rows are deleted (line 179-180). | N-U01-124 |
| VDR-U01-C240 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:214 | update_records('mail.followers' | FACT | always | — | Attachments, followers, activities, messages and external identifiers are repointed (lines 213-217); stored reference fields too (223-240). | N-U01-124 |
| VDR-U01-C241 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:241 | company_dependent fields referring the merged records | FACT | always | — | JSON company-dependent many2one values and ir.default fallbacks are rewritten to the destination (241-284); source company-dependent values fill the destination (288-316). | N-U01-124 |
| VDR-U01-C242 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:357 | get all fields that are not | FACT | always | — | Field merge: later non-empty values override; summable fields (empty by default, line 335-338) are added. | N-U01-124 |
| VDR-U01-C243 | FUNCTION MAPPING REQUIRED | account/wizard/base_partner_merge.py:11 | customer_rank | FACT | module account installed | — | Accounting adds customer_rank and supplier_rank as summable merge fields. | N-U01-124 |
| VDR-U01-C244 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:473 | src_partners.sudo().unlink() | FACT | always | — | Source contacts are deleted after merge (log line at 475-476). | N-U01-124 |
| VDR-U01-C245 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:517 | HAVING COUNT(*) >= 2 | FACT | always | — | Duplicate groups are found by grouping lower(email), lower(name), spaceless vat, is_company or parent (lines 483-524) with a maximum group count. | N-U01-125 |
| VDR-U01-C246 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:680 | self.env.cr.commit() | FACT | always | — | Automatic merge commits after each group; parent_migration_process_cb also commits (line 725). | N-U01-132 |
| VDR-U01-C247 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:142 | access_base_partner_merge_automatic_wizard | FACT | always | — | Merge wizard models are granted to group_partner_manager (lines 141-142). | N-U01-126 |
| VDR-U01-C248 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:569 | "%s (copy)" | FACT | always | — | copy_data appends (copy) to the name unless name given. | N-U01-129 |
| VDR-U01-C249 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:562 | does not match the company this | FACT | always | — | Constraint: a contact that is a company's partner must have that company as its own company_id. | N-U01-131 |
| VDR-U01-C250 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:251 | active = fields.Boolean(default=True) | FACT | always | — | Contacts are archived via active; duplicate warnings include archived contacts. | N-U01-127 |
| VDR-U01-C251 | FUNCTION MAPPING REQUIRED | base_vat/models/res_partner.py:92 | _inherit = 'res.partner' | OBSERVATION | restored DB | — | base_vat (VAT format validation) exists in source but is not in the 356 installed modules of the reference DB, so country VAT format checks are not active there. | N-U01-128 |
| VDR-U01-C252 | FUNCTION MAPPING REQUIRED | base/data/res_partner_data.xml:4 | id="main_partner" | OBSERVATION | restored DB | — | DB: 7 contacts (base seeds 5: 4 noupdate), 0 bank accounts, 22 company-dependent fields on contact added by other apps. | N-U01-130 |
| VDR-U01-C253 | FUNCTION MAPPING REQUIRED | n/a | def _merge | UNKNOWN | n/a | RT | Behaviour of installed address, autocomplete and country modules on contact validation was not studied; merge behaviour under real data needs runtime confirmation. | N-U01-134 |
| VDR-U01-C254 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:680 | self.env.cr.commit() | INFERENCE | always | RT | A partial automatic merge cannot be undone and interruption leaves earlier groups committed (inferred from commit at 680 and deletion at 473). | N-U01-132 |
| VDR-U01-C255 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:237 | string='Tax ID' | INFERENCE | always | — | No uniqueness enforcement on vat leaves duplicates possible and relies on the soft warning (lines 450-487). | N-U01-133 |
| VDR-U01-C256 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:27 | size=3 | FACT | always | — | Currency name holds a 3-character ISO code; symbol required (line 30); rounding default 0.01 (line 37); position after or before (line 42). | N-U01-135 |
| VDR-U01-C257 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:376 | company_id = fields.Many2one | FACT | always | — | Rate company defaults to the current company's root. | N-U01-142 |
| VDR-U01-C258 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:51 | The currency code must be unique! | FACT | always | — | SQL unique on currency name. | N-U01-138 |
| VDR-U01-C259 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:55 | The rounding factor must be greater | FACT | always | — | SQL CHECK rounding > 0. | N-U01-138 |
| VDR-U01-C260 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:166 | math.ceil(math.log10(1/currency.rounding)) | FACT | always | — | decimal_places is derived from rounding (0 for rounding of 1 or more). | N-U01-138 |
| VDR-U01-C261 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:223 | float_round(amount, precision_rounding=self.rounding) | FACT | always | — | round() uses the rounding factor. | N-U01-139 |
| VDR-U01-C262 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:246 | float_compare(amount1, amount2 | FACT | always | — | compare_amounts compares after rounding; is_zero (261) uses rounding too; the docstring warns is_zero(a-b) differs from compare_amounts. | N-U01-139 |
| VDR-U01-C263 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:381 | Only one currency rate per day | FACT | always | — | SQL unique (name, currency_id, company_id). | N-U01-140 |
| VDR-U01-C264 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:385 | must be strictly positive | FACT | always | — | SQL CHECK rate > 0. | N-U01-140 |
| VDR-U01-C265 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:359 | Technical Rate | FACT | always | — | Stored rate is the technical rate relative to the currency of rate 1; company_rate and inverse_company_rate are computed views relative to the company currency (lines 361-370, 428-455). | N-U01-141 |
| VDR-U01-C266 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:462 | abs(diff) > 0.2 | FACT | always | — | Onchange warns when a new rate differs by more than 20% from the latest rate. | N-U01-141 |
| VDR-U01-C267 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:477 | Currency rates should only be created | FACT | always | — | Constraint: rate company must have no parent (root company). | N-U01-142 |
| VDR-U01-C268 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:276 | rates only ever live on the | FACT | always | — | _get_conversion_rate resolves the company to its root_id. | N-U01-142 |
| VDR-U01-C269 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:129 | order='company_id.id, name DESC' | FACT | always | — | Rate lookup: latest rate at or before date for the root company or shared (company_id in False, root) with company-specific preferred by ordering. | N-U01-143 |
| VDR-U01-C270 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:131 | rate_fallback | FACT | always | — | If no rate on or before the date, the earliest rate of the currency for that company scope is used. | N-U01-143 |
| VDR-U01-C271 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:138 | COALESCE((%s), (%s), 1.0) | FACT | always | — | If neither exists the rate is 1.0. | N-U01-143 |
| VDR-U01-C272 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:155 | currency_rates.get(currency.id) or 1.0 | FACT | always | — | Current rate = rate of currency / rate of the target currency (company currency by default). | N-U01-143 |
| VDR-U01-C273 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:303 | to_currency.round(to_amount) if round else to_amount | FACT | always | — | _convert rounds to the target currency unless round False; zero amounts return 0.0 (line 300). | N-U01-144 |
| VDR-U01-C274 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:118 | cannot be deactivated | FACT | always | — | Constraint on active refuses archiving a currency set on a company (skipped in install_mode or with force_deactivate). | N-U01-145 |
| VDR-U01-C275 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:331 | selected currencies are enabled | FACT | always | — | Creating a company activates its currency; write of currency_id also reactivates (lines 360-363). | N-U01-145 |
| VDR-U01-C276 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:89 | active_currency_count > 1 | FACT | always | — | More than one active currency applies group_multi_currency as implied group of group_user; at most one removes it (lines 83-106). | N-U01-147 |
| VDR-U01-C277 | FUNCTION MAPPING REQUIRED | product/models/res_currency.py:13 | group_product_pricelist | FACT | module product installed | — | Product also applies the price-list group and creates price lists when multi-currency turns on; archiving a currency archives its price lists (22-23). | N-U01-147 |
| VDR-U01-C278 | FUNCTION MAPPING REQUIRED | account/models/res_currency.py:31 | cannot reduce the number of decimal | FACT | module account installed | — | Accounting forbids lowering a currency's decimals once used in move lines. | N-U01-149 |
| VDR-U01-C279 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:59 | access_res_currency_public | FACT | always | — | Currencies and rates readable by public, portal and internal (lines 59-64); write only system group (65-66). | N-U01-150 |
| VDR-U01-C280 | FUNCTION MAPPING REQUIRED | spreadsheet/models/res_currency_rate.py:8 | _get_rate_for_spreadsheet | INFERENCE | module spreadsheet installed | — | Only reading helpers for rates were found outside base and accounting; no rate-download provider was found in Community modules examined (search of res.currency.rate users). | N-U01-148 |
| VDR-U01-C281 | FUNCTION MAPPING REQUIRED | base/data/res_company_data.xml:7 | base.USD | OBSERVATION | restored DB | — | Base seeds the main company with USD; DB shows company currency THB, so the seed was altered after installation. | N-U01-152 |
| VDR-U01-C282 | FUNCTION MAPPING REQUIRED | base/data/res_currency_data.xml:5 | id="USD" | OBSERVATION | restored DB | — | DB: 170 currencies, 2 active (THB, USD) both rounding 0.01 / 2 decimals; res_currency_rate has 0 rows; base seeds no rate-update cron (only 2 base crons). | N-U01-136 |
| VDR-U01-C283 | FUNCTION MAPPING REQUIRED | base/data/ir_cron_data.xml:3 | autovacuum_job | OBSERVATION | restored DB | — | None of the 54 DB cron names concerns exchange rates. | N-U01-148 |
| VDR-U01-C284 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:272 | _get_conversion_rate | INFERENCE | always | — | No rates present means 1.0 silently (coalesce at line 138), inferred from the code only; runtime confirmation needed. | N-U01-151 |
| VDR-U01-C285 | FUNCTION MAPPING REQUIRED | n/a | class ResCurrency | UNKNOWN | n/a | RT | Accounting-side revaluation and rate use on documents belongs to the accounting unit. | N-U01-153 |
| VDR-U01-C286 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:134 | 'no gap' implementation | FACT | always | — | Implementation selection standard or no_gap with help text: no-gap never skips an assigned number but is slower and gaps remain when records are deleted. | N-U01-156 |
| VDR-U01-C287 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:157 | gaps-allowed PostgreSQL sequence | FACT | always | — | Standard implementation creates a PostgreSQL sequence ir_sequence_NNN (line 162) whose nextval is not rolled back. | N-U01-156 |
| VDR-U01-C288 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:54 | SELECT nextval | FACT | always | — | Standard draw uses nextval. | N-U01-156 |
| VDR-U01-C289 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:204 | _update_nogap(self, self.number_increment) | FACT | always | — | No-gap draw increments number_next in the row inside the transaction. | N-U01-156 |
| VDR-U01-C290 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:61 | FOR UPDATE NOWAIT | FACT | always | — | No-gap draw locks the sequence row with NOWAIT: a concurrent transaction fails immediately instead of waiting. | N-U01-166 |
| VDR-U01-C291 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:237 | Invalid prefix or suffix for sequence | FACT | always | — | Prefix and suffix interpolated with date placeholders; invalid placeholders raise UserError at draw time. | N-U01-157 |
| VDR-U01-C292 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:219 | 'year': '%Y' | FACT | always | — | Placeholders year, month, day, y, doy, woy, weekday, h24, h12, min, sec, isoyear, isoy, isoweek, each also with range_ and current_ prefixes (lines 218-228). | N-U01-157 |
| VDR-U01-C293 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:246 | date_from = '{}-01-01' | FACT | always | — | Auto-created date range spans the calendar year of the requested date. | N-U01-158 |
| VDR-U01-C294 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:252 | date_range.date_to + timedelta(days=1) | FACT | always | — | New range boundaries are trimmed to avoid overlapping existing ranges (lines 248-253). | N-U01-158 |
| VDR-U01-C295 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:269 | seq_date = self._create_date_range_seq(dt) | FACT | always | — | With use_date_range and no range for the date, one is created on the fly (as superuser create at 254). | N-U01-158 |
| VDR-U01-C296 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:289 | No ir.sequence has been found for | FACT | always | — | next_by_code returns False (debug log only) when no sequence matches. | N-U01-159 |
| VDR-U01-C297 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:16 | Step must not be zero | FACT | always | — | Zero step is refused when creating or altering the underlying counter (lines 15-16, 33-34). | N-U01-160 |
| VDR-U01-C298 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:185 | _drop_sequences | FACT | always | — | Changing implementation from standard drops the PostgreSQL sequences; from no-gap creates them (lines 188-194). | N-U01-160 |
| VDR-U01-C299 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:275 | self.browse().check_access('read') | FACT | always | — | next_by_id and next_by_code require read access on ir.sequence; no company filter in next_by_id. | N-U01-161 |
| VDR-U01-C300 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:29 | access_ir_sequence_group_user | FACT | always | — | Internal users read-only, system group full on ir.sequence (29-30) and date ranges (31-32). | N-U01-161 |
| VDR-U01-C301 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:140 | number_next = fields.Integer | FACT | always | — | number_next default 1; number_next_actual is computed from the PostgreSQL sequence or the row and writable (lines 141-144). | N-U01-162 |
| VDR-U01-C302 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:152 | use_date_range | FACT | always | — | Date ranges optional per sequence. | N-U01-163 |
| VDR-U01-C303 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:93 | _name = 'ir.sequence' | OBSERVATION | restored DB | — | DB: 34 sequences; 0 owned by base; 14 owned by stock, purchase, sale, account and others; 20 without external id (warehouse-created); 2 no_gap; 1 with date ranges; 0 date-range rows; 13 with no company. | N-U01-164 |
| VDR-U01-C304 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:150 | company_id = fields.Many2one | OBSERVATION | restored DB | — | DB: no ir.rule exists for ir.sequence or ir.sequence.date_range. | N-U01-165 |
| VDR-U01-C305 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:273 | def next_by_id | INFERENCE | always | — | next_by_id draws any sequence the user can read regardless of company (lines 273-276, no company filter). | N-U01-167 |
| VDR-U01-C306 | FUNCTION MAPPING REQUIRED | n/a | FOR UPDATE NOWAIT | UNKNOWN | n/a | RT | Which applications use gap-free numbering for legal reasons was not determined here. | N-U01-168 |
| VDR-U01-C307 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:104 | _inherits = {'ir.actions.server' | FACT | always | — | ir.cron delegates to an ir.actions.server row (ir_actions_server_id required, restrict). | N-U01-169 |
| VDR-U01-C308 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:113 | interval_type = fields.Selection | FACT | always | — | Interval units: minutes, hours, days, weeks, months; interval_number default 1; nextcall required; lastcall; priority 5 default. | N-U01-169 |
| VDR-U01-C309 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:110 | Scheduler User | FACT | always | — | user_id (scheduler user) required, default current user. | N-U01-173 |
| VDR-U01-C310 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:287 | nextcall <= %(now)s | FACT | always | — | Ready: active and (nextcall passed or a trigger row with call_at passed). | N-U01-171 |
| VDR-U01-C311 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:303 | ORDER BY failure_count, priority, id | FACT | always | — | Ready jobs are ordered by consecutive failures, priority, id. | N-U01-171 |
| VDR-U01-C312 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:365 | FOR NO KEY UPDATE SKIP LOCKED | FACT | always | — | Job acquisition locks the row with SKIP LOCKED so two workers never run the same job (explained in comments 324-347). | N-U01-172 |
| VDR-U01-C313 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:228 | processed by another worker | FACT | always | — | A serialization failure or a taken job is skipped and the loop continues. | N-U01-172 |
| VDR-U01-C314 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:426 | env = api.Environment(cron_cr, job['user_id'], {}) | FACT | always | — | Job runs as the job user_id with empty context. | N-U01-173 |
| VDR-U01-C315 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:483 | 'lastcall': job['lastcall'] | FACT | always | — | Context passed to the action: lastcall, cron_id, cron_end_time (lines 482-486). | N-U01-173 |
| VDR-U01-C316 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:688 | self.env['ir.actions.server'].browse(server_action_id).run() | FACT | always | — | _callback runs the server action in the job's environment, then flushes, signals and commits; any exception rolls back and re-raises. | N-U01-173 |
| VDR-U01-C317 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:496 | loop_count < MIN_RUNS_PER_JOB | FACT | always | — | The action is looped while status is undetermined until at least 10 runs and 10 seconds (constants lines 33-34). | N-U01-174 |
| VDR-U01-C318 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:667 | INSERT INTO ir_cron_trigger | FACT | always | — | Partially done jobs are re-queued with an immediate trigger; fully done and failed jobs are rescheduled later (_reschedule_later at 635). | N-U01-174 |
| VDR-U01-C319 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:431 | CONSECUTIVE_TIMEOUT_FOR_FAILURE | FACT | always | — | Three consecutive timeouts with no progress make the next run count as failed without executing. | N-U01-175 |
| VDR-U01-C320 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:819 | timed_out_counter + 1 | FACT | always | — | Each started run pre-increments the timeout counter in a progress row (committed before running). | N-U01-175 |
| VDR-U01-C321 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:36 | MIN_FAILURE_COUNT_BEFORE_DEACTIVATION = 5 | FACT | always | — | Deactivation thresholds: 5 failures and 7 days (line 37). | N-U01-176 |
| VDR-U01-C322 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:599 | has been deactivated after failing | FACT | always | — | On deactivation the admin is notified via _notify_admin (base logs a warning, line 396). | N-U01-176 |
| VDR-U01-C323 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:391 | The base implementation of this method | FACT | always | — | Base _notify_admin only logs; real notification is supplied by overrides. | N-U01-188 |
| VDR-U01-C324 | FUNCTION MAPPING REQUIRED | mail/models/ir_cron.py:17 | channel_admin | FACT | module mail installed | — | With mail installed, admin notifications are posted to the admin channel. | N-U01-176 |
| VDR-U01-C325 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:607 | failure_count = 0 | FACT | always | — | Non-failed statuses reset failure_count and first_failure_date. | N-U01-177 |
| VDR-U01-C326 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:642 | Use the timezone of the user | FACT | always | — | Next call advances by the interval in the user's timezone to keep the hour across DST (lines 640-650). | N-U01-177 |
| VDR-U01-C327 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:273 | MAX_FAIL_TIME | FACT | always | — | Jobs are skipped while modules are installing or upgrading, unless the oldest job is older than 5 hours, in which case module states are reset (281). | N-U01-178 |
| VDR-U01-C328 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:251 | raise BadVersion() | FACT | always | — | Skipped when the base latest_version differs from the code version. | N-U01-178 |
| VDR-U01-C329 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:166 | already executing | FACT | always | — | Manual run is refused when the job is locked; method_direct_trigger requires write access (line 159) and runs _process_job with a new cursor. | N-U01-179 |
| VDR-U01-C330 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:703 | currently being executed and may not | FACT | always | — | write and unlink refuse changes while the cron is locked by a running worker (697-719). | N-U01-180 |
| VDR-U01-C331 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:629 | DELETE FROM ir_cron_trigger | FACT | always | — | Past triggers of a job are cleared when it starts. | N-U01-181 |
| VDR-U01-C332 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:910 | relativedelta(weeks=-1) | FACT | always | — | Autovacuum removes triggers older than a week of inactive crons. | N-U01-181 |
| VDR-U01-C333 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:725 | database.is_neutralized | FACT | always | — | toggle() does nothing on neutralised databases so crons cannot be re-enabled by side effects. | N-U01-183 |
| VDR-U01-C334 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:126 | interval number must be a strictly | FACT | always | — | SQL CHECK interval_number > 0. | N-U01-186 |
| VDR-U01-C335 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:5 | access_ir_cron_group_cron | FACT | always | — | Cron, cron progress and trigger models are system-group only (5-7). | N-U01-186 |
| VDR-U01-C336 | FUNCTION MAPPING REQUIRED | base/data/ir_cron_data.xml:3 | autovacuum_job | FACT | always | — | Base seeds Auto-vacuum (daily, priority 3, model._run_vacuum_cleaner) and Portal Users Deletion (daily, priority 8, batch 50, line 17). | N-U01-184 |
| VDR-U01-C337 | FUNCTION MAPPING REQUIRED | base/models/ir_autovacuum.py:42 | random.shuffle(all_methods) | FACT | always | — | Autovacuum collects all @api.autovacuum methods and runs them in random order, re-queuing those that report remaining work. | N-U01-184 |
| VDR-U01-C338 | FUNCTION MAPPING REQUIRED | base/models/ir_autovacuum.py:33 | AccessDenied() | FACT | always | — | Autovacuum refuses unless the caller is admin and a cron_id is in context. | N-U01-185 |
| VDR-U01-C339 | FUNCTION MAPPING REQUIRED | base/models/ir_autovacuum.py:62 | self.env.cr.rollback() | FACT | always | — | A failing vacuum method is logged and rolled back; the loop continues. | N-U01-185 |
| VDR-U01-C340 | FUNCTION MAPPING REQUIRED | base/data/ir_cron_data.xml:13 | ir_cron_res_users_deletion | OBSERVATION | restored DB | — | DB: 54 ir_cron rows (47 active), all with user_id 1; 2 owned by base; ir_cron_trigger 0 rows; ir_cron_progress 50 rows. | N-U01-184 |
| VDR-U01-C341 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:598 | _notify_admin(self.env._( | INFERENCE | always | — | A job failing for a week is deactivated and only notified through logs or the admin channel. | N-U01-188 |
| VDR-U01-C342 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:482 | api.Environment(job_cr | INFERENCE | always | — | All DB crons use the superuser id, so they bypass rules and company scoping. | N-U01-187 |
| VDR-U01-C343 | FUNCTION MAPPING REQUIRED | n/a | def _process_jobs | UNKNOWN | n/a | RT | Multi-worker, update-time and neutralisation behaviour and real cadence require runtime testing. | N-U01-190 |
| VDR-U01-C344 | FUNCTION MAPPING REQUIRED | n/a | def _process_jobs | UNKNOWN | n/a | RT | Worker polling cadence and whether workers run in the target deployment are not testable from source. | N-U01-189 |
| VDR-U01-C345 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:61 | FULLY_DONE | FACT | always | — | Completion statuses of a run are fully done, partially done and failed (class CompletionStatus lines 61-64); a job also has idle and running (locked) phases. | N-U01-182 |
| VDR-U01-C346 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:130 | _compute_cron_name | FACT | always | — | cron_name is stored from the delegated server action name in English. | N-U01-169 |
| VDR-U01-C347 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:175 | Stage is set to | FACT | always | — | Trigger values: stage set, user set, tag added, state set, priority set, archive, unarchive, create, create or write, write (deprecated), unlink, on change, based on date, after creation, after last update, incoming message, outgoing message, webhook (lines 175-196). | N-U01-192 |
| VDR-U01-C348 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:97 | CREATE_TRIGGERS | FACT | always | — | Trigger groups: CREATE_TRIGGERS (97), WRITE_TRIGGERS (107), MAIL_TRIGGERS (120), TIME_TRIGGERS (124). | N-U01-192 |
| VDR-U01-C349 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:244 | Before Update Domain | FACT | always | — | Pre-condition filter_pre_domain (not checked on creation) and post-condition filter_domain (Apply on). | N-U01-194 |
| VDR-U01-C350 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:837 | all fields are implicit triggers | FACT | always | — | Without trigger fields every change qualifies; a create counts all fields as modified (839-841). | N-U01-194 |
| VDR-U01-C351 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:792 | avoid recursive processing | FACT | always | — | _process marks (rule, record) as done in the __action_done context dict so each rule runs once per record per chain. | N-U01-195 |
| VDR-U01-C352 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:1020 | "__action_done" | FACT | always | — | Message triggers are skipped when processing is already inside an automation, for internal messages and for notification-type messages. | N-U01-195 |
| VDR-U01-C353 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:283 | Target model of actions | FACT | always | — | Constraint: all actions must target the rule's model. | N-U01-196 |
| VDR-U01-C354 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:317 | can only be used with | FACT | always | — | Constraint: on_change triggers accept only code actions. | N-U01-196 |
| VDR-U01-C355 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:324 | cannot be used when deleting records | FACT | always | — | Constraint: on_unlink cannot use email, follower or activity actions. | N-U01-196 |
| VDR-U01-C356 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:171 | Mail event can not be configured | FACT | always | — | Constraint: message triggers require a model with the discussion feature. | N-U01-196 |
| VDR-U01-C357 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:1190 | final_exception | FACT | always | — | Time-based cron: a failing rule is rolled back (1210), logged, processing continues, and the last exception is re-raised at the end (1218-1219) so the job counts as failed. | N-U01-198 |
| VDR-U01-C358 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:828 | except Exception as e | FACT | always | — | Exceptions in actions are annotated with the rule (postmortem) and re-raised, aborting the user's transaction. | N-U01-198 |
| VDR-U01-C359 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:652 | No record to run the automation | FACT | always | — | Webhook raises ValidationError when the record getter finds nothing; controller turns any exception into HTTP 500 json (controllers/main.py:17). | N-U01-198 |
| VDR-U01-C360 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:678 | 'active': bool(automations) | FACT | always | — | _update_cron activates the time-trigger job only when active time-based rules exist. | N-U01-197 |
| VDR-U01-C361 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:736 | Minimum 1 minute, maximum 4 hours | FACT | always | — | Cron interval = min delay divided by 10, clamped to 1 minute to 4 hours, default 4 hours. | N-U01-197 |
| VDR-U01-C362 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:683 | only update the cron interval if | FACT | always | — | Cron interval is only ever shortened by rule changes. | N-U01-197 |
| VDR-U01-C363 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:1165 | relative_offset | FACT | always | — | Time rules find records whose date field falls between last run and now shifted by the delay; created and updated variants use create_date or write_date or date_automation_last. | N-U01-197 |
| VDR-U01-C364 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:1131 | automation.trg_date_calendar_id and automation.trg_date_range_type == 'day' | FACT | always | — | Day-based delays can use a working calendar (plan_days). | N-U01-197 |
| VDR-U01-C365 | FUNCTION MAPPING REQUIRED | base_automation/data/base_automation_data.xml:11 | name="active" eval="False" | FACT | always | — | The Automation Rules cron is seeded inactive (4-hour interval) inside a noupdate block. | N-U01-204 |
| VDR-U01-C366 | FUNCTION MAPPING REQUIRED | base_automation/controllers/main.py:6 | auth='public' | FACT | module base_automation installed | — | Route /web/hook/<uuid> is public, csrf off, GET or POST. | N-U01-199 |
| VDR-U01-C367 | FUNCTION MAPPING REQUIRED | base_automation/controllers/main.py:9 | request.env['base.automation'].sudo() | FACT | module base_automation installed | — | The rule is looked up by webhook_uuid as superuser and executed through _execute_webhook. | N-U01-201 |
| VDR-U01-C368 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:161 | webhook_uuid | FACT | always | — | Each rule has a random uuid4 webhook identifier (not copied); rotate action at 561-563; record_getter code (162) default builds the record from payload _model and _id. | N-U01-199 |
| VDR-U01-C369 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:164 | log_webhook_calls | FACT | always | — | Optional logging of webhook calls into ir.logging. | N-U01-199 |
| VDR-U01-C370 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:637 | safe_eval.safe_eval(self.record_getter | FACT | always | — | record_getter is evaluated with safe_eval using model, user, uid and payload. | N-U01-199 |
| VDR-U01-C371 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:707 | sudo().search(domain) | FACT | always | — | _get_actions finds the rules for a model and trigger as superuser, then re-binds to the user env. | N-U01-201 |
| VDR-U01-C372 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:824 | for action in self.sudo().action_server_ids | FACT | always | — | Actions are run from a sudo recordset: pre and post filters are also evaluated in sudo (747, 762). | N-U01-201 |
| VDR-U01-C373 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:1179 | action.sudo()._run | FACT | always | — | ir.actions.server.run checks _can_execute_action_on_records then executes action.sudo()._run. | N-U01-201 |
| VDR-U01-C374 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:1222 | You don't have enough access rights | FACT | always | — | If the action has groups the user must hold one (all_group_ids); otherwise write access to the model and records is required (1224-1242). | N-U01-200 |
| VDR-U01-C375 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:965 | raise ValidationError(msg) | FACT | always | — | Python code is syntax-checked on save (test_python_expr). | N-U01-200 |
| VDR-U01-C376 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:1016 | safe_eval(self.code.strip() | FACT | always | — | Code actions run in safe_eval with env, model, record, records, log and UserError (1111-1149). | N-U01-200 |
| VDR-U01-C377 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:724 | ir.actions.server.history | FACT | always | — | Code changes are kept as history entries. | N-U01-200 |
| VDR-U01-C378 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:1074 | timeout=1 | FACT | always | — | Webhook action posts after commit with 1 second timeout and logs failures; a rollback cancels it (1062-1064). | N-U01-202 |
| VDR-U01-C379 | FUNCTION MAPPING REQUIRED | base/models/ir_actions.py:613 | ('object_write', 'Update Record') | FACT | always | — | Base server action types: update record, create record, duplicate record, execute code, send webhook notification, multi actions. | N-U01-191 |
| VDR-U01-C380 | FUNCTION MAPPING REQUIRED | mail/models/ir_actions_server.py:27 | ('mail_post', 'Send Email') | FACT | module mail installed | — | Mail adds create activity, send email, add and remove followers action types; sms adds send SMS (sms/models/ir_actions_server.py:12). | N-U01-191 |
| VDR-U01-C381 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:693 | re-install the model patches, and notify | FACT | always | — | Rule create, write of critical fields or unlink re-installs the method patches and flags the registry as invalidated. | N-U01-203 |
| VDR-U01-C382 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:852 | Patch models that should trigger action | FACT | always | — | At registry load every rule patches create, write, _compute_field_value, unlink, message_post of its model and registers onchange methods. | N-U01-208 |
| VDR-U01-C383 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:1044 | Patch method `name` on `model` | FACT | always | — | Models are patched once per method; every create or write on a watched model therefore passes through the engine. | N-U01-208 |
| VDR-U01-C384 | FUNCTION MAPPING REQUIRED | base_automation/__manifest__.py:18 | 'depends': ['base', 'digest' | FACT | always | — | base_automation depends on digest, resource, mail and sms. | N-U01-205 |
| VDR-U01-C385 | FUNCTION MAPPING REQUIRED | base_automation/security/ir.model.access.csv:2 | access_base_automation_config | FACT | always | — | Single ACL row: base.group_system full CRUD on base.automation; the module declares no record rule or group. | N-U01-206 |
| VDR-U01-C386 | FUNCTION MAPPING REQUIRED | base_automation/security/ir.model.access.csv:2 | access_base_automation_config | OBSERVATION | restored DB | — | DB: base_automation module owns 1 ACL, 0 rules, 0 groups; no ir.rule exists on base.automation, ir.actions.server or ir.cron. | N-U01-206 |
| VDR-U01-C387 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:141 | class BaseAutomation | OBSERVATION | restored DB | — | DB: base_automation table has 0 rows; the module cron exists inactive; ir_act_server has 168 rows (114 plain, 54 cron-usage), all state code, none with usage base_automation. | N-U01-204 |
| VDR-U01-C388 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:141 | class BaseAutomation | INFERENCE | always | — | No company_id field exists on base.automation; rules apply across companies. | N-U01-206 |
| VDR-U01-C389 | FUNCTION MAPPING REQUIRED | base_automation/models/base_automation.py:619 | _execute_webhook | INFERENCE | always | — | Webhook actions executed after the sudo lookup run elevated because the rule recordset is sudo (controllers/main.py:9, base_automation.py:824). | N-U01-207 |
| VDR-U01-C390 | FUNCTION MAPPING REQUIRED | n/a | class BaseAutomation | UNKNOWN | n/a | RT | On-change, message and time-based behaviour with real data and under write load is not verifiable from source. | N-U01-209 |
| VDR-U01-C391 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:114 | naming convention | FACT | always | — | Settings fields are classified by prefix: default_ (ir.default), group_ (implied group), module_ (install), config_parameter attribute (ir.config_parameter), others via set_values (docstring 99-148; classification 178-228). | N-U01-210 |
| VDR-U01-C392 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:368 | Only administrators can change the settings | FACT | always | — | execute requires env.is_admin() (superuser or erp_manager); ACL for the transient model is system group (csv line 131). | N-U01-213 |
| VDR-U01-C393 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:131 | access_res_config_settings | FACT | always | — | res.config.settings model access: base.group_system. | N-U01-213 |
| VDR-U01-C394 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:160 | Cannot duplicate configuration! | FACT | always | — | copy on settings is refused. | N-U01-213 |
| VDR-U01-C395 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:326 | groups._apply_group(implied_group) | FACT | always | — | Group switches add or remove the implied group on the target group (default group_user), sudo; current state read from all_implied_ids (256). | N-U01-214 |
| VDR-U01-C396 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:378 | to_uninstall | FACT | always | — | Unchecked installed modules open the base.module.uninstall wizard (384-394); installs run at the end through button_immediate_install (173). | N-U01-215 |
| VDR-U01-C397 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:317 | IrDefault.set(model, field, value) | FACT | always | — | default_ fields store ir.default without user or company (global). | N-U01-216 |
| VDR-U01-C398 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:349 | IrConfigParameter.set_param(icp, value) | FACT | always | — | config_parameter fields are stored as global parameters. | N-U01-216 |
| VDR-U01-C399 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:12 | default=lambda self: self.env.company | FACT | module base_setup installed | — | Settings company_id defaults to the current company; related company fields (report footer at 33, layout at 37) edit that company. | N-U01-216 |
| VDR-U01-C400 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:14 | module_base_import | FACT | module base_setup installed | — | Module toggles: base_import, google_calendar, microsoft_calendar, mail_plugin, auth_oauth, auth_ldap, account_inter_company_rules, voip, web_unsplash, sms, partner_autocomplete, base_geolocalize, google_recaptcha, website_cf_turnstile, google_address_autocomplete (lines 14-32). | N-U01-211 |
| VDR-U01-C401 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:35 | implied_group='base.group_multi_currency' | FACT | module base_setup installed | — | Multi-currency switch is a group_ field implying base.group_multi_currency. | N-U01-211 |
| VDR-U01-C402 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:38 | config_parameter='base_setup.show_effect' | FACT | module base_setup installed | — | show_effect and profiling window (line 46) are global parameters. | N-U01-211 |
| VDR-U01-C403 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:105 | _compute_active_user_count | FACT | module base_setup installed | — | Counts of companies, active internal users and languages are shown (99-114); is_root_company computed from parent_id (133-136). | N-U01-217 |
| VDR-U01-C404 | FUNCTION MAPPING REQUIRED | base_setup/models/res_config_settings.py:60 | default_user_group | FACT | module base_setup installed | — | open_new_user_default_groups returns the default group form, creating the group and its non-updatable external id when missing (58-79). | N-U01-218 |
| VDR-U01-C405 | FUNCTION MAPPING REQUIRED | base/models/ir_config_parameter.py:98 | param.unlink() | FACT | always | — | set_param with False or None deletes the key and only writes when the string value changed (95). | N-U01-219 |
| VDR-U01-C406 | FUNCTION MAPPING REQUIRED | base_setup/__manifest__.py:22 | 'auto_install': True | FACT | module base_setup installed | — | base_setup auto-installs and depends on base and web. | N-U01-221 |
| VDR-U01-C407 | FUNCTION MAPPING REQUIRED | base_setup/controllers/main.py:12 | base.group_erp_manager | FACT | module base_setup installed | — | The /base_setup/data endpoint requires the access-rights manager group and counts active internal users and users never logged in. | N-U01-221 |
| VDR-U01-C408 | FUNCTION MAPPING REQUIRED | base/models/ir_config_parameter.py:18 | _default_parameters | FACT | always | — | Default parameters created at init: database.secret, database.uuid, database.create_date, web.base.url, base.login_cooldown_after (10), base.login_cooldown_duration (60). | N-U01-222 |
| VDR-U01-C409 | FUNCTION MAPPING REQUIRED | base/models/ir_config_parameter.py:114 | You cannot rename config parameters | FACT | always | — | Default parameter keys cannot be renamed (114) or deleted (125). | N-U01-222 |
| VDR-U01-C410 | FUNCTION MAPPING REQUIRED | base/models/ir_config_parameter.py:72 | @ormcache('key', cache='stable') | FACT | always | — | Parameter reads are cached; get_param checks read access first (68). | N-U01-223 |
| VDR-U01-C411 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:118 | access_ir_config_parameter_system | FACT | always | — | Only system group has CRUD on ir.config_parameter. | N-U01-223 |
| VDR-U01-C412 | FUNCTION MAPPING REQUIRED | base/data/ir_config_parameter_data.xml:4 | default_max_email_size | OBSERVATION | restored DB | — | DB: 45 config parameters in total; base ships base.default_max_email_size (noupdate) and base.template_portal_user_id by data files. | N-U01-224 |
| VDR-U01-C413 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:833 | database.secret | INFERENCE | always | — | The database.secret parameter feeds the session token query, so parameter write access is security-critical; web.base.url feeds links (updated at login, 807). | N-U01-225 |
| VDR-U01-C414 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:326 | groups._apply_group(implied_group) | INFERENCE | always | — | Because the target group is group_user by default, switches change the rights of all internal users database-wide; removal uses _remove_group (res_groups.py:315-320). | N-U01-226 |
| VDR-U01-C415 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | The key-indicator controller and provider in base_setup were not read. | N-U01-227 |
| VDR-U01-C416 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:518 | always accessible for reading | FACT | always | — | _check_access docstring: public attachments readable; attachments with a record follow the record's access (field access too for non-admins); recordless attachments only for admin and creator. | N-U01-232 |
| VDR-U01-C417 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:550 | attachment.public and operation == 'read' | FACT | always | — | Public attachments skip further checks for read. | N-U01-232 |
| VDR-U01-C418 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:555 | attachment.create_uid.id != self.env.uid | FACT | always | — | Without res_id, non-system users may access only their own attachments. | N-U01-232 |
| VDR-U01-C419 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:564 | _has_field_access(field, operation) | FACT | always | — | Attachments bound to a field require field access for non-system users. | N-U01-232 |
| VDR-U01-C420 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:539 | check write operation instead of unlinking | FACT | always | — | Create and unlink on attachments are checked as write on the linked record. | N-U01-232 |
| VDR-U01-C421 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:704 | _filtered_access('read') | FACT | always | — | _search filters results by read access in batches of PREFETCH_MAX. | N-U01-233 |
| VDR-U01-C422 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:3 | access_ir_attachment_group_user | FACT | always | — | Internal users have full ACL on ir.attachment; the group-less row (line 4) grants nothing, so portal and public have no model-level access. | N-U01-233 |
| VDR-U01-C423 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:805 | generate_access_token | INFERENCE | always | — | Attachments can carry access tokens (generate_access_token 805, raw token scope 816) used by serving routes, which is how outsiders obtain files. | N-U01-233 |
| VDR-U01-C424 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:491 | Sorry, you are not allowed to | FACT | always | — | Binary attachments with a url can only be written by users in the serving groups, unless admin. | N-U01-234 |
| VDR-U01-C425 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:499 | cannot attach an attachment to itself | FACT | always | — | Constraint on circular attachment. | N-U01-234 |
| VDR-U01-C426 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:459 | company_id = fields.Many2one | INFERENCE | always | — | company_id is stamped but _check_access (514-588) does not use it; access follows the linked record. | N-U01-245 |
| VDR-U01-C427 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2253 | UniqueIndex('(module, name)') | FACT | always | — | External identifiers are unique per (module, name); the module column records the owner. | N-U01-229 |
| VDR-U01-C428 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2252 | External IDs cannot contain spaces | FACT | always | — | SQL CHECK on name. | N-U01-236 |
| VDR-U01-C429 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2249 | noupdate = fields.Boolean | FACT | always | — | noupdate (Non Updatable) flag per external identifier. | N-U01-235 |
| VDR-U01-C430 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2442 | ON CONFLICT (module, name) | FACT | always | — | _update_xmlids upserts identifier rows; during updates (update True) rows flagged noupdate are not repointed (line 2450). | N-U01-235 |
| VDR-U01-C431 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2647 | noupdate set to false, but not | FACT | always | — | _process_end deletes records whose identifier is not noupdate and was not loaded in the module data of this update. | N-U01-235 |
| VDR-U01-C432 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2724 | check_access('write') | FACT | always | — | toggle_noupdate requires write access on the record and flips noupdate on its identifiers. | N-U01-236 |
| VDR-U01-C433 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2477 | Administrator access is required to uninstall | FACT | always | — | _module_data_uninstall requires system user and deletes only records not referenced by another module's identifiers (docstring 2464-2470). | N-U01-236 |
| VDR-U01-C434 | FUNCTION MAPPING REQUIRED | base/models/res_groups.py:206 | __custom__ | FACT | always | — | _ensure_xml_id creates external identifiers in module __custom__ for groups lacking one. | N-U01-229 |
| VDR-U01-C435 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:126 | At least one language must be | FACT | always | — | Constraint on active (not checked while registry loads). | N-U01-237 |
| VDR-U01-C436 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:115 | The code of the language must | FACT | always | — | Unique name, code and url_code (lines 110-121). | N-U01-237 |
| VDR-U01-C437 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:394 | Base Language 'en_US' can not be | FACT | always | — | Deletion guards: base language, user's context language (397) and active languages (399-400). | N-U01-237 |
| VDR-U01-C438 | FUNCTION MAPPING REQUIRED | base/wizard/base_language_install.py:39 | _update_translations | FACT | always | — | lang_install activates the chosen languages (38) and loads translations of all installed modules, overwrite option default True (23-25). | N-U01-238 |
| VDR-U01-C439 | FUNCTION MAPPING REQUIRED | base/security/ir.model.access.csv:136 | access_base_language_install | FACT | always | — | Language install wizard is system group only. | N-U01-238 |
| VDR-U01-C440 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:706 | context > request > company > | FACT | always | — | Context language fallback chain implemented in context_get (706-718). | N-U01-239 |
| VDR-U01-C441 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:88 | def _storage | FACT | always | — | Attachment storage backend is selected by _storage (file or db); the docstring (64-70) says storage engines can be replaced by overriding file read, write and delete. | N-U01-241 |
| VDR-U01-C442 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:61 | class IrAttachment | OBSERVATION | restored DB | — | DB: ir_attachment has 3576 rows (2701 url type, 875 binary type; 202 without a linked model). | N-U01-242 |
| VDR-U01-C443 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2226 | class IrModelData | OBSERVATION | restored DB | — | DB: ir_model_data 54300 rows; module base 6680 rows (5386 updatable, 1294 non-updatable); base: 32 rules non-updatable, 146 ACL updatable, 12 groups (2 non-updatable), 2 crons updatable, company non-updatable. | N-U01-243 |
| VDR-U01-C444 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:3 | noupdate="1" | INFERENCE | always | — | Rules loaded with noupdate=1 do not follow module corrections; ACL rows in the CSV are updatable, so a fix to ACLs is applied on update but a fix to rules is not. | N-U01-244 |
| VDR-U01-C445 | FUNCTION MAPPING REQUIRED | n/a | company_id = fields.Many2one | UNKNOWN | n/a | RT | Token-based public sharing and orphan file cleanup (_gc_file_store) were only skimmed. | N-U01-246 |
| VDR-U01-C446 | FUNCTION MAPPING REQUIRED | n/a | _parent_store = True | UNKNOWN | n/a | RT | Browser company switcher behaviour (selection order, branch ticking, persistence) was only partly read. | N-U01-026 |
| VDR-U01-C447 | FUNCTION MAPPING REQUIRED | n/a | _parent_store = True | UNKNOWN | n/a | RT | Handling of records owned by a user whose allowed company is later removed is not determined. | N-U01-027 |
| VDR-U01-C448 | FUNCTION MAPPING REQUIRED | n/a | from __future__ import annotations | UNKNOWN | n/a | RT | Second-factor, passkey and external-provider flows deliberately not read. | N-U01-108 |
| VDR-U01-C449 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | n/a | RT | Effective cross-company behaviour of non-base models must be read in their own units. | N-U01-019 |
| VDR-U01-C450 | FUNCTION MAPPING REQUIRED | base/wizard/base_partner_merge.py:475 | def _log_merge_operation | FACT | always | — | In base the merge is only logged to the server logger (info line at 476); no database note is written. | N-U01-124 |
| VDR-U01-C451 | FUNCTION MAPPING REQUIRED | mail/wizard/base_partner_merge_automatic_wizard.py:11 | dst_partner.message_post( | FACT | module mail installed | — | With mail installed, a note listing the merged contacts (name, email, id) is posted on the destination contact; this refines the prior candidate statement that a note is written (not a contradiction). | N-U01-124 |
| VDR-U01-C452 | FUNCTION MAPPING REQUIRED | loyalty/wizard/base_partner_merge.py:8 | merge corresponding nominative loyalty cards | FACT | module loyalty installed | — | Loyalty overrides _update_foreign_keys to merge loyalty cards; website (website/models/base_partner_merge.py:13) merges visitors first to avoid a unique violation. | N-U01-124 |
| VDR-U01-C453 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:16 | multi-company rule | INFERENCE | always | — | Purpose of company scoping is visible in the contact rule comment (lines 15-18): the company rule must not hide contacts of internal users; company rules are the tenancy filter on master data. | N-U01-005 |
| VDR-U01-C454 | FUNCTION MAPPING REQUIRED | base/models/res_company.py:49 | active = fields.Boolean(default=True) | FACT | always | — | Company has an active flag (default True); no other state field exists on the company. | N-U01-015 |
| VDR-U01-C455 | FUNCTION MAPPING REQUIRED | base/models/ir_rule.py:26 | domain_force = fields.Text | INFERENCE | always | — | A rule stores a domain per model and operation set, i.e. a row-level filter (purpose inferred from fields 22-31 and _compute_domain). | N-U01-030 |
| VDR-U01-C456 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:5 | res_users_log_rule | OBSERVATION | restored DB | — | DB: the 32 base rules target these models: res.users.apikeys, change.password.own, change.password.user, ir.embedded.actions, ir.default, ir.filters, ir.ui.view.custom, properties.base.definition, res.company, res.currency.rate, res.device, res.device.log, res.partner, res.partner.bank, res.users, res.users.identitycheck, res.users.log, res.users.settings. | N-U01-042 |
| VDR-U01-C457 | FUNCTION MAPPING REQUIRED | base/security/base_security.xml:59 | ('company_id', '=', False) | INFERENCE | always | — | Rules for bank accounts, currency rates (line 65) and contacts (line 19) include the shared (no company) alternative, so a mistakenly empty company on such records makes them visible to every company. | N-U01-051 |
| VDR-U01-C458 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2090 | perm_read = fields.Boolean | FACT | always | — | ir.model.access has model_id, group_id and four perm flags (lines 2088-2093). | N-U01-056 |
| VDR-U01-C459 | FUNCTION MAPPING REQUIRED | base/security/base_groups.xml:80 | Portal members have specific access rights | INFERENCE | always | — | Purpose of the portal and public type groups per the group comments (lines 80, 89): dedicated groups carrying restricted record rules and menus for external users. | N-U01-058 |
| VDR-U01-C460 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:159 | inherits from res.partner | INFERENCE | always | — | Class docstring: partner data (lang, name, address, avatar) lives on the contact; the user model holds technical data only (lines 156-161). | N-U01-082 |
| VDR-U01-C461 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:227 | active = fields.Boolean(default=True) | FACT | always | — | User has an active flag; active_partner (line 228) mirrors the contact flag. | N-U01-099 |
| VDR-U01-C462 | FUNCTION MAPPING REQUIRED | base/models/res_users.py:808 | ICP.set_param('web.base.url', base) | INFERENCE | always | — | Because the parameter is rewritten on every system-user browser login unless frozen, links built from it in outgoing documents follow the last administrator login address. | N-U01-106 |
| VDR-U01-C463 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:245 | bank_ids: ResPartnerBank | FACT | always | — | Contact fields include bank_ids, category_id tags (249), industry_id (280), lang, tz, user_id salesperson, vat, company_registry, website, comment notes. | N-U01-110 |
| VDR-U01-C464 | FUNCTION MAPPING REQUIRED | base/models/res_partner.py:301 | technical field used for managing commercial | INFERENCE | always | — | commercial_partner_id exists to let one contact tree carry shared commercial data for accounting, sales and purchasing (purpose from comment at 301 and sync logic 685-827). | N-U01-111 |
| VDR-U01-C465 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:281 | date = date or fields.Date.context_today(self) | INFERENCE | always | — | Conversions are always dated (defaulting to today) so the same amount converts reproducibly at a given date (_get_conversion_rate 272-282). | N-U01-137 |
| VDR-U01-C466 | FUNCTION MAPPING REQUIRED | base/models/res_currency.py:41 | active = fields.Boolean(default=True) | FACT | always | — | Currency active flag; its count drives the multi-currency group (lines 83-106). | N-U01-146 |
| VDR-U01-C467 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:147 | padding = fields.Integer | FACT | always | — | Sequence fields: prefix, suffix, padding, number_next, number_increment, company_id, use_date_range (lines 138-153). | N-U01-154 |
| VDR-U01-C468 | FUNCTION MAPPING REQUIRED | base/models/ir_sequence.py:89 | unique identifiers in a transaction-safe | INFERENCE | always | — | Docstring states sequences generate unique identifiers in a transaction-safe way (purpose of controlled numbering). | N-U01-155 |
| VDR-U01-C469 | FUNCTION MAPPING REQUIRED | base/models/ir_cron.py:92 | Model describing cron jobs | INFERENCE | always | — | ir.cron describes cron jobs (actions or tasks) run by workers without user interaction. | N-U01-170 |
| VDR-U01-C470 | FUNCTION MAPPING REQUIRED | base_automation/__manifest__.py:12 | automatically trigger actions | INFERENCE | module base_automation installed | — | Manifest description: automation rules automatically trigger actions for various screens, with examples (assign a sales team, reminder on stale opportunities). | N-U01-193 |
| VDR-U01-C471 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:100 | Base configuration wizard for application settings | INFERENCE | always | — | res.config.settings is a base wizard giving administrators one screen for defaults, groups and modules (docstring lines 100-148). | N-U01-212 |
| VDR-U01-C472 | FUNCTION MAPPING REQUIRED | base/models/res_config.py:217 | name.startswith('module_') | FACT | always | — | module_ fields are optional boolean or selection toggles resolved to installable modules; effects are database-wide. | N-U01-220 |
| VDR-U01-C473 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:456 | res_model = fields.Char | FACT | always | — | Attachment links by res_model, res_field and res_id (Many2oneReference, lines 456-458); content stored through the file store described at lines 64-70. | N-U01-228 |
| VDR-U01-C474 | FUNCTION MAPPING REQUIRED | base/models/res_lang.py:123 | def _check_active | OBSERVATION | restored DB | — | DB: res_lang has 93 rows of which exactly 1 active (en_US). | N-U01-230 |
| VDR-U01-C475 | FUNCTION MAPPING REQUIRED | base/models/ir_attachment.py:514 | def _check_access | INFERENCE | always | — | Purpose of attachment access rules: no document leak through attachments of records the user cannot access (rules docstring 515-524). | N-U01-231 |
| VDR-U01-C476 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2722 | def toggle_noupdate | FACT | always | — | External identifier updatable state can be flipped; languages carry an active flag (res_lang.py:76). | N-U01-240 |
