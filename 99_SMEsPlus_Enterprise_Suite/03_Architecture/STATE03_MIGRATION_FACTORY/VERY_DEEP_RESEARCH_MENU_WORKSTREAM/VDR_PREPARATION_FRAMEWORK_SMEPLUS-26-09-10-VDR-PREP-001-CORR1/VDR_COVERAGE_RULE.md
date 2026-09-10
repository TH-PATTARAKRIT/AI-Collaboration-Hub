# VDR_COVERAGE_RULE.md
# SMEsPlus Universal Very Deep Research — Coverage Rule (Preparation Control 03)

Session: `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
Parent: `[SMEPLUS-26-09-10-VDR-MENU-NS-001]` · Workstream `ERPPLUS-153` · Governance `ERPPLUS-152`
Layer: **LAYER 1 — CLEAN-ROOM.** No reference-vendor identifiers appear in this file.
Status: **FROZEN v1.0 (this session)** — corrections from the Inventory Pilot are recorded in
`VDR_FRAMEWORK_PILOT_CORRECTION_REGISTER.md` and are already incorporated below.

---

## 1. Why this rule exists

A coverage percentage is a claim about a **population**. Publishing a percentage without publishing
its denominator, and without publishing how that denominator was produced, is not a measurement — it
is an assertion with a number attached to it.

Every SMEsPlus coverage figure must therefore be traceable to a denominator that a second party can
independently regenerate from primary evidence.

---

## 2. The Denominator Contract — five mandatory clauses

No coverage percentage may be published unless all five clauses are declared **and executed**, and the
executed command plus its output are preserved as evidence.

| # | Clause | Meaning | Failure mode it prevents |
|---|--------|---------|--------------------------|
| D1 | **POPULATION** | The set of things being counted, defined by a rule, never by an author's list | Author-chosen scope presented as a census |
| D2 | **PATTERN** | The exact search expression / parse rule that selects members | A pattern that is declared but never run |
| D3 | **PATH SET** | The exact root list searched, and the exact exclusions, with reasons | Evidence present on the host but outside the search |
| D4 | **UNIT** | What one counted row *is* (one menu? one element? one occurrence?) | Instances counted as actors; occurrences counted as history |
| D5 | **ELIGIBILITY** | Why every member of the population is admissible, and what was excluded and on whose authority | Exclusion errors, which are invisible by construction |

**A clause that is written but not executed does not satisfy this contract.** Publish the command and
its output, not the intention.

---

## 3. Instrument Validation Contract — four mandatory controls

A denominator produced by a defective instrument is not a denominator. Each of the following must be
performed and recorded for **every** extractor that contributes to a published count.

| # | Control | Requirement |
|---|---------|-------------|
| I1 | **Second-shape count** | Reproduce the count with a command of a *different shape* (parser vs regex vs index). Any difference must be reconciled to an exact arithmetic identity, not waved away. |
| I2 | **Positive control (synthetic injection)** | Inject one artefact that *must* match, re-run, and confirm the count rises by exactly the expected amount. This proves the predicate can fire — a filter that cannot fire returns a silence indistinguishable from absence. |
| I3 | **Coverage assertion** | Report `units_processed / units_declared` for every loop. A loop that silently skips inputs produces a clean, wrong zero. |
| I4 | **Zero re-test** | No zero result may be published until it has been re-derived by a second, independent query form. Most zeros observed in this programme have been instrument defects, not facts. |

**A negative result is a claim about the instrument before it is a claim about the subject.**
"NO EVIDENCE FOUND" is never interchangeable with "THE FUNCTION DOES NOT EXIST".

---

## 4. Research States

A Learning Item advances through these states. They are ordered; a later state presupposes the earlier
ones. **Knowing a menu's name is state 1, not coverage.**

| State | Name | Satisfied when |
|-------|------|----------------|
| S0 | `DISCOVERED` | The item exists in the Source Learning Master List with a Learning ID |
| S1 | `SOURCE LOCATED` | A reproducible evidence pointer resolves to primary evidence |
| S2 | `UI VERIFIED` | Its user-visible surface (screen, control, state, label, empty/error state) is described from evidence |
| S3 | `CONFIG VERIFIED` | Every configuration/toggle/installation condition that changes its presence or behaviour is identified |
| S4 | `FUNCTION VERIFIED` | Its business function, rules, validations and state transitions are described from evidence |
| S5 | `DATA VERIFIED` | Its object/field/relationship/constraint/identity/immutability impact is described from evidence |
| S6 | `CROSS-MODULE VERIFIED` | Its upstream/downstream handoffs and accounting/inventory consequences are described from evidence |
| S7 | `EDGE VERIFIED` | Failure, cancel, reverse, return, concurrency and migration behaviour are described from evidence |
| S8 | `CHALLENGED` | An **independent** party has adversarially challenged it and the findings are dispositioned |
| S9 | `DECISION READY` | No open blocker, no unowned unknown, downstream would not need to guess |

**VERIFIED, for coverage purposes, means S4 or higher.** A Learning Item counts toward the numerator
only from S4.

---

## 5. Coverage Formula

```
Coverage(dimension) =  Verified Learning Items in dimension
                       ------------------------------------
                       Applicable Learning Items in dimension
