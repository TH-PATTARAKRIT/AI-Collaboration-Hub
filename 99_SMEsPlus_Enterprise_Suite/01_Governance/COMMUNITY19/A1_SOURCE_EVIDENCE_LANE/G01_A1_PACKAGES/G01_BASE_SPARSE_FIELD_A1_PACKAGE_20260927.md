# G01 PLATFORM_BASE — RED TEAM A1 Package — `base_sparse_field`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `base_sparse_field` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_SPARSE_FIELD_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `d18d6476be0cfd2fc1d728ed4814b04e06677f47a23a33ce8ba41a4386b08b9f` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/base_sparse_field/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SPARSE_FIELD_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `2e0e1584…95c8`, matches `FREEZE_W1-B04.json`) |
| Freeze | batch W1-B04, freeze hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B, and no runtime evidence was used |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: the claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. Nothing here recommends reusing the vendor's schema, ORM, workflow, UI or naming. No QIDs are answered. The bank was used only as a topic lens: coupling of attributes in shared storage, false-vs-absent semantics, referential integrity, change control over rename and storage, access isolation, concurrency, malformed content, search and sort, and reflection idempotency.

Evidence key (blob SHA-1 from Lane A): E1 `__manifest__.py` c487ecfe…; E4 `models/fields.py` cb26946e…; E5 `models/models.py` f2196226…; E6 `security/ir.model.access.csv` c163e1f2…; E7 `views/views.xml` 1c199e72…; E9 `tests/test_sparse_fields.py` 944ff206…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-SPRS-C01 | WHAT: A hidden technical module lets many mostly-empty attributes share one text container holding a JSON map, instead of one column each. WHY: to get around the database limit on columns per table. RISK: the optimisation is platform-wide once the module is installed. | E1; E4 (spot-check S1, S2) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C02 | WHAT: The only dependency is the core base module. There are no controllers, cron jobs, config parameters or external services. | E1 (S1); Lane A 404 on controllers | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C03 | WHAT: The module globally patches the core field definition, so any field on any model can name a container. Such a field is forced non-stored, becomes computed from the container, is writable back only when not read-only, and is non-copied by default unless the field says otherwise. RISK: behaviour changes across the whole registry, not just inside this module. | E4 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C04 | WHAT: When a value is written, the whole container map is read, one key is changed, and the whole map is written back. A falsy value (false, 0, 0.0, empty) removes the key instead of storing it. RISK: a legitimately-zero or false value cannot be told apart from "never set". | E4 inverse (S2) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C05 | WHAT: A relational value is stored as a bare id. On read it is filtered for existence, so a reference to a deleted record silently reads as empty. There is no database-level referential integrity, index or type check. RISK: dangling ids stay hidden in the stored payload. | E4 compute/inverse (S2) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C06 | WHAT: The container type turns a dict into JSON on write. Any other value passes through unchanged, or becomes null when falsy. On read, the stored text is decoded with no visible guard. RISK: a non-dict or malformed payload can reach storage, and a malformed payload would raise on read instead of degrading safely. | E4 `Serialized` (S2) | MED | SOURCE-STATIC |
| A1-G01-SPRS-C07 | WHAT: The container is excluded from default prefetch. | E4 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C08 | WHAT: The field-metadata registry gains a new type (cascade on uninstall) and a pointer from a field to its container. The pointer is limited to containers on the same model and is cascade-deleted with the container. RISK: uninstalling or deleting a container definition cascades to the definitions of its dependent attributes. | E5 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C09 | WHAT: A metadata write that changes the container pointer is refused, and so is renaming a field that has a container. WHY: the stored key is the field name, so a rename would orphan the historical values. The help text says the pointer "cannot be changed after creation". | E5 `write`, field help (S3) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C10 | WHAT: The rename guard runs whenever the pointer key OR the name key is in the write payload. For a field that has a container, it reads the incoming name even when only the (unchanged) pointer was supplied. RISK: that payload shape would hit a missing-key failure (a technical error, not a controlled refusal). | E5 `write` (S3) | HIGH (source path) | SOURCE-STATIC — **CONTRADICTION CONFIRMED-FROM-SOURCE** (runtime reachability unproven) |
| A1-G01-SPRS-C11 | WHAT: The storage-change guard compares the current pointer with the requested one. So attaching a container to an existing non-sparse field, or detaching one, is refused as well. Storage mode is effectively fixed at creation. | E5 `write` (S3) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C12 | WHAT: After core reflection, the container pointers of every field on the reflected models are synchronised with direct SQL. Only rows whose value differs are updated, and recompute notifications follow. A missing container raises a user error that names the field. WHY: the container must be reflected before its dependants. RISK: this bypasses ORM access checks and audit (it runs in module-load context). | E5 `_reflect_fields` (S3) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C13 | WHAT: Admin-created custom fields become sparse when their metadata carries a container pointer. So the feature is reachable through runtime customisation, not just through code. | E5 `_instanciate_attrs` (S3) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C14 | WHAT: On both technical forms (model and field), the "Serialization Field" selector is read-only for base (non-custom) fields and does not allow quick-create. | E7 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C15 | WHAT: Only system administrators get read/write/create on the demo transient model. Unlink is not granted. No groups or record rules are added. | E6 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-SPRS-C16 | RISK (inference): sparse values share one physical container, so a user who can read or write the container can reach every sibling value. A per-attribute group restriction does not isolate data that is already exposed through the container. | E4, E5 (no per-key access logic) | LOW | SOURCE-STATIC (inference) |
| A1-G01-SPRS-C17 | RISK (inference): every write rewrites the whole map, so two concurrent writes to different attributes on the same record rely on core row-level concurrency control to avoid lost updates. The module adds no merge logic. | E4 inverse (S2) | MED | SOURCE-STATIC (inference) |
| A1-G01-SPRS-C18 | WHAT: The module provides no search or sort support for sparse attributes (they are non-stored computed fields and no search method is defined). | E4 (S2) | MED | SOURCE-STATIC |
| A1-G01-SPRS-C19 | WHAT: The in-module test covers only incremental set/unset on a demo model and reflection of the container link. There is no test for rename, storage change, concurrency or malformed payloads. | E9 (Lane A) | MED | SOURCE-STATIC |

