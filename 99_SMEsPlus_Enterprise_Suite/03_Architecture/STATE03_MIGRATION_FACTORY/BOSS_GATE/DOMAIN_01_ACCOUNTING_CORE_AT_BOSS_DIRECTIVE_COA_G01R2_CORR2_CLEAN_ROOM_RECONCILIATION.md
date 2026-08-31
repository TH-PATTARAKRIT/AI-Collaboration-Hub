# [SMEPLUS-26-08-31-COA-G01R2-CORR2-001]

# COA-G01R2-CORR2 — Residual Clean-Room State Reconciliation / L99.99

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Authorize a targeted correction of residual R-08/E-07/C-06/N-03 clean-room state contradictions after CORR1 | Claude executor; ChatGPT Independent Re-audit | This directive; CORR1 commit `7241c6e0195040a611d42a2597d8a48e103bff00`; Jira `ERPPLUS-132` comment `10914` | 2026-08-31 | ChatGPT Independent Re-audit after publication; PMO; Boss (sole Final Approver) | AUTHORIZED FOR TARGETED CORRECTION ONLY | COA-G01 remains HOLD; COA-G02 remains NOT STARTED / NOT AUTHORIZED |

## 1. Authority and current control

Boss directed the team to continue after ChatGPT independently verified the CORR1 publication and identified a residual internal contradiction.

Execute in the **same Claude session**. Do not create a new broad session.

Current control:

- `COA-G01 = HOLD / CORRECTION REQUIRED + EVIDENCE REQUIRED`
- `COA-G02 = NOT STARTED / NOT AUTHORIZED`
- Development Authorization = NOT GRANTED
- Production Authorization = NOT GRANTED
- Do not claim ChatGPT Audit PASS, PMO Verification, Boss approval, Gate PASS, Gate Freeze, or Gate closure.
- Boss remains the sole Final Approver.

## 2. Verified CORR1 baseline

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Branch: `SMEsPlus`
- CORR1 commit: `7241c6e0195040a611d42a2597d8a48e103bff00`
- Jira: `ERPPLUS-132`, comment `10914`
- CORR1 SHA-256: 23/23 entries independently reverified by ChatGPT
- Commit `58ab36d6f8cd70843553de01be892e444ea7b784` removed the accidental fourth `COA_STANDARD` document.
- Current `COA_STANDARD` population relevant to this finding = 3 documents.

## 3. Residual contradiction requiring CORR2

The CORR1 clean-room document correctly states the current branch contains 3 relevant `COA_STANDARD` documents and records:

- 2 = `VERIFIED CLEAN-ROOM BOUNDARY`
- 1 = `COVERAGE GAP`
- the former fourth document is deleted and retained only as historical conflicting evidence.

However, `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md` still states:

- R-08: 4 documents, none covered, scope grown;
- E-07: same stale 4-document/scope-grown condition.

Related C-06, N-03, Gate Report, current-state, closure, index, manifest and SHA statements may therefore no longer describe one consistent current state.

No Evidence = No Progress. Do not paper over this contradiction.

## 4. Mandatory targeted actions

### 4.1 Inspect current branch first

1. Fetch `origin/SMEsPlus`.
2. Verify the current branch head and compare it with this directive's commit.
3. Report any new commit touching:
   - `DOMAIN_01_ACCOUNTING_CORE`
   - `COA_STANDARD`
   - `COA_G01_EVIDENCE`
   - the DOMAIN_01 COA Boss Gate index.
4. Stop for Boss direction if an unresolved overlapping change exists.

### 4.2 Close the remaining explicit disclaimer gap

Update:

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`

Add a direct clean-room boundary statement that:

- `id`, `name`, `reconcile`, `code`, and `account_type` are observed source-workbook column names only;
- they are not proposed SMEsPlus canonical IDs, schema fields, ORM names, table design, or implementation architecture;
- Account Code and Account Name are not canonical identity;
- only business facts and business semantics may be learned.

Do not redesign the document or introduce production architecture.

### 4.3 Reconcile the clean-room control state

Re-read all 3 current `COA_STANDARD` documents after the disclaimer change and update the controlled clean-room review.

Separate clearly:

1. Current branch documents.
2. Historical deleted `c530138` document.
3. Document-level clean-room classification.
4. B14 historical coverage.
5. Current dedicated COA clean-room review coverage.
6. Remaining gap, if any.

Do not claim the historical B14 matrix was changed if it was not changed.

### 4.4 Reconcile every affected register

Inspect and update where required:

- `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md`
  - R-08
  - E-07
  - Q/R/E status arithmetic
- `COA_G01_SOURCE_CONFLICT_REGISTER.md`
  - C-06
  - C-07 current-vs-historical wording
- `COA_G01_OPEN_UNKNOWN_REGISTER.md`
  - N-03
- `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`
- `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`
- `COA_G01_GATE_REPORT.md`
- `COA_G01_EVIDENCE_MANIFEST.md`
- `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md`
- any closure artifact whose current-state statement becomes stale.

Use only evidence-supported statuses. Do not predetermine `RESOLVED`. If remediation is complete but independent verification is pending, state that explicitly. Recompute all summary counts mechanically from the individual rows.

### 4.5 Evidence Manifest and SHA-256

Rebuild the manifest after all corrections.

The operational SHA-256 set must include:

- every current file in `COA_G01_EVIDENCE/` except the checksum file itself;
- Boss authorization artifact AQ already included by the existing convention;
- all 3 current `COA_STANDARD` documents used by the clean-room review.

Record:

- exact entry count;
- reproducible verification command;
- verification result;
- zero missing and zero unexpected entries, or explicitly register any exception.

### 4.6 Controlled closure and publication

Create:

`COA_G01_CORR2_POST_PUBLICATION_CLOSURE.md`

It must contain:

- Item / Task
- Owner
- Evidence location
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact
- current branch
- final commit SHA handling convention
- Jira comment handling convention
- exact corrected findings
- exact remaining open blockers
- statement that COA-G02 was not started.

Then:

1. Fetch again before commit.
2. Commit and push fast-forward only.
3. Post Jira evidence to `ERPPLUS-132` only after GitHub is inspectable.
4. Do not change Jira status, assignee, or due date.
5. Stop for ChatGPT Independent Re-audit.

## 5. Acceptance criteria

CORR2 may be reported as submitted for re-audit only when:

- current `COA_STANDARD` count is consistently stated as 3;
- historical fourth-document evidence is clearly separated from current-state evidence;
- the source-column clean-room disclaimer exists;
- R-08/E-07/C-06/N-03 and all dependent summaries reconcile;
- no stale “4 current documents / scope grown” statement remains;
- Q/R/E arithmetic matches the individual statuses;
- SHA-256 verification includes the 3 current `COA_STANDARD` documents;
- GitHub commit and Jira comment are inspectable;
- no G02/Development/Production work occurred.

## 6. Stop line

This directive authorizes **CORR2 targeted evidence reconciliation only**.

It does not authorize:

- COA-G01 PASS or closure;
- COA-G02;
- Base Kernel discovery;
- production schema, APIs, coding, build, deployment, or release;
- PMO or Boss approval claims;
- deletion or rewriting of historical evidence.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
