# SMEsPlus ENTERPRISE SUITE
## GMVQ — G01 PLATFORM_BASE Standard 35 Adversarial Question Bank

**Document ID:** GMVQ-G01-STD35-V1.00  
**Group:** G01 PLATFORM_BASE  
**Destination:** SAAS_FOUNDATION  
**Authoring Team:** OVQDT / GMVQ  
**Status:** DRAFT / AUTHORING IN PROGRESS / NOT FROZEN  
**Boss Authorization:** APPROVED TO PROCEED WITH G01 QUESTION AUTHORING  
**Lane A / Lane B:** NOT STARTED — module/batch freeze required first  

## Controls

- 35 Standard Questions apply to every module in the frozen batch.
- Every question is behavioral, source-neutral, and has a concrete disconfirming observation.
- NOT_APPLICABLE requires explicit evidence/reason; padding is forbidden.
- SAAS_FOUNDATION outputs are restricted to GAP / REQUIREMENT / RISK / CONSTRAINT / BUSINESS INVARIANT.
- No source-derived schema, technical identifiers, API shapes, ORM relationships, algorithms, or copied implementation patterns.
- module + QID is a Research Evidence Join Key only, not a Canonical Function-ID or Formal Coverage denominator.
- Lane A and Lane B answer the same frozen QIDs independently.

## Q01 — Cross-customer direct isolation

```yaml
QID: G01-STD-Q01
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A user in one independent customer context cannot view, search, modify, export, or act on records belonging exclusively to another independent customer context.
WHY_IT_MATTERS: >
  Failure is cross-customer data leakage and breaks the primary SaaS security boundary.
DISCONFIRMING_OBSERVATION: >
  A user in Customer A can discover or act on a Customer B record through any normal path.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Two independent customer contexts with distinct users and distinguishable records.
```

## Q02 — Indirect relationship boundary bypass

```yaml
QID: G01-STD-Q02
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Following related records, references, history, or activity links never weakens the current customer boundary.
WHY_IT_MATTERS: >
  Direct access may be blocked while indirect traversal still exposes restricted data.
DISCONFIRMING_OBSERVATION: >
  A permitted record contains a relationship path that opens or reveals data from another customer context.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Related records exist on both sides of the customer boundary.
```

## Q03 — Search and suggestion leakage

```yaml
QID: G01-STD-Q03
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Search, autocomplete, recent items, suggestions, and reference pickers reveal only records permitted in the active execution context.
WHY_IT_MATTERS: >
  Metadata leakage can disclose sensitive facts even when record opening is blocked.
DISCONFIRMING_OBSERVATION: >
  A restricted record appears in search results, suggestions, counts, recent items, or pickers.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restricted records contain unique distinguishable values.
```

## Q04 — Aggregate and count leakage

```yaml
QID: G01-STD-Q04
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Counts, totals, grouped summaries, dashboards, and aggregate results use only data visible in the active execution context.
WHY_IT_MATTERS: >
  Hidden rows must not leak through totals or existence information.
DISCONFIRMING_OBSERVATION: >
  A total, count, group, graph, or summary changes because of records the user cannot otherwise see.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Visible and restricted records have materially different totals.
```

## Q05 — Export and bulk-read isolation

```yaml
QID: G01-STD-Q05
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Export, download, print, batch read, and bulk selection enforce the same data boundary as normal on-screen use.
WHY_IT_MATTERS: >
  Alternate read paths can bypass interactive filtering and cause high-volume leakage.
DISCONFIRMING_OBSERVATION: >
  An export, printout, download, or bulk result contains restricted records or fields.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Permitted and restricted records exist in the same logical area.
```

## Q06 — Attachment and linked-content isolation

```yaml
QID: G01-STD-Q06
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Attached files, generated documents, previews, thumbnails, and shared content inherit the same customer and permission boundary as the parent object.
WHY_IT_MATTERS: >
  File access can survive after parent access is denied.
DISCONFIRMING_OBSERVATION: >
  A user who cannot access the parent record can still retrieve its attachment, preview, or generated file.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  A restricted record has an attachment or generated document.
```

