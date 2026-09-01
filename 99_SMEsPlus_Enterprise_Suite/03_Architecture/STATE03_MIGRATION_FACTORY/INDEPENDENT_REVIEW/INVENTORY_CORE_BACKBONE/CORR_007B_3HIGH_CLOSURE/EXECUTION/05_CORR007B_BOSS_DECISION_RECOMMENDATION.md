# CORR-007B — Boss Decision Recommendation

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02

## 1. Repository / branch / commit

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Branch: `audit/inventory-core-corr007b-3high-closure-010`
- Base commit: `deceb7339b39eba309236782f159f8393224f5fd` (CORR-007A final commit,
  `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`)
- GitHub links to deliverables: see §4 (populated after this branch is pushed — see the pending-push
  note in `07_CORR007B_SESSION_CLOSURE.md`).

## 2. GRPA-M18 / WHT exclusion confirmation

`GRPA-M18` (Thai WHT / 50-twi certificate) is **not** in scope for this package and was not touched,
re-analyzed, or re-dispositioned here. Its CORR-007A recommendation (remove from the Inventory Evidence
Gate High list; track as `GRPA-M18-D` Accounting/Tax filing carry-forward + `GRPA-M18-E` legal-review
item) remains exactly as CORR-007A left it, pending Boss's own separate decision on that package. This
was independently re-verified by Team I4 (`04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md` §5).

## 3. Result per item

### `GRPA-M15` — purchase-order-line source-to-dump drift

**RESOLVED**, with one controlled carry-forward. All 9 dump-observed columns now have a source
disposition; 8 are directly source-cited (re-verified against primary source this session), and the
9th (`purchase_request_id`) is classified as a legacy orphan column on FK + module-family + relation-
table-successor evidence, carried forward only for a data-content check before it can be safely dropped
from the schema. Full proof: `01_CORR007B_GRPA_M15_PURCHASE_ORDER_LINE_DRIFT_PROOF.md`.

### `N-A7-01` — inventory count freeze / conflict behavior

**RESOLVED AS SOURCE BEHAVIOR; DESIGN POLICY REQUIRED.** Odoo's reference behavior is definitively
soft conflict detection at apply-time (`is_outdated` → `stock.inventory.conflict` wizard), with no hard
freeze of any kind during an active count — confirmed by full method-body re-read, not only field-name
matching. What remains is a SMEsPlus product-design decision among four named options; that decision is
explicitly not made by this report. Full proof: `02_CORR007B_N_A7_01_COUNT_FREEZE_CONFLICT_PROOF.md`.

### `N-A12-01` — fiscal-year / cross-year inventory continuity — **REOPENED BY BOSS, HIGH REMAINS**

The original disposition (`CONTROLLED ACCOUNTING X INVENTORY CROSS-PROOF CARRY-FORWARD`, from
`03_CORR007B_N_A12_01_CROSS_YEAR_CONTINUITY_PROOF.md`) was rejected by Boss in two addenda as
insufficient for Functional Design: a lock-date citation does not prove the end-to-end Accounting-led
period-close workflow, and it does not by itself determine whether Periodic or Perpetual valuation
governs how inventory value, COGS, and GL postings actually behave. Both challenges are answered in
`08_CORR007B_N_A12_01_ACCOUNT_LED_INVENTORY_PERIOD_CLOSE_FUNCTIONAL_DESIGN_PROOF.md`, which proves,
from primary source in the `stock_account` bridge module (`depends: ['stock', 'account']`):

- the exact per-move GL-posting gate (`_should_create_account_move()`, keyed on
  `product_id.valuation == 'real_time'`) that separates Perpetual (posts every move immediately) from
  Periodic (defers all GL impact to closing);
- where the valuation method is configured (company default, product-category override — not a
  per-product or separate "accounting policy" field, none of which was found in source);
- the full closing mechanism (`action_close_stock_valuation`, daily cron, three-part value-gap
  aggregation, journal posting, and a running-ledger "carry-forward" boundary recorded via
  `ir.config_parameter` rather than a posted opening entry);
