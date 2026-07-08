# SMEsPlus CLAUDE SKILL ARCHITECT CONTROLLER BLUEPRINT

Document ID: SMEPLUS-SKILL-ARCHITECT-BLUEPRINT-001
Version: v0.1
Status: GITHUB INTAKE COMPLETED / SKILL ARCHITECT CONTROLLER BLUEPRINT PREPARED / STATE-BASED SKILL LIFECYCLE INCLUDED / NO SKILL PACKAGE BUILT / AI PMO REVIEW REQUIRED / CHATGPT L99 REVIEW REQUIRED / BOSS DECISION REQUIRED
Control Level: /L99.99
Prepared By: Claude AI (Skill Architect Controller Designer role, Boss-approved order 2026-07-08)
Nature: DESIGN BLUEPRINT ONLY — NOT the actual SKILL.md package — REPOSITORY FILE PRESERVED (not activated) — awaiting AI PMO / ChatGPT L99 / Boss review and approval
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Branch: SMEsPlus
Actual Path (GitHub-verified): `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/Skill_Design/SMEsPlus_CLAUDE_SKILL_ARCHITECT_CONTROLLER_BLUEPRINT_v0.1.md`
GitHub Intake Commit: fb5f2619bdae95e1e3c1784f6e0ad4bf7643d4db
Generated: 2026-07-08 (Asia/Bangkok)

**MANDATORY CAVEAT:** This document defines the blueprint for how `claude-skill-architect-controller` should be designed and behave. It does not build the Skill. It does not create SKILL.md. It does not create repository files. It does not automate any Make workflows. Every design decision herein is subject to AI PMO review, ChatGPT L99 review, and Boss approval before implementation.

---

## 1. Executive Summary

`claude-skill-architect-controller` is a mandatory meta-skill that must be designed, reviewed, and approved before any other operational Claude Skill is built, packaged, or activated in SMEsPlus.

**Why it must exist first:**
- No operational Skill can be designed in isolation — it requires current State context, evidence snapshots, RACI validation, Make payload schema, and gate status confirmation.
- Boss clarified that Skill design must be state-based, not upfront-comprehensive, to avoid obsolescence if upstream artifacts change.
- This meta-skill enforces the state-based lifecycle principle and prevents broken Skill designs from being activated.

**What it does:**
- Designs Claude Skill blueprints with full State context
- Validates proposed Skill designs against rejection criteria
- Recommends build sequence for operational Skills
- Maintains Skill boundaries (forbidden actions)
- Ensures no Skill self-approves or bypasses governance authority
- Archives Skill versions after State completion to prevent stale reuse

**What it does NOT do:**
- Build actual SKILL.md packages (that is done after blueprint review)
- Approve operational gates (only designs Skills that others will use for gate work)
- Issue governance verdicts (only provides design recommendations)
- Push to GitHub (design blueprints are reviewed before any commit)
- Activate Make automation (only designs automation triggers, does not execute them)
- Replace Boss final decisions (only documents decision inputs)

---

## 2. Purpose of the Skill

`claude-skill-architect-controller` exists to answer the following design question before any operational Skill is created:

**"Is this proposed Skill safe to build, sound in design, properly bounded, and ready for the State where it will operate?"**

If the answer is "no," the Skill must not be built until the design gaps are closed.

If the answer is "yes," the blueprint is ready for AI PMO owner lock, ChatGPT L99 review, and Boss approval.

The Skill's purpose is quality gatekeeping, not speed. A well-designed Skill is better than a fast Skill that fails in production.

---

## 3. Why This Skill Must Exist Before Other Skills

**Problem Statement:** Without a Skill architect controller, operational Skills are built without:
- Confirmation that the State they are designed for is actually the current State
- Evidence that the FDS/evidence register/RACI/Make payload they depend on matches what is live in GitHub
- Validation against the 20 required design fields (business_purpose, owner_work_replaced, trigger_conditions, etc.)
- Review of the 11 mandatory rejection criteria (missing owner purpose, target State, input evidence, etc.)
- Verification that the Skill's forbidden actions are clearly defined and understood
- Confirmation that the Skill's output is actually evidence, not gate-moveable approval
- Documentation of when the Skill should be archived or retired after its State completes

**Result:** Broken Skills, silent failures, gate logic bypasses, unauthorized actions, and skills that become obsolete but are never retired.

**Solution:** Design and approve `claude-skill-architect-controller` first. Use it to review every subsequent Skill design before building SKILL.md.

**Effect:** All downstream Skills are safer, clearer, and aligned with the state-based lifecycle.

---

## 4. State-Based Skill Lifecycle Principle

This meta-skill must enforce SMEsPlus's state-based approach:

```text
Principle:
A Claude Skill is not a permanent truth source.
A Claude Skill is an execution helper that must be synchronized 
with the latest project source of truth before use.
```

**Current source of truth priority (from State-Based Skill Lifecycle Control v0.1):**

1. GitHub verified file / commit / path
2. PMO evidence register
3. Jira / execution ticket where applicable
4. Google Drive evidence archive where applicable
5. Boss explicit decision
6. ChatGPT L99 review result

**Application to this meta-skill:**
Before the Skill architect controller designs any operational Skill, it must verify:
- Latest GitHub commit SHA for the State's evidence files
- Latest evidence register version from AI PMO
- Latest RACI matrix version (currently v0.1.1 per commit 3bd7324e...)
- Latest Make payload schema version
- Latest gate status from ChatGPT L99 or Boss
- No conflicting boss decisions or ChatGPT L99 verdicts from recent reviews

If any source of truth is stale or missing, the Skill design must be marked:

```text
SKILL_REFRESH_REQUIRED / STATE ENTRY HOLD
```

---

## 5. Trigger Conditions

The `claude-skill-architect-controller` Skill is triggered when:

1. **State Planning:** AI PMO or Boss initiates a new State and calls for Skill design review
2. **Operational Skill Proposal:** Someone (team, Human Owner, or another AI role) proposes a new Claude Skill for development
3. **Skill Refresh:** An existing Skill's freshness check fails and the Skill needs redesign before reuse in a new State
4. **Skill Boundary Review:** A suspected Skill boundary violation (e.g., a Skill attempting to approve/close/merge) needs validation
5. **State Entry Gate Failure:** AI PMO cannot answer the 10 State Entry Skill Gate questions (Section 4 of the Lifecycle Control document) and requests Skill design clarity
6. **Rejected Skill Design:** A proposed Skill design is rejected as missing required fields, and the proposer requests the controller to review what's missing
7. **Archive / Retirement:** A State completes, and the controller needs to document which Skill versions should be archived or retired

