# G01 PLATFORM_BASE — `google_recaptcha` + `base_sparse_field` — RED TEAM A3 RE-CHECK of Remediation R1 (STATIC)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent re-check of remediation R1 |
| Independence | This reviewer did not write the original A3 reports (A3-RCAP-D1..D6, A3-SPRS-D1/D2) or any R1 addendum. Source was fetched again into a separate scratch folder (`scratchpad/a3r1_rcap/src/`) and blob-verified. The remediation scratch copies (`remed_rcap/src/`) were **not** reused |
| Scope | STATIC only. RUNTIME cases PC-RCAP-19, 27, 27R, 31, 32 and PC-SPRS-23 are NOT-EXECUTED: neither passed nor failed. The runtime device is OFFLINE |
| Date / intake | 2026-09-27, intake at 15:26:01Z (`scratchpad/a3r1_rcap/intake.sha`) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| **Overall disposition** | **A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route MASTER/Integration Control [process rules 4 and 5, separation of duties, commit subjects]; A2 [independence-note overclaim]; REC [rule-4 citations of Proof, BR4R1/P2R1/F5R1 lineage]; A1 [optional refinements R-6]; Lane A owner [item 12 erratum])** — MASTER HANDOFF PENDING RUNTIME |
| **Suspension decision** | **MASTER MAY LIFT** the suspension of REC-RCAP-09, 10 and 11 **in favour of REC-RCAP-09R1, 10R1 and 11R1**, for static-content consumption. A3 re-derived the R1 content on its own and it holds. None of the residual defects changes a consumed conclusion. The originals stay withdrawn and are kept for lineage only. MASTER consolidation stays BLOCKED on runtime |

### Inputs (sha256 at intake = exit, see §9)

| Input | sha256 |
|---|---|
| Original A3 rcap `G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md` | `ff91606234f5b276cc659538b0fa852ac119308c70dbead5c9479de48c63273b` |
| Original A3 sparse `G01_A3_CHALLENGES/G01_BASE_SPARSE_FIELD_A3_STATIC_20260927.md` | `2ec7cb8a285e02fe61f2bca1de24fdb52d39ebe6964d0655107be967c5f981cb` |
| A1 R1 `G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_ADDENDUM_R1_20260927.md` | `6926e67b3c97d2c5dbb5fead4dcb75c63a0e25064ef1f86dc3531f06d8381c53` |
| A2 R1 `G01_A2_REVIEWS/G01_RCAP_SPRS_A2_ADDENDUM_R1_20260927.md` | `86260c80f355d611b95da177b89be32195cbbde7fcd6f8ea983575ca1455a896` |
| REC R1 `G01_RECONCILIATION/G01_RCAP_SPRS_REC_ADDENDUM_R1_20260927.md` | `e8d748b2d965501f5699325458d73b06d003306e6dad90a6f44f0b6e6c3b89cd` |
| PROOF R1 `G01_PROOF/G01_RCAP_SPRS_PROOF_ADDENDUM_R1_20260927.md` | `8528361c7c6d763d6d9f68b1a3853ae6e83c05c8c4a2cb2f2b6b483a8a791707` |
| Predeclared cases `scratchpad/remed_rcap/PROOF_CASES_PREDECLARED_R1.md` | `ffa4879429731a36276bf1d350e47213a0934a8d5ef6e85e163c12ebe635da1c`. **Verified**: equal to `predeclared_R1.sha256`; mtime 15:21:07.18Z equals `predeclared_R1.ts` |
| MASTER board `COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` | `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42` |
| Frozen banks | rcap `471e0323…d7724` and sparse `2e0e1584…77895c8`, both re-hashed and unchanged |

### A3 source fetch (`scratchpad/a3r1_rcap/blob_a3r1.txt`, 15:26:20–22Z, HTTP 200 each, `git hash-object` equals the recorded blob, 8 of 8)

