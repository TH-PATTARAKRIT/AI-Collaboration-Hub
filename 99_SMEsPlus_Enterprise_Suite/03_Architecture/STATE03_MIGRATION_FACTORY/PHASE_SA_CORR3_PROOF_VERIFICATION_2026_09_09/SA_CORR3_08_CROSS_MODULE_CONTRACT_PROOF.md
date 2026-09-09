# SA_CORR3_08 — CROSS-MODULE OUTPUT → INPUT CONTRACT PROOF
## CP-SA-C3-50 · CP-SA-C3-60 · CP-SA-C3-70

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR3-PROOF-001]`
Finding prefix `XMC-` · Frame: **`CORR3-FRAME`**, adopted by pointer, not re-declared.
Controls re-fired before any count: positive `BD-ACC-01` → **55** blobs (two shapes); `clean.room`
(-i) → **1,266**; negative `qxvz7481_no_such_token` → **0**; corpus size re-verified at **3,900** by
directory enumeration, a different shape from the extraction log.

Governing law: master prompt §1 and §11 — `INPUT → PROCESS → OUTPUT → DOWNSTREAM ROUTING → NEXT
MODULE INPUT`, and for every material handoff **UPSTREAM OUTPUT = DOWNSTREAM REQUIRED INPUT**.

> **Orchestrator intake note.** Same-model executor; `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not
> adopted on its word.** Two load-bearing findings re-executed and **CONFIRMED**:
> - **`XMC-F-12`** — the 16-element contract's own title is *"Inventory → Accounting Minimum Handoff
>   Data Contract"* and **all four** scope clauses bind it to that one boundary in one direction
>   (lines 16, 31, 56, 83). Verified verbatim.
> - **`XMC-F-01`** — over the active Phase SA package, `10_INVENTORY_CROSS_MODULE_HANDOFF` → **0
>   files**, `07_INVENTORY_ACCOUNTING_CONTROL_IMPACT` → **0**, `HX-` → **0**, while
>   `03_INVENTORY_FUNCTIONAL_DESIGN_V1` → 1 and `FINAL_SOLUTION` → 1. The instrument reaches; the two
>   artefacts whose whole subject is the cross-module accounting interface were never opened.
> - The §3 disposition rule quoted by the executor is verbatim at line 50.

---

## 1. Method, and what `PROVEN` means for a contract at Phase SA

### 1.1 The two primary instruments, read at primary text

| Instrument | Primary pointer | Status, verbatim |
|---|---|---|
| **`BD-ACC-01`** | blob `1db097c7…`, `.../01_BOSS_APPROVED_ARCHITECTURE_RULINGS.md` | `CLOSED / BOSS APPROVED` |
| **The 16-element Minimum Handoff Data Contract** | blob `b4c39831…`, on `origin/SMEsPlus`, commit `d9e845e` | `BOSS APPROVED / EFFECTIVE`; execution evidence `PENDING PER SCENARIO / HANDOFF` |

Element count validated on three shapes: numbered-list lines → **16**; maximum ordinal → **16**; the
document's own self-descriptions `16 mandatory` and `16-field`. All three agree.

`BD-ACC-01` carries one sentence that governs §3, quoted because it is an **authority grant**:

> Phase SA may design the technical representation independently; this ruling does not prescribe
> UUID/ULID/sequence/schema implementation.

### 1.2 `XMC-F-12` — the contract's declared scope is narrower than the programme has been reading it

Read at primary text, **four times in four places**:

> **Title** — *"Inventory → Accounting Minimum Handoff Data Contract"*
> **§1** — *"an additional mandatory Final Solution control for every material handoff **from Inventory
> Core to Accounting Core**."*
> **§4** — *"For every scenario with **an Inventory → Accounting handoff**…"*
> **§5** — *"…for **all material Inventory → Accounting interactions**…"*

**The contract is scoped to one boundary in one direction.** Of the twelve handoff classes master
prompt §11 mandates, exactly **one** falls inside it. Sales → Inventory, Sales → Manufacturing,
Sales → Purchase, Manufacturing → Inventory, Sales → AR, Purchase → AP, Payment → Bank,
Asset → Accounting, Expense → Accounting, Tax → reporting and Close → subledgers have **no
Boss-approved element contract of any kind.**

**This is a finding about Phase SA's reading, not about Boss's ruling.** The ruling is precise; the
programme has been treating its sixteen elements as a suite-wide handoff standard. That reading is
convenient and has never been checked against the approval's scope clause. `XMC-D-02` asks whether
Boss extends the scope or whether each boundary gets its own contract.

**Consequence:** the 16 elements are applied as a **test** only where the ruling applies them, and as
a **checklist of questions** elsewhere, with the difference stated in every row. **A proof that
silently widens the scope of the standard it invokes is not a proof.**

### 1.3 What `PROVEN` means here

A row is `PROVEN` only when **all seven** hold:

| # | Clause |
|---|---|
| `P1` | The upstream output is **named by its owner** in a primary artefact, in the owner's own vocabulary |
| `P2` | The downstream required input is **named by its consumer** in a primary artefact |
| `P3` | `P1` and `P2` are **the same fact at business-semantic level**, established by reading both primaries — not by two registers agreeing |
| `P4` | The route is justified by **Business Nature**, not module name |
| `P5` | **Every** downstream consumer is enumerated. A missing consumer is a defect |
| `P6` | The consumer can **join** the fact to its origin, its correction and the other half of the same commercial act, by an identity surviving retry, replay and reversal |
| `P7` | At the Inventory → Accounting boundary, each of the 16 elements is **supplied, or `N/A` with reason, or `HOLD / EVIDENCE REQUIRED`** |

**The standard for "supplied" is the approval's own, and it is three conjuncts:** *"known, traceable,
**and** evidence-backed"*. `SA_CORR2_04` §3 applied that standard to element 10 and concluded, rightly,
that *"a specification satisfies none of the three on its own"*. **This register applies the same
standard to every element, including the ones a specification would be pleasant to close.** That
symmetry is what §6 turns on.

### 1.4 Self-review status

Every challenge here is **INTERNAL ADVERSARIAL SELF-CHALLENGE**, same model, same session. Not
independence, and nowhere presented as such.

---

## 2. The handoff contract register

### 2.1 `XMC-F-01` — the register Phase SA was chartered to build already exists in one direction, and Phase SA never opened it

**Instrument.** PATTERN `\bHX-[0-9]{2}\b`, case-sensitive, word-bounded; PATH SET the whole frame,
no pre-filter; attribution by joining blob → path afterwards. **RESULT: 13 blobs / 13 paths / 112
occurrences**, three command shapes agreeing on the blob figure. Positive control: the two Phase SA
packages are reachable from this instrument (**39** blobs by path join); `BD-ACC-01` fires **55**.
Negative control **0**. **Paths under either Phase SA package: 0.**

The source is `.../FINAL_SOLUTION/INVENTORY/V1_0/10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md`, which
publishes **31 handoff rows, `HX-01`…`HX-31`**, each with From → To, the fact handed over, the
trigger, the receiver's obligation, and a class. Row count validated on three shapes → **31**. Its
status line: `SMEsPlus-OWNED HANDOFF DESIGN — BUSINESS FACTS ONLY — CLOSES NO JOINT OR ACCOUNTING
DECISION`.

