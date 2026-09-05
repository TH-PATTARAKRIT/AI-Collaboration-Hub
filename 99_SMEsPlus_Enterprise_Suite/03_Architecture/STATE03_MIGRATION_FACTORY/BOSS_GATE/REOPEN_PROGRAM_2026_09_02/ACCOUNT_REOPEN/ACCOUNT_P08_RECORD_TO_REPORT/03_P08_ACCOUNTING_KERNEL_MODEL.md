# P08_ACCOUNTING_KERNEL_MODEL — What the accounting source of truth is

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 (clean-room) · scope model per `SMEPLUS-26-09-04-ACC-REV2-CORR1`

This file answers the session's critical question and fixes the boundaries between the eight layers named in the process directive.

---

## 1. The question, stated precisely

> `SOURCE BUSINESS DOCUMENT` → `ACCOUNTING EVENT` → `POSTING INSTRUCTION` → `JOURNAL ENTRY` → `JOURNAL ITEM` → `SUBLEDGER` → `GENERAL LEDGER` → `FINANCIAL REPORT`
>
> Which of these holds original truth, which holds derived truth, and where does the boundary move under manual journals?

Answering it requires separating three things that the benchmark fuses: what a layer **is**, what a layer **stores**, and what a layer is **allowed to assert**.

## 2. The benchmark's answer, established by evidence

### 2.1 Five of the eight layers do not exist as objects

