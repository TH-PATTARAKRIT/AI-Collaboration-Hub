# G01 PLATFORM_BASE — RED TEAM A2 Review — `base_sparse_field`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional / semantic verifier of A1 conclusions) |
| Group / Module | G01 PLATFORM_BASE / `base_sparse_field` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_SPARSE_FIELD_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `50c2c610f8df71d3f7cbdd6073c24bd02da746933622962f4f6b91322ebca91d` |
| Upstream Lane A packet sha256 | `d18d6476be0cfd2fc1d728ed4814b04e06677f47a23a33ce8ba41a4386b08b9f` (matches the value recorded in the A1 header) |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SPARSE_FIELD_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `2e0e158431d3b32522092d3770f7028acd5d6c6c2616466f45468c5f977895c8` (matches the A1 header; batch W1-B04, ELIGIBLE) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Lane B | None available. See section 5 |
| Date | 2026-09-27 |
| Disposition | **A2 PASS WITH FINDINGS** |

Independence and clean-room note: A2 re-read the source independently at the anchor commit. It did not repair or edit the A1 package or the Lane A packet. This review contains no vendor code. Identifiers appear only as evidence pointers. It answers no QIDs, gives no percentages and makes no Formal Coverage claim.

### Source re-check (A2 independent fetch, `git hash-object`)

| Ref | Path | Blob SHA-1 (A2 computed) | vs Lane A / A1 |
|---|---|---|---|
| E1 | addons/base_sparse_field/__manifest__.py | c487ecfef4f50434826b1df23933f76a3dcd686c | MATCH |
| E4 | addons/base_sparse_field/models/fields.py | cb26946e9e356dee65fe65fca09dbe24fd4373cb | MATCH |
| E5 | addons/base_sparse_field/models/models.py | f219622654de80989f1202226dee84c3ff8caef9 | MATCH |
| E6 | addons/base_sparse_field/security/ir.model.access.csv | c163e1f2c64d9e3f76a0d2cc426e70d622ec60b3 | MATCH |
| E7 | addons/base_sparse_field/views/views.xml | 1c199e72b7736ef1170bf0de9e929b205950d579 | MATCH |
| E9 | addons/base_sparse_field/tests/test_sparse_fields.py | 944ff206dc137b8ca61f23e33860b40ce1dba122 | MATCH |
| — | addons/base_sparse_field/controllers/__init__.py | HTTP 404 | Confirms that there are no controllers (C02) |

The package `__init__` files were re-fetched (HTTP 200). They import only the field patch and the model extensions, which is consistent with E2 and E3.

## 1. Test plan (predeclared before claim review)

| TP | Check | Applies to | Pass rule |
|---|---|---|---|
| TP1 | Lineage: recompute the sha256 of the A1 package, Lane A packet and bank, and compare with the A1 header | Header | Every hash matches |
| TP2 | Blob integrity: re-fetch every cited source file and compare its `git hash-object` with Lane A | E1–E9 | Every blob matches |
| TP3 | Independent semantic re-read of every HIGH claim against the source text | C01–C05, C07–C15 | The claim statement is literally supported, and any scope qualifier is accurate |
| TP4 | Contradiction and CRQ deep read. C10: rename-guard condition versus the keys actually present. C11: guard behaviour for attach and detach. C06: container encode/decode path, including non-object content | C06, C10, C11, CON-SPRS-01/02 | A2 traces the same path independently, and reaches the same conclusion or records a divergence |
| TP5 | Inference claims: confirm that the module-level premise exists, and separate the premise from its runtime consequence | C16, C17 | The premise is verified. The consequence is routed to Proof |
| TP6 | Business-meaning review for SaaS extensible storage: tenant custom attributes, reporting, integrity, access, lifecycle | All | Overclaims and omissions are recorded |
| TP7 | Bank topic lens (used only for topics, no QIDs answered) to find areas A1 did not address | Section 4 | Each omission is recorded with evidence or marked as unexamined |
| TP8 | Lane B classification and Proof requirements for inherently runtime claims only | Sections 5–6 | Each proof item states an expected result and a fail condition |