**Measured consumption of the 30-artefact package by the two Phase SA packages** (positive control:
`03_INVENTORY_FUNCTIONAL_DESIGN_V1` returns 1, so the instrument fires):

| Artefact | Cited? |
|---|---|
| `02_…EXECUTIVE_SUMMARY.md` | yes — once, in `SA_CORR2_03` |
| `03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` | yes — once, §7 only |
| `07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md` | **0** |
| `10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md` | **0** |
| `08_…VALUATION_LANDED_ANALYTIC_COST_V1.md` · `12_…RISK_GAP_DECISION_REGISTER_V1.md` | **0** |
| the token `HX-` | **0** |

Corroborating on identifiers: of the twelve Joint decisions, **4** appear anywhere in either Phase SA
package; of the nine `TH-HOLD-xx` statutory items, **0** do, while `JT-` returns non-zero in the same
files — so the zero is controlled.

> **`XMC-F-01`. Phase SA's cross-module assurance consumed 2 of the 30 artefacts of the only
> SMEsPlus-owned domain design package in the repository, and neither of the two whose whole subject
> is the cross-module accounting interface. `SA03`/`SA04` built a 28-route producer→consumer matrix
> without reading the 31-row handoff register one of the two producers had already published.**

**This is one level worse than the "party searches its own directory" defect `SA_CORR2_01` §2 names.**
CORR2 **reached the package** — it quotes §7 of the functional design and the exec summary's boundary
rule — and consumed one paragraph of each. **The bound of a read is not the bound of a package.**

### 2.2 `XMC-F-10` — one side of every Inventory ↔ Accounting contract has an owner-side design and the other has none

**Instrument.** `awk -F'\t' '$2 ~ /FINAL_SOLUTION/'` over `bpb_FULL.tsv`; **30 paths / 30 blobs**, and
**0** outside `FINAL_SOLUTION/INVENTORY` (validated by an inverted-match count, a second shape). Two
version directories: `V1_0` (18) and `V2_0` (12).

There is **no** `FINAL_SOLUTION/ACCOUNT`, `FINAL_SOLUTION/SALES` or `FINAL_SOLUTION/PURCHASE`.
Authority for the unsearched: the complement of `CORR3-FRAME`. **A real, stated residual and the first
thing a challenger should test** (§8).

> **Structural consequence:** for every Inventory → Accounting handoff, the **producing** side has a
> published, versioned, SMEsPlus-owned design naming the fact, its payload and its trigger; the
> **consuming** side has research packages, reconciliation matrices and Boss rulings, and **no design
> artefact stating what it requires**. `UPSTREAM OUTPUT = DOWNSTREAM REQUIRED INPUT` cannot be proved
> when only one of the two terms has been written down by its owner. **Clause `P2` fails on the
> Accounting side of every row in this register.**

### 2.3 `XMC-F-02` — the producer's own published payload against the sixteen mandated elements

`07_INVENTORY_ACCOUNTING_CONTROL_IMPACT_V1.md` §1.1 defines what a valuation fact carries, in seven
rows: *Event type · Quantity and unit · Cost basis and amount · Effective date · References (source
document, movement fact, product, category, warehouse, lot where applicable) · Reason and approver ·
Policy version.* **This is the first time in the programme the emitting payload has been compared to
the mandated elements.**

| # | Mandated element | Carried by the published payload? |
|---:|---|---|
| 1 | `WHAT happened` | **CARRIED** — Event type, ten named values |
| 2 | `WHO owns the fact` | **CARRIED BY THE OWNERSHIP RULE, NOT BY THE PAYLOAD** |
| 3 | `WHEN physical event occurred` | **CARRIED** |
| 4 | `WHEN financial recognition occurs` | **`N/A` BY DESIGN, WITH REASON** — the producer *"never decides recognition timing"*; the approval expressly permits *"or explicit pending/hold condition"*. **A compliant `N/A`, not a gap** |
| 5 | `HOW MUCH quantity` | **CARRIED** |
| 6 | `WHICH UOM` | **CARRIED** |
| 7 | `WHAT valuation/cost basis applies` | **CARRIED** — basis, amount, and the method version that produced it |
| 8 | `WHICH Product / Lot / Serial` | **PARTIAL** — serial not named in the payload |
| 9 | `WHICH Warehouse / Location` | **PARTIAL** — location not named |
| **10** | `WHICH Company / Tenant` — **unconditional** | **ABSENT.** `tenant` occurs **once** in the whole artefact and not in §1.1 (two shapes agree); `company` occurs on **4** lines, none in §1.1. Positive control: `company` fires 7 times in the same file |
| 11 | `WHICH Source Document` | **CARRIED** |
| 12 | `WHICH Original Event` | **PARTIAL** — a *movement fact* reference. **A movement reference is not an accounting-event identity, and that distinction is the whole of `BD-ACC-01`** |
| 13 | `WHICH Reversal / Correction` | **ABSENT from the payload** — correction-by-new-movement is stated as a principle; **no element carries the link** |
| 14 | `WHICH Migration / Replay Batch` | **ABSENT**, and the producer says so: the provenance reference *"does not exist yet"* |
| 15 | `WHICH Idempotency Identity` | **ABSENT** — see `XMC-F-11` |
| 16 | `WHAT Evidence proves it` | **PARTIAL / CONDITIONAL** — an evidence pack exists for scrap only |

**Tally, executed by reading the right-hand column: 6 carried · 1 `N/A` by design · 1 carried by rule
not payload · 4 partial · 4 absent = 16**, each of 1…16 exactly once. ✓

> **`XMC-F-02`. Element 10 — the one element the approval states with no qualifier, and the one proved
> sufficient on its own to produce `0 of 22` — is absent from the emitting party's own published
> payload. That is a second, simpler, entirely independent cause of the same result, and no register
> in the programme records it.**

`SA_CORR2_04` §3 established element 10 fails because the invariant set is *specified, not built, not
verified*. That is a **proof-side** cause and it is correct. **This is an interface-side cause: even
with 58 invariants proven and every enforcement surface built, a valuation fact whose declared payload
has no company or tenant field would still not supply element 10. Two causes, and closing the one
everybody is working on does not close the other.** `RISK-U03`'s remedy is necessary and **not
sufficient**.

### 2.4 `XMC-F-11` — a requirement with no carrier

The producing package states element 15's requirement as a design rule — `HR-02`, *"A retried handover
must be recognisable as the same fact, not treated as a second one"* — and **its payload has no
element in which to put the thing that would make `HR-02` executable.** A rule stated on the producer,
addressed to nobody, carried by nothing.

Same shape as `JCP-03` from a third angle. `SA_CORR2_04` found element 15 recorded as missing by both
domains, *"owned by neither."* **`XMC-F-11` adds that the producing side published the obligation
without publishing a place to satisfy it — which is why neither party experienced itself as failing to
deliver.**

### 2.5 The contract register — 18 rows

The `16-el` column is a **test** only for Inventory → Accounting and a **checklist** elsewhere.

