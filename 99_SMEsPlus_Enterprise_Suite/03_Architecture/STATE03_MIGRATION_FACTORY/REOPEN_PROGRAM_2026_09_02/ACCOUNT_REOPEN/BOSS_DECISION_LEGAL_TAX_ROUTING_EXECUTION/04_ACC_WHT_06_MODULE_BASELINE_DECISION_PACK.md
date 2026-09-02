# 04 — ACC-WHT-06 MODULE BASELINE DECISION PACK (`ACC-DEC-003`)

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-003` |
| Source Item | 20 EG-05; 21 §6.3; 22 #1b; A2 §B.1; source `10_TAX_WHT_VAT_CIT_REPORTING_MAP.md` |
| Decision Authority | Boss / Accounting-Tax |
| Owner | UNASSIGNED (Accounting-Tax reviewer, once named) |
| Status | `BOSS DECISION REQUIRED` |
| Gate Impact | `COA-G06`; `ACC-WHT-06` (severity: **HIGH**) |

## The fact this decision turns on

Source `A2` §B.1 records that the benchmark instance had the `l10n_th_withholding_tax_multi` module's **dependency present but the module itself not installed**. This means the benchmark's own observed WHT behaviour (chart of accounts, tax templates, reporting grids referenced across source files `02`, `03`, `10`) reflects **single-rate** WHT handling, not the multi-rate WHT handling that module would add. This is new material fact surfaced only in this study (source `21` §2 item 8) — it was not known when `ACC-WHT-06` was originally scoped.

## Why this matters

Thai withholding tax is not single-rate in practice: WHT rates vary by payment type (services, rent, professional fees, transport, advertising, etc.) and by payee type (company vs. individual) — 1%, 2%, 3%, 5% and others appear in the Thai chart-of-accounts tax templates already read from the benchmark's LGPL localization data (source `21` §2 item 6: "18 tax templates (VAT 7/0/exempt; WHT 1/2/3/5% company/personal/income)"). If SMEsPlus's `ACC-WHT-06` design baselines on the benchmark's as-observed (single-rate-module-absent) behaviour, it risks under-designing multi-rate WHT handling that Thai SME accounting practice requires.

## Decision options

| Option | Effect | Risk if wrong |
|---|---|---|
| **A — Baseline on benchmark-as-observed (module absent)** | `ACC-WHT-06` designs against single-rate WHT only, matching what was actually observable in the benchmark instance | May under-design; Thai SMEs commonly need multi-rate WHT (2/3/5% is routine, not exceptional) |
| **B — Baseline on multi-rate WHT as in-scope regardless of benchmark state** | `ACC-WHT-06` is designed for multi-rate WHT from the start, using the module's *documented* behaviour (not benchmark-observed) as one input among others, subject to `06_LEGAL_TAX_REVIEW_BRIEF.md` confirmation of actual Thai WHT rate structure | Requires re-installing/observing the module in a fresh benchmark instance, or relying on documentation instead of first-hand observation — must be flagged as such |
| **C — Defer `ACC-WHT-06` entirely until legal-tax review (`06`) returns authoritative WHT rate/category citations** | No baseline chosen now; `ACC-WHT-06` stays `HOLD` until Thai statutory WHT categories and rates are confirmed by a qualified reviewer | Slower; but avoids designing against either an incomplete benchmark observation or unverified module documentation |

## Recommendation basis (not a decision)

This session does not recommend an option — that is Boss's call per governing-prompt Charter constraints. What can be stated as fact: **Option A is the only option not requiring any further evidence-gathering**, because it is what was actually observed. Options B and C both require additional evidence (module re-observation, or legal-tax citations respectively) before `ACC-WHT-06` can be considered evidenced rather than assumed.

## Boss decision record

| Field | Value |
|---|---|
| Option selected | ☐ A ☐ B ☐ C |
| Additional evidence commissioned (if B or C) | _______________________________________________ |
| Decided by | _______________________________________________ |
| Date | _______________________________________________ |

Until completed, `ACC-WHT-06` remains `HIGH` severity `BOSS DECISION REQUIRED` and `COA-G06` cannot proceed on the WHT sub-item.