| Layer | Exists as a persisted object in the benchmark? | Evidence class |
|---|---|---|
| Source business document | **Yes**, in each producing process | FACT VERIFIED |
| Accounting event | **Partly — CORRECTED** | **A VERIFIED ABSENCE** — scope: all 1 533 distinct model names declared across the 790 modules of the target root; **39** contain the word *event*, of which **36 belong to the event-management domain and 3 do not** — a calendar appointment, its type, and a barcode-scanning mixin. **None of the 39 is an accounting construct.** *(Corrected after independent review: the draft said "all 39 belong to the event-management domain", which is false. The conclusion is unaffected; the evidence line was wrong, in the sentence underpinning the package's most load-bearing absence.)* |
| Posting instruction | **No** — it is a transient structure built inside each producer's posting routine and discarded | **B NOT FOUND IN SEARCHED SCOPE** *(downgraded after independent review: the scope quoted was a model-name census on the token "event", which is orthogonal to a posting-instruction object. No pattern capable of falsifying this claim has been declared, so it may not carry class A.)* |
| Journal entry | **Yes** | FACT VERIFIED |
| Journal item | **Yes** | FACT VERIFIED |
| Subledger | **No** — it is a query over journal items net of matching links | A VERIFIED ABSENCE, scope: every model whose name contains *reconcile* (7, of which 2 are state and 5 are configuration or transient) plus the four report engines that produce partner open-item output |
| General ledger | **No separate store** — it is the same journal-item table read differently | FACT VERIFIED |
| Financial report | **Partly** — the *definitions* are stored, the *figures* are recomputed, and a **third store holds figures that are not derived from journal items at all** | FACT VERIFIED |

### 2.2 The consequence

`KRN-01` — **The journal item is the only durable accounting fact *in the ledger*.** Everything above it in the chain is transient; the partner subledger and the general ledger below it are projections. **Corrected after independent review, which found the accepted peer correction `REV-P-02` had not been propagated here:** the statement does **not** hold across the wider system — the **fixed-asset register and the inventory valuation record are genuine separate stores** carrying independently maintained values, and nothing reconciles either to the ledger. See `KRN-05a`. `FACT VERIFIED` as re-worded.

`KRN-02` — **The journal entry is the accounting representation of an accounting event, and it is also the event's only record.** There is no object behind it. `FACT VERIFIED`. Prior Wave A reached this conclusion on a narrower search; P08 reproduces it at full model-population scope, which upgrades its evidential standing without changing its content.

`KRN-03` — **The general ledger is not a store; it is a reading.** The trial balance, general ledger and partner ledger are three groupings of one table. There is no posting from a subledger into a ledger, because there is no subledger to post from. `FACT VERIFIED`.

`KRN-04` — **The financial report layer holds independent truth.** Three stores exist whose values are not derived from journal items: externally supplied values, values entered by hand directly on a statement cell, and values carried forward and materialised at close. A cell fed from any of them reports a number that no posting supports, and no ledger control reaches it. `FACT VERIFIED`.

`KRN-05` — **RESTATED AT THE CORRECT LAYER after independent review.** The draft answered "the general ledger is original truth, and the report is derived truth except where it is not". That is incoherent against this file's own `KRN-03`: a reading cannot hold original truth. The corrected answer:

> **The journal item is both original and derived truth, and nothing marks which.** The general ledger is **uniformly derived** — it is a reading of the items with no independent content. The report layer holds **three further independent truth bearers** (externally supplied values, hand-entered statement values, carried-forward values materialised at close), and its **definition is a fourth**: the formulas are retroactively editable by one ordinary role with no change history, so the definition determines the reported figure independently of any fact.

**There are therefore at least four independent truth bearers in the benchmark, not two**, and the binary framing of the draft understated the package's own evidence.

## 3. Where original truth actually sits, layer by layer

| Layer | Truth status in the benchmark | Why |
|---|---|---|
| Source business document | **Original truth about the business event** | It records what was agreed, delivered, invoiced or paid |
| Accounting event | **Absent** — the assertion "this business fact has an accounting consequence" has no carrier | Nothing records that the consequence was recognised, when, by what rule, or under what version of that rule |
| Posting instruction | **Absent** — the rule that mapped the business fact to accounts is not preserved | Two entries produced by different versions of the same rule are indistinguishable afterwards |
| Journal entry | **Original truth about the accounting effect**, and simultaneously the *only* record of the event | The fusion is the finding: correcting the event and editing its representation are the same operation |
| Journal item | **Original truth about the financial fact** | Amount, account, party, date, currency — all stored here and nowhere else |
| Subledger | **Derived** — and derived from *two* inputs, not one | Amounts derive from journal items net of matching links; and the party attribution of an unattributed line is supplied by the matching link itself |
| General ledger | **Derived presentation of the journal items** | No independent content |
| Financial report | **Derived, plus three independent stores** | See `KRN-04` |

`KRN-05a` — **CORRECTED after an inbound peer finding (P04).** The statement "there is no subledger, only a projection" is too broad and is narrowed here. It holds for the **partner** subledger. It does **not** hold for the **fixed-asset register** or the **inventory valuation record**, which are genuine separate stores carrying independently maintained values. For those, the kernel imposes **no reconciliation obligation at all** — no control-account relationship, no periodic proof, no exception when the two disagree. That is a gap in the kernel, not in the producing module, and P08 owns it. New requirement `P08-RQ-KRN-01`. The absence of a reconciliation mechanism is class `C NOT YET SEARCHED` for P08's own scope; see `09A`.

`KRN-05b` — **The kernel carries one measurement basis per fact.** A second statutory or tax basis over the same events is not expressible without duplicating the ledger. New requirement `P08-RQ-KRN-02`; new decision `P08-BD-11`. See `09A` §5.

`KRN-06` — **The partner subledger is a projection of journal items *and the matching graph*.** This is stronger than "the subledger is derived". A line posted without a counterparty is attributed to a counterparty *because it was matched*; un-matching removes it from that party's statement. The matching graph is therefore not a settlement artefact sitting beside the ledger — it is load-bearing for the ledger's own party dimension. `FACT VERIFIED`.

## 4. Manual journals — where the boundary moves

The directive asks specifically whether the general ledger is original truth, derived truth, or both under controlled manual-journal scenarios. The evidence gives a definite answer.

`KRN-07` — **Under a document-generated entry, the general ledger is derived truth with a recoverable origin.** The entry carries a link back to its source document, and the producing module can in principle re-derive it.

`KRN-08` — **Under a manual journal, the general ledger is original truth with no origin at all.** A manual entry has no source document, no producing rule, and no event behind it. It is the first and only assertion of the fact.

`KRN-09` — **The two are indistinguishable after the fact by any structural property.** There is no field that says "this entry was derived" versus "this entry was asserted". A manual entry can target any account, including a subsidiary-ledger control account, because the constraints that keep control accounts aligned to their subsidiary ledgers are gated on the entry being a customer or supplier document — and a manual entry is neither, so both branches are skipped. `FACT VERIFIED`, independently reproduced by this session.

`KRN-10` — **Provenance of a document-generated entry can be destroyed by ordinary operations.** Resetting a posted entry to draft silently deletes its cost-allocation lines and removes every settlement match it participated in; re-dating utilities in the custom layer discard the entry's number entirely and re-post it under a new one. Neither operation records what was destroyed as a ledger fact. `FACT VERIFIED`.

**Answer to the directive's question:** the general ledger is **both**, and nothing in the benchmark marks which. That is the defect — not that manual journals exist, but that the ledger cannot say of any given fact whether it is a derivation or an assertion.

## 5. The kernel model P08 proposes for SMEsPlus

`DESIGN CANDIDATE` throughout. No implementation authority. Scope labels per the corrected scope model.

### 5.1 Nine objects, of which the benchmark has four

| # | Object | Scope | Mutable after commitment? | Present in benchmark? |
|---|---|---|---|---|
| `K1` | **Business fact** — what happened, owned by the producing process | `COMPANY` | by its own process, before recognition | yes |
| `K2` | **Accounting event** — the assertion that `K1` has an accounting consequence, carrying event identity, recognition point, the rule version applied, and the actor | `COMPANY` | **never** | **partly — for externally-originated events only.** Database-enforced identity bound 1:1 to the entry exists for bank file import, payment-provider transactions and e-invoicing dispatch; nothing equivalent exists for any internally-originated path. See `39` |
| `K3` | **Posting instruction** — the mapping `K2` → accounts and amounts, as evaluated, retained | `COMPANY` | **never** | **no** |
| `K4` | **Journal entry** — the balanced set of financial facts realising `K3` | `COMPANY` | **never** once posted | yes |
| `K5` | **Financial fact (journal item)** — one signed amount on one account, in one currency, with its measurement context | `COMPANY` | **never** once posted | yes |
| `K6` | **Settlement fact** — a matching link between financial facts, with its own event date | `COMPANY` | **never**; undone only by a new settlement fact | partly — the link exists, the event date does not |
| `K7` | **Finality declaration** — the assertion that a period is closed, as an object | `COMPANY` | forward only | **no** — it is a bare date |
| `K8` | **Period** — the object the finality declaration attaches to, carrying state | `COMPANY` | state transitions only | **no** |
| `K9` | **Issued statement** — the fact that a statement was produced, for a company, for a period, from a named definition version against a named data state | `COMPANY` | **never** | **no** |

**`K8` and `K9` were added after independent review.** `06` §5 already required both in the mandated trace, and `09`/`11` already carried requirements that depend on them, while the object list stopped at seven — four published files required objects the design deliverable did not define.

### 5.2 The five invariants that follow

`KRN-INV-00` — **THE ACCOUNTING IDENTITY.** The `K5` items of a `K4` sum to zero, **in every currency frame the entry uses**, enforced at the persistence layer, with no caller-supplied waiver and no configuration that disables it.

**Added after independent review.** The draft's invariant set omitted the double-entry identity entirely, while the same package called its absence "the single most important requirement" and "the most severe finding". A kernel that does not state the invariant it exists to protect cannot be handed to anyone. It is numbered `00` because it precedes all the others.

`KRN-INV-01` — **ONE FACT → ONE ACCOUNTING EFFECT.** Stated as **two** constraints, because the draft's single constraint did not deliver the capability it was sold on:
- **`01a` (`K1`→`K2`):** a `K2` is uniquely determined by `(K1, posting rule, recognition point)`. A second attempt to assert the same accounting consequence for the same business fact is **refused on collision**, not recorded as a second event. This is the idempotency key, and it is where duplicate detection actually lives.
- **`01b` (`K2`→`K4`):** every `K4` names exactly one `K2`, and every `K2` produces at most one `K4` per company.

**Corrected after independent review.** The draft stated only `01b` and then claimed duplicate detection as a capability. `01b` alone does not deliver it: two postings of one business fact create two `K2`s and two lawful `K4`s and the invariant is satisfied. `06` §5 also placed the invariant at the second node while `03` placed it on the third-to-fourth arrow; `01a`/`01b` resolves that disagreement by stating both.

**`KRN-INV-01` exception, stated explicitly.** Two posting classes have no `K1` behind them and are **not** defects: an **opening-balance declaration** and a **restatement**. Each is admitted as a `K2` whose origin is a declaration rather than a business fact, and each must name its authority, its date and its basis. Without this exception the kernel as drafted forbade migration entirely — which this package's own business-event register requires. A **reversal** is a `K2` in its own right, linked to the `K2` it reverses; that is what makes `KRN-INV-04` (correction by new fact) coherent rather than circular.

`KRN-INV-02` — **A posted financial fact is immutable, and immutability is a property of the persistence layer, not of a code path.** The benchmark's balance assertion, posted-record protection, deletion guards and tamper seal are all application-layer checks, and three of the four are suppressible by a request parameter supplied by the caller.

`KRN-INV-03` — **Every posted fact carries its own provenance: the event, the instruction, the actor, the measurement context, and the tenant and company that own it.** Absent in the benchmark; `K2`, `K3` and the measurement context each supply one part of it.

`KRN-INV-04` — **Correction is by new fact only.** The benchmark already demonstrates the pattern in one place — its period-transfer and account-transfer routines generate new posted entries, reconcile them against the originals, and annotate both sides, leaving the originals untouched. That pattern is the model; the destructive paths beside it are not.

`KRN-INV-05` — **A tenant-scope mutation may never rewrite a company-scope posted fact, and may never silently change a company-scope issued statement.** Either requires an explicit, auditable company-scope restatement fact.

**Restated after independent review.** The draft covered only posted facts. That wording permits the two most consequential restatement routes this package itself established, because neither touches a posted fact: retroactive re-classification of an account, and retroactive edit of a statement's own formulas — both tenant-scope objects rewriting a **derivation input**. It also failed to cover an account-flag change that rewrites stored open amounts by direct database statement. The invariant is the one this session offers P11 as its most transferable output, and it must not travel in the under-stated form.

`KRN-INV-06` — **Every subsidiary store that carries an independently maintained value has a stated control-account relationship and a periodic proof that the two agree; the failure of that proof is itself an accounting event.** (`P08-RQ-KRN-01`.)

`KRN-INV-07` — **A financial fact carries its measurement basis, and the kernel supports more than one basis over one set of accounting events without duplicating the events.** (`P08-RQ-KRN-02`.)

`KRN-INV-08` — **Every object with a financial effect has exactly one owning company. Where ownership cannot be proven, the operation is denied.**

**Added after independent review**: the handoff pack was carrying this forward as a sixth invariant to Core Reconciliation while the kernel model declared only five. A downstream reader taking the two documents together received two different invariant sets.

### 5.3 What this makes possible that the benchmark cannot do

| Capability | Requires |
|---|---|
| Detect that one business fact was posted twice | `K2` **and `KRN-INV-01a`** — `K2` alone is not enough |
| Explain why an entry says what it says, years later | `K3` |
| Re-run a prior period's statement and get the same answer | `K7` plus `KRN-INV-02` |
| Prove the ledger from stored data without trusting the code that wrote it | `KRN-INV-00` and `KRN-INV-02`, both at persistence level |
| Distinguish a derived entry from an asserted one | `K2` presence or absence |
| Prove the fixed-asset register agrees with the ledger | `KRN-INV-06` |
| Produce a tax position without a second ledger | `KRN-INV-07` |
| Reopen a period and know what was issued before the reopen | `K8` and `K9` |

## 6. Classification summary

| Statement | Class |
|---|---|
| The journal item is the only durable accounting fact **in the ledger**; genuine separate subsidiary stores exist outside it | `FACT VERIFIED` as re-worded — the unqualified form was `CONTRADICTED` by the P04 peer finding and is withdrawn |
| No accounting-event object exists | `A VERIFIED ABSENCE`, scope stated in §2.1 |
| No posting-instruction object exists | `A VERIFIED ABSENCE`, same scope |
| The subledger is a projection of items **and** the matching graph | `FACT VERIFIED` |
| The report layer holds three independent value stores | `FACT VERIFIED` |
| The general ledger is both original and derived truth, unmarked | `SUPPORTED INTERPRETATION` built on the four facts above |
| The nine-object kernel `K1`..`K9` | `DESIGN CANDIDATE` |
| Whether SMEsPlus adopts `K2`/`K3` as stored objects or as an append-only log | `BOSS CONTROLLED DECISION` `P08-BD-04` |
