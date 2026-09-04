# P09_SCOPE_OWNERSHIP_MATRIX

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Issued under:** `SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. THE RULE APPLIED

Permitted scopes: **PLATFORM**, **TENANT**, **COMPANY**. Context requirements are *derived* from the determined scope; they are not applied uniformly.

| Scope | Tenant context | Company context |
|---|---|---|
| PLATFORM | not required | not required |
| TENANT | mandatory | not required unless the specific operation is company-scoped |
| COMPANY | mandatory | mandatory |

`MISSING REQUIRED SCOPE = DENY`. `OWNERSHIP CANNOT BE PROVEN = DENY`.
`OWNERSHIP ≠ AVAILABILITY`. `OWNERSHIP SCOPE ≠ OPERATIONAL SCOPE ≠ FINANCIAL SCOPE ≠ REFERENCE SCOPE`.

## 2. THE STRUCTURAL FINDING THAT PRECEDES THE MATRIX

**The reference pattern has no scope representation at all.** It has one nullable company field per object, and that single field is asked to express three different things:

1. ownership ("this belongs to company X");
2. availability ("this may be used by every company");
3. selection ("this rule applies when the company is X").

Where the field is empty, the three meanings are indistinguishable. There is no tenant concept anywhere on the analytic surface, and one object — the dimension axis — carries no company field either (COR-P09-03).

**Therefore the matrix below is a P09 *determination*, not a reading of the reference pattern.** Where the reference-pattern column says "undeclared", that is the finding.

## 3. THE MATRIX

Columns follow the correction's eight research questions.

| Object | 1 OWNS | 2 EXECUTES | 3 ACCESS | 4 MUTATE | 5 REFERENCE | 6 Financial effect? | 7 Company owning the effect | 8 Data class | Reference pattern | Evidence |
|---|---|---|---|---|---|---|---|---|---|---|
| **Dimension axis** (analytic plan) | TENANT | TENANT | TENANT | TENANT (admin tier) | TENANT + all its companies | no | n/a | tenant-owned management policy | **undeclared** — no company field, no tenant concept; materialises as shared physical schema | COR-P09-03, EV-P09-010 |
| **Dimension value** (analytic account) | TENANT default; COMPANY where the value denotes a legal-entity object | TENANT | TENANT | TENANT (admin tier) | any company of the owning tenant | no | n/a | tenant-owned; company-qualified subset | optional company; empty = visible to every company | EV-P09-027, EV-P09-028 |
| **Management record** (analytic line) | **COMPANY** | COMPANY | COMPANY | **none after close** (proposed) | its own company only | no directly; it *represents* one | the company on the record | company-specific management truth | required, immutable company; strictly scoped record rule | EV-P09-027, EV-P09-028 |
| **Allocation on a costed row** | COMPANY (follows its carrier) | COMPANY | COMPANY | COMPANY, audited, closed at period close | — | no | the carrier's company | company truth | schemaless payload; no scope check attaches | EV-P09-016, EV-P09-114 |
| **Allocation rule** (distribution model) | TENANT | TENANT | TENANT | TENANT (admin tier) | any company of the tenant; company is a *selector*, not ownership | no | n/a | tenant-owned policy | optional company; every selector treats empty as a wildcard | EV-P09-021, EV-P09-115 |
| **Obligation rule** (applicability) | TENANT | TENANT | TENANT | TENANT (admin tier) | company-qualified | no | n/a | tenant-owned policy | optional company; empty applies to every company | EV-P09-034 |
| **Cost object** | TENANT or COMPANY by type — see `P09_COST_OBJECT_MODEL` §6 | COMPANY | TENANT | owner tier | any company of the tenant | no | the company bearing the cost | mixed | **no object exists** | COR-P09-04 |
| **Budget** | TENANT (management) or COMPANY (statutory) — declared per record | COMPANY | per declared scope | owner tier, revision only after confirm | — | no | the company whose actuals it consumes | mixed; must be declared | optional company; empty = visible to every company | EV-P09-070 |
| **Budgetary position** | TENANT | TENANT | TENANT | TENANT (admin tier) | company-qualified | no | n/a | tenant-owned reference | **not found in scope** (class B) | EV-P09-060 |
| **Allocation-to-ledger mechanism** (automatic transfer) | **COMPANY** | COMPANY | COMPANY | COMPANY | its own company only | **YES — it posts** | the destination journal's company | company legal/accounting truth | company derived from the destination journal | EV-P09-040, EV-P09-049 |
| **Management report definition** | TENANT (or PLATFORM for a standard report) | per report | per declared scope | owner tier | — | no | n/a | mixed | undeclared; the analytic column is gated by one hidden group | EV-P09-056 |
| **Management report *result*** | scope of the aggregation, declared | per declared scope | per declared scope | immutable | — | no | n/a | derived | implicit widening: company-empty records enter every company's total | EV-P09-031 |
| **Privileged-axis system parameter** | — | — | — | — | — | no | n/a | **PLATFORM artefact carrying a TENANT decision — scope violation by construction** | database-global parameter; source states it cannot be changed safely once set | EV-P09-013 |

## 4. THE SCOPE VIOLATIONS FOUND

| ID | Violation | Why it is a violation under the corrected constitution | Evidence |
|---|---|---|---|
| **SV-01** | The dimension axis materialises as **shared physical schema**. | A TENANT-owned object is physically PLATFORM-shared. Its ownership cannot be proven, and `OWNERSHIP CANNOT BE PROVEN = DENY` cannot be enforced because there is nothing to deny against. | EV-P09-010, COR-P09-03 |
| **SV-02** | One axis is privileged by a **database-global parameter**. | A PLATFORM-scoped artefact carries a TENANT-scoped decision, and the source states it cannot be safely changed afterwards. | EV-P09-013 |
| **SV-03** | Ownership and availability share **one nullable field** on five object types. | `OWNERSHIP ≠ AVAILABILITY` is not representable. | EV-P09-027/028, EV-P09-070 |
| **SV-04** | A COMPANY-scoped aggregate silently admits records of undeclared scope. | Implicit widening from COMPANY to a wider scope, unauthorised and unmarked. | EV-P09-031 |
| **SV-05** | The COMPANY-consistency check between a costed row and its dimension values fires on **one axis only**, and cannot structurally attach to the allocation payload. | A COMPANY-scoped mutation is not scope-checked. Confirmed by independent challenge on two independent platform mechanisms. | EV-P09-029, EV-P09-114, **CH-CAND-02 CONFIRMED** |
| **SV-06** | An allocation rule with no selectors matches **every** transaction in the database. | A TENANT-scoped policy object with unbounded cross-scope reach. | EV-P09-021, EV-P09-025-row |
| **SV-07** | The analytic surface has **one** permission group with full create/delete on every object, in a hidden category. | No scope tier can be enforced because no role tier exists. | EV-P09-012 |

**Note on what is *not* a violation.** The presence of company-empty dimension values and company-empty rules is **not**, by itself, a violation — under the corrected constitution those objects are legitimately TENANT-scoped. This is a material narrowing of the session's original reading and is recorded in `P09_REVISION_LOG` §R1. The violation is the absence of a declaration, not the presence of a null.

## 5. DERIVED CONTEXT REQUIREMENTS FOR SMEsPlus

| Operation | Tenant context | Company context | Denial condition |
|---|---|---|---|
| read a dimension axis | mandatory | not required | axis not owned by the caller's tenant |
| create / retire a dimension axis | mandatory | not required | caller lacks the tenant admin tier |
| read a dimension value | mandatory | not required | value not owned by, or not available to, the caller's tenant |
| assign an allocation to a costed row | mandatory | **mandatory** | any named dimension value not available to that company |
| create a management record | mandatory | **mandatory** | period closed for that company; cost object closed |
| mutate a management record | — | — | **always denied**; correction is a new record |
| read a dimension balance | mandatory | mandatory **unless** the aggregation is explicitly declared tenant-scoped and authorised | undeclared aggregation scope |
| define an allocation rule | mandatory | not required | caller lacks the tenant admin tier |
| run an allocation-to-ledger mechanism | mandatory | **mandatory** | period closed; approval absent |
| define a budget | mandatory | required only for a COMPANY-scoped budget | scope not declared on the record |
| read actual-versus-budget | mandatory | per the budget's declared scope | scope not declared on the record |

## 6. PEER DEPENDENCIES OPEN

P09 records its own determinations and does not adjudicate against another process. The following are **`PEER DEPENDENCY OPEN`** and are carried to P11 for reconciliation:

| ID | Dependency | Counterpart |
|---|---|---|
| PD-01 | scope of the manufacturing order and the work centre as cost objects | P03 Manufacture-to-Cost |
| PD-02 | scope of the asset as a cost object, and the asset↔equipment relationship | P04 Acquire-to-Retire |
| PD-03 | scope of the commitment concept (whether an encumbrance is ledger-visible) | P01 Procure-to-Pay |
| PD-04 | scope of the accounting event identity that P09's trace step 2 requires and does not have | Core Ledger / P11 |
| PD-05 | whether a tenant may span legal entities in more than one jurisdiction, which determines whether a TENANT-scoped budget is admissible at all | P07 TH Tax Compliance, P11 |
| PD-06 | the platform-level definition of tenant, which P09 assumes but does not own | P11 |

## 7. HELD

| ID | Item | Status |
|---|---|---|
| SC-H-01 | scope of the work-centre allocation carrier | `HOLD — SCOPE EVIDENCE REQUIRED` (PD-01) |
| SC-H-02 | whether the deployed tenant custom set includes the department dimension at all | `HOLD — EVIDENCE REQUIRED`; class **D**, three copies differ |
| SC-H-03 | any Thai statutory constraint on cross-company management reporting | `HOLD / EVIDENCE REQUIRED` — routed to the Accounting-Tax track; no statutory claim is made in this package |

## 8. TERMINAL STATE

**MATRIX ISSUED. SEVEN SCOPE VIOLATIONS RECORDED. SIX PEER DEPENDENCIES OPEN. THREE ITEMS HELD. NO GATE MOVED.**
