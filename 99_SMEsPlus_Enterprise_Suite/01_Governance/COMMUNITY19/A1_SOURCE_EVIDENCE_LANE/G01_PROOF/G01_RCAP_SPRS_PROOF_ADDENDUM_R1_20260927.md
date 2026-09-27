# G01 PLATFORM_BASE — `google_recaptcha` + `base_sparse_field` — PROOF ADDENDUM R1 (remediation)

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF** (addendum only; the original Proof documents are NOT edited) |
| Parents (superseded in part) | `G01_PROOF/G01_GOOGLE_RECAPTCHA_PROOF_20260927.md` sha256 `273400741878d2aa944d7bec9c87f132d97831bda52f82e56b6ddcc069ee194b`; `G01_PROOF/G01_BASE_SPARSE_FIELD_PROOF_20260927.md` sha256 `94237a9c3ac336856c8adbe712b508ea4bf1c3c5c4fd4aab79856d18f83c4d64` (both equal A3 intake) |
| Upstream addenda | A1 R1 `G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_ADDENDUM_R1_20260927.md` sha256 `6926e67b3c97d2c5dbb5fead4dcb75c63a0e25064ef1f86dc3531f06d8381c53`; A2 R1 `G01_A2_REVIEWS/G01_RCAP_SPRS_A2_ADDENDUM_R1_20260927.md` sha256 `86260c80f355d611b95da177b89be32195cbbde7fcd6f8ea983575ca1455a896`; REC R1 `G01_RECONCILIATION/G01_RCAP_SPRS_REC_ADDENDUM_R1_20260927.md` sha256 `e8d748b2d965501f5699325458d73b06d003306e6dad90a6f44f0b6e6c3b89cd` |
| A3 reports | `G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md` sha256 `ff91606234f5b276cc659538b0fa852ac119308c70dbead5c9479de48c63273b`; `G01_A3_CHALLENGES/G01_BASE_SPARSE_FIELD_A3_STATIC_20260927.md` sha256 `2ec7cb8a285e02fe61f2bca1de24fdb52d39ebe6964d0655107be967c5f981cb` |
| Challenge IDs addressed | A3-RCAP-D4 (HIGH), A3-RCAP-D5 (minor), A3-SPRS-D2 (Proof side); Lane A item 12 erratum (origin of A3-RCAP-D1) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` |
| Runtime device | OFFLINE (unchanged since 2026-09-24T12:53Z per `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`) |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/remed_rcap/` |
| Date | 2026-09-27 |
| Status | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean room: neutral summaries, pointers only, no code reproduced. No QID answered, no percentages, no Formal Coverage. No git operations.

## 2. Predeclaration (before execution)

| Item | Value |
|---|---|
| File | `scratchpad/remed_rcap/PROOF_CASES_PREDECLARED_R1.md` |
| sha256 | `ffa4879429731a36276bf1d350e47213a0934a8d5ef6e85e163c12ebe635da1c` (`predeclared_R1.sha256`) |
| Written | 2026-09-27T15:21:07.18Z (`predeclared_R1.ts`; file mtime 15:21:07.18Z) |
| Execution logs | `exec_R1.txt` (started 15:21:21Z) sha256 `f50d8b879691174a6831eb0cda2e5630475228f1d5156ac2e7eb7ff6c0d3d5d4`; `exec_builtin_R1.txt` (15:21:34Z) sha256 `381b2d5b13befc76623f42bae43a7e9f6dab657398583e78335ae107c8011518` |
| Ordering | Predeclaration (15:21:07Z) precedes both execution logs |
| Disclosure | The Step-1 independent re-derivation read the source (fetch log `blob_remed.txt`, 15:18:55Z, sha256 `ad205536b83bef00934e36b9864e358c3336722732501500fc79edb68f1a7f5c`; preliminary built-in check `builtin_eval.txt` sha256 `a10b2ae64dfddcac19ec51c6703007d5c42277fad694e6c08fe84af4b145ad1f`) before the cases were written. Per A3 Challenge 3, predeclaration must precede execution, not reading. To counter the confirmation-bias risk A3 identified in PC-RCAP-06, every new case carries an explicit disconfirming branch (the value the conversion actually receives, the loop scope, the lookup model) |

