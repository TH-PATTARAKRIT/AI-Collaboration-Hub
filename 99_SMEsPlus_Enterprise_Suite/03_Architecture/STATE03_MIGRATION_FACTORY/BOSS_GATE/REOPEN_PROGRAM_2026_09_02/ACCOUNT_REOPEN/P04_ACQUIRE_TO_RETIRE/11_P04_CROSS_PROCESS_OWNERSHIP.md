# 11 — P04 CROSS-PROCESS OWNERSHIP

Layer: **2 — audit quarantine**.

**ONE BUSINESS FACT → ONE OWNER → ONE ACCOUNTING EFFECT.**

This file applies that rule across the P04 boundaries, and records where the
estate breaks it. Scope columns follow `20_P04_SCOPE_OWNERSHIP_MATRIX.md`.

---

## 1. P01 — Procure-to-Pay

### What crosses, in each direction

| Direction | What crosses |
|-----------|--------------|
| **P01 → P04** | The **posted accounting document** — the only trigger. Its **line**, joined by a relation table. The invoice date, which **derives** the acquisition date. The line label, which **derives** the asset name — and a blank label raises an error. The line quantity, which decides **how many** assets are created. The line's analytic distribution. Non-deductible tax value |
| **P04 → P01** | **Nothing.** No write-back except a message-log note and the back-link. Cancelling the bill attempts to archive derived assets; resetting it to draft deletes derived draft assets |
| **Never crosses** | **Any capital-versus-expense intent expressed on the purchase document.** There is none to cross |

### Ownership rulings

| Business fact | Owner | Ruling |
|---------------|-------|--------|
| "This purchase is a capital item" | **P01 must own it; today nobody does** | The purchase order and receipt carry **no** classification field. The classification is derived downstream from product → category → account, and the capitalization flag sits on the **account**. **The decision is made by an accountant configuring a chart of accounts, months before the purchase.** Registered `P04-B-06` |
| Acquisition cost | **P01 owns the amount; P04 owns its composition** | Today P04 receives the bill line balance and composes nothing. Registered `P04-B-08` |
| Acquisition date | **P04**, derived from the earliest source line's invoice date | Works, but **only while the source-line join survives** |
| Asset identity / name | **P04**, derived from the first source line's label | A weak identity: it is a transaction description, not an asset name |
| The link to the initiating business event | **nobody** | The purchase-order reference lives on the journal item, never on the asset. `P04-B-01` |

> **P04-F-59.** The single most consequential ownership failure at the P01
> boundary is that the **capitalization decision has no owner at the moment it is
> made**. It is pre-committed once per account, applied automatically to every
> qualifying line, and is invisible to everyone who touches the purchase.
> Class: **FACT VERIFIED.**

### Resolution order, recorded so it is not re-derived

Vendor bill line: product property → product-category property, each
company-dependent, mapped through the fiscal position; then, under Anglo-Saxon
accounting for a storable real-time-valued product on a purchase document, the
account is **replaced** by the stock-input account; then fallbacks by partner
history, by the previous two lines, and finally the journal default. The
capitalization test runs **last**, on whatever account that chain produced.

Goods receipt: gated twice — no general-ledger effect at all for
periodic-valuation categories, and none for non-storable products. Where it does
post, **the location's valuation account overrides the product category**.

## 2. P03 — Manufacture-to-Cost

| Direction | What crosses |
|-----------|--------------|
| **P03 → P04** | **Nothing.** No asset reference of any kind in the manufacturing modules |
| **P04 → P03** | **Nothing in the general ledger.** No route feeds a machine's depreciation into the work-centre rate. The rate is a **free-typed float with no computation and no source link** |
| **P04 → P03, analytic** | An asset's distribution reaches the depreciation entry's **two** lines — and, as established, **they cancel** |

| Business fact | Owner | Ruling |
|---------------|-------|--------|
| Machine cost per hour | **P03 owns the rate; P04 owns the depreciation** | **They are not connected.** The rate is typed by a human |
| The machine's identity in costing | **nobody** | The operation references a work centre and nothing else; equipment references a work centre; the asset references neither. `BD-03` vindicated |
| Machine depreciation entering product cost | **contested — nine candidate paths** | See `06` §2. **This is the AAS+ veto's second limb** |
| Which company owns a work centre's financial effect | **unanswerable today** — the work centre is company-optional | `P04-B-35`. **PEER DEPENDENCY OPEN — P03** |

> **P04-F-60.** The rule *one fact → one owner → one effect* is broken at this
> boundary in **both** directions at once: one business fact (an hour of machine
> use) has **up to five** monetisations, and one financial fact (a machine's
> depreciation) has **no** route to the cost it is required by TAS 2 ¶12 to enter.
> Class: **FACT VERIFIED.**

