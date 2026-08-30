# DOMAIN_01 Accounting Core — PMO Post-Boss Decision Register

Date: 2026-08-30

## Purpose

This register updates the **active PMO decision status after Boss Final Gate evidence**.

The historical PMO verification file is preserved as a pre-decision evidence artifact and is not rewritten to pretend PMO made the Boss decision. This register supersedes its recommendation-only fields for current reporting.

Authority rule:

`PMO Recommendation ≠ Approval`

`Boss Decision + Evidence = Active Approved Status`

## Evidence Baseline

- ChatGPT Independent Re-Audit Round 8: `c380e4862cb3437ccd100c5196ca0cd52789b630`
- PMO pre-decision verification: `50276a71c6c8c5b7cd82de8e15a87bc3d4add993`
- Boss Final Gate Decision Pack: `5c394fdd2479b0dda6da6405f8b6369854dfd3d2`
- Boss Thailand COA ruling: `27dd58f42bb63e6f2ed7f3389813490356e16ccc`
- Odoo18 tab source inventory: `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`
- Boss Final Gate Ruling: `62164aadd085d6af2587b7622388337182199bda`

## Active PMO Decision Register

| ID | Topic | Former PMO Position | Boss Evidence / Ruling | Active PMO Status | Gate Impact |
|---|---|---|---|---|---|
| A1 | Rounding Policy | Recommend Option B | Boss approved Option B in Final Gate ruling `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss policy decision |
| A2 | Ordinary Period Reopen | Recommend Option A | Boss approved Option A in `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss policy decision |
| A3 | COA Template / Instance | Recommend Option A with carry-forward | Boss approved Thailand COA direction `27dd58f...`; prerequisite extraction completed `ae2b0719...`; Boss Final Gate confirms A3 | **BOSS APPROVED — PRECONDITION EVIDENCED** | COA direction closed; row-level canonical mapping continues before exact COA freeze |
| A4 | Audit Tamper-Evidence Scope | Recommend Option A | Boss approved Option A in `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss policy decision |
| A5 | Correction Shape Flexibility | Recommend Option A | Boss approved Option A in `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss policy decision |
| A6 | CO-02 / CO-06 Coupling | Recommend Option A | Boss approved Option A in `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss control decision |
| A7 | Fiscal-Year Membership Restatement Tier | Recommend Option A | Boss approved Option A in `62164aad...` | **BOSS APPROVED — EVIDENCE RECORDED** | Closed as Boss authorization-control decision |

## PMO Current Gate Statement

```text
Gate Result: PASS
Blocking Design Findings: 0 in the accepted independent-review chain
Boss Policy Decisions A1-A7: APPROVED / EVIDENCE RECORDED
Non-Blocking Carry-Forward: YES
Next Controlled Work: COA row-level canonicalization + residual-unknown reconciliation
Development Authorization: NOT GRANTED
Production Authorization: NOT GRANTED
```

PMO shall no longer report A1-A7 as merely `PMO Recommendation` or `HOLD FOR BOSS DECISION` in current status summaries. The current status must be reported as **Boss Approved**, with the evidence commit/link.

## COA Item-1 Evidence Status

Boss required completion of extraction item 1 before A3 became effective.

Verified result:

- `Odoo18` tab/business table inventory completed.
- Data rows: 389 (`0–388`).
- Business columns: `id`, `name`, `reconcile`, `code`, `account_type`.
- Evidence commit: `ae2b0719081ef9497f08e3b3e1ea8329d053cf83`.

Therefore:

`A3 PRECONDITION = SATISFIED`

`A3 ACTIVE PMO STATUS = BOSS APPROVED — EVIDENCE RECORDED`

## Remaining PMO Controls

The following remain open and must not be falsely closed:

1. Row-level SMEsPlus canonical COA mapping is not yet frozen.
2. Exact final Account Type canonical IDs/rules are not yet frozen.
3. Team A residual-unknown count requires reconciliation against individually enumerated IDs.
4. STEP linkage remains `TBD / BASELINE LINKAGE REQUIRED` until project governance binds it.
5. Official Project / STATE / STEP percentages remain `TBD / BASELINE REQUIRED` absent approved weighting.
6. Jira ownership/due-date red flags remain administrative follow-up until independently corrected.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