Blob verification (fresh fetch, HTTP 200, `git hash-object` = recorded): E4 78d5a71c, E5 c2f237bb, E1 0dcee164, A2-X6 21c82bf6, A2-X5 50464416, sparse `models/models.py` f2196226, `models/fields.py` cb26946e, `views/views.xml` 1c199e72 — 8/8 MATCH, re-hashed at execution start (`exec_R1.txt`).

## 3. Replacement / new cases and results

| PC | Replaces / REC | Layer | Expected (predeclared, summary) | Fail condition (predeclared, summary) | Observed | Result |
|---|---|---|---|---|---|---|
| **PC-RCAP-06R** | Replaces PC-RCAP-06 for consumption / REC-RCAP-09R1, 10R1, 11R1 | SOURCE+CONFIG | No default on the min-score read; absent key → false; false → 0.0 with no exception, "abc" raises, "nan" converts; conversion outside guard; with 0.0 no score (missing or ≥0) is "below"; absent parameter loads as 0.7; 0.0 saved as false → deleted/absent | Absent → none/non-convertible; false raises; positive default; conversion guarded; 0.0 persisted; absent loads as 0.0 | E4 L83 reads with no default; getter returns stored value or false (A2-X6 L60, L69, L79); `exec_builtin_R1.txt`: false→0.0, "abc"→raises, "nan"→converts, false/0.0/0.1/0.9 below 0.0 → all false; conversion at L102 outside try L84–98; A2-X5 L268 passes field default (E5 L17 "0.7"), L286–289 converts; L342 zero → false; A2-X6 L94–98 deletes; E1 data list has only the view file | **PASS** |
| **PC-RCAP-30** | New / REC-RCAP-10R1 (C08R1-b) | SOURCE+CONFIG | Save loop covers every config field each save; absent stored (false) ≠ "0.7" → written | Loop limited to changed fields, or absent compares equal to default | A2-X5 L332 iterates all classified config fields; L347 skips only when stored equals form value; L349 writes; built-in check: false vs "0.7" not equal | **PASS** (confidence MED: web-client payload not read) |
| **PC-RCAP-31** | Corrected expected for PC-RCAP-19 / REC-RCAP-09R1, 10R1 | RUNTIME | (a) deleted, (b) 0.0 saved: low-score success and no-score success **accepted**, screen shows 0.7; (c) "abc" stored: unhandled server error | (a)/(b) refused or erroring, screen 0.0; (c) accepted or defined refusal | — | **NOT-EXECUTED** (device OFFLINE) |
| **PC-RCAP-32** | New / REC-RCAP-10R1 | RUNTIME | After (b), an unrelated settings save makes the parameter "0.7"; low score then refused | Parameter still absent, or low score accepted | — | **NOT-EXECUTED** |
| **PC-RCAP-27R** | Replaces PC-RCAP-27 for consumption / REC-RCAP-16 (A3-RCAP-D5) | RUNTIME | Client sends forged forwarding value F, true address T, proxy peer P. (i) proxy mode off → logged/posted IP = P. (ii) proxy mode on → T | (i) F or T used; (ii) F or P used | — | **NOT-EXECUTED** |
| **PC-SPRS-22** | New / REC-SPRS-08R1 (A3-SPRS-D2) | SOURCE | Only container name carried; lookup on (own model, name); missing → user error; present → raw-SQL re-point; compute/inverse access container by name on the record; no type check on resolved row | Model identity carried; lookup on pointer's model; compute/inverse reach another model; type checked | `models.py` L84–88 carries the name only; L59–63 look up by own model + name from a query selecting model, name, id, pointer (L49–55; no type column); L64–69 user error; L70–79 raw-SQL update; `fields.py` L53, L62–71 by name on the record; 0 constraint methods | **PASS** |
| **PC-SPRS-23** | New / REC-SPRS-08R1 (PR-SPRS-10) | RUNTIME | Variant 1: user error at reflection, nothing stored in B; variant 2: re-pointed to A's same-named container | Value stored in B's container, or pointer stays on B with no error | — | **NOT-EXECUTED** |

Totals for this addendum: PASS 3 (PC-RCAP-06R, PC-RCAP-30, PC-SPRS-22); FAIL 0; NOT-EXECUTED 4 (PC-RCAP-31, PC-RCAP-32, PC-RCAP-27R, PC-SPRS-23). No runtime result is claimed or fabricated.

## 4. Status of original cases (not re-declared, not edited)

