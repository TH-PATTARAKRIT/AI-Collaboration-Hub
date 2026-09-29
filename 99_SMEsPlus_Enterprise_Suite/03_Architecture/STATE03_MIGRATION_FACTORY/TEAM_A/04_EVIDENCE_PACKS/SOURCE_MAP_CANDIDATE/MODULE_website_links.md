# Source Map (candidate) — `website_links`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_links` |
| Display name | Link Tracker |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d61a90927cc994b6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_links/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website`, `link_tracker`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `website_sale_loyalty`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/Website / Generate trackable & short URLs
- Inventory of user-facing artifacts (counts): menu items 1, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `link.tracker`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `link.tracker`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 40 of 41 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_links (Link Tracker)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_links.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: short, trackable URLs carrying campaign/medium/source markers, to measure clicks and downstream results (website_links/__manifest__.py:4-8).

## A. Capabilities / functions
- Conditional: depends on website and link_tracker and is `auto_install` (website_links/__manifest__.py:10,17); appears when both are installed.
- Core: a "Link Tracker" page on the website (`/r`) where a signed-in internal user pastes a target URL, picks campaign / medium / source, and gets a short tracked link (website_links/controller/main.py:15-21, 9-13).
- Core: choose a custom short code for an existing tracked link (website_links/controller/main.py:23-30).
- Core: "recent links" lists ordered as newest, most clicked, or recently used (website_links/controller/main.py:32-34; link_tracker/models/link_tracker.py:296-305).
- Core: a per-link statistics page reachable by appending "+" to the short URL, plus a "Statistics" button on the tracker form (website_links/controller/main.py:36-46; website_links/models/link_tracker.py:11-17; website_links/views/link_tracker_views.xml:8-10).
- Core: short URL host is the current website's domain, or the company's website domain when they differ (website_links/models/link_tracker.py:19-25); (TEST) (website_links/tests/test_link_tracker.py:42-66).
- Menu "Link Tracker" under the current-page website menu (website_links/views/link_tracker_views.xml:14-18).
- Redirect for visitors is owned by link_tracker: permanent redirect to the target with UTM markers added, one click record per non-bot visit (link_tracker/controller/main.py:12-23).

## B. Business objects, relationships, lifecycle
- Link tracker (target URL, title, label, campaign, medium, source, click count) -> codes (one or more short codes) -> clicks (IP, country, campaign) (link_tracker/models/link_tracker.py:31-53, 317-322, 345-356).
- Lifecycle: create link (a random short code is generated) -> optional extra custom code -> visits create clicks and raise the counter -> clicks removed if the link is deleted (link_tracker/models/link_tracker.py:192-222, 322, 352-353).
- Campaign/medium/source references are kept if their UTM record is deleted ("set null") (link_tracker/models/link_tracker.py:51-53).

## C. Validations, automation, security, multi-company
- Target URL is mandatory; links starting with `?` or `#` are refused; URL is normalised; page title auto-filled from the target page when empty (link_tracker/models/link_tracker.py:38, 192-206).
- Uniqueness: the combination URL + campaign + medium + source + label must be unique, else a user error listing the duplicates (link_tracker/models/link_tracker.py:154-190). Website page uses "search or create" so an existing identical link is reused (website_links/controller/main.py:13; link_tracker/models/link_tracker.py:224-273).
- UTM cookies never pre-fill a new tracker (link_tracker/models/link_tracker.py:208-211).
- Redirect route is public; bots are not counted (link_tracker/controller/main.py:12-16). Unknown code returns not-found (link_tracker/controller/main.py:21-22). Redirection is external-capable (`local=False`) (link_tracker/controller/main.py:23).
- (TEST) direct code redirect returns permanent redirect without language prefix; language alias path redirects first to the language path (website_links/tests/test_controller.py:30-48).
- Management pages/routes require a logged-in user (`auth='user'`) (website_links/controller/main.py:9,15,23,32,36). Creation buttons depend on create right (website_links/controller/main.py:18-19, 42).
- Access: website designers get full rights on link trackers, codes and clicks (website_links/security/ir.model.access.csv:2-4); base link_tracker grants internal users read-only and system admins full rights, public none (link_tracker/security/ir.model.access.csv:2-10). Result: an internal user without designer rights can read but not create trackers from the website page (website_links/controller/main.py:18-19).
- Multi-company: no record rules; only short-URL host depends on company/website (website_links/models/link_tracker.py:20-25). Visibility of trackers across companies: UNKNOWN — EVIDENCE INSUFFICIENT.
- Statistics route builds a page from the link's data with `read()` of the found link (website_links/controller/main.py:38-44).

## D. Handoffs to other modules
- link_tracker (owner of the model, redirect and clicks); utm (campaign/medium/source) (link_tracker/__manifest__.py:11).
- mass_mailing: extends the tracker and click models and auto-converts email links to tracked links (mass_mailing inherits link.tracker and link.tracker.click; link_tracker/models/link_tracker.py:275-279).
- Lead generation, sales orders and recruitment attribution of UTM values are consumed by crm, sale, hr_recruitment (manifest description website_links/__manifest__.py:7); mechanics not traced: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Which host appears in the short URL depends on the current website versus the user's company website (website_links/models/link_tracker.py:20-25).
- Minimum short-code length is a constant in link_tracker (link_tracker/models/link_tracker.py:20).
- No settings screen or system parameter in this module.

## F. Effective extension path (module names only)
- link.tracker extended by: mass_mailing, website_links. link.tracker.click extended by: mass_mailing.

## G. Not verified
- Custom code creation when the requested code already exists (response shape): UNKNOWN — EVIDENCE INSUFFICIENT.
- Tests: controller redirect, short-URL host, UI tour (TEST) (website_links/tests/test_controller.py; website_links/tests/test_link_tracker.py; website_links/tests/test_ui.py:20).

