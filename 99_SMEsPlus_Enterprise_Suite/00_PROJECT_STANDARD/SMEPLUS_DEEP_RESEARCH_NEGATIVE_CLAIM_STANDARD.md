# SMEPLUS DEEP RESEARCH — NEGATIVE CLAIM CONTROL STANDARD

Status: **issued for Boss ratification** · Origin session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`
Effective: on Boss ratification · Scope: **all** SMEsPlus Deep Research domains and **all** Levels

---

## 1. Why this standard exists

In session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`, six research claims were contradicted by
independent review. **Three of the six were negatives asserted at a scope wider than the evidence
actually searched.** In each case the researcher searched a narrow boundary, found nothing, and
reported the finding as a property of the whole system.

| Failure | What was searched | What was claimed | Reality |
|---|---|---|---|
| Fiscal year | one token spelling in one directory | "no fiscal-year model exists in the tree" | the model exists under a different name in an adjacent module |
| Rate types | one file in a module | "no rate-type dimension exists" | four rate types are derived at query time in the same module |
| Localization source | not searched | implied unavailable | two localization modules present in the verified build |

A prior session in this programme failed the same way and concluded "no source code or database
access exists" after searching only its own working tree. **This is therefore a recurring, systemic
defect, not an isolated lapse**, and it warrants a standing control.

---

## 2. The rule

> ### `ABSENCE OF EVIDENCE WITHIN SEARCHED SCOPE SHALL NOT BE REPORTED AS ABSENCE OF BEHAVIOUR ACROSS THE WHOLE SYSTEM.`
>
> Canonical shorthand: **`NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST`**

A negative conclusion is valid **only** when its declared search boundary and its evidence support
that exact scope — no wider.

---

## 3. Mandatory classification of every negative claim

| Class | Name | Meaning | May be relied upon? |
|---|---|---|---|
| **A** | `VERIFIED ABSENCE` | Evidence proves the behaviour does not exist **within an explicitly stated scope** | yes, **within that stated scope only** |
| **B** | `NOT FOUND IN SEARCHED SCOPE` | The search did not find evidence; absence is **not** proven | no — treat as open |
| **C** | `NOT YET SEARCHED` | The relevant scope has not been investigated | no |
| **D** | `UNKNOWN` | Available evidence supports neither presence nor absence | no |
| **E** | `CONTRADICTED` | New evidence disproves a prior negative claim | the prior claim is void |

### The conversion prohibition

> **B, C and D SHALL NEVER be converted into A.**

Elapsed time, repetition, restatement in a later document, downstream citation, or the absence of a
challenge do **not** upgrade a class. Only new evidence, at a stated scope, upgrades a negative to A.

Class A always travels with its scope. `VERIFIED ABSENCE` is never written unqualified.

---

## 4. Rules

**`DR-NC-01`** Absence of evidence within searched scope SHALL NOT be reported as absence of
behaviour across the whole system.

**`DR-NC-02`** Every material negative claim SHALL declare its search boundary — the modules, files,
directories, screens, configurations, database objects or runtime states actually examined, and the
method used.

**`DR-NC-03`** "Not found" SHALL be distinguished from "verified absent", using the class letters in
§3.

**`DR-NC-04`** System-wide negative claims require system-wide evidence proportional to the claim. A
claim about "the system" requires a search of the system. A claim about a module requires a search of
the module.

**`DR-NC-05`** Independent Review SHALL challenge high-impact negative claims before they are relied
upon. A negative that blocks a gate, drives a `REJECT` decision, or supports a `Tolerance = 0`
proposal is high-impact by definition.

**`DR-NC-06`** If a later reviewer finds contradictory evidence, the original negative SHALL be
re-scoped, corrected or retracted **with lineage preserved**. The original claim is never silently
deleted or overwritten.

---

## 5. Required wording

**Prohibited**, unless the whole relevant system boundary was proven:

- "The system does not support X."
- "X does not exist."
- "There is no X."
- "X is not implemented anywhere."
- "No X exists in the tree."

**Required form:**

> "No evidence of X was found within \[explicit scope: modules / files / directories / UI / configuration / database / runtime searched\], using \[method\]. Other scopes remain unverified. Classification: **B — NOT FOUND IN SEARCHED SCOPE**."

Or, where absence genuinely was proven:

> "X is absent from \[explicit scope\], verified by \[method\]. Classification: **A — VERIFIED ABSENCE within that scope**. Behaviour outside that scope is not addressed."

### Words requiring evidence proportional to their strength

`never` · `always` · `only` · `none` · `nothing` · `anywhere` · `no such` · `cannot`

Each occurrence in a research deliverable SHALL be supported by a stated boundary, or rewritten.

---

## 6. Search-boundary declaration — minimum content

Every material negative claim carries:

1. **Roots searched** — absolute paths or named systems.
2. **Method** — the search performed, precisely enough to repeat (the exact pattern, the tool).
3. **Known unsearched adjacent scopes** — named, not merely implied. Enterprise or advanced modules,
   localization modules, the web client, reporting layers, runtime state and database contents are
   each separate scopes and are commonly missed.
4. **Naming risk** — whether alternative names, spellings, separators or synonyms for the sought
   concept were tried. *Two of the three origin failures were pure naming-variant misses.*

---

## 7. Applicability

This standard applies to **all** SMEsPlus Deep Research work, at **all** Levels:

Accounting · Inventory · Purchase · Sale · Manufacturing · CRM · Project · HR · Approval · Document ·
Payment · and every future domain.

It applies equally to research teams, expert reviewers, challenge units and audit units. A reviewer's
negative is subject to the same rule as a researcher's.

---

## 8. Interaction with existing project rules

| Existing rule | Interaction |
|---|---|
| `No Evidence = No Progress` | **This standard is its converse.** That rule stops a positive claim without evidence; this one stops a *negative* claim without evidence. Both were needed; only the first existed |
| Evidence classes (`VERIFIED FACT` / `REFERENCE BEHAVIOUR` / `INFERENCE` / `RECOMMENDATION` / `UNKNOWN`) | unchanged and still required. The negative class in §3 is **additional**, not a replacement — a negative carries both |
| Constitution principle 7 — independent reviewers must not review their own work | `DR-NC-05` is the operational hook: independent review is where high-impact negatives are challenged |
| Constitution principle 12 — `0 BUG FOUND` triggers Test Adequacy Verification | the same logic: a null result is a claim about the search, not about the system. This standard generalises that principle from testing to research |
| Prohibited verdict vocabulary | unchanged |

`INFERENCE:` principle 12 already encoded this idea for testing. The programme did not carry it into
research. This standard closes that asymmetry.

---

## 9. Compliance check for a research session

Before any package is declared ready for a gate:

1. Mechanically scan for the §5 prohibited forms and the strength words.
2. For each occurrence, confirm a declared boundary and a class letter, or rewrite.
3. Confirm no B, C or D has been restated as A anywhere in the package, including in summaries,
   executive sections and gate reports — **restatement is where the upgrade usually happens**.
4. Record the scan result in the session closure.
5. Where a negative is high-impact, confirm it was independently challenged.

---

## 10. Standing note for gates

Where a research package contains material negatives, its **positive** and **negative** findings
should be weighted differently. Positives that survive independent re-verification are the stronger
class. Negatives are the weaker class and should be re-scoped before reliance.

This is not a criticism of any team. It is a property of searching: finding a thing proves it exists;
not finding it proves only that the search did not find it.