## Q07 — Multi-tab execution-context confusion

```yaml
QID: G01-STD-Q07
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When one user belongs to multiple customer contexts, separate tabs remain bound to each tab's explicit context and never silently inherit the other tab's context.
WHY_IT_MATTERS: >
  Context confusion can create cross-customer writes without visible permission bypass.
DISCONFIRMING_OBSERVATION: >
  Switching or acting in one tab causes another tab to read or write under the wrong customer context.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  One user has legitimate membership in two distinct customer contexts and two tabs are open.
```

## Q08 — Company-context switch with open record

```yaml
QID: G01-STD-Q08
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing company context while a record is open cannot cause that record to be saved or processed under an unintended company.
WHY_IT_MATTERS: >
  Stale screens can write valid data into the wrong legal/accounting boundary.
DISCONFIRMING_OBSERVATION: >
  A record opened under Company A is committed under Company B or gains Company B defaults without an explicit safe transition.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  User has access to two companies and an editable record is open before switching context.
```

## Q09 — Permission revocation during in-flight action

```yaml
QID: G01-STD-Q09
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If permission is revoked after an action starts but before commit, authority is revalidated at the decisive point and unauthorized completion is prevented.
WHY_IT_MATTERS: >
  Long-lived forms or sessions must not preserve authority indefinitely after revocation.
DISCONFIRMING_OBSERVATION: >
  A user completes a restricted action after the required permission has been removed.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  User starts an action and an administrator revokes the needed permission before final commit.
```

## Q10 — Permission grant propagation consistency

```yaml
QID: G01-STD-Q10
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Newly granted access becomes effective consistently across equivalent supported paths without unpredictable allow/deny divergence.
WHY_IT_MATTERS: >
  Inconsistent propagation creates non-reproducible behavior and hidden bypasses.
DISCONFIRMING_OBSERVATION: >
  The same user and context receive materially different authorization outcomes across equivalent paths after the grant.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Begin with access denied, grant a permission, then exercise equivalent paths during propagation.
```

## Q11 — Session expiry during state-changing operation

```yaml
QID: G01-STD-Q11
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a session expires during a state-changing action, the result is safely committed once or not committed at all; it is never half-applied without recovery state.
WHY_IT_MATTERS: >
  Session expiry can expose atomicity defects and inconsistent state.
DISCONFIRMING_OBSERVATION: >
  Some effects are visible while other required effects are missing, with no explicit recoverable status.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use an action with multiple observable effects and force expiry immediately before or during completion.
```

## Q12 — Concurrent update lost-update protection

```yaml
QID: G01-STD-Q12
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two authorized users edit the same object concurrently, one user's committed changes are not silently overwritten by stale data from the other.
WHY_IT_MATTERS: >
  Lost updates corrupt business truth without obvious error.
DISCONFIRMING_OBSERVATION: >
  The later save silently removes or replaces the first user's committed changes without conflict handling or traceability.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Two authorized sessions open the same record before either saves.
```

## Q13 — Duplicate-submit and retry idempotency

```yaml
QID: G01-STD-Q13
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Repeating the same state-changing request because of double-click, timeout, or uncertainty cannot create duplicate business effects.
WHY_IT_MATTERS: >
  Duplicate execution can create duplicated documents, postings, notifications, or allocations.
DISCONFIRMING_OBSERVATION: >
  One intended action creates more than one durable effect when submitted repeatedly under ambiguous feedback.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use an action that produces a uniquely identifiable durable result and intentionally repeat submission.
```

## Q14 — Partial-failure atomicity

```yaml
QID: G01-STD-Q14
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a mandatory step in a multi-step operation fails, dependent effects do not remain committed unless a controlled partial-success state and recovery path are explicit.
WHY_IT_MATTERS: >
  Silent partial success creates unreconcilable business and audit states.
DISCONFIRMING_OBSERVATION: >
  A mandatory later step fails but earlier effects remain durable with no explicit partial status or compensation path.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger an operation with multiple required effects and make a later mandatory step fail.
```

## Q15 — Ambiguous timeout recovery