| # | Handoff (Business Nature basis) | MATCH / GAP | Exact missing element if GAP | 16-el | Status |
|---|---|---|---|---|---|
| `XMC-H-01` | **Sales → Inventory** | MATCH at fact level; **GAP at guarantee level** | The route is **indirect via the rule engine** on the sell side and **direct and synchronous** on the buy side, so *"a confirmed commitment produces a movement"* is true on one side and eventually-true on the other. No published contract states which | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-02` | **Sales → Manufacturing** | GAP | **The manufacturing order never raises its own demand** — the raiser is the replenishment rule engine acting on a deficit. The Supply Nature rule deciding *make* is itself undetermined | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-03` | **Sales → Purchase** (dropship / MTO) | **GAP — a control breach, not a data gap** | The write **bypasses the demand-approval gate every human-raised purchase must pass**. A document enters a module **below that module's own control floor** | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-04` | **Manufacturing → Inventory** | MATCH | — | out of scope | **`HOLD — EXACT GAP`** — fails only on `P6` and on the `XMC-H-05` leg beneath it |
| `XMC-H-05` | **Inventory → Accounting** | GAP | **Element 10 absent from the payload · element 15 absent with its requirement stated but uncarried · element 14 absent by the producer's own record · elements 12 and 13 partial** | **IN SCOPE — tested** | **`HOLD — EXACT GAP`** |
| `XMC-H-06` | **Sales → AR / Accounting** | MATCH forward; **GAP backward** | The **round-trip is the shape ownership rules exist to prevent**. Sales derives *already-billed* by reading Accounting's stored result rather than consuming a published fact | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-07` | **Purchase → AP / Accounting** | MATCH forward; GAP backward | Same round-trip defect | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-08` | **Payment → Bank / Accounting** | GAP | The Boss-ruled chain is achievable only if one identity is carried on every link, and **the matching state anchoring it is *"freely destructible across a closed period"*** | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-09` | **Asset → Accounting** | **GAP — a consumer is missing** | Capitalization evidenced; **derecognition `PARTIAL`**; the **Equipment consumer has no evidenced route**. Under `P5`, a missing consumer is a defect | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-10` | **Expense → Accounting** | GAP | `AR-18` `PARTIAL` against a terminal `HOLD` in the owning package; petty cash and employee advance both structurally broken | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-11` | **Tax → Accounting / reporting** | GAP | The **substitution rule base is `EVIDENCE-INSUFFICIENT`** — *"a black box in this evidence set"* — a **single point of dependence replicated per Company** under `BD-ACC-02`. **No statutory claim is made** | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-12` | **Close → all subledgers** | GAP | **There is no accounting-period object**, and the accounting date is *"silently movable past a lock"*. The producing side designed a native period guard with **no global bypass** and is waiting for a lock source with no object behind it | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-13` | **Inventory → Sales and Purchase** | MATCH, with a named hazard | Sell-side header progress and transfer status are **independently re-derived** rather than read. Two derivations of one fact can disagree after a partial cancellation, a return or a correction, **and nothing reconciles them** | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-14` | **Quality → Inventory** | MATCH on routing; **GAP on the object** | The **route is Boss-ruled verbatim** and the accounting answer is determinate. **The Quality object itself is absent** — 0 blobs, two shapes, firing positive controls | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-15` | **Quality hold → Accounting** | **NOT APPLICABLE** — internal→internal emits no valuation fact | — | in scope; `N/A` **with reason**, which the approval expressly permits | **`NOT APPLICABLE — EVIDENCE-BACKED`** |
| `XMC-H-16` | **Internal transfer → Accounting** | **NOT APPLICABLE** | — | in scope; `N/A` with reason | **`NOT APPLICABLE — EVIDENCE-BACKED`** — with the caveat at §2.6 |
| `XMC-H-17` | **Service / Project performance → Accounting** | GAP | `BD-ACC-01` presumes a business fact owned by a source module; **for a service there is no physical fact, only an assertion, with no event record**. And the project derivation **writes three costed rows from one duration**, with two report surfaces reading different row sets | out of scope | **`HOLD — EXACT GAP`** |
| `XMC-H-18` | **Migration / replay → Inventory and Accounting** | GAP | **The provenance reference does not exist** (element 14); replay requires *"a stable identity"* (element 15); and **no reconciliation matrix carries this flow at all** (`XMC-F-14`) | **IN SCOPE — tested; 14 and 15 `NOT SUPPLIABLE`** | **`HOLD — EXACT GAP`** |

### 2.6 Detail on the rows that carry the register

**`XMC-H-05` — the only row inside the contract's declared scope.** Elements 1, 3, 5, 6, 7, 11
**supplied**; element 4 a **compliant `N/A` with reason**; 8, 9, 12, 16 **partial**; 10, 13, 14, 15
**absent**. Under the approval's own disposition rule — *"Blank values are not acceptable for material
fields. If a field is not applicable, record `N/A` plus reason. If it is unknown or unsupported,
record `HOLD / EVIDENCE REQUIRED`; do not infer or fabricate"* — the four absent elements are
`HOLD / EVIDENCE REQUIRED`, and §4 states the consequence itself: such a scenario *"remains
`HOLD / EVIDENCE REQUIRED` until resolved or explicitly controlled by Boss decision."*
**`XMC-H-05` is `HOLD — EXACT GAP` by the ruling's own operation, not by this register's judgement.**

**`XMC-H-16` — the `N/A` is evidence-backed and its protection is not.** The determination is primary
and sound: *"A movement between two internal company locations changes where stock is and creates no
accounting consequence."* `SA06-F-05` records that this neutrality *"is protected only by
configuration; no independent check exists"*, and `SA_CORR2_05` §3.1 sharpened it: the same rule makes
a quality hold cost-neutral, so **one unprotected invariant governs two flows.** **This register adds
a third: the same rule is what makes `XMC-H-15` and `XMC-H-16` `N/A` at all.** A configuration change
that breaks transfer neutrality **silently converts two `NOT APPLICABLE — EVIDENCE-BACKED` rows into
ungoverned postings.** The `N/A` is correct today and is **not durable** — and that belongs in the row,
not a footnote.

**`XMC-H-03` — the routing is right and the control floor is wrong, and these are different defects.**
Business Nature says a dropship or subcontract line must route to Purchase. It does. The defect is
that the route **enters Purchase beneath Purchase's own hard gate**. `SA03-F-02`'s determination is
adopted unchanged with its independent rationale intact. **What this register adds:** the control-floor
rule is a **contract clause about routing**, not a control to be added later — stated as `XMC-C-D3`.

---

## 3. The `BD-ACC-01` cross-domain contract, specified

### 3.0 Authority, and what this is not

`BD-ACC-01` **assigns** the canonical Accounting Event Identity to Accounting Core and expressly
leaves the representation to Phase SA. `SA14` §2 puts resolution authority on SMEs Core.
`SA_CORR2_04` §4.3: *"This is not a new Boss question — the ruling exists."*

