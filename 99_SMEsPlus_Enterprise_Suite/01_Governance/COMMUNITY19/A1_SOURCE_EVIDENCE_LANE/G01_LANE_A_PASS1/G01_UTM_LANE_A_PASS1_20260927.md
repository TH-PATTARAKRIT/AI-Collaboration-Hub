# G01 PLATFORM_BASE — LANE A PASS-1 — Module `utm`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T6 |
| Governed group | G01 PLATFORM_BASE |
| Module | `utm` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/utm/` |
| Retrieval | raw.githubusercontent.com at the anchor commit; files discovered via manifest and `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (static JS assets were skipped on purpose, as scoped) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |

## 1. Evidence Pointer Table (23 blobs; SHA-1 = `git hash-object`)

| Path (addons/utm/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 94c25dc98ad015df4c6d9278e415a4fe5fdc31a7 | Identity, deps, data/demo list |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Imports models only |
| `models/__init__.py` | adcd8af45dd19d1ee84f4031ea156b31533014f3 | Model import list |
| `models/utm_mixin.py` | 0c8be65a139fda06c873cec9d491090fdf33c655 | Tracking mixin, find-or-create, unique-name generator |
| `models/utm_campaign.py` | a9b073656845484d56a5e849753fddc9422ecfa6 | Campaign entity |
| `models/utm_medium.py` | 539b4dc75565ce2e15a6df3c69ba8de42ed176ba | Medium entity, protected records, fetch-or-create |
| `models/utm_source.py` | 636587e93760986da6b5db071174c16956c7ee6a | Source entity, protected Referral, source-naming mixin |
| `models/utm_stage.py` | 100018c7c714b26648644794a933b31e29d59a36 | Campaign stage |
| `models/utm_tag.py` | 6d00402c99d7da37310e0d32363e278cbbd46e38 | Campaign tag |
| `models/ir_http.py` | 8a6e6e4f25c7eea231b5d62284038c200d6b013e | Captures URL params into cookies after each request |
| `security/ir.model.access.csv` | 3f7f7241d5ff8085f40f32850124c0b83035d89f | ACL (10 rows) |
| `data/utm_medium_data.xml` | d719225fe7ca2e8ec444da96f2621b8beea9a60a | 10 seeded mediums (noupdate) |
| `data/utm_source_data.xml` | 736911c3e66e2f90915877a100650713ecda7660 | 10 seeded sources incl. Referral (noupdate) |
| `data/utm_stage_data.xml` | 87e7e7c0874ded298bbaaeed016909d03a5aa96c | Mandatory default stage "New" |
| `data/utm_tag_data.xml` | 30775283505691f46ee96aedd3bf4b0760452a8f | One seeded tag |
| `data/utm_campaign_demo.xml` | 32c0e3d64d84ed21bed2cff5c9cbb9556be0d7a6 | Demo campaigns |
| `data/utm_stage_demo.xml` | 979511e60b70e5fd6052d19b8e7fb23dd796a745 | Demo stages |
| `views/utm_campaign_views.xml` | f23ea50a57183d9533c80a5e941d18aaf333a718 | Campaign search/form/list/quick-create/kanban + action |
| `views/utm_medium_views.xml` | e29a96e30f05dfc9b463740b5fb7412126baeaec | Medium list/form/search + action |
| `views/utm_source_views.xml` | 43f8ce341818c115984d7c17cc5a01ae01dcf905 | Source list/form + action |
| `views/utm_stage_views.xml` | 1cb632f16bbb670308824683a9c6f3ffa99616b9 | Stage search/list/form + action |
| `views/utm_tag_views.xml` | bc453406cc49f037da45b8cc078c7b8ee9db93d8 | Tag list + action |
| `views/utm_menus.xml` | 7743723c576dc44e41da290ca806bce5ab659986 | Link Tracker / UTMs menus (debug-only) |

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
- U-M1: The module manages marketing attribution trackers: campaign, medium and source. It is version 1.1, category Marketing, licence LGPL-3. [`__manifest__.py`]
- U-M2: It depends only on `base` and `web`, which makes it a low-level shared dependency for business modules that attribute records to marketing origins. [`__manifest__.py`]
- U-M3: It has no controllers and no wizards. Static assets are loaded into the backend bundle. [`__init__.py`, `__manifest__.py`]

### 2.2 Data (models, mixins, key fields, constraints)
- U-D1 `utm.mixin` is an abstract capability. It adds three optional, indexed links (campaign, source, medium) to any business record that inherits it. [`models/utm_mixin.py`]
- U-D2 `utm.campaign`:
  - It has two name fields: an identifier (`name`, computed from the title, stored, editable, not translated) and a display title (required, translated).
  - It has a required responsible user (defaults to the current user) and a required stage (defaults to the first stage; deleting a stage that is in use is restricted; not copied).
  - Other fields: tags, an auto-generated flag, colour and an active flag.
  - The identifier is unique at database level.
  - Source: [`models/utm_campaign.py`]
- U-D3 `utm.medium`: its name is required, not translated and unique at database level. It has an active flag. [`models/utm_medium.py`]
- U-D4 `utm.source`: its name is required and unique at database level. The source has no active flag. [`models/utm_source.py`]
- U-D5 `utm.source.mixin` is an abstract capability for content records (for example mailings or posts). Each record owns exactly one source: required, deletion restricted while in use, not copied. The record's name is a writable proxy of the source name. [`models/utm_source.py`]
- U-D6 `utm.stage` has an ordered name (translated) and a sequence. `utm.tag` has a name (translated, unique) and a random default colour. [`models/utm_stage.py`, `models/utm_tag.py`]

### 2.3 Business rules / identity / uniqueness / auto-naming / protected records
- U-B1 **Unique-name generator** (WHAT): when a requested name collides with an existing one, case-insensitively, the generator appends a numeric counter suffix and fills gaps in the counter sequence. An explicitly requested counter is kept if it is free. Updates can exclude the records being changed so a record does not collide with itself. WHY: keeps tracker identities unique without rejecting user input. RISK: case-insensitive matching combined with suffixing can create near-duplicate trackers. [`models/utm_mixin.py`]
- U-B2 Creating a medium or source always passes the name through the generator. Creating a campaign uses the identifier (falling back to the title) and runs it through the generator. The identifier is recomputed from the title whenever the title changes. [`models/utm_medium.py`, `models/utm_source.py`, `models/utm_campaign.py`]
- U-B3 **Find-or-create from free text**:
  - A lookup matches the trimmed name case-insensitively and includes archived records.
  - If nothing matches, a new record is created. Campaigns created this way are flagged as auto-generated.
  - A public wrapper allows the same lookup for non-UTM models by plain create, relying on standard ACLs.
  - Source: [`models/utm_mixin.py`]
- U-B4 **Source naming**: a source name is generated from the content's display field: newlines are flattened, the text is truncated past a length threshold, and the model description and creation date are appended. When no explicit name is given, content records create their source in batch. A write that changes the name on several records at once is refused (error message about uniqueness). Duplicating a record creates a new source name with an incremented counter. [`models/utm_source.py`]
- U-B5 **Protected records**:
  - Six seeded mediums cannot be deleted: Email, Direct, Website, X, Facebook, LinkedIn (user error). The seeded mediums Phone, Banner, Television and Google Adwords are not protected.
  - The seeded Referral source cannot be deleted (validation error).
  - Both guards are skipped during module uninstall.
  - Source: [`models/utm_medium.py`, `models/utm_source.py`]
- U-B6 **Medium fetch-or-create by key**: a name is normalised into an external-id key under a given module namespace. If that key is missing, the medium and its external id are created with elevated rights. [`models/utm_medium.py`]
- U-B7 **Campaign lifecycle**: stage records are the only lifecycle, with no status transitions or guards. The kanban always shows every stage, including empty ones (the stage list is read with elevated rights). A default "New" stage ships as data, not demo, so the required stage is always available. [`models/utm_campaign.py`, `data/utm_stage_data.xml`]
- U-B8 **Attribution capture**:
  - After each HTTP request, the module copies the URL parameters `utm_campaign`, `utm_source` and `utm_medium` into optional cookies. The cookies last 31 days and are scoped to the request host.
  - When a record that inherits the mixin is created, default values are read from those cookies, and free-text values are resolved to records through find-or-create.
  - Salespeople are skipped (group `sales_team.group_sale_salesman`) unless the code runs as superuser.
  - Source: [`models/ir_http.py`, `models/utm_mixin.py`]
- U-B9 RISK: cookie-driven find-or-create means external visitors can cause new tracker records to be created simply by visiting a URL with UTM parameters, subject to the creating user's ACL at record creation.

### 2.4 Security
- U-S1 ACL (`security/ir.model.access.csv`):
  - Internal users (`base.group_user`) can read, write and create campaigns, mediums and sources, but not delete them. They can only read stages and tags.
  - Settings administrators (`base.group_system`) have full rights on all five models.
- U-S2 There are no groups and no record rules. No model has a company field, so trackers are shared across companies.
- U-S3 Elevated-rights use is limited to medium fetch-or-create (creating the record and its external id) and reading stages for kanban grouping.
- U-S4 Menus are restricted to debug mode (`base.group_no_one`). [`views/utm_menus.xml`]

### 2.5 UI surfaces (names only)
- The root menu "Link Tracker", with a "UTMs" submenu containing Campaigns, Mediums and Sources. [`views/utm_menus.xml`]
- Window actions exist for stages and tags, but no menu entry in this module points to them. [`views/utm_stage_views.xml`, `views/utm_tag_views.xml`]
- Campaign views: search, form, list, quick-create and kanban. There are no HTTP routes.

### 2.6 Jobs / config
- No crons and no config parameters. The cookie lifetime (31 days) is fixed in code.

## 3. Cross-module edges
- X1 `base` / `web`: user ownership of campaigns, ACL groups, and the HTTP post-dispatch hook.
- X2 Soft reference to `sales_team`: the group check in the mixin defaults, although that module is not a declared dependency.
- X3 Downstream: any module that inherits `utm.mixin` (attribution) or `utm.source.mixin` (content-owned sources). Its extension points include the tracking-field list and the cookie domain hook, and it can register its own mediums through the fetch-or-create namespace.
- X4 The public find-or-create wrapper is documented as used by frontend link tooling (a website links module). That edge is not verified here.

## 4. Evidence gaps / contradictions
- G1 In the free-text find-or-create helper, a statically observed path (a name that is blank after trimming) leaves the lookup variable unset before use. Whether this can be reached at runtime is unverified; the observation is flagged for A1 and is not claimed as a defect.
- G2 Protection is not uniform across the seeded mediums: four of the ten have no deletion guard. It is unclear whether this is intentional.
- G3 The contents of the demo files were not analysed beyond their presence. JS assets were not reviewed.
- G4 Downstream consumers of the mixins are outside this module and were not enumerated.
- No contradictions found.

## 5. Limitations
- Static source evidence only. Source presence does not prove runtime reachability. No runtime proof, no Formal Coverage claim, no percentages. GMVQ QIDs are not answered here.
