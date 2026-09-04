# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 02 — `MTI-D-01` / `MTI-D-02` / `MTI-D-03` Ruling Consolidation

Control Level: `/L9999.9999`
Status: `THREE RULINGS CONSOLIDATED — DECIDED BY BOSS — NOT PROOF, NOT CLOSURE, NOT DEVELOPMENT FINAL GATE`

---

## 1. What Has Now Been Decided By Boss — The Answer To Question 1

Three decisions, and exactly three. Each is stated below in the ruling's own words, then in its binding operational form.

| Decision | Topic | Boss Ruling | Ruling File | Commit |
|---|---|---|---|---|
| `MTI-D-01` | Product Master Scope | **`Option B — Company-owned Product Master / tenant-company scoped product identity`** | `24_BOSS_RULING_…MTI-D01-PRODUCT-MASTER-SCOPE-001.md` | `d84fe49` |
| `MTI-D-02` | Authorization Granularity | **`Company + Warehouse + Operation-Type`** | `26_BOSS_RULING_…MTI-D02-AUTHORIZATION-GRANULARITY-001.md` | `13b3e63` |
| `MTI-D-03` | Tenant-Changeable Boundary | **`Platform-owned Core + Tenant Config Overlay`**, with a Private Company option opened through Gate | `28_BOSS_RULING_…MTI-D03-TENANT-CHANGEABLE-BOUNDARY-001.md` | `6897cc9` |

**These three were items 1, 2 and 3 of the invariant-set Boss Decision List, and rank 1 of the invariant-set PMO recommendation.** Rank 1 is discharged as a Boss act. Items 4 through 11 of that list are **untouched** by these rulings and remain exactly as tabled.

---

## 2. `MTI-D-01` — Product Master Scope

### 2.1 The binding decision

Product identity is **scoped by tenant/company context**. Each tenant/company sees and operates only its own product, configuration, inventory, valuation context, routes, rules, packaging, lots and serials, and reports.

### 2.2 The eight binding interpretation rules, carried exactly

1. Product identity is scoped by tenant/company context.
2. Product code / name / barcode / UoM similarity must **never** create shared identity across tenants/companies.
3. Cross-tenant product deduplication is **not** a requirement.
4. Cross-company product deduplication is **not** a default requirement.
5. Any cross-company or group-level comparison must use an **explicit controlled mapping layer**, not a shared product master.
6. Inventory, Sale, Purchase, Manufacturing, Accounting, Reporting, Approval and Document must consume product identity **through tenant/company context**.
7. Migration **may preserve duplicate products** across tenants/companies where that reflects source business reality.
8. Reporting may aggregate **only after an explicit authorized mapping exists**.

### 2.3 The business reason, recorded because it governs interpretation

Boss's stated reason is operational and legal separation per customer/company, with the worked example of two companies performing what looks like the same transport service under different withholding-tax conditions. **Similar name does not imply same object.** Where a downstream reading of any rule above would collapse two business objects because they look alike, that reading is wrong.

### 2.4 What the ruling supersedes

The ruling **supersedes the earlier AAS+ recommendation** that preferred a tenant-level product master with company-level attachment. AAS+ has formally corrected its own position (`25_AAS_PLUS_ADVICE_CORRECTION_MTI_D01_OPTION_B_2026_09_04.md`), stating that its prior recommendation *over-weighted duplicate reduction and under-weighted the Boss's SaaS separation objective*.

### 2.5 Required carry-forward wording

The ruling and the AAS+ correction each prescribe carry-forward wording. Both are reproduced so that downstream prompts may cite either:

> `MTI-D-01 = OPTION B — Company-owned Product Master / tenant-company scoped product identity.`

> `MTI-D-01 is ruled as Option B: Product Master is tenant/company scoped. Similar products across tenants/companies are separate business objects unless an explicit Boss-authorized mapping layer links them for reporting or migration purposes.`

### 2.6 What the ruling explicitly leaves unaffected

The ruling itself enumerates these, and this session carries them unchanged: `MTI-D-02` and `MTI-D-03` remained open at the time of the ruling (both now ruled); `RISK-U03` / `GAP-FS-10` remains open; `0 of 8` L9 proofs unchanged; `0 of 22` cross-proof scenarios unchanged; Accounting COGS dependency remains `HOLD`; **no development is authorized**.

---

## 3. `MTI-D-02` — Authorization Granularity

### 3.1 The binding decision

`Company + Warehouse + Operation-Type`. Inventory permission and execution context must be controlled by **all applicable dimensions**: tenant/company, warehouse, and operation type.

### 3.2 The eight core control rules, carried exactly

