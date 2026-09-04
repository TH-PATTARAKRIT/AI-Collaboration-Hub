# [SMEPLUS-26-09-04-INV-MTI-RULING-CONSOLIDATION-001]
# 08 — Tenant Config Overlay Proof Requirements

Control Level: `/L9999.9999`
Status: `POOL PROOF REQUIREMENTS SPECIFIED — PRIVATE COMPANY REQUIREMENTS NOT DEFINABLE — 0 OF 18 EXECUTABLE TODAY`

---

## 1. Scope

Mandated proof themes **7** (SaaS pool configuration boundary) and **8** (Private Company escalation criteria), plus the configuration-specific properties `MTI-D-03` rule 5 requires: configuration-led, evidence-backed, reversible where applicable, auditable.

The same proof-state vocabulary as `07` §1.1 applies, and the same governing condition from AAS+ advice `29` §7: **where a requirement cannot be classified as pool-safe or Private-Company-required, it remains `HOLD` until classification evidence exists.**

---

## 2. What AAS+ Advice `29` §5 Requires, And Where Each Is Answered

The D-03 advice names eight things downstream proof must show. This file answers all eight, and reports that two of them cannot yet be stated as propositions.

| # | AAS+ Advice `29` §5 Requirement | Requirement ID | State |
|---:|---|---|---|
| 1 | Which Inventory records are platform-owned | `RC-P-35` | `DEFINABLE — CONDITIONAL` |
| 2 | Which are tenant/company-configurable | `RC-P-36` | `DEFINABLE — CONDITIONAL` |
| 3 | Which configuration changes are allowed in the shared pool | `RC-P-37`, `RC-P-38` | `DEFINABLE — CONDITIONAL` |
| 4 | Which changes require Private Company escalation | `RC-P-45` | **`NOT DEFINABLE`** |
| 5 | How `MTI-D-01` product isolation remains intact | `RC-P-39` | `DEFINABLE` |
| 6 | How `MTI-D-02` authorization remains intact | `RC-P-40` | `DEFINABLE` |
| 7 | How cross-tenant leakage is prevented in UI, API, report, scheduler, import, export, audit trail | → `07` §3-§7 | Covered |
| 8 | How configuration changes are versioned, auditable, reversible where applicable | `RC-P-41` .. `RC-P-44` | `DEFINABLE` |

---

## 3. Theme 7 — The SaaS Pool Configuration Boundary

| ID | Proposition | Acceptance Criterion — A Rejection, Not A Demonstration | State | Blocked By |
|---|---|---|---|---|
| `RC-P-35` | The set of **platform-owned** Inventory records is enumerated, published and complete | Every Inventory record class resolves to exactly one of `platform-owned` or `tenant-configurable`; **no class is unclassified**; and an attempt by a tenant to modify a platform-owned class is **rejected at `STORE`** | **`DEFINABLE — CONDITIONAL`** | **`RC-F-06`.** `D-03` §3 ends with *"other approved Inventory configuration/master records"*. An open-ended list cannot satisfy "complete" |
| `RC-P-36` | The set of **tenant-configurable** records is enumerated, published and complete, and every instance carries a `CTX` | The eleven named classes plus whatever closes the list; every configuration record has a mandatory company anchor; a company-less configuration record is **rejected at `STORE`** | **`DEFINABLE — CONDITIONAL`** | `RC-F-06`. `MTI-34` requires tenant configuration to always carry a `CTX` |
| `RC-P-37` | **The six prohibitions hold absolutely in the pool.** No tenant configuration forks platform source code, database schema, posting engine behaviour, authorization engine behaviour, immutable event logic, or cross-tenant isolation rules | For each of the six, an attempted configuration that would produce that divergence is **rejected**, and the rejection is recorded and routed to Private Company evaluation rather than silently dropped | **`DEFINABLE — CONDITIONAL`** | Prohibitions 1, 2, 3 and 6 have a defined escalation route (`29` §6). **Prohibitions 4 and 5 do not** — `RC-D-03` |
| `RC-P-38` | Configuration is **configuration-led**: no configuration act invokes, generates or requires bespoke logic | A configuration change is expressible entirely as data within a published schema; no configuration path emits code, a migration, or a schema change | `DEFINABLE` | Implementation. `MTI-CH-01` — whether `STORE` enforcement is achievable in a chosen technology is a Team B question, not approached |
| `RC-P-39` | Configuration **never weakens `MTI-D-01`** | No configuration change makes a product visible, selectable, referenceable or reportable outside its owning company. Tested specifically on **Product Category** and **UoM Category**, which `D-03` names configurable and which touch product semantics | **`DEFINABLE`** — and **`HELD` on the costing facet** | `RC-F-08`: Product Category owns reporting, put-away **and costing** in one concept; the costing split is `GAP-FS-02`, precondition-blocked on `JT-01`, **NOT DECIDABLE**. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| `RC-P-40` | Configuration **never weakens `MTI-D-02`** | No configuration change removes, widens or bypasses a warehouse or operation-type authorization axis. Creating an operation type does not confer authority over it; **defining a configuration object and being authorized to act through it are separate grants** | `DEFINABLE` | Implementation |

