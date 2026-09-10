# VDR_HOP0_CANONICAL_POPULATION_REGISTER.md
# Hop-0 rebuilt from two independent methods — 5,074 → 24,553

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoints 02 / 04.

---

## 1. What Hop-0 means here, and why it was rebuilt

**Hop-0 is the complete immediate functional and technical surface of the target domain, before any
one-hop or two-hop expansion rule is applied.** Two rounds argued about hop 1 and hop 2; a challenger
then showed the population was incomplete at hop 0 — surface that never entered the relational graph
could not be reached by any hop rule.

**Nothing was assumed from the prior population.** It was reconstructed from scratch by two methods and
then reconciled against it.

## 2. The declared domain rule — a property test, fixed before enumeration

| | |
|---|---|
| **ANCHOR** | the domain's own core module |
| **ANCHOR SET** | every model the anchor **declares** — **51 models** |
| **DOMAIN SET** | every module that **declares or extends** a model in the anchor set, plus the anchor — **99 modules** of 1,433 |

This is a property test over source, not a name test, and **it can fail** — a module whose name looks
domain-related but touches no anchor model is excluded, and one whose name does not is included.

**It is also narrower than the rule prior rounds used**, which named 137 modules. §5 of this register
records what that costs.

## 3. Method 1 — SOURCE

| Clause | Value |
|--------|-------|
| **PATTERN** | Python AST for code entities; XML tree parse for declarative entities; CSV parse for access lines. **No regular expression decides membership** |
| **UNIT** | one declared entity |
| **COVERAGE** | **12,075 Python files parsed, 0 failures · 660 XML files parsed, 0 failures · 44 security files** |
| **RESULT** | **12,092 declared entities** |

## 4. Method 2 — RUNTIME

| Clause | Value |
|--------|-------|
| **PATTERN** | COPY-block parse of the deployments' own registries; **rows whose field count differs from the declared column list are rejected and counted, never padded** |
| **UNIT** | one registry record |
| **PATH SET** | five deployment identities across three generations |
| **RESULT** | 6,216 · 6,159 · 6,123 · 3,833 · 3,337 domain-attributed records per deployment |

> ### Independence — as an independent validator corrected it
> The two methods are **independent in OBSERVATION**: different evidence bases, and neither derives an
> entity from the other. They are **NOT independent in POPULATION**: method 2 opens method 1's output to
> obtain the domain module set. Perturbing that set moved method 2's output by **74.6%**.
>
> **Consequence, stated plainly: the agreement rate has zero power against an error in the shared
> scope.** A module wrongly included or excluded by method 1 is invisible to it. A runtime-native module
> set was available on all five deployments and was not used. The header sentence claiming full logical
> independence is **withdrawn**.

## 5. The population

| | |
|---|---|
| **HOP-0 CANONICAL POPULATION** | **24,553 rows — 20,326 distinct identities.** The headline double-counts **4,227** (a field appearing in both the xmlid-attributed stream and the wider surface). *Corrected by independent challenge.* |
| Prior population (PREP-005) | 5,074 rows / 4,699 distinct identities |
| **Newly discovered** | **17,429** |
| Prior identities **not** in the new Hop-0 | **1,802** |

| Kind | Total | Both methods | Source only | Runtime only |
|------|------:|-------------:|------------:|-------------:|
| Field on a domain model, any owner | 11,158 | — | — | 11,158 |
| Field declared by a domain module | 5,134 | 2,632 | 640 | 1,862 |
| Behaviour | 4,096 | — | 4,096 | — |
| Data record | 1,490 | 105 | 764 | 621 |
| View | 1,091 | 791 | 223 | 77 |
| Access line | 406 | 312 | 46 | 48 |
| Model | 281 | 157 | 41 | 83 |
| Window action | 225 | 182 | 28 | 15 |
| Menu | 172 | 137 | 22 | 13 |
| Model extension | 129 | — | 129 | — |
| Constraint | 87 | — | 46 | 41 |
| Record rule | 73 | 67 | 4 | 2 |
| Server action | 63 | 48 | 5 | 10 |
| Report action | 44 | 36 | 5 | 3 |
| Group | 43 | 27 | 12 | 4 |
| Client action | 23 | 20 | 1 | 2 |
| Scheduled job | 20 | 10 | 10 | — |
| Sequence | 13 | 9 | 2 | 2 |
| Configuration parameter | 5 | 4 | 1 | — |

