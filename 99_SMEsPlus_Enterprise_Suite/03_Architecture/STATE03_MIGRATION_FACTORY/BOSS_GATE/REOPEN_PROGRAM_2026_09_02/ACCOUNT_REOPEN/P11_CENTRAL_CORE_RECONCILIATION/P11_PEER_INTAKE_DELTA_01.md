# P11 — PEER INTAKE DELTA 01

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
**Supersedes `P11_SOURCE_LINK_REGISTER.md` §5 in part. Nothing earlier is deleted.**

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The premise changed during the session

`P11_SOURCE_LINK_REGISTER.md` §5 published, at `SNAPSHOT_UTC=2026-09-04T22:41:38+0700`:

> `PEER DEPENDENCY OPEN × 10` — **0 of 10 peer processes have published any artefact at any commit
> SHA.**

**That statement was true when written and is false now.** Re-running the same script at
`SNAPSHOT_UTC=2026-09-04T23:08:58+0700` — **27 minutes later** — returned three peer branches on
`origin`. The register's own qualifier held: it declared the count *"a reading at an instant, not a
stable population"*, and the instant passed.

> **This is the single most important methodological result of the session.** The one claim P11
> stated most forcefully, and the one an independent reviewer (`X1`, §4.5 item 10) **declined to
> endorse as `NOT DECIDABLE` from its position**, is the claim that expired first. A time-bounded
> claim about live parallel work is not a finding about the programme; it is a measurement. P11
> labelled it as one, and that labelling is what makes this delta an update rather than a
> contradiction.

## 2. Peer register — corrected

| Process | Branch on `origin`? | HEAD SHA | Files | Terminal state as that package declares it |
|---|---|---|---|---|
| `P01` Procure-to-Pay | **No** | — | 0 | `PEER DEPENDENCY OPEN` — unpublished work in progress observed |
| `P02` Order-to-Cash | **No** | — | 0 | `PEER DEPENDENCY OPEN` — unpublished WIP observed |
| **`P03` Manufacture-to-Cost** | **Yes** | `812cc5c6f579892da16371d7ec7b116a4db8fa2f` | **25** | **`READY FOR CORE ACCOUNTING RECONCILIATION`** |
| **`P04` Acquire-to-Retire** | **Yes** | `2602dfe9a911e9ee4ec5a23199d494a5a77cca58` | **19** | **`READY FOR CORE ACCOUNTING RECONCILIATION`** · *no asset final freeze declared* |
| `P05` Expense-to-Pay | **No** — 1 local commit, unpushed | — | 0 | `PEER DEPENDENCY OPEN` |
| **`P06` Bank-to-Reconcile** | **Yes** | `4146bb1be881afeb33f81b2c7b6e62d2899c9c60` | **20** | **`READY FOR CORE ACCOUNTING RECONCILIATION`**, as evidence for a decision, **under `AASP-VETO-01`** · 42 blockers · `RECOMMEND HOLD` |
| `P07` Tax-to-Compliance | **No** | — | 0 | `PEER DEPENDENCY OPEN` |
| `P08` Record-to-Report | **No** | — | 0 | `PEER DEPENDENCY OPEN` |
| `P09` Plan-to-Analyze | **No** | — | 0 | `PEER DEPENDENCY OPEN` |
| `P10` Time-Based Recognition | **No** | — | 0 | `PEER DEPENDENCY OPEN` |

> ## `PEER DEPENDENCY OPEN × 7` — corrected from × 10.
> **Three of ten have published. Not one declares a state stronger than `READY FOR CORE ACCOUNTING
> RECONCILIATION`, and each states in terms that it is not a `PASS`, not a freeze, not a merge and
> not an implementation authorisation.** `P06` hands over **under a standing reliance veto**.

## 3. What the three published packages change in P11

### 3.1 `DC-09` — no longer a P11-only inference. It is confirmed, and its direction reverses.

