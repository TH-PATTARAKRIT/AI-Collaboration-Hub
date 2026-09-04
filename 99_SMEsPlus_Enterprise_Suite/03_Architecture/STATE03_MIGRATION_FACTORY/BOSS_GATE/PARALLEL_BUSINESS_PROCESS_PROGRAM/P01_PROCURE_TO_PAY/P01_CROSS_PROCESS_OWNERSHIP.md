# P01 — CROSS-PROCESS OWNERSHIP REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Rule enforced: a consumer process may read, reference, derive from or report an event.
It may **not** recreate the same economic effect.

---

## 1. PARALLEL PROGRAM STATUS

**P01 is the first process session of the Parallel Business Process Accounting Deep Research
programme.** A branch enumeration of the repository at session start found no peer process
branch (`P02`…`P0n`) for any other process. Every cross-process row below therefore has a
peer status of **NOT YET EXECUTED**, not "awaiting publication".

Enumeration method: `git for-each-ref refs/remotes/origin` over the full remote branch list,
filtered for process identifiers. False-negative mode: a peer session executing in another
workspace without having pushed would not appear.

---

## 2. OWNERSHIP MATRIX

| Business fact | P01 role | Other process | Their role | Conflict risk |
|---|---|---|---|---|
| Inventory quantity increase on receipt | **Owner** | Inventory | Consumer / reporter | Low |
| Inventory **value** increase on receipt | **Owner**, but only for storable + continuous items | Inventory | Owner of subsequent value movements | **Boundary must be drawn at the receipt layer** |
| Unit cost established at receipt | **Owner** | Inventory / COGS | Consumer | The COGS track is on standing HOLD; P01 must not assume a cost method |
| Cost of goods sold | Not P01 | Inventory / COGS / P02 | Owner | P01 must not post any consumption effect |
| Landed cost absorption | Candidate shared | Inventory | Candidate owner | **UNRESOLVED** — assigned to an expert, see `P01_AAS03_EXPERT_CHALLENGE.md` |
| Vendor payable | **Owner** | Account (core ledger) | Consumer / reporter | Low |
| Payment and settlement | **Owner** for vendor-side | Account (core ledger) | Owner of the reconciliation engine and of FX difference | **P01 must not re-derive FX**; FX arises in the ledger at settlement (`EV-P01-21`) |
| FX rate selection and missing-rate policy | Consumer | Account Wave A | **Owner** — a standing Boss ruling exists on the Account track | P01 must inherit, not decide |
| Purchase tax (input tax) | Candidate owner | Account / Localization | Candidate owner | **UNRESOLVED** |
| Withholding tax | **UNRESOLVED — bill or payment** | Account / Localization | Candidate owner | **UNRESOLVED**, and the Account track holds this as a statutory question |
| Asset recognition | **Trigger**, at bill posting | Asset | **Owner** of the asset lifecycle | P01 owns the *trigger*, Asset owns the *asset*. The boundary is the bill line. |
| Depreciation | Not P01 | Asset | Owner | P01 must not post any depreciation effect |
| Period close | Consumer | Account (core ledger) | Owner | P01 must not define lock semantics |
| Cross-company document generation | **P01 is a trigger surface** (`EV-P01-27`) | SaaS / Platform Architecture | Owner of the tenant and company boundary | **Tolerance-zero. See §4.** |
| Subcontract purchase | Candidate consumer | Manufacturing | Candidate owner | **CLASS C — NOT YET SEARCHED** |
| Intercompany purchase | Trigger surface | Account / SaaS | Owner | See §4 |

---

## 3. INHERITED CONSTRAINTS FROM PEER TRACKS

P01 does not re-open any of these. It records them as binding inputs.

| Source track | Constraint on P01 |
|---|---|
| COGS Deep Research | Terminal **HOLD**. The reference system's continuous-valuation pattern was found unstable across versions. P01 must not assume any particular cost method survives. **This session independently reproduced that instability in a second area — the receipt-to-bill clearing bridge (`EV-P01-24`,`EV-P01-25`).** |
| Account Wave A | System-derived accounting date; silent single-rate FX fallback; no event identity. **P01 independently reproduced the system-derived accounting date in the receipt path (`EV-P01-06`).** |
| Account Wave A / GB-08 | Boss ruling on FX rate ownership and missing-rate policy. P01 inherits it. |
| Inventory MTI ruling set | Multi-tenant invariants. P01's cross-company trigger surface (§4) must be tested against them. |
| Negative Claim Standard | Applied throughout this package. |
| 8-Criteria Universal Exit Constitution | Governs this session's exit. See `P01_PMO_REVIEW.md`. |

---

## 4. TOLERANCE-ZERO: CROSS-COMPANY EFFECT TRIGGERED FROM P01

