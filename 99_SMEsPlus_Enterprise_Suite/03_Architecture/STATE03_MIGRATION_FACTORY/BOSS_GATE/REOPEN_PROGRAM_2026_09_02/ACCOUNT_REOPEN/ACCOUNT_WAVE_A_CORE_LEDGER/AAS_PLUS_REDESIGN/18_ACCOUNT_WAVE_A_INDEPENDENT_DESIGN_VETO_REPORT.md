# 18 — INDEPENDENT DESIGN VETO REPORT

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> Two fresh independent reviewers, **disjoint assignments, neither authored the package**, each briefed
> adversarially and each instructed: *"if any path in this brief is wrong, report it as a finding."*
> Both did. Their reports are recorded here **as returned**, then dispositioned.

---

## 1. Result

| | Reviewer A | Reviewer B | Total |
|---|---|---|---|
| Assignment | event ownership · canonical identity · immutability · correction/reversal · migration continuity · reconciliation | date semantics · period/lock/close/reopen · FX · tenant isolation · report consistency · **the registers themselves** | disjoint |
| Findings | **29** | **39** | **68** |
| `MATERIAL` | **17** | **29** | **46** |
| `MINOR` | 11 | 10 | 21 |
| Recorded `SOUND` | 1 | — | 1 |
| Clean-room leaks | **0** | **0** | **0** |
| Prohibited verdict wording | **0** | **0** | **0** |

### Both reviewers reached the same verdict, independently and in almost the same words

> **The design substance survives adversarial challenge. The labelling and the register discipline do
> not.**

Reviewer A: *"The design substance is not what fails. What fails is the status labelling and the
citation layer."*
Reviewer B: *"I could not disprove the substance of any of the six candidate models. What I can
disprove is the labelling and the register discipline around them."*

**Neither reviewer disproved a single design position.** Between them they disproved **the evidence
this package cited for them**, in 46 material places.

---

## 2. The three systemic defects

### `V-SYS-1` — the highest label did not mean what the package defined it to mean

Found independently by both (`RA-02`, `RB-27`). At least **nine** designs carried `STABLE-CANDIDATE`
while their own register cell named an open gating unknown. Reviewer B found the package had even
**stated the redefinition in terms**, at `02 §6`: *"they are labelled `STABLE-CANDIDATE` because the
positive evidence is strong — not because the negative is settled."*

And the bar could not have been tested regardless: **`T0-01`…`T0-06` appeared zero times in the entire
package** (`RB-29`), though at least three of the six demonstrably bear on package designs —
`T0-01` on `D-02`/`D-18`, `T0-03` on `D-02`/`D-20`/`DP-05`, `T0-04` on `D-33`/`D-34`/`L-9`/`T-19`.

**Disposition — `ACCEPTED IN FULL`.** `STABLE-CANDIDATE` is now **unused in this package**
(`AASR-C-01`, `00 §4`). All 20 designs demoted.

### `V-SYS-2` — the package consumed the parent's findings but not the parent's *corrections* to them

The deepest finding, and both reviewers reached it by different routes.

| Source never consumed | What it contained | Found by |
|---|---|---|
| `CORR1/C04` negative-claim scope register | **`NC-01`…`NC-24`** — the parent's own class assignments. **11 claims class `E — CONTRADICTED`** | `RA-25` |
| `MCC_G §8` second correction notice | **`G-C1`…`G-C8`** — *"the single richest source of contradictions I found"* | `RB` (6 of its findings) |

**This is the same defect this package diagnosed in itself at `18A §6` — one layer deeper than it
looked.** `18A` proposed `ER-AASR-1` (*design input comes from a source's adversarial section, never
its summary*) after finding six errors from `MCC_G §7`. The reviewers then found the package had
missed **`MCC_G §8`** — the correction notice *after* the section it had just learned to read — and an
entire governing register one round below.

**Disposition — `ACCEPTED IN FULL`.** Corrections applied in §4.

### `V-SYS-3` — the controlling register is not closed against its own source

`RB-31`, `RB-32`, `RB-33`, `RA-05`, `RA-12`. Live parent ids absent from the register that calls itself
*"the delta-revalidation worklist"*:

`T0-01`…`T0-06` · `GB-05` · `GB-06` · `MCU-60` · `MCU-61` · `CL-01`…`CL-04` · `TI-07` · `TI-08` ·
`SB-05`…`SB-08` · `BW-28a` · `D-28`

