# P01 — PMO REVIEW

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1.**
Test applied: **SMEsPlus Very Deep Research 8-Criteria Universal Exit Constitution**
(`SMEPLUS-DR-EXIT-8C-001`), as amended by the scope-aware correction
`SMEPLUS-26-09-04-ACC-REV2-CORR1`.

PMO may issue only a recommendation. **Boss alone decides.**

---

## 1. THE EIGHT CRITERIA

### `EC-01` — Scope Bounded → **NOT SATISFIED**

Bounded and reproducible: the source path set (five roots, with every other root on the volume
explicitly recorded as not searched); three source-derived populations each with population,
unit, pattern, declared false-negative modes and path set; the journal-entry creation-site
population, declared **a floor rather than a total**; the deployed-schema evidence.

Not bounded: the **function** population is declared `UNBOUNDED / NOT YET ENUMERABLE`, and this
package therefore publishes **no coverage percentage** anywhere. That is the correct behaviour
under the denominator rule, and it is also the reason this criterion is not satisfied.

The module denominator was also **wrong during the session** and was corrected by an
independent expert, not by the author: it was a direct-dependency set rather than a transitive
closure, and it omitted landed costs and subcontract purchase — both named explicitly in the
directive (`ERR-P01-04`).

### `EC-02` — Enumeration Converged → **NOT SATISFIED**

The session did not converge; it **diverged**. Contradictions rose from six to eleven. A new
material evidence class — deployed database schemas — appeared late, from outside the declared
evidence base, and immediately changed the severity of the session's central finding. Four
enumeration or citation defects were found *inside* the session (`ERR-P01-01`..`-06`).

Convergence requires material-delta stability. There was none.

### `EC-03` — Unknown Exhausted → **NOT SATISFIED**

Six gating dependencies and seven scope questions remain open, each classified rather than
hidden, and none routed to a later wave to disguise a current-scope blocker. But `DEP-P01-01`
— which generation and copy is deployed — is **gating and unresolved**, and it is a
current-scope question.

### `EC-04` — Tolerance-Zero Closed → **NOT SATISFIED**

At least four tolerance-zero boundaries are open:

1. **Company / tenant isolation.** A company-scoped financial effect is created in a company
   whose ownership is inferred from a tenant-scoped contacts hierarchy, resolved with elevated
   privilege, superuser by default, optionally auto-posted; **no tenant test found** (class B).
2. **Immutable posted facts.** Reset-to-draft and cancel **delete** derived journal items.
3. **Financial integrity.** A soft period lock **rewrites the date** instead of refusing.
4. **Unauthorised / duplicate posting.** Order reset-to-draft is unguarded; bill-to-order
   matching does not test the vendor on the reference branches and then **replaces the
   vendor's own bill lines**.

`EC-04` states plainly that a conditional outcome may not bypass a tolerance-zero risk.

### `EC-05` — Contradiction Resolution Complete → **NOT SATISFIED**

Eleven contradictions, all dispositioned with evidence and lineage, **none closed**. Two are
Boss decisions, one needs runtime evidence, one needs statutory evidence, one needs both.

### `EC-06` — Negative Claim Controlled → **SATISFIED, with a caveat**

Every material negative in this package carries a class letter and a stated scope. No class B,
C or D is restated as class A anywhere, including in summaries — the place the standard
identifies as where the upgrade happens. A mechanical scan was run before commit.

**Caveat, and it is a real one:** the session produced **six fabricated class-A absences** in a
single probe run and caught them only because the probe printed the size of what it searched
(`ERR-P01-06`). Two independent experts hit the same class of tooling artefact. The control
worked three times out of three, but it was a *deliberate* control each time, not a systemic
one.

### `EC-07` — Two Consecutive Clean Independent Passes → **NOT SATISFIED**

Not two. Not clean. **One partial pass.**

- Four independent experts on disjoint assignments; three returned before this review began,
  the fourth during it.
- The pass produced **new material populations**, **new finding classes**, **new gating
  unknowns**, and **a new evidence class** — the definition of *not clean* under `EC-07`.
