# Inventory Full Reopen — TBRAC Deep Findings (Track 02): Thailand Business Reality & User Fitness

Session: `SMEPLUS-26-09-02-INV-REOPEN-001`
Jira: `ERPPLUS-139`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Canonical Branch: `SMEsPlus`
Execution Branch: `audit/inventory-reopen-2026-09-02-inv-reopen-001`
Execution Worktree: `INVENTORY_REOPEN_2026_09_02_EXECUTION`
Deliverable: `04_TBRAC_DEEP_FINDINGS.md` — CP-03 (9 Veto Challenge Council) + CP-04 (9 Special Team Challenge) convergence output for Track 02
Mandate / Track: `Track 02 — TBRAC / Thailand Business Reality & User Fitness` (Thai operating reality, user fitness, industry variation, real-user evidence)
Control Level: `/L999.999`
Status: `CP-03 / CP-04 OUTPUT — TBRAC COUNCIL CHALLENGE + SPECIAL TEAM INVESTIGATION COMPLETE — TRACK 02 VERDICT: HOLD / EVIDENCE REQUIRED — NOT A GATE DECISION`

This document does not close, pass, or authorize anything. It converges two findings sets produced independently and blind to each other, per the Nine Veto Council & Special Team Charter's Anti-Groupthink Rule (§8: *"Fresh Council findings must not be shown to other Council mandates before their first pass where practical"*) and Core Control Statement (§10: *"Special Team investigates; Council challenges; PMO preserves; Boss decides."*). This document performs the PMO-preservation function for Track 02 only: it holds both findings sets faithfully, surfaces where they corroborate and where their coverage diverges, and hands the combined evidence to Boss. It does not vote, does not pick one set over the other, and — per Charter §6, *"Neither the Council nor Special Teams decide by majority vote... Boss alone makes final business / Scope / Gate / override decisions"* — it does not decide anything on Boss's behalf.

Both inputs converged here were themselves already-completed, independent passes; this document does not re-run their underlying git/source research. Claims below are attributed to "the Council pass" or "the Special Team pass" as reported by each, with their own citations preserved. Header fields, deliverable numbering, taxonomy vocabulary, and cross-track fingerprint IDs (`INV-FP-*`) are verified directly against `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`, `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`, and `NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md`, all read in full by this consolidation pass.

---

## 1. Executive Summary

Two independent passes examined the same Inventory Core Backbone evidence chain (DR-002 → IER-003 → CORR-005 → IDR-007 → CORR-006 → CORR-007A → CORR-007B) through the TBRAC lens — Thai operating reality, user fitness, industry variation, and real-user evidence — without visibility into each other's findings:

- The **9 Veto Challenge Council, Track 02 (TBRAC)**, running a first-pass independent challenge, reached verdict **HOLD**.
- The **9 Special Team Challenge, Track 02 (TBRAC mirror)**, running a deeper primary-source investigation over the same evidence base, reached verdict **HOLD**.

Both verdicts were reached independently and **converge without conflict**: neither had to be picked over the other. Where the two passes examined the same item, they corroborate rather than contradict each other — in several cases (the Thai branch dual-concept, the count-freeze mechanism, the "damaged goods" absence) the Special Team independently re-verified at primary source exactly what the Council pass concluded from the same documents, which is a meaningfully stronger evidentiary position than either pass alone. Where the two passes diverge is in **coverage, not conclusion**: each surfaced material items the other's pass did not address at all. Per the Charter (*"If a material finding is suppressed from Boss because it is inconvenient, that is a governance control failure"*), this document does not merge those unique items away — §4 below states plainly what each side alone caught, and §8's classification table carries every item forward with a "Raised By" column so nothing is silently absorbed into a false single narrative.

**Reconciled Track 02 verdict: `HOLD / EVIDENCE REQUIRED`.**

The headline reason, stated identically and independently by both passes: every Thai-business-reality claim in nine rounds of otherwise disciplined evidence work traces to exactly one reference vendor's source code plus one customer's database dump, and that dump's `stock_move` table holds only 48 rows across 2 states. No real-user validation — no interview, survey, pilot, or structured Thai SME/warehouse-staff input — has ever been executed anywhere in this chain, and the founding TBRAC control document's own Administrative Red Flags recording that gap on 2026-08-30 remain open, unchanged, three days and seven correction rounds later.

This document does not declare Gate PASS. It does not authorize Team B, Team C, Development, Account Reopen, or the Account × Inventory Joint Reopen. It is a challenge-and-investigation finding for Boss's Gate decision, prepared per Charter §10: *"Boss = Sole Final Approver."*

---

## 2. Checkpoint Records

