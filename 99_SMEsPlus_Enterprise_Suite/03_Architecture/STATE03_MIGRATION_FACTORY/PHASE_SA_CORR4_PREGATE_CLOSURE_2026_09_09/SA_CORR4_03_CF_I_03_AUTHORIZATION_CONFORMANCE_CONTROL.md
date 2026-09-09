# SA_CORR4_03 — `CF-I-03` AUTHORIZATION CONFORMANCE CONTROL

## CP-SA-C4-30 — `CF-I-03` SPECIFIED AND LINKED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Condition closed: **`C4-03`**
Boss: **SOLE FINAL APPROVER**

---

## 1. The finding that changes what this condition is

CORR3 set `C4-03` as a **design act**: *"Specify `CF-I-03`, the authorization conformance control.
Until it exists, `MTI-43`'s second attestation is a reference to nothing."* Its register states the
gap twice, in the absolute:

> `SA_CORR3_07` §3.1: *"**`CF-I-03`** — **the load-bearing absence in the whole set:** the authorization
> conformance control **does not exist**"*
> `SA_CORR3_07` §5.1: *"**The control does not exist.** **No published invariant states it**; a veto
> forbids recording the field as available meanwhile"*

**Both sentences are falsified against primary text.**

> ### `C4-03-F-01` — `CF-I-03` is a published invariant, it states the control, and CORR3 counted it
>
> `.../REOPEN_PROGRAM_2026_09_02/INVENTORY_REOPEN/MTI_RULING_CONFORMANCE_EXECUTION/`
> `03_MTI_INVARIANT_SET_R2_CONFORMED.md` **§13** *"The Eight Invariants The Rulings Require To Be
Added"*, the `CF-I-*` table, **row 3**, verbatim *(this file first cited §14; §14 is "Internal
Consistency Of The Conformed Set" — corrected by independent challenge, the quotation itself was
accurate)*:
>
> > **`CF-I-03`** — *"A continuous authorization conformance control asserts, for every recorded act,
> > that the `AUTH` it records was within a grant in force at the time of the act; that no act is
> > recorded with an absent axis where the acted-on object carries that axis; and that no grant spans
> > more than one company. Breach raises; it does not silently repair. Its runs are retained,
> > context-scoped and inspectable, and are what `HF-CTX-11` references."*
> > Owner `SaaS Foundation + Inventory` · Layer `CONTROL` · Status **`SPECIFIED`** · lineage `CF-F-05`,
> > `CD-28`, the `AUTH` analogue of `MTI-19`, `MTI-50`.
>
> **`CF-I-03` is one of the eight `CF-I-*` invariants that make CORR3's own denominator 58** — and
> `SA_CORR3_07`'s own **UNIT** clause defines a member as *"one row whose leading table cell is an
> invariant identifier and which carries an R2 status."* `CF-I-03` is exactly such a row and carries
> exactly such a status. **CORR3's register counts `CF-I-03` as a defined, published, `SPECIFIED`
> invariant in one section and states that no published invariant states it in another.**

### 1.1 Where the wording came from, and the exact defect

The absolute form is **inherited, not invented**. Its source is bounded, and the boundary was dropped.

| Instrument | Verbatim | Scope |
|---|---|---|
| `03_MTI_INVARIANT_SET_R2_CONFORMED.md` §12.13 | *"`HF-CTX-11` references a control that `CF-I-03` requires and that **is not stated by any of the 50 published invariants**"* | **Bounded** — the 50 carried. `CF-I-03` is one of the **8 added** and is therefore outside the sentence's own subject |
| `04_CTX_AUTH_RELATIONSHIP_AND_AXIS_MODEL.md` §5.3 table, last row | *"`CF-I-03` authorization conformance control — **which does not exist**"* | **Unbounded** |
| `04_CTX_AUTH_RELATIONSHIP_AND_AXIS_MODEL.md` §10 status table | *"Does authorization have a conformance control? **No** — `CF-F-05`, **`CF-I-03` specified and not built**"* | **The same package's own resolution** |
| `12_AAS_PLUS_CHALLENGE_VERDICT.md` `CF-V-01` basis | *"`HF-CTX-11` references the control `CF-I-03` requires, **and that control does not exist**"* | Unbounded |

