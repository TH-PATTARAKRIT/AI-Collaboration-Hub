# 28 — Prompt Governance Constitution Baseline (STEP030113 / STATE03 Adoption Baseline)

Session ID: [SMEPLUS-26-07-15-001] · Control Level /L99.99 · Mode: CONTROLLED DECISION IMPLEMENTATION
Current Prompt ID: STEP030113 · Parent Prompt ID: STEP030112 · Reference Prompt IDs: STEP030111, STEP030110, STEP030109, STEP030108
Evidence Link: https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/pull/33
Final Approval Authority: Boss — Sole Final Approver

---

## 0. Existing Constitution Search Result and Disposition

A repository-wide search was performed before drafting this file (this Prompt, pre-flight §5 item 14–15; see `26_STEP030113_BOSS_DECISION_IMPLEMENTATION_RECORD.md` §3).

- **No canonical Prompt Governance Constitution exists on `SMEsPlus` or the PR #33 branch.**
- **An unmerged candidate exists:** PR #36, "[Governance] SMEsPlus Prompt Governance Constitution v1.0 (ERPPLUS-96)", opened by the `chatgpt-codex-connector` GitHub App on branch `governance/prompt-governance-constitution-v1`, file `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_PROMPT_GOVERNANCE_CONSTITUTION_v1.0.md`. State: OPEN / DRAFT / NOT MERGED. This is a **new finding**, not previously recorded anywhere in the STEP0301 package before this Prompt.
- PR #36's own file header self-declares `Status: BOSS DIRECTIVE — EFFECTIVE IMMEDIATELY; BASELINE INCORPORATION PENDING GOVERNANCE CHANGE REVIEW`. Per this package's established convention for self-declared authority inside unmerged PRs (see CONF-14, File 05, applied to PR #34's self-declared approval record), a status claim made **inside an unmerged draft PR** is **PR_ONLY / UNVERIFIED** until independently reviewed and merged — it is not treated as binding on STATE03 by virtue of its own text alone.
- A separate `PROJECT_CONSTITUTION.md` exists on `SMEsPlus` (`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`, Status: Approved, Approved By: Boss). It is a broader project constitution (authority model, execution flow) and does **not** define the Prompt ID naming standard, Session Traceability field set, or evidence-classification taxonomy this Prompt is instructed to baseline. It is not a competing Prompt Governance Constitution and is not superseded by this file.

**Disposition:** This file (28) does **not** compete with, duplicate, or attempt to supersede PR #36's candidate document. It is created as a **STEP0301/STATE03-scoped controlled adoption baseline** — a codification of the prompt-governance practice this package (Files 00–27, STEP030101–STEP030113) has already followed, so that STATE03's remaining Steps (STEP0302–STEP0311) have a stable reference. Reconciliation between this file and PR #36 (which one becomes the single project-wide canonical Constitution, or whether both are merged into one) is a **future repository-governance action**, not decided here. Project-wide canonical placement of any Prompt Governance Constitution — including whether `00_Project_Governance/` or `03_Architecture/STEP0301_.../28_...` is the correct canonical home — remains undecided; no Governance Index found on the target branch clearly authorizes this STEP0301 directory as project-wide source of truth (see §16).

**Conflict reported:** PR #36 and this file independently arrive at overlapping rules (Prompt ID form `STEPxxyyzz`, Session Traceability, Boss as sole approver, Clean Room, No Evidence = No Progress). No rule in this file contradicts PR #36's rules as read; both are recorded here so Boss can decide formal reconciliation (recommended scope: STEP0303 or STEP0309, per File 27).

## 1. Purpose and Authority

This Constitution baseline establishes the mandatory structure for controlled Prompts within STATE03 of the SMEsPlus Enterprise Suite program, so that every Prompt's traceability, evidence classification, and approval boundary are independently verifiable from repository evidence alone. Authority to approve, amend, or supersede this baseline rests solely with Boss.

## 2. Naming Standard

- **Step ID:** `STEPxxyy` — `xx` = STATE number (two digits), `yy` = Step sequence within the STATE (two digits). Example: `STEP0301` = STATE 03, Step 01.
- **Prompt ID:** `STEPxxyyzz` — `zz` = Prompt sequence within the Step (two digits). Example: `STEP030113` = STATE 03, Step 01, Prompt 13 (this Prompt).
- Prompt IDs are never reused, renumbered to fill a gap, or reassigned after issuance. A defect in an issued Prompt ID (e.g., a labelling collision) is corrected by an annotated record (see File 21 §1a for a worked example), not by silently renumbering history.

## 3. Mandatory Session Traceability

Every controlled Prompt output must carry:

- Current Prompt ID
- Parent Prompt ID
- Reference Prompt IDs
- Evidence Link (the governing Pull Request URL)
- Commit SHA (recorded at completion, not guessed in advance)
- State Status
- Step Status

