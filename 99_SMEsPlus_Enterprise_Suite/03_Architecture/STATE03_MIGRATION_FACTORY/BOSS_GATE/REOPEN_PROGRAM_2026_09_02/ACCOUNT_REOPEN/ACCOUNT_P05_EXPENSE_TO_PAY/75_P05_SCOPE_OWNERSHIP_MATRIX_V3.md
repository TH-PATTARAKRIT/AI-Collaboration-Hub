# 75 — P05 SCOPE OWNERSHIP MATRIX V3

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-10` · **PHASE S CANDIDATE**
Supersedes `22` and `31` for P05-owned objects. **Scope is derived per object, never blanket-enforced.**

`PLATFORM` — neither context required · `TENANT` — tenant required, company only if the operation is
company-scoped · `COMPANY` — both required. `MISSING REQUIRED SCOPE = DENY`.
`OWNERSHIP ≠ AVAILABILITY` · `OWNERSHIP ≠ CONFIGURATION ≠ EXECUTION ≠ FINANCIAL ≠ REFERENCE SCOPE`.

## 1. P05-Owned Objects and Events

| Object / event | Owns | Executes | Access | Mutate | Reference | Financial effect | Company owning it | Data character | Required context |
|---|---|---|---|---|---|---|---|---|---|
| Cost capture (`CI-01`..`CI-03`) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | not yet | the capture's company | COMPANY operational truth | Tenant + Company |
| Claim (grouping) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **yes at authorisation** | the claim's company | COMPANY accounting truth | Tenant + Company |
| **Authorisation act** | **TENANT policy, COMPANY execution** | COMPANY | TENANT | TENANT | COMPANY | gates one | company of the gated event | TENANT-owned policy | Tenant; **Company at execution** |
| Obligation / payable | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **yes** | the obligation's company | COMPANY legal truth | Tenant + Company |
| Accounting event (`CO-02`) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | **yes** | the event's company | COMPANY legal truth | Tenant + Company |
| **Cash float master** | **COMPANY** *(derived: its balance is a company's cash position)* | COMPANY | COMPANY | COMPANY | COMPANY | **yes** | undeterminable in the reference — no company field | COMPANY accounting truth | Tenant + Company |
| Expense category | **TENANT** | — | TENANT | TENANT | TENANT | no | n/a | TENANT catalogue | Tenant |
| — its account mapping | **COMPANY** | COMPANY | COMPANY | COMPANY | COMPANY | yes when applied | the reading company | COMPANY | Tenant + Company |
| Counterparty (employee contact / vendor) | **TENANT by default, COMPANY-restrictable** | — | TENANT | TENANT | TENANT | no | n/a | TENANT master data | Tenant; Company where the reference is company-constrained |
| — its payable account property | **COMPANY** | COMPANY | COMPANY | COMPANY | COMPANY | yes when applied | the reading company | COMPANY | Tenant + Company |
| **WHT rate + form classification** | **PLATFORM candidate** | — | PLATFORM | PLATFORM | TENANT/COMPANY | no by itself | n/a | statutory reference — **P07 owns the statute** | neither required for the rate |
| — its GL mapping | **COMPANY** | COMPANY | COMPANY | COMPANY | COMPANY | yes when applied | the mapping's company | COMPANY | Tenant + Company |
| Attribution dimension | **TENANT** (may be company-restricted) | COMPANY | TENANT | TENANT | COMPANY | no | n/a | TENANT dimension — **P09 owns the architecture** | Tenant; Company where restricted |
| Evidence artefact (receipt) | **TENANT** | — | TENANT, restricted | TENANT | COMPANY | no | n/a | TENANT document | Tenant |

## 2. Company Consistency Available Inside P05

| Control | Present? |
|---|---|
| Claim carries a required, non-editable company | **yes** |
| All claim lines must share the claim's company | **yes** — constraint |
| The funding instrument must belong to the claim's company | **yes** for the reimbursement journal |
| The **counterparty** must belong to the claim's company | **no early check** — enforced late, at accounting-artefact creation; **elevation does not bypass it** |
| The **cash float** must belong to a company | **NO — no company field exists on it** |
| Attribution must belong to the claim's company | derived through the engine, company passed but **not in the recompute trigger** |

## 3. Findings

| ID | Finding | Class |
|---|---|---|
| `SC-V3-01` | The cash float is **COMPANY-scoped by derivation** — its balance is a sum of posted entries on a company's account — yet carries **no company**, and its uniqueness constraint is global. | FACT VERIFIED (source). Cross-company consequence **not observed** in the 4-company target population — class **B**. |
| `SC-V3-02` | An operation with a company-owned financial effect resolves its **authoriser** through a tenant-level path without asserting the executing company. | FACT VERIFIED |
| `SC-V3-03` | The WHT configuration object **conflates PLATFORM statutory reference with COMPANY mapping** in one record, forcing per-company duplication with nothing keeping copies equal. On the v18 target: 40 codes / 4 accounts / 4 companies. | FACT VERIFIED (structural). **Statutory half is P07's — not asserted.** |
| `SC-V3-04` | Counterparty company-consistency fails **late, not early** — savable on a draft claim, erroring only at accounting-artefact creation. | FACT VERIFIED |

## 4. Boundary

This is **PHASE S learning only**. No cross-tenant event-chain orchestration was performed;
**AI EOS is NOT ACTIVE.** Tenant-model questions that depend on how SMEsPlus itself will be
partitioned remain `BOSS DECISION REQUIRED` and are not decided here.
