# P01 — VENDOR BILL CORRECTION INTEGRITY

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.** Produced under an explicit **disproof** assignment.

---

## 1. CLASSIFICATION

> ### `MIXED` — and the strong form of the previous finding is **CONTRADICTED**
>
> The previous round's claim — *"posted vendor bill correction **destroys** accounting
> lineage"* — **does not survive in its strong form.** Deletion of a posted move's journal items
> **writes a durable audit record of what was deleted.**

---

## 2. WHAT THE DISPROOF ESTABLISHED

Deleting a journal item from a move that has been posted before writes a **message and tracking
record** capturing the change. Six fields are tracked in both generations: the account, the
label, the balance, the taxes, the tax tags and the maturity date.

**Proven executing in a deployment**, not merely present in source: a live message recording a
deleted journal item, with four tracking rows preserving the account, the balance and the tax
information.

Classification: **FACT VERIFIED** (expert, with deployed evidence).

---

## 3. WHAT DIES AND WHAT SURVIVES — THE PRECISE ANSWER

| | |
|---|---|
| **Survives** | the bill itself · the payable line · the document name · the posted-before marker · and, in the audit record, **the account and the amount** of each deleted item |
| **Destroyed** | the item's **kind** (that it was a valuation line) · its link to the originating purchase line · product · quantity · partner · analytic distribution · currency |

> **You can recover *what was posted*. You cannot recover *what it was for*.**

That is a materially different — and more precise — finding than "lineage is destroyed", and it
is the finding P01 now carries.

---

## 4. FOUR WEAKNESSES IN THE SURVIVING RECORD

The audit trail exists, and it is not strong:

| # | Weakness |
|---|---|
| 1 | **It is itself deletable** — the guard that would protect it is gated on an audit-trail setting that is **unset on 44 of 44 companies** |
| 2 | The field-identification column is **null in every row** — 5,407 of 5,407 in one database, 4,019 of 4,019 in another |
| 3 | **190 of 202** bill-related chatter rows in one database are **orphaned** |
| 4 | On the v16 deployment the claim **survives in full force**: that database logs 10,147 created-or-updated events and **zero deletions** |

Point 4 matters most: **the generation with the real transaction history has no deletion audit
at all.**

---

## 5. DEPLOYED CONTROL STATE

| Control | State |
|---|---|
| Entry hashing | **on 0 of 109 journals**, including **0 of 7 purchase journals** |
| Audit trail | **on 0 of 88 companies** |
| All five lock dates | **unset everywhere** in the analysed databases |

Every guard that would make correction-by-deletion safe is available and switched off.

---

## 6. A v19 REGRESSION FOUND IN PASSING

v18 **refused** to delete a reconciled line — a check that raised. **v19 replaced it with a
routine that silently tears the reconciliation down**, and the source comment changed from
*"check the reconciliation"* to *"break the reconciliation"*. v19 also removed a brake on the
reset-to-draft button.

**Expert-reported; not re-derived by this session.**

---

## 7. FINAL CLASSIFICATION AGAINST THE DIRECTIVE

| Required value | Verdict |
|---|---|
| `REVERSAL` | no |
| `DELETION` | partly — the items are hard-deleted |
| `MUTATION` | no |
| **`MIXED`** | **yes — deletion of the item, with partial preservation in a separate, weakly-protected audit record** |
| `VERSION / MODULE DEPENDENT` | yes — the audit record exists in 18/19 and **not** in the v16 deployment |

---

## 8. WHAT THE TARGET DESIGN SHOULD TAKE

1. **Correction must be by reversal**, so that *what it was for* survives, not only *what it
   was*.
2. **An audit record that can be deleted is not an audit record.**
3. **A control that ships switched off protects nothing.** Every relevant guard here is
   available and unset in every analysed database.

## 9. WHAT REMAINS OPEN

| ID | Item | Status |
|---|---|---|
| `BC-01` | Whether reset-to-draft succeeds at all on a reconciled, hashed or locked bill | `HOLD — RUNTIME EVIDENCE REQUIRED` |
| `BC-02` | The v19 reconciliation-teardown regression | expert-reported, **not re-derived** |
| `BC-03` | `D4`'s correction history | **class C, known-reachable** |