E4 `addons/google_recaptcha/models/ir_http.py` 78d5a71c · E5 `.../res_config_settings.py` c2f237bb · E1 `.../__manifest__.py` 0dcee164 · X6 `odoo/addons/base/models/ir_config_parameter.py` 21c82bf6 · X5 `odoo/addons/base/models/res_config.py` 50464416 · sparse `models/models.py` f2196226 · `models/fields.py` cb26946e · `views/views.xml` 1c199e72.
Built-in evaluation: `scratchpad/a3r1_rcap/builtin_a3r1.txt`, Python 3.11.15, run by A3 on its own.

Clean room: neutral WHAT/WHY/RISK statements. Identifiers and line numbers are pointers only; no vendor code is reproduced. No QID answered, no percentages, no Formal Coverage claim. Git used read-only. No input edited.

## 2. Task 1 — Independent re-derivation of min-score semantics

| # | Assertion | A3 trace (pointers) | A3 result |
|---|---|---|---|
| S1 | Absent parameter → false | E4 L83 reads with no default. X6 L60 sets the getter default to false. L69 returns stored value or default. L77–79 give an empty result for a missing row | **CONFIRMED** |
| S2 | False → 0.0; score gate off | E4 L102 converts outside the guarded block (L84–98). float(false) = 0.0 with no exception. With threshold 0.0, "below" is false for a missing score (false) and for 0.0, 0.1, 0.9 and 1.0, so the flow proceeds to L105–109 (human) | **CONFIRMED** (no technical error) |
| S3 | Saving 0.0 deletes the parameter | X5 L341–342: a zero float becomes false. L347 skips when the stored value is already absent. Otherwise L349 → X6 L94–98 unlink | **CONFIRMED** |
| S4 | The screen shows 0.7 when the parameter is absent | X5 L266–268 pass the field default (E5 L17 "0.7") as the getter default. L284–286 convert it to 0.7 | **CONFIRMED** |
| S5 | A non-numeric stored value raises | float("abc") raises ValueError at E4 L102, which is unguarded, on the success branch only | **CONFIRMED** |
| S6 | The manifest seeds no parameter | E1 data list holds one view file only | **CONFIRMED** |

### NEW finding (a) — C08R1-b / PC-RCAP-30: "saving any setting from the absent state writes 0.7" (declared MED)

Refutation attempts:
1. *Is the save loop limited to changed fields?* No. `set_values` classifies with no field filter (X5 L303 → L178–228; with the filter unset, every field is classified) and loops over **all** config-parameter fields (L332). The `current_settings` snapshot (L304) is used only for the default and group categories (L316, L323), **not** for config fields. The config comparison is against the **stored** value (L335, L347).
2. *Would the record value be 0.7?* Either the client sends the displayed 0.7, or it omits the field and the record takes its default through the same `default_get` path (L268 → 0.7). **Both paths converge on 0.7.** This narrows the "web-client payload not read" caveat the remediation gave.
3. *Does absent compare equal to "0.7"?* No. The stored value is false; the form value becomes "0.7" (L342). "False" and false both differ from "0.7" (L347), so L349 → X6 L100–102 creates the parameter. A3 evaluation: `form=0.7, stored=absent → set_param('0.7') create`.

**Result: UPHELD, not refuted.** A3 confidence is MED: core field-default wrapping, any client onchange and access behaviour for group-restricted fields on save were not read. Risk: an unrelated settings save silently turns a gate that is off (0.0) into 0.7, with no explicit edit and no admin intent.

### NEW finding (b) — C08R1-c: "nan" disables the gate; above-range refuses every success

Refutation attempts: float("nan") and float("NaN") convert without error. Every `score < nan` is false, so every success passes (gate off, silently). "1.5" or "inf" makes every success score (≤ 1.0) "below", so every success is refused as a bot. There is no range validation (E5 L13–19 give only help text; no constraint in module scope). The verifier's 0–1 scale rests on help text only (E5 L18) and is outside source scope.
**Result: UPHELD** (conversion HIGH; verifier scale MED).

### A3 refinements not stated by R1 (R-6, LOW, non-blocking; route A1 for optional note)