```yaml
QID: G01-STD-Q15
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  After a timeout where the user cannot know whether the action succeeded, the system provides a trustworthy way to determine the authoritative outcome before retry.
WHY_IT_MATTERS: >
  Ambiguous outcomes cause accidental duplicate actions.
DISCONFIRMING_OBSERVATION: >
  No trustworthy success/failure outcome is available and retry can create a second durable effect.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a client-visible timeout during a state-changing operation and inspect the resulting state.
```

## Q16 — Background job respects execution boundary

```yaml
QID: G01-STD-Q16
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Automated background work executes under an explicit auditable customer/company scope and cannot process records outside that scope.
WHY_IT_MATTERS: >
  Background execution is a common route for cross-tenant leakage and unauthorized mass changes.
DISCONFIRMING_OBSERVATION: >
  An automated task reads or changes records from an unintended customer or company context.
EXPECTED_SURFACE: S4,S5,S6
PRECONDITIONS: >
  Similar eligible records exist in two separate scopes before the automated task runs.
```

## Q17 — Configuration change during background execution

```yaml
QID: G01-STD-Q17
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If configuration changes while a long-running job executes, one logical run remains deterministic and auditable and does not silently mix incompatible rule versions.
WHY_IT_MATTERS: >
  Mixed-rule processing makes results impossible to reproduce or reconcile.
DISCONFIRMING_OBSERVATION: >
  Records in one logical run follow different rule sets solely because configuration changed mid-run, with no version trace.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Start a multi-record job, change relevant configuration during the run, and compare early vs late results.
```

## Q18 — Stale authorization cache after revocation

```yaml
QID: G01-STD-Q18
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Authorization revocation invalidates or safely expires cached permission state quickly enough that restricted actions cannot continue through stale authorization.
WHY_IT_MATTERS: >
  Correct stored policy is insufficient if stale runtime permission remains active.
DISCONFIRMING_OBSERVATION: >
  A revoked user continues restricted actions for a material period because a prior authorization decision remains cached.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  User exercises valid access, then loses it while the session remains active.
```

## Q19 — Default-value scope contamination

```yaml
QID: G01-STD-Q19
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Automatically suggested or inherited defaults come only from the active customer/company context unless an explicitly shared rule is authorized.
WHY_IT_MATTERS: >
  Cross-scope defaults can silently inject another company's control values into new data.
DISCONFIRMING_OBSERVATION: >
  A new record receives a default value owned exclusively by another context.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure distinguishable default candidates in two scopes and create records in each.
```

## Q20 — Copy/duplicate unsafe carry-over

```yaml
QID: G01-STD-Q20
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Copying or duplicating recalculates ownership, scope, permission-sensitive defaults, and lifecycle state rather than carrying unsafe control values.
WHY_IT_MATTERS: >
  Duplication can bypass creation controls and preserve hidden security-sensitive metadata.
DISCONFIRMING_OBSERVATION: >
  A duplicate inherits restricted ownership, scope, state, or permission-derived values that a newly created equivalent would not receive.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Duplicate a record containing context-specific ownership or control values.
```

## Q21 — Archive/delete orphan access

```yaml
QID: G01-STD-Q21
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a parent object is archived, disabled, or removed, dependent links and historical paths do not become unintended operational access routes.
WHY_IT_MATTERS: >
  Orphaned relationships can preserve access after normal navigation is closed.
DISCONFIRMING_OBSERVATION: >
  A dependent or historical link still permits an action or data view that the parent object's new state should prohibit.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create references or attachments, change parent availability, then retest indirect paths.
```

## Q22 — Shared reference data ownership rules

```yaml
QID: G01-STD-Q22
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: >
  Data visible across multiple companies or customers has explicit rules that distinguish visibility, ownership, edit authority, and financial/operational scope.
WHY_IT_MATTERS: >
  Shared visibility is often mistaken for shared ownership and can cause cross-company contamination.
DISCONFIRMING_OBSERVATION: >
  A user alters shared-looking data in a way that changes another company's behavior without explicit shared-governance authority.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Identify data visible in more than one scope and compare read/write effects from each scope.
```

