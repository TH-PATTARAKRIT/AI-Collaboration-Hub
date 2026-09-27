# G01 PLATFORM_BASE — `google_recaptcha` — RED TEAM A1 ADDENDUM R1 (remediation of A3-RCAP-D1)

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **RED TEAM A1** (addendum only; the original A1 package is NOT edited) |
| Group / Module | G01 PLATFORM_BASE / `google_recaptcha` |
| Parent (superseded in part) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_PACKAGE_20260927.md` sha256 `122308a976f8c966682372697463653f9218ccc6977399257f1430bc39d0b270` (equals A3 intake) |
| Upstream Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_GOOGLE_RECAPTCHA_LANE_A_PASS1_20260927.md` sha256 `a7710f32db0332615bf8debc478b8c30e3c98ec2755e4bb473cc9e9a2d770479` (not edited; erratum for item 12 is recorded in the PROOF addendum §7) |
| A3 reports | `G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md` sha256 `ff91606234f5b276cc659538b0fa852ac119308c70dbead5c9479de48c63273b`; `G01_A3_CHALLENGES/G01_BASE_SPARSE_FIELD_A3_STATIC_20260927.md` sha256 `2ec7cb8a285e02fe61f2bca1de24fdb52d39ebe6964d0655107be967c5f981cb` |
| Challenge IDs addressed | A3-RCAP-D1 (HIGH, owner A1: C08 / CRQ-RCAP-02); A3-RCAP-D3 scope input (C09). No A1 action was routed for `base_sparse_field` (A3-SPRS-D1/D2 are REC/A2/Proof) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` |
| Date | 2026-09-27 |
| Status | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean room: neutral WHAT/WHY/RISK statements; identifiers and line numbers are evidence pointers only; no vendor code is reproduced. No QID answered, no percentages, no Formal Coverage claim. No git operations.

## 2. Independent re-derivation (STEP 1 — performed before accepting A3)

Source re-fetched into `scratchpad/remed_rcap/src/` (HTTP 200 each); `git hash-object` equals the recorded blob for every file (log `blob_remed.txt`, sha256 `ad205536b83bef00934e36b9864e358c3336722732501500fc79edb68f1a7f5c`):
E4 `addons/google_recaptcha/models/ir_http.py` 78d5a71c; E5 `addons/google_recaptcha/models/res_config_settings.py` c2f237bb; E1 `__manifest__.py` 0dcee164; A2-X6 `odoo/addons/base/models/ir_config_parameter.py` 21c82bf6; A2-X5 `odoo/addons/base/models/res_config.py` 50464416.

Trace (pointers only):
1. The min-score parameter is read with **no default argument** (E4 L83), before the guarded outbound block (L84–98).
2. The core parameter getter returns the stored value **or the caller's default, which is false when none is given** (A2-X6 L60, L69). The raw lookup yields an empty result for an absent key (L77–79), so the getter returns **false**, not an empty/none value.
3. On the success branch (E4 L100) the missing score is taken as false (L101) and compared against the numeric conversion of the threshold (L102), outside any guard.
4. Evaluating the language's float conversion locally (`exec_builtin_R1.txt`, sha256 `381b2d5b…8011518`, Python 3.11.15): false converts to **0.0 without raising**; unrecognised text (e.g. "abc") raises; "0" gives 0.0; "nan" converts without raising.
5. With a 0.0 threshold, "score below threshold" is false for a missing score and for every score at or above zero, so every successful verification proceeds to the action check and then to the human outcome (E4 L102–109).
6. Settings load: for an absent parameter the settings screen passes the field default (0.7, E5 L17) as the getter default and shows it (A2-X5 L268, L284–289).
7. Settings save: a zero float is turned into false (A2-X5 L342); saving false deletes an existing parameter (A2-X6 L94–98) or, when already absent, is skipped (A2-X5 L347).
8. Settings save iterates **every** config-parameter field on each save and writes whenever the stored value differs from the form value (A2-X5 L332–349). From the absent state, the form value is the displayed default 0.7, which differs from the absent (false) stored value.
9. The manifest seeds no parameter (E1 data list: one view file only).

**A1 independent conclusion: AGREE with A3-RCAP-D1.** The original C08 statement "never saved → unhandled technical error" is **wrong on source**. The absent state gives an effective threshold of 0.0 with no error (score gate silently off). Only a stored value that the float conversion rejects raises the unhandled error. No A3 item is DISPUTED. Two refinements are added (C08R1-b, C08R1-c) that A3 did not state.

## 3. Supersede map

| Original (A1 package) | Status | Replaced by |
|---|---|---|
| A1-G01-RCAP-C08 | **WITHDRAWN — CONTRADICTED-FROM-SOURCE** (the "never saved → technical error" branch) | C08R1-a, C08R1-b, C08R1-c |
| A1-G01-RCAP-C09 | **SCOPE-CORRECTED** | C09R1 |
| BR4 | Scope-corrected | BR4R1 |
| §3 posture P2 | Withdrawn | P2R1-a, P2R1-b |
| §4 failure mode F5 | Withdrawn | F5R1 |
| CON-RCAP-01 ("one path leaves the defined categories" via absent parameter) | Withdrawn as stated | CON-RCAP-01R1 |
| CRQ-RCAP-02 | Replaced | CRQ-RCAP-02R1, CRQ-RCAP-08 |
| §9 spot-check row S3 wording "score conversion outside the guard" | Fact still true; its consequence is corrected by C08R1-a | — |
| All other claims (C01–C07, C10–C19) | Unchanged | — |

## 4. Corrected claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-RCAP-C08R1-a | WHAT: When the min-score parameter is absent (never saved, deleted, or removed by saving 0.0), the verification reads false, which converts to an effective threshold of 0.0 **with no error**. Every successful verification then passes the score check, whatever its score, including a success reply with no score. RISK: the score gate is silently **off**, while the settings screen displays 0.7 (display/enforcement divergence). Fail-open on score, not an outage. | E4 L83, L100–109; A2-X6 L60–79; A2-X5 L268, L341–349; A2-X6 L94–98; E1 data list; `exec_builtin_R1.txt` | HIGH (source + language built-in) | SOURCE-STATIC (runtime end-to-end pending) |
| A1-G01-RCAP-C08R1-b | WHAT: From the absent state, any later save of the settings screen (for any setting) persists the displayed default 0.7, because the save writes every config-parameter field whose form value differs from the stored value. RISK: the effective threshold silently flips 0.0 → 0.7 on an unrelated save. An admin who chose 0.0 does not keep it, and the change is not tied to an explicit min-score edit. | A2-X5 L304, L332–349; E5 L17 | MED (web-client transmission of unchanged defaults not read; the default path also yields 0.7) | SOURCE-STATIC |
| A1-G01-RCAP-C08R1-c | WHAT: The conversion sits outside the guarded block, so a stored value the float conversion rejects (e.g. arbitrary text, only reachable by a non-screen write) raises an unhandled technical error on the success branch only. A stored value that converts but is not a meaningful score is accepted silently: "nan" disables the gate (no comparison is true), and a value above the verifier's scale refuses every successful verification (no range validation, C16). | E4 L84–102; E5 L13–19; `exec_builtin_R1.txt` | HIGH (conversion); MED (verifier score scale per help text only) | SOURCE-STATIC |
| A1-G01-RCAP-C09R1 | WHAT: A success reply with no score is taken as false. It is classed as a bot **only when the effective threshold is positive** (a stored positive value). When the parameter is absent (effective threshold 0.0), a success reply with no score passes as human. | E4 L101–109; C08R1-a | HIGH | SOURCE-STATIC |

Corrected rule, postures and failure modes:
- BR4R1: A score below a **stored positive** minimum, or a missing score under a stored positive minimum, is refused. With no stored minimum, no score is refused (C08R1-a, C09R1).
- P2R1-a: Enabled, secret set, min score absent → verifier-dependent outcome only; score gate off; screen shows 0.7 (C08R1-a).
- P2R1-b: Enabled, secret set, min score stored as unconvertible text → unhandled technical error after a successful verification; defined refusals on verifier failure (C08R1-c).
- F5R1: Min score non-convertible → unhandled technical error (success branch only). Min score absent → no error, gate off.
- CON-RCAP-01R1 (CONFIRMED-FROM-SOURCE, runtime pending): the settings screen presents a 0.7 minimum while the enforced minimum is 0.0 whenever the parameter is absent; the only path outside the defined categories is a non-convertible stored value.

CRQ updates:
- CRQ-RCAP-02R1: With a secret configured and the min-score parameter absent (deleted, and separately after saving 0.0), confirm that a successful low-score verification and a success reply with no score are accepted, and that the screen shows 0.7. With unconvertible text stored, confirm the technical error.
- CRQ-RCAP-08 (new): From the absent state, save an unrelated setting and confirm the parameter becomes 0.7 and low scores are refused.

## 5. Confidence and limits

- The absent → false → 0.0 chain is HIGH: it rests on read source plus a local evaluation of the language's built-in conversion. The end-to-end request outcome is runtime-pending (PROOF addendum PC-RCAP-31/32).
- Core field-default wrapping and the web client's save payload were not read; C08R1-b is capped at MED.
- Verifier behaviour (score scale, presence of a score) is outside source scope.
- No other A1 claim is changed by this addendum.
