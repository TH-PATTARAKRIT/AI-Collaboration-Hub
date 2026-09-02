# CORR-007B — N-A12-01 Clean-Room Learning Summary: Account-Led Inventory Period Close

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Branch: `audit/inventory-core-corr007b-3high-closure-010`  
Mode: Clean-room remediation / business-semantics learning / no development authorization

## 0. Clean-Room Remediation Notice

This file is the current clean-room learning version of the prior file `08`.

The previous version contained implementation-level excerpts that should not be used for Team B, Team C, or Development handoff. This rewritten version preserves the same learning structure and business conclusions, but removes source code, method bodies, field declarations, implementation paths, and vendor-specific design instructions.

This file is not a Gate PASS, not a Team B design, not a Team C design, and not development authorization. It is a sanitized learning artifact for controlled review.

## 1. Purpose

Boss challenged `N-A12-01` because fiscal-year close, monthly close, inventory cut-off, valuation, carry-forward, and GL reconciliation are not only technical behaviors. They are functional business controls that determine whether Inventory and Accounting can be trusted together.

This document records what must be learned from the prior evidence in clean-room language:

- how inventory movement should be controlled around a closed period;
- how inventory value should be known at a closing date;
- how periodic and perpetual valuation behaviors differ;
- how inventory value should reconcile to accounting;
- how opening and carry-forward should be treated;
- where SMEsPlus needs its own original functional design decision.

## 2. Clean-Room Boundary

Allowed in this document:

- business behavior;
- control objectives;
- functional risks;
- decision points;
- acceptance criteria;
- open gaps requiring Boss or Team B decision.

Not allowed in this document:

- source code excerpts;
- method bodies;
- exact field declarations;
- class names;
- file paths;
- ORM structure;
- vendor-specific implementation patterns;
- wording that says SMEsPlus must copy the reference system.

## 3. Business Workflow Learned

The period-close behavior is best understood as two related but separate control tracks:

| Track | Business Meaning | SMEsPlus Design Implication |
|---|---|---|
| Accounting close control | Accounting defines when a fiscal or hard close prevents further backdated changes. | SMEsPlus needs a clear accounting-owned lock policy. |
| Inventory valuation close | Inventory value is calculated, compared, and posted or reported for accounting use. | SMEsPlus needs an inventory-close workflow that is explicitly sequenced with Accounting. |
| Inventory movement cut-off | Stock transfers and adjustments must respect closed periods. | SMEsPlus must define whether cut-off is checked at document level, line level, or both. |
| Inventory-to-GL reconciliation | Physical stock value and accounting value must be comparable as of a date. | SMEsPlus must provide a controlled reconciliation artifact before financial statements rely on inventory. |

The key learning is that Accounting close and Inventory valuation close must not be assumed to be one automatic process. SMEsPlus should design the sequencing explicitly.

## 4. Accounting Initiation and Control

Accounting controls the business close by setting lock dates or close boundaries. Inventory must respect those boundaries when users attempt to backdate or change stock documents.

Required SMEsPlus design questions:

1. Who is allowed to close or lock a period?
2. What date types are locked: fiscal year, hard close, tax period, sales period, purchase period, or stock period?
3. Can Inventory backdate after Accounting close?
4. If an exception is allowed, who approves it and how is it audited?
5. Does Accounting close automatically trigger Inventory valuation close, or must both be performed as a controlled checklist?

## 5. Stock Movement Cut-Off

The evidence supports the business concept that stock movement after a closed period must be restricted. However, the design granularity remains open.

SMEsPlus must decide whether cut-off applies to:

| Design Option | Meaning | Risk |
|---|---|---|
| Document-level control | A whole transfer is allowed or blocked as one unit. | Simpler, but weaker for mixed-date or mixed-line transfers. |
| Line-level control | Each movement line is checked independently. | More precise, but more complex. |
| Hybrid control | Document must pass overall close rules, and each line must pass detail rules. | Strongest control, but requires careful UX and audit logic. |

Recommended clean-room direction: treat this as a SMEsPlus original control design decision, not as something inherited from any reference system.

## 6. Inventory Quantity and Value at Closing Date

The learning requirement is that SMEsPlus must be able to answer two questions as of a selected date:

1. What quantity exists physically?
2. What value does Accounting recognize for that quantity?

The system should be able to compare physical inventory value and accounting value without relying on current-date balances only.

Required acceptance criteria:

| Requirement | Acceptance Criteria |
|---|---|
| As-of-date stock position | The system can calculate quantity and value at a selected closing date. |
| Accounting-side value | The system can calculate posted accounting value as of the same date. |
| Difference analysis | The system can identify valuation difference, inventory loss, or adjustment delta. |
| Auditability | The calculation basis can be reviewed without exposing vendor implementation. |

