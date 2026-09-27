# G01 PLATFORM_BASE — RED TEAM Proof Addendum R1 (A3 remediation, batch B3A) — `auth_signup`, `base_setup`, `base`, `portal`, `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF**. This is an addendum only. No parent Proof package or earlier Proof addendum was edited |
| Group / Modules | G01 PLATFORM_BASE / `auth_signup`, `base_setup`, `base`, `portal`, `base_automation` |
| Date | 2026-09-27 |
| **REC consumed (rule 4)** | `G01_RECONCILIATION/G01_B3A_REC_ADDENDUM_R1_20260927.md`, sha256 **`44deb36d461c391c7f10d5602e5f26d3727cec7397ae7ee981f6dec341810fdd`**, frozen and hashed 2026-09-27T15:45:45Z (scratch `remed_b3a/rec_addendum.sha256`) — **before** this Proof's predeclaration. The same hash is written into the predeclared cases file |
| A2 consumed | `G01_A2_REVIEWS/G01_B3A_A2_ADDENDUM_R1_20260927.md`, sha256 `26d828ce29c78dd5e8da310f93322a2a3d4e1e8debc2cf4617eb403fa86a0c8c` (frozen 15:43:10Z) |
| **Predeclaration (rule 5)** | Scratch `remed_b3a/proof_b3a_cases_predeclared.txt`, sha256 **`6b7a9777ed0bfb50cbeb1f502f23c9f70133767c4240f5838f814b4a3033b1ba`**, timestamp file `proof_b3a_predeclared.timestamp` = **2026-09-27T15:46:33.446Z**, file set read-only. The Proof fetch folder `remed_b3a/src_proof/` did not exist at that moment |
| Proof source fetch | First Proof fetch started **after** the predeclaration: `fetch_start` = **2026-09-27T15:46:44.929Z** in `remed_b3a/proof_exec_log.txt` (11 s after the predeclaration stamp); static execution 15:47:21–15:47:51 UTC. Execution log sha256 `1fffef8ef4462b8d1d1ba0c1738726b4f6ba501d2429b727b7ed778bca409cfe` |
| Stage order achieved | A2 addendum (15:43:10Z) → REC addendum hashed (15:45:45Z) → Proof predeclared and hashed (15:46:33Z) → Proof fetch and execution (from 15:46:44.929Z) |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`; every file checked with `git hash-object` (section 2) |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE**. Probe 2026-09-27T15:47:51Z: `getent hosts` rc=2; HTTP probe to port 8069 → curl rc=6 (could not resolve host) |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** (Proof disposition for every module remains PARTIAL: source/config executed, runtime pending) |

### 0.1 Parent artifacts (sha256; unchanged)

| Parent Proof | sha256 |
|---|---|
| `G01_PROOF/G01_AUTH_SIGNUP_PROOF_20260927.md` | `deee3cf05169f7073ade39593a98b3b62d1899c912fa33a57b4bdb90504d0caf` |
| `G01_PROOF/G01_BASE_SETUP_PROOF_20260927.md` | `c9f0c353ca9cda7d40e840385d59dd64b72260a706d8926cba4a8e240e506faf` |
| `G01_PROOF/G01_BASE_PROOF_20260927.md` | `49e96bcfd16a1098b64aae6ad6d169aa676227d02ee14dd29af4d36ec38618e6` |
| `G01_PROOF/G01_PORTAL_PROOF_20260927.md` | `09190a38d42cd41631374925c12449a549d3c1450525218619da05bcb8dbd49a` |
| `G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md` | `d3d3ad25a58a74c96b1aa7ee81eaf1760b2066add79163807984f77534867aff` |
| `G01_PROOF/G01_BASE_AUTOMATION_PROOF_ADDENDUM_R1_20260927.md` | `091359539b2648a2a1ffa886188dd9c9d9a40dfe7b43d56ddbac5473ebf21e39` |

### 0.2 A3 reports and challenge IDs addressed (Proof part)

| A3 report | sha256 | IDs |
|---|---|---|
| `G01_A3_CHALLENGES/G01_AUTH_SIGNUP_A3_STATIC_20260927.md` | `44eddb06aca5f049181dc083db8b2b8f3c8092428c9573c4054357601b5db48e` | CH-06 / D-ASGN-A3-01; CH-08, CH-11 / D-ASGN-A3-02 |
| `G01_A3_CHALLENGES/G01_BASE_SETUP_A3_STATIC_20260927.md` | `673c4f572f5f96bda52672339efcf22d0d067ce3321ef6f8b32c2e41e308bd17` | CH-02 / D-BSET-A3-01, -02; CH-04, CH-07 / D-BSET-A3-03; CH-06 / D-BSET-A3-04 |
| `G01_A3_CHALLENGES/G01_BASE_A3_STATIC_20260927.md` | `79f442833b0a838524ad8d0f957436b307c7908e8d8468e70a31c20318cd5f01` | D1, D3; D4 (via base_automation) |
| `G01_A3_CHALLENGES/G01_PORTAL_A3_STATIC_20260927.md` | `3ecf4c6ba5dd07949f9d4b1d6074a2f3f46dfe5f28e303ee9fe9d9657d36d370` | CH-P2 / D-PRTL-A3-01; CH-P7 / D-PRTL-A3-02 |
| `G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_RECHECK_R1_20260927.md` | `f8868ca59b03e6ca41dd4481ef34e653676af53251b1757ef3cecfc56b99eefe` | RD-1, RD-2, RD-3, RD-4, RD-5 (Proof part) |

Not addressed here (owner is not a stage this batch acts for): D-ASGN-A3-04, D-BSET-A3-05, base D2, D-PRTL-A3-03 (Integration Control commit-subject errata). No git operation was performed.

**Independence and blindness disclosure.** The same controller wrote the A2 and REC addenda of this batch and did the A2 source re-read before predeclaring. The predeclared expectations are therefore **not blind** to source. They are falsifiable re-reads; A3 should weigh them as such.

Clean-room note: neutral paraphrase only; identifiers and line numbers are pointers. No vendor code is reproduced. Scratch logs contain raw grep output and must not be promoted into governed artifacts. No percentages. No Formal Coverage claim. No QID answered. No git operations. No existing artifact was edited.

### 0.3 MASTER C1-B process-rule compliance (this addendum)

| Rule | Compliance | Evidence |
|---|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` | **MET**. Every new runtime case lists its A2 label; no Proof text reclassifies a label | Section 4 |
| 2. Post-declaration text tagged `POST-DECLARATION` | **MET**. Every observation not in the predeclared file is tagged. Retro-tags are applied to the parent defects A3 named (base_setup PC-BSET-03/07 evidence; base_automation PC-12R1 and PC-64) | Sections 3.x "POST-DECLARATION", 5 |
| 3. REC scans all A1 classes | **NOT APPLICABLE** (REC duty; met in the REC addendum §4) | — |
| 4. REC hashed before Proof; Proof header records REC hash | **MET**. REC hash `44deb36d…0fdd` at 15:45:45Z; predeclaration 15:46:33Z; execution after | Header |
| 5. Cases sha256 + UTC before the first Proof source fetch | **MET**. Predeclared file hashed and timestamped at 15:46:33Z; the Proof fetch folder was created afterwards; all Proof-stage fetch times follow | Header; exec log |

