# G01 PLATFORM_BASE — PROOF Addendum, Remediation Cycle R2 batch D — `phone_validation`, `onboarding`, `web_unsplash`

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. Parent Proof documents and the B3C Proof R1 addendum were not edited |
| Group / Modules | G01 PLATFORM_BASE / `phone_validation`, `onboarding`, `web_unsplash` |
| Cycle | Remediation Cycle **R2**, batch **D** |
| Date | 2026-09-27 |
| **REC input consumed (rule 4)** | REC addendum `G01_RECONCILIATION/G01_R2D_REC_ADDENDUM_20260927.md` sha256 **`a49c5364af68918dbfae19a0acd687e2bfdd552424e26b400f2144e1e82ace63`**, frozen 2026-09-27T16:32:58.198Z |
| Upstream A2 addendum | `G01_A2_REVIEWS/G01_R2D_A2_ADDENDUM_20260927.md` sha256 `3a4d1bdc8972e2cec1640c85d47e9f0cd23ea48ec8f071b71439c97ca1d0757e` |
| Input — A3 re-check (immutable) | `G01_A3_CHALLENGES/G01_B3C_A3_RECHECK_R1_20260927.md` sha256 `a30062c25bf3a2f8f41284b473863b3a97e12de8ae99d42c9d8733cf12a823a2` |
| Parent Proofs corrected (in part; sha256 equal to A3 R1 intake, unchanged) | phone `c0b58670e71096db44dc10c37d28ae94181452f8bbb9dbbebbfe4183a4e70ca9`; onboarding `841e394aebc53078b519d655d0783326c106d6271b5394fbc4f26d525da5c219` |
| B3C Proof R1 addendum consumed (immutable; the source of the two Proof-only residuals) | `G01_PROOF/G01_B3C_PROOF_ADDENDUM_R1_20260927.md` sha256 `c8fdd5a2c82cb442c52f6a98051efe0c99c5f505f33e9ad0dacd8cd551c18c82` |
| Governing rules | `MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` sha256 `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42`; `MASTER_DECISION_LOG_G01_20260927.md` sha256 `20c10c3efe3dddf321d888aba88b1f69e2e8455ee162274e934947d8c65a8981` (MD-07/MD-08) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` |
| External contact | Only `raw.githubusercontent.com`. **No request was sent to Unsplash, its CDN or any other external service** |
| Runtime device | **Not probed in this batch.** Runtime remains NOT-EXECUTED per the standing B3C device-offline record (`device_probe.txt` sha256 `e20166110bd83c07e65afdba822d903b65966a8cd4431327a75e6bba9bbd4aeb`, 2026-09-27T15:51:18Z); no new probe was run, and no runtime result is claimed |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/r2_batchD/` |
| Residuals addressed here | **R-PHON-1** (static basis case PC-PHON-31), **R-ONBD-1** (tally re-tag), **R-ONBD-2** (wording correction) |
| Residual addressed at REC only | R-PHON-2 (QID lineage), R-UNSP-1 (sub-tag) — see the REC R2D addendum; no Proof action needed |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** (Proof disposition for the R2D cases: PROOF PARTIAL — STATIC EXECUTED, RUNTIME NOT-EXECUTED) |

Clean room: neutral paraphrase, pointers only, no code reproduced. No percentages. No Formal Coverage claim. No QID answered. No git write operations. No existing artifact was edited. No runtime result is claimed or inferred.

## 2. Predeclaration and ordering evidence (rules 4 and 5)

| Step | UTC | Evidence |
|---|---|---|
| A2 R2D addendum frozen | 16:31:45.862Z | sha256 `3a4d1bdc…757e` |
| REC R2D addendum frozen | 16:32:58.198Z | sha256 `a49c5364…ce63` |
| Predeclaration file written and hashed | **16:33:15.982Z** | `PROOF_CASES_PREDECLARED_R2D.md` sha256 `d14e524f6e4712d4e39bbf220242e74954f965ac6968a71c091042b467ff5d25` (`predeclared_R2D.sha256`, `predeclared_R2D.ts`) |
| Proof R2D fetch started | 16:33:23.207Z | `proof_fetch_start.txt`. The `src_proof/` folder did not exist before this point |
| First (only) Proof R2D source file written | 16:33:23.646Z | `proof_blob_log.txt` sha256 `c3701cebd91715dbfd07d41db37857e985956ccb17c795f36ade9c23a1bc291f` |

Disclosure: the A2 and REC stages of this remediation read source into a separate `src/` folder before the predeclaration (A2 R2D §0.1, 16:28:07–16:28:09Z). Rule 5 requires predeclaration before the first **Proof** fetch into its own scratch, and that is met: `src_proof/` was created only after the predeclaration hash was written, and the single new fetch it contains (`phone_blacklist.py`) post-dates the predeclaration by 8 seconds.

## 3. Blob verification (Proof R2D fetch)

1 request: `addons/phone_validation/models/phone_blacklist.py` → `git hash-object` = `d94486f63734da6dd4abdbcd6c21f407466c8142`. **MATCH** against the value already on record in the B3C A2/REC/Proof addenda and the A3 R1 report (all cite the same blob for this file). No drift.

