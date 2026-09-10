# B-7 ROUND 2 — INDEPENDENT CHALLENGE VERDICT

# `HOLD`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-ROUND2-001]`
Challenged branch: `architecture/account-phase-pretest-new-session-2026-09-10-001`
Challenged SHA (as handed by Boss): `c91d58406b4ac504f2216e68b9fe16851eb23b2d`
This channel: `audit/b7-round2-independent-2026-09-10` — **the canonical branch was NOT written**
Boss: **SOLE FINAL APPROVER**

> **This verdict is `HOLD`. It is not an `EC-07` pass. It does not authorize Functional Design.
> The executor cannot convert it into a `PASS`.**

---

## 0. MANDATORY DISCLOSURE — THE APPOINTED INDEPENDENCE DOES NOT EXIST

`17_` §0 appoints **"Independent OpenAI GPT-5.6 Sol"** and requires *"different vendor"* independence.

**This session is Claude Opus 5.** It is **not** the appointed party. That is disclosed before any
finding, because the next fact makes it load-bearing.

```
$ git log -3 --format='%h %s%n%b' c91d5840 | grep -i 'Co-Authored'
     Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>     <- challenged package
     Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
     Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>

$ git log -1 --format='%h %s%n%b' 5bd36d62 | grep -i 'Co-Authored'
     Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>     <- B-7 ROUND 1 VERDICT
```

**`R2-F-01` — MATERIAL.** The repository record shows **B-7 Round 1 was executed by the same model
family as the party it audited.** The package asserts the opposite in at least five places
(resume state: *"appointee **Independent OpenAI GPT-5.6 Sol**, new clean session, **different vendor**"*).
**No artefact in the frozen package evidences the appointee's participation in Round 1**, and the only
authorship metadata that exists contradicts it.

**Consequence:** every downstream statement that rests on *"an independent party has now attacked it"*
— including exit condition `2`'s move to `SATISFIED — QUALIFIED` on the ground that
*"`B7-F-13`'s circularity is **cured** — an independent party has attacked it"* (`08_` row 2) — rests
on an independence the record does not support. **Exit condition `2` is not safe at
`SATISFIED — QUALIFIED` on that ground.**

**This verdict inherits the same defect and must be read as a second-line challenge, not as independent
assurance.** Recording it as an `EC-07` pass would repeat the `AAS-V-02` error the package correctly
refuses to commit: asserting that an act by a designated external party occurred when no evidence
shows it did.

---

## 1. VERDICT

| | |
|---|---|
| **VERDICT** | **`HOLD`** |
| Targets mandated | `13` (`T1`…`T13`) |
| Targets executed | **`13`** |
| Falsification attempts recorded | **`13 of 13`** |
| Attempts that **succeeded** | **`11`** — `T1`, `T2`, `T3`, `T5`, `T6`, `T7`, `T8`, `T10`, `T11`, `T12`, `T13` |
| Attempts that **failed** (executor upheld) | **`2`** — `T4`, `T9` |
| Findings raised | **`17`** — `R2-F-01`…`R2-F-17` · **`7` MATERIAL · `9` MODERATE · `1` MINOR** |
| My own instrument failures reported | **`3`** — §12 |
| Claims I could **not** test | **`4`** — §11 |
| Is the challenged terminal position (`HOLD PRE-TEST EXIT`) wrong? | **NO — it is understated** |
| Is the baseline reliable as a certified gate input? | **NO** |

**Why `HOLD` and not `FAIL`:** the package's substantive conservatism is real and was reproduced —
manifests verify, no canonical artefact was overwritten, `0` competing writers under the corrected
instrument, `AAS-V-02` independently re-measured as `NOT DISCHARGED`, the `18/4/0` arithmetic and
membership are internally exact, and the row-`15` re-opening reasoning is sound and runs against the
executor's interest. **Why not `PASS`:** two Boss-reserved denominators were silently reduced, an
outstanding Pre-Test obligation was dropped from the exit denominator, the ruling that produces the
headline `7 / 13` has no recorded artefact, and `MF-03`'s replacement ground is contradicted at primary
text. **A baseline whose Boss-facing counts are wrong cannot certify a successor.**

---

## 2. `T1` — RECOVERY BASELINE INTEGRITY · **ATTACK SUCCEEDED (on the declared figures, not the content)**

### 2.1 Frozen SHA — the pointer resolves to a different commit than the one I was handed

```
$ git rev-parse origin/architecture/account-phase-pretest-new-session-2026-09-10-001
c91d58406b4ac504f2216e68b9fe16851eb23b2d              <- branch head == Boss-handed SHA
$ git merge-base --is-ancestor c91d5840 <branch> && echo YES
YES
$ git log --oneline c91d5840..<branch> | wc -l
0
```

`17_` §1 instructs the auditor to resolve the frozen SHA **from the resume state**. Doing so returns:

```
$ git show c91d5840:.../PHASE_PRETEST_AUTO_RESUME_STATE.md | grep 'RECOVERED CANONICAL BASELINE ='
**RECOVERED CANONICAL BASELINE = `fec7c49b4ab3ccae4080eb9be205bfd1e308ca0e`**
```

**`R2-F-02` — MINOR.** The Boss-handed authoritative SHA (`c91d5840`) and the SHA the package's own
designated carrier names (`fec7c49b`) are different commits. I verified the substance is unaffected:

```
$ git diff --stat fec7c49b c91d5840 -- .../RECOVERY_2026_09_10/
(empty — the recovery package trees are byte-identical)
```

`c91d5840` changes exactly two lines (the pointer line and its hash in the top manifest). **No finding
in this verdict turns on the difference.** It is recorded because the instruction *"resolve the SHA from
the resume state"* does not return the SHA the auditor was told is authoritative.

### 2.2 The manifest count is wrong again — the defect `B7-F-15` raised, in the prompt that cites it

`17_` §1: *"Manifest ... **(14 entries — VERIFY the count yourself; Round 1 was handed a wrong figure,
finding `B7-F-15`)**"*.

```
$ git show c91d5840:.../RECOVERY_2026_09_10/16_RECOVERY_MANIFEST_SHA256.txt | grep -cE '^[0-9a-f]{64}  '
15
$ ... | awk 'NF==2{n++}END{print n+0}'      # second command shape
15
$ ... | wc -l                               # third
15
```

**`R2-F-03` — MODERATE.** The handoff figure is **`14`; the manifest holds `15`.** Round 1 was handed a
wrong manifest figure; the prompt that names that finding hands the next auditor a wrong manifest figure.

