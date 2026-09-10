# SMEsPlus Deep Research Session Operating Model v1.1

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Project: SMEsPlus ENTERPRISE SUITE  
Control scope: Deep Research / Migration Factory / controlled handoff into SMEsPlus design and development  
Decision authority: Boss — Sole Final Approver  
Effective direction: 2026-08-30 Asia/Bangkok  
Status: **BOSS-DIRECTED SESSION CONTROL BASELINE**  
Global Project Operating Model v1.0: **NOT OVERWRITTEN BY THIS FILE**; this document clarifies the Deep Research execution flow and is the controlled basis for the next visual/baseline revision.

## 1. What the Boss requires

This Deep Research workstream exists to create an evidence-backed knowledge foundation from source code, database/dump, observable behavior, and business facts so that SMEsPlus design decisions can be challenged and verified independently before they enter design or development.

The Boss requires four distinct controls:

1. **Research is separated from analysis/design transformation.**
2. **Team B output is not self-approved and is not automatically an SMEsPlus design baseline.**
3. **An independent reviewer must verify Team B output before it can enter SMEsPlus design/development.**
4. **Claude AI is an execution/design agent that must be challenged against evidence; it is not the Source of Truth and cannot approve its own output.**

Core rule:

`Researcher != Transformer != Independent Reviewer != Developer != Final Approver`

## 2. What this Session does

This Session is not a production-development session and is not a direct vendor-to-SMEsPlus translation exercise.

It must answer, with inspectable evidence:

- What does the source implementation demonstrate as an observed fact?
- What does the database/dump demonstrate as a structural or data fact?
- How do source and database evidence relate?
- What business behavior or semantic meaning is supported?
- What is fact, inference, assumption, unknown, or vendor-specific implementation?
- What domain invariants, mathematical rules, state transitions, events, and functional requirements can be stated vendor-neutrally?
- What gaps, conflicts, legal/license controls, or unresolved questions remain?
- Is the resulting candidate input safe and sufficiently evidenced to be reviewed for SMEsPlus use?

The required clean-room transformation remains:

```text
SOURCE IMPLEMENTATION
    -> OBSERVED FACT
    -> BUSINESS SEMANTIC
    -> DOMAIN INVARIANT / MATHEMATICAL RULE
    -> VENDOR-NEUTRAL FUNCTIONAL SPEC
    -> CANDIDATE SMEsPlus DESIGN INPUT
    -> INDEPENDENT REVIEW
    -> BOSS GATE
    -> APPROVED SMEsPlus DESIGN INPUT
```

Direct vendor ORM/class/method/table/schema -> SMEsPlus class/schema/code translation is prohibited.

## 3. Team Model

### Team A — Research

Team A produces evidence and observed facts. Team A does not authorize SMEsPlus target design.

#### Team A1 — Source / Code / Technical Research

Responsibilities:

- source inventory and identity;
- module/component observation;
- model/field/rule/workflow observation where allowed by clean-room classification;
- technical behavior evidence;
- source-side provenance and evidence indexing;
- explicit distinction between observed behavior and inferred meaning.

Required output class: **RESEARCH EVIDENCE / OBSERVED FACTS**.

#### Team A2 — Database / Data / Behavior Research

Responsibilities:

- database/dump identity and schema census;
- table/column/constraint/relationship evidence;
- data-pattern and data-quality observation;
- behavioral evidence and transaction/data semantics where supported;
- source <-> database correlation support;
- explicit unknowns, DB-only objects, source-only objects, and contradictions.

Required output class: **RESEARCH EVIDENCE / DATA & BEHAVIOR FACTS**.

### Team B — Analysis & Canonical Transformation

Team B consumes only controlled/sanitized Team A evidence and converts it into vendor-neutral SMEsPlus candidate input.

Responsibilities:

- reconcile Team A1 and Team A2 findings;
- distinguish fact / inference / assumption / unknown;
- extract business semantics;
- formulate domain rules and invariants;
- formulate mathematical/accounting rules where applicable;
- define candidate lifecycle/events/state-machine semantics;
- define candidate functional requirements and conceptual domain boundaries;
- identify design options, conflicts, missing evidence, and advancement objectives;
- produce traceability from evidence -> semantic -> candidate requirement/design decision.

Team B output class: **CANDIDATE SMEsPlus DESIGN / FUNCTIONAL INPUT**.

Team B output is **NOT**:

- an Approved SMEsPlus Design Baseline;
- development authorization;
- production code authority;
- physical target schema authority;
- merge/release/deployment authority.

### Team D — Independent Design & Clean-room Review

Team D is the independent reviewer before Team B output may enter SMEsPlus design or development.

Review responsibilities:

- evidence traceability;
- business/domain correctness;
- mathematical/accounting consistency;
- clean-room / IP separation;
- source-implementation contamination risk;
- fact vs inference vs assumption discipline;
- conflict, missing evidence, and unresolved-question review;
- internal design consistency;
- behavioral and regression proof where required.

Allowed dispositions:

- **REVIEW PASS** — evidence-backed candidate may proceed to PMO/Boss Gate;
- **HOLD / RETURN TO TEAM B** — correction required;
- **FAIL / FROZEN** — evidence absent, inaccessible, contradictory, prohibited, or materially unsafe.

Team D cannot self-approve the Boss Gate.

### PMO / Governance Verification

PMO verifies that the review evidence, status, owner, timestamp, reviewer, gate impact, and required artifacts are complete before presenting the item to Boss.

