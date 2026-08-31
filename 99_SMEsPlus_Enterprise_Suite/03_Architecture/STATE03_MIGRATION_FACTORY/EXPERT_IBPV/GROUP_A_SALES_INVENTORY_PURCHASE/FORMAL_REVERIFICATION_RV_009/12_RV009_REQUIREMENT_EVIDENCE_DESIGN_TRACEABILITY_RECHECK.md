# 12 — Requirement/Evidence-to-Design Traceability Recheck (RV-009)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-009-D12`
Project: SMEsPlus ENTERPRISE SUITE
STATE: STATE03 — Architecture
Domain Group: GROUP A — Sales + Inventory + Purchase Integrated Commercial–Supply–Inventory Backbone
Execution Function: EXPERT IBPV — Independent Business Process & Design Verification Team
Session: Formal IBPV Re-Verification RV-009
Reviewing: TEAM B CORR-008 corrective package
Frozen pre-correction baseline: `b98a3b9fb435845dbd15fae79db63b0b73a82420`
Corrected commit under review: `359f96c0cfee2f74955fe7e8f1d0110ec21a0a45`
Checked-out branch: `ibpv/group-a-sip-formal-reverification-009`
Control Level: `/L999.999`
Boss: Sole Final Approver

Role reminder: this deliverable independently re-checks every evidence citation TEAM B's CORR-008 corrective
reasoning makes. TEAM B's own `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` and
`CORRECTIVE_CORR_008/26_TEAM_B_CORR008_DELTA_AND_TRACEABILITY_REGISTER.md` were used only to identify which
citations to check — every primary source below was located and read directly, not taken on TEAM B's word.

---

## Method note applicable to Checks 1–3

Checks 1, 2, and 3 all cite the same two TEAM A files:
`GROUP_A_SALES_INVENTORY_PURCHASE/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` and
`.../01_SHARED_MASTER_DEPENDENCY_MAP.md`. A full-repository search (`find`, `grep -r`) confirmed **neither file
exists anywhere in the working tree of the frozen, checked-out commit** (`359f96c0...`), nor in its parent
baseline (`b98a3b9f...`), nor anywhere under `TEAM_A/` on this branch. TEAM A's actual
`06_DOMAIN_RESEARCH/GROUP_01_SALES_INVENTORY_PURCHASE/` folder on this branch contains only three
`00_NEW_SESSION_PROMPT_*.md` files — no numbered deliverables were ever merged into this branch's history for
that domain group (contrast `DOMAIN_01_ACCOUNTING_CORE`, which has a full 01–25 set).

Git-history archaeology located both files: they were authored on a **separate, never-merged sibling branch**,
`origin/claude/group-a-sales-inventory-purchase-dr002` (files added at commits `99158adb...` and `cfd1e2adb...`,
tip `8b0993d8...`). `git merge-base --is-ancestor cfd1e2adb... HEAD` returns **not an ancestor** — this branch's
content was never merged into the line this RV-009 checkout, TEAM B's CORR-008 branch, or even TEAM B's own
cited "Formal IBPV input" commit (`535724c0...`) descend from. `git show 535724c0...:<path>` for either file
also fails ("does not exist in ...") — confirming the files are not reachable from that commit either.

