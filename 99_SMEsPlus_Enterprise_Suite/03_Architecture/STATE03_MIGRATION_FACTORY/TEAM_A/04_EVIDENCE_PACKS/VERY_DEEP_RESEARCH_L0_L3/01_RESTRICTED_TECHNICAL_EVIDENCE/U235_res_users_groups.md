# U235 — res.users and res.groups — Restricted Technical Evidence

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

**Evidence status:** DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Research Unit: U235 (STATE03 VDR, TEAM_A, level L0-L3)
- Subject: res.users and res.groups in Odoo 19 Community (membership field, implied groups, privilege model, user types, multi-company fields, API keys, credential checks)
- Revision studied: 19.0.post20260921 (Community only)
- Research date: 2026-10-03 (research started 2026-10-02)
- Researcher: STATE03 VDR Worker U235
- Commit SHA: PENDING_COMMIT (local commit, not pushed)
- Primary modules: base (res_users, res_groups, res_groups_privilege, ir_module, base_groups data), auth_password_policy, auth_signup, auth_totp (pointer only), auth_passkey (pointer only, owner U108), portal, mail, base_setup, web (widget and stale mock)
- Out of scope here: record rules (U214), ACL rows (U222), passkey internals (U108)

## 0. Method and Pointer Convention

- Static source reading only. Odoo was not started. No database was restored for this unit. Database reconciliation: NOT PERFORMED — source-only study.
- All pointers are written as module-relative paths with a line or line range. They resolve under the addons directory of the release, or under the ORM core directory for ORM files.
- Statements about v16/v17 behaviour are labelled INFERENCE (prior knowledge) because v16/v17 source is not present in this tree.
- Class vocabulary: FACT (read directly in source), INFERENCE (derived or absence-based), UNKNOWN (cannot be settled statically), OBSERVATION is reserved for restored-database facts and is therefore not used here.
- A seeded default credential exists in the base data files of the release (base/data/res_users_data.xml, line 16). Its value is deliberately not reproduced in any file of this unit. It is a hygiene finding for deployment review only.
- Function-ID for every capability and claim: FUNCTION MAPPING REQUIRED (the function index has no entry for users and groups).
- No maturity levels, percentages or gate wording are assigned in this file.

Analysis dimensions used per capability: structure, state transitions, triggers and callers, access path, data effects, configuration, UI surface, integration, runtime dependence. Entries marked NOT APPLICABLE carry a short reason; UNKNOWN entries are listed under the unknown list of the capability.

---

## CAP-U235-01 Group membership model

Function-ID: FUNCTION MAPPING REQUIRED

### Fields and names (v19)

| Item | Pointer | Statement |
|---|---|---|
| Explicit membership on res.users | base/models/res_users.py:257 | group_ids, Many2many to res.groups through relation table res_groups_users_rel (columns uid, gid), default from _default_groups |
| Effective membership on res.users | base/models/res_users.py:258-259 | all_group_ids, non-stored computed, compute_sudo, with a search method |
| Compute of effective membership | base/models/res_users.py:446-449 | all_group_ids is the implied closure of group_ids |
| Search of effective membership | base/models/res_users.py:451-452 | rewritten to a domain on group_ids.all_implied_ids |
| Inverse on res.groups | base/models/res_groups.py:17 | user_ids, same relation table with columns swapped |
| Effective users on res.groups | base/models/res_groups.py:18-19 | all_user_ids, computed with search and inverse |
| Effective user count | base/models/res_groups.py:21-22 | all_users_count, computed at base/models/res_groups.py:382-385 |

Pointer: base/models/res_users.py:257
```
group_ids = fields.Many2many('res.groups', 'res_groups_users_rel', 'uid', 'gid', string='Groups', default=lambda s: s._default_groups(), help="Groups explicitly assigned to the user")
```

Pointer: base/models/res_users.py:446-452
```
@api.depends('group_ids.all_implied_ids')
def _compute_all_group_ids(self):
for user in self:
user.all_group_ids = user.group_ids.all_implied_ids
def _search_all_group_ids(self, operator, value):
return [('group_ids.all_implied_ids', operator, value)]
```

Pointer: base/models/res_groups.py:17
```
user_ids = fields.Many2many('res.users', 'res_groups_users_rel', 'gid', 'uid', help='Users explicitly in this group')
```

### State descriptions

- D1 explicit membership: user without group A -> user with group A [write of group_ids, wizard, role onchange, data file link command, settings option]; reverse by unlink command.
- D2 effective membership: recomputed when explicit groups or any implication closure changes; no stored value, so no migration of stored data.
- D3 inverse edit: effective user list edit on a group -> explicit list adjusted; removal of a user who holds the group only by implication is refused (see CAP-U235-02).

### Who may write membership

- Self path: base/models/res_users.py:188-193 lists the self-writable fields; group_ids is not in the list. The self-readable list at base/models/res_users.py:175-186 does include group_ids (line 183) and share (line 185).

Pointer: base/models/res_users.py:193
```
return ['signature', 'action_id', 'company_id', 'email', 'name', 'image_1920', 'lang', 'tz', 'api_key_ids', 'phone']
```

- write at base/models/res_users.py:596-645: the block at base/models/res_users.py:605-615 runs a write with elevated rights only when all keys are self-writable; otherwise normal ACL applies (ACL detail belongs to U222).
- A write that touches group_ids clears access related caches (base/models/res_users.py:634-636).
- Superuser protections in write: base/models/res_users.py:597-600 (cannot activate the superuser; cannot deactivate the current user).
- _allow_sudo_commands is False for res.users (base/models/res_users.py:167), res.groups (base/models/res_groups.py:13), res.users.apikeys (base/models/res_users.py:1523) and module categories (base/models/ir_module.py:80). ORM semantics: default True at orm/models.py:457; when the comodel flag is False, x2many commands on that comodel use the transaction default user instead of an elevated environment (orm/fields_relational.py:772-777; call sites at orm/fields_relational.py:977, 1084, 1420, 1603). Exact scenarios where results differ: UNKNOWN / runtime.

