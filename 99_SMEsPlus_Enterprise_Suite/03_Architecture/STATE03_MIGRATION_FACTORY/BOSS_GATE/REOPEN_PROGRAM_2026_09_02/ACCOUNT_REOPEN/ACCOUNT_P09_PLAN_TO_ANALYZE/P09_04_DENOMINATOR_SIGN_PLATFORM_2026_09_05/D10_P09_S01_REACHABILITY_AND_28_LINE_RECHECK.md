# D10 — P09_S01_DEPLOYMENT_REACHABILITY and P09_28_LINE_COMPLETENESS_RECHECK

**Checkpoints:** `CP-P09D09`, `CP-P09D10` · **Layer:** 1 — clean-room.

---

## 1. THE TEMPLATE — EVERY ROW CLASSIFIED, NO SAMPLING

**27 data rows** (28 lines including the header — my earlier "28-line file" conflated the two; a unit error in miniature).

Convention derived from the file's own majority: 1 = asset, 2 = liability, 3 = equity, 4 = income, 5–8 = expense.

| Line | Code | Type declared | Expected group | Violation |
|---|---|---|---|---|
| 4 | 1201 | liability | **asset** | **YES** — the account is named as an outstanding-cheque item |
| 6 | 1411 | depreciation-**expense** | **asset** | **YES** — named as accumulated depreciation |
| 7 | 1421 | depreciation-**expense** | **asset** | **YES** — named as accumulated depreciation |
| all other 24 rows | — | — | — | conform |

> **3 violations in 27 data rows, not 2.** The prior round found the second and stopped; a complete classification finds a third. **Two consecutive rounds under-counted the same 27-row file** — the first said one, the second said two, the complete pass says three.

## 2. THE DEPLOYED CHART — REACHABILITY MEASURED

Exhaustive over all **339** deployed accounts, same convention, stated explicitly.

**9 code-block/type contradictions**, reproducing the reported figure exactly:

| Code | Type | Name | Assessment |
|---|---|---|---|
| 1153002 | income | accrued income | asset code, income type |
| 1201000 | liability | outstanding cheques | **the deployed twin of template line 4** |
| 2100000 / 2120000 / 2130000 / 2140000 | equity | capital, retained earnings, dividends, income summary | **convention-dependent** — see §3 |
| **7180001** | **fixed asset** | a major-expense job account | **THE MATERIAL ONE** — expense code block, expense name, **balance-sheet type** |
| 7210001 / 7210003 | income | currency gains | expense code block, income type — arguably correct in substance |

## 3. HONEST QUALIFICATION OF THE "NINE"

**4 of the 9 are equity accounts in the 2-block, and that is a convention I chose, not one the chart declares.** Many charts place equity in the 2 or 3 block legitimately. Under a convention where 2 = liability *and* equity, those 4 are not violations.

> **Defensible count: 5 contradictions, of which 1 is materially consequential.** Reporting "9" without this qualification would repeat the very defect this round exists to fix — a count whose rule was chosen by the author of the claim it bounds.

## 4. THE MATERIAL FINDING — `7180001`

An account whose **code block and name both assert expense**, typed as a **balance-sheet fixed asset**.

**Consequence under Gate A** — the gate three of four builds carry: its type resolves to `asset`, so it is **silently excluded** from budget consumption. **A cost account's spend never reaches any budget.**

> **This is `TH-F-01`'s defect class, present in the deployment, in the opposite direction.** `S01` §5's *"the contradiction is internal to the template and does not reach this deployment"* is **CONTRADICTED**, and the correction stands.

**P09 does not classify its cause.** Configuration error, localisation error, template error, build error or deliberate — **`UNRESOLVED — EVIDENCE REQUIRED`**, routed to **P08** (account-type semantics) and **P07** (any statutory reading). **P09 makes no statutory claim.**

## CHECKPOINT
**`CP-P09D09`, `CP-P09D10` — COMPLETE — EVIDENCE VERIFIED.** Template violations 3 of 27; deployed contradictions 5 defensible / 9 under a stated convention; 1 materially consequential. Auto-continue.
