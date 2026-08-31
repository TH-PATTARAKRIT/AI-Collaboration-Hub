# COA-G01 Round 2 — Pre-Prompt Finding Closure Register

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Disposition every Q/R/E/S finding from `DOMAIN_01_ACCOUNTING_CORE_AR_COA_G01R2_PRE_PROMPT_CHALLENGE_AND_READINESS_RECORD.md` | Claude (session SMEPLUS-26-08-30-COA-G01R2-001) | This artifact; cross-referenced R2 deliverables in this folder | 2026-08-31 | ChatGPT Independent Review (pending); Boss (pending) | See per-item disposition | COA-G01 remains HOLD; no item here closes the Gate by itself |

Disposition values used: **RESOLVED** (genuine new evidence closes the question), **PARTIALLY RESOLVED** (real progress, residual gap remains), **OPEN** (unchanged from Round 1), **HOLD** (requires a Boss decision this session cannot make), **CARRY-FORWARD** (explicitly out of G01 scope, routed to a later Gate).

## CORR1 correction notice (2026-08-31)

The Jira-facing summary posted for the original Round 2 comment (`10913`) mislabeled its own item count (stated "13 items" against a list of 19, and folded the S-series into the Q/R/E tally inconsistently). **The authoritative, reproducible count is below.** No individual disposition below was changed by this correction — every Q/R/E/S verdict is exactly as originally determined; only the summary arithmetic and its presentation were wrong.

### Authoritative totals

**AS Prompt §9 scope (Q-01..08, R-01..08, E-01..08 — 24 items, addressed "by ID" per the controlling prompt):**

| Disposition | Count | IDs |
|---|---:|---|
| RESOLVED | **14** | Q-01, Q-02, Q-03, Q-05, Q-06, Q-08, R-01, R-03, R-04, E-01, E-04, E-05, E-06, E-08 |
| PARTIALLY RESOLVED | **4** | Q-07, R-05, R-06, E-03 |
| OPEN | **6** | Q-04, R-02, R-07, R-08, E-02, E-07 |
| **Total** | **24** | |

**S-01..S-05 (Scope/Authority Concerns — tracked separately; not part of the AS §9 "by ID" 24-item requirement, but addressed as part of the overall Round 2 boundary discipline):**

| Disposition | Count | IDs |
|---|---:|---|
| RESOLVED | **5** | S-01, S-02, S-03, S-04, S-05 |

**Combined (Q+R+E+S, 29 items total, for reference only — this combined figure is not the AS §9 count and should not be cited as "the 24"):** 19 RESOLVED, 4 PARTIALLY RESOLVED, 6 OPEN.

## Q — Questions to Consider

| ID | Question | Disposition | Evidence |
|---|---|---|---|
| Q-01 | How will the current published GitHub/Jira state supersede stale statements without rewriting historical evidence? | **RESOLVED** | `COA_G01_CURRENT_STATE_ADDENDUM_R2.md` — builds the full chronology (`00daa7d7` → `157a496` → `c530138`/`8fceca0` → this session) with explicit supersession notes; no historical file altered. |
| Q-02 | Which substantive Team A process, state/event, integration, security, edge-case and migration records belong to mandatory Source Class A? | **RESOLVED** | `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` — full inventory of 62 Team A files across both research rounds, categorized by evidence type with explicit thin/substantial assessment per category. |
| Q-03 | Do the cited 11-item and 20-item Unknown registers represent different scopes or an actual count contradiction? | **RESOLVED — different scopes, not a contradiction** | Confirmed by direct inspection: the **11**-item register is `TEAM_A/09_OPEN_QUESTIONS/UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md` (program-wide, not Domain-01-specific: `Q-01`–`Q-04`, `G-05`–`G-11`). The **20**-item figure is the stated total in `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/11_RESIDUAL_UNKNOWN_REGISTER.md`, which states verbatim: `"TOTAL OPEN AFTER THIS ROUND = 20"` (9 carried forward + 11 new `GAP-D01-14..24`, minus closures). These are two distinct documents at two distinct scopes (program-level open questions vs. Domain-01 residual technical unknowns after the Sonnet deep-synthesis pass) — see `COA_G01_OPEN_UNKNOWN_REGISTER.md` update below for the full reconciliation table. Round 1's C-04 correctly found "20 does not appear in the 11-item file" but did not trace where "20" actually originates; this session closes that trace. |
| Q-04 | Where are the Boss-provided Thai COA requirements and Thai financial-statement presentation example required by Source Classes E and F? | **OPEN — confirmed EVIDENCE_MISSING, independently re-searched this session** | No new location found. Whole-volume search (this session, Explore agent) for Thai financial-statement terms and any workbook/example file found nothing beyond what Round 1 already recorded absent. See `COA_G01_SOURCE_BASELINE_REGISTER.md` classes E/F (unchanged) and `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md`. |
| Q-05 | What source deployment or tenancy facts are directly observable, rather than inferred from absent evidence? | **RESOLVED — no change needed, already correctly scoped** | `COA_G01_SAAS_INVARIANT_COMPLIANCE.md` (Round 1) already separates "G01 classification scope" from "execution scope" and does not assert deployment/tenancy facts beyond source-code observation (SE-15/16 company currency, SE-24-26 lock model). Re-verified this session — no unsupported architecture claim found in any COA-G01 artifact. |
| Q-06 | How are canonical account concept, published template entry, company COA instance and posting account distinguished without using code/name as identity? | **RESOLVED — conceptual distinction only, no production ID/schema designed** | `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` — every one of the 19 Account Types is classified with an explicit "Canonicalization relevance" field distinguishing concept vs. template entry vs. company instance vs. posting account, consistent with SI-05. |
| Q-07 | What does source `reconcile` behavior prove about AR/AP control, partial/full reconciliation, payment matching, clearing and reversal? | **PARTIALLY RESOLVED** | Team A evidence (SE-20 `reconcile` flag, BR-09) is real and cited; it proves *that* a per-account reconciliation flag exists and gates matching eligibility. It does **not** prove partial-vs-full reconciliation mechanics, payment-matching algorithm, or reversal-driven auto-reconciliation depth beyond SE-09 ("reversal auto-reconciles against the original when posting"). Retained as UNKNOWN beyond what SE-09/SE-20/BR-09 state — see `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md`, "Reconcile flag" row. |
| Q-08 | Which Thai statements are source observations, Boss rulings, regulatory facts or real-user validated practices? | **RESOLVED — Evidence Character field now applied throughout** | `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` and `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md` tag every Thai-relevant item with Evidence Character (`Source Observation` / `Boss Ruling` / `Regulatory Verification` / `Real-User Validation` / `Unclassified-Missing`). No source observation is elevated to Thailand-wide fact. |

