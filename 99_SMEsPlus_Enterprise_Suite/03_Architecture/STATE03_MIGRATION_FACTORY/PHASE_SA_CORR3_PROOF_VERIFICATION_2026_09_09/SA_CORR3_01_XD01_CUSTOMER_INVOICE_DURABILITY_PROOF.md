# SA_CORR3_01 — XD-01 CUSTOMER-INVOICE DURABILITY: TARGETED VERY DEEP STUDY AND PROOF
## CP-SA-C3-10 (XD-01 limb) — STUDIED AND PROVEN BEFORE ESCALATION

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]`
Branch: `architecture/phase-sa-corr3-proof-verification-2026-09-09-001` @ `5953ce26`
Finding prefix: `XD1-`. Governing law: CORR3 master prompt §4.
Frame: **`CORR3-FRAME`**, adopted by pointer (`SA_CORR3_00` §2), not re-declared.

> **Orchestrator intake note.** Produced by a same-model executor; labelled
> `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not adopted on the executor's word.** Verified before
> acceptance:
> - **`XD1-05` re-executed and CONFIRMED.** Over the active Phase SA package, patterns `BINV-06`,
>   `B04_`, `B05_`, `Downstream Consumption`, `HO-05`, `HO-06` each return **0 files**, while the
>   positive control `BD-ACC-01` returns **28**. The instrument reaches; the material was never cited.
> - **`XD1-04`'s substrate CONFIRMED to exist**: `.../TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/`
>   holds `B00`…`B13`, fourteen files, including `B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md` and
>   `B05_ACCOUNTING_INVARIANT_BASELINE.md`.
> - **One correction applied by the orchestrator (`XD1-C1`).** The executor states the denominator as
>   *"0 of 41 files"*. Re-measured at the unit actually used — markdown files in the two package
>   directories — the denominator is **38** (23 parent + 15 CORR2). The executor appears to have
>   counted non-markdown manifest files it did not then search. **The result is unchanged (still 0,
>   positive control still 28); the denominator is corrected.** This is the programme's own
>   *unit-is-not-population* defect, at low materiality, and it is corrected rather than carried.
> The executor's own residual-uncertainty and attack-first sections are preserved unedited.

---

## 1. Why this register exists, and what it is not allowed to do

CORR2 closed `XD-01` as **`OPEN — BOSS AUTHORITY REQUIRED`** — two decisions plus one delivery, with
a durability precondition attached (`SA_CORR2_01` §3.6; `SA_CORR2_13` §16 Decision 1). The CORR3
master prompt §4 forbids that disposition:

> Do NOT ask Boss to choose a state or design. SMEs Core must study and prove […]

This register therefore does two things in order. First it **re-tests CORR2's decomposition**,
because master prompt §3 is explicit that the prior Boss-decision classification must not be
preserved by default. Second, it executes the §4 study.

It does **not** restart Phase S or L1, does not begin Functional Design or the Pre-Test Matrix, and
does not merge, release or self-approve anything. Checkpoint completion is not Boss approval.

---

## 2. Instrument — declared, executed, validated on a second command shape

| # | Question | PATTERN | PATH SET | UNIT | Shape 1 | Shape 2 | Positive control |
|---|---|---|---|---|---|---|---|
| `I-1` | Corpus reach of the subject | `XD-01` | `CORR3-FRAME` | `U1` blob | **26** | **26** | `BD-ACC-01` → 55 |
| `I-2` | Same, as paths | `XD-01` | `CORR3-FRAME` | `U2` path | **19** | — | — |
| `I-3` | Did Phase SA or CORR2 read the SMEsPlus Accounting Core invariant baseline? | `BINV-06` | the two package directories | file | **0** | **0** | `BD-ACC-01` → **28** |
| `I-4` | …its lifecycle model or interface primitive? | `B04_`, `B05_`, `proposed [Ee]ntry` | same | file | **0 / 0 / 0** | **0** | as `I-3` |
| `I-5` | …the Account programme's own handoff map? | `HO-05`, `HO-06`, `ACCOUNT_PROCESS_HANDOFF_MAP` | same | file | **0 / 0 / 0** | **0** | as `I-3` |
| `I-6` | Corpus reach of the baseline that was not read | `BINV-06` | `CORR3-FRAME` | `U1` blob | **28** | — | — |
| `I-7` | Does a SMEsPlus AR / Receivables design pack exist? | `receivable` (-i); `/AR_` | `CORR3-FRAME` `U2` | path | **0** and **0** | **0** | `DOMAIN_01_ACCOUNTING_CORE` → **292** paths |
| `I-8` | Team B domain-design roots | directory segment | `CORR3-FRAME` | root | **2** | **2** | — |

**Version multiplicity checked before reading.** Every primary artefact cited was resolved to its
distinct content versions first. `B04`, `B05`, `B03`, `B09`, `B11`, `B13`, and the P02 registers each
resolve to **exactly one** blob across all 184 branch heads plus mainline. `06_SALES_CANONICAL_DESIGN`
resolves to **two** and `07_PURCHASE_CANONICAL_DESIGN` to **three**; all were read and the quoted
clauses are present in every version. This control exists because `SA_CORR2_09` §1 records a round
that read the wrong version of the right file.

**Peer identifier families cited but not owned here:** `BE-nn`, `AE-nn`, `EV-P02-nnn`, `P02-F-nn`,
`TZ-nn`, `TC-nn`, `DB-nn`, `H-01…H-07`, `C2-F-nn`, `C2-D-nn`, `JCP-nn`, `ND-nn`, `HO-nn`, `BINV-nn`,
`CAP-nn`, `CO-nn`, `DT-nn`, `BR-nn`, `SAnn-F-nn`, `AR-nn`, `E2E-nn`, `R-nn`, `BD-ACC-nn`, `GB-08`,
`MTI-D-nn`. Only `XD1-` identifiers are created here.

---

## 3. The question, restored from primary text

Verbatim from Group A's own residual matrix
(`.../TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/CORRECTIVE_CORR_010/34_CORR010_ACCOUNTING_HOLD_AND_RESIDUAL_DEPENDENCY_MATRIX.md` §A1):

