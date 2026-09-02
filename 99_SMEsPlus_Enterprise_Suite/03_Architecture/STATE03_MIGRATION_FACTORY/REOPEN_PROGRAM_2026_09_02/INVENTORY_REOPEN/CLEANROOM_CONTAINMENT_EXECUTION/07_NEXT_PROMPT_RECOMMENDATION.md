# 07 — Next Prompt Recommendation

## 1. The single highest-priority next step

A written Boss ruling on the CORR-007B git-history containment question (Boss Decision Support `SMEPLUS-26-09-02-INV-CLEANROOM-HISTORY-CONTAINMENT-001`, options A/B/C/D). This session applied option D (warning label) as the non-destructive interim step every piece of evidence in this program recommends, but a warning label is a documentation control, not a technical one (`02_CORR007B_C05_CLEAN_ROOM_REAUDIT.md` §2.3) — it does not close the underlying question.

## 2. Recommended next prompt shape, if Boss wants to keep moving before ruling on history containment

A short, Boss-authored (or Boss-dictated) prompt whose only content is the actual A/B/C/D ruling, addressed to whichever session/process is authorized to act on it. This is not a task for another AI-executed audit session — the master prompt for *this* session already correctly scoped the decision itself as Boss-only, and nothing in this session's work changes that.

## 3. Recommended next AI-executed session, if Boss wants further mechanical work in the meantime

A propagation-scope session, once Boss has ruled on which branch is authoritative, that:

1. Applies the same two fixes (or supersedes them, if Boss's ruling changes the label's wording) directly on the two original branches (`audit/inventory-core-corr007b-3high-closure-010`, `audit/inventory-menu-deep-challenge-2026-09-02-001`) as new commits — not this session's parallel copies — so there is exactly one authoritative version of each file going forward.
2. Formally ratifies (by Boss instruction, not by AI self-declaration) the Clean-room Re-Audit's tie-breaking read of files `08`/`09`, closing `10_REMEDIATION_ACTION_REGISTER.md` item 3.
3. Does not attempt `U-07` or any Team B/C/Development authorization — both remain outside any AI session's authority per every prior session in this program.

## 4. What not to do next

- Do not run a history rewrite (`git filter-repo` + force-push) without a separate, explicit, written Boss command and backup plan — Boss Decision Support §3 option C and Remediation Action Register item 1 are both explicit that this session and any session like it must not execute this unilaterally.
- Do not treat this session's branch as merge-ready — it is a parallel copy pending a propagation decision, not a superseding authoritative version.
- Do not declare `C-05 CLOSED` from this session's work alone; that requires the Boss ratification named in §2 above, which this session did not seek or receive.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
