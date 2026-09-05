# 16 — P04 AAS+ INDEPENDENT AUDIT

Layer: **2 — audit quarantine**.
**Disagreement is preserved, not adjudicated.**

---

## 1. Independence — stated first, because it governs how the rest is read

The prior package's declared deviation was that its AAS+ audit was *"a structured
self-challenge by the same session that did the work"*, and the standing
programme lesson is that **independent review is the only control that has caught
this defect class** — a prior self-review found 13 issues and an independent
review then found 68 more.

This session therefore ran **two separate things**, and keeps them separate:

| | §2 — Self-challenge | §3 — Independent challenge |
|---|---|---|
| Who | This session, against its own package | A separate agent, adversarially briefed, with **no access to this session's reasoning** |
| Brief | Find what the package overstates | **Disprove** the package's load-bearing claims against primary source; find classification errors, denominator defects, internal inconsistency, omissions, and governance breaches |
| Limitation | Same author. Weak by construction | Still AI-executed. **No human has reviewed this package** |

**The limitation is not discharged.** The veto's scope should be treated as a
floor, not a ceiling.

## 2. Self-challenge — what this package overstates, found by this session

These were found and **corrected before publication**. They are recorded because
the corrections are the evidence that the check ran.

| # | Overstatement | Correction | Where |
|---|---------------|------------|-------|
| 1 | *"797 modules"* repeated as a population | 797 entries / 791 directories / **790 installable modules**. Executed | `05` §2.1, `18` `P04-REV-01` |
| 2 | The figure was attributed to *"three packages"* | It appears in **21 files across two** source-based packages; the earliest predates source access | `18` `P04-REV-01` |
| 3 | *"All 280 live assets originate from migration"* | The runtime capture's identifier query was **hand-bounded to 26 names**. Downgraded to UNRESOLVED | `01` §6.2, `18` `P04-REV-08` |
| 4 | A 30-day notice requirement for fixed-asset write-off, taken from a search summary | The underlying ruling says the **opposite** on its facts. The summary was discarded and the residual question registered as HOLD | `07` §5, `18` `P04-REV-07` |
| 5 | *"Nine paths"* set against a prior *"two"*, inviting a false comparison | The **unit caveat** was added: nine is correct under a **declared disjunctive unit**; the prior count declared none; the weakest of the nine is named | `06` §2.3 |
| 6 | Five blocker identifiers cited in the package but **absent from the blocker register** | Registered as `10` §7A. **The package had reproduced, in its own first draft, the exact defect it documents across three prior packages** | `10` §7A, `18` `P04-REV-10` |
| 7 | A cross-reference to a section of file `06` that did not exist | The section was written | `06` §2.3 |
| 8 | An expert-raised item (VAT on disposal) registered as *"not researched"* | **Researched the same session** rather than deferred, closing one part and escalating another at High | `07` §5.5 |

**Self-assessment of the self-challenge: weak, and it still found eight things.**
Items 3, 4 and 6 would each have put a false or incomplete statement into a
register.

## 3. Independent challenge

The review returned **25 findings across four tiers**, plus a list of claims it
tested that survived and a list it declares unreviewed. Every finding was
**verified by this session against primary source before being acted on** — the
constitution requires that agents not be taken at face value, and §3.2 shows why
that mattered.

### 3.1 Findings adopted — the package was wrong and is corrected