---

## 6. Expected Inputs

When triggered, the `claude-skill-architect-controller` Skill expects to receive:

```yaml
# Mandatory inputs
state_id:                    # e.g., STATE-04-FUNCTIONAL-DESIGN
state_name:                  # Human-readable State name
owner_work_required:         # Narrative of what work the human Owner must do
skill_needed_description:    # What work the Skill should handle
latest_github_commit:        # Commit SHA of current branch
latest_github_path:          # Repository path to the State's evidence/FDS
latest_evidence_register:    # Path to current evidence register
latest_raci_version:         # Version of RACI matrix in use
latest_make_payload_schema:  # Version/path of Make automation payload contract
current_gate_status:         # Current gate state (DRAFTED / HOLD / REVIEWED / etc.)
current_reviewer:            # Who reviews Skill output (ChatGPT L99 / Boss / etc.)
proposed_skill_name:         # Candidate Skill name
sample_trigger_prompt:       # Example use case or trigger phrase

# Optional inputs (if proposing a full Skill design upfront)
proposed_skill_purpose:      # Business purpose of the Skill
proposed_skill_inputs:       # What data the Skill expects
proposed_skill_outputs:      # What artifact the Skill produces
proposed_skill_forbidden_actions: # Actions the Skill must not perform
proposed_skill_sample_prompt: # Sample trigger
proposed_skill_sample_output: # Sample output for validation
```

---

## 7. Expected Outputs

When triggered, the `claude-skill-architect-controller` Skill produces one of three output packages:

### Option A: State Entry Freshness Confirmation

```yaml
status: SKILL_ARCHITECTURE_READY_FOR_STATE
state_id: <current state>
required_skill_refresh_check:
  latest_github_commit: <verified>
  latest_evidence_register: <verified>
  latest_raci_version: <verified>
  latest_make_payload_schema: <verified>
  current_gate_status: <documented>
  current_reviewer: <confirmed>
next_action: "Proceed to operational Skill design for this State"
```

### Option B: Skill Design Blueprint

```markdown
# <Skill Name> Design Blueprint

## Basic Info
- skill_name: <name>
- business_purpose: <purpose>
- owner_work_replaced: <human work this Skill handles>
- target_state: <which State>
- trigger_conditions: <when it runs>
- expected_input: <required data>
- expected_output: <artifact produced>
- required_evidence: <what must exist before Skill is created>
- allowed_actions: <what Skill may do>
- forbidden_actions: <what Skill must not do>
- reviewer: <who reviews output>
- verifier: <who verifies correctness>
- github_path: <repository path>
- make_payload_fields: <relevant Make automation fields>
- gate_impact: <how output affects gate>
- sample_prompt: <example use case>
- sample_output: <example output>
- activation_condition: <when to turn on>
- archive_or_retire_condition: <when to stop using>

## Detailed Design Sections
[Section detailing the Skill's internal design, not the SKILL.md yet]
```

### Option C: Skill Design Hold / Rejection

```yaml
status: SKILL_DESIGN_HOLD
reason: "<specific reason>"
missing_fields:
  - "<field>"
  - "<field>"
missing_evidence:
  - "<evidence>"
  - "<evidence>"
recommendation: "Cannot recommend build until [specific items] are provided"
next_action: "Provide missing items and resubmit design"
```

---

## 8. Required Evidence Before Action

Before the `claude-skill-architect-controller` can design or recommend building any operational Skill, the following evidence must exist and be verified as current:

| Evidence Item | Source | Verification Method |
|---|---|---|
| Current State ID and name | AI PMO / Boss | Confirmed in active State planning document |
| GitHub repository path | GitHub | Commit SHA verified; file path confirmed |
| Functional Design or requirements | GitHub / PMO evidence register | Version number, timestamp, and path confirmed |
| RACI matrix | GitHub (currently v0.1.1 at commit 3bd7324e...) | Commit SHA verified; latest version confirmed |
| Evidence register | AI PMO | Timestamp current (within past 2 work days) |
| Make automation payload schema | GitHub / Make automation config | Version/path confirmed; schema fields current |
| Gate status from ChatGPT L99 | GitHub / ChatGPT L99 review log | Latest review verdict documented |
| Boss decision (if required) | Boss decision log | Decision ID, date, reason documented |
| Owner assignment | AI PMO owner lock | Named owner confirmed for the State/module |
| Reviewer assignment | AI PMO | Named reviewer confirmed (ChatGPT L99 / Boss / etc.) |

**If any evidence is missing or stale (not updated within past 2 work days for non-repository items), the Skill design must be marked:**

```text
SKILL_REFRESH_REQUIRED / STATE ENTRY HOLD / MISSING_EVIDENCE: [list missing items]
```

---

## 9. Skill Freshness Check

Every time the `claude-skill-architect-controller` is asked to design or validate a Skill, it must perform a freshness check on 7 items:

### Freshness Check Template

```yaml
freshness_check_timestamp: <current datetime>

checks:
  - item: latest_github_path_exists
    evidence: "<commit SHA>:<path>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_fds_or_design_confirmed
    evidence: "<file path>:<version>:<timestamp>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_evidence_register_confirmed
    evidence: "<path>:<timestamp>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_raci_confirmed
    evidence: "<path>:<commit SHA>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_make_payload_schema_confirmed
    evidence: "<schema path>:<version>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_gate_status_confirmed
    evidence: "<AI PMO note | ChatGPT L99 verdict>"
    status: "VERIFIED" | "STALE" | "MISSING"
    
  - item: latest_boss_decision_confirmed
    evidence: "<decision log>:<decision ID>"
    status: "VERIFIED" | "STALE" | "MISSING"

overall_freshness_status: "FRESH_FOR_STATE" | "REFRESH_REQUIRED"
```

**If any check is STALE or MISSING, overall status is REFRESH_REQUIRED, and the Skill design process halts at this point.**

---

## 10. State Entry Skill Gate

Before any Skill is activated for a State, the `claude-skill-architect-controller` must confirm that AI PMO can answer all 10 State Entry Skill Gate questions (from the State-Based Skill Lifecycle Control v0.1):

```text
1. What State is starting?
2. What Owner work is required?
3. What Skill is needed?
4. Is an existing Skill still valid?
5. What upstream data changed?
6. What GitHub commit/path is current?
7. What evidence register is current?
8. What gate rules are current?
9. Who reviews the Skill output?
10. Who approves final State movement?
```

