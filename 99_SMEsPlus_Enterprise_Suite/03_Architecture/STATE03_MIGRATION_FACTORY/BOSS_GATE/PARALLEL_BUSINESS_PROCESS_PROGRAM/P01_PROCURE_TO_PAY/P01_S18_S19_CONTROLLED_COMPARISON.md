# P01 — SERIES-18 vs SERIES-19 CONTROLLED COMPARISON

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-09`

**Precondition, and it was observed.** Each generation was classified **independently** before any
comparison was drawn. The series-18 classification is in
`P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md`, reached without reference to the series-19 estate.
The series-19 classification is the one already published in rounds 3 and 4. This document is the
**first** point at which the two are placed side by side.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. THE OBSERVATION THAT LOOKS IDENTICAL

| | Series-18 deployment (`idemo18_uat`) | Series-19 estate (`E-1`) |
|---|---|---|
| `stock_valuation_layer` rows | 47,801 | 14,441 movements |
| …carrying `account_move_id` | **0** | **0** |

**Two identical zeros.** Everything below is about why they are not the same fact.

---

## 2. THE DISCRIMINATING VARIABLES

| Variable | Series 18 | Series 19 | Same? |
|---|---|---|---|
| Valuation policy | **`manual_periodic`**, 126/126 categories × 4/4 companies | `real_time` intended | **NO** |
| Policy label in that generation | `manual_periodic` = "Manual" | `real_time` = "Perpetual (at invoicing)" | **NO** |
| Valuation account configured | 15 categories jsonb + company default (co 1 all) | **43 of 44 companies** via company defaults | broadly yes |
| **Stock journal configured** | **YES — all 4 companies (`STJ` 16/24/32/40)** | **NO — unset on 44 of 44** | **NO** |
| Goods-received clearing account | **configured, 171 of 504 pairs**, `210300` reconcilable | not the published binding gap | **NO** |
| Bill-line account override module | **absent from the source tree** | present (`stock_account/models/account_move_line.py`) | **NO** |
| Anglo-saxon accounting | on in company 1 only | — | — |
| Receipt-side clearing bridge in source | **present** | **removed by design** | **NO** |
| Journal entries in the deployment | 15,522 | 16 | **NO** |
| Is the zero expected? | **YES — the policy specifies it** | **NO — the policy intends posting** | **NO** |

---

## 3. THE VERDICT

> ### SAME SHAPE / DIFFERENT CAUSE.

| | Series 18 | Series 19 |
|---|---|---|
| Cause of the zero | **Valuation policy is periodic.** The gate at `stock_valuation_layer.py:81` never opens. The journal and the clearing account are configured and dormant | **The company stock journal is unset on 44 of 44 companies.** The policy intends posting and the binding configuration is missing |
| Classification | **EXPECTED UNDER PERIODIC POLICY — VERIFIED** | **DEFECT — configuration gap** (`ERR-P01-19` corrected the *cause*; the conclusion stands) |
| Remediation | **None required.** Changing anything here is a business policy decision, not a fix | **Set the company stock journal.** Setting the valuation account — the round-3 remediation — would not have helped |
| What a reader must not do | Read the series-18 zero as a defect | Read the series-19 zero as a policy |

**If these two zeros had been merged, the result would have been a single false statement in both
directions**: it would have declared a correctly-configured periodic system defective, and it would
have offered "the policy explains it" as a defence for a system whose journal is genuinely missing.

---

## 4. WHERE THE GENERATIONS GENUINELY DIVERGE IN SOURCE

Independent of configuration, the two generations are **not the same software**:

| Mechanism | Series 18 | Series 19 |
|---|---|---|
| `stock_account/models/` file count | 15 | 17 |
| `account_move_line.py` in `stock_account` | **absent** | present — carries `_compute_account_id` redirecting the bill line to the valuation account |
| `property_valuation` label for `real_time` | "Automated" | **"Perpetual (at invoicing)"** |
| Receipt-side clearing bridge | present | **removed by design** |
| Price-difference replay engine | present (`purchase_stock`) | **absent** |

**`ERR-P01-10` remains correct and is now better supported.** The series-19 change is a deliberate
redesign — recognition moved to invoicing — not a misconfiguration. Reading it as a defect was the
error; reading the series-18 zero as the same defect would have been a second, larger one.

---

## 5. WHAT THE COMPARISON DOES *NOT* LICENCE

- It does **not** make the series-18 deployment a substitute for the series-19 estate. Findings
  measured in `E-1`, `E-2` or `E-3` stay bound to those populations.
- It does **not** transfer the series-18 policy explanation to the series-19 zero. That was tested
  and refused: series 19's journal is unset, which is an independent and sufficient cause there.
- It does **not** establish which generation the project should target. That is a Boss decision,
  and P01 does not make it.
- It does **not** resolve whether periodic valuation is right for this business. See
  `P01_S18_GRNI_CLEARING_ACCOUNT_PROOF.md §9`: the configuration was built for a perpetual bridge
  and the switch is set to periodic, with a series-14 predecessor that did post to a stock journal.
  **That is the question this comparison hands upward.**

---

## 6. ONE SENTENCE FOR THE DECISION PACKAGE

> Two deployments in this estate show no inventory value reaching the general ledger from goods
> receipts, and they show it for opposite reasons: in the series-18 system the valuation policy is
> periodic and the absence is correct; in the series-19 estate the policy intends posting and the
> journal that would carry it is unset in every company.

Same shape. Different cause. **Different decision.**