Three statements of the package composition exist **in one frozen commit**, and no two agree:

| Source | Statement | Measured |
|---|---|---|
| `17_` §1 | *"`14` entries"* | **`15`** |
| `15_` §1 | *"**`16` artefacts** — `01_`…`15_` + `16_` manifest"* | `16` files — but the range **includes `13_`, which does not exist**, and **omits `17_`, which does** |
| resume state | *"`01_`…`17_` + `16_` manifest — **`15` entries, `15 OK`**"* | entry count **correct**; the range implies `17` files where `16` exist |

`13_` was the recovery manifest at commit `a5bdd625` and was renumbered to `16_`; the gap is explained
by history but is not explained anywhere in the package.

**`R2-F-04` — MODERATE.** `15_` §1's inventory reproduces `B7-F-16` exactly — the same shape
(*"`N` artefacts — `01_`…`k_` + manifest"*, omitting the highest-numbered artefact). `34_` had recorded a
preventive control for this: *"The `CORR1` manifest (`37_`) lists its own membership explicitly to
prevent the recurrence."* **The control did not hold one commit later.**

### 2.3 Integrity of the content — VERIFIED, with a firing control on the checker

```
$ cd <extracted RECOVERY_2026_09_10> && shasum -a 256 -c 16_RECOVERY_MANIFEST_SHA256.txt
01_… OK   02_… OK   03_… OK   04_… OK   05_… OK   06_… OK   07_… OK   08_… OK
09_… OK   10_… OK   11_… OK   12_… OK   14_… OK   15_… OK   17_… OK          (15/15)
```

**Positive control 1 — one-byte corruption:**
```
$ printf 'X' >> 01_RECOVERY_SESSION_BASELINE.md && shasum -a 256 -c 16_…txt | grep FAILED
01_RECOVERY_SESSION_BASELINE.md: FAILED
shasum: WARNING: 1 computed checksum did NOT match
```
**Positive control 2 — synthetic injection of an unlisted file:** the checker reports **nothing**.
`shasum -c` **cannot detect additions**; coverage must be proved by set-difference, which I therefore ran.

**Every manifest in the package, entries and failures:**
```
PRETEST_PACKAGE_MANIFEST_SHA256.txt                    entries=22  failures=0
CORRECTIVE_CLOSURE.../CORRECTIVE_PACKAGE_MANIFEST…txt  entries=24  failures=0
CORRECTIVE_CLOSURE.../24_PRETEST_POST_RULING_…txt      entries=24  failures=0
CORRECTIVE_CLOSURE.../39_PRETEST_CORR1_MANIFEST…txt    entries=38  failures=0
RECOVERY_2026_09_10/16_RECOVERY_MANIFEST_SHA256.txt    entries=15  failures=0
```

**Coverage, by set-difference (POPULATION `80` files; UNIT file; PATH SET `NEW_SESSION_2026_09_10/**`):**
```
files present                                   80
distinct paths covered by some manifest         75
present but NOT covered                          5  -> the 5 manifests themselves (self-reference limit)
covered but ABSENT                               0
```
**Integrity coverage is complete. `0` unexplained gaps. This attack FAILED and the result is published.**

### 2.4 No canonical artefact modified — VERIFIED

```
$ git diff --name-status 8674f735 c91d5840
M  PHASE_PRETEST_AUTO_RESUME_STATE.md
M  PRETEST_PACKAGE_MANIFEST_SHA256.txt
A  RECOVERY_2026_09_10/01_ … 17_                    (16 additions)
$ git diff --name-only 8674f735 c91d5840 | grep -v 'PHASE_PRETEST/NEW_SESSION_2026_09_10/'
(none)
```
`0` `PT-xx` and `0` `CORRECTIVE_CLOSURE` artefacts modified. **Upheld.**

### 2.5 `R-F-01` collision instrument — re-run with the correction, and with its own controls

```
POPULATION 194 remote branches (excl. canonical) · UNIT branch · PATTERN writes vs merge-base
PATH SET  99_…/STATE03_MIGRATION_FACTORY/PHASE_PRETEST

DEFECTIVE INSTRUMENT (path presence):  2 branches carry the path
  origin/architecture/account-phase-pretest-new-session-2026-09-10-001
  origin/audit/b7-independent-2026-09-10                <- the Round-1 auditor's own read-only branch

CORRECTED INSTRUMENT (writes vs merge-base): COMPETING WRITERS = 0
POSITIVE CONTROL (same instrument on the canonical branch vs origin/SMEsPlus): 80 files  -> it fires
```
**`0` competing canonical writers. `R-F-01`'s correction is sound and its result reproduces.
This attack FAILED.**

---

## 3. `T2` — `R-D-01` PHASE PLACEMENT · **ATTACK SUCCEEDED**

### 3.1 (a) Is each re-placement supported by the criterion's OWN governing authority?

I read the cited authorities at primary source rather than in the executor's summary.

| Re-placed | Cited authority | Read at primary text | Verdict |
|---|---|---|---|
| `EC-04` → State Gate | `8C-CLARIFICATION-01` cl. 3 | `SC-54` cl. 3: *"**`EC-04` is closed by EXECUTED RUNTIME PROOF plus INDEPENDENT REPRODUCTION**, evidenced **no later than the STATE 8-Criteria Exit Gate**"* | **SUPPORTED — verbatim** |
| `EC-07` → Module + State | `SC-AUTH-02` Reading C | `SC-54` cl. 2: *"The eight Exit Criteria attach at exactly the two gates named in §5 and at no other transition … **An internal `PHASE` transition inside a State is NOT an eight-criteria gate**"*; cl. 4 places `Phase SA → Pre-Test` as an internal verification transition | **SUPPORTED** |
| `48`-item verification → Build/Test | `SA17` §2b | a real citation on the item's own subject matter (*"nothing may be read as testing tenant isolation until an implementation exists"*) | **SUPPORTED** |
| `E2E-04` `D`/`I` limbs → FD Exit / Build-Test | **none external** | `09_` §2.4 constructs an `S`/`D`/`I`/`G` limb split. `8C-CLARIFICATION-01` governs `EC-01`…`EC-08`; `E2E-04` is **not** an `EC` | **THE EXECUTOR'S OWN READING** |

**`R2-F-05` — MODERATE.** `3 of 4` re-placements rest on the criterion's own governing authority.
**The fourth — the one that removes a whole condition from the denominator — rests on a classification
the executor invented for this purpose and on no external instrument.** `14_` §1 presents all four in a
single table without distinguishing them.

