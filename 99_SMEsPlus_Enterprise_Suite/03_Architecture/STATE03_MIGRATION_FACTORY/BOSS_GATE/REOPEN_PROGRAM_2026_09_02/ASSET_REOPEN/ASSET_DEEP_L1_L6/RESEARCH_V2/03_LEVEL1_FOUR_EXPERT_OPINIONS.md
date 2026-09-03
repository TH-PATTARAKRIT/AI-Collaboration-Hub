# 03 — DEEP LEVEL 1: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

Expert opinions are **independent perspectives, not verdicts**. None of them
issues PASS, APPROVE or FREEZE (§6).

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** The creation-route inventory and the state set are solid: they come
from the field definition and the guard methods, not from the UI. The finding
that Asset Model is a *status*, not a separate entity, is well founded and it
changes how the SMEsPlus functional model should be drawn.

**Missing.** Level 1 has established *what functions exist*. It has not yet
established **what a user is required to do versus permitted to do**. Specifically:
nothing yet says whether an asset can run with no accounts set, whether a model is
mandatory, or what happens functionally when a required account is blank. Those
are Level 3 questions and they must not be assumed away here.

**Risky.** The capability table marks 12 items `ABSENT`. There is a standing
temptation to read "absent" as "we must build it". Absence of Transfer, Split and
Merge in a mature ERP after fifteen years of development is **evidence about
demand**, not only about capability. Before SMEsPlus commits to building them,
someone should ask why an entire market apparently does not need them.

**Challenge.** I challenge the framing of item 4, Capitalization. Calling it
`PARTIAL` is generous. There is no capitalisation *process* at all — no
construction-in-progress stage, no accumulation of multiple cost sources onto one
pending asset, no commissioning event. For a business that builds its own concrete
plant assets, that is not a partial capability, it is a missing one. I would
reclassify it and I am recording the disagreement rather than resolving it.

**Evidence required next.** The functional consequence of a fully-depreciated
asset that keeps running: does the reference ERP show it, report it, or lose it?

**Assumed too early.** That "Asset" means the same thing to the Boss and to the
reference ERP. The Boss's Asset is a machine that makes concrete. The reference
ERP's Asset is a number that amortises. Level 1 has now proven those are different
objects; the team should stop using one word for both.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** The single-table, status-discriminated design is confirmed from the
model definition, and the parent/child self-reference for value increases is
confirmed from the field pair. Both are structural facts, established without any
reliance on foreign keys.

**Missing.** Level 1 has no **cardinality** statement yet, and cardinality is where
this design will hurt. The self-reference means an asset's true value is a
**recursive aggregate over a tree**, not a column. Any SMEsPlus reporting or
migration that reads the value column of a single row will be wrong for every
revalued asset. This must be carried forward explicitly.

**Risky.** The overload of one table across model / live / retired / component is
convenient for the application and hostile to the data layer. Every query about
"assets" must remember to exclude templates. Every aggregate must remember to
exclude or include children consistently. The runtime evidence already shows the
consequence: the population count had to be expressed as *state != model* to mean
"real assets".

**Challenge.** I challenge any statement of the form "the asset table holds the
asset's value". It does not. It holds *this node's* value. I want that sentence
banned from downstream documents.

**Evidence required next.** Storage and recursion characteristics of the value
fields — which are stored, which are computed, which are recursive. Level 2.

**Assumed too early.** That the 280 records observed on the UAT are 280 assets.
They are 280 rows with `state != model`. Whether any of them are children of each
other has not been checked, and if some are, the population is smaller than it
looks. I am raising this as a concrete verification item, not a rhetorical point.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** The boundary statement in §6 is the correct conclusion and it is
properly evidenced by exhaustive search rather than by inspection of a few likely
files.

**Missing.** Localisation is entirely absent from Level 1 and that is a gap in the
level, not in the product. Nothing here yet separates:

- what the reference ERP does,
- what Thai accounting standards require,
- what Thai tax law requires,
- what SMEsPlus should target.

Level 1 currently describes only the first. The other three are unaddressed until
`26`, and until then no statement in this level should be read as an accounting
requirement.

**Risky.** The most dangerous item in the whole capability table is #22, *no tax
book*. Thailand routinely produces a book/tax difference on fixed assets because
the statutory rates are **ceilings** and the accounting useful life is an entity
judgement. A system with exactly one depreciation schedule cannot represent that
difference. Every downstream design that treats the single schedule as "the"
depreciation is inheriting a defect.

**Challenge.** I challenge the classification of item 13, Revaluation, as
`PARTIAL`. Creating a child asset for an upward revaluation is not a weak
implementation of revaluation — it is a **different accounting event** (a
subsequent capital addition). Labelling it revaluation invites someone to believe
the reference ERP supports the IAS-16 revaluation model. It does not, and I want
that recorded as a boundary, not a partial.