| Field | CP-03 — 9 Veto Challenge Council, Track 02 | CP-04 — 9 Special Team Challenge, Track 02 mirror |
|---|---|---|
| Checkpoint | `CP-03` | `CP-04` |
| Result | `HOLD` | `HOLD` |
| Evidence | Independent first-pass challenge against the full Inventory Core Backbone chain (DR-002, IER-003, CORR-005, IDR-007, CORR-006, CORR-007A, CORR-007B) and the founding `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` (Doc ID `SMEPLUS-26-08-30-TBRUF-001`, Boss-approved 2026-08-30), produced blind to Track 02's Special Team pass and to the other 8 Council tracks. Full findings in §5. | Deeper primary-source investigation over the same chain, prior-evidence-loaded first per the Special Team Investigation Rule (CP-01 index), with direct re-reads of `IER-003` file 06, `IDR-007` file 05, the canonical Boss scope ruling (commit `997809d`), `CORR-005` file 02, and `CORR-007B` files 02/08/15, plus independent `git merge-base`/`git ls-tree` checks against branch `audit/inventory-core-corr007b-3high-closure-010`. Produced blind to Track 02's Council pass. Full findings in §6. |
| AI Audit SMEsPlus Impact | Directly informs Track 01 (evidence-currency: TBRAC's own real-user-validation gap is itself an evidence-currency question); Track 03/IBPV (Stockable/Consumable/Service Thai edge cases, shared boundary item `INV-FP-13`); Track 06 (Financial/Accounting interface: post-close governance asymmetry G-2, count-freeze design policy); feeds deliverable `12` (Stockable/Consumable/Service deep proof) and `13`/`15` (unknown/conflict and gate-reopen registers). | Directly informs Track 01 (new evidence-traceability/chain-of-custody finding — see §6.4 — is squarely Track 01's mandate); Track 07/Security (`N-A13-02` company-ACL/tenant-isolation residual conditions, `INV-FP-05`); Track 06 (newly-drawn `N-A12-01` → `TH-INV-03` → `COA-G06` dependency, currently unowned by any N-A12-01 deliverable); Track 03/IBPV (Stockable/Consumable/Service, `INV-FP-13`, with two named Thai edge cases for the deep-proof). |
| % Board | `TBD — BASELINE REQUIRED` (no board/tracker reference available to this consolidation pass) | `TBD — BASELINE REQUIRED` |
| % STATE | `TBD — BASELINE REQUIRED` | `TBD — BASELINE REQUIRED` |
| % STEP | `TBD — BASELINE REQUIRED` | `TBD — BASELINE REQUIRED` |
| Open Risks | See §9 (Material Questions and Open Risks) and §8 (Item Classification Table) — none rise to `FAIL / FROZEN`; all are material enough to sustain `HOLD` per Charter §6 (*"A single material Veto may be enough to place a Prompt on HOLD if evidence supports the concern"*). | Same register, §9/§8 — the evidence-traceability finding (§6.4) is additionally flagged for Track 01 ownership, not resolved here. |
| Next Action | PMO consolidation into deliverables `02`, `12`, `13`, `15`, `20`; Boss Gate decision. | Same. |

---

## 3. Track Verdict — Reconciled

| Source | Verdict | Reached |
|---|---|---|
| Council Challenge (CP-03) | **HOLD** | Independently, blind to Special Team |
| Special Team Investigation (CP-04) | **HOLD** | Independently, blind to Council |
| **Reconciled Track 02 verdict** | **HOLD / EVIDENCE REQUIRED** | Both converge; no conflict to arbitrate |

Neither verdict was selected over the other — there was nothing to select between. Both independently applied the same governing rule (Council cites its own control document's Gate Enforcement clause, *"applicable material evidence gap → HOLD"*; the Special Team cites TBRAC's charter §3.3/§6 and its explicit boundary against declaring Gate PASS) and both landed on HOLD from independent readings of the same underlying chain. This is the strongest form of convergence available under the Charter's Anti-Groupthink Rule: two blind passes agreeing is evidence the HOLD is well-founded, not an artifact of one pass anchoring the other.

Nothing in either pass rises to `FAIL / FROZEN — MATERIAL EVIDENCE / GOVERNANCE / CLEAN-ROOM FAILURE`. Both passes are explicit that the existing evidence chain is disciplined and its own gaps are honestly labeled rather than concealed or converted into false facts — the issue is that a structural category of evidence (real Thai user/business input) has never been gathered, not that existing evidence is wrong or fabricated.

---

## 4. Convergence, Corroboration, and Coverage Reconciliation

Per Charter §8 (Anti-Groupthink Rule) and the instruction that a suppressed material finding is a governance control failure, this section states plainly what both passes found together, what each pass alone found, and confirms there is no direct factual contradiction between them on any item they both examined.

### 4.1 Convergent findings — independently corroborated by both blind passes

Both passes, working from the same evidence chain without seeing each other's work, independently reached the same conclusion on each of the following. Independent convergence is treated here as strengthening these findings, not merely duplicating them:

| Item | Council conclusion | Special Team conclusion |
|---|---|---|
| Overall evidentiary foundation | Real-user validation "has never been executed anywhere in the nine-round chain"; the founding control document's Day-1 red flags remain open | "Every Thai-business-reality claim... traces to exactly one reference vendor's source code plus one customer's database dump"; the 48-row `stock_move` table is "too small a sample" |
| Thai branch dual-concept (`INV-FP-03` / GRPA-H8/H3) | Architecture question closed; real-user validation "carried forward... not resolved here" | Re-read `IER-003`/`IDR-007` at primary source; "No delta found; restated, not reopened" — both mechanisms confirmed simultaneously live in the one dataset |
| Expiry/lot tracking (N-A5-02) and consignment stock (N-A5-03) | `EVIDENCE_MISSING — NOT YET RESEARCHED` since 2026-08-31; IDR-007 declined to elevate on an absence-of-evidence basis | Same status, same date, "no delta by any of the three escalation rounds"; recommended as concrete next-delta candidates |
| Count-freeze policy (N-A7-01) | Source behavior is soft conflict-detection only; 4-option design choice open with zero Thai operational input | Independently re-read the method bodies (`stock_quant.py`, `stock_inventory_conflict.py`, `stock_inventory_warning.py`) in full and confirmed the identical disposition |
| Purchase over-receipt control | No ceiling/block evidenced anywhere in the mechanism | Same finding, same citation (`_compute_qty_received()`) |
| Purchase approval-workflow modules | Source "entirely absent from the available volume" (SAAS-05), acknowledged black box | Same finding, confirmed absent "by two independent passes" |
| "Damaged goods" as a distinct exception category | Direct search across the full chain returns zero hits; only scrap and a generic return wizard are evidenced | Independently ran the same direct search with the same null result |
| Stockable/Consumable/Service Thai edge cases (`INV-FP-13`) | Untested against F&B/repair-shop service+parts combos and stocked-vs-drop-shipped trading SKUs | Independently named the same two patterns (service+parts via BOM/kit; dropship resellers, cross-referencing `GRPA-M16`) with added vertical detail (spas/clinics, social-commerce) |

### 4.2 Findings raised only by the Council pass

The Special Team's findings do not address these; they are carried forward here in full rather than treated as absorbed into the shared list:

- **G-2** — the asymmetry between Inventory's single, global, unaudited `skip_lock_date_check` toggle and Accounting's governed, scoped `account.lock_exception` model, framed against ordinary Thai statutory-audit expectations for a registered company.
- **G-3** — backdate enforcement at whole-`stock.picking` (document) granularity rather than per `stock.move` line, and whether that fits real Thai multi-line transfer practice.
- **GRPA-M19** — Thai district/sub-district address data reaching Inventory/delivery routing, classified `UNKNOWN` since 2026-08-31 and not re-tested by any later round.
- Explicit citation of the founding `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` document and its Day-1 Administrative Red Flags (real-user validation panel/sample = TBD; TBRAC named membership = TBD) as the governing artifact this track answers to.

### 4.3 Findings raised only by the Special Team pass

The Council's findings do not address these; they are equally carried forward in full:

- **Evidence-traceability / chain-of-custody gap** — the `IER-003` TBRAC review and the Boss Inventory Scope Ruling (commit `997809d`) that formally closes the branch dual-concept question are both physically absent from the tree of `audit/inventory-core-corr007b-3high-closure-010`, the branch this reopen has been told is controlling. Verified independently via `git merge-base --is-ancestor` and `git ls-tree -r`. This is squarely Track 01's mandate; it is surfaced here because it directly affects re-inspectability of this track's own closed item (see §6.4).
- **`N-A13-02` conditions re-extraction** — company-scoped `ir.rule` enforcement confirmed comprehensive at the ORM layer, explicitly paired with two un-closed residuals (no database-layer CHECK-constraint backstop; unaudited `sudo()`-bypass question across `stock_account`/`sale_stock`/`purchase_stock`/`mrp`), read against real Thai multi-company/multi-branch group structures.
- **`N-A12-01` → `TH-INV-03` → `COA-G06` cross-track dependency** — DR-002's own Thailand register deferred the Thai costing-method/valuation-norm question to `COA-G06` on 2026-08-31; `COA-G06` remains not closed, and no round of CORR-006/007A/007B's `N-A12-01` work names either `TH-INV-03` or `COA-G06`. The dependency itself appears to have been lost between tracks.

### 4.4 Reading this reconciliation

No direct factual contradiction was found between the Council pass and the Special Team pass on any item both examined — where they overlap, they corroborate. The divergence is one of **coverage breadth**, produced naturally by the Anti-Groupthink Rule's design (two blind passes will not sample the same evidence identically), not a disagreement to be adjudicated. Boss should treat the union of §4.1–§4.3 as the operative Track 02 evidence base, not either pass in isolation — this is precisely why the Charter requires both a Council challenge and a Special Team investigation rather than either alone.

---

## 5. Detailed Findings — Council Challenge (CP-03)

### 5.1 The evidentiary foundation and the real-user validation gap

The Council pass's central finding is structural rather than incidental. SMEsPlus's own founding governance document for this exact mandate — `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` (Document ID `SMEPLUS-26-08-30-TBRUF-001`, Boss-approved 2026-08-30, three days before this reopen) — states in writing that "real user validation cannot be replaced by AI synthesis," and its own Administrative Red Flags section recorded, on day one, "Real-user validation panel/sample = TBD / EVIDENCE REQUIRED" and "TBRAC named membership = TBD / GOVERNANCE ASSIGNMENT REQUIRED." Having read the complete Inventory Core Backbone chain — DR-002, IER-003, CORR-005, IDR-007, CORR-006, CORR-007A, and CORR-007B — the Council pass found neither red flag remedied. No interview, survey, pilot, or structured SME/warehouse-staff input appears anywhere across nine rounds of otherwise disciplined, well-cited evidence work. Every item labeled "REQUIRES REAL USER VALIDATION" in this chain carries that label forward unchanged from round to round; none has ever been closed by the validation the label names.

### 5.2 Source-specific mechanics versus Thailand-proven behavior

The Council pass treats this as the direct answer to its material challenge question — which stock-control behaviors are proven for Thai SME/enterprise operation versus merely proven for the reference source. The answer, on the evidence, is that almost nothing in the operational-mechanics layer is Thailand-proven. DR-002's own A11 Thailand Business Reality and Regulatory Register states candidly that its fresh research into stock/valuation, product/UOM, and sale/purchase/manufacturing handoffs "was conducted entirely against generic Odoo business logic, not Thailand-specific customization code," because none of the three research agents dispatched that pass were asked to search for Thailand-specific Inventory logic at all. That scoping choice is defensible given the separately-established fact that Thai customizations in the one available dataset attach only to party/company master data, never to `stock.picking` itself — but it means the state/event lifecycle, warehouse/location/UOM/traceability model, route/procurement logic, and adjustment/count/cutoff mechanics are proofs of Odoo's reference mechanism, not of Thai operating practice. The one place Thai reality was directly tested — the branch/company field conflict — rests on a single company whose entire `stock_move` table holds 48 rows across 2 states, which the underlying re-verification itself calls too small a sample to infer even that one company's actual usage, let alone Thailand-wide practice.

### 5.3 Industry-dependent gaps: expiry/lot tracking and consignment stock

Two industry-dependent, checklist-named items have sat at "EVIDENCE_MISSING — NOT YET RESEARCHED" since DR-002 closed on 2026-08-31: expiration/lot-expiry handling (`N-A5-02`, the `product_expiry` module) and owner/consignment stock (`N-A5-03`). IDR-007 explicitly declined to elevate either — but did so, in its own words, on the basis of "no [contrary evidence] currently," i.e. an absence-of-evidence call rather than a business-impact call informed by Thailand's real food/pharma/cosmetics (expiry-driven) or FMCG/electronics/auto-parts-distribution (consignment-driven) SME segments. Boss's subsequent escalation of eight named items across CORR-006/007A/007B never touched either. The Council pass treats this as exactly the kind of industry-dependent unknown this track exists to keep visible rather than let quietly age out of the register through repeated non-selection, and separately questions whether "Low severity" is itself an unverified assumption for the Thai vertical segments SMEsPlus intends to serve (carried into §8 as a `REOPEN_ELIGIBLE` item).

