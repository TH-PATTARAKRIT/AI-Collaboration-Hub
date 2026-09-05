# P10 — SCOPE REGISTER

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Consolidated. Six axes per object, per the scope-aware constitution. **Tenant and Company are not imposed on every object.**

---

## 1. The Register

| Object | Ownership | Configuration | Execution | Recognition | Financial effect | Reference | Expiry |
|--------|-----------|---------------|-----------|-------------|------------------|-----------|--------|
| Day-count convention **definition** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | — |
| Period-grid **algorithm** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | — |
| Recognition **event schema** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | **`SX-01`** |
| Service / benefit **window** | TENANT | TENANT | TENANT | referenced by COMPANY | none directly | COMPANY | — |
| Allocation convention **tenant standard** | TENANT | TENANT | TENANT | n/a | none directly | COMPANY | **`SX-02`** |
| Fiscal calendar instance | COMPANY | COMPANY | COMPANY | COMPANY | none directly | COMPANY | — |
| Allocation convention **binding value** | COMPANY | COMPANY | **active company — defect** | COMPANY | yes, indirectly | COMPANY | — |
| Control accounts and journals | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **base** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **event** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **`SX-01`** |
| Posting act | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **attribution** | COMPANY required | **structure has no company field** | COMPANY | COMPANY | yes | COMPANY | **`SX-03`** |
| Recognition **report** | COMPANY data | COMPANY | **derived — defect** | COMPANY | yes when generating | COMPANY | — |

**13 determinations · 0 changed this round · 3 carry expiry triggers · 4 deliberately not COMPANY-scoped.**

## 2. Rules Applied

| Rule | Applied to |
|------|-----------|
| An **absent** scope value is undefined, never universal; missing required scope denies | The attribution structure, which has no company field |
| A company-scoped attribution requirement may not be enforced through a tenant-scoped structure | Adopted from `P09` as a P10 design constraint |
| A determination taken against behaviour the programme must change is time-indexed | `SX-01`, `SX-02`, `SX-03` |
| A mitigation that is a data state is not a control | Two exposure mitigations — identical configuration across 88 companies, and near-unshared charts |

## 3. Two Scope Defects, Unchanged

`P10-S-01` — the allocation policy is resolved at the **executing** scope, not the owning one. Reachable through the automatic posting routine even in a single-company tenant. **Mitigated today only by all 88 companies holding one identical configuration**, which expires on the first divergence.

`P10-S-02` — a scopeless report object performs a company-scoped act, with the owning company **derived rather than asserted**. Mitigated today only by the chart being near-unshared.

Both remain source-verified and unreproduced; both sit under `EC-04` components `TZ-4` and `TZ-5`.

## 4. Comparison Status

**Six of seven scope objects have never been compared with any peer's determination** — class `C`, and for most of them a comparison is currently **impossible** because no peer has published one. See `55`.
