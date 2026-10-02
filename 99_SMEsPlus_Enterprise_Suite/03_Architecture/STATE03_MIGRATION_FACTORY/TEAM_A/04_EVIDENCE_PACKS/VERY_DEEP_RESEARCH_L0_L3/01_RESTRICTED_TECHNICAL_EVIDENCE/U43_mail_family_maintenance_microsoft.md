# U43 — mail family, maintenance, Microsoft (restricted technical evidence)

RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Unit: U43 (mail_family_maintenance_microsoft)
- Modules: mail_bot, mail_bot_hr, mail_group, mail_plugin, maintenance, microsoft_account, microsoft_calendar, microsoft_outlook
- Source revision: 19.0.post20260921
- Date: 2026-10-02
- Method: source read-only, config-only DB queries; no runtime executed. Earlier evidence aligned: U03, U17, U19 (C211-C227, C300-C302), U21 (C284-C353, C375-C389).

## CAP-U43-01 OdooBot onboarding and bot replies

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: mail_bot, mail_bot_hr
- Claims: VDR-U43-C001, VDR-U43-C002, VDR-U43-C003, VDR-U43-C004, VDR-U43-C005, VDR-U43-C006, VDR-U43-C007, VDR-U43-C008, VDR-U43-C009, VDR-U43-C010, VDR-U43-C011, VDR-U43-C012, VDR-U43-C013, VDR-U43-C014, VDR-U43-C015

### D1 Business purpose
Guide a new internal user through a scripted onboarding in chat and answer simple prompts.