Pointer: orm/fields_relational.py:772-777
```
def _check_sudo_commands(self, comodel):
# if the model doesn't accept sudo commands
if not comodel._allow_sudo_commands:
# Then, disable sudo and reset the transaction origin user
return comodel.sudo(False).with_user(comodel.env.transaction.default_env.uid)
return comodel
```

### Name inventory against v17

| v17 name (INFERENCE) | v19 name | Pointer |
|---|---|---|
| groups_id on res.users | group_ids | base/models/res_users.py:257 |
| users on res.groups | user_ids | base/models/res_groups.py:17 |
| (no equivalent) | all_group_ids | base/models/res_users.py:258-259 |
| (no equivalent) | all_user_ids | base/models/res_groups.py:18-19 |
| trans_implied_ids | all_implied_ids (reflexive) | base/models/res_groups.py:71-73 |
| category_id on res.groups | privilege_id | base/models/res_groups.py:36 |

- Whole-word groups_id remains only in the stale web test mock: web/static/tests/_framework/mock_server/mock_server.js:694, and again at lines 700 and 708 of the same file. Not a runtime field.
- Other v19 models that use group_ids as a restriction field: base/models/ir_actions_report.py:182, base/models/ir_ui_menu.py:29, base/models/ir_ui_view.py:175, base/models/ir_actions.py:329 and base/models/ir_actions.py:661; and res.groups.privilege exposes group_ids as a One2many (base/models/res_groups_privilege.py:14).
- res.groups also keeps: model_access (base/models/res_groups.py:24), rule_groups (base/models/res_groups.py:25-26, record rules = U214), menu_access (27), view_access (28), comment (29), full_name (30), share (31), api_key_duration (32-33), sequence (35), privilege_id (36), view_group_hierarchy (37).

Dimensions: UI surface = access rights page of the user form (CAP-U235-03); integration = settings fields (CAP-U235-02).
Unknown / runtime: effect of the disabled sudo commands on third-party wizards; actual data in res_groups_users_rel of a given database.

---

## CAP-U235-02 Implied groups and group model

Function-ID: FUNCTION MAPPING REQUIRED

### Model facts

- res.groups header: base/models/res_groups.py:11-14 (_description Access Groups, _rec_name full_name, _allow_sudo_commands False, _order privilege_id, sequence, name, id).
- Implication fields: implied_ids (base/models/res_groups.py:69-70), all_implied_ids (71-73, recursive, compute_sudo, search), implied_by_ids (74-75), all_implied_by_ids (76-77), disjoint_ids (78-80).

Pointer: base/models/res_groups.py:69-70
```
implied_ids = fields.Many2many('res.groups', 'res_groups_implied_rel', 'gid', 'hid',
```

Pointer: base/models/res_groups.py:245-250
```
@api.depends('implied_ids.all_implied_ids')
def _compute_all_implied_ids(self):
""" Compute the reflexive transitive closure of implied_ids. """
group_definitions = self._get_group_definitions()
for g in self:
g.all_implied_ids = g.ids + group_definitions.get_superset_ids(g.ids)
```

- Closure engine: SetDefinitions in tools/set_expression.py (class at line 11; get_id at 146, get_superset_ids at 164, get_subset_ids at 178). _get_group_definitions (base/models/res_groups.py:362-376) is cached under the groups cache and builds supersets from implied_ids and disjoints from disjoint_ids.
- Cache clearing: on create (base/models/res_groups.py:297-301), on unlink (303-306), on write of implied_ids or implied_by_ids (197-199), and in the user-type disjoint check (82-86). write also calls call_cache_clearing_methods (192-193) and refuses names that start with a dash (185-187).
- All implied_by closure: _compute_all_implied_by_ids at base/models/res_groups.py:260-265 and search at 267-278.

### Add and remove behaviour

Pointer: base/models/res_groups.py:308-313
```
def _apply_group(self, implied_group):
""" Add the given group to the groups implied by the current group
:param implied_group: the implied group to add
groups = self.filtered(lambda g: implied_group not in g.all_implied_ids)
groups.write({'implied_ids': [Command.link(implied_group.id)]})
```

Pointer: base/models/res_groups.py:315-320
```
def _remove_group(self, implied_group):
groups = self.all_implied_ids.filtered(lambda g: implied_group in g.implied_ids)
groups.write({'implied_ids': [Command.unlink(implied_group.id)]})
```

- Add: _apply_group links the implied group only into groups whose closure does not already contain it. Remove: _remove_group unlinks it from every group in the closure that lists it directly. Neither touches user rows; user effect arrives through the recomputed closure.
- Settings integration: group-typed settings fields call these helpers at base/models/res_config.py:209-216 (field definition), default_get at base/models/res_config.py:254-258 and set_values at base/models/res_config.py:319-328.
- Effective user list inverse (refusal of implied removal):

Pointer: base/models/res_groups.py:228-232
```
def _inverse_all_user_ids(self):
for group in self:
user_to_add = group.all_user_ids - group.all_implied_by_ids.user_ids
user_to_remove = group.all_implied_by_ids.user_ids - group.all_user_ids
group.user_ids = group.user_ids - user_to_remove + user_to_add
```

