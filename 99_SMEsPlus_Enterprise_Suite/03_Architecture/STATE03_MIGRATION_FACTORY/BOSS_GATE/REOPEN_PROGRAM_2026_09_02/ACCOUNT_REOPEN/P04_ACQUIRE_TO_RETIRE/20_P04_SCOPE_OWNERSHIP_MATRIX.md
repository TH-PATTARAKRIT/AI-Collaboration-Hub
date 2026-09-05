# 20 — P04 SCOPE OWNERSHIP MATRIX

Layer: **2 — audit quarantine**.

Produced under **`SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution
Correction**, received mid-session. This session was **not reset**; the
correction is applied forward, and the findings materially affected by the
superseded "Tenant + Company mandatory for every operation" wording are
revalidated in §4.

---

## 1. The canonical rule applied here

**SCOPE-AWARE EVERYWHERE.** Every material object and operation first determines
its applicable scope.

| Scope | Tenant context | Company context |
|-------|----------------|-----------------|
| **PLATFORM** | not required | not required |
| **TENANT** | **mandatory** | not required, unless the specific operation is company-scoped |
| **COMPANY** | **mandatory** | **mandatory** |

Missing required scope = **DENY**. Required ownership cannot be proven = **DENY**.

Definitions applied: **TENANT** = security / customer boundary. **COMPANY** =
legal / accounting / business boundary. Ownership ≠ availability. Ownership
scope ≠ operational ≠ financial ≠ reference scope. Multi-tenant membership ≠
multi-tenant execution context. Unrelated independent companies = **separate
tenants by default**.

## 2. The eight questions, answered for every material P04 object

Columns: **OWN** owns · **EXEC** executes · **ACC** may access · **MUT** may
mutate · **REF** may reference · **FIN** creates a financial effect · **FIN-CO**
which company owns that effect · **CLASS** platform reference / tenant-owned /
company legal-accounting truth.

### 2.1 The asset record and its immediate family

| Object | OWN | EXEC | ACC | MUT | REF | FIN | FIN-CO | CLASS |
|--------|-----|------|-----|-----|-----|-----|--------|-------|
| **Asset record** | COMPANY | COMPANY | COMPANY | COMPANY | TENANT (read-only reporting) | **Yes** — cost, depreciation, disposal | the owning company, unambiguously | company legal/accounting truth |
| **Depreciation entry** | COMPANY | COMPANY | COMPANY | COMPANY | — | **Yes** | as the asset | company legal/accounting truth |
| **Disposal / derecognition entry** | COMPANY | COMPANY | COMPANY | COMPANY | — | **Yes** | as the asset | company legal/accounting truth |
| **Asset model (template)** | **TENANT candidate** | COMPANY | TENANT | TENANT | COMPANY | No — it posts nothing | n/a | **tenant-owned policy**, instantiated per company |
| **Asset group** | **TENANT candidate** | — | TENANT | TENANT | COMPANY | No | n/a | tenant-owned grouping |
| **Capitalization designation on an account** (automation mode, attached models, split flag) | COMPANY | COMPANY | COMPANY | COMPANY | — | **Indirectly — it decides whether a financial effect is created at all** | the company owning the account | **company legal/accounting truth** |
| **Gain and loss on disposal accounts** | COMPANY | COMPANY | COMPANY | COMPANY | — | **Yes** | the company holding them | company legal/accounting truth |
| **Asset journal** | COMPANY | COMPANY | COMPANY | COMPANY | — | **Yes** | that company | company legal/accounting truth |

### 2.2 Reference and policy data P04 depends on

| Object | OWN | ACC | MUT | FIN | CLASS | Note |
|--------|-----|-----|-----|-----|-------|------|
| **Thai statutory depreciation rate ceilings** (Royal Decree No. 145 s.4–5) | **PLATFORM** | PLATFORM | PLATFORM | No | **platform reference data** | The same for every tenant and every company. A tenant may not edit it |
| **Thai statutory pro-ration rule** (Revenue Code s.65 bis (2)) | **PLATFORM** | PLATFORM | PLATFORM | No | platform reference data | as above |
| **Destruction-evidence procedure** (Revenue Department instructions, §5 of file `07`) | **PLATFORM** | PLATFORM | PLATFORM | No | platform reference data | The *procedure* is platform; the *evidence produced under it* is company |
| **Accounting policy — depreciation method and day convention** | **COMPANY** | COMPANY | COMPANY | **Yes, decisively** | **company legal/accounting truth** | This is an accounting-policy election. It belongs to the legal entity, not to the customer account. A tenant-level default is a **convenience**, not the source of truth |
| **Asset useful life and residual value** | **COMPANY** | COMPANY | COMPANY | **Yes** | company legal/accounting truth | TAS 16 requires review at least each financial year end — a company act |
| **Normal capacity** (the TAS 2 ¶13 denominator) | **COMPANY** | COMPANY | COMPANY | **Yes** — it sets what is absorbed and what is expensed | **company legal/accounting truth** | Recorded because `BLK-07` may be mistaken for an operational setting. It is an accounting estimate owned by the legal entity |
| **Internal-usage accumulator** (`BD-01`) | **TENANT or COMPANY — HOLD** | — | — | **No, by decision** — it must not alter statutory figures | see §3.2 | The `BD-01` decision makes it a management/control concept, which permits tenant ownership; but if it is ever used to price an inter-company charge it becomes company-scoped |
| **Equipment / machine record** | **TENANT candidate** | TENANT | TENANT | No, by itself | tenant-owned operational data | Operational scope ≠ financial scope. A tenant may legitimately manage a machine register across its companies |
| **Work centre and its hourly rate** | **COMPANY** | COMPANY | COMPANY | **Yes** — the rate lands in inventory valuation | **company legal/accounting truth** | The rate is a costing input with a direct financial effect. Recorded explicitly because prior evidence shows it is company-**optional** in the estate |
| **Analytic plan and distribution** | **TENANT for the plan; COMPANY for the effect** | TENANT | TENANT | **Yes, through the entries that carry it** | mixed — see §3.3 | The plan is a reporting structure; the distributed amount is a company financial fact |

### 2.3 P04 operations

| Operation | EXEC scope | Why |
|-----------|-----------|-----|
| Configure an asset model | **TENANT** | Produces no financial effect |
| Attach an asset model to an account | **COMPANY** | Decides whether a company creates assets automatically |
| Create an asset | **COMPANY** | Company financial fact |
| Confirm an asset | **COMPANY** | Posts the whole schedule |
| Post a depreciation entry | **COMPANY** | Company financial fact |
| Modify, re-evaluate, pause, resume | **COMPANY** | All post entries |
| Sell or dispose | **COMPANY** | Company financial fact; and the lock date consulted is the company's |
| Transfer between companies | **COMPANY at both ends — and it is NOT a transfer** | Prior evidence rules that across companies this is a disposal and an acquisition, not a move. That ruling is **reinforced** by the corrected constitution: a company financial fact cannot migrate between legal entities without derecognition |
| Report assets across companies | **TENANT** | Read-only aggregation; no financial effect. **This is the one place a tenant-scoped read over company data is legitimate** |
| Report assets across tenants | **PLATFORM — and it must be DENIED to any tenant** | Unrelated independent companies are separate tenants by default |

## 3. Scope determinations that could not be closed

Per the correction, these are recorded as **HOLD — SCOPE EVIDENCE REQUIRED** and
unaffected work continued.

| ID | Question | Why it is not resolvable here |
|----|----------|-------------------------------|
| **P04-SC-01** | Is the **asset model** tenant-owned or company-owned in SMEsPlus? | Business semantics point to tenant: it is a policy template that posts nothing. But it carries the depreciation **method and duration**, which are company accounting-policy elections (§2.2). The resolution is a design decision about whether the template holds a *default* or the *truth*. **HOLD — SCOPE EVIDENCE REQUIRED** |
| **P04-SC-02** | Is the **internal-usage accumulator** tenant or company? | `BD-01` makes it a management concept with no statutory effect, which permits tenant scope. If it ever prices an inter-company usage charge it becomes a company financial fact. The trigger condition is undesigned. **HOLD — SCOPE EVIDENCE REQUIRED** |
| **P04-SC-03** | May one **tenant** hold companies that are unrelated to each other? | **ANSWERED BY P11, and it remains a HOLD.** P11 (`P11-SR-01`, branch `research/account-core-reconciliation-2026-09-04-001` @ `aaa4eeb`) reports that **the exception is undeclared**: the corrected constitution states the default and names neither an exception nor a granting authority. Routed to Boss as `D-11`. **Operative consequence P04 adopts now:** under *missing required scope = DENY* and *required ownership cannot be proven = DENY*, an undeclared exception **cannot be self-granted**, so **the default operates as absolute** until the Boss names one. P04 therefore treats "unrelated independent companies are separate tenants" as an absolute rule for every determination in this matrix |
| **P04-SC-04** | Does the SMEsPlus **company hierarchy** ever span a tenant boundary? | **ANSWERED BY P11 as a recommendation, and the HOLD stands.** P11 (`P11-SR-02`) recommends **NO** — a hierarchy may not span a tenant boundary — derived from the standing "no cross-tenant financial access or effect" invariant plus the fact that a parent-child edge carries at least two traversal mechanisms. Routed to Boss as `D-12`. **P11 states explicitly that its ruling confirms this hold and does not lift it**, because no published invariant makes tenant assignment binding, so the span cannot be shown unreachable. §4.2 is updated with the lift condition and with P04's own primary-source corroboration |

## 4. Revalidation of findings affected by the superseded assumption

Only findings materially affected by the blanket "Tenant + Company everywhere"
wording are revalidated. Everything else is preserved unchanged.

### 4.1 Company-optional master data — the prior SaaS-integrity FAIL

**Original finding** (P3, AAS+ area verdict, the single FAIL): *"Company-optional
master data on equipment, work centres, bills of materials and operations, plus
an asset rule that traverses to parent companies, is not a multi-tenant-safe
foundation."* Carried as `CTR-C-10`, severity High for SaaS.

**Scope assumption used.** That every object must carry a company, because
Tenant + Company were treated as mandatory for every operation.

**Why it is over-constrained.** Under the corrected model, a company-optional
object is **not automatically a defect**. Ownership scope ≠ operational scope. An
object that is genuinely TENANT-scoped and produces no financial effect
**legitimately** has no company. The prior finding condemned a whole class of
objects on a rule that no longer applies to all of them.

**Correct scope analysis, object by object:**

| Object | Company-optional in the estate? | Correct scope | Verdict under the corrected rule |
|--------|-------------------------------|---------------|----------------------------------|
| **Equipment / machine record** | Yes | **TENANT — *conditionally, and the condition expires*** (§4.1.1) | **NOT A DEFECT TODAY.** Company-optional is correct for a tenant-scoped operational register **for as long as no absorption path exists** |
| **Work centre** | Yes | **COMPANY** — its rate has a direct financial effect (§2.2) | **STILL A DEFECT.** A company-optional object that feeds inventory valuation cannot prove which company owns the financial effect. Question 7 of the correction is unanswerable for it |
| **Bill of materials, routing operation** | Yes | **TENANT candidate** for the structure; the **valuation** it drives is COMPANY | **PARTLY A DEFECT** — the structure may be tenant-scoped; the costing consequence may not be ownerless |
| **Asset group** | Yes — company defaulted, **not required** | **TENANT candidate** (§2.1) | **NOT A DEFECT in principle**, with one mechanical caveat — see below |
| **Asset record** | **No** — company is required | COMPANY | correct as it stands |

**Updated classification.** `CTR-C-10` is **narrowed, not withdrawn**. It was
recorded at High severity across four object classes. Under the corrected
constitution it is High severity for **one** — the work centre — and the finding
is **stronger** there for being isolated: an object with a direct financial
effect and no owning company is a scope violation on the correction's own terms
(question 7 cannot be answered, therefore DENY).

Recorded as **P04-F-55**, class **FACT VERIFIED** as to the estate's behaviour,
**SUPPORTED INTERPRETATION** as to the scope assignment of each object.

#### 4.1.1 The machine register's TENANT scope is conditional and dated — adopted from P11

P11 accepted this narrowing with one qualification (`P11-F-05`), which P04
**adopts in full** because it is correct and because it changes the shelf life of
the determination:

> The machine register is TENANT-scoped **with no financial effect only because
> the absorption path is absent.** TAS 2 ¶12 makes absorption of production-
> equipment depreciation into inventory **required, not permitted** — a position
> already closed on standard text by a prior package. **On the day SMEsPlus
> builds the absorption path it is obliged to build, the machine record becomes
> the carrier of a financial effect, and the scope test forces COMPANY.**

So the determination is **correct now and expires on that change**. It is
recorded here **with its condition attached, not as a standing fact**:

| | |
|---|---|
| **Determination** | Machine / equipment register = **TENANT** |
| **Condition it rests on** | No mechanism carries machine depreciation into inventory conversion cost. Verified this session — `06` §8: no route feeds depreciation into the resource rate, and the analytic route nets to zero |
| **Expiry trigger** | The first SMEsPlus mechanism that carries machine depreciation into product cost — which TAS 2 ¶12 **obliges** the design to build |
| **Scope on expiry** | **COMPANY**, by the same test that already forces it for the work centre |
| **Consequence if missed** | A tenant-scoped, company-less object silently becomes the carrier of a company financial effect, and question 7 becomes unanswerable for it — the exact defect this narrowing corrected for the work centre would reappear on the machine |

Registered `P04-B-44`. This is the second time in this package that a scope
determination has been found to depend on the **absence** of a capability the
standard requires; the first was the work centre. **A scope matrix built against
a system that does not yet comply with the standard has a shelf life**, and
saying so is part of the determination.

**Architecture impact.** The SMEsPlus rule is not "add a company everywhere". It
is: *an object may be company-less only if it is proven TENANT- or
PLATFORM-scoped and creates no financial effect* — **and the proof must be
re-tested whenever a financial effect is added.* The work centre fails the test
today; the machine register passes it today and is scheduled to fail it.

**Cross-process impact.** P03 owns the work centre. **PEER DEPENDENCY OPEN —
P03.** P04 does not resolve it and does not stop for it.

**Evidence required.** A count of work centres and equipment records with no
company on the running system — already registered in the prior package's UAT
query set. Its priority **rises**: it is now the deciding evidence for a
narrowed, sharper finding rather than for a broad one.

### 4.2 The upward-traversing visibility rule

**Original finding** (P3): an asset rule that traverses to parent companies is
part of the SaaS-integrity failure.

**Re-verified directly this session.** Both the asset record and the asset group
carry a global visibility rule of the form *the record's company is a parent of
one of the active companies*. This makes a **parent company's asset visible from
a child company's context**.

**Correct scope analysis.**

| Case | Verdict |
|------|---------|
| Within one tenant, inside a genuine company hierarchy | A **company-scope** question, not a tenant-security question. It is an accounting-visibility choice — arguably wrong, because a subsidiary has no claim on a parent's asset — but it is **not a tenant breach** |
| Across tenants | A **tenant breach**, and would be DENY under the corrected rule |

Whether the second case is reachable depends on **P04-SC-04**, which P04 cannot
answer.

> **P04-F-56.** The upward-traversing rule is **re-classified**: it is a
> **COMPANY-scope accounting-visibility defect** with certainty, and a
> **TENANT-scope security defect only if** the company hierarchy can span
> tenants. The prior finding asserted the security character without
> establishing the hierarchy question.
> Class: **FACT VERIFIED** (the rule); **HOLD — SCOPE EVIDENCE REQUIRED** (its
> security character). **The hold stands** — see §4.2.1.

#### 4.2.1 A second traversal mechanism, verified from primary source

P11 reasons that a parent-child edge carries **at least two** traversal
mechanisms, the second being the lock date, and that this converts a spanning
hierarchy from a visibility problem into a **cross-tenant financial effect**.
P11 derived that from standing invariants. **P04 verified it directly against
the accounting core**, and it holds — with a detail P11 did not have.

| Behaviour | Evidence | Class |
|-----------|----------|-------|
| The effective hard lock date of a company is the **maximum over its entire parent chain**, computed with **elevated privilege** and with archived companies included | The compute walks the parent set and takes the maximum | **FACT VERIFIED** |
| The same parent-chain traversal is used for the **soft** lock dates | The soft-lock resolver iterates the parent set | **FACT VERIFIED** |
| The traversal is **deliberately privileged to reach companies the user cannot see** — the code carries an explicit comment saying elevated privilege is needed *because the user might not have access to a parent company* | Source comment at the soft-lock resolver | **FACT VERIFIED** |
| The hard lock date is **irreversible**: removing it raises, and setting it earlier than the current value raises | Two explicit guards | **FACT VERIFIED** |

> **P04-F-66.** A parent company's lock date **cascades to every descendant,
> irreversibly, through a deliberately privileged traversal that the code itself
> documents as reaching companies the user cannot access.** If a company
> hierarchy could span a tenant boundary, a parent in one tenant would
> **irreversibly close an accounting period for a company in another** — not a
> visibility leak but a **cross-tenant financial effect**, executed with elevated
> privilege and impossible to undo.
> Class: **FACT VERIFIED.** This corroborates P11's `P11-SR-02` reasoning from
> primary source rather than by citation.

**Compounding with `P04-B-31`.** This session already established that an entry
aimed at a locked period is **silently re-dated forward rather than refused**.
Put together: the lock that cannot be reversed and cascades across the hierarchy
is the same lock that **does not refuse** — it moves the entry into an open
period instead. A cross-tenant hierarchy would therefore not produce a visible
failure; it would produce **silently mis-periodised entries in the other tenant's
books**.

#### 4.2.2 The detectability boundary — and why it is not only a tenant question

P11 opened a tolerance-zero boundary on this evidence, `T0-13`:

> A financial effect may not cross a tenant boundary silently. No mechanism may
> re-date, re-attribute or otherwise mutate an accounting fact in one tenant as a
> consequence of an act in another, and no such effect may occur without a
> **refusal or a recorded, attributable trace**.

P11's framing of why it sits **beside** rather than **inside** the existing
isolation boundary is adopted, because it is the right distinction and P04 had
not made it: one asks whether a boundary is **crossed**, the other whether the
crossing is **detectable**, and the remedies differ — an isolation invariant
closes the first, only a refusal-or-trace guarantee closes the second.

**P04 extends it, on its own evidence.** `T0-13` is scoped to tenant crossings.
The detectability defect this session found is **not scoped to tenant crossings
at all**:

> **P04-F-68.** The silent re-dating requires **no tenant boundary and no company
> hierarchy** to do damage. Inside a **single company**, an entry aimed at a
> locked period is already mutated into an open one with **no refusal and no
> trace** — the estate's own test asserts a charge migrating into the following
> fiscal year at full value. The cross-tenant case is the **worst** instance of
> the defect, not its only one.
> Class: **FACT VERIFIED.**

Consequence: a control written only against tenant crossings would leave the
same mechanism misstating a fiscal year **inside one company today**. The
detectability requirement — *refuse, or leave an attributable trace* — belongs at
**every** scope, not only at the tenant boundary. `P04-B-31`'s close condition is
restated accordingly.

**Accepted by P11 and `T0-13` widened.** The boundary now reads that an
accounting fact may not be silently mutated **at any scope**, with the tenant
crossing as the aggravated case rather than the defining one. P11 widened rather
than opening a sibling, on the reasoning that the boundary asserts **one
property** and the scopes differ in **blast radius, not in the property** — a
sibling would split one invariant into two that must be kept in step. P04 adopts
that reasoning; it is better than the sibling P04 offered as the alternative.

**Two consequences P04 carries:**

1. **`T0-13` is no longer contingent on the Boss's tenant ruling.** The defect is
   reachable today inside one company, so the boundary stands whatever `D-12`
   decides.
2. **`P04-B-31` moves from prospective risk to PRESENT DEFECT.** Re-framed in
   `10` §6 and in the ranking at §8.

**Independent corroboration, from a source that is not P04's.** P11 reports that
its own `P11_UNIFIED_ACCOUNTING_EVENT_REGISTER` §2 already recorded **four
accounting events invisible at the moment they occur, two of them single-company
re-datings** — one noting that *"the posted record carries no trace that its date
was moved"*, another recording an event that *fires with no lock configured* and
is not visible. **Neither needs a tenant.** Both predate `T0-13` by four
documents.

> **P04-F-70.** The single-company silent-mutation defect is recorded **twice, in
> two packages, from two independent evidence bases** — P04's from the reference
> product's own test, P11's from its accounting-event register — and **neither
> session connected it to the boundary being drafted about it**.
> Class: **FACT VERIFIED**, both halves. **Upgraded from peer-published after
> P04 read P11's register directly** at commit `2e284ef` — see `18` `P04-REV-19`
> for why it was not read sooner, which is a defect of P04's, not a limitation.

**And reading it produced something neither session had.** P11's register records
**two** re-dating events, not one variant of the same:

| | Trigger | Lock involved? |
|---|---------|----------------|
| `UAE-04` | Entry re-dated **on posting** | **yes** — a lock is violated |
| `UAE-05` | Entry re-dated **on a document-date change**, on any non-sale document | **no** — *"fires with no lock configured"* |

> **P04-F-76.** `P04-B-31` describes re-dating as a **lock-interaction** defect —
> an entry aimed at a locked period is moved rather than refused. P11's register
> records a **second, independent** re-dating path that **needs no lock at all**:
> an ordinary document-date edit silently re-attributes the accounting period,
> which P11 notes can be a clerical edit upstream *"with no accounting
> justification"*.
> **Silent period mutation is therefore not only a lock defect.** A control
> written against the lock path alone would leave the second one live, which is
> the same mistake — one scope narrower than the evidence — that `T0-13` was
> widened to fix.
> Class: **FACT VERIFIED** (read at `2e284ef`). Registered `P04-B-45`.

**The method note P11 derived from it is adopted by P04 as well**, because P04 is
equally exposed to it:

> When opening a tolerance-zero boundary — or any invariant — **re-derive its
> scope from the register, never from the finding that prompted it.** A boundary
> drafted while composing a specific case takes its scope from the case in front
> of it, not from the evidence that already generalises it.

#### 4.2.3 The expiry rule is now named

P11 generalised `P04-B-44` into a standing position (`SCP-09`): a scope
determination taken against behaviour the programme is **obliged to change** must
record its **expiry trigger** — it is a dated reading, not a standing fact.

Both P04 instances are covered by it: the machine register (`P04-B-44`) and the
work centre. This package had found the pattern twice and stated it once, in
prose, without naming it. It is named now, and both determinations in §2 and §4.1
carry their trigger.

**Exact lift condition for the hold**, adopted from P11 verbatim in substance:

> An invariant of the class that admits **no exception**, asserting that every
> company's tenant assignment is **stored and non-null** and that **no
> company-hierarchy edge may connect two companies with different tenant
> assignments** — plus a **continuous conformance control** asserting it.

Until both exist, the span cannot be shown unreachable and the security
character of `P04-F-56` stays **HOLD — SCOPE EVIDENCE REQUIRED**. Registered
`P04-B-43`.

**One mechanical caveat, new this session.** The asset **group** may have no
company, and the visibility rule tests a parent-of relation on that company. A
company-less group's behaviour under that operator is **not decidable from
source** — it may be visible to none, or to all. Registered **P04-B-28**;
it is a one-query check on the running system.

### 4.3 Analytic distribution

*`P04-F-99`/`P04-F-100`: the scope reasoning below is unaffected. The dimension it scopes is **empty in `551ab874`** — one plan, zero accounts, 0 of 40,353 lines — and **populated in `4b766580`**, where 9 accounts exist and every distributed asset move nets to zero.*

**Original position.** Analytic distribution was treated as a company-context
matter throughout.

**Correct scope analysis.** The **plan** is a reporting structure and is a
TENANT candidate. The **distributed amount** is a company financial fact. The
two are different objects and the correction requires them to be scoped
separately (ownership ≠ reference scope).

This sharpens P04-F-52: mandatory-plan enforcement being bypassed on every
programmatic post is not merely a control weakness — **a tenant-scoped
reporting structure is being relied on to enforce a company-scoped financial
attribution requirement (`BD-02`)**. That is a scope mismatch in the design
intention, independent of whether the enforcement fires.

Recorded as **P04-F-57**, class **SUPPORTED INTERPRETATION**.

### 4.4 What was NOT affected

The following were reviewed against the correction and found **unaffected**;
they are preserved unchanged and were not re-run:

- the entire upstream capitalization trace (`01`) — it concerns which document
  creates a company financial fact, and every candidate was already company-scoped;
- the event register and the asset-to-general-ledger matrix (`03`, `04`);
- the disposal and derecognition matrix (`07`), including all statutory findings;
- the depreciation and cost handoff (`06`), except §5 as revised at §4.3 above;
- every imported prior-evidence finding, every commit citation, and every
  contradiction inherited from the three prior packages.

## 5. Peer dependencies opened by this correction

| ID | Dependency | Owner | Status |
|----|-----------|-------|--------|
| **P04-PD-01** | Work-centre scope and its company-ownership requirement | **P03** | **PEER DEPENDENCY OPEN** |
| **P04-PD-02** | Whether a company hierarchy may span tenants | **P11** | **PEER DEPENDENCY OPEN** |
| **P04-PD-03** | Whether one tenant may hold unrelated companies, and who grants the exception | **P11** | **PEER DEPENDENCY OPEN** |
| **P04-PD-04** | Analytic plan scope — tenant-owned structure versus company-owned effect | **P09** | **PEER DEPENDENCY OPEN** |
| **P04-PD-05** | Chart-of-accounts scope: is the capitalization designation company truth or a tenant template applied per company? | **P08** | **PEER DEPENDENCY OPEN** |

None of these stops P04. All unaffected work continued.