> **`C4-03-F-02`. The R2 package publishes a fact and its negation in two of its own files** — §5.3
> says the control *does not exist*, §10 says it is *specified and not built* — and a reader can pick
> either. **CORR3 picked the unbounded one and widened it further**, from *"not stated by any of the
> 50"* to *"no published invariant states it."* This is the programme's recorded **narrow-negatives-
> survive** defect: a bounded negative was re-published without its bound and became false.

### 1.2 What actually does not exist — stated exactly

| Layer | Exists? | Evidence |
|---|---|---|
| The **invariant** stating the required property | **YES** — `CF-I-03`, status `SPECIFIED` | §1 above |
| A **control specification** at the granularity a test can be written from | **NO** | No trigger, input set, decision rule, deny condition, exception path, evidence artefact, audit event, severity or test class is stated anywhere. **This file supplies it** |
| A **built** control | **NO** | `0 of 60` proof requirements executable, `0 of 52` negative access tests, *"because no implementation exists"* |
| A **control run** for `HF-CTX-11` to reference | **NO** | Follows from the row above |

> **The remediation this changes.** *"Does not exist"* invites **invention** — a new control, authored
> from nothing, owned by nobody, with no ruling lineage. **`Specified, not built` requires
> elaboration** — of an invariant that already carries `MTI-D-02`'s lineage, `CD-28`'s delta trace and
> an owner. **Phase SA may elaborate a specification; that is the phase's own authority.** The
> difference is not presentational: it is the difference between an act inside authority and an act
> the phase would have had to ask for.

### 1.3 `CF-V-01` is not breached by this file, and is not discharged by it

`CF-V-01`, verbatim: *"VETO on recording `HF-CTX-11`, the authorization attestation, or the authority
half of handoff element 10, **as supplied, available, satisfied or suppliable**. Their status is
`specified, not built, not verified`, and no other wording may be substituted."*

The veto is on **availability wording**, and the package that issued it says so in terms: *"Both vetoes
are on wording and reliance. Neither is a veto on design content, and neither prevents Boss from
commissioning any lane."*

**This file states no availability.** `HF-CTX-11` remains `specified, not built, not verified`, in those
words and no others. **`CF-V-01` remains in force and is not discharged.** Vetoes in force after this
package: **6**. Discharged: **0**.

---

## 2. Control objective

`CF-I-03` proves, continuously and by inspection rather than by assertion, that **every recorded act was
performed under an authority that was actually in force, on every axis the acted-on object carries, and
never across a company boundary.**

It is the **authorization** analogue of `MTI-19`, and the two are disjoint by construction:

| | `MTI-19` | `CF-I-03` |
|---|---|---|
| Asserts | the record's **context** is right | the **act** that produced it was **permitted** |
| Over | `CTX` = (tenant, company, warehouse?, location?) | `AUTH` = (tenant, company, warehouse, operation type) |
| Attested by | `HF-CTX-06` | **`HF-CTX-11`** |
| Enforcement point | `EP-R` Resolve | **`EP-P` Permission evaluation** |
| Failure mode | act **fails**, recorded as a failure | act is **refused**, recorded as a refusal |

`03_MTI_INVARIANT_SET_R2_CONFORMED.md` §14 — *Internal Consistency* — states the non-overlap as a
determination: *"Neither. They
assert disjoint properties over the same acts … Context conformance and authorization conformance are a
third and fourth independent property, and none implies another."* **`CF-I-03` therefore cannot be
satisfied by any `MTI-19` result, and `MTI-19`'s scope note forbids reading one as the other.**

### 2.1 What the control must honour — the eight properties the master prompt names

