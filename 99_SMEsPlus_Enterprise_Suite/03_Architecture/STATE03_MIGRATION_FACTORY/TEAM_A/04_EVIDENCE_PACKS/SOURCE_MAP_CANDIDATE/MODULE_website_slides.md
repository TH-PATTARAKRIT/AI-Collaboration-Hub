# Source Map (candidate) — `website_slides`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_slides` |
| Display name | eLearning |
| Manifest version | 2.7 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f9f6740eaeb2eeee` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_slides/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `portal_rating`, `website`, `website_mail`, `website_profile`
- Direct dependents in 300-module list (3): `hr_skills_slides`, `website_slides_forum`, `website_slides_survey`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `mass_mailing_slides`, `test_discuss_full`, `test_website_modules`, `website_sale_slides`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/eLearning / Manage and publish an eLearning platform
- Inventory of user-facing artifacts (counts): menu items 15, views 50, window actions 16, server actions 0, reports 0, mail templates 6, scheduled jobs 0, wizards 3, web routes 39
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `slide.channel.invite` (Channel Invitation Wizard); `slide.embed` (Embedded Slides View Counter); `slide.slide` (Slides); `slide.channel` (Course); `slide.question` (Content Quiz Question); `slide.answer` (Slide Question's Answer); `slide.tag` (Slide Tag); `slide.channel.partner` (Channel / Partners (Members)); `slide.slide.partner` (Slide / Partner decorated m2m); `slide.slide.resource` (Additional resource for a particular slide); `slide.channel.tag.group` (Channel/Course Groups); `slide.channel.tag` (Channel/Course Tag)
- Objects extended from other modules (20): `mail.composer.mixin`, `base.partner.merge.automatic.wizard`, `gamification.challenge`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`, `rating.mixin`, `mail.activity.mixin`, `website.cover_properties.mixin`, `website.published.multi.mixin`, `res.groups`, `gamification.karma.tracking`, `mail.activity`, `res.users`, `res.config.settings`, `website`, `mail.message`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `slide.slide` ← Community: `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.channel` ← Community: `hr_skills_slides`, `mass_mailing_slides`, `website_sale_slides`, `website_slides_forum`, `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.channel.partner` ← Community: `hr_skills_slides`, `website_slides_survey`; open-license custom/third-party scanned: —
- `slide.slide.partner` ← Community: `website_slides_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `base.partner.merge.automatic.wizard`, `gamification.challenge`, `mail.thread`, `image.mixin`, `website.seo.metadata`, `website.published.mixin`, `website.searchable.mixin`, `rating.mixin`, `mail.activity.mixin`, `website.cover_properties.mixin`, `website.published.multi.mixin`, `res.groups`, `gamification.karma.tracking`, `mail.activity`, `res.users`, `res.config.settings`, `website`, `mail.message`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 9 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 5 (`group_website_slides_officer`, `group_website_slides_manager`, `website_slides.group_website_slides_officer`, `website_slides.group_website_slides_manager`, `base.default_user_group`); record rules 21 (of which company-scoped by text 0); access rows 41

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 69 of 70 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_slides (eLearning)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_slides.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: manage and publish an eLearning platform with courses, lessons, quizzes, tags, statistics (website_slides/__manifest__.py:5, 9-20).

## A. Capabilities / functions
- Optional application: depends on portal_rating, website, website_mail and website_profile; `application: True`, no `auto_install` (website_slides/__manifest__.py:22-27, 69). Settings toggles install the optional companions: certifications (website_slides_survey), paid courses (website_sale_slides), mass mailing (mass_mailing_slides), forum (website_slides_forum) and a Google Docs key for external documents (website_slides/views/res_config_settings_views.xml:12-27; website_slides/models/website.py:10).
- Core: courses (training or documentation type) with sections and lessons (image, article, document/PDF/sheet/slides, video from device, YouTube, Vimeo or Google Drive, quiz), tags and tag groups, cover, description, promoted content strategy (latest, most voted, most viewed, manual, none) (website_slides/models/slide_channel.py:61-94; website_slides/models/slide_slide.py:88-143).
- Core: public catalogue `/slides` with search, tag filters, "my courses", top learners; course pages with reviews; lesson pages, fullscreen player, embed pages for third-party sites with view counting (website_slides/controllers/main.py:405-715, 973-1060, 1515-1560; website_slides/models/slide_embed.py).
- Core: enrolment policies (open or by invitation), course visibility (everyone, signed-in, attendees only, anyone with link), auto-enrol by user group, prerequisite courses, access requests to the course responsible (website_slides/models/slide_channel.py:127-146, 193-201, 657-700, 871-930).
- Core: attendee tracking: per-course membership with status (invited, joined, ongoing, completed), completion percentage and completed count, per-lesson progress with vote and quiz attempts (website_slides/models/slide_channel_partner.py:13-33, 88-138; website_slides/models/slide_slide_partner.py:10-24).
- Core: quizzes on lessons with question/answers; reward karma by attempt number (10 / 7 / 5 / 2 by default) and course completion karma (10) and ranking (5) (website_slides/models/slide_slide.py:79-82; website_slides/models/slide_channel.py:183-191; website_slides/models/slide_question.py).
- Core: additional downloadable resources per lesson visible to attendees (website_slides/models/slide_slide_resource.py:11-32; website_slides/security/website_slides_security.xml:240-249).
- Core: invitation and enrol wizard (email to selected contacts) with 3-month invitation validity; completion email; publication notification to followers; sharing emails (website_slides/wizard/slide_channel_invite.py:15-117; website_slides/models/slide_channel_partner.py:185-242; website_slides/models/slide_slide.py:736-756; website_slides/data/mail_template_data.xml:4-158).
- Backend: menus for courses, lessons, attendees, reporting, ratings, partner course counts and statistics (website_slides/views/website_slides_menu_views.xml; website_slides/models/res_partner.py:8-80).
- Gamification: seeded badges and challenges (Get started, Know yourself, Power User and others) and a challenge category for slides (website_slides/data/gamification_data.xml:5-97; website_slides/models/gamification_challenge.py:7-12).

## B. Business objects, relationships, lifecycle
- Course (slide.channel) 1..n lessons/sections (slide.slide), lesson 0..n quiz questions -> answers, 0..n resources, 0..n embeds; attendee membership (slide.channel.partner) and lesson progress (slide.slide.partner) link contact to course/lesson (website_slides/models/slide_channel.py:77-82, 149-154; website_slides/models/slide_slide.py:63-77, 103; website_slides/models/slide_channel_partner.py:13-33).
- Lesson lifecycle: created (publish date set only if creator may publish) -> published (followers notified using the course's template; completion of members recomputed) -> archived (unpublished) (website_slides/models/slide_slide.py:565-642, 736-756). Publishing rights: for training courses only the course responsible (or managers); documentation courses also upload groups (website_slides/models/slide_channel.py:377-405).
- Membership lifecycle: invited (accepted within 3 months or purged) -> joined -> ongoing -> completed; leaving archives the membership and keeps earned karma; re-joining unarchives and recomputes (website_slides/models/slide_channel.py:694-834; website_slides/models/slide_channel_partner.py:88-138, 243-257).
- Completion: computed from completed published active lessons; reaching 100 percent sets "completed", sends the completion email and grants course-finish karma; falling below removes it again (website_slides/models/slide_channel_partner.py:88-138, 161-183).
- Lesson completion rules: quiz lessons complete only by passing the quiz; "training" course lessons open by a member are auto-completed except videos; members may mark/unmark others when permitted (website_slides/controllers/main.py:95-106, 973-990; website_slides/models/slide_slide.py:838-877). Quiz karma removed when un-completing (website_slides/models/slide_slide.py:878-914).
- Archiving a course archives lessons and unpublishes it; unarchiving restores lessons (website_slides/models/slide_channel.py:553-581).

## C. Validations, automation, security, multi-company
- Database checks: visibility "attendees only" requires enrol "on invitation"; membership unique per course/contact and lesson/contact; completion between 0 and 100; vote among -1/0/1; a lesson has either external URL or HTML, not both; resource link/file consistency (website_slides/models/slide_channel.py:203-212; website_slides/models/slide_channel_partner.py:35-42; website_slides/models/slide_slide_partner.py:20-27; website_slides/models/slide_slide.py:174-178; website_slides/models/slide_slide_resource.py:25-32). Each quiz question needs at least one correct and one incorrect answer (website_slides/models/slide_question.py:24-35).
- Contact merge blocked if several merged contacts are enrolled in the same course (website_slides/models/base_partner_merge.py:11-24); (TEST) (website_slides/tests/test_slide_channel.py:165).
- Groups: eLearning Officer implies website restricted editor; Manager implies Officer (website_slides/security/website_slides_security.xml:9-22). Access rows: public/portal/internal read courses, lessons, questions, tags; officers edit their own courses' content (create/write without delete on courses); managers full; membership and progress tables have no default access (officers/managers only) (website_slides/security/ir.model.access.csv:2-42). Record rules: public sees only published public/link-based courses and their category or previewable lessons; signed-in users see published courses that are public/signed-in/link-based, or where they are attendee or invited (lesson rule is similar); officers read all but edit only courses they are responsible for; managers everything; resources readable by attendees (website_slides/security/website_slides_security.xml:26-104, 113-158, 240-282). (TEST) many access scenarios: invite, public, members-only, connected, preview, publish, resource, field access (website_slides/tests/test_security.py:18-575).
- Invitation links use a signed hash of contact and course; invalid, missing or 3-month-old pending invitations are refused; logged-in user must match the invited contact; unlogged invited partners are sent to sign-up/login or to a course preview (website_slides/controllers/main.py:718-748, 803-873; website_slides/models/slide_channel_partner.py:155-159). (TEST) (website_slides/tests/test_attendee.py:485-570).
- Join: public users get an error with hint whether self sign-up exists; invited members on invite-only courses may enrol themselves; other joins require the course to be open (website_slides/controllers/main.py:875-887; website_slides/models/slide_channel.py:760-767). Leave: membership archived (website_slides/controllers/main.py:889-894).
- Likes, comments and reviews need membership and enough karma (course-level thresholds: review 10, comment 3, vote 3) and are blocked if comments are disabled (website_slides/controllers/main.py:1113-1140; website_slides/models/slide_channel.py:186-191, 442-458).
- Quiz submit requires login and all questions answered; wrong answers give attempt increments without completion; success completes the lesson and returns rank progress (website_slides/controllers/main.py:1265-1315).
- Non-members' lesson views increase public view counters once per session (website_slides/controllers/main.py:72-93).
- Elevated operations are used for membership creation, karma and progress writes after access checks (website_slides/models/slide_channel.py:694-758; website_slides/models/slide_slide.py:786-914).
- Website scoping: courses belong optionally to a website; lesson pages check the current website (website_slides/controllers/main.py:975-977). Company scoping: none by evidence.

## D. Handoffs to other modules
- website_profile (profiles, karma, ranks, leaderboard; controller subclassed) (website_slides/controllers/main.py:33); gamification (karma, badges, challenges); portal_rating (reviews); website_mail (follow); mail (activities for access requests, templates, followers); res.users/res.groups hooks for auto-enrol (website_slides/models/res_users.py:8-36; website_slides/models/res_groups.py:8-16).
- Optional companions: website_slides_survey (certifications), website_slides_forum (forums), website_sale_slides (selling courses), mass_mailing_slides, hr_skills_slides (skills from courses).

## E. Configuration / defaults that change outcomes
- Course fields: visibility, enrol policy, upload groups, auto-enrol groups, prerequisite courses (must share visibility and publication state), templates for publish/share/completion, karma thresholds and gains (website_slides/models/slide_channel.py:107-146, 183-201).
- Lesson fields: preview flag (unpublished visibility on public course), completion time (auto for PDFs), downloadable flag, quiz rewards (website_slides/models/slide_slide.py:57-59, 79-82, 104).
- Invitation validity 3 months; view counting per session; catalogue page size 12 (website_slides/models/slide_channel_partner.py:243-257; website_slides/controllers/main.py:429).
- Google Docs key on the website record, visible only to system administrators (website_slides/models/website.py:10).

## F. Effective extension path (module names only)
- slide.channel: hr_skills_slides, mass_mailing_slides, website_sale_slides, website_slides_forum, website_slides_survey. slide.channel.partner: hr_skills_slides, website_slides_survey. slide.slide and slide.slide.partner: website_slides_survey. Controller WebsiteSlides subclassed by: website_slides_forum, website_slides_survey. res.users: website_forum, website_profile, website_slides and others.

## G. Not verified
- Payment/sale of courses: UNKNOWN — EVIDENCE INSUFFICIENT (website_sale_slides, not traced).
- External metadata fetching from YouTube, Vimeo and Google Drive (network behaviour, error handling): UNKNOWN — EVIDENCE INSUFFICIENT.
- Details of statistics reporting screens: UNKNOWN — EVIDENCE INSUFFICIENT.