### 5.4 Design-policy items awaiting Thai operating input

**Count-freeze policy (N-A7-01)** is a fully open, 4-option Team B design decision — hard freeze, soft conflict, location-lock, or manager-exception — with no evidence yet gathered on how Thai warehouses actually run physical counts, so none of the four options can yet be shown to fit real operating practice; this is precisely the "SME simplicity vs. enterprise control" tension this track exists to test.

**Post-close correction governance (G-2)** sits directly on the "documents and approval reality" checklist item. Accounting's period-lock exception mechanism (`account.lock_exception`) is scoped by user, reason, and expiry, and is fully auditable; Inventory's equivalent — a single global `skip_lock_date_check` boolean — carries, in the source proof document's own words, "no record of who set it, why, or for how long." Thai limited companies are broadly subject to annual statutory financial-statement audit regardless of size (the specific statutory citation is outside what this track tested, and would need Track 06/Legal confirmation), which makes an unaccountable, company-wide bypass on the physical-stock side of the ledger a real control-maturity mismatch against the audited side, not a cosmetic asymmetry.

**Backdate enforcement granularity (G-3)** is enforced at the whole-`stock.picking` document level, not per `stock.move` line, and Team B's own carried-forward action item already asks whether document-level granularity is acceptable for SMEsPlus's actual multi-line transfers — a genuine Thai warehouse-workflow question (for example, a receiving document split across a delayed partial delivery) that no one has yet asked a real user.

### 5.5 Receiving, approval, and exception-handling gaps

Purchase-side over-receipt has no ceiling or block anywhere in the traced mechanism, and the purchase-approval-workflow modules that would normally gate such a receipt are, per A10 (`SAAS-05`), completely absent from the available source — an acknowledged black box, not merely unread. A direct search across the entire chain for "damaged goods" as a receiving/warehouse exception distinct from scrap or a generic return returns nothing; only scrap (via the Inventory-loss usage location) and a generic return wizard are evidenced. Neither should be read as a defect in the prior work — DR-002's own scope did not reach delivery-carrier or approval-module internals — but both are genuine, named absences this reopen should not let close by default.

### 5.6 Shared boundary item: Stockable/Consumable/Service routing

A5 §4 establishes what the reference source does — a three-value `type` field (`consu`/`service`/`combo`) plus a separate `is_storable` boolean that only `consu` products can ever set true — but the target-design question of whether this gate, or a Thai-adapted variant, fits real SME/enterprise practice remains `UNKNOWN — STILL MATERIAL` per the reopen's own prior-evidence index (`INV-FP-13`). The Council pass names concrete edge cases for the dedicated deep-proof (deliverable `12`, owned in depth by Track 03/IBPV) to test against real Thai practice: F&B or repair-shop "combo" transactions bundling a stockable part with a service labor line in one document, and trading-house SKUs that are stocked for some customers and drop-shipped direct-from-mill for others on the same product master record.

### 5.7 Council's recommendation

Nothing found contradicts the existing architecture or amounts to an unsafe assumption warranting FAIL/FROZEN, and the discipline of the existing chain in labeling its own gaps honestly is itself worth crediting. But per this track's own control document's Gate Enforcement rule — "applicable material evidence gap → HOLD" — and given that the real-user-validation deficit is total, structural, and unremedied since this program's own founding, the Council pass's verdict is **HOLD**. This is not a call to redo the reopen from zero, nor to reopen the closed branch/architecture ruling — it is a call for Boss to see, in one place, that the Thai-business-reality half of the Inventory evidence base has not materially advanced beyond code-reading and a single 48-move dataset, and that Team B design authorization for count-freeze policy, post-close correction governance, backdate granularity, and expiry/consignment support should not proceed on the assumption that real Thai operating evidence already exists for these choices.

---

## 6. Detailed Findings — Special Team Investigation (CP-04)

### 6.1 Method and scope

The Special Team investigation was conducted under the mirrored TBRAC mandate, independently of the parallel Council challenge. Per the Special Team Investigation Rule, prior Inventory evidence was loaded first (the CP-01 prior-evidence index) and only genuinely open, material-delta items within this mandate's boundary were investigated further: the carry-forward residue on the Thai branch dual-concept (`INV-FP-03`), the Stockable/Consumable/Service routing hypothesis (`INV-FP-13`), the Thai-business-reality angle underneath `N-A12-01`, and a full sweep of this mandate's own checklist against the live git history at the controlling branch, with selective primary-source verification against sibling branches (`IER-003`, `IDR-007`, `CORR-005`, `CORR-006`) and canonical `origin/SMEsPlus` where material. Items already marked `CLOSED_WITH_EVIDENCE` in the prior-evidence index were not re-litigated.

### 6.2 The overarching finding: one thin dataset, nine rounds of re-reading it

The calibrating fact underneath every item below is the shape of the evidence base, not any single open item. Every Thai-business-reality claim in the Inventory Core Backbone chain — from DR-002's original 22-domain research through IER-003, CORR-005, IDR-007, CORR-006, CORR-007A, and CORR-007B — is drawn from exactly one reference vendor's source code plus one customer's database dump, whose `stock_move` table holds only 48 rows across two states. Nine corrective rounds have made the reading of that one sample progressively deeper and more precise; none has ever introduced a second Thai company, a second industry vertical, or an actual interviewed user. A11's own governing rule, restated verbatim in every round that touches it — "one ERP/customer dataset is not Thailand-wide inventory practice" — has been correctly recited and never yet satisfied.

### 6.3 GRPA-H8/H3 re-verified at primary source — no delta

Although already `CLOSED_WITH_EVIDENCE` as an architecture question in the prior-evidence index, the Special Team pass went to primary source anyway — reading IER-003's own TBRAC review document and IDR-007's later carry-forward audit of it in full — both to confirm the restatement is accurate and to look for material delta. None was found: the two branch mechanisms (`l10n_th`'s computed, `company_registry`-derived branch display, and `l10n_th_partner`'s independently stored Char field) are confirmed simultaneously installed and live in the one customer's actual production data, genuinely uncoordinated, and the closure correctly avoids claiming which one, if either, reflects real business practice. "REQUIRES REAL USER VALIDATION" stands exactly where IER-003 left it — an external dependency this reopen cannot discharge internally.

