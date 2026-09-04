# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 06 — Cross-Module Handoff Contract Fields And Ownership

Control Level: `/L9999.9999`
Status: `ELEMENT 10 SPECIFIED AS A GUARANTEE — ELEMENTS 14 AND 15 REMAIN UNSUPPLIABLE — ELEMENTS 4 AND 7 REMAIN HELD — 0 HANDOFFS CONTRACT-COMPLIANT`

---

## 1. The Control This File Answers To

The Boss-approved Minimum Handoff Data Contract (`d9e845e`, `BOSS APPROVED / EFFECTIVE`) requires sixteen elements per material handoff. Element 10 reads:

> `WHICH Company / Tenant` — **mandatory** company and tenant context.

The 22-Scenario Cross-Proof Baseline (`296b495`) requires the same at §3 as *"tenant / company context"*, likewise without qualifier. Contract §4 forbids declaring a scenario verified where it is *"missing company/tenant isolation context"*.

The ownership boundary is not reopened by this file:

`Inventory Core = Stock Truth Owner.` `Accounting Core = Financial Truth Owner.`
**Inventory emits facts. Accounting decides postings.**

---

## 2. What Was Actually Missing

R4's formulation is exact and is the design brief for this file:

> Company and tenant context **can be carried but not guaranteed**. Handoff element 10 unsuppliable **as a guarantee**. — `09` §3

Carriage was never absent. A payload can always print a company. What contract §3 and §4 require is that the value be **known, traceable and evidence-backed**, and §4 disqualifies an element that is *"unsupported by evidence"* or *"dependent on an unapproved assumption"*.

Therefore the contract field set below specifies **the value and the evidence of the value**, not the value alone.

---

## 3. The Context Field Group — `HF-CTX-01` .. `HF-CTX-09`

These fields together constitute element 10 and support elements 8, 9, 11, 12, 13 and 16.

| Field | Content | Mandatory | Owner | Governing Invariant |
|---|---|---|---|---|
| `HF-CTX-01` | Tenant identity | **Always** | SaaS Foundation | `MTI-01`, `MTI-02` |
| `HF-CTX-02` | Company identity | **Always** | Inventory | `MTI-01`, `MTI-04` |
| `HF-CTX-03` | Warehouse identity | Where the fact is situated | Inventory | `MTI-07` |
| `HF-CTX-04` | Location identity — source and destination, each resolved | Where the fact moves goods | Inventory | `MTI-08`, `MTI-15` |
| `HF-CTX-05` | **Context anchor path** — the object chain from which company was derived, e.g. movement fact → document → operation type → warehouse → company | **Always** | Inventory | `MTI-05` |
| `HF-CTX-06` | **Conformance attestation** — the identifier of the control run that last asserted `MTI-19` over this record's object type, with its timestamp and result | **Always** | Inventory + SaaS Foundation | `MTI-19`, `MTI-43`, `MTI-50` |
| `HF-CTX-07` | **Cross-context relationship identity** — the `MTI-22` register entry and correlation identity, where the fact is one side of a cross-company pair | Where applicable; `N/A` **with reason** otherwise | Inventory + Boss | `MTI-22`, `MTI-44` |
| `HF-CTX-08` | **Authority reference** — the actor and the authority under which the act occurred, including any `MTI-18` grant relied on | **Always** | SaaS Foundation | `MTI-18`, `MTI-30`, `MTI-38` |
| `HF-CTX-09` | **Owner dimension** — whose the goods are, stated separately from company | Where an owner other than the company applies; `N/A` with reason otherwise | Inventory | `MTI-16` |

### 3.1 `HF-CTX-05` and `HF-CTX-06` are the fields that change element 10's status

Without them the payload asserts a company. With them it states **how the company was determined** and **when that determination was last independently checked**. That is the difference between carriage and guarantee, and it is the difference contract §4 turns on.

`HF-CTX-06` is deliberately a reference to a control run rather than a boolean. A boolean is an assertion by the emitter about itself; a control-run reference is inspectable by the consumer and by an auditor, and satisfies element 16 (`WHAT Evidence proves it`) for the context portion of the fact.

Recorded as a new finding: `MTI-F-04`, first stated at `03` §10.1.

### 3.2 `HF-CTX-09` exists because location and ownership are independent

`L5-07` records that *where* goods are and *whose* they are are two orthogonal questions, and that the v1.0 concept model already carries an owner dimension. If ownership is not carried as its own field, a consumer must infer it from company — and consignment stock, or goods held at a customer site on approval, will be inferred wrongly in one direction or the other.