### 3.2 (b) Did an obligation get LOST rather than re-registered? — **YES, and `R-F-03` did not catch it**

`09_` §3 places condition `11`'s limbs:

> *"`S` limb: Pre-Test (closed) · `D` limb: Functional Design exit · `I` limb: Build/Test ·
> **`G` limb: Pre-Test (outstanding)**"*

`09_` §2.4: *"**The `G` limb is correctly placed and is simply outstanding.**"*
`14_` §4.1: the re-grade act *"**stays live, unowned by any gate the ruling moved**"*, `OUTSTANDING`.

`14_` §2 then removes condition `11` from the exit set entirely:
```
removed : {9, 10, 11, 12}
after   : 7 satisfied / 13 applicable
surviving set {1,2,3,4,5,6,7,8,13,14,15,16,17}
```

**`R2-F-06` — MATERIAL.** **Condition `11` retains an unsatisfied, expressly Pre-Test-placed obligation
and was nevertheless removed from the Pre-Test exit denominator.** `R-F-03` re-registered the `G` limb
**in prose** and did not re-register it **in the instrument that produces the headline**. Recording an
obligation in a table while deleting the row that counts it is the loss `R-F-03` says it prevented.

**Re-derived, holding condition `11` because a Pre-Test limb remains open:**

| | Executor | Corrected |
|---|---|---|
| Applicable | `13` | **`14`** |
| Satisfied | `7` | `7` |
| Failing | `6` | **`7`** — `3`, `4`, **`11`(G)**, `13`, `15`, `16`, `17` |
| Percentage | `53.8 %` | **`50.0 %`** |

**`R-F-02`'s own warning applies to `R-F-02`'s own figure:** `53.8 %` is the number a later reader will
quote, and it is `3.8` points higher than the corrected instrument supports.

### 3.3 (c) I read the cited authorities myself — and found a control the application does not answer

`SC-54` cl. 5, **NO DUMPING**, verbatim:
> *"A current-scope Phase SA **specification** gap may **NOT** be carried into Pre-Test. **Only
> obligations that REQUIRE EXECUTION to discharge may be met in Pre-Test.** Any item moved forward must
> be recorded **with the evidence proving it is execution-dependent**."*

**`R2-F-07` — MODERATE.** `14_` applies clause 3 and clause 2 and **never addresses clause 5**, whose
principle — *forward movement requires published evidence of execution-dependency* — is the direct
control on what `R-D-01` does. For `EC-04` and the `48` items the evidence is present in substance
(*"specified, not executed"*, *"enumerated, not executed"*, `0 of 48`). For **`E2E-04`'s `D` limb — "the
target state machine carrying the supply-raised exit" — the obligation is a design artefact, not an
execution artefact**, and no execution-dependency evidence is offered for moving it. On the package's
own governing clause, that limb is the one move clause 5 would question, and it is unexamined.

### 3.4 The ruling itself has no record

```
$ git grep -n 'RECOVERY-BOSS-RULING' c91d5840 -- '*'
…/RECOVERY_2026_09_10/14_RD01_RULING_APPLICATION_AND_GATE_CONSTITUTION.md:6:
     Ruling: `[SMEPLUS-26-09-10-PHASE-PRETEST-RECOVERY-BOSS-RULING-001]` · Recovery baseline `94f23976`
--- occurrences on the entire frozen tree: 1

POSITIVE CONTROL — the previous ruling round, same search shape:
$ git grep -ln 'BOSS-RESOLUTION-001' c91d5840 -- '*'
… 17_ … 18_ … 19_ … 20_ … 21_PRETEST_BOSS_ONE_TURN_RULING_BLOCK.md … 22_ … 23_ … 26_ …  (9 files)
```

**`R2-F-08` — MATERIAL.** The prior Boss ruling round produced a **dedicated capture artefact**
(`21_PRETEST_BOSS_ONE_TURN_RULING_BLOCK.md`) plus an application register (`22_`). **`R-D-01` produced
an application register and no ruling record.** Its entire existence in the frozen package is a session
identifier in the header of the challenged party's own application file, plus quotations that party
transcribed.

Under the programme's own rule — *"executor conclusions are scope, not evidence"* — **the authority that
moves `4` of `17` exit conditions and produces the headline `7 / 13` is, in this baseline,
unverifiable by an auditor.** I cannot confirm or falsify the ruling's terms. **I record the placement
analysis as sound where it cites external authority (§3.1) and the authority act itself as
UNEVIDENCED.**

---

## 4. `T3` — THE `7 / 13` EXIT COUNT · **ARITHMETIC UPHELD · DENOMINATOR FALSIFIED**

**Arithmetic, re-executed independently:**
```
satisfied {1,2,5,6,7,8,14}                       = 7
failing   {3,4,9,10,11,12,13,15,16,17}           = 10      7+10 = 17  OK
removed   {9,10,11,12}  intersect satisfied = {} = 0       numerator cannot rise  OK
after     {1,2,3,4,5,6,7,8,13,14,15,16,17}       = 13      7+6  = 13  OK
7/17 = 41.176 %   7/13 = 53.846 %   delta = +12.67 points
```
**Every figure reproduces. `0` of the removed four were satisfied. `R-F-02`'s characterisation —
*percentage rises, `0` obligations close* — is correct and honestly stated.**

**The membership is not.** See `R2-F-06`: the denominator is **`14`**, not `13`.

**Row-by-row, the `7` satisfied and `6` failing:** I checked each against `08_` §2 and the cited grounds.
`6`, `7`, `8`, `14` are satisfied on Boss acts (`CC-D-01`, `B3′`, `B6`, `8 of 8`) and stand.
`1` and `5` are correctly qualified. **`2` does not stand** — its qualification rests on
*"an independent party has attacked it"*, which `R2-F-01` falsifies. **Corrected: `6` satisfied of `14`
(42.9 %)** if condition `2`'s cure is withdrawn.

**Row `15` — I was asked to test the re-opening reasoning, and it holds.** *"A completed challenge
against a superseded package does not certify its successor"* is correct, is the reason the count cannot
rise merely because a challenge occurred, and runs against the executor's interest. **`08_` §4's
published account of its own wrong recount (`8` → `7`, wrong on rows `2`, `13`, `15`) is the strongest
single control in the package.** Attack FAILED; recorded as evidence.

---

## 5. `T4` — THE `18 / 4 / 0` READINESS MATRIX · **INTERNALLY EXACT · EXTERNALLY UNAUTHORISED**

