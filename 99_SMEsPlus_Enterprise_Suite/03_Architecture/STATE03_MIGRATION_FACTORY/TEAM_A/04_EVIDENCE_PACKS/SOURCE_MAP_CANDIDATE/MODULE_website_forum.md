# Source Map (candidate) — `website_forum`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_forum` |
| Display name | Forum |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b318318a84e7725b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_forum/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `auth_signup`, `website_mail`, `website_profile`
- Direct dependents in 300-module list (1): `website_slides_forum`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Manage a forum with FAQ and Q&A
- Inventory of user-facing artifacts (counts): menu items 7, views 14, window actions 7, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 40
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `forum.post.reason` (Post Closing Reason); `forum.post.vote` (Post Vote); `forum.forum` (Forum); `forum.post` (Forum Post); `forum.tag` (Forum Tag)
- Objects extended from other modules (10): `gamification.challenge`, `ir.attachment`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `gamification.karma.tracking`, `res.users`, `website`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `forum.forum` ← Community: `website_slides_forum`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `gamification.challenge`, `ir.attachment`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `gamification.karma.tracking`, `res.users`, `website`

## 6. Actions / states / validation / automation / security
- State fields found: `forum.post` → ['active', 'pending', 'close', 'offensive', 'flagged']
- Validation: 1 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 12 (of which company-scoped by text 0); access rows 15

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 63 of 64 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_forum (Forum)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_forum.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: a community Q&A / discussion forum with FAQ (website_forum/__manifest__.py:6-9).

## A. Capabilities / functions
- Optional app: depends on auth_signup, website_mail and website_profile; no `auto_install` (website_forum/__manifest__.py:11-15). Installing it sets the sign-up invitation scope to "customers can sign up themselves" (b2c) as a data default (website_forum/data/ir_config_parameter_data.xml:3).
- Core: forums (Questions mode: one accepted answer; Discussions mode: several answers), each with privacy (public, signed-in only, or restricted to one user group), guidelines/FAQ, welcome message, default ordering, relevance parameters, sharing option (website_forum/models/forum_forum.py:16-87).
- Core: posts = questions and their answers; tags per forum; votes; favourites; comments as chatter messages; view counter; closing reasons; moderation queues (validation, flagged, offensive, closed) (website_forum/models/forum_post.py:29-92; website_forum/controllers/website_forum.py:529-650).
- Core: reputation-driven permissions (karma): each forum defines the karma needed to ask, answer, edit own/all, retag, close, delete, upvote, downvote, accept, comment, convert, flag, post without validation, moderate, use editor features, show biography, plus karma gained/lost per event (website_forum/models/forum_forum.py:98-133; defaults at 98-133).
- Core: public pages: forum index and question lists with filters (all, unanswered, my, tag, sorting, search), tag list, FAQ and karma-rules page, question page with answers; sitemap and search integration (website_forum/controllers/website_forum.py:69-340; website_forum/models/website.py:34-42).
- Core: notification emails on new question, new answer, edits, and validation requests to moderators; tags can be followed (website_forum/models/forum_post.py:445-475; website_forum/data/mail_templates.xml:3-23; website_forum/data/mail_message_subtype_data.xml:5-40).
- Core: gamification badges for questions, answers, participation and moderation, and a "Forum" challenge category (website_forum/data/gamification_badge_data_question.xml; website_forum/data/gamification_badge_data_answer.xml; website_forum/data/gamification_badge_data_participation.xml; website_forum/data/gamification_badge_data_moderation.xml; website_forum/models/gamification_challenge.py:10-12).
- Seeds: a "Help" forum, closing reasons (13), a menu "Forum" on the website menu, FAQ template (website_forum/data/forum_forum_data.xml:4-9; website_forum/data/forum_post_reason_data.xml; website_forum/data/website_menu_data.xml:3-6).
- Extra: profile page extended with forum activity; per-forum website counter; footer link suggestion in the site configurator (website_forum/controllers/website_forum.py:664-800; website_forum/models/website.py:10, 23-32, 44-56).

## B. Business objects, relationships, lifecycle
- Forum -> posts (question -> answers via parent link) -> tags (per forum, unique name per forum), votes (one per user per post), favourites, comments (messages) (website_forum/models/forum_post.py:35, 61-79; website_forum/models/forum_tag.py:19-28; website_forum/models/forum_post_vote.py:19-22).
- Post states: active, pending validation, closed, offensive, flagged (website_forum/models/forum_post.py:36-41).
- Lifecycle of a question: created (active if the author has enough karma to post freely, else pending) -> validated by a moderator (karma granted for asking) or refused -> active -> may be flagged -> moderator marks offensive (inactive, author penalised) or closes with reason -> reopen (penalty reversed for spam/offensive) (website_forum/models/forum_post.py:311-337, 477-575, 577-592).
- Answer acceptance: only one accepted answer per question in controller flow; author of the answer gains karma, accepter gains karma, self-acceptance yields no karma (website_forum/controllers/website_forum.py:453-463; website_forum/models/forum_post.py:347-380).
- Voting adjusts the recipient's karma by the forum's per-event amounts, different for questions and answers; changes are computed as differences from the previous vote (website_forum/models/forum_post_vote.py:24-40, 100-115).
- Archiving a forum or post cascades to its posts/answers; changing forum privacy to public/signed-in clears the authorised group (website_forum/models/forum_forum.py:259-271; website_forum/models/forum_post.py:400-403).
- Deleting an accepted answer reverses the karma given (website_forum/models/forum_post.py:339-345).