| # | Property | How `CF-I-03` reaches it | Governing |
|---:|---|---|---|
| 1 | **Tenant boundary** | axis `T` present and inside the act's `CTX` spine | `MTI-01`, `MTI-02`, `CF-I-01` |
| 2 | **Company boundary** | axis `C` present where the object is company-scoped; **no grant spans two companies** | `MTI-04`, `BD-ACC-02`, `CF-I-01` |
| 3 | **Actor / service authority** | the recorded principal resolves to a grant; a **rule** is an actor only with its identity **and version** | `HF-CTX-08`; `XMC-C-C3` |
| 4 | **Role / permission policy** | the grant evaluated is the grant in force **at the time of the act**, not at check time | `CF-I-03` clause 1 |
| 5 | **Privileged access policy** | a `MTI-18` named grant is a first-class `AUTH` source with grantor, grantee, reason, scope, **expiry** | `MTI-18`; `SA_CORR4_01` |
| 6 | **Handoff context integrity** | every emitted fact carries `HF-CTX-08` **and** `HF-CTX-11` | `MTI-43`, `MTI-45` |
| 7 | **No implicit cross-tenant execution** | multi-tenant **membership** never becomes multi-tenant **execution context** | Boss decision `00`/`01`; `SA10` §8.2 |
| 8 | **Auditable denial / failure** | a refusal emits a refusal event; it *"never degrades to a filter, an empty result or a silent no-op"* | `EP-P`; `N-01`, `N-03` |

---

## 3. `CF-I-03` — full control specification

Everything below is **new specification text**. It elaborates the invariant; it does not amend it. Where
this file and the invariant disagree, **the invariant governs** and the disagreement is a defect in this
file.

### 3.1 Identity

| Field | Value |
|---|---|
| **Control ID** | **`CF-I-03`** |
| Control name | Authorization Conformance Control |
| Class | Continuous detective control (`CONTROL` layer) — **not** a preventive gate. The preventive twin is `EP-P` |
| Owner | **SaaS Foundation** (control mechanics, grant store, run retention) **+ Inventory** (act population, object axis map) |
| Topology scope | **`SHARED SaaS POOL` only.** `CF-I-08` binds: nothing here may be asserted to hold, transfer or fail inside a Private Company operating model |
| Status | **`SPECIFIED — NOT BUILT — NOT VERIFIED`.** No other wording |

### 3.2 Trigger

| # | Trigger | Type |
|---:|---|---|
| `T1` | **Continuous / scheduled sweep** over acts recorded since the last completed run, per context | primary |
| `T2` | **On emission** — an act producing a handoff fact is asserted before `HF-CTX-11` may name a run | synchronous |
| `T3` | **On grant change** — a grant revoked, narrowed or expired triggers a sweep over acts recorded under it | reactive |
| `T4` | **On deferred release** — a queued run releasing revalidates under `CF-I-02`; the revalidation is a `CF-I-03` input | reactive |
| `T5` | **On demand** — an auditor or Boss may cause a run over a named context and period | governance |

**`T1` is not sufficient alone.** A control that only sweeps periodically cannot supply `T2`'s
synchronous obligation, and `MTI-43` requires the attestation to name a run that **precedes the act it
attests**. `SA_CORR3_07` states the corresponding negative test: *"referenced run predating the act →
reject."* **The run must be current for the act, which is why `T2` exists.**

### 3.3 Inputs

| # | Input | Source | Absent ⇒ |
|---:|---|---|---|
| `I1` | The **recorded act**: principal, timestamp, object, operation type, and the `AUTH` tuple recorded with it | act/audit record | `D6` |
| `I2` | The **grant store**, historised — every grant with its grantor, grantee, four axes, reason, effective-from and effective-to | authoritative policy source, §3.4 | run **cannot execute**; §3.11 |
| `I3` | The **object axis map** — for the acted-on object type, which of the four axes that object carries | `04_CTX_AUTH…` §6, 41 functions × 4 axes | `D5` |
| `I4` | The **privileged-grant register** — `MTI-18` named grants | `SA_CORR4_01` | `D4` |
| `I5` | The **scope class** of the object — `PLATFORM` / `TENANT` / `COMPANY` | `SCOPE-AWARE EVERYWHERE` | `D5` |
| `I6` | The **deferral record** where the act was released from a queue — scheduling authority, release authority, both timestamps | `CF-I-02`, `MTI-30` | `D7` |

### 3.4 Authoritative policy source

