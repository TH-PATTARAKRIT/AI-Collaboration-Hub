# Prior Evidence Load and Path Register

## A. Governing-prompt commit baseline — verification result

All 6 hashes cited in the governing prompt's "Mandatory Governance Baseline" were checked with `git cat-file -t` against `AI-Collaboration-Hub`.

| # | Cited as | Hash | Exists? | What it actually contains | Account-specific? |
|---|---|---|---|---|---|
| 1 | Full Reopen Program | `42e04e639f2c83aeef6d7c313152a55170a4c6ef` | ✅ real commit, 2026-09-02 01:25:29 | New file: `BOSS_GATE/REOPEN_PROGRAM_2026_09_02/STATE03_BOSS_ACCOUNT_INVENTORY_FULL_REOPEN_PROGRAM_2026_09_02.md` — authorizes 3 parallel tracks: Account, Inventory, and Account×Inventory Joint | Partial — jointly scoped with Inventory |
| 2 | Account 9-Veto Challenge/Readiness | `4fb9db04621707becf04e69822147370b9002a72` | ✅ real commit, 2026-09-02 01:26:12 | New file: `ACCOUNT_REOPEN/00_PRE_PROMPT_9VETO_CHALLENGE_AND_READINESS.md` — Account-specific delta triggers and Council questions | Yes — the only purely Account-specific commit of the 5 |
| 3 | NEW PROMPT Governance v2.0 | `03b4244b2101e8c0a89d36255cc654fc2537c748` | ✅ real commit, 2026-09-02 01:14:53 | Modified: `00_Project_Governance/STATE03_PLUS_PRE_PROMPT_INDEPENDENT_CHALLENGE_RULE.md` v1.1→v2.0 | No — project-wide governance rule, domain-agnostic |
| 4 | 9 Veto/9 Special Team Charter | `5d81d628b9b159f89a93da7ab920c42ef8f09555` | ✅ real commit, 2026-09-02 01:16:03 | New file: `00_Project_Governance/NINE_VETO_COUNCIL_AND_SPECIAL_TEAM_CHARTER.md` | No — project-wide charter |
| 5 | Global Challenge Ledger | `f8d940900896a5a11e7232bac0e829fc5a60e908` | ✅ real commit, 2026-09-02 01:16:26 | New file: `00_Project_Governance/GLOBAL_CHALLENGE_CONTINUITY_LEDGER.md` | No — process ledger, "accounting" appears nowhere in it |
| 6 | Local Account Reopen publication commit | `fc468ed` | ❌ **not found** | N/A | N/A |

**Net finding:** 5 of 6 cited hashes are real and unmodified from what the prompt claims — this baseline was not fabricated. But only 1 of the 5 (`4fb9db0`) is substantively Account-specific; 3 are domain-agnostic governance scaffolding that would read identically for any domain; 1 is jointly Account+Inventory scoped. All 5 were committed within an 11-minute window (01:14–01:26, 2026-09-02) — same-day scaffolding for this investigation, not an established track record. The 6th hash does not exist anywhere checked.

## B. Canonical path register

| Path (rooted at `ISOLATED_ACCOUNT_CORR5/`) | Status | Notes |
|---|---|---|
| `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/` | ✅ exists, current | ~22 lettered rulings (README, D, AF–AX) + STATE03 execution prompt; true order verified via `git log --diff-filter=A`, not alphabetical (letters AH and AQ each reused) |
| `.../TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/` | ✅ exists, current | B01–B24 design pack + `COA_G01_EVIDENCE/` (99 files) + `COA_STANDARD/` (3 files) |
| `.../TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/` | ✅ exists, current | 18 numbered research registers |
| `.../PMO_VERIFICATION/`, `.../CHATGPT_AUDIT/`, `.../TEAM_B_HANDOFF/` | ✅ exist, current | Not exhaustively deep-read this pass; structurally confirmed present |
| `.../REOPEN_PROGRAM_2026_09_02/` | ❌ does not exist inside `ISOLATED_ACCOUNT_CORR5` | Only exists under the excluded `INVENTORY_REOPEN_2026_09_02_EXECUTION/` non-git folder |
| `.../REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/EXECUTION/` (claimed, 18 files + SHA-256 manifest) | ❌ does not exist anywhere | See CP-01 finding |
| Root-level `/03_Architecture/STATE03_MIGRATION_FACTORY/` (sibling to `AI-Collaboration-Hub`, non-git) | ⚠️ exists but **stale** | Same structure, materially behind `ISOLATED_ACCOUNT_CORR5` (e.g. `BOSS_GATE` has 1 file vs. ~22) — usable only as older reference, never as current state |

## C. Real Account git branch register

| Branch | Local/remote sync | Commits | Tip | Payload |
|---|---|---|---|---|
| `audit/account-wht-grpa-m18-closure-010` | Identical — no divergence | 48 unique vs. merge-base `a4cebfc` | `fe356f7` | WHT (withholding tax) closure package for "GRPA-M18"; 180 files changed vs. base, 19,290 insertions, almost entirely governance/evidence markdown |
| `audit/account-reopen-2026-09-02-acc-reopen-001` (cited in governing prompt) | N/A | N/A | N/A | **Does not exist**, local or remote |

## D. Boss-instruction disposition

Per Boss decision recorded in [00_CHECKPOINT_EXECUTION_LOG.md](00_CHECKPOINT_EXECUTION_LOG.md), this entire investigation proceeds only on rows marked ✅ above. Rows marked ❌ are carried as `HOLD / EVIDENCE REQUIRED` in [07_MATERIAL_UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md](07_MATERIAL_UNKNOWN_AND_EVIDENCE_GAP_REGISTER.md), not assumed complete and not recreated.
