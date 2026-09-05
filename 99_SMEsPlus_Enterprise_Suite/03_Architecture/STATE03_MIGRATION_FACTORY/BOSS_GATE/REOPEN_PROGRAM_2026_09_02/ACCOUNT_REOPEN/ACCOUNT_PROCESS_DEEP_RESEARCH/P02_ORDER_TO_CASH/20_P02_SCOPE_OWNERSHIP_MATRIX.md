# 20 — P02 SCOPE OWNERSHIP MATRIX

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Produced under constitution correction **`SMEPLUS-26-09-04-ACC-REV2-CORR1`** — *SCOPE-AWARE EVERYWHERE*.

## 0. The Governing Rule Applied Here

```
PLATFORM SCOPE   -> Tenant context NOT REQUIRED, Company context NOT REQUIRED
TENANT SCOPE     -> Tenant context MANDATORY,    Company context NOT REQUIRED
                    (unless the specific operation is Company-scoped)
COMPANY SCOPE    -> Tenant context MANDATORY,    Company context MANDATORY

MISSING REQUIRED SCOPE          = DENY
REQUIRED OWNERSHIP UNPROVABLE   = DENY
```

Tenant = security / customer boundary. Company = legal / accounting / business boundary.
`OWNERSHIP ≠ AVAILABILITY`. `OWNERSHIP SCOPE ≠ OPERATIONAL SCOPE ≠ FINANCIAL SCOPE ≠ REFERENCE SCOPE`.

**This file does NOT assert that both tenant and company context are required for every P02 operation.**
Each row below is determined from business, legal and accounting semantics plus source evidence, and each
row that cannot be determined is held.

## 0a. Denominator Declaration

Added after the independent challenge observed that this file made counted claims with no declared basis.

- **POPULATION** — the P02 objects and operations enumerated in `05_P02_BUSINESS_EVENT_REGISTER.md` (24
  business events) and `06_P02_ACCOUNTING_EVENT_REGISTER.md` (13 accounting events), plus the
  configuration and reference objects those events read.
