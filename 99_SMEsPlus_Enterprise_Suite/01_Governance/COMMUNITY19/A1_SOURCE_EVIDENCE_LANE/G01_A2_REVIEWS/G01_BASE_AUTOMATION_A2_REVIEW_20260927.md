# G01 PLATFORM_BASE — RED TEAM A2 Review — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions). Independent of A1; A1 package not repaired or rewritten |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| A1 package (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_BASE_AUTOMATION_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `f01dec29aeb323747b288b4ef3687acad4e5deefdddc10d7422fa4fac6297007` |
| Lane A packet (input, immutable) | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_AUTOMATION_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `8656751d9142e0b59c433454558cef5e57b7c4f089bf42c04cf2a280b18ec058` — matches the value recorded in the A1 header |
| Question bank (topic lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_AUTOMATION_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `3c38cec4aa1ef2aa92d0e850da0d18242da9dc7c6ef7bd137c433edb379b9a49` (W1-B02 ELIGIBLE). No QID answered |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/base_automation/` (raw.githubusercontent.com) |
| Predeclared test plan | scratchpad `a2_baut/test_plan_predeclared.txt`, sha256 `3f1c8c24df5134469ea3618e9bd435057065c5cf0cf22a0b8049de5a6f75aa0d`, written 2026-09-27 14:51 UTC before any source re-read |
| Lane B | No Lane B runtime evidence exists for this module. Not treated as a failure (see section 5) |
| Date | 2026-09-27 |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. All 24 A1 claims were re-read against source. 22 are VERIFIED and 2 are PARTIAL (C12, C19). None is NOT_VERIFIED, and no claim overstates its source enough to require a return to A1.
2. The C24 contradiction candidate is confirmed at source-path level. Its practical effect remains a runtime question.
3. A1 omitted several important behaviours of an ERP automation engine. The most important are O1 (the webhook endpoint does not check the trigger type), O2 (a time-based rule's first run catches up over all history), O3 (one failing record stalls a time-based rule) and O6 (the webhook record lookup runs as superuser with a caller-chosen model). These are A2 findings routed to Reconciliation/Proof. They are not A1 defects that block handoff.
4. Several A1 gaps are partly settled by the source (G7, G10, G11, CRQ-03, CRQ-09). The details are in section 2b.

Clean-room note: every statement below is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced and nothing is recommended for reuse. No percentages. No Formal Coverage claim. No git operations were performed; source copies are held in the scratchpad only.

## 1. Test plan (predeclared, executed as declared)

| Test | Scope | Method | Result |
|---|---|---|---|
| T1 Lineage | A1 package, Lane A packet, bank | sha256 of each file; compare A1's recorded Lane A hash | PASS — hashes recorded above; Lane A hash matches A1 header |
| T2 Blob integrity | E1, E4, E5, E7, E8, E9, E10, E11, E12 | fetch at anchor; `git hash-object` vs Lane A table | PASS — 9 of 9 blobs match the recorded SHA-1 (E2, E3, E6 are loader stubs and were not re-fetched) |
| T3 Semantic re-read | All HIGH claims (C01, C02, C04–C17, C20–C24) and MED claims (C03, C18, C19) | Full read of E4 (both halves), E5, E7, E8, E9, E10; targeted read of E11 domain-editor and webhook sections; string search for `sms`, ordering and company attributes | Done — verdicts in section 2 |
| T4 Contradiction CRQ-02 / C24 | Message-post path, pre-condition compute, view visibility | Trace which conditions the message path evaluates; check whether the apply-on condition is reached by any other route; check which editors each UI mode shows | Done — confirmed (section 2, C24) |
| T5 CRQ static resolvability | CRQ-01 … CRQ-10 | For each, check whether the source settles it (identity, copy flags, ordering attribute, company field, tracking attributes, rotation, cron re-check) | Done — section 2b |
| T6 Business semantics and omissions | Trigger semantics, recursion, time triggers, webhook security, execution identity, audit | Adversarial re-read of all execution paths (create, write, recompute, unlink, onchange, message, webhook, cron) | Done — sections 3 and 4 |
| T7 Lane B classification | Every claim | Label NOT_APPLICABLE / UNCORROBORATED / MISSING_REQUIRED_RUNTIME_PROOF | Done — section 5 |

## 2. Claim verdict table

Verdict key: VERIFIED = a source re-read supports the claim as written. PARTIAL = the core is supported, but part of the claim is inaccurate or its scope is materially incomplete. NOT_VERIFIED = the source does not support the claim. OUT_OF_SCOPE = the claim cannot be judged within module scope.

| Claim | A1 conf. | A2 verdict | A2 basis (source re-read, paraphrased) |
|---|---|---|---|
| C01 | HIGH | VERIFIED | The rule's target-model field accepts only non-abstract models. Its trigger set covers record events, time, messages, UI change and webhook. The manifest describes automation for any object. |
| C02 | HIGH | VERIFIED | The manifest declares base, digest, resource, mail and sms. A search of all nine fetched files finds `sms` only in the manifest. The JS assets remain unchecked (A1 G1). |
| C03 | MED | VERIFIED | The rule inherits the chatter and activity mixins. Tracking is declared on name, target model, trigger, date field, delay amount, delay mode and delay unit. See O12: the source settles the untracked-field question. |
| C04 | HIGH | VERIFIED | 18 trigger values, grouped exactly as A1 lists them. The update trigger is marked deprecated. |
| C05 | HIGH | VERIFIED | The resolver looks up the conventional name or the customization-prefixed name and keeps the first match. With no match it returns an empty set, so the generated condition is empty and the watched-field set is empty. An empty watched-field set means "watch all fields" (see section 3, S2). |
| C06 | HIGH | VERIFIED | Create, write, recompute, unlink and message-post are patched, and onchange hooks are appended. Rule create and unlink always re-register. Refinement: a rule write re-registers only when model, active, trigger or on-change fields change, and re-registration is skipped entirely under a file-import context (O9). |
| C07 | HIGH | VERIFIED | Write and recompute paths: the before-condition is evaluated before the change and the apply-on condition after it. Create and unlink paths: apply-on only. Watched-field comparison uses the old values of the written stored fields; on create every field counts as changed. Refinement: on delete, the actions run before the record is removed (O8). |
| C08 | HIGH | VERIFIED | The path skips internal messages, internal subtypes and the notification, auto-comment and user-notification message types. The message is classed "received" when it has no author or the author is a share partner, and "sent" otherwise. |
| C09 | HIGH | VERIFIED | The guard is a context map from rule to processed records, marked before execution, with an in-place feedback mode for filter-time recomputes. It is per rule and per call chain, with no cross-transaction store. Refinement: message-trigger suppression is broader than "while any rule is running" (O7). |
| C10 | HIGH | VERIFIED | Each action runs per record with active-model and active-id context and the post-condition passed along. The loop runs every record for one action before moving to the next action. The optional last-automation timestamp is written before the actions run (O16). |
| C11 | HIGH / LOW | VERIFIED | Rule lookup, filter evaluation and the action list all run elevated, and the action records handed to execution carry the superuser flag. Refinement: in the webhook path the rule is loaded elevated, so the record-getter evaluation and the record lookup also run elevated. The user seen by expressions is the triggering or public user (O6). Final execution identity stays in base, so the LOW confidence on that part stands. |
| C12 | HIGH | **PARTIAL** | The filter and record-getter evaluator exposes date/time helpers, uid, user and model, plus the payload for webhooks: verified. Inaccurate scope: the JSON helper and the request payload are added only for code-type actions, and the payload is added whenever *any* HTTP request is active and carries JSON or query data, not only for webhook calls (O5). |
| C13 | HIGH | VERIFIED | Field names are extracted by pattern matching. An in-source comment gives the reason: the method sits on a compute path reachable from crafted onchange calls. |
| C14 | HIGH | VERIFIED | The route is public, unauthenticated, CSRF-exempt and session-less, and accepts GET and POST. It looks the rule up elevated by identifier. Responses are a generic status with 404, 500 or 200. The identifier is random per rule, not copied on duplication, and has a rotate action. Material omission (O1): the lookup does not check that the rule's trigger is webhook. It checks only the identifier and (through default active filtering) that the rule is active. |
| C15 | HIGH | VERIFIED | When logging is enabled, the log store receives an entry for every call that reaches a rule (containing the payload), plus error entries with tracebacks. The writes run elevated. No retention logic exists in the module. The payload is also always sent to the debug-level application logger. |
| C16 | HIGH | VERIFIED | There is one ACL row, for the system-administrator group with full rights. The manifest data list contains no record-rule file. The rule has no company field. Advanced editors, the rotate button, the log toggle and the log view are restricted to the developer-mode group in the form, which is UI gating only. |
| C17 | HIGH | VERIFIED | All six constraints are present as A1 describes them. The server-action extension also warns when the action model differs from the rule model. |
| C18 | MED | VERIFIED | Duplication copies the actions and relinks them. The identifier and last-run are non-copied, so the duplicate gets a fresh identifier. The active field has no non-copy flag. Under standard ORM copy semantics (defined in base) the duplicate would inherit the active state, and creating it re-registers patches immediately. This is a runtime proof item (PR-18). |
| C19 | MED | **PARTIAL** | Verified: the window runs from last-run (or the epoch when never run) to now, shifted by the signed delay; working-day planning with leaves applies when a calendar is set and the unit is days; date and datetime use different comparisons. Inaccurate: the fallback to creation date applies only when the chosen date field is the last-automation timestamp field and it is empty. The "after last update" trigger uses the write-date field with no fallback. Omitted: first-run behaviour (O2). |
| C20 | HIGH | VERIFIED | The job iterates active time rules. It re-checks active and existence per rule, flushes, rolls back a failing rule and keeps its last-run, commits and advances last-run per successful rule, and re-raises the last error. Omitted consequence: one poison record blocks its rule indefinitely (O3). |
| C21 | HIGH | VERIFIED | The job ships inactive at 4 hours with no-update. Its active flag follows whether any active time rule exists, so it also turns off. The interval is one-tenth of the smallest non-zero delay, bounded between 1 minute and 4 hours. Refinement: the interval is only ever shortened, even though the method's docstring says it restores; the update is skipped silently if the job row lock is not obtained (O10). |
| C22 | HIGH | VERIFIED | Rule id and name are attached to the error only when the current user is internal. The error is re-raised in every case. |
| C23 | HIGH | VERIFIED | The extension adds the usage value (cascade), the back-link (cascade, indexed), the exclusion from multi-action children, restriction of available models to the rule's model, and navigation from actions and scheduled jobs. |
| C24 | HIGH (path) | VERIFIED — **contradiction candidate confirmed at source level** | The message path evaluates only the before-condition, and it calls processing without a post-condition. No other route applies the apply-on condition to message triggers. The before-condition compute clears the value for every trigger except tag-set whenever trigger or reference changes, but the field stays writable. In developer mode the form shows both the before-condition editor and the apply-on editor for message triggers. Outside developer mode it shows neither. So a developer-mode admin can set an apply-on condition that is silently ignored, while a before-condition set by hand is honoured. Practical effect: PR-03. |

**Primary claim verdict counts:** VERIFIED 22, PARTIAL 2, NOT_VERIFIED 0, OUT_OF_SCOPE 0.

### 2b. Derived A1 items (business rules, states, failures, gaps, CRQs)

| Item | A2 verdict | Note |
|---|---|---|
| BR1 | VERIFIED | Admin-only (ACL), elevated lookup |
| BR2 | VERIFIED | Constraints re-read |
| BR3 | VERIFIED | Per rule, per call chain |
| BR4 | VERIFIED | With S2: an empty watched-field set fires on any write |
| BR5 | PARTIAL | The identifier match is not tied to the webhook trigger; the rule must also be active (O1, O13) |
| BR6 | VERIFIED | — |
| State 1–6 | VERIFIED | — |
| State 7 / G7 | PARTIAL | The source does show that the time job re-checks active and existence per rule between commits, so a rule deactivated or deleted mid-run is skipped if not yet reached. Synchronous and in-flight behaviour elsewhere is still unevidenced (O13) |
| F1 | VERIFIED | Warning log and skip at registration |
| F2 | VERIFIED | A failing getter re-raises. A missing record raises a validation error. Both become a generic 500 |
| F3 | VERIFIED (static) | The error propagates. The rollback of the triggering transaction is a runtime item (PR-24) |
| F4 | VERIFIED | — |
| F5 | VERIFIED | — |
| F6 | VERIFIED (static) | Same as C24 |
| G1–G6 | VERIFIED as gaps | Carried unchanged |
| G8 | VERIFIED as gap | No company field on the rule; confirmed |
| G9 | VERIFIED as gap | No idempotency key anywhere in the module |
| G10 | PARTIAL | No sequence or order attribute on the rule model, so lookup order falls to the ORM default (base, expected to be record id). Runtime confirmation: PR-21 |
| G11 | Settled by source (declaration level) | See O12 |
| CRQ-01 | Open — runtime | PR-01, PR-02 |
| CRQ-02 | Open — runtime (source confirmed) | PR-03 |
| CRQ-03 | Partly settled | The identifier is a version-4 random UUID. Rotation replaces the stored value, and lookup is by current value with no cache in the module. The module has no rate limiting. The payload goes to the debug logger always and to the log store when enabled. Residual: PR-05, PR-07 |
| CRQ-04 | Open — runtime | PR-10, PR-13 |
| CRQ-05 | Open — runtime | PR-22 |
| CRQ-06 | Partly settled | See G10; PR-21 |
| CRQ-07 | Partly settled | See G7; PR-23 |
| CRQ-08 | Open — runtime | PR-11, PR-14, PR-15 |
| CRQ-09 | Settled at declaration level | See O12. Runtime confirmation: PR-27 |
| CRQ-10 | Open — runtime | PR-18 |

## 3. Semantic / business findings (ERP automation engine framing)

- S1 — Trigger semantics are change-driven, not state-driven. Write-type rules fire on a transition: the before-condition was satisfied and the apply-on condition is satisfied after the change. Create and delete rules check only the end state. The time-based rules are also not state-driven: they are window-driven (O11). A1 frames this correctly for write, create and delete, and underplays it for time.
- S2 — "Watched fields empty means all fields." When a convenience trigger cannot resolve its conventional field, or an admin clears the watched fields, the rule fires on every create or write of the model. A1's F5 says "may be broader than intended". The source supports a stronger statement: it fires on any write.
- S3 — Recursion is bounded per rule and per record within a call chain, not globally. Different rules may still chain on the same record, and the same rule may run on *other* records in the chain. There is no depth limit. The A1 framing "bounded recursion" is correct only in that narrow sense.
- S4 — Execution identity is split. Expressions see the triggering user, or the public user for webhooks. Filters and record matching run as superuser, and the action records are superuser-flagged. A business reader should not assume that "the rule runs as the user who triggered it". A1 correctly withholds a privilege-escalation conclusion. The static evidence leans towards elevated execution, and PR-01 and PR-02 must settle it.
- S5 — The webhook's security model is a bearer secret in the URL, and the secret is bound to the rule rather than to the webhook trigger (O1). The default record-getter lets the caller name any model and record id, and the lookup runs as superuser (O6). The only other access control is the rule's active flag. A1's framing ("the only access control") is directionally right, but it misses the trigger-agnostic exposure.
- S6 — Time-based processing is catch-up, window-based and non-idempotent. A new rule starts from the epoch (O2), a failing record freezes the rule (O3), and changing a record's date can make it fire twice or never (O11). These are the automation behaviours most likely to create surprises in ERP operations (mass emails, duplicate follow-ups), and A1 does not state them.
- S7 — Failure semantics differ by path. The synchronous paths (create, write, recompute, delete, message, onchange) propagate the error, so the business operation that triggered the rule is expected to fail with it. The time path isolates failures per rule. The webhook path returns a generic 500 to the caller. A1 covers the pieces, but it does not state the user-facing consequence for the synchronous paths: an automation rule can block ordinary business operations such as saving or deleting a record.

## 4. Omissions (behaviours A1 did not state)

| ID | Severity | Omission (source-grounded, paraphrased) | Evidence | Proof |
|---|---|---|---|---|
| O1 | HIGH | The webhook route resolves any active rule by its identifier without checking that the rule's trigger is webhook. Every rule receives an identifier at creation, and the identifier survives a change of trigger. A URL shared while a rule was a webhook stays callable after the rule is switched to another trigger. | E7 lookup; E4 identifier default and URL compute | PR-04 |
| O2 | HIGH | A time-based rule that has never run treats its last-run as the epoch. Its first job run selects every matching record whose shifted date falls between the epoch and now, which amounts to retroactive mass execution. | E4 time-record search | PR-11 |
| O3 | HIGH | Because last-run advances only on full success, one record that always fails makes its rule fail on every job run, never advance, and never process later records. The rule stalls indefinitely. | E4 cron processor | PR-12 |
| O4 | MED | UI-change rules run whenever the watched fields change in a form, whether or not the user saves (the form itself warns about this). They run for any user editing that form, and their actions are superuser-flagged. Any side effects outside the edited record depend on how onchange transactions are handled at runtime. | E4 onchange maker; E11 warning text | PR-20 |
| O5 | MED | The request payload is injected into every code-type server action evaluated during any HTTP request that carries JSON or query data, not only webhook calls. | E5 eval context; E4 payload helper | PR-26 |
| O6 | HIGH | The webhook record-getter is evaluated with the rule's elevated environment. The default getter takes model name and id from the caller's payload, so an external caller chooses which model and record are looked up as superuser. A 200 versus 500 response may also reveal whether a record exists. | E7; E4 webhook execution, record-getter default | PR-08 |
| O7 | MED | Message triggers are skipped whenever the processing-guard marker is in context. That marker is set for the whole time-based job run and for any create or write on a model that has matching rules. So messages posted by time-based actions, and messages posted during such creates and writes, never fire message rules. | E4 message patch, lookup helper, cron | PR-19 |
| O8 | MED | Delete rules run their actions before the deletion. If an action fails, the deletion is aborted. | E4 unlink maker | PR-24 |
| O9 | MED | Patches are re-registered only when model, active, trigger or on-change fields change, and never under a file-import context. Rules imported from a file may not take effect until the registry is reloaded. | E4 write, update-registry | PR-25 |
| O10 | LOW | The job interval is only ever shortened automatically. After short-delay rules are removed, the job stays at the short interval (contrary to the docstring). If the job row cannot be locked, the activation update is skipped silently, so a new time rule could sit behind an inactive job. | E4 cron update | PR-17 |
| O11 | MED | The time trigger fires on window crossings, not on record state. A record whose date moves forward into a later window can fire again, and one whose date moves back into an already-processed window never fires. The apply-on condition is evaluated at job time, not at event time. Date-type fields are compared against the UTC date of the job clock. | E4 time-record search | PR-14, PR-15 |
| O12 | MED | Tracking is declared only on name, model, trigger, date field and delay settings. Active flag, both conditions, watched fields, actions, calendar, record-getter, log toggle and identifier have no tracking. Enabling or disabling a rule, or changing its conditions, leaves no before/after audit value. | E4 field declarations | PR-27 |
| O13 | LOW | An inactive rule is invisible to the webhook lookup, so its URL returns 404, and the time job skips a rule deactivated between commits. This partly answers G7 and CRQ-07. | E7; E4 cron | PR-06, PR-23 |
| O14 | MED | The before and apply-on conditions are evaluated against superuser-visible data. A condition can therefore match on values the triggering user cannot read, and the resulting records are handed on to superuser-flagged actions. | E4 filter methods | PR-22 |
| O15 | LOW | No ordering attribute exists on rules. When several rules match one event, the order is whatever the default model order gives. | E4 (no order or sequence attribute) | PR-21 |
| O16 | LOW | The last-automation timestamp is written before the actions run. That write is itself a write on the target record, so other rules' write triggers may be evaluated on it. | E4 process | PR-09 |
| O17 | LOW (observation) | Two source-level anomalies, not asserted as defects. (a) In the date-type branch for an empty last-automation field, the upper bound on creation date uses the current calendar date instead of the shifted bound. (b) Duplicating several rules in one call copies all their actions together and assigns them to the result collectively. | E4 time search; E4 copy | PR-16, PR-18 |

## 5. Lane B classification

There is no Lane B runtime evidence for `base_automation` in the repository. That absence is not a failure. Labels:
- NOT_APPLICABLE: a purely declarative or structural claim that runtime observation cannot add to.
- UNCORROBORATED: a behavioural claim that the source settles adequately, with no runtime corroboration yet.
- MISSING_REQUIRED_RUNTIME_PROOF: a claim, or its stated risk, that is inherently runtime and cannot be settled statically.

| Claim | Lane B status | Linked proof |
|---|---|---|
| C01 | UNCORROBORATED | — |
| C02 | NOT_APPLICABLE | — |
| C03 | UNCORROBORATED | PR-27 (optional) |
| C04 | NOT_APPLICABLE | — |
| C05 | UNCORROBORATED | — |
| C06 | MISSING_REQUIRED_RUNTIME_PROOF (effect on in-flight work and on other workers) | PR-23, PR-25 |
| C07 | UNCORROBORATED | — |
| C08 | UNCORROBORATED | PR-19 (breadth) |
| C09 | MISSING_REQUIRED_RUNTIME_PROOF (actual recursion bound, cross-transaction duplicates) | PR-09, PR-10 |
| C10 | UNCORROBORATED | — |
| C11 | MISSING_REQUIRED_RUNTIME_PROOF (final execution identity) | PR-01, PR-02 |
| C12 | MISSING_REQUIRED_RUNTIME_PROOF (payload exposure outside webhooks) | PR-26 |
| C13 | NOT_APPLICABLE | — |
| C14 | MISSING_REQUIRED_RUNTIME_PROOF (endpoint behaviour, trigger-agnostic lookup, rotation) | PR-04, PR-05, PR-06 |
| C15 | UNCORROBORATED | PR-07 |
| C16 | UNCORROBORATED | PR-22 (company scope) |
| C17 | UNCORROBORATED | — |
| C18 | MISSING_REQUIRED_RUNTIME_PROOF (active state of the copy, double effect) | PR-18 |
| C19 | MISSING_REQUIRED_RUNTIME_PROOF (time zone, calendar, catch-up) | PR-11, PR-14, PR-15, PR-16 |
| C20 | MISSING_REQUIRED_RUNTIME_PROOF (external side effects, stall) | PR-12, PR-13 |
| C21 | UNCORROBORATED | PR-17 |
| C22 | UNCORROBORATED | PR-24 |
| C23 | NOT_APPLICABLE | — |
| C24 | MISSING_REQUIRED_RUNTIME_PROOF (practical effect of the ignored apply-on condition) | PR-03 |

Totals: NOT_APPLICABLE 4, UNCORROBORATED 11, MISSING_REQUIRED_RUNTIME_PROOF 9.

## 6. Proof requirements (falsifiable; for Reconciliation / Proof)

Each item is a runtime test on a disposable database built from the anchored source, run by the Proof stage. "Expected" is the outcome the static reading predicts. "Fail" is the outcome that falsifies the static reading. Both outcomes must be recorded verbatim.

| PR | Linked | Setup / action | Expected (static prediction) | Fail condition |
|---|---|---|---|---|
| PR-01 | C11, CRQ-01 | An internal user without write rights on model Y edits a record of model X. That write triggers a create-or-edit rule whose code action writes a record of Y. Inside the action, record the effective user and the superuser flag | The write to Y succeeds. The recorded user is the triggering user and the superuser flag is set | Access error, or the superuser flag is not set (then elevated execution is disproved) |
| PR-02 | C11, O6 | Call a webhook rule anonymously. Record the effective user and the superuser flag inside its code action | User is the public user, superuser flag set, action effects persist | Access error or no effect |
| PR-03 | C24, CRQ-02 | Mail-capable model. An incoming-message rule has an apply-on condition (set in developer mode) that excludes record R. Post an external-author message on R | The action runs on R, so the apply-on condition is ignored | The action does not run on R |
| PR-04 | O1 | Create a webhook rule and record its URL. Change the trigger to create-or-edit and save. Call the old URL with a valid payload | 200, and the actions run on the resolved record | 404, or the actions do not run |
| PR-05 | C14, CRQ-03 | Rotate the identifier. Call the old URL, then the new URL | Old URL returns 404 at once. New URL returns 200 | Old URL still executes |
| PR-06 | O13 | Archive a webhook rule and call its URL | 404 | 200, or execution |
| PR-07 | C15 | Enable logging and send a payload containing a marker value; then disable logging and repeat | With logging on, the log store holds an entry containing the marker. With logging off, the log store has no new entry | The marker is absent when on, or an entry appears when off |
| PR-08 | O6 | Call the default record-getter with a payload naming a different model than the rule's and a valid id; repeat with a non-existent id | Lookup succeeds under superuser for the foreign model, and the status code differs between existing and non-existent ids. Record any action effect | The foreign-model lookup is refused, or the status codes are identical |
| PR-09 | C09, O16 | Rule A (on edit) sets a field on the same record. Rule B (on edit) reacts to that field and edits the field that A watches | Each rule runs at most once per record per call chain, and the chain terminates | A rule runs more than once on the same record in one chain, or recursion error |
| PR-10 | C09, CRQ-04, G9 | Deliver the same webhook payload twice. The action creates a record | Two records are created (no idempotency) | Only one record |
| PR-11 | O2, C19 | Model with records created over the past year. Add an "after creation + 1 day" rule that stamps records. Run the job once | Every historical record whose shifted date is up to now is stamped in the first run | Only records created after the rule are stamped |
| PR-12 | O3, C20 | A time rule whose action fails on one specific record, plus a second, healthy time rule. Run the job three times, adding new eligible records between runs | The failing rule's last-run never advances and its new records are never processed. The healthy rule advances each time. The job is marked failed each run | The failing rule advances, or the other records get processed |
| PR-13 | C20, CRQ-04 | A time rule with two actions: an outbound HTTP call to a capture endpoint, then a forced failure. Run the job twice | The rule's database changes and queued mails are rolled back each run, and the capture endpoint receives one call per run (duplicates) | The capture endpoint receives nothing, or database changes persist |
| PR-14 | O11 | "Based on date field" rule. After a job run, move a processed record's date forward past the next window; move another unprocessed record's date back into the already-processed window. Run the job | The first record fires again. The second never fires | Otherwise |
| PR-15 | O11, C19, CRQ-08 | Date-type trigger field; user time zone well ahead of UTC; record date = local "today" while UTC is still the previous day. Run the job | Selection follows the UTC date of the job clock, not the user's local date | Selection follows the user's local date |
| PR-16 | C19, O17 | (a) An "after last update" rule on records with an old write-date: confirm no fallback to create-date. (b) A "based on date field" rule on the last-automation timestamp with the field empty: confirm fallback to create-date, and record the upper bound applied in the date-type case | (a) write-date only. (b) Fallback applies | (a) create-date used. (b) No fallback |
| PR-17 | C21, O10 | Create a time rule with a 30-minute delay; inspect the job. Delete it; inspect again | After creation: job active, interval 3 minutes. After deletion: job inactive, interval still 3 minutes | The interval returns to 4 hours, or the job stays active |
| PR-18 | C18, CRQ-10, O17 | Duplicate an active create rule whose action creates a note. Create one target record | The copy is active, has a new identifier and an empty last-run, its actions are distinct copies, and two notes are created | The copy is inactive, or one note |
| PR-19 | O7 | (a) A time rule whose action posts an external-author message, with an incoming-message rule on the same model. (b) Same, but the message is posted during a create that matches a create rule | The incoming-message rule does not fire in (a) or in (b) | It fires |
| PR-20 | O4 | A UI-change code action creates a record on another model. Change the watched field in the form, then discard without saving | Record whether the other-model record persists. The static prediction is that the action runs on every change, whether or not the form is saved | The action does not run until save |
| PR-21 | G10, CRQ-06 | Two rules on the same trigger append markers in order. Create them in order A then B; repeat with B then A | Execution order follows rule id (creation order) | Order is independent of id, or non-deterministic |
| PR-22 | O14, CRQ-05, G8 | Multi-company. A user restricted to company 1 edits a company-1 record. The rule's apply-on condition reads a field from a company-2 record, and its action writes a company-2 record | The condition matches and the write succeeds (no company scoping) | The condition fails, or an access or company error occurs |
| PR-23 | O13, C06, CRQ-07 | Two time rules. Deactivate the second from another session while the job is processing the first | The second rule is skipped in that run | The second rule runs |
| PR-24 | F3, O8, C22 | (a) A create rule whose action raises: create a record as an internal user, then as a portal or public user. (b) A delete rule whose action raises: delete a record | (a) The create is rolled back; the internal user's error carries the rule id and name; the portal user's error has no rule context. (b) The record is not deleted | (a) The create persists or the rule context is wrong. (b) The record is deleted |
| PR-25 | O9 | Import a create rule via file import, then create a target record in the same registry generation | The rule does not fire until the registry is reloaded | It fires immediately |
| PR-26 | O5, C12 | A code action (non-webhook trigger) records whether a payload variable exists. Trigger it from an ordinary web-client save | The payload variable is present, containing the request body | Absent |
| PR-27 | O12, CRQ-09 | Archive a rule, change its apply-on condition, and add an action | No tracking values are recorded for these changes. Changes to name, trigger or delay are tracked | Tracking values are recorded for them |

Proof requirement count: 27.

## 7. Limitations

- Static re-read only. A2 executed no runtime. Every Expected column in section 6 is a prediction, not an observation.
- Scope was limited to the 9 re-fetched files. The JS assets, tests, and the base implementations of server-action execution, cron commit progress, ORM copy semantics and default ordering were not read. Claims that depend on them are labelled as base-dependent and routed to Proof.
- The view file (E11) was read in targeted sections (condition editors, webhook controls, developer-mode groups), not line by line.
- Verdicts judge the semantic accuracy of A1 statements. They do not grade A1's severity or confidence choices, beyond noting where the source supports a stronger or narrower statement.
- Omissions O1–O17 are A2 findings from source. They are not QID answers and are not confirmed defects until Proof executes.
- No percentages, no Formal Coverage claim, no git operations. The A1 package and the Lane A packet were not modified.
