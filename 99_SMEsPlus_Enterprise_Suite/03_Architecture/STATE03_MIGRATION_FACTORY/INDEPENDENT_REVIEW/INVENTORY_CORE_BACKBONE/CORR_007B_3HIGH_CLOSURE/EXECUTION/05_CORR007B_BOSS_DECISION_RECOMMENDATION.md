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

### `N-A12-01` — fiscal-year / cross-year inventory continuity

**CONTROLLED ACCOUNTING X INVENTORY CROSS-PROOF CARRY-FORWARD.** Inventory's own mechanisms (accounting-
date propagation, hard lock-date enforcement on completed pickings, fiscal-year-aware valuation-over-
period math) are fully proven and independently re-verified against primary source. The
`fiscalyear_lock_date`/`hard_lock_date` fields and the `_get_lock_date_violations()` method they depend
on are owned by the `account` module (Accounting domain), not by Inventory. What remains — proof that a
real SMEsPlus cutover correctly carries opening quantities/values across a fiscal-year boundary — is a
joint Accounting x Inventory deliverable this session cannot close alone. Full proof:
`03_CORR007B_N_A12_01_CROSS_YEAR_CONTINUITY_PROOF.md`.

## 4. GitHub links

Populate after push (see `07_CORR007B_SESSION_CLOSURE.md` for push status):

- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/01_CORR007B_GRPA_M15_PURCHASE_ORDER_LINE_DRIFT_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/02_CORR007B_N_A7_01_COUNT_FREEZE_CONFLICT_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/03_CORR007B_N_A12_01_CROSS_YEAR_CONTINUITY_PROOF.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/06_CORR007B_SHA256_MANIFEST.txt`
- `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/blob/audit/inventory-core-corr007b-3high-closure-010/99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/INDEPENDENT_REVIEW/INVENTORY_CORE_BACKBONE/CORR_007B_3HIGH_CLOSURE/EXECUTION/07_CORR007B_SESSION_CLOSURE.md`

## 5. Inventory High blocker count — before and after

| | Count | Items |
|---|---|---|
| Before CORR-007B | 3 | `GRPA-M15`, `N-A7-01`, `N-A12-01` |
| After CORR-007B (pure Inventory-owned High blockers, if Boss accepts) | 0 | — |
| Total open items still requiring work (recategorized, not eliminated) | 3 | data-content check (`GRPA-M15`); design-policy selection (`N-A7-01`); joint cross-proof (`N-A12-01`) |

Per Team I4's audit (`04_CORR007B_FINAL_HIGH_DISPOSITION_REGISTER.md` §7), both rows must be presented
together. "0" describes evidence completeness for the Inventory domain; it does not describe 3 real
open items disappearing.

## 6. Controlled carry-forward list

| Item | Type | Owner | Target gate | Stop condition |
|---|---|---|---|---|
| `purchase_request_id` data-content check | Migration data profiling | Team A / Migration | Migration Data Profiling phase | If populated rows are found, return to Inventory/Purchase design review before dropping the column. |
| Count-freeze design-policy selection (A/B/C/D) | Inventory design decision | Team B (not authorized to start from this task) | Inventory Design Freeze | Team B must not finalize count/adjustment UX without selecting and recording one option. |
| Accounting x Inventory fiscal-year cross-proof | Cross-domain evidence | Team A + Accounting/Tax jointly | Future joint cross-proof session | No migration cutover across a fiscal-year boundary until this cross-proof exists. |

## 7. Gate impact

This package does not declare the Inventory Evidence Gate PASS. If Boss accepts all three dispositions,
the Inventory Evidence Gate's *pure Inventory-owned* High blocker count goes to 0, but the Gate remains
subject to: (a) Boss's still-pending CORR-007A decision on `GRPA-M18`, (b) the 14 Medium / 7 Low items
already logged in `A14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md` and reconfirmed by IDR-007 (unchanged
by this package — out of scope here), and (c) the three carry-forward items in §6, none of which are
Inventory Evidence Gate blockers by definition but all of which must be resolved before Team B/Team C
work in their respective areas can be considered complete.

## 8. Team authorization status

- **Team B authorized: NO.** Not authorized by this task or this package. Requires Boss's explicit
  approval after reviewing this evidence, per task governance.
- **Team C authorized: NO.** Not authorized by this task or this package.

## 9. Boss decision options

**A. ACCEPT CLOSURE OF SOME/ALL ITEMS** — accept `GRPA-M15` as RESOLVED, `N-A7-01` as RESOLVED AS
SOURCE BEHAVIOR (design policy still required), and/or `N-A12-01` as reclassified to controlled
carry-forward, individually or together.

**B. ACCEPT CONTROLLED CARRY-FORWARD** — accept the three items in §6 as the correct forward-tracking
mechanism, with the named owners, gates, and stop conditions.

**C. KEEP INVENTORY GATE HOLD** — decline some or all of the reclassifications above and keep one or
more of `GRPA-M15` / `N-A7-01` / `N-A12-01` counted as Inventory High blockers pending further evidence.

**D. REQUEST FRESH INDEPENDENT RE-REVIEW** — commission a further independent pass (e.g. an IDR-style
session, as was done for CORR-005) before accepting this package's dispositions.

## 10. Final status

**CORR-007B COMPLETE — READY FOR BOSS INVENTORY 3-HIGH DECISION**

This is not a Gate PASS declaration. This is not Team B or Team C authorization. Boss remains the sole
Final Approver of every disposition in this package.
