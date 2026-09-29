# Source Map (candidate) — `website_blog`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_blog` |
| Display name | Blog |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d3a85bccf5bdcae6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_blog/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_mail`, `website_partner`, `html_builder`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_website_modules`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Publish blog posts, announces, news
- Inventory of user-facing artifacts (counts): menu items 5, views 12, window actions 5, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 4
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `blog.blog` (Blog); `blog.tag.category` (Blog Tag Category); `blog.tag` (Blog Tag); `blog.post` (Blog Post)
- Objects extended from other modules (9): `mail.thread`, `website.seo.metadata`, `website.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`, `website.published.multi.mixin`, `website.page_visibility_options.mixin`, `website.snippet.filter`, `website`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `mail.thread`, `website.seo.metadata`, `website.multi.mixin`, `website.cover_properties.mixin`, `website.searchable.mixin`, `website.published.multi.mixin`, `website.page_visibility_options.mixin`, `website.snippet.filter`, `website`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 16

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 49 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_blog (Blog)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_blog.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: publish blog posts, announcements and news (website_blog/__manifest__.py:9).

## A. Capabilities / functions
- Optional app (no `auto_install`); depends on website_mail, website_partner and html_builder (website_blog/__manifest__.py:11). Opens the blog page at install through a launch action (website_blog/data/website_blog_data.xml:29-38).
- Core: blogs (containers) with sub-title, cover, own web page listing posts; posts with title, sub-title, author, tags, rich content, teaser, cover, publication date and view counter (website_blog/models/website_blog.py:14-37, 161-204).
- Core public pages: blog index (all blogs, or a single blog), filter by tag and by month, paging of 12 posts, per-blog feed (up to 50 items), post page with "next post" link, legacy URL redirect (website_blog/controllers/main.py:168-205, 207-215, 217-223, 224-295).
- Core: a single blog on the website makes the index redirect to that blog (website_blog/controllers/main.py:182-184).
- Core: website search, dynamic "blog posts" snippet with samples, suggested-controller and site-configurator hooks (website_blog/models/website.py:10-42; website_blog/models/website_snippet_filter.py:12-64; website_blog/views/snippets/s_blog_posts.xml).
- Core: "New Blog Post" quick-create from the website "new content" menu (website_blog/views/blog_post_add.xml:4-26).
- Optional feature: comments on posts via a template option that is inactive by default; anonymous visitors are asked to sign in to comment (website_blog/views/website_blog_templates.xml:306-319).
- Core: notification to blog followers when a post is published, on the blog chatter with subtype "Published Post" (website_blog/models/website_blog.py:241-250; website_blog/data/mail_message_subtype_data.xml:5-10).
- Seeds: default demo-like blog "Our blog" and a "Blog" menu entry are installed as normal (non-demo) data (website_blog/data/website_blog_data.xml:4-15).