**Output:** A gate confirmation document listing all 10 answers, with sources and timestamps.

**If any answer is missing:** Skill design must be marked `SKILL_REFRESH_REQUIRED / STATE ENTRY HOLD` and processing halts.

---

## 11. Skill Design Review Checklist

The `claude-skill-architect-controller` must review every proposed Skill design against this checklist before recommending build:

```text
SKILL DESIGN REVIEW CHECKLIST

Metadata:
☐ Skill name is clear and follows <noun>-<adjective>-<action> pattern
☐ Business purpose is one clear sentence
☐ Owner work replaced is explicitly named (e.g., "FDS revision work" not "design work")
☐ Target State is documented and current
☐ Skill does not assume it will exist beyond its target State

Inputs / Outputs:
☐ Expected input is documented (data type, format, source)
☐ Expected output is documented (artifact type, path, format)
☐ Sample prompt is provided (realistic use case)
☐ Sample output is provided (realistic example)
☐ Output is evidence, not approval (see Skill Boundary Rules)

Evidence & Verification:
☐ Required evidence (what must exist before Skill is built) is documented
☐ Reviewer is named (ChatGPT L99 / Boss / specific role)
☐ Verifier is named (who confirms Skill output correctness)
☐ Evidence path is documented (where output goes in GitHub)
☐ Traceability to FDS/RACI/gate is documented

Actions & Boundaries:
☐ Allowed actions are listed (draft, revise, package, etc.)
☐ Forbidden actions are listed (no approve, no merge, no gate closure, etc.)
☐ Gate impact is documented (does Skill output move a gate? NO — it should be evidence only)
☐ Make payload fields are documented (if Skill output is routed through Make)
☐ Skill cannot self-review or self-approve (verified)

Governance:
☐ Current RACI matrix version is referenced
☐ Current Make payload schema version is referenced
☐ Skill does not bypass ChatGPT L99, AI PMO, or Boss authority (verified)
☐ Skill does not claim forbidden statuses (PASS, APPROVED, READY, DONE, COMPLETE, CERTIFIED)
☐ Skill archive/retire condition is documented (when to stop using this version)

Activation:
☐ Activation condition is clear (when is this Skill turned on)
☐ Deactivation/archival condition is clear (when is this Skill turned off / versions archived)
☐ Dry-run capability is documented (how to test without live impact)
☐ Rollback plan is documented (how to undo if Skill produces bad output)
```

**Result:** If all boxes are checked, the Skill blueprint is ready for recommendation.  
**Result:** If any box is unchecked, the Skill is flagged for redesign before recommendation.

---

## 12. Claude Skill Package Standard

The `claude-skill-architect-controller` must ensure that every operational Claude Skill, once approved for building, follows this package standard:

```text
<skill-name>/
├── SKILL.md (required — the actual Skill definition)
├── README.md (optional — high-level Skill overview)
├── references/ (optional — documentation referenced by Skill)
│   ├── raci-matrix-reference.md
│   ├── state-lifecycle-reference.md
│   ├── make-payload-schema-reference.md
│   └── <other domain-specific references>
├── scripts/ (optional — executable code for deterministic tasks)
│   ├── validate-skill-boundary.py
│   ├── snapshot-github-evidence.py
│   └── <other helper scripts>
└── assets/ (optional — templates, icons, etc.)
    └── <domain-specific assets>
```

**This blueprint document does NOT create these files.** It defines what they will look like once the Skill is approved for build.

---

## 13. SKILL.md Required Structure

Once a Skill blueprint is approved, the SKILL.md file for any operational Skill must include (at minimum):

```markdown
---
name: <skill-name>
description: <one-line trigger + purpose>
---

# <Skill Title>

## Control Level
/L99.99

## Core Principles
- Drafted only / not approved
- No self-approval
- No gate closure
- Requires ChatGPT L99 / AI PMO / Boss review
- [Other control principles per Skill type]

## Purpose
<Clear one-sentence purpose>

## State Context
- Current State: <STATE-NN>
- Current GitHub commit: <SHA>
- Current evidence register version: <version>
- Current RACI version: <version>
- Current Make payload schema version: <version>

## Execution Mode
A (repo access) / B (chat export) / C (review-revision only)

## Trigger Conditions
<When this Skill is invoked>

## Expected Input
<Data format, source>

## Expected Output
<Artifact type, location, format>

## Allowed Actions
- <action>
- <action>

## Forbidden Actions
- Approve / Pass / Certify / Release / Merge
- Close any gate
- Declare BUILD READY / CODING READY / JIRA READY
- Declare PASS / APPROVED / READY / DONE / COMPLETE / CERTIFIED
- Override ChatGPT L99 / AI PMO / Boss

## Evidence Path
<GitHub path where output goes>

## Reviewer
<Named role>

## Verifier
<Named role>

## Gate Impact
<Does output move a gate? NO — output is evidence only>

## Skill Freshness Rule
Before use, verify:
- Latest GitHub commit: <check>
- Latest evidence register: <check>
- Latest RACI: <check>
- Latest Make payload: <check>
- Current gate status: <check>
- Current reviewer: <check>
- Current Boss decision: <check>

If any check fails, mark SKILL_REFRESH_REQUIRED and stop.

## Archive / Retire Condition
<When to stop using this Skill version>

## Final Response Format
[Template matching Final Status Rule]

Every response must end with one of:
PREPARED ONLY / NOT APPROVED
PUSHED TO GITHUB / NOT REVIEWED
REVIEWED WITH COMMENTS / GATE HOLD
REQUIRES OWNER REVIEW
REQUIRES CHATGPT L99 REVIEW
REQUIRES BOSS DECISION
```

---

## 14. Required YAML Frontmatter Standard

Every Skill's SKILL.md must include this YAML frontmatter (minimum):

```yaml
---
name: <skill-name>
description: |
  <Trigger condition> Use this Skill when <user scenario>.
  <Trigger condition> Use when <scenario>.
  <What it does>. <Boundary constraint: never...>
control_level: /L99.99
state_aware: true
current_state: <STATE-NN>
freshness_required: true
requires_evidence_snapshot: true
---
```

**The `description` field must include:**
- At least two trigger conditions
- What the Skill does
- One or more boundary constraints (what it does NOT do)

**Example:**

