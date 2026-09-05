# 29 — P03 DC-14 ANALYTIC DUPLICATION FORENSIC

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Authoritative definition

`DC-14`, from `25` §3: `project_mrp_account/models/mrp_workorder.py:9-14` overrides
`_create_or_update_analytic_entry_for_record(value, hours)`, calls `super()` — which
distributes the value over the **work centre's** distribution — then distributes the
**identical `value` and `hours`** over the **project's** distribution.

## 2. The five separations the directive requires

Counted, not asserted.

| Quantity | Count | Evidence |
|---|---|---|
| **Function calls** | **2** | `super()._create_or_update_analytic_entry_for_record(...)` then `_perform_analytic_distribution(project…)` |
| **Calculated monetary values** | **1** | `value` and `hours` are the *same variables* passed to both; computed once in `mrp_account/models/mrp_workorder.py:45-47` |
| **Analytic line sets** | **2** | `wc_analytic_account_line_ids` and `mo_analytic_account_line_ids` — separate many2many relations, separate physical tables |
| **Economic cost facts** | **1** | one work-order hour, one rate, one amount |
| **WIP / financial cost injections** | **0** | analytic lines are a separate ledger; no path from `account.analytic.line` to inventory carrying value exists |

## 3. Testing the five hypotheses

| | Hypothesis | Result |
|---|---|---|
| **A** | Second call creates duplicate **records** only | **TRUE, always** — two line sets from one value |
| **B** | Second call creates a second **management attribution** | **TRUE where the two distributions resolve to a common analytic account.** Where they resolve to different accounts it is one cost attributed to two dimensions, which is the legitimate purpose of a second plan |
| **C** | Second call creates a second **WIP / financial** cost | **FALSE.** No analytic-to-GL path exists. `FACT VERIFIED` |
| **D** | Result depends on **configuration** | **TRUE** — on whether the work-centre and project distributions name the same account, and on whether analytic plans collide |
| **E** | Result is **unreachable in deployed runtime** | **TRUE for every readable deployment — see §4** |

## 4. Deployment reachability — executed

`project_mrp_account` is the **only** module that contains the override.

| Database | `project_mrp_account` | Work orders | Verdict |
|---|---|---|---|
| `iSMEs` | **NOT INSTALLED** | 0 | unreachable, twice over |
| `BK12MAY26` | **NOT INSTALLED** | 0 | unreachable, twice over |
| `iEVING` | not installed (mrp data absent) | 0 | unreachable |
| `iTEST02` | **UNKNOWN — dump unreadable** | unknown | `UNR-P03-07` |

Evidence: `evidence/P03T_EXECUTED_OUTPUT.txt`.

## 5. Disposition

> **`DC-14` — MULTIPLE ATTRIBUTIONS — ECONOMIC EFFECT DEPENDENT.**
>
> One economic cost fact. One computed value. Two analytic line sets. **Zero financial or
> WIP injections.** The management effect doubles only where both distributions resolve to
> a common analytic account. Unreachable in every readable deployment because the module
> that contains it is not installed.

**Severity revised down from High to Medium**, and the reason is stated so the change is
auditable: `25` §3 rated it High on the mechanism alone, before deployment evidence
existed. The mechanism is unchanged and still verified; its reach is now measured.

## 6. P03 withdraws part of its dissent against P04

`25` §3 said *"P03 rates this higher than P04 does"*, against P04's assessment that M5 is
the weakest of its paths.

**That framing conflated two different questions, and P03 was wrong on one of them:**

| Question | P04 | P03 now |
|---|---|---|
| Is M5 a distinct **path** under P04's declared unit (own rate **or** driver **or** destination ledger)? | **No** — it satisfies none of the three disjuncts | **P04 is correct.** P03 should not have implied otherwise |
| Does the analytic **ledger** carry the cost twice? | **Yes** — P04-F-45, `FACT VERIFIED` (mechanism), incidence a data question | **Agreed — the two sessions never actually disagreed here** |

The apparent disagreement was P03 answering a denominator question with a ledger answer.
**P03 withdraws the "rates it higher" framing** and retains only the ledger finding, which
was never in dispute. Recorded as `RE-P03-12`.
