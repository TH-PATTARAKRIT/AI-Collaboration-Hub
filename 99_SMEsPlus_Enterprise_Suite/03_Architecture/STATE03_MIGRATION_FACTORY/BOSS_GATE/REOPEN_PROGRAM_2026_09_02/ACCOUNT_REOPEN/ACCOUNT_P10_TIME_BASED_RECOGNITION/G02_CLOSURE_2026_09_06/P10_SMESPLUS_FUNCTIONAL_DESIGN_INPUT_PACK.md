# P10 — SMEsPLUS FUNCTIONAL DESIGN INPUT PACK

Closure round `[SMEPLUS-26-09-06-G02-P10-TBR-BOUNDED-DEEP-CLOSURE-DESIGN-INPUT-001]` · Layer 1 · **clean-room**

> **This pack is DESIGN INPUT. It is not architecture, not a schema, not an API, not a UI specification, and nothing in it is frozen or authorised for implementation.** `AASP-VETO-01` revision 3 remains in force and blocks implementation start.

---

## 0. How to Read This Pack

Every entry carries exactly one label:

| Label | Meaning |
|---|---|
| **FACT-SUPPORTED FUNCTIONAL REQUIREMENT** | Derived from verified evidence — usually from an **observed absence with a consequence**. Not a preference |
| **BOSS-APPROVED POLICY INPUT** | Already ruled by the Boss; preserved, not re-decided |
| **DESIGN CANDIDATE** | P10's recommendation. Requires a decision it does not make |
| **UNRESOLVED — DECISION/EVIDENCE REQUIRED** | Named dependency; owner stated |

**Two standing qualifications apply to every source-derived statement in this pack:**

1. **The deferral mechanism has never executed in any deployed database P10 can read** — installed, configured in 43 of 44 companies, **zero entries**. Every behavioural statement is `INSTALLED AND CONFIGURED`, never `EXERCISED`, and therefore never `ECONOMICALLY VALIDATED`.
2. **The estate population is a floor**, and the reference generation P10 read is not demonstrably the generation the estate runs. See `P10_EVIDENCE_POPULATION_BOUNDARY.md`.

**Boss policy boundaries preserved, not re-decided:** invoice policy is separate from cost-recognition policy · time-based recognition must not silently redefine physical inventory or cost events · scope is determined per object, never blanket tenant+company · correction must preserve audit lineage, and destructive reference behaviour must not be normalised into a SMEsPlus requirement.

---

## F-01 — RECOGNITION POLICY

| Field | Content |
|---|---|
| **Business purpose** | Declares *how* an amount is spread over time: the convention, the grid, the residue destination, and when recognition is triggered |
| **Trigger / event** | Configured by a user; **read at schedule creation**, not at posting |
| **Actors** | Accounting configuration role; not an operator function |
| **Preconditions** | A company exists; a fiscal calendar exists |
| **Lifecycle / states** | draft → active → superseded. **A policy must be versioned** |
| **Inputs / outputs** | In: convention, grid basis, residue destination, trigger. Out: the parameters a schedule is built from |
| **Core data semantics** | Convention **definition** is reference data; the **choice** is a company binding value |
| **Recognition period semantics** | Policy determines how a window is cut, not which period an amount lands in |
| **Posting date semantics** | None. **A policy must not influence a posting date** |
| **Accounting effect** | None directly |
| **Currency / amount** | None directly; it decides rounding currency, which must be the **base's** currency, not the executor's |
| **Scope** | Definition **PLATFORM** · tenant standard **TENANT** · binding value **COMPANY** |
| **Controls** | The binding value **must be read from the company that owns the financial effect**. Where that company cannot be proven, **DENY** |
| **Idempotence** | n/a |
| **Correction** | A policy change must **never** silently re-derive existing recognition. It creates a new version and a correction event |
| **Period close** | n/a |
| **Audit** | Every recognition event must record **which policy version produced it** |
| **Cross-process** | Fiscal calendar from `P08` |
| **Evidence** | Reference reads the convention from the **active** company while reading accounts and journal from the document's company — a verified scope defect, systematic via the automatic posting routine |
| **Open design choices** | May a tenant **bind** rather than default a convention? |
| **UI implication** | A configuration screen with a version history. Not an operator screen |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for scope-correct reading, versioning and policy-recording. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for tenant binding (Boss).

