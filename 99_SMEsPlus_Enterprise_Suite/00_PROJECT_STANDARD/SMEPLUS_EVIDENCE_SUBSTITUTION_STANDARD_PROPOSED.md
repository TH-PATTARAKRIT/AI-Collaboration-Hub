# SMEsPlus EVIDENCE SUBSTITUTION STANDARD — **PROPOSED, NOT ADOPTED**

Proposal ID: `SMEPLUS-DR-EVSUB-001-PROPOSED`
Status: **`PROPOSED FOR BOSS RATIFICATION — NOT IN FORCE`**
Raised by: P07 Thailand Tax-to-Compliance, on evidence produced jointly with P04 Acquire-to-Retire, 2026-09-04
Branches: `research/account-p07-th-tax-compliance-2026-09-04-001`; `research/account-p04-acquire-to-retire-2026-09-04-001` @ `8d1f735`

## 0. Standing of This File

This is a **proposal**, written on an unmerged research branch, following the precedent of
`SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD.md`, which was likewise issued from a
research branch for Boss ratification. **It is not in force.** No session may cite it as
binding until the Boss adopts it. It is filed here because two independent sessions produced
the same two failure classes on the same day and neither had a route to the programme method
register; leaving that evidence inside two research packages would lose it.

## 1. Why a Proposal Rather Than a Finding

Both classes below are **method** defects, not domain defects. They do not belong to Thai
tax or to asset lifecycle; they recur wherever evidence is gathered. The existing
`SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` governs how a negative is *stated*. Neither
class is a negative-claim defect, so neither is caught by that standard.

## 2. Class 1 — Evidence Substitution by Secondary Summary

**Proposed rule: a summary may LOCATE a source. It may never BE the evidence.**

The wording is P04's and is adopted here unchanged.

### 2.1 Evidence

| Instance | Session | Secondary summary asserted | Primary text showed |
|---|---|---|---|
| 1 | P04 | A 30-day advance notice requirement applies to fixed-asset write-off. | Reading `ข้อหารือ กค 0811/09658` in full showed the opposite on its facts: the deduction was allowed **without** prior notice where destruction was proved and the auditor certified it. Summary discarded. |
| 2 | P07 | The reduced 7% VAT rate expires 30 September 2026 — twenty-six days after the session date. | A further extension to 30 September 2027 had been approved by Cabinet on 27 July 2026 and confirmed by the Revenue Department on 2 August 2026. Had the summary been used, the package's highest-severity finding would have been published as an imminent compliance cliff that does not exist. |
| 3 | P04 | The s.87(3) scope limit reached P04 first as a search summary. | P04 fetched the statute before using it. **Rule applied successfully after being named** — the only instance of the three that cost nothing. |

### 2.2 Why the existing controls did not catch it

Neither instance 1 nor 2 involves a negative claim, an enumeration, or a denominator, so
none of the standards in force applies. Both were caught only because the author happened to
open the primary text. Instance 3 shows the control works once it is named.

### 2.3 Proposed obligation

1. A search result, vendor blog, practitioner note or AI summary may be used **only** to
   locate a citation. The citation must then be retrieved and read.
2. Any claim resting on a source that was located but **not** retrieved must be recorded as
   such, with the instrument named, rather than stated as evidence.
3. Where retrieval is attempted and fails, that is recorded as an attempted-and-not-located
   hold, not as an absence.

## 3. Class 2 — Bounded-Enumeration False Negative

**Proposed rule: an enumeration that returns nothing is a defective enumeration until its
pattern has been proved against a known-positive case.**

### 3.1 Evidence

P04 reports five instances across five different actors, **including an adversarial reviewer
briefed specifically to catch this class**. P07 contributes four more from its own round:

| Instance | What was searched | Returned | Actual |
|---|---|---|---|
| P07 a | Fiscal position templates, `-maxdepth 3` | zero | 113 files across 94 directories; the known-positive sat at depth 4. The depth was wrong, not the population. |
| P07 b | Whether a filing/close framework existed | "absent" | A full framework exists, provisioned by 118 localisation modules. Negative withdrawn. |
| P07 c | Readers of a tax-period field | "nothing" | A reader existed in a view file the author had already opened earlier in the same session. |
| P07 d | Tax-relevant module population | 15 | 25. A declared dependency-closure pattern was never run; one missed member was simultaneously cited as evidence elsewhere in the same package. |

Nine instances, nine actors, two domains, one day.

### 3.2 The distinguishing feature

In every instance the pattern was **plausible** and the result was **clean**. A zero result
looks identical to a true absence, and neither reviewer nor author can tell them apart
without a known-positive. P07 instance (a) is the clearest: the zero was accepted as
meaningful for as long as it took to notice that a known example could not have matched.

### 3.3 Proposed obligation

1. Before any enumeration is relied on, run it against **at least one known-positive case**
   and show that it matches. Publish that check next to the count.
2. Publish the **command and its output**, not the pattern description. A pattern described
   but not executed reads identically to one executed.
3. A zero or near-zero result is a **prompt to test the pattern**, never a finding in itself.
4. Where a pattern is declared with false-negative modes recorded as "none known", that
   phrase is itself a flag: it means the modes were not searched for.

## 4. Relationship to Standards in Force

| Standard | Covers | Does not cover |
|---|---|---|
| `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` | how a negative is stated, classed and bounded | how the evidence behind it was gathered |
| Denominator Completeness Rule | `POPULATION + PATTERN + PATH SET + UNIT` | whether a declared pattern was **executed**, and whether a clean zero is real |
| **This proposal** | evidence substitution; unexecuted and untested patterns | — |

Class 2 sits directly against the `PATTERN` clause of the Denominator Completeness Rule and
should be read as an execution obligation on it rather than as a new rule, if the Boss
prefers to consolidate.

## 5. What This Proposal Does Not Do

- It does not bind any session. It is not in force.
- It does not amend, weaken or reinterpret any standard in force.
- It does not assert that either originating session complied with it: **P07 violated
  Class 2 four times and Class 1 once in the round that produced this proposal**, and P04
  violated Class 1 once. The proposal is written from the failures, not from the successes.
- It carries no gate consequence and no exit-criteria claim.

## 6. Requested Boss Decision

Adopt, amend, consolidate into the Denominator Completeness Rule, or reject. Until then no
session should cite `SMEPLUS-DR-EVSUB-001-PROPOSED` as authority.
