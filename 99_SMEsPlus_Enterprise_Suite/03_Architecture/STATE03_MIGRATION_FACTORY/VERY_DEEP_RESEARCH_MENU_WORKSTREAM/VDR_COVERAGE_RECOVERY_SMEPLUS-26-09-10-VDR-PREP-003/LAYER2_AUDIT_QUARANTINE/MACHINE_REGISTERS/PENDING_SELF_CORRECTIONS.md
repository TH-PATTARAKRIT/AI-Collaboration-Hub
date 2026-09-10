# PENDING_SELF_CORRECTIONS — PREP-003 R1
# HELD OUTSIDE THE PACKAGE PATH. Not applied while the review round is open (GOV-01).
**LAYER 2 — AUDIT QUARANTINE.** Working record, retained as audit lineage.

Frozen baseline under review: `a146e004`. These corrections are applied only after the
round closes, in a new baseline, with the round's validity re-verified first.

---

## `SC-01` — the published applicability rule table does not match the executed code

`VDR_COVERAGE_MEASUREMENT_SPEC.md` §3 publishes a class→dimension rule table. Two defects:

**(a) The HANDOFF row is wrong.** Published: SOURCE · RUNTIME · CROSS_MODULE (3 dimensions).
Executed: **SOURCE · CROSS_MODULE only (2)**. `RUNTIME` is `NA` on all 90 handoff rows.

**(b) §3's own governing claim is false as executed.** §3 states *"`NA` is never assigned to an
individual row."* It is, on **90 rows**:
- `BUTTON`: PROCESS applicable on **379 of 431** — 52 rows carry a per-row `NA` whose recorded reason is
  that the invoked method is not declared inside the 149-module boundary;
- `MENUX`: PROCESS applicable on **96 of 134** — 38 rows, action owned outside the domain census.

Those 90 per-row `NA`s each carry an evidenced reason, so they are **not** unknowns dressed as `NA` —
but the rule table claims a purity the code does not have, and the claim must be corrected rather than
the code. Correct statement: *applicability is class-based, with a declared per-row exception where the
target of the element lies outside the declared boundary; each such row records its own reason.*

## `SC-02` — every RESEARCH-COMPLETE item is the class with the fewest applicable dimensions

**All 90 RESEARCH-COMPLETE items are class `HANDOFF`** — the class with **2 applicable dimensions of
9**, the smallest footprint in the population. No item of any other class is research-complete.

The headline *"RESEARCH-COMPLETE 90 of 5,074 = 1.77%"* is arithmetically right and **materially
misleading without this sentence beside it**. The honest form:

> Research-complete items: 90 of 5,074 (1.77%) — **all 90 are handoff elements, which are applicable on
> 2 of the 9 dimensions. Zero items are research-complete on a footprint of 3 dimensions or more.**

**Consequence for the Critical Area matrix**, which must be corrected in the same edit: Critical Area 15
(Cross-Module Financial Handoff) is reported as the one area at 100%. Its 4 items are handoff elements,
so its 100% is **100% of a two-dimension footprint**. The corrected reading of the headline is:

> **1 of 15 Critical Areas reaches 100%, and it does so on 2 of 9 dimensions. On the full dimension
> set, 0 of 15 are complete.**

This makes the result worse, not better. It is published for that reason.

## `SC-03` — two disjoint sets of size 90 are reported in the same package

`VDR_RUNTIME_CRITICAL_PROOF_REPORT.md` `R3-F-01` reports **90** runtime research-verified cells
(62 menus, 17 objects, 11 scheduled jobs). The coverage figures report **90** research-complete items
(90 handoff elements). **The two sets are disjoint and share no member.** Both figures are correct; the
coincidence of magnitude invites conflation. A disambiguating note is required at both sites.

## `SC-04` — the union figure is the sum, mislabelled

`VDR_CRITICAL_AREA_COMPLETION_MATRIX.md` §2 states: *"Items mapped to at least one Critical Area:
**912** (union; areas overlap)."*

**912 is the sum of the per-area populations. The union is 737.** Enumerated:
`sum(len(v) for v in critical_area_map.values()) = 912`; `len(set().union(*values)) = 737`.
The parenthetical says "union" while the number is the sum — the two are not the same quantity, and the
overlap the sentence acknowledges is exactly the difference (175 multiply-mapped memberships).

Correct statement: **737 distinct items are mapped to at least one Critical Area; 912 area-memberships
in total, because 175 memberships are second or later mappings of an item already counted.**

---

## Note on how these were found

All four came from re-deriving the package's own published numbers from the register rather than
re-reading the prose. `SC-04` in particular is the defect this package accuses its predecessor of —
a total asserted rather than enumerated — committed in the same package that names the rule.
