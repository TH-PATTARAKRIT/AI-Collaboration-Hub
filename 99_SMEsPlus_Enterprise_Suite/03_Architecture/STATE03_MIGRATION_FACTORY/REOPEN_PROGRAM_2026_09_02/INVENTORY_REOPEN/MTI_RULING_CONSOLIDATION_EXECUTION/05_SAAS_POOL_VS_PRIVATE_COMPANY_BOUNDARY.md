# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 05 — SaaS Pool Versus Private Company Boundary

Control Level: `/L9999.9999`
Status: `POOL LANE SUBSTANTIALLY SPECIFIED — PRIVATE COMPANY LANE UNSPECIFIED — BLOCKED BY PRIVATE COMPANY CLASSIFICATION`

---

## 1. The Two-Lane Model

`MTI-D-03` and AAS+ advice `29` §4 together establish a two-lane operating model. The authorization at §9.5 requires the two lanes to be separated, and they are separated here.

| Lane | Purpose | Boundary | Specification State |
|---|---|---|---|
| **SaaS Pool** | Standard shared SaaS operation | Platform-owned core + tenant/company configuration overlay | **Substantially specified.** Eleven record classes named, six prohibitions named, one open end |
| **Private Company** | High-specificity customer operation | Explicitly opened by governance when the shared pool is not enough | **Unspecified.** Named as an option; no criteria, no invariants, no proofs, no gate definition |

**The asymmetry is the finding of this file.** One lane has a ruling with content. The other has a ruling that it exists.

---

## 2. Lane 1 — The SaaS Pool Boundary

### 2.1 What a tenant/company MAY configure — from `MTI-D-03` §3

| # | Record Class | Governing Invariant | Note |
|---:|---|---|---|
| 1 | Warehouse | `MTI-07` | Company-anchored; company immutable after first completed movement. **Never equated with a Thai tax branch** (`TH-HOLD-06`) |
| 2 | Location | `MTI-08` | Anchored to warehouse; company derived and mandatory. Location *kind* carries financial meaning and is versioned |
| 3 | Route | `MTI-10` | Company-anchored; route-to-rule company consistency is an invariant |
| 4 | Rule | `MTI-10` | May not belong to a company other than its route's |
| 5 | Operation Type | `MTI-09` | Anchored to warehouse, therefore company. **Now also an authorization axis** under `D-02` |
| 6 | Putaway Rule | `MTI-14` family | Must act only within its own `CTX` |
| 7 | Reordering Rule | `MTI-14` | Cross-company half closed by `MTI-14`; **within-company overlap remains open** (`R4-F-11`) |
| 8 | Storage Category | `MTI-05` anchor declaration | |
| 9 | Product Category | `MTI-11` category facet | **`RC-F-08`** — owns reporting, put-away **and costing** in one concept; the costing facet is `GAP-FS-02`, precondition-blocked on `JT-01` (**NOT DECIDABLE**) |
| 10 | Unit of Measure Category | `MTI-05` | `R4-F-13` — upward conversion rounding inflates quantity monotonically. Configurability **widens** that surface |
| 11 | Barcode Nomenclature | `MTI-26`, `MTI-27` | `R4-F-12` — a misparsed structured barcode yields a plausible but wrong quantity. Configurability **widens** that surface |
| 12 | **"Other approved Inventory configuration/master records"** | — | **Open-ended. `RC-F-06`** |

### 2.2 What the shared pool must NEVER allow — from `MTI-D-03` §3

Six prohibitions, and they are absolute within the pool.

| # | Prohibited Fork | Why It Is Absolute |
|---:|---|---|
| 1 | **Platform source code** | A forked core is not a pool |
| 2 | **Database schema** | Layers 1 and 2 of the control model require `STORE` enforcement; a per-tenant schema divergence makes a single structural guarantee impossible |
| 3 | **Posting engine behaviour** | The posting boundary is where Inventory hands off to Accounting; a per-tenant posting fork makes handoff element 16 unevidenceable |
| 4 | **Authorization engine behaviour** | `D-03` rule 4 — configuration may not weaken `D-02` |
| 5 | **Immutable event logic** | `MTI-38` .. `MTI-42`; an event log that varies per tenant cannot support replay determinism |
| 6 | **Cross-tenant isolation rules** | The boundary itself |

