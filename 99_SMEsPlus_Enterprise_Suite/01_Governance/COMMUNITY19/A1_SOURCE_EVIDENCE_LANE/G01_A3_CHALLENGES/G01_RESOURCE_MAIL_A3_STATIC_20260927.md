# G01 PLATFORM_BASE — Module `resource_mail` — RED TEAM A3 Independent Challenge (STATIC scope)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3 (independent adversarial challenger) |
| Independence | This A3 wrote none of Lane A, A1, A2, REC or PROOF for `resource_mail`. An earlier A3 attempt stopped at intake with no output. This is a fresh start, and nothing from that attempt was reused. |
| Date | 2026-09-27. Exit check at 2026-09-27T15:14:44Z. |
| Scope | STATIC only. Runtime cases PC-RMAIL-R01..R03 are **NOT-EXECUTED**, so they are neither passed nor failed. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched each file and checked it with `git hash-object` (section 2). |
| Question lineage | Standard 55 only (W1-STD). MVQ lineage is unavailable (GMVQ backlog). |
| **Overall disposition** | **A3 STATIC PASS — MASTER HANDOFF PENDING RUNTIME**. No challenge was sustained. The 3 UNKNOWN_PENDING_PROOF items and the 3 runtime cases stay open. |

### Intake hashes (sha256; scratch `a3_rsrc2/intake.sha256`, file sha256 `83440c1f74652ebbdd221089867ffa8e13ec7518570e85dd5ae5e56515646520`)

| Input (relative to `A1_SOURCE_EVIDENCE_LANE/`) | sha256 |
|---|---|
| G01_LANE_A_PASS1/G01_RESOURCE_MAIL_LANE_A_PASS1_20260927.md | 7ddbb4501027579e85e689feefd4acf91cc73a29907d0e9fb8c6e89d5c453c45 |
| G01_A1_PACKAGES/G01_RESOURCE_MAIL_A1_PACKAGE_20260927.md | f3f552c5098154ed344d338ff91148b6a0f39a6c605fdb6df5284ff16cc88ee8 |
| G01_A2_REVIEWS/G01_RESOURCE_MAIL_A2_REVIEW_20260927.md | e4e630b904a55c3b98a75ce26f82618c11fad62cce522e11370c60d8073c42a9 |
| G01_RECONCILIATION/G01_RESOURCE_MAIL_REC_20260927.md | 1ec90af273af437692663390db5e4d182cf4490204385dbf67d25fefed8cb26f |
| G01_PROOF/G01_RESOURCE_MAIL_PROOF_20260927.md | c15b9e11994d2ffd6e291dda93b710f26de72920456523250360883c5d0078a6 |
| ../GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md | f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d |

**Exit check:** `sha256sum -c` returned OK for every input at 15:14:44Z. No input was changed or edited.

## 2. Blob re-verification (by A3)

| File | Blob (recomputed) | vs recorded |
|---|---|---|
| addons/resource_mail/__manifest__.py | 032a25c2cd5c1be067974b60ca1efb7c5848d54c | MATCH |
| addons/resource_mail/models/resource_resource.py | 797be7bd04f8ef3f089dbda74db6cf9841b84406 | MATCH |
| addons/resource/models/resource_resource.py (cross-ref) | aad3af2f8b87bff4cc650819abc2856fdb826067 | MATCH |
| addons/resource/security/ir.model.access.csv (cross-ref) | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 | MATCH |
| addons/resource/security/resource_security.xml (cross-ref) | 500b70f06c5fb917bd5657bbaaf23843920dae0c | MATCH |
| odoo/orm/models.py (framework) | 11f50c4e0b676fbb4b8a45e9703326946348ff98 | MATCH (value recorded by PROOF) |

A3 also fetched the package `__init__` and `models/__init__` files. Each has a single import, which is consistent with Lane A (the controller and wizard entries were probed and returned 404).

## 3. Challenge log

### CH-1 — Re-derive REC items from source

| Target | A3 re-derivation (paraphrase and pointers) | Disposition |
|---|---|---|
| REC-RMAIL-04 / 06 (C04, OM-01): avatar-card exposure | The model file, lines 17–18: the avatar-card method returns a plain read of the field list the caller names. It adds no elevation, filter or whitelist. The resource model mirrors the linked user's email, phone and share flag as related fields (`resource` resource_resource : 38–42), and this module adds presence (line 15). The resource ACL grants read to the internal-user and system groups only; it has no portal or public row. The global company rule admits the session's companies plus no-company. The exposure statement is therefore correct at static level. One precision point: "same company or no company" in REC-06 means the session's active companies plus no-company. Whether related values are fetched with elevated rights is framework behaviour, and PROOF correctly routes it to R03 (R1). | **UPHELD** (runtime R03 pending) |
| REC-RMAIL-07 (OM-02): an empty field list returns all readable fields | orm/models.py : 3491–3492. An empty or missing list expands to the output of the field-listing method, and that method skips fields for which the caller lacks field-level read access (3364–3365). "All readable fields" is confirmed. | **UPHELD** |
| REC-RMAIL-01 (C01): hidden, auto-install, no data or security | The manifest shows category Hidden, depends on `resource` and `mail`, and has auto-install set. It declares only asset bundles and no data, demo or security keys. | **UPHELD** (runtime R01 pending) |

