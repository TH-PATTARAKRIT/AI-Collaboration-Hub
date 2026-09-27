# G01 PLATFORM_BASE — RED TEAM A3 Independent Challenge (STATIC scope) — `base`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, an independent adversarial challenger. This reviewer authored no upstream stage (Lane A, A1, A2, REC or Proof) |
| Group / Module | G01 PLATFORM_BASE / `base` |
| Date | 2026-09-27. Intake 15:19:38 UTC; source re-fetch 15:20:10 UTC; write-up 15:24 UTC |
| Scope | STATIC only (SOURCE / CONFIG / CROSS-MODULE). Runtime is **NOT-EXECUTED**: it has neither passed nor failed |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, fetched from the commit-pinned raw URL. Every blob was recomputed with `git hash-object`. Local copies are held in the scratchpad `a3_base/src/`, with the blob log at `a3_base/blob_log.txt` |
| Intake manifest | Scratchpad `a3_base/intake.sha256` (section 0.1) |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to PROOF, INTEGRATION CONTROL, and base_automation A3 / next round). All defects are LOW and none reverses a verdict. MASTER handoff is PENDING RUNTIME** |

### 0.1 Intake (sha256, recorded before any other read)

| Input (relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`) | sha256 | Cross-check |
|---|---|---|
| `G01_LANE_A_PASS1/G01_BASE_LANE_A_PASS1_20260927.md` | `9108bd4f64762c79f763a35c9d6e944153bd7eec5c0fad3bda9d0eadcd59403b` | Equals the REC / Proof intake |
| `G01_A1_PACKAGES/G01_BASE_A1_PACKAGE_20260927.md` | `a45a2beff88b8be61cd81b6075f7072f156c1b9d1d93029f0afb6ad35a0189e7` | Equals the REC / Proof intake |
| `G01_A2_REVIEWS/G01_BASE_A2_REVIEW_20260927.md` | `05e422246b9bb925145c67ac044a6dc789bd99212376d59d47afa28a9b3500c1` | Equals the REC / Proof intake |
| `G01_RECONCILIATION/G01_BASE_REC_20260927.md` | `c343d43408c57b7e6cc75a3b9d5edf85737281dc9e5bda71a732762a567b833c` | Not recorded in the Proof header (see D1) |
| `G01_PROOF/G01_BASE_PROOF_20260927.md` | `49e96bcfd16a1098b64aae6ad6d169aa676227d02ee14dd29af4d36ec38618e6` | Equals the committed HEAD blob `547457c8…` |
| `../GMVQ/G01_PLATFORM_BASE/G01_BASE_GMVQ_MVQ_50_V1.00_DRAFT.md` | `b242fa0e98aeedd12b5ae33aa9800a1831a795222052f87621960d4d9aed8777` | **Equals** the `FREEZE_W1-B01.json` bank entry. freeze_hash `558ec880…7177` is as declared |
| `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B01.json` | `d0edfb228d849b5633cdd1dccea95667305831c2c264f43432c337c4fa3d1351` | Equals the REC intake |

Clean-room statement: this record contains neutral WHAT/WHY/RISK paraphrases only. Identifiers are evidence pointers. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. Git was used read-only (`log`, `show`, `diff`, `rev-parse`, `hash-object`). No input was edited.

## 1. Challenge log

### Ch-1 — Tenant/company model (C04, C06, C12, S1, O7): **UPHELD**, with one LOW wording defect (D3)

The model was re-derived from source (`ir_rule.py` e64f4e2c, `orm/environments.py` ec6b89fc, `orm/models.py` 11f50c4e, `base_security.xml` 63195795, `ir.model.access.csv` 29785e02). Each refutation attempt is listed below.

| Claim | Refutation attempted | Result |
|---|---|---|
| Rule composition: global rules are ANDed; applicable group rules are ORed and that OR is ANDed with the globals; superuser gets no rules | Looked for any path that ORs globals, or ANDs group rules with each other | None. The rule lookup returns an empty set under superuser. Group rules whose groups do not intersect the user's effective groups are skipped. A group rule with an empty domain counts as TRUE, so it widens the OR term to "all" (A2's refinement is correct). Delegated-parent domains are ANDed first and apply even when the model has no own rules. **Nuance, not a defect:** the SQL pre-selection matches on the user's directly resolved groups, and the in-code filter matches on all effective groups. Both are the user's own groups, so composition is unaffected |
| The `company_ids` evaluation input is the activated set | Checked whether the full allowed set is used instead | The evaluation context uses the environment's activated companies and current company. The user is passed with an empty context. The domain cache key contains uid, superuser flag, model, mode and the raw activated-company context value |
| A non-superuser may only activate allowed companies | Looked for a path that accepts out-of-set ids for a non-superuser | Both accessors (current company, activated companies) **raise** an access error on any id outside the user's allowed companies, and only outside superuser mode. They reject; they do not filter. The Proof's predeclared expectation "reject or filter" is a disjunction (weak-condition flag W1), but the fail condition stayed falsifiable |
| No company context means all allowed companies | Looked for a fallback to the main company | For the activated set, the fallback is **all** allowed companies. The current-company accessor falls back to the user's default company. Proof R1 is correct |
| The superuser account uid always runs in superuser mode | Looked for any constructor path that clears the flag for that uid | Environment construction forces the flag whenever the uid is the superuser account. Switching user drops the flag unless it is passed explicitly, and it is forced again for that uid |
| The company-consistency check is opt-in and is not skipped under superuser | Looked for a superuser guard and for context-key skips | It runs after create and write only when the model-level flag is set, and only for fields flagged individually. No superuser guard exists, and linked records are read elevated. Company-dependent fields are checked against the *current* company, and in superuser mode that value is not validated against the user's allowed set. That is a residual point for runtime, not a defect |
| S1: "company is a user-selected filter, not a tenant boundary" | Looked for any storage-level or connection-level separation in the read files | None found in scope. Separation is context-driven rule evaluation inside one data store, bypassed by elevation, with share-flag exemptions and an unrestricted manager rule. **Refinement (D3):** Proof section 6 says company visibility "is bypassed by any elevated execution". That is true for record rules and the company-context check. It is **not** true for the opt-in consistency check, which still refuses cross-company links under elevation (Proof R4 / PC-38). The design note should carry that exception |
| O7: the access-rights manager can edit company-separation rules, add users to the administrator group, and set others' passwords, including an administrator's | Searched for guards in the users and groups models; the users, groups and rules **views**; the wizard index; the rule model's write, create and unlink paths; the field-level `groups` attribute on the membership field; `check_identity` on those paths; and record rules on the users, groups and rules models | **No authorization guard found.** The access-rights manager holds full CRUD on rules, groups and users, and read/write/create on the admin password wizards. Company rules give that group an "always true" row. The users write path guards only activating the superuser, deactivating oneself, and the self-edit field list. The groups write path guards only the name prefix and implied-group removal. The rule write path only clears caches. In the views, the membership widget and the groups menu are shown only in developer mode (`group_no_one`). That is UI visibility, not authorization. The password wizard calls the plain password setter with no check on the target's privilege; empty input is skipped or refused, not accepted. **Additional corroboration:** the users model's own "is admin" helper treats membership of the access-rights manager group as administrator-equivalent, so the vendor code itself regards this role as admin-tier. Other modules remain unread (G4), so a guard there is not excluded |

### Ch-2 — Execution identity (CRQ-01; seeded crons): **UPHELD** (A2 side; the R2 exclusion is handled correctly, with one note)

- CRQ-01: the base_automation file (blob `099ba2e3…`, MATCH) has exactly two `run` call sites, the per-record processor and the UI-change hook. Both iterate the actions of an elevated copy of the rule. There is no unelevated call. A2's CLOSED-STATIC holds for the static question. A1's NARROWED was the correct disposition for A1's evidence at the time, because A1 lacked the file. REC's classification of this as a disposition-level CONTRADICTION is appropriate.
- Crons: the job environment is built from the job's user id with no explicit elevation and no company context. The callback runs the server action there. The seeded-job data declares no user, and the user field defaults to the environment's current user. The module loader builds its environment for the superuser account uid (`odoo/modules/loading.py`, blob `7be8669d7bba55c67d3bf71c09c8b7cbf0455d56`, reproduced).
- R2 adjudication: the Proof blob log marks `loading.py` "supplementary, post-predeclaration". Its file timestamp (15:12:30) is later than the predeclaration (15:10:59, read-only). The Proof uses it only in 3.1 R2, and no predeclared verdict depends on it. REC-29 cites it inside its "Basis for class" cell, but labels it "supplementary observation", and the class (CONTRADICTION) would be the same without it. **The exclusion from case results is correct.** Note: PC-36's predeclared fail condition ("default is a fixed superuser") is not met at field level, but it is effectively realised through the loader. The Proof surfaced this honestly as R2 rather than recasting PC-36; weak-condition flag W2.

### Ch-3 — The 7 CONTRADICTIONs: **UPHELD** (all 7 re-verified; source supports A2 in each)

| Item | A3 re-read | Verdict |
|---|---|---|
| C14 | The branch helper always walks from an elevated copy and intersects with the activated set. The superuser uid matters only for the empty-result fallback, which returns the company itself (commented as the scheduler case) | A2 supported |
| C26 | With groups, the gate checks group membership only. Without groups, it checks model write access, and then the write-rule check on records collected from context **only when the context model equals the action model**. Single-record runners iterate the context ids regardless | A2 supported (O1, O2) |
| C27 | The multi runner iterates the children of the elevated parent. Each child's gate runs elevated: model and record checks are skipped, but the group check reads the environment user, which keeps the real uid. Code actions at top level receive the caller's environment | A2 supported (O3) |
| C28 | The webhook reads the record elevated and sends after commit with a 1 s timeout. The warning builder flags any payload field that carries field-level groups, and run refuses actions with warnings | A2 supported (O4) |
| C29 | See Ch-2. "Not in superuser mode at entry" fails for any job whose user is the superuser account, and seeded jobs get that user through the loader | A2 supported; R2 goes further (supplementary) |
| C31 | The loop continues while fewer than 10 iterations **or** less than 10 s have passed, so it stops only when both limits are reached. **The 5-hour limit, which REC had not re-read, was re-read here:** it applies only when modules are in a pending install/upgrade/remove state, when it decides whether to reset module state | A2 supported on both points. The REC note "5-hour point not re-read" is now discharged by A3 |
| CRQ-01 | See Ch-2 | A2 supported |

All 7 stay CONTRADICTION as preserved dual-source records, with the static side settled for A2. The runtime effect is pending for C26–C29, C31 and CRQ-01.

### Ch-4 — Static PASS re-execution: **UPHELD** (9 cases re-executed; 0 overturned; 2 weak-condition flags)

| Case | A3 result | Note |
|---|---|---|
| PC-BASE-21 | PASS reproduced | Composition as in Ch-1 |
| PC-BASE-23 | PASS reproduced | W1: the "reject or filter" expectation is disjunctive, but the fail condition is still falsifiable |
| PC-BASE-24 | PASS reproduced | The constructor forces the flag for the superuser uid. The ORM access check, `has_access` and access filtering all short-circuit under superuser |
| PC-BASE-29 | PASS reproduced and **widened** | The guard search now also covers views, the wizard index, rule write paths and record rules. Still no guard (Ch-1) |
| PC-BASE-30 | PASS reproduced | The records collected depend on the context model |
| PC-BASE-32 | PASS reproduced | The group check uses the real uid |
| PC-BASE-36 | PASS reproduced | W2 (see Ch-2) |
| PC-BASE-37 | PASS reproduced | |
| PC-BASE-38 | PASS reproduced | No superuser bypass. Opt-in at model and field level |
| PC-BASE-42 | PASS reproduced | Also covers the 5-hour point (Ch-3) |

ORM blobs (these had no upstream blob; recorded by A3 at the anchor):

| Path | Computed blob | Status |
|---|---|---|
| `odoo/orm/environments.py` | `ec6b89fc3b752d3c52eb220e95437dbd4db134fd` | HTTP 200. Equals the Proof |
| `odoo/orm/models.py` | `11f50c4e0b676fbb4b8a45e9703326946348ff98` | HTTP 200. Equals the Proof |
| `odoo/models.py` | n/a | **HTTP 404: this path does not exist at the anchor.** The ORM lives under `odoo/orm/`, so the Proof's path choice is correct |
| `odoo/modules/loading.py` | `7be8669d7bba55c67d3bf71c09c8b7cbf0455d56` | HTTP 200. Equals the Proof scratch blob log |
| `odoo/api/__init__.py` | not re-fetched | The Proof uses it for no verdict |

All 16 upstream-referenced base blobs that A3 re-fetched (the rule, users, company, groups, model, actions, cron and HTTP models; the security XML and CSV; the cron data) match exactly. The users, groups and rules views and the wizard index were read for Ch-1 only, and their blobs are in the A3 blob log.

### Ch-5 — Cross-module note to base_automation (Proof R4 / R5): **UPHELD — routed** (see D4)

The base_automation Proof R4 wording ("the per-action gate does not restrict rule-triggered actions") is **true only for actions without groups**. Under elevation, the model and record checks are skipped, but the group check still tests the real uid's effective groups. A group-restricted action attached to an automation therefore raises for a triggering user outside the group (A2 O3), and can block that user's own edit. A3 adds one static point, recorded as a question only: for time-based automations run by a job whose user is the superuser account, the group check tests that account's groups. Whether that account belongs to a given group is data-dependent and runtime-only. It is not claimed here.

### Ch-6 — Predeclaration, lineage, overclaim, Lane B, QID fit, bank, clean room: **UPHELD**, with LOW lineage defects D1 and D2

- **Predeclaration:** `rec_base/proof_cases_predeclared.txt` has sha256 `55d9b0f9…53fd`, which is **equal**. Its mtime is 15:10:59 and its mode is read-only. The sidecar hash was written at 15:11:06. The ORM copies were fetched at 15:10:11–12, which is before the predeclaration, consistent with the Proof's disclosure "fetched for hashing before, not re-read until after". Read-timing cannot be verified from file metadata (a limitation). `loading.py` was fetched at 15:12:30, after the predeclaration, as disclosed.
- **Lineage (read-only `git log --follow`):** A2 is in `79cd651` (15:07:34, correctly labelled). Lane A is in `42612ef`, whose message names base_sparse_field/google_recaptcha. A1 is in `1da52bf`, whose message names onboarding/html_builder/…. REC is in `d59dd2b`, whose message names "A3 resource …". So three base artifacts were committed under **other modules' commit messages (D2)**. The Proof was committed in `6d55fdb` and then changed in `0eaeb25`. The change is one line, a cosmetic correction of the runtime-case list in section 5 ("PC-06..12, 16, 17" became "PC-06..12, PC-17"). It changes no verdict. The current working-tree blobs for REC, Proof and A2 equal HEAD.
- **Overclaim:** none found. Static PASS is never counted as a runtime result. All 21 runtime cases are NOT-EXECUTED. UNKNOWN_PENDING_PROOF items remain open. CLOSED-STATIC is explicitly "not a proven escalation".
- **Lane B:** no misuse. The REC search found no Lane B pool for `base`. Absence is UNCORROBORATED or NOT_APPLICABLE and is never FAIL. No runtime claim rests on Lane B.
- **QID mapping fit (sample of 6):** Q009 (actor identity vs background process) → C27/C29/CRQ-01: good fit. Q022 (direct navigation = search authorization) → C02/C04: good. Q031 (cross-company copy revalidates relations) → G1/PC-38: acceptable. Duplication goes through create, which triggers the opt-in check, but only for opted-in models, and the mapping says as much. Q045 (company boundary with shared user/partner) → C10–C13/O7: good. Q050 (deferred operation revalidates after deactivation) → C24/C29/G7: good. Q047 (privilege change during a long batch) → C03/C29: **weak but tolerable**. C03 (cache clearing on group change) fits; C29 is only indirect. Lineage only; no QID answered.
- **Bank:** sha256 equals the FREEZE_W1-B01 entry. The freeze hash is as declared (replay not re-run by A3; the REC replay is relied on).
- **Clean room:** a scan of REC and Proof for code-shaped text (definitions, domain literals, elevation calls, imports, SQL clauses) and for percentage/Formal Coverage tokens found only negation statements. No vendor code or schema was reproduced. The design-implication note is neutral and non-prescriptive, apart from the D3 wording.

## 2. Lineage

| Stage | Artifact sha256 | Commit (read-only) | Chain check |
|---|---|---|---|
| Lane A | `9108bd4f…403b` | `42612ef` (mislabelled message) | Hash carried in A1, A2, REC and Proof |
| A1 | `a45a2bef…89e7` | `1da52bf` (mislabelled message) | Hash carried in A2, REC and Proof |
| A2 | `05e42224…00c1` | `79cd651` | Hash carried in REC and Proof |
| REC | `c343d434…833c` | `d59dd2b` (mislabelled message) | **Not carried in the Proof header (D1)** |
| Proof | `49e96bcf…18e6` | `6d55fdb` → `0eaeb25` (one cosmetic line) | Intake hash is the post-change version |
| Bank / Freeze | `b242fa0e…8777` / `d0edfb22…51` | `b0f6dfd` | Bank equals the freeze entry |
| Predeclaration | `55d9b0f9…53fd` | scratchpad (not committed) | Equal; read-only; timed before re-read |
| A3 (this) | — | not committed by A3 | Hands off to MASTER |

## 3. Defects routed

| ID | Severity | Owner stage | Defect | Required action |
|---|---|---|---|---|
| D1 | LOW | PROOF | The Proof header names the upstream REC file but records no sha256 for it, and the Proof file was changed (cosmetically) after its first commit | Record the REC sha256 in the Proof header. Log the `6d55fdb` → `0eaeb25` one-line correction in a change note |
| D2 | LOW | INTEGRATION CONTROL | Base Lane A, A1 and REC were committed under commit messages naming other modules or stages | Record a lineage erratum that maps each base artifact to its actual commit. No history rewrite |
| D3 | LOW | PROOF (section 6 design note) | "Company visibility … is bypassed by any elevated execution" overstates the case. The opt-in company-consistency check still applies under elevation (PC-38, R4) | Add the exception to the S1 bullet. No verdict change |
| D4 | LOW (wording) | **base_automation A3 / next round** (cross-module) | base_automation Proof R4 / PC-BAUT-40 says the gate "does not restrict" rule-triggered actions. That is true only for actions with no groups. Under elevation the group check still tests the real user (base A2 O3; PC-BASE-32 reproduced by A3). No base_automation REC item carries O3 | Refine the R4 wording. Consider carrying O3 as a REC item. Runtime variants: PC-BASE-07, PC-BASE-10 |
| W1, W2 | Flags only | PROOF (next round) | PC-23 has a disjunctive expectation. PC-36's fail condition is realised indirectly through the loader (R2) | Tighten these conditions in future predeclarations. No re-execution needed |

No MEDIUM or HIGH defect. No stage FAIL. No challenge was sustained against any verdict: every PASS, class and CONTRADICTION direction was reproduced.

## 4. Runtime-blocked items (NOT-EXECUTED; not passed, not failed)

- All 21 runtime cases: PC-BASE-01..20 and PC-BASE-47. The device THPATTARAKRIT-SOLUTION-SERVICE-2.local was offline per the Proof.
- High-priority for MASTER: isolation outcomes (PC-01..05, PC-13); elevated action effects and automation identity (PC-06..12), including R2 (seeded jobs run as the superuser account in superuser mode); access-rights-manager self-elevation and the password-set variant (PC-19); key rejection and throttling (PC-14, PC-15); scheduler concurrency and thresholds (PC-16, PC-17); cross-worker cache (PC-18); debug-mode disclosure (PC-47).
- All 20 UNKNOWN_PENDING_PROOF items and the runtime effect of 6 CONTRADICTION items (all except C14).
- Carried GAPs: G2 (core HTTP session/token), G4 (views, wizards, other modules; partially sampled by A3 for O7 only), G7 (scheduler-user eligibility). G1 is narrowed but open (audit stamping, retry, HTTP-to-ORM wiring).

## 5. Limitations

- Static only. A3 did not re-read every MATCH item. It relied on A2 for C01, C09, C15–C19, C21–C23, C32, C36, O12 and O13, except that C16's update-time admin-check skip was spot-seen.
- The O7 "no guard" finding covers `base` model, security, view and wizard files at the anchor. Guards in other modules (for example web client, auth or mail addons) were not searched.
- Predeclaration read-timing is inferred from file metadata and the Proof's own disclosure. It cannot be proven from mtimes.
- The freeze-hash replay was not re-run by A3. Bank equality with the freeze entry was checked directly.
- A3 re-read only a sample of the QID mapping (6 QIDs). It is lineage, not coverage.
- No percentages. No Formal Coverage claim. Inputs were not edited. Git was used read-only.

**Final A3 disposition: A3 STATIC PASS WITH DEFECTS (route to PROOF: D1, D3; INTEGRATION CONTROL: D2; base_automation A3 / next round: D4). MASTER handoff PENDING RUNTIME.**