## 4. New static case — executed (closes the "no proof-requirement link" half of R-PHON-1's basis)

| PC | Layer | Links | Expected (predeclared, summary) | Fail (predeclared, summary) | Observed (paraphrased; pointer @ blob) | Result |
|---|---|---|---|---|---|---|
| **PC-PHON-31** | SOURCE | REC-PHON-31; PR-PHON-12 | The nested `create()` call inside `_remove`'s missing-value branch re-discovers and returns the just-archived entry, so both a tracking-log message and a posted note land on it | An emptiness guard exists on this path; or the nested create's existence search misses the just-archived entry; or `message_post` is scoped to genuinely new records only | `phone_blacklist.py`@d94486f6: `_remove` (L108-127) finds `records` for the submitted numbers including archived (L112), computes `todo` by membership (L113); if `records` is non-empty, `_track_set_log_message` (L115-116) then `action_archive()` (L117) run on it. `todo` (always non-empty for a no-value term, per PC-PHON-30) is passed to the model `create()` override (L118-119), which re-sanitizes on the acting user (L35), searches existing entries including archived (L45) — this re-finds the entry `_remove` just archived — keeps it inactive without reactivating (L48), excludes it from `to_create_filtered` (L51-52), and returns it as part of `existing \| created` (L57-58). Back in `_remove`, `message_post` (L120-125) runs over every record in that returned set, including the just-re-found, just-archived entry. No emptiness guard exists anywhere on L108-127 or L22-58 | **PASS** |

Static totals for this addendum: 1 executed. PASS 1, FAIL 0, PARTIAL 0, INCONCLUSIVE 0.

## 5. New runtime case — declared, NOT-EXECUTED (device not probed; standing offline record applies)

| PC | Links | Expected (summary) | Fail (summary) | Status |
|---|---|---|---|---|
| PR-PHON-12 | REC-PHON-31 | Two audit writes (tracking log + posted note) land on the same acting-user entry for one `_remove` call with a no-value input | One audit write only, or the writes land on different records | NOT-EXECUTED |

Runtime totals for this addendum: 1 declared. NOT-EXECUTED 1, PASS 0, FAIL 0.

## 6. Corrections to the B3C Proof R1 addendum (errata; that addendum is not edited)

### 6.1 R-ONBD-1 — PC-ONBD-05 re-tagged SUPPLEMENTARY, excluded from consumed totals

**Independent re-derivation (A2 R2D §2.2, adopted here):** `grep`-scanning the re-fetched `test_onboarding_concurrency.py` and `test_onboarding.py` for the three elevation constructs reproduces the B3C Proof addendum's own count exactly: 4 `api.SUPERUSER_ID` constructions (concurrency test) + 1 `with_user(...)` call (functional test, which lowers rather than raises rights) = 5, all inside `tests/`. The substance (zero elevation in runtime code, five in test-harness code) is unchanged and is not in dispute.

**Adjudication (adopting A3 R1 §4.2 in full):** PC-ONBD-05's FAIL is a predicate-integrity re-execution of an already-counted proposition, not an independent substantive finding — the same situation PC-PRIV-12 was in when it was labelled SUPPLEMENTARY and excluded from the tallies consumed by MASTER. Treating PC-ONBD-05 differently from PC-PRIV-12 in the same B3C addendum was the inconsistency A3 R1 flagged, not a double-count of the underlying elevation finding.

**Correction:**

| Field | Was (B3C R1, section 4/8) | **Now (R2D)** |
|---|---|---|
| PC-ONBD-05 tag | (untagged; counted as one of the 9 executed static cases) | **SUPPLEMENTARY (predicate-integrity re-execution).** Excluded from the static totals consumed by MASTER, on the same footing as PC-PRIV-12. The FAIL result itself is unchanged and stays on record as a process note: the parent predicate's post-hoc narrowing is what PC-ONBD-05R was declared to answer independently |
| B3C static totals (section 4/8) | "Static totals for this addendum: 9 executed. PASS 5, FAIL 1, PARTIAL 1, INCONCLUSIVE 1, RECORDED 1" | **Corrected for MASTER consumption: 8 executed independent propositions. PASS 5 (PC-PHON-30, PC-PRIV-24, PC-UTM-25, PC-UTM-26, PC-ONBD-05R), FAIL 0, PARTIAL 1 (PC-UNSP-27), INCONCLUSIVE 1 (PC-ONBD-20), RECORDED 1 (PC-PHON-29). PC-ONBD-05 (FAIL) is excluded as SUPPLEMENTARY, carried as a process note only** |

No REC class, Lane B label or proof link changes. REC-ONBD-15 and REC-ONBD-BR7 stay UPP pending runtime PC-ONBD-06 exactly as the B3C Proof addendum §7 recorded.

### 6.2 R-ONBD-2 — "deeper", not "widened"

