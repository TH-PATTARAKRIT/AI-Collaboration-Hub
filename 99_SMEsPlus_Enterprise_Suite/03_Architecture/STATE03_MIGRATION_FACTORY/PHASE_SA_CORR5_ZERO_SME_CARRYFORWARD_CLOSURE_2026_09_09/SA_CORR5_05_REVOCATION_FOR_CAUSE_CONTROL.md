# SA_CORR5_05 — REVOCATION-FOR-CAUSE CONTROL

## CP-SA-C5-50 — REVOCATION-FOR-CAUSE SA-SPEC COMPLETE

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **E** · Closes: **`C4-08-F-02`**
Boss: **SOLE FINAL APPROVER**

---

## 1. The finding this closes, at primary text

`SA_CORR4_08` §6.1: `CF-I-03` §3.4 reads the grant **in force at the act's timestamp**; §6.5 answers
the objection — *an act by an authority since revoked for cause should not be certified conformant* —
by saying revocation for cause is *"a separate finding over the same act."* A challenger searched the
whole corpus for *grant validity · grantor authority · void grant · rescind · retroactive revocation ·
fraudulent grant · compromised credential* and returned **zero hits, every term**. Consequence, verbatim:
*"an actor whose grant was obtained fraudulently, or issued by a grantor who lacked authority, is
certified `CONFORMANT` permanently, with no compensating control."*

**Re-measured over `CORR5-FRAME`** (186 heads, case-insensitive, unit = path): `revocation for cause`
**1** — `SA_CORR4_03` §6.5, the sentence that *names* the absence · `rescind`, `fraudulent grant`,
`compromised credential` **1 each — all in `SA_CORR4_08` §6.1, the challenger's own search terms** ·
`void ab initio` **0**. **Outside the two CORR4 files that record the gap, every term returns 0.**
Positive control `git grep -l -i 'revoke' <186 refs> -- '*.md'`, unique paths → **53** (`\brevoked?\b` → 47; a first draft printed 42 from an unpublished shape — `CHA-12`) (`MTI-30`, `FDS_IAM` `FR-IAM-002`/`-010`, `FDS_INTEGRATION`
`FR-INT-002`/`-006`, `ARC-WP-009` §12.7/§12.8/`R-009-02` among them). **The corpus knows revocation as
a *leaver/rotation* event; it has no concept of a grant that was never valid.** The finding reproduces.

### 1.1 What already exists and is consumed, not re-originated (`AUTO-C5-02`)

| Existing position | Content | Used for |
|---|---|---|
| **`MTI-18`** | A legitimate elevation is a named grant carrying **grantor, grantee, reason, scope, expiry and a permanent record** | grant issuance fields |
| **`MTI-30`** (R2) | A deferred run revalidates the **full four-axis `AUTH`** at release; if any axis has *"lapsed, been revoked, narrowed, or its grant expired"* the run does not execute and the non-execution is recorded | effect on future deferred executions |
| **`CF-I-03`** `T3` | *"On grant change — a grant revoked, narrowed or expired triggers a sweep over acts recorded under it"* | **the sweep mechanism already exists**; what it lacks is a result class other than `CONFORMANT`/`BREACH`/`NOT ASSESSABLE` for the swept acts |
| **`CF-I-03`** `I2` | A **historised** grant store — every grant with grantor, grantee, four axes, reason, effective-from, effective-to | the store this control writes to |
| **`MTI-50`** | Control runs retained, context-scoped, inspectable | retention |
| **`ARC-WP-009`** §12.6–12.8 | Privileged access *"time-bound, MFA-enforced and fully audited"*; *"token revocation on subscription/role change"*; leaver → *"immediate deactivation and session/token revocation"*; `R-009-02` stale token after leaver | leaver revocation, token effect (stranded, `DRAFT · HOLD`) |
| **`XMC-C-A8`/`A9`** | Reversal is a new event referencing the original; correction is reversal plus new event, never re-dating | relationship to correction/reversal |
| **`FDS_INTEGRATION`** `FR-INT-002`/`-006` | Secret rotation: *"Old Secret Revoked"*; client disable: *"Token Revoked, Audit Recorded"* | service-credential revocation events |
| **`ENTERPRISE_CONTROL_LAYER`** §12.4 | Overrides *"require an exception record"*; restricted actions always audited | exception-record shape |