---

## 1. Supersede map

| Old case | New case | Reason | Old status |
|---|---|---|---|
| PC-BSET-18 (runtime) | **PC-BSET-18R1** | D-BSET-A3-02: add demoted-owner variant (PR-BSET-12) | SUPERSEDED (never run) |
| PC-BSET-23 (runtime, optional) | **PC-BSET-23R1** (required) | D-BSET-A3-03 | SUPERSEDED (never run) |
| PC-PRTL-17 (runtime; with parent R1 extension) | **PC-PRTL-17R1** | D-PRTL-A3-01: R1 extension could not run as written | SUPERSEDED (never run). The parent R1 extension text is **withdrawn** |
| PC-PRTL-18 (runtime; record-only) | **PC-PRTL-18R1** | D-PRTL-A3-02: must be able to fail | SUPERSEDED (never run) |
| PC-BAUT-64 (runtime) | **PC-BAUT-64R1** | RD-1 (and RD-4 restoration) | SUPERSEDED (never run) |
| PC-BAUT-65 (runtime) | **PC-BAUT-65R1** | RD-2 (persistent starvation) | SUPERSEDED (never run) |
| — | New static: PC-ASGN-34..36, PC-BSET-29..30, PC-BASE-48, PC-PRTL-23..24, PC-BAUT-66..69 | See section 3 | — |
| — | New runtime: PC-ASGN-37..38, PC-BAUT-70..71 | See section 4 | — |

