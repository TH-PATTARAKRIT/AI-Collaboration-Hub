# P11 — SAAS ACCOUNTING BOUNDARY

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 13 of 15 · Layer 1 clean-room
Governed by constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1`.
**Detailed determinations live in `P11_SCOPE_OWNERSHIP_MATRIX.md`; this file states the boundary.**

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The boundary, corrected

| Boundary | Definition | Consequence for accounting |
|---|---|---|
| `PLATFORM` | shared reference truth | No tenant or company context required. Currency definitions, statutory rate references, standard chart templates, standard report definitions |
| `TENANT` | **security / customer boundary** | Tenant context mandatory. Product master (Boss ruling `D-01`), analytic dimension definitions, tenant-authored reports, control evidence, migration batch identity |
| `COMPANY` | **legal / accounting / business boundary** | Both contexts mandatory. **Every object with a financial effect** (`SCP-04`) |

`UNRELATED INDEPENDENT COMPANIES = SEPARATE TENANTS BY DEFAULT.` This narrows `DC-13` and `PC-05`
materially: cross-company coupling can only occur **inside** a tenant (`RV-04`).

## 2. The reference model's position, and the gap

**No tenant concept exists.** The outermost boundary is the **company group** — a root company and its
descendants. Structures keyed to the group root rather than the company: **account codes, currency
rates, fiscal years**. In a deployment where multiple tenants share one database, those are shared at
exactly the level a SaaS must keep separate.

This is a **boundary mismatch**, not a defect in a system that was never built for that deployment. It
is SMEsPlus's to close deliberately, and under the correction the closure is **scope declaration**
(`F8`), not field addition.

## 3. The boundary failures, ranked

| Rank | id | Failure | Severity |
|---|---|---|---|
| 1 | `SC-01` / `SB-01` | The numbering/date-alignment control store has **no dimension at all**. One write disables a control **for every tenant in the database, invisibly** — and that control **moves accounting dates** | **highest** |
| 2 | `SC-02` / `MCU-04` | Report definitions: two scopes, one model, no record rule in 6 roots, full create/write/unlink; **`CLOSED — VERIFIED DEFECT`** on the `T0-04` tenant boundary | high |
| 3 | `SC-05` / `T0-07` | FX rate: `PLATFORM` observation and `COMPANY` selection collapsed into one object; 10 bypassing readers, **five** fallback semantics; behaviour differs across **5 of 22** roots | high, **`UNRESOLVED`** |
| 4 | `SC-06` / `SB-02` | `account × 10000 + company` aliases silently once any company identifier reaches 10,000 — reached by **cumulative creation, not live count** | high |
| 5 | `SC-07` / `SB-03` | Hash chain keyed on storage row identifiers; **cannot survive a tenant split, merge, restore or migration — precisely when assurance matters most** | high |
| 6 | `SC-08` / `SB-04` | Control evidence written to the application log — **leaves the tenant's data entirely** | high |
| 7 | `SC-04` | Fiscal year is refused to child companies — **a company cannot declare its own legal period** | material |
| 8 | `SC-03` / `FC-A1` | Report-created menus: no company field, no record rule | material |
| 9 | `SC-09` | Hard-lock cascade — **narrowed by `RV-04`** to related companies inside one tenant | material |

## 4. Boss question 16 — the standard-vs-tenant distinction

The reference model **cannot answer it**, because **it retains no record of which accounts came from
the template.** Once provisioned, template accounts and tenant accounts are indistinguishable.

Under the correction this is no longer a chart-of-accounts question. It is `SCP-03` — *an object that
serves two scopes must be two objects* — and it has **three** instances, not one: chart entries,
report definitions (`SC-02`) and the FX rate table (`SC-05`). **Recognising them as one defect with
three instances is a P11 contribution.**

## 5. Tenant isolation requirements, restated

| id | Requirement | Change under the correction |
|---|---|---|
| `TI-01` | ~~No configuration may have database-wide effect~~ → **a `TENANT`- or `COMPANY`-scoped value may not be held in a store of wider scope** | **corrected** (`RV-01`, `SCP-02`) |
| `TI-02` | No identity encoded by arithmetic over other identities | unchanged |
| `TI-03` | Tamper-evidence keys on business identity | unchanged |
| `TI-04` | All control evidence stored inside the tenant's own data | unchanged (`SCP-06`) |
| `TI-05` | Template-derived and tenant-created configuration remain distinguishable for the life of the tenant | **generalised** to all three instances (`SCP-03`) |
| `TI-06` | Tenant isolation of ledger data and controls is a `Tolerance = 0` candidate | unchanged — and `T0-04` **remains `UNRESOLVED`** |
| **`TI-07`** | **Every material object declares its scope as a non-null property; `MISSING REQUIRED SCOPE = DENY` is enforced at the point of effect** | **new** (`SCP-01`, `SCP-05`) |
