# 54 — LIVE ZEROING ROOT CAUSE

**LAYER 2 — AUDIT QUARANTINE.** §10 of the directive: *prove or disprove* that the
principal live defect is zeroing.

---

## 1. Verdict

> **PARTLY DISPROVED. Zeroing is the principal live defect in `iSMEs` and is NOT the
> principal live defect overall.**

Round 3 concluded *"the principal live defect is zeroing"* from three databases. With the
fourth open, the picture is two-sided:

| Database | Principal live defect |
|---|---|
| `iSMEs` | **ZEROING** — conversion cost structurally absent, plus `P03R-F-02`'s 49 unvalued and 280 zero-valued finished moves |
| `iSMEs` | **and EXPLOSION** — 30 valuation rows to ±10²¹, `55` |
| `iTEST02` | **ZEROING TOO, by a different gate** — periodic valuation, no valuation layers, 32 GL lines. `DC-07`'s configuration is fully met (60 of 60 work centres lack an expense account) but the relief never posts |

**Two opposite failures coexist in `iSMEs`** — conversion cost zeroed, material value
exploded. A package reporting only zeroing would have been half right.

And zeroing turns out to be **universal across the examined deployments**, reached by two
different routes: absent work centres in one database, absent valuation in the other
(`P03R-F-09`).

## 2. Where the cost disappears — traced, mechanism by mechanism

The directive lists six candidate mechanisms. Each tested:

| Candidate | Result |
|---|---|
| **Analytic netting** | **NOT the cause of P03 zeroing.** Real (`33`), and P09/P04-owned, but it zeroes a *management* number. `iSMEs` has 27 analytic accounts and 0 work-centre distributions, so it never fires on manufacturing at all |
| **Line eligibility** | Not applicable — no analytic lines are produced |
| **Bridge behaviour** | **YES, in `iSMEs`** — `mrp_workorder` and its HR bridge are **not installed**, so `_cal_cost`'s employee half does not exist and no time log can be created |
| **Missing WIP injection** | **YES** — `mrp_accountant` absent, so the WIP wizard cannot run |
| **Wrong cost owner** | **YES, in `iTEST02`** — the relief credit lands on product COGS, not on the expense that was incurred (`DC-07`) |
| **No conversion-cost transaction** | **YES, the dominant one in `iSMEs`** — 0 work centres, 0 routing operations, 0 work orders, 0 time logs |

## 3. The root cause, stated precisely

> **`P03R-F-05`. Conversion cost does not disappear from a ledger in `iSMEs` — it is never
> created.** There is no lossy step to find. `_cal_price` computes
> `−Σ(consumed layers) + work_centre_cost + extra_cost` with the second and third terms
> structurally zero, and `_post_labour` exits at its zero-amount guard on every order.
> The arithmetic is correct; its inputs do not exist.

This distinguishes P03's zeroing from P09's:

| | P09 zeroing | P03 zeroing |
|---|---|---|
| Mechanism | records **created**, amounts **cancel** | records **never created** |
| Gross movement | 2X | **0** |
| Net | 0 | **0** |
| Detectable in the ledger? | yes, at line level | **no — there is nothing to detect** |
| Owner | **P09** | **P03** |

**Same net, different mechanism.** `65` reconciles them.

## 4. The second, larger loss

`P03R-F-02`: 49 of 13,284 completed finished-goods moves carry **no valuation record**, and
280 more are valued at **zero**; 1,386 of 30,067 component consumptions are unvalued.

> Round 3 reported *"material cost present"* as measured. **It was inferred.** The measured
> answer is that material cost reaches most, not all, of the population. `FACT VERIFIED`.

Whether the 49 are a manufacturing defect or an inventory-valuation one is **not
established** — the finished move belongs to P03, the valuation layer to Inventory.
`UNR-P03-15`, routed to the Inventory track with the evidence attached.

## 5. What P03 does not claim

- **Not** that the operators were wrong to run material-only costing. That is a policy
  question with a legitimate answer, and `52` §3 statement 4 explicitly refuses to infer
  intent.
- **Not** that TAS 2 is breached. The standard says conversion cost belongs in inventory;
  whether this population's facts breach it is a **statutory determination** routed to the
  Accounting-Tax track, unchanged from `34` §5.
- **Not** that SMEsPlus may omit conversion cost because the reference deployment does.
  §25 of the directive forbids exactly that inference, and `71` §5 records it as a design
  boundary.
