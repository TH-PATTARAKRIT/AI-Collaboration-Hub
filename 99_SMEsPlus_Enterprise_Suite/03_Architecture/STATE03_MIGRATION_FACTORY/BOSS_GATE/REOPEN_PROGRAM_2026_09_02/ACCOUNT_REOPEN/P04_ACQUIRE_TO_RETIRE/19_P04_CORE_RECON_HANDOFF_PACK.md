# 19 — P04 CORE ACCOUNTING RECONCILIATION HANDOFF PACK

**Layer 1 — clean-room business learning.**
This is the only file in this package cleared to seed downstream SMEsPlus design
material. It contains no vendor model, field, file or menu names. A mechanical
token scan is recorded in `17_P04_PMO.md`.

Process: **P04 — Acquire-to-Retire.**
Terminal status: **READY FOR CORE ACCOUNTING RECONCILIATION.**
**No asset final freeze is declared. No approval, no authorisation to develop.**

---

## 1. What P04 established

### 1.1 The capitalization decision has no owner at the moment it is made

A fixed asset comes into existence from a **posted supplier invoice**, or from
journal entries an accountant selects by hand. It does **not** come into
existence from the purchase order and it does **not** come into existence from
the goods receipt. The purchasing documents carry **no capital-versus-expense
classification of their own**.

What decides capitalization is a **flag on a general-ledger account**, set once
by an accountant, applied automatically thereafter to every qualifying invoice
line. Nobody who raises the requisition, approves the order, or receives the
goods makes — or sees — the decision.

Three further consequences, each verified:

- There is **no capitalization threshold and no repair-versus-improvement rule**
  anywhere. Nothing distinguishes a repair from an improvement.
- There is **no assets-under-construction stage**. An asset either does not exist
  or exists at its full cost. Self-built plant has nowhere to accumulate.
- **Acquisition cost is whatever the invoice line says.** Nothing assembles a
  cost from several documents — freight, installation, import duty,
  non-recoverable input tax, testing, or a dismantling provision.

### 1.2 The link back to the purchase is not durable

The reference to the purchase order lives on the **accounting line**, never on
the asset. Answering *"which purchase produced this asset"* requires a two-step
traversal that is nowhere stored, and that is lost outright if the asset is
duplicated or created without its source lines.

The programme's own rule — *always trace a financial fact to its initiating
business event* — is therefore **not satisfiable from stored data** for assets in
the reference behaviour. SMEsPlus must store the reference, not derive it.

### 1.3 Buying a machine creates two records that never meet

An accounting asset is created from the supplier invoice. An operational
equipment record is created from the goods receipt. **They are not linked** in
the reference product, and the project's own attempt to link them is largely
inactive. Two separate custom paths create equipment from stock movements; none
of them creates or links an asset.

The divergence runs in both directions: it exists at acquisition, and it exists
at retirement — **retiring an asset does not retire its equipment.**

There is a third break behind them: the operational routing step references a
**work centre** and nothing else. It cannot say **which machine** performed the
work. This is the structural basis of the Boss's long-standing concern, and it is
confirmed.

### 1.4 Retirement is where the accounting is weakest

- The **derecognition entry is created in draft and the system never posts it.**
  The asset is marked closed first. An asset can read "Closed" indefinitely while
  its cost and accumulated depreciation remain in the ledger.
- There is **no transfer**, **no impairment**, **no scrap distinct from disposal**
  and **no partial disposal**.
- An impairment can only be recorded as **accelerated depreciation**, and appears
  in the ledger **labelled as ordinary depreciation**.
- Gain and loss on disposal go to **one account each per legal entity**, for every
  asset class. They cannot be segregated by class or by administrative-versus-
  production use.
- Completing a disposal **silently rewrites those company-wide default accounts**.
- The disposal date is a free field defaulting to today, with **no link to the
  transfer of control**.

Measured against the Thai standard on property, plant and equipment: of seven
derecognition requirements, **one is met, two are partly met, and four have no
host in the reference behaviour**. Four require new design, not configuration.

### 1.5 A depreciation charge aimed at a closed period is moved, not refused

This is the most immediately consequential operational finding.

When a depreciation entry is posted into a period that is **locked**, the system
**changes the entry's date** to just after the lock and posts it there. The lock
check then passes, because the date has already been altered. The reference
product's own test asserts this behaviour: a charge belonging to one financial
year is asserted to post **seven months later, in the following year, carrying
its full value with it**.

The same lock date **hard-refuses** a disposal. One module, one control, two
opposite behaviours.

For SMEsPlus this is a policy decision that must be taken deliberately:
**refuse, or re-date.** Silently re-dating misstates the year.

### 1.6 The asset sub-ledger is not reconciled to the ledger

Creating an asset does **not** touch the accounting line it came from; the two
are joined by a reference table, not by a balancing entry. Six distinct
mechanisms can break the agreement between the asset register and the ledger
balances, and **nothing in the reference behaviour would detect any of them**.

A reconciliation between the asset register and the general ledger must be
**originated** by SMEsPlus. There is nothing to adapt.

### 1.7 Machine cost does not reach product cost — and the paths that exist do not agree

Thai accounting standards **require** the depreciation of production equipment to
enter the conversion cost of inventory. In the reference behaviour:

- **No route feeds a machine's depreciation into the work-centre rate.** That rate
  is a number a human types.
- The route everyone believed existed — attribution through the cost-centre
  dimension — **nets to zero**. Both sides of a depreciation entry carry the same
  attribution and the two amounts cancel. Depreciation reaches the cost centre and
  immediately leaves it.
