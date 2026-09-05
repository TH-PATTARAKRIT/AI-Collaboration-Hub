# SMEsPlus EVIDENCE SUBSTITUTION STANDARD — **PROPOSED, NOT ADOPTED**

Proposal ID: `SMEPLUS-DR-EVSUB-001-PROPOSED`
Status: **`PROPOSED FOR BOSS RATIFICATION — NOT IN FORCE`**
Raised by: P07 Thailand Tax-to-Compliance, on evidence produced jointly with P04 Acquire-to-Retire and P11 Central Core Reconciliation, 2026-09-04
Revision: `r7`, 2026-09-05 — halves stamped `value @ owner-SHA` per the `P11-G-02` refinement (`§3.1c`); refusal-as-control note and the `P11-E-20` symmetry recorded at `§3.0`
Revision: `r6`, 2026-09-05 — P11's half enumerated by its owner and verified present (2 → 5); `P11-E-19` recorded as obligation 6's strongest warrant; defeat attempt against P11's candidate at `§4b`
Revision: `r5`, 2026-09-05 — mechanism sharpened (`§2.1a`); suspicion-independence rationale added (`§3.0`); P11's half held at the owner's own declaration against a peer's restatement
Revision: `r4`, 2026-09-05 — `P11-E-17` verified at source and counted; identifier corrected from `P11-E-16`; joint tally replaced by declared halves (`P11-G-02`); obligations 5 and 6 added; P11's third pattern recorded and declined with reasons
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
| 6 | P11 | **`P11-E-17`.** A grep printed the right file and the right line; P11 saw the heading, did not open the passage two lines away, and published an attribution claim about the passage. The claim was false. | Nobody's search was too narrow — the failure was downstream of a search that had already succeeded. **Verified by P07 at source**, not on a peer's description: `research/account-core-reconciliation-2026-09-04-001 @ 2e284ef`, `P11_RESEARCH_ERROR_AND_REVISION_LOG.md:218`. P11's own log independently classes it as secondary-source at `:323`. |
| 5 | P07 | The instrument behind the own-business-use safe harbour reached P07 first as a search summary stating it was issued under s.77/1(10)(ก). | P07 fetched the announcement itself before using it, which is how the (10)(ก)-versus-(8)(ง) ambiguity at `U-23` was found at all — the summary would have concealed it. **Rule applied successfully.** |

**Class 1: 6 instances across 3 actors — P04 2, P07 3, P11 1.** Enumerated from the table
above by parsing its rows, not by counting them by eye. `UNIT` as declared at §3.1. Two of the five
(3 and 5) are the rule working rather than failing, which is deliberate: a standard
evidenced only by failures reads as a list of accidents.

**Recorded against this sentence.** Its first draft read "3 P04, 2 P07" — the split
reversed, in the sentence declaring a corrected count, in a file whose subject is counting.
Caught by executing the count instead of asserting it, **before publication and by the
author** — the first time in this exchange that either has held. Registered as instance 6 of
the §3.1a sub-case. Three counting errors in three consecutive revisions of one file is not
carelessness that a warning would fix; it is evidence that hand-maintained counts fail at a
rate that makes §3.3's obligations necessary rather than advisory.

### 2.1a The Mechanism, Stated Precisely

Sharpened by P04 from P07's instance 4, and recorded as theirs:

> **The substitution needs tool output PLUS a plausible reason not to open the source.
> Either half alone is usually survivable. It is the pair.**

In instance 4 the pair was: a grep result that looked complete, and a *commented-out*
declaration of the same field higher in the file, which made the whole file read as inert at
a glance. In instance 2 it was a search summary that looked authoritative, and a date that
was plausible on its face. In instance 6 (`P11-E-17`) it was a grep that printed the right
heading, and a heading that appeared to say what the passage said.

This is why "read more carefully" is not the remedy and **open the source** is. The author
in each case did read carefully — of the wrong artefact.

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

P07 contributes **5 instances committed by 1 actor** (the P07 session, in every case).
Composition changed at r3 without the total changing: `P07 c` was reclassified out to
Class 1, and `P07 f` — the split error made while correcting this very tally — replaced it.
That the total held while its members changed is a coincidence, and is stated so no reader
treats the stability as corroboration.

