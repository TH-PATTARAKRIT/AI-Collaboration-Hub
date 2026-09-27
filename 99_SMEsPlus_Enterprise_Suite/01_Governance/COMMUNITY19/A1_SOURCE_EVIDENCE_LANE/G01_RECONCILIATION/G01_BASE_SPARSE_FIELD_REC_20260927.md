# G01 PLATFORM_BASE — Module `base_sparse_field` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `base_sparse_field` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/base_sparse_field/`) |
| Frozen bank (lineage lens only) | W1-B04 `G01_BASE_SPARSE_FIELD_GMVQ_MVQ_40_V1.00_DRAFT.md` — 41 QIDs (G01-BASE_SPARSE_FIELD-Q001..Q041) |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_BASE_SPARSE_FIELD_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (24 REC items; 1 CONTRADICTION and 7 UNKNOWN_PENDING_PROOF carried to Proof) |

Format reference: at intake (about 15:02Z) `G01_RECONCILIATION/` did not exist. `G01_BUS_REC_20260927.md` appeared at about 15:04Z while this stage was running. This document follows its section structure.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_SPARSE_FIELD_LANE_A_PASS1_20260927.md` | `d18d6476be0cfd2fc1d728ed4814b04e06677f47a23a33ce8ba41a4386b08b9f` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_SPARSE_FIELD_A1_PACKAGE_20260927.md` | `50c2c610f8df71d3f7cbdd6073c24bd02da746933622962f4f6b91322ebca91d` | Equals the value recorded in the A2 header. 19 claims (C01–C19) |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_BASE_SPARSE_FIELD_A2_REVIEW_20260927.md` | `b50478d63b806e827dfb561cc784bf6d4208dca568e7f37e3060531c640ee42a` | A2 PASS WITH FINDINGS: 16 VERIFIED, 3 PARTIAL; SF-1..SF-7; OM-1..OM-5; 9 proof requirements (PR-SPRS-01..09) |
| Frozen bank | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SPARSE_FIELD_GMVQ_MVQ_40_V1.00_DRAFT.md` | `2e0e158431d3b32522092d3770f7028acd5d6c6c2616466f45468c5f977895c8` | Equals the `FREEZE_W1-B04.json` bank_files entry |
| Freeze hash | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B04.json` (file sha256 `27db90332c140e569d4ab7f3a6d2fe7f5d0aae5f375065b5ab2ffe2d95f4d4f9`) | `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` | Recomputed with the `freeze_batch.py` formula (batch, sorted modules, sorted file:sha256). MATCH. All 4 bank files re-hashed: MATCH |

The inputs were only read. None was edited, and no git operations were run.

## 3. Lane B evidence-pool search (recorded)

- Scope: the whole repository tree (`.git` excluded), searched 2026-09-27T15:02:28Z.
- Path search (`*lane_b*`, `*laneb*`, `*LANE-B*`, `*evidence_pool*`, case-insensitive): 0 hits.
- Content search: files that mention `base_sparse_field` / `google_recaptcha` AND "Lane B". There were 10 hits. All of them are the Lane A packets, A1 packages, A2 reviews, GMVQ banks or the W1-B04 authoring checkpoint, and each says that Lane B was not viewed or not started. None is a runtime observation record.
- `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md` records the runtime device as OFFLINE since 2026-09-24T12:53Z.
- Scratch log: `laneb_search.txt`, sha256 `e5b891c5ea8e32c876d11ac484a0c5ae6a69db5871e836b2f76d826cf127b135`.
- **Result: no Lane B runtime evidence exists for `base_sparse_field`.** The Lane B column uses UNCORROBORATED (observable at runtime, not observed) or NOT_APPLICABLE (structural or metadata item). An item is never marked FAIL because Lane B evidence is absent.

## 4. Classification rules applied

| Class | Rule |
|---|---|
| MATCH | A2 VERIFIED the A1 claim on WHAT and WHY/RISK, and no A2 runtime proof requirement is needed to hold it |
| GAP | A2 PARTIAL or extension where the A1 framing is incomplete, or an A2 omission or semantic finding promoted to a new REC item |
| CONTRADICTION | A2, citing source, directly contradicts an A1 statement |
| UNKNOWN_PENDING_PROOF | A2 VERIFIED the source fact (or premise), but the conclusion is behavioural and A2 requires runtime proof |

## 5. Reconciliation table

C01–C19 are the A1 claims `A1-G01-SPRS-Cnn`. SF and OM items are A2 findings promoted to REC items. The QID mapping is lineage only, by topical fit to the frozen bank. **No QID is answered.** QIDs are written `sparse+Qnnn` = `G01-BASE_SPARSE_FIELD-Qnnn`.

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+QID lineage |
|---|---|---|---|---|---|---|---|
| REC-SPRS-01 | C01 | Hidden module packs mostly-empty attributes into one JSON-map text container, to avoid the column limit. The effect is platform-wide | VERIFIED | MATCH | NOT_APPLICABLE | PC-SPRS-01 (lineage) | sparse+Q001, sparse+Q040 |
| REC-SPRS-02 | C02 | Depends only on base. No controllers, cron, parameters or external services | VERIFIED (controllers 404) | MATCH | NOT_APPLICABLE | PC-SPRS-01 | — (no clear fit) |
| REC-SPRS-03 | C03 (+BR4) | Global field patch: the field is forced non-stored and computed from the container, has an inverse only when not read-only, and is not copied by default | VERIFIED | MATCH | NOT_APPLICABLE | PC-SPRS-10 | sparse+Q005, sparse+Q040 |
| REC-SPRS-04 | C04 (+BR3) | Whole map read-modify-write. A falsy value removes the key, so zero/false cannot be told apart from unset | VERIFIED. The in-module test uses false as "unset" | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-SPRS-02 / PC-SPRS-14 (PR-SPRS-02) | sparse+Q002, sparse+Q003, sparse+Q037 |
| REC-SPRS-05 | C05 | Relational values are stored as bare ids and filtered for existence on read. Dangling ids are hidden. No DB integrity, index or type check | VERIFIED | MATCH | UNCORROBORATED | — (no A2 PR) | sparse+Q004, sparse+Q036 |
| REC-SPRS-06 | C06 + SF-2 + OM-3 | A dict is JSON-encoded, anything else passes through (null if falsy). Decode has no guard, so malformed content raises on read | VERIFIED **with extension**: well-formed non-map JSON (a list or scalar) decodes and then fails at the sparse read. A string is stored without a JSON validity check. One corrupt container makes every sparse attribute on the record unreadable, and "corrupt" cannot be told apart from "absent" | GAP | UNCORROBORATED | PC-SPRS-03 / PC-SPRS-15 (PR-SPRS-03) | sparse+Q013, sparse+Q028 |
| REC-SPRS-07 | C07 | The container is excluded from default prefetch | VERIFIED | MATCH | NOT_APPLICABLE | — | — (no clear fit) |
| REC-SPRS-08 | C08 (+BR5) + SF-1 | Adds a metadata type (cascade on uninstall) and a pointer "limited to containers on the same model", cascade-deleted with the container | PARTIAL. **Overclaim**: the same-model limit exists only as a UI/selection domain. There is no server-side constraint, so a manual field can point to a container on another model (C13 does not check the target) | CONTRADICTION | NOT_APPLICABLE | PC-SPRS-06 | sparse+Q008, sparse+Q009 |
| REC-SPRS-09 | C09 (+BR2) | Changing the pointer and renaming a field that has a container are both refused. WHY: the stored key is the field name | VERIFIED | MATCH | NOT_APPLICABLE | PC-SPRS-05 | sparse+Q007 |
| REC-SPRS-10 | C10 / CON-SPRS-01 + SF-3 | The rename guard reads the incoming name even when only an unchanged pointer is supplied, giving a missing-key technical error | VERIFIED (source path). Runtime reachability is OPEN. Candidate callers: RPC, metadata import, module data | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-SPRS-04 / PC-SPRS-13 (PR-SPRS-01) | sparse+Q006, sparse+Q007 |
| REC-SPRS-11 | C11 + CON-SPRS-02 + SF-4 | Attaching or detaching a container after creation is refused. Storage mode is fixed at creation. The help text under-describes this | VERIFIED. UI/server divergence: on a manual field the selector stays editable, but the server refuses the save | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-SPRS-05 / PC-SPRS-18 (PR-SPRS-06) | sparse+Q006 |
| REC-SPRS-12 | C12 + SF-5 | Reflection syncs pointers with raw SQL, only for rows that differ. A missing container raises a user error. ORM access/audit is bypassed | VERIFIED. Refinement: upgrades can re-point or detach code-defined fields by bypassing the write guard. Static evidence supports idempotency | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-SPRS-09 / PC-SPRS-19 (PR-SPRS-07) | sparse+Q008, sparse+Q038, sparse+Q039 |
| REC-SPRS-13 | C13 | Admin-created custom fields become sparse through the pointer, so the feature can be reached through runtime customisation | VERIFIED. The target model is not checked (ties to REC-SPRS-08) | MATCH | NOT_APPLICABLE | — | sparse+Q009 |
| REC-SPRS-14 | C14 | On the technical forms the selector is read-only for base fields, with no quick-create | VERIFIED | MATCH | UNCORROBORATED | PC-SPRS-11 | sparse+Q006, sparse+Q009 |
| REC-SPRS-15 | C15 | Demo model ACL: system group read/write/create, no unlink. No groups or rules | VERIFIED | MATCH | NOT_APPLICABLE | PC-SPRS-11 | — (no clear fit; demo model) |
| REC-SPRS-16 | C16 (inference) | Sibling values are reachable through the shared container, so a per-attribute group does not isolate them | PARTIAL. The premise (no per-key access logic) is verified. The consequence is runtime-dependent | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-SPRS-17 (PR-SPRS-05) | sparse+Q016, sparse+Q017, sparse+Q018 |
| REC-SPRS-17 | C17 (inference) | A whole-map rewrite relies on core row-level concurrency to avoid lost updates. No merge logic | PARTIAL. The premise is verified. Core isolation was not examined (GAP-6) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-SPRS-16 (PR-SPRS-04) | sparse+Q010, sparse+Q011, sparse+Q031 |
| REC-SPRS-18 | C18 | The module gives no search or sort support for sparse attributes | VERIFIED (module scope). The core fallback remains GAP-3 | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-SPRS-10 / PC-SPRS-21 (PR-SPRS-09) | sparse+Q020, sparse+Q021 |
| REC-SPRS-19 | C19 + OM-5 | The test covers only set/unset of truthy values and reflection | VERIFIED. Addition: there is no zero/false-value test, which matters most because of C04 | MATCH | NOT_APPLICABLE | PC-SPRS-12 | sparse+Q003 |
| REC-SPRS-20 | SF-6 (A2 new) | — (not addressed) | Cache coherence candidate: no dependency on the container is declared for the sparse compute. Core inference was not examined (GAP-4) | GAP | NOT_APPLICABLE | PC-SPRS-10 / PC-SPRS-20 (PR-SPRS-08) | sparse+Q012 |
| REC-SPRS-21 | OM-1 (A2 new) | — (not addressed) | **Orphaned keys**: there is no unlink override or cleanup, so a deleted attribute's key stays in every container and is carried forward by rewrites | GAP | NOT_APPLICABLE | PC-SPRS-07 | sparse+Q015 |
| REC-SPRS-22 | OM-2 (A2 new) | — (not addressed) | **Arbitrary key injection**: the container accepts any map with no per-key validation. Unknown keys never become active attributes, but they can be stored through a direct container write (API or import) | GAP | NOT_APPLICABLE | PC-SPRS-08 | sparse+Q014, sparse+Q019 |
| REC-SPRS-23 | OM-4 (A2 new) | Only the cascade on metadata was stated (C08) | The effect on stored container columns and dependent addons at uninstall was not examined. Left as a gap | GAP | NOT_APPLICABLE | — (no proof case; unexamined) | sparse+Q015 |
| REC-SPRS-24 | SF-7 (A2 business meaning) | RISK set for tenant-defined attributes | A2 concurs that the RISK set is materially correct, with no overclaim. Affects reporting (no filter/group), zero/No semantics and audit (opaque whole-map rewrite) | MATCH | NOT_APPLICABLE | — | sparse+Q003, sparse+Q020, sparse+Q030 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 11 | REC-SPRS-01, 02, 03, 05, 07, 09, 13, 14, 15, 19, 24 |
| GAP | 5 | REC-SPRS-06, 20, 21, 22, 23 |
| CONTRADICTION | 1 | REC-SPRS-08 |
| UNKNOWN_PENDING_PROOF | 7 | REC-SPRS-04, 10, 11, 12, 16, 17, 18 |
| **Total** | **24** | 19 A1 claims + 5 A2 findings/omissions promoted (SF-6, SF-7, OM-1, OM-2, OM-4). SF-1..SF-5 and OM-3/OM-5 are merged into their parent claim rows |

Lane B column: UNCORROBORATED 7 (REC-SPRS-04, 05, 06, 10, 14, 16, 17, the same set A2 listed as C04, C05, C06, C10, C14, C16, C17). NOT_APPLICABLE 17. FAIL: 0.

## 6. MODULE+QID lineage summary (frozen bank W1-B04, 41 QIDs)

This is lineage only. Mapped QIDs are **not answered** and carry no coverage meaning.

- **Mapped (29):** Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q016, Q017, Q018, Q019, Q020, Q021, Q028, Q030, Q031, Q036, Q037, Q038, Q039, Q040.
- **No evidence yet (12):** Q022 (atomic mixed transaction), Q023 (retry after ambiguous timeout), Q024 (defaults with absent key), Q025 (company/tenant ownership of optional values), Q026 (backup/restore/migration), Q027 (type-change migration validation), Q029 (scoped administrative repair), Q032 (very large values), Q033 (Unicode round-trip), Q034 (numeric precision through serialization), Q035 (record-level access on traversal of a stored relation), Q041 (diagnostics without leaking siblings).
- REC items with no clear QID fit: REC-SPRS-02, 07, 15.

## 7. Carried forward

- A1 evidence gaps GAP-1..GAP-6 remain open. GAP-2 is statically resolved as C10, but its reachability stays open. GAP-3, GAP-4 and GAP-6 underlie REC-SPRS-18, 20 and 17.
- CRQ-SPRS-01..07 are carried unchanged and map to PR-SPRS-01, 02, 04, 05, 03, 09 and 07.
- The CONTRADICTION REC-SPRS-08 must not be resolved in favour of A1's "limited to the same model" unless a server-side constraint is shown. PC-SPRS-06 tests this on source.
- CON-SPRS-01 (the source-path defect) is upheld by both A1 and A2. It is carried as REC-SPRS-10 (UNKNOWN_PENDING_PROOF for runtime reachability), not as an A1/A2 contradiction.

## 8. Handoff to PROOF

All 9 A2 proof requirements (PR-SPRS-01..09) are passed to Proof. Items that require proof: REC-SPRS-04, 06, 08, 10, 11, 12, 16, 17, 18 and 20. Items with a static check only: REC-SPRS-01, 02, 03, 09, 14, 15, 19, 21 and 22.

## 9. Limitations

- REC reconciles documents. Re-reading the source belongs to Proof Stage 2.
- No Lane B evidence exists, so nothing here is runtime-corroborated.
- No Formal Coverage claim, no percentages and no QID answered. The bank was not edited.
- Clean room: neutral WHAT/WHY/RISK summaries only. Identifiers are evidence pointers and no code is reproduced.
- Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_sprs_rcap`.