- the account structure (Stock Valuation, Price Difference, Stock Variation, location-level interim
  equivalents) for both methods;
- and, on year-end specifically: **no source evidence of an explicit P&L-to-Retained-Earnings closing
  journal entry** — Odoo's reference design computes current-year earnings as a live report rollup
  (`equity_unaffected` account type) rather than posting a year-end closing entry. This is reported as a
  genuine divergence from Boss's general-accounting-theory framing, found by evidence rather than
  assumed away.

Six named functional-design gaps result (G-1 through G-6, file 08 §10 and §23). Per Boss's explicit
instruction, none of this additional depth counts as closing the item.

Boss raised two further addenda: whether Product Category (not company) truly owns costing/valuation
policy, and a request for a 4-role independent AI expert panel. On the latter, this session flagged
directly that the work is produced by one model, not four independent parties, and Boss selected an
honest four-analytical-lens framing instead (recorded in
`10_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md` §0). Both addenda are answered in
`09_CORR007B_PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md` and
`10_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md`, which resolved one gap (G-4, the manual-trigger UI
path) and named one new gap (G-7, empty PDF/XLSX export stubs in the reference module). The consolidated
current position is `11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md`.

**`N-A12-01` remains High**, reclassified as: **ACCOUNT-LED MONTHLY CLOSE, YEAR-END CLOSE, STOCK
CUT-OFF, INVENTORY VALUATION METHOD, PERIODIC/PERPETUAL POSTING BEHAVIOR, CARRY-FORWARD BALANCE, AND
RETAINED EARNINGS FUNCTIONAL DESIGN GAP.** Current position of record:
`11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` (consolidates files 03/08/09/10, all
retained on the branch for audit-trail continuity, none individually current on their own).

## 4. GitHub links

Populate after push (see `07_CORR007B_SESSION_CLOSURE.md` for push status):

- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/01_CORR007B_GRPA_M15_PURCHASE_ORDER_LINE_DRIFT_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/02_CORR007B_N_A7_01_COUNT_FREEZE_CONFLICT_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/03_CORR007B_N_A12_01_CROSS_YEAR_CONTINUITY_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/08_CORR007B_N_A12_01_ACCOUNT_LED_INVENTORY_PERIOD_CLOSE_FUNCTIONAL_DESIGN_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/09_CORR007B_PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/10_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/06_CORR007B_SHA256_MANIFEST.txt`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/07_CORR007B_SESSION_CLOSURE.md`

## 5. Inventory High blocker count — before and after

| | Count | Items |
|---|---|---|
| Before CORR-007B | 3 | `GRPA-M15`, `N-A7-01`, `N-A12-01` |
| After CORR-007B, following Boss's `N-A12-01` reopening | **1** | `N-A12-01` — ACCOUNT-LED MONTHLY CLOSE, YEAR-END CLOSE, STOCK CUT-OFF, INVENTORY VALUATION METHOD, PERIODIC/PERPETUAL POSTING BEHAVIOR, CARRY-FORWARD BALANCE, AND RETAINED EARNINGS FUNCTIONAL DESIGN GAP — HIGH REMAINS |
| Total open tracked items (all, including sub-gaps) | 8 | see §6 |

`N-A12-01` is explicitly **not** counted as closed anywhere in this package, per Boss's instruction.
`GRPA-M15` and `N-A7-01` are unaffected by the reopening.

## 6. Controlled carry-forward / open item list

