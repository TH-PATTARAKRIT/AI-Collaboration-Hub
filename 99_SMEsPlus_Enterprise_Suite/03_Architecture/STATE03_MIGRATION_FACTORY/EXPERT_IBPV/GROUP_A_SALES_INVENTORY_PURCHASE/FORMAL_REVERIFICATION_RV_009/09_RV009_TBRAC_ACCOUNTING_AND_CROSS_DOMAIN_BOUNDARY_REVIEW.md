> GROUP A — Sales + Inventory + Purchase Integrated Backbone | Formal IBPV Re-Verification (RV-009)

# 09 — TBRAC / ACCOUNTING BOUNDARY / RESIDUAL ITEM REVIEW

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D09`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009`
Reviewed package: TEAM B CORR-008 corrective closure, commit `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`
Baseline (pre-correction): `b98a3b9fb435845dbd15fae79db63b0b73a82420`
Control Level: `/L999.999`
Boss: Sole Final Approver
Independence note: this deliverable is an independent Phase-9 review of three items **not** among CORR-008's
nine claimed closures — TEAM B did not purport to fix any of them. This document determines their current status
after CORR-008, on this session's own re-derivation of the evidence, not by checking a closure claim that was
never made.

## 0 — Scope and Method

Verified directly against the repository, not against any prior team's summary:

- Full changed-file diff, `b98a3b9f...` → `359f96c0...`, scoped to
  `TEAM_B_DESIGN/GROUP_A_SALES_INVENTORY_PURCHASE/`: **20 files changed** (1443 insertions, 66 deletions) — 13
  pre-existing numbered files (`03`, `04`, `05`, `07`, `08`, `09`, `10`, `12`, `13`, `14`, `18`, `19`, `20`) plus 7
  new CORR-008 evidence artifacts (`22`–`28`). This matches the "13-file changed-file list" referenced in scope.
- `git diff --stat b98a3b9f... 359f96c0... -- .../15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` →
  **empty output — file 15 was NOT touched by CORR-008.** Independently confirmed.
- `git diff --stat b98a3b9f... 359f96c0... -- .../16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md` → **empty
  output — file 16 was NOT touched by CORR-008.** Independently confirmed.
- Full text re-read of file 15 (unchanged), file 07 §07 (unchanged), file 13 (changed sections only), file 10, file
  12, file 14, file 18, files 22 and 23 (CORR-008 evidence), and the FV-006 source findings (`14`, `15` in the
  FV-006 extract) and the Boss Evidence Gate approval §4.1.
- `grep -in` sweep of all 13 changed files for `vendor bill|AR/AP|posted invoice|cancellation gate|locked invoice`
  and separately for `thai|SME businesses|SME expect|Thailand`, to catch any incidental re-statement that might
  drift outside the TBRAC evidence-tier discipline or the Accounting boundary.

---

## 1 — TBRAC Discipline Check (post-CORR-008)

**Status: `VERIFIED`.**

- File 16 (`16_THAILAND_USER_REALITY_VALIDATION_REGISTER.md`) is confirmed byte-for-byte unchanged by CORR-008
  (empty `git diff --stat`). The evidence-tier discipline FV-006 D11 verified (`FV006-TH-001`–`004`, all
  `VERIFIED`) is therefore preserved by construction — there is nothing new in file 16 to re-check.
