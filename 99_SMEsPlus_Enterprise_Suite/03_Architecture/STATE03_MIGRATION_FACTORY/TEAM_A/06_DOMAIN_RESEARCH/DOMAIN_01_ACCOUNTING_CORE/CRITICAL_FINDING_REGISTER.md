# CRITICAL FINDING REGISTER — DOMAIN_01 ACCOUNTING CORE (CANONICAL)

Created by CORR-03 to resolve a counting inconsistency in the prior round.

## THE INCONSISTENCY, AND WHAT CAUSED IT
The prior round stated **6** critical findings in the evidence pack, **5** in the executive
summary, and applied **5** neutralization records (N-01…N-05).

Root cause, determined not assumed: the count was never wrong in substance — **six findings
exist, and N-02 covers two of them.** CF-04 (reversal is a relationship, not a state) and
CF-06 (posted history is mutable via reset-to-draft) are both aspects of the *correction
model*, and were neutralized together in N-02. The executive summary then reported "five
findings that matter most" by listing neutralization records rather than findings.

**Canonical count: 6 critical findings, 5 neutralization records.**
Both numbers are correct and are now stated together everywhere they appear.

## CANONICAL TABLE

| Finding ID | Finding | Critical? | Neutralized? | Evidence | Status |
|---|---|---|---|---|---|
| **CF-01** | Entry-level `Σdebit = Σcredit` is enforced only by application code (`_check_balanced`), which is suppressible; no DB CHECK can express it and **there are zero triggers** in the database | YES | YES — N-01 | P1 `account_move.py:2765,2769`; P2 direct `pg_restore -l`: TRIGGER=0, CHECK constraints are row-level only | **VERIFIED FACT** (mechanism) / **EVIDENCE_MISSING** (whether stored data actually balances) |
| **CF-02** | Ledger tamper-evidence (`inalterable_hash`, `secure_sequence_number`) is **opt-in per journal** via `restrict_mode_hash_table` | YES | YES — N-04 | P1 `account_journal.py:145,794–800` | **VERIFIED FACT** |
| **CF-03** | Period control is six company lock-date fields + per-user computed variants + a lock-exception object + a `BYPASS_LOCK_CHECK` context escape | YES | YES — N-03 | P1 `company.py:60–113`; `account_lock_exception.py`; `account_move.py:69,2807` | **VERIFIED FACT** |
| **CF-04** | Reversal is a **relationship** (`reversed_entry_id`), not a lifecycle state; states are only draft/posted/cancel | YES | YES — N-02 | P1 `account_move.py:129–133,623,631,5433` | **VERIFIED FACT** |
| **CF-05** | Money is exact decimal end-to-end (`numeric`), not floating point | YES | YES — N-05 | P2 column definitions; P1 monetary field declarations | **VERIFIED FACT** |
| **CF-06** | Posted history is mutable by design — `button_draft` accepts entries in `posted` **and** `cancel` | YES | YES — N-02 (with CF-04) | P1 `account_move.py:6108,6109` | **VERIFIED FACT** |

**Totals — to be used identically in every artifact:**
```
Critical Findings registered      = 6
Neutralization records            = 5   (N-02 covers CF-04 + CF-06)
Verified Fact (mechanism)         = 6
Evidence Missing (data-level)     = 1   (CF-01 data-level balance)
Supported Inference               = 0
Unverified                        = 0
```

## CF-01 — CORRECTED STATEMENT (supersedes the prior round's claim)

**Prior claim (RETRACTED):** "zero CHECK constraints therefore no database enforcement."
That rested on a derived inventory which, as CORR-01 established, **cannot represent CHECK
constraints at all** (only FK/PK/UNIQUE across all 1,395 tables).

**Corrected, evidence-separated statement:**

| Layer | Finding | Status |
|---|---|---|
| Source application validation | `_check_balanced` asserts `Σdebit = Σcredit` and raises `UserError`; wrapped in `_disable_recursion(..., 'check_move_validity', default=True, target=False)` so it **can be switched off** | **VERIFIED FACT** (P1) |
| Database structural constraint | PK and FK present on both core tables | **VERIFIED FACT** (P2 direct) |
| Database CHECK constraint | **Four CHECK constraints exist on `account_move_line`** — but all are *row-level* (credit×debit=0, sign agreement, required account, empty presentation lines). A row-level CHECK **cannot** express an aggregate across an entry's lines | **VERIFIED FACT** (P2 direct) |
| Database trigger | **Zero triggers in the entire database** (TOC census). No trigger enforces balance or anything else | **VERIFIED FACT** (P2 direct) |
| Database rule | 9 rules, all view `_RETURN`; none on accounting tables | **VERIFIED FACT** (P2 direct) |
| Data-level actual balance | Whether stored entries actually balance | **EVIDENCE_MISSING** — requires a restore not performed |

**Conclusion (now verified, previously inferred):** entry-level balance has **no database
enforcement**, because the only mechanisms that could provide it — aggregate CHECK (impossible
per row) and triggers (none exist) — are absent. The guarantee is application-level and
suppressible. This is materially stronger evidence than the prior round had, and it corrects
the reasoning even though the headline conclusion survived.

## MIGRATION CONSEQUENCE (business/migration principle candidate — NOT SMEsPlus design)
> Migrated Accounting Entries must be independently validated for debit/credit balance and not
> assumed valid merely because records exist in the source database.

Classification: **B — Accounting/Regulatory** (migration-control principle).
This is a validation obligation, not an implementation instruction. No target design implied.