1. A tenant/company must never see, select, search, report, infer or operate another tenant/company's inventory records.
2. A user authorized for one warehouse is **not** automatically authorized for every warehouse in the same company.
3. A user authorized for one operation type is **not** automatically authorized for every operation type in the same warehouse.
4. Operation Type does not replace Company or Warehouse context.
5. Warehouse does not replace Company context.
6. Company context does not replace Tenant isolation.
7. Inventory reports, valuation views, replenishment views, adjustments, transfers, scrap, landed cost flows, scheduler actions and stock movement history must preserve the same authorization context.
8. Background jobs and system automation must carry **explicit** tenant/company/warehouse/operation-type context when executing inventory actions.

### 3.3 The operation types named as examples

Receipt · Delivery · Internal Transfer · Inventory Adjustment · Scrap · Replenishment · Landed Cost review/action · Scheduler-controlled replenishment or reservation actions.

The ruling states this list as *"including, but not limited to"*. It is an illustration, **not a closed enumeration**, and no downstream design may treat it as one.

### 3.4 The decision this closes upstream

`RISK-U01` / `U-01` — *"whether user rights can be scoped to a warehouse or a storage place"*, recorded in prior evidence as **"not merely undesigned — unevidenced either way"** — is a Boss scope ruling, and it is now taken. The R4 review's rank 9 ("rule on authorization scope `U-01`") is **discharged as a decision**.

### 3.5 What the ruling does not say, stated without re-litigating it

The invariant set prepared three shapes at `04` §7: company-only, warehouse-level, and *"location- or operation-class-level"*. **Boss ruled the operation-class half of the third shape and the warehouse axis, and did not name `location`.**

Applied as written, `AUTH = (tenant, company, warehouse, operation type)`. That is the shape this package uses throughout, and it is the correct reading of a ruling that lists three dimensions.

What is not settled is whether a **location** axis is thereby excluded or merely not required. The two readings differ for five matrix rows that the invariant set assigned to the finest filter. This is recorded as a clarification item (`RC-D-01` at `09`), **not** as a challenge to the ruling; design proceeds on the three axes ruled, and the residual is registered rather than assumed away in either direction.

---

## 4. `MTI-D-03` — Tenant-Changeable Boundary

### 4.1 The binding decision

`Platform-owned Core + Tenant Config Overlay`. In the shared SaaS pool the platform core remains centrally owned; tenant/company-specific behaviour is expressed through **controlled configuration and master data overlays only**.

### 4.2 What a tenant may configure — the ruling's list

Warehouse · Location · Route · Rule · Operation Type · Putaway Rule · Reordering Rule · Storage Category · Product Category · Unit of Measure Category · Barcode Nomenclature · **"Other approved Inventory configuration/master records"**.

### 4.3 What the shared SaaS pool must never allow

Customer-specific changes that fork **platform source code**, **database schema**, **posting engine behaviour**, **authorization engine behaviour**, **immutable event logic**, or **cross-tenant isolation rules**.

### 4.4 The Private Company option

Where a customer has requirements that cannot be safely handled inside the shared pool, that customer **may** be separated into a `Private Company` operating model. The ruling is explicit and this package treats it as binding:

- The option **may be opened when required**.
- It **must pass controlled governance before use**.
- It is **not a bypass** for evidence, authorization, audit, tenant isolation, or Boss approval.
- Separation **requires an explicit Gate record, evidence, and a Boss ruling** before downstream implementation.

**Private Company is therefore an option, not a state. No customer is in it, no criteria for entering it exist, and nothing in this package treats it as approved.**

### 4.5 The six binding control rules, carried exactly

1. Platform-owned core logic remains centrally controlled.
2. Tenant/company configuration must not modify platform source logic.
3. Tenant/company configuration must not weaken `MTI-D-01` product isolation.
4. Tenant/company configuration must not weaken `MTI-D-02` authorization.
5. Shared pool customization must remain configuration-led, evidence-backed, reversible where applicable, and auditable.
6. Private Company separation requires explicit Gate record, evidence and Boss ruling before downstream implementation.

### 4.6 The AAS+ caution, carried because it governs interpretation

*Tenant Config Overlay* must not be read as permitting uncontrolled customer customization. Where a requirement needs source-level behaviour, schema-level divergence, posting-behaviour divergence or isolation-rule divergence, AAS+ advises moving it to **Private Company evaluation** rather than modifying the shared pool. And: where a requirement **cannot be classified** as pool-safe or Private-Company-required, **the item remains `HOLD` until classification evidence exists.**

That last clause is the origin of the `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` status used at `09`.

