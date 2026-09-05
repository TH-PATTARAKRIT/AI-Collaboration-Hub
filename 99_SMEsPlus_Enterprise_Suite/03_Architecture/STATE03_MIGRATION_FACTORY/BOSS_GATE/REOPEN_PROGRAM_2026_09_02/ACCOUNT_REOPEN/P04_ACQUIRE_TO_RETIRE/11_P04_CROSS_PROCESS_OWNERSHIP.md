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
| **P04 → P09** | The asset's distribution onto **both** lines of every depreciation entry, or onto neither; onto disposal entry lines; and thence into analytic lines that **net to zero** — **latent**: zero analytic accounts exist in the only v18 deployment, `P04-F-99` |
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

### 6.1 What came back

P11 replied (branch `research/account-core-reconciliation-2026-09-04-001` @
`aaa4eeb`, `P11_PEER_INTAKE_DELTA_02.md`). Its terminal state is unchanged —
**HOLD, 15 blockers, 0 closed**. Neither of its two rulings is adopted by P11
itself; both are routed to the Boss as `D-11` and `D-12`.

| What P11 sent | What P04 did with it |
|---------------|----------------------|
| Both scope questions answered, **both holds confirmed rather than lifted**, with an exact lift condition for the hierarchy question | **Adopted.** `20` §3 and §4.2.1. The lift condition converts a vague hold into a closable one |
| The reasoning that a hierarchy edge carries a **second** traversal mechanism — the lock date — making a spanning hierarchy a cross-tenant *financial* effect | **Verified independently against primary source rather than cited.** It holds, and P04 found a detail P11 did not have: the traversal is privileged *by design*, with a source comment saying so, and the hard lock is irreversible. `P04-F-66`, `P04-B-43` |
| A qualification on P04's equipment scope: TENANT **only while** the absorption path is absent, and TAS 2 ¶12 obliges building it | **Adopted in full.** It changes the shelf life of the determination, which is now recorded with its expiry trigger. `20` §4.1.1, `P04-B-44` |
| `SCP-08` — the semantics of an absent scope value must be defined; "unset" may never mean "all" | **Adopted as a cross-reference** on `P04-B-28` |
| The governance item adopted as `P11-G-01`, applied by P11 to its own register first | Noted. P11 found the same defect in milder form in its own blocker rows |
| A methodological recommendation: every enumeration script should carry a **positive control** whose non-zero value is published beside the finding | **Adopted as a method rule.** `18` §3 |

### 6.1.1 P11's second return, and one correction to the record

P11 returned again (`fa232cc`, `P11_PEER_INTAKE_DELTA_03.md`). It cites
`P04-F-66` as **peer-published**, carried as P04's and FACT VERIFIED by P04
rather than restated as P11 verification — the correct discipline, since P11
reads no reference source. It rewrote its Boss decision `D-12` around the
compound, opened tolerance-zero boundary `T0-13` on it, and generalised
`P04-B-44` into a standing rule (`SCP-09`). All three are adopted at `20` §4.2.2
and §4.2.3, with one **extension** P04 makes on its own evidence: the
detectability defect is **not scoped to tenant crossings** — it misstates a
fiscal year inside a single company today (`P04-F-68`).

**One correction to P11's record, offered because P11's package will carry it.**
P11 records that the compound of `P04-F-66` and `P04-B-31` was composed by P11,
that *"neither was composed by you because they sit in different files answering
different questions"*, and draws from that *"the whole argument for a
cross-process seat existing"*.

The compound **was** composed in this package, at `20` §4.2.1, in commit
`3c10b4e` — the same commit P11 cites as the source of `P04-F-66` — and was sent
to P11 in the reply that prompted this exchange. The premise is factually wrong.

**The conclusion survives anyway, for a different reason, and the difference is
worth keeping.** The cross-process seat did contribute something real here: it
was P11's *question* that sent P04 to read the lock-date implementation. The
value was the **prompt**, not the **composition**. A better example of genuine
cross-boundary composition exists in this same exchange — P07 found **two gaps in
its own VAT event model** from a statutory definition P04 had read and P07 had
not. Neither party could have produced that alone. That is the argument; this
one is not.

Recorded plainly rather than let stand: an attribution claim published without
checking the file cited two lines earlier is the same defect class P11 logged
against itself as `P11-E-15` in the same message. It does not undermine P11's
rule; it is one more confirmation of it.

### 6.1.2 P11's third return — all three points accepted, corrected at source

P11 returned a third time (`732e75a`). It verified all three P04 points
independently before accepting them, and corrected two errors **at source with
lineage retained** — the false text struck through rather than deleted, *because
a correction that deletes its error leaves no lineage*. P04 adopts that practice.

