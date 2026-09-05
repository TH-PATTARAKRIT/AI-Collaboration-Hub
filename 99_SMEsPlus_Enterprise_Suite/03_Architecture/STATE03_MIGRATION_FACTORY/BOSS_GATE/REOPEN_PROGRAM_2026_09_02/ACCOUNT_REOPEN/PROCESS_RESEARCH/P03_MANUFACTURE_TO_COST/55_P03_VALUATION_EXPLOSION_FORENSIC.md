# 55 — VALUATION EXPLOSION FORENSIC

**LAYER 2 — AUDIT QUARANTINE.** The largest single finding of the P03 package.

---

## 1. What was found

Thirty rows of the `iSMEs` inventory valuation ledger carry values between ±1 × 10¹² and
**±1.5 × 10²¹**. The ledger has 74,982 rows, every one well-formed (19 columns, zero
unparseable cells) — **this is data, not a parsing artefact**, and the check that
established it is recorded because the first draft of this analysis wrongly assumed the
opposite.

| Measure | Value |
|---|---|
| Valuation ledger total, all 74,982 rows | **205,490,835.88** |
| Excluding the 30 corrupt rows | **400,338,755.98** |
| **Distortion contributed by 30 rows** | **−194,847,920.10 = −48.7 %** |
| Corruption window | **2024-08-28 → 2024-09-03**, 5 distinct days |
| Ledger span | 2023-10-03 → 2026-07-11 |

## 2. The subsidiary ledger has diverged from the general ledger

| Test | Result |
|---|---|
| Corrupt rows claiming a journal entry | **25 of 30** |
| Those journal entries **exist** | **25 of 25** |
| Amount **matches** the valuation row | **0 of 25** |
| Amount **mismatches** | **25 of 25** |
| GL lines anywhere with \|balance\| > 1e12 | **0** |
| Sum of all 447,384 GL line balances | **0.00 — balanced** |

Example: valuation row 27394 carries **1,533,508,025,629,365,764,096.00**; its journal
entry 105228 has a total debit of **874,350.00**.

> **`P03R-F-01`. The general ledger is balanced and sane. The inventory valuation
> subsidiary ledger is not. They disagree on 25 rows by up to eighteen orders of
> magnitude.** `FACT VERIFIED`.

The stock-valuation report and the balance-sheet inventory account **cannot reconcile**.

## 3. Causal chain — where it starts, and it is not manufacturing

Product 11556, a jasmine-rice raw material. Full valuation history read; the break is
unambiguous.

| Date | Event | Unit cost |
|---|---|---|
| 2023-10-23 → 2024-08-27 | ordinary vendor receipts | **27.50 – 31.66** |
| **2024-08-27 09:46** | vendor receipt `WH/IN/03634` | **712,186.25** ← **first break, ×23,000** |
| 2024-08-28 08:26 | bill revaluation `AP2024081214`, no move | value −10,954,387,437.50 |
| 2024-08-28 09:25 | receipt `WH/IN/03689` | 4,456,673,707.51 |
| 2024-08-29 09:26 | receipt `WH/IN/03707` | 15,685,015,415,021.04 |
| 2024-08-30 09:17 | receipt `WH/IN/03709` | **52,616,504,567,828,624.00** |
| 2024-08-30 09:19 / 09:27 | revaluations `AP2024081365`, `AP2024081372` | −4.4e17, −5.0e17 |

**Ordinary receipts at 30.00–30.84 continue interleaved on the same days**, so this is not a
unit-of-measure change or a currency error — it is a **compounding average-cost feedback
loop**, driven by vendor-bill price-difference revaluations on an average-costed product.

**Origin: the purchase receipt / vendor bill path.** P01 and the Inventory track own that
mechanism. **P03 does not adjudicate it and does not claim it.**

## 4. How manufacturing amplified it

| Date | Manufacturing event | Effect |
|---|---|---|
| 2024-08-31 09:17 | **MO 4410** consumes 11556 | raw layer at unit −1,608,091,395,637.72 |
| same instant | MO 4410 produces 11630, 11632, 11633 | finished layers at up to 2,266,696,491,129.46/unit |
| 2024-08-31 09:59 | **MO 4412** | same shape |
| 2024-09-03 09:32–09:33 | **UNBUILD 440–444** release 11632 | five layers at −352,468,555,154.38/unit |

Product 11632's own history: 349 valuation rows, unit costs **13.83 – 279.91** for ten
months, then **2,266,696,491,129.46** the moment MO 4410 valued it.

### Attribution of the 30 corrupt rows

| Origin | Rows | Net value |
|---|---|---|
| Revaluation (no move) | 4 | −940,247,640,679,603,456.00 |
| **Receipt / other — P01 or Inventory** | **8** | 736,631,055,036,973,056.00 |
| Raw consumption — **P03** | 2 | 197,850,793,351,276,800.00 |
| Finished output — **P03** | 4 | 197,850,793,351,274,400.00 |
| **Unbuild — P03** | **12** | −192,085,001,254,677,504.00 |
| **Total** | **30** | **−194,756,704.00** |

**18 of 30 corrupt rows are manufacturing-origin, 12 of them unbuild** — the single largest
group.

> **`P03R-F-03`. `_cal_price` propagates a corrupt input into finished-goods value with no
> bound, no validation and no sanity check, and unbuild propagates it again.**
> Manufacturing did not originate the corruption; it is the **amplifier with the widest
> reach**. `FACT VERIFIED` for the mechanism; the trigger's ownership is **P01/Inventory**.

## 5. The cancellation that hides it

The 30 rows net to **−194.7 million** against a gross exposure near **10²¹**. They nearly
cancel.

> **This is the most dangerous property of the finding.** Any partial correction — reversing
> one unbuild, revaluing one product, deleting one entry — **breaks the cancellation** and
> releases an error of astronomical magnitude into the ledger. The position is not
> "wrong by 195 million"; it is "wrong by 10²¹ in both directions, currently almost
> cancelling".

Recorded as a **`Tolerance = 0`** boundary, `TZ-09`.

## 6. Ownership and routing

| Element | Owner |
|---|---|
| The trigger — vendor receipt / bill revaluation on an average-costed product | **P01** and the **Inventory** track |
| Average-cost compounding without bound | **Inventory** track |
| Subsidiary-ledger ↔ general-ledger divergence | **P08 / Core Accounting** |
| `_cal_price` amplification without validation | **P03 — this is ours** |
| Unbuild propagation | **P03 — `DC-13`** |
| Remediation sequencing given the cancellation | **Boss decision at final gate** |

**P03 claims only the two amplification rows.** The rest is routed with evidence attached
and no adjudication — `smeplus-session-execution-pattern`.

## 7. SMEsPlus requirement generated — `DESIGN CANDIDATE`

`R-17`: **a cost-injection path must validate the magnitude of its inputs and refuse to
capitalise a value it cannot justify.** A manufacturing order that consumes a component
valued at 1.6 × 10¹² per unit against a ten-month history of 30 must fail, not post.

Not authorised for implementation. `AASP-VETO-01` stands.