### 6.4 New finding: evidence-traceability gap in the controlling branch

In the course of that re-verification, the Special Team pass made one new, independently confirmed finding, not carried from any prior document. Using `git merge-base --is-ancestor`, it confirmed that the IER-003 TBRAC review document and the Boss Inventory Scope Ruling that formally closes the branch question (commit `997809d`) are both physically absent from the tree of `audit/inventory-core-corr007b-3high-closure-010` — the branch this reopen has been told is latest/controlling. IER-003 and CORR-005 are sibling branches forked from the same DR-002 tip, not a linear chain, and the ruling's own commit exists only on canonical `origin/SMEsPlus`, never merged into any audit branch. CORR-005's prose cites both by relative path; those paths resolve to nothing inside the branch anyone is currently told to treat as controlling. The Special Team independently read the ruling's actual canonical text and confirmed it matches every downstream paraphrase precisely — **this is a chain-of-custody gap, not a content contradiction**, and the closures themselves remain sound — but it means an auditor working only from the controlling branch cannot currently open either grounding document, only trust a chain of citations. This finding is squarely within Track 01's evidence-currency mandate; it is recorded here because it directly affects re-inspectability of this track's own closed item.

### 6.5 N-A13-02 — company ACL / tenant isolation conditions, re-extracted

The Special Team's task brief specifically flagged that `N-A13-02`'s "VERIFIED WITH CONDITIONS" disposition (`INV-FP-05` in the prior-evidence index) had never had its conditions independently re-extracted from CORR-005's own text by any prior pass. Doing so: company-scoped `ir.rule` enforcement is confirmed comprehensive at the ORM layer (a full 16-model rule table and the complete `ir.model.access.csv` were read), explicitly paired with two distinct, un-closed residuals — the already-known absence of any database-layer CHECK-constraint backstop (`SAAS-03`), and a genuinely un-audited question of whether every code path in `stock_account`, `sale_stock`, `purchase_stock`, and `mrp` actually routes through the standard ORM versus a `sudo()` call that bypasses record rules entirely. This matters concretely for real Thai operations: many Thai SME groups run several legal companies under one ownership structure for tax and liability reasons, sharing one back-office team across "branches" that are really separate companies in the platform's own terms. The promise that a storekeeper scoped to one company cannot see or adjust another company's stock currently rests entirely on unaudited application code, with no database-level backstop if that code is ever wrong. This is Track 07's audit to perform; it is reported here because it is the concrete mechanism underneath this mandate's branch/warehouse operational-difference checklist item.

### 6.6 N-A12-01 — the unnamed Thai-costing-method dependency

`N-A12-01` belongs primarily to Track 06 and Track 03, and the Special Team pass does not attempt to resolve it or select a design option. CORR-007B's Product Category valuation proof is genuinely deep and well-cited at the mechanism level — Product Category proven as the true owner of costing method and valuation timing; Periodic and Perpetual confirmed as independent axes from standard/FIFO/average costing — but all of it is generic-Odoo mechanism proof. DR-002's own A11 register already asked the real Thai question directly — does Thai inventory-valuation and reporting practice require or customarily use a specific costing method, and is Periodic or Perpetual actually the norm for a Thai SME versus a Thai enterprise — and explicitly deferred it to `COA-G06`, Thailand Tax Accounting Controls. `COA-G06` remains not closed. No file in the CORR-007B `N-A12-01` package names `TH-INV-03` or `COA-G06` at all. No depth of further Inventory-side mechanism proof can make `N-A12-01` Thailand-fit without an Accounting/Tax-side answer to a question that has been sitting, correctly deferred and quietly unaddressed, since 2026-08-31.

### 6.7 Stockable/Consumable/Service — Thai industry edge cases

Track 03 owns the dedicated deep-proof on this routing hypothesis; the Special Team's contribution is limited to Thai-business-reality risk framing. The reference mechanism is well evidenced: a three-value `type` field gates whether `is_storable` can ever be true, and lot/serial tracking is forced off whenever a product is not storable. Two concrete Thai-industry patterns are named for that deep-proof to test rather than assume: Thai repair trades, spas and clinics, and food-and-beverage businesses commonly sell something structured as a "service" that also consumes physical parts or supplies, ordinarily reconciled through a linked bill-of-materials or kit rather than the service line itself carrying stock; and Thailand's large social-commerce and marketplace reseller segment commonly sells goods that are nominally "Stockable" but that the seller never physically holds, a pattern the evidence chain already names once, as `GRPA-M16`'s dropship carry-forward. Both are offered as named hypotheses requiring real-user validation, not as verified conclusions.

### 6.8 Checklist sweep

Reading CORR-007B's count-freeze proof in full, at the method-body level, confirmed the reference system implements soft conflict detection only — an `is_outdated` signal resolved through a wizard at apply time — never a hard freeze; four design options are correctly named for Team B without a recommendation, and none has been tested against real Thai warehouse practice. On returns and overages, returns funnel through one generic wizard with a `to_refund` exclusion flag, and purchase-side received quantity is computed with no ceiling at all against ordered quantity — over-receipt is simply a larger completed move, never specially flagged. No distinct "damaged goods" workflow, separate from ordinary scrap or write-off, was found anywhere in the evidence read. On lot/serial/expiry, expiration handling and consignment were both explicitly registered as unresearched at DR-002's close and remain untouched through three further escalation rounds; the underlying `product_expiry` source itself lives outside this repository in the adjacent `ACCOUNT/` directory, which this session's own prior-evidence context flags as belonging to a separate, parallel Account-reopen session — that boundary was honored rather than read across sessions. On documents and approvals, three Purchase approval modules gate whether a physical receipt is even expected, and their logic is confirmed absent from the entire available source volume by two independent passes — a black box against real Thai single-approver-SME versus multi-level-enterprise sign-off practice.