For due diligence, the content was read directly from the sibling branch's tip (`8b0993d8...`) and checked
against TEAM B's claims (see per-check content verification below). It substantively matches what CORR-008
claims, and FV-006's own deliverables (`07_CONTROL_APPROVAL_PERMISSION_SOD_VERIFICATION.md`,
`06_DATA_FACT_OWNERSHIP_AND_HANDOFF_VERIFICATION.md`) already used near-identical citations to identify the
*original* findings (`FV006-SOD-001`, `FV006-DFO-005`, part of `FV006-INT-001`'s context) — meaning FV-006's own
review session evidently had access to this content through some means. TEAM B did not fabricate new file
names; it repeated citations that a prior review round also used. But as constituted in the frozen commit this
RV-009 session is chartered to audit, **the cited primary sources are absent and unreachable from HEAD** — this
is a real, blocking traceability defect independent of whether the content itself, once located, turns out to be
accurate. Verdict below is `EVIDENCE MISSING` for all three checks, with the content-accuracy finding recorded
separately so it is not lost.

---

## Check 1 — CORR8-02 (Retry/Idempotency) citing TEAM A `13` §02 item 3

**Claim checked** (`22_TEAM_B_CORR008_FINDING_CLOSURE_REGISTER.md` line 62–63; repeated in
`CORRECTIVE_CORR_008/26_TEAM_B_CORR008_DELTA_AND_TRACEABILITY_REGISTER.md` line 33): "Governing evidence/baseline:
TEAM A `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` §02 item 3 (the one evidenced concurrency case, already
addressed pre-correction)."

**Primary source located**: not present at the frozen commit/branch under review (see Method note above).
Located instead at `origin/claude/group-a-sales-inventory-purchase-dr002` tip `8b0993d8...`, file
`TEAM_A/06_DOMAIN_RESEARCH/GROUP_01_SALES_INVENTORY_PURCHASE/13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`,
§02 item 3: *"One row per (product, location, lot, package, owner) in stock.quant" — Confirmed absence: "No
unique/composite DB index enforces this — it's an application convention reconciled AFTER THE FACT by
`_merge_quants()`, which exists specifically because concurrent writers can violate it."* — this does match the
"evidenced concurrency case" characterization.

**Verdict**: `EVIDENCE MISSING` (at the frozen commit under formal re-verification). Content, when located via
git archaeology outside the audited baseline, supports the claim — but the citation does not resolve to anything
in the reviewable repository state.

---

## Check 2 — CORR8-05 (Self-Approval) citing TEAM A `13` §01 item 10

**Claim checked** (`22` line 155–156; `26` line 70–71): "Governing evidence/baseline: TEAM A
`13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md` §01 item 10 (the role-based gate itself, test-confirmed)."

**Primary source located**: same file as Check 1, same absence from the audited baseline. At the sibling-branch
tip, §01 item 10 reads: *"Purchase's amount-threshold approval gate: a non-manager cannot self-approve above the
configured amount | ORM method guard, **test-confirmed** | Purchase PO-06/08."* This matches CORR8-05's
characterization exactly (role-based, test-confirmed).

**Verdict**: `EVIDENCE MISSING` (at the frozen commit under review) — same structural defect as Check 1. Content
accurate when located out-of-band.

---

## Check 3 — CORR8-08 (Archival) citing TEAM A `01_SHARED_MASTER_DEPENDENCY_MAP.md` for `UOM-06`, `PAY-07`, `CUR-08`

**Claim checked** (`22` line 252–254; `26` line 111; also restated verbatim in the corrected
`04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md` §08): `UOM-06` — "protected UoMs 'cannot be deleted, only
archived'"; `PAY-07` — "payment-term deletion 'blocked if any `account.move` still references the term'";
`CUR-08` — "'a currency used by any company cannot be deactivated'."

**Primary source located**: `01_SHARED_MASTER_DEPENDENCY_MAP.md` is likewise absent from the audited baseline
(same sibling-branch-only situation as Checks 1–2). At `8b0993d8...`, the file (831 lines) contains, verified
line-by-line:
- Line 220: `UOM-06 | uom_uom.py | L24–32, L105–112 | Protected "master data" UoMs cannot be deleted, only archived`
- Line 406: `PAY-07 | account_payment_term.py | L258–261 | Delete blocked if any account.move still references the term`
- Line 463: `CUR-08 | res_currency.py | L108–118 | A currency used by any company cannot be deactivated`

All three quotes are exact matches to TEAM B's claims. This is independently corroborated by FV-006's own
`06_DATA_FACT_OWNERSHIP_AND_HANDOFF_VERIFICATION.md` (lines 323–325), which quotes the identical three items, and
by FV-006's `12_REQUIREMENT_EVIDENCE_TO_DESIGN_TRACEABILITY_AUDIT.md` (line 96), which independently re-verified
other sections of this same file with exact line-number citations at review time.

**Verdict**: `EVIDENCE MISSING` (at the frozen commit under review) — same structural defect as Checks 1–2.
Content, once located, is accurate and precisely quoted. This is the same finding requested for cross-check with
Deliverable 07's independent reviewer; both should reach the same absence conclusion if that reviewer also works
strictly from the frozen commit.

**Recommendation for all three checks (1–3)**: before this evidence can be treated as verified-in-place for any
future gate, `origin/claude/group-a-sales-inventory-purchase-dr002` (or at minimum the two files
`01_SHARED_MASTER_DEPENDENCY_MAP.md` and `13_CROSS_MODULE_INVARIANT_CANDIDATE_REGISTER.md`) must be merged into
the branch line that TEAM B's design and this IBPV review operate on. Until then, CORR8-02, CORR8-05, and
CORR8-08 rest on evidence that is real and accurately quoted but not present in the audited repository state.

---

## Check 4 — CORR8-09 (SaaS/Tenant) governance citations

**Claim checked** (`22` line 285–287): `STATE01_PROJECT_CHARTER_v1.0.md` §5; `STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md`
Product Boundary; `ARCHITECTURE_GOVERNANCE_STANDARD.md` "Multi-Tenant by Design" — "all three Boss-approved,
mandate-level only."

**Primary sources located and read directly** (all exist at HEAD, all under
`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/`):

1. `State_01_Project_Identity/STATE01_PROJECT_CHARTER_v1.0.md` — Status: `APPROVED BASELINE`, Final Approver:
   Boss, Approval Date 2026-07-13. §5 "Initial Product Scope" states: "SaaS Foundation and tenant control ...
   Sales, Purchase, Inventory, Product, and Master Data ..." — a scope-inclusion mandate, zero structural
   elaboration (no isolation model, no layering, no mechanics stated). Matches TEAM B's characterization.
2. `State_01_Project_Identity/STATE01_SCOPE_PRINCIPLES_RACI_v1.0.md` — Status: `APPROVED BASELINE`, Approval
   Date 2026-07-13 (same date as the Charter). "Product Boundary" section states: "In scope: SaaS foundation,
   tenant/company/user control, ..." — again mandate-only, no structure. **Minor precision note**: unlike the
   Charter, this file's own header does not itself name "Boss" as approver (only "Status: APPROVED BASELINE");
   Boss-approval is established for this document via the project's own governing pattern (Charter + RACI issued
   as one same-day baseline package, and the RACI table inside this very document names Boss as Approver for
   "Project identity documents" and "Governance documents," the category this file itself belongs to) rather
   than a self-declaration in this specific file. Not a material defect, but worth noting for completeness.