## 2. Blob verification (Proof-stage fetch, executed)

Every file shared with the A2-stage fetch has an identical blob (compared line by line in the log). Proof-only reads:

| Path | Blob | Prior record |
|---|---|---|
| `addons/portal/wizard/portal_share.py` | `b0491d4e3517118f94fa7dc439b46f324bf8f5f3` | equals portal Lane A / A3 |
| `addons/portal/wizard/portal_wizard.py` | `368f4c1d369892aaefb4e16b5632e6e7b3486cc8` | equals portal Lane A / A3 |
| `addons/portal/models/mail_thread.py` | `971d3f790238ae0359f6236fc1a8230b50a97ed0` | equals portal Lane A / A3 |
| `addons/mail/models/mail_thread.py` | `c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374` | new pointer (no prior record here) |
| `addons/hr/models/hr_employee.py` | `f95bb51dcd422dd4d4d49f155312c6318b028389` | new pointer |
| `addons/survey/controllers/main.py` | `7726df42eadaed68874ed8c54ca234846d470141` | new pointer |
| `addons/website_slides/controllers/main.py` | `5f625dfd307065215c0f8b9bd823a99ed3a5458f` | new pointer |
| `addons/website_sale/controllers/main.py` | `3c73577fcbfa66c157c24920c8b5f9ce88621c04` | new pointer |
| Shared with A2 fetch (all MATCH): `odoo/service/db.py` `63c314a7…`; `ir_config_parameter.py` `21c82bf6…`; auth_signup `res_partner.py` `02aab000…`, `res_users.py` `1a0280b8…`; core `res_users.py` `9d42d77a…`; portal key-description `44c0008f…`; base_setup settings `7de29781…`, kpi `69c9c21c…`; core `res_config.py` `50464416…`; `odoo/orm/models.py` `11f50c4e…`; portal controller `e6b03c24…`; sale portal `181e7214…`; base_automation model `099ba2e3…`, ACL `77253ff3…`; `ir_cron.py` `e8762b92…`; `ir_actions.py` `45d06ee4…` | | |

---

## 3. Static cases — executed (predeclared expected / fail in substance)

### 3.1 `auth_signup`

| Case | Links | Expected | Fail condition | Actual (paraphrased; file lines) | Result |
|---|---|---|---|---|---|
| PC-ASGN-34 | REC-ASGN-28, O4-R1 | Duplicate and copy-flagged restore force default-parameter re-init incl. a new secret and a local base URL; non-copy restore does not | Either path absent; non-copy restore regenerates; secret not in forced defaults | Duplicate forces the re-init unconditionally after the copy (db service L185, L208). Restore forces it only inside the copy branch (L334, L380-382). The defaults table contains a random-UUID secret and a local-host base URL (config-parameter L19, L22) | **PASS** |
| PC-ASGN-35 | REC-ASGN-18, C18-R1 | No rights check for a userless partner on either builder; token only with a type; sign-up type prepared elevated under the signup-valid context | A check that applies to userless partners; token without a type | The single entry's two write checks are each conditioned on another internal or portal user existing (partner model L33, L35). The multi builder has none. The only other guard in the file protects the auth-param helper (L96). Preparation under the signup-valid context applies only to partners with no user (L46); the token is added only inside the typed branch (L58) | **PASS** |
| PC-ASGN-36 | PR-ASGN-14, REC-ASGN-18 | At least one call site outside auth_signup reaches a builder without checking the acting user's write rights on the target partner | None outside auth_signup, or all check | Call sites at the anchor: **(1)** portal share wizard, sign-up branch (portal_share L78-84, chosen by send when B2C is on and the record has no token, L98-108): for recipients with no user, calls the auth-param helper (internal-or-admin gate) then the multi builder; no write check on the recipient partner. **(2)** survey controller error path for the survey start route (public route L209; L124-141): for an answer partner without users on a survey that allows sign-up, prepares a sign-up type elevated and builds a link that is rendered to the holder of the answer token. **(3)** website_slides invite and identify routes (public; L803, L845-850, L857-870): for a partner without a user, prepares elevated and redirects the visitor holding a valid invite hash to a sign-up link. **(4)** portal grant wizard (L161, L229) and auth_signup users (L165) only prepare the type; the link is built by their templates (templates not read). **Not present at the anchor:** the default-branch index candidates hr employee and website_sale have no call to either builder; mail thread has none | **PASS** |

