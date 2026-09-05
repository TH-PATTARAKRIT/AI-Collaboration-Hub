# 52 — P05 CERTIFICATE FINDING REVISION

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E13`
Consolidates the certificate corrections made in `P05#03` (`25 §3`) and re-bounds them with this
round's v18 evidence. **Original claims preserved; nothing silently rewritten.**

| # | Original finding | Why it was wrong | Evidence used to correct | Corrected finding | Severity effect | Handoff effect | Veto effect |
|---|---|---|---|---|---|---|---|
| 1 | **`TX-20`** — *"4,081 of 5,201 certificates (78.5%) carry a date that is not the payment date"*, attributed to a create-time default on `date` | The author compared two columns and **assumed which was the truth**, never joining to the payment | `account_payment.move_id` → `account_move.date`, 3,794 joined, **0 unjoinable** | `payment_date` = `create_date::date` in **5,201/5,201 = 100.00%**; the printed `date` matches the real payment date in **97.79%**; `payment_date` matches in **16.05%**; deltas are **negative** | **Inverted, not reduced.** A `NOT NULL` column named `payment_date` carries no payment information in 100% of rows | `H-P07-3` restated | none |
| 2 | **`TX-13`** — *"32 payments hold multiple live statutory certificates"*, one holding nine | Filter admitted `draft`; never grouped by supplier | Decomposition by `supplier_partner_id`, state and rate | 21 of 32 are **one certificate per distinct payee** on bulk runs; 8 are same-payee **rate splits**; 2 are `done`+`draft`; **1 exact duplicate** (payment 659, certs 124/126, identical number `JRCSH12023100176`) | **Overstated ~30×.** Survives as a control defect with one instance | `H-P07-2` restated | none |
| 3 | `TX-15` — 13 unreportable `pnd1` certificates | — | reproduced exactly | **CONFIRMED** | unchanged | routed | none |
| 4 | `TX-14` — sparse substitution refs | Two explanations considered, a third missed | `ref_wt_cert_id` FK is `ON DELETE SET NULL` | **Class `D` upheld**; reasoning completed | unchanged | — | none |
| 5 | **`TX-01a`** — *"all seven WHT codes point at one account; `WHT3%` rate is 0"* | **Generalised from one database** | v18 target: **40 codes, 4 accounts, 4 companies, rates 1/2/3/5, no zero-rate** | **Re-bounded to `iSMEs` v16 only** | claim narrowed | `H-P07-12` re-bounded | none |
| 6 | Population caveats omitted | — | — | 1,407 certs (27.1%) have neither `payment_id` nor `move_id`; `move_id` populated on **0**; 1,417 have **no certificate number**, 1,414 of them `done`; 75 numbers shared; 362 of 6,159 lines orphaned | new material | `H-P07-9`, `H-P07-10` | none |

## v18 Cross-Check

`idemo18_uat` holds **332 certificates** against `iSMEs`' 5,201. The v18 population was **not**
re-analysed for duplication or dating in this round — budget was spent on the petty-cash contradiction
and the TX-01 denominator. **Class `C — NOT YET SEARCHED`**, recorded as `U-19`.

This matters: every corrected certificate figure above is **v16 evidence**. Whether the same patterns
hold at v18 is open, and the v19 schema regression (`DB-06`) shows the model does change across
versions. **The corrections are not asserted as platform-general.**

## Net Effect

| | |
|---|---|
| Findings withdrawn outright | 0 |
| Findings inverted | 1 (`TX-20`) |
| Findings materially reduced | 1 (`TX-13`) |
| Findings re-bounded to one database | 1 (`TX-01a`) |
| Findings confirmed | 2 |
| New findings from the correction work | 9 (`DB-01`..`DB-09`) |
| Vetoes affected | **none** |