| Original case | Status after R1 |
|---|---|
| PC-RCAP-06 | Recorded PASS stands as a historical observation: each listed observation is literally true. Its **interpretation** "CON-RCAP-01 and A2 SF-1 are both confirmed on source" (original Proof §4 and §5) is **WITHDRAWN** as an over-read; the predicate omitted the value the conversion receives. Consumers use PC-RCAP-06R |
| PC-RCAP-19 | **Retained exactly as declared.** Still NOT-EXECUTED. Source forecast (not a verdict): when run, cases (a) and (b) are expected to record **FAIL** (the request passes). That FAIL must be preserved; the case must not be re-declared after execution. PC-RCAP-31 carries the corrected expectation |
| PC-RCAP-27 | Retained as declared, NOT-EXECUTED; superseded for consumption by PC-RCAP-27R (falsifiable split) |
| PC-RCAP-07 | PASS stands for the positive-threshold scope only ("below any positive threshold"); it does not cover the absent-parameter state (see PC-RCAP-06R) |
| PC-SPRS-06 | PASS stands (no server-side constraint). Its effect statement "the runtime cross-model setup behaviour is not examined" is amended: the module-scope path is shown by PC-SPRS-22; only core reflection timing and the runtime outcome remain (PC-SPRS-23) |

Amended §5 wording for the rcap Proof (replaces the REC-RCAP-09/10 statements): "PC-RCAP-06R PASS confirms on source that an absent min-score parameter yields an effective threshold of 0.0 with no error while the settings screen shows 0.7; only a non-convertible stored value raises. REC-RCAP-09R1 stays UNKNOWN_PENDING_PROOF and REC-RCAP-10R1/11R1 are GAP until PC-RCAP-31/32 run."

## 5. Effect on REC items

| REC item | Status after PROOF R1 |
|---|---|
| REC-RCAP-09R1 | Source premise confirmed (PC-RCAP-06R PASS); runtime pending (PC-RCAP-31). UNKNOWN_PENDING_PROOF |
| REC-RCAP-10R1 | Source premise confirmed (PC-RCAP-06R, PC-RCAP-30 PASS); runtime pending (PC-RCAP-31, 32). GAP |
| REC-RCAP-11R1 | Source confirmed for both scopes (PC-RCAP-07 positive threshold; PC-RCAP-06R zero effective threshold). GAP |
| REC-RCAP-16 | Runtime case replaced by PC-RCAP-27R; NOT-EXECUTED |
| REC-SPRS-08R1 | Constraint absence (PC-SPRS-06) and re-resolution path (PC-SPRS-22) PASS; runtime outcome pending (PC-SPRS-23). CONTRADICTION vs A1 C08 stands |

## 6. Runtime pack additions

Same environment rules as the original packs (isolated instance at anchor `8d05257d`, vendor test keys only, no production data). PC-RCAP-31 case (c) and the no-score variant need a technical-menu write and a controlled verifier stub — record stub use, since stub replies are not verifier behaviour. PC-RCAP-27R needs a reverse proxy and control of proxy mode. PC-SPRS-23 needs developer-mode field creation and a registry reload/upgrade. Record every FAIL as it occurs; do not re-run to obtain a pass.

## 7. Lane A erratum note — item 12 (Lane A packet NOT edited)

- Packet: `G01_LANE_A_PASS1/G01_GOOGLE_RECAPTCHA_LANE_A_PASS1_20260927.md` sha256 `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479`, item 12 (and G5 reference).
- Erratum: the observation "if the parameter was never saved the conversion appears liable to fail with an unhandled error" is **incorrect**. An absent parameter reaches the conversion as false, which converts to 0.0 without error (PC-RCAP-06R). Only a stored value that the float conversion rejects raises. The companion sentence "a missing score … is effectively below threshold" holds **only for a positive stored threshold**; with the parameter absent it is not below.
- Origin chain recorded: Lane A item 12 → A1 C08 / CRQ-RCAP-02 → A2 C08 verdict + SF-1 + posture row → REC-RCAP-09/10/11 → Proof PC-RCAP-06 interpretation / PC-RCAP-19 expected. Each link is corrected by the R1 addendum of its owner stage.
- Lane A owner may issue its own erratum; this note is a Proof-recorded pointer only.

## 8. Limitations

- Static execution on one anchor; the float-conversion behaviour is a language built-in evaluated locally (Python 3.11.15). Core field-default wrapping, web-client save payload, core proxy handling and core reflection timing were not read.
- No runtime execution; four RUNTIME cases remain NOT-EXECUTED. Original Proof files and Lane A packet untouched.