## C. Validations, automation, security, multi-company
- Recursive post links prohibited (website_forum/models/forum_post.py:165-168). A vote is unique per post and user; voting on one's own post or another person's vote is refused; cast rights depend on karma (website_forum/models/forum_post_vote.py:79-98). (TEST) karma-access matrix for ask, answer, close, comment, delete, downvote, edit, flag, offensive, refuse, validate, vote (website_forum/tests/test_forum_karma_access.py:14-461).
- Answers cannot be posted on closed or deleted questions (website_forum/models/forum_post.py:323-324). Questions need karma to ask and answers need karma to answer, else access error (website_forum/models/forum_post.py:326-329).
- Content controls: users below the "dofollow" karma have links marked nofollow; users below the editor karma cannot post images or links (website_forum/models/forum_post.py:425-441).
- New tags need karma; otherwise ignored when submitted from a post; direct tag creation also needs karma unless administrator (website_forum/models/forum_forum.py:281-300; website_forum/models/forum_tag.py:40-46). Tag name unique per forum (website_forum/models/forum_tag.py:25-28).
- Users with pending question already waiting cannot ask another until it is handled (website_forum/controllers/website_forum.py:412-427). Posting requires a valid email on the account, else redirect to the profile page (website_forum/controllers/website_forum.py:403-410).
- Hidden posts: posts of negative-karma authors are hidden from everyone except users able to close them; pending posts are hidden (not found) for users below the free-posting karma unless they are the author (website_forum/models/forum_post.py:271-295, 146-148; website_forum/controllers/website_forum.py:325-331).
- Access rows: public read forums/posts/reasons; public may create tags; portal and internal users can create/edit posts and votes; only ERP managers get full forum rights (website_forum/security/ir.model.access.csv:2-16). Record rules: public sees only public forums, posts and tags; signed-in users see public and signed-in forums plus restricted forums of their authorised group; website designers can create forums; managers see all; users only see their own votes (website_forum/security/ir_rule_data.xml:4-86). Multi-website: forum has an optional website and a per-website forum count (website_forum/models/forum_forum.py:23; website_forum/models/website.py:44-56).
- Company scoping: none by evidence (no company field). Karma changes and moderation actions use elevated writes (website_forum/models/forum_post.py:331, 335, 359-376).
- Spam control: mass mark-as-offensive by creator, country, or post (website_forum/models/forum_post.py:594-605). Captcha on the follow modal is inherited from website_mail (website_forum/views/forum_templates_mail.xml:36).
- Attachment bypass: users able to use the full editor may attach images to posts (website_forum/models/ir_attachment.py:10-22).

## D. Handoffs to other modules
- website_profile (owner of profile pages, karma display, leaderboard); gamification (karma, badges, challenges, tracking origin option) (website_forum/models/gamification_karma_tracking.py:10-11); website_mail (follow); auth_signup (invitation scope); mail (chatter, subtypes); website (menu, search, SEO, multi-website).
- website_slides_forum links a course to a forum; website_slides uses the same karma/profile system.

## E. Configuration / defaults that change outcomes
- Per forum: mode, privacy, authorised group, all karma thresholds and gains listed at website_forum/models/forum_forum.py:98-133 (for example ask 3, answer 3, edit own 1, edit all 300, close own 100, close all 500, delete own 500, delete all 1000, upvote 5, downvote 50, post without validation 100, moderate 1000, flag 500, editor 30, dofollow 500).
- Relevance sort parameters 0.8 and 1.8; default order "last updated" (website_forum/models/forum_forum.py:75-83).
- Karma gains: ask +2, question upvote +5 / downvote -2, answer upvote +10 / downvote -2, accept +2, accepted +15, flagged -100 (website_forum/models/forum_forum.py:98-105).
- Sign-up scope set to self-service (website_forum/data/ir_config_parameter_data.xml:3).

## F. Effective extension path (module names only)
- res.users: website_forum, website_profile, website_slides and others. Profile controller hooks used here from website_profile. Forum content used by website_slides_forum. website extended (family) with website_forum in the list of website-extending modules. Tests exist for tours, performance, sitemap, editor (TEST) (website_forum/tests/test_forum_tours.py; website_forum/tests/test_performance.py; website_forum/tests/test_sitemap.py; website_forum/tests/test_web_editor.py).

## G. Not verified
- Exact email recipients and templates content on validation queue; badge grant thresholds: UNKNOWN — EVIDENCE INSUFFICIENT.
- Answer acceptance in Discussions mode behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.
- Retention/anonymisation of user contributions on account deletion: UNKNOWN — EVIDENCE INSUFFICIENT.