**Three independent corroborations that no contract has been published**, each from a different party:
`SA_CORR2_06` §6 — *"`BD-ACC-01` already assigns identity ownership to Accounting Core. **Nobody has
published it.**"*; the producing side's `HR-02` states the retry requirement and supplies no carrier;
and the Accounting programme's own central reconciliation pack routes *"Duplicate/replay/idempotency
requirements"* to Phase B marked **`routed, not designed`**, recording *"Every row's delivery status is
`unevidenced`."*

**What follows is at business-semantic level only** — no schema, field list, endpoint, table, key
format, cardinality notation or technology. **`BD-ACC-01` would permit the representation; the CORR3
authority boundary does not, and where the two differ this register takes the narrower.**

### 3.1 Part A — the deterministic Accounting Event Identity

| ID | Clause |
|---|---|
| `XMC-C-A1` | **What an accounting event is.** The Accounting Core's recognition that a business fact owned by a source module has a financial consequence. Not a posting, not a document, not a number, not a report line. A business fact may exist with no accounting event; an accounting event may not exist without a business fact or an assertion under Part C |
| `XMC-C-A2` | **Who assigns identity.** The Accounting Core. The source module never assigns it; the Posting Engine never assigns it. A source module may present a fact repeatedly; it may not present an identity |
| `XMC-C-A3` | **What makes it deterministic.** A function of a declared, immutable **identity basis** and nothing else. Six parts: **tenant**; **company**; **owning source domain**; **business-fact occurrence** as its owner identifies it; the **recognition role** that occurrence bears; and the **policy version in force at recognition**. Same basis in, same identity out — every run, every process, any later date |
| `XMC-C-A4` | **Why the recognition role is in the basis.** One business fact may bear more than one role: a validated outbound movement bears a stock-issue role **and** a cost-of-sales role — two events over one fact. Without the role in the basis, either the two collapse into one identity, or identity must be made unique by something outside the fact, **which is where non-determinism enters** |
| `XMC-C-A5` | **What must not be in the basis.** Wall-clock processing time. Processing actor. Arrival order. Any resettable counter or sequence. Any document number, journal-entry number or reconciliation-matching number. `BD-ACC-01` declares identity *distinct from* those three; **this clause says the stronger thing — such a number may not be an *input* either.** **Live hazard, not precaution:** the Accounting programme records a path that **resets the entry-number sequence to 1, so previously issued numbers can be re-issued.** A basis built on such a number produces two different facts with one identity |
| `XMC-C-A6` | **Retry.** A second presentation of the same basis **is** the same event. The Accounting Core recognises it and does not create a second, and the source module is not required to know it is retrying. `HR-02` restated as an obligation on the party that owns identity rather than an aspiration on the party that does not |
| `XMC-C-A7` | **Replay and migration.** A replayed fact keeps the identity of the fact it replays. Replay-batch provenance travels **beside** the identity, never inside the basis; inside, a replayed fact would acquire a new identity and **replay would become duplication**. **Element 14 is a companion of the identity, not a component** — the semantic reason the approval could make 14 conditional and 10 unconditional |
| `XMC-C-A8` | **Reversal.** A **new** event whose basis includes the identity of the event it reverses, in the reversal role. Never mutation, never deletion. Each discoverable from the other |
| `XMC-C-A9` | **Correction after effect.** The only correction of an event that has taken effect is reversal plus a new event. **Re-dating an existing event is not a correction; an event whose date can move after recognition has not been corrected — it has been altered** |
| `XMC-C-A10` | **Scope, and its consequence.** Identity is Tenant + Company bounded. **It follows that a fact whose company cannot be determined has no identity and cannot be recognised. The contract fails closed.** This is the semantic answer to element 10: it converts an isolation-*proof* obligation into an *interface* obligation the producing side can discharge by carrying the context, **independently of when the invariant set is built and proven** |
| `XMC-C-A11` | **What every consumer may rely on.** (i) Stability under retry, reprocessing, replay, correction and reversal. (ii) Sufficiency to join every downstream artefact of one commercial act, cost half and revenue half included. (iii) A reversal discoverable from its original and vice versa. (iv) The identity does not change when policy changes |
| `XMC-C-A12` | **What no consumer may rely on.** That events arrive in order. That an identity implies a posting occurred. That an identity implies an amount is final. That adjacent identities are related. **Consumers needing ordering must reconcile; they must not infer** |
| `XMC-C-A13` | **Namespace.** Every event identity is qualified by its owning domain; no domain may mint an identifier another could also mint. **Load-bearing:** `BE-14` denotes *"Customer invoice posted"* in one register and *"Unused advance returned in cash"* in another; `RC-01`/`RC-04`/`RC-06` denote Inventory requirements in one package and verification results in another. **Cross-package collision is already present in the corpus at register level; a contract that does not forbid it at event level will reproduce it where it costs more** |

### 3.2 Part B — the customer-invoice lifecycle interface

| ID | Clause |
|---|---|
| `XMC-C-B1` | The Accounting Core **publishes** the lifecycle as named, observable states. Publication means a consumer reads the state as a fact **from its owner** — not by reading the owner's stored result |
| `XMC-C-B2` | Each published state declares four things: what it **consumes**, what it **recognises**, what it **destroys**, and whether it is **reversible**. From the owning `FACT VERIFIED` register: *draft* — consumes billable quantity, recognises nothing, freely deleted; *posted* — recognises revenue, receivable, tax and cost of sales; *reset to draft* — **destroys cost lines**, retains revenue lines; *cancelled* — destroys cost lines; *credit note posted* — reverses revenue, receivable, tax and cost. **Physical return received is a movement, not an invoice state**, and is published as such |
| `XMC-C-B3` | **Matching / reconciliation is a relation, not a state of the invoice**, and is published as a relation. Stated because treating it as a state is what lets a consumer believe it is as durable as the invoice. **It is not** |
| `XMC-C-B4` | **Durability grade.** Every published state carries a declared grade: whether another module may build a **blocking gate** on it. A state that can be silently undone is **not gate-grade**. `C2-F-01` turned from a warning into an interface obligation |
| `XMC-C-B5` | **No round-trip derivation.** A source module does not compute its own state by reading the Accounting Core's stored result. It consumes a published fact. Applies symmetrically to the buy side |
| `XMC-C-B6` | **Every state transition with a financial consequence is itself an accounting event under Part A.** A lifecycle interface publishing states without publishing them as events gives consumers something to read and nothing to join |
| `XMC-C-B7` | **What this interface deliberately does not do.** It does not decide **which** state blocks a sell-side cancellation. That is `XD-01`, normative. **The contract's obligation is to make every candidate state observable and durability-graded so the decision is decidable; taking the decision would be this register answering a reserved question.** Stated in the contract, not only in a covering note |

### 3.3 Part C — the assertion-based event for non-physical performance

