# P09_AFFECTED_FINDING_REDERIVATION_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room.

> **Only findings whose truth, denominator, scope, generation boundary, domain classification or I/P/O/Handoff role depends materially on the corrected population are re-derived here. Nothing else was re-researched.**

---

## 1. IMPACT MAP

| # | Corrected population item | Finding(s) affected | Old wording | New evidence | Disposition |
|---|---|---|---|---|---|
| **I-01** | a second planning family exists, **account-keyed** | *"a plan cannot be stated against a specific account — only a whole account **type**"* — routed forward as a retained interface fact | the second family's item carries a **required account reference**; a plan **is** stated per individual account | **`CONTRADICTED — CORRECTED`.** The claim is false inside the declared root and is **withdrawn**. It had already been routed to another domain as settled, so the withdrawal must travel with it |
| **I-02** | the same family carries **no analytic dimension at all** *(measured 0, with a working control)* | *"the intended amount is stated per dimension and window"* — Candidate Input `CI-05` | there are **two** kinds of intended amount: one dimensional with a window, one **dimensionless keyed to an account with a single date** | **`CONTRADICTED — CORRECTED`.** `CI-05` splits into `CI-05a` / `CI-05b` |
| **I-03** | its amount is a **plain float, no currency** | the currency findings, which addressed only the management record | a second intended-amount object carries **no currency at all** | **NEW FINDING — `FACT VERIFIED — P09`** |
| **I-04** | it has **no state, no revision lineage** | *"planning states are draft→confirmed→revised→done(→canceled)"* | that vocabulary describes **one** of the two families; the other has **no lifecycle whatsoever** | **`CONTRADICTED — CORRECTED`** — the state finding is **bounded to the first family**, not withdrawn |
| **I-05** | it is consumed as a **percent-comparison column via a temporary table** | the report-shadowing finding, previously stated for the analytic column | the **same structural mechanism** — a temporary table substituted into a report — carries the second planning family | **`SUPPORTED INTERPRETATION — P09`**, minimum interface fact only; the report engine was **not** researched |
| **I-06** | ownership is a property of the **file** | the domain-purity verdict `NOT DECIDABLE` | a P09 module holds adjacent-domain files **and** an adjacent-domain module holds a P09 file | **`CONTRADICTED — CORRECTED`** — see `P09_DOMAIN_PURITY_RECHECK` |
| **I-07** | two modules previously called P09-owned only **extend** | *"the P09-owned surface is four modules"* | **3 owning modules, 10 owning files**; the two are producers | **`CONTRADICTED — CORRECTED`** |
| **I-08** | the two over-plan computations on the commitment carrier sit in **P09-authored files on an adjacent-domain model** | `CP-06` / `CO-03`, already corrected to "three computations" | the **count stands**; the **classification** is now exact — P09 semantics, adjacent-domain carrier | **`FACT VERIFIED — P09`**, classification corrected |
| **I-09** | 16 files extend the P09 fact table | nothing previously stated this | P09 owns **one** file declaring its fact table; **sixteen** reshape it | **NEW FINDING — `FACT VERIFIED — P09`** |
| **I-10** | the previously withdrawn platform-wide event-identity premise | `CH-01` | already corrected to *"not found in the scope P09 has read"*; the corrected population **does not restore** the wider claim, and this round researched no adjacent domain | **UNCHANGED — the narrowed wording stands** |

---

## 2. WHAT WAS DELIBERATELY NOT RE-DERIVED

Per *No Material Delta = No Additional Research Round*:

| Untouched | Why |
|---|---|
| the zeroing theorem and its measured entry-level rate | arithmetic and deployed-data findings; the population correction does not reach them |
| the 19-artefact database census | a different evidence axis entirely |
| the composite correction finding (allocations mutable after close) | held from prior rounds; nothing in the corrected population bears on it |
| the six planning-concept absences | the corrected population **widens** the search surface, so the absences are **re-tested** below rather than assumed — see §3 |
| every adjacent-domain producer's internal lifecycle | domain purity |

---

## 3. THE ABSENCES, RE-TESTED — AND THE RESULT IS NOT THE ONE EXPECTED

The previous round's six absences were measured over four modules. The corrected population is 49 files across 28 modules, so the absences were re-run over it rather than inherited.

**Measured, unit = file, positive controls first:**

| Term | Files | Lines | Result |
|---|---|---|---|
| *(control)* the plan term | 9 | 130 | **the search fires** |
| *(control)* the dimension term | 46 | 341 | **the search fires** |
| forecast | **0** | 0 | not found |
| scenario | 0 | 0 | not found |
| simulation | 0 | 0 | not found |
| variance | 0 | 0 | not found |
| target | 2 | 2 | **inspected, not counted** — both are user-interface window attributes, not planning targets |
| baseline | 1 | 2 | **inspected, not counted** — both are a stylesheet class name |

### 3.1 The forecast zero is the finding

**We already know a forecast object exists in this root.** The previous round established it: a module named for the concept, carrying a stored intent/achieved/ratio triple joined to the management fact table.

**The corrected, model-based population returns zero for it.**

The reason is exact. That module contributes **one** file to the corrected population — the file that extends the management record. The file that actually declares the forecast object **extends no P09 model at all**, so the model-based instrument cannot reach it.

> **Two instruments, two different blind spots, the same false zero.**
> The name-based selector could not see the forecast module's *name pattern mismatch*. The model-based selector cannot see a file that carries planning semantics *without touching a P09 model*. Neither is complete. **Only the union of the two sees the object, and this round has run both.**

### 3.2 Consequence for every absence

| Concept | Disposition |
|---|---|
| **forecast** | **`CONTRADICTED — CORRECTED`.** The absence is **withdrawn**: an object exists, established by the union of the two instruments |
| scenario, simulation, variance, target, baseline | **`UNRESOLVED — SPECIFIC EVIDENCE REQUIRED`.** Each measures zero under **both** instruments — but the forecast case **proves blind spot B-2 is populated, not theoretical**, so a zero from either instrument is not a closed absence |

**`RD-01` — An absence measured by an instrument with a demonstrably populated blind spot is not a closed absence.** The five remaining zeros are recorded as unresolved for that reason and for no other. Restoring any of them to `FACT VERIFIED` would repeat the defect this round exists to correct.

---

## 4. THE PATTERN ACROSS THE IMPACT MAP

Ten affected findings. **Seven are corrections, two are new findings, one is unchanged.**

Every correction runs the same way: **a claim that was true of the population searched, stated as though true of the domain.** The negatives were honestly bounded and the boundaries were honestly declared — and the boundary was drawn by an instrument that could not see part of the domain it bounded.

**That is not the same defect as a false claim, and it should not be recorded as one.** It is a defect of *reach*, and the corrected population is the repair.