```yaml
---
name: smesplus-expert-fds-designer
description: |
  Use when Claude is asked to draft, revise, or package Functional Specification 
  artifacts for SMEsPlus. Use when FDS batch drafting, business rules, gap analysis, 
  traceability, or UI handoff is needed. Drafts and prepares artifacts only; must 
  never approve, pass, certify, release, merge, or declare build/coding/Jira/production 
  readiness.
control_level: /L99.99
state_aware: true
current_state: STATE-04-FUNCTIONAL-DESIGN
freshness_required: true
requires_evidence_snapshot: true
---
```

---

## 15. Required Instruction Sections

Every SKILL.md must include at minimum these sections (in this order):

1. **Role Title** — What role the Skill plays
2. **Control Level** — /L99.99 or /L99
3. **Core Principles** — 5–10 governing principles
4. **Purpose** — One clear sentence
5. **State Context** — Current State, GitHub, evidence, RACI, Make payload versions
6. **Important Capability Boundary** — What the Skill does NOT have access to
7. **Execution Mode** — Mode A/B/C explanation
8. **Trigger Conditions** — When the Skill is invoked
9. **Expected Input** — Data format, source, required preconditions
10. **Expected Output** — Artifact type, location, format, evidence requirements
11. **Allowed Actions** — Explicit list of what the Skill may do
12. **Forbidden Actions** — Explicit list of what the Skill must never do
13. **Evidence Requirements** — What evidence must exist before action
14. **Reviewer / Verifier** — Named roles responsible for review/verification
15. **Gate Impact** — How the Skill's output affects gates (if at all — usually NONE)
16. **Authority Boundary** — May/must-not list (similar to Allowed/Forbidden but for authority)
17. **Skill Freshness Rule** — Mandatory freshness check before use
18. **Archive / Retire Condition** — When to stop using this Skill version
19. **Final Response Format** — Template for how the Skill must end every response

---

## 16. Required References Folder Standard

If a Skill needs reference documentation, it must include a `references/` folder with (at minimum):

```text
references/
├── raci-matrix-snapshot.md
│   Contains: Copy of current RACI matrix version relevant to this Skill
│   Updated: Whenever RACI matrix is updated
│
├── state-lifecycle-snapshot.md
│   Contains: Copy of State-Based Skill Lifecycle Control v0.1 rules relevant to this Skill
│   Updated: When lifecycle rules change
│
├── make-payload-schema-snapshot.md
│   Contains: Current Make automation payload schema this Skill outputs to
│   Updated: When Make payload schema changes
│
└── <domain-specific-references>.md
    Examples: account-posting-rules.md, thai-tax-rules.md, database-design-patterns.md
    Content: Domain-specific guidance the Skill needs to execute correctly
```

**Critical rule:** References must be SNAPSHOTS, not links. If the source files change, the Skill's references become stale. The Skill's freshness check must flag when a snapshot needs updating.

---

## 17. Optional Scripts Folder Standard

If a Skill produces executable helper code, it may include a `scripts/` folder:

```text
scripts/
├── validate-skill-boundary.py
│   Purpose: Self-check that the Skill's output doesn't violate boundary rules
│   Runs: Before Skill produces final output
│   Checks: No PASS / APPROVED / READY / DONE claims; no gate closure attempts
│
├── snapshot-github-evidence.py
│   Purpose: Capture current GitHub commit SHA, evidence paths, timestamps
│   Runs: When Skill is triggered (freshness check)
│   Produces: Evidence snapshot for this execution
│
├── verify-make-payload.py
│   Purpose: Validate that Skill's output matches Make automation payload schema
│   Runs: Before Skill hands off to Make
│   Checks: All required fields present, format correct
│
└── <other helper scripts as needed>
```

**All scripts must be read-only aids,** not executable gatekeepers. The Skill itself, operating under human/Boss oversight, is the gatekeeper.

---

## 18. Optional Assets Folder Standard

If a Skill produces templates, examples, or static assets, it may include an `assets/` folder:

```text
assets/
├── fds-template.md
│   Template for new FDS documents, with section structure
│
├── gap-analysis-template.md
│   Template for gap analysis documents
│
├── evidence-register-template.md
│   Template for evidence register format
│
└── <other domain-specific templates>
```

Assets are reference materials, not executable code.

---

## 19. Skill Boundary Rules

Every operational Claude Skill in SMEsPlus must enforce these boundaries (no exceptions):

### 1. Drafting vs. Approval Boundary
- **Skill may:** Draft, revise, package artifacts
- **Skill must not:** Approve, certify, release, declare PASS

### 2. Evidence vs. Gate Boundary
- **Skill may:** Produce evidence (a file, document, register entry)
- **Skill must not:** Move a gate, declare a gate READY/PASSED/APPROVED

### 3. Recommendation vs. Decision Boundary
- **Skill may:** Recommend (e.g., "recommend the Skill is ready for build review")
- **Skill must not:** Decide (e.g., "this Skill is approved for activation")

### 4. Preparation vs. Execution Boundary
- **Skill may:** Prepare review packs, draft decision materials, collect evidence
- **Skill must not:** Execute the review, make the decision, approve the execution

### 5. Surface Capability Boundary
- **Skill may:** (Per its Execution Mode) inspect files, stage commits, verify checksums
- **Skill must not:** Push without explicit authorization; merge; force-push; modify unrelated files

### 6. State Awareness Boundary
- **Skill may:** Assume current State, artifact versions, gate status (verified at freshness check)
- **Skill must not:** Assume a prior State's context or reuse a Skill from a prior State without freshness check

### 7. Authority Boundary
- **Skill may:** Consult ChatGPT L99 verdicts, AI PMO owner locks, Boss decisions
- **Skill must not:** Override, replace, or substitute for ChatGPT L99, AI PMO, or Boss authority

### 8. Self-Reference Boundary
- **Skill may:** Reference its own boundaries, describe its own allowed/forbidden actions
- **Skill must not:** Review its own output as if it were an independent reviewer; close a gap it authored

### 9. Status Vocabulary Boundary
- **Skill may:** Use internal/working status values (DRAFTED, PREPARED ONLY, IN REVISION, HOLD_WITH_GAPS)
- **Skill must not:** Use final approval status values (PASS, APPROVED, READY, DONE, COMPLETE, CERTIFIED) except as cited examples of what NOT to claim

### 10. Automation Boundary
- **Skill may:** Produce output that WILL BE routed through Make automation
- **Skill must not:** Assume its output automatically triggers Make; assume Make will approve/deploy/merge based on output

---

## 20. Forbidden Actions

Every Claude Skill in SMEsPlus, without exception, must never:

```text
1. Approve any artifact, decision, or gate
2. Pass any gate or status
3. Certify compliance or correctness
4. Release code, data, or configuration
5. Merge any branch
6. Deploy or activate any system
7. Close any gate or status barrier
8. Declare PASS / APPROVED / READY / DONE / COMPLETE / CERTIFIED
9. Declare BUILD READY / CODING READY / JIRA READY / PRODUCTION READY
10. Declare GATE COMPLETE / RELEASE READY / MERGE READY
11. Mark anything as FULLY REVIEWED / VERIFIED / TESTED (implication: approved)
12. Override ChatGPT L99's governance verdict
13. Override AI PMO's owner lock or evidence registration
14. Override Boss's final decision authority
15. Route work around Make automation's payload validation
16. Activate Make automation triggers without explicit handoff
17. Create a gate status that doesn't exist in the current RACI/lifecycle vocabulary
18. Assume prior State's context without freshness check
19. Reuse a Skill version across States without State Entry Skill Gate confirmation
20. Claim skill-authored work is ready for the next State without independent review
```

---

## 21. Owner Replacement Control

When an operational Skill is designed, the blueprint must explicitly document:

```yaml
owner_work_replaced:
  human_work_before: |
    [Describe the human/Owner work this Skill will handle]
  
  skill_work_after: |
    [Describe exactly what the Skill does — NOT what humans will do with Skill output]
  
  boundary_between_skill_and_owner: |
    [Describe the handoff point — where Skill output goes and what Owner does next]
  
  risk_if_skill_fails: |
    [What happens if the Skill produces bad output — manual recovery plan]
```

**Example:**

```yaml
owner_work_replaced:
  human_work_before: |
    Manual drafting of Functional Specification sections, manually creating gap 
    analysis documents, manually building traceability matrices — estimated 40 hours per batch.
  
  skill_work_after: |
    Drafts FDS content, produces gap analysis structure, builds traceability matrix, 
    packages all files with SHA256 manifest — produces prepared artifacts ready for review.
  
  boundary_between_skill_and_owner: |
    Skill outputs to /FDS_BATCH_EXPORT. PMO Owner reviews batch against checklist. 
    ChatGPT L99 reviews for governance. Boss approves. Owner (or ChatGPT L99) may 
    request revisions.
  
  risk_if_skill_fails: |
    If Skill produces FDS with errors/gaps: ChatGPT L99 review catches them. 
    Manual fallback: Owner creates FDS from scratch (restores to pre-Skill time). 
    GitHub rollback: revert to prior batch commit if Skill pushed incorrect files.
```

---

## 22. AI PMO Handoff Rule

Every operational Skill must include clear documentation of how AI PMO receives and routes its output:

```yaml
ai_pmo_handoff:
  trigger: |
    [When does this Skill complete and signal AI PMO?]
  
  output_format:
    artifact_path: <GitHub path>
    artifact_type: <markdown, yaml, json, etc.>
    verification_checksum: <SHA256 or equivalent>
  
  ai_pmo_action:
    lock_owner: <does PMO assign an owner to this work>
    register_evidence: <what evidence paths PMO records>
    route_to_reviewer: <send to ChatGPT L99 / Boss / other>
    update_status: <move from DRAFTED to REQUIRES REVIEW, etc.>
  
  next_milestone:
    reviewer: <who reviews next>
    timeline_sla: <expected turnaround>
    escalation_if_overdue: <route to Boss if past SLA>
```

---

## 23. ChatGPT L99 Review Rule

Every operational Skill must document what ChatGPT L99 reviews when it receives Skill output:

```yaml
chatgpt_l99_review:
  scope: |
    [What does L99 review? Process compliance? Evidence completeness? Boundary violations?]
  
  evidence_l99_checks:
    - no_skill_self_approval: <checks Skill output doesn't claim approval>
    - no_gate_movement: <checks Skill output is evidence only, not gate movement>
    - no_forbidden_status: <checks for PASS/APPROVED/READY/DONE claims>
    - traceability_completeness: <checks all FRs / gaps traced>
    - reviewer_assignment: <checks all owners/reviewers named>
    - github_evidence_paths: <checks all paths exist and match manifest>
  
  l99_verdict_output:
    recommendation: "Skill output is sound / has gaps / requires revision"
    gate_impact: "Output does / does not affect gate movement"
    next_action: "Hand to Boss / Request revision / Ready for next stage"
```

---

## 24. Boss Decision Rule

Every operational Skill must document the decision points where Boss approval is required:

```yaml
boss_decision_points:
  - decision_point_1: |
      [Scenario where Boss must decide]
      Decision options: A, B, C
      Evidence L99 provides to Boss: [what L99 review found]
      Boss decision authority: [can Boss delegate this?]
      Escalation if Boss defers: [what happens if Boss says "unclear, gather more evidence"]
  
  - decision_point_2: |
      [Scenario 2]
  
  - decision_point_N: |
      [Scenario N]

boss_decision_log:
  location: <GitHub or PMO register path>
  format: "Decision ID | State | Skill | Scenario | Boss Decision | Reason | Date"
  required_fields: ["decision_id", "state", "skill_name", "scenario", "boss_decision", "reason", "decision_date"]
```

---

## 25. Make Automation Compatibility Rule

Every operational Skill that produces output meant for Make automation must document:

```yaml
make_automation_compatible:
  make_payload_version: <current schema version>
  make_payload_fields_this_skill_populates:
    - event_type: <what type of event>
    - batch_id: <from Skill input>
    - module: <from Skill input>
    - repo: <static>
    - branch: <static>
    - commit_sha: <from Skill input>
    - source_path: <where Skill output is>
    - target_path: <where Make will deliver>
    - owner_skill: <this Skill's name>
    - reviewer_skill: <next role in chain>
    - evidence_required: <list of outstanding evidence>
    - current_gate_status: <current RACI status value>
    - forbidden_actions: <PASS, APPROVED, MERGE, etc. — what Make cannot do with this output>
    - callback_channel: <PMO Slack / email / GitHub issue for Make to report results>
  
  make_routing_rule: |
    [How does Make decide where to route this Skill's output?]
    Example: "If event_type = fds_batch_prepared, route to ChatGPT L99 for review."
  
  dry_run_mode: |
    [How is this Skill tested in draft mode without triggering live Make automation?]
```

---

## 26. Skill Validation Checklist

Before the `claude-skill-architect-controller` recommends a Skill for building, it must validate:

