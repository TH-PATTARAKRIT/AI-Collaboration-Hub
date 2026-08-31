# 03 — Cross-Module / Cross-Domain Flow Verification

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D03`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Status Vocabulary Used: charter §8 terms only

## 0 — Method and Inputs

This deliverable independently verifies cross-module/cross-domain coherence between Sales, Inventory, and
Purchase, and the coherence (not the internal design) of their shared boundary with Accounting, per charter §5
items 2 and 12. Four checks were performed, each required by the governing New Prompt Governance and the
Formal IBPV pre-prompt readiness record (`00_PRE_PROMPT_READINESS_SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006.md`
§3.3/§3.5):

1. Does the domain boundary model (`02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md`) create overlapping or
   contradictory ownership?
2. Is the shared-master boundary model (`04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`) consistent with TEAM A's
   approved shared-master evidence (`TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md`)?
3. Does the fact ownership/handoff matrix (`10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md`) contain an
   orphaned fact (created but never consumed) or a fact with ambiguous/dual ownership?
4. Is there a scenario that can fail even when each module is locally correct (charter §5 item 12), and is it
   addressed?

TEAM A's `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` was read in full (all 14 concept sections, §01–§14) for
check 2, not sampled — every claim in TEAM B `04`'s summary boundary table was traced back to a specific TEAM A
evidence ID.

## 1 — Domain Boundary Model: Overlap / Contradiction Check

`02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md` §02–§03 draws boundaries on "who may originate the fact."
Independently re-derived from the same underlying evidence (`TEAM_A/02`–`TEAM_A/04`, `TEAM_A/06`, `TEAM_A/07`):

- Capabilities C1–C13 (Shared Master) are read-only inputs to C14–C35 — confirmed no capability in this range
  authors a commitment, movement, or posting itself.
- C18–C27 (Physical Stock, Reservation, Movement, Reversal, etc.) are Inventory-exclusive — confirmed negatively
  in evidence (`TEAM_A/06` §05: "Sale never reads or writes `stock.quant` directly," "Purchase never reads or
  writes `stock.quant` directly either").
- The only two evidenced write-crossings — (a) Purchase opportunistically extending the Vendor Price Reference at
  commitment time, and (b) a scoped product-configuration Sales→Purchase auto-creation (subcontract/dropship) —
  are each explicitly named, narrowly scoped, and traced to a specific evidence ID (`04` §03; `08` §09; `10` §01
  row "Supply Commitment... except the scoped subcontract/dropship auto-creation"). Neither creates a second
  owner for a fact already owned elsewhere; each is a one-directional, bounded exception with the *result* still
  owned by the receiving domain.

**Finding FV006-XDF-001**
- Verification Area: Domain boundary model — ownership overlap/contradiction
- TEAM B Artifact(s): `02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md` §02–§04
- Approved Evidence/Baseline: `TEAM_A/06_CROSS_MODULE_EVENT_AND_DEPENDENCY_MAP.md` §05;
  `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` §05
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: No capability is claimed by two domains at once, and the two evidenced exceptions to
  strict single-ownership are each explicitly scoped, one-directional, and do not create a competing owner for
  the resulting fact. The boundary model is internally non-contradictory.
- Cross-domain impact: Sales, Inventory, Purchase, Shared Master.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

## 2 — Shared Master Boundary Model vs. TEAM A's Shared Master Dependency Map

Every row of TEAM B `04` §08 (Summary Boundary Table) and `14` §05 (Sharing-Default Matrix) was traced back to a
specific TEAM A `01` concept section:

| TEAM B claim (`04`/`14`) | TEAM A evidence trace |
|---|---|
| Party: no transaction domain writes it; optionally company-scoped | `TEAM_A/01` §02 PTY-06 (`company_id` nullable) |
| Product/Service: only Inventory writes trackability-derived state | `TEAM_A/01` §03 PRD-09/10 (`is_storable` derived, stock-owned) |
| Sales Price Rule read by Sales only; Purchase has no equivalent | `TEAM_A/01` §06 PRC-22 ("no `pricelist_id` field exists on `purchase.order`") |
| Vendor Price Reference read/extended by Purchase only | `TEAM_A/01` §06 PRC-23..25, cross-concept note (`product.supplierinfo`) |
| Tax Rule: required company + jurisdiction scope | `TEAM_A/01` §07 (`account_tax.company_id`/`country_id` both NOT NULL) |
| Payment Term: two distinct partner-property defaults, snapshotted | `TEAM_A/01` §08 PAY-12/PAY-16 (`property_payment_term_id` vs. `property_supplier_payment_term_id`) |
| Currency: global; Rate root-company-only; two unrelated default chains | `TEAM_A/01` §09 (CUR-12; "two unrelated default chains" stated verbatim in both files) |
| Document Sequence: one consistent fallback required (TEAM A found two) | `TEAM_A/01` §10 SEQ-15 ("a different, inconsistent fallback sentinel") |
| Company/Branch: legal-entity hierarchy, disjoint from Thai Tax-Branch | `TEAM_A/01` §12 CO-04, CO-15..24 |
| Cost Dimension: definitions shareable, usage always company-attributed | `TEAM_A/01` §13 AN-04 vs. `account_analytic_line.company_id NOT NULL` |

Every TEAM B claim independently traces to a specific, correctly-read TEAM A evidence item; none was found
overstated, contradicted, or unsupported. TEAM B's departures from the evidenced *defaults* (e.g., requiring one
consistent sequence fallback instead of preserving two, `04` §04) are explicitly labeled as corrections, not
silently substituted.

**Finding FV006-XDF-002**
- Verification Area: Shared-master boundary model consistency with approved evidence
- TEAM B Artifact(s): `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` (all sections), `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §05
- Approved Evidence/Baseline: `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` §01–§13 (full file, all 12 concepts)
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: This is the most evidence-dense boundary claim in the package (12 shared-master concepts × up
  to 3 consuming domains) and it holds up completely under independent line-by-line tracing against the primary
  evidence file. No fabricated coupling and no dropped asymmetry was found.
