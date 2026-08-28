> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 01 — DEEP LOGIC SYNTHESIS

## WHAT IS ACTUALLY TRUE, AND WHY
Accounting Core, stripped of vendor packaging, implements one real business capability
correctly and undermines it in one specific, identifiable way.

**Correctly implemented:** the atomic unit of financial truth (a posting line) is well-formed —
row-level database guarantees prevent a line from carrying both a debit and a credit, prevent
sign disagreement between company- and transaction-currency amounts, and prevent a
non-financial line from smuggling in financial content. Money is exact decimal throughout. A
sound correction pattern (reversal) exists and is peer-validated.

**Undermined by one specific gap:** the aggregate truth of a *whole entry* (Σdebit=Σcredit) is
never database-guaranteed, because the mechanism that could guarantee it (a trigger) does not
exist, and the only mechanism that does check it (application code) is switchable off. This
single gap is compounded, not offset, by the domain's other weakness: a posted entry can be
silently returned to an editable state and altered, with the same switchable-off balance check
applying to the re-post. **The two weaknesses are the same weakness at two different moments**
— nothing in the persisted record can be fully trusted, because nothing forces the record to
stay true either at the moment it is written or at any moment after.

## THE CONCEPTUAL BUSINESS LOGIC MODEL
```
Business Event
      │  (e.g. a sale, a purchase, an accrual, a manual adjustment)
      ▼
Validation
      │  — is this a coherent financial fact? (account exists, currency valid,
      │    company context valid, period open)
      ▼
Accounting Fact
      │  — the fact is now expressed as balanced debit/credit lines
      │    (GR-01, GR-02, GR-03, GR-04)
      ▼
Accounting Entry
      │  — the fact is committed: numbered, dated, made part of the ledger
      │    (this is the moment the reference system's guarantee is weakest —
      │    CF-01's suppressible check applies exactly here)
      ▼
Ledger Consequence
      │  — account balances change; the entry becomes an input to every
      │    downstream report (trial balance, P&L, balance sheet)
      ▼
Audit Evidence
      │  — SHOULD be forced and permanent from this point forward; in the
      │    reference system this is optional (chatter) and separate from the
      │    record's own mutability (CF-02, CF-06)
      ▼
Correction / Reversal (if required)
      — SHOULD be the only path back into this diagram once Ledger Consequence
        has occurred; the reference system offers this path (CF-04, sound) but
        does not close off the alternative, destructive one (CF-06, unsound)
```
This is the **conceptual business logic**, not SMEsPlus architecture. No target states, storage
shapes, or method names appear in it.

## THE MOST IMPORTANT SENTENCE IN THIS DOMAIN
*A fact that can be silently reopened after it has already influenced a downstream conclusion
is not a fact — it is a claim that happened, until now, to remain unchallenged.*
This is the through-line connecting CF-01 (the fact might never have been true), CF-03 (the
fact might have been recorded when it legally shouldn't have been), and CF-06 (the fact might
stop being true later without anyone being forced to notice). All three findings are instances
of one deeper problem: **the reference system has no single moment at which a financial fact
becomes non-negotiable.**

## WHERE THE REFERENCE SYSTEM IS GENUINELY GOOD, AND SHOULD BE MATCHED OR EXCEEDED
Exact-decimal money (CF-05) · row-level line integrity (MR-05's four CHECK constraints) ·
the existence of a peer-validated reversal pattern (CF-04) · journal/ledger separation of
concerns (AP-03, T-04) · account typing driving statement placement and carry-forward (GR-08).
None of these need to be reinvented; they need to be preserved.

## WHERE THE REFERENCE SYSTEM IS GENUINELY WEAK, WITH THE ROOT CAUSE NAMED
Every weakness in this domain traces to the same root: **a guarantee that exists is not
irrevocable.** The balance check exists but can be suppressed. The tamper-evidence mechanism
exists but is opt-in. The lock checks exist but have a programmatic bypass. The reversal
pattern exists but is not the only path. This is not four unrelated bugs — it is one design
posture (guarantees as defaults that can be turned off) applied consistently across the domain.
That posture, not any single field or method, is the actual thing an independent rebuild should
consciously decide whether to repeat.

## SEPARATING WHAT IS PROVEN FROM WHAT IS ASSUMED
Proven by direct evidence (source + database, this round and Part 1): the mechanism-level shape
of all six critical findings; the four row-level CHECK constraints; the zero-trigger fact;
the reversal linkage; the exact-decimal storage.
Proven by independent external triangulation this round: double-entry as universal; journal/
posting as universal concepts; correction-by-reversal and period-state modeling as validated
cross-ERP patterns (with the reference system diverging from peer practice on posted-history
mutability); IAS 21's remeasurement requirement; two scoped Thai statutory requirements.
Assumed and now flagged rather than silently carried: `hard_lock_date` irreversibility;
`restrict_mode_hash_table`'s default; whether IAS 21 remeasurement is implemented at all;
whether Thai statutory integrity/numbering requirements extend beyond their confirmed narrow
scopes. **Assumption, once named, stops being assumption and becomes a tracked question** —
that is the actual product of this synthesis pass.