| ID | Clause |
|---|---|
| `XMC-C-C1` | **Where performance has no physical movement — a service, a milestone, elapsed time, a re-invoiced expense, a subscription period — the business fact *is* an assertion, and the assertion is the event.** `BD-ACC-01` presumes a fact owned by a source module; here the source module owns an assertion and nothing else. **This clause draws the boundary the ruling did not need when it was written** |
| `XMC-C-C2` | An assertion event carries four things and is invalid without them: **who** asserted, **when**, **on what basis**, and **which obligation** it discharges |
| `XMC-C-C3` | The asserter is an identified person or an identified automatic rule. ***"The system"* is not an asserter.** A rule is an asserter only if its identity **and version** are recorded, **because a rule that changed is a different asserter** |
| `XMC-C-C4` | An assertion is an accounting event under Part A. Re-asserting the same performance is the same event. Withdrawing an assertion is a reversal, never an erasure |
| `XMC-C-C5` | **An assertion is not evidence that performance occurred. It is evidence of who claimed it occurred.** Stated because the evidenced reference records the quantity and not the assertion, so nothing can later show who said the work was done — **and for a service business that record is the only audit trail there is** |
| `XMC-C-C6` | **The symmetry rule.** Every recognition of revenue produces **either** a cost recognition bound to the same identity, **or** an explicit, recorded determination that no cost arises. **Silence is not a permitted answer.** Under this clause a dropship sale can no longer recognise revenue, receivable and tax while its cost lands elsewhere, on another date, joined to nothing |

### 3.4 Part D — cross-cutting clauses from this register's own findings

| ID | Clause |
|---|---|
| `XMC-C-D1` | **Every handoff payload carries the tenant and the company** — not because a proof requires it, but because `XMC-C-A10` makes an event without them unrecognisable. **This closes the *interface* half of element 10, a distinct half from the one the invariant programme is building** |
| `XMC-C-D2` | **Every stated handoff rule has a carrier.** A rule addressed to a receiver with no element capable of satisfying it **is not a rule** |
| `XMC-C-D3` | **A route inherits its destination's entry conditions.** If routing follows Business Nature, a nature routing into a module carries that module's control floor with it; **an automatically created document may not enter beneath a floor a human-created one must clear** |
| `XMC-C-D4` | **A published fact is published once, by its owner.** Where a consumer re-derives a fact the owner also derives, the contract requires one of two things and says which: publish one derived fact and have consumers read it, **or** keep both and publish a reconciliation proving they agree. **Silence between two derivations is not a third option** |

### 3.5 The authority boundary this specification stopped at

**Produced here, inside Phase SA authority:** the meaning of an accounting event; what makes identity
deterministic; the exact composition of and exclusions from the identity basis; behaviour under
retry, replay, correction and reversal; the tenant/company scoping consequence; consumer reliances
and non-reliances; the namespace obligation; the lifecycle as a published, durability-graded
interface; and the assertion event with its four mandatory carriers.

**Deliberately not produced:**

| Not produced | Reason |
|---|---|
| Any representation of an identity — format, generation scheme, length, encoding, uniqueness mechanism | `BD-ACC-01` permits Phase SA to design it. **The CORR3 authority boundary forbids database/API/UI design, and the narrower boundary governs.** A challenger should note this register **declined an authority it was granted**, deliberately |
| Field lists, schemas, endpoints, tables, message shapes | Functional Design and beyond. Not authorized |
| **Which invoice state blocks a sell-side cancellation** | `XD-01`. Normative. **The contract makes it decidable and does not decide it** |
| **Where dropship cost recognition lands, and its date** | `C2-D-02`. Two reference generations are `FACT VERIFIED` and disagree. `XMC-C-C6` forces the question to be *answered*; it does not answer it |
| **Which Product Category governs a kit** | `C2-D-03` — **and see `SA_CORR3_02`, which resolves it by proof; this register's deferral is superseded by that one** |
| **Whether a supplier→customer movement emits two valuation facts or none** | `XMC-D-01`, §4.3 |
| Any statutory Thai position | `HOLD / EVIDENCE REQUIRED`, without exception |
| **Any claim that publishing this closes anything** | §6 |

---

## 4. `CP-SA-C3-60` — Inventory / Manufacturing / Purchase routing

### 4.1 The mandatory routing rules, tested

| Rule | Result |
|---|---|
| Stock-affecting flow → Inventory | **Holds for 18 enumerated flows; the enumeration is short by at least one** (§5.4) |
| Manufacture-required flow → Manufacturing | **Holds as a route; the trigger that *selects* make is undetermined** |
| Procurement-required / dropship → Purchase | **Holds, and the entry is beneath Purchase's control floor** (`XMC-H-03`) |
| Every material business flow → Accounting semantic reconciliation | **29 of 29 have an explicitly determined semantic; 14 carry a named open element** |
| One output may have multiple consumers; a missing consumer is a defect | **One defect found: `XMC-H-09`, Asset → Equipment has no evidenced route** |
| Routing follows Business Nature, not module name | **Holds. The resolution *rule* is still undetermined** |

### 4.2 `XMC-F-03` — dropship *is* answered in the SMEsPlus-owned design, under a vocabulary nobody searched

**Instrument.** PATH SET the 30 blobs of `FINAL_SOLUTION/INVENTORY`; PATTERN `drop.?ship` (-i);
**RESULT 0 blobs, 0 occurrences**, two shapes. Positive controls **inside the same path set**:
`valuation` → **28 of 30**; `direct[- ]?(ship|deliver[a-z]*)|supplier.{0,25}customer` → **3**.
Reachability control: the same pattern over the whole frame → **120 blobs**, so the instrument fires.

And the answer, from `03_INVENTORY_FUNCTIONAL_DESIGN_V1.md` line 126 — the SMEsPlus-owned list of
named templates a Thai SME user chooses per warehouse:

> *"…a one-step, two-step or three-step receipt; a one-step, two-step or three-step delivery; resupply
> from another warehouse; buy-on-reorder-point; make-or-buy on demand; **direct shipment from supplier
> to customer**; and manufacture — and the system resolves the movement chain from that choice."*

> **`XMC-F-03`. That single sentence carries the SMEsPlus-owned routing for `BN-01`, `BN-04`, `BN-05`,
> `BN-06`, `BN-16` and the manufacture natures, and no Phase SA register has read it.** `BN-05`
> dropship has been graded `HOLD` then `PARTIAL` across three rounds on the ground that the routing was
> undetermined. **It is determined, by SMEsPlus, in SMEsPlus's own vocabulary — and the word `dropship`
> appears nowhere in the package that determines it.**

**This is `C2-F-02b` recurring one round after CORR2 named it and prescribed its control.** CORR2's own
prescription was to *"run the instrument against the other party's path set with a positive control
proving it reaches there."* **CORR2 ran that against the Account programme's path set and found the
answer there. It did not run it against the Inventory Final Solution path set, where a second and
different answer was sitting. A control applied to the party you last got caught by is not a control;
it is a patch.**

### 4.3 `XMC-F-04` — the boundary rule that reconciles four Inventory rows has no third case, and dropship is the third case

The rule, primary, from two artefacts:

> *"A movement between two internal company locations changes **where** stock is and creates no
> accounting consequence. A movement crossing the boundary between an internal location and a
> non-internal counterpart — a supplier, a customer, a loss, an adjustment counterpart, production —
> changes **whether** the company owns the stock and therefore emits a valuation fact."*

> *"Movements always have two ends. Where one end is outside the company's stock, SMEsPlus uses a named
> counterpart that never holds real stock: supplier, customer, loss or scrap, adjustment counterpart,
> production counterpart, and in-transit."*