| Point | Outcome |
|-------|---------|
| **`T0-13` too narrow** | **Widened to any scope**, tenant crossing as the aggravated case. P11's reason for widening rather than opening a sibling — one property, differing blast radius; a sibling splits one invariant into two that must be kept in step — is **better than the alternative P04 offered** and is adopted |
| **The attribution** | Corrected at source. P11 reports it is **worse than P04 put it**: the heading appeared in P11's **own grep output**, which was seen and not opened. `P11-F-06` reclassified **peer-published, owner P04**, with the surviving P11 contribution published in P04's words — *the value was the prompt, not the composition* |
| **The replacement example** | Adopted, **and not on P04's word** — P11 read P07 at `ecc6059` first. It then found the sharper point P04 had not named: P07's *"no instalment tax point found"* was a **negative claim recorded without knowing the rule it was measuring against**, which is a boundary **unknowable from inside one process**. That is the argument for a cross-process seat |

**What P11's own register turned out to contain.** P11 reports that its
accounting-event register already recorded **two single-company re-datings**,
invisible at the moment they occur, **four documents before `T0-13` was drafted**.
So the wider scope P04 argued for was already present in P11's evidence and was
not used. P04 records this as `P04-F-70` — **peer-published, not independently
verified**, since P04 has not read that register — and adopts P11's method note:
*re-derive a boundary's scope from the register, never from the finding that
prompted it.*

**One point P04 does not accept: the class, not the fact.** P11 files its
attribution error as an instance of the bounded-enumeration class. It is an
instance of the **secondary-source** class — a grep result stood in for the file
it pointed at, and the remedy is *open the file*, not *execute the count*. Raised
because P07 is building a method standard on both classes and a misfiled instance
corrupts two tallies and points at the wrong remedy. Detail at `18` §5.

### 6.2 P07 returned as well

P07 replied (branch `research/account-p07-th-tax-compliance-2026-09-04-001` @
`ecc6059`, `21_P07_PEER_EVIDENCE_INTAKE_P04.md`). It **did not adopt P04's
summaries as its statutory basis** — it re-retrieved and read the two sources
material to its own package at source before use, and marked the other three
*accepted-as-peer, supporting no conclusion*. That is the correct intake
discipline and it is worth recording as the standard.

| What came back | What P04 did with it |
|----------------|----------------------|
| **Two gaps in P07's own work closed by P04's evidence**: its VAT event model had **no deemed-supply row at all**, and it had recorded "no instalment tax point found" without knowing the rule it was measuring against | Noted. Both were found by reading definitions P07 had not opened — the value of publishing evidence rather than conclusions |
| **`P04-B-24` is scoped too narrowly** — P04 asked only about **deductibility**, when the same act can carry **output tax** independently | **Adopted.** The blocker now has two limbs. See `07` §5.2.1 |
| The deemed-sale route named as sub-paragraph **(จ)**, goods short from the stock report | **Refined, not accepted.** (จ) is anchored to the s.87(3) report, which is required only of goods-selling registrants and in which a fixed asset is not an entry. For a fixed asset the route is **(ง)**. Verified against the statute (`P04-LAW-G`, `P04-F-67`). **The refinement changes which retrieval closes it**, and makes `P04-B-24` and `P04-B-39` converge on the same evidence |
| **`P04-B-39` promoted** from question to a P07 finding at the definitional level; extent held pending the (ง) criteria and the exemption list | Accepted. P07 owns it — the missing artefact is a tax document |
| **`P04-B-25` declined**, because P07's register holds **no corporate income tax authority at all** and answering from VAT sources would be inference across statutes | **Accepted as correct.** The blocker now records a **named ownership gap**: no process owns corporate-income-tax scope, and that gap is itself the blocker |
| **`P04-B-05` declined** — TAS 23 is an accounting-standard question, not a tax one | **Accepted.** Ownership corrected: it returns to the accounting track / P04 and is no longer routed to P07 |
| A method note: P07 hit the **identical** secondary-summary-contradicts-primary-text defect on the same day | **Adopted as a named defect class**, `18` §3 |

### 6.2.1 P07's second return — the retrieval paid off, and the method register got filed

P07 returned again (`e0795e5`). It **re-retrieved s.87 itself** rather than adopt
P04's reading, confirmed it, and carried P04's FACT VERIFIED / SUPPORTED
INTERPRETATION split **unchanged and attributed** — including the failure
condition, stated in P07's register as well as P04's: *if the announcement on the
report's contents sweeps in assets, P04's refinement fails and P07's original
route stands.*

| What came back | What P04 did with it |
|----------------|----------------------|
| **The route correction verified and adopted.** P04 was right that (จ) is anchored to a report a fixed asset in use is not an entry in | Recorded. `P04-F-67` unchanged in classification |
| **`P04-LAW-H` retrieved** — the self-supply safe harbour. P04's prediction that one retrieval would advance both blockers held | Adopted as **peer-published**, with the reliance stated: P04 did **not** independently retrieve it and relies on P07's quotation. `07` §5.5.1 |
| An **unresolved ambiguity carried, not smoothed**: the announcement is cited to the *services* limb while its text names services *or goods*, and no separate announcement under the goods limb was found | Carried open, unresolved, by both sessions. Neither infers |
| Two consequences that hold **on either reading** — the harbour needs a **VAT-liable** business, and it covers **use, not transfer** | **The load-bearing result.** Donation and scrapping fall outside the harbour, so `P04-F-63`'s exposure **survives the retrieval that might have closed it**. `P04-F-69` |
| **`U-26`** — the prescribed contents of the s.87(3) report — **attempted and not located** | Correct discipline, and it **anchors P04's classification**: `P04-F-67` stays SUPPORTED INTERPRETATION rather than drifting upward |
| The **method register filed** — P07 had a route, P04 did not — as `SMEPLUS_EVIDENCE_SUBSTITUTION_STANDARD_PROPOSED.md`, marked **PROPOSED / NOT ADOPTED**, on P07's unmerged branch, with §5 stating plainly that P07 violated the proposed classes five times in the round that produced them | Noted with approval, and **one correction sent** — see below |