- Cross-domain impact: All three domains, via every shared-master concept.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

## 3 — Fact Ownership / Handoff Matrix: Orphaned-Fact and Dual-Ownership Check

Every row of `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01 was checked for a listed consumer. No fact
was found with an empty "who reads" column, and no fact was found claimed by two domains as independent authors
without an explicit, narrow, disclosed exception (see §1 above). Two shared-concept patterns were examined
specifically for disguised dual ownership and found sound:

- **Approval Control** (`10` §01 row "Approval state (sequential level-based)"): owned independently per
  instance by "the owning commitment/request document" — a shared *concept*, not a shared *instance*. Each
  document type's approval state has exactly one owner. Not a conflict.
- **Vendor Price Reference**: Shared Master-owned but narrowly, opportunistically extended by Purchase — the one
  disclosed exception (`04` §03, `10` §01). Not a conflict.

However, two cross-domain **reads** asserted elsewhere in the package were found to be **absent** from every file
whose stated job is to define the cross-domain interface contract — this is a coherence gap between files, not a
missing consumer for an owned fact.

**Finding FV006-XDF-003**
- Verification Area: Cross-domain reads into Accounting-owned facts, asserted without a corresponding interface
  definition
- TEAM B Artifact(s): `07_PURCHASE_CANONICAL_DESIGN.md` §07 ("an open vendor bill" as a cancellation-gate
  condition); `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 (same); `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md`
  §04 APR-003 (Sales confirmation gate reading "Shared Master... Party credit exposure") — cross-checked against
  `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` (no section defines a "credit exposure" fact on Party anywhere
  in this file) and `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md` §01/§03 (the Financial Handoff
  Contract lists only Billable-Now write, Tax Rule candidacy, Payment Term, Currency/Rate snapshot, and Cost
  Dimension as what crosses the boundary — no backward "open vendor bill" or "credit exposure" read is modeled)
  and `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §02 (Handoff Points table lists nine handoffs; neither
  read appears)
- Approved Evidence/Baseline: `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` (no such interface
  modeled either — Accounting Core's posting/credit facts are out of GROUP A's researched scope by governance
  §19); `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` §02 PTY-14 (`_compute_credit_to_invoice` is explicitly a
  "cross-module (sale+account) credit-limit coupling," i.e., an Accounting-computed fact, not a Party/Shared
  Master identity fact)
- Finding Status: `CONFLICT FOUND`
- Severity: Major
- Why it matters: Two of TEAM B's own control designs — Purchase's dual cancellation gate (`07` §07: "locked OR
  an open vendor bill") and Sales' proposed Confirmation Gate Policy (`13` §04 APR-003: credit-exposure check) —
  each require reading a fact that this package's own boundary rules place inside Accounting Core (AP
  posting-state; AR credit-limit/aging). `13` §04 additionally mislabels the credit-exposure read as a "Shared
  Master" dependency, but `04` (the file whose entire purpose is to define what Shared Master contains) never
  defines credit exposure as a Party attribute — it is not there to mislabel correctly or incorrectly, it is
  simply absent. `15` (the file whose entire purpose is to define the Accounting interface contract) does not
  define either read either. This is exactly the risk the governing pre-prompt readiness record names explicitly:
  "financial/control assumptions entering GROUP A without Accounting authority." The underlying business
  control is sound and evidenced (TEAM A confirmed both the vendor-bill gate and the credit-exposure coupling
  exist); what is missing is the interface-contract representation connecting a GROUP A control decision to the
  Accounting-owned fact it depends on.
- Cross-domain impact: Purchase ↔ Accounting; Sales ↔ Accounting. Without this interface being named, Team C has
  no specification for how Purchase or Sales would actually obtain either fact at runtime.
- Gate impact: Falls under charter §9's "unresolved accounting/compliance impact" — a named Pre-Development
  blocking condition — specifically for the two control features that depend on it (Purchase's financial-exposure
  cancellation gate; Sales' credit-exposure confirmation-gate option). Does not block the rest of the
  cancellation/confirmation-gate design, which is otherwise sound.
- Required owner: TEAM B (to add the missing backward-read interface definitions to `04`/`15`/`10`, or to
  explicitly relabel the credit-exposure dependency as an Accounting-interface read rather than a Shared Master
  one)
- Blocks Development: Yes, for the two specific control features named above, until the interface is documented
- Boss decision required: No for this specific finding (a design-completeness/consistency correction, not a
  business-policy choice) — separate from the already-disclosed, Boss-owned question of what each gate's default
  behavior should be (`13` §04, `18` item N3)

**Finding FV006-XDF-004**
- Verification Area: Orphaned-fact check across the fact ownership matrix
- TEAM B Artifact(s): `10_FACT_OWNERSHIP_HANDOFF_AND_DEPENDENCY_MATRIX.md` §01, `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md`
- Approved Evidence/Baseline: `TEAM_A/07_BUSINESS_FACT_OWNERSHIP_AND_HANDOFF_MATRIX.md` §01–§05
- Finding Status: `VERIFIED`
- Severity: N/A (positive confirmation)
- Why it matters: Aside from the interface-representation gap in FV006-XDF-003 (a missing *read definition*, not
  an orphaned fact), no fact in the matrix was found with zero declared consumer. Facts that are Inventory-internal
  only (Reservation, Fulfillment Continuation link) are correctly documented as intentionally not read by
  Sales/Purchase (`10` §01, `09` §06) rather than silently unconsumed — this is a deliberate non-coupling decision
  TEAM B states explicitly (`08` §03), not an oversight.
- Cross-domain impact: All three domains.
- Gate impact: None.
- Required owner: N/A
- Blocks Development: No
- Boss decision required: No

## 4 — Scenarios That Can Fail Even When Each Module Is Locally Correct

Per charter §5 item 12 and §6, this section specifically stress-tests scenarios where Sales, Inventory, and
Purchase are each individually correct per their own canonical design, but the *interaction* produces an
unaddressed failure.

### 4.1 — Inventory reserved, then Sales cancels

Explicitly modeled and correct: "A Reservation on a cancelled not-yet-executed instruction is released back to
Available" (`08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §05); consistent with `12` §08 and the Inventory-owned
invariant in `05` §04. No gap.

