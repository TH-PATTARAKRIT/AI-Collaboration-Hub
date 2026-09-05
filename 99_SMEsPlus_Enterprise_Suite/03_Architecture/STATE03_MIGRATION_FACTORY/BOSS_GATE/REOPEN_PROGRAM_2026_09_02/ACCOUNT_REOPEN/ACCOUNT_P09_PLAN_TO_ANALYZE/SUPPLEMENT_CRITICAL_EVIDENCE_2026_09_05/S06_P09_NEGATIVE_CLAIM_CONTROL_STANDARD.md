# S06 — P09_NEGATIVE_CLAIM_CONTROL_STANDARD

**Checkpoint:** `CP-P09S06` · **Layer:** 1 — clean-room. **Issued for adoption across all SMEsPlus Deep Research processes.**

---

## 1. WHY THIS EXISTS

The programme already carries a negative-claim standard: *no evidence found ≠ function does not exist*, with classes A–E and declared boundaries. **P09 satisfied that standard and still produced a false negative**, twice:

| Failure | All four denominator components declared? | What defeated it |
|---|---|---|
| "no deployment carries an allocation" | **yes** | the listing command's **output limit** |
| "budget consumption nets to zero on a Thai-chart install" | **yes** | a **template read promoted to a deployed claim** without querying the deployment |

**Neither was a discipline failure. Both were failures of things the discipline did not cover.** This standard covers them.

## 2. THE PROTOCOL — SEVEN STEPS BEFORE ANY "ABSENT"

1. **Declare the denominator** — population, pattern, path set, unit. *(existing rule, retained)*
2. **Enumerate exhaustively.** No `head`, `tail`, sampling, `limit`, or first-N command may bound a population. Where a listing is wanted for readability, produce the **count separately from the listing** and cite the count.
3. **Record the command and its result count**, verbatim, in the artefact.
4. **Verify no shell expansion, glob failure, quoting error or output limit altered the population.** State explicitly that this was checked.
5. **Run a positive control** — demonstrate the same pattern *can* fire, on data known to contain the thing. A pattern that cannot fire returns silence indistinguishable from absence. *(existing rule, reinforced)*
6. **Independently challenge the absence.** A negative bounding a headline claim requires a reviewer whose brief is to find the counter-example.
7. **State the evidence boundary** and the class letter.

## 3. THE TWO NEW RULES THIS SESSION ADDS

> **NC-8 — A negative result is only as good as the command that produced it, including its output limits.**
> An enumeration that bounds a claim must be run unbounded, or must report its count separately from its listing.

> **NC-9 — A finding about a template, a default, a fixture or a configuration file is a claim about CONFIGURATION CAPABILITY, never about DEPLOYED BEHAVIOUR, unless the deployment is measured.**
> Promoting the first to the second is a scope error even when the template reading is perfectly correct.

## 4. APPLIED TO EVERY REMAINING MATERIAL NEGATIVE IN P09

| Claim | Re-tested under this protocol | Result |
|---|---|---|
| no account-type filter on the management-record creation path | exhaustive pattern over the whole reference root, positive control fired | **CONFIRMED**, class A — see `S04` |
| no deployment uses the shipped Thai template accounts | exhaustive over all 339 account records of the only populated deployment | **CONFIRMED**, class A within that deployment |
| no deployment holds budgets | exhaustive over both budget tables | **CONFIRMED**, class A within that deployment |
| no asset outside deployment S carries an allocation | exhaustive over every asset row of all five readable databases | **CONFIRMED**, class A |
| the analytic surface is absent from the archive addons root | prior round, pattern-measured | **retained**, class A |
| no custom module overrides the depreciation, accrual or cash-basis paths | prior round, reviewer-measured with declared archive-file residue | **retained**, class A with class-C residue |

**No class B, C or D anywhere in the P09 package has been converted to A by this supplement.**

## 5. WHAT THIS STANDARD CANNOT DO

It cannot make an unsearched thing searched. `NC-8` and `NC-9` prevent two specific ways of being confidently wrong; they do not bound the residue that was never opened. The declared class-C items in the package remain class C, and the supplement's own sweeps declare their own residues.

## CHECKPOINT

**`CP-P09S06` — COMPLETE — EVIDENCE VERIFIED.** Protocol issued; two new rules; six material negatives re-tested. Auto-continue.
