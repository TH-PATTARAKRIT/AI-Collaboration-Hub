# Material Unknown and Evidence Gap Register

No silent caps: every gap found this session is listed here, none suppressed or converted into apparent progress.

## A. Structural / evidence-location gaps (from CP-00/CP-01)

| ID | Gap | Where found | Status |
|---|---|---|---|
| G-A1 | Governing prompt's execution branch `audit/account-reopen-2026-09-02-acc-reopen-001` does not exist, local or remote | `AI-Collaboration-Hub` | `HOLD` — Boss to confirm intended branch, or accept `audit/account-wht-grpa-m18-closure-010` as the real Account branch |
| G-A2 | Commit `fc468ed` cited as "local Account Reopen publication commit" does not resolve anywhere checked | 6 locations checked | `HOLD` — unverifiable; treat as erroneous citation unless Boss can locate it elsewhere |
| G-A3 | Claimed 18-file Account Reopen execution package + SHA-256 manifest does not exist | `.../REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/` (only 2 input files present) | `HOLD / EVIDENCE REQUIRED` per explicit Boss directive — not recreated without separate authorization |
| G-A4 | Root-level `03_Architecture/STATE03_MIGRATION_FACTORY/` is a stale snapshot materially behind `ISOLATED_ACCOUNT_CORR5` (e.g. 1 vs. ~22 Boss Gate rulings) | Root folder, sibling to `AI-Collaboration-Hub` | Open — see VC-01; Boss should mark it archived/superseded |
| G-A5 | 3 different folders all sit on canonical branch `SMEsPlus` at 3 different commits with no marker distinguishing which is authoritative | `ISOLATED_ACCOUNT_CORR5`, `AI-Collaboration-Hub-CORR3`, `AI-Collaboration-Hub-CORR5-ISOLATED` | Resolved for this session by Boss directive; underlying ambiguity (why 3 copies exist) not investigated |

## B. Content gaps within Accounting Core (from the 12 P0 questions)

| ID | Gap | P0 ref | Severity |
|---|---|---|---|
| G-B1 | VAT and CIT: zero research performed anywhere in the inspected corpus | VC-06 | High — undecided whether in-scope or deferred |
| G-B2 | WHT multi-rate: source module silently drops GL tagging for 2+ rate payments on one transaction | P0-2, `ACC-WHT-06` | High — Boss-flagged, held pending module-baseline decision |
| G-B3 | 50-TWI: 3 tax-form checkboxes + 2 WHT-condition checkboxes missing from print template | P0-3 | Medium — already routed to legal-tax review |
| G-B4 | PND3/PND53: `tax_report_pnd.py` duplicated across 2 modules (deployment-dependent output); WHT-condition export column hardcoded to `'1'` | P0-4 | Medium — code-quality/localization risk, not yet remediated |
| G-B5 | AR/AP aging and fixed-asset roll-forward: explicitly "no research performed" | P0-10 | High — full scope absence, blocks migration-reconciliation sign-off |
| G-B6 | SaaS standard-template mechanics: explicitly unapproved, open since Round 1 through Round 7 | P0-9 | Medium — blocks COA-G04S |
| G-B7 | Upgrade preview / upgrade audit trail: not evidenced either way | P0-9 | Medium — unresearched, not confirmed absent |
| G-B8 | SoD, granular permissions, backup/recovery, destructive-action controls: not directly evidenced in this pass | VC-07 | Medium — likely exist in `B09` CO-01–16 but not confirmed against these specific topics |
| G-B9 | Boundary analysis (`B03`-style) exists for Inventory only; not confirmed for Sales, Purchase, Expense, Employee, Manufacturing | VC-03 | Medium |
| G-B10 | Landed cost / returns / inventory-adjustment posting scenarios not individually traced across the Account×Inventory boundary | ST-06 | Medium |

## C. Unread-but-inventoried evidence (real files, content not yet verified)

| ID | Location | Size | Note |
|---|---|---|---|
| G-C1 | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_G01_EVIDENCE/` | 99 files (36 top-level + `COA_G01_SOURCE_PORT/STATE03_LOCAL/` 63 ported files) | Structurally mapped, not content-verified. Likely contains the "389/389" figure referenced in the governing prompt (unlocated — see ST-02) |
| G-C2 | `TEAM_B_DESIGN/DOMAIN_01_ACCOUNTING_CORE/COA_STANDARD/` | 3 files | Likely substantiates "36 Base Kernel" / "19 active types" (governing prompt Section 7 item 3) — unverified |
| G-C3 | `PMO_VERIFICATION/`, `CHATGPT_AUDIT/`, `TEAM_B_HANDOFF/` (full contents beyond the single named file each) | Not counted | Structurally confirmed present, not deep-read this session |

## D. Open Boss-decision items (verbatim from source, not paraphrased away)

1. **N-04** — Thai financial-statement PDF (`งบการเงิน 2567.pdf`) inaccessible; Boss must reissue file access.
2. **N-05** — "ACCEPTED RESIDUAL UNKNOWN — BOSS DECISION REQUIRED."
3. **C-03** — "BOSS DECISION REQUIRED" (S1 substantive status).
4. **ACC-WHT-06** — Boss must confirm whether `l10n_th_withholding_tax_multi` is part of the intended module baseline.
5. Standard COA template option (`B13` DT-03) — awaiting Boss decision.
6. Whether Inventory-backbone content inside the Account worktree (`ISOLATED_ACCOUNT_CORR5`) is intentional joint-tracking or drift (this session's own finding, G-A4/file 09).

None of the above have been resolved by this session. All are preserved here exactly as found.
