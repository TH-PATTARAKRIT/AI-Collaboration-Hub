# G01 PLATFORM_BASE — PROOF Addendum R1 (A3 remediation, batch 3C) — `phone_validation`, `privacy_lookup`, `utm`, `onboarding`, `html_builder`, `web_hierarchy`, `web_unsplash`

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. The parent Proof documents were not edited |
| Group / Modules | G01 PLATFORM_BASE / `phone_validation`, `privacy_lookup`, `utm`, `onboarding`, `html_builder`, `web_hierarchy`, `web_unsplash` |
| Date | 2026-09-27 |
| **REC input consumed (rule 4)** | REC addendum `G01_RECONCILIATION/G01_B3C_REC_ADDENDUM_R1_20260927.md` sha256 **`c77ed8a00d6a6d88c6f34c3356ee3b64c645ee8e9950296d6e88ab8492709f6b`**, frozen 2026-09-27T15:48:54.394Z. Parent REC files (frozen values, recorded in that addendum's header; unchanged since A3 intake): phone `87a34f17b618b902a8933413c706c76cdaeccc9cfec6d6fd3626160c7187a717`; privacy `86a047dce7eac80b3b2563bd815f770e54d9de8d42734711de5becc9b787c41a`; utm `cd2576689b4b0412614109f11ff7b2c1eafd5d3cf4460c8c2ee65fbc68e19975`; onboarding `fdd2d41b3b3cfdc7d5612820ff46c6c226da92d95d27012adbbd384308b91889`; html_builder `d6efb05e3e3893dce981084d0f2a93cefa42b017cdb1a407677f5aa3d51b9803`; web_hierarchy `ac6842312bd2159b6b642f7fafe929cc30ac72d1f14cfc382aff70df77509e53`; web_unsplash `66eb15218a853ab0f43589e5558b4622586080aa3d8c1a8a2f6eb2a5de1f3ffd` |
| Upstream A2 addendum | `G01_A2_REVIEWS/G01_B3C_A2_ADDENDUM_R1_20260927.md` sha256 `a364fa30d6007c06dc34f79747a8bc6fc60afea71a4bacf131940a0720581750` |
| Parent Proofs (superseded in part; sha256 equal to A3 intake) | phone `c0b58670e71096db44dc10c37d28ae94181452f8bbb9dbbebbfe4183a4e70ca9`; privacy `8fe1bd6057c13cf7298202bcabaf888f29f8428dc9c8ee9cd27605ec1e5b4a23`; utm `25e3ccc262cd28f66c6b1923e25ae31053e83654f89ff90d30c3dfd7d0a135b6`; onboarding `841e394aebc53078b519d655d0783326c106d6271b5394fbc4f26d525da5c219`; html_builder `9f75d2414ac0634a714902e0f0f1a9497318c564e344302a39b0dec14f0d369b`; web_hierarchy `86510da84a062ce33dc157af50a35b2f3dc11dd0df0bd13784e52351ef6a4aa9`; web_unsplash `434e20f82ef2832700ce52cd60412aa8fc410fc3a0ebb002bd56dc5f550adf9b` |
| A3 reports | As listed in the A2 addendum section 0.2 |
| Governing rules | `MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` sha256 `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` |
| External contact | Only `raw.githubusercontent.com`. **No request was sent to Unsplash, its CDN or any other external service** |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local is **OFFLINE**: `getent hosts` rc=2 at 2026-09-27T15:51:18Z (`device_probe.txt` sha256 `e20166110bd83c07e65afdba822d903b65966a8cd4431327a75e6bba9bbd4aeb`) |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/remed_b3c/` |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** (Proof disposition for the R1 cases: PROOF PARTIAL — STATIC EXECUTED, RUNTIME NOT-EXECUTED) |

Clean room: neutral paraphrase, with pointers only and no code reproduced. No percentages. No Formal Coverage claim. No QID answered. No git operations. No existing artifact was edited. No runtime result is claimed or inferred.

## 2. Predeclaration and ordering evidence (rules 4 and 5)

| Step | UTC | Evidence |
|---|---|---|
| A2 addendum frozen | 15:42:01.118Z | `a2_addendum.sha256` → `a364fa30…1750` |
| REC addendum frozen | 15:48:54.394Z | `rec_addendum.sha256` → `c77ed8a0…9f6b` |
| Predeclaration file written | 15:49:53.38Z (file mtime) | `PROOF_CASES_PREDECLARED_R1.md` |
| **Predeclaration hashed and time-stamped** | **15:49:57.247Z** | sha256 **`62591154d8c1198f21b137979f3edc5ac8f5eac18839635d626312cf91e6735e`** (`predeclared_R1.sha256`; `predeclared_R1.ts`) |
| Proof R1 fetch started | 15:50:09.971Z | `proof_fetch_start.txt`. The `src_proof/` folder did not exist before this point (checked at predeclaration) |
| First Proof R1 source file written | 15:50:10.512Z | `proof_blob_log.txt` line 1 |
| Execution | 15:50:55Z – 15:51:12Z | `exec_R1.txt` sha256 `06478c55b793635de31b3ebff4c972b9478dfd31ac68fd32f63715e5bb88f53d` |

Disclosure: the A2 and REC stages of this remediation read source (A2 fetch at 15:36:52Z into the separate `src_a2/` folder) before the cases were written. Rule 5 requires predeclaration before the first **Proof** fetch, and that is met. To counter confirmation bias, every new static case carries an explicit disconfirming fail branch, and one of them (PC-ONBD-05, verbatim re-execution) was **expected** to fail.

## 3. Blob verification (Proof R1 fetch, `proof_blob_log.txt` sha256 `649b8bb30f9d29e842857442f8ceb992b16967a5962554ff90a833018dc7271d`)

32 requests:
- 21 files match their recorded blob: all phone, privacy, utm and onboarding files carrying a prior record, plus `web_unsplash/controllers/main.py` `00cf725f`.
- 1 expected absence was confirmed: `addons/onboarding/controllers/__init__.py` returned HTTP 404.
- 10 files are new lineage records:
  - `addons/portal/controllers/portal.py` `e6b03c24fa227c362a20d6811cfa5c59cf717f02`;
  - `addons/account/controllers/__init__.py` `85c15401…`, `portal.py` `ed85ff8b…`, `terms.py` `f57296c0…`, `download_docs.py` `2403b0c6…`, `tests_shared_js_python.py` `1a157c73…`, `catalog.py` `d3d263dd…`;
  - `addons/payment/controllers/__init__.py` `10ef4ca2…`, `portal.py` `85549665…`;
  - `odoo/addons/base/models/ir_config_parameter.py` `21c82bf62ed0fec4b4307c935f8a2b4ebaff4321`. This value equals the blob recorded for this file in the rcap remediation (`G01_RCAP_SPRS_PROOF_ADDENDUM_R1`, "A2-X6 21c82bf6").

## 4. New static cases — executed

| PC | Layer | Links | Expected (predeclared, summary) | Fail (predeclared, summary) | Observed (paraphrased; pointer @ blob) | Result |
|---|---|---|---|---|---|---|
| **PC-PHON-30** | SOURCE | REC-PHON-21, ST1; PR-PHON-11 | Remove formats with raising off. The "missing" list treats a no-value as missing. Missing values are created with the inactive flag. Create formats on the acting user and falls back to that user's number. An existing entry requested inactive stays inactive. The reset helper passes values elevated with no guard | Emptiness guard; empty values excluded from "missing"; reactivation; user-independent formatting | `phone_blacklist.py`@d94486f6: remove formats with raising off (L104–106). "Missing" is computed by membership against found numbers (L113), so a no-value is always missing. Missing values are created inactive (L118–119). Create formats on the acting user with raising on (L35) and searches existing entries including archived (L45). Requested-inactive existing entries are kept inactive (L48–50), and only unfound numbers are created (L54–55). `models.py`@dccf9fbf L75–82: with no number, the formatter reads the singleton's number fields, else returns no value. `mail_thread_phone.py`@01ca256f L245–246: reset passes sanitized values under elevation. No emptiness guard in L104–127 (the only membership filter is the "missing" computation) | **PASS** |
| **PC-PHON-29** | CROSS-MODULE (observation) | REC-PHON-H3, REC-17, GAP-PHON-02 | Record whether the portal deactivation route calls the users hook elevated | — (observation) | `portal/controllers/portal.py`@e6b03c24 L914–928: the account-deactivation route (user auth, POST) checks the login confirmation and the credentials, then calls the users deactivation hook **on the elevated current user** (L926). The phone override therefore runs its list add in an elevated environment (`phone_validation/models/res_users.py`@ca7def5e L20–25). Elevation keeps the acting user id | **RECORDED-ELEVATED** |
| **PC-PRIV-24** | SOURCE | REC-PRIV-19 wording, BR2 | Flush, then direct cursor execution with no elevated wrapper and no company or access predicate. Elevation only at the display name, archive, delete and model list | Elevated discovery; company predicate; remediation not elevated | `privacy_lookup_wizard.py`@3b6d52e0: flush (L167), then direct cursor execution (L168), with no elevation on this path. Elevation appears only at the model list (L222), the display name (L282), archive/unarchive (L295) and delete (L301). The only "company" hits are one field name in the email-like list (L112) and a comment (L255). Neither is a predicate | **PASS** |
| **PC-UTM-25** | SOURCE | REC-UTM-19; PR-U4R | Parameter → cookie with no module-level encoding. Cookie → find-or-create. Trim, then an unescaped equals-pattern | Any module-level encode, escape or validation | `ir_http.py`@8a6e6e4f L20–21: the request-layer parameter value is written to the cookie as-is. `utm_mixin.py`@0c8be65a L39, L41–43: the cookie value goes to find-or-create. L92–94: trim, then the equals-pattern operator, unescaped | **PASS** (request-layer decoding and cookie-library encoding are outside the module and were not read, so PC-UTM-18R keeps its setup check) |
| **PC-UTM-26** | SOURCE | REC-UTM-30; PR-U11 | Title translatable; identifier non-translatable, stored and computed from the title in the current environment; free text matches the identifier | Any of these not so | `utm_campaign.py`@a9b07365 L13–14 (identifier: computed, stored, non-translatable), L15 (title translatable), L36–42 (compute reads each title in the current environment). `utm_mixin.py` L94: free text matches on the identifier | **PASS** |
| **PC-ONBD-05** (verbatim re-execution of the parent predicate) | SOURCE/CONFIG | REC-ONBD-15 | Parent predicate unchanged: "only system rows non-zero; zero elevation calls in module code" across **all module .py** | "any non-system grant or any elevation call" | ACL `security/ir.model.access.csv`@f99bf429: only the four system-group rows are non-zero; the "all" and internal-user rows are all zero. Scan of all 12 module .py files: **5 elevation constructs, all under `tests/`**. There are 4 superuser environment constructions in `test_onboarding_concurrency.py`@801def35 (L25, L37, L49, L72) and 1 user switch in `test_onboarding.py`@32649804 (L236), which lowers rights | **FAIL** (literal predicate). Explanation: every hit is test-harness code that is not loaded at normal runtime, and none is in models or package init. The runtime-scope question is answered by PC-ONBD-05R |
| **PC-ONBD-05R** | SOURCE/CONFIG | REC-ONBD-15, BR7 | Runtime code (package init, manifest, models/__init__, 4 model files): zero elevation constructs; system-only ACL | Any construct in runtime code, or a non-system grant | 0 constructs in the runtime-code set. ACL as above | **PASS** |
| **PC-ONBD-20** | CROSS-MODULE (bounded) | REC-ONBD-H3, GAP-1 | "/onboarding" route owner identified with its auth mode | Not found → INCONCLUSIVE. FAIL only if in-module absence is disproved | `addons/onboarding/controllers/__init__.py` returned 404 (absence re-confirmed). `account` and `payment` both declare a dependency on `onboarding` (A2 re-derivation: `account/__manifest__.py`@f3e264e5 L17, with onboarding data at L25; `payment/__manifest__.py`@93c02fd0 L8). Their controllers packages import 5 and 1 submodules. All 8 controller files were fetched, and **0 mention "onboarding"** | **INCONCLUSIVE** (bounded; not proof of dead documentation) |
| **PC-UNSP-27** | CROSS-MODULE | REC-UNSP-ST1, REC-UNSP-21 | A falsy value passed to the set method removes the parameter. The route passes request values as received | A falsy value is stored as-is, or the parameter is kept | `ir_config_parameter.py`@21c82bf6 L82–103: an existing parameter is **removed** when the new value is false or none (L94, L97–98). An empty string is **written** as an empty value (L94–96), because only false and none trigger removal. `main.py`@00cf725f L152–157: both values are passed straight from the request payload (an absent key gives none) under elevation | **PARTIAL**. Confirmed for an absent value: the credential is removed, which makes it revocation by omission. Disconfirmed for an empty string, which is stored as an empty value (still a blanked credential, but not removed) |

Static totals for this addendum: 9 executed. PASS 5, FAIL 1, PARTIAL 1, INCONCLUSIVE 1, RECORDED 1.

## 5. New runtime cases — NOT-EXECUTED (device offline)

All cases below were predeclared in `PROOF_CASES_PREDECLARED_R1.md` (sha256 `62591154…735e`). None was executed, and no result is inferred from the static cases.

| PC | Links | Expected (summary) | Fail (summary) | Status |
|---|---|---|---|---|
| PC-PHON-28R | PR-PHON-11; REC-PHON-21 | (i) N_u's entry archived; (ii) a new archived entry for N_u; (iii) as (i) through the reset helper | Validation error or no-op; no N_u entry archived or created | NOT-EXECUTED |
| PC-PRIV-23 | REC-PRIV-19 | Email `%@%` with a non-matching name returns unrelated "@"-bearing logins and email-field records | Only exact-subject records; input rejected | NOT-EXECUTED |
| PC-UTM-18R | PR-U4R; REC-UTM-19 | With `%25` sent and the cookie verified as a literal single percent sign, an existing source is linked and no literal "%" source is created | A literal "%" source is created; none linked while sources exist. SETUP-INVALID if the cookie value differs | NOT-EXECUTED |
| PC-UTM-27 | PR-U11; REC-UTM-30 | An L2 title edit changes the identifier; the old-identifier revisit creates a new auto-campaign | Identifier unchanged; original campaign linked | NOT-EXECUTED |
| PC-UTM-28 | REC-UTM-EX4 | Exact-name create of an archived medium hits the uniqueness constraint | Created with a suffix, or the archived medium reused | NOT-EXECUTED |
| PC-UNSP-08R | REC-UNSP-09; PR-UNSP-04 | Local-mock redirect from an allow-listed prefix to an internal listener is followed | Not followed, or final host re-checked. SETUP-INVALID on a TLS failure or prefix rejection | NOT-EXECUTED |
| PC-UNSP-26R | REC-UNSP-16; PR-UNSP-13 | A non-provider URL under the notify prefix receives a request carrying the server key (captured by the mock) | Not sent. SETUP-INVALID on a TLS failure | NOT-EXECUTED |

Runtime totals for this addendum: 7 declared. NOT-EXECUTED 7, PASS 0, FAIL 0.

### 5.1 web_unsplash runtime pack amendment (D-UNSP-A3-4)

This amendment was declared in the R1 predeclaration. It replaces the parent §6 pack for PC-UNSP-08 and PC-UNSP-26 and adds conditions for every mock case.

1. **Non-substitution statement.** A local-mock outcome establishes only this module's behaviour against a controlled endpoint (redirect following, parameter forwarding, timeout absence, batch abort). It **cannot** settle claims about the real provider:
   - A1 GAP-5 (whether provider hosts actually redirect; this decides C09 exploitability);
   - A1 BR-5(b) ("as its API terms require");
   - provider-side quota or parameter handling.

   No mock result may be cited as closing any of these. They are marked PROVIDER CLAIM — NOT SOURCE-PROVABLE in the REC addendum (REC-UNSP-BR5, REC-UNSP-G5).
2. **TLS trust for mocked hosts.** The mock must serve HTTPS on the mocked allow-listed hosts with a certificate from a locally generated CA. That CA must be trusted by the server's outbound HTTP client, scoped to the isolated instance only. Without it, the mock cannot answer on the allow-listed prefixes. A TLS failure is recorded as SETUP-INVALID, not as PASS or FAIL.
3. **Non-test-mode requirement for PC-UNSP-08R and PC-UNSP-26R.** The platform current-test marker must **not** be set, and requests must go through the normal HTTP route. The marker disables both prefix checks (`main.py`@00cf725f L34, L84), which are the checks these cases exercise. PC-UNSP-10 is the exception: it tests the bypass itself and must run with the marker set.
4. Real egress stays blocked. No request may reach the real provider.

## 6. Corrections to parent Proof records (errata; parents not edited)

| Parent Proof | Item | Correction |
|---|---|---|
| phone | **PC-PHON-23** (A3-PHON-D2) | Recorded **PASS → PARTIAL (static)**. The mechanics are confirmed. The predeclared caller-elevation element was not established by that case, because the portal controller was not read. That element is now supplied separately by **PC-PHON-29 (RECORDED-ELEVATED)**. PC-PHON-23 is not retroactively upgraded. Parent static totals become: 16 executed, PASS 15, PARTIAL 1, FAIL 0 |
| phone | Header "Source anchor" wording (A3-PHON-D3) | Replace "fetched 2026-09-27 15:06:04–05 UTC" with: "fetch-start marker written 15:06:04.877 UTC; first source file written 15:06:05.15 UTC". 15:06:04 is the marker time, not a download. This is consistent with "first fetch 15:06:05" in the predeclaration row |
| phone | §3.2 R1 "they do not change any verdict" | **Superseded.** R1 is HIGH under SF-PHON-01 (A2 addendum SF-PHON-01-R1; REC-PHON-21), and it includes the absent-entry branch (PC-PHON-30 PASS) |
| phone | §6 proposal PC-PHON-28 | Superseded by the predeclared **PC-PHON-28R**, which covers both branches |
| privacy | **PC-PRIV-12** (A3-PRIV-D3) | Labelled **SUPPLEMENTARY (static harness)**. It is excluded from static and runtime tallies used for MASTER consumption. **`POST-DECLARATION` method change:** the predeclared case named a source read, while the harness (`harness_email.py` sha256 `30988af7…b783`) was written at 15:08:08Z, after the predeclaration hash at 15:06:04Z. The expected and fail conditions were predeclared; the method was not. **Binding:** the result holds for anchor code executed under local Python 3.11.15 only. Parser strictness itself is selected at import time from the standard library (`odoo/tools/mail.py`@2b05c91f L56–61). For wildcard-only inputs, the static reading supports the result independently (A2 addendum §2.1) |
| privacy | **PC-PRIV-19** (A3-PRIV-D4) | Split result. The source elements are **PASS**: the log is created from the raw wizard fields, and the masker requires exactly two "@"-split parts. The display-name element ("a quoted display name containing '@' passes validation") is **INCONCLUSIVE (static)**, because it depends on the standard-library parser version. It is to be settled by runtime PC-PRIV-07 |
| privacy | §6 proposal PC-PRIV-23 | Now predeclared (section 5) |
| utm | PC-UTM-18 (D-UTM-A3-01) | Retained as declared, and still NOT-EXECUTED. It is superseded for consumption by **PC-UTM-18R** (encoding and cookie check) |
| onboarding | **PC-ONBD-05** (A3-ONBD-05, D-ONBD-A3-4) | Recorded **PASS → FAIL** against the literal predeclared predicate (section 4 re-execution: 5 elevation constructs, all in `tests/`). The parent result note "no elevation in module runtime code" and its scope narrowing are tagged **`POST-DECLARATION`**. The runtime-scope question is answered by the newly predeclared PC-ONBD-05R (PASS) |
| onboarding | PC-ONBD-15 | INCONCLUSIVE stands. The widened bounded search PC-ONBD-20 is also INCONCLUSIVE |
| web_hierarchy | PC-WHIR-09 citation (D-WHIR-A3-4) | "`models/models.py` L22–24" for the search call is replaced by "L22". L23–24 is the multi-match branch and contains no search. The verdict is unchanged (non-material) |
| web_hierarchy | PC-WHIR-11 predicate note | "Duplicates possible" holds only through the L20 concatenation (a self-parent). The L22 search excludes ids already present. Verdict unchanged |
| web_unsplash | PC-UNSP-08, PC-UNSP-26 step text "(mock-resolved)"; PC-UNSP-10 step text "(mock)"; parent §6 runtime-pack text | Tagged **`POST-DECLARATION`** (absent from `predeclared_proof_cases.tsv` sha256 `2203bab7…f307`). They are superseded for PC-UNSP-08/26 by the predeclared PC-UNSP-08R/26R and the pack amendment in 5.1 |
| web_unsplash | PC-UNSP-07 predicate note | The trailing "/" after both allowed hosts pins the host at parse level, so the only route off the allow-listed host is a redirect served by that host. Verdict unchanged |
| onboarding, html_builder, web_hierarchy, web_unsplash | Parent Proof headers lack a REC sha256 (D-*-A3-3; D-HBLD-A3-1) | **Header erratum:** the REC input for these four parent Proofs is now recorded in section 1 as the frozen parent REC sha256 values. For html_builder, the parent Proof may have been produced while the earlier REC version (`0fd609ab…`, commit `b31a0e8`) was current. The only difference between the versions is a one-line freeze-hash abbreviation (per A3), and no Proof case depends on that line. The parent results are unchanged |

## 7. Effect on REC items

| REC item | Effect of Proof R1 |
|---|---|
| REC-PHON-21, REC-PHON-ST1 | The static basis for the removal direction and the absent-entry branch is confirmed (PC-PHON-30 PASS). The item stays **UPP**. Runtime PC-PHON-01 and PC-PHON-28R are pending |
| REC-PHON-17, REC-PHON-H3 (GAP-PHON-02) | Caller elevation is established statically: the standard portal flow calls the hook elevated, so the list add is not blocked by the system-only list ACL (PC-PHON-29). As a static forecast, not a verdict, the "access error rolls back" branch of PR-PHON-09 is not expected in the standard flow. Runtime PC-PHON-09 is pending. The class stays UPP |
| REC-PHON-30 (GAP-PHON-10) | Unchanged. SMS and marketing callers were not read |
| REC-PRIV-19, REC-PRIV-BR2 | The corrected wording is confirmed (PC-PRIV-24). Runtime PC-PRIV-02 and PC-PRIV-23 are pending |
| REC-UTM-19 | The in-module transport has no escaping (PC-UTM-25). Library decoding was not read. PC-UTM-18R is pending |
| REC-UTM-30 | Static basis confirmed (PC-UTM-26). UPP pending PC-UTM-27 |
| REC-UTM-EX4 | CONTRADICTION stands on source (REC re-read). Runtime PC-UTM-28 is pending |
| REC-ONBD-15, REC-ONBD-BR7 | Runtime code has zero elevation (PC-ONBD-05R PASS). The literal PC-ONBD-05 FAIL is recorded. UPP pending runtime PC-ONBD-06 (PR-ONBD-03) |
| REC-ONBD-H3, REC-ONBD-G1 | INCONCLUSIVE (PC-ONBD-20). GAP stays open |
| REC-UNSP-ST1, REC-UNSP-21 | The static basis supports A2 OM-U02 for an **absent** value: the stored credential is removed, so the A1 state line "no revocation state" is contradicted at source for that branch. An empty-string value blanks the credential without removing it (PC-UNSP-27 PARTIAL). The class stays UPP until runtime PC-UNSP-24, which shows what the client actually sends |
| REC-UNSP-BR5(b), REC-UNSP-G5 | Not closable by any case in this pack (non-substitution, 5.1) |
| All other REC items | Unchanged. No UPP item is closed, because no runtime was executed |

## 8. Totals

| Set | Executed | PASS | FAIL | PARTIAL | INCONCLUSIVE | RECORDED | NOT-EXECUTED |
|---|---|---|---|---|---|---|---|
| R1 static (section 4) | 9 | 5 | 1 | 1 | 1 | 1 | 0 |
| R1 runtime (section 5) | 0 | 0 | 0 | 0 | 0 | 0 | 7 |
| Parent result corrections (section 6) | — | — | +1 (PC-ONBD-05) | +1 (PC-PHON-23) | +1 element (PC-PRIV-19 display-name) | — | — |

## 9. Process-rule compliance (C1B systemic findings 1–5)

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Preserve A2 MRRP labels | **MET**. Proof R1 re-labels nothing. Its REC input carries the restored labels (REC addendum §9 row 1: 45 items, including onboarding C11/C17, web_hierarchy C10 and web_unsplash C12) | REC addendum |
| 2 | Tag post-predeclaration text `POST-DECLARATION` | **MET**. Every Expected, predicate or method text added after a predeclaration is tagged: PC-PRIV-12 method, the PC-ONBD-05 scope note, and the PC-UNSP-08/10/26 "(mock…)" additions and parent §6 pack. All R1 cases were predeclared before execution, and no R1 expected or fail text was changed afterwards. Results that differ from expectation are recorded as FAIL or PARTIAL (PC-ONBD-05, PC-UNSP-27) | Sections 4, 6 |
| 3 | REC scans all A1 item classes | **MET (consumed)**. The REC addendum reconciles BR, states, exceptions, handoffs, gaps, contradictions and CRQs for all seven modules. Proof links in section 7 target those rows | REC addendum §§1.4–7.2 |
| 4 | Order A2 → REC (sha256) → Proof predeclare → execute; the Proof header records the REC sha256 | **MET**. 15:42:01Z → 15:48:54Z → 15:49:57Z → fetch at 15:50:09Z → execution at 15:50:55Z. The header records REC addendum `c77ed8a0…9f6b` and all seven parent REC sha256 values. The four UI-module parent Proof headers get an erratum (section 6) | Sections 1, 2 |
| 5 | Predeclared cases hashed and UTC-stamped before the first Proof source fetch | **MET**. The hash and UTC stamp were written at 15:49:57.247Z. The first Proof R1 file was written at 15:50:10.512Z into a folder that did not exist before. The earlier A2/REC source reads are disclosed (section 2) | `predeclared_R1.sha256`, `predeclared_R1.ts`, `proof_blob_log.txt` |

## 10. Limitations

- No runtime was executed and no runtime result is claimed. Every UPP item remains open.
- The time-stamp evidence rests on self-written scratch files and file mtimes, not on a committed record (the same limitation A3 noted for the parents). No git operations were run.
- The following were not read: request-layer URL decoding and cookie encoding (utm); SMS and marketing callers (phone GAP-PHON-10); controllers of `onboarding` dependents other than `account` and `payment`; the `html_editor` attachment helper and core serving protection (web_unsplash); ORM recompute language semantics (utm O9).
- The bounded searches (PC-ONBD-20) have no listing API, and no file was fetched by a guessed name beyond the import lines.
- No percentages. No Formal Coverage claim. No QID answered.
