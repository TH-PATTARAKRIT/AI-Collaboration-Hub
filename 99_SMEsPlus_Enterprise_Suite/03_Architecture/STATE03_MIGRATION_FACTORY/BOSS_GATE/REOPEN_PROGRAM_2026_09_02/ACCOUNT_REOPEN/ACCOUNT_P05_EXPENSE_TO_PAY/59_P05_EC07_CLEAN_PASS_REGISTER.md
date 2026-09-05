# 59 — P05 `EC-07` CLEAN-PASS REGISTER

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E20`

## 1. Definition (quoted, not invented)

From `SMEPLUS-DR-EXIT-8C-001`: at least **two consecutive fresh independent passes** must complete
with none of — new material population · new material finding class · new gating unknown · reopened
tolerance-zero issue · new Gate-changing contradiction · evidence-integrity failure.
*"Reviewer findings must themselves be independently verified before acceptance."*

**Reset rule, as applied here:** any one disqualifier makes a pass unclean and returns the
consecutive counter to **0**. A research-error discovery, a method error, and a peer delta each
qualify **if** they meet one of the six criteria — they are not separate resets.

## 2. Pass Ledger

| Pass | Round | Disqualifiers raised | Clean? |
|---|---|---|---|
| 1 | `P05#02` — four AAS-03 experts | new population (`l10n_th_reports`); 60 new findings; 7 new TZ boundaries; 12 author findings corrected | **NO** |
| 2 | `P05#03` — four experts, targeted closure | new population (6 registries, 5,201 certificates); new finding class; `RE-07` evidence-integrity failure; **2 published findings contradicted** | **NO** |
| **3** | **This round — four challenge classes** | **new material population (`idemo18_uat`, the target platform); new gating unknowns `U-15`..`U-18`; `RE-20` evidence-integrity failure; `TZ-01` contradicted — a Gate-changing contradiction** | **NO** |

## 3. Status

> **`EC-07`: 0 of 2. The counter has been reset three times.**

Blocker classification: **INTERNAL — METHOD**. Not waiting on an external party.

**The counter cannot advance while the evidence base is still moving.** Each of the three passes
discovered a population the previous one did not have. The earliest a clean pass is possible is after
`U-18` (`pankhamhom`), `U-15` (`scgl_signature_hr_expense`) and `U-16` (source-vs-deployed) are closed
— because each is a known, named source of a further material population.

**No self-certification is offered.** This session does not declare any pass clean, including its own.