Pointer: base/models/res_groups.py:234-237
```
cannot_remove = group.all_implied_by_ids.user_ids & user_to_remove
if cannot_remove:
raise UserError(self.env._(
"It is not possible to remove implied group %(group)s from users %(users)s",
```

- Compute of effective users uses an inactive-inclusive context: base/models/res_groups.py:223-226 (line 225 sets active_test False).
- Delete protection of groups linked to settings: base/models/res_groups.py:114-119.
- Other constraints: UNIQUE(privilege_id, name) at base/models/res_groups.py:39-40; CHECK api_key_duration >= 0 at base/models/res_groups.py:41-44; inherited view groups check at base/models/res_groups.py:88-90; copy_data at 177-182; _ensure_xml_id at 203-221.
- Display name: _compute_full_name at base/models/res_groups.py:121-129 builds the privilege name and group name joined by a slash unless the short display context is set; _search_full_name at 131-165.
- Feature flags: _is_feature_enabled at base/models/res_groups.py:378-380 reads membership of the superuser record, so feature enablement equals uid 1 membership.

Pointer: base/models/res_groups.py:378-380
```
def _is_feature_enabled(self, group_reference):
return self.env['res.users'].sudo().browse(api.SUPERUSER_ID)._has_group(group_reference)
```

State descriptions:
- D1 implication edge: absent -> present [settings option on, data file link, _apply_group]; present -> absent [settings option off, _remove_group, unlink command].
- D2 closure cache: valid -> cleared [create, unlink, write of implication fields, disjoint check]; recomputed on next _get_group_definitions call.
- D3 user effective groups: change follows from D1/D2 without a write on the user.

Dimensions: access path = res.groups ACL (U222); data effects = relation table res_groups_implied_rel.
Unknown / runtime: closure size and cache behaviour in a multi-worker deployment (cache invalidation across workers uses the registry mechanism; not exercised).

---

## CAP-U235-03 Classification: privilege model

Function-ID: FUNCTION MAPPING REQUIRED

- New model res.groups.privilege: base/models/res_groups_privilege.py:5 (_name), 6 (_description Privileges), 7 (_order), fields name (9), description (10), placeholder (11, default No), sequence (12, default 100), category_id (13), group_ids (14, One2many to res.groups by privilege_id).

Pointer: base/models/res_groups_privilege.py:14
```
group_ids = fields.One2many('res.groups', 'privilege_id', string='Groups')
```

- res.groups.privilege_id: base/models/res_groups.py:36.

Pointer: base/models/res_groups.py:36
```
privilege_id = fields.Many2one('res.groups.privilege', string='Privilege', index=True)
```

- Module category: ir.module.category has privilege_ids (base/models/ir_module.py:86) and exclusive Boolean (base/models/ir_module.py:90). The exclusive flag is used by module installation only: base/models/ir_module.py:450-472, with the search at line 458 and the error at lines 467-468.

Pointer: base/models/ir_module.py:458
```
exclusives = self.env['ir.module.category'].search([('exclusive', '=', True)])
```

- No category_id field on res.groups in v19 (INFERENCE from field list; v17 had it — INFERENCE).
- Base role groups carry the prefix Role in their name (base/security/base_groups.xml:36, 43, 79, 88).
- Seeds: module category master data base/security/base_groups.xml:6-9; privileges export (11-14) and contact (16-19); export group linked to export privilege (65); partner manager group linked to contact privilege (72).
- User form data feed: view_group_hierarchy Json on res.users at base/models/res_users.py:268-271 and builder _get_view_group_hierarchy at base/models/res_groups.py:325-360 (payload keys groups, privileges, categories). The web widget consuming it: web/static/src/webclient/res_user_group_ids_field/res_user_group_ids_field.js:24-34.
- User form: access rights page at base/views/res_users_views.xml:158-166 (role radio at 160, company_ids at 161, company_id at 162, widget on group_ids at 164-165; the second variant is hidden for share users when debug mode is off). Group form: base/views/res_groups_views.xml:1-170; default access opener form at base/views/res_groups_views.xml:156-169.

Pointer: base/views/res_users_views.xml:164-165
```
<field name="group_ids" widget="res_user_group_ids" nolabel="1" colspan="2" groups="base.group_no_one"/>
<field name="group_ids" widget="res_user_group_ids" nolabel="1" colspan="2" groups="!base.group_no_one" invisible="share"/>
```

Absence finding (INFERENCE, grep based): no sel_groups_* or in_group_* pseudo-field generation was found in the v19 base module sources searched. Replacement mechanism: role Selection (base/models/res_users.py:272), view_group_hierarchy (base/models/res_users.py:271) and the widget above. v17 behaviour of dynamic pseudo-fields is INFERENCE.

CONTRADICTION: the comment in base/security/base_groups.xml:21-25 says the field category_id is set later in the module category data file, but that data file contains only module category records and the group model has privilege_id, not category_id.

Pointer: base/security/base_groups.xml:23
```
Note that the field 'category_id' is set later in
```

Dimensions: UI surface is the main consumer; state transitions NOT APPLICABLE (static classification).
Unknown / runtime: the payload produced for a given database; ordering of groups inside privileges.

---

## CAP-U235-04 User types and base group chain

Function-ID: FUNCTION MAPPING REQUIRED

### Type groups and exclusivity

Pointer: base/models/res_groups.py:284
```
for xid in ('base.group_user', 'base.group_portal', 'base.group_public')
```

- Disjoint ids are the other type groups: _compute_disjoint_ids at base/models/res_groups.py:289-295.
- User-side constraint at base/models/res_users.py:535-548 (error when effective groups contain more than one type group).

