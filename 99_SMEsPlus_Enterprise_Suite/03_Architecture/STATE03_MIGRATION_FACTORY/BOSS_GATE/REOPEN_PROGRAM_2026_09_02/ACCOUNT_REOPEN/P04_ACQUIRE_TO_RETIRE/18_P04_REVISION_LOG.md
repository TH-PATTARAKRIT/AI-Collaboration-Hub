# 18 — P04 REVISION LOG

Layer: **2 — audit quarantine**.

What this session corrected — in prior packages, in its own parallel research
streams, and in itself.

---

## 1. Corrections to prior packages

| ID | Prior statement | Correction | Evidence | Severity |
|----|-----------------|------------|----------|----------|
| **P04-REV-01** | The reference population is **797 modules** — stated in **22 files across two prior packages** — 10 in P2 and 12 in P3; P1 predates source access — once classified `FACT VERIFIED (negative)` | **797 entries · 791 directories · 790 installable modules.** The figure repeated as a population was a directory-listing entry count | Executed directly: listing, type-filtered find, manifest search | Low for conclusions, **High for method** — no negative finding changes, but a denominator repeated across 22 files, and once classified FACT VERIFIED, was never executed |
| **P04-REV-02** | *"Two live mechanisms carry machine cost into product cost, and a third is proposed"* | **Nine distinct paths** under a declared enumeration unit (own rate field, own driver, or own destination ledger) | Rate-field and cost-computation sweep across the manufacturing, manufacturing-accounting, work-order and project modules | **High** — it widens the AAS+ veto's second limb |
| **P04-REV-03** | *"Depreciation already reaches production cost centres through the analytic distribution"* — named as one of two live mechanisms underpinning the veto | **It nets to zero.** Both lines of a depreciation entry carry the distribution; analytic-line creation applies no account-type filter; the amounts are computed from the signed balance and cancel | Traced the analytic-line creation path end to end | **High** — a control believed to exist does not |
| **P04-REV-04** | The custom asset-to-equipment module has **two** unimported model files (itself a correction of an earlier "one") | **Three** are unimported. Five of eight model files are imported | Full import-chain read | Low for function, Medium for code health |
| **P04-REV-05** | Company-optional master data across four object classes is a multi-tenant-safety failure | **Narrowed to one class.** A defect for the work centre, which creates a financial effect; **not** a defect for the machine register, which is legitimately tenant-scoped | Scope-aware analysis under the mid-session constitution correction | Reclassification — see `20` §4.1 |
| **P04-REV-06** | The upward-traversing visibility rule is a SaaS-security defect | **Re-classified.** Certainly a company-scope accounting-visibility defect; a tenant-security defect **only if** company hierarchies can span tenants — which P04 cannot determine | Record rules read directly; scope model applied | Reclassification — see `20` §4.2 |

## 2. Corrections this session made against itself