## 2. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 independent basis / note |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The manifest states the column-limit purpose, the Hidden category and a JSON-map container. The field-type registration patches core globally. |
| C02 | HIGH | VERIFIED | The only dependency is `base`. There are two data files. The controllers package returns 404. No cron, parameters or external calls appear in E4 or E5. |
| C03 | HIGH | VERIFIED | The attribute resolution forces non-stored, sets copy to false only when copy is not already given, attaches the sparse compute, and attaches the inverse only when the field is not read-only. `sparse` is accepted as a valid parameter on the base abstract model. |
| C04 | HIGH | VERIFIED | The write path converts the value to its read form. A truthy value is placed under the field-name key, and a falsy value removes the key. The map is written back only when it has changed. The in-module test uses a false write as "unset", which confirms that this is intended design. |
| C05 | HIGH | VERIFIED | Relational values are stored in id form without display names. On read they are filtered for existence. Being non-stored, they have no DB constraint, index or type check. |
| C06 | MED | VERIFIED (with extension, see SF-2) | Encode: a dict is JSON-encoded, and any other value passes through, or becomes null when falsy. Decode: the stored text is parsed with an empty-map fallback for null only, and has no error handling. |
| C07 | HIGH | VERIFIED | The container type disables default prefetch. |
| C08 | HIGH | PARTIAL | Verified: the `serialized` type is added with cascade-on-uninstall, and the pointer is cascade-deleted with its container. Overclaim: "limited to containers on the same model" is expressed only as a selection **domain** on the pointer field. The module has no server-side constraint that enforces it (see SF-1). |
| C09 | HIGH | VERIFIED | The write override refuses a pointer change and refuses a rename of a field that has a pointer. The in-code comment records this as a known limitation. The WHY (key = field name) is independently supported because the compute and inverse key by the field's own name. |
| C10 | HIGH (source path) | VERIFIED (source path). Runtime reachability is OPEN | Independent trace: the outer condition passes when either key is present. The rename test then reads the incoming name without checking that it is present. If the payload carries only the pointer (unchanged) and the field is sparse, the lookup fails as a missing-key technical error, not a user error. The failure does not occur when the field is not sparse, or when the name is present. CON-SPRS-01 is upheld. |
| C11 | HIGH | VERIFIED | The comparison is current pointer id versus requested value. A none→set change (attach) and a set→none change (detach) both differ, so both are refused. Create is not overridden, so the pointer can be set only at creation. CON-SPRS-02 is upheld: the help text under-describes the rule (and see SF-4 for the UI). |
| C12 | HIGH | VERIFIED | After the core reflection runs, the module reads existing rows and computes the target pointer from the code declaration. Only differing rows are updated, grouped by value, with raw SQL. A modified-notification is deferred to post-init. A missing container raises a user error naming both fields. Raw SQL bypasses ORM access checks and the write guard (see SF-5). |
| C13 | HIGH | VERIFIED | Registry-defined (manual) fields with a populated pointer get `sparse` set to the pointed container's name. The target model is not checked (ties to SF-1). |
| C14 | HIGH | VERIFIED | Both inherited technical forms add the selector as read-only when the field state is base, with quick-create disabled. |
| C15 | HIGH | VERIFIED | One ACL row: the system group gets read/write/create, and unlink is 0. There are no other data files, so no groups or rules are added. |
| C16 | LOW (inference) | PARTIAL | Premise verified: the module has no per-key access logic, and the demo container has no group restriction. Consequence (sibling exposure through the container or through export) is runtime-dependent. Routed to PR-SPRS-05. |
| C17 | MED (inference) | PARTIAL | Premise verified: whole-map read-modify-write, with no merge or version logic. Whether a lost update occurs depends on core transaction isolation, which was not examined (GAP-6). Routed to PR-SPRS-04. |
| C18 | MED | VERIFIED (module scope) | The module defines no search or ordering method for sparse attributes. Any core fallback remains GAP-3. |
| C19 | MED | VERIFIED | One test: incremental set and unset with truthy values only, plus a reflection check. It does not test zero values, rename, storage change, concurrency or malformed payloads. |

