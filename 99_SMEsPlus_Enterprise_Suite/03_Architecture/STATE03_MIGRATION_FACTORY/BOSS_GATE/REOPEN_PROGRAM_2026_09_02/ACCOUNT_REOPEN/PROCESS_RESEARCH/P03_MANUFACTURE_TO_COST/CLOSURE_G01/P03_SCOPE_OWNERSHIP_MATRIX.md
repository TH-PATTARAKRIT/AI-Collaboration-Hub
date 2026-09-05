# P03 — SCOPE OWNERSHIP MATRIX (G01 CLOSURE)

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-08`. Scope derived from each object's own semantics.
**Company scope is not inferred from an accounting effect; tenant scope is not inferred from
sharing.**

---

## 1. Matrix

| Object | Financial effect? | Which company owns it? | Nature | **Ownership scope** | Context required |
|---|---|---|---|---|---|
| Unit of measure, currency | no | n/a | platform reference | `PLATFORM` | neither |
| Productivity-loss taxonomy | no | n/a | reference, tenant-extensible | `PLATFORM` candidate | neither — `SCOPE-Q-02` open |
| **Work centre — as a resource** | **no** | n/a | scheduling resource | **`TENANT`** | tenant only |
| **Work centre — its rate** | **YES** — enters inventory valuation | **unanswerable where `company_id` is null** | costing parameter | **`COMPANY`** | **both — mandatory** |
| Routing operation | no | n/a | engineering definition | `TENANT` | tenant only |
| Bill of materials | no | n/a | engineering definition | `TENANT` | tenant only |
| **Equipment register** | **no** — its own cost field is inert | n/a | operational master data | **`TENANT`**, company-optional **correct** | tenant only |
| **Asset** | **YES** — depreciation posts | the company on the asset | legal / accounting truth | **`COMPANY`** | both |
| Manufacturing order | **YES** — consumes and produces inventory | the MO's company | accounting truth | **`COMPANY`** | both |
| Work order, time log | **YES** — evidence for conversion cost | the MO's company | accounting truth | **`COMPANY`** | both |
| Valuation layer | **YES** | the layer's company | accounting truth | **`COMPANY`** | both |
| Production / WIP accounts | **YES** | company-dependent by construction | accounting truth | **`COMPANY`** | both |
| Analytic plan / account | depends | — | **undetermined** | **`HOLD — SCOPE EVIDENCE REQUIRED`** | `SCOPE-Q-01`, P09-owned |

## 2. The two determinations that required care

**Equipment register — `TENANT`, and company-optional is *correct*.** Not because it is
shared, but because it produces **no financial effect**, so CORR1's question 7 has no subject.
P03 re-derived this independently rather than adopting P04's narrowing (`64` §2).

**Work centre — split.** The record fuses a `TENANT` resource and a `COMPANY` costing
parameter in one row whose company column is **nullable**. `MISSING REQUIRED SCOPE = DENY`.

## 3. `SCOPE-02` — mechanism stands, incidence measured

| | |
|---|---|
| Mechanism | the rate is a `COMPANY`-scoped financial parameter on a record with a nullable company. `CTR-P03-06`. **FACT VERIFIED** |
| **Incidence** | **0 of 60** — every work centre in the only deployment that has any carries `company_id = 1` |
| Severity | **High → Medium**, reduced on measured incidence, **not** on the mechanism |
| Status | **OPEN**, preserved for P11 |

**Why measured-zero does not close it:** a nullable column that nobody has yet left null is
still nullable, and the rule concerns what the system **permits**. That general question —
*can a defect with zero measured incidence but a permitted mechanism be closed?* — is
`P11-D-6`.

## 4. Dissent preserved

P03 does **not** extend P04's tenant narrowing from Equipment to Asset. §1 of
`P03_EQUIPMENT_OPERATION_COST_CAUSALITY.md` shows the two objects are **unlinked in both
directions**, so a scope conclusion about one carries no information about the other.
Preserved for P11 as `D-1`.

## 5. Disposition

> **`CQ-P03-08` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**, except the analytic plan
> row, which is **`EXTERNAL / CROSS-PROCESS OWNER`** (P09) and `SCOPE-Q-02`, which remains
> **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** pending a business-semantics decision.