P11 reasoned that building the TAS 2 ¶12 absorption path without relieving the expense line would
charge depreciation twice. `P03` and `P04` supply the measured picture, and it is **worse in both
directions at once**:

- **Today the cost is understated, not doubled.** `P03`'s finished-goods unit-cost formula
  *"excludes, entirely: equipment depreciation, factory building depreciation, right-of-use asset
  depreciation, planned maintenance, energy and utilities, indirect factory labour, and fixed
  production overhead of every kind."* Most of those **belong in** conversion cost under the standard.
  *"Inventory produced under this model is therefore understated by construction, and cost of sales is
  understated with it."*
- **And a genuine double-charge already exists on a different axis.** `P03` behaviour 1: machine time
  is costed on a **head-count-dependent base**, so *"where two people work one machine, machine cost is
  charged twice. Inventory is **overstated**."* Designated `Tolerance = 0`.
- **And the count of competing mechanisms is five, not two.** `P04`: *"the same machine hour is
  monetised by **as many as five different routines** — and they do not reconcile with one another.
  Under one supported costing configuration there is a **genuine ledger mismatch** between the planned
  overhead credited to production and the actual overhead debited back, with **no variance account and
  no report that shows it**."*
- **And the route P11 and the Asset baseline both believed carried attribution does not.** `P04`:
  the cost-centre attribution route ~~**nets to zero**~~ — *"both sides of a depreciation entry carry the
  same attribution and the two amounts cancel."* Where an asset carries **no** attribution, the two
  sides can pick up **different** ones and leave *"a meaningless residue."*

  > **CORRECTED `2026-09-05` by `P09` `S23_P09_POST_PUBLICATION_CORRECTION.md` (`S8` re-run).**
  > ***"Nets to zero" is withdrawn by its own author, re-measured before acceptance.*** In deployed
  > data the net is **`+3,595,851.11` — a sign-inverted CREDIT**, annihilation **98.24 %** over
  > **17,444 / 17,488** records. *"Depreciation makes the cost centre look more profitable … materially
  > worse than zero, and no document in the package said it."* `P09` names the cause as
  > *"an asset-derived subset, not the population — **the programme's own denominator rule, missed
  > again**."* **The near-cancellation is real; the zero is not.** `P11-B-22`.

**Correction to P11:** `DC-09` stands as a risk of the corrective work, but P11's framing —
*"the risk is created by the correct action"* — was incomplete. The measured present state is
**simultaneously understated (omission) and overstated (head-count double charge)**, with five
unreconciled monetisations. `X1-F10` separately identified a sixth: a fully depreciated asset made
depreciable again by a capital improvement, where *"running both would count the same machine twice"*
and `BD-01` is **silent**.

### 3.2 Confirmed double-counting and settlement mechanisms — `P06`

`P06` returns **seven confirmed defects from eight attacks**, several of which P11 could only state
as unguarded classes:

| P11 class | `P06` confirmation |
|---|---|
| `DC-01` double posting | **`A1`** duplicate bank transactions via CSV, QIF, OCR, manual entry, `copy()`, or a second journal — precondition *"import a file twice — **the lowest bar in the set**"* |
| `DC-05`/`DC-06` duplicate AP/AR | **`A3`** duplicate payment against the same invoice; detection **advisory at every call site**, and one call site queries a state value **absent from the v18 selection** |
| `DC-11` double settlement | **`A5`** resetting or reversing a document **silently destroys the bank reconciliation**, via two independent paths, *"neither aware of the statement line"* |
| `DC-13`/`DC-14` leakage | **`A4b`** an **unowned bank account (`company_id = False`) admitted into every company by three separate guards**; **`A4c`** a payment token visible to a wider scope than its own transactions |
| `DC-15` closed-period mutation | **`A6`** *"reconciling and un-reconciling are **outside the entire period-close regime**"* |
| `DC-17` audit-trail inconsistency | **`A7`** statement-line deletion bypasses the audit trail; **enabling the audit trail converts a hard refusal into a silent un-reconcile** |