Reviewer B's sharpest point: **these are *backward* contradictions, not forward ones.**

> *"`DEP-00` is a forward dependency on files the parent has not yet published. Findings `RB-04`,
> `RB-08`, `RB-11`, `RB-17`, `RB-20`, `RB-24`, `RB-32`, `RB-33` are **backward** — contradictions with
> parent text that already exists, was already read into this session's evidence base, and was not
> carried. **Delta revalidation cannot fix those; it will diff against a baseline that already omits
> them.**"*

**Disposition — `ACCEPTED IN FULL`, and it is the finding that determines this session's terminal
state.** A register that omits twenty live parent ids cannot serve as the delta-revalidation worklist,
which is the one job `01` claims.

---

## 3. Material findings that change a design position

| id | Finding | Disposition |
|---|---|---|
| `RA-01` | **`XM-01` contradicted.** `NC-13`, class `E`: a duplicate control **does** exist — a duplicated-reference field over sale and purchase documents, across draft and posted, that **suppresses auto-posting and writes a thread message**. It does not block manual posting and was not found to extend to machine-generated entries | **ACCEPTED.** `03 §1` restated |
| `RA-09` | **`VF-02` is class `D — UNKNOWN`**, not `VERIFIED FACT`. `NC-14`: *"within the fourteen invariants this package enumerated, two were found unconditional. **The enumeration is the package's own and is not proven exhaustive.**"* And the parent's own `L3` says **one**, not two | **ACCEPTED.** The sole foundation of `D-02`, `EL-03`, `ADR-02` and all of `04 §2` |
| `RB-11` + `NC-19` | **`D-23` is `INVALIDATED`.** A post-and-reverse unrealised-FX revaluation mechanism **exists**; `G-C2` adds it is **user-overridable per currency with a warning**, making it a *detecting control* `BW-28` claimed did not exist. **`BW-28` withdrawn → `BW-28a`**: where the consolidating root holds no rate row for a subsidiary's functional currency, **that subsidiary's entire balance sheet and income statement translate at 1.0**, silently — now `T0-07`'s headline instance, and absent from the package | **ACCEPTED.** `10 §4` rewritten; `BW-28a` added to `14 §4` |
| `NC-22` | **`VF-06` withdrawn**, class `E`, four verified counterexamples — including that **the posting-time call IS lock-gated** | **ACCEPTED.** `02` restated |
| `NC-20`/`NC-21` | **`VF-05` restated.** Purpose-specific recognition-date carriers exist; a **derived** tax point exists for cash-basis taxes via the reconciliation's maximum matched date | **ACCEPTED** |
| `NC-05` | **Typed origin links exist** — payment, recurring-entry, cash-basis, statement-line, plus a free-text origin field. What is absent is a *general, mandatory* identity | **ACCEPTED.** `02 §6` restated |
| `RA-14` | **`D-03`/`FF-03` does not close `BW-35`.** The design constrains the *link* — unique, non-severable, bidirectional — but never requires it to be **validated against the content it claims to correct**. `BW-35` finding 1: *"nothing checks that the entry a reversal points at is the entry it actually reverses — not the amounts, not the signs, not the accounts, not the period."* A reversal pointing at the wrong original, on a perfect link, still balances | **ACCEPTED — a real design gap.** Rule added at `04 §5` |
| `RA-21` | **`RE-01` contradicts `D-18` inside one file.** `RE-01` said unreconciling *"removes settlement facts"*; `D-18` says settlement facts are never destroyed; `08 §1` classes the matching record as immutable `F4`. And since `07 §5` removes un-posting, **unreconcile was the surviving destruction path** | **ACCEPTED — a real design contradiction.** `RE-01` rewritten |
| `RB-02`/`RB-05` | **`CL-01` and `CL-04` are parent-registered Boss decisions** answered here at the highest label. `CL-01`: *is a closed period a record with a closer, a timestamp and a basis, or a date?* `CL-04`: *does a late document post to its own period or the current one?* `CL-01`…`CL-04` appeared **zero times** in the package | **ACCEPTED.** `D-06`, `DP-07` → `UNKNOWN — Boss`; added to `15 §3` |
| `RB-20` | **`VF-15` reverted to class `B`.** `MCU-60`/`MCU-61` were reverted from out-of-scope to `UNKNOWN`, class `B` — *"a not-found presented as a positive establishment"*, and `MCU-60`'s basis is **circular**. `MCU-61` is deployment- and hosting-layer tenancy. Both are among the 17 gating unknowns; both appeared **zero times** in the package | **ACCEPTED.** `D-33`'s foundation moved onto its positive evidence, which is unaffected |
| `RB-33` | **`MCU-02`/`MCU-03` is a Boss decision, not a research item**: *"cannot be closed by any amount of further research. It is `GB-01`-class."* `D-01`'s revalidation instruction said *"re-run the search"* | **ACCEPTED.** Moved to `15 §3` |
| `RB-19` | **`TI-07` omitted** — the parent's *"single highest-value structural requirement"*: every measurement, classification and control value carries exactly **one** owning boundary, **and every writer and every reader applies the same scoping rule**. `TI-08`: no boundary enforced solely in the application layer where a database constraint can express it. `GB-01`'s Boss question is *"a decision on the SMEsPlus boundary model (`TI-07`)"* | **ACCEPTED.** Added as `CR-09`/`CR-10` |
| `RB-17` | **`T0-09` wording**: the package had **strengthened** an already-corrected claim from *"can never execute"* to *"proven inert"*. `G-C7`: present in the view layer, absent at write; population floor **30 across 4 files** | **ACCEPTED** (already applied at `EFC-02`, re-verified) |
| `RB-10` | **"14 sites / 12 expressions, 100% coverage" is a denominator *defect* reported as a statistic.** `MCC_B` `B-3`: two disciplined enumerations returned 12 and 14 because **the unit was never defined** — *"a bounded population with an undefined unit is not yet a denominator."* Only **20 of 20 files** survives as coverage | **ACCEPTED** |
| `RB-12` | The class-`A` negative retiring the `FX-08` hold cites **1,752 module directories** — the **pre-correction** figure. `MCC_E` `E-C3`: *"the directory figure and the module figure are different populations and this file conflated them"*; the corrected form is 791 directories + 962 modules, and **3 stray modules were missed entirely** | **ACCEPTED.** Boundary restated |
| `RB-16` | **192/9 does not reconcile.** If elevation is 0 of 93 and raw-SQL 0 of 62, the 9 must all be root-vs-company — but the source records **4 of 37**. `0+0+4 = 4 ≠ 9`. Two different rounds' metrics were merged | **ACCEPTED.** Restated per-population: `3 of 93 · 4 of 37 · 2 of 62 = 9 of 192` |
| `RB-28` | **`01 §3`'s arithmetic does not reproduce**: claimed 21/11/2/1, actual **24/9/1/1**. And **`D-28` has no row** in the controlling register | **ACCEPTED** |
| `RB-23` | `14 §3` counts `T-03` as fully answered while `14 §2` marks it *mixed*; `T-08` rests on a blocked class-`B` negative. Correct: **6 fully answered, 1 partial** | **ACCEPTED** |
| `RB-09` | **FX namespace collision.** Package rules `FX-01`…`FX-08c` collide with parent risk/blocker ids `FX-01`…`FX-08` **with inverted meanings** — `FX-01` is *"the highest risk in Wave A"* upstream and a design rule downstream. The package flagged the milder `BW-16` collision as `MCD-01` and missed its own worst one | **ACCEPTED.** Renamed `FXD-01`…`FXD-07` |
| `RB-32` | **`MCU-20`/`21`/`22` id collision**, undeclared: the ids denote five *Boss decisions on close, period and tenancy* in the convergence round and three *new gating findings* in the closure round. **Five parent-registered Boss decisions were lost through it** | **ACCEPTED.** Raised as `MCD-02` |
| `RA-16`/`RA-17` | *"Five of seven lineages unrecorded"* is **four of seven** — an arithmetic error in the parent's own checkpoint line, propagated here and contradicted by the table directly below it. And *"the reference implements none of this"* is contradicted by that same table, which marks **three** recorded | **ACCEPTED** |
| `RB-07`/`RA-06` | `NCS-06` was graded **SOUND** by the package's own scan on the boundary *"the tree"* — **precisely the boundary the parent proved short by 962 modules**, and in violation of `18A §4`'s own standing clause | **ACCEPTED.** Re-graded `UPGRADE`; `VF-10` restated class `B` per `NC-04` |
| `RB-34` | **`18A §3` claimed corrections applied that were not in the files.** The file reporting the negative-claim control carried an unearned completion statement — *"the precise defect class it exists to catch"* | **ACCEPTED.** §3 re-titled and re-verified |
| `RA-26` | `17 §1` and `18A §3` stated independent review had returned **before it had**. Prospective claims written as completed | **ACCEPTED** |
| `RA-27`/`RB-37`/`RB-39` | Bare numeric cross-references collide with the package's own file numbering (`04` cites *"`15 §4`"* meaning the **parent's** identity register). The package registered exactly this defect against its input as `MCD-01` and reproduced it against itself | **ACCEPTED.** Parent citations prefixed `P-` |

