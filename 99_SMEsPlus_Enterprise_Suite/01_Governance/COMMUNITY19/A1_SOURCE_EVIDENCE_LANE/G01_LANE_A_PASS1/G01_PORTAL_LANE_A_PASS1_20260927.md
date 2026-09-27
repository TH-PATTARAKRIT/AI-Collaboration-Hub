# G01 PLATFORM_BASE — LANE A PASS-1 — Module `portal`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T6 |
| Governed group | G01 PLATFORM_BASE |
| Module | `portal` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/portal/` |
| Retrieval | raw.githubusercontent.com at the anchor commit; files discovered via manifest and `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (static JS/SCSS assets were skipped on purpose, as scoped) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |

## 1. Evidence Pointer Table (31 blobs; SHA-1 = `git hash-object`)

| Path (addons/portal/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 0df9206a8a580649d9c2e81905e3e92a6a109587 | Identity, deps, data list, assets |
| `__init__.py` | 3919eaea7d1be20a9223d30dfb6c978ad09af7d4 | Package imports; global template helper registration |
| `models/__init__.py` | f49f180354e695c6ec17b960cc7ea28f007e5b94 | Model import list |
| `models/portal_mixin.py` | d24085d8da0a56a8b078d0d073aa85d6016f6d79 | Portal document mixin (token, URL, share action) |
| `models/mail_thread.py` | 971d3f790238ae0359f6236fc1a8230b50a97ed0 | Signed-hash token, notification access button, thread access by token/hash |
| `models/mail_message.py` | 179764577eb2216b6c7ae8a9ede2ed54a146106d | Portal message formatting, attachment tokens, author detection |
| `models/res_partner.py` | d8f075eb4038182d04afdab4ea4f78724e167eb5 | Frontend-writable field allow-list; edit-permission helpers |
| `models/res_config_settings.py` | e483cf8160460f8ab79127137ff9145478f5a3c2 | Setting for customer API keys (config param) |
| `models/res_users_apikeys_description.py` | 44c0008fd902b3ac08c57d0eb036b5c5c29bf0ef | Lets portal users create API keys when the setting is on |
| `models/ir_http.py` | c6eec1b127f071b7b1b13e33e6d03bab41dc8eca | Frontend translations; tour session info |
| `models/ir_qweb.py` | f3d09495c872fd70fa197d01d1a74d08ee242c01 | Frontend render environment values |
| `models/ir_ui_view.py` | 791fcf49f1b25d052243b313d90325b9f792c6f1 | Adds the `customize_show` view flag |
| `controllers/__init__.py` | 633f88e75383c61cfab65c7437022037ca3a62d7 | Controller import list |
| `controllers/portal.py` | e6b03c24fa227c362a20d6811cfa5c59cf717f02 | `/my/*` routes, address management, security page, document access check, report render |
| `controllers/portal_thread.py` | 363bc48c39bb0b30dc082b2be9154a66d405923b | Portal chatter init, fetch, avatar, internal flag |
| `controllers/thread.py` | 8384c8d57d0163c6546fa5868d165e99327d2b83 | Author attribution and edit rights for public posters |
| `controllers/message_reaction.py` | bd84a5e258d609bf919b6280a53945d6dc4d21bd | Reaction author from a portal token |
| `controllers/mail.py` | aef21b45f04ef933521f41dd7013f0a9e9b01e1f | `/mail/view` redirect with token; unfollow route |
| `controllers/web.py` | fa0f57fc072de43cac21eee7740db949c63676be | Redirects non-internal users to `/my` |
| `utils.py` | b83ac0a1415ab9c1c5b7acd8c8d5c2c38c3417d1 | Constant-time token/hash validators; portal partner resolution |
| `wizard/__init__.py` | fe113bb98e2aba169f9a05f6fdbe7c2ad13e08e2 | Wizard import list |
| `wizard/portal_wizard.py` | 368f4c1d369892aaefb4e16b5632e6e7b3486cc8 | Grant/revoke/re-invite portal user wizard |
| `wizard/portal_wizard_views.xml` | 9d3bf34325212e0925b3f7fc37bf011ef13bb5c5 | Server action bound to contacts; wizard form |
| `wizard/portal_share.py` | b0491d4e3517118f94fa7dc439b46f324bf8f5f3 | Share-document wizard |
| `wizard/portal_share_views.xml` | e0528c252e938435c72eb5bb933459e6283c5ecc | Share wizard form and action |
| `security/ir.model.access.csv` | 6506676a9e55e5ccb7f2d578b1c7804efbb2142e | ACL (3 rows) |
| `data/mail_templates.xml` | 1d3bda61a84eda9d6ce9ec11b15583e7d560f111 | Share invitation body template (noupdate) |
| `views/portal_templates.xml` | 7ef359dfa8ffce659311fcbb35a9cd50b86093a3 | Portal layout, home, security, chatter, sidebar templates |
| `views/address_templates.xml` | 3e2aed701cb6fcadd96a36ecad55f1a500e94d84 | Contact details and address management templates |
| `views/mail_templates_public.xml` | 13765d20790343833972679902212abc33507010 | Unfollow page uses the portal layout |
| `views/res_config_settings_views.xml` | 862a35865bc3bde0080282165436e058c59c9759 | API-key setting (debug-mode only) |

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
- P-M1: The module is the base layer for a customer-facing portal. It supplies a base controller and base templates, and business modules extend them with their own document pages. Its category is Hidden and its licence is LGPL-3. [`__manifest__.py`]
- P-M2: It depends on `web`, `html_editor`, `http_routing`, `mail` and `auth_signup`. It does not depend on `website`. The manifest describes it as usable without website editing. [`__manifest__.py`]
- P-M3: Data load order: ACL, then mail template, then address, public-mail, portal and settings views, then the share and grant-access wizard views. There is no demo data and no cron. [`__manifest__.py`]
- P-M4: At import time the package registers a global URL-slug helper for templates. WHY: portal templates can build readable record URLs. [`__init__.py`]

### 2.2 Data (models, mixins, key fields, constraints)
- P-D1: `portal.mixin` is an abstract capability that a business document inherits to become portal-visible. It adds a computed access URL (default placeholder `#`), an access token that is not copied on duplicate and can be searched only with in/not-in, and a computed access warning (empty by default). Business modules are expected to override the URL and the warning. [`models/portal_mixin.py`]
- P-D2: The `mail.thread` extension declares the token field used for external posting (`_mail_post_token_field`, which defaults to the access token). It also adds a website-messages relation, filtered to customer-visible message types, that skips search access checks. [`models/mail_thread.py`]
- P-D3: Two transient wizards manage portal users: `portal.wizard` and `portal.wizard.user`. A wizard line carries the contact, an editable email, the linked user (computed with elevated rights), last login, portal/internal flags and an email status (valid / invalid / already registered). [`wizard/portal_wizard.py`]
- P-D4: `portal.share` is a transient wizard. It holds the target model and id, a computed record reference, recipients, a note, the computed share link and the access warning. [`wizard/portal_share.py`]
- P-D5: The `res.partner` extension defines a fixed allow-list of contact and address fields that portal/public users may change: name, phone, email, street lines, city, state, country, zip, VAT and company name. [`models/res_partner.py`]
- P-D6: The module adds no SQL or Python constraints of its own. Integrity depends on validation in the wizard and controller logic.

### 2.3 Business rules / states / lifecycle / exceptions
- P-B1 **Access token lifecycle**: a token (a random UUID) is created lazily the first time a share URL or portal URL is requested. The write runs with elevated rights, so a user who can read the record can mint its token. The portal module has no path that rotates or expires tokens. RISK: a token is a long-lived bearer credential for as long as the record exists. [`models/portal_mixin.py`]
- P-B2 **Share URL**: the share URL checks read access before it embeds a token. It can also add a partner id plus a signed hash (to identify the chatter author) and signup parameters. The redirect form goes through `/mail/view`. [`models/portal_mixin.py`]
- P-B3 **Signed hash**: this is an HMAC-SHA256 over the database name, the record's post-token value and the partner id, keyed with the database secret. It raises an error if the model has no token field. A parent-record hash hook exists and defaults to none. [`models/mail_thread.py`, `utils.py`]
- P-B4 **Access action**: when an external (share) user opens a document, or when website view is forced, they are sent to the tokenized portal URL if they can read the record. Otherwise the standard backend action applies. [`models/portal_mixin.py`]
- P-B5 **Notifications**: for portal-enabled documents, the customer recipient gets an access button carrying a token, pid, hash and signup parameters. The token is created with elevated rights. The generic portal recipient group is switched on with an access button. [`models/mail_thread.py`]
- P-B6 **Grant access** (the preconditions below produce user-facing errors):
  - Preconditions: the email is valid and not used by another user's login, and the contact does not already have portal or internal access.
  - The partner email is updated if the user edited it.
  - A new user is created from the template in the partner's company, falling back to the current company. Creation runs with elevated rights.
  - The user is activated, added to the portal group and removed from the public group.
  - Signup is prepared and an invitation email is sent with the set-password template, which is owned by auth_signup.
  - Source: [`wizard/portal_wizard.py`]
- P-B7 **Revoke access**: this requires the contact to currently have portal access. It clears the partner's signup type, which invalidates the signup token, and archives the portal user. The user stays in the portal group. Internal users are never archived by this path. [`wizard/portal_wizard.py`]
- P-B8 **Re-invite**: this requires existing portal access and a unique, valid email. It re-sends the invitation. [`wizard/portal_wizard.py`]
- P-B9 **Wizard defaults**: selected partners are expanded to include their child contacts of type contact or other. The expansion reads partners with elevated rights. [`wizard/portal_wizard.py`]
- P-B10 **Share wizard dispatch**:
  - If the record has a token, or B2C signup is not enabled (config param `auth_signup.invitation_scope`), every recipient gets the public link.
  - Otherwise only existing users get the public link, and non-users get individual signup links that redirect to the record.
  - Mails are posted on the record as internal notes in the recipient's language.
  - Source: [`wizard/portal_share.py`]
- P-B11 **Customer address edits**:
  - A customer can edit their own partner, and child partners of type invoice, delivery or other under their commercial entity.
  - VAT can be edited only on the commercial entity (no parent).
  - Archiving the main address is refused.
  - Form fields are filtered through the frontend-writable allow-list.
  - Source: [`models/res_partner.py`, `controllers/portal.py`]
- P-B12 **Account self-service**:
  - Password change requires the old password and matching confirmation, then refreshes the session token.
  - Account deactivation requires typing the login again and passing an interactive credential check. The deactivation routine is called with elevated rights and the session is logged out.
  - Source: [`controllers/portal.py`]
- P-B13 **Pending attachment removal**: removal is allowed only if the attachment is still in the pending composer state and is not linked to any message. Access is by ACL or a valid token. [`controllers/portal.py`]
- P-B14 **Report rendering**: allowed types are html, pdf and text. A multi-company record set is refused. Rendering runs with elevated rights, scoped to the record's company. [`controllers/portal.py`]

### 2.4 Security (groups, ACL, record rules, tokens, sudo, company scoping)
- P-S1 ACL: create, read and write on the three wizard models is limited to `base.group_partner_manager`, with no unlink. The module defines no groups and no record rules. [`security/ir.model.access.csv`]
- P-S2 **Central document gate** (`_document_check_access`): the record is loaded as superuser. If the normal read check fails, access falls back to a constant-time comparison with the stored token. On success the caller receives a record with superuser rights. RISK: once access passes, any action on the returned record bypasses ACL and record rules. [`controllers/portal.py`]
- P-S3 Chatter thread access: the core check is tried first, then signed hash + pid or token, using constant-time comparisons. The allowed access parameters are extended with hash, pid and token. [`models/mail_thread.py`, `utils.py`]
- P-S4 Portal message fetch runs with elevated rights after the thread access check, restricted to share-visible, non-empty messages of that record. Attachment and avatar data likewise use elevated reads after a token check. [`controllers/portal_thread.py`, `models/mail_message.py`]
- P-S5 Public posters are attributed to the partner resolved from the hash/pid or the token. The same resolution lets them edit their own messages and react. RISK: anyone holding a leaked token can post as the document's customer. [`controllers/thread.py`, `controllers/message_reaction.py`, `utils.py`]
- P-S6 The `/mail/view` redirect: when the user lacks access but supplies a valid token, they are redirected to the portal URL, with pid/hash kept. The public user is used when there is no session. [`controllers/mail.py`]
- P-S7 The address routes browse partners with elevated rights, then enforce the ownership check and return Forbidden otherwise. The country-info route is public and reads states with elevated rights. [`controllers/portal.py`]
- P-S8 The `/mail/update_is_internal` route (authenticated) writes the internal flag with no portal-specific check. It relies on the mail.message ACL and rules, which live outside this module. [`controllers/portal_thread.py`]
- P-S9 API keys: when the config param `portal.allow_api_keys` is set, portal users may create API keys. Other non-internal users are refused. The setting is shown only in debug mode (`base.group_no_one`). [`models/res_users_apikeys_description.py`, `models/res_config_settings.py`, `views/res_config_settings_views.xml`]
- P-S10 Security and account pages send headers that forbid framing by other origins (clickjacking defence). [`controllers/portal.py`]
- P-S11 Company scoping appears only where users are created (partner company, falling back to the current company) and where reports are rendered (record company, multi-company refused). There is no company rule on portal data in this module.

### 2.5 UI surfaces (names only)
- Routes in `controllers/portal.py`:
  - `/my`, `/my/home`, `/my/counters`, `/my/account`, `/my/addresses`
  - `/my/address` (GET), `/my/address/submit` (POST), `/my/address/archive`, plus a public country-info route
  - `/my/security`, `/my/deactivate_account`
  - `/portal/attachment/remove`
- Routes in `controllers/portal_thread.py`: `/portal/chatter_init`, `/mail/chatter_fetch`, `/mail/avatar/mail.message/<id>/author_avatar/<w>x<h>`, `/mail/update_is_internal`.
- Routes in `controllers/mail.py`: `/mail/unfollow`.
- Web client (`controllers/web.py`): index and web-client overrides, plus the login redirect, send non-internal users to `/my`.
- Backend: the server action "Grant portal access" is bound to contacts. The share action binds to its own wizard model, so it is reached through `action_share`, not a contact menu. Neither module ships a menu.
- Templates: portal layout, home, docs entry, sidebar, security, message thread, pager, contact details and address management.

### 2.6 Jobs / config
- No crons. Config params read or written: `portal.allow_api_keys`, `database.secret` (HMAC key), `auth_signup.invitation_scope`.

## 3. Cross-module edges
- X1 `mail`: the thread and message extensions, notification groups, `/mail/view` and chatter controllers.
- X2 `auth_signup`: signup preparation and auth parameters, the set-password invitation template, and the signup type used for revocation.
- X3 `base`: portal, public and partner-manager groups, user template creation, and API-key descriptions.
- X4 Soft references to modules not in the dependency list:
  - `web_tour` (tour session info)
  - `website.group_website_restricted_editor` (chatter publisher flag)
  - an optional VAT check that is present when accounting is installed
- X5 Downstream: business modules inherit `portal.mixin` and extend `CustomerPortal`. Access URL, access warning, parent-hash hook and home counters are all override points.

## 4. Evidence gaps / contradictions
- G1 The deactivation routine and the user-template creation are defined outside portal (base/auth_signup), so their behaviour was not read here.
- G2 `mail.message._get_search_domain_share` and the core `_get_thread_with_access` are in `mail` and were not read. The exact visibility set for customers is not proven.
- G3 JS/SCSS assets were not reviewed, as scoped. Client-side token handling is unverified.
- G4 The share action binding target looks unusual (it binds to its own model). Whether the action is reachable from contact screens can only be confirmed at runtime.
- G5 No token expiry or rotation was found in portal. Whether another module provides it is unknown.
- No contradictions found.

## 5. Limitations
- Static source evidence only. Source presence does not prove runtime reachability. No runtime proof, no Formal Coverage claim, no percentages. GMVQ QIDs are not answered here.