Verdict counts: VERIFIED 16, PARTIAL 3, NOT_VERIFIED 0, OUT_OF_SCOPE 0.

A1 business rules: BR1, BR2, BR3 and BR4 are supported. BR5 is only PARTIAL, because the same-model rule is a UI/selection domain and is not an enforced invariant (SF-1). A1 contradictions: CON-SPRS-01 is upheld as a source-path contradiction. CON-SPRS-02 is upheld as under-described wording.

## 3. Semantic findings (A2)

- **SF-1 (overclaim, C08/BR5) — same-model limit is advisory.** The pointer's same-model restriction exists only as a domain on the relational field and in the form views. The module's write override checks change, not target validity, and there is no constraint method. A manual field whose pointer targets a container on another model would get a `sparse` name (C13) that may not exist on its own model. Setup-time behaviour for that case is not visible in module scope. Business meaning: for tenant-configurable custom attributes, the integrity rule depends on the UI, not on the server.
- **SF-2 (extension, C06/X5) — non-object content fails later and differently.** Two cases exist. Malformed text fails at decode, as A1 says. Well-formed JSON that is not an object (for example a list or a scalar) decodes without error, and the failure moves to the sparse read, which expects a key/value map. A string value written to the container is also passed through to storage without any check that it is valid JSON. So any caller able to write the container field directly can store content that later breaks every sparse read on that record. X5 should cover both failure points.
- **SF-3 (C10 reachability framing).** The defect needs a payload that carries the pointer key without the name key, on a field that already has a pointer. Candidate callers are external RPC, data import of field metadata, and module data files that re-state the pointer. A2 did not verify whether the standard form client sends unchanged values. A1 correctly left reachability open.
- **SF-4 (UI/server divergence, C11/C14).** The selector is read-only only for base-state fields. On an existing custom (manual) field it stays editable in the form, but the server refuses any change on save. The UI therefore offers an action that the server always rejects after creation. This is consistent with CON-SPRS-02.
- **SF-5 (C12/BR1 scope).** "Storage mode is fixed at creation" holds for ORM metadata writes only. Reflection at module load or upgrade rewrites pointers with raw SQL to match the code declaration, without going through the guard. So code changes can re-point or detach code-defined fields during an upgrade. A1's BR1 wording ("through metadata writes") is accurate, but the upgrade path is a controlled bypass that downstream design should know about. Because the sync touches only differing rows, the static evidence supports reflection idempotency (CRQ-SPRS-07). This is not runtime-proven.
- **SF-6 (new, cache coherence — unverified).** The module attaches the compute to sparse fields without declaring any dependency on the container field. Whether the core infers a dependency (so that writing the container directly invalidates the cached sparse values) was not examined. This is flagged as a candidate only, under GAP-4, and routed to PR-SPRS-08.
- **SF-7 (business meaning, SaaS extensible storage).** A1's RISK set is materially correct for tenant-defined attributes. Zero/false collapse to "unset" (C04). Dangling references are silent (C05). There is no search or sort (C18). Sibling values are exposed through the shared container (C16). Duplicates do not copy these values (C03). For an SME ERP these affect reporting (values cannot be filtered or grouped), quantity/flag semantics (a legitimate 0 or No is lost), and audit (C04 plus whole-map rewrite). A1 does not overclaim these, and it labels C16 and C17 as inference.

## 4. Omissions (A1 did not address; bank used as topic lens only)

