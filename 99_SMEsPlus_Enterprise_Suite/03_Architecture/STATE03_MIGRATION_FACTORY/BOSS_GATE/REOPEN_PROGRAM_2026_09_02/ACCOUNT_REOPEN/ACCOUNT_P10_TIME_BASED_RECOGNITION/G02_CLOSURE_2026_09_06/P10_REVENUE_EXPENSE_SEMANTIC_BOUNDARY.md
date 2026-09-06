# P10 — REVENUE vs EXPENSE SEMANTIC BOUNDARY  (`CQ-P10-04`)

**Terminal disposition: `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the mechanism · **`BOSS DECISION REQUIRED`** for the revenue-timing policy, which is Boss-reserved and consumed from P02.

---

## 1. What the Reference Actually Does

**Deferred revenue and deferred expense are one mechanism with a direction switch.** Same code path, same grid, same conventions, same defects. They are **not two domains and must not be counted as two engines.**

What differs is genuinely small:

| Axis | Revenue | Expense |
|---|---|---|
| Source document direction | customer invoice | vendor bill |
| Eligible account types | income, other income | expense, cost of sales, depreciation expense |
| Control account | deferred revenue (liability) | deferred expense / prepayment (asset) |
| Journal | separate | separate |
| **Generation method setting** | **independent** | **independent** |
| **Convention setting** | **independent** | **independent** |

## 2. The Asymmetry That Matters

The last two rows are the finding. **Twelve configuration combinations are reachable**, and nothing warns about, detects or prevents an asymmetric pair.

For a **resold service** — a purchased service and a sold service covering the *same window* — the two sides of the margin are then allocated by different rules onto different journal shapes. **The monthly margin becomes an artefact of configuration**, re-converging only at the end of the window.

**Measured in the deployed estate:** all 44 companies in each of the two multi-company databases hold **one identical configuration**. So the asymmetry is **reachable and not currently realised**. That mitigation is a **data state, not a control**, and it expires on the first divergence.

## 3. Do Not Force Symmetry — where the two genuinely differ

| Element | Shared? |
|---|---|
| Grid, convention, window semantics | **shared, and identically implemented** |
| Attribution construction | **shared, and identically defective** |
| Correction behaviour | **shared** |
| Control account **meaning** | **NOT shared** — a liability unwinding into income is not an asset unwinding into expense |
| Statutory presentation | **NOT shared** — routed to `P07`; P10 makes no statutory claim |
| **The event that triggers recognition** | **NOT shared** — see §4 |

## 4. The P02 Input — the boundary's real content

P02 hands P10 a measured fact and a Boss-reserved question:

> **CORRECTED — `G02-R-01`. P02 WITHDREW THIS FINDING AND P10 CONSUMED THE WITHDRAWN FORM.**
>
> ~~*Billing ahead of performance dominates. 789 invoiced-ahead versus 47 delivered-not-invoiced; 2,564 versus 253. 3,353 lines already billed ahead.*~~
>
> P02's correction banner `C-34`/`RE-29` records that those figures use a **draft-inclusive** counter. Re-measured on the **posted (accounting) basis**, delivered-not-invoiced is **1,145** against **792** billed-ahead — **1.4:1 toward DELIVERY**, the opposite direction. P02's own words: *"the sentence 'the dominant cut-off exposure is billing ahead of performance' is **WITHDRAWN** for Archive C."*
>
> **P02's three written handoff conditions, none of which P10 had carried (`G02-R-02`):** the figures carry the `C-34` draft-basis caveat and are **floors for 7 of 8 databases**; the direction is withdrawn; and **every population figure must be quoted by unit, never as a single number** — so "3,353" is itself a breach, summing two databases on two different bases.
>
> P02 further forbade acting on 792/2,564 before segmenting by product product invoicing policy (`P02-F-34e`, accepted and **not yet executed**), because for an order-policy product `invoiced > delivered` is the **designed** state, not an exposure.

And: **Boss Decision 3 — *revenue on billing versus performance* — is `OPEN — Boss reserved`.** P02 supplies measurement only. P02's unresolved dependency 5 names the owner as **`Boss / P10`**.

**P10's position, which is a measurement and not a decision:**

1. **The reference's deferral mechanism is a *billing-triggered* mechanism.** It starts from an invoiced amount and spreads it. It has no concept of performance, delivery or satisfaction of an obligation. Recognition begins because something was **billed**, not because something was **delivered**.
2. **Therefore, if the Boss rules recognition on performance, the reference mechanism does not implement it** — not as a configuration, not as a setting. It would be a build requirement, exactly as P02 found for its own cost trigger.
3. **A cut-off population exists on both sides and its direction is unsettled** — `G02-R-01`. On the accounting basis the larger Archive C exposure is **delivered-not-invoiced (1,145)**, which makes **`IN-P02-3` (deliver-never-invoice)** the stronger driver, not billing-ahead. What P10 measured itself is unaffected: in **6 of 6** distinct deployed databases the deferral mechanism has **never generated an entry**, so nothing spreads any line over time. **Recognition follows billing in practice; the configured deferral policy is present, unexercised and unenforced** — re-worded from *"by omission"*, `G02-R-01`, because "omission" imputes an absence of decision that P10 has not measured and that is Boss-reserved (`BP-03`, `OPEN`).

> **`P10-F-G02-01` — the deployed estate recognises revenue on billing by omission, not by policy.** The mechanism that would spread it is installed, configured in 43 of 44 companies, and has produced **zero entries**. `FACT VERIFIED` within the four databases.

**This is P10's answer to P02's first question, and it is a measurement, not a ruling.** The ruling is Boss-reserved.

## 5. P02's Other Three Questions

| P02 question | P10's disposition |
|---|---|
| **Bill-and-hold in scope? Trigger?** | **`BOSS DECISION REQUIRED`.** P10 records only that a bill-and-hold obligation is a *performance* concept and the reference recognition mechanism has no performance input, so it cannot express one. Routed back to Boss with P02's framing preserved |
| **Must P10's model tolerate a deployment that delivers and never invoices?** | **`FACT-SUPPORTED FUNCTIONAL REQUIREMENT`: yes.** A recognition model keyed solely on billing cannot represent 1,201 delivered-not-invoiced lines with 0 ever matched. **A performance-triggered path must at minimum be representable, whatever the Boss rules for the default** |
| **Is the obligation position P10-owned or P02-owned?** | **`DESIGN CANDIDATE`, recommendation only.** P10's position: the **measurement** of the obligation is P02's — it derives from order and delivery state P10 does not own; the **recognition consequence** is P10's. Split at the measurement/consequence line. Routed to P11 as an ownership question, not settled by P10 |

## 6. Disposition

- Mechanism symmetry and the twelve-combination asymmetry: **`FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`**
- Revenue on billing versus performance: **`BOSS DECISION REQUIRED`** — preserved from P02, not re-decided
- Bill-and-hold: **`BOSS DECISION REQUIRED`**
- Tolerating deliver-never-invoice: **`FACT VERIFIED`** as a requirement on the model
- Obligation-position ownership: **`CROSS-PROCESS OWNER — HANDOFF PUBLISHED`** (P11)
