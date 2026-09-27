# G01 PLATFORM_BASE — RED TEAM A1 Package — `base_automation`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_BASE_AUTOMATION_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `8656751d9142e0b59c433454558cef5e57b7c4f089bf42c04cf2a280b18ec058` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/base_automation/` |
| Question bank (lens only) | `GMVQ/G01_PLATFORM_BASE/G01_BASE_AUTOMATION_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `3c38cec4…9a49`, matches `FREEZE_W1-B02.json`) |
| Freeze | batch W1-B02, freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`, ELIGIBLE |
| Lane B dependency | None. A1 does not wait for Lane B; no runtime evidence consumed |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: the claims below are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. Nothing here recommends reusing vendor schema, ORM, workflow, UI or naming. No QIDs are answered. The bank was used only to decide which topics matter: scope isolation, authority at execution time, recursion, idempotency/replay, failure and partial success, time/catch-up, audit/actor, external input, and duplication.

Evidence key (blob SHA-1 from the Lane A packet): E1 `__manifest__.py` dc874003…; E4 `models/base_automation.py` 099ba2e3…; E5 `models/ir_actions_server.py` 69efd9a0…; E7 `controllers/main.py` e2eae519…; E8 `security/ir.model.access.csv` 77253ff3…; E9 `data/base_automation_data.xml` a680e343…; E10 `data/digest_data.xml` 7330f4b3…; E11 `views/base_automation_views.xml` 32290c98…; E12 `views/ir_actions_server_views.xml` 7afe06b4…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-BAUT-C01 | WHAT: The module provides admin-configured rules that run server-side actions on any non-abstract business model when events, time conditions, messages, UI changes or inbound webhooks occur. WHY: no-code business automation. RISK: one mechanism reaches every business domain. | E1; E4 (rule model, target-model field) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C02 | WHAT: The declared dependencies are base, digest, resource, mail and sms. No use of sms appears in the Python or view files cited. RISK: the sms edge is only declared, and its purpose is unexplained. | E1; E4, E5, E11 (spot-check S7) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C03 | WHAT: Rules are themselves tracked, chattered records. Changes to key settings (name, model, trigger, dates) leave tracking entries. WHY: configuration audit trail. RISK: tracking covers only some fields, so changes to actions and filters may have no tracked before/after values. | E4 (class header, tracking attrs) | MED | SOURCE-STATIC |
| A1-G01-BAUT-C04 | WHAT: The trigger taxonomy covers field-value-set (stage, user, tag, state, priority), archive/unarchive, create, create-or-edit, update (deprecated), delete, UI change, three time-based variants, message received/sent, and webhook. | E4 (trigger selection) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C05 | WHAT: Convenience triggers find their target field by naming convention, including customization-prefixed names. If no field is found, the helper fields stay empty. RISK: the rule's meaning depends on how the target model names its fields, and the rule silently has no condition when no field matches. | E4 (trigger-specific field resolver) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C06 | WHAT: Activating rules patches the create, write, recompute, unlink and message-post behaviour of the target models at runtime. Creating or changing a rule re-registers the patches and invalidates the registry. RISK: changing configuration has registry-wide side effects, and when that change takes effect for work already in flight is unclear. | E4 (register hook / update registry) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C07 | WHAT: On update, a "before" condition is checked before the write and an "apply-on" condition after it. On create and delete, only the apply-on condition is checked. A watched-field change comparison gates execution. | E4 (pre/post filter, write patch, trigger-field check) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C08 | WHAT: Message triggers skip internal messages, internal subtypes and system-notification message types. A message is classed "received" when it has no author or the author is an external/share partner, and "sent" otherwise. RISK: whether a message counts as external depends on how the partner is classified. | E4 (message-post patch; S5) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C09 | WHAT: A context-carried map of rule to processed records stops the same rule from firing again on the same record within one call chain. Message triggers are suppressed while any rule is running. WHY: bounded recursion. RISK: the guard lives only in the transaction context and does not deduplicate across transactions or jobs. | E4 (process, get actions) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C10 | WHAT: Every server action of a rule runs once for each matching record, with the record passed as context. If the target has a last-automation timestamp field, it is stamped. | E4 (process; S3) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C11 | WHAT: Rule lookup, action iteration, filter-domain evaluation and webhook rule resolution all run with elevated (sudo) privileges. The effective identity under which the server action finally runs is decided outside this module. RISK: automation could exceed the authority of the triggering actor. | E4 (get actions, process, filters); E7 | HIGH (sudo use) / LOW (final identity) | SOURCE-STATIC |
| A1-G01-BAUT-C12 | WHAT: Filter expressions and the webhook record-getter are evaluated through a restricted evaluator that exposes model, user, time helpers and, for webhooks, the payload. The server-action context gains a JSON helper and the request payload. RISK: admin-authored expressions run against externally supplied data. | E4 (eval context, webhook exec); E5 | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C13 | WHAT: Field names in domains are extracted by pattern matching rather than evaluation. WHY: the comment in the source names hardening against crafted UI-change calls. | E4 (domain-field extraction comment) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C14 | WHAT: The webhook endpoint is public, unauthenticated, CSRF-exempt and session-less, and accepts GET and POST. The rule is resolved by a per-rule random identifier that is not copied when the rule is duplicated. Responses are generic ok/error with 200/404/500. RISK: the random identifier in the URL is the only access control. | E7 (S2); E4 (uuid default, rotate action) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C15 | WHAT: When logging is enabled, webhook calls, including payloads and tracebacks, are written to the system log store with elevated privileges. RISK: sensitive payloads are kept with no retention rule visible in this module. | E4 (webhook exec) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C16 | WHAT: Only the system-administrator group has create, read, update and delete access to rules. No record-level rules ship with the module, and developer-mode groups hide advanced fields in the UI. RISK: rules are not scoped per company or tenant, and developer-mode hiding is not a security boundary. | E8 (S4); E11 | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C17 | WHAT: Constraints: mail triggers need mail-capable models; every action must target the rule's model; delays cannot be negative; a UI-change rule may use only code actions; a delete rule may not use mail, follower or activity actions; no child action may carry warnings. | E4 (constraints); E5 | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C18 | WHAT: Duplicating a rule duplicates its actions and does not carry over the webhook identifier or last-run time. The duplicate's active state is not explicitly reset in the cited evidence. RISK: two active rules could produce the same business effect. | E4 (copy, field copy flags) | MED | SOURCE-STATIC |
| A1-G01-BAUT-C19 | WHAT: Time-based rules select records in a window from the previous run to now, shifted by the delay. They can plan by working days on a calendar, and "after last update" falls back to the creation date. RISK: behaviour depends on the time zone and the date-versus-datetime handling. | E4 (time-based record search) | MED | SOURCE-STATIC |
| A1-G01-BAUT-C20 | WHAT: The time-based job runs each active rule in turn. If a rule fails, its work is rolled back and its last-run time is not advanced; the other rules continue, and the last error is raised again to mark the job as failed. Successful rules commit and advance last-run one rule at a time. RISK: the whole window of a failed rule is retried; external side effects already sent are not rolled back. | E4 (cron processor; S6) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C21 | WHAT: The single scheduled job ships inactive at 4 hours, with no-update set. It switches on when any active time-based rule exists, and its interval shrinks to about one-tenth of the shortest delay, bounded between 1 minute and 4 hours. | E9 (S4); E4 (cron interval) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C22 | WHAT: When the current user is internal, action errors are raised again with the rule's identity attached. RISK: errors seen by non-internal or public users carry no rule context. | E4 (postmortem helper; S3) | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C23 | WHAT: The server-action extension adds an "automation" usage and a back-link to the owning rule, with cascade delete. It keeps rule-owned actions out of multi-action children and navigates from an action or scheduled job to its rule. | E5; E12 | HIGH | SOURCE-STATIC |
| A1-G01-BAUT-C24 | WHAT: The message-trigger path evaluates only the "before" condition. The "apply-on" condition is never evaluated there, and no apply-on condition is passed to the actions. The "before" condition is cleared automatically for every trigger except tag-set, but stays editable in developer mode. The apply-on editor is visible for message triggers in developer mode. See CRQ-02. | E4 (message-post patch, pre-domain compute); E11 (field visibility) — S5 | HIGH (source path) | SOURCE-STATIC — **CONTRADICTION CANDIDATE** |

