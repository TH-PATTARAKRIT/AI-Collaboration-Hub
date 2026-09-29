> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Challenge Question Set Log

# CHALLENGE QUESTION SET (CQS) LOG (Gx7)

| ID | Challenge question | Hypothesis challenged | Outcome | Evidence |
|---|---|---|---|---|
| CQS-MFG-01 | Does manufacturing consumption/completion follow the Gx6 "post at invoice time" rule, or its own model? | "Everything defers to an invoice, per Gx6" | **Contradicted, but reconciled at a higher level** | Manufacturing posts automatically at consumption/completion — no invoice involved at all — because there is no external bill/invoice event for internal production; this is the same "financial-transaction-time" rule, just applied where the manufacturing event itself is that transaction. |
| CQS-MFG-02 | Does manufacturing conserve total inventory value (component value out = finished good value in)? | Assumed: yes, conservation | **Contradicted** | Documentation explicitly states finished goods "usually raise total inventory value" via added labor/operations cost. |
| CQS-MFG-03 | Is WIP interim posting automatic for any multi-day MO? | Assumed: automatic if MO spans a period | **Contradicted** | Documented as a manual, optional per-MO action — not automatically triggered by elapsed time or period boundaries. |

| CQS-MFG-04 | Does Odoo 19 still post the pre-19 "Revaluation of WH/MO/XXX (negative inventory)" entry for negative-inventory MO consumption, or has this been superseded by vendor-bill-time-only posting? | Carried forward from `GAP-MFG-01` | **Open — Version Tension, Not Resolved** | Forum thread (pre-19) and Odoo-partner blog (v19) disagree; no official Odoo 19 documentation page found this round confirming either reading. See `06_BUSINESS_RULE_REGISTER.md` MFG-F05, `19_PROVENANCE_REGISTER.md` EV-MFG-05/06. |

## Status

`CLOSED (documentation-tier)`: CQS-MFG-01 (reconciled, not merely contradicted), CQS-MFG-02, CQS-MFG-03.

`OPEN (Version Tension, sub-documentation-tier evidence only)`: CQS-MFG-04 — `MFG-F05` now has a formed challenge question (2026-09-29) but not a documentation-tier answer; official-doc or AWT confirmation still required.
