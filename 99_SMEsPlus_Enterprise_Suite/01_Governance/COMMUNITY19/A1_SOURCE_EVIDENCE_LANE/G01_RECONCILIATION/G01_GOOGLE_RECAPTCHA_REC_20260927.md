# G01 PLATFORM_BASE — Module `google_recaptcha` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `google_recaptcha` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/google_recaptcha/` plus core cross-references) |
| Frozen bank (lineage lens only) | W1-B04 `G01_GOOGLE_RECAPTCHA_GMVQ_MVQ_40_V1.00_DRAFT.md`, 42 QIDs (G01-GOOGLE_RECAPTCHA-Q001..Q042) |
| Lane B | None exists (search recorded in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_GOOGLE_RECAPTCHA_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (30 REC items; 1 CONTRADICTION and 8 UNKNOWN_PENDING_PROOF carried to Proof) |

Format reference: `G01_RECONCILIATION/` did not exist at intake (about 15:02Z). `G01_BUS_REC_20260927.md` appeared at about 15:04Z, while this stage was running, and this document follows its section structure.

## 2. Intake (immutable inputs, sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_GOOGLE_RECAPTCHA_LANE_A_PASS1_20260927.md` | `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479` | Equals the value in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_PACKAGE_20260927.md` | `122308a976f8c966682372697463653f9218ccc6977399257f1430bc39d0b270` | Equals the value in the A2 header. 19 claims (C01–C19) |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_GOOGLE_RECAPTCHA_A2_REVIEW_20260927.md` | `961a5d749a296601186b3eb933a5d987f0bbd00265c9670a0969ba39d574ec4b` | A2 PASS WITH FINDINGS: 17 VERIFIED, 2 PARTIAL; SF-1..SF-6; OM-1..OM-6; 12 proof requirements (PR-RCAP-01..12) |
| Frozen bank | `GMVQ/G01_PLATFORM_BASE/G01_GOOGLE_RECAPTCHA_GMVQ_MVQ_40_V1.00_DRAFT.md` | `471e0323450c71223ac795ee859f004d1f5f8e0c8baac04a398b51f7c3bd7724` | Equals the `FREEZE_W1-B04.json` bank_files entry |
| Freeze hash | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B04.json` (file sha256 `27db90332c140e569d4ab7f3a6d2fe7f5d0aae5f375065b5ab2ffe2d95f4d4f9`) | `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377` | Recomputed with the `freeze_batch.py` formula: MATCH. All 4 bank files were re-hashed: MATCH |

Inputs were read only. None was edited, and no git operations were run.

## 3. Lane B evidence-pool search (recorded)

- One search was run for both modules on 2026-09-27T15:02:28Z. Scratch log: `laneb_search.txt`, sha256 `e5b891c5ea8e32c876d11ac484a0c5ae6a69db5871e836b2f76d826cf127b135`.
- Path search (`*lane_b*`, `*laneb*`, `*LANE-B*`, `*evidence_pool*`, case-insensitive) over the whole repository: 0 hits.
- Content search for files that mention the module AND "Lane B": the only hits are Lane A, A1, A2, GMVQ and checkpoint documents, and each of them states that Lane B was not viewed or not started. None of them is a runtime observation record.
- The runtime device is OFFLINE since 2026-09-24T12:53Z, as recorded in `MASTER_CONTROLLED_HANDOFF_STATE_20260927.md`.
- **Result: no Lane B runtime evidence exists for `google_recaptcha`.** The Lane B column is marked UNCORROBORATED or NOT_APPLICABLE. It is never marked FAIL because evidence is absent.

## 4. Classification rules applied

| Class | Rule |
|---|---|
| MATCH | A2 VERIFIED the A1 claim, and no A2 runtime proof requirement is needed to hold it |
| GAP | A2 PARTIAL on scope, an A2 extension or refinement that A1 did not state, or an A2 omission promoted to a new REC item |
| CONTRADICTION | A2, citing source, directly contradicts an A1 statement |
| UNKNOWN_PENDING_PROOF | A2 VERIFIED the source fact, but the conclusion is behavioural or security-related and A2 requires runtime proof |

## 5. Reconciliation table

C01–C19 are the A1 claims `A1-G01-RCAP-Cnn`. SF and OM items are A2 findings promoted to REC items. The QID mapping records lineage only, by topical fit. **No QID is answered.** `rcap+Qnnn` means `G01-GOOGLE_RECAPTCHA-Qnnn`.

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+QID lineage |
|---|---|---|---|---|---|---|---|
| REC-RCAP-01 | C01 | Hidden v3 integration. Depends on base_setup. No routes, models or tests | VERIFIED (controllers and tests 404) | MATCH | NOT_APPLICABLE | PC-RCAP-01 | — (no clear fit) |
| REC-RCAP-02 | C02 (+BR1) | Checked **only** when the route declares a captcha action and the method is not safe. The surface is opt-in | PARTIAL. The mechanism is verified (safe set GET/HEAD/OPTIONS/TRACE). "Only" is not established, because the verify method can be called directly by other code and other dispatchers were not examined | GAP | NOT_APPLICABLE | PC-RCAP-02 / PC-RCAP-22 (PR-RCAP-05) | rcap+Q001, rcap+Q024, rcap+Q025 |
| REC-RCAP-03 | C03 | Verification runs before the endpoint, so a refusal comes before business side effects | VERIFIED | MATCH | NOT_APPLICABLE | PC-RCAP-02 | rcap+Q038 |
| REC-RCAP-04 | C04 | The flag defaults to on when absent. When off, verification is skipped | VERIFIED | MATCH | UNCORROBORATED | PC-RCAP-03 | rcap+Q012, rcap+Q013 |
| REC-RCAP-05 | C05 + SF-5 | The token is removed before verification, so it **never** reaches the endpoint | PARTIAL. **Contradicted for the disabled posture**: removal happens only after the enabled check, so when the flag is off the token passes through to the endpoint as an ordinary parameter | CONTRADICTION | NOT_APPLICABLE | PC-RCAP-03 / PC-RCAP-24 (PR-RCAP-07) | rcap+Q019, rcap+Q035 |
| REC-RCAP-06 | C06 (+BR2) | No secret → "no secret" → pass (FAIL-OPEN), silently, with no log | VERIFIED | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-RCAP-04 / PC-RCAP-18 (PR-RCAP-01) | rcap+Q002, rcap+Q014 |
| REC-RCAP-07 | SF-2 (A2 new) | Both paths were recorded but the asymmetry was not stated | **Missing vs wrong secret asymmetry**: a missing secret fails open silently, while an invalid secret fails closed for every public visitor with a "private key is invalid" message that discloses the configuration fault to anonymous users | GAP | UNCORROBORATED | PC-RCAP-04, PC-RCAP-08 | rcap+Q014, rcap+Q015, rcap+Q031 |
| REC-RCAP-08 | C07 (+BR3) | With a secret set, timeout → retryable refusal and any other failure → malformed refusal. FAIL-CLOSED, 2 s timeout, no retry | VERIFIED. The HTTP status is not checked separately | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-RCAP-05 / PC-RCAP-20 (PR-RCAP-03) | rcap+Q006, rcap+Q007, rcap+Q028 |
| REC-RCAP-09 | C08 / CON-RCAP-01 | The min-score conversion sits outside the guard and has no seeded default. Never saved or non-numeric → unhandled technical error | VERIFIED (source path). Reachability refined (see REC-RCAP-10): saving through the settings screen normally persists 0.7, so "never saved" narrows to non-screen writes | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-RCAP-06 / PC-RCAP-19 (PR-RCAP-02) | rcap+Q008, rcap+Q009, rcap+Q032 |
| REC-RCAP-10 | SF-1 (A2 new) | — (not addressed) | **Score 0.0 deletes the setting → error on success**: the core settings save turns 0.0 into false, and false deletes the parameter. Every *successful* verification then raises the technical error, so real users hit an outage while bots still get a defined refusal | GAP | UNCORROBORATED | PC-RCAP-06 / PC-RCAP-19 (PR-RCAP-02 b) | rcap+Q009, rcap+Q032 |
| REC-RCAP-11 | C09 (+BR4) | A success reply with no score counts as falsy, is below any positive threshold, and is classed as a bot | VERIFIED. A zero threshold cannot persist (SF-1) | MATCH | UNCORROBORATED | PC-RCAP-07 | rcap+Q008 |
| REC-RCAP-12 | C10 (+BR5) | Binding refuses only a non-empty returned action that differs. An empty action skips the check | VERIFIED. A missing action key goes to malformed. The expected action comes from the server-side route | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-RCAP-07 / PC-RCAP-23 (PR-RCAP-06) | rcap+Q004, rcap+Q021, rcap+Q036 |
| REC-RCAP-13 | C11 | Verifier error-code mapping. Secret and token errors are validation errors; the rest are user errors, with a generic "suspicious" fallback | VERIFIED. The first recognised code wins | MATCH | NOT_APPLICABLE | PC-RCAP-08 | rcap+Q015, rcap+Q031, rcap+Q042 |
| REC-RCAP-14 | C12 | A missing token is still sent to the verifier. Replay protection depends only on the verifier | VERIFIED (nuance: how the HTTP client encodes a false token was not re-read) | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-RCAP-29 (PR-RCAP-12) | rcap+Q002, rcap+Q005 |
| REC-RCAP-15 | C13 + CON-RCAP-03 | The raw token and IP are logged at warning on failure, the IP is logged on other paths, and the wrong-action log prints the score in the action slot | VERIFIED. The generic-exception path logs no IP and no detail | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-RCAP-09 / PC-RCAP-21 (PR-RCAP-04) | rcap+Q019, rcap+Q020, rcap+Q039 |
| REC-RCAP-16 | C14 | Uses the raw remote address. Proxy behaviour depends on the core | VERIFIED | UNKNOWN_PENDING_PROOF | NOT_APPLICABLE | PC-RCAP-10 / PC-RCAP-27 (PR-RCAP-10) | rcap+Q022 |
| REC-RCAP-17 | C15 (+BR6) + OM-3 | 4 plain config parameters, system-admin only. The secret is read with sudo, with no encryption or masking | VERIFIED. The parameter-model ACL is system-only. Other elevated readers were not enumerated (GAP-5 narrowed) | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PC-RCAP-11 / PC-RCAP-28 (PR-RCAP-11) | rcap+Q010, rcap+Q012 |
| REC-RCAP-18 | C16 | No score-range or key-format validation, only help text | VERIFIED | MATCH | NOT_APPLICABLE | PC-RCAP-11 | rcap+Q032 |
| REC-RCAP-19 | C17 | Only the site key goes into session info, and only when enabled and present. The secret never does | VERIFIED | MATCH | NOT_APPLICABLE | PC-RCAP-12 | rcap+Q011 |
| REC-RCAP-20 | C18 | The client library loads only when a site key is present. An error message is returned for an invalid site key | VERIFIED (nuance: the key is URL-encoded, and *any* client execution failure is reported as an invalid site key) | MATCH | UNCORROBORATED | PC-RCAP-16 | rcap+Q016, rcap+Q026, rcap+Q034 |
| REC-RCAP-21 | C19 | Installed through the core general-settings toggle, extending the host block | VERIFIED | MATCH | NOT_APPLICABLE | PC-RCAP-01 | — (no clear fit) |
| REC-RCAP-22 | CON-RCAP-02 | With the flag on, a site key and no secret, the client mints tokens but the server passes everything. Appearance and enforcement diverge | Upheld by A2 | MATCH | UNCORROBORATED | PC-RCAP-04, PC-RCAP-12 / PC-RCAP-18 | rcap+Q013, rcap+Q014 |
| REC-RCAP-23 | SF-3 (A2 new) | Not covered by postures P0–P3 | **Secret without a site key**: the client gets no token and the server posts a missing token. The expected result is a token-invalid refusal for every visitor on every protected form | GAP | UNCORROBORATED | PC-RCAP-12, PC-RCAP-16 / PC-RCAP-25 (PR-RCAP-08) | rcap+Q013, rcap+Q016 |
| REC-RCAP-24 | SF-4 (A2 new) | — (not addressed) | **Malformed enable flag**: a strict boolean parse with no fallback raises on unrecognised text. It also runs when session info is built, which affects page loads. This needs a write outside the settings screen | GAP | NOT_APPLICABLE | PC-RCAP-13 / PC-RCAP-26 (PR-RCAP-09) | rcap+Q012, rcap+Q032 |
| REC-RCAP-25 | OM-1 (A2 new) | — (not addressed) | **No hostname or timestamp check**: only success, score, action and error codes are read. A token from another site that shares the key pair is not distinguished locally. Freshness is left to the verifier | GAP | NOT_APPLICABLE | PC-RCAP-14 | rcap+Q003, rcap+Q005 |
| REC-RCAP-26 | OM-2 (A2 new) | — (not addressed) | **Database-wide, not per-company, settings**: the parameter model has no company field, so there is one key pair and one threshold for every company and site in a database | GAP | NOT_APPLICABLE | PC-RCAP-15 | rcap+Q023, rcap+Q041 |
| REC-RCAP-27 | OM-4 (A2 new) | — (not addressed) | Third-party transfer of the client IP and token and a vendor script load, with no consent or disclosure claim. A legal-notice template exists | GAP | NOT_APPLICABLE | — (no proof case; outside source scope) | — (no clear fit) |
| REC-RCAP-28 | OM-5 (A2 new) | C13 covers what *is* logged | Outage observability: the generic-exception path cannot tell DNS, TLS, HTTP-status and JSON failures apart | GAP | NOT_APPLICABLE | PC-RCAP-05, PC-RCAP-09 | rcap+Q031, rcap+Q039 |
| REC-RCAP-29 | OM-6 (A2 new) | Positive controls not stated | The expected action and the threshold are server-side, so the client cannot lower them. The site key is URL-encoded into the script URL | GAP | NOT_APPLICABLE | PC-RCAP-06, PC-RCAP-07, PC-RCAP-16 | rcap+Q008, rcap+Q021, rcap+Q034 |
| REC-RCAP-30 | SF-6 (A2 business meaning) | Posture analysis found sound | Consumer example: a public POST form route declares captcha and disables CSRF, so captcha is its main anti-automation control. In that case fail-open (REC-RCAP-06) leaves it unprotected with no operator signal | GAP | NOT_APPLICABLE | PC-RCAP-17 | rcap+Q001, rcap+Q025 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 10 | REC-RCAP-01, 03, 04, 11, 13, 18, 19, 20, 21, 22 |
| GAP | 11 | REC-RCAP-02, 07, 10, 23, 24, 25, 26, 27, 28, 29, 30 |
| CONTRADICTION | 1 | REC-RCAP-05 |
| UNKNOWN_PENDING_PROOF | 8 | REC-RCAP-06, 08, 09, 12, 14, 15, 16, 17 |
| **Total** | **30** | 19 A1 claims + CON-RCAP-02 + 10 A2 findings/omissions promoted (SF-1, SF-2, SF-3, SF-4, SF-6, OM-1, OM-2, OM-4, OM-5, OM-6). SF-5 and OM-3 are merged into parent rows |

Lane B column: 11 UNCORROBORATED (REC-RCAP-04, 06, 07, 08, 10, 11, 12, 17, 20, 22, 23). These include every claim A2 listed: C04, C06, C07, C09, C10, C15, C18. There are 19 NOT_APPLICABLE and 0 FAIL.

## 6. MODULE+QID lineage summary (frozen bank W1-B04, 42 QIDs)

Lineage only. Mapped QIDs are **not answered** and carry no coverage meaning.

- **Mapped (34):** Q001, Q002, Q003, Q004, Q005, Q006, Q007, Q008, Q009, Q010, Q011, Q012, Q013, Q014, Q015, Q016, Q019, Q020, Q021, Q022, Q023, Q024, Q025, Q026, Q028, Q031, Q032, Q034, Q035, Q036, Q038, Q039, Q041, Q042.
- **No evidence yet (8):** Q017 (double-submit race during challenge load), Q018 (retry duplicating the business action), Q027 (accessibility/keyboard recovery), Q029 (early rejection under bot load), Q030 (verification not substituting for auth/authorization), Q033 (key rotation policy), Q037 (back/forward cache reuse of stale token), Q040 (non-production testing without production secrets).
- REC items with no clear QID fit: REC-RCAP-01, 21, 27.

## 7. Carried forward

- A1 gaps GAP-1..GAP-6 remain open. GAP-5 is narrowed by OM-3 (the parameter ACL is system-only). GAP-1 (the protected-route inventory) is not closed: A2-X9 is only one example.
- CRQ-RCAP-01..07 are carried unchanged. They map to PR-RCAP-01, 02, 03, 04, 05, 11 and 06.
- CONTRADICTION REC-RCAP-05 must not be resolved in favour of A1's "never reaches the endpoint" unless source shows the token being stripped in the disabled posture. PC-RCAP-03 tests this.
- CON-RCAP-01 (a source-path defect) is upheld by A1 and A2 and carried as REC-RCAP-09/10. CON-RCAP-03 (cosmetic log label) is carried in REC-RCAP-15.

## 8. Handoff to PROOF

All 12 A2 proof requirements (PR-RCAP-01..12) go to Proof. Items with a runtime case: REC-RCAP-02, 05, 06, 08, 09, 10, 12, 14, 15, 16, 17, 22, 23, 24. Items with a static check only: REC-RCAP-01, 03, 04, 07, 11, 13, 18, 19, 20, 21, 25, 26, 28, 29, 30. REC-RCAP-27 has no proof case.

## 9. Limitations

- REC reconciles documents. Re-reading source is Proof Stage 2.
- No Lane B evidence exists, so nothing here is runtime-corroborated. The verifier's own behaviour is outside the source scope.
- No Formal Coverage claim, no percentages and no QID answered. The bank was not edited.
- Clean room: neutral WHAT/WHY/RISK summaries only. Identifiers are evidence pointers, and no code is reproduced.
- Scratch: `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/rec_sprs_rcap`.
