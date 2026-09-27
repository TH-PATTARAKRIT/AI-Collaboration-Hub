# G01 PLATFORM_BASE — Module `html_builder` — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, an independent adversarial challenger. It did not author any upstream stage |
| Module | G01 PLATFORM_BASE / `html_builder` |
| Date | 2026-09-27 (intake 15:21:45Z) |
| Scope | STATIC, CLAIM-LEVEL. Runtime NOT-EXECUTED (neither passed nor failed). MVQ lineage **NOT A3-ELIGIBLE** (W1-B06 HOLD). Standard 55 sampled |
| Source anchor | `…/8d05257d83f9128953f580a066db67c48fcdb96f/addons/html_builder/`. A3 re-fetched `__manifest__.py`, `__init__.py`, the test file and `i18n/html_builder.pot`, and all blobs MATCH |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC; PROOF)** — substance holds; process rules 1, 3 and 4 are defective |

### Intake (sha256)

| Input | sha256 |
|---|---|
| Lane A | `76275bbb39379c2736d2b8411bdcb331771aa28f378bfef5c1eeb574f143deec` |
| A1 | `2cfc3d1e75a6a3a7db1c123c5aac73ea87802aaeaef17e74c15e3d5b050a3332` |
| A2 | `745b25b560cbcac864b19c59ab5f9f32db69e142db169e3f47ca279465760b3d` |
| REC | `d6efb05e3e3893dce981084d0f2a93cefa42b017cdb1a407677f5aa3d51b9803` |
| PROOF | `9f75d2414ac0634a714902e0f0f1a9497318c564e344302a39b0dec14f0d369b` |

## 2. Challenge log

| # | Challenge | A3 re-check | Disposition |
|---|---|---|---|
| A3-HBLD-01 | "Assets-only" claim (REC-HBLD-02, PC-HBLD-08) | `__init__.py`@e69de29b is 0 bytes, so no Python is imported. `__manifest__.py`@f55fb070 has no `data` key (L1–70), so no XML or CSV data is loaded. Only `assets` (L23–68), `depends` (L21) and metadata remain. Weak condition in PC-HBLD-08: it probed only 4 absent paths, but the empty init and the missing data key close the gap. Adversarial caveat: the module is assets-only *itself*, but its hard dependency on `mail` (L21) means installing it brings in `mail`'s server surface. A1/REC should not read "assets-only" as "no server surface when installed". | **UPHELD** (with scope caveat) |
| A3-HBLD-02 | Mail-helper coupling INCONCLUSIVE (PC-HBLD-06) | Manifest comment L19–20 names a mail helper as the reason for the dependency. `web.assets_unit_tests` (L64–67) is the only bundle that pulls `static/tests/**`. The 79 enumerable `static/src` files (upstream log) have 0 occurrences. A3 cannot enumerate `static/tests/**` without a listing API, and it fetched nothing by guessed name. The result is consistent with test-only coupling but does not prove it. | **UPHELD** (INCONCLUSIVE correctly classified) |
| A3-HBLD-03 | PC-HBLD-05 NOT-EXECUTED (precondition: file listing) | The predeclared row says "if precondition unmet ⇒ NOT-EXECUTED", and the precondition (full save-path enumeration) was genuinely unmet: the manifest uses globs (L25, L37, L45, L51, L65) and there is no listing API. The PROOF correctly keeps its lead observation (snippet save, rename and delete calls in fetched JS) out of the results. Adversarial note: a *partial* execution over the enumerable paths was possible. It would still be cross-module, because the server authorization lives in `html_editor`, `website` and the view model, so NOT-EXECUTED is the more conservative and correct label. | **UPHELD** — correctly classified; CRQ-HBLD-2 must route to the `html_editor`/`website`/`mass_mailing` proofs |
| A3-HBLD-04 | C08 count correction (REC-HBLD-08 GAP) | A3 recount of `i18n/html_builder.pot`@dd82b494: 528 `msgid` entries including the header, so 527 translatable. 79 distinct referenced files = 32 JS + 47 XML + 0 Python. | **UPHELD** |
| A3-HBLD-05 | REC cites a PROOF case | REC-HBLD-08 cites PC-HBLD-07 in its proof-link column. The REC was edited after PROOF started (commit `b31a0e8` → `37823e6`, a one-line correction to a freeze-hash abbreviation). REC was not frozen before PROOF. | **CHALLENGE-SUSTAINED (REC)** |

