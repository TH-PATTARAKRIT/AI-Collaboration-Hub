# P01 — FINANCIAL OWNERSHIP PROOF MATRIX

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Assessed under the scope-aware constitution.

Scopes: `PLATFORM` · `TENANT` · `COMPANY`. `MISSING REQUIRED SCOPE = DENY`.
**`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`.**

---

## 1. CLASSIFICATION

> ### `UNPROVEN — INFERRED ONLY`
>
> And, established this round, **reachable today in a database holding three unrelated
> corporate groups.**

---

## 2. THE FINDING, IN FULL

Approving a purchase order, or posting a vendor bill, whose counterparty resolves to another
company creates a document **in that other company**.

| Question | Answer |
|---|---|
| Scope of the resulting document | **COMPANY** — a legal record of the target company |
| Scope executing the operation | **COMPANY (source)** — a different company |
| How the target company is resolved | an **ancestor match on the shared contacts hierarchy**, run with elevated privilege, **first match wins**, with **no ordering specified** |
| Is a tenant boundary tested? | **No. Class A** — verified absent across all four source roots by the expert |
| Is the acting user's company set tested? | **No** |
| Who creates the document | the configured "create as" user — **which is the superuser on 44 of 44 deployed companies** |
| Is it posted automatically? | on **3** deployed companies, yes |
| Is the capability on? | a generator flag is on for **8 deployed companies, spanning all three corporate groups** |

---

## 3. THE DECLARED GUARD CANNOT EXECUTE — PROVEN

The mechanism declares an access check on the creating user. The expert proved it **can never
fire**:

- the framework forces superuser mode whenever the acting user is the superuser;
- the deployed "create as" user **is** the superuser on **44 of 44** companies.

So the one control standing between a cross-company trigger and a posted document in another
company **is inert in every deployed company**.

This is the **prove-the-executor** rule producing its most consequential result in P01: a guard
that exists, reads correctly, and cannot run.

---

## 4. REACHABILITY — SPLIT HONESTLY

The expert separated two routes and did not merge them:

| Route | Reachable today? |
|---|---|
| Via the **partner hierarchy** — a contact whose parent is another company's partner | **Not currently.** Only 44 of 22,974 partners resolve to a company, and each resolves only to itself |
| Via the **company partner directly** | **Yes, now.** All 44 company partners have **no company restriction**, and a shipped record rule makes company-less partners **selectable by every user in every company** |

> **A user in one corporate group can select another group's company partner and produce a
> vendor bill inside that company, created as the superuser.**

Classification: **FACT VERIFIED** (expert, deployed data). The tenant consequence follows from
the corporate-group structure: the databases hold **three unrelated groups** — 18, 15 and 10
companies plus one more — in **one schema**. Under the constitution, unrelated companies are
separate tenants by default, so this is a **candidate cross-tenant path**, not merely
cross-company.

---

## 5. WHERE IT IS INSTALLED

| Deployment | Intercompany modules |
|---|---|
| `D1` v19 | **installed** |
| `D2` v19 | **installed** |
| `D3` v16 | **uninstalled** |
| `D4` v19 | **installed** |

The capability is live on the v19 line and absent from the v16 one.

---

## 6. A SECOND SCOPE DEFECT

The **full reconciliation** object has **no company field and no record rule in either
generation** — zero rule hits across all four source roots — while full create, read, update and
delete are granted to the accounting-invoicing group.

Correct scope, on the evidence: **COMPANY**, stored and required, across ownership, access,
mutation and reference.

v19 additionally removed a field and an unlink override that reversed exchange-difference
entries; the partial-reconciliation path **needs re-verification**. Expert-reported, **not
re-derived**.

---

## 7. DISPOSITION

| Item | Status |
|---|---|
| Financial company ownership | **`UNPROVEN — INFERRED ONLY`** |
| Tolerance-zero | **HOLD.** Under `EC-04` a conditional outcome may not bypass it |
| The declared guard | **proven inert in every deployed company** |
| Cross-tenant reachability | **FACT VERIFIED as reachable** via the company-partner route |
| Full-reconcile scoping | **HOLD — SCOPE EVIDENCE REQUIRED**; correct scope proposed, not decided |
| Owner of the remedy | **SaaS / Platform Architecture and P11.** P01 makes no target-architecture decision |

---

## 8. WHAT P01 IS NOT SAYING

- Not that intercompany transactions are illegitimate. A genuine intercompany transaction is
  exactly this shape.
- Not that a breach has occurred. **No transaction was executed and no cross-company document
  was observed being created this way.**
- Not that the three corporate groups are separate tenants **as the platform defines tenancy** —
  that is the platform's determination. P01 records that they are unrelated groups in one
  schema, and that the constitution's default treats unrelated companies as separate tenants.