- R-6a: A stored unconvertible value shows on the screen as **0.0** (X5 L286–289 fall back with a warning). The next unrelated settings save then **deletes** it (form 0.0 → false ≠ stored text → unlink; A3 evaluation `form=0.0, stored='abc' → unlink`). So the error state turns silently into gate-off. The screen also diverges in this state: it shows 0.0 while the enforced result is an error.
- R-6b: A stored negative value (for example "-1") also disables the gate. An out-of-scale value such as 1.5 **is reachable through the screen** (no range check). C08R1-c says only that *unconvertible text* needs a non-screen write, which is correct.
- R-6c: A verifier reply whose score is JSON null reaches E4 L102 as none, and comparing none with a number raises (A3 evaluation: TypeError), unguarded. This depends on the verifier and is observation only; the PC-RCAP-31 stub variant covers a *missing* score, not a null one.

## 3. Task 2 — Original defect dispositions

| Defect | Sev. | Remediation | A3 check | Disposition |
|---|---|---|---|---|
| A3-RCAP-D1 (A1 C08 / CRQ-RCAP-02; origin Lane A item 12) | HIGH | C08 WITHDRAWN (CONTRADICTED-FROM-SOURCE) → **C08R1-a/b/c**; C09 → C09R1; BR4 → BR4R1; P2 → P2R1-a/b; F5 → F5R1; CON-RCAP-01 → CON-RCAP-01R1; CRQ-RCAP-02 → **02R1** + new **CRQ-RCAP-08** | Every R1 statement matches §2. The supersede map is complete in the A1 addendum §3. The Lane A erratum exists only as a pointer recorded by Proof (§7); the Lane A owner has not issued one | **CLOSED** (content). Residual R-5 (Lane A erratum, LOW) |
| A3-RCAP-D2 (A2 SF-1, posture row) | HIGH | SF-1 → **SF-1R1**; posture row split into three rows; C08 re-verdicted NOT_VERIFIED for the absent branch; C09 → PARTIAL; counts 17/2/0 → 15/3/1 plus 4 R1 claims VERIFIED | Counts are arithmetically consistent with the original A2 (L75). Split rows match §2 | **CLOSED** (content). Residual R-3 (independence note) |
| A3-RCAP-D3 (REC-RCAP-09/10/11) | HIGH | **REC-RCAP-09R1** (UNKNOWN_PENDING_PROOF), **10R1** (GAP), **11R1** (GAP) with an explicit MASTER consumption rule; originals kept for lineage. Class counts 10/11/1/8 → 9/12/1/8 (total 30, consistent) | The content matches §2. The no-score-passes note is present | **CLOSED** (content). Residual R-2 (rule 4) and R-4 (rule 3 lineage) |
| A3-RCAP-D4 (Proof PC-RCAP-06 predicate, PC-RCAP-19 expected, §5 wording) | HIGH | **PC-RCAP-06R** predeclared with a disconfirming branch; original PC-RCAP-06 PASS kept as history and its interpretation withdrawn; §5 wording amended; **PC-RCAP-19 kept as declared**; PC-RCAP-31 carries the corrected expectation; PR-RCAP-02 → **02R1 + 13** (the original is not deleted) | See §4. The original Proof sha256 `27340074…ee194b` is unchanged, so PC-RCAP-19 was not edited | **CLOSED** |
| A3-RCAP-D5 (PC-RCAP-27 unfalsifiable) | Minor | **PC-RCAP-27R**: proxy mode off/on split with distinct F/T/P (PR-RCAP-10R1) | Falsifiable: each mode has one expected address and two distinct fail addresses. The core proxy handling was not read, so whether (ii) resolves to T is a runtime question | **CLOSED** (declaration level) |
| A3-RCAP-D6 (Q030/Q033 "no evidence") | Minor | Q030 → REC-RCAP-03, and Q033 → REC-RCAP-17/26, as partial static lineage (not answered). Mapped 34 → 36; no-evidence 8 → 6. Q009 and Q008 re-pointed to R1 items | Consistent with the original list at REC L102–103 | **CLOSED** |
| A3-SPRS-D1 (Q024/Q035) | Minor | Q024 → REC-SPRS-04 and Q035 → REC-SPRS-05, both partial static. Mapped 29 → 31; no-evidence 12 → 10 | Consistent with the original REC L97–98 | **CLOSED** |
| A3-SPRS-D2 (A2 SF-1 wording / PC-SPRS-06 effect) | Minor | **SF-1R1-SPRS**; **REC-SPRS-08R1** (CONTRADICTION kept); **PC-SPRS-22** (SOURCE) and **PC-SPRS-23** / PR-SPRS-10 (RUNTIME); PC-SPRS-06 effect statement amended | See §4 | **CLOSED** |

