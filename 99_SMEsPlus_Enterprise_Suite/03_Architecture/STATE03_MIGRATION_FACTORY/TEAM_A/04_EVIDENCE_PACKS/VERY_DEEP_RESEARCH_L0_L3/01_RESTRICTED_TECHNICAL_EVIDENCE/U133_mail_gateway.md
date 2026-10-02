# U133 Mail Gateway — Restricted Technical Evidence
**Unit:** U133 | **Gap:** GAP-039 | **Priority:** P2 | **Group:** G13
**Date:** 2026-10-02 | **Researcher:** DeepSeek Worker (Claude Sonnet 4.6)

---

## L1 — Manifest / Dependencies

**Source:** `mail/__manifest__.py:63`

- Module name: `mail` (Discuss), version `1.19`
- `depends`: `['base', 'base_setup', 'bus', 'web_tour', 'html_editor']`
- Key data files registered:
  - `data/ir_cron_data.xml` (fetchmail cron)
  - `views/fetchmail_views.xml`
  - `views/mail_alias_views.xml`
  - `views/mail_alias_domain_views.xml`
  - `views/mail_gateway_allowed_views.xml`
  - `data/mail_templates_mailgateway.xml`

**Outgoing mail server:** `ir.mail_server` defined in `base/models/ir_mail_server.py:126`; extended by `mail/models/ir_mail_server.py`.

---

## L2 — Models / Fields / ORM

### mail.alias (`mail/models/mail_alias.py`)
- `alias_name` (Char, line 39): local-part of the email alias
- `alias_full_name` (Char computed+stored, line 42): full `alias_name@domain`, indexed btree_not_null
- `alias_domain_id` (Many2one `mail.alias.domain`, line 43): domain record
- `alias_model_id` (Many2one `ir.model`, required, line 48): target ORM model
- `alias_defaults` (Text, line 56): Python dict literal for default field values
- `alias_force_thread_id` (Integer, line 59): if set, all incoming mail attaches to this record
- `alias_parent_model_id` (Many2one `ir.model`, line 64): owner model (e.g. project vs task)
- `alias_parent_thread_id` (Integer, line 69): owner record ID
- `alias_contact` (Selection, line 73): `everyone | partners | followers`
- `alias_incoming_local` (Boolean, line 84): local-part-only matching flag
- `alias_bounced_content` (Html, line 85): custom bounce body
- `alias_status` (Selection, line 88): `not_tested | valid | invalid`
- Unique constraint: `(alias_name, COALESCE(alias_domain_id, 0))` line 96

### mail.alias.domain (`mail/models/mail_alias_domain.py`)
- `name` (Char, line 20): domain string e.g. `example.com`
- `bounce_alias` (Char, line 27): local-part for bounce Return-Path
- `catchall_alias` (Char, line 32): local-part for catchall Reply-To
- `default_from` (Char, line 37): default from local-part or full address
- Computed: `bounce_email`, `catchall_email`, `default_from_email`

### fetchmail.server (`mail/models/fetchmail.py`)
- `server_type` (Selection, line 104): `imap | pop | local`
- `is_ssl` (Boolean, line 110): SSL/TLS flag
- `object_id` (Many2one `ir.model`, line 121): target model for new records
- `priority` (Integer, line 125): processing order
- `script` (Char, line 128): default `'/mail/static/scripts/odoo-mailgate.py'`
- `state` (Selection, line 98): `draft | done`

### mail.gateway.allowed (`mail/models/mail_gateway_allowed.py`)
- `email` (Char, line 23): trusted email address
- `email_normalized` (Char computed+stored, line 24): normalized form for lookup
- System parameters: `mail.gateway.loop.minutes` (default 120) and `mail.gateway.loop.threshold` (default 20)

### ir.mail_server (`base/models/ir_mail_server.py:126`)
Extended by `mail/models/ir_mail_server.py`:
- `owner_user_id` (Many2one `res.users`, line 20): personal mail server owner
- `mail_template_ids` (One2many `mail.template`, line 14): templates using this server

---

## L3 — Workflow / State Machine

**Incoming email routing flow** (all in `mail/models/mail_thread.py`):

