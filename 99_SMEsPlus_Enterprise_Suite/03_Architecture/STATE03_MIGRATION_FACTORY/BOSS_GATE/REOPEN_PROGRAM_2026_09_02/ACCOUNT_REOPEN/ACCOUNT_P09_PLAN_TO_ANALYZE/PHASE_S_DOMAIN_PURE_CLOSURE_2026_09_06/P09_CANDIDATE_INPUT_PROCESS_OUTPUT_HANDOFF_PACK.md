# P09_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room.

> **THIS IS A CANDIDATE PACK. IT IS NOT A CONTRACT.**
> No item here is a final cross-domain Input/Output Contract. Contracts are formed after PHASE SA, by Boss decision, not by P09.

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements in this file were **contradicted by the AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are marked inline; superseded wording is retained. The full list is in `P09_AAS03_INDEPENDENT_CHALLENGE_RECORD`.

---

## 1. THE ONE-PARAGRAPH POSITION

P09 consumes **costed facts that someone else authored**, attaches **management meaning** to them along declared axes, compares them against **an intended amount**, and emits **management judgement**. Every one of those four verbs is evidenced. Only the second and third are P09-owned. The first is owned by adjacent domains and the fourth terminates with management. **P09's own boundary is therefore narrower than the analytic machinery it studies** — much of that machinery is other domains writing into P09's dimension, which is exactly why domain purity had to be enforced rather than assumed.

---

## 2. CANDIDATE INPUT

> `CANDIDATE INPUT` — required meaning stated; **producer internals deliberately not researched.**

| # | Candidate Input | Required business meaning | Producer candidate | Scope | Period / date meaning | Identity requirement | Uncertainty |
|---|---|---|---|---|---|---|---|
| **CI-01** | **a costed fact with a financial effect** | an amount that a legal entity has actually incurred or earned, already posted | `EXTERNAL DOMAIN BOUNDARY` — the posting domains | COMPANY | the **accounting date** of the posting | needs a stable **financial-event identity** — *which does not exist* | **UNRESOLVED.** The identity P09 needs has never existed; inherited gap, not a P09 defect |
| **CI-02** | **a costed fact with no financial effect** | an operational measurement carrying a cost (labour time, machine time, estimated valuation) | `EXTERNAL DOMAIN BOUNDARY` — operational domains | COMPANY for the amount; TENANT for the resource | the **operational event date** | must be distinguishable from CI-01 **by class, not by inspection** | P09 requires a provenance class that the reference pattern does not carry |
| **CI-03** | **the dimension structure** — axes and their values. **FLAGGED: this row is two inputs.** The axis and the value have different scope carriers, different determinations and different context requirements; the Uncertainty cell is true only of the axis half. Splitting them into `CI-03a` / `CI-03b` is required, and **the input count of six is therefore a floor** | the tenant's declared way of analysing its own management result | **P09-OWNED** | TENANT (axis), TENANT or COMPANY (value) | effective-dated; history must survive change | tenant-unique, immutable identity | axis is materialised as physical schema, so it is *not* tenant data today |
| **CI-04** | **the allocation instruction** | how much of a costed fact belongs to which dimension value | **P09-OWNED as a rule**; applied by producers | TENANT (rule), COMPANY (application) | the date of the fact it applies to | must carry referential integrity | today a schemaless payload with no foreign key |
| **CI-05** | **the intended amount** (the plan) | what the organisation intends to spend or earn, per dimension and window | **P09-OWNED** | TENANT or COMPANY, **declared per plan** | a free-form window — **no fiscal-period object** | plan identity + revision lineage | window is not bound to a fiscal calendar |
| **CI-06** | **the commitment** | value committed but not yet incurred | `EXTERNAL DOMAIN BOUNDARY` — the commitment-raising domain | COMPANY | the **order date** — a third time basis | must be reconcilable to CI-01 when it converts | **the carrier is generation-specific.** In one generation the plan line carries it; in the other the field does not exist and the report emits a hardcoded zero, deferring to an optional module. **A zero is therefore ambiguous between *nothing committed* and *module absent*** (EV-P09-207). The conversion point is not evidenced as an event in either |

**The input-side finding:** of six candidate inputs, **three are authored outside P09** (CI-01, CI-02, CI-06) and P09 can state only what they must *mean*. Two of those three arrive on **different time bases** from each other and from the plan window (CI-05). That is not a defect P09 can fix inside its own boundary.

---

## 3. CANDIDATE PROCESS SEMANTIC

> `CANDIDATE PROCESS SEMANTIC` — what P09 itself does.

