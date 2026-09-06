# P04 — SMEsPlus FUNCTIONAL DESIGN INPUT PACK

**LAYER 2 — AUDIT QUARANTINE.** Prompt §11. **Design input only.**
**This pack authorises nothing.** No schema, no API, no UI, no GL account, no production
design is frozen here. Object names are **placeholders for a business concept**, not proposed
technical names. Boss remains Sole Final Approver.

**Every entry carries exactly one label:**
`FACT-SUPPORTED FUNCTIONAL REQUIREMENT` · `BOSS-APPROVED POLICY INPUT` · `DESIGN CANDIDATE` ·
`UNRESOLVED — DECISION/EVIDENCE REQUIRED`

**Reading rule.** A `FACT-SUPPORTED FUNCTIONAL REQUIREMENT` states what the examined estate
demonstrably does — it is **not** an instruction that SMEsPlus must do the same. Benchmark
behaviour is never automatically canonical (prompt §3).

**Source basis for every fact below: series 18 reference tree + `18.0.x` custom addons; runtime
facts are per-identity with the series named.** The v16 deployment's source is unobtainable on
this host (`MD-P04-01`) — no fact here is asserted of it.

---

## DF-01 · Depreciation Policy (Asset Model)

| | |
|---|---|
| **Business purpose** | Hold a reusable depreciation policy so like assets are treated alike |
| **Trigger / event** | Accountant defines or edits a policy |
| **Actors** | Accounting policy owner (define), asset creator (apply) |
| **Preconditions** | Company chosen; accounts and journal exist |
| **Lifecycle** | Draft → in use → superseded. **No versioning exists in the estate** |
| **Inputs / outputs** | In: method, duration, period, declining factor, prorata type, three accounts, journal, analytic distribution, not-depreciable %. Out: values applied to an asset |
| **Core data semantics** | In the estate a "model" is **an asset record in `state='model'`**, not a separate entity |
| **Accounting effect** | None directly; supplies the accounts an asset will post to |
| **Management / analytic** | Supplies a default analytic distribution |
| **Scope** | **COMPANY** — enforced by domain on the asset's `model_id` |
| **Controls** | *(estate)* none beyond the domain |
| **Correction / reversal** | Editing a policy does **not** restate existing assets — except the not-depreciable percentage, which **does** flow through live |
| **Period / lock** | none |
| **Cross-process** | P08 (chart), P07 (tax method admissibility) |
| **Evidence** | `CQ-P04-01`; `P04-F-145`, `P04-F-146` |
| **Open choices** | See DF-02 |
| **UI implication** | A policy register distinct from the asset register |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — a reusable depreciation policy object exists
> and is applied to assets.

## DF-02 · Policy application and propagation

| | |
|---|---|
| **Estate behaviour** | **Ten fields copied by an `onchange`; one field (`salvage_value`) a live computed reference; `create()` copies nothing.** The policy is applied by **three call sites** — the form, an explicit post-create call in the automatic capitalisation path, and the test suite — **not by the record** |
| **Consequence** | Any **fourth** creation path — import, API, automated action, custom module, migration — yields an asset with **empty accounts and journal**, which later **silently drops a ledger leg** |
| **Evidence** | `CQ-P04-01`; `P04-F-145`, `P04-F-146`, joined to `P04-F-23` |

