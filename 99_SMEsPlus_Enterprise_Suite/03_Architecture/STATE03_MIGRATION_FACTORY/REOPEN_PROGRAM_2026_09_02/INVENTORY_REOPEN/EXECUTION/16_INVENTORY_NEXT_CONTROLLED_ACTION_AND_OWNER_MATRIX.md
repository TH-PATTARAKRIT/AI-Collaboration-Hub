# Inventory Full Reopen — Next Controlled Action and Owner Matrix

Session: `SMEPLUS-26-09-02-INV-REOPEN-001` | Jira: `ERPPLUS-139` | Control Level: `/L999.999`
Status: `CP-06/CP-07 OUTPUT — ACTION MATRIX — NOT AN AUTHORIZATION OF ANY LISTED ACTION`

This matrix compiles every recommended next action from deliverables `03`–`13`, `20` into one prioritized, owner-assigned list. **Listing an action here does not authorize it.** Each remains subject to Boss's own decision and the owning track/team's own scoping.

---

## Tier 0 — Boss-Only Decisions (cannot be delegated to any team)

| # | Decision | Deliverable |
|---|---|---|
| 0.1 | Adjudicate the `N-A12-01` files 08/09 clean-room conflict (item `C-05`) — accept Council's "correctable language" reading, Special Team's "remediation required before Team B/C access" reading, or commission the recommended independent tie-breaking read | `13` |
| 0.2 | Rule on which "9 Veto Challenge Council" definition governs (`U-07`) — the execution-team-composed CORR-007B artifact or the audit-mandate-composed ratified Charter | `13`, `03` |
| 0.3 | Decide whether the idempotency/migration-replay gap (`C-02`) is a Gate-blocking requirement or a downstream Team A/Migration design input | `13`, `06` |
| 0.4 | Decide whether `SI-01..10` (Cross-Gate SaaS Invariants) extends to Inventory or Inventory needs its own Boss-approved invariant set | `07`, `13` |
| 0.5 | Render an explicit Gate decision on IDR-007 / CORR-006 / CORR-007A / CORR-007B as a package — the pattern of "recommendation issued, never formally ruled on" has now recurred at least twice in this chain and should not recur a third time | `01`, `03` |
| 0.6 | Confirm whether Track 07's and Track 09's `HOLD` vs. `CONTINUE_WITH_NOTES` verdict splits should stand as reconciled (`HOLD`) or be revisited with Boss's own reading of both narratives | `09`, `11`, `13` |

## Tier 1 — Single Bounded Verification Passes (small, high-traceability-value, one session each)

| # | Action | Owner | Source |
|---|---|---|---|
| 1.1 | Native re-trace of Purchase-side cancellation-cascade symmetry within Inventory Core Backbone (not borrowed from GROUP_A) | Team A / Track 01 | `13` C-01 |
| 1.2 | One bounded verification pass on `N-CONC-01` `try_lock_for_update()` — locking mode, coverage, race sufficiency | Team A / Track 07 | `13` C-04 |
| 1.3 | Exercise Council's review-of-Special-Team-findings function on the `_get_value_from_returns()` return-valuation citation | Track 01 | `13` C-03 |
| 1.4 | Locate and read `N-A13-01`'s `_inverse_qty_available()` method in full — spotted twice across nine rounds, never read | Team A | `05` §10.4 |
| 1.5 | Reconcile the `stock_security.xml` 108-line-vs-169-line citation discrepancy between IER-003 and IDR-007 | Team A / Track 01 | `07` §7, `09` §6 |
| 1.6 | Resolve IER-003 file 08's physical absence from the CORR-005/CORR-007B git trees (chain-of-custody, not content) | Track 01 | `07` §7, `04` §6.4 |

## Tier 2 — Governance / Process Hygiene

