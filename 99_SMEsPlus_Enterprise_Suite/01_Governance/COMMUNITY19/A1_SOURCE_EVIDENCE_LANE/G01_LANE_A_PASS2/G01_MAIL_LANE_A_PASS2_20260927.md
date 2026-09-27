# G01 PLATFORM_BASE — Lane A PASS-2 Source Evidence (DELTA) — module `mail`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) — PASS-2 depth / gap closure, delta-first |
| Governed group / slot | G01 PLATFORM_BASE / T3 |
| Module | `mail` |
| Parent packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_MAIL_LANE_A_PASS1_20260927.md` sha256 `8511f925843c54984cc4fb0edf589c8e3421640e38e996551d236b7958be22e6` (not modified) |
| Source anchor | odoo/odoo @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/mail/` (one out-of-module pointer: `odoo/tools/config.py`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 via `git hash-object`; all cited fetches HTTP 200 |
| Date | 2026-09-27 |
| Status | **LANE A PASS-2 COMPLETE — HANDOFF TO A1 (DELTA)** |

Clean-room note: neutral WHAT / WHY / RISK only; identifiers are evidence pointers, not design input. No code reproduced. Source presence != runtime reachability. No runtime proof, no Formal Coverage, no percentages, no QID answered. Files already hashed in PASS-1 were re-read only where needed to close a gap; their blob SHA-1 re-computed and matched PASS-1 values (consistency check).

## 1. Gap closure table

| PASS-1 gap | Status | Pointer |
|---|---|---|
| G3 `tools/*` / guest-context authorisation | CLOSED (static) | F1-F5 |
| G4 `models/update.py` publisher-warranty cron | CLOSED (static) | F6-F9 |
| G2 `wizard/*` compose, mass mail/post, template rendering | CLOSED (static); two sub-points NARROWED (N2, N3) | F10-F20 |
| G8 / finding 36 allowed-company FIXME (`mail_message.py` ~L1361) | NARROWED (precise static scope stated; runtime effect OPEN) | F21-F23 |
| (e) multi-company of template / alias / activity | NARROWED | F24-F28 |
| G1, G5 (partial), G6, G7 | OPEN (not in PASS-2 brief) | section 4 |

## 2. Evidence Pointer Table (40 blobs; * = also in PASS-1, hash matches)

| Path | Git blob SHA-1 | Purpose |
|---|---|---|
| addons/mail/tools/__init__.py | 7c972410876c75417525580e090cd817294b7d75 | tools roster (6 modules) |
| addons/mail/tools/discuss.py | 692708b5629e7bf0330cdd463b5c1aa88453e6a3 | guest-context decorator, RTC/SFU key helpers, Store serializer |
| addons/mail/tools/link_preview.py | 18515419263f8fc005029601a5c7bc821cc9f727 | outbound URL fetch for previews |
| addons/mail/tools/parser.py | 803c43eb8357ee08f230e236f2c3841df6aa9ca4 | res_ids string parsing |
| addons/mail/tools/web_push.py | e660da83af7f5b0282b10b64367c0bfb8559da97 | web push encryption/VAPID send |
| addons/mail/tools/mail_validation.py | de7443c61464b3292415010e6b257d3bfe473685 | optional email validator fallback |
| addons/mail/tools/alias_error.py | b1c88086dbba31b03b9e2e4a331d9d297e34e95e | alias error value object |
| addons/mail/wizard/__init__.py | c9d933471e37b378a9423e81007f241f563df1df | wizard roster (9 modules) |
| addons/mail/wizard/mail_compose_message.py | 32fdf95981c9ea92af0d506711414decb32d2cd1 | composer: comment / mass_mail modes |
| addons/mail/wizard/mail_template_preview.py | 23b0e07760dc59d393dc165ef8513080c290f013 | template preview |
| addons/mail/wizard/mail_template_reset.py | 33036193b1dec7d16c21712c2a462d5864513577 | template reset |
| addons/mail/wizard/mail_followers_edit.py | aa7e46bade32f1f16f31ef1f0804db4659edb7e8 | bulk follower add/remove |
| addons/mail/wizard/mail_activity_schedule.py | 0e67cb0efe1b4903c7118d568b47d41de66f6220 | activity / plan scheduling |
| addons/mail/wizard/mail_activity_schedule_summary.py | d7396f58e6c2e9ba17c7e97fdd8a5e0f2d0845cd | schedule line |
| addons/mail/wizard/mail_blacklist_remove.py | f4347d54b9d9a7aebe79cd2693962b85bbb1bef0 | unblacklist with reason |
| addons/mail/wizard/base_partner_merge_automatic_wizard.py | 3a99a177281a2787e2a9786447f993c769f3bd75 | partner-merge chatter log |
| addons/mail/wizard/base_module_uninstall.py | 43e029ba85147b7842f0ab330d09a0a909307df1 | uninstall model filter |
| addons/mail/models/update.py | 05603784124c160005a75d3c77afee94c72d2f62 | publisher warranty contract model |
| addons/mail/models/__init__.py * | 553bd76763256a3cdd19b1863da6d8983eef76f8 | confirms `update` imported |
| addons/mail/models/mail_message.py * | 4a70962dbcad8cab3d6de3bf1b112e5e753a062b | ~L1352-1380 notification-update region |
| addons/mail/models/mail_composer_mixin.py | 57f7a65ac0654fa88fadea44c1c63a9847919bc2 | composer render elevation heuristic |
| addons/mail/models/mail_render_mixin.py * | 25ef82e3615fec8f6c5bba7defe79d706368f8bc | restriction predicate, engines |
| addons/mail/models/mail_template.py * | f95b8f53dd95166603eadd42013907b77a23870f | unrestricted flag, save-time checks |
| addons/mail/models/res_config_settings.py | 4347eaa77874e9b05214c8aa13a0acc930893c3e | restrict-rendering setting |
| addons/mail/models/ir_config_parameter.py | edbfc4f5c22d7414416c4dd839f425405db4f850 | param -> group toggle; ICP catalogue |
| addons/mail/models/discuss/mail_guest.py * | 9c7c2192c6d5da4f8b334c967a094c381b6c2786 | guest token/cookie |
| addons/mail/models/mail_mail.py * | 44c9e2d2066e5d0d01908e95298f3c7662e34b80 | caller of notification update (~L286) |
| addons/mail/models/mail_thread.py * | c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374 | caller of notification update (~L3262) |
| addons/mail/models/mail_alias.py * | 3d5c8fb2b32e82bc9a20f6cde25f036675d02989 | alias company-domain checks |
| addons/mail/models/mail_activity.py * | 66d9cd7994a49fc01d62d4992b64501cc26bfc48 | activity (no company field) |
| addons/mail/models/mail_activity_plan.py | aefe528e2d1517e2145abe568cd543445b42a1ac | plan company field |
| addons/mail/models/mail_activity_plan_template.py | 5510608988e2a99942d7d24aeeb83ff17c8086c3 | plan line company-related field |
| addons/mail/models/mail_alias_mixin.py * | 88cecd644378ce58ad57a5b2c199eeffa9eefc58 | alias created in record company |
| addons/mail/models/mail_link_preview.py | 153d3026c1f392519078fa17a6e47a1c2b075689 | link preview caller / throttle |
| addons/mail/data/ir_cron_data.xml * | d72aacbe8f9e17e84d4dd62dfc3642a1ba4dc9fd | publisher cron record |
| addons/mail/data/mail_groups.xml * | 4b4125ed11ba10696bb321cf40f7573ec4387ec8 | template editor group |
| addons/mail/data/ir_config_parameter_data.xml * | 1f556c605ddc3dbd13dbf68554cabec78dc47906 | restrict-rendering seed |
| addons/mail/security/mail_security.xml * | 0219605e445b1f0f545e78f15aa6bca9084a0b5b | composer/template rules; company grep |
| addons/mail/security/ir.model.access.csv * | 29275551e7ca156899fa03985765fb2828de0b06 | wizard ACLs |
| odoo/tools/config.py (out-of-module) | 433ff84b625a69e08cce9f42911aa608d3e615ee | publisher URL option default |

## 3. Findings

### 3.1 Guest context (G3)
1. Guest identity on public-auth routes is established by a decorator that reads one named cookie (`dgid`), splits it into guest id + secret, loads the guest with elevation, and accepts it only if the stored secret matches under a constant-time comparison; otherwise the guest is empty. Elevation is dropped before returning. (`tools/discuss.py` `add_guest_to_context`; `models/discuss/mail_guest.py` `_get_guest_from_token`)
2. The guest secret is a random UUID4 generated at creation, readable only by system admins; the cookie is set HttpOnly with a 365-day expiry. No Secure/SameSite attribute is passed in this call, and no rotation/revocation routine was seen in the files read. RISK: long-lived bearer cookie; transport/samesite posture depends on framework defaults (not verified). (`mail_guest.py` `_set_auth_cookie`, `_format_auth_cookie`)
3. The context-resident guest is honoured only if it is an actual guest record instance (and at most one); a scalar value in context is ignored. WHY: prevents a client-supplied context value from asserting a guest. (`mail_guest.py` `_get_guest_from_context`)
4. The decorator may write a timezone taken from a `tz` cookie (validated against the timezone list) when the guest has none and the cursor is writable. Same decorator serves websocket requests. (`tools/discuss.py`)
5. Other tools: link-preview fetch issues outbound GET with redirects, 3 s timeout, streamed, custom UA; no private-address/SSRF filter visible in the tool or its caller (only a per-domain throttle param `mail.link_preview_throttle`, default 99, 0 disables). Web push POSTs to a device-supplied endpoint; only `.invalid` hosts are refused; VAPID JWT 12 h. `parse_res_ids` accepts only literal lists of ints. RTC helpers read Twilio/SFU credentials from params or environment variables. RISK: server-side outbound requests to user-influenced URLs. (`tools/link_preview.py`, `models/mail_link_preview.py`, `tools/web_push.py`, `tools/parser.py`, `tools/discuss.py`)

### 3.2 Publisher-warranty cron (G4)
6. The model is abstract, defined inside `mail` and imported by the models roster. Weekly cron runs as the root user, priority 1000, first run +7 days; the default cron list action is overridden to hide this cron. (`models/update.py`, `models/__init__.py`, `data/ir_cron_data.xml`)
7. Data leaving the instance (single HTTP POST, form field containing JSON): database UUID, database name, DB create date, product version, counts of active users / users active in last 15 days / share users / active share users, installed application names, enterprise code, web base URL, the calling user's language, and — if the calling user's partner has a company — that company's name, email and phone. (`models/update.py` `_get_message`)
8. Destination: server config option `publisher_warranty_url`, a file-only option whose default is an `http://` (not https) vendor services URL; timeout 30 s. The response is parsed as a Python literal; its "messages" are posted as elevated comments into the all-employees channel addressed to the root partner, and "enterprise_info" overwrites six `database.*` config params (expiration date/reason, enterprise code, linked-subscription URLs/email). RISK: plaintext egress by default; remote content injected into an internal channel and config params. (`models/update.py`, `odoo/tools/config.py` ~L215)
9. Disable paths visible statically: deactivate/delete the cron record (hidden from the default list, but it is a normal cron record in a noupdate block); or change the file-only URL option. No `mail`-level param toggle exists. Note: cron passes an explicit null for `cron_mode`, which is falsy, so failures re-raise instead of being silently swallowed — the "catch all in cron" branch is not taken by the scheduled call. (`data/ir_cron_data.xml`, `models/update.py`)

### 3.3 Wizards / compose / template rendering (G2)
10. Composer ACL: internal users read/write/create, no unlink; record rule restricts read/write to the creator. Portal/public have no composer ACL. (`security/ir.model.access.csv`, `security/mail_security.xml`)
11. Two modes: comment (per-record message post, including batch "mass post") and mass_mail (email generation). Comment mode calls the document's post routine per record (so post-access checks of the thread apply) or a generic notify when the model is not a thread; batch comment suppresses author auto-follow. (`wizard/mail_compose_message.py` `_action_send_mail_comment`)
12. Mass mail: target ids come from a stored domain searched as the current user (record rules apply) or from an explicit id list. There is no explicit per-record access check; the source comment states access is enforced implicitly by reading records during value preparation, after which outgoing mails are created elevated and notifications created. Batch size from `mail.batch_size` (fallback 50); direct send capped by `mail.mail.force.send.limit`. RISK: authorisation depends on implicit reads during rendering. (`_action_send_mail_mass_mail`)
13. Mass-mail values carry the record company and alias domain per target record; default recipients are used when no template/partners; blacklist exclusion defaults on. (`_prepare_mail_values_dynamic`)
14. Scheduling is allowed only in single-record comment mode. (`_action_schedule_message`)
15. Rendering restriction predicate: a render-mixin user is "restricted" unless the model is flagged unrestricted, a private bypass sentinel is in context, the user is admin, or the user is in `mail.group_mail_template_editor`. Restricted users: inline_template with non-trivial expressions is refused; qweb rendering runs with forbidden-code checks for the model; placeholder-only content goes through a regex fast path. (`models/mail_render_mixin.py` `_is_restricted`, `_render_template_*`)
16. Templates are flagged unrestricted at render time; protection moves to save time: create/write/translation update raise if a non-editor saves content with unsafe expressions (superuser exempt). Template save also test-renders dynamic fields on one record of the target model and rejects abstract models. (`mail_render_mixin.py` create/write, `models/mail_template.py`)
17. Composer elevation heuristic: when a template is set and the user is not an editor, rendering is elevated (bypass sentinel) only if the field value equals the template value; for body, if the user cannot edit the body or it still equals the template, the template body is forced back before elevated rendering. Non-editors can edit the body only when no template is set (mass_mail excluded). Without a template, no bypass. WHY: trust validated master data only. (`models/mail_composer_mixin.py`)
18. Group membership toggle: setting param `mail.restrict.template.rendering` falsy makes all internal users inherit the editor group; truthy removes it (admins retain via system group). Seed value is 1 (restricted). Contradiction noted: the in-code ICP catalogue comment says "Not activated by default" while the data seed activates it. (`models/ir_config_parameter.py`, `data/ir_config_parameter_data.xml`, `models/res_config_settings.py`)
19. Template preview: internal-user ACL; the target record is user-selectable; rendering is done by the (unrestricted) template as the current user, so record reads follow user access; model list populated elevated. Template reset: editor group only. (`wizard/mail_template_preview.py`, `wizard/mail_template_reset.py`, ACL csv)
20. Other wizards: followers edit delegates to thread subscribe/unsubscribe (their access rules apply) and requires sender email to notify; blacklist remove is system-admin only; partner merge logs a chatter message listing merged partners' names/emails; uninstall wizard filters to thread models; activity scheduling filters plans by company (see F27) and checks an upload-type assignee's create access by impersonation. (`wizard/*`)

### 3.4 Allowed-company FIXME (G8)
21. Scope: the FIXME sits in the routine that pushes notification-status updates over the bus. It keeps a message only if the linked document passes a read-access check and still exists, evaluated in the calling environment (current user and its company context). No explicit allowed-company evaluation is performed; the FIXME records that as unresolved. (`models/mail_message.py` ~L1352-1380)
22. What is not checked: the filtered set is then sent to the current user and to the message author (if non-public), serialised under the author's user, but the access filter was evaluated for the current user only, not per recipient. Payload: body, date, type, recipient notification statuses, document display name and model label. (same)
23. Callers: outgoing-mail post-processing on failure (~L286) and bulk cancel of a user's failed notifications (~L3262). Whether the first caller runs as superuser (which would make the check always pass) depends on the send path and is not proven. RISK: cross-company / cross-user leakage of message snippets via bus. (`models/mail_mail.py`, `models/mail_thread.py`)

### 3.5 Multi-company (e)
24. No company-based record rules exist in `mail_security.xml` (grep for "company" returns none). (`security/mail_security.xml`)
25. Templates carry no company field; company enters only at render time (record company for layout). The template source itself warns that partner find-or-create during recipient rendering can merge data from records of different companies into one partner. (`models/mail_template.py` ~L419)
26. Aliases: created in the owning record's company; validated so the alias domain matches the owner/target document company when the domain is company-bound; default domain from current company. (`models/mail_alias.py` ~L101-175, `models/mail_alias_mixin.py`)
27. Activities: no company field; access derived from the document. Plans carry a company (default current); plan-line company is related to plan; filtering to "no company or scheduler company" happens in the scheduling wizard, which also blocks mixed-company record batches. No record rule backs plan company scoping. (`models/mail_activity.py`, `models/mail_activity_plan*.py`, `wizard/mail_activity_schedule.py`)
28. Plan-line responsible field has a company-check attribute; a model-level automatic company-check flag was not found in the file, so enforcement strength is unverified.

## 4. New gaps / open items
- N1: Framework defaults for cookie Secure/SameSite and guest route coverage per controller (which routes lack the decorator) — needs controller-by-controller pass / runtime.
- N2: Whether mass_mail value preparation truly reads every target record as the user (implicit-read authorisation) — requires full trace of `_prepare_mail_values*` and template generation; runtime proof advised.
- N3: Rendering bypass heuristic equality checks (esp. HTML sanitisation of body equality `body_has_template_value`) — edge cases not proven.
- N4: Superuser vs user env on mail-failure path for F23.
- N5: `mail.channel_all_employees` xmlid definition not located in files fetched.
- N6: No SSRF/private-network filter seen for link preview/web push — confirm no framework-level guard.
- Carried OPEN: G1, G5 (remaining models only fetched, not studied), G6, G7.

## 5. Limitations
- Static reading only; no execution, no runtime reachability. Line numbers (~L) valid at anchor only.
- Out-of-module pointer (`odoo/tools/config.py`) used solely for the URL default.
- Other modules' overrides (e.g. mass mailing, enterprise) out of scope and may change behaviour of composer/templates.
- Delta-only packet; read together with parent PASS-1.
