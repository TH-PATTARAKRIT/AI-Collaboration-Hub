# P06_DEPENDENCY_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Inbound dependencies — what P06 needs from others

| ID | Depends on | What P06 needs | Status | Blocks |
|---|---|---|---|---|
| `D-01` | **P01** | Vendor payable ownership; payment-intent authorship on the buy side | **PEER DEPENDENCY OPEN — branch not published** | `F-02`, part of `B-04` |
| `D-02` | **P08** | The period-close architecture; whether a posting constraint may alter a recognition period | **PEER DEPENDENCY OPEN — branch not published** | `B-46`, `F-06`, `F-15`, `F-17` |
| `D-03` | **P02** | Resolution of the state-independence verdict | **CONTESTED — `P06-XC-01` routed to P11** | headline (i) |
| `D-04` | **P07** | Nothing. P07 mirrors P06's statutory HOLD rather than resolving it | **SETTLED — symmetric HOLD** | — |
| `D-05` | **P11** | Reconciliation of P06's 31 event→GL rows into the unified matrix; adjudication of `P06-XC-01` | **OPEN at P11** — `P11-B-13` states it *"has not been done, and no cell has been filled from them"* | handoff completeness |
| `D-06` | **Boss** | Decision on 26 `HOLD — DESIGN DECISION REQUIRED` items | **BOSS CONTROLLED DECISION** | implementation |
| `D-07` | **Accounting-Tax track** | Thai Revenue Code / TFRS sources for WHT at payment, cheque practice, e-payment recordkeeping, retention | **HOLD — STATUTORY EVIDENCE REQUIRED** | `B-08`, `B-09`, `B-21`, `B-13` |
| `D-08` | **Target database** | `ir.module.module` export; `res_company` hierarchy + VAT; `multi_approval_type` configuration | **HOLD — DATABASE EVIDENCE REQUIRED** | `B-44`, `B-19`, `B-31`, `OQ-91` |
| `D-09` | **Odoo 18 enterprise distribution** | A known-good copy to diff `account_accountant_batch_payment` against | **HOLD — SOURCE EVIDENCE REQUIRED** | `OQ-63` |

---

## 2. Outbound dependencies — what others need from P06

| ID | Owed to | What P06 supplies | Status |
|---|---|---|---|
| `D-10` | **P07** | Payment date as the withholding anchor; allocation per document; reversal linkage; one FX policy — P07 marks all **BLOCKING** | **SUPPLIED, WITH DEFECTS DECLARED.** All three exist and all three are defective: the payment date is user-settable and changing it silently drops the withholding (P05 `TX-03`); allocation is mutated by two mutually-unaware subsystems; reversal linkage does not exist |
| `D-11` | **P10** | Answer to `X-08` — are bank-side prepayments and interest accruals P10 or P06 events | **ANSWERED — P10 may close it.** Resolves by absence: no bank-interest object exists for either process |
| `D-12` | **P11** | `P06-B-27` closure; `P06-XC-01`; net-new scope rows (bank account, provider, token); the 31 event→GL rows | **SUPPLIED** — `P06-B-27` may be struck from P11's `D-3` UAT list |
| `D-13` | **P09** | Confirmation or refutation of P09's class-B claim about P06's widget overwriting analytic values | **PARTIALLY ANSWERED** — the overwrite shape is confirmed (RM-F-01 clears and rebuilds every line); the analytic specifics are not traced. **P09's class B is correct and should stay class B** |
| `D-14` | **P05** | Confirmation that P06 owns the reimbursement payment door P05 operates | **SUPPLIED** — P11 `UBE-33` settles it to P06 |
| `D-15` | **P08** | The full period-close input set: reconciliation must be inside the close regime; RELOCATE is not an acceptable default; lock inheritance across possibly-distinct legal entities; the pre-close control is one-time only; no accounting field may be written by raw SQL | **SUPPLIED, UNCLAIMED** — no P08 exists to receive it |

---

## 3. Dependency chains that gate more than one item

**DEP-CHAIN-01 — `root_id` (now broken).**
`P06-B-27` gated attack A4a, `RM-R-10` and `SCOPE-R-02`. **Two closed on evidence; the third reclassified to a design decision.** The chain is discharged. P11 may strike `P06-B-27` from `D-3`.

**DEP-CHAIN-02 — P08's absence gates four items.**
`B-46` (RELOCATE), `F-06` (posting-state authorship), `F-15` (cash/bank GL balance), `F-17` (lock/close status). **One publication closes the chain.** This is now the highest-leverage unresolved dependency in P06, replacing `B-27`.

**DEP-CHAIN-03 — Target-database absence gates four items.**
`B-44`, `B-19`, `B-31`, `OQ-91` — plus it caps `F02`'s evidence class permanently at source-level. **One `ir.module.module` export closes most of it.**

**DEP-CHAIN-04 — The statutory track gates four items** and cannot be closed by any research session.

---

## 4. Dependencies P06 discovered it had and did not know

**DEP-F-01 — P06 depends on P04's finding about the generic posting routine.**
P06 analysed date relocation on three reconciliation paths and framed it as a reconciliation behaviour. P04 established it lives in *"the accounting core's generic posting routine"*. **P06's framing was too narrow, and it was corrected by a process P06 never expected to depend on** — asset accounting.

**DEP-F-02 — P06 depends on P05 for its own door denominator.**
The eighth settlement path (`SR-04`, cash moving with no payment object) was found by the expense process. **A denominator P06 published as complete was incomplete, and the correction came from outside.** This is the second time in this package that an independent pass corrected a P06 denominator — the first was the ingestion-door count (REV-E-01).

**DEP-F-03 — P10 addresses its close and FX dependencies to P04, not P08.**
P10 routes lock dates, fiscal calendar and currency policy to *"`P04` A2R"*, calling it "the ledger", while P11 and P02 route the same questions to P08 / Core Accounting. **Since no P08 branch exists, P10's dependencies are addressed to a process that does not own them and cannot answer.**
**P06 does not adjudicate this** — it is a peer's routing decision. It is flagged to P11 as a routing defect that will surface at reconciliation. Recorded as `P06-OQ-93`.

---

## 5. Standing limitation

Two of nine inbound dependencies are unpublished counterparties. **P06 cannot close `F-02`, `F-06`, `F-15`, `F-17` or `B-46` by any amount of further research.** They are recorded as `PEER DEPENDENCY OPEN` and, per the constitution, they block those conclusions and nothing else.
