# 01 — ACCOUNT WAVE A — METHOD CONVERGENCE SCOPE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room · cites `MCE-0NN`
Standard applied: `SMEPLUS-DR-MC-001` (`SMEPLUS_DEEP_RESEARCH_METHOD_CONVERGENCE_STANDARD.md`)
Parent: `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Programme: `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`

---

## 1. Why this round exists

The parent gate report `G10` §6 states the position exactly:

> The package has three times declared a set of findings complete and three times had material
> additions found by independent review. The correct conclusion is not that the current list is
> right; it is that the enumeration method has not yet converged.

That is blocker `GB-04`. Trigger conditions 1, 2, 3 and 4 of the standard §2 are all met.

**This round does not search for more findings.** Its object is the *method*: to establish whether
the Wave A research universe is bounded, systematically enumerated, independently repeatable, and
converged — and where it is not, to name the exact enumeration defect.

## 2. What is in scope

| In scope | Out of scope |
|---|---|
| Defining the Wave A enumeration universe and its verified denominators | Finding new Wave A findings for their own sake |
| Diagnosing `GB-04` to root cause | Re-litigating `GB-01`, `GB-02`, `GB-03` — these are Boss design decisions, not research questions |
| Converting reviewer-discovered finding classes into deterministic enumeration rules | Any Wave B–H research |
| Classifying every remaining unknown | Implementation, design, or source-code change of any kind |
| Re-testing tolerance-zero boundaries | Declaring Wave A closed |
| Negative-claim convergence over the **whole** package | Boss approval of anything |
| Building the balanced-but-wrong taxonomy before counting instances | |
| Executing `MC-01` … `MC-10` | |

## 3. Wave A boundary, fixed

Wave A is **Core Ledger & Closing**: chart of accounts · journals · journal entries · journal items ·
reconciliation · lock dates · fiscal years and closing · currencies and FX.

Deliberately outside Wave A, with destination named:

| Excluded | Destination |
|---|---|
| Customer invoicing, revenue | Wave B |
| Vendor bills, expense | Wave C |
| Tax computation, localization | Wave D |
| Analytic / management accounting | Wave E |
| Deferrals, accruals, time-based recognition | Wave F |
| Financial statements and report layer | Wave G |
| Payments, bank statements, banking | Wave H |

An item is Wave A if it determines **ledger identity, ledger measurement, ledger period control, or
ledger integrity**, regardless of which module raises it.

## 4. Baseline under re-validation

The parent figures are **inputs to be tested**, not accepted facts. Re-validation results are in
file `03`; the headline outcome is recorded here because it governs everything downstream:

| Parent claim | Re-validation result |
|---|---|
| Function coverage `104/155 = 67.1%` | **Denominator is not source-derived, and the figure is not reproducible from the register's own rows** — see `MCE-010` |
| Evidence coverage `148/155 = 95.5%` | Same denominator defect; the ratio is internally consistent but measures a hand-authored taxonomy, not the system |
| Contradiction resolution `16/16 = 100%` | Referred to independent review — file `10` |
| Prior blocker closure `4/4 = 100%` | Accepted; re-verified by `GR1` in the parent round |
| Remaining unknowns `41` | Re-enumerated and classified — file `06` |
| Negatives rescoped `26` | Accepted; **but the scan covering them reached only 41.9% of the package** — `MCE-011` |
| Balanced-but-wrong `27`, a floor | Accepted as a floor; taxonomy built first — file `08` |

## 5. Method

1. Fix the Wave A boundary (§3).
2. Enumerate populations from **primary source structure**, not from a written taxonomy. Every
   denominator must be produced by a single-pass mechanical command over a declared path set.
3. Where a denominator cannot be proven, mark the population `UNBOUNDED / NOT YET ENUMERABLE` and
   state no percentage.
4. Diagnose `GB-04` by comparing the populations the author enumerated against the populations the
   reviewers' findings actually came from.
5. Convert every reviewer-discovered finding class into a deterministic enumeration rule.
6. Classify unknowns; close the gating ones or stay on `HOLD`.
7. Re-test tolerance-zero boundaries.
8. Apply `DR-NC-01`…`DR-NC-06` to the **whole** package, not a subset.
9. Build the balanced-but-wrong taxonomy, then enumerate against it.
10. Execute `MC-01`…`MC-10`.
11. Fresh independent convergence review by reviewers who did not author this package.
12. Recommend a gate status. Recommendation only.

## 6. Evidence and layering

Primary-source citations (`file:line`), vendor model names and framework tokens are held in
`LAYER2_MC_EVIDENCE/MCE00_ENUMERATION_PRIMARY_EVIDENCE.md`, **Layer 2 / audit quarantine**.
Every Layer 1 file in this directory cites `MCE-0NN` and is vendor-token free, per the Clean Room
Learning Directive. A mechanical token scan of the Layer 1 outputs is recorded in file `12`.

## 7. Standing constraints observed

`No Evidence = No Progress` · `Never Skip Gate` · Boss is sole Final Approver.
This round does not start Wave B, does not implement, does not merge, does not deploy, and does not
declare a gate outcome. It recommends only.