**The historised grant store is the only authoritative source, and the control reads the grant *in force
at the act's timestamp*, never the grant in force at check time.**

Stated because the failure it prevents is silent and total: a control reading current grants marks every
act by a since-revoked authority as conformant, and marks every act by a since-granted authority as a
breach. **Both errors point away from the truth, and neither is visible in the control's own output.**

`MTI-50` supplies the retention obligation that makes the historised store possible. **`CF-I-03` is
unbuildable without it, and this is a hard dependency, not a preference.**

### 3.5 Expected decision

For each act in scope the control returns exactly one of:

| Result | Meaning |
|---|---|
| **`CONFORMANT`** | every applicable axis present, inside a grant in force at the act's timestamp, no grant spanning two companies |
| **`BREACH`** | one or more deny conditions `D1`–`D8` met. **Raises. Does not repair** |
| **`NOT ASSESSABLE`** | an input required to decide is absent. **Never `CONFORMANT`.** §3.11 |

> **`CF-I-03` never repairs, never back-fills, never annotates the act, and never suppresses a
> duplicate breach.** Copied from `MTI-19`'s *"Breach raises; it does not silently repair"* and stated
> again because a control that repairs destroys the evidence that it was needed.

### 3.6 Deny conditions

| ID | Condition | Severity |
|---|---|---|
| `D1` | The recorded `AUTH` is **not inside any grant in force at the act's timestamp** | **CRITICAL** |
| `D2` | A single grant **spans more than one company** | **CRITICAL** |
| `D3` | The act's `AUTH` crosses a **tenant** boundary, in any form, including via a membership in two tenants | **CRITICAL — tolerance zero** |
| `D4` | The act relies on a privileged elevation with **no `MTI-18` named grant**, or one **expired at the act's timestamp**, or one lacking grantor / grantee / reason / scope / expiry | **CRITICAL** |
| `D5` | An axis is **absent** where `I3`/`I5` say the object carries it | **HIGH** |
| `D6` | The act carries **no `AUTH` record at all** | **CRITICAL** |
| `D7` | A deferred act's authority was **valid at scheduling and not revalidated at release** | **HIGH** |
| `D8` | An axis value was **defaulted, inferred, or inherited from a session fallback** rather than resolved | **HIGH** |

`D3` is separated from `D1` deliberately. **A cross-tenant act is not a stronger case of a missing
grant; it is a different failure, because Boss decision `00`/`01` makes tenant the security boundary
and forbids any lower-level relationship from weakening it.** A control that folds `D3` into `D1`
reports the programme's most serious failure under its most common label.

### 3.7 Exception path

**There is exactly one, and it is not an exception to the property.**

A cross-company effect is conformant **only** where it is an enumerated `MTI-22` Cross-Context
Relationship register entry, and the act carries `HF-CTX-07` naming that entry and its correlation
identity. **Anything else is `D2`.**

- **There is no cross-tenant exception path. None is specified, and this file does not create one.**
- The register today holds **4 entries — 1 incomplete, 3 conditional, 0 unconditionally settled**, so
  the exception path's **content is not yet closed.** The control's *shape* does not depend on that;
  its *test set* does — §3.13.

### 3.8 Privileged path handling

A `MTI-18` grant is **an `AUTH` source like any other and is evaluated identically** — it is not an
exemption and does not suppress `D1`. It additionally requires `D4`'s six fields, and its **expiry is
evaluated against the act's timestamp**.

**A privileged path whose grant is absent from `I4` is `D4`, not `CONFORMANT` and not `NOT
ASSESSABLE`.** Stated because the enumeration in `SA_CORR4_01` is bounded, and a control that treats
"unknown path" as "no finding" **converts the enumeration's own residual into a silent pass** — the
programme's recorded *control-that-cannot-detect-its-own-failure* class.

### 3.9 Required evidence, and the audit event

Each **run** retains: run identity; context scope; period covered; population size; per-result counts;
every `BREACH` with its act reference and deny condition; every `NOT ASSESSABLE` with the absent input;
and the **grant-store version** read.

Each **breach** emits an audit event carrying: act reference; principal; recorded `AUTH`; the grant
evaluated (or its absence); deny condition; severity; run identity.

