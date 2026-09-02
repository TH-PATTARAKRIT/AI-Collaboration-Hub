# SMEsPlus Lifecycle Standard — Understand -> Transfer -> Document & Preserve

Document ID: `SMEPLUS-GOV-UTP-001`  
Version: `1.0`  
Status: `BOSS APPROVED / EFFECTIVE`  
Effective Date: `2026-09-02`  
Project: `SMEsPlus ENTERPRISE SUITE`  
Jira: `ERPPLUS-141`  
Control Level: `/L999.999`  
Final Approval Authority: `Boss — Sole Final Approver`  
9-Veto Challenge Evidence: `d4bcf801c350becf6bff05cd7cf3b435bfccd086`

---

## 1. Boss Ruling

Boss approves and declares effective the following lifecycle operating principle:

> **เข้าใจให้จริง -> ส่งต่อให้ตรง -> รักษาไว้ด้วยหลักฐาน**

> **Understand deeply -> Transfer accurately -> Document & Preserve verified understanding.**

This standard applies across controlled SMEsPlus lifecycle work wherever material knowledge, business semantics, design intent, implementation understanding, verification findings or operational learning must pass from one owner/team/stage to another.

The principle is intentionally simple. It does not create a new numbered STATE and does not replace existing Evidence Gates, Veto Challenges, IBPV, Team D, IDTM, IESA or Boss approval.

It strengthens the quality of what is learned, handed off and preserved.

---

## 2. Three Mandatory Responsibilities

### 2.1 UNDERSTAND — ทำความเข้าใจ

The owning team must reach **Verified Understanding**, not merely produce a summary.

Material understanding should cover, as applicable:

- `WHAT` — what exists / what the capability or fact is;
- `HOW` — process, state, event, data and control behavior;
- `WHY` — business/control/accounting/system reason where evidence supports it;
- `WHAT IF` — partial, cancel, reject, reverse, failure, retry, exception, multi-company, migration and other material edge conditions;
- `BOUNDARY` — what this owner/domain controls and what it does not;
- `EVIDENCE` — what evidence supports each material conclusion;
- `UNKNOWN / CONFLICT` — what remains unresolved or contradictory.

Mandatory rule:

`Understanding without sufficient evidence = Hypothesis, not Verified Knowledge.`

A genuine Unknown may remain if evidence does not exist, but it must be explicit and controlled.

Target:

`Material Understanding Complete = Material Unknowns resolved OR explicitly controlled with owner, evidence status and Gate impact.`

---

### 2.2 TRANSFER — ส่งต่อความเข้าใจ

A handoff is not complete merely because a file, link, ticket or document has been sent.

The receiving party must be able to correctly distinguish, as applicable:

- verified fact;
- observed behavior;
- business semantic;
- approved decision;
- hypothesis;
- unknown;
- contradiction;
- boundary / ownership;
- carry-forward control;
- what the receiver may trust;
- what the receiver must not assume.

Where material, use **Teach-Back**:

```text
Owner explains
-> Receiver questions/challenges
-> Receiver explains back
-> Owner/reviewer checks semantic accuracy
-> Handoff accepted or corrected
```

Mandatory rule:

`File Sent != Knowledge Transferred.`

### Independent-Team Protection

At an independent lifecycle boundary, especially `Team A -> Team B`, Teach-Back is used to confirm correct understanding of evidence, facts, boundaries and Unknowns. It must not become an Answer Key that dictates the receiving team's independent target conclusion.

`Transfer knowledge, not predetermined conclusions.`

---

### 2.3 DOCUMENT & PRESERVE — ทำเอกสารและรักษาความเข้าใจ

Documentation exists to preserve verified understanding and its evidence lineage; documentation is not the primary proof that understanding exists.

Mandatory principle:

`Documentation != Proof of Understanding.`

Material canonical records should preserve, as applicable:

- what is understood;
- why it is understood that way;
- evidence location / immutable reference;
- business/process/state/event semantics;
- exceptions / negative cases;
- ownership / boundaries;
- cross-domain effects;
- Unknowns / conflicts;
- decisions / overrides;
- rejected assumptions;
- what next team may trust;
- what next team must not assume;
- carry-forward actions / Gate impact.

Evidence should be captured during the work. Teams must not wait until final documentation and then reconstruct provenance from memory.

```text
During work -> Working Evidence Capture
After verified understanding / transfer -> Canonical Preservation
```

---

## 3. Definition of Done

### UNDERSTANDING DONE

Use only when:

`Owner can explain and defend the material understanding with evidence, and material Unknowns are resolved or explicitly controlled.`

### TRANSFER DONE

Use only when:

`Receiver can accurately teach back the material facts, boundaries, Unknowns and no-assumption controls required for its role.`

### DOCUMENTATION / PRESERVATION DONE

Use only when:

`Verified understanding, evidence lineage, material Unknowns, decisions, boundaries and handoff constraints are preserved in an inspectable canonical record.`

None of the three statuses automatically equals lifecycle Gate PASS. Existing Gate authorities remain unchanged.

---

## 4. Lifecycle Application