### D2 Architecture and data
mail_bot onboarding state machine on res.users.odoobot_state; reply via channel message_post (sudo); mail_bot_hr only adjusts the user form. Objects: res.users, discuss.channel, mail.canned.response.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- idle -> onboarding_emoji [start the tour or bootstrap]
- onboarding_emoji -> onboarding_command [emoji in message]
- onboarding_command -> onboarding_ping [help command]
- onboarding_ping -> onboarding_attachement [ping]
- onboarding_attachement -> onboarding_canned [attachment]
- onboarding_canned -> idle [canned response used]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Bot logic skips messages authored by the bot itself and non-comment messages (read lines 25-26 together). (VDR-U43-C001) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Bot replies are posted as sudo on the channel, so reply posting does not depend on the user's own write rights (VDR-U43-C002) ; Bot replies are posted silent (no follower notification fan-out). (VDR-U43-C003) |
| 4 | Side effects / cross-module | The bot creates a canned response record (Thanks) for the user during onboarding; side effect on another model (VDR-U43-C008) ; _init_odoobot writes the initial state with sudo for internal users at webclient bootstrap (_is_internal check (VDR-U43-C013) |
| 5 | Configuration / optionality | An idle user can restart onboarding by typing the phrase; state returns to onboarding_emoji. (VDR-U43-C009) ; mail_bot_hr replaces the notification_alert widget in the HR-modified user form and re-adds the bot fields (li (VDR-U43-C014) |
| 6 | Validation / constraints | State onboarding_emoji advances to onboarding_command when the body contains an emoji (_body_contains_emoji). (VDR-U43-C004) ; After the command step, help text leads to onboarding_ping; ping step follows around line 81. (VDR-U43-C005) ; Attachment step (spelling onboarding_attachement is the source token) precedes the canned-response step. (VDR-U43-C006) ; Canned-response step deletes the demo canned response created at line 90 and moves the user to idle. (VDR-U43-C007) |
| 7 | Roles / permissions | odoobot_state is a read-only field for the UI; writes in server code use plain env.user assignment (non-sudo)  (VDR-U43-C011) |
| 8 | Scheduled / automated | mail_bot_hr is auto_install and depends on mail_bot and hr (line 9). (VDR-U43-C015) |
| 9 | Exception / failure | odoobot_failed flag is consulted in _is_help_requested to change the fallback wording. (VDR-U43-C010) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: mail_bot and mail_bot_hr installed; no config rows specific to the bot beyond views.

### Unknown / RT
RT: non-admin odoobot_state persistence; bot reply wording not read in full.

## CAP-U43-02 Mailing group lifecycle and moderation

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: mail_group
- Claims: VDR-U43-C016, VDR-U43-C017, VDR-U43-C018, VDR-U43-C019, VDR-U43-C020, VDR-U43-C021, VDR-U43-C022, VDR-U43-C023, VDR-U43-C024, VDR-U43-C025, VDR-U43-C026, VDR-U43-C027, VDR-U43-C028, VDR-U43-C029, VDR-U43-C030, VDR-U43-C031, VDR-U43-C032, VDR-U43-C033, VDR-U43-C034, VDR-U43-C035

### D1 Business purpose
Run list-style email groups with optional moderation of inbound posts.

### D2 Architecture and data
mail.group with alias mixin; mail.group.message moderation_status; mail.group.moderation rules; fan-out via mail.mail. Objects: mail.group, mail.group.message, mail.group.moderation, mail.mail.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- received -> pending_moderation [moderated group]
- received -> accepted [unmoderated or allow rule]
- pending_moderation -> accepted [moderator accepts]
- pending_moderation -> rejected [moderator rejects or ban rule]
- accepted -> delivered [fan-out batch]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | mail.group inherits mail.alias.mixin so each list has an incoming-mail alias. (VDR-U43-C016) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Constraints at lines 207-229: moderators need an email; notify message required when moderation notify is on;  (VDR-U43-C017) ; Alias error check rejects mail for closed groups and for senders who are not members when access is members-on (VDR-U43-C018) ; Unmoderated group notifies members directly through _notify_members. (VDR-U43-C021) ; A moderation rule with status allow accepts automatically and ban rejects (lines 352-357). (VDR-U43-C022) |
| 4 | Side effects / cross-module | message_new and message_update are no-ops; incoming mail is routed through message_post instead (lines 271-280 (VDR-U43-C019) ; When moderation_notify is set, a sudo mail.mail with auto_delete and state outgoing tells the sender the messa (VDR-U43-C023) ; Member fan-out is batched by the ICP mail.session.batch.size. (VDR-U43-C024) ; The author is skipped in the member fan-out (line 433). (VDR-U43-C025) ; Outgoing list mail carries List-Unsubscribe, one-click post header, Precedence list, auto-response suppress, L (VDR-U43-C026) ; Fan-out mail.mail records are created with sudo (line 486). (VDR-U43-C027) ; Message create makes a mail.message with sudo (line 97). (VDR-U43-C033) ; Reject creates a sudo mail.mail rejection email. (VDR-U43-C035) |
| 5 | Configuration / optionality | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 6 | Validation / constraints | Incoming message is stored with moderation_status pending_moderation when the group is moderated, else accepte (VDR-U43-C020) ; Guidelines can be sent only by admin or moderators; closed groups refused (line 382); banned emails filtered ( (VDR-U43-C029) ; Accept path calls _assert_moderable (line 120) before notifying members. (VDR-U43-C031) |
| 7 | Roles / permissions | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 8 | Scheduled / automated | Daily cron notifies moderators of pending messages; DB shows cron active, interval 1 day, priority 1000. (VDR-U43-C028) |
| 9 | Exception / failure | Mail to a closed group is bounced by routing check. (VDR-U43-C030) ; Constraint raises AccessError for invalid author/moderator combos (lines 79-87). (VDR-U43-C034) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 9 ACL rows and 10 rules match source; cron active (1 day, priority 1000); 3 mail templates; 0 groups.

### Unknown / RT
RT: mail send/receive; moderation allow/ban callers; JS and portal templates not read.

## CAP-U43-03 Mailing group membership, tokens and portal

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: mail_group
- Claims: VDR-U43-C036, VDR-U43-C037, VDR-U43-C038, VDR-U43-C039, VDR-U43-C040, VDR-U43-C041, VDR-U43-C042, VDR-U43-C043, VDR-U43-C044, VDR-U43-C045, VDR-U43-C046, VDR-U43-C047, VDR-U43-C048, VDR-U43-C049

### D1 Business purpose
Let people join, leave and manage subscriptions via email links and a portal.

### D2 Architecture and data
mail.group.member; HMAC tokens with three scopes; /group routes; one-click unsubscribe route. Objects: mail.group.member, controllers portal.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- visitor -> pending_confirmation [public subscribe]
- pending_confirmation -> member [valid confirm token]
- member -> left [unsubscribe or one-click]
- logged-in -> member [direct join]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | action_join and action_leave call _join_group/_leave_group as sudo (561/568). (VDR-U43-C036) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Action token is an HMAC with scope mail_group-email-subscription. (VDR-U43-C038) ; Per-email portal access token uses a separate HMAC scope; the group-level token uses another (lines 700-703). (VDR-U43-C039) ; A logged-in user subscribing joins immediately; public users get a confirmation email (line 273). (VDR-U43-C043) ; Group list route /groups is auth public. (VDR-U43-C047) |
| 4 | Side effects / cross-module | Confirmation emails for join and leave are sent immediately with force_send. (VDR-U43-C037) ; _find_members searches members with sudo. (VDR-U43-C040) ; Subscribe confirm uses no_create=True partner lookup. (VDR-U43-C046) |
| 5 | Configuration / optionality | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 6 | Validation / constraints | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 7 | Roles / permissions | 9 ACL rows: public/portal read-only on group and message; base.group_user full CRUD on group, member, message, (VDR-U43-C048) ; Moderator write rule domain uses moderator_ids; 10 rules in source, 10 in DB. (VDR-U43-C049) |
| 8 | Scheduled / automated | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 9 | Exception / failure | One-click unsubscribe compares token with consteq (constant time). (VDR-U43-C041) ; One-click unsubscribe POST route disables CSRF by design for mail clients. (VDR-U43-C042) ; Group access token compared with != (not constant-time) at line 326. (VDR-U43-C044) ; Confirm path uses == on tokens (line 385); confirms U19 C222 observation. (VDR-U43-C045) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: same ACL and rule rows as capability 02; no members (0 groups).

### Unknown / RT
RT: confirm-link behaviour end to end; portal templates not read.

## CAP-U43-04 Mail plugin authentication, enrichment and logging

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: mail_plugin
- Claims: VDR-U43-C050, VDR-U43-C051, VDR-U43-C052, VDR-U43-C053, VDR-U43-C054, VDR-U43-C055, VDR-U43-C056, VDR-U43-C057, VDR-U43-C058, VDR-U43-C059, VDR-U43-C060, VDR-U43-C061, VDR-U43-C062, VDR-U43-C063, VDR-U43-C064, VDR-U43-C065

### D1 Business purpose
Let an email add-in authenticate, find or create contacts, enrich companies and log emails.

### D2 Architecture and data
/mail_plugin/auth issues signed auth code; access_token route exchanges for API key; auth outlook routes; IAP enrichment. Objects: res.users.apikeys, res.partner, res.partner.iap, iap.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- unauthenticated -> code_issued [auth by user]
- code_issued -> key_issued [code valid under 3 minutes]
- key_issued -> expired [expiry days elapsed]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Auth start route requires a logged-in user and issues an auth code. (VDR-U43-C050) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Redirect with the auth code goes to a caller-supplied redirect target (non-local). (VDR-U43-C051) ; Auth code is data plus HMAC signature with scope mail_plugin (lines 114-127). (VDR-U43-C053) ; Auth code expires after 3 minutes. (VDR-U43-C054) ; API key lifetime from param, default 30 days, reset to 30 when not positive. (VDR-U43-C056) |
| 4 | Side effects / cross-module | Access token exchange creates a res.users.apikeys key with sudo and scope odoo.plugin.outlook. (VDR-U43-C057) ; Company enrichment calls the IAP enrich API (data leaves the system: domain name); runtime unverified. (VDR-U43-C059) ; Company logo URL is fetched with a 2-second timeout. (VDR-U43-C061) ; Email body is posted to the record chatter as Markup (HTML trusted from the add-in). (VDR-U43-C064) |
| 5 | Configuration / optionality | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 6 | Validation / constraints | Partner creation requires create access on res.partner else Forbidden. (VDR-U43-C062) ; log_mail_content only allowed for whitelisted models. (VDR-U43-C063) |
| 7 | Roles / permissions | auth=outlook routes validate the key through apikeys with scope odoo.plugin.outlook. (VDR-U43-C058) ; One ACL row; res.partner.iap limited to base.group_system. (VDR-U43-C065) |
| 8 | Scheduled / automated | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 9 | Exception / failure | Signature compared in constant time. (VDR-U43-C055) ; Insufficient IAP credit is mapped to an enrichment_info response; any other exception becomes type other. (VDR-U43-C060) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 1 ACL row for the IAP partner table; module installed; API-key rows not queried (credential data).

### Unknown / RT
RT: IAP credits and enrichment result; logo fetch; redirect-target validation not observed; res_partner.py and res_partner_iap.py not read.

## CAP-U43-05 Maintenance request workflow

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: maintenance
- Claims: VDR-U43-C066, VDR-U43-C067, VDR-U43-C068, VDR-U43-C069, VDR-U43-C070, VDR-U43-C071, VDR-U43-C072, VDR-U43-C073, VDR-U43-C074, VDR-U43-C075, VDR-U43-C076, VDR-U43-C077, VDR-U43-C078, VDR-U43-C079, VDR-U43-C080

### D1 Business purpose
Track corrective and preventive maintenance requests through stages with recurrence and activities.

### D2 Architecture and data
maintenance.request with stage, kanban_state, recurrence copy on done, activity mixin, cc thread. Objects: maintenance.request, maintenance.stage, mail.activity.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- new -> in_progress [stage change]
- in_progress -> repaired [done stage]
- in_progress -> scrap [done stage]
- done -> new_copy [recurrence repeat]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | maintenance.request inherits mail.thread.cc and the activity mixin. (VDR-U43-C066) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Moving to a done stage copies the request for recurrence (lines 335-347). (VDR-U43-C069) ; activity_update builds the scheduled maintenance activity for the technician. (VDR-U43-C077) |
| 4 | Side effects / cross-module | Done closes the maintenance activity with feedback and updates activity. (VDR-U43-C071) ; When a new activity is needed the old activity is unlinked and recreated. (VDR-U43-C072) ; Default stage, creation subtype and tracking subtype hooks at 188-194. (VDR-U43-C076) ; Seeds the maintenance activity type with wrench icon. (VDR-U43-C080) |
| 5 | Configuration / optionality | A default team is chosen at create. (VDR-U43-C075) ; 4 seeded stages; two are done (Repaired, Scrap); DB has 4 stages. (VDR-U43-C079) |
| 6 | Validation / constraints | On create, close_date set if the stage is a done stage. (VDR-U43-C067) ; Stage change resets kanban_state to normal. (VDR-U43-C068) ; Archive and reset actions set the archive flag on a request. (VDR-U43-C073) |
| 7 | Roles / permissions | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 8 | Scheduled / automated | Stage group_expand reads all stages with sudo. (VDR-U43-C078) |
| 9 | Exception / failure | Constraints at 268-271 and 288-291 validate dates and repeat settings. (VDR-U43-C074) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 4 stages; 0 requests.

### Unknown / RT
RT: recurrence TypeError when repeat_until empty; full views arch not read.

## CAP-U43-06 Equipment, categories, teams and alias intake

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: maintenance
- Claims: VDR-U43-C081, VDR-U43-C082, VDR-U43-C083, VDR-U43-C084, VDR-U43-C085, VDR-U43-C086, VDR-U43-C087, VDR-U43-C088, VDR-U43-C089, VDR-U43-C090, VDR-U43-C091

### D1 Business purpose
Register equipment, group it into categories, assign teams, compute reliability figures, accept requests by email.

### D2 Architecture and data
maintenance.equipment with MTBF/MTTR mixin; maintenance.team with alias mixin; category delete guard. Objects: maintenance.equipment, maintenance.equipment.category, maintenance.team.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- equipment_active -> archived [archive]
- email -> request_created [team alias]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Equipment inherits thread, activity and the MTBF mixin. (VDR-U43-C081) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | The owner is auto-subscribed as follower on create/write. (VDR-U43-C083) ; Team is cleared if it belongs to another company. (VDR-U43-C086) |
| 4 | Side effects / cross-module | Team alias creates maintenance.request with default team. (VDR-U43-C087) ; mail.thread.cc stores cc emails on incoming message_new (approximate line; source of cc storage). (VDR-U43-C089) |
| 5 | Configuration / optionality | Team inherits mail.alias.mixin and mail.thread. (VDR-U43-C088) ; Seeds team Internal Maintenance; DB has 1 team and 1 alias. (VDR-U43-C090) |
| 6 | Validation / constraints | Equipment serial number is unique. (VDR-U43-C082) ; MTBF, MTTR and estimated next failure computed in the mixin (lines 94-101). (VDR-U43-C084) ; Category deletion blocked when equipment or requests are linked. (VDR-U43-C085) |
| 7 | Roles / permissions | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 8 | Scheduled / automated | Team dashboard computes counts of open requests (429-442). (VDR-U43-C091) |
| 9 | Exception / failure | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 1 team, 1 alias (no name, contact everyone, default team 1); 0 equipment queried as business data not needed.

### Unknown / RT
RT: MTBF/MTTR numbers; alias mail intake.

## CAP-U43-07 Maintenance security and multi-company

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: maintenance
- Claims: VDR-U43-C092, VDR-U43-C093, VDR-U43-C094, VDR-U43-C095, VDR-U43-C096, VDR-U43-C097

### D1 Business purpose
Restrict who may see and change maintenance records.

### D2 Architecture and data
Group equipment manager; request/equipment rules limited to owner, follower, technician; multi-company rule. Objects: ir.model.access, ir.rule.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- NOT APPLICABLE — no workflow states
- static access rules

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Equipment manager group implies base.group_user; root and admin included. (VDR-U43-C092) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Request user rule limits to owner, follower or technician. (VDR-U43-C093) ; Equipment user rule: follower only. (VDR-U43-C094) ; Multi-company rule domain includes company_ids plus False. (VDR-U43-C095) |
| 4 | Side effects / cross-module | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 5 | Configuration / optionality | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 6 | Validation / constraints | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 7 | Roles / permissions | 10 ACL rows in source and DB; 8 rules in DB vs 8 in source. (VDR-U43-C096) |
| 8 | Scheduled / automated | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 9 | Exception / failure | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 10 ACL rows, 8 rules; source declares 8 rules.

### Unknown / RT
RT: rule evaluation per user not exercised.

## CAP-U43-08 Microsoft account OAuth and token lifecycle

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: microsoft_account
- Claims: VDR-U43-C098, VDR-U43-C099, VDR-U43-C100, VDR-U43-C101, VDR-U43-C102, VDR-U43-C103, VDR-U43-C104, VDR-U43-C105, VDR-U43-C106, VDR-U43-C107, VDR-U43-C108, VDR-U43-C109

### D1 Business purpose
Authorize against Microsoft identity and store tokens for dependent services.

### D2 Architecture and data
MicrosoftService with endpoints overridable by parameters; controller callback; tokens on res.users. Objects: res.users, ir.config_parameter.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- unlinked -> authorized [callback with code]
- authorized -> refreshed [refresh token]
- authorized -> unlinked [refresh failure by caller]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Requests to Microsoft use a 20-second timeout. (VDR-U43-C098) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Client secret is stored as a system parameter and read by a private method. (VDR-U43-C100) ; OAuth state is plain JSON (db name, service, return URL, database uuid) and is not signed. (VDR-U43-C104) ; Token write uses plain write (no sudo) with token fields restricted to system group; contrasts with U21 accoun (VDR-U43-C106) |
| 4 | Side effects / cross-module | Authorization and token endpoints can be overridden by system parameters. (VDR-U43-C099) ; Statuses 204 and 404 return an empty dict. (VDR-U43-C107) |
| 5 | Configuration / optionality | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 6 | Validation / constraints | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 7 | Roles / permissions | Token fields are readable by the system group only. (VDR-U43-C108) |
| 8 | Scheduled / automated | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 9 | Exception / failure | _do_request asserts the host is the token endpoint or the graph host. (VDR-U43-C101) ; Token fetch HTTP errors become a configuration warning. (VDR-U43-C103) ; Error cases redirect with error query parameter. (VDR-U43-C109) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: module installed; no client id or secret configured; 0 users with a refresh token.

### Unknown / RT
RT: whether a non-admin consent callback fails on the non-sudo token write; debug log content.

## CAP-U43-09 Outlook calendar synchronization

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: microsoft_calendar
- Claims: VDR-U43-C110, VDR-U43-C111, VDR-U43-C112, VDR-U43-C113, VDR-U43-C114, VDR-U43-C115, VDR-U43-C116, VDR-U43-C117, VDR-U43-C118, VDR-U43-C119, VDR-U43-C120, VDR-U43-C121, VDR-U43-C122, VDR-U43-C123, VDR-U43-C124, VDR-U43-C125, VDR-U43-C126, VDR-U43-C127, VDR-U43-C128, VDR-U43-C129, VDR-U43-C130, VDR-U43-C131, VDR-U43-C132, VDR-U43-C133, VDR-U43-C134, VDR-U43-C135, VDR-U43-C136, VDR-U43-C137, VDR-U43-C138, VDR-U43-C139

### D1 Business purpose
Two-way sync of calendar events with Microsoft Graph, using delta tokens and a periodic cron.

### D2 Architecture and data
microsoft.calendar.sync mixin; calendar.event, recurrence, attendee overrides; users sync status; wizard reset. Objects: calendar.event, calendar.recurrence, res.users, ir.cron.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- not_configured -> active [auth]
- active -> paused [parameter]
- active -> stopped [admin stop]
- active -> need_auth [refresh fail]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Sync to Microsoft runs after commit; failures are only logged as warnings (46-47). (VDR-U43-C110) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | Recurrence capped at 720 occurrences. (VDR-U43-C112) ; Graph timeout ICP microsoft_calendar.graph_timeout default 5s, minimum 1. (VDR-U43-C114) ; Patch result sets need_sync_m = not res. (VDR-U43-C115) ; Full sync window is range_days before and twice after. (VDR-U43-C118) ; Fetch asks for html body and page size 50. (VDR-U43-C121) ; On 400/401 token refresh: rollback, wipe tokens and sync token, commit, raise UserError. (VDR-U43-C122) ; Next sync token is stored before events are processed. (VDR-U43-C123) ; Full sync when no sync token. (VDR-U43-C125) ; First-sync date stops older events from triggering invitations. (VDR-U43-C126) ; Organizer must have synced calendar and be an attendee. (VDR-U43-C132) ; Attendee accept/decline sends answer with sendResponse True. (VDR-U43-C134) |
| 4 | Side effects / cross-module | Unlinking deletes the event in Microsoft first. (VDR-U43-C116) ; Delta sync uses calendarView/delta; data in: events; out: Graph token. (VDR-U43-C117) ; Unknown attendee emails create partners (no_create=False) during inbound sync. (VDR-U43-C127) ; Outbound event body is the customer description; attendee names and emails are sent to Microsoft (555-564). (VDR-U43-C128) ; Teams join URL maps into videocall location. (VDR-U43-C129) ; Synced events excluded from Odoo notification alarms. (VDR-U43-C133) ; sync_data route runs sync as sudo with dont_notify. (VDR-U43-C137) |
| 5 | Configuration / optionality | post_init_hook sets microsoft_guid parameter. (VDR-U43-C136) ; Neutralize script clears tokens and stops sync. (VDR-U43-C139) |
| 6 | Validation / constraints | Conflict policy: the last updated side wins by timestamp compare (lines 332-347). (VDR-U43-C113) ; Recurrence creation in Odoo forbidden when sync is active. (VDR-U43-C130) ; Attendees must have email else ValidationError lists events. (VDR-U43-C131) ; Reset wizard clears tokens, sync token and last sync date. (VDR-U43-C138) |
| 7 | Roles / permissions | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 8 | Scheduled / automated | Cron syncs each user with its own commit/rollback and logs exceptions. (VDR-U43-C124) ; Cron every 12 hours; DB confirms active, user 1. (VDR-U43-C135) |
| 9 | Exception / failure | Post-commit sync failure is logged and swallowed; the record keeps need_sync_m. (VDR-U43-C111) ; fullSyncRequired and SyncStateNotFound trigger a full resync. (VDR-U43-C119) ; Delete tolerates 404. (VDR-U43-C120) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: cron active, 12 hours, priority 5, user 1; 1 ACL row; guid and redirect URI parameters present; no client id or secret; 0 users with refresh token.

### Unknown / RT
RT: Graph responses, rate limits, throttling; token rotation and rollback; calendar internals (rrule parsing) not read.

## CAP-U43-10 Outlook mail server OAuth (SMTP and IMAP)

- Function-ID: FUNCTION MAPPING REQUIRED
- Modules: microsoft_outlook
- Claims: VDR-U43-C140, VDR-U43-C141, VDR-U43-C142, VDR-U43-C143, VDR-U43-C144, VDR-U43-C145, VDR-U43-C146, VDR-U43-C147, VDR-U43-C148, VDR-U43-C149, VDR-U43-C150, VDR-U43-C151, VDR-U43-C152, VDR-U43-C153, VDR-U43-C154, VDR-U43-C155, VDR-U43-C156

### D1 Business purpose
Send and fetch mail through Outlook using token-based sign-in.

### D2 Architecture and data
microsoft.outlook.mixin on ir.mail_server and fetchmail.server; direct or IAP token flow. Objects: ir.mail_server, fetchmail.server, iap.

### D3 Source logic and state diagram
Control flow follows the claims below; state diagram:

- unlinked -> linked [callback]
- linked -> refreshed [expiry near]
- linked -> failed [error_description]

### Ten-dimension table

| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Only administrator may link an Outlook account. (VDR-U43-C140) ; Manifest depends mail, auto_install true. (VDR-U43-C156) |
| 2 | Reversal / negative path | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 3 | Multi-company / scope | With client id and secret, token POST goes direct to Microsoft; otherwise IAP. (VDR-U43-C141) ; OAuth string refreshes token when expired or within 10 seconds and stores new tokens on the record. (VDR-U43-C144) ; CSRF token is deterministic HMAC of model and id. (VDR-U43-C145) ; Tokens and expiry are stored sudo on the record. (VDR-U43-C149) ; Personal server limit param default 10 minutes. (VDR-U43-C155) |
| 4 | Side effects / cross-module | IAP access-token fetch sends refresh_token and db_uuid as GET query params; refresh token leaves system. (VDR-U43-C142) ; Default IAP endpoint overridable by system parameter. (VDR-U43-C143) ; IAP callback receives tokens in the query string. (VDR-U43-C148) |
| 5 | Configuration / optionality | Onchange defaults smtp.outlook.com STARTTLS 587. (VDR-U43-C152) |
| 6 | Validation / constraints | SMTP outlook server: empty password, STARTTLS and user required. (VDR-U43-C151) ; IMAP login uses XOAUTH2; SSL required (26-30). (VDR-U43-C154) |
| 7 | Roles / permissions | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 8 | Scheduled / automated | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |
| 9 | Exception / failure | State CSRF compared with consteq. (VDR-U43-C146) ; Email taken from JWT without signature verification; check applies only to personal servers or non-admins. (VDR-U43-C147) ; Imports get_iap_error_message from google_gmail without declaring it in depends. (VDR-U43-C150) |
| 10 | Accounting, audit, security | NOT APPLICABLE or UNKNOWN — no claim read for this dimension in this unit |

### DB reconciliation
DB: 0 mail servers and 0 fetchmail servers (config only).

### Unknown / RT
RT: IAP behaviour and failures; mail send/fetch; google_gmail.tools not read.

## MODULE STATUS TABLE

| Module | Matrix status before | Claims | Capabilities | Assessment |
|---|---|---|---|---|
| mail_bot | PARTIAL | 13 | CAP-U43-01 | PARTIAL — reply text, JS bot assets and non-admin state write not verified |
| mail_bot_hr | PARTIAL | 2 | CAP-U43-01 | L3-READY (view-only bridge; no Python) |
| mail_group | PARTIAL | 34 | CAP-U43-02, CAP-U43-03 | PARTIAL — portal templates, moderation callers in views and runtime mail flow not read |
| mail_plugin | PARTIAL | 16 | CAP-U43-04 | PARTIAL — res_partner.py, res_partner_iap.py and redirect validation not read |
| maintenance | PARTIAL | 31 | CAP-U43-05, CAP-U43-06, CAP-U43-07 | PARTIAL — full views arch, hr_maintenance and runtime not read |
| microsoft_account | PARTIAL | 12 | CAP-U43-08 | L3-READY (small module; runtime RT items remain) |
| microsoft_calendar | PARTIAL | 30 | CAP-U43-09 | PARTIAL — calendar internals and Graph runtime not read; some line ranges read only at summary level |
| microsoft_outlook | PARTIAL | 17 | CAP-U43-10 | PARTIAL — google_gmail.tools and IAP internals not read |

Note: claim counts above count claims by pointer module; mail/mail_thread_cc pointer counts under mail.

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U43-C001 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:25 | author | FACT | module installed | — | Bot logic skips messages authored by the bot itself and non-comment messages (read lines 25-26 together). | N-U43-001 |
| VDR-U43-C002 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:31 | message_post( | FACT | always | — | Bot replies are posted as sudo on the channel, so reply posting does not depend on the user's own write rights. | N-U43-003 |
| VDR-U43-C003 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:35 | silent=True | FACT | always | — | Bot replies are posted silent (no follower notification fan-out). | N-U43-003 |
| VDR-U43-C004 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:63 | onboarding_emoji | FACT | onboarding state | — | State onboarding_emoji advances to onboarding_command when the body contains an emoji (_body_contains_emoji). | N-U43-006 |
| VDR-U43-C005 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:72 | onboarding_ping | FACT | onboarding state | — | After the command step, help text leads to onboarding_ping; ping step follows around line 81. | N-U43-006 |
| VDR-U43-C006 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:89 | onboarding_attachement | FACT | onboarding state | — | Attachment step (spelling onboarding_attachement is the source token) precedes the canned-response step. | N-U43-006 |
| VDR-U43-C007 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:105 | unlink | FACT | onboarding state | — | Canned-response step deletes the demo canned response created at line 90 and moves the user to idle. | N-U43-006 |
| VDR-U43-C008 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:90 | mail.canned.response | FACT | onboarding state | — | The bot creates a canned response record (Thanks) for the user during onboarding; side effect on another model. | N-U43-004 |
| VDR-U43-C009 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:127 | start the tour | FACT | idle state | — | An idle user can restart onboarding by typing the phrase; state returns to onboarding_emoji. | N-U43-005 |
| VDR-U43-C010 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:333 | odoobot_failed | FACT | help requested | — | odoobot_failed flag is consulted in _is_help_requested to change the fallback wording. | N-U43-009 |
| VDR-U43-C011 | FUNCTION MAPPING REQUIRED | mail_bot/models/res_users.py:21 | readonly=True | FACT | always | — | odoobot_state is a read-only field for the UI; writes in server code use plain env.user assignment (non-sudo) in bot logic. | N-U43-007 |
| VDR-U43-C012 | FUNCTION MAPPING REQUIRED | mail_bot/models/mail_bot.py:101 | odoobot_state | INFERENCE | non-admin user | RT | Bot state writes use env.user without sudo (see lines 63-105); whether a non-admin internal user can persist the state depends on SELF_WRITEABLE handling in res_users; not proven here. | N-U43-011 |
| VDR-U43-C013 | FUNCTION MAPPING REQUIRED | mail_bot/models/res_users.py:49 | sudo().odoobot_state | FACT | webclient bootstrap | — | _init_odoobot writes the initial state with sudo for internal users at webclient bootstrap (_is_internal check at line 30). | N-U43-004 |
| VDR-U43-C014 | FUNCTION MAPPING REQUIRED | mail_bot_hr/views/res_users_views.xml:10 | notification_alert | FACT | hr installed | — | mail_bot_hr replaces the notification_alert widget in the HR-modified user form and re-adds the bot fields (line 21); no Python in this module. | N-U43-005 |
| VDR-U43-C015 | FUNCTION MAPPING REQUIRED | mail_bot_hr/__manifest__.py:11 | auto_install | FACT | mail_bot and hr installed | — | mail_bot_hr is auto_install and depends on mail_bot and hr (line 9). | N-U43-008 |
| VDR-U43-C016 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:37 | mail.alias.mixin | FACT | always | — | mail.group inherits mail.alias.mixin so each list has an incoming-mail alias. | N-U43-013 |
| VDR-U43-C017 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:211 | constrains | FACT | always | — | Constraints at lines 207-229: moderators need an email; notify message required when moderation notify is on; moderated group needs moderators; authorized-group requirement. | N-U43-015 |
| VDR-U43-C018 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:251 | _alias_get_error | FACT | incoming mail | — | Alias error check rejects mail for closed groups and for senders who are not members when access is members-only (lines 251-268). | N-U43-015 |
| VDR-U43-C019 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:271 | message_new | FACT | always | — | message_new and message_update are no-ops; incoming mail is routed through message_post instead (lines 271-280). | N-U43-016 |
| VDR-U43-C020 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:332 | pending_moderation | FACT | moderated group | — | Incoming message is stored with moderation_status pending_moderation when the group is moderated, else accepted. | N-U43-018 |
| VDR-U43-C021 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:349 | if not self.moderation | FACT | unmoderated group | — | Unmoderated group notifies members directly through _notify_members. | N-U43-015 |
| VDR-U43-C022 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:352 | moderation_rule | FACT | moderated group | — | A moderation rule with status allow accepts automatically and ban rejects (lines 352-357). | N-U43-015 |
| VDR-U43-C023 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:358 | auto_delete | FACT | moderation notify on | — | When moderation_notify is set, a sudo mail.mail with auto_delete and state outgoing tells the sender the message is held. | N-U43-016 |
| VDR-U43-C024 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:429 | mail.session.batch.size | FACT | always | — | Member fan-out is batched by the ICP mail.session.batch.size. | N-U43-016 |
| VDR-U43-C025 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:433 | author | FACT | always | — | The author is skipped in the member fan-out (line 433). | N-U43-016 |
| VDR-U43-C026 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:445 | List-Unsubscribe | FACT | always | — | Outgoing list mail carries List-Unsubscribe, one-click post header, Precedence list, auto-response suppress, List-Id and List-Post headers. | N-U43-016 |
| VDR-U43-C027 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:486 | sudo | FACT | always | — | Fan-out mail.mail records are created with sudo (line 486). | N-U43-016 |
| VDR-U43-C028 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:489 | _cron_notify_moderators | FACT | cron active | — | Daily cron notifies moderators of pending messages; DB shows cron active, interval 1 day, priority 1000. | N-U43-020 |
| VDR-U43-C029 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:371 | action_send_guidelines | FACT | always | — | Guidelines can be sent only by admin or moderators; closed groups refused (line 382); banned emails filtered (388). | N-U43-018 |
| VDR-U43-C030 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:537 | _routing_check_route | FACT | closed group | — | Mail to a closed group is bounced by routing check. | N-U43-021 |
| VDR-U43-C031 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group_message.py:115 | action_moderate_accept | FACT | always | — | Accept path calls _assert_moderable (line 120) before notifying members. | N-U43-018 |
| VDR-U43-C032 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group_message.py:143 | action_moderate_allow | INFERENCE | always | RT | action_moderate_allow and action_moderate_ban (lines 143-150) do not call _assert_moderable while accept and reject do; effect depends on the callers in views. | N-U43-023 |
| VDR-U43-C033 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group_message.py:97 | create | FACT | always | — | Message create makes a mail.message with sudo (line 97). | N-U43-016 |
| VDR-U43-C034 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group_message.py:79 | AccessError | FACT | always | — | Constraint raises AccessError for invalid author/moderator combos (lines 79-87). | N-U43-021 |
| VDR-U43-C035 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group_message.py:240 | mail.mail | FACT | reject | — | Reject creates a sudo mail.mail rejection email. | N-U43-016 |
| VDR-U43-C036 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:556 | action_join | FACT | always | — | action_join and action_leave call _join_group/_leave_group as sudo (561/568). | N-U43-025 |
| VDR-U43-C037 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:637 | force_send=True | FACT | public subscribe | — | Confirmation emails for join and leave are sent immediately with force_send. | N-U43-028 |
| VDR-U43-C038 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:690 | mail_group-email-subscription | FACT | always | — | Action token is an HMAC with scope mail_group-email-subscription. | N-U43-027 |
| VDR-U43-C039 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:698 | mail_group-access-token-portal-email | FACT | always | — | Per-email portal access token uses a separate HMAC scope; the group-level token uses another (lines 700-703). | N-U43-027 |
| VDR-U43-C040 | FUNCTION MAPPING REQUIRED | mail_group/models/mail_group.py:751 | sudo | FACT | always | — | _find_members searches members with sudo. | N-U43-028 |
| VDR-U43-C041 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:235 | consteq | FACT | one-click | — | One-click unsubscribe compares token with consteq (constant time). | N-U43-033 |
| VDR-U43-C042 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:218 | csrf=False | FACT | one-click | — | One-click unsubscribe POST route disables CSRF by design for mail clients. | N-U43-033 |
| VDR-U43-C043 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:267 | _join_group | FACT | logged-in | — | A logged-in user subscribing joins immediately; public users get a confirmation email (line 273). | N-U43-027 |
| VDR-U43-C044 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:326 | _generate_group_access_token | FACT | always | — | Group access token compared with != (not constant-time) at line 326. | N-U43-033 |
| VDR-U43-C045 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:385 | excepted_token | INFERENCE | confirm | — | Confirm path uses == on tokens (line 385); confirms U19 C222 observation. | N-U43-033 |
| VDR-U43-C046 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:351 | no_create | FACT | confirm subscribe | — | Subscribe confirm uses no_create=True partner lookup. | N-U43-028 |
| VDR-U43-C047 | FUNCTION MAPPING REQUIRED | mail_group/controllers/portal.py:63 | auth | FACT | always | — | Group list route /groups is auth public. | N-U43-027 |
| VDR-U43-C048 | FUNCTION MAPPING REQUIRED | mail_group/security/ir.model.access.csv:2 | mail_group | FACT | always | — | 9 ACL rows: public/portal read-only on group and message; base.group_user full CRUD on group, member, message, moderation, reject; DB matches 9 rows. | N-U43-031 |
| VDR-U43-C049 | FUNCTION MAPPING REQUIRED | mail_group/security/mail_group_security.xml:26 | moderator_ids | FACT | always | — | Moderator write rule domain uses moderator_ids; 10 rules in source, 10 in DB. | N-U43-031 |
| VDR-U43-C050 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:21 | /mail_plugin/auth | FACT | always | — | Auth start route requires a logged-in user and issues an auth code. | N-U43-037 |
| VDR-U43-C051 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:56 | local=False | FACT | always | — | Redirect with the auth code goes to a caller-supplied redirect target (non-local). | N-U43-039 |
| VDR-U43-C052 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:56 | redirect | INFERENCE | always | RT | Redirect target validation not seen in the lines read; open-redirect risk depends on a check not observed. | N-U43-047 |
| VDR-U43-C053 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:125 | mail_plugin | FACT | always | — | Auth code is data plus HMAC signature with scope mail_plugin (lines 114-127). | N-U43-039 |
| VDR-U43-C054 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:106 | minutes=3 | FACT | always | — | Auth code expires after 3 minutes. | N-U43-039 |
| VDR-U43-C055 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:100 | compare_digest | FACT | always | — | Signature compared in constant time. | N-U43-045 |
| VDR-U43-C056 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:84 | access_token_expiration_days | FACT | always | — | API key lifetime from param, default 30 days, reset to 30 when not positive. | N-U43-039 |
| VDR-U43-C057 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/authenticate.py:89 | _generate | FACT | always | — | Access token exchange creates a res.users.apikeys key with sudo and scope odoo.plugin.outlook. | N-U43-040 |
| VDR-U43-C058 | FUNCTION MAPPING REQUIRED | mail_plugin/models/ir_http.py:22 | _check_credentials | FACT | auth outlook | — | auth=outlook routes validate the key through apikeys with scope odoo.plugin.outlook. | N-U43-043 |
| VDR-U43-C059 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:287 | _request_enrich | FACT | enrichment | RT | Company enrichment calls the IAP enrich API (data leaves the system: domain name); runtime unverified. | N-U43-040 |
| VDR-U43-C060 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:288 | InsufficientCreditError | FACT | enrichment | RT | Insufficient IAP credit is mapped to an enrichment_info response; any other exception becomes type other. | N-U43-045 |
| VDR-U43-C061 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:100 | timeout=2 | FACT | logo fetch | RT | Company logo URL is fetched with a 2-second timeout. | N-U43-040 |
| VDR-U43-C062 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:230 | Forbidden | FACT | partner create | — | Partner creation requires create access on res.partner else Forbidden. | N-U43-042 |
| VDR-U43-C063 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:260 | Forbidden | FACT | log mail | — | log_mail_content only allowed for whitelisted models. | N-U43-042 |
| VDR-U43-C064 | FUNCTION MAPPING REQUIRED | mail_plugin/controllers/mail_plugin.py:269 | Markup(message) | FACT | log mail | — | Email body is posted to the record chatter as Markup (HTML trusted from the add-in). | N-U43-040 |
| VDR-U43-C065 | FUNCTION MAPPING REQUIRED | mail_plugin/security/ir.model.access.csv:2 | res_partner_iap | FACT | always | — | One ACL row; res.partner.iap limited to base.group_system. | N-U43-043 |
| VDR-U43-C066 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:181 | mail.thread.cc | FACT | always | — | maintenance.request inherits mail.thread.cc and the activity mixin. | N-U43-049 |
| VDR-U43-C067 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:322 | close_date | FACT | create | — | On create, close_date set if the stage is a done stage. | N-U43-054 |
| VDR-U43-C068 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:332 | kanban_state | FACT | write | — | Stage change resets kanban_state to normal. | N-U43-054 |
| VDR-U43-C069 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:340 | repeat | FACT | write to done stage | — | Moving to a done stage copies the request for recurrence (lines 335-347). | N-U43-051 |
| VDR-U43-C070 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:342 | repeat_until | INFERENCE | repeat_type until without date | RT | Line 342 compares schedule_date.date() with repeat_until; if repeat_until empty a TypeError is plausible; not run. | N-U43-059 |
| VDR-U43-C071 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:352 | activity_feedback | FACT | write to done stage | — | Done closes the maintenance activity with feedback and updates activity. | N-U43-052 |
| VDR-U43-C072 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:358 | activity_unlink | FACT | write | — | When a new activity is needed the old activity is unlinked and recreated. | N-U43-052 |
| VDR-U43-C073 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:258 | archive_equipment_request | FACT | always | — | Archive and reset actions set the archive flag on a request. | N-U43-054 |
| VDR-U43-C074 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:267 | constrains | FACT | always | — | Constraints at 268-271 and 288-291 validate dates and repeat settings. | N-U43-057 |
| VDR-U43-C075 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:200 | team | FACT | always | — | A default team is chosen at create. | N-U43-053 |
| VDR-U43-C076 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:188 | _default_stage | FACT | always | — | Default stage, creation subtype and tracking subtype hooks at 188-194. | N-U43-052 |
| VDR-U43-C077 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:373 | activity_update | FACT | always | — | activity_update builds the scheduled maintenance activity for the technician. | N-U43-051 |
| VDR-U43-C078 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:400 | sudo | FACT | kanban | — | Stage group_expand reads all stages with sudo. | N-U43-056 |
| VDR-U43-C079 | FUNCTION MAPPING REQUIRED | maintenance/data/maintenance_data.xml:5 | stage | FACT | noupdate | — | 4 seeded stages; two are done (Repaired, Scrap); DB has 4 stages. | N-U43-053 |
| VDR-U43-C080 | FUNCTION MAPPING REQUIRED | maintenance/data/mail_activity_type_data.xml:5 | mail_act_maintenance_request | FACT | always | — | Seeds the maintenance activity type with wrench icon. | N-U43-052 |
| VDR-U43-C081 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:110 | mail.thread | FACT | always | — | Equipment inherits thread, activity and the MTBF mixin. | N-U43-061 |
| VDR-U43-C082 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:153 | serial_no | FACT | always | — | Equipment serial number is unique. | N-U43-066 |
| VDR-U43-C083 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:158 | owner | FACT | create write | — | The owner is auto-subscribed as follower on create/write. | N-U43-063 |
| VDR-U43-C084 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:100 | mtbf | FACT | always | — | MTBF, MTTR and estimated next failure computed in the mixin (lines 94-101). | N-U43-066 |
| VDR-U43-C085 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:66 | UserError | FACT | category delete | — | Category deletion blocked when equipment or requests are linked. | N-U43-066 |
| VDR-U43-C086 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:88 | company | FACT | always | — | Team is cleared if it belongs to another company. | N-U43-063 |
| VDR-U43-C087 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:449 | _alias_get_creation_values | FACT | always | — | Team alias creates maintenance.request with default team. | N-U43-064 |
| VDR-U43-C088 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:404 | mail.alias.mixin | FACT | always | — | Team inherits mail.alias.mixin and mail.thread. | N-U43-065 |
| VDR-U43-C089 | FUNCTION MAPPING REQUIRED | mail/models/mail_thread_cc.py:25 | cc | OBSERVATION | incoming mail | — | mail.thread.cc stores cc emails on incoming message_new (approximate line; source of cc storage). | N-U43-064 |
| VDR-U43-C090 | FUNCTION MAPPING REQUIRED | maintenance/data/mail_message_subtype_data.xml:41 | equipment_team_maintenance | FACT | noupdate | — | Seeds team Internal Maintenance; DB has 1 team and 1 alias. | N-U43-065 |
| VDR-U43-C091 | FUNCTION MAPPING REQUIRED | maintenance/models/maintenance.py:420 | dashboard | FACT | always | — | Team dashboard computes counts of open requests (429-442). | N-U43-068 |
| VDR-U43-C092 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:9 | group_equipment_manager | FACT | always | — | Equipment manager group implies base.group_user; root and admin included. | N-U43-073 |
| VDR-U43-C093 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:21 | owner | FACT | always | — | Request user rule limits to owner, follower or technician. | N-U43-075 |
| VDR-U43-C094 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:31 | message_partner_ids | FACT | always | — | Equipment user rule: follower only. | N-U43-075 |
| VDR-U43-C095 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:67 | company_ids | FACT | multi-company | — | Multi-company rule domain includes company_ids plus False. | N-U43-075 |
| VDR-U43-C096 | FUNCTION MAPPING REQUIRED | maintenance/security/ir.model.access.csv:2 | maintenance | FACT | always | — | 10 ACL rows in source and DB; 8 rules in DB vs 8 in source. | N-U43-079 |
| VDR-U43-C097 | FUNCTION MAPPING REQUIRED | maintenance/security/maintenance.xml:45 | (1, '=', 1) | FACT | admin | — | Manager rules use an always-true domain. | N-U43-083 |
| VDR-U43-C098 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:15 | TIMEOUT = 20 | FACT | always | — | Requests to Microsoft use a 20-second timeout. | N-U43-085 |
| VDR-U43-C099 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:52 | microsoft_account.auth_endpoint | FACT | always | — | Authorization and token endpoints can be overridden by system parameters. | N-U43-088 |
| VDR-U43-C100 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:24 | client_secret | FACT | always | — | Client secret is stored as a system parameter and read by a private method. | N-U43-087 |
| VDR-U43-C101 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:160 | assert | FACT | always | — | _do_request asserts the host is the token endpoint or the graph host. | N-U43-093 |
| VDR-U43-C102 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:164 | _logger.debug | FACT | debug logging | RT | Debug logging records request headers and params, which can include bearer token and client secret in the token POST. | N-U43-095 |
| VDR-U43-C103 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:142 | HTTPError | FACT | token fetch | — | Token fetch HTTP errors become a configuration warning. | N-U43-093 |
| VDR-U43-C104 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:100 | state | FACT | authorize | — | OAuth state is plain JSON (db name, service, return URL, database uuid) and is not signed. | N-U43-087 |
| VDR-U43-C105 | FUNCTION MAPPING REQUIRED | microsoft_account/controllers/main.py:18 | state | INFERENCE | callback | — | Redirect after authentication goes to state f, which is unsigned; open-redirect inference. | N-U43-095 |
| VDR-U43-C106 | FUNCTION MAPPING REQUIRED | microsoft_account/models/res_users.py:17 | _set_microsoft_auth_tokens | FACT | always | CONTRA | Token write uses plain write (no sudo) with token fields restricted to system group; contrasts with U21 account modules that use sudo (U21 evidence). | N-U43-087 |
| VDR-U43-C107 | FUNCTION MAPPING REQUIRED | microsoft_account/models/microsoft_service.py:21 | RESOURCE_NOT_FOUND_STATUSES | FACT | always | — | Statuses 204 and 404 return an empty dict. | N-U43-088 |
| VDR-U43-C108 | FUNCTION MAPPING REQUIRED | microsoft_account/models/res_users.py:13 | base.group_system | FACT | always | — | Token fields are readable by the system group only. | N-U43-091 |
| VDR-U43-C109 | FUNCTION MAPPING REQUIRED | microsoft_account/controllers/main.py:31 | error | FACT | callback | — | Error cases redirect with error query parameter. | N-U43-093 |
| VDR-U43-C110 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:27 | after_commit | FACT | always | — | Sync to Microsoft runs after commit; failures are only logged as warnings (46-47). | N-U43-097 |
| VDR-U43-C111 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:46 | Could not sync record now | FACT | always | — | Post-commit sync failure is logged and swallowed; the record keeps need_sync_m. | N-U43-105 |
| VDR-U43-C112 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:21 | MAX_RECURRENT_EVENT | FACT | always | — | Recurrence capped at 720 occurrences. | N-U43-099 |
| VDR-U43-C113 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:340 | odoo_event_updated_time | FACT | sync | — | Conflict policy: the last updated side wins by timestamp compare (lines 332-347). | N-U43-102 |
| VDR-U43-C114 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:473 | graph_timeout | FACT | always | — | Graph timeout ICP microsoft_calendar.graph_timeout default 5s, minimum 1. | N-U43-099 |
| VDR-U43-C115 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:407 | need_sync_m | FACT | patch | — | Patch result sets need_sync_m = not res. | N-U43-099 |
| VDR-U43-C116 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/microsoft_sync.py:115 | unlink | FACT | always | — | Unlinking deletes the event in Microsoft first. | N-U43-100 |
| VDR-U43-C117 | FUNCTION MAPPING REQUIRED | microsoft_calendar/utils/microsoft_calendar.py:106 | /v1.0/me/calendarView/delta | FACT | delta sync | RT | Delta sync uses calendarView/delta; data in: events; out: Graph token. | N-U43-100 |
| VDR-U43-C118 | FUNCTION MAPPING REQUIRED | microsoft_calendar/utils/microsoft_calendar.py:68 | range_days | FACT | full sync | — | Full sync window is range_days before and twice after. | N-U43-099 |
| VDR-U43-C119 | FUNCTION MAPPING REQUIRED | microsoft_calendar/utils/microsoft_calendar.py:98 | fullSyncRequired | FACT | delta | — | fullSyncRequired and SyncStateNotFound trigger a full resync. | N-U43-105 |
| VDR-U43-C120 | FUNCTION MAPPING REQUIRED | microsoft_calendar/utils/microsoft_calendar.py:181 | status_code | FACT | delete | — | Delete tolerates 404. | N-U43-105 |
| VDR-U43-C121 | FUNCTION MAPPING REQUIRED | microsoft_calendar/utils/microsoft_calendar.py:63 | outlook.body-content-type | FACT | fetch | — | Fetch asks for html body and page size 50. | N-U43-099 |
| VDR-U43-C122 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/res_users.py:52 | rollback | FACT | refresh failure | — | On 400/401 token refresh: rollback, wipe tokens and sync token, commit, raise UserError. | N-U43-099 |
| VDR-U43-C123 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/res_users.py:99 | next_sync_token | FACT | sync | — | Next sync token is stored before events are processed. | N-U43-099 |
| VDR-U43-C124 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/res_users.py:123 | commit | FACT | cron | — | Cron syncs each user with its own commit/rollback and logs exceptions. | N-U43-104 |
| VDR-U43-C125 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/res_users.py:92 | full_sync | FACT | sync | — | Full sync when no sync token. | N-U43-099 |
| VDR-U43-C126 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/res_users.py:186 | first_synchronization_date | FACT | always | — | First-sync date stops older events from triggering invitations. | N-U43-099 |
| VDR-U43-C127 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:416 | _partner_find_from_emails_single | FACT | inbound sync | — | Unknown attendee emails create partners (no_create=False) during inbound sync. | N-U43-100 |
| VDR-U43-C128 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:523 | _get_customer_description | FACT | outbound sync | — | Outbound event body is the customer description; attendee names and emails are sent to Microsoft (555-564). | N-U43-100 |
| VDR-U43-C129 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:356 | joinUrl | FACT | inbound sync | — | Teams join URL maps into videocall location. | N-U43-100 |
| VDR-U43-C130 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:165 | recurrent events must be created directly | FACT | sync active | — | Recurrence creation in Odoo forbidden when sync is active. | N-U43-102 |
| VDR-U43-C131 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:656 | ValidationError | FACT | always | — | Attendees must have email else ValidationError lists events. | N-U43-102 |
| VDR-U43-C132 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar.py:99 | organizer | FACT | always | — | Organizer must have synced calendar and be an attendee. | N-U43-099 |
| VDR-U43-C133 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar_alarm_manager.py:14 | microsoft_id IS NULL | FACT | always | — | Synced events excluded from Odoo notification alarms. | N-U43-100 |
| VDR-U43-C134 | FUNCTION MAPPING REQUIRED | microsoft_calendar/models/calendar_attendee.py:30 | sendResponse | FACT | accept decline | — | Attendee accept/decline sends answer with sendResponse True. | N-U43-099 |
| VDR-U43-C135 | FUNCTION MAPPING REQUIRED | microsoft_calendar/data/microsoft_calendar_data.xml:12 | interval_number | FACT | always | — | Cron every 12 hours; DB confirms active, user 1. | N-U43-104 |
| VDR-U43-C136 | FUNCTION MAPPING REQUIRED | microsoft_calendar/__init__.py:11 | uuid | FACT | install | — | post_init_hook sets microsoft_guid parameter. | N-U43-101 |
| VDR-U43-C137 | FUNCTION MAPPING REQUIRED | microsoft_calendar/controllers/main.py:44 | sudo() | FACT | sync_data | — | sync_data route runs sync as sudo with dont_notify. | N-U43-100 |
| VDR-U43-C138 | FUNCTION MAPPING REQUIRED | microsoft_calendar/wizard/reset_account.py:51 | _set_microsoft_auth_tokens | FACT | reset | — | Reset wizard clears tokens, sync token and last sync date. | N-U43-102 |
| VDR-U43-C139 | FUNCTION MAPPING REQUIRED | microsoft_calendar/data/neutralize.sql:1 | UPDATE | FACT | neutralize | — | Neutralize script clears tokens and stops sync. | N-U43-101 |
| VDR-U43-C140 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:78 | admin | FACT | link | — | Only administrator may link an Outlook account. | N-U43-109 |
| VDR-U43-C141 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:170 | _fetch_outlook_token | FACT | direct flow | RT | With client id and secret, token POST goes direct to Microsoft; otherwise IAP. | N-U43-111 |
| VDR-U43-C142 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:220 | refresh_token | FACT | IAP flow | RT | IAP access-token fetch sends refresh_token and db_uuid as GET query params; refresh token leaves system. | N-U43-112 |
| VDR-U43-C143 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:29 | outlook.api.odoo.com | FACT | IAP flow | — | Default IAP endpoint overridable by system parameter. | N-U43-112 |
| VDR-U43-C144 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:252 | refresh | FACT | send mail | — | OAuth string refreshes token when expired or within 10 seconds and stores new tokens on the record. | N-U43-111 |
| VDR-U43-C145 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:268 | _get_outlook_csrf_token | FACT | always | — | CSRF token is deterministic HMAC of model and id. | N-U43-111 |
| VDR-U43-C146 | FUNCTION MAPPING REQUIRED | microsoft_outlook/controllers/main.py:82 | consteq | FACT | callback | — | State CSRF compared with consteq. | N-U43-117 |
| VDR-U43-C147 | FUNCTION MAPPING REQUIRED | microsoft_outlook/controllers/main.py:99 | email | FACT | callback | — | Email taken from JWT without signature verification; check applies only to personal servers or non-admins. | N-U43-117 |
| VDR-U43-C148 | FUNCTION MAPPING REQUIRED | microsoft_outlook/controllers/main.py:55 | iap_confirm | FACT | IAP flow | — | IAP callback receives tokens in the query string. | N-U43-112 |
| VDR-U43-C149 | FUNCTION MAPPING REQUIRED | microsoft_outlook/controllers/main.py:114 | active | FACT | callback | — | Tokens and expiry are stored sudo on the record. | N-U43-111 |
| VDR-U43-C150 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/microsoft_outlook_mixin.py:15 | google_gmail | FACT | always | — | Imports get_iap_error_message from google_gmail without declaring it in depends. | N-U43-117 |
| VDR-U43-C151 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/ir_mail_server.py:30 | constrains | FACT | always | — | SMTP outlook server: empty password, STARTTLS and user required. | N-U43-114 |
| VDR-U43-C152 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/ir_mail_server.py:57 | smtp.outlook.com | FACT | always | — | Onchange defaults smtp.outlook.com STARTTLS 587. | N-U43-113 |
| VDR-U43-C153 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/res_users.py:19 | smtp-mail.outlook.com | FACT | personal server | — | Personal server uses smtp-mail.outlook.com, mismatching ir_mail_server default. | N-U43-119 |
| VDR-U43-C154 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/fetchmail_server.py:53 | XOAUTH2 | FACT | imap | — | IMAP login uses XOAUTH2; SSL required (26-30). | N-U43-114 |
| VDR-U43-C155 | FUNCTION MAPPING REQUIRED | microsoft_outlook/models/ir_mail_server.py:91 | personal.limit | FACT | always | — | Personal server limit param default 10 minutes. | N-U43-111 |
| VDR-U43-C156 | FUNCTION MAPPING REQUIRED | microsoft_outlook/__manifest__.py:18 | auto_install | FACT | always | — | Manifest depends mail, auto_install true. | N-U43-109 |