### Static PASS re-execution

| PC | A3 re-execution | Citation check | Weakness flagged |
|---|---|---|---|
| PC-HBLD-01 | PASS reproduced: remove directives at L38–39. The test (L8 post-install tag; L16–19) asserts only the absence of the edit-SCSS suffix | exact | The test does not guard `*.edit.js`/`*.edit.xml` or `*.dark.scss` removal. The PASS correctly states this gap (REC-HBLD-11) |
| PC-HBLD-03 | PASS reproduced: frontend background SCSS L41–43; primary-variables glob L24–26 | exact | None |
| PC-HBLD-07 | PASS reproduced (528 / 79 / 32 / 47 / 0) | — | None |
| PC-HBLD-08 | PASS reproduced (0-byte init) | — | Probe set narrow; closed by the missing data key |
## 3. Process-rule compliance (MASTER C1B systemic findings 1–5)

Source of the rules: `01_Governance/COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` section "Systemic process findings". Evidence below is from the inputs, the upstream scratch folder `scratchpad/rec_ui4` (read only) and read-only `git log`/`git show`.

| # | Rule | Result for this batch (onboarding, html_builder, web_hierarchy, web_unsplash) | Evidence |
|---|---|---|---|
| 1 | Preserve the A2 `MISSING_REQUIRED_RUNTIME_PROOF` (MRRP) label; do not collapse it into `UNCORROBORATED` | **NOT MET** | None of the four RECs uses the MRRP label in any row. The label is kept only indirectly, where the REC class is UNKNOWN_PENDING_PROOF (whose definition cites MRRP). Where A2 classed a claim MRRP but REC gave it another class, only `UNCORROBORATED` remains: onboarding C11 (CONTRADICTION) and C17 (GAP); web_hierarchy C10 (GAP); web_unsplash C12 (GAP). html_builder has one MRRP claim (C06); it is UNKNOWN_PENDING_PROOF, so it is preserved indirectly only. |
| 2 | Tag any Expected/predicate text added after predeclaration `POST-DECLARATION` | **NOT MET** | 0 `POST-DECLARATION` tags in the four PROOF files. Untagged changes against `predeclared_proof_cases.tsv`: PC-ONBD-05 scope narrowed from "all module .py / any elevation call" to "module runtime code" (tests excluded); PC-UNSP-08 and PC-UNSP-26 steps gained "(mock-resolved)", and PC-UNSP-10 gained "(mock)". Most other rows are wording changes with the same meaning. |
| 3 | REC scans all A1 item classes (BR / states / exceptions / handoffs / gaps / CRQ) | **NOT MET** | The four REC tables reconcile only the claims (Cnn) and A2 omissions (OM). GAP and CRQ items are carried forward in prose. No BR-, state, exception or handoff item is reconciled (0 `BR-` mentions in the four RECs). Effect: onboarding BR-5 and the state line "Panel scope: global → per-company (one way)" still state the negated C11 position; web_unsplash state lines and BR-5 are not updated for REC-UNSP-12/21 and CONTRADICTION-UNSP-1. |
| 4 | REC frozen (sha256 recorded) before PROOF; PROOF header records the REC sha256 it consumed | **NOT MET** | None of the four PROOF headers records a REC sha256 (they give path + item count only). The REC files cite `laneb_search.txt` (sha256 `21b8a78d…0ce7f`), and that file's mtime is 15:13:14Z, after PROOF source fetch began (first `src/` file 15:11:03Z; `blobcheck.txt` 15:11:12Z). REC files were first committed at 15:14:38Z (onboarding), 15:15:22Z (html_builder), 15:16:10Z (web_hierarchy) and 15:17:15Z (web_unsplash), all after PROOF execution started. The html_builder REC was edited again between commits `b31a0e8` and `37823e6` (a one-line correction to a freeze-hash abbreviation; nothing recorded the change), and REC-HBLD-08 cites a PROOF case (PC-HBLD-07). |
| 5 | Cases-file sha256 + UTC timestamp written before first source fetch | **MET (with note)** | `predeclared_proof_cases.tsv` recomputed sha256 = `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307` (MATCH); `predeclared_sha256.txt` and `predeclared_time.txt` = 2026-09-27T15:10:27Z; first source file 15:11:03Z; 67 case IDs present (19 + 8 + 14 + 26). Note: `tree_probe.json` (15:09:19Z, before predeclaration) records a GitHub API tree-listing attempt that returned 403 with no source content. The timestamp evidence still rests on self-written files and mtimes in scratch, not on a committed record. |