POST-DECLARATION observations (PC-ASGN-36; carry no PASS/FAIL): the survey and slides flows authorise by possession of an answer token or an invite hash rather than by the acting user's rights, so the sign-up link reaches whoever holds that token or hash. The share-wizard flow requires an internal caller with wizard access and read on the record. Template-side link construction for the grant wizard and for auth_signup invites was not read.

### 3.2 `base_setup`

| Case | Links | Expected | Fail condition | Actual | Result |
|---|---|---|---|---|---|
| PC-BSET-29 | REC-BSET-15/26, F1-R1 | No key removal/disable on group, user-type or share change; removal only by share-only self-deletion, expiry clean-up or revoke; allow-keys parameter only in the wizard creation gate; programmatic path skips that gate; key check has no share/group term | Any key removal on such change; share/group term in check; parameter consulted at verification | Core users write (L596-640) has no key reference. Key removals: self-deletion (L967, reachable only by share users, L944-950), the key record's own remove (L1558), programmatic revoke (L1710), expiry clean-up (L1715-1722). The parameter appears only in the portal override of the wizard gate (portal key-description L15). The wizard calls the gate (core L1817, L1834-1836); the programmatic generator does not (L1636-1690). The key check joins only owner-active, scope and expiry terms (L1725-1752). KPI verifies with remote-call scope (kpi L102) | **PASS** |
| PC-BSET-30 | REC-BSET-12, PR-BSET-06R1 | Counter non-stored, elevated, no explicit active term; save/execute disable archive filtering | Stored; explicit active term; neither path disables | Counter declared computed and non-stored (settings L40); elevated count on the share flag only (L105-108). Core settings paths switch archive filtering off (res_config L302, L370) | **PASS** |

### 3.3 `base`

| Case | Links | Expected | Fail condition | Actual | Result |
|---|---|---|---|---|---|
| PC-BASE-48 | D3, REC-BASE-51 | Company-consistency check has no superuser short-circuit; opt-in by model and field flag | A superuser guard skips it | No superuser test in the check routine (orm models L4015-4105, zero occurrences). Called after create and write only when the model flag is set (L4522, L4749; default off, L451); fields collected only if flagged (L4032-4040) | **PASS** |

### 3.4 `portal`

| Case | Links | Expected | Fail condition | Actual | Result |
|---|---|---|---|---|---|
| PC-PRTL-23 | REC-PRTL-01/21, O2-R1 | Pager: neighbours from the given record's environment, no read check, tokens ensured; page-values passes the gate result; gate returns a superuser-bound record; history from server session; filling list routes require login and store own ids | Read check in pager; caller-env record from gate; history from request input; public list routes | Pager has no access check (controller L96-121, zero occurrences) and ensures tokens for both neighbours (L104, L111). The gate returns the record bound to the superuser account (L972). History is read from the session (L1014) and passed with the document (L1015). Sale list routes are login-only and store the user's own result ids (sale portal L106-115) | **PASS** |
| PC-PRTL-24 | REC-PRTL-04/22, PR-P5R1 | Gate: existence, caller read, then token; no active/company/state filter; sale document route redirects only when the gate raises | Any such filter before rendering | No active, company or state term in the gate (L961-980, zero occurrences). The sale document route catches only access and missing-record errors from the gate (sale portal L137-140) | **PASS** |

### 3.5 `base_automation`

