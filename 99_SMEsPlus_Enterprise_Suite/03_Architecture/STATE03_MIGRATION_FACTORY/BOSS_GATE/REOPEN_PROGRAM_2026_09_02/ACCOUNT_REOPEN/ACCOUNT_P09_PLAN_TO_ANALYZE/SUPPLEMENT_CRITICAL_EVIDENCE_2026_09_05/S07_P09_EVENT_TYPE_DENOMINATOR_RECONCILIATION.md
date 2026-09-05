# S07 — P09_EVENT_TYPE_DENOMINATOR_RECONCILIATION

**Checkpoint:** `CP-P09S07` · **Layer:** 1 — clean-room.

---

## 1. THE UNIT — DECLARED FIRST, BECAUSE IT IS THE DEFECT

Every figure below is in the unit **one file:line match**. It is **not** interchangeable with any of these, and the package previously mixed them:

| Unit | Why it differs |
|---|---|
| **file:line match** | what all the counts below are in |
| **write site** | some matches are simultaneously a read and a write |
| **writer** | two matches can carry **one logical write of one value** into two dictionaries of the same entry — the headline mechanism is exactly this |
| **call** | a match inside a loop is one match and N runtime writes |
| **module** | three different module denominators (11 / 23 / 33) come from the same field |

> **Any sentence of the form "N sites across M modules" that does not name its unit cannot be reconciled against another such sentence.** The prior round's claim that the headline site sits "outside the 45" mixed *file:line* with *writer*.

## 2. THE RECONCILIATION — INDEPENDENTLY RE-MEASURED

| # | Pattern | Sites | Modules |
|---|---|---|---|
| P1 | the key followed by a colon in a values dictionary *(the originally declared pattern)* | **45** | **11** |
| P2 | record-attribute assignment | **19** | 11 |
| P3 | **subscript assignment** | **18** | 13 |
| **P1∪P2∪P3** | | **82** | **23** |
| P4 | **augmented assignment** — found this round, in none of the above | **1** | 1 |
| **FULL UNION** | | **83** | **23** |
| superset | any mention of the key at all | **328** | **33** |

**The three original patterns are pairwise disjoint** — overlaps 0, 0, 0 — so 45+19+18 = 82 exactly.

### 2.1 Both prior figures are arithmetically correct
The **45/11** is correct *for its declared pattern*. The **82/23** is correct *for the three-pattern union*. **Neither was wrong; they measure different things**, and the package presented them as though one superseded the other.

### 2.2 The headline-site claim, corrected
The both-legs assignment that the whole finding rests on is a **subscript** assignment, matched by P3 and not by P1 — so it is outside the **45 file:line matches**. **But its module is inside the 11**, via two other matches in the same file. **The site denominator was defeated; the module denominator was not.** The prior round stated this too broadly.

## 3. WHAT THE UNION STILL DOES NOT REACH

| Residue | Size | Class |
|---|---|---|
| modules that mention the key but appear in **no** write pattern — they reach the field through helper methods rather than by naming it | **10 modules** | **C — a route no lexical pattern on the key can reach** |
| non-code carriers: view definitions | **84 sites / 17 modules** | **C — outside a code-only path set** |
| interface component code, including the widget's own write | **8 sites / 2 modules** | **C** |
| the default-context route, which the platform converts into a write | 3 sites | **C** |

> **The full union of 83 covers about 25 % of the field's non-test footprint.** Declaring the path set as code-only removes the **primary interactive writer** — the user interface — from the population entirely.

## 4. WHY THE DENOMINATOR CHANGED

Not because the first measurement was miscounted. Because **the pattern was chosen to match one syntactic form of a write**, and the field is written in at least four forms across three file types. **The population was defined by how it is spelled, not by what it does.**

## 5. THE COUNT THAT SHOULD BE USED

For any statement about *which mechanisms allocate*, the useful denominator is **not** any of these. It is the **9-module direct-instantiation set** established in the base package, plus the helper-method routes in §3. **The 45, the 82 and the 83 are all lexical proxies, and every one of them is a proxy chosen by the author of the claim it bounds** — the precise defect the project's denominator rule exists to prevent.

## CHECKPOINT

**`CP-P09S07` — COMPLETE — EVIDENCE VERIFIED.** Unit declared; 45/82/83/328 reconciled; residue bounded at four classes. Auto-continue.
