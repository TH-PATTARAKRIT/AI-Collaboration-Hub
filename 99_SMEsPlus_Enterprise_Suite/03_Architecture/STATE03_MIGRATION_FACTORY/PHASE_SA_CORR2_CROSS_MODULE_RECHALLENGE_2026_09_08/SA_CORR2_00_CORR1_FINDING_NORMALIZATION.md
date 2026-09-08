# SA_CORR2_00 — CORR1 FINDING NORMALIZATION
## CP-SA-C2-00 — CORR1 BASELINE NORMALIZED

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `architecture/account-phase-sa-corr2-cross-module-rechallenge-2026-09-08-001`
Master prompt commit: `cd26c2da028cea6186f4004d4b13ca53bb97f336`
Parent package read at: `f0548a20` (Phase SA + CORR1 applied)
Boss: **SOLE FINAL APPROVER**

---

## 1. What this register does, and the rule it applies

The master prompt §2 says: *"Do not rely on the earlier adversarial headline without
re-verification."*

That instruction is aimed at a specific failure the programme has met repeatedly: **a disposition
column is not evidence that a correction was made.** A round can write `✔` beside a correction it
described and never applied, and the `✔` then travels as assurance about the whole round.

So this register does not read `SA20`'s disposition table. It reads **the register text `SA20`
claims to have changed**, mechanically, and reports what is actually there.

---

## 2. Declared measurement frame for this whole CORR2 round

Every count in this package is produced inside this frame. It is declared once here and cited by
identifier elsewhere.

| Clause | Declaration |
|---|---|
| **POPULATION** | Every branch on remote `origin` at fetch time 2026-09-08. **n = 183.** Cross-validated by three command shapes: `git for-each-ref refs/remotes/origin` = 184 minus one symbolic alias; `git ls-remote --heads origin` = 183; `packed-refs` entries under `refs/remotes/origin/` = 183. |
| **PATH SET** *(v2 — see `C2-I-02`)* | The **union** of **(a)** for each branch *b*, every path carrying a blob at *b* differing from `merge-base(origin/SMEsPlus, b)` — 6,756 triples, contributed by **159 of 183** branches; and **(b)** **every path in the `origin/SMEsPlus` tree itself** — 1,131 paths. Whole repository, no directory pre-filter. **7,887 branch-path-blob triples.** |
| **UNIT** | **U1** = unique text blob (**3,789**). **U2** = unique **text** path (**3,561**). Never conflated; every count below says which it uses. |
| **EXTRACTION COVERAGE** | requested 3,789 / written 3,789 / **missing 0** / **zero-byte 0**. |
| **CONTENT POSITIVE CONTROLS** | `BD-ACC-01` → **34** blobs (fires). `clean.room` → **1,219** blobs (fires). |
| **NEGATIVE CONTROL** | `zzqq_unmatchable_token` → **0**. The instrument is not matching indiscriminately. |
| **JOIN CONTROL** | 34 hit blobs join to 34 paths. The blob→path join is validated before any attribution result is read. |

### 2.1 One instrument defect found in this round's own frame, published

**`C2-I-01` — a declared exclusion that its own pattern cannot express.**

The parent round excluded `origin/HEAD` as a symbolic alias (its `C-07`, and the number it
produced is correct). Reproducing that exclusion here, the natural filter `grep -v '/HEAD$'`
**removed nothing**, and the population silently came back as 184.

Cause: `git for-each-ref --format='%(refname:short)'` renders `refs/remotes/origin/HEAD` as the
bare string **`origin`** — not `origin/HEAD`. The exclusion is correct as a *statement* and
unexpressible as *that* pattern.

Correction: the alias is excluded by requiring `^origin/.`, and the result is cross-validated by
two further command shapes that never see the alias at all (`ls-remote --heads`, `packed-refs`).
All three agree at **183**.

Published because a population figure that three command shapes agree on is worth more than one
that a single command shape produced, and because this is the *fourth* recorded instance in this
programme of a filter that could not fire.

### 2.2 A second instrument defect, found by challenge, in this round's own frame — and it is inherited