| Instance | What was enumerated | Returned | Actual |
|---|---|---|---|
| P07 a | Fiscal position templates, `-maxdepth 3` | zero | 113 files across 94 directories; the known-positive sat at depth 4. The depth was wrong, not the population. |
| P07 b | Whether a filing/close framework existed | "absent" | A full framework exists, provisioned by 118 localisation modules. Negative withdrawn. |
| ~~P07 c~~ | ~~Readers of a tax-period field~~ | — | **RECLASSIFIED OUT OF CLASS 2 at r3.** The search was not too narrow: the grep printed the reader. It is now Class 1 instance 4 (`REV-E-18`). Struck rather than deleted, per obligation 5c. |
| P07 d | Tax-relevant module population | 15 | 25. A declared dependency-closure pattern was never run; one missed member was simultaneously cited as evidence elsewhere in the same package. |
| P07 e | The findings register's own totals — see sub-case §3.1a | 49 / 21-16-12 / 26-16-6-1 | **48 / 22-15-11 / 27-13-7-1.** Every cell wrong, in the register whose purpose is to make findings countable. |
| P07 f | The Class 1 split declared in the r3 sentence | "3 P04, 2 P07" | **2 P04, 3 P07.** Caught before publication by parsing the table rather than reading it — the only self-caught counting error of the exchange. Sub-case instance 6. |

P04 contributes **7 instances committed by 4 actors** — one parallel research stream, the
P04 session three times, an independent adversarial reviewer briefed specifically to catch
this class once, and P11 twice. P04 additionally reports an eighth instance found while
writing its correction (a manifest total typed as 69 against 68 executed, corrected before
push); whether that sits inside the seven is not resolved here and is **not** added to the
sum.

Each half is stated as **value @ owner-SHA**, per the `P11-G-02` refinement at §3.1c.

| Half | Instances | Actors | Executed by | Owner-SHA |
|---|---|---|---|---|
| P07 | 5 | 1 | P07, by enumerating its own revision log | this branch, r6 |
| P04 | 9 | 4 | P04, by enumerating its own register | **none supplied** — see §3.1c |
| P11 | **5** — `P11-E-03`, `-E-12`, `-E-15`, `-E-18`, `-E-19` | 1 | P11, by parsing its own log with the command published beside the figure | `b68ae17`, all five ids verified present by P07 |

**There is deliberately no total on this table.** It is published as declared halves under
`P11-G-02`, adopted from P11 and stated in P11's words: **a cross-party tally cannot be
executed by either party.** P07 cannot open P04's drafts; P04 has not read P11's register
and says so; P07 has enumerated only its own. A single joint figure is unexecutable by
construction, and every joint figure produced in this exchange was wrong — including one
P11 inherited from P04 without re-deriving it (`P11-E-18`), and the two P07 published at r1
and r2.

**Note on P11's half — and the sharpest warrant obligation 6 has.** This row moved twice, and
both moves are instructive.

P04 first reported P11's half as **2**. P07 declined it, because it was a peer relaying a
third party's number — the class of evidence that had produced the wrong identifier one
message earlier — and carried `≥1` instead, the only figure P11 had stated directly.

P11 has since enumerated its own half by parsing its log and reports **5**, correcting its
own previously published figure of 2. P07 verified all five ids are present at `b68ae17`
before adopting; the classification of each as enumeration-class is P11's, not re-adjudicated
here.

**P11's published "2" was itself asserted, not executed** — registered by P11 as `P11-E-19`.
Two of the three omitted instances are decisive: `P11-E-03` was simply overlooked, and
`P11-E-18` **was logged in the same document, four paragraphs above the figure that omitted
it.**

So `P11-G-02` — the rule that a cross-party tally must be published as declared halves, each
executed by its owner — **failed on its first application, by its author, in the document
that opened it.** That is the strongest warrant in this file for obligation 6, and it belongs
to P11. It also means every party to this exchange has now published an unexecuted
self-describing count: P04 nine times, P07 five, P11 at least twice. No party caught its own
except by executing it.

Note that P04's "2" was not a fabrication — it was an accurate relay of P11's own published
figure. **Both the relay and the original were wrong, in the same way, one step apart.** A
figure inherited from a peer carries that peer's execution status, and neither party can see
it.

### 3.1c Refinement — a Declared Half Goes Stale Silently

`P11-G-02` as first stated said *publish two declared halves, each executed by its owner*. It
did not say **when** a half was executed. P11 refined it after observing this file carry
`P11: ≥1` correctly:

> A declared half is published as **value @ owner-SHA**, and correcting staleness is the
> **owner's obligation to push**, not the consumer's to re-derive.

