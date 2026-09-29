# Source Map (candidate) — `mail_group`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mail_group` |
| Display name | Mail Group |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `50e43c069373fb23` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mail_group/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`, `portal`
- Direct dependents in 300-module list (1): `website_mail_group`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: None / Manage your mailing lists
- Inventory of user-facing artifacts (counts): menu items 2, views 12, window actions 6, server actions 0, reports 0, mail templates 3, scheduled jobs 1, wizards 1, web routes 9
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `mail.group.message.reject` (Reject Group Message); `mail.group.member` (Mailing List Member); `mail.group` (Mail Group); `mail.group.message` (Mailing List Message); `mail.group.moderation` (Mailing List black/white list)
- Objects extended from other modules (1): `mail.alias.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `mail.group` ← Community: `website_mail_group`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.alias.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `mail.group.moderation` → ['allow', 'ban']
- Validation: 6 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Mail List: Notify group moderators every 1 days
- Security: groups declared 2 (`group_mail_group_manager`, `base.group_system`); record rules 10 (of which company-scoped by text 0); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 45 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — mail_group
Source revision: 19.0.post20260921 | Module: "Mail Group" (mail_group/__manifest__.py:5) | LGPL-3 (:45)
Basis: static reading of models, security, controller (route list and subscription routes), wizard, cron, manifest; views/templates and tests by title only.
## A. Capabilities and optionality
- A1. Mailing lists managed in Odoo: people send an e-mail to the group's address; the message is archived and re-sent to all members; optional moderation. mail_group/__manifest__.py:6-9; mail_group/models/mail_group.py:27-33,280-369,410-486
- A2. Optional add-on (not auto_install, no application flag); depends on mail and portal. mail_group/__manifest__.py:11-14
- A3. Public web pages (routes under /groups) to browse archives and to subscribe/unsubscribe; page exposure depends on the website side, provided by website_mail_group (snippet/menu) which depends on this module. mail_group/controllers/portal.py:63-64,107-108,147-148,242-244,276-278; website_mail_group/__manifest__.py:8
- A4. Conditional features: moderation (per group switch), guidelines mail to newcomers (moderated-group option), automatic notification to a sender whose message is pending, privacy modes Everyone / Members only / Selected group. mail_group/models/mail_group.py:64-84,349-367,598-600
- A5. Demo data present but only loaded in demo mode. mail_group/__manifest__.py:32-34
## B. Objects and lifecycle
- B1. Mail Group (mail.group): name, description, image, closed flag, privacy mode, authorised group, moderation settings, moderators, members, messages, e-mail alias. mail_group/models/mail_group.py:34-84
- B2. Member (mail.group.member): e-mail and optional partner; one subscription per partner per group. mail_group/models/mail_group_member.py:12-28
- B3. Group message (mail.group.message): wraps a chatter message with parent/children threading and a moderation status Pending / Accepted / Rejected, and the moderator who decided. mail_group/models/mail_group_message.py:19-62
- B4. Moderation rule (mail.group.moderation): per e-mail address in a group, "Always Allow" or "Permanent Ban"; one rule per address per group; address normalised. mail_group/models/mail_group_moderation.py:8-39
- B5. Reject wizard: choose Reject or Ban, optionally compose an explanatory e-mail to the author. mail_group/wizard/mail_group_message_reject.py:8-42
- B6. Inbound lifecycle: e-mail to alias -> routing (bounced if group closed) -> message stored -> if group not moderated: sent to all members immediately; if moderated: rule "allow" auto-accepts, rule "ban" auto-rejects, otherwise waits Pending (optional automatic acknowledgement to the sender). mail_group/models/mail_group.py:536-550,332-367
- B7. Moderator actions: accept (sends to members), reject, reject with comment, allow author (accepts all their pending messages in that group), ban author (rejects all their pending messages). Only Pending messages can be moderated. mail_group/models/mail_group_message.py:112-181,215-229
- B8. Daily reminder to moderators of groups that still have Pending messages. mail_group/data/ir_cron_data.xml:3-12; mail_group/models/mail_group.py:488-522
- B9. Membership: join/leave from the backend or web; joining a closed group is refused; members with a partner follow the partner's e-mail. mail_group/models/mail_group.py:556-619; mail_group/models/mail_group_member.py:30-36
## C. Validations, automation, security, external service
- C1. Constraints: moderators must have e-mail; a moderated group needs moderators; notification and guidelines options need their texts; "Selected group" privacy needs an authorised group. mail_group/models/mail_group.py:206-229
- C2. Sending rules by privacy mode (inbound): Members only -> sender must be a member (else bounce); Selected group -> sender e-mail must belong to a user of that group. mail_group/models/mail_group.py:251-268
- C3. Closed group: incoming mail is bounced with a message; the group stays readable. mail_group/models/mail_group.py:51,536-550
- C4. Delivery to members: one mail per unique address, author excluded, batches (500 default, system parameter), with list headers (archive, subscribe, unsubscribe one-click, list id, precedence list) and a per-member footer with unsubscribe link. mail_group/models/mail_group.py:424-486
- C5. Subscription security: anonymous subscribe/unsubscribe sends a confirmation e-mail with a signed link; logged-in users act directly; one-click unsubscribe (POST, CSRF disabled deliberately) requires a signed token per e-mail. mail_group/controllers/portal.py:218-240,242-308,344-375; mail_group/models/mail_group.py:661-713
- C6. Access rights (table): public and portal read-only on groups and messages; internal users full model rights on groups, members, messages, moderation rules and reject wizard, narrowed by record rules below. mail_group/security/ir.model.access.csv:2-10
- C7. Record rules: groups readable when public, or user is moderator, or user's group matches "Selected group", or user is a member of a "Members only" group; moderators can modify/delete their groups; the Mail Group Administrator group sees everything. mail_group/security/mail_group_security.xml:3-45
- C8. Messages: public/portal see only Accepted messages of groups they can read; internal users see Accepted messages of readable groups plus non-accepted only as moderator. mail_group/security/mail_group_security.xml:46-97
- C9. Members and moderation rules are visible only to the group's moderators (internal) or administrators. mail_group/security/mail_group_security.xml:108-147
- C10. Administrator group "Mail Group Administrator" is implied by system administrators. mail_group/data/res_groups.xml:3-8
- C11. Guidelines can be sent by an administrator or a moderator only, not for closed groups; banned addresses are skipped. mail_group/models/mail_group.py:371-408
- C12. Body clean-up: the mailing footer is stripped from incoming replies before storage. mail_group/models/mail_group.py:524-534
- C13. Company scoping: no company field on groups or messages and no multi-company rules; sender address for notices comes from the acting user's company or the catch-all. mail_group/models/mail_group.py:363,514,633; UNKNOWN — EVIDENCE INSUFFICIENT for multi-company behaviour of aliases (owned by mail).
- C14. External-service implication: relies on the database's incoming and outgoing mail servers and catch-all/alias domain; a missing alias domain is logged as an error. mail_group/models/mail_group.py:417-418
## D. Handoffs
- D1. Alias creation/routing, mail queue, templates, composer, chatter message storage: mail. mail_group/models/mail_group.py:14-19,231-237,295-323,486
- D2. Web publishing (snippet, website menu) of groups: website_mail_group. website_mail_group/__manifest__.py:6-14
- D3. Portal/website pages and access tokens: portal. mail_group/__manifest__.py:13; mail_group/controllers/portal.py:63-391
- D4. Member mass mailing from a member list ("Send email" list action) uses mail.compose.message in mass mode. mail_group/views/mail_compose_message_views.xml:3-14
- D5. Mailing campaigns to groups vs. this module: (TEST) mail_group/tests/test_mail_group_mailing.py — file-level pointer only; UNKNOWN — EVIDENCE INSUFFICIENT for the relationship with mass_mailing.
## E. Configuration that changes outcomes
- E1. Privacy mode and authorised group; moderation on/off; moderators; automatic notification text; guidelines text; closed flag. mail_group/models/mail_group.py:51,64-84
- E2. Alias name / contact policy: alias contact policy defaults to Everyone for public groups and Followers otherwise. mail_group/models/mail_group.py:40-45,192-197
- E3. Batch size system parameter for member mailings. mail_group/models/mail_group.py:429
- E4. Moderation rules per sender (allow/ban) override manual decisions. mail_group/models/mail_group.py:342-357
## F. Extension path
- mail (alias, mail queue, composer), portal, mail_group (this), website_mail_group (only Community module naming it in a manifest dependency).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of attachments and size limits for group messages beyond passing attachments to members.
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction with the mass-mailing module (no dependency found).
- UNKNOWN — EVIDENCE INSUFFICIENT: content of the web archive templates (views/portal_templates.xml not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: retention/archiving of messages (only an active flag on groups was seen).

