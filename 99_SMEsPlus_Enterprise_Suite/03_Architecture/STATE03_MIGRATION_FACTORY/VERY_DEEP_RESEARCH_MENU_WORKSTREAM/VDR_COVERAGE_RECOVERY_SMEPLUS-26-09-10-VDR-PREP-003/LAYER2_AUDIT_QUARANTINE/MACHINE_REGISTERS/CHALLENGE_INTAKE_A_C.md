# CHALLENGE INTAKE — Challengers A and C (B still open)
# HELD OUTSIDE THE PACKAGE PATH. Nothing applied while the round is open (GOV-01).
**LAYER 2 — AUDIT QUARANTINE.** Working record, retained as audit lineage.
Frozen baseline under review: `a146e004`.

## Verification standard applied to intake
A challenger's finding is not adopted because it was reported. Each is re-run here before
disposition. Where my re-derivation differs from theirs, **my number and their number are both
published** and the difference in method is stated.

---

## ACCEPTED — CRITICAL

### `AC-01` — the denominator moved to absorb the cells that failed (A-01, A-02, C-01)
**Verified by re-running the package's own build logs.**

```
close_remaining.txt   PROCESS 1564 applic / 1030 verif = 65.86%   RUNTIME 5074 / 4984 = 98.23%
                      remaining NOT_VERIFIED: 400 BUTTON PROCESS · 96 OBJECT PROCESS
                                              90 HANDOFF RUNTIME · 38 MENUX PROCESS
close_final.txt       PROCESS 1474 / 1474 = 100.00%              RUNTIME 4984 / 4984 = 100.00%
                      remaining NOT_VERIFIED: {}
```

The 180 cells that were `NOT_VERIFIED` became `NA`, and the denominators fell by exactly those 180
(1,564→1,474 and 5,074→4,984). **The 100.00% DETERMINED row was produced by the reclassification, not
by evidence.** Under the spec's own §3 rule table the applicable total is **30,921**, not 30,741.

The 180 reasons are individually defensible — the invoked method or the object lies outside the
declared 149-module boundary. **That does not rescue the number.** Three separate rules were broken:
- §3: *"`NA` is never assigned to an individual row."* It was, on 90 rows (52 BUTTON, 38 MENUX).
- §6: an exclusion requires *Learning ID · reason · evidence · reviewer · status* in an exclusion
  register. **There is no exclusion register in the package.**
- §8: *"No percentage may rise because a predicate was relaxed."* It rose, from 65.86%/98.23% to
  100.00%/100.00%.

**This is the same drift I caught once and stopped — and did not catch the second time.** The
single-grade model reaching 100% everywhere was recognised as a symptom; the rebuilt DETERMINED grade
carries the identical signature (100.00% on all nine dimensions) and I published it without turning the
diagnosis on it. C-16 names this precisely.

### `AC-02` — the one Critical Area at 100% does not survive the package's own specification (C-02, A-04)
Re-derived: Critical Area 15's four items are HANDOFF, applicable on SOURCE + CROSS_MODULE only,
because RUNTIME was `NA`'d contrary to §3's table which marks it applicable.

```
Area 15 under the published §3 rule table:  8 / 12 = 66.7%     (published: 8/8 = 100.0% COMPLETE)
Critical Areas at 100% under §3:            0 of 15            (published: 1 of 15)
RESEARCH-COMPLETE under §3:                 0 of 5,074         (published: 90 = 1.77%)
```

**The corrected headline is 0 of 15, and PREP-003 did not improve on PREP-002's 0 of 15.** My own
`SC-02` reached the neighbouring observation — that all 90 research-complete items are the class with
the smallest footprint — but stopped short of the correct conclusion, which is that the footprint
itself is unauthorised.

### `AC-03` — RESEARCH-VERIFIED is very largely a class label, not an item measurement (A-05)
Re-derived independently. My figures differ from A's and both are published:

| | mine | A's |
|---|---:|---:|
| verified cells that are all-or-nothing within their class | **9,424** | 9,362 |
| verified cells carrying an item-level decision | **61** | 123 |

The difference is in how the varying pairs are attributed; the substance is identical and not in
dispute. **Only 7 of ~90 class/dimension pairs vary within class at all** — PROCESS×MENU (7 of 62),
PROCESS×OBJECT (10 of 96), CONFIGURATION×SETTING (7 of 237), OPTIONAL_FUNCTION×SETTING (7 of 237),
RUNTIME×AUTOMATION (11 of 26), RUNTIME×OBJECT (17 of 96), EDGE×OBJECT (2 of 96).

For SOURCE, DATA_MODEL, SECURITY and CROSS_MODULE the grade **never varies within a class**. So for
those four dimensions the two grades the spec says *"must never be merged"* are merged — into the same
class rule table that already decides applicability. Security's 60.1% is 270 rule/ACL/group rows
verified *about themselves*, with 0 of 1,846 fields and 0 of 96 objects — the items the grade is about.

---

## ACCEPTED — MATERIAL

| # | Finding | Verification |
|---|---------|--------------|
| `AC-04` | **10 of the 90 RUNTIME research-verified items are recorded as installed on no deployment** (A-06). Re-derived exactly: 46 MENU "(2 of 2)" · 17 OBJECT · 11 AUTOMATION · **10 MENU "not installed on any observed deployment"** · 6 MENU "(1 of 2)". By the report's own grade table the figure is **80 / 1.61%**, and **52 menus**, not 62. The same 10 are counted in the census row that says they are not installed | **CONFIRMED, exact** |
| `AC-05` | **912 is the sum, not the union** (A-03, C-05, my `SC-04`). Union = **737**; 157 items are double- or triple-mapped. Found independently by all three parties | **CONFIRMED, exact** |
| `AC-06` | **`FUNCTION_COMPLETE` = YES on all 5,074 rows** of the machine register while the matrix publishes 0 for fourteen areas (A-09, C-06). `VERIFIED_DIMS` sums to 30,741 against a true 9,485. Legacy columns from the pre-two-grade build, never removed. **This is `PW3-F-01` committed inside the package that names it** | **CONFIRMED** |
| `AC-07` | **The evidence base is not "the whole of it"** (C-07). The path set was never published; ≥12 further database identities exist on the host, two of them full ERP databases carrying the tables this package measures, one owned by role `smeplus`. A controlled-install lab with a directory named for the very configuration `CRITICAL-GAP-01` needs sits on the same host. **My "declared, and the whole of it" heading is not supported and must be retracted** | **ACCEPTED — C's own declared exclusions noted: its dump identification was a floor, not a census** |
| `AC-08` | **`BOSS-DEC-10` is omitted from the carry-forward register** (C-08). Verified: it exists in the PREP-001 decision register and asks whether stop-at-one-hop becomes the universal boundary rule. **The 5,074-item denominator under every number in this package rests on a rule its own programme classifies as provisional and subject to an open Boss decision**, and my register that exists so no reader has to guess dropped it | **CONFIRMED** |
| `AC-09` | **The three container menus are still fully applicable in my own register** (C-09). `LI-INV-MENU-0028 / -0034 / -0042` carry `kind: CONTAINER` and 6 applicable dimensions each. I accused PREP-002 of not landing a correction in its rows, then did not land mine | **CONFIRMED** |
| `AC-10` | **Two predicates do not test the sentence attached to them** (A-13). `CROSS_MODULE_CALL` matches **any** ORM model access including same-domain, so `P3-F-04`'s *"call into another domain"* is not established — the count is *"accesses some model"*. `ERROR` is a bare substring `'raise'`, firing on comments and identifiers, so 18.8% is an upper bound. **The declared positive control injected a cross-domain call — a control that fires identically on an in-domain call, so it could not fail the way the predicate fails.** `CORR-F-37` recurring | **ACCEPTED — retraction required on `P3-F-04`** |
| `AC-11` | **"all twenty facets are established" for the 17 PROCESS-verified items is unsupported** (A-12). None of the 17 carries a facet record; 10 sit at the register's lowest status. The report declares nine of the twenty not covered by this session at all, so the claim contradicts its own §2 | **ACCEPTED — retraction required** |
| `AC-12` | **The TRIGGER marginal omits 82 of 962** (A-07). onchange + constrains = **94**, published as 13; delete-hook 15, published as 14. The row sums to 880 under a heading declaring n = 962. The other ten marginals reproduce exactly | **CONFIRMED** |
| `AC-13` | **"33 distinct optional modules" and "twelve capability switches"** (A-08). 33 is the count of distinct activation **strings**; 8 are not modules and 101 elements have no module route. Atomic modules = **25**. Switches: 16 distinct values, 15 `group_` routes, 14 atomic — **12 does not reproduce under any reading**. Unit conflated with population | **CONFIRMED** |
| `AC-14` | **Cross-file contradictions on load-bearing numbers** (A-14). BK12MAY26 completed movements published as **14,441** in one table and **3,680** in three other places — 14,441 is the movement-table row count, not the completed count, so the column heading is wrong and the state basis is undeclared. Gated elements **633** and **709** in the same file. `85,832` appears once and matches no register | **CONFIRMED** |
| `AC-15` | **Overall Verified Coverage is defined, made computable, and never published** (C-03, A-15). The figure this package exists to produce appears in no published file. Its value is 1.77% on the register basis and **0.00%** under the spec's own rule table | **CONFIRMED** |