---

## F-02 — RECOGNITION SCHEDULE

| Field | Content |
|---|---|
| **Business purpose** | The durable plan: *this base, over this window, by this policy, produces these periods* |
| **Trigger / event** | Creation of a recognition obligation — **which is not necessarily an invoice.** See F-05 |
| **Actors** | System-generated; operator may amend under control |
| **Preconditions** | A recognition base, a window, a policy version, an owning company |
| **Lifecycle / states** | draft → active → amended (new version) → completed → cancelled. **The reference has no such object at all** |
| **Inputs / outputs** | In: base, window, policy. Out: a set of recognition events |
| **Core data semantics** | Must be **durable and versioned**. The reference computes the segment set inside one call and **discards it** |
| **Recognition period semantics** | The schedule owns the period set. It must survive the entries it produces |
| **Posting date semantics** | **None.** A schedule has no posting date |
| **Accounting effect** | None. A schedule is a plan |
| **Currency / amount** | Must carry the base's **currency, amount, measurement rate and measurement date** |
| **Scope** | **COMPANY** — it produces a company financial effect |
| **Controls** | Window start ≤ end; base non-zero; policy version pinned at creation |
| **Idempotence** | **A schedule must be uniquely identified so it cannot be generated twice for one obligation.** The reference has no such identity, and its duplicate control is a date-and-state proxy that has been defeated |
| **Correction** | Amendment creates a **new version**; prior versions preserved; produces STANDS / RE-DERIVED / CATCH-UP DELTA |
| **Period close** | A schedule is unaffected by close. Only its postings are |
| **Audit** | Must reference its **origin line**, not only its origin document |
| **Cross-process** | Origin from `P01`/`P02`; posting from `P08` |
| **Evidence** | No schedule object exists in the reference; the grid is calendar-monthly in **every** configuration; there is **no amendment path** other than tearing down the source document |
| **Open design choices** | Must a **daily** grid be supported, or is monthly sufficient? The reference cannot express daily |
| **UI implication** | **A schedule screen is required and does not exist in the reference.** Today the entire surface is two optional, hidden-by-default columns |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for durability, versioning, identity and line-level origin. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for the daily grid (Boss).

---

## F-03 — RECOGNITION EVENT

| Field | Content |
|---|---|
| **Business purpose** | One period's share of one obligation: *this amount belongs to this period* |
| **Trigger / event** | The passage of time across a period boundary — **the only P10 business event with no producer**; nothing in the business causes it and no document records it |
| **Actors** | System |
| **Preconditions** | An active schedule; a period in the grid |
| **Lifecycle / states** | planned → due → **refused** → recognised → superseded → reversed. **CORRECTED, `G02-R-18`:** `refused` was absent while F-09's own precondition requires it, so the closure control could not be evaluated against this model. **States still unnamed and required: `suspended` (the deployed schema carries a paused-days counter, so the concept exists for assets and not here), `provisional` (a schedule on an estimated base, which `X-05` presupposes), `empty` (a window inside the source document's own month generates no entries at all), and `partially recognised` — see `X-09`.** No transition set is stated for any lifecycle in this pack: seven state lists, zero edges |
| **Inputs / outputs** | In: schedule, period. Out: a posting instruction |
| **Core data semantics** | **Must have an identity independent of any journal entry.** This is P10's root-cause finding |
| **Recognition period semantics** | **The event owns the period.** It must carry period **start and end**, not only the end |
| **Posting date semantics** | **None of the event's business.** The event says *which period*; the posting act says *which date* |
| **Accounting effect** | None until posted |
| **Currency / amount** | Amount in the base's currency, with the measurement rate and date inherited from the schedule |
| **Scope** | **COMPANY** |
| **Controls** | Amounts across a schedule's events must sum to the base; residue destination is a declared policy, never a default |
| **Idempotence** | **One obligation + one period + one policy version = one event.** This is the identity the reference lacks and the only sound basis for duplicate prevention |
| **Correction** | An event is superseded, never edited. The prior version is preserved |
| **Period close** | An event's period **must not change** because its posting was constrained |
| **Audit** | Event → schedule → origin line → policy version, all resolvable in one hop each |
| **Cross-process** | The **accounting-event object belongs to `D-5`**; P10 specialises it |
| **Evidence** | Anchoring in the reference is graduated: line-level for loans, object+period for depreciation, move-set for both deferral paths, **none for accruals**. What collapses for deferrals is the **period**, not the identity |
| **Open design choices** | Whether SMEsPlus introduces a layer-3 accounting-event object — **`D-5`, Boss** |
| **UI implication** | Visible as a schedule line with its period, status and resulting posting |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for identity, period ownership and the idempotence key. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for the event object (`D-5`), with **`AASP-COND-01`** attached as P10's acceptance condition.