- **PATTERN** — for each, the eight scope questions of correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` §4.
- **PATH SET** — the evidence for the *company-level* determinations is
  `L2_AUDIT_QUARANTINE/T4_SCOPE_BOUNDARY_AND_CLOSE_EVIDENCE.md`, whose own denominator is declared in its
  §0 and was **independently reproduced** by the primary session (the 71-field / 31-unvalidated count and
  the 9,431-file population both reproduce exactly). **This file inherits that denominator and declares
  the inheritance rather than restating it.**
- **UNIT** — one object or one operation.
- **Declared limit** — every *tenant-level* determination in this file is a `DESIGN CANDIDATE` derived
  from business semantics. **The reference has no tenant concept**, so no tenant row can be, or is,
  evidenced.

## 1. Method Statement

For every material P02 object and operation the eight correction questions are answered:
(1) which scope **owns** it; (2) which scope **executes** it; (3) which may **access**; (4) which may
**mutate**; (5) which may **reference**; (6) does it create a **financial effect**; (7) if so which
**company** owns that effect; (8) is it platform reference data, tenant-owned data, or company-specific
legal/accounting truth.

Columns 3–5 are collapsed into one **Access / Mutate / Reference** column where they coincide, and are
split where they do not — the split cases are the interesting ones.

**The reference system provides no evidence at tenant level at all** — the case-insensitive token
`tenant` returns **zero files** across the five core modules (T4 §10.1). Every tenant determination below
is therefore a **`DESIGN CANDIDATE` derived from business semantics**, never a `FACT VERIFIED` about the
reference. Company-level determinations *are* evidenced.

## 2. P02 Object Scope Matrix

| Object | Owns | Executes | Access / Mutate / Reference | Financial effect? | Company owning it | Data class | Tag |
|---|---|---|---|---|---|---|---|
| Unit of measure, currency **code**, country, tax **jurisdiction identity** | **PLATFORM** | PLATFORM | access: all · mutate: PLATFORM only · reference: all | no | n/a | platform reference | `DESIGN CANDIDATE` |
| **Currency exchange rate** | **see §4 — HELD** | — | — | **yes, indirectly** | — | disputed | `HOLD — SCOPE EVIDENCE REQUIRED` |
| Customer (commercial identity) | **TENANT** | TENANT | access: tenant · mutate: tenant · reference: any company **within** the tenant | no | n/a | tenant-owned | `DESIGN CANDIDATE` |
| **Customer receivable position** | **COMPANY** | COMPANY | company only | **yes** | the invoicing company | company legal truth | `FACT VERIFIED` (company level) |
| Product (commercial identity, description, class) | **TENANT** | TENANT | access: tenant · mutate: tenant · reference: any company in the tenant | no | n/a | tenant-owned | `DESIGN CANDIDATE` |
| **Product cost / valuation configuration** | **COMPANY** | COMPANY | company only | **yes** | the holding company | company legal truth | `FACT VERIFIED` — company-dependent in the reference |
| Price list / commercial terms | **TENANT**, optionally narrowed to COMPANY | TENANT | access: tenant · mutate: tenant | no | n/a | tenant-owned policy | `DESIGN CANDIDATE` |
| **Chart of accounts / account role mapping** | **COMPANY** | COMPANY | company only | **yes** | the owning company | company legal truth | `FACT VERIFIED` — and see §5 |
| **Invoice policy** (order vs delivery) | **TENANT** policy, **COMPANY** effect | TENANT sets, COMPANY applies | mutate: tenant · reference: company | **yes, indirectly — it determines when revenue may be recognised** | the invoicing company | tenant policy with a company effect | `DESIGN CANDIDATE` |
| **Cost-recognition policy** | **COMPANY** | COMPANY | company only | **yes** | the company relieving inventory | company legal truth | `FACT VERIFIED` — company-level in the reference |
| Quotation / Sales order | **COMPANY** | COMPANY | company only | no | n/a | company operational | `FACT VERIFIED` |
| Outflow movement | **COMPANY** | COMPANY | company only | **yes** | the company whose inventory is relieved | company legal truth | `FACT VERIFIED` |
| **Stock location** | **COMPANY** — *but see §3* | COMPANY | — | indirect | — | **contested in the reference** | `CONTRADICTED` |
| Valuation layer | **COMPANY** | COMPANY | company only | **yes** | the company | company legal truth | `FACT VERIFIED` |
| Customer invoice / credit note | **COMPANY** | COMPANY | company only | **yes** | the issuing company | company legal truth | `FACT VERIFIED` |
| Payment / receipt | **COMPANY** | COMPANY | company only | **yes** | the company holding the bank | company legal truth | `FACT VERIFIED` |
| Matching / reconciliation record | **COMPANY** | COMPANY | company only | **yes** — it emits FX and cash-basis entries | the company | company legal truth | `FACT VERIFIED` |
| Lock date / period close | **COMPANY** | COMPANY | mutate: a company-scoped accounting authority | **yes** | the company | company legal truth | `FACT VERIFIED` |
| **Intercompany sale pair** | **COMPANY × COMPANY, within one TENANT** | see §6 | — | **yes on both sides** | both, independently | company legal truth | `DESIGN CANDIDATE` + `HOLD` |
| Consolidated / cross-company reporting | **TENANT** | TENANT | read-only aggregate over member companies | **no — reporting only** | n/a | tenant-derived | `DESIGN CANDIDATE` |
| Platform tax **reference** (rate tables as published) | **PLATFORM** | PLATFORM | access: all · mutate: PLATFORM | no | n/a | platform reference | `DESIGN CANDIDATE` |
| **Tax configuration as applied** (which tax on which sale) | **COMPANY** | COMPANY | company only | **yes** | the company filing the return | company legal truth | `FACT VERIFIED` |

## 3. Scope Findings From The Evidence

### SF-01 — The reference's boundary is COMPANY-only, and it is data, not structure

**`FACT VERIFIED`** — no tenant entity exists (T4 §10.1). The company boundary is enforced by
**record-rule rows evaluated against the user's *activated* companies** — the company switcher — and
those rows are runtime-editable data (T4 §9.2).

**Scope consequence.** A boundary evaluated against a user-switchable set is a **filter**, not a scope. It
cannot serve as a TENANT boundary, because the answer to "which tenant is this?" would then depend on
what the user has switched on. `DESIGN CANDIDATE`: the tenant scope must be resolved **before** any query
is built and must not be derivable from user preference.

### SF-02 — Company propagation is four mechanisms, not one invariant

**`FACT VERIFIED`** — T4 §1. Order and order line take the **environment** company; the movement takes the
**routing rule's** company; the valuation layer and movement line take **whatever the creating code
passes**; the accounting document takes the **journal's** company.

**Scope consequence.** There is no single propagation rule to lift to tenant level. `DESIGN CANDIDATE`:
scope must be **stamped once at the origin of a business transaction and carried, never re-derived** from
the execution environment at each hop.

### SF-03 — Company-dependent configuration resolves from the environment, not the record

**`FACT VERIFIED`** — the valuation mode, costing method, stock journal and the three stock accounts are
company-dependent properties, and for such fields the consistency check validates against the
**environment** company, not the record's (T4 §2).

**`FACT VERIFIED`** — one live consequence: the interim-account matching routine resolves the interim
account **with no company context at all**, in direct contrast to the sibling cost-of-sales builder in the
same file which sets it explicitly. Where the environment company differs from the document's company the
account matches no line and **the matching silently does nothing** (T4 §3).

**Scope consequence — this is the single most important scope lesson in P02.** Configuration that
*belongs to* a company must not be *resolved from* the acting context. `DESIGN CANDIDATE`: every
scope-dependent value must be read through the **record's** declared scope, and reading one without a
declared scope must be a denial, not a default.

### SF-04 — The shared transit location is a scope violation by construction

**`FACT VERIFIED`** — the inter-company transit location is a **single, company-less, database-global
record**, and creating any company **unarchives it database-wide unconditionally**. The onward rewiring of
every other company's partner stock locations runs as superuser over the whole company table — but is
**gated on the acting user holding the multi-company group**. The unqualified form of this claim was a
track overstatement corrected by the primary session on re-derivation; see
`12_P02_CONTRADICTION_REGISTER.md` C-11.

**Scope consequence.** This object has **no owning scope at all**. In a single database it makes every
company a stock counterparty of every other by configuration default. At tenant level it is not merely
wrong, it is a **cross-tenant stock path**. `DESIGN CANDIDATE`: there is **no PLATFORM-scoped stock
location**. Every location is COMPANY-scoped; a transit position between two companies is a
**relationship between two company-scoped locations**, and a relationship whose two ends are in different
tenants must be **unrepresentable**.

### SF-05 — Cross-company reads that carry no scope

**`FACT VERIFIED`** — three enumerated instances (T4 §3):
- a settings sweep across the whole database on a model that has no company at all;
- **partner deletion removes that partner's draft and cancelled orders in every company**;
- the forecast report **discloses draft-order counts, quantities and order names from companies the
  viewer is not in**, whenever no warehouse filter is in context.

**Scope consequence.** Each is an operation whose *operational scope* is wider than its *ownership scope*
— precisely the distinction the correction requires to be made explicit. `DESIGN CANDIDATE`: an operation
whose scope is wider than the scope of the objects it touches must **declare** that widening and be
denied unless the declaration is authorised.

### SF-06 — Reconciliation crosses legal entities on a shared root

**`FACT VERIFIED`** — the terminal matching call does not require identical companies, only a shared root
company (T4 §3). **Journal items of two different legal entities that share one root are reconcilable with
each other.**

**Scope consequence.** Settlement is a COMPANY-scoped financial fact. Matching across two companies means
one company's receivable is settled by another company's money with no intercompany accounting.
`DESIGN CANDIDATE`: matching must require **scope equality at COMPANY level**. Parent/child relaxation is
not admissible for a financial effect.

### SF-07 — The consistency check admits scope-less records

**`FACT VERIFIED`** — the default consistency domain admits records whose company is **unset**, and the
branch variant admits every **parent** company (T4 §2).

**Scope consequence.** `MISSING REQUIRED SCOPE = DENY` is directly contradicted by a check that treats a
missing scope as acceptable. `DESIGN CANDIDATE`: absent scope is a denial, never a wildcard.

### SF-08 — 31 of 71 consistency-flagged fields are never validated

**`FACT VERIFIED`** — auto-validation is opt-in per model and is **off** on the movement, the movement
line, the quant and the valuation layer — **the entire physical-and-valuation half of the O2C chain**
(T4 §2). The eight compensating manual calls are **event-time** checks, not transition checks.

**Scope consequence.** `DESIGN CANDIDATE`: scope consistency must be enforced on **every** create and
write, not at selected workflow events, and must not be a per-model opt-in.

### SF-09 — v19 resolves one value from two company sources in a single expression

**`FACT VERIFIED`** — `R19/stock_account/models/product.py:73-77` (`EV-P02-119`) computes a product's
valuation mode as:

```python
product_template.valuation = product_template.categ_id.with_company(
    product_template.company_id).property_valuation or self.env.company.inventory_valuation
