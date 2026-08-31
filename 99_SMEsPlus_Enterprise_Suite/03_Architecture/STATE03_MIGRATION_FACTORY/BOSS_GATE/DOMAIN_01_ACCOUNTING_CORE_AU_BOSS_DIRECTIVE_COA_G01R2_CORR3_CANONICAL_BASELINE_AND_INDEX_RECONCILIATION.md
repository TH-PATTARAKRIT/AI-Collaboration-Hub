# [SMEPLUS-26-08-31-COA-G01R2-CORR3-001]

# COA-G01R2-CORR3 — Canonical Baseline & Evidence Index State Reconciliation / L99.99

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Authorize a narrow correction of AUD2-01..AUD2-03 identified by the ChatGPT independent CORR2 re-audit | Claude executor; ChatGPT Independent Re-audit | ChatGPT audit commit `8f5fa522a3f1a3553584eb5d5063238eec6a88a2`; Jira `ERPPLUS-132` comment `10917`; this Boss directive | 2026-08-31 | ChatGPT Independent Re-audit after publication; PMO pending; Boss sole Final Approver | **BOSS AUTHORIZED — TARGETED CORR3 ONLY** | COA-G01 remains HOLD; COA-G02 remains NOT STARTED / NOT AUTHORIZED |

## 1. Boss decision and current control

Boss approves the proposed narrow `CORR3`.

Continue in the **same Claude execution lineage/session**. Do not open a new broad COA session. Do not begin COA-G02.

Current control remains:

- `COA-G01 = HOLD / CORRECTION REQUIRED + EVIDENCE REQUIRED`
- `COA-G02 = NOT STARTED / NOT AUTHORIZED`
- Development Authorization = NOT GRANTED
- Production Authorization = NOT GRANTED
- PMO Verification = PENDING
- Boss is the sole Final Approver

This directive authorizes correction of the three findings below only. It does not authorize Gate PASS, Gate closure, Base Kernel Discovery, schema/API design, coding, build, deployment, release or Production activity.

## 2. Authoritative baseline

- Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
- Branch: `SMEsPlus`
- CORR2 executor commit: `a4cebfc1b4b9beca9133b5325c93b645d36be822`
- ChatGPT CORR2 independent re-audit commit: `8f5fa522a3f1a3553584eb5d5063238eec6a88a2`
- ChatGPT audit artifact:
  `CHATGPT_AUDIT/DOMAIN_01_ACCOUNTING_CORE_AE_COA_G01_CORR2_INDEPENDENT_REAUDIT.md`
- Jira: `ERPPLUS-132`, comments `10916` and `10917`
- Boss-approved SMEsPlus Local Thailand Account Type target: **19 ACTIVE types**
- `15` is an observed `l10n_th` source-template instantiation count, not the current target capability baseline.
- Source Classes E and F remain `EVIDENCE_MISSING`.
- The Connected Drive re-verification claim from `c530138/8fceca0` remains unverified and must not be used as Gate evidence.
- N-03 is resolved; N-01, N-02, N-04 and N-05 remain open.

## 3. Mandatory start sequence

1. Fetch `origin/SMEsPlus`.
2. Verify that the branch contains audit commit `8f5fa522a3f1a3553584eb5d5063238eec6a88a2`.
3. Compare all commits after that audit commit.
4. Report any overlapping change touching:
   - `DOMAIN_01_ACCOUNTING_CORE`
   - `COA_STANDARD`
   - `COA_G01_EVIDENCE`
   - the DOMAIN_01 COA Boss Gate Evidence Index
   - this directive
5. Stop for Boss direction if an unresolved overlapping change exists.
6. Read the full ChatGPT audit artifact before editing any evidence.

No Evidence = No Progress. Do not infer the branch state.

## 4. Mandatory targeted corrections

### 4.1 AUD2-01 — Reconcile the 15-source-observation vs 19-active-target contradiction

