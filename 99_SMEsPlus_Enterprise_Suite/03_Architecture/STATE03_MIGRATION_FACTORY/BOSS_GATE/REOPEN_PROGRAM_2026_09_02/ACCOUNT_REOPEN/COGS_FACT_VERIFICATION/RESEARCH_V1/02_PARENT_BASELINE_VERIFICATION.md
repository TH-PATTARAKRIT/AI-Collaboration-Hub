# 02 — Parent Baseline Verification

Verified against canonical evidence, not against memory or prior narrative summaries.

## 1. Source Documents Directly Opened This Session

| Document | Location | Role |
|---|---|---|
| `30_COGS_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md` | `audit/cogs-deep-research-2026-09-02-001`, `.../COGS_DEEP_RESEARCH/RESEARCH_V1/` | Primary unknown register |
| `33_COGS_DEEP_RESEARCH_FINAL_REPORT.md` | same path | Headline findings, terminal status, coverage statement |
| `01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-COGS-DR-001.md` | same path | Defines `JT-01`–`JT-12` scope tags as used by the register |
| `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` | `design/inventory-final-solution-v1-2026-09-02-001` | **The actual source of `JT-01`–`JT-12` definitions** — one line each |

## 2. Claim-by-Claim Reverification

| Parent session claim | Verified? | Actual finding |
|---|---|---|
| COGS Deep Research was completed | **TRUE** | Session `SMEPLUS-26-09-02-COGS-DR-001` published 37 files (`00`–`36`) on branch `audit/cogs-deep-research-2026-09-02-001`; terminal status recorded in file `33` |
| Terminal state remained HOLD | **TRUE** | File `33` §6: `HOLD / EVIDENCE REQUIRED — COGS MATERIAL UNKNOWN NOT EXHAUSTED`, with three stated reasons |
| ~59 material unknowns recorded | **TRUE, exact** | File `30` §10 Register Roll-Up states **59** as the explicit total; this session independently counted the line items in §2–§9 of that register (`CGS-U01`–`CGS-U50` = 50 numbered items, plus the Thai statutory block in §9) and confirms 59 is the register's own authored total. See §4 below for one small internal bookkeeping note on the Thai sub-count. |
| 0/59 closed | **TRUE** | File `30` §10: "Closed by this session — **0**"; every row in §2–§9 carries `HOLD`, `MATERIAL`, `BLOCKING`, `CONFLICTING`, or `WATCH` — no row is marked closed. Independently confirmed by scanning every row: zero contain the word "CLOSED" or "VERIFIED" as a final disposition. |
| 0/12 Joint Decisions closed | **TRUE** | `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` lists `JT-01`–`JT-12`; file `33` §2 states explicitly "No open Joint decision (`JT-01`–`JT-12`) closed... All twelve remain open" |
| JT-04 and JT-05 not decidable from documentation alone | **TRUE, in the DR session's own words** | File `33` §6 point 3: "`JT-05`/`C-03` (return cost basis) and `JT-04` (COGS recognition timing)... remain genuinely undecidable from reference-ERP evidence alone, by this research's own finding, and require a Joint session with Thai-evidence input this package could only partially supply." |
| Account gates remained HOLD | **Not reverified in this session** | Out of scope for a COGS-focused fact session; carried from parent without independent re-check here — flagged so it is not silently treated as re-confirmed |
| Boss Account Ruling intentionally paused | **Consistent with governance record** | No Boss ruling document found dated after the parent session's stated pause; not independently reproven beyond absence-of-evidence |

## 3. What "COGS Deep Research Completed" Actually Means

It means 37 documentation-only research files were produced by a single coordinating session (with delegated research passes reviewed before publication — file `33` header). It does **not** mean any fact was verified against a live system, a database, or a posted transaction, because none exists for SMEsPlus (see `01_SESSION_CONTROL.md` §1). The "evidence" in the DR package is entirely Level 6/7 (reference-product documentation, existing project research) plus Level 9 (Thai statutory primary sources) in the hierarchy given to this session. This is a legitimate and often the correct evidence ceiling for a pre-build architecture research phase — it is not runtime proof, and this session does not pretend otherwise.

## 4. One Non-Material Bookkeeping Note (Not a Material Contradiction)

File `30` §10 states the Thai statutory track subtotal as **9**, but the literal ID list in §9 enumerates `TH-HOLD-COGS-01` through `04`, one residual note (`TH-HOLD-05-residual`), and one bundled carried-forward row naming five prior IDs (`TH-HOLD-01, 04, 06, 08, 09`) — a literal ID count of 10, not 9, depending on whether the residual note is counted as its own item or as a sub-note on an already-counted carried ID. This is a labeling ambiguity in the original register, not a new material unknown, and does not change the authored total of 59 (which is stated once, directly, in the roll-up table, independent of how the Thai subtotal is internally itemized). Recorded here for completeness per the "no evidence is silently smoothed over" rule; no action required unless a future session needs the exact Thai sub-count.

## 5. Verdict on Parent Baseline

**CONFIRMED AS STATED.** The parent Joint Closure session's factual claims about the COGS material unknown population, its closure state, and the JT-04/JT-05 undecidability finding are accurate and traceable to primary session documents, not to narrative summary. This session proceeds on that confirmed baseline.
