# CANONICAL_ROLE_GLOSSARY.md

Status: Additive — controlled addition under RC-010 (STATE02_SOURCE_GOVERNANCE_CONFLICT_REGISTER_v1.0.md)
Source of Content: STATE02_CANONICAL_RACI_v1.0.md §2 (Controlled Roles)
Authorization: Boss Decision 2 — CONTROLLED SOURCE CORRECTION AUTHORIZED (RC-001..RC-010)
Prepared By: Claude Code (Responsible role only)
Approval Status: Pending Independent Review and Boss Closure Decision — NOT Canonical until approved

## Purpose

This glossary resolves the ambiguous standalone use of `PMO` across State 02 governance
documents (RC-010) by defining every controlled role by full name and authority
boundary. It is additive documentation; it does not delete or reclassify any
pre-existing document. Where a governance document below RC-010 in this correction
package used `PMO` ambiguously, the corrections in RC-001 through RC-009 replace it with
one of the explicit terms defined here.

## Canonical Role Definitions

| Role Code | Full Name | Authority Boundary |
|---|---|---|
| BOSS | Boss | Sole Final Approver. Final authority for Canonical publication, Gate approval, Merge, Release, Deployment, and Production approval. Not the operational executor. |
| ES | Executive Secretary / Liza | Accountable coordination owner. Evidence and execution coordination. Cannot independently approve own work. |
| AO | Acting Owner | Temporary Accountable role for a specific assigned deliverable when the permanent Owner is missing, inactive, unavailable, obstructing execution, or has not provided required evidence. May coordinate execution, assign Responsible roles, request evidence, prepare review packages, and escalate control failures. May not approve Final Gate, State Closure, Build, Merge, Release, Deployment, Production, or override Boss authority. |
| L99 | ChatGPT L99 | Independent Governance Reviewer. Cannot be Final Approver. Cannot verify its own repository write without separate system evidence. |
| CAI | Claude AI | Responsible execution and document preparation. Cannot be Accountable Owner, independent Reviewer, Evidence Verifier, or Final Approver. |
| AI PMO | AI PMO | **Support Only.** Tracking, report preparation, evidence organization. Cannot approve, verify, pass Gate, merge, release, or deploy. Any standalone `PMO` reference in a governance document that grants approval, veto, or gate authority is a conflict and must be corrected to this definition. |
| RO | Repository Owner / Authorized GitHub Execution Agent | Responsible for repository write execution. Must provide real Commit SHA. Cannot declare Gate PASS. |
| GR | Governance Reviewer | Independent review of governance meaning, classification, severity, gate impact. |
| EV | Independent Evidence Verifier | Verifies path, commit, hash, owner, approval, and evidence. Must be separate from the preparer. |
| DC | Document Control | Registry maintenance, version control, classification execution, controlled publication execution after approval. |
| FO | Functional Owner | Owns functional content correctness of domain documents. |
| TO | Technical Owner | Owns technical content correctness and technical execution (build/release/deploy execution after approval). |
| GTR | Gate Reviewer | Prepares Gate recommendation from review and verification evidence. Cannot approve the Gate. |
| FA | Final Approver | Boss only. No AI may hold this role. |

## Control Statement

This glossary is additive and does not itself grant, remove, or reassign authority. Its
sole function is definitional: eliminating ambiguity in the term `PMO` and aligning all
State 02 governance documents to the single Accountable-owner and Support-Only rules
already established in `STATE02_CANONICAL_RACI_v1.0.md` and `DOCUMENT_REGISTRY.yaml`.
Boss remains Sole Final Approver. This document is not Canonical until Independent Review,
Independent Verification, and Boss approval are recorded.
