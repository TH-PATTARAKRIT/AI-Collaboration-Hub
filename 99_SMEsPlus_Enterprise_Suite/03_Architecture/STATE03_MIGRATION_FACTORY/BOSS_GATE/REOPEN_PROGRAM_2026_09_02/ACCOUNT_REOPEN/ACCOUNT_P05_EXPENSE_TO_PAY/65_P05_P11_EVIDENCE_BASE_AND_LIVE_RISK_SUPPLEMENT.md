# 65 — P05 → P11 EVIDENCE-BASE AND LIVE-RISK SUPPLEMENT

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E27`

> ## **SUPPLEMENT TO THE PRIOR P05 HANDOFF — NOT A REPLACEMENT.**
> `19_P05_CORE_RECON_HANDOFF_PACK.md` and everything it cites remain in force except where corrected
> below. This file carries **material delta only**.

## 1. Evidence-Base Correction — the delta that changes everything else

The prior handoff rested on a population that **excluded the target platform**.

| | Prior handoff | Now |
|---|---|---|
| Database identities | 6 "registries" | **9 identities**, 7 readable, 1 unread, 2 zero-byte |
| Odoo 18 database with the P05 surface | **"none exists in the available evidence"** | **`idemo18_uat` — 44 MB, on the host throughout** |
| Search method | folders where dumps had been found | **exhaustive filesystem search**, root + pattern + unit declared |

**`RE-20`.** P11 should treat any prior P05 statement of the form *"not found in the deployed
population"* as **class B at best** unless it post-dates `41`.

## 2. Deployed Reality on the Target Platform (`idemo18_uat`, Odoo 18.0, 4 companies)

| Module | State | Note for P11 |
|---|---|---|
| `hr_expense` | INSTALLED | **993 expenses, 979 sheets** |
| **`hr_expense_petty_cash`** | **INSTALLED 18.0.1.2** | **634 of 993 expenses (63.8%) are `petty_cash`** — the dominant mode. `own_account`: **2**. |
| `scgl_advance_expense_request` | **uninstalled** | employee advance deployed **nowhere** across 6 registries |
| `scgl_purchase_advance_payment` | **uninstalled here**; installed in 4 of 6 others | P01 territory |
| `l10n_th_withholding_tax*` (4 modules) | INSTALLED | 40 codes, 4 accounts, 4 companies, 332 certificates |
| `l10n_th_reports` | INSTALLED | **both** WHT subsystems present together |
| `hr_expense_extract`, `account_payment_multi_deduction`, `account_disallowed_expenses` | **INSTALLED** | all three were "absent/uninstalled" in the prior handoff |
| `scgl_signature_hr_expense` | **INSTALLED** | **never analysed by P05** — `U-15`, class `C` |

> **P05's depth of analysis was inverted relative to real usage.** The employee-reimbursement path
> P05 traced most thoroughly is used **twice**; petty cash, traced as a defect story, is the dominant
> mechanism.

## 3. The Provenance Finding — P11 should apply this programme-wide

**All 712 expense-sheet-linked journal entries in the target database were created on 2026-08-25 by
`create_uid = 1` in a journal named `"COA Migration 2026"`, prefix `MIG26/`, with back-dated
accounting dates.** Zero were produced by live application posting.

Consequences:

1. A correct, reproducible measurement over that population **cannot answer any question about live
   application behaviour**. P05 published such a conclusion and withdrew it (`RE-27`).
2. **P11 should require provenance — who created these rows, when, by what process — before accepting
   any cross-process reclassification built on database evidence.** This is `AASV-03`.
3. Any peer package that has reclassified findings using these same dumps is exposed to the same
   defect. P05 asserts nothing about peer packages; it flags the risk.

## 4. Corrected Risk Picture

| Finding | Prior handoff | Now |
|---|---|---|
| `TZ-01` petty cash | headline defect → then `LATENT` | **`C — NOT DECIDABLE`.** Source defect unrebutted; no live posting exists to test it |
| `PC-01` *(new)* | — | 238 of 625 petty-cash sheets have **no linked entry**, 206 `done`. Counts class `A`; cause class `C` |
| `TX-01` | 92.55% (v16) | **100.00% on the v18 target** — 358 of 358. Structurally overdetermined. **Best-evidenced finding in the package** |
| `TZ-11a`/`TZ-12` (P01) | "live in all four real business databases" | installed in 4 of 6, **not** on the target; exercised **21×** in one; **financial effect never observed** |
| Employee advance cluster | `LATENT` | **confirmed latent** across all 6 registries — strengthened |
| `account_move_line.expense_id` | — | **NULL on all 815 lines examined** — line-level traceability absent |

## 5. Registers Delivered

`40` checkpoints · `41` evidence base · `42` DB population · `43` module matrix · `44` live/latent ·
`45`–`47` reclassifications · `48` authorisation · `49` P01 · `50`–`51` TX-01/P07 · `52` certificates ·
`53` `R-01` · `54` errors `RE-07`..`RE-28` · `55` method failure · `56` exit criteria ·
`57` handoff · `58` tolerance-zero · `59` `EC-07` · `60` dump boundary · `61` peers · `62` challenges ·
`63` vetoes · `64` PMO.

## 6. Remaining External Blockers

| Blocker | Class |
|---|---|
| **Runtime execution** (`U-02b`) — the only way to observe live posting and settle `TZ-01`, `PC-01`'s cause, `TX-14`, `U-03` | `HOLD — RUNTIME EVIDENCE REQUIRED` |
| **`U-16`** — deployed code vs analysed source copy, unverified either way | `HOLD — RUNTIME` |
| `U-15` `scgl_signature_hr_expense` unanalysed · `U-18` `pankhamhom` unread · `U-19` v18 certificates unanalysed | class `C` — all P05-closable |
| Thai statutory (`U-09`) | P07 |

## 7. Boundary

P05 decides no peer's canonical architecture, asserts no Thai statutory position, and declares no
financial loss. Every item carries its evidence class. **`PEER DEPENDENCY OPEN` for P01, P06, P07,
P08, P09, P11 — none of which has consumed any P05 output, and four of which have published no branch.**