### 3.1 The two configurable classes that widen an existing finding

`D-03` names as tenant-configurable two record classes that R4 already recorded as silent-failure surfaces. Configurability makes each surface larger, and the proof requirements must be written against the configured set, not a default set.

| Configurable Class | Existing Finding | Effect Of Configurability |
|---|---|---|
| **Unit of Measure Category** | `R4-F-13` — default conversion rounding is upward; repeated conversion inflates quantity monotonically and silently | Each tenant may now define its own conversion structures. The rounding behaviour must be proven **per configured category**, not once |
| **Barcode Nomenclature** | `R4-F-12` — a misparsed structured barcode yields a plausible but wrong quantity, silently | Each tenant may now define its own nomenclature. A misparse is now a **tenant-configurable** failure mode |

Neither finding is upgraded here. Both are recorded as having a larger surface than when raised, so that whoever re-scores them does so with this in hand.

---

## 4. Theme 8 — Private Company Escalation Criteria

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-45` | Every customer requirement is classifiable as **pool-safe** or **Private-Company-required**, by an objective published test | Applied to a requirement set, the test returns exactly one answer per requirement, with no residue | **`NOT DEFINABLE`** | **`RC-D-03`** — no criteria exist. `05` §4 shows the classification failing on **4 of 7** live requirement classes today |
| `RC-P-46` | A Private Company preserves every control rule the pool preserves, or names each one it changes | The control-rule delta at `05` §5 item 3 exists and is complete | **`NOT DEFINABLE`** | **`RC-F-07`** — no invariant, matrix row, proof or scenario is written for the Private Company topology |
| `RC-P-47` | Private Company separation occurs only through an explicit Gate record with evidence and a Boss ruling | No customer is in a Private Company without those three artifacts | **`DEFINABLE` as a governance control** | The Gate record's required **content** is unspecified — `05` §5 item 2. The prohibition is testable; the positive path is not |
| `RC-P-48` | A tenant's movement between pool and Private Company preserves immutable history | Either no such movement is permitted, or it is a migration with provenance and the pre-movement history is not re-interpreted | **`NOT DEFINABLE`** | `MTI-06` makes the context spine immutable by design; `GAP-FS-08` provenance does not exist. **Neither path is specified** — `05` §5 item 5 |

**Three of four Private Company requirements are `NOT DEFINABLE`.** This is the substantive content of theme 8: the authorization asks for proof of escalation criteria, and the honest answer is that the criteria do not exist, so no proof can be written against them.

`RC-P-47` is the exception and is worth stating because it is usable now: the **prohibition** half is enforceable immediately — no Private Company without a Gate record, evidence and a Boss ruling — even though the positive path is undefined.

---

## 5. Versioning, Auditability And Reversibility

`MTI-D-03` rule 5 requires pool configuration to be *"configuration-led, evidence-backed, reversible where applicable, and auditable"*. Each is a distinct proof.

| ID | Proposition | Acceptance Criterion | State | Blocked By |
|---|---|---|---|---|
| `RC-P-41` | Configuration is **versioned with effective dates and never regenerated in place** | A template version change **mutates no instantiated tenant record**; and every generated operation, movement and proposal resolves to the configuration version in force **at the time it was generated**, not the current one | `DEFINABLE` | Implementation. `MTI-35`, `MTI-36`; `IV-15` |
| `RC-P-42` | **Reconfiguration never re-derives a record without its company** | A warehouse is reconfigured; **no** operation type, location or route is recreated, and none is recreated without a company anchor | **`DEFINABLE` — and this is the highest-value configuration proof in the file** | Implementation. This is the `R4-F-09` condition produced **in bulk by an ordinary administrative action** — `SAAS-04` regeneration |
| `RC-P-43` | Every configuration change is an **auditable act** carrying actor, authority, `CTX`, both dates, and the prior and resulting versions | The audit trail answers *who changed which configuration, in which company and warehouse, under what authority, and what it was before* | `DEFINABLE` | Implementation. `MTI-38` |
| `RC-P-44` | **Reversibility is version supersession, never in-place mutation** | Reverting a configuration creates a **new version**; the superseded version remains readable; and **no completed movement, document or valuation fact changes meaning as a result** | `DEFINABLE` | Implementation. `MTI-36`, `MTI-06`, `MTI-42` |

### 5.1 Why `RC-P-44` is stated as a prohibition on the obvious implementation

*"Reversible where applicable"* is the phrase in `MTI-D-03` most likely to be implemented wrongly, because the natural reading of "revert" is "put it back". Putting it back in place would satisfy the word and violate `MTI-36` (never regenerated in place), `MTI-06` (context spine immutable), and `MTI-42` (context never inferred or re-assigned) simultaneously — and would silently re-interpret every completed movement that resolved to the superseded version.

The rule is therefore stated as: **reversion is a forward act.** A reverted configuration is a new version whose content matches an older one; it is never the older one restored.

---

## 6. What Cannot Be Proven Under The Configuration Boundary

| Item | Why |
|---|---|
| That the configurable-record enumeration is complete | `RC-F-06` — the list is open-ended |
| That any requirement is correctly classified pool-safe versus Private Company | `RC-D-03` — no criteria |
| That the Private Company topology preserves isolation | `RC-F-07` — no invariants written for it |
| That Product Category configuration is safe in its costing facet | `RC-F-08` — `GAP-FS-02` precondition-blocked on `JT-01`, **NOT DECIDABLE**. `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| That any configuration label means what a Thai user expects | `GAP-FS-11` — **`0 of 78`**. Every one of the eleven record-class names in `D-03` §3 is an unvalidated label |
| That `STORE`-level enforcement of any of it is achievable | `MTI-CH-01` — a Team B question, not approached by any session in this chain |

