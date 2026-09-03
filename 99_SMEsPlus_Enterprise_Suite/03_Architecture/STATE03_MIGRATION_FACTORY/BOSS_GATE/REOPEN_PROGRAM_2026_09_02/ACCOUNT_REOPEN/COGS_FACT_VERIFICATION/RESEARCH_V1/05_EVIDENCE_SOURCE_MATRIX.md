# 05 — Evidence Source Matrix

Applying the parent prompt's Evidence Hierarchy (Levels 1–9) to what is actually available.

| Level | Evidence Type | Available for SMEsPlus? | Available for the Reference ERP (benchmark)? |
|---|---|---|---|
| 1 | Actual Runtime Evidence | **No — no SMEsPlus runtime exists** | Partial (documented behavior only, not this session's own live session) |
| 2 | Actual Database / Transaction Data | **No — no SMEsPlus database exists** | No (not queried this session) |
| 3 | Actual Configuration | **No — no SMEsPlus instance exists** | Partial (documented defaults, some PROVISIONAL) |
| 4 | Executed Posting / Journal Evidence | **No — no SMEsPlus transaction has ever been posted** | Partial (documented worked examples, attributed to source) |
| 5 | Source Code Behavioral Evidence | **No — no SMEsPlus source code implements COGS logic yet** | Partial, cited where the DR session used it |
| 6 | Official Product Documentation | N/A (SMEsPlus has no product docs for unbuilt features) | **Yes — primary evidence tier used throughout the DR register** |
| 7 | Existing Project Research Evidence | **Yes — this is the real evidence base**: files `30`, `33`, `36` of the DR session; `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` | — |
| 8 | Business SME Confirmation | Not obtained this session (see file `17`) | — |
| 9 | External Accounting / Statutory Reference | **Yes, for Thailand-specific items** — Revenue Code §65 bis (6), Revenue Department Order Por.79/2541, TFAC TAS 2 explanatory manual (all opened directly in DR file `24`, not re-opened in this session) | — |

## What This Means for "Evidence Acquisition"

The parent prompt's Steps 05, 09 ("acquire available runtime/DB/config/posting/source evidence" and "purchase-to-COGS trace" with Transaction/Movement/Valuation/Journal Entry IDs) assume a system that produces those artifacts. SMEsPlus does not yet. The only acquirable evidence this session could add beyond what the DR session already holds would be:

1. A **live walkthrough of the actual reference ERP instance** for the five items flagged `OPEN — LIVE INSTANCE REQUIRED` in file `03` (`CGS-U05`, `CGS-U07`, `CGS-U30`, `CGS-U42`, and the FIFO sub-case inside `CGS-U32`). This requires provisioning and operating a real instance of that reference system — an action with real infrastructure/licensing footprint, not a documentation review — and was not authorized or attempted in this session.
2. A **direct re-fetch** of the 19.0 Finance/Accounting settings page that failed twice in the DR session (`CGS-U04`, `CGS-U12`). This is a bounded, low-risk documentation re-check that a future session could reasonably attempt.
3. **Business SME input** for the items in file `17` that cannot be resolved technically at all.
4. **Additional Thai statutory research** for the items in file `03` Section H that remain open beyond what DR file `24` already covered.

This session recommends (2)–(4) as the highest-value next acquisition steps, and flags (1) as requiring an explicit resourcing decision from Boss before a future session attempts it.
