# P10 — EVIDENCE-BASE CHALLENGE PROTOCOL

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001` · Layer 1
Checkpoint `CP-P10D09` (part 2).

---

## 1. Why the Protocol Exists

Across this session's three rounds, challenge scope and yield ran as follows:

| Round | Challenges | Scope | Evidence-base or method defects found |
|-------|-----------|-------|---------------------------------------|
| 1 | 4 | findings | 0 |
| 2 | 4 | findings ×3, evidence base ×1 | 4, **all from the one** |
| 3 | 4 | evidence base, method, findings, **decision authority** | see `59` |

**The directive's caution against over-generalising statistically is accepted.** Two rounds is not a sample. The protocol below is justified not by the counts but by a structural argument: **a challenge scoped at conclusions inherits the author's evidence base**, and a reviewer working from the same population cannot see what the population excludes. The one challenge that broke that inheritance found things no finding-scoped challenge could have.

## 2. The Protocol — mandatory ordering

> **A finding may not be challenged until the evidence beneath it has been.**

| Step | Challenge | Question | Fails if |
|------|-----------|----------|----------|
| **A** | **Population** | What is the universe, and how was it enumerated? | The population was declared and not enumerated; or the unit is undeclared; or duplicates are counted as members |
| **B** | **Denominator** | What is the denominator of every ratio, count and coverage claim, and who chose it? | A denominator was chosen by the author of the claim it bounds; or a percentage is published without one |
| **C** | **Tooling** | What tool, what version, what alternatives were searched, what was the output? | A capability negative is asserted without all four |
| **D** | **Extraction completeness** | What was extracted, what was retained, what was displayed, what was read? | A conclusion rests on a display that did not contain the deciding field |
| **E** | **Findings** | Only now: are the conclusions right? | — |

**Plus, added by P10 to its own protocol this round, and PROPOSED for programme adoption — P10 cannot make it programme-permanent:**

| Step | Challenge | Question | Fails if |
|------|-----------|----------|----------|
| **F** | **Decision authority** | For every peer-sourced claim: what does the peer's own **status field** say? | A position, recommendation or open blocker is used as an adopted boundary; or an option is eliminated on an unresolved external decision |

Step F is added because the defect it catches — an option eliminated on an unadopted boundary — was invisible to A through E. It is not an evidence defect and not a method defect. It is a **governance** defect, and it needs its own reader.

## 3. Application to P10's Remaining Material Findings

Applied in this round to every finding P10 still carries. Result:

| Finding | A | B | C | D | F | Outcome |
|---------|---|---|---|---|---|---------|
| Recognition event collapsed into the posting act | ok | ok | ok | ok | ok | Stands; under challenge C this round |
| Silent re-date, specified, with an executed control | ok | **corrected** — denominator was 44, is 90 | **corrected** — one tool, no alternatives searched | **corrected** — lock columns extracted, not read | ok | Stands as capability; **exposure claim withdrawn** |
| Attribution nets to zero, validation path | ok | ok | ok | ok | ok | Stands, narrowed |
| Deferral test suite has no attribution coverage | — | — | — | — | — | **Withdrawn** in the prior round, class `E` |
| Deferral mechanism has no schedule object | ok | **class `B`** — model scan across the root never run | ok | ok | ok | Stands at class `B`, not `A` |
| No accounting-event object exists | ok | ok | ok | ok | **corrected** — peer's universal claim carried as `C`; P10's own root-scoped search is `A` | Stands, re-scoped to one root |
| The status quo is excluded by a programme boundary | — | — | — | — | **FAILS F** | **Withdrawn**; option restored |

**Two findings failed at step F that had passed every other step.** That is the protocol's justification.

## 4. Limits of This Protocol — declared

1. It does not make a reviewer independent. A protocol executed by the author is still self-review.
2. Step F depends on peers publishing legible status fields. Where a peer's status is ambiguous, F cannot resolve it and must record `UNRESOLVED — EVIDENCE REQUIRED` rather than guess.
3. Ordering does not guarantee coverage. A reviewer can execute all six steps shallowly.
4. The protocol has been applied **once**. Its yield is not yet measurable, and this document should not be cited as evidence that it works.
