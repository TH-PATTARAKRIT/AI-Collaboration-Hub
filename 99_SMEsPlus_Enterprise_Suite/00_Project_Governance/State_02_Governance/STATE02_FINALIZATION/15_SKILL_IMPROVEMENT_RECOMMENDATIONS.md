# 15 — SKILL IMPROVEMENT RECOMMENDATIONS

Proposed Skill: SMEsPlus State 02 Governance and Evidence Gate Controller ·
Repository: TH-PATTARAKRIT/AI-Collaboration-Hub · HEAD `8570187` · 2026-07-14.

The simulation passed all Critical and High criteria. The recommendations below harden the
Skill and remove ambiguity observed against real repository evidence. They do not change the
verdict.

## Priority recommendations

**REC-1 — Live source re-scan on every run (authority-integrity gate).**
The Skill must always grep the *current* source of truth for joint-approval phrases
(`Boss / PMO`, `PMO + Boss`, `QA AI + PMO`, `Boss and PMO Gate`, `Liza / PMO AI`) rather than
trusting a register's "COMPLETE" flag. This run found 6 P0 lines still live despite CONFIRMED
corrections — only a live scan catches "confirmed-but-not-applied".

**REC-2 — Status reconciliation detector (single source of truth per finding).**
Detect and flag the two-layer drift where PENDING shells are never updated after review/merge
(observed: registers/crosswalk/checklist say PENDING while L99 records + PR #13 show completed).
Emit a reconciliation task and name the canonical status document.

**REC-3 — Enforce the 7 evidence fields as a hard schema.**
Any document or claim missing Work item / Owner / Evidence location / Timestamp /
Reviewer-Verifier / Verification status / Gate impact is auto-classified NOT VERIFIED.
Would have flagged the header-only `AUTHORITY_SCAN_EVIDENCE_REGISTER_v1.1` stub automatically.

## Secondary recommendations

**REC-4 — Verified-vs-created counter split.** Never let a "files created = N/N" or checklist
quantity render as progress %. Report `created`, `reviewed`, `verified` as three separate
counters so "24/24 created" can never be misread as "24/24 verified".

**REC-5 — Canonical-existence precheck before authoring.** Before writing any governance
document, the Skill checks the canonical index; if a valid canonical exists, it writes a
pointer/validation file instead of a duplicate, and records the justification.

**REC-6 — Boss-decision schema lint.** Reject any Boss item that lacks Decision ID, exact
matter, recommended decision, evidence, both effect branches, and copy-ready approval wording.

**REC-7 — Canonical wording provisioning.** When the recommended authority string
(`Boss ดำเนินการตัดสินใจและอนุมัติขั้นสุดท้ายแต่เพียงผู้เดียว`) is absent from the tree, raise it
as an explicit Boss decision (done here as BAQ-04) rather than silently assuming it exists.

**REC-8 — File-count reconciliation note.** Auto-emit one authoritative count reconciliation
when manifest/PR/canonical counts diverge (observed 24 vs 25 vs 13).

## Top-3 for the required summary

1. Live source re-scan of authority wording on every run (REC-1).
2. Two-layer status reconciliation detector (REC-2).
3. Hard 7-field evidence schema with verified-vs-created counter split (REC-3 + REC-4).

Boss is the Sole Final Approver. No Evidence = No Progress.
