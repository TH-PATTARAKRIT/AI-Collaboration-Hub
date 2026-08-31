# [SMEPLUS-26-08-31-COA-G01R2-CORR4-001]

# BOSS DIRECTIVE — COA-G01R2-CORR4 Evidence Recovery, Controlled Source Port & Residual Blocker Closure / L99.99

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Authorize controlled CORR4 remediation of remaining COA-G01 evidence blockers before any subsequent Gate | Boss | This directive; ChatGPT audit commit `f37a3076fff7a81bcb2e2e02fadcb0445f91fca8`; Jira `ERPPLUS-132` comment `10920` | 2026-08-31T06:05:53.575Z | Claude executor → ChatGPT Independent Re-audit → PMO → Boss | **AUTHORIZED FOR CORR4 EXECUTION ONLY — NO EXECUTION CREDIT YET** | COA-G01 remains HOLD / EVIDENCE REQUIRED; COA-G02 remains blocked |

## 1. Boss authorization and boundary

Boss directs the project to correct and reconcile the remaining COA-G01 blockers before any subsequent work.

Continue in the **same Claude COA-G01 execution lineage/session**. Do not create a new broad session.

This authorizes COA-G01 source-evidence recovery, provenance, reconciliation and controlled documentation only. It does not authorize COA-G02, Base Kernel discovery, schema/API design, coding, Development, Deployment, Release or Production.

## 2. Current controlling state

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Branch: `SMEsPlus`
- Jira: `ERPPLUS-132`
- CORR3 executor: `37d5fd69e5b0e410bdf514967e60c9099cb7042c`
- CORR3 independent audit: `f37a3076fff7a81bcb2e2e02fadcb0445f91fca8`
- `CORR3 TARGETED REMEDIATION = PASS / VERIFIED`
- `COA-G01 = HOLD / EVIDENCE REQUIRED`
- `COA-G02 = NOT STARTED / NOT AUTHORIZED`
- Boss is the sole Final Approver.

## 3. Mandatory start sequence

1. Fetch `origin/SMEsPlus`.
2. Read this directive, the CORR3 audit, current COA-G01 registers, Evidence Manifest and SHA-256 file in full.
3. Verify branch ancestry and inspect all commits after this directive.
4. If the normal clone contains unrelated unpushed work, do not reset, merge, stage or push it. Use a fresh isolated clone.
5. Reconcile existing evidence before new research.
6. Report any new contradiction or source-integrity failure immediately.
7. Execute only Sections 4.1–4.7.

## 4. Authorized correction scope

### 4.1 Boss-approved Odoo18 workbook recovery — N-01 / Source Class D

ChatGPT independently found and hashed the exact source in the Boss-controlled Drive. The private Drive identifier and access URL are deliberately not published in GitHub.

Controlled source fingerprint:

