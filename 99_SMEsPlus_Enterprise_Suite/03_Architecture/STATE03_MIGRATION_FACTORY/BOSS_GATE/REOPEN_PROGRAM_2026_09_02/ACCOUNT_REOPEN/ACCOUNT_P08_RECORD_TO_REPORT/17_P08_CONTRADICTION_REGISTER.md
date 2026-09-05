# P08_CONTRADICTION_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Every material contradiction records the competing claims, the evidence for each, the scope of each evidence source, the contradiction type, the disposition and the downstream impact. Contradictions are preserved, never averaged away and never resolved by reviewer count.

## 1. Contradictions between the benchmark's own layers

| ID | Competing claims | Type | Disposition | Downstream |
|---|---|---|---|---|
| `P08-CONTRA-01` | The settlement guard's **message** asserts that both sides must belong to the same company; its **code** tests the root of the company tree | implementation-specific | **Code wins.** Two different companies in one tree may be settled together | `P08-T0-04`; `P08-RQ-REC-03` |
| `P08-CONTRA-02` | The account-number interface presents one row **per company**; the store is keyed **per tree root** | implementation-specific | **Store wins.** Editing one company's row changes every company under that root | `P08-BD-01`; `P08-RQ-COA-06` |
| `P08-CONTRA-03` | Account-number **uniqueness** is checked in both directions of the company tree; account **visibility** runs downward only | semantic | Both stand; they are inconsistent by construction. A refusal can name an object the requester cannot see | `P08-RQ-AID-03` |
| `P08-CONTRA-04` | **Posting-side** rate resolution admits company-less rates; **reporting-side** resolution excludes them by strict equality | implementation-specific | Both stand. The same fact converts two ways depending on the consumer | `P08-BD-08` |
| `P08-CONTRA-05` | The **entry-numbering** subsystem derives the fiscal year from the company parameter pair; the **reporting** subsystem consults the year-record table first | implementation-specific | Both stand. An irregular year record makes them disagree | `P08-RQ-PC-08`; occurrence is `D UNKNOWN` |
| `P08-CONTRA-06` | Two rate-type shortcut paths emit **different value sets** for the same mode, and neither matches the set the consuming join requests | implementation-specific | Unresolved in the benchmark | `P08-U-FX-01` (`D UNKNOWN` whether it produces a wrong figure or an unused row) |
| `P08-CONTRA-07` | A book of account is an instrument of **one legal entity**; the benchmark scopes it to the company **tree**, so a parent's book is selectable by every descendant's entries | semantic vs implementation | The business semantic governs SMEsPlus; the benchmark behaviour is recorded as evidence, not adopted | `SC-JE-01`; `P08-RQ-JPM-*` |
| `P08-CONTRA-08` | A tamper-seal chain asserts a property of **one company's** records; the benchmark chains on a per-book series and a book is tree-scoped, so a chain may span companies | semantic vs implementation | Business semantic governs | `SC-JE-08` |
| `P08-CONTRA-09` | A fiscal year is a legal attribute of a **legal entity**; the benchmark delegates it to the **root** of the company tree | semantic vs implementation | Business semantic governs. Whether one tenant may hold companies with differing year-ends is `P08-SC-U-01` | `SC-CL-01` |

| `P08-CONTRA-16` | The same period cut-off **hard-refuses** an asset re-evaluation with an explicit error, and **silently relocates** an entry posted through the ordinary posting routine — including when the cut-off violated is the irrevocable one | implementation-specific | **Both stand.** One control, two opposite behaviours in one module. The cause is structural: a period has no state, so each code path chooses how to honour the date | `P08-PEER-02`; `P08-RQ-PC-02` |

## 2. Contradictions between this session and prior programme evidence

| ID | Prior claim | P08 finding | Disposition |
|---|---|---|---|
| `P08-CONTRA-10` | Prior rounds recorded "no accounting-event object exists" bounded to **one** root, and the programme's own closure round re-scoped every such class-A absence to ≤1 of 22 roots | P08 re-ran the claim across **all 22 declared roots** and found it holds in 22 of 22 | **Prior claim upheld and its scope widened.** Not a contradiction of substance; a contradiction of *scope*, resolved in the prior claim's favour |
| `P08-CONTRA-11` | Prior rounds recorded the balance invariant as suppressible and reported the dispatch layer as unfiltered, with exploitability classed as inference | P08 independently reproduced both, and adds that the same dispatch mechanism reaches the posted-record guard and the seal's version selector | **Prior claim upheld and widened.** Exploitability remains `SUPPORTED INTERPRETATION` — P08 executed nothing |
| `P08-CONTRA-12` | A prior round claimed "no fiscal-year model exists"; a later round contradicted it | P08 confirms the year entity exists, and confirms the surviving load-bearing claim — that no closing, locking or state attaches to it | **Contradiction already resolved by the prior programme; P08 does not re-open it, and does not re-import the withdrawn wording** |
| `P08-CONTRA-13` | A prior round claimed "no rate-type dimension exists"; a later round contradicted it | P08 confirms the dimension exists, is derived at query time, is assigned by account classification rather than by transaction, and attaches to no posted fact | **Prior contradiction upheld; P08 adds the reason the dimension is nonetheless unusable for a posted fact** |

## 2A. Contradictions between two governing instruments, raised not resolved