**What may be valued as whose asset is not decided here.** `GAP-MD-09` is open and the valuation consequence carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`. The field is specified; the policy is not.

---

## 4. Element-By-Element Position After This Design

For the ten material Inventory-to-Accounting handoffs at `16` §3.

| # | Element | Position Before | Position After This Design | Suppliable? |
|---:|---|---|---|---|
| 1 | `WHAT happened` | Suppliable | Unchanged | Yes |
| 2 | `WHO owns the fact` | Suppliable | Unchanged; `HF-CTX-08` strengthens it | Yes |
| 3 | `WHEN physical event occurred` | Suppliable | Unchanged; carried as two distinct dates (`MTI-38`) | Yes |
| 4 | `WHEN financial recognition occurs` | Not suppliable | **Unchanged** | No — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| 5 | `HOW MUCH quantity` | Suppliable | Unchanged | Yes |
| 6 | `WHICH UOM` | Suppliable | Unchanged | Yes |
| 7 | `WHAT valuation / cost basis` | Not suppliable | **Unchanged** | No — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` |
| 8 | `WHICH Product / Lot / Serial` | Suppliable but not unique | **Strengthened.** Identity is the resolved tuple, never the bare value (`MTI-12`) | Yes, subject to implementation |
| 9 | `WHICH Warehouse / Location` | Suppliable but company-optional | **Strengthened.** `HF-CTX-03`, `HF-CTX-04`; location company is mandatory and derived (`MTI-08`) | Yes, subject to implementation |
| **10** | **`WHICH Company / Tenant`** | **Not suppliable as a guarantee** | **Specified.** `HF-CTX-01`, `-02`, `-05`, `-06` supply the value, the derivation and the evidence | **Specified, not built, not verified** — see §4.1 |
| 11 | `WHICH Source Document` | Suppliable | Unchanged | Yes |
| 12 | `WHICH Original Event` | Suppliable in principle | Strengthened by `MTI-38`, `MTI-39`; **weakened in practice** by the absence of the attempt identity | Partial — rank 2 dependent |
| 13 | `WHICH Reversal / Correction` | Suppliable in principle | Strengthened by `MTI-39`, `MTI-40`; corrections may not change context | Partial — rank 2 dependent |
| 14 | `WHICH Migration / Replay Batch` | Not suppliable | **Unchanged.** `MTI-42` requires explicit context assignment but the provenance reference itself does not exist | No — `GAP-FS-08`, rank 3 |
| 15 | `WHICH Idempotency Identity` | Not suppliable | **Unchanged.** `MTI-31` supplies run scoping, not identity | No — `RISK-C02`, rank 2 |
| 16 | `WHAT Evidence proves it` | Partial | Strengthened for the context portion by `HF-CTX-06` and `MTI-50` | Partial |

### 4.1 The honest statement about element 10

**Element 10 moves from *unsuppliable in principle* to *specified, not built, not verified*.**

That is a genuine change of state and a small change in effect. It does not make any handoff contract-compliant, because:

- elements 4 and 7 remain held under the Accounting COGS Gap on eight of the ten material handoffs;
- element 15 remains absent on all ten;
- element 14 remains absent on the handoffs where it is contractually applicable — which, per the review's refinement `REV-F-02`, is the migration, replay and recovery handoffs, not all ten;
- and a specification is not an implementation. Contract §3 requires elements to be *known, traceable and evidence-backed*. A design document makes element 10 **definable**; only a built and checked system makes it **evidence-backed**.

**Zero of the ten material Inventory-to-Accounting handoffs is contract-compliant. That result is unchanged by this session.** See `12` `AAS-V-01`.

---

## 5. The Cross-Context Relationship Register — Instantiated

`MTI-22` requires a closed, enumerated register of every legitimate cross-company path. This is its initial content. It is deliberately short, and every entry that cannot be completed says so.

| ID | Relationship | Direction | Permitted Effect | Evidence Obligation | Status |
|---|---|---|---|---|---|
| `XCR-01` | **Inter-company transfer** (`HO-22`) | A → B, paired | Two single-context facts, one per company, correlated by a shared relationship identity. Never one fact | Both facts carry `HF-CTX-07` naming this entry and the correlation identity | **INCOMPLETE — `JT-10` open; path never traced end to end (`GAP-FS-07`)** |
| `XCR-02` | **Cross-Context Report Grant** (`MTI-25`) | Read only, within one tenant | Aggregate read across an enumerated company set. **No write. No valuation content while the COGS Gap stands** | Grant identity, granting authority, scope, expiry, and a log entry per use | `SPECIFIED — CONDITIONAL (`MTI-D-04`)` |
| `XCR-03` | **Tenant-level definitional master reference** (`MTI-11`) | Read only, within one tenant | A company-scoped record may reference tenant-level definitional data. Carries no quantity, value, policy attachment or history | The reference resolves to a versioned definitional record | `SPECIFIED — CONDITIONAL (`MTI-D-01`)` |
| `XCR-04` | **Platform template instantiation** (`MTI-35`) | Platform → tenant, at provisioning only | Copy, recording the template version. Never a live link; a later template change never propagates | The instantiated record names the template version copied | `SPECIFIED — CONDITIONAL (`MTI-D-03`)` |

