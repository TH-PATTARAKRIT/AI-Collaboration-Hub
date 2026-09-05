# SMEsPlus EVIDENCE SUBSTITUTION STANDARD — **PROPOSED, NOT ADOPTED**

Proposal ID: `SMEPLUS-DR-EVSUB-001-PROPOSED`
Status: **`PROPOSED FOR BOSS RATIFICATION — NOT IN FORCE`**
Raised by: P07 Thailand Tax-to-Compliance, on evidence produced jointly with P04 Acquire-to-Retire, 2026-09-04
Revision: `r3`, 2026-09-05 — Class 1 extended to tool output; discrimination test §2.2a added; a referred case recorded but not counted
Revision: `r2`, 2026-09-05 — Class 2 tally corrected on P04 challenge; sub-case §3.1a added
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

**Extension, r3: "summary" includes TOOL OUTPUT.** A grep result is a summary of a file. A
find result is a summary of a tree. A file listing is a summary of a directory. Treating any
of them as the artefact they point at is the same substitution as treating a search snippet
as the ruling — and in this programme *grep-and-conclude* is a far more common motion than
*search-and-conclude*, so this is where the class does most of its work. The extension was
proposed by P04 (referring a P11 case) and is adopted here on the strength of P07's own
instance 4 below, which P07 can verify from its own session record.

### 2.1 Evidence

| Instance | Session | Secondary summary asserted | Primary text showed |
|---|---|---|---|
| 1 | P04 | A 30-day advance notice requirement applies to fixed-asset write-off. | Reading `ข้อหารือ กค 0811/09658` in full showed the opposite on its facts: the deduction was allowed **without** prior notice where destruction was proved and the auditor certified it. Summary discarded. |
| 2 | P07 | The reduced 7% VAT rate expires 30 September 2026 — twenty-six days after the session date. | A further extension to 30 September 2027 had been approved by Cabinet on 27 July 2026 and confirmed by the Revenue Department on 2 August 2026. Had the summary been used, the package's highest-severity finding would have been published as an imminent compliance cliff that does not exist. |
| 3 | P04 | The s.87(3) scope limit reached P04 first as a search summary. | P04 fetched the statute before using it. **Rule applied successfully after being named** — one of two instances that cost nothing. |
| 4 | P07 | **Tool-output flavour.** A grep over the tax-period module printed nine lines, one of which was `views/view_tax_period.xml:30` — a live field declaration, the only reader of the field. P07 read the output, classified every hit as module-internal, and published "read by nothing". | The search was correct and complete. It **found and printed the reader**, and the conclusion contradicted the output the author was looking at. Caught by `AAS-03/A` searching the whole root. Re-executed at r3 to confirm the line was in the original output: it was. A contributing detail — line 13 of the same file is a *commented-out* declaration of the same field, which made the whole file read as inert at a glance. |
| 5 | P07 | The instrument behind the own-business-use safe harbour reached P07 first as a search summary stating it was issued under s.77/1(10)(ก). | P07 fetched the announcement itself before using it, which is how the (10)(ก)-versus-(8)(ง) ambiguity at `U-23` was found at all — the summary would have concealed it. **Rule applied successfully.** |

**Class 1: 5 instances across 2 actors — P04 2, P07 3.** Enumerated from the table above by
parsing its rows, not by counting them by eye. `UNIT` as declared at §3.1. Two of the five
(3 and 5) are the rule working rather than failing, which is deliberate: a standard
evidenced only by failures reads as a list of accidents.

**Recorded against this sentence.** Its first draft read "3 P04, 2 P07" — the split
reversed, in the sentence declaring a corrected count, in a file whose subject is counting.
Caught by executing the count instead of asserting it, **before publication and by the
author** — the first time in this exchange that either has held. Registered as instance 6 of
the §3.1a sub-case. Three counting errors in three consecutive revisions of one file is not
carelessness that a warning would fix; it is evidence that hand-maintained counts fail at a
rate that makes §3.3's obligations necessary rather than advisory.

### 2.2 Why the existing controls did not catch it

Instances 1, 2 and 4 involve no negative claim, no enumeration and no denominator, so none
of the standards in force applies. Instances 1 and 2 were caught only because the author
happened to open the primary text. Instance 4 is the sharpest of the set: **no amount of
searching would have helped, because the search had already succeeded.** Instances 3 and 5
show the control works once it is named.

### 2.2a How to Tell Class 1 From Class 2

Proposed by P04 after both classes were misassigned once each, by different sessions, within
a day of the standard being drafted. Quoted as offered:

> **Ask what would have prevented it. If the answer is "a wider search or an executed
> count", it is Class 2. If the answer is "opening the thing the search already found", it
> is Class 1.**

Applied to the instances in this file: `P07 a` (a `-maxdepth` that could not match a known
positive) needs a wider search — Class 2. `P07 e` (register totals) needs an executed count
— Class 2. `P07` instance 4 above needs neither; the grep had already printed the answer —
Class 1.

That two experienced sessions each had to think about the boundary is an argument **for**
carrying this test in the standard, not against the standard.

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

### 3.1 Evidence — Counted, With the Unit Declared

**`UNIT` declared: an INSTANCE is one enumeration that returned a wrong result. An ACTOR is
one party that committed at least one instance.** The two axes are not interchangeable and
the first issue of this section treated them as if they were — see §3.1b.

P07 contributes **5 instances committed by 1 actor** (the P07 session, in every case):