---

## 5. Are The Three Rulings Mutually Consistent? — `L5`

Tested directly, because three rulings taken on three days by one authority against a moving design are exactly where an inconsistency would hide.

| Pair | Test | Result |
|---|---|---|
| `D-01` × `D-02` | Does company-scoped product identity conflict with warehouse/operation-type authorization? | **No.** They compose cleanly. `D-01` narrows *what exists in a context*; `D-02` narrows *who may act within it*. `D-02` rule 6 ("company context does not replace tenant isolation") and `D-01` rule 1 state the same spine from two directions |
| `D-01` × `D-03` | May a tenant configure product master records, given products are company-owned? | **Consistent, and `D-03` says so.** Product Category and UoM Category are named as tenant-configurable; `D-03` rule 3 forbids configuration from weakening `D-01` isolation. Company-owned product master and tenant-configurable product category coexist because the category is configuration and the product is a business object |
| `D-02` × `D-03` | May configuration weaken the authorization axes? | **No, explicitly.** `D-03` rule 4 forbids it, and lists the authorization engine among the things configuration may never fork |
| All three × the SaaS pool | Do the three together define a coherent pool? | **Yes for the pool. No for the second lane.** All three are written for the shared pool. **None of them specifies how any rule changes, or does not change, inside a Private Company.** See `05` §5 |

**Verdict: the three rulings are mutually consistent. The inconsistency in the evidence is not between rulings — it is between `MTI-D-01` and the design that preceded it.** See `03` §3.

---

## 6. What The Rulings Decide, And What They Explicitly Do Not

This is the distinction the whole package turns on, and each ruling states it in its own §7 or §6.

| Dimension | Position After All Three Rulings |
|---|---|
| **The shape of what may be built** | **Decided.** Where product identity lives, how many axes authorization has, and what a tenant may change |
| **That the shape is correct for the market** | Not established by the rulings and not claimed. Thai validation remains `0 of 78` |
| **That anything conforming to the shape exists** | **No.** No implementation exists |
| **That the standing design conforms to the shape** | **No — and one invariant does not.** `MTI-11` took the option Boss did not rule. See `03` §3 |
| **That any isolation property is proven** | **No.** `0 of 8` |
| **That any handoff is contract-compliant** | **No.** `0 of 10` |
| **That any cross-proof scenario is verified** | **No.** `0 of 22` |
| **That development may begin** | **No.** All three rulings carry an explicit non-authorization clause naming Team B, Team C, source code, database, schema freeze, merge, production, release, Final Solution `PASS`, and Development Final Gate |

---

## 7. Consolidated Carry-Forward Block

Every downstream Inventory prompt, register, design and proof package must carry the following verbatim, or cite the three ruling files directly.

```
MTI-D-01 = OPTION B — Company-owned Product Master / tenant-company scoped
           product identity. Similar products across tenants/companies are
           separate business objects unless an explicit Boss-authorized
           mapping layer links them for reporting or migration purposes.
           Duplication is NOT a defect.

MTI-D-02 = Company + Warehouse + Operation-Type. Inventory action context
           must carry tenant/company, warehouse and operation type wherever
           applicable, across UI, API, import, export, scheduler, report,
           audit trail and cross-module handoff.

MTI-D-03 = Platform-owned Core + Tenant Config Overlay. Shared SaaS pool
           keeps platform core centrally owned; tenants configure approved
           Inventory master/config records only. Private Company may be
           opened for high-specificity customers through Gate and Boss
           Ruling, and is never automatically approved.
```

---

## 8. Items Closed By These Rulings

| Category | Closed | Detail |
|---|---:|---|
| Decision blockers ruled by Boss | **3** | `MTI-D-01`, `MTI-D-02`, `MTI-D-03` |
| Upstream decisions discharged | **1** | `RISK-U01` / `U-01`, decision half only |
| Findings closed | **0** | No `R4-F-*`, `MTI-F-*` or `REV-F-*` item is closed by a ruling |
| L9 proofs achieved | **0** | Unchanged at `0 of 8` |
| Cross-proof scenarios verified | **0** | Unchanged at `0 of 22` |
| Handoffs made contract-compliant | **0** | Unchanged at `0 of 10` |
| Joint decisions made ready | **0** | Unchanged at `0 of 12` |
| Thai validations obtained | **0** | Unchanged at `0 of 78` |
| Capabilities built | **0** | `RISK-U03` / `GAP-FS-10` remains open |
| Vetoes discharged | **0** | See `11` §5 |

**A ruling settles a question. It does not build, prove, validate or verify anything, and this package records none of it as if it had.**

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
