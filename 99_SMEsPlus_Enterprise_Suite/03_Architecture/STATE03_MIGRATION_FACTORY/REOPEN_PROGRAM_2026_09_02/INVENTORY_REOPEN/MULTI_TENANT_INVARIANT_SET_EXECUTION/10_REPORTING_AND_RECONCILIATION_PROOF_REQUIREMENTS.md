# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 10 — Reporting And Reconciliation Proof Requirements

Level: `L11 — reconciliation / end-to-end proof`
Control Level: `/L9999.9999`
Status: `CONTEXT PROOF REQUIREMENTS DEFINED FOR 10 RECONCILIATION IDENTITIES AND 6 REPORTING SURFACES — 0 SCENARIOS DECLARABLE VERIFIED`

---

## 1. Standard Applied

Two Boss-approved controls govern L11 and neither is softened here: the 22-Scenario Cross-Proof Baseline (`296b495`) and the Minimum Handoff Data Contract (`d9e845e`). The convergence rule is binding: Accounting and Inventory Final Solutions **must not be independently frozen and only reconciled afterward**.

This session performs no cross-proof, convenes no joint session, and freezes nothing. It states what a reconciliation must assert about **context**, so that when a cross-proof becomes convenable there is something to test.

---

## 2. The Governing Reporting Requirement

`MTI-28`: **a report's `CTX` scope is part of its identity.**

This is stated as a requirement rather than a convenience because of a specific failure mode. A stock position, a valuation position and a movement history are all commonly compared across time, across sites and against an accountant's figures. Two reports produced over different context scopes are **different reports**, and comparing them produces a difference that looks like a stock or value discrepancy and is not one.

A report that does not state its scope cannot be reconciled at all — it can only be believed.

---

## 3. Context Proof Requirements By Reporting Surface

| Surface | Menus | Context proof requirement | Status |
|---|---|---|---|
| **Stock position** | `INV-M10`, `INV-M11` | Scoped before evaluation. Every row and every subtotal resolves to one `CTX`. The stated scope appears on the output and in the export. Display clamping must not conceal a cross-context arithmetic break (`R4-F-07` interaction, `MTA-07`) | `SPECIFIED` |
| **Movement history / stock card** | `INV-M12`, `INV-M13` | Same scoping. **The ordering rule is stated and applied consistently** (`R4-F-08`), and the context-conformance evidence states which date it was evaluated against | `SPECIFIED` |
| **Valuation position** | `INV-M14` | Same scoping. Cross-company aggregation prohibited; **no Cross-Context Report Grant may carry valuation content while the COGS Gap stands** (`AAS-V-03`) | `SPECIFIED — VALUE HELD` |
| **Warehouse analytics** | `INV-M15` | Same scoping. Every derived measure carries the `CTX` of its inputs. Analytic surfaces rarely display their own scope, which makes this the least visible leak surface | `SPECIFIED` — measure set evidence-thin (`GAP-FS-13`) |
| **Registers to Audit** | `HO-27` | Context-scoped, with the audit trail itself scoped. Statutory **format** is `TH-HOLD-01`, held | `SPECIFIED` — format held |
| **Export** | `INV-F-25` | The export carries its scope statement; the export act is evented. **Nothing in the system controls the file after it leaves** — this is a labelling and governance obligation, not a technical one (`MTA-09`) | `SPECIFIED` — residual `MATERIAL` |

---

## 4. Context Assertions For The Ten Reconciliation Identities

`RC-01` .. `RC-10` are carried unchanged from v1.0. This file adds only the context assertion each must carry, and adds one new identity.

