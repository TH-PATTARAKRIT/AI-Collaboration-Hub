# P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G04)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Continues:** `14_P06_REVISION_LOG.md` (REV-E-01…04) · `39_P06_RESEARCH_ERROR_AND_REVISION_LOG.md` (…REV-E-11) · `62_P06_TARGETED_CLOSURE_AUTHOR_ERROR_REVISION.md` (…REV-E-16). **Same numbering. None of those files is superseded.**

> **Prompt §11 forbids silently overwriting contradictions or prior errors.** Nothing here is overwritten. Every superseded wording is quoted verbatim before its correction, and — the point of this file — **every correction is edited into the register that carries the error**, not only recorded here.
>
> **`62_` recorded 16 author errors and its disposition table said the registers were corrected. Auditing that claim this round found one register that was not.** See `REV-E-20`.

---

## 1. `REV-E-17` — a loop reported `0 of 109` when the answer was `12`

**What was executed, and what it returned:**
```
FILES NAMING P06: 0 of 109
```
**Why that was false:** `P10_TO_P06_HANDOFF.md` is a file in that tree whose entire purpose is to name P06. A count of zero was refuted by a document already open in the session.

**Caught by:** noticing the contradiction with a known file. **Not by the loop, and not by any control** — there was no control.

**Re-run with an explicit positive control** (assert the pattern matches a file known to contain it before trusting any zero): **`12 of 109`.** All 12 were then read.

**Root cause:** the loop's file-path construction failed silently for every iteration, and a per-iteration failure is indistinguishable from a per-iteration non-match when only the aggregate is printed.

**Classification:** the `coverage-assertion` defect class — *a loop that silently processes fewer artefacts than it claims*. **Third occurrence in this programme.** The standing rule is already written: **a zero is not a result until the instrument has been shown to be capable of returning non-zero on this exact population.** The rule existed; it was not applied.

**Consequence for this round:** none of the substantive findings depend on the wrong count — the corrected 12 were read in full before any conclusion was drawn. **But had the `0` been believed, this entire round would have terminated with "P10 says nothing about P06", and all four `H06` items would have been missed.**

**Correction applied in place:** the corrected denominator, and this defect, are stated inside `P06_P10_MATERIAL_DELTA_REGISTER.md` §1 — in the register, at the point of use, not only here.

---

## 2. `REV-E-18` — seven files claim a peer dependency is closed that the peer still carries OPEN

**Superseded wording, quoted verbatim:**

| File | Wording |
|---|---|
| `35_`:121 | *"**Either way P10 may close `X-08` as answered**…"* |
| `35_`:145 | `\| **P10** \| **X-08 answered** (§6) \| — \| **closed by P06** \|` |
| `36_`:29 `D-11` | *"**ANSWERED — P10 may close it.** Resolves by absence…"* |
| `34_`:40 `F-12` | *"**UNOWNED — and P06 now answers P10**"* |
| `34_`:99 | *"P10 asked P06 and P06 answers that the object does not exist for either."* |
| `18_`:198 | *"P10 `X-08` — bank-side prepayments and interest accruals: **answered and closable.**"* |
| `39_`:96 | `\| **P10** \| X-08 is answered and may be closed. \|` |
| `57_`:31 | *"no peer claims it; P10 asked P06 and **P06 answered by absence** (`X-08`)."* |
| `70_`:71 | *"**P10 `X-08` — answered and closable.**"* |

**What the peer's own latest register says**, read at `1fea562` (`BR-05`):
```
53_P10_PEER_DEPENDENCY_REGISTER_V2.md:30  PD-08 | P06 | ... | OPEN — PEER EVIDENCE | no | —
19_P10_DEPENDENCY_REGISTER.md:19,59       D-08  | P06 | ... | PEER DEPENDENCY OPEN ... "PEER DEPENDENCY OPEN — unchanged"
10_P10_CROSS_PROCESS_OWNERSHIP.md:36      X-08  | P06 | ... | PEER DEPENDENCY OPEN
```

**What is and is not contradicted, stated precisely:**

- **NOT contradicted — the substance.** P06's answer is untouched: *there is no bank-interest object in the searched scope for either process; P06 recommends the boundary at accrual (P10) versus receipt (P06)*. Re-affirmed.
- **CONTRADICTED — the status.** `35_`:145 and `39_`:96 assert closure. **A dependency owned by a peer is not closed by the answering party.** P06 can answer; only P10 can close. Two rounds and a later commit have passed and P10's register says *"unchanged"*.