---

## F-04 — RECOGNITION LINE

| Field | Content |
|---|---|
| **Business purpose** | The accounting detail of one recognition event: which accounts, which amounts, which attribution |
| **Trigger / event** | Realisation of a recognition event |
| **Actors** | System |
| **Preconditions** | A due event; derived accounts |
| **Lifecycle / states** | prepared → posted → reversed |
| **Inputs / outputs** | In: event, account derivation. Out: journal items |
| **Core data semantics** | Must carry account, amount, **currency and foreign amount**, attribution and a reference to its event |
| **Recognition period semantics** | Inherited from the event, **not** from its own date |
| **Posting date semantics** | Assigned by the posting act, and **may differ from the period** |
| **Accounting effect** | The reclassification itself |
| **Currency / amount** | **Must carry the currency dimension.** The reference's deferral lines carry **none** — no currency, no foreign amount — so a foreign contract is frozen at the invoice-date rate for its whole window |
| **Scope** | **COMPANY** |
| **Controls** | Balanced by construction; **and a foreign-amount integrity check must exist** — the reference has none, which is why an accrual counterpart can post with a foreign currency and a zero foreign amount |
| **Idempotence** | Inherited from the event |
| **Correction** | Reversed, never edited |
| **Period close** | Subject to lock; the divergence must be recorded |
| **Audit** | Line → event → schedule → origin line |
| **Cross-process** | `P08` for posting, currency model and integrity checks; `P09` for attribution |
| **Evidence** | **Attribution written onto both legs with opposite signs nets to zero and the netting survives period bounding** — so a period-scoped management report shows zero movement from the entire mechanism. Four independent mechanisms implement this shape and fail three different ways |
| **Open design choices** | Should a recognition line carry attribution at all, or should attribution be **derived from the origin**? P10's position: **derived** |
| **UI implication** | Read-only detail beneath the event |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for the currency dimension, the foreign-amount check and single-leg attribution. **`DESIGN CANDIDATE`** for deriving attribution from origin.

---

## F-05 — ORIGIN FACT REFERENCE

| Field | Content |
|---|---|
| **Business purpose** | The immutable link from recognition back to the business fact that caused it |
| **Trigger / event** | Schedule creation |
| **Actors** | System |
| **Preconditions** | An origin fact exists and is identifiable **at line level** |
| **Lifecycle / states** | immutable once set |
| **Inputs / outputs** | In: origin document, origin line, origin event type. Out: a durable reference |
| **Core data semantics** | **The origin is not necessarily an invoice.** It may be a delivery, an obligation, or a contractual instalment |
| **Recognition period semantics** | The origin supplies the **window**, which is a **TENANT** fact — one contract billed by two companies of one tenant has **one** window |
| **Posting date semantics** | None |
| **Accounting effect** | None |
| **Currency / amount** | Supplies the base, **and the measurement rate and date** |
| **Scope** | Window **TENANT** · base **COMPANY** |
| **Controls** | An origin reference **must not be nullable and must not be silently orphaned**. A reference teardown path exists that orphans posted entries with their back-reference nulled |
| **Idempotence** | The origin reference is half the idempotence key |
| **Correction** | Immutable. A corrected origin creates a **new** schedule referencing both |
| **Period close** | n/a |
| **Audit** | This is the root of the lineage chain |
| **Cross-process** | `P02` for sold obligations, `P01` for purchased |
| **Evidence** | Deferral entries reference the **source move**, never the source line. The accrual references **nothing** — the code that would write the link iterates a collection that is never populated |
| **Open design choices** | **Is the obligation position P10-owned or P02-owned?** P10's position: the **measurement** is P02's, the **recognition consequence** is P10's |
| **UI implication** | A navigable link in both directions |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for line-level, non-nullable, bidirectional origin reference. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for obligation-position ownership (P11).