### 4.2 — Purchase receives, but the stock was already promised elsewhere (allocation-priority race)

This scenario was found **not addressed**. The canonical design defines Reservation as a claim against `Available`
(`On-Hand − Reserved`) stock only (`05` §04; `11` §01) — a Sales Reservation cannot claim not-yet-arrived
(`Forecasted`/`Incoming`) stock, which correctly rules out the *simplest* form of overselling. However, the design
also defines a "chained" Movement Instruction pattern specifically to represent demand-triggered replenishment
(`05` §01: "a Movement Instruction may be chained to another... required to represent... demand-triggered
replenishment chains"), preserved from TEAM A's evidenced make-to-order mechanism (`TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md`
Scenario 1, closed by CORR-003). Nowhere in `05`, `08`, `09`, `11`, or `12` does the design state whether a
chained Purchase receipt, once it becomes On-Hand, is **exclusively earmarked** for the specific downstream
Sales/internal demand that triggered the chain, or whether it re-enters the general `Available` pool the instant
it posts — contestable by any other order's Reservation that happens to claim it first. TEAM A's own evidence
confirmed the chaining *data model* exists (`move_dest_ids`/`move_orig_ids`) but never traced its *allocation
semantics* under contention; TEAM B's canonical design carries the pattern forward without resolving this either,
and does not register it as an open item in `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` (§03's new-items
list, N1–N7, has no entry for allocation priority/earmarking).

