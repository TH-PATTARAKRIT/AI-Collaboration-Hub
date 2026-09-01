# CORR-007B — N-A12-01 Revised Functional Design Disposition (Consolidated)

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02

This file is the single current-state summary of `N-A12-01` after four rounds of Boss challenge. It
supersedes `03_CORR007B_N_A12_01_CROSS_YEAR_CONTINUITY_PROOF.md` as the item's position of record; files
`03`, `08`, `09`, `10` remain on the branch for audit-trail continuity and are not to be read as
individually current without this file's consolidation.

## 1. Evolution of this item within CORR-007B

| Round | Trigger | Evidence produced | Resulting status |
|---|---|---|---|
| Original | Task brief | `03_...CROSS_YEAR_CONTINUITY_PROOF.md` | `CONTROLLED ACCOUNTING X INVENTORY CROSS-PROOF CARRY-FORWARD` |
| Addendum 1 | Boss: lock-date citation insufficient, need end-to-end workflow proof | `08_...FUNCTIONAL_DESIGN_PROOF.md` §1-14 | Reopened — `HIGH REMAINS`, mechanism proven, gaps G-1..G-5 named |
| Addendum 2 | Boss: Periodic vs Perpetual not yet determined | `08_...FUNCTIONAL_DESIGN_PROOF.md` §15-24 | `HIGH REMAINS`, gap G-6 added |
| Addendum 3 | Boss: Product Category ownership + screenshot terminology | `09_...PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md` | `HIGH REMAINS`, category ownership confirmed, Stock Input/Output legacy-terminology finding added |
| Addendum 4 | Boss: 4-lens challenge (reframed from literal "independent panel" after this session raised the provenance concern; Boss selected honest-lens framing) | `10_...AI_EXPERT_PANEL_CHALLENGE_REPORT.md` | `HIGH REMAINS`, G-4 resolved, G-7 added |

## 2. Final gap register (as of this file)

| Gap | Description | Status | Owner | Target gate |
|---|---|---|---|---|
| G-1 | No proven sequencing between Accounting lock-date setting and Inventory valuation closing | Open | Team B | Inventory Design Freeze |
| G-2 | Asymmetric post-close correction governance (`account.lock_exception` vs. global `skip_lock_date_check`) | Open | Team B | Inventory Design Freeze |
| G-3 | Backdate enforcement at `stock.picking` level, not per `stock.move` line | Open | Team B | Inventory Design Freeze |
| G-4 | Manual closing-trigger UI path not source-verified | **Resolved** (file 10 §4 — `controller.js` read in full; confirmed date-selectable, `auto_post=False` by default) | — | Closed |
| G-5 | Migration-cutover opening-balance cross-proof against Accounting's own evidence | Open | Team A + Accounting/Tax jointly | Future joint Accounting x Inventory cross-proof session |
| G-6 | No source-evidenced year-end P&L-to-Retained-Earnings closing entry; Thai statutory close-book need not covered by any existing integration (file 10 §3 confirms no `l10n_th_*` module touches `stock`/`stock_account`) | Open | Team B + Accounting/Tax | Inventory Design Freeze + Accounting close-book design |
| G-7 | `stock_valuation_report.py` PDF/XLSX export methods are empty stubs | Open | Team A / Code review follow-up | Before this report screen is relied on for a printable audit artifact |

**Net open count: 6** (G-1, G-2, G-3, G-5, G-6, G-7). One resolved (G-4) since the original reopening.

## 3. What is now proven beyond reasonable challenge (source + dump, both cited throughout files 08-10)

- The full Periodic/Perpetual mechanism, including the exact per-move posting gate.
- Product Category as the config owner, with company-level fallback, and the precedence order between
  them.
- The complete account structure actually present in this source baseline (Stock Valuation, Stock
  Variation, Price Difference, location-level interim accounts) vs. the classic category-level Input/
  Output accounts Boss's screenshot referenced, which are not declared in this source snapshot.
- The closing/reconciliation/carry-forward mechanism, cron-driven and manually-triggerable, with the
  manual path now fully verified.
- The absence of any Thai-localization dependency on this mechanism.
- The absence of any month-12-specific or explicit P&L-to-Retained-Earnings closing entry in the
  reference system.

## 4. What remains genuinely unproven, and cannot be proven by more re-reading of this same source

- G-5: whether SMEsPlus's actual migration cutover will correctly establish and reconcile an opening
  position. This requires Accounting's own migration evidence, not more Inventory-side source reading.
- G-6, functional-design half: whether SMEsPlus needs an explicit year-end closing entry for Thai
  statutory compliance, and if so, its design. This is a new requirement decision, not something further
  source archaeology in this Odoo reference snapshot can resolve, because the reference snapshot does not
  implement it.
- G-1/G-2/G-3: these are SMEsPlus product-design choices about sequencing, correction governance, and
  enforcement granularity. Odoo's reference behavior does not mandate an answer; Team B must choose one.

## 5. Disposition

**`N-A12-01` = ACCOUNT-LED MONTHLY CLOSE, YEAR-END CLOSE, STOCK CUT-OFF, INVENTORY VALUATION METHOD,
PERIODIC/PERPETUAL POSTING BEHAVIOR, CARRY-FORWARD BALANCE, AND RETAINED EARNINGS FUNCTIONAL DESIGN GAP
— HIGH REMAINS.**

This is not functionally closed. Further Inventory-only evidence sessions against this same source
baseline are unlikely to move G-1/G-2/G-3/G-6 (functional-design half) or G-7 further — they are design
decisions and a code defect, not missing citations. G-5 and G-6 (statutory half) require Accounting/Tax
evidence this session cannot produce. **No Account + Inventory Backbone Reference Baseline may be
published listing `N-A12-01` as closed.** Recommendation to Boss: treat `N-A12-01` as ready for a design
decision (Team B, once authorized) and a joint Accounting cross-proof, not for a further Inventory-only
evidence round.

See `04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md` and `05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`
(both updated) for how this feeds the overall CORR-007B blocker count and Boss decision options.
