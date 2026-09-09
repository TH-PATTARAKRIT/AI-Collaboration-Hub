# SA_CORR4_08 — SMEs CORE FINAL RE-CHALLENGE

## CP-SA-C4-80 — SMEs CORE FINAL RE-CHALLENGE COMPLETE

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR4-PREGATE-CLOSURE-001]`
Branch: `architecture/phase-sa-corr4-pregate-closure-2026-09-09-001`
Boss: **SOLE FINAL APPROVER**

---

## 1. The result, before the method

> **Two independently-scoped challengers were instructed to falsify the four closures. They returned
> `9` material findings against this package. `8` of the 9 verified against primary source and were
> accepted; `1` was refuted. `3` further findings were produced by the orchestrator's own arithmetic
> and consistency sweeps.**
>
> **The largest single correction moved `C4-02`'s cross-domain result from `5 CONTRACT-SUFFICIENT / 5
> CONTRACT-GAP` to `2 / 8`.** It was not a computational slip. **This file had stated one test and
> silently applied a weaker one to three rows**, and the weaker test flattered the result.

**No closure was overturned. Every closure was corrected.** `C4-01`, `C4-02` and `C4-03` remain
`CLOSED`; `C4-04` remains `NOT CLOSED`; **and one of the corrections removed the cited authority from
the argument by which `C4-04` reduces 183 branch-acts to one.**

---

## 2. Method, and the one thing it got wrong

| | |
|---|---|
| Challengers | **2**, independently scoped, same model, **different vocabularies** — CORR3's recorded reason this works |
| Challenger A | Security/Authorization · SaaS/Tenant/Company · Data/Identity · Integration — 10 named attack targets |
| Challenger B | PMO/Governance · Audit/Standards · Clean-room · Accounting · Inventory · Manufacturing/Purchase · Functional — 11 named attack targets |
| Instruction | *"YOUR JOB IS TO FALSIFY, NOT CONFIRM. A challenge that finds nothing is a failed challenge."* Each was handed the four closures' **own §7 residuals**, i.e. told where their author thought they were weakest |
| Orchestrator's own controls, run in parallel | tally re-derivation from table rows; identifier-sequence sweep; cross-file consistency sweep; `PASS`-wording sweep; clean-room token sweep; SHA resolution of all 21 cited objects |
| **Perspectives covered** | **11 of 11** required by master prompt §10 |

### 2.1 `C4-08-F-01` — the package was **not frozen** while the challenge ran, and that is a defect

Challenger B raised this first, and it is correct. **While independent review was in progress the
branch received four commits**, `SA_CORR4_05` appeared, and three files grew. **The challenger watched
`SA_CORR4_02` §3.1's tally defect get corrected underneath its own audit.**

> **The programme's own recorded rule is `freeze the package before review opens`. It was not
> followed.** Two consequences, and both are real:
>
> - **It invalidated part of the challenger's own report**, which had to time-stamp every verdict
>   against a moving commit graph.
> - **It produced a false claim inside this package.** `SA_CORR4_02`'s `C4-02-F-06` asserted that
>   *"every count in `SA_CORR4_06` was re-derived the same way after it."* **That was untrue when
>   written** — `SA_CORR4_06` carried an uncorrected instance of the identical defect, which the
>   challenger then found. **The claim is withdrawn at `C4-06-F-01`.**
>
> **A self-reported sweep is not evidence that the sweep ran.** The only reason this was caught is that
> a challenger checked the claim rather than the conclusion.

---

## 3. The ten challenge questions, answered

| # | Question | Answer |
|---:|---|---|
| 1 | **Did `C4-01` miss any privileged route?** | **YES — three findings.** A **fifth** Platform-Admin cross-tenant act (`FR-SM-005`, entitlement-granting); a **fourteenth path class** (approval execution); and a **second audit schema** with the same missing axis. **All three were inside the five `FDS` files `C4-01` §8.3 declared and did not open** |
| 2 | **Can any receiver still execute without authoritative tenant context?** | **YES.** `FDS_INTEGRATION` defines how a non-human principal authenticates and names four tables with **no columns**; `tenant_id` and `company_id` return **0** on both instruments. Classes 1, 6, 11, 13 and 14 have no stated execution context |
| 3 | **Can company context be inferred incorrectly or substituted silently?** | **YES.** `MTA-05` — *"a background or import path finds no company and falls back to 'the first' or 'the default'"* — `RESIDUAL: MATERIAL`. Its mitigations (`MTI-20`, `MTI-45`) are `SPECIFIED`, **not built** |
| 4 | **Can `XMC-C-D1` be replayed across the wrong boundary?** | **YES, structurally.** The only idempotency carrier in the estate is *"table-global rather than tenant-scoped"*; `R6` is `SPECIFIED`, not built. **`JCP3-F-05b` stands unweakened** |
| 5 | **Is `CF-I-03` actually testable?** | **YES** — 8 deny conditions, 25 test classes, 4 of them instrument controls on the control itself. **Not executable**: `P1`–`P6` are runtime. **One design position is unrebutted** — question 7 below |
| 6 | **Does `MTI-43` now reference a real control?** | **YES.** `CF-I-03` is a published `SPECIFIED` invariant that CORR3's own register counted among its 58 while stating elsewhere that no published invariant states it. **Independently confirmed at source by Challenger A** |
| 7 | **Did propagation correct the whole compliance claim block?** | **The block, yes — the population, no.** The claim class is **one file**, established on four instruments and **re-run independently**, and **extended into Thai** (`มาตรฐาน`, `รับรอง`, `ปฏิบัติตาม`, `ใบรับรอง` — 51 blobs, 95 lines read) **with no second instance found**. **Mainline is uncorrected and public** |
| 8 | **Are any branches still carrying misleading certification language?** | **YES — 183 of 185**, including `origin/SMEsPlus`. **Independently re-verified live: `"visibility":"public"`, `HTTP 200` unauthenticated, prohibited heading present in the response body** |
| 9 | **Did any closure cross into implementation or design authority?** | **No violation found**, on an explicit sweep for schema, data types, identifier formats and API shapes. **One borderline item flagged**: `CF-I-03` §3.9's required-evidence field list approaches record shape — **without types or column names**. Recorded, not corrected |
| 10 | **Are remaining issues genuine Boss authority, or still SMEs Core work?** | **§5** |

---

## 4. Findings accepted, with what changed

**`8` challenger findings accepted · `1` refuted · `3` orchestrator self-findings.**

| ID | Finding | Source | Disposition |
|---|---|---|---|
| **`C4-02-F-09`** | **`C4-02` classified 3 of 10 flows on a weaker test than it stated.** `HX-01`/`-04`/`-18` are **Inventory's** register of facts it *receives*; on flows 1, 4 and 6 the emitters are Sales, Purchase and Manufacturing, **who have no producing-side package at all** — the exact condition used to fail flows 2, 7, 8, 9 | Challenger A | **ACCEPTED. `5/5` → `2/8`.** §5.1's finding enlarged from five gaps to eight |
| **`C4-06-F-01`** | `SA_CORR4_06` published **three different counts** for one quantity — §1 said `4` forward, §8 said `5`, the register carries `7` `Δ` marks. True: **`6` forward, `2` backward** | Challenger B | **ACCEPTED and corrected.** The `SA_CORR4_02` claim to have swept this file is **withdrawn** |
| **`C4-04-F-05`** | `SA_CORR4_04`'s namespace census reads `22` and `9`; re-derived per branch they are **`21` and `10`**. **The total of 183 survived only because the two errors cancelled** | Challenger B | **ACCEPTED and corrected.** Third instance in this package of *a total that sums while its distribution is wrong* |
| **`C4-04-F-06`** | *"The containment rule"* occurs in **exactly one blob predating this package** — `SA_CORR3_05`'s own assertion. **Asserted, never defined, traced to no ruling.** Positive control: `containment` alone returns 121 paths | Challenger B | **ACCEPTED.** It is **one weak instrument, not one of three.** The disposition now rests on the two master-prompt clauses |
| **`C4-04-F-07`** | *"The supersession rule"* occurs in six blobs, **all governing which document version to read** — none about correcting a published claim. `SA_CORR4_04` §4.3 extended it to a subject it has never covered | Challenger B | **ACCEPTED. The extension is withdrawn.** The 182-branch recommendation is restated as **a PMO judgement with no cited authority** — and it is **the reading that minimises this session's own work** |
| **`C4-02-F-08`** | `R1`/`R2` cited `SI-01`/`SI-02` as governing cross-module handoffs. The ruling's own scope is **`EVERY COA CLOSURE GATE`** — `COA-G01`…`G08` | Challenger A | **ACCEPTED.** Citations relabelled *by analogy*; **`RULED` survives** on element 10, `MTI-01`/`-02`/`-04` and `SCOPE-AWARE EVERYWHERE` |
| **`C4-01-F-08/-09/-10`** | A fifth Platform-Admin act, a second audit schema, a fourteenth path class — **all inside the declared residual** | Challenger A | **ACCEPTED.** `13` classes → `14`; `G1` `4` → `5`; **`G3` upgraded from one document's defect to the corpus's audit shape** |
| **`C4-08-F-01`** | The package was **not frozen** during review | Challenger B | **ACCEPTED** — §2.1 |
| `C4-03` §1 section pointer | `§14` should read `§13` | Challenger A | **ACCEPTED and corrected.** The quotation itself was accurate |
| Auto-resume self-contradiction | `CP-SA-C4-10` `CLOSED` in the ladder, `IN PROGRESS` in the results table | Challenger B | **ACCEPTED and corrected** |
| **`C4-02-F-06`** | §3.1 tally `9/3/1` against rows reading `10/2/1` | **Orchestrator** | Corrected before challenge closed |
| **`C4-07-F-03`** | **`SA17`, the Pre-Test handoff baseline, grades `E2E-15` its "strongest established area"** on a citation to `SA09`, which now carries an inline supersession saying idempotency *"moves the other way"* | **Orchestrator** | **§6** |
| **`C4-01-F-07`/`-07a`** | **20 architecture deliverables written and stranded on one unmerged branch**, while mainline's register declares 13 of them `Pending` | **Orchestrator** | Re-scopes `G2` |

### 4.1 The one challenger finding **refuted**

Challenger A reported that `HX-` and `HO-` are *"a total, unbroken numeric alias"* across roughly
eighteen identifiers, and that `FDS_APPROVAL` contains *"zero occurrences of tenant or company."*

- **The alias is real and the challenger is right that my "disjoint families" was wrong** — corrected
  at `C4-02-F-02`. **But my own count of six and the challenger's of eighteen were both artefacts of
  the same elision** (`` `HO-01`, `-02` ``). **Two parties, one pattern, two wrong counts.**
- **`FDS_APPROVAL` does not contain zero.** It contains **two** — an actor label *"Company Admin"* and
  a bare security bullet *"Tenant Isolation"*. **Neither carries a context obligation, so the substance
  stands and the count did not.** **REFUTED as stated, accepted as corrected.**

> **Recorded because the programme's rule is to verify a peer's claim before adopting it, and because
> this is the second time in this session that verification changed a peer's finding rather than
> confirming it** — the first being `C4-I-06`, where a reported `git grep` truncation defect **did not
> reproduce** on any of 15 fixed strings, a simple `-E`, or the broad `-E` alternation at `1,061 =
> 1,061`.

---

## 5. Are the remaining issues Boss authority, or SMEs Core work?

**Tested item by item. The answer is that almost none of it is Boss's.**

| Item | Owner | Boss decision? |
|---|---|---|
| `G1` five unscoped path classes · `G3` two audit schemas · `G5` metering/wallet integration | **SMEs Core** | **No — design acts** |
| `G2` cross-tenant-actor contradiction | **PMO + an independent reviewer** | **No.** `C4-01-F-07` re-scopes it: **a written model exists and has never been reviewed** |
| `G4` break-glass | **PMO** | **No — a staffing item.** Its owner role is named and unfilled |
| `C4-04` propagation | **PMO / repository owner** | **No.** Boss decisions `03` and `05` **already prohibit the claim class**; applying them is execution |
| `C4-D-01` the Boss-mandated joint interface artifact | **PMO** | **No — an appointment** |
| `C4-07-F-03` `SA15`/`SA17` over-grading | **`SA15`/`SA17`'s owner** | **No — a Phase SA correction** |
| The 20 stranded deliverables | **PMO** | **No — a merge-or-archive decision, then review** |
| **Element 15's severity — is idempotency gate-blocking?** | **Boss** | **YES.** *"Rule on whether idempotency is gate-blocking"*, `UAE-29` `HOLD — BOSS DECISION REQUIRED — the root` |
| **The five scenario-level Boss decisions** — `JT-05`, `XD-01`, return basis, service routing, `C2-D-01`/`03` | **Boss** | **YES — carried, not re-asked** |
| **Thai statutory items** | **Boss / Legal / Tax** | **YES — evidence acquisition, unchanged** |
| **6 vetoes in force** | **Boss / issuers** | **YES — none discharged, none asked to be** |

> **Of the twelve open items this package leaves, `7` are SMEs Core or PMO work and `5` are genuinely
> Boss's — and `4` of those `5` were already Boss's before this round began.** **CORR4 adds exactly
> one new item to Boss's list: nothing.** Every finding it raised has a non-Boss owner.

---

## 6. What survived the challenge unweakened

**Stated because a re-challenge report that lists only damage misrepresents its own result.**

| Claim | Verdict |
|---|---|
| **No Phase SA artefact cites the `FDS` domain family** | **CONFIRMED.** Challenger A searched `FDS`, `SaaS Foundation`, `FR-IAM-`, `FR-INT-`, `FR-AUD-`, `TEN-00`, `BR-TEN-`, `BR-IAM-`, `BR-AUD-`, `BR-REP-`, `Platform Operator`, `Platform Admin` across all `SA*` artefacts — **zero hits on every one**, `MODULE_SPEC_AUTHORIZATION` firing 6 as a positive control |
| **The cross-tenant-actor contradiction is real** | **CONFIRMED and understated by me.** Challenger A found the only candidate resolution, `ARC-WP-009`, **contradicts itself on the identical question** — §12.4 lists Platform Operator as a standard role while §12.5/§16/`AC-004` assert no role widens scope beyond its tenant. **A third independent self-contradiction, inside the document I named as the possible fix** |
| **The audit record carries 1 of 4 axes** | **CONFIRMED exactly**, under no alias — `resource`/`resource_id` name the audited object, not the company — **and corroborated by a second schema** |
| **`CF-I-03` is a published `SPECIFIED` invariant** | **CONFIRMED, and CORR3's self-contradiction confirmed at source.** Challenger A: CORR3 *"uses 'specified, not built, not verified' precisely and repeatedly elsewhere; its choice of 'does not exist' for `CF-I-03` specifically breaks that pattern"* |
| **The compliance claim class is one file** | **CONFIRMED and extended into Thai** — a language every prior instrument in this chain was blind to. **The negative got stronger** |
| **Public exposure** | **CONFIRMED live and unauthenticated, and the challenger judged it understated** |
| Core denominators — `185` · `3,926` · `3,604` · `183/2/0` · `58` | **All re-derived from scratch and reproduced exactly** |
| `PASS`-wording · clean-room · implementation-authority | **Clean on all three**, each swept independently |

### 6.1 The one design position the challenge left standing, and unrebutted

`CF-I-03` §3.4 reads the grant **in force at the act's timestamp**. §6 named this the file's weakest
point and invited attack. **Challenger A took the invitation and made the case worse than I did:**

> Searched the whole 185-branch corpus for *grant validity · grantor authority · void grant · rescind ·
> retroactive revocation · fraudulent grant · compromised credential* — **zero hits, every term.**

**`CF-I-03` §6.5 answers the objection by saying revocation-for-cause is *"a separate finding over the
same act."* No such mechanism exists anywhere in the corpus.** Under the design as specified, **an
actor whose grant was obtained fraudulently, or issued by a grantor who lacked authority, is certified
`CONFORMANT` permanently, with no compensating control.**

> **This is not corrected here, and it is not a defect in the control's specification** — it is a
> **named absence in the control set around it**, and inventing the missing control would be exactly
> the self-serving move `CF-I-03` §6.5 was trying to avoid. **It is added to `G1`'s neighbourhood as
> `C4-08-F-02` and carried to the Boss Final Gate as an SMEs Core design act** — the first thing to
> design *after* `CF-I-03`, not inside it.

---

## 7. What the challenge did not reach

1. **Both challengers drew from one corpus assembled by one party.** `ND-12` records that internal
   challenge cannot escape this, and **CORR3 said the same of its own nine-executor panel.** Two
   challengers with different vocabularies found what one would not; **neither is the structurally
   independent review that `PHASE-SA/Q-BOSS-02` requires and that no appointment yet covers for
   Phase SA.**
2. **Neither challenger was asked to falsify `SA_CORR4_05` or `SA_CORR4_07`'s conclusions directly** —
   they were given the four closures and the reclassification. **`C4-07-F-03`, the finding with the
   most direct bearing on the Pre-Test authorization, came from the orchestrator, not from either
   challenger.** A third challenger scoped at the Pre-Test handoff would have been the right fourth
   control and was not run.
3. **The `1,061`-path compliance population remains ~12% read.** Extending into Thai strengthened the
   negative; **it did not close the sample.**
4. **`ARC-WP-008` and fifteen other stranded deliverables are still unread.**

## 8. Checkpoint

> ## `CP-SA-C4-80 — SMEs CORE FINAL RE-CHALLENGE COMPLETE`
> **2 challengers · 11 of 11 perspectives · 10 of 10 questions answered · `9` challenger findings,
> `8` accepted and `1` refuted-as-stated · `3` orchestrator findings · `1` largest correction
> (`5/5` → `2/8`).**
> **0 closures overturned · 4 closures corrected · 0 vetoes discharged · 0 invariants proven ·
> element 10 does not move.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