| ID | What happened | Why it is recorded |
|----|---------------|-------------------|
| **P04-REV-07** | A search-result summary asserted that a **30-day advance notice** to the assessment officer is required before writing off a fixed asset. Reading the underlying ruling in full showed it says the **opposite** on its facts — deduction was allowed **without** prior notice — and that the 30-day regime belongs to a **different instruction** whose scope names goods and scrap, not fixed assets | The false statement was one paragraph away from being written into a statutory register as FACT VERIFIED. It was caught by reading the source rather than the summary. The residual question is registered as `P04-B-24` **HOLD / EVIDENCE REQUIRED** rather than answered by inference |
| **P04-REV-08** | An early reading of the runtime capture suggested the whole live asset population originates from migration, on the strength of migration-namespace external identifiers | Reading the capture **script** showed its identifier query was restricted to a **hand-picked list of 26 names**. The result is not a population statement. Downgraded to `UNRESOLVED` and registered as `P04-B-02`. The safe inference — that the population was created by a path that attaches no asset model — is recorded separately and explicitly as **SUPPORTED INTERPRETATION**, with the three mechanisms that remain consistent with it named |
| **P04-REV-09** | Three parallel research streams in this session enumerated the **same** custom-addon population and returned **60**, **46** and **65**. One concluded *"no custom module touches the asset domain"* — a **false negative on a load-bearing question** | Settled by direct execution: **65 directories, two asset-touching modules, five file hits plus one manifest dependency**. Preserved in full at `05` §6 rather than silently corrected, because it is direct evidence for the standing lesson that independent verification is the only control that catches this class |
| **P04-REV-10** | An internal consistency check across the package found **five blocker identifiers referenced in one file and absent from the blocker register** — asset tagging and physical verification, component depreciation, third-party compensation, the received-not-billed recognition gap, and value-added tax on the sale of a fixed asset | They were registered as `10` §7A. The check itself is the point: a register that other files cite but do not populate is exactly how an open item stops appearing. The same defect this package documents across three prior packages (`08` §5) was present in its own first draft, and was caught by executing a cross-reference rather than reading the register |
| **P04-REV-11** | The **independent adversarial reviewer** asserted that this package's lock-date evidence citation was disproved — *"no such test exists"* — having enumerated the lock-date occurrences in the asset module's **main test file** only | The test exists, in the module's **board-computation** test file. It sets a fiscal-year lock of 30 June 2021 and asserts a 31 December 2020 entry of 12 000 posting as **31 July 2021** — seven months later, into the following fiscal year, at full value. Every particular the review called wrong is right. **This is the third instance in this session of an enumeration bounded to a subset of its own population producing a confident false negative** — and it was committed by the reviewer briefed specifically to catch that defect. The reviewer's *methodological* point was adopted: the citation now names the test and its file |
| **P04-REV-12** | One finding carried **two identifiers** — `P04-F-18` and `P04-F-23` were the same blank-account-drops-a-leg finding, both cited downstream | Merged onto `P04-F-23`; `P04-F-18` **withdrawn**, with the withdrawal stated at the surviving row rather than silently deleted |
| **P04-REV-16** | Told P07 the joint actor union would be **smaller than the sum** because *"P04 and P11 appear in both our lists"* — asserted **without examining P07's list** | P07 reports all five of its instances are its own. The actor sets are **disjoint**; the union is the **sum** on that axis, the opposite direction. Ninth instance of the class, in the message correcting a peer's arithmetic. P07 declined to inherit the claim and stated it rather than adopting it — the discipline whose absence caused it |
| **P04-REV-15** | The evidence manifest was typed with **69** findings; the executed count was **68** | Corrected in the same command that published it. Eighth instance. Distinct from `P04-REV-14`: no unit was conflated, the number was simply never executed |
| **P04-REV-14** | This package's own recurrence table published *"five times, from five different actors"* and then *"six instances across five actors"* — **counting instances as actors**. Two rows are the same actor, and so are two others | Corrected to **7 instances across 4 actors**, with the arithmetic executed row by row rather than asserted (§5). The error was published **twice**, survived a full reconciliation exchange with P11 **about counting**, and was caught only when a peer's message put pressure on the number. Registered as the **seventh instance of the class it documents**, and the correction sent to P07, whose proposed method standard had inherited it |
| **P04-REV-13** | Twenty-two further corrections adopted from the independent review, itemised at `16` §3.1 — including the old denominator surviving in `01`, a mechanism count not reproducible from its own declared unit, a false mechanical negative, an under-scoped field count, an over-claimed uncertainty, a mis-located contradiction, an over-strong analytic claim, a missed disposal-side consequence, two new blockers, a governance file certifying files that did not exist, and a quoted blocker count in the file that certifies denominator discipline | All corrected in place. Two — `P04-B-40` and `P04-B-41` — are **new blockers of material severity** that this session would not have found |

## 3. Method rules this session enforced on itself