## 4. Task 3 — Re-execution of static cases (A3's own copies, against the predeclared text in file `ffa48794…35da1c`)

| PC | Predeclared elements | A3 observation | A3 result |
|---|---|---|---|
| **PC-RCAP-06R** | E1 no default; E2 absent → false; E3 false → 0.0, "abc" raises, "nan" converts; E4 conversion outside the guard, and no score is "below" 0.0; E5 absent loads 0.7, and 0.0 is saved as false → deleted | E1: E4 L83. E2: X6 L60, L69, L79. E3: `builtin_a3r1.txt`. E4: try at L84–98, compare at L102, all "below 0.0" results false. E5: X5 L268, L286, L342, L347; X6 L94–98. No fail element observed | **PASS (agrees)** |
| **PC-RCAP-30** | The loop covers every config field; absent (false) ≠ "0.7" → written | X5 L303/L178–228 (no filter), L332, L335, L347, L349; evaluation: create "0.7". Neither fail element (loop limited to changed fields; absent equal to default) is observed | **PASS (agrees)**, MED |
| **PC-SPRS-22** | Only the name is carried; lookup on (own model, name); missing → user error; present → raw-SQL re-point; compute and inverse by name on the record; no type check | models.py L84–88 set only the container name. L49–55 query model, name, id and pointer, with no type column. L60–63 look up on the reflected model's own name and the sparse name. L64–69 raise a user error. L70–79 run a raw SQL update. fields.py L53 and L62–71 access by name on the record. No constraint in module scope; `views.xml` L12 is the only view domain | **PASS (agrees)** |
| **PC-RCAP-19** | (original, RUNTIME) Expected "unhandled server error in both cases, and the 0.0 save removes the parameter"; Fail "request passes, defined refusal, or parameter persists" | The case is still NOT-EXECUTED, and the original Proof file is unchanged. The Proof addendum §4 records a **source forecast** (not a verdict) that (a) and (b) will record **FAIL** when run, because the request passes. It says the FAIL must be preserved and the case not re-declared. It is **not re-labelled**, and the corrected expectation lives only in the separate PC-RCAP-31. A3 note: the "0.0 removes the parameter" element is forecast to hold (S3). The FAIL comes from the "request passes" fail element | **CONFIRMED kept as declared, predicted FAIL** |

Predeclared-text fidelity (rule 2): A3 compared the Expected and Fail summaries in the Proof addendum §3 with the predeclared file for all seven cases. No Expected text was added beyond the declaration. The "E1 data list" (manifest) observation in the PC-RCAP-06R Observed column is an observation, not an expectation. **COMPLIANT.**

## 5. Task 4 — Disclosure adjudication

### 5.1 Source read before case declaration

Timeline from files and logs:

| Time | Event |
|---|---|
| 15:18:55Z | Remediation source fetch (`blob_remed.txt`) |
| 15:19:34Z | Preliminary built-in check (`builtin_eval.txt`) |
| 15:20:41Z | C1-B board publishes rule 5 (commit 57c46fe at 15:20:45Z) |
| 15:21:07Z | Cases predeclared (`ffa48794…`) |
| 15:21:21Z / 15:21:34Z | Proof execution logs |
| 15:22:39Z | A1 R1 |
| 15:23:30Z | A2 R1 |
| 15:24:11Z | REC R1 |
| 15:25:07Z | PROOF R1 |

