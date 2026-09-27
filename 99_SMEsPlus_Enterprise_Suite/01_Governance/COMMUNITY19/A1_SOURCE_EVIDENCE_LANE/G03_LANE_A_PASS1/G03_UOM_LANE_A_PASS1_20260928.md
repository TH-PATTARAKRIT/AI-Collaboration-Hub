> **CANDIDATE-ROSTER PARTIAL EVIDENCE — G03 membership is PARTIAL (only the named anchor module(s) below are evidence-backed; the remaining 8 of 11 modules are unresolved GAP, not Boss-confirmed); not Formal Coverage; not a precedent for opening any other G02–G16 group.** See MASTER_DECISION_LOG_G01_20260927.md MD-07/MD-08/MD-17.

# G03 MASTER_DATA (partial) — Module `uom` — LANE A PASS-1 Source/Static Evidence

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Group | G03 MASTER_DATA (PARTIAL; 3/11 named anchors: `product`, `uom`, `analytic`; remaining 8 GAP) |
| Module | `uom` |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/uom/`) |
| Retrieval | raw.githubusercontent.com at the pinned commit; blob SHA-1 verified with `git hash-object` on fetched bytes against the pinned-commit tree (`git ls-tree` of a local shallow fetch of the same commit) |
| Date | 2026-09-28 |
| Scope | PASS-1 breadth: manifest, package inits, server-side Python model, security CSV/XML, seed data. Views (`views/uom_uom_views.xml`), JS/static assets, i18n, tests, demo data (none in this module) NOT studied. |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (breadth only; depth gaps in section 4) |

Clean-room note: all findings are neutral WHAT / WHY / RISK abstractions built from reading the fetched bytes; no source code is reproduced verbatim beyond short field/method names used as evidence pointers. Source presence does not equal runtime reachability. No runtime proof, no Formal Coverage claim, no percentages, no GMVQ QID answered. Dependencies listed in section 3 are dependency relationships only (per `depends` in `__manifest__.py`), not group-membership claims (MD-07/08 discipline).

## 1. Evidence Pointer Table (7 blobs)

| Path (addons/uom/…) | git blob SHA-1 (fetched, hash-verified) | Purpose |
|---|---|---|
| `__manifest__.py` | 6148b6e7f4976950c344090332d5a0e326a89fb4 | Name "Units of measure", category Sales/Sales, `depends: [base]`, data list, backend assets, LGPL-3 |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Package init (models) |
| `models/__init__.py` | 357b0410c0096a18f1abca149ea5cdd4fb822d83 | Model import roster |
| `models/uom_uom.py` | 5a066b510dbf7cd2e5912dfbef74e3c6a92dee65 | `uom.uom`: unit-of-measure record, conversion factor tree, rounding, conversion methods |
| `data/uom_data.xml` | 989e743efbac505779b0453dcdaa7e40aaa07362 | Seed `decimal.precision` row + ~30 seed `uom.uom` records (units, time, length, surface, volume, weight, energy; metric + US customary) |
| `security/uom_security.xml` | f7e0c0dd4d4742598a2816a5138a11d595831cf5 | Group `group_uom` ("Manage Multiple Units of Measure") |
| `security/ir.model.access.csv` | c22a097f9cef8b4aefabfbca7fb642de166a5f55 | Model ACL (2 rows) |

Blobs cited: **7**. All 7 fetches returned HTTP 200; all 7 blob SHA-1 values were re-derived locally with `git hash-object` on the fetched bytes and matched the `git ls-tree` listing of the same pinned commit (no unpinned listing was used as evidence — the tree listing only fixed which paths exist at that exact commit; every cited byte still comes from the pinned raw fetch).

## 2. Findings by A1 completion-card section

### 2.1 Manifest / dependencies / purpose
1. WHAT: `uom` ("Units of measure") is the base module defining units of measure and unit conversion for the rest of the system. WHY: it is the single source of truth for "how much is one X in terms of the reference unit," used anywhere a quantity is recorded or converted (weight, volume, length, time, count). Category Sales/Sales, license LGPL-3. (`__manifest__.py`)
2. Declared dependency (dependency relationship only, not group membership): `base` only. (`__manifest__.py`)
3. `data` installs seed data first (`data/uom_data.xml`), then security (`uom_security.xml`, `ir.model.access.csv`), then views. No `demo` key present — this module ships no demo data. Assets are injected only into `web.assets_backend` (a UI component under `static/src/components/`, not read in this pass). (`__manifest__.py`)

### 2.2 Data — model, inheritance, key fields, identity/uniqueness
4. `uom.uom` has no explicit `_inherit`/mixins (plain `models.Model`). It is self-referential via `relative_uom_id` (Many2one to itself, `ondelete='cascade'`), with `_parent_name = 'relative_uom_id'` and `_parent_store = True` — i.e. Odoo's materialized-path parent/child tooling (`parent_path`) is used to represent a *tree* of units, each expressed relative to another unit, rather than the flat "category + factor" model used by older Odoo versions. Key fields: `name` (required, translatable), `relative_factor` (required, unlimited-precision numeric, default 1.0, "how much bigger/smaller this unit is vs. its reference unit"), `active` (default True), computed+stored `factor` (the unit's absolute quantity, computed recursively up the `relative_uom_id` chain via `@api.depends(..., recursive=True)`), computed `sequence` (derived from `relative_factor`, capped at 1000, only auto-set before creation or when unset), computed `rounding` (shared across all UoMs, sourced from the `decimal.precision` record named "Product Unit"). A `related_uom_ids` One2many is the inverse of `relative_uom_id`. No explicit unique-name constraint was found in this file. (`models/uom_uom.py`)
5. Data-integrity constraint: `_factor_gt_zero` (DB `CHECK (relative_factor!=0)`) — a unit's own conversion ratio can never be zero. A Python-level `@api.constrains` (`_check_factor`) additionally requires a `relative_uom_id` whenever `relative_factor != 1.0`, i.e. only the implicit "reference of itself" units may have factor 1 with no parent. (`models/uom_uom.py`)

### 2.3 Business rules / states / lifecycle / exceptions
6. Conversion arithmetic: `_compute_quantity(qty, to_unit, round, rounding_method, raise_if_failure)` converts a quantity from `self` to `to_unit` by multiplying by `self.factor` then dividing by `to_unit.factor` (both being the each unit's own absolute-quantity chain result), then optionally rounds to `to_unit.rounding`. Because both source and destination units resolve to an absolute `factor` independent of category grouping, **no explicit "same measurement category" check is performed in this method** — converting between unrelated trees (e.g. a length unit and a weight unit) is not itself blocked by `_compute_quantity`; the docstring's own "different UomUom category" wording is aspirational relative to what the code enforces. RISK: A1 should verify whether a category-compatibility guard exists elsewhere (e.g. UI-level domain filters) since this method alone does not raise on cross-category conversion. (`models/uom_uom.py`)
7. `round()`, `compare()`, `is_zero()` all delegate to the same shared "Product Unit" `decimal.precision` entry (not a per-UoM precision), i.e. rounding precision is global across every unit of measure in the system, not configurable per unit. (`models/uom_uom.py`)
8. `_check_qty()` rounds a quantity to the nearest multiple of a packaging quantity (expressed in another UoM), used for "is this a whole number of packages" checks; it deliberately avoids the `%` modulo operator, noting float-precision pitfalls in its own comment. (`models/uom_uom.py`)
9. Protected/system seed units: `_unprotected_uom_xml_ids()` names three seed units (`product_uom_hour`, `product_uom_dozen`, `product_uom_pack_6`) as *not* protected by default (i.e. deletable) while `_filter_protected_uoms()` treats every other unit still linked to `uom`-module `ir.model.data` (external IDs) as protected. `_unlink_except_master_data` (an `@api.ondelete` guard, `at_uninstall=False`) raises a `UserError` naming the offending units if a delete would remove a protected one, recommending archiving instead. (`models/uom_uom.py`)
10. Editing-a-live-system warning: `_onchange_critical_fields` (on `relative_factor`) shows a non-blocking UI warning — not an error — if the record being edited is itself a protected UoM and is more than 1 day old, warning that "existing data WON'T be updated by this change" and that changing core units in a running database is not recommended. This is a warning only; the write is not prevented. (`models/uom_uom.py`)
11. `_has_common_reference(other_uom)` walks each unit's `parent_path` (materialized-path string) to determine whether two units share any ancestor in the relative-unit tree — used, per its docstring, to tell whether two units are convertible at all (same tree) as opposed to merely both resolving to some absolute factor. This is the closest thing in this module to a "compatible category" check, and it is a caller-invoked helper, not enforced inside `_compute_quantity` itself (see finding 6). (`models/uom_uom.py`)

### 2.4 Security
12. One custom group is defined: `group_uom` ("Manage Multiple Units of Measure"), with no `implied_ids` and no groups XML hierarchy beyond this single row — this module does not itself gate `uom.uom` CRUD by `group_uom`; that gating (if any) is expected to live in dependent modules' views (out of scope for this file; view bodies not read). (`security/uom_security.xml`)
13. ACL (2 rows): `base.group_system` (full CRUD) and `base.group_user` (read-only) on `uom.uom`. No row references `group_uom` in this module's own ACL file. No `ir.rule` (record rule / multi-company scoping) file exists in this module. (`security/ir.model.access.csv`)

### 2.5 UI surfaces (names only, not fetched/read)
14. `views/uom_uom_views.xml` (declared in the manifest's `data` list) — file presence only, not fetched in this pass.

### 2.6 Jobs / config / integrations
15. No cron jobs, no `ir.config_parameter` reads, and no outbound integrations were found anywhere in the fetched files.

## 3. Cross-module edges
16. Depends on (dependency relationship only, not group membership per MD-07/08): `base` only. (`__manifest__.py`)
17. `uom.uom` is a foundational reference model: any module recording a quantity (products, stock, sales, purchase, manufacturing, etc.) is expected to reference `uom.uom` records and call `_compute_quantity`/`round`/`compare`/`is_zero` for cross-unit arithmetic — confirmed only as a general Odoo pattern from this module's own API surface, not verified here against any specific dependent module's code (out of scope for this file).
18. `product` (this same G03 pilot's other anchor module) is expected to extend `uom.uom` with a `category_id`/product-specific grouping concept (the historical "UoM category" model that pre-19.0 Odoo used to gate cross-category conversion) — this is an inference from the module name and the gap identified in finding 6, not verified in this file; see `product`'s own Lane A Pass-1 file, where `models/uom_uom.py` (product's extension of this model) is separately fetched and hash-verified.

## 4. Evidence gaps / contradictions
- G1: `views/uom_uom_views.xml` was not fetched — menu/form/list structure and any `group_uom`-gated visibility are unverified.
- G2: The static asset under `static/src/components/**/*` (backend UI component) was not fetched — client-side behavior unverified.
- G3: `tests/` and `i18n/` (if present) were not enumerated or fetched — out of PASS-1 scope; this module's tree listing at the anchor was filtered to manifest/init/models/security/data/controllers/wizard patterns only, so an authoritative statement that no test files exist would require a fresh, unfiltered `git ls-tree` (not done in this pass; see Limitations).
- G4: Whether a "measurement category" concept exists elsewhere (e.g. on `product.uom.categ` or an equivalent model in a dependent module) that gates `_compute_quantity` at a higher layer was not checked — flagged as a RISK/open question for A1 in finding 6, not resolved here.
- No contradictions were observed between the manifest's declared `data` list, the `__init__.py` import roster, and the fetched files. All 7 cited fetches returned HTTP 200 and hash-verified.

## 5. Limitations
- PASS-1 breadth only; static source reading at a single pinned commit; no execution, no database, no runtime reachability.
- Blob SHA-1 values were computed locally with `git hash-object` on the fetched bytes and cross-checked against `git ls-tree` of the same pinned commit (via a local shallow fetch of that exact commit) — the tree listing was used only to confirm file paths/hashes at the anchor, not as a source of evidence content; all findings above are drawn only from the raw-fetched file bytes.
- This is a CANDIDATE-ROSTER PARTIAL-EVIDENCE file: `uom` is one of only 3 evidence-backed named anchors (with `product`, `analytic`) out of G03 MASTER_DATA's governed count of 11; the remaining 8 are unresolved GAP, not Boss-confirmed, per `GMVQ/GROUP_STRUCTURE_V2_CORE_CANDIDATE_20260928.tsv` and the OVQDT hold notice. Nothing in this file should be read as certifying the full G03 roster.
- No GMVQ QID is answered here; no Formal Coverage is claimed; no percentage or completion metric is implied.