1. **`message_process`** (line 1438): top-level entry point.
   - Decodes RFC2822 bytes.
   - Calls `message_parse()` → `msg_dict`.
   - Duplicate check: `pg_try_advisory_xact_lock(hashtext(message_id))` (line 1488).
   - Calls `message_route()` → routes list.
   - Calls `_message_route_process()` → `thread_id`.

2. **`message_route`** (line 1122): route determination.
   - Step 1 (line 1185): reply-to-thread via `References`/`In-Reply-To` headers; searches `mail.message` by `message_id`.
   - Step 2 (line 1285): alias lookup — searches `mail.alias` by `alias_full_name IN rcpt_tos_list` OR `alias_incoming_local=True AND alias_name IN localparts`.
   - Step 3 (line 1304): fallback to provided `model` / `thread_id`.
   - Step 4 (line 1320): catchall bounce if no route found.
   - Raises `ValueError` if no route and no bounce (line 1336).

3. **`_routing_check_route`** (line 847): validates each candidate route.
   - Checks model exists and has `message_new` / `message_update`.
   - Checks `alias_contact`:
     - `followers`: author must be in `message_partner_ids` of target/parent record.
     - `partners`: author (res.partner) must exist.
     - `everyone`: always passes.
   - Calls `_alias_get_error()` (`models.py:785`) for the contact-security check.
   - On error: calls `alias._alias_bounce_incoming_email()` (`mail_alias.py:512`).

4. **`_message_route_process`** (line 1343): processes validated routes.
   - For each route: calls `message_update()` if thread exists, else `message_new()`.
   - Posts via `thread_root.message_post()` (line 1429) or `message_notify()`.

**Bounce handling** (`mail_thread.py:786`):
- `_routing_handle_bounce`: triggered when `message_dict['is_bounce']` is True.
- Updates `mail.notification` records with `failure_type='mail_bounce'` (line 832).
- Bounce Return-Path constructed from `mail.alias.domain.bounce_alias` + domain name.

**Catchall logic** (`mail_thread.py:1159`):
- `mail.catchall.domain.allowed` system parameter (optional allowlist of extra domains).
- Catchall email = `catchall_alias@domain_name` from `mail.alias.domain`.
- Direct write to catchall triggers bounce (line 1264).

---

## L4 — Cross-Module Dependencies

- `base`: `ir.mail_server`, `res.partner`, `ir.model`, `ir.config_parameter`
- `base_setup`: contributes to outgoing mail server configuration UI
- `mail/models/ir_mail_server.py`: extends `ir.mail_server` with `owner_user_id`, template tracking, personal server throttling

---

## L5 — Views / Wizards

- `views/fetchmail_views.xml`: UI for incoming mail servers
- `views/mail_alias_views.xml`: alias configuration forms
- `views/mail_alias_domain_views.xml`: domain configuration
- `views/mail_gateway_allowed_views.xml`: trusted-address allowlist

---

## L6 — Access / Record Rules

- `mail_security.xml`: no specific fetchmail/alias record rules found (open within group).
- `ir.mail_server._allow_sudo_commands = False` (`base/models/ir_mail_server.py:129`): prevents sudo bypass.
- SMTP credentials (`smtp_user`, `smtp_pass`) restricted to `base.group_system` (line 153-154).

---

## L7 — Configuration Prerequisites

1. At least one `mail.alias.domain` record must exist with valid `name`, `bounce_alias`, `catchall_alias`.
2. For POP/IMAP polling: `fetchmail.server` record in `state='done'` required; triggers cron activation via `_update_cron()` (`fetchmail.py:356`).
3. For MTA pipe gateway: deploy `mail/static/scripts/odoo-mailgate.py`; configure MTA alias to pipe stdin to script with `--host`, `--port`, `-u`, `-p`, `-d` params. Script calls `mail.thread.message_process` via XML-RPC (`odoo-mailgate.py:87`).
4. `mail.catchall.domain.allowed` system parameter (optional): restricts which domains gateway accepts.
5. Anti-loop parameters: `mail.gateway.loop.minutes` (default 120) and `mail.gateway.loop.threshold` (default 20).