| # | Process semantic | Evidenced behaviour | Class |
|---|---|---|---|
| **CP-01** | **dimensional attribution** — bind a costed fact to dimension values | by assignment alone; no account-type, row-type, context or company test on the creation path | `FACT VERIFIED — P09` |
| **CP-02** | **allocation arithmetic** — split a fact across values by percentage | the management amount is the **negated** row balance × share; percentages need not total 100 unless a mandatory axis and an opted-in caller coincide | `FACT VERIFIED — P09` |
| **CP-03** | **aggregation** — sum management records per dimension | computed at read time; converted at **today's** rate into the **reading user's** company currency | `FACT VERIFIED — P09` |
| **CP-04** | **plan-versus-actual comparison** | **three** figures on three time bases in one generation, **two** in the other; **none stored**, recomputed on every read | `FACT VERIFIED — P09`, generation-bounded (EV-P09-207) |
| **CP-05** | **consumption ratio** | achieved / theoretical, each as an amount and a percentage of plan; **committed only where that generation carries it**, otherwise a hardcoded zero | `FACT VERIFIED — P09`, generation-bounded |
| **CP-06** | **over-plan signalling** | ~~a displayed boolean that gates nothing~~ → **THREE distinct computations, not one**: one on the plan line, and two on purchase-domain models, of which one is a **prospective commitment-time** test (`committed + uncommitted > plan`). **CORRECTED** (EV-P09-208 §9.5) | `CONTRADICTED — CORRECTED` |
| **CP-07** | **revision** — supersede a plan by a successor | parent/child link; confirming the successor flips the predecessor to a revised state | `FACT VERIFIED — P09` |
| **CP-08** | **variance quantification** | **DOES NOT EXIST** — established in three independent forms | `FACT VERIFIED — P09` (absence, class B, boundary declared) |
| **CP-09** | **forecasting, scenario modelling, target setting, baselining, simulation** | **NOT FOUND IN SCOPE** — zero declarations for all five | `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED` outside the bounded set |

---

## 4. CANDIDATE OUTPUT

| # | Candidate Output | Business meaning | Consumer | Scope | Period meaning | Correction semantics | Lineage |
|---|---|---|---|---|---|---|---|
| **CO-01** | **management attribution** — cost/revenue by dimension value | who is accountable for this amount | `TERMINAL MANAGEMENT OUTPUT` | COMPANY record, TENANT aggregate | the record's own date | today: silently mutable after period close | EV-P09-100..103 |
| **CO-02** | **plan consumption** — achieved / theoretical (and committed where carried) vs plan | how much of the intention is used up | `TERMINAL MANAGEMENT OUTPUT` | per plan's declared scope | two or three time bases, by generation | recomputed, therefore retrospectively changing | EV-P09-062..064 |
| **CO-03** | **over-plan signal** | an advisory flag | `TERMINAL MANAGEMENT OUTPUT` | ~~per plan~~ → **per plan AND per purchase order** — scope corrected | window | none | EV-P09-065, EV-P09-208 §9.5 |
| **CO-04** | **management figures presented on a financial surface** | an analytic column inside a financial report | **`CANDIDATE HANDOFF` — and a contested one** | COMPANY | as presented | none | EV-P09-050..053 |
| **CO-05** | **allocation converted into postings** | a reallocation that reaches the ledger | **`CANDIDATE HANDOFF`** | COMPANY | posting date | reversal not evidenced | EV-P09-040..049 |

**The output-side finding:** three of five outputs are **terminal** — they end with management and cross no boundary. Only **CO-04 and CO-05 leave P09**, and both are the mechanisms P09 has already recorded as boundary violations. **P09's clean outputs do not cross into finance; the two that do are the two it recommends against.**

---

## 5. CANDIDATE HANDOFF

| # | Handoff | To | Direction | Status |
|---|---|---|---|---|
| **CH-01** | *"a costed fact needs a stable identity we can attribute to"* | the posting domains, reconciled by P11 | P09 **requires** | `CANDIDATE HANDOFF` — the identity does not exist |
| **CH-02** | *"a costed fact must declare whether it has a financial effect"* | operational + posting domains | P09 **requires** | `CANDIDATE HANDOFF` |
| **CH-03** | *"a commitment must declare the event at which it becomes an actual"* | the commitment-raising domain | P09 **requires** | `CANDIDATE HANDOFF` |
| **CH-04** | management figures on a financial surface (CO-04) | the financial-reporting domain | P09 **emits** | `CANDIDATE HANDOFF — P09 RECOMMENDS AGAINST` |
| **CH-05** | allocation-generated postings (CO-05) | the ledger | P09 **emits** | `CANDIDATE HANDOFF — P09 RECOMMENDS AGAINST` |
| **CH-06** | *"a management figure carried into reconciliation must state its sign convention and its scope"* | P11 | P09 **emits** | `CANDIDATE HANDOFF` |

**This table is a SUBSET.** `CH-07` and `CH-08` exist in `P09_CANDIDATE_HANDOFF_REGISTER` and were **omitted here** — the two most decision-relevant inbound requirements dropped from the summary pack a downstream reader would lift. **CORRECTED by reference**; the authoritative set is the handoff register's, and it has **eight** rows, not nine and not six.

**None of `CH-01`…`CH-08` is a contract.** Each states a required *meaning* at the boundary. **P09 did not research how any counterparty would satisfy it.**

---

## 6. WHAT THIS PACK DOES NOT DECLARE

No final contract. No schema. No API. No event bus. No workflow. No implementation. No adjacent-domain behaviour. No statutory position. No build selection. No gate movement. **Boss is sole Final Approver.**