## 2. Business rules
- BR1: Only system administrators manage rules (C16). Rules act on any model with elevated lookup (C11).
- BR2: A rule's actions must target the rule's own model, and certain action types are banned for UI-change and delete triggers (C17).
- BR3: Within one call chain, a record is processed at most once per rule (C09).
- BR4: Updates fire only when the watched fields actually changed and both conditions pass. Creates and deletes check only the apply-on condition (C07).
- BR5: A webhook runs only when the per-rule identifier matches, and that identifier can be rotated (C14).
- BR6: Time-based processing advances last-run only when a rule succeeds (C20).

## 3. States / transitions (trigger lifecycle)
1. Rule draft/config → active: active rules are registered and the target models patched. Changing a critical field re-registers them (C06). If a time-based rule is active, the job switches on and its interval may shrink (C21).
2. Event occurs (write, create, unlink, message, onchange, webhook, time window) → rules resolved under sudo (C11).
3. Filter stage: before and apply-on conditions, depending on the path (C07 and C24). Watched-field check (C07).
4. Recursion mark: the record is marked done for the rule (C09).
5. Execute: each action for each record (C10). Success → continue. Error → error raised again with rule context (C22).
6. Time path only: the rule's changes commit and last-run advances. On failure they roll back and last-run stays put (C20).
7. Rule deactivated/deleted → registry re-registered. How already-queued or in-flight work is treated is not evidenced (G7).

