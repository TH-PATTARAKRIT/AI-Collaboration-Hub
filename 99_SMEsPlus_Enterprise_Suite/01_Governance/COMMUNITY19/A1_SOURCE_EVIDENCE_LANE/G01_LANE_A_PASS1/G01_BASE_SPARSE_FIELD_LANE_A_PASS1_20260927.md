# G01 PLATFORM_BASE — LANE A PASS-1 — `base_sparse_field`

| Item | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T4 (refill) |
| Group | G01 PLATFORM_BASE |
| Module | `base_sparse_field` (governed roster member, FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** |
| Handoff target | RED TEAM A1 only. No Lane B material viewed. No runtime proof claimed. |

Clean-room note: findings are neutral WHAT / WHY / RISK abstractions. Identifiers are pointers only; nothing here is a recommendation to copy schema, ORM, workflow or UI. No GMVQ QID is answered here.

## 1. Evidence Pointer Table

All paths relative to `addons/` at the anchor commit. SHA-1 = `git hash-object` of the fetched file.

| # | Path | Git blob SHA-1 | Purpose |
|---|---|---|---|
| E1 | base_sparse_field/__manifest__.py | c487ecfef4f50434826b1df23933f76a3dcd686c | Manifest: purpose, deps, data list |
| E2 | base_sparse_field/__init__.py | cde864bae21a11c0e4f50067aa46b4c497549b4c | Package imports (models only) |
| E3 | base_sparse_field/models/__init__.py | 37c0f9345ccd8da658314ee901c59970f16c8039 | Imports field-framework patch + model extensions |
| E4 | base_sparse_field/models/fields.py | cb26946e9e356dee65fe65fca09dbe24fd4373cb | Field-framework patch: `sparse` attribute, `Serialized` field type |
| E5 | base_sparse_field/models/models.py | f219622654de80989f1202226dee84c3ff8caef9 | Extensions of `base`, `ir.model.fields`; demo transient model |
| E6 | base_sparse_field/security/ir.model.access.csv | c163e1f2c64d9e3f76a0d2cc426e70d622ec60b3 | ACL for demo transient model |
| E7 | base_sparse_field/views/views.xml | 1c199e72b7736ef1170bf0de9e929b205950d579 | Adds serialization pointer to model/field technical forms |
| E8 | base_sparse_field/tests/__init__.py | 1dc570533d5d6f4099d65adcb935a1d925179b5c | Test package import list |
| E9 | base_sparse_field/tests/test_sparse_fields.py | 944ff206dc137b8ca61f23e33860b40ce1dba122 | Unit test of sparse round-trip and reflection |

`controllers/__init__.py` returned HTTP 404 at anchor: no controllers package (consistent with E2 importing models only).

## 2. Findings by Card Section

### 2.1 Manifest / dependencies / purpose
1. WHAT: Technical, hidden-category module whose stated purpose is to provide "sparse" fields, i.e. mostly-null attributes whose values are packed into one shared container column instead of one database column each. WHY: stated in manifest as a way around the database's per-table column-count limit. [E1]
2. Sole dependency is the core `base` module; LGPL-3; data files = one ACL file and one view file. No `auto_install`, no assets, no demo data declared. [E1]

### 2.2 Data (models, fields, constraints, serialization semantics)
3. WHAT: A new field type `serialized` is registered into the core field framework; storage is a text column holding a JSON object; in memory it is exposed as a dict (empty dict when null). Non-dict values pass through as-is or become null. It is excluded from default prefetch. [E4 `Serialized`]
4. WHAT: Every field class gains an optional `sparse` parameter naming the container field. When set, the field is forced non-stored, defaults to not-copied (unless explicitly overridden), and becomes a computed field reading its value from the container by key; if not read-only it also gets an inverse that writes back into the container. [E4 `_get_attrs`, `_compute_sparse`, `_inverse_sparse`]
5. Semantics — write: the value is converted to its read/export form (relational values become ids, no display names) before being put into the JSON map; a falsy value removes the key rather than storing null/false. RISK: legitimately-false values (0, 0.0, False, empty string) are indistinguishable from "unset" once stored. [E4 `_inverse_sparse`]
6. Semantics — read: relational sparse values are filtered for existence on read, so references to deleted records silently vanish (no FK / referential integrity at DB level). RISK: no DB-level constraints, indexes, or type checks on sparse values; filtering/sorting/searching on them is not provided by this module (not stored). [E4 `_compute_sparse`; absence of search method in E4]
7. The field-definition registry (`ir.model.fields`) is extended: new type value `serialized` (cascade on uninstall) and a self-referencing pointer `serialization_field_id` restricted by domain to serialized fields of the same model, cascade-deleted with the container. [E5 `IrModelFields`]
8. Constraint: once a registry field is linked to a container, changing its storage pointer or renaming it raises a user error ("not allowed"). [E5 `write`]
9. Reflection: after core field reflection, the module synchronizes the container pointer in the registry for every field of the reflected models using direct SQL, then triggers recompute notifications; a missing container field raises a user error naming the sparse field. [E5 `_reflect_fields`]
10. Custom (manual) fields: when instantiating registry-defined fields, a populated container pointer is translated into the `sparse` attribute, so admin-created custom fields can also be sparse. [E5 `_instanciate_attrs`]
11. `base` abstract model accepts `sparse` as a valid field parameter (suppresses unknown-parameter warnings). [E5 `Base`]
12. Demo/test transient model `sparse_fields.test` holds one container and six sparse fields (boolean, integer, float, char, selection, many2one to partner). [E5]

### 2.3 Business rules / states / exceptions
13. No business workflow or states. Exceptions are limited to: storage-change forbidden, rename forbidden, container-not-found during reflection (all user errors). [E5]
14. Tests assert: empty container initially; incremental set/unset of each sparse field grows/shrinks the JSON map key-by-key; registry reflects all sparse fields pointing to the container named `data`. [E9]

### 2.4 Security
15. ACL: only the system-administrator group has read/write/create on the demo transient model; unlink not granted. No record rules, no new groups. [E6]
16. Reflection writes bypass ORM access checks by using raw SQL (runs in module-load context). No explicit `sudo` calls. [E5 `_reflect_fields`]
17. RISK (source-visible, not runtime-proven): sparse values inherit the access of the container field; field-level `groups` on an individual sparse field does not isolate data already readable through the container. Inference only — not asserted by source comments.

### 2.5 UI surfaces (names only)
18. Technical model form and technical field form each gain a "Serialization Field" selector, read-only for base (non-custom) fields, no quick-create. [E7 `model_form_view`, `field_form_view`] No menus, actions, routes, or settings fields.

### 2.6 Jobs / config
19. None: no cron, config parameters, external services, or assets. [E1, E4, E5]

## 3. Cross-module edges
- Monkey-patches the core field framework globally (all models in the registry see the `sparse` parameter and the `Serialized` type once installed). [E4]
- Extends core `ir.model.fields` and inherits core technical views `base.view_model_form`, `base.view_model_fields_form`. [E5, E7]
- Demo model references `res.partner`. [E5]
- Downstream consumers (which other addons declare sparse/serialized fields) not enumerated in this pass — outside module scope.

## 4. Evidence gaps / contradictions
- G1: Consumers of sparse fields across the 19.0 tree not inventoried (would need repository-wide search; api.github.com blocked).
- G2: Source observation (not a runtime claim): in the registry `write` override, the rename check indexes the incoming `name` key even when only the storage-pointer key was supplied; if an unchanged pointer is written alone on a sparse field, this path appears liable to a key lookup failure. Flag for A1/Proof; not verified.
- G3: No search/order support for sparse fields is visible in this module; whether core provides any fallback is not examined here.
- G4: Core `fields.Field._get_attrs` and core reflection behavior (being patched) not read in this pass.

## 5. Limitations
- Static source only at the anchor commit; source presence != runtime reachability. No runtime execution, no Formal Coverage, no percentages.
- Files discovered via manifest/`__init__` imports only; any unlisted file in the module directory is not covered.
