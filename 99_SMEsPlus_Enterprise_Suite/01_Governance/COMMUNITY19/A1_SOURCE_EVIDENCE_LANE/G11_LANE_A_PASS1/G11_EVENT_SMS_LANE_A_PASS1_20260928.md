> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_sms` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_sms` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_sms/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, security CSV/XML, seed data (full — module is small). No views exist in this module. JS asset, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstraction only; no verbatim vendor code reproduced beyond short field/method-name pointers; the two seed SMS message bodies are quoted in section 2.2 as literal seed-data content (not proprietary logic) because their exact wording is itself the evidence (what attendees actually receive). No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (10 blobs)

| Path (addons/event_sms/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 582855ae69060d176493983e6c01f2c724700322 | Name "SMS on Events", depends `event`+`sms`, `auto_install: True` |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package init |
| `data/sms_data.xml` | e8fd9ea45c9ba2557cbb381e16f97cce84e18a23 | Seed two `sms.template` records: registration confirmation + reminder |
| `models/__init__.py` | 007f80cf0b3a45efe28700fb88fcd29fe8c2b74e | Model import roster |
| `models/event_mail.py` | f1d605ef599aa52c865e15df17c96050fcbfc624 | `event.mail` extension: adds `sms` as a notification type/template kind |
| `models/event_mail_registration.py` | e1ad66c4edb1f9adc00f3ee9ad86a9478b5a9d16 | `event.mail.registration` extension: SMS dispatch on the attendee-based execution path |
| `models/event_type_mail.py` | fcd0ae7096cd300e419341f4f1ae3346225f7977 | `event.type.mail` extension: same SMS selection/reference addition at template level |
| `models/sms_template.py` | 771467322b52f0563b0ed487cad77d8354f93746 | `sms.template` extension: event-scoped search filter, cascade-cleanup on unlink |
| `security/ir.model.access.csv` | b34e4dd5b87e19c2421c14a7a70b5994cfee0663 | Model ACL (1 row) |
| `security/sms_security.xml` | 87f028ff232d6e7fa7a9a73ad705f35e3d9c3461 | `ir.rule` scoping SMS-template write access for event managers |

Blobs cited: **10**. All returned HTTP 200 and hash-verified against the pinned-commit tree. This module has no `views/` directory in the pinned-commit tree (confirmed via the tree listing, not merely absent from the fetch plan) — its only UI surface is the backend asset for the "template reference" widget, reused from `mail`'s equivalent field.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_sms` extends `event`'s automated-communication scheduler (`event.mail`, evidenced separately in `event`'s file) so that a schedule entry can send an SMS instead of an email, using the `sms` app's own `sms.template`/dispatch machinery. `depends`: `event`, `sms`; `auto_install: True` (installs automatically once both are present, consistent with the other bridge modules in this pilot). (`__manifest__.py`)
2. This module has no `views/` directory at all in the pinned-commit tree; its only asset is a backend JS/XML/SCSS widget (`template_reference_field`) for rendering the polymorphic mail/SMS template-reference field in forms — presumably shared with, or parallel to, `mail`'s own such widget (not verified against `mail`'s file in this pass). (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `event.mail` and `event.type.mail` extensions both add `'sms'` to the `notification_type` selection and to the `template_ref` Reference field's selection/`ondelete` map (so a scheduler or template line can reference an `sms.template` and cascade-delete if that template is removed). No new model or field beyond these two selection-add extensions and the shared `_compute_notification_type` override (sets `notification_type='sms'` whenever the referenced template is actually an `sms.template`, overriding `event`'s base default of `'mail'`). (`models/event_mail.py`, `models/event_type_mail.py`)
4. Two seed `sms.template` records, both bound to `event.registration`: "Event: Registration" — `{{ object.event_id.organizer_id.name or object.event_id.company_id.name or user.env.company.name }}: We are happy to confirm your registration for the {{ object.event_id.name }} event.`; and "Event: Reminder" — a conditional template that includes the event's start time/timezone and address if known, or a generic "join us on [website URL]" line if the event has no physical address (checking, at render time, whether `website_published` even exists as a field on `event.event`, i.e. gracefully degrading when the optional `website_event` module is not installed). WHY quoted verbatim: this is exactly the message content end users (attendees) receive, which is itself the evidence, not a description of proprietary logic. (`data/sms_data.xml`)

### 2.3 Business rules / states / lifecycle / exceptions
5. Dispatch routing: `event.mail._execute_event_based_for_registrations` is extended so that, when `notification_type == 'sms'`, it calls `_send_sms(registrations)` (which calls `registrations._message_sms_schedule_mass(template=..., mass_keep_log=True)` — an `sms` app method, not defined in this module) instead of falling through to `event`'s base mail-sending path; `_template_model_by_notification_type` is extended so the base scheduler's template-validity check (`_filter_template_ref`, evidenced in `event`'s file) recognizes `sms.template` as the correct model for an `sms`-typed scheduler. Together, these two overrides are the entire mechanism by which `event.mail.execute()` (unchanged, defined in `event`) transparently sends SMS instead of email for SMS-typed schedulers — no new scheduling, batching, or cron logic is added in this module; it reuses `event`'s scheduler execution, batching, error-handling, and cron entirely, only substituting the send action. (`models/event_mail.py`)
6. The attendee-based (`after_sub`) execution path is separately overridden on `event.mail.registration._execute_on_registrations`: SMS-typed registration-mail rows are filtered out and sent via `scheduler._send_sms(...)` directly (marked `mail_sent=True`), while any remaining (non-SMS) rows fall through unchanged to the base mail-sending implementation — i.e. within a single mixed-type batch of pending per-attendee communications, SMS and email rows are dispatched through two different code paths but as one combined `execute()` call. (`models/event_mail_registration.py`)
7. `sms.template` extension mirrors `mail`'s own `mail.template` extension pattern (evidenced in `event`'s file) exactly: a context-flag-gated `_search` override restricts a reference-field picker to only `event.registration`-bound templates, and `unlink()` cascades to delete any `event.mail`/`event.type.mail` rows still referencing a deleted SMS template. (`models/sms_template.py`)

### 2.4 Security
8. ACL (1 row): `sms.template` — full CRUD, restricted to `event.group_event_manager`. This is the *only* ACL row this module adds; no ACL changes are made to `event.mail`/`event.type.mail`/`event.mail.registration` themselves (their access continues to be governed entirely by `event`'s own ACL, evidenced separately). (`security/ir.model.access.csv`)
9. One `ir.rule`, applied only to `base.group_multi_company`-independent — actually applied unconditionally per its `groups` eval, which restricts it to members of `event.group_event_manager` (not `base.group_multi_company` as in some other modules in this pilot — re-checked: the `groups` field here scopes *which users the rule applies to*, i.e. it targets event managers specifically) and sets `domain_force` to `[('model_id.model', 'in', ('event.event', 'event.registration'))]` with `perm_read` explicitly set to `False`. WHAT this means: an event manager's write/create/unlink access to `sms.template` (already granted at the ACL layer, finding 8) is further narrowed by this rule to only those SMS templates bound to `event.event` or `event.registration` models — they cannot use their `sms.template` ACL grant to affect unrelated SMS templates belonging to other apps (e.g. marketing SMS campaigns), and the rule does not restrict *read* (per `perm_read=False`, meaning this rule does not apply to the read operation at all, so read access is governed solely by the base ACL/other rules). RISK: A1/A2 should double-check this `perm_read=False` semantic against actual `ir.rule` behavior (it typically means "this domain is not enforced for read," not "read is denied") since it is easy to misinterpret. (`security/sms_security.xml`)

### 2.5 UI surfaces (names only, not fetched/read)
10. No `views/` directory exists in this module. Its only UI-adjacent asset is the `template_reference_field` widget bundle (JS/XML/SCSS, not fetched).

### 2.6 Jobs / config / integrations
11. No crons and no `ir.config_parameter` reads found in this module's fetched files — it reuses `event`'s existing `event_mail_scheduler` cron entirely (finding 5). The only external integration is indirect, through the `sms` app's own outbound SMS gateway, not touched directly by this module's code. (`__manifest__.py`, `models/event_mail.py`)

## 3. Cross-module edges
12. Depends on `event` and `sms` (dependency relationship only, not group membership per MD-07/08); `auto_install: True` — presence in a database is a consequence of both being installed, consistent with the pattern in every other bridge module in this pilot. (`__manifest__.py`)
13. This module is structurally the SMS-flavored mirror of `mail.template`'s extension inside `event` itself (both add a notification-type option, a `template_ref` selection-add, a search-filter context hack, and an unlink-cascade) — a design pattern A1 should recognize as repeated once per notification channel `event` supports, not module-specific novelty.
14. The seed reminder template's graceful-degradation check for `website_published` (finding 4) is a direct, source-visible acknowledgment that `event_sms` expects to sometimes run without `website_event` installed — a soft coupling flagged as a design observation, not a `depends` entry (matches MD-07/08 discipline: this is not a group-membership claim).

## 4. Evidence gaps / contradictions
- G1: The `template_reference_field` JS/XML/SCSS widget bundle was not fetched.
- G2: `sms.template._message_sms_schedule_mass` (the actual outbound-send implementation, defined in the `sms` app, not this module) was not fetched or verified — its behavior is taken as a call-site reference only.
- G3: i18n and tests not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 10 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