- The disclosure is **accurate and complete**: the source was read, and a preliminary built-in evaluation was run, before declaration.
- On its face this breaches **rule 5** ("cases file sha256 + UTC timestamp must be written before first source fetch"). Mitigation: the rule was published **after** that fetch (15:20:41Z against 15:18:55Z), and the original A3 had accepted "predeclare before execution, not before reading".
- **Materiality: NOT MATERIAL to the static results.** A3 independently re-executed all three static cases from its own fetch and got the same outcomes. Every new case carries a falsifiable disconfirming branch, and A3 found no PASS that was false. The four RUNTIME cases are unaffected, because nothing ran.
- Recorded as a disclosed process deviation, R-1 (LOW).

### 5.2 One controller wrote all four owner-stage addenda (separation of duties)

Evidence that one controller wrote them all:
- All four addenda share one scratch folder (`remed_rcap/`) and one blob log (`blob_remed.txt`).
- The A1 addendum (15:22:39Z) cites the **Proof execution log** `exec_builtin_R1.txt` (15:21:34Z) as evidence.
- The A2 addendum says A2 "re-traced the paths on its own re-fetched copies", but cites only the shared `remed_rcap/blob_remed.txt`. No separate A2 fetch exists.
- All four were written within 2.5 minutes, **after** Proof execution.
- Git author identity is shared (acknowledged in C1-B).

**Adjudication:**
- **MATERIAL to process and independence**: the A2 R1 and REC R1 verdicts cannot count as independent verification of A1 R1. The A2 independence note is an overclaim (R-3). The stage order A1 → A2 → REC → PROOF was inverted, because Proof executed before its upstream addenda existed.
- **NOT MATERIAL to static content**: the corrected conclusions are deterministic on the anchored source, and this independent A3 re-check reproduces every one of them (§2, §4). A3 therefore provides the independent check that the single-author chain lacked.
- Condition: the four RUNTIME cases (PC-RCAP-31, 32, 27R, PC-SPRS-23) should be executed or witnessed by a party other than the R1 author, and A3 runtime review must remain independent (route MASTER/Integration Control).

## 6. Task 5 — Process rules (C1-B) and clean room

| Rule | Check | Result |
|---|---|---|
| 1. Do not collapse A2 `MISSING_REQUIRED_RUNTIME_PROOF` into UNCORROBORATED | The label is absent from both original A2 reviews and from the A2 R1. The REC R1 Lane B column uses only NOT_APPLICABLE or UNCORROBORATED, never FAIL | **N/A — COMPLIANT** |
| 2. Post-declaration Expected text must be tagged | §4 fidelity check | **COMPLIANT** |
| 3. REC must scan all A1 item classes | REC R1 carries C08R1-a/b/c, C09R1, CON-RCAP-01R1, CRQ-RCAP-02R1 and CRQ-RCAP-08. **BR4R1, P2R1-a/b and F5R1 are not named** (BR4 is implicit through REC-RCAP-11R1; P2 and F5 had no original REC row) | **PARTIAL — R-4 (LOW, REC)** |
| 4. REC frozen (sha256) before PROOF executes; PROOF header records the REC sha256 it consumed | The PROOF header records REC R1 `e8d748b2…` (matches). However, REC R1 was written at 15:24:11Z, **after** Proof execution at 15:21:21Z, and it **cites Proof results** ("source premise confirmed by PC-RCAP-06R", REC-RCAP-09R1 class column; the proof-link columns). The rule was already published (15:20:41Z) | **NOT COMPLIANT — R-2 (MED, process; REC + MASTER)**. Content is unaffected (§5.2) |
| 5. Cases sha256 + UTC timestamp before first source fetch | The fetch at 15:18:55Z came before declaration at 15:21:07Z. This is disclosed, and the rule was published at 15:20:41Z | **DEVIATION DISCLOSED — R-1 (LOW)** |
| C1-B Integration Control corrective rule (accurate commit subjects; checkpoint bodies list paths) | The R1 addenda were committed under subjects naming other modules: e9e22a8 "A3 G01: portal, utm" (A1 R1); 749f1a4 "A3 … phone_validation, privacy_lookup" (REC R1); c17226c "A3 … auth_signup, base_setup" (PROOF R1); c384f73 "checkpoint" (A2 R1). The bodies do list the paths | **PARTIAL — R-7 (LOW, MASTER/Integration Control)**. Content lineage: each file has a single commit, and the current sha256 equals intake |

