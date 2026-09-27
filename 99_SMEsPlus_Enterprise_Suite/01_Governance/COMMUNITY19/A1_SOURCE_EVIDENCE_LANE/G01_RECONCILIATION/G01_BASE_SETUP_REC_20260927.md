# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `base_setup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_BASE_SETUP_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `base_setup` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/base_setup/` (+ core files named in the Proof package) |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_BASE_SETUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `2161184604279f38a59f8e56db288f53d4e706d4ec85cb5ba2a224e883a26d62`. This **equals** the `bank_files` entry in `FREEZE_W1-B04.json`. Freeze hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377`. W1-B04 is ELIGIBLE per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md`. The bank holds **41** QIDs (Q001–Q041; floor delta recorded in the replay file) |
| Join key | MODULE `base_setup` + QID + freeze hash above. Mapping is lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (34 REC items; 5 CONTRADICTION items carried into Proof, none closed by REC) |

### 0.1 Input intake (immutable; sha256 recorded at intake, 2026-09-27 ~15:03 UTC)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_BASE_SETUP_A1_PACKAGE_20260927.md` | `3e37b467fb26899f96af1f44cc17db63a7855b3696ca96a72ab5e3f489a90970` | Matches the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_BASE_SETUP_A2_REVIEW_20260927.md` | `9e913ee76c3e1c34418a7e1d1ae93e4df1c65636abbd101849cc79cb3b651a31` | Disposition "A2 PASS WITH FINDINGS" (C11 NOT_VERIFIED); 11 proof requirements (PR-BSET-01..11) |
| Lane A packet | `G01_LANE_A_PASS1/G01_BASE_SETUP_LANE_A_PASS1_20260927.md` | `59d3d312c3f5bff8dba13b24bb66a648f357b418677a9e74f242d0929f6ae4ce` | Matches the hash recorded in both A1 and A2 headers |
| Cross-module A2 (interaction only) | `G01_A2_REVIEWS/G01_AUTH_SIGNUP_A2_REVIEW_20260927.md` | `e5ce1b56ab35903665d02b3c58d184e2ba334ba72e8d09578ae0ff07f5dd28f9` | Used only for O2 (no invitation on reactivation) |
| Question bank | see header | `21611846…26d62` | Equals FREEZE_W1-B04 entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B04.json` | `27db90332c140e569d4ab7f3a6d2fe7f5d0aae5f375065b5ab2ffe2d95f4d4f9` | freeze_hash `9e31f2d2…0377` |

### 0.2 Lane B evidence-pool search (recorded, 2026-09-27 15:03 UTC)

- `grep -ril base_setup /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite` → 38 files. Filtering for `lane_b|lane b|laneb|gemini|evidence_pool|evidence pool` → 14 files; every hit is a governance statement of absence ("Lane B dependency: None", "No Lane B material viewed", freeze-rule text). None contains a runtime observation.
- `find` for `*lane_b*`, `*gemini*`, `*evidence_pool*` over the repository → **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `base_setup`**. Absence is not failure.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code reproduced; nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited.

## 1. Classification rules (predeclared)

Identical to `G01_AUTH_SIGNUP_REC_20260927.md` §1 (MATCH / GAP / CONTRADICTION / UNKNOWN_PENDING_PROOF; Lane B UNCORROBORATED / NOT_APPLICABLE, never FAIL). One explicit exception: C12 is MATCH although A2 lists PR-BSET-06, because A2 marks the underlying contradiction X-BSET-02 RESOLVED by a core read and the runtime case is confirmatory only.

Scope: A1 claims C01–C22; A2 omissions O1–O7; A1 contradiction candidate X-BSET-03 (resolved); carried gaps not absorbed. Fold-ins: G1→C12 (X-BSET-02); G4→C15/O3 and C17/O4; G6→C11 (X-BSET-01); G8→C07; F2→C11/O7; F3→C07/O1; F7→C21.

## 2. Reconciliation table

PC = proof case in `G01_PROOF/G01_BASE_SETUP_PROOF_20260927.md`. Static cases PC-BSET-01..17 executed; runtime cases PC-BSET-18..28 (= PR-BSET-01..11) pending.

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (MODULE `base_setup`) |
|---|---|---|---|---|---|---|---|---|
| REC-BSET-01 | C01 | General-settings anchor; auto-install; no ACL/rule files / HIGH | VERIFIED | MATCH | Manifest re-read (PC-01) | NOT_APPLICABLE | PC-01 | — |
| REC-BSET-02 | C02 | Settings menu admin-only; blocks dev-mode / multi-company / HIGH | VERIFIED | MATCH | Menu and block groups re-read (PC-02) | UNCORROBORATED | PC-02 | Q001 |
| REC-BSET-03 | C03 | Company pass-throughs (footer, layout, identity) written on save / MED | **PARTIAL** — only footer writable; layout/name/country read-only | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-03 PASS, incl. core related-field readonly default). Both preserved | UNCORROBORATED | PC-03; PC-27 | Q002, Q023 |
| REC-BSET-04 | C04 | Install toggles; mechanics in base / MED | VERIFIED | MATCH | 15 toggle fields re-read (PC-15 context) | NOT_APPLICABLE | — | Q004, Q036 |
| REC-BSET-05 | C05 | Default-access group created on demand, registered non-updatable / HIGH | VERIFIED (strengthened: runs as caller; implied groups applied to new internal users) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-04). Audit attribution is runtime (PR-BSET-11) | UNCORROBORATED | PC-04; PC-28 | Q007, Q009, Q041 |
| REC-BSET-06 | C06 | Bulk invite normalises, reactivates archived matches, creates users with prepared link / HIGH | **PARTIAL** — "prepared link" mis-attributed; base_setup sets an inert context flag, link comes from auth_signup create hook | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-05 PASS). Both preserved | UNCORROBORATED | PC-05 | Q010, Q011 |
| REC-BSET-07 | C07 (+G8) | Reactivation flips active only; prior groups may be restored / MED | VERIFIED (strengthened → O1) | UNKNOWN_PENDING_PROOF | Core write on reactivation leaves groups untouched (PC-06 PASS). Runtime PR-BSET-07 | UNCORROBORATED | PC-05, PC-06; PC-24 | Q011 |
| REC-BSET-08 | C08 | Bulk invite fails closed without Discuss layer / HIGH | VERIFIED | MATCH | Re-read (PC-13) | UNCORROBORATED | PC-13 | Q014 |
| REC-BSET-09 | C09 (+F7) | Dashboard data route: session + explicit manager check; counts + 10 pending ids/logins / HIGH | VERIFIED (counts cross-company) | MATCH | Re-read (PC-11) | UNCORROBORATED | PC-11 | Q018, Q019 |
| REC-BSET-10 | C10 | Pending = active internal with no log row; WHY: consistent with search not compute basis / HIGH | **PARTIAL** — definition verified; WHY refuted (bases coincide) | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-11; auth_signup PC-ASGN-11). Both preserved | UNCORROBORATED | PC-11 | Q020 |
| REC-BSET-11 | C11 (X-BSET-01, +G6) | Demo-status route: no group check; any logged-in user learns demo state / HIGH | **NOT_VERIFIED** — literal true; non-admins get an access error via module-registry ACL | **CONTRADICTION** (A1 vs A2; A1 claim refuted at source) | Route has no elevation; registry read granted to system administrators only; count enforces model read access (PC-10 PASS). Runtime PR-BSET-05 | UNCORROBORATED | PC-10; PC-22 | Q018, Q022 |
| REC-BSET-12 | C12 (X-BSET-02, +G1) | Settings counter lacks explicit active filter; divergence depends on core / MED | VERIFIED; X-BSET-02 RESOLVED | MATCH | Default archive filter applies to the ORM count (PC-12 PASS). PC-23 confirmatory | UNCORROBORATED | PC-12; PC-23 (confirmatory) | Q017, Q020 |
| REC-BSET-13 | C13 | KPI route unauthenticated, no session save, >500 pairs rejected / HIGH | VERIFIED | MATCH | Re-read (PC-08) | UNCORROBORATED | PC-08 | Q032 |
| REC-BSET-14 | C14 (+F5 part) | Per-DB independent evaluation; silent omission; anti-enumeration / HIGH | VERIFIED (nuance: distinct code paths, server-side log with DB name) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-08). Body/timing equality is runtime (PR-BSET-03) | UNCORROBORATED | PC-08; PC-20 | Q027, Q028, Q029 |
| REC-BSET-15 | C15 (+F1) | Verified key → full internal-user roster; no role check on key owner / HIGH | VERIFIED (strengthened) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-07). Runtime PR-BSET-01 | UNCORROBORATED | PC-07; PC-18 | Q019, Q027, Q033 |
| REC-BSET-16 | C16 (+F6) | Providers rolled back per call; errors captured / HIGH | VERIFIED (limit: explicit commit or external effects not prevented) | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-08). Durability of side effects is runtime (PR-BSET-09) | UNCORROBORATED | PC-08; PC-26 | Q030, Q031 |
| REC-BSET-17 | C17 | Providers discovered from installed addons' manifests; injection point / MED | **PARTIAL** — discovery reads every manifest on the addons path regardless of install state | **CONTRADICTION** (A1 vs A2) | Source re-read supports A2 (PC-09 PASS). Both preserved | UNCORROBORATED | PC-09; PC-26 | Q030, Q031 |
| REC-BSET-18 | C18 | Abstract KPI provider with empty hook / HIGH | VERIFIED | MATCH | Re-read (PC-17) | NOT_APPLICABLE | PC-17 | Q030 |
| REC-BSET-19 | C19 | Visual-effect flag seeded non-updatable, internal sessions only / MED | VERIFIED | MATCH | Re-read (PC-14) | NOT_APPLICABLE | PC-14 | — |
| REC-BSET-20 | C20 | Profiling-until is a settings-bound parameter; enforcement elsewhere / LOW | VERIFIED | MATCH | Re-read (PC-15); enforcement location carried as REC-BSET-34 | UNCORROBORATED | PC-15 | Q025 |
| REC-BSET-21 | C21 (+F7) | Counters privileged across all companies / MED | VERIFIED | MATCH | Re-read (PC-15) | UNCORROBORATED | PC-15 | Q017 |
| REC-BSET-22 | C22 | No scheduled jobs / HIGH | VERIFIED | MATCH | Manifest data list re-read (PC-01) | NOT_APPLICABLE | PC-01 | — |
| REC-BSET-23 | X-BSET-03 | KPI last-login (log rows) vs auth_signup login-date field — CANDIDATE | RESOLVED — both derive from log rows | MATCH | A1 raised a candidate only; A2 resolution supported by core read (auth_signup PC-ASGN-11) | UNCORROBORATED | PC-ASGN-11 | Q020 |
| REC-BSET-24 | O1 / F3 (HIGH) | (C07 stated groups only) | O1 HIGH — bulk-invite reactivation restores groups **and** revives unexpired API keys, with no invitation | UNKNOWN_PENDING_PROOF | Key check requires only owner active, unexpired, scope unset or remote-call; keys are removed only on self-deletion or expiry GC, not on archive (PC-06 PASS). Runtime PR-BSET-07 | UNCORROBORATED | PC-06; PC-24 | Q011 |
| REC-BSET-25 | O2 | (not stated) | O2 MED — reactivated users receive no invitation / notification | UNKNOWN_PENDING_PROOF | Cross-module: auth_signup re-invite search excludes archived users; reactivation is not a create (auth_signup PC-ASGN-19 PASS). Runtime PR-BSET-07 | UNCORROBORATED | PC-ASGN-19; PC-24 | Q011, Q012 |
| REC-BSET-26 | O3 / F1 (HIGH) | (C15 stated no role check) | O3 HIGH — KPI key check: no role/share check on owner; accepts no-scope keys; portal keys may pass | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-07 PASS). Portal keys are creatable only when the portal module's allow-keys parameter is set (PC-07 observation). Runtime PR-BSET-01, PR-BSET-02 | UNCORROBORATED | PC-07; PC-18, PC-19 | Q019, Q027, Q033 |
| REC-BSET-27 | O4 | (C17 installed-only) | O4 MED — KPI providers loaded from all addons on the path, not installed-only | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-09 PASS). Execution against a DB where the addon is not installed is runtime (PR-BSET-09) | UNCORROBORATED | PC-09; PC-26 | Q030, Q031 |
| REC-BSET-28 | O5 / F5 | (not stated) | O5 MED — no database-filter enforcement in KPI path; timing side channel | UNKNOWN_PENDING_PROOF | No DB-filter reference in the module path (PC-16 PASS). Runtime PR-BSET-03, PR-BSET-04 | UNCORROBORATED | PC-16; PC-20, PC-21 | Q027, Q028 |
| REC-BSET-29 | O6 / F4 | (not stated) | O6 MED — bulk invite can create a second identity with an e-mail already held by an active user whose login differs | UNKNOWN_PENDING_PROOF | No active-user e-mail check in bulk invite (PC-05 PASS). Runtime PR-BSET-08 | UNCORROBORATED | PC-05; PC-25 | Q010, Q012 |
| REC-BSET-30 | O7 / F2 | (C11) | O7 MED — demo-status protection is ACL-implicit | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-10). Runtime PR-BSET-05 | UNCORROBORATED | PC-10; PC-22 | Q018 |
| REC-BSET-31 | G2 | Controller-level cursor binding not verified | Open | GAP | Not read | NOT_APPLICABLE | — | — |
| REC-BSET-32 | G3 (partial) | Base settings machinery beyond save not analysed | Partially read (save only) | GAP | Install/implied-group mechanics not read | NOT_APPLICABLE | — | — |
| REC-BSET-33 | G5 | Static JS (invite widget) not reviewed | Open | GAP | Out of scope | NOT_APPLICABLE | — | — |
| REC-BSET-34 | G7 | Profiling expiry enforcement location not identified | Open | GAP | Not in fetched files | NOT_APPLICABLE | — | — |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 13 | C01, C02, C04, C08, C09, C12, C13, C18, C19, C20, C21, C22, X-BSET-03 |
| CONTRADICTION | 5 | C03, C06, C10, C11, C17 (all A1 vs A2) |
| UNKNOWN_PENDING_PROOF | 12 | C05, C07, C14, C15, C16, O1, O2, O3, O4, O5, O6, O7 |
| GAP | 4 | G2, G3 (partial), G5, G7 |
| **Total** | **34** | 22 A1 claims + 1 A1 contradiction candidate + 7 A2 omissions + 4 carried gaps |

Lane B: UNCORROBORATED 25, NOT_APPLICABLE 9 (C01, C04, C18, C19, C22, G2, G3, G5, G7). No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- C11 / X-BSET-01: A1 claimed exposure to any logged-in user; A2 NOT_VERIFIED — non-administrators receive an access error. The Stage-2 static read supports A2 (PC-10). REC does not rewrite A1; the item stays CONTRADICTION for A3, with runtime confirmation pending (PC-22).
- C03, C06, C10, C17: A2 narrowed scope or corrected attribution; static re-read supports A2 in each (PC-03, PC-05, PC-11, PC-09).
- X-BSET-02 (C12) and X-BSET-03: resolved by A2 core reads; classified MATCH, not CONTRADICTION.
- A2 HIGH items O1 (reactivation) and O3 (KPI key) are not reviewer disagreements; they are carried as UNKNOWN_PENDING_PROOF with static basis confirmed.

## 3. QID lineage map (frozen bank; lineage only, not answers)

Join key: MODULE `base_setup` + QID + freeze hash `9e31f2d27dfb959e555cf8ff117d829969e8122fe5e5544bbaf737b6ddea0377`. Mapping = topical relevance only.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-BASE_SETUP-Q001 | Global settings restricted to administrators | REC-02 (C02) |
| G01-BASE_SETUP-Q002 | Company-context save isolation | REC-03 (C03) |
| G01-BASE_SETUP-Q004 | Install decision before activation | REC-04 (C04) |
| G01-BASE_SETUP-Q007 | Default access template controlled | REC-05 (C05) |
| G01-BASE_SETUP-Q009 | Default-access change auditable | REC-05 (C05) |
| G01-BASE_SETUP-Q010 | Bulk creation normalisation / duplicates | REC-06 (C06), REC-29 (O6) |
| G01-BASE_SETUP-Q011 | Reactivation does not restore stale privileges | REC-06, REC-07 (C07), REC-24 (O1), REC-25 (O2) |
| G01-BASE_SETUP-Q012 | Mixed-input bulk outcome deterministic | REC-25 (O2), REC-29 (O6) |
| G01-BASE_SETUP-Q014 | Prerequisite absent → fail closed | REC-08 (C08) |
| G01-BASE_SETUP-Q017 | Counts identified as system-wide vs local | REC-12 (C12), REC-21 (C21) |
| G01-BASE_SETUP-Q018 | Endpoint authorisation equals visible settings | REC-09 (C09), REC-11 (C11), REC-30 (O7) |
| G01-BASE_SETUP-Q019 | Setup data minimises identity details | REC-09 (C09), REC-15 (C15), REC-26 (O3) |
| G01-BASE_SETUP-Q020 | Active vs never-logged-in rule | REC-10 (C10), REC-12 (C12), REC-23 (X-BSET-03) |
| G01-BASE_SETUP-Q022 | Environment/demo indicators | REC-11 (C11) |
| G01-BASE_SETUP-Q023 | Footer/layout company isolation | REC-03 (C03) |
| G01-BASE_SETUP-Q025 | Profiling expiry | REC-20 (C20) |
| G01-BASE_SETUP-Q027 | Per-database authentication | REC-14 (C14), REC-15 (C15), REC-26 (O3), REC-28 (O5) |
| G01-BASE_SETUP-Q028 | No existence disclosure on failed auth | REC-14 (C14), REC-28 (O5) |
| G01-BASE_SETUP-Q029 | Version mismatch rejected | REC-14 (C14) |
| G01-BASE_SETUP-Q030 | Provider isolation | REC-16 (C16), REC-17 (C17), REC-18 (C18), REC-27 (O4) |
| G01-BASE_SETUP-Q031 | Providers observational only | REC-16 (C16), REC-17 (C17), REC-27 (O4) |
| G01-BASE_SETUP-Q032 | Unauthenticated request bounded | REC-13 (C13) |
| G01-BASE_SETUP-Q033 | Remote-call-scoped credentials only | REC-15 (C15), REC-26 (O3) |
| G01-BASE_SETUP-Q036 | Save cannot bypass install authority | REC-04 (C04) |
| G01-BASE_SETUP-Q041 | Configuration actions attributable | REC-05 (C05) |

**Mapped: 25 QIDs.** **No evidence yet: 16 QIDs** — Q003 (save resets unrelated settings), Q005 (no-op save triggers install), Q006 (disabled capability leaves stale access), Q008 (default-access change not retroactive), Q013 (concurrent creation), Q015 (implied-group toggles scope), Q016 (company-limited admin and broad groups), Q021 (demo data loading explicit), Q024 (template-edit authority), Q026 (diagnostics authority), Q034 (telemetry failure details secrets), Q035 (post-save readiness status), Q037 (anti-abuse config validation), Q038 (integration secrets not exposed), Q039 (atomic configuration change), Q040 (idempotent retry of admin save). No mapping answers a QID. Note: the auth_signup REC item REC-ASGN-25 (unrelated settings save persists a sign-up policy) is topically adjacent to Q003 but belongs to MODULE `auth_signup`; per the MODULE+QID join key it is not mapped here.

## 4. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_BASE_SETUP_PROOF_20260927.md`.
- Proof must address the 12 UNKNOWN_PENDING_PROOF items and the 5 CONTRADICTION items. The 4 GAP items are carried forward.

## 5. Limitations

- REC used only the immutable inputs in 0.1 and, for classification support, the static proof results from Stage 2. No runtime evidence exists.
- Other installed modules may widen the module-registry ACL (affects C11) or add archive/reactivation hooks (affects C07/O1).
- QID mapping is topical lineage judged by this controller; not a coverage measure. No Formal Coverage claim. No percentages.
