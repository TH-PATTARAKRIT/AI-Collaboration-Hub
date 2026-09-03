# 01 — Session Control

Session: `SMEPLUS-26-09-03-COGS-TARGETED-RESOLUTION-001` | Control Level: `/L999.999`
Parent Sessions:
- `SMEPLUS-26-09-03-COGS-JOINT-CLOSURE-001` (nominal parent; see file `02` for a provenance discrepancy this session found and did not paper over)
- `SMEPLUS-26-09-03-COGS-FACT-VERIFICATION-001` (immediate predecessor, commit `178cd06f7e9923bb3f876e17664f4833e534833c` on `origin/research/cogs-fact-verification-2026-09-03-001`)

Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub` | Canonical Branch: `SMEsPlus` (untouched, not merged into)
Execution Branch: `research/cogs-targeted-resolution-2026-09-03-001` | Base: `origin/SMEsPlus`
Boss: Sole Final Approver
Execution Mode: `EVIDENCE-FIRST / TARGETED RESOLUTION / CLEAN-ROOM / NO-GUESS / NO-FORCE-CLOSE`

## 1. Mandate

Take the Fact Verification session's re-verified baseline (59 material unknowns, 0 closed, 12 Joint Decisions open, `JT-04`/`JT-05` genuinely undecidable from documentation alone — commit `178cd06`) and run a targeted resolution pass in priority order: `JT-04` → `JT-05` → `JT-01` → COGS recognition-timing model analysis → `CGS-U03` → `CGS-U34`/`CGS-U36` → remaining P0 → P1 → material P2. Resolve what can honestly be resolved with the evidence actually available this session; disposition everything else as HOLD naming the specific missing evidence and its owner.

## 2. Tool/Evidence Availability This Session (Read Before Any Deliverable)

Confirmed unavailable this session, verified by direct attempt, not assumed:
- **Jira (Atlassian MCP):** unauthenticated/unavailable. No ticket could be read, created, or updated. Any Jira ticket numbers referenced below (`ERPPLUS-142`, `ERPPLUS-139`) are carried forward from project memory / prior session file paths only — not independently re-verified against a live Jira instance this session.
- **GitHub MCP connector:** failing (`400 Authorization header is badly formatted`). Plain `git` CLI was used instead for all clone/branch/commit/push operations — confirmed working.
- **Live reference-ERP instance:** none available. Every reference-ERP claim in this session is inherited, with citation, from the Fact Verification and COGS Deep Research sessions' own documentation-tier research — no new reference-product page was fetched this session.
- **Thai statutory legal database:** none available. No new Thai primary source was opened this session. `TH-NEW-01` and `TH-NEW-02` (identified in the Fact Verification session, file `12` of that package) remain unresearched here for the same reason.
- **Business SME / Boss:** no live stakeholder available this session. Every item routed to a Business SME question or a Boss ruling is dispositioned HOLD, never self-decided.

## 3. What This Session Does NOT Do

- Does not fabricate Jira ticket numbers, statuses, or comments.
- Does not fabricate live reference-ERP behavior beyond what prior sessions already documented with citation.
- Does not fabricate Thai statutory citations beyond what `12_THAI_ACCOUNTING_TARGETED_EVIDENCE.md`'s source material (the Fact Verification session's file `12`, itself pointing to DR file `24`) already contains.
- Does not close `JT-04` or `JT-05` by ruling — both are dispositioned per the DECIDABLE / DECIDABLE WITH CONTROL / NOT DECIDABLE framework, and neither qualifies as plain DECIDABLE.
- Does not finalize Inventory v2.0.
- Does not execute any Boss Account Ruling — every such item is routed HOLD to Boss.
- Does not merge into `SMEsPlus`.
- Does not start development or coding.
- Does not push to any branch other than `research/cogs-targeted-resolution-2026-09-03-001`.

## 4. Session Structure

24 numbered deliverable files plus `SHA256SUMS.txt`, listed in `24_SESSION_CLOSURE.md` §1. Priority order stated above governs the depth of treatment: `JT-04`, `JT-05`, `JT-01`, and the COGS recognition options analysis receive the most detailed treatment; remaining P1/P2 unknowns are addressed at register level (file `03`) and routed (file `07`), not individually deep-dived, consistent with the evidence ceiling in §2.

No Evidence = No Progress. Never Skip Gate. An unknown is not automatically a design problem. Boss = Sole Final Approver.