```text
SKILL VALIDATION CHECKLIST

[] Skill name follows <noun>-<adjective>-<action> pattern
[] Business purpose is one clear sentence
[] Owner work replaced is documented (human work before vs. Skill work after)
[] Current State confirmed (not generic across multiple States)
[] Trigger conditions are clear and realistic
[] Expected input is documented (format, source, required preconditions)
[] Expected output is documented (type, path, evidence requirements)
[] Sample prompt provided (realistic use case)
[] Sample output provided (example artifact)
[] Allowed actions explicitly listed
[] Forbidden actions explicitly listed (include universal 20-item list)
[] Skill cannot self-approve or self-review
[] Skill output is evidence, not gate-moveable
[] Reviewer role named (ChatGPT L99 / Boss / other)
[] Verifier role named (different from Reviewer)
[] GitHub evidence path documented
[] Make payload fields documented (if applicable)
[] Current RACI matrix version referenced
[] Current Make payload schema version referenced
[] Current State-Based Lifecycle Control rules referenced
[] Skill freshness check procedure documented
[] Archive / retire condition documented
[] Skill does not claim forbidden final statuses
[] Skill boundary violations checked (20 Skill Boundary Rules)
[] AI PMO handoff procedure documented
[] ChatGPT L99 review scope documented
[] Boss decision points documented
[] Make automation routing documented (if applicable)
[] Dry-run capability documented
[] Risk assessment and recovery plan documented
```

**If all items are checked:** Skill is ready for build recommendation.  
**If any item is unchecked:** Skill must be redesigned before recommendation.

---

## 27. Skill Build Approval Checklist

After the `claude-skill-architect-controller` validates and recommends a Skill, AI PMO, ChatGPT L99, and Boss must complete this checklist before the actual SKILL.md is built:

```text
SKILL BUILD APPROVAL CHECKLIST

AI PMO Review:
[] Blueprint is complete (all required sections present)
[] Owner assignment is locked (named human or AI role)
[] Evidence registration plan is clear
[] GitHub path is confirmed and accessible
[] RACI/Make routing is correct
[] State Entry Skill Gate questions answered for this State

ChatGPT L99 Review:
[] Skill design respects governance authority
[] Skill design does not bypass AI PMO / Boss
[] Boundary rules are clear and enforceable
[] No self-approval or self-closure mechanism
[] Skill output format enables proper review and evidence tracking

Boss Decision:
[] Skill approved for build
[] Owner assignment confirmed
[] Budget/timeline for Skill development approved
[] Acceptance criteria for Skill testing approved
[] Dry-run scope approved (what is safe to test before live)

Final Approval Gate:
[] All three above reviewers have signed
[] No open concerns remain (or documented exceptions recorded)
[] Skill blueprint is ready to hand to engineering team for SKILL.md creation
```

**Only after ALL items are signed off may the actual SKILL.md be built.**

---

## 28. Example: How to Review a Proposed Skill

Scenario: Someone proposes a Skill called "accounting-posting-review-prep" to prepare review packs for posting rules.

**The `claude-skill-architect-controller` workflow:**

```markdown
# Review of Proposed Skill: accounting-posting-review-prep

## Input Received
- Skill name: accounting-posting-review-prep
- Business purpose: Prepare Accounting Owner review packs for posting rules
- Owner work replaced: Manual review pack assembly
- Target State: STATE-04-FUNCTIONAL-DESIGN
- Sample trigger: "Prepare the posting rules review pack for ACC-001"

## Step 1: Freshness Check
Verify current context:
- Latest GitHub commit: [checked] ✓
- Latest evidence register: [checked] ✓
- Latest RACI v0.1.1: [checked] ✓
- Latest Make payload schema: [checked] ✓
- Current gate status: [confirmed] DRAFTED → REQUIRES OWNER REVIEW
- Current reviewer: [confirmed] Named Accounting Owner (not yet assigned)
- Latest Boss decision: [confirmed] No conflicting decision

Freshness status: FRESH FOR STATE ✓

## Step 2: Validation Against Checklist
[Check all 26 items from Skill Validation Checklist]
Result: 25/26 items checked ✓
Item unchecked: "Archive/retire condition not documented"

## Step 3: Feedback to Proposer
The Skill blueprint is mostly sound. 
One item needs revision: Archive/retire condition.

Questions for proposer:
- When should this Skill version (or any accounting-posting-review-prep version) be archived?
  Example: "After STATE-04 completes, retire all STATE-04 versions; refresh for next State"

## Step 4: Revised Blueprint Submitted
Proposer adds: "Archive after STATE-04 completes; if posting rule changes in next State, refresh with latest rules."

Freshness check 2: [re-check] ✓
Validation 2: [all 26 items checked] ✓

## Step 5: Recommendation
Result: SKILL_BLUEPRINT_APPROVED_FOR_BUILD_REVIEW

This Skill blueprint is sound and ready for AI PMO owner lock, ChatGPT L99 review, and Boss approval before SKILL.md is built.

Next steps:
1. AI PMO locks named Accounting Owner
2. ChatGPT L99 reviews governance boundaries
3. Boss approves build and timeline
4. Engineering builds SKILL.md per approved blueprint
5. Skill is deployed to State-04 only
```

---

## 29. Example: How to Reject an Unsafe Skill

Scenario: Someone proposes a Skill that attempts to "auto-close gaps and move gates based on review packs."

**The `claude-skill-architect-controller` workflow:**

```markdown
# Review of Proposed Skill: auto-gap-closer [REJECTED]

## Input Received
- Skill name: auto-gap-closer
- Business purpose: Automatically close gaps and move gates when review packs are available
- Proposed forbidden actions: [none listed]

## Step 1: Boundary Violation Check
Proposed Skill action: "Automatically close gaps after review pack is delivered"

Boundary violation check:
- Skill Boundary Rule 2 (Evidence vs. Gate): ✗ VIOLATED
  Skill is attempting to move a gate, not produce evidence.
- Skill Boundary Rule 8 (Self-Reference): ✗ VIOLATED
  Skill would be both producing review pack (evidence) and closing the gap (gate movement).
- Forbidden Action #2: ✗ VIOLATED
  "Pass any gate or status" — exactly what this Skill proposes.

## Step 2: Authority Check
Proposed Skill action: "Auto-close gaps when conditions met"

Authority violation check:
- Section 9 (Boss Final Decision Rule): ✗ VIOLATED
  Only Boss can approve gate movement; Skill cannot decide when gates move.
- Section 23 (ChatGPT L99 Review Rule): ✗ VIOLATED
  ChatGPT L99 must review all gate-moving logic; auto-closure removes review.

## Step 3: Rejection Reason
This Skill violates multiple mandatory Skill Boundary Rules and the Boss Final Decision Rule. 

It cannot be approved in its current form.

## Step 4: Feedback to Proposer
Rejection verdict: SKILL_DESIGN_HOLD

Reason: The Skill attempts to perform gate closure, which is a forbidden action.

Recommendation: Redesign the Skill to:
- Produce a review summary and evidence (allowed)
- NOT attempt to close gaps or move gates (forbidden)
- Deliver output to AI PMO, which routes to ChatGPT L99 and Boss for review (allowed)

If this Skill is redesigned to stop before gate closure, it can be reviewed again.
```

