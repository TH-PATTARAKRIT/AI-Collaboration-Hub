# P09_CORRECTED_EVIDENCE_POPULATION_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room. Evidence identifiers resolve in Layer 2.

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements here were **contradicted by the four AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are inline; superseded wording is retained. Full list: `P09_AAS03_CORRECTION_CHALLENGE_RECORD`.

---

## 1. THE CLOSURE QUESTION, DECLARED BEFORE THE SEARCH

**CQ-C-01.** *What is the complete P09-owned model / field / file population inside the already-declared P09 roots?*

| Element | Declared |
|---|---|
| **purpose** | replace a module-name selection with one at the unit in which the claims are asserted |
| **root** | **the already-declared root only.** No new root. No estate, volume or cloud sweep |
| **unit** | **file → model declaration / extension → field / function** |
| **denominator** | every source file in the root that declares or extends a P09 model |
| **expected class** | a superset of the four modules previously declared |
| **stop condition** | every such file enumerated, with positive controls proving the instrument sees the four objects the previous selector missed |

---

## 2. THE CORRECTED POPULATION

> ~~**49 files across 28 modules**~~ → **52 files across 29 modules** — against **4 modules** previously declared.
>
> **CORRECTED AFTER CHALLENGE.** The published 49 was **wrong in both directions at once**: it admitted one file on the very false-positive class this round named and claimed to have fixed, and it missed **four** files whose inheritance of a P09 model sits in a **non-first list position** — one of them in a **multi-line** list, invisible to any single-line pattern. **An entire module was absent from the declared set.**

| Class | Files | Modules |
|---|---|---|
| **P09-OWNED** — declares a P09 model | **10** | **3** *(unchanged by the correction)* |
| **EXTENDS a P09 model** — producers and consumers writing into P09's surface | ~~39~~ **42** | ~~27~~ **26** |

**Positive controls: three of four hold; the fourth FAILED and was wrongly recorded as holding.** Control 4 was satisfied by a *different file* in the forecast module than the one declaring the object under test — an acceptance control evaluated at **module** granularity for an instrument declared **file**-granular. **A control that returns a positive while the object it names is unreachable is not a control on that object**, and *"the instrument is accepted"* did not follow from it. The instrument sees the enterprise analytic extension, the project-budget module, the module carrying the second planning family, and the module named `forecast` — every object the name-based selector provably could not reach (`EV-P09-300`).

---

## 3. THE PRIOR DECLARATION WAS WRONG IN BOTH DIRECTIONS

This is the correction, stated plainly.

| Previously declared P09-owned | Corrected |
|---|---|
| the analytic module | **OWNS** — correct |
| the plan module | **OWNS** — correct |
| the enterprise analytic extension | **DOES NOT OWN** — it only extends. **Wrongly included** |
| the project-budget module | **DOES NOT OWN** — it only extends. **Wrongly included** |
| — | **the financial-reporting module OWNS a second planning family. Wrongly excluded** |

**Two modules were counted as owned that are not, and one that is was not counted.** A name pattern cannot distinguish *declaring* a model from *extending* one, and ownership is exactly that distinction.

---

## 4. OWNERSHIP IS A PROPERTY OF THE FILE — PROVEN IN BOTH DIRECTIONS

| Direction | Evidence |
|---|---|
| a **P09 module** containing **adjacent-domain files** | the plan module holds two files that attach P09 plan semantics to a **purchase-domain carrier** |
| an **adjacent-domain module** containing a **P09 file** | the financial-reporting module — some thirty files extending report, ledger, partner and company models — holds **one file declaring a P09 planning family** |

> **Module-level ownership cannot express either case. File-level ownership expresses both.**
> This is why the previous round's domain-purity verdict was `NOT DECIDABLE`: it was measured on the wrong unit, not measured wrongly.

**`PC-01` — P09 ownership shall be declared at file granularity, and every declaration shall state whether the file *declares* or *extends* the model it touches.**