> 1. What is the Customer Invoice/AR lifecycle state (draft, posted, partially paid, fully paid) that
>    should be treated as equivalent in blocking weight to Purchase's "open vendor bill" gate, if any?
> 2. Does an Accounting-posted (not merely drafted) Customer Invoice against a Sales commitment line
>    constitute a financial exposure Accounting considers should block that commitment's cancellation
>    — symmetric to how a posted vendor bill blocks Purchase's?
> 3. What does "posted," "locked," "reconciled," or "reversed" mean, precisely, for a Customer Invoice
>    in Accounting's own model — **and which of those states, if any, should be the exact fact
>    GROUP A's Sales cancellation gate checks?**

### 3.1 `XD1-01` — CORR2's "Question 3 is answered" verdict answers a truncated question

`SA_CORR2_01` §3.4 restates Question 3 as *"what do 'posted', 'locked', 'reconciled', 'reversed' mean
precisely for a Customer Invoice in Accounting's own model?"* and grades it
**`ANSWERED — by existing evidence, at FACT VERIFIED`**. **The clause after the em-dash is absent**
from CORR2's restatement and from its answer.

That dropped clause is **the same normative question as Question 1**, asked a second time about the
same object. So the set is not "one answered, two decisions". It is **one descriptive question about
the reference's behaviour (Q3a), and one normative question asked three ways (Q1, Q2, Q3b)**.

This is the programme's own recorded *unmeasured consequence clause* defect: a finding and its
consequence are two claims, and the well-evidenced half made the other feel safe.

**Status: `EVIDENCE-PROVEN`.**

### 3.2 `XD1-02` — CORR2's delivery instruction for Q3 is source-copying, by CORR2's own test

CORR2 disposes of Q3 as: *"Deliver `BE-13`…`BE-18` + `AE-04` into Group A's register. No research
required."* Those rows are, by their own registers' declarations, measured facts about the
**reference estate**.

One section earlier, on Question 1, CORR2 writes the correct rule:

> under the Clean Room / Nature DNA constitution **a reference behaviour is learning, never a
> determination**. Inheriting "none" by default is source-copying by omission.

Delivering a reference lifecycle into the target design register as the answer to *"what do these
states mean in Accounting's own model"* is the same act, performed deliberately rather than by
omission. **CORR2 applied its own rule to Q1 and suspended it for Q3 two paragraphs later.**

**Status: `EVIDENCE-PROVEN`.**

### 3.3 `XD1-03` — Question 3 has no referent in the SMEsPlus target model

> | Sales / Accounts Receivable | IN | Revenue and receivable recognition | **Proposed Entry — never a "customer invoice" object** |
> Every IN arrow terminates at CAP-02. No neighbour writes to the Ledger, Period state, or Audit
> Evidence directly — this is the enforceable meaning of "Accounting Core owns the moment a fact
> becomes authoritative."
> — `.../TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/B03_DOMAIN_BOUNDARY_MODEL.md` §3

There is no Customer Invoice inside SMEsPlus Accounting Core. Asking it what *posted / locked /
reconciled / reversed* mean **for a Customer Invoice** is asking about an object that, by an already
published structural decision, it does not hold.

**Status: `EVIDENCE-PROVEN`.**

---

## 4. `XD1-04` — the durability precondition is not open: the SMEsPlus baseline already answers it

CORR2's precondition, in full:

> **No customer-invoice state in the evidenced estate is durable enough to carry blocking weight.**
> Posted is reversible; locked is optional; reconciled is destructible across a closed period.
> **Requested:** decide which state blocks — and, in the same act, **which state SMEsPlus will make
> durable enough to block with.**

Clause 1 is a measured statement about **the evidenced estate**, and it is verified (§7). Clause 2
asks what **SMEsPlus** will make durable. **That clause was never measured against the SMEsPlus
design, and the SMEsPlus design answers it.**

### 4.1 What the target baseline already determines

All published, unsuperseded, single-version across all 184 branch heads *and* the mainline:

| Element | Determination | Source |
|---|---|---|
| Ledger states | **Four, minimal:** `DRAFT` · `COMMITTED` · `VOIDED` and `SUPERSEDED` — **reached only via a linked, dated Correction Entry, never a status flip** | `B04` §2 |
| The gate on mutability | **Downstream Consumption**, first-class. Amendment of a `COMMITTED` entry permitted **iff** `consumed == false` **and** Period open. Otherwise *"the ONLY correction path is a linked Correction Entry; permanent, regardless of Period status"* | `B04` §4 |
| Consumption triggers | **Three, enumerated:** included in a statutory filing or issued statement; matched against an external record; **or another `COMMITTED` entry references it or was computed from it.** Period close deliberately **not** one | `B04` §4 |
| Consumption permanence | *"Once a Consumed event is recorded against an Entry, it is never retracted, deleted, or reversed."* Enforced structurally — *"there is no operation in this domain's capability model that clears a Consumed event, by construction, not by policy"* | `B05` `BINV-07` |
| Immutability | *"Once a `COMMITTED` Entry is consumed […] its content is permanently frozen."* | `B05` `BINV-06` |
| Correction shape | A new Entry, **permanently and bidirectionally linked**; the original never overwritten; chainable | `B05` `BINV-05`; `B04` §6; `B11` #14 |
| Two temporal properties | **Effective Date and Recorded At separate and both immutable-once-recorded** — a backdated correction *"can change 'current' results but cannot touch 'as known at T' results"* | `B05` `BINV-11`/`12` |
| Higher tier for the dangerous case | **Restatement** requires authorization at least as strict as fiscal-year close and always emits a distinguished event, *"never silently blended"* | `B04` §3a; `B09` `CO-15` |
| Audit independence | Event log is *"a forced, append-only capability, structurally separate from the Entry's own state"*; history reconstructable from it **alone** | `B02` `CAP-08`; `B05` `BINV-08` |
| Fact/evidence indivisibility | *"there is no reachable state where one exists without the other"* | `B11` #18 |
| Idempotency | Every proposed Entry carries the origin domain's idempotency reference; a second commitment carrying a reference already seen is **refused**; both logged | `B11` #9 |
| Origin traceability | Every Entry carries an origin reference or a required actor + reason; commitment with neither is **refused** | `B11` #15 |
| Concurrency | A stale-state action *"fails cleanly […] it never silently overwrites"* | `B11` #17 |
| Draft cannot hide | A `DRAFT` beyond a policy age **must be surfaced** — never auto-posted, never auto-deleted | `B09` `CO-13` |
| Safe path not the harder one | Correction must not require a **higher** tier than in-place amendment | `B09` `CO-06` |

