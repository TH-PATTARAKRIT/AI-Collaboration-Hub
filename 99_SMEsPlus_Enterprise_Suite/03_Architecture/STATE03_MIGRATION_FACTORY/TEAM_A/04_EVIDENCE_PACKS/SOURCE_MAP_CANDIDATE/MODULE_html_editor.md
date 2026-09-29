# Source Map (candidate) — `html_editor`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `html_editor` |
| Display name | HTML Editor |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5cf7d4199fe8c311` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/html_editor/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `bus`, `web`
- Direct dependents in 300-module list (6): `html_builder`, `mail`, `portal`, `web_unsplash`, `website`, `website_profile`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `point_of_sale`, `test_html_field_history`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / 
        A Html Editor component and plugin system
    
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 15
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `html_editor.converter.test` (Html Editor Converter Test); `html_editor.converter.test.sub` (Html Editor Converter Subtest); `html.field.history.mixin` (Field html History)
- Objects extended from other modules (21): `ir.http`, `base`, `ir.attachment`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.many2one`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.monetary`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.qweb`, `ir.ui.view`, `ir.websocket`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `html.field.history.mixin` ← Community: `project`, `test_html_field_history`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `base`, `ir.attachment`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.many2one`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.monetary`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.qweb`, `ir.ui.view`, `ir.websocket`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 47 of 47 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — html_editor
Source revision: 19.0.post20260921 | Module: "HTML Editor" (html_editor/__manifest__.py:2) | Category Hidden (:15) | License LGPL-3
Basis: static reading of manifest, models (history mixin, attachment, websocket, view saving), controllers, one access CSV, selected tests (TEST). Front-end framework module (brief note).

## A. Capabilities; core vs optional vs conditional
- A1. Provides an extensible rich-text editor component and plugin system for HTML fields, plus a read-only renderer for the public site. html_editor/__manifest__.py:3-10 (summary/description); assets sections :22-60
- A2. Core: auto_install is on; dependencies are base, bus, web only. Present automatically when those are present. html_editor/__manifest__.py:16,20
- A3. Media dialog support: upload image data or add by URL, look up image info, video URL data, edit/crop image copies, remove unused attachments. html_editor/controllers/main.py:216-246, 317-361, 363-373, 375-404, 406-497
- A4. Media library (external service): search and download stock images into attachments. Endpoint is a system parameter with a default external address. html_editor/controllers/main.py:499-548, 752-760
- A5. AI text generation (conditional on the external IAP service being reachable and quota available). html_editor/controllers/main.py:646-666
- A6. Real-time collaboration on an HTML field: bus channel per (model, field, record); WebRTC ICE server list. html_editor/controllers/main.py:668-684; html_editor/models/ir_websocket.py:8-41
- A7. Link previews: external (public route) and internal (login required). html_editor/controllers/main.py:686-750
- A8. Field history (versioning) as a reusable mixin: stores patches per versioned field with revision id, timestamp, user, and supports restore/compare. Opt-in per model by declaring versioned fields. html_editor/models/html_field_history_mixin.py:9-40, 48-112, 114-130
- A9. Rendering/parsing of dynamic fields in edited pages (converters between stored values and edited HTML for integer, float, many2one, contact, date, datetime, text, selection, html, image, monetary, duration). html_editor/models/ir_qweb_fields.py:178-599 (class list)
- A10. Saving edited page sections into template views and "oe_structure" areas; custom snippet save/rename/delete. html_editor/models/ir_ui_view.py:295-360, 462-560
- A11. Edit-mode flags ("editable", "edit_translations", "translatable") are picked up from the request query string and put in the request context. html_editor/models/ir_http.py:5-20

## B. Business objects, relationships, lifecycle
- B1. Attachment extension: adds a local URL, image source URL, image width/height (computed), and a link to an "original" unoptimized attachment (used when an image is resized/optimized). html_editor/models/ir_attachment.py:23-27, 29-72
- B2. Only image types gif, jpeg, png, svg, webp get an image source. html_editor/models/ir_attachment.py:9-17, 40
- B3. Attachments created from the editor are public and unattached when they belong to view content; otherwise linked to the given record. html_editor/controllers/main.py:266-278
- B4. History lifecycle: on save of a versioned field, a patch to the previous content is inserted at the head with next revision number; history is capped (default 300 revisions per field); direct writes to the history field are ignored; history is not copied in on create. html_editor/models/html_field_history_mixin.py:12, 42-46, 48-112
- B5. Adopters of history: project task description (owner: project). project/models/project_task.py:109-110; test model test_html_field_history (test-only module). test_html_field_history/models/model_html_field_history_test.py
- B6. Test-only models (converter test) with system-admin-only access exist in this module. html_editor/security/ir.model.access.csv:2-3; html_editor/models/test_models.py:6,32
- B7. View saving lifecycle: edited section parsed; embedded field elements saved back to their records and replaced by field references; oe_structure areas saved into separate records when non-empty; arch written only if it actually changed, and marked as protected from module updates. html_editor/models/ir_ui_view.py:295-360, 292-294

## C. Validations, automation, security, multi-company
- C1. All editor routes require a logged-in user except: public shape/image-shape rendering and external link preview. html_editor/controllers/main.py:550,606,686 (auth public); others auth user (:216,317,363,375,400,406,499,646,668,672,693,752)
- C2. Users without permission to create attachments may still be allowed through a hook that base returns False for; other modules (e.g., forum-type or unsplash uploads) override it; when bypassed the record is created with elevated rights and a token generated if not public. html_editor/models/ir_attachment.py:79-86; html_editor/controllers/main.py:300-312
- C3. Attachment removal is blocked when any view still references the attachment URL; blocked ones are reported with the view names. html_editor/controllers/main.py:216-246
- C4. Editing an image copy requires read on the source record and write on the target record. html_editor/controllers/main.py:444-449
- C5. Collaboration channel subscription and broadcast require: not public, read and write on the document, and read and write on the field. html_editor/models/ir_websocket.py:23-38; html_editor/controllers/main.py:672-684
- C6. History requires versioned fields to be sanitized fields; otherwise the write fails with a validation error. html_editor/models/html_field_history_mixin.py:71-75
- C7. Company context: the attachment-removal route drops the allowed-companies context so website scoping does not hide attachments. html_editor/controllers/main.py:248-251. Other multi-company behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.
- C8. Saved-snippet name uniqueness is computed within the current website's domain (website scoping enters through context). html_editor/models/ir_ui_view.py:475-482. (Website model owner: website.)
- C9. (TEST) Upload and admin attachment creation, illustration shape, image info, internal link preview covered. html_editor/tests/test_controller.py:28,50,100,133,146
- C10. (TEST) Views: infinite inheritance loop guard, oe_structure as inherited view, available-name search. html_editor/tests/test_views.py:24,34,65
- C11. (TEST) Diff utilities for history. html_editor/tests/test_diff_utils.py (file-level pointer)

## D. Handoffs
- D1. Bus / websocket channels for collaboration: bus. html_editor/models/ir_websocket.py:8-9; html_editor/__manifest__.py:16
- D2. External AI text generation and IAP transport: iap tools (base-side helper), quota outcomes shown as user messages. html_editor/controllers/main.py:646-666
- D3. ICE server list for live collaboration: mail (mail.ice.server). html_editor/controllers/main.py:668-670
- D4. Website editing, published pages, snippet stores, website scoping: website (and html_builder as the newer builder front end). website/__manifest__.py:445
- D5. Portal chatter/editing uses this editor library: portal declares dependency. portal/__manifest__.py:12
- D6. Other modules that list html_editor as a dependency: mail, portal, point_of_sale, web_unsplash, website_profile, website, test_html_field_history, html_builder (manifest grep).
- D7. Stock image download and media search services: external "media library" service configured by parameter. html_editor/controllers/main.py:513-514, 754-755

## E. Configuration / defaults that change outcomes
- E1. html_editor.media_library_endpoint (default external media library address) controls stock-media search/download. html_editor/controllers/main.py:513-514, 754-755
- E2. html_editor.olg_api_endpoint (default external text-generation address) controls AI text. html_editor/controllers/main.py:27, 649-650
- E3. History size limit default 300 revisions, overridable per model. html_editor/models/html_field_history_mixin.py:12, 105-106
- E4. Query-string flags switch on editable / translation edit contexts. html_editor/models/ir_http.py:5, 8-20
- E5. Database identity (uuid) is sent to the external media library and AI endpoints. html_editor/controllers/main.py:517-520, 651-656 (data leaving the system; note for privacy review)

## F. Effective extension path (module names only)
- project (history adopter), website, html_builder, web_unsplash (attachment bypass hook, per hook comment only), website_profile, point_of_sale, mail, portal, mass_mailing. Hook implementers for attachment bypass: UNKNOWN — EVIDENCE INSUFFICIENT (not searched).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: editor plugin behaviours in JavaScript.
- UNKNOWN — EVIDENCE INSUFFICIENT: field-level converters' failure handling in ir_qweb_fields beyond class list.
- UNKNOWN — EVIDENCE INSUFFICIENT: which modules override the attachment-rights bypass hook.
- UNKNOWN — EVIDENCE INSUFFICIENT: exact restore semantics of history comparison beyond lines read.