## 6. The agreement rate — and the only valid basis for it

Three kinds are **structurally single-method**: behaviours and model extensions are not registry
records and are invisible to runtime; fields owned by other modules on domain models are invisible to a
source enumeration of *this* domain. Counting those as disagreement would manufacture a number.

| Over the **9,170 entities both methods can see** | |
|---|---:|
| found by **both** | **4,537 — 49.5%** *(see the version-basis correction below)* |
| source only | 1,850 — 20.2% |
| runtime only | 2,783 — 30.3% |

> ### Version basis — declared after an independent validator found it missing
> The five deployments span **three platform generations** (three at 19.0, one at 18.0, one at 16.0)
> and the source tree is **19.0**. **765 of the 2,783 comparable runtime-only rows (27.5%) exist only on
> an off-version deployment** and were scored as method disagreement.
>
> | basis | agreement |
> |---|---:|
> | as published, five deployments | **49.5%** |
> | **the three current-generation deployments only** | **53.9%** |
>
> **53.9% is the figure on a constant basis.** Neither reaches a level at which the population could be
> called corroborated, and the mixed-basis figure may not be cited without this table.

> **Two independent methods, applied to the same domain, agree on roughly half of what they find.**
> §8 states that a population is not certifiable if its discovery methods do not corroborate one
> another. **This population is therefore NOT CERTIFIED**, and it is reported as such rather than
> published as a denominator.

## 7. Two instrument defects caught before publication

**Both were caught by disbelief at a clean result, not by a reviewer.**

1. **A population mismatch.** *Every field on a domain model* (runtime) was about to be compared against *every field declared by a domain module* (source). Those are different populations, and the resulting disagreement would have been an artefact of the mismatch. The wider runtime set is now carried separately and named for what it is.
> **And a third, which an independent validator found and the author did not:** the same namespace
> mismatch is **unfixed for constraints** — 46 source-only, 41 runtime-only, **0 both** — the identical
> artefactual disagreement, present in a third namespace and left inside the comparable denominator.
> The normaliser also silently drops real matches: **48 rows would flip from disagreement to agreement**
> under a correct map.

2. **A namespace mismatch.** The two methods name the same thing differently — a runtime field is `<module>.field_<model>__<field>`, a source field is `<model>.<field>`. Compared unnormalised **they can never match, and agreement would have read 0% — a perfect, entirely artefactual disagreement.** A normaliser was written, with a control: 2,632 runtime identities land on a source identity, and a fabricated one does not.

Both are recorded because the *first* run of each produced a plausible, publishable, wrong number.

## 8. What this register does not claim

- **Not certified.** 49.5% corroboration is the finding, not a footnote.
- **Not a denominator.** No coverage figure in this package uses it as one.
- **Not complete.** An independent challenger was tasked with the question *what exists at Hop-0 that this enumeration missed*, and its answer is in `VDR_HOP0_INDEPENDENT_CHALLENGE_REPORT.md`.
- **Narrower than its predecessor in one direction.** 1,802 prior identities are absent. **An earlier
  edition of this sentence said they "fall outside the anchor rule" — that was false and the
  reconciliation matrix in this same package refutes it: only 215 do.** Decomposed by an independent
  challenger: **1,568 of the 1,802 (87%) belong to modules that ARE in the 99**, 670 are pure
  identity-scheme artefacts, and **1,132 are genuinely absent in any form** — 383 buttons, 371 gated
  elements, 178 access grants and others.
- **The reconstruction is incomplete inside its own declared domain.** An independent challenger
  measured a **floor of 6,104 entities** the enumeration does not carry — 3,921 of kinds it never looked
  for (buttons, gated elements, selection values, compute dependencies, defaults, client templates,
  onchange and constraint triggers, HTTP routes), 1,536 declared in non-domain modules but targeting
  domain models, 103 live access grants, and 544 registry records from custom modules outside the
  declared source path set.
- **The evidence base is not the whole of it.** **11 generation-19 databases are live in a running
  container on this host**, reachable by no filesystem search, and were never enumerated. The sweep
  script that chose the five is in the package; **its output is nowhere on disk**, so the choice of five
  has no recorded provenance.