Update:

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`

Requirements:

1. Preserve the historical/source observations:
   - Core source universe = 19
   - inspected `l10n_th` template = 15 instantiated types / 144 rows
   - Odoo18 workbook inventory = 14 observed labels / 389 source rows
2. Add an explicit, prominent controlled supersession statement near the Executive Result and before any design recommendation:
   - the former `15 active + 4 reserved` recommendation is historical/superseded for target design;
   - the Boss-approved SMEsPlus Local Thailand target is **19 ACTIVE Account Types**;
   - template omission is not a business prohibition;
   - source observation count is not target capability count.
3. Rewrite or clearly mark the existing “Controlled Design Recommendation” and “Gate Impact” text so no current reader can interpret `15 active + 4 reserved` as the active SMEsPlus target.
4. Do not delete the 15-type source evidence.
5. Do not invent canonical IDs, schema, ORM, table design or implementation architecture.

### 4.2 AUD2-02 — Remove residual reliance on the rejected Connected Drive / Source Class E/F claims

Update:

`BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md`

Requirements:

1. Replace the current claim that the workbook was “directly re-verified in connected Drive during G01 execution” with evidence-supported wording:
   - the 389-row / 14-label inventory exists as a controlled extraction;
   - the primary workbook is not recoverable in the current environment;
   - the Connected Drive re-verification claim is unverified and not Gate evidence.
2. Classify Source Class E — Boss-provided Thai COA business requirements — as `EVIDENCE_MISSING`.
3. Classify Source Class F — Boss-provided Thai financial-statement presentation example — as `EVIDENCE_MISSING`.
4. Do not use governance rulings, regulatory anchors or generic report names as substitutes for the missing E/F source documents.
5. Preserve the rejected `c530138/8fceca0` claims only as clearly labeled historical conflicting evidence.
6. Update the current independent-review status to cite the ChatGPT audit artifact and commit `8f5fa522...`; the result is `HOLD / CORRECTION REQUIRED`, not PASS.

### 4.3 AUD2-03 — Recompute current counts and unknown status

Update:

- `BOSS_GATE/DOMAIN_01_ACCOUNTING_CORE_AL_COA_CLOSURE_EVIDENCE_INDEX.md`
- `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/COA_G01_OPEN_UNKNOWN_REGISTER.md`

Requirements:

1. Recompute the current evidence-folder count mechanically from the branch.
2. Distinguish:
   - files physically in `COA_G01_EVIDENCE/`;
   - Markdown evidence files included in SHA-256;
   - total operational SHA-256 entries after external AQ and the 3 current `COA_STANDARD` documents.
3. State the current unknown result:
   - N-03 = RESOLVED;
   - N-01, N-02, N-04, N-05 = OPEN;
   - current open N-series count = 4.
4. Correct the Open Unknown Register's top metadata/current summary so it no longer says none are closed.
5. Preserve historical five-open statements only as explicitly dated historical snapshots.

### 4.4 Controlled consistency sweep

Inspect current-state sections of:

- `COA_G01_GATE_REPORT.md`
- `COA_G01_CURRENT_STATE_ADDENDUM_R2.md`
- `COA_G01_EVIDENCE_MANIFEST.md`
- `COA_G01_SOURCE_BASELINE_REGISTER.md`
- `COA_G01_SOURCE_CONFLICT_REGISTER.md`
- `COA_G01_PRE_PROMPT_FINDING_CLOSURE_REGISTER_R2.md`
- `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`
- `COA_G01_CORR2_POST_PUBLICATION_CLOSURE.md`
- any current Boss Gate index/summary that consumes these facts

Search for and reconcile all current-state occurrences of:

- `15 active` / `4 reserved` used as current target;
- `directly re-verified` / Connected Drive used as verified Gate evidence;
- Source Class E/F shown as verified or reconciled;
- open unknown count = 5 after N-03 resolution;
- evidence folder count = 21 after CORR1/CORR2;
- ChatGPT independent audit = pending/not yet performed after commit `8f5fa522...`;
- current 4-document `COA_STANDARD` claims.

Historical text may remain only when clearly dated and explicitly superseded. Do not silently rewrite history.

## 5. Required CORR3 output

Create:

`TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/COA_G01_CORR3_POST_PUBLICATION_CLOSURE.md`

It must contain:

- Item / Task
- Owner
- Evidence location
- Timestamp
- Reviewer / Verifier
- Verification Status
- Gate Impact
- branch and pre-execution head
- exact files changed
- exact disposition of AUD2-01, AUD2-02 and AUD2-03
- current evidence-folder count
- current open-unknown count
- current Source Class E/F status
- current workbook-provenance status
- final commit SHA handling convention
- Jira comment handling convention
- exact remaining substantive COA-G01 blockers
- statement that COA-G02 was not started

Append a clearly labeled CORR3 section to the Gate Report and update the Evidence Manifest where the operational set changes.

## 6. Evidence Manifest and SHA-256

After all edits:

1. rebuild `COA_G01_EVIDENCE_MANIFEST.md`;
2. rebuild `COA_G01_SHA256SUMS.txt`;
3. include every current file in `COA_G01_EVIDENCE/` except the checksum file itself;
4. retain the existing AQ artifact convention;
5. include all 3 current `COA_STANDARD` documents;
6. record the exact entry count;
7. run the recorded verification command;
8. report zero missing, zero unexpected, zero duplicate paths and every hash result, or register each exception explicitly.

Do not copy the prior count without recomputing it.

## 7. Acceptance criteria

CORR3 may be submitted for ChatGPT re-audit only when:

- the Account Type source-reconciliation standard cannot be read as authorizing a 15-active target;
- the 19 ACTIVE Boss baseline is explicit and traceable;
- the Connected Drive claim is not represented as verified Gate evidence;
- Source Classes E/F remain explicitly `EVIDENCE_MISSING`;
- N-03 is resolved and exactly four N-series unknowns remain open;
- evidence-folder and operational SHA counts are mechanically reproducible;
- current-state summaries agree;
- historical statements are preserved only with explicit supersession labels;
- SHA-256 verification passes;
- GitHub commit and Jira evidence are inspectable;
- no COA-G02, Development, Production, schema, API or coding work occurred.

## 8. Publication sequence

1. Fetch again immediately before commit.
2. Stop if an overlapping branch change exists.
3. Commit and push fast-forward only.
4. Verify the GitHub commit and changed files are inspectable.
5. Post a Jira evidence comment to `ERPPLUS-132` only after the GitHub commit exists.
6. Do not change Jira status, assignee or due date.
7. Stop for ChatGPT Independent Re-audit.

## 9. Prohibitions

Do not:

- open a new broad Claude session;
- start COA-G02 or later Gates;
- discover or freeze the Base COA Kernel;
- freeze 32 or 389 target accounts;
- change the 19 ACTIVE Boss baseline;
- convert EVIDENCE_MISSING into FACT;
- infer or recreate missing workbook/Thai statement evidence;
- modify B14 unless separately authorized;
- claim ChatGPT Audit PASS, PMO Verification, Boss Gate PASS or Gate closure;
- design production schema, APIs or implementation;
- code, build, deploy or release;
- change Jira status, assignee or due date;
- delete historical evidence.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.

## 10. Stop line

Stop after CORR3 evidence is committed, pushed, verified and recorded in Jira.

Report:

- final commit SHA;
- direct GitHub links;
- Jira comment ID;
- exact file count and SHA result;
- AUD2-01..AUD2-03 disposition;
- remaining blockers;
- `COA-G01 = HOLD / CORRECTION REQUIRED + EVIDENCE REQUIRED`;
- `COA-G02 = NOT STARTED / NOT AUTHORIZED`.

Do not continue without the next Boss decision.