This baseline's own compliance: see §22 below.

## 4. Mandatory Model Identity

Every controlled Prompt output must record: AI Provider, Execution Agent, Actual Model Name, Actual Model Version/Model ID, Reasoning/Effort Mode, Runtime/Environment, execution start timestamp (UTC), current and parent Prompt ID, and Human Final Approval Authority. Unavailable platform-managed fields are recorded as `NOT EXPOSED BY PLATFORM — PLATFORM-MANAGED` — never guessed, inferred, or omitted silently.

## 5. Requested Capability Tier versus Actual Model Distinction

A Prompt may request a capability tier (e.g., "high-effort", "L99.99 control level"). The **Actual Model** actually executing the Prompt must always be separately, independently recorded (§4) and must never be silently substituted for, or conflated with, the requested tier. If a lower-capability model executes a high-risk Prompt, this must be disclosed, not concealed (established practice: Files 21 §2, 24 §2, 26 §2 of this package).

## 6. Producer / Reviewer / Decision Owner Separation

Three roles are structurally distinct and must never be collapsed into one actor within a single Prompt's authority claim:

- **Producer (Preparer/Executor):** drafts and executes controlled output. No approval authority.
- **Independent Reviewer:** verifies a Producer's claims from a fresh session/context, ideally cross-provider. No approval authority — a VERIFIED review result is evidence, not approval (File 25 §13).
- **Decision Owner:** Boss, and Boss alone, for any Architecture Gate, Step closure, PR merge, or Build/Release/Deploy/Migration/Production authorization.

An AI agent must never self-describe as the Decision Owner or as having approval authority, regardless of its assigned role in a given Prompt.

## 7. Boss as Sole Final Approver

No Gate, no Step closure, no PR merge, and no Build/Release/Deploy/Migration/Production action may be authorized by any AI agent under any Control Level. This applies uniformly to Claude Code, ChatGPT, and any other AI provider used in this program.

## 8. Evidence Classification

Every controlled Prompt output must classify each material statement as exactly one of:

- **Verified Fact** — independently, mechanically reproducible from live Git/GitHub state or an equivalent authoritative source.
- **Producer Claim** — asserted by the Producer, not yet independently reproduced.
- **Independent Review Result** — the output of a distinct-session (or cross-provider) reviewer's reproduction attempt.
- **Recommendation** — a suggested action, not a decided fact.
- **Assumption** — a load-bearing but unverified premise, explicitly flagged as such.
- **Boss Decision Required** — a fork in the work that only Boss may resolve.
- **Missing Evidence** — a required input that could not be found; recorded as absent, not silently skipped.

## 9. No Evidence = No Progress

No Gap, Conflict, Gate, or Step may be marked closed, corrected, or passed without a stated, checkable evidence reference (commit SHA, file path, checksum, or live query result). A claim without evidence is recorded as a Producer Claim or Missing Evidence, never silently upgraded to Verified Fact.

## 10. ห้ามข้าม Gate (No Skipping Gates)

No Architecture Gate (A/B/C/D) may be passed out of sequence, and no Step may be treated as entered before its stated entry criteria are independently confirmed satisfied. A mapping table, proposal, review record, or Boss-decision-approval record is evidence toward a Gate — it is not, by itself, a Gate PASS (File 25 §13, File 27 §0).

## 11. Git Controls

- No force push.
- No history rewrite.
- No rebase of a shared/reviewed branch without explicit Boss authorization.
- Commits are additive and traceable; a defect in prior committed evidence is corrected by an annotated follow-up commit, not by silently editing history.
- No direct push to a protected base branch (e.g., `SMEsPlus`) — all changes flow through a Pull Request.

## 12. Branch and PR Controls

- Each controlled Prompt operates on its Step's designated working branch; a harness/tooling branch-assignment discrepancy is disclosed and the actual PR branch is used, per established precedent (File 24 §3, File 26 §3), never silently substituted without disclosure.
- No AI agent merges, closes, rebases, or force-pushes any Pull Request without explicit Boss authorization.
- A Pull Request's own body text (including any self-declared "Boss approval," "effective immediately," or "VERIFIED" claim) is classified PR_ONLY / UNVERIFIED until independently reviewed and merged — regardless of which AI platform authored the PR (established practice: CONF-14 on PR #34; §0 above on PR #36).

## 13. Manifest and Checksum Controls

Every controlled package must ship a SHA-256 manifest excluding itself, and every Prompt that adds, removes, or modifies a controlled file must regenerate and re-verify that manifest (`sha256sum -c`) before being reported complete. Duplicate, missing, unexpected, or mismatched records block completion until corrected — they are never concealed or force-reconciled.

## 14. Clean-Room and License Controls

No third-party source code is copied, ported, translated, or structurally imitated into any controlled deliverable. No credentials, secrets, tokens, database dumps, or uncontrolled generated archives may be introduced into the repository under any Prompt.

