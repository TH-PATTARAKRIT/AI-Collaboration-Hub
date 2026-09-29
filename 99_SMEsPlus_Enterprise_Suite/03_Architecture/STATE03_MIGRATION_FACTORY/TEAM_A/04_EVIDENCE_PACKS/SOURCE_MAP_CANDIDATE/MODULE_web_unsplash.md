# Source Map (candidate) — `web_unsplash`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `web_unsplash` |
| Display name | Unsplash Image Library |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `16c444583c5e46ae` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/web_unsplash/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`, `html_editor`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_website`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Find free high-resolution images from Unsplash
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 4
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `ir.qweb.field.image`, `res.users`, `res.config.settings`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.qweb.field.image`, `res.users`, `res.config.settings`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 28 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — web_unsplash
Source revision: 19.0.post20260921 | Module: "Unsplash Image Library" v1.1, category Hidden, LGPL-3 (web_unsplash/__manifest__.py:4-7,29). Basis: static reading; one HTTP test file read (TEST).

## A. Capabilities and optionality
- A1. Adds a stock-photo search source (Unsplash.com) to the image-library dialog of the rich-text/media editor; chosen images are downloaded into Odoo as attachments. web_unsplash/__manifest__.py:6,8,18-23; web_unsplash/controllers/main.py:44-128
- A2. Conditional: auto_install is on with dependencies base_setup and html_editor, so it is present whenever both are installed. web_unsplash/__manifest__.py:9,13
- A3. Base settings also expose an "Unsplash Image Library" toggle that installs/uninstalls the module; after enabling, the user must save and return to enter credentials. base_setup/models/res_config_settings.py:26; base_setup/views/res_config_settings_views.xml:157-161
- A4. Two credential fields ("Access Key", "Application ID") appear in Settings once the module is on. web_unsplash/models/res_config_settings.py:9-10; web_unsplash/views/res_config_settings_view.xml:9-17
- A5. On public pages, a small client script reports the display of Unsplash images to Unsplash's view-tracking endpoint if an Application ID is set. web_unsplash/static/src/frontend/unsplash_beacon.js:9-28

## B. Objects and lifecycle
- B1. No new business model. Extends the settings screen, users (one permission helper), and the image field converter used when web content is saved. web_unsplash/models/res_config_settings.py:6; web_unsplash/models/res_users.py:9; web_unsplash/models/ir_qweb_fields.py:6-10
- B2. Lifecycle of an imported image: download from Unsplash, re-encode/verify resolution, store as an attachment named "unsplash_<id>_<query><ext>" with a public-style path "/unsplash/<id>/<query>", optional description, access token generated, then Unsplash is pinged about the download. web_unsplash/controllers/main.py:101-126
- B3. When editable content containing such an image is saved back to a record, the stored image is taken from the matching attachment (same record, public, same path) instead of fetching it again. web_unsplash/models/ir_qweb_fields.py:16-28

## C. Validations, security, external service
- C1. Downloaded image URLs must start with the Unsplash image hosts (images. or plus. unsplash.com); the notify URL must start with the Unsplash photos API path; both checks are skipped during test runs. web_unsplash/controllers/main.py:34-35,84-86
- C2. Endpoints require a signed-in user except the app-id lookup, which is public. web_unsplash/controllers/main.py:44,130,147
- C3. Only administrators (settings group) or website restricted editors can save credentials; others get "not found". Same check decides whether a failed search shows a real error or a generic "no access". web_unsplash/models/res_users.py:15-16; web_unsplash/controllers/main.py:135-137,143-145,153-157
- C4. Uploading onto a record other than the user's own is denied by normal attachment access rules (TEST: partner and own user allowed, another user forbidden). web_unsplash/tests/test_unsplash.py:30-95. The bypass hook that lets non-admins store the image is declared in html_editor/models/ir_attachment.py:80-86; which module overrides it is UNKNOWN — EVIDENCE INSUFFICIENT.
- C5. Credentials are kept as system parameters (unsplash.access_key, unsplash.app_id), not per company. web_unsplash/models/res_config_settings.py:9-10. The Application ID is readable by anonymous visitors (C2). Every search sends the access key from the server to api.unsplash.com. web_unsplash/controllers/main.py:138-139
- C6. Company scoping: none defined in this module. Outbound network access to Unsplash is required for search and import.

## D. Handoffs
- D1. Media dialog / attachment creation: html_editor (owns attachment creation helper and dialog). web_unsplash/controllers/main.py:14,115; html_editor/controllers/main.py:254
- D2. Website: has tests and demo data referencing Unsplash images but no dependency (website comment says no dependency). website/tests/test_unsplash_beacon.py:7-43; web_unsplash/models/res_users.py:10-14
- D3. Settings screen and toggle: base_setup.

## E. Configuration that changes outcomes
- E1. If either the access key or the app id is empty, search returns an error state (key missing for managers, no access for others). web_unsplash/controllers/main.py:134-137
- E2. The view-tracking beacon only fires when an Application ID is present. web_unsplash/static/src/frontend/unsplash_beacon.js:21

## F. Extension path
- Modules referencing Unsplash: html_editor (dialog and attachment rights hook), website (beacon test/demo), test_website (tests); base_setup (toggle).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: Unsplash API terms, rate limits, or licensing of retrieved images (external).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end media-dialog behaviour (static JS only sampled).
- UNKNOWN — EVIDENCE INSUFFICIENT: what happens on failed downloads for the caller beyond the skipped item (log and continue is shown at main.py:94-99).

