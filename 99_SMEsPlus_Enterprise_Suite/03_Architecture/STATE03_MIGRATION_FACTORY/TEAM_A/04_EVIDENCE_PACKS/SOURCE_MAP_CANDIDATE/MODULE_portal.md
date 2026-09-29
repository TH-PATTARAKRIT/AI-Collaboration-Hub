# Source Map (candidate) — `portal`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `portal` |
| Display name | Customer Portal |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4415ca5bfdb7bfe9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/portal/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`, `html_editor`, `http_routing`, `mail`, `auth_signup`
- Direct dependents in 300-module list (15): `account`, `auth_passkey_portal`, `auth_password_policy_portal`, `auth_totp_portal`, `digest`, `event`, `loyalty`, `mail_group`, `payment`, `portal_rating`, `project`, `spreadsheet` … (+3)
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `mass_mailing_sms`, `test_mail_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Customer Portal
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 2, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 5, web routes 6
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `portal.share` (Portal Sharing); `portal.wizard` (Grant Portal Access); `portal.wizard.user` (Portal User Config); `portal.mixin` (Portal Mixin)
- Objects extended from other modules (8): `ir.http`, `mail.thread`, `ir.ui.view`, `ir.qweb`, `res.config.settings`, `mail.message`, `res.partner`, `res.users.apikeys.description`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `portal.share` ← Community: `project`; open-license custom/third-party scanned: —
- `portal.wizard.user` ← Community: `website`; open-license custom/third-party scanned: —
- `portal.mixin` ← Community: `account`, `l10n_in_ewaybill`, `point_of_sale`, `project`, `purchase`, `sale`, `test_mail_full`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `mail.thread`, `ir.ui.view`, `ir.qweb`, `res.config.settings`, `mail.message`, `res.partner`, `res.users.apikeys.description`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 87 of 91 source pointers resolve to an existing file and in-range line (4 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — portal
Source revision: 19.0.post20260921 | Module: "Customer Portal" (portal/__manifest__.py:4) | License LGPL-3 | Category Hidden (:6)
Basis: static reading of manifest, models, wizards, controllers, security CSV; selected tests marked (TEST). Skeleton: sourcemap/portal.json (orientation only).

## A. Capabilities; core vs optional vs conditional
- A1. Foundation layer for the external-user (customer/vendor) portal; provides base controller and templates only. Business modules add their own pages. portal/__manifest__.py:7-11
- A2. Depends on web, html_editor, http_routing, mail, auth_signup. No auto_install and not an application; it is a hidden infrastructure module pulled in by others. portal/__manifest__.py:12 (no auto_install key present)
- A3. Capability: a reusable "portal document" behaviour (share link + secret access token + web address) that any business document can adopt. portal/models/portal_mixin.py:9-19
- A4. Capability: staff-side sharing of a document with chosen contacts by email. portal/wizard/portal_share.py:6-28, 98-110
- A5. Capability: staff-side grant / revoke / re-invite of portal login for contacts. portal/wizard/portal_wizard.py:15-20, 133-200
- A6. Capability: customer self-service pages — home dashboard (/my), account details, address book (add/edit/archive), password change, account deletion, optional API keys. portal/controllers/portal.py:184-198, 219-236, 349-393, 465-493, 858-867, 871-937
- A7. Capability: portal chatter (message thread on a shared document) for authenticated and token-identified visitors. portal/controllers/portal_thread.py:31-106
- A8. Conditional: customer API keys are off unless a system parameter is set; the toggle appears only in developer-mode settings. portal/models/res_users_apikeys_description.py:15-20; portal/views/res_config_settings_views.xml:12-14
- A9. Conditional: pager/breadcrumb/searchbar/docs-entry templates are shared building blocks for business modules. portal/views/portal_templates.xml:124,144,204,237,311,663
- A10. External users landing: non-internal users hitting the backend root or web client, or logging in without a redirect, are sent to /my. portal/controllers/web.py:13-27; (TEST) portal/tests/test_login.py:10-14

## B. Business objects, relationships, lifecycle
- B1. Portal Mixin (abstract): adds web address, secret token (not copied on duplicate), and an access warning text to any adopting document. portal/models/portal_mixin.py:13-19. Adopters found: sale order, purchase order, invoices/journals (account), project and task, e-way bill (l10n_in_ewaybill). sale/models/sale_order.py; purchase/models/purchase_order.py; account/models/account_move.py; project/models/project_project.py; project/models/project_task.py; l10n_in_ewaybill/models/l10n_in_ewaybill.py (module-level pointers, grep result)
- B2. Token lifecycle: created lazily the first time a link is needed; once set it is reused (no expiry logic in this module). portal/models/portal_mixin.py:34-39. UNKNOWN — EVIDENCE INSUFFICIENT whether any adopter regenerates or expires tokens.
- B3. Message thread extension: every mail-thread record gains a "website messages" view limited to comment/email-type messages, bypassing search access. portal/models/mail_thread.py:15-18
- B4. Portal Sharing wizard (transient): target document (model + id), recipient contacts (required), optional note, generated link, warning text. portal/wizard/portal_share.py:24-30
- B5. Grant Portal Access wizard (transient) with one line per contact: contact, editable email, linked user, latest login, is-portal / is-internal flags, email status (valid / invalid / already registered). portal/wizard/portal_wizard.py:32-34, 81-93
- B6. Contact selection for the wizard: the chosen partners plus their child contacts of type "contact" or "other". portal/wizard/portal_wizard.py:23-30
- B7. Access lifecycle for a contact: no user -> user created in portal group and activated -> may be revoked (user archived, signup type cleared, stays in portal group) -> may be granted again. portal/wizard/portal_wizard.py:150-187; (TEST) portal/tests/test_portal_wizard.py:179-201
- B8. Revoked users used to sit in the public group; granting again adds portal and removes public. portal/wizard/portal_wizard.py:158-159; (TEST) portal/tests/test_portal_wizard.py:80-118
- B9. Account deletion lifecycle (customer-initiated): credentials wiped and login renamed, API keys removed, user queued for deletion; the deletion job later removes it. base/models/res_users.py:934-975 (owner: base); route in portal/controllers/portal.py:914-937; (TEST) portal/tests/test_portal.py:52-90
- B10. Address book: customer main address plus child addresses (billing = invoice/other types; delivery = delivery/other types) under the commercial partner. portal/controllers/portal.py:238-262; portal/models/res_partner.py:51-55

## C. Validations, automation, security, multi-company
- C1. Model access: only the "Contact Creation" group (base.group_partner_manager) may read/write/create the three wizards; no delete. portal/security/ir.model.access.csv:2-4. (TEST) Ordinary employees are refused on the portal wizard. portal/tests/test_portal_wizard.py:44-55
- C2. No record rules, no groups, no scheduled jobs defined in this module (skeleton: rules [] groups [] crons []). Group definitions for portal/public/internal are owned by base.
- C3. Token-based bypass: a document can be opened by someone without read rights if the supplied token equals the document token (constant-time comparison). portal/controllers/portal.py:961-980; portal/controllers/mail.py:38-56
- C4. Signed identity for chatter: a keyed hash of (database, document token, contact id) proves which contact opened the shared link; parent-record hash accepted as alternative when the model supplies one. portal/models/mail_thread.py:65-90; portal/utils.py:6-13. The signing secret is the database secret system parameter. portal/models/mail_thread.py:80
- C5. Sharing precondition: generating a link requires the sharer to have read access on the document. portal/models/portal_mixin.py:63-65
- C6. Recipients who are not yet users: if signup is open to everyone (invitation scope "b2c") and the document has no token, they receive an individual signup link; otherwise a token link is sent to all recipients. portal/wizard/portal_share.py:98-108. Signup scope parameter is owned by auth_signup (auth_signup/models/res_users.py:88-89; default set to b2c in auth_signup/data/ir_config_parameter_data.xml:5).
- C7. Grant wizard validations: invalid email or an email equal to another existing user's login blocks grant/re-invite; internal users cannot be granted or revoked; a contact already portal cannot be granted again; revoke only for active portal users. portal/wizard/portal_wizard.py:95-108, 141-146, 174-175, 235-241; (TEST) portal/tests/test_portal_wizard.py:120-160
- C8. Email on the contact is updated from the wizard when it is valid and different. portal/wizard/portal_wizard.py:243-247; (TEST) portal/tests/test_portal_wizard.py:57-78
- C9. Multi-company: a newly created portal user takes the contact's company, else the current company; user is limited to the company set of the creating environment. portal/wizard/portal_wizard.py:155-156, 211-217; (TEST) portal/tests/test_portal_wizard.py:162-177
- C10. Reports on the portal refuse records spanning several companies and render under the record's company. portal/controllers/portal.py:1023-1028
- C11. Address editing rules: customer may edit own address and child addresses (invoice/delivery/other) of their commercial partner; otherwise forbidden. portal/models/res_partner.py:32-42; portal/controllers/portal.py:381-382, 488-489
- C12. Writable customer fields whitelist: name, phone, email, street lines, city, state, country, zip, VAT, company name. portal/models/res_partner.py:16-19
- C13. Address validation: email format; VAT check only if accounting is installed; name/email locked for partners linked to internal users; commercial fields locked on sub-addresses; country change blocked and VAT change on the commercial entity blocked when the base hooks say documents were issued (base hooks return "allowed"; adopters override). portal/controllers/portal.py:659-735, 737-753; portal/models/res_partner.py:21-30. (TEST) portal/tests/test_addresses.py:82-94, 121-153, 171-185
- C14. Mandatory address fields: name, email always; phone, street, city, country (plus state / zip when the country requires them) when an address is needed; providing any address field makes the whole address required. portal/controllers/portal.py:293-347, 771-775
- C15. Main address cannot be archived; only editable child addresses can. portal/controllers/portal.py:858-867; (TEST) portal/tests/test_addresses.py:277-320
- C16. New address is stored under the commercial partner (if active), with language of the visitor, company of the current partner, and type derived from billing/delivery/both. portal/controllers/portal.py:789-814
- C17. Account deletion requires typing the login and the current password; only external (share) users can be deleted this way. portal/controllers/portal.py:914-932; base/models/res_users.py:944-950
- C18. Chatter visibility: portal viewers see only non-internal message types (share-domain), non-empty messages; author avatar shown only if a valid token or signed identity is presented. portal/controllers/portal_thread.py:13-29, 89-120
- C19. Public visitors posting to a shared document are attributed to the identified contact; only the same contact may edit that message. portal/controllers/thread.py:10-26
- C20. Only a signed-in user may flip a message's internal flag via the portal route (no extra rule here; underlying message write rights apply). portal/controllers/portal_thread.py:125-129
- C21. Attachment removal from portal only for pending compose attachments not linked to any message, requiring read access or the token. portal/controllers/portal.py:939-957
- C22. Password change: all three fields required, confirmation must match, old password checked; session token refreshed. portal/controllers/portal.py:890-912
- C23. Notification emails on portal-enabled records add a "customer" recipient group with a link carrying token, signed hash, and signup parameters; portal-group recipients get a button. portal/models/mail_thread.py:20-63

## D. Handoffs
- D1. Users, groups (portal/public/internal), account deletion queue, password change: base. base/models/res_users.py:934-975
- D2. Signup token, invitation scope, "Portal: new user" email template, partner signup preparation: auth_signup. portal/wizard/portal_wizard.py:223, 161; auth_signup/models/res_users.py:88-89
- D3. Message/thread engine, follower notifications, unfollow link, blacklist on account deletion: mail. portal/controllers/mail.py:59-61; mail/models/res_users.py:358-380
- D4. Phone normalisation after address save: phone_validation (conditional). portal/controllers/portal.py:553-563; phone_validation/models/res_users.py:10-20
- D5. VAT validation: account/base_vat chain via the partner check hook (conditional on availability). portal/controllers/portal.py:739-753
- D6. Business portals that adopt the mixin / extend the customer portal controller: sale, sale_management, sale_project, sale_stock, sale_timesheet, purchase, account, account_peppol, project, hr_timesheet, payment, loyalty, mrp_subcontracting, snailmail_account, website_sale, website_sale_loyalty, website_profile, website_crm_partner_assign, auth_password_policy_portal. (grep of controller classes; module-level)
- D7. Website layout, pager template, published-website context on the portal routes: website (routes flagged for website). portal/controllers/portal.py:175,184,190; portal/controllers/portal_thread.py:31-35
- D8. API key creation rules: base (users API keys); portal adds a conditional exception. portal/models/res_users_apikeys_description.py:11-20

## E. Configuration / defaults that change outcomes
- E1. "Customers can generate API Keys" (system parameter portal.allow_api_keys), shown only in developer mode; when off, portal users cannot create keys; when on, portal (but not other non-internal) users may. portal/models/res_config_settings.py:16-27; portal/models/res_users_apikeys_description.py:15-20; portal/views/res_config_settings_views.xml:12-14
- E2. Signup scope (b2b vs b2c) decides whether unregistered recipients get signup links. portal/wizard/portal_share.py:99-108
- E3. Items per page on portal lists defaults to 80; generic pager default 30. portal/controllers/portal.py:22,144
- E4. Share warning text is empty by default; adopters can set it. portal/models/portal_mixin.py:26-28
- E5. Whether an address is "needed" defaults to yes; other modules may say no (e.g. quick checkout). portal/controllers/portal.py:331-333
- E6. "Use Pictograms" home layout is an active, customizable view option. portal/views/portal_templates.xml:258
- E7. Grant wizard sets no password mail at creation and sends a separate invitation instead. portal/wizard/portal_wizard.py:211

## F. Effective extension path (module names only)
- Adopting documents: sale, purchase, account, project, l10n_in_ewaybill. Controller extenders: sale, sale_management, sale_project, sale_stock, sale_timesheet, purchase, account, account_peppol, project, hr_timesheet, payment, loyalty, mrp_subcontracting, snailmail_account, website_sale, website_sale_loyalty, website_profile, website_crm_partner_assign, auth_password_policy_portal. Partner extenders for edit rules: sale/website_sale-type modules (UNKNOWN — EVIDENCE INSUFFICIENT which override _can_edit_country / can_edit_vat; not read).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: token expiry or revocation policy for shared links.
- UNKNOWN — EVIDENCE INSUFFICIENT: content of portal templates beyond names (views not read line by line).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end interaction scripts (signature form, chatter boot) behaviour.
- UNKNOWN — EVIDENCE INSUFFICIENT: per-adopter record rules for customers/vendors (owned by sale/purchase/account/project, not read here).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the pending-attachment removal route has additional restrictions beyond those seen.