**The rule is stated over exactly two cases, and both presuppose at least one internal end.** A
**direct shipment from supplier to customer has no internal end** — both ends are named counterparts
that never hold real stock.

| Reading | Result | Consequence |
|---|---|---|
| The rule requires an internal end; a movement with none is outside it | **No valuation fact** — revenue, receivable and tax recognised, no cost | **Reproduces exactly the evidenced reference behaviour that `ND-09` was written to decline** |
| *"Crossing to a supplier, customer…"* is satisfied by either end independently | **Two valuation facts** in one movement | A cost and a revenue in the same company on the same act, joinable — **but the company never held the goods** |

> **`XMC-F-04`. `SA_CORR2_05` graded `IR-13` dropship `RECONCILED — AS A MEASURED NEGATIVE` on the
> strength of the reference's behaviour, and grades `IR-09`, `IR-12`, `IR-14` and `IR-17` on the
> strength of this boundary rule. The boundary rule does not decide `IR-13`. The row that most needed
> it is the one case its two clauses do not cover, and no register has noticed because the reference's
> answer and the rule's silence look identical from outside.**

`H-02`'s stated cause — *"the movement exists and the consumer's classification has no category for
it"* — is now located precisely, **and it is located in SMEsPlus's own design, not only in the
reference.** That relocation is why §6 concludes `XD-06` does not close `H-02`: **an event-identity
contract supplies a way to *join* facts; this defect is that the producer cannot decide *whether there
is a fact to emit at all*.**

**`XMC-D-01` — raised to Boss, not decided here.** *Does a direct shipment from supplier to customer
emit two valuation facts, or none — and if none, what discharges `XMC-C-C6`?* **Not research: both
readings are consistent with every fact in the corpus.** A determination with a statutory-adjacent
consequence, because the sell-side leg carries output tax either way.

### 4.4 Inventory reconciliation, carried with its tally corrected

`SA_CORR2_05` §2's 18 rows adopted unchanged (failure containment). Counts re-verified on two shapes
→ **18**.

| Status | Identifiers | Count |
|---|---|---|
| `RECONCILED` | `IR-01`…`IR-14` | **14** |
| `PARTIAL` | `IR-15`, `IR-16`, `IR-17` | **3** |
| `NOT RECONCILED` | `IR-18` | **1** |

**`XMC-F-06`.** §2.1 publishes **14 / 3 / 1** with a correction note recording it *first* published
`13 / 4 / 1`. **Its own checkpoint line still reads `13 of 18 reconciled, 4 partial, 1 not
reconciled`.** The correction was applied to the table and not to the sentence summarising it — **in
the register whose own note explains that this is exactly how such an error survives.**
*(Independently reproduced by two other executors this round: `SA_CORR3_04` `MNT-F-12` and
`SA_CORR3_06` `JCP3-F-07`. Three instruments, three populations, one defect.)*

`XMC-F-04` puts `IR-13`'s `RECONCILED` grade in question on its stated basis. **This register does not
silently re-grade a peer's row:** `IR-13` is carried as published with `XMC-F-04` attached, and the
re-grade is routed to the owning register.

### 4.5 Manufacturing and Purchase legs

| Leg | Position |
|---|---|
| Manufacturing → Inventory | Evidenced. None open at routing level |
| Manufacturing → Accounting | **`GAP`** — fixed-overhead elements with **no injection path**; one variance of nine recognised; WIP recognition timing undecided |
| Purchase → Inventory | Evidenced, **direct and synchronous** — structurally unlike the sell side's indirect path. **The asymmetry is real and uncontracted** |
| Inventory → Purchase | Evidenced, with a **reject-with-reason** obligation. Over-receipt tolerance open; over/under receipt **unguarded, blocked nowhere** |
| Sales → Purchase | The **only** boundary write in the backbone — `XMC-H-03`, clause `XMC-C-D3` |
| Equipment / maintenance → Inventory | A spare-part issue is a movement whose **cost has no destination**. The only `NOT RECONCILED` row. **No statutory conclusion drawn** |

`CP-SA-C3-60` execution position: **the three routings are reconciled at the level of route, and one
route — direct shipment from supplier to customer — has no valuation classification in SMEsPlus's own
rule.**

---

## 5. `CP-SA-C3-70` — Accounting / Tax / Payment convergence

### 5.1 Accounting convergence, carried with its tally corrected

`SA_CORR2_06` §2's 29 rows adopted unchanged; identifier count re-verified → **29**.

| Status | Count |
|---|---|
| `RECONCILED` (including 5 `NO POSTING BY DESIGN`) | **15** |
| `PARTIAL` | **14** |
| `UNKNOWN` / `NOT RECONCILED` | **0** |

**`XMC-F-07`.** §2.1 publishes **15 / 14 / 0** with a note that it first published `16 / 13 / 0`.
**The prose immediately below says *"Thirteen of them have a named open element"*, and the checkpoint
line says *"13 carry a named open element"*.** Enumerating the `PARTIAL` rows gives **14**. **The
corrected figure reached the tally table and neither of the two sentences restating it.** Same defect
as `XMC-F-06`, sibling register, same day, **and it survived the same pre-commit sweep.**

Both are clerical in size and neither changes a conclusion. **Published because a consumer who quotes
the checkpoint line rather than the table inherits a wrong count, and because two independent
occurrences of one defect class in one package is evidence about the control, not about the two
files.**

### 5.2 Tax convergence

| Flow | Status |
|---|---|
| Customer billing → output tax, statutory register | `PARTIAL` — tax arises at **posted**, `FACT VERIFIED` |
| Vendor billing → input tax, withholding | `PARTIAL` — shared determination; **neither commercial module computes tax** |
| **Tax substitution rule base** | **`EVIDENCE-INSUFFICIENT`** — *"a black box in this evidence set"* |
| Cross-company transaction | `RECONCILED — as a ruling`: `BD-ACC-02` forbids cross-company statutory posting, offsetting, settlement, aggregation or filing authority |
| Thai statutory form codes, formats, procedures | **`HOLD / EVIDENCE REQUIRED`** — nine `TH-HOLD-xx` items, **0 consumed by any Phase SA register** |

**No statutory claim of any kind is made by this register.** Under `BD-ACC-02` the determination is
Company-scoped, so the single point of dependence is **replicated per Company** — an architectural
statement about dependence, not about Thai law.

### 5.3 Payment convergence

Boss decision separates Finance, General Ledger and Invoicing and requires mutual traceability:
`BUSINESS DOCUMENT -> ACCOUNTING POSTING -> MONEY SETTLEMENT -> RECONCILIATION -> FINANCIAL REPORT`.

> **The chain has five links and the fifth is anchored on a state the owning programme records as
> freely destructible across a closed period. A chain whose last link can be removed after the fact is
> not traceable end-to-end; it is traceable up to the last durable link, which is the posting.** Under
> `XMC-C-B4` the matching relation is **not gate-grade**, and under `XMC-C-B3` it is published as a
> relation rather than a state — **so a consumer needing settlement durability is told so by the
> interface instead of discovering it.**

Customer receipt and supplier payment `RECONCILED`; advance receipt/payment, payment batch, bank
reconciliation, petty cash and employee advance all `PARTIAL`, the last two **structurally broken**.