**Independent re-derivation (A2 R2D §2.3, adopted here):** re-fetching all 8 controller files of the two onboarding dependents (`account`: `__init__`, `portal`, `terms`, `download_docs`, `tests_shared_js_python`, `catalog`; `payment`: `__init__`, `portal`) and re-grepping them for "onboarding" (case-insensitive) reproduces 0 hits, matching the B3C figure exactly. The **module** set PC-ONBD-20 probed (2 declared dependents) is narrower than the original A3 CH's 15-module probe; the **file** set within those modules (all 8 controller submodules, not just package `__init__.py`) is more thorough than the parent PC-ONBD-15 (package inits only). "Widened" describes an axis (module count) that in fact went down; "deeper" describes the axis that went up (files read per module).

**Correction:**

| Parent Proof | Item | Was (B3C R1, section 6) | **Now (R2D)** |
|---|---|---|---|
| onboarding | PC-ONBD-15 / PC-ONBD-20 | "PC-ONBD-15 INCONCLUSIVE stands. **The widened bounded search** PC-ONBD-20 is also INCONCLUSIVE" | "PC-ONBD-15 INCONCLUSIVE stands. **The deeper bounded search** PC-ONBD-20 (all 8 controller submodules of the 2 declared dependents, versus package inits only) is also INCONCLUSIVE. Its module set remains narrower than the original 15-module probe; the INCONCLUSIVE result is unaffected and does not supersede that broader probe" |

No verdict change. REC-ONBD-H3 and REC-ONBD-G1 stay GAP exactly as recorded.

## 7. Effect on REC items

| REC item | Effect of Proof R2D |
|---|---|
| REC-PHON-31 (new) | Static basis for the audit-duplication mechanism confirmed (PC-PHON-31 PASS). Item stays **UPP** pending runtime PR-PHON-12 |
| REC-PHON-21, REC-PHON-30 | Unchanged by this addendum (R-PHON-2's QID-lineage correction is a REC-only table edit; see the REC R2D addendum) |
| REC-ONBD-15, REC-ONBD-BR7 | Unchanged in class. The static totals MASTER consumes now carry one row per independent proposition (section 6.1) |
| REC-ONBD-H3, REC-ONBD-G1 | Unchanged (GAP; wording-only correction, section 6.2) |
| REC-UNSP-BR5, REC-UNSP-G5 | Unchanged by this addendum (R-UNSP-1's sub-tag is a REC-only edit; see the REC R2D addendum) |
| All other REC items | Unchanged. No UPP item is closed, because no runtime was executed |

## 8. Totals

| Set | Executed | PASS | FAIL | PARTIAL | INCONCLUSIVE | RECORDED | NOT-EXECUTED |
|---|---|---|---|---|---|---|---|
| R2D static (section 4) | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| R2D runtime (section 5) | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
| B3C static totals, corrected for MASTER consumption (section 6.1) | 8 | 5 | 0 | 1 | 1 | 1 | — |

## 9. Process-rule compliance (C1B rules 1–5, and MD-07/MD-08)

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Preserve A2 MRRP labels | **MET / N-A**. No Lane B label is changed by this addendum | — |
| 2 | Tag post-predeclaration text `POST-DECLARATION` | **MET.** The SUPPLEMENTARY tag and the "deeper" wording are corrections predeclared in `PROOF_CASES_PREDECLARED_R2D.md` before any R2D fetch; no R2D text was added or changed after execution | Section 2, 6.1, 6.2 |
| 3 | REC scans all A1 item classes | **MET (consumed)**. The REC R2D addendum's new item (REC-PHON-31) is linked here to a proof case and a runtime PR; the two Proof-only residuals touch no unreconciled A1 class | REC R2D addendum §1.1 |
| 4 | Order A2 → REC (sha256) → Proof predeclare → execute; the Proof header records the REC sha256 | **MET**. 16:31:45Z → 16:32:58Z → predeclare 16:33:15Z → fetch 16:33:23Z. The header records REC R2D addendum `a49c5364…ce63` | Sections 1, 2 |
| 5 | Predeclared cases hashed and UTC-stamped before the first Proof source fetch | **MET.** Hash/stamp at 16:33:15.982Z; first (only) Proof R2D fetch at 16:33:23.646Z, into a folder that did not exist before | Section 2 |
| MD-07 | Anchor-only evidence, `git hash-object`-verified | **MET.** The one new fetch (`phone_blacklist.py`) matches the blob already on record across three prior artifacts; no drift; no GitHub API or code search used | Section 3 |
| MD-08 | Enumeration claims bounded, not completeness | **MET.** Section 6.2 states the account/payment re-check as a bounded re-confirmation of the same 2-module, 8-file set the B3C Proof addendum already enumerated by manifest-dependency and import-following, explicitly narrower in module count than the original 15-module probe | Section 6.2 |

## 10. Limitations

- No runtime was executed and no runtime result is claimed. PR-PHON-12 remains open pending a live runtime device.
- The time-stamp evidence rests on self-written scratch files and file mtimes, not a committed record (same limitation the B3C addenda and A3 R1 disclosed). No git write operations were run.
- Mail-thread message sequencing and chatter rendering (which PR-PHON-12 will exercise) were not read; PC-PHON-31 establishes only the source-level control-flow mechanism.
- No percentages. No Formal Coverage claim. No QID answered.