---

## F-06 — PERIOD GRID / CONVENTION

| Field | Content |
|---|---|
| **Business purpose** | Cuts a window into periods and weights each one |
| **Trigger / event** | Schedule creation |
| **Actors** | System, parameterised by policy |
| **Preconditions** | A fiscal calendar; a convention |
| **Lifecycle / states** | Conventions are reference data with versions |
| **Inputs / outputs** | In: window, calendar, convention. Out: an ordered period set with weights |
| **Core data semantics** | **The grid and the convention are two things.** The reference conflates them: its grid is calendar-monthly unconditionally while its convention only changes weights |
| **Recognition period semantics** | The grid **is** the period semantics |
| **Posting date semantics** | None |
| **Accounting effect** | None |
| **Currency / amount** | Weights are dimensionless; residue is currency-bearing and its destination is a **policy**, not arithmetic |
| **Scope** | Algorithm **PLATFORM** · conventions **PLATFORM** reference data · calendar instance **COMPANY** |
| **Controls** | Weights must sum to unity; residue must land where the policy says, never by default |
| **Idempotence** | Deterministic for a given window, calendar and convention version |
| **Correction** | A convention change is a **policy version change**, never a silent re-derivation |
| **Period close** | The grid must be the **company's fiscal** calendar, not the civil calendar. The reference uses civil, unconditionally |
| **Audit** | The convention version is part of every event's lineage |
| **Cross-process** | Fiscal calendar from `P08` — **and that peer reports the ledger has no period object at all** |
| **Evidence** | **Three day-count engines exist in one reference root**, implementing three different conventions; one is a named standard **with its February exception deleted**, and a complete standards-named library of **eight** conventions already exists in the same root. Two engines differ by **5.5%** on the same February window |
| **Open design choices** | Fiscal or civil grid? Daily grid supported? Both **Boss** |
| **UI implication** | Convention selection on the policy screen; the resulting period set visible on the schedule |

**Label: `DESIGN CANDIDATE`** — and the recommendation changes from **build** to **adopt-and-extend**, since a standards-named library already exists. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for fiscal-versus-civil and daily support.

---

## F-07 — POSTING INSTRUCTION