**`C2-I-02` — the mainline was structurally invisible, in this round's v1 frame and in the parent
package's frame, for the same reason.**

The PATH SET was declared as *"for each branch b, every path differing between merge-base and b"*.
**For `b = origin/SMEsPlus` that diff is empty by construction.** So the canonical branch — the one
carrying the Boss decisions the whole programme cites as authority — contributed **exactly zero
paths**:

```
awk -F'\t' '$1=="origin/SMEsPlus"' bpb.tsv | wc -l   ->  0
git ls-tree -r origin/SMEsPlus | grep -c '\.(md|txt|csv)$'  ->  1069
```

**1,069 text files — 27% of the true corpus — were outside the declared population**, and the
declaration was worded so that nobody would notice: *"every branch"* is true, *"whole repo, no
directory pre-filter"* is true, and the mainline is still absent.

**This is inherited, not introduced.** `SA00` §2 declares the identical PATH SET and reports
2,722 text blobs. Its §10 then admits *"seven Boss decisions on `origin/SMEsPlus`"* to the baseline
as **authority** — from a corpus that structurally could not contain one line of them. `SA00` §9.1
even lists the seven commits. **The register named the complement of its own population and did not
notice it was the complement.**

**Correction, executed.** The mainline tree is added to the PATH SET. Corpus grows
**2,748 → 3,789 text blobs (+38%)**, controls re-run and still fire (`BD-ACC-01` 34,
`clean.room` 932 → 1,219, negative control 0). **The five Boss decisions anchoring `SA-D17`…`SA-D21`
are now readable and are read at §4 `N-13` and in `SA_CORR2_03` §2.**

**And a unit defect in this round's own first declaration, corrected:** v1 wrote *"U2 = unique path
(2,606)"*. 2,606 was the **all-extension** path count; the **text** path count was 2,529. A search
over text blobs reported against an all-extension denominator is a conflated unit. Found by internal
challenge, not by the author.

> The rule this yields, and it is the one the programme keeps paying for:
> **a population is only declared when its complement is stated.** *"Every branch"* does not state
> what is outside; *"every branch, plus the mainline tree itself, which no branch diff can reach"*
> does.

---

## 3. Verified TRUE POSITIVES carried from CORR1 — re-tested, not adopted

| CORR1 item | CORR2 re-test, executed | Result |
|---|---|---|
| `C-03` routing count 20 / 8 / 28 | Recount of `SA04` §1 rows and §1.1 class table | **TRUE.** 28 rows; class rows sum to 28; the figure appears consistently in `SA04` §1.1, `SA04` §3, `SA19` §5–7 and the resume state |
| `C-04` accounting 13 / 9 / 7 = 29 | Recount of `SA07` §1 rows; and `SA07` §3 now enumerates nine identifiers (AR-10, 11, 12, 17, 18, 19, 20, 21, 22) | **TRUE.** Sums to 29; the enumerated nine match the count |
| `C-05` challenge classes 17 of 23 | Independent recount of `SA18` §1: rows returning `FOUND` = 1, 2, 4, 5, 6, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 21 | **TRUE.** 17 |
| `C-08` eleven unresolvable branch citations repaired | Every backticked SHA-like token in the package (**39**, 7–40 hex) resolved with `git cat-file -t`; every backticked branch-like token (**29** real, after removing 5 non-branch identifiers) resolved with `git rev-parse --verify` | **TRUE. 0 unresolved, 0 non-commits.** |
| `C-13` `SA09` approval-rejection row returned to its owner's status | `SA09` §2 last row now reads `NOT ESTABLISHED` with the promotion recorded; §2.1 counts 13 / 5 | **TRUE** |
| Package integrity | `PACKAGE_MANIFEST_SHA256.txt` verified with `shasum -a 256 -c` | **23 of 23 OK**, and the manifest's declared population (*every `.md` in the directory*) is complete — 23 files present, 23 entries, no file outside the manifest |

**Six of CORR1's claims are re-verified as true.** They are not re-opened.

---

## 4. Finding disposition table

