> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 22 — UNKNOWN AND GAPS

| ID | Gap | Impact | Route to close |
|---|---|---|---|
| GAP-D01-01 | Enterprise accounting behaviour (reconciliation workbench, reporting engine, assets, budget) is unobservable | Cannot evidence a large part of day-to-day accounting behaviour | Behavioural observation under an authorised route; never source reading |
| GAP-D01-02 | ~~pg_restore could not run~~ | **CLOSED (CORR-01)** — executed offline with postgres:18; 28,648 TOC entries observed; triggers, rules and CHECK constraints newly established | CLOSED |
| GAP-D01-03 | Row-level accounting behaviour unavailable — snapshot is configuration/UAT (~6 entries, 23 lines) | Cannot observe posting volumes, lock behaviour in practice, reconciliation or reversal usage | Dataset with real posted activity, or purpose-entered transactions under an authorised route |
| GAP-D01-04 | Rounding and decimal-precision configuration not analysed (`decimal_precision.py` present, unread this pass) | Precision semantics unknown; material to financial correctness | Next pass on the readable `account` module |
| GAP-D01-05 | Chart-template mechanics not analysed (`chart_template.py` present) | Initial chart creation semantics unknown | Next pass |
| GAP-D01-06 | Analytic accounting analysed only structurally | Coupling depth unknown | Analytic domain, or a targeted coupled pass |
| GAP-D01-07 | Thai statutory posting/period-close obligations unknown | Cannot judge whether the observed model satisfies Thai law | External research is now AVAILABLE but **no Thai statutory source was located or cited**; requires an authoritative statutory route |
| GAP-D01-08 | Whether gapless numbering is legally required in Thailand | Affects numbering design decisions | External/statutory confirmation |
| GAP-D01-09 | Customer-layer accounting modules (`cr_effective_date_entries`, `smesplus_account_reports`, `smesplus_tax_period_date`) not analysed | Customer-specific accounting behaviour unknown | Customer-layer domain pass |
| GAP-D01-10 | System-generated line taxonomy (tax/rounding/payment-term lines) not enumerated | Migration double-count risk | Tax and AR/AP domains |

**Class G items receive zero progress credit** (F-20, F-21, F-22 in `20_CLASSIFICATION_A_G.md`).

## GAPS ADDED THIS ROUND
| ID | Gap | Impact | Route to close |
|---|---|---|---|
| GAP-D01-11 | **Data-level balance unverified** — whether stored entries actually satisfy Σdebit=Σcredit | CF-01's data half is EVIDENCE_MISSING | Restore into an isolated environment under specific authorisation, then aggregate per move |
| GAP-D01-12 | A6 triangulation covers 3 of 9 targets | Journal/posting/audit-trail/multi-currency principles not independently confirmed | Continue external triangulation |
| GAP-D01-13 | `account_move` CHECK constraints not enumerated (only `account_move_line` observed) | Header-level DB guarantees unknown | Deeper TOC inspection or source pass |

## STATUS
```
GAPS CLOSED THIS ROUND : 1  (GAP-D01-02)
GAPS ADDED THIS ROUND  : 3  (GAP-D01-11..13)
GAPS OPEN              : 12
```
