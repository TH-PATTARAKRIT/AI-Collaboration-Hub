# G01 PLATFORM_BASE — LANE A PASS-1 — Module `privacy_lookup`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T3 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `privacy_lookup` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/privacy_lookup/` |
| Retrieval | raw.githubusercontent.com at the anchor commit. Files found through the manifest and the `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |

## 1. Evidence Pointer Table (11 blobs; SHA-1 = `git hash-object`)

| Path (addons/privacy_lookup/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 9eaa9987cdaa97b006c5fea0f961016490f811cd | Identity, deps, data list, auto_install |
| `__init__.py` | 2ae6446f9dc25fe7563ce0c6a4f1cc4904124cc5 | Imports models, wizard |
| `models/__init__.py` | 202b5ea8fefddfcc7fb7d903109aeb154d3928eb | Model import list |
| `models/privacy_log.py` | 045a2d25f7115f860d558c28d0d2f80301b64781 | Privacy action log with name/email masking |
| `models/res_partner.py` | 19962c362f2b31fd12ad0aa383071db82fbd97d5 | Opens the lookup wizard with the partner's name and email filled in |
| `wizard/__init__.py` | 17273b6f2b7eff9009fcef4bb985a59cf751c921 | Wizard import |
| `wizard/privacy_lookup_wizard.py` | 3b6d52e055a912c67e85970d0299de14d97cc619 | Lookup query across models; result lines; archive/delete actions |
| `wizard/privacy_lookup_wizard_views.xml` | 9d49f1dbe6953295daf616f1d0f29f7b54b848fd | Wizard/line views, actions, partner/user server-action bindings |
| `views/privacy_log_views.xml` | 2116cc13cac9496ea25a04b48cfba032264e6fc0 | Log list/form, actions, "Privacy" menus |
| `security/ir.model.access.csv` | d70edab351c9369c4e8100145b9006d1043029fe | ACL (3 rows) |
| `data/ir_actions_server_data.xml` | 7aac52ec8a0b8773de14cfc1670da285eeacf952 | Bulk "Archive Selection" / "Delete Selection" server actions on lines |

Not present at anchor (404): `controllers/__init__.py`, `tools/__init__.py`. Neither package exists in this module.

## 2. Findings by card section

### 2.1 Manifest / dependencies / purpose
1. Name "Privacy", category Hidden, version 1.0, auto_install, LGPL-3. The only dependency is `mail`, and there is no description text. Its purpose, inferred from the models: find the personal-data footprint of a data subject (name + email) across the database, archive or delete what is found, and keep an audit log in masked form. [`__manifest__.py`]

### 2.2 Data (models, fields)
2. `privacy.log` is persistent. It stores:
   - a date (defaults to now);
   - a masked name and a masked email, both required;
   - the handling user (required, defaults to the current user);
   - execution details;
   - a description of the records found;
   - an additional note.

   The handling user is shown as the record name. [`models/privacy_log.py`]
3. `privacy.lookup.wizard` is transient, with a lifetime cap of 24 hours and no count cap. It holds:
   - the name and email searched for (both required);
   - the result lines;
   - stored execution details, computed from the lines;
   - a link to its log record;
   - a computed description of the records found;
   - a line count.

   [`wizard/privacy_lookup_wizard.py`]
4. `privacy.lookup.wizard.line` is transient with the same 24-hour lifetime. Each line holds:
   - the target model and record id;
   - the stored record name, resolved with sudo;
   - a computed reference to the record, cleared when the viewer cannot read it;
   - whether the target model supports archiving;
   - an is-active flag and an is-unlinked flag;
   - per-line execution details.

   [`wizard/privacy_lookup_wizard.py`]

### 2.3 Business rules / lookup scope / actions / logging
5. **Input validation:** the email must normalize to a valid address, or a UserError "Invalid email address" is raised. The name and email are trimmed before use. [`wizard/privacy_lookup_wizard.py` `_get_query`]
6. **Lookup scope, fixed part:** partners whose normalized email matches or whose name matches, used as the set of indirect references. The fixed part returns:
   - those partners;
   - users whose login matches the email pattern, or whose partner matches by email or name;
   - messages authored by the referenced partners (the "direct messages" special case).

   [`_get_query`]
7. **Lookup scope, dynamic part:** every registered model that is non-transient and has its own table, except six excluded models: partner, user, notification, followers, channel member, message. Excluded models are either handled in the fixed part or removed automatically by cascade. For each remaining model, two kinds of condition apply:
   - (a) stored email-like fields (normalized email, email, email_from, company_email), matched exactly on the normalized form or by pattern otherwise; when an email field matches, a stored untranslated char record-name also matches on the name;
   - (b) any stored many-to-one to partner whose ondelete is not cascade, matched when it points at a referenced partner.

   [`_get_query`, `_get_query_models_blacklist`]
8. **RISK (scope):** name matching is a pattern match on the raw name without wildcards added. Name hits can over-match (homonyms) or under-match. Relations that cascade on delete, as well as fields other than the listed email fields (phone, address, free text), are not searched. Coverage depends on which modules are installed. [`_get_query`]
9. Running the lookup flushes pending ORM writes, runs one combined raw query, replaces all existing lines and opens the line list. [`action_lookup`]
10. **Archive / unarchive:** toggling the line's active flag writes the active value on the target record with sudo, and records "Archived/Unarchived <model> #id" in the line's details. Bulk archive skips lines whose model has no active field and lines that are already inactive. [`_onchange_is_active`, `action_archive_all`]
11. **Delete:** unlinks the target record with sudo, then records "Deleted <model> #id" and marks the line as unlinked. A second delete raises an error. Bulk delete skips lines already unlinked. The UI asks for confirmation ("irreversible"). [`action_unlink`, `action_unlink_all`; `privacy_lookup_wizard_views.xml`]
12. **Anonymize:** the module has no field-level anonymization action for target records. "Anonymize" appears only in the log's masking of the data subject's name and email. [absence across files; `models/privacy_log.py`]
13. **Privacy action logging:**
    - Whenever the combined execution details change and are non-empty, a `privacy.log` record is created once per wizard.
    - Later changes update the details and the record description of that log.
    - The log stores the masked subject, the acting user, a timestamped list of actions, and the record ids found per model. Technical model names appear only for users in the debug group.

    [`_post_log`, `_compute_execution_details`, `_compute_records_description`]
14. Masking rule: each word keeps its first character and the rest becomes asterisks. The email user part is masked per dot-segment. The domain is masked except its TLD, and three large public domains are kept as-is. [`models/privacy_log.py`]
15. **Exception defect (static observation):** the email-masking helper *returns* a UserError object instead of raising it when the email is empty or has no "@". The object could then be passed as the field value. Whether this path is reachable is unverified, because wizard input is validated first. [`models/privacy_log.py` `_anonymize_email`]
16. The log may record no archive/unlink action at all when the lookup finds records but none are acted on. It is created only once execution details exist. [`_post_log`]

### 2.4 Security
17. ACL: only `base.group_system` has access.
    - Wizard: full CRUD.
    - Line: read, write and create, but not unlink.
    - Log: full CRUD, so administrators can edit or delete audit entries (**RISK** to audit integrity).

    [`security/ir.model.access.csv`]
18. The partner and user server actions ("Privacy Lookup", form binding) are restricted to `base.group_system`. [`wizard/privacy_lookup_wizard_views.xml`]
19. No record rules, and no company scoping on the query or the log.
    - The raw lookup query ignores record rules and multi-company rules, so it finds records in every company.
    - The only filter is the line's record reference, which is cleared when the viewer cannot read the record ("multi-company ir.rule" comment).
    - Archive and delete run with sudo, so they bypass per-record access and company rules.
    - The record name is resolved with sudo, so names of unreadable records can still show.

    **RISK:** a cross-company erasure capability held by system administrators. [`wizard/privacy_lookup_wizard.py`]
20. The target-model selection lists all models through sudo. [`_selection_target_model`]

### 2.5 UI surfaces (names only)
21. The wizard form has a "Lookup" button and a line-count stat button. The line list has buttons "Open Record" and "Delete" (with confirmation) and an inline active toggle. There is a line search view, and window actions "Privacy Lookup" and "Privacy Lookup Line". [`wizard/privacy_lookup_wizard_views.xml`]
22. Server actions:
    - "Privacy Lookup" on the partner and user forms;
    - "Archive Selection" and "Delete Selection" bound to the line list/kanban.

    [`wizard/privacy_lookup_wizard_views.xml`, `data/ir_actions_server_data.xml`]
23. Privacy log list and form views, and window actions "Privacy Logs". The menu path is "Privacy" > "Privacy Logs" under the technical settings menu. The menu xml id contains the typo `pricacy_log_menu` (pointer only). [`views/privacy_log_views.xml`]

### 2.6 Jobs / config
24. No cron or config parameter. Wizard and line data are cleaned up by the standard transient vacuum after 24 hours, but the log persists with no retention rule. [`wizard/privacy_lookup_wizard.py`; absence]

## 3. Cross-module edges
- `mail`: `mail.message` (authorship), `mail.notification`, `mail.followers` and `discuss.channel.member` are referenced by name in the exclusion list. [`_get_query_models_blacklist`]
- `base`: `res.partner`, `res.users`, `ir.model`, `ir.model.data` and `ir.actions.*` are used. The lookup scans every installed module's tables dynamically, so the effective scope grows with each installed module. A special case exists for `mailing.trace`, which belongs to a mass-mailing module not in the dependencies. [`_get_query`]
- Relation to `phone_validation`: none. The lookup does not search phone fields or the phone blacklist. [absence]

## 4. Evidence gaps / contradictions
- G1: The mis-raised error in the email masking helper (finding 15). Whether it can be reached at runtime is unknown.
- G2: Deleting with sudo relies on the target model's own unlink constraints. Cascade and restrict effects on dependent records are not visible from this module.
- G3: There is no module description or documentation of intended legal scope (e.g. GDPR), so purpose is inferred from code.
- G4: The name match is an unanchored equality-style pattern and the email match uses surrounding wildcards. How precise matching is, and how often it produces false positives, cannot be assessed statically.
- G5: The log is editable and deletable by administrators, and there is no immutability or retention control. Whether this is intended is undocumented.
- G6: Tests were not reviewed.

## 5. Limitations
Static source reading only. Source presence does not prove runtime reachability. No runtime proof, no Formal Coverage claim, no GMVQ QID answers. Clean-room abstractions only.