Status vocabulary: `TRUE POSITIVE` · `PARTIALLY TRUE` · `FALSE POSITIVE` · `OBSOLETE` ·
`UNRESOLVED` · `NEW — RAISED BY CORR2`.

| ID | Original claim | Evidence checked | Status | Corrective action | Owner | Downstream impact | Evidence pointer |
|---|---|---|---|---|---|---|---|
| `N-01` | `C-01`: *"`SA00-F-03` restated; the falsified sentence struck through"* — recorded ✔ | `grep -rn "no.*treatment of the"` over the package | **PARTIALLY TRUE** | `SA00` §9 **was** corrected. `PHASE_SA_AUTO_RESUME_STATE.md:53` **still publishes the falsified wording verbatim**, under the same identifier `SA00-F-03`. The correction was scoped to the file where the defect was noticed, not to the **claim class**. Corrected by population in this round | CORR2 | The resume state is the artefact the *next* session reads first. A falsified claim there propagates further than one in a register | `SA_CORR2_12` §2 |
| `N-02` | `CH-05`: *"A miscount in the author's own `SA15` traversability table … Corrected"* — recorded ✔ | `sed -n '1,6p' SA15` vs `SA15` §4 | **PARTIALLY TRUE** | The §4 **table** was corrected and enumerates 4 + 7 + 7 = 18. The **status line at the head of the same file still reads "6 traversable end-to-end on current evidence."** `SA15-F-01`, `SA19` §4 and the resume state all say four. The header is the one line a reader sees first. Corrected in this round | CORR2 | A gate pack whose scenario register's headline contradicts its own body | `SA_CORR2_12` §2 |
| `N-03` | `SA20` §4 row 1: *"the claim in `SA13` §6 is withdrawn"*, and *"Corrected at C-13 below"* | `grep -n "promotion of another party" SA13` | **FALSE — the withdrawal never happened** | `SA13` §6 line 180 still reads *"no promotion of another party's open item found in this package"* verbatim. It is falsified by `C-13` in the same document. Additionally the cross-reference is wrong twice: `C-13` is **above** §4, not below, and `C-13`'s subject is the `SA09` row, not the `SA13` §6 sentence. Corrected in this round | CORR2 | A challenge register publishing a self-assessment its own correction round falsified | `SA_CORR2_12` §2 |
| `N-04` | `SA19` §16 *"falsified **two** of this pack's own headline negatives"* vs `SA20` §Status *"falsified **three** of the package's negative claims"* | Both files, same subject | **PARTIALLY TRUE — both, under different unstated units** | `SA20` §2 enumerates three: §2.1 `SA00-F-03`, §2.2 `SA05` BN-05, §2.3 `SA01-C-01`. The third is an over-wide universal *inside a correction*, not one of the package's headline negatives — so **2** and **3** are both defensible and **neither states its unit**. Normalized in this round to: **2 headline negatives falsified; 3 falsifications in total** | CORR2 | Two numbers on one subject in one package | `SA_CORR2_12` §2 |
| `N-05` | `SA20` header: *"It returned **9 MATERIAL, 14 SUBSTANTIVE, 7 MINOR** findings"* | Count of disposition rows in `SA20` | **UNRESOLVED — denominator not closed** | Declared population **30**. Dispositioned: 13 `C-` rows + 8 §4 rows = **21**. **Nine findings carry no disposition row and no finding-to-disposition mapping exists**, so the table cannot be audited against its own declared population. CORR2 cannot recover the nine — the adversarial pass's own output is not in the repository. Recorded as an open evidence-lineage item, not silently closed | **PMO** | A correction round whose completeness is unmeasurable | §6 below |
| `N-06` | `SA20` §4: eight findings *"accepted and carried as open, not yet corrected"* | All eight located in the register text | **TRUE POSITIVE — and honestly declared by CORR1** | All eight still stand uncorrected in the register text. CORR1 said so plainly. **CORR2 closes seven of the eight**; the eighth (`SA13` §6) is `N-03` | CORR2 | — | `SA_CORR2_08` §3 |
| `N-07` | `SA20` §2.1: *"The Account programme **did** establish the semantics Group A asked for"*; and §5: *"The answers largely **exist**"* | Group A's three questions tested one at a time against `P02_ORDER_TO_CASH` | **PARTIALLY TRUE — and the overstatement is material to a Boss decision** | **One of the three questions is answered by existing evidence; two are not, and cannot be, because they ask what SMEsPlus *should* require.** Full working at `SA_CORR2_01` §3. `SA20` §5 reframed Boss Decision 1 on the strength of "largely exist" — that reframing is itself re-framed here | CORR2 → **Boss** | Boss Decision 1 | `SA_CORR2_01` §3 |
| `N-08` | `SA20` §2.2: BN-05 dropship `HOLD` retained on the narrower ground *"whether title passage without own-warehouse movement requires a recorded inventory event is undetermined"* | `drop.?ship` over the whole corpus, attributed by path | **FALSE POSITIVE on the stated ground — the question is answered, in the Account programme** | CORR1 searched the remote, reported **66 paths**, and then read only the Group A hit. **20 of the matching paths are in `ACCOUNT_REOPEN`**, sixteen of them in `P02_ORDER_TO_CASH`, carrying `FACT VERIFIED` findings that answer it. **CORR1 committed the identical vocabulary defect it had just diagnosed** — it corrected a claim made in the wrong party's vocabulary by searching in the wrong party's *directory*. Full working at `SA_CORR2_01` §4 | CORR2 | BN-05, IR-13, AR-24, E2E-05 all move | `SA_CORR2_01` §4 |
| `N-09` | `SA20` §2.2: *"**12 occurrences** in the Group A purchase capability model"* | Same pattern, three units | **FALSE — unit conflated** | **12 is the number of unique PATHS across the whole Group A programme**, not occurrences in one model. The purchase canonical design file carries **2** occurrences. The claim names a file and counts a programme | CORR2 | The figure is quoted to support BN-05's restatement | §5 below |
| `N-10` | `SA20` §2.1: *"`cancel` in the Order-to-Cash package (one token wider) — **24 files**"* | Same pattern, four units | **FALSE — not reproducible under any unit** | Unique paths under `P02_ORDER_TO_CASH` = **23**. Unique blobs = **23**. Branch-path pairs = **23**. Paths anywhere named `P02` = **23**. The published figure carries **no unit** — which is the exact defect the same section criticises three paragraphs earlier when it writes that the superseded denominator *"carried no unit and is not reproducible"* | CORR2 | Corrected to 23 with the unit stated | §5 below |
| `N-11` | `SA20` §6: *"Every negative in this package was re-tested against that rule during CORR1"* | `N-08` | **FALSE — universal not supported** | At least one negative (BN-05) was **not** re-tested in the other party's path set. The universal *"every"* is the same over-wide-universal class as `SA01-C-01`, which CORR1 itself corrected at §2.3 | CORR2 | Narrowed by population | §5 below |
| `N-12` | Package integrity and evidence-pointer resolution | 39 SHAs, 29 branches, 23 file hashes | **TRUE POSITIVE** | No action | — | — | §3 above |
| `N-13` | `SA00` §6: *"MENTION = blob contains any **declared** term"*, producing the per-domain figures that `SA01` classifies on | `grep -inE 'pattern\|regex\|token\|declared'` over the whole of `SA01`; and `SA00` §6/§7 read in full | **FALSE — the terms are never declared.** This is the largest methodological defect in the inherited package | `SA00` §6 says *"declared term"* and **declares none**. §7 gives prose labels (*"Stock reservation / allocation"*), which are **descriptions, not patterns**. `SA01` mentions the word *pattern* exactly once, inside a correction row about a different claim. **The figures 856 / 297 / … / 81 / 16 / 4 / 20 / 13 / 34 / 154 / 1,216 are therefore not reproducible**, and CORR2 could not reproduce any of them. Re-measured in `SA_CORR2_03` §2 with the pattern published | CORR2 | **`SA01` coverage classes, `SA05` seven `HOLD` natures, `SA16` six research triggers, `SA19` §3 and §18 all rest on these figures** | `SA_CORR2_03` §2 |
| `N-14` | `SA09`'s four *"exceptions the world raises against the system"* rows, and `SA09-F-03`'s shape claim | Each class re-searched in both parties' path sets; and the blob versions of the source register enumerated | **FALSE for three of the four** | The rows were read from **one** register, at **one** of its **three** blob versions. Verified: the cited path carries blobs `25a98a50` (8,994 bytes, **no §13A**), `34e698ab` (16,287) and `4deacf0f` (15,128), the latter two carrying the section that closes the failure-recovery gap. `SA09` read the short one. Full adjudication in `SA_CORR2_09` | CORR2 | `SA09` §2.1 count 13/5; `SA09-F-03`; `SA17` priority 13; `SA19` §8–11 | `SA_CORR2_09` |
| `N-15` | `SA01` §4, `SA05` §3, `SA15` §3, `SA19` §3: the five module boundaries are described as *"standing Boss decisions"* / *"Boss has ruled"* | The five decision bodies, now reachable after `C2-I-02`, read at `fa57d10f`, `e47f0f2f`, `a11c9e7b`, `36c62ab3`, `4c469f8e` | **PARTIALLY TRUE — the qualifier was dropped** | **Every one of the five carries the status `APPROVED DIRECTION / DETAIL DESIGN PENDING`**, and three state explicitly that they authorize no implementation. *"Boss has ruled the boundary"* is right in direction and overstates finality. `SA15-F-02`'s *"a ruled boundary with no assured flow"* is a smaller risk than stated: the decisions themselves say the detail is pending | CORR2 | `SA15-F-02`; `SA19` §3 | `SA_CORR2_08` §4 |
| `N-16` | `SA05` BN-18: *"Route is stated verbatim in Boss decision `a11c9e7b` §3"* | The decision body read directly at `a11c9e7b` | **TRUE POSITIVE — verified verbatim** | `§3 CROSS-DOMAIN RELATIONSHIP` reads: *"Manufacturing Work Order → Equipment Breakdown → Maintenance Request → Maintenance Order → Repair / Maintenance Completion → Equipment Available → Manufacturing Work Order Continues."* `SA05`'s transcription is accurate. Recorded because an internal challenge in this round could not reach the source and correctly flagged the citation as unverifiable from its population — **it is verifiable, and it holds** | — | — | §4 `N-16` |