## Q23 — Time-zone and date-boundary consistency

```yaml
QID: G01-STD-Q23
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  The same business event has one authoritative date/time interpretation across user time zones and boundary transitions do not move it into an unintended day or period.
WHY_IT_MATTERS: >
  Date drift can alter cut-off, reporting, sequencing, and audit interpretation.
DISCONFIRMING_OBSERVATION: >
  The same event is treated as belonging to different business dates or periods solely because the acting user's time zone changed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use two users with different time zones and process an event near a day boundary.
```

## Q24 — Unique numbering under concurrency and scope

```yaml
QID: G01-STD-Q24
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Identifiers that must be unique remain unique under concurrent creation and obey the intended customer/company scope without accidental sharing or collision.
WHY_IT_MATTERS: >
  Duplicate or cross-scope numbering damages auditability and traceability.
DISCONFIRMING_OBSERVATION: >
  Concurrent actions produce duplicate identifiers or draw identifiers from another scope's sequence.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger near-simultaneous creation in the same scope and in two different scopes.
```

## Q25 — Upload metadata and file-content boundary

```yaml
QID: G01-STD-Q25
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Uploaded content, filename, preview metadata, extracted text, and derived artifacts remain constrained by the same authorization boundary as the parent throughout their lifecycle.
WHY_IT_MATTERS: >
  Derived metadata can leak even when raw-file download is restricted.
DISCONFIRMING_OBSERVATION: >
  Restricted content or metadata is visible through preview, search, index, thumbnail, or another derived representation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Upload uniquely identifiable content to a restricted record and probe all available representations from an unauthorized context.
```

## Q26 — Notification and recipient isolation

```yaml
QID: G01-STD-Q26
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Notifications, reminders, and recipient lists are recalculated from current authorization and ownership before delivery.
WHY_IT_MATTERS: >
  A protected record can leak through stale or over-broad notifications.
DISCONFIRMING_OBSERVATION: >
  A user who no longer has access receives restricted content, identifier, or link that reveals protected information.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Schedule or trigger a notification, then change recipient authorization before delivery.
```

## Q27 — Audit trail completeness and immutability

```yaml
QID: G01-STD-Q27
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Material state, permission, ownership, configuration, and scope changes create durable history identifying what changed, who or what caused it, and when; ordinary users cannot silently rewrite that history.
WHY_IT_MATTERS: >
  Without trustworthy history, incidents and disputes cannot be reconstructed.
DISCONFIRMING_OBSERVATION: >
  A material change has no durable trace, the actor cannot be identified, or a normal user can alter/remove history without equivalent audit evidence.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Perform one material user change and one automated change, then inspect historical evidence.
```

## Q28 — Automated action accountable identity

```yaml
QID: G01-STD-Q28
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: REQUIREMENT
HYPOTHESIS: >
  Automated actions are distinguishable from human actions and preserve enough initiating context to determine why the automation executed.
WHY_IT_MATTERS: >
  Generic system identities make root-cause analysis and accountability impossible.
DISCONFIRMING_OBSERVATION: >
  An automated change is indistinguishable from an unexplained generic user action or cannot be linked to its initiating rule/event.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Trigger one comparable action manually and one through automation, then compare audit evidence.
```

## Q29 — Restore/recovery preserves isolation

```yaml
QID: G01-STD-Q29
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Recovery, restore, rollback, or repair preserves customer/company boundaries and does not reintroduce records, permissions, or files into the wrong scope.
WHY_IT_MATTERS: >
  Recovery tooling can bypass normal controls and cause high-impact cross-tenant contamination.
DISCONFIRMING_OBSERVATION: >
  A restored or repaired object becomes visible, owned, or actionable in an unintended customer/company context.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Use controlled test data with distinguishable ownership before and after a recovery or repair operation.
```

## Q30 — Bulk operation scope and partial-error behavior

