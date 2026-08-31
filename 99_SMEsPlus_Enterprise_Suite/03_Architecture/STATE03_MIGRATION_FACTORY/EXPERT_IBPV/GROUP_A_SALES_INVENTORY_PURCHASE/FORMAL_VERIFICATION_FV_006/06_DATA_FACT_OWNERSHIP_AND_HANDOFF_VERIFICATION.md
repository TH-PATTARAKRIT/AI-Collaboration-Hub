> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV | Formal Verification FV-006
> Phase 5 — Fact / Data Ownership / Lifecycle / Handoff Verification | Independent Verification, Not Redesign

# 06 — DATA / FACT OWNERSHIP AND HANDOFF VERIFICATION

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D06`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Verification Function: EXPERT IBPV — Independent Business Process & Design Verification
Domain Group: GROUP A — Sales + Inventory + Purchase
TEAM B Frozen Design Commit Referenced: `b98a3b9fb435845dbd15fae79db63b0b73a82420`
TEAM A Approved Evidence Commit Referenced: `8b0993d824cf726fa52edd687272ff54b0977c42`
Boss Evidence Gate: `EVIDENCE GATE — PASS / BOSS APPROVED` (`GROUP_A_BOSS_EVIDENCE_GATE_APPROVAL_2026-08-31.md`)
Deliverable Role: Formal IBPV Deliverable 06 of 16 (Phase 5 — Fact Ownership / Handoff Verification)

---

## 1 — Scope and Method

This deliverable independently verifies, for every material business fact identified in TEAM B's canonical design,
who owns it, what creates it, what changes it, what locks/reverses it, what happens when it crosses a domain
boundary, and whether its lifecycle-end and audit-history behavior are defined. Per the EXPERT IBPV Charter and the
FV-006 governing prompt, this is a **classification exercise**, not a redesign exercise: every finding below either
confirms traceability to approved evidence/baseline, or names a gap/conflict/missing-evidence point for TEAM B (or
the proper owner) to close. No replacement design is authored here.

TEAM B artifacts reviewed as the primary object of verification:

- `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md`
- `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`
- `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`
- `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md`

Supporting TEAM B artifacts consulted for cross-reference only (their own verification is owned by other FV-006
deliverables and is not repeated here): `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`,
`13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`, `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md`,
`18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md`.

TEAM A approved evidence baseline used for independent cross-check:

- `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md`
- `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md`

Verification questions applied to every fact, per the FV-006 prompt §8 and the IBPV Charter §6: Who owns it? What
event creates/changes it? Who else may write it? Who reads it? What handoff occurs across a domain boundary? What
is its lifecycle end? Is audit history preserved where the fact carries financial or compliance weight?

---

## 2 — Ownership Verification — Shared Master Facts

Cross-checked against TEAM A `01_SHARED_MASTER_DEPENDENCY_MAP.md` §01–§13 and TEAM B `04` §01–§08 / `14` §05.

| Fact | TEAM B Owner (04 §08 / 14 §05) | Verified Against TEAM A | Result |
|---|---|---|---|
| Party | Shared Master admin (identity); no transaction domain writes it | `01` §02 (PTY-01…22): confirms single `res.partner` model, `company_id` nullable, no dedicated warehouse/branch FK | VERIFIED |
| Product/Service | Shared Master admin (identity); Inventory writes stock-trackability derived state | `01` §03 (PRD-01…18) | VERIFIED WITH CONDITIONS — see Finding FV006-DFO-003 |
| Product Classification | Shared Master admin only | `01` §04 (CAT-01…11) | VERIFIED |
| UOM | Shared Master admin; conversion ratio immutable once referenced | `01` §05 (UOM-11: write() blocks ratio change once any non-cancel/done stock.move/quant references it) | VERIFIED |
| Sales Price Rule | Shared Master admin / Sales pricing admin; Sales-only | `01` §06 (PRC-22: no `pricelist_id` field exists on `purchase.order`) | VERIFIED |
| Vendor Price Reference | Shared Master admin; narrow write exception for Purchase at commitment time | `01` §05/§06 (PRD-14, PRC-23/24: `product.supplierinfo`) | VERIFIED |
| Tax Rule | Shared Master admin (Accounting-adjacent); substitution algorithm Controlled Carry-Forward | `01` §07 (TAX-07: fiscal-position base model not located — EVIDENCE_MISSING) | VERIFIED — TEAM B correctly preserves the Unknown rather than inventing substitution logic |
| Payment Term | Shared Master admin; TEAM B claims snapshot-on-commitment | `01` §08 (PAY-11…17: only a live FK `payment_term_id`/`property_supplier_payment_term_id` evidenced on the order; schedule realization occurs at Accounting's `account.move`, not on the order itself) | **GAP** — see Finding FV006-DFO-004 |
| Currency / Rate | Shared Master admin (Rate: root-company only); frozen/snapshotted at commitment on both sides | `01` §09 (CUR-15, CUR-18: `currency_rate` frozen at `date_order` on both Sale and Purchase) | VERIFIED — directly evidenced, correctly adopted |
| Document Sequence | Shared Master admin; TEAM B requires one consistent fallback behavior | `01` §10 (SEQ-15: Sale falls back to literal `"New"`, Purchase to `"/"` — confirmed CONFLICT) | VERIFIED — TEAM B correctly labels this a design requirement to resolve an evidenced inconsistency, not an invented rule |
| Warehouse / Location | Shared Master / Inventory admin; Warehouse immutable after creation | `01` §11 (WH-10: `write()` raises `UserError` on `company_id` change; WH-20/21: base Sale/Purchase carry zero Warehouse references) | VERIFIED |
| Company / Branch | Shared Master admin; hierarchy immutable after creation | `01` §12 (CO-09: changing `parent_id` raises `UserError`; CO-27/29: both Sale and Purchase call `_accessible_branches()`) | VERIFIED |
| Cost Dimension | Shared Master admin; definitions shareable, usage always company-attributed | `01` §13 (AN-04 nullable on Account, but `account_analytic_line.company_id NOT NULL`) | VERIFIED |

---

## 3 — Ownership Verification — Commercial / Physical / Supply / Financial-Handoff Facts

Cross-checked against TEAM A `07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` §01–§06 and TEAM B `10` §01–§04.

| Fact | TEAM B Owner (10 §01) | Verified Against TEAM A | Result |
|---|---|---|---|
| Commercial Commitment (header+line) | Sales; no other domain writes | `07` §01 (SO state, `action_confirm()`, `locked`) | VERIFIED |
| Supply Commitment (header+line) | Purchase; scoped subcontract/dropship auto-creation remains Purchase-owned once created | `07` §05 (`sale_purchase`/`sale_purchase_stock`, `sale_line_id` write path — "Hard, but scoped") | VERIFIED — the narrow creation-vs-ownership split is explicitly and correctly stated, avoiding a silent dual-owner reading |
| Internal Demand Request | Purchase (demand-capture) | `07` §04 (`purchase_request.state`, real/active usage confirmed) | VERIFIED |
| Movement Instruction / Execution | Inventory; **hard rule**, no other domain writes | `07` §02 (`_action_done()`; "both read-only, neither module writes physical-movement facts") | VERIFIED — TEAM B's "hard rule" wording matches TEAM A's evidenced exclusivity exactly |
| Stock Position | Inventory; only as a consequence of Movement Execution | `07` §02 (`stock.quant.quantity`, `_update_available_quantity()`) | VERIFIED, and TEAM B's `12` §11 independently strengthens this beyond evidence (see §6 below) |
| Reservation | Inventory | `07` §02 (`stock.quant.reserved_quantity`) | VERIFIED |
| Fulfillment Continuation (backorder) link | Inventory; **not directly read by Sales/Purchase** | `07` §02 ("Neither Sale nor Purchase read this field... genuine non-consumption", POL-31 full-grep confirmed) | VERIFIED — high-fidelity match, including the negative-evidence nuance |
| Reversal | Inventory; traceability-only read by Sales/Purchase | `07` §02/§06 (no "un-execute" path evidenced anywhere) | VERIFIED |
| Billable-Now quantity | Sales / Purchase, each its own | `07` §03 (`qty_to_invoice`, `_compute_qty_to_invoice()`) | VERIFIED |
| Invoiced quantity | Sales / Purchase, but explicitly **backward-derived**; Financial Handoff is the actual source of truth | `07` §03 ("A round-trip: Accounting owns the source data, Sale owns the derived field") | VERIFIED — the mirror/source-of-truth split is explicit, closing a potential dual-owner ambiguity (see §6) |
| Approval state (amount-threshold) | Purchase | `07` §04 (`po_double_validation`, real/sourced) | VERIFIED |
| Approval state (sequential level-based) | Sales / Purchase / Internal Demand Request, each owning its own instance of a shared Approval Control concept | `07` §04 (three modules confirmed installed/used; internal logic EVIDENCE_MISSING) | VERIFIED — TEAM B correctly separates the shared *template* from each document's own *instance*; internal-logic HOLD is correctly preserved, not designed around |
| Traceability unit (lot/serial) | **Not listed** in `10` §01 | `01`/`07` do not directly evidence a GROUP A ownership rule for lot/serial identity | **GAP** — see Finding FV006-DFO-001 |
| Handling unit (package) | **Not listed** in `10` §01 | Not directly evidenced in the TEAM A files reviewed for this deliverable | **GAP** — see Finding FV006-DFO-001 |
| Standing agreement (blanket/template) | **Not listed** in `10` §01 | Not directly evidenced in the TEAM A files reviewed for this deliverable | **GAP** — see Finding FV006-DFO-002 |
| Financial Handoff contract shape | Jointly negotiated — Sales/Purchase own producing the value, Accounting owns acceptance criteria | `10` §04, self-labeled "Independent Addition" | VERIFIED — an explicit, well-labeled co-ownership with a stated arbitration rule; a positive example of the discipline this verification is checking for |

---

## 4 — Cross-Domain Handoff Verification

TEAM B `10` §02 lists nine handoff points; TEAM A `07` §05 lists seven. All seven TEAM A handoffs are present in TEAM
B's set with matching Hard/Advisory classification and matching qualifying language:

| Handoff | TEAM A (`07` §05) | TEAM B (`10` §02) | Result |
|---|---|---|---|
| Commercial commitment → physical fulfillment | Hard | Hard | VERIFIED, verbatim-equivalent |
| Supply commitment → physical receipt expectation | Hard | Hard | VERIFIED, verbatim-equivalent |
| Physical execution → commercial/supply derived quantity | Advisory (but drives next hard gate) | Advisory (but drives next hard gate) | VERIFIED, near-identical wording |
| Fulfillment quantity → billing eligibility | Hard | Hard | VERIFIED |
| Financial posting → re-derived invoiced quantity | Hard | Hard | VERIFIED |
| Internal demand → supply commitment | Hard | Hard | VERIFIED |
| Commercial line (scoped config) → draft supply commitment | Hard, scope-limited | Hard, scope-limited | VERIFIED, verbatim-equivalent |

TEAM B adds two handoffs with no direct TEAM A predecessor: "Stock shortage → supply need" (reflective/pluggable
dispatch, explicitly honest that "Inventory does not know who will respond") and "Physical reversal → traceability"
(advisory, informational only). Both are corollaries of already-evidenced facts (Supply Need Signal, Reversal
traceability requirement) rather than net-new business capability, and neither is dressed up as evidenced fact —
**VERIFIED as a reasonable, non-overclaiming elaboration**, not an unlabeled invention.

**Accounting interface boundary** (`15` §01–§08): the handoff contract (Billable-Now quantity + resolved
Party/Product/Currency/Payment-Term/Tax-candidacy/Cost-Dimension identities) is well-bounded; TEAM B explicitly
excludes COA, GL posting, WHT engine, and fiscal-position internals from its own design authority (`15` §08),
consistent with the IBPV Charter's own scope boundary. The correction/reversal signal requirement (`15` §05 — a
posted-record correction must be observable on Sales/Purchase's next backward read, never a stale cached value) is
a materially adequate audit-continuity requirement at the interface boundary. VERIFIED.

---

## 5 — Competing-Ownership Check

Systematically checked every fact in §2–§3 for a second, unstated writer. Results:

- **No silent dual ownership found** in the Shared Master layer: the one narrow, explicitly-scoped exception
  (Purchase extending Vendor Price Reference) is stated with its boundary named precisely ("never Product, Party, or
  any other master concept" — `04` §03).
- **Amount-threshold and sequential-level approval are correctly modeled as two separate facts**, not one merged
  field, even though TEAM A evidence shows both mechanisms genuinely coexist on the same Purchase Order in
  production (`13` §01, restated from `07` PURCHASE_CANONICAL_DESIGN §03). This avoids the exact "two owners on one
  fact" failure mode this check is designed to catch.
- **Invoiced quantity's round-trip is explicitly arbitrated**: Accounting is stated as the actual source of truth;
  Sales/Purchase's own field is stated to be a read-only mirror. Not a competing-owner situation.
- **Stock Position** is protected against a real, evidenced competing-writer risk: TEAM A's evidence (Team A
  Fit-Gap material referenced in `12` §11) shows concurrent writers to the same logical stock bin can each insert a
  competing row requiring after-the-fact reconciliation. TEAM B `12` §11 requires this to become an **enforced**
  invariant (concurrency-safe upsert or equivalent) rather than an application convention — a deliberate
  strengthening beyond evidence, clearly labeled. VERIFIED, commendable.
- **One material internal inconsistency found**: Product/Service "stock-trackability" is stated in the same file
  (`04` §02) both as "derived from type, full stop... not a separately overridable flag" and as a fact that
  "Inventory may write." See Finding FV006-DFO-003.

---

## 6 — Lifecycle-End (Archival / Reversal / Correction) Check

| Fact type | Lifecycle-end evidence | Result |
|---|---|---|
| Movement execution (actual) | Immutable; correctable only via a new opposing movement (Reversal) — `03` §03 | VERIFIED |
| Reservation | Released on cancellation or converted to physical decrement on execution — `03` §03 | VERIFIED |
| Internal Demand Request | Create/approve/reject/convert — full lifecycle stated — `10` §01 | VERIFIED |
| Multi-vendor comparison (tender) | Resolved at confirmation; losers cancelled, not deleted, history-preserving — `03` §04 | VERIFIED |
| Line deletion after commitment | A confirmed line with Financial Handoff activity cannot be deleted, only zeroed, symmetric both sides — `12` §15 | VERIFIED |
| Traceability unit (lot/serial) | No stated lifecycle end (closure/exhaustion/archival) | **GAP** — folded into Finding FV006-DFO-001 |
| Handling unit (package) — live instance | No stated disposition of the *live* fact after the historical snapshot is frozen at transfer completion | **GAP** — folded into Finding FV006-DFO-001 |
| Standing agreement (blanket/template) | No stated expiry/supersession/cancellation lifecycle | **GAP** — folded into Finding FV006-DFO-002 |
| Reference/Master facts generally (Party, Product/Service, Tax Rule, Payment Term, Currency, Document Sequence) | No general "archive, do not hard-delete, once referenced by a historical Commitment/Physical/Financial fact" rule stated at the Shared Master level, despite TEAM A evidencing this exact protection for several individual concepts (UOM-06: protected UoMs archived not deleted; PAY-07: payment-term delete blocked while referenced by `account.move`; CUR-08: a currency used by any company cannot be deactivated) | **GAP** — see Finding FV006-DFO-005 |

---

## 7 — Audit-History Preservation Check (Financial / Compliance-Weight Facts)

| Fact | Audit-history mechanism | Result |
|---|---|---|
| Movement Execution | Immutable once executed; only a new opposing movement corrects it — "TEAM B's strongest inherited invariant" (`03` §03) | VERIFIED |
| Billable-Now / Invoiced quantity | Control/Financial-handoff type is "history-preserving once acted upon" (`03` §00); traceability link elevated from database-only FK to application-visible (`15` §04) | VERIFIED |
| Reversal | Mandatory traceability link to the movement it reverses (`03` §03) | VERIFIED |
| Line deletion after commitment with Financial Handoff activity | Zeroed, not deleted, symmetric both sides (`12` §15) | VERIFIED |
| Currency / Rate | Frozen at commitment time; a missing-rate condition must surface as a data-quality exception rather than silently defaulting to parity (`04` §04) | VERIFIED — this is a deliberate strengthening beyond the evidenced silent-fallback behavior, and is labeled as such |
| Financial posting correction/reversal | Sales/Purchase's backward read of Invoiced quantity must always reflect current Accounting state, never a stale cached value (`15` §05) | VERIFIED |
| Approval rejection | Rejection is a first-class event with actor, reason, and timestamp (`12` §14, `13` §03) | VERIFIED at the shape level; internal resubmission-vs-restart behavior is correctly left `HOLD` pending the unavailable legacy module source — this is a Cluster B / Deliverable 07 concern and is not re-litigated here |
| Payment Term installment schedule | Claimed to be snapshotted onto the commitment as a historical fact (`04` §04) | **Not independently confirmed** — see Finding FV006-DFO-004; if the underlying behavior is in fact a live reference rather than a freeze, a later edit to a shared Payment Term could retroactively reinterpret a historical commitment, which would itself be an audit-integrity gap |
| Reference/Master facts referenced by a historical transaction | No general non-deletion/archival rule stated | **Gap** — see Finding FV006-DFO-005; this is squarely an audit-history-preservation question, since a hard-deleted Party/Product/Tax-Rule/Payment-Term/Currency/Sequence record referenced by a historical Commitment or Financial Handoff would leave a broken or ambiguous audit trail |

---

## 8 — Cross-Check Against TEAM A — Omissions Either Direction

**TEAM A facts checked for omission from TEAM B's catalog/matrix**: every row in `TEAM_A/07` §01–§06 and every
concept in `TEAM_A/01` §01–§13 was traced to a corresponding TEAM B catalog entry or boundary-model row. No TEAM A
fact was found silently dropped. Two items warrant explicit note as correctly-preserved carry-forwards rather than
omissions:

- The two independent, uncoordinated Thai "branch" mechanisms (`TEAM_A/01` §12, CO-15…24) are **not** designed into
  TEAM B's Party/Company model as a resolved ownership rule, but this is not a silent omission — it is explicitly
  tracked as a Controlled Carry-Forward in TEAM B's own `16` §01 item 1 and `18` §01 item 4. VERIFIED as correctly
  handled, not a gap in this deliverable's scope.
- The `res.partner` multi-brand/multi-HQ orphaned columns (`TEAM_A/01` §02, PTY-21/24) are explicitly excluded from
  the canonical Party model (`04` §01) and explicitly carried forward (`18` §01 item 3), not silently dropped.
  VERIFIED as correctly handled.

**New TEAM B facts checked for correct "new decision" labeling**: Tenant (`14` §02 — explicitly self-labeled
"Independent decision... registered as a new capability requirement, not inferred from evidence," and reconfirmed
in `18` §04) and the Financial Handoff Contract's joint-ownership statement (`10` §04 — explicitly self-labeled "an
independent addition... not explicit in evidence") are both **correctly and explicitly labeled** as new design
decisions rather than being presented as inherited fact. This is the standard the rest of the catalog should be
held to; the one place this standard is not met is the Payment Term snapshot claim (Finding FV006-DFO-004), which
reads as an evidenced-adoption statement in parallel with the genuinely-evidenced Currency snapshot statement in
the same section, but is not supported by an equivalent TEAM A citation.

---

## 9 — Material Findings

### FV006-DFO-001 — Traceability Unit and Handling Unit facts absent from the Master Ownership Table

- **Verification Area**: Data / Fact Ownership
- **TEAM B Artifact(s)**: `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §03 ("Traceability unit (lot/serial)",
  "Handling unit (package)"); absence confirmed in `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01
- **Approved Evidence / Baseline Reference**: No TEAM A ownership-matrix equivalent was located in
  `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` or `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` for
  either fact within the files reviewed for this deliverable
- **Finding Status**: GAP FOUND
- **Severity**: Major
- **Why it matters**: The catalog itself calls Handling Unit "a first-class design decision, not a footnote" and
  requires every Commitment and Physical fact to carry a durable, application-visible identity (`03` §06). Lot/serial
  traceability and package/handling-unit membership are exactly the kind of facts that carry recall, batch-integrity,
  and audit weight in an ERP; leaving them out of the Master Ownership Table means no single document currently
  states who owns creation, what event changes them, who else may write them, or what their lifecycle end is (see
  §6 above — neither fact has a stated lifecycle end either).
- **Cross-domain impact**: Both facts sit at the Inventory/Physical layer but are read cross-domain wherever
  traceability is required (recalls, batch costing, warranty), so an unresolved owner creates ambiguity for any
  future Sales/Purchase-side traceability query.
- **Gate impact**: Does not block the current design's internal coherence, but leaves two catalog-declared "material"
  facts without the ownership specification the rest of the matrix provides.
- **Required owner**: TEAM B (to add the missing rows) — Purchase/Inventory business owner if additional evidence
  or a policy decision is required.
- **Blocking Development**: No, but should be closed before Pre-Development Gate sign-off, since Development would
  otherwise need to infer an owner unilaterally at build time.
- **Boss decision required**: No, unless TEAM B's clarification surfaces a genuinely new capability requirement.

### FV006-DFO-002 — Standing Agreement (blanket/template) absent from the Master Ownership Table

- **Verification Area**: Data / Fact Ownership
- **TEAM B Artifact(s)**: `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §04 ("Standing agreement
  (blanket/template)"); absence confirmed in `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01
- **Approved Evidence / Baseline Reference**: No TEAM A ownership-matrix equivalent located within the files
  reviewed for this deliverable
- **Finding Status**: GAP FOUND
- **Severity**: Moderate
- **Why it matters**: The catalog states this is "a real, evidenced distinction from a live commitment" but the
  ownership matrix does not state who owns it, what creates/changes it, or its lifecycle end (expiry, supersession,
  cancellation).
- **Cross-domain impact**: Confined to Purchase/Shared-Master boundary; low direct cross-domain exposure, but a
  Supply Commitment's pricing resolution logic depends on this concept being unambiguous.
- **Gate impact**: Minor completeness gap in an otherwise well-specified matrix.
- **Required owner**: TEAM B.
- **Blocking Development**: No.
- **Boss decision required**: No.

### FV006-DFO-003 — Internal inconsistency: Product/Service stock-trackability stated as both pure derivation and an Inventory-writable fact

- **Verification Area**: Data / Fact Ownership — competing-ownership check
- **TEAM B Artifact(s)**: `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §02 (both the "derived from type, full
  stop... not a separately overridable flag" statement and the "Only Inventory may write the... derived state"
  statement appear in the same section); restated in `04` §08 and `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`
  §01
- **Approved Evidence / Baseline Reference**: `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` §03 (PRD-09/10: the
  reference system's `is_storable` is a computed field forced to `False` whenever `type != 'consu'` — i.e., purely
  derived, not independently written by any module)
- **Finding Status**: CONFLICT FOUND
- **Severity**: Moderate
- **Why it matters**: The catalog's own design intent (closing the reference system's "two switches for one
  decision" ambiguity) is undermined by granting Inventory a write permission on the same fact it says should be a
  pure function of `type`. This is precisely the "two silently-competing owners on one fact" pattern this
  verification is required to check for: if trackability can both be recomputed from `type` and independently
  written by Inventory, the two paths could diverge under a bug or race condition, recreating the exact ambiguity
  TEAM B states it closed.
- **Cross-domain impact**: Sales, Inventory, and Purchase all read this fact; a divergence would silently affect
  order-line eligibility for physical fulfillment across all three.
- **Gate impact**: A documentation/design-clarity issue, not a fundamentally unresolved business question — the
  underlying business intent (trackability follows type) is stated consistently everywhere except the ownership
  wording.
- **Required owner**: TEAM B — clarify whether Inventory's role is (a) a pure recomputation trigger with no
  independent write semantics, or (b) a cached/stored projection, and if (b), state the invariant that prevents it
  from diverging from `type`.
- **Blocking Development**: No.
- **Boss decision required**: No.

### FV006-DFO-004 — Payment Term "snapshot" claim not supported by an equivalent evidence citation

- **Verification Area**: Data / Fact Ownership — evidence traceability
- **TEAM B Artifact(s)**: `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §04, Payment Term paragraph ("the
  specific installment schedule is copied onto that commitment as a historical fact, not left as a live reference —
  TEAM B adopts this snapshot pattern deliberately")
- **Approved Evidence / Baseline Reference**: `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` §08 (PAY-11…17): evidence
  shows only a live FK (`payment_term_id` / `property_supplier_payment_term_id`) stored on the Sale/Purchase order;
  the installment schedule itself is realized only at the Accounting-layer `account.move` (PAY-14, PAY-17); no
  write-block or immutability guard equivalent to UOM-11 (UOM ratio) or PRC-19 (pricelist-on-confirmed-order) is
  evidenced for Payment Term at the commitment level
- **Finding Status**: EVIDENCE MISSING
- **Severity**: Moderate
- **Why it matters**: The sentence is structurally parallel to the Currency/Rate sentence in the same section, which
  *is* directly evidenced (`TEAM_A/01` CUR-15/CUR-18: `currency_rate` frozen at `date_order`). Presenting an
  unevidenced claim in the same voice as an evidenced one risks a reviewer treating both as equally settled. If the
  actual target behavior leaves Payment Term as a live reference rather than a freeze, a later edit to a shared
  Payment Term's installment lines could retroactively reinterpret an already-committed order — which would itself
  be an audit-integrity gap against the catalog's own stated principle that a Commitment fact, once made, is
  history-preserving (`03` §00).
- **Cross-domain impact**: Affects both Sales and Purchase commitments and their eventual Financial Handoff payload
  (`15` §03 lists "the resolved Payment Term (snapshotted at commitment time)" as part of what Accounting must
  consume — the Financial Handoff design already depends on the snapshot assumption being true).
- **Gate impact**: Should be reclassified as either (a) a TEAM B independent design decision, explicitly labeled the
  same way Tenant and the Financial Handoff Contract co-ownership are labeled elsewhere, or (b) closed with a
  specific evidence citation if such evidence exists outside the files reviewed for this deliverable.
- **Required owner**: TEAM B.
- **Blocking Development**: No, but should be resolved before Financial Handoff implementation begins, since `15`
  §03 already relies on it.
- **Boss decision required**: No, unless resolving it surfaces a genuine policy question about whether historical
  commitments should be insulated from master-data edits.

### FV006-DFO-005 — No general archival/non-deletion rule stated for Shared Master facts referenced by a historical transaction

- **Verification Area**: Data / Fact Ownership — lifecycle-end / audit-history preservation
- **TEAM B Artifact(s)**: `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §01 (Shared Master Concepts table);
  `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §01–§08
- **Approved Evidence / Baseline Reference**: `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` — UOM-06 (protected
  master-data UoMs "cannot be deleted, only archived"); PAY-07 (payment-term deletion "blocked if any `account.move`
  still references the term"); CUR-08 ("a currency used by any company cannot be deactivated")
- **Finding Status**: GAP FOUND
- **Severity**: Major
- **Why it matters**: TEAM A's own evidence independently shows the reference system already protects at least
  three Shared Master concepts (UOM, Payment Term, Currency) against deletion/deactivation once referenced by a
  transaction. TEAM B's catalog explicitly carries forward this protection only for UOM's conversion ratio and for
  Warehouse's owning-company assignment; it states no equivalent general rule for Party, Product/Service, Tax Rule,
  Payment Term, Currency, or Document Sequence. This is a direct instance of the audit-history-preservation
  requirement this verification was asked to check: a hard-deleted Party, Product, Tax Rule, or Currency record
  referenced by a historical Commitment or Financial Handoff would leave that historical record with a dangling or
  ambiguous reference.
- **Cross-domain impact**: Affects every domain's read of every Shared Master concept, since all rely on the master
  record remaining resolvable for as long as any historical Commitment, Physical fact, or Financial Handoff record
  references it.
- **Gate impact**: Not a design defect in what TEAM B has stated, but a completeness gap in what TEAM B has left
  unstated at the general Shared Master level.
- **Required owner**: TEAM B.
- **Blocking Development**: No, but should be closed before Pre-Development Gate sign-off given its direct bearing
  on audit-history integrity across every Shared Master concept.
- **Boss decision required**: No.

---

## 10 — Positive Verification Notes (Not Findings)

For balance, the following are explicitly confirmed as high-fidelity, well-labeled design work and are not
findings:

- The seven cross-domain handoffs shared with TEAM A's matrix carry matching Hard/Advisory classification with
  near-verbatim qualifying language (§4 above).
- The Fulfillment Continuation (backorder) non-consumption pattern is preserved with its exact negative-evidence
  nuance ("neither Sale nor Purchase read this field," confirmed by TEAM A's full-grep) — a genuinely difficult
  fact to carry forward faithfully, and it was.
- The Financial Handoff Contract's joint-ownership statement (`10` §04) is an exemplary instance of the
  "explicitly shared/co-owned with a stated arbitration rule" pattern this verification looked for.
- The Stock Position uniqueness-at-write-time strengthening (`12` §11) closes a real, evidenced competing-writer
  risk rather than merely inheriting the reference system's after-the-fact reconciliation pattern.
- The Tenant concept and the two uncoordinated Thai-branch mechanisms are both correctly and explicitly carried
  forward as labeled Unknowns/new-capability items rather than silently resolved or silently dropped.

---

## 11 — Verification Roll-Up

| Verification Question | Result |
|---|---|
| Every fact has a single authoritative owner, or explicit shared ownership with a stated arbitration rule | VERIFIED WITH CONDITIONS — one internal conflict (FV006-DFO-003) |
| No fact has two silently-competing owners | VERIFIED WITH CONDITIONS — same conflict as above; all other checked facts pass |
| Every fact has a defined lifecycle end (archival/reversal/correction) | GAP FOUND — Traceability Unit, Handling Unit, Standing Agreement (FV006-DFO-001/002), and general Shared Master archival (FV006-DFO-005) |
| Audit-history preservation is addressed for every fact with financial/compliance weight | VERIFIED WITH CONDITIONS — strong for Movement Execution, Billable-Now/Invoiced, Reversal, Line Deletion; unresolved for Payment Term snapshot (FV006-DFO-004) and general Reference-fact deletion protection (FV006-DFO-005) |
| TEAM A facts omitted from TEAM B's catalog | None found |
| New TEAM B facts correctly labeled as new, not silently introduced | Correctly labeled in the cases checked (Tenant, Financial Handoff Contract), with one exception (Payment Term snapshot, FV006-DFO-004) |

---

## 12 — Scoped Conclusion for This Deliverable

Within the Fact / Data Ownership and Handoff verification area, TEAM B's design is **substantially traceable and
internally coherent**. The Shared Master boundary model and the transactional fact-ownership matrix correctly
reproduce every ownership and handoff rule independently confirmed in TEAM A's approved evidence, correctly
preserve every Unknown TEAM A could not close, and in at least two places (Stock Position concurrency, Currency
no-rate-found handling) deliberately strengthen the design beyond what evidence alone would require — clearly
labeled as such.

Five material findings are recorded (FV006-DFO-001 through FV006-DFO-005), none rated Critical. Two are rated
Major (FV006-DFO-001, traceability/handling-unit ownership gap; FV006-DFO-005, general Reference-fact archival
gap) because they bear directly on audit-history integrity, which this verification was specifically asked to
test; none of the five is assessed as independently blocking Development, but FV006-DFO-001 and FV006-DFO-005
should be closed before Pre-Development Gate sign-off given their direct bearing on traceability and audit-history
preservation. This deliverable's findings feed into the consolidated Design Conflict / Open Gap register
(Deliverable 13) and the final IBPV recommendation (Deliverable 15); this document does not itself issue a
Pre-Development Gate recommendation.