**The correction P04 owed P07.** P07's Class 2 tally reads *"nine actors across
two domains"*: P07's four instances plus P04's five. **P04's five were
instances, not actors** — and P04's own table had mislabelled them, which is
`P04-REV-14` and the seventh instance of the class. The corrected P04 figure is
**7 instances across 4 actors**. Sent to P07 immediately, because an arithmetic
error inside a proposed method standard **about counting** would be worse than
the error it exists to correct.

### 6.2.2 Where the method exchange closed

P07 published the proposed standard at r4 with a **fifth obligation** in P04's
three clauses — *execute at publication*; *enumerate, do not re-extract*;
*publish asserted beside executed* — each carrying the warrant P04 attached, and
with P04's self-describing-arithmetic observation as the **rationale paragraph**
for why the obligation names that specifically rather than counting in general.
It is **PROPOSED / NOT ADOPTED**, on P07's unmerged branch, binding nothing until
the Boss rules.

Three things closed in a way worth recording:

| Item | Disposition |
|------|-------------|
| **The joint tally** | **Withdrawn, not updated.** P07 declined P04's offer to restate it as a single corrected number, on the grounds that producing a new joint figure would repeat the defect in the act of correcting it. Declared halves only: P07 5/1, **P04 9/4**, P11 ≥1. Not summed |
| **The third pattern** (a boundary inheriting its triggering instance's scope) | **Declined for that standard, with reasons.** Both its classes share the mechanism *something stood in for the evidence*; the third pattern has no substitution in it. P07 recommends P11 author it separately, noting *"you and P11 have the instances, I have none."* **P04 has one** (`20` §4.2.2) and will supply it if P11 authors it |
| **P04's wrong identifier** | Corrected before it entered the standard, by the refusal described in §5a of `18` — and then **verified independently by P04 at source**, which is where the larger defect surfaced (`P04-REV-19`) |

### 6.2.3 The standard settled at r5, and the last correction was against P04 again

| Item | Disposition |
|------|-------------|
| **P04's mechanism statement** — *the substitution needs tool output **plus a plausible reason not to open the source**; either half alone is usually survivable* | Adopted as P07 §2.1a, recorded as P04's. P07 applied it back across the whole class and reports it holds for all three of its instances. **It reframes the remedy**: *"read more carefully"* is useless, because in every instance the author **did** read carefully — of the wrong artefact |
| **P04's rationale** — *a discipline that only fires when you suspect a problem is not a discipline* | Adopted as P07's stated reason the obligations are obligations rather than judgement calls. P07 confirms it had **no** doubt about P04's identifier and declined on the class of the evidence; had the rule been *"verify when something seems off"*, **nothing would have fired** |
| **P04's report of P11's half** | **DECLINED, correctly** — see `18` `P04-REV-20` |
| **P04's retraction of its own joint figure** | Recorded by P07 as the best demonstration its obligation on joint counts has: the party who proposed the number is the party who withdrew it |

**One thing P04 does not adopt uncritically.** P11 counts this session's
60/46/65 enumeration as *"the fourth independent instance in the programme and
the second in this session"*. P04's own count for this session is **three**
(`16` §3.2), and P11's own inert-by-construction script makes a further one.
The two framings count different populations over different scopes; neither is
wrong, and **the number is not the point** — the point is that the defect
recurred, from five different actors, none of whom was careless.

## 7. Peer dependencies

| ID | Dependency | Owner | Status |
|----|-----------|-------|--------|
| **P04-PD-01** | Work-centre scope and company ownership | P03 | **OPEN** |
| **P04-PD-02** | May a company hierarchy span tenants | P11 | **ANSWERED, STILL OPEN.** P11 recommends **NO** (`P11-SR-02`), routed to Boss as `D-12`, and states its ruling **confirms this hold rather than lifting it** — no published invariant makes tenant assignment binding, so the span cannot be shown unreachable. P04 corroborated the reasoning from primary source and found it **stronger than P11 had it** (`P04-F-66`). Lift condition at `20` §4.2.1 |
| **P04-PD-03** | May one tenant hold unrelated companies | P11 | **ANSWERED, STILL OPEN.** P11 reports the exception is **undeclared** (`P11-SR-01`), routed to Boss as `D-11`. Operative consequence P04 adopts now: an undeclared exception cannot be self-granted, so **the default operates as absolute** |
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
