# P03 → P11 (CORE ACCOUNTING RECONCILIATION) — G01 CLOSURE HANDOFF

**LAYER 1 — CLEAN ROOM.**
**SUPPLEMENT to the prior P03 handoffs — NOT a replacement.** Prior handoffs stand.

---

## 1. What this closure changed

| # | Change |
|---|---|
| 1 | **P01 withdrew its routing of the valuation cost-explosion to P03 as owner.** The origin is inside the purchase path. **P03 had independently reached the same attribution from its own data.** Two processes, opposite directions, one answer |
| 2 | **P03's source basis did not match the deployment.** Four rounds of code reading were done in a **later generation** than the system carrying the manufacturing data. Corrected, bounded, disclosed |
| 3 | The one defect observed firing in production data — the dismantling path releasing goods at the wrong cost — is confirmed, and is **12 of the 30 corrupt records** |
| 4 | Manufacturing is **not a participant** in the purchase price-difference correction chain, in either generation available |

## 2. Decisions for P11

| # | Decision | Why it is P11's |
|---|---|---|
| `P11-D-4` | **Which ledger is authoritative** where the inventory subsidiary ledger and the general ledger disagree, and how divergence is detected | cross-process; neither P03 nor Inventory may set it |
| `P11-D-5` | **Remediation sequencing** for a corrupt position that currently **self-cancels** — any single-process fix releases the full gross exposure | above every individual process |
| `P11-D-6` | Whether a defect with **zero measured incidence** but a permitted mechanism can be closed | recurs for every latent defect in the programme; P03's scope item is one instance |
| `P11-D-1` | *(carried)* whether a scope narrowing for one object reads across to a related object — **P03's dissent preserved**: the two objects are unlinked in both directions | unchanged |
| `P11-D-2` | *(carried)* what closes a defect whose specified evidence returns an empty population | now **partly answered** — the population was found in a fourth database and returned **0 of 60** |

## 3. Named holds and their owners

| Hold | Owner | What closes it |
|---|---|---|
| Source matching the deployment's own generation | **environment / P01** | a source tree of that generation. **Nothing else** |
| Which deployment SMEsPlus must migrate | **Boss / programme** | a statement. Open since round 3 |
| The purchase-side origin mechanism | **P01** | P01 retains it; P03 inherited and **did not verify** it |
| Fixed-overhead absorption denominator | **Boss**, Asset register | unchanged; P03 evaluated no option |
| The subcontract bill-difference path in the older generation | **UNRESOLVED** | no deployment exercises it; P01 concurs |

## 4. What P03 asserts, and on what basis

| Claim | Basis | Survives the generation gap? |
|---|---|---|
| Conversion cost is zero in every examined deployment | measured in 4 databases | **YES** |
| 30 valuation records are corrupt; 25 diverge from the ledger; −48.7 % of inventory valuation | measured | **YES** |
| Manufacturing amplifies rather than originates — 18 of 30 records | measured | **YES** |
| No fixed-overhead cost is exercised anywhere | measured | **YES** |
| No manufacturing participant in the correction chain | read in 2 generations | **YES for those two** |
| The specific origin function and its defects | **inherited from P01, not verified by P03** | **attributed, not asserted** |
| The internal behaviour of the cost-injection functions | read one generation later than the deployment | **NO — bounded** |

> **The measured half of P03 is unaffected by the generation gap. The source half is bounded
> and says so.** P11 should rely on the first and treat the second as generation-specific.

## 5. What P03 does not conclude

- **Not** that the reference product's latent defects are harmless because they are latent.
  They are latent because the system is **unconfigured**, not because it is controlled.
- **Not** that SMEsPlus may omit labour, machine cost, depreciation or overhead because a
  deployment does. The accounting requirement is unaffected by what an operator configured.
- **Not** that material-only costing was an error rather than a policy. **No evidence of
  intent exists and none is inferred.**
- **Not** any statutory determination.

## 6. Status

Prior blockers closed: **none.** Gates closed: **none.** Nothing merged, frozen, approved or
authorised. **No mutation of any kind was performed.** The standing costing veto is unchanged
and remains strengthened.
