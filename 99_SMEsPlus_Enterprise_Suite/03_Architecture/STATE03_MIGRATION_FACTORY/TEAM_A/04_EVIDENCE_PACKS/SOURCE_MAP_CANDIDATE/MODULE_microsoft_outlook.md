# Source Map (candidate) — `microsoft_outlook`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `microsoft_outlook` |
| Display name | Microsoft Outlook |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `85d860aa6f17a1cf` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/microsoft_outlook/` |
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
- Objects introduced (1): `microsoft.outlook.mixin` (Microsoft Outlook Mixin)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 42 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — microsoft_outlook
Source revision: 19.0.post20260921 | Module: "Microsoft Outlook" v1.1, category Hidden, LGPL-3 (microsoft_outlook/__manifest__.py:5-7,20). Basis: static reading; two unit tests read (TEST).

## A. Capabilities and optionality
- A1. Lets outgoing (SMTP) mail servers, incoming (IMAP) mail servers and users' personal outgoing servers connect to a Microsoft Outlook / Office 365 mailbox through Microsoft's sign-in and consent flow (OAuth) instead of a stored password. microsoft_outlook/__manifest__.py:8; microsoft_outlook/models/ir_mail_server.py:18-20; microsoft_outlook/models/fetchmail_server.py:16; microsoft_outlook/models/res_users.py:9-12
- A2. Conditional: auto_install on with only mail as dependency; mail Settings also shows a "Support Outlook Authentication" toggle. microsoft_outlook/__manifest__.py:9-11,18; mail/models/res_config_settings.py:24; mail/views/res_config_settings_views.xml:50-52
- A3. Company's own Microsoft app ID and secret are entered in Settings; without both, the connect action relies on an Odoo-run intermediary that is refused outside Enterprise builds ("Please configure your Outlook credentials"). microsoft_outlook/models/res_config_settings.py:10-11; microsoft_outlook/models/microsoft_outlook_mixin.py:85-92
- A4. Incoming servers: type "Outlook OAuth Authentication" presets imap.outlook.com, port 993, SSL; always IMAP. microsoft_outlook/models/fetchmail_server.py:16,32-38,58-63
- A5. Outgoing servers: authentication "Outlook OAuth Authentication" presets STARTTLS port 587; personal server type "Outlook" is offered on the user. microsoft_outlook/models/ir_mail_server.py:57-62; microsoft_outlook/models/res_users.py:9-22

## B. Objects and lifecycle
- B1. Adds token fields (refresh, access, expiry, authorization link) to both server types, administrator-readable only, not copied on duplicate. microsoft_outlook/models/microsoft_outlook_mixin.py:31-40
- B2. Lifecycle: save server -> connect -> Microsoft consent -> callback stores tokens and reactivates the record -> each send/fetch renews the access token when within about 10 seconds of expiry; using an unconnected server is refused ("connect first"). microsoft_outlook/controllers/main.py:114-120; microsoft_outlook/models/microsoft_outlook_mixin.py:20,246-266
- B3. Changing away from Outlook clears stored tokens. microsoft_outlook/models/ir_mail_server.py:63-66; microsoft_outlook/models/fetchmail_server.py:39-43

## C. Validations, automation, security, external service
- C1. Outlook SMTP server must have empty password, STARTTLS security, and a username (the mailbox address). microsoft_outlook/models/ir_mail_server.py:30-47
- C2. Outlook IMAP server must use SSL. microsoft_outlook/models/fetchmail_server.py:26-30. (TEST) a valid Outlook incoming server authenticates with the stored access token and opens INBOX (microsoft_outlook/tests/test_fetchmail_outlook.py:15-40); creating one with incomplete settings raises a user error (:42-49).
- C3. The server's sender filter is set to the username so only matching sender addresses may use it unless the mail.default.from parameter widens it. microsoft_outlook/models/ir_mail_server.py:25-27,68-72
- C4. Personal Outlook servers have a lower send cap per minute (default 10, parameter mail.server.personal.limit.minutes_outlook) than the generic personal-server cap (default 30). microsoft_outlook/models/ir_mail_server.py:83-92; mail/models/ir_mail_server.py:101-106
- C5. Only administrators can start a connection; a valid email address is required. microsoft_outlook/models/microsoft_outlook_mixin.py:77-83
- C6. Callback protection: signed anti-forgery token tied to model+record, only mixin models accepted, otherwise forbidden. microsoft_outlook/controllers/main.py:69-87; microsoft_outlook/models/microsoft_outlook_mixin.py:268-279
- C7. Identity check: for personal servers or non-administrator completion, a fresh token is requested and the mailbox email in it must equal the server email, else rejected; administrator-set shared servers skip this. microsoft_outlook/controllers/main.py:89-112
- C8. External services and credentials: Microsoft login endpoint (default common tenant, overridable by system parameter microsoft_outlook.endpoint), 5-second timeout; client secret stored as a system parameter; scopes are sign-in, email, offline access, user profile and IMAP-access or SMTP-send. microsoft_outlook/models/microsoft_outlook_mixin.py:19,54-60,183-194,281-286; microsoft_outlook/models/fetchmail_server.py:14; microsoft_outlook/models/ir_mail_server.py:16
- C9. Observed inconsistency for reference: outlook SMTP host is preset as smtp-mail.outlook.com for personal server creation but smtp.outlook.com in the server form default. microsoft_outlook/models/res_users.py:19; microsoft_outlook/models/ir_mail_server.py:60. Which is authoritative in practice: UNKNOWN — EVIDENCE INSUFFICIENT.
- C10. Undeclared dependency observed: the error-message helper is imported from google_gmail although the manifest depends only on mail. microsoft_outlook/models/microsoft_outlook_mixin.py:15; microsoft_outlook/__manifest__.py:9-11. Effect when google_gmail is absent: UNKNOWN — EVIDENCE INSUFFICIENT.
- C11. No security file or rules here; rights follow the underlying server models. Company scoping: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Outgoing servers: base (ir.mail_server) and mail (sending queue, cap logic). Incoming servers: mail (fetchmail). Personal server end action: users. microsoft_outlook/models/ir_mail_server.py:13; microsoft_outlook/models/fetchmail_server.py:11-12; microsoft_outlook/models/res_users.py:24-28; mail/models/mail_mail.py:591
- D2. Settings host: mail. Parallel design and shared helper: google_gmail.

## E. Configuration that changes outcomes
- E1. System parameters microsoft_outlook_client_id / microsoft_outlook_client_secret (direct flow vs intermediary). microsoft_outlook/models/microsoft_outlook_mixin.py:43-47,156-160
- E2. microsoft_outlook.endpoint, mail.server.outlook.iap.endpoint (default outlook.api.odoo.com, non-Community), mail.server.personal.limit.minutes_outlook. microsoft_outlook/models/microsoft_outlook_mixin.py:29,94-97,283-286; microsoft_outlook/models/ir_mail_server.py:90-91

## F. Extension path
- mail (fetchmail, settings, send queue), base (ir.mail_server), users; google_gmail (helper import, sibling).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: incoming-mail routing after fetch (mail module, not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: intermediary service return shape and Enterprise behaviour (external).
- UNKNOWN — EVIDENCE INSUFFICIENT: tenant-specific Microsoft app registration requirements (external).