Pointer: base/models/res_users.py:541-543
```
for user in self:
disjoint_groups = user.all_group_ids & user_type_groups
if len(disjoint_groups) > 1:
```

- Group-side constraint _check_user_disjoint_groups at base/models/res_groups.py:92-112 searches active users whose effective groups contain two type groups.
- share: stored computed boolean at base/models/res_users.py:234-235; compute at base/models/res_users.py:459-464.

Pointer: base/models/res_users.py:459-464
```
@api.depends('all_group_ids')
def _compute_share(self):
user_group_id = self.env['ir.model.data']._xmlid_to_res_id('base.group_user')
internal_users = self.filtered_domain([('all_group_ids', 'in', [user_group_id])])
internal_users.share = False
(self - internal_users).share = True
```

- Type predicates: _is_internal, _is_portal, _is_public, _is_system at base/models/res_users.py:1165-1179, each elevating before has_group.
- role Selection: base/models/res_users.py:272; _compute_role at 428-435; _onchange_role at 437-444 swaps the system or user group inside group_ids.
- Type chosen at creation: there is no type selector in the user form (INFERENCE from the form file); employee comes from the default groups (CAP-U235-08), portal from the portal wizard or signup template, public from the public user record (base/security/base_groups.xml:93-95).

### Base group chain (base/security/base_groups.xml)

| Group | Pointer | Implication or note |
|---|---|---|
| Access Rights (group_erp_manager) | base/security/base_groups.xml:26-29 | implies group_user (line 28) |
| Bypass HTML Field Sanitize | base/security/base_groups.xml:31-33 | no implication |
| Role Administrator (group_system) | base/security/base_groups.xml:35-40 | implies group_erp_manager and group_sanitize_override (line 38); seeded members at line 39 |
| Role User (group_user) | base/security/base_groups.xml:42-46 | api_key_duration 90.0 (line 45) |
| Multi Companies | base/security/base_groups.xml:48-50 | no implication in XML; synced from allowed companies (CAP-U235-05) |
| Multi Currencies | base/security/base_groups.xml:52-54 | no implication |
| Technical Features (group_no_one) | base/security/base_groups.xml:56-59 | implied_by group_user and group_system (line 58) |
| Allowed (group_allow_export) | base/security/base_groups.xml:61-66 | implied_by group_system |
| Creation (group_partner_manager) | base/security/base_groups.xml:68-73 | implied_by group_system |
| Role Portal | base/security/base_groups.xml:78-82 | type group |
| Role Public | base/security/base_groups.xml:87-91 | type group |

Pointer: base/security/base_groups.xml:38
```
<field name="implied_ids" eval="[Command.link(ref('group_erp_manager')), Command.link(ref('group_sanitize_override'))]"/>
```

- Chain result: system role -> access rights -> user role (all three effective for a system user), plus sanitize override.
- group_no_one: has_group only reports it in debug mode: base/models/res_users.py:1081-1082.
- Seeded users in base data: the system-level record with login __system__ and no stored credential, inactive (base/data/base_data.sql:134-135); uid 1 group Employee row at base/data/base_data.sql:138-139.

### Creation paths per type

- Portal wizard: action_grant_access at portal/wizard/portal_wizard.py:133-165; the write at line 159 links the portal group and unlinks the public group; revoke (167-187) only archives the user; _compute_group_details at 116-131 classifies wizard users as internal, portal or none; _create_user at 207-217 copies the template user.

Pointer: portal/wizard/portal_wizard.py:159
```
user_sudo.write({'active': True, 'group_ids': [(4, group_portal.id), (3, group_public.id)]})
```

- Mail constraint tying notification type to share: mail/models/res_users.py:70-73; compute at 75-95 removes the inbox group for users converted to share (lines 93-95); inverse at 120-124.

Pointer: mail/models/res_users.py:70-73
```
_notification_type = models.Constraint(
"CHECK (notification_type = 'email' OR NOT share)",
'Only internal user can receive notifications in Odoo',
)
```

- Settings record creation only for internal users in create: base/models/res_users.py:583 and 593.
- Public user lookup for a company uses effective users of the public group: base/models/res_company.py:490-504.

Dimensions: triggers = form, wizard, signup, data files; access path = ACL (U222).
Unknown / runtime: which users exist in a given database and their types; behaviour of the constraint against inactive users with historic dual membership.

---

## CAP-U235-05 Multi-company fields

Function-ID: FUNCTION MAPPING REQUIRED

- company_id (default company) at base/models/res_users.py:245-246 and company_ids (allowed companies) at base/models/res_users.py:247-248, relation table res_company_users_rel. Inverse on res.company: user_ids at base/models/res_company.py:68.

Pointer: base/models/res_users.py:247-248
```
company_ids = fields.Many2many('res.company', 'res_company_users_rel', 'user_id', 'cid',
```

- Constraint _check_user_company at base/models/res_users.py:501-510: active users must have company_id inside company_ids.

Pointer: base/models/res_users.py:504
```
if user.company_id not in user.company_ids:
```

- _get_company_ids at base/models/res_users.py:725-729; invalidation field list at base/models/res_users.py:735-740.
- Multi-company group sync in the UsersMultiCompany mixin: base/models/res_users.py:1352-1397; the counting logic at 1362-1366 adds or removes the multi-company group depending on whether the number of allowed companies exceeds one.

Pointer: base/models/res_users.py:1363
```
if company_count <= 1 and group_multi_company_id in user.group_ids.ids:
```

