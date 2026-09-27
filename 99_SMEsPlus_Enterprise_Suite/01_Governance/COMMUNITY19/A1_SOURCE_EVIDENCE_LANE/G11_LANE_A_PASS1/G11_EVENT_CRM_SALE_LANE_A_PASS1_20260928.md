> **CANDIDATE-ROSTER PILOT — G11 membership is DERIVED, not Boss-confirmed; not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-17/MD-18.

# G11 EVENTS (pilot) — Module `event_crm_sale` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G11 EVENTS (CANDIDATE-ROSTER PILOT; DERIVED membership, not CONFIRMED) |
| Module | `event_crm_sale` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/event_crm_sale/`) |
| Retrieval | raw.githubusercontent.com at pinned commit; blob SHA-1 verified with `git hash-object` against `git ls-tree` of the same pinned commit |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, package inits, the module's single model-extension file. This module has no security file and no data file. View XML, i18n, tests NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |

Clean-room note: neutral WHAT/WHY/RISK abstraction only; no verbatim vendor code reproduced beyond short method-name pointers. No runtime proof, no Formal Coverage, no percentages, no GMVQ QID answered. `depends` in section 3 is a dependency relationship only, not a group-membership claim (MD-07/08).

## 1. Evidence Pointer Table (4 blobs)

| Path (addons/event_crm_sale/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | d8e088dfc27af087be79b87ed3c02b370848a0b8 | Name "Event CRM Sale", depends `event_crm`+`event_sale`, `auto_install: True` |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package init |
| `models/__init__.py` | 20ce9ac3fb49904b12c2942db487d94638265153 | Model import (single file) |
| `models/event_registration.py` | 480d4a0e41f20a04f853577b5f51001de2a27317 | `event.registration` extension: sale-order-based lead grouping override |

Blobs cited: **4**. This is the smallest module in the pilot's fetch set — it has no `security/`, no `data/`, and a single one-method model extension. All 4 fetches returned HTTP 200 and hash-verified against the pinned-commit tree.

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `event_crm_sale` is a narrow three-way bridge module whose entire purpose (per its own one-line description) is "add information of sale order linked to the registration for the creation of the lead" — i.e. it makes `event_crm`'s "per order" lead-grouping rule actually group by real `sale.order` records once `event_sale` is installed, instead of `event_crm`'s own date-based heuristic grouping. `depends`: `event_crm`, `event_sale`; `auto_install: True` (installs itself once both are present — not an independent choice). (`__manifest__.py`)
2. Only one data file is declared (`views/event_lead_rule_views.xml`) and no `security/*` file is shipped in this module. (`__manifest__.py`)

### 2.2 Data — models, inheritance, key fields, identity/uniqueness
3. No new model and no new field is declared anywhere in this module's Python. The single extension is a method override on the existing `event.registration` model (inherited from `event`, extended earlier by `event_crm` and, for the `sale_order_id` field this override reads, by `event_sale`). (`models/event_registration.py`)

### 2.3 Business rules / states / lifecycle / exceptions
4. `event.registration._get_lead_grouping` is overridden to replace `event_crm`'s default date-based ("registrations created in the same batch, approximated by matching `create_date`") grouping with sale-order-based grouping, but only for registrations that actually carry a `sale_order_id` (a field this module does not itself define — it is provided by `event_sale`'s extension of `event.registration`, confirmed only structurally here, not by reading `event_sale`'s file in this evidence pass). Registrations without a `sale_order_id` fall through to the parent (date-based) implementation unchanged. WHAT the override does: for each "per order" rule, it batches the new registrations by `sale_order_id`, searches (in one batch query, to avoid N+1 lookups) for any existing lead already linked to that same rule and to registrations sharing that sale order, and returns each sale order's registrations paired with that existing lead (so `event_crm`'s core loop can update it) or with no lead (so it creates a new one). WHY: a single sale order (e.g. one checkout buying tickets for 5 attendees) should produce or update exactly one lead, keyed on the order itself, rather than on a same-second heuristic that `event_crm`'s own docstring already flags as approximate. (`models/event_registration.py`)
5. RISK (carried over from `event_crm`'s own design note, now made concrete here): "update an existing lead" is only possible when a lead already exists for that exact `(rule, sale_order)` pair; if the lead was manually deleted, merged elsewhere, or the sale order's registrations were previously ungrouped (e.g. added to the order after the initial lead was created under the date-based path, before this module was installed), a new lead could be created alongside stale data rather than updating in place — not verified against runtime behavior; A1/A2 should confirm.

### 2.4 Security
6. No ACL and no `ir.rule` are shipped in this module — access to `event.registration`/`crm.lead` continues to be governed entirely by `event`, `event_crm`, `event_sale`, and `crm`'s own security definitions; this module only changes which existing, already-permitted lead gets updated vs. a new one created. Nothing here widens or narrows the permission surface.

### 2.5 UI surfaces (names only, not fetched/read)
7. `views/event_lead_rule_views.xml` — file presence only; likely exposes a sale-order-aware UI hint on the rule form (not verified).

### 2.6 Jobs / config / integrations
8. No crons and no `ir.config_parameter` reads. This module's only integration is the in-memory grouping-key change described in finding 4; it plugs into `event_crm`'s existing daily cron / creation-trigger pipeline without adding a new one. (`models/event_registration.py`)

## 3. Cross-module edges
9. Depends on `event_crm` and `event_sale` (dependency relationship only, not group membership per MD-07/08); both are within this pilot's DERIVED G11 roster. `auto_install: True` again means this module's presence is a consequence of the other two being installed together, consistent with the pattern already observed in `event_booth_sale` and `event_crm`. (`__manifest__.py`)
10. This module's single method reads a `sale_order_id` field on `event.registration` that it does not itself define — a direct, source-visible dependency on `event_sale`'s model extension being present, beyond the formal `depends` entry; A1 should note this as a genuine (not merely declared) coupling to confirm `event_sale`'s evidence file defines that field. (`models/event_registration.py`)

## 4. Evidence gaps / contradictions
- G1: `views/event_lead_rule_views.xml` (the module's only data file) not read.
- G2: i18n and tests not fetched (this module has neither an `i18n/` nor a `tests/` directory in the pinned-commit tree listing used to plan fetches).
- No contradictions observed between manifest, `__init__.py` roster, and fetched files. All 4 fetches returned HTTP 200 and hash-verified.

## 5. Limitations
Static source only, single pinned commit, no runtime/DB observation. CANDIDATE-ROSTER PILOT under MD-18 — G11 membership of this module is DERIVED, not Boss-confirmed. No GMVQ QID answered; no Formal Coverage claimed.
