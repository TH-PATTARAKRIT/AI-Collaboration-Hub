# P10 — SCOPE OWNERSHIP MATRIX  (`CQ-P10-11`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the determinations · **`BOSS DECISION REQUIRED`** for two normative scope questions.

`Scope-aware everywhere. PLATFORM / TENANT / COMPANY determined per object and per operation. Tenant + Company is NOT blanket-enforced.`

---

## 1. The Matrix — six axes

| Object | Ownership | Configuration | Execution | Recognition | Financial effect | Reference | Expiry |
|---|---|---|---|---|---|---|---|
| Day-count convention **definition** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | — |
| Period-grid **algorithm** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | — |
| Recognition **event schema** | PLATFORM | PLATFORM | PLATFORM | n/a | none | any | **`D-5`** |
| Service / benefit **window** | **TENANT** | TENANT | TENANT | referenced by COMPANY | none directly | COMPANY | — |
| Allocation convention **tenant standard** | **TENANT** | TENANT | TENANT | n/a | none directly | COMPANY | **`P10-D-04`** |
| Fiscal calendar instance | COMPANY | COMPANY | COMPANY | COMPANY | none directly | COMPANY | — |
| Allocation convention **binding value** | COMPANY | COMPANY | **ACTIVE company — defect** | COMPANY | yes | COMPANY | — |
| Control accounts and journals | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **base** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **event** | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | **`D-5`** |
| Posting act | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY | — |
| Recognition **attribution** | COMPANY *required* | **structure has no company field** | COMPANY | COMPANY | yes | COMPANY | **cost object** |
| Recognition **report object** | COMPANY data | COMPANY | **derived — defect** | COMPANY | yes when generating | COMPANY | — |

**13 determinations · 0 changed this round · 3 carry expiry triggers · 4 deliberately NOT company-scoped.**

## 2. The Four That Are Deliberately Not COMPANY

Restated because a blanket tenant+company reading would get all four wrong, and because they survived revalidation:

1. **Convention definitions** are PLATFORM reference data. A company owns the *choice*, not the definition of 30/360.
2. **The period-grid algorithm** is PLATFORM. The company owns its fiscal calendar, not the arithmetic that cuts a window against it.
3. **The event schema** is PLATFORM today and passes to the ledger owner on `D-5`. The *instances* are COMPANY.
4. **The service window is a TENANT fact.** One contract billed by two companies of one tenant has **one** window. Forcing it to COMPANY would duplicate a customer fact per legal entity and make inter-company recharge incoherent.

## 3. Company Consistency — verified per object

| Object | Consistency enforced? |
|---|---|
| Control account and journal | **yes** — read from the document's company |
| Allocation convention | **NO** — read from the active company |
| Grouped generation | **NO** — the object carries no company; the entry's company is back-filled from the journal |
| Source-document ↔ generated-entry links | **NO company check**, and written by raw SQL on one path |
| Accrual | **YES** — stored company, explicit context, **refuses** a mixed-company selection |
| Asset, loan | **yes** — company set explicitly on every generated entry |

**The accrual is the pattern to copy: it is the only mechanism implementing `MISSING REQUIRED SCOPE = DENY`.**

## 4. Absent Scope Values

`"unset" may never mean "all".` The attribution structure has **no company field at all**. Under the superseded reading that would be "available to every company". Under the rule it is **undefined**, and missing required scope **denies**.

> **P10's determination: recognition attribution may not be enforced, relied upon, or reported as company truth through the present structure.** That is a constraint P10 places on its own design, not a demand on the analytic process, which found and published the defect.

## 5. Expiry Triggers

| # | Determination | Expires on |
|---|---|---|
| `SX-01` | Event schema is PLATFORM | **`D-5`** — if an accounting-event object is authored, the schema passes to the ledger owner and this is **superseded**, not revised |
| `SX-02` | Convention is a TENANT default and a COMPANY binding value | **`P10-D-04`** — a ruling that a tenant may *bind* converts it |
| `SX-03` | Attribution is COMPANY-required and structurally scopeless | **authoring of the cost object**, which does not exist as a first-class object |

**And two exposure mitigations are data states, not controls:** all 88 companies holding one identical configuration; the chart being near-unshared. Each expires on the first change to that data.

## 6. Cross-Process Comparison

**Six of seven scope objects have never been compared with any peer's determination.** For most, comparison is **currently impossible** — no peer has published a determination for the same object. P10 cannot compare its determination with silence and must not read silence as agreement.

**One was compared this round:** recognition attribution. The analytic process reached, independently, that a company-scoped attribution requirement must never be enforced through a tenant-scoped structure. **Agreement — and both are positions, not adopted boundaries. Neither may be used to eliminate an option.**

## 7. Disposition

- The 13 determinations: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- The two scope defects: **`FACT VERIFIED`** in code, **`UNRESOLVED`** for the observable consequence
- Whether a tenant may **bind** a convention: **`BOSS DECISION REQUIRED`**
- Whether a shared chart of accounts is permitted: **`BOSS DECISION REQUIRED`** — it decides whether the second defect fails loudly or silently
- Cross-process comparison of six objects: **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** (P11)