**`H-03` supplies the mechanism P11 could only name:** *"the identity system **fails open at every
layer, in the same direction**. Four of seven ingestion doors attach no identity; three enforcement
points treat a null identity as 'not a duplicate'; the provider reference is unconstrained, never
searched, and **overwritten by the last callback received**."*

### 3.3 A P11 position is materially qualified — `SRP-06`

P11 endorsed, from Wave A, *"bank-reconciliation completeness gates period locking — adopt and
generalise"*, calling it *"the one good pattern in the area"*.

`P06` `A6` and its AAS+ escalation qualify it decisively: *"the sharper reading is not 'corrections
after close are possible' but **'a signed-off bank reconciliation is not a durable fact.'**"*

**These are not contradictory** — the lock performs a point-in-time completeness check, and nothing
afterwards preserves the result. **But `SRP-06` as P11 published it is misleading**, because it
commends a control whose output does not survive. `SRP-06` is amended: the completeness precondition
is adopted **and** the reconciliation result must be a durable, lock-aware fact.

### 3.4 New material P11 had not registered

| Source | Fact | P11 impact |
|---|---|---|
| `P04` §1.1 | **The capitalization decision has no owner at the moment it is made** — a flag on a GL account decides it; *"nobody who raises the requisition, approves the order, or receives the goods makes — or sees — the decision"* | `UBE-25` was scored `C2` **pass**. It is a `C2` **FAIL** |
| `P04` §1.1 | **No capitalization threshold, no repair-versus-improvement rule, no assets-under-construction stage**; acquisition cost is whatever the invoice line says — nothing assembles freight, installation, duty, testing or a dismantling provision | Missing business events, with `X1-F10` |
| `P04` §1.4 | **The derecognition entry is created in draft and the system never posts it.** *"An asset can read 'Closed' indefinitely while its cost and accumulated depreciation remain in the ledger"* | A new orphan-financial-fact instance under `DC-12` |
| `P04` §1.4 | **Impairment can only be recorded as accelerated depreciation, and appears in the ledger labelled as ordinary depreciation** | `DC-17` inconsistent reporting semantics |
| `P04` §1.4 | **Completing a disposal silently rewrites company-wide default gain/loss accounts** | A transaction mutating configuration — a new `C4` consumer-recreation instance |
| `P04` §1.5 | **A depreciation charge aimed at a closed period is re-dated, not refused** — *"a charge belonging to one financial year is asserted to post **seven months later, in the following year, carrying its full value with it**"* — while **the same lock hard-refuses a disposal. One module, one control, two opposite behaviours** | `PC-01`/`UAE-04` confirmed with a measured instance, and `PCP-05` gains direct support |
| `P04` §1.6 | **The asset subledger is not reconciled to the ledger; six distinct mechanisms can break agreement and nothing would detect any of them.** *"A reconciliation… must be **originated** by SMEsPlus. There is nothing to adapt"* | The subledger register's Asset row is **not** *"of record, unverified"* — it is unreconciled by construction |
| `P04` §2 | **There is no tax book and no tax written-down value**; hire-purchase acquisition has no path; destruction of goods/scrap requires approval, witnesses, an auditor as witness, written certification and **30 days' advance notice** — *"a single retire action cannot carry two different evidence regimes"* | New `P07`/`P04` statutory items; supports `X3-F14`(b)(d) |
| `P03` behaviours 2–4 | **Capitalised-but-never-relieved and relieved-but-never-capitalised residues net against each other in one account** — *"a small production-account balance is **not** evidence that costing is correct"* | A balanced-but-wrong instance at cross-process level |
| `P03` behaviour 5 | **The conversion-cost relief defaults to a cost-of-sales account** — *"cost of sales is credited in a period in which nothing was sold"* | Direct `DC-03` adjacency |
| `P03` behaviour 7 | Work orders with no recorded time are costed at **expected** duration — *"an estimate is recorded indistinguishably from a measurement, and the variance is structurally zero"* | Confirms `UAE-31`'s absence has a masking effect, not merely a gap |
| `P03` behaviour 9 | **Conversion cost is company-scoped, but the accounts for its entry are resolved against the acting user's company** — *"entries can reach the wrong legal entity's accounts"*. `Tolerance = 0` | A **`COMPANY`-scope violation on the accounting side** — the analogue of `SC-01`, and new to the scope matrix |
| `P03` §7 | **Manufacturing appears in none of the existing end-to-end processes or module specifications** — its admission to the target baseline is an open Boss/PMO item | A programme-scope gap P11 had not registered |
| `P06` `CPO-F-01` | **The `P0x` process identifiers do not exist in the canonical repository.** The repository's own `END_TO_END_BUSINESS_PROCESS_MATRIX.md` enumerates ten processes and **contains no cash, bank, payment, settlement or reconciliation process at all** — the chain terminates at *invoice* on both sides | **`P06` has no receiving specification.** With `P03` §7 this becomes a programme-level finding, below |
| `P06` `CPO-F-02` | **No Jira work item carries `P06`** — population 146 in project `ERPPLUS`, pattern match on `bank\|payment\|reconcil\|treasury\|settlement\|cash` returns **0** | The Jira evidence requirement is unsatisfiable for that process |
| `P06` `CPO-F-04` | **Twelve physical bank accounts collapse onto two general-ledger accounts**, and **two companies reuse the same journal codes**, so journal code is not a unique key across the tenant. *"The general ledger cannot answer 'what is the balance of bank account X'"* | Reconciliation must be **journal-scoped, not account-scoped**; a new scope-mismatch row |
| `P06` `F-01`…`F-20` | **20 cross-boundary facts: 8 `CONTESTED`, 4 `UNOWNED`, 1 `HOLD`** — including payment intent (four entry points, no single author), invoice payment status (two writers), and **bank confirmation state, which has no field in the system at all** | Direct input to the ownership register; and `P06` states *"no sibling package was read"*, so **P11 is the only place these can be reconciled** |

