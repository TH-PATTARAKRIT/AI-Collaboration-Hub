# 60 — HEADLINE / REGISTER RECONCILIATION CONTROL

**LAYER 2 — AUDIT QUARANTINE.** A control introduced because the same defect recurred
five times in three rounds.

---

## 1. The defect being controlled

A headline count stated in prose that does not reconcile with the register beneath it.
Every instance in this package:

| # | Round | Headline | Register | Cause | Caught by |
|---|---|---|---|---|---|
| 1 | 1 | `02` §2 "eleven … and eight" | 20 rows | 11 + 8 ≠ 20; one row unclassified | **self-challenge** (`C-07`) |
| 2 | 2 | `25` §2 "P04 counts nine" | P04's branch says 7 | cited a message, not the source | **round 4** (`RE-P03-11`) |
| 3 | 3 | `28` §3 "One is live" | table marked 3 more reachable | headline asserted from one member | **round 3 self-check** (`RE-P03-14`) |
| 4 | 3 | manifest totals | registers | asserted, not enumerated | **round 3** (`RE-P03-13`, near-miss) |
| 5 | **4** | `53` §2 "4 + … = 15" | 15 rows | `DC-14` counted twice; total asserted | **this control** (`RE-P03-17`) |

**Five instances. Four were arithmetic; one was a citation.** The searches behind them were
sound every time — this package's failure mode is not its evidence, it is the sentences
that summarise its evidence.

## 2. The control

Immediately before publication, for every material count:

1. Produce the **register total** by running a query over the register file.
2. Compare it to the **headline total** written in prose.
3. Record `REGISTER TOTAL · HEADLINE TOTAL · DELTA · CAUSE`.
4. A non-zero delta blocks publication of that sentence.

## 3. Execution this round

| Count | Register total | Headline total | Delta | Cause |
|---|---|---|---|---|
| `DC-*` defects | 15 (`grep … \| sort -u \| wc -l`) | 15 | **0** | — |
| Exposure classes | 15 across 7 classes | 15 | **0** | after `RE-P03-17` correction |
| Exposure class **IDs distinct** | 15 (`grep -oE 'DC-[0-9]+' \| sort -u \| wc -l` over §2) | 15 | **0** | verified explicitly |
| Databases | 4 found, 4 readable | 4 | **0** | — |
| Corrupt valuation rows | 30 | 30 | **0** | — |
| Attribution of the 30 | 4+8+2+4+12 = 30 | 30 | **0** | added, not asserted |
| Work centres, `iTEST02` | 60 | 60 | **0** | — |
| Work centres with no company | 0 of 60 | 0 | **0** | — |
| Custom addon roots | 3 roots, 1,325 `.py`, 378 control hits | same | **0** | 518+448+359 and 146+133+99 both re-added |

**One delta found and repaired before publication** (`53` §2). **Nine counts verified
clean.**

## 4. Why this control and not more review

`smeplus-totals-are-unverified-claims` records the mechanism: reviewing a *finding* does not
review the *arithmetic describing it*. Four of the five instances above survived adversarial
challenge rounds that were reading the same files — because challengers argue about whether
a finding is true, not about whether a total was added.

**The control is mechanical for that reason.** It is the only one of P03's controls that
does not depend on someone being suspicious.
