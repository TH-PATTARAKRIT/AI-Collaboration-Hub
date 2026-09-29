# Source Map (candidate) — `gamification`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `gamification` |
| Display name | Gamification |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3e9e8a61e4e2b15a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/gamification/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail`
- Direct dependents in 300-module list (4): `gamification_sale_crm`, `hr_gamification`, `survey`, `website_profile`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / —
- Inventory of user-facing artifacts (counts): menu items 7, views 26, window actions 10, server actions 0, reports 0, mail templates 4, scheduled jobs 2, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (10): `gamification.badge.user.wizard` (Gamification User Badge Wizard); `gamification.goal.wizard` (Gamification Goal Wizard); `gamification.challenge` (Gamification Challenge); `gamification.goal.definition` (Gamification Goal Definition); `gamification.badge.user` (Gamification User Badge); `gamification.karma.rank` (Rank based on karma); `gamification.karma.tracking` (Track Karma Changes); `gamification.badge` (Gamification Badge); `gamification.challenge.line` (Gamification generic goal for challenge); `gamification.goal` (Gamification Goal)
- Objects extended from other modules (3): `mail.thread`, `image.mixin`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `gamification.badge.user.wizard` ← Community: `hr_gamification`; open-license custom/third-party scanned: —
- `gamification.challenge` ← Community: `survey`, `website_forum`, `website_slides`; open-license custom/third-party scanned: —
- `gamification.badge.user` ← Community: `hr_gamification`; open-license custom/third-party scanned: —
- `gamification.karma.tracking` ← Community: `website_forum`, `website_slides`; open-license custom/third-party scanned: —
- `gamification.badge` ← Community: `hr_gamification`, `survey`, `website_profile`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.thread`, `image.mixin`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: `gamification.challenge` → ['draft', 'inprogress', 'done']; `gamification.goal` → ['draft', 'inprogress', 'reached', 'failed', 'canceled']
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Gamification: Goal Challenge Check every 1 days; Gamification: Karma tracking consolidation every 1 months
- Security: groups declared 0 (—); record rules 3 (of which company-scoped by text 1); access rows 28

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 59 of 59 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — gamification
Source revision: 19.0.post20260921 | Module: "Gamification" v1.0, category Human Resources, LGPL-3 (gamification/__manifest__.py:4-7,53). Basis: static reading of models, security, cron, wizards, seed data; test names read (TEST).

## A. Capabilities and optionality
- A1. Motivation toolkit for users in three parts: goals set through challenges (numeric or done/not-done), badges granted by peers or by challenge results, and a "karma" points system with named ranks. gamification/__manifest__.py:9-19; gamification/models/gamification_challenge.py:49-58; gamification/models/gamification_badge.py:14-25; gamification/models/res_users.py:11-18
- A2. Optionality: no auto_install and no settings switch; depends on mail. It is installed on its own or as a dependency of other apps (survey, website_profile) and is the parent of auto-installed bridges hr_gamification and gamification_sale_crm. gamification/__manifest__.py:8; survey/__manifest__.py, website_profile/__manifest__.py (dependency listed); hr_gamification/__manifest__.py:21; gamification_sale_crm/__manifest__.py:11
- A3. Back-office screens live under Settings > Gamification Tools and are visible only in developer mode. gamification/views/gamification_menus.xml:4-7
- A4. Seed content: four badges (one inactive, "no one can grant"), two onboarding challenges ("Complete your Profile", "Setup your Company"), four goal definitions, five ranks with thresholds 1 / 100 / 500 / 2000 / 10000 karma, and preset 2500 karma for the root and admin users. gamification/data/gamification_badge_data.xml:4-30; gamification/data/gamification_challenge_data.xml:5-62; gamification/data/gamification_karma_rank_data.xml:4-13,25-77

## B. Objects, relationships, lifecycle
- B1. Goal definition (rule for measuring): manual entry, count of records, sum of a field, or a code snippet; done/not-done or progressive display; "higher is better" or "lower is better"; optional filter, date field, batch mode, action link. gamification/models/gamification_goal_definition.py:25-63
- B2. Challenge: name, responsible user, participants (fixed list and/or a user-filter that is re-evaluated), period (once, daily, weekly, monthly, yearly), start/end dates, lines (definition + target), rewards, report frequency and template, display mode (personal or ranking). gamification/models/gamification_challenge.py:76-145
- B3. Challenge lifecycle: Draft -> In Progress -> Done. Starting adds participants from the filter and creates one goal per line per participant; finishing triggers rewards; going back to Draft is refused while goals are unfinished. gamification/models/gamification_challenge.py:204-226,330-332,360-433
- B4. Goal: one user, one definition, one period; states draft, in progress, reached, failed, cancelled; reached when current value meets target, failed when end date passes unmet; a started goal cannot change its definition or user. gamification/models/gamification_goal.py:38-44,116-133,291-293
- B5. Manual goals: user updates the value through a small form; if not updated for the challenge's delay, a reminder is sent once. gamification/models/gamification_goal.py:91-114,324-335; gamification/wizard/update_goal.py:15-23
- B6. Badge: name, image, level (bronze/silver/gold), grant rule (everyone, selected users, holders of other badges, nobody), optional monthly per-person send cap. Granted instance records who, sender, comment and originating challenge. gamification/models/gamification_badge.py:30-51; gamification/models/gamification_badge_user.py:15-20
- B7. Karma: each user has a points total and a history of changes (old value, new value, reason, source). Total is recomputed from the latest history entry; rank and next rank are updated and a "new rank" email is queued when rank changes (not during installation). gamification/models/res_users.py:20-45,263-275; gamification/models/gamification_karma_tracking.py:19-34
- B8. Rank: name, description, required karma; changing thresholds recomputes affected users. gamification/models/gamification_karma_rank.py:18-59

