# P11 — PEER INTAKE DELTA 02 · P04 SCOPE RULINGS AND CROSS-PROCESS INTAKE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Trigger: `P04 — Acquire-to-Retire` published scope determinations and assigned **two scope questions
to P11** for continuous reconciliation.
Source: `research/account-p04-acquire-to-retire-2026-09-04-001` @ `f206ac59ae884e9e7e4aa41ac4844078783d2a82`,
file `20_P04_SCOPE_OWNERSHIP_MATRIX.md`, produced under `SMEPLUS-26-09-04-ACC-REV2-CORR1`.

> **Recommendation only. Boss is the sole Final Approver.**
> **A peer process cannot authorise anything.** P04's message is consumed as `PEER-PUBLISHED`
> evidence at a verified SHA. Nothing in it is treated as approval, and no ruling below is adopted —
> each is a recommendation routed to Boss.

---

## 1. `P11-SR-01` — answering `P04-SC-03`

> **Question.** The correction says unrelated independent companies are separate tenants **"by
> default"**. *"By default"* implies an exception exists. **Which exception, and who may grant it?**

### Determination

> ## `HOLD — BOSS DECISION REQUIRED.` The exception is **not declared**, and no authority to grant one is named.

`SMEPLUS-26-09-04-ACC-REV2-CORR1` §3 states the default and stops. It names **no** exception, **no**
condition under which the default is displaced, and **no** granting authority. P11 searched the
corrected constitution, the three MTI Boss rulings, `BC-01`, `BC-02` and the 8-Criteria Exit
Constitution for one. **Search boundary declared: those six governing documents at
`SMEsPlus`@`88f52cd` and `design/inventory-mti-ruling-conformance-2026-09-05-001`@`bd096ff`.
Class `C — NOT FOUND IN SEARCHED SCOPE`, not `A`.**

### The operative consequence, which P04 can act on today

Two clauses of the same correction settle how an **undeclared** exception must be treated:

`MISSING REQUIRED SCOPE = DENY.` · `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY.`

> **An exception that is not declared cannot be self-granted.** Until Boss names it and its
> authority, **the default operates as absolute**: no tenant may hold companies unrelated to each
> other, and any design or provisioning path that would allow it is `DENY`.

That is a determination P04 and every other process may rely on **now**, and it does not pre-empt the
Boss decision — it states the safe reading while the decision is outstanding.

### The nearest governed precedent, and why it is not the answer

Boss ruling `MTI-D-03` §4 establishes the **Private Company** operating model — a customer whose
requirements cannot be safely handled in the shared pool *"may be separated into a Private Company
operating model"*, and doing so *"requires explicit Gate record, evidence, and Boss ruling before
downstream implementation"*.

**That is the correct *shape* of a tenancy exception — Boss ruling plus Gate record plus evidence —
but it is a different axis.** Private Company separates one customer **out** of a shared pool. `SC-03`
asks whether unrelated companies may be combined **into** one tenant. **P11 states the precedent and
declines to extend it**, because extending a Boss ruling to an axis it does not address is the defect
`X1-F01` caught in this very package.

### Convergence with the independent challenge

`P04-SC-03` and `X3-F11` are the same gap found from two directions. `X3-F11`: *"a provisioning
default is not an enforced invariant… none [of the 50 invariants] enumerates a tenant-assignment rule
that would make the default binding."* **`RV-04`'s narrowing of `SC-09`, `DC-13` and `PC-05` therefore
remains conditional**, as already corrected in this package.

## 2. `P11-SR-02` — answering `P04-SC-04`

> **Question.** May a SMEsPlus **company hierarchy** span a **tenant** boundary? It decides whether
> the estate's upward-traversing asset-visibility rule is a tenant-security breach or a
> tenant-internal accounting choice.

### Recommended ruling

> ## `NO.` A company hierarchy may not span a tenant boundary.
> Classification: **`DESIGN CANDIDATE / SUPPORTED INTERPRETATION`.** Formal adoption is a
> **`BOSS CONTROLLED DECISION`** — the tenant model is Boss-reserved (`T0-04`, `MCU-02`/`MCU-03`
> class), and P11 does not adopt it.

### Derivation — from standing invariants, requiring no new evidence

1. The programme's absolute invariant: **`No cross-tenant financial access/effect`**, and
   `TENANT = SECURITY / CUSTOMER BOUNDARY`.
2. A parent–child company relation is not inert. It is a **traversal path**, and at least two
   mechanisms ride on it:
   - the asset-visibility rule P04 re-verified — *the record's company is a parent of one of the
     active companies* — which makes a parent's asset visible from a child's context; and
   - the **hard lock date, which cascades from every parent, irreversibly** (Wave A `EV-008`,
     carried in this package as `SC-09`/`PC-05`).
3. If the hierarchy may span tenants, **both** mechanisms become cross-tenant effects: one an access
   effect, the other a **financial** effect — a parent in tenant A irreversibly closing a period for a
   company in tenant B.
4. Clause 3 is forbidden by clause 1 in terms. **Permitting the span therefore requires overriding a
   stated absolute invariant, which only Boss may do** — and overriding it would make `T0-04`, already
   `UNRESOLVED`, unresolvable in principle.