> **`C5-05-F-01`. The control is missing exactly one thing: a *validity* dimension on a grant that is
> independent of its *time* dimension.** Every existing mechanism treats a grant as valid from issuance
> until expiry or revocation-by-lifecycle. None can express *"this grant was never valid"* or *"this
> grant became invalid at T, and acts between issuance and T are suspect."* The specification below adds
> that dimension and nothing else.

---

## 2. Control identity

| Field | Value |
|---|---|
| **Control ID** | **`CF-I-03R`** — *Revocation-for-Cause*, the companion of `CF-I-03`. Named as a companion rather than a new `CF-I-09` because it amends no invariant and adds no axis; it adds a **grant-validity state** and a **finding class** the existing control consumes |
| Class | Governance-triggered detective control with one preventive effect (§6.1) |
| Owner | **Boss + SaaS Foundation** (grant store, validity state, sweep — the same owners as `MTI-18`, whose fields §3.1 generalises) **+ the granting authority's owner** (the revocation decision) (`CHA-15`) |
| Layer | `CONTROL` + `GOVERNANCE` |
| Topology | `SHARED SaaS POOL` only (`CF-I-08`) |
| Scope rule | `SCOPE-AWARE EVERYWHERE`: a `PLATFORM` grant is revoked in platform context; a `TENANT`/`COMPANY` grant in its own; **a revocation never crosses a tenant boundary** |
| Status | **`SPECIFIED — NOT BUILT — NOT VERIFIED`**. No other wording |

---

## 3. Grant lifecycle — the validity dimension added

### 3.1 Issuance (carried from `MTI-18`, made general)

Every grant — interactive role, privileged `MTI-18` elevation, service credential, approval authority,
deferred-execution authority — is issued with: **grantor** (an identified principal with authority to
grant, itself under a grant); **grantee**; **four-axis scope** (`CF-I-01`); **reason**;
**effective-from**; **effective-to** (mandatory for privileged grants; `NONE` permitted only for
ordinary role grants and stated as such); and a **permanent record**. A grant with an absent grantor,
scope or effective-from is **not a grant** and is `CF-I-03` `D4`/`D6` on every act under it.

### 3.2 Validity states

| State | Meaning | Reachable from |
|---|---|---|
| **`VALID`** | Issued by an authorised grantor, inside the grantor's own scope, not revoked | issuance |
| **`EXPIRED`** | Effective-to passed. **Not a revocation** | `VALID` |
| **`REVOKED — LIFECYCLE`** | Withdrawn without cause: leaver, mover, rotation, scope narrowing, subscription change. Acts **before** the revocation instant are unaffected | `VALID` |
| **`REVOKED — FOR CAUSE`** | Withdrawn because the grant **should not have been relied on** from a stated instant `T_cause` ≤ revocation instant. Acts at or after `T_cause` are **suspect** | `VALID`, `EXPIRED`, `REVOKED — LIFECYCLE` (a grant may be found to have been invalid after it has already lapsed) |
| **`VOID AB INITIO`** | Never valid: grantor lacked authority, issuance fraudulent, grantee identity false. `T_cause` = effective-from. **Every** act under it is suspect | any state |
| **`SUPERSEDED`** | Replaced by a new grant with its own identity; the old one ends at the new one's effective-from. Not a revocation | `VALID` |