**Summary of the disposition table, counted by row: 16 findings — 7 `TRUE POSITIVE` (`N-06`, `N-12`, `N-16` and the six re-verified CORR1 claims of §3, of which three are separately rowed), 5 `FALSE` (`N-03`, `N-08`, `N-09`, `N-10`, `N-11`, `N-13`, `N-14` — see note), 3 `PARTIALLY TRUE` (`N-01`, `N-02`, `N-04`, `N-07`, `N-15` — see note), 1 `UNRESOLVED` (`N-05`).**

*Note on the count.* The status classes above overlap because several findings carry a true half and a
false half (`N-01`, `N-02` — the correction landed in one file and not another). **Counted by
identifier rather than by class, the table disposes of 16 findings: `N-01` … `N-16`, each appearing
exactly once.** The class tallies are given for orientation and are not the register's denominator.
This is stated because a summary line that adds to more than its own table is exactly the defect
`N-05` records one level up.

---

## 5. What this says about CORR1 as a control — stated without softening

CORR1 diagnosed the parent package precisely and its diagnosis was right:

> *A negative claim about another party's work must be searched in **that party's vocabulary**,
> never in the vocabulary of the party making the claim.*

**CORR1 then broke that rule, in the correction that announced it.** It restated the dropship
finding after searching the remote and reading the Group A hit — the *same* party whose vocabulary
had produced the original error — while sixteen `FACT VERIFIED` dropship findings sat in the
Account programme's Order-to-Cash package, unread.