## B. Business objects, relationships, lifecycle
- Blog (1) -> posts (n) -> tags (n:m) -> tag category; posts require a blog and vanish with it (website_blog/models/website_blog.py:36, 187-188, 130-136, 144-153).
- Post lifecycle: created (author defaults to current user's contact, first blog by default) -> published (flag) -> visible from its publication date -> archived (unpublishes) (website_blog/models/website_blog.py:183-187, 227-239, 262-264).
- Publication date: set when first published or re-published; blank publish date falls back to creation date; a future date holds the post back from public lists even if flagged published (website_blog/models/website_blog.py:198-199, 227-239, 267-270; website_blog/controllers/main.py:104-105).
- Archiving or restoring a blog does the same to all its posts (website_blog/models/website_blog.py:44-53).
- Followers: subscribing to a blog does not subscribe to its posts; commenting on a post makes the commenter a follower (TEST) (website_blog/tests/test_website_blog_flow.py:23-68). Replies to the "published" email are treated as internal notes to avoid spamming followers (website_blog/models/website_blog.py:55-64).
- Teaser: manual text, otherwise the first 200 characters of content (website_blog/models/website_blog.py:206-225); (TEST) (website_blog/tests/test_website_blog_flow.py:114-183).
- Views counter increases once per session per post (website_blog/controllers/main.py:289-294).

## C. Validations, automation, security, multi-company
- Tag names and tag category names are unique (website_blog/models/website_blog.py:138-141, 155-158).
- Access-control: public, portal, and internal users can read blogs, posts, tags, tag categories; website designers have full rights (website_blog/security/ir.model.access.csv:2-17). Record rules: public/portal see only published posts and only active blogs (website_blog/security/website_blog_security.xml:4-16). Internal users see all posts per access rows and the controller's date filter hides future-dated posts from non-designers (website_blog/controllers/main.py:35-36, 95-105, 259-260).
- A post whose publication date is still in the future, requested directly by a non-designer, redirects to the blog page (website_blog/controllers/main.py:259-265); unpublished posts are hidden from public/portal by the record rule (website_blog/security/website_blog_security.xml:4-9). Response shape for that hidden case: UNKNOWN — EVIDENCE INSUFFICIENT.
- Notification e-mail on publication is sent when a flagged-published post is created or updated and only for active posts (website_blog/models/website_blog.py:241-258, 272).
- Comment attachments need a valid ownership token; a portal user with a bad token is rejected (TEST) (website_blog/tests/test_website_blog_flow.py:70-112). Comments do not create inbox items, only emails (website_blog/models/website_blog.py:308-315).
- Posting rights on the thread are read-level (`_mail_post_access = 'read'`), so anyone who can read a post can comment where comments are enabled (website_blog/models/website_blog.py:168). Anonymous commenting: needs sign-in per the template text (website_blog/views/website_blog_templates.xml:317).
- Website scoping: blog is multi-website (optional website), post inherits blog's website; index queries filter by website (website_blog/models/website_blog.py:20, 204; website_blog/controllers/main.py:76, 180, 244).
- Company scoping: none (no company field). Referenced form fields cannot be deleted from the schema while a post content still references them (TEST) (website_blog/tests/test_website_blog_flow.py:221-240).
- Feed and search: feed lists posts with the caller's access (website_blog/controllers/main.py:212). A raw database aggregation is used for tag counts, bypassing record rules (website_blog/models/website_blog.py:66-98); effect: tag list may include tags of unpublished posts, UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- website_mail (follow widget, subscription), website_partner (author contact page), mail (chatter, followers, notifications), portal (comment thread), html_builder (editing), website (SEO, cover, multi-website, search, snippets, sitemap) (website_blog/__manifest__.py:11; website_blog/models/website_blog.py:17-23, 164-166).
- Nothing outside the website world consumes blog posts by evidence in this pass.

## E. Configuration / defaults that change outcomes
- Comments off by default (template option); sidebar/tags/cover options through website customise options (website_blog/views/website_blog_templates.xml:306-308).
- Posts per page 12; comments per page 10; feed limit up to 50 (website_blog/controllers/main.py:21-22, 212).
- Blog subtype "Published Post" is on by default for followers (website_blog/data/mail_message_subtype_data.xml:8).
- Tests for performance, sitemap language, UI flows exist (TEST) (website_blog/tests/test_performance.py:39-62; website_blog/tests/test_sitemap.py:24-38; website_blog/tests/test_ui.py:36-144).

## F. Effective extension path (module names only)
- website extended (family): website_blog with website_crm, website_crm_partner_assign, website_customer, website_event, website_forum, website_hr_recruitment, website_livechat, website_profile, website_sale, website_slides and others. website.snippet.filter: website_blog, website_event, website_sale. blog.* models are not extended by other modules in this tree. Referenced by test module test_website_modules.

## G. Not verified
- Email content of publication notification and per-recipient language: UNKNOWN — EVIDENCE INSUFFICIENT.
- Social sharing, rating and dynamic snippet behaviour in browser code: UNKNOWN — EVIDENCE INSUFFICIENT.