**Four entries. One incomplete, three conditional, none unconditionally settled.** That is the register's true state and it is stated rather than padded. A register with more entries than the evidence supports would be worse than a short one, because the isolation claim is a claim about this list being complete.

---

## 6. Field Obligations Of Each Consuming Module

`MTI-45` requires every consumer to receive `CTX` as a mandatory, non-inferable input. What each consumer must do with it differs.

| Consuming Module | Fields Required | Obligation On The Consumer | Lineage |
|---|---|---|---|
| **Accounting** | `HF-CTX-01`, `-02`, `-05`, `-06`, `-07`, `-08`, `-09` | Post within the company the fact resolves to and no other. May not infer, default or reconstruct company. Must reject a fact whose attestation is absent or failing | `HO-07`, `-09`, `-10`, `-11`, `-12`, `-14`, `-17`, `-20`, `-22`, `-24` |
| **Purchase** | `HF-CTX-01` .. `-04`, `-08` | A proposal or expected receipt is actioned only in its own company. Over-receipt tolerance and approver are per company | `HO-04`, `-05`, `-06` |
| **Sale** | `HF-CTX-01` .. `-04`, `-08`, `-09` | Availability promised is availability in the customer's company. The owner dimension must not be read as availability | `HO-01`, `-02` |
| **Manufacturing** | `HF-CTX-01` .. `-04`, `-08` | Component demand and output resolve to one company; batch genealogy links identities within one company or via `XCR-01` | `HO-18`, `-19`, `-20` — conditional on `GAP-FS-19` scope ruling |
| **Approval** | `HF-CTX-01`, `-02`, `-08` | **An approver must hold authority in the record's own `CTX`.** Approval routing may not cross a company boundary. Segregation of duties composes with, and never overrides, the context boundary | `L7-03`, `L7-04`, `L7-09` — granularity conditional on `U-01` |
| **Document** | `HF-CTX-01`, `-02`, `-08`, `-11` | An attached document inherits the `CTX` of the fact it evidences and is visible only within it. **PDPA scope is `GAP-MD-29`, zero coverage — `MTI-D-05`** | `INV-F-04`, `-07`, `-12`, `-14`, `-19`, `-41` |
| **Reporting** | `HF-CTX-01` .. `-04`, plus the report's own scope statement | Scope before evaluation, never filter after. State the `CTX` scope as part of the report identity. No cross-company aggregation except under `XCR-02` | `HO-26`, `-27`; `INV-M10` .. `INV-M15` |

### 6.1 The Approval obligation is the one most likely to be got wrong

Segregation of duties requires that the approver be a different person from the actor. The context boundary requires that the approver be inside the same company. In a Thai SME with two office staff, those two requirements can conflict directly: the only other person with authority may be in another company of the same group.

The rule stated here is that **the context boundary wins**, and the segregation requirement must degrade to a compensating control rather than be satisfied by crossing a company. `R4-F-21` already records that a segregation model which cannot degrade will simply be bypassed. The compensating-control design needs Thai user input (Lane C) and is not authored here.

Recorded as a new finding: `MTI-F-05`.

---

## 7. Coverage Result

| Measure | Result |
|---|---:|
| Contract elements addressed | 16 of 16 |
| Elements whose status **improves** | 3 — elements 8, 9, 10 |
| Elements **specified as a guarantee for the first time** | 1 — element 10 |
| Elements still unsuppliable | 2 — 14, 15 (ranks 3 and 2, not in this authorization) |
| Elements still held under the COGS Gap | 2 — 4, 7 |
| Context field group defined | 9 fields, `HF-CTX-01` .. `HF-CTX-09` |
| Consuming modules given field obligations | 7 of 7 |
| Cross-context relationship register entries | 4 — 1 incomplete, 3 conditional |
| **Material handoffs contract-compliant** | **0 — unchanged** |
| New findings | 1 — `MTI-F-05` |

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
