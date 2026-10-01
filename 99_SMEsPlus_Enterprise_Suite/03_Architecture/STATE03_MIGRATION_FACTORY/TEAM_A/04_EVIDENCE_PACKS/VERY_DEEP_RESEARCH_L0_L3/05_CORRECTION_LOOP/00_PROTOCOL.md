# STATE03 VDR — Automatic Correction & Evidence Completion Loop (standing instruction)

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Routine correction cycles need no Boss approval. Notification/traceability only; not a merge request, Gate PASS or verification result.

## Roles in this session (disclosed)
- **DeepSeek (primary research worker)** — executed here through Claude Code; owns research and correction packets.
- **Claude Code (harness)** — in this session also performs *spot-check review* of worker output against source and the restored dump; those reviews are **not independent verification** and are labelled as such.
- **Claude verifier session (independent)** — separate session; its comments on PR #74 are the authoritative verification feed. At the time of writing it had posted no correction request.

## Classification of every reviewed claim
`ACCEPTED` · `NEEDS_MORE_EVIDENCE` · `CORRECTION_REQUIRED` · `CONTRADICTION_UNRESOLVED` · `RUNTIME/AWT_REQUIRED`. Priority: **C1 / Material / Normal**. C1, Clean-Room leakage, licence-boundary breach and material contradiction are processed first.

## Procedure
1. A reviewer posts a structured correction request to PR #74: boundary / module / Function-ID, Claim-ID(s), original commit and packet, missing or conflicting evidence, exact source/dump research required, acceptance criteria, priority.
2. DeepSeek checks PR #74 **after every Atomic Boundary, before changing module, and before any Module Closure Package**; processes requests DELTA-FIRST (affected scope only).
3. Originals are never edited: the correction packet `<BOUNDARY>-R<n>` (restricted claims + neutral statements, gated by the same pointer/anchor/leak script) is added; superseded claims are listed in `SUPERSESSION_INDEX.tsv` as `SUPERSEDED` / `SUPERSEDED-IN-PART` with a pointer to the packet.
4. Push, notify PR #74, continue other non-blocked research. Runtime behaviour is never inferred from source/dump: such items go to `06_AWT_BACKLOG/`.
5. The reviewer re-verifies every correction packet; loop repeats until ACCEPTED, RUNTIME/AWT_REQUIRED, or a true hard blocker.

## Lineage note (self-disclosure)
Two earlier corrections to B01 (commits `4a4f39cf`, `c348a8c8`) were applied **in place** before this standing instruction. Original wording is preserved in git history (`1c7a8e8e`) and re-stated with supersession in packet `B01-R1`. From now on originals are not edited.

## Files
`REVIEW_REGISTER.tsv` (claims reviewed so far; claim IDs resolved by pointer proximity — reviewers should confirm) · `CORRECTION_REQUESTS.md` · `SUPERSESSION_INDEX.tsv` · `packets/<ID>_restricted.md` + `packets/<ID>_neutral.md`.
