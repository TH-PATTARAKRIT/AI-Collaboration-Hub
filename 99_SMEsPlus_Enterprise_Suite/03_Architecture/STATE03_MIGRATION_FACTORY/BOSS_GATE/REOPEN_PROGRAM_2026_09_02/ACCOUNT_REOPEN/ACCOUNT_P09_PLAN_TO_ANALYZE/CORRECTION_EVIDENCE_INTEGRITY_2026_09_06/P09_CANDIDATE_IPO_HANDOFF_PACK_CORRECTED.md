# P09_CANDIDATE_IPO_HANDOFF_PACK — CORRECTED

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room.

> **CANDIDATE ONLY. NOT A CONTRACT. The term `FINAL CONTRACT` is not used in PHASE S.**
> This supersedes the corresponding sections of the Phase S pack **only where the corrected population changes them.** Superseded wording is retained in the prior pack and in the re-derivation register.
> **`AAS+-VETO-04` remains in force over every completeness claim below.**

---

## 1. WHAT CHANGED, AND WHAT DID NOT

| Changed by the correction | Unchanged |
|---|---|
| the intended amount is **two objects, not one** | the analytic attribution semantics |
| the count and class of Candidate Inputs | the allocation arithmetic |
| Candidate Output terminality, restated precisely | the three contested outbound handoffs |
| the domain classification of the over-plan computations | the zeroing consequence |
| handoff population reconciled to **one** identifier set | the sign-convention requirement to reconciliation |

---

## 2. CANDIDATE INPUT — CORRECTED

`CANDIDATE INPUT`. Producer internals **not researched**.

| # | Candidate Input | Required meaning | Producer candidate | Scope | Period meaning | Status |
|---|---|---|---|---|---|---|
| **CI-01** | a costed fact **with** a financial effect | an amount a legal entity has incurred or earned, already posted | `EXTERNAL DOMAIN BOUNDARY` | COMPANY | accounting date | unchanged; needs an event identity **not found in the scope P09 has read** |
| **CI-02** | a costed fact **without** a financial effect | an operational measurement carrying a cost | `EXTERNAL DOMAIN BOUNDARY` | COMPANY / TENANT | operational event date | unchanged |
| **CI-03a** | **the dimension axis** | the tenant's declared axis of management analysis | **P09-OWNED** | TENANT | effective-dated | **SPLIT from the former CI-03** — the axis and its values have different scope carriers and different determinations |
| **CI-03b** | **the dimension value** | one member of an axis | **P09-OWNED** | TENANT, or COMPANY where it denotes a legal-entity object | effective-dated | **SPLIT** |
| **CI-04** | the allocation instruction | what share of a costed fact belongs where | **P09-OWNED as a rule** | TENANT rule, COMPANY application | the fact's date | unchanged |
| **CI-05a** | **the dimensional intended amount** | intent per dimension over a **window** | **P09-OWNED** | TENANT or COMPANY, declared per plan | `date_from` / `date_to` | **CORRECTED** — this is one of two intended-amount objects |
| **CI-05b** | **the account-keyed intended amount** | intent for **one specific account** on a **single date** | **P09-OWNED** | **COMPANY — required, defaulted** | **a single date, not a window** | **NEW.** Carries **no analytic dimension**, **no currency**, **no state**, **no revision lineage** |
| **CI-06** | the commitment | value committed but not yet incurred | `EXTERNAL DOMAIN BOUNDARY` — the commitment carrier | COMPANY | order date | unchanged; carrier is generation-specific, and its zero is ambiguous between *nothing committed* and *module absent* |

**Count: 8 rows — and the count is a `CANDIDATE`, not a closed set.** `AAS+-VETO-04` blocks any claim that this enumeration is complete: blind spot `B-2` is demonstrably populated.

---

## 3. CANDIDATE PROCESS SEMANTIC — CORRECTED WHERE AFFECTED

| # | Semantic | Corrected statement | Class |
|---|---|---|---|
| **CP-04** | plan-versus-actual comparison | applies to the **dimensional** family only. The **account-keyed** family carries **no consumption figures on the model at all** — comparison happens entirely in the consuming report | `FACT VERIFIED — P09` |
| **CP-06** | over-plan signalling | **three computations.** One on the plan line; **two in P09-authored files attached to an adjacent-domain commitment carrier**, one of which is a **prospective** test | `FACT VERIFIED — P09` |
| **CP-10** *(new)* | **account-keyed planning** | an intended amount may be stated **per individual account**, dimensionless, single-dated, currency-less | `FACT VERIFIED — P09` |

---

## 4. CANDIDATE OUTPUT — TERMINALITY RESTATED

The previous pack called three outputs terminal; that was corrected to one. Restated precisely here:

| # | Output | Crosses a boundary? | Status |
|---|---|---|---|
| **CO-01** | management attribution by dimension value | **YES** — carried to reconciliation with a required sign convention, and its value varies with the reading user's company and the reading day's rate | `CANDIDATE HANDOFF` |
| **CO-02a** | dimensional plan consumption | **YES** — same reasons | `CANDIDATE HANDOFF` |
| **CO-02b** | **account-keyed plan comparison** | **YES** — consumed by a financial report as a comparison column via a temporary table | `CANDIDATE HANDOFF` — **new, and it is the second instance of the report-substitution mechanism P09 has already recorded against** |
| **CO-03** | the over-plan signal | **partly** — plan-scoped instance is terminal; the two commitment-carrier instances surface on an adjacent domain's document | **terminal only for the plan-line instance** |

**No output is now claimed as unconditionally terminal.**

---

## 5. CANDIDATE HANDOFF — ONE RECONCILED POPULATION

**Eight rows. This is the authoritative set; the earlier three populations are superseded.**

| # | Direction | Handoff | Status |
|---|---|---|---|
| **CH-01** | inbound | a costed fact carries a stable identity | `EXTERNAL DOMAIN BOUNDARY` — identity **not found in the scope P09 has read** |
| **CH-02** | inbound | a costed fact declares whether it has a financial effect | `EXTERNAL DOMAIN BOUNDARY` |
| **CH-03** | inbound | a commitment declares the event at which it becomes an actual | `EXTERNAL DOMAIN BOUNDARY` |
| **CH-07** | inbound | an account's **type** is stable and its change governed | `EXTERNAL DOMAIN BOUNDARY` — **and now sharper**: one planning family keys to an account **type**, the other to a **specific account**, so a typing change and an account change have different blast radii |
| **CH-08** | inbound | a producing domain declares when it allocates every row of a balanced set | `EXTERNAL DOMAIN BOUNDARY` |
| **CH-04** | outbound | management figures on a financial statement surface | `CANDIDATE HANDOFF — P09 RECOMMENDS AGAINST` |
| **CH-05** | outbound | postings generated from a management allocation rule | `CANDIDATE HANDOFF — P09 RECOMMENDS AGAINST` |
| **CH-06** | outbound | any management figure into reconciliation, **with sign convention, scope, and — added — rate source and rate date** | `CANDIDATE HANDOFF` |

**`CH-09` is deleted, not renumbered.** It asserted terminality that has been withdrawn; retaining it as a handoff row would preserve the error that produced three conflicting populations.

---

## 6. WHAT THIS PACK STILL DOES NOT CLAIM

No contract. No counterparty agreement. No completeness — `AAS+-VETO-04` stands over every count here. No adjacent-domain behaviour. No statutory position. No build selection. No PHASE SA control. **Boss is sole Final Approver.**
