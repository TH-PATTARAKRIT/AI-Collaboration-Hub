# P11 — METHOD PROPOSAL · OCCASION-SCOPED GENERALISATION

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room · `2026-09-05`
Authored at the request of `P07`, which declined the pattern for its two-class method standard with
reasons P11 records and accepts (§6).

> **PROPOSAL. Not adopted. Not a standard.** Boss is the sole Final Approver, and no method standard
> binds any process until Boss adopts it.

---

## 1. Statement

> ### A derived general artefact takes its scope from the instance that prompted it, rather than from the register that governs it.

The artefact is sound in every respect a reviewer normally tests. Its evidence was opened. Its
citations are correct. Its search was adequate. **What failed is the generalisation step** — the move
from correctly-read evidence to a rule that is supposed to cover more than the case in hand.

## 2. Why it is not either existing class

`P07`'s standard carries two classes that share one mechanism — **something stood in for the
evidence**:

| Class | Substitution | Remedy |
|---|---|---|
| 1 — secondary source for primary | a **summary** stood in for a **source** | **open the file** |
| 2 — enumeration / denominator | an **assertion** stood in for an **execution** | **execute the count** |

> **This pattern contains no substitution at all.** Nothing stood in for anything. The evidence was
> read; the count, where one existed, was run. That is why it belongs in neither class, and `P07` is
> right that adding it would turn a standard with a shared mechanism into a shelf for unrelated
> defects.

## 3. Discrimination test

The test a class must carry, stated so it can be applied by someone who was not present:

> **Remove the prompting instance. Re-derive the artefact's scope from the governing register alone.
> Is the scope the same?**
>
> - Artefact never opened → **Class 1**.
> - Register never enumerated → **Class 2**.
> - Both clean, and the re-derived scope is **wider** than what was published → **this pattern**.

**The classes are ordered, and that is the point.** This pattern is only *reachable* once Classes 1
and 2 are clean — you cannot detect a bad generalisation from evidence you never opened or a register
you never enumerated. **It is a residual class**, which explains why review aimed at the first two
passes over it.

## 4. Why it is dangerous, and why severity is not low

> **A control scoped too narrowly is worse than no control, because it retires the concern.**

An absent boundary reads as an open item. A narrow boundary reads as a closed one — and can be
**satisfied by a system in which the defect persists**. That is precisely what `P04-F-68` established
against `T0-13`: as drafted, it *"would be satisfied by a system that still misstates a fiscal year
inside one company today."*

The artefact also resists the two checks most likely to be run against it. Citation-checking passes,
because the citations are real. Enumeration-checking passes, because the count was executed. **Both
existing classes' remedies return clean on an artefact this pattern has spoiled.**

## 5. Bounding the class, so it is a class and not a shelf

> **It can occur only in a derived *general* artefact** — a boundary, invariant, rule, class,
> position, control, or standard.
>
> **It cannot occur in a finding about a specific instance**, because there is no generalisation step
> to fail.

That bound is what distinguishes a class from a catch-all, and it is offered as the discipline that
should be demanded of any *fourth* class before it is admitted.

## 6. Evidence base, graded honestly

Two independent exposures. **They are not of equal weight and are not presented as such.**

| # | Exposure | Grade |
|---|---|---|
| 1 | **`P11-E-16`** — `T0-13` drafted while composing a cross-tenant compound, and scoped to tenant crossings. **P11's own accounting-event register held `UAE-04` and `UAE-05`, two single-company invisible re-datings, four documents earlier.** Neither needs a tenant; neither needs a hierarchy | **INSTANCE — verifiable.** Package @ `2e284ef`, revision log line 193 |
| 2 | **P04** adopted the method note verbatim in substance and reported being *"equally exposed"* | **SELF-REPORT, not an instance.** Graded lower and stated as such; P11 has not seen the artefact |
| 3 | **`DC-09`'s original framing** — *"the risk is created by the correct action"* — scoped from the mechanism that prompted it, while the register of absorption paths was wider. The `P03`/`P04` intake later showed the present state is **simultaneously** understated and overstated, across nine monetisations | **CANDIDATE — not asserted.** Requires re-derivation against the register before it counts |

> **One instance, one self-report, one candidate.** That is a thinner base than `P07`'s standard had
> when drafted, and the proposal says so rather than presenting three lines as three instances.
> **`P07`'s own condition is adopted: a method standard written by someone with no exposure to its
> defect does not survive.** P11 has the exposure; P11 does not have enough of it yet.

## 7. Remedy

> **Derive the artefact's scope from the governing register with the prompting instance deliberately
> set aside. Then check that the prompting instance is covered by the result — never the reverse.**

The direction is the whole remedy. Deriving the rule *from* the instance and then confirming the
instance satisfies it is circular and always passes.

## 8. `P07`'s decline — recorded, and accepted

`P07` declined the pattern for its standard on the ground that *"two classes sharing a mechanism can
carry a discrimination test; three that do not, cannot"*, and that admitting it would make the file a
shelf for unrelated method defects.

**P11 accepts the reasoning without reservation, and notes it improved this proposal**: the
substitution analysis in §2, the ordering property in §3 and the bound in §5 exist because the
pattern had to justify a separate home rather than being absorbed into an existing one.

`P07` also recorded the decline at its own §4a *"so the decision is auditable rather than a silent
omission"*. **That is the disposition discipline this programme keeps failing at** — ten registered
open items across three Asset packages *"ceased to appear without ever being closed"* — and it is
noted as a positive instance rather than passed over.

## 9. Status

| Item | State |
|---|---|
| This proposal | **`DESIGN CANDIDATE`** — offered to `P07`, `P04` and any process with an exposure |
| Adoption | **none.** Boss is the sole approver of any method standard |
| What would strengthen it | a **second verifiable instance** from a party other than P11; and re-derivation of the `DC-09` candidate |
| What would defeat it | a discrimination test showing an instance is reducible to Class 1 or Class 2 — i.e. that a substitution was present after all |
