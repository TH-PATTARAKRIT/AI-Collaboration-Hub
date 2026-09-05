# P06_SEQUENCE_REWIND_FORENSIC.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S07)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **This file substantially REVISES the round-3 sequence-rewind claim.** The rewind is real as an `ALTER SEQUENCE`, and it is **largely irrelevant to v18 journal-entry numbering** — because v18 does not number journal entries from `ir.sequence` at all. The observable renumbering has a **different cause**, and that cause is worse.

---

## 1. The mechanism is real

**SRF-F-01 — For `implementation = 'standard'`, the counter IS a Postgres sequence object, and writing `number_next` rewinds it.**
`$V18E/base/models/ir_sequence.py:171-179`:
```
if seq.implementation == 'standard':
    if new_implementation in ('standard', None):
        if values.get('number_next'):
            _alter_sequence(self._cr, "ir_sequence_%03d" % seq.id, number_next=n)
```
`:32-46` — `_alter_sequence` issues `ALTER SEQUENCE <name> RESTART WITH <n>`.
The module writes `{'number_next': 1}` (`model.py:35-38`, `:189-193`), which is truthy. **The `ALTER SEQUENCE … RESTART WITH 1` executes.**

**SRF-F-02 — `number_next` is a column; `number_next_actual` is the truth.**
`ir_sequence.py:94-104` — for `standard` it reads the Postgres sequence via `_predict_nextval`; only for `no_gap` does it fall back to the column. `no_gap` (`:196-201`) locks the row `FOR UPDATE NOWAIT` and increments the column.

---

## 2. And it is largely irrelevant to v18 journal numbering

**SRF-F-03 — `account.move` does NOT use `ir.sequence` in v18. This is the decisive finding.**
`$V18E/account/models/account_move.py:88` inherits `sequence.mixin`. `$V18E/account/models/sequence_mixin.py:267-300` derives the next number by **querying the table itself** — *"taking the number with the greatest alphabetical value"*, `SELECT {self._sequence_field} FROM {self._table} …`, narrowed by `account_move.py:3479-3500` to `WHERE journal_id = %(journal_id)s AND name != '/'`.

**DENOMINATOR:** PATTERN `ir\.sequence` over `$V18E/account`, `--include='*.py'`. **RESULT: 4 hits, none of them journal-entry numbering** — `company.py:158,161` (batch-payment sequence), `account_payment.py:378` (a `_compute_name` fallback reached only when `move_id.name` is falsy), and one test fixture.

**SRF-F-04 — The prefixes the module targets are pre-v18 artefacts.**
`'BNK1/%'`, `'CSH1/%'`, `'INV/%'`, `'EXCH/%'`, `'MISC/%'`, `'账单/%'`, `'杂项/%'` (`model.py:186-193`) are **v12/v13-era journal sequence prefixes**. They no longer drive `account_move.name`.

**SRF-F-05 — For date-ranged sequences the write is a no-op on the counter that actually issues numbers.**
`ir_sequence.py:171-179` alters only `ir_sequence_%03d`. Date-range subsequences (`ir_sequence_%03d_%03d`) are altered only in the `number_increment` branch. But `_next` delegates to the subsequence when `use_date_range` is set (`:256-262`). **So for any date-ranged sequence, `number_next: 1` changes a value nothing reads.**

---

## 3. The renumbering is real — and its cause is worse than a sequence reset

**SRF-F-06 — The two clauses, stated adjacently so neither is read alone** *(clarified at challenge, E1-S-03)*: **the `ALTER SEQUENCE` is largely inert against v18 journal numbering, AND the renumbering happens anyway by a different mechanism.** The correction moves the *cause*, not the *effect* — and it makes the finding worse, because protecting `ir.sequence` would not prevent it.

**Document numbers become reusable because `delete from account_move` empties the table that `_get_last_sequence` reads.**

v18 derives the next number from the **highest existing name in the journal**. Delete every row and the highest existing name is nothing. **The next entry starts again at 1 — not because a counter was reset, but because the evidence of prior numbering was destroyed.**