| # | What it disproved or weakened | Action taken |
|---|-------------------------------|--------------|
| 1 | **File `01` still declared the old denominator** — 797 modules, 60 custom, "857 total", and the sentence *"the 797 figure is therefore a population"*. The one file the correction exists to fix was the one file where it was not applied | Corrected. `01` §1 now declares **790 installable / 65 custom / 855**, with §1.1 showing the executed counts. `00` §2 corrected too |
| 2 | **The nine-path count is not reproducible from its own declared unit.** Applied literally, M1/M2 collapse and M4/M5 collapse — the declared unit yields **7**. Reaching 9 by re-reading "destination ledger" as "destination entry" is changing the unit after the count, which `00` §4 forbids | Corrected in `06` §2.3. Three counts are now given against three explicitly named units — **6, 7 and 9** — with 7 as the figure the declared unit produces. `P04-F-42` restated |
| 3 | **A declared mechanical negative was false.** *"The equipment keyword returns zero hits"* — it returns **one**, in a help string on an effectiveness metric | Corrected in `05` §3. The negative is restated as *no equipment field or reference*, with the textual occurrence named |
| 4 | **A field count was under-scoped.** *"The routing-operation model declares 20 fields"* — the base declares **22**, and **four modules inherit it**, adding 4 more. The read stopped at one file | Corrected to **26 across all five files**, all four inheritors read. **`P04-F-37`'s conclusion survives** — none of the 26 is an equipment reference |
| 5 | **`P04-B-28` over-claimed uncertainty.** The parent-of operator drops falsy identifiers and expands to a membership test, so a null company can never match; the asset rules omit the explicit null alternative the framework's own helper adds. A company-less asset group is **visible to no one** — decidable from source | `P04-B-28` **closed**. Runtime query `Q-13` withdrawn and repurposed. This was the **mirror image of the negative-claim defect**: over-claiming uncertainty where the source decides |
| 6 | **`P04-CTR-05` mis-located the contradiction.** The silent re-dating is in the **accounting core's generic posting routine**, not the asset module. It is not a per-module inconsistency | Corrected in `12` and `11` §3. The finding is **larger**: it applies to every programmatically posted entry in the product, and its owner is **P08**, not the asset domain |
| 7 | **`P04-F-49` was framed too strongly.** Two analytic lines **are** created, each with its own general-ledger account. The **net balance** is zero; the attribution exists at line level | Reframed. This changes what `BD-02` needs: a **report change** recovers the data, rather than new behaviour. The corrected statement is materially more useful than the original |
| 8 | **A consequence was missed.** Every line of the disposal entry carries the distribution and the entry is balanced, so **gain or loss on disposal also nets to zero** in the analytic ledger | Added as `P04-F-64`. A second `BD-02` breach this session did not see |
| 9 | **`P04-F-19` overstated.** The inverse fires on a **write** of the wizard field; leaving the computed default is a no-op. *"Every disposal"* would not survive challenge | Softened in `03` and `07`. The material claim — per-transaction mutation of company configuration under elevated privilege — holds |
| 10 | **`EV-23` was classified UNRESOLVED where the source decides it.** Every auto-created asset is draft or running, so the archive guard **always** raises | Upgraded to **FACT VERIFIED**, with the usable finding stated: cancelling a vendor bill that auto-created an asset is hard-blocked, with an error about *archiving* that does not describe the situation |
| 11 | **A materially worse behaviour was missed.** The clearing routine's **draft branch carries no date test**, so the draft derecognition entry is **silently deleted** by re-opening, pausing or re-valuing the asset | Registered as **`P04-B-40`**, `07` §2.1, and raised to **rank 4** in `10` §8. `P04-B-19` re-classified from UNRESOLVED to FACT VERIFIED. **The single most valuable finding of the review** |
| 12 | **`P04-F-13` needed a scope qualifier.** The confirm path and the tail of the modify wizard *do* post every non-posted entry without discriminating by type | Restated as *"no path in the disposal flow posts it"* — falsifiable as originally written |
| 13 | **`P04-F-34`'s summary contradicted its own table.** One of the "four with no host" has a host and is a control gap — and `15` `D-P04-03` records that scoring as an **open disagreement**, which the summary asserted as settled and `19` carried into the clean-room pack | Corrected in `07` and in `19`. The disagreement is now visible in the Layer-1 pack |
| 14 | **`17` §4 certified deliverables that did not exist** — files `14` and `16` | Corrected; see §3.3 |
| 15 | **The blocker count was quoted, not executed** — `17` said 26 new against a register that had grown | Re-executed: **39 register rows = 3 re-registered + 36 new.** `17` corrected. *The package quoted a count in the very file that certifies its denominator discipline* |
| 16 | `17` §5 deviation 1 **listed six identifiers and called them five** | Corrected |
| 17 | **One finding carried two identifiers** — `P04-F-18` and `P04-F-23` are the same blank-account finding, both cited downstream | Merged onto `P04-F-23`; `P04-F-18` **withdrawn** |
| 18 | **Two broken finding cross-references** in `01` §5 and `04` §5 | Both corrected |
| 19 | **`P04-REV-01`'s own count was wrong** — 21 files, executed gives **22** (10 + 12) | Corrected. An executed-count error inside the file that exists to punish quoted counts |
| 20 | **Two uncounted counts** — *"fourteen subscription modules"* (**13**, and no unit declared) and *"six non-directory entries"* (**7**, the seventh being a hidden dotfile) | Both corrected with the enumeration stated |
| 21 | **The clean-room scan was under-specified.** `19` was substantively clean on every declared token, but used **"work centre"** — the reference product's own UI label for an object whose *technical* token is on the scrub list. The scan cannot catch a UI label by construction | Replaced with SMEsPlus vocabulary. `19` now returns **0** on the UI-label forms as well |
| 22 | **The custom advance-expense module was mis-described**, and the real finding is bigger. Its data file is under the manifest's **`data`** key with the `demo` key commented out, so it loads on **every** install — creating a hard-coded general-ledger account and a product, and **setting the capitalization flag from a data file** | Registered as **`P04-B-41`** and `01` §1.3. It is also **live proof of `UC-02`/`UC-04`**: a shipped, non-interface path writing the exact field this package said the interface alone protects |
| 23 | **`P04-B-26` was broader than the evidence.** The stray artefact is a **zero-byte** file dated months earlier — a writability probe. Also unrecorded: one directory of 791 has **no manifest and no content** | Narrowed, severity reduced, and the empty module stated as a qualifier on *"primary source complete"* |
| 24 | **Lifecycle arcs missing from `02`** — the draft-clearing deletion path, and the archive arc contradicting `03` `EV-23` | Both added to `02` §3 |