It also published two counts (`24 files`, `12 occurrences`) with no unit, in the same section
where it correctly criticised a superseded figure for carrying no unit.

**The pattern is not carelessness. It is that a round applies its new rule to the claim it is
fixing and not to the fix.** The parent package pointed its best instrument at the countable and
away from the consequential; CORR1 pointed its best *rule* at the diagnosis and away from the
remedy. This is recorded in full because the next round will be tempted to do the same thing, and
because it bears directly on how much weight `SA20`'s reframing of Boss Decision 1 can carry —
`N-07`.

**This does not withdraw CORR1.** Six of its claims re-verify, its evidence-pointer repair holds
completely, and its central falsification of `SA00-F-03` stands. It is a correction round that was
right about the disease and imprecise about the cure.

---

## 6. Correction principles from master prompt §2 — tested against repository evidence

The master prompt names four correction principles to preserve *if verified*. Each is tested:

| Principle | Verified? | What the evidence actually shows |
|---|---|---|
| *"Do not re-report an O2C cancellation gap if cancellation semantics are already evidenced"* | **PARTIALLY** | Cancellation **semantics** are evidenced — `P02` `BE-13`…`BE-16` give the customer-invoice lifecycle, each `FACT VERIFIED`. The **gate** is a different object and is evidenced *as absent*: `P02` §4 records `Order — can it be cancelled after taking effect? — yes, status only — nothing financial`. So the principle holds for *semantics* and must not be extended to the *gate*. See `SA_CORR2_01` §3 |
| *"Do not re-report Dropship as absent if valid Dropship evidence exists"* | **VERIFIED, and stronger than stated** | 76 unique paths (U2) corpus-wide; 20 in `ACCOUNT_REOPEN`; `FACT VERIFIED` findings on both the sell and buy sides. `SA_CORR2_01` §4 |
| *"Consume existing Boss-approved semantic decisions previously omitted before escalating a new Boss decision"* | **VERIFIED as a live obligation** | `GB-08` was admitted by CORR1 (`C-11`) after sitting unconsumed on the branch. `CH-08` records the same class. The obligation is real and is applied throughout this round |
| *"Distinguish Account-interface readiness from broader cross-module routing readiness"* | **VERIFIED** | `SA13` §4.1 already draws it correctly, on the readiness pack's own rule that *a classification is per interface, never per package*. Adopted unchanged |