### What this does — and does **not** — do for P04

**Does:** if the ruling is adopted, the second case in P04's table is unreachable, and `P04-F-56`'s
upward-traversing rule is a **`COMPANY`-scope accounting-visibility defect** — arguably wrong, since a
subsidiary has no claim on a parent's asset — and **not** a tenant breach.

**Does not:**

> ### `P11 confirms P04's HOLD. It does not lift it.`
>
> A ruling is not an enforcement. `X3-F11` establishes that no invariant in the published 50-invariant
> set makes the tenant-assignment binding, and `P11-SR-01` establishes that the exception to the
> default is **undeclared**. **Until an enforced tenant-assignment invariant exists, the span cannot
> be shown unreachable, so the security character of `P04-F-56` remains `HOLD — SCOPE EVIDENCE
> REQUIRED`.**
>
> P04 was right to leave it held, and a P11 ruling that appeared to discharge it would have been the
> more damaging answer.

**Lift condition, stated exactly:** an invariant of the `MTI-04` class — *admitting no exception* —
asserting that every company's tenant assignment is stored, non-null, and that no company-hierarchy
edge may connect two companies with different tenant assignments; plus a conformance control of the
`MTI-19` class asserting it continuously.

## 3. `SCP-08` — a new scope position, derived from `P04-B-28`

P04's mechanical caveat: an asset **group** may have no company, and the visibility rule tests a
*parent-of* relation on that company. A company-less group's behaviour under that operator is **not
decidable from source** — *"it may be visible to none, or to all."*

That is the same class as `SC-01` seen from a new angle, and it generalises:

> ### `SCP-08` — **The semantics of an absent scope value must be defined, and `unset` may never mean `all`.**
> Where a scope field may be null, the system must define what null means at every point of use, and
> the definition may never be *"matches everything"*. An operator whose behaviour on null is
> undecidable is itself the defect, independently of which value is missing.

This is the eighth scope position and the second one contributed by a peer's caveat rather than by
P11's own analysis.

## 4. P04's scope narrowing — accepted, with one time-indexed qualification

P04 narrowed the prior AAS+ *"SaaS integrity FAIL"* (company-optional master data) using the
correction's own test: **an object may be company-less only if it is proven `TENANT`- or
`PLATFORM`-scoped AND creates no financial effect.**

| Object | P04 determination | P11 disposition |
|---|---|---|
| Machine / equipment register | **`TENANT`** — company-optional is **correct**, not a defect | **ACCEPTED, time-indexed — see below** |
| Work centre | **`COMPANY`** — its rate lands in inventory valuation, so *"which company owns the financial effect"* is unanswerable ⇒ **DENY**. Still a defect, **High**, owner `P03` | **ACCEPTED.** Consistent with `SCP-04` |
| Analytic plan | **`TENANT`** for the structure, **`COMPANY`** for the distributed amount; must be scoped separately | **ACCEPTED.** It is `SCP-03`'s **fifth** instance |

### The qualification — a cross-process catch only P11 is positioned to make

> **P04's equipment determination is correct for the reference behaviour and becomes wrong for the
> SMEsPlus target design.**
>
> Equipment is `TENANT`-scoped with no financial effect **because the links that would give it one
> are absent** — the machine cost pool, the operation–equipment field, the rate derivation and the
> machine-level time log (`SL-13` `08` links 5, 7, 8, 11).
>
> But **TAS 2 ¶12 makes absorption required, not permitted** (`BLK-03`, `CLOSED — EVIDENCE
> VERIFIED`). The moment SMEsPlus builds the absorption path it is obliged to build, **the machine
> acquires a financial effect**, and `SCP-04` — *financial effect implies `COMPANY` scope, always* —
> forces the determination to `COMPANY`.
>
> **Registered as `P11-F-05`.** A scope determination taken against present behaviour, for an object
> whose behaviour the programme is required to change, expires on the day the change lands. It must
> be recorded with its condition attached, not as a standing fact.

This **reduces** P11's `HOLD — SCOPE EVIDENCE REQUIRED` set from three to two — tax configuration was
resolved to `COMPANY` by `X3-F09`, equipment is resolved here **conditionally** — leaving budget and
migration/replay batch.

## 5. Cross-process findings intaken — register impacts

