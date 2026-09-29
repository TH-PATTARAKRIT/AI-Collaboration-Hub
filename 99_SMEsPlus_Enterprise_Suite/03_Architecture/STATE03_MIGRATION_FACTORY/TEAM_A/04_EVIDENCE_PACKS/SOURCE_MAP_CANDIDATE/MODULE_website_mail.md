# Source Map (candidate) — `website_mail`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_mail` |
| Display name | Website Mail |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `9ca504a6530f1a99` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_mail/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `mail`
- Direct dependents in 300-module list (4): `website_blog`, `website_forum`, `website_hr_recruitment`, `website_slides`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `website_event`, `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Website Module for Mail
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `publisher_warranty.contract`, `ir.http`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `publisher_warranty.contract`, `ir.http`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 31 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_mail (Website Mail)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_mail.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: mail improvements for the website, mainly the follow/subscribe widget (website_mail/__manifest__.py:9-11).

## A. Capabilities / functions
- Conditional: depends on website and mail and is `auto_install` (website_mail/__manifest__.py:12,17), so it is pulled in automatically when both are present. Whether it is present in a given deployment: UNKNOWN — EVIDENCE INSUFFICIENT.
- Core: a reusable "follow" block that lets a visitor subscribe or unsubscribe by email to any record that supports followers (blog posts, forum items, courses etc.), with subscribe/unsubscribe buttons or icons (website_mail/views/website_mail_templates.xml:3-30; website_mail/controllers/main.py:10-41).
- Core: a lookup that tells the page which of the listed records the current visitor already follows, and the visitor's known email (website_mail/controllers/main.py:43-81).
- Core: adds the mail translation bundle to the front-end (website_mail/models/ir_http.py:9-12).
- Reports website usage in the periodic instance-information message (website_mail/models/update.py:10-14).
- Front-end interaction and styling are loaded for all website pages (website_mail/__manifest__.py:18-22).

## B. Business objects, relationships, lifecycle
- No own stored model. It acts on followers (mail.followers) of any record: a visitor's contact (partner) is subscribed to or removed from the record's follower list (website_mail/controllers/main.py:32-40, 70-76).
- Lifecycle of a subscription: logged-in user -> own contact used; anonymous -> contact found or created from the entered email; subscribing stores the contact in the browser session so later visits recognise the visitor (website_mail/controllers/main.py:22-40, 64-65).
- The toggle is driven by the state sent by the page (currently following = "on" leads to unsubscribe) (website_mail/controllers/main.py:14,34-41; website_mail/views/website_mail_templates.xml:6).

## C. Validations, automation, security, multi-company
- Public route (no login) tied to the website; unknown record returns nothing (website_mail/controllers/main.py:10,15-17).
- The caller must have read access on the target record (website_mail/controllers/main.py:19), then the subscription itself is done with elevated rights (website_mail/controllers/main.py:35,40). Read access is therefore the only gate for subscribing an arbitrary email to a readable record.
- Anti-bot: for anonymous visitors the captcha hook is invoked; if it fails (or errors), the contact is looked up but not created (website_mail/controllers/main.py:26-32). The captcha implementations are optional add-ons (google_recaptcha, website_cf_turnstile).
- Follower lookup runs with elevated rights but only for the current visitor's contact and the record ids requested; no per-record access check on the listed ids (website_mail/controllers/main.py:59-76). Impact of leaking follow status of unreadable records: UNKNOWN — EVIDENCE INSUFFICIENT.
- No access-control rows, record rules or company scoping in this module; website scoping comes from the routes' `website=True` (website_mail/controllers/main.py:10,43).

## D. Handoffs to other modules
- mail (owner): follower list, subscribe/unsubscribe, contact-from-email matching (website_mail/controllers/main.py:32,35,40).
- google_recaptcha / website_cf_turnstile: optional captcha checks (website_mail/controllers/main.py:27; google_recaptcha/models/ir_http.py:36; website_cf_turnstile/models/ir_http.py:28).
- Consumers embedding the follow block: website_blog, website_forum, website_slides, website_event, website_hr_recruitment, website_sale (manifest dependency evidence: website_blog/__manifest__.py, website_event/__manifest__.py, website_forum/__manifest__.py, website_hr_recruitment/__manifest__.py, website_sale/__manifest__.py, website_slides/__manifest__.py). Exact embedding points of each: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Template parameters: `div_class` and `icons_design` switch between button and icon presentation; icon mode is not shown to anonymous users (website_mail/views/website_mail_templates.xml:4,13).
- `unsubscribe` request parameter pre-marks the block as an unsubscribe request (website_mail/views/website_mail_templates.xml:7).
- Captcha configuration lives elsewhere (see D). No settings of its own.

## F. Effective extension path (module names only)
- ir.http: also extended by many modules (see ir.http inheritors: website, portal, mail, google_recaptcha, website_cf_turnstile ...). publisher_warranty.contract: website_mail only.
- Modules depending on website_mail (manifest): website_blog, website_event, website_forum, website_hr_recruitment, website_sale, website_slides.

## G. Not verified
- Exact deliverability/confirmation of subscription emails (no double opt-in step in this module): UNKNOWN — EVIDENCE INSUFFICIENT.
- Module tests: none in this module.

