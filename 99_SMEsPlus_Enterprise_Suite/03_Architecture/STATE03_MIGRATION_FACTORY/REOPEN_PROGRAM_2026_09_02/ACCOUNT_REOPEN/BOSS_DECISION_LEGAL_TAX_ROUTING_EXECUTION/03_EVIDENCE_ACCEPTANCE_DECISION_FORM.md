# 03 — EVIDENCE ACCEPTANCE DECISION FORM (`ACC-DEC-001`)

| Field | Value |
|---|---|
| Decision ID | `ACC-DEC-001` |
| Source Item | 20 EG-10; 21 §6.1; A1 §A; 17 VC-08 |
| Decision Authority | Boss |
| Owner | Boss (UNASSIGNED for execution once ruled) |
| Status | `BOSS DECISION REQUIRED` |
| Gate Impact | None directly moved by this decision, but every menu-tree and installed-module fact in source files `02`, `03`, `05`, `A1`, `A2` rests on it |

## What is being decided

Source files `A1_BENCHMARK_MENU_TREE_EVIDENCE_iTEST02.md` and `A2_BENCHMARK_INSTALLED_ACCOUNTING_MODULES_iTEST02.md` were produced by extracting metadata from a Docker-hosted benchmark database dump (not a running, screenshot-observed instance). Source `20` (EG-10) and `17` (VC-08) record that this extraction method was **not covered by an explicit prior authorization record**. Boss must now acknowledge or reject this method, after the fact, as valid evidence for the 116-node menu tree and installed-module list it produced.

## What is NOT being decided here

- The correctness of any individual menu label or module name (those stand as recorded in `A1`/`A2` unless Boss identifies a specific error).
- Whether screenshots (a separate, still-missing evidence source — see `ACC-DEC-002`) should also be obtained. That is a parallel, not a substitute, question.
- Any Thai naming, legal, or tax conclusion — those are routed separately (`06`, `08`).

## Decision options

| Option | Effect |
|---|---|
| **A — Accept** | A1/A2 metadata extraction stands as valid evidence going forward. Future sessions may continue to cite it without re-litigating the authorization gap. Boss should record the retroactive authorization (who, when, why) for the audit trail. |
| **B — Reject** | A1/A2 are demoted to unverified/candidate evidence. Every fact in `02`, `03`, `05` that depends solely on A1/A2 (the 116-node menu tree, the installed-module list) reverts to `HOLD / EVIDENCE REQUIRED` pending a re-extraction under an explicit authorization, or pending screenshot evidence per `ACC-DEC-002`. |
| **C — Accept with conditions** | Boss accepts the extraction as evidence but requires a specific compensating control (e.g., independent PMO spot-check of a sample of A1/A2 rows against the live instance) before the menu tree is treated as final. |

## Boss decision record

| Field | Value |
|---|---|
| Option selected | ☐ A — Accept ☐ B — Reject ☐ C — Accept with conditions |
| Conditions (if C) | _______________________________________________ |
| Decided by | _______________________________________________ |
| Date | _______________________________________________ |
| Notes | _______________________________________________ |

Until this form is completed and returned, `ACC-DEC-001` remains `BOSS DECISION REQUIRED` and the status of A1/A2-derived facts in the source package is unchanged from `PROCESS REFERENCE ONLY` (i.e., neither accepted nor rejected — usable as reference, not as approved evidence for Gate movement).
