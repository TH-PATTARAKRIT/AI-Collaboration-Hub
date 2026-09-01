# Inventory Full Reopen — Financial / Accounting / Tax / Statutory VETO Findings (Track 06): Financial Truth, Posting, Period, AR/AP, Tax, Reporting & Statutory Evidence

Session: `SMEPLUS-26-09-02-INV-REOPEN-001`  
Jira: `ERPPLUS-139`  
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`  
Canonical Branch: `SMEsPlus`  
Execution Branch: `audit/inventory-reopen-2026-09-02-inv-reopen-001`  
Execution Worktree: `INVENTORY_REOPEN_2026_09_02_EXECUTION`  
Deliverable: `08_FINANCIAL_ACCOUNTING_INTERFACE_VETO_FINDINGS.md` — CP-03 (9 Veto Challenge Council) + CP-04 (9 Special Team Challenge) convergence output for Track 06  
Mandate / Track: `Track 06 — Financial / Accounting / Tax / Statutory VETO` (Financial truth, posting, period, AR/AP, tax, reporting, statutory evidence)  
Control Level: `/L999.999`  
Status: `CP-03 / CP-04 OUTPUT — FINANCIAL / ACCOUNTING / TAX / STATUTORY COUNCIL CHALLENGE + SPECIAL TEAM INVESTIGATION COMPLETE — TRACK 06 VERDICT: HOLD / EVIDENCE REQUIRED — NOT A GATE DECISION`

This document does not close, pass, or authorize anything. It converges two findings sets produced independently and blind to each other, per the Nine Veto Council & Special Team Charter's Anti-Groupthink Rule (§8: *"Fresh Council findings must not be shown to other Council mandates before their first pass where practical"*) and Core Control Statement (§10: *"Special Team investigates; Council challenges; PMO preserves; Boss decides."*). This document performs the PMO-preservation function for Track 06 only: it holds both findings sets faithfully, surfaces where they corroborate and where their coverage diverges — including the one point where they reach opposite conclusions on the same specific question — and hands the combined evidence to Boss. It does not vote, does not pick one set over the other, and — per Charter §6, *"Neither the Council nor Special Teams decide by majority vote... Boss alone makes final business / Scope / Gate / override decisions"* — it does not decide anything on Boss's behalf.

Both inputs converged here were themselves already-completed, independent passes produced blind to each other per the Anti-Groupthink Rule; this document does not re-run their underlying source/code research, though it reproduces the primary-source file/line citations each pass itself made, verbatim, for traceability. Claims below are attributed to "the Council pass" or "the Special Team pass" as reported by each, with their own citations preserved. Header fields, deliverable numbering, taxonomy vocabulary, and cross-track fingerprint IDs (`INV-FP-*`, `G-*`) are verified directly against `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md`, `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md`, and `NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md`, each read directly by this consolidation pass.

---

## 1. Executive Summary

Two independent passes examined the same Inventory Core Backbone evidence chain (DR-002 → IER-003 → CORR-005 → IDR-007 → CORR-006 → CORR-007A → CORR-007B), concentrated on `N-A12-01` (`INV-FP-09`) and the wider Financial/Accounting/Tax/Statutory mandate boundary — financial truth, posting, period, AR/AP, tax, reporting, and statutory evidence — without visibility into each other's findings:

- The **9 Veto Challenge Council, Track 06**, running a first-pass independent challenge plus its own primary-source spot-verification, reached verdict **HOLD**.
- The **9 Special Team Challenge, Track 06 mirror**, running a deeper primary-source investigation over the same evidence base plus targeted new research into previously-unexamined checklist items, reached verdict **HOLD**.

Both verdicts converge without conflict at the track level: neither had to be picked over the other. Where the two passes examined the same ground, they substantially corroborate each other — both independently re-verified, character-for-character, the same load-bearing CORR-007B citations (the Perpetual/Periodic posting gate, Product Category's ownership of valuation policy, the absent year-end retained-earnings closing entry), and both independently identified manufacturing valuation and landed/additional cost as genuine, previously-unexamined blind spots across nine prior evidence rounds. This is a meaningfully stronger evidentiary position than either pass alone, and on every citation independently re-checked by both passes this round, the prior evidence chain held up exactly as claimed — no fabrication was found.

This round also surfaced **one direct, explicit disagreement** between the two blind passes on a single specific question, which this document does not paper over: the cost basis at which returned stock re-enters inventory. The Council pass, working from the CORR-007B evidence package, found this untraced anywhere in the chain and listed it as an open, unevidenced risk. The Special Team pass went further and independently traced the actual mechanism (`_get_value_from_returns()`) at primary source, and reports it confirmed, well-designed, and closed. Section 4.4 states both positions in full and explains why they differ; the Item Classification Table (§8) carries this item as `CONFLICTING — REOPEN REQUIRED` so Boss sees the disagreement rather than a silently-merged answer.

Beyond that one conflict, coverage differs materially. The Council pass alone identified that the reference system's own field label ("Perpetual (at invoicing)") does not describe its actual posting trigger (stock-move validation, not invoice posting) and reframed the Inventory-side lock-date bypass (G-2) as a statutory internal-control weakness, not merely a UX gap. The Special Team pass alone traced the actual AR/AP-to-Inventory valuation bridge — core mandate territory neither the Council pass nor any prior round had examined — and, from it, derived a concrete new mechanism by which a vendor bill posted after a period closes can silently alter that period's recomputed stock value without correcting the posted closing entry; it also independently re-confirmed G-7 (the empty `stock_valuation_report.py` PDF/XLSX export stub methods).

Neither pass found any clean-room violation, any fabricated evidence, or any basis for `FAIL / FROZEN`. Both independently reconfirm that `N-A12-01` remains a HIGH FUNCTIONAL DESIGN GAP and that the `Account + Inventory Backbone Reference Baseline` remains HOLD; both independently confirm that G-5 (migration-cutover opening-balance cross-proof) and the statutory half of G-6 (year-end retained-earnings entry design) cannot be closed by any further Inventory-only work, because the parallel Account/COA backbone track has not closed `COA-G04` through `COA-G08`.

**Reconciled Track 06 verdict: `HOLD / EVIDENCE REQUIRED`.**

This document does not declare Gate PASS. It does not authorize Team B, Team C, Development, Account Reopen, or the Account × Inventory Joint Reopen. It is a challenge-and-investigation finding for Boss's Gate decision, prepared per Charter §10: *"Boss = Sole Final Approver."*

---

## 2. Checkpoint Records

| Field | CP-03 — 9 Veto Challenge Council, Track 06 | CP-04 — 9 Special Team Challenge, Track 06 mirror |
|---|---|---|
| Checkpoint | `CP-03` | `CP-04` |
| Result | `HOLD` | `HOLD` |
| Evidence | Independent first-pass challenge against the full CORR-007B execution set (files 01–16) on branch `audit/inventory-core-corr007b-3high-closure-010`, concentrated on `N-A12-01`, plus three primary-source spot-verifications performed directly against the reference Odoo source tree on local disk — not against CORR-007B's prose alone. Produced blind to Track 06's Special Team pass and to the other 8 Council tracks. Full findings in §5. | Deeper primary-source investigation over the same evidence chain: independent re-performance of the Council-cited citations directly against the reference Odoo source tree, then targeted new research into checklist items no prior round had examined — manufacturing valuation handoff, landed/additional cost concepts, the Stockable/Consumable/Service routing hypothesis, and the AR/AP-to-Inventory valuation bridge. Produced blind to Track 06's Council pass. Full findings in §6. |
| AI Audit SMEsPlus Impact | Directly informs deliverable `12` (Stockable/Consumable/Service deep proof) via the Perpetual-path corroboration; deliverable `14` (Accounting Dependency Register) via G-5/G-6/`GRPA-M18-D`; Track 01 (Audit VETO) via the branch-currency basis both passes relied on; Track 08 (Clean-Room) via §7 below. | Directly informs deliverable `12` via the definitive two-field routing mechanism; deliverable `14` via the new AP-bridge/late-bill mechanism and the manufacturing-WIP automation gap; Track 01 via the same branch-currency finding, independently reached; Track 04 (IDTM) / Track 05 (IESA) via the incidental `G-7` re-confirmation. |
| % Board | `TBD — BASELINE REQUIRED` (no board/tracker reference available to this consolidation pass) | `TBD — BASELINE REQUIRED` |
| % STATE | `TBD — BASELINE REQUIRED` | `TBD — BASELINE REQUIRED` |
| % STEP | `TBD — BASELINE REQUIRED` | `TBD — BASELINE REQUIRED` |
| Open Risks | See §9 (Material Questions and Open Risks) and §8 (Item Classification Table) — none rise to `FAIL / FROZEN`; all are material enough to sustain `HOLD` per Charter §6 (*"A single material Veto may be enough to place a Prompt on HOLD if evidence supports the concern"*). | Same register, §9/§8 — the return/reversal conflict (§4.4) and the AP-bridge/late-bill mechanism are additionally flagged as this pass's own new material this round. |
| Next Action | PMO consolidation into deliverables `02`, `12`, `13`, `14`, `15`, `20`; Boss Gate decision. | Same. |

---

## 3. Track Verdict — Reconciled

| Source | Verdict | Reached |
|---|---|---|
| Council Challenge (CP-03) | **HOLD** | Independently, blind to Special Team |
| Special Team Investigation (CP-04) | **HOLD** | Independently, blind to Council |
| **Reconciled Track 06 verdict** | **HOLD / EVIDENCE REQUIRED** | Both converge on the track-level verdict; one item-level conflict identified and preserved, not arbitrated (§4.4, §8) |

Neither track-level verdict was selected over the other — both independently landed on HOLD from independent readings of the same underlying chain, which is the strongest form of convergence available under the Charter's Anti-Groupthink Rule (§8): two blind passes agreeing is evidence the HOLD is well-founded, not an artifact of one pass anchoring the other.

This convergence is not, however, total agreement on every question inside the mandate. On one specific, narrow question — return/reversal cost-basis treatment — the two passes reached opposite positions (§4.4). This does not change the track-level verdict, because neither position, taken either way, would move the overall track past HOLD: the Council's position (unevidenced, open risk) is itself a HOLD-supporting finding, and the Special Team's position (confirmed, no gap) simply removes one item from the open-item list without resolving `N-A12-01`'s other, larger open items (G-5, G-6's statutory half, and the newly-surfaced manufacturing-valuation and landed-cost gaps). Per the Charter's No Majority Vote rule (§6: *"A single material Veto may be enough to place a Prompt on HOLD if evidence supports the concern"*), this document does not average, vote, or silently pick a side on the return/reversal question — it carries both positions forward explicitly and lets the HOLD stand on its many other, uncontested legs.

Nothing in either pass rises to `FAIL / FROZEN — MATERIAL EVIDENCE / GOVERNANCE / CLEAN-ROOM FAILURE`. Both passes are explicit that the existing evidence chain is disciplined, that its citations held up exactly as claimed under independent re-verification, and that its own gaps are honestly labeled rather than concealed or converted into false facts.

---

## 4. Convergence, Corroboration, and Coverage Reconciliation

Per Charter §5 (Direct-to-Boss Rule: *"If a material finding is suppressed from Boss because it is inconvenient, that is a governance control failure"*), this section states plainly what both passes found together, what each pass alone found, and — unlike every other track converged so far in this reopen — the one place the two passes directly disagree.

### 4.1 Convergent findings — independently corroborated by both blind passes

| Item | Council conclusion | Special Team conclusion |
|---|---|---|
| N-A12-01 primary-source citations | 3 load-bearing citations independently spot-verified character-for-character (`stock_move.py:630-638`; `product.py:666-670`; `company.py:177,823,847`) — all matched exactly | 4 citations independently re-verified (periodic/real_time field; `action_close_stock_valuation()`; the posting gate; the `ProductCategory` class boundary) — all matched CORR-007B files 03/08/09/13/15/16 exactly |
| Standing N-A12-01 disposition | `HIGH FUNCTIONAL DESIGN GAP`; `Account + Inventory Backbone Reference Baseline = HOLD` — reaffirmed | Same — "CONFIRMED, not weakened or strengthened by this round" |
| Absent year-end retained-earnings closing entry (G-6 negative finding) | Independently re-derived via filesystem search (no closing wizard/action found) + direct read of `get_unaffected_earnings_account` | Same finding, same citations, cross-referenced against `account_reports/models/account_report.py` |
| G-5 opening-balance cross-proof blocked on the parallel Account track | Structurally blocked pending `COA-G04..G08` closure | Same blocker, tied explicitly to governing ruling `47018139` and the Full Reopen Program `42e04e63` |
| Manufacturing valuation/COGS handoff is a genuine, previously-unexamined blind spot | Zero evidence anywhere; `mrp_account` has zero citations in CORR-007B's own SHA-256 manifest | Confirms the blind spot, then independently produces primary-source mechanism evidence for it this round |
| Landed/additional cost concepts are a genuine, previously-unexamined item | Confirmed to exist but functionally untraced | Confirms the existence finding, then independently traces the FIFO/AVCO-only rule, split methods, and lock-date safety this round |
| Stockable/Consumable/Service (`INV-FP-13`) posting-gate relevance | `is_storable` AND-condition inside the verified posting gate supports the Perpetual-path routing hypothesis | Confirms as a hard, 2-field gate (`type` + `is_storable`), correcting an assumed 3-way-enum field model |
| `GRPA-M18-D` disposition unchanged | Handed off to Accounting/Tax by CORR-007A; receipt not independently confirmed | `CONTROLLED CARRY-FORWARD TO ACCOUNTING/TAX`, `HIGH REMAINS`, unchanged |
| G-2 asymmetric governance mechanism | Independently confirms the mechanism, then reframes it in statutory internal-control-weakness terms | Independently confirms the identical mechanism and facts |

### 4.2 Findings raised only by the Council pass

The Special Team's findings do not address these; they are carried forward here in full rather than absorbed into the shared list:

- The reference field's own label ("Perpetual (at invoicing)") not matching its actual code trigger (`_action_done()` — a physical stock-move event, not a billing event) — the revenue/COGS timing-matching risk this creates (`FIN-DELTA-03`, below).
- G-2's explicit reframing in statutory internal-control-weakness terms — the Special Team pass confirms the identical underlying mechanism and facts but does not itself apply this specific framing.
- The procedural question of whether the Account-domain reopen track has actually logged or accepted receipt of the `GRPA-M18-D` hand-off, as distinct from the item's own disposition (which both passes agree is unchanged).

### 4.3 Findings raised only by the Special Team pass

The Council's findings do not address these; they are equally carried forward in full:

- `G-7` (the empty `stock_valuation_report.py` PDF/XLSX export stub methods, `INV-FP-10`) independently re-performed and reconfirmed this round — not touched by the Council pass's material this round.
- The AR/AP-to-Inventory valuation bridge (`purchase_stock._get_value_from_account_move`) — core mandate territory examined by neither the Council pass nor any prior evidence round, despite AR/AP being named explicitly in this track's own mandate boundary.
- The derived late-posted-vendor-bill-vs-closed-period risk — the first concrete mechanism given for the previously-abstract G-1 sequencing risk.
- The return/reversal valuation trace that produces the §4.4 conflict (see below).
- The evidence-currency observation that every citation this track relies on this round lives only on the unmerged branch `audit/inventory-core-corr007b-3high-closure-010` (tip `0eb78c68`), with canonical `origin/SMEsPlus` carrying zero footprint of CORR-006/007A/007B — and this pass's own response of re-verifying directly against the reference Odoo source rather than trusting branch prose alone.
- A precise, immaterial citation-range note: CORR-007B file 08 cites `_should_create_account_move()` as lines 630–635, where the method body actually runs 630–638 (matching the Council pass's own independently-confirmed range). Flagged for completeness, not as a finding of concern.

### 4.4 The one explicit disagreement between the two passes

Both passes independently examined whether stock returning to inventory — a customer return, specifically — re-enters at its original outbound cost or as a new layer at current cost under FIFO/AVCO, a question with direct margin and COGS-restatement consequences on any SKU with material return volume. They reached opposite conclusions, and this document states both in full rather than resolving the disagreement on its own authority.

**The Council pass's position**, stated as an open, unevidenced question: return/reversal cost-basis treatment "is not traced anywhere in the chain. It logically flows through the same posting gate as any move, but which value it carries — with real margin/COGS restatement consequences — is unproven." Its own item classification for this question is `HOLD`, with the evidence noted as "inferred only structurally... not directly traced."

**The Special Team pass's position**, stated as a confirmed, closed finding: having specifically set out to test this question — its own findings frame it as "an initial hypothesis I was testing" — it read the full method body of `_get_value_from_returns()` at `stock_account/models/stock_move.py:463-472` and found that a customer return is priced at the original delivery move's pro-rated cost via `origin_returned_move_id`, not a fresh current-cost layer. Its own words: "CONFIRMED well-designed, correcting an initial hypothesis I was testing... no gap found here." Its item classification for this question is `STABLE`.

Both positions are accurate accounts of what each pass actually did. The Council pass, working from the CORR-007B evidence package plus three of its own spot-verifications concentrated on `N-A12-01`'s central citations, did not itself trace `_get_value_from_returns()` and correctly declined to assert a conclusion it had not evidenced. The Special Team pass, tasked with deeper primary-source investigation, went and traced it. Because the two passes were run blind to each other per the Charter's Anti-Groupthink Rule (§8), neither had the opportunity to reconcile with the other before this document was assembled.

This document's own judgment, offered to Boss rather than substituted for Boss's decision: the Special Team's finding is the more probative of the two on this specific narrow question, because it rests on an actual traced method body with a file and line citation, not an inference. Boss may reasonably treat the return/reversal cost-basis question as substantively answered by that citation. But this document does not unilaterally close it, for two reasons stated plainly. First, closing a Council-flagged open item on the strength of a Special Team citation the Council pass has not itself reviewed and had the chance to challenge would bypass the Council's own review-of-Special-Team-findings function (Charter §2: "reviewing Special Team findings" is a named Council responsibility, not yet exercised here for this specific item). Second, and more simply, the taxonomy exists precisely for this situation. The Item Classification Table (§8) below carries this item as `CONFLICTING — REOPEN REQUIRED`, not as closed, so the disagreement itself — not just its likely resolution — reaches Boss.

### 4.5 Reading this reconciliation

No other direct factual contradiction was found between the Council pass and the Special Team pass on any item both examined — where they overlap elsewhere, they corroborate, in several cases down to the identical file and line citation. The divergence elsewhere is one of coverage breadth and depth, produced naturally by the Anti-Groupthink Rule's design (two blind passes will not sample the same evidence identically, and a Special Team's deeper-investigation mandate will sometimes finish tracing something a first-pass Council challenge correctly left open) — not a disagreement to be adjudicated by this document. Boss should treat the union of §4.1–§4.4 as the operative Track 06 evidence base, not either pass in isolation, and should treat §4.4 specifically as the one place this round where the two passes' outputs cannot simply be unioned without a decision.

---

## 5. Detailed Findings — Council Challenge (CP-03)

### 5.1 Method and primary-source spot-verification

The Council pass conducted an independent, first-pass challenge of the Inventory Full Reopen evidence against this mandate's single boundary: financial truth, posting, period, AR/AP, tax, reporting, and statutory evidence. Per the Charter's Anti-Groupthink Rule, it was formed without visibility into the Special Team pass for this same track. Primary review concentrated, as directed, on `N-A12-01` (`INV-FP-09`) — the one live, unresolved pure-Inventory High item — using the full CORR-007B execution set (files 01–16) on branch `audit/inventory-core-corr007b-3high-closure-010`.

Beyond reading, the Council pass performed targeted primary-source spot-verification against the actual Odoo reference tree on local disk, checking three separate load-bearing citations character-for-character against the live source files rather than against CORR-007B's own prose:

| Citation | File and location | Result |
|---|---|---|
| `_should_create_account_move()` posting gate | `stock_account/models/stock_move.py:630-638` | Matched exactly |
| `property_valuation` field and its "Periodic (at closing)" / "Perpetual (at invoicing)" selection labels | `stock_account/models/product.py:666-670` | Matched exactly |
| `get_unaffected_earnings_account`, `account_opening_move_id`, and the "Profit or Loss Appropriation" mechanism | `account/models/company.py:177, 823, 847` | Matched exactly |

All three matched the CORR-007B package's citations exactly, including line numbers. This is a meaningful positive finding in its own right, independent of anything else in this report: the evidence this track inherited is not being taken on faith, and on the sample checked it is accurate, not fabricated or embellished.

### 5.2 N-A12-01: the standing evidence reaffirmed, not weakened or strengthened

The standing governance disposition (deliverable `13`'s Revised Functional Design Disposition) is correct and should not be disturbed: `N-A12-01` remains a HIGH FUNCTIONAL DESIGN GAP, and `Account + Inventory Backbone Reference Baseline = HOLD`. The Council pass found the technical evidence underneath it substantially more thorough than the governance layer's own "NOT PROVEN" labels suggest at first read — a prior cross-reference table correctly resolves that apparent tension by distinguishing "no functional-design decision has been made" (true, and correctly still open) from "no evidence exists" (false for the majority of the item's own sub-items). The Council pass independently confirms that distinction is accurate rather than a convenient reframing.

The mechanism proof itself is sound and worth restating in financial terms. Accounting and Inventory share configuration state on `res.company` and `product.category` but do not call into each other — Accounting's lock-date wizard never triggers a stock valuation closing, and the closing mechanism never checks whether the fiscal year is locked. Inventory's own enforcement is a correct one-way consumer of Accounting's lock-date contract, which is the right shape for a boundary that should not let Inventory silently own Accounting. The per-move GL-posting gate is a single boolean condition — storable, valued, has a valuation account, non-zero quantity, and `product.valuation == 'real_time'` — and it is this same gate, not a separate mechanism, that separates Perpetual (immediate per-move posting) from Periodic (deferred to a closing that true-ups physical value against GL value). Product Category, not company or product, is the class-verified owner of both the valuation-timing and cost-method policy, with company-level fallback only. All of this is now proven from source, not merely asserted, and the Council pass found no basis to doubt it.

### 5.3 The sharpest finding: no year-end retained-earnings closing entry (G-6)

The single most consequential finding in the entire package, from this mandate's specific lens, is G-6: no source-evidenced journal entry anywhere in the reference system transfers Income/Expense balances to a Retained Earnings account at fiscal year-end. Odoo computes the unaffected-earnings figure as a live reporting rollup instead of a posted closing entry. The Council pass independently re-derived this by searching the source tree for any fiscal-year-closing wizard or action (none found) and by tracing `get_unaffected_earnings_account` directly — the negative finding holds.

The Council pass sharpens rather than softens how this should land with Boss: this is a genuine divergence between common statutory book-closing practice — including Thai practice, where an auditable year-end transfer of net profit/loss to retained earnings is a normal expectation of a closed set of books — and the reference system's own design choice to treat it as a report-time computation. SMEsPlus should not treat Odoo's absence of a closing entry as evidence that one is unnecessary. It is evidence that Odoo solved the reporting need differently, not evidence that Thai statutory practice does not need a discrete, auditable entry. Whether SMEsPlus needs one is correctly logged as a new SMEsPlus functional design decision, not an inherited default — but the point belongs on the record explicitly.

### 5.4 Two new blind spots: manufacturing valuation and landed cost

Two items in this mandate's checklist — manufacturing valuation/COGS handoff and landed/additional cost concepts — have essentially no prior scrutiny anywhere in the nine-round evidence chain, confirmed by direct check rather than by absence of citation alone.

The manufacturing-accounting bridge module `mrp_account` exists in the reference source (confirmed on disk, alongside `mrp_subcontracting_account` and related modules), yet it produces zero hits in CORR-007B's own SHA-256 evidence manifest, and DR-002's own manufacturing handoff research (A8) explicitly scoped itself to the physical raw-material/WIP/finished-goods movement primitives, not their valuation or GL-posting behavior. At present there is no evidence anywhere in this project of how component cost rolls into finished-goods value, how standard-cost variance on manufactured items is absorbed, or whether `mrp_account` follows the same `stock_account` posting gate or a separate one.

Landed cost is in a narrower but related state: `stock_landed_costs` and its dump table `stock_valuation_adjustment_lines` are confirmed real and were checked once, specifically to rule out a legacy-orphan-column false positive — but no file has traced how a landed-cost document actually allocates additional cost across a receipt's valuation or what account movement results.

Both are legitimate candidates for Special Team deep-dive before either can be called even source-mechanism-proven, let alone ready for Team B design — and, as §6.3–§6.4 below show, the Special Team pass took up exactly that work this round and materially advanced both.

### 5.5 A label that does not match its own trigger

The reference field's own label — "Perpetual (at invoicing)" — does not describe its own trigger, which the Council pass independently confirmed by direct read of `_action_done()` fires on stock-move validation, a physical goods-movement event, not on customer/vendor invoice posting, a billing event. This is a revenue/COGS timing-matching risk (delivery-time value recognition versus invoice-time revenue recognition) that SMEsPlus's own clean-room design must resolve explicitly rather than silently inherit the reference label's implication. If SMEsPlus's design intends inventory value/COGS recognition to track delivery rather than billing, that is a legitimate choice — but it must be a stated design decision, not an inherited label.

### 5.6 G-2 reframed: an internal-control question, not only a UX gap

G-2 — Inventory's single global, unaudited `stock_account.skip_lock_date_check` bypass, set against Accounting's granular, audited `account.lock_exception` — is not only a Team B UX decision as currently filed. From a Financial/Statutory lens it is an internal-control weakness. Any bypass of a posting-period cutoff that has no user attribution, no reason, and no expiry would not survive ordinary statutory audit-trail scrutiny if carried into SMEsPlus as-is.

### 5.7 Sequencing, hand-off, and the shared-boundary corroboration

G-5 (migration-cutover opening-balance cross-proof) and G-6's statutory half (year-end retained-earnings entry design) are not merely "awaiting Accounting evidence" in the abstract — they are structurally blocked because the parallel Account/COA backbone track has not closed `COA-G04` through `COA-G08` (per this session's own governance context: `COA-G01`/`G02` closed, `COA-G03` self-reported but not yet independently audited, `COA-G04..G08` not closed at all). Even a perfect Inventory-side answer cannot close these until the Account track advances. This is a cross-track dependency the Boss Gate should see explicitly, not a residual Inventory-side gap.

Separately, `GRPA-M18-D` (Thai WHT/PND3/PND53 monthly-filing obligation, `INV-FP-06`) was formally handed off from Inventory to "Accounting/Tax" scope by CORR-007A, but nothing in the evidence available to the Council pass confirms the Account-domain reopen track has actually logged or accepted receipt of that item. A hand-off without a confirmed receiving owner is not yet a closed hand-off.

Finally, the `is_storable` condition inside the already-verified `_should_create_account_move()` gate is direct, already-evidenced support for the Perpetual-path routing hypothesis under `INV-FP-13` (non-storable products structurally cannot receive a per-move GL posting). This does not close `INV-FP-13` — the Periodic path and Service-type behavior specifically remain untested — but it is new synthesis this pass contributed, not a restatement.

### 5.8 Council's recommendation

The Council pass recommends **HOLD**, not READY and not FAIL_FROZEN. The evidence base for `N-A12-01` is not broken, dishonest, or in need of discarding — on the sample independently verified, it is accurate and unusually well self-audited. The reason for HOLD is that this mandate's material question — whether Inventory exposes correct business facts without silently owning Accounting, and which cost/timing matters remain genuinely Account-dependent — is not yet fully answered: two checklist items (manufacturing valuation, landed cost mechanism) have essentially no evidence at all, one (return cost-basis) is unproven per this pass's own review, and two of the six named gaps (G-5, G-6's statutory half) are structurally blocked on a parallel track's own incompleteness. Special Team investigation is warranted specifically on manufacturing valuation and landed-cost mechanism proof; the remainder are correctly Team B/Accounting design questions once authorized, not further Inventory-only evidence-gathering.

---

## 6. Detailed Findings — Special Team Investigation (CP-04)

### 6.1 Method, scope, and the evidence-currency basis for this track

The Special Team pass conducted an independent deep investigation of the Inventory-to-Accounting financial interface, within the same strict mandate boundary, deliberately not exercising Accounting design ownership and not selecting any policy Team B must choose. Method: primary-owned deep review of `N-A12-01` using the CORR-007B evidence chain on branch `audit/inventory-core-corr007b-3high-closure-010` (tip `0eb78c68`), followed by independent re-performance of that chain's most load-bearing citations directly against the reference Odoo source tree, and then targeted new research into checklist items this reopen's own prior-evidence index flagged as genuinely unexamined: manufacturing valuation handoff, landed/additional cost concepts, and the Stockable/Consumable/Service financial-routing hypothesis. No canonical question already marked `CLOSED_WITH_EVIDENCE` was re-litigated absent a concrete reason.

One context finding is worth stating plainly because it explains this pass's own method: every primary-source citation this track relies on this round — CORR-007B files 03, 08, 09, 13, 15, 16 — lives only on the unmerged branch `audit/inventory-core-corr007b-3high-closure-010` and its ancestors; canonical `origin/SMEsPlus` has zero footprint of CORR-006, CORR-007A, or CORR-007B, not even a prompt file (consistent with Material Finding F-01 in deliverable `01`). The Special Team pass's response to that currency gap was to independently re-verify the load-bearing citations directly against the reference Odoo source itself, not merely against CORR-007B's prose — and this document treats that re-verification, not blind trust in branch prose, as this pass's actual evidentiary basis.

### 6.2 N-A12-01 and G-7 independently re-verified

The standing disposition was independently re-verified rather than taken on faith. The Special Team pass read `stock_account/models/res_company.py`, `stock_account/models/stock_move.py`, and `stock_account/models/product.py` directly and confirmed, line-for-line, the citations CORR-007B's files 03, 08, 09, 13, 15, and 16 rest on: the `inventory_valuation` selection field (periodic/real_time) and `inventory_period` cadence field on `res.company`; `action_close_stock_valuation()`'s guard against back-dated closings and its three-source aggregation; the exact per-move posting gate `_should_create_account_move()`; and the `ProductCategory` class boundary, confirming Product Category — not company, not product template — is the real configuration owner, with company-level fallback only.

`G-7` (`INV-FP-10`, the empty `action_print_as_pdf`/`action_print_as_xlsx` stub methods on `stock_valuation_report.py`) was independently re-performed and confirmed verbatim: both methods are literal no-op `return` bodies, at lines 140-144 of the reference file. This item is formally owned by Track 04 (IDTM) / Track 05 (IESA) per the fingerprint index; it is noted here only because it surfaced incidentally during this pass's own N-A12-01 sweep, and Track 06 should not treat it as newly its own to close.

Nothing in this independent re-performance contradicts or weakens CORR-007B's own conclusions on N-A12-01; the standing verdict — HIGH FUNCTIONAL DESIGN GAP; Account + Inventory Backbone Reference Baseline = HOLD — is unchanged, because its remaining open sub-items (G-1 sequencing, G-2 correction-governance asymmetry, G-5 migration-cutover cross-proof, G-6 absent year-end retained-earnings entry) are Team B design choices or Accounting-evidence dependencies, not missing citations.

### 6.3 New evidence: manufacturing valuation handoff

`mrp_account` (depends on `mrp`, `stock_account`) is the Accounting-Manufacturing bridge, structurally identical in shape to `stock_account` itself. Completed manufacturing-order output and component-consumption moves ride the exact same `stock.move` valuation gate already proven for ordinary receipts — confirmed via the `_get_value_from_production()` hook-override pattern, the same abstract-hook/concrete-override architecture governing every other valuation source in the reference system. In-progress manufacturing orders are different: their Work-In-Progress value is exposed to Accounting only through a wholly manual wizard, `mrp.account.wip.accounting`, which posts an accrual entry and automatically reverses it the next day — and the Special Team pass confirmed by direct search that no `ir.cron` record exists anywhere in the module. Unlike ordinary periodic stock valuation, which has a daily/monthly cron as an automatic safety net, manufacturing WIP has none: if nobody runs the wizard before a period locks, in-progress production cost is simply invisible to the GL for that period.

This is a real, newly-evidenced gap in the same shape as G-1, not previously named anywhere in the N-A12-01 register, and it is squarely a Team B design question — does SMEsPlus need an automated equivalent, and how does it sequence against the existing closing mechanism — not something this track can resolve.

### 6.4 New evidence: landed/additional cost concepts

`stock_landed_costs` (depends on `stock_account`, `purchase_stock`) restricts landed-cost allocation to FIFO/AVCO-costed products only — a hard, source-coded business rule (`UserError` for standard-cost products) — with three real allocation split-methods (by quantity, weight, volume) plus an equal split. The Special Team pass specifically tested whether landed-cost postings might bypass Accounting's lock-date protection, since no landed-cost-specific backdate check exists in the module; tracing `account.move._check_fiscal_lock_dates()` to its actual call sites in `write()`/posting (`account/models/account_move.py:2806`, called at `:3911`, `:3916`, `:3958`) confirmed that every `account.move`, including a landed cost's, is protected by the same generic Accounting-side lock-date enforcement — a confirmed-safe finding, not a gap, reported precisely rather than manufactured into a problem.

One precise, unresolved observation was also surfaced and should not be overstated either way: the code path that would apply a landed cost to a Periodic-valued product's standard-cost layer (a `standard_price` batch-update block inside `button_validate()`) is present in source but commented out (approximately lines 132-142). This needs one further targeted read before Team B can treat "landed costs update Periodic-valued layers" as fully proven.

### 6.5 New evidence: Stockable/Consumable/Service is a two-field gate, not a three-way enum

The Stockable/Consumable/Service financial-routing hypothesis (`INV-FP-13`) — flagged by this reopen's own prior-evidence index as one of the two genuinely open new-research items alongside N-A12-01 — was tested directly and confirmed as a hard-enforced source behavior, with an important terminology correction for Team B. The reference system does not have three peer `type` values; `type` has only `consu` (Goods), `service`, and `combo`. Storability is a separate boolean, `is_storable`, defaulting to false, and forcibly reset to false for any non-`consu` type by `compute_is_storable` (`stock/models/product.py:894-895`). Most decisively, `stock.quant.check_product_id()` is a hard ORM constraint — "Quants cannot be created for consumables or services" (`stock/models/stock_quant.py:583-585`) — whenever `is_storable` is false, meaning it is architecturally impossible in the reference system to create an on-hand-balance ledger row for a Service or a non-storable Goods product.

This directly confirms the routing hypothesis directionally (Stockable drives the Inventory Stock Truth ledger; Consumable and Service do not) while correcting the underlying field model Team B should design against — a 2-field gate, not a 3-way enum.

### 6.6 New evidence: the AR/AP-to-Inventory valuation bridge, and the risk it exposes

This track traced the actual AR/AP-to-Inventory valuation bridge, core mandate territory no prior round — and no other pass this round — had examined. `purchase_stock` overrides the base valuation cascade's accounting-document hook (`_get_value_from_account_move`, `purchase_stock/models/stock_move.py:153-219`) to derive receipt value from actual posted vendor bills — gated explicitly on `aml.move_id.state == 'posted'` and an as-of-date filter (`aml.date <= at_date`), correctly handling vendor credit notes (`in_refund`) as reductions, and apportioning billed value across multiple receipts against the same purchase order line to prevent double-counting. This is a real, well-designed, working mechanism.

Because it is a live recomputation rather than a frozen ledger, this pass also identified — as new evidence, not a fabricated risk — that a vendor bill posted after a period has already closed will silently change what a recomputed valuation shows for that closed period without correcting the already-posted closing journal entry; the true-up only surfaces at the next closing. This is a concrete mechanism explaining how the already-named G-1 sequencing risk can actually manifest financially, and it raises a genuine open question — whether SMEsPlus needs an explicit late-bill exception rule to satisfy Thai statutory period-integrity expectations — that only Team B jointly with Accounting/Tax can answer.

### 6.7 Return valuation traced and confirmed — see §4.4 for the resulting disagreement

This pass also confirmed that customer-return valuation is well-designed: returned goods re-enter inventory priced at the original delivery's pro-rated cost via `_get_value_from_returns()` (`stock_account/models/stock_move.py:463-472`), not at a fresh or arbitrary current cost — closing an open question this pass was itself testing, with a positive, no-gap finding. As §4.4 states in full, this directly contradicts the Council pass's position that this question is unevidenced; both positions are preserved rather than merged.

### 6.8 GRPA-M18-D carried forward, not re-derived this round

`GRPA-M18-D` (Thai PND3/PND53 monthly statutory filing/export) is explicitly named as this track's own carried item in the reopen's fingerprint index (`INV-FP-06`); CORR-007A's boundary statement, independently spot-checked this round, leaves it unchanged: `CONTROLLED CARRY-FORWARD TO ACCOUNTING/TAX`, `HIGH REMAINS`, separate from the payee-facing 50-twi certificate module CORR-007A did resolve. File existence was spot-checked this round (`l10n_th_reports/models/tax_report_pnd.py`, 145 lines, consistent with cited line ranges) but not re-derived to N-A12-01 depth — this should not be reported as freshly re-proven this round.

### 6.9 Special Team's recommendation

No contradiction, unsafe assumption, or fabricated fact was found in this mandate's scope; nothing here warrants FAIL/FROZEN. Equally, no new evidence closes `N-A12-01` itself, and several items — the gaps this pass narrowed but did not close (manufacturing WIP automation, the Periodic landed-cost code path), the AP-bridge period-integrity question, and the G-5/G-6 Accounting dependency — remain material enough that a Product or Replacement Readiness claim would be premature. This track's recommendation to Boss is **HOLD**: the standing Account+Inventory Backbone HOLD is independently reconfirmed, with the specific evidence gaps above logged as the concrete conditions for moving past it. This is an investigation finding for Boss's decision, not a Gate PASS, and does not authorize Team B, Team C, development, merge, or release.

---

## 7. Clean-Room Impact

Both passes were asked, independently, whether this round's evidence — or the target-design implications of the gaps it found — puts any clean-room principle at risk, and both answered **no violation found or alleged**. This section reads both against the four clean-room principles fixed in the execution prompt (§8):

1. **Reference Only.** Both passes confirm every reference-system mechanism cited this round — the manufacturing WIP wizard, the landed-cost allocation rules, the AR/AP valuation bridge, the return-valuation method, the `type`/`is_storable` gate, the posting gate, the absent closing-entry finding — is reported strictly as reference-system business-semantic evidence. The Council pass states this explicitly: every CORR-007B file frames its Odoo citations as reference-only business-semantic learning (for example, "Product Category is the config owner" stated as a business fact, not an instruction to copy a field). The Special Team pass states it with equal explicitness: every citation above is a location and a described business behavior — "landed costs are FIFO/AVCO-only," "WIP posting has no cron," "vendor bills must be posted to affect valuation," "customer returns price at original cost" — never a code excerpt proposed for reuse.

2. **No Copy / No Clone / No Reuse.** Neither pass alleges a code, schema, or architecture reuse violation by any prior round in this chain, and neither pass itself proposed one: the Special Team pass records explicitly that this round made no git commits and modified no files in the working tree. No SMEsPlus target schema, code, table, or naming has been produced or proposed from this round's material by either pass.

3. **Migrate Business Facts + Business Semantics Only — not legacy application architecture.** This is where both passes converge on the same underlying discipline, at different altitudes. The Council pass names a specific forward-looking risk for the record: file 09's account inventory — Stock Valuation, Stock Variation, Price Difference, location-level `valuation_account_id` — is close enough to Odoo's own account vocabulary that a future SMEsPlus Chart of Accounts must be independently defined against Thai statutory/TFRS-for-NPAEs account categories (an inventory asset account, a cost-of-goods-sold/variance account, a retained-earnings account under Equity) rather than transliterating Odoo's English labels. The business need — an asset account, a P&L true-up account — is the fact to migrate; the label and account-count structure are not. The Special Team pass practices the identical discipline as a working method rather than stating it as a risk: where a business fact differs from Boss's own screenshot or hypothesis vocabulary — the `type`/`is_storable` two-field gate correcting an assumed three-way enum, the manual-only WIP mechanism — that difference is reported precisely rather than smoothed over, consistent with migrating business facts rather than assuming legacy terminology maps one-to-one onto the target design.

4. **SMEsPlus Target Design Must Be Original.** Both passes are explicit that no SMEsPlus target design, contract, or schema is proposed anywhere in this round's material. Every open item — manufacturing WIP automation, landed-cost allocation completeness, the AP-bridge late-bill exception rule, the year-end retained-earnings entry, the Perpetual/delivery-vs-invoice timing decision — is left for Team B (not authorized this session) and, where an Accounting/Tax evidence dependency exists, for the Account reopen track.

One scope boundary is recorded for completeness: the Special Team pass performed no independent audit of deliverable `12`'s own Clean-Room Compliance Review function and defers that specific audit to Track 08 (Clean-Room / IP / Provenance VETO), noting only that nothing found this round contradicts its no-violation posture.

**Conclusion:** No clean-room violation is found or alleged by either pass this round. Both independently identify, from different altitudes, the same discipline as the live risk to manage going forward — not a Principle 1/2 breach, but a Principle 3 default-by-convenience risk if a future Team B, once authorized, reaches for Odoo's own account vocabulary or field cardinality as the path of least resistance rather than deriving SMEsPlus's design from independently-evidenced Thai statutory and business facts.

---

## 8. Item Classification Table

Classified per the CP-02 taxonomy fixed in the execution prompt: `CLOSED_WITH_EVIDENCE — DO NOT REASK`, `CARRY_FORWARD — NO MATERIAL DELTA`, `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS`, `CONFLICTING — REOPEN REQUIRED`, `UNKNOWN — STILL MATERIAL`, `SUPERSEDED — HISTORICAL ONLY`. Where an existing fingerprint ID (`INV-FP-*`) or standing gap number (`G-*`) already covers an item, it is reused. Genuinely new items surfaced this round are given a local `FIN-DELTA-*` reference pending PMO consolidation into the fingerprint index and deliverables `13`/`14`/`15`; these are **not** program-wide fingerprint IDs. Where the Council pass's own `STABLE`/`PROVISIONAL`/`HOLD` internal scale and the Special Team pass's own identical internal scale differ from each other or need translation into this fixed taxonomy, that translation is this document's own judgment, stated so Boss can see the reasoning, not the source passes' own words.

| Ref | Item | Classification | Raised by | Evidence |
|---|---|---|---|---|
| `INV-FP-09` | N-A12-01 umbrella — Account-led monthly/year-end close, stock cut-off, product-category valuation policy, periodic/perpetual posting, GL reconciliation, retained earnings | `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS` (standing CORR-007B disposition; reaffirmed, not weakened, by two further independent primary-source verifications this round) | Both, independently, strong corroboration | Council: 3/3 spot-verified citations matched exactly (`stock_move.py:630-638`; `product.py:666-670`; `company.py:177,823,847`). Special Team: 4/4 independently re-verified (periodic/real_time field; `action_close_stock_valuation`; posting gate; `ProductCategory` class), matching CORR-007B files 03/08/09/13/15/16 exactly. |
| `G-1` | Sequencing: Accounting lock-date enforcement vs. Inventory's periodic valuation closing | `CARRY_FORWARD — NO MATERIAL DELTA` on the mechanism-independence fact; `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS` on the control-design question (new concrete mechanism this round) | Both; Special Team adds new mechanism | Council: `_action_close_stock_valuation` reads no lock-date field; the lock-date wizard has no Inventory field. Special Team: same substrate, plus the late-posted-vendor-bill mechanism at `FIN-DELTA-04` below. |
| `G-2` | Post-close correction governance asymmetry — Inventory's global unaudited toggle vs. Accounting's scoped, audited exception model | `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS` (mechanism itself source-proven by both; Council's fresh statutory-control-weakness reframing this round is itself a material delta) | Both; Council reframes | Council: reframed as an internal-control weakness — "would not survive ordinary statutory audit-trail scrutiny." Special Team: independently confirms `account/models/account_lock_exception.py` vs. `stock_picking.py:15` — one global unaudited boolean, no user/reason/expiry. |
| `G-3` | Backdate enforcement granularity — whole-document vs. per-line | `CARRY_FORWARD — NO MATERIAL DELTA` | Neither pass examined this round | Not raised by either input this round; standing disposition (CORR-007B file 15, Addendum-4) carried forward unchanged. Listed here so the omission is explicit, not silent. |
| `G-5` | Migration-cutover opening-balance cross-proof (Inventory's valuation-over-period output vs. Accounting's opening trial balance) | `UNKNOWN — STILL MATERIAL` — cannot be produced by Inventory evidence alone; structurally blocked pending `COA-G04..G08` | Both, independently, strong corroboration | Council: ties directly to `COA-G01`/`G02` closed, `COA-G03` self-reported/unaudited, `COA-G04..G08` not closed. Special Team: same blocker, tied to governing ruling `47018139` and Reopen Program `42e04e63`. |
| `G-6` | No year-end P&L-to-Retained-Earnings closing entry exists in the reference system; whether SMEsPlus needs one | `CLOSED_WITH_EVIDENCE` on the reference-system negative finding; `UNKNOWN — STILL MATERIAL` on the SMEsPlus design decision (blocked on the same COA dependency as G-5) | Both, independently, strong corroboration | Council: re-derived via filesystem search (no closing wizard found) + `company.py:177,823,847`. Special Team: same finding, same citations, cross-referenced against `account_reports/models/account_report.py`. |
| `G-7` / `INV-FP-10` | `stock_valuation_report.py` PDF/XLSX export stub methods | `UNKNOWN — STILL MATERIAL` as a source fact (standing classification; formally owned by Track 04/05) | Special Team only this round | Independently re-performed and confirmed verbatim: literal `return` bodies, lines 140-144. Not examined by the Council pass this round. |
| `FIN-DELTA-01` | Manufacturing valuation/COGS handoff — `mrp_account` bridge; completed-MO moves reuse the ordinary posting gate; in-progress WIP valuation is a manual-only wizard with zero automated/cron trigger | `REOPEN_ELIGIBLE — DELTA TRIGGER EXISTS` | Both, independently identified the blind spot; Special Team advanced it to a mechanism proof this round | Council: zero `mrp_account` citations anywhere in CORR-007B's SHA-256 manifest; DR-002 A8 scoped to physical handoff only. Special Team: `_get_value_from_production()` hook confirmed; grep for `ir.cron` in the module returns zero hits. |
| `FIN-DELTA-02` | Landed/additional cost concepts — `stock_landed_costs` family, FIFO/AVCO-only eligibility, allocation split methods, lock-date exposure, commented-out Periodic `standard_price` block | `CLOSED_WITH_EVIDENCE` on the lock-date-safety sub-question; `UNKNOWN — STILL MATERIAL` on the full valuation-allocation mechanism | Both, independently identified the blind spot; Special Team advanced it to a mechanism proof this round | Council: module/table confirmed to exist, hashed once only to clear an orphan-table false positive. Special Team: FIFO/AVCO-only restriction traced (hard `UserError`); lock-date call sites traced to `account/models/account_move.py:2806,3911,3916,3958`; Periodic `standard_price` block observed present but commented out (~lines 132-142). |
| `FIN-DELTA-03` | Reference field label ("Perpetual (at invoicing)") does not match its own code trigger (`_action_done()` — a physical stock-move event, not an invoice-posting event) | `UNKNOWN — STILL MATERIAL` — a new SMEsPlus design decision on delivery-time vs. billing-time recognition | Council only | Council independently confirmed by direct read of `_action_done()`. Not addressed by the Special Team pass this round. |
| `FIN-DELTA-04` | AR/AP-to-Inventory valuation bridge (`purchase_stock._get_value_from_account_move`) and the derived late-posted-vendor-bill-vs-closed-period risk | `CLOSED_WITH_EVIDENCE` on the mechanism as a reference-system fact; `UNKNOWN — STILL MATERIAL` on the Thai statutory period-integrity design question it raises | Special Team only — core mandate territory neither the Council pass nor any prior round examined | Special Team: full method read, `purchase_stock/models/stock_move.py:153-219`; gated on `aml.move_id.state=='posted'` and `aml.date<=at_date`; handles `in_refund`; apportions across multiple receipts. |
| `FIN-DELTA-05` | Return/reversal cost-basis treatment under FIFO/AVCO | `CONFLICTING — REOPEN REQUIRED` — **the one direct disagreement between the two passes this round; see §4.4** | Council: unevidenced / `HOLD`. Special Team: traced and confirmed / `STABLE`. | Special Team: `stock_account/models/stock_move.py:463-472`, `_get_value_from_returns()`, prices returns at pro-rated original cost. Council: "not traced anywhere in the chain... inferred only structurally... unproven." |
| `INV-FP-13` | Stockable/Consumable/Service financial routing — a 2-field `type`/`is_storable` gate, not a 3-way enum | `UNKNOWN — STILL MATERIAL` at the target-design layer (standing classification; primary ownership Track 03/IBPV); `CLOSED_WITH_EVIDENCE` at the reference-mechanism-fact layer this round | Both; Special Team supplies the definitive mechanism | Council: `is_storable` AND-condition inside the posting gate supports the Perpetual-path routing hypothesis. Special Team: `type` limited to `consu`/`service`/`combo`; `is_storable` forced False for non-`consu` (`stock/models/product.py:894-895`); hard ORM constraint at `stock/models/stock_quant.py:583-585`. |
| `INV-FP-06` | GRPA-M18-D — Thai WHT/PND3/PND53 monthly statutory filing/export | `CARRY_FORWARD — NO MATERIAL DELTA` on the item's own disposition (`CONTROLLED CARRY-FORWARD TO ACCOUNTING/TAX`, `HIGH REMAINS`, unchanged) | Both confirm carry-forward status; Council raises an additional receipt-confirmation question | Special Team: file existence spot-checked (`l10n_th_reports/models/tax_report_pnd.py`, 145 lines); not re-derived to N-A12-01 depth this round. Council: no evidence available confirms the Account-domain reopen has logged/accepted receipt of the hand-off. |
| `INV-FP-15` | Is Accounting the Financial Truth owner? | `CARRY_FORWARD — NO MATERIAL DELTA` | Neither pass examined this round | Not raised by either input this round; standing disposition (file `01`, `INV-FP-15`) carried forward unchanged. Listed here so the omission is explicit, not silent. |

No item examined by either pass this round was found to be `SUPERSEDED — HISTORICAL ONLY`; that classification is considered and left unused for Track 06 this pass.

---

## 9. Material Questions and Open Risks Carried to Boss

### 9.1 N-A12-01 disposition, evidence currency, and the return-valuation conflict

- Given both passes independently confirm N-A12-01's central mechanism proofs match primary source exactly, is there anything left for further Inventory-only source-reading to add, or does everything remaining now require either Team B design authorization or Accounting-track evidence? Both passes answer no to the former and yes to the latter.
- Should Boss treat the return/reversal cost-basis question (§4.4, `FIN-DELTA-05`) as closed on the strength of the Special Team's `_get_value_from_returns()` citation, given the Council pass's own review-of-Special-Team-findings function (Charter §2) has not yet been exercised on this specific item?
- Every citation this track relies on lives only on the unmerged `audit/inventory-core-corr007b-3high-closure-010` branch; canonical `origin/SMEsPlus` carries none of it. Is Track 01's evidence-currency remediation (making this branch's evidence reachable in some governed form) a precondition for this track's HOLD to ever move, independent of anything Track 06 itself could do?

### 9.2 The two new blind spots

- Manufacturing WIP valuation has no automated equivalent to the periodic stock-closing cron proven for ordinary Inventory valuation. Does SMEsPlus's target design need one, and how must it sequence against the existing Inventory-only periodic-closing mechanism?
- Is "landed costs update Periodic-valued layers" fully proven, given the relevant code path is present in source but commented out? This needs one further targeted read before Team B can rely on it.
- Manufacturing valuation and landed cost were both completely unexamined through nine prior evidence rounds despite sitting squarely inside every version of this mandate's checklist. Should Boss ask why — was scope narrowed deliberately, or did these items simply not surface until this reopen's Council and Special Team were specifically tasked to look?

### 9.3 Timing, recognition, and control-governance questions

- Does SMEsPlus intend inventory value/COGS recognition to track physical delivery (as the reference system's actual trigger does) or invoice posting (as its label claims)? This must be a stated SMEsPlus design decision, not an inherited label.
- Is G-2's asymmetry (Inventory's unaudited global bypass vs. Accounting's audited, scoped exception) acceptable for a company subject to ordinary Thai statutory audit expectations, or must it be closed before any Inventory Gate decision — and does it require Team B alone, or Team B jointly with Accounting/Tax given it touches both sides of the same backbone?
- Should SMEsPlus adopt an explicit late-bill exception rule for the AP-bridge risk the Special Team identified — a vendor bill posted after a period closes silently altering that period's recomputed stock value without correcting the posted closing entry — or is deferring the true-up to the next closing (the reference system's own approach) acceptable under Thai statutory period-integrity expectations?

### 9.4 Cross-track sequencing and hand-off

- G-5 and G-6's statutory half cannot close on any amount of further Inventory-only work; both independently confirmed passes tie this to `COA-G04` through `COA-G08` remaining not closed on the parallel Account/COA track. Is that track's own timeline known to Boss, and should this track's HOLD carry an explicit re-check trigger tied to COA's progress rather than sit as an open-ended hold?
- Has the Account-domain reopen track actually logged or accepted receipt of the `GRPA-M18-D` hand-off CORR-007A made? A hand-off without a confirmed receiving owner is not yet a closed hand-off, per the Council pass.

---

## 10. Recommendation

Both the Council pass and the Special Team pass recommend **HOLD** to Boss's Gate decision process, independently reached and substantially corroborating, with one narrow, explicitly surfaced disagreement (§4.4). This is a recommendation, not a decision: per Charter §6 and §10, Boss alone makes the final Gate call. Track 06 recommends that Boss treat the following as the concrete conditions for moving past HOLD, drawn from both passes' convergent and unique findings (§4, §8, §9):

1. Route manufacturing valuation/COGS handoff (`FIN-DELTA-01`) and landed-cost allocation mechanism completeness (`FIN-DELTA-02`) to further Special Team investigation before either is treated as evidence-complete — both remain genuinely open despite this round's material advance.
2. Exercise the Council pass's own review-of-Special-Team-findings function (Charter §2) on whether the Special Team's `_get_value_from_returns()` citation is accepted as closing the return/reversal cost-basis question (`FIN-DELTA-05`) — do not let this document's own stated preference (§4.4) substitute for that review.
3. Require SMEsPlus's own clean-room design to state its delivery-time vs. billing-time revenue/COGS recognition basis explicitly (`FIN-DELTA-03`) rather than inherit the reference system's "Perpetual (at invoicing)" label, which does not match its own code trigger.
4. Carry G-2 into any future Team B design authorization with its statutory internal-control dimension attached, not only as a UX asymmetry.
5. Confirm, via Track 01 or the Account-domain reopen's own package, that `GRPA-M18-D` (`INV-FP-06`) has an acknowledged receiving owner before treating the CORR-007A hand-off as durable.
6. Hold G-5 and G-6's statutory half exactly where both passes place them — pending the parallel Account/COA track's closure of `COA-G04` through `COA-G08` — and treat that as a cross-track sequencing dependency this track cannot discharge alone, not as an Inventory-side evidence gap to keep re-testing.

---

## 11. Closing Statement

This document is a Council challenge and Special Team investigation finding, converged for Boss's Gate decision. It is **not** a Gate PASS declaration, and it does **not** authorize Team B, Team C, Development, Account Reopen, or the Account × Inventory Joint Reopen. Consistent with the execution prompt's Final Stop Instruction (§9) and the Charter's Core Control Statements (§10) — `No Evidence = No Progress`, `Never Skip Gate`, `Boss = Sole Final Approver`, `No Material Unknown Exhaustion = No Inventory Evidence Gate PASS` — Track 06's reconciled verdict is recorded here as **HOLD / EVIDENCE REQUIRED** for Boss's consideration alongside the other eight Veto tracks and their Special Team mirrors.

This track's own findings sit directly on top of the execution prompt's explicit boundary list (CP-07) of what Inventory must not close by itself: COA / Account Type / Account Group conclusions; final journal entry design; VAT / WHT / CIT statutory conclusions; retained-earnings / current-year-earnings logic; Account lock-date policy as Accounting truth; Inventory valuation-to-GL reconciliation as final Accounting closure; and the Account × Inventory Backbone baseline itself. Nearly every open item in this report maps directly onto that list — G-6 is retained-earnings logic; `GRPA-M18-D` is VAT/WHT/CIT statutory conclusions; G-1/G-2 are Account lock-date policy; G-5 is GL reconciliation; `N-A12-01` as a whole is the Account × Inventory Backbone baseline — which is precisely why this document converges evidence and surfaces disagreement rather than closing any of them.

Next action is PMO consolidation of this track's findings into deliverables `02`, `12`, `13`, `14`, `15`, and `20`, and Boss's own Gate decision — not further action by this track alone.

---

## Sources

Primary inputs: (1) Council Challenge findings, Track 06 (Financial / Accounting / Tax / Statutory VETO), produced independently and blind to the Special Team pass, per Charter §8; (2) Special Team Investigation findings, Track 06 mirror, produced independently and blind to the Council pass, per the same rule. Both are preserved in full in §5 and §6 above and are available in their original structured form on request. Governance and format grounding, read directly by this consolidation pass: `NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md` (§1–§10, including the exact Track 06 mandate boundary text at §4 row 06: "Financial / Accounting / Tax / Statutory VETO — Financial truth, posting, period, AR/AP, tax, reporting, statutory evidence"); `02_CLAUDE_SONNET_5_MAX_EXECUTION_PROMPT_SMEPLUS-26-09-02-INV-REOPEN-001.md` (CP-02 taxonomy, CP-07 Accounting-boundary "must not close" list, §6 deliverable numbering, §8 Hard Rules and clean-room principles, §9 Final Stop Instruction); `01_INVENTORY_PRIOR_EVIDENCE_AND_QUESTION_FINGERPRINT_INDEX.md` (source of `INV-FP-06`, `INV-FP-09`, `INV-FP-10`, `INV-FP-13`, `INV-FP-15`, the G-1 through G-7 sub-item numbering, the Account-domain `COA-G01..G08` state, and the header/taxonomy conventions followed here); `04_TBRAC_DEEP_FINDINGS.md` (structural and header-format precedent for this deliverable class, Track 02).
