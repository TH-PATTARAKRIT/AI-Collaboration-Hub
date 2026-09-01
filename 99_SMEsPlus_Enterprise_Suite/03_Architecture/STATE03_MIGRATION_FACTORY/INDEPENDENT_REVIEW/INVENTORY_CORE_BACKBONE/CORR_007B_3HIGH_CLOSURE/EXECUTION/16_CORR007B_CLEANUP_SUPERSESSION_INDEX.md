# CORR-007B — Documentation Cleanup & Supersession Index

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001` (documentation cleanup pass)
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd`
Timestamp: 2026-09-02
Scope: **Documentation cleanup only.** No evidence conclusion, disposition, or gap status is changed by
this file. No file is deleted. This file exists solely to resolve a file-numbering collision between two
concurrent sessions and to make each document's role in the package unambiguous.

## 1. Why this file exists

Two concurrent Claude Code sessions, sharing one git working directory, both produced work in response to
Boss's addendum-5 request ("9 Veto Challenge Council" / "9 Special Team Challenge" / clean-room review /
revised disposition). One session (this one) had already used file numbers `10` and `11` for earlier,
distinct addendum-4 deliverables. The other session used `10`, `11`, `12`, `13` for its addendum-5
deliverables, unaware of the collision. Boss directed that the pushed session's addendum-5 files be kept
as-is and authoritative, and that this session's colliding addendum-4 files be renumbered — not deleted —
with explicit cross-references, since inspection showed the two sets of files serve **different roles**:
the pushed session's files are a **governance charter** (who challenges what, and a scope ruling); this
session's files are the **technical evidence** (source/dump citations proving or disproving specific
mechanisms). Neither makes the other redundant.

## 2. Renumbering map

| Original number/name | New number/name | Reason | Content changed? |
|---|---|---|---|
| `10_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md` | `14_CORR007B_AI_EXPERT_PANEL_CHALLENGE_REPORT.md` | Collided with the pushed session's `10_CORR007B_9_VETO_CHALLENGE_COUNCIL_REPORT.md` | No — renamed only; internal self-references updated to the new number |
| `11_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` | `15_CORR007B_N_A12_01_ADDENDUM4_EVIDENCE_DISPOSITION.md` | Collided with the pushed session's `11_CORR007B_9_SPECIAL_TEAM_CHALLENGE_REPORT.md`, and shared an identical title with the pushed session's `13_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` | No — renamed and retitled ("Addendum-4 Evidence Disposition" vs. the original "Revised Functional Design Disposition (Consolidated)") to disambiguate from file 13; a scope-clarifying note was added at the top; every finding (G-1 through G-7) is unchanged |
| `10_CORR007B_9_VETO_CHALLENGE_COUNCIL_REPORT.md` | *(unchanged)* | Pushed session's file — kept exactly as authored | No |
| `11_CORR007B_9_SPECIAL_TEAM_CHALLENGE_REPORT.md` | *(unchanged)* | Pushed session's file — kept exactly as authored | No |
| `12_CORR007B_CLEAN_ROOM_COMPLIANCE_REVIEW.md` | *(unchanged)* | Pushed session's file — kept exactly as authored | No |
| `13_CORR007B_N_A12_01_REVISED_FUNCTIONAL_DESIGN_DISPOSITION.md` | *(unchanged)* | Pushed session's file — kept exactly as authored; this is the standing governance-level disposition | No |

No file was deleted. Every file that existed before this cleanup still exists, either at its original
path (files 01-09, 12, 13) or at a new path with a forwarding note at the old path's would-be location
(handled by this index rather than a stub file, per the git history itself preserving the rename).

## 3. Charter vs. evidence — what each file actually is