---

## L8 — Immutability / Audit

- `alias_status` resets to `not_tested` on field changes (`mail_alias.py:241`).
- `alias_status` set to `valid` on successful record creation (`mail_thread.py:1381`).
- `alias_status` set to `invalid` on bounce from config error (`mail_alias.py:527`).

---

## L9 — Accounting / Stock Postings

**N/A** — mail gateway has no accounting or inventory postings.

---

## L10 — Cron / Queue / Import-Export

- **Cron `ir_cron_mail_gateway_action`** (`data/ir_cron_data.xml:40`):
  - Name: `Mail: Fetchmail Service`
  - Model: `fetchmail.server`, code: `model._fetch_mails()`
  - Interval: every 5 minutes
  - `active=False` by default; toggled by `_update_cron()` when `fetchmail.server` records are in `state='done'` (non-local type).
- **`_fetch_mails`** (`fetchmail.py:245`): called by cron; sorted by priority then date; calls `thread_process_message` per message using a separate DB cursor.
- **`_fetch_mail`** (`fetchmail.py:263`): per-server mail fetch; commits per message; handles IMAP/POP disconnection.
- **`OdooIMAP4`/`OdooPOP3`** classes (lines 27-87): custom wrappers for unread message retrieval.

---

## L11 — API Surface

- **XML-RPC**: `mail.thread.message_process(model, message_bytes)` — called by `odoo-mailgate.py:87`.
- **Cron**: `fetchmail.server._fetch_mails()` — internal cron entry, context-gated (`cron_id` check at line 247).

---

## L12 — Runtime / AWT (C3 — NOT YET PROVEN)

**AWT Test Plan:**

### AWT-1: IMAP/POP Server polling path
1. Create `fetchmail.server` with real IMAP credentials pointing to a test mailbox; confirm login; verify `state='done'`.
2. Send test RFC2822 email from external client to the test mailbox address.
3. Trigger `fetchmail.server._fetch_mails()` manually (or wait cron cycle).
4. Verify: new `mail.message` record created under correct model/thread_id; `alias_status='valid'` on matched alias.

### AWT-2: MTA pipe (odoo-mailgate.py) path
1. Configure postfix/sendmail alias pipe to `odoo-mailgate.py --host=localhost --port=8069 -d <db> -u 1 -p <pass>`.
2. Send RFC2822 email to alias address (e.g. `support@example.com`).
3. Verify: script exits 0; new `mail.message` / record created in Odoo.

### AWT-3: alias_contact enforcement
1. Set `alias_contact='followers'` on a `mail.alias`; send email from non-follower address.
2. Verify: bounce email returned; `alias_status='invalid'` (config error) or unchanged (non-config rejection).

### AWT-4: catchall bounce
1. Send email directly to `catchall@example.com` (no matching alias).
2. Verify: bounce email sent using `mail_bounce_catchall` template; no record created.

### AWT-5: duplicate suppression
1. Send same email (identical Message-Id) twice.
2. Verify: second invocation returns `False`; only one `mail.message` record.

