# MCC_K — REUSABLE METHOD DELTA

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room
Proposed delta to `SMEPLUS_DEEP_RESEARCH_METHOD_CONVERGENCE_STANDARD.md` (`SMEPLUS-DR-MC-001`)
and to `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD.md` (`DR-NC-01`…`06`).

> **Proposal only. Boss ratifies. Nothing in the project-wide standard is modified by this session,
> and no prior conclusion is overwritten — lineage is preserved throughout.**

---

## 1. Why this section exists at all

Boss has declared the L1–L12 Deep Research approach and the Method Convergence protocol
**project-wide standards**. Everything learned here must therefore be classified by transferability
and handed to the modules that come next: Inventory, Purchase, Sale, Manufacturing, CRM, Project, HR,
Approval, Document, Payment.

**The single most valuable thing this round produced is not a finding about currency rates.** It is a
complete statement of a defect that has now caused every failure in this programme, five rounds
running, and that the previous rounds had learned three-quarters of.

---

## 2. `ER-CORE-1` — the complete denominator rule · `DOMAIN-INDEPENDENT`

> ### A denominator is `POPULATION` + `PATTERN` + `PATH SET` + `UNIT`.
> ### None of the four may be chosen by the author of the claim it bounds.

| Clause | Learned at | What it means | What it cost to learn |
|---|---|---|---|
| `POPULATION` | `GB-04`, MC round | Enumerate what the system **is made of**, not what it is **for**. A taxonomy of business functions has no cell a fact about mechanism can occupy | 3 rounds of findings that no round could bound |
| `PATTERN` | `GB-07` / `ER-CORE`, MC round | Declare the expression that selects members, and its **false-negative modes**. A population bounded by a regex is bounded by the regex, not by the source | 2 false closures |
| **`PATH SET`** | **this round, twice** | Declare and **prove** the directories searched. Proving a path set means enumerating the source root, not repeating a habit | The rate surface was under-bounded by 6 files; the module tree by 962 modules; the localisation surface by 904 of 906 |
| **`UNIT`** | **this round** | Say what **one member is**. Two disciplined enumerations of the identical bounded surface returned **12** and **14** because one counted expressions and the other counted sites | A denominator that cannot be compared between two reviewers |
| **`INDEPENDENCE`** | **this round** | The four clauses above are all chosen by whoever writes them. **A control designed by the author is not independent of the author** | The reviewer brief written by this session named a wrong path; only an independent operator noticed |

**Classification: `DOMAIN-INDEPENDENT`.** Applies unchanged to every SMEsPlus module.

---

## 3. `ER-CORE-2` — enumerate by call site, then read · `DOMAIN-INDEPENDENT`

> **Never extract a value with a second pattern. Find the call sites with a token search, then read
> each one.**

Evidence: one population of six configuration keys defeated **two** different regexes in **two**
rounds, by two different mechanisms — a call spanning lines, and a double-quoted literal. **The
call-site token search returned all six on the first attempt, both times.** Only the value-extraction
step ever failed.

**Generalisation:** the same applies to any two-stage enumeration — find, then parse. **The find stage
is robust; the parse stage is where populations get silently truncated.** Read the sites.

---

## 4. `ER-CORE-3` — the correction-propagation rule · `DOMAIN-INDEPENDENT`

Closes `GB-06`. **Demonstrated in this round rather than merely proposed.**

> 1. Every accepted correction lands **in the register it contradicts, by id**, before the round closes.
> 2. The corrected text is **not deleted**. The correction is appended and the governing order is
>    stated **once**, at the top of the package.
> 3. A correction that changes a **published metric** must name every artefact that carries that
>    metric.
> 4. Reviewer findings are consolidated **by id**, never by re-narration. A finding that appears in no
>    file outside the review that raised it has been **lost**.
> 5. **Corrections may themselves be wrong.** This round found an accepted correction that reversed a
>    figure the original had right. A correction register needs the same discipline as a finding
>    register.

**Cost when absent, measured:** 7 contradicted affirmative claims standing live at a gate baseline ·
5 orphan unknown ids · 2 unregistered balanced-but-wrong cases · **1 lost tolerance-zero candidate** ·
2 corrections a round accepted and never propagated to the registers that publish the contradicted
figures.

---

## 5. `ER-CORE-4` — the empty-cell rule · `DOMAIN-INDEPENDENT`

> **An empty cell in a taxonomy means UNSEARCHED until a declared search has been run against it.
> It never means ABSENT.**