- The grep sweep of all 13 changed files found every Thailand/Thai reference either (a) restating the existing,
  unchanged non-conflation of Thai Tax-Branch (a Party attribute) with the Tenant/Company/Branch structural layer
  (`04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §06, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` line 121,
  `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` line 51 — all pre-existing statements, not new claims), or (b)
  explicitly labeled `N/A` / "no Thailand-specific evidence" (`13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`
  lines 46, 83, 109), or (c) explicitly cross-referenced to file 16's own `CONTROLLED ASSUMPTION / REQUIRES
  FUTURE VERIFICATION` classification rather than asserted as fact (`14` §07, §08 row 8; `18` §01 item 4, item
  6; `18` §02 Medium #19; `CORRECTIVE_CORR_008/23` §4 row 8, §5). **No new unguarded Thailand-wide generalization
  was introduced.**
- SaaS/Tenant reconciliation (`CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md`) was
  spot-checked specifically for a Domain-01 (Accounting Core) import: §3's source table explicitly enumerates
  `COA_G01_SAAS_INVARIANT_COMPLIANCE.md` and the AQ SaaS Context Clarification, and explicitly excludes from
  import into GROUP A: Platform Context / Standard Template administration (AQ §3 items 1, 4, 5), Template
  versioning (`SI-03/04/06/07`), and the Thai-Tax-Branch-adjacent Domain-01 finding `SI-10`/"Finding S5" — stated
  twice, in the source table's own "Scope applicable to GROUP A" column and again in the "Evidence-boundary rule"
  paragraph immediately below it. Only the cross-module Tenant/Company-context invariant (AQ §3 items 2–3,
  `SI-01`/`SI-02`) is imported, and file 23 states this is a project-wide control GROUP A applies, not one it
  newly invents. **No COA-template/versioning/tax-branch-specific Domain-01 rule was found imported into GROUP
  A.**
- Owner: none — this is a clean bill, not an open item. Blocks Team C: **N**.

---

## 2 — Item 1: Sales/Purchase Cancellation-Gate Accounting Dependency (Fit-Gap #12 / `FV006-GAP-015`)

**Current status: unchanged from FV-006 — `CONFLICT FOUND`, still requiring a Boss policy decision with
Accounting-domain input. Not touched, not closed, not incidentally altered by CORR-008.**

### 2.1 — File 15 confirmed untouched

`git diff --stat` for `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` between the two commits returns
no output. Full re-read confirms file 15 §00 still states, verbatim: "AR/AP internal posting logic ... [is]
Accounting Core's own domain and [is] not designed, redesigned, or second-guessed here," and §08 restates "AR/AP
internal posting logic" in its Explicit Non-Design List. This is the exact boundary statement FV-006 D09
(`FV006-ACC-003`, Critical) found Fit-Gap #12's justification crosses.

### 2.2 — File 07 §07 (the cancellation gate itself) confirmed untouched in substance

CORR-008 touched file 07 only at §01 (new `Rejected`-state block, CORR8-01) and §03 (the `HOLD`/"numbered, not
enforced-sequence" wording note, CORR8-04) — both cited explicitly in the CORR-008 Finding Closure Register
(`CORRECTIVE_CORR_008/22` CORR8-01, CORR8-04). §07 ("Cancellation") carries no CORR-008 marker anywhere and
reproduces the identical reasoning FV-006 reviewed: "an outstanding vendor bill represents real financial
exposure that an outstanding customer invoice ... does not symmetrically create at cancellation time," disposed
as `ADAPT both as-is`. The identical restatement appears, also untouched, in
`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 ("Gate asymmetry disposition"). A repo-wide grep for
`vendor bill` across all 13 CORR-008-changed files returns exactly these two (identical, unmodified) instances —
no new occurrence, no rewording.

### 2.3 — Checked for incidental interaction from the new CORR-008 mechanics — none found

- **New `Rejected` state (CORR8-01):** occurs only on the `Pending Approval → Rejected` transition, which is
  strictly pre-`Committed` in Purchase's lifecycle (`07` §01). The cancellation gate under review governs
  cancellation of an already-`Committed` Supply Commitment against an open vendor bill — a bill cannot yet exist
  against a commitment that was never committed. No structural overlap.
- **New `Handoff Unresolved`/`Handoff Resolved` status (CORR8-03):** per `10` §02, the two Financial-Handoff-facing
  rows ("Fulfillment quantity → billing eligibility" and "Financial posting → re-derived invoiced quantity") are
  both explicitly marked **"Out of CORR-008 scope — the Financial Handoff boundary's own failure semantics are
  Accounting Core's domain, per [15]."** CORR-008 itself declined to extend its handoff-failure closure into the
  Accounting boundary — direct confirmation that the boundary GROUP A cannot cross was respected, not
  incidentally eroded.
- No other CORR-008 finding (idempotency, event-transport semantics, Traceability/Handling Unit ownership,
  Shared-Master archival, SaaS/Tenant reconciliation) references vendor-bill state, AR/AP lifecycle, or the
  cancellation gate at all.

### 2.4 — Conclusion

