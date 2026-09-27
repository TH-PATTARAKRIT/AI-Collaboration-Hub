> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_product` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_product` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_product/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, models, seed data. This module ships **no `security/` directory at all** (confirmed against the pinned-commit tree listing, not merely absent from the fetch plan). Views, demo data, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstraction only; no verbatim vendor code reproduced beyond short field/method-name pointers. No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (10 blobs)

| Path (addons/event_product/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | b0742fefb19cdb594b3c729aa2644c8c2e8adbce | Name "Events Product", depends `event`+`product`+`account`, `auto_install: True` |
| `__init__.py` | 0650744f6bc69b9f0b865e8c7174c813a5f5995e | Package init |
| `data/event_product_data.xml` | 577ad52ea432dd0e0d7f536046e3192276b202cd | Seed product category "Events" + a default "Event Registration" service product |
| `models/__init__.py` | 55b06f9c5fe3334aa357fd7007bb84923cf71ede | Model import roster |
| `models/event_event.py` | fbe71750dd89dc354e138c61a48ffbd5f7303a7c | `event.event` extension: related company currency |
| `models/event_event_ticket.py` | 6bb9e960113463e9748a5cd733a415f0929bf2d7 | `event.event.ticket` extension: tax-inclusive pricing fields |
| `models/event_registration.py` | ed1861270304a654b7abaf2f71456cadb5146017 | `event.registration` extension: shared `sale_status` field/default logic |
| `models/event_type_ticket.py` | e0056361d0d21c8ccf0e045233056b5c1947a0ec | `event.type.ticket` extension: adds the `product_id`/`price` fields that make a ticket type sellable |
| `models/product_product.py` | 4d94b04e2863b1b15d25862c0cbe50d52f456a68 | `product.product` extension: reverse link to tickets + integrity constraint |
| `models/product_template.py` | 0b6c5e223de37a89651a7afd8c3b3ffc2f6ddf95 | `product.template` extension: adds the `event` `service_tracking` option |

Blobs cited: **10**. All returned HTTP 200 and hash-verified against the pinned-commit tree. No `security/ir.model.access.csv` and no `security/*.xml` exist in this module at the pinned commit (confirmed via `git ls-tree` of the anchor commit, not an assumption) — recorded as a finding, not a gap.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_product` is the foundational bridge that makes an event *ticket type* into a sellable `product.product` (a new `service_tracking = 'event'` product category), independent of whether an actual point-of-sale or e-commerce sale flow (`event_sale`, `pos_event`) is installed. It adds the `product_id`/`price` fields onto `event.type.ticket` (the template-level ticket definition already present in `event`), and a shared `sale_status` field on `event.registration` intended to be computed cooperatively by whichever selling module (`event_sale` or `pos_event`) is actually installed. `depends`: `event`, `product`, `account`; `auto_install: True` (installs automatically once all three are present, not an independent choice — same pattern already observed in the other `event_*` bridge modules in this pilot). (`__manifest__.py`)
2. Declares an empty `assets` dict explicitly (`'assets': {}`) — i.e. no JS/CSS assets, backend or frontend. (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. `event.type.ticket` extension adds: `description` (computed from the linked product's sale description, then user-editable and stored), `product_id` (required, indexed, domain `service_tracking='event'`, defaults to a seeded generic "Event Registration" product), `currency_id` (related), `price` (computed from the product's list price, then editable and stored), `price_reduce` (computed from the product's "contextual discount," itself flagged in-source as a hacky, pricelist-adjacent mechanism — see finding 8). (`models/event_type_ticket.py`)
4. `event.event.ticket` extension (the per-event, not per-template, ticket row) adds `price_reduce_taxinc` and `price_incl`, both computed tax-inclusive prices, filtering the product's taxes to only those belonging to the *event's* company (not necessarily the product's own company) before computing. (`models/event_event_ticket.py`)
5. `event.event` extension adds a single related, read-only `currency_id` (the event's company's currency). `product.product` extension adds a reverse one2many `event_ticket_ids` (which tickets use this product). `product.template` extension adds a new `service_tracking` selection value `'event'` ("Event Registration") and blacklists it from the generic service-tracking configurator UI (same pattern as `event_booth_sale`'s `'event_booth'` value). (`models/event_event.py`, `models/product_product.py`, `models/product_template.py`)
6. `event.registration` extension adds `sale_status` (selection: to_pay/sold/free; computed, stored, sudo-computed, read-only, precomputed). The model comment explicitly states this field is intentionally placed in this base bridge module (rather than in `event_sale` or `pos_event` directly) because *both* of those modules need to compute it, and each is expected to override `_compute_registration_status`/`_has_order()` rather than redefine the field. In this module alone (with neither selling module's logic present), `_has_order()` always returns `False`, so every registration defaults to `sale_status='free'` and `state='open'` if not already set. (`models/event_registration.py`)

### 2.3 Business rules / states / lifecycle / exceptions
7. Product/ticket integrity: a product cannot be linked to any `event.event.ticket` unless its `service_tracking` is exactly `'event'` (`@api.constrains` on `product.product`, `ValidationError` naming the field's own selection label). (`models/product_product.py`)
8. Pricing: `event.type.ticket.price_reduce` is explicitly flagged in a source comment as "broken by design, depending on the hacky `_get_contextual_discount` field on products… core part of the pricelist mess" and marked `TODO clean this feature in master`, with a note that its usage should be UX-only, never used for effective price computation. RISK: this is a source-author-acknowledged, not hypothetical, weakness — A1/A2 should confirm no downstream module (e.g. `event_sale`, `event_booth_sale`, both of which reuse a near-identical `price_reduce` compute pattern) relies on this value for anything beyond display. (`models/event_type_ticket.py`)
9. `event.event.ticket._compute_sale_available` is overridden: a ticket whose linked product has been archived (`product_id.active = False`) is forced to `sale_available = False` before falling through to the base availability computation (seat/date logic from `event`) for the remaining tickets — i.e. archiving the underlying product is a valid way to pull a ticket off sale without touching the ticket/event records themselves. (`models/event_event_ticket.py`)
10. Data-migration helper `_init_column` on `event.type.ticket` (structurally identical to the one seen in `event_booth_sale`'s `event.booth.category`): when this module is installed onto a database with pre-existing `event.type.ticket` rows, it back-fills the newly-required `product_id` column via a direct SQL `UPDATE`, creating a generic fallback product if the seeded one isn't found. Same RISK class as in `event_booth_sale`: raw SQL bypassing ORM validation during a one-time install-time backfill. (`models/event_type_ticket.py`)
11. The `sale_status` field's coordination contract (finding 6) is a source-visible cross-module design decision rather than an enforced one: nothing in this module's own code prevents two selling modules from both being installed and both overriding `_compute_registration_status` inconsistently; this is a design assumption A1/A2 should flag as unverified without also reading `event_sale`'s and `pos_event`'s overrides together.

### 2.4 Security
12. **No security file exists in this module.** There is no `security/ir.model.access.csv` and no `security/*.xml` at all in the pinned-commit tree for `addons/event_product/` — confirmed by listing the pinned commit's tree (`git ls-tree`), not merely by omission from the fetch plan. All access to the fields/behavior this module adds is therefore governed entirely by the base ACL/rules already defined in `event`, `product`, and `account` for the models being extended (`event.type.ticket`, `event.event.ticket`, `event.registration`, `product.product`, `product.template`, `event.event`) — this module adds no new model that would require its own ACL row. RISK framing: nothing to evidence here beyond noting the absence itself, which is a normal pattern for a pure model-extension bridge module with no new models.

### 2.5 UI surfaces (names only, not fetched/read)
13. `views/event_ticket_views.xml`, `views/event_registration_views.xml`. File presence only.

### 2.6 Jobs / config / integrations
14. No crons and no `ir.config_parameter` reads found in this module's fetched files. The only external-facing integration is the product/service-tracking mechanism shared with `account`/`product` (invoicing policy via `service_tracking`, reused by downstream selling modules). (`__manifest__.py`, `models/product_template.py`)

## 3. Cross-module edges
15. Depends on `event`, `product`, `account` (dependency relationship only, not group membership per MD-07/08); `auto_install: True` — its presence in a database is a consequence of those three, not an independent choice, matching the pattern in the other `event_*` bridge modules seen in this pilot. (`__manifest__.py`)
16. This module is the actual origin of the `product_id`/`price` fields on `event.type.ticket` and the `event`-valued `service_tracking` selection that `event.event.ticket`/downstream selling modules build on. `event_sale`'s own manifest (verified separately; see its evidence file) declares `event_product` directly in its `depends`, confirming this upstream relationship formally, not just structurally. The `sale_status` field defined here is the shared contract point both `event_sale` and `pos_event` (not in this pilot's roster) are expected to complete. (`models/event_registration.py`, `models/event_type_ticket.py`)
17. Seeds a product category (`event_product.product_category_events`) that `event_booth_sale`'s fallback-product creation code (evidenced separately) also references by external ID — a direct, source-confirmed cross-module data dependency beyond the formal `depends` declarations.

## 4. Evidence gaps / contradictions
- G1: Two view XML files not read.
- G2: `data/event_product_demo.xml`, `data/event_demo.xml` (demo-only) not fetched.
- G3: i18n and tests not fetched.
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 10 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
