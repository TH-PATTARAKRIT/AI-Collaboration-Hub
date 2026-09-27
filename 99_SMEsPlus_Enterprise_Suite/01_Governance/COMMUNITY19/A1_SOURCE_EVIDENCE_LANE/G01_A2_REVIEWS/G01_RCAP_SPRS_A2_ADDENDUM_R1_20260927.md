# G01 PLATFORM_BASE — `google_recaptcha` + `base_sparse_field` — RED TEAM A2 ADDENDUM R1 (remediation)

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **RED TEAM A2** (addendum only; the original A2 reviews are NOT edited) |
| Parents (superseded in part) | `G01_A2_REVIEWS/G01_GOOGLE_RECAPTCHA_A2_REVIEW_20260927.md` sha256 `961a5d749a296601186b3eb933a5d987f0bbd00265c9670a0969ba39d574ec4b`; `G01_A2_REVIEWS/G01_BASE_SPARSE_FIELD_A2_REVIEW_20260927.md` sha256 `b50478d63b806e827dfb561cc784bf6d4208dca568e7f37e3060531c640ee42a` (both equal A3 intake) |
| A1 inputs | A1 rcap package sha256 `122308a976f8c966682372697463653f9218ccc6977399257f1430bc39d0b270`; **A1 ADDENDUM R1** `G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_ADDENDUM_R1_20260927.md` sha256 `6926e67b3c97d2c5dbb5fead4dcb75c63a0e25064ef1f86dc3531f06d8381c53`; A1 sparse package sha256 `50c2c610f8df71d3f7cbdd6073c24bd02da746933622962f4f6b91322ebca91d` (unchanged) |
| A3 reports | `G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md` sha256 `ff91606234f5b276cc659538b0fa852ac119308c70dbead5c9479de48c63273b`; `G01_A3_CHALLENGES/G01_BASE_SPARSE_FIELD_A3_STATIC_20260927.md` sha256 `2ec7cb8a285e02fe61f2bca1de24fdb52d39ebe6964d0655107be967c5f981cb` |
| Challenge IDs addressed | A3-RCAP-D2 (HIGH: SF-1, posture-matrix row); A3-RCAP-D3 input (C08/C09 verdicts); A3-SPRS-D2 (minor: SF-1 wording) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`; blobs re-verified (`scratchpad/remed_rcap/blob_remed.txt`, sha256 `ad205536…c7f5c`) |
| Date | 2026-09-27 |
| Status | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Independence note: A2 re-traced the paths on its own re-fetched copies (E4 78d5a71c, E5 c2f237bb, A2-X5 50464416, A2-X6 21c82bf6; sparse `models/models.py` f2196226, `models/fields.py` cb26946e, `views/views.xml` 1c199e72). Clean room: neutral summaries, pointers only, no code. No QID answered, no percentages, no Formal Coverage.

## 2. `google_recaptcha` — corrected verdicts

| Item | Original A2 verdict | A2 R1 verdict | Basis |
|---|---|---|---|
| C08 (original) | VERIFIED (source path) — "absent parameter produces an unhandled type error" | **NOT_VERIFIED — disproved on source** for the absent branch; VERIFIED only for the non-convertible-text branch | The getter returns false for an absent key (A2-X6 L60–79); false converts to 0.0 without raising (`exec_builtin_R1.txt`); comparison at E4 L102 then never refuses. The original A2 "type error" statement was an A2 error, not only an A1 error |
| C08R1-a (A1 addendum) | — | **VERIFIED** | Same trace; screen default A2-X5 L268 |
| C08R1-b (A1 addendum) | — | **VERIFIED (source path), MED** | Save loop over all config fields, write on difference (A2-X5 L332–349) |
| C08R1-c (A1 addendum) | — | **VERIFIED** | Conversion outside guard (E4 L84–102); no range validation (E5 L13–19) |
| C09 (original) | VERIFIED, with "a zero threshold cannot persist" | **PARTIAL (scope)** | A zero *stored* threshold cannot persist, but a zero *effective* threshold is exactly the absent state; there a success reply with no score passes |
| C09R1 (A1 addendum) | — | **VERIFIED** | E4 L101–109 |
| BR4 / BR4R1 | Supported with SF-1 caveat | BR4 PARTIAL; BR4R1 supported | as above |
| CON-RCAP-01 / CON-RCAP-01R1 | Upheld and refined | CON-RCAP-01 **withdrawn as stated**; CON-RCAP-01R1 upheld | display/enforcement divergence |

Revised verdict counts for the rcap review (for consumption): over the original 19 claims VERIFIED 15, PARTIAL 3 (C02, C05, C09), NOT_VERIFIED 1 (C08 original, absent branch); plus the four A1 R1 claims above VERIFIED.

### SF-1R1 (replaces SF-1 in full)

- (a) Unchanged fact: saving through the settings screen from the absent state normally persists 0.7 (A2-X5 L332–349). This now reads as a **re-arm** effect (C08R1-b): any save of the screen, even of an unrelated setting, writes 0.7.
- (b) **Corrected**: choosing 0.0 converts to false and deletes the parameter (A2-X5 L342; A2-X6 L94–98). The result is an effective threshold of 0.0 — which is what the admin chose — and **no error**. The original statement "every successful verification raises the technical error … outage for real humans" is **withdrawn**. The real defect is that the screen then displays 0.7 while 0.0 is enforced, and the next unrelated save silently restores 0.7. The admin can neither see nor keep the 0.0 choice.
- (c) New: the only error branch is a stored value the conversion rejects (non-screen write). A stored "nan" disables the gate silently; an out-of-scale value refuses every successful verification (C16, no range check).
- Business meaning: for a public SaaS form, the observable risk is **silent fail-open on score** in a posture the admin believes is protected at 0.7, and silent threshold changes with no explicit edit — not an availability outage. Auditability of the effective threshold (bank topic Q009) is weak.

### Protection-posture matrix — replacement of the row "on | yes | yes | absent, zero-saved or non-numeric"

| Flag | Site key | Secret | Min score | Client | Server outcome | Defined? |
|---|---|---|---|---|---|---|
| on | yes | yes | **absent** (never saved, deleted, or 0.0 saved) | Tokens minted; screen shows 0.7 | Any verifier success passes (effective 0.0), including a reply with no score; verifier failures give defined refusals | Defined, but **misleading** (display ≠ enforcement) (C08R1-a, SF-1R1) |
| on | yes | yes | stored text the conversion rejects | Tokens minted | Unhandled technical error on verifier success; defined refusals on failure | **No** (C08R1-c) |
| on | yes | yes | stored "nan" or out-of-scale value | Tokens minted | "nan": all successes pass; above scale: all successes refused | Defined but unvalidated (C08R1-c, C16) |

All other matrix rows are unchanged.

### Proof requirement update

- PR-RCAP-02 is **superseded** by PR-RCAP-02R1 (it is not deleted; its runtime case PC-RCAP-19 stays declared as it was).
- **PR-RCAP-02R1**: Secret set. States (a) parameter deleted, (b) 0.0 saved via the screen and absence confirmed, (c) unconvertible text stored. Submit with a token that verifies successfully with a low score, and a success reply without score. Expected: (a)(b) accepted, screen shows 0.7; (c) unhandled technical error. Fail: (a)/(b) refused or erroring, screen shows 0.0; (c) accepted or defined refusal.
- **PR-RCAP-13 (new)**: From state (b), save an unrelated setting. Expected: parameter becomes 0.7 and a low score is refused. Fail: parameter stays absent or low score accepted.
- **PR-RCAP-10R1** (A3-RCAP-D5 input): split by proxy mode off/on with a forged forwarding header; predicate defined in the PROOF addendum.

## 3. `base_sparse_field` — semantic correction for REC-SPRS-08 (A3-SPRS-D2)

A2 re-read `models/models.py`@f2196226 L41–89 and `models/fields.py`@cb26946e L50–71. **A2 agrees with A3** (no dispute).

### SF-1R1-SPRS (replaces the last three sentences of SF-1; the first part — "same-model limit is advisory, no server-side constraint" — stands)

- When a registry-defined field is instantiated, only the pointed container's **name** is carried (models.py L84–88); the pointer's model is dropped.
- During reflection, the name is resolved against the field's **own** model (L59–63). If the own model has no field row of that name, a user error is raised (L64–69), which interrupts reflection (setup / upgrade availability risk). If it has one, the stored pointer is **silently rewritten** by raw SQL to that own-model row (L70–79).
- The compute and inverse read and write the container by name on the record itself (fields.py L53, L62–71).
- The resolution does not check the resolved row's type (L63 looks up by model and name only), so a same-named non-container field on the own model could become the target. The consequence of that case in core setup was not read.
- **Corrected risk statement**: a cross-model pointer can never cause storage in the other model's container. Its effects are (i) a user error at reflection time, or (ii) a silent re-point to a same-named row on the field's own model. The original wording "setup-time behaviour for that case is not visible in module scope" is **withdrawn**: the module-scope path is visible; only the timing of reflection for manual fields (core) is not.
- C13 note updated: "the target model is not checked" stays true at write time; at reflection the target is re-derived from the own model.
- Verdict on A1 C08 unchanged: PARTIAL (overclaim "limited to the same model").

- **PR-SPRS-10 (new)**: Create a manual field on model A whose pointer targets a container on model B; variant 1 A has no same-named field, variant 2 A has a same-named container. Trigger registry reload. Expected: variant 1 user error at reflection and nothing stored in B's container; variant 2 pointer re-pointed to A's container. Fail: a value is stored in B's container, or the pointer stays on B without error.

## 4. Limitations

- Static only. Core field-default wrapping, web-client save payload, core reflection timing for manual fields and the verifier's score scale were not read.
- Nothing in the original A2 reviews was edited; consumers must read this addendum together with them.