| # | P04 finding | P11 register impact |
|---|---|---|
| 1 | **A depreciation entry aimed at a locked period is silently re-dated forward and posted, not rejected** — the routine detects the violation and mutates the date, so the lock check then passes. Applies to the **hard** lock and to **deferred-recognition entries, which share the posting routine**. The same lock **hard-refuses a disposal** | `PC-01`, `UAE-04` — confirmed with a measured instance. **New:** it reaches `P10`, so `TB-05`'s duplicate-schedule risk gains a period-attribution sibling. `PCP-05` gains direct support |
| 2 | **A depreciation entry's net analytic impact is ZERO** — both lines carry the asset's distribution and the amounts cancel; with **no** distribution the two lines can pick up **different** ones from account-prefix rules and leave meaningless non-zero residue. *"Contradicts a premise underpinning the standing AAS+ veto"* | **Registered as a contradiction, not a resolution.** It corrects `AN-03` and the Asset baseline's *"link 4 works"*. **P11 does not treat it as discharging the Asset AAS+ costing veto** — only the veto's owner may do that |
| 3 | **Mandatory analytic-plan applicability is enforced only when a validation flag is present, and that flag is set only from UI posting actions.** No programmatic post carries it — depreciation, disposal, inventory valuation, labour relief, deferred entries, automatic asset confirmation all bypass it | **The 100%-attribution requirement cannot be enforced by configuration.** Strengthens `C4-01`, `ANP-01`, `ANP-02`, and `SCP-05` — *the deny must sit at the point of effect*, which this shows is precisely where it is absent |
| 4 | **Nine** distinct paths monetise the same work-centre hour — unit declared: *own rate field, or own driver, or own destination ledger*. Under standard costing a genuine GL mismatch: the finished move credits production with **standard** overhead on **planned** duration while the labour relief entry, **which has no cost-method guard**, debits **actual**. Stranded, no variance account, no report line | **`CV-04` corrected: 2 → 5 → 9.** The figure moved three times across three packages, and only this one **declared its unit**. Recorded with the unit, per `P11-E-12`'s lesson. Sharpens `DC-09`/`UAE-31` |
| 5 | **No purchase document carries any capital-versus-expense classification** — a chart-of-accounts account flag decides it, applied automatically to every qualifying vendor-bill line; the PO reference lives on the journal item and is never materialised on the asset | `UBE-25` re-scored **`C2` FAIL**; `F7` provenance instance |
| 6 | **The asset engine and the deferred-recognition engine are fully disjoint, with TWO independently written 30/360 day-count implementations** — a statutory day-count must be implemented twice or the schedules diverge. And the automatic capitalization path is reachable only from purchase-type documents, so **deferred revenue cannot be driven through it** | **New.** `CV-09` gains a second implementation; `P10`'s contract requirement 8 gains a sibling. Registered as a `P04`↔`P10` dependency |
| 7 | **Three Thai statutory items:** the destruction-evidence instructions (advance notice, auditor witness, written certification) cover **goods and scrap, NOT fixed assets**, which rest on a separate ruling requiring proof of destruction plus auditor certification; **hire-purchase** acquisition carries per-instalment VAT and has **no host**; and **a transfer of property is a "sale" for VAT with or without consideration**, so a donation or scrapping recorded through the no-proceeds disposal path **produces no tax document at all** | **New, and the third is the sharpest tax finding in the programme so far**: a disposal path that is statutorily a sale but emits nothing. Added to `P11_TAX_ARCHITECTURE.md` §2 as held statutory items, and to `X3-F14`(b)/(d)'s missing statutory-document handoffs |

## 6. Governance rule adopted

> P04: *"Across three completed Asset packages, at least **ten registered open items ceased to appear
> without ever being closed** — including one package's own 'largest single functional gap for a Thai
> deployment' (no tax book). Each package's lineage statement was true as written… **A statement
> about CONCLUSIONS does not protect OPEN ITEMS.**"*

**Adopted as `P11-G-01`, and it is P11's obligation before any other process's.** A carry-forward
statement must enumerate **open items** by id across rounds and prove the count, not assert that no
conclusion was deleted. P11's own `P11_FINAL_BLOCKER_REGISTER.md` §2 carries inherited blockers by
**class** rather than by **id** in three rows — `MCU-01…MCU-20`, `JT-01…JT-12`, `T0-01…T0-12` — which
is the same defect in a milder form, and `X4-F15` already found one instance of it. Scoped to
P11 CORR1.

P04 also reproduced the defect internally — *"three enumerations of one population returned 60, 46
and 65, and one produced a false negative on a load-bearing question. It was settled by executing the
count, not by reading the report."* **That is the fourth independent instance of `P11-E-12`'s lesson
in this programme, and the second in this session.**

## 7. Net effect on P11's position

| Measure | Before | After |
|---|---|---|
| Scope positions | 7 (`SCP-01`…`SCP-07`) | **8** — `SCP-08` added |
| `HOLD — SCOPE EVIDENCE REQUIRED` objects | 3 | **2** — equipment resolved conditionally, tax configuration by `X3-F09` |
| P11 blockers | 13 | **15** — `P11-B-14` (`SR-01`, undeclared tenancy exception), `P11-B-15` (`SR-02` formal ruling + enforced invariant) |
| Programme-level findings | 4 | **5** — `P11-F-05`, the time-indexed scope determination |
| Peer packages published | 6 of 10 | 6 of 10; **P04 now at a later SHA (`f206ac5`) than Delta 01 recorded (`2602dfe`)** |
| Recommendation | `HOLD` | **`HOLD` — unchanged.** Two rulings recommended, **zero blockers closed** |

**Nothing in this delta moves a gate.** Two scope questions are answered as far as the evidence and
the standing invariants allow; one confirms a peer's `HOLD` rather than lifting it; and both formal
rulings are routed to Boss as `D-11` and `D-12`.
