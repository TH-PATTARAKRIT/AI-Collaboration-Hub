# P08_SCOPE_AWARE_ACCOUNTING_MATRIX

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T11`

Targeted revalidation under `REV2-CORR1`. **Delta only** — the full assignment set is `01_P08_SCOPE_OWNERSHIP_MATRIX.md` and is not restated. This file answers the directive's requirement to separate **five** scopes per object, which the earlier matrix conflated into fewer columns.

Scopes: `PLATFORM` (no tenant, no company context) · `TENANT` (tenant mandatory) · `COMPANY` (tenant **and** company mandatory).

## 1. The five-way separation for the objects the directive names

| Object | Ownership | Configuration | Execution | Financial | Reference |
|---|---|---|---|---|---|
| Chart-of-accounts definition | `TENANT` | `TENANT` | `TENANT` | **none** | `COMPANY` |
| Ledger account | `TENANT` (identity) | `TENANT` | `TENANT` | **none directly** | `COMPANY` |
| Account number in a set of books | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` |
| Account group | `TENANT` (definition) | `TENANT` | `TENANT` | none | `COMPANY` (adoption) |
| Journal / book | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` |
| **Journal entry** | `COMPANY` | — | `COMPANY` | **`COMPANY`** | `COMPANY` |
| **Journal item** | `COMPANY` | — | `COMPANY` | **`COMPANY`** | `COMPANY` |
| Fiscal year | `COMPANY` | `COMPANY` | `COMPANY` | none | `COMPANY` |
| Lock date | `COMPANY` | **`TENANT` or above grants a derogation** | `COMPANY` | none | `COMPANY` |
| Currency | `PLATFORM` | `PLATFORM` | `PLATFORM` | none | any |
| Exchange rate — observation | `PLATFORM` | `PLATFORM` | `PLATFORM` | none | any |
| Exchange rate — policy | `TENANT` | `TENANT` | `TENANT` | none | `COMPANY` |
| **Exchange rate — as applied to a posting** | `COMPANY` | — | `COMPANY` | **`COMPANY`** | `COMPANY` |
| Statement definition — statutory | `PLATFORM` | `PLATFORM` | `PLATFORM` | none | `COMPANY` |
| Statement definition — management | `TENANT` | `TENANT` | `TENANT` | none | `COMPANY` |
| **Statement execution / produced statement** | `COMPANY` | — | `COMPANY` | **`COMPANY`** | `COMPANY` |
| Reconciliation model (matching rule) | `TENANT` (template) | `TENANT` | `COMPANY` (adoption) | **`COMPANY` in effect** | `COMPANY` |
| **Settlement record** | `COMPANY` | — | `COMPANY` | **`COMPANY`** | `COMPANY` |
| Accounting rule / posting policy | `TENANT` (definition, versioned) | `TENANT` | `COMPANY` | **`COMPANY`** | `COMPANY` |

## 2. The distinction the earlier matrix under-stated

**Configuration scope and financial scope diverge for four objects**, and the divergence is where the risk sits:

| Object | Configured at | Financial effect owned by | Consequence |
|---|---|---|---|
| Matching rule | `TENANT` | `COMPANY` | a tenant-scope configuration determines which account a company's posting hits |
| Exchange-rate policy | `TENANT` | `COMPANY` | a tenant-scope choice determines a company's measured amount |
| Posting policy | `TENANT` | `COMPANY` | a tenant-scope rule determines a company's accounting effect |
| Lock derogation | granted above the company | `COMPANY` | the company bears the effect of a permission it did not grant itself |

In every case the rule is the same and it is the generalisation of this session's central invariant:

> **A tenant-scope object may *determine* a company-scope financial effect, but it may never *rewrite* one, and the company-scope fact must record which version of the tenant-scope object produced it.**

That second clause is `K3` — the posting instruction — and it is the reason the kernel needs it. Without it, a tenant-scope configuration change silently re-attributes the meaning of company-scope facts already posted.

## 3. Deployment evidence bearing on scope

| Observation | Databases | Scope consequence |
|---|---|---|
| **44 companies** in two databases, **1** in the third | `DB-BK`, `DB-EV` / `DB-SM` | multi-company is real in this estate, so company-boundary findings are not theoretical |
| No tenant dimension exists on any accounting object | 22 of 22 roots | the `TENANT` scope must be **built**, not adapted. Every `TENANT` row above is a `DESIGN CANDIDATE`, not an observation |
| Statement definitions carry no company dimension | 22 of 22 roots | in a 44-company database, one ordinary accounting role edits the definitions that produce all 44 companies' statements |
| Settlement records carry no isolation rule | 22 of 22 roots | in a 44-company database, the settlement graph is unbounded by company at the object layer |

The last two are the scope findings the deployment evidence sharpens most: both were stated as source facts, and the presence of a 44-company database turns each into a live cross-company surface rather than a latent one.

## 4. Unresolved

| ID | Question | State |
|---|---|---|
| `P08-SC-U-01` | May one tenant hold companies with different statutory year-ends? | `HOLD — SCOPE EVIDENCE REQUIRED` |
| `P08-SC-U-06` | **New.** Is a matching rule a tenant template adopted per company, or a company object? The benchmark has no adoption step, so a tenant-scope edit takes effect in every company immediately | `BOSS DECISION REQUIRED AT FINAL GATE` — `P08-BD-18` |
| `P08-SC-U-07` | **New.** Must a posted fact record the **version** of the tenant-scope rule that produced it? P08 says yes on evidence; the cost is a design question | `P08-BD-19` |
