> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_booth` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_booth` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_booth/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, security CSV, seed data. Views, mail-template body (beyond a short excerpt), demo data, static images, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstractions only; no verbatim vendor code reproduced. No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (11 blobs)

| Path (addons/event_booth/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 0f44bbc3875b442643b62b9054e26da601f252dd | Name "Events Booths", depends `event` only, data/demo list |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package init |
| `models/__init__.py` | dece3622c5a5c9b4a99389441ca42fd9cbe06ea0 | Model import roster |
| `models/event_booth.py` | 0eeb4018c17115ce07c37f3e4a3e1b36078a47f6 | `event.booth`: rentable booth instance, availability state, renter contact |
| `models/event_booth_category.py` | be27ceaf5d039f7cb220eacb368fb750ea402c94 | `event.booth.category`: booth product/tier definition |
| `models/event_event.py` | f82609bcc913cedd795254c45e8f773242890f4b | `event.event` extension: booth lines synced from template, booth counts |
| `models/event_type.py` | e557aa1f7a1a5b32f1208f77d0298b3ca07fc4a7 | `event.type` extension: template booth lines |
| `models/event_type_booth.py` | 62975bcad7611e27d2b4ea5312215f7dde8a7f2a | `event.type.booth`: per-template booth definition (base class `event.booth` inherits) |
| `security/ir.model.access.csv` | a28a53dc16cc68c1f9e6c06901a8d7641727f1c8 | Model ACL (9 rows) |
| `data/event_booth_category_data.xml` | d20865f3b2a5a8d04c084e8907a145a8e82d4751 | Seed categories: Standard/Premium/VIP booth, each with an image and an HTML feature list |
| `data/mail_message_subtype_data.xml` | d46e203639524cabecb3e09cb7e7e2e832e06877 | `mt_event_booth_booked` chatter subtype on `event.event` |

Blobs cited: **11**. All returned HTTP 200 and hash-verified against the pinned-commit tree. `data/mail_templates.xml` was fetched and hash-verified (hash `477ed9881a8f37d519375f741d0d6c8968c77489`) but its QWeb body was only spot-read, not cited as a numbered finding — recorded in gaps.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_booth` adds exhibitor/sponsor booth management to `event`: booth categories (tiers with price-relevant descriptions, though no price field lives in this module itself), per-event booth inventory, and an availability workflow (available → unavailable) with a renter contact and a chatter notification when a booth is booked. `depends`: `event` only. (`__manifest__.py`)
2. Data load order: ACL, then category/type/booth/event/menu views, then seed category data, a chatter subtype, and a mail-notification QWeb template. Demo data (booth + event-type demo) is separate. (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `event.booth` inherits `event.type.booth` (shares `name`, `event_type_id`→made optional here, `booth_category_id`) plus `mail.thread`/`mail.activity.mixin`. Adds `event_id` (required, cascade delete), renter fields `partner_id`/`contact_name`/`contact_email`/`contact_phone` (each computed-once from the partner then user-editable and stored), and `state` (available/unavailable, default available) with a computed `is_available` boolean (also searchable). No uniqueness constraint declared on the booth itself. (`models/event_booth.py`)
4. `event.booth.category` inherits `image.mixin` (gives it an image field set): `name`, `sequence`, `description` (HTML), and a `booth_ids` one2many visible only to `event.group_event_registration_desk`+ (field-level `groups=`). (`models/event_booth_category.py`)
5. `event.type.booth` is the per-event-template booth definition: `name`, `event_type_id` (required, cascade), `booth_category_id` (required; defaults to the sole existing category if there is exactly one). `event.booth` inherits this model directly, so a concrete booth carries the same name/category fields plus its own event/state/renter fields. (`models/event_type_booth.py`)
6. `event.event` extension adds `event_booth_ids` (one2many, computed-and-store, synced from the event's `event_type_id` the same "emulated onchange" way as tickets/mails in `event`), plus computed `event_booth_count`/`event_booth_count_available` and two computed many2many roll-ups of booth categories present on the event (`event_booth_category_ids`) and still available (`event_booth_category_available_ids`, intended for frontend use). `event.type` extension adds `event_type_booth_ids` (template booth lines). (`models/event_event.py`, `models/event_type.py`)

### 2.3 Business rules / states / lifecycle / exceptions
7. Booth lifecycle: `available` (default) → `unavailable`. `action_confirm(additional_values=None)` writes `state='unavailable'` merged with any extra values (extension point for a booking transaction, e.g. from a sale order in a downstream module) and posts a chatter notification (`_post_confirmation_message`, using the `mt_event_booth_booked` subtype and the `event_booth_booked_template` QWeb snippet) on the parent event, not on the booth itself. `write()` also independently detects a transition into `unavailable` (even without going through `action_confirm`) and posts the same confirmation message; `create()` similarly posts confirmation for any booth created already-unavailable, with `mail_create_nosubscribe` set to avoid auto-subscribing the creating user. WHY: any code path that marks a booth unavailable (direct write, `action_confirm`, or an already-booked import) reliably notifies followers of the event; RISK: no state guard prevents writing `unavailable→unavailable` twice or `unavailable→available` without a symmetrical "released" notification — only the confirm direction is instrumented. (`models/event_booth.py`)
8. Template sync mirrors the core `event` pattern for tickets/mail: `_compute_event_booth_ids` on `event.event` removes existing booth lines that are still `available` (i.e. unbooked placeholder lines from the template) and re-adds the current template's booth lines whenever `event_type_id` changes; booths that have already become `unavailable` (booked) are preserved. RISK: switching an event's template after some booths are already booked will still delete any *other* still-available template-derived booths and replace them with the new template's set — expected in isolation, but downstream modules that add price/order links to `event.booth` should confirm this doesn't strand paid-for-but-still-available booths (e.g. a booth marked available again after a cancelled order). (`models/event_event.py`)
9. No `@api.constrains` or `@api.ondelete` guards were found in this module's models (contrast with `event`'s question/ticket/slot delete guards) — booths and categories can apparently be deleted or reassigned without a source-level check here; not verified whether a downstream module (e.g. `event_booth_sale`) adds one.

### 2.4 Security
10. ACL (9 rows): both `event.booth` and `event.booth.category` carry an explicit base "deny all" row (empty group column, all perms 0) plus group-specific grants layered on top: `group_event_registration_desk` gets read-only on both; `group_event_user` and `group_event_manager` get full CRUD on `event.booth` and `event.type.booth`; only `group_event_manager` gets CRUD on `event.booth.category` (desk group is read-only on categories). No dedicated `ir.rule` (record rule) is declared in this module — multi-company scoping for `event.booth` relies entirely on the `event` module's rule on `event.event.company_id` reached indirectly (booths are per-event but have no own `company_id` field) — RISK: not source-confirmed that booth records are filtered by company; A1/A2 should check whether `event.booth` is reachable cross-company via its `event_id` relation without a rule on the booth model itself. (`security/ir.model.access.csv`)
11. `event.booth.category.booth_ids` is field-group-restricted to the registration-desk group and above, consistent with the ACL. (`models/event_booth_category.py`)

### 2.5 UI surfaces (names only, not fetched/read)
12. `views/`: `event_booth_category_views.xml`, `event_type_booth_views.xml`, `event_booth_views.xml`, `event_type_views.xml` (extension), `event_event_views.xml` (extension), `event_menus.xml`. File presence only.

### 2.6 Jobs / config / integrations
13. No crons and no `ir.config_parameter` reads found in this module's fetched files. The only "integration" observed is the chatter notification pipeline (`message_post_with_source`) reusing `mail`'s subtype/QWeb-template mechanism established by the `event` dependency. (`models/event_booth.py`, `data/mail_message_subtype_data.xml`, `data/mail_templates.xml`)

## 3. Cross-module edges
14. Depends on `event` only (dependency relationship, not group membership per MD-07/08): inherits `event.event`/`event.type`, and reuses `event.group_event_registration_desk`/`event.group_event_user`/`event.group_event_manager` groups defined there. (`__manifest__.py`, `security/ir.model.access.csv`)
15. `event.booth` is designed as an extension point: `event.type.booth` is a separate base model precisely so a booth "in a template" and a booth "on a live event" share fields via inheritance, the same pattern `event` itself uses for tickets/mail. A downstream module adding sale/pricing to booths (observed in this pilot's roster as `event_booth_sale`) would be expected to inherit `event.booth`/`event.type.booth` further — confirmed only as a structural expectation from this module's design, not verified against `event_booth_sale`'s actual code in this file (see separate `event_booth_sale` evidence file).

## 4. Evidence gaps / contradictions
- G1: Six view XML files not read.
- G2: `data/mail_templates.xml` QWeb body only spot-read (first ~30 lines); full template logic (conditional recipient display) not fully reviewed.
- G3: `data/event_booth_demo.xml`, `data/event_type_demo.xml` (demo-only) not fetched.
- G4: Static images (`static/src/img/*.jpeg`) referenced by the category seed data were not fetched (binary, out of scope for text evidence).
- G5: i18n and tests not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 11 fully-cited fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