## 4. Exceptions / failure modes
- F1: The target model is missing because it was uninstalled. A warning is logged and the rule is skipped; it does not fail visibly to users (E4 register hook).
- F2: The webhook record-getter fails or finds no record. The failure is logged, logged again to the log store if enabled, and the caller gets a generic 500 (E4, E7).
- F3: An action fails in the synchronous path. The error propagates and the triggering transaction is expected to fail; runtime outcome not proven (C22).
- F4: An action fails in the time path. That rule rolls back, the other rules continue, and the job is marked failed (C20).
- F5: No convention field matches. The convenience trigger has an empty condition and may be broader than intended (C05).
- F6: The message path ignores the apply-on condition, so the rule may fire on records the admin intended to exclude (C24; to be verified).

## 5. Cross-module handoffs
| Edge | Nature | Claim |
|---|---|---|
| base (models, fields, server actions, cron, logging, groups, menu root) | Execution substrate; decides the final action identity | C11, C23, G4 |
| mail | Mixins on the rule; message-post hook; mail action types | C03, C08, C17 |
| resource | Working-day calendar for time delays | C19 |
| digest | Informational tip for administrators | E10 |
| sms | Declared only; out of the G01 roster | C02, G2 |
| Every business model | Runtime patching; an implicit edge to all groups | C01, C06 |
| External callers | Unauthenticated inbound webhook | C14 |

## 6. Evidence gaps
- G1 (carried): static JavaScript and tests not inspected.
- G2 (carried): the reason for the sms dependency is not evidenced; confirmed by grep (S7).
- G3 (carried): group gating of the parent menu lies in base.
- G4 (carried): the effective identity of server-action execution under sudo'd action lists and the public webhook context is defined in base.
- G5 (carried): tests directory not read.
- G6 (carried): absence of i18n, migrations and reports not proven.
- G7 (new): no evidence of how queued or in-flight work is treated when a rule is disabled, edited or deleted mid-run.
- G8 (new): no multi-company or tenant scoping of rules or their executions found in the cited evidence.
- G9 (new): no deduplication key or idempotency marker for webhook redelivery or for retrying a failed time window.
- G10 (new): no ordering attribute seen for several rules on the same event; order is not evidenced (C06 area).
- G11 (new): tracking coverage of changes to actions, filters and webhook settings is unverified (C03).

