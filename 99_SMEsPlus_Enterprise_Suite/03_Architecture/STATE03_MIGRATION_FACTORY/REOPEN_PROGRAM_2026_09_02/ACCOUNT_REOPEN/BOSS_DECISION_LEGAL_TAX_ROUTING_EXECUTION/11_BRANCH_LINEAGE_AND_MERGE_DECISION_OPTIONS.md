# 11 — BRANCH LINEAGE AND MERGE DECISION OPTIONS

| Field | Value |
|---|---|
| Decision IDs | `ACC-DEC-016` (merge/lineage), `ACC-DEC-017` (missing G-A3 package) |
| Source | `20_GAP_OWNER_GATE_IMPACT_REGISTER.md` EG-08, EG-11; `21_BOSS_FINAL_GATE_PACKAGE.md` §6 item 6; `22_NEXT_PROMPT_RECOMMENDATION.md` §2 items 9, 10; source `01_PRIOR_EVIDENCE_AND_LINEAGE_REGISTER.md` §A–§B (referenced) |
| Owner | Boss / repo owner |
| Status | `BOSS DECISION REQUIRED` (both) |
| Gate Impact | Discoverability from canonical branch; evidence chain (no COA gate directly moved) |

## The situation as recorded

Three Account-track artefacts exist only on unmerged branches off `SMEsPlus`:

1. This study's package — `audit/account-menu-process-deep-study-2026-09-02-001` (verified in `01`, commit `5183e9f6ef4272e68c65d831580886e341118d53`)
2. A prior "Ai Audit SMEsPlus" package — `audit/account-ai-audit-smeplus-2026-09-02-001`
3. A governing prompt file — `prompt/account-menu-process-deep-study-2026-09-02`

Separately, source `20` EG-08 records that the Account Reopen program's originally planned **18-deliverable package (`G-A3`)** is missing, and that an earlier prompt in the lineage cited a branch/commit that **did not exist** (this session's own source citation has since been independently verified in `01` and does not repeat that defect).

## `ACC-DEC-016` — Merge/lineage decision for the three unmerged artefacts

| Option | Effect | Trade-off |
|---|---|---|
| **A — Merge all three to `SMEsPlus`** | All three become discoverable from the canonical branch without needing to know branch names | Merging is normally irreversible in effect (history becomes part of canonical); this session must **not** perform this merge itself — it requires Boss's explicit order per governing-prompt §13 ("Do not merge to `SMEsPlus`") |
| **B — Keep as unmerged evidence branches, but publish an index** | Canonical `SMEsPlus` gets a small pointer/index file (e.g., in the reopen program's session register) listing branch names, commits, and one-line descriptions, so a reader of canonical `SMEsPlus` can find them without a merge | Lowest-risk option; matches the established session pattern already used for the Inventory reopen program (an index/register file, not a merge) |
| **C — Selective merge** | Only the packages Boss judges final/stable (e.g., this study's package, once its own open items in `20` are resolved) are merged; the others stay as evidence branches | Requires Boss to judge "stable enough," which is itself a governance call, not a technical one |

**No option is recommended by this session** — governing-prompt §13 is explicit that this session may not open a PR or merge without a direct Boss order. This table exists so Boss's decision can be recorded against a concrete option set rather than an open-ended question.

## `ACC-DEC-017` — Missing 18-deliverable Account Reopen package (`G-A3`)

| Option | Effect |
|---|---|
| **A — Recreate `G-A3`** | A future session is commissioned to produce the originally planned 18-deliverable package from scratch, using this study and the prior Ai Audit package as inputs |
| **B — Accept the prior Ai Audit package + this menu-process-deep-study package as `G-A3`'s replacement** | Boss formally rules that the *combination* of these two existing packages satisfies whatever purpose `G-A3` was meant to serve, closing the lineage gap without new production work |
| **C — Leave open, revisit after `COA-G01` unblock** | No decision now; the question is deferred until `09` (COA-G01 unblock) resolves, on the reasoning that `G-A3`'s content would itself depend on G01-gated facts |

## Recommended sequencing (not a decision)

If Boss selects Option B for `ACC-DEC-017` (accept existing packages as replacement), that also strengthens the case for Option B or C on `ACC-DEC-016` (index rather than merge), since there would then be exactly two canonical Account artefacts to index rather than three plus a yet-to-be-recreated fourth. This is offered as a sequencing observation only — both decisions remain independently Boss's to make.

## Boss decision record

| Field | Value |
|---|---|
| `ACC-DEC-016` option selected | ☐ A ☐ B ☐ C |
| `ACC-DEC-017` option selected | ☐ A ☐ B ☐ C |
| Decided by | _______________________________________________ |
| Date | _______________________________________________ |