| Field | Content |
|---|---|
| **Business purpose** | Carries a recognition event into the ledger **without becoming it** |
| **Trigger / event** | An event becoming due, or an operator releasing it |
| **Actors** | System; operator for exception handling |
| **Preconditions** | A due event; an open period **or** an accepted divergence |
| **Lifecycle / states** | pending → posted → **relocated** → refused → reversed |
| **Inputs / outputs** | In: event, accounts. Out: a journal entry, **and a divergence record if the date differs from the period** |
| **Core data semantics** | **The instruction is where period and date are allowed to differ, and where that difference must be recorded** |
| **Recognition period semantics** | Carried from the event, **read-only** |
| **Posting date semantics** | Assigned here; **may be constrained by a lock** |
| **Accounting effect** | The entry |
| **Currency / amount** | From the line |
| **Scope** | **COMPANY**, asserted — **never derived from a journal or from an active session** |
| **Controls** | **The governing control of the whole pack:** where a posting constraint moves the date, the system must **refuse, or record an attributable trace** — and where the mutation path has **no violation to detect**, the trace is **mandatory, not alternative** |
| **Idempotence** | One event → at most one live posting |
| **Correction** | Reversal is typed: **structural** (part of the pattern, e.g. an accrual's own reversal) versus **corrective**. The reference does not distinguish them |
| **Period close** | Behaviour must be declared per path: `REFUSE` / `RELOCATE-AND-RECORD` / `PROCEED`. **Silent relocation is the defect** |
| **Audit** | Divergence between period and date must be **reportable and reconcilable** |
| **Cross-process** | **`P08` owns posting, locks and numbering. P10 does not define close semantics** |
| **Evidence** | Relocation is specified behaviour, recorded by an executed test in which one fiscal year shows nothing and the next shows double. **The landing period is chosen by the journal's sequence numbering format** — a convention whose answer changes with a numbering format is not a convention. **The silence is a choice**: the same routine posts a chatter message six lines above the relocation branch |
| **Open design choices** | **Six options classified, none eliminated.** `BOSS DECISION REQUIRED`, coupled to the peer boundary and to `D-5` |
| **UI implication** | A divergence must be **visible**, not merely stored |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for the period/date separation and the divergence record. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for which of the six options governs.

---

## F-08 — RECOGNITION CORRECTION / REVISION

| Field | Content |
|---|---|
| **Business purpose** | Change a recognition plan or fix a recognised amount **without destroying history** |
| **Trigger / event** | Contract amendment, cancellation, re-measurement, or an error |
| **Actors** | Operator, under authorisation |
| **Preconditions** | An active or completed schedule |
| **Lifecycle / states** | requested → applied → superseded |
| **Inputs / outputs** | In: the change and its reason. Out: a new schedule version, a delta event set, and reversals where required |
| **Core data semantics** | **Three outcomes: STANDS · RE-DERIVED · CATCH-UP DELTA.** Which one applies is **domain-specific**; the *operations* that trigger them are not shared at all |
| **Recognition period semantics** | A catch-up delta lands in the **current** period and **says so** |
| **Posting date semantics** | A corrective reversal **must be reconcilable to what it corrects**, including across periods |
| **Accounting effect** | Reversal plus re-derivation, or a delta |
| **Currency / amount** | Re-measurement must record a new rate and date, never overwrite the old |
| **Scope** | **COMPANY** |
| **Controls** | **Never destructive.** Three reference behaviours are destructive — unlinking entries, orphaning posted entries on teardown, and rebuilding a draft board — and the Boss boundary already forbids normalising them |
| **Idempotence** | A correction is itself an event with an identity |
| **Correction** | Corrections are correctable; versions chain |
| **Period close** | A correction into a closed period follows F-07's rule |
| **Audit** | **Actor, reason and prior version — the reference records none of the three** |
| **Cross-process** | `P08` for reversal mechanics |
| **Evidence** | Four mechanisms, four different correction behaviours. **The most correction-resilient path is the one no deployed company uses.** A corrective reversal can land in a **different period** from the entry it corrects — verified with an executed control. The shared teardown's **cancel branch is unreachable**, so a posted entry is always reversed |
| **Open design choices** | Does a correction require approval? Not evidenced either way |
| **UI implication** | An amendment screen showing what stands, what is re-derived and what the catch-up is — **before** it is applied |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for non-destructiveness, actor/reason/version, and reconcilable reversal. **`DESIGN CANDIDATE`** for the three-primitive algebra, **which carries its own counter-evidence**: in-flight amendment differs by domain lifecycle, not by algebra.

---

## F-09 — RECOGNITION CLOSURE

| Field | Content |
|---|---|
| **Business purpose** | Establishes that a period's recognition is complete and consistent, and that a schedule has finished |
| **Trigger / event** | Period close; schedule completion |
| **Actors** | Accountant |
| **Preconditions** | All events for the period are posted, refused, or explicitly deferred with a trace |
| **Lifecycle / states** | open → complete → closed |
| **Inputs / outputs** | In: the period's events. Out: a closure assertion and an exception list |
| **Core data semantics** | Closure is an **assertion about a period**, not a date being moved. The peer reports that in the reference **closing a period is moving a date** |
| **Recognition period semantics** | Closure binds the **period**, not the posting date |
| **Posting date semantics** | Constrains F-07 |
| **Accounting effect** | None directly |
| **Currency / amount** | n/a |
| **Scope** | **COMPANY** |
| **Controls** | **A period may not close while an event belonging to it is unposted and untraced.** No such control exists in the reference |
| **Idempotence** | Closing twice is a no-op |
| **Correction** | Reopening must state what it re-derives. **The reference re-derives nothing** |
| **Period close** | This function *is* the interaction |
| **Audit** | The exception list is the audit artefact |
| **Cross-process** | **`P08` owns close. P10 supplies the completeness assertion** |
| **Evidence** | Nothing re-derives suppressed or relocated recognition on reopen. **1 of 46 distinct companies in the examined estate has any lock configured**, so close controls are barely used |
| **Open design choices** | Does close **block** or merely **report** incomplete recognition? |
| **UI implication** | A pre-close checklist naming unposted and relocated events |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for the completeness assertion and the reopen statement. **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`** for block-versus-report (Boss/`P08`).

---

## F-10 — RECOGNITION AUDIT / RECONCILIATION

| Field | Content |
|---|---|
| **Business purpose** | Proves that what was recognised matches what should have been, and explains every difference |
| **Trigger / event** | On demand; at close |
| **Actors** | Accountant, auditor |
| **Preconditions** | Schedules, events and postings exist and are linked |
| **Lifecycle / states** | n/a — a reporting function |
| **Inputs / outputs** | In: schedules, events, postings, corrections. Out: a reconciliation with a **named cause for every difference** |
| **Core data semantics** | Must reconcile **three** populations: what the schedule planned, what was recognised, what was posted |
| **Recognition period semantics** | Reported **by period**, from the event's period — not from the entry's date |
| **Posting date semantics** | Reported alongside, with divergences itemised |
| **Accounting effect** | None |
| **Currency / amount** | Must reconcile in **both** the base currency and the company currency |
| **Scope** | **COMPANY** |
| **Controls** | Every difference has a cause: relocated, refused, corrected, cancelled, or **unexplained** — and unexplained must be a visible state |
| **Idempotence** | Re-running yields the same answer for the same inputs |
| **Correction** | n/a |
| **Period close** | Feeds F-09 |
| **Audit** | This function **is** the audit surface |
| **Cross-process** | `P08` for the ledger side; `P09` for the management side |
| **Evidence** | The reference's two reports **recompute the expected spread on every render from two date fields** — they are a model of what *should* have been recognised, not a record of what was. **Where a posting was relocated, the report and the ledger disagree and the report is right about the economics** — and the divergence is invisible from either side alone |
| **Open design choices** | none material |
| **UI implication** | A three-way reconciliation screen. **The reference has two read-only reports and no reconciliation at all** |

**Label: `FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** throughout — every element is derived from an observed absence with a stated consequence.

---

## 11. Cross-Cutting Requirements

| # | Requirement | Label |
|---|---|---|
| `X-01` | A recognition period is **carried** *and* the period/date divergence is **reportable**. Carrying alone is insufficient — depreciation carries its period and is still silently relocated | **FACT-SUPPORTED** |
| `X-02` | `MISSING REQUIRED SCOPE = DENY` on every generation path. The accrual wizard already does this and is the pattern to copy | **FACT-SUPPORTED** |
| `X-03` | Attribution on a posted recognition entry is **immutable or tracked**. It is presently neither | **FACT-SUPPORTED** |
| `X-04` | **One economic fact → one recognition path.** The reference produces two structurally different shapes from one company setting, with different residue destinations, different rounding currencies, different analytic effects, and **total intra-month divergence** | **FACT-SUPPORTED** |
| `X-05` | A performance-triggered recognition path must be **representable**, whatever the default. A model keyed solely on billing cannot represent 1,201 delivered-and-never-invoiced lines | **FACT-SUPPORTED**, from P02's measurement |
| `X-06` | Invoice policy stays separate from cost-recognition policy; recognition must not silently redefine physical inventory or cost events | **BOSS-APPROVED POLICY INPUT** |
| `X-07` | Revenue on **billing** versus **performance** | **UNRESOLVED — Boss reserved.** P02 supplies measurement; P10 supplies the mechanism fact that the reference is billing-triggered and cannot express performance |
| `X-08` | Bill-and-hold scope and trigger | **UNRESOLVED — Boss** |
| `X-09` | **Partial recognition must be representable** — part of a line, an amount re-measured mid-window, partial cancellation or refund, and milestone or percentage-complete recognition | **UNRESOLVED — UNASKED QUESTION, added after adversarial challenge, `G02-R-19`.** The reference has no partial primitive, and **this pack forecloses it**: F-03 and F-04 require amounts to sum to the base and events to be superseded rather than edited. Correct for immutability, and together they make a partially-recognised event unrepresentable. **None of the thirteen closure questions covers it.** P10 does not add closure questions; this is routed to the Boss as an unasked one |
| `X-10` | **The unbilled position** — a contract asset when performance leads billing, and its counterpart when billing leads performance | **UNRESOLVED — MISSING.** This pack inherits a deferred-revenue control account from the reference and has **no unbilled side at all**. `X-05` presupposes it: a performance-triggered path without an unbilled position has nowhere to put the balance. Raised by challenge, `G02-R-19` |
| `X-11` | **A continuing performance-measurement input** — deliveries, milestone confirmations, time entries — feeding a schedule *after* it is created | **UNRESOLVED — MISSING.** F-05 models the origin as a one-shot immutable reference. Performance recognition needs a **stream**, not a reference |
| `X-12` | **Cutover for the already-billed-ahead population.** A ruling on `X-07` needs a transition treatment for lines already recognised on billing | **UNRESOLVED.** Named as the population that makes the question live; never as a migration requirement |
| `X-13` | **Version basis.** Source claims are verified against generation 18.0+e. The field sets they turn on are verified **present and unchanged** in the deployed 19.0+e schema. **Behavioural equivalence across generations is untested** | **STANDING QUALIFICATION on every entry in this pack**, `G02-R-04` |

### 11a. Two Cross-Cutting Entries Corrected After Challenge

**`X-02` restated — `G02-R-13`.** The requirement is *`MISSING REQUIRED SCOPE = DENY` **on every
generation path, including unattended ones***. The accrual is cited only as the **sole observed
instance of a scope refusal**, and that citation is bounded: it is an **operator** path, and the
systematic scope defect lives in the **unattended** posting routine, which searches with no company
filter and posts under the scheduler's own context — the one context where a wizard's ability to
refuse a user's mixed selection proves nothing. The accrual is also the **weakest** mechanism in this
package on every other axis — no anchor, no idempotence, a dead back-link, two currency defects, no
lock pre-check and no tests. **"The pattern to copy" is withdrawn as an unqualified phrase.**

**One engine, two domains — `G02-R-04`, F-04's boundary restated.** The reference shares one code
path, one grid, one convention set and one defect set between revenue and expense. That is an
**implementation** observation and it was being carried as a **functional** one. P10's own boundary
document records that *the event that triggers recognition is **NOT shared***, and a domain is defined
by its triggering event. Five further divergences are none of them a sign flip: **cancellation
economics** (forfeiture or refund liability on the revenue side; a refund receivable on the expense
side — opposite directions, not opposite signs), **control weight**, **actor and screen**, **statutory
presentation**, and **estimate direction**. Restated: **one engine — grid, convention, window
arithmetic, correction outcomes; two domains — trigger, cancellation economics, control weight, actor,
presentation.**

## 12. What This Pack Does Not Contain

No schema, no object names, no field names, no API, no UI layout, no module boundary, no technology choice, and **no implementation authorisation**. Where an object is named — *policy*, *schedule*, *event*, *line* — it is a **functional concept**, and the prompt's instruction not to presuppose final names is observed.

**Ten functions. 39 labelled entries after challenge: 19 `FACT-SUPPORTED FUNCTIONAL REQUIREMENT` · 2 `BOSS-APPROVED POLICY INPUT` · 5 `DESIGN CANDIDATE` · 12 `UNRESOLVED — DECISION/EVIDENCE REQUIRED` · 1 standing qualification.**

> **Readiness, assessed adversarially and accepted.** Four functions are specifiable from this pack
> (`F-01`, `F-04`, `F-06`, `F-10`); four are partly specifiable (`F-02`, `F-03`, `F-05`, `F-07`); two
> are named only — `F-08`, now demonstrably incomplete, and `F-09`, which is written from the
> **absence of use** of close controls rather than from evidence about closure.
>
> **No lifecycle in this pack has a transition set.** Seven state lists, zero edges: not one entry
> states which actor or event drives a transition, which are forbidden, or which are terminal. Two of
> the transitions an SMB actually performs — **cancel mid-window** and **extend mid-window** — are
> undrawn, and the most common correction edge (`recognised → superseded` where the superseding period
> is closed) terminates in `F-07`, whose own governing rule is one of six undecided options.
> **A state list is an enumeration of nouns; a lifecycle is a relation. This pack has the nouns.**
