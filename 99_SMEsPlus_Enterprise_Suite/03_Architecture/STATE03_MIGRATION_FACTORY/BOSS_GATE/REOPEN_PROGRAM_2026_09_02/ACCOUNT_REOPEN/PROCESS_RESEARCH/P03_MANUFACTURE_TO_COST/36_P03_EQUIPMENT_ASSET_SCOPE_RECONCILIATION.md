# 36 — P03 EQUIPMENT / ASSET SCOPE RECONCILIATION

**LAYER 2 — AUDIT QUARANTINE.** Under `REV2-CORR1` — SCOPE-AWARE EVERYWHERE.

The directive is explicit: **do not assume Equipment = Asset**, and do not promote P04's
reported correction into universal fact until evidence supports it. Re-derived here.

---

## 1. Are they the same object? — executed

| Test | Result |
|---|---|
| Does a maintenance-equipment record reference an asset? | **No such field.** `05_P04_ASSET_EQUIPMENT_RELATIONSHIP.md` establishes it; P03 confirms no asset reference exists anywhere in the manufacturing modules |
| Does an asset reference equipment? | **No** |
| Does an operation reference equipment? | **No** — the routing-operation model declares 20 fields, none an equipment reference |
| What is the only equipment link? | equipment → **work centre**, from the maintenance bridge |
| Row counts | `maintenance_equipment` **0** in `BK12MAY26`; `account_asset` **36** there, **685** in `iSMEs` |

> **Equipment and Asset are disjoint objects with no reference between them in either
> direction.** The chain is `asset (X) equipment → work centre ← operation`, broken on the
> asset side and again immediately after. `FACT VERIFIED`.

**They are therefore not merely scoped differently — they are different objects**, and any
scope conclusion that treats them as one is wrong before scope is even considered.

## 2. Scope derived per object, from its own semantics

Applying CORR1's questions rather than inheriting P04's answer.

### Equipment register

| Question | Answer |
|---|---|
| Does it create a financial effect? | **No.** It carries no cost that posts; its own cost field is inert (`ASSET_DR_CONTINUATION/06` §4) |
| Which company owns that effect? | **Not applicable** — there is none |
| Platform reference, tenant-owned, or company legal truth? | **Tenant-owned operational master data** |
| **Ownership scope** | **`TENANT`** |
| Company context required? | **No** — requiring it would be over-constraint |

**P04's correction is confirmed by independent derivation, not adopted.** Company-optional
is correct for the equipment register.

### Asset

| Question | Answer |
|---|---|
| Does it create a financial effect? | **Yes** — depreciation posts to the ledger |
| Which company owns that effect? | The company on the asset; the depreciation entry is company-scoped |
| Nature | **Company legal / accounting truth** |
| **Ownership scope** | **`COMPANY`** |
| Company context required? | **Yes — mandatory** |

### Work centre — the object that decides the disagreement

| Question | Answer |
|---|---|
| Does the **resource** create a financial effect? | No — it is a calendar, a capacity and an alternatives group |
| Does the **rate on it** create a financial effect? | **Yes** — it lands in inventory valuation via `M1`/`M2` |
| Which company owns that effect? | **Unanswerable** where `company_id` is null |
| **Verdict** | The record fuses a `TENANT` resource and a `COMPANY` costing parameter in one row that may have **no company at all** |

`MISSING REQUIRED SCOPE = DENY.` Carried as `SCOPE-02` / `P04-B-35`.

## 3. The full scope table

| Object | Ownership | Configuration | Execution | Operational | Cost | Financial | Reference |
|---|---|---|---|---|---|---|---|
| Equipment register | `TENANT` | `TENANT` | `TENANT` | `TENANT` | — | — | `COMPANY` may reference |
| Asset | `COMPANY` | `COMPANY` | `COMPANY` | `TENANT` may view | `COMPANY` | **`COMPANY`** | `COMPANY` |
| Work centre — resource | `TENANT` | `TENANT` | `TENANT` | `TENANT` | — | — | `COMPANY` |
| **Work centre — rate** | **`COMPANY`** | **`COMPANY`** | `COMPANY` | — | **`COMPANY`** | **`COMPANY`** | `COMPANY` |
| Routing operation | `TENANT` | `TENANT` | `TENANT` | `TENANT` | — | — | `COMPANY` |
| Cost allocation / analytic | **unresolved** — `SCOPE-Q-01`; P09 records plans have **no company field at all** | | | | | | |
| Financial posting | `COMPANY` | `COMPANY` | `COMPANY` | — | `COMPANY` | **`COMPANY`** | — |

## 4. Where P03 does **not** follow P04

P04's narrowing is correct **for the equipment register**. P03 does not extend it to the
asset, and P04 did not ask it to. The dissent is preserved because a later reconciliation
could read the narrowing too broadly:

> **P03 position.** An object whose depreciation is a company-scoped financial effect
> cannot itself be tenant-scoped. Equipment being `TENANT` says nothing about Asset,
> because §1 shows they are **not the same object and are not even linked**.

Preserved for P11 — `37`.

## 5. The correction to P03's own prior matrix

`18` §3 originally carried one row, *"Machine / equipment — `COMPANY`"*. That conflated the
two objects. Corrected in `25` §6 as `REV-S-05`, P03's first downgrade under CORR1, and
re-derived independently here rather than left resting on P04's say-so.

**The re-derivation matters** because `smeplus-peer-intake-discipline` warns that adopting a
peer's route unexamined imports their scoping error under your own classification. Here the
route survives examination — but §1's finding that the two objects are **unlinked** is
stronger than P04's framing, and it is P03's own.

## 6. `MA-11` adopted from P09

> *A company-scoped attribution requirement shall never be enforced through a tenant-scoped
> structure.*

P03 adopts it as directly on point: the work-centre rate is a company-scoped financial
parameter enforced through a tenant-scoped resource record. **`SCOPE-02` is an instance of
`MA-11`**, which is P09's principle, cited not re-derived.