## 15. Canonical Terminology: Open ERP

The canonical, project-approved product terminology is **Open ERP**. Non-canonical terms (e.g., `Odoo-first`, `Odoo-style`, `Odoo Architecture` used as a project-direction descriptor) must be corrected under separate Boss authorization before being treated as canonical text (see CONF-11, File 05).

## 16. Historical-Source Terminology Labelling

A reference to an upstream open-source project's own module or component name (e.g., `OdooBot`, an upstream module display name in a source-reconciliation record) is not a canonical-terminology violation. Such references must be explicitly labelled `HISTORICAL_SOURCE_REFERENCE — NOT PROJECT CANONICAL TERMINOLOGY` at the point of use (established practice: CONF-13 note, File 05).

## 17. Forbidden Approval Language for AI Agents

No AI agent's output may use unqualified `PASS`, `APPROVED`, `COMPLETE`, `CLOSED`, `VERIFIED` (without a scope qualifier), or `READY FOR MERGE` to describe a Gate, Step, or PR unless that exact status was itself the subject of an explicit, cited Boss decision. Status vocabularies are restricted to values that distinguish evidence-state from approval-state (established practice: File 10 §"Status values (only)").

## 18. Gate Controls

Gate A (Scope Baseline), Gate B (Architecture Baseline), Gate C (Build Ready), and Gate D (Release Ready) each require an explicit, evidence-backed Boss decision to move from HOLD/PARTIAL_EVIDENCE to PASS. No Prompt at any Control Level may issue a Gate PASS on Boss's behalf.

## 19. Closure Controls

A Step is not closed merely because its successor Step's structure is baselined, or because a Gap/Conflict register maps rows to it (File 27 §0). Step closure requires an explicit, separately authorized Step Exit/Closure assessment.

## 20. Supersession and Amendment Controls

This baseline may be amended, extended, or superseded only by an explicit Boss-approved record referencing this file's path and the specific section changed. A future project-wide canonical Prompt Governance Constitution (whether derived from PR #36, this file, or a fresh synthesis) supersedes this STATE03-scoped baseline only upon Boss approval and merge to `SMEsPlus`; until then, this file governs Prompts within the STEP0301 package and is not itself binding outside STATE03/STEP0301 scope.

## 21. Final Report Standard

Every controlled Prompt's final response must include, at minimum: execution status, exact allowed result string, Model Identity, Traceability, live Git evidence (Base/Starting/Final Head/Commit SHA, PR URL), decision/evidence summary, remaining blockers, and the Mandatory Non-Approval/Control Statement for that Prompt.

## 22. Mandatory Non-Approval Statement

Every controlled Prompt output must include an explicit statement of what it does **not** do (close a Step, pass a Gate, merge a PR, authorize Build/Release/Deploy/Migration/Production), naming Boss as sole Final Approver. This file's own such statement is in §23.

This baseline's own compliance with §3 (Mandatory Session Traceability): Current Prompt ID `STEP030113`, Parent Prompt ID `STEP030112`, Reference Prompt IDs `STEP030111, STEP030110, STEP030109, STEP030108`, Evidence Link `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub/pull/33`, Commit SHA recorded in the Final Report and `STEP0301_EXECUTION_LOG.md` at completion, State Status `STATE03 — ACTIVE UNDER CONTROL`, Step Status `STEP0301 — OFFICIAL CURRENT STEP / NOT CLOSED`.

## 23. Constitution Effective Status and Boss Approval Reference

| Field | Value |
|---|---|
| Status | CONTROLLED STATE03/STEP0301 ADOPTION BASELINE — codifies existing practice already followed by Files 00–27 |
| Project-wide canonical status | **NOT ESTABLISHED.** Remains a future, separately authorized repository-governance action; not decided by this Prompt. |
| Relationship to PR #36 | Disclosed candidate, PR_ONLY / UNVERIFIED / NOT MERGED; not superseded, not merged, not competed with (§0) |
| Relationship to `PROJECT_CONSTITUTION.md` | Complementary, not competing — different scope (§0) |
| Boss approval reference | BOSS-DEC-030113-08 (`26_STEP030113_BOSS_DECISION_IMPLEMENTATION_RECORD.md` §4) |
| Effective for | Prompts within `99_SMEsPlus_Enterprise_Suite/03_Architecture/STEP0301_Architecture_Baseline_Inventory/`, STATE03, from this Prompt forward |
| Amendment authority | Boss — Sole Final Approver |

**This Constitution baseline does not itself close STEP0301, does not start STEP0302, does not pass any Gate, does not merge any Pull Request (including PR #33, PR #26, PR #34, or PR #36), and does not authorize Build, Release, Deploy, Migration, or Production. It does not resolve the open reconciliation question between this file and PR #36 — that remains a future Boss decision. Boss is the sole Final Approver.**

No Evidence = No Progress. ห้ามข้าม Gate.