## 4. Lineage

| Artifact | Commits (read-only) | Content check |
|---|---|---|
| Lane A | `1ee5230` 14:52:49Z | = intake |
| A1 | `9aba486` 14:56:14Z | = value recorded by A2 |
| A2 | `c4a1ea7` 15:04:40Z | = value recorded by REC |
| REC | `b31a0e8` 15:15:22Z (sha `0fd609ab…`), then `37823e6` 15:16:10Z (= intake `d6efb05e…`) | Edited after PROOF began, and no change record exists |
| PROOF | `0eaeb25` 15:19:09Z | = intake |

Commit subjects are ignored, because MASTER checkpoint commits carry subjects that name other modules. Predeclaration verified (`2203bab7…f307`, 15:10:27Z). Standard-55 sample: REC-HBLD-06 and REC-HBLD-08 are marked "no clear fit", which is acceptable for an asset module. No QID is answered; MVQ is NOT A3-ELIGIBLE.

Overclaim, Lane B and clean room: no runtime claimed as proven; no percentages; no Formal Coverage. No Lane B exists, and none was misused. The PC-HBLD-05 lead observation is correctly excluded from results. Clean room: 0 code fragments; identifiers are used as pointers.

## 5. Defects routed

| ID | Owner | Severity | Defect | Action |
|---|---|---|---|---|
| D-HBLD-A3-1 | REC / PROOF | MED | REC was not frozen before PROOF; it was edited after PROOF started; it cites a PROOF case; and the PROOF header has no REC sha256 (rule 4) | Freeze the REC, record its sha256 in the PROOF header, and remove the PC reference from the REC (or tag it POST-PROOF) |
| D-HBLD-A3-2 | REC | LOW | BR-1, BR-2 and the state/exception/handoff sections were not reconciled (rule 3) | Add REC rows for them. BR-2 should carry the REC-HBLD-11 limitation (the test guards only the edit-SCSS suffix) |
| D-HBLD-A3-3 | REC | LOW | C06 MRRP is kept only through its UNKNOWN_PENDING_PROOF class; the Lane B column shows only UNCORROBORATED (rule 1) | Show the A2 MRRP label explicitly |
| D-HBLD-A3-4 | A1 (advisory) | LOW | "Assets-only" should state that the hard `mail` dependency brings in `mail`'s server surface when this module is installed | Add a scope note at the next A1 revision |

## 6. Runtime / gate-blocked items

- RUNTIME NOT-EXECUTED: PC-HBLD-02 and PC-HBLD-04 (device OFFLINE).
- PC-HBLD-05 is NOT-EXECUTED because its precondition is unmet (cross-module). It is not a runtime item.
- PC-HBLD-06 is INCONCLUSIVE.
- MASTER handoff pending: runtime and gate (W1-B06 HOLD-LOCAL; Formal Coverage not authorized).

## 7. Limitations

One anchor commit. `static/tests/**` and the globbed `static/src/**` trees are not enumerable (no listing API), and A3 fetched no file by a guessed name. There was no runtime and no external contact beyond `raw.githubusercontent.com`. Git was used read-only; inputs were not edited. No percentages; no Formal Coverage; no QID answered.
