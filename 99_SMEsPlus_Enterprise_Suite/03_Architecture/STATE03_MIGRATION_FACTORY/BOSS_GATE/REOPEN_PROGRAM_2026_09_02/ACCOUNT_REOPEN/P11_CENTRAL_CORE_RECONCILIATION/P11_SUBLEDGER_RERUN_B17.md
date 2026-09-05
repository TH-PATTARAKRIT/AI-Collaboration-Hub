# P11 — `P11-B-17` DISCHARGED · THE SUBLEDGER TEST RE-RUN AGAINST ITS STATED RULE

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C05a · Layer 1 clean-room
Closes the head of the correction backlog opened at `P11-E-26` / `X2-F06` (**CRITICAL**).

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. What was wrong

`X2-F06`, the only `CRITICAL` of the 86-finding challenge, and **unrepaired for thirty-plus commits**:

> `P11_SUBLEDGER_ARCHITECTURE.md` §1 states *"a structure failing `S3` **or** `S4` is a derived view,
> not a subledger, and **no reconciliation may be claimed against it**."*
> §2 applied **"fails both"** and awarded *"of record"* to four rows failing one criterion.

**Deliberately not bodged when found** — *"bodging a critical logic error to clear an audit is how it
went unrepaired"*. It is discharged here, in a CORR1 round, by re-running all ten rows.

## 2. Corrections applied to the row data before re-running

Three challenge findings corrected the **inputs**, not just the rule. All three are applied.

| Finding | Correction |
|---|---|
| `X2-F07` | **AR and AP fail `S3` and `S4`** on the same evidence used to fail Settlement: the residual is a stored `DERIVED FACT` *"capable of drift"*; entry substance while posted is *"no — application guard, **seven production bypass sites**"*; entry existence *"no — configuration, default off"*; matching records *"deleted by an entry-level operation"* |
| `X2-F08` | **The Asset row's defect is `S2`, not `S4`** — `CTR-06` is a model constraint *evaluated on ORM write*, which **a direct data load does not evaluate**; an application-only enforcement over an unmeasured migrated population is an **agreement** question |
| `X2-F09` | **The Tax row's `S3` failure was tested with the wrong instrument** — hash coverage is tamper-**evidence**, not immutability, and CORR1 `C04` governs: *"tax fields and the due date carry field-level change tracking"* |

**And the population's `S3` is settled by evidence that did not exist when the register was written.**
`P08` @ `838134f`, over the **declared** 22-root set: *"Nine header attributes are protected and the
protection is waived by a caller-supplied parameter; a posted journal item's account, counterparty,
label, reference and cost allocation are **editable in place**."*

> ### `S3` — *"detail is immutable once posted"* — **fails for every structure whose detail is journal items.** That is AR, AP, Bank, Tax and Settlement. It is not a per-row finding; it is a property of the substrate.

## 3. The re-run, against the rule as stated

| Structure | `S1` | `S2` | `S3` | `S4` | Verdict under the **stated** rule |
|---|---|---|---|---|---|
| **AR — open receivable items** | ✔ | ✔ | **✘** substrate | **✘** residual drifts | **DERIVED VIEW** |
| **AP — open payable items** | ✔ | ✔ | **✘** substrate | **✘** residual drifts | **DERIVED VIEW** |
| **Bank / liquidity items** | ✔ | ✔ | **✘** substrate | ✔ | **DERIVED VIEW** |
| **Inventory valuation layers** | ✔ | **✘** boundary-only | ✔ | ✔ | **OF RECORD — with a disclosed agreement rule.** `S2` is not in the rule |
| **Asset register** | ✔ | **✘** ORM-only, population unmeasured (`X2-F08`) | ✔ | ✔ | **OF RECORD — agreement unverified.** `S2` is not in the rule |
| **Tax items** | ✔ | ✔ | **✘** substrate | ✔ | **DERIVED VIEW** |
| **Settlement / matching records** | ✔ | n/a | **✘** substrate | **✘** unconstrained | **DERIVED VIEW** |
| **Analytic lines** | ✔ | n/a | **✘** | **✘** | **DERIVED VIEW** |
| **WIP** | ✔ | `?` | ✔ | **✘** `JT-09` | **DERIVED VIEW** |
| **Deferred schedules** | `?` | `?` | `?` | `?` | **UNKNOWN — EVIDENCE REQUIRED** |

## 4. Result

| Measure | As published | **Re-run against the stated rule** |
|---|---|---|
| Of record, unqualified | **3** | **0** |
| Of record, qualified | 4 | **2** — Inventory, Asset; both on `S2`, which the rule does not test |
| Derived view | 1 | **7** |
| Unknown | 2 | **1** |

> ### `X2-F07`'s prediction is confirmed exactly: **"3 unqualified" becomes `0`.**
>
> **Seven of ten candidate subledgers are derived views under P11's own stated rule, and the rule's
> consequence is explicit: *no reconciliation may be claimed against them*.**

## 5. What this means, stated plainly

**Five of the seven fail `S3` for one reason** — their detail *is* journal items, and a posted journal
item is editable in place with the protection waived by a caller-supplied parameter. **This is not
five findings. It is one substrate property with five consequences**, and it is the same root as
`UAE-29`/`D-5`: *there is no immutable accounting fact to be a subledger of.*

**Corroborated independently by `P08`**, which reaches the same place from the ledger side: the general
ledger is *"a reading of the journal items"*, the partner subledger is *"a projection"*, and the only
genuine separate stores — the **fixed-asset register** and the **inventory valuation record** — are
exactly the two structures that survive here as *of record*. **Two packages, opposite directions, same
two survivors.**

**Consequence for P11's own model:** `P11_WHOLE_ACCOUNTING_SEMANTIC_MODEL.md` §5 Q7 (*"which subledger
owns the balance?"*) and Q9 (*"how is it reconciled?"*) are answered *"see the subledger architecture"*
— and the answer is now **"seven of ten cannot own a balance, and no reconciliation may be claimed
against them."** Both questions are re-pointed here.

## 6. Disposition

| Item | State |
|---|---|
| `X2-F06` (**CRITICAL**) | **REPAIRED** — rule and application now agree |
| `X2-F07`, `X2-F08`, `X2-F09` | **APPLIED** to the row data |
| `P11-B-17` | **CLOSED — DESIGN RESOLUTION VERIFIED.** Closed by re-running the rows, not by rewording |
| Original §2 register | **PRESERVED** at `P11_SUBLEDGER_ARCHITECTURE.md`, superseded by this file, per `P11-G-03` |
| Blockers closed by CORR1 | **2** — `B-17`, `B-18`; both by completed work |

> **This is the second-largest substantive change in the package's life**, after the peer intake — and
> it makes the package **worse**, not better: a headline of *three subledgers of record* becomes
> **zero**. That is the correction working.
