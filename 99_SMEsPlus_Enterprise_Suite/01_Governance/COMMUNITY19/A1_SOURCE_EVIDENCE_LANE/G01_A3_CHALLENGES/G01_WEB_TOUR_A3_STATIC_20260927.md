# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC) — `web_tour`

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial challenger. A3 did not write any upstream stage |
| Group / Module | G01 PLATFORM_BASE / `web_tour` |
| Date | 2026-09-27 |
| Scope | STATIC only (SOURCE layer; the module reads no config). RUNTIME is **NOT-EXECUTED**, which means neither passed nor failed |
| Intake manifest | scratchpad `a3_web/intake.sha256` (manifest sha256 `6ec235d8d24d9fb681c3213c285f668c0160d933c919e7d11466c37d5fdc592f`, shared with `web`) |
| Inputs (sha256) | Lane A PASS-1 `111e1959eb255d339ac921a3981c090b0bbb9a77d9db1273c2b15d8a96b387d0`; A1 `d794e25f34cbd6a821661764b3cec356df1219625510605261a9b1fc7546d315`; A2 `b7d585137777cb92900a51b044e8a7bc91482c70d1b6b7e3f66456d7064381b4`; REC `b875cc2864bbe03fa9773802b54417062f9f2ce643e240ebd3c08906bdd59c55`; PROOF `96c82939d402cc7c9270b084a3ab53d537fb85e1156e29fec673e7e79e5f7fa8` |
| Bank / freeze | `G01_WEB_TOUR_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `fdc06e0b530f327b2eec9ffddd3abff4104d387acb43c2fade99344854986f37`, which equals the FREEZE_W1-B05 entry. FREEZE_W1-B05.json sha256 is `7884f78d…bd6a`, freeze_hash `cc81bc57…1bd3`. The bank holds 40 QIDs; `formal_coverage` is NOT AUTHORIZED |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 re-fetched these files and verified each with `git hash-object`: web_tour models/tour.py `575bf0a5…`, models/res_users.py `9ab9decb…`, security/ir.model.access.csv `71ea4517…`, views/tour_views.xml `c80188dc…`, base ir_actions.py `45d06ee4…`, base ir_attachment.py `905ae118…`. All MATCH |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to Lane A / A1; PROOF minor)**. No source-layer conclusion is overturned. The runtime cases PC-WTOUR-01..03 are still pending |

Clean-room note: this record contains neutral paraphrase only. Identifiers are evidence pointers, and no vendor code is reproduced. It contains no percentages and makes no Formal Coverage claim. Git was used read-only, and the inputs were not edited.

## 2. Challenge log

| # | Challenge | A3 independent check (paraphrase, approximate line pointers) | Disposition |
|---|---|---|---|
| A3-T-01 | **C11 "Export JS by read-only user" RESOLVED AT SOURCE** | ACL (4 rows): the system group has full CRUD on guide and step, and internal users are read-only on both. The bound server action is code-type, targets the guide model, binds to the form view, and has no group field (views ~L78-89). The menu has no group attribute (~L75). Base run path (ir_actions ~L1151-1242): per action, the rights check runs **before** the elevated run. With no action groups, the caller must pass a model-level write check and a record-level write check, and a failure is refused with a warning log. The code body calls the export method on the records from the eval context; those stay in the caller's environment. Direct RPC to the public export method creates a linked attachment as the caller. The attachment check maps create/unlink to write on the linked record (ir_attachment ~L514-541) | **UPHELD** at source. Residual (not a defect in this module's chain): any **other** module that grants write on the guide model to a wider group would reopen the path. That is outside `web_tour` scope and can only be checked cross-module or at runtime (PC-WTOUR-02) |
| A3-T-02 | **C09 OPEN (public vs private JSON builder)** | The by-name getter is a public model method that passes a possibly empty search result to the builder. The builder is underscore-prefixed (tour.py ~L44-58). The current-guide method is also public and gated on internal user plus flag (~L38-42) | **UPHELD** (A2 reading is correct; A1's RISK "all internal users read all guides" also stands). A3 recommends that MASTER record it as a surface-precision correction with an agreed risk. It can remain OPEN in form only |
| A3-T-03 | **Re-execution of static PASS cases (2 or more required)** | PC-WTOUR-07: reproduced (A3-T-01). PC-WTOUR-08: reproduced (4 ACL rows as stated). PC-WTOUR-09: reproduced (action and menu without groups). PC-WTOUR-12: reproduced (A3-T-02). PC-WTOUR-05: reproduced (internal check, name lookup as caller, elevated set-link, unknown name is a no-op, current guide returned). PC-WTOUR-06: reproduced (name and URL placed raw inside quoted literals of the generated script, steps JSON-serialised, attachment named from the raw name, new attachment on every call). PC-WTOUR-10: reproduced in part (the default flag uses the Access-Rights admin predicate, an elevated demo-module count and a not-in-test check; the toggle writes the current user under elevation with no internal check). **Weak conditions flagged:** PC-WTOUR-06 passes on *presence* of unescaped interpolation, but exploitability is bounded by system-group authoring and remains runtime (PC-WTOUR-03). PC-WTOUR-14 is a keyword-bounded absence check | **UPHELD** (7 of 7 re-executed cases reproduce) |
| A3-T-04 | **Predeclaration** | The file is shared with `web`: sha256 `32cafe38…ec6fb` recomputed equal, mtime 15:05:27Z, earlier than the first fetch at 15:05:46Z | **UPHELD** (scratchpad file, not tamper-evident; see the `web` record) |
| A3-T-05 | **Overclaim / Lane B misuse** | A2's C11 refutation is stated as static with runtime still required, which is correctly bounded. REC's "RESOLVED AT SOURCE, RUNTIME PENDING" is correctly qualified. No Lane B evidence exists, and nothing fails for absence | **UPHELD** |
| A3-T-06 | **QID mapping fit (sample of 4) and "no evidence" checks** | Sample for REC-WTOUR-04 (C04): Q020 (repeat completion without duplicate membership) **fits**, because the set-link is idempotent. Q021 (concurrent completion converges) **fits** as topic, with runtime pending. Q023 (completion plus next-guide coherence) **fits**, because consume returns the current guide. Q034 (completion per own history) **fits**, because progress is a per-user relation. "No evidence" checks: **Q033 (internal identifiers in step payload)**: the guide JSON builder removes the record id from the guide payload, and the step JSON builder removes the id from each step payload (tour.py ~L49-58, ~L100-112). This is direct static evidence in module source. **Q016 (step with no body content)**: the step builder omits the content key when it is empty (~L108-109), which is partial static evidence. No Lane A/A1 claim or A2 omission captures either | **UPHELD** for REC (its "no evidence yet" is accurate relative to REC items). **CHALLENGE-SUSTAINED (owner: Lane A / A1, with A2 TP6 omission scan)**: payload identifier stripping (Q033) and empty-content handling (Q016) were missed |
| A3-T-07 | **Bank sha256 vs freeze** | Equal. REC maps 34 QIDs and lists 6 as no evidence, which accounts for all 40 | **UPHELD** |
| A3-T-08 | **Clean-room scan** of all 5 upstream files | No code fences, no code-shaped tokens, no percentages. Formal Coverage appears only in disclaimers | **UPHELD** |
| A3-T-09 | **OM-T03 carried without a proof case** | The relation-row removal on guide delete is base ORM behaviour and was not read by any stage | **INCONCLUSIVE**. Correctly carried as UNKNOWN_PENDING_PROOF |

## 3. Lineage

| Artefact | Git history (read-only) | HEAD content sha256 = intake? |
|---|---|---|
| Lane A PASS-1 | single add `d7eb909` 14:49:20Z | yes |
| A1 package | single add `1ee5230` 14:52:49Z (message names other modules) | yes |
| A2 review | single add `442993c` 15:02:40Z (message names mail / auth_signup / base_setup) | yes |
| REC | single add `fc6e7c3` 15:13:14Z (message names base_automation / mail) | yes |
| PROOF | single add `f510676` 15:14:38Z (message names portal / utm) | yes |

A2 recorded no lineage defects for `web_tour`, and A3 finds none in content. Every file's committed content equals its consumed hash. The only residual is that commit messages do not name the `web_tour` artefacts they add. The Proof header refers to the REC without a sha256.

## 4. Defects routed

| ID | Severity | Owner stage | Defect | Required action |
|---|---|---|---|---|
| D-T1 | LOW | **Lane A / A1** (A2 TP6 omission scan also missed it) | Payload identifier stripping for guide and steps (Q033) and empty step-content omission (Q016) are present in module source but not claimed | Add them in a future Lane A pass or A1 delta, then route through A2 → REC |
| D-T2 | LOW | **PROOF** | The Proof header does not pin the REC sha256 | Pin upstream hashes |
| D-T3 | LOW | **Integration Control** | Commit messages do not name the `web_tour` artefacts | Record a lineage note. Do not rewrite history |

## 5. Runtime-blocked items (NOT-EXECUTED — neither passed nor failed)

- PC-WTOUR-01: concurrent consume (C04).
- PC-WTOUR-02: Export JS by a non-system internal user, both through the bound action and by direct RPC (C11 runtime confirmation).
- PC-WTOUR-03: double-quote in the guide name or URL (C10).

OM-T03 (progress after guide delete) has no case. A3 recommends adding one at the next Proof revision.

## 6. Limitations

- Static source at one commit. The JS runner and recorder, inherited menu-parent groups, completion-message sanitisation and base ORM relation-delete behaviour were not read.
- A3 did not re-execute PC-WTOUR-04, 11, 13 and 14; it relied on their predeclared text.
- The cross-module grant of write on the guide model (A3-T-01 residual) was not searched.
- No Formal Coverage, no percentages. Git was used read-only, and the inputs were not edited.