Item 1 is exactly where FV-006 left it: TEAM B's own accounting-interface boundary (file 15, unchanged) still
places AR/AP internal vendor-bill-lifecycle state outside GROUP A's authority, and Purchase's stricter
cancellation gate (file 07 §07 / file 12 §07, unchanged) still depends on that fact to justify the asymmetry
against Sales. This is not a new defect CORR-008 introduced or failed to fix — it was never one of CORR-008's
nine claimed findings, and nothing in the nine closures touches it, directly or by side effect.

- **Current status:** `CONFLICT FOUND` (carried forward unchanged from FV-006 D14 §3.3 / D13 `FV006-GAP-015`).
- **Owner:** Boss (business-policy decision: symmetric gate vs. accepted disclosed asymmetry), **with mandatory
  input from whoever independently owns the Accounting Core / AR-AP domain**, since the underlying fact (posted
  vendor bill vs. posted customer invoice) is outside GROUP A's authority to resolve unilaterally. GROUP A/TEAM B
  must not invent AR/AP internal state to close this itself — none has been invented; this is confirmed, not
  merely asserted.
- **Blocks Team C now:** **N** for the rest of GROUP A (both sides' gates are independently implementable as
  designed); **Y**, narrowly, for finalizing the Sales-side cancellation-gate symmetry decision specifically —
  identical scope to FV-006's original blocking statement, unchanged.
- **What exactly closes it:** a Boss ruling (with Accounting-domain input) on FV-006 D15 §3 item 2's two options —
  either require a Sales-side gate symmetric to Purchase's, or formally accept the asymmetry as a disclosed
  business-risk trade-off. Until Boss rules, the item remains open exactly as FV-006 scoped it.

---

## 3 — Item 2: Missing Legacy Approval Internal Workflow/Permission Evidence

**Current status: unchanged, pre-existing carry-forward — `EVIDENCE MISSING` for the internal enforcement/gating
logic only. CORR8-04 and CORR8-05's separation from this carry-forward holds under independent re-reading.**

### 3.1 — The carry-forward itself

Boss Evidence Gate Approval (`GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md` §4 item 1) records the three
legacy modules (`sale_order_level_approve`, `purchase_request_level_approve_po`, `purchase_request_level_approve`)
as a controlled carry-forward: "Team B must not invent their internal workflow semantics." File 13 §00
(unchanged in substance by CORR-008 — CORR-008 touched §02, §03, §05, §06, not §00) restates this identically:
"TEAM B does **not** infer exact internal workflow from field names or row values," listing the same unresolved
items (exact approval-button behavior, exact transitions, exact permission model, exact SoD behavior).

### 3.2 — Verifying CORR8-04 and CORR8-05 did not overstate legacy internals

Both corrections were re-read in full against `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`:

- **CORR8-04 (`FV006-SOD-004`, wording only):** the new §03 reading-note blockquote states explicitly that
  "sequential"/"ordered" name only "the numbering/labeling convention," that neither term "asserts that
  level-to-level **gating** is enforced in strict order," and that "whether gating is actually enforced in
  sequence remains `HOLD / EVIDENCE REQUIRED FOR THIS DECISION POINT`." The Summary Table (§06) keeps two
  separate rows — "generic shape" (`HOLD? No`) vs. "internal workflow / level-to-level gating logic"
  (`HOLD? **Yes**`) — unchanged in substance, only split for clarity. No claim about actual legacy gating
  behavior was added.
- **CORR8-05 (`FV006-SOD-001`, new identity-based control):** the new §02 row is explicit that "TEAM B does not
  claim this was how any legacy module's internal logic behaved (that internal logic remains outside evidence,
  per §00); this is a target business-control requirement stated independently of the unverified legacy
  internals." This is a new TEAM B-owned target requirement layered on top of the evidenced role-based gate
  (`04` §02 PO-06/07/08), not a claim about what the legacy modules actually enforced.

### 3.3 — Checked file 07 for the same discipline

File 07 §01/§03 (the CORR8-01/CORR8-04 corrected sections) both explicitly re-state the `HOLD` and attribute
resubmission-restart-level uncertainty to "the Approval Control's own internal transition logic, which remains
`HOLD`" — consistent, no overstatement found.

### 3.4 — Verifying the block is scoped correctly, not broadened or narrowed

File 13 §00's HOLD list and file 18 §01 item 1 (unchanged) both still scope the block to internal
enforcement/gating logic specifically — data shape (levels, approver assignment, approve/reject event, rejection
reason) is independently designed and unaffected. CORR-008's two additions live entirely on the data/target-
requirement side of that line (a wording precision and a new, explicitly-labeled target control), never on the
internal-logic side. The separation CORR8-04/CORR8-05 claim to preserve does hold under this independent
re-reading.

