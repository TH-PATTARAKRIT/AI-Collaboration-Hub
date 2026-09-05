# P01 — `EC-06` DETERIORATION FORENSIC

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.**

---

## 1. THE AUTHORITATIVE DEFINITION — RETRIEVED, NOT INFERRED

From the Very Deep Research 8-Criteria Universal Exit Constitution:

> **`EC-06` — Negative Claim Controlled.**
> All material negative claims must comply with the Negative Claim Control.
> `NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.`
> Every material statement such as `never`, `always`, `cannot`, `does not exist`,
> `not supported`, `no validation`, or similar system-wide negative **must declare and prove the
> search boundary proportional to the claim.**
> Allowed classifications: `VERIFIED ABSENCE` · `NOT FOUND IN SEARCHED SCOPE` ·
> `NOT YET SEARCHED` · `UNKNOWN` · `CONTRADICTED`.

The operative words are **"declare and prove"**. Declaring a boundary is half the criterion.
**Proving it is the other half, and that is where P01 failed.**

---

## 2. PRIOR STATE vs NEW STATE

| Round | `EC-06` | Basis |
|---|---|---|
| Round 2 | **SATISFIED, with a caveat** | Every material negative carried a class letter and a stated scope; no class B/C/D was restated as A; a mechanical scan ran before commit. Caveat recorded: six fabricated class-A absences had been produced by an empty extraction and caught by a size guard |
| Round 3 | **NOT SATISFIED** | Three published claims were found **false** |
| **This round** | **NOT SATISFIED — and the diagnosis is now precise** | See §3 |

---

## 3. WHY IT DETERIORATED — THE MATERIAL DELTA

The three false claims all had the same shape:

> *"X is **not installed in any readable deployment**"*

Against the criterion:

| Criterion requirement | P01's performance |
|---|---|
| Declare the search boundary | **Done, every time.** The claims said *"any readable deployment"* — an honest, explicit bound |
| Classify correctly | **Done.** They were framed as bounded absences, not universal ones |
| **Prove the boundary** | **NOT DONE.** *Readable* was decided by a **single failed invocation of one tool**, never tested against the tools actually installed |

> **The deterioration is not a decline in discipline. It is the discovery that the discipline
> was operating on an unproven boundary.**

The criterion says *declare **and prove** the search boundary*. P01 had been reading it as
*declare the search boundary* for three rounds. The three false claims are what that costs.

### The second-order finding

Round 2 rated itself **SATISFIED** under the same practice that produced the round-3
falsifications. So `EC-06` was **never actually satisfied** — round 2's rating was itself wrong,
and the criterion did not deteriorate so much as **become correctly measured for the first
time**.

That is the honest reading, and it is worse than "it got worse".

---

## 4. WHAT THIS ROUND DID ABOUT IT

| Action | Effect |
|---|---|
| The excluded archive was opened with an already-installed tool | **The boundary that failed was repaired** |
| Two further evidence-base defects were found by the author — one archive pair being a single deployment, one superlative stated without its axis | Both were **boundary defects, not reasoning defects** — the same family |
| A tool-capability step was added ahead of every absence claim | Now embedded in the governing directive as §7.2 |
| Every remaining "not found" in the package was re-checked for a **proven**, not merely declared, boundary | See §5 |

---

## 5. CLOSURE REQUIREMENT

`EC-06` cannot be marked satisfied until **every material negative in the package has a boundary
that was proven, not merely stated.** Concretely, that means:

| # | Requirement | Status |
|---|---|---|
| 1 | Every absence claim names the tools enumerated, not just the tool used | **partially done** — done for the database evidence, not audited across all source claims |
| 2 | Every "not installed" claim names the deployment population and proves it is complete | **done** for the module population — four archives, three deployments |
| 3 | Every "no source found" claim proves the path set is complete | **DONE THIS ROUND.** The series-16 **custom** root was located and searched — it is the source of the deployment's custom layer, six of six versions matching. The series-16 **core** was then searched for across the whole volume and all unextracted archives by release-version declaration: **12 core trees, 4 at series 19, 8 at series 18, 0 at series 16.** `VERIFIED ABSENCE`, class A, false-negative modes declared |
| 4 | Every zero carries the size of what was searched **and** the relevant sub-population | **partially done** |

**Item 3 is now closed, and closing it is the strongest evidence that the criterion is
understood.** The same question — *is the path set complete?* — was asked properly this time:
the instrument was enumerated, the pattern declared, the false-negative modes stated, and the
result is a genuine `VERIFIED ABSENCE` rather than an untested assumption.

**Items 1 and 4 remain open**, and item 2 is done. `EC-06` therefore moves from *four unfinished
boundary proofs* to **two**.

---

## 6. EXTERNAL / PEER DEPENDENCY

None. **`EC-06` is entirely within P01's control to fix**, and P01 has not yet fixed it.

That distinguishes it from most other open criteria, which wait on runtime access, statutory
sources or Boss decisions.

---

## 7. STATUS

> **`EC-06` — NOT SATISFIED — METHOD.**
>
> Not blocked by evidence, tooling, peers or Boss. Blocked by **four unfinished boundary
> proofs**, of which the series-16 source root is the largest and is reachable today.