| Item | Type | Owner | Target gate | Stop condition |
|---|---|---|---|---|
| `purchase_request_id` data-content check | Migration data profiling | Team A / Migration | Migration Data Profiling phase | If populated rows are found, return to Inventory/Purchase design review before dropping the column. |
| Count-freeze design-policy selection (A/B/C/D) | Inventory design decision | Team B (not authorized to start from this task) | Inventory Design Freeze | Team B must not finalize count/adjustment UX without selecting and recording one option. |
| G-1 — no proven Accounting-lock-date-vs-Inventory-closing sequencing | Inventory design decision | Team B | Inventory Design Freeze | Do not assume order is guaranteed; must be explicitly designed. |
| G-2 — asymmetric post-close correction governance | Inventory design decision | Team B | Inventory Design Freeze | `stock_account.skip_lock_date_check` must not remain the only Inventory-side override before go-live. |
| G-3 — backdate enforcement at `stock.picking`, not per-line | Inventory design decision | Team B | Inventory Design Freeze | Confirm document-level granularity is acceptable for SMEsPlus multi-line transfers. |
| G-5 — migration-cutover opening-balance cross-proof | Cross-domain evidence | Team A + Accounting/Tax jointly | Future joint Accounting x Inventory cross-proof session | No migration cutover across a fiscal-year boundary until this cross-proof exists. |
| G-6 — no source-evidenced year-end P&L-to-Retained-Earnings closing entry; confirmed no Thai-localization module fills this gap either | New functional design decision (not inherited from Odoo reference) | Team B jointly with Accounting/Tax (Thai statutory requirement) | Inventory Design Freeze + Accounting close-book design | If Thai statutory close-book requires an explicit entry, SMEsPlus must design one — it cannot be assumed present. |
| G-7 — `stock_valuation_report.py` PDF/XLSX export methods are empty stubs (source-verified, `10_...md` §4) | Code defect, not a design decision | Team A / follow-up code review | Before this report screen is relied on for a printable audit artifact | Do not assume Print PDF/XLSX buttons work; verify or implement before UAT. |

(G-4 — manual closing-trigger UI path — was open in `08_...md` but was resolved in `10_...md` §4 by
reading `controller.js` in full; it is not carried forward as an open item.)

## 7. Gate impact

This package does not declare the Inventory Evidence Gate PASS. Following Boss's `N-A12-01` reopening,
the Inventory Evidence Gate's *pure Inventory-owned* High blocker count is **1**, not 0. The Gate remains
further subject to: (a) Boss's still-pending CORR-007A decision on `GRPA-M18`, (b) the 14 Medium / 7 Low
items already logged in `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` and reconfirmed by IDR-007
(unchanged by this package — out of scope here), and (c) the eight open items in §6, none of which are
Inventory Evidence Gate blockers by definition (except `N-A12-01` itself, which is) but all of which must
be resolved before Team B/Team C work in their respective areas can be considered complete. **No Account
+ Inventory Backbone Reference Baseline may be published listing `N-A12-01` as closed.**

## 8. Team authorization status

- **Team B authorized: NO.** Not authorized by this task or this package. Requires Boss's explicit
  approval after reviewing this evidence, per task governance.
- **Team C authorized: NO.** Not authorized by this task or this package.

## 9. Boss decision options

**A. ACCEPT CLOSURE/DISPOSITION OF `GRPA-M15` AND `N-A7-01`** — accept `GRPA-M15` as RESOLVED and
`N-A7-01` as RESOLVED AS SOURCE BEHAVIOR (design policy still required), individually or together.
`N-A12-01` is not offered for closure under this option — it remains High per Boss's own reopening.

**B. ACCEPT THE 8-ITEM CARRY-FORWARD/OPEN LIST** — accept the items in §6 (including the six named
`N-A12-01` sub-gaps G-1..G-6) as the correct forward-tracking mechanism, with the named owners, gates,
and stop conditions, while `N-A12-01` itself continues to be counted as an open Inventory High item.

**C. KEEP INVENTORY GATE HOLD** — decline some or all of the `GRPA-M15`/`N-A7-01` dispositions above and
keep additional items counted as Inventory High blockers pending further evidence. (`N-A12-01` is already
held High regardless of this option, per Boss's reopening.)

**D. REQUEST FRESH INDEPENDENT RE-REVIEW** — commission a further independent pass (e.g. an IDR-style
session, as was done for CORR-005) before accepting this package's dispositions.

## 10. Final status

**CORR-007B COMPLETE — READY FOR BOSS INVENTORY 3-HIGH DECISION**

This is not a Gate PASS declaration. This is not Team B or Team C authorization. Boss remains the sole
Final Approver of every disposition in this package.