**Every transition is itself an evented, approved act** (`MTI-40`'s pattern applied to grants), carrying
actor, authority, reason, both timestamps, before/after state.

### 3.3 Revocation event — mandatory content

| Field | Rule |
|---|---|
| Revoked grant identity | the grant, never the grantee (a person may hold several) |
| Revocation class | `LIFECYCLE` · `FOR CAUSE` · `VOID AB INITIO` |
| **Reason class** | `FRAUDULENT_ISSUANCE` · `GRANTOR_LACKED_AUTHORITY` · `GRANTEE_IDENTITY_FALSE` · `CREDENTIAL_COMPROMISED` · `POLICY_VIOLATION` · `SEPARATION_OF_DUTIES_BREACH` · `OTHER_STATED` (free text mandatory). Classes are platform-owned and context-independent — the `MTI-33`/`CF-I-05` pattern — so the same reason means the same thing in every tenant |
| **Effective time of revocation** | the instant from which the grant may no longer be relied on for **new** acts |
| **`T_cause`** | the instant from which past acts are **suspect**; `= effective-from` for `VOID AB INITIO`; may not precede effective-from; may not be later than the revocation instant |
| Revoking authority | an identified principal under its own valid grant, **distinct from the grantee** |
| Evidence reference | the investigation, incident or governance record that grounds the cause |
| Emergency flag | §5 |

---

## 4. Effect on executions

### 4.1 Future executions — preventive, immediate

From the revocation instant: every `EP-P` evaluation under the grant **denies** (`CF-I-03` `D1`);
every session/token bound to it is invalidated (`ARC-WP-009` §12.7/12.8, `FDS_IAM` `FR-IAM-010`,
`FDS_INTEGRATION` `FR-INT-006`); every **deferred** execution scheduled under it does not release and
records its non-execution (`MTI-30`). **No grace period exists for `FOR CAUSE` or `VOID AB INITIO`.**

### 4.2 Previously executed transactions — detective, never rewriting

The revocation event triggers `CF-I-03` **`T3`** over every act recorded under the grant from `T_cause`.
`CF-I-03` §3.4 is **not** re-timed: the conformance question *"was the `AUTH` inside a grant in force at
the act's timestamp?"* keeps its answer. **A new, separate result is produced for the same act:**

| New result class | Meaning |
|---|---|
| **`SUSPECT — GRANT REVOKED FOR CAUSE`** | The act was conformant against a grant later found invalid from `T_cause`. Carries the revocation event reference, the reason class and the act reference |

**Why a fourth result and not a re-graded `BREACH`:** the act's own conformance record is evidence of
what the system believed at the time; rewriting it would destroy the evidence that the control was
deceived, which is the audit fact an investigation needs. `CF-I-03` §3.5 *"never repairs, never
back-fills"* is honoured; the revocation adds a layer, it does not edit one.

### 4.3 What happens to a suspect act — the correction relationship

A `SUSPECT` finding **does not itself reverse anything.** It opens a per-act **disposition** owned by
the business owner of the affected context:

| Disposition | Rule |
|---|---|
| `RATIFIED` | The act is confirmed on its merits by an authority that holds a valid grant; the confirmation is an evented act; the `SUSPECT` finding is closed with the ratification reference |
| `REVERSED` | Reversal under `XMC-C-A8` — a **new** event referencing the original; for Inventory, a reversing movement fact (`INV-F-40`); **never deletion, never re-dating** (`A9`) |
| `UNDER INVESTIGATION` | Open, with an owner and a review date; the act remains effective meanwhile unless a period lock or a business hold prevents further downstream effect |

A suspect act's downstream handoff facts are **flagged, not withdrawn**: the emitted `HF-CTX-11`
attestation named a run that was correct when made; the consumer is **notified** of the `SUSPECT`
finding (the `CF-I-03` §3.10 `D3` notification path, reused) and applies its own disposition.

### 4.4 Retroactive investigation without rewriting history

All of the following are **reads over retained evidence** and none is a write to it: the historised
grant store (`I2`) answers *which grants were in force at any instant*; `MTI-38` events answer *which
acts relied on which grant*; `MTI-50` retains every `CF-I-03` run; the revocation event carries
`T_cause`. **An investigation therefore reconstructs the exposure window from stored facts and produces
new findings; it never alters the acts, the runs or the grants it examines.**

---

## 5. Emergency revocation

An `EMERGENCY` revocation is a `FOR CAUSE` or `LIFECYCLE` revocation issued **with reason class
provisional** and **evidence reference deferred**, by a principal holding an emergency-revoke grant
(itself an `MTI-18`-class grant: named, scoped, expiring, recorded). Preventive effect (§4.1) is
**immediate and unconditional**. Detective effect (§4.2) runs immediately with the provisional class.
**Within a bounded interval the provisional reason must be confirmed or the revocation reclassified
`LIFECYCLE`**; an unconfirmed emergency revocation is itself a `CF-I-03R` finding against the revoking
principal. **There is no emergency *grant*; break-glass access (`G4`) remains a name with a future
owner and is not created here.**

---

## 6. Guarantees, stated as testable clauses

| ID | Clause |
|---|---|
| `RFC-01` | No grant may be `VALID` whose grantor did not hold, at issuance, a valid grant whose scope contains the issued scope (`CF-I-01`: no broadening). Issuance outside the grantor's scope is `VOID AB INITIO`. **Status: an invariant-level rule stated here for the first time — `SPECIFIED`, candidate for the `CF-I-*` family at the Inventory owner's next conformance pass** (`CHA-15`) |
| `RFC-02` | Revocation is a state transition on the grant, evented, reasoned, timed, authorised by a principal other than the grantee |
| `RFC-03` | `FOR CAUSE` and `VOID AB INITIO` produce a `SUSPECT` finding for **every** act under the grant from `T_cause`, on **every** context the grant covered — a sweep that returns a population size and a `NOT ASSESSABLE` count beside its finding count (`CF-I-03` §3.11's rule), never a bare count |
| `RFC-04` | A `SUSPECT` act is dispositioned by ratification or reversal; the act, its conformance record and its handoff facts are never edited or deleted |
| `RFC-05` | The exposure window of any revoked grant is reconstructible from retained evidence alone |
| `RFC-06` | A revocation never widens: it cannot grant, cannot cross a tenant, cannot re-scope another grant |
| `RFC-07` | Revoking a grant does not revoke the grants it was used to issue **automatically**; it places them `UNDER REVIEW` and produces a finding per dependent grant. Cascading revocation is an authorised act, not an inference |

---

## 7. Audit evidence and Tenant/Company scope

Every revocation event, every `SUSPECT` finding and every disposition is a `MTI-38` event: full `CTX`,
the four-axis `AUTH` of the revoking principal, actor, two dates, evidence reference. Retained under
`MTI-50`. **Scope:** a tenant-context grant is revoked and swept inside that tenant; a company grant
inside that company; a `PLATFORM` grant (a platform operator's) is revoked in platform context and its
sweep is executed as **N tenant-context control runs, one inside each tenant it acted on, each with its
own result, whose results are lifted to platform context** (`MTI-29`'s rule; the `G5` `T(i)`/`P`
shape) — **it is not a platform-context read of N tenant audit streams**, which would be an
unregistered cross-tenant read path (`CHA-09`); and a platform-context finding never becomes a
tenant-context write.

---

## 8. Test classes — the Pre-Test Matrix's obligation

| ID | Class |
|---|---|
| `RFC-P-01` | Lifecycle revocation → past acts unaffected, future acts denied |
| `RFC-P-02` | For-cause revocation with `T_cause` mid-window → acts before `T_cause` unaffected, acts from `T_cause` `SUSPECT` |
| `RFC-P-03` | `VOID AB INITIO` → every act `SUSPECT`; issuance outside grantor scope detected at issuance (`RFC-01`) |
| `RFC-N-01` | Revocation by the grantee → refused |
| `RFC-N-02` | `T_cause` before effective-from → refused |
| `RFC-N-03` | Revocation attempting to cross a tenant → refused, `D3` |
| `RFC-B-01` | Revocation instant equals an act's timestamp — inclusivity stated |
| `RFC-B-02` | Grant expired, then revoked for cause → sweep still runs over its window |
| `RFC-C-01` | **Synthetic injection**: one act under a grant later voided → `SUSPECT` count `0 → 1` |
| `RFC-C-02` | Sweep coverage: population / assessed / not-assessable published; shortfall fails the run |

---

## 9. What this file does not do

Build anything · discharge `CF-V-01` or any veto · amend `CF-I-03` (it consumes `T3`, `I2`, §3.5, §3.11
unchanged) · design break-glass (`G4`, PMO staffing) · rule `CF-D-02` · create a cross-tenant path ·
define retention periods (a policy decision routed with `MTI-50`'s own open cadence, `MTA-11`).

## 10. Residual

1. **Reason classes are originated here** and reviewed by nobody outside this session. They follow the
   context-independence pattern the corpus already mandates for reason taxonomies (`MTI-33`).
2. **`RFC-07` (no automatic cascade) is a position, not a proof.** The alternative — automatic cascade —
   is coherent and safer against a compromised grantor, and more disruptive. Stated so it can be
   challenged; not escalated, because either reading is a design position within Phase SA authority.
3. **The disposition owner in §4.3 is the *business owner of the affected context*.** Who that is for a
   platform-context act is the same unanswered role question as `G4`'s owner; carried there.

## 11. Checkpoint

> ## `CP-SA-C5-50 — REVOCATION-FOR-CAUSE SA-SPEC COMPLETE`
> **`C4-08-F-02` closed at specification level: 6 validity states · 7 reason classes · 1 new result
> class · 7 guarantees · 10 test classes · 9 existing positions consumed · 1 finding (`C5-05-F-01`).**
> **`CF-I-03R`: `SPECIFIED — NOT BUILT — NOT VERIFIED`. 0 vetoes discharged.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
