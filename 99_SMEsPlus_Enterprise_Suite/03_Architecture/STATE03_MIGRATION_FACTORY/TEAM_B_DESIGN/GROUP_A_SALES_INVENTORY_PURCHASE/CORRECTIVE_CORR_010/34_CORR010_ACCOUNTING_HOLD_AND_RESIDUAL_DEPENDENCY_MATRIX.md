> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B Corrective Rework (CORR-010)

# 34 — CORR-010 ACCOUNTING HOLD AND RESIDUAL DEPENDENCY MATRIX

Session: `SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010`

This is the single canonical residual matrix for every item this session is explicitly not authorized to close,
per the governing prompt §3.2 and §7. No item below is answered on Accounting's, PMO's, or Boss's behalf — each
states only the minimum interface question GROUP A needs answered, without answering it.

## A1 — Sales-Side Cancellation-Gate Symmetry (Accounting/AR-AP Dependency)

**Current control status: `HOLD — WAITING FOR ACCOUNTING/AR-AP AUTHORITY`.**

- **What TEAM B already designed, unchanged by this session**: `07`§07 records Purchase's dual cancellation gate
  (locked OR an open vendor bill) as a legitimate, preservable business asymmetry against Sales' single gate
  (locked only), reasoning that an outstanding vendor bill represents real financial exposure a merely-drafted
  customer invoice does not symmetrically create at cancellation time.
- **What GROUP A needs from Accounting — as questions, not answers**:
  1. What is the Customer Invoice/AR lifecycle state (draft, posted, partially paid, fully paid) that should be
     treated as equivalent in blocking weight to Purchase's "open vendor bill" gate, if any?
  2. Does an Accounting-posted (not merely drafted) Customer Invoice against a Sales commitment line constitute a
     financial exposure Accounting considers should block that commitment's cancellation — symmetric to how a
     posted vendor bill blocks Purchase's?
  3. What does "posted," "locked," "reconciled," or "reversed" mean, precisely, for a Customer Invoice in
     Accounting's own model — and which of those states, if any, should be the exact fact GROUP A's Sales
     cancellation gate checks?
- **What GROUP A does not invent**: the AR/customer-invoice internal lifecycle; the AP/vendor-bill internal
  lifecycle beyond what `07`§07 already cites from evidence; any posted/locked/reconciled semantics; which
  specific Accounting fact, if any, should hard-block Sales-side cancellation.
- **Boss decision required**: (a) require a symmetric Sales-side gate once Accounting supplies the answers above,
  or (b) accept the current asymmetry as a disclosed risk trade-off. Not decided by this session.
- **Scope note**: this is a narrow HOLD — it blocks only the Sales-side cancellation-gate design, not any other
  GROUP A work.

## A2 — Legacy Approval Internal Workflow/Permission Evidence

**Current control status: `EVIDENCE MISSING / BOSS DECISION REQUIRED`.**

- **What TEAM B already designed, unchanged by this session**: the vendor-neutral shape of both approval
  mechanisms (`13`§02/§03) — configurable threshold/role gate; N numbered approval levels with approve/reject
  events, timestamps, and mandatory rejection reasons.
- **What remains unverified and is not designed here** (`13`§00, unchanged): exact approval-button behavior;
  exact Level 1 → Level 2 transition; exact reject transition; exact permission model; exact SoD enforcement
  mechanism; exact trigger for the undocumented intermediate state observed in historical data; exact cancel/reset
  interaction with an in-progress approval.
- **This session's B1/B5 edits do not touch this HOLD**: the B1 cross-reference added to `13`§02 only names the
  `Supply Commitment Rejected` *event* that the (unverified-internals) approval action produces once a decision is
  reached — it does not infer, assume, or design the internal decision-triggering logic itself.
- **Boss/PMO decision required**: (a) commission source-code acquisition/reverse-engineering/interview effort for
  the three named modules (`sale_order_level_approve`, `purchase_request_level_approve_po`,
  `purchase_request_level_approve`), or (b) formally accept the vendor-neutral shape as final target design and
  proceed without the internal logic ever being independently verified.

## A3 — Three Deferred Policy Defaults

**Current control status: `SAFE TO DEFER` (reconfirmed, unchanged by this session).**

1. Canonical Invoiced Quantity definition (any-non-cancelled vs. posted-only) — `06`§02, `11`§04, file 18 N1.
2. Over-Fulfillment/Over-Billing default (block/warn/allow) — `07`§02, `12`§02/§03, file 18 N2.
3. Sales Confirmation Gate default (credit exposure/inventory availability) — `13`§04, file 18 N3.

No new evidence surfaced during this session's authorized non-Accounting work materially shortens any of these
three defaults' safe-to-defer window. This session does not choose any of the three policy values — each remains
a Boss/business decision, to be set before the specific computation/flow each feeds is considered feature-complete.
The Sales Confirmation Gate default (item 3) retains the shortest fuse of the three, per prior IBPV assessment,
unchanged.

## C4 — TEAM A Evidence Branch-Lineage Gap (PMO Action, Not TEAM B)

**Current control status: `EVIDENCE MISSING (in-lineage)` — PMO-actionable.**

- **What Formal IBPV RV-009 independently found** (Deliverable 11 C4, Deliverable 12): the TEAM A source files
  cited by CORR8-02, CORR8-05, and CORR8-08 (`13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`,
  `01_SHARED_MASTER_DEPENDENCY_MAP.md`) are absent from the commit ancestry this session's branch and CORR-008
  were built on; they exist only on an unmerged sibling branch (`origin/claude/group-a-sales-inventory-purchase-dr002`).
  Content recovered read-only from that branch substantiates all three citations verbatim — RV-009 independently
  confirmed this is a repository-integration gap, not an evidence-fabrication risk.
- **What TEAM B does not do**: modify TEAM A evidence, fake or rewrite branch ancestry, or merge branches. This
  session performed no write of any kind against TEAM A evidence files or branch history.
- **Required PMO action**: merge the relevant TEAM A evidence files into the canonical lineage feeding
  `GROUP_A_SALES_INVENTORY_PURCHASE`'s design work, so future citations resolve within the audited ancestry
  without requiring cross-branch archaeology.

## Any New Residual Discovered This Session

- **Governance-baseline hash discrepancy** (governing prompt header field `36820bf574272fc1d818da178584fd4cec04826b`)
  and the missing Five-Unit readiness record — both documented in
  [29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md](29_CORR010_PREFLIGHT_AND_FINDING_REPRODUCTION.md) §02.
  Neither gates this session's authorized design work; both are carried forward for Boss/PMO reconciliation.
- No other new residual dependency was discovered while closing CORR10-01/02/03 and B1–B8; all edits made were
  scoped exactly to the authorized items and did not surface a new Accounting-, legacy-approval-, or
  policy-default-adjacent gap.

## No Silent Waiver

Every item above remains exactly as open as Formal IBPV RV-009 left it, or more precisely scoped (A1's exact
interface questions are now itemized above; C4's required PMO action is now stated explicitly). Nothing above is
resolved, waived, or silently narrowed by this session.