### CH-2 — Re-executed static PASS cases

| Case | A3 re-execution | Falsifiability | Disposition |
|---|---|---|---|
| PC-RMAIL-01 | Manifest keys confirmed as above | Strong: any data file, or auto-install off, would fail it | UPHELD |
| PC-RMAIL-02 | Colour default is a random integer from 1 to 11 inclusive. The field is stored and has no constraint. | Adequate: "Deterministic/unique" | UPHELD |
| PC-RMAIL-03 | Presence is a non-stored related field through the linked user | Strong: stored or independent would fail it | UPHELD (definition only; the empty case is R02) |
| PC-RMAIL-04 | Confirmed as in CH-1 | Strong: filter, sudo or whitelist would fail it | UPHELD |
| PC-RMAIL-06 | Confirmed as in CH-1 | Adequate. The Fail condition covers "raises or returns none" but not "returns fields beyond readable". The Expected wording "(readable)" carries that part. | UPHELD (minor looseness) |

### CH-3 — Predeclaration integrity

The case file is shared with `resource`: scratch `rec_rsrc/PROOF_CASES_PREDECLARED.md`, sha256 `14159fb2…114de`. That value equals the one PROOF records. The file was born and last modified at 15:03:14Z, before the framework fetch at 15:04:10Z. Its PC-RMAIL-01..06 rows match the executed cases. The blob log (`blob_log.txt`) was born at 15:07:37Z, after the stated execution window. A3 therefore treats the log timing as INCONCLUSIVE. Integrity is still covered, because A3 re-verified every blob independently. **Disposition: UPHELD**, with that timing caveat.

### CH-4 — Lineage

See section 4.

### CH-5 — Overclaim, Lane B, Standard 55, clean room

| Check | Finding | Disposition |
|---|---|---|
| Overclaim | The PROOF disposition is PARTIAL, and no runtime result is claimed. REC-RMAIL-03 PASS is limited to the definition, and the empty-presence case is runtime. There are no percentages and no Formal Coverage claim. | UPHELD |
| Lane B misuse | No Lane B evidence exists. Its absence is recorded as UNCORROBORATED or NOT_APPLICABLE and never as FAIL. | UPHELD |
| Standard-55 fit (3 sampled) | REC-04 maps to Q28/Q29 (cross-boundary visibility; record-level access). Good fit: a caller can reach the linked user's contact data through the resource. REC-03 maps to Q36 (indirect relationship traversal). Good fit: presence is read through the user hop. REC-05 maps to Q29 (no new ACL). This is an acceptable weak fit: it records absence of controls. No QID is claimed as answered. | UPHELD |
| Clean room | The inputs contain 0 fenced code blocks. Method and field identifiers appear only as pointers. This A3 file paraphrases and does not reproduce code. | UPHELD |

## 4. Lineage adjudication

| File | Commits |
|---|---|
| G01_PROOF/G01_RESOURCE_MAIL_PROOF_20260927.md | One commit: `6302d8f` 15:10:22Z, "SMEsPlus REC/Proof G01: resource, resource_mail". The file was added (85 lines) and has not been modified since. |
| G01_RECONCILIATION/G01_RESOURCE_MAIL_REC_20260927.md | One commit: `79cd651` 15:07:34Z, "SMEsPlus A2 G01: base review (CRQ-01 closed-static)". The file was added (98 lines) and has not been modified since. |

- No content change follows the first commit of either file. The dispositions **6 PASS / 0 FAIL / 3 NOT-EXECUTED** and the 7-item REC counts (2/2/0/3) are intact.
- **Adjudication: content integrity UPHELD. Author attribution is INCONCLUSIVE from git.** Every commit shares one author identity and one session trailer, and the REC file first landed inside a commit titled for a *different* stage and module (the A2 `base` review). This cross-stage commit bundling is a provenance-hygiene note routed to Integration Control. It is not a content defect, because the committed content equals the intake hash.

## 5. Defects routed

None sustained.

Non-blocking notes:
- N-1: REC-06 wording "same company or no company" should read "the session's active companies or no company". This is a precision point with no routing required.
- N-2: The blob-log timing note (CH-3).
- N-3: The commit bundling noted in section 4 goes to Integration Control.

## 6. Runtime-blocked items (NOT-EXECUTED — neither passed nor failed)

- PC-RMAIL-R01 (auto-install effect).
- PC-RMAIL-R02 (empty presence when no user is linked).
- PC-RMAIL-R03 (actual avatar-card exposure: contact fields on a same-company resource, empty-list behaviour, cross-company denial, and whether related fields are elevated).
- All 3 UNKNOWN_PENDING_PROOF items (REC-RMAIL-01, 03, 04) stay open.
- The PDPA-type exposure (OM-01) remains an input to IAM design.

## 7. Limitations

- The review is static only. JS assets (the avatar-card UI consumer), tests and the `mail` presence field definition were not read (A1 G1–G3 stay open).
- Framework semantics for related-field elevation are not proven.
- No percentages, no Formal Coverage claim, and no QID answered. Git was used read-only, the inputs were not edited, and clean-room rules were followed.
