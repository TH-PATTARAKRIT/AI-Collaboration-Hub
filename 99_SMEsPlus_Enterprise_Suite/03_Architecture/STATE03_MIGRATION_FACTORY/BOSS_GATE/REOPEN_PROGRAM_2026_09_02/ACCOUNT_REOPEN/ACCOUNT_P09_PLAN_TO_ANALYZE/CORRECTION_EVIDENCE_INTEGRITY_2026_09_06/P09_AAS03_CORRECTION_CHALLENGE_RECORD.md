# P09_AAS03_CORRECTION_CHALLENGE_RECORD

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room.

Four bounded challenges, disjoint assignments, run **only against surfaces changed by this correction**, against a **frozen** package. **Every adopted finding was re-verified against source by the author before adoption.** Dissent preserved.

---

## 1. RESULT

| | |
|---|---|
| Findings returned | **31** |
| Re-verified against source before adoption | **31** |
| Adopted | **27** |
| Narrowed on re-verification | **3** |
| Adopted **in P09's favour** (an under-claim) | **1** |
| Author errors this round | **9** |
| Self-caught before challenge | **2** |
| **Caught only by challenge** | **7** |

**The process breach of the previous round was not repeated: the package was frozen before the challenges opened, and no file was edited while they ran.**

---

## 2. THE VERDICT ON THIS ROUND'S CENTRAL CLAIM

> **The corrected instrument is better than the one it replaced, and it is still wrong.**

| | Name-based selector | Model-based selector |
|---|---|---|
| P09 ownership | wrong in both directions | **correct — 10 files, 3 modules, reproduced by two challengers independently** |
| population | 4 modules | **52 files / 29 modules — after four defects, one of which shipped** |
| forecast object | invisible | **still invisible** |

**All four experts converged again — this time on the fact that the corrected instrument carries defects of the same class it was built to eliminate.**

---

## 3. WHAT WAS FALSIFIED — VERIFIED AT SOURCE

| # | Published claim | Source shows | Verdict |
|---|---|---|---|
| **1** | *"the corrected selector … negative control now returns 0"* | the selector **printed as corrected carries no anchor**; the published population is the output of the **unfixed** instrument, and the control returns **1** | **CONTRADICTED** |
| **2** | population **49 / 28** | **52 / 29.** Four files inherit a P09 model from a **non-first list position** — one in a **multi-line** list; an entire module was absent | **CONTRADICTED** |
| **3** | extension split **39 / 27** | **42 / 26** | **CONTRADICTED** |
| **4** | fact-table extenders **16** | **17** — an off-by-one **inside the author's own population** | **CONTRADICTED** |
| **5** | allocation-mixin extenders **7** | **10**; and a whole model row was missing from the matrix | **CONTRADICTED** |
| **6** | blind spot `B-2` is *"class C — invisible by construction"* | the property was mis-stated; it is **class A, measurable**, floor **164 files / 51 modules** | **CONTRADICTED** |
| **7** | the forecast zero demonstrates `B-2` | it demonstrates **`B-1`** — the declaring file reaches the fact table by **raw SQL**. `B-1` was classed *"not searched"* and is populated: **12 files / 3 unseen modules** | **CONTRADICTED** |
| **8** | *"all four positive controls passed; the instrument is accepted"* | control 4 was satisfied by a **different file** than the object it names — a module-granular control for a file-granular instrument. **It failed** | **CONTRADICTED** |
| **9** | the second family is *"self-contained / extended by nothing"* | nothing **inherits** it, but an adjacent master model carries a **reverse relation** into it | **CONTRADICTED** |
| **10** | `CI-05b` — *"one specific account on a single date"* | its writer takes a real **window** and decomposes it into monthly rows; the item amount is a **delta**; and it is written **by the consuming report from a user's cell** | **CONTRADICTED** |
| **11** | `CH-06` — sign convention, scope, rate source and rate date | the consumption row set mixes **rate bases per component** on a carrier with **no currency field**; one pair is not sufficient | **CONTRADICTED** |
| **12** | `CH-07` — *"type versus specific account, different blast radii"* | the second family is **also** account-type gated at consumption. The radii differ in **shape**, not reach | **CONFIRMED WITH CAVEAT** |
| **13** | `CI-05b` scope *"COMPANY — required, defaulted"* | true of the **header**; the **amount-bearing row has no company field** — company is stamped from the **reader's** active company | **CONFIRMED WITH CAVEAT** |
| **14** | the domain-purity flip to PRESERVED | one challenger could not falsify it; another showed the test is **near-tautological**. It **holds on the corrected population, by luck of what the four missed files contained** | **CONFIRMED WITH CAVEAT** |
| **15** | veto discharge condition = *"a semantics-keyed instrument … wider work"* | **two thirds of it is two greps over the already-declared root**, both available this round | **CONFIRMED WITH CAVEAT** |