### AWT-6: anti-loop throttle
1. Send >20 emails within 120 minutes from same address to an alias with record-creation route.
2. Verify: after threshold, further emails are blocked unless sender is in `mail.gateway.allowed`.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| C133-01 | F-ALIAS-MODEL | `mail/models/mail_alias.py:19-95` | `class MailAlias` / `_name = 'mail.alias'` | C1 | Always | C1 | `mail.alias` ORM model defines alias_name, alias_model_id, alias_contact (everyone/partners/followers), alias_force_thread_id, alias_parent_model_id fields | Alias routing table model with contact-security selector and optional forced-thread override |
| C133-02 | F-ALIAS-DOMAIN | `mail/models/mail_alias_domain.py:9-64` | `class MailAliasDomain` / `_name = 'mail.alias.domain'` | C1 | Always | C1 | `mail.alias.domain` stores domain name, bounce_alias, catchall_alias, default_from; catchall and bounce emails computed as `{alias}@{domain}` | Domain-level configuration record holding bounce and catchall local-part values |
| C133-03 | F-FETCHMAIL-MODEL | `mail/models/fetchmail.py:89-128` | `class FetchmailServer` / `_name = 'fetchmail.server'` | C1 | Always | C1 | `fetchmail.server` model stores IMAP/POP3 server credentials, server_type, priority, state; `object_id` field sets target model for new records | Incoming mail server account model supporting IMAP and POP3 protocol variants |
| C133-04 | F-FETCHMAIL-IMAP | `mail/models/fetchmail.py:27-57` | `class OdooIMAP4` / `class OdooIMAP4_SSL` | C1 | server_type=imap | C1 | Custom IMAP4 wrapper marks messages as unread via `store(num, '-FLAGS', '\\Seen')` during retrieval and `+FLAGS` on success; SSL variant inherits both | Custom IMAP connection wrapper restoring unread state during fetch to avoid message loss on failure |
| C133-05 | F-FETCHMAIL-POP | `mail/models/fetchmail.py:60-87` | `class OdooPOP3` / `class OdooPOP3_SSL` | C1 | server_type=pop | C1 | Custom POP3 wrapper calls `dele(num)` only after successful processing via `handled_message` | Custom POP3 wrapper deleting messages only after confirmed processing |
| C133-06 | F-FETCH-MAILS-CRON | `mail/models/fetchmail.py:245-258` | `def _fetch_mails` | C1 | cron context | C1 | `_fetch_mails` is the cron entry point; asserts `cron_id` context matches `mail.ir_cron_mail_gateway_action`; sorts servers by priority then date; calls `_fetch_mail` | Cron-gated method that sorts and dispatches mail fetch across all active incoming servers |
| C133-07 | F-FETCH-MAIL-LOOP | `mail/models/fetchmail.py:263-345` | `def _fetch_mail` | C1 | Always | C1 | `_fetch_mail` opens a separate DB cursor per server; calls `MailThread.message_process` for each unread message; commits per message; deactivates server after 5-day persistent failure | Per-server fetch loop with isolated transaction per message and auto-deactivation on prolonged failure |
| C133-08 | F-UPDATE-CRON | `mail/models/fetchmail.py:356-364` | `def _update_cron` | C1 | create/write/unlink | C1 | `_update_cron` toggles `mail.ir_cron_mail_gateway_action` active flag based on presence of `state='done'` non-local servers | Cron activation automatically managed on incoming server create, write, and delete events |
| C133-09 | F-MSG-PROCESS | `mail/models/mail_thread.py:1438-1512` | `def message_process` | C1 | Always | C1 | `message_process` is the public entry point for incoming RFC2822 bytes; deduplicates using `pg_try_advisory_xact_lock(hashtext(message_id))`; calls `message_route` then `_message_route_process` | Public gateway entry point parsing raw email bytes, deduplicating by advisory lock, and dispatching to routing |
| C133-10 | F-MSG-ROUTE | `mail/models/mail_thread.py:1122-1340` | `def message_route` | C1 | Always | C1 | `message_route` applies three-step heuristic: (1) reply-to-thread by References/In-Reply-To, (2) alias lookup by alias_full_name or local-part, (3) fallback model; raises ValueError if no route and no catchall bounce | Three-step routing heuristic matching incoming email to existing thread, named alias, or configured fallback model |
| C133-11 | F-ALIAS-LOOKUP | `mail/models/mail_thread.py:1285-1302` | inside `message_route` | C1 | rcpt_tos present | C1 | Alias lookup searches `mail.alias` where `alias_full_name IN rcpt_tos_valid_list` OR `alias_incoming_local=True AND alias_name IN localparts`; one route per matched alias | Full-address or local-part alias match generating one route tuple per alias recipient |
| C133-12 | F-ROUTE-CHECK | `mail/models/mail_thread.py:847-941` | `def _routing_check_route` | C1 | Always | C1 | `_routing_check_route` validates model existence, record existence, `message_new`/`message_update` presence, and `alias_contact` security; calls `_alias_get_error` and on rejection triggers bounce | Route validator enforcing model capability checks and alias contact-security policy before accepting a route |
| C133-13 | F-ALIAS-CONTACT-SEC | `mail/models/models.py:785-804` | `def _alias_get_error` | C1 | alias_contact in partners/followers | C1 | `_alias_get_error` returns `AliasError` if `alias_contact='followers'` and author not in `message_partner_ids`, or `alias_contact='partners'` and no author partner exists | Contact-security enforcement returning typed error when sender does not satisfy alias access policy |
| C133-14 | F-BOUNCE-INCOMING | `mail/models/mail_alias.py:512-534` | `def _alias_bounce_incoming_email` | C1 | route rejected | C1 | `_alias_bounce_incoming_email` sets `alias_status='invalid'` (config errors) or leaves it; calls `_routing_create_bounce_email` with optional custom body from `alias_bounced_content` | Bounce sender and optionally mark alias invalid when an incoming message fails routing checks |
| C133-15 | F-BOUNCE-CATCHALL | `mail/models/mail_thread.py:760-783` | `def _routing_create_bounce_email` | C1 | bounce triggered | C1 | `_routing_create_bounce_email` uses Return-Path header or email_from as bounce target; resolves bounce sender from `company.bounce_email`; creates and sends `mail.mail` immediately | Outbound bounce email generator using company bounce address as sender and Return-Path as recipient |
| C133-16 | F-HANDLE-BOUNCE | `mail/models/mail_thread.py:786-844` | `def _routing_handle_bounce` | C1 | is_bounce=True | C1 | `_routing_handle_bounce` processes inbound DSN/bounce: finds original notification records, updates them with `failure_type='mail_bounce'`; calls `_message_receive_bounce` on blacklist-enabled models | Inbound bounce processor updating notification failure status and propagating bounce data to blacklist-enabled models |
| C133-17 | F-CRON-DEF | `mail/data/ir_cron_data.xml:40-49` | `id=ir_cron_mail_gateway_action` | C1 | Always | C1 | Cron `Mail: Fetchmail Service` runs `model._fetch_mails()` on `fetchmail.server` every 5 minutes; `active=False` by default; enabled by `_update_cron` when active done servers exist | Gateway polling cron definition starting inactive and enabled automatically by server configuration |
| C133-18 | F-MAILGATE-SCRIPT | `mail/static/scripts/odoo-mailgate.py:62-113` | `def main` | C1 | MTA pipe | C1 | `odoo-mailgate.py` reads RFC2822 from stdin, calls `mail.thread.message_process` via XML-RPC `xmlrpc/2/object`; handles fault codes for missing alias (EX_NOUSER), bad database (EX_CONFIG), and connection errors (EX_TEMPFAIL) | MTA pipe script reading raw email from standard input and forwarding to the gateway entry point via authenticated remote call |
| C133-19 | F-ANTI-LOOP | `mail/models/mail_thread.py:1010-1060` | `_detect_loop_sender` region | C1 | Always | C1 | Loop detection checks sender against `mail.gateway.allowed`; reads `mail.gateway.loop.minutes` (default 120) and `mail.gateway.loop.threshold` (default 20); aborts route if record-creation count exceeds threshold | Spam-loop guard counting recent records created from same sender address and blocking if threshold exceeded within time window |
| C133-AWT1 | F-AWT-IMAP-POLL | N/A | Runtime | C3 | fetchmail.server configured | AWT,GAP | AWT: configure IMAP server, send test email, trigger cron, verify mail.message and alias_status='valid' created | Runtime verification of IMAP polling path creating a record and confirming alias validity |
| C133-AWT2 | F-AWT-MTA-PIPE | N/A | Runtime | C3 | odoo-mailgate.py deployed | AWT,GAP | AWT: pipe RFC2822 via MTA alias, verify XML-RPC call succeeds and record created | Runtime verification of MTA pipe path through the mailgate script and XML-RPC layer |
| C133-AWT3 | F-AWT-CONTACT-SEC | N/A | Runtime | C3 | alias_contact=followers | AWT,GAP | AWT: send email from non-follower to followers-only alias, verify bounce sent and record not created | Runtime verification of contact-security policy rejecting unauthorized senders |

---

*Generated by DeepSeek Research Worker U133 — STATE03 VDR*
