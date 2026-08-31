> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 09 — ACCOUNTING HOLD AND CONTROLLED-RESIDUAL BOUNDARY RE-VERIFICATION (RV11-07)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D09`

## 00 — What Was Checked

`CORRECTIVE_CORR_010/34_CORR010_ACCOUNTING_HOLD_AND_RESIDUAL_DEPENDENCY_MATRIX.md` was read as a claim under
test, then independently checked against `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` (full),
`07_PURCHASE_CANONICAL_DESIGN.md` §07 (the cancellation-gate asymmetry), and the RV-009 baseline (Deliverable 11
§A) for whether CORR-010 answered any question it was not authorized to answer.

## 01 — A1 — Sales-Side Cancellation-Gate Symmetry

**Required status**: `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`.

Independently confirmed: `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` (full document) and
`07`§07 (the dual-gate-vs-single-gate asymmetry) are **byte-for-byte unchanged** by CORR-010 — confirmed via
`git diff b2f7cbd3... e4418644... -- .../15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` and the same
for `07` (no hunk in either file's diff touches §07 or any part of file 15). CORR-010's file 34 poses three
questions to Accounting (what Customer-Invoice/AR lifecycle state should carry equivalent blocking weight; does a
posted invoice constitute financial exposure; what "posted/locked/reconciled/reversed" precisely means) without
answering any of them, and explicitly states what it does not invent: "the AR/customer-invoice internal
lifecycle... any posted/locked/reconciled semantics; which specific Accounting fact, if any, should hard-block
Sales-side cancellation." Independently confirmed no such semantics appear anywhere in files 15 or 07§07 as they
stand today.

**Verdict: `VERIFIED` — HOLD correctly preserved, no AR/AP fact invented.**

## 02 — A2 — Legacy Approval Internal Workflow Evidence

**Required status**: `EVIDENCE MISSING / BOSS DECISION REQUIRED`.

Independently confirmed: `13`§00 and §03's `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT` marking is
unchanged (Deliverable 08 above). CORR-010's only edit in this area is `13`§02's Event Impact cross-reference,
which names an *outcome event* the already-designed state model produces, not the internal trigger/permission
logic itself — independently confirmed this does not touch the `HOLD`.

**Verdict: `VERIFIED` — status correctly preserved.**

## 03 — A3 — Three Deferred Policy Defaults

**Required status**: `SAFE TO DEFER` (reconfirmed).

The three defaults (canonical Invoiced Quantity definition — `06`§02, `11`§04, `18` N1; Over-Fulfillment/
Over-Billing default — `07`§02, `12`§02/§03, `18` N2; Sales Confirmation Gate default — `13`§04, `18` N3) were
independently checked against every file CORR-010 touched (`04`, `05`, `06`, `07`, `08`, `09`, `10`, `12`, `13`,
`18`, `19`). None of CORR-010's edits — the ordering/atomicity closures, the B1–B8 precision fixes — touches the
computations or gates these three defaults feed. **Independently confirmed: no new evidence surfaced by CORR-010
shortens any of the three safe-to-defer windows.**

**Verdict: `VERIFIED` — reconfirmed unchanged.**

## 04 — C4 — TEAM A Evidence Branch-Lineage Gap

**Required status**: `EVIDENCE MISSING (in-lineage)`, PMO-actionable.

Independently confirmed unchanged: CORR-010 performed no write against TEAM A evidence files or branch history
(Deliverable 02 §04–05 above, scope-clean corrective delta). This item's disposition is unaffected by CORR-010 —
it remains exactly where RV-009 (D11 item C4) left it.

**Verdict: `VERIFIED` — reconfirmed unchanged, correctly not TEAM-B-actionable.**

## 05 — New Residual Discovered by CORR-010 Itself

CORR-010's file 34 discloses the governance-baseline hash discrepancy and missing Five-Unit record as a new
residual, carried forward for Boss/PMO reconciliation. Independently superseded by Deliverable 03 above — the
discrepancy is resolved to `GOVERNANCE EVIDENCE EXISTS — CROSS-BRANCH TRACEABILITY / LINEAGE VISIBILITY ISSUE`,
not left as an open unknown. No other new Accounting-, legacy-approval-, or policy-default-adjacent gap was
independently found in any file CORR-010 touched.

## 06 — No-Silent-Waiver Check

Every item above was independently checked against its RV-009 baseline status, not merely against CORR-010's own
"unchanged" claim. Each is confirmed genuinely unchanged, more precisely scoped where CORR-010 says so (A1's
questions, C4's required PMO action), and none is resolved, waived, or narrowed without evidence.

## 07 — Verdict

**`VERIFIED`.** CORR-010 answers zero Accounting-owned questions, invents zero AR/AP lifecycle facts, and leaves
A1, A2, A3, and C4 exactly where independent re-reading of the untouched primary files confirms they were left by
RV-009 — narrower in stated scope for A1 (now itemized as three explicit questions) but not narrower in actual
authority. The Accounting HOLD boundary is held.