**This is a stronger finding than the one it replaces**, for three reasons:
1. **It cannot be prevented by protecting `ir.sequence`.** The vulnerability is that numbering is derived from data rather than from a counter.
2. **It is silent.** No `ALTER SEQUENCE` appears in any log; the numbering simply restarts.
3. **It applies to every `sequence.mixin` consumer**, not only to the prefixes the module happens to name.

**Classification: FACT VERIFIED** for the mechanism (`sequence_mixin.py:267-300` + `account_move.py:3479-3500` + the unfiltered delete). The renumbering is a **consequence of the deletion**, not of the sequence write.

---

## 4. Scope of the rewind

**SRF-F-07 — `ir.sequence.company_id` exists and is NOT required** (`ir_sequence.py:146-147`, `default=lambda s: s.env.company`, no `required=True`).

**And the module's two sequence paths disagree with each other:**
- the generic path (`model.py:31-38`) filters on code/prefix **only**, under **`.sudo()`** — so in a multi-company database it rewinds **every company's** matching sequences;
- the `remove_account` path (`model.py:180-193`) **does** filter `('company_id','=',self.env.company.id)`, and does **not** use `sudo()`.

**This is the same split-scoping defect as the table deletes** (`50_` SCOPE-F-13): one half of the operation is company-aware and the other is not, and no decision reconciles them.

---

## 5. Answers

| Question | Answer |
|---|---|
| Which sequences? | any `ir.sequence` whose `code` or `prefix` matches; generic path **all companies**, account path **current company only** |
| What objects? | in v18, **not journal entries**; `account.payment` fallback numbering and any custom sequence sharing a prefix |
| What values? | `number_next` → 1, and for `standard` a real `ALTER SEQUENCE … RESTART WITH 1` |
| Can identifiers be reused? | **YES — but principally via the table emptying (SRF-F-06), not the sequence write** |
| Legal/accounting document numbers affected? | **Journal entry names: YES, by SRF-F-06.** Tax-document numbering: **routed to P07/P08** |
| Chronological uniqueness broken? | **YES** — new entries reuse numbers previously issued to deleted entries |
| Audit references ambiguous? | **YES**, and irreducibly: the prior holder of a number no longer exists to disambiguate it |
| Rewind scope | **inconsistent** — global under `sudo()` on one path, company-scoped on the other |

**No statutory conclusion is drawn.** Whether reused accounting document numbers breach Thai requirements is **HOLD — STATUTORY EVIDENCE REQUIRED**, routed to **P07** (tax documents) and **P08** (which owns entry numbering: `SC-JE-06` *"Entry numbering series — COMPANY"*).

---

## 6. Correction to round 3

| Round 3 | Now |
|---|---|
| *"then rewinds the bank/cash/invoice sequences to 1"* — implying this causes the renumbering | **The `ALTER SEQUENCE` is real but largely inert against v18 journal numbering.** The renumbering is caused by **emptying the table `_get_last_sequence` reads** |
| sequence reset presented as unscoped | **two paths: one global under `sudo()`, one company-scoped** |
| — | **date-ranged sequences: the write does not reach the counter that issues numbers** |

**Recorded as REV-E-14.** The round-3 statement was not false — the sequences are reset — but it **attributed the observable damage to the wrong mechanism**, which would have led a remediation to protect `ir.sequence` and leave the real defect untouched.

---

## 7. Requirements

| ID | Requirement |
|---|---|
| `SRF-R-01` | Document numbering derives from a counter that is independent of the data, never from the maximum existing value. Emptying a table must never make numbers reissuable. |
| `SRF-R-02` | An issued document number is never reused, and the fact of issuance outlives the document. |
| `SRF-R-03` | Sequence state is COMPANY-scoped and may not be altered across companies by any operation. |
| `SRF-R-04` | Any reset of a numbering series is an authorised, logged, irreversible-by-default administrative act. |

**Open:** `P06-OQ-117` — the v19 numbering mechanism was not re-derived; `iEVING` is v19.