> **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`.** Three mutually exclusive designs, none
> derivable from evidence:
> **(a)** snapshot at creation, applied on **every** write path, never propagating afterwards;
> **(b)** live reference, so a policy edit restates future schedules of linked assets;
> **(c)** snapshot with an explicit, audited *"re-apply policy"* action.
> **What is not in question:** the current mixture of (a) and (b) **on different fields of the
> same object, silently**, is not a design any of the three would produce.

## DF-03 · Financial Asset Record

| | |
|---|---|
| **Business purpose** | Carry cost, depreciation schedule and book value of a capitalised item |
| **Trigger** | Posted vendor bill or manually selected posted journal item — **never** the PO, the receipt, or the product |
| **Actors** | Accountant |
| **Preconditions** | A posted journal item on an account flagged for asset creation |
| **Lifecycle** | `draft → open → (paused) → close`; `model` is a separate use of the same object |
| **Accounting effect** | Periodic entry: **Dr** depreciation expense, **Cr** accumulated depreciation |
| **Management / analytic** | Distribution copied to **both** legs → **nets to zero** |
| **Scope** | **COMPANY** |
| **Controls** | Three of four determining values are enforced by the **interface only** |
| **Correction / reversal** | Disposal **raises** on a locked date; account re-assignment **silently skips** locked moves |
| **Period / lock** | Two different lock behaviours in one module (`P04-F-155`) |
| **Cross-process** | **P01** (acquisition lineage), P08, P07 |
| **Evidence** | base package `P04-F-01`…`P04-F-11`; `P04-F-155` |
| **UI implication** | Asset register with schedule; policy applied at creation |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** for the record and its posting shape.
> **`UNRESOLVED`** for whether capitalisation may originate anywhere other than a posted
> vendor bill — the estate has no capitalise-vs-expense decision point at all (`P04-B-06`,
> `P04-BD-08`).

## DF-04 · Operational Equipment Record

| | |
|---|---|
| **Business purpose** | Track a physical unit for operations and maintenance, **whether or not it is a financial asset** |
| **Trigger** | **Validating a goods receipt** for a product flagged *Is Equipment* with a per-move opt-in |
| **Actors** | Warehouse (create), maintenance (operate) |
| **Preconditions** | Product `type='consu'`, `tracking='serial'`, equipment flag set |
| **Lifecycle** | `eqp` → `tass`, **one-way, no reverse anywhere in either custom tree** |
| **Accounting effect** | **None** |
| **Management / analytic** | One `Float` cost field; **no ledger, no analytic, no cost object** |
| **Scope** | **COMPANY** |
| **Evidence** | `CQ-P04-04`; `P04-F-150`, `P04-F-152` |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — equipment without an asset is supported,
> automatic and the default path.
> **`BOSS-APPROVED POLICY INPUT`** — *"Equipment may exist without being a financial Asset."*
> **Already satisfied by the estate**; carried so the design does not regress it.

## DF-05 · Asset ↔ Equipment Association

| | |
|---|---|
| **Estate behaviour** | One custom `Many2one` **asset → equipment**; no reverse field; **no cardinality constraint**; **no company domain**; validation flips equipment to *To Assets*, **irreversibly** |
| **Dead code alongside it** | A duplicate older link file inheriting a model that does not exist, unreachable because it is not imported |
| **Evidence** | `CQ-P04-03`; `P04-F-148`, `P04-F-149`, `P04-F-156` |

> **`UNRESOLVED — DECISION/EVIDENCE REQUIRED`**, four separable decisions:
> **(i)** cardinality — may several assets reference one equipment? *(blocks `CQ-P04-05`'s
> reconciliation invariant if unresolved)*;
> **(ii)** reversibility — must there be a release path, and does disposal trigger it?;
> **(iii)** company constraint — pending the record-rule check `P04-B-54`;
> **(iv)** whether the association is an **event with a period** or a **static pointer**.
> **`DESIGN CANDIDATE`** — an association with validity dates rather than a pointer, which
> makes (ii) and (iv) fall out together.

## DF-06 · Depreciation Schedule / Event

| | |
|---|---|
| **Trigger** | Board computation at asset validation; posting per period |
| **Core semantics** | Two day conventions plus *no proration*; the non-daily branch is **30/360 with real-length boundary scaling**, not plain 30/360 |
| **Deployed reality** | **683 of 685** (v16) and **375 of 388** (v18) assets on **daily computation** — the **non-default** setting |
| **Accounting effect** | Dr expense / Cr accumulated |
| **Period / lock** | End-of-life clamp prevents overshoot |
| **Evidence** | `CQ-P04-02`; `P04-F-147` |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — a schedule with a selectable day convention.
> **`UNRESOLVED`** — which convention SMEsPlus adopts as **its** default. The estate's near-
> unanimous use of daily is a **configuration fact, not a legal requirement**; the statutory
> question is **P07's** and the gazetted TAS 16 text is still unretrieved (`P04-B-30`).

## DF-07 · Equipment Usage Event

| | |
|---|---|
| **Business purpose** | Record that a **specific** equipment was **actually used**, so cost can follow use |
| **Trigger** | Manufacturing execution records the use |
| **Actors** | Production (producer), asset costing (consumer) |
| **Core semantics** | equipment · operation · MO · driver quantity · period |
| **Accounting effect** | None itself; it is the **input** to DF-08 |
| **Scope** | **COMPANY** |
| **Producer / consumer** | **P03 / MRP produces, P04 consumes** — the interface contract, not an implementation |
| **Evidence** | **Absent from the estate.** P03 `CQ-P03-06` and P04 `CQ-P04-07`, both series 18 |

> **`DESIGN CANDIDATE`.** Nothing to configure; this is a build.
> **`BOSS-APPROVED POLICY INPUT`** — *"Work Center membership alone is NOT evidence of machine
> cost absorption"*, and the target causality *Routing → Operation → Equipment Actually Used →
> Equipment Usage Cost → MO/WIP/FG*.
> **Prohibited by measured evidence, not by preference:** deriving machine usage from human
> time logs. P03 measured that an unattended machine generates no cost and two operators on one
> machine generate two machine-hours.

## DF-08 · Productive Usage Allocation

| | |
|---|---|
| **Business purpose** | Move the productive share of a period's depreciation into WIP/FG |
| **Trigger** | Period close, or per usage event |
| **Preconditions** | DF-07 exists; the **denominator is chosen**; DF-05 cardinality is resolved |
| **Accounting effect** | Depreciation expense relieved into inventory value — **a real GL effect, therefore Boss- and P08-gated** |
| **Scope** | COMPANY |
| **Evidence** | No path exists: **0 of 4 deployments** carry any machine cost into finished goods (P03) |

> **`BOSS DECISION REQUIRED`** — `BLK-07` / `P04-BD-05`. Drivers permitted by policy: **Machine
> Hour / Work Centre Hour / Production Quantity, with no mandatory default.**
> **`DESIGN CANDIDATE`** for the mechanism, conditional on that decision.

## DF-09 · Non-Productive Cause Attribution

| | |
|---|---|
| **Business purpose** | Attribute the non-productive share to a **named** operational cause |
| **Trigger** | Period close |
| **Core semantics** | Cause taxonomy — idle, maintenance, breakdown, changeover, unallocated capacity |
| **Accounting effect** | Period expense with a named cause, **never** into inventory |
| **Evidence** | Causes exist only as work-centre loss reasons; **no join to an asset**; maintenance cost never reaches a ledger |

> **`BOSS-APPROVED POLICY INPUT`** — *"no unclassified depreciation."*
> **`DESIGN CANDIDATE`** for the taxonomy and the join.
> **`UNRESOLVED`** — whether "unallocated capacity" is a cause of its own or the residual of
> DF-08's denominator choice. **It cannot be answered before `BLK-07`**, which is why it is not
> guessed here.

## DF-10 · Managerial / Off-Balance Internal Usage Tracking

| | |
|---|---|
| **Business purpose** | Keep charging internal usage after financial depreciation ends, without touching financial truth |
| **Trigger** | `value_residual = 0` **and** equipment still operational |
| **Core semantics** | Managerial pool; residual is a **reference, not a cap**; financial residual is **not consumed** |
| **Accounting effect** | **Off-balance to off-balance only.** Never cross-posted into financial WIP |
| **Hard constraint** | **`account.asset` cannot post to an off-balance account — all three of its account fields exclude that type by domain (`P04-F-154`).** A managerial ledger **cannot** be a configuration of the asset object |
| **Evidence** | `CQ-P04-06`; `P04-F-154` |

> **`BOSS-APPROVED POLICY INPUT`** for the principles.
> **`DESIGN CANDIDATE`** for a separate managerial mechanism.
> **`UNRESOLVED`** — the rate basis (original daily ratio / replacement / policy), whether the
> pool reconciles or is purely statistical, the off-balance chart structure (**P08**), and
> whether the asset or the equipment owns the managerial life (depends on DF-05(i)).

## DF-11 · Analytic Allocation

| | |
|---|---|
| **Estate behaviour** | Distribution written to **every** line of the depreciation entry → charge and contra on the same analytic account → **nets to zero**. Only on **draft** moves, only inside `write()` |
| **Evidence** | `CQ-P04-09`; `P04-F-153` |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — an analytic dimension exists and reaches
> depreciation entries.
> **`BOSS-APPROVED POLICY INPUT`** — analytic distribution must not be omitted from
> non-production and management-cost design.
> **`DESIGN CANDIDATE`** — analytic applied to the **expense leg only**, so the analytic
> account carries the cost rather than zero. **Stated as a candidate, not a bug fix**: netting
> both legs is defensible for a balance-sheet view, and which is wanted is a design choice.

## DF-12 · Maintenance Integration

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — maintenance requests, teams and schedules exist
> against equipment.
> **`UNRESOLVED`** — maintenance cost has **no accounting representation at all** (one `Float`,
> no ledger, no analytic). Whether SMEsPlus gives it one is a design decision with a **P05**
> dependency (vendor/repair expense) and a **P08** dependency (chart).

## DF-13 · Disposal / Derecognition

| | |
|---|---|
| **Estate behaviour** | `set_to_close` raises before the lock date, closes asset **and children**, builds disposal moves, distinguishes *sold* from *disposed* by whether invoice lines were supplied |
| **Known defects carried** | Derecognition entry left in **draft** and **silently deletable**; a blank account **drops a leg**; **equipment is never released** |
| **Evidence** | `CQ-P04-10`; base package; `P04-F-149`, `P04-F-155` |

> **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`** — disposal and sale are distinguishable events
> with dated derecognition.
> **`UNRESOLVED`** — whether derecognition must post automatically (`P04-BD-06`, recommendation
> on file, **not** approved), whether scrap is a distinct event (`P04-BD-07`, same), and whether
> disposal releases the equipment.

---

## Cross-cutting design inputs

| Input | Label | Note |
|---|---|---|
| Financial depreciation ≠ managerial/internal usage allocation | **BOSS-APPROVED POLICY INPUT** | Two truths; DF-10 keeps them apart |
| Off-Balance is an Account Type; off-balance pairs with off-balance | **BOSS-APPROVED POLICY INPUT** | **Constrained by `P04-F-154`** |
| Asset Model defines calculation policy, **not** production placement/routing | **BOSS-APPROVED POLICY INPUT** | Consistent with DF-01/DF-07 |
| Scope determined per object — PLATFORM / TENANT / COMPANY | **BOSS-APPROVED POLICY INPUT** | `CORR1`; `CQ-P04-11` |
| Capitalise-vs-expense threshold and its scope | **UNRESOLVED** | `P04-BD-08`; no decision point exists in the estate |
| Asset model = tenant template or company accounting truth | **UNRESOLVED** | `P04-BD-09` |

## What this pack deliberately does not contain

No schema, no field names, no API surface, no menu tree, no GL account numbers, no
implementation sequencing, and **no conversion of any `DESIGN CANDIDATE` into authority.**
UI implications are stated only at the functional level required by §11.