## 7. CRQ candidates (need runtime proof or more source)
| CRQ | Question | Basis |
|---|---|---|
| CRQ-01 | Under which user identity do server actions run for UI, time, message and webhook triggers? Can a non-privileged trigger obtain effects above its own rights? | C11, G4 |
| CRQ-02 | CONTRADICTION CANDIDATE: on message triggers, is an admin-set apply-on condition ignored at runtime while the before condition is honoured, even though the before condition is auto-cleared for message triggers? | C24 |
| CRQ-03 | Webhook secret strength and lifecycle: how much entropy does the identifier really have in use, does it leak through logs, referrers or proxies, is there rate limiting, and does rotation invalidate the old URL immediately? | C14, C15 |
| CRQ-04 | Does webhook redelivery or retrying a failed time window produce duplicate durable effects (email, records, external calls)? | C09, C20, G9 |
| CRQ-05 | Do rule executions respect company/tenant boundaries when triggered from one company's records? | C16, G8 |
| CRQ-06 | Is the order of execution deterministic when several rules match one event? | G10 |
| CRQ-07 | When a rule is disabled or edited during a long batch or job run, what effect does that have? | C06, G7 |
| CRQ-08 | How are time windows computed across time zones and calendars, and after downtime, is overdue work caught up in one burst? | C19, C21 |
| CRQ-09 | Are rule configuration changes (actions, filters, webhook settings) audited with before/after values? | C03, G11 |
| CRQ-10 | Does a duplicated rule start active and fire the same effects twice? | C18 |

## 8. Spot-check log
Each file was fetched from raw.githubusercontent.com at anchor `8d05257d…`, and `git hash-object` was run on the local copy.
| # | File | Recorded blob | Computed blob | Result | Claim checked |
|---|---|---|---|---|---|
| S1 | `__manifest__.py` | dc874003… | dc87400390755ec3b07ef6b55073451e6caa7b52 | MATCH | C02 dependency list |
| S2 | `controllers/main.py` | e2eae519… | e2eae519dd6ad74866240e10a242b37d323581b0 | MATCH | C14 public, CSRF-exempt, GET/POST, generic responses |
| S3 | `models/base_automation.py` | 099ba2e3… | 099ba2e3b5352a03fce94aec9f7bdc7219247144 | MATCH | C10, C22 process loop and internal-user postmortem |
| S4 | `security/ir.model.access.csv`, `data/base_automation_data.xml` | 77253ff3…, a680e343… | 77253ff3e968d1325b73f05fcf65f09ef073df34, a680e343b6339e7b18a1c44582e9aaf23afad54f | MATCH | C16, C21 |
| S5 | `models/base_automation.py`, `views/base_automation_views.xml` | 099ba2e3…, 32290c98… | same; 32290c98655266f42ff8f332b9ade8a3b584f8ec | MATCH | C08, C24: message path calls only the before-filter; before-filter compute resets except tag-set; view shows both editors in dev mode for message triggers |
| S6 | `models/base_automation.py` | 099ba2e3… | as above | MATCH | C20: rollback on failure, last-run written only on success, last error re-raised |
| S7 | `models/ir_actions_server.py` | 69efd9a0… | 69efd9a00029cc7b55fb8486790d60ba1b29ed37 | MATCH | C02: no sms reference in E4/E5/E11 |
Spot-check refinement to Lane A item 15: the skipped message types include auto-comment and user-notification types, not only notification (C08).

## 9. Provenance
- Input: only the Lane A packet (sha256 above). Spot-check copies are held in the session scratchpad and were not committed.
- Bank consulted read-only for topic salience. The bank sha256 matches the W1-B02 freeze manifest. No QID was answered and no bank was edited.
- No Lane B material was viewed. No git operations were performed.

## 10. Limitations
- Source presence does not prove runtime reachability, and each claim is SOURCE-STATIC only.
- C24 is confirmed at the source-path level. Whether it matters in practice is a runtime question (CRQ-02) and it is not asserted as a defect.
- Final execution identity (G4) is unresolved, so no privilege-escalation conclusion is drawn.
- No Formal Coverage claim is made, and there are no percentages.