### 2.3 The five conditions on pool configuration — from `MTI-D-03` rule 5

Configuration in the pool must be **configuration-led**, **evidence-backed**, **reversible where applicable**, **auditable**, and must not weaken `D-01` or `D-02`.

**"Reversible where applicable" carries a boundary that must be stated.** `MTI-36` requires configuration to be versioned with effective dates and **never regenerated in place**, and `MTI-07` makes a warehouse's company immutable after the first completed movement. Reversibility therefore means *a new version supersedes an old one*, never *a past act is re-interpreted*. A downstream design that implements reversibility as in-place mutation would satisfy the word and violate `MTI-36`, `MTI-06` and `MTI-42` simultaneously.

### 2.4 What `MTI-D-03` did not resolve

`GAP-MD-14` / `SAAS-04` has three components. The ruling addresses one.

| Component | State |
|---|---|
| **Boundary** — what a tenant may change | **Substantially supplied** by `D-03` §3, subject to `RC-F-06` |
| **Regeneration** — reconfiguring a warehouse re-derives its operation types, locations and routes | **Unchanged.** `MTI-35` and `MTI-36` specify the divergence; nothing verifies it. This is the moment at which a derived record can be recreated **without its company**, in bulk, by an ordinary administrative action — the `R4-F-09` condition |
| **Switch-off guards and versioning** | **Unchanged.** `MTI-37` specifies; nothing verifies |

---

## 3. Lane 2 — Private Company

### 3.1 What the ruling establishes

| Established | Not Established |
|---|---|
| The option **exists** | **When** it applies |
| It **may be opened when required** | **Who** decides it applies, on what evidence |
| It **must pass controlled governance before use** | What that governance **is** |
| It requires an explicit **Gate record, evidence, and Boss ruling** | What the Gate record must **contain** |
| It is **not a bypass** for evidence, authorization, audit, tenant isolation or Boss approval | Which control rules **change**, and which are identical |
| It is **not automatically approved** | Whether an existing pool tenant can **migrate into** it, and what happens to its history if it does |

### 3.2 Why this is a material gap, not a future detail — `RC-F-07`

The invariant set's 50 invariants, 35 matrix rows, 41 function enforcement points, 8 L9 proofs and 30 proof scenarios are **written for one topology**. A Private Company is a second topology. Three specific consequences:

1. **The L9 proofs may not transfer.** `L9-01` requires that no tenant reaches another tenant's data *"under any code path"*, with the path set certified complete. If a Private Company runs a different deployment shape, its path set is a different path set, and a completeness certification over the pool's paths says nothing about it.
2. **`MTI-06` makes the context spine immutable by design.** If a customer can move from pool to Private Company, that movement is either a context change on existing records — which `MTI-06` prohibits — or a migration with provenance, which requires `GAP-FS-08`, which does not exist. **Neither path is specified.**
3. **AAS+ advice `29` §7 makes unclassifiability a `HOLD` condition.** Any requirement that cannot be classified as pool-safe or Private-Company-required must remain `HOLD` *"until classification evidence exists"*. With no criteria published, **the classification cannot currently be performed for any requirement**, which means the `HOLD` condition is live and general rather than exceptional.

Point 3 is the practical consequence and it is why `09` carries a `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` status class at all.

### 3.3 The escalation criteria that AAS+ advice implies but does not define

AAS+ advice `29` §6 gives a **directional** test: where a customer requirement needs source-level behaviour, schema-level divergence, posting-behaviour divergence or isolation-rule divergence, move it to Private Company evaluation rather than modifying the pool.

That maps cleanly onto four of the six pool prohibitions at §2.2 — prohibitions 1, 2, 3 and 6. **It says nothing about prohibitions 4 and 5**: whether a requirement needing authorization-engine divergence or immutable-event-logic divergence may be met by a Private Company, or is prohibited outright everywhere.

