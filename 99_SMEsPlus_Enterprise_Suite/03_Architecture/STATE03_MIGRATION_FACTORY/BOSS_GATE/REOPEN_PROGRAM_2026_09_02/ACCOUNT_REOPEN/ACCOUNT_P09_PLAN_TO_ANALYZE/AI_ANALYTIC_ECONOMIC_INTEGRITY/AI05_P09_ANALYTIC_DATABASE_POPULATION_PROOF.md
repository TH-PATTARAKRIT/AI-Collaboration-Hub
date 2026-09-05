# AI05 — P09_ANALYTIC_DATABASE_POPULATION_PROOF

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

**No denominator is invented in this document.** Where the data cannot answer a question, the answer is `NOT DECIDABLE FROM AVAILABLE DATA` with the reason.

---

## 1. WHAT WAS SEARCHED

A full-volume sweep for database dumps, exports and runtime traces, plus the five candidate artefacts named by prior sessions. Nine artefacts were located and inspected read-only. **Two are real PostgreSQL dumps** — a materially better evidence position than the base package had, which used no deployed data at all.

| # | Artefact | What it is | Usable for this question? |
|---|---|---|---|
| 1 | asset runtime trace, one deployment | live capture of **280** asset-master records | partly — see §2 |
| 2 | the capture script for artefact 1 | proves which fields were requested | decisive, negatively — see §2 |
| 3 | asset import/export workbook | **asset category templates**, 16 rows, no monetary values | no |
| 4 | asset mapping handoff document | a procedural plan, not a data export | no |
| 5 | a management report for an unrelated deployment | prose | no |
| 6 | **PostgreSQL custom-format dump, deployment A** | real database | **yes** |
| 7 | **plain-text PostgreSQL dump, deployment B** | real database | **yes** |
| 8 | an unrelated schema script from a different technology stack | — | no |
| 9 | this continuation's own trace document | source-code proof, symbolic example | no — and correctly asserts no denominator |

## 2. THE COUNTS THAT ARE GENUINELY DERIVABLE

| Question | Answer | Reason |
|---|---|---|
| assets carrying an allocation, deployments A and B | **0 of 12, and 0 of 12** | the allocation column exists and is null on every row in both dumps |
| asset rows in those dumps | 12 and 12, **all of them category templates** with zero monetary values | not posted assets |
| depreciation journal rows in deployment A | **0** on the depreciation journal the asset rows themselves reference; 23 journal rows exist in total, none on that journal | — |
| journal rows of any kind in deployment B | **0** | the table is empty |
| management records in deployment A | **2**, neither carrying a general account, neither depreciation-linked | — |
| management records in deployment B | **0** | table empty |
| assets in the traced deployment | **280** (217 open, 35 draft, 27 closed, 1 paused) | asset-master count only |
| whether those 280 carry an allocation | **NOT DECIDABLE FROM AVAILABLE DATA** | the capture script never requested the field — verified by reading the script |
| symmetric pairs anywhere | **NOT DECIDABLE FROM AVAILABLE DATA** | requires paired journal rows carrying an allocation; no such rows exist in any artefact |
| net-zero analytic effects anywhere | **NOT DECIDABLE FROM AVAILABLE DATA** | same reason |

## 3. THE FINDING THIS PRODUCES — AND IT IS NOT THE ONE EXPECTED

**In every deployment for which real data was located, no asset carries an analytic allocation at all.**

That is class **A within the stated scope** — the column was searched by exact name across both dumps, and is null on all 24 asset rows.

The consequence is precise and it changes which branch of the mechanism matters:

- The zeroing branch (`E19`) requires the asset to **carry** an allocation. **It has not been observed to fire anywhere in the searched scope.**
- The branch that actually applies to the observed data is the **no-allocation** branch (`E20`): the key is omitted and each row derives its own from the rule set.
- Where **no rule matches either account** — the ordinary state of a deployment with no allocation rules configured — **neither row produces a management record at all**. Depreciation is then attributed **nowhere**: not correctly, not incorrectly, not to zero. It is simply absent from management accounting.

**This is a third state, and the base package did not carry it.** It is added as `E22`.

## 4. WHAT THIS DOES AND DOES NOT DO TO THE CENTRAL HYPOTHESIS

| It does **not** | It does |
|---|---|
| weaken the algebra — a proof does not need a witness | bound the *observed* incidence to zero in the searched scope |
| make the defect hypothetical — it is unconditional whenever the precondition holds | show that the precondition (an asset with an allocation) is **not present** in any deployment for which data was found |
| justify downgrading the finding | justify stating, honestly, that **no instance has been observed** |

**The correct reading:** the mechanism is proven and will fire the moment any deployment starts allocating assets to cost centres — which is exactly what an organisation does when it begins cost-centre reporting. The defect is **latent in the observed deployments and armed**.

## 5. CLASSIFICATION

**PARTIAL DATABASE EVIDENCE.** What is missing, named precisely: populated depreciation journal rows carrying an allocation, and the management records they would produce. Neither exists in any artefact located.

For the population question specifically: **`HOLD — DATABASE EVIDENCE REQUIRED`**. To close it, one of:
1. a dump from a deployment where assets carry allocations; or
2. a re-run of the asset trace with the allocation field included — a **read-only** capture, well within what the existing script does, and the cheapest way to close it; or
3. read-only query access to a deployment with posted depreciation.

Routed as `DEP-P09-14`.

## 6. PROCESS NOTE

One trace artefact begins with a bare marker line not explained by its own capture script. It carries **no directive text of any kind** — the file is three lines and was read in full. It was not acted on. Recorded here only so that the register is complete; no escalation was required and none is implied.

## 7. CHECKPOINT

**CP-AI05 — DATABASE POPULATION QUANTIFIED, TO THE EXTENT THE DATA PERMITS.** Observed incidence of the precondition: **zero**. Mechanism unaffected. Auto-continue.