```yaml
QID: G01-STD-Q30
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bulk actions enforce authorization per affected record and expose deterministic outcomes when only some selected records are valid.
WHY_IT_MATTERS: >
  Bulk processing can bypass per-record checks or create silent partial updates.
DISCONFIRMING_OBSERVATION: >
  A bulk action modifies a restricted record, silently skips failures without trace, or leaves an unexplained partial state.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Select a mix of permitted, restricted, valid, and invalid records where the interface allows it.
```

## Q31 — Noisy-neighbor resource fairness

```yaml
QID: G01-STD-Q31
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONSTRAINT
HYPOTHESIS: >
  Heavy activity in one customer context cannot consume shared capacity without control to the point that unrelated customers lose critical availability or correctness.
WHY_IT_MATTERS: >
  Shared SaaS must contain noisy-neighbor impact.
DISCONFIRMING_OBSERVATION: >
  High load in Customer A causes sustained critical failure, starvation, or data-processing error in unrelated Customer B without protective control.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Two isolated customer contexts are active; one generates sustained load while the other performs a stable reference transaction.
```

## Q32 — Failure isolation between customers

```yaml
QID: G01-STD-Q32
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A malformed, failing, or repeatedly retried workload from one customer cannot corrupt or indefinitely block unrelated customers' work.
WHY_IT_MATTERS: >
  Fault isolation is required for secure and reliable shared SaaS operation.
DISCONFIRMING_OBSERVATION: >
  A failure loop or malformed workload in one customer causes unrelated valid operations to fail, corrupt, or remain indefinitely blocked.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Run a deliberately failing/retrying workload in one context while executing a stable control scenario in another.
```

## Q33 — Upgrade/migration preserves boundary semantics

```yaml
QID: G01-STD-Q33
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  After an upgrade, migration, or configuration-version change, historical records preserve intended ownership and permission semantics unless a controlled migration explicitly changes them.
WHY_IT_MATTERS: >
  Migration defects can expose historical data even when new records behave correctly.
DISCONFIRMING_OBSERVATION: >
  Historical records become newly visible, editable, re-owned, or differently scoped without an explicit migration rule and evidence.
EXPECTED_SURFACE: S1,S3,S4,S6
PRECONDITIONS: >
  Capture a controlled before-state for records with distinct ownership/permission, perform the version change, and retest identical access scenarios.
```

## Q34 — Equivalent paths enforce equivalent controls

```yaml
QID: G01-STD-Q34
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The same business action through interactive, bulk, automated, import, or other supported paths is subject to equivalent authorization, validation, scope, and audit controls.
WHY_IT_MATTERS: >
  Security and integrity defects often exist only in alternate execution paths.
DISCONFIRMING_OBSERVATION: >
  An action blocked or validated in one supported path succeeds through another without equivalent control or traceability.
EXPECTED_SURFACE: S1,S4,S5,S6
PRECONDITIONS: >
  Identify at least two supported ways to perform the same effect and execute them under the same user/context conditions.
```

## Q35 — Conflicting state transitions under race

```yaml
QID: G01-STD-Q35
TYPE: STANDARD
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When two authorized actors or processes attempt incompatible state changes nearly simultaneously, resolution is deterministic and the final state is coherent and fully traceable.
WHY_IT_MATTERS: >
  Race conditions can create impossible states that ordinary happy-path tests never reveal.
DISCONFIRMING_OBSERVATION: >
  Both incompatible actions appear successful, the final state contains effects from both without a defined rule, or history cannot explain which action prevailed.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Choose two materially incompatible actions that are both initially authorized and execute them as close together as practicable.
```

---

## Internal authoring checklist

- [x] Exactly 35 Standard QIDs authored.
- [x] Every question has DISCONFIRMING_OBSERVATION.
- [x] Behavioral / source-neutral language only.
- [x] Boundary, concurrency, failure, recovery, negative-path and isolation challenges included.
- [x] No Formal Coverage claim from question count.
- [ ] Exact G01 23-module membership reconciled and evidence-linked.
- [ ] Per-module MVQ authored and QA-gated.
- [ ] Module/batch question bank Boss-frozen before Lane A/Lane B starts.

**Disposition:** AUTHORING IN PROGRESS / NOT FROZEN / LANE A HOLD / LANE B HOLD
