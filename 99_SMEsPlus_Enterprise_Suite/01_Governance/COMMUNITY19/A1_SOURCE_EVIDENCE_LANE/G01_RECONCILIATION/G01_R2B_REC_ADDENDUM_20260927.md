# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum (Cycle R2, batch B) — `resource`, `resource_mail`, `google_recaptcha`, `base_sparse_field`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. All parent REC files and all R1 REC addenda are immutable and were not edited. |
| Cycle | **R2 (remediation of A3-sustained residual defects, Cycle R2)**, remediation batch **B** |
| Group / Modules | G01 PLATFORM_BASE / `resource`, `resource_mail`, `google_recaptcha`, `base_sparse_field` |
| Date | 2026-09-27 (written after the A2 addendum below; sealed **before** the PROOF addendum for this cycle) |
| A2 addendum consumed (this cycle) | `G01_A2_REVIEWS/G01_R2B_A2_ADDENDUM_20260927.md`, sha256 **`5b1cf760b703326be12663b74aa83cfb50a3ac3df67c9e4f49f85ddc0847174f`**, frozen 2026-09-27T16:32:55.456Z (recorded before this REC addendum's own text below was sealed) |
| R1 addenda consumed (immutable inputs) | bus/digest/resource/resource_mail A2 R1 `9664c13e01c777e4731381966a412b4a9eea675168ec5ad4f848c56d0a6a037c`; REC R1 `18292fd3418f26152330446fc20080f4fd453a04c3555c1932807652e56c5331`; PROOF R1 `141fb8558c59303a9e6395d4bd6fd2b26bf5fb865d6d094988153108fd0854f9`; RCAP/SPRS A2 R1 `86260c80f355d611b95da177b89be32195cbbde7fcd6f8ea983575ca1455a896`; RCAP/SPRS REC R1 `e8d748b2d965501f5699325458d73b06d003306e6dad90a6f44f0b6e6c3b89cd`; RCAP/SPRS PROOF R1 `8528361c7c6d763d6d9f68b1a3853ae6e83c05c8c4a2cb2f2b6b483a8a791707` |
| A3 re-checks consumed | `G01_BATCH2_A3_RECHECK_R1_20260927.md` `52a0e7f1b9b98f46a962025b38b1cf518851653aeb11a613e7e7d5d9a5043261`; `G01_RCAP_SPRS_A3_RECHECK_R1_20260927.md` `528be113bc8fc35f5d9afbbdd79b4abb80e5c24f200c69e48889227822b9b4e4` |
| Parent REC artifacts touched by this addendum (sha256, unchanged, re-verified 2026-09-27) | `G01_RESOURCE_REC_20260927.md` `e2adc10a1f346bb5dc1fe73100d3187c485a1208c12af6bc3a4732475a0fe259`; `G01_RESOURCE_MAIL_REC_20260927.md` `1ec90af273af437692663390db5e4d182cf4490204385dbf67d25fefed8cb26f` |
| Residuals addressed | **R-RSRC-1** (restore `MISSING_REQUIRED_RUNTIME_PROOF` on the `resource`/`resource_mail` REC rows A2 originally so labelled); **RCAP/SPRS R-2** (REC-then-PROOF ordering violation in R1 — disposed here) |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: neutral paraphrase only, identifiers as pointers, no code reproduced. No percentages. No Formal Coverage claim. No QID answered (lineage only). No git write operations. No existing artifact was edited.

---

## 1. R-RSRC-1 — restoring the A2 `MISSING_REQUIRED_RUNTIME_PROOF` label on `resource` and `resource_mail`

### 1.1 Rule found from source of the defect (not re-derived; this is a label-carry rule, no new source fact needed)

A3's residual finding: the parent A2 reviews for both modules label their own runtime-only proof requirement sets — `resource` PR-01..PR-10 (`G01_RESOURCE_A2_REVIEW_20260927.md` §7, heading "Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF — inherently runtime only)") and `resource_mail` PR-01..PR-03 (`G01_RESOURCE_MAIL_A2_REVIEW_20260927.md` §7, heading "Proof requirements (MISSING_REQUIRED_RUNTIME_PROOF)") — but the R1 REC addendum mapped every runtime-linked item in these two modules to `UNCORROBORATED` (or, where static, `NOT_APPLICABLE`), never restoring the `MISSING_REQUIRED_RUNTIME_PROOF` label the way the same R1 addendum did for `bus` (§1.1, 8 rows) and `digest` (§2.1, 7 rows).

**Rule applied (same rule the R1 addendum already applied to `bus`/`digest`, carried here without change):** the Lane B column reads `MISSING_REQUIRED_RUNTIME_PROOF` on the REC row that is the **direct** carrier of an original A1 claim (`Cxx`) for which A2 §7 declares a numbered proof requirement (`PR-xx`) under that exact heading. A REC row that instead originates from an **omission A2/REC itself discovered** (an `OM-xx` row, even when it happens to share the same `PR-xx` runtime link as a `Cxx` row) keeps `UNCORROBORATED`, because A2 did not declare *that* row's own claim `MISSING_REQUIRED_RUNTIME_PROOF` — only the original claim was so declared. This is exactly how the R1 addendum treated `bus` (REC-BUS-03/05/07/09/13/14/17/18 restored; REC-BUS-21..24, which share `PR-BUS-09`/`06` with restored rows, were **not** restored) and is applied here without modification.

### 1.2 `resource` — every affected REC row (enumerated)

| REC ID | A1 claim | A2 proof requirement (§7 heading) | Parent/R1 Lane B | **R2 Lane B** |
|---|---|---|---|---|
| REC-RSRC-01 | C01 | PR-01 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-02 | C02 | PR-02 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-04 | C04 | PR-03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-05 | C05 | PR-04 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-07 | C07 | PR-05 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-08 | C08 | PR-06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-09 | C09 | PR-07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-10 | C10 | PR-07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RSRC-17 | C17 | PR-08 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

**Not restored (kept UNCORROBORATED — omission-sourced rows, per the rule in 1.1):** REC-RSRC-11 (OM-01, shares PC-RSRC-12 basis with REC-RSRC-20), REC-RSRC-20 (OM-02), REC-RSRC-21 (OM-03, shares PR-10 with REC-RSRC-26), REC-RSRC-22 (OM-04, shares PR-09), REC-RSRC-23 (OM-05, shares PR-04 with REC-RSRC-05), REC-RSRC-24 (OM-06, shares PR-06 with REC-RSRC-08 — the same pattern the R1 addendum applied to REC-BUS-24 against REC-BUS-18), REC-RSRC-25 (OM-07, shares PR-07 with REC-RSRC-09/10), REC-RSRC-26 (OM-08, shares PR-10), REC-RSRC-27 (OM-09, no PR-numbered link), REC-RSRC-28 (OM-10, no PR-numbered link), and the new R1 items REC-RSRC-29..35 (N1–N7, all A2-addendum-derived, not original `Cxx` claims). REC-RSRC-06 (CONTRADICTION) and REC-RSRC-19 (OM-01/GAP) have no A2 §7 `PR` declared against their own claim number and are unaffected. REC-RSRC-03/12/13/14/15/16/18 remain as R1 left them (NOT_APPLICABLE or UNCORROBORATED per the R1 S-B correction, unaffected by R-RSRC-1).

**Recomputed Lane B column for `resource` (R2):** NOT_APPLICABLE 2 (unchanged: REC-RSRC-03, 15) + UNCORROBORATED **24** (33 minus the 9 restored) + **MISSING_REQUIRED_RUNTIME_PROOF 9** = **35** (unchanged total; matches the R1 total of 35). FAIL 0. Class counts (MATCH 7 / GAP 11 / CONTRADICTION 1 / UNKNOWN_PENDING_PROOF 16) are **unchanged** — R-RSRC-1 is a Lane B label correction only, not a reclassification.

### 1.3 `resource_mail` — every affected REC row (enumerated)

| REC ID | A1 claim | A2 proof requirement (§7 heading) | Parent/R1 Lane B | **R2 Lane B** |
|---|---|---|---|---|
| REC-RMAIL-01 | C01 | PR-01 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RMAIL-03 | C03 | PR-02 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-RMAIL-04 | C04 | PR-03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

**Not restored (kept UNCORROBORATED — omission-sourced rows sharing PR-03 with REC-RMAIL-04):** REC-RMAIL-06 (OM-01), REC-RMAIL-07 (OM-02). REC-RMAIL-02 stays UNCORROBORATED per the R1 M-B correction (unaffected by R-RSRC-1; it carries no A2 §7 `PR` link at all). REC-RMAIL-05 stays NOT_APPLICABLE (declared absence, unaffected).

**Recomputed Lane B column for `resource_mail` (R2):** NOT_APPLICABLE 1 (unchanged: REC-RMAIL-05) + UNCORROBORATED **3** (6 minus the 3 restored: REC-RMAIL-02, 06, 07) + **MISSING_REQUIRED_RUNTIME_PROOF 3** = **7** (unchanged total; matches the R1 total of 7). FAIL 0. Class counts (MATCH 2 / GAP 2 / UNKNOWN_PENDING_PROOF 3) are **unchanged**.

### 1.4 Effect

This is a **label-only** correction (Lane B column), carried forward exactly as the R1 addendum already did for `bus`/`digest`. No REC class (MATCH/GAP/CONTRADICTION/UNKNOWN_PENDING_PROOF) changes, no proof link changes, no runtime is claimed, and no percentage or coverage figure is stated. R-RSRC-1 is **CLOSED**.

---

## 2. RCAP/SPRS R-2 — REC-then-PROOF ordering violation (R1), disposition

### 2.1 The violation (as found by A3)

The RCAP/SPRS A3 re-check (§6, rule 4 row) found: the R1 PROOF header records the R1 REC addendum's sha256 (`e8d748b2b2…8b9cd`), but the R1 REC addendum was **written at 15:24:11Z, after** Proof's static execution at 15:21:21Z, and its own text **cites Proof-derived wording** ("source premise confirmed by PC-RCAP-06R" in the REC-RCAP-09R1 class column). This breaches C1-B rule 4 (REC must be frozen, sha256 recorded, **before** PROOF executes).

### 2.2 Disposition chosen: **option (a) — independent re-derivation, confirmed to land the same**

Per the task routing, this residual is resolved by reconstructing REC's classification independently of the R1 Proof text and confirming it still lands the same way, rather than by declaring the R1 rows an unresolved ordering violation routed to R3.

**Independent basis:** the A2 addendum (this cycle), section 1, re-derives the entire min-score chain (T1–T9) directly from the anchor files (`ir_http.py`, `res_config_settings.py`, `ir_config_parameter.py`, `res_config.py`), fetched fresh in this R2 session and `git hash-object`-verified, **without** starting from or citing the R1 Proof addendum's wording. That independent trace reproduces, fact for fact:

- absent parameter → `False` → `0.0`, gate silently off (supports REC-RCAP-09R1's premise, "source premise confirmed", now confirmed **independently** rather than by citing PC-RCAP-06R's own text);
- saving `0.0` deletes the parameter (supports the GAP/UNKNOWN_PENDING_PROOF framing carried by REC-RCAP-10R1/11R1, which rest on the same absent-parameter chain);
- the screen shows `0.7` while the enforced value is `0.0`/off, and any settings save while absent rewrites `0.7` (the MED-confidence new finding the R1 Proof addendum recorded as PC-RCAP-30, itself independently reproduced in A2 addendum section 1, step T9, without reference to that case's Proof text).

**Conclusion:** REC-RCAP-09R1 (UNKNOWN_PENDING_PROOF), REC-RCAP-10R1 (GAP) and REC-RCAP-11R1 (GAP), as classified by the R1 REC addendum, **land the same way** under an independent re-derivation performed in this cycle. The MASTER consumption rule the R1 REC addendum attached to these three items (static-content consumption only, runtime still blocked) is **unaffected** and continues to apply.

**What is and is not fixed by this disposition:**
- The **substantive classifications** (REC-RCAP-09R1/10R1/11R1) are confirmed independently and are **not** disturbed.
- The **process defect itself** — that the R1 REC addendum's own text, as written, cites Proof-derived wording and was finalized after Proof's execution window — is **not retroactively repairable**. The R1 REC addendum is immutable and is not edited by this addendum. This matches the R1 addendum's own treatment of the equivalent `resource` ordering problem (S-E, "the parent's order problem... cannot be repaired retroactively and remains INCONCLUSIVE for the parent").
- Going forward (this cycle, and by MASTER decision applicable to future rounds): REC must be frozen (sha256 + UTC timestamp recorded) **before** any Proof text for the same cycle is written. This addendum's own header records its freeze timestamp (below) **before** the R2B PROOF addendum was written, so this cycle itself does not repeat the violation.

### 2.3 Freeze record (this addendum)

This REC addendum's full text above is sealed at the timestamp and sha256 recorded in the header of the PROOF addendum (which consumes and cites this file's sha256, computed **after** this text was finalized and **before** any PROOF-addendum text for this cycle was written). No PROOF case text exists yet for this cycle at the time this REC addendum is sealed; PROOF (this cycle) states nothing beyond RUNTIME NOT-EXECUTED and a process-only record, so there is no proof-derived wording in this REC addendum for the same reason there was in the R1 addendum.

RCAP/SPRS **R-2 is CLOSED** under option (a): the substance is independently confirmed unchanged; the R1 process defect is recorded, not repaired retroactively, consistent with how R1 itself treated its own unrepairable ordering defects.

---

## 3. `base_sparse_field` — no REC change

No A3-sustained residual defect names `base_sparse_field` for REC in this batch (its two closed defects, A3-SPRS-D1/D2, carry no open REC residual; see the RCAP/SPRS A3 re-check §7, which routes only R-1, R-2, R-3, R-4, R-6, R-7 — none to `base_sparse_field` REC specifically beyond R-2, disposed in section 2 for the RCAP/SPRS pair as a whole). No REC row for `base_sparse_field` is changed by this addendum.

---

## 4. Limitations

- REC reconciles documents; the source re-derivation this addendum relies on for R-2 is recorded in the A2 addendum (this cycle), section 1.
- No Lane B (runtime) evidence exists for any of the four modules; nothing here is runtime-corroborated. No REC class was changed for R-RSRC-1 (label-only) or R-2 (confirmed, not reclassified).
- No percentages, no Formal Coverage claim, no QID answered. No git write operations. No parent or R1 artifact was edited.

## 5. Rule-compliance table

| Rule | Compliance | Evidence |
|---|---|---|
| C1-B rule 1 (preserve A2 MRRP label; do not collapse to UNCORROBORATED) | **MET (remediated)** — this is the R-RSRC-1 fix itself: 9 `resource` rows + 3 `resource_mail` rows restored to `MISSING_REQUIRED_RUNTIME_PROOF`; every omission-sourced row correctly kept UNCORROBORATED | Sections 1.2–1.3 |
| C1-B rule 2 (tag post-declaration Expected text) | **N/A** — this addendum declares no new proof case Expected/Fail text | — |
| C1-B rule 3 (REC must scan all A1 item classes) | **Not re-scanned in this batch** — this addendum only restores a Lane B label and disposes an ordering residual; it does not re-open the R1 QID lineage work for `resource`/`resource_mail`/`google_recaptcha`/`base_sparse_field`, which A3 did not fault | — |
| C1-B rule 4 (REC frozen, sha256 recorded, before PROOF executes; PROOF records the REC sha256 consumed) | **MET for this cycle** — this file's sha256 is recorded and its freeze precedes the R2B PROOF addendum (see PROOF header); **RCAP/SPRS R-2 (the R1 violation) is disposed under option (a)** in section 2, not repaired retroactively | Section 2.3; PROOF addendum header |
| C1-B rule 5 (cases sha256 + UTC timestamp before first source fetch) | **N/A** — no new proof cases are declared in this cycle | — |
| MD-04/MD-09 (different-author runtime execution) | **N/A this cycle** — no runtime executes (device offline) | — |
| MD-05 (rule-compliance table in every addendum) | **MET** (this table) | — |
| MD-06 (commit subject/body) | Applies at commit time (Integration Control / MASTER) | — |
| MD-07 (anchor-fetched, `git hash-object`-verified evidence only; no code search/index/training recall for completeness) | **MET** — this addendum's own claims rest on the A2 addendum's section 1 trace (anchor-fetched, hash-verified in this session) and on the `resource`/`resource_mail` A2 review §7 headings (read directly, quoted verbatim in section 1.1) | Section 1.1; A2 addendum §0.2 |
| MD-08 (enumeration claims must state method, be reproducible, or be bounded) | **MET** — sections 1.2–1.3 state the exact rule used to include/exclude each row and list every excluded row with its reason; no "only" or "complete" claim is made beyond the two modules' own REC tables, which are enumerated in full | Sections 1.2–1.3 |
