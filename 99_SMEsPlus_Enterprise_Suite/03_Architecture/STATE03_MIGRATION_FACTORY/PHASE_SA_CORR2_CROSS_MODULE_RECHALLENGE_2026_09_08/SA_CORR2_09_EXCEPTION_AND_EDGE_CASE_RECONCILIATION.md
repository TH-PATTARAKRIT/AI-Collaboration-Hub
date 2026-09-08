# SA_CORR2_09 — EXCEPTION AND EDGE-CASE RECONCILIATION
## CP-SA-C2-70 — EXCEPTION INTEGRITY CHALLENGED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §9. Supersedes at claim level: `SA09` §2.1 counts and `SA09-F-03`.
Master prompt §9's binding instruction: *"Do not report a gap until repository evidence and relevant
package evidence have been checked."*

---

## 1. `C2-F-25` — `SA09` diagnosed a defect and then committed it, one level up

`SA09-F-01` is one of the better findings in the parent package. It records that the Group A
exception matrix is *"the **only** one of its programme's six registers carrying **no
corrective-update section**"*, and that consumers reading it alone inherit closed items as open.
`SA09` correctly refused to inherit two of those rows.

**`SA09` then built four of its five `NOT ESTABLISHED` rows from that same register — and read the
wrong version of a sibling file.**

Measured. The path
`.../TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`
carries **three distinct blob versions** across the corpus:

| Blob | Bytes | Carries §13A? |
|---|---|---|
| `25a98a50` | 8,994 | **No — 0 occurrences** |
| `34e698ab` | 16,287 | Yes — 2 |
| `4deacf0f` | 15,128 | Yes — 2 |

§13A is the section that closes the downstream-handoff-failure gap. **`SA09` read the 8,994-byte
version**, the only one of the three without it.

> **The register was not merely unread. The wrong *version* was read — right path, right programme,
> superseded content.** `SA09-F-01` is about a stale register; this is about a stale **blob**, and
> no control in the package looked at version multiplicity. **222 paths in the v2 corpus carry more
> than one distinct content version** — `SA00` §2.1 records **223** under the parent's own frame —
> and no consumer register used that fact. *(This register first re-published the parent's 223
> without re-measuring it: a stale count, in the file whose subject is a stale version. Corrected
> after adversarial challenge.)*

---

## 2. Re-adjudication of the eight exception classes

Instrument: each class searched in **both** parties' path sets — the Group A design tree **and**
`ACCOUNT_REOPEN` (packages `P01`…`P11`, whose `*_EDGE_CASE_MATRIX.md`, `*_CONTRADICTION_REGISTER.md`
and `*_BUSINESS_EVENT_REGISTER.md` files `SA09` never opened) — in **both** vocabularies. Every
count carries a positive control on the same command shape; every zero is confirmed on a second
command shape of different form.

### 2.1 Wrong item / wrong quantity — **SPLIT: item CONFIRMED, quantity FALSIFIED**

`SA09` graded these as one row. They are two classes and they have opposite answers.

**Wrong ITEM: `NOT ESTABLISHED` — CONFIRMED**, and stated with its bound. `mis-?pick`,
`item mismatch`, `product mismatch`, `incorrect item` all return **0 corpus-wide on two shapes**.
The only two statements are negative and one is a decision:

> `| 5 | Wrong item / wrong quantity | Not observed | No dedicated correction workflow found distinct
> from … edit-in-place or return | NOT OBSERVED / EVIDENCE_MISSING |`
> **TEAM B decision: `NOT MATERIAL TO CURRENT DESIGN`** — present in **all three** blob versions.

**Two of `SA09`'s five survive** — this one, and approval rejection, which `SA09` had already
regraded and which is Boss-owned. Supplier-SLA lateness survives as **half** of a split class.
And even for wrong item the permitted claim is *not found in the declared populations searched* —
not *does not exist*. *(The first version said "the only one of the five that survives", which its
own §3 table contradicted two pages later. Corrected after adversarial challenge — in the register
whose subject is over-wide universals.)*

**Wrong QUANTITY: FALSIFIED.** The Procure-to-Pay package carries four distinct quantity-exception
rows — over-receipt; under-receipt then order closed; over-billing beyond received quantity; and
quantity difference between receipt and bill — plus a measured guard finding: **a guard blocking
reduction of ordered quantity below received quantity exists in one generation and, in a later one,
survives only in translation catalogues, one of them marked obsolete, with no equivalent guard
found.** And the SMEsPlus side already has a design position: *`EXTEND` — an explicit, configurable
over-fulfilment policy (block / warn-and-allow / allow-silently), applied symmetrically to delivered
and received.*

**`SA09` graded over/under-receipt `ESTABLISHED AS A NEGATIVE` in one row and `NOT ESTABLISHED` in
another. Both rows are about the same fact.**

### 2.2 Late supply / delivery breach — **NARROWED**