### 5.4 `XMC-F-14` — a material flow that no reconciliation matrix carries

**Instrument.** PATTERN `migration|opening balance|cutover` (-i); PATH SET the four reconciliation
matrices `SA06`, `SA07`, `SA_CORR2_05`, `SA_CORR2_06`; UNIT occurrence. **RESULT: 0, 0, 0, 0.**
Positive control: the stem `migration` returns **11 files** across the two Phase SA package
directories, **so the instrument reaches the packages and the zero is specific to the four matrices.**

The flow exists, is material, and **three other instruments carry it**: the producing side publishes
it as three handoff rows including *"certified opening balances, quantity and value, requiring human
certification against the accountant's opening trial balance"*; the Boss contract gives it **element
14**, the one conditional element; and the joint cross-proof carries it as **scenarios 20 and 21**.

> **`XMC-F-14`. The 18-row stock-affecting matrix and the 29-row material-flow matrix are each short by
> at least one flow, and the missing flow is the only one for which a Boss-approved contract element
> was written specifically. The joint cross-proof carries what the convergence matrices that feed it
> omit.**

`IR-18` maintenance was added under the *"every stock-affecting flow"* requirement. **Cutover opening
balance satisfies the same requirement — it increases stock from zero and increases value — and was
not.** Carried here as `XMC-H-18` and **routed to the owning registers rather than inserted into their
tallies.**

`CP-SA-C3-70` execution position: **29 of 29 enumerated material flows have an explicitly determined
accounting semantic; 14 carry a named open element; the enumeration itself is short by at least one.**

---

## 6. What `XD-06` closes — verified one by one

The claim, published twice in identical words: publishing the contract *"is a design act, needs no
Boss decision, and closes `H-01`, `H-02`, `H-03`, handoff element 15, `JCP-03` and `AR-26`."*

**The authority half is verified and holds.** `BD-ACC-01` exists at primary text, assigns identity
ownership, and expressly leaves representation to Phase SA. **Publishing the contract is a design act
and needs no Boss decision. This register acted on it (§3).**

**The closure half, tested against the approval's own three-conjunct standard:**

| Item | Does publishing close it? |
|---|---|
| **`H-01`** | **PARTIALLY, AND ONLY THE HALF THE CONTRACT OWNS.** Part B publishes the interface, so *"no interface publishes it"* is answered at specification level. **The downstream requirement is a *gate*, and which state carries blocking weight is `XD-01`.** `H-01` moves from *"no interface"* to *"interface specified, blocking rule undecided"*. **Not closed** |
| **`H-02`** | **NO, AT ANY STANDARD.** `SA_CORR2_01` §6.1 groups this with `H-01`/`H-03` as a failure of identity. **It is not an identity failure. It is a classification failure**, located by `XMC-F-04` inside SMEsPlus's own boundary rule. **An event-identity contract tells you how to *join* facts; it does not tell a producer *whether a fact exists to emit*.** **Not closed, and not closable by this contract** |
| **`H-03`** | **PARTIALLY.** `XMC-C-A11(ii)` gives the join and `XMC-C-C6` forbids the silence. **Whether the vendor-bill cost *is* the sell-side cost of sales, and at what date, is `C2-D-02`** — two `FACT VERIFIED` generations answer oppositely. **Not closed** |
| **Element 15** | **NO.** Part A specifies the identity, making it **known** and arguably **traceable**, and **not evidence-backed**. Publishing moves element 15 to **`Specified, not built, not verified`** — **word for word the status `SA_CORR2_04` §3 assigns element 10, and on which it declines to call element 10 suppliable. The same standard, applied to element 15, gives the same answer. Not closed** |
| **`JCP-03`** | **THE OWNERSHIP HALF CLOSES; THE SUPPLY HALF DOES NOT.** *"Owned by neither"* ends. Element 15 remains not suppliable. **Narrows from an ownership vacuum to a build obligation. Not closed** |
| **`AR-26`** | **THE BOUNDARY CLOSES; THE ROW DOES NOT.** Part C draws the boundary `BD-ACC-01` did not, which is `C2-F-17`'s actual ask. But `AR-26` is `PARTIAL` because the governing quantity is *"a permanent human assertion, with no independent operational event and no event record"* — **and a specification does not create the record. Not closed** |

### 6.1 `XMC-F-05` — the finding this verification produces

> **Of the six items the claim names, publishing the contract closes `0` at the evidentiary standard
> the contract itself sets, and closes `3` halves at the specification standard — the `H-01` interface
> half, the `JCP-03` ownership half, and the `AR-26` boundary half. `H-02` is closed at no standard,
> because it is not an identity defect. Element 15 is not closed, because closing it by specification
> would require applying to element 15 exactly the standard `SA_CORR2_04` §3 refused to apply to
> element 10, one register earlier, in the same package.**

**Why the claim was made honestly and is still wrong.** Every one of the six has *identity* in its
causal chain, and for five of them identity is genuinely the binding term. The claim then made two
moves invisible from inside: **it read *"a design act needs no Boss decision"* as *"a design act
completes the item"*, and it applied to its own proposal a standard it had just declined to apply to
somebody else's blocker.** That is **self-interested classification** in its exact published form — *a
test that rescues your own proposal is not yours to adopt* — **and adversarial self-review cannot
catch it, because the reviewer shares the proposal.**

**This does not reduce `XD-06`'s value.** It remains the highest-leverage open item and the contract is
specified at §3 because it should be. **What changes is the claim attached to it.** A resume state
saying a single design act closes six items **will cause the next executor to schedule the build behind
a checkbox that has already been ticked.**

**Correct successor statement, replacing the one in the resume state:**

> Publishing the `BD-ACC-01` cross-domain contract is a design act, needs no Boss decision, and is a
> **precondition** for closing `H-01` (with `XD-01`), `H-03` (with `C2-D-02`), element 15, `JCP-03` and
> `AR-26`. It **does not close** any of them, and it does not bear on `H-02`, which requires
> `XMC-D-01` and a third case in the internal / non-internal boundary rule.

---

## 7. Tally, cross-checked against its own rows

| Status | Identifiers | Count |
|---|---|---|
| `PROVEN` | — | **0** |
| `NOT APPLICABLE — EVIDENCE-BACKED` | `XMC-H-15`, `XMC-H-16` | **2** |
| `HOLD — EXACT GAP` | `XMC-H-01`…`14`, `17`, `18` | **16** |
| **Total** | `XMC-H-01`…`XMC-H-18`, each exactly once | **18** |

**Check 1** arithmetic: 0 + 2 + 16 = 18 ✓ · **Check 2** identifier enumeration: 18 distinct, no gap, no
repeat ✓ · **Check 3** — the check an identifier sweep cannot perform: **each row's Status cell
re-read against its class assignment**; only two read `NOT APPLICABLE`, none reads `PROVEN` ✓ ·
**Check 4** scope column: exactly **2** rows `IN SCOPE`, consistent with `XMC-F-12`; both are
`HOLD — EXACT GAP`, and **no out-of-scope row was graded using the 16 elements as a test** ✓