## 2. Business rules
- BR1: Storage mode (container or own column) is decided when a field is created and cannot be changed later through metadata writes (C09, C11).
- BR2: A field that has a container cannot be renamed (C09).
- BR3: An absent key, a falsy value and "unset" all mean the same thing (C04).
- BR4: Unless the field says otherwise, duplicating a record does not copy sparse values (C03).
- BR5: A sparse attribute and its container must belong to the same model (C08).

## 3. States / transitions
- There is no business workflow. The only lifecycle is at the metadata level: a field is defined with or without a container, and its container link can only go from none to linked at creation (C11). Removing the container cascades to its dependants (C08).
- Per-record key lifecycle: absent → present (truthy write) → absent (falsy write). Re-adding a key produces a fresh entry (C04, E9).

## 4. Exceptions / failure modes
- X1: Storage-change refusal (user error) (C11).
- X2: Rename refusal (user error) (C09).
- X3: Missing-key failure when an unchanged pointer is written without a name (C10). Candidate technical error.
- X4: Container not found during reflection (user error) blocks loading the model (C12).
- X5: Decoding a malformed stored payload raises on read (C06). No safe-degrade path is visible.
- X6: A deleted related record silently reads as empty (C05). Nothing is surfaced.

## 5. Cross-module handoffs
- H1: The core field framework is globally patched (E4). Every addon that declares a sparse or serialized field depends on this module.
- H2: The module extends core field-metadata reflection and inherits the core technical model and field forms (E5, E7).
- H3: The demo model references the core partner entity (E5).
- H4: Downstream consumers are not inventoried (see GAP-1).

