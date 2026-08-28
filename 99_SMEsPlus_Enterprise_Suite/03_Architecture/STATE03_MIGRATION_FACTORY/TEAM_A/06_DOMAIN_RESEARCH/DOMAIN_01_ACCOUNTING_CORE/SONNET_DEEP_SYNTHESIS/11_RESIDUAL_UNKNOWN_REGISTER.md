> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 11 — RESIDUAL UNKNOWN REGISTER

Consolidates Part 1's 13 gaps (GAP-D01-01…13, still open except GAP-D01-02 which Part 1 closed)
with unknowns newly surfaced by this synthesis pass. **Class G. Zero progress credit.**

## CARRIED FORWARD FROM PART 1 (unresolved)
GAP-D01-01 Enterprise accounting behaviour unobservable (black-box) · GAP-D01-03 no
representative dataset · GAP-D01-04 rounding/decimal-precision policy · GAP-D01-05
chart-template mechanics · GAP-D01-06 analytic coupling depth · GAP-D01-09 customer-layer
accounting modules · GAP-D01-10 system-generated line taxonomy · GAP-D01-11 data-level balance
proof · GAP-D01-13 `account_move` header-level CHECK constraints not enumerated.

## PARTIALLY RESOLVED THIS ROUND
- **GAP-D01-07** (Thai statutory obligations) — SPLIT, not closed. e-Tax invoice integrity
  (AP-10) and tax-invoice numbering (AP-11) now have real, cited evidence. Whether either
  extends to the general ledger / all journal entries remains open.
- **GAP-D01-08** (gapless numbering, Thai legal status) — SPLIT similarly; confirmed for tax
  invoices at P4 confidence, unconfirmed for the general ledger.
- **GAP-D01-12** (A6 triangulation) — 9/9 targets now addressed (was 3/9); **closed as
  "addressed," not as "all resolved to VERIFIED CLOSED"** — several remain honestly UNKNOWN.

## NEW UNKNOWNS SURFACED THIS ROUND
| ID | Unknown | Source of the question | Route to close |
|---|---|---|---|
| GAP-D01-14 | Default value of `restrict_mode_hash_table` (opt-in field) never independently confirmed | CF-02 reasoning, §4 | Read the field declaration's `default=` argument |
| GAP-D01-15 | Mechanism (if any) preventing `hard_lock_date` from moving backward | CF-03 reasoning; RC-02 disagreement | Targeted source read of the field's write path / any override guard |
| GAP-D01-16 | `balance` column's arithmetic consistency with `debit − credit` — no CHECK constraint found tying them | MR-02, new mathematical finding | Re-inspect TOC for a constraint not yet enumerated, or confirm its absence is genuine |
| GAP-D01-17 | IAS 21 periodic remeasurement of monetary items — whether implemented at all | MR-04 reasoning | Source read of `account_move` currency revaluation logic (if any) |
| GAP-D01-18 | Whether Enterprise-layer UI (`account_accountant`) restricts reset-to-draft beyond the core guard | CF-06 point 12 | **Cannot be closed — black-box, permanently unreadable under clean-room rule** |
| GAP-D01-19 | Whether cross-company posting is actually blocked, or merely typed by FK | INV-03 reasoning | Targeted source read of company-boundary validation logic |
| GAP-D01-20 | Future-dated posting — whether restricted | Exception analysis §09 | Targeted source read |
| GAP-D01-21 | Concurrency control on simultaneous edits | Exception analysis §09 | Out of scope for a read-only forensic pass; would need ORM-locking research |
| GAP-D01-22 | Whether reopening a posted entry is role-gated beyond the core status guard | Exception analysis §09 | Security/permission domain pass (deferred) |
| GAP-D01-23 | Semantics of a reversal-of-a-reversal (chain behaviour) | Exception analysis §09 | Targeted source read of reversal chain handling |
| GAP-D01-24 | Primary-source (statute text) confirmation of Thai Revenue Code §86 and the e-Tax integrity requirement's scope | 08 triangulation confidence note | Locate and read the primary legal text, not secondary summaries |

## STATUS
```
GAPS CARRIED FORWARD, UNRESOLVED : 9
GAPS PARTIALLY RESOLVED THIS ROUND : 3  (07, 08, 12 — split or addressed, not fully closed)
GAPS PERMANENTLY UNCLOSEABLE      : 1  (GAP-D01-18 — black-box by rule, not by effort)
NEW UNKNOWNS SURFACED             : 11 (GAP-D01-14..24)
TOTAL OPEN AFTER THIS ROUND        : 20
```
Every item above receives **zero progress credit** per directive §22/§16. Surfacing more
unknowns than existed before is treated as evidence of deeper, more honest analysis — not as
a regression.
