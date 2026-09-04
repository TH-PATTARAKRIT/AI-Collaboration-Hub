# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 04 — Inventory MTI Control Model

Control Level: `/L9999.9999`
Status: `CONTROL MODEL CONSOLIDATED FROM THREE BOSS RULINGS — SPECIFIED, NOT BUILT, NOT VERIFIED`

---

## 1. What This File Is And Is Not

**Is:** the single consolidated statement of the Inventory multi-tenant control model as the three Boss rulings define it, expressed so that a downstream re-specification pass can be checked against it.

**Is not:** a new design, an amendment to the 50 invariants, a proof, or a claim that anything conforms to it. Where this model and the published invariant set disagree, **this model governs and the invariant set must be revised** — because this model is derived from Boss rulings and the invariant set predates them. See `03` §3.

---

## 2. The Two Tuples, And Why They Are Now Different Shapes

Before the rulings there was effectively one context shape. After `MTI-D-02` there are two, and the distinction is load-bearing.

| Tuple | Shape | Purpose | Source |
|---|---|---|---|
| **`CTX`** — the record context | `(tenant, company, warehouse?, location?)` | **Where a fact belongs.** Anchors every record, derived value, event and payload | Invariant set `03` §2.1 |
| **`AUTH`** — the authorization context | `(tenant, company, warehouse, operation type)` | **What an actor may do.** Governs every permission evaluation | Boss ruling `MTI-D-02` |

### 2.1 The four rules that relate them

1. **`AUTH` is always a subset of a single `CTX` spine.** Never a superset, never a union across companies. Multi-company access is several `AUTH` entries, never one broadened entry. *(Carried unchanged from `04` §7 of the invariant set; unaffected by the ruling.)*
2. **`AUTH` carries a dimension `CTX` does not** — operation type. `CTX` says where a record lives; `AUTH` says which class of act an actor may perform there.
3. **`CTX` carries a dimension `AUTH` does not** — location. Location anchors records (`MTI-08`) and is a mandatory situational axis; whether it is also an authorization axis is `RC-D-01`, unruled.
4. **Neither substitutes for the other.** A correct `CTX` on a record proves nothing about whether the actor was permitted to create it; a valid `AUTH` proves nothing about whether the resulting record was anchored correctly. **Both must be evidenced, separately.**

Rule 4 is the reason `MTI-F-04`'s attestation requirement widened. Element 10 now needs evidence of the record's context **and** of the authority the act relied on — `HF-CTX-05` / `HF-CTX-06` for the first, `HF-CTX-08` for the second.

Recorded as `RC-F-05`: the invariant set's execution family (`MTI-29` .. `MTI-33`) resolves a `CTX` and carries an authority, but **no invariant states that a deferred or background run resolves an operation-type axis**, which `MTI-D-02` rule 8 requires.

---

## 3. The Control Model — Five Layers

Stated as a stack, because each layer's guarantee is only as good as the one beneath it.

| # | Layer | Governing Ruling | What It Guarantees | Enforcement Layer Required |
|---:|---|---|---|---|
| **1** | **Tenant isolation** | `D-02` rule 6 | No tenant reaches another tenant's Inventory data by any path, including privileged, system, background, administrative and migration paths | `STORE` |
| **2** | **Company isolation** | `D-01`; `D-02` rule 1 | Within a tenant, one company's records, products, stock, value, configuration and derived surfaces do not reach another | `STORE` |
| **3** | **Warehouse authorization** | `D-02` rules 2, 5 | Within a company, an actor scoped to one warehouse cannot read or write in another | `PLATFORM` + `DOMAIN` |
| **4** | **Operation-type authorization** | `D-02` rules 3, 4 | Within a warehouse, an actor scoped to one operation type cannot perform another | `PLATFORM` + `DOMAIN` |
| **5** | **Configuration boundary** | `D-03` | A tenant may change approved configuration and master records, and nothing else. Core logic, schema, posting, authorization and isolation are never forked | `STORE` + `GOVERNANCE` |

