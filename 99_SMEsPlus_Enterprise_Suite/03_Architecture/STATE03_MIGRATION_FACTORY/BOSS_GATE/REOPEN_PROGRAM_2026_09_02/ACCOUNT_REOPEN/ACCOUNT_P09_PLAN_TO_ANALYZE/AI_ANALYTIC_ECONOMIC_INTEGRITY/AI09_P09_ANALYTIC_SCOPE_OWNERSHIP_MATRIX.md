# AI09 — P09_ANALYTIC_SCOPE_OWNERSHIP_MATRIX (targeted revalidation)

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Supersedes nothing.** Extends `19_P09_SCOPE_OWNERSHIP_MATRIX` in the base package with the six-scope decomposition the continuation directive requires, and re-tests `MA-11`.
**Layer:** 1 — clean-room.

---

## 1. WHY A REVALIDATION IS NEEDED HERE

The base matrix determined **ownership** scope per object. The continuation directive requires six scopes to be distinguished for each analytic object, because the zeroing defect is partly a scope failure: **the object that decides whether an allocation happens and the object that carries the money are not the same object and are not the same scope.**

## 2. THE SIX-SCOPE DECOMPOSITION

| Analytic object | Ownership | Applicability | Execution | Financial effect | Management attribution | Reference |
|---|---|---|---|---|---|---|
| **analytic plan (axis)** | TENANT | TENANT, company-qualified by the obligation rule | TENANT | **none** — it carries no amount | defines the *dimension* only | TENANT |
| **analytic account (axis value)** | TENANT default; COMPANY where it denotes a legal-entity object | TENANT | TENANT | **none** | is the *target* of attribution | TENANT, available to the tenant's companies |
| **allocation on a journal row** | COMPANY (follows its carrier row) | COMPANY | COMPANY | **indirect** — it does not post, it directs | decides *which* target | COMPANY |
| **management record (analytic item)** | **COMPANY** | COMPANY | COMPANY | **it represents one**, and carries the amount | **is** the attribution | COMPANY |
| **journal row** | COMPANY | COMPANY | COMPANY | **yes — canonical** | is the *source* | COMPANY |
| **cost centre / cost object** | TENANT or COMPANY by type | TENANT | COMPANY | none directly | is the *accountable thing* | TENANT |
| **obligation rule (applicability)** | TENANT | TENANT, optionally company-qualified | TENANT | **none** | decides whether attribution is *required* | TENANT |
| **budget** | TENANT or COMPANY, declared per record | per declared scope | COMPANY | none | *consumes* attribution | per scope |
| **management report result** | scope of the declared aggregation | declared | declared | none | *presents* attribution | derived |

## 3. RE-TEST OF `MA-11`

> **MA-11** *(adopted from `P04-PD-04`)* — the object carrying an obligation or control must have scope consistent with the fact it governs.

**Re-tested against the zeroing defect. MA-11 holds, and the defect is a second, independent instance of it.**

| Instance | The obligation | The object carrying it | Its scope | The fact governed | Its scope | Mismatch? |
|---|---|---|---|---|---|---|
| **the one P04 found** | "this axis must be filled" | the analytic plan's applicability rule | **TENANT** | the attribution of a company's financial amount | **COMPANY** | **yes** |
| **the one this continuation finds** | "this row's economic effect belongs to cost centre CC" | the allocation on a **row** | **COMPANY**, but scoped to **one row** | the economic effect of the **event**, which spans several rows | **COMPANY, event-level** | **yes — a scope mismatch in *granularity*, within the same tenant and company** |

**AI-S-01 — MA-11 is generalised.** A control must match the fact it governs in **scope *and* in granularity**. An allocation attached to a single row cannot express an attribution whose subject is a multi-row event. The zeroing defect is the arithmetic consequence: the row-level carrier has no way to know that another row of the same event carries the same allocation with the opposite balance.

This is a stronger statement than the base package's `EA-06`, which said *do not allocate both legs*. `AI-S-01` says *the carrier is at the wrong granularity to make that rule expressible.* Forbidding both-legs allocation is a rule a developer must remember; putting the carrier at event level makes the rule structural.

## 4. THE SCOPE ANSWER TO THE DIRECTIVE'S QUESTION 17

> *Does company ownership determine eligibility?*

**No.** Eligibility is determined solely by whether a row was given an allocation (`AI02` §1). Company participates nowhere in the eligibility test. The base package already established that the company-consistency check between a row and its axis values fires on one axis only and cannot attach to the allocation payload at all (`EC-21`, `EC-22`, both confirmed by independent challenge). **This continuation adds nothing that changes those, and withdraws nothing.**

Consequence for scope: a management record's company is inherited from its source row, so a symmetric pair is always within one company — **the zeroing defect is a within-company defect and is not a tenant-boundary defect.** It must not be conflated with the boundary findings; they are independent.

## 5. SCOPE-AWARE STATEMENT OF THE DEFECT

- **Ownership scope:** COMPANY. Both records belong to the posting company.
- **Financial effect scope:** COMPANY. The financial effect is correct and undisturbed — the ledger is right.
- **Management attribution scope:** COMPANY, **and it is wrong** — the net attribution is zero where the economic cost is `X`.
- **Reference scope:** TENANT. The axis and axis value are correct and undisturbed.

**The failure is confined to exactly one of the six scopes.** That is a precise and useful result: it tells SMEsPlus that the fix belongs in the management-attribution layer alone, and that no tenant, company, reference or financial control would have caught it.

## 6. CHECKPOINT

**CP-AI09 — SCOPE REVALIDATION COMPLETED.** `MA-11` upheld and generalised to granularity as `AI-S-01`. No prior scope determination withdrawn. Auto-continue.
