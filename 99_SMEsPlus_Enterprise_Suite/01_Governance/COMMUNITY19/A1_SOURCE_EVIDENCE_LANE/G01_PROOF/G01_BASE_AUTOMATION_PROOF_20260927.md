# G01 PLATFORM_BASE — RED TEAM Proof Package — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus PROOF controller (Stage 2 of a two-stage REC + PROOF run) |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Date | 2026-09-27 |
| Upstream REC | `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_20260927.md` (46 REC items: MATCH 16, CONTRADICTION 5, UNKNOWN_PENDING_PROOF 20, GAP 5) |
| Inputs (sha256 at intake) | A1 `f01dec29…7007`; A2 `bf95295f…4208`; Lane A `8656751d…ec058`; base Lane A `9108bd4f…403b` (the base A1 package was absent); bank `3c38cec4…9a49` equals FREEZE_W1-B02; freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`, fetched 2026-09-27 14:57:40 UTC; every blob verified with `git hash-object` (section 2) |
| Predeclaration | Scratchpad `rec_baut/proof_cases_predeclared.txt`, sha256 `35e55e11afef0a8a1c551e6579113aca22eb0bda2db231a561f82c319e601f27`, hashed 2026-09-27 14:58:26 UTC. Source was fetched (for hashing) before this point but was not re-read until after it |
| Runtime device | THPATTARAKRIT-SOLUTION-SERVICE-2.local: **OFFLINE**. Host resolution failed at 2026-09-27 ~15:00 UTC (`getent hosts` rc=2; HTTP probe returned no response) |
| **Disposition** | **PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING** |

Clean-room note: results are neutral paraphrases of observed source behaviour. Identifiers are evidence pointers only. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited. Source copies are held in the scratchpad only.

## 1. Case design

- The 27 A2 proof requirements (PR-01..PR-27) become **runtime cases PC-BAUT-01..27**, one to one. Setup, expected result and fail condition are taken unchanged from A2 section 6. They are restated in section 4 so they can run without further authoring.
- For each PR, the static prediction basis becomes a **SOURCE / CONFIG / CROSS-MODULE static case, PC-BAUT-28..55**. These were predeclared (hash above) and **executed now**.
- A static PASS confirms only that the source reads as the static prediction assumes. **It is never counted as a result for the linked runtime case.**
- Layers: SOURCE = module code read; CONFIG = shipped data/ACL/view/manifest declarations; CROSS-MODULE = behaviour that depends on base (server-action run path, ORM semantics); RUNTIME = disposable database built from the anchor.

## 2. Blob verification (executed)

| File (under `addons/base_automation/` unless noted) | Expected blob (Lane A) | Computed `git hash-object` | Result |
|---|---|---|---|
| `__manifest__.py` | dc874003… | dc87400390755ec3b07ef6b55073451e6caa7b52 | MATCH |
| `models/base_automation.py` | 099ba2e3… | 099ba2e3b5352a03fce94aec9f7bdc7219247144 | MATCH |
| `models/ir_actions_server.py` | 69efd9a0… | 69efd9a00029cc7b55fb8486790d60ba1b29ed37 | MATCH |
| `controllers/main.py` | e2eae519… | e2eae519dd6ad74866240e10a242b37d323581b0 | MATCH |
| `security/ir.model.access.csv` | 77253ff3… | 77253ff3e968d1325b73f05fcf65f09ef073df34 | MATCH |
| `data/base_automation_data.xml` | a680e343… | a680e343b6339e7b18a1c44582e9aaf23afad54f | MATCH |
| `data/digest_data.xml` | 7330f4b3… | 7330f4b3e4e1c841a4ff9366944dc51e1c9ff873 | MATCH |
| `views/base_automation_views.xml` | 32290c98… | 32290c98655266f42ff8f332b9ade8a3b584f8ec | MATCH |
| `views/ir_actions_server_views.xml` | 7afe06b4… | 7afe06b4e22d7ddd466ec73f295759f2d26e21ce | MATCH |
| `odoo/addons/base/models/ir_actions.py` (cross-module) | 45d06ee4… (base Lane A E12) | 45d06ee4210b6e5559c6c96ab82ddc238a891a52 | MATCH |
| `odoo/addons/base/models/ir_cron.py` (cross-module) | e8762b92… (base Lane A E10) | e8762b920da6a68fd655dccf1a936671838c561d | MATCH |

11 of 11 blobs match.

## 3. Static cases — executed (SOURCE / CONFIG / CROSS-MODULE)

Expected and fail conditions are quoted in substance from the predeclaration.

| Case | Layer | Links | Expected (predeclared) | Fail condition (predeclared) | Actual (observed, paraphrased) | Result |
|---|---|---|---|---|---|---|
| PC-BAUT-28 | SOURCE | PR-04, O1, REC-25 | Webhook lookup filters by identifier only | A trigger==webhook term in the lookup or pre-execution check | The controller searches rules elevated with a single identifier term. Nothing checks the trigger type before the webhook executes. The URL compute blanks the URL for non-webhook triggers (UI only) | PASS |
| PC-BAUT-29 | SOURCE | PR-05, C14 | Rotation assigns a new random identifier; no in-module cache | Old value kept valid (alias/cache/list) | The rotate action writes a fresh version-4 random identifier per rule. There is no alias, history or cache of old identifiers in the module | PASS |
| PC-BAUT-30 | SOURCE | PR-06, O13 | Lookup does not disable default active filtering | active_test turned off in the lookup | The lookup passes no active-test override, so the ORM default applies. That default is a base ORM behaviour and is not read here | PASS |
| PC-BAUT-31 | SOURCE | PR-07, C15 | Log-store writes gated by the per-rule flag and elevated; payload always sent to the debug logger | Unconditional or non-elevated log write | The payload goes to the debug-level logger on every call. Log-store entries (call, getter failure, missing record, action failure with traceback) are written through an elevated log model only when the log toggle is on | PASS |
| PC-BAUT-32 | SOURCE | PR-08, O6 | Default getter takes model and id from the payload; evaluated in the rule's elevated environment | Getter bound to the rule model, or non-elevated | The default getter expression resolves model name and id from payload keys. The evaluation context's model handle comes from the rule's environment, which is elevated because the controller loaded the rule elevated. A failing getter or missing record raises, and the controller turns that into a generic 500 | PASS |
| PC-BAUT-33 | SOURCE | PR-11, O2 | Empty last-run → epoch lower bound | Lower bound = creation time or now | An empty last-run is replaced by the Unix epoch, built as a naive server-local date-time | PASS |
| PC-BAUT-34 | SOURCE | PR-12, PR-13, C20, O3 | Per-rule try/except; rollback on failure; last-run written only on success; per-rule commit; last error re-raised | Last-run advanced on failure, or no rollback | Per rule: records processed, then flush. On exception the cursor is rolled back, the error is logged, the exception is remembered and the loop continues (no last-run write). On success last-run is set to the run's start time and progress is committed. The last exception is re-raised at the end | PASS |
| PC-BAUT-35 | CONFIG | C21 | One job, inactive, 4 h, no-update | Any differs | One scheduled job record in a no-update data block: inactive, interval 4 hours, code calls the time-based processor | PASS |
| PC-BAUT-36 | SOURCE | PR-17, O10, C21 | Interval only reduced; active follows existence of active time rules; silent skip on lock failure | Interval restored/increased, or active not toggled | Active is set to whether any active time rule exists. Interval fields are written only when the new interval is strictly shorter. A lock failure returns without change. The method docstring says the default 4 hours is restored, but the code never restores it (contradiction with declared intent recorded as REC-34) | PASS |
| PC-BAUT-37 | SOURCE | PR-18, C18 | Identifier and last-run not copied; active has no non-copy flag; copy duplicates actions | Active non-copied or reset on copy | Identifier and last-run carry the non-copy flag. Active has a default only, with no non-copy flag. The copy override duplicates the source actions and assigns them to the copy. For a multi-rule copy, all actions are copied together and assigned collectively (O17b) | PASS |
| PC-BAUT-38 | SOURCE | PR-03, C24 | Message hook applies only the before-condition and processes without an apply-on condition; before-condition compute clears except tag-set | Apply-on evaluated in the message path | The message hook filters with the before-condition only and calls processing with no post-condition. The before-condition compute blanks it for every trigger except tag-set. No other path applies the apply-on condition for message triggers | PASS |
| PC-BAUT-39 | CONFIG | PR-03, C24 | For message triggers, both editors visible only in developer mode | Apply-on editor hidden for message triggers in dev mode | Developer-mode form: the before-condition editor is hidden only for create, delete, UI-change, webhook and time triggers, so it is visible for message triggers. The apply-on editor is hidden only for webhook, so it is visible for message triggers. Non-developer form: the apply-on editor is shown only for create, create-or-edit, UI-change, delete and time triggers, so it is hidden for message triggers | PASS |
| PC-BAUT-40 | CROSS-MODULE | PR-01, PR-02, C11, G4 | base_automation runs actions from an elevated collection; base run evaluates in the environment of the action recordset and object write/create act elevated | Elevation dropped before run, or base forces the caller's non-elevated user | The module iterates its rule's actions from an elevated view and calls run on each with the per-record context. The base run path builds the evaluation environment (the one code actions receive) from the recordset it is called on, so it is elevated here. It runs the access gate in that same environment and dispatches on an elevated action record. Elevation preserves the triggering uid (base Lane A items 21 and 38). The static prediction is therefore that code actions execute in superuser mode with the triggering user's uid and the per-action gate is not restrictive. The ORM superuser semantics live in `odoo/orm`, which was not read | PASS (static only) |
| PC-BAUT-41 | SOURCE | PR-21, O15, G10 | No order/sequence attribute on the rule model | Explicit order or sequence field present | No model order declaration and no sequence field on the rule model. The only "sequence" in the module's views is on the menu item | PASS |
| PC-BAUT-42 | SOURCE + CONFIG | PR-22, O14, G8, C16 | No company field; single admin ACL row; no record-rule file | Company field or record rule present | There is no company field on the rule model. The ACL file has one row granting the system-administrator group full rights. The manifest data list contains no record-rule file. The before and apply-on conditions are evaluated on an elevated recordset | PASS |
| PC-BAUT-43 | SOURCE | PR-27, O12, C03 | Tracking only on name, model, trigger, date field and delay amount/mode/unit | Tracking on active, conditions or actions | Tracking is declared on exactly those seven fields | PASS |
| PC-BAUT-44 | SOURCE | PR-26, O5, C12 | Payload added for code actions whenever an HTTP request carries JSON or query data; not gated to webhook | Gated on webhook trigger/context | The server-action eval-context extension adds the JSON helper and, when the request-payload helper returns a non-empty value (JSON body, or query arguments if the body is not JSON), the payload, for code-type actions only. There is no trigger or webhook condition | PASS |
| PC-BAUT-45 | SOURCE | PR-25, O9, C06 | Re-register only on model/active/trigger/on-change field changes; skipped under import context | Unconditional re-registration | Rule write re-registers only when a critical field (model, active, trigger, on-change fields) is written. Delay-field writes update only the job. Registry update runs only when the registry is ready and no file-import context flag is set. Create and delete always attempt it, under the same guard | PASS |
| PC-BAUT-46 | SOURCE | PR-24, O8, C22 | Postmortem context only for internal users; error always re-raised; delete hook runs actions before the actual delete | Error swallowed, or delete before actions | Rule id and name are attached to the error only when the current user is internal, and the error is re-raised unconditionally (synchronous and UI-change paths). The delete hook processes matching rules first and then calls the original delete | PASS |
| PC-BAUT-47 | SOURCE | PR-19, O7 | Message hook exits early when the guard marker is in context; the job sets the marker | No such early exit | The message hook returns without processing when the processing-guard marker is present (also for internal messages/subtypes and notification-type messages). The time-based processor sets the marker at entry. Rule lookup for create/write also installs it, and records are created or written in that environment | PASS |
| PC-BAUT-48 | SOURCE | PR-09, C09, O16 | Per-rule processed-records map in context, marked before execution; last-automation stamp written before actions | No per-rule map, or marking after execution | A context map from rule to processed records is consulted and updated before any action runs. Refinement: after the watched-field check, the mark is narrowed to the records that passed it, so records skipped by that check are not held as processed. The last-automation stamp (when the field exists) is written before the action loop | PASS |
| PC-BAUT-49 | SOURCE | PR-14, PR-15, O11 | Selection by shifted date in (last-run, now]; date-type compared with a date from the job clock, no user time zone | User time zone applied | The upper bound is the job's transaction time. Datetime fields use a half-open window [last-run, now) after the shift. Date fields use (last-run date, now date] derived from those shifted bounds. No user time zone is consulted. The apply-on condition is evaluated at job time | PASS |
| PC-BAUT-50 | SOURCE | PR-16, C19 | Creation-date fallback only for the last-automation field; after-last-update uses write-date with no fallback | Fallback on after-last-update | The fallback is active only when the chosen date field is the last-automation field and the model has a creation date. The "after last update" trigger resolves to the write-date field, so no fallback applies. Refinement (O17a): in the date-type fallback branch the creation-date upper bound is the process-local current date-time, not the shifted bound | PASS |
| PC-BAUT-51 | SOURCE | PR-10, G9, C09 | No dedup/idempotency key in module files | Dedup key present | No idempotency, deduplication, nonce or replay construct exists in the model, server-action extension, controller or views | PASS |
| PC-BAUT-52 | SOURCE + CONFIG | PR-20, O4 | UI-change rules restricted to code actions; view carries an unsaved-change warning | Absent | A constraint and an onchange warning restrict UI-change rules to code actions. The form shows a notice that such rules run every time watched fields change, saved or not. The UI-change hook runs actions from an elevated collection | PASS |
| PC-BAUT-53 | SOURCE | PR-23, O13 | Job re-checks each rule's active/existence before processing | No re-check | Before each rule, the job skips the rule if it is now inactive or no longer exists | PASS |
| PC-BAUT-54 | SOURCE | PR-02, C14 | Public/unauthenticated, CSRF off, GET+POST, session not saved | Auth user or CSRF on | Route declared with public auth, GET and POST, CSRF disabled and session saving disabled. Responses are a generic JSON status with 404 (no rule), 500 (any exception) or 200 | PASS |
| PC-BAUT-55 | CONFIG | C02 | Deps base, digest, resource, mail, sms; sms only in the manifest | Differs | Dependencies are exactly the five. Among the nine module files fetched, the token appears only in the manifest | PASS |

**Static totals: 28 executed — PASS 28, FAIL 0.** No failed static result exists to preserve. Refinements observed during execution (not failures) are recorded in 3.1.

### 3.1 Refinements observed (for A3; they do not change any verdict)

- R1 (PC-48): processed-record marking is narrowed after the watched-field check. A record that fails the check in one pass can still be processed by the same rule later in the same call chain. This is relevant to PC-09.
- R2 (PC-50, O17a): the date-type fallback bound uses the process-local current date-time. A2 described it as "current calendar date".
- R3 (PC-33): the epoch fallback is a naive server-local value, not an explicit UTC value. Its effect on first-run selection is runtime (PC-11, PC-15).
- R4 (PC-40): in the base run path, the per-action access gate runs in the same elevated environment. Statically, it therefore does not restrict rule-triggered actions. Runtime confirmation: PC-01.

## 4. Runtime cases — NOT-EXECUTED (runtime unavailable)

Common preconditions for every runtime case: a disposable database built from the anchored source (`8d05257d…`) with `base_automation` installed, plus the named test users and models. The system clock must be controllable for time cases (PC-11..17). An outbound HTTP capture endpoint is needed for PC-13. Record verbatim outcomes. Status for all: **NOT-EXECUTED — runtime device THPATTARAKRIT-SOLUTION-SERVICE-2.local offline**. No result is inferred from the static cases.

| Case | Layer | Links (REC) | Steps (ready to run) | Expected | Fail condition | Status |
|---|---|---|---|---|---|---|
| PC-BAUT-01 | RUNTIME + CROSS-MODULE | PR-01, REC-11 | Internal user U has no write access to model Y. U edits a record of X. A create-or-edit rule on X has a code action that writes a Y record and records the effective uid and superuser flag | Y write succeeds; uid = U; superuser flag set | Access error, or superuser flag not set | NOT-EXECUTED |
| PC-BAUT-02 | RUNTIME | PR-02, REC-14, REC-30 | Anonymous call to a webhook rule whose code action records uid and superuser flag | Public user, flag set, effects persist | Access error or no effect | NOT-EXECUTED |
| PC-BAUT-03 | RUNTIME | PR-03, REC-24 | Mail-capable model. Incoming-message rule with an apply-on condition (set in dev mode) excluding record R. Post an external-author message on R | Action runs on R | Action does not run on R | NOT-EXECUTED |
| PC-BAUT-04 | RUNTIME | PR-04, REC-25 | Create a webhook rule and note its URL. Switch the trigger to create-or-edit and save. Call the old URL with a valid payload | 200 and actions run | 404, or no action | NOT-EXECUTED |
| PC-BAUT-05 | RUNTIME | PR-05, REC-14 | Rotate the identifier. Call the old URL, then the new URL | Old URL 404 at once; new URL 200 | Old URL still executes | NOT-EXECUTED |
| PC-BAUT-06 | RUNTIME | PR-06, REC-37 | Archive a webhook rule and call its URL | 404 | 200 or execution | NOT-EXECUTED |
| PC-BAUT-07 | RUNTIME | PR-07, REC-15 | Logging on: send a payload with a marker. Logging off: repeat | Marker in the log store only when on | Marker absent when on, or an entry appears when off | NOT-EXECUTED |
| PC-BAUT-08 | RUNTIME | PR-08, REC-30 | Default getter; payload names a foreign model with a valid id; repeat with a non-existent id | Foreign lookup succeeds elevated; status codes differ; record any action effect | Foreign lookup refused, or identical codes | NOT-EXECUTED |
| PC-BAUT-09 | RUNTIME | PR-09, REC-09, REC-40 | Rule A (edit) sets field f. Rule B (edit) reacts to f and edits A's watched field | Each rule at most once per record per chain; chain terminates | A rule runs more than once on the same record in one chain, or recursion error | NOT-EXECUTED |
| PC-BAUT-10 | RUNTIME | PR-10, REC-09 | Deliver the identical webhook payload twice; the action creates a record | Two records | One record | NOT-EXECUTED |
| PC-BAUT-11 | RUNTIME | PR-11, REC-26 | Records created over the past year. Add an "after creation + 1 day" stamping rule. Run the job once | All historical eligible records stamped in the first run | Only post-rule records stamped | NOT-EXECUTED |
| PC-BAUT-12 | RUNTIME | PR-12, REC-27 | A time rule that fails on one record, plus a healthy time rule. Run the job three times, adding eligible records between runs | Failing rule never advances and new records are never processed; healthy rule advances; job marked failed each run | Failing rule advances, or the other records get processed | NOT-EXECUTED |
| PC-BAUT-13 | RUNTIME | PR-13, REC-20 | A time rule: outbound call to a capture endpoint, then forced failure. Run the job twice | DB changes and queued mail rolled back each run; one capture call per run | No capture, or DB changes persist | NOT-EXECUTED |
| PC-BAUT-14 | RUNTIME | PR-14, REC-35 | "Based on date field" rule. After a run, move a processed record's date past the next window, and move an unprocessed record's date into a processed window. Run the job | First fires again; second never fires | Otherwise | NOT-EXECUTED |
| PC-BAUT-15 | RUNTIME | PR-15, REC-35 | Date-type field. User time zone ahead of UTC. Record date = local today while UTC is still yesterday. Run the job | Selection follows the UTC job-clock date | Selection follows the user's local date | NOT-EXECUTED |
| PC-BAUT-16 | RUNTIME | PR-16, REC-19, REC-41 | (a) "After last update" rule on records with an old write-date. (b) Last-automation-field rule with the field empty; record the date-type upper bound | (a) write-date only; (b) fallback applies | (a) create-date used; (b) no fallback | NOT-EXECUTED |
| PC-BAUT-17 | RUNTIME + CONFIG | PR-17, REC-34 | Create a 30-minute time rule and inspect the job. Delete it and inspect again | After create: active, 3 minutes. After delete: inactive, still 3 minutes | Interval back to 4 h, or job stays active | NOT-EXECUTED |
| PC-BAUT-18 | RUNTIME + CROSS-MODULE | PR-18, REC-18, REC-41 | Duplicate an active create rule whose action creates a note. Create one target record | Copy active, new identifier, empty last-run, distinct actions; two notes | Copy inactive, or one note | NOT-EXECUTED |
| PC-BAUT-19 | RUNTIME | PR-19, REC-31 | (a) A time rule's action posts an external-author message; an incoming-message rule exists on the same model. (b) Same, but the message is posted during a create that matches a create rule | Message rule fires in neither | It fires | NOT-EXECUTED |
| PC-BAUT-20 | RUNTIME | PR-20, REC-28 | A UI-change code action creates a record on another model. Change the watched field, then discard | Record whether the other-model record persists; the action runs on change without save | Action does not run until save | NOT-EXECUTED |
| PC-BAUT-21 | RUNTIME + CROSS-MODULE | PR-21, REC-39 | Two same-trigger rules append markers. Create A then B; repeat with B then A | Order follows rule id | Order independent of id, or non-deterministic | NOT-EXECUTED |
| PC-BAUT-22 | RUNTIME + CROSS-MODULE | PR-22, REC-38, REC-16 | Multi-company. A user restricted to company 1 edits a company-1 record. The rule's condition reads a company-2 record and its action writes a company-2 record | Condition matches; write succeeds | Condition fails, or access/company error | NOT-EXECUTED |
| PC-BAUT-23 | RUNTIME | PR-23, REC-37, REC-06 | Two time rules. Deactivate the second from another session while the job processes the first | Second skipped in that run | Second runs | NOT-EXECUTED |
| PC-BAUT-24 | RUNTIME | PR-24, REC-22, REC-32 | (a) A create rule's action raises; create as an internal user, then as a portal/public user. (b) A delete rule's action raises; delete a record | (a) Create rolled back; internal error carries rule id and name; portal error has none. (b) Record not deleted | (a) Create persists, or wrong context. (b) Record deleted | NOT-EXECUTED |
| PC-BAUT-25 | RUNTIME | PR-25, REC-33 | Import a create rule via file import, then create a target record in the same registry generation | Rule does not fire until registry reload | Fires immediately | NOT-EXECUTED |
| PC-BAUT-26 | RUNTIME | PR-26, REC-12, REC-29 | A non-webhook code action records whether a payload variable exists. Trigger it from an ordinary web-client save | Payload present with the request body | Absent | NOT-EXECUTED |
| PC-BAUT-27 | RUNTIME | PR-27, REC-36, REC-03 | Archive a rule, change its apply-on condition, add an action; separately change name, trigger and delay | No tracking values for the first set; tracked for the second | Tracking values recorded for the first set | NOT-EXECUTED |

**Runtime totals: 27 cases — NOT-EXECUTED 27, PASS 0, FAIL 0.**

## 5. Summary of results

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE (incl. SOURCE+CONFIG) | 24 | 24 | 0 | 0 |
| CONFIG | 3 (PC-35, PC-39, PC-55) | 3 | 0 | 0 |
| CROSS-MODULE (static) | 1 (PC-40) | 1 | 0 | 0 |
| RUNTIME (incl. runtime + cross-module / config) | 27 | 0 | 0 | 27 |
| **Total** | **55** | **28** | **0** | **27** |

REC item status after Proof:
- The 5 CONTRADICTION items (C12, C19, C24, O1, O10) are **source-confirmed**: the A2 side or the source-side behaviour holds statically. They remain CONTRADICTION for A3 and are not closed. The runtime effect is pending for all five (PC-26, PC-11/14/15/16, PC-03, PC-04, PC-17).
- The 20 UNKNOWN_PENDING_PROOF items have their static prediction basis confirmed (all linked static PASS). **All remain UNKNOWN_PENDING_PROOF** until the runtime cases run.
- The 16 MATCH items are unchanged. The 5 GAP items are carried forward and cannot be closed by Proof in this scope.

## 6. A3 eligibility

**Disposition: PROOF PARTIAL — SOURCE/CONFIG EXECUTED, RUNTIME PENDING.**

A3 can challenge **now** (static scope):
1. REC classifications and counts (46 items), including the fold-in of G4/G7/G8/G9/G10/G11 and the MATCH treatment of O12.
2. The 28 executed static cases PC-BAUT-28..55: whether each expected/fail pair was truly falsifiable, whether the actual observations support PASS, and the refinements R1–R4.
3. The 5 CONTRADICTION items: the A1-vs-A2 scope corrections (C12, C19) and the three source-vs-intent findings (C24, O1, O10).
4. The cross-module identity reasoning (PC-40): its reliance on base Lane A item 38 and on unread ORM superuser semantics, given that the base A1 package is absent.
5. QID lineage (31 mapped, 9 "no evidence yet"), the join key and freeze hash, and clean-room compliance.
6. Input integrity (sha256 intake table, bank-to-freeze equality, blob verification), and the predeclaration timing.

**Blocked** until the runtime device is available:
- All 27 runtime cases PC-BAUT-01..27. In particular, final execution identity and privilege effect (PC-01, PC-02, PC-22), webhook exposure (PC-04, PC-05, PC-06, PC-08), time-job catch-up/stall/duplicate side effects (PC-11..PC-15), duplicate-rule effect (PC-18), message-path apply-on effect (PC-03) and payload exposure (PC-26).
- Closing any UNKNOWN_PENDING_PROOF item, or settling the practical effect of any CONTRADICTION item.
- Any sufficiency judgement that needs runtime evidence. A full A3 → MASTER handoff is therefore **not** eligible yet. This package is eligible for **A3 static-scope challenge only**.

## 7. Limitations

- No runtime was executed and no runtime result is claimed. Static PASS results confirm source readings only.
- ORM behaviours (default active filtering, copy semantics, superuser access bypass, default ordering, transaction time) are base or ORM code outside the files read. They come from base Lane A where cited and are otherwise routed to runtime.
- The base A1 package was absent at intake, so base Lane A (source-level) was used.
- JS assets and tests were not read (G1, G5).
- No percentages, no Formal Coverage claim, no git operations. Inputs were not edited. Source copies stay in the scratchpad (`rec_baut/src/`, blob log `rec_baut/blob_log.txt`).
