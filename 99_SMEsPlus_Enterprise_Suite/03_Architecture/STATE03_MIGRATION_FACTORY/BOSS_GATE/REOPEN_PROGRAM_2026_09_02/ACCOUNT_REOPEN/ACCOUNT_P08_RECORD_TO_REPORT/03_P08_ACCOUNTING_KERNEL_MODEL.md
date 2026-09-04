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
| Accounting event | **No** | **A VERIFIED ABSENCE** — scope: all 1 533 distinct model names declared across the 790 modules of the reference build; 39 contain the word *event* and all 39 belong to the event-management (marketing) domain |
| Posting instruction | **No** — it is a transient dictionary built inside each producer's posting method and discarded | A VERIFIED ABSENCE within the same scope |
| Journal entry | **Yes** | FACT VERIFIED |
| Journal item | **Yes** | FACT VERIFIED |
| Subledger | **No** — it is a query over journal items net of matching links | A VERIFIED ABSENCE, scope: every model whose name contains *reconcile* (7, of which 2 are state and 5 are configuration or transient) plus the four report engines that produce partner open-item output |
| General ledger | **No separate store** — it is the same journal-item table read differently | FACT VERIFIED |
| Financial report | **Partly** — the *definitions* are stored, the *figures* are recomputed, and a **third store holds figures that are not derived from journal items at all** | FACT VERIFIED |

### 2.2 The consequence

`KRN-01` — **The journal item is the only durable accounting fact in the benchmark.** Everything above it in the chain is transient; everything below it is a projection. `FACT VERIFIED`.

`KRN-02` — **The journal entry is the accounting representation of an accounting event, and it is also the event's only record.** There is no object behind it. `FACT VERIFIED`. Prior Wave A reached this conclusion on a narrower search; P08 reproduces it at full model-population scope, which upgrades its evidential standing without changing its content.

`KRN-03` — **The general ledger is not a store; it is a reading.** The trial balance, general ledger and partner ledger are three groupings of one table. There is no posting from a subledger into a ledger, because there is no subledger to post from. `FACT VERIFIED`.

`KRN-04` — **The financial report layer holds independent truth.** Three stores exist whose values are not derived from journal items: externally supplied values, values entered by hand directly on a statement cell, and values carried forward and materialised at close. A cell fed from any of them reports a number that no posting supports, and no ledger control reaches it. `FACT VERIFIED`.

`KRN-05` — **Therefore the benchmark's answer to the critical question is: the general ledger is original truth, and the financial report is derived truth *except* where it is not.** The exception is not marginal. It is a designed feature with its own store, its own edit action, and a manager-level permission with no change history.

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

### 5.1 Seven objects, of which the benchmark has four

| # | Object | Scope | Mutable after commitment? | Present in benchmark? |
|---|---|---|---|---|
| `K1` | **Business fact** — what happened, owned by the producing process | `COMPANY` | by its own process, before recognition | yes |
| `K2` | **Accounting event** — the assertion that `K1` has an accounting consequence, carrying event identity, recognition point, the rule version applied, and the actor | `COMPANY` | **never** | **no** |
| `K3` | **Posting instruction** — the mapping `K2` → accounts and amounts, as evaluated, retained | `COMPANY` | **never** | **no** |
| `K4` | **Journal entry** — the balanced set of financial facts realising `K3` | `COMPANY` | **never** once posted | yes |
| `K5` | **Financial fact (journal item)** — one signed amount on one account, in one currency, with its measurement context | `COMPANY` | **never** once posted | yes |
| `K6` | **Settlement fact** — a matching link between financial facts, with its own event date | `COMPANY` | **never**; undone only by a new settlement fact | partly — the link exists, the event date does not |
| `K7` | **Finality declaration** — the assertion that a period is closed, as an object | `COMPANY` | forward only | **no** — it is a bare date |

### 5.2 The five invariants that follow

`KRN-INV-01` — **ONE FACT → ONE ACCOUNTING EFFECT.** Every `K4` names exactly one `K2`, and every `K2` may produce at most one `K4` per company. This is the invariant the directive names, and it is unenforceable without `K2`, because there is nothing to be *one* of. In the benchmark, the same business fact posted twice yields two equally valid entries and nothing detects it.

`KRN-INV-02` — **A posted financial fact is immutable, and immutability is a property of the persistence layer, not of a code path.** The benchmark's balance assertion, posted-record protection, deletion guards and tamper seal are all application-layer checks, and three of the four are suppressible by a request parameter supplied by the caller.

`KRN-INV-03` — **Every posted fact carries its own provenance: the event, the instruction, the actor, the measurement context, and the tenant and company that own it.** Absent in the benchmark; `K2`, `K3` and the measurement context each supply one part of it.

`KRN-INV-04` — **Correction is by new fact only.** The benchmark already demonstrates the pattern in one place — its period-transfer and account-transfer routines generate new posted entries, reconcile them against the originals, and annotate both sides, leaving the originals untouched. That pattern is the model; the destructive paths beside it are not.

`KRN-INV-05` — **A tenant-scope mutation may never rewrite a company-scope posted fact.** It may only add a new company-scope fact. This is the general form of the counterparty reach-through recorded in `P08_SCOPE_OWNERSHIP_MATRIX.md` §2.7 and is the rule that would have prevented it.

`KRN-INV-06` — **Every subsidiary store that carries an independently maintained value has a stated control-account relationship and a periodic proof that the two agree; the failure of that proof is itself an accounting event.** (`P08-RQ-KRN-01`.)

`KRN-INV-07` — **A financial fact carries its measurement basis, and the kernel supports more than one basis over one set of accounting events without duplicating the events.** (`P08-RQ-KRN-02`.)

### 5.3 What this makes possible that the benchmark cannot do

| Capability | Requires |
|---|---|
| Detect that one business fact was posted twice | `K2` |
| Explain why an entry says what it says, years later | `K3` |
| Re-run a prior period's statement and get the same answer | `K7` plus `KRN-INV-02` |
| Prove the ledger from stored data without trusting the code that wrote it | `KRN-INV-02` at persistence level |
| Distinguish a derived entry from an asserted one | `K2` presence or absence |
| Prove the fixed-asset register agrees with the ledger | `KRN-INV-06` |
| Produce a tax position without a second ledger | `KRN-INV-07` |
| Reopen a period and know what was issued before the reopen | `K7` as an object, plus statement issuance as a fact |

## 6. Classification summary

| Statement | Class |
|---|---|
| The journal item is the only durable accounting fact in the benchmark | `FACT VERIFIED` |
| No accounting-event object exists | `A VERIFIED ABSENCE`, scope stated in §2.1 |
| No posting-instruction object exists | `A VERIFIED ABSENCE`, same scope |
| The subledger is a projection of items **and** the matching graph | `FACT VERIFIED` |
| The report layer holds three independent value stores | `FACT VERIFIED` |
| The general ledger is both original and derived truth, unmarked | `SUPPORTED INTERPRETATION` built on the four facts above |
| The seven-object kernel `K1`..`K7` | `DESIGN CANDIDATE` |
| Whether SMEsPlus adopts `K2`/`K3` as stored objects or as an append-only log | `BOSS CONTROLLED DECISION` `P08-BD-04` |