Evidence, decisive and cheap: two taxonomy classes stood at **zero instances** and had never been
searched. **One was searched this round and produced a verified defect immediately.** The other has
still not been searched and is still reported as zero.

**Operational form:** every taxonomy, matrix or coverage register must carry, per cell, either an
instance **or** a declared search that found none **or** the marker `NOT SEARCHED`. **A blank is
forbidden.**

---

## 6. `ER-CORE-5` — the discovery-asymmetry rule · `DOMAIN-INDEPENDENT`

> **Independent review is not a quality gate on the method. It is the only discovery engine the
> method has. Budget it as such.**

Five rounds. **Every material correction came from an independent reviewer; none from the author.**
Including the round convened to diagnose that pattern, and including this round, convened to close
that round. In this round the author caught **one** of its own four errors.

**Consequences for planning, stated as ratios rather than exhortation:**

| Rule | Form |
|---|---|
| `ER-CORE-5a` | Independent review is **not** a final check. Schedule it **inside** the enumeration phase, not after it |
| `ER-CORE-5b` | Reviewers get **disjoint** assignments. Two reviewers on one surface confirm each other; two reviewers on disjoint surfaces find different things — this round's two found **zero overlapping** primary findings |
| `ER-CORE-5c` | At least one reviewer must be **adversarial by assignment** — tasked to find a missing population, a new class, an unbounded negative, a misclassification, a denominator defect. The confirmatory reviewer will not find these |
| `ER-CORE-5d` | **Reviewer instruments are authored by someone, and are therefore defective.** State in every brief: *"if any path or definition in this brief is wrong, report it as a finding."* This round's brief was wrong and only that instruction surfaced it |
| `ER-CORE-5e` | Record reviewer claims that are **reduced or rejected** on verification, alongside those accepted. `Independent Review ≠ Truth` must be visible in both directions or it is a slogan |

---

## 7. `ER-CORE-6` — the cross-version rule · `DOMAIN-INDEPENDENT`

> **Compare files, not tokens. Version order does not predict behaviour.**

Two independent confirmations now exist in this programme, in two unrelated domains:
- costing — the reference ERP's own costing pattern is unstable across its own versions;
- **FX — a branch-preference behaviour exists in a LATER v18 point release and in NEITHER v19 tree;
  and v19 ADDS a rate resolver in the ORM core that no v18 has.**

**Operational form:** any claim of cross-version stability must be supported by a **file-level diff**,
never by a checklist of tokens. This round asserted stability from a token list and was wrong.

**Corollary for SMEsPlus specifically:** *a v18 → v19 migration can WIDEN a control surface rather
than converging it.* Every module's Wave A conclusions must be re-tested on the target version before
they are relied on.

---

## 8. `ER-CORE-7` — the declared-but-inert control rule · `DOMAIN-INDEPENDENT`

> **A control is not present because it is declared. Prove the gate that executes it.**

Two bounded instances this round: **16** company-consistency guards declared on the company model,
on the destination accounts of automatically generated ledger facts, where the automatic check is
**never enabled** and the check is **never invoked**; and a declared uniqueness constraint whose
**definition string is empty**.

**Operational form — three questions, asked of every control found:**
`Where is it declared?` → `What executes it?` → `Under what condition does that executor run?`
**A control that answers only the first question is a comment.**

---

## 9. Module-specific and boundary-specific rules