## R — Risks / Blind Spots

| ID | Risk | Disposition | Evidence |
|---|---|---|---|
| R-01 | Gate Report and embedded session closure show pre-push/pre-Jira state while later archive evidence confirms publication | **RESOLVED** | `COA_G01_CURRENT_STATE_ADDENDUM_R2.md` supersession table. |
| R-02 | Local-only evidence is cited as VERIFIED FACT although GitHub is the declared Source of Record | **OPEN — by design, correctly labeled, not silently fixed** | Round 1 already labels every local-only fact "VERIFIED FACT (local, not yet on GitHub — see C-01)" rather than a bare VERIFIED FACT — this is the correct discipline, not a violation. The underlying gap (local evidence not yet ported to GitHub) remains genuinely open; porting requires a Boss decision on scope/method (`COA_G01_OPEN_UNKNOWN_REGISTER.md` N-02). Confirmed unchanged this session. |
| R-03 | SI-08 is described as HOLD/not PASS and also concluded PASS/VERIFIED | **RESOLVED** | Direct inspection of the current `COA_G01_SAAS_INVARIANT_COMPLIANCE.md` (Round 1 artifact, re-verified this session) shows no internal contradiction: SI-08 is consistently `PASS / VERIFIED (classification scope)` / `HOLD (execution scope, COA-G07)` in every place it appears (the matrix table and Jira comment `10909`). The contradictory state the Five-Unit Challenge observed predates Round 1's remediation and was already cured by it. No further action needed; carried forward as resolved. |
| R-04 | Source is described as single-tenant/on-premise without direct evidence in the reviewed package | **RESOLVED — no such claim found** | Re-reviewed all COA-G01 artifacts this session; no assertion of source deployment topology (single-tenant, on-premise, or otherwise) appears anywhere. Team A evidence (SE-15/16, SE-24) is scoped to company-currency and lock-date fields, not deployment architecture. |
| R-05 | Canonical concept, template, company instance and posting-account layers are not consistently separated | **PARTIALLY RESOLVED** | `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` now applies this distinction consistently for the 19 Account Types. Full architectural design of the four layers remains COA-G04S scope (not attempted here). |
| R-06 | COA is treated mainly as taxonomy while posting events, origin modules, exception lifecycle and SoD dependencies are incomplete | **PARTIALLY RESOLVED** | `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` shows Process (PR-01..07) and Edge-case (EC-01..18) evidence is substantial; Security (SEC-01..05, explicitly scoped out of this domain) and Integration (INT-01..10, coupling-only, "no research performed on the deferred side") evidence is thin by the Team A researchers' own admission. This is not a G01 defect — it is an accurately labeled evidence boundary. Do-Not-Merge controls relying on thin categories (security, integration) are flagged as lower-confidence in the concept-field table. |
| R-07 | Primary workbook is not preserved as controlled evidence although the 389-row extraction exists | **OPEN — confirmed, independently re-verified this session** | `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md` — whole-volume search this session found **zero** copies of the workbook `.xlsx` file or any Drive-sync cache anywhere on the volume. Only the Google Drive URL/ID is recorded. This is worse than a reproducibility gap: the primary artifact is genuinely unrecoverable from this environment if the Drive link ever becomes inaccessible. Registered as N-01 (Round 1) and reconfirmed, not resolved. |
| R-08 | B14 clean-room matrix does not specifically cover the three COA_STANDARD documents | **OPEN — confirmed, and scope has grown** | `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` update (below) — the `COA_STANDARD/` folder now holds **4** documents (the unverified `c530138` file was added after Round 1's gap-check), none of which B14 covers. The gap is unresolved and larger than when first registered. |

## E — Evidence / Validation Concerns

| ID | Concern | Disposition | Evidence |
|---|---|---|---|
| E-01 | Mandatory Source Class A appears partially reconciled | **RESOLVED** | `COA_G01_TEAM_A_SOURCE_CLASS_A_RECONCILIATION_R2.md` — full inclusion/exclusion rationale per evidence category, citing exact file paths. |
| E-02 | Source Classes E and F remain EVIDENCE_MISSING | **OPEN — reconfirmed, not closable without new primary evidence** | Independent re-search this session (Explore agent, whole-volume) found nothing. Genuinely `EVIDENCE_MISSING`; requires a Boss decision on which route to fund (`COA_G01_OPEN_UNKNOWN_REGISTER.md` N-04). |
| E-03 | Workbook provenance and source-row lineage are incomplete | **PARTIALLY RESOLVED** | `COA_G01_WORKBOOK_PROVENANCE_AND_ROW_LINEAGE_R2.md` documents file identity, extraction method, and limitations as completely as the existing evidence allows. The file itself remains unrecoverable locally (see R-07); this is a hard ceiling on how complete provenance can become without new Boss-provided access. |
| E-04 | Mandatory per-concept fields are incomplete | **RESOLVED** | `COA_G01_CONCEPT_FIELD_COMPLETENESS_R2.md` — all 17 mandatory fields from AS §8.7 populated for all 19 Account Types plus the significant cross-cutting concepts already identified in Round 1's `COA_G01_ACCOUNT_CONCEPT_UNIVERSE.md`. |
| E-05 | TBRAC TB-01..TB-13 applicability/compliance matrix is absent | **RESOLVED** | `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md` — new matrix built directly from `THAILAND_BUSINESS_REALITY_USER_FITNESS_CONTROL_V1.md` (commit `d57cca7`), applied at G01 scope. |
| E-06 | Thai WHT timing, Tax Branch and Thai party identity observations may not be regulatory-verified facts | **RESOLVED — Evidence Character correctly applied** | These items (S2, S3, S5) are tagged `Evidence Character: Source Observation`, `Fact Status: VERIFIED FACT (at the source-observation layer only)` throughout — never elevated to `Regulatory Verification`. See `COA_G01_TBRAC_TB01_TB13_MATRIX_R2.md` TB-05. |
| E-07 | Clean-room coverage does not include all COA evidence used by G01 | **OPEN — confirmed, scope grown (see R-08)** | Same finding as R-08. |
| E-08 | Operational hashes were reported as independently recalculated by the Audit VETO advisory lens, but this PMO record does not independently recreate that calculation | **RESOLVED** | This session independently ran and recorded a fresh SHA-256 computation over the full, updated evidence package — see rebuilt `COA_G01_EVIDENCE_MANIFEST.md` and `COA_G01_SHA256SUMS.txt`, with the exact verification command recorded. |

## S — Scope / Authority Concerns

| ID | Concern | Disposition | Evidence |
|---|---|---|---|
| S-01 | G04S/G05/G06/G07 matters could be pulled into G01 | **RESOLVED — boundary held** | No production tenancy, schema, taxonomy, tax-control, or runtime-isolation design was produced this session. All such items remain tagged CARRY-FORWARD throughout. |
| S-02 | Stronger review could silently expand functional scope | **RESOLVED — boundary held** | This session added evidence and reconciliation only; it did not change the 19-type baseline, the `~32` working expectation, or any Boss ruling. |
| S-03 | Team D could be treated as a pre-prompt co-executor | **RESOLVED — not applicable** | No Team D involvement occurred in this session. |
| S-04 | Reviewer questions could become predetermined answers | **RESOLVED** | Every disposition above cites newly-gathered or re-verified evidence, not an assumed answer; items without closing evidence are left OPEN rather than forced closed. |
| S-05 | G01 evidence remediation could be mistaken for Development or Production authority | **RESOLVED — explicit statement below and in every new artifact** | Development Authorization: NOT GRANTED. Production Authorization: NOT GRANTED. COA-G02: NOT STARTED. |

## Additional finding not in the original AR record

A material new conflict was discovered during this Round 2 session and is **not** one of the original Q/R/E/S items: commits `c530138fd33b5651d56e3542be6d35f8d3d72111` and `8fceca04d2f02da80e349408cc4402883d6fbc2a`, pushed to `SMEsPlus` between the AS prompt's publication and this session's start, self-declare `ChatGPT Independent Evidence Review = PASS` with no separate audit artifact, no PMO artifact, and no Jira record. Full investigation and classification (`CONFLICTING EVIDENCE / UNVERIFIED SELF-DECLARED RESULT`) is recorded in `COA_G01_CURRENT_STATE_ADDENDUM_R2.md` and `COA_G01_SOURCE_CONFLICT_REGISTER.md` (new item C-07). Both commits are preserved unmodified.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