---

## 30. Example: How to Approve a Skill for Build Review, Not for Gate Approval

Scenario: A Skill is reviewed and approved for the engineering team to build SKILL.md, but the approval does NOT mean the Skill is approved for operational gates.

**The `claude-skill-architect-controller` clarification:**

```markdown
# Skill Build Approval vs. Gate Approval Distinction

## Key Distinction

SKILL BUILD APPROVAL:
- Means: The blueprint is sound; safe to build SKILL.md; safe to deploy to the specified State
- Does NOT mean: The Skill is approved to close gates, approve work, or bypass review
- Scope: Applies to the Skill's design quality and boundary correctness

GATE APPROVAL:
- Means: A gate may move because Skill output has been independently reviewed and verified
- Requires: ChatGPT L99 verdict + Boss decision
- Scope: Applies to a specific batch's work, not the Skill itself

## Example: FDS Designer Skill

The smesplus-expert-fds-designer Skill is approved for build.
This means: The Skill can be built and deployed to STATE-04-FUNCTIONAL-DESIGN.

This does NOT mean: Any FDS artifact produced by the Skill is automatically gate-approved.

Process:
1. Skill produces FDS artifact (SKILL BUILD APPROVAL applies — Skill is safe to use)
2. Artifact is reviewed by ChatGPT L99 (GATE APPROVAL process starts)
3. ChatGPT L99 issues verdict (approve / revise / reject)
4. Boss makes final decision (GATE APPROVAL issued or denied)

The Skill cannot move the gate. Only the gate approval process can.

## Clarification for This Meta-Skill

This `claude-skill-architect-controller` Skill is approved for design/build.
This does NOT mean: It is approved to approve other Skills for operational gates.

Its role: Validate Skill designs; recommend for build; flag unsafe designs.
Its boundary: Cannot approve operational gates, issue governance verdicts, or replace Boss authority.
```

---

## 31. Recommended First Operational Skill Batch

Based on the State-Based Skill Lifecycle and the current project State, the `claude-skill-architect-controller` should recommend the following build sequence:

### Batch 1: Governance & Dispatch (Prerequisite for all other Skills)

| Priority | Skill | Reason | Dependencies |
|---|---|---|---|
| P0 | claude-skill-architect-controller | Controls all future Skill design quality; meta-skill prerequisite | None — must exist first |
| P1 | ai-pmo-owner-lock | Dispatches work; prevents ownerless execution; locks named owners | Skill architect controller (design standards) |
| P1 | make-automation-controller | Routes Skill outputs; ensures payloads are valid before automation | Skill architect controller + ai-pmo-owner-lock |

### Batch 2: FDS Production & Testing (Core operational work)

| Priority | Skill | Reason | Dependencies |
|---|---|---|---|
| P1 | smesplus-expert-fds-designer | Handles FDS production/revision; currently STATE-04-FUNCTIONAL-DESIGN | Batch 1 complete |
| P1 | qa-uat-package-generator | Converts FDS into testable UAT evidence; prepares for STATE-07 | Batch 1 + FDS Designer |

### Batch 3: Review & Verification (Gating/evidence roles)

| Priority | Skill | Reason | Dependencies |
|---|---|---|---|
| P2 | accounting-posting-review-prep | Prepares posting rule review packs; needed by STATE-04-FUNCTIONAL-DESIGN | Batch 2 (FDS complete) |
| P2 | thai-tax-review-prep | Prepares Thai VAT/WHT review packs; CRITICAL PATH for ACC-001 | Batch 2 (FDS complete) |
| P2 | db-design-review-prep | Prepares DB entity review packs; needed by STATE-03-ARCHITECTURE | Batch 1 + FDS complete |
| P2 | enterprise-api-review-prep | Prepares API contract review packs; needed by STATE-03-ARCHITECTURE | Batch 1 + FDS complete |

### Batch 4: Domain Review & Governance (Verdict roles)

| Priority | Skill | Reason | Dependencies |
|---|---|---|---|
| P3 | intelligently-designed-erp-reviewer | Reviews ERP/accounting logic; informational to gate, not decisive | Batch 2 + Batch 3 complete |
| P3 | chatgpt-l99-gate-reviewer | Independent governance verdict; required for gate approval | All prior Batches staged |

---

## 32. Risks and Controls

### Risk: Skill Becomes Stale Due to Upstream Changes

**Control:** Mandatory State Entry Skill Gate (Section 10) + Skill Freshness Check (Section 9) before every use.  
**Additional control:** Archive/retire condition (Section 21) — Skill versions are frozen after State completion.

### Risk: Skill Authorizes Forbidden Actions (Approve, Merge, Close Gate)

**Control:** Skill Validation Checklist (Section 26) items #11–13 verify no self-approval mechanism.  
**Additional control:** Forbidden Actions list (Section 20) is non-negotiable; Skill Boundary Rules (Section 19) are enforced.

### Risk: Skill Output Is Not Independently Reviewed

**Control:** ChatGPT L99 Review Rule (Section 23) requires ChatGPT L99 to review all Skill output before gate movement.  
**Additional control:** No Skill can move a gate; only a gate approval process (ChatGPT L99 + Boss) can.

### Risk: Skill Is Reused Across States Without Validation

**Control:** Skill Freshness Check flags stale versions.  
**Additional control:** State-aware Skill versioning (Section 4 of Lifecycle Control) — e.g., smesplus-expert-fds-designer__state-04__v0.1 prevents accidental cross-State reuse.

### Risk: Skill Designer Circumvents Approval Process

**Control:** Skill Build Approval Checklist (Section 27) requires three independent sign-offs: AI PMO + ChatGPT L99 + Boss.  
**Additional control:** No SKILL.md is built until all three have signed off.

---

