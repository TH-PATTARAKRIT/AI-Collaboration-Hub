# P09_AAS03_CHALLENGE

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Layer:** 1 — clean-room. Full expert records with citations are in the Layer 2 quarantine.

---

## 1. HOW THE CHALLENGE WAS RUN

Four AAS-03 experts ran **inside** the research phase, not after it, with **disjoint** assignments, each instructed to disprove rather than agree, and each given the standing clause: *if any path in this brief is wrong, report it as a finding.*

| Expert | Discipline | Owned candidates |
|---|---|---|
| X1 | functional design | CH-CAND-03, CH-CAND-04 |
| X2 | database design | CH-CAND-01, CH-CAND-02 |
| X3 | integration and localization | CH-CAND-05 |
| X4 | code, user interface and access control | CH-CAND-06 |

Each candidate was owned by exactly one expert, and no expert reviewed a candidate arising from its own reading.

## 2. VERDICTS

| ID | Claim | Entry status | Verdict | Decided by |
|---|---|---|---|---|
| CH-CAND-01 | the assignment-rule scope constraint does not re-fire on a payload-only change | PLAUSIBLE | **CONFIRMED** | X2, by reading the platform's validation entry point rather than the decorator |
| CH-CAND-02 | a costed row of one company can be allocated to another company's axis value through any non-privileged axis | PLAUSIBLE | **CONFIRMED**, and upgraded — reachability needs no execution | X2, on two independent structural mechanisms |
| CH-CAND-03 | postings arriving in an already-closed reallocation period are never allocated | PLAUSIBLE | **CONFIRMED** | X1, full module read; the only escape is a human act outside the mechanism |
| CH-CAND-04 | a dimension-filtered reallocation moves the whole balance, not the allocated share | PLAUSIBLE (highest severity) | **CONFIRMED**, and **re-characterised** | X1, every step read; see §3 |
| CH-CAND-05 | the report shadow view multiplies rows per axis | PLAUSIBLE | **DISPROVED as an exposure claim** — mechanism confirmed and found *stronger* than stated, exposure not reachable | X3, by enumerating every caller |
| CH-CAND-06 | an allocation change on a posted, locked, hash-chained entry passes every guard and leaves no trace | class A on three lists | **CONFIRMED** | X4, guard-by-guard trace |

**Five confirmed, one disproved.** The disproof is recorded as the most valuable single result of the challenge phase, because it is the only one that reduces a claim the research team had already written down.

## 3. THE TWO VERDICTS THAT CHANGED THE FINDING, NOT JUST ITS STATUS

**CH-CAND-04 was re-characterised, not merely confirmed.** The research team wrote that a partial allocation is "transferred as if it were total". X1 traced every step and established the sharper fact: the filter compiles to an **overlap test on the allocation's keys**, and the percentage never enters the query at all; the aggregation then takes the full balance; and **the complementary unfiltered bucket excludes the same rows in full**, so the unallocated fraction is not picked up anywhere either.
**This is a misallocation, not a duplication.** That phrasing supersedes the research team's throughout the package.

**CH-CAND-05 was disproved, and the disproof surfaced a stronger mechanism and a new residual.** X3 established that the multiplication factor is **the total number of root axes defined anywhere in the database**, not the number a given record populates — stronger than the team's claim. It then enumerated every caller, found exactly one, and showed that the one call site always attaches the restricting filter in the same construction. **The exposure does not follow.** While disproving it, X3 raised a *new* open question: the restricting filter compares integer identifiers against a column wrapped as a JSON scalar, and whether that comparison matches or silently returns nothing was **not decided from source** — a correctness question, not an exposure one, class **C**.

**Recorded as a standing lesson:** the disproof did not make the mechanism safe. Correctness here depends on one filter that one call site happens always to attach. That is a latent hazard, and `P09_EDGE_CASE_MATRIX` EC-44 carries it as such rather than closing it.

## 4. CORRECTIONS RETURNED AGAINST THE RESEARCH TEAM

Eleven corrections were returned by the four experts. **Every material correction in this session came from a reviewer, none from the author** — consistent with the pattern recorded across the programme.

