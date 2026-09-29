# Source Map (candidate) — `base_sparse_field`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_sparse_field` |
| Display name | Sparse Fields |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `58181e55c888bfa6` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_sparse_field/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Implementation of sparse fields.
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `sparse_fields.test` (Sparse fields Test)
- Objects extended from other modules (2): `base`, `ir.model.fields`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `base`, `ir.model.fields`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — base_sparse_field
Source revision: 19.0.post20260921 | Module: "Sparse Fields", category Hidden, LGPL-3 (base_sparse_field/__manifest__.py:3,11,19). Basis: static reading only.

## A. Capabilities and optionality
- A1. Lets a field be declared "sparse": its value is not held in its own database column but packed with other rarely-filled fields into one shared serialized text container on the same record (structured as a key/value mapping). Stated purpose: get around the database limit on columns per table. base_sparse_field/__manifest__.py:5-10
- A2. Sparse fields are, by default, not stored, not copied on duplication, and are read/written through the container; they are writable unless declared read-only. base_sparse_field/models/fields.py:41-47
- A3. A new "serialized" field type is provided as the container; it is not pre-fetched with the record. base_sparse_field/models/fields.py:78-83
- A4. Writing an empty value removes that field's key from the container; a non-empty value adds or updates it. base_sparse_field/models/fields.py:60-71
- A5. Relational sparse values are re-checked for existence on read (deleted target records drop out). base_sparse_field/models/fields.py:55-57
- A6. Optionality: depends only on base; no auto_install, no settings switch, no group. Manifest has neither auto_install nor application flag. base_sparse_field/__manifest__.py:13 (depends base only; no auto_install key in file).
- A7. Dynamic ("custom") fields can also be made sparse through the field-definition screen, by choosing a container field on the same model. base_sparse_field/models/models.py:22-27; base_sparse_field/views/views.xml:19-29

## B. Objects and relationships
- B1. Extends the base abstract model to accept the "sparse" field parameter. base_sparse_field/models/models.py:9-13
- B2. Extends the field-definition registry (ir.model.fields) with a "serialized" type and a link "serialization_field_id" pointing to the container field of the same model; link removed together with the container (cascade). base_sparse_field/models/models.py:19-27
- B3. During registry reflection, each sparse field's link to its container is synchronised; a sparse field naming a missing container raises a user-facing error. base_sparse_field/models/models.py:41-82 (esp. 65-69)
- B4. Only business-visible object: transient test model "Sparse fields test" (technical demonstration; six sparse attributes in one container). base_sparse_field/models/models.py:92-102
- B5. Lifecycle: no states; container content changes only as sparse fields are written.

## C. Validations, security, multi-company
- C1. Changing the container of an existing sparse field, or renaming a sparse field, is refused with a user error. base_sparse_field/models/models.py:29-39
- C2. Access: only the test model has an access rule; group base.group_system may read/write/create, not delete. base_sparse_field/security/ir.model.access.csv:2
- C3. No record rules, no groups, no company scoping, no audit trail defined here. base_sparse_field/security/ (only the csv file present).
- C4. The link field is read-only in the UI for base-state (module-owned) fields and creation of new containers from that widget is disabled. base_sparse_field/views/views.xml:13,26

## D. Handoffs
- D1. No business handoff. Infrastructure for the ORM/field-definition layer owned by base.
- D2. Test (TEST): create-empty, set/unset each of six types, check the container content and the reflected link to it. base_sparse_field/tests/test_sparse_fields.py:8-40

## E. Configuration/defaults that change outcomes
- E1. No configuration parameters. Behavioural defaults are A2 (not stored / not copied). Sparse values cannot be searched or grouped by the normal column route because they are not stored — UNKNOWN — EVIDENCE INSUFFICIENT (search behaviour of non-stored computed fields not verified in this module).

## F. Effective extension path
- Modules that extend the field-definition registry (ir.model.fields): mail, website (plus this module). Modules extending the base abstract model: base_import, hr, html_editor, mail, phone_validation, sms, transifex, web, web_hierarchy, website (grep of inheritance declarations).
- No other Community module declares a dependency on base_sparse_field (grep of manifests found none) and none uses the sparse parameter or serialized type in production models (grep of sparse=/Serialized( found only this module).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether any Community feature (e.g., custom-field studio-like tools) relies on this module at runtime outside Community.
- UNKNOWN — EVIDENCE INSUFFICIENT: performance/size limits of the container.
- UNKNOWN — EVIDENCE INSUFFICIENT: import/export handling of sparse values.

