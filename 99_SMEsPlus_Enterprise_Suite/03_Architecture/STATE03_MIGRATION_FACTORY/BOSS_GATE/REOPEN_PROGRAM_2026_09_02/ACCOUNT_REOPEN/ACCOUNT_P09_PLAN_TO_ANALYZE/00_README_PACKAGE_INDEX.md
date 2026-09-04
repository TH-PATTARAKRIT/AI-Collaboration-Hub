# ACCOUNT P09 — PLAN-TO-ANALYZE — PACKAGE INDEX

**Session:** `SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001`
**Process:** P09 — Plan-to-Analyze (Management Accounting / Analytic / Budget) · `/L99999.99999`
**Repository:** `TH-PATTARAKRIT/AI-Collaboration-Hub` · canonical branch `SMEsPlus` (untouched)
**Working branch:** `research/account-p09-plan-to-analyze-2026-09-04-001` · base commit `88f52cd`
**Execution model:** Claude Opus 5 (high) · autonomous · final gate only
**Constitution correction absorbed mid-execution:** `SMEPLUS-26-09-04-ACC-REV2-CORR1` (scope-aware) — no reset, no re-run; see `14` §R1
**Terminal state:** **READY FOR CORE ACCOUNTING RECONCILIATION**, qualified by a PMO recommendation of **HOLD** on four named blockers
**Boss is sole Final Approver. No gate moved, nothing merged, no implementation authorised.**

---

## 1. READ IN THIS ORDER

| Order | File | Why |
|---|---|---|
| 1 | `18_P09_CORE_RECON_HANDOFF_PACK` | the one-paragraph handover and the eight questions for Core Accounting |
| 2 | `07_P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` | the central determination, including the three-truth model |
| 3 | `16_P09_AAS_PLUS` | the root-cause synthesis, the preserved disagreements, and the two vetoes |
| 4 | `17_P09_PMO` | completeness, process controls, and the gate recommendation |
| 5 | everything else, as needed |

## 2. LAYER 1 — CLEAN-ROOM DELIVERABLES

No reference-product file path, model name, method name or code fragment appears in any file below. Claims cite evidence identifiers only.

| # | File | Terminal state |
|---|---|---|
| 00 | `00_README_PACKAGE_INDEX` | this file |
| 01 | `01_P09_MANAGEMENT_ACCOUNTING_MODEL` | 10 positions issued; 2 of 12 required objects absent from the reference pattern, 1 present only as display |
| 02 | `02_P09_ANALYTIC_SEMANTIC_MODEL` | 15 determinations; one record type found asserting at least five different business facts |
| 03 | `03_P09_ANALYTIC_DISTRIBUTION_MATRIX` | 12 carriers; 11 requirements; 3 items open |
| 04 | `04_P09_COST_OBJECT_MODEL` | **the cost object does not exist in the reference pattern and must be authored**; non-asset equipment cost has no precedent |
| 05 | `05_P09_BUDGET_CONTROL_MODEL` | budget control is **not a gate**; the budgetary position object was not found in scope |
| 06 | `06_P09_ACTUAL_VS_BUDGET_TRACE` | the trace is **not traversable**; three figures on three time bases |
| 07 | `07_P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY` | 9 boundary positions; three truths, not two |
| 08 | `08_P09_EVENT_TO_ANALYTIC_MATRIX` | 19 events; 8 produce management truth with no financial counterpart, 2 the reverse |
| 09 | `09_P09_CROSS_PROCESS_OWNERSHIP` | 1 of 8 processes has a coded ownership boundary; 3 Thai items held |
| 10 | `10_P09_EDGE_CASE_MATRIX` | 6 rows confirmed by challenge, 1 disproved, 1 added by the disproof, 5 open |
| 11 | `11_P09_CONTRADICTION_REGISTER` | 19 internal contradictions · 7 disagreements preserved · 7 held · 11 declared unsearched |
| 12 | `12_P09_SOURCE_LINK_REGISTER` | 13 sources; Jira evidence unavailable, class B, cause recorded |
| 13 | `13_P09_EVIDENCE_MANIFEST` | scan results and checksums |
| 14 | `14_P09_REVISION_LOG` | also the research-error log required by the correction |
| 15 | `15_P09_AAS03_CHALLENGE` | 5 candidates confirmed, 1 disproved, 13 corrections, 15 expert findings |
| 16 | `16_P09_AAS_PLUS` | one root cause; 2 vetoes; 7 disagreements preserved |
| 17 | `17_P09_PMO` | **RECOMMEND HOLD** on 4 named blockers |
| 18 | `18_P09_CORE_RECON_HANDOFF_PACK` | handover |
| 19 | `19_P09_SCOPE_OWNERSHIP_MATRIX` | *(added by the correction)* 7 scope violations; context derived from scope, never applied uniformly |
| 20 | `20_P09_DEPENDENCY_REGISTER` | *(added by the correction)* 2 blocking · 7 peer · 9 evidence · 5 decisions · 7 held |