**Retention and inspectability are `MTI-50`.** `HF-CTX-11` names *the run*, with timestamp and result —
**never a boolean.** The invariant set's own reason, carried verbatim: *"A boolean is an assertion by the
emitter about itself; a control-run reference is inspectable by the consumer and by an auditor."*

### 3.10 Failure severity

| Class | Severity | Effect |
|---|---|---|
| `D3` cross-tenant | **CRITICAL — TOLERANCE ZERO** | breach → the emitting fact is not emitted; a fact already emitted is flagged and its consumers notified |
| `D1`, `D2`, `D4`, `D6` | **CRITICAL** | breach → consumer **must reject** the fact (`MTI-45`) |
| `D5`, `D7`, `D8` | **HIGH** | breach → fact rejected; a per-context exception record is raised |
| Control **cannot run** | **CRITICAL** | **fail closed.** §3.11 |

### 3.11 Fail-closed, and the `NOT ASSESSABLE` rule

**If `CF-I-03` cannot run, or an act cannot be assessed, the result is never `CONFORMANT`.**

`MTI-20` states the general form — *"Where context cannot be resolved, the act fails and is recorded as a
failure. Context is never defaulted, never inferred"* — and this clause applies it to authorization.

> **The single most likely way this control fails in practice is by returning a clean zero because its
> inputs were not readable.** A zero-breach run over a population of zero, or over acts whose grant
> history was unavailable, is **indistinguishable in its headline from a zero-breach run over a full
> population** — and the programme has recorded that exact failure more than once. **Therefore every
> run publishes its population size and its `NOT ASSESSABLE` count beside its breach count, and a run
> that publishes a breach count alone is not a valid run.**

### 3.12 Test preconditions

| # | Precondition | Present today? |
|---:|---|---|
| `P1` | An implementation exists in which acts are recorded with an `AUTH` tuple | **NO** |
| `P2` | A **historised** grant store with effective-from / effective-to | **NO** — `MTI-50` unbuilt |
| `P3` | The object axis map instantiated for the implemented object set | **Specified** (41 functions), **not instantiated** |
| `P4` | The `MTI-18` privileged-grant register **exists and is populated** | **NO** — `SA_CORR4_01` |
| `P5` | The `MTI-22` register content closed | **NO** — 1 incomplete, 3 conditional |
| `P6` | The **implemented** operation-type set and its platform classes | **NO** — `CF-D-02` unruled. `N-06` binds: the test set derives from the **implemented** enumeration, **never from `MTI-D-02` §5's illustration** |

**`P1`–`P6` are why `C4-03` closes as a specification and cannot close as a proof.** They are the phase
boundary, not a defect of this file.

### 3.13 Test classes — the Pre-Test Matrix's obligation

**Positive**

| ID | Class |
|---|---|
| `CF3-P-01` | Act inside a grant on all four axes → `CONFORMANT` |
| `CF3-P-02` | Act on a `PLATFORM`-scoped object with neither tenant nor company → `CONFORMANT`. **`SCOPE-AWARE EVERYWHERE` — the control must not over-constrain** |
| `CF3-P-03` | Act on a `TENANT`-scoped object with tenant and no company → `CONFORMANT` |
| `CF3-P-04` | Cross-company effect **inside** an `MTI-22` entry with `HF-CTX-07` present → `CONFORMANT` |
| `CF3-P-05` | Act under an **unexpired** `MTI-18` grant with all six fields → `CONFORMANT`, and the grant appears in the run record |

**Negative — one per deny condition, each tested in isolation**

`CF3-N-01`…`CF3-N-08` map one-to-one onto `D1`…`D8`.
**`N-05` binds: each axis is tested independently.** A test removing two grants at once cannot show
which axis refused, *"and a system enforcing only company would pass it."*

**Boundary**