- Active-company context in the environment: env.company and env.companies at orm/environments.py:216-283 (context key allowed_company_ids).
- Record rules for multi-company: see U214 (not repeated).

Dimensions: UI = company switcher and user form fields at base/views/res_users_views.xml:161-162.
Unknown / runtime: contents of allowed_company_ids in a live session; interaction with the context key for non-web callers.

---

## CAP-U235-06 Credential layer

Function-ID: FUNCTION MAPPING REQUIRED

### Password verification

- _check_credentials(credential, env) at base/models/res_users.py:312-402. The password branch requires credential type password with a non-empty value (line 350), distinguishes interactive and non-interactive environments (353-362), reads the stored hash by SQL (364-368), verifies and possibly upgrades the hash (369-378), and returns an auth-info dict with auth_method password (381-385). Non-interactive calls may fall back to API key verification with scope rpc (387-394). Otherwise an access denied exception is raised (402).

Pointer: base/models/res_users.py:383
```
'auth_method': 'password',
```

Pointer: base/models/res_users.py:392
```
'auth_method': 'apikey',
```

- Setters: _set_password at base/models/res_users.py:294-297; _set_encrypted_password at 299-306; API-key-only restriction hook _rpc_api_keys_only at 308-310.
- Hash context: _crypt_context at base/models/res_users.py:1193-1212; schemes pbkdf2_sha512 with plaintext accepted only as deprecated legacy; rounds from a system parameter but not below MIN_ROUNDS (600000 at base/models/res_users.py:79).

Pointer: base/models/res_users.py:1211
```
pbkdf2_sha512__rounds=max(MIN_ROUNDS, int(cfg.get_param('password.hashing.rounds', 0))),
```

- Session token: base/models/res_users.py:829-884.
- Authentication entry points: _login at 760-782; authenticate at 784-811; _check_uid_passwd at 813-827.
- Re-authentication for sensitive actions: check_identity at base/models/res_users.py:87-127 (10 minute window around line 100); identity wizard model at 1400-1439.
- Password change: change_password at 898-917; _change_password at 919-932; wizards at 1446 (change.password.wizard), 1469 (change.password.user) and 1486 (change.password.own).
- Registry hook warns on legacy method name: base/models/res_users.py:1309-1311; MFA hooks at 1313-1319.

### Login throttling

- _assert_can_auth at base/models/res_users.py:1214-1281 and _on_login_cooldown at 1283-1307. Parameters: base.login_cooldown_after (default 5, zero disables) and base.login_cooldown_duration (default 60). Failure registry is a per-process map (base/models/res_users.py:1228-1229, 1247-1250).
- CONTRADICTION: docstring says by login (lines 1219-1222) but the key is the HTTP remote address (line 1252).

Pointer: base/models/res_users.py:1252
```
source = request.httprequest.remote_addr
```

### Password policy (auth_password_policy)

- get_password_policy at auth_password_policy/models/res_users.py:9-14; _set_password override at 16-19; _check_password_policy at 21-33 using parameter auth_password_policy.minlength (default 0); settings fields at auth_password_policy/models/res_config_settings.py:7-9 and _on_change_mins at 11-15.

### API keys (res.users.apikeys)

- Constants at base/models/res_users.py:1508-1516; class at 1519-1752 (_auto False at 1522, fields 1525-1529); init 1531-1554; remove 1556-1558; _remove 1560-1572 (line 1565 lets system users or the key owner delete).
- Expiry rule at base/models/res_users.py:1577-1589: system users bypass; otherwise a date is required, bounded by the longest api_key_duration among effective groups of the environment user (line 1585), future only.
- Key generation: _generate at base/models/res_users.py:1591-1618 (random hex at line 1606; stored as a hash plus an index prefix at line 1612).
- Programmatic generation: _ensure_can_manage_keys_programmatically at 1620-1634 (system parameter base.enable_programmatic_api_keys; system users exempt); generate at 1636-1685 (per-user limit parameter base.programmatic_api_keys_limit default 10 at line 1665, error at 1669-1670, scope rule comment at 1672-1677).
- Scope: key scope NULL matches any scope (SQL at line 1743 of _check_apikey_credentials, 1725-1752).

Pointer: base/models/res_users.py:1743
```
AND (scope IS NULL OR scope = %(scope)s)
```

- revoke at 1687-1712; garbage collection _gc_user_apikeys at 1714-1722.
- Wizard model res.users.apikeys.description at base/models/res_users.py:1755-1836: duration selection at 1759-1776 (1, 7, 30, 90, 180, 365 days; persistent value 0 at 1769; custom -1 at 1770); make_key at 1814-1832; creation limited to internal users at 1834-1836; show wizard at 1839-1845.
- Portal override: portal/models/res_users_apikeys_description.py:11-20 (system parameter portal.allow_api_keys).

### Logs, settings, deletion

- res.users.log at base/models/res_users.py:134-152 (_gc_user_logs at 143-152).
- res.users.settings: base/models/res_users_settings.py:8 (_name), 14-17 (UNIQUE user_id), 24-29 (_find_or_create_for_user).
- res.users.deletion: base/models/res_users_deletion.py:20 (_name); _gc_portal_users at 36-100; portal user deactivation helper at base/models/res_users.py:934-987.

### TOTP and passkey (pointer only)

- auth_totp/models/res_users.py: rate limits at 24-27, _mfa_type 47-52, _mfa_url 54-59, _rpc_api_keys_only 66-69, session token fields 71-72, _check_credentials 74-96 (auth_method totp at line 93).
- auth_passkey/models/res_users.py (owner U108): _login 34-47, _check_credentials 49-73 (auth_method passkey at 69, mfa skip at 70), token fields 75-76, token query params 78-85.

