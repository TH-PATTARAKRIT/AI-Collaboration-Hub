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
| **P04-SC-03** | May one **tenant** hold companies that are unrelated to each other? | The correction says unrelated independent companies are separate tenants **by default**. "By default" implies an exception exists. Which exception, and who may grant it, is a platform-governance decision outside P04. **PEER DEPENDENCY OPEN — P11** |
| **P04-SC-04** | Does the SMEsPlus **company hierarchy** ever span a tenant boundary? | Determines whether the estate's upward-traversing visibility rule (§4.1) is a tenant breach or a tenant-internal choice. **PEER DEPENDENCY OPEN — P11** |

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
| **Equipment / machine record** | Yes | **TENANT** (§2.2) | **NOT A DEFECT.** Company-optional is correct for a tenant-scoped operational register |
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

**Architecture impact.** The SMEsPlus rule is not "add a company everywhere". It
is: *an object may be company-less only if it is proven TENANT- or
PLATFORM-scoped and creates no financial effect.* The work centre fails that
test; the machine register passes it.

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
> security character).

**One mechanical caveat, new this session.** The asset **group** may have no
company, and the visibility rule tests a parent-of relation on that company. A
company-less group's behaviour under that operator is **not decidable from
source** — it may be visible to none, or to all. Registered **P04-B-28**;
it is a one-query check on the running system.

### 4.3 Analytic distribution

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
