# 12 — Requirement/Evidence-to-Design Traceability Audit

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006-D12`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-FV-006`
Control Level: `/L999.999`
Boss: Sole Final Approver
Role reminder: IBPV classifies. It does not redesign, does not choose a business policy on Boss's behalf, and does not accept TEAM B's own readiness self-assessment (file 20) as proof of anything it asserts. Every conclusion below was independently re-derived from the underlying TEAM A evidence and TEAM B design files.

Sources reviewed directly for this deliverable:
- TEAM B (primary): `17_TEAM_B_INDEPENDENT_DESIGN_DECISION_FIT_GAP_REGISTER.md`, `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md`, `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md`, `20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` (read skeptically, as a self-assessment, never as an answer key); supporting design files `03`, `05`, `11`, `12`, `13`, `14` opened to verify what file 19 and file 17 actually cite.
- TEAM A (baseline evidence): `16_FIT_GAP_CANDIDATE_PACK.md`, `14_UNKNOWN_CONFLICT_EVIDENCE_GAP_REGISTER.md`, `17_GROUP_A_EVIDENCE_MANIFEST.md`, `18_TEAM_A_EVIDENCE_GATE_CANDIDATE_REPORT.md`, plus underlying evidence files `01`, `02`, `03`, `04`, `05`, `07` opened directly to re-verify specific traceability-matrix citations.
- Independent Evidence Review (method reference only, not treated as an answer key for TEAM B): `AUDIT_REVIEW/07_GROUP_A_INDEPENDENT_EVIDENCE_REVIEW_REPORT.md`.
- TEAM B's own SHA-256 manifest (`21_TEAM_B_FINAL_SHA256_MANIFEST.txt`) and the prior independently-recomputed hash list (`RECOMPUTED_SHA256.txt`).

---

## PART A — SHA-256 Integrity Re-Performance

### A.0 — Result

An independent SHA-256 recomputation (`shasum -a 256`) was run directly against TEAM B's own files 01–20 as staged for this verification, in this session, as a sanity check on the fact already established for this review (an earlier independent recomputation, recorded in `RECOMPUTED_SHA256.txt`, had already passed). All three hash sets — TEAM B's own manifest (`21_TEAM_B_FINAL_SHA256_MANIFEST.txt`), the previously-recomputed list (`RECOMPUTED_SHA256.txt`), and this session's own fresh `shasum -a 256` run — are **byte-for-byte identical across all 20 files**. No missing file, no extra file, no mismatched hash.

**Result: PASS.** 20/20 files verified.

### A.1 — What this does and does not prove

This confirms **file integrity only**: the 20 design files this verification is reading are exactly the files TEAM B committed, unmodified in transit. It proves:
- No file was silently edited, truncated, or substituted between TEAM B's session and this IBPV session.
- TEAM B's own manifest is not fabricated — it reproduces under independent re-computation.

It does **not** prove, and must not be read as proving:
- That any citation inside those files (a cross-reference to a TEAM A evidence file/section, or between TEAM B's own files) actually resolves to real, supporting content.
- That TEAM B's design conclusions are internally consistent, complete, or correctly derived from the evidence.
- That the "independent decisions" TEAM B claims to have made beyond TEAM A's own classifications are sound.

Those are separate, substantive checks, performed independently in Parts B and C below. A hash match is necessary but nowhere near sufficient evidence of design correctness — treating a passed hash-integrity check as if it were a completeness or correctness proof would itself be a verification failure.

---

## PART B — Evidence-to-Design Traceability Spot-Checks (File 19)

### B.0 — Method

Five of file 19's citations were selected for full re-performance: for each, the cited TEAM A evidence file/section was opened directly (not read through TEAM B's paraphrase) and the cited evidence-ID rows were located by line number; the cited TEAM B design-file target was then opened directly to confirm the design conclusion is actually present there and is actually supported by (not merely adjacent to) the cited evidence. Four of the five are file 19 §02's "worked examples" (its most consequential, governance-required chain-format claims); the fifth is drawn from file 19 §01's deliverable-to-evidence index, to also test a claim outside the worked-examples set. Note on scope: this spot-check does not attempt to re-verify file 19 §03 (vendor-contamination self-check) or §05 (internal coherence self-check) — both are TEAM B's own self-scans of its own 21 files, and re-verifying those would require a full re-read of all 21 TEAM B files for vendor terminology and cross-reference resolution, which was out of scope for this specific deliverable's 5-citation spot-check mandate.