| Case | Links | Expected | Fail condition | Actual | Result |
|---|---|---|---|---|---|
| PC-BAUT-66 | REC-BAUT-11/38, RD-1 | Initial rule search and last-run write unelevated; single settings-group ACL row; ORM search checks model read for non-superuser | Elevation on the search; another ACL row; no ORM check | Rule search runs in the processor's own environment (module L1191); no elevation call anywhere in the processor (L1184-1220, zero). ACL file: header plus one row (settings group). ORM search checks model read access unless superuser or bypass (orm models L5364-5366) | **PASS** |
| PC-BAUT-67 | REC-BAUT-47, RD-2 | Rule search, active check (missing-record guard only), selection, last-run write and progress commit outside isolation; no ordering attribute on the rule model; ORM default order by id | Any inside isolation; ordering attribute declared | Active check guarded only against a missing record (L1196-1200); selection at L1203 precedes the isolation block (L1205-1212); last-run write and progress commit follow it (L1214-1216). No ordering attribute in the module model (zero). ORM default ordering is the id (orm models L434) | **PASS** |
| PC-BAUT-68 | REC-BAUT-27, RD-3 | FAILED without execution after ≥3 consecutive timeouts with no done count; job-update routine returns silently on lock failure and activates only with an active time rule | Otherwise | Scheduler: timed-out counter at or above the constant (3, L35) and no done count → FAILED without running the job (L429-443). Module job-update: lock failure returns (L672-675); active set to whether any active time rule exists (L676-678) | **PASS** |
| PC-BAUT-69 | REC-BAUT-48, O19, D4 | Group test against the environment user, not skipped under elevation; model/record checks skipped under elevation | Group test skipped under elevation | The gate reads the action's groups elevated and compares them with the environment user's groups, with no superuser exemption (ir_actions L1215-1222). The model and record write checks use the ORM check, which short-circuits under superuser mode (orm models L4120) | **PASS** |

**Static totals (this addendum): 12 executed — PASS 12, FAIL 0.** No failed static result to preserve.

---

## 4. Runtime cases — NOT-EXECUTED (device offline; ready to run; no result claimed)

Common preconditions as in each parent Proof. All carry A2 label **MISSING_REQUIRED_RUNTIME_PROOF**.

| Case | Links | Steps (from A2 addendum B3A §7, unchanged in substance) | Expected | Fail condition | Status |
|---|---|---|---|---|---|
| PC-ASGN-37 | PR-ASGN-13; REC-ASGN-28; Q032, Q036 | Reset link issued on D; copies (a) platform duplicate, (b) restore not flagged as copy, (c) external dump and reload; present link to D and each copy; record the base URL of a new link in each copy | D accepts; (a) rejects; (b) and (c) accept | (a) accepted, or (b)/(c) rejected | NOT-EXECUTED |
| PC-ASGN-38 | PR-ASGN-15; REC-ASGN-18; Q009 | Non-manager internal user drives the share-wizard sign-up flow (B2C on, record without token) for (i) a userless partner, (ii) a partner of another internal user, (iii) a partner with a portal user; separately, an anonymous holder of a survey answer token and of a slides invite hash drives flows (2) and (3) of PC-ASGN-36 for a userless partner. Test whether each issued link verifies | (i) and the anonymous flows: a verifying sign-up link is issued; (ii)/(iii) the share wizard skips them (it targets only userless recipients) | (i) or an anonymous flow: access error or no verifying link; (ii)/(iii) a sign-up link issued to a partner that has a user | NOT-EXECUTED |
| PC-BSET-18R1 | PR-BSET-01 + PR-BSET-12; REC-BSET-15/26 | Parent steps (internal-user key; portal key with portal keys enabled), **plus** variant: portal installed, allow-keys absent; internal U creates an unscoped key; admin changes U to portal; confirm key exists; call KPI; repeat with portal not installed | Roster returned in every step and variant; key present after demotion | Key removed by demotion, or request rejected / roster omitted for an unexpired key | NOT-EXECUTED |
| PC-BSET-23R1 | PR-BSET-06R1; REC-BSET-12 | With archived internal users: counter on form load, counter right after a save, dashboard active count | All equal | Any differs (record which) | NOT-EXECUTED |
| PC-PRTL-17R1 | PR-P4 + PR-P4R1; REC-PRTL-01/21 | Parent PR-P4 steps unchanged; **plus** stale history: portal user P lists D1-D3, loses read on D1 and D3 (tokens cleared in one variant), opens D2 in the same session | PR-P4: access error, no token. Stale history: neighbour links for D1/D3 render with tokens; cleared variant writes new tokens | PR-P4: token written or URL returned. Stale history: no neighbour link renders, page errors, or no token written in the cleared variant | NOT-EXECUTED |
| PC-PRTL-18R1 | PR-P5R1; REC-PRTL-04/22 | Without login, open by token through a gate-using route: (a) cancelled-state document (sale order route); (b) document of another company; (c) archived document where a portal model with an active flag exists | Each renders | Any refused by gate or route (redirect, not-found, access error) | NOT-EXECUTED |
| PC-BAUT-64R1 | PR-29R1; REC-BAUT-11/38 | Variants (i) default job user, (ii-a) settings-group U with a record rule hiding X2, (ii-b) non-settings V | (i) X1, X2 stamped, uid superuser account, **flag set**; (ii-a) only X1, uid U, flag set in the action; (ii-b) FAILED at rule lookup, nothing stamped, last-run unchanged, counter +1 | (ii-a) X2 stamped, uid not U, **or flag not set in the action**; (ii-b) any stamp or run not FAILED | NOT-EXECUTED |
| PC-BAUT-65R1 | PR-30R1; REC-BAUT-47 | Lower-id rule's condition raises; higher-id healthy rule; run three times | Every run FAILED; healthy rule never processed; its last-run unchanged | Healthy rule processed in any run | NOT-EXECUTED |
| PC-BAUT-70 | PR-31; REC-BAUT-27 | (a) three consecutive worker timeouts then a fourth start; (b) lock the job row, write a critical rule field while the job is inactive | (a) fourth start FAILED without executing, counter +1; (b) job stays inactive | (a) executes or not FAILED; (b) job becomes active | NOT-EXECUTED |
| PC-BAUT-71 | PR-32; REC-BAUT-48; base PC-BASE-07/10 | On-save rule on X whose action carries group K; U (write on X, not in K) edits X; variant without K | U's edit fails with an access error, action not run; variant: action runs, flag set, uid U | Main: edit succeeds with action run or skipped silently; variant: access error | NOT-EXECUTED |