### 3.1 Why layers 1 and 2 require `STORE` and layers 3 and 4 do not

Layers 1 and 2 are **structural**: a violating record must be impossible to create by any code path. Prior evidence records company scoping enforced at the application layer with **no database-layer backstop** and an unfinished privileged-bypass audit, which is precisely the condition `STORE` exists to remove. An invariant enforced only in application logic is an assertion, not a guarantee.

Layers 3 and 4 are **actor-relative**: they concern who may act, not what may exist. A warehouse-scoped actor and a company-scoped actor may both legitimately create the same record. The guarantee is therefore about evaluation before the act, not about the shape of the stored result — which is why it belongs at `PLATFORM` and `DOMAIN`, and why it must be **evidenced separately** per rule 4 of §2.1.

**This distinction is a consequence of the rulings, not a design choice, and it is the reason `07` and `08` specify two different kinds of proof.**

---

## 4. The Twelve Consolidated Control Rules

Every rule below traces to a ruling clause. No rule is invented here.

| # | Control Rule | Source |
|---:|---|---|
| **C-01** | Product identity is scoped by tenant/company. Similarity of code, name, barcode, UoM, category, route or description never creates shared identity | `D-01` rules 1, 2 |
| **C-02** | Duplicate products, services and configuration across tenants/companies are **legitimate** and must never be treated, reported or remediated as a defect | `D-01` §1, rules 3, 4 |
| **C-03** | Any cross-company or group-level comparison requires an **explicit controlled mapping / provenance layer**. Aggregation occurs only after an authorized mapping exists | `D-01` rules 5, 8 |
| **C-04** | Every consuming module — Sale, Purchase, Manufacturing, Accounting, Reporting, Approval, Document, Payment — consumes product identity **through** tenant/company context, never by inference | `D-01` rule 6 |
| **C-05** | Migration may and must preserve duplicate products across tenants/companies where that reflects source business reality | `D-01` rule 7 |
| **C-06** | Every Inventory action resolves tenant/company context **before execution** | `D-02` rule 1; AAS+ advice `27` §4.1 |
| **C-07** | Warehouse authorization is enforced independently. One warehouse does not imply another in the same company | `D-02` rule 2 |
| **C-08** | Operation-type authorization is enforced independently. One operation type does not imply another in the same warehouse | `D-02` rule 3 |
| **C-09** | No dimension substitutes for a wider one: operation type ⊄ warehouse ⊄ company ⊄ tenant | `D-02` rules 4, 5, 6 |
| **C-10** | Reports, valuation views, replenishment views, adjustments, transfers, scrap, landed cost flows, scheduler actions and movement history all preserve the **same** authorization context | `D-02` rule 7 |
| **C-11** | Background jobs and system automation carry **explicit** tenant/company/warehouse/operation-type context. Context is never defaulted, inherited implicitly, or inferred | `D-02` rule 8 |
| **C-12** | Tenant configuration never modifies platform source logic, schema, posting behaviour, authorization behaviour, immutable event logic or isolation rules. Where a requirement needs any of those, it is a Private Company evaluation, not a pool configuration | `D-03` §3, rules 1, 2, 5, 6; AAS+ advice `29` §6 |

---

## 5. The Enforcement Surface — Where The Model Must Hold

`D-02` rule 7 and AAS+ advice `27` §4.4 together enumerate the surfaces. This is the **complete** list the rulings require, and every one of them must carry the same `AUTH`.

