# 02 — AUTHORITY CONFLICT DECISION REGISTER

Repository: TH-PATTARAKRIT/AI-Collaboration-Hub · HEAD `8570187` ·
Prepared By: Claude AI (preparer only) · 2026-07-14 · Final Approver: Boss.

This register maps each authority conflict to a **Boss decision**. It does not resolve,
close, or authorize correction of any conflict. Live-status re-checked against the current
working tree (not merely transcribed from the older register).

## Canonical authority wording (recommended)

> **Boss ดำเนินการตัดสินใจและอนุมัติขั้นสุดท้ายแต่เพียงผู้เดียว**

PMO, Reviewer, Verifier, and AI are **supporting control roles only** — never a joint or
final approver.

## P0 conflicts — LIVE in source of truth (re-verified 2026-07-14)

| ID | Source (path:line) | Current text | Correction | Live? | Boss Decision |
|---|---|---|---|---|---|
| ACF-001 | `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md:160` | Build Gate = `PMO + Boss` | RC-001 → Boss-only | **YES (live)** | BAQ-01 |
| ACF-002 | `00_Project_Governance/AI_ROLE_AND_RESPONSIBILITY.md:159` | QA/UAT Gate = `QA AI + PMO` | RC-002 → QA AI/PMO support only | **YES (live)** | BAQ-01 |
| ACF-004 | `00_Project_Governance/ARCHITECTURE_GOVERNANCE_STANDARD.md:31` | `Boss / PMO authority is required for gate movement` | RC-004 → Boss approval evidence | **YES (live)** | BAQ-01 |
| ACF-005 | `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md:23` | FDS Final Approver = `Boss / PMO` | RC-005 → Boss-only | **YES (live)** | BAQ-01 |
| ACF-006 | `00_Project_Governance/APPROVAL_AUTHORITY_MATRIX.md:24` | SDS/API/DB/UX Final Approver = `Boss / PMO` | RC-006 → Boss-only | **YES (live)** | BAQ-01 |
| ACF-008 | `00_Project_Governance/DOCUMENT_REGISTRY.yaml` vs 2026-07-05 standards | registry/standards divergence | RC-008 → controlled reconcile | Register-tracked | BAQ-01 |

## P1 conflicts — supporting

| ID | Source (path:line) | Current text | Correction | Boss Decision |
|---|---|---|---|---|
| ACF-003 | `AI_ROLE_AND_RESPONSIBILITY.md:95` | `Production ... approved by Boss and PMO Gate` | RC-003 → Boss-only | BAQ-01 |
| ACF-007 | `APPROVAL_AUTHORITY_MATRIX.md:18` | Constitution draft owner `Liza / PMO AI` | RC-007 → ES Accountable, AI Responsible | BAQ-01 |
| ACF-009 | `FOLDER_REGISTRY.yaml:26,31,36,41,61` | folder owners name PMO alone/jointly | RC-009 → one Accountable owner each | BAQ-01 |
| ACF-010 | cross-document PMO terminology | ambiguous PMO wording | RC-010 → AI PMO = Support Only | BAQ-01 |

## Independent evidence check performed for this register

`grep -niE "Boss ?/ ?PMO|PMO ?\+ ?Boss|Boss and PMO|QA AI \+ PMO"` over
`99_SMEsPlus_Enterprise_Suite/00_Project_Governance/` on HEAD `8570187` returns the exact
lines above — confirming the P0 conflicts are **not yet corrected in source**. The Step 03
package proposed and L99-CONFIRMED RC-001..010, but the source documents were deliberately
not modified (see `STATE02_RACI_SOURCE_DOCUMENT_UPDATE_PLAN_v0.1.md`, "no source document
touched"). Application awaits Boss authorization → **BAQ-01**.

## Authority-conflict control statement

```text
P0 authority conflicts remain OPEN in the source of truth.
Corrections are CONFIRMED as proposals only; none is applied or Boss-authorized.
A live P0 authority conflict PREVENTS unconditional State 02 closure.
Boss is the Sole Final Approver.
```