## 7. Posting and Reconciliation Behavior

The clean-room learning is that inventory valuation can affect Accounting through two broad patterns:

| Pattern | Business Behavior | Functional Consequence |
|---|---|---|
| Per-transaction valuation | Inventory movement creates accounting impact close to the time of movement. | GL is updated continuously, but still needs reconciliation. |
| Periodic valuation | Inventory movement changes quantity first; accounting value is summarized later at close. | Month-end close is more important because GL is updated by closing process. |

SMEsPlus must decide which modes are supported, whether both modes can exist by product group/category/company, and how the user sees the consequences.

## 8. Opening Balance and Carry-Forward

The learning is that ongoing systems may carry forward inventory value through a running balance concept, but migration has a special first-period problem.

For SMEsPlus, the first migrated period cannot rely on a prior internal close that does not exist yet. Therefore opening stock quantity and opening stock value must be proven against Accounting opening balances.

Required design points:

| Item | Required Decision |
|---|---|
| First opening stock quantity | Source, owner, cut-off date, and approval must be defined. |
| First opening stock value | Must reconcile with Accounting opening balance. |
| Prior-period boundary | Must be locked before live transaction migration. |
| Adjustment after migration | Must require controlled exception and audit trail. |

This remains a joint Account x Inventory issue.

## 9. Post-Close Correction Governance

A controlled ERP must allow correction when legally or operationally necessary, but the correction must not silently bypass Accounting control.

SMEsPlus must define:

1. exception requester;
2. approving authority;
3. reason code;
4. date and period affected;
5. expiry of the exception;
6. audit record;
7. whether correction affects Inventory only, Accounting only, or both;
8. whether financial statements must be regenerated or flagged.

A single global bypass is not acceptable as a target design without explicit Boss approval.

## 10. Named Gaps Preserved

| Gap | Clean-Room Statement | Owner |
|---|---|---|
| G-1 | No approved SMEsPlus sequencing contract exists between Accounting close and Inventory valuation close. | Team B / Boss |
| G-2 | Post-close Inventory correction governance is not yet designed to the same audit strength expected from Accounting. | Team B / Audit |
| G-3 | Cut-off granularity remains undecided: document-level, line-level, or hybrid. | Team B |
| G-5 | Migration first opening balance requires Account x Inventory cross-proof. | Team A + Accounting + Inventory |
| G-6 | Year-end retained-earnings treatment must be designed for SMEsPlus and Thai statutory/audit expectation. | Accounting/Tax + Team B |

## 11. Periodic vs. Perpetual Learning

The prior learning supports the following business distinction:

| Valuation Mode | What Happens During the Month | What Happens at Close |
|---|---|---|
| Periodic | Stock moves affect quantity; accounting value is summarized later. | Closing calculates and posts or proposes the value difference. |
| Perpetual | Stock moves affect quantity and accounting value closer to the movement event. | Close is mainly reconciliation and adjustment. |

SMEsPlus must decide:

- whether both modes are allowed;
- whether selection is controlled by company, product category, product type, or another SMEsPlus-native policy object;
- whether switching mode is allowed after go-live;
- how historical reporting is protected if mode changes;
- what Thai accounting/tax constraints apply.

## 12. Year-End Close Learning

Monthly close and year-end close should not be assumed to be identical for SMEsPlus.

SMEsPlus must decide whether year-end requires:

1. final stock count lock;
2. final valuation lock;
3. final GL reconciliation;
4. retained earnings transfer or reporting treatment;
5. audit-ready close package;
6. reopening controls if post-close correction is required.

This is not closed by Inventory evidence alone.

## 13. Clean-Room Acceptance Criteria for Future Team B Work

Before Team B uses this learning for functional design, the package must pass these checks:

| Check | Required Result |
|---|---|
| No source code | No implementation excerpt appears in Team B material. |
| No vendor path or method dependence | Team B receives business behavior only. |
| No copy instruction | No sentence tells SMEsPlus to copy reference architecture. |
| Decision ownership | Every unresolved item has owner and gate. |
| Accounting dependency | Joint Account x Inventory items are not closed by Inventory alone. |
| Thai reality | Thai statutory/accounting treatment remains separately validated. |

## 14. Disposition

`N-A12-01` remains:

`HIGH FUNCTIONAL DESIGN GAP — REOPENED`

Reason: the business behavior is now understood well enough to support controlled discussion, but SMEsPlus has not yet produced and approved its own original clean-room functional design for close, valuation, retained earnings, migration opening balance, and Account x Inventory reconciliation.

This file reduces clean-room risk by replacing implementation-level evidence with business-semantics learning. It does not close the Gate.

Boss remains the sole Final Approver.