PMO does not replace technical/domain independent review and does not approve the final design baseline.

### Boss Gate

Boss is the sole Final Approver.

Only after Boss approval may the reviewed candidate be promoted to **APPROVED SMEsPlus DESIGN INPUT / BASELINE** for the authorized downstream State.

### Team C / Design / Development

Engineering, migration-adapter implementation, physical schema design, API/code implementation, or other development work may consume only Boss-approved downstream input and only when the appropriate Design/Development Gate is separately authorized.

For this Deep Research control flow, **Team C must not sit between Team B and the Independent Review Gate**.

## 4. Mandatory Handoff Chain

```text
TEAM A1  Source/Code Research ----\
                                  -> TEAM A Evidence Package
TEAM A2  DB/Data/Behavior Research-/
                                         |
                                         v
                         TEAM B Analysis & Canonical Transformation
                                         |
                                         v
                           CANDIDATE SMEsPlus DESIGN INPUT
                                         |
                                         v
                          TEAM D INDEPENDENT REVIEW GATE
                              |                      |
                           HOLD/FAIL               PASS
                              |                      |
                              v                      v
                           TEAM B FIX        PMO GOVERNANCE VERIFY
                                                     |
                                                     v
                                                 BOSS GATE
                                                     |
                                                     v
                                      APPROVED SMEsPlus DESIGN INPUT
                                                     |
                               +---------------------+--------------------+
                               |                                          |
                               v                                          v
                      Architecture/Functional                        Team C / Engineering
                         /UX Design work                         (only if separately authorized)
```

## 5. Status Vocabulary

### Team A

`DRAFT -> EVIDENCE READY -> INDEPENDENTLY VERIFIED / HOLD`

### Team B

`DRAFT -> CANDIDATE INPUT READY -> READY FOR INDEPENDENT REVIEW -> REVIEW HOLD / REVIEW PASS`

### Post-review

`REVIEW PASS -> PMO VERIFIED -> READY FOR BOSS GATE -> BOSS APPROVED -> RELEASED TO AUTHORIZED DOWNSTREAM STATE`

No item may be called `APPROVED SMEsPlus DESIGN` from Team B status alone.

## 6. Required Traceability Chain

Every promoted domain requirement/design decision must be traceable as:

`A-Evidence ID -> Observed Fact -> Business Semantic -> Domain Rule/Invariant -> Team B Candidate Decision -> Team D Review Finding/Disposition -> PMO Verification -> Boss Decision -> Downstream Design/Development Reference`

Missing links are HOLD and receive no progress credit.

## 7. STATE / Board Mapping for this Workstream

The Project Operating Model separates lifecycle, ownership, and execution:

- **STATE** answers where the work is in the project lifecycle.
- **Board** answers who owns the functional/governance decision area.
- **Team** answers who executes the specialized work.

For the current Deep Research / Migration Factory workstream:

- Primary current lifecycle: **STATE03 — Architecture**.
- Primary ownership: **Board06 — Data & Canonical Model**, with Architecture Review responsibilities remaining relevant under the approved STATE03 board mapping.
- Boss-approved reviewed output may later feed **STATE04 — Functional Design** through a controlled handoff; it does not automatically create STATE04 progress.
- Development work remains a separate **STATE06** authorization decision and must not be inferred from Team B or Team D completion.

Board/STATE/STEP percentages remain TBD where approved denominator/weights are absent.

## 8. Claude AI Position

Claude AI may act as an executor within an authorized Team A or Team B task depending on the assigned prompt and evidence boundary.

Claude AI must not:

- become the Source of Truth;
- consume prohibited proprietary implementation as target-design authority;
- self-approve Team B output;
- skip Team D independent review;
- authorize PMO/Boss Gate;
- authorize coding, merge, release, deployment, or production migration.

The Deep Research evidence package must be able to **challenge / cross-check / falsify** Claude's candidate design rather than merely document Claude's conclusions.

## 9. DOMAIN_01 Transitional Interpretation

Existing DOMAIN_01 Team B artifacts and corrective rounds remain preserved as historical and current evidence. This operating-model clarification does not delete or rewrite that history.

For governance interpretation going forward:

- Team B artifacts are treated as **candidate design evidence/input** until the independent review and Boss gates are satisfied.
- Existing ChatGPT independent audit/re-audit rounds are evidence of the independent-review function; they do not become Boss approval.
- PMO/Boss/Development gates remain separate.
- No historical PASS/HOLD status is silently upgraded by this document.

## 10. Visual Revision Rule

The supplied Project Operating Model v1.0 remains historical evidence. The next visual revision should preserve Sections 1-3 unless separately changed, and revise Section 4 so the Deep Research/Migration sub-flow reads conceptually as:

`Team A (A1+A2 Research) -> Team B (Analysis & Canonical Transformation) -> Team D (Independent Review) -> Boss Gate -> authorized Design/Development / Team C Engineering`

The feedback loop must return Review HOLD to Team B, and evidence defects may return to Team A1/A2.

## 11. Governance Principles

- No Evidence = No Progress.
- Never Skip Gate.
- Boss is the sole Final Approver.
- Research evidence is not target implementation authority.
- Team B candidate output is not an approved design baseline.
- Independent review is mandatory before design/development handoff.
- Cross-State work is allowed, but ownership and gate authority must remain explicit.
- No Build / Merge / Release / Deploy / Production Migration is authorized by this document.