- Every admitted expert finding was independently re-derived by this session, honouring
  *Independent Review ≠ Truth*. Those not re-derived are labelled SUPPORTED INTERPRETATION.
- The briefs were issued **before** the scope-aware correction and it **could not be
  forwarded** (`REV-P01-02`, `DEP-P01-06`). A pass performed under a superseded constitution
  cannot count as a clean pass under the corrected one.
- **An expert may have suppressed a legitimate observation as "missing company scoping" under
  the superseded reading. Suppression is invisible to a re-read.** That asymmetry is unrepaired.

### `EC-08` — Final Knowledge Package Complete → **SUBSTANTIALLY SATISFIED**

All twenty-one deliverables named in the directive are present, plus two the session added:
the scope matrix required by the correction, and the deployed-schema evidence. Registers,
evidence manifest, contradiction and dependency registers, revision log and expert challenge
are all present, with repository, branch, path and commit recorded.

Missing from completeness: runtime evidence and statutory evidence, both of which the package
declares rather than conceals.

---

## 2. SCORE

| Criterion | Outcome |
|---|---|
| `EC-01` Scope Bounded | **NOT SATISFIED** |
| `EC-02` Enumeration Converged | **NOT SATISFIED** |
| `EC-03` Unknown Exhausted | **NOT SATISFIED** |
| `EC-04` Tolerance-Zero Closed | **NOT SATISFIED** |
| `EC-05` Contradiction Resolution Complete | **NOT SATISFIED** |
| `EC-06` Negative Claim Controlled | **SATISFIED, with caveat** |
| `EC-07` Two Clean Independent Passes | **NOT SATISFIED** |
| `EC-08` Final Knowledge Package Complete | **SUBSTANTIALLY SATISFIED** |

**Six of eight not satisfied.**

---

## 3. PMO RECOMMENDATION

> ### `RECOMMEND HOLD`

Not `RECOMMEND PASS`. Not `RECOMMEND CONDITIONAL PASS` — that outcome is unavailable here,
because `EC-04` forbids using it to pass over a tolerance-zero risk and four are open.
Not `RECOMMEND FAIL` — the research is sound, reproducible and materially advanced; it is the
*evidence base*, not the work, that is incomplete.

**This is a recommendation only. Boss is the Sole Final Approver.**

---

## 4. WHAT THE SESSION NONETHELESS DELIVERED

Stated because `HOLD` should not be read as "nothing was learned".

- The receipt-to-bill bridge traced end-to-end, with five distinct ledger patterns identified
  behind one document set.
- **A structural divergence between reference generations confirmed at the deployed-schema
  level** — the clearing account and the valuation-layer table are absent from both readable
  v19 databases. This independently reproduces, in the liability bridge, the instability the
  COGS track recorded in the valuation pattern.
- Eleven contradictions raised, evidenced and dispositioned.
- Four silent-failure paths identified, each of which loses value or history with no error.
- A tolerance-zero cross-company trigger identified and correctly re-framed under the
  scope-aware correction.
- A verified arithmetic defect in the project's own withholding layer, and an inversion between
  two shipped copies that means at least one misclassifies every certificate.
- Six research defects found and logged **inside** the session rather than shipped.

---

## 5. THE HONEST METHOD FINDING

Of the six defects in this session's own work: **five were caught by the author, one by an
independent reviewer — and the one caught from outside was the only one that changed a
denominator.** The author's five were caught by mechanical self-checks deliberately built into
each step (re-resolving every citation; printing the size of what a probe searched; questioning
implausible counts). The reviewer's one was caught because the expert brief carried the
instruction *"if any path in this brief is wrong, report it as a finding"* — and that same
instruction also caught two wrong field names **in the brief the author wrote**.

The programme's standing conclusion holds, with a refinement worth recording:

> Mechanical self-checks materially raise the number of the author's own defects caught, and
> they still do not find the ones that are invisible from inside the author's frame — the
> boundary of a population, and the correctness of the author's own instructions.
> **Independent review remains the only control that has found those.**