**Evidence required next.** Primary Thai statutory text on rates, pro-ration and
the treatment of disposal. Do not accept secondary summaries.

**Assumed too early.** That "Off-Balance" as the Boss uses it is an accounting
concept with external standing. It is at present an account classification inside
one product. Whether Thai statutory reporting tolerates the construction the Boss
intends is completely unestablished.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** Every claim in §2 and §3 is traceable to a field definition, a
selection list or a guard method in primary source. The negative findings are
the strongest part: they came from exhausting the search space (797 modules), not
from failing to find something.

**Missing.** The trace demanded by the prompt — UI → view → model → field → method
→ calculation → write → database → journal — has been started only at the model
layer. The view layer is untouched. In particular nobody has yet established
**which fields are actually visible to a user**, and that matters: a field that
exists in the model but appears in no view is not a capability, it is an
implementation detail.

**Risky.** Three of the four "roles" in §1 are distinguished only by `state`, and
`state` is `readonly=True` on the model. Every transition therefore happens through
a method. If SMEsPlus reimplements this with a writable status, it will inherit
none of the guards and all of the shape. That is a concrete, avoidable defect and
I want it flagged now, at Level 1, not discovered at build time.

**Challenge.** I challenge the completeness of the creation-route table on one
point: it lists routes that the *product* provides. It does not list what a
**custom module** could already have added on this project's UAT. Level 1 has
looked at the reference product and at two custom modules found in the workspace.
It has not proven that those are the only custom modules on the running system.

**Evidence required next.** The installed module list from the UAT itself. Until
that exists, every "no such capability" statement in this package is bounded by
*"in the source trees available in this workspace"* and must be written that way.

**Assumed too early.** That the source tree in the workspace is the code running
on the UAT. Nobody has verified the build hash. This is not pedantry — the whole
session's method rests on it.

---

## AAS+ CONSOLIDATION — LEVEL 1

### Agreements

1. Asset Model is a status of the asset object, not a separate entity. All four.
2. The reference Asset domain is a closed financial sub-ledger with no operational
   surface. All four.
3. The 12 `ABSENT` items are genuinely absent from the reference product as far as
   the available source trees show. All four.
4. Level 1 has not yet touched localisation, views, or cardinality. All four.

### Disagreements — preserved, not averaged

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D1-01` | Classification of **Capitalization** | Expert 1: should be `ABSENT`, not `PARTIAL`, because there is no process. Expert 4: `PARTIAL` is correct because value assignment demonstrably occurs. **Unresolved — carried to `39`** |
| `D1-02` | Classification of **Revaluation** | Expert 3: should be a boundary statement ("a different event"), not `PARTIAL`, to prevent a false inference of IAS-16 support. Experts 1/2: `PARTIAL` with the caveat written is sufficient. **Unresolved — carried to `39`** |
| `D1-03` | How to read the 12 absences | Expert 1: absence is market evidence, do not build reflexively. Expert 3: absence of a *tax book* is a defect regardless of market. **Both stand; they are about different items** |

### Contradictions found at Level 1

None internal to Level 1. The material contradictions arise at Levels 3 and 4 and
are registered in `37`.

### Evidence gaps opened at Level 1

| ID | Gap | Raised by | Closes at |
|----|-----|-----------|-----------|
| `G1-01` | Installed module list on the running UAT is unknown | Expert 4 | **Does not close this session** → `41` `UNR-04` |
| `G1-02` | Build identity of the UAT vs the workspace source tree unverified | Expert 4 | **Does not close this session** → `41` `UNR-05` |
| `G1-03` | Whether any of the 280 UAT assets are children of others | Expert 2 | **Does not close this session** → `41` `UNR-06` |
| `G1-04` | Field storage / recursion characteristics | Expert 2 | Level 2 — `04` |
| `G1-05` | Field visibility in views | Expert 4 | Level 2 — `04` |
| `G1-06` | Thai statutory primary text | Expert 3 | `26` |

### Consolidated position at the end of Level 1

The Asset domain is **bounded, closed and financial**. Its capability set is
larger than the previous session credited in the depreciation engine, and smaller
than the Boss's working model assumes in capitalisation, revaluation, impairment
and tax. The three most consequential absences for SMEsPlus are, in order:
**no tax book**, **no capitalisation process**, and **no operational surface**.

Every negative finding in this package carries the standing qualifier established
by Expert 4: *within the source trees available in this workspace*. `G1-01` and
`G1-02` are the reason that qualifier cannot be dropped, and they are carried to
the unresolved register rather than argued away.

### Gate to Level 2

Open. Level 2 must deliver the field register with storage/compute/related
characteristics (`G1-04`) and view ownership (`G1-05`).