```

- **Denominator** = the Applicable Source Learning Population for that dimension, produced under §2.
- **Numerator** = items at S4 or higher for that dimension.
- `Applicable` excludes items formally dispositioned `OUT OF SCOPE` with a named authority (D5).
  The excluded set must be published with its size; an exclusion whose reason is stated but whose
  authority is not named does not reduce the denominator.

**Dimensions are reported separately and never collapsed into one number.** See §21 of the session
prompt and the dashboard in `INVENTORY_PILOT_COVERAGE_REPORT.md`.

---

## 6. The Gate

| Condition | Threshold |
|-----------|-----------|
| Overall Verified Coverage | **>= 95%** |
| Every Critical Area | **100%** |

**Critical 100% overrides the overall percentage in both directions.** Overall 99% with one Critical
Area at 95% is `HOLD`, not `CONDITIONAL PASS`.

### Critical Areas (minimum set)

Financial Posting · Stock Ownership · Stock Quantity · Inventory Valuation · Security ·
Tenant Isolation · Company Isolation · Approval Control · Audit Trail · Identity · Immutability ·
Period Close · Reversal · Data Integrity · Cross-Module Financial Handoff.

A domain may add Critical Areas. It may not remove one without Boss approval.

---

## 7. Rules that bind every coverage claim

1. **Menu coverage is not function coverage.** They are separate dimensions with separate
   denominators. (Pilot evidence: the Inventory menu instrument identified 13 contributing modules;
   the model instrument identified 99 over the same generation and root — a 7.6x difference.)
2. **A count of artefacts is not a count of things.** Declare which one the number is.
3. **State basis belongs on the same line as the number** (draft / posted / cancelled / active /
   installed), never in surrounding prose.
4. **A percentage moves with its denominator.** When a denominator is corrected, every percentage
   derived from it is `SUPERSEDED` until re-derived — including ones that did not change numerically.
5. **A blind spot must be measured, not asserted.** Declaring a gap does not size it. Put the
   positive control *inside* the blind spot.
6. **A correction round publishes a new denominator**, and is subject to this whole rule again.
7. **Totals are unverified claims.** Register totals are enumerated by a script, never asserted and
   never re-derived by hand.
8. **The evidence base is itself a claim.** Before any negative about capability or availability,
   the PATH SET must have been swept and published — including every mount and `$HOME`. Every prune
   is an exclusion and every exclusion is a claim (D5).
9. **Establish the generation before reading source.** Source findings are generation-bounded and
   must be labelled with the generation they were read from. A directory name is not a generation
   discriminator; a manifest version string is not a generation discriminator. Use a content-based
   discriminator and publish it.

---

## 8. Worked example (from this session's Pilot)

```
DIMENSION       : Configuration / Feature Toggle
POPULATION      : every field declared on the configuration-settings model by any module in the
                  declared domain module set
PATTERN         : AST parse; class whose declaration set includes the configuration-settings model;
                  every assignment whose right-hand side is a framework field constructor
PATH SET        : R1 (declared root, content-verified generation), domain module set = 149 modules
UNIT            : one declared settings field = one row
ELIGIBILITY     : all 149 modules processed (149/149 coverage assertion); 0 parse failures
RESULT          : 237 rows
SECOND SHAPE    : independent re-run over the same root after instrument repair: 237 (agrees)
POSITIVE CONTROL: synthetic module injected -> extractor count rose by exactly 1
```

---

## 9. Disposition vocabulary

`PASS` · `CONDITIONAL PASS` · `HOLD` · `FAIL`.

No AI role — Research Team, LESA, SMEs Core, PMO, Reviewer — may issue `FINAL APPROVED`.
Boss is the sole Final Approver.