This session takes no position on that. It is a decision, recorded as `RC-D-03`. Stating the question is within authority; answering it is not — `D-03` rule 6 reserves Private Company separation to an explicit Gate record and Boss ruling.

---

## 4. The Boundary Decision Test — What Can Be Classified Today

Applied to the live requirement classes in the evidence chain, to establish whether the `HOLD` condition at §3.2 point 3 is theoretical or actual.

| Requirement Class | Pool-Safe? | Private Company? | Classifiable Today? |
|---|---|---|---|
| Tenant configures its own warehouses, locations, routes, rules, operation types | **Yes** — named in `D-03` §3 | No need | **Yes** |
| Tenant configures its own product categories and UoM categories | **Yes** — named | No need | **Yes, with `RC-F-08` noted** |
| Tenant needs a different **posting** treatment for a stock movement | **No** — prohibition 3 | Indicated by `29` §6 | **Blocked** — no criteria, and the posting treatment itself is `HOLD` under the COGS Gap |
| Tenant needs a different **authorization** shape from `Company + Warehouse + Operation-Type` | **No** — prohibition 4, `D-03` rule 4 | **Unknown** — `29` §6 does not address prohibition 4 | **No — `RC-D-03`** |
| Tenant needs a different **isolation** rule | **No** — prohibition 6 | Indicated by `29` §6 | **Blocked** — but see `RC-F-07` point 1 |
| Tenant needs a **group-level consolidated read** across its companies | **No** — `D-01` rules 5, 8 require a mapping layer; `MTI-D-04` unruled | Not a Private Company question — it is a cross-company question **within** a tenant | **No — `MTI-D-04` unruled, `RC-F-03` layer unspecified** |
| Tenant needs schema-level divergence | **No** — prohibition 2 | Indicated by `29` §6 | **Blocked** — no criteria |

**Three of seven classifiable. Four not.** The `HOLD` condition is actual, not theoretical.

---

## 5. What Must Be Specified Before The Private Company Lane Can Be Used

Not designed here. Enumerated so the next controlled action has a scope.

| # | Required Specification | Owner | Gating |
|---:|---|---|---|
| 1 | **Escalation criteria** — the objective test that moves a requirement from pool to Private Company | Boss + product scope | `RC-D-03` |
| 2 | **Gate record content** — what evidence a Private Company Gate submission must contain | PMO + Boss | Follows 1 |
| 3 | **Control-rule delta** — which of the twelve control rules at `04` §4 change, and which are identical | Inventory + AAS+ | Follows 1 |
| 4 | **Proof delta** — which of the 8 L9 proofs and 30 `MTP-*` scenarios transfer unchanged, which need a variant, which do not apply | Inventory | Follows 3 |
| 5 | **Transition semantics** — whether a pool tenant may move into a Private Company, and what happens to its immutable history if it does | Inventory + Boss | `MTI-06`, `GAP-FS-08` |
| 6 | **Disposition of prohibitions 4 and 5** — whether authorization-engine and immutable-event divergence are Private-Company-eligible or prohibited outright | Boss | `RC-D-03` |

**Six items. Zero specified. Item 5 additionally depends on `GAP-FS-08`, which does not exist.**

---

## 6. Boundary Status

| Dimension | SaaS Pool Lane | Private Company Lane |
|---|---|---|
| Ruled by Boss | **Yes** | **Yes — that it exists** |
| Boundary content specified | **Substantially** — 11 classes, 6 prohibitions | **No** |
| Enumeration complete | **No** — `RC-F-06` | **No** |
| Invariants written for it | **Yes** — all 50 | **None** |
| L9 proofs written for it | **Yes** — all 8 | **None** |
| Proof scenarios written for it | **Yes** — all 30 | **None** |
| Escalation criteria defined | — | **No** — `RC-D-03` |
| Any customer in it | **N/A** | **No** |
| Implementation authorized | **No** | **No** |

`SaaS POOL — SPECIFIED, NOT BUILT, NOT VERIFIED`
`PRIVATE COMPANY — BLOCKED BY PRIVATE COMPANY CLASSIFICATION`

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