### 6.9 Special Team's recommendation

No contradiction, unsafe assumption, or fabricated fact was found in this mandate's scope; nothing here warrants FAIL/FROZEN. Equally, no new evidence closes any of the open items above, and several — the dataset-thinness ceiling, the orphaned TBRAC/ruling documents, the untouched expiry and consignment gaps, and the untested Thai edge cases on service-routing and count-freeze — are material enough that a Product or Replacement Readiness claim would be premature. Consistent with TBRAC's own charter and this mandate's explicit boundary against declaring Gate PASS or authorizing further teams, the Special Team's recommendation to Boss is **HOLD**: the standing Account+Inventory Backbone HOLD is independently reconfirmed from the Thai-business-reality lens, with the specific evidence gaps above logged as the concrete conditions for moving past it.

---

## 7. Clean-Room Impact

Both passes were asked the same question independently — does this pass's evidence, or the target-design implications of the gaps it found, put any clean-room principle at risk — and both answered **no violation found or alleged**, while independently identifying the same underlying risk mechanism from different altitudes. This section reads both against the four clean-room principles fixed in the execution prompt (§8):

1. **Reference Only.** Both passes confirm every reference-system mechanism cited (branch fields, count-freeze wizard, product-category valuation gate, `type`/`is_storable`/tracking gating, purchase receiving) is reported strictly as reference-system business-semantic evidence. The Special Team pass states this explicitly: nothing was "proposed for adoption," consistent with Reference Only / No Copy-Clone-Reuse.

2. **No Copy / No Clone / No Reuse.** No source code, schema, or architecture was copied by either pass, and neither pass alleges a violation by any prior round in this chain. The Stockable/Consumable/Service target routing remains, in both passes' assessment, an undesigned, original open question rather than a cloned one.

3. **Migrate Business Facts + Business Semantics Only — not legacy application architecture.** This is where both passes converge on the actual risk, stated at different levels of resolution. The Council pass frames it conceptually: because the only concrete, detailed evidence available for Inventory's operational mechanics is Odoo's own source behavior read against a single 48-move company dataset, with zero real Thai user or SME evidence anywhere in the chain, Team B — once authorized — will face genuine pressure to reach for "what Odoo already does" (soft count-conflict, the global backdate toggle, document-level backdate granularity, the 3-way type/`is_storable` gate) as the de facto answer simply because it is the only concrete pattern in front of them, not because it was derived from Thai business semantics. That would not be a code-copy violation, but it would quietly defeat the principle that SMEsPlus migrates business facts and semantics, not legacy application architecture — the reference behavior becoming the target design by default rather than by evidenced choice. The Special Team pass names the same risk as three concrete instances: (a) adopting either of the two conflicting Thai branch-field mechanisms without real-user confirmation; (b) adopting the source's soft-conflict count handling as the SMEsPlus default without testing it against real Thai warehouse practice; (c) defaulting Consumable/Service to "no stock ledger" without checking it against real Thai service-plus-parts and dropship-reseller business models. These are the same risk mechanism the Council pass names conceptually, made concrete — not a competing view.

4. **SMEsPlus Target Design Must Be Original.** Both passes treat closing the real-user-validation gap as a precondition for satisfying this principle going forward, not merely a business-fitness nicety: without independent Thai operating evidence to weigh against it, Odoo's mechanism is currently the only voice in the room for count-freeze, backdate governance, receiving controls, and the 3-way product-type gate.

One additional data point comes from the Special Team pass only, and is recorded here for completeness since it bears directly on clean-room compliance even though the Council pass did not address it: two explicit access boundaries were independently honored during that investigation. The Boss `bh_*`/`bhpro_*` source-learning exclusion was not touched or reopened, and the adjacent `ACCOUNT/` directory (the actual Odoo reference source checkout, belonging to a separate parallel session) was not read beyond the top-level directory listing already on record — even though doing so would have let that session verify the expiry/consignment modules directly. This is recorded as an affirmative compliance fact, not a gap.

**Conclusion:** No clean-room violation is found or alleged by either pass this round. The material risk both identify is upstream of copying — a default-by-absence risk to Principle 3, not a Principle 1/2 breach — and closing the real-user-validation gap this document documents is a precondition for clean-room-safe design of count-freeze, post-close governance, backdate granularity, receiving controls, and the Stockable/Consumable/Service gate, not merely a business-fitness improvement.

---

## 8. Item Classification Table

Classified per the CP-02 taxonomy fixed in the execution prompt: `CLOSED_WITH_EVIDENCE — DO NOT REASK`, `CARRY_FORWARD — NO MATERIAL DELTA`, `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS`, `CONFLICTING — REOPEN REQUIRED`, `UNKNOWN — STILL MATERIAL`, `SUPERSEDED — HISTORICAL ONLY`. Where an existing fingerprint ID from `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` already covers an item, it is reused (`INV-FP-*`). Genuinely new items surfaced this round are given a local `TBRAC-DELTA-*` reference pending PMO consolidation into the fingerprint index and deliverables `13`/`15`; these are **not** program-wide fingerprint IDs.

