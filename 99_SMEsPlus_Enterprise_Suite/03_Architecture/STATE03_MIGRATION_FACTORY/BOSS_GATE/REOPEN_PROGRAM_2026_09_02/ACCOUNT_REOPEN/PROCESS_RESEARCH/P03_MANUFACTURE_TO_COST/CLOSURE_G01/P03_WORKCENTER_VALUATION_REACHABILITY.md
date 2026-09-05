# P03 — WORK-CENTRE RATE / VALUATION-POLICY REACHABILITY

**LAYER 2 — AUDIT QUARANTINE.** `CQ-P03-07`. No new estate-wide census.

---

## 1. The claim under test

`P03R-F-09` (round 4): *work centres with rates and real-time valuation have never co-existed
in any examined deployment.*

## 2. Declared denominator

| Field | Value |
|---|---|
| **Population** | the **4** database dumps in P03's declared path set, all now readable |
| **Unit** | one database; within it, one work-centre row and one product-category valuation setting |
| **Selection rule** | every dump ≥1 MB found under the declared roots — no sampling |
| **Positive control** | the row-count parser returns 36 / 685 / 12 assets, 44 / 1 / 1 companies, 103,949 stock moves — it finds data where data exists |

## 3. The measurement

| Database | Work centres | Rated | Valuation mode | Valuation layers | GL lines | Conversion cost can post? |
|---|---|---|---|---|---|---|
| **`iSMEs`** | **0** | — | **real-time**, 15 categories; 18 FIFO + 8 average, **0 standard** | 74,982 | 447,384 | **NO — no work centres** |
| **`iTEST02`** | **60** | **1** | **periodic**; 3 explicit categories `standard`+`periodic`; **no valuation-layer table at all** | **none** | **32** | **NO — no valuation** |
| `BK12MAY26` | 0 | — | not measured | — | — | **NO** |
| `iEVING` | 0 | — | not measured | — | — | **NO** |

## 4. Which of the four candidate explanations is it?

| Candidate | Verdict |
|---|---|
| **Genuine absence** | **No** — the capability exists; 60 work centres and 154 routing operations are configured in `iTEST02` |
| **Configuration separation** | **YES — this is the answer.** The two preconditions are configured in **different databases**, neither of which has both |
| Evidence-population limitation | **Partly** — 4 databases is the whole declared population, but `iTEST02` holds **32 GL lines**: it is a *test system*, so its configuration is not evidence about production behaviour |
| Unreachable path | **No** — no code prevents coexistence |

> **`CQ-P03-07` answer: CONFIGURATION SEPARATION, in an evidence population of four, one of
> which is a test system.** The claim stands as measured and must always be read with its
> denominator, because "never co-existed in four databases, one of them a 32-line test
> system" is a materially weaker statement than "cannot co-exist".

## 5. Does any P03 mechanism depend on their coexistence?

**Yes — four of them, and this is why the question matters:**

| Mechanism | Requires |
|---|---|
| `M1` machine cost → FG | a rated work centre **and** FIFO/average valuation |
| `M2` labour relief entry | a rated work centre **and** real-time valuation |
| `DC-07` relief credits product COGS | `M2` firing — hence both |
| `DC-09` relief dated at posting | `M2` firing — hence both |

**All four are latent for exactly this reason**, and all four become live the moment one
administrator fills a rate field in a database that also has automated valuation. That is a
configuration step, not a code change.

## 6. Version bound

The *measurement* is version-independent — it reads the databases. The *gates* that make
coexistence necessary were read in **series 18** while `iSMEs` runs **series 16** (`MD-01`),
and `MD-02` shows the `_post_labour` gate **gained an extra clause** by series 19. The gate's
series-16 form is **not established**.

## 7. Disposition

> **`CQ-P03-07` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`.**
> Cause: **configuration separation**, denominator 4 databases, one a test system.
> Four P03 mechanisms depend on the coexistence and are latent solely because of it.
> The gate's series-16 form: **UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE** (`MD-01`).