| # | Action | Owner | Source |
|---|---|---|---|
| 2.1 | Annotate CORR-007B's rival "9 Veto Challenge Council" document as non-canonical/superseded-in-practice, cross-referencing the actual ratified Charter — preserve, do not delete | Track 01 | `03` §7 |
| 2.2 | Correct or explicitly supersede the canonical `STATE03_ACCOUNTING_INVENTORY_BACKBONE_EVIDENCE_CHAIN_INDEX.md` (frozen pre-DR-002, actively wrong) | Track 01 / PMO | `03` §7 |
| 2.3 | Populate the canonical Global Challenge Continuity Ledger with this reopen's 17 `INV-FP` rows | Track 01 / PMO | `03` §7 |
| 2.4 | Formally declare Material Unknown Exhaustion superseded by the item-by-item Boss-challenge model, or formally re-run it | Track 01, Boss | `03` §3.5, §7 |
| 2.5 | Give concurrent AI sessions isolated worktrees/branches by default — two independent shared-worktree collisions occurred within CORR-007B alone | PMO / all tracks | `03`, `08`, `10` (independently, multiple times) |
| 2.6 | Pair any future self-declared clean-room compliance review with a mechanical citation/fenced-code sweep, not principle-restatement alone | PMO | `10` §7 |
| 2.7 | Confirm procedurally (session/invocation IDs, timestamps) whether this reopen's own 9-Council/9-Special-Team dispatch was genuinely parallel | Track 01 / PMO | `13` U-05, `11` §3.6 |
| 2.8 | Extend CP-01's own disclosure discipline to match CORR-007B file 14's independence-disclosure precedent | Track 01 / PMO | `11` §7 |

## Tier 3 — Named Preconditions for Future Team B Design Work (not authorized to start)

**Financial / Accounting interface (Track 06):**
- Route manufacturing valuation/COGS handoff and landed-cost allocation to further Special Team investigation
- Require SMEsPlus's own clean-room design to state delivery-time vs. billing-time recognition explicitly, not inherit the reference's mismatched label
- Carry `G-2`'s statutory internal-control dimension into any future Team B design authorization

**Process design (Track 03):**
- Produce an `N-A7-01`-parity options-based design-policy brief for over-fulfillment/over-receipt before Inventory Design Freeze
- Carry partial-fulfillment heterogeneity and Sale/Purchase structural asymmetry onto Team B's design-freeze checklist as named items

**System architecture (Track 05):**
- Assign explicit ownership and milestone for Inventory's own SaaS tenancy question
- Resolve the Inventory→Accounting posting-architecture fork by decision, not default
- Carry the do-not-inherit list (`ir.rule` XML framework, `sudo()` escape hatch, `try_lock_for_update()`, category-vs-location field split, Product Category's dual ownership) forward explicitly

**Security (Track 07):**
- Explicit Boss-level scope ruling on whether warehouse-level authorization and operation-level role segregation are Inventory's evidence burden
- `sudo()`-bypass code-path audit across `stock_account`/`sale_stock`/`purchase_stock`/`mrp`
- PDPA/privacy scoped as a new research item, joint with Account/Legal, before production go-live

**AI Control (Track 09) — preconditions for any future AI-orchestrated migration authorization:**
- First-class deterministic migration idempotency key
- External-ID/provenance mapping layer design
- Database-layer, non-ORM-trust tenant-isolation boundary plus post-write leakage audit
- Locked, human-approved Product Category assignment rule table
- Deterministic UOM conversion mechanism
- Generalized exception/anomaly escalation threshold
- Named AI-execution-specific clean-room control (extend A17's quarantine discipline to migration code itself)
- Human-recorded certification step for `G-5` opening balance that AI cannot self-satisfy

## Tier 4 — Deferred to Account Reopen / Joint Reopen

See deliverable `20` in full. Not restated here to avoid drift between the two documents.

---

## Owner Summary

| Owner | Item count (Tiers 1–3) |
|---|---:|
| Track 01 (Audit VETO) / PMO | 11 |
| Team A (general research) | 4 |
| Track 06 (Financial) | 3 |
| Track 03 (IBPV) | 2 |
| Track 05 (IESA) | 3 |
| Track 07 (Security) | 3 |
| Track 09 (AI Control) | 8 |
| Boss directly | 6 (Tier 0) |

No item in this matrix authorizes Team B, Team C, Development, merge, release, or production. This matrix is an ordered work list for evidence and governance hygiene, not a project plan.