**Finding FV006-XDF-005**
- Verification Area: Cross-domain allocation-priority for stock claimed by a chained (demand-triggered) supply
  commitment vs. a competing, independently-reserving Sales commitment
- TEAM B Artifact(s): `05_INVENTORY_CORE_CANONICAL_DESIGN.md` §01 and §04, `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md`
  §01–§02, `11_QUANTITY_COMMITMENT_FULFILLMENT_SEMANTICS.md` §01, `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md`
  §11 (covers only the technical concurrent-writer race on one ledger bin, not the business-semantic allocation
  race across competing commitments), `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §03 (no corresponding
  entry)
- Approved Evidence/Baseline: `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md` Scenario 1 and Scenario 2 gap-closure
  note (chaining data model confirmed to exist; allocation behavior under contention never traced or evidenced
  either way — genuinely absent from the evidence package, not merely unread)
- Finding Status: `GAP FOUND`
- Severity: Major
- Why it matters: This is precisely the class of failure the charter requires IBPV to test for: each module is
  individually correct (Inventory's chaining mechanism is sound; Sales' Reservation-against-Available rule is
  sound; Purchase's direct/synchronous receipt is sound), yet the *interaction* — a Purchase receipt intended for
  one Sales commitment being silently claimed by a different, faster-reserving Sales commitment once it posts as
  On-Hand — is a real operational overselling/broken-promise risk in a genuine order-to-cash + procure-to-pay
  backbone, and no evidence or design decision closes it in either direction.
- Cross-domain impact: Sales, Inventory, and Purchase all participate in the failure mode; none of the three
  domain's own designs is individually wrong.
- Gate impact: Charter §9's "unresolved state/event transition that affects financial/control integrity" — a
  named Pre-Development blocking condition.
- Required owner: TEAM B — to close this the same way it closed the structurally similar Over-Fulfillment Policy
  gap (`12` §02: introduce an explicit, configurable mechanism — here, an allocation-priority/earmarking rule for
  chained supply — rather than leaving the interaction implicit), with the specific default left to Boss/business
  per the pattern already established in this package
- Blocks Development: Yes, for any make-to-order/chained-replenishment feature; does not block the plain
  make-to-stock path, where Reservation-against-Available already prevents the simplest oversell case
- Boss decision required: Yes, for the default allocation rule once TEAM B defines the policy's shape

### 4.3 — Tenant boundary layer: unverifiable against an approved baseline

`14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §02 introduces Tenant as a new top-level isolation layer above
Legal Company. TEAM B discloses, correctly and repeatedly, that this is **not** evidence-derived
(`18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §04; `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §05 item 3:
"Formal IBPV should treat this as a new capability claim requiring its own validation, not as evidence-traced
design"). This review had no approved SMEsPlus SaaS/multi-tenancy project baseline available anywhere in the
supplied evidence, Boss Gate record, or governance charter to independently check the claim against, as the
pre-prompt readiness record itself instructs (§3.3 priority item 4: "verify against approved project
identity/baselines, not TEAM B assertion alone").

**Finding FV006-XDF-006**
- Verification Area: Tenant concept — traceability to an approved project baseline
- TEAM B Artifact(s): `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §01–§03; also referenced in
  `02_CANONICAL_CAPABILITY_AND_DOMAIN_BOUNDARY_MODEL.md` (implicitly, via Company/Branch scoping) and
  `08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §07
- Approved Evidence/Baseline: None located. `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md` §12 (Company/Branch) has
  no tenant-layer concept; no SaaS/multi-tenancy project baseline document was included in, or referenced by, the
  supplied evidence set, Boss Gate record, or IBPV charter
- Finding Status: `EVIDENCE MISSING`
- Severity: Critical
- Why it matters: This is not merely an unevidenced business claim (which TBRAC discipline elsewhere in this
  package handles correctly by labeling and deferring) — it is a structural boundary-layer concept sitting above
  Company/Branch, which every Sales and Purchase line's access-scoping rule (`04` §06, `14` §03) is now defined
  relative to. Charter §9 lists "untraceable Team B design decision" as, by itself, a named Pre-Development
  blocking condition; TEAM B's own readiness report independently reaches the same conclusion. This is the
  single most consequential open item this review identified, because unlike the other findings in this file it
  is not a gap *within* an otherwise-evidenced boundary — it is a new boundary layer with no evidence or approved
  baseline on either side.
- Cross-domain impact: All three domains and Shared Master — every access-scoping rule in the package is now
  expressed relative to a layer this review could not verify.
- Gate impact: Charter §9, "untraceable Team B design decision" — blocking, independent of severity elsewhere.
- Required owner: Boss (a product/business decision on whether SMEsPlus's SaaS multi-tenancy scope is real,
  approved, and at what layer — not resolvable by further TEAM B design reasoning alone, since no evidence exists
  either way)
- Blocks Development: Yes, for any capability whose access-scoping depends on the Tenant layer specifically
  (as opposed to Company/Branch, which is fully evidenced and does not depend on this finding)
- Boss decision required: Yes

## 5 — Summary

| Check | Verdict | Material open items |
|---|---|---|
| Domain boundary model overlap/contradiction | `VERIFIED` | None |
| Shared-master boundary model vs. TEAM A evidence | `VERIFIED` | None |
| Fact ownership/handoff matrix — orphaned facts | `VERIFIED` | None |
| Fact ownership/handoff matrix — undocumented Accounting-boundary reads | `CONFLICT FOUND` (Major) | FV006-XDF-003 |
| Reservation/allocation-priority under cross-domain contention | `GAP FOUND` (Major) | FV006-XDF-005 |
| Tenant boundary layer traceability | `EVIDENCE MISSING` (Critical) | FV006-XDF-006 |

Three of six checks returned a clean `VERIFIED`. Three material findings were raised, none of them a redesign
proposal — each names the specific artifact, the specific missing or unresolved element, and the owner (TEAM B
for two design-completeness items; Boss for the SaaS/Tenant baseline question and for both features' policy
defaults) required to close it. Per charter §9, the Tenant finding (FV006-XDF-006) and the allocation-priority gap
(FV006-XDF-005) each independently justify a `NOT READY FOR DEVELOPMENT` classification for the specific
capabilities they touch (Tenant-scoped access control; make-to-order/chained-replenishment fulfillment), without
implying the rest of the cross-domain design — which this review found substantially `VERIFIED` — is unsound. This
deliverable feeds the consolidated IBPV Independent Verification Report and Pre-Development Gate Recommendation
elsewhere in this package; it does not itself constitute Boss approval, Development readiness, or Team C
authorization.