## 3. LAYER 2 — AUDIT QUARANTINE

**Boss / PMO / AI-Audit only.** Contains reference-product identifiers and citations. **Nothing in this directory may be transcribed into a Layer 1 document or any downstream package.**

| File | Contents |
|---|---|
| `LAYER2_AUDIT_QUARANTINE/E00_PRIMARY_EVIDENCE_BASE` | denominator declaration, 70+ evidence items, negative-claim ledger, challenge candidates |
| `LAYER2_AUDIT_QUARANTINE/E01_EVIDENCE_CORRECTIONS_AND_EXTENSIONS` | 6 corrections against the research team, 20 extensions |
| `LAYER2_AUDIT_QUARANTINE/EXPERT_REVIEW/X1_…FUNCTIONAL_DESIGN_REVIEW` | 9 findings; CH-CAND-03 and CH-CAND-04 confirmed |
| `LAYER2_AUDIT_QUARANTINE/EXPERT_REVIEW/X2_…DATABASE_DESIGN_REVIEW` | 6 findings; constraint trigger inventory; CH-CAND-01 and CH-CAND-02 confirmed |
| `LAYER2_AUDIT_QUARANTINE/EXPERT_REVIEW/X3_…INTEGRATION_LOCALIZATION_REVIEW` | 5 findings; Thai enumeration; **CH-CAND-05 disproved** |
| `LAYER2_AUDIT_QUARANTINE/EXPERT_REVIEW/X4_…CODE_UI_ARCHITECT_REVIEW` | 6 findings; access matrix; CH-CAND-06 confirmed |

## 3A. POST-PUBLICATION AMENDMENT

The package was amended after its first commit (`16f884f`) by a **verified incoming correction from the P04 process**. P04 established that a posted asset depreciation allocates **both** legs of a balanced pair, so the two management records are mirror images and **net to zero** — the cost centre is debited and credited in the same posting. P09 re-verified all three steps from primary source before accepting, corrected row E19 of `08`, added rows E20 and E21, added positions EA-06 and EA-07, contradictions CN-20 and CN-21, edge cases EC-56 to EC-59, and accepted peer dependency `P04-PD-04` with position MA-11.

Full record at `14` §R9. **A published P09 finding was corrected by another process; that is recorded, not smoothed over.**

## 4. THE SIX HEADLINE FINDINGS

1. **The management dimension is physical schema, not scoped data.** Eleven independently-found defects follow from that one choice (`16` §2). Fixing them individually would be eleven patches on a representation that regenerates them.
2. **Schema-altering rights over the dimension structure are one settings toggle away from every internal user** — and axis deletion drops a column with cascade, destroying history unenumerated. Ranked first by AAS+.
3. **A management allocation on a posted, lock-dated, hash-chained entry is freely editable, by an ordinary billing role, with no audit trace** — and every budget figure over that period changes silently as a result.
4. **A financial report can present, as posted ledger data, records that were never posted** — the ledger table is replaced by a view built from management records and stamped with a literal posted state.
5. **A dimension-filtered reallocation moves the whole balance when only a share was allocated**, and writes no dimension onto the entries it posts. A misallocation, not a duplication.
6. **Two of the eight constitutional trace steps have no carrier at all** — the financial-event identity and the cost object. The trace cannot be inherited; it must be authored.
7. *(added post-publication)* **An allocation applied symmetrically to both legs of a balanced pair attributes nothing.** Asset depreciation does exactly this, so depreciation reaches the cost centre and leaves it in the same posting. The complementary case — no allocation on the asset — lets each leg find its own, so a balanced pair can be attributed to two different cost objects, producing a residue that corresponds to no economic event.

## 5. CONTROL RESULTS

| Control | Result |
|---|---|
| prohibited verdict vocabulary | mechanical scan across every file in the package — **zero occurrences** |
| clean-room vendor tokens, Layer 1 | mechanical scan — **zero occurrences** (2 substring false positives inside the ordinary English word "quantity", verified) |
| negative-claim standard | every negative carries class A/B/C/D with a declared boundary; **no class upgraded at any point in the session** |
| denominator rule | **caught 2 author defects** — an author-chosen producer list wrong by 5 members, and a population stated in the wrong unit |
| brief-error clause | **fired twice**, both returned as findings by reviewers |
| independent adversarial challenge | **13 corrections and 15 findings returned against the author; none originated with the author** |
| incoming peer correction, verified before acceptance | **1** — a published finding corrected by the P04 process; author-originated material corrections in this session remain **zero** |

## 6. WHAT THIS PACKAGE DOES NOT DO

No approval. No merge. No deployment. No implementation authorisation. No freeze. No statutory claim of any kind. No adjudication between parallel evidence tracks. No conversion of any class B, C or D finding. Nothing in this package was executed against a running system.