This is the most serious ownership finding in the session and it is stated in full.

Approving a purchase order, or posting a vendor bill, whose partner resolves to another
company in the same database, causes a document to be **created in that other company**,
executed as that company's designated user, with the company context switched.
`EV-P01-27`, `EV-P01-28`.

The mechanism has four properties, each verified:

1. The company is resolved by an **elevated-privilege search across every company in the
   database**, ignoring the acting user's allowed companies. `EV-P01-26`.
2. The match is an **ancestor match on the contact hierarchy**, so a *child contact* of another
   company's partner resolves to that company — not only the company's own partner record.
   `EV-P01-26`.
3. The search takes the **first match**; if two companies' partners are both ancestors of the
   contact, one is chosen silently. `EV-P01-26`.
4. The "create as" user **defaults to the superuser**, and a company setting can make the
   generated document **post automatically** rather than stay in draft. `EV-P01-29`,
   `EV-P01-30`.

No guard restricting the two companies to a common tenant, economic group, or the acting
user's allowed companies was found — **class B, scope: the three files cited only.** An
independent check was assigned to the Database Design expert.

### 4.1 Assessment under the corrected SCOPE-AWARE model

`SMEPLUS-26-09-04-ACC-REV2-CORR1` supersedes any blanket "Tenant and Company context are
mandatory for every operation" reading. The correct test is **scope-aware**, and this finding
is stated under that test, not under the superseded one.

**Scope classification of the mechanism:**

| Question | Answer |
|---|---|
| What scope OWNS the generated document? | **COMPANY** — it is a legal/accounting record of the target company |
| What scope EXECUTES the operation? | **COMPANY (source)** — the acting user is operating in the source company |
| What scope may MUTATE the target company's records? | **COMPANY (target)** |
| Does it create a financial effect? | **Yes**, where the target company's setting posts it automatically |
| Which company owns that financial effect? | **The target company** |

So the operation is COMPANY-scoped, and its execution context is a *different* company from
the one that owns the resulting financial effect. That is not automatically wrong — a genuine
intercompany transaction is exactly that. The defect is in **how the ownership is
established**:

- The corrected constitution states **`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`**.
- Here ownership of the target-company financial effect is not proven. It is **inferred from
  an ancestor match in the shared contacts hierarchy**, resolved with elevated privilege that
  ignores the acting user's allowed companies, taking the first match when several exist.
  `EV-P01-26`.
