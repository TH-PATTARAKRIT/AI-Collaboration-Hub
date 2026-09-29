> Domain: MANUFACTURING_VALUATION_PILOT (Gx7) | Documentation-Tier

# 01 — EXECUTIVE RESEARCH SUMMARY (Gx7)

## Scope

Five functions: raw material consumption → WIP transfer, finished goods completion → valuation transfer, manual interim WIP posting/reversal for long-running orders, MO cost computation, and a flagged edge case (negative-inventory revaluation entries).

## Material finding — the unifying rule strengthens, doesn't complicate, the Gx6 resolution

> **STATUS DOWNGRADE (2026-09-29, Boss ruling).** The Gx6 resolution this section confirms is `Material Finding — Independently Unverified`, not Canonical Architecture Truth, pending `CHATGPT_AUDIT` independent re-audit. See `00_Architecture_Governance/STATE03_VALUATION_TIMING_CROSS_GX_CONTRADICTION_MATRIX.md`.

Documentation states plainly: consuming raw materials moves value from the component's stock valuation account to a **WIP account** automatically (under Automated/real-time valuation); completing the MO transfers that WIP value to the finished-good's valuation account, automatically, plus labor/operations cost. Both are **automatic, not deferred to any invoice** — because manufacturing has no external vendor-bill/customer-invoice equivalent. This confirms the general rule discovered in Gx6: posting happens at the financial-transaction event, and for an internally-generated event (adjustment, manufacturing consumption/completion), the event itself *is* the financial transaction, so it posts immediately; for an externally-invoiced event (receipt, delivery), posting defers to that invoice. Three pilots (Gx4, Gx7, and by extension Gx6 itself) now converge on this single model rather than three separate exceptions.

## Second finding — WIP has its own optional interim mechanism for long-running orders

For manufacturing that spans a reporting boundary, a **manual, postable-and-reversible "Post WIP Accounting Entry"** action exists — distinct from the automatic consumption/completion entries — specifically to reflect partial completion value mid-process. This is itself analogous to Gx6's period-close accrual mechanism, but manually triggered per-MO rather than a single period-wide close.

## Not established

Negative-inventory / revaluation entries during an MO (surfaced only via a forum thread title, not yet read in detail) are flagged as an open edge case, not characterized. Full runtime confirmation of the whole model, as with every prior Gx.