---

## 5. DECLARED BLIND SPOTS OF THE CORRECTED INSTRUMENT

Recorded because a corrected instrument that hides its own limits repeats the defect it fixed.

| # | Blind spot | Class |
|---|---|---|
| **B-1** | a model reached through a variable-held name, or through **raw SQL** | **CLASS CORRECTED: A — populated, and it is the class the forecast object actually falls in.** Measured: **15 files reach a P09 table by raw SQL; 12 lie outside the population, in 3 modules absent from it entirely.** Closable by one bounded command that was not run |
| **B-2** | P09 semantics on an adjacent-domain carrier that **does not declare or inherit** a P09 model | **CLASS CORRECTED: A — measurable, and now measured.** The property was mis-stated as *"never touches"*; the named instance **does** touch P09 models by relational reference. Measured: **187 files reference a P09 model without declaring or inheriting it; 164 lie outside the population, across 51 modules** |
| **B-3** | non-source carriers such as views and data files | **C — not searched.** The prior round's variance disposition was already reduced for this reason |
| **B-4** | roots outside the declared one, including the unresolved principal root of the base package | **B — boundary declared, deliberately not chased**; chasing it needs the estate sweep this prompt forbids |

**`PC-02` — CORRECTED. The residue was mis-stated AND under-stated.** A model-based selector cures the name-based selector's blind spot and introduces its own — but that residue is **not invisible by construction**. It is **measurable on the already-declared root**, and measuring it returns a floor of **164 files across 51 modules** (reference class) and **12 files across 3 unseen modules** (raw-SQL class).

**`PC-03` (new) — declaring a blind spot as class C is itself a claim, and must be tested before it is published.** Two of this round's four blind spots were class **A** all along. **Declaring a limit is not measuring it**, and an unmeasured limit understates the very gap it exists to disclose.

---

## 6. TWO DEFECTS IN THIS ROUND'S OWN INSTRUMENT, BOTH CAUGHT BEFORE PUBLICATION

| # | Defect | Consequence had it shipped |
|---|---|---|
| **D1** | a relational-field attribute whose name **ends with the declaration keyword** matched the declaration pattern | 3 files falsely reported as declaring a P09 model |
| **D2** | the *declare-and-inherit-the-same-model* pattern is an **in-place extension**, not a declaration | 2 timesheet files falsely reported as **owning the management fact model** |

Uncorrected, the pair would have inflated P09 ownership from 3 modules to 5 **and assigned the management fact model to a timesheet module.** Both were found by inspecting the suspicious rows instead of accepting the count.

> **AND THE D1 FIX WAS NEVER APPLIED TO THE PUBLISHED NUMBER.** The selector printed as *"the corrected selector"* carries **no anchor**; the published 49 is the output of the **unfixed** instrument, and the negative control returns **1**, not 0.
>
> **A third defect, `D3`, shipped undetected: list-position dependence.** The pattern matched a P09 model in an inheritance list only when it was the **first** element, missing four files — one in a multi-line list no single-line pattern can see.
>
> **The single defect this round offered as evidence of instrument discipline was described and not carried into the artefact.**

---

## 7. DISPOSITIONS

| Item | Disposition |
|---|---|
| the corrected population | ~~49 / 28~~ → **52 files / 29 modules** — `CONTRADICTED — CORRECTED` |
| the ownership split | ~~10 / 39~~ → **10 owning / 42 extending** — `CONTRADICTED — CORRECTED`; the owning count is unchanged |
| `PC-01` file-granular ownership | `SUPPORTED INTERPRETATION — P09` |
| blind spots `B-1`…`B-4` | `UNRESOLVED — SPECIFIC EVIDENCE REQUIRED`, each with its class and boundary |
| the base package's unresolved principal root | `UNRESOLVED — SPECIFIC EVIDENCE / AUTHORIZATION REQUIRED` — named, not chased |