State descriptions:
- D1 credential: none -> hashed [_set_password]; hashed legacy -> rehashed [successful login when the context deems it deprecated].
- D2 API key: absent -> present [generate or wizard]; present -> removed [revoke, expiry GC].
- D3 failed attempts: counted per worker and source address -> cooldown active -> expired.

Hygiene finding: a seeded default credential is set in the base data file at base/data/res_users_data.xml:16. The value is not reproduced here. Deployment checks should confirm it is changed.

Dimensions: configuration = system parameters listed above; integration = TOTP and passkey overrides.
Unknown / runtime: parameter values, hash scheme distribution in a given database, cooldown behaviour across workers.

---

## CAP-U235-07 Superuser and system semantics

Function-ID: FUNCTION MAPPING REQUIRED

- SUPERUSER_ID is 1: orm/utils.py:19.
- Environment construction for uid 1 forces elevated mode: orm/environments.py:64-67.

Pointer: orm/environments.py:66
```
if uid == SUPERUSER_ID:
```

- Changing the user in an environment copy resets the elevated flag unless the target is uid 1: orm/environments.py:126-148 (line 147).
- is_superuser (orm/environments.py:178-180), is_admin (182-185: elevated or the user record is administrator-class), is_system (187-190) are methods. env.user is elevated: orm/environments.py:207-213.

Pointer: orm/environments.py:185
```
return self.su or self.user._is_admin()
```

- Record-level helpers: _is_admin at base/models/res_users.py:1181-1183 (superuser or access rights group), _is_superuser at 1185-1187.
- has_group: base/models/res_users.py:1065-1083. Caller restriction at line 1075 and error at 1078; has_groups at 1033-1063; _has_group at 1085-1096; _get_group_ids at 1098-1104.
- Module-level audit helper using is_admin: base/models/ir_module.py:57-73 (line 68).
- Superuser deletion and protection: base/models/res_users.py:647-660 (master data guard); at-least-one-administrator constraint at 550-555, skipped while the registry has no initialising modules (lines 552-553).
- Seeded system membership: base/security/base_groups.xml:39 and base/data/base_data.sql:134-139.

Dimensions: state transitions NOT APPLICABLE (static semantics).
Unknown / runtime: how third-party code uses env.su after user switching.

---

## CAP-U235-08 Default user creation and signup

Function-ID: FUNCTION MAPPING REQUIRED

- Default groups: _default_groups at base/models/res_users.py:203-212 returns the employee group plus the implied groups of the default access group record.

Pointer: base/models/res_users.py:209
```
default_group = self.env.ref('base.default_user_group', raise_if_not_found=False)
```

- The record base.default_user_group is seeded in a noupdate block: base/security/base_groups.xml:113-117. No base.default_user template record exists in v19 (INFERENCE; v17 template mechanism also INFERENCE).
- Configuration UI: base_setup opener at base_setup/models/res_config_settings.py:58-79; form at base/views/res_groups_views.xml:156-169; settings entry at base_setup/views/res_config_settings_views.xml:116-123. About 22 demo data files extend the default group, for example stock/data/stock_demo.xml:9-11.
- Signup (auth_signup/models/res_users.py): signup at 37-85; invitation scope at 87-89 (system parameter auth_signup.invitation_scope default b2b; uninvited signup refused unless b2c at 96-98); _signup_create_user at 91-102; _create_user_from_template at 111-129.

Pointer: auth_signup/models/res_users.py:112
```
template_user_id = literal_eval(self.env['ir.config_parameter'].sudo().get_param('base.template_portal_user_id', 'False'))
```

- Template user: base/security/base_groups.xml:98-104 (inactive, group set to portal at line 102) and parameter record at 106-109. The copy is activated (auth_signup/models/res_users.py:123) and copied without password reset mail (line 126); missing template raises an error (114-115, 127-129).

Pointer: base/security/base_groups.xml:102
```
<field name="group_ids" eval="[Command.set([ref('base.group_portal')])]"/>
```

State descriptions:
- D1 new internal user: no groups -> employee plus default access group implications [create without explicit groups].
- D2 new portal user: none -> copy of template [signup or portal wizard].
- D3 template: inactive record, never logged in by design.

Dimensions: configuration = default access group contents and signup parameters.
Unknown / runtime: actual contents of the default access group and the template in a given database.

## Migration Flags (against v16/v17, INFERENCE where v17 behaviour is stated)