> **`PROVEN` = 0 of 18, and the reason is one clause.** `P6` — the joinable identity — fails on every
> row, because the identity it requires is specified at §3 and does not yet exist. `P2` independently
> fails on every row with an Accounting endpoint. **Two independent universal failures, either of which
> alone produces `0 of 18`. The same arithmetic shape as `JCP-04`: resolving one tomorrow would move
> the result from `0 of 18` to `0 of 18`.**

**Findings raised: 14** (`XMC-F-01`…`XMC-F-14`), each exactly once; 3 evidence-base + 3
contract-content + 2 routing + 2 claim-verification + 4 register-integrity = 14 ✓

Two stated in full here:

**`XMC-F-08` — a roll-up count derivable under neither unit.** The HX register rolls its 31 rows into
four classes summing to **34**. Three rows are deliberately dual-classed, so an overlapping roll-up is
legitimate — **but the unit must then be consistent, and it is not.** `JOINT` names *"HX-08, 09, 10,
15, 16, 17, 22, 24, and the eligibility parts of 14 and 20"*: **8 whole rows under a row unit, 10 items
under a part unit, and the declared figure is 9.** De-duplicated to rows, the four classes cover
14 + 7 + 8 + 2 = **31**, every row exactly once — **which is the reassuring result and the reason the
defect survived: the row-level enumeration is perfect and the published tally is a part-count wrong in
one cell.** `count unit vs population` in its purest form, in the primary source this register
otherwise relies on heavily.

**`XMC-F-09` — cross-package identifier collision is already present**, at register level. Raised
because §3's contract mints event identities, and `XMC-C-A13` exists to stop this recurring **where a
wrong join would be a wrong posting rather than a wrong citation.**

### 7.1 Decisions raised

| ID | Decision | Authority | Why it is not research |
|---|---|---|---|
| `XMC-D-01` | Does a direct shipment from supplier to customer emit **two** valuation facts or **none**, and what discharges `XMC-C-C6` if none? | **Boss** — an accounting-recognition determination with an output-tax consequence | **Both readings are consistent with every fact in the corpus** |
| `XMC-D-02` | Is the 16-element contract **extended** beyond Inventory → Accounting, or does each boundary get its own? | **Boss** — a scope question about a Boss-approved control | The approval's scope is unambiguous at primary text. **Nothing to research; something to decide** |
| `XMC-D-03` | Are `HX-01`…`HX-31` adopted into the Phase SA routing matrix, reconciled against `R-01`…`R-28`, or formally declined with a reason? | PMO, then SMEs Core | The register exists and is published |
| `XMC-D-04` | Do `SA_CORR2_05`/`SA_CORR2_06` add a cutover-opening-balance row, or record its exclusion with an authority? | Owning registers, via PMO | The flow is carried by three other instruments |

---

## 8. Residual uncertainty, proof gaps, and what to attack first

### 8.1 What could not be proven, and the exact gap

| # | Could not prove | Exact gap |
|---|---|---|
| 1 | That **no Accounting-side Final Solution design exists** | §2.2 proves only that no path under `FINAL_SOLUTION` outside `INVENTORY` exists in `CORR3-FRAME`. **A `git log --all --diff-filter=A` over path patterns, or a per-branch lookup, would settle it; neither was run** |
| 2 | That `HX-01`…`HX-31` and `R-01`…`R-28` are **reconcilable** | That is `XMC-D-03`'s work; doing it here would be re-deriving a peer's register rather than reading it |
| 3 | That the contract at §3 is **sufficient** | Sufficiency is provable only against an implementation. `XMC-C-A11`'s reliances are assertions about a thing that does not exist yet |
| 4 | That `XMC-F-02`'s payload map is the **producer's current** position | `V2_0` exists (12 paths) and its functional delta was not read in full. **If `V2_0` adds tenant/company to the payload, `XMC-F-02` narrows to `V1_0` and must say so** |
| 5 | That the two `NOT APPLICABLE` rows are **durably** `N/A` | Their `N/A` rests on a neutrality recorded as configuration-protected with no independent check |
| 6 | Anything about **Thai statutory correctness** | No legal source consulted. `HOLD / EVIDENCE REQUIRED` |

### 8.2 Residual uncertainty carried

`0 of 22` scenarios, `0 of 8` isolation proofs, `0 of 13` enforcement surfaces, `0 of 52` negative
access tests — **nothing here moves any of them, and specifying a contract does not.** Element 10
remains not suppliable for **two independent reasons** now, the second unrecorded until this register
and not closed by it. `XD-01`, `C2-D-02`, `XMC-D-01`, `XMC-D-02` are Boss-reserved and none is answered
here. **`XMC-F-03` does not re-grade `BN-05`; it supplies evidence the owning register should re-grade
on.** Every challenge here is same-model internal self-challenge.

### 8.3 The three claims a challenger should attack first

1. **`XMC-F-05`, the `XD-06` closure verification.** Most leverage, and it rests on one move: that the
   approval's three-conjunct standard applies to element 15 the way `SA_CORR2_04` §3 applied it to
   element 10. **The attack: is that symmetry right?** Element 10's failure is about a *fact about
   deployments*; element 15's is about a *design object*. **A challenger could argue a specification
   genuinely does close a design object in a way it cannot close a deployment fact** — in which case
   §6 weakens from "closes 0 of 6" to "closes 1 or 2 of 6". I believe the symmetry holds because the
   standard is stated once for all sixteen elements with no per-element qualifier — **but I am the
   party whose §3 benefits from being told it closes nothing, and self-abnegation is as self-interested
   as self-promotion.**
2. **`XMC-F-04`, the third-case gap.** Turns on reading two sentences as *presupposing* an internal
   end. **The attack: read the rule again** — *"crossing to a supplier, customer…"* can be read as a
   rule about crossing *to* a named counterpart from anywhere, in which case a supplier→customer
   movement emits two facts and `XMC-D-01` is a reading, not a Boss decision. **I did not open
   `05_INVENTORY_PROCESS_FLOW_CATALOG_V1.md`, and it is the artefact most likely to settle this.**
3. **`XMC-F-02`, the payload map.** Its unit is *"named in the §1.1 payload table"* — an author-chosen
   boundary of exactly the kind this programme keeps getting caught by. **The attack: is §1.1 the
   payload, or a summary of it?** If the emitting contract is §1.1 composed with the movement fact,
   serial and location move to `CARRIED`. **The company/tenant absence survives either reading** —
   neither list contains them — **but the 6/1/1/4/4 breakdown does not.**

---

`CP-SA-C3-50 — execution status.` 18 handoffs carry a contract row; **0 `PROVEN`, 2 `NOT APPLICABLE —
EVIDENCE-BACKED`, 16 `HOLD — EXACT GAP`**, each gap named at the element. The `BD-ACC-01` cross-domain
contract is **specified** at business-semantic level, with its authority boundary stated, and
**specification is not closure of any item it was claimed to close.**

`CP-SA-C3-60` and `CP-SA-C3-70` execution positions at §4.5 and §5.4.

Checkpoint completion is **not** Boss approval. **No PASS is written, recommended or implied anywhere
in this artifact.** Boss remains the sole Final Approver.