---

## 7. Requirement Roll-Up

| State | Count | IDs |
|---|---:|---|
| `DEFINABLE` | **7** | `RC-P-38`, `-40`, `-41`, `-42`, `-43`, `-44`, and `RC-P-47` in its prohibition half |
| `DEFINABLE — CONDITIONAL` | **4** | `RC-P-35`, `-36`, `-37`, and `RC-P-39` in its non-costing half |
| `NOT DEFINABLE` | **4** | `RC-P-45`, `-46`, `-48`, and `RC-P-47` in its positive half |
| `HELD` under the COGS Gap | **1** | `RC-P-39` costing facet |
| **Total requirements** | **14** (`RC-P-35` .. `RC-P-48`) | |
| **Combined with `07`** | **48 requirements** | |
| **Executable today** | **0** | No implementation exists |
| **Proofs produced by this session** | **0** | |

---

## 8. The `HOLD` Condition, Restated

AAS+ advice `29` §7: *"If downstream design cannot classify a requirement as SaaS Pool-safe or Private Company-required, the item must remain HOLD until classification evidence exists."*

**The classification cannot currently be performed for four of seven live requirement classes** (`05` §4). The `HOLD` is therefore live and general, and every item depending on that classification carries `BLOCKED BY PRIVATE COMPANY CLASSIFICATION` at `09`.

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