3. `ARCHITECTURE_GOVERNANCE_STANDARD.md` — Status: `Approved`, Approved By: Boss, Effective Date 2026-07-05.
   "Architecture Principles" bullet list includes, verbatim, "Multi-Tenant by Design" — a bare principle-level
   bullet, no elaboration, no structural definition whatsoever. Exact match to TEAM B's citation.

**Verdict**: `VERIFIED WITH CONDITIONS`. All three documents exist, are genuinely part of a Boss-approved
governance baseline, and state a mandate only — TEAM B's characterization ("mandate-level only," not a structural
definition) is accurate. Condition: the minor documentation-completeness point on document 2 above (approver not
self-named in that specific file) should be closed by whoever owns governance hygiene, but it does not undermine
the traceability claim CORR8-09 makes.

---

## Check 5 — Spot-check of `19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` diff

`git diff b98a3b9f... 359f96c0... -- .../19_EVIDENCE_TO_DESIGN_TRACEABILITY_MATRIX.md` shows exactly one
addition: a new "05A — CORR-008 Lineage Note" (14 lines), inserted before the pre-existing "05 — Internal
Coherence Check" section.

The added text states that file 19 itself is **not rewritten** by CORR-008 (its worked examples remain a
statement of the pre-correction baseline only), and that the nine CORR-008 findings' traceability chain lives in
a separate, correctly-linked file: `CORRECTIVE_CORR_008/26_TEAM_B_CORR008_DELTA_AND_TRACEABILITY_REGISTER.md`
(confirmed to exist at that path), plus a pointer to
`CORRECTIVE_CORR_008/23_TEAM_B_CORR008_SAAS_TENANT_BASELINE_RECONCILIATION.md` (also confirmed to exist). Both
links resolve to real files.

**Verdict**: `VERIFIED`. The addition is a navigational/lineage pointer only — it asserts no new evidence claim
of its own, does not alter any pre-existing worked example, and correctly directs a future reader to file 26 for
the nine findings. No untraceable claim introduced. (Cosmetic-only observation: the new section is numbered
"05A" ahead of the pre-existing "05," which is a slightly unusual numbering choice but not a traceability
defect.)

---

## Check 6 — Spot-check of `26_TEAM_B_CORR008_DELTA_AND_TRACEABILITY_REGISTER.md` (3 entries, before/after diffed against `b98a3b9f...`)