| Ref | Item | Classification | Raised by | Evidence |
|---|---|---|---|---|
| `INV-FP-03` | GRPA-H8/H3 — Thai branch dual-concept | `CLOSED_WITH_EVIDENCE` (architecture ruling) / `CARRY_FORWARD — NO MATERIAL DELTA` (real-user-validation residue) | Both, independently corroborated | IER-003 file 06; IDR-007 file 05; CORR-005 file 02; Boss ruling `997809d` |
| `TBRAC-DELTA-01` | Evidence-traceability: IER-003 TBRAC review + Boss ruling unreachable from controlling branch tree | `CONFLICTING — REOPEN REQUIRED` (chain-of-custody, not content) | Special Team only (new) | `git merge-base --is-ancestor` (both return NO against `audit/inventory-core-corr007b-3high-closure-010`); `git ls-tree -r` confirms absence |
| `TBRAC-DELTA-02` | Core stock-control mechanics (state machine, warehouse/location, adjustment/count/cutoff, cross-domain handoff) — source-proven vs. Thailand-proven | `UNKNOWN — STILL MATERIAL` | Council explicit; Special Team's overarching finding corroborates | A11 closing section: research "conducted entirely against generic Odoo business logic" |
| `TBRAC-DELTA-03` | Representativeness of the single examined dataset (48-row `stock_move`, 2 states, 1 company) | `UNKNOWN — STILL MATERIAL` | Both, independently | IER-003 file 06 / 09 (dump re-verification) |
| `N-A5-02` | Expiration/lot-expiry handling (`product_expiry`) | `CARRY_FORWARD — NO MATERIAL DELTA` | Both, independently | A5 §8; A14; IDR-007 file 06 ("No elevation") |
| `N-A5-03` | Owner/consignment stock workflow | `CARRY_FORWARD — NO MATERIAL DELTA` | Both, independently | A5 §10; A14; IDR-007 file 06 |
| `TBRAC-DELTA-04` | IDR-007 "No elevation" (Low severity) call on N-A5-02/N-A5-03 | `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS` | Council explicit; Special Team corroborating | Both question whether Low severity is an evidenced business-impact judgment or an absence-of-evidence default for Thai food/pharma/FMCG segments |
| `N-A7-01` | Count-freeze/conflict policy | `CLOSED_WITH_EVIDENCE` (source mechanism: soft-conflict only, no hard freeze) / `UNKNOWN — STILL MATERIAL` (Thai-fit design choice among 4 options) | Both, independently, strong corroboration | CORR-007B file 02, full method-body read (both passes) |
| `G-2` | Post-close correction governance asymmetry (Inventory's unaudited global toggle vs. Accounting's governed lock-exception) | `CONFLICTING — REOPEN REQUIRED` (practice conflict; regulatory fit unknown) | Council only | CORR-007B file 08 §9–10 |
| `G-3` | Backdate enforcement granularity, document- vs. line-level | `CARRY_FORWARD — NO MATERIAL DELTA` | Council only | CORR-007B file 15, Addendum-4 (open Team B action item) |
| `TBRAC-DELTA-05` | Purchase over-receipt control (no ceiling/block) | `UNKNOWN — STILL MATERIAL` | Both, independently | A8 §2, `_compute_qty_received()` |
| `SAAS-05` | Purchase approval-workflow modules | `CARRY_FORWARD — NO MATERIAL DELTA` (source acknowledged absent from volume, unchanged) | Both, independently | A10; confirmed absent by two independent module-landscape scans |
| `TBRAC-DELTA-06` | Damaged-goods receiving/warehouse exception category | `UNKNOWN — STILL MATERIAL` | Both, independently, strong corroboration | Direct text search across full chain, zero hits (run independently by both passes) |
| `INV-FP-13` | Stockable/Consumable/Service 3-way routing vs. Thai industry edge cases | `UNKNOWN — STILL MATERIAL` (shared boundary; deep-proof owned by deliverable `12`/Track 03) | Both, independently; Special Team adds `GRPA-M16` cross-reference | A5 §4; A8 §3; `GRPA-M16` (CORR-006 §5.4) |
| `INV-FP-05` | N-A13-02 — company ACL / tenant isolation | `CARRY_FORWARD — NO MATERIAL DELTA` (ORM-layer comprehensively evidenced; DB-backstop and `sudo()`-bypass audit gap carried to Track 07) | Special Team only (explicitly assigned re-extraction) | CORR-005 file 02, N-A13-02 row; A10 SAAS-03 |
| `TBRAC-DELTA-07` | N-A12-01 Thai costing-method dependency (TH-INV-03 → COA-G06) | `UNKNOWN — STILL MATERIAL` (unowned cross-track dependency) | Special Team only (new connection drawn this session) | A11 row TH-INV-03; CORR-007B N-A12-01 package (no TH-INV-03/COA-G06 mention found) |
| `GRPA-M19` | Thai district/sub-district address data → Inventory/delivery routing | `UNKNOWN — STILL MATERIAL` | Council only | A11 TH-INV-05; A14 GRPA-M19, unchanged since 2026-08-31 |
| `TBRAC-DELTA-08` | TBRAC real-user validation panel and named membership | `CARRY_FORWARD — NO MATERIAL DELTA` | Council explicit (citing founding control document); Special Team corroborating in substance | `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` §10 Administrative Red Flags, dated 2026-08-30, both items still open |

No item examined by either pass this round was found to be `SUPERSEDED — HISTORICAL ONLY`; that classification is considered and left unused for Track 02 this pass.

---

## 9. Material Questions and Open Risks Carried to Boss

### 9.1 Real-user validation and evidentiary foundation

- Is "REQUIRES REAL USER VALIDATION" a governance status with a real path to closure (an owner, a method, a date), or has it functioned as a permanent label that survives every correction round unchanged? On `INV-FP-03` specifically, it has passed through DR-002, IER-003, CORR-005, and every later round without a single step toward closure.
- A11 discloses that DR-002's research agents were never instructed to look for Thailand-specific Inventory logic, on the grounds that Thai customizations attach only to party/company/tax fields in the one available dataset. Was that scoping decision itself ever independently challenged, or has it silently defined "Thai reality" as "branch/tax fields only" for the whole chain, leaving the warehouse-operations layer entirely unexamined for Thailand-specific variation?
- If the entire operational-mechanics evidence base reduces to generic Odoo source plus one 48-move, single-company dump, on what evidentiary basis can any future Team B design-freeze package describe its count-freeze, backdate-governance, or receiving-control choices as fitting Thai SME or Thai enterprise operating reality, rather than simply fitting Odoo's own reference behavior?
- No real-user validation evidence exists or is scheduled anywhere in the Inventory Core Backbone chain, and TBRAC's own named membership remains unassigned per its founding control document — a standing, unremedied hold on any claim of Thai product readiness for Inventory.

### 9.2 Industry-dependent design gaps