---

## 4. Findings NOT accepted

| id | Finding | Why not |
|---|---|---|
| `RB-21` | *"The four boundary failures"* is a completeness claim against an `SB-01`…`SB-08` register | **PARTIALLY ACCEPTED.** The reviewer states the substance of `SB-05`/`SB-06` is carried under successor ids and *"nothing is lost"*. The enumeration wording is corrected; no design changes |
| `RB-03` | Tax-point row labelled `EVIDENCE-DEPENDENT` without naming a parent finding | **ACCEPTED AS MINOR**, but the row now names `NC-21` (`E — CONTRADICTED` in part), which did not exist in the package when the finding was raised |
| — | No finding in either report was **rejected**. | Every one was accepted in full, in part, or as minor |

---

## 5. The veto

> ### `AASR-VETO-01` — `01` is NOT a usable delta-revalidation worklist in its current state.
>
> Raised by Reviewer B, seconded by Reviewer A's `RA-05`/`RA-12`, and **upheld**.
>
> `01` claims one job: *"when the parent terminates, this register is the delta-revalidation
> worklist."* It cannot perform that job while it omits `T0-01`…`T0-06`, `GB-05`, `GB-06`, `MCU-60`,
> `MCU-61`, `CL-01`…`CL-04`, `TI-07`, `TI-08`, `BW-28a` and `D-28` — because **delta revalidation
> diffs against the consumed baseline, and a baseline that omits them will never surface them.**
>
> **This veto is not lifted by the parent finishing.** It is lifted only by closing the register
> against the parent evidence **that already exists**.