| ID | Correction | Effect |
|---|---|---|
| COR-REV-01 | the "no ledger link" finding must not be read as "management records are a homogeneous, summable population" | narrows a team claim |
| COR-REV-02 | the reporting-grouping map is exactly four entries, transcribed | closes a class-C residue |
| COR-REV-03 | the discarded ledger link is a general pattern, not an isolated inventory fact | generalises a team claim |
| COR-REV-04 | a profitability domain's own source admits it is incomplete and depends on a downstream module; without that module, labour costs fall into a generic unlabelled bucket | **new fact the team did not have** |
| COR-X2-01 | axis deletion drops the column **with cascade**, taking every dependent database object, unenumerated | raises severity |
| COR-X2-02 | the privileged-axis cache **is** invalidated on every write path that matters | **narrows a team claim** — the team's wording invited a wrong reading of indefinite staleness |
| COR-X2-03 | before the current version the delete rule on non-privileged axis columns was set-null, not restrict | adds a third historical state |
| COR-X4-01 | the client-side allocation control is decorative — it colours a total and does not block saving | narrows the team's obligation narrative |
| COR-X4-02 | the axis-value picker never restricts by company, and the source carries the developers' own comment saying a company restriction might be needed | strengthens a team claim with an admission in source |
| COR-X4-03 | the analytic group is an **implied group with no explicit granting group**, so one settings toggle grants it to every internal user | **materially raises severity** |
| COR-X4-04 | the confirmed-budget lock is reopenable through the normal interface via an unguarded state reset | **narrows and worsens** — a narrower exploit path than "raw programmatic write", and an easier one |
| X3-COR-01 | the tenant custom-root figures were stated in the wrong unit — directory entries, not modules | **denominator correction against the author**; see `P09_REVISION_LOG` §R2 |
| X3-COR-02 | a **statutory** Thai module is present in two custom copies and absent from the third | raises the deployment-copy uncertainty from a management concern to a statutory one |

## 5. FINDINGS THE EXPERTS ADDED THAT THE TEAM DID NOT HAVE

Nine substantive additions. The four with the largest consequence:

| ID | Finding | Why it matters |
|---|---|---|
| X4-01 | schema-altering rights over the dimension structure are **one settings checkbox away from every internal user**, by ordinary configuration semantics | converts a governance concern into a live exposure |
| X1-05 | the budget match join has **no exclusivity guard**, and a blank axis column on a budget line is a **wildcard**, not "not applicable" — so one management record can be counted in full against several budgets at once | a second, independent double-count mechanism, distinct from anything the team found |
| X1-04 | one work-order duration change produces **two** management records at two rates against potentially different axis values, which one profitability section aggregates without distinguishing them | a third double-count mechanism, configuration-dependent |
| X3-03 | inter-company mirroring **silently drops** the entire allocation at the company boundary, asserted as expected behaviour by the module's own test | extends the boundary finding across companies |

Further additions: X1-03 (project↔axis binding is optional, many-to-one, and orphans history on reassignment), X1-06 (two reporting surfaces scope the same records by structurally different rules), X1-07 (the achieved filter is engineered to sweep in ledger-less records), X2-06 (no database-level check constraint exists anywhere on the surface), X2-08 (no index over allocation percentages), X2-09 (the upgrade script crashes on a state its own runtime declares possible), X4-02 (the view patch's permission gate sits inside a cache whose key has no user component), X4-03 (the patch silently no-ops on the most common customisation), X4-04 (the allocation field carries no model-level group restriction, so the view restriction gates nothing), X4-05 (the report's shadow object is connection-scoped and never dropped), X4-06 (a create call reaches a state the write rules appear to reserve).

## 6. THE BRIEF-ERROR CONTROL FIRED TWICE

Two of the four experts reported an error in the brief that tasked them:

- X2 found that the platform-source path given to it carried a doubled directory segment and did not exist; it located the correct path and used it for every citation.
- X1 could not locate the tenant custom roots — its brief named only the two reference roots — and correctly declared **class C, not searched because not found**, rather than asserting absence or silently substituting.

X1 additionally flagged an apparent count discrepancy against the evidence base and **declined to call it an error** without running the team's method. It was reconciled afterwards as two correct measurements of different units (`P09_REVISION_LOG` §R3).

**The control is retained for every future brief.**

## 7. DISAGREEMENT PRESERVED

Points on which the experts do not agree with each other or with the research team are **not** resolved here. They are carried into `P09_AAS_PLUS` intact, per the constitution.

## 8. TERMINAL STATE

**CHALLENGE COMPLETE. 5 CANDIDATES CONFIRMED, 1 DISPROVED, 13 CORRECTIONS ACCEPTED, 15 EXPERT-ORIGINATED FINDINGS ADDED. NO GATE MOVED.**