### FV006-TRC-001 — Worked Example 1 (MOV-31): Evidence ID Real, Section Locator Wrong

- **Verification Area:** Evidence-to-design traceability precision — cancellation-guard correction
- **TEAM B Artifact(s):** `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` §02, Worked Example 1: "Evidence: `02` §04 MOV-31, precision-corrected by CORR-003 to an all-or-nothing whole-recordset guard" → recorded in `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07
- **Approved Evidence/Baseline reference:** `TEAM_A/02_INVENTORY_CAPABILITY_MODEL.md`. MOV-31 is a real, exact evidence row (line 71): `_action_cancel()`'s all-or-nothing whole-recordset guard, precision-corrected by CORR-003, cited verbatim in TEAM A's own file. However, that row sits inside TEAM A file 02's **`# 02 — MOVEMENT CORE`** section (lines 40–150), not a "§04" section. File 02's actual `§04` is **`# 04 — PICKING / TRANSFER`** (lines 261–298), an unrelated section about `stock.picking`/`stock.picking.type`, not the movement-cancellation guard.
- **Finding Status:** `GAP FOUND` (citation-locator error; underlying evidence ID and substance are genuine)
- **Severity:** Minor
- **Why it matters:** The evidence ID (MOV-31) is real, the quoted content is accurate, and TEAM B's own design conclusion in `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07 ("per-instruction evaluation instead" of an all-or-nothing batch guard) is a faithful, correctly-reasoned response to that evidence. The defect is narrowly in the traceability-matrix's own section pointer — a future auditor or Team C engineer trying to pull up "`02` §04" to re-verify this specific claim would land on the wrong section (Picking/Transfer instead of Movement Core) and could wrongly conclude the citation doesn't exist at all.
- **Cross-domain impact:** None on the design conclusion itself; a documentation-inspectability issue only.
- **Gate impact:** Does not block — the underlying design decision is sound and separately verifiable at the correct location. File 19's claim in its own §00 that this is a "worked example in the governance-required chain format" implies a standard of pinpoint accuracy that this specific citation does not meet.
- **Required owner:** TEAM B design custodian (correct the section pointer from `§04` to `§02` in file 19).
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-TRC-002 — Worked Example 2 (Sequential Approval Investigation): Verified Precise

- **Verification Area:** Evidence-to-design traceability — sequential level-based approval control
- **TEAM B Artifact(s):** `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` §02, Worked Example 2: "Evidence: `04` §03 (full cross-model approval-schema investigation, CORR-003 resolution)" → recorded in `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §03 (APR-002)
- **Approved Evidence/Baseline reference:** `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md`. Section `# 03 — THE ORPHANED TWO-LEVEL APPROVAL SCHEMA (cross-model investigation)` (lines 85–173) is confirmed exact — the section number and title both match the citation precisely, and its content (three real installed modules, zero corresponding Python source anywhere, one real wiring point onto `purchase.request` only) is exactly what file 19 characterizes.
- **Finding Status:** `VERIFIED`
- **Severity:** N/A (positive confirmation)
- **Why it matters:** Cross-checked against `13_APPROVAL_CONTROL_SOD_REQUIREMENT_MODEL.md` §03: TEAM B's recorded decision (design the vendor-neutral shape as `EXTEND`; explicitly `HOLD` the internal workflow logic, citing the same "existence/installation/historical-use confirmed, internal logic unconfirmed" distinction TEAM A's own evidence draws) is a faithful, non-overreaching translation of the cited evidence. This is the correct pattern: EXTEND what's proven, HOLD what isn't.
- **Cross-domain impact:** None negative.
- **Gate impact:** Supports readiness of this citation as accurate.
- **Required owner:** N/A.
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-TRC-003 — Worked Example 3 (Return/Reversal): Verified, With a Minor Evidence-ID-Range Overstatement

