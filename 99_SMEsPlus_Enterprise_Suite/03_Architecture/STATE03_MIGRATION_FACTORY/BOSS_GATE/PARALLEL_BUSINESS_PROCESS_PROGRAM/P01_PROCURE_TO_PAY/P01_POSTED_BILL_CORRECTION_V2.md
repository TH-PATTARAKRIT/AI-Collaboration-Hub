# P01 — POSTED BILL CORRECTION v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.** Produced under an explicit **disproof** assignment.

---

## 1. CLASSIFICATION

> ### `MIXED` — confirmed, and now **worse than the prior round recorded**
>
> Reliance: **HOLD.**

---

## 2. THE SEVEN CORRECTION PATHS

| Path | What happens |
|---|---|
| **Reset to draft** | derived journal items are **hard-deleted**; still-draft derived assets are deleted |
| **Cancel** | same deletion; and see §4 on sequence numbers |
| **Reverse** | a counter-entry is created — **history preserved** |
| **Credit note** | a new document with its own identity — **history preserved** |
| **Delete** | permitted; guards that would prevent it are **off everywhere** |
| **Modify** (after posting) | **REFUSED** by the lock check — the one path that refuses |
| **Repost** | re-runs the derived-item creation |

**Two of seven preserve history. Four destroy or mutate. One refuses.**

---

## 3. WHAT SURVIVES A DELETION — CORRECTED IN FOUR PLACES

The prior round recorded that deletion writes a tracking record capturing six fields. The
disproof corrects that:

| Prior statement | Corrected |
|---|---|
| *"the field-identification column is null in every row"* | **CONTRADICTED.** The field **identifier** is populated in every observed row; it is a different, descriptive column that is null |
| *"six tracked fields"* | **Six is the capability. Observed records carry four** |
| *"a deletion writes a record"* | **Every deletion message is paired with a creation message — the prior round read only half the evidence** |
| *"the audit record is deletable"* | **Confirmed**, and the cause identified: it is **configuration state, not design** — every protective setting is off |

---

## 4. THE EMPIRICAL FINDING THAT BREAKS THE AUDIT RECORD

In the one deployment where deletions were logged at all:

> **The two logged deletions are a destroy-and-recreate of the same tax line.** The deleted item
> and the surviving item are identical in account, label, balance and tag.
>
> **The audit record cannot distinguish a real business deletion from a system re-issue.**

And worse:

> **Three further journal items are gone with no record at all. Un-logged destructions outnumber
> logged ones three to two.**

And after cancellation:

> **The posted sequence numbers were overwritten**, and the replacement numbers now sit in a live
> sequence alongside other posted documents.

**All expert-reported; not re-derived by this session.** Each is high-consequence and should be
re-derived before reliance.

---

## 5. EVERY GUARD IS OFF, EVERYWHERE

| Guard | State |
|---|---|
| Restrictive audit trail | **unset in all 89 company rows** across the estate |
| Journal hash chaining | **off in all 119 journals** |
| Per-move immutability hash | **set on 0 of 183,600 moves** |

> The protections exist, ship **off**, and are off in every deployment.

*Counting note: the 89 and 119 figures aggregate across archives, and two archives are one
estate — so the distinct populations are smaller. The **proportion is unaffected**: it is zero
everywhere.*

---

## 6. THE THREE LINEAGE KINDS — ANSWERED PER PATH

| Path | NUMERICAL | ACCOUNTING | **BUSINESS SEMANTIC** |
|---|---|---|---|
| Reverse | preserved | preserved | **preserved** |
| Credit note | preserved | preserved | **preserved** |
| Reset to draft | **partly** — amount survives in the tracking record | **partly** — account survives | **LOST** |
| Cancel | partly | partly | **LOST**, and the document number may be overwritten |
| Delete | **lost where unlogged** | lost where unlogged | **LOST** |
| Modify | n/a — refused | n/a | n/a |

> **You can often recover *what was posted*. You cannot recover *what it was for*, and on the
> unlogged paths you cannot recover it at all.**

---

## 7. DISPOSITION

| Item | Status |
|---|---|
| Classification | **`MIXED`** |
| Reversal paths | preserve history |
| Draft/cancel/delete paths | **destroy business meaning** |
| The audit record | **exists, is incomplete, is deletable, and cannot distinguish deletion from re-issue** |
| Unlogged destruction | **observed, and more frequent than logged destruction** |
| Guards | **off in every deployment** |
| Owner | **P08** owns correction and audit architecture. P01 supplies evidence |
