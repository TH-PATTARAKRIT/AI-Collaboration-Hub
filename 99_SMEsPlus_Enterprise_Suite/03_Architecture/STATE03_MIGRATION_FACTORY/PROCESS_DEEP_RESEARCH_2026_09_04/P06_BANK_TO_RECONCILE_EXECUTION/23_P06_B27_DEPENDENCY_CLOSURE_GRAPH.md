# P06_B27_DEPENDENCY_CLOSURE_GRAPH.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Governing rule for this file:** *"If B-27 closes multiple blockers, close them ONLY after independently verifying that their dependency conditions are actually satisfied."*

---

## 1. The claimed dependency

The prior package asserted that `P06-B-27` gated three items: attack **A4a**, requirement **RM-R-10**, and scope requirement **SCOPE-R-02**. Each is tested below **on its own merits**, not inherited from B-27's closure.

```
                         P06-B-27  root_id semantics
                         CLOSED — SOURCE EVIDENCE VERIFIED
                                    │
             ┌──────────────────────┼──────────────────────┐
             ▼                      ▼                      ▼
          A4a                    RM-R-10               SCOPE-R-02
   cross-company            company isolation      declare the boundary
   reconciliation           tested at company_id         once
             │                      │                      │
      DEPENDENCY MET         DEPENDENCY MET        DEPENDENCY PARTIALLY MET
             ▼                      ▼                      ▼
     CONFIRMED DEFECT         REINSTATED            RESTATED, still a
     (not merely HOLD)     with new rationale       DESIGN DECISION
```

---

## 2. Per-item verification

### A4a — cross-company reconciliation between sibling branches

- **Dependency condition as stated:** *"whether companies sharing a `root_id` are branches of one legal entity or distinct legal entities."*
- **Is the condition satisfied?** **The condition was mis-specified, and the correct question is now answered.** B27-CONCLUSION establishes that `root_id` guarantees a shared fiscal calendar and currency but **imposes no constraint on `vat` or `company_registry`** (B27-F-04). The legal arrangement beneath a root is therefore *unconstrained by the model*.
- **Independent verification performed:** the guard itself was re-read. `$V18E/account/models/account_move_line.py:2336-2340` tests `len(self.company_id.root_id) > 1` and raises *"Entries don't belong to the same company"*. The test is on the fiscal grouping; the message names the company. Corroborated by the matching domain in the same flow using `child_of self.company_id.root_id.id` (`$V18E/account/models/account_bank_statement_line.py:518`) alongside `child_of self.company_id` at `:525` — two different boundaries in one code path.
- **DISPOSITION: CLOSED — SOURCE EVIDENCE VERIFIED. Classification restored to CONFIRMED DEFECT.**
- **Rationale, stated precisely:** the defect is **not** "the system lets distinct legal entities reconcile together" — that would be data-dependent. The defect is that **a control which names the company boundary is implemented against a different boundary, and is therefore structurally incapable of enforcing what it claims.** That holds for every deployment.

### RM-R-10 — company isolation must be tested at `company_id`, never at `root_id`

- **Dependency condition as stated:** the requirement presumed `root_id` never legitimately equals the company boundary.
- **Is the condition satisfied?** **Yes, and the presumption turns out to be correct — for a reason the prior round did not have.** `root_id` cannot equal the company boundary because it is a *fiscal* boundary that leaves legal identity free (B27-F-04).
- **Independent verification performed:** the requirement was re-derived from scratch rather than restored. A financial guard must test the boundary that owns the financial effect. Per the scope determination (Scope Matrix S-08, S-10), a journal entry and a reconciliation are **COMPANY**-owned. Therefore the guard must test `company_id`.
- **DISPOSITION: CLOSED — SOURCE EVIDENCE VERIFIED. RM-R-10 reinstated, with the rationale corrected.**
- **What changed in the requirement's wording:** the prior conditional form ("depends on what `root_id` denotes") is withdrawn. The unconditional form is restored, because the answer is now known.

### SCOPE-R-02 — the COMPANY boundary must be declared once and every financial guard must test it

