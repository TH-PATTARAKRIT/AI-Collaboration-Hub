# PMO_PREP004_CERTIFICATION_REPORT.md
# PMO verification and certification decision

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 15.

---

## 1. Decision

> # CERTIFICATION: **HOLD**

**Not DENIED, and not GRANTED.** The previous round was **DENIED**, on grounds that included a
measurement that moved its own denominator and corrections verified only by their author. **Both
grounds are addressed.** What now blocks certification is the substantive bar in §18 — not a defect in
how the work was done.

## 2. §18 conditions, tested one by one

| Condition | State |
|-----------|-------|
| denominator frozen | **MET.** Population V5, 5,074 items / 30,870 cells, **derivable from the published class rule table alone** — which was not true of V3 or V4 |
| no silent exclusions | **MET.** The exclusion register is empty; every surviving `NA` is class-based and enumerated |
| false exclusions corrected | **MET.** 180 cells restored; **48 of 52 exclusion reasons proved false against source** and corrected; the container rule applied to all 17 nodes, not the 3 a reviewer named |
| evidence admission completed | **MET.** Every quarantined item classified; **not one discovered database is a target-generation deployment** |
| all critical gaps closed | **NOT MET — 2 of 6** |
| Critical Areas 15/15 at 100% | **NOT MET — 0 of 15** |
| Overall Verified Coverage ≥ 95% | **NOT MET — 0.00%** |
| Process coverage verified | **NOT MET — 0.00%**, and this is the blocking dimension |
| Configuration coverage verified | **PARTIAL — 17.31%**, all nine axes determined for all 49 gates |
| Optional Function coverage verified | **PARTIAL — 22.36%**, activation *and* deactivation determined for all 39 subjects |
| critical runtime reachability measured | **MET.** 2,854 of 3,319 element-observable items observed as themselves |
| clean independent challenge completed | **PENDING** — this baseline is frozen for it |
| **no unresolved technical matter misrouted to Boss** | **MET — 0.** Four previously-misrouted questions were withdrawn and answered |

**Four conditions unmet, two partial, one pending. → HOLD.**

## 3. What PMO verified about the conduct of the work

| Check | Result |
|-------|--------|
| Denominator lineage | **three versions published with their deltas** — 30,741 → 30,921 → 30,906 → 30,870, each movement attributable to a numbered correction |
| Any cell reclassified `NA` after being graded | **none.** The R1 defect does not recur |
| `NOT_DETERMINED` present in the register | **yes, 42 cells** — the grade can fail, which was the previous round's critical defect |
| Learning ID uniqueness | 5,074 rows, 5,074 distinct ids, verified by enumeration |
| Orphan evidence | none — every extract is indexed with row count and hash |
| Unsupported `N/A` | none — every `NA` carries a class reason, and every class is in the published table |
| Reproducibility | **the grade-assigning code is shipped this round.** The previous round's grades were produced by code that was not in the package |
| Large extracts omitted for size | **declared as an exclusion, with row counts and SHA-256 per file** so a reviewer can regenerate and verify byte-for-byte |

## 4. Two matters PMO records against this round

### `PMO4-01` — a governance finding against the previous round, upheld
A challenger withdrew its own confirmation that the previous freeze had held, and it was right to.
**Two commits landed in the package path while that challenge round was still open** — the challenger
resumed after reporting and read a superseded baseline. The prior baseline was preserved as an
ancestor and nothing was rewritten, and the corrections all weakened the package's own claims, but
**the round was treated as closed on the inference that every challenger had reported, rather than on an
explicit, timestamped close.**

**Control adopted for this round:** the round's open and close are both recorded, and **no commit enters
the package path between them.** Challenger reports do not close the round; the recorded close does.

### `PMO4-02` — a challenger's disclosed conduct
The scope challenger recorded that it continued a sweep after a stop signal and asked that a person
judge it. **PMO's technical finding: nothing entered certified evidence through it** — the two items
that mattered most were classified **NOT ADMITTED**, one for the wrong generation and one for holding no
data. The conduct question itself is **not a technical fact** and is the one item in this package
correctly placed on the Boss list.

## 5. Why this is HOLD and not DENIED

Denial in the previous round rested on **how the work was done**: a denominator that absorbed its own
failures, and corrections nobody but their author had checked. This round:

- the denominator is derivable from a published rule and moved only by numbered corrections;
- the grade has a failing value that actually occurs;
- **four questions the previous round pushed upward were taken back and answered**, and three of the answers changed the package;
- the code that assigns every grade is shipped;
- and the largest single evidence advance in the programme — element-level runtime observation — was produced by reading a table that had been available for three rounds and never extracted.

**What remains is not a process defect. It is that the domain is not yet understood to the required
depth**, and one dimension — process — accounts for that on its own.

## 6. Statement of authority

This is a verification finding and a **HOLD**. It is not an approval, and it does not decide the
programme's disposition. **No AI may issue FINAL APPROVED, and none is issued here.**