| Flag | Severity | Pointer | Summary |
|---|---|---|---|
| GROUPS_ID_RENAMED_GROUP_IDS | HIGH | base/models/res_users.py:257 | groups_id (v17, INFERENCE) is now group_ids; inverse is user_ids at base/models/res_groups.py:17 |
| ALL_GROUP_IDS_EFFECTIVE_MEMBERSHIP | MEDIUM | base/models/res_users.py:446-452 | effective membership is a separate computed field |
| TRANS_IMPLIED_IDS_REPLACED | MEDIUM | base/models/res_groups.py:69-77 | closure fields are reflexive all_implied_ids and all_implied_by_ids |
| GROUP_CATEGORY_ID_REPLACED_BY_PRIVILEGE | HIGH | base/models/res_groups.py:36 | category on groups replaced by privilege_id and the privilege model |
| SEL_GROUPS_IN_GROUP_REMOVED | HIGH | NONE - absence finding | pseudo-fields not found by grep (INFERENCE) |
| MODULE_CATEGORY_EXCLUSIVE_INSTALL_ONLY | LOW | base/models/ir_module.py:458-468 | exclusive flag gates installation only |
| DEFAULT_USER_TEMPLATE_REPLACED | MEDIUM | base/models/res_users.py:203-212 | default access group record, no default user template |
| CHECK_CREDENTIALS_SIGNATURE | HIGH | base/models/res_users.py:312-402 | new credential dict signature; legacy method name warned at base/models/res_users.py:1309-1311 |
| HAS_GROUP_RESTRICTED_CALLERS | MEDIUM | base/models/res_users.py:1075-1082 | caller restriction and debug gating |
| PROGRAMMATIC_API_KEYS_GATED | MEDIUM | base/models/res_users.py:1620-1634 | parameter gate and per-user limit |
| API_KEY_DURATION_BY_GROUP | MEDIUM | base/models/res_users.py:1585 | expiry bound from group data |
| MFA_HOOKS_AND_AUTH_INFO | LOW | base/models/res_users.py:1313-1319 | MFA hooks and auth-info dict |
| USER_SETTINGS_INTERNAL_ONLY | LOW | base/models/res_users.py:583 | settings record created only for internal users at creation |
| ENV_IS_ADMIN_IS_SYSTEM | INFO | orm/environments.py:178-190 | environment predicates are methods |
| ALLOW_SUDO_COMMANDS_FALSE | MEDIUM | orm/fields_relational.py:772-777 | elevated x2many commands disabled for listed comodels |
| ALL_USER_IDS_INVERSE_REFUSES_IMPLIED_REMOVAL | LOW | base/models/res_groups.py:228-240 | implied membership cannot be removed through effective list |
| ADMIN_CONSTRAINT_BYPASS_DURING_BASE_LOAD | LOW | base/models/res_users.py:550-555 | constraint skipped while registry init list is empty |
| MAIL_NOTIFICATION_TYPE_CHECK | MEDIUM | mail/models/res_users.py:70-73 | CHECK ties notification type to share |
| GROUP_NO_ONE_IMPLIED_BY_GROUP_USER | MEDIUM | base/security/base_groups.xml:58 | technical features group implied by employee and system roles, debug gated |
| GROUP_DISPLAY_NAME_USES_PRIVILEGE | LOW | base/models/res_groups.py:121-129 | full name built from privilege name |
| ROLE_SELECTION | LOW | base/models/res_users.py:272 | role Selection on user |
| STALE_GROUPS_ID_IN_WEB_TEST_MOCK | INFO | web/static/tests/_framework/mock_server/mock_server.js:694 | stale test mock |
| STALE_CATEGORY_ID_COMMENT | INFO | base/security/base_groups.xml:23 | stale comment |
| LOGIN_COOLDOWN_DOC_MISMATCH | INFO | base/models/res_users.py:1252 | docstring says login, code uses remote address |
| FEATURE_FLAGS_DRIVEN_BY_SUPERUSER_MEMBERSHIP | LOW | base/models/res_groups.py:378-380 | feature enablement reads uid 1 membership |

## DISCOVERED SUPPORTING MODULES

| Module | Why relevant | Pointer |
|---|---|---|
| auth_signup | template user copy, signup scope, default portal creation | auth_signup/models/res_users.py:111-129 |
| portal | wizard granting and revoking portal access; API key override | portal/wizard/portal_wizard.py:133-187 |
| mail | notification type CHECK tied to share and the inbox group | mail/models/res_users.py:70-95 |
| auth_totp | MFA hooks and TOTP credential branch (pointer only) | auth_totp/models/res_users.py:74-96 |
| auth_passkey | passkey credential branch (pointer only, owner U108) | auth_passkey/models/res_users.py:49-73 |
| auth_password_policy | minimum length check on password set | auth_password_policy/models/res_users.py:21-33 |
| base_setup | default access group opener | base_setup/models/res_config_settings.py:58-79 |
| web | group widget on the user form and stale test mock | web/static/src/webclient/res_user_group_ids_field/res_user_group_ids_field.js:24-34 |

## Contradictions and Documentation Defects

1. Stale comment about category_id on groups: base/security/base_groups.xml:21-25 versus the group model (privilege_id at base/models/res_groups.py:36).
2. Login cooldown docstring versus implementation: base/models/res_users.py:1219-1222 versus base/models/res_users.py:1252.
3. The has_group access error text contains a source typo (ony): base/models/res_users.py:1078 (cosmetic).
4. Stale groups_id references in the web test mock: web/static/tests/_framework/mock_server/mock_server.js:694.

## Runtime-Dependent and Unknown Items (RT list)

- RT-01: contents of base.default_user_group and which groups it implies in a given database (affects new user defaults).
- RT-02: value of the system parameter naming the template portal user, and the groups of that user.
- RT-03: values of signup invitation scope, login cooldown parameters, password minimum length, hashing rounds.
- RT-04: API key gate parameter, per-user limit, and the api_key_duration of all custom groups.
- RT-05: exact scenarios where disabled elevated x2many commands change behaviour.
- RT-06: presence of users with legacy dual type membership (inactive users are excluded from the group-side check).
- RT-07: whether any deployed custom code still uses groups_id, sel_groups_*, in_group_* or the legacy credential method name.
- RT-08: whether the seeded default credential has been changed in each deployment (value not reproduced).

## Restricted Claims Register

Same 26 claims as the neutral table; technical statements use real names. Function-ID for all rows: FUNCTION MAPPING REQUIRED.