---

## 4. ADOPTED IN P09'S FAVOUR — THE ROUND UNDER-CLAIMED

One challenger looked specifically for quiet adjacent-domain research and **found none**: every R2R fact is confined to the lines cited, every commitment fact derives from P09-authored files. **The purity discipline held.**

Its finding was the opposite one — **two P09-side facts were omitted that require no adjacent-domain reading**, and both are now recorded:

| # | Fact | Significance |
|---|---|---|
| **N-1** | the second family's rows are shadowed into the report as **`parent_state: 'posted'`**, plan amount written into **`balance`**, on a temp table inheriting the ledger row with NOT-NULL dropped on currency, move, journal and display type | **a second instance of the report-shadowing mechanism `AAS+-VETO-02` already stands against.** P09 plan rows are read as posted journal items |
| **N-2** | a P09-authored file reads the plan line through **`sudo()`** from an adjacent-domain document | an elevated read **inward** into P09's surface, bypassing record rules including company rules |

Plus **N-3** (no company on the amount row), **N-4** (mixed rate bases, no currency) and **N-5** (no unique constraint, no company check; duplicates tolerated by design).

**The "minimum interface fact" rule had been applied as a ceiling on volume rather than a floor on P09-relevance.**

---

## 5. DISSENT PRESERVED

| ID | Disagreement | Position |
|---|---|---|
| **DIS-C1** | Population: one challenger measured **52/29**, another **51/29**. | **Reconciled: 52 is right at the published (unanchored) selector; 51 at the anchored one; the difference is the D1 false positive. The correct figure at the corrected instrument is 52 files including that file's legitimate re-admission as a *reference* case — recorded with both numbers and the reason.** |
| **DIS-C2** | Is the purity flip earned or self-serving? | **UNRESOLVED, both recorded.** It survived an independent attempt at falsification; it is also near-tautological by construction. Both are true and neither cancels the other. |
| **DIS-C3** | Is `B-2` real at all? | **Both stand.** The *class* is real; the *instance* used to demonstrate it was misclassified, and the class is measurable rather than invisible. |
| **DIS-C4** | Is the second family a P09 planning object, or a reporting artefact P09 is over-claiming? | **UNRESOLVED.** It declares planning models and is keyed to an account; it is also written from a report cell and consumed only by that report. **P09 does not settle it here.** |
| **DIS-C5** | Identity and cardinality of the second family | **NOT DECIDABLE** without report-engine research this round correctly declined. Flagged as an unmeasured surface, not a defect. |

---

## 6. AUTHOR-ERROR LINEAGE

| Round | Errors | Self-caught |
|---|---|---|
| lineage before this round | 45 | 10 |
| **this round** | **9** | **2** |
| **total** | **54** | **12** |

**Eleven of the fifty-four are denominator or unit errors.** This round added two more, and both were **inside the instrument built to end that class**: a fix described but not applied, and a pattern that shipped with a position dependence.

**The lesson this round adds:** *the round that corrects a denominator is the round most likely to publish a new one.* The corrections were real, the ownership result is right and independently reproduced — and the population number carrying it was wrong in both directions.