| File | Type | What it contains |
|---|---|---|
| `10` (VETO) | Governance charter | Defines the 9 Veto Challenge Council's composition, authority boundary, and mandatory duties. Reopens `N-A12-01` procedurally. Contains no source/dump citations. |
| `11` (SPECIAL TEAM) | Governance charter | Defines the 9 Special Team Challenge's mandate and lists what must be proven for `N-A12-01` (§4.1-4.4). Contains no source/dump citations — it specifies requirements, not findings. |
| `12` (CLEAN ROOM) | Governance charter | Restates the four clean-room principles and lists challenge questions. Does not check specific citations in files 01-09/14/15 against those principles. |
| `13` (DISPOSITION) | Governance disposition | Marks `N-A12-01` sub-items A/B as `SOURCE MECHANISM PROVEN` and C-I as `NOT PROVEN` (§4), and lists "Required Next Deliverables" (§7). **This is the standing governance-level disposition for `N-A12-01`, per Boss's direction.** |
| `08`, `09`, `14`, `15` (this session) | Technical evidence | Source-line citations (file, line number), dump/schema CSV citations, SHA-256 hashes, and explicit resolved/open determinations for the same topics files 10-13 scope. |

**Both are needed and neither supersedes the other's role.** The governance files establish *what must be
challenged and who is accountable*; the evidence files establish *what the reference system's source and
dump actually show*. File 13 §4's `NOT PROVEN` marks are a **governance judgment that a functional-design
decision has not yet been made** (correct — no Team B design exists anywhere in this package, by design,
since Team B is not authorized). They are not a finding that no *evidence* exists — in most cases,
substantial evidence already does, cited below.

## 4. Cross-reference: file 13 §4 sub-items → where the evidence actually is

