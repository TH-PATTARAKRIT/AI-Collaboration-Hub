# Source Map (candidate) — `website_profile`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_profile` |
| Display name | Website profile |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `038feeaa0e6143ee` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_profile/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `html_editor`, `website_partner`, `gamification`
- Direct dependents in 300-module list (2): `website_forum`, `website_slides`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_event_track_quiz`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Access the website profile of the users
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 0, web routes 8
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `res.users`, `gamification.badge`, `website.published.mixin`, `website`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`, `gamification.badge`, `website.published.mixin`, `website`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 42 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_profile (Website profile)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_profile.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: lets users have a public web profile showing statistics such as karma and badges (website_profile/__manifest__.py:8-9).

## A. Capabilities / functions
- Optional base for community features: depends on html_editor, website_partner and gamification; no `auto_install` (website_profile/__manifest__.py:10-14). Pulled in by website_forum and website_slides (their manifests list it).
- Core: public profile page per user `/profile/user/<id>` with an access check, back-link label when arriving from forum or courses (website_profile/controllers/main.py:41-60, 99-124).
- Core: profile editing (name, website, email, city, country, description, picture and publish flag) by the user; a system administrator can edit another user's profile (website_profile/controllers/main.py:128-156).
- Core: leaderboard `/profile/users` (30 per page) ranking published users with karma above 1, by total karma or by karma gained in the last week or month, with the viewer's own position if outside the page (website_profile/controllers/main.py:197-293); (TEST) paging by period (website_profile/tests/test_website_profile.py:51-104).
- Core: "Ranks and Badges" page listing published badges and ranks; badges filterable by challenge category (website_profile/controllers/main.py:160-193).
- Core: avatar route that shows a user's picture publicly only for published users with karma above 0 (website_profile/controllers/main.py:29-39, 83-97).
- Core: email validation for the profile: sends a validation link; opening it gives 3 karma if the user had none (website_profile/controllers/main.py:319-338; website_profile/models/res_users.py:11, 43-65).
- Core: badges can be published on the website (website_profile/models/gamification_badge.py:8-9; website_profile/views/gamification_badge_views.xml:3-14). Website form has a setting for minimum karma to view other profiles (website_profile/models/website.py:10; website_profile/views/website_views.xml:4-13).
- Portal: changing one's own email in the address form resets the "validation email sent" indicator (website_profile/controllers/portal.py:10-19).
- Restricted website editors may manage karma ranks (website_profile/security/ir.model.access.csv:2).

## B. Business objects, relationships, lifecycle
- User (res.users, base) with karma, rank, next rank (owned by gamification), badges (gamification), plus website fields (published, description, city, country, website) from the contact record (website_partner) (website_profile/models/res_users.py:18-25).
- Lifecycle: registered user with 0 karma -> validates email (+3 karma) -> can appear on the leaderboard once karma exceeds 1 and profile is published -> earns karma through forum or course activity (owned by those modules) -> ranks and badges granted by gamification.
- The publish flag is the user's own privacy switch and is only settable on one's own profile via the profile form (website_profile/controllers/main.py:141-142).
- Email validation link token is valid only for the current day and is bound to user id and email; secret stored as a system parameter created on first use (website_profile/models/res_users.py:27-41).

## C. Validations, automation, security, multi-company
- Profile visibility: own profile always visible; else the profile must be published, and the viewer's karma must reach the website's minimum (default 150); otherwise an "access denied" page with a reason (website_profile/controllers/main.py:47-60; website_profile/models/website.py:10). Order of checks means an unpublished, non-existing id shows "private" before not-found (website_profile/controllers/main.py:53-56).
- Editing: only whitelisted self-editable fields are written; country cannot be changed once documents were issued for the account (website_profile/controllers/main.py:153-156). Self-writable fields include country, city, website, description, published flag (website_profile/models/res_users.py:22-25); self-readable adds karma (website_profile/models/res_users.py:18-19).
- Only a full administrator may save another user's profile; other users always save their own (website_profile/controllers/main.py:147-151).
- Avatar route only serves four image field names, else forbidden; sudo only if published and karma above 0 (website_profile/controllers/main.py:87-97).
- Public/other listing exposes: name, company name, rank, karma, badge count, published flag for published users only (website_profile/controllers/main.py:197-215).
- Validation email: public link route; any valid token for the day works; karma bonus only if karma is exactly zero (website_profile/controllers/main.py:326-332; website_profile/models/res_users.py:63-64). Sending requires a logged-in non-public user and an email on the account (website_profile/controllers/main.py:319-324; website_profile/models/res_users.py:44-45).
- Elevated reads: user, rank, badge and karma queries run with elevated rights on public pages (website_profile/controllers/main.py:34, 47, 173-176, 227, 254). Multi-company effect on cross-company users: UNKNOWN — EVIDENCE INSUFFICIENT.
- Website scoping: the karma threshold is per website record; user publication is global to the contact (website_profile/models/website.py:10). Company scoping: none in this module.

## D. Handoffs to other modules
- gamification (owner): karma, ranks, badges, challenges, karma tracking. website_partner: contact publication and description. website: layout, pager, public user check. portal: address/portal form (website_profile/controllers/portal.py:5). mail: validation email template (website_profile/data/mail_template_data.xml:6-9).
- website_forum and website_slides: award karma and reuse this profile (their notes). hr_gamification and survey also extend badges.

## E. Configuration / defaults that change outcomes
- Minimum karma to see others' profiles: 150 by default per website (website_profile/models/website.py:10).
- Validation bonus: 3 karma (website_profile/models/res_users.py:11).
- Leaderboard threshold karma above 1, page size 30, pager shows up to 5 pages (website_profile/controllers/main.py:23-24, 215).
- Badge visibility on the public page requires the badge to be published (website_profile/controllers/main.py:164).

## F. Effective extension path (module names only)
- res.users: many modules; in this family gamification, hr_gamification, website, website_forum, website_profile, website_slides. gamification.badge: hr_gamification, survey, website_profile. Controller hook methods (badge domain, profile values, user values) are meant for website_forum and website_slides (website_profile/controllers/main.py:62-81, 160-167).

## G. Not verified
- Karma rank thresholds and badge granting rules: UNKNOWN — EVIDENCE INSUFFICIENT (gamification).
- Cache/CDN behaviour for avatars: UNKNOWN — EVIDENCE INSUFFICIENT.

