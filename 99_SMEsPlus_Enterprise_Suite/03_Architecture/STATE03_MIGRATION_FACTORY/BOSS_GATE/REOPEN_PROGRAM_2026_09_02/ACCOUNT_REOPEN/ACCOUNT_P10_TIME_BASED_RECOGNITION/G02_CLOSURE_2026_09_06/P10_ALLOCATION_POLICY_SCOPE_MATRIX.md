# P10 — ALLOCATION POLICY OWNERSHIP AND SCOPE  (`CQ-P10-05`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for where policy is owned and read · **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** for the runtime consequence, which needs an executing reproduction.

---

## 1. Where the Policy Lives

| Policy element | Stored on | Scope it *should* have | Scope it is *read from* |
|---|---|---|---|
| Generation method (validation / grouped) | the company | **COMPANY** | the **document's** company — correct |
| Control account and journal | the company | **COMPANY** | the **document's** company — correct |
| **Allocation convention** (day / month / full-month) | the company | **COMPANY** | **the ACTIVE company** — **defect** |

## 2. The Defect, Stated Precisely

**One flow reads two different companies.** The generation method, the control account and the journal are resolved from the company that owns the document. The **convention that decides the amounts** is resolved from whichever company is active in the session.

**Reachable three ways**, and the third does not require a multi-company user at all:

1. a user with several companies posting a document belonging to another;
2. a batch post across companies;
3. **the automatic posting routine** — it searches drafts with **no company filter** and posts them under the scheduler's own company context.

> Route 3 makes the mismatch **systematic rather than accidental**, and it is the route the deployed estate would use, because deferral entries are created for future periods and left to that routine.

## 3. The Scope Rule It Breaks

Under the scope-aware constitution the allocation convention is a **COMPANY-scoped binding value producing a COMPANY financial effect**. It is parameterised from the **executing** scope instead of the **owning** scope.

`OWNERSHIP SCOPE != EXECUTION SCOPE.` The correct behaviour when the owning scope cannot be proven is **DENY**; the observed behaviour is **silent substitution**.

**A second, structurally worse instance:** the grouped generation runs on a **report object that carries no company at all**, over a line population that may span companies, and creates one entry whose company is **back-filled from the journal**, falling back to the active company. Lock check and rounding precision consult only the active company. *Required ownership cannot be proven → the correct behaviour is DENY; the observed behaviour derives it.*

**And the correct pattern exists in the same product:** the accrual wizard carries a stored company, executes explicitly in that company's context, and **refuses outright** when the selection spans companies. It is the only mechanism that implements `MISSING REQUIRED SCOPE = DENY`.

## 4. Deployed Reachability

| | |
|---|---|
| Companies in the two multi-company databases | 44 each |
| Distinct configurations among them | **one, identical across all 88** |
| Therefore the convention mismatch can currently diverge | **No** |
| Accounts shared across companies | 1 of 544 in one database, 0 of 544 in the other |
| Therefore the cross-company generation would currently | most likely **fail loudly**, not post silently |

**Both mitigations are data states, not controls.** The first expires the first time any company's configuration differs; the second the first time a second account is shared. Neither is a guard, and neither was designed.

## 5. Scope Determination — six axes

| Object | Ownership | Configuration | Execution | Recognition | Financial effect | Reference |
|---|---|---|---|---|---|---|
| Convention **definition** (30/360, actual) | PLATFORM | PLATFORM | PLATFORM | n/a | none | any |
| Convention **tenant standard** | TENANT | TENANT | TENANT | n/a | none directly | COMPANY |
| Convention **binding value** | COMPANY | COMPANY | **ACTIVE company — defect** | COMPANY | yes | COMPANY |
| Control account / journal | COMPANY | COMPANY | COMPANY | COMPANY | yes | COMPANY |
| Grouped generation object | **carries no company at all** | — | **derived** | COMPANY | yes | COMPANY |

**Deliberately not COMPANY-scoped, and this survives revalidation:** the convention *definition* is PLATFORM reference data — a company owns the *choice*, not the definition of 30/360.

## 6. Disposition

- Ownership and read-scope of each policy element: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- The two scope defects: **`FACT VERIFIED`** in code; **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`** for the observable consequence, which requires an executing reproduction. Obtaining it needs a database service started on the host — **`CLASS D`, named HOLD, Boss/operator authorisation**, and P10 will not make that state change read-only
- Whether a tenant may **bind** rather than default a convention: **`BOSS DECISION REQUIRED`**