| ID | Statement |
|---|---|
| `P08-CONTRA-17` | **Two governing instruments define the negative-claim class letters differently.** The ratified standard defines `B` = *not found in searched scope*, `D` = *unknown*, `E` = *contradicted*. A later closure-round compliance artefact defines `B` = *searched, not answerable from source*, `D` = *residual of a closed search*, `E` = *no evidence found, reported as absence — prohibited as a conclusion*. The letters `A` and `C` agree; `B`, `D` and `E` do not. **P08 uses the ratified standard's table and says so in `00` §2.** Which table governs is a `BOSS CONTROLLED DECISION` — `P08-BD-15` — and until it is settled, any cross-round comparison of class letters is unsafe. |
| `P08-CONTRA-18` | **The class-`A` prohibition's closing condition is stated two ways in the same parent package.** One line makes it "until the root set is declared", which this session satisfies; the gating register and the gate report make it "which reference core root does SMEsPlus target", which this session cannot satisfy because it is a programme declaration. P08 records both readings and takes neither silently. See `01A` §1. |

## 3. Contradiction between a Boss instrument and a session assumption

| ID | Statement |
|---|---|
| `P08-CONTRA-14` | The GB-08 ruling, read literally, requires tenant **and** company context for FX rate resolution. The mid-session scope correction withdraws any blanket "tenant + company for every operation" reading. **Disposition:** these are not in conflict once the object is split — the *application of a rate to a posting* is company scope and the ruling applies in full; the *rate observation* is platform scope and the ruling's isolation invariants do not apply to it. Recorded in `00A` §3 and `01` §2.3. No Boss instrument is weakened by this session. |

## 4. Governance boundary raised, not resolved

| ID | Statement |
|---|---|
| `P08-CONTRA-15` | The GB-08 ruling states Wave B must not start before Wave A receives its Boss Final Research Gate decision. P08 was commissioned by Boss prompt in the same period and overlaps Wave A's subject matter. **P08 does not adjudicate this.** It executes as research only, produces no implementation authority, does not close Wave A, and records the sequencing question as `BOSS CONTROLLED DECISION` `P08-BD-10`. |

---

# CLOSURE DELTA — `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001`

Added because an independent reviewer established that **none** of the closure's identifiers had reached any register. That was an `EC-08` failure and it is corrected here rather than argued with.

| ID | Contradiction | Disposition |
|---|---|---|
| `P08-CONTRA-19` | The configuration-data claim was true of production data and false of demonstration data, which declares entries in a majority of roots | **REFINED, not withdrawn.** And see `P08-CONTRA-32`: the published control for it did not test the thing denied |
| `P08-CONTRA-20` | The custom-module denominator was the work-queue length, not the ledger-touching population | **CORRECTED** to the measured population. **Still contested** — a reviewer could not reproduce it either; see `P08-CONTRA-33` |
| `P08-CONTRA-21` | Six peer packages record P08 as unpublished; the branch is present with an earlier tip | **UNRESOLVED.** Push time is not recoverable from the clone. Both readings leave the same actionable consequence — `46` §1A |
| `P08-CONTRA-22` | **Files 38 and 41 contradicted each other on the same table in the same session.** The orphan headline omitted the two origin pointers populated at scale | **RESOLVED AGAINST FILE 38.** 9,754, not 83,820 — `47` §1. Found independently by **two** reviewers |
| `P08-CONTRA-23` | "The 53 imbalances are the population the missing assertion would have caught" | **WITHDRAWN.** 49 carry the counter-leg already exculpated; the residual is 4 — `47` §2 |
| `P08-CONTRA-24` | The backdating population read as human behaviour; 98.3% is one machine-generated catch-up | **RESTATED** as 112 plus a migration — `47` §3 |
| `P08-CONTRA-25` | "The retention column does not exist in any of the 3 databases" | **FALSE for 2 of 3; WITHDRAWN and ESCALATED.** Present in both 19.0 databases, unset on 88 of 88 — `47` §4 |
| `P08-CONTRA-26` | The seal denominator was 64 journals | **CORRECTED to 109** — `47` §5 |
| `P08-CONTRA-27` | "0 of 447,384 items disagree with their entry" was true of the six mirrors tested; the seventh disagrees on 174,977 | **RESTATED** — `47` §6 |
| `P08-CONTRA-28` | File 41 §2 (item mirrors add no information) contradicts file 41 §8 (carry provenance on the item) | **ACCEPTED as a real internal contradiction.** The resolution is a design position and belongs to P11 |
| `P08-CONTRA-29` | "Any rate that is not 7% is silently outside the statutory register" reads as suppressed VAT; 4 of the 5 excluded groups are withholding groups | **MISCHARACTERISED, corrected.** All statutory readings remain `HOLD` |
| `P08-CONTRA-30` | The gapless-counter finding fused a design fact in one product line with a configuration fact in another | **SEPARATED.** The measurement stands |
| `P08-CONTRA-31` | Relocation was bounded by the absence of a period lock; it is **not** a lock behaviour | **CORRECTED.** Default behaviour for every non-sale document; measured at 20.95% of purchase entries in a lock-free database — `46` §6 |
| `P08-CONTRA-32` | **A counterexample published as "read directly" does not hold.** The uniqueness constraint sits on the system's own generated reference, not on the external provider reference | **CONFIRMED AGAINST THE AUTHOR.** The retraction it supported still stands on independently verified evidence; the counterexample is struck — `48` |
| `P08-CONTRA-33` | **A withdrawn class-A claim is still carried at class A in two places, one of them governing an entire register — while the negative-claim register certifies that no such restatement exists** | **CONFIRMED AGAINST THE AUTHOR.** The prohibition the programme names as its own was breached — `48` |
| `P08-CONTRA-34` | **"N of 21 roots" is at most 7 independent observations.** The core posting file resolves to 7 distinct contents across the roots that carry it | **CONFIRMED AGAINST THE AUTHOR** by content hash — `48` |
| `P08-CONTRA-35` | "In a real population the duplicate detector is swamped" is not supported by the author's own data when scoped to the population the detector covers | **CONFIRMED AGAINST THE AUTHOR.** 677 of 36,961, largest group 14 — `48` |