The gap is subtle and worth stating, because the rule's *correct* behaviour is what conceals
it. Holding `P11: 2` or `P11: ≥1`, a consumer cannot distinguish **disagreement** from
**staleness** — and the rule forbids the one action that would resolve it, re-deriving
another party's half. So a consumer obeying the rule is structurally blind to the half going
out of date. Stamping the SHA makes staleness visible without licensing re-derivation.

Applied above. **P04's half carries no SHA** because none was supplied; it is P04's to stamp,
not P07's to infer, and until it is stamped that row cannot be distinguished from a stale one.

**Recorded against P04.** P04 has retracted its "adjust to 14 across 5" offer as
`P04-REV-18`, on the ground that it supplied a number it could not execute *in the message
arguing that counts must be executed*. Recorded here because the retraction is the strongest
demonstration of obligation 6 in the file: the party who proposed the joint figure is the
party who withdrew it, on the rule they had just adopted.

**Recorded against P07.** r2 published "12 instances across 5 actors" and r3 left it
standing. Both were single joint numbers of exactly the kind `P11-G-02` forbids. P04 has
since revised its half from 7 to 9 — resolving the eighth instance P07 had declined to place
(`P04-REV-15`, the 69-against-68 manifest count) and adding a ninth (`P04-REV-16`, asserting
the union direction against P07's list without examining it, made *in the message correcting
P07's arithmetic*). P04 offered "adjust to 14 across 5 if you want it current". **P07 declines
the offer, not the input:** the halves are adopted, the single number is not, because
producing one would repeat the defect this section documents.

**One residual, declared rather than resolved.** Whether "an independent adversarial
reviewer" is *one* actor across sessions or *one per invocation* is itself a `UNIT` question
on the actor axis. Counted per invocation above. Counted per role, the union of actors would
be smaller. A reader who needs the actor figure to be load-bearing must fix that convention
first; the instance figure does not depend on it.

### 3.0 The Referred Case — Identifier Corrected, Now Counted

P04 referred a P11 defect it believed was misfiled under Class 2, and filed the argument
against **`P11-E-16`**. r3 recorded it as a pending candidate, uncounted, on the ground that
P07 had only a peer's description of it.

P11 then confirmed directly **and corrected the identifier: it is `P11-E-17`, not
`P11-E-16`.** P07 verified both at source before acting —
`research/account-core-reconciliation-2026-09-04-001 @ 2e284ef`,
`P11_RESEARCH_ERROR_AND_REVISION_LOG.md`:

| Id | Line | Heading | Remedy |
|---|---|---|---|
| `P11-E-16` | 193 | a tolerance-zero boundary drafted narrower than P11's own evidence | re-derive a boundary's scope from the register |
| `P11-E-17` | 218 | an attribution published without opening the file cited two lines earlier | open the file |

`P11-E-17` is now **counted** as Class 1 instance 6. `P11-E-16` is **not** in this standard
at all — see §5a.

**Why this matters more than a typo.** Had r3 counted the referral when it arrived, the
standard would have illustrated secondary-source substitution with a defect that has nothing
to do with sources and whose remedy is unrelated — and it would have done so *inside the
file that names the class*. The refusal to count a peer's description is what left room for
the owner to correct the identifier before it landed. The rule paid for itself in one
exchange.

**And it fired without suspicion, which is the load-bearing part.** P07 had no reason to
doubt the identifier and formed no doubt about it; the referral was declined on the **class
of the evidence**, not on any misgiving about its content. P04 draws the general rule from
this against itself, and it is adopted here as the rationale for why §2.3 and §3.3 are
obligations rather than judgement calls:

> **A discipline that only fires when you suspect a problem is not a discipline.**

A control conditioned on suspicion is unavailable in exactly the case that matters — the one
where the author is not suspicious. Both classes in this file were survived, repeatedly, by
authors who had no reason to doubt what they were looking at.

**A symmetry worth recording, because it runs the other way.** P11 told P07 and P04 that the
identifier correction was time-critical because the wrong id would otherwise land in this
standard. It never could have: the referral had already been declined, on a ground that
predates anyone knowing there was an error at all. P11 logged that against itself as
`P11-E-20` — *a correct finding published with an overstated consequence* — verified present
by P07 at `cdde634:…/P11_RESEARCH_ERROR_AND_REVISION_LOG.md:369`. Their own summary of it:
they asserted what P07's package would do **without opening P07's package**, which is the
same defect from the other direction.

P07 does not classify `P11-E-20` here. It is P11's error and P11's to place, and the question
is genuinely open — no summary was substituted, only an assumption, which may put it outside
both classes in this file.

**And a positive control, offered by P11 as `SUPPORTED INTERPRETATION` and recorded as
theirs.** Four refusals across three sessions: P11 declining to extend a Boss ruling to an
axis it does not address; P11 declining to adopt a P07 example on P04's word and reading the
P07 package first; P07 declining to count a P11 error on P04's description; P04 declining to
re-derive P11's half. **None contributed a finding. Every one prevented a defect.** A
cross-process seat's value is at least as much in what it declines to carry as in what it
composes — which is not measurable by any count in this file, and is worth stating for that
reason.

**Note on what "confirmation" bought.** P11's message is itself a summary of P11's log. Owner
confirmation is better evidence than third-party description, but it is not the document. The
count above rests on `git show` of their log at the cited commit, which is why the identifier
error was caught in the same action that confirmed the instance.

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

5. **Self-describing arithmetic.** A figure that describes a body of work — a total, a
   breakdown, a tally, a register count — is subject to three further clauses. Proposed by
   P04, adopted here, each warranted by a case already in this file rather than by
   reasoning:

   - **5a. Execute at publication.** The figure is executed in the same action that
     publishes it, and may not be carried across an edit that changes what it counts.
     *Warrant:* every cell of P07's three-dimension findings register; P04 rows 7–9.
   - **5b. Enumerate; do not re-extract.** The execution counts the rows. A value
     re-derived with a **second pattern** is a new measurement with a new failure mode, not
     a verification of the first. *Warrant:* P07's first correction attempt, which
     double-counted a dual-state cell and summed correctly **by coincidence**. This clause
     exists because "just re-run it" is the obvious remedy and is **not sufficient**.
   - **5c. Publish asserted beside executed** wherever they differed. A correction without
     lineage is a smaller correction. *Warrant:* `00 §3.1` of the P07 package, and the
     preservation of P07's original wrong tally at §3.1b of this file.

   **Why clause 5 names self-describing arithmetic specifically, on P04's observation:** the
   defect is not evenly distributed. Across both packages, every **domain** number was
   executed and right first time — 280 live assets, 790 installable modules, 65 custom
   directories, 118 return-type modules, 94 of 126 fiscal-position directories, 447,384
   journal lines. Every **wrong** number described the authors' own work: blocker ids,
   routing fields, instance tallies, findings totals. Evidence numbers get executed because
   they are understood to be evidence; bookkeeping numbers get typed because they are
   understood to be bookkeeping. **They are both evidence, and the second kind is what a
   reader uses to judge the first.**

   Empirical warrant, stated so a reader can weigh it: across this exchange **every number
   carried across an edit was wrong and every number executed was right** — nine instances
   on P04's side, five on P07's including a three-dimension register, one on P11's, and no
   counter-example in either direction.

6. **Cross-party counts** (`P11-G-02`, adopted from P11). A tally spanning parties is
   published as **declared halves, each executed by its owner**, never as one number.
   Neither party can execute the other's half, so a single joint figure is unverifiable by
   construction. *Warrant:* every joint figure in the P04 / P07 / P11 exchange was wrong,
   including two P07 published and one P11 inherited without re-deriving.

   **6a. Stamp each half `value @ owner-SHA`** (P11's refinement, §3.1c). A half without a
   SHA cannot be distinguished from a stale one, and the rule's own prohibition on
   re-deriving another party's half is what conceals the staleness. Correcting a stale half
   is the **owner's** obligation to push, never the consumer's to re-derive.

## 4. Relationship to Standards in Force

| Standard | Covers | Does not cover |
|---|---|---|
| `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` | how a negative is stated, classed and bounded | how the evidence behind it was gathered |
| Denominator Completeness Rule | `POPULATION + PATTERN + PATH SET + UNIT` | whether a declared pattern was **executed**, and whether a clean zero is real |
| **This proposal** | evidence substitution; unexecuted and untested patterns | — |

Class 2 sits directly against the `PATTERN` clause of the Denominator Completeness Rule and
should be read as an execution obligation on it rather than as a new rule, if the Boss
prefers to consolidate.

## 4a. A Third Pattern, Offered by P11 — Recorded, and DECLINED for This Standard

P11 offers a third pattern, drawn from `P11-E-16`, explicitly as an option rather than
forcing it onto an existing shelf:

> **A boundary derived from its triggering instance inherits that instance's scope.**
> `T0-13` was drafted while composing a cross-tenant compound and took its scope from the
> case in front of it, while P11's own register — four documents away — already generalised
> it. Remedy: re-derive a boundary's scope from the register, never from the finding that
> prompted it. P04 reports being equally exposed.

**P07's judgement: the pattern is real, and it does not belong in this standard.**

Both classes here share one mechanism — *something stood in for the evidence*: a summary
stood in for a source (Class 1), an assertion stood in for an execution (Class 2). The third
pattern has a different mechanism entirely: nothing stood in for anything. The evidence was
read correctly and the **scope of a derived artefact** was drawn too narrowly from its
occasion. Its remedy — re-derive from the register — is not "open the primary" and is not
"execute the count".

Filing it here would make the standard a shelf for unrelated method defects, which is
precisely the failure P11 avoided by not forcing it. Two classes that share a mechanism can
carry a discrimination test (§2.2a); three that do not, cannot.

**Recommended instead:** raise it as its own proposal. P07 has no instance of it and
therefore should not be its author.

**P11 has since authored it** — `P11_METHOD_PROPOSAL_OCCASION_SCOPED_GENERALISATION.md`,
verified present at `b68ae17` — as a `DESIGN CANDIDATE`, not a standard, with its evidence
graded one instance / one self-report / one unasserted candidate. P11 invited an attempt to
defeat it. P07 made one, reading `P11-E-16` in full at source rather than from P11's
description; the result is at §4b.

`P11-E-16` is accordingly **absent from every tally in this file**, which is also what
§3.0's identifier correction was protecting.

## 4b. Defeat Attempt Against P11's Candidate Pattern — Result

P11 states the condition that would defeat its candidate: *a discrimination test showing an
instance reduces to Class 1 or Class 2 — that a substitution was present after all.* P07
attempted it against the sole instance, `P11-E-16`, read in full at
`b68ae17:…/P11_RESEARCH_ERROR_AND_REVISION_LOG.md:193-216`.

**Against Class 1 — the pattern survives.** No summary was consulted. The triggering instance
was real primary evidence, correctly read. Class 1's mechanism is *X purports to represent Y
and was used instead of Y*; here nothing purported to represent the governing register. The
occasion is not a proxy for the register, it is a different and narrower fact. **No
substitution. Not Class 1.**

**Against Class 2 — the pattern survives as a pattern, but this instance may not.** P11's own
routing rule says *register never enumerated → Class 2*. The entry reads: `T0-13` "took its
scope from the case in front of it **rather than from** the register that already generalised
it". That wording is ambiguous between *the register was consulted and mis-weighted* and *the
register was never consulted*. On the second reading, P11's own test routes `P11-E-16` to
Class 2 and the candidate pattern is left with **zero clean instances rather than one.**

**P07's result, stated as a finding against the proposal rather than a verdict on it:**

- The *mechanism* is not defeated. A rule's scope inherited from its occasion is a real and
  distinct failure, and its remedy — re-derive from the register — is neither "open the
  source" nor "execute the count".
- The *instance* does not cleanly establish it, on the entry's own text. Whether `P11-E-16`
  belongs to the candidate pattern or to Class 2 turns on a fact only P11 holds: **was the
  unified event register open, or merely extant, when `T0-13` was drafted?** If consulted and
  still mis-scoped, the instance is clean and the pattern has its first. If never consulted,
  it is Class 2 and the pattern's evidence base is one self-report and one candidate.
- P07 does not resolve that question and should not: it is a fact about P11's own drafting
  process, not about the artefact.

This is offered in the spirit P11 asked for. It does not recommend withdrawal — a candidate
whose grading is corrected is stronger than one whose sole instance is unexamined, and P11's
decision to grade its evidence explicitly is what made the test possible at all.

## 5. What This Proposal Does Not Do

- It does not bind any session. It is not in force.
- It does not amend, weaken or reinterpret any standard in force.
- It does not assert that any contributing session complied with it: **P07 violated Class 2
  five times and Class 1 twice in the round that produced this proposal** — including
  once *inside this file*, in the tally at §3.1b, and once more in the first attempt to
  correct it. P04 violated Class 1 once and Class 2 seven times, and caught the tally error
  that this file inherited. The proposal is written from the failures, not from the
  successes.
- It carries no gate consequence and no exit-criteria claim.

## 6. Requested Boss Decision

Adopt, amend, consolidate into the Denominator Completeness Rule, or reject. Until then no
session should cite `SMEPLUS-DR-EVSUB-001-PROPOSED` as authority.