**The supplier-SLA half is confirmed absent**, with a firing control: over the Accounting path set,
`\bSLA\b`, `lead time`, `penalt`, `delivery breach`, `late delivery`, `on-time delivery`,
`vendor performance`, `supplier scorecard` → **0 blobs each**, against positive controls of 17 and 40
on the identical shape. Corpus-wide `liquidated damages` → 0.

**The late-*economic-event* half is heavily established and was missed**, because the vocabulary is
*late bill / late transaction / late cost*, not *SLA*:

> `| FE-19 | **Late transaction** | **REACHABLE, silently** | re-dated forward; the posted record
> carries no trace that its date was moved, and the warning is hidden once posted |`
> `| UAE-32 | **Prior-period attribution of a late cost** — **no prior-period attribution mechanism
> exists in the reference ERP at all** | affects late bills, late costs, close |`

### 2.3 Missing or late documents — **FALSIFIED**

Not merely established: **quantified, and `FACT VERIFIED`.**

> `| GRNI is a **swept suspense account, not an item-matched bridge** — 13,666 posted items,
> **−฿7,048,692.08**, unreconciled | FACT VERIFIED |`
> `| **B-28** | **฿29,029,467.66 received-not-invoiced is absent from the package** … 1,580 order
> lines, *"recognised nowhere in the ledger — no receipt entry, no clearing balance, no accrual"*,
> accrual control **0 of 15,522** | HIGH |`
> Three-way match: *"It is an **advisory status, not a control** … a bill in exception can be posted
> and paid."* `FACT VERIFIED`.

**Even on the narrowest reading of `SA09`'s row — *no detection of a document that failed to
arrive* — it is falsified: `0 of 15,522` is a measured detection result and ฿29.0m is the detected
population.**

### 2.4 General transaction-failure recovery — **FALSIFIED**

Closed by `SA09`'s own programme, in the two registers it did not open **and in the blob version it
did not read**:

> `| FV006-INT-002 | Downstream handoff failure / compensation | GAP FOUND | Major |`
> then, at re-verification: **`Result: VERIFIED WITH CONDITIONS`** for both retry/idempotency and
> downstream-failure compensation.
> and §13A, present in two of three blobs: a *Handoff Unresolved* status becomes visible; **retry is
> always eligible**; and a **non-disappearance guarantee** — it *"can be cleared only by the
> convergence criterion — no manual dismissal, auto-expiry, or archival/cleanup process may clear or
> hide it."*

§13A explicitly separates itself from the lateness class `SA09` conflated it with: *"§13 is about a
shipment or document being **late** … this section is about the **technical** handoff write itself
failing."*

Independently, the Accounting side supplies a 23-class and a 34-class failure taxonomy —
*"Twenty-three classes. **Twenty-one are undetectable by any control in the benchmark**"* — which is
a stronger and more useful statement than `NOT ESTABLISHED`.

### 2.5 Cross-period / cut-off — **ESTABLISHED, and the default behaviour is the defect**

> `| FE-03 | **Incorrect period** | **REACHABLE, and it is the default behaviour** | the accounting
> date is moved by a lock rule and, for non-sale documents, by a numbering rule that operates **with
> no lock configured** |`
> `| FE-21 | Reopening a period | **REACHABLE, unguarded** |`
> `### C-10 — Receipt and consumption both inside a period that then closes, bill in the next …
> **The period closes clean and complete, and is wrong by the full value of everything received and
> consumed but not yet billed.**`
> `| **Period truth** | The lock **re-dates instead of refusing**, so cut-off tests on entry dates
> are self-confirming |`

A twelve-combination cross-period matrix exists, and carries its own honest limit:
**"None of these was executed. Every row is a test to run, not a test that passed."**

### 2.6 FX — **ESTABLISHED, with a named silent defect**

> `| FE-06 | **Stale exchange rate** | **REACHABLE** | resolution falls back to the latest rate on or
> before the date, then to the earliest rate ever, then to **1.0** |`
> `| CONTRA-08 | **A posting in a currency with no configured rate is converted at 1:1, silently.**
> The resulting entry balances, satisfies the sign constraint, and passes every other control.`
> Measured: `| TZ-05 | 34,733 foreign-currency lines; **2 posted with no rate on or before their
> date** |`

Governed by **`GB-08`**, admitted to the baseline by CORR1 (`C-11`), which **prohibits** the silent
`1.0` fallback. **The ruling and the evidenced defect are the same subject, and `SA09` carried
neither.**

### 2.7 Price / cost variance — **ESTABLISHED and quantified**

> `| Price differences: **1,175 of 1,267 never reach the GL**; the 92 that do net **−฿7,267,712.95**;
> **1,082 of 1,175** sit on a bill line posted to P&L | FACT VERIFIED — replaces a statement
> *"FALSE IN BOTH HALVES"* |`
> `| 15 | Price difference where the item has no expense account | **Nothing is posted. Silent.** |`

### 2.8 Duplicate event / idempotency — **NARROWED DOWNWARD**

`SA09` graded this `ESTABLISHED` on one bin-ledger race. **The Accounting side records it as an
absence, in four independent packages:**

