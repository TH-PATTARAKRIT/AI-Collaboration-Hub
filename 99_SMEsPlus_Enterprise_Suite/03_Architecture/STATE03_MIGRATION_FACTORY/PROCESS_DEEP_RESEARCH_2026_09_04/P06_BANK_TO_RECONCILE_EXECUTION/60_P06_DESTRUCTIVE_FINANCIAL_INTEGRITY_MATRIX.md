# P06_DESTRUCTIVE_FINANCIAL_INTEGRITY_MATRIX.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S05)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"Do NOT equate 'database remains balanced' with 'financial history remains valid.'"*

---

## 1. The matrix

| Question | Answer | Mechanism |
|---|---|---|
| Can historical financial truth be deleted? | **YES** | `delete from account_move` / `account_move_line`, no WHERE |
| Can posted journal entries disappear? | **YES** | posted state is a column; SQL does not read it |
| Can journal items disappear **without** their entry being targeted? | **YES — by cascade** | `account_move_line.move_id` is `required=True, ondelete="cascade"` |
| Can reconciliations disappear? | **PARTIALLY, and that is worse** | partials deleted; **full-reconcile heads survive orphaned** |
| Can payment history disappear? | **YES** | `account_payment` in both accounting methods |
| Can bank statements disappear? | **YES** | `account.bank.statement` (chart method); lines also **cascade** from `account_move` |
| Can audit chatter disappear? | **YES**, and it cascades further | `mail_message` + **10 non-transient cascades incl. `mail_tracking_value`**, the field-level audit trail |
| Can sequence state be rewound? | **YES for `ir.sequence`; largely IRRELEVANT to v18 journal numbering** | see `61_` |
| Can subsequent records reuse prior numbering? | **YES — but by a different route than assumed** | the table `_get_last_sequence` reads is emptied |
| Can reports still reconcile after deletion? | **They can *balance*. They cannot be *true*.** | see §3 |
| Can GL/subledger totals become orphaned? | **YES** | 17 `company_dependent` refs to `account_account` carry **no FK at all** |
| Can original source provenance be reconstructed? | **NO** | the chatter, the tracking values and the entries are gone together |
| Can deleted effects be reversed? | **NO** | no reversal, no log, no ORM hook; each table committed separately |

---

## 2. Classification

**FINANCIAL HISTORY: `DELETION OF FINANCIAL HISTORY VERIFIED`.**

Verified from source that the path deletes posted journal entries, journal items, payments, bank statements and statement lines with no WHERE clause, no state check, no lock-date consultation and no reversal. Corroborated independently by **P08 `AT-21`** and by the existence of **`om_data_remove_fix`**, a remediation module whose manifest states the deletes *"bypass the ORM"* and quotes a resulting user-facing error.

---

## 3. Why "the database still balances" is not reassurance

**DFI-F-01 — Double entry survives deletion. Truth does not.**
`delete from account_move_line` removes debits and credits **together**, so the remaining ledger still foots. A trial balance after the event is internally consistent and **describes a business that did not happen**. Balance is preserved precisely because everything is removed symmetrically — which is why balance is the wrong test.

**DFI-F-02 — The ledger is left in a state the application itself rejects.**
Full-reconcile heads survive with zero parts; `account_move_line.full_reconcile_id` points at them; the ORM constraint at `account_move_line.py:1340-1356` requires `matching_number` to agree with `full_reconcile_id`. That constraint is **Python, not Postgres**. So the database accepts a state that the ORM will refuse on the next write to those lines — **the corruption is latent and surfaces later, at an unrelated operation.**
This is exactly what `om_data_remove_fix` was written to clean up: *"Missing Record … (Record: stock.picking(58,), User: 2)"*.

**DFI-F-03 — Exchange-difference entries are never reversed.**
`account_full_reconcile.unlink()` exists to reverse them. Raw SQL never calls it. **So FX gains and losses booked by a reconciliation remain in the P&L after the reconciliation that justified them has been deleted.** Reported profit is left carrying the consequence of a settlement that no longer exists.

**DFI-F-04 — And the audit trail is destroyed by the same act that destroys the records.**
`remove_all` chains `remove_account` → `remove_account_chart` → `remove_message`. `mail_message` cascades to `mail_tracking_value`. **One call removes the facts, the discussion of the facts, and the field-level record of what changed.** There is no order of operations in which the evidence outlives the event.

**DFI-F-05 — Deletion of a posted entry leaves no record on a default installation, independently of this module.**
P08 `JPM-28`: the deletion-log routine *"filters to entries whose company has the retention option **enabled**. On a default installation that option is off, so a forced deletion of a posted entry leaves **no log line and no database record — no evidence at all**."*
**So the ORM path is also silent by default.** `P06-B-12` is worse than recorded: the company toggle governs not only whether deletion is permitted but whether it is **recorded**.

---

## 4. What survives, and why it is the wrong comfort

| Survives | Why it does not help |
|---|---|
| Trial balance foots | symmetric removal (DFI-F-01) |
| `account_full_reconcile` rows | orphaned heads — worse than absence |
| FX difference entries | unreversed, unjustified (DFI-F-03) |
| `res.partner.bank` | only because 3 RESTRICTs refuse — and the refusal is swallowed |
| `account.journal`, `account.account` | often refused for the same reason; **partial success is the normal outcome** |
| Product/partner property values | they point at deleted accounts, with **no FK** to protect them |

---

## 5. Requirements

| ID | Requirement |
|---|---|
| `DFI-R-01` | A posted financial fact is immutable and undeletable. Correction is by a new, linked, dated fact. |
| `DFI-R-02` | The audit trail is not deletable by any operation, and is not a cascade target of any relation. |
| `DFI-R-03` | An operation that leaves the ledger in a state the domain layer rejects must not be expressible. |
| `DFI-R-04` | Consequential entries (FX difference, cash-basis tax) are linked to the fact that produced them and are reversed with it, or the removal is refused. |
| `DFI-R-05` | *Balanced* is not *valid*. Integrity tests must assert provenance and referential completeness, not only that debits equal credits. |
