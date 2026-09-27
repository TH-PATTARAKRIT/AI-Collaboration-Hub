# G01 PLATFORM_BASE — Module `base_sparse_field` — RED TEAM A3 Independent Challenge (STATIC)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3 — independent adversarial challenger |
| Independence | This reviewer did not author Lane A, A1, A2, REC or Proof for this module, and did not reuse the Proof scratch copies of source. Source was fetched again separately and blob-verified |
| Scope | STATIC only. RUNTIME cases (PC-SPRS-13..21) are NOT-EXECUTED: neither passed nor failed |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Frozen bank | W1-B04 `G01_BASE_SPARSE_FIELD_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `2e0e1584…77895c8`. This equals the `bank_files` entry in `FREEZE_W1-B04.json` (file sha256 `27db9033…d4f9`, which equals the value in the REC intake) |
| Intake manifest | `scratchpad/a3_sprs_rcap/intake.sha256` (sha256 `f4c577d93e63d45f6831e7dffc900562c3f61fe995661e1909956d672d85def7`): 10 stage files for both modules, 2 banks and the freeze file |
| Intake hashes (this module) | Lane A `d18d6476be0cfd2fc1d728ed4814b04e06677f47a23a33ce8ba41a4386b08b9f`; A1 `50c2c610f8df71d3f7cbdd6073c24bd02da746933622962f4f6b91322ebca91d`; A2 `b50478d63b806e827dfb561cc784bf6d4208dca568e7f37e3060531c640ee42a`; REC `b8a7da6eab7448e17ce13b587213bd43d1b2e8800b1f00b796d0c37e1b8b11f3`; Proof `94237a9c3ac336856c8adbe712b508ea4bf1c3c5c4fd4aab79856d18f83c4d64` |
| Exit hashes | All intake files were hashed again at exit. Every value is identical (`exit_inputs.sha256`): the inputs are unchanged. A3 source blob log `blob_a3.txt` sha256 `f88117f6d4a111f3928d1fd932032a986f7a7720ea8529d1fa1ecd64527925c1` |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC for the QID lineage; route to A2/Proof for the REC-SPRS-08 refinement)**. Both defects are minor. No static conclusion was disproved. Runtime remains pending for MASTER |

## 2. Challenge log

### Challenge 1 — Re-derive REC items from source and try to refute them

Six source files were fetched again from the anchor (HTTP 200 each). Each `git hash-object` equals the recorded blob: `__manifest__.py` c487ecfe, `models/fields.py` cb26946e, `models/models.py` f2196226, `views/views.xml` 1c199e72, `security/ir.model.access.csv` c163e1f2, `tests/test_sparse_fields.py` 944ff206.

| REC item | Refutation attempt | A3 finding | Disposition |
|---|---|---|---|
| REC-SPRS-04 (C04, falsy removes key) | Looked for any path that stores 0 or false | In the inverse (`fields.py` L59–71), a falsy read-converted value only removes the key. No path stores a falsy value. The compute (L50–54) returns "absent" for a missing key | UPHELD |
| REC-SPRS-06 (C06 + SF-2, unguarded decode) | Looked for a type check or error handling | A write passes a non-dict value through as-is (L88–90). The read conversion decodes with no guard (L92–93). The compute does a map lookup on the decoded value (L53–54), so a list or scalar fails at that point | UPHELD |
| REC-SPRS-08 (C08, same-model limit is UI-only; CONTRADICTION) | Looked for a server-side constraint on the pointer target model | None exists. The same-model rule appears only as a string domain on the field (`models.py` L22–23) and as a view domain on the model form (`views.xml` L12). The field form has no view-level domain (L24–26). The CONTRADICTION class is upheld. **Refinement**: the consequence is visible in module scope, although A2 SF-1 says it is not. When a registry field is instantiated, only the container's *name* is carried (L84–88). During reflection the name is resolved against the field's *own* model (L61–71). If the own model has no container with that name, a user error is raised. If it has one, the pointer is silently rewritten by raw SQL to the own-model container. So data cannot land in the other model's container. The real risk is an error while reflecting (setup/upgrade availability) or a silent re-point. When reflection runs for manual fields is decided in core code, which was not read | UPHELD with refinement (CHALLENGE-SUSTAINED, minor: the A2 SF-1 wording and PC-SPRS-06 scope) |
| REC-SPRS-10 (C10, rename guard reads a missing key) | Looked for a guard on the name key | The outer condition is "pointer key OR name key" (L32). The name is indexed with no presence check (L36). A payload that carries only an *unchanged* pointer for a field that has a pointer passes L34 and reaches L36, which raises a missing-key technical error. A *changed* pointer raises the user error at L35 first. The normal web form sends only dirty fields, so the path is reached through RPC, import or module data. Whether it is reachable at runtime stays open | UPHELD (source path) |
| REC-SPRS-22 (OM-2, arbitrary key injection) | Looked for a key allow-list | Any map is serialised (L90). A read looks up only its own name (L54). Unknown keys persist and are carried forward by later whole-map rewrites (L62–71) | UPHELD |
| REC-SPRS-12 (C12, raw SQL sync) | Checked diff-only behaviour | Updates are collected only where the current value differs (L70–71) and applied by raw SQL (L77–79). The missing-container case is a user error (L62–69). Side note: the lookup of the field's own row at L61 is outside the try block, so a field without a reflected row would raise a plain missing-key error. It is expected to be unreachable after the core reflection, which was not read | UPHELD |

### Challenge 2 — Re-execute static PASS cases

| PC | A3 re-execution | Result | Weakness |
|---|---|---|---|
| PC-SPRS-02 | `fields.py` L59–71 read | Same as Proof (PASS) | None. The fail condition is falsifiable |
| PC-SPRS-04 | `models.py` L29–39 read; condition L32, index L36 | Same (PASS) | None |
| PC-SPRS-06 | L22–27; `views.xml` L12, L24–26; grep for constraints found 0 | Same (PASS) | The case predicate covers only whether a constraint exists. It did not follow the reflection re-resolution (see Challenge 1), so the effect statement in Proof §5 ("runtime cross-model setup behaviour is not examined") understates what source already shows |
| PC-SPRS-11 | ACL row: system group, 1/1/1/0; views readonly only when the state is base, no quick-create | Same (PASS) | None |
| PC-SPRS-12 | The test writes only truthy values and unsets with false (L23, L31) | Same (PASS) | None |

Runtime-case review for weak conditions: PC-SPRS-21 accepts "refused, or explicitly unsupported" but fails only on "silently empty or wrong". The core fallback for searching a non-stored field without a search method was not read, so the outcome classes may overlap. This is flagged as a weak split, not a defect. PC-SPRS-16 and PC-SPRS-17 are falsifiable. **Disposition: UPHELD** (with the PC-SPRS-06 scope note carried into Challenge 1).

### Challenge 3 — Predeclaration integrity

Verified: `rec_sprs_rcap/PROOF_CASES_PREDECLARED.md` has sha256 `59a6e0d0…dcbc` (matches) and mtime 15:03:45.39Z. The first Stage-2 source file is dated 15:04:02Z and `blob_results.txt` 15:04:07Z. The ordering therefore holds. The cases were written after reading A1/A2, which paraphrase the source. A3 judges this **acceptable**: predeclaration has to precede *execution* (observing results), not the reading of the claims under test, because the cases have to be derived from those claims. The residual risk is confirmation bias, where a case is built to confirm the upstream mechanism. For this module A3 found no case whose PASS is false. **Disposition: UPHELD.**

### Challenge 4 — Lineage

`git log --follow` (read-only):
- REC: a single commit, `3215ebe` at 2026-09-27 15:08:44Z, message "REC/Proof G01: bus, digest …". The file was swept into another module's commit. This is a commit-message mislabel only; the commit is a MASTER checkpoint of on-disk state.
- Proof: a single commit, `7c417ac` at 15:10:30Z, "in-flight Proof checkpoint".
- The working tree is clean for both files, and the current sha256 equals the intake. There is no later content change by anyone other than the author. **Disposition: UPHELD** (the mislabelled commit message is noted, timing only).

### Challenge 5 — Overclaim, Lane B, QID mapping, bank hash, clean room

- Overclaim: no Formal Coverage, no percentages and no QID answered. RUNTIME cases are correctly left NOT-EXECUTED. **UPHELD.**
- Lane B: none exists. The column uses UNCORROBORATED or NOT_APPLICABLE and never FAIL. No misuse. **UPHELD.**
- Bank sha256 equals the `FREEZE_W1-B04.json` entry. **UPHELD.**
- Clean room: a scan of REC and Proof for code constructs found no reproduced code. Identifiers appear only as evidence pointers. **UPHELD.**
- QID mapping sample: Q007 (renaming must not disconnect values) → REC-SPRS-09/10: good fit. Q008 (the container must resolve before use) → REC-SPRS-08/12: good fit. Q015 (removal retention) → REC-SPRS-21/23: good fit. Verification of the "no evidence" list:
  - **Q035** (a stored relation must honour record-level access on traversal) is listed as "no evidence", but REC-SPRS-05 (relational values held as bare ids and filtered only for existence) is direct static evidence on it. **CHALLENGE-SUSTAINED (REC)**.
  - **Q024** (defaults with an absent key) is listed as "no evidence", but REC-SPRS-04 shows static evidence on how an absent key reads (the compute returns absent and applies no default). **CHALLENGE-SUSTAINED (REC)**, minor.

## 3. Lineage

| Artifact | sha256 at intake = exit | Git commits |
|---|---|---|
| Lane A | d18d6476…b08b9f | — (not examined beyond hash) |
| A1 | 50c2c610…ebca91d | — |
| A2 | b50478d6…0ee42a | — |
| REC | b8a7da6e…11f3 | 3215ebe (single; mislabelled message) |
| Proof | 94237a9c…d18f83c4d64 | 7c417ac (single) |
| Bank | 2e0e1584…77895c8 = FREEZE entry | — |
| Predeclared cases | 59a6e0d0…dcbc (scratch) | not in the repository |

## 4. Defects routed

| ID | Severity | Owner stage | Defect | Required action |
|---|---|---|---|---|
| A3-SPRS-D1 | Minor | REC | Q035 and Q024 are listed as "no evidence" although REC-SPRS-05 and REC-SPRS-04 provide static evidence on them | Add them to the lineage map (still not answered) |
| A3-SPRS-D2 | Minor | A2 (SF-1 wording) / Proof (PC-SPRS-06 effect) | "Setup-time behaviour is not visible in module scope" is inaccurate. Reflection re-resolves the container by name on the field's own model, which gives either a user error or a silent SQL re-point | Restate the REC-SPRS-08 risk as an availability error or a silent re-point, not cross-model storage. Add a runtime case: create a manual field that points to another model's container and observe the reflection outcome |

## 5. Runtime-blocked items

PC-SPRS-13 to PC-SPRS-21 are NOT-EXECUTED because the runtime device is OFFLINE. They cover REC-SPRS-04, 06, 10, 11, 12, 16, 17, 18 and 20, which stay UNKNOWN_PENDING_PROOF or GAP. A new cross-model pointer case is recommended (A3-SPRS-D2). REC-SPRS-23 (uninstall data effect) still has no case.

## 6. Limitations

- Static only, on one anchor commit. Core field setup, core reflection timing for manual fields, transaction isolation and the search fallback were not read.
- The QID fit check is a sample (5 QIDs), not a full re-map.
- No inputs were edited. Git was used read-only. No Formal Coverage claim, no percentages and no QID answered.
- Clean room: neutral summaries. Line numbers and identifiers are pointers only.