| Lifecycle Stage / Handoff | UNDERSTAND | TRANSFER | DOCUMENT & PRESERVE |
|---|---|---|---|
| Team A Learning / Evidence | Source facts, semantics, behavior, Unknowns, provenance | Transfer neutral verified knowledge to Evidence Gate / Team B | Evidence pack, Unknown/Conflict register, provenance, no-assumption notes |
| Team A -> Team B | Team A knows what evidence proves and does not prove | Team B correctly receives facts/semantics/Unknowns without target Answer Key | Controlled Team A handoff / frozen evidence inputs |
| Team B Design | Team B understands approved inputs and owns independent canonical design reasoning | Transfer controlled business/design intent to Figma/IBPV | Canonical design, decisions, assumptions, interfaces, constraints |
| Team B -> Figma/UX | Business rules, states, exceptions and constraints understood | UX team can teach back intended user/business behavior | UX handoff record and traceability |
| Figma -> IBPV | Design intent and interaction semantics understood | IBPV receives testable/verifiable design without losing context | Figma evidence + design traceability |
| IBPV -> Pre-Dev / Team C | Verified findings, conditions, gaps and approved decisions understood | Team C receives only Boss-authorized/frozen implementation inputs | Verification record, corrections, Boss decision, handoff pack |
| Team C Development | Engineers understand design contracts, invariants and exceptions | Transfer implementation behavior/evidence to Team D/testing | Code/PR/design references, test evidence, implementation notes |
| Team C -> Team D / Testing | Implementation contract and known risks understood | Independent testers understand what was built without inheriting the builder's verdict | Test baseline, known limitations, evidence references |
| Team D / IDTM / IESA | Findings and system behavior understood independently | Transfer findings without suppressing disagreement | Defect, test, assurance, residual-risk and evidence records |
| Production / Operations | Approved operating behavior, limits, monitoring and recovery understood | Operations/customer-support handoff where applicable | Runbook, monitoring baseline, incident/lesson evidence |

---

## 5. 9 Veto Challenge Integration

The `9 Veto Challenge Council` may challenge all three responsibilities:

```text
UNDERSTAND -> Is the understanding deep, evidence-backed and correctly bounded?
TRANSFER -> Did the receiver receive the correct meaning without distortion or Answer Key contamination?
PRESERVE -> Can the understanding and evidence be reconstructed later without losing context?
```

A material failure may result in `HOLD`, `REWORK REQUIRED`, `EVIDENCE MISSING` or other status permitted by the applicable Gate.

The `9 Special Team Challenge` is activated only under its existing material-trigger rules.

---

## 6. Special Team Learning-Absorption Rule

A Special Team may investigate and solve a hard problem, but the owning team must not treat the Special Team as a permanent substitute for domain understanding.

Where the Special Team finding materially changes the owning team's work, before applicable Gate closure the owning team must absorb, as relevant:

- why the original understanding was incomplete or wrong;
- what evidence changed the conclusion;
- the corrected reasoning pattern;
- the material invariant / control;
- applicability boundary;
- how to detect the same pattern in the future.

Mandatory rule:

`Special Team may solve the hard problem; the owning team must absorb the learning before Gate closure where applicable.`

---

## 7. No Endless Research Rule

This standard does not require every person to know everything or every theoretical edge case before progression.

Research/handoff should stop when the applicable Gate has sufficient evidence that:

- material understanding is established;
- material Unknowns are resolved or explicitly controlled;
- the receiving role has enough correct understanding to execute its authorized responsibility;
- no blocking Veto or Gate condition remains.

`Material Unknown Exhaustion != Artificial Certainty.`

---

## 8. No Scope Expansion

This standard governs quality of learning, transfer and preservation. It does not silently add product capability.

If understanding exposes a missing capability:

```text
Gap -> Evidence -> Baseline Check -> IN-SCOPE controlled work OR Change Request -> Boss Decision
```

`Better Understanding != Automatic Scope Expansion.`

---

## 9. Clean-Room / Independent Design Boundary

For SMEsPlus clean-room work:

- source code/vendor implementation details remain learning/evidence inputs only;
- Team A transfers business facts, semantics, observations, provenance and Unknowns;
- Team B independently designs SMEsPlus canonical behavior;
- no vendor source architecture, ORM/schema/workflow implementation is transferred as a mandatory target design;
- no code copying/reuse is authorized by this standard.

`Migrate / learn Business Facts + Business Semantics, not legacy application architecture.`

---

## 10. Required Handoff Record — Minimum Material Fields

Where a formal controlled handoff is required, record at minimum:

```text
Handoff ID:
From Owner / Team:
To Owner / Team:
Scope:
Verified Understanding:
Evidence References:
Known Unknowns / Conflicts:
Boundaries / Ownership:
What Receiver May Trust:
What Receiver Must NOT Assume:
Teach-Back Result (if material):
Challenge / Review Result:
Carry-Forward Controls:
Gate Impact:
Timestamp:
Verifier / Reviewer:
```

If a field is not applicable, state `N/A` rather than silently omit a material control.

---

## 11. Core Statements

`Understand deeply.`  
`Transfer accurately.`  
`Document & Preserve verifiably.`  
`เข้าใจให้จริง -> ส่งต่อให้ตรง -> รักษาไว้ด้วยหลักฐาน.`  
`Documentation != Proof of Understanding.`  
`File Sent != Knowledge Transferred.`  
`Transfer knowledge, not predetermined conclusions.`  
`Material Unknowns must be resolved or explicitly controlled.`  
`No Evidence = No Progress.`  
`No Evidence Preservation = No Lifecycle Promotion.`  
`Never Skip Gate.`  
`Boss = Sole Final Approver.`

---

## 12. Authority Boundary

This standard does not by itself authorize:

- Functional Scope addition;
- Team progression outside existing Gate rules;
- Development;
- Release;
- Deployment;
- Production;
- statutory/legal claims;
- source-code reuse.

Existing governance, Evidence Gate, 9 Veto Council, 9 Special Team, Team independence and Boss authority remain fully effective.
