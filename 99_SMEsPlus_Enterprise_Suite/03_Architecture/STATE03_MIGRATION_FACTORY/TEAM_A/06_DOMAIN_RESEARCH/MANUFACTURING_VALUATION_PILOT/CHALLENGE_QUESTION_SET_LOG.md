> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx7)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-MFG-01 | Does manufacturing consumption/completion follow the Gx6 "post at invoice time" rule, or its own model? | "Everything defers to an invoice, per Gx6" | **Contradicted, but reconciled at a higher level** | Manufacturing posts automatically at consumption/completion — no invoice involved at all — because there is no external bill/invoice event for internal production; this is the same "financial-transaction-time" rule, just applied where the manufacturing event itself is that transaction. |
| CQS-MFG-02 | Does manufacturing conserve total inventory value (component value out = finished good value in)? | Assumed: yes, conservation | **Contradicted** | Documentation explicitly states finished goods "usually raise total inventory value" via added labor/operations cost. |
| CQS-MFG-03 | Is WIP interim posting automatic for any multi-day MO? | Assumed: automatic if MO spans a period | **Contradicted** | Documented as a manual, optional per-MO action — not automatically triggered by elapsed time or period boundaries. |

## Status

`CLOSED (documentation-tier)`: CQS-MFG-01 (reconciled, not merely contradicted), CQS-MFG-02, CQS-MFG-03.

No round cap. `MFG-F05` (negative-inventory revaluation) has no challenge question yet — needs a documentation pass before one can be formed.