**Root cause — and it is not a research failure.** P06 conflated *supplying the answer* with *discharging the dependency*, and then recorded the discharge in its own status columns. **This is the `unresolved-peer-decision-is-not-a-boundary` shape run in reverse:** rather than adopting a peer's open item as settled, P06 declared its own contribution settled on the peer's behalf.

**Corrections applied in place** — all nine statements, in the seven register files, this round. The substantive answer is retained; the status claim is replaced with *"ANSWERED BY P06 — CLOSURE IS P10'S. Still `OPEN — PEER EVIDENCE` at `1fea562`."*

---

## 3. `REV-E-19` — a third reference tree existed and was undeclared

**Found:** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417` — a **later v19 Enterprise build** than the `19.0+e.20260312` tree this package adopted in round 4 as its v19 basis.

**How:** a `find /Volumes/iMacSys -maxdepth 5 -type d -name "odoo-19.0+e*"` run to re-establish source paths after the session resumed. **Not a new sweep, and not an intentional search for it.**

**Why it matters, and why it matters less than it looks:**
- `P06-B-55` states the evidence base is a filtered distribution and every tree-scope negative inherits that boundary. **That blocker was correct and this is a third confirmation of it.**
- **`REV-E-10` was the first occurrence** of this exact defect: round 3 declared a v19 search unnecessary and a complete v19 tree existed. **This is the second occurrence, after the lesson was written down.**
- **All six expressions at issue this round were re-executed against it and are identical** (`P06_P10_MATERIAL_DELTA_REGISTER.md` §4). No finding changes.

**Bounded, deliberately.** The new tree was used for **exactly the six expressions already under test** and nothing else. Re-basing the package's v18-only analyses (FK resolution, sequence, numbering) onto a third build would be **widening**, and is prohibited. Recorded as **`P06-OQ-123`** — *the v18-only analyses have never been tested against any v19 build, and now there are two.*

**Correction applied in place:** `51_` and the source-link register carry the new tree as a declared, non-adopted third basis — see `P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` §4.

---

## 4. `REV-E-20` — the package still asserts P08 is unpublished, three rounds after consuming it

**This is the most serious of the four, because it is a correction the package believed it had already made.**

**Superseded wording, quoted verbatim — four statements in four files:**

| File | Wording |
|---|---|
| `11_`:148 `T-10` | *"…flagged to P11 as a routing defect; **no P08 branch exists to answer**."* |
| `35_`:22 | `\| P08 GL / Record-to-Report \| **NOT PUBLISHED** \| **PEER DEPENDENCY OPEN** \|` |
| `36_`:33 `D-15` | *"**SUPPLIED, UNCLAIMED** — **no P08 exists to receive it**"* |
| `36_`:61 `DEP-F-03` | *"**Since no P08 branch exists**, P10's dependencies are addressed to a process that does not own them and cannot answer."* |
| `39_`:98 | *"**Since no P08 exists**, P10's dependencies are addressed to a process that cannot answer."* |

**What was already established, in round 3, by this package** — `53_P06_P08_INTAKE_AND_DEPENDENCY_REFRESH.md`:
```
:15  | P08 Record-to-Report | NOT PUBLISHED | research/account-p08-record-to-report-2026-09-04-001 — PUBLISHED, 39 files |
:27  P08 independently found om_data_remove — E02_COA_AND_IDENTITY.md:125
:30  16_P08_ORPHAN_DUPLICATE_POSTING_ATTACK.md:107, AT-21 "Erase the ledger from a settings screen"
:45  27_P08_TOLERANCE_ZERO_REGISTER.md — P08-T0-08
```
**P06 read P08's branch, quoted three of its files by line, answered a question P08 left open, and adopted one of P08's tolerance-zero boundaries.** And five statements in four other files still say P08 does not exist.

**How it was found:** not by looking for it. `MD-P06-09` required checking whether any P06 claim depended on a P10 statement about P08. The check — `grep -n "P10.*P08\|P08.*P10" *.md` — was clean on its own question and returned these five lines as a side effect.

**Root cause:** `53_` was written as a **new file** rather than as a set of edits to the registers the new evidence falsified. The new fact was published; the old ones were left standing. **`62_`'s disposition table records the round-3 corrections as applied. For this one, it does not — the error is not in `62_` at all.**

**Classification: the `revision-log-is-not-a-correction` defect, found inside the package that has been recording that defect in other packages since round 2.** A correction is not applied until the text that carries the error is edited.

**Corrections applied in place** — all five statements, this round. The routing finding `DEP-F-03` **survives**: P10 routing its close/FX dependencies to P04 while P11 and P02 route them to P08 is still a real divergence. **What changes is its consequence** — it is no longer *"addressed to a process that cannot answer"*; it is *"addressed to a process that exists, is published, and was not asked."* **That is a materially worse finding, not a milder one.**

---

## 5. `REV-E-21` — the corrections were not applied to the registers, and the population says when

**`REV-E-20` was found incidentally. That made its population an open question, so the population was executed.**

**DENOMINATOR.** POPULATION: the eight author errors recorded in `62_P06_TARGETED_CLOSURE_AUTHOR_ERROR_REVISION.md` (`REV-E-09` … `REV-E-16`) — the round-4 correction file whose consolidated table reports them as dispositioned. UNIT: **a correction, audited against the register text it was supposed to change.** PATTERN: for each, grep the package for the superseded wording and check whether the target register carries a correction marker. **RESULT: 8 audited, 6 failed.**

| `62_` correction | Target register(s) still carrying the superseded wording | Verdict |
|---|---|---|
| `REV-E-09` — *"a `TransientModel` with a broad default ACL"* | `20_`:239 — **zero correction markers in the whole file** | **NOT APPLIED** |
| `REV-E-10` — *"no v19 source tree"* / generation gap | `46_`:74 `B-44`, `18_`:185 `B-9` | **NOT APPLIED** |
| `REV-E-11` — three `is_matched` branches | `01_`:122, `18_`:16, `25_`:40, `46_`:47 — **four statements** | **NOT APPLIED** |
| `REV-E-12` — *"an eighth settlement door"* | `18_`:181 `B-6` *(`40_`, `46_`, `55_` were corrected)* | **NOT APPLIED** |
| `REV-E-13` — copy count 4 → 17 | none — *"present in all four custom roots"* remains **true as written**; the correction was an enlargement to a different population, recorded in `58_`:87 | **NOT A FAILURE** |
| `REV-E-14` — sequence rewind attributed to `ir.sequence` | `20_`:234 `CMD-F-17` | **NOT APPLIED** |
| `REV-E-15` — bytecode misread | none found; `11_` `T-14` and `70_`:100 both carry the withdrawal | **APPLIED** |
| `REV-E-16` — *"filtered distribution"* is a relocation | `12_`:150, `18_`:183, `38_`:63, `42_`:25 — **four statements** | **NOT APPLIED** |

**Six of eight. Thirteen individual statements.** And `62_`'s consolidated table reports all eight as dispositioned.

### The denominator was then widened, because AAS-03 said it was half the population

**`E4-G-04` challenged this finding on its denominator: `14_` and `39_` record `REV-E-01` … `REV-E-08` and were not audited. They were then audited, on the same pattern.**

| Correction | Target register | Verdict |
|---|---|---|
| `REV-E-01` door denominator 6 → 7 | `02_`:69 carries the correction inside the file | **APPLIED** |
| `REV-E-02` unverified `tenant` count | `19_` carries it at `R-08` | **APPLIED** |
| `REV-E-03` four unbounded negatives | `01_`:183 `PSM-F-19` and `:199` `PSM-F-22` both now carry a declared scope | **APPLIED** |
| `REV-E-04` ambiguous source tree | `11_` carries it at `T-03` | **APPLIED** (flagged by design, not silently retained) |
| `REV-E-05` unit conflation | `21_` §3 carries the corrected baseline | **APPLIED** |
| `REV-E-06` blocker arithmetic | `40_` §3 carries a unit declaration above the table | **APPLIED** |
| `REV-E-07` deferred grep | not a text correction — the work was executed | **N/A** |
| `REV-E-08` stale counts | propagated to `40_`, `18_`, `13_` at the time | **APPLIED** |

**RESULT: 7 of 7 auditable corrections from rounds 1–2 were applied in place. 2 of 8 from round 4 were. Full population 15 auditable corrections; 6 failures, and all six are in one round.**

**`E4-G-04` was right to challenge and the challenge changed the finding.** *"The defect is systematic"* is **withdrawn** as stated. **The accurate finding is narrower and more useful: the correction discipline held through rounds 1–2 and collapsed in round 4** — the round that produced the most corrections and the most new files in the shortest time. **The failure mode is volume, not culture**, and it is therefore predictable and preventable rather than diffuse.

**`20_P06_CUSTOM_MODULE_DELTA.md` is the worst case and it is worth naming separately:** it is the origin file for `P06-B-50`, the package's top CRITICAL blocker, it carried **two** superseded claims — a false ACL premise and a wrong causal attribution for the sequence rewind — and it contained **not one correction marker of any kind** before this round.

**And `18_P06_CORE_RECON_HANDOFF_PACK.md` is the most consequential:** it is the artefact **built to be consumed by P11**, and it carried **five** superseded statements (`B-6`, `B-8`, `B-9`, and the `is_matched` and `X-08` claims). A downstream consumer reading the handoff pack would have taken all five as current.

**A third status class was found while applying these:** `35_`:139 and `46_`:95 assert **P01 is unpublished**. Executed — `git ls-remote --heads origin` — **`research/account-p01-procure-to-pay-2026-09-04-001` exists at `b820b29`. P01 is published, and P06 has not consumed it.** Corrected in place. **Consuming P01 is a new peer intake and is outside this round's bound — recorded as `P06-OQ-124`, routed, not executed.**

**Root cause, stated once.** Every round of this package published its corrections as a **new numbered file** and left the falsified registers untouched. The disposition tables in `39_` and `62_` then recorded those corrections as complete — which is true of the *correction record* and false of the *package*. **The control that would have caught this is trivial and was never run: grep the package for the superseded wording after writing the correction.** It was run this round only because `REV-E-20` surfaced by accident.

**Corrections applied in place this round: 30 edits across 15 register files** — 9 for `REV-E-18`, 8 for `REV-E-20`, 13 for `REV-E-21`. Each edit **quotes the superseded wording verbatim** and carries a dated marker. **Nothing was overwritten silently**, per prompt §11.

**Consequence for terminality:** this is exactly the condition prompt §12 terminal state **C** describes. Whether it is discharged by having performed the corrections inside the same round — or whether a package that corrected 30 statements about itself in one unreviewed pass can assert its own integrity — is put to AAS-03 and PMO rather than settled here.

---

## 6. Contradictions arising this round

Appended to the families in `11_P06_CONTRADICTION_REGISTER.md` (Type I internal / Type II peer / Type III cross-version). **Register totals are enumerated, not asserted** — see `P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` §5.

| ID | Type | Contradiction | Disposition |
|---|---|---|---|
| `T-11` | **II — peer** | P06 states `X-08` is closed; P10's three registers state `OPEN — PEER EVIDENCE` at `1fea562` | **RESOLVED IN PLACE** — `REV-E-18`. Substance retained, status corrected in nine statements |
| `T-12` | **I — internal** | P06 states P08 is unpublished (4 files, 5 statements) and simultaneously quotes P08's published package by line (`53_`) | **RESOLVED IN PLACE** — `REV-E-20`. The five statements corrected; `DEP-F-03`'s consequence strengthened |
| `T-13` | **I — internal** | `39_`'s tail computes an eight-error attribution table (*"Six of eight were caught by…"*) that was never re-based when the count reached 16, and is now 20 | **RESOLVED IN PLACE** — the table is scoped in its own text to the errors it enumerates; a scope line is added so it is not read as a claim about the package total. **The attribution *ratio* is not restated, because restating it would require re-attributing 12 further errors and that is a separate unit** |
| `T-14` | **III — cross-version** | None arising. All four new findings are invariant across v18 `20250608`, v19 `20260312` and v19 `20260417` | **NO CONTRADICTION** — recorded so the absence is denominator-bounded rather than unstated |

---

## 7. Author-error tally, executed

```
grep -oh 'REV-E-[0-9]\+' *.md G02_CLOSURE_2026_09_06/*.md | sort -u | wc -l
```
**POPULATION:** distinct `REV-E-*` identifiers across the whole package including this round's directory. **UNIT:** author error. **RESULT recorded at publication** in `P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` §5, **after** the last file of this round is written — because a count taken before the last file is a count of a package that no longer exists. *That sequencing is itself a correction of `REV-E-08`, in which counts went stale between execution and close.*

**Detection attribution for this round's five:**

| Caught by | Count | Which |
|---|---|---|
| Contradiction with a known artefact | 1 | `REV-E-17` |
| Reading a peer's status field rather than a summary | 1 | `REV-E-18` |
| Incidental — a path-setup command | 1 | `REV-E-19` |
| Incidental — a check run for an unrelated question | 1 | `REV-E-20` |
| **Executing the population of an incidental finding** | **1** | **`REV-E-21` — the only one found deliberately, and only because `REV-E-20` forced the question** |
| **Author, by re-reading their own work** | **0** | — |

**Zero of five were found by the author re-reading the package.** Two were found by commands run for a different purpose entirely, and the largest — 6 failed corrections over 13 statements — was found only because a smaller accident made its population worth executing. That is the same distribution the programme has recorded since round 2, and it is the argument for `P06_AAS03_BOUNDED_CHALLENGE.md` being a separate step rather than a section of this file.