- `OWNERSHIP ≠ AVAILABILITY` and `MULTI-TENANT MEMBERSHIP ≠ MULTI-TENANT EXECUTION CONTEXT`:
  this mechanism derives an **execution context** in the target company from a **reference-data
  relationship** (a contact's parent), which is precisely the substitution those two rules
  forbid.

**Restated finding:** the mechanism is not condemned for being cross-company. It is condemned
because a COMPANY-scoped financial effect is raised in a company whose ownership of that
effect was never proven — only inferred from reference data that a different scope controls.
Under the corrected rule the correct behaviour where ownership cannot be proven is **DENY**;
the observed behaviour is **proceed, as superuser, and optionally post**.

**Tenant question, stated separately and honestly:** whether the two companies belong to the
same tenant is **not tested anywhere in the code read**. That is a class **B** negative
(scope: the three cited files). Under the corrected model, unrelated independent companies are
separate tenants by default, so an untested company pair is also an untested *tenant* pair —
which makes this a candidate **TENANT-boundary** crossing, not merely a company one. This is
the item that carries the tolerance-zero weight, and it remains **UNRESOLVED — SCOPE EVIDENCE
REQUIRED** pending the Database Design expert's independent check.

**Relationship to prior evidence:** the Account Wave A track recorded a hard company lock
being defeated through a contacts-role partner merge. This is the **same primitive**
(partner-hierarchy resolution granting cross-company reach) appearing independently in a
second process. Two independent instances make this a systemic architectural property of the
reference model, not a local defect.

**Disposition:** `TOLERANCE-ZERO — HOLD.` Under exit criterion EC-04 a conditional outcome may
not bypass a tolerance-zero risk. This item alone prevents P01 from being presented as
unconditionally ready.

---

## 5. HANDOFF OBLIGATIONS TO PEER PROCESSES

When each peer process session runs, it must accept or contest these P01 positions:

| ID | Position P01 asserts | Peer that must respond |
|---|---|---|
| `HO-01` | The vendor bill is the sole owner of the payable event | P02 (Order-to-Cash) — must not create a vendor payable |
| `HO-02` | Receipt owns the *first* valuation layer; Inventory owns everything after | Inventory |
| `HO-03` | P01 owns only the asset *trigger*; the asset lifecycle is Asset's | Asset |
| `HO-04` | P01 does not decide FX rate policy | Account |
| `HO-05` | The received-not-billed obligation has two competing representations and needs one owner | Account + Inventory |
| `HO-06` | The cross-company trigger surface is a platform decision, not a process decision | SaaS / Platform Architecture |

---

# ADDENDUM — PEER STATUS CORRECTED, AND TWO PEER ITEMS ANSWERED

Added after the package was committed, following a re-fetch of the remote at the end of the
session.

## A.1 Correction to §1

§1 states that no peer process branch existed. **That was true at session start and is now
stale.** A re-fetch shows **six** peer process branches published on the same day:
`P02` Order-to-Cash · `P03` Manufacture-to-Cost · `P04` Acquire-to-Retire ·
`P05` Expense-to-Pay · `P06` Bank-to-Reconcile · `P09` Plan-to-Analyze.

The original statement carried its false-negative mode explicitly — *"a peer session running in
another workspace that has not pushed would not appear"* — and that is exactly what happened.
The declared mode was the right one; the claim is corrected here rather than rewritten above,
per the rule that an earlier conclusion is never deleted.

Every `PEER-P01-*` row marked **NOT YET EXECUTED** in `P01_DEPENDENCY_REGISTER.md` §2 should be
read as **PUBLISHED — RECONCILIATION NOT YET PERFORMED**. P01 does **not** adjudicate against
these packages; that is cross-process reconciliation work, and P11's.

## A.2 P05 asks P01 a direct question — answered

P05 records: *"Advance to vendor — P01 owns it … PEER DEPENDENCY OPEN — P01 must state whether
it owns vendor advances."*

**P01's answer: yes, P01 accepts ownership of the vendor-advance event.**

Basis, from P01's own evidence:

- In the base capability, vendor advances are **bill-first**: an advance is recorded as a vendor
  bill and then attached to a purchase order. The routine that does so has exactly one caller in
  the whole root, and there is **no order-side advance wizard** — class **A within `R1`**
  (`EV-P01-37`).
- The project's custom vendor-advance module sits on the purchase capability and is inside
  P01's module closure.

Two qualifications P05 should carry:

1. **P01 has not traced the custom vendor-advance module's own behaviour.** It was assigned to
   an expert and is carried as SUPPORTED INTERPRETATION, not FACT VERIFIED. Ownership of the
   *event* is asserted; the *mechanism* is not yet evidenced by P01.
2. P05 reports that on its own advance path the disbursement debits a profit-and-loss expense
   account with **no advance asset account**. If the vendor-advance module shares that pattern,
   a vendor advance would be expensed on payment and then expensed again on the bill.
   **P01 has not tested this and does not assert it** — it is recorded as a joint edge case for
   whichever session traces the custom module.

## A.3 A cross-process contradiction on withholding tax

| | |
|---|---|
| **P05's position** | The withholding overlap between P01, P02 and P05 is **"Low — single implementation"**, on the basis that all three reach the same payment-register extension |
| **P01's position** | **Two parallel and incompatible withholding mechanisms exist** — one treating withholding as a tax on the bill, the other as a write-off at payment — auto-mirrored into each other, with the reporting layer unioning both sources |
| **P01's verified additions** | The partial-payment netting term is computed with the wrong sign, so withholding **compounds** across partial vendor payments (`CONTRA-P01-09`, re-derived by this session). Two shipped copies of the certificate module map a corporate counterparty to **opposite statutory forms** (`CONTRA-P01-10`, read directly in both copies) |
| **Why the two views differ** | P05 looked at the *call path* — and on that axis it is right: the same extension is reached. P01 looked at the *mechanisms and the shipped copies* — and on those axes there is more than one of each. **Both observations are correct about different things.** |
| **Disposition** | **HOLD — CROSS-PROCESS RECONCILIATION REQUIRED.** P01 does not overrule P05. The risk rating "Low", however, rests on a single-implementation premise that P01's evidence does not support, and P01 asks that the rating be revisited in reconciliation |
| **Routed to** | P11, and the Accounting-Tax track for the statutory axis (`DEP-P01-04`) |

## A.4 A methodological convergence worth recording

P05 reports that its first enumeration returned **every module absent** because an unquoted
shell glob was expanded before the search ran. P01 produced **six fabricated class-A absences**
from an extraction that silently wrote empty files (`ERR-P01-06`), and its Functional Design
expert hit the same class twice more.

**Four independent instances, in two independent sessions, on the same day, of a tooling
artefact presenting as a verified absence** — and in every case the absence would have been the
strongest class of claim the negative-claim standard permits.

This is no longer an incident. It is a systemic property of how this research is conducted, and
it warrants a programme-level control rather than four separate lessons:

> **No enumeration may report a zero without also reporting the size of what it searched, and
> no zero result may be published until the query has been re-run in a second, differently-shaped
> form.**
