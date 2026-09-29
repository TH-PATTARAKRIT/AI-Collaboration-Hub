> Domain: PERIOD_CUTOFF_VALIDATION_PILOT (Gx6) | Evidence Annex Index

# 19 — PROVENANCE REGISTER (Gx6)

Retrieved via `WebSearch` on **2026-09-28**; same egress constraint as all prior Gx.

| Evidence ID | URL | Used for |
|---|---|---|
| EV-PCO-01 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/reporting/year_end.html` | PCO-F01, F02 (Lock Dates, fiscal year closing) |
| EV-PCO-02 | `https://www.odoo.com/documentation/19.0/applications/finance/accounting/get_started/inventory_valuation.html` | **PCO-F03 (THE resolving finding — month-end Stock Closing, accrual entries, "no longer creates journal entries upon physical receipt/delivery")** |
| EV-PCO-03 | `https://www.odoo.com/documentation/19.0/applications/inventory_and_mrp/inventory/inventory_valuation/cheat_sheet.html` | PCO-F03 (cross-referenced with Gx1 EV-GRV-04, Gx2 EV-SDV-05) |

| EV-PCO-SRC-01 | Odoo 19.0.post20260921 Community source, read-only, `account`/`stock_account` modules + license-open overlay modules `account_lock_date_update`/`base_accounting_kit` (exact file+line in `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` `D-07`) | **Source-code-tier**, retrieved 2026-09-30 by Boss's own local Claude Code session, incorporated here by this session (never read directly by it) | `GAP-PCO-01` corroborating (not closing) evidence — lock-type composition, Hard Lock irreversibility, absence of DB-level enforcement |
| EV-PCO-SRC-02 | Same source tree, `stock_account`/`account` Stock Closing + Accrued Orders wizard modules (exact file+line in `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md` `D-06`) | **Source-code-tier**, same provenance as `EV-PCO-SRC-01` | `GAP-PCO-02` corroborating evidence — manual/cron trigger modes, Stock Closing vs. Accrued Orders/WIP distinction |

## Note on evidence convergence

EV-PCO-02 is the same URL as Gx2's EV-SDV-04 (`.../accounting/get_started/inventory_valuation.html`). The Gx6 search surfaced a more complete synthesis of that same page's content than the Gx2 search did — this is a real instance of "researching the same evidence source twice can still yield Material Delta" (fuller synthesis, not new content) — recorded per Master Prompt discipline, not treated as circular.

| EV-PCO-SRC-03 | `TEAM_A/04_EVIDENCE_PACKS/SOURCE_MAP_CANDIDATE/MODULE_account.md` §3 (`company.py`, `account_move.py`, `account_move_line.py`, `account_lock_exception.py`) | **Source-code-tier, S2-CANDIDATE** — a per-module structural/trace record from the worker's broader 300-module source-map pass, retrieved 2026-09-30, incorporated here by this session (never read directly by it) | `GAP-PCO-01` independent re-verification: resolves the two-path ambiguity (silent date-shift on post vs. `UserError` on editing a posted entry), TEST-confirms Hard Lock's absoluteness, and surfaces 3 new findings (parent-company lock-chain evaluation, a `bypass_lock_check` context flag of untraced reachability, and Community's permissive review-lock behavior) |

## Evidence-tier disclosure (source/dump round, 2026-09-30)

`EV-PCO-SRC-01`/`02` are source-code-tier — strictly higher confidence than V1/V2 for what they directly evidence, but this session did not read the source itself (relayed via a separate local session's own Clean-Room-scoped work, consolidated in `STATE03_SOURCE_DUMP_EVIDENCE_DELTA_HANDOFF.md`) and the DB-schema cross-check found the actual test/pilot database extends beyond vanilla Community (~696 non-Community tables) — these findings describe Community-core-plus-two-reviewed-overlay-modules behavior, not necessarily the full behavior of any live/customized deployment. `CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET` applies.