## C. Validations, automation, security
- C1. Goal definition of type count/sum must have a valid filter and a stored field; checked on save. gamification/models/gamification_goal_definition.py:77-121,123-140
- C2. Rank threshold must be greater than 0. gamification/models/gamification_karma_rank.py:23-26
- C3. Badge granting rules enforced on every badge creation: "nobody" refuses, selected-users list, required-badges, monthly cap; administrators bypass. A user cannot grant a badge to themselves via the wizard. gamification/models/gamification_badge.py:176-218; gamification/models/gamification_badge_user.py:55-59; gamification/wizard/grant_badge.py:22-24
- C4. Daily job "Goal Challenge Check": starts draft challenges whose start date arrived, closes running ones past end date, updates goals, creates missing goals, sends due reports, checks rewards. Only goals of users who were recently present in the web client (session window) are recomputed. gamification/data/ir_cron_data.xml:4-11; gamification/models/gamification_challenge.py:232-313
- C5. Monthly job "Karma tracking consolidation": merges karma history entries from two months back into one entry per user, losing per-entry source and reason. gamification/data/ir_cron_data.xml:13-22; gamification/models/gamification_karma_tracking.py:70-83
- C6. Rewards: for a challenge with a badge for every succeeder, users who reached all goals get it once (real-time option) or at period end; first/second/third place badges at end; optionally also rewards best performers who did not succeed. gamification/models/gamification_challenge.py:654-745,747-802
- C7. Access: everyone internal reads definitions, challenges, badges; ERP managers have full control; employees may update goals they can see and create/edit badge-grant records; portal/public have read on badges and ranks (portal can also write goals and badge grants). gamification/security/ir.model.access.csv:3-32
- C8. Record rules on goals: users see their own goals plus goals of challenges they participate in that use ranking display; managers see all; a multi-company rule limits goals to users of allowed companies. gamification/security/gamification_security.xml:3-34
- C9. Karma history is hidden from everyone except system administrators (no rights for others). gamification/security/ir.model.access.csv:33-34; gamification/models/res_users.py:12
- C10. Code-based goal definitions execute stored code with restricted evaluation; only managers can create definitions. gamification/models/gamification_goal.py:152-168; gamification/security/ir.model.access.csv:8
- C11. Emails: badge-received, goal reminder, progress report, new-rank templates. gamification/data/mail_template_data.xml:4,87,108,308. Outgoing mail server required for delivery (mail).
- C12. (TEST) challenge join, reach, filtering of goals updated, sum-based goals, ranking report, badge granting; karma ranking, gain calculation, consolidation, rank switching. gamification/tests/test_challenge.py:32-284; gamification/tests/test_karma_tracking.py:53-437

## D. Handoffs
- D1. Karma awarders: website_slides (courses), website_forum (posts/votes). website_slides/models/slide_slide.py; website_forum/models/forum_post.py; website_forum/models/forum_post_vote.py (calls to add-karma).
- D2. Surveys: certification badges and challenge/goal creation from surveys: survey. survey/models/survey_survey.py:144,1235-1247; survey/models/challenge.py:8; survey/models/badge.py:8
- D3. Public profile / leaderboards using karma ranking helpers: website_profile. gamification/models/res_users.py:126-160 (helpers); website_profile/__manifest__.py (dependency listed).
- D4. HR badge sending from employee records: hr_gamification. CRM-based goal definitions: gamification_sale_crm. (module names only from manifests: hr_gamification/__manifest__.py:4; gamification_sale_crm/__manifest__.py:4)
- D5. Discuss channel for report copies: mail. gamification/models/gamification_challenge.py:134

## E. Configuration that changes outcomes
- E1. Challenge: period, dates, participant filter (default: all active internal users), reward settings, real-time reward flag, report frequency, reminder delay. gamification/models/gamification_challenge.py:68-73,92-137
- E2. Definition: computation mode, direction (higher/lower), domain, batch mode. gamification/models/gamification_goal_definition.py:25-61
- E3. Badge: grant rule and monthly cap. gamification/models/gamification_badge.py:34-51
- E4. Rank thresholds. gamification/data/gamification_karma_rank_data.xml:25-77

## F. Extension path
- survey, website_profile, website_slides, website_forum, hr_gamification, gamification_sale_crm.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: content of hr_gamification and gamification_sale_crm (only manifest names read).
- UNKNOWN — EVIDENCE INSUFFICIENT: exact effect of the "presence" filter when presence tracking is unavailable (bus/mail presence tables owned by mail).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end board widgets (static assets not read).

