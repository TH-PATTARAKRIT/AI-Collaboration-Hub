# Source Map (candidate) — `website_mail_group`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_mail_group` |
| Display name | Website Mail Group |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c2b13edbff0d3159` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_mail_group/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mail_group`, `website`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: None / Add a website snippet for the mail groups.
- Inventory of user-facing artifacts (counts): menu items 3, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `mail.group`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `mail.group`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 27 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_mail_group (Website Mail Group)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_mail_group.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: a website building block for mail groups (website_mail_group/__manifest__.py:6).

## A. Capabilities / functions
- Conditional: depends on mail_group and website, `auto_install` (website_mail_group/__manifest__.py:8-9), so it appears automatically when both are installed.
- Core: a "Discussion Group" subscribe/unsubscribe snippet (email box + buttons) that can be dropped on any website page (website_mail_group/views/snippets/s_group.xml:3-15; website_mail_group/views/snippets/snippets.xml:7-11).
- Core: a public "is this email a member?" check used by the snippet, returning membership and the email (website_mail_group/controllers/main.py:9-38).
- Core: a "Go to Website" button on the mail group form that opens the public group page (website_mail_group/models/mail_group.py:10-16; website_mail_group/views/mail_group_views.xml:8-15).
- Menus: "Mailing Lists" and "Moderation Rules" under the website configuration menu, the latter for mail group managers only (website_mail_group/views/website_mail_group_menus.xml:3-17).
- Removes the "install this app" placeholder for the mail group snippet in the external snippets list (website_mail_group/views/snippets/snippets.xml:3-5).
- Builder option to choose the group shown by the snippet (website_mail_group/static/src/website_builder/mail_group_option_plugin.js).

## B. Business objects, relationships, lifecycle
- Uses mail group (owned by mail_group) and its members; no new model (website_mail_group/models/mail_group.py:7-9).
- Public group pages (list, thread, message, subscribe, unsubscribe, confirmation) are owned by mail_group (mail_group/controllers/portal.py:63, 104, 146, 242, 276, 344, 360).
- Subscription lifecycle: request subscribe -> confirmation link by email -> member created (routes `/group/subscribe`, `/group/subscribe-confirm`) (mail_group/controllers/portal.py:242, 344). Detail of confirmation email handling: UNKNOWN — EVIDENCE INSUFFICIENT.

## C. Validations, automation, security, multi-company
- Membership check requires the group to exist; if a signed token is supplied it must match the group's access token (otherwise nothing is returned) and then the group is read with elevated rights; without a token the caller must have read access to the group (website_mail_group/controllers/main.py:12-25).
- For logged-in users the check always uses their own email/contact, ignoring any email supplied; anonymous users' supplied email is used (website_mail_group/controllers/main.py:27-31). Membership look-up itself runs with elevated rights (website_mail_group/controllers/main.py:33).
- The group privacy modes (everyone / members / selected user group) are defined in mail_group; a group restricted to a user group must name that group (mail_group/models/mail_group.py:78-82, 226-228).
- Public `/groups` index lists groups found by a search with elevated rights when no token is given; token mode shows only one group (mail_group/controllers/portal.py:63-84). Visibility of private groups on that page: UNKNOWN — EVIDENCE INSUFFICIENT.
- Moderation menu limited to the mail-group manager group (website_mail_group/views/website_mail_group_menus.xml:16).
- No access-control rows or record rules here; no company scoping beyond website routes (website_mail_group/controllers/main.py:9).

## D. Handoffs to other modules
- mail_group (owner): groups, members, messages, moderation, tokens (mail_group/models/mail_group.py:700-703).
- website: snippet framework, menu root, technical page validation (website_mail_group/__manifest__.py:8; website_mail_group/views/website_mail_group_menus.xml:6).
- Test: the `/groups` page loads as a valid technical website page (TEST) (website_mail_group/tests/test_website_groups_technical_page.py:8-9).

## E. Configuration / defaults that change outcomes
- Which group the snippet targets is set in the page builder (website_mail_group/static/src/website_builder/mail_group_option_plugin.js). Group privacy mode default "Everyone" (mail_group/models/mail_group.py:78-82).

## F. Effective extension path (module names only)
- mail.group extended by: website_mail_group (plus mail_group itself). No other website module extends the snippet by evidence in this pass.

## G. Not verified
- Email templates, moderation flow and member data rules: UNKNOWN — EVIDENCE INSUFFICIENT (owned by mail_group; not traced here).