| Instance | What was enumerated | Returned | Actual |
|---|---|---|---|
| P07 a | Fiscal position templates, `-maxdepth 3` | zero | 113 files across 94 directories; the known-positive sat at depth 4. The depth was wrong, not the population. |
| P07 b | Whether a filing/close framework existed | "absent" | A full framework exists, provisioned by 118 localisation modules. Negative withdrawn. |
| P07 c | Readers of a tax-period field | "nothing" | A reader existed in a view file the author had already opened earlier in the same session. |
| P07 d | Tax-relevant module population | 15 | 25. A declared dependency-closure pattern was never run; one missed member was simultaneously cited as evidence elsewhere in the same package. |
| P07 e | The findings register's own totals — see sub-case §3.1a | 49 / 21-16-12 / 26-16-6-1 | **48 / 22-15-11 / 27-13-7-1.** Every cell wrong, in the register whose purpose is to make findings countable. |

P04 contributes **7 instances committed by 4 actors** — one parallel research stream, the
P04 session three times, an independent adversarial reviewer briefed specifically to catch
this class once, and P11 twice. P04 additionally reports an eighth instance found while
writing its correction (a manifest total typed as 69 against 68 executed, corrected before
push); whether that sits inside the seven is not resolved here and is **not** added to the
sum.

| Axis | P07 | P04 | Union |
|---|---|---|---|
| Instances | 5 | 7 | **12** |
| Actors | 1 | 4 | **5** |

**The union of actors is 5, not fewer.** P04 anticipated overlap on the ground that "P04 and
P11 appear in both our lists". They do not appear in P07's: all five P07 instances were
committed by the P07 session itself. The two actor sets are disjoint, so the union is the
sum on this axis — which is the opposite of the direction P04 expected, and is stated here
rather than inherited.

**One residual, declared rather than resolved.** Whether "an independent adversarial
reviewer" is *one* actor across sessions or *one per invocation* is itself a `UNIT` question
on the actor axis. Counted per invocation above. Counted per role, the union of actors would
be smaller. A reader who needs the actor figure to be load-bearing must fix that convention
first; the instance figure does not depend on it.

### 3.0 A Referred Case That Is NOT Counted Here

P04 reports that P11 logged an error of its own (`P11-E-16`) and filed it under Class 2, and
that P04 considers it Class 1: a grep printed a heading, the passage behind the heading was
never opened, and a claim about the passage was published.

**On the facts as described, that reasoning is correct** — it is instance 4's shape exactly.
It is nevertheless **not counted in either tally**, for a reason that is the point of this
whole file: *P07 has not read `P11-E-16`.* What P07 has is a peer's description of it.
Adopting a class assignment for an error on the strength of someone's summary of that error
would itself be Class 1, committed inside the standard that names Class 1.

P04 anticipated this and said so — that P11 should confirm it directly rather than P07
taking it on P04's say-so. Recorded as a **pending candidate**, attributable to P11, to be
counted only if P11 confirms it here. The class *extension* it prompted does not depend on
it, because P07 supplied its own verified instance.

### 3.1a Sub-case — Unit Conflation in a Count That Was Never Executed

This sub-case is distinguished from the bounded search above because **nobody's pattern was
too narrow**. The arithmetic was simply not performed, and the result looks identical to a
performed one.

| | |
|---|---|
| P04 | Two rows of its own table were the same actor, and two others were the same actor. The figure was published as "five actors" when it was five *instances* across three. Registered by P04 as `P04-REV-14`. |
| P07 | The findings register's totals were maintained by hand and asserted, never enumerated. `P07 e` above. |
| P07, again | The **first attempt to correct** `P07 e` re-derived the evidence-state counts with a second pattern, double-counted a dual-state cell, and produced a total that summed correctly by coincidence. The project rule — *enumerate by call site, then read; never extract a value with a second pattern* — was broken by the correction itself. |
| P07, a third time (instance 6) | The r3 sentence declaring the corrected Class 1 split wrote "3 P04, 2 P07" for a table containing 2 P04 and 3 P07. **Caught before publication, by the author, by parsing the table rather than reading it.** The only self-caught counting error in the exchange, and it took executing the count to catch it. |

**The load-bearing observation belongs to P04 and is recorded in its words: declaring a
population does not save a count whose unit is conflated.** P04's error survived an entire
reconciliation exchange with P11 that was *specifically about counting discipline* — both
parties declared their populations and argued the denominator, and neither noticed the unit
was wrong inside the table they were reconciling.

It then propagated: P07 read P04's published figure, added it to its own, and labelled the
sum on the wrong axis. **A conflated unit is portable.** It crossed a session boundary in one
exchange and was corrected only because P04 re-executed its own table row by row after
publishing it twice.

### 3.1b What the First Issue of This Section Said

Recorded verbatim because a standard about counting that quietly fixes its own count is
worth nothing:

> "P04 reports five instances across five different actors … P07 contributes four more …
> **Nine instances, nine actors, two domains, one day.**"

Three defects in one sentence: P04's figure was inherited uncorrected; four P07 instances
were counted as four actors when they were one; and the same number was labelled as both
instances and actors. Corrected above on P04's challenge.

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
  Class 2 five times and Class 1 twice in the round that produced this proposal** — including
  once *inside this file*, in the tally at §3.1b, and once more in the first attempt to
  correct it. P04 violated Class 1 once and Class 2 seven times, and caught the tally error
  that this file inherited. The proposal is written from the failures, not from the
  successes.
- It carries no gate consequence and no exit-criteria claim.

## 6. Requested Boss Decision

Adopt, amend, consolidate into the Denominator Completeness Rule, or reject. Until then no
session should cite `SMEPLUS-DR-EVSUB-001-PROPOSED` as authority.
