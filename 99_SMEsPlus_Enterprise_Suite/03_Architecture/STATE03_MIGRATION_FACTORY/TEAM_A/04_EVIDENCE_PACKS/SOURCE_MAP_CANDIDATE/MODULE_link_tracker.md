# Source Map (candidate) — `link_tracker`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `link_tracker` |
| Display name | Link Tracker |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `33383375069ceaa7` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/link_tracker/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `utm`, `mail`
- Direct dependents in 300-module list (1): `website_links`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `marketing_card`, `mass_mailing`, `pos_self_order`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing / —
- Inventory of user-facing artifacts (counts): menu items 1, views 10, window actions 3, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `link.tracker` (Link Tracker); `link.tracker.code` (Link Tracker Code); `link.tracker.click` (Link Tracker Click)
- Objects extended from other modules (3): `mail.render.mixin`, `utm.campaign`, `utm.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `link.tracker` ← Community: `mass_mailing`, `website_links`; open-license custom/third-party scanned: —
- `link.tracker.click` ← Community: `mass_mailing`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.render.mixin`, `utm.campaign`, `utm.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 40 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — link_tracker
Source revision: 19.0.post20260921 | Module: "Link Tracker" v1.1, category Marketing, LGPL-3 (link_tracker/__manifest__.py:5-6,10,18). Basis: static reading of models, controller, access file; test names read (TEST).

## A. Capabilities and optionality
- A1. Wraps any web address in a short tracked address of the form <base URL>/r/<code>, counts visits, and appends campaign, medium and source markers to the destination. link_tracker/__manifest__.py:8; link_tracker/models/link_tracker.py:99,131-144; link_tracker/controller/main.py:12-23
- A2. Provides a helper that rewrites every link in an HTML or plain-text message body into a tracked short link (skipping mail-to, phone and SMS links, already-shortened links, and caller-supplied exclusions). link_tracker/models/mail_render_mixin.py:24-62,65-91
- A3. Adds a "clicks" figure to marketing campaigns. link_tracker/models/utm.py:11-21
- A4. Optionality: no auto_install, no settings switch; depends on utm and mail. Installed as a dependency of mass_mailing, marketing_card, website_links, pos_self_order. link_tracker/__manifest__.py:11; mass_mailing/__manifest__.py:16; marketing_card/__manifest__.py:6; website_links/__manifest__.py:10; pos_self_order/__manifest__.py:7.
- A5. The tracker list is reachable from the UTM/Link Tracker menu only in developer mode. link_tracker/views/link_tracker_views.xml:194-198

## B. Objects, relationships, lifecycle
- B1. Tracked link: target address, optional button label, page title, campaign/medium/source, click count. If the campaign/medium/source is deleted the link keeps existing with that value cleared. link_tracker/models/link_tracker.py:38-53
- B2. Code: one or more short codes per link, globally unique; new codes are random letters/digits, starting at 3 characters and growing when collisions occur. link_tracker/models/link_tracker.py:316-341
- B3. Click: one row per counted visit with link, IP address, country; campaign is copied from the link. link_tracker/models/link_tracker.py:344-374
- B4. Creation: a link cannot be created without an address; addresses starting with "?" or "#" are refused (would loop to the same page); address is normalized; title is fetched from the target page's preview, else the address itself; UTM values are NOT taken from visitor cookies. link_tracker/models/link_tracker.py:191-221. (TEST) loop rejection: link_tracker/tests/test_link_tracker.py:259-264
- B5. Reuse: "search or create" returns the existing link for the same combination, creating only missing ones. link_tracker/models/link_tracker.py:223-272
- B6. Visit lifecycle: public visit -> click recorded unless caller is a known bot/preview agent -> permanent (301) redirect; unknown code gives "not found". link_tracker/controller/main.py:14-23. (TEST) preview agents not counted, normal browser counted: link_tracker/tests/test_tracker_http_requests.py:8-47

## C. Validations, security, external effects
- C1. Uniqueness: the combination of address, campaign, medium, source and label must be unique (checked in code, blank label treated as none). link_tracker/models/link_tracker.py:154-189. (TEST) link_tracker/tests/test_link_tracker.py:145
- C2. Access: internal users read-only on links, codes, clicks; public none; administrators full. link_tracker/security/ir.model.access.csv:2-10. Creation by other apps runs with their own rights or elevated rights (code/click creation is elevated). link_tracker/models/link_tracker.py:214; link_tracker/controller/main.py:15
- C3. No record rules or company field on links/clicks: UNKNOWN — EVIDENCE INSUFFICIENT for company isolation (none defined in this module).
- C4. Privacy: each counted click stores visitor IP and country (geo lookup by server). link_tracker/controller/main.py:15-19; link_tracker/models/link_tracker.py:355-356
- C5. External effects: creating a link may fetch the target page to read its title (outbound request). link_tracker/models/link_tracker.py:146-152. Public route is open to anyone with the code.
- C6. Switch "no external tracking": when the system parameter link_tracker.no_external_tracking is set, campaign/medium/source markers are added only to addresses on the company's own site. link_tracker/models/link_tracker.py:118-129. (TEST) link_tracker/tests/test_link_tracker.py:200

## D. Handoffs
- D1. Campaign, medium, source owner: utm. link_tracker/models/link_tracker.py:35,349-353
- D2. Email body rewriting is offered on the mail rendering mixin (owner: mail); the mass-mailing app supplies its own extra link attributes. link_tracker/models/link_tracker.py:12; mass_mailing/__manifest__.py:16. SMS link shortening uses the plain-text helper from mass_mailing_sms: mass_mailing_sms/models/mailing_mailing.py:310; mass_mailing_sms/wizard/sms_composer.py:78.
- D3. Website short-link UI: website_links. Social/marketing cards: marketing_card. Loyalty coupon sharing and POS self-order reference the tracker: website_sale_loyalty/wizard/coupon_share.py:61-63; pos_self_order/models/pos_config.py:284.

## E. Configuration that changes outcomes
- E1. link_tracker.no_external_tracking (C6). link_tracker/models/link_tracker.py:122
- E2. Base URL (system web base URL) determines the short link host. link_tracker/models/link_tracker.py:99; link_tracker/models/mail_render_mixin.py:42

## F. Extension path
- mass_mailing, mass_mailing_sms, marketing_card, website_links, pos_self_order, website_sale_loyalty; utm (campaign figure).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how bot detection decides (delegated to http routing "is_a_bot", not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: retention/purge of click records (no cron found in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: statistics screens beyond names (view file only sampled).

