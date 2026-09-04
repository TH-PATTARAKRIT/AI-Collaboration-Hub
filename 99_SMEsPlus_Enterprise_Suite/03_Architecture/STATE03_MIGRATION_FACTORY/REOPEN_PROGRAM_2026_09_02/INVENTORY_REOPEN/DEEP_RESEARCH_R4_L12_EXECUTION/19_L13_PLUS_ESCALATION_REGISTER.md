# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 19 — L13+ Escalation Register

Control Level: `/L9999.9999`
Status: `4 CONDITIONAL LEVELS OPENED — 6 ESCALATED ITEMS — DEEP RESEARCH ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Escalation Rule Applied

The Boss standard permits opening `L13+` without an interim Boss click, provided every added level records: reason for escalation, evidence lineage, risk or gap ID, checkpoint reference, owner, and next gate or required Boss decision.

R4 opened four conditional levels. Each entry below carries all six required fields.

An item was escalated only where L1-L12 genuinely could not contain it — not merely because it was difficult or unresolved. Most unresolved items in this package stay at L12 and are carried in `20_RISK_GAP_DECISION_REGISTER.md`.

---

## 2. `L13` — Cost Timing Forensic

Trigger condition met: cost is affected by receipt, delivery, invoice, landed cost or return sequence.

### `L13-01` — Retroactive cost compensation is sequenced by record creation order, not by effective date

| Field | Content |
|---|---|
| Reason for escalation | L6 established that a cost layer timing gap exists (`L6-13`). It could not establish *how the gap is closed*, and the closing mechanism turns out to carry its own defect. That is a level deeper than edge-case identification. |
| Evidence lineage | Layer 2 primary-source inspection, 2026-09-04, target-generation reference ERP. Citation held in audit quarantine under Clean Room Learning Directive v2.0; withheld from this Layer 1 document. Corroborated by the COGS evidence chain's records on interim accounts and value timing. |
| Finding | Goods issued before receipt are valued at an estimate and marked with a negative remaining quantity. A later compensation pass matches those estimated issues against real receipts and books the difference. **The matching is ordered by the technical creation sequence of the records, not by their effective business dates.** A back-dated receipt entered after an estimated issue therefore compensates as though it had occurred later. |
| Consequence | Cost can be attributed to the wrong period. Since back-dated entry is routine in a Thai SME (`18` §5 assertion 1), this is an ordinary-operation defect, not an edge case. It also means a value adjustment can land after the period it economically belongs to has closed, which intersects `L16`. |
| Risk / gap ID | `R4-F-20` |
| Checkpoint | `CP3` |
| Owner | Joint Accounting × Inventory |
| Next gate / Boss decision | Joint 22-Scenario Cross-Proof, scenarios 5, 6, 19. Requires `JT-03` and `JT-06`. **`DEPENDENCY: ACCOUNTING COGS GAP`.** |

### `L13-02` — Scrap salvage has no reference pattern and must be originated

| Field | Content |
|---|---|
| Reason for escalation | L6 asks what happens in the edge case. Here the answer is that the concept does not exist at all, which converts an edge-case question into an origination requirement — a different kind of work needing its own record. |
| Evidence lineage | Layer 2 primary-source inspection, 2026-09-04. The scrap concept carries no salvage-value field and no salvage-recovery mechanism; its lifecycle is two states. Citation held in audit quarantine. |
| Finding | The Boss-mandated edge case "scrap with salvage value" cannot be answered by transfer from the benchmark. Open design questions it raises: do salvaged goods re-enter stock as a different item, or leave stock and generate only a financial recovery; is salvage a property of the scrap event or a separate later event; how is the link to the original write-off preserved. |
| Consequence | A Thai SME selling salvage either records it nowhere or records it as an unrelated sale, breaking the link to the write-off it came from. |
| Risk / gap ID | `R4-F-03`; function `INV-F-13` |
| Checkpoint | `CP2` |
| Owner | Inventory, with an Accounting dependency for the value treatment |
| Next gate / Boss decision | Boss scope decision on whether salvage is in v2.0 scope. Value treatment is `DEPENDENCY: ACCOUNTING COGS GAP`. |

---

## 3. `L14` — Traceability Proof

Trigger condition met: batch and serial traceability cannot be proven from L1-L12 alone.

### `L14-01` — Traceable identity uniqueness is not provable at L1-L12

| Field | Content |
|---|---|
| Reason for escalation | L8 defines the canonical identity and L9 asks whether isolation holds. Neither can prove that a traceability *chain* is unbroken, because a chain is a property of a sequence of facts, not of any single record. Proving it requires a dedicated level. |
| Evidence lineage | Layer 2 primary-source inspection, 2026-09-04: uniqueness scoped to (identifier, product, company), with company-less identities possible and a reactive cross-company duplicate check rather than prevention. Citation held in audit quarantine. Prior evidence lineage `GAP-MD-11`, `IV-04`, `INV-04`. |
| Finding | A reactive duplicate check is a report, not a guarantee. Combined with the ability to amend or merge batch identities (`INV-F-20`), which rewrites history, and with migration importing legacy identities in bulk (`R4-F-23`), the chain has three independent break paths and none is currently closed. |
| Consequence | Recall capability is the business purpose of traceability. In regulated Thai sectors — food, cosmetic, pharmaceutical — a broken chain is a compliance exposure. The sector obligations themselves are `TH-HOLD-08`, held. |
| Risk / gap ID | `R4-F-06`, `R4-F-23`; `GAP-MD-11` |
| Checkpoint | `CP3` |
| Owner | Inventory + SaaS Foundation |
| Next gate / Boss decision | Requires the multi-tenant invariant set (`RISK-U03`) as a precondition. **Lane A — not COGS-gated.** |

---

## 4. `L15` — Scheduler / Automation Race Condition

Trigger condition met: replenishment and the scheduler can duplicate or conflict with manual actions.

### `L15-01` — Automated supply can duplicate through three independent paths

| Field | Content |
|---|---|
| Reason for escalation | L6 identified scheduler duplication (`L6-10`) and rule conflict (`L6-11`) as two separate edge cases. Forensic work shows they are two of three expressions of one missing capability, and the third is contractual rather than operational. That synthesis does not fit inside an edge-case register. |
| Evidence lineage | Layer 2 primary-source inspection, 2026-09-04: no run-level mutual exclusion exists; rule uniqueness is enforced only on (product, location, company) while the shortfall computation walks the location hierarchy. Citations held in audit quarantine. Contract path from the Boss-approved Minimum Handoff Data Contract, element 15. |
| The three paths | **(a)** Two runs overlap, or a manual run overlaps a scheduled one — nothing prevents it. **(b)** Overlapping rules at a parent and a child location each raise supply for the same shortfall — the uniqueness constraint prevents only the exact-match case, which is the case a user is least likely to create by accident. **(c)** A retried operation cannot be distinguished from a second genuine operation, because no idempotency identity exists. |
| Consequence | Duplicate purchasing is a direct cash cost to a Thai SME and destroys trust in automation faster than any other failure. Path (c) additionally makes Boss-approved cross-proof scenario 22 — retry, idempotency, replay — unprovable. |
| Risk / gap ID | `R4-F-11`, `R4-F-16`; `GAP-MD-21`, `RISK-C02` |
| Checkpoint | `CP3` |
| Owner | **Boss** for the `C-02` severity ruling; Inventory for paths (a) and (b) |
| Next gate / Boss decision | **Boss decision on `C-02`.** R4 supplies new contract-based evidence at `07` §5 and explicitly declines the decision itself. **Lane A — not COGS-gated.** |

### `L15-02` — Reservation concurrency remains an unarbitrated conflict with an unfollowed lead

| Field | Content |
|---|---|
| Reason for escalation | This is a live disagreement between two prior challenge passes that was reconciled to a hold rather than settled, with a specific named verification never performed. It is a race-condition question and belongs with `L15-01`. |
| Evidence lineage | `C-04` / `N-CONC-01`. One pass classified it a blocking unknown with an unfollowed lead; another classified it partially verified and not blocking. Reconciled to `HOLD`. Layer 2 inspection this session confirms reservation is held as a quantity on the balance record rather than as an independent fact. |
| Consequence | Two concurrent operations may both believe they reserved the same goods. An adjustment may silently reduce a reservation and break a customer promise. |
| Risk / gap ID | `C-04`, `RISK-C04` lineage |
| Checkpoint | `CP5` — raised by AAS+ Track 07 as a criticism of this session |
| Owner | Team A / Track 07 |
| Next gate / Boss decision | One bounded verification pass. **R4 acknowledges it did not perform it despite having primary-source access — see `20` `R4-D-05`.** |

---

## 5. `L16` — Close / Reopen Governance

Trigger condition met: period close and late inventory changes conflict.

### `L16-01` — Late-period cost attribution has no reference mechanism at all

| Field | Content |
|---|---|
| Reason for escalation | L6 (`L6-15`) resolves the *guard* question by adopting the fixed v1.0 design position. It cannot resolve what happens to a cost that arrives late, because there is nothing to research — the mechanism does not exist in the benchmark. |
| Evidence lineage | COGS evidence chain: the reference ERP has **no documented prior-period attribution mechanism at all** for a late supplier bill, and `JT-06` is consequently largely original design work. The close model itself changed shape across reference versions and must not be silently merged. Reinforced by `L13-01`, which shows retroactive compensation can itself land after the relevant period has closed. |
| Consequence | A Thai importer's duty invoice arriving in a later period is the normal case (`18` §5 assertion 6). If the system has no attribution mechanism, either the period reopens — which accountants resist — or the cost lands in the wrong period — which auditors resist. |
| Risk / gap ID | `JT-06`, `RISK-N-A12-01`, `RISK-G1G2G3` |
| Checkpoint | `CP4` |
| Owner | Joint Accounting × Inventory |
| Next gate / Boss decision | Joint 22-Scenario Cross-Proof, scenarios 5, 6, 19. **`DEPENDENCY: ACCOUNTING COGS GAP`.** The v1.0 guard design — native guard at entry and validation, exception recorded with grantor, reason and expiry, global unaudited bypass **rejected** — is fixed and is not re-litigated by R4. |

---

## 6. Escalation Roll-Up

| Level | Items | Lane | Owner |
|---|---:|---|---|
| `L13` Cost Timing Forensic | 2 | `L13-01` C (COGS-gated); `L13-02` A for scope, C for value | Joint; Inventory |
| `L14` Traceability Proof | 1 | A — not COGS-gated | Inventory + SaaS Foundation |
| `L15` Scheduler / Automation Race | 2 | A — not COGS-gated | **Boss** (`C-02`); Team A |
| `L16` Close / Reopen Governance | 1 | C — COGS-gated | Joint |
| **Total** | **6** | **4 of 6 are Lane A** | |

Four of the six escalated items are **not** blocked by the Accounting COGS Gap. That distribution mirrors the finding at `05` §4 and `12` §2, and it is the reason `R4-F-16` is the lead recommendation rather than the COGS dependency itself.

No escalated item is closed by this session.

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