## 4. The programme-level finding this delta produces

`P03` §7 and `P06` `CPO-F-01` are independently derived, in different processes, from different
evidence, and say the same thing:

> ### The `P01`–`P11` process taxonomy does not exist in the canonical repository.
>
> The repository's own `END_TO_END_BUSINESS_PROCESS_MATRIX.md` enumerates ten processes — `E2E-001`
> … `E2E-010` — and **the chain terminates at *invoice* on both the sell side and the buy side.**
> There is **no cash, bank, payment, settlement or reconciliation process**, and **manufacturing
> appears in none of the end-to-end processes or module specifications**.
>
> Consequently `P03` and `P06` — and, by the same argument, `P01`, `P02`, `P05`, `P07`, `P09`, `P10`
> — have **no receiving specification**, and their outputs cannot be traced into the canonical
> traceability matrix without first creating the process rows.

**Registered as `P11-F-04`, `HOLD — BOSS DECISION REQUIRED`.** It is the `P11-F-01` finding
(no declared output path) one level deeper: the programme declares neither its **source root**
(`MCU-21`), nor its **output path**, nor its **process taxonomy**. Three undeclared denominators,
each found by a different route.

## 5. What this delta does NOT change

- **The event-to-GL matrix is still not filled by P11.** `P03`, `P04` and `P06` each publish their
  own event-to-GL matrix — `P06` alone carries 31 event→entry rows. **Reconciling those into the
  unified matrix is a full round of work against three packages that arrived after this session's
  synthesis was written and after its four-expert challenge was commissioned.** It has not been done,
  and no cell has been filled from them. Recorded as `P11-B-13`.
- **The recommendation.** Three packages arriving, each declaring `RECOMMEND HOLD` or handing over
  under a standing veto, with 42 blockers in one of them alone, does not move a gate toward closure.