- **Verification Area:** Evidence-to-design traceability — Return/Reversal domain ownership
- **TEAM B Artifact(s):** `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` §02, Worked Example 3: "Evidence: `03` §05 SRET-01..08, `04` §07 POL-29/30 (both full-file-grep negative)" → recorded in `05_INVENTORY_CORE_CANONICAL_DESIGN.md` §05; `17_...FIT_GAP_REGISTER.md` item 15
- **Approved Evidence/Baseline reference:** `TEAM_A/03_SALES_CAPABILITY_MODEL.md` `# 05 — RETURN (Sale-side...)` (lines 196–218) and `TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` `# 07 — PO LINE QUANTITIES & RECEIPT` (lines 295–343). Both section locators are exactly correct. POL-29/30 are exact, real rows. **However, SRET-01 and SRET-03 do not exist as rows anywhere in TEAM A file 03** — only SRET-02, SRET-04/05/06 (combined row), SRET-07, and SRET-08 are actually present (6 of the 8 numbers TEAM B's range implies).
- **Finding Status:** `VERIFIED WITH CONDITIONS`
- **Severity:** Minor
- **Why it matters:** The substantive claim — Sales has no dedicated Return feature or button anywhere, confirmed by full-file greps (SRET-08 negative) — is fully and independently supported by the rows that do exist (SRET-02, 04–06, 07, 08); TEAM A's own synthesis text ("there is no Sale-side 'Return' button or feature at all") is unambiguous. The condition is narrowly that citing a continuous range "01..08" overstates what is literally present in the source register by two IDs. This does not change the finding's substance but is a precision defect a strict citation audit is obligated to record.
- **Cross-domain impact:** None — the underlying business fact (Reversal is Inventory-owned; neither Sales nor Purchase has a commercial-side Return object) is independently confirmed and is the single most exhaustively-evidenced pattern in the whole package, consistent with the Independent Evidence Review's own Cluster D finding (`AUDIT_REVIEW/07...` §05) that Fit-Gap item 15's rationale carries one wording qualifier but is otherwise sound.
- **Gate impact:** None.
- **Required owner:** TEAM B design custodian (tighten the cited range to the IDs that actually exist, or note the gap in numbering as TEAM A's own artifact).
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-TRC-004 — Worked Example 4 (Thai Branch / Orphaned Party Columns): Verified, Precise

- **Verification Area:** Evidence-to-design traceability — Party/Thai-Branch duplication and orphaned multi-brand columns
- **TEAM B Artifact(s):** `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` §02, Worked Example 4: "Evidence: `01` §02 PTY-17..21, `01` §12 CO-15..24" → recorded in `04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §01; `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §01/§02
- **Approved Evidence/Baseline reference:** `TEAM_A/01_SHARED_MASTER_DEPENDENCY_MAP.md`. Section `# 02 — PARTY...` (lines 45–115) contains PTY-17 through PTY-22 at lines 67–72 (PTY-17..21 fully present, plus PTY-22 not cited but consistent). Section `# 12 — COMPANY / BRANCH` (lines 640–738) contains CO-15 through CO-24 at lines 669–688, exactly as cited. Both section numbers and every individual evidence ID are exact.
- **Finding Status:** `VERIFIED`
- **Severity:** N/A (positive confirmation)
- **Why it matters:** This is TEAM B's most precisely-cited worked example. TEAM B's design conclusion (canonical Party model treats Tax-Branch as one attribute — `REJECT` the duplication pattern; multi-brand/HQ capability explicitly **not** designed, registered as `CONTROLLED CARRY-FORWARD` rather than invented) is a faithful, non-overreaching translation: it resolves the structural duplication (two modules writing an overlapping concept) without inventing a multi-brand/HQ capability the evidence cannot support (PTY-21/CO-24: those columns have no corresponding source-code field definition anywhere — `EVIDENCE_MISSING` on origin/purpose, correctly left unresolved rather than guessed at).
- **Cross-domain impact:** None negative.
- **Gate impact:** Supports readiness.
- **Required owner:** N/A.
- **Blocking Development:** No.
- **Boss decision required:** No.

### FV006-TRC-005 — Index-Table Citation (SaaS/Tenant Boundary): Verified, With an Honest Scope Limit Already Disclosed

- **Verification Area:** Evidence-to-design traceability — Multi-Company/Warehouse context feeding the SaaS/Tenant Boundary file
- **TEAM B Artifact(s):** `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` §01, deliverable-index row: "14 SaaS / Multi-Company / Tenant Boundary | `01` §12, `05` Scenario 11"
- **Approved Evidence/Baseline reference:** `TEAM_A/05_INTEGRATED_E2E_LIFECYCLE_MAP.md`, `## Scenario 11 — Multi-Warehouse / Location / Company Context` (line 215), confirmed to exist exactly as cited, with a "VERIFIED FACT" confidence tag in TEAM A's own text, and content (company/warehouse/location scoping rules, Branch = child `res.company`, Thai Tax-Branch orthogonal to this hierarchy) matching what `14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md` §03–§04 builds on.
- **Finding Status:** `VERIFIED`
- **Severity:** N/A (positive confirmation), with one cross-reference noted below
- **Why it matters:** The cited evidence genuinely supports the Legal Company/Branch/Warehouse layers of file 14. It does **not**, and does not claim to, support the **Tenant** layer TEAM B places above Legal Company — file 14 §00/§02 is explicit that Tenant is "independently reasoned" and "a new capability requirement, not inferred from evidence," which is an honest, correctly-labeled disclosure, not a traceability defect. This distinction (evidence-grounded Company/Branch/Warehouse layers vs. a TEAM-B-invented Tenant layer with no evidence basis) was independently examined in `11_SAAS_MULTI_COMPANY_THAILAND_REALITY_VERIFICATION.md` (`FV006-SAAS-001`, status `GAP FOUND`, Major, Boss decision required) in this same IBPV session — that finding is not repeated in full here, only cross-referenced, to avoid duplicate adjudication of the same design decision under two deliverable numbers.
- **Cross-domain impact:** See `FV006-SAAS-001` for the full cross-domain analysis.
- **Gate impact:** None additional from this citation-precision check; the substantive Tenant-layer gate impact is recorded under `FV006-SAAS-001`.
- **Required owner:** N/A for this specific citation.
- **Blocking Development:** No (for this citation itself; see `FV006-SAAS-001` for the Tenant layer's own blocking status).
- **Boss decision required:** No (for this specific citation; see `FV006-SAAS-001`).

### B.1 — Spot-Check Summary

| Finding | Citation | Result | Severity | Blocking |
|---|---|---|---|---|
| FV006-TRC-001 | `02` §04 MOV-31 | GAP FOUND (wrong section pointer; content genuine) | Minor | No |
| FV006-TRC-002 | `04` §03 approval investigation | VERIFIED | — | No |
| FV006-TRC-003 | `03` §05 SRET-01..08, `04` §07 POL-29/30 | VERIFIED WITH CONDITIONS (ID-range overstated by 2) | Minor | No |
| FV006-TRC-004 | `01` §02 PTY-17..21, `01` §12 CO-15..24 | VERIFIED | — | No |
| FV006-TRC-005 | `01` §12, `05` Scenario 11 | VERIFIED (Tenant layer itself separately gated — see FV006-SAAS-001) | — | No |

**Net result: 3 of 5 fully precise (TRC-002, 004, 005), 2 of 5 carry a minor citation-precision defect (TRC-001, 003) with no impact on the substance of the underlying design conclusion.** No spot-checked citation was found to point to non-existent or contradicting content. This is a materially better result than a random sample would be entitled to assume, but it is not a "100% inspectable" traceability matrix as file 19 §00 characterizes itself — two precision defects in a 5-item sample is a real, if minor, quality signal that the traceability matrix's own internal cross-references were not independently proofread against TEAM A's actual section numbering before being finalized.

---

## PART C — Independent Re-Derivation of Fit-Gap Items #7, #10, #12

### C.0 — Why This Section Exists and How It Was Done

TEAM B's own readiness report (`20_TEAM_B_FORMAL_IBPV_READINESS_REPORT.md` §04, criterion 4) claims credit for "3 cases where TEAM B resolved an item Team A left UNKNOWN." That self-claim is **not** accepted as proof of anything here. For each of the three items, this section places three things side by side, independently: (1) TEAM A's original framing, quoted verbatim from `TEAM_A/16_FIT_GAP_CANDIDATE_PACK.md`; (2) TEAM B's conclusion, quoted verbatim from `17_...FIT_GAP_REGISTER.md` and the underlying design file it points to; (3) this reviewer's own independent judgment of which of the five governing categories the resolution actually falls into — (a) evidence-supported design reasoning, (b) a valid new target requirement explicitly labeled as such, (c) an unsupported assumption, (d) a cross-domain conflict, or (e) evidence missing.

---

### FV006-FG-007 — Item #7: Physical Count-in-Progress vs. Settled On-Hand

**TEAM A original (file 16, item 7):**
> Reference Observation: "Physical count workflow fused into the same ledger row as the on-hand quantity (`stock.quant`)" | Generic Business Semantic: "Inventory count-and-adjust is not a separate document type from the on-hand ledger itself" | Candidate: **UNKNOWN** | Rationale: "Works in source, but conflates two concerns (ledger + count-in-progress) in one row — a target design may reasonably prefer separation"

**TEAM B conclusion (file 17, item 7; design detail in `03_CANONICAL_BUSINESS_FACT_AND_CONCEPT_CATALOG.md` §00):**
> "TEAM B independently resolves this to a decision: keep count-in-progress conceptually distinct from the settled on-hand ledger fact, **even if a future schema implementation stores them adjacently** — a count-in-progress is a Commitment-type fact (a proposed correction awaiting reconciliation), not yet a Physical fact" ... "Disagree with leaving it UNKNOWN — TEAM B resolves it using the Commitment/Physical/Derived fact-type taxonomy already established in `03`, which Team A's evidence-only mandate did not have available to it."

**Independent comparison:** TEAM A's UNKNOWN was about a **practical design/schema question**: should a target implementation keep the physical count-in-progress and the settled on-hand ledger fact as separate structures, given the reference system fuses them into one row? TEAM B's "resolution" operates one level up, at the conceptual fact-typing level (assigning count-in-progress to the "Commitment fact" category and on-hand to "Physical fact" in TEAM B's own taxonomy from file 03). That conceptual distinction is sound, internally consistent design reasoning and does not contradict any evidence — a physical count is, by ordinary inventory-management logic, a proposed correction that only becomes truth once reconciled/applied, which is a defensible generalization, not an invented business fact. But TEAM B's own phrasing — "even if a future schema implementation stores them adjacently" — is an explicit admission that the **practical schema question TEAM A actually raised is not decided by this**. TEAM B has answered a narrower, adjacent question (how to name/classify the concepts) and is presenting that as a full resolution of TEAM A's broader UNKNOWN (whether to structurally separate them). This is a real overstatement of what was resolved, even though nothing in it is factually wrong.

- **IBPV Classification:** Primarily **(b) a valid new target requirement, explicitly labeled as such** for the fact-type distinction itself; but the disposition as "resolved, disagree with UNKNOWN" overstates its own scope against TEAM A's original question, which functionally remains open at the schema-design level.
- **Finding Status:** `VERIFIED WITH CONDITIONS`
- **Severity:** Moderate
- **Why it matters:** If Team C reads file 17 item 7 at face value, it could reasonably conclude the physical-count-vs-ledger schema question has been fully decided, when in fact only a conceptual naming/classification layer has been fixed and the structural (single-row vs. separate-row/table) decision is exactly as open as it was in TEAM A's evidence. Mislabeling an open implementation decision as "resolved" creates a risk that no explicit design-time decision is ever made about it, because everyone downstream believes IBPV or TEAM B already made it.
- **Cross-domain impact:** None beyond Inventory itself; this is a self-contained physical-fact-modeling question.
- **Gate impact:** Recommend re-labeling this item's disposition from "resolved" to `CONTROLLED CARRY-FORWARD` in the design record, scoped specifically to the schema-separation question, while retaining TEAM B's fact-type taxonomy (which is sound and should stand).
- **Required owner:** TEAM B design custodian (clarify scope of the resolution in file 17 item 7 and file 03 §00), then Team C at implementation time for the actual schema decision.
- **Blocking Development:** No — the underlying invariant (movement execution is immutable once executed) is solid and independently verified; the residual schema question is an ordinary implementation-time decision, not a control-integrity or compliance risk.
- **Boss decision required:** No — this is an internal design-precision matter, not a business-policy question.

---

### FV006-FG-010 — Item #10: Over-Fulfillment / Over-Delivery Policy

**TEAM A original (file 16, item 10):**
> Reference Observation: "Over-receipt/over-delivery is completely unguarded on both Sale and Purchase lines" | Generic Business Semantic: "Whether exceeding ordered quantity should be blocked, warned, or silently allowed" | Candidate: **UNKNOWN** | Rationale: "A real design decision SMEsPlus must make deliberately — the source's silence here is not evidence that silence is correct"

**TEAM B conclusion (file 17, item 10; design detail in `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §02–§03):**
> "TEAM B resolves this to a decision rather than leaving it open: **EXTEND** — introduce an explicit, configurable Over-Fulfillment Policy" ... "TEAM B does not fix a default value; this is flagged for Boss/business policy input" ... "TEAM B judges 'no system reaction to any quantity mismatch' as a real enough operational risk that the *existence* of a policy (not its default value) is decidable now."

**Independent comparison:** Unlike item #7, TEAM B here explicitly and correctly splits TEAM A's UNKNOWN into two distinct sub-questions and is honest about resolving only one: (1) *should a configurable policy mechanism exist at all* — TEAM B decides yes, on the defensible general-design-principle ground that leaving a quantity mismatch with zero system reaction is an operational/data-quality/audit risk regardless of which specific default a business later chooses; and (2) *what should the default behavior be (block/warn/allow)* — TEAM B explicitly does **not** decide this, and the item is separately tracked forward as item N2 in `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` §03 ("Default value for the Over-Fulfillment/Over-Billing Policy... CONTROLLED CARRY-FORWARD"). This is the correct pattern: TEAM B did not invent a business rule TEAM A's evidence could not support (it did not pick block, warn, or allow), and it did not silently drop the harder half of the question either.
- **IBPV Classification:** **(b) a valid new target requirement, explicitly labeled as such.** The "existence of a configurable policy point" is a legitimate design-team decision (adding a control surface is not itself a business-policy choice), cleanly separated from the genuine business-policy choice it does not make.
- **Finding Status:** `VERIFIED`
- **Severity:** N/A (positive confirmation)
- **Why it matters:** This is the most disciplined of the three claimed resolutions — it demonstrates the difference between a design team legitimately narrowing an Unknown (permissible) and a design team resolving it by invented certainty (not permissible). No correction is required to file 17 item 10 itself.
- **Cross-domain impact:** None from the mechanism decision itself. The deferred default value has Sales/Purchase/Accounting interface implications, addressed independently in Deliverable 13 (`FV006-GAP` register, item N2).
- **Gate impact:** None from this item; see Deliverable 13 for the deferred-default disposition.
- **Required owner:** N/A for this finding.
- **Blocking Development:** No.
- **Boss decision required:** No for the mechanism (already correctly TEAM B's own call); Yes for the default value, tracked separately (Deliverable 13, item N2).

---

### FV006-FG-012 — Item #12: Asymmetric Cancellation Gates (Dual vs. Single)

**TEAM A original (file 16, item 12):**
> Reference Observation: "Purchase's cancellation gate is dual (locked OR open vendor bill); Sale's is single (locked only)" | Generic Business Semantic: "Cancellation preconditions" | Candidate: **UNKNOWN** | Rationale: "Could be intentional (AP exposure is a harder blocker than AR exposure) or accidental — **not resolvable from source alone**"

**TEAM B conclusion (file 17, item 12; design detail in `12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §07):**
> "TEAM B resolves this: **ADAPT** both gates as evidenced (not a defect) — an outstanding vendor financial exposure is a materially different, legitimately-stricter blocking condition than a merely-drafted customer invoice" ... "TEAM B judges this resolvable from the business-semantic difference alone, **without needing further evidence**."

**Independent comparison — this is the item requiring the most scrutiny, per the governing instruction, and it is where this review's independent judgment departs from TEAM B's:**

1. TEAM A did not merely flag an open question — it made an explicit, reasoned finding that the source evidence is **silent on intent**: the asymmetry "could be intentional... or accidental — not resolvable from source alone." That is itself a piece of evidence (a negative finding), not an absence of one.
2. TEAM B's rationale for overriding that finding rests entirely on a single sentence of unsourced business reasoning, explicitly declared to need "no further evidence." Re-reading the underlying evidence TEAM A itself cites for this item (`TEAM_A/04_PURCHASE_CAPABILITY_MODEL.md` PO-35: `button_cancel()` blocks on `locked` **OR** "any non-cancel/non-draft vendor bill" — i.e., any vendor bill that is confirmed/posted and not yet cancelled; `TEAM_A/03_SALES_CAPABILITY_MODEL.md` CANC-04/CANC-05: Sale's `action_cancel()` blocks only on `locked`, and its `_action_cancel()` merely **auto-cancels any draft invoices** as a side effect of cancelling — it does not check for, and is not blocked by, a **posted/confirmed** customer invoice at all).
3. TEAM B's own justification text says the asymmetry is legitimate because vendor exposure is "materially different... than a **merely-drafted** customer invoice." That phrasing mischaracterizes the actual evidenced gap: the true asymmetry is not "Purchase blocks on posted bills, Sale only lacks protection for draft invoices" — it is that **Sale has no gate against a posted/confirmed customer invoice either**. A sales order can be cancelled while a *posted, unpaid* customer invoice already exists against it, with no equivalent of Purchase's "open vendor bill" check. TEAM B's stated rationale does not address this — the sentence it uses to justify closing the item describes a comparison ("stricter than a merely-drafted invoice") that is not the comparison the evidence actually supports (the real gap is symmetric-in-kind: an *outstanding, posted* financial document on either side).
4. No evidence anywhere in the TEAM A package (or in TEAM B's own file 12 §07, which lists "Accounting Interface Impact" only for the Over-Fulfillment/Over-Billing items, not for this one) establishes what happens to a posted customer invoice when the sales order behind it is subsequently cancelled. That interaction sits squarely at the Sales/Accounting Core boundary (Financial Handoff, per `15_ACCOUNTING_AND_EXTERNAL_INTERFACE_DEPENDENCY_MODEL.md`) and is not addressed by TEAM B's closure of this item.

- **IBPV Classification:** **(c) an unsupported assumption**, presented with more confidence than either the cited evidence or TEAM A's own explicit "not resolvable from source alone" finding warrants. It is not evidence-supported design reasoning (category a) because the one sentence of reasoning offered does not accurately characterize the evidenced asymmetry it claims to explain, and it is not a valid new target requirement (category b) because it closes rather than adds a control point.
- **Finding Status:** `CONFLICT FOUND` — this review's independent re-derivation reaches a different conclusion than TEAM B's stated resolution, and TEAM B's own supporting rationale contains an internal accuracy gap against the evidence it cites.
- **Severity:** Major
- **Why it matters:** Closing this item as "ADAPT both as evidenced, not a defect" removes it from further scrutiny going forward — a future Team C build could reasonably treat the Sales-side cancellation gate as fully specified and deliberately asymmetric, when the actual open question (should Sales get an equivalent block against an outstanding/posted customer invoice, mirroring Purchase's outstanding-vendor-bill block?) has not been answered by evidence or by a sound business argument — only asserted.
- **Cross-domain impact:** Yes — directly touches the Sales↔Accounting Core Financial Handoff boundary (a cancelled commitment with a live posted invoice against it is exactly the kind of state/event combination the Accounting interface needs a defined answer for, and none currently exists in this design package).
- **Gate impact:** Recommend re-opening this item's classification from `ADAPT` (closed) to `EVIDENCE MISSING` / `CONTROLLED CARRY-FORWARD`, requiring an explicit Boss/business decision: does SMEsPlus want a Sales-side cancellation gate symmetric to Purchase's (block on locked OR an outstanding/posted customer invoice), or is the asymmetry deliberately accepted as a business risk trade-off? Either answer is legitimate — what is not legitimate is treating the question as already answered by "business-semantic reasoning alone" when the reasoning offered does not hold up against the cited evidence.
- **Required owner:** Boss (business-policy decision), with TEAM B as design custodian once directed.
- **Blocking Development:** **Yes, for the Sales-side cancellation-gate design specifically** — this meets the charter's Pre-Development Blocking Rule (`EXPERT_IBPV_CHARTER.md` §9) on two counts: "unverified state/event transition that affects financial/control integrity" (cancelling a commitment with a live posted invoice attached) and, pending the Accounting Core boundary check in item 4 above, a potential "unresolved accounting/compliance impact." Does not block the rest of GROUP A's design.
- **Boss decision required:** Yes.

### C.1 — Fit-Gap Re-Derivation Summary

| Item | TEAM A original | TEAM B claim | IBPV independent verdict | Status | Severity | Blocking |
|---|---|---|---|---|---|---|
| #7 — Count-in-progress vs. on-hand | UNKNOWN | "Resolved" (fact-type taxonomy) | Conceptual layer only resolved; practical schema question still open — re-label as carry-forward | VERIFIED WITH CONDITIONS | Moderate | No |
| #10 — Over-Fulfillment Policy | UNKNOWN | "Resolved" (mechanism only; default explicitly deferred) | Honest, correctly-scoped resolution | VERIFIED | — | No (mechanism); Yes for default (see Deliverable 13, N2) |
| #12 — Asymmetric cancellation gates | UNKNOWN ("not resolvable from source alone") | "Resolved" (ADAPT both, no further evidence needed) | Unsupported assumption; evidence does not support the stated rationale; re-open | CONFLICT FOUND | Major | **Yes**, for the Sales-side gate specifically |

**Net independent verdict on TEAM B's headline claim** (file 20 §04 criterion 4: "3 cases where TEAM B resolved an item Team A left UNKNOWN"): **Not accepted as stated.** Of the three, one (#10) is a genuinely sound and honestly-scoped resolution; one (#7) is a partial resolution overstated as complete; one (#12) is an unsupported assumption that should not have been closed and is elevated here to a Major, Boss-decision-required, Development-blocking (for that specific sub-item) finding. TEAM B's self-assessment that all three represent disciplined, evidence-respecting design work is only one-third correct on independent re-performance.
