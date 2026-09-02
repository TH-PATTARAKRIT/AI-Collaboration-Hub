# 09 — Next Prompt Recommendation

Session: `SMEPLUS-26-09-02-INV-FINAL-SOLUTION-V2-001` | Jira: `ERPPLUS-139`
Status: `RECOMMENDATION ONLY — BOSS CHOOSES THE NEXT SESSION`

---

## 1. Candidate Next Sessions

| # | Candidate | What it would do | Prerequisite | Value |
|---|---|---|---|---|
| **G** | **Execute the COGS Deep Research session already authorized** (`SMEPLUS-26-09-02-COGS-DR-001`, Jira `ERPPLUS-142`) | Run the 37-deliverable menu-by-menu, field-by-field, Periodic-vs-Perpetual research the prompt (already issued, commit `d57a52c`) specifies in full. | **None from Boss.** Readiness (`4f8b7d0`) and the prompt (`d57a52c`) already exist. Only scheduling and an executor are needed. | **Highest.** Directly unblocks 9 of 12 `JT-*` decisions (file 07 §3), the largest concentration of open items in the entire Inventory register. |
| B | Thai user validation session *(carried from v1.0 candidate B)* | Convert `UNVALIDATED - THAI USER REVIEW REQUIRED` rows in v1.0 file 11 into evidenced per-label, per-flow acceptance records. | Boss commissions; needs real users. | High. Independent of G. |
| D | Migration provenance design session *(carried from v1.0 candidate D)* | Design the provenance reference as a first-class Migration Factory component. | None. | High and independent of G. |
| A | Joint Accounting ↔ Inventory session *(carried from v1.0 candidate A)* | Close the twelve `JT-*` decisions. | **Now specifically requires G to have run first** for 9 of the 12 items (file 04 §3, Lane C) — this is a stronger prerequisite than v1.0 stated, because v1.0 did not yet know the COGS research itself would stall at readiness. | Highest value once G exists; premature before it. |
| C | Independent re-audit *(carried from v1.0 candidate C)* | Verify clean-room compliance and internal consistency of v1.0 **and now v2.0**. | Boss decides re-audit is needed. | Medium. |
| E | Inventory resilience and exception design *(carried from v1.0 candidate E)* | Close `GAP-FS-23`. | None. | Medium. |
| F | Boss history-containment ruling | Not a session — a Boss decision on `C-05`. | Boss only. | Blocking for the evidence chain regardless of what else runs. |

---

## 2. Recommendation

**Commission G immediately. Run B and D in parallel with G, exactly as v1.0 recommended for its own next step. Schedule A only after G reaches a terminal status.**

Reasoning: G is not a new request — it is the completion of something Boss already authorized twice (the readiness verdict and the prompt itself) and that simply has not been executed. Every session in this programme since v1.0 closed has been blocked, in part, on this same missing piece; running it removes the single largest concentration of open items in one pass (file 07 §3, §6). B and D remain exactly as valuable and exactly as independent as v1.0 assessed them to be — nothing about the COGS Gap changes that. A should wait: convening it before G exists would mean the Joint session either stalling mid-session or ruling on 9 of 12 items without the evidence the Boss Ruling requires before those rulings, which is precisely what this session's `HOLD` exists to prevent. C and E are unchanged from v1.0's assessment. F is not a session and should be decided regardless of what else runs.

---

## 3. Recommended Prompt for the Controlling Next Session (Option G)

> **This is not a new prompt to draft.** The prompt already exists, unmodified, at:
>
> `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/COGS_DEEP_RESEARCH/01_NEW_SESSION_PROMPT_SMEPLUS-26-09-02-COGS-DR-001.md`
> on `SMEsPlus` (commit `d57a52c6f749a89226305b05d05beeb383b10f6c`).
>
> Boss's only remaining action is to schedule its execution and confirm the executor. The prompt's own mandatory reading list (§4.2) already names the correct Inventory Final Solution v1.0 files; this session recommends it be updated to also read this v2.0 dependency package (files 02 and 04 in particular) before execution begins, so the executor understands exactly which of the twelve `JT-*` items its findings will unblock.

---

## 4. Recommended Prompts for the Parallel Sessions (Options B and D)

Carried unchanged from v1.0 (`15_NEXT_PROMPT_RECOMMENDATION.md`, v1.0, §3 and §4) — neither prompt requires any modification, because neither depends on the COGS Gap. Reproduced here by reference rather than duplicated verbatim, to avoid two diverging copies of the same recommendation existing in the repository.

---

## 5. What Should Not Be the Next Session

| Not this | Why |
|---|---|
| The Joint Accounting ↔ Inventory session (Option A), run *before* Option G | It would either stall waiting for evidence mid-session, or rule on 9 of 12 items without the evidence this package's own `HOLD` exists to require. |
| A schema or data-model session | Still blocked by `C-02`, `U-03`, and the absent provenance layer, exactly as in v1.0. |
| A screen or user-interface design session | Still blocked by the total absence of Thai user validation. |
| Any build, migration, or release session | Not authorized by any ruling in this programme. |
| Another Inventory-only functional pass | Diminishing returns, exactly as v1.0 concluded — what remains open is Joint (now specifically COGS-gated), Boss-only, or needs real users. |
| **A second attempt to write this dependency package without running Option G first** | Would produce the same `HOLD` this session reached, with nothing new to say. |

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