### 3.5 — Conclusion

- **Current status:** `EVIDENCE MISSING` (pre-existing, unchanged) for the internal enforcement/gating/permission
  logic of the three named legacy modules only. The surrounding data shape, plus the two CORR-008 additions
  (numbering-only wording precision; identity-based self-approval exclusion as a new target requirement), are
  independently verified as correctly scoped and not overstating what is known about the legacy internals.
- **Owner:** Boss/PMO, for source acquisition or an explicit "final target design, no further acquisition" ruling
  (Boss Gate §4.1 item 1; FV-006 D15 §3 item 3) — unchanged scope. Not TEAM B's to close by design reasoning
  alone.
- **Blocks Team C now:** **N** for the vendor-neutral data shape and the two new CORR-008 controls (both may
  proceed); **Y**, narrowly, for implementing the level-to-level gating/enforcement logic itself.
- **What exactly closes it:** Boss commissions source acquisition/reverse-engineering for the three named modules
  (option a), or Boss formally accepts the vendor-neutral shape as final target design and closes the
  legacy-fidelity question without further acquisition (option b) — FV-006 D15 §3 item 3, unchanged by CORR-008.

---

## 4 — Item 3: Three Deferred Policy Defaults

**Current status: all three reconfirmed safe to defer. No CORR-008 mechanic (new `Rejected` state, `Handoff
Unresolved` status, or SaaS/Tenant reconciliation) shortens any of the three windows; the relative urgency
ordering FV-006 set is unchanged.**

