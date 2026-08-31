> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY against Team A evidence | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Independent Evidence Review Scope and Baseline

# 01 — INDEPENDENT REVIEW SCOPE AND BASELINE

## 00 — Reviewer identity and independence statement

This review was performed by a separate agent session, not Team A, not Team B, not IBPV/IDTM/IESA formal
verification. It re-performed material checks against primary evidence (actual Odoo source files and the actual
`iTEST02` PostgreSQL dump) rather than trusting Team A's closure narrative. Team A's evidence branch was treated
as read-only throughout; no Team A file was edited by this review.

## 01 — Baseline verification

| Item | Claimed | Independently confirmed |
|---|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` | Confirmed — `origin` remote matches exactly |
| Team A evidence branch | `claude/group-a-sales-inventory-purchase-dr002` | Confirmed to exist on `origin` (only became visible after `git fetch --prune`; the branch was pushed very close to this review's start) |
| Frozen Team A review commit | `8b0993d824cf726fa52edd687272ff54b0977c42` | Confirmed to exist, is the tip of the dr002 branch, and is a `research(group-a): corrective closure CORR-003...` commit dated 2026-08-31 08:44:28 +07 |
| Canonical baseline at prompt creation | `7241c6e0195040a611d42a2597d8a48e103bff00` | Confirmed to exist and to be an ancestor of `origin/SMEsPlus` |
| Canonical `SMEsPlus` HEAD at review start | (not fixed by the governing prompt — "current canonical branch") | `origin/SMEsPlus` had already advanced past the prompt-creation baseline by the time this review began (`00e0b7a3...`, the commit that added this review's own governing prompt file), and advanced again mid-review to `a4cebfc1...` (an unrelated Accounting-Core clean-room reconciliation commit from a concurrent session). The audit branch was cut from the latest fetched `origin/SMEsPlus` at branch-creation time, per governing-prompt §6 ("create a separate review branch from the current canonical `SMEsPlus` branch") |
| Team A Corrective Session ID | `SMEPLUS-26-08-31-MIG-A-GRPA-SIP-CORR-003` | Confirmed — matches the frozen commit's message and `19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md`'s own session banner |
| Governance file set (§7 of the governing prompt) | 6 governance files, 2 prior-session prompts, 13 evidence files (02/04/05/06/07/08/13/14/16/17/18/19/20) | All 21 files confirmed present at the frozen commit / canonical HEAD; none missing |

## 02 — Independence / branch control compliance

- Team A's branch and frozen commit were only ever read via `git show <commit>:<path>` (or, for the DB claims,
  via an independently-restored scratch copy of the source dump) — never checked out into a working tree that
  could be edited.
- No file under `TEAM_A/06_DOMAIN_RESEARCH/GROUP_01_SALES_INVENTORY_PURCHASE/` was modified by this review.
- This review's own artifacts were written only under
  `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/CHATGPT_AUDIT/GROUP_A_SALES_INVENTORY_PURCHASE/`.
- The audit branch `audit/group-a-sip-evidence-review-004` did not exist before this session; it was created fresh
  from `origin/SMEsPlus` — no branch-control conflict.
- No merge into `SMEsPlus` was performed or requested.

## 03 — Primary evidence available for independent re-performance

Beyond Team A's own written evidence chain, this review confirmed the following primary sources are present on
the local volume and used them directly (not merely cited from Team A's report):

| Source | Path | Used for |
|---|---|---|
| Odoo-19 source tree | `ACCOUNT/01 ACCOUNT/SOURCE CODE/02 OTHER/` | Cluster A/B re-performance — direct reads of `purchase_order.py`, `stock_move.py`, `stock_picking.py`, `stock_rule.py` |
| `iTEST02` full dump | `ACCOUNT/01 ACCOUNT/iTEST02_2026-06-14_14-41-19.dump` (65,444,053 bytes) | Cluster C re-performance — independently restored into a fresh, disposable local PostgreSQL instance and queried directly |
| GROUP A evidence chain (frozen) | exported from commit `8b0993d8...` into a local scratch directory, 22 files | All clusters |
| Governance / DR-002 / CORR-003 governing prompts | `origin/SMEsPlus` working tree | Section-citation accuracy checks (§5, §6, §12, §13, §15, §17, §19, §21, §22 all independently confirmed to exist with matching titles in `00_NEW_SESSION_PROMPT_SMEPLUS-26-08-30-MIG-A-GRPA-SIP-DR-002.md`) |

## 04 — Scope executed vs governing prompt

All five review clusters (§8–§12 of the governing prompt) were executed:

| Cluster | Deliverable | Status |
|---|---|---|
| A — R7 Purchase cancellation re-performance | `02_GROUP_A_R7_R8_REPERFORMANCE_MATRIX.md` | Complete |
| B — R8 Procurement→Purchase re-performance | `02_GROUP_A_R7_R8_REPERFORMANCE_MATRIX.md` | Complete |
| C — R6 Approval evidence boundary | `03_GROUP_A_APPROVAL_EVIDENCE_BOUNDARY_REVIEW.md` | Complete — includes a full independent DB restore and re-query, not a document review only |
| D — Fit-Gap neutrality / TBRAC | `04_GROUP_A_FIT_GAP_NEUTRALITY_TBRAC_REVIEW.md` | Complete |
| E — Gate package / hash / remaining-gap consistency | `05_GROUP_A_GATE_PACKAGE_AND_HASH_RECONCILIATION.md`, `06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md` | Complete |

## 05 — Out of scope (not performed, per governing prompt §4/§15)

- No Team A file was edited.
- No Team B target design was created or implied.
- No Formal IBPV/IDTM/IESA verification was performed.
- No merge, release, or production action was taken.
- No new broad Thailand research programme was launched (TBRAC review was a classification check of existing
  register entries only, per §3.2 of the governing prompt).