- Was IDR-007's "No elevation" call on N-A5-02 (expiry) and N-A5-03 (consignment) an evidenced business-impact judgment against SMEsPlus's actual target-customer industry mix, or purely a default of "no contrary evidence exists to elevate" in the absence of any research having been done at all? If the latter, is Low severity itself an unverified assumption for the food/pharma/FMCG-distribution segments SMEsPlus intends to serve?
- Expiry-date tracking and owner/consignment stock handling are completely unresearched for Inventory and are plausibly high-materiality for real Thai vertical segments the product intends to serve; both should be scoped for dedicated research, not left at Low by default.

### 9.3 Design-policy items requiring Thai operational input

- Count-freeze policy (4 open options) and post-close correction governance (G-2 unaudited global toggle, G-3 document- vs. line-level backdate) are live Team B design inputs with zero Thai operational input gathered; absent that input, the risk is default adoption of Odoo's bare reference mechanism rather than an evidenced, original SMEsPlus control choice.
- G-2's unaudited, global, all-users backdate-bypass toggle sits opposite Accounting's fully governed, user-scoped, time-boxed lock-exception model within the same paired Account+Inventory backbone. Is this asymmetry acceptable given ordinary Thai statutory-audit expectations for a registered company, or does it need to be closed before any Inventory Gate decision — and which track/gate owns deciding that, given it touches both Accounting's control model and Inventory's design freeze?

### 9.4 Receiving and approval control gaps

- Purchase over-receipt has no evidenced ceiling/block, and the purchase-approval-workflow modules are an acknowledged black box absent from source entirely; any future migration of a customer that relied on those modules, or any design assumption about receiving controls, carries an unresolved risk.
- "Damaged goods" as a receiving/warehouse exception category has no evidence anywhere in the chain and should not be assumed adequately covered by the evidenced scrap/return mechanisms without a dedicated check.
- Thai district/sub-district address data reaching Inventory/delivery routing (`GRPA-M19`) remains fully unknown and untouched since 2026-08-31.

### 9.5 Cross-track dependencies and governance

- `TH-INV-03` (Thai costing-method/valuation-presentation requirement) was explicitly deferred by DR-002's own A11 register to `COA-G06` over two days ago; `COA-G06` remains not closed and no CORR-007B `N-A12-01` deliverable names this dependency. Is `COA-G06` actually scheduled to produce this specific answer, or has the dependency itself been lost between the Inventory and Account reopen tracks, the same way the IER-003/ruling files were lost between branches?
- The IER-003 TBRAC review and the Boss scope ruling are both cited accurately throughout this chain but are physically unreachable from the CORR-007B branch tree this reopen is told is controlling — should CORR-007B (or this reopen's own package) be required to carry forward a verbatim copy or a resolvable pointer of both documents before Boss treats the branch-dual-concept closure as durable, rather than relying on a chain of paraphrase? (Track 01 ownership — flagged, not resolved, here.)
- `N-A13-02`'s residual `sudo()`-bypass code-path audit across `stock_account`/`sale_stock`/`purchase_stock`/`mrp` has not yet been performed (Track 07 ownership) and is load-bearing for real multi-branch/multi-company Thai tenant trust.

---

## 10. Recommendation

Both the Council pass and the Special Team pass recommend **HOLD** to Boss's Gate decision process, independently reached and mutually corroborating. This is a recommendation, not a decision: per Charter §6 and §10, Boss alone makes the final Gate call. Track 02 recommends that Boss treat the following as the concrete conditions for moving past HOLD, drawn from both passes' convergent and unique findings (§4, §8, §9):

1. Assign real-user validation ownership, method, and timeline for the Thai branch dual-concept, count-freeze policy, and backdate-granularity questions — the standing gap since the program's 2026-08-30 founding control document.
2. Scope dedicated research (not a re-read of the existing dataset) for expiry/lot tracking (N-A5-02) and consignment stock (N-A5-03) against Thailand's food, pharma, cosmetics, and FMCG-distribution segments.
3. Resolve, via Track 01, the evidence-traceability gap between the CORR-007B controlling branch and the IER-003/Boss-ruling documents it depends on but cannot reach.
4. Route the G-2 post-close governance asymmetry and the N-A12-01 → TH-INV-03 → COA-G06 dependency to their owning tracks (Track 06, jointly with Track 07 for N-A13-02) with an explicit owner, rather than leaving them unaddressed by any current deliverable.
5. Carry the Stockable/Consumable/Service Thai edge cases (service+parts combos; stocked-vs-drop-shipped SKUs; dropship resellers) into deliverable `12` as named test cases, not general awareness.

---

## 11. Closing Statement

This document is a Council challenge and Special Team investigation finding, converged for Boss's Gate decision. It is **not** a Gate PASS declaration, and it does **not** authorize Team B, Team C, Development, Account Reopen, or the Account × Inventory Joint Reopen. Consistent with the execution prompt's Final Stop Instruction and the Charter's core control statements — `No Evidence = No Progress`, `Never Skip Gate`, `Boss = Sole Final Approver`, `No Material Unknown Exhaustion = No Inventory Evidence Gate PASS` — Track 02's reconciled verdict is recorded here as **HOLD / EVIDENCE REQUIRED** for Boss's consideration alongside the other eight Veto tracks and their Special Team mirrors. Next action is PMO consolidation of this track's findings into deliverables `02`, `12`, `13`, `15`, and `20`, and Boss's own Gate decision — not further action by this track alone.

---

## Sources

Primary inputs: (1) Council Challenge findings, Track 02 (TBRAC), produced independently and blind to the Special Team pass, per Charter §8; (2) Special Team Investigation findings, Track 02 (TBRAC mirror), produced independently and blind to the Council pass, per the same rule. Both are preserved in full in §5 and §6 above and are available in their original structured form on request. Governance and format grounding, read directly by this consolidation pass: `NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md`; `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`; `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` (source of `INV-FP-03`, `INV-FP-05`, `INV-FP-13`, and the header/taxonomy conventions followed here).
