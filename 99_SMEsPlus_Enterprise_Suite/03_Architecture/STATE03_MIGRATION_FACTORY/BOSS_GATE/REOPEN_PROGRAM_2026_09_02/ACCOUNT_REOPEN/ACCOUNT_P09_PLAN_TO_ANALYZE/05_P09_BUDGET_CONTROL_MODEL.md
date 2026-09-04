# P09_BUDGET_CONTROL_MODEL

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Evidence identifiers resolve in the Layer 2 quarantine.

---

## 1. WHAT WAS FOUND

| Object the process needs | Present in the reference pattern? | Evidence |
|---|---|---|
| budget header | yes | EV-P09-060 |
| budget line | yes | EV-P09-060 |
| **budgetary position** (the account grouping a budget is stated against) | **not found in scope** — two modules, three name patterns, code files only; translation catalogues only | **B** (EV-P09-060) |
| budget vs actual reporting | yes — a non-stored query recomputed on every read | EV-P09-062 |
| commitment tracking | yes — from open purchase commitments only | EV-P09-063 |
| **budget control (a gate)** | **not found in the budget modules** — every raise in both modules enumerated; none references an amount or an excess | **A within those two modules; C system-wide** (EV-P09-065) |
| budget revision / versioning | yes — a revision is a copy with a parent link, and confirming the parent flips it to a revised state | EV-P09-060 |
| fiscal period binding | **not found in scope** — free-form dates only | **B** (EV-P09-069) |

**Budget excess is a displayed boolean.** It appears on the budget line, on the purchase order and on the purchase order line, and it gates nothing: no write, no state transition, no confirmation (EV-P09-065).

## 2. THE CONTROL THAT ISN'T

The directive asks for a budget control model. The reference pattern's answer is **advisory only**. This is not a defect to be corrected by imitation — many organisations run advisory budgets deliberately. It is a **determination point** that SMEsPlus must make explicitly rather than inherit by default.

**BC-01 — Budget control shall be a declared policy per budget, from a closed vocabulary:**

| Policy | Behaviour |
|---|---|
| `ADVISORY` | excess is visible; nothing is blocked |
| `WARN` | excess requires an acknowledgement recorded against the transaction |
| `APPROVE` | excess requires a named approval before the committing document may proceed |
| `BLOCK` | excess denies the commitment |

**BC-02 — The control point shall be the commitment, not the posting.** Blocking a posting after a commitment has been made is too late to be a control and too disruptive to be operable. The reference pattern's own commitment concept — open purchase commitments — is the correct anchor (EV-P09-063), and it is precisely the point where the reference pattern chooses not to act.

**BC-03 — A control shall be enforced by the server, not by a view.** In the reference pattern the only thing that stops a confirmed budget amount from being changed is a read-only attribute on two views; no server-side write guard, field-level restriction or record rule was found in either module (EV-P09-066, class B with the boundary declared). The lock therefore holds through the user interface and not through the programmable interface.

**BC-04 — State transitions shall have server-side preconditions.** Reset-to-draft sets the state unconditionally from any state, and cancel has no server-side state precondition; the draft-only restriction on the cancel action is view visibility (EV-P09-067). One integration path already exploits the gap benignly: a budget created from the project side is auto-confirmed immediately after creation, bypassing the manual open step (EV-P09-068).

## 3. THE MISSING BUDGETARY POSITION

A budgetary position answers: *what set of accounts does this budget line govern?* Without it, a budget line is matched to actuals by dimension and date alone, and the account dimension enters only as a **type filter** inside the reporting query — expense-type accounts for an expense budget, income-type for a revenue budget (EV-P09-062).

Consequences:

1. a budget cannot be stated against a specific account group — only against a whole account *type*;
2. two budgets governing different expense categories on the same cost centre and period **cannot be distinguished**, because nothing narrows them;
3. the budget's meaning depends on the chart of accounts' type assignment, which is a Core Accounting artefact, not a budget artefact.

**BC-05 — SMEsPlus shall carry an explicit budgetary position object**: a named, reusable set of accounts (or account groups) against which a budget line is stated, with its own scope and its own lifecycle. Without it, budget-versus-actual is not attributable.

## 4. BUDGET REVISION AND HISTORY

Revision exists as a copy-with-parent-link. Two properties are worth carrying forward and one is not:

- **carry forward:** revision as a first-class object rather than an in-place edit; the original remains readable.
- **carry forward:** the original transitions to an explicit revised state rather than being deleted.
- **do not carry forward:** the amount on a confirmed budget remains writable through the programmable interface (BC-03), so the revision object can be bypassed entirely.

**BC-06 — Once confirmed, a budget amount shall be immutable. Change shall occur only by revision.**

## 5. WHAT A BUDGET IS MEASURED AGAINST

Fully treated in `P09_ACTUAL_VS_BUDGET_TRACE`. Summarised here because it bears on control design: the reference pattern's three figures — achieved, committed and theoretical — are computed from **three different sources on three different time bases**, none of them stored. A control built on an unstored, multi-basis figure is a control whose trigger cannot be reproduced after the fact.

**BC-07 — Any blocking or approving control shall fire against a stored, dated, reproducible consumption figure, and the figure that fired shall be retained with the transaction.**

## 6. SCOPE DETERMINATION FOR THE BUDGET

Under `SMEPLUS-26-09-04-ACC-REV2-CORR1`:

| Budget kind | Owning scope | Tenant context | Company context | Rationale |
|---|---|---|---|---|
| group / management budget spanning several legal entities | **TENANT** | mandatory | **not required** | it governs management intent, carries no financial effect, and is not a legal artefact |
| statutory or legal-entity budget | **COMPANY** | mandatory | mandatory | it governs a legal entity's result |
| platform-level reference budget template | **PLATFORM** | not required | not required | reference data only; carries no amounts attributable to anyone |

**BC-08 — The budget record shall declare its own scope.** The reference pattern's budget carries an optional company whose empty value means "visible to every company" (EV-P09-070) — a single nullable field being asked to express both ownership and availability. Under the corrected constitution these are separate concerns and shall be separately represented.

**BC-09 — A TENANT-scoped budget consumed by COMPANY-scoped actuals is a legitimate and expected configuration.** It requires an explicit, named cross-company aggregation with its own authorisation (`P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` B-09), not an implicit widening through an empty field.

## 7. OPEN AND HELD

| ID | Item | Status |
|---|---|---|
| BC-U-01 | whether any budget control exists **outside** the two budget modules | **C — not searched.** Selected by module-name pattern only. Recorded so it is never restated as an absence. |
| BC-U-02 | Thai statutory requirements bearing on budgetary control or public-sector budget reporting | **HOLD / EVIDENCE REQUIRED** — routed to the Accounting-Tax track. No statutory claim is made here. |
| BC-U-03 | whether SMEsPlus requires commitment accounting at all (a ledger-visible encumbrance) | **Boss determination required.** The reference pattern has commitment as a *reporting* concept only, never as a posting. |

## 8. TERMINAL STATE

**BC-01 … BC-09 ISSUED AS PROPOSALS. BUDGET CONTROL IS DETERMINED TO BE ABSENT AS A GATE IN THE SCOPE SEARCHED. NO GATE MOVED.**