### 3.2 Findings NOT adopted — the challenge was itself disproved

**The review's Tier-1 finding #1 — its headline — is wrong, and this session
disproved it against source.**

It asserted that the package's lock-date evidence citation *"is DISPROVED — no
such test exists"*, having enumerated the `fiscalyear_lock_date` occurrences in
the asset module's **main test file** and found only a cancellation test and two
mid-year lock tests with a two-month shift inside one fiscal year.

The test exists. It is `test_post_moves_after_lock_date`, in the asset module's
**board-computation** test file — a file the review did not search. It sets a
fiscal-year lock of **30 June 2021** and asserts that a **31 December 2020**
depreciation entry of 12 000 posts as **31 July 2021**: a **seven-month** shift,
into the **following** fiscal year, at **full value**. Every particular the
review called wrong is right.

> **This is the third instance in this session of one enumeration bounded to a
> subset of its own population producing a confident false negative** — after the
> three-way disagreement on the custom-addon count (`05` §6) and this package's
> own first-draft register gap (`18` `P04-REV-10`). The independent reviewer,
> briefed specifically to catch that defect, committed it.
> Recorded as `18` `P04-REV-11`.

The reviewer's **methodological** point is nonetheless adopted: the citation was
given without naming the test or its file, which is what made it expensive to
verify and easy to mis-refute. `11` §3 and `10` `P04-B-31` now name both.

**Positions preserved rather than resolved:**

| Subject | Reviewer | This session |
|---------|----------|--------------|
| The nine-path count | The unit was changed after the fact to rescue the figure | Accepted — and the fix is to publish **three** counts against three named units, not to pick one. The reviewer's implied preference for a single headline number is what produced the problem |
| `P04-F-49` framing | *"Depreciation does not reach cost centres"* overstates | Accepted at balance level. **Disagreement preserved** on consequence: the reviewer holds this makes it a report change; this session holds that a cost centre whose sum is zero is not attribution in any sense a reader of `BD-02` would accept, whatever a filtered report can recover |

### 3.2.1 What no amount of adversarial review would have caught

P11 reports its own error tally by **the control that caught each one**: 3
self-caught before challenge, 4 caught in parallel, 6 caught by adversarial
challenge, and **3 caught by P04 after publication — two of them about P11's own
material**.

Its observation is worth carrying into this package's own conclusions:

> The findings P04 returned **could not have been bought by running the
> adversarial challenge harder**, because they needed a party who had **written
> the evidence P11 was citing**.

That is a statement about **control design**, not about diligence. This package
already records that its independent review returned 24 real findings and one
false one (§3.1, §3.2), and that roughly half its statutory content went
unreviewed for want of document access (§3.3). Add P11's observation and the
conclusion sharpens:

> **P04-F-71.** **No single control was sufficient, and the controls are not
> interchangeable.** Self-challenge caught overstatements. Adversarial challenge
> caught defects the author could not see. **Peer exchange caught defects
> neither could see, because they required someone who held the other half of
> the evidence.** Scaling any one of them would not have produced what the
> others found.
> Class: **SUPPORTED INTERPRETATION** — an inference from four sessions' error
> tallies over one week, not a measured result.

### 3.2.2 The failure mode a cooperative exchange creates

P11 logged a correction against itself for **agreeing too readily**. It had
written that it adopted P04's classification *"over its own"* and framed the
deference as a virtue — grounding a classification in **who said it** rather than
in the evidence. P04 had objected to exactly that, and P11 records the objection
as correct.

P11's observation, adopted here because it completes `P04-F-71`:

> This is the only correction in the exchange for **agreeing too readily**, and
> **four expert panels instructed to attack could not have produced it.**
> Deference is the failure mode a **cooperative** exchange creates, and nothing
> in an adversarial setting rewards catching it.

> **P04-F-79.** The control taxonomy has a fourth entry, and it is the one this
> package's own four-expert challenge is structurally unable to supply. Adversarial
> review is instructed to attack, so it cannot detect **excessive agreement**;
> only a cooperative counterparty can, and only by refusing a concession offered
> to it. A package reviewed solely by adversarial means is unprotected against
> its own deference — including deference to its reviewers.
> Class: **SUPPORTED INTERPRETATION**, on two instances across two sessions.

The symmetric confirmation, from P11, of this package's closing observation:

> **Four refusals across three sessions, and not one contributed a finding —
> every one prevented a defect.** P11 declining to extend a Boss ruling to an
> axis it does not address; P11 declining to adopt an example on P04's word and
> reading the source first; P07 declining to count an error on P04's description
> of it; P04 declining to re-derive a half it could not own.

> **P04-F-80.** A cross-process seat's value is **at least as much in what it
> declines to carry as in what it composes.** This is the corrected form of an
> earlier claim in this exchange that a cross-process seat's value lay in
> composition — a claim P04 disproved and P11 withdrew.
> Class: **SUPPORTED INTERPRETATION**, on four instances across three sessions.

### 3.3 What the review could not test — declared unreviewed

The reviewer states it had no document access and therefore tested **none** of
the TAS 16 quotations or the five Thai statutory sources; none of the runtime
figures; the prior packages' imported findings except the repeated population
figure; two of the nine cost paths; the legacy source tree; and the time-based
recognition comparison.

**Roughly half this package's statutory content has had no independent
challenge of any kind.** That is a larger unreviewed surface than the AAS+
verdicts in §4 would suggest on their own, and it is stated here rather than
left to inference.

## 4. AAS+ area verdicts

| # | Area | Verdict | Basis |
|---|------|---------|-------|
| 1 | **Upstream capitalization** | **CLEARED as research** | The mechanism question is answered from primary source with a declared enumeration. The **business** position is a gap, not a finding: the capitalization decision has no owner (`P04-F-59`) |
| 2 | **Lifecycle coverage** | **HOLD** | Four lifecycle stages named by the governing prompt — transfer, impairment, scrap, derecognition-as-an-event — have **no host**. That is established. What SMEsPlus should do instead is **not designed**, and this session was not asked to design it |
| 3 | **Retire end / TAS 16** | **HOLD** | Four of seven derecognition requirements have no host. But every TAS 16 row rests on an **explanatory manual that says it is not the standard**. The classification is correct and the gazetted text has now been outstanding across **two** packages |
| 4 | **Period integrity** | **FAIL — of the current state, not of the research** | A depreciation charge aimed at a locked period is **silently re-dated into another financial year**, asserted by the estate's own test. Until that is decided and designed, no statement that period control holds for assets is supportable |
| 5 | **Sub-ledger integrity** | **FAIL — of the current state** | No reconciliation exists; six mechanisms break agreement; none is detected |
| 6 | **Cost handoff** | **HOLD, and worse than at the previous gate** | The veto's second limb is **wider**: nine paths, one of the two previously named as live **nets to zero**, and a **new** live ledger mismatch was found under standard costing |
| 7 | **Attribution (`BD-02`)** | **HOLD** | Two new breaches by the reference behaviour, and the obvious control **cannot fire** |
| 8 | **Scope / SaaS integrity** | **HOLD — narrowed from the prior FAIL** | Correctly narrowed under the correction to the one object class that creates a financial effect. **Warning attached:** narrowing a High finding on a constitutional correction is exactly when a real defect quietly disappears. It must not later be cited as a clearance |
| 9 | **Statutory evidence** | **CLEARED** | Five sources retrieved, classification discipline applied and stated, one summary-derived assertion discarded on reading the source, two questions routed rather than inferred |
| 10 | **Prior-evidence import** | **CLEARED, and it found something** | The import is faithful, and it surfaced that **ten registered open items ceased to appear** across three packages |
| 11 | **Denominator discipline** | **CLEARED with a recorded failure** | Two populations carried by assertion were executed and **both were wrong**. Three parallel streams disagreed and one produced a false negative. The discipline worked **because it was executed** |
| 12 | **Governance** | **CLEARED** | No prohibited wording anywhere; Layer-1 file scans clean on every token; no Boss question put; no freeze declared |
| 13 | **Independence** | **NOT CLEARED** | §1 |