## 3. P08 — Record-to-Report

| Direction | What crosses |
|-----------|--------------|
| **P04 → P08** | Accounting entries carrying an asset reference and a type code — depreciation, sale, purchase, disposal, negative revaluation, positive revaluation. A read-only asset report |
| **P08 → P04** | The company's fiscal lock date, consulted at **exactly three places**; the generic auto-posting scheduled action; the company's fiscal-year boundaries, used to align periods |
| **Never crosses** | **Any close-driven asset recomputation, revaluation or freeze.** There is no asset-specific close step and no profit-and-loss year-close entry at all |

### The headline

> **P04-F-61.** A depreciation entry aimed at a **locked** period is **silently
> re-dated forward**, not rejected. The posting routine computes the violated
> lock dates and **mutates the entry's date** to the accounting date derived from
> the last violated lock — the lock date plus one day, rolled to the end of that
> period. The subsequent lock check then passes, because the date has already
> changed. The violated-lock lookup is called with the hard flag set, so the
> **hard lock is covered too**.
>
> **Citation, given precisely because it was challenged.** The estate's own test
> `test_post_moves_after_lock_date`, in the asset module's board-computation test
> file, sets a fiscal-year lock of **30 June 2021** and confirms an asset whose
> board carries a **31 December 2020** entry of 12 000. It asserts that entry
> posts as **31 July 2021** — a **seven-month** shift, into the **following**
> fiscal year, **carrying its full 12 000**.
>
> An independent review challenged this citation as non-existent, having searched
> only the module's main test file. The test is in the **board-computation** test
> file. The challenge was **not sustained**; the citation is now given by test
> name and file so it is verifiable without repeating the search. See `18`
> `P04-REV-11`.
> Class: **FACT VERIFIED.** Severity **High.** Registered `P04-B-31`.

Contrast: **disposal is hard-blocked** by the same lock date, with an explicit
error. So one asset operation is refused at the lock and another is silently
re-dated.

**Stated correctly after independent challenge:** the two behaviours do **not**
sit in one module. The hard refusal is asset-module code. The silent re-dating is
the **accounting core's generic posting routine**, and therefore applies to
**every programmatically posted entry in the product** — depreciation, disposal,
inventory valuation, manufacturing relief and time-based recognition alike. The
finding is not an asset-domain quirk; it is a core behaviour that the asset
domain merely makes visible. **Owner: P08.**

| Business fact | Owner | Ruling |
|---------------|-------|--------|
| Which period a depreciation charge belongs to | **P04 computes it; P08 may silently overwrite it** | **Two owners for one fact.** The rule is broken |
| Whether a period is closed | **P08** | Correct — but P04 honours it in only three of its paths |
| Sub-ledger to ledger agreement | **nobody** | `P04-B-17` |
| Tax written-down value | **nobody — no tax book exists** | `P04-B-13`, re-opened after falling out of the registers |

## 4. P09 — Plan-to-Analyze

| Direction | What crosses |
|-----------|--------------|
| **P04 → P09** | The asset's distribution onto **both** lines of every depreciation entry, or onto neither; onto disposal entry lines; and thence into analytic lines that **net to zero** |
| **P09 → P04** | Only the bill line's distribution at creation, and the asset model's distribution. **No plan applicability, no mandatory check, and no account-prefix distribution rule reaches the asset** |

| Business fact | Owner | Ruling |
|---------------|-------|--------|
| Which cost centre bears a depreciation charge | **P04 owns the distribution; P09 owns the plan** | The asset **never consults** the account-prefix rules that govern every manual journal item. A rule an accountant believes is universal is **invisible to assets** |
| Enforcement that a charge is attributed | **nobody** | Mandatory plans **do not fire** on any programmatic posting, and depreciation entries would be skipped anyway. `P04-F-52` |
| Attribution of a **capitalized addition** | **nobody** | Neither the entry nor the child asset carries a distribution. `P04-F-53` |
| A project's asset count | P09, read-only | Counts assets whose distribution mentions the project's analytic account. An asset split across two projects is counted **under both** — it is a count, not a partition. Harmless for reporting, misleading for attribution |

**Scope note.** Under the corrected constitution the **plan** is a tenant
candidate and the **distributed amount** is a company financial fact. Relying on
a tenant-scoped structure to enforce a company-scoped requirement (`BD-02`) is a
scope mismatch in the design intention. `P04-F-57`.
**PEER DEPENDENCY OPEN — P09.**

## 5. P10 — Time-Based Recognition