### CORR8-01 (Denied-Approval Wind-Down)
- **Before, as claimed**: "07 §01 stated Pending Approval with no exit on denial; 08 §01 and 09 §02 conflicted on
  when the Inventory fulfillment request was created." `git show b98a3b9f...:.../07_PURCHASE_CANONICAL_DESIGN.md`
  §01 confirms: lifecycle line reads `Draft → Sent → [Pending Approval, conditional] → Committed → Cancelled`
  with no `Rejected`/denial exit anywhere in that specific lifecycle statement (a `Rejected` state does appear
  elsewhere in the pre-correction file, but only in the unrelated §04 "Internal Demand Capture" concept — a
  different fact from the Supply Commitment lifecycle in §01, so no contradiction). Matches.
- **After, as claimed**: new `Rejected` state, `Supply Commitment Rejected` event, reuse of the Cancellation
  cascade. `git diff` on `07`, `08`, `09` for this commit range confirms a new ~35-line "CORR-008 closure" block
  in `07` §01 stating exactly this (new state, denial event, owner, downstream stand-down via the existing
  not-yet-executed cascade, audit history, resubmission classification, residual unknown). Matches.

### CORR8-06 (Event Transport Semantics)
- **Before, as claimed**: "08 §10's one-pair-only transport characterization (Purchase direct/synchronous vs.
  Sales indirect/event-driven)." `git show b98a3b9f...:.../08_INTEGRATED_E2E_LIFECYCLE_AND_STATE_MODEL.md` §10
  confirms this exact contrast, stated only for that one pair, with no catalog-wide rule anywhere else in the
  pre-correction file. Matches.
- **After, as claimed**: new catalog-wide §00A in file 09. `git diff` confirms a new "00A — Event Transport
  Semantics" section with classification rule (synchronous/asynchronous), default, ordering guarantee, and
  consumer-failure rule, exactly as described. Matches.

### CORR8-08 (Shared-Master Archival)
- **Before, as claimed**: "no general archival rule; protection stated only for UOM's conversion ratio and
  Warehouse's owning-company assignment." `git show b98a3b9f...:.../04_SHARED_MASTER_CANONICAL_BOUNDARY_MODEL.md`
  confirms: §03 states "Conversion ratios become immutable once referenced by any commitment or physical fact"
  (UOM) and §05 states "Warehouse is company-owned and immutable-after-creation" — these are the only two
  protection-adjacent statements in the pre-correction file; no general archive-vs-delete rule exists anywhere
  else in it. Matches (note: these are immutability statements, not literally "archive not delete" statements —
  a fair paraphrase, not a mismatch).
- **After, as claimed**: new §08 "General Archival / Non-Deletion Rule." `git diff` confirms the new section
  cites `UOM-06`/`PAY-07`/`CUR-08` verbatim (see Check 3), states the general rule, scope, owner, archive
  semantics, reference-preservation, and a stated zero-historical-reference exception. Matches. (Side effect
  noted: this insertion renumbers the old "08 — Summary Boundary Table" to "09" — cross-references elsewhere that
  point to "04 §08" now correctly point at the new archival rule per the diff reviewed; no dangling reference
  found in the files checked for this deliverable.)

**Verdict (Check 6 overall)**: `VERIFIED`. All three spot-checked entries' "before" and "after" states match the
real pre-correction (`b98a3b9f...`) and corrected (`359f96c0...`) text exactly.

---

## Check 7 — General sweep of the 13 CORR-008-changed baseline files for untraceable TEAM B design decisions presented as evidence

Files swept (the 13 baseline files, 01–21, actually touched by CORR-008, per `git diff --stat b98a3b9f... 359f96c0...`):
`03`, `04`, `05`, `07`, `08`, `09`, `10`, `12`, `13`, `14`, `18`, `19`, `20`. Every inserted line in each file's
diff against `b98a3b9f...` was read (not just the 7 evidence-package files 22–28).