**AAS+ overall position: HOLD.**
**Recommended terminal state: READY FOR CORE ACCOUNTING RECONCILIATION.**
Not a freeze, not an approval, not an authorisation to develop.

## 5. AAS+ findings raised against this research

| # | Finding | Severity |
|---|---------|----------|
| **A+1** | The package **establishes gaps and does not design remedies** for the four unhosted lifecycle stages. That is within its brief, and a reader who takes "no host" as a specification will be disappointed. The gaps are named; the designs are not | Medium |
| **A+2** | **All TAS 16 conclusions rest on an explanatory manual.** The gazetted text is one retrieval away and has been outstanding across two packages. Every finding is classified correctly today; the risk is that a later reader upgrades them | **Medium-High** |
| **A+3** | **The nine-path enumeration is not comparable to the prior two-path count**, and a reader will compare them. The caveat is now stated, and it is a caveat, not a fix. The only real fix is to re-run the prior count under this unit | Medium |
| **A+4** | The **third `BLK-07` option** is genuinely new and genuinely under-examined. It changes the depreciation charge, and its tax consequences were **not researched**. It is offered as an option with that caveat attached — but options offered at a Final Gate tend to get chosen | **Medium-High** |
| **A+5** | **Six blockers depend on runtime evidence that no session has yet obtained**, and the priority-1 runtime query — the installed-module list — has now been outstanding across **three** packages. Every "not found" in three packages is bounded by it | **High** |
| **A+6** | The **handover-residue finding** is the most transferable thing here, and this package has **no mechanism** to stop its own 40-plus blockers suffering the same attrition. It recommends a rule; it does not implement one | **High** |
| **A+7** | `P04-B-18` and `P04-B-19` are **code paths with no test coverage in the estate itself**, reported as UNRESOLVED. Correct — and it means two disposal-related behaviours are unknown to the vendor as well as to us | Medium |
| **A+8** | The scope matrix assigns scope to **fourteen objects** on business, legal and accounting semantics. Two are on HOLD; the other twelve are **reasoned, not evidenced**. They are classified as SUPPORTED INTERPRETATION where it matters, and a reader should not treat the matrix as a survey of what the platform does | Medium |

## 6. The veto

The standing veto — **no implementation of the costing model may begin before the
denominator is decided and the single-mechanism condition is proved** — is
**endorsed and not discharged**.

> Its second limb is **further from discharge after this session than before it**.
> Nine paths, not three. One of the two previously named as live **does not
> behave as named**. A new live ledger mismatch was found that no prior package
> recorded.

That is the correct outcome of an honest enumeration, and it is stated as a
widening rather than dressed as progress.

## 7. What AAS+ would want done next, in order

1. **One runtime session.** It closes six blockers and caps every negative
   finding in three packages. It has been asked for three times.
2. **Decide the locked-period policy** — refuse or re-date. It is live behaviour
   misstating a financial year, not a design gap.
3. **Retrieve the gazetted TAS 16 text.** It converts a whole class of findings
   from interpretation to standard.
4. **Adopt a carry-forward rule that tracks open items**, before this package's
   blockers meet the same attrition the package documents.