| ID | Class |
|---|---|
| `CF3-B-01` | Grant expires **between** act and check → act is `CONFORMANT` (grant in force **at the act**) |
| `CF3-B-02` | Grant issued **after** the act → **`D1`**. The mirror of `CF3-B-01`, and the one a current-grants implementation passes wrongly |
| `CF3-B-03` | Referenced run **predates** the act → **reject.** `MTI-43`'s stated third negative form |
| `CF3-B-04` | Attestation **absent** → reject. `MTI-43`'s first negative form |
| `CF3-B-05` | Referenced run **itself in breach** → reject. `MTI-43`'s second negative form |
| `CF3-B-06` | Act at the exact effective-from / effective-to instant — **inclusivity stated, not left to the implementation** |
| `CF3-B-07` | Actor holding grants in **two tenants** acts on one → `CONFORMANT` for that one, and **`D3` if the act touches the other.** The membership-vs-execution boundary, tested directly |
| `CF3-B-08` | Object whose scope class is **`COMPANY`** but whose axis map omits company → **`D5`**, not `CONFORMANT` |

**Instrument controls the Pre-Test Matrix must run on the control itself**

| ID | Class |
|---|---|
| `CF3-C-01` | **Synthetic injection** — inject one known-breaching act and confirm the run moves `0 → 1`. Proves the predicate **can fire** |
| `CF3-C-02` | **Discriminating population** — a never-transacted context must return a **structurally different** result from a clean one, not the same zero |
| `CF3-C-03` | **Coverage assertion** — population requested vs assessed vs `NOT ASSESSABLE`; a shortfall fails the run |
| `CF3-C-04` | **Negative control** — a nonsense principal returns 0 |

`CF3-C-01`…`CF3-C-04` exist because this control's characteristic failure is a **false clean result**,
and no positive test detects that.

### 3.14 The five expectations the master prompt names

| Expectation | `CF-I-03` result |
|---|---|
| **Retry / replay** | The **original** act's timestamp and grant govern. A replay never re-resolves authority — `MTI-41`'s "replay never re-resolves `CTX` from current configuration", applied to `AUTH`. A replay asserting present authority for a past act is **`D1`** |
| **Tenant mismatch** | **`D3` — CRITICAL, tolerance zero.** Fact not emitted; if already emitted, flagged and consumers notified |
| **Company mismatch** | **`D2`** unless an `MTI-22` entry covers it with `HF-CTX-07` present |
| **Missing context** | **`D5`** where an axis is absent; **`D6`** where no `AUTH` is recorded. **Never `CONFORMANT`, never `NOT ASSESSABLE`** — the input is present and shows the absence |
| **Break-glass** | Evaluated as a normal grant **plus** `D4`'s six fields **plus** expiry at the act's timestamp. **No suppression of any other deny condition** |
| **Service account** | Identical evaluation. A non-interactive principal is a principal. **`XMC-C-C3` binds: *"the system" is not an asserter*** — a rule is an actor only with identity **and version**, so a service principal without a version is **`D6`** |

---

## 4. `MTI-43` linkage — proved, not asserted

`MTI-43`, verbatim: *"Every emitted handoff fact carries the resolved `CTX` **and an attestation** naming
which invariants guaranteed it and which control last asserted them. Element 10 is satisfied by the
tuple **plus** the attestation, never by the tuple alone."*

The two attestations, and their state:

| Half | Value field | Attestation field | Control behind it | State |
|---|---|---|---|---|
| **Context** | `HF-CTX-01`…`-05` | `HF-CTX-06` | `MTI-19` | specified, not built |
| **Authority** | `HF-CTX-08`, `HF-CTX-10` | **`HF-CTX-11`** | **`CF-I-03`** | **specified** by §3 of this file, **not built** |

| Question | Before this file | After |
|---|---|---|
| Does `HF-CTX-11` name a control that is **specified**? | Recorded as **no** by CORR3; **actually yes** at invariant level | **Yes**, and now at control level |
| Is that specification **testable** — trigger, inputs, decisions, deny conditions, evidence, test classes? | **No** | **Yes** — §3.2–§3.13, `5` positive · `8` negative · `8` boundary · `4` instrument classes |
| Is the control **built**? | No | **No** |
| Can `MTI-43`'s three negative forms now be **constructed**? | **No** — CORR3, correctly, given what it had | **Yes** — `CF3-B-03`, `CF3-B-04`, `CF3-B-05` |
| Can they be **executed**? | No | **No** — `P1`–`P6` |
| Does element 10 move? | — | **No.** `AAS-V-01` and `CF-V-01` both stand |

