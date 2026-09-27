# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `phone_validation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_PHONE_VALIDATION_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `phone_validation` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/phone_validation/` |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_PHONE_VALIDATION_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `c70aae333f7a25b558383945b2cca58a66816413eb079c6225161075a50b8a80`. This **equals** the `bank_files` entry in `FREEZE_W1-B10.json` (manifest sha256 `049aa570fdf26c11ec7289e33d9fb9675399f7410a140761aa00c248243956d8`). Freeze hash `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010`. W1-B10 is **ELIGIBLE** per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` (row W1-B10: "ELIGIBLE (floor delta)"; sha256 of gate file `52430ca1…810e2`) |
| Join key | MODULE `phone_validation` + QID + freeze hash above. The mapping is lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (29 REC items; 3 CONTRADICTION items carried into Proof, none closed by REC) |

### 0.1 Input intake (immutable; sha256 recorded at intake 2026-09-27 15:04:27 UTC)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_PHONE_VALIDATION_A1_PACKAGE_20260927.md` | `e128cb2e9905aed013c9447c922441d4680c46467b7355f92ce01d14e0c003b0` | Matches the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_PHONE_VALIDATION_A2_REVIEW_20260927.md` | `60bccae9c9946fc2e0c82d5c546006fa3ce15b14ce51fbc68c65aec38f9b33ec` | Disposition "A2 VERIFIED WITH FINDINGS". 20 claims (17 VERIFIED, 3 PARTIAL). 10 proof requirements (PR-PHON-01..10) |
| Lane A packet | `G01_LANE_A_PASS1/G01_PHONE_VALIDATION_LANE_A_PASS1_20260927.md` | `069aca0017cae09ae1bddb28f46299671080d36ecbc869b5b1d1923cc998b888` | Matches the hash recorded in both the A1 and A2 headers |
| Question bank | see header | `c70aae33…0a50b8a80` | Equals FREEZE_W1-B10 `bank_files` entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B10.json` | `049aa570fdf26c11ec7289e33d9fb9675399f7410a140761aa00c248243956d8` | freeze_hash `0d7f6e94…1222010`; equals the manifest sha256 cited by A2 |

### 0.2 Lane B evidence-pool search (recorded 2026-09-27 15:04:47 UTC)

- Command: `grep -ril phone_validation /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite`. It returned 29 files: the Lane A, A1 and A2 artifacts for this module (and privacy_lookup's, which cite it for the cross-module edge note); G01 static-intake/checkpoint files; GMVQ freeze/status/review files; and inventory CSVs under `V2.0/THAI/.../Evidence_CSV`, `07_Output_From_AI` and `03_Architecture` (source/dump inventories, not runtime observations).
- Filtering those hits for `lane_b|laneb|gemini|runtime|evidence_pool|observ` returned **no match** (rc=1).
- `find /home/user/AI-Collaboration-Hub` for names `*lane_b*`, `*gemini*`, `*evidence_pool*` returned **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `phone_validation`**. Absence is not a failure. Every Lane B cell below is UNCORROBORATED or NOT_APPLICABLE.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited.

## 1. Classification rules (predeclared; same rules as the G01 `base_automation` REC)

- **MATCH**: A1 and A2 agree, and a source re-read supports the claim. Runtime corroboration is optional.
- **GAP**: evidence is missing, and no static or runtime proof in scope can settle it now.
- **CONTRADICTION**: A1 and A2 disagree (A2 PARTIAL correction), or the source disagrees with intent the source itself declares (comment, help text, ACL declaration).
- **UNKNOWN_PENDING_PROOF (UPP)**: A1 and A2 agree at source level (or A2 adds a statically predicted omission), but the claim or its stated risk is inherently runtime- or config-dependent.
- **Lane B column**: UNCORROBORATED (behavioural, no runtime observation) or NOT_APPLICABLE (structural or source-only). Never FAIL for absence.
- **Scope of REC items**: A1 claims C01–C20; A2 omissions O-PHON-01..07 as new items (O-PHON-06 folded into C20, which it corrects); carried A1 gaps not absorbed by a claim (GAP-PHON-01, -07, -09). Folds: GAP-02→C17, GAP-03→C07, GAP-04→C11, GAP-05→C15, GAP-06→C16, GAP-08→C05. A2 candidate contradictions: X1→C07/O-03, X2→C05.
- **Severity**: A2's severities are preserved. The instruction set lists four phone items as "new HIGH"; A2 rates SF-PHON-01 HIGH and SF-PHON-02/03/04 MED. REC records A2's rating and gives a PDPA note for all four (section 4).

## 2. Reconciliation table

PC = proof case in the PROOF package. Static cases PC-PHON-11..26 were executed; runtime cases PC-PHON-01..10 are pending.

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (MODULE `phone_validation`) |
|---|---|---|---|---|---|---|---|---|
| REC-PHON-01 | C01 | Hidden auto-install module; deps base+mail; validation, list, mixin; no controllers/cron/settings / MED | VERIFIED | MATCH | Manifest re-read; no cron/settings data | NOT_APPLICABLE | — | — (general scope) |
| REC-PHON-02 | C02 | DB-unique on number; sanitized on create/write/add/remove / HIGH | VERIFIED (+SF-01, SF-02) | UPP | Uniqueness mechanism source-confirmed. A2 shows the stored value depends on the acting user (fallback and country). Runtime effect pending | UNCORROBORATED | PC-11, PC-12, PC-16; PC-01, PC-10 | Q004, Q014, Q015, Q032 |
| REC-PHON-03 | C03 | No company dimension, no record rules; DB-wide list / HIGH | VERIFIED | UPP | Absence of company field/rules confirmed. Cross-company effect is runtime | UNCORROBORATED | PC-24; PC-04 | Q009, Q029, Q030 |
| REC-PHON-04 | C04 | System-only ACL with zero row for all / HIGH | VERIFIED | MATCH | Three ACL rows re-read (PC-24) | UNCORROBORATED | PC-24 | Q021 |
| REC-PHON-05 | C05 (+GAP-08, X2) | Sudo set/reset helpers bypass ACL; callers not visible / HIGH | VERIFIED | UPP | Sudo confirmed (PC-14). Reachability for non-admins lies in other modules | NOT_APPLICABLE | PC-14; PC-03 | Q021, Q023, Q024, Q036 |
| REC-PHON-06 | C06 | Flag computed with sudo; existence oracle for internal users / HIGH | VERIFIED (aggravated by SF-04) | UPP | Sudo compute + group restriction confirmed (PC-17). Oracle exposure is runtime | UNCORROBORATED | PC-17; PC-04 | Q009, Q010, Q028, Q031 |
| REC-PHON-07 | C07 (+GAP-03, X1) | Wizard entry pre-check; comment admits wizard rights "not working as expected" / HIGH | **PARTIAL** — RISK framing incomplete: apply not elevated, wizard system-only, so list ACL is effective control | **CONTRADICTION** (A1 vs A2; and source comment vs declared ACL) | A1 frames a pre-check-only control; A2 narrows X1 to defense-in-depth. Source re-read supports A2 (PC-18 PASS). The in-code comment contradicts the declared system-only wizard ACL. Both statements preserved | UNCORROBORATED | PC-18; PC-02 | Q021, Q022, Q024 |
| REC-PHON-08 | C08 | Possible+valid checks; one retry for too-long / HIGH | VERIFIED | MATCH | Parse path re-read | UNCORROBORATED | — | Q002, Q003, Q004 |
| REC-PHON-09 | C09 | Library absent → raw passthrough, one info log / HIGH | VERIFIED | UPP | Fallback confirmed (PC-19). Storage of raw values is runtime/config | UNCORROBORATED | PC-19; PC-05 | Q003, Q014, Q037 |
| REC-PHON-10 | C10 | E164/RFC3966/INTERNATIONAL/NATIONAL selection / MED | VERIFIED | MATCH | Format branch re-read | NOT_APPLICABLE | — | Q001, Q005 |
| REC-PHON-11 | C11 (+GAP-04) | Record country → partner fields (last wins) → company / HIGH | VERIFIED | UPP | No-break loop confirmed (PC-21). Interpretation outcome is runtime | UNCORROBORATED | PC-21; PC-07 | Q001, Q006, Q037 |
| REC-PHON-12 | C12 | Add collapses duplicates, reactivates archived / HIGH | VERIFIED | MATCH | Inactive-inclusive search and reactivation re-read (PC-25) | UNCORROBORATED | PC-25 | Q010, Q011, Q032 |
| REC-PHON-13 | C13 | Remove archives; unknown numbers created archived; reason logged / HIGH | VERIFIED (API only; ACL allows hard delete → O-05) | MATCH | Re-read (PC-25). Wording "never deletes" holds for the API as A2 notes | UNCORROBORATED | PC-25 | Q010, Q012, Q013 |
| REC-PHON-14 | C14 | Search falls back to raw term / HIGH | VERIFIED | UPP | Fallback confirmed (PC-19, PC-15). Matching of raw stored strings is runtime | UNCORROBORATED | PC-19; PC-05 | Q016, Q018 |
| REC-PHON-15 | C15 (+GAP-05) | One sanitized value; last-field-wins flag loop / HIGH | VERIFIED | UPP | Loop overwrite and single sanitized comparison confirmed (PC-20). Effect on a two-number record is runtime | UNCORROBORATED | PC-20; PC-06 | Q006, Q007, Q008, Q025, Q026, Q027 |
| REC-PHON-16 | C16 (+GAP-06) | Min length 3, +/00, strip, error on no phone fields, index-missing skip / MED | **PARTIAL** — error only when no stored number fields **and** the sanitized index is missing | **CONTRADICTION** (A1 vs A2) | A1 states a broader error condition; source re-read supports A2 (PC-22 PASS). Both preserved. Index-state effect is runtime | UNCORROBORATED | PC-22; PC-08 | Q016, Q017, Q018, Q019, Q020, Q040 |
| REC-PHON-17 | C17 (+GAP-02) | Portal deactivation adds numbers without sudo; log names both users / HIGH | VERIFIED | UPP | No sudo in override confirmed; base hook located (PC-23). Caller elevation not in files read | UNCORROBORATED | PC-23; PC-09 | Q035 |
| REC-PHON-18 | C18 | Number and active tracked; messages on add/remove; no typed event / MED | VERIFIED | MATCH | Re-read | UNCORROBORATED | — | Q035 |
| REC-PHON-19 | C19 | Partner phone reformatted to INTERNATIONAL in change handler / MED | VERIFIED (UI handler only) | MATCH | Re-read | UNCORROBORATED | — | Q005, Q027 |
| REC-PHON-20 | C20 (+O-06) | 8 loaders + 2 version-gated hooks / MED | **PARTIAL** — all 8 loaders are version-gated too | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-26 PASS). Both preserved | NOT_APPLICABLE | PC-26 | Q040 |
| REC-PHON-21 | O-PHON-01 (SF-01) | (not stated) | **HIGH** — unformattable input → empty → create falls back to acting user's own number → wrong subject suppressed | UPP | Full static path confirmed (PC-11, PC-12, PC-13, PC-14, PC-15 PASS), plus a mirror path that un-suppresses the acting user (Proof R1). Runtime effect pending | UNCORROBORATED | PC-11..15; PC-01 | Q003, Q008, Q013, Q014, Q023 |
| REC-PHON-22 | O-PHON-02 (SF-02) | (not stated) | MED — canonical form depends on acting user's country | UPP | Formatter runs on the acting user record (PC-16 PASS). Two-entry outcome is runtime | UNCORROBORATED | PC-16; PC-10 | Q001, Q002, Q004, Q038 |
| REC-PHON-23 | O-PHON-03 (SF-03) | (C07 partial) | MED — wizard apply non-elevated; wizard system-only; narrows X1 | UPP | Confirmed statically (PC-18). Direct-URL behaviour is runtime | UNCORROBORATED | PC-18; PC-02 | Q021, Q022 |
| REC-PHON-24 | O-PHON-04 (SF-04) | (C06 partial) | MED — searchable flag gives bulk enumeration to internal users | UPP | Raw-SQL search on active entries, group = internal user (PC-17 PASS). No A2 PR; no runtime case predeclared in this run (post-hoc proposal in Proof §6) | UNCORROBORATED | PC-17 | Q031 |
| REC-PHON-25 | O-PHON-05 (SF-06) | (C13 "never deletes") | MED — admin hard delete erases entry and chatter | MATCH | ACL grants unlink to system group (PC-24). Declarative | UNCORROBORATED | PC-24 | Q035 |
| REC-PHON-26 | O-PHON-07 | (C03) | MED — no consent/lawful-basis/company/channel attributes | MATCH | Entry model holds number + active only (+ chatter). Structural | NOT_APPLICABLE | PC-24 (context) | Q030 |
| REC-PHON-27 | GAP-PHON-01 | Vendored per-region metadata not fetched | VERIFIED as gap | GAP | Not read in this run | NOT_APPLICABLE | — | Q040 |
| REC-PHON-28 | GAP-PHON-07 | JS/static assets and tests not reviewed | VERIFIED as gap | GAP | Not read | NOT_APPLICABLE | — | — |
| REC-PHON-29 | GAP-PHON-09 | Concurrency of simultaneous add/remove | VERIFIED as gap | GAP | Not statically assessable; no A2 PR | NOT_APPLICABLE | — | Q033, Q034 |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 10 | C01, C04, C08, C10, C12, C13, C18, C19, O-05, O-07 |
| CONTRADICTION | 3 | C07 (A1 vs A2; comment vs ACL), C16 (A1 vs A2), C20 (A1 vs A2) |
| UNKNOWN_PENDING_PROOF | 13 | C02, C03, C05, C06, C09, C11, C14, C15, C17, O-01, O-02, O-03, O-04 |
| GAP | 3 | GAP-PHON-01, GAP-PHON-07, GAP-PHON-09 |
| **Total** | **29** | 20 A1 claims + 6 A2 omissions (O-06 folded into C20) + 3 carried gaps |

Lane B column: UNCORROBORATED 21, NOT_APPLICABLE 8 (C01, C05, C10, C20, O-07, GAP-01, GAP-07, GAP-09). No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- C07: A1's statement (pre-check at one entry point; wizard rights admitted broken) and A2's narrowing (apply not elevated; wizard system-only) are both kept verbatim in their packages. The source comment conflicts with the declared ACL. Static re-read supports A2 (PC-18). Runtime PC-02 pending.
- C16 and C20: A1 wording is broader/narrower than source; A2's correction is source-supported (PC-22, PC-26). Items stay CONTRADICTION until A3 reviews them.

## 3. QID lineage map (frozen bank W1-B10; lineage only, not answers)

Join key: MODULE `phone_validation` + QID + freeze hash `0d7f6e94acde38662de420f8947ffaa1ab04cddaaec43516e46b441ce1222010`. A mapping means "this REC item is topically relevant evidence". It does not answer the QID or satisfy any disconfirming observation. **Lineage is A3-eligible** (W1-B10 ELIGIBLE; bank sha256 equals freeze entry).

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-PHONE-VALIDATION-Q001 | Destination-country interpretation | REC-10 (C10), REC-11 (C11), REC-22 (O-02) |
| G01-PHONE-VALIDATION-Q002 | Stable across user default country | REC-08 (C08), REC-22 (O-02) |
| G01-PHONE-VALIDATION-Q003 | Malformed not silently normalized into another number | REC-21 (O-01), REC-08 (C08), REC-09 (C09) |
| G01-PHONE-VALIDATION-Q004 | Equivalent forms → one identity | REC-02 (C02), REC-08, REC-22 (O-02) |
| G01-PHONE-VALIDATION-Q005 | Formatting keeps digits | REC-10, REC-19 (C19) |
| G01-PHONE-VALIDATION-Q006 | Country change recomputes identity | REC-11, REC-15 (C15) |
| G01-PHONE-VALIDATION-Q007 | Multi-field precedence | REC-15 |
| G01-PHONE-VALIDATION-Q008 | Explicit fallback when primary empty/invalid | REC-15, REC-21 (O-01) |
| G01-PHONE-VALIDATION-Q009 | Block applies to all records of same identity in scope | REC-03 (C03), REC-06 (C06) |
| G01-PHONE-VALIDATION-Q010 | Inactive entry not an active block | REC-06, REC-12, REC-13 |
| G01-PHONE-VALIDATION-Q011 | Re-add reactivates | REC-12 |
| G01-PHONE-VALIDATION-Q012 | Idempotent removal | REC-13 |
| G01-PHONE-VALIDATION-Q013 | Removing never-blocked number does not enable a different number | REC-13, REC-21 (O-01; Proof R1 mirror path) |
| G01-PHONE-VALIDATION-Q014 | Invalid input not persisted as identity | REC-02, REC-09, REC-21 |
| G01-PHONE-VALIDATION-Q015 | Edit revalidates | REC-02 |
| G01-PHONE-VALIDATION-Q016 | Search punctuation/prefix equivalence | REC-14 (C14), REC-16 (C16) |
| G01-PHONE-VALIDATION-Q017 | Minimum search length | REC-16 |
| G01-PHONE-VALIDATION-Q018 | Set-based search operations | REC-14, REC-16 |
| G01-PHONE-VALIDATION-Q019 | No phone source fails clearly | REC-16 |
| G01-PHONE-VALIDATION-Q020 | Index/upgrade state does not change truth | REC-16 |
| G01-PHONE-VALIDATION-Q021 | Only governed authority can unblock | REC-04, REC-05, REC-07, REC-23 |
| G01-PHONE-VALIDATION-Q022 | No bypass through alternate wizard/action | REC-07, REC-23 |
| G01-PHONE-VALIDATION-Q023 | Record actions use canonical identity | REC-05, REC-21 |
| G01-PHONE-VALIDATION-Q024 | Record unblock reverses same identity | REC-05, REC-07 |
| G01-PHONE-VALIDATION-Q025 | Phone+mobile indicator clarity | REC-15 |
| G01-PHONE-VALIDATION-Q026 | Secondary identity does not escape | REC-15 |
| G01-PHONE-VALIDATION-Q027 | Phone change updates derived state | REC-15, REC-19 |
| G01-PHONE-VALIDATION-Q028 | Propagation to blacklisted equivalent | REC-06 |
| G01-PHONE-VALIDATION-Q029 | No crossing of customer boundary | REC-03 |
| G01-PHONE-VALIDATION-Q030 | Company-specific vs shared explicit | REC-03, REC-26 (O-07) |
| G01-PHONE-VALIDATION-Q031 | No enumeration by users without list access | REC-06, REC-24 (O-04) |
| G01-PHONE-VALIDATION-Q032 | Bulk mixed valid/invalid atomicity | REC-02, REC-12 |
| G01-PHONE-VALIDATION-Q033 | Concurrent add converges | REC-29 (GAP-09) |
| G01-PHONE-VALIDATION-Q034 | Concurrent add/remove deterministic | REC-29 (GAP-09) |
| G01-PHONE-VALIDATION-Q035 | Audit distinguishes lifecycle operations | REC-17 (C17), REC-18 (C18), REC-25 (O-05) |
| G01-PHONE-VALIDATION-Q036 | Downstream flows honour blacklist | REC-05 (consumers outside module; reachability only) |
| G01-PHONE-VALIDATION-Q037 | Re-evaluation after country/config change | REC-09, REC-11 |
| G01-PHONE-VALIDATION-Q038 | Same identity across nodes/sessions | REC-22 (O-02) |
| G01-PHONE-VALIDATION-Q040 | Restore/migration preserves identity | REC-16, REC-20 (C20), REC-27 (GAP-01) |

**Mapped: 39 QIDs.** **No evidence yet: 1 QID**, Q039 (transient failure outcome knowable before retry). No mapping answers a QID.

## 4. PDPA-relevance notes (HIGH / flagged items; design implication only, neutral)

Reference frame: Thailand Personal Data Protection Act B.E. 2562 themes. These notes state design implications for SMEsPlus. They are not legal conclusions and do not evaluate the reference ERP's compliance.

| Item | A2 severity | PDPA theme | Design implication (neutral) |
|---|---|---|---|
| O-PHON-01 / PR-PHON-01 (wrong-subject suppression via empty-value fallback) | HIGH | Data accuracy (s.35); honouring objection / consent withdrawal (s.32, s.19) | A suppression or objection register must bind only to the identity explicitly submitted for the intended data subject. Unvalidatable input is rejected, never substituted with another identity. The audit entry records the submitted input and the resolved identity. |
| O-PHON-02 (canonical form depends on acting user's country) | MED | Data accuracy (s.35) | Canonicalization of a data-subject identifier should be deterministic and independent of which operator enters it, with an explicit country input where the number is not internationally qualified. |
| O-PHON-04 (internal-user bulk search of suppressed records) | MED | Security / need-to-know (s.37) | Suppression status reveals that a person objected. Visibility and bulk filtering of that status should follow least-privilege rules defined for the register, not general internal-user membership. |
| O-PHON-03 / C07 (unblock apply not elevated; narrows X1) | MED | Authority over withdrawal of objection; records of processing (s.39) | Every path that lifts a suppression should enforce the same authorization, at the service layer, not only at an entry point, and produce an attributable event. |

## 5. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_PHONE_VALIDATION_PROOF_20260927.md`.
- Proof must address the 13 UNKNOWN_PENDING_PROOF items and the 3 CONTRADICTION items. The 3 GAP items are not closable by Proof in this scope and are carried forward.

## 6. Limitations

- REC used only the immutable inputs in 0.1 and, for classification support, the static proof results from Stage 2. No runtime evidence exists.
- QID mapping is topical lineage judged by this controller. It is not a coverage measure. No Formal Coverage claim. No percentages.
- Downstream consumers (SMS, marketing, portal controller) were not read; reachability statements are bounded.