Source of the three items and their FV-006 disposition: `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §03
(`N1`, `N2`, `N3`) and FV-006 `15_PRE_DEVELOPMENT_GATE_RECOMMENDATION_TO_BOSS.md` §3 item 4. None of `N1`/`N2`/`N3`
carries a CORR-008 marker; their register rows are byte-identical in substance to the pre-correction package.

### 4.1 — Canonical Invoiced Quantity definition (`N1`)

- Owning artifacts: `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` (not in the 13-file CORR-008 changed list —
  confirmed unchanged) and file 15 (confirmed unchanged, §2). The only Financial-Handoff-adjacent CORR-008 touch
  (`10` §02, Handoff-failure-detection column) explicitly marks the "Financial posting → re-derived invoiced
  quantity" row **"Out of CORR-008 scope."**
- No interaction found with `Rejected` (pre-`Committed`, never billed) or `Handoff Unresolved` (a fulfillment-
  request-creation signal, not a billing/quantity signal).
- **Reconfirmed: safe to defer**, timing unchanged from FV-006 D15 §3 item 4 ("before the specific
  computation/flow ... is considered feature-complete").

### 4.2 — Over-Fulfillment/Over-Billing default (`N2`)

- Owning artifacts: `12` §02/§03 (Over-Fulfillment Policy, Over-Billing Policy) — both sections carry no
  CORR-008 marker; the only CORR-008 addition in file 12 near them is the unrelated, distinctly-numbered §11
  idempotency paragraph (CORR8-02) and new §13A (CORR8-03).
- Checked directly for the interaction named in scope (denied-approval wind-down / Handoff-Unresolved coupling
  with over-fulfillment): the `Rejected` wind-down path never reaches a Received/Delivered quantity, because
  Purchase's approval gate resolves strictly before `Committed`, and Received stays at zero until a Movement
  Execution occurs after `Committed` (`10` §03 reminder 2, unchanged). `Handoff Unresolved`/`Resolved` governs
  whether a Movement Instruction gets created at all, not whether a created one over-executes — over-fulfillment
  is a quantity-mismatch question that arises only once execution actually occurs, downstream of where
  Handoff-Unresolved operates. If anything, the new idempotency invariant (CORR8-02, `12` §11) *reduces* one
  concrete over-fulfillment vector (duplicate Movement Execution from a retried trigger), making the deferred
  default marginally **less**, not more, exposed than at FV-006.
- **Reconfirmed: safe to defer**, and CORR-008 does not shorten the window; the FV-006 timing note (before the
  computation/flow is feature-complete) still applies unchanged.

### 4.3 — Sales Confirmation Gate default (`N3`)

- Owning artifact: `13` §04 (APR-003) — carries **no** CORR-008 marker; the CORR-008 corrections in file 13 are
  confined to §02, §03, §05, §06. Re-read in full: still "TEAM B does not fix a default," still `Carry-Forward:
  Yes`, still cross-referenced to file 17 as requiring Boss/business input.
- Checked directly for the interaction named in scope: the Sales Confirmation Gate operates at commitment
  **confirm time** (credit exposure / inventory-availability pre-check, before a Movement Instruction is even
  requested); `Handoff Unresolved` operates strictly **after** a successful confirm, on the Sales→Inventory
  handoff itself (`10` §02 row 1). These are sequential, non-overlapping control points — a confirm that clears
  the gate can still later surface `Handoff Unresolved`, but that new visibility is a mitigation (an observable
  failure signal that did not exist at FV-006 time), not a new exposure. No coupling was found that would shorten
  the safe-to-defer window; if anything the new observability is a mild net positive for deferring the exact
  default value a little longer, since fulfillment-side visibility is now stronger than at FV-006.
- **Reconfirmed: safe to defer, and FV-006's own relative ranking is unchanged — this remains the item with "the
  shortest fuse" of the three**, per FV-006 D15 §3 item 4's own language, restated (not superseded) by this
  review: recommended to be resolved before the Sales-side confirm/credit/overselling flow is considered
  feature-complete, still ahead of the other two on urgency, still not a blocker for Development to start
  broadly.

### 4.4 — Summary

| Item | Reconfirmed status | Owning artifact(s), confirmed unchanged | Coupling to new CORR-008 mechanics found? |
|---|---|---|---|
| `N1` Invoiced Quantity definition | Safe to defer, unchanged | `11` (untouched), `15` §02/§05 (untouched) | None — Financial Handoff explicitly out of CORR-008 scope |
| `N2` Over-Fulfillment/Over-Billing default | Safe to defer, unchanged (marginally reinforced) | `12` §02/§03 (untouched sections) | None found; idempotency addition (`12` §11) mitigates one vector |
| `N3` Sales Confirmation Gate default | Safe to defer, unchanged — still shortest fuse of the three | `13` §04 (untouched) | None found; `Handoff Unresolved` adds downstream visibility, does not shorten the window |

- **Owner (all three):** Boss/business policy (FV-006 D15 §3 item 4, unchanged).
- **Blocks Team C now:** **N** for all three — none is itself a control-integrity or evidentiary gap; Development
  may proceed broadly per FV-006's original disposition, unchanged by this review.
- **What exactly closes each:** Boss/business sets the specific default value (or explicitly rules "no default")
  for each of the three, before the respective computation/flow each feeds is considered feature-complete — same
  action item FV-006 named, still open, still not urgent enough to block Team C from starting.

---

## 5 — Consolidated Table

| # | Item | Current status | Owner | Blocks Team C now? |
|---|---|---|---|---|
| — | TBRAC discipline check | `VERIFIED` | — | N |
| 1 | Sales/Purchase cancellation-gate Accounting dependency (Fit-Gap #12) | `CONFLICT FOUND` (unchanged) | Boss + Accounting-domain input | Y (narrow — Sales-gate-symmetry decision only) |
| 2 | Legacy approval internal workflow/permission evidence | `EVIDENCE MISSING` (pre-existing, unchanged) | Boss/PMO | Y (narrow — internal gating-logic implementation only) |
| 3 | Three deferred policy defaults (Invoiced Qty / Over-Fulfillment / Sales Confirmation Gate) | Reconfirmed safe to defer, unchanged | Boss/business | N |

## 6 — What This Review Is Not

- Not a Boss decision, not a Team C authorization, not a Formal IBPV PASS for CORR-008 as a whole (that
  conclusion belongs to this session's own consolidated verification report, not to this Phase-9-scoped
  deliverable).
- Does not waive Item 1 or Item 2 — both remain on HOLD for their narrow scope until their named owner acts.
- Does not retroactively re-open any of CORR-008's nine claimed closures — none of those nine findings is
  restated, re-scored, or re-opened here; this deliverable's independent conclusion is limited to the three items
  named in its own scope, plus the TBRAC discipline check.

`Independent experts verify the design; only Boss decides whether the lifecycle may advance.`