## 33. Items Requiring AI PMO Review

Before `claude-skill-architect-controller` is approved for build, AI PMO must review and confirm:

```text
1. Proposed repository path for Skill blueprints
   Currently proposed: 99_SMEsPlus_Enterprise_Suite/00_Project_Governance/Skill_Design/
   Confirm or correct: [AI PMO to decide]

2. Freshness check SLA thresholds
   How often must Evidence Register be updated? (currently: "within past 2 work days")
   How often must GitHub commits be verified? (currently: per-use)
   Confirm or adjust: [AI PMO to decide]

3. Owner assignment process
   Who nominates initial owners for each Skill? (currently: AI PMO or Boss)
   Who confirms owner availability? (currently: AI PMO)
   Confirm or document: [AI PMO to decide]

4. Evidence path registry
   Where is the master list of approved GitHub evidence paths?
   Should Skill blueprints reference this registry? (currently: assumed yes)
   Create or confirm: [AI PMO to decide]

5. Skill Validation Checklist severity
   Are all 26 items equally required, or are some optional? (currently: all required)
   Can a Skill be approved with 25/26 items checked? (currently: no, all 26 must pass)
   Confirm severity levels: [AI PMO to decide]

6. State Entry Skill Gate
   Who is responsible for answering the 10 State Entry questions? (currently: assumed AI PMO)
   What is the SLA for answering? (currently: not defined)
   Confirm roles and SLA: [AI PMO to decide]

7. Dry-run scope
   What is considered a "safe" dry-run? (currently: draft/sandbox mode, no live gate impacts)
   Who authorizes dry-run execution? (currently: assumed AI PMO)
   Define scope and authority: [AI PMO to decide]
```

---

## 34. Items Requiring ChatGPT L99 Review

Before `claude-skill-architect-controller` is approved for build, ChatGPT L99 must review and confirm:

```text
1. Governance boundary rules
   Are the 20 Skill Boundary Rules (Section 19) comprehensive?
   Are there any gaps where a Skill could claim authority it should not have?
   Review and recommend: [ChatGPT L99 to decide]

2. Skill Validation Checklist
   Does the 26-item checklist (Section 26) catch all governance violations?
   Are there validation gaps? (e.g., cases where an unsafe Skill could pass all checks)
   Review and recommend: [ChatGPT L99 to decide]

3. Forbidden Actions list
   Is the universal 20-item Forbidden Actions list (Section 20) sufficient?
   Are there Skill-specific forbidden actions that should be added per Skill type?
   Review and recommend: [ChatGPT L99 to decide]

4. RACI matrix alignment
   Does this Skill Architect Controller blueprint align with RACI matrix v0.1.1?
   Are there RACI contradictions? (e.g., a Skill is both R and A for gate closure)
   Review alignment: [ChatGPT L99 to decide]

5. Make automation boundary
   Does this Skill's design prevent Make automation from bypassing review?
   Are there scenarios where Make could abuse a Skill's output to approve/merge/deploy?
   Review and recommend: [ChatGPT L99 to decide]

6. State-Based Lifecycle alignment
   Does this Skill Architect Controller enforce the state-based lifecycle principle?
   Are there scenarios where a stale Skill version could be reused without detection?
   Review alignment: [ChatGPT L99 to decide]

7. Boss decision points
   Are Boss decision points (Section 24) documented clearly enough that Skill cannot substitute?
   Are there scenarios where a Skill could implicitly approve something by omission?
   Review and recommend: [ChatGPT L99 to decide]
```

---

## 35. Items Requiring Boss Decision

Before `claude-skill-architect-controller` is approved for build, Boss must decide:

```text
1. SKILL ARCHITECT CONTROLLER APPROVAL
   Approve this meta-Skill for build? (YES / NO / REQUEST CHANGES)
   Decision: [Boss to decide]
   Reason: [Boss to document]

2. FIRST OPERATIONAL SKILL BATCH APPROVAL
   Approve the recommended Batch 1 (ai-pmo-owner-lock, make-automation-controller) for build?
   Decision: [Boss to decide]
   Timeline: [Boss to specify]

3. BUDGET & RESOURCE ALLOCATION
   Budget approved for Skill Architect Controller build/maintenance?
   Resource allocation approved (how much Claude/engineering time)?
   Decision: [Boss to decide]

4. DRY-RUN SCOPE APPROVAL
   What dry-run scope is acceptable before live activation?
   (Currently: draft outputs, no live gate impacts, sandbox Make automation)
   Approve or modify: [Boss to decide]

5. SKILL ARCHIVE POLICY
   When operational Skills complete a State, how long are they archived before deletion?
   (Currently: not specified)
   Decide: [Boss to decide]

6. EXCEPTION AUTHORITY
   If a proposed Skill violates Skill Boundary Rules, can an exception be granted?
   Under what circumstances? (Currently: no exceptions assumed, but not explicitly decided)
   Decide: [Boss to decide]

7. ESCALATION AUTHORITY HIERARCHY
   If a Skill design is rejected by Skill Architect Controller, 
   can the proposer appeal to ChatGPT L99? To Boss?
   Who has final authority over Skill design in case of dispute?
   Decide: [Boss to decide]
```

---

## CONCLUSION

The `claude-skill-architect-controller` is a meta-Skill designed to ensure that all subsequent operational Skills are safe, bounded, fresh, and aligned with SMEsPlus's state-based lifecycle principle.

**This blueprint is NOT the actual SKILL.md.** It is a design specification that must be reviewed by AI PMO, ChatGPT L99, and Boss before engineering builds the actual SKILL.md package.

**Next steps (in order):**

1. AI PMO reviews this blueprint against its ownership checklist (Section 33)
2. ChatGPT L99 reviews this blueprint against its governance checklist (Section 34)
3. Boss issues decision on all items in Section 35
4. Engineering builds `claude-skill-architect-controller/SKILL.md` per approved blueprint
5. First operational Skill batch (Batch 1) receives design review by the new meta-Skill
6. Batch 1 Skills are built and tested in dry-run mode
7. Batch 1 Skills are activated for their target States only
8. Subsequent Skill batches proceed in sequence, each validated by the Skill Architect Controller

---

SKILL ARCHITECT CONTROLLER BLUEPRINT PREPARED / STATE-BASED SKILL LIFECYCLE INCLUDED / NO SKILL PACKAGE BUILT / AI PMO REVIEW REQUIRED / CHATGPT L99 REVIEW REQUIRED / BOSS DECISION REQUIRED
