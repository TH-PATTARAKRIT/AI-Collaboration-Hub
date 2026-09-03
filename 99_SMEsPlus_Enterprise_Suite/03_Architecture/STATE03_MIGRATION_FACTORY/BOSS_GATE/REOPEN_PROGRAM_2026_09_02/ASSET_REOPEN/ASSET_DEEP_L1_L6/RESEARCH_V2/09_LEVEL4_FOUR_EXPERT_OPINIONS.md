# 09 — DEEP LEVEL 4: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** §4 states the business reality better than anything produced in
earlier sessions: buying one machine creates **two records, by two people, from two
documents, joined by a manual dropdown**. That sentence should go straight into the
Boss pack, because it is the problem in one line.

**Missing.** Nobody has asked what the *users* currently do about it. Is the
dropdown filled in on the UAT? On how many of the 280? That is a five-minute count
and it tells us whether the link is a real practice or a decoration.

**Risky.** §6 link 1. The hourly rate is a number a person types, default zero.
If nobody typed it, every work order costs **nothing**, and the finished-goods
valuation quietly contains no machine cost at all. Before SMEsPlus proposes to
improve that rate, someone should check whether it is currently set.

**Challenge.** I challenge §5's conclusion being labelled a "differentiator" without
qualification. Maintenance capturing no cost is a gap, yes. But the reason a
maintenance module captures no cost in most ERPs is that the cost arrives through
**purchase invoices and timesheets**, which are already costed elsewhere. Before
SMEsPlus builds maintenance costing, it should establish whether the cost is
genuinely uncaptured or merely uncaptured *in that module*.

**Evidence required next.** Two counts on the UAT: how many assets have the
equipment link populated, and what the hourly rate is on the work centres actually
in use.

**Assumed too early.** That fixing `Operation → Equipment` fixes the toll-gate
problem. It fixes the *modelling*. It does not tell us who will maintain the data.
Someone has to record which machine ran which job, every time, and that is an
operational burden the design has not yet acknowledged.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** The graph was built the way §40 demands — dependencies, then models,
then fields, then call chains — and the 797-module exhaustive search is the right
way to establish a negative.

**Missing.** Cardinality is stated for the structural gap but not for the custom
link. §4 says the join has "no inverse and no uniqueness constraint". That should
be a **counted** fact on the UAT, not a code observation. I asked for this at
Level 2 and it is still open.

**Risky.** §7 row "Equipment operational status": a financial confirmation mutates
a row in an operational table, with no inverse on cancel. In data terms that is an
**unowned write across a domain boundary**. It is the kind of thing that produces
irreconcilable states, and it will not show up in any reconciliation because
nothing reconciles those two domains.

**Challenge.** I challenge the phrase "source of truth" in §7 for *Book value*. I
wrote it as "derived", and derived values do not have a source of truth, they have
a **derivation**. If SMEsPlus stores a book value anywhere, it must store the
derivation inputs with it or it will not be reproducible. This is not pedantry:
the derivation includes a recursive tree walk and an exclusion of reversed entries.

**Evidence required next.** Counts, as above. Plus: how many of the 280 assets are
children of other assets (`G1-03`, open since Level 1).

**Assumed too early.** That the matrix in §2 describes the deployed system. It
describes the reference product plus the custom modules **found in this
workspace**. `G1-01` remains open and it caps the confidence of this entire level.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** §6 is the most useful correction produced by this session. Reframing
the finding from "production costing does not exist" to "**links 2–6 exist; 7 and 8
do not**" changes the size of the SMEsPlus build by an order of magnitude, and it
is properly evidenced.

**Missing.** Level 4 contains no Thai content whatsoever. In particular: whether
Thai cost-accounting or TFAC practice permits depreciation to be absorbed into
inventory value at all, and on what basis. That is not a detail — it is the
precondition for the whole design. It is not answered in `26` either, and I am
recording that as a gap rather than letting it pass.

**Risky.** §6 link 5 posts a real GL entry crediting an expense account and
debiting stock valuation, **only when the product is real-time valued**. If any
product in scope is periodic-valued, the machine cost lands in the finished-goods
*unit price* but produces no GL entry. That is a book/ledger divergence with a
configuration switch controlling it, and it is exactly the class of problem that
surfaces at year-end audit.

**Challenge.** I challenge the optimism implicit in §6's framing. Yes, links 2–6
exist. But they were built to absorb **labour and machine time at a standard
rate**. Feeding them a depreciation-derived rate does not make the output
depreciation; it makes it a standard rate that happens to have been derived from
depreciation. The variance between absorbed and actual will still exist, and
nothing in links 2–6 computes or posts that variance. **SMEsPlus will have to build
variance handling, and Level 4 has not said so.**

