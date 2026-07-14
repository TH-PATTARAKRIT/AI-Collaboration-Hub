# STATE02_CANONICAL_ROLE_DEFINITIONS_GLOSSARY_v1.0.md

Document ID: SMEPLUS-STATE02-GLOSSARY-001
State: 02 — Governance
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub
Target Branch: SMEsPlus | Execution Branch: `claude/state-02-governance-26bzvw`
Prepared By: Claude AI (Responsible / analysis only)
Prepared At: 2026-07-14 (UTC)
Authority: Boss decision **S02-FINAL-003 (APPROVED, 2026-07-14)**
Status: CANONICAL — CONFIRMED BY BOSS (S02-FINAL-003)

## 1. Purpose

Resolve the root-cause ambiguity (ACF-010) in which the term **"PMO"** carried at least three
different meanings across governance documents, producing the joint-authority conflicts ACF-001,
ACF-002, ACF-007, and ACF-009. This glossary defines one canonical meaning per term.

## 2. Canonical Role Definitions

| Term | Canonical Meaning | May be Accountable Owner? | May be Final Approver? |
|---|---|---|---|
| **Boss** | The single human decision authority. Boss ดำเนินการตัดสินใจและอนุมัติขั้นสุดท้ายแต่เพียงผู้เดียว. | Yes (for gate/state decisions) | **Yes — sole Final Approver** |
| **PMO (Human coordination office)** | The human Project Management Office function: prepare, coordinate, control, monitor, report. Executive Secretary / Liza operates within this function. | Yes (coordination accountability) | **No** |
| **AI PMO** | An AI operating in a **Support-Only** capacity: tracking, report preparation, evidence organization. | **No — never Accountable Owner** | **No** |
| **Executive Secretary / Liza** | Named human accountable coordination owner; prepares closure packages; cannot approve own work. | Yes | No |
| **Owner** | The single Accountable party for an assigned work item. | Yes (exactly one per activity) | No (unless the Owner is Boss for a decision) |
| **Reviewer** | Independent governance-consistency reviewer. | No (for the item under review) | No |
| **Verifier** | Independent evidence/traceability verifier; must differ from the preparer. | No | No |
| **AI (Claude AI, etc.)** | Analyze, draft, consolidate, execute within authorized boundaries. | No (not Accountable Owner, Reviewer, Verifier, or Approver) | **No** |

## 3. Disambiguation Rules

1. A bare token **"PMO"** in any governance document defaults to **PMO (Human coordination office)**
   unless the text explicitly says **AI PMO**.
2. **AI PMO** is **Support Only**. It is never an Accountable Owner, never a gate authority, never a
   Final Approver.
3. No activity may list a **joint** Final Approver (e.g. "Boss / PMO", "PMO + Boss"). Final approval
   is **Boss alone**. Coordination by PMO is recorded separately from approval.
4. Where a document previously named "PMO AI" or "PMO / Boss" as a draft or approval authority, the
   authority resolves to the human role (Boss for approval; Executive Secretary / human PMO for
   coordination), and AI PMO is recorded as Support Only.

## 4. Conflicts Resolved by This Glossary

| Conflict | Resolution |
|---|---|
| ACF-007 | `Liza / PMO AI` draft owner → `Liza (Executive Secretary)`; AI PMO = Support Only (applied in APPROVAL_AUTHORITY_MATRIX.md) |
| ACF-009 | Ambiguous folder owners → `PMO (Human coordination office)` (applied in FOLDER_REGISTRY.yaml) |
| ACF-010 | Root-cause ambiguity removed by this canonical glossary |
| ACF-001, ACF-002 (support) | "PMO" in Build/QA gate rows now unambiguously the human coordination office; final approval is Boss (applied in AI_ROLE_AND_RESPONSIBILITY.md) |

## 5. Control Statement

Boss is the Sole Final Approver. This glossary is CANONICAL by Boss decision S02-FINAL-003.
Independent review/verification recording of the applied corrections remains tracked under
S02-FINAL-005. AI PMO remains Support Only; no AI holds Final Approver authority.
