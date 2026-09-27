# G01 PLATFORM_BASE — Module `html_builder` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions); independent of A1 |
| Governed group / module | G01 PLATFORM_BASE / `html_builder` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_HTML_BUILDER_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `2cfc3d1e75a6a3a7db1c123c5aac73ea87802aaeaef17e74c15e3d5b050a3332` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_HTML_BUILDER_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `76275bbb39379c2736d2b8411bdcb331771aa28f378bfef5c1eeb574f143deec` (equals the value recorded in the A1 header) |
| Question Gate | Batch W1-B06 = **HOLD-LOCAL** (freeze hash not reproducible). A2 verifies claims only. QID-level lineage is **NOT A3-eligible** until GMVQ re-freezes W1-B06. Gate condition, not an A1 defect. |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/html_builder/`; blobs via `git hash-object` in scratchpad |
| Date | 2026-09-27 |
| Lane B | None exists (section 6) |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. The central conclusion "assets only, no server-side Python" is independently confirmed. 9 claims: 8 VERIFIED, 1 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE.
2. The PARTIAL (C08) is a count precision issue: 527 translatable entries, not 528 (the extra one is the file header).
3. Omissions are minor and additive. Handoff: Reconciliation, carrying 4 proof requirements.

## 2. Test plan (predeclared before verification)

Plan file sha256 `18528f0e21564afc1168d49e7e5be9f492d3784f8a4c3d41035995615beb0a51` (scratchpad).

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP-1 | Lineage hashes | Recorded equals recomputed | PASS |
| TP-2 | Re-fetch 6 Lane A pointer files; probe `models/`, `controllers/`, `security/` absence | Blobs match; absences 404 | PASS (6 of 6 match; package init is 0 bytes; 3 absences 404) |
| TP-3 | Semantic re-read of all HIGH claims (C01–C07, C09): assets-only, dependencies, bundles, test guard, frontend injection | Meaning matches manifest/test | Done, section 3 |
| TP-4 | Independent recount of translation inventory (C08) | Counts reproduce | 79 files (32 JS, 47 XML) reproduce; entry count 527 |
| TP-5 | Business framing + omission scan of manifest and test | Material omissions recorded | SF-H01..SF-H03, OM-H01..OM-H05 |
| TP-6 | Lane B classification | Never FAIL for absence | Section 6 |
| TP-7 | Proof requirements | Falsifiable | Section 7 (4 items) |
| TP-8 | Gate note | W1-B06 HOLD-LOCAL recorded | Header |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| A1-G01-HBLD-C01 | HIGH | VERIFIED | Manifest description names website builder and mass-mailing editor as intended users. |
| A1-G01-HBLD-C02 | HIGH | VERIFIED | Package init is the empty-file blob (0 bytes); models, controllers and security paths 404. Only Python is the test package. |
| A1-G01-HBLD-C03 | HIGH | VERIFIED | Manifest has no data key. |
| A1-G01-HBLD-C04 | HIGH | VERIFIED | Dependencies base, `html_editor`, `mail`; manifest comment attributes the mail dependency to a single client helper. Refinement: the helper's name indicates a client model-definition helper of the kind used in JS unit tests, which would make the coupling test-only; not established from module source (PR-HBLD-04). |
| A1-G01-HBLD-C05 | HIGH | VERIFIED | Three new bundles (builder, in-builder iframe, add-snippet dialog iframe) and four contributions (primary variables, public frontend, web dark, unit tests). Refinement: the builder bundle removes every file matching the edit-only pattern (not only SCSS) plus dark SCSS. |
| A1-G01-HBLD-C06 | HIGH | VERIFIED | One post-install HTTP test resolves the builder bundle and asserts no file ends with the edit SCSS suffix. Refinement: the test is narrower than the removal directives. It does not check non-SCSS edit files or dark SCSS (OM-H02). |
| A1-G01-HBLD-C07 | HIGH | VERIFIED | Background SCSS added to the public frontend bundle. |
| A1-G01-HBLD-C08 | MED | PARTIAL | 79 distinct static source files (32 JS, 47 XML) reproduce; no Python references. The "528 message IDs" count includes the empty header entry; translatable entries with source references = 527. Lower-bound framing stays correct. |
| A1-G01-HBLD-C09 | HIGH | VERIFIED | No groups, ACL, rules or elevation (no Python, no security files). Authorization for persistence belongs to other modules. |

Totals: VERIFIED 8 · PARTIAL 1 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

Contradiction/CRQ items: A1 reports none, and A2 agrees. CRQ-HBLD-1..3 are well-founded. CRQ-HBLD-1 depends on PR-HBLD-04: if the mail coupling is test-only, the CRQ becomes a packaging question, not a runtime coupling.

## 4. Semantic / business findings

- SF-H01 (assets-only scope): Correct and important for downstream design. The builder carries no business rules, data or authorization; any save, publish or content-validation behaviour must be verified in `html_editor`, website or mass-mailing modules. A2 found no client call to server routes in the main builder component imports (surface check only).
- SF-H02 (styling boundary, C06/C07): The editor/public styling boundary is a build-composition concern; its only automated guard is a post-install test, which is not part of a standard at-install run.
- SF-H03 (footprint, C05/C07): The module's styling reaches beyond the editor: a variables contribution enters the shared primary-variables bundle and a background stylesheet enters every public page. This is visual surface only, not a data or security surface.

## 5. Omissions (material, not in A1)

- OM-H01 Variables contribution to the shared primary-variables bundle influences every bundle compiled from it (backend and frontend), which is wider than the public-page footprint in C07.
- OM-H02 Test guard narrower than removal rules (see C06 refinement).
- OM-H03 Manifest sets no installable/auto-install/application keys, so framework defaults apply. The module is never auto-installed and is reached only through consumer dependencies (Lane A noted this; A1 omitted it).
- OM-H04 Unit-test bundle includes the full builder bundle.
- OM-H05 Translation count precision (see C08).

## 6. Lane B classification

No Lane B evidence exists for `html_builder`. Absence is not a failure.

| Claim | Classification |
|---|---|
| C01, C02, C03, C04, C05, C08, C09 | NOT_APPLICABLE (static declarations and absences) |
| C07 | UNCORROBORATED (observable on a public page, fully determined by manifest) |
| C06 | MISSING_REQUIRED_RUNTIME_PROOF (the guard only exists when the post-install test is executed) |

## 7. Proof requirements

| PR | Claim(s) | Procedure | Expected | Fail condition |
|---|---|---|---|---|
| PR-HBLD-01 | C06, OM-H02 | Run the post-install bundle test; separately list the resolved builder bundle files | Test passes; no edit-pattern or dark SCSS file in the bundle | Any edit-pattern or dark file present |
| PR-HBLD-02 | C07, OM-H01 | Load a public page with the module installed; inspect the compiled frontend CSS for the builder background rules | Rules present outside edit mode | Absent → injection not effective |
| PR-HBLD-03 | C09, CRQ-HBLD-2 | Cross-module source review of the save path(s) the builder uses in `html_editor`/website/mass mailing; identify authorization checks | Server-side authorization identified per save path | Any save path without server-side authorization |
| PR-HBLD-04 | C04 | Source search in `html_builder` static code for use of the mail helper; classify as runtime or test-only | Classification recorded | Not recorded; claim remains as stated |

## 8. Limitations

- Static manifest/test/translation analysis only; client JS/XML behaviour not analysed (by brief). Full static inventory unknown; 79 remains a lower bound.
- No QID answered; W1-B06 HOLD-LOCAL means QID-level lineage is not A3-eligible until re-freeze. No Formal Coverage; no percentages.
- Clean room: neutral statements; identifiers are pointers; no code reproduced. Inputs unmodified; no git operations.
