# G01 PLATFORM_BASE — Module `digest` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions); independent of A1 |
| Governed group / module | G01 PLATFORM_BASE / `digest` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_DIGEST_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `030442be4f9ccd83f2f988e4299749fafcf76a6954a794f2948337c7fa04ba87` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_DIGEST_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `d0f6ec30b0823ac82a20e0ae2b9b8261732d81383b2124a880becb3c49c62afe` (matches value recorded in A1 header) |
| Topic lens | W1-B03 bank `G01_DIGEST_GMVQ_MVQ_40_V1.00_DRAFT.md` sha256 `1ba4226db5739143130e0afc1757e3aaa3c0cf1f934ccf3349a907d0c64d74ec` (matches A1-recorded prefix/suffix); ELIGIBLE; no QID answered |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/digest/` via raw.githubusercontent; blobs computed locally with `git hash-object` in scratchpad only |
| Date | 2026-09-27 |
| Lane B | None exists for this module; see section 6 |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. All 19 A1 claims are source-grounded; no claim is contradicted on its WHAT. 17 VERIFIED, 2 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE.
2. PARTIALs: C07 (timezone "localization" does not change the KPI windows in the way A1 states; windows are rolling durations from now) and C09 (failure-handling RISK framing incomplete: mail is only queued in the digest run, so real delivery failures never reach the digest's catch, and a mid-digest failure can leave partial sends that repeat next run).
3. Material multi-company omissions (section 5) — notably the company label/currency vs KPI-company mismatch and the default digest auto-subscribing users of every company — are additive and routable to Reconciliation/Proof; they do not require A1 rework before REC. Handoff: Reconciliation, carrying 10 proof requirements.

## 2. Test plan (predeclared before verification)

Predeclared plan file sha256 `383d583a3b1f2b0d905aedebffadb24496e14d6529551f44a88f6680d6d56fff` (scratchpad, shared bus/digest plan written before semantic re-reading).

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP-D1 | Lineage: sha256 of A1 package and Lane A packet; A1 header value for Lane A hash | Equal | PASS |
| TP-D2 | Re-fetch 12 digest files at anchor (manifest, ACL, digest/tip/users/settings models, portal controller, 4 data files, backend views); recompute blob SHA-1 | Equal to Lane A pointer table | PASS (12/12, incl. all 7 A1 spot-check files) |
| TP-D3 | Semantic re-read of every HIGH claim (C01–C06, C09–C13, C15, C17) and CRQ/contradiction items (C03, C04, C06, C08, C10, C11, C12, C15, C19, X1, X2) | Claim meaning matches source behavior | Done; section 3 |
| TP-D4 | Re-read MED "Lane A only" claims (C07, C08, C14, C16, C18, C19) | Same | Done |
| TP-D5 | Business framing: periodic KPI digest in multi-company SaaS ERP | No overclaim; no material omission of company/recipient/delivery risk | SF-D01..SF-D06 |
| TP-D6 | Omission scan: digest model, portal controller, users extension, views, email template, data | Material behaviors absent from A1 recorded | OM-D01..OM-D08 |
| TP-D7 | Lane B classification | Never FAIL for absence | Section 6 |
| TP-D8 | Proof requirements | Falsifiable, expected + fail | Section 7 (10 items) |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| A1-G01-DGST-C01 | HIGH | VERIFIED | Manifest: depends mail, portal, resource; no auto-install key (default off). "Internal users" follows from the recipient domain and auto-subscribe filter. |
| A1-G01-DGST-C02 | HIGH | VERIFIED | Four ACL rows: ERP manager full CRUD on digest and tip; internal user read-only on both. |
| A1-G01-DGST-C03 | HIGH | VERIFIED | Manifest data list has no record-rule file; company field optional, default current company; no company check on read paths. Menu restricted to ERP manager; ACL read open to all internal users. |
| A1-G01-DGST-C04 | HIGH | VERIFIED | Messages KPI counts by date window, comment subtype and three message types, with no company term; connected-users KPI uses the company helper. Refinement: evaluation runs as the recipient with the company context narrowed to the recipient's default company, so the effective aggregation boundary is the framework's message-visibility rule under that single-company context — runtime-dependent (PR-DGST-02). |
| A1-G01-DGST-C05 | HIGH | VERIFIED | Helper uses digest company, or current company when unset; users model filtered on its multi-company field; others on single company field. |
| A1-G01-DGST-C06 | HIGH | VERIFIED | Per-window evaluation as the recipient and under the recipient's default company; only access errors are caught and the KPI is dropped from the list silently. Other exceptions propagate and abort the send. |
| A1-G01-DGST-C07 | MED | PARTIAL | Three windows with preceding-window comparison verified. "Window anchor localized to company working-calendar timezone" is overstated: the code attaches the calendar timezone to a UTC wall-clock value without converting it, and the windows are rolling offsets from the current instant (not calendar days); the timezone therefore does not align windows to local days. Also the company used is the recipient's default company, not the digest company. Exact effect on persisted query strings is framework-dependent (PR-DGST-04). |
| A1-G01-DGST-C08 | MED | VERIFIED | KPI discovery by boolean fields with the three prefixes, admitting custom/studio fields. |
| A1-G01-DGST-C09 | HIGH | PARTIAL | Facts verified: daily cron as root; selects activated digests due by today; only the mail-delivery exception type is caught. RISK framing incomplete: (a) the digest run only *queues* mail records, so actual SMTP failures occur later in the mail queue and never reach this catch — the digest advances its next date regardless; (b) there is no per-digest savepoint, so if the caught exception fires after some recipients were queued, those mails persist while the digest remains due, producing repeats next run; (c) an uncaught exception's effect on already-processed digests (abort remaining vs roll back whole run) is framework-dependent. |
| A1-G01-DGST-C10 | HIGH | VERIFIED | Slowdown computed only when the update flag is set; manual send passes it off. Slowdown triggers when no recipient has any login log since the window limit; escalation capped at quarterly. |
| A1-G01-DGST-C11 | HIGH | VERIFIED | Tip HTML field declared with sanitization off; each tip rendered by the mail rendering mixin under elevated rights with the template engine, then sanitized. Tips writable by ERP manager. |
| A1-G01-DGST-C12 | HIGH/LOW | VERIFIED | Route auth=user, no method restriction, ERP-manager group check, value whitelist, then change on the browsed id without ownership/company check; link embedded in email preferences for daily digests to ERP managers. CSRF effect remains LOW/framework (not asserted by A2). |
| A1-G01-DGST-C13 | HIGH | VERIFIED | POST-only, CSRF disabled with MUA rationale; token is HMAC with fixed scope over (digest id, user id); constant-time compare; mismatch → not found. |
| A1-G01-DGST-C14 | MED | VERIFIED | Without token/user id, only a non-share logged-in user acting on self. (See OM-D03 for the tokenized GET path A1 did not cover.) |
| A1-G01-DGST-C15 | HIGH | VERIFIED | Send Now / Activate / Deactivate buttons, KPI General/Custom sections, Recipients page and next date field shown to system group; menus for ERP manager; ACL write for ERP manager. |
| A1-G01-DGST-C16 | MED | VERIFIED | Recipient restriction is a field domain (UI) only; auto-subscribe filters share users; no constraint. |
| A1-G01-DGST-C17 | HIGH | VERIFIED | Mail record created under elevated rights, outgoing, auto-delete; subject = recipient's company name + digest name; sender = digest company partner email → current user → root. |
| A1-G01-DGST-C18 | MED | VERIFIED | On user creation, non-share users added to the configured digest when both params are set; params seeded (enable = True, id = default digest, noupdate). Default digest record (daily, admin recipient, both base KPIs, next date = install date) lives in the tips data file, not the main digest data file. |
| A1-G01-DGST-C19 | MED | VERIFIED | Manual and scheduled share one send routine that sets the next date after sending. |

Totals: VERIFIED 17 · PARTIAL 2 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

A1 contradiction/CRQ items: REFINEMENT on Lane A #17 confirmed. CANDIDATE-DGST-X1 and X2 agreed as layered-control mismatches, not code contradictions. CRQ-DGST-01..08 are well-founded; CRQ-DGST-02 should be widened by OM-D01/OM-D02 (label/currency company vs KPI company), CRQ-DGST-04 by OM-D03 (tokenized GET unsubscribe), CRQ-DGST-08 by C09 PARTIAL.

## 4. Semantic / business findings

- SF-D01 (company semantics): A digest has three different company notions — digest company (company-based KPI filter and sender), recipient default company (evaluation context, subject line, header name, currency formatting, timeframe calendar), and none (messages KPI). A1 identifies the third but not the first/second split (OM-D01).
- SF-D02 (silent omission vs zero, C06): Correct and business-critical. Additionally, because evaluation is narrowed to the recipient's default company, a company-based KPI for a different digest company can return zero through record-rule filtering rather than raising an access error — so "zero", "restricted" and "dropped" are three indistinguishable outcomes for the reader (OM-D02).
- SF-D03 (period comparison): The connected-users KPI is based on each user's last login timestamp, so the preceding-window value counts only users whose *latest* login fell there; the margin is not a true period-over-period metric. A1 carries margin arithmetic from Lane A but not this meaning issue.
- SF-D04 (scheduling semantics): Next date uses server date without company timezone; a single cron run serves all companies; manual send shifts the schedule (C19) — A1 framing correct; together these mean delivery date is server-local, not tenant-local.
- SF-D05 (privilege model, C11/C15): Correct. Framing note: the magnitude of the ERP-manager vs system gap depends on what the ERP-manager group can already do in the platform (framework), so the RISK should be stated as "non-system editor content executed with elevated rights", which A1 does.
- SF-D06 (audit, C17): Auto-delete plus no run log means there is no durable evidence of who received which figures — relevant for KPI confidentiality reviews in a multi-company tenant. A1 captures this in GAP-DGST-07.

## 5. Omissions (material, not in A1)

- OM-D01 Company label/currency mismatch: subject/header use the recipient's default company name and monetary KPIs are formatted with that company's currency, while company-based KPI values are computed for the digest company. The seeded default digest takes the installing company and auto-subscription adds new internal users of every company, so multi-company tenants get digests labelled with one company and computed for another by default.
- OM-D02 Zero-by-rule path (see SF-D02).
- OM-D03 Tokenized unsubscribe over GET: the email body's unsubscribe link targets the legacy route with token and user id, and that route accepts GET; a link scanner or prefetcher can unsubscribe the recipient — the exact scenario the POST-only one-click route is designed to avoid. Tokens have no expiry or rotation beyond the database secret.
- OM-D04 Delivery is asynchronous (see C09 PARTIAL): digest success ≠ mail delivered; partial per-recipient queueing without savepoint.
- OM-D05 Self-subscription: subscribe/unsubscribe actions are public methods that write membership with elevated rights for any internal user acting on self, with no company check; combined with open read ACL, an internal user could join any company's digest (reachability via RPC is runtime — PR-DGST-10). No subscribe button in the shipped form.
- OM-D06 Connected-users KPI meaning (SF-D03).
- OM-D07 Timeframe/timezone handling (C07 PARTIAL) and server-date scheduling (SF-D04).
- OM-D08 Recipients who later become share users remain recipients (no constraint, no cleanup) — extends C16.

## 6. Lane B classification

No Lane B evidence exists in the repository for `digest`. Absence is not a failure.

| Claim | Classification |
|---|---|
| C01, C02, C08 | NOT_APPLICABLE (static declaration) |
| C05, C10, C13, C14, C15, C16, C17, C18, C19 | UNCORROBORATED (runtime-observable, not inherently runtime-dependent) |
| C03, C04, C06, C07, C09, C11, C12 | MISSING_REQUIRED_RUNTIME_PROOF |

## 7. Proof requirements

All in an authorized, isolated test instance; no production mail delivery; tip-template test uses a harmless marker expression only.

| PR | Claim(s) | Procedure | Expected | Fail condition |
|---|---|---|---|---|
| PR-DGST-01 | C03 | Internal user of company B (no ERP manager) reads digest and tip records created for company A via RPC | Records readable | Access denied or filtered |
| PR-DGST-02 | C04 | Recipient with access to companies A and B, default A; comment messages created on documents of B in the window | Determine whether B messages are counted | Recorded either way; RISK stands only if counted |
| PR-DGST-03 | C06, OM-D02 | Recipient lacking access to a KPI source model; second recipient with access but different default company | First: KPI absent with no notice; second: zero or restricted value | KPI shown with a denial label or error |
| PR-DGST-04 | C07, OM-D07 | Company calendar timezone far from UTC; records created at local-day boundary; send digest | Windows are rolling from send instant, not local calendar days | Windows align to local calendar days |
| PR-DGST-05 | C09, OM-D04 | Force the caught mail exception after first recipient is queued; rerun cron | First recipient receives duplicate on rerun; digest remained due | No duplicate / next date advanced |
| PR-DGST-06 | C11 | ERP manager (non-system) stores a tip containing a harmless template expression revealing execution identity; send | Expression evaluated with elevated identity, output sanitized | Expression rendered as literal text |
| PR-DGST-07 | C12 | Authenticated ERP manager follows a cross-site GET to the periodicity route for a digest of another company | Periodicity changes | Request rejected (CSRF/method/ownership) |
| PR-DGST-08 | OM-D01 | Digest company A, recipient default company B with different currency; monetary KPI present | Subject/header/currency show B, values computed for A | Labels and values from the same company |
| PR-DGST-09 | OM-D03 | Issue plain GET to the email unsubscribe link (no session) | Recipient unsubscribed | GET refused or confirmation required |
| PR-DGST-10 | OM-D05 | Internal user of company B calls the subscribe action on company A's digest via RPC | User added as recipient | Refused |

## 8. Limitations

- Single anchor commit; email template bodies read for links and company/currency usage only; tips data read for the default digest record and tip groups; framework internals (CSRF on GET, record-rule defaults, message visibility, datetime serialization, cron transaction scope, ERP-manager group powers) not read.
- Nothing here is runtime proof; section 7 defines what would be.
- No Formal Coverage claim; no percentages; no QID answered; bank used as topic lens only.
- Clean room: neutral WHAT/WHY/RISK; identifiers are evidence pointers; no code reproduced.
- A1 package and Lane A packet were not modified. No git operations performed.