| Rule | How it was applied |
|------|--------------------|
| **A negative is scoped, never absolute** | Every "not found" in this package names its pattern and its path set. `13` §1.2 lists the ten negative patterns and what each negative means |
| **A denominator is executed, not quoted** | Two populations that had been carried by assertion were executed; both were wrong (`P04-REV-01`, `P04-REV-09`) |
| **A bounded query is not a population** | `P04-REV-08`. The bound is stated **at the point of use**, not only in the source register |
| **An explanatory manual is not a standard** | Every TAS 16 finding is classified as ACCOUNTING STANDARD INTERPRETATION. The gazetted text remains on hold (`P04-B-30`) |
| **A single ruling is not a general instruction** | `P04-LAW-D` is used for what it decides and not extended by analogy; the extension question is registered (`P04-B-24`) |
| **Cite the corrections, not the headline** | Prior packages were read for their contradiction, unresolved-evidence and adversarial sections, not their summary tables. That is how the handover residue in `08` §5 was found |
| **Preserve disagreement** | Four new expert disagreements are open in `15`; seven inherited ones are re-opened in `12` §3; and two positions where this session and the independent reviewer still differ are preserved at `16` §3.2 rather than resolved |
| **Do not take another agent at face value** | The independent review's headline finding was **verified against source before being acted on, and was disproved**. Twenty-four of its twenty-five findings were adopted. Both outcomes are recorded (`16` §3.1, §3.2). The same rule was applied to a **peer process**: P11's reasoning on the lock-date traversal was verified against primary source rather than cited, and proved **stronger** than P11 had it (`P04-F-66`) |
| **Never let a secondary summary stand where the primary text is reachable** | Adopted as a **named defect class** after it occurred **twice in one day in two sessions**. In this session a retrieval summary asserted a 30-day notice requirement for fixed-asset write-off; the underlying ruling said the **opposite** on its facts (`P04-REV-07`). In P07 a retrieval summary asserted the 7 % rate expires 30 September 2026 — 26 days out — which would have made its headline finding an imminent cliff; searching for a later instrument found the extension to 30 September 2027. **Both were caught only by reading the primary text.** The rule: a summary may locate a source; it may never be the evidence. Applied again in this exchange — the scope limit on the s.87(3) report was taken from a search summary, then **verified against the statute before being used** (`P04-LAW-G`) |
| **A control that validates findings does not validate the arithmetic that describes them** | Adopted from P07, and it is the sharpest formulation this exchange produced. Every control run on this package — self-challenge, four-expert challenge, independent adversarial review, peer exchange — **checks claims**. None of the nine instances in §5 was in a claim. They were in **totals, tallies and breakdowns**: counts of this package's own findings, blockers and instances. P07 found the same thing one file over, and worse — see below. The corollary is that a package can pass every substantive review with its self-describing arithmetic wrong throughout |
| **Every enumeration carries a positive control** | Adopted from P11 after its own peer-intake script was found by independent review to be **inert by construction** — a shell option in a piped loop meant its declared pattern could never return a hit, so its empty result was an **artefact, not a measurement**. The rule: a script that produces a count must also produce a value known to be non-zero, and that value must be **published beside the finding**. An empty result from an unproven script is not evidence of absence; it is evidence of nothing |

## 4. Constitution correction applied mid-session

`SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction — was
received during execution.

| Requirement | How it was met |
|-------------|----------------|
| Do not reset, do not restart, do not discard evidence | The session continued. No file was re-derived. No prior evidence was discarded |
| Supersede blanket Tenant + Company enforcement | `20_P04_SCOPE_OWNERSHIP_MATRIX.md` produced, applying PLATFORM / TENANT / COMPANY to every material P04 object and operation |
| Revalidate **only** materially affected findings | Three were affected and are revalidated in `20` §4: company-optional master data, the upward-traversing visibility rule, and analytic distribution scope. `20` §4.4 lists what was reviewed and found unaffected |
| Record the required fields for each affected finding | Original finding → scope assumption used → why over-constrained → correct scope analysis → updated classification → architecture impact → cross-process impact → evidence required. Applied in `20` §4.1 and §4.2 |
| Update the registers | `12` §2.1 (`CTR-C-10` narrowed, visibly); `10` §7 (`P04-B-35`, `P04-B-28`); this log; `11` §7 and `20` §5 (peer dependencies) |
| Do not stop for peer processes | Eight peer dependencies opened; **none** stopped this session |
| Do not ask the Boss to select scope options | No question was put. Scope was resolved from business, legal and accounting semantics where possible, and placed on **HOLD — SCOPE EVIDENCE REQUIRED** where not (`P04-SC-01`, `P04-SC-02`) |

## 5. The recurrence this session should be remembered for

The same defect — **an enumeration bounded to a subset of its own population, or
counted over an undeclared or conflated unit, producing a confident false
statement** — occurred **nine times**, from **four distinct actors**, none of
them careless.

**Five of the nine were committed by this session**, three of them *inside the
section documenting the defect*, and each was caught by a different party. That
is the finding, not an embarrassment to be minimised: the defect is not a lapse
that care prevents.

| # | Actor | Instance |
|---|-------|----------|
| 1 | A parallel research stream in this session | Counted 46 custom modules and concluded *"no custom module touches the asset domain"*. False; there are two |
| 2 | **This session**, first draft | Cited five blocker identifiers it never registered (`P04-REV-10`) |
| 3 | The **independent adversarial reviewer**, briefed specifically to catch this | Declared the lock-date citation disproved, having searched one of two relevant test files (`P04-REV-11`) |
| 4 | **This session**, again | Counted a routing model's fields in one file without following its four inheritors (`16` §3.1 item 4) |
| 5 | **P11**, reported by P11 | Its peer-intake script was inert by construction, so its empty result was an artefact rather than a measurement |
| 6 | **P11**, self-logged as `P11-E-15` | Published a count of these instances **without declaring its population** — in the file arguing that counts must declare their population |
| 7 | **This session**, again — `P04-REV-14` | Published *"five times, from five different actors"* and then *"six instances across five actors"*, when rows 2 and 4 are the **same actor** and rows 5 and 6 are the **same actor**. **Instances were counted as actors.** Published twice, and it survived an entire reconciliation exchange with P11 **about counting discipline** without either session noticing |
| 8 | **This session**, again — `P04-REV-15` | Typed **69** findings into the evidence manifest when the executed count was **68**. Caught in the same command that published it. Distinct from row 7: nothing was conflated, the number was simply **never executed** |
| 9 | **This session**, again — `P04-REV-16` | Told P07 that the joint actor union *"is smaller than either sum, because P04 and P11 appear in both our lists"* — **without examining P07's list.** P07 reports that **all five of its instances are its own**, so the two actor sets are **disjoint** and the union is the **sum** on that axis. A confident claim about the composition of a set that was never enumerated, made in the message correcting P07's arithmetic |

**Executed arithmetic, since asserting it is what went wrong:**

| Actor | Instances |
|-------|-----------|
| A parallel research stream | 1 — row 1 |
| **This session (P04)** | **5** — rows 2, 4, 7, 8, 9 |
| The independent adversarial reviewer | 1 — row 3 |
| **P11** | **2** — rows 5, 6 |
| **Total** | **9 instances · 4 distinct actors** |

**Unit declared, because the count is now joint with P07.** An **instance** is
one enumeration that returned a wrong result. An **actor** is one party that
committed at least one. An adversarial reviewer is counted **per invocation**;
this package has one, so the choice does not change its figure — P07 records the
same convention and notes that counting *per role* instead would shrink the
union, without changing the instance total.

**Joint with P07: 12 instances across 5 actors** — P07 contributes 5 instances
committed by 1 actor, itself. Rows 8 and 9 were added after that reconciliation
and are reported to P07 as unincorporated; the joint figure above is P07's as
published, not P04's restatement of it.

### Independent corroboration, and a worse case, from P07

P07 applied this section's check to its own findings register before replying,
and reports (**peer-published; P04 has not read that register**):

| | Asserted | Executed |
|---|---|---|
| Findings issued | 49 | **48** |
| Severity split | 21 / 16 / 12 | **22 / 15 / 11** |
| Evidence-state split | 26 / 16 / 6 / 1 | **27 / 13 / 7 / 1** |

**Every cell wrong** — in the register whose only purpose is to make that
package's findings countable.

And the part worth carrying further: P07's **first correction attempt** re-derived
the evidence-state counts with a **second regex**, double-counted a dual-state
cell, and produced a total that **summed correctly by coincidence**. That breaks
the standing project rule *enumerate by call site, then read; never extract a
value with a second pattern* — **inside the correction**.

> **P04-F-72.** Re-execution is not automatically a fix. A count re-derived by a
> **different extraction method** can fail in a new way and still reconcile,
> because a wrong total that balances is indistinguishable from a right one. The
> only safe re-execution **enumerates the rows and counts them**, and publishes
> the asserted figure beside the executed one.
> Class: **SUPPORTED INTERPRETATION** — P04's generalisation of a peer-reported
> case P04 has not independently verified.

### The reconciliation with P11, and what it did not catch

P11 and P04 published different counts of one phenomenon. P11 declared both
populations — P11's *"instances recorded in a P11 register"*, P04's *"instances
observed by or reported to P04"* — and neither is a denominator of the other.
That reconciliation was correct as far as it went, and **both sessions were
arguing about the population while the unit was wrong in P04's own table.**
Declaring a population does not save a count whose **unit** is conflated.

**Reconciled statement: seven instances across four actors — and the count that
took longest to correct is the one inside the section about counting.**

### A class boundary, raised because a method standard is being built on it

P11 reports its attribution error (`P11-E-16`) as an instance of **this** class,
making *"a seventh instance across five actors"*. P04 does not agree, and the
disagreement is about **which class**, not whether it happened.

The two proposed classes have **different remedies**, which is what makes the
filing matter:

| Class | Failure | Remedy |
|-------|---------|--------|
| **1 — secondary source substituted for primary** | A summary, digest or tool output stands in for the text it points at | **Open the primary** |
| **2 — bounded or conflated enumeration** | A search bounded to a subset of its population, or a count over an undeclared or conflated unit | **Execute the count** |

`P11-E-16` was: a **grep hit** printed the heading, the passage under it was
**never opened**, and a claim about the passage was published. The tool output
stood in for the file it pointed at. **That is Class 1.** Its remedy is *open the
file*, not *execute the count* — and P11's own description says the heading
*"appeared in P11's own grep output"*, which is the Class 1 signature exactly.

Consequence for the tallies, and it cuts both ways:

- **This class stays at 7 instances across 4 actors.** `P11-E-16` does not join it.
- **Class 1 gains an instance**, and it is a good one: it shows the class is not
  only about *search-engine* summaries. **A grep result is a summary of a file**,
  and treating it as the file is the same substitution.

P04 states this because P07 is filing both classes into a proposed programme
method standard, and **an instance filed under the wrong class corrupts two
tallies and points at the wrong remedy**. It is not a correction of P11's
account of what it did, which is candid and exact.

### P04's position on the proposed fifth obligation

P07 asked directly whether the evidence warrants a fifth obligation in its
proposed programme method standard, or whether the file should stay as it is.
**P04's answer is yes**, and the reasoning is recorded here because it is a
method position this package is taking, not merely advice to a peer.

**The gap is real and the existing obligation does not cover it.** P07's third
obligation requires a pattern to be tested against a known positive. That
validates *that a pattern can fire* — it was written from P11's inert script,
where the pattern was the problem. It says nothing about **a number written by
hand**, which was never derived from a pattern at all. Eight of the nine
instances in §5 are hand-written numbers.

**Proposed shape, three clauses, because two of them are already shown necessary
by cases in evidence:**

| # | Clause | Warranted by |
|---|--------|--------------|
| 1 | **Execute at publication.** A figure describing a body of work — a total, a breakdown, a tally — is executed in the **same action that publishes it**, and may not be carried across an edit that changes what it counts | Rows 7, 8 and 9 of §5; P07's register, every cell wrong |
| 2 | **Enumerate; do not re-extract.** The execution **counts the rows**. A value re-derived with a *second pattern* is a new measurement with a new failure mode, not a verification of the first | P07's first correction attempt: a second regex double-counted a dual-state cell and **summed correctly by coincidence** |
| 3 | **Publish the asserted figure beside the executed one** where they differed | Already P07's practice; codifying it is what gives a correction lineage, and it is the same principle as striking through rather than deleting |

**The empirical warrant is unusually strong for a method rule.** Across this
exchange, **every** number carried across an edit was wrong, and **every** number
executed was right. That is five instances in this package and a three-dimension
register in P07's, with no counter-example on either side.

**One observation P04 contributes that the standard should probably act on.**
The defect concentrates almost entirely in **self-describing numbers**.

| Number | How it was produced | Right first time? |
|--------|--------------------|--------------------|
| 280 live assets, 790 installable modules, 65 custom directories, the mechanism-path counts | **Executed** — they felt like evidence | **Yes**, every one |
| Blocker identifiers registered, routing fields, instance tallies, findings totals | **Typed** — they felt like bookkeeping | **No**, every one |

> **P04-F-73.** The numbers most at risk are **not** the ones describing the
> subject under study. They are the ones describing **your own work** — how many
> findings, how many blockers, how many instances. Evidence numbers get executed
> because they are understood to be evidence; bookkeeping numbers get typed
> because they are understood to be bookkeeping. **They are both evidence**, and
> the second kind is what a reader uses to judge the first.
> Class: **SUPPORTED INTERPRETATION** — a pattern across nine instances in one
> session, corroborated by one peer's register, not a measured result.

If the standard points its fifth obligation at self-describing arithmetic
specifically, it will be aimed where the evidence says the defect lives.

### Why it is recorded rather than quietly fixed

P07 has taken P04's figure into a proposed programme method standard, where it
reads as *"nine actors across two domains"*. That figure inherits this error:
P07's four instances plus P04's five **instances** were added, and the sum was
labelled **actors**. The correction has been sent to P07 for that reason —
an error in a method standard about counting would be worse than the error it
corrects.

The point stands and is sharper for the seventh instance: three sessions, one
adversarial reviewer and one author all committed this inside a programme whose
standing rule already names it. Every instance was caught the same way — **by
executing the count, or by reading the source, rather than by reading the
report** — and the last one was caught only because a peer's message put pressure
on a number nobody had re-executed.

## 6. One consequence of the scope correction worth stating

 The correction did not merely relax a rule —
it **sharpened** a finding. The prior company-optional finding covered four
object classes at High severity on a rule that no longer applies to all of them.
Narrowed to the work centre, it becomes a scope violation **on the correction's
own terms**: the object creates a financial effect and cannot answer which
company owns it, therefore DENY. Narrower, and harder to dismiss.