And the Boss ruling already says the same in its own words:

> The canonical Accounting Event is **immutable in identity and provenance**. **Same-event retry must
> not create duplicate accounting events.** **Reversal is a new accounting event referencing the
> original.** Every accounting event is bounded by Tenant + Company context. […] **Production
> corrections must preserve auditability through controlled correction/reversal/adjustment mechanisms
> rather than silent deletion.** — `BD-ACC-01`

> **Silent destruction of a settlement record is already prohibited for SMEsPlus by a standing Boss
> ruling.** *"Reconciled is destructible across a closed period"* is a statement about the reference
> that SMEsPlus is **already forbidden from inheriting**. It is not an open design question.

**Status: `EVIDENCE-PROVEN`.**

### 4.2 `XD1-05` — controlled negative: neither Phase SA nor CORR2 read that baseline

| Clause | Declaration |
|---|---|
| PATTERN | `BINV-06` · `B04_` · `B05_` · `proposed [Ee]ntry` · `Downstream Consumption` · `HO-05` · `HO-06` |
| PATH SET | the two package directories, **38 markdown files** (23 parent + 15 CORR2) — *orchestrator-corrected denominator, `XD1-C1`* |
| UNIT | file |
| RESULT | **0 for every pattern**, on two command shapes |
| POSITIVE CONTROL, identical shape and path set | `BD-ACC-01` → **28 files**. The instrument reaches |
| CORPUS REACH of the unread material | `BINV-06` → **28 blobs**, including six files of the Account programme's own menu-process deep study. **Other programmes read it. Phase SA did not.** |
| WHAT WAS NOT SEARCHED | any citation naming the material without using one of the patterns. A bounded negative about two directories, **not** a claim that no Phase SA author ever saw the file |

`SA07` §5 states the position that follows from not having read it: *"BD-ACC-01 is a **ruling**, and
rulings are not contracts."* True — **and the contract's design substrate was already written, in the
same repository, on the same branch, under `TEAM_B_DESIGN/`, and was never opened.**

This is the fourth consecutive occurrence of one defect, and the class is one step wider than CORR2
named it:

> **A party states the open question in the words it already uses — and then looks for the answer in
> the estate it was auditing, not in the design it was building.**

**Status: `EVIDENCE-PROVEN`.**

### 4.3 `XD1-06` — CORR2's own package contradicts itself on decision authority

| Where | Statement |
|---|---|
| `SA_CORR2_04` §4.3 | *"Owner: **SMEs Core**, to publish the contract. Boss confirms at the Functional Design gate. **This is not a new Boss question** — the ruling exists."* |
| `SA_CORR2_01` §6.1 | *"**What is missing is not a decision; it is the published contract that the decision presupposes.** It is a design obligation, correctly owned by SMEs Core."* |
| `SA14` `XD-06` | Resolution authority: *"**SMEs Core** — publish the cross-domain contract."* |
| `SA_CORR2_01` §3.6 and `SA_CORR2_13` §16 Decision 1 | The durability precondition is routed to **Boss**. |

**Three of four say SMEs Core owns it and it is not a Boss question. The fourth escalates it. The
escalation is the outlier and it is the one that reached the gate pack.**

**Status: `EVIDENCE-PROVEN`** — a cross-file consistency defect inside CORR2, of the class where a
package publishes a fact and its negation because no control grepped the universal claim against the
package's own register.

---

## 5. What business fact must become durable — the decomposition that dissolves the impasse

Group A asked which **invoice state** should block. There is no single fact behind that question.
There are **four**, with four owners, four durability requirements and four consumers. **Collapsing
them into one document lifecycle is the root cause of `XD-01`.**

| # | Business fact | Plain statement | Owner | Authoritative when | Durability class |
|---|---|---|---|---|---|
| `F-1` | **Commercial commitment** | "We agreed to supply X on these terms" | Sales | at confirmation | **Mutable, cancellable, status-only.** No financial effect |
| `F-2` | **Billing intent reserved** | "Quantity Q is already claimed by an in-progress billing document" | Sales / billing preparation | at draft creation | **Transient by design.** Visible, deterministically released, posts nothing |
| `F-3` | **Accounting Event** — revenue, receivable, output tax, cost of sales | "A financial fact came into existence, Tenant + Company bounded" | **Accounting Core** (`BD-ACC-01`) | at commitment | **Immutable in identity and provenance**; content frozen once consumed |
| `F-4` | **Settlement** | "This receivable has been discharged, and by what" | Accounting Core | at the matching act | **Append-only.** Reversal is a new dated linked event |

**The three exposures Group A worried about are all `F-3` and `F-4`. The counter it actually reads
today is `F-2`. The thing it wants to gate is `F-1`. Nobody had separated them, on either side of the
boundary, in three rounds.**

### 5.1 `XD1-09` — `F-2` and `F-3` are two facts, and the corpus measures the divergence

Team B's Sales canonical design records the collision and reserves it as an open choice:

> **Invoiced quantity — deliberate single-source requirement**: evidence shows two non-interchangeable
> variants (any-non-cancelled vs. posted-only) coexisting with no single canonical answer. TEAM B
> requires a target design to pick **one** […] flags for Boss/business input rather than resolves
> unilaterally. — `06_SALES_CANONICAL_DESIGN.md` §02