| Claim-ID | Pointer | Anchor | Class | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|
| U235-C01 | base/models/res_users.py:257 | res_groups_users_rel | FACT | — | res.users.group_ids is a Many2many to res.groups through res_groups_users_rel (uid, gid) | Explicit user to group membership stored in a dedicated relation table |
| U235-C02 | base/models/res_users.py:449 | user.group_ids.all_implied_ids | FACT | — | all_group_ids is computed as group_ids.all_implied_ids (non-stored, searchable) | Effective membership computed from explicit groups together with implied groups |
| U235-C03 | base/models/res_groups.py:237 | It is not possible to remove | FACT | — | _inverse_all_user_ids raises UserError when a user holds the group only through implication | Removing implied membership through the effective user list is refused with an error |
| U235-C04 | base/models/res_users.py:193 | 'api_key_ids', 'phone'] | FACT | — | SELF_WRITEABLE_FIELDS excludes group_ids | Profile edits by the user themselves exclude access group changes |
| U235-C05 | base/models/res_groups.py:69 | res_groups_implied_rel | FACT | — | implied_ids stored in res_groups_implied_rel; all_implied_ids and all_implied_by_ids are recursive computed closures | Direct group implications stored in relation table with recursive closure fields |
| U235-C06 | base/models/res_groups.py:250 | get_superset_ids(g.ids) | FACT | — | _compute_all_implied_ids uses SetDefinitions from _get_group_definitions (groups cache) | Implication closure computed from set definitions of all groups |
| U235-C07 | base/models/res_groups.py:319 | implied_group in g.implied_ids | FACT | — | _remove_group unlinks the implied group from implied_ids of every group in the closure that lists it | Switching a settings option off removes the implied group from direct implication lists |
| U235-C08 | base/security/base_groups.xml:23 | field 'category_id' is set | INFERENCE | CONTRA | stale comment about category_id on res.groups; model has privilege_id | Comment about a category field on groups no longer matches the group model |
| U235-C09 | base/models/res_groups_privilege.py:14 | 'res.groups', 'privilege_id' | FACT | — | res.groups.privilege has category_id and group_ids One2many on res.groups.privilege_id | Privilege record links a module category to a set of groups |
| U235-C10 | base/models/res_users.py:271 | view_group_hierarchy = fields.Json | INFERENCE | — | view_group_hierarchy Json feeds the res_user_group_ids widget | Group hierarchy exposed as one structured field for the web group widget |
| U235-C11 | base/models/ir_module.py:458 | ('exclusive', '=', True) | INFERENCE | — | ir.module.category.exclusive is used only by module installation conflict check | Exclusive category flag restricts module installation not group membership |
| U235-C12 | base/models/res_groups.py:284 | base.group_portal | FACT | — | _get_user_type_groups returns base.group_user, base.group_portal and base.group_public | Three disjoint user type groups identify employee portal and public users |
| U235-C13 | base/models/res_users.py:543 | len(disjoint_groups) > 1 | FACT | — | _check_disjoint_groups raises ValidationError for more than one type group | A user may hold at most one user type group |
| U235-C14 | base/models/res_users.py:463 | internal_users.share = False | FACT | — | share is computed from all_group_ids containing base.group_user | External flag derived from presence of the employee group in effective groups |
| U235-C15 | base/security/base_groups.xml:38 | group_sanitize_override | FACT | — | group_system implies group_erp_manager, which implies group_user | Administrator role implies access rights group which implies the employee group |
| U235-C16 | base/models/res_users.py:247 | res_company_users_rel | FACT | — | company_id default company and company_ids allowed companies | Users hold one default company and a set of allowed companies |
| U235-C17 | base/models/res_users.py:504 | user.company_id not in user.company_ids | FACT | — | _check_user_company constraint for active users | Default company must belong to the allowed companies of an active user |
| U235-C18 | base/models/res_users.py:1363 | company_count <= 1 | FACT | — | UsersMultiCompany syncs base.group_multi_company with number of allowed companies | Multi company group membership follows the number of allowed companies |
| U235-C19 | base/models/res_users.py:383 | 'auth_method': 'password', | FACT | — | _check_credentials returns auth-info dict with auth_method password | Successful password verification yields user identity with password method |
| U235-C20 | base/models/res_users.py:1211 | pbkdf2_sha512__rounds=max(MIN_ROUNDS | FACT | — | _crypt_context uses pbkdf2_sha512 with rounds at least MIN_ROUNDS (600000) | Password hashing uses a slow key derivation with a minimum round count |
| U235-C21 | base/models/res_users.py:1606 | os.urandom(API_KEY_SIZE) | FACT | — | API key is random hex, stored hashed with an index prefix | API key is random hex text stored only as a hash with an index prefix |
| U235-C22 | base/models/res_users.py:1585 | group.api_key_duration | FACT | RT | max key lifetime from the longest api_key_duration among all_group_ids of the environment user | Maximum key lifetime derives from the longest duration among the user groups |
| U235-C23 | orm/environments.py:66 | if uid == SUPERUSER_ID: | FACT | — | Environment.__new__ forces su for uid 1 | Environment for the superuser identifier always runs in elevated mode |
| U235-C24 | base/models/res_users.py:1183 | base.group_erp_manager | FACT | — | _is_admin is superuser or member of base.group_erp_manager | Administrator status means superuser or membership of the access rights group |
| U235-C25 | base/models/res_users.py:209 | base.default_user_group | FACT | — | _default_groups returns base.group_user plus implied_ids of base.default_user_group | New users start with the employee group plus configurable default groups |
| U235-C26 | auth_signup/models/res_users.py:112 | base.template_portal_user_id | FACT | RT | _create_user_from_template copies the user named by the system parameter base.template_portal_user_id | Portal signup copies a template user named by a system parameter |

End of restricted evidence for U235.