> # `MTI-43 CONTROL REFERENCE CLOSED`
>
> **Closed in the exact sense the classification offers and no wider: `HF-CTX-11` now references a
> control specification that exists, is testable, is owned, and carries ruling lineage.** The
> attestation is **no longer a reference to nothing.**
>
> **It is a reference to something not yet built.** `MTI-43` stays `HOLD — PROOF MISSING`, element 10
> stays `specified, not built, not verified`, `CF-V-01` stays in force, and **nothing in this file may
> be read as making `HF-CTX-11` supplied, available, satisfied or suppliable.**

**What this does change, materially:** CORR3 recorded `MTI-43`'s first negative test as one that
*"cannot be constructed"* — a **specification** gap, closable at Phase SA. It is now constructed, and
the residue is a **runtime** gap, closable only by a build and an executed test. **The item moves from
this phase's ledger to the next one's**, which is what a pre-gate closure round is for.

---

## 5. What this file does not do

| | |
|---|---|
| Discharge `CF-V-01` or `AAS-V-01` | **No.** 6 vetoes in force, 0 discharged |
| Move element 10 | **No** |
| Prove anything | **No.** `0 proven` is unchanged everywhere |
| Amend `CF-I-03` the invariant | **No.** Elaboration only; the invariant governs |
| Close `CF-F-05` | **The specification half only.** `CF-F-05` records that authorization has no conformance control; it now has a specified one and no built one |
| Rule `CF-D-02` (operation-class enumeration) | **No — Boss-reserved.** `P6` and `N-06` carry the consequence |
| Decide `RC-D-01` (`location` as an authorization axis) | **No — unruled.** The control is specified on the **three ruled** axes plus operation type, exactly as `CF-I-01` states |
| Author anything for the **Private Company** topology | **No.** `CF-I-08` |

---

## 6. Residual, stated exactly

1. **`P2` is the hard one.** Without a historised grant store, `CF-I-03` cannot be built at all — not
   partially. **`MTI-50` is therefore upstream of `CF-I-03`, and no Pre-Test scheduling may put them
   in the other order.** Stated as a dependency observation; commissioning is not my act.
2. **The exception path's content is open** — the `MTI-22` register has 1 incomplete and 3 conditional
   entries. `CF3-P-04` is specified and **its test data does not exist**.
3. **`P6` is Boss-gated.** `CF-D-02` is stated and never chosen; option (c) is to withdraw `CF-I-05`
   entirely. **If (c) were ruled, `CF-I-03`'s operation-type axis loses its platform binding** — the
   control survives on three axes and `D5` narrows. Recorded, not decided.
4. **This specification has been reviewed by nobody outside this session at the time of writing.**
   It is re-challenged at `SA_CORR4_08`, by parties drawn from the same corpus — which `ND-12` records
   internal challenge cannot escape.
5. **What a challenger should attack first:** §3.4's claim that reading the *grant in force at the act's
   timestamp* is the correct semantic. It is the load-bearing design decision here, it is **mine**, and
   an argument exists against it — that an act by an authority since revoked for cause should not be
   certified conformant. **My answer is that revocation for cause is a separate finding over the same
   act and must not be produced by silently re-timing the conformance question** — but that is a
   position, not a proof, and Boss or an independent reviewer may take the other one.

---

## 7. Checkpoint

> ## `CP-SA-C4-30 — CF-I-03 SPECIFIED AND LINKED`
> **`CF-I-03` control specification published** — 5 triggers · 6 inputs · 3 results · 8 deny
> conditions · 1 exception path · 25 test classes.
> **`MTI-43 CONTROL REFERENCE CLOSED`** at specification level; runtime proof deferred.
> **2 findings** — `C4-03-F-01`, `C4-03-F-02`. **0 vetoes discharged. 0 invariants proven.**

**Next autonomous action:** `CP-SA-C4-40`, compliance retraction propagation.

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