**The choice is unnecessary.** The draft-inclusive counter answers *"may I raise another billing
document for this line?"* — an `F-2` question whose correct answer **must** include unposted documents
or the same quantity is billed twice. The posted-only counter answers *"how much revenue has been
recognised?"* — an `F-3` question whose correct answer **must** exclude them or revenue is overstated.
**Both counters are right about different questions. Picking one guarantees the other becomes
unanswerable.**

Measured:

> **1,877 of 4,901 confirmed lines carry a draft invoice** […] The delivered-not-invoiced exposure was
> understated 24× — **1,145 lines (23.4%), not 47 (1.0%)** […] the sentence "the dominant cut-off
> exposure is billing ahead of performance" is **WITHDRAWN**.

**38.3 % of one deployment's confirmed commitment lines sit where the two counters disagree, and a
headline exposure figure inverts by 24× purely on which one is read.**

**Status: `EVIDENCE-PROVEN`.** This also **discharges Team B's reserved open item by proof, not by
choosing.**

### 5.2 `XD1-07` — the producer contract Phase SA recorded as absent exists at `PARTIAL`

`SA03` §5 and `SA04` `R-20` record *"no producer contract exists"*; `H-01` softens it to
*"`CONTRACT REQUIRED`"*. **Both are too strong.** The Account programme published a handoff register
containing the contract skeleton for exactly this boundary — `HO-05` (business fact → proposed
Entry), `HO-06` (commitment → durable event with permanent identity, *"no reset after consumption
(BINV-06); correction only additive"*), `HO-09` (*"Settlement status orthogonal to posting status"*),
each graded `PARTIAL`.

`I-5`: **0 of 38 Phase SA/CORR2 files mention it**, against a positive control of 28.

The accurate statement: **the contract exists at `PARTIAL`, in the producer's own vocabulary, and was
never published to the consumer.** That is a materially different remedy from "invent a contract" —
it is "complete, name, version and publish an existing `PARTIAL` one".

**Status: `EVIDENCE-PROVEN` — corrects `SA03` §5, `SA04` `R-20` and `H-01` at claim level.**

---

## 6. `XD1-08` — the symmetry premise, tested on both sides

Buy-side rationale, verbatim (present in all three blob versions):

> **Dual cancellation gate (locked OR an open vendor bill) vs. Sales' single gate**: TEAM B judges
> this a **legitimate, preservable business asymmetry** […] (**a Sales cancellation only touches draft
> invoices, never posted ones, by the same logic**). `ADAPT` both sides' actual gates as-is; do not
> force symmetry. — `07_PURCHASE_CANONICAL_DESIGN.md` §07

**(a) The mechanism claim is `NOT ESTABLISHED`.** The Account programme's measured position on
cancelling a commitment is *"Order | yes — status only | **nothing financial**"*. PATTERN
`cancel.{0,60}invoice|invoice.{0,40}cancel` over the 59 blobs of the Order-to-Cash package returns six
statements, **none** describing a commitment-cancellation cascade onto a billing document. **A bounded
negative over one package.** The mechanism half of Team B's rationale is a design assertion, not an
evidenced one.

**(b) The exposure conclusion survives on a stronger ground.** Under `BD-ACC-01` and
`BINV-05`/`BINV-06`, a recognised `F-3` fact **cannot be undone by cancelling `F-1` in any case**.
So neither gate is protecting the ledger. Both protect a **commercial** position — *the same purpose
on both sides*. **The asymmetry is an artefact of two sides designed against two different reference
behaviours, not a business truth.** And the sell-side exposure is the larger:

> A posted customer invoice creates **four** simultaneous exposures — revenue, receivable, tax and
> cost of sales […] **The sell-side exposure is the larger of the two**, and it includes a *statutory*
> element (tax) that the buy side's gate was never protecting. — `SA_CORR2_01` §3.3

**Status: `EVIDENCE-PROVEN` for (b); `MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP` for (a)** (§15 `G-1`).

---

## 7. Reachability — LIVE, LATENT, and merely capable

| Clause | Claim class | Status | Measurement |
|---|---|---|---|
| **"Posted is reversible"** | Capability `FACT VERIFIED`; **firing rate `UNMEASURED`** | `LATENT-CAPABLE` | Reset-to-draft permitted by default with four blocking conditions. **No count of occurrences exists in any deployed database.** PATTERN `reset to draft` over 3,900 blobs → 12 statements, every one a code-path or design statement, **none a deployment count** |
| **"Locked is optional"** | **Measured, and stronger than stated** | **`LIVE`** | *"Company records, all databases: **127**. With a fiscal-year lock date: **6 (4.7 %)**. […] With a hard (irreversible) lock date: **0**."* **121 of 127 companies carry no period control at all** |
| **"Reconciled is destructible"** | Code-path `FACT VERIFIED`; characterisation `SUPPORTED INTERPRETATION`; **firing rate `UNMEASURED`** | `LATENT-CAPABLE`, live enabling condition | *"the unreconcile path itself is not lock-date gated […] **The partial-reconcile model returns zero hits.**"* And **121 of 127 companies have no lock to cross** |
| **Sell-side consequence** | Measured, cross-generational | **`LIVE`** | **3,593 order lines across 5 of 8 deployed databases and 4 reference generations**, out of **172,341** confirmed lines; one database re-measured rises 47 → **1,145**, making 3,593 a **floor** |
| **The `F-2` hazard** | Measured | **`LIVE`** | **1,877 of 4,901 confirmed lines (38.3 %)** carry a freely-deletable draft that has already reduced what Sales believes it may bill |

### 7.1 `XD1-11` — the reference's strongest durability mechanism is field-scoped, not entry-scoped

An **independent** Account-programme package traced the guard chain for a business-material field
write on a **posted, sealed, lock-dated** ledger row:

> that list, at **every** supported hash version, is drawn only from description, debit, credit,
> account and partner. The intersection is empty, so the branch never raises **even on an entry
> carrying a hash**. […] **Which guard fires: none.**

with its own declared boundary (*"a code-path read, not an executed reproduction"*). Adoption of the
seal in the deployed estate is **`NOT MEASURED`**.

**Consequence:** even adopting the reference's strongest mechanism yields **field-list-scoped**
immutability that a business-material write can pass, on a per-journal opt-in an administrator must
remember. **That is not a foundation a blocking control can stand on.**

### 7.2 `XD1-10` — restated precondition

> **Corrected form of `C2-F-01`.** In the evidenced reference estate, no customer-billing document
> state is durable enough to carry blocking weight: reversal of a posted state is an evidenced
> capability whose **firing rate is unmeasured**; the period control that would constrain it is
> measured absent on **121 of 127** company records and its irreversible form on **0 of 127**;
> destruction of settlement links is an evidenced code path whose **firing rate is unmeasured**; and
> the strongest available integrity mechanism is opt-in and field-scoped. **In the SMEsPlus target,
> this question does not arise, because the target's durable object is not a document state.**

---

## 8. Retry, restart, reversal; transient; immutable or append-only

| Requirement | `F-1` | `F-2` | `F-3` | `F-4` |
|---|---|---|---|---|
| **Survive retry** | commitment identity | nothing | **the event identity**: a repeated submission carrying an origin reference already seen is **refused**, original and refusal both logged | settlement identity and linkage |
| **Survive restart** | current state | **nothing** — but its *absence* must be detectable | event, origin reference, both dates, audit record — **indivisibly** | match record and every reversal |
| **Survive reversal** | history of the cancellation | n/a | **the original, unchanged**, plus a bidirectional link; consumption never retracted | **the match record itself** — unmatch is a new linked event, never deletion |
| **May be transient** | quotation stage | **the whole of `F-2`**, if visible while it exists and released deterministically | nothing | nothing |
| **Immutable** | — | — | **identity, provenance, origin reference, Recorded At**; content once consumed | that a match occurred, and when |
| **Append-only** | commitment history | — | **the audit stream**, structurally separate from the entry | the match/unmatch chain |
| **Concurrency** | — | — | stale-state actions **fail cleanly, never silently overwrite** | same |

### 8.1 `XD1-16` — the idempotency element is reclassified

`JCP-03` / `C2-F-13` grade the deterministic accounting-event identity as *"one missing object,
recorded twice, owned by neither"*. Correct **about the reference and the two research programmes**.
Against the target it is superseded: `BD-ACC-01` assigns ownership, `B11` #9 specifies the mechanism
and the refusal behaviour, `B11` #15 the origin reference, `B04` §3 / `B05` `BINV-08` where the
evidence lives.

**Corrected grading: `SPECIFIED — OWNER ASSIGNED — 0 PROVEN`, not "owned by neither".** Exact key
shape is explicitly deferred past domain design by `B11` #9's own residual column and is not closed
here.

---

## 9. `XD1-12` — what requires blocking authority, and why it is not the invoice state

Under `BINV-05`/`06`/`07` and `BD-ACC-01`, a recognised `F-3` fact cannot be silently undone
regardless of what happens to `F-1`. Therefore:

> **Blocking the cancellation of a commercial commitment contributes nothing to ledger integrity. The
> ledger is already protected by a different mechanism, at a different layer, owned by a different
> domain.**

The sell-side gate is **not an accounting control**. It is a **commercial-exposure control**, and its
correct trigger is not a document status but:

> **Does an unreversed Accounting Event exist that is bound to this commitment by origin reference?**

Answerable because `B11` #15 makes the origin reference permanent and immutable on every entry, and
`BD-ACC-01` makes the event identity canonical. **Not** answerable from a document status, because the
target model has no such document inside Accounting Core (`XD1-03`).

**Where blocking authority genuinely is required** — already ruled and already designed:

| Control | Blocking? | Source |
|---|---|---|
| Commit an unbalanced entry | **Refused, structurally** | `B11` #1 |
| Commit into a closed period | **Refused** unless authorized recorded override | `B11` #2 |
| Commit a duplicate origin reference | **Refused**, both attempts logged | `B11` #9 |
| Commit without an origin reference | **Refused** | `B11` #15 |
| Amend a consumed entry in place | **Refused permanently** — correction only | `B04` §4; `BINV-06` |
| Backdate a correction into a consumed period | **Restatement tier only**, distinguished event | `B04` §3a; `CO-15` |
| Cancel a commitment with only `F-2` outstanding | **Not blocked.** Release the reservation; surface the stale draft | `B09` `CO-13` |

---

## 10. Accounting, tax, payment; correction; Tenant/Company; audit

**10.1 Accounting.** `F-3` at commitment creates revenue, receivable, output tax and — where policy
places it there — cost of sales. SMEsPlus's placement is already ruled: `BD-ACC-03A`/`03B`, Product
Category only. `ND-10` requires `Perpetual` and `Periodic` to be *defined* wherever used, because the
same two words denote different recognition points across reference generations. Deployed
confirmation the placement is not theoretical: **447,384 ledger lines and 74,982 valuation layers,
and the invoice-side cost mechanism has never executed once.**

**10.2 Tax — Company-scoped, statutorily held.** `BD-ACC-02` makes VAT, WHT, registers, reporting,
ownership and filing **Company-scoped**, with no cross-company posting, offsetting, aggregation or
filing authority. **Every Thai statutory consequence of cancelling a commitment carrying an issued tax
document is `HOLD — STATUTORY EVIDENCE REQUIRED`** — eight such questions stand held in the owning
package. **This register makes no statutory claim and closes none of them.**

`XD1-17`: one of `AE-10`'s two cash-basis preconditions is measured **present** in a deployed company,
while `AE-10`'s negative was stated about the **localisation template**, not a deployment; the second
precondition is `NOT MEASURED` there. **Two different populations, not a contradiction** — but the
settlement→tax dependency is closer to live than the template-level reading suggests.

**10.3 Payment and settlement.** Two facts must be carried into the contract: a receipt may produce
**no ledger entry at all** in one configuration, and derived entries arising from a settlement are, on
unmatch, **reversed rather than deleted and re-dated forward**. The first is a configuration hazard
SMEsPlus must design out; the second is a *shape* worth keeping — reversal rather than deletion —
while rejecting the silent re-dating.

**10.4 Correction and reversal.** One mechanism, two purposes, no status flips: a correction is a new,
ordinary, dated Entry, bidirectionally linked, subject to every posting gate; tagged **void** for a
full reversal, **supersede** when it carries a replacement value. Chains are first-class. The safe
path must not be the harder path (`CO-06`), **except** Restatement, deliberately stricter (`CO-15`).

**10.5 Tenant / Company boundary.** Measured: **all nine financial effects in the Order-to-Cash event
register are `COMPANY`-scoped; none at Tenant or Platform scope.** Design side: `BINV-03` forbids an
Entry spanning Companies; `CO-10` requires operation within one tenant's context and forbids shared
mutable state across tenants, naming document numbering specifically — *"a cross-tenant-visible
sequence would itself leak information"*. A legitimate inter-company transaction is **two independent
Entries, one per Company**, linked only by a shared origin reference.

A cancellation-gate severity is a commercial control and is none of `MTI-D-03`'s four no-fork
behaviours, so it is legitimately tenant-configurable — but any `XD-01` contract inherits the
isolation lineage's standing status: **58 invariants specified, 0 proven.**

**10.6 Audit.** Append-only stream structurally separate from the entry (`CAP-08`); history
reconstructable from that stream **alone** (`BINV-08`); commitment and audit event indivisible
(`B11` #18); tamper-evidence **by default across the whole trail**, adopted as a SMEsPlus initiative
and explicitly **not** claimed as a Thai legal requirement (`CO-07`); retention as a **floor** that
cannot be configured below the legal minimum (`CO-11`).

---

## 11. Architecture alternatives, compared on criteria declared before the comparison

**`ALT-A` — Document-state gate.** Publish a customer-billing-document lifecycle state across the
boundary; block when it has a named value. The shape Group A's questions presuppose.

**`ALT-B` — Event-and-consumption gate.** The gate asks Accounting Core one question: *does an
unreversed Accounting Event exist bound to this commitment by origin reference, and is it consumed?*
No document state crosses the boundary.

**`ALT-C` — No gate; coexistence plus a standing reversal obligation.** Cancellation always proceeds;
where a bound unreversed Accounting Event exists the commitment enters a named, non-dismissible
*reversal-owed* condition until a linked correction discharges it. Extends a rule Team B has
**already adopted** on the physical side.

| Criterion | `ALT-A` | `ALT-B` | `ALT-C` |
|---|---|---|---|
| Conforms to `BD-ACC-01` | **No** — publishes a document state as the accounting interface | **Yes** | **Yes** |
| Conforms to `B03` §3 | **No** — requires an object Accounting Core does not have | **Yes** | **Yes** |
| Durability of the blocking fact | **Weak** — §7 shows the mechanism is opt-in, field-scoped, measured absent | **Strong** | **Strong** |
| Defeatable without a trace? | Yes, wherever a status can be moved | **No** | **No** |
| Cross-module coupling | **High** — consumer learns producer vocabulary | **Low** | **Low** |
| Correct for services / non-goods revenue | Unclear | **Yes**, via `ND-11` | **Yes** |
| Handles dropship (`H-02`/`H-03`) | **No** | **Yes** — absence of a bound cost event is the answer | **Yes** |
| Statutory / tax exposure | Highest | Lowest | Low, persists until discharged |
| Operational effect on a live estate | Would false-block **1,877 of 4,901 lines (38.3 %)** carrying only `F-2` | Blocks only where a real `F-3` exists | Blocks nothing; converts exposure to a tracked obligation |
| Requires that does not yet exist | A document-lifecycle contract **and a durability mechanism the target design does not provide** | **Nothing new** — completion of `HO-05`/`06`/`09` plus `F-2` as a named released reservation | The above, plus an obligation object |

**`ALT-A` is rejected on proof, not preference.** It fails two structural conformance tests, its
blocking fact has no durability substrate, and it would produce a live false-block rate of 38.3 %.

---

## 12. Recommendation

> ### `XD-01` — SMEs CORE ARCHITECTURE RECOMMENDATION, `EVIDENCE-PROVEN`
>
> **`XD1-R1` — Separate the four facts.** No SMEsPlus register may use one term for two of them.
> **This dissolves Team B's reserved "pick one invoiced quantity" item by proof: they are two facts
> and both are kept, separately named and separately owned.**
>
> **`XD1-R2` — Adopt `ALT-B` as the structural rule.** The gate asks Accounting Core exactly one
> question over the canonical Accounting Event Identity. No document state crosses the boundary.
>
> **`XD1-R3` — Adopt `ALT-C`'s behaviour where the gate does not trip, or trips and is overridden.**
> A named, **non-dismissible** *reversal-owed* condition, clearable only by a linked correction —
> never by manual dismissal, auto-expiry, archival or cleanup.
>
> **`XD1-R4` — `F-2` is a released reservation, not an inferred count.** Visible while it exists,
> deterministically released, holder surfaced when stale. **Never the input to an accounting or
> cut-off figure.**
>
> **`XD1-R5` — Publish the contract; do not invent it.** Complete, version, name and publish
> `HO-05`/`HO-06`/`HO-09` as the `XD-06` cross-domain contract, carrying: canonical event identity;
> origin reference; Effective Date and Recorded At; consumption status; Tenant + Company; correction
> linkage; idempotency reference. **Owner: SMEs Core. Boss confirms at the Functional Design gate —
> the authority CORR2 itself recorded three times out of four.**
>
> **`XD1-R6` — Gate severity is configurable; platform default `block`.** Outside `MTI-D-03`'s no-fork
> boundary, so legitimately tenant-configured. Default `block` because the sell-side exposure is the
> larger and includes a statutory element. **The residual authority question about that default is at
> §14.3.**

### 12.1 What was deliberately not copied

| Not adopted | Reason |
|---|---|
| The reference's billing-document lifecycle as the interface | The ruling makes the **event identity** canonical; `B03` §3 forbids Accounting Core learning source vocabulary |
| Its reversible posted state and reset-to-draft affordance | `BINV-06` replaces it |
| Its optional, per-journal, field-scoped integrity seal | §7.1 shows it is passable; `CAP-08` + `CO-07` replace it with a whole-trail guarantee |
| Its period lock as a **redirect** | `B11` #2 replaces it: bar at create, no context-level bypass |
| Its draft-inclusive counter as *the* invoiced quantity | `XD1-R1` — two facts, both kept |
| The buy-side gate shape mirrored onto the sell side | Mirroring would import the reference's accident. **One rule replaces both sides** |
| **"None"** — the reference's answer, inherited by omission | The defect `SA12-F-01` names, refused here as CORR2 refused it for Q1 |
| The reference's settlement-destruction behaviour | Already prohibited by `BD-ACC-01` |

---

## 13. Findings register

| ID | Claim | Status |
|---|---|---|
| `XD1-01` | Group A's Q3 has a second clause CORR2's restatement drops; Q3b is Q1 restated | `EVIDENCE-PROVEN` |
| `XD1-02` | CORR2's Q3 disposition is source-copying by the test CORR2 applies to Q1 two paragraphs earlier | `EVIDENCE-PROVEN` |
| `XD1-03` | Q3 has no referent in the target model: Accounting Core holds a **proposed Entry, never a customer-invoice object** | `EVIDENCE-PROVEN` |
| `XD1-04` | The durability precondition's clause 2 is already determined by published target design plus `BD-ACC-01` | `EVIDENCE-PROVEN` |
| `XD1-05` | Neither Phase SA nor CORR2 read that baseline. **0 of 38 files** on seven patterns; positive control **28**; corpus reach of the unread material **28 blobs** | `EVIDENCE-PROVEN` |
| `XD1-06` | CORR2 publishes both *"this is not a new Boss question"* and a Boss escalation of the same object | `EVIDENCE-PROVEN` |
| `XD1-07` | A producer contract skeleton exists at `PARTIAL` (`HO-05`/`06`/`09`); *"no producer contract exists"* is too strong | `EVIDENCE-PROVEN` — corrects `SA03`, `SA04` `R-20`, `H-01` |
| `XD1-08a` | Team B's mechanism premise is not established in either party's evidence | `MATERIAL HOLD` (§15 `G-1`) |
| `XD1-08b` | The gate is a commercial control, not a ledger control; sell-side exposure is the larger | `EVIDENCE-PROVEN` |
| `XD1-09` | The two billed-quantity counters are two business facts. Divergence **1,877 of 4,901 (38.3 %)**; a headline figure inverts **24×** on basis alone | `EVIDENCE-PROVEN` — discharges Team B's reserved item |
| `XD1-10` | Reachability separated: *locked is optional* **LIVE** (121/127, 0/127 irreversible); the other two **LATENT-CAPABLE, firing rates unmeasured**; sell-side consequence **LIVE** (3,593, a floor) | `EVIDENCE-PROVEN` |
| `XD1-11` | The reference's strongest durability mechanism is field-scoped and opt-in; adoption rate `NOT MEASURED` | `EVIDENCE-PROVEN` (source-read) |
| `XD1-12` | The blocking control does not belong on a document state | `EVIDENCE-PROVEN` |
| `XD1-13` | **No SMEsPlus AR / Receivables design pack exists.** `0 of 3,579` paths; positive control **292** | `EVIDENCE-PROVEN`; gap `G-3` |
| `XD1-14` | CORR2's precondition is two claims; clause 2 was never measured against the target, which answers it | `EVIDENCE-PROVEN` |
| `XD1-15` | All nine sell-side financial effects are `COMPANY`-scoped; isolation lineage remains **58 specified, 0 proven** | `EVIDENCE-PROVEN` for scope; **`0 PROVEN`** carried |
| `XD1-16` | Deterministic identity reclassified from *"owned by neither"* to **`SPECIFIED — OWNER ASSIGNED — 0 PROVEN`** | `EVIDENCE-PROVEN` |
| `XD1-17` | One of `AE-10`'s two cash-basis preconditions is measured present in a deployment; a population distinction, not a contradiction | `EVIDENCE-PROVEN` |
| `XD1-C1` | *(orchestrator)* the executor's *"0 of 41 files"* denominator is **38** at the unit actually searched; result unchanged | `CORRECTED` |

**Register integrity, executed:** 19 identifiers — `XD1-01`…`XD1-17` with `XD1-08` split, plus
`XD1-C1` — each appearing exactly once; family contiguous; every `XD1-` identifier cited in the body
is defined here and vice versa.

---

## 14. Disposition and reclassification

### 14.1 Question by question

| Question | CORR2 | CORR3 after proof | Owner |
|---|---|---|---|
| **Q1** which state *should* block | `NOT ANSWERED — NORMATIVE`; **Boss** | **`TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED`.** The premise is false: no *state* should block | **SMEs Core** |
| **Q2** does a posted invoice constitute blocking exposure | `NOT ANSWERED — DECISION`; **Boss** | **`PROOF ESTABLISHED`.** Yes, and the larger of the two — but a **commercial** exposure, not ledger-integrity | **SMEs Core** |
| **Q3a** what the reference's states mean | `ANSWERED — deliver` | **`ANSWERED — AND MUST NOT BE DELIVERED AS A TARGET SEMANTIC`** | **SMEs Core** — deliver as *learning*, tagged |
| **Q3b** which state the gate checks | *not restated by CORR2* | **`PROOF ESTABLISHED`.** None. The gate checks a fact, not a state | **SMEs Core** |
| **Durability precondition** | `RAISED`; **Boss**, *"in the same act"* | **`EVIDENCE-PROVEN — ALREADY DETERMINED`** | **SMEs Core** — publish the contract |

**`XD-01` overall: `EVIDENCE-PROVEN ARCHITECTURE RECOMMENDATION`**, with bounded material HOLDs at
§15, none of which re-opens the architecture.

### 14.2 CORR3 §3 reclassification of CORR2 Decision 1

**Class `A` — `SMEs CORE CAN RESOLVE — STUDY/PROOF REQUIRED`, resolved by this register. Not class
`D`.** The two governance observations falling out of it are class `B`: the claim-level correction of
`SA03`/`SA04` `R-20`/`H-01` (`XD1-07`), and the internal-contradiction correction inside CORR2's own
decision-authority statements (`XD1-06`).

### 14.3 The one residual genuine policy item, in the required form

> **`XD1-P1` — the platform default for gate severity.**
>
> **What is proven.** The gate's trigger, data contract, durability substrate, failure behaviour,
> audit requirements and Tenant/Company scoping are all determined (§§5–12). The gate is a commercial
> control outside `MTI-D-03`'s no-fork boundary, so it is legitimately tenant-configurable.
>
> **What alternatives survive proof.** Exactly two, both architecturally sound: default **`block`**
> (refused while an unreversed bound Accounting Event exists, overridable at a named tier, override
> audited) or default **`warn-and-allow`** (proceeds into the non-dismissible reversal-owed condition).
> **Nothing in the evidence distinguishes them on correctness, durability, auditability or statutory
> exposure** — both leave the ledger equally protected and both leave an equally complete trail. They
> differ only in **whose** work the friction lands on, and in tolerance for open commercial exposure.
>
> **SMEs Core recommends** default **`block`**, because the sell-side exposure is the larger and
> carries a statutory element the buy-side gate was never protecting.
>
> **The precise authority reason SMEs Core cannot settle it.** Group A's owning session reserved this
> exact election to Boss in writing — *"(a) require a symmetric Sales-side gate once Accounting
> supplies the answers above, or (b) accept the current asymmetry as a disclosed risk trade-off.
> **Not decided by this session.**"* — and that reservation has never been discharged. **Accounting
> has now supplied the answers, which was the reservation's stated precondition. SMEs Core may not
> discharge a reservation it does not hold, and a platform default is a risk-appetite election, not a
> technical determination.** Offered as a confirmable recommendation, not a research or design gap.

---

## 15. Residual uncertainty, proof gaps, and what to attack first

### 15.1 Residual uncertainty

| ID | Item | Bound |
|---|---|---|
| `G-1` | Whether cancelling a commitment reaches its in-progress billing documents at all | Six statements over 59 blobs, none describing such a cascade. **Bounded to one package.** Not searched: the Group A design tree in that vocabulary, the other ten Account process packages, the deployed databases. `NO EVIDENCE FOUND`, not `DOES NOT EXIST` |
| `G-2` | Live firing rate of posted-state reversal; adoption rate of the integrity seal | Both **`NOT MEASURED`**. `XD1-10`'s `LATENT-CAPABLE` classification rests on that absence and would move to `LIVE` on a single measurement |
| `G-3` | **The SMEsPlus AR / Receivables domain has no design pack** | `0 of 3,579` paths against a control of 292. `F-2`'s document, numbering, statutory presentation and release semantics belong to a pack that does not exist |
| `G-4` | Thai statutory consequences of cancelling a commitment carrying an issued tax document | `HOLD — STATUTORY EVIDENCE REQUIRED`. **No statutory claim is made here and none is closed** |
| `G-5` | Tenant/Company enforcement | **58 specified, 0 proven**, carried unchanged. Any contract published under `XD1-R5` inherits this and must not be read as proving isolation |
| `G-6` | `B11` #9's exact idempotency-key shape | Deferred past domain design by its own residual column. Not closed here |

### 15.2 What could not be proven, and the exact gap

1. **That `ALT-B` is implementable at the stated cost.** The origin reference is *mandated* by
   `B11` #15 but **`0 PROVEN`**. The gap is a conformance test at the Functional Design gate, which
   this register is forbidden from entering.
2. **That `F-2`'s release semantics are complete.** Billing documents are **merged across commitments
   by default** with only a per-line structural link, which makes release non-trivial. Gap: an
   enumerated release matrix over the merge cases.
3. **That the gate is correct for the dropship shape.** `ALT-B` returns *no bound cost event*, right
   only if `ND-09`'s explicit recorded determination is present. `H-02`/`H-03` remain open.
4. **That CORR2 did not read the target baseline for a reason recorded elsewhere.** The negative is
   about **two directories and seven patterns**, and is stated at that width.

### 15.3 The claim a challenger should attack first

> **Attack `XD1-04`.** Everything else is a correction, a measurement or a decomposition. `XD1-04` is
> load-bearing: that the SMEsPlus Accounting Core baseline already determines the durability semantics
> CORR2 escalated.
>
> 1. **Governance status.** These files carry a Boss Gate and Team B handoff authorization plus seven
>    independent audit rounds, and are single-version across all 184 branch heads and mainline. It was
>    **not** established that they are *approved as binding at the same tier as* `BD-ACC-01`; their own
>    final-gate document is titled a **candidate**. If a governance instrument places them lower,
>    `XD1-04` weakens from *determined* to *specified-and-recommended*. **Strongest available attack,
>    and it could not be closed from the corpus.**
> 2. **Supersession.** Version multiplicity was checked and no retiring artefact found — but not
>    exhaustively for a supersession notice in a third package naming them without a searched
>    identifier. The programme has been burned by *right branch, right SHA, wrong file*.
> 3. **The consumption trigger list.** `B05` `BINV-06`'s own residual column concedes the three-trigger
>    list *"is this domain's own design judgment […] flagged explicitly as a Team B design assumption
>    requiring gate review."* The recommendation makes consumption the durability gate. **If the trigger
>    list is wrong, the gate is wrong — and its author already said so.**
>
> Secondary: `XD1-09`'s 38.3 % is **one** deployment, and its source states *"every other row remains
> draft-basis and is therefore a floor, not a measure."* Direction corroborated across four
> generations; **magnitude is single-deployment.**

---

`CP-SA-C3-10 (XD-01 limb) — execution status.` Nineteen findings; `XD-01` reclassified from
`OPEN — BOSS AUTHORITY REQUIRED` to an `EVIDENCE-PROVEN` architecture recommendation owned by SMEs
Core, with six bounded residuals and **one** residual policy election stated in the required form.

Checkpoint completion is **not** Boss approval. Boss remains the sole Final Approver.