```

The category is read through the **record's** company; the fallback is read from the **acting**
company. For a product with no `company_id` — the ordinary shape for a product shared across
companies — the category is read with `with_company(False)` while the fallback still resolves against
whoever is acting.

**This is `SF-03`'s lesson recurring in the generation SMEsPlus targets**, and in a sharper form: not a
value resolved from the wrong scope, but **one value resolved from two scopes at once**, so which one
governs depends on which half of the expression is reached.

**Status — `OBSERVATION`, not a defect.** No deployed v19 instance was tested against it, and the
bound of `RE-23` applies: this is a fact about the declared root. **`DESIGN CANDIDATE`:** a fallback
chain must resolve every link through **one** declared scope, and a missing scope must deny rather
than silently switch to the acting context.

## 4. `HOLD — SCOPE EVIDENCE REQUIRED`: The Currency Rate

**The question.** Is an exchange rate PLATFORM reference data, TENANT-owned data, or COMPANY-specific
accounting truth?

**The evidence.** In the reference, rates are stored **per root company**, and a rate may only be created
for a main company (T4 §4). Two separate root companies therefore read **independent rate tables**, and
where one has no rate the conversion silently uses 1.0.

**Why it cannot be settled here.**

- Arguments for PLATFORM: a published central-bank rate for a date is an objective external fact; holding
  it once avoids the divergence the reference exhibits.
- Arguments for TENANT: a group commonly mandates one rate source and one revaluation policy across its
  companies; that is a group policy, not an external fact.
- Arguments for COMPANY: the rate actually **used** in a journal entry is part of that company's
  accounting record and must be immutable once posted, whatever its source.

**The likely correct answer** — and it is a *shape*, not a choice between the three — is that the rate
**source/table** and the rate **application** are different objects at different scopes. That shape must
be ruled on, not assumed.

**`HOLD — SCOPE EVIDENCE REQUIRED` — P02-SC-01.** This intersects the existing Boss ruling on FX rate
ownership and missing-rate policy recorded on the Account Wave A GB-08 track. **P02 does not
re-adjudicate it.** Routed to Core Accounting Reconciliation, with the O2C-side evidence in
`09_P02_PAYMENT_RECONCILIATION_MATRIX.md` §4.

## 5. `HOLD — SCOPE EVIDENCE REQUIRED`: The Chart Of Accounts

**The evidence.** In the reference the chart of accounts is **many-to-many to companies** — one account
row is legitimately shared by several companies (T4 §2).

**The question.** Is the *account structure* (codes, names, roles) a TENANT-owned standard that companies
instantiate, or is each company's chart its own object?

**Why it matters for P02.** `07_P02_EVENT_TO_GL_MATRIX.md` §5 shows four account **roles** this process
needs that the Thai chart does not supply. If the chart is tenant-scoped, the missing roles are a
one-time tenant-level design act. If it is company-scoped, every company must be configured
independently and the cross-validation problem of `02_P02_INVOICE_POLICY_MATRIX.md` §1 multiplies by the
number of companies.

**`HOLD — SCOPE EVIDENCE REQUIRED` — P02-SC-02.** Routed to Core Accounting Reconciliation. **P02's
requirement is scope-independent and is stated in `07_P02_EVENT_TO_GL_MATRIX.md` §5**: the five roles must
exist, and the *goods-delivered-not-invoiced* role must be a controlled subledger.

## 6. `HOLD — SCOPE EVIDENCE REQUIRED`: Intercompany Execution Scope

**The evidence.** The intercompany mirror runs as a configured user **defaulting to the superuser**, and
locates the counterparty with an **unscoped** elevated search over the whole company table (T4 §4).
There is **no guarantee of equal total, equal accounting date, or equal exchange rate** between the two
sides, and **nothing compares them afterwards.**

**The scope questions this raises, none answerable from the reference:**

1. Which scope **executes** an intercompany mirror? It is one operation producing **two** company-scoped
   financial effects. Under the canonical model it is a **TENANT-scoped operation with two COMPANY-scoped
   effects** — but that is a design position, not evidence.
2. May an intercompany pair cross a **tenant** boundary? Under `UNRELATED INDEPENDENT COMPANIES = SEPARATE
   TENANTS BY DEFAULT`, the answer is **no by default** — two companies that trade as counterparties and
   are *not* in the same tenant are ordinary third parties, and the mirror must not exist. In the
   reference it can cross **any** company boundary in the database.
3. What identity executes it? A superuser default has **no scope at all**, which the canonical model
   forbids.

**`HOLD — SCOPE EVIDENCE REQUIRED` — P02-SC-03.** P02's evidenced position, offered as a
`DESIGN CANDIDATE`: an intercompany mirror is a **TENANT-scoped operation**, permitted only between two
companies of the **same** tenant, executed under a scoped service identity rather than a superuser, and
**required to produce a reconciled pair** — equal untaxed amount, declared treatment of any tax
divergence, one agreed accounting date, and one agreed rate.

## 7. Scope Determinations That Are Settled

| # | Determination | Basis |
|---|---|---|
| SD-01 | **Every financial effect in P02 is COMPANY-scoped.** All nine financial events of `05_P02_BUSINESS_EVENT_REGISTER.md` §2 are company-owned. No P02 event creates a financial effect at TENANT or PLATFORM scope. | evidenced |
| SD-02 | **The commercial layer above the financial one is TENANT-scoped**: customer identity, product identity, commercial terms. A tenant with several companies has one customer, not several. | business semantics |
| SD-03 | **Reporting that spans companies is TENANT-scoped and read-only.** It may aggregate company-scoped facts; it may not create one. | business semantics |
| SD-04 | **A period close is COMPANY-scoped.** One company may close while another is open. Nothing in P02 requires a tenant-wide close. | evidenced |
| SD-05 | **There is no PLATFORM-scoped object in the P02 transaction path.** Platform scope appears only in reference data the path *consults* — units, currency codes, jurisdictions. | derived |
| SD-06 | **Ownership ≠ availability, evidenced.** Stock owned by a company can be physically unavailable (reserved) and financially out of scope (owner-restricted movements are excluded from valuation while remaining in the company's records). The reference already distinguishes these three; SMEsPlus must too. | evidenced — `EV-P02-025` |

## 8. Register Updates Required By This File

| Register | Update |
|---|---|
| `12_P02_CONTRADICTION_REGISTER.md` | C-09 added: two incompatible answers to "which company's configuration applies" — the record's, or the environment's. |
| Dependency register (§ of `10_P02_CROSS_PROCESS_OWNERSHIP.md`) | P02-SC-01, P02-SC-02, P02-SC-03 added as scope holds routed to Core Accounting Reconciliation. |
| `15_P02_REVISION_LOG.md` | The correction's impact-revalidation record, in the mandated seven-field format. |

## 9. Statement Required By The Correction

**No P02 finding produced before correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` asserted that tenant and
company context are mandatory for every operation.** The scope model was not yet applied at the point the
correction arrived; deliverables 00–09 were written at company level, which the correction does not
disturb. **Nothing was discarded, nothing was reset, and no completed work was repeated.** The full
revalidation record, including the one finding that required re-expression (T4 §9), is in
`15_P02_REVISION_LOG.md` §4.
