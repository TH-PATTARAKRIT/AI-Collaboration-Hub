# SA_CORR3_03 — BLK-07 PRODUCTION OVERHEAD — TARGETED VERY DEEP STUDY
## CP-SA-C3-10 (production-overhead limb)

Phase SA CORR3 · SMEs Core · finding prefix `POH-` · Frame: **`CORR3-FRAME`**, adopted by pointer.
Branch `architecture/phase-sa-corr3-proof-verification-2026-09-09-001` @ `5953ce26`.

> **Status of this document:** technical study and `HOLD` recommendation. **Not an approval, not a
> design freeze, not a Boss ruling.** It does not begin Pre-Test Matrix, Functional Design or code.

> **Orchestrator intake note.** Same-model executor; `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not
> adopted on its word.** `POH-F-13`'s load-bearing half re-executed and **CONFIRMED**:
> `22_ASSET_FINAL_BLOCKER_REGISTER.md` line 19 reads `| BLK-06 | Where does unabsorbed depreciation
> go? | **CLOSED — BOSS DECISION** |`, and `10_P04_BLOCKER_REGISTER.md` line 24 records it *"closed by
> `BD-02`"*. The destination of unabsorbed overhead **is** already closed by a standing Boss decision.

---

## 1. Verdict in one page

> ## `HOLD` — the production-overhead path is **NOT** `EVIDENCE-PROVEN`.
> **Two of seven semantic links are proven at design-candidate level. Four are gapped. One is partial
> with named holes. The exact unresolved proof gap is named at §11.**

And the question this study was commissioned to answer:

> ## `POH-F-01` — `BLK-07` is **mostly not a Boss policy decision.** It is a design and proof gap that SMEs Core must close, wrapped in a decision label.
>
> On the corpus's own primary registers: the **destination** of unabsorbed overhead is already **closed
> by a standing Boss decision** (`BLK-06`, `BD-02`); the **allocation basis for fixed overhead** is
> recorded as **settled by evidence** in the owning register, **which lists the alternative in its own
> *Rejected* table as `REJECTED — INVALID ASSUMPTION`**; and the **existence of an absorption mechanism
> at all** was never a policy question in any register — **it is unbuilt architecture.**
>
> What is genuinely left for Boss is **six items, none of which is "normal capacity or actual hours"**
> (§9).

---

## 2. Method, instruments, and controls

Five instruments: `q.sh` (case-sensitive by default); `grep -rli -E` as a second shape for every
published count; literal-variant `grep -rli` as a third shape where a negative is load-bearing; an
`awk` blob→path join; and a working-tree `find … | xargs grep -l` for file-unit counts.

**Controls on every published count:** a positive control on each negative, run through the same
instrument; negative control `qxvz7481_no_such_token` = 0 in every population; a **coverage assertion**
where a per-artefact loop was used (`30 requested / 30 read / 0 missing`); and a **second command of a
different shape** for every count in §3.

**What was declined:** adopting any prior package's conclusion without opening its primary text (nine
packages read at primary-text level); copying a vendor costing engine, module structure, rate field or
posting sequence; deciding `BLK-07`, `BLK-08` or any §9 item; and verifying Thai gazetted statutory
text (§10).

**Independence:** internal adversarial self-challenge only. **Three of the corrections in §8 were
produced by self-challenge; on the programme's own recorded history that ratio is unrepresentative of
what independent review finds.**

---

## 3. Counts, with pattern, population, unit, path set and second shape

`POPULATION` = `CORR3-FRAME` `U1` = **3,900** blobs. `UNIT` = one blob.

| id | Pattern | Shape 1 | Shape 2 | Shape 3 | Positive control | Negative |
|---|---|---|---|---|---|---|
| `C-1` | `over[- ]?absor` (-i) | **2** | **2** | **2** (5 literals) | `unabsorbed` 16/16 | 0 |
| `C-2` | `unabsorbed` (-i) | 16 | 16 | — | — | 0 |
| `C-3` | `unallocated` (-i) | 35 | — | — | — | 0 |
| `C-4` | `overhead` (-i) | 135 | — | — | — | 0 |
| `C-5` | `normal capacity` (-i) | 51 | — | — | — | 0 |
| `C-6` | `conversion cost` (-i) | 73 | — | — | — | 0 |
| `C-7` | `BLK-07` | 82 | — | — | — | 0 |

**`C-1` is the load-bearing count and it was wrong on the first pass.** A narrower pattern returned
**1**; widening returned **2**, and the second hit is the CORR3 master prompt itself — the document
commissioning this study. **Substantive treatments of over-absorption in the entire 3,900-blob corpus:
exactly one.** Recorded as a method event, not hidden: **a count validated only against its own narrow
pattern is not validated.**

### 3.1 File-unit counts inside the assurance packages

`POPULATION` = the two Phase SA package directories = **40 files** (executor's count; the orchestrator
measures **38** at the markdown unit — see the note on `SA_CORR3_01` `XD1-C1`; **neither figure changes
any result below, all of which are zeros against firing controls**).

| id | Pattern | Files | Positive control |
|---|---|---|---|
| `C-8` | `ASSET_DR_CONTINUATION` ∪ `BLK-08` ∪ `PRODUCTIVE_NONPRODUCTIVE` | **0** | `BLK-07` = **6** |
| `C-9` | `UAE-16` ∪ `UAE-17` ∪ `UAE-31` ∪ `UBE-23,24,26,27` | **0** | `SA11-F-01` = **8** |
| `C-10` | any `UAE-nn`/`UBE-nn` identifier at all | **1 distinct** (`UAE-32`) | as above |

### 3.2 The adopted inventory design set

`POPULATION` = every (path, blob) pair matching `FINAL_SOLUTION/INVENTORY` = **30**.
**`COVERAGE: 30 requested / 30 read / 0 missing.`**

| id | Pattern | Hits | Second shape | Positive control |
|---|---|---|---|---|
| `C-11` | `overhead` (-i) | **0 of 30** | set-intersection of the 30 SHAs with the corpus-wide hit list = **0** | `valuation` = **28 of 30** |
| `C-12` | `conversion cost` (-i) | **0 of 30** | — | as above |
| `C-13` | `normal capacity` (-i) | **0 of 30** | — | as above |
| `C-14` | `absorb` (-i) | **1 of 30** — on inspection an unrelated use | — | as above |

> **`POH-F-02`.** The module that owns inventory valuation in the SMEsPlus **adopted-design** layer
> contains **zero** references to production overhead, conversion cost, or normal capacity across its
> complete two-version set, on two instrument shapes, **with a positive control firing on 28 of 30
> artefacts.** Class: `MEASURED NEGATIVE` within the declared path set.

---

## 4. The seven-link semantic chain, proven or gapped link by link

`Cost Source → Cost Classification → Allocation Basis → Manufacturing Consumption/Absorption →
WIP/FG Cost → Accounting Fact/Event → Posting/Reporting`

| # | Link | Verdict | What is proven | What is missing |
|---|---|---|---|---|
| **L1** | **Cost Source** | **`GAPPED — PARTIAL`** | One pool has a source: the asset sub-ledger produces a dated period depreciation charge, its posting behaviour characterised | **No source is specified for any other fixed pool.** Maintenance cost has *no accounting existence at all*. **Energy, standing utilities, indirect labour and factory supervision have no capture mechanism named in any SMEsPlus design document.** The maintenance *part issue* is a movement whose cost has no destination |
| **L2** | **Cost Classification** | **`PROVEN AT DESIGN-CANDIDATE LEVEL`** | A three-axis taxonomy (traceability / behaviour / item nature), **explicitly orthogonal**, with the three conflation errors named; and a **21-row element matrix** giving each element its position on all three axes, its destination and its statutory basis | **`DESIGN CANDIDATE`, unadopted, cited by nothing outside its own package** (`C-8`). Two rows left to case judgement. **The fixed/variable axis is something SMEsPlus must add — a requirement, not a built thing** |
| **L3** | **Allocation Basis** | **`DETERMINED FOR FIXED` / `OPEN BY DESIGN FOR VARIABLE`** | Four candidate drivers scored on thirteen criteria; work-centre averaging eliminated **structurally, not by preference**, and the elimination survived challenge; **normal-capacity machine hour is the only compliant driver for fixed overhead**, and the register states the result *"comes from statute, not from analysis preference"* | The **variable** driver is deliberately per-element and configurable — **correctly open, not a gap**. The **departure from `BD-04`** needs Boss confirmation (`POH-D-01`). **A dated normal-capacity register per machine is a required object that does not exist** |
| **L4** | **Consumption / Absorption** | **`GAPPED`** | The absorption arithmetic is fully specified for the depreciation pool, including the closure identity `Productive absorbed + Non-productive = period depreciation`, **exact, every period** | **(i)** No overhead **pool object** exists — the specified numerator is depreciation only, so **five of the six classified fixed elements have no pool to enter**. **(ii)** No **capacity denominator** object. **(iii)** The **exactly-one-mechanism** proof required by the standing veto **cannot be discharged in either direction** — it *"fails on three of four tests and returns zero on the runtime test"*. **(iv)** No mutual exclusion, validation or collision check |
| **L5** | **WIP / FG Cost** | **`GAPPED`** | The adopted inventory design names the boundary and the fact: consumption decreases stock *"into work in progress"*; output increases stock *"from work in progress"*; each emits a fact | **WIP is a named counterpart with no defined value composition.** `C-11`…`C-13`: **zero references to overhead, conversion cost or normal capacity.** Period-end WIP valuation exists only as an unadopted candidate, described there as *"the single largest structural addition the period model needs"*. **Nothing in the adopted layer receives an absorbed amount** |
| **L6** | **Accounting Fact / Event** | **`PARTIAL — IDENTIFIED, NOT DETERMINED`** | The events **exist as identified entities** with owners and triggers: conversion cost absorbed; unabsorbed overhead expensed; capacity idle; depreciation absorbed; absorbed-vs-actual variance. A position exists that absorption **and** the relief of the period-expense line must each be an explicit posted event, **neither implicit** | Three carry `NOT DETERMINED` or `HOLD` in their own status field. **The absorbed-vs-actual variance event has no owner.** Underneath sits **no accounting-event recognition identity distinct from entry creation** — the root blocker, **duplicates undetectable across all ten processes**. **And none of these identifiers has ever reached the assurance layer** (`C-9`, `C-10`) |
| **L7** | **Posting / Reporting** | **`GAPPED`** | Design candidates exist and are unusually complete: **three closes in a one-directional order**; the costing entry carries the **costing period's** date and is **refused if that period is locked**; hours rated at the rate in force **when logged**; a per-machine period reconciliation that **must close to exactly zero** as the publication gate; late-evidence rules; freeze-after-close asymmetry | All `DESIGN CANDIDATE`, **none adopted, none cited outside its own package**. **No statutory presentation treatment of over- or under-absorption is specified anywhere.** No absorption reconciliation report in any adopted design |

**Chain tally: `L2` and `L3` proven-at-candidate; `L6` partial; `L1`, `L4`, `L5`, `L7` gapped = 7.** ✓
**The chain does not close.**

> **`POH-F-03`.** The break is not evenly distributed, and its **single most consequential discontinuity
> is between `L4`/`L7` and `L5`**: a complete absorption arithmetic and a complete posting/close model
> exist as design candidates in one package, **and the package that owns inventory value has never heard
> of them. An absorbed amount is computed by a model with nowhere to send it, into a receiver that has
> no field to receive it.**

---

## 5. The overhead element population — the denominator is author-chosen and version-specific

`SA11-F-01` states *"seven of eight overhead elements have no source path at all."* Row-count executed:

| Source | Rows | Element set |
|---|---|---|
| the earlier register | **8** | equipment, building and right-of-use depreciation; planned maintenance; energy/utilities; indirect labour; overhead pool; machine cost via the work-centre rate |
| the **later**, closure-round matrix | **7** | depreciation *(three kinds collapsed to one)*; planned maintenance; **repair**; energy/utilities; indirect labour; pool + capacity denominator; machine cost |
| **Union of distinct named elements** | **9** | |

> **`POH-F-04`.** The `8` in `SA11-F-01` is the element set of **one round**. The **later** matrix
> publishes a **different set of 7**, collapsing three depreciation kinds into one and **adding
> *repair*** — an element absent from the 8-set. The union is **9**. `SA11-F-01` therefore carries a
> denominator that is **(a) author-chosen, (b) not the latest, and (c) omits an element its own lineage
> later named.** **Nothing in the substantive conclusion changes** — every element in every version is a
> gap — **but the fraction `7 of 8` is not a reproducible measurement, and it has propagated to the
> assurance layer as if it were.**

Cross-reference: the `L2` matrix carries **six** rows whose behaviour axis is `Fixed` and whose
destination is `WIP → FG, on normal capacity`. **The specified absorption arithmetic at `L4` has a
numerator covering one of those six.**

---

## 6. Master-prompt §6 mandatory topics — coverage and disposition

**Coverage assertion: 15 of 15 mandatory topics addressed; 0 omitted; 2 found to rest on a single
unreviewed source each.**

| Topic | Disposition |
|---|---|
| **Fixed production overhead** | Classified (`L2`); basis determined (`L3`); **pool source absent for 5 of 6 elements**; no pool object |
| **Variable production overhead** | **Applicable.** Required basis is *actual use*, **correctly per-element and configurable** — explicitly the place where a universal winner would be wrong |
| **Normal capacity treatment** | Basis determined; **the register object is absent**; governance controls specified (dated record, never an editable field; annual review; per-period absorption-ratio report) |
| **Under-absorption** | **Destination CLOSED by Boss decision** (`BLK-06`, `BD-02`). **Mechanism absent** |
| **Over-absorption** | **`C-1`: one substantive treatment in 3,900 blobs.** Candidate: cap productive absorption at the period's charge, so **absorbed cost may never exceed cost that exists**; when the cap binds, **report it, because a binding cap means normal capacity is set too low** |
| **Idle capacity** | Decomposed into **8 named causes** with per-cause destinations, and **`OTHER` designed as a control, not a bucket** — non-zero means evidence is missing and must be reported. Two causes left as policy candidates |
| **Direct vs indirect production cost** | Axis A of the three-axis model; explicitly **not** a synonym for fixed/variable, **and conflating them is named as the exact mechanism producing the non-compliant spread** |
| **Work Center relationship** | Work-centre averaging **eliminated** for the fixed component — **it cannot answer *which machine*, which is the business requirement.** **Silent fallback to work-centre averaging is forbidden**; unattributed allocations must be recorded and reported |
| **Period timing** | Three closes in fixed order; cost attributed to **the period the hours were logged**, not the period of completion; entry **refused if the costing period is locked** |
| **Standard vs actual cost** | **Material and under-weighted.** Absorption is **conditional on costing method**: under standard costing, work-centre cost **never enters finished-goods value**. Any design assuming machine cost reaches inventory is *"silently wrong for every standard-costed product"*. **Interacts directly with `BD-ACC-03B`** |
| **Inventory valuation interaction** | **`L5` gap.** Absorption's ledger half is conditional on valuation posture, so **`BD-ACC-03A` governs whether absorption reaches the ledger at all** |
| **COGS interaction** | The cost-of-sales recognition point is itself `NOT DECIDABLE` at the joint layer, so **an absorbed amount's arrival in COGS inherits an unclosed decision upstream of it** |
| **Month close** | `L7`. **A costing close distinct from the accounting close does not exist and must be built** |
| **Reversals / corrections** | Specified: allocation on a cancelled order **reversed by a dated correction, never deleted**; a reopened costing close must **recompute, not patch**; statutory allocation frozen after close with corrections to the next open period |
| **Evidence lineage · clean-room rationale** | §3 and §7.5 |

---

## 7. The `(a)`–`(d)` decomposition, with an owner per part

### 7.1 `(a)` Does an absorption mechanism exist at all?

> **`POH-F-05`. Owner: SMEs Core. This is not, and has never been, a policy question in any register.**
> It is unbuilt architecture, and it is **logically prior to and independent of the denominator
> question**: *any* absorption reading — **including the rejected one** — requires a pool, a driver, a
> cost object, an event and a posting. **None exists.**

| Requirement | Exists? |
|---|---|
| A fixed-overhead **pool object** | **No** |
| A **capacity denominator** object | **No** |
| A **production / non-production classification on the asset**, gating entry to the model | **No** — required by three design documents, built by none |
| A **fixed/variable attribute** on a cost element | **No** — *"without it TAS 2 ¶13 cannot be implemented at all"* |
| An **equipment usage event** joining a machine's use to an asset's charge | **No** |
| A resolved **asset ↔ equipment cardinality** | **No** — many-to-one and unconstrained |
| An **absorbed-vs-actual variance** event with an owner | **No** |
| A proof that **exactly one** mechanism carries machine cost into product cost | **No — and the test as specified cannot return one** |

> **`POH-F-06`.** The standing veto has **two limbs**, and the programme has been tracking only the
> first. Limb 1 (`BLK-07`) is the decision. **Limb 2 — prove exactly one mechanism carries machine cost
> into product cost — is an SMEs Core proof obligation, it is undischarged, and its own reviewer records
> that the limb *"tests for uniqueness where the answer is zero"*, so it cannot be discharged in either
> direction as written.** Restating a veto limb is reserved to the veto's issuer and Boss. **Deciding
> `BLK-07` alone would not lift the veto.**

> **`POH-F-07`.** The associated risk is **not hypothetical and not a configuration issue**: the gate
> pack records that mechanisms **already** reach product cost and that this design proposes another,
> that **no mutual exclusion, validation or collision check exists**, and that **because each mechanism
> reconciles perfectly against *itself*, no report in the design would detect a double count. A design
> that double-counts and reconciles is worse than one that visibly fails.**

> **`POH-F-08` — latent vs live, measured.** The `(a)` defects are **latent in the examined deployments
> and architecturally live**: **1 live, 11 latent, 3 unreachable.** They are latent **because the system
> is unconfigured, not because it is controlled** — every empty field is one an administrator is
> expected to fill on day one. **A veto whose subject is architecture is not discharged by configuration
> emptiness.**

### 7.2 `(b)` What allocation basis and normal-capacity definition applies?

> **`POH-F-09`. Settled by evidence for the fixed class; one Boss confirmation remains, and it is not
> the confirmation being asked for.**

The decisive item is **inside the owning register itself**:

| Section | Says |
|---|---|
| §1 status row | `BLK-07` — *"Is the allocation denominator normal capacity or actual hours?"* — **`HOLD — DESIGN DECISION REQUIRED`** |
| §3 | Question restated as a binary; *"Why it cannot be researched: `BD-02` is genuinely ambiguous between the two"*; **Recommendation: normal capacity** |
| **§6 — *Rejected*** | *"The reading of `BD-02` that divides period depreciation across actual productive hours — **`REJECTED — INVALID ASSUMPTION`**. It breaches TAS 2 ¶13, is undefined at zero output, and capitalises idleness into inventory. **Recorded as rejected so it is not rediscovered as an obvious simplification during build**"* |

> **`POH-F-10` — an internal contradiction inside the owning register.** `BLK-07`'s §3 question offers
> exactly two options, and **the same document's §6 has already rejected one of them by name, with
> reasons, deliberately, so it cannot come back.** The blocker is stated as an open binary **whose second
> branch its own author closed.** Two downstream packages have already read it that way.

> **`POH-F-11` — the surviving live options agree on the denominator.** A later package opened a third
> option and separated two things the binary had merged: **one standard governs the size of the charge;
> the other governs its absorption.** The actual-hours reading fails. **Both surviving options use normal
> capacity as the absorption denominator.** The live choice between them is therefore a
> **depreciation-method election** — a different question, with a different owner-facing consequence
> (it changes the charge itself, requires a per-asset expected-output estimate nothing holds, and has
> **unresearched tax consequences**) — **carried under a different identifier.**

> **`POH-F-12`.** That third option **never reached the assurance layer as a distinct decision**. `SA11`
> and `SA_CORR2_13` continue to escalate `BLK-07` as a binary. **A Boss asked to decide "normal capacity
> or actual hours" is being asked to choose between an option and an option his own registers rejected,
> while the choice that is actually live is not on the paper.**

**Normal-capacity *definition*** is likewise determined, not open: capacity lost to **planned**
maintenance is subtracted from the denominator, so planned-maintenance cost is recovered through every
productive hour and **must not also generate a period charge — charging it twice is the failure mode.**
That is the substance of **`BLK-08`**.

### 7.3 `(c)` Where does under/over-absorption go, and when?

> **`POH-F-13`. Under-absorption: destination CLOSED. Over-absorption: one unreviewed design candidate.
> Timing: SMEs Core, specified but unadopted.**

| Limb | Status | Owner |
|---|---|---|
| **Under-absorbed → destination** | **`CLOSED — BOSS DECISION`** (`BLK-06`, `BD-02`), *"reinforced by evidence"*, register records **"Remaining evidence requirement: None for the destination"** | **Already decided. Not a Boss item** |
| Under-absorbed → mechanism | **ABSENT** | SMEs Core |
| **Over-absorbed → destination** | **One treatment in the corpus** (`C-1`): cap absorption at the period's charge; when the cap binds, report it. **`DESIGN CANDIDATE`, never reviewed, never cited outside its own package** | SMEs Core |
| The variance itself as a fact | **`HOLD — DESIGN DECISION`, no owner named** | SMEs Core |
| **When** | Costing close, after the operational close and before the accounting close; **per-machine reconciliation closing to exactly zero as the publication gate**; frozen after close with dated corrections forward | SMEs Core |

> **`POH-F-14` — the over-absorption cap has a consequence nobody has tested.** Capping absorption at
> the period's charge means over-absorption **cannot arise for the depreciation pool** — **which is
> convenient, and which is exactly the shape of a result that should be attacked.** Once the pool
> contains standing utilities, indirect labour and planned maintenance (as `L2` requires), **the cap's
> behaviour across a *multi-element* pool is unspecified.** Additionally, **`BLK-06` is worded as *"where
> does **unabsorbed depreciation** go"* — it does not decide where an over-absorption *credit* goes, and
> no register asks.** Class: `SPECIFIED FOR A NARROWER POPULATION THAN THE ONE IT WILL SERVE`.

### 7.4 `(d)` What numeric normal-capacity level a tenant sets

> **`POH-F-15`. Owner: tenant/company configuration. Not architecture, not a Boss decision.** But **not
> control-free**, and the corpus is unusually clear-eyed about why.

Normal capacity **directly determines how much cost is capitalised into inventory** — lower it and more
cost is absorbed into stock and less hits the period. **That is the classic overhead-absorption abuse.**
Three controls are specified, all cheap, **none a Boss decision**: the figure is a **dated, attributed
record — never an editable field**; **reviewed annually** alongside a review the asset lifecycle already
requires; and the per-period reconciliation **reports the absorption ratio**, so a machine consistently
over- or under-absorbing is visible immediately. Plus one firm rule: **normal capacity is never changed
retrospectively** — permitting it would make inventory value **editable after the fact**.

`SCOPE-AWARE` note: the corpus does not settle whether the capacity register is `COMPANY`- or
`TENANT`-scoped. Given it determines a statutory inventory figure, `COMPANY` is the reading consistent
with `BD-ACC-02` — **stated as an observation, not decided here**, and flagged at §13 as a residual.

### 7.5 Clean-room rationale

Every design position is justified from **(i)** the requirement that conversion cost be computable at
all, **(ii)** the Boss's own standing decisions, and **(iii)** the internal consistency of the
arithmetic — **never from reference-product behaviour.** The corpus's strongest recorded statement on
the reference product is that it **models no fixed/variable distinction anywhere in the manufacturing
cost chain**, merges both classes into one scalar, and therefore **cannot** satisfy the requirement.
**There is no pattern available to copy, which removes both the temptation and the risk.** Where
reference behaviour is cited it is cited as *evidence that a thing is absent*, and once as an explicit
**anti-pattern to avoid** — storing a rate snapshot that nothing consumes.

---

## 8. Corrections to inherited claims

| id | Inherited claim | Correction |
|---|---|---|
| `POH-C-01` | `SA11` §2, TAS 2 ¶12 row: **"SMEsPlus control: none yet"** | **Contradicted.** Four substantive design-candidate documents exist covering classification, allocation driver, absorption arithmetic and period close. Correct statement: *"controls specified as design candidates; none adopted, none cited by any assurance artefact."* **The difference matters: "none yet" implies research is owed; the evidence says publication and adoption are owed** |
| `POH-C-02` | `SA11-F-01`: *"seven of eight overhead elements"* | Denominator **author-chosen and superseded**; union = **9**; the later matrix publishes **7** and adds an element the 8-set omits |
| `POH-C-03` | *"gated behind the normal-capacity decision that only Boss can take"* | **Over-broad.** `BLK-07` gates the *denominator*. It does **not** gate the pool object, the capacity register, the fixed/variable attribute, the production classification, the usage event, the cardinality resolution, the variance event, or veto limb 2 — **each buildable and provable under either reading** |
| `POH-C-04` | `SA_CORR2_13` §16 Decision 4: `BLK-07` *"now carrying a second absent mechanism"* | **The second mechanism already has its own identifier, status field and determined destination.** `BLK-08` is `HOLD — DESIGN DECISION REQUIRED` with a statute-driven recommendation to split. **`BLK-08` appears in 0 of the assurance files.** Merging it into `BLK-07` **loses a determination that already exists** |
| `POH-C-05` | `TVDR-05`: *"Decide where maintenance cost lands — Boss-owned, joined to `BLK-07`"* | **Where it lands is already determined at design-candidate level.** What is genuinely absent is the **source**. **That is an `L1` build item, not a Boss decision** |
| `POH-C-06` | *"Runtime: **0 work centres exist**"* | **Stated without its database qualifier.** Executed: one deployment has **0**; the other has **60**, of which **1** is rated and **0 of 60** carry an absorption account |
| `POH-C-07` | *(self-correction)* My own `C-1` first returned **1** | A narrow alternation missed a hit; widened and re-run on three shapes, all returning **2**. **Recorded because a count validated only against its own pattern is not validated** |

---

## 9. Residue that is genuinely Boss's after `(a)`–`(d)` are separated

| id | Item | Why it is genuinely Boss's | Standing recommendation (attributed, not adopted here) |
|---|---|---|---|
| `POH-D-01` | **Confirm the declared departure from `BD-04`** — one allocation driver per **cost class**, not per configuration context | It **modifies a standing Boss decision.** Only Boss may amend one, however statutory the reason | *"Yes. The standard requires different bases; a single driver cannot serve both"* |
| `POH-D-02` | **Depreciation-method election**: straight-line absorbed at normal capacity, or units-of-production absorbed at normal capacity | It **changes the charge itself**, is an accounting-policy election, has **unresearched tax consequences**, and requires a per-asset expected-output estimate the business does not maintain | Offered as a genuine third option, explicitly **not** as a displacement of the standing recommendation |
| `POH-D-03` | **Is SETUP time productive?** | Genuine business-meaning policy | *Candidate: productive — caused by, and traceable to, a specific job* |
| `POH-D-04` | **Are IDLE and NO_DEMAND one cause or two?** | Pure management-reporting policy — **they are accounted identically** | *Candidate: keep both* |
| `POH-D-05` | **Who owns the normal-capacity figure, and the review cadence** | Control-ownership policy | *Dated, attributed record; reviewed annually alongside the useful-life review* |
| `POH-D-06` | **`BLK-07` and `BLK-08`: confirm, or restate** | **Governance act.** A Boss-owned blocker can only be retired, restated or confirmed by Boss. §7.2 shows `BLK-07`'s stated binary is internally contradicted by its own register. **This document requests a restatement; it does not perform one.** Same for veto limb 2 | — |

> **`POH-F-16`. Of the four parts `(a)`–`(d)`, three are SMEs Core or configuration. The Boss residue is
> six items, five of them small, and *none of them is the question `BLK-07` currently asks*. The single
> largest item — `(a)` — is the one no register ever framed as a decision, and it is the one blocking
> everything.**

---

## 10. Statutory treatment, and what does **not** depend on it

> **`POH-F-17`. Within `CORR3-FRAME` no gazetted or professional-body primary text was read.** Every
> Thai statutory claim is recorded **`HOLD — EVIDENCE REQUIRED`**, and the instrument reference and Thai
> terminology **candidate / UNVALIDATED**. The corpus's own assurance layer reaches a compatible
> position: TAS 2 ¶13 items graded `EVIDENCE GAP`, and ¶13 conformance recorded as *unprovable* on
> current evidence.

> **`POH-F-18`. The requirement that an absorption path exist at all, with a capacity-based denominator
> and a defined destination for the unabsorbed remainder, does not depend on resolving any Thai-specific
> statutory question. Asserted, and here is the proof:**
>
> 1. **Existence is prior to basis.** `(a)` asks whether a pool, driver, cost object, event and posting
>    exist. **Every candidate reading of the denominator — including the rejected one — requires all
>    five.** Resolving the statutory question cannot create them and cannot make them unnecessary.
>    **Nothing in §7.1's eight-row table cites a statute.**
> 2. **The destination is fixed by a Boss decision, independently of statute.** `BLK-06` closed on
>    **`BD-02`**, and the register records that the statutory text *"independently reaches the same
>    destination"* — **corroboration, not the load-bearing basis.**
> 3. **A capacity-based denominator is forced by arithmetic, not only by statute.** An actual-output
>    denominator is **undefined at zero output** — an idle month has no divisor. **A costing model that
>    cannot compute in an idle month is not a costing model.** That objection survives the removal of
>    every statutory citation.
> 4. **The remaining statutory dependencies are narrow and identified**: the over-absorption cap's
>    strength; `BLK-08`'s direction; and the tax consequences at `POH-D-02`. **None blocks `(a)`,
>    `(c)`-mechanism, `(d)`, or veto limb 2.**
>
> **Consequence: SMEs Core's `(a)` work can and should proceed while the Thai statutory items remain on
> `HOLD`. Holding the build for a statutory confirmation that governs three narrow parameters would be
> holding the whole chain for a fraction of one link.**

### 10.1 The unmeasured consequence clause

`SA11-F-01` contains **two** claims:

| Claim | Status |
|---|---|
| *Fixed production overhead has no path into inventory value* | **Measured, version-independent, the load-bearing half.** Conversion cost is zero across the examined deployments by two different routes |
| *Therefore inventory is understated / COGS is misstated* | **NOT MEASURED — and for the SMEsPlus subject, NOT MEASURABLE on current evidence** |

> **`POH-F-19`.** Unmeasured in **three distinct senses**, which must not be collapsed:
> 1. **For the examined deployments it is deliberately refused.** The owning package states it does
>    **not** claim the standard is breached, and **refuses to infer intent**, since material-only costing
>    may be a legitimate policy.
> 2. **For SMEsPlus it is unmeasurable by construction** — there is no deployment, so no population in
>    which an understatement could be observed.
> 3. **The magnitude is unsizeable, and the reason is itself a finding.** No monetary quantum appears
>    anywhere in the 3,900-blob corpus. **It could not: sizing the pool requires the production /
>    non-production classification on the asset, and that classification does not exist.** **The exposure
>    cannot be sized because the object that would size it is one of the missing objects.**
>
> **Permitted wording: *"no absorption path is verified, and the resulting misstatement is unquantified
> and currently unquantifiable."* Any stronger form is unsupported.**

---

## 11. Acceptance condition — the exact unresolved semantic and proof gap

> ## `HOLD`. The production-overhead path is **not** `EVIDENCE-PROVEN`.

| id | The exact gap | Why it is a proof gap and not a research gap |
|---|---|---|
| `POH-G-01` | **No cost-pool object and no capacity-denominator object exist, and no source is specified for five of the six classified fixed elements.** The one specified absorption arithmetic has a numerator covering **one** of the **six** its own companion matrix classifies as fixed-and-absorbable | The classification is published; what is missing is a **pool** for the other five and a **capture mechanism** for their amounts. **Both are design artefacts. No further research produces them** |
| `POH-G-02` | **`L5` has no receiver.** Zero references to overhead, conversion cost or normal capacity across the complete 30-artefact adopted set, two shapes, firing positive control | **The absorbing model and the receiving model have never been in the same document.** An integration gap closable by SMEs Core in one artefact |
| `POH-G-03` | **Veto limb 2 is undischarged and, as written, undischargeable.** No mutual exclusion, validation or collision check; and **because each mechanism reconciles against itself, a double count would be invisible to every report in the design** | Restating the limb is the issuer's and Boss's act. **Building the mutual exclusion is SMEs Core's and does not wait on the restatement** |
| `POH-G-04` | **The absorbed-vs-actual variance is an identified event with no owner, no mechanism and no posting destination**, sitting above a deeper root: **no accounting-event recognition identity distinct from entry creation**, making duplicates undetectable across all ten processes. **Neither identifier has ever reached the assurance layer** | The variance is SMEs Core design. **The root is the one genuinely Boss-held blocker underneath this chain, and it is not `BLK-07`** |

**What would move this to `EVIDENCE-PROVEN`:** `POH-G-01`, `POH-G-02` and `POH-G-04`'s variance closed by
SMEs Core design work requiring **no** Boss decision and **no** statutory resolution; `POH-G-03`'s mutual
exclusion built and its detection report specified; and `POH-D-01`, `POH-D-02`, `POH-D-06` returned by
Boss. **Three of those six are already unblocked today.**

---

## 12. Findings register

`POH-F-01`…`POH-F-20`, `POH-C-01`…`POH-C-07`, `POH-D-01`…`POH-D-06`, `POH-G-01`…`POH-G-04`,
`C-1`…`C-14`, `I-1`…`I-5`. **Every identifier cited in the body is defined; none defined and left
uncited.** Peer families cited but not owned, and therefore not checked for definition here: `SA*`,
`IR-*`, `AR-*`, `BLK-*`, `BD-*`, `UAE-*`, `UBE-*`, `CV-*`, `CVP-*`, `P04-*`, `C2-F-*`, `TVDR-*`, `DC-*`,
`DEP-*`, `UNR-*`, `CQ-*`.

Findings not stated in full above:

**`POH-F-20`.** `SA06` — the inventory reconciliation matrix — contains **0** occurrences of overhead,
conversion, WIP, absorption or normal capacity on two shapes, **while grading manufacturing consumption
and finished-goods receipt `RECONCILED`.** **Its reconciliation unit is quantity; the value composition
of a finished-goods receipt is out of its unit and therefore invisible to it.** **A flow can be
`RECONCILED` and its value undefined at the same time.** Class: `MEASURED NEGATIVE + UNIT DEFECT`.

---

## 13. Residual uncertainty, proof gaps, and what to attack first

### 13.1 Residual uncertainty

1. **The corpus complement.** `CORR3-FRAME` excludes blobs reachable only from non-head history and all
   non-`.md`/`.txt`/`.csv` files. **A design artefact abandoned mid-branch, or an absorption
   specification in a spreadsheet, diagram or presentation, is outside everything searched.** Bears
   directly on `POH-F-02`, `POH-F-12` and `C-8`, **all of which are negatives.**
2. **Runtime and database evidence.** Worked entirely from the text corpus and working tree. **The host
   was not swept.** Every deployment-side figure cited is **inherited and re-read at primary text, not
   independently re-measured.** **A declared blind spot, not a clean result**, and its complement is
   *every runtime and database artefact on this host*.
3. **Version basis.** The source-side halves of the inherited negatives are bounded to the generations
   those packages read, and **at least one records that the generation read was not the generation
   deployed.** That bound is inherited and not narrowed.
4. **Scope of the capacity register.** `COMPANY` vs `TENANT` unsettled; **an observation, decided
   nothing.**
5. **Design-candidate quality.** Verified the candidates **exist, are internally coherent, and reach the
   conclusions attributed to them.** **Did not audit their arithmetic against worked examples**, and
   their own package states they were reviewed by the same session that wrote them.

### 13.2 What could not be proven, and the exact gap

| # | Could not prove | Exact gap |
|---|---|---|
| 1 | That **no** absorption mechanism exists anywhere for SMEsPlus | Can prove **no *adopted*** mechanism exists in the declared path set, and that four candidates exist unadopted. **Permitted wording: "no adopted absorption mechanism is verified within `CORR3-FRAME`."** |
| 2 | That the over-absorption cap generalises to a multi-element pool | **The gap is a worked case:** a pool containing depreciation + standing utilities + indirect labour + planned maintenance, at above-normal output, showing what the cap binds on and in what order. **Nobody has written it** |
| 3 | That the Thai statutory readings are correct | Primary gazetted text not read. **The gap is retrieval from an authoritative source, with the retrieval recorded.** Gates three narrow parameters, not the chain |
| 4 | That exactly one mechanism carries machine cost into product cost | **The gap is the limb's own specification: it tests for uniqueness in a population where the answer is zero, so it returns neither one nor not-one.** Until restated, the proof is not merely undone — **it is unformulable** |
| 5 | The magnitude of any misstatement | **The gap is the production/non-production asset classification.** Until that object exists, the pool cannot be sized |
| 6 | That the design candidates are arithmetically sound | **The gap is a numeric walkthrough of one machine across four periods — normal, low, idle, above-normal — closing the stated identity to zero in every one, including the idle period where the rejected reading is undefined** |

### 13.3 The claims a challenger should attack first, in order

1. **`POH-F-01` and `POH-F-10` — that `BLK-07` is answered inside its own register.** The headline, and
   it rests on reading a document's §6 *Rejected* table as governing its §3 *Open blocker* table. **A
   challenger should argue the opposite: that §3's status field is authoritative** (the programme's own
   peer status-field rule says read the register **and its status field**, which here says `HOLD — DESIGN
   DECISION REQUIRED`), and that §6 is a working note recording what the author would not build. **If
   that reading wins, `POH-F-01`, `-09`, `-10`, `-11`, `-16` and most of §9 weaken together, and `BLK-07`
   reverts to a genuine open binary. I have argued the stronger reading; I have not proved it. Attack
   this first.**
2. **`POH-F-02` / `C-11` — the zero on the adopted inventory design.** **Attack the path set, not the
   count:** is `FINAL_SOLUTION/INVENTORY` the whole adopted-design population, or the convenient
   artefact? **The programme's own history records exactly this failure mode twice. I did not intersect a
   declared design population with a delivered one, because no declared design population exists that I
   could find — which is itself either a finding I missed or a search I did not run.**
3. **`POH-F-18` — that the architecture is statute-independent.** **The sharpest attack is step 3:** a
   designer could define the actual-hours reading to yield zero absorption in an idle month and avoid the
   undefined case entirely — **at which point step 3 collapses and the statutory text does more work than
   I credit it with.** Steps 1 and 2 survive; step 3 may not.
4. **`POH-F-05`'s eight-row "does not exist" table.** **Eight negatives in one table, each inherited, none
   re-measured against source or runtime.** Pick the two most load-bearing rows — the equipment usage
   event and the asset↔equipment cardinality — and re-run them. **Eight inherited negatives in a row is
   precisely the shape that has failed before.**
5. **`POH-C-01` — that "none yet" is contradicted.** The mildest reading of *"none yet"* is *"no adopted
   control"*, which would make the correction pedantic. **Test whether the distinction between "specified
   but unadopted" and "none" changes any downstream disposition.** I believe it does — it converts a
   research obligation into a publication obligation, **the difference between months and days** — but
   **that belief is an argument, not a measurement.**

---

Checkpoint completion is **not** Boss approval. Boss remains the sole Final Approver.