- **Dependency condition as stated:** *"branch companies are either one legal entity or several"* — a declaration the design must make.
- **Is the condition satisfied?** **PARTIALLY.** B-27 removes the *ambiguity about what the reference model means*, but it does **not** make the SMEsPlus design decision. The target must still declare whether it will permit a company hierarchy at all, and if so what it means.
- **What B-27 does contribute:** it removes one bad option. A design cannot adopt the reference's fiscal-hierarchy guard and call it company isolation. That option is now evidenced as defective rather than merely doubtful.
- **DISPOSITION: HOLD — DESIGN DECISION REQUIRED.** **Not closed.** Reclassified from `HOLD — SCOPE EVIDENCE REQUIRED` (which is now satisfied) to `HOLD — DESIGN DECISION REQUIRED` (which is not).
- **This is the discipline the governing rule demands:** two of three dependents close on evidence; the third does not, because evidence was never what it was waiting for.

---

## 3. Second-order items examined and NOT closed

Items that touch `root_id` but whose dependency on B-27 was **not** asserted by the prior package. Each was checked so that no closure is claimed by association.

| Item | Touches `root_id`? | Closed by B-27? | Reason |
|---|---|---|---|
| A4b — unowned bank account (`company_id = False`) | no | **NO** | Independent of the hierarchy entirely; it concerns objects with *no* company. Remains CONFIRMED DEFECT on its own evidence. |
| A4c — payment token visible via `parent_of` | yes, indirectly | **NO** | `parent_of` is an *ancestor* test on a record rule, not `root_id`. Separately revalidated — see `31_`. |
| C-13 — two boundaries in one code flow | yes | **defect classification restored** | The contradiction never depended on B-27; only its severity did. |
| `P06-B-26` — unowned bank accounts | no | **NO** | As A4b. |
| `P06-B-28` — token scope | partly | **NO** | Separate evidence. |
| Payment-register wizard root-scoping (`account_payment_register.py:953-956`) | yes | **newly implicated** | Same defect shape as A4a, in a second location. Raised as **`P06-B-43`** rather than folded silently into A4a. |

**`P06-B-43` is a new blocker produced by this closure.** A targeted closure round that only ever removes blockers is not doing forensic work; resolving `root_id` made a second instance of the same defect legible.

---

## 4. Closure ledger for this graph

| ID | Prior status | New status | Evidence class |
|---|---|---|---|
| `P06-B-27` | HOLD — SCOPE EVIDENCE REQUIRED | **CLOSED** | SOURCE EVIDENCE VERIFIED |
| A4a | HOLD — SCOPE EVIDENCE REQUIRED | **CLOSED as a finding** — CONFIRMED DEFECT | SOURCE EVIDENCE VERIFIED |
| RM-R-10 | conditional | **CLOSED** — reinstated unconditionally | SOURCE EVIDENCE VERIFIED |
| SCOPE-R-02 | HOLD — SCOPE EVIDENCE REQUIRED | **HOLD — DESIGN DECISION REQUIRED** | not closed |
| C-13 | severity HOLD | **severity HIGH restored** | SOURCE EVIDENCE VERIFIED |
| C-29 | — | **newly raised** | SOURCE EVIDENCE VERIFIED |
| `P06-B-43` | — | **newly raised** | SOURCE EVIDENCE VERIFIED |

**Net effect on the blocker population: −1 closed (B-27), +1 raised (B-43). Population unchanged at 42.**
Stated plainly because the objective is evidence-based reduction, not a lower number: **this closure improved the package's accuracy without improving its count.**

---

## 5. What the next process needs from this

- **P08 (GL / Period Close)** — currently unpublished. The lock-date inheritance finding (B27-F-05: the strictest ancestor wins, and lock dates are *not* delegated) is a direct input to close architecture. Recorded as **PEER DEPENDENCY OPEN**.
- **P11 (Whole Accounting Reconciliation)** — must reconcile P06's company-boundary position against every peer's. P06's position is now unambiguous: **the financial boundary is COMPANY; the hierarchy is a TENANT-scoped grouping; no financial guard may be written at the grouping level.**

---

# End