**Evidence required next.** Whether any absorption-variance mechanism exists in the
reference product. If it does not, that is a second `VERIFIED GAP` of equal
importance to links 7 and 8, and it is currently unrecorded.

**Assumed too early.** That "Off-Balance" survives contact with this chain. `04`
§2.5 established that off-balance accounts are **forbidden** on the asset account
triple. Level 4 has not asked whether they are permitted on the *work centre
expense account* or in the *stock valuation* path. If they are not, the Boss's
Off-Balance design has nowhere to attach on either side.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** The exhaustive search is methodologically sound and I have
independently confirmed the count. The Operation model carries a work-centre field
and no equipment field; that is a two-line verification and it holds.

**Missing.** The runtime event graph demanded by §40 is the weakest of the six
graphs. Dependencies, models, fields and call chains were all built. **Runtime
events were not** — nothing here traces what actually fires when a work order is
closed on the UAT.

**Risky.** §6 link 2: the hourly rate is **snapshotted onto the work order at
creation**. So changing the work centre rate does not change work orders already
created. Any SMEsPlus design that derives the rate monthly from depreciation must
decide what happens to work orders that were created under last month's rate. That
is a real design constraint discovered from source and it has not been carried
into `27` yet.

**Challenge.** I challenge §2's matrix on one omission: it shows no row for the
**custom modules themselves** as actors. `F22`'s cross-domain write is a custom
edge that appears nowhere in the matrix. If custom edges are not in the graph, the
graph describes the product, not the system.

**Evidence required next.** The runtime event trace, and `G1-01`.

**Assumed too early.** That the absence of an edge in the product means the absence
of an edge on the UAT. Three custom modules were found; the installed list is
unknown. Every "—" in the §2 matrix carries that qualifier.

---

## AAS+ CONSOLIDATION — LEVEL 4

### Agreements

1. Three modules out of 797 reference the asset model; none from operations or
   manufacturing. All four.
2. `Operation → Equipment` does not exist; the Boss's toll-gate concern is
   structurally correct. All four.
3. Maintenance records **no cost at all**; its only production effect is capacity.
   All four.
4. Links 2–6 of the production cost chain exist; links 7 and 8 do not. All four.
5. The Asset↔Equipment association is consumed by nothing. All four.

### Disagreements — preserved

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D4-01` | Whether maintenance costing is a genuine SMEsPlus differentiator | Expert 1: not until we prove the cost is uncaptured *anywhere*, not just in that module. Expert 3: the module-level gap is enough to justify the design question. **Unresolved — `39`** |
| `D4-02` | Whether reusing links 2–6 is as cheap as §6 implies | Expert 3: no — absorption variance is unbuilt and unrecorded. Experts 2/4: agreed it is a real omission. **Resolved in Expert 3's favour — recorded as a new `VERIFIED GAP` and as `UNR-14`** |
| `D4-03` | Whether the §2 matrix should include custom edges | Expert 4: yes. Others: agreed. **Resolved — `08` §4 and §7 carry the custom edges; the matrix is annotated `C`** |

### New verified gap opened at this level

| ID | Gap |
|----|-----|
| `GAP-ABS-VAR` | **No absorption-variance mechanism.** The production chain absorbs machine cost at a standard rate and contains nothing that computes, reports or posts the difference between absorbed and actual. Raised by Expert 3, accepted by all. Equal in importance to links 7 and 8 |

### Contradictions

| ID | Summary |
|----|---------|
| `CTR-04` | A financial confirmation mutates an operational record with no inverse |

### Evidence gaps

| ID | Gap | Status |
|----|-----|--------|
| `G4-01` | How many of the 280 assets have the equipment link populated | Open → `41` `UNR-08` |
| `G4-02` | Whether work-centre hourly rates are set at all on the UAT | Open → `41` `UNR-15` |
| `G4-03` | Runtime event trace | Open → `41` `UNR-16` |
| `G4-04` | Whether Thai practice permits depreciation absorption into inventory | Open → `41` `UNR-03` |
| `G4-05` | Whether off-balance accounts are permitted in the work-centre / valuation path | Open → `41` `UNR-17` |

### Consolidated position at the end of Level 4

The reference system models **one physical machine as two unconnected objects**: a
financial object that amortises and knows nothing operational, and an operational
object that schedules and knows nothing financial. This project has already built
one thin, manual, partly-inert bridge between them.

The production cost chain is **more complete than previously reported** and its
missing piece is **narrower and more specific** than previously reported: derive a
per-machine rate, and give the operation an equipment dimension to consume it.

Two new gaps opened here and both are material: **absorption variance** and the
unanswered **Thai admissibility** of depreciation absorption. Neither was in the
prior session's register.

### Gate to Level 5

Open, with the qualifier that every "—" in this level is bounded by `G1-01`.