| Identity | Subject | Context assertion added | Blocked? |
|---|---|---|---|
| `RC-01` | Conservation — on hand equals total in minus total out | Holds **within each company independently**, not only in aggregate. A group-level conservation check that balances while two companies are wrong in opposite directions is not a check | No — Inventory-owned, continuously checkable |
| `RC-02` | Movement completeness | Every movement fact resolves to exactly one company and is counted in exactly one company's reconciliation | No |
| `RC-03` | Document-to-fact agreement | Document and its facts resolve to the same `CTX`; numbering continuity holds per `(company, operation type)` | No |
| `RC-04` | Internal movement value neutrality | Extended per `R4-F-18` to an **independent** zero-value check, asserted per company | Mechanism no; **value definition held** |
| `RC-05` | Reservations never exceed on hand | Holds per company; a reservation never draws on another company's availability | No |
| `RC-06` | Traceability chain completeness | Every chain link resolves within one company, or crosses only via an `XCR-01` correlation | Partly — `XCR-01` incomplete (`JT-10`) |
| `RC-07` | Inventory-to-ledger agreement | Asserted per company against that company's ledger. A tenant-level total is a **sum of per-company agreements**, never a substitute for them | **Yes** — `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED` (`JT-01`, `JT-03`, `JT-07`) |
| `RC-08` | Cutover certification | Certified **per company**, by a named human, against that company's opening trial balance. Quantity half is separable and certifiable now (`R4-F-25`) | Quantity half no; **value half yes** |
| `RC-09` | Period boundary integrity | The lock date is per company; an exception grant carries `CTX` as well as grantor, reason and expiry | Consequence held (`JT-06`, `JT-12`) |
| `RC-10` | Evidence reachability | Every reconciliation run's evidence is retained, context-scoped and inspectable (`MTI-50`) | No |
| **`RC-11`** | **Context conservation across handoffs** — **new** | Every fact emitted in a context is received in that context, and the emitted and received populations agree per company | Mechanism no; **the value comparison is held** |

### 4.1 `RC-11` is the new reconciliation identity this session adds

`MTI-46` requires it and no prior round states it. Its purpose is narrow and important: **every other reconciliation checks Inventory against itself or against the ledger. None checks that the boundary survived the handoff.**

A fact can be emitted correctly in company A and consumed into company B by a consumer that inferred, defaulted or reconstructed the company — exactly what `MTI-45` prohibits. Without `RC-11`, that failure is invisible on both sides: Inventory's own reconciliation balances, and Accounting's does too, because each is internally consistent.

Recorded as a new finding: `MTI-F-06`. Owner: Inventory and Accounting jointly. The **count** comparison is specifiable now; the **value** comparison carries `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`.

---

## 5. End-To-End Proof Requirements

For a context isolation claim to be end-to-end rather than surface-level, three assertions must hold together. Stating them separately is what prevents a partial result being read as a whole one.

| # | Assertion | Evidence required | Available now? |
|---:|---|---|---|
| 1 | **Stored** — every record resolves to exactly one `CTX`, consistent with its anchor | `MTI-19` conformance control runs, per object type, with results | No — requires an implementation |
| 2 | **Derived** — no computed value aggregates across a boundary | `EP-A` exercised on all six reporting surfaces; `MTP-20` .. `MTP-26` | No — requires an implementation |
| 3 | **Transferred** — every emitted fact is received in the context it was emitted in | `RC-11`; `HF-CTX-06` attestations matched on both sides | No — requires both domains and the joint interface artifact, which **does not exist** |

**All three are specified. None is available.** Assertion 3 additionally requires the joint interface artifact that the Boss controls mandate before integrated final freeze; it does not exist, R4 correctly declined to author it as a single-domain session, the review likewise, and **this session likewise does not author it**.

---

## 6. The 22 Scenarios — Reporting And Reconciliation View

Carried from `07` §5 and not restated in full. The reporting-specific position:

| Scenario | Reporting / reconciliation position after this design |
|---|---|
| **12 — Count / adjustment** | Recorded by R4 as the closest to specifiable. The context half is now specified; the reason taxonomy is `R4-Q-01`, Thai panel |
| **14 — Internal transfer, no inappropriate financial effect** | `RC-04` extended to an independent per-company zero-value check. **Mechanism specifiable; value definition held** |
| **15 — Multi-company / tenant boundary** | The scenario this package serves. Testable once implemented; **not verified** |
| **19 — Period-end / cut-off** | `RC-09` gains a context requirement on the exception grant. Consequence remains held |
| **20, 21 — Migration across fiscal years; mapping and deterministic reconciliation** | Unchanged. Deterministic reconciliation requires the provenance reference, rank 3 |
| **All 22** | **0 declarable verified. Unchanged.** |

---

## 7. Coverage Result

| Measure | Result |
|---|---:|
| Reporting surfaces given context proof requirements | **6 of 6** |
| Reconciliation identities given a context assertion | **10 of 10 carried, plus 1 new** |
| Identities unblocked at the context level | 7 — `RC-01`, `-02`, `-03`, `-05`, `-06` (partly), `-10`, and the quantity half of `RC-08` |
| Identities held under the COGS Gap | 4 — `RC-04` (value), `RC-07`, `RC-08` (value), `RC-09` (consequence) |
| End-to-end assertions specified | 3 |
| End-to-end assertions **available now** | **0** |
| New findings | 1 — `MTI-F-06` |
| Scenarios declarable verified | **0 — unchanged** |
| Items closed | **0** |

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