| # | Surface | Ruling Basis | Note |
|---:|---|---|---|
| 1 | User interface — search, selection, confirmation | `27` §4.4 | Permission evaluated **before** search, not as a filter after |
| 2 | API execution | `D-02` rule 8; `27` §4.4 | |
| 3 | Import | `27` §4.4 | Context supplied explicitly, never inferred from file content |
| 4 | Export | `D-02` rule 7; `27` §4.4 | The `MTI-D-04` hole: an unsanctioned cross-company read is met by export |
| 5 | Scheduler and background execution | `D-02` rule 8 | `RC-F-05` — operation-type axis absent from `CTX` |
| 6 | Report generation | `D-02` rule 7 | Scope **before** evaluation; scope is part of report identity (`MTI-28`) |
| 7 | Reconciliation views | `27` §4.5 | |
| 8 | Posting handoff to Accounting | `27` §4.4 | Element 10 plus the widened attestation |
| 9 | Audit trail | `D-02` §4; `27` §5 | Must record **who / what / under which tenant, company, warehouse, operation type** |
| 10 | Valuation views | `D-02` rule 7 | **`HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** on content; context carriage is specifiable |
| 11 | Replenishment views and scheduler-driven proposals | `D-02` rule 7, §5 | |
| 12 | Movement history | `D-02` rule 7 | Ordering rule is `R4-F-08`, open |
| 13 | Landed cost flows | `D-02` rule 7, §5 | **`HOLD`** on the posting half; `JT-08` Audit VETO retained |

**Thirteen surfaces. `0 of 13` verified. No surface has been exercised against the model, because no implementation exists.**

---

## 6. What Segregation Of Duties Becomes Under This Model — `L7`

Prior evidence records segregation of duties as **undesignable** because the authorization scope was unruled (`L7-09`, `R4-F-21`). `MTI-D-02` changes that, and it is the clearest positive effect of the three rulings.

| Before `D-02` | After `D-02` |
|---|---|
| Authorization axes unknown, so "a different person" could not be constrained to a meaningful boundary | `AUTH` has four axes. A segregation rule can now be expressed as *a different actor holding a different operation type within the same company and warehouse* |
| `L7-09` recorded as not designable | **Designable.** Not designed |
| `MTI-F-05` compensating control had no axis to attach to | The axis exists. **The control content still requires Thai user input** — a Thai micro-SME with two staff may have no second actor at all (`R4-F-21`) |

**The context boundary still wins.** `MTI-D-01` and `MTI-D-02` rule 1 together mean approval routing may never cross a company boundary to satisfy a segregation requirement. Segregation degrades to a compensating control; it is never satisfied by crossing a company. That rule is unchanged and is now more firmly grounded than when `MTI-F-05` raised it.

---

## 7. What This Model Does Not Cover

Recorded because the largest risk in a consolidated control model is that a reader takes its completeness for granted.

| Gap | Why It Is Outside This Model | Register ID |
|---|---|---|
| The Private Company topology | All three rulings describe the shared pool. None states which of the twelve control rules changes inside a Private Company | `RC-F-07`, `05` §5 |
| The controlled mapping / provenance layer | `C-03` requires it; no design specifies it | `RC-F-03` |
| Whether location is an authorization axis | `D-02` names three dimensions and not location | `RC-D-01` |
| The closure of the configurable-record list | `D-03` ends the list with *"other approved…"* | `RC-F-06` |
| Whether a sanctioned cross-company read exists | `MTI-D-04`, unruled — and `C-03` depends on it | `RC-F-04` |
| Every valuation consequence of every rule above | `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` | `09` §5 |
| Whether any of it is right for a Thai SME | `0 of 78` validated. **Every term in this model is an unvalidated label** | `GAP-FS-11` |
| Whether any of it can be enforced at `STORE` in a chosen technology | `MTI-CH-01` — a Team B question, not approached | `MTI-CH-01` |

---

## 8. Model Status

| Dimension | Status |
|---|---|
| Is the model stated? | **Yes** — twelve control rules, five layers, two tuples, thirteen surfaces |
| Is it derived from Boss rulings? | **Yes** — every rule traces to a clause |
| Is it internally consistent? | **Yes** — tested at `02` §5 |
| Is it consistent with the published invariant set? | **No** — one contradiction, `RC-F-01` |
| Is it complete? | **No** — eight gaps at §7 |
| Is it built? | **No** |
| Is it verified? | **No.** `0 of 13` surfaces, `0 of 8` proofs |
| Is it validated by a Thai user? | **No** — `0 of 78` |
| Does it authorize implementation? | **No** |

`SPECIFIED, NOT BUILT, NOT VERIFIED`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