> `| FE-01 | **Duplicate posting** of the same business event | **REACHABLE** | no accounting-event
> identity and no idempotency key exist |`
> `| 20 | Which controls prevent duplicate or missing accounting events? | **None.** |`
> `| XM-01 | No business-level idempotency for machine-generated events | **HOLD — DESIGN DECISION
> REQUIRED** |`
> `| 15 | deterministic idempotency identity | **the single element that prevents [duplicate
> effect]; does not exist today** |`

And the owning package had already recorded the exact grading error `SA09` repeats:

> `| Idempotency | **absent as a guard** — FACT VERIFIED. **Exploitability is UNRESOLVED — EVIDENCE
> REQUIRED** and the two halves must not be collapsed into one tag. |`

**`SA09` collapsed them, in the opposite direction, having been told not to by the package it was
summarising.**

---

## 3. Count

The population is **`SA09`'s eighteen classes, plus two created by decomposition** — wrong item /
wrong quantity split, and lateness split into supplier-SLA and late-economic-event. **20.**

| Class | Members | Count |
|---|---|---|
| **`ESTABLISHED`** | partial fulfilment (sell) · partial receipt (buy) · cancel before commitment · cancel after commitment · cancel after reservation · cancel after partial movement · correction after completed movement · customer return · vendor return · retry · reversal (accounting) · timing mismatch · over/under receipt *(as a negative)* · **wrong quantity** *(falsified → established)* · **missing documents** *(falsified → established)* · **late economic event** *(falsified → established)* | **16** |
| **`NOT ESTABLISHED`** | **wrong item** · **supplier-SLA lateness** · **approval rejection** *(unchanged from `SA09`, Boss-owned)* · **idempotency** *(regraded downward)* | **4** |
| **Total** | | **20** |

**16 + 4 = 20**, and each of the twenty appears in exactly one row.

*(**Corrected after adversarial challenge.** The first version published `13 / 4 / 2 / 1 = 20` with
four classes: it counted cut-off, FX and price variance **twice** — once inside "the twelve
carried" and again in a "with a named live defect" row — and **dropped `SA09`'s fifth
`NOT ESTABLISHED` row, approval rejection**, the very row `C-13` had restored and `SA_CORR2_00` §3
re-verified. The arithmetic summed to 20 and the partition was broken. General failure recovery is
folded into **late economic event**'s row above as a falsified→established class; cut-off, FX and
price variance are master-prompt §9 classes and are carried in §4, not here.)*

> **`SA09`'s headline — *"four of the five missing classes are exceptions the world raises against
> the system"* — does not survive.** Three of the four are established, one splits, and the class
> that moved in the other direction (idempotency) is one the system raises against **itself**. The
> shape claim was real and the evidence for it was not.

---

## 4. The remaining master-prompt §9 classes

| Class | Status | Source |
|---|---|---|
| cancel · return · reverse · correction · partial fulfilment · partial receipt · partial invoice · backorder | `ESTABLISHED` | `SA09` §2, carried unchanged |
| retry | `ESTABLISHED` — always eligible, with a non-disappearance guarantee | §2.4 |
| duplicate event | **`NOT ESTABLISHED`** | §2.8 |
| timeout | **`NOT ESTABLISHED`** — no distinct evidence found; folded into failure recovery by every source | §2.4 |
| late upstream change · late vendor bill | `ESTABLISHED — with a named live defect` | §2.2, §2.5 |
| price/cost variance | `ESTABLISHED — quantified` | §2.7 |
| FX | `ESTABLISHED — with a named silent defect`, governed by `GB-08` | §2.6 |
| tax change | `PARTIAL` — fiscal-position rule base recorded as *a black box in this evidence set* | `SA08` |
| stock shortage | `PARTIAL` — mechanism determined, target binding soft (`C2-D-01`) | `SA_CORR2_02` §3.1 |
| manufacturing shortage | `PARTIAL` — same | `SA_CORR2_02` §3.1 |
| cross-period timing | `ESTABLISHED — and it is the default behaviour` | §2.5 |
| company boundary · tenant boundary | `SPECIFIED — 0 PROVEN` | `SA10`, unchanged |

---

## 5. `C2-F-26` — the exceptions are not the problem; the ledger's durability is

Reading §2.5, §2.6 and §2.8 together with `SA_CORR2_01` §3.5 produces one statement that none of the
four registers makes alone:

> **Every established exception class writes a correction into a ledger whose entries can be
> silently re-dated past a lock, whose matching rows are freely destructible across a closed period,
> and which has no identity that would make a retry safe.**

A return works. A reversal works. A retry is *"always eligible"*. **And none of the three leaves a
record the next period cannot quietly alter.** This is the same object as `C2-F-13` — the
deterministic accounting-event identity — reached from the exception side rather than the handoff
side, which is the third independent route to it in this package.

**It is not a new gap. It is the reason the exception classes being "established" is worth less than
it reads.**

---

`CP-SA-C2-70 — EXCEPTION INTEGRITY CHALLENGED (execution status).` Twenty classes; **2 not
established, and one previously graded established is not**.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
