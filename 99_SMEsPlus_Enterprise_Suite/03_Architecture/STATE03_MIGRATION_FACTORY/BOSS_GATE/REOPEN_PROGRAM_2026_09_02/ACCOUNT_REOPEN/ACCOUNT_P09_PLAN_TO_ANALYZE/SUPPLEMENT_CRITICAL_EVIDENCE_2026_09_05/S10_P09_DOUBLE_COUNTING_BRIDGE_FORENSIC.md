# S10 — P09_DOUBLE_COUNTING_BRIDGE_FORENSIC

**Checkpoint:** `CP-P09S10` · **Layer:** 1 — clean-room.
**The previously-named pair is NOT retained.** It was contradicted last round and is replaced here.

---

## 1. VERDICT ON THE CORRECTED PATH

**`CONFIRMED WITH CAVEAT` — source-only, with zero deployed corroboration.** An independent challenge attacked it on six fronts; the mechanism survived every one.

## 2. THE MECHANISM

One work-order duration change:

1. the base module creates a **work-centre** management record — value = negative hours × the work centre's hourly rate — against the **work centre's own** allocation;
2. a **bridge module** then calls the base and creates a **second** record with the **same value and the same hours** against the **project's** allocation;
3. the two records live in **different relation sets**, so **neither deduplication path can see the other** — the only cross-set operations are cancel and delete;
4. the profitability section selects on axis value **and** event category, grouped by currency, **with no discriminator on source** — no journal link test, no field-set test. Both records are even labelled identically, and both carry the same category.

**Where the work centre's allocation names the project's own axis value, the same machine cost is attributed twice and summed into one reported figure.**

## 3. THE CAVEATS — BOTH NARROW THE CLAIM

| # | Caveat |
|---|---|
| **C1** | **the value limb is conditional.** The project side is **always** 100 %; the work-centre side carries its configured share. Full duplication requires a 100 % work-centre allocation. The prior wording "same value" was an overstatement |
| **C2** | **the hours limb is unconditional and stronger than claimed.** Quantity is deliberately **not** distributed — both records carry the **full** hours regardless of percentages. Any hours-based costing or capacity report double-counts unconditionally |

## 4. TWO CORRECTIONS TO MY OWN CITATIONS

- **a misattributed location.** The module I cited as the employee-rate variant only declares a field and renames a line; the employee rate is computed in a **different** module. Corrected.
- **an incomplete causal statement.** I wrote that the section sums both *"because both carry the same category"*. Category alone is **not** sufficient — both the category **and** the axis-value test must be satisfied. Stating only the first invites a reader to mistake the second for an undiscovered discriminator.

## 5. HOW MANY RECORDS ONE DURATION CHANGE PRODUCES

| Stack | Records |
|---|---|
| base + project bridge | **2** — both at the work-centre rate. **These two are the duplicate** |
| full stack, adding the employee modules | **3** — the third uses a **different** rate against the same project allocation |

**Only 2 of the 3 are a duplicate.** The third is the complementary machine-plus-labour pair, which the prior round's contradiction correctly established is **not** a double count.

## 6. THE VENDOR'S OWN TESTS CUT BOTH WAYS — AND THE SECOND ONE IS DECISIVE

- a test named for the same-axis-value case carries a docstring asserting **no duplicated lines are posted** — and its body **sets the two to different axis values**, so **the case its own name describes is never exercised**;
- an enterprise profitability test asserts the machine cost appears **exactly once**, and passes only because its work centre carries **no allocation**. Give that work centre the project's axis value and the same assertion changes.

**The reference's own stated expectation is that the machine cost appears once. The corrected path identifies a reachable configuration in which it appears twice.**

## 7. DEPLOYED EVIDENCE — NONE, AND THAT IS THE FINDING

| Check | Result |
|---|---|
| management records carrying the manufacturing category | **0 of 339,382** — confirmed in two independent forms, with a positive control |
| work-order records | **0** |
| the two bridge relation tables | **absent from the archive entirely** |
| the bridge module | **not present in the module registry at all** — not merely uninstalled |
| the other three deployments | manufacturing category **0** in each |

**The mechanism has never run in any deployment in the population.**

And a **second version-basis instance**: the deployed manufacturing module stores those links as **single** relational columns, where the source I read uses **paired multi-value** relations. **The deployed code is a different version with a different data shape** — so even a future attempt to evidence this from that database would be testing a different implementation.

## 8. FINAL CLASSIFICATION

> **`CONFIRMED — SOURCE-ONLY, CONFIGURATION-GATED, UNEXERCISED IN EVERY DEPLOYMENT MEASURED, AND READ FROM A VERSION NO DEPLOYMENT RUNS.`**

The duplicate is a **duplicate management attribution**, not a duplicate financial cost — the ledger is untouched — and it reaches **budget consumption** and the **axis value's own balance**, not only the profitability section.

## CHECKPOINT

**`CP-P09S10` — COMPLETE — EVIDENCE VERIFIED.** Corrected path confirmed with two narrowing caveats and two of my own citations corrected. Auto-continue.
