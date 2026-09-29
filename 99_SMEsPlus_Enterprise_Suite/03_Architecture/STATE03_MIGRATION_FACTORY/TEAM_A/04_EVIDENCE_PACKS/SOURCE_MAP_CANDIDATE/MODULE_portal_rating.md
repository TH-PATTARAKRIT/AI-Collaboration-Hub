# Source Map (candidate) — `portal_rating`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `portal_rating` |
| Display name | Portal Rating |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `10545635d5d646b3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/portal_rating/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `portal`, `rating`
- Direct dependents in 300-module list (1): `website_slides`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `ir.http`, `rating.rating`, `mail.message`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `rating.rating`, `mail.message`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 30 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: portal_rating (Portal Rating)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/portal_rating.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. This module has no tests directory (portal_rating/tests absent), so no (TEST) claims are made.

## A. Capabilities / functions
- Bridge module: adds customer-rating display and rating-related publishing to the customer portal discussion thread (portal_rating/__manifest__.py:6-10). Depends only on portal and rating (portal_rating/__manifest__.py:12-15).
- Conditional: installs automatically once both dependencies are present (`auto_install`) (portal_rating/__manifest__.py:21); it is not a manually chosen feature. Which business apps trigger those dependencies: UNKNOWN — EVIDENCE INSUFFICIENT.
- Core: lets the company post a public reply ("publisher comment") to a customer's rating, stored on the rating with author and time (portal_rating/models/rating_rating.py:8-12, 44-54).
- Core: portal thread messages can be enriched with the related rating, its publisher reply, and (when the rated document supports it) rating statistics, only if the caller asks for rating information (portal_rating/models/mail_message.py:11-23, 25-50).
- Core: portal thread search can filter to a single star value and treats a message with only a rating (no text) as non-empty (portal_rating/controllers/portal_chatter.py:6-13).
- Core: an authenticated endpoint to publish or update the comment on a rating (portal_rating/controllers/portal_rating.py:10-22).
- Optional presentation: static star widget and a popup composer ("Add Review" / "Edit Review") for pages of other apps; the composer is hidden from public visitors or when disabled by the host page (portal_rating/views/rating_templates.xml:6-41, 53-54, 78-90). Front-end assets are registered in the manifest (portal_rating/__manifest__.py:22-41).
- Back-office: the rating form gains a Comment block showing author and date (portal_rating/views/rating_rating_views.xml:8-19).

## B. Business objects, relationships, lifecycle
- Rating (owned by rating) is extended with three fields: publisher comment, commenting partner, comment date; the last two are read-only and behave like a stamp (portal_rating/models/rating_rating.py:8-12, 44-47).
- Rating -> message (one link from rating to a discussion message) and message -> ratings, with a derived rating value and consumed flag, are defined in rating, not here (rating/models/rating.py:49; rating/models/mail_message.py:11-27).
- Lifecycle of a publisher comment: whenever a comment text is supplied on create or update, the commenting partner defaults to the current user's partner and the date to now, if not given (portal_rating/models/rating_rating.py:48-54). No state machine or approval step exists in this module.
- Consumers: other apps embed the widgets, e.g. website_sale and website_slides depend on this module (website_sale/__manifest__.py:11; website_slides/__manifest__.py:23). Project only ships its own stylesheet named after it (project/__manifest__.py:108); a dependency is not shown there: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- Write guard on comments: a user may set a comment only if a member of the website restricted-editor group (when that group exists in the database) or holds write access on the rated document; otherwise access is refused with a message about needing write access on the related record (portal_rating/models/rating_rating.py:27-42).
- The guard runs on both create and update whenever comment text is present (portal_rating/models/rating_rating.py:14-25, 48-49). Empty comments bypass the check: UNKNOWN — EVIDENCE INSUFFICIENT whether clearing an existing comment is otherwise restricted.
- Publishing endpoint requires a logged-in user (portal_rating/controllers/portal_rating.py:10) and returns "Invalid rating" if the rating is not visible to the caller (portal_rating/controllers/portal_rating.py:12-17).
- Rating data is read with elevated rights when formatting portal messages (portal_rating/models/mail_message.py:34, 48), so visibility relies on the caller having already been allowed to see the message thread by the portal module. Exact portal thread access rules: UNKNOWN — EVIDENCE INSUFFICIENT (owned by portal).
- No access rules or ACL files are shipped in this module (no security directory); baseline ACL on rating: internal users read/write/create without delete, portal and public no direct access, system full (rating/security/ir.model.access.csv:2-5).
- No company scoping is defined here; multi-company behavior: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- Portal thread rendering and message fetching belong to portal; this module only extends them (portal_rating/controllers/portal_chatter.py:5; portal_rating/views/portal_templates.xml:3-6).
- Rating records, tokens, consumed state and average statistics belong to rating; this module adds the reply layer (portal_rating/models/rating_rating.py:5).
- Website product/course pages that show stars belong to their own apps (website_sale, website_slides); no accounting or sale-order handoff exists here.

## E. Configuration/defaults that change outcomes
- Request option "include rating information" gates whether rating data is added to portal messages (portal_rating/models/mail_message.py:18-22). Thread flag `display_rating` on the discussion container gates the rating UI (portal_rating/views/portal_templates.xml:5).
- Star-widget parameters on the host page (compressed style, inline mode, disable composer, default message/rating) change what is shown (portal_rating/views/rating_templates.xml:11-17, 54-77).
- No system parameters, settings screens or seed data in this module.

## F. Effective extension path
- portal, rating (dependencies); website_sale, website_slides (consuming apps); website (optional group referenced by name only).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: who is allowed to post the original customer rating from the portal (owned by rating/portal, outside the assigned files).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end behavior beyond declared templates and asset lists (browser-side scripts were not traced).
- Revision `19.0.post20260921`; findings apply to this revision only and are not universal rules.