**The engines are separate.** Confirmed at model level: no shared model, no
shared method, no shared settings.

| Difference | Asset engine | Deferred engine |
|------------|--------------|-----------------|
| Contra account | **per asset** | **one pair, company-wide** |
| Journal | per asset | one per company, per direction |
| Period alignment | month **or fiscal year** | **calendar month only** |
| Day-count | its own 30/360 implementation, with a calendar alternative | **a second, independently written 30/360 implementation** |
| Method | linear, degressive, degressive-then-linear | pro-rata only |
| Entry shape | one two-line entry per period | one full-reversal entry **plus** one per period |
| Currency | full conversion at the entry date | company currency only — **no currency handling found** |

| Business fact | Owner | Ruling |
|---------------|-------|--------|
| Spreading a cost over time | **two owners, two engines** | A statutory day-count requirement must be implemented **twice**, or the two schedules diverge |
| A depreciation-expense account | **both** | That account type is a **permitted deferral target**. An account can be the destination of an asset schedule **and** the source of a deferral schedule, with **no cross-check** |

> **P04-F-62.** The automatic capitalization path is reachable **only from
> purchase-type documents** — the sale-side exclusion cancels every sale document
> that would otherwise qualify. Any P10 design expecting to drive deferred
> **revenue** through the asset engine is designing against a path that **does
> not execute**.
> Class: **FACT VERIFIED.**

**Shared exposure.** Both engines are triggered from the same posting routine and
posted by the same scheduled action — so **both** are subject to the silent
lock-date re-dating of §3.

## 6. Cross-process publication actually performed

The correction requires P11 to reconcile scope semantics across P01–P10
**continuously**. P01 through P11 were confirmed to be executing **concurrently**
at the time of this session. Rather than record dependencies and leave them
undiscovered, P04 published its findings to the owning sessions directly.

| Sent to | Content |
|---------|---------|
| **P11** | Both unresolved scope questions (`P04-SC-03`, `P04-SC-04`); the narrowing of the prior company-optional finding and the test applied to it; all seven cross-process findings; and the handover-residue governance item with a recommended carry-forward rule |
| **P08** | The silent lock-date re-dating, with its mechanism, the estate's own test result, its extension to the hard lock and to time-based recognition entries, and the contrast with the hard-refused disposal. Plus: no year-close entry exists; no sub-ledger reconciliation exists; and the **tax book** gap re-opened as `P04-B-13` with P08 named as owner |
| **P09** | The analytic cancellation, the divergent-distribution residue, the non-enforcement of mandatory plans on every programmatic post, the un-attributed capitalized addition, and the plan-versus-amount scope split (`P04-PD-04`) |
| **P03** | The nine-path enumeration with its declared unit **and its honest caveat**, the standard-costing ledger mismatch, the three further reconciliation failures, the re-verified operation-to-equipment gap, and the work-centre scope defect assigned to them (`P04-B-35`, `P04-PD-01`) |
| **P07** | All five statutory sources retrieved this session, with the classification discipline attached — so the retrieval is not duplicated — and the three tax questions routed to them (`P04-B-24`, `P04-B-39`, `P04-B-25`), plus the unresearched borrowing-cost item (`P04-B-05`) |

This is publication, **not** agreement. Every ownership ruling in §1–§5 that
assigns a fact to another process remains **provisional on that process's own
determination**, and no peer dependency was treated as closed by having been
communicated.

## 7. Peer dependencies

| ID | Dependency | Owner | Status |
|----|-----------|-------|--------|
| **P04-PD-01** | Work-centre scope and company ownership | P03 | **OPEN** |
| **P04-PD-02** | May a company hierarchy span tenants | P11 | **OPEN** |
| **P04-PD-03** | May one tenant hold unrelated companies | P11 | **OPEN** |
| **P04-PD-04** | Analytic plan scope | P09 | **OPEN** |
| **P04-PD-05** | Chart-of-accounts scope for the capitalization designation | P08 | **OPEN** |
| **P04-PD-06** | Ownership of the capital-versus-expense classification on the purchase document | P01 | **OPEN** |
| **P04-PD-07** | Which single mechanism carries machine cost into product cost | P03 | **OPEN — the AAS+ veto's second limb** |
| **P04-PD-08** | Lock-date policy: refuse versus re-date | P08 | **OPEN** |

**P01, P02 and P03 sessions for this wave had not published at the time of this
session's execution.** Every ownership ruling above that assigns a fact to
another process is therefore **provisional on that process's own determination**,
and is recorded as a peer dependency rather than as an agreement. Per the
cross-process rule, this session did **not** stop for any of them.