- Exact title: `Account_Odoo18_19 sent 270369.xlsx`
- Source location: `BOSS-CONTROLLED DRIVE / ACCESS-CONTROLLED`
- MIME type: `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Size: `307308 bytes`
- Observed modified time: `2026-08-21T08:04:15.433Z`
- Raw SHA-256: `0b886e38cc8225e90e4534f04ed2bb6f2300e9f012e4ecc51edc1022e3e471f2`
- Observed source tab: 389 rows, index 0–388, fields `id,name,reconcile,code,account_type`, 14 Account Type labels.
- Independent distribution: Bank and Cash 9; Current Assets 33; Receivable 15; Current Liabilities 79; Fixed Assets 28; Depreciation 16; Payable 10; Non-current Liabilities 4; Equity 4; Income 7; Other Income 14; Cost of Revenue 9; Expenses 160; Current Year Earnings 1.
- Reconcile observation: `True 33 / False 356`.

Executor must use the connected Drive, search the exact title, independently download/read the raw workbook, recompute SHA-256, confirm the actual `Odoo18` tab identity, reproduce the 389-row/14-label result and compare the current GitHub inventory row-by-row. Any hash/row mismatch = `CONFLICTING EVIDENCE` and immediate stop.

**Boss N-01 disposition:** keep the raw binary in access-controlled Drive. Do not commit the `.xlsx`, private Drive ID or private URL to GitHub/Jira. GitHub shall retain title, controlled-source alias, metadata, raw SHA-256, reproducible extraction method, tab identity, row/type counts and exact comparison result.

### 4.2 Boss-provided Thai COA requirements — Source Class E

Build a controlled requirement-source register from:

- `..._AG_BOSS_COA_LOCAL_TH_RULING.md`
- `..._AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md`
- `..._AK_BOSS_THAI_COA_CLOSURE_AUTHORIZATION.md`
- `..._AM_BOSS_COA_SAAS_ARCHITECTURE_AMENDMENT.md`
- `..._AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`
- `..._AQ_BOSS_SAAS_CONTEXT_CLARIFICATION_AND_G01_REMEDIATION_AUTHORIZATION.md`
- this CORR4 directive.

Map each G01 requirement to exact file/section/commit. Keep `BOSS RULING`, `VERIFIED FACT`, `SUPPORTED INFERENCE`, `UNKNOWN` and `EVIDENCE_MISSING` separate. Class E may move from `EVIDENCE_MISSING` only for requirements directly anchored to Boss-authored GitHub rulings.

### 4.3 Local STATE03 evidence port — C-01 / N-02

**Boss port decision:** source-preserving safe port plus manifest.

Inventory the exact local sources supporting S1–S11, T1–T9, `STEP0303R2`–`STEP0303R5` and every local register cited by current COA-G01 evidence.

For every source:

- preserve original relative path, filename, timestamp, byte count and SHA-256;
- classify license/provenance/clean-room status;
- scan for credentials, secrets, customer PII and unrelated project data;
- copy safe textual evidence byte-for-byte into `COA_G01_SOURCE_PORT/STATE03_LOCAL/`;
- do not publish unsafe material; record only hash, exclusion reason, owner, controlled location and Gate impact;
- map old local path → GitHub path;
- do not replace source evidence with a paraphrased summary.

C-01/N-02 may close only when every cited source is safely published and hashed or explicitly registered as inaccessible/excluded.

### 4.4 STEP0303R2 contradiction — C-02 / N-05

Build a chronology from the actual folder, its 11 files and the later registers that said no artifact was found.

- verify existence, timestamps, sizes and hashes;
- preserve both claims;
- determine cause only if evidence proves it;
- otherwise retain `cause = UNKNOWN`;
- use the verified folder/artifacts as controlling evidence for current existence;
- mark earlier “not found” statements superseded for current-existence status only;
- record the unexplained cause as a controlled residual, not a missing current artifact.

C-02/N-05 may resolve for G01 source-control purposes while cause remains UNKNOWN. UNKNOWN must not become FACT.

### 4.5 Dedicated SI-10 classification evidence

Using only verified ported evidence, `l10n_th`, Boss rulings and current registers, prove or hold the G01 classification boundary:

- SaaS Core is country-neutral;
- Thailand-specific rules/data belong to a versioned localization profile/equivalent controlled layer;
- no Odoo table/model/class/ORM/source architecture is adopted;
- source observations are business semantics only;
- Tenant, Company/Legal Entity and Tax Branch contexts are separated where required;
- no schema/API/production implementation design is created.

SI-10 may be `PASS / VERIFIED` only at COA-G01 classification scope after every cited local anchor is inspectable and internally consistent. Execution proof remains deferred.

### 4.6 Thai financial-statement presentation source — Class F / N-04

Boss designates an access-controlled Drive source for G01. Private Drive identifiers and the raw document are not published.

Controlled source fingerprint:

- Exact title: `งบการเงิน 2567.pdf`
- Source location: `BOSS-CONTROLLED DRIVE / ACCESS-CONTROLLED`
- MIME type: `application/pdf`
- Size: `581504 bytes`
- Raw SHA-256: `75bcfff4942234411bde9bcd1456e7c04e5868587196317d8fbf7f998143a573`
- Observed content class: Thai private-company financial statements containing balance-sheet, profit-and-loss, changes-in-equity and note presentation.

**Confidentiality:** do not commit the PDF, private Drive ID/URL, amounts, signatures or personal data. Publish only a redacted structure/line-label taxonomy, title, controlled-source alias, metadata, SHA-256, extraction method and redaction statement.

**Boss N-04 route decision:** route (a), using the Department of Business Development (DBD) as the primary source for financial-statement presentation requirements. Revenue Department sources remain primary for tax claims; tax forms are not substitutes for DBD presentation requirements.

Official anchors:

- https://www.dbd.go.th/storage/law/0fafe207-f3e1-4173-bca7-47c32219a932.pdf
- https://efiling.dbd.go.th/efiling-documents/03_ManualEF.pdf

Reconcile the redacted Boss example to the applicable DBD company form at presentation-line level only. Do not perform G05 Financial Statement Taxonomy design. Class F may close at G01 only when source identity, confidentiality, structural extraction and DBD applicability are evidenced.

### 4.7 B14 control presentation

Do not rewrite historical B14. `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md` remains the controlling COA-specific clean-room artifact selected in CORR2.

Current registers must state:

- B14 itself is not extended;
- all current COA_STANDARD documents are covered by the dedicated check;
- the dedicated check passed the CORR3 independent integrity review;
- B14 non-extension is an intentional method decision, not an unregistered gap.

## 5. Required deliverables

1. `COA_G01_PRIMARY_SOURCE_RECOVERY_REGISTER_R4.md`
2. `COA_G01_BOSS_THAI_COA_REQUIREMENTS_REGISTER_R4.md`
3. `COA_G01_LOCAL_STATE03_SOURCE_PORT_MANIFEST_R4.md`
4. `COA_G01_SOURCE_PORT/STATE03_LOCAL/`
5. `COA_G01_STEP0303R2_CONTRADICTION_RECONCILIATION_R4.md`
6. `COA_G01_SI10_CLASSIFICATION_ANALYSIS_R4.md`
7. `COA_G01_THAI_FINANCIAL_STATEMENT_PRESENTATION_SOURCE_R4.md`
8. updated Source Baseline, Conflict, Open Unknown, Thai Relevance, SI, TBRAC and Clean-Room registers;
9. updated Evidence Manifest and rebuilt SHA-256;
10. updated Gate Report and Boss Gate Evidence Index;
11. `COA_G01_CORR4_POST_PUBLICATION_CLOSURE.md`;
12. `SESSION_CLOSURE_R4.md`.

Every Markdown artifact must contain Item/Task, Owner, Evidence location, Timestamp, Reviewer/Verifier, Verification Status and Gate Impact.

## 6. Final reconciliation and permitted result

Mechanically report:

- workbook SHA and 389-row comparison;
- Classes A–I;
- Class E exact Boss anchors;
- Class F redaction/DBD status;
- C-01/C-02 and N-01/N-02/N-04/N-05 disposition;
- SI-01..SI-10 classification;
- physical/Markdown/SHA-entry counts;
- all remaining UNKNOWN/EVIDENCE_MISSING/CONFLICTING/carry-forward items;
- no source count treated as target COA count;
- no arbitrary 32/389-account freeze.

If every G01 exit criterion is evidenced, executor may report only:

`COA-G01 = PROPOSED PASS / INDEPENDENT AUDIT REQUIRED / BOSS DECISION PENDING`

Otherwise:

`COA-G01 = HOLD / EVIDENCE REQUIRED`

No ChatGPT Audit PASS, PMO verification, Boss approval or Gate closure may be claimed by the executor.

## 7. Git/Jira and stop controls

- Fetch before commit and before push.
- Fast-forward only; no force-push.
- Do not modify unrelated work.
- GitHub evidence before Jira.
- Keep Jira Status/Assignee/Due Date unchanged.
- Stop after publication for ChatGPT Independent Re-audit.
- Do not start PMO, COA-G02, Base Kernel discovery, coding, schema/API, Development or Production.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