**Membership extracted mechanically from `04_` §3 and checked against `X-01`…`X-22`:**
```
WRITABLE n=18 : X-01 X-02 X-03 X-04 X-05 X-06 X-07 X-10 X-11 X-12 X-13 X-14 X-15 X-18 X-19 X-20 X-21 X-22
GATED    n=4  : X-08 X-09 X-16 X-17
duplicates across classes: 0     missing from X-01..X-22: none     extra: none
POSITIVE CONTROL on the extractor: injected `X-99` -> extractor returns X-99   (it fires)
```
**`18 + 4 + 0 = 22`; each identifier exactly once. Arithmetic and membership are exact. Attack FAILED.**

- **`X-05` → `WRITABLE` on `B7-F-03`: correct.** `SC-BD-07`'s *"`3 of 3`, as one principle"* and
  *"NOT ruled: none"*, with §3 rejecting a split, defeat the test that produced `NOT ESTABLISHED`.
- **`X-08`/`X-09` → `GATED`: the residual does reach both rows.** `SC-SMT-01` attaches to `JT-05`, and
  `JT-05` governs **both** return rows. Grading one `GATED` and the other `WRITABLE` was the asymmetry
  `B7-F-05` identified. **Correct.**
- **`B5′` remains `NO BOSS RULING`.** The figure is `PROVISIONAL` and the package says so in every
  citation I checked. **No overclaim found.**

**`R2-F-09` — MODERATE (identifier collision).** The prefix `X-nn` names **three different populations**
in this package:

| Family | Population | `X-14` in it means |
|---|---|---|
| readiness rows (`04_` §3) | `X-01`…`X-22` | a scenario row, **`WRITABLE`** |
| external-authority items (`36_` §2) | `X-01`…`X-13` + `X-15` — **`X-14` is not a row** | — |
| SMEs Core obligations (resume state L93) | `CORE-04`, `-05`, `-06`, **`X-14`** | the AAS+ issuer act, **`OUTSTANDING`** |

A reader resolving `X-14` gets `WRITABLE` from one register and `OUTSTANDING` from another.

---

## 6. `T5` — THE `18` ROUND-1 FINDINGS · **MOSTLY REMEDIATED · TWO RECURRED**

I checked each of the `18` for *remediated* versus *recorded*. The package's declared method — *"`0`
prior artefacts modified; corrections published as superseding artefacts"* — is legitimate, and I
verified the corrected values were in fact published (`34_`, `26_`), not merely promised:

```
$ grep -rn '24. entries' <package>
34_PRETEST_CORR1_RECONCILED_MATRIX.md:90: | B7-F-15 | 25_ §1: manifest has "23 entries" | 24 entries, verifying 24 of 24 OK with a firing positive control |
```
**`16 of 18` are remediated in substance. `B7-F-15` and `B7-F-16` are remediated in text and
recurred in fact** (§2.2, §2.4) — the recurrence is `R2-F-03`/`R2-F-04`, not a separate finding.

**No `CONFIRMED` disposition was found to be a re-statement without a fix**, with one exception:

**`R2-F-10` — MODERATE.** `36_`'s *"`X-14` executed"* is booked across five artefacts (`03_`, `07_`,
`11_`, `12_`, `15_`, and `17_` §2) as a **substantive reversal** — one of only **`2`** wrong-session
conclusions the recovery claims to have corrected (`12_` §: *"Wrong-session conclusions **corrected**:
`2`"*). At primary text, `36_` never claimed a discharge:

> `36_` header: *"`CHECKPOINT E (part 3) — 14 ITEMS · X-14 EXECUTED · **AAS-V-02 NOT DISCHARGED**`"*
> `36_` §1 table: *"AAS+ issuer records **`0`** … **`AAS-V-02` NOT DISCHARGED — `HOLD` PRESERVED** …
> Self-discharge **`0`** … Vetoes **`7` canonical · `0` discharged**"*

What `36_` recorded as *executed* was **the issuer-evidence search**, described immediately beneath the
heading with three instruments and two positive controls. **The status before and after the
"reversal" is identical in every field.** `1` of the `2` claimed wrong-session corrections **corrects a
heading, not a conclusion**, and is presented as a status change.

---

## 7. `T6` — THE `12 ↔ 18 ↔ 10` BOUNDARY MAPPING · **DERIVED — AND IT WAS DERIVABLE**

`05_` §4 declines the `12 ↔ 10` leg: *"Mapping them requires a determination about which granularity
governs — **a scope act, not a transcription**."* **I derived it.** A *structural* crosswalk needs no
scope act; only choosing which granularity is **canonical for counting** does.

**`SA_CORR4_02` §5's `10` rows against the declared `12` (`XMC-H-01`…`12`), at primary text:**

| Contract row | Declared class reached |
|---|---|
| 1 Sales → Inventory | `1` |
| 2 Sales → Manufacturing | `2` |
| 3 Sales → Purchase / dropship | `3` |
| **4 Purchase → Inventory** | **NONE — no declared class, and no `XMC-H` row either** |
| 5 Inventory → Accounting | `5` |
| 6 Manufacturing → Inventory → Accounting | `4` **and** `5` (one row, two classes) |
| 7 AR/AP → Payment/Bank → Accounting | `6`, `7` **and** `8` (one row, three classes) |
| 8 Asset → Accounting | `9` |
| 9 Expense → Accounting | `10` |
| 10 Tax-related handoffs | `11` |
| — | **class `12` Close → all subledgers: reached by NO contract row** |

```
$ git show c91d5840:…/SA_CORR3_08_CROSS_MODULE_CONTRACT_PROOF.md | grep -oE 'XMC-H-[0-9]{2}' | sort -u | wc -l
18                                  # population verified at primary source, transcription in 05_ is faithful
$ … | sed -n '608p'
| **Total** | `XMC-H-01`…`XMC-H-18`, each exactly once | **18** |
```

**`R2-F-11` — MATERIAL.** The derivation is **`9` of `10` rows map; `1` maps to nothing; `11` of `12`
classes are reached; `1` is reached by nothing**, with `2` rows spanning multiple classes. Two facts fall
out that the package has never recorded:

1. **`Purchase → Inventory` is a `CONTRACT-GAP` flow that lies outside the declared `12` and outside the
   `18`-row `XMC-H` population entirely.** The package's headline is *"**`4`** gap-carrying handoffs
   outside the declared boundary set"*. That count is bounded to the `XMC-H` population and **does not
   say so**. Measured across both registers, there are **`5`** gap-carrying flows outside the declared
   set. `CORE-07` — which Boss made a **precondition to any `B4′` amendment** — is scoped to `4`.
2. **Declared class `12` (Close → all subledgers) was never covered by the contract proof at all.**

**The leg was derivable. What is not derivable without a Boss scope act is which granularity governs the
count — and that is a narrower statement than the one the package published.**

---

## 8. `T7` — `XMC-H-13/-14/-17/-18` AND THE `-15`/`-16` DISPOSITIONS

**Characterisations: CORRECT.** Each verified word-for-word at `SA_CORR3_08` lines 225–230
(`-13` *"MATCH, with a named hazard"*; `-14` *"MATCH on routing; **GAP on the object**"*; `-17` GAP;
`-18` GAP, *"the provenance reference does not exist"*). **Attack FAILED on this limb.**

**`-15`/`-16`: the dispositions survive — the instruction attached to them did not.**

`SA_CORR3_08` §2.6, verbatim:
> *"**`XMC-H-16` — the `N/A` is evidence-backed and its protection is not.** … A configuration change
> that breaks transfer neutrality **silently converts two `NOT APPLICABLE — EVIDENCE-BACKED` rows into
> ungoverned postings.** The `N/A` is correct today and is **not durable** — and **that belongs in the
> row, not a footnote**."*

**`R2-F-12` — MODERATE.** The caveat **is** preserved in `28_` (*"Caveat preserved: … a configuration
change could make `H-16` emit"*), which `03_` disposes **`A ADOPT`**. But the recovery's own superseding
registers drop it:

```
$ grep -rn 'XMC-H-15\|XMC-H-16\|`-15`\|`-16`' RECOVERY_2026_09_10/*.md
05_…:29 | `-15` | Quality hold → Accounting | — none — | **NOT APPLICABLE — EVIDENCE-BACKED** …
05_…:30 | `-16` | Internal transfer → Accounting | — none — | **NOT APPLICABLE — EVIDENCE-BACKED** |
10_…:18 | — NOT APPLICABLE — EVIDENCE-BACKED | 2 | YES — `-15`, `-16` | SA_CORR3_08 | YES |
POSITIVE CONTROL: the same grep shape fires 3 times on SA_CORR3_08 itself.
```
The primary source said the non-durability *"belongs in the row"*. **In `05_` §1 and `10_` §1 — the
recovery's canonical registers — it is in neither the row nor a footnote.** Consequence: **`4` outside is
a floor conditional on two configuration-defeasible `N/A`s, and is published as a fixed count.**

---

## 9. `T8` — `MF-01` / `MF-03` · **THE NEW GROUND IS CONTRADICTED AT PRIMARY SOURCE**

### 9.1 The evidence base does not contain the evidence

```
POPULATION: whole frozen tree at c91d5840 · UNIT: file · PATTERN: literal HX-nn · PATH SET: all paths

ID       TOTAL  OUTSIDE the challenged package
HX-01        6      3          HX-04   2   1        HX-07   2   1
HX-18        2      1          HX-27   1   1        HX-31   4   1
HX-24        8      0   <---   HX-25   4   0   <---
POSITIVE CONTROL: XMC-H-18 -> 1 file outside the package (the discriminating set is non-degenerate)

$ git ls-tree -r --name-only c91d5840 | grep -i 'INVENTORY_CROSS_MODULE_HANDOFF'
NOT ON TREE
```

**`R2-F-13` — MATERIAL (evidence base).** `06_` grounds **`MF-01`'s migration-event property** on
`HX-24` and **`MF-03`'s re-classification** on `HX-25`. **Neither identifier has any definition on the
baseline the auditor is told is *"the ONLY authorized B-7 Round-2 input"*.** The register that defines
them exists — I found it, off-baseline:

```
$ for r in $(git branch -r …); do git ls-tree -r --name-only $r | grep -i INVENTORY_CROSS_MODULE_HANDOFF; done
origin/design/inventory-final-solution-v1-2026-09-02-001:
  …/FINAL_SOLUTION/INVENTORY/V1_0/10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md   (HX-01 … HX-31, 31 rows)
```
**The frozen baseline is incomplete for a claim it carries.** `T8` was therefore not dischargeable
against the authorized baseline; I discharged it against primary source off-baseline and report both.

### 9.2 Tested against primary source, `MF-03`'s new ground fails

```
$ git show <design branch>:…/10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md | sed -n '45,47p'
| HX-23 | Migration → Inventory | Master data with a provenance reference | Cutover | … | PR-*, CF-* | INV-OWNED — provenance does not exist yet (GAP-FS-08) |
| HX-24 | Migration → Inventory / Accounting | Certified opening balances, quantity and value | Cutover | Human certification; cross-proof against the opening trial balance | OP-02, RP-05 | JOINT (JT-11, G-5) |
| HX-25 | Migration → Inventory | Movement history, or opening plus history from the cutover date | Cutover | Replay with a stable identity; reconcile | RP-03, RP-04 | INV-OWNED — depends on C-02 |
```

`06_` §2.2 asserts: *"`HX-25`/element `14` **describe replay as re-running a migration package**"*, and
answers its own discriminator — *"its own trigger, source state and destination state distinct from
`MF-01`/`MF-02`?"* — **NO**.

**Three falsifications:**

1. **`HX-25` does not describe re-running a migration package.** It carries *"movement history, or
   opening plus history from the cutover date"* — a **different payload** from `HX-24`'s certified
   opening balances.
2. **Every discriminator the primary register actually records separates the two rows**, and the
   executor tested only the one that returns the wanted answer. Trigger is shared (`Cutover`); **payload,
   guarantee, control references (`OP-02`/`RP-05` vs `RP-03`/`RP-04`) and ownership class
   (`JOINT (JT-11, G-5)` vs `INV-OWNED`, per the register's own ownership table) all differ.**
3. **The unbuilt control was relocated, not removed.** `B7-F-10`'s defect was that `MF-03`'s exclusion
   rested on `RT-E15-05`, resting on unbuilt element `15`. **`HX-25`'s own stated guarantee is
   *"Replay with a stable identity"* — element `15`.** And element `14` (provenance) belongs at primary
   source to **`HX-23`**, not `HX-25`. `SA_CORR3_08` line 230 places both in one clause:
   *"**`14` and `15` `NOT SUPPLIABLE`**"*.

**`06_` §2.2's closing claim — *"the ground is now evidence rather than an unbuilt control"* — is
falsified. `MF-03`'s `EXECUTION MODE` classification is NOT ESTABLISHED on the cited ground.**

### 9.3 `MF-01` — the narrowing survives, with an unstated precondition

`B7-F-09`'s disproof of `CC-F-11`'s universal clause is **sound**: under `Standard`, value is a policy
attribute of the product rather than a function of a movement's carried cost, and `SA_CORR3_03` L178
corroborates the mechanism. **`CORE-06` (the counterpart account) is the correct residue.** Attack FAILED.

**Recorded, unmeasured:** the asymmetry between `Standard` and `Average`/`FIFO` holds **only if the
product standard cost is itself established independently of the migration**. In a cutover the standard
cost is itself migrated data. `06_` §1 does not state or test that precondition.

---

## 10. `T9` — `AAS-V-02` · **RE-RUN INDEPENDENTLY · EXECUTOR UPHELD**

```
POPULATION: STATE03_MIGRATION_FACTORY/** at c91d5840 · UNIT: file · PATH SET size: 779 files

INSTRUMENT A  'authored by …AAS+' | 'AAS+ …(authored|issued|has performed the discharge)'   -> 4
INSTRUMENT B  line-level 'AAS+ …(discharge|concurrence)…(received|arrived|executed|given)'
              minus negations                                                                -> 0
INSTRUMENT C  header names AAS+ as issuing body  '^(Issued by|Author|From):.*AAS'            -> 0

POSITIVE CONTROL 1  files mentioning AAS+ at all                                             -> 114
POSITIVE CONTROL 2  instrument A's shape applied to 'SMEs Core'                              -> 0   ** FAILED **
SYNTHETIC INJECTION  a file containing 'Issued by: AAS+' / 'AAS+ has performed the discharge act'
                     instrument A -> fires    instrument C -> fires
```

**Instrument A's `4` hits, enumerated and inspected — not reported as a count:**

| File | What it is |
|---|---|
| `07_PRETEST_VETO_CANONICAL_REGISTER.md:76` | a hypothetical (*"then a named, in-force, AAS+-issued … veto"*) |
| `36_…EXTERNAL_AUTHORITY_ITEMS.md:21,34` | the description of instrument 2, and the `SC-42` quotation |
| `07_AAS_V02_ISSUER_EVIDENCE_STATUS.md:33,59` | the executor's own statement of the zero |
| `SC-42_POH_D06_AASPLUS_POST_COLLISION_AUTHORITY_STATUS.md:17,19` | *"AAS+ input arrived since `093585d0`? — **NO — `0`**"* |

**`0` AAS+-authored records. `AAS-V-02` = NOT DISCHARGED. Vetoes `7` · `0` discharged.
`X-14`/`X-03` OUTSTANDING. The executor's handling is CORRECT and the attack FAILED.**

**Positive control 2 failed** — the corpus uses no *"authored by X"* convention for any party, so that
control cannot discriminate. **Reported as my own instrument failure (§12) and replaced by the synthetic
injection, which fires.** The zeros are real absences, not broken predicates.

**Recorded:** three parties have now published three different denominators for the same firing control
— B-7 R1 `103`, `36_` `104`, this session `114`. **None of the three declared the same `PATH SET`.**
Mine is declared above.

---

## 11. `T10`, `T11`, `T12`, `T13`

### 11.1 `T10` — `E2E-04` phase separation **CONCEALS** rather than cures

`B7-F-11` is confirmed at primary text, and I read it there rather than in the summary:
```
$ … SC-03_SMT_FIRST_LINE_CHALLENGE_REGISTER.md:21
**And this is not independent assurance.** It is **internal first-line challenge by specialist role**
$ … SC-04_VETO_AUTHORITY_HANDOFF_REGISTER.md:94
`SC-03` is internal first-line challenge by specialist role. It is not independent assurance…
```
**Latest-artefact test:** the only later candidate is
`SAAS_CELL_ARCHITECTURE/04_BOSS_DECISION_SMT_GRC_ASSURANCE_STRUCTURE_… (2026-09-06)`; `SC-03`/`SC-04`
are `2026-09-10` and later. **Nothing re-designates SMT as independent.**

**The re-grade act remains routed to a party primary text says is not independent, and its parent
condition has left the exit denominator.** The non-independence is unchanged; what changed is that it no
longer registers as a failing exit condition. **That is concealment in the instrument — the same defect
as `R2-F-06`, and the second instance of one root cause.**

### 11.2 `T11` — stale / superseded evidence · **A SUPERSEDING SECTION IS ITSELF SILENTLY SUPERSEDED**

`10_PRETEST_CANONICAL_RECOVERED_MATRIX.md` opens *"**ALL DENOMINATORS RESTATED WITH NAMED MEMBERSHIP**"*
and closes *"**`0` denominators without named membership**"*. Measured against its own file:

| `10_` row | States | Measured |
|---|---|---|
| FD blockers | **`3`** | `10_` §2 itself lists `3` **"plus `2` new"** = `5`; `14_`, `15_`, `17_`, resume state all say **`5`** |
| SMEs Core obligations | `4` — *"`CORE-04`…`-06`, `CORE-05` held"* | the named range is **`3` members**; resume state L55 names `{04,05,06,07}`; resume state L93 names `{04,05,06,X-14}` — **three memberships for one count** |
| External-authority items | `14` — *"`X-01`…`X-14`"* | actual set is **`X-01`…`X-13` + `X-15`**; `X-14` is **not a register row**; the stated range adds a non-member and drops a member |
| `IR` flows `20` / `AR` flows `30` | *"Membership named? **YES**"* | **no file in the frozen package enumerates `10`+ distinct `IR-nn`;** one enumerates `10` distinct `AR-nn` against a declared `30`. **POSITIVE CONTROL: the same instrument finds `PTX-01`…`-11` enumerated in two files** — it fires |
| Exit conditions | `7 of 17` | superseded by `7 / 13` in `14_`; **`10_` carries no supersession marker** (`grep -niE 'supersed\|stale\|pre-ruling' 10_… -> NONE`) |

**`R2-F-14` — MATERIAL.** The file that exists to prove every denominator has named membership publishes
**`4` wrong or unsupported memberships and `1` self-contradicting count**, and its closing assertion
*"`0` denominators without named membership"* is false on its own evidence.

**And the headline defect of this session:**

```
22_ §4 / 23_          Open Boss decisions:  7 -> 1     (POH-D-02)
34_ §2                "That count was low."  1 -> 3    (POH-D-02, SC-SMT-01, BOSS-CORR1-01)
37_ §, resume L230    Boss decisions open:   3
RECOVERY 10_, 14_ §7, 12_, and 17_ §7 handed to me:   1
```
```
$ grep -rn 'BOSS-CORR1-01' RECOVERY_2026_09_10/
(no output — 0 occurrences in the entire recovery package)
$ grep -rn 'SC-SMT-01' RECOVERY_2026_09_10/14_…md
116: | SC-SMT-01 | existing open Boss-owned obligation; do NOT re-ask | carried, NOT re-asked …
      It gates X-08/X-09 — recorded, not escalated |
```

**`R2-F-15` — MATERIAL.** **The recovery reverts, without addressing it, a correction a prior round made
against its own interest, on the count reserved to the Boss.** Neither `SC-SMT-01` nor `BOSS-CORR1-01` is
recorded anywhere as closed. `SC-SMT-01` is expressly still open and merely *"not escalated"*.
**`BOSS-CORR1-01` — the boundary-denominator escalation on which `28_` §4 says the per-boundary
applicability declaration is `STILL BLOCKED` — appears `0` times in the recovery package.**

The resume state does carry all three at line 260 (*"Boss action awaiting in parallel and not blocking
Round 2"*) — **so the items are preserved in prose and dropped from the count**, exactly as with the
`E2E-04` `G` limb. **The Round-2 prompt then hands the auditor *"`1` Boss decision open"*.**

**`R2-F-16` — MODERATE.** The resume state's section headed **"`## Superseding state — these figures
replace the ones above`"** is itself silently replaced by the later recovery section, with no marker.
Its `7 of 17` (`7 of 14` Pre-Test-owned; `3` re-placed) is a **fourth** exit denominator in the frozen
package — `17`, `14`, `13` and the corrected `14` of `R2-F-06` — and `14_` presents `17 → 13` as a single
move without ever acknowledging that a `17 → 14` re-placement already existed.

### 11.3 `T12` — the `3` circular gate defects · **THE COUNT HAS TWO INCOMPATIBLE MEMBERSHIPS**

```
$ grep -n 'CGD-0\|CIRCULAR GATE DEFECT\|not strictly circular\|not a defect' 09_…md
 3: # `3 CIRCULAR GATE DEFECTS CONFIRMED …`
44: ### 2.1 `CGD-01` — condition `9`
54: ### 2.2 `CGD-02` — condition `10`          <- §2.2 verdict: "Not strictly circular"
63: ### 2.3 `CGD-03` — condition `12`
71: ### 2.4 Condition `11` — a **split** case, **not a defect**
113: | **CIRCULAR GATE DEFECT** | **`9`, `12`** and `11`'s `D` limb |
126: > **`3` CIRCULAR GATE DEFECTS** (`9`, `12`, `11`-`D`)
```

**`R2-F-17` — MODERATE.** One file publishes two mutually exclusive membership sets for one count of
`3`: the identifiers `CGD-01/-02/-03` = `{9, 10, 12}`, and §4.1/§5 = `{9, 12, 11-D}`. **Each set contains
a member the same file denies** (§2.2 says `10` is *"not strictly circular"*; §2.4 says `11` is
*"not a defect"*). `14_` §5 then propagates the identifier set as *"`3` → `0` … `CGD-01`/`-02`/`-03`
resolved by re-placement"*.

**Does re-placement resolve or relocate?** For `EC-04` and the `48` items, **genuinely resolve** — the
receiving gates (State, Build/Test) are downstream of the build the circularity required, and I found no
new circularity there. **Attack FAILED on that limb.** For `E2E-04`'s `D` limb, **relocate**: it moves to
*"Functional Design Exit"*, a gate that Pre-Test exit itself authorises entry to. That is not a loop, but
it converts a gate-**entry** control into a gate-**exit** control, and `09_` §4.1's own classification
calls that limb circular while §2.4 calls it not a defect.

### 11.4 `T13` — new material contradictions

**`B7-F-08` is open and correctly recorded — attack FAILED.** `B9′` admits `MF-01`/`MF-02` into `IR`
(`18→20`) and `AR` (`29→30`); `B4′` excludes `XMC-H-18`; the admitted flows travel on the excluded
handoff. Verified at `SA_CORR3_08` line 230 and `05_` §3. **It is not the only one.** New in this round:

- **`R2-F-15`** — the open-Boss-decision count reverted `3 → 1` with `0` closures recorded.
- **`R2-F-06`** — the exit denominator drops a live Pre-Test obligation.
- **`R2-F-11`** — a fifth gap-carrying flow outside the declared set, and declared class `12` uncovered.
- **`R2-F-13`** — `MF-03`'s ground contradicted by the register it cites.
- **`R2-F-01`** — the independence the `B-7` apparatus rests on is contradicted by the git record.

---

## 12. WHAT I COULD NOT TEST, AND WHY · MY OWN INSTRUMENT FAILURES

**Could not test — `4`:**

| # | Claim | Why not |
|---:|---|---|
| 1 | **`R-D-01`'s terms** | no ruling artefact exists on the frozen tree (`R2-F-08`). I can test the placement *analysis*; I cannot test what Boss actually ruled |
| 2 | **`HX-24`/`HX-25` as they stood at freeze** | the defining register is not on the baseline (`R2-F-13`). I tested against the off-baseline `design/inventory-final-solution-v1-…` copy and say so |
| 3 | **`IR`/`AR` reconciled counts `14` / `15`** | the member enumerations are not in the package; a count whose membership is unpublished cannot be re-derived, only re-read |
| 4 | **Whether `Standard` costs are themselves migrated** (§9.3) | requires the costing design package, off-baseline |

**My own instrument failures — `3`, reported as required:**

1. **`git archive … --strip-components=8`** — wrong depth (`6` was correct). It produced an **empty
   extraction and exit code `0`**: a silent zero indistinguishable from an empty directory. Caught only
   because I counted the extracted files. Re-run corrected.
2. **Branch-exclusion comparison `[ "$r" = "${CB#origin/}" ]`** — compared `origin/x` against `x`, so the
   canonical branch was not excluded from the collision sweep and appeared in its own result. Corrected
   before the count was taken.
3. **`sed`-based membership extraction from `04_` §3** — the pattern did not match the backticked table
   cells and returned `1` identifier per class instead of `18`/`4`. Replaced by a line-addressed
   extractor **with a synthetic `X-99` injection control** before any figure was published.

---

## 13. FINDINGS

| ID | Finding | Severity |
|---|---|---|
| **`R2-F-01`** | The repository record shows B-7 Round 1 was executed by the same model family as the audited party; the appointed independent vendor is evidenced nowhere. Exit condition `2`'s cure depends on it | **MATERIAL** |
| **`R2-F-06`** | Condition `11` retains an outstanding, expressly Pre-Test-placed `G`-limb obligation and was removed from the exit denominator. Correct denominator `14`, not `13`; `50.0 %`, not `53.8 %` | **MATERIAL** |
| **`R2-F-08`** | `R-D-01` has no ruling artefact. The authority producing the headline `7 / 13` exists only as a session id in the challenged party's own application file | **MATERIAL** |
| **`R2-F-11`** | The `12 ↔ 10` leg **is** derivable structurally. Derived: `Purchase → Inventory` is a fifth gap-carrying flow outside the declared set, and declared class `12` is covered by no contract row | **MATERIAL** |
| **`R2-F-13`** | `MF-03`'s replacement ground is contradicted at primary source: `HX-25` is a distinct row by payload, guarantee, controls and ownership, and its own guarantee is the unbuilt element `15`. The defining register is not on the baseline | **MATERIAL** |
| **`R2-F-14`** | `10_` publishes `4` wrong or unsupported memberships and `1` self-contradicting count, and asserts *"`0` denominators without named membership"* | **MATERIAL** |
| **`R2-F-15`** | Open Boss decisions reverted `3 → 1` with `0` closures recorded; `BOSS-CORR1-01` appears `0` times in the recovery package; the Round-2 prompt hands the auditor `1` | **MATERIAL** |
| **`R2-F-03`** | The Round-2 handoff prompt states `14` manifest entries; there are `15` — `B7-F-15`'s defect, in the prompt that cites it | **MODERATE** |
| **`R2-F-04`** | `15_` §1's inventory reproduces `B7-F-16` exactly; the preventive control declared at `34_` did not hold one commit later | **MODERATE** |
| **`R2-F-05`** | `3` of `4` re-placements rest on external authority; `E2E-04`'s rests on a limb split the executor invented, presented in the same undifferentiated table | **MODERATE** |
| **`R2-F-07`** | `8C-CLARIFICATION-01` cl. 5 (`NO DUMPING`) is the direct control on forward movement and is never addressed; `E2E-04`'s `D` limb is a design obligation with no execution-dependency evidence | **MODERATE** |
| **`R2-F-09`** | `X-nn` names three different populations; `X-14` resolves to `WRITABLE` in one register and `OUTSTANDING` in another | **MODERATE** |
| **`R2-F-10`** | `1` of the `2` claimed wrong-session conclusion corrections corrects a heading, not a conclusion; every status field is identical before and after | **MODERATE** |
| **`R2-F-12`** | The primary source's instruction that `-15`/`-16`'s non-durability *"belongs in the row"* is dropped from `05_` and `10_`; *"`4` outside"* is a floor published as a fixed count | **MODERATE** |
| **`R2-F-16`** | A section headed *"these figures replace the ones above"* is itself silently superseded; a fourth exit denominator (`7 of 14`) is live and unreconciled | **MODERATE** |
| **`R2-F-17`** | `09_` publishes two incompatible membership sets for its count of `3` circular gate defects, each containing a member the same file denies | **MODERATE** |
| **`R2-F-02`** | The SHA the package's designated carrier names (`fec7c49b`) differs from the Boss-handed authoritative SHA (`c91d5840`); content identical | **MINOR** |

**`7` MATERIAL · `9` MODERATE · `1` MINOR = `17` findings.**
*(`R2-F-01`…`R2-F-17`, each numbered once; verified `$ grep -oE 'R2-F-[0-9]{2}' <this file> | sort -u | wc -l`.)*

---

## 14. WHAT THE EXECUTOR GOT RIGHT — recorded because refusals are evidence

| | |
|---|---|
| Manifest integrity | `5` manifests, `123` entries, **`0` failures**; coverage complete by set-difference |
| Canonical artefacts | **`0`** modified by the recovery arc; **`0`** changes outside the package path |
| `R-F-01` collision correction | sound; **`0`** competing writers reproduced with a firing control |
| `AAS-V-02` | **NOT DISCHARGED** — re-measured independently in three instrument shapes with a synthetic injection control |
| `18 / 4 / 0` | arithmetic and membership exact; `X-05`/`X-08`/`X-09` moves correct on primary text; `PROVISIONAL` honestly carried |
| `7 / 17` recount | reproduces exactly; **`08_` §4's published account of its own wrong recount is the strongest control in the package** |
| Row `15` re-opening | *"a completed challenge against a superseded package does not certify its successor"* — correct, and against the executor's interest |
| `B7-F-09` narrowing | correct; `CORE-06` is the right residue |
| `R-F-02` | the *"instrument correction, not improvement"* caveat is stated plainly and repeatedly, and is honest |
| `B7-F-08` | correctly recorded as an open material contradiction rather than closed |
| `12 ↔ 10` | recorded as **owed** rather than asserted — the right refusal, on a reason narrower than stated |

---

## 15. TERMINAL

> ## `VERDICT: HOLD`

| | |
|---|---|
| Pre-Test exit | **`HOLD` — and the published `7 / 13` is not the correct instrument** |
| Corrected exit position | **`7` of `14`** (`50.0 %`), or **`6` of `14`** if condition `2`'s independence cure is withdrawn per `R2-F-01` |
| Open Boss decisions | **`3`, not `1`** — `POH-D-02` · `SC-SMT-01` · `BOSS-CORR1-01` |
| Gap-carrying flows outside the declared set | **`5`, not `4`** — and `4` is itself a floor (`R2-F-12`) |
| `EC-04` · `EC-07` · verification · `E2E-04` | **`0/3` · `0/2` · `0 PASS · 48 HOLD` · `NOT TRAVERSABLE`** — unchanged, and I found no attempt to change them |
| Vetoes | **`7` · `0` discharged** · `AAS-V-02` **NOT DISCHARGED** — independently reproduced |
| `MF-03` classification | **NOT ESTABLISHED on the cited ground** |
| `R-D-01` | **UNEVIDENCED as an authority act** |
| Functional Design | **NOT AUTHORIZED** |
| This verdict as an `EC-07` pass | **NO** — and `EC-07` is Module + State placed, not Pre-Test |
| Independence of this challenge | **NOT SATISFIED** — §0 |

**`0` canonical writes. `0` evidence waived. `0` `PASS` declared. `0` re-grades performed.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Falsify before Accept.
**Boss is the sole Final Approver.**