**Finding**: no clear violation located. Where CORR-008 introduces a new TEAM B design decision, it is
consistently and explicitly labeled as such, distinct from evidence:
- File 14 (`14_SAAS_MULTI_COMPANY_TENANT_BOUNDARY_MODEL.md`) introduces an explicit five-category classification
  scheme (§00, §08) and tags every material Tenant statement with one of `EXISTING BOSS-CONTROLLED SAAS
  INVARIANT`, `TEAM B CANONICAL DESIGN CHOICE WITH EXPLICIT RATIONALE`, `EVIDENCE-SUPPORTED GROUP A DESIGN
  ELABORATION`, or `CONTROLLED ASSUMPTION / REQUIRES FUTURE VERIFICATION`. Two of its citations to FV-006's own
  findings were independently checked against the FV-006 source: `FV006-SAAS-002` ("Legal Company / Branch /
  Warehouse / Shared-Master Layers: Evidence-Cited, Not Independently Re-Traceable in This Session," status
  `VERIFIED WITH CONDITIONS`) and `FV006-SAAS-004` ("Cross-Company Handoff: Appropriately Scoped Out," status
  `VERIFIED`) — both paraphrases in file 14 are accurate.
- File 13's new "Identity-Based Self-Approval Exclusion" row explicitly states "TEAM B does not claim this was
  how any legacy module actually behaved" — correctly labeled as a target requirement, not a legacy-behavior
  claim.
- File 12's new idempotency invariant (§11) and file 08/09/10's handoff-failure-detection additions are stated
  as TEAM B business-semantic decisions ("TEAM B states one general ... business invariant," "TEAM B decision"),
  not attributed to evidence.
- File 04 §08's general archival rule (Check 3/6 above) explicitly uses the words "generalizes" and "extends ...
  to the concepts that previously had no stated rule" when moving from the three evidenced items to all Shared
  Master concepts — honest about the evidence boundary, though it does not use the same explicit
  `TEAM B CANONICAL DESIGN CHOICE` tag file 14 introduces. This is a minor stylistic inconsistency across the
  package (file 14's classification scheme is not applied uniformly to file 04), not a mischaracterization —
  the prose itself does not claim the extension is evidenced.

**Relationship to Checks 1–3**: Checks 1–3 found that the *primary sources* CORR8-02/05/08 cite are absent from
the audited baseline. That is a distinct defect (evidence-location failure) from what Check 7 looks for
(TEAM B's own choice mischaracterized as evidence). Because the cited content, once located, does substantiate
the claims, this review does not additionally recharacterize CORR8-02/05/08 as Check-7 violations — but flags
that Checks 1–3's finding must be resolved (per the recommendation there) before CORR8-02/05/08's evidence
status can be called fully closed.

**Verdict**: `VERIFIED`. No sentence in the 13 changed baseline files was found presenting a TEAM B design choice
as independently evidenced. One minor stylistic-consistency observation recorded above (file 04 §08 vs. file
14's explicit tagging convention) — informational only, not a blocking defect.

---

## Summary

| # | Check | Verdict |
|---|---|---|
| 1 | CORR8-02 idempotency ← TEAM A `13` §02 item 3 | `EVIDENCE MISSING` (source absent from audited baseline; content accurate when located out-of-band) |
| 2 | CORR8-05 self-approval ← TEAM A `13` §01 item 10 | `EVIDENCE MISSING` (same defect; content accurate) |
| 3 | CORR8-08 archival ← TEAM A `01_SHARED_MASTER_DEPENDENCY_MAP.md` | `EVIDENCE MISSING` (same defect; content accurate, quotes exact) |
| 4 | CORR8-09 governance mandate citations | `VERIFIED WITH CONDITIONS` (minor approver-attribution note on one document) |
| 5 | File 19 diff (+14 lines) | `VERIFIED` |
| 6 | File 26, 3 spot-checked entries | `VERIFIED` |
| 7 | General sweep, 13 changed baseline files | `VERIFIED` (one minor stylistic observation) |

This deliverable's overall conclusion is `NOT READY FOR DEVELOPMENT` on evidence-traceability grounds specific to
CORR8-02, CORR8-05, and CORR8-08: three of the nine CORR-008 findings rest on TEAM A source files that do not
exist in the repository state this Formal IBPV re-verification is chartered to audit. The content of those files,
recovered from an unmerged sibling branch, corroborates TEAM B's claims — this is assessed as a repository/branch
integration defect rather than evidence fabrication — but until the two TEAM A files are merged into the audited
line, CORR8-02/05/08 cannot be certified as evidence-verified-in-place. This finding does not extend to CORR8-09
(Check 4) or to the general sweep (Check 7), both of which verify cleanly. This is not a Boss approval, a
Pre-Development Gate PASS, or a Team C authorization.