## 6. Evidence gaps (Lane A gaps carried forward)
- GAP-1 (Lane A G1): Consumers of sparse or serialized fields across the 19.0 tree are not inventoried.
- GAP-2 (Lane A G2): Resolved statically by spot-check S3 as C10. Runtime reachability (which caller would send that payload shape) is still unproven.
- GAP-3 (Lane A G3): It is not examined whether the core offers any fallback for search, sort or group-by on non-stored computed fields.
- GAP-4 (Lane A G4): The core field attribute resolution and core reflection that this module patches were not read.
- GAP-5 (new): How export and import treat the raw container versus individual attributes was not examined.
- GAP-6 (new): Core row-level concurrency behaviour for whole-container rewrites was not examined (C17).

## 7. CRQ candidates
- CRQ-SPRS-01: Show at runtime whether writing only an unchanged container pointer on a sparse field gives a technical error instead of a controlled refusal (C10).
- CRQ-SPRS-02: Show whether zero or false values on sparse numeric or boolean attributes are lost, and whether they read back the same as "unset" (C04).
- CRQ-SPRS-03: Show whether concurrent writes to two different sparse attributes on one record lose either value (C17).
- CRQ-SPRS-04: Show whether a user limited from one sparse attribute can read or write it through the container or through export (C16, GAP-5).
- CRQ-SPRS-05: Show how the system behaves when the container holds malformed or non-map content (C06).
- CRQ-SPRS-06: Show whether search, filter or sort on a sparse attribute is refused, empty or wrong (C18, GAP-3).
- CRQ-SPRS-07: Show whether repeating reflection or upgrading is idempotent and never re-points existing values (C12).

## 8. Contradictions
- CON-SPRS-01 **CONFIRMED-FROM-SOURCE** (S3): the guard's stated intent is to refuse renames in a controlled way, but the code path reads the incoming name even when none is supplied (C10). Runtime reachability has not been proven.
- CON-SPRS-02 CANDIDATE: the help text says only the pointer "cannot be changed after creation", but the guard also refuses attaching a container to an existing field (C11). This is consistent in effect, but the wording under-describes it.

## 9. Spot-check log
Files re-fetched from `raw.githubusercontent.com/odoo/odoo/8d05257d…/addons/base_sparse_field/<path>`. Every fetch returned HTTP 200, and `git hash-object` was compared with the Lane A blob.

| # | File | Lane A blob | Computed blob | Result | Claims verified |
|---|---|---|---|---|---|
| S1 | `__manifest__.py` | c487ecfe… | c487ecfef4f50434826b1df23933f76a3dcd686c | MATCH | C01, C02: base-only dependency, two data files, stated column-limit purpose |
| S2 | `models/fields.py` | cb26946e… | cb26946e9e356dee65fe65fca09dbe24fd4373cb | MATCH | C03–C07, C17, C18: forced non-store/non-copy, falsy removes key, existence filter, unguarded decode, no prefetch |
| S3 | `models/models.py` | f2196226… | f219622654de80989f1202226dee84c3ff8caef9 | MATCH | C08–C13: pointer domain/cascade; guard condition reads the name key unconditionally for sparse fields; raw-SQL reflection; custom-field path |
| S4 | `security/ir.model.access.csv`, `views/views.xml` | c163e1f2…, 1c199e72… | c163e1f2c64d9e3f76a0d2cc426e70d622ec60b3, 1c199e72b7736ef1170bf0de9e929b205950d579 | MATCH | C14, C15 |

Refinements to Lane A: item 3 ("non-dict values pass through") is sharpened to C06, since decoding has no guard. Item 8 is sharpened to C11, since attaching a container after creation is also refused.

## 10. Provenance
- The only input is the Lane A packet (sha256 above), plus spot-check re-fetches at the anchor commit. Re-fetched copies are held only in the session scratchpad.
- The GMVQ bank was used as a topic lens only. Its hash was verified against `FREEZE_W1-B04.json`. No QID was answered and nothing was edited.

## 11. Limitations
- This is static source at one anchor commit. Source presence does not mean runtime reachability, and no runtime execution took place. This is not Formal Coverage and gives no percentages.
- C16 and C17 are inferences with no direct source assertion.
- Core files that the module patches were not read (GAP-4).