**Runtime totals (this addendum): 10 active cases — NOT-EXECUTED 10, PASS 0, FAIL 0.**

---

## 5. Corrections to parent Proof records (tagged; no parent file edited)

### 5.1 `base_setup`

- **Parent refinement R2 is WITHDRAWN** (D-BSET-A3-01). Replacement text, POST-DECLARATION relative to the parent predeclaration `97055575…ec01f`: "Portal-held keys reach the KPI roster independently of the portal allow-keys parameter whenever the key was created while its owner was internal, by server code, or through the programmatic path; the parameter governs only wizard creation (PC-BSET-29)." The parent PC-BSET-07 PASS stands on its predeclared expected/fail pair (A3 CH-07).
- **Retro-tag (D-BSET-A3-04):** in the parent, the portal key-description read (15:05:59–15:06:00Z) used in PC-BSET-07 and the core field-definition read (15:07:27Z) used in PC-BSET-03 are **POST-DECLARATION evidence** added after the predeclaration stamp 15:04:44Z. They extend evidence without changing the expectation.
- **PC-BSET-12 fail-condition weakness (D-BSET-A3-03):** recorded. The save-path context is now covered by static PC-BSET-30 and required runtime PC-BSET-23R1. The parent PASS is kept for the form-load path only.

### 5.2 `base`

- **D1 — REC hash the parent Proof consumed:** the parent Proof used `G01_RECONCILIATION/G01_BASE_REC_20260927.md`, whose sha256 at A3 intake was `c343d43408c57b7e6cc75a3b9d5edf85737281dc9e5bda71a732762a567b833c`. The parent header did not record it; it is recorded here. Because REC was finalised in the same run after Proof static execution (REC addendum B3A §2), this hash identifies the REC version A3 reviewed, **not** a REC frozen before that Proof ran.
- **D1 — change note:** the parent Proof was committed in `6d55fdb` and changed in `0eaeb25` (per A3): one cosmetic line in section 5, runtime list "PC-06..12, 16, 17" → "PC-06..12, PC-17". No verdict changed. Recorded here as the missing change note (no git operation performed by this stage).
- **D3 — corrected S1 bullet of the parent section 6 design note** (POST-DECLARATION; replaces the sentence "It is bypassed by any elevated execution (PC-24)"): "Record rules and company-context checks are bypassed by elevated execution (PC-24). The opt-in company-consistency check on flagged relational fields is **not** bypassed: it still refuses cross-company links for opted-in models under elevation (PC-38, R4, PC-BASE-48). Models that do not opt in get no such check." The implication sentence is unchanged, except that "or on the absence of elevation" should read "or on the absence of elevation for record visibility".