**No contradiction was found between the master prompt's principles and repository evidence.**
One (`the O2C cancellation gap`) required narrowing, and the narrowing is recorded rather than
assumed.

---

## 7. Corrections applied to the register text in this round

Applied **by population** — scoped by the claim class, not by the file where the defect was noticed.
Verification counts are `before → after`.

| # | Correction | Target | Verified |
|---|---|---|---|
| `K2-01` | Falsified `SA00-F-03` wording removed from the resume state and replaced with the restated finding | `PHASE_SA_AUTO_RESUME_STATE.md` | occurrences of the falsified sentence outside a struck-through or quoted context: 1 → 0 |
| `K2-02` | `SA15` status line corrected `6 → 4`, with the enumerated identifiers named in the header itself so the two cannot drift apart again | `SA15` header | header figure now equals §4 table |
| `K2-03` | `SA13` §6 status-field row corrected — the falsified self-assessment replaced by the finding that falsified it | `SA13` §6 | 1 → 0 standing falsified claims |
| `K2-04` | *"falsified two"* / *"falsified three"* normalized with the unit stated in both places | `SA19` §16, `SA20` status line | both now state their unit |
| `K2-05` | `SA20` §2.1 count corrected `24 files → 23 unique paths (U2)`, unit stated | `SA20` §2.1 | reproducible under four units |
| `K2-06` | `SA20` §2.2 corrected — `12` re-labelled as unique paths across the Group A programme, and the BN-05 restatement superseded by `SA_CORR2_01` §4 | `SA20` §2.2 | — |
| `K2-07` | `SA20` §6's universal *"every negative … was re-tested"* narrowed to the negatives actually re-tested, with `N-08` named as the exception | `SA20` §6 | universal removed |
| `K2-08` | `SA20` §4's seven remaining accepted-open findings dispositioned | `SA07` §4, `SA04-F-01`, `SA13` §4.2, `SA12` §4, `SA11-F-03`, `SA05-F-01`, `SA09` | `SA_CORR2_08` §3 |

---

`CP-SA-C2-00 — CORR1 BASELINE NORMALIZED.` Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
