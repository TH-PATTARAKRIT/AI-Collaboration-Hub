# Source Map (candidate) — `google_gmail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `google_gmail` |
| Display name | Google Gmail |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f3849f750adaae53` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/google_gmail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `google.gmail.mixin` (Google Gmail Mixin)
- Objects extended from other modules (4): `ir.mail_server`, `res.users`, `fetchmail.server`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.mail_server`, `res.users`, `fetchmail.server`, `res.config.settings`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 37 of 37 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — google_gmail
Source revision: 19.0.post20260921 | Module: "Google Gmail" v1.2, category Hidden, LGPL-3 (google_gmail/__manifest__.py:5-7,20). Basis: static reading; one token-lifetime unit test read (TEST).

## A. Capabilities and optionality
- A1. Lets outgoing (SMTP) and incoming (IMAP) mail servers, and personal outgoing servers of users, connect to a Gmail account through Google's sign-in and consent flow (OAuth) instead of a stored password. google_gmail/__manifest__.py:8; google_gmail/models/ir_mail_server.py:16-18; google_gmail/models/fetchmail_server.py:12; google_gmail/models/res_users.py:9-12
- A2. Conditional: auto_install on with only mail as dependency, yet mail Settings also shows a "Support Gmail Authentication" toggle for it. google_gmail/__manifest__.py:9-11,18; mail/models/res_config_settings.py:23; mail/views/res_config_settings_views.xml:41-42
- A3. Credentials of the company's own Google app (ID and secret) are entered in mail Settings; without both, the connect button relies on an Odoo-run intermediary service that is refused in Community builds ("Please configure your Gmail credentials"). google_gmail/models/res_config_settings.py:10-11; google_gmail/models/google_gmail_mixin.py:85-92,94-124
- A4. Incoming servers: server type "Gmail OAuth Authentication" fixes host imap.gmail.com, port 993, SSL; connection type is always IMAP. google_gmail/models/fetchmail_server.py:12,28-34,54-59
- A5. Outgoing servers: authentication "Gmail OAuth Authentication" fixes smtp.gmail.com, port 587, STARTTLS; users' personal outgoing type "Gmail" preloads these. google_gmail/models/ir_mail_server.py:35-40; google_gmail/models/res_users.py:14-22

## B. Objects and lifecycle
- B1. Adds shared token fields to servers (refresh token, access token, expiry, authorization link), readable only by administrators; not copied on duplicate. google_gmail/models/google_gmail_mixin.py:35-40
- B2. Lifecycle: save server -> "Connect your Gmail account" opens Google consent -> callback stores refresh/access tokens and reactivates the server -> "Gmail Token Valid" badge shown -> each send/fetch renews the access token when within about 10 seconds of expiry. google_gmail/views/ir_mail_server_views.xml:9-28; google_gmail/controllers/main.py:117-123; google_gmail/models/google_gmail_mixin.py:16-20,244-265. (TEST) three timing cases reuse/renew the token: google_gmail/tests/test_google_gmail.py:20-73
- B3. Changing away from Gmail clears the stored tokens. google_gmail/models/ir_mail_server.py:41-44; google_gmail/models/fetchmail_server.py:35-38

## C. Validations, automation, security, external service
- C1. Gmail SMTP server must have empty password, "TLS (STARTTLS)" security, and a username (the Gmail address). google_gmail/models/ir_mail_server.py:52-69
- C2. Gmail IMAP server must use SSL. google_gmail/models/fetchmail_server.py:22-26
- C3. Sender restriction: the server's "from filter" is set to the Gmail username so only matching sender addresses can use it unless a default-from system parameter is set. google_gmail/models/ir_mail_server.py:22-25,46-50
- C4. Only an administrator can start the connection; the server needs a valid email address. google_gmail/models/google_gmail_mixin.py:78-83
- C5. Callback protection: signed anti-forgery token tied to model and record; only models using this mixin accepted; failure returns forbidden. google_gmail/controllers/main.py:70-88; google_gmail/models/google_gmail_mixin.py:267-278
- C6. Identity check: for personal servers, or when a non-administrator completes it, the signed-in Google address must be verified and equal to the server's email or the connection is rejected. Administrator-set shared servers skip this check. google_gmail/controllers/main.py:90-115
- C7. External services and credentials: accounts.google.com (consent), oauth2.googleapis.com (token exchange, 5-second timeout), googleapis userinfo. Client secret is stored as a system parameter; tokens stored on the server record. google_gmail/models/google_gmail_mixin.py:53-66,158-200; google_gmail/controllers/main.py:95-99. Requested permission scope is full Gmail mailbox access plus email address. google_gmail/models/google_gmail_mixin.py:30-32
- C8. Security file/record rules: none in this module; rights follow mail-server and fetchmail models (owners: base/mail). Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Outgoing servers: base (ir.mail_server). Incoming servers: mail (fetchmail.server). Personal outgoing server setup end action: users/mail. google_gmail/models/ir_mail_server.py:13; google_gmail/models/fetchmail_server.py:9-10; google_gmail/models/res_users.py:24-28
- D2. Settings host: mail. google_gmail/views/res_config_settings_views.xml:7
- D3. Sibling with the same pattern for Microsoft: microsoft_outlook.

## E. Configuration that changes outcomes
- E1. System parameters google_gmail_client_id / google_gmail_client_secret (Google app) decide direct vs intermediary flow. google_gmail/models/google_gmail_mixin.py:43-46,158-163
- E2. mail.server.gmail.iap.endpoint (intermediary endpoint, default gmail.api.odoo.com) applies to non-Community builds only. google_gmail/models/google_gmail_mixin.py:33,94-98
- E3. mail.default.from system parameter widens which senders may use the server (mentioned in help text only). google_gmail/models/ir_mail_server.py:24-25

## F. Extension path
- mail (fetchmail, settings), base (ir.mail_server), users; microsoft_outlook (parallel design).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: incoming-mail processing rules (fetchmail cron and routing owned by mail, not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: Enterprise intermediary service behaviour (external).
- UNKNOWN — EVIDENCE INSUFFICIENT: Google app verification/quota requirements for the tenant's own credentials (external).

