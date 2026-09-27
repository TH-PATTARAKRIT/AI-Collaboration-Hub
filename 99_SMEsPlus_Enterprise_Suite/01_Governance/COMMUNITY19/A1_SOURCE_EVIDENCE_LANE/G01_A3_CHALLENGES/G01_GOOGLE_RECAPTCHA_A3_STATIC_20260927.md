# G01 PLATFORM_BASE — Module `google_recaptcha` — RED TEAM A3 Independent Challenge (STATIC)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3 — independent adversarial challenger |
| Independence | This reviewer did not author Lane A, A1, A2, REC or Proof for this module. Source was fetched again separately and blob-verified. The Proof scratch copies were not reused |
| Scope | STATIC only. RUNTIME cases (PC-RCAP-18..29) are NOT-EXECUTED: neither passed nor failed |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Frozen bank | W1-B04 `G01_GOOGLE_RECAPTCHA_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `471e0323…d7724`. This equals the `FREEZE_W1-B04.json` `bank_files` entry. The freeze file sha256 is `27db9033…d4f9`, which equals the value in the REC intake |
| Intake manifest | `scratchpad/a3_sprs_rcap/intake.sha256` (sha256 `f4c577d93e63d45f6831e7dffc900562c3f61fe995661e1909956d672d85def7`) |
| Intake hashes (this module) | Lane A `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479`; A1 `122308a976f8c966682372697463653f9218ccc6977399257f1430bc39d0b270`; A2 `961a5d749a296601186b3eb933a5d987f0bbd00265c9670a0969ba39d574ec4b`; REC `fc976cb455216cc44d053416c151b37cbc441239f003ce986a7d1bcd74b0afbf`; Proof `273400741878d2aa944d7bec9c87f132d97831bda52f82e56b6ddcc069ee194b` |
| Exit hashes | All inputs were hashed again at exit and are identical (`exit_inputs.sha256`), so no input changed. A3 blob log `blob_a3.txt` sha256 `f88117f6d4a111f3928d1fd932032a986f7a7720ea8529d1fa1ecd64527925c1` |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (route to A1 [C08/CON-RCAP-01], A2 [SF-1, posture matrix], REC [REC-RCAP-09/10/11], Proof [PC-RCAP-06 predicate, PC-RCAP-19 expected])**. One HIGH-severity sustained challenge: the "missing or 0.0 min-score → technical error on success" conclusion is disproved on source. The other conclusions hold. MASTER must not consume REC-RCAP-09, 10 or 11 as they stand |

## 2. Challenge log

### Challenge 1 — Re-derive REC items from source and try to refute them

The following were fetched again (HTTP 200) and `git hash-object` equals the recorded blob for each: E1 0dcee164, E4 `models/ir_http.py` 78d5a71c, E5 `models/res_config_settings.py` c2f237bb, E7 `recaptcha.js` 2cbbf952, X1 core `ir_http.py` d9d2a00b, A2-X5 `res_config.py` 50464416, A2-X6 `ir_config_parameter.py` 21c82bf6, A2-X7 `tools/misc.py` 6d275059.

| REC item | Refutation attempt | A3 finding | Disposition |
|---|---|---|---|
| REC-RCAP-05 (C05; the token passes through when disabled; CONTRADICTION) | Looked for token removal before the flag check | The flag is read (E4 L44) and the hook returns when it is off (L45–46). The token is removed only afterwards (L48). When disabled, the token stays in the request parameters. Nuance: in that posture the client gets no site key (L32), so the token is present only if a client or attacker sends one | UPHELD |
| REC-RCAP-06 (C06, fail-open with no secret) | Looked for a log line or refusal | An absent secret returns "no secret" before any call or log (L80–82). The hook accepts it silently (L50–51) | UPHELD |
| REC-RCAP-08 (C07, fail-closed) | Looked for a retry, or an exception treated as a pass | There is one POST with a 2 s timeout (L85–89). A timeout maps to "timeout" and any other exception (non-JSON body, missing `success` key) maps to "bad request" (L93–98). Both are refused (L56–59). The HTTP status is not checked | UPHELD |
| **REC-RCAP-09 (C08 / CON-RCAP-01) and REC-RCAP-10 (SF-1: a 0.0 score deletes the setting, then an error on success)** | Traced what the conversion actually receives when the parameter is absent | The min score is read with no default (L83). The core `get_param` then returns **false** when the key is absent (`ir_config_parameter.py` L60–69, L73–79). The success path converts that value to a number (L102). Converting false gives **0.0 and does not raise** (confirmed by evaluating the language built-in). So when the parameter is absent, whether never saved or deleted by a 0.0 save (`res_config.py` L341–349 → `set_param` L94–98), there is **no technical error**. The effective threshold is 0.0, and every successful verification passes whatever its score. Only a stored **non-numeric** value raises. **Real risk (static)**: the score gate is silently disabled, while the settings screen shows the field default 0.7 when the parameter is absent (`res_config.py` L268). What is displayed and what is enforced diverge, which is fail-open on score, not an outage | **CHALLENGE-SUSTAINED** (origin Lane A item 12 "appears liable" → A1 C08/CRQ-RCAP-02 → A2 SF-1 and the posture-matrix row → REC-RCAP-09/10 → Proof PC-RCAP-06/19) |
| REC-RCAP-11 (C09, a missing score is classed as a bot) | Checked it against a zero effective threshold | A missing score becomes false (L101). False < 0.0 is false, so when the parameter is absent a success reply with **no score passes as human**. The claim holds only for a positive stored threshold. "A zero threshold cannot persist" is technically true, but a zero *effective* threshold is the absent-parameter state | CHALLENGE-SUSTAINED (A1 C09 scope; REC note) |
| REC-RCAP-25 (OM-1, no hostname check) | Looked for hostname or timestamp reads | Only `success`, `action`, `score` and `error-codes` are read (L91–92, L101, L110) | UPHELD |
| REC-RCAP-26 (OM-2, database-wide settings) | Looked for company scoping | The parameter model has only key and value and is documented as per-database (`ir_config_parameter.py` L28–37). The settings fields have no company dependency (E5 L10–19) | UPHELD |
| REC-RCAP-12 (C10, empty-action binding) | Read the action extraction | The action is read only when there is success and an expected action (L92). A missing key → bad request. An empty returned action skips binding (L105) | UPHELD |
| REC-RCAP-24 (SF-4, malformed flag) | Read the boolean helper | With no fallback, the helper raises on unrecognised text (`misc.py` L509–515). It is called with no fallback at L30, L44 and E5 L25 | UPHELD |

### Challenge 2 — Re-execute static PASS cases

| PC | A3 re-execution | A3 result | Weakness |
|---|---|---|---|
| PC-RCAP-03 | E4 L44–48 | PASS (agrees) | None |
| PC-RCAP-04 | E4 L80–82, L50–51 | PASS (agrees) | None |
| PC-RCAP-06 | E4 L83, L100–102; E1 data list; `res_config.py` L341–349; `ir_config_parameter.py` L82–103 | Each observation is literally true, but the **predicate is insufficient**. The fail condition "conversion guarded or defaulted" missed the implicit false default of `get_param`, and false converts to 0.0 without error. The PASS was used to "confirm CON-RCAP-01 and SF-1 on source" (Proof §4, §5), and that confirmation is **not supported** | **CHALLENGE-SUSTAINED (Proof)** |
| PC-RCAP-09 | Log lines L94, L97, L103, L106, L108, L111 | PASS (agrees). The raw token is logged at L111. The wrong-action line puts the score in the action slot (L106) | None |
| PC-RCAP-13 | E4 L30, L44; `misc.py` L493–516 | PASS (agrees) | None |
| PC-RCAP-14 | E4 L90–111 | PASS (agrees) | None |

Runtime cases, weak or wrong conditions:
- **PC-RCAP-19**: the expected result "unhandled server error in both cases" is contradicted by source for case (a) (deleted) and case (b) (0.0 saved). If the case runs as predeclared, it is expected to record FAIL, because the request passes. That FAIL must be preserved, and the case must not be re-declared after execution. A3 recommends that Proof add a new, separately predeclared case: the absent parameter gives an effective threshold of 0.0, a low-score success passes, and the settings screen shows 0.7. A non-numeric stored value gives a technical error.
- **PC-RCAP-27**: the expected result "raw peer address unless the core rewrites it" is close to unfalsifiable, because a core proxy rewrite based on headers would satisfy both expected and fail. It needs a split predicate for proxy mode on and off.

### Challenge 3 — Predeclaration integrity

The file `PROOF_CASES_PREDECLARED.md` (sha256 `59a6e0d0…dcbc`, matches) has mtime 15:03:45.39Z. The first source copy is dated 15:04:02Z and the blob log 15:04:07Z, so the ordering holds. The cases were written after reading A1/A2. That is acceptable in principle, because predeclaration must precede execution and not the reading of the claims. **This module shows the residual risk**: PC-RCAP-06 copied the A1/A2 mechanism into its expected condition and did not include a disconfirming branch (the value the conversion actually receives). The ordering is UPHELD. Case independence: **CHALLENGE-SUSTAINED (Proof)**, as a case-design weakness rather than tampering.

### Challenge 4 — Lineage

- REC: one commit, `69d312f` at 15:09:02Z, "in-flight REC/Proof/A3 artifacts checkpoint" (a MASTER on-disk checkpoint).
- Proof: one commit, `811e8ae` at 15:12:19Z, "REC/Proof G01: base_sparse_field, google_recaptcha".
- The working tree is clean, and the current sha256 equals the intake. There is no content change by anyone other than the author. **UPHELD.**

### Challenge 5 — Overclaim, Lane B, QID mapping, bank hash, clean room

- **Overclaim:** Proof §5 states "CON-RCAP-01 and A2 SF-1 are both confirmed on source". That overclaims (see Challenge 1). There is no Formal Coverage claim and there are no percentages. **CHALLENGE-SUSTAINED (Proof).**
- **Lane B:** none exists. The Lane B column uses UNCORROBORATED or NOT_APPLICABLE only, with no FAIL and no misuse. **UPHELD.**
- **Bank hash:** equals the freeze entry. **UPHELD.**
- **Clean room:** the code-construct scan of REC and Proof found nothing reproduced. User-facing message texts are paraphrased or quoted briefly as evidence. **UPHELD.**
- **QID sample:**
  - Q009 (a min-score change takes effect predictably and is auditable) → REC-RCAP-09/10. The fit is good, but the behaviour mapped is the disproved one. The re-derived display/enforcement divergence is the relevant evidence.
  - Q023 (scope isolation) → REC-RCAP-26. Good fit.
  - Q035 (the token cannot be replaced by attacker data that bypasses validation) → REC-RCAP-05. Acceptable fit.
- **"No evidence" check:**
  - Q030 (verification never substitutes for auth): REC-RCAP-03 shows the hook only raises or returns before the endpoint, with no elevation. That is partial static evidence, so the classification is arguable. Minor note.
  - Q033 (key rotation): REC-RCAP-17/26 show one plain key pair with no rotation mechanism. That is partial static evidence. Minor note, routed to REC.

## 3. Lineage

| Artifact | sha256 at intake = exit | Git |
|---|---|---|
| Lane A | a7710f32…770479 | — |
| A1 | 122308a9…0b270 | — |
| A2 | 961a5d74…d574ec4b | — |
| REC | fc976cb4…afbf | 69d312f (single) |
| Proof | 27340074…ee194b | 811e8ae (single) |
| Bank | 471e0323…d7724 = FREEZE entry | — |
| Predeclared cases | 59a6e0d0…dcbc (scratch) | not in the repository |

## 4. Defects routed

| ID | Severity | Owner stage | Defect | Required action |
|---|---|---|---|---|
| A3-RCAP-D1 | HIGH | A1 (C08, CRQ-RCAP-02); origin Lane A item 12 | "Never saved → unhandled technical error" is wrong. An absent parameter gives false, which converts to 0.0 without error. Only a non-numeric value raises | Restate C08: an absent parameter gives an effective threshold of 0.0 (score gate off). A non-numeric value gives a technical error |
| A3-RCAP-D2 | HIGH | A2 (SF-1, posture-matrix row "absent, zero-saved or non-numeric") | "A 0.0 save gives an outage for real humans" is wrong. The 0.0 save deletes the parameter and the effective threshold becomes 0.0, which is what the admin chose. However, the screen then shows 0.7 while 0.0 is enforced | Replace it with the display/enforcement divergence finding. Split the matrix row |
| A3-RCAP-D3 | HIGH | REC | REC-RCAP-09/10 carry the disproved conclusion. REC-RCAP-11 ("classed as a bot") does not hold under the zero effective threshold | Re-classify after the A1/A2 correction. Add a no-score-passes note to REC-RCAP-11 |
| A3-RCAP-D4 | HIGH | Proof | The PC-RCAP-06 predicate is insufficient and its PASS was over-read. The PC-RCAP-19 expected result is contradicted by source | Keep PC-RCAP-19 as declared (a FAIL is expected when it runs). Predeclare a new corrected case. Amend the §5 wording |
| A3-RCAP-D5 | Minor | Proof | The PC-RCAP-27 predicate is close to unfalsifiable | Split it by proxy mode |
| A3-RCAP-D6 | Minor | REC | Q030 and Q033 are marked "no evidence" although partial static evidence exists | Review the lineage map |

## 5. Runtime-blocked items

PC-RCAP-18 to PC-RCAP-29 are NOT-EXECUTED because the runtime device is OFFLINE. REC-RCAP-06, 08, 12, 14, 15, 16 and 17 stay UNKNOWN_PENDING_PROOF. REC-RCAP-09/10 must be re-derived before runtime (A3-RCAP-D1..D4). REC-RCAP-27 (third-party transfer) has no case.

## 6. Limitations

- Static only, on one anchor. The core dispatcher variants, the HTTP client's encoding of a false token and the core proxy handling were not read.
- The float(false) → 0.0 behaviour is a language built-in that A3 evaluated locally. The end-to-end request outcome remains runtime-pending.
- QID fit was sampled (5 QIDs). No inputs were edited, and git was used read-only. No Formal Coverage claim, no percentages and no QID answered.
- Clean room: neutral summaries. Identifiers and line numbers are pointers only.
