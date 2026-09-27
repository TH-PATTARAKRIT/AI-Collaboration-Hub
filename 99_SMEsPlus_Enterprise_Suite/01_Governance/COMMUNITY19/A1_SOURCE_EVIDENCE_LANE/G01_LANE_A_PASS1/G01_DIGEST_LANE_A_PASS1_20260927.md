# G01 PLATFORM_BASE — Module `digest` — Lane A Pass-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | SMEsPlus LANE A (blind source/static evidence) |
| Slot | T5 |
| Governed group | G01 PLATFORM_BASE |
| Module | `digest` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0, commit `8d05257d83f9128953f580a066db67c48fcdb96f` (raw.githubusercontent fetch) |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material consulted. No GMVQ QID answered. |

## 1. Evidence Pointer Table

| Path (addons/digest/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 6ee68b6fd27c098ee26ff71351af956f9aed6f67 | Identity, deps, data list |
| `__init__.py` | 7d34c7c054abd3105d5bb41fe9674111e1c27c16 | Package import graph |
| `models/__init__.py` | 1882e860af3dc5ffa10af7d15448d6fae4784f15 | Model import list |
| `controllers/__init__.py` | 903b755e71e3d1673e604f1c47e60a45e9181542 | Controller import list |
| `models/digest.py` | 3eea1c39f8c5aa53b6eb1a43acc986d7f0ed204c | Digest model: KPIs, periodicity, send, slowdown, token |
| `models/digest_tip.py` | 8c0208db9ad28ed2d8fc8f803cf245d75b04e078 | Tip model |
| `models/res_config_settings.py` | 59f13bdff4ec4cafb69c9bd268b35a0cec11da75 | Settings bound to config params |
| `models/res_users.py` | 4488455454832441de947a9e8c49eedcc5214fc9 | Auto-subscribe new internal users |
| `controllers/portal.py` | b0e76145b13ecdbc4b69fd7bdeddcfac66ae5ffc | Unsubscribe / set periodicity routes |
| `security/ir.model.access.csv` | 49ef355262e6ea7d15eba86ab876f0e072ffedba | ACL |
| `data/digest_data.xml` | 649268fe3378ae29f32a48159bea7a35dd4aa146 | Default digest record + email templates |
| `data/digest_tips_data.xml` | 29c504458e102e5e13c6f6b0c817da9ef0e28b16 | Seed tips |
| `data/ir_cron_data.xml` | a6c1d0915a54e21f36867bede259f9b46a7436a1 | Scheduled send job |
| `data/res_config_settings_data.xml` | cacc318daf09fbdc42f9fe7de2533d718ec0c931 | Default config params |
| `views/digest_views.xml` | e0dd92c650bcc21b72564d259240f77147a619d1 | Backend list/form/search, actions, menus |
| `views/digest_templates.xml` | 9f7ddb754dfa3695cb28695abce41c246f166c9c | Public "unsubscribed" confirmation page |
| `views/res_config_settings_views.xml` | 0c99862f74e6beeaf0ccb16d3ccf31d53c5cf6c7 | Settings block |

Blob count: 17.

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. Purpose: periodic KPI summary emails to internal users. Category Marketing; not auto-install (`__manifest__.py`).
2. Deps: `mail`, `portal`, `resource`. Data: ACL, default digest, tips, cron, default config params, backend views, portal template, settings view.

### 2.2 Data (models, key fields, constraints)
3. `digest.digest`: translatable required name; recipients (users, UI domain restricted to non-share users); periodicity {daily, weekly, monthly, quarterly} default daily, required; next mailing date; optional company (defaults to current company); currency related to company; state {activated, deactivated} readonly, default activated (`models/digest.py`).
4. KPI pattern: each KPI is a boolean toggle plus a computed non-stored value field sharing a name stem; base ships two KPIs — connected users, messages sent. KPI discovery is by naming prefix (`kpi_`, `x_kpi_`, `x_studio_kpi_`), which also admits custom/studio fields (`_get_kpi_fields`, `_compute_available_fields`).
5. `digest.tip`: sequence (ordering), translatable name, HTML description (translatable, stored unsanitized), "already received" users, authorized group (default internal user) (`models/digest_tip.py`).
6. No SQL/Python constraints declared on either model.
7. Settings: two config-param-backed fields — enable default digest for new users (`digest.default_digest_emails`) and which digest (`digest.default_digest_id`); seeded to True and the default digest (`models/res_config_settings.py`, `data/res_config_settings_data.xml`, noupdate).
8. Default digest record: daily, admin as recipient, both base KPIs on, next date = install date (noupdate). Seven seed tips, all group = internal user, tips data is updatable (noupdate=0).

### 2.3 Business rules / states / lifecycle / exceptions
9. Lifecycle: activated ↔ deactivated via explicit actions; only activated digests are picked by the scheduler.
10. Scheduling: on create, next date computed if absent; periodicity change recomputes next date (onchange). Next date = today + 1 day / 1 week / 1 month / 3 months.
11. Scheduled send: selects activated digests with next date ≤ today; per digest, mail-delivery failures are logged and skipped (digest remains due); other exception types are not caught in the loop (`_cron_send_digest_email`).
12. Automatic slowdown (anti-spam): for scheduled sends only, if no recipient has a login log within the periodicity window (2 days / 7 days / 1 month / 3 months), periodicity is escalated one step (daily→weekly→monthly→quarterly, capped at quarterly) and the email carries a notice. Manual "Send Now" skips this check (`_check_daily_logs`, `_get_next_periodicity`, `action_send_manual`).
13. Manual send also advances next date (shared send routine).
14. Per-recipient rendering: body rendered in recipient language; KPIs, tips and preferences computed per recipient; email queued via elevated create as outgoing, auto-delete, subject = company name + digest name; sender = digest company email, else current user, else root user.
15. KPI computation: three columns — last 24 h, last 7 days, last 30 days — each compared against the equivalent preceding window to produce a percentage margin (zero if either value is zero or equal). Timeframe anchor localized to the company's working-calendar timezone when set (`_compute_timeframes`, `_get_margin_value`).
16. KPI evaluation runs as the recipient user and under the recipient's company; if the recipient lacks access to a KPI's underlying data (access error), that KPI is silently omitted from that recipient's email (`_compute_kpis`).
17. Generic company-based KPI helper: counts or sums records in a date window, filtered by the digest's company (or current company if none), grouped by company; the users model is filtered by its multi-company field (`_calculate_company_based_kpi`, `_get_company_field`). The messages-sent KPI is NOT company-filtered (counts comment-type messages globally in the window).
18. Currency/float formatting of KPI values uses the company currency symbol and position.
19. Tips: per send, picks up to N (1) tips not yet received by the user, whose group is among the user's groups or unset; rendered via template engine (elevated) then HTML-sanitized; the tip is marked consumed for that user.
20. Preferences block: slowdown notice, or (for daily digests to ERP managers) a switch-to-weekly link; ERP managers also get a customize link.
21. KPI action links: extension hook returns none in base; downstream modules may map KPIs to actions.
22. Auto-subscription: on user creation, internal (non-share) users are added to the configured default digest when the setting is enabled (`models/res_users.py`).
23. Subscribe/unsubscribe actions apply only to internal users acting on themselves; membership writes use elevated rights.

### 2.4 Unsubscribe
24. Email includes RFC 8058-style one-click unsubscribe headers pointing to a POST-only, CSRF-exempt route (rationale in source: mail user agent has no session). Token = HMAC over (digest id, user id) with a fixed scope; compared in constant time; mismatch → not found (`_get_unsubscribe_token`, `controllers/portal.py`).
25. Legacy unsubscribe route (GET/POST): without token/user id, works only for a logged-in internal user unsubscribing themselves; deprecated one-click flag forces POST.

### 2.5 Jobs / config
26. Cron "Digest Emails": daily interval, runs as root, first call ~2 h after install, forcecreate (`data/ir_cron_data.xml`).
27. Config params: `digest.default_digest_emails`, `digest.default_digest_id`.

### 2.6 Security
28. ACL: ERP manager (`base.group_erp_manager`) full CRUD on digests and tips; internal users read-only on both (`security/ir.model.access.csv`).
29. No record rules shipped → no multi-company isolation of digest or tip records themselves; company scoping exists only in KPI computation (finding 17) and the recipient-context evaluation (finding 16). RISK: digests of other companies readable by any internal user (subject to UI menu visibility only).
30. Form buttons (Send Now, Activate, Deactivate) and recipient/KPI sections are shown only to `base.group_system`; menus limited to ERP manager. ACL layer and UI layer use different groups (ERP manager vs system) — noted, not a contradiction by itself.
31. `/digest/<id>/set_periodicity`: authenticated, requires ERP manager, validates the periodicity value, changes state via a GET-reachable link embedded in email. RISK: state change on GET (CSRF exposure is framework-dependent; not verified).
32. Tip HTML is stored unsanitized and rendered as a template with elevated rights before sanitization; editable by ERP managers. RISK: template-evaluation surface for privileged editors.
33. Cron runs as root but KPI values are computed with the recipient's rights (finding 16).

### 2.7 UI surfaces (names only)
34. Backend: Digest list/form/search (default filter: activated), Digest Tips list/form/search; menus "Digest Emails" and "Digest Tips" under the email settings technical menu, ERP-manager only. Settings block "Digest Email" in the mail settings form.
35. Public/portal: `/digest/<id>/unsubscribe_oneclik`, `/digest/<id>/unsubscribe`, `/digest/<id>/set_periodicity`; confirmation page "Digest Subscriptions".
36. Email templates: main body, layout wrapper, mobile section, KPI cell sub-template (`data/digest_data.xml`).

## 3. Cross-module edges
- `mail`: message model (KPI source), mail rendering mixin, outgoing mail queue, mail-comment subtype, mail settings form inheritance.
- `portal`: portal layout for the unsubscribe page.
- `resource`: company working calendar timezone for KPI windows.
- `base`: users (login date, multi-company field, share flag, groups), user login log (slowdown), companies/currency, config params, cron, HMAC helper.
- Extension surface for other apps: new KPI toggle/value pairs and KPI→action mapping (consumers not in this module).
- No direct edge to `bus` observed.

## 4. Evidence gaps / contradictions
- G1: Email template bodies (digest_data.xml) read by structure only, not line-by-line.
- G2: Downstream KPI contributors (sales, CRM, accounting, etc.) not in scope; their company scoping unknown.
- G3: Whether `set_periodicity` GET is CSRF-protected by framework defaults is not evidenced in this module.
- G4: Observation: default recipient domain restricts internal users only in the UI domain; no server-side constraint preventing share users as recipients (auto-subscribe filters share users). Evidence-only.
- G5: Observation: messages-sent KPI lacks the company filter used by other KPIs — potential cross-company aggregation; source-visible, runtime unverified.
- No contradictions found.

## 5. Limitations
- Source presence ≠ runtime reachability; no runtime proof; no Formal Coverage claim; no percentages.
- Clean-room: neutral WHAT/WHY/RISK only; identifiers are pointers, not design recommendations.
- Single anchor commit; JS not applicable/not reviewed.