- **OM-1 — orphaned keys on attribute removal.** The module has no unlink override or cleanup. Deleting a sparse attribute's definition leaves its key in every record's container. Because rewrites preserve the whole map, the key is carried forward indefinitely (static: only `write` and reflection are overridden in E5).
- **OM-2 — extra/injected keys.** A sparse read looks up only its own name, so unknown keys never become active attributes. But the container accepts any map on write, and no per-key validation happens, so a direct container write (API or import) can inject arbitrary keys and value types. This relates to GAP-5 (import/export).
- **OM-3 — decode failure blast radius.** A single corrupt container makes every sparse attribute on that record unreadable, not just one attribute (SF-2 combined with the shared-container design). No diagnostic separates "absent" from "corrupt".
- **OM-4 — uninstall data effect.** A1 C08 notes cascade on metadata. The effect on stored container columns and on dependent addons at uninstall was not examined. This is left as a gap, not a claim.
- **OM-5 — test gap for zero values.** C19 lists missing tests but not the absence of any zero/false-value test. That absence matters because C04 is the main semantic risk.

## 5. Lane B classification

There is no Lane B Evidence Pool for this module. None of the claims is FAIL on Lane B grounds.

| Claims | Classification | Reason |
|---|---|---|
| C01, C02, C03, C07, C08, C09, C11, C12, C13, C15, C18, C19 | NOT_APPLICABLE | These are structural, metadata or source-inventory claims with no normal-user surface. |
| C04, C05, C06, C10, C14, C16, C17 | UNCORROBORATED | Their behaviour could be observed on a runtime surface (technical forms, record values, errors), but there is no Lane B evidence. |

## 6. Proof requirements (inherently runtime claims only)

| PR | Claim | Falsifiable test (isolated test database) | Expected (claim holds) | Fail condition (claim falsified) |
|---|---|---|---|---|
| PR-SPRS-01 | C10 / CON-SPRS-01 | As an admin via RPC, write only the unchanged pointer value to the metadata record of an existing sparse field | Technical missing-key error (not a user/validation error), transaction rolled back | A controlled user error, or the write succeeds |
| PR-SPRS-02 | C04 | Write integer 0, float 0.0 and boolean false to sparse attributes that previously held truthy values, then read them back and inspect the container | Keys removed. Read-back is identical to a never-set attribute | A key is kept with a falsy value, or the read-back differs from unset |
| PR-SPRS-03 | C06, SF-2 | Put (a) non-JSON text and (b) a JSON list into the container of a test record, then read one sparse attribute | (a) decode error; (b) error at sparse read. Neither case degrades to empty | A read returns empty or default values silently, or returns partial values |
| PR-SPRS-04 | C17 | Two concurrent transactions each write a different sparse attribute on the same record | One transaction is refused or retried by core concurrency control, and after retry both values are present | Both commit and one value is silently missing |
| PR-SPRS-05 | C16 | Restrict one sparse attribute to a group, then read the container field and export it as a user outside that group | The restricted value is visible through the container (claim holds) | The value is not reachable through the container or export |
| PR-SPRS-06 | C11 / SF-4 | On an existing manual field, attach a container through the form, then detach one from a sparse manual field | Both saves are refused with the storage-change user error | Either change is saved |
| PR-SPRS-07 | C12 / SF-5 | Upgrade the module twice with no code change, capturing the pointer values and the count of updated rows | Second run updates zero rows. The pointers are unchanged | Any pointer changes, or rows are rewritten on the second run |
| PR-SPRS-08 | SF-6 | In one transaction, write the container directly with a new value for a key, then read the matching sparse attribute | The attribute returns the new value | A stale value is returned |
| PR-SPRS-09 | C18 | Search, filter and order records by a sparse attribute, in the UI and through the API | Refused or explicitly unsupported (a clear error or non-searchable marker) | Silently empty or wrong results presented as valid |

Proof requirement count: 9.

## 7. Limitations

- This is static review at one anchor commit. Source presence does not establish runtime reachability. No runtime execution was performed.
- Core field attribute resolution, core reflection, transaction isolation and core search fallback were not read (A1 GAP-3, GAP-4 and GAP-6 remain open). SF-6 is a candidate only.
- The bank was used only as a topic lens. No QIDs were answered, and nothing was edited.
- The re-fetched source is held only in the session scratchpad and is not reproduced here. This review makes no Formal Coverage claim and gives no percentages.
