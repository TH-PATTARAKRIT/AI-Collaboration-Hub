# STATE03 Deep Study — Controlling Prompt Provenance Index

Session: `SMEPLUS-26-09-28-STATE03-ARCH-KNOWLEDGE-REBASE-001`
Document ID: `STATE03-PROMPT-PROVENANCE-INDEX`
Version: 1.0
Date: 2026-09-29
Authority: Boss's "STATE03 Corrective Checkpoint Prompt," §B1 (prompt provenance verification)
Boss: Sole Final Approver

This index exists because the corrective checkpoint prompt explicitly requires: *"Verify the exact prompt file used in the repository and report its path, commit, SHA-256, and line count... Do not claim an attached prompt is byte-identical without comparing its actual hash."* Every hash below was computed directly with `sha256sum` against the file as delivered to this session (chat upload), then re-verified identical after being copied into this repository path — not asserted from visual comparison.

## 1. Controlling prompt files, in chronological order

| Order | File (this folder) | Original delivery | SHA-256 | Lines | Role |
|---|---|---|---|---|---|
| 1 | `00_MASTER_PROMPT_v1_SESSION_START_2026-09-28.md` | Chat upload, 2026-09-28 (session start) | `3aefd98b02d3d5dbf01150ea6a3da827159c00f8a8bd56e57b6fc2510558663e` | 185 | The Master Prompt actually in force when Lane C (Gx1–Gx10, 46 functions) and `M1` (Manufacturing/BOM/Routing, 5 functions) were researched |
| 2 | `00_MASTER_PROMPT_v2_WITH_7A_13A_2026-09-29.md` | Chat upload, 2026-09-29 (re-sent twice, confirmed byte-identical to each other by hash — see §3) | `6fc9cb5928dc721e9b4956648b19c07c035ef269d14038bbd1a045b391b08546` | 216 | A **materially different** version of the Master Prompt — see §2 for the exact diff. This is the version now "current controlling" per Boss's later rulings. |
| 3 | `01_NEXT_PROMPT_AUTONOMOUS_EXPANSION_2026-09-29.md` | Chat upload, 2026-09-29 (re-sent twice, confirmed byte-identical by hash) | `207b796ec41809b346de04d7ab1e6d63424743c3dc7b7a63f70edc2520bc913e` | 92 | "STATE03 Next Prompt — Autonomous Research Continuation and Module Expansion" — governed the `M1` module selection and the first-checkpoint reconciliation |
| 4 | `02_CORRECTIVE_CHECKPOINT_PROMPT_2026-09-29.md` | Chat upload, 2026-09-29 | `7ba19d8b27a5a2cbdc363308279bad9119f6884b3186150bcc7115d7fce3d78b` | 105 | This corrective checkpoint itself — supplements and corrects the Next Prompt; does not reset research |

## 2. Material diff: v1 (session-start) vs. v2 (current controlling)

**Self-correction**: an earlier turn in this session was asked whether a re-uploaded Master Prompt file carried "new instructions," and answered no, based on comparing it only against the *immediately prior* chat upload (which was in fact identical to it). That comparison never reached back to the actual session-start prompt (v1 above), so it missed a real, material difference. This index corrects that.

`diff` between v1 and v2 shows exactly two additions, nothing removed and nothing else changed:

1. **New §7A — "Mandatory Source Code Study"** (17 lines): requires studying actual Odoo source (module manifest, decision-point logic, effective override/extension chain, compute/onchange/constraint behavior, scheduled actions, security conditions) for every C1/C2 Function, and every C3/C4 Function where source is needed to resolve a material doubt; producing a "Restricted Source Study Index"; and explicitly permitting `Black-box / Unavailable` with the V-exception policy when source is not accessible.
2. **New §13A — "Next-Phase Gate"** (15 lines): six explicit preconditions before STATE03 may be proposed for Boss review (every function has a recorded V level; C1 functions meet V5 or a documented V4 exception; every Unknown is classified; source studies/config profiles/AWT/control checks are complete or exceptioned; every candidate handoff passed Abstract & Sanitize; a consolidated Closure/Handoff Recommendation exists) — and states STATE04 may not start without Boss approval.

**Effect on work already done**: no rework required. Every pilot and module researched under v1 (Lane C + `M1`) already, independently of §7A existing, recorded `Black-box / Unavailable` for source/runtime access and applied the same V-exception policy §7A itself describes as the fallback — consistent with Boss's own 2026-09-28 chat ruling that AWT/source access is `Black-box/Unavailable` for this container. §7A formalizes a practice already followed; it does not retroactively invalidate anything, and no function's Actual V has been overstated relative to it. §13A's Next-Phase Gate has not been reached or claimed by any artifact in this repository — `STATE03_DEEP_STUDY_REGISTER.md` explicitly disclaims "STATE03 Complete" throughout.

## 3. Re-upload identity checks (also required by §B1)

- v2 (Master Prompt) was delivered twice in this session; both copies hash to `6fc9cb59...` — genuinely byte-identical, not merely visually similar.
- The Next Prompt was delivered twice; both copies hash to `207b796e...` — genuinely byte-identical.

## 4. What this index does not do

Committing these files does not itself constitute a Gate decision, a canonical designation, or a Boss ruling. It preserves the exact prompt text this Deep Study has operated under, per Boss's own explicit instruction to verify provenance rather than assert it.
