# G01 PLATFORM_BASE — LANE A PASS-1 — Module `resource_mail`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T6 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `resource_mail` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/resource_mail/` |
| Retrieval | raw.githubusercontent.com at the anchor commit; files found through the manifest and the `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (Python and manifest surface fully read; static JS skipped on purpose, as scoped, which leaves its UI behaviour an open gap) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |
| Question bank | No module-specific bank yet (Standard 55 only). This does not block Lane A. No QIDs are answered here. |

## 1. Evidence Pointer Table (4 blobs; SHA-1 = `git hash-object`)

| Path (addons/resource_mail/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 032a25c2cd5c1be067974b60ca1efb7c5848d54c | Identity, deps, auto-install, assets |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Imports models only |
| `models/__init__.py` | 756a33c3d3d50e77c2563c6caad30b45d78602a6 | Imports the single resource extension |
| `models/resource_resource.py` | 797be7bd04f8ef3f089dbda74db6cf9841b84406 | Extends the resource with colour, presence and avatar-card data |

Probed absences (HTTP 404, not imported → absence, not gap): `controllers/__init__.py`, `wizard/__init__.py`.
The manifest has no `data` or `demo` keys, so this module ships no security, view, menu or data files.

## 2. Findings by card section

### 2.1 Manifest / deps / purpose
1. Hidden bridge module. Depends on `resource` and `mail`. **Auto-install** (it installs as soon as both dependencies are present). LGPL-3. Stated purpose: make features built for users in the messaging layer usable for resources as well. [`__manifest__.py`]
2. Its main payload is front-end assets (backend bundle and unit-test bundle), which were skipped by scope. The Python side is a small model extension. [`__manifest__.py`]

### 2.2 Data
3. Adds two fields to the resource entity:
    - a stored integer **colour**, defaulting to a random value from a small fixed palette range (1–11);
    - a non-stored **presence status**, related to the linked user's messaging presence.
    [`models/resource_resource.py`]
4. No new models, no constraints and no timezone handling. Resources without a linked user get an empty presence status (a consequence of the related-field chain; not runtime-verified).

### 2.3 Business rules / exceptions
5. It exposes a public method that returns caller-selected fields of the resource for an "avatar card" UI. It relies wholly on the standard read path, so ordinary ACLs and record rules apply; it adds no extra filtering or elevation. WHY: lets the UI show a resource popover the way a user popover is shown. RISK: the caller chooses which fields are returned. Exposure is bounded by field-level and model access, which is read-only for internal users on `resource.resource` per the `resource` module's ACL. [`models/resource_resource.py`; ACL cross-ref `resource/security/ir.model.access.csv` blob 34ca64a5…]
6. The random default colour is not deterministic. Two resources can share a colour, and colours are not unique.

### 2.4 Security
7. No ACL, record-rule or group files. It inherits all access control from `resource` (resource: read for internal users and system admins; multi-company rule on company plus none) and from `mail` (the presence source). [manifest data absence; see `resource` card §2.4]

### 2.5 UI surfaces (names only)
8. No server-side views, actions or menus. Any UI (for example avatar cards or presence badges for resources) lives in the skipped JS assets and is **not evidenced** in this pass.

### 2.6 Jobs / config
9. No scheduled jobs, settings, data records or controllers.

## 3. Cross-module edges
10. **resource → resource_mail**: extends `resource.resource` in place (inheritance, no new model).
11. **mail → resource_mail**: the presence value is read through the linked user's messaging presence field, which the `mail` module owns. This field lives on the user model and was not re-read here.
12. **Downstream**: auto-installing means any database with both `resource` and `mail` gets these fields. Consumers (likely scheduling/HR UIs) were not identified from this module's source.

## 4. Evidence gaps / contradictions
- G1: Static JS (`static/src/**`) and its tests were not reviewed (scoped out). The actual UI behaviour of the bridge is therefore unevidenced.
- G2: The presence field's definition on the user model (in `mail`) was not re-read in this slot. It is taken from the relation path only.
- G3: No callers of the avatar-card method were found in Python. The consumer is presumed to be JS (unverified).
- No contradictions observed.

## 5. Limitations
Source presence ≠ runtime reachability. No runtime proof, no Formal Coverage, no percentages. The findings are a static reading of a single commit.