**Consequence for the terminal state.** This session does not claim its register is ready. `19`
records the veto as an open condition, and the register-closure work as the first item of any
continuation — ahead of, and independent of, delta revalidation.

---

## 6. What survived

Stated plainly, because 68 findings could otherwise read as a failed package.

**Not one design position was disproved.** Both reviewers, on disjoint assignments, tried and could
not. What survived adversarial challenge on verified positive evidence:

- separating the accounting event from the journal entry;
- unconditional immutability enforced below the application;
- additive correction with a constrained relation — **now extended to require content validation**;
- permanent classification identity with succession rather than rewrite;
- provenance travelling with the fact;
- a hard-bounded, undestroyable settlement fact;
- removal of the accounting-date derivation rule;
- the period as an object with state;
- no measurement fallback of any kind;
- the refusal to make any tenant-isolation claim.

Reviewer A recorded one area explicitly `SOUND` (`RA-20`: `D-35`/`MCU-19` and `D-14`/`T0-08`, verified
line by line). Reviewer B independently reproduced and could not break: `192 = 93+37+62`, `9 = 3+4+2`,
the gating trajectory `17→11→18→17`, **19** taxonomy classes, **20 of 20** rate files, **962** modules
and **904 of 906** localisations, **9 of 22** models and **36 of 139** fields.

Both independently confirmed **zero clean-room leaks and zero prohibited verdict wording**.

---

## 7. The method result

Five consecutive parent rounds produced the same pattern: **every material correction came from an
independent reviewer, none from the author.** This session set out to break that pattern by running
the scan as a separately-tasked step, and **caught 11 of its own defects before review returned**
(`NCS-01`…`NCS-07`, `EFC-01`…`EFC-06`).

**The reviewers then returned 68 more, 46 material.**

> **Self-review moved the ratio from 0-in-N to 11-in-79. It did not come close to replacing
> independent review.** The two reviewers were given **disjoint** assignments and returned
> **near-identical systemic verdicts by different routes** — which is the strongest available evidence
> that both were reading the package and not each other.
>
> **`ER-AASR-1` — take design input from a source's adversarial section, not its summary — was
> authored by this session after finding six such errors, and was then itself found insufficient:
> the reviewers located a *second* correction notice (`MCC_G §8`) below the one it had learned to
> read, and a governing register (`CORR1/C04`) an entire round below that.**
>
> The rule is correct and was under-applied by its own author within the same session. That is the
> independence clause — `MCC_K`'s fifth, the one never implemented — demonstrated at close range.