**Clean-room scan**: the four R1 addenda were grepped for code constructs (definitions, attribute access, imports, SQL verbs, core method names, fenced code, parameter keys). There were **0 hits**. The predeclared scratch file uses core method names and a standard HTTP header name only as pointers, with no code blocks. This report uses pointers only. **UPHELD.**

## 7. Residual defects (route)

| ID | Sev. | Owner | Residual | Required action | Blocks suspension lift? |
|---|---|---|---|---|---|
| R-1 | LOW | MASTER / Integration Control | Rule 5 deviation (source read before declaration). Disclosed; the rule post-dates the fetch | Record it as a disclosed deviation. No re-declaration needed for static cases | No |
| R-2 | MED | REC (+ MASTER) | Rule 4: REC R1 was finalised after Proof executed and cites Proof results | REC to issue a short note that strips the Proof-result wording from the REC classes, or MASTER to record the deviation. Future R-rounds freeze REC before Proof executes | No (content independently confirmed) |
| R-3 | MED | A2 (+ MASTER) | Single-author R1 chain. The A2 independence note overclaims ("own re-fetched copies"). A1 R1 cites a Proof log | A2 to correct the independence note. MASTER to record that R1 A1/A2/REC/PROOF have one author and that independence rests on A3 R1. Runtime R1 cases to be executed or witnessed by a party other than the R1 author | No |
| R-4 | LOW | REC | BR4R1, P2R1-a/b and F5R1 are not named in the REC R1 lineage | Add a lineage line | No |
| R-5 | LOW | Lane A owner | The item 12 erratum exists only as a pointer recorded by Proof | Lane A to issue its own erratum, or MASTER to accept the pointer | No |
| R-6 | LOW | A1 (optional) | Unstated refinements: unconvertible value shows 0.0 and is deleted by an unrelated save; negative values; screen-reachable out-of-scale values; null-score comparison raises | Optional note, or fold into CRQ-RCAP-02R1/08 | No |
| R-7 | LOW | MASTER / Integration Control | Commit subjects for the R1 addenda name other modules | Apply the C1-B commit rule | No |

## 8. Overall

**A3 R1 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC [R-2, R-4], A2 [R-3], MASTER/Integration Control [R-1, R-2, R-3, R-7], Lane A owner [R-5], A1 optional [R-6]) — MASTER HANDOFF PENDING RUNTIME.**

- All eight original A3 defects (A3-RCAP-D1..D6, A3-SPRS-D1/D2) are **CLOSED** on content.
- Both new remediation findings survive A3's refutation attempts: (a) re-arm on any save, MED; (b) "nan" gives gate-off and above-range gives refuse-all.
- PC-RCAP-06R, PC-RCAP-30 and PC-SPRS-22 re-execute to PASS.
- PC-RCAP-19 is kept as declared, with a forecast FAIL and no re-label.
- **MASTER MAY LIFT the suspension of REC-RCAP-09/10/11 in favour of REC-RCAP-09R1/10R1/11R1.** MASTER must consume only the R1 items together with the REC R1 consumption rule. The residuals are process and lineage items that do not change any consumed conclusion.
- MASTER consolidation remains BLOCKED on runtime: PC-RCAP-19, 27R, 31, 32 and PC-SPRS-23 are NOT-EXECUTED.

## 9. Limitations and exit

- Static only, on one anchor. Not read: core field-default wrapping, the web-client settings payload and onchange, the core proxy handling, core reflection timing for manual fields, and the verifier's score scale. The float behaviours are language built-ins that A3 evaluated locally (Python 3.11.15).
- Dispatch time of the R1 remediation relative to the C1-B publication is not recorded in the inputs. Rule applicability in §6 rests on file and commit timestamps only.
- No inputs were edited, and git was used read-only. No Formal Coverage claim, no percentages and no QID answered.
- Exit: all inputs listed in §1 were re-hashed at exit and are identical (`scratchpad/a3r1_rcap/exit.sha`).
