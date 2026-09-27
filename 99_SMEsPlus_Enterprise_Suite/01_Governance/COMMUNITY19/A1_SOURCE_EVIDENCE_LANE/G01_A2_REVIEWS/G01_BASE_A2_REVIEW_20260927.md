# G01 PLATFORM_BASE — RED TEAM A2 Review — `base`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1. The A1 package was not repaired or rewritten |
| Group / Module | G01 PLATFORM_BASE / `base` |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_A1_PACKAGE_20260927.md`, sha256 `a45a2beff88b8be61cd81b6075f7072f156c1b9d1d93029f0afb6ad35a0189e7` |
| Lane A packet (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_LANE_A_PASS1_20260927.md`, sha256 `9108bd4f64762c79f763a35c9d6e944153bd7eec5c0fad3bda9d0eadcd59403b`. This matches the value in the A1 header |
| R14 carry-forward (G01 section) | `A1_SOURCE_EVIDENCE_LANE/G01_G04_RED_TEAM_STATIC_CHECKPOINT_R14_20260925.md`, sha256 `3c3f0bd038fffb2ddf11016c6c25ddcc96066c6124557967b03c0541becdf883`. This matches the value in the A1 header |
| Question bank (topic lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_GMVQ_MVQ_50_V1.00_DRAFT.md`, sha256 `b242fa0e98aeedd12b5ae33aa9800a1831a795222052f87621960d4d9aed8777` (W1-B01, ELIGIBLE). This matches the value in the A1 header. No QID is answered |
| Cross-module source (CRQ-01) | `addons/base_automation/models/base_automation.py` at the anchor, blob `099ba2e3b5352a03fce94aec9f7bdc7219247144`. This matches the base_automation Lane A E4 entry |
| Cross-reference (read-only) | `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_REVIEW_20260927.md`, sha256 `bf95295f2d53891c8358422a8a3b5179e50bc44fa028a8be19be6c2a72bd4208`. It was used only for proof alignment and was not edited |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `odoo/addons/base/` (raw.githubusercontent.com) |
| Predeclared test plan | scratchpad `a2_base/test_plan_predeclared.txt`, sha256 `cc62076dfc4ae7cead4b66a19aa3f8ac0a59aa5fea3428f6ad0a099eab88d784`. It was written 2026-09-27 14:59 UTC, before any source was re-read |
| Lane B | No Lane B runtime evidence exists for this module. This is not treated as a failure (section 7) |
| Date | 2026-09-27 |
| **Disposition** | **A2 PASS WITH FINDINGS — HANDOFF TO REC** |

Disposition reasons:
1. All 36 A1 claims were re-read against source. Results: 30 VERIFIED, 6 PARTIAL (C14, C26, C27, C28, C29, C31), 0 NOT_VERIFIED, 0 OUT_OF_SCOPE. No PARTIAL claim reverses an A1 conclusion, so none requires a return to A1.
2. **CRQ-01 is CLOSED-STATIC** (section 4). A1 left it NARROWED. The cross-module file shows that every place where base_automation invokes server actions hands over an action record that already carries the superuser flag. The runtime effect is still routed to Proof.
3. The main A2 findings are O1 and O2. Both show that the server-action access gate is evaluated on a different record set from the one the action mutates. A1 described the gate as covering "the real target records" and missed this gap. These findings are routed to REC/PROOF. They are not A1 defects that block handoff.
4. The business-meaning review (section 5) finds that A1 reports the multi-company mechanism correctly. However, A1 does not state plainly that the company boundary is not a tenant boundary. The business reading of C11, C12 and O7 must carry that point downstream.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced and nothing is recommended for reuse. No percentages. No Formal Coverage claim. No git operations. Source copies are held only in scratchpad `a2_base/`.

## 1. Test plan (predeclared, executed as declared)

| Test | Scope | Method | Result |
|---|---|---|---|
| T1 Lineage | A1 package, Lane A packet, R14, bank | sha256 of each file, compared with the A1 header | PASS. All three upstream hashes recorded by A1 match |
| T2 Blob integrity | E1, E3, E4, E5, E6, E8, E9, E10, E11, E12, E13, E15, E17, E18, E19, E20, plus the four R14 blobs, plus the base_automation file | Fetched at the anchor; `git hash-object` compared with the recorded SHA-1 | PASS. All 21 blobs match |
| T3 Semantic re-read | All HIGH claims, MED claims C14 and C32, and C36 by pointer | Full read of the rule model and the rule XML. Section reads of the users model (credentials, throttle, identity re-check, API keys, invariants, write, multi-company sync), company (write, archive, branch helper), partner share compute, ACL check, parameter model, server-action run/gate/runners/eval context/warnings, scheduler (acquire, process, run loop, failure count, reschedule, callback, write lock, toggle, version/module-state checks) and HTTP auth methods. Manifest parsed for data order | Done. Verdicts in section 3 |
| T4 Contradiction/CRQ focus | X1–X4; the ten focus topics in the brief | Adversarial re-read, one execution path at a time | Done. Sections 3, 5 and 6 |
| T5 CRQ-01 | base_automation execution paths | Located every server-action invocation and every rule-processing entry point in the file | Done. Section 4 |
| T6 Business semantics | Tenant isolation and privilege model in a multi-company SaaS ERP | Read each claim as a product owner would; searched for overclaims and omissions | Done. Sections 5 and 6 |
| T7 Lane B / Proof | Every claim | Classified NOT_APPLICABLE / UNCORROBORATED / MISSING_REQUIRED_RUNTIME_PROOF; wrote falsifiable proof requirements | Done. Sections 7 and 8 |

## 2. Contradictions X1–X4 (A1 section 8)

| ID | A1 status | A2 result |
|---|---|---|
| X1 | CONFIRMED | **CONFIRMED.** The key-verification helper is defined inside the users model file (E3), so the Lane A G3 gap is superseded. At verification time one database query applies four filters: the owner is active, the key index matches, the scope is empty or equal to the requested scope, and the expiry is empty or not yet passed. The candidate hash is then verified. Expired keys therefore fail at check time, independent of the vacuum. Both the RPC password fallback and the bearer route call the helper with the fixed scope label "rpc" |
| X2 | CONFIRMED refinement | CONFIRMED. The counter reset applies to both fully-done and partially-done outcomes |
| X3 | CONFIRMED refinement | CONFIRMED. The bearer route passes the fixed label, so it accepts both global keys and keys scoped literally to that label |
| X4 | CONFIRMED refinement | CONFIRMED. Without a request object the throttle context yields immediately and records nothing |

## 3. Claim verdict table

Verdict key: VERIFIED = a source re-read supports the claim as written. PARTIAL = the core is supported, but part of the claim is inaccurate or its scope is materially incomplete. NOT_VERIFIED = the source does not support the claim. OUT_OF_SCOPE = the claim cannot be judged within module scope.

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read, paraphrased) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The manifest has category Hidden, auto-install, no dependency key, LGPL-3 and a post-init hook. In the parsed data list, groups and rules sit at positions 10–11, before the first view file, and the ACL list is the final entry of 65. Refinement: the seed data (banks, languages, partners, currencies, main company) loads before the groups |
| C02 | HIGH | VERIFIED | The ACL check returns "allowed" at once in superuser mode. Rule lookup returns an empty set in superuser mode, so the rule computation yields only delegated-parent domains, and those are also empty under superuser |
| C03 | HIGH | VERIFIED | The allowed-model set is the union of rows that are active and grant the mode, with no group or with one of the user's effective groups. It is cached per uid and mode. The cache is cleared on ACL create/write/delete, and on any user write that touches group membership. A group-less granting row logs a deprecation warning at creation |
| C04 | HIGH | VERIFIED | Candidate rules must be active, carry the mode flag, and be global or linked to one of the user's groups. Group rules are filtered again against the user's effective groups. The result is every global domain AND the OR of the applicable group domains. A group rule with no domain counts as "true", so it opens the whole group block for its holders |
| C05 | HIGH | VERIFIED | For each delegated parent whose link field is stored, the parent's computed domain is ANDed in through that link. Refinement: this applies even when the child model has no rules of its own |
| C06 | HIGH / LOW | VERIFIED (inputs) | The evaluation context has three inputs: the user with an empty context, the ids of the current environment's companies, and the current company id. The docstring says the ids are the companies activated through the switcher and that they are "filtered and trusted". The trust property itself is ORM-core behaviour and stays at LOW (G1) |
| C07 | HIGH | VERIFIED | The cache key is uid, superuser flag, model, mode and the raw activated-company context value. It is a tuple, so the order of the ids matters (this is commented in source). Caching is off when the "xml" developer mode is set. Rule create, write and delete flush and clear the registry cache |
| C08 | HIGH | VERIFIED | Diagnostics treat the applicable group rules as one block and test each global rule separately. The info log carries the operation, up to 6 record ids, the uid and the model. See O8 for the debug-mode disclosure that A1 did not cover |
| C09 | HIGH | VERIFIED | Rules may not target the rule model. A database constraint requires at least one mode flag. Active rules with a domain are evaluated and validated against the target model at save |
| C10 | HIGH | VERIFIED | The global rules on partners, partner bank accounts and currency rates use "company is ancestor-or-self of an activated company, or empty". The stated RISK follows: a record owned by a branch is invisible from the parent while only the parent is activated |
| C11 | HIGH | VERIFIED | The global partner rule also admits partners whose "shared" flag is false. A1 gap G5 is settled by source: the stored compute sets the flag false when at least one linked user is internal, and always for the superuser's partner. A partner with no users, or with only portal/public users, is "shared" and falls under company scoping |
| C12 | HIGH | VERIFIED | The four company rules are non-global group rules: internal, portal and public see the activated companies, and the access-rights manager sees all. The users global rule shows internal users always, and share users only when their allowed companies intersect the activated set |
| C13 | HIGH | VERIFIED | The portal/public partner group rule limits reads to the commercial-entity subtree. It carries only the read mode. The portal users rule limits all modes to the same commercial entity. Both AND with the global rules |
| C14 | MED | **PARTIAL** | The helper always walks the branch tree under elevation and intersects it with the activated set. Superuser status only matters on the fallback. When the intersection is empty and the uid is the superuser account (commented as the scheduler case), the helper returns the company itself. A1's "in superuser contexts it walks with elevation" puts the elevation in the wrong place |
| C15 | HIGH | VERIFIED | Four controls hold: the parent link cannot be written after creation, duplication raises, archiving archives direct children (and cascades through their own writes), and a constraint blocks archiving a company that is the default of active users. Root-delegated fields are copied from the root to branches on write, and a constraint requires them to equal the parent's. Setting an inactive currency on a company re-activates that currency |
| C16 | HIGH | VERIFIED | Login uniqueness is a database constraint. The default company must be within the allowed companies (for active users only). The exclusive user-type check runs over effective groups. The at-least-one-administrator check is skipped while `base` itself is being updated. The write guards and the ondelete guards (superuser, admin, portal template, public) are confirmed |
| C17 | HIGH | VERIFIED | Self-edits limited to the self-writeable list run elevated. A default company outside the user's allowed companies is removed from the values without an error |
| C18 | HIGH | VERIFIED | The multi-company group is linked or unlinked from the allowed-company count on create, on write of allowed companies, and in the draft (new) path |
| C19 | HIGH | VERIFIED | PBKDF2-SHA512 with rounds = max(600000, parameter). At init, rows not in modular-crypt format are rehashed. The own-password change and the credential check reject empty values. Own-password change through the admin field raises. Refinement: in the admin set-password path an empty new password is ignored silently, not rejected |
| C20 | HIGH | VERIFIED | The throttle key is the request's remote address. The counter lives on the worker's registry and is used only when a request exists. A cooldown attempt is refused with an error and does not raise the counter. A private-address warning is logged. See O5 for reset-on-success and bearer coverage |
| C21 | HIGH | VERIFIED | The decorator refuses to run without a request. It allows the call if the session's last check was within 10 minutes. Otherwise it returns an identity-check dialog instead of executing |
| C22 | HIGH | VERIFIED | The key is random, and storage keeps a PBKDF2 hash at a low fixed round count plus an 8-hex-character index. Each key is bound to one user and carries an optional scope label |
| C23 | HIGH | VERIFIED | The expiry check is skipped for system users and in superuser mode. Otherwise expiry is required, must be in the future, and is capped by the highest group duration, falling back to 1 day if every duration is zero. The internal group seeds 90. Programmatic generate/revoke requires administrator rights or the enabling parameter. Generate also requires a live key of the same user and a per-user count limit, and it runs inside the login throttle |
| C24 | HIGH | VERIFIED | See X1. Interactive removal requires identity re-check. Removal is allowed only for the owner or a system user, and it clears the cache. The vacuum deletes expired rows. Persistent administrator-created keys never expire |
| C25 | HIGH | VERIFIED | none: the user is cleared. public: the public user is assigned when there is no user. user: the missing user and the public users are refused with session-expired. bearer: a header key is verified; a mismatch with the session user is refused; the session is marked non-savable; with no key, a session user is accepted only with navigation Sec-Fetch headers; the user-level check then follows. CORS preflight authenticates as none. An invalid session is logged out and the request continues with no user. Unexpected exceptions become access denied |
| C26 | HIGH | **PARTIAL** | The two gate branches, the refusal when warnings exist, and the code syntax/safety check at save are all confirmed. Overclaim: the "real target records" the gate checks are the records named by the call context, and only when the context model equals the action's model. They are not the records the action actually mutates. See O1 and O2 |
| C27 | HIGH | **PARTIAL** | Confirmed: code runs with the caller's environment; update/create/duplicate and sequence-valued updates run through the elevated action environment; uid is preserved in the eval context. Inaccurate for multi-action children: model-level and record-level gate checks pass automatically under elevation, but a child's group check still tests the real uid's groups, because elevation keeps the user. Children's code runs elevated. The claim also omits O1 (the mutated records differ from the gated ones) |
| C28 | HIGH | **PARTIAL** | Confirmed: the record is read through the elevated environment; the send is registered post-commit (a rollback only logs and never sends); one-second timeout; failures are logged only. The claim omits a mitigation: a webhook action that includes any field-level group-restricted field gets a warning, and actions with warnings refuse to run. The RISK "fields outside the caller's read rights" therefore narrows to record-rule read asymmetry (see O4) |
| C29 | HIGH | **PARTIAL** | The job environment is built from the job's configured user without an explicit elevation flag, and the server action is run in that environment. Overgeneralisation: seeded jobs have no explicit user and default to the installing account. `base`'s own branch helper comments that the superuser account is the scheduler case (C14). Whether the ORM treats that uid as superuser mode is G1. So "not in superuser mode at entry" holds only for jobs configured with an ordinary user. The job context also carries no activated-company value (see O10) |
| C30 | HIGH | VERIFIED | Acquisition uses row-level no-key-update skip-locked selection. Write and delete take a record lock and refuse while the job is running. A manual run requires write access and refuses if the job cannot be acquired. The ready order is failure count, priority, id |
| C31 | HIGH | **PARTIAL** | Confirmed: 3 timeouts count as one failure without running; deactivation needs at least 5 failures AND more than 7 days, with an admin notification; fully and partially done both reset the counters; the callback rolls back and re-raises (the run loop catches this and classifies it). Inaccurate on two points. (a) The loop continues until both 10 iterations AND 10 seconds are reached, not "at least 10 iterations or 10 seconds". (b) The 5-hour limit applies to modules pending install/upgrade, after which module states are force-reset. A base version mismatch skips the database with no time limit |
| C32 | MED | VERIFIED | The interval is added in the job user's time zone to keep the wall-clock hour. On a neutralized database the whole toggle is skipped |
| C33 | HIGH | VERIFIED | The read-access check happens before the cached lookup (stable cache). Protected keys cannot be renamed or deleted, though their values stay writable. Elevated framework readers bypass the parameter ACL |
| C34 | HIGH | VERIFIED | Scheduler, server-action and parameter rows are for the administrator only. ACL rows, rules, groups, users, companies and models are CRUD for the access-rights manager. Partner CRUD belongs to the contact-creation group. API-key rows are read-only for internal and portal users, with the rule limiting them to their own keys. Public users are denied by rule and have no ACL row |
| C35 | HIGH | VERIFIED | Two daily seeded jobs (vacuum, and portal-user deletion with batch 50). Neither sets an explicit user (see C29) |
| C36 | HIGH (R14) | VERIFIED (by pointer) | All four R14 blobs match. Spot greps confirm: admin-only storage migration and table lock in attachments; plain-text downgrade path; no elevated relational commands and row-locking for gapless sequences; no elevated relational commands and the at-least-one-active check for languages |

Verdict counts: VERIFIED 30, PARTIAL 6, NOT_VERIFIED 0, OUT_OF_SCOPE 0.

### 3b. A1 CRQ candidates — static settlement

| CRQ | A2 static result | Residual proof |
|---|---|---|
| BASE-CRQ-01 | Partly settled. Yes for update-path targets and for create/duplicate targets, because those records are never gated (O1). For the starting record, the gate checks write rules when the context model matches | PR-06, PR-11 |
| BASE-CRQ-02 | Settled statically: children evaluate in an elevated environment, so their code runs in superuser mode. Their group check still applies to the real user | PR-07 |
| BASE-CRQ-03 | Settled statically: yes. There is no record check, and the mutation runs elevated | PR-08 |
| BASE-CRQ-04 | Narrowed. Field-level group-restricted fields are blocked by the warning. Record-rule read asymmetry and related-record ids in relational fields remain possible | PR-09 |
| BASE-CRQ-05 | Open. Cross-worker propagation of registry-cache clearing is outside module scope (G6) | PR-18 |
| BASE-CRQ-06 | Settled at rule-text level (C10) | PR-02 |
| BASE-CRQ-07 | Settled statically: yes. The counter is per worker, a success resets it, non-HTTP calls are exempt, and bearer verification does not use the throttle (O5) | PR-15 |
| BASE-CRQ-08 | Settled statically: yes. Expiry is compared with the current time inside the verification query, so it does not depend on the vacuum | PR-14 |
| BASE-CRQ-09 | Open (concurrency). The locking design is confirmed | PR-16, PR-17 |
| BASE-CRQ-10 | Narrowed. Elevation preserves the uid, so the recorded user is the caller or the job user. Audit-field stamping is ORM core (G1) | PR-06, PR-12 |

## 4. CRQ-01 disposition (base_automation execution identity)

**Result: CLOSED-STATIC.** (A1 left it NARROWED.)

Evidence (base_automation file, blob `099ba2e3…` MATCH):
- The file invokes server actions at exactly two sites. The first is the common per-record processor, which every event, message, time-based and webhook path funnels into. It iterates the rule's action list through an elevated copy of the rule and calls run on each action. The second is the onchange hook, which takes the action list from an elevated copy of the rule and calls run. No invocation of run on a non-elevated action exists in the file.
- When base's run is called on an elevated action, the evaluation environment is elevated, so code actions execute in superuser mode. Model-level and record-level gate checks pass automatically. The group check still tests the real uid's groups, because elevation preserves the uid (C27 refinement).
- The uid in effect depends on the path:
  - event-triggered paths: the triggering environment's uid;
  - time-based paths: the uid of the scheduler job that runs the processor (C29 applies; the job's configured user);
  - webhook path: the uid set by the webhook route, which is outside this file. The base_automation A2 review records it as the public user (its PR-02).

What CLOSED-STATIC means here: the static question (does automation invoke server actions elevated, and does any path invoke them unelevated?) is answered from source. Elevated always; unelevated never. This does not assert a proven privilege escalation. The runtime effect stays a proof requirement (PR-10 here, and base_automation PR-01/PR-02). Side effect worth routing: if an automation's action carries groups, a triggering user outside those groups makes the automation raise an access error. That error can block the user's own business operation (O3).

## 5. Semantic findings (business meaning, multi-company SaaS ERP)

- S1 — The company is not a tenant boundary. In this platform, "company" is a visibility filter inside one database, driven by the user's activated selection. Internal users, their partner records, and every company record visible to an access-rights manager cross company lines by design (C11, C12). A SaaS design that uses the reference's multi-company model as tenant isolation would inherit cross-entity disclosure of staff identities and contact data. A1 states the pieces but does not draw this conclusion. Downstream data/IAM work must treat tenant isolation as a separate, harder boundary.
- S2 — Visibility follows the selection, not the entitlement. Rules evaluate against the activated set (C06). The same user sees different data from moment to moment, and the rule cache is keyed on the raw selection. Correctness depends on ORM-core filtering of that selection against the user's allowed companies (G1). This is the single most important unverified trust assumption for isolation.
- S3 — Hierarchy visibility runs one way. Branches see ancestor-owned shared data. Parents do not see branch-owned shared data unless the branch is activated (C10). For group consolidation this is a functional gap, not a leak. For isolation it is the safer direction.
- S4 — The authorisation gate for server actions checks "can the caller write the record in context". Execution is "superuser mutates what the action is configured to mutate". The two record sets differ in three cases (O1, O2): relational update paths, create/duplicate on another model, and context-model mismatch. The privilege model is therefore configuration-trust: any administrator-authored action becomes a delegated privilege for everyone who passes the gate. A1's BR6 is correct in shape but understates the breadth.
- S5 — Background identity is configured, not derived. Scheduler work runs as whatever user the job names. Seeded jobs name the installing account, and automation actions always run elevated. Audit fields preserve a human-looking uid while effects are unrestricted. For a SaaS audit trail, "who did it" and "under what authority" are separate facts, and the platform records only the first.
- S6 — Credential lifecycle is mostly sound. Keys fail closed at check time on expiry and on inactive owner (X1). Non-admin keys always expire. Remaining concerns are the ones listed in O5/O6: keys are not company-scoped, "scope" is only a label, administrator keys can be persistent, and throttling is per worker.

## 6. Omissions (not in A1)

| ID | Severity | Omission | Evidence pointer | Proof |
|---|---|---|---|---|
| O1 | HIGH | Gate/target mismatch in object actions. (a) An update action with a relational path walks from the context record to related records under elevation and writes those. Only the starting record was gated. (b) Create actions create on a separately configured model under elevation; that model is never gated. (c) Duplicate actions copy a fixed, configured source record under elevation and may then write a link on the context record | E12 object-write/create/copy runners; gate | PR-06 |
| O2 | HIGH (reachability open) | The gate collects its records from the context only when the context model equals the action's model. Otherwise the record check is skipped and only model-level write ACL applies. Single-record runners still iterate the context ids and browse them on the action's model under elevation. A caller able to invoke run with a mismatched or missing context model could have a record-rule-protected record updated. Whether any non-admin entry point allows that is outside module scope (controller) | E12 eval-context build, run, dispatch loop, gate | PR-11 |
| O3 | MED | The group check keeps binding the real user under elevation. Group-restricted actions attached to automations, or used as multi-action children, raise for triggering users outside the group, which can block their operations | E12 gate; base_automation processor | PR-07, PR-10 |
| O4 | MED | Webhook payload guard (mitigation): any field-level group-restricted field in the payload produces a warning, and an action with warnings refuses to run. A1's C28 risk statement omits this | E12 warning messages; run refusal | PR-09 |
| O5 | MED | The throttle counter for an address is cleared by any successful authentication from that address. Bearer-route key verification is not wrapped by the throttle. Programmatic generate/revoke are wrapped | E3 throttle; E13 bearer | PR-15 |
| O6 | MED | API keys carry no company binding and no privilege subset. A key acts with all of the owner's groups and allowed companies. Scope is a free label: a key with the literal RPC label passes the RPC check and can programmatically generate a global key | E3 key model and helper; E13 bearer | PR-14 |
| O7 | HIGH (business) | The access-rights manager role has full CRUD on users, groups, record rules, ACL rows, models and companies. It can therefore delete or loosen the global company walls. Whether it can raise itself to administrator is not settled here, because group-write guards were not read in full | E19 rows; E18 | PR-19 |
| O8 | MED | Debug-mode access errors, for internal users holding the technical-features group, list the display names of up to 6 denied records (read elevated), the failing rule names, and company names | E9 error builder | none (static; UNCORROBORATED) |
| O9 | LOW | Denied-access diagnostics compute failing rules through elevated searches over the denied ids. This is a side channel only if timing or rule names are exposed (see O8) | E9 | none |
| O10 | HIGH (multi-company) | Scheduler jobs carry no activated-company context. Their rule evaluation depends on the ORM-core default for the company set (G1). Seeded jobs run as the installing account | E10 job environment; E20; E4 comment | PR-12, PR-13 |
| O11 | MED | Scheduler-run server actions have no context records, so the gate reduces to model-level write ACL (or the group check). No record-rule check occurs at the gate | E10 callback; E12 gate | PR-12 |
| O12 | LOW | The self-writeable list includes the key relation and the home action. The elevated self-write is contained because the key model refuses elevated relational commands | E3 self-writeable list; key model | none |
| O13 | LOW | The at-least-one-administrator constraint is skipped during updates of `base`. The admin set-password path silently ignores empty values | E3 | none |

## 7. Lane B classification

No Lane B evidence exists. Nothing is FAIL.

| Class | Claims |
|---|---|
| NOT_APPLICABLE (runtime cannot meaningfully corroborate: manifest structure, storage format, carried pointer) | C01, C19, C22, C36 |
| UNCORROBORATED (runtime-observable, no Lane B yet) | C02, C03, C05, C08, C09, C13, C14, C15, C16, C17, C18, C21, C23, C25, C32, C33, C34, C35 |
| MISSING_REQUIRED_RUNTIME_PROOF (inherently runtime: isolation outcome, identity at execution, caching, concurrency, throttling) | C04, C06, C07, C10, C11, C12, C20, C24, C26, C27, C28, C29, C30, C31 |

## 8. Proof requirements

Priority 1 covers cross-company isolation and superuser execution under automation. Each requirement states a setup, an expected result and a fail condition.

| PR | Priority | Claims | Setup / action | Expected | Fail condition |
|---|---|---|---|---|---|
| PR-01 | 1 | C06, C07, S2 | User U with allowed companies A and B. Records R_A (company A) and R_B (company B) on a company-ruled model. Activate A only and search; switch to B only in the same session and search; repeat with a call on a second worker | Only R_A is visible, then only R_B. The second worker gives the same results | R_B is visible while only A is active, or R_A is visible after the switch, on any worker |
| PR-02 | 1 | C10, CRQ-06 | Parent P with branch Q. Partner X owned by Q, partner Y owned by P. User allowed P and Q. Activate P only, then Q only | With P active: Y visible, X not. With Q active: X and Y visible | X visible while only P is active, or Y not visible while Q is active |
| PR-03 | 1 | C11, S1 | Company A user U1. Company B internal user U2 and company B portal user U3. U1 activates A only and searches partners | U2's partner is visible. U3's partner is not | U3's partner is visible, or U2's partner is not |
| PR-04 | 1 | C12 | Internal non-manager user reads company C (allowed but not activated) and company D (not allowed). Repeat as access-rights manager | Non-manager: neither C nor D. Manager: both | Non-manager sees C or D, or manager misses either |
| PR-05 | 1 | C04 | Model M with a global rule G (company wall) and two group rules for group K: narrow N and broad "all". A user in K | Visible set = G ∩ all = G. Removing the broad rule gives G ∩ N | Any record outside G is visible, or the broad rule fails to widen within G |
| PR-06 | 1 | C27, O1, CRQ-01, CRQ-10 | Non-admin U can write record R (model X) but not related record S (reached by a relational path from R). Admin creates an unrestricted update action on X with a path to S; U runs it on R. Also: a create action targeting model Z, where U has no create ACL on Z | S is written and Z's record is created. Last-writer/creator fields name U | Access error on S or Z. That disproves the elevated-target reading |
| PR-07 | 1 | C27, O3, CRQ-02 | Multi action (no groups) with a code child that records the superuser flag and uid. Run by non-admin U with write on the model. Variant: the child and parent carry group K and U is not in K | Superuser flag set; uid = U. Variant: access error before execution | Flag not set in the base case, or the variant executes |
| PR-08 | 1 | C26, CRQ-03 | Update action restricted to group K. U is in K but R is outside U's write rules. U runs it on R | R is updated | Access error |
| PR-09 | 2 | C28, O4, CRQ-04 | Webhook action on a model whose field F is group-restricted: include F, then remove F and include a field of a record U can write but not read by rule. Capture the outbound POST | With F: the run is refused (warning). Without F: the POST contains the value | With F: a POST is sent. Without F: a refusal (this would disprove the elevated read) |
| PR-10 | 1 | CRQ-01 (section 4) | Event-triggered automation on model X whose code action writes model Y and records the superuser flag and uid. Internal user U without write on Y edits an X record. Cross-ref base_automation PR-01 | Y is written; flag set; uid = U | Access error, or flag not set |
| PR-11 | 1 | O2 | U can write model X but record R is outside U's write rules. Invoke an unrestricted update action on X with active id R and a context model different from X, through every non-admin entry point available (web action route, RPC) | Static hypothesis: R is updated under elevation. Record which entry points allow it | For the hypothesis: an access error on every entry point. That closes O2 as unreachable |
| PR-12 | 1 | C29, O10, O11, CRQ-10 | Inspect the configured user of the seeded jobs and record the superuser flag inside a job's code. Configure a job to a non-admin user whose server action targets a model without write ACL | Seeded: the installing account, flag as observed. Non-admin: access error logged, failure count incremented | The non-admin job executes its mutation, or the failure is not counted |
| PR-13 | 1 | O10 | A job run by user J (allowed A and B, default A) counts records of a company-ruled model owned by A, B and C (C not allowed) | C records are never counted. Record whether B is included | C records are counted |
| PR-14 | 1 | C24, O6, CRQ-08 | Keys: expired (expiry forced into the past, before the vacuum), owner archived, scoped to a non-RPC label, literal RPC label. Use each on a bearer route and on RPC | Rejected: expired, archived, non-RPC scoped. Accepted: literal RPC label | Any of the first three accepted, or the literal-label key rejected |
| PR-15 | 2 | C20, O5, CRQ-07 | Configure N=3. Fail 3 times from one address on worker 1, then try on worker 2. Interleave a success. Send 50 invalid bearer keys | Worker 1 is in cooldown; worker 2 is not. A success resets the counter. Bearer attempts are never throttled | Cooldown shared across workers, no reset on success, or bearer throttled (any of these disproves the static reading) |
| PR-16 | 2 | C30, CRQ-09 | Two cron workers and one due job that logs each start | Exactly one start per due slot | Two concurrent starts |
| PR-17 | 2 | C31, CRQ-09 | A job that always fails: 5 failures within 1 day; then failures spanning more than 7 days | Still active after the first series; deactivated with an admin notification after the second | Deactivated early, or never deactivated |
| PR-18 | 2 | C07, CRQ-05 | Edit a rule in worker 1, then search in worker 2 immediately | The new rule applies in worker 2 | Stale result in worker 2 |
| PR-19 | 2 | O7 | An access-rights manager who is not an administrator adds themself to the administrator group, then archives a global partner rule | Hypothesis: both succeed | For the hypothesis: either is refused |
| PR-20 | 3 | C17 | A user sets their own default company to one outside their allowed companies through the self-edit path | Write succeeds; default company unchanged; no error | An error is raised, or the default company changes |

Proof requirement count: 20.

## 9. Limitations

- SOURCE-STATIC only. No runtime, no database, no Lane B. Source presence does not prove runtime reachability. Overriding modules (2FA, mail, portal, web controllers) may change credential, identity and entry-point behaviour.
- ORM core is outside module scope (G1). This covers superuser semantics for the superuser uid, derivation of the activated company set, audit-field stamping and company-consistency enforcement. So are the HTTP session layer (G2) and multi-worker cache propagation (G6). Conclusions that depend on these are marked as proof requirements, not verdicts.
- Large files were read in sections around the cited behaviour. Group-write guards (O7), the web action controller (O2) and the webhook route (section 4) were not read.
- CRQ-01 is CLOSED-STATIC only at source-path level. No privilege-escalation outcome is asserted without runtime proof.
- No QID answered, no Formal Coverage, no percentages, no git operations. Clean-room paraphrase only.
