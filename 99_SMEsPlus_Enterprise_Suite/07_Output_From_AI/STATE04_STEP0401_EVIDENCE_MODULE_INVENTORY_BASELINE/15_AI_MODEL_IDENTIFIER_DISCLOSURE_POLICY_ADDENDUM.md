# AI Model Identifier Disclosure Policy Addendum

**Document ID:** STATE04-STEP0401-15
**Effective Prompt:** STEP040113
**Effective Session:** SMEPLUS-26-07-16-005
**Authority:** Boss (Sole Final Approver)
**Scope:** All future SMEsPlus AI prompts and repository evidence, across all STATEs and Steps

---

## 1. Background

`12_STEP040112_BATCH1_INDEPENDENT_REVIEW_REPORT.md` §11 identified that no existing constitution document in this repository (`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/PROJECT_CONSTITUTION.md`, `docs/00_Project_Governance/AI_PROJECT_CONSTITUTION.md`, or `99_SMEsPlus_Enterprise_Suite/00_Unified_Engineering_Standard/01_ENTERPRISE_CONSTITUTION.md`) contains a clause governing AI Model identity disclosure, and that prior practice was inconsistent: STEP040108's `30_STEP040108_AI_PLATFORM_MODEL_AND_AGENT_METADATA_CORRECTION.md` recorded the exact model identifier directly in a committed repository file, while STEP040110 through STEP040112 withheld it, citing an unverified "platform-level restriction."

This addendum resolves that gap by establishing a single, Boss-approved, explicit policy for how AI model identity is recorded in repository evidence going forward.

---

## 2. Policy

### 2.1 Exact Identifier Available and Repository Disclosure Permitted

Record the exact runtime model identifier exactly as technically reported by the session's runtime.

### 2.2 Identifier Verified but Repository Disclosure Prohibited

Record exactly:

> VERIFIED IN CURRENT RUNTIME — WITHHELD FROM REPOSITORY BY PLATFORM POLICY

Also record:

- AI Platform
- AI Provider
- Session ID
- Agent Role
- Reason exact disclosure is restricted
- Repository verification limitation

Do not claim that the repository independently proves the exact model string.

### 2.3 Identifier Cannot Be Verified

Record exactly:

> NOT VERIFIABLE FROM CURRENT EXECUTION ENVIRONMENT

### 2.4 Prohibitions

Never:

- Guess a model identifier.
- Copy it from a previous session.
- Treat prior chat memory as durable evidence.
- Claim repository verification when the identifier exists only in live chat.
- Use "WITHHELD" without stating whether runtime verification occurred.
- Invent a platform restriction.

---

## 3. Historical Treatment

STEP040111 and STEP040112 metadata are accepted as **grandfathered controlled evidence** for Batch 1. Their exact model identifiers remain not independently repository-verifiable. Their historical artifacts (`05_STEP040111_BATCH1_EXECUTION_AUTHORIZATION.md`, `12_STEP040112_BATCH1_INDEPENDENT_REVIEW_REPORT.md`, and all other files 00–13) are **not modified** by this addendum or by any prompt in this lineage.

This historical limitation is non-blocking for Batch 1 because:

- Platform and provider are disclosed.
- Session and agent roles are traceable.
- No source-code generation occurred.
- Work was evidence-only.
- Independent Review confirmed all material counts and integrity controls.

The STEP040108 precedent (direct disclosure of `claude-sonnet-5` in a committed file) and the STEP040110–STEP040112 withholding precedent are both treated as historical facts under this addendum; neither is retroactively corrected. This addendum governs treatment from STEP040113 forward only.

---

## 4. Application to This Prompt (STEP040113)

This session's runtime configuration explicitly instructs, as a direct current-session runtime restriction, that the exact model identifier must not be written into any artifact pushed to a repository (commit messages, PR titles/bodies, code comments, or committed file content), and must be confined to the live chat/operator channel only.

Applying Section 2.2 of this policy, `14_STEP040113_BOSS_DECISION_AND_BATCH1_ACCEPTANCE.md` §3 records:

- Exact Model Identifier: **VERIFIED IN CURRENT RUNTIME — WITHHELD FROM REPOSITORY BY PLATFORM POLICY**
- AI Platform: Claude Code
- AI Provider: Anthropic
- Session ID: SMEPLUS-26-07-16-005
- Agent Role: Boss Decision Implementation and GitHub Governance Agent
- Reason exact disclosure is restricted: direct, current-session runtime instruction (not inferred, not guessed, not carried over from a prior session)
- Repository verification limitation: the exact identifier exists only in this session's live runtime/chat context and cannot be independently proven from committed repository content alone

---

## 5. Enforcement

Every future prompt and repository artifact in this project must comply with this addendum.

Non-compliance must be classified as:

- **CONTROLLED FOLLOW-UP** when non-material and truthfully disclosed; or
- **EVIDENCE INSUFFICIENT** when identity claims cannot be substantiated.

---

Boss is the sole Final Approver.