Base totals after this addendum: 48 active — PASS 27, FAIL 0, NOT-EXECUTED 21.

### 5.3 `portal`

- **Parent R1 severity basis restated** (POST-DECLARATION; D-PRTL-A3-01): the pager site is **stronger** than stated — it runs on the superuser-bound handle and bypasses implicit read enforcement too (PC-PRTL-23) — but its **reach is narrower**: ids come only from the caller's own session history, filled by login-required list routes. Exposure is stale history after access loss in the same session. The parent sentence "with a crafted or previous session history" is withdrawn.
- PC-PRTL-18R1 now has a falsifiable fail condition (D-PRTL-A3-02).

Portal totals: 24 active — PASS 14, FAIL 1 (parent PC-PRTL-01, preserved), NOT-EXECUTED 9.

### 5.4 `base_automation`

- **RD-4 retro-tags on the Proof addendum R1 (`09135953…1e39`):**
  - PC-BAUT-12R1: the step "Then write a delay-range field on a rule" and the expectation "The job re-activates after the rule write" are **POST-DECLARATION** (absent from predeclared file `531f5951…456d`, which only said the job re-activates "only after" a create/delete/critical-or-range write or manual edit). They are kept as tagged additions; the predeclared fail list is unchanged.
  - PC-BAUT-64: the predeclared fail element "flag not set in the action" and the expected "flag set" in step (i) were dropped without a tag. They are **restored** in PC-BAUT-64R1 (section 4). PC-BAUT-64 itself is superseded.
- **D4 — correction to parent Proof refinement R4 / PC-BAUT-40 wording** (POST-DECLARATION): "The per-action gate runs in the elevated environment; it does not restrict rule-triggered actions **that carry no groups**. For actions that carry groups, the group test still uses the real user's groups and raises for users outside them (PC-BAUT-69; base PC-BASE-32), which can block the triggering user's own edit (PC-BAUT-71)." The parent PC-BAUT-40 PASS stands for elevated dispatch (as already limited by PC-BAUT-40R1).
- **RD-5 — stage-order disclosure for addendum R1:** the A2 addendum R1 (created 15:18:33Z) and REC addendum R1 (created 15:19:43Z) both post-date the Proof addendum R1 predeclaration (15:17:13Z) and its execution start (15:17:31Z). The Proof addendum R1 header lists them as "inputs"; they should be read as **records written after execution**, not inputs that execution consumed. This batch followed the required order (header).

base_automation totals: 71 active — static PASS 39, FAIL 0; runtime/config NOT-EXECUTED 32. Superseded and retained for lineage: 7 (PC-12, 13, 40, 42, 49, 64, 65).

### 5.5 Module totals after this addendum

| Module | Active cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| auth_signup | 38 (parent 33 + 3 static + 2 runtime) | 24 | 0 | 14 |
| base_setup | 30 (parent 28 + 2 static; 2 runtime superseded one-for-one) | 19 | 0 | 11 |
| base | 48 (parent 47 + 1 static) | 27 | 0 | 21 |
| portal | 24 (parent 22 + 2 static; 2 runtime superseded one-for-one) | 14 | 1 | 9 |
| base_automation | 71 (after R1: 65 + 4 static + 2 runtime; 2 superseded one-for-one) | 39 | 0 | 32 |

REC effect: no class change by Proof. All UNKNOWN_PENDING_PROOF items and the runtime effect of every CONTRADICTION item remain open. **Disposition for each module: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.** Eligible for A3 static re-check only; A3 → MASTER full handoff remains not eligible.

## 6. Limitations

- No runtime executed; no runtime result claimed. Static PASS confirms source readings only and never counts for a runtime case.
- PC-ASGN-36 enumerated call sites only in the candidate files named in the predeclaration (from a default-branch index plus the flows A3 named). A caller that exists only at the anchor and in other files would be missed; mail and auth_signup template-side link construction was not read.
- The predeclared expectations are not blind (same controller did the A2 re-read); timing rests on scratch files and timestamps that are not externally anchored.
- Integration Control items (commit-subject errata) are outside this batch's stages and remain open.
- No percentages. No Formal Coverage claim. No git operations. No existing file was edited. Source copies are in scratchpad `remed_b3a/src_proof/` only.
