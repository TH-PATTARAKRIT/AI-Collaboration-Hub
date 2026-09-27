# G01 PLATFORM_BASE — RED TEAM A1 Package — `base`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `base` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `9108bd4f64762c79f763a35c9d6e944153bd7eec5c0fad3bda9d0eadcd59403b` |
| Carried-forward delta | `A1_SOURCE_EVIDENCE_LANE/G01_G04_RED_TEAM_STATIC_CHECKPOINT_R14_20260925.md` (G01 section only), sha256 `3c3f0bd038fffb2ddf11016c6c25ddcc96066c6124557967b03c0541becdf883` |
| Cross-link (read-only) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_AUTOMATION_A1_PACKAGE_20260927.md`, sha256 `f01dec29aeb323747b288b4ef3687acad4e5deefdddc10d7422fa4fac6297007` (not edited) |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `odoo/addons/base/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_GMVQ_MVQ_50_V1.00_DRAFT.md`, sha256 `b242fa0e98aeedd12b5ae33aa9800a1831a795222052f87621960d4d9aed8777` (matches `FREEZE_W1-B01.json` bank entry) |
| Freeze | batch W1-B01, freeze hash `558ec88047aef5c8e7ea0e2675b1c43ef358ec29b172d6878068330f3fba7177`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B; no runtime evidence consumed |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. Nothing here recommends reusing vendor schema, ORM, workflow, UI or naming. No QIDs are answered. The bank was used only to decide which topics matter: cross-scope contamination, privilege timing at execution, actor identity for background work, credential lifecycle, cache staleness, failure semantics and configuration drift.

Evidence key (blob SHA-1 from the Lane A packet; paths under `odoo/addons/base/`): E1 `__manifest__.py` 5250c852…; E3 `models/res_users.py` 9d42d77a…; E4 `models/res_company.py` 86aa2fb0…; E5 `models/res_partner.py` 502616ef…; E6 `models/res_groups.py` e69accc2…; E8 `models/ir_model.py` ca0c48b5…; E9 `models/ir_rule.py` e64f4e2c…; E10 `models/ir_cron.py` e8762b92…; E11 `models/ir_config_parameter.py` 21c82bf6…; E12 `models/ir_actions.py` 45d06ee4…; E13 `models/ir_http.py` d9d2a00b…; E15 `models/res_users_deletion.py` d6c1118d…; E17 `security/base_groups.xml` 2cd6d3d4…; E18 `security/base_security.xml` 63195795…; E19 `security/ir.model.access.csv` 29785e02…; E20 `data/ir_cron_data.xml` 0676236b…. R14 = carried-forward delta (ir_attachment 905ae118…, ir_sequence 920e0b23…, res_currency 015ca783…, res_lang 563b4eff…).

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-BASE-C01 | WHAT: `base` is the kernel module: hidden, auto-installed, no declared dependencies, LGPL-3, with a post-init hook. Groups and record rules load before views; the model ACL list loads last. WHY: later data refers to earlier groups/models. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C02 | WHAT: Access is two-layered: a model-level permission list, then record-level rules. Superuser mode skips both layers (model check returns allowed; rule lookup returns no rules). RISK: any code path that elevates silently removes both layers. | E8, E9 (S1, S7) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C03 | WHAT: Model-level permission is the union of active rows that grant the mode and either name no group or a group the user holds (implied groups included); results are cached per user and mode and cleared when permission rows or user groups change. Group-less granting rows raise a deprecation warning. RISK: stale-cache windows between change and clearing are not evidenced as impossible. | E8, E3 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C04 | WHAT: Record-rule composition: rules for the model and mode are split into global rules (no groups) and group rules (only those whose groups intersect the user's effective groups). Effective filter = every global rule AND (OR of applicable group rules). Inactive rules and rules without the mode flag are ignored. WHY: global rules are hard walls; group rules are alternative grants. RISK: one broad group rule (e.g. an "all records" rule) overrides every narrower group rule for its holders, but never a global rule. | E9 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C05 | WHAT: Rules of delegated parent models are ANDed into the child model's filter through the delegation link, but only when that link is stored. | E9 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C06 | WHAT: Rule expressions are evaluated with three inputs: the current user (context-free), the set of companies the user has currently activated (described in source as filtered and trusted), and the current single company. WHY: rules follow the active company selection, not the full allowed set. RISK: the trust in the activated set depends on filtering done in ORM core (G1). | E9 (S1) | HIGH (inputs) / LOW (filtering) | SOURCE-STATIC |
| A1-G01-BASE-C07 | WHAT: The computed rule filter is cached by user, superuser flag, model, mode and the active-company context; caching is disabled in one developer mode. Creating, editing or deleting a rule clears the registry cache. RISK: correctness of company switching depends on the context key being present and consistent. | E9 (S1) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C08 | WHAT: Denial diagnostics treat all applicable group rules as one block and each global rule separately; the denial is logged with operation, first ids, user and model. | E9 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C09 | WHAT: Rules cannot target the rule model itself, need at least one mode, and are domain-validated at save. | E9 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C10 | WHAT: Shared master data (partners, partner bank accounts, currency rates) use global rules with ancestor semantics: visible when owned by no company or by a company that is an ancestor of (or equal to) an activated company. WHY: branches see parent-company master data. RISK: a parent company does not see a branch's records unless the branch is also activated. | E18 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C11 | WHAT: The global partner rule additionally exempts partners not flagged as shared (per source comment: partners of internal users), so those are visible regardless of company. WHY: avoid users becoming unselectable. RISK: internal-user contact data is cross-company visible by design. | E18 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C12 | WHAT: Company records are protected only by group rules: internal, portal and public roles see activated companies; the access-rights manager role sees all. Because group rules OR together, the manager rule wins for holders. The users model has a global rule: internal users always visible; share users only when they belong to an activated company. | E18 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C13 | WHAT: Portal/public users are further limited by group rules to partners within their own commercial entity; portal users to users of their commercial entity. These AND with the global partner/user rules. | E18 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C14 | WHAT: A branch-resolution helper returns a company's branches intersected with the activated set; in superuser contexts it walks the hierarchy with elevation. | E4 (S8) | MED | SOURCE-STATIC |
| A1-G01-BASE-C15 | WHAT: Company hierarchy is fixed after creation; duplication is forbidden; archiving cascades to branches; a company that is the default of active users cannot be archived; root-delegated values (currency) are forced identical on branches. | E4 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C16 | WHAT: User invariants: unique login; default company within allowed companies; at most one user-type role (internal/portal/public); at least one administrator; superuser cannot be activated; self cannot be deactivated; admin, template and public users cannot be deleted. | E3, E6 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C17 | WHAT: A user editing only self-editable fields is elevated for that write; a self-chosen default company outside allowed companies is dropped silently. RISK: silent correction, no user-visible error. | E3 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C18 | WHAT: The multi-company group is added/removed automatically according to the count of allowed companies. | E3 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C19 | WHAT: Passwords are stored as slow salted hashes with a floor on rounds (configurable upward); plaintext rows are rehashed at init; empty passwords are rejected; own password changes go through a wizard. | E3 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C20 | WHAT: Login throttling is keyed on source address, held in the worker's in-memory registry, and applies only inside an HTTP request; after N failures further attempts are ignored for D seconds (both configurable; N=0 disables). A warning is logged when the throttled address is private (possible proxy). RISK: per-worker, non-shared, and bypassed outside HTTP; proxy misconfiguration collapses all users to one address. | E3 (S5) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C21 | WHAT: Sensitive self-service actions require a password re-check within the last 10 minutes held in the session, and are refused outside HTTP. | E3 (S5) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C22 | WHAT: API keys are random, stored only as a salted hash plus a short clear prefix used as lookup index, bound to one user and an optional scope (no scope = any RPC). WHY: key recovery from storage is infeasible; lookup is fast. RISK: the hash uses a deliberately low round count justified by key randomness. | E3 (S5) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C23 | WHAT: Key expiry is required for non-administrators, capped by the highest duration across the user's groups (internal role seeds 90 days), and cannot be in the past. Administrators or elevated contexts may create non-expiring keys. Programmatic creation needs administrator or an explicit parameter, with a per-user count limit. | E3 (S5), E6, E17 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C24 | WHAT: At verification time a key is accepted only if its owner is active, its scope is empty or matches, and it is not expired; expired keys are purged by the periodic vacuum. Removal is limited to the owner or a system user and clears caches. RISK: persistent administrator-created keys never expire. | E3 (S5) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C25 | WHAT: HTTP route authentication levels: none (no user), public (falls back to the public user), user (rejects anonymous and public users), bearer (API key in header; must match any session user; makes the session stateless; without a key, cookie use needs browser navigation headers). CORS preflight is always treated as "none". An invalid session is logged out and the request continues anonymously before the level check. Unexpected authentication errors become access denied. | E13 (S6) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C26 | WHAT: Server-action execution gate: if the action names groups, the caller must hold one and no record-level check follows; otherwise the caller needs model write permission and write-rule access to the real target records. Actions with warnings refuse to run; code is safety-checked at save. RISK: a group-restricted action skips per-record write checks entirely. | E12 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C27 | WHAT: Server-action identity: the evaluation environment and the gate use the environment of whoever calls run; the action record is then elevated to execute. Code actions execute with the caller's environment. Update, create and duplicate actions (and value sequences) execute through the elevated action environment, i.e. in superuser mode after the caller-level gate passed. Multi-action children are invoked from the elevated parent, so their gate and code run in superuser mode. Elevation keeps the user id, so audit fields and the "user" input name the caller. RISK: effects beyond the caller's record rules once the gate passes. | E12 (S3) | HIGH (source path) | SOURCE-STATIC |
| A1-G01-BASE-C28 | WHAT: The outbound-webhook action reads the selected fields of the target record through the elevated action environment and posts them after commit (cancelled on rollback), fire-and-forget with a 1-second timeout. RISK: fields outside the caller's read rights may leave the system; failures are only logged. | E12 (S3) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C29 | WHAT: Scheduled jobs run as their configured scheduler user (default creator), not in superuser mode at entry; the job's server action is called unelevated, so the gate applies to that user. RISK: the scheduler user is an admin-set field; identity of background effects equals whoever it names. | E10 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C30 | WHAT: Job acquisition uses row locks with skip-locked selection so parallel workers do not double-run; editing or deleting a running job and manual re-run of an executing job are refused. Ready jobs are ordered by failure count, priority, id. | E10 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C31 | WHAT: A run loops at least 10 iterations or 10 seconds while progress is committed; three consecutive timeouts count as one failure; a job is deactivated only after at least 5 consecutive failures AND more than 7 days since the first, with an admin notification; fully- or partially-done runs reset the counters. Module version mismatch defers execution up to 5 hours. Callback failure rolls back and re-raises. | E10 (S4) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C32 | WHAT: Rescheduling preserves wall-clock hour across DST in the user's time zone; enabling jobs is suppressed on neutralized databases. | E10 | MED | SOURCE-STATIC |
| A1-G01-BASE-C33 | WHAT: Reading a system parameter checks read permission (administrator only), then serves a cached value; framework code commonly reads parameters elevated. Database secret, uuid and creation date cannot be renamed or deleted. RISK: every elevated reader bypasses the parameter ACL. | E11 (S7), E19 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C34 | WHAT: Key ACLs: scheduler, server actions and system parameters are administrator-only; permission rows, rules, groups, users, companies and model registry are managed by the access-rights manager; partner writes need the contact-creation group; API-key rows readable by internal/portal users but rule-limited to own keys (public none). | E19, E18 (S2) | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C35 | WHAT: Seeded daily jobs: internal auto-vacuum and deferred portal-user deletion in batches of 50. | E20, E15 | HIGH | SOURCE-STATIC |
| A1-G01-BASE-C36 | WHAT (R14 delta, by pointer): attachments — admin-only storage migration, sanitised paths, locked GC, XML-like uploads downgraded for users without view-write, access follows the referenced record; sequences — no sudo commands, gapless variant uses row locking, company/date-range scoped; currencies — unique code, multi-currency group auto-toggle, rates from global or root-company records; languages — unique codes, at least one active. | R14 (not re-researched) | HIGH (R14 verified) | SOURCE-STATIC |

## 2. Business rules
- BR1: Every access decision = model permission AND (global rules AND OR-of-group-rules), unless superuser mode (C02, C04).
- BR2: Company visibility is driven by the activated company set; shared data use ancestor-or-empty semantics (C06, C10).
- BR3: Company records are visible to all only for access-rights managers (C12).
- BR4: A user holds exactly one user-type role at most and needs a default company within allowed companies (C16).
- BR5: Non-admin API keys always expire within the group-derived cap; verification re-checks expiry and owner activity (C23, C24).
- BR6: Server actions gate at the caller, then execute object mutations elevated (C26, C27).
- BR7: Scheduled work runs as the configured user and is single-runner per job (C29, C30).

## 3. States / transitions
- API key: generated (hash stored) → active → expired (rejected at check) → purged by vacuum; or removed by owner/system (C22–C24).
- Scheduled job: inactive ↔ active; ready → acquired (row lock) → running (progress commits) → done / partially done (counters reset) / failed (counter +1) → auto-deactivated after 5 failures over >7 days (C30, C31).
- Company: created (hierarchy fixed) → active → archived (branches archived; blocked if default of active users) (C15).
- Session: valid → invalid (logout, continue anonymous) → route level decides (C25). Identity re-check: fresh for 10 minutes (C21).
- Login throttle: normal → cooldown after N failures → normal after D seconds or success (C20).

## 4. Exceptions / failure modes
- F1: Throttle state is per worker and lost on restart; non-HTTP authentication is not throttled (C20).
- F2: Self-service default-company outside allowed set is dropped without error (C17).
- F3: Group-restricted server action skips record-level write checks (C26).
- F4: Webhook action failure/timeout is only logged; effects may be uncertain after 1 second (C28).
- F5: Scheduled job failure rolls back its own transaction; already-committed progress batches stay (C31).
- F6: Unexpected errors during authentication collapse to access denied (C25).

## 5. Cross-module handoffs
| Edge | Nature | Claim |
|---|---|---|
| base_automation | Execution substrate and final action identity — see CRQ-01 disposition below | C26, C27, C29 |
| web / http_routing / core HTTP layer | Route auth levels; session validity is decided outside the module path (G2) | C25 |
| portal / auth_signup | Portal template user parameter; deferred portal-user deletion job | C35 |
| mail, digest, resource, all business modules | Partner/user/company models are the tenancy anchor; ancestor rules shape visibility | C10–C13 |
| l10n groups (outside G01) | Company creation may auto-install localisations | Lane A item 41 |

**base_automation CRQ-01 disposition: NARROWED (not CLOSED).** Static base evidence (C27, S3) fixes the rule: whoever calls run determines the gate and code-action environment; object mutations always run elevated; uid is preserved. The base_automation package (C11, spot-checked S3 there) records that its action iteration runs elevated. Combined, event-triggered rules would execute code actions in superuser mode under the triggering uid, and time-based rules under the scheduler job's configured user with elevated iteration. Remaining open for runtime proof: actual call-site environment per trigger type (UI change, message, webhook — webhook route runs without a user), whether any path calls run unelevated, and whether a non-privileged trigger can obtain effects above its own rights. Not CLOSED because no runtime evidence and the call site was not re-fetched here.

## 6. Evidence gaps
- G1 (carried): ORM core (company-consistency enforcement, activated-company derivation, elevation semantics) outside module path.
- G2 (carried): session check and token handling in core HTTP/security modules not read.
- G3 (Lane A) — CLOSED by spot-check: the API-key credential helper is defined inside E3 and enforces expiry, scope and owner-active at check time (C24).
- G4: views, wizards, menus, module lifecycle, mail servers, filters, defaults, reports and tests not read (Lane A G5).
- G5: whether the partner "shared" flag is exactly "not linked to an internal user" is taken from a source comment; its compute in E5 was not re-read.
- G6: no evidence of how rule/ACL cache clearing propagates across workers in multi-process deployments.
- G7: scheduler user eligibility (e.g. whether a portal or inactive user can be set) not evidenced.

## 7. CRQ candidates
| CRQ | Question | Basis |
|---|---|---|
| BASE-CRQ-01 | At runtime, do update/create/duplicate server actions write records the caller cannot write under record rules, once the gate passes? | C26, C27 |
| BASE-CRQ-02 | Do multi-action children run code in superuser mode for a non-admin caller? | C27 |
| BASE-CRQ-03 | Can a group-restricted server action be used to modify records outside the caller's rule scope? | C26 |
| BASE-CRQ-04 | Does the outbound-webhook action send field values the caller cannot read? | C28 |
| BASE-CRQ-05 | After switching the activated company set, are rule results and parameter caches refreshed immediately in every worker? | C07, C33, G6 |
| BASE-CRQ-06 | Does a parent company user miss branch-owned partner/bank/rate records unless the branch is activated? | C10 |
| BASE-CRQ-07 | Can login throttling be bypassed across workers or via non-browser channels? | C20 |
| BASE-CRQ-08 | Are expired API keys rejected immediately (before vacuum) on bearer routes and RPC? | C24, C25 |
| BASE-CRQ-09 | Under concurrent workers, is any scheduled job ever run twice, and does auto-deactivation fire only after both thresholds? | C30, C31 |
| BASE-CRQ-10 | Which user identity is recorded on records created by scheduled jobs and elevated server actions? | C27, C29 |

## 8. Contradictions
| ID | Statement | Status |
|---|---|---|
| X1 | Lane A G3 states the API-key credential helper is imported from outside scope and expiry at check time is unverified. Source at E3 defines the helper locally and checks expiry, scope and owner activity. | **CONFIRMED** (S5) — Lane A gap superseded |
| X2 | Lane A item 35 says success resets failure counters; source also resets on partially-done runs. | CONFIRMED refinement (S4), not a conflict of substance |
| X3 | Lane A item 39 says bearer needs a "global scope" key; source accepts empty scope or a literal matching scope, commented as effectively global. | CONFIRMED refinement (S6) |
| X4 | Lane A item 14 does not state that throttling is skipped outside HTTP requests; source skips it. | CONFIRMED refinement (S5) |

## 9. Spot-check log
Each file fetched from `raw.githubusercontent.com/odoo/odoo/8d05257d…/odoo/addons/base/<path>`; `git hash-object` run on the local copy (scratchpad only).
| # | Path | Recorded blob | Computed blob | Result | Claims checked |
|---|---|---|---|---|---|
| S1 | `models/ir_rule.py` | e64f4e2c… | e64f4e2c88209836d39f2bfe163469def41b71c0 | MATCH | C02, C04–C09: global AND / group OR; superuser returns no rules; eval inputs; cache key; delegated parents |
| S2 | `security/base_security.xml` | 63195795… | 63195795684ed8d3c873e6a5a67324dd07482333 | MATCH | C10–C13, C34: ancestor-or-empty globals; partner exemption; company group rules; users global rule |
| S3 | `models/ir_actions.py` | 45d06ee4… | 45d06ee4210b6e5559c6c96ab82ddc238a891a52 | MATCH | C26–C28: gate, caller env for code, elevated object ops, multi children, webhook read |
| S4 | `models/ir_cron.py` | e8762b92… | e8762b920da6a68fd655dccf1a936671838c561d | MATCH | C29–C31: run as job user, skip-locked, thresholds, reset on partial |
| S5 | `models/res_users.py` | 9d42d77a… | 9d42d77ae8ec19028c99b3c668294569ded3a86a | MATCH | C20–C24, X1, X4 |
| S6 | `models/ir_http.py` | d9d2a00b… | d9d2a00b9bc7d3e7f439b7ff4ecc46488876953a | MATCH | C25, X3 |
| S7 | `models/ir_model.py`, `models/ir_config_parameter.py` | ca0c48b5…, 21c82bf6… | ca0c48b566843ece9948c8c5e7f759714a3faf8e, 21c82bf62ed0fec4b4307c935f8a2b4ebaff4321 | MATCH | C02 superuser bypass; C33 read check before cache |
| S8 | `models/res_company.py`, `models/res_groups.py` | 86aa2fb0…, e69accc2… | 86aa2fb0f6974bdf0f541efb2c871b37a43c140c, e69accc22b676fccb5d0372e5312f259b1599f6b | MATCH | C14 branch helper; C23 duration non-negative constraint |

## 10. Provenance
- Inputs: Lane A packet and R14 G01 section (sha256 above); R14 delta incorporated by pointer only (C36), not re-researched.
- base_automation A1 package read only for CRQ-01 cross-link; not edited.
- Bank consulted read-only for topic salience; bank sha256 matches the W1-B01 freeze entry; no QID answered; no bank edited.
- No Lane B material viewed. No git operations performed. Spot-check copies held in the session scratchpad only.

## 11. Limitations
- SOURCE-STATIC only. Source presence does not prove runtime reachability; overriding modules (2FA, mail, portal) may change identity and credential behaviour.
- CRQ-01 disposition is a static narrowing; no privilege-escalation conclusion is asserted without runtime proof.
- Large files were read selectively around cited behaviour; unlisted methods are not analysed.
- No Formal Coverage claim is made, and there are no percentages.