## ACCEPTED — MINOR
`AC-16` the 512-table attributes the 52 removed buttons' reason to the 31 retained ones — disjoint sets
(A-11). `AC-17` "Fourteen are [below 100%]" — thirteen are; area 6 is not computable, which is not
below 100% (A-15). `AC-18` the CONFIGURATION 100% coverage assertion counts 26 automation rows whose
recorded condition is a runtime activation statement, not a configuration determination (A-16).
`AC-19` "both current-generation deployments" while three exist, and which two is never stated (C-18).
`AC-20` §6's "minimum set" modality is not carried into the matrix's "required 15 of 15" (C-17).
`AC-21` `CRITICAL-GAP-04`'s *"a design prohibition to adopt"* reads imperatively before deferring to
Boss; rephrase to a recommendation (C-14).
`AC-22` the `DET_*`/`RV_*` columns are written by no script in the package (A-10) — the two-grade step
must be shipped for the register to be reproducible.

## NOT ADOPTED / CARRIED AS OBSERVATION
- A-17's finding **against PREP-002** — that `00D` §2's *"30 nodes with no prior coverage"* does not
  equal its own 17 + 16 = 33 — is verified and correct, and is a **third** defect in that package, not
  in this one. It is added to the forward corrections, not applied to the frozen artefact.

## CONFIRMATIONS RECORDED (silence here would be misread as untested)
Freeze honoured — `git log a146e004..HEAD -- <pkg>` empty, working tree clean, no file modified after
the freeze; `GOV-01` did **not** recur. Manifest 23/23 hashes recomputed, 0 mismatches. The fifteen
Critical Areas are verbatim from the frozen `VDR_COVERAGE_RULE.md` §6, name-for-name and in order — no
category invented. LAYER 1 is free of vendor identifiers (the only hits were the challenger's own
pattern matching inside "Stock Quantity"). No approval, no certification, no self-certification, no
Boss-decision foreclosure. **396 of 417 published figures reproduce to the digit**, including every cell
of the Critical Area matrix, the §3 blocking table, the two-grade table, and all four censuses.

**The shape of the result: the arithmetic is nearly flawless and the sets are wrong.** Every material
defect is one rung above the arithmetic — a denominator that moved, a grade that is a class label, a
union never taken, predicates that cannot test their own sentence. All four would survive any recount,
because passing a recount is exactly what they do.