- Where an asset carries **no** attribution, the two sides can pick up
  **different** attributions and leave a meaningless residue.

Separately, and independently of depreciation, the same machine hour is
monetised by **as many as five different routines** — and they do not reconcile
with one another. Under one supported costing configuration there is a **genuine
ledger mismatch** between the planned overhead credited to production and the
actual overhead debited back, with **no variance account and no report that shows
it**.

### 1.8 The requirement that every depreciation charge be attributed cannot be enforced by configuration

Two findings together:

- Capitalizing an **addition** to an existing asset creates a new depreciable
  record **with no cost attribution at all** — so every subsequent charge on that
  addition is unattributed by construction.
- The obvious control — making cost attribution mandatory — **does not apply to
  any automatically generated entry**, including every depreciation entry.

Meeting the 100 %-attribution requirement therefore needs behaviour SMEsPlus
originates. It is not a setting.

## 2. What Thai law and standards require that the reference behaviour does not provide

| Requirement | Status |
|-------------|--------|
| Depreciation of production equipment must enter inventory conversion cost | **Required.** No mechanism exists |
| Fixed overhead absorbed on **normal capacity**; the per-unit charge may not rise as output falls; the unabsorbed remainder is a period expense; planned maintenance sits inside normal capacity | **Required.** No normal-capacity mechanism exists anywhere |
| Depreciation may not be stopped merely because an asset is idle or withdrawn from routine use — **unless it is already fully depreciated** | The reference product's pause function has no accounting justification for an idle owned asset |
| Under a usage-based method, a period charge of **zero when there is no production** is expressly contemplated | Available in principle; requires an expected-output estimate the business does not maintain |
| Derecognise when **no future economic benefit is expected**, not only on disposal | **No such trigger exists** |
| Impairment, derecognition and third-party compensation are **separate events, separately recorded** | Impairment has no host and is recorded as depreciation |
| Useful life and residual value reviewed **at least at each financial year end** | No mechanism exists |
| Significant components depreciated separately | No component concept exists |
| Destruction of a **damaged fixed asset**: the loss is deductible where destruction is **proved** and the **auditor certifies** it | The retire event must carry evidence and a certification artefact. It carries neither |
| Destruction of **goods and scrap**: approval, witnesses, an auditor as witness, written certification, and **30 days' advance notice** to the tax authority | A single retire action **cannot carry two different evidence regimes**. Scrap must be a distinct event |
| Acquisition by **hire purchase or instalment**: a tax invoice on each instalment due date; tax computed per instalment | No acquisition path exists for this ordinary Thai purchase form |
| Tax depreciation is capped by statutory **ceilings**, so book and tax figures diverge by design | **There is no tax book and no tax written-down value.** The reconciliation is external and manual |

Two statutory questions are deliberately left open and routed to the
Accounting-Tax track rather than answered by inference: whether the 30-day
notice regime reaches fixed assets, and the tax treatment of a gain on disposal.

## 3. What Core Accounting Reconciliation should take from P04

| # | Item | Why it is a reconciliation matter |
|---|------|-----------------------------------|
| 1 | **Asset register to ledger reconciliation** | It does not exist, six ways to break it are verified, and none is detected |
| 2 | **Locked-period policy: refuse or re-date** | The current behaviour silently moves a charge into the wrong financial year |
| 3 | **Automatic posting of the derecognition entry** | Otherwise a closed asset's cost stays in the ledger indefinitely |
| 4 | **One mechanism for machine cost into product cost** | Up to five monetisations of the same hour, plus a live ledger mismatch under one costing configuration |
| 5 | **Attribution of capitalized additions** | Unattributed by construction, against a standing requirement that everything be attributed |
| 6 | **Gain and loss segregation on disposal** | One account pair per entity cannot support class-level or production-versus-administrative reporting |
| 7 | **Tax book** | Without it the entity cannot compute its own tax position |
| 8 | **Evidence and certification at retirement** | A statutory deduction depends on proof the system does not capture |

## 4. Open decisions reserved to the Boss

1. The absorption denominator — normal capacity or actual hours — with a **third
   option now available**: a usage-based depreciation charge absorbed at normal
   capacity, which satisfies both standards and makes an idle month's charge
   genuinely zero. It requires an expected-output estimate per asset and has tax
   consequences that are unresearched.
2. Whether maintenance splits into planned and unplanned.
3. Whether the derecognition entry posts automatically.
4. Whether scrap is a retire event distinct from disposal.
5. Whether a capitalization threshold policy is adopted, and at which ownership
   level it lives.
6. Whether the asset template is owned by the customer account or by the legal
   entity — the template carries the depreciation method and duration, which are
   accounting-policy elections of the legal entity.

## 5. Standing controls that are **not** discharged

- The independent-challenge **veto on starting costing implementation** stands.
  Its second condition — proving that exactly **one** mechanism carries machine
  cost into product cost — is **wider** after this work, not narrower.
- The governance condition attached to the previous gate stands.
- **No asset final freeze is declared.**

## 6. One governance lesson worth carrying beyond P04

Across three completed research packages, **at least ten registered open items
stopped appearing without ever being closed** — including the item one package
called the largest single functional gap for a Thai deployment. Each package's
own lineage statement was **true as written**: no conclusion was deleted and none
was promoted without evidence. The residue happened anyway, because a statement
about **conclusions** does not protect **open items**.

The same defect reproduced inside this single piece of work: three independent
counts of one population returned three different totals, and one produced a
false negative on a load-bearing question. It was caught by executing the count
rather than reading the report.

**Carry-forward must track open items, not only conclusions — and a denominator
must be executed, not quoted.**
