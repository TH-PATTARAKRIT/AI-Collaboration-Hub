# P11 — RESEARCH ERROR AND REVISION LOG

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> This log records **this session's own errors**, not other packages'. Errors found in other packages
> are contradictions and live in `P11_CONTRADICTION_REGISTER.md`.

---

## `P11-E-01` — a headline figure contradicted its own table

| | |
|---|---|
| **Where** | `P11_UNIFIED_EVENT_OWNERSHIP_REGISTER.md` §2 |
| **Error** | The headline was drafted as *"`C2` fails for **8** of 44"*. Re-deriving the count from the §3 table returns **9** business facts |
| **Cause** | The draft figure was written before the table was finished and was not re-derived afterwards |
| **Detection** | Self-caught, by re-deriving the count from the table rather than restating the headline |
| **Correction** | Stated **inside the affected file**, adjacent to both figures, with the corrected value: **`C2` fails for 9 of 44** |
| **Why it is logged at all** | This is **`GB-06`'s exact shape** — a published count contradicting the dispositions beneath it — and it is the defect that produced `FC-F1` in the parent programme. It occurred here, in the first session to write about it. **A log that only recorded other people's instances of `GB-06` would be evidence that the control does not work** |

## `P11-E-02` — the superseded scope assumption

| | |
|---|---|
| **Where** | Every scope statement written before constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` was received |
| **Original assumption** | Tenant context + company context mandatory for every operation, inherited from `BC-02` element 10 and Wave A `TI-01` |
| **Why over-constrained** | `PLATFORM`-scoped reference data legitimately requires neither; a blanket rule would forbid the platform layer from existing |
| **Correction applied** | `P11_SCOPE_OWNERSHIP_MATRIX.md` created; five revalidations `RV-01`…`RV-05` recorded in full, each with original finding → assumption used → why over-constrained → correct analysis → updated classification → architecture impact → cross-process impact → evidence required |
| **Scope of rework** | **Delta only.** No evidence discarded, no checkpoint re-run, no completed enumeration repeated. Findings **not** touching the assumption are preserved byte-for-byte |
| **Net effect on severity** | **`RV-05` did not relax.** The 10-of-10 element-10 failure stands, because all ten material handoffs create a financial effect and are `COMPANY`-scoped. `RV-02` and `RV-03` **sharpened** their findings without changing either disposition. `RV-04` **narrowed** one blast radius. `RV-01` corrected a rule's reach while preserving its intent |

> A correction that relaxes a rule invites the reading that failing counts relax with it. **They did
> not, in four of five cases.** Recording the direction of each revalidation — rather than assuming
> it — is the whole point of running them.

## `P11-E-03` — a peer clone was mis-enumerated on the first pass

| | |
|---|---|
| **Where** | The first peer-intake sweep |
| **Error** | The glob `ACCOUNT_P0*_2026_09_04_EXECUTION` **silently excluded `P10`**, whose directory is `ACCOUNT_P10_TBR_...`. The first reading was "nine clones exist, `P10` has none" |
| **Cause** | An author-chosen pattern that did not cover its own declared population — **the exact defect the denominator rule exists to prevent**, committed while writing the file that states the rule |
| **Detection** | Caught when the enumeration script was written with the population declared **first**, which forced the pattern to cover `P10` |
| **Correction** | `p11_scripts/peer_intake.sh` and `peer_wip_snapshot.sh` both enumerate `P0[1-9]` **and** `P10` explicitly. All counts in this package are from the scripts, not from the first sweep |
| **Consequence if undetected** | The register would have reported a **9**-process peer dependency instead of **10** |

## `P11-E-04` — a peer working tree changed between two observations

| | |
|---|---|
| **Where** | `P01`'s working tree, between the intake script and the WIP snapshot, minutes apart |
| **Not an error — a property of the observation** | The peer sessions are **live**. `P01` showed `worktree_changes=0` on the first run and one untracked file on the second |
| **Correction to method** | Every peer-state count in this package is stamped `SNAPSHOT_UTC=2026-09-04T22:41:38+0700` and is described as a reading at an instant, not a stable population |
| **Why it is logged** | Because the alternative — reporting a count of peer work-in-progress as a finding — would have been a measurement presented as a fact about the programme |

---

## Summary

| Measure | Count |
|---|---|
| Errors made by this session | **3** (`P11-E-01`, `P11-E-02`, `P11-E-03`) |
| Self-caught before publication | **3 of 3** |
| Caught by an external reviewer | **0** — and this is **not** evidence of quality. `EC-07` requires two consecutive clean independent passes; this session has had **none** |
| Method observations logged | **1** (`P11-E-04`) |

---

# PART 2 — POST-CHALLENGE

## `P11-E-05` — a Boss ruling inverted and attributed to the ruling that superseded it

| | |
|---|---|
| **Where** | `P11_SCOPE_OWNERSHIP_MATRIX.md` §3 product-master row; repeated in `P11_SAAS_ACCOUNTING_BOUNDARY.md` §1 |
| **Error** | P11 recorded *"Product master \| `TENANT` (per Boss ruling `D-01`)"*. `MTI-D-01` rules **`OPTION B — Company-owned Product Master`**, and its §4 records that the ruling **supersedes** the earlier AAS+ recommendation preferring a tenant-level master. P11 reinstated the superseded position and cited the ruling that killed it as its authority |
| **Why it matters beyond the row** | P11's own table defines `TENANT` as *company context not required*. The placement therefore licenses exactly the shared cross-company product identity the ruling refuses — and the ruling's stated business reason is two companies performing a same-looking transport service under **different withholding-tax conditions** |
| **Detection** | **Three times independently** — P11's own re-read of the ruling, `X3-F06`, and `X1-F01` |
| **Correction** | Product master → `COMPANY` owns/mutates; a separate `TENANT`-scoped **mapping-layer** object added per ruling rule 5 (reference only, no financial effect) |

## `P11-E-06` — an undecided decision package listed among the controls that govern the round

`BC-04` sat in the table headed *"Boss-approved controls that **govern** this reconciliation"* while
the GB-08 artefact reads **`BOSS DECISION REQUIRED — GB-08` / "This file does not select an option"**
— and P11's own `DEP-14` says *"packaged, not decided"*. **§1's declared POPULATION was contaminated
by it**, because the population is defined as *"named in a `PEER-PUBLISHED` artefact or a
`BOSS-APPROVED` control"*. Found by `X1-F02`. Reclassified to `PEER-PUBLISHED`, pending decision.

## `P11-E-07` — the trace-lane headline contradicted itself in one sentence

*"2 reach a statement line without an unresolved break … and each carries an open tolerance-zero or
contract failure at the end of the lane."* Self-caught, and independently by `X4-F12`, which
re-derived **3** lanes with no ✘ and **0** free of an unresolved break. Corrected to state both tests
separately.

## `P11-E-08` — accounting-standard requirements presented as Thai statute

`P11_TAX_ARCHITECTURE.md` §1 headed three positions *"Statutory"*. The source reserves
`THAI STATUTORY REQUIREMENT` for Revenue Code s.65 bis (2) and Royal Decree 145 alone, classifies
TAS 2 ¶12/¶13 as **`ACCOUNTING STANDARD REQUIREMENT (TFRS)`**, and the DBD finding as
**`THAI REGULATORY FACT`**. Self-caught and independently by `X3-F01`. **P11 closes no
`THAI STATUTORY REQUIREMENT`.**

## `P11-E-09` — two of TAS 2 ¶13's four requirements dropped

Requirement **1** (normal capacity *"taking into account capacity lost to planned maintenance"*; the
actual level may be used **if close to normal capacity**) and requirement **4** (in abnormally high
production the per-unit fixed amount is **reduced**, so inventory is **not carried above cost**).
Consequence: `CVP-01` mandated absorption **with no upper bound** — the half of ¶13 that protects the
balance sheet. Self-caught and independently by `X3-F02`.

## `P11-E-10` — `DC-09` overclaimed as novel

The Asset package already names the **analytic-tag-plus-rate** variant: *"if depreciation reaches
product cost **both** through an analytic tag **and** through a derived machine rate, nothing in the
platform notices."* P11's contribution is the **expense-relief** variant only. Self-caught. Both are
now registered, and `P04` has since shown the true count of competing monetisations is **five**.

## `P11-E-11` — the stated subledger rule was not the rule applied

`X2-F06`, **CRITICAL**. §1 declares *"a structure failing `S3` **or** `S4` is a derived view"*; §2
applied *"fails both"* and awarded *"of record"* to four rows failing one criterion. Under the stated
rule the register reads **3 of record, 5 derived views, 2 unknown** — and `X2-F07` then shows AR and
AP fail on the same evidence used to fail Settlement, taking *"3 unqualified"* to **0**. **A logic
error, not a citation error.**

## `P11-E-12` — a pattern that could not cover its declared population, twice

`P11-E-03` recorded the first instance (a glob excluding `P10`). `X4-F02` found the second and worse
one: **`peer_intake.sh` section C was inert by construction** — `set -e` plus a piped `for` loop
killed the subshell at the first ref with no match, so declared PATTERN (b) **could never return a
hit**. The published empty result was an **artefact**, not a measurement. Corrected as v2 with the
`set -e` removed, `|| true` per ref, and a **positive control** whose value (86 matching paths) makes
an empty section C evidence rather than silence.

> **This is the most serious methodological failure of the round.** The defect was invisible to every
> reading of the script and was found only by an independent party **executing** it. It is the
> programme's own rule — *a denominator must be executed, not quoted* — proven again, against the
> session that wrote the rule down.

## `P11-E-13` — the negative-claim boundary was declared once and not applied package-wide

`X2-F11`, `X1-F11`, `X4-F14`. `F7` was stated *"not implemented at all"* where the governing CORR1
disposition is **`PARTIALLY VERIFIED`** — *"a real database constraint exists, but only with an
optional module installed, and it is **table-global rather than tenant-scoped**"*. And `X4-F14`
established that the blanket class-`C` demotion was simultaneously **over-broad** (two packages **did**
declare exhaustive search boundaries) and **inconsistent** (P11 relies on those same negatives as
fact). **P11 conflated *applicability* with *verification*: `MCU-21` is which root SMEsPlus targets,
not which scope was searched.**

## `P11-E-14` — the premise expired mid-session

Recorded in full at `P11_PEER_INTAKE_DELTA_01.md`. P11's synthesis was written against **0** published
peer packages; its four-expert challenge was commissioned against **0** and reviewed against **2**;
**six** had published by session close, and **two were already at a later SHA than P11 read**.

**Not an error of fact** — every count was stamped and labelled a reading at an instant, and one
reviewer declined to endorse it rather than assume it. **It is an error of sequencing**: a
reconciliation was scheduled before the things it reconciles existed.

---

## Summary — both parts

| Measure | Count |
|---|---|
| Errors made by this session | **13** (`P11-E-01`…`P11-E-14`, less `P11-E-04` which is a method observation) |
| Self-caught before the challenge | **3** |
| Self-caught in parallel with the challenge | **4** |
| Found only by independent challenge | **6**, including both CRITICAL |
| Findings raised by the four panels | **86** · accepted **86** · disputed **0** |
| Defects found by two or more panels independently | **6**, three of them found three times |
| Errors corrected at source in this session | see `P11_BOSS_FINAL_GATE_PACK` §26 |

> **The controlling lesson, and it is not new — it is the fourth recorded instance:**
> **independent review found what self-review could not, and the two it found first were the two that
> invalidated the round's own instruments.** Self-review found 3 before the challenge; the challenge
> found 86, including a broken evidence script and a rule stated one way and applied another. A
> round that reported only its self-caught errors would have published a false picture of its own
> reliability.

---

# PART 3 — POST-PUBLICATION, PEER-CAUGHT

## `P11-E-15` — a count published without its declared population

Logged in full at `P11_PEER_INTAKE_DELTA_03.md` §5. P11 published *"the fourth instance in the
programme and the second in this session"* **without declaring the population it counted over** — in
the delta arguing that counts must declare their population. Reconciled by declaring both units.

## `P11-E-16` — a tolerance-zero boundary drafted narrower than P11's own evidence

**Where.** `T0-13`, as opened at `P11_PEER_INTAKE_DELTA_03.md` §3.

**Error.** Scoped to *tenant crossings*. `P04-F-68` (`FACT VERIFIED`) establishes the silent re-dating
needs **no tenant boundary and no company hierarchy** — inside a single company an entry aimed at a
locked period is already mutated with no refusal and no trace. **A boundary that can be satisfied
while the defect persists is not a boundary.**

**Why it is worse than the peer reported.** P04 found the wider scope in P04's evidence. **P11 already
had it in its own.** `P11_UNIFIED_ACCOUNTING_EVENT_REGISTER.md` §2 records four accounting events
**invisible at the moment they occur**, two of which are **single-company re-datings** — `UAE-04`
(*"the posted record carries no trace that its date was moved"*) and `UAE-05` (*Visible?* **no**;
*"fires with no lock configured"*). Neither needs a tenant. Both predate `T0-13` by four documents.

**Cause, identified rather than described.** `T0-13` was drafted *while* composing the cross-tenant
compound and took its scope from the case in front of it rather than from the register that already
generalised it. **A boundary derived from its triggering instance inherits that instance's scope.**
Recorded as a method note: when opening a tolerance-zero boundary, re-derive its scope from the
register, never from the finding that prompted it.

**Correction.** Widened to every scope — `PLATFORM`, `TENANT`, `COMPANY` — with the tenant crossing as
the aggravated case. `T0-13` is consequently **not contingent on `D-12`** and is a **present defect,
not a prospective risk**.

## `P11-E-17` — an attribution published without opening the file cited two lines earlier

**Where.** `P11_PEER_INTAKE_DELTA_03.md` §2, classification paragraph.

**Error.** P11 published that the `P04-F-66` + `P04-B-31` compound *"is P11's… neither component was
composed by its owner"*, and drew from it *"the whole argument for a cross-process seat existing at
all"*. **The compound, and the exact phrase P11 used as its headline, were composed by P04** in
`20_P04_SCOPE_OWNERSHIP_MATRIX.md` at `3c10b4e`, under the heading *"Compounding with `P04-B-31`"* —
**the same commit P11 cited two lines earlier as the source of `P04-F-66`** — and were sent to P11
verbatim under an explicit heading before intake.

**Aggravating.** The heading appeared in **P11's own terminal output**: the grep run to verify
`P04-F-66` printed lines 232–234 of that file. P11 saw the heading, did not open the passage, and
published a claim about it.

**Class — RECLASSIFIED at `P11_PEER_INTAKE_DELTA_05.md` §1, on P04's argument, which is better than
P11's original filing.**

> ~~Identical to `P11-E-15` — a claim published without its evidence opened — committed in the same
> message that logged `P11-E-15`. Seventh instance across five actors.~~

**Governing classification: `Class 1 — secondary source substituted for primary.` Remedy: open the
file.** It is **not** the enumeration class, whose remedy is *execute the count*. **Nobody's search
was too narrow here** — the grep found the right file and printed the right line; the failure was
**downstream of the search**. P11 filed it by surface resemblance to `P11-E-15`'s prose rather than by
**remedy**, which is the only thing a class is for.

**The extension P11 adopts from P04, and it widens the class:** *a grep result is a summary of a
file.* Treating it as the file is the same substitution as treating a search snippet as a ruling — so
Class 1 reaches **any tool output that stands in for its source**, not only search-engine summaries.

*It remains true that this was committed in the same message that logged `P11-E-15`; that is a fact
about timing, not about class.*

**Correction.** `P11-F-06` reclassified `PEER-PUBLISHED`, owner P04. The false text is retained struck
through at source, with lineage. The surviving P11 contribution is stated exactly and is smaller:
**the value was the prompt, not the composition** — P11's `SR-02` question is what sent P04 to read
the lock-date implementation.

**And the example was replaced.** The claim *"this is the argument for a cross-process seat"* now
attaches to a case P11 verified independently at `P07`@`ecc6059`: a statutory definition P04 had read
and P07 had not produced two gaps in P07's own VAT model — a missing deemed-supply row (`P07-D-30`:
*"the VAT limb is P07's and is the half that would otherwise be missed"*) and a *"no instalment tax
point found"* recorded **without knowing the rule it was measuring against** (`P07-F-59`). **The
second is a negative claim whose boundary was unknowable from inside one process.** That is the
argument; the lock-date compound was not.

---

## Summary — all three parts

| Measure | Count |
|---|---|
| Errors made by this session | **16** |
| Self-caught before the challenge | 3 |
| Self-caught in parallel with the challenge | 4 |
| Found only by independent challenge | 6, including both CRITICAL |
| **Found only by a peer process, after publication** | **3** — `P11-E-15` (partly), `P11-E-16`, `P11-E-17` |
| Corrections published **at source** rather than as footnotes | **all** |

> **The controlling lesson, fifth recorded instance and now demonstrated three ways:** self-review
> found 3; independent adversarial challenge found 86; **a peer process reading the same evidence
> found 3 more that both had missed — two of them errors about P11's own material.**
>
> No single control was sufficient. The peer catch is the one that could not have been bought by
> running the challenge harder, because it required a second party who had **written** the evidence
> P11 was citing.

## `P11-E-18` — an actor count inherited from a peer and never executed

**Where.** `P11_PEER_INTAKE_DELTA_03.md` §5 and this log's `P11-E-17` entry: *"across **five**
actors"*.

**Error.** Re-derived from P04's own original enumeration — parallel research stream · P04's first
draft · adversarial reviewer · **P04 again** on a field count · P11's script — the actors are
**four**, not five. P04 repeats. The figure was **already wrong in the message P11 received it in**,
and P11 published it without re-deriving it.

**Class.** The executed-not-quoted rule, broken by P11, **in a tally about counting**, inside a delta
whose §5 reconciles two counts. The first error in this exchange that P11 **inherited** rather than
originated — the failure mode a reconciliation function is most exposed to and least protected
against, because its whole input is other parties' figures.

**Structural fix — `P11-G-02`.** A **cross-party tally cannot be executed by either party**: P11
cannot open P04's drafts, and P04 has not read P11's register and says so. Neither can verify more
than its own half, so a single joint figure is **unexecutable by construction** — and every joint
figure in this exchange has been wrong. **A cross-party count is published as two declared halves,
each executed by its owner, never as one number.**

**P11's half — ~~executed: 2~~ CORRECTED at `P11-E-19` below. It is 5, and it was not executed when
first published.**
**P04's half:** carried `PEER-PUBLISHED` at `cc332d9`, not re-derived.

---

## Summary — all parts, corrected

| Measure | Count |
|---|---|
| Errors made by this session | **27** |
| Self-caught before the challenge | 3 |
| Self-caught in parallel with the challenge | 4 |
| Found only by independent adversarial challenge | 6, including both CRITICAL |
| **Found only by a peer process, after publication** | **5** — `P11-E-15`, `-E-16`, `-E-17`, its reclassification, and `-E-18` |
| **Found by applying a peer's rule to P11's own figure** | **1** — `P11-E-19` |
| **Found by a peer correcting P11 for agreeing too readily** | **1** — `P11-E-21`; unreachable by adversarial challenge |
| Corrections published **at source** | **all** |
| Of P11's errors, in the **enumeration** class | **6** — `P11-E-03`, `-E-12`, `-E-15`, **`-E-16`**, `-E-18`, `-E-19`. `E-16` added by `P07`'s ruling, which cost P11 its only proposal instance |
| Of P11's errors, in the **secondary-source** class | **1** (`P11-E-17`) |
| Unplaced by agreement | **1** (`P11-E-20`) — `P07` declined to place it and P11 does not tidy it onto a shelf |


> **`P04-F-71`, adopted with P04's classification (`SUPPORTED INTERPRETATION`) over P11's flat
> assertion:** the controls are **not interchangeable**. Self-review caught overstatements;
> adversarial challenge caught what the author could not see; **peer exchange caught what neither
> could, because it needed a party who had *written* the evidence the other was citing.** Scaling any
> one harder would not have produced what the others found. An inference from four sessions' tallies
> over one week — not a measured result.

## `P11-E-19` — a declared half published without enumerating it

**Where.** `P11_PEER_INTAKE_DELTA_05.md` §3 and this log's `P11-G-02` entry: *"P11's half, executed:
2 — `P11-E-12` and `P11-E-15`."*

**Error.** It was **not executed**. Enumerated this session by parsing the log
(`grep -n '^## \`P11-E-'`), the enumeration/denominator-class instances are **five**:

| id | Instance |
|---|---|
| `P11-E-03` | a glob that excluded `P10` — the pattern did not cover the declared population |
| `P11-E-12` | an intake script inert by construction — the pattern could not fire |
| `P11-E-15` | a count published without its declared population |
| `P11-E-18` | an actor count inherited from a peer and never executed |
| `P11-E-19` | *this entry* — a half asserted rather than enumerated |

**Two omissions, and the second is the telling one.** `P11-E-03` was simply overlooked.
**`P11-E-18` was logged in the same delta that published the half as 2** — the count was wrong about a
member that appeared four paragraphs above it.

> ### The rule failed on its first application, by its author, in the document that opened it.
>
> `P11-G-02` requires each party to **execute** its own half. P11 published its half in the same
> breath and **asserted** it. The rule is not wrong; **stating a rule and applying it are different
> acts, and this is the second time this session that gap has produced a defect** — the first was the
> subledger test, whose stated rule (`S3` **or** `S4`) was not the rule applied (*fails both*).

**Correction.** The half is **5**, enumerated by parse, with the command published beside it. Carried
to `P07`, whose standard records P11's half as *"≥1"* on the strength of the same understated figure.

**Class.** Enumeration — an assertion standing in for an execution — which is why it is a member of
the very set it miscounted.

## `P11-E-20` — a correct finding published with an overstated consequence

**Where.** Messages to P04 and P07, and `P11_PEER_INTAKE_DELTA_05.md` §2: the identifier error was
raised as **time-critical because it would otherwise land in P07's programme standard**.

**Error.** The premise was false. **It never reached the standard.** P07 had already declined to count
it, on a ground that predates anyone knowing there was an error: *"I have not read it. I have your
description of it. Adopting a class assignment for an error on the strength of a peer's summary of
that error would itself be Class 1, committed inside the file that names Class 1."*

**P11 was right about the error and wrong about the exposure.** The containment came from a rule
applied **unconditionally**, not from P11's alert. P04's formulation is adopted verbatim: **P07 had no
reason to doubt the identifier; it declined on the *class of the evidence*, not on its plausibility —
and a discipline that only fires when you suspect a problem is not a discipline.**

**Class.** Not a factual error in the finding; an unverified claim about **downstream state**. P11
asserted what a third package would do without reading that package. The remedy is the one P11 keeps
re-learning from the other direction: **P07's file was openable, and P11 did not open it before
describing its behaviour.**

## `P11-E-21` — a correct classification adopted for a partly wrong reason

**Where.** `P11_PEER_INTAKE_DELTA_05.md` §5: *"P11 adopts P04's classification **over its own**"*,
framed as *"the discipline improving by crossing a boundary"*.

**Error.** That grounds a classification in **who said it**. P04 objected, and is right: *"I would
rather it not become a pattern of deference in either direction. I classified it that way because four
sessions' tallies over one week is an inference, not because your statement was careless."*

**The right ground**, adopted: `P04-F-71` is `SUPPORTED INTERPRETATION` **because four sessions'
tallies over one week is an inference** — and it would be that if no peer had ever mentioned it.

**Forward rule, adopted and symmetric:** if a fifth or sixth tally holds, the classification **moves
up without either party's permission**.

> **This is the only correction in the exchange for *agreeing too readily*, and it is the one an
> adversarial challenge could not have produced.** Deference is the failure mode a cooperative
> exchange creates; four expert panels instructed to attack could not have surfaced it, because
> nothing in that setting rewards it.

## `P11-E-22` — an incapacity asserted and never tested, inside the rule about what can be executed

**Where.** `P11_PEER_INTAKE_DELTA_05.md` §3 and `P11-G-02`: *"`P04`'s half: carried `PEER-PUBLISHED`,
not re-derived, **because P11 cannot open the artefacts it rests on**."*

**Trigger.** `P04` confessed `P04-REV-19` — it had claimed it could not read P11's register, the claim
was **false and never tested**, and one `git fetch` disproved it. **P11 tested its own analogous
statement rather than treating the confession as one-sided.**

**Executed.** `git show <P04>:…/18_P04_REVISION_LOG.md` at `ae525fc` returns **20** `P04-REV` ids and,
at line 103, `| **Total** | **9 instances · 4 distinct actors** |`. **`P04`'s half is enumerable from
its published package. P11's stated reason was false.**

**Class.** The negative-claim defect turned on P11's **own capabilities** — the programme's *"never
declare no code access from a working-tree search"*, committed about a **peer** instead of a source
tree, **by the author of the rule about what can and cannot be executed across a boundary**.

**Correction, adopting `P04`'s bound.** A cross-party **tally** may be unexecutable — neither party can
enumerate the other's unpublished drafts. A cross-party **citation** is always verifiable, because the
branch is published. `P11-G-02` stands for tallies over unpublished material and **never licensed
declining to open a published artefact**. `P04`'s half is now carried **verified-as-stated**, with
per-row classification left to its owner.

> **Both parties asserted an untested incapacity about the other while jointly building a rule about
> what can be executed across the boundary between them.** Neither noticed until one of them ran the
> command.

## `P11-E-23` — an internal contradiction in P11's method proposal, which produced a peer dispute

**Where.** `P11_METHOD_PROPOSAL_OCCASION_SCOPED_GENERALISATION.md` §2 vs §3.

**Error.** §2 argues the pattern is **not** Class 2 **by mechanism** — *"this pattern contains no
substitution at all"*. §3's routing rule classifies **by remedy** — *"register never enumerated →
Class 2"*. **On `P11-E-16` they reach opposite verdicts.**

**Consequence, and it is not internal.** Two peers each applied one half correctly and reached
opposite conclusions: `P07` reduced `P11-E-16` to Class 2 on §3; `P04`'s `F-78` routes it to the
pattern on §2's logic. ~~**The dispute was manufactured by P11's own file**~~, and neither peer erred.

> **CORRECTED `2026-09-05` — the self-attribution was too broad.** `P07` @ `9a99c01` found the *same*
> split in its own file: §4a reads *"an assertion stood in for an execution"*; §3.1a reads *"the
> arithmetic was simply not performed"*. **Neither says whether an execution had to be *attempted*.**
> `P04` read the first, P11 read the second, **and both were reading `P07` accurately.**
> **The ambiguity was jointly produced by two files, not manufactured by P11's alone.** `P07` has
> corrected its own to *"an assertion standing in for an **owed** execution"*.
>
> Recorded because an over-broad self-blame is still an inaccurate record, and this exchange has twice
> shown that accepting a peer's framing of one's own conduct without testing it is its own defect
> (`P11-E-21`).

**Why P11 does not settle it.** Resolving in favour of §2 restores the proposal's only instances —
P11's **and** `P04`'s. **Both parties to the test benefit from one outcome.** A classification settled
by the two parties it rescues is the structural form of every defect this exchange has caught.
Routed to `P07`, which benefits from neither, and to Boss.

**RESOLVED `2026-09-05`, against P11.** `P07` — routed to precisely because it benefits from neither
outcome — ruled on the only question it owns: *"'an owed enumeration was never performed' is inside
Class 2 as written… your routing of your own instance stands."* **`P11-E-16` is Class 2.** §3's routing
rule stands; **§2's mechanism argument was the wrong half of P11's own file**, and the proposal is
**withdrawn as a competing class**. P11's enumeration half **rises from 5 to 6** as a direct
consequence — *a half that only ever falls is not being executed.*

> **The merits are recorded in both directions** at Delta 09 §2, including the argument **against**
> P11's own interest: a class defined by its **remedy** should cover the case its remedy fixes, and
> executing a count would have caught both instances.

**`P07`'s ruling (`9a99c01` §4d) adopted that argument as dispositive, and defeated P11's own
consistency argument on a disanalogy P11 had missed:**

> `P11-E-20`'s assumption substitutes for an **inspection** — opening a document — and Class 1 covers
> that only where a **proxy** is present, which there was not; it stays orphaned. `P11-E-16`'s scope
> claim substitutes for an **execution** — *a scope is a claim about a **population**, and a population
> claim owes an enumeration.* **`E-20` substitutes for reading; `E-16` substitutes for counting. Not
> parallel.**

The correct line is therefore **"was an execution *owed*"**, not `P04-F-78`'s *"was one attempted"* —
*"whether the author realised it does not change what was owed, and an intent test would be unworkable
anyway."*

## `P11-E-24` — a cost classification resting on an untested capability claim

**Where.** `P11_FINAL_BLOCKER_REGISTER.md` §3: `MCU-19` filed under *"A running instance"*.

**Error.** `MCU-19` asks *"does any migrated/restored **database** hold a rate row whose company has a
parent?"* — **a database question, not a runtime one.** Readable PostgreSQL dumps exist on this host
and the installed client reads at least one. **The classification was an untested capability claim**,
and it sat in the column the Boss pack uses to rank cheap work.

**Trigger.** `P04` @ `7d4ca03`, applying `P07`'s generalisation: *a statement that something is
unavailable to this session is a capability claim, and a capability claim is evidence.*

**Boundary declared.** P11 verified dumps exist and are **partly** readable — one archive header reads,
another is rejected as an unsupported version. **P11 did not answer `MCU-19`**: table-data extraction
was **refused by this session's permission boundary**, and P11 does not assert an answer it did not
obtain. Corrected cost: **`UNKNOWN, plausibly cheap`**.

**Class.** Same family as `P11-E-22` — an untested claim about what this session can reach — but turned
on **the evidence base** rather than on a peer. Fourth version in this exchange, and **the first to
reach a Boss-facing decision input** rather than a method register.

## `P11-E-25` — a capability test that stopped at the first failing tool

**Where.** `P11-F-09`: *"`iTEST02_2026-07-14` archive header — **NOT readable** — unsupported version
(1.16) in file header."*

**Error.** True of the **default** client (`pg_restore 16.15`) and **false of the host**.
**`postgresql@18` is installed on the same machine** and reads the archive: **26,804 TOC entries.**
Credit `P07`, which tested its own incapacity, found a 65 MB dump **inside its own declared path set**,
and warned: *"stopping there yields a **`TESTED`** incapacity that is still false. A capability test
that stops at the first failing tool is not a capability test."*

**Why it is sharper than `P11-E-22`.** `E-22` was an incapacity **asserted and never tested**. This one
**was** tested — and the test was incomplete, so it produced a false negative wearing the authority of
an execution. **A `TESTED` label is not a boundary; the tool used is.**

**Correction.** All dumps tested are readable with the right client. The finding's *"readability is not
uniform"* is withdrawn: the true unit is **the (artefact, tool) pair**, and a negative result binds only
the tool used.

## `P11-E-26` — a correction register that claimed corrections not made

**Where.** `P11_AAS03_FINAL_CHALLENGE.md`, the `ACCEPTED — CORRECTED` disposition column, across 86
findings.

**Error.** Audited against the actual register text, **ten** accepted findings — including the round's
**only CRITICAL**, `X2-F06` — were **never edited into the registers at all**. Three of them P11 had
explicitly described as *"corrected in place"*.

**Trigger.** `P04` @ `6953856`, naming a defect neither session had: **"a revision log is not a
correction; the edit is."**

**Severity — the highest in the package, and it is about the package.** The challenge file is what a
reader consults to conclude the work was repaired. A disposition column reading `ACCEPTED — CORRECTED`
over an unrepaired register **is a false assurance about all 86 findings**, not an error in one.

**Disposition.** Nine repaired at source this session. **`X2-F06` deliberately not repaired** — it needs
ten subledger rows re-run against the stated rule, under which the register's *"3 unqualified"* becomes
**0**. **Head of the CORR1 backlog.** *Bodging a critical logic error to clear an audit is how it got
here.*

## `P11-E-27` — the audit that found `E-26` failed first, in the same way

P11's first pass used grep patterns whose escaping silently did not match, and reported **"corrected"**
for four findings that were **all still present**. Only direct per-file checks got the real answer.

**This is `P11-E-12`'s inert-pattern defect recurring for the third time — inside the audit written to
catch exactly this class.** *A pattern returning a clean result is not evidence until it has been shown
able to return a dirty one.* It is the same positive-control rule P11 published for
`peer_intake.sh` and did not apply to its own audit thirty commits later.

## `P11-M-01` — a peer's verification is still a secondary source (method note, not an error)

`P07` declined to discharge its own conditional on **P11's** verification of `P04-B-31`, and read the
artefact itself. Its reason is a sharpening P11 had been applying too loosely:

> *"Your message is a **peer's verification of a third party's artefact**, which is one step further
> from the source than the case that started this whole thread… Separating the test from the facts only
> works if whoever discharges it goes to the facts."*

**Correct, and it bounds P11's own conduct.** P11 verified `P04-B-31` at source — one step from the
artefact. `P07` receiving that through P11's message would have been **two**. Class 1's mechanism
reaches it: *a summary standing in for a source*, where the summary happens to be a competent peer's
verification.

**Standing note:** offering a verification to a peer discharges nothing for that peer. It supplies a
**citation they can execute**, and executing it remains theirs. P11 will not again describe a
conditional as *"discharged"* by its own reading on another party's behalf — the correct phrasing is
*"P11 has verified it; the conditional is theirs to discharge."*

Recorded as a method note rather than an error: no false claim was published, and `P07` reached the
same verdict. **But P11's phrasing in Delta 10 §1 — *"the conditional is discharged"* — over-stated
what one party's reading can do for another, and is corrected here.**