| File 13 sub-item | File 13's status | What the cited evidence file actually shows |
|---|---|---|
| `N-A12-01-A` — lock-date mechanism | `SOURCE MECHANISM PROVEN` | Confirmed independently in `08_...FUNCTIONAL_DESIGN_PROOF.md` §4, §21 (`stock_picking._check_backdate_allowed`, full body) |
| `N-A12-01-B` — accounting_date propagation | `SOURCE MECHANISM PROVEN` | Confirmed in `08_...md` §7 (`accounting_date` → `force_period_date` → posted move date chain) |
| `N-A12-01-C` — monthly close functional workflow | `NOT PROVEN` | **Evidence exists**: `08_...md` §2 (Mermaid workflow diagram), §7 (`action_close_stock_valuation` full mechanism, cron trigger, journal posting), §17-18 (Periodic vs. Perpetual posting-time difference). This is a full functional workflow, sourced and hashed. It does not constitute a SMEsPlus *design* (correctly not claimed as one) — it is the reference-system evidence a design would be built from. |
| `N-A12-01-D` — month-12 year-end close to retained earnings | `NOT PROVEN` | **Evidence exists, and is itself the finding**: `08_...md` §22 documents an exhaustive source search (`find` across the full tree for fiscal-year-closing wizards/actions) that found **no** month-12-specific code path and **no** posted P&L-to-Retained-Earnings entry — Odoo computes `equity_unaffected` as a live report rollup instead (`account_reports/models/account_report.py`, cited with line numbers). This is a proven *absence*, which is exactly the kind of finding that should change "NOT PROVEN" (implying nobody looked) to "proven absent, with two named design options for Team B" (file 08 §22 states both). |
| `N-A12-01-E` — inventory valuation to GL reconciliation | `NOT PROVEN` | **Evidence exists**: `08_...md` §7 cites `stock_account/report/stock_valuation_report.py` in full — the `stock_account.stock.valuation.report` model computes Initial Balance (GL-posted) vs. Ending Stock (physical) vs. Inventory Loss vs. Stock Variation for any date. This *is* the reconciliation mechanism. |
| `N-A12-01-F` — opening balance / carry-forward | `NOT PROVEN` | **Evidence exists**: `08_...md` §8, §19 cite `_get_last_closing_date()`/`_save_closing_id()` in full — the running-ledger mechanism by which each closing's boundary becomes the next closing's starting point. |
| `N-A12-01-G` — Periodic vs Perpetual / Manual vs Automated | `NOT PROVEN` | **Evidence exists, extensively**: `08_...md` §15-21 (the entire Boss-addendum-2 response) and `09_...PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md` §3-5 (reconciling "Manual"/"Automated" screenshot terminology against the actual `periodic`/`real_time` field and its help text). |
| `N-A12-01-H` — Product Category valuation policy | `NOT PROVEN` | **Evidence exists**: `09_...md` §1 (class-verified: `property_valuation`/`property_cost_method` are declared inside `class ProductCategory`, not `ProductTemplate`), §2 (precedence: category overrides company default), §7 (full account-field matrix, including the finding that classic "Stock Input"/"Stock Output" category fields are **not** declared in this source snapshot — a genuine correction to the screenshot's assumed field set), §9 (functional design matrix by category setting). |
| `N-A12-01-I` — clean-room SMEsPlus target close design | `NOT PROVEN` | **Correctly not proven — no correction needed.** No file in this package proposes a SMEsPlus target design; Team B is not authorized. This is the one sub-item where "NOT PROVEN" accurately reflects that the task is a future design decision, not a missed evidence-gathering step. `14_...md` (the four-lens challenge) independently reinforces this in its Functional Design lens (§1): the mechanism is proven and testable, but the *decision* is explicitly left to Team B. |

**Reading this table correctly**: it does not argue that `N-A12-01` should be closed, reclassified, or
counted differently than file 13 states. File 13's overall disposition (`N-A12-01 = REOPENED HIGH
FUNCTIONAL DESIGN GAP`, `Account + Inventory Backbone Reference Baseline = HOLD`) is **unchanged and
correct** — a substantial evidence base does not equal a completed, Boss-accepted, original SMEsPlus
functional design. What this table corrects is narrower: several `NOT PROVEN` labels in file 13 §4
describe *evidence-gathering* status, and for those specific rows (C, D, E, F, G, H), the evidence has, in
fact, already been gathered and cited — it is the *design decision built on that evidence* that remains
undone, exactly as file 13 §5 ("Required Functional Design Proof") and its list of clean-room-original
design deliverables (§7) correctly demand.

## 5. File 13 §7 "Required Next Deliverables" — status against what already exists

| File 13's requested deliverable | Status |
|---|---|
| `N_A12_01_MONTHLY_CLOSE_FUNCTIONAL_WORKFLOW.md` | Substantially covered by `08_...md` §2 (diagram), §7, §11 (event matrix) — not a separately-named file, but the content exists |
| `N_A12_01_PRODUCT_CATEGORY_VALUATION_POLICY_MATRIX.md` | Covered by `09_...md` §7, §9 (matrix table) |
| `N_A12_01_PERIODIC_PERPETUAL_BEHAVIOR_PROOF.md` | Covered by `08_...md` §15-21 |
| `N_A12_01_YEAR_END_RETAINED_EARNINGS_PROOF.md` | Covered as a proof-of-absence by `08_...md` §22 |
| `N_A12_01_ACCOUNT_INVENTORY_GL_RECONCILIATION_PROOF.md` | Covered by `08_...md` §7 (`stock_valuation_report.py`) |
| `N_A12_01_CLEAN_ROOM_TARGET_CLOSE_CONTRACT.md` | **Not covered, and correctly so** — this is a SMEsPlus original design artifact, which requires Team B authorization this package does not grant. |

Recommendation for a future round (not actioned here — this is a documentation-cleanup file, not a new
evidence round): rather than commissioning six new files, a future session could produce a short index
confirming which of files 08/09/14/15 already satisfies each requested filename's *evidence* content,
and scope any genuinely new work to the one item that is not covered — the clean-room target close
contract itself, which requires Team B authorization first.

## 6. Final status (unchanged by this cleanup)

- `N-A12-01` = **HIGH FUNCTIONAL DESIGN GAP** (per file 13, the standing governance disposition) — not
  closed, not reclassified, not counted as resolved anywhere in this package.
- `Account + Inventory Backbone Reference Baseline` = **HOLD** (per file 13 §6) — not published, not
  implied ready.
- `GRPA-M15` and `N-A7-01` dispositions (files 01, 02, 04, 05) are unaffected by this cleanup or by
  addendum 5 — neither was in scope for the governance challenge.
- **CORR-007B remains OPEN for Boss Challenge.** No Gate PASS is declared. Team B is not authorized.
  Team C is not authorized. Boss remains the sole Final Approver.

This cleanup changed file names, one file title, and added cross-reference notes. It did not change any
evidentiary finding, any G-1 through G-7 gap status, any disposition label, or any blocker count.