| Rule | Classification | Statement |
|---|---|---|
| `ER-FX-1` | **`FX-SPECIFIC`** | Enumerate rate **resolvers**, not rate **writers**. Writers are few and guarded; resolvers are many, disagree, and are where the money is lost. Over one table this round found **14 sites / 12 expressions**, 6 including the shared row and 6 excluding it |
| `ER-FX-2` | **`FX-SPECIFIC`** | Enumerate the **fallback chain of every resolver**, to its end. This one table has **four** distinct fallback semantics: par · the earliest rate *ever* · the earliest *future* rate · and a report-time par substituted where the ledger used a real rate. **Par is the least dangerous of the four** and is the only one the programme had been tracking |
| `ER-CB-1` | **`COMPANY-BOUNDARY-SPECIFIC`** | Any guard written over a **root** or an **ancestor chain** rather than the company itself is a candidate defect. Enumerate every such expression and assess each. In this addon there are **37**, of which **4** were ever assessed — and one of the unassessed ones admits cross-branch settlement of a posted fact |
| `ER-CB-2` | **`COMPANY-BOUNDARY-SPECIFIC`** | A field declared `readonly` is a **client-side** attribute. If a model's own create routine honours a caller-supplied value for it, `readonly` is not a control |
| `ER-CB-3` | **`COMPANY-BOUNDARY-SPECIFIC`** | An authorisation that checks **group membership** and then writes under **elevated privilege** has no company dimension. Enumerate these separately from record rules |
| `ER-TEN-1` | **`TENANT-BOUNDARY-SPECIFIC`** | Where no tenant entity exists in the domain, research can establish **what crosses a company boundary** and cannot establish **whether that is a tenant crossing**. Say which is which, every time. Do **not** let the second question absorb the first — every company-boundary fact must be established on its own evidence and then handed to the design decision |
| `ER-ACC-1` | **`ACCOUNTING-SPECIFIC`** | For every mechanism, ask the four balanced-but-wrong questions explicitly: *can debit=credit hold · can the ledger still look consistent · what independent control detects it · what evidence proves that control exists*. The fourth question is the one that is normally skipped, and it is the one that finds the gap |
| `ER-ACC-2` | **`ACCOUNTING-SPECIFIC`** | **Shipped demo data is a financial input.** Resolve every data file to `data` or `demo` in its manifest, and resolve every **absent field to the model default the loader applies**. A field absent from a data file is **not** absent from the loaded row — this round got that wrong and was corrected |

---

## 10. Proposed standard delta — for Boss ratification

| # | Delta | Target | Cost |
|---|---|---|---|
| `D-1` | Adopt `ER-CORE-1`: every denominator declares `POPULATION` + `PATTERN` + `PATH SET` + `UNIT`. **Reject any coverage percentage whose denominator lacks all four** | `SMEPLUS-DR-MC-001` §on enumeration | None — it is a rejection rule |
| `D-2` | Adopt `ER-CORE-3` correction propagation, including clause 5 (corrections can be wrong) | `SMEPLUS-DR-MC-001`, new section | Low — editorial |
| `D-3` | Adopt `ER-CORE-4` empty-cell rule: **a blank cell is forbidden** in any taxonomy or coverage register | both standards | Low |
| `D-4` | Adopt `ER-CORE-5`: independent review is a **discovery phase**, budgeted and scheduled inside enumeration, with disjoint assignments, at least one adversarial, and briefs that invite their own correction | `SMEPLUS-DR-MC-001` §on review | **This is the expensive one, and it is the one that works** |
| `D-5` | Adopt `ER-CORE-6`: cross-version claims require a file-level diff | `SMEPLUS-DR-MC-001` | Low |
| `D-6` | Adopt `ER-CORE-7`: prove the executor of every control | both standards | Low |
| `D-7` | Extend `DR-NC-02` so that **completeness assertions** (`complete`, `bounded`, `the population is N`, and the status words `ENUMERATED` / `CONVERGED`) are scanned as negatives. **Two of the parent's three false closures were status words, not sentences** | `DR-NC-01`…`06` | Low |
| `D-8` | Add `DR-NC-07`: **every negative declares its own false-negative modes.** A negative without them is class `B`, never `A` | `DR-NC-01`…`06` | Low |

---

## 11. Immediate hand-off to the other modules

**Run these first, in this order, before any new module's deep research begins.** All are mechanical,
all return bounded counts on first execution, and all are domain-independent.

| # | Rule | Why first |
|---|---|---|
| 1 | **Prove the path set** — enumerate the source root's module trees before searching any of them | This round found 962 modules outside the tree five rounds had been searching. **Cost: one `find`.** It invalidates the scope of every prior negative if skipped |
| 2 | `ER-16a` record-scoping coverage per model | Inherited from the MC round; still the cheapest, highest-yield rule |
| 3 | `ER-CORE-7` control-executor proof | Found 16 inert guards in one file |
| 4 | `ER-CB-1` root-vs-company guard enumeration | Found a tolerance-zero-severity class in an unassessed remainder |
| 5 | `ER-CORE-2` call-site-then-read | Defeats the pattern-truncation failure that has now occurred three times |

> **Total mechanical cost of the enumeration layer across the last two rounds: under two hours.**
> It produced 24 verified denominators, one bounded surface at 100% evidence, one closed root cause,
> three closed gating unknowns, four corrected gate findings, and two recovered tolerance-zero
> candidates. **The expensive part is not the enumeration. It is the independent review — and the
> independent review is what finds everything.**
