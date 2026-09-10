# B-7 INDEPENDENT CHALLENGE — VERDICT

# `VERDICT: HOLD`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-INDEPENDENT-001]`
Channel: **INDEPENDENT REVIEW — this is NOT the challenged branch**
Challenged branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` — **READ ONLY, 0 writes**
Frozen baseline read: **`c94839e8815e3796e499848a4bd45e595e25fc94`** (package content freeze `8af573f2`)
Boss: **SOLE FINAL APPROVER**

> **`0` writes to the challenged branch · `0` challenged artefacts modified · `0` re-grades performed ·
> `0` PASS manufactured. The executor cannot convert this HOLD into a PASS.**

---

## 0. Intake — baseline and integrity verified before any target

| Check | Command | Result |
|---|---|---|
| Frozen head resolves | `git rev-parse origin/architecture/...-2026-09-10-001` | **`c94839e8`** — matches the SHA supplied |
| Content freeze lineage | `git log -1 8af573f2` | **CHECKPOINT G–J commit — confirmed** |
| Manifest verification | `shasum -a 256 -c 24_PRETEST_POST_RULING_MANIFEST_SHA256.txt` | **`24 of 24 OK`** |
| **Positive control** | appended one byte to `01_`, re-ran the checker | **`01_…: FAILED`** — the checker fires; restored, `24 OK` |
| Manifest set identity | `diff <(sort CORRECTIVE_PACKAGE_MANIFEST…) <(sort 24_…)` | **identical content sets** |

**The package is intact and the baseline is the one I was told to read.**

---

## 1. Verdict

> # `HOLD`

**Not `PASS`:** the mandatory first target does not reproduce (`T1`), the `T3` mapping I executed returns
an adverse result the package never measured, and **two of the eight exit conditions counted `SATISFIED`
are not established on the evidence available** (§4).

**Not `FAIL`:** the package's terminal posture is correct and conservative. `HOLD PRE-TEST EXIT`,
`0 of 48`, `EC-04 0/3`, `EC-07 0/2`, `E2E-04 NOT TRAVERSABLE`, `7` vetoes with `0` discharged, Functional
Design **not** authorized — every one of these reproduced. **Nothing I found manufactures a PASS, and
several of the executor's refusals were correct where a permissive reading was available.**

**`12 of 12` targets carry a recorded falsification attempt. `6` attempts succeeded, `6` failed.**

---

## 2. Findings

### `T1` — THE READINESS SPLIT `19 / 2 / 1` — **MANDATORY, FIRST** — **FALSIFIED**

**Method.** Re-derived per cell from primary text, never from the executor's tables. Reproduced
`SA_CORR5_10` §4 mechanically, then tested each gating decision at its own Boss ruling record.

**Command + output — the pre-derivation baseline, independently reproduced:**

```
$ awk '/^\| # \| Scenario \| SEM/,/^### 4.1/' SA_CORR5_10_…md | grep -E '^\| *[0-9]+ \|' \
  | awk -F'|' '{p=$14; gsub(/[ *`]/,"",p); print p}' | sort | uniq -c
  12 GATED
  10 WRITABLE
$ # cell totals, dimensions $4..$12
  TOTAL B CELLS = 13     TOTAL CELLS = 198     ⇒ C = 185
$ # S markers: rows 1 2 3 4 5 6 9 13 19  → TOTAL_S = 9
```

**`10 WRITABLE / 12 GATED`, `198` cells, `185 C · 13 B · 9 S · 0 G` — reproduced exactly.
Correction `C4` is confirmed: `S` is an annotation inside a `C` or `B` cell, not a fourth partition.**

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-03`** | **`β5` (`X-05`, partial receipt) is recorded `NOT ESTABLISHED` on a test the ruling's own structure defeats.** `CC-F-01` argues `F2` was ruled `3 of 3` with its members never enumerated. But **`SC-BD-07` §2 rules `F2` as `BLOCK — ON ALL THREE MEMBERS, RULED ONCE AS A PRINCIPLE`**, its header records **`NOT ruled — see §8: none`**, and **§3 expressly rejects *"split the ruling across the three members."*** The **governing** register — `SA17_…FINAL_CONTROLLED_V2` §2d, which correction `C2` itself designates and which I confirmed is the latest generation by commit date (`2026-09-09 22:38`, later than the CORR5 generation's `19:51`) — maps **`F2` control defaults → `E2E-01`; rows 5, 10**. Row 5's membership is therefore carried by the governing register, not merely *"consistent"*. **`β5` should be `WRITABLE`.** The executor erred **conservative**. | **MATERIAL** |
| **`B7-F-04`** | **`β8` (`X-09`, sales return) is graded `WRITABLE` while its own row records an open Boss decision.** `02_` §3 row `β8` carries the open dependency ***"`Average`-costing residual → Boss"***. At primary text that is **`SC-SMT-01`**, disposition **`BOSS-ONLY DECISION`**: *"`JT-05` → original cost leaves a residual under `Average` costing that nothing in the recommendation places … The recommendation is **incomplete as written**"*, and **`SC-BD-05` §8.1** names it *"a **live obligation, not a closed condition** … **not** discharged by this ruling."* `SC-11` §6 obligation `3` carries it, owner **Boss**, and `PT-11` line 109 carries it **`OPEN`**. Since `BD-ACC-03B` puts `Average` in scope by Product Category, **the expected value of a return reversal is not derivable for an `Average`-costed category** — which contradicts `02_` §3.1's own qualification two lines below the grade: ***"Expected values must be taken from the ruling text."*** | **MATERIAL** |
| **`B7-F-05`** | **`β7` (`X-08`, purchase return) carries a resolved dependency and omits its live one.** `β7`'s listed dependency is *"return basis `PENDING`"* — which `SA_CORR5_10` row 8 states **is `JT-05` seen from Inventory**, i.e. closed by the very ruling on the same row. Meanwhile `SC-SMT-01` attaches to **`JT-05`**, which governs **both** return rows; the `Average` residual is recorded on `β8` only. **No basis is given for the asymmetry, and one of the two rows is wrong either way.** | **MATERIAL** |
| **`B7-F-06`** | **`19` is not reproducible as a membership.** My per-cell derivation moves `β5` **into** `WRITABLE` and takes `β8` (and, on `B7-F-05`, `β7`) **out** of it. The errors run in **opposite directions**, so a total near `19` can survive while the membership underneath it is wrong in at least two cells. `T1` asked for a per-cell re-derivation precisely because the total is not the claim. **`B5′` remains `NO RULING — PROVISIONAL` (`22_` §7), so no authority stands behind `19`.** | **MATERIAL** |

**Falsification attempts that FAILED — the executor is right on these:**

- **`JT-04`/`JT-05` are genuinely ruled.** `SC-BD-05`: *"`JT-04 = THE BUSINESS EVENT (PHYSICAL MOVEMENT) · JT-05 = ORIGINAL COST`"*, **`2 of 2`**, `NOT ruled: none`. §7 states the ruling **fixes expected values** for *"the 10 of 22 scenarios carrying `expected value pending`"* — which answers `T1`'s hypothesis in the executor's favour for rows 1–4, 6.
- **`X-16`/`X-17` correctly remain `GATED`** — see `T2`.
- **`β12` (`X-18`) is correctly `WRITABLE`**: `SC-BD-02` rules `XMC-D-02` (`2 of 2`) and `SC-BD-08` rules `XMC-D-01` (`1 of 1`, *"leaves the Boss decision list entirely"*).

---

### `T2` — BOSS RULING IMPLEMENTATION (`22_`), especially `X-16`/`X-17` — **ATTEMPT FAILED**

**Tested for under-claiming.** `22_` §4.1 holds `X-16`/`X-17` `GATED` after `POH-D-01` was ruled, and
names `B-6`'s four components. Verified at primary text: `POH-D-06` **RULED** (`SC-BD-06`), `POH-D-01`
**RULED**, `POH-D-02` **WITHHELD** — *"Thai statutory authority is still required"*, excluded from `B1` —
and **veto limb 2 OUTSTANDING**, which `SC-42` §2 records as *"cannot be discharged in either direction as
written"* with **AAS+ issuer authority** and *"SMEs Core does not draft it."*

**Two of four components remain and one is undischargeable as worded. Holding the rows `GATED` is
correct, not conservative posturing.** `17_` §3 supplies the four required re-wording properties as input
to the issuer and **declines to draft the wording** — the correct refusal.

---

### `T3` — THE `12`-BOUNDARY DECLARATION — **FALSIFIED · THE MAPPING IS ADVERSE**

`CC-F-13` records that `12 ↔ 18 ↔ 10` *"is now derivable and has not been derived."* **I derived it.**

**Command + output** (population `XMC-H-01…18`, the register's own *"each exactly once"*; unit = handoff
row; map target = the `12` classes declared at `22_` §1):

```
XMC-H-01  Sales → Inventory                            class 1
XMC-H-02  Sales → Manufacturing                        class 2
XMC-H-03  Sales → Purchase (dropship / MTO)            class 3
XMC-H-04  Manufacturing → Inventory                    class 4
XMC-H-05  Inventory → Accounting                       class 5
XMC-H-06  Sales → AR / Accounting                      class 6
XMC-H-07  Purchase → AP / Accounting                   class 7
XMC-H-08  Payment → Bank / Accounting                  class 8
XMC-H-09  Asset → Accounting                           class 9
XMC-H-10  Expense → Accounting                         class 10
XMC-H-11  Tax → Accounting / reporting                 class 11
XMC-H-12  Close → all subledgers                       class 12
XMC-H-13  Inventory → Sales and Purchase               — NONE —
XMC-H-14  Quality → Inventory                          — NONE —
XMC-H-15  Quality hold → Accounting                    — NONE —
XMC-H-16  Internal transfer → Accounting               — NONE —
XMC-H-17  Service / Project performance → Accounting   — NONE —
XMC-H-18  Migration / replay → Inventory and Accounting — NONE —
```

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-07`** | **The declared `12` is exactly `XMC-H-01…12` and stops there.** `6 of 18` map to no declared class. Two of the six (`XMC-H-15`, `-16`) are `NOT APPLICABLE — EVIDENCE-BACKED`. **The remaining `4` — `XMC-H-13` Inventory→Sales/Purchase, `-14` Quality→Inventory, `-17` Service/Project→Accounting, `-18` Migration/replay→Inventory and Accounting — each carry `HOLD — EXACT GAP` in `SA_CORR3_08` and fall entirely outside the declared boundary set.** Since `SC-BD-02` §7 fixes **the Pre-Test Matrix element-contract denominator** at those `12`, these four gap-carrying handoffs are outside the contracted and tested surface. **The declaration closes the denominator question and leaves a measured `4`-row coverage hole that the package never measured.** | **MATERIAL** |
| **`B7-F-08`** | **Two rulings applied in the same register are in tension, and the interaction was not tested.** `B9′` **admits** `MF-01`/`MF-02` into `IR` (`18→20`) and `AR` (`29→30`); `B4′` **fixes** the contract and Pre-Test denominator at `12` boundaries that **exclude `XMC-H-18`, the migration/replay handoff those very flows travel on** — the row `SA_CORR3_08` records as *"elements 14 and 15 `NOT SUPPLIABLE`"*. `22_` applies both rulings and never puts them against each other. | **MATERIAL** |

**What I did NOT do:** I did not test whether the declared `12` is the *right* set. Declaring it is a Boss
authority act and is not falsifiable by me. **I tested only its coverage against the tested population.**

---

### `T4` — VETO COUNT `= 7` — **ATTEMPT FAILED · A/B/C EACH TESTED INDEPENDENTLY**

**Test A — is the manufacturing veto `AAS-V-03` under another name?** Re-measured in two command shapes:

```
$ for t in BLK-07 BLK-08 manufactur machine overhead AAS-V-01 AAS-V-02 AAS-V-03 CF-V-01 CF-V-02 RC-V-01
  ; do grep -o -i -- "$t" SC-04_VETO_AUTHORITY_HANDOFF_REGISTER.md | wc -l ; done
  BLK-07 0   BLK-08 0   manufactur 0   machine 0   overhead 0
  AAS-V-01 3  AAS-V-02 3  AAS-V-03 4  CF-V-01 3  CF-V-02 3  RC-V-01 4
$ awk 'BEGIN{IGNORECASE=1}…' SC-04…   →   BLK-07/08=0 machine=0 manufactur=0
```

**The four zeros reproduce with six positive controls firing in the same file, in two instrument shapes.**
`AAS-V-03`'s limbs are `F6` (`MTI-D-04`) and `F1` COGS; the manufacturing veto's are `BLK-07` and machine
cost. **Four limbs, four subjects. `A` disproved.**

**Test B — declared exclusion?** `SC-04` §1 names its exclusions (`MNT-V-01` a verdict; `DB-V-01`/`-02`
substrings). The manufacturing veto is not named. **`B` disproved.**

**Test C — the authority question.** `SC-19` §6 verbatim, confirmed: *"**Vetoes remain 6 in force · 0
discharged · 0 self-discharged.**"* **The executor did NOT override it.** `07_` §4 records
***"Carried figure: `6`, as reported — this round does NOT renumber"***, on the stated ground that
enlarging a veto population is an issuer act. It supplied `CLASS C` as a **determination** and routed the
renumbering to `B3`. **Boss then ratified at `B3′`.** That is determination → ratification in the correct
order, and it is the opposite of an override.

---

### `T5` — `AAS-V-02` / `CC-F-14` — **ATTEMPT FAILED · THE EXECUTOR'S ZERO IS CORRECT**

```
$ grep -rliE 'authored by.*AAS\+|AAS\+ (record|response|concurrence) (received|arrived)' <factory tree>
  0
$ grep -rl 'AAS+' <factory tree> | wc -l        # positive control
  103
```

**`0` AAS+-authored records against a `103`-file control that fires.** `SC-42` §1 at primary text:
*"AAS+ input arrived since `093585d0`? — **NO — `0`.**"*

**`CC-F-14` is correct and its handling is the right one.** Boss ratification is **given**; the issuer's
discharge act is **unevidenced**; the executor applied it as a **standing ratification that takes effect on
the issuer's act** rather than recording a discharge. Recording `AAS-V-02` discharged would have asserted
an act by an external authority that no evidence shows occurred. **`7` canonical, `0` discharged — confirmed.**

---

### `T6` — THE `48` DENOMINATOR — **ATTEMPT LARGELY FAILED · ONE DEFECT FOUND**

**All four sub-populations re-derived from primary source, not from `11_`:**

```
$ grep -oE 'E2E-[0-9]{2}' SA15_…FINAL_CONTROLLED_V2.md | sort -u | wc -l     → 18
$ grep -rhoE 'PT-S-[0-9]{2}' PHASE_PRETEST/ | sort -u | wc -l                → 7
$ grep -rhoE 'PT-C-[0-9]{2}' PHASE_PRETEST/ | sort -u                        → PT-C-01
$ grep -oE '\bX-[0-9]{2}\b' PT12_…MATRIX.md | sort -u | wc -l                → 22
                                                       22 + 18 + 7 + 1 = 48 ✔
```

**Every member is enumerated, not asserted. `CC-F-09` discloses the split (`40` authority-declared + `8`
session-added) and publishes the ratio in both halves — which is the correct treatment of a mixed
denominator.**

**I then re-ran the measurements the `8` additions rest on, at the declared corpus:**

```
POPULATION: 6 declared dirs · UNIT: one .md file with ≥1 match · CORPUS: 192 .md  (reproduced exactly)
dropship 49 (ctrl)   idempot 57   stale 30   metering 12   VAT 8   WHT 4
make-to-stock 0   partial payment 0   partial invoic 1   out-of-order 1   event order 0
```

**Every figure in `PT-01` §5.1 reproduces exactly — including all five zeros the `CLASS 2` additions rest
on.** The refusal half (`11` candidates tested, `10` refused as already covered, `1` routed with its
reason) is real and is the half a coverage review usually omits. **The `8` additions do not inflate the
denominator.**

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-14`** | **`PT-S-01`'s evidence line is false as written, and its path set is stated as a description.** The claim is *"`VAT` `0` and `WHT` `0` in **all three scenario registers**"*. The three are **never named**. Measured: `SA15_…V2` `0/0`, `SA17_…V2` `0/0`, `SA15_…CORR5` `0/0` — but **`SA_CORR5_10`, the register that defines the `X-01…X-22` population the `48` is built on, returns `VAT=2` and `WHT=2`** (dropship control fires `1` in the same file). Under the most natural membership the stated zero is not zero. **`PT-S-01`'s substance survives** — the `VAT`/`WHT` occurrences there are statutory period references inside `S` markers, not a scenario carrying a tax determination — **but the published measurement does not.** | **MODERATE** |

---

### `T7` — MIGRATION ADMISSION (`B9′`) — **FALSIFIED ON BOTH LIMBS PUT TO ME**

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-09`** | **`CC-F-11`'s universal second clause is false.** It asserts *"**Every** valuation rule in the corpus binds value to a **movement** … so **no existing rule reaches** `MF-01`."* **`BD-ACC-03B` rules `Standard \| Average \| FIFO` with authority Product Category. Under `Standard` costing an item's value is a policy attribute of the product, not a function of a movement's carried cost** — `SA_CORR3_03` line 178 states the same mechanism from the other side: *"under standard costing, work-centre cost **never enters finished-goods value**."* A certified opening balance under a `Standard`-costed category therefore **does** have a valuation rule that reaches it. **The correct residue is the narrower, well-evidenced claim the executor makes separately and correctly — the counterpart account is undetermined (`CORE-06`). The universal clause travelled untested on the strength of the half beside it.** | **MATERIAL** |
| **`B7-F-10`** | **`MF-03`'s exclusion rests on a property nothing has established.** `17_` §2 excludes `MF-03` as *"a DIMENSION … not a flow"* because it *"adds ZERO quantity"* and *"adds ZERO value"*, cited to **`RT-E15-05`**. `RT-E15-05` is one of the `PTX` controls, and `B6` records **`0 of 11` satisfied**; element 15 is unbuilt (`MTI-50`), and `X-22` — the scenario that would test replay idempotency — is `HOLD` among the `0 of 48`. **The zero-effect property is design intent, not evidence. If replay is not idempotent, `MF-03` affects stock and belongs in `IR`.** The exclusion is stated as a fact about the flow when it is a claim about an unbuilt control. | **MATERIAL** |

**Attempt that FAILED:** the arithmetic and the honesty of the admission are sound. `IR 18→20`,
`AR 29→30` with **reconciled counts unchanged** (`14/3/3`, `15/14/1`), and both `22_` §7.1 and `23_` §1.1
state plainly that a denominator rise is not an improvement. **That is the correct reporting of an
admission that opens a gap.**

---

### `T8` — `E2E-04` — **THE BAR IS REAL · BUT `CC-F-08` IS NOT FULLY RESOLVED**

**The refusal is correct and is not hiding.** The executor built the `12`-node chain, located the break at
node `5` (*"the shortage state exits only on reservation completing, never on procurement being raised"*),
graded `4` traversable / `1` break / `7` unreachable, and separated the specification, target-model and
runtime levels. **Three independent records bar the re-grade**, and I confirmed the Boss one verbatim —
`SC-BD-02` §8.4: *"**`E2E-04` is NOT re-graded `TRAVERSABLE` by this ruling** … the re-grade is held for
the independent reviewer."* **`0` re-grades were made, and `0` are made here.**

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-11`** | **`B8′` Structure A routes the re-grade to a party the canonical evidence declares is not separate from the executor, and `22_` accepted it without testing that.** `SC-03` §0, primary text: ***"And this is not independent assurance. It is internal first-line challenge by specialist role, drawn from the same corpus assembled by the same party — the limitation `ND-12` records."*** `SC-04` §5: *"`SC-03` is internal first-line challenge by specialist role. It is **not** independent assurance"* … *"All challengers and the author drew from one corpus assembled by one party."* Yet `10_` line 86 records re-grade authority as *"SMT or B-7 … **NOT SMEs Core**"*, treating SMT as a distinct party. **In the whole `PHASE_PRETEST` tree, `ND-12` appears `0` times and *"first-line"* appears `0` times.** Structure A's own safeguard — performer ≠ certifier — **is** satisfied, because B-7 certifies. **But the stronger bar `10_` §3.1 itself identified — that the re-grade would reverse a challenge-produced withdrawal on the strength of a self-written specification — is not cured by routing the act to another role inside the same party.** | **MATERIAL** |
| **`B7-F-12`** | **Exit condition `16` is not established.** `23_` §2 moves row `16` (*"no unresolved material contradiction"*) `FAIL → SATISFIED` citing *"`CC-F-06` closed by `B3′`, **`CC-F-08` by `B8′`**"*. `CC-F-06` **is** closed. `CC-F-08` is closed **as a routing question only**; per `B7-F-11` the self-interest bar underneath it stands and the package does not say so. | **MATERIAL** |

**Not testable by me:** `B8′` assigns the re-grade to SMT and it **has not been performed**. There is
therefore **nothing for B-7 to verify**, and I did not perform it — doing so would be the certification of
my own act that `B8′` forbids.

---

### `T9` — DEFERENCE — **FALSIFIED**

**Where the executor accepted a Phase SA reading it should have refused:** `B7-F-11` is the principal
instance — an inherited premise (*SMT is a party distinct from SMEs Core*) carried into a routing
resolution without independent derivation, **contradicted by two primary records the executor cites
elsewhere in the same package**. `B7-F-09` is a second: `CC-F-11`'s universal clause was inherited from
the `JT-04` framing (*value follows the movement*) and never tested against the `Standard` branch of a
ruling the same package treats as binding.

**Counterweight, recorded because it costs something to report:** the executor **refused** more often than
it deferred — it declined to enumerate a `12`-set from a prompt floor (`02_` §2.4), declined to renumber
the veto register (`07_` §4), declined to draft issuer wording (`17_` §3.2), declined to record `AAS-V-02`
discharged (`22_` §6.1), and declined the `E2E-04` re-grade (`10_` §3.1). **`5` refusals, each on a stated
ground, each of which I verified holds.**

---

### `T10` — STALE / SUPERSEDED EVIDENCE — **ATTEMPT FAILED**

Correction `C2` verified independently **by commit date, not by filename**:

```
SA17_…BASELINE.md                    2026-09-08 22:31  9ffe6faa
SA17_…FINAL_CONTROLLED_V2.md         2026-09-09 22:38  9d5bc2db   ← latest
SA17_…CORR5_CONTROLLED.md            2026-09-09 19:51  78d1b3c6
```

**The `FINAL_CONTROLLED_V2` generation is the latest and is the only one carrying §2d.** In the package:
**`FINAL_CONTROLLED_V2` cited `22` times; the superseded CORR5 generation cited once and explicitly
labelled *"superseded"*; `0` citations of any `PARALLEL_EXECUTION_SUPERSEDED_2026_09_10` artefact as
authority.** `01_` §4 resolves seven supersession chains before relying on them.

**Correction `C3` verified:** `git cat-file -t a1fc7cd6` → **`blob`**. The pointer is valid and `git log`
on it is silent by construction. **Correction `C6` verified** at `17_` §1 — `SC-11` created the obligation
at `89ba9c7d`, `SC-14`/`-15` discharged it `23` minutes later at `dfea73b7`, and the executor published
the correction against its own three prior files. **Supersession hygiene is the strongest control in this
package.** The one path-set defect I found is recorded at `B7-F-14`, and it is a boundary-declaration
defect rather than a supersession one.

---

### `T11` — CIRCULAR PROOF — **FALSIFIED**

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-13`** | **Exit condition `2` is certified `SATISFIED` on the executor's own unratified conclusion.** `15_` row `2`: *"Gate state **freshly re-derived** — **SATISFIED** — `01_` §3 · `02_` §3 — `19 / 2 / 1` derived per-cell"*, carried unchanged through `23_` §2. Its sole evidence is the re-derivation, and **`22_` §7 records `B5′` as `NO RULING — remains PROVISIONAL `19 / 2 / 1`, B-7 attack target #1`.`** An exit condition is thus satisfied by the single figure the package itself nominates for adversarial attack and states no authority has ruled. **Combined with `B7-F-06`, row `2` is NOT ESTABLISHED.** | **MATERIAL** |

---

### `T12` — EXTERNAL-AUTHORITY SUBSTITUTION — **ATTEMPT FAILED**

**No statutory question is treated as answered by a Boss ruling.** `19_` §2 states the negative explicitly:
*"**What it does NOT mean:** that the statutory question is answered. **`TH-NEW-01`/`-02` remain
`HOLD / EVIDENCE REQUIRED`** and travel on the same line as the ruling."* `SC-BD-05` itself makes the same
disclaimer at §8.2: *"no TAS 2 claim is made anywhere by this ruling."*

Boss **did** rule `JT-04`/`JT-05` without the statutory input, and `SC-BD-05` §3 records that as a
deliberate rejection of *"hold pending the Thai statutory input"*. **That is Boss exercising Boss
authority over a business question, with the statutory validation left open and marked — not Boss
substituting for a statutory authority.** `POH-D-02` is the one case where the **decision itself** is
withheld and excluded from `B1`, which is the correct handling. The Thai population is `4`
(`TH-NEW-01`, `TH-NEW-02`, `POH-D-02` tax consequences, over-absorption cap strength) and is consistent
across `PT-10`, `PT-11`, `PT-16` and `19_`.

---

## 3. Denominators — verified, not inherited

| Denominator | Verified? | Basis |
|---|---|---|
| `12` declared boundary classes | **YES as a declaration · NO as coverage** | `22_` §1 enumerates `12`. **`B7-F-07`: covers `XMC-H-01…12` only; `4` gap-carrying handoffs outside it** |
| `18` `XMC-H` handoff rows | **YES** | enumerated `01…18`, *"each exactly once"*; disposition tally `0 / 2 / 16 = 18` ✔ |
| `10` `SA_CORR4_02` contract rows | **NOT TESTED** | §5 |
| `7` canonical vetoes, `0` discharged | **YES** | `T4`; A and B disproved with firing controls; `0` AAS+ acts (`T5`) |
| `11` `PTX` controls, `0` satisfied | **YES** | `B6` adopts `11`, *"does not satisfy any `PTX` control"*; `0 of 11` |
| `20` `IR` flows, `14` reconciled | **YES arithmetically** | `B9′`; reconciled count unchanged — correctly reported. **`B7-F-10`** attacks `MF-03`'s exclusion |
| `30` `AR` flows, `15` reconciled | **YES arithmetically** | as above |
| `48` verification items, `0 PASS` | **YES** | all four sub-populations re-derived from primary source; `22+18+7+1=48` ✔ |
| `3` `EC-04` boundaries, `0` closed | **YES** | `09_`; unchanged through the rulings |
| `2` `EC-07` passes, `0` clean | **YES** | appointment ≠ pass; **this verdict does not create one** |
| `17` exit conditions, `8` satisfied | **NO** | §4 |
| `3` remaining FD blockers | **YES as stated** | `2 of 5` closed by ruling; but see `B7-F-07` on blocker 1's closure |

---

## 4. The exit-condition count — re-derived

**Command + output, both files, unit = exit-condition row:**

```
$ 15_ §1 table  →  13 FAIL · 1 PARTIAL—treated-as-FAIL · 3 SATISFIED   (17 rows ✔)
$ 23_ §2 BEFORE →  13 FAIL · 1 PARTIAL/FAIL          · 3 SATISFIED   (17 rows ✔)
$ 23_ §2 AFTER  →   9 FAIL                            · 8 SATISFIED   (17 rows ✔)
$ rows moving FAIL→SATISFIED: 1 5 6 7 16              count: 5
```

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-01`** | **`15_`'s headline `5 SATISFIED · 12 FAIL` contradicts its own table, which enumerates `3`.** Its parenthetical *"(`2`, `8`, `14`, and partially `7`)"* names **four** items for a count of five. `23_`'s *"up from `5`"* inherits the error. **The true baseline is `3`, so the round's own gain is `3 → 8`, larger than claimed. The executor understated its result.** | **MATERIAL — arithmetic** |
| **`B7-F-02`** | **`23_` §2 states *"`3` conditions moved on rulings"* while enumerating `1`, `5`, `6`, `7`, `16` in the same sentence — five, which my command confirms.** | **MODERATE** |
| **`B7-F-18`** | `23_` §6 reports *"`5` moved on rulings, `8` did not"* against §1's own tally of `5` `YES` **plus** `1` `YES (count only)` — the veto count did move `6 → 7`. **`6` moved, `7` did not.** | **MINOR** |

**Where the `8` stands after this challenge:**

| Row | Package | This challenge |
|---|---|---|
| `1` 12-gate set established | SATISFIED | **SATISFIED as a declaration, QUALIFIED** — `B7-F-07` |
| `2` gate state freshly re-derived | SATISFIED | **NOT ESTABLISHED** — `B7-F-06`, `B7-F-13` |
| `16` no unresolved material contradiction | SATISFIED | **NOT ESTABLISHED** — `B7-F-11`, `B7-F-12` |
| `5`, `6`, `7`, `8`, `14` | SATISFIED | **unchallenged — they stand** |

> **`8 of 17` is not reproducible. `6 of 17` stand on the evidence I could verify; `1` is qualified.
> `9` FAIL are correct and unchallenged. The recommendation `HOLD PRE-TEST EXIT` is unaffected — it was
> already `HOLD`, and it remains `HOLD` for more reasons than the package records.**

---

## 5. Package-integrity findings and what I could NOT test

| ID | Finding | Severity |
|---|---|---|
| **`B7-F-15`** | **The prompt I was given states the manifest has `23` entries. It has `24`, and verifies `24 of 24`.** A challenger told to check a denominator was handed a wrong one. | **MODERATE** |
| **`B7-F-16`** | **`23_` §5 inventories *"Artefacts `24` — `01_`…`23_` + manifest"*, which omits `25_` although `24_` lists it.** The re-freeze register's artefact inventory does not match the manifest it names, and the two `24`s coincide numerically by accident. | **MINOR** |
| **`B7-F-17`** | **`22_` §8 totals *"`5` denominators"* over a table that moves `6` distinct denominators** (boundary, veto, open Boss decisions, `PTX`, `IR`, `AR`). The unit counted is **rulings**; the unit stated is **denominators**. | **MINOR** |

**Named, not silently omitted — what I could not test and why:**

1. **The `E2E-04` re-grade.** `B8′` assigns it to SMT; **it has not been performed**, so there is nothing to verify. Performing it myself would breach `B8′` and the §0 prohibition on certifying my own re-grade.
2. **Every runtime claim.** No implementation exists. `0 of 48`, `0 of 8`, `0 of 60`, `0 of 11` are not verifiable in either direction from documents, and I assert nothing about them beyond reproducing the counts.
3. **AAS+ internal state.** `0` AAS+-authored records exist. I can prove absence in this corpus with a firing control; I cannot prove the body has not acted elsewhere.
4. **The `4` Thai statutory questions.** External authority. Nothing in a corpus answers them.
5. **Whether the declared `12` is the *correct* set.** A Boss authority act. I tested coverage only.
6. **The `12 ↔ 10` mapping** (`SA_CORR4_02` §5 contract rows). I executed `12 ↔ 18`; the `10`-row leg of `CORE-04` remains underived, by me as well as by the executor.
7. **`0` of the challenged artefacts were modified**, so no test requiring a mutation of the evidence was run.

### 5.1 My own instrument failures — `5`, reported as required

| # | Failure | How it surfaced | Correction |
|---|---|---|---|
| **`1`** | **Off-by-one field index** parsing `SA_CORR5_10` §4: I read `$13` (`RP`) as the `PT` column and got *"`22 Y`"* for a readiness split. | Caught by **implausibility**, not by design — a `22`-way unanimous readiness column cannot be right. | Published the header field map **before** the tally; `PT` is `$14`. All `T1` figures re-derived after the fix. |
| **`2`** | **Identifier-pattern false positive.** `grep -oE '[A-Z]{2,3}-V-[0-9]{2}'` over `SC-04` returned **`SC-V-01`**, which I briefly treated as a veto missing from `07_`'s population. | Second-shape search across the repo returned `SC-10` line 97: *"(`SC-V-01` is a **measurement id** in `SC-04`, **not** a veto — it is excluded from the population.)"* | Hypothesis withdrawn. **The executor's population bound is correct and was pre-declared.** |
| **`3`** | **A count command matching its own documentation.** `grep -rliF` over the `6` directories searched **`199`** files, not the declared **`192` `.md`**, and matched `PACKAGE_MANIFEST_SHA256.txt`, which *lists a filename* containing `DROPSHIP` and `idempot` — inflating **both** positive controls by exactly `1` (`50`/`58` vs `49`/`57`). | I first suspected corpus drift and tested it at `PT-01`'s own commit; the file sets were identical, which located the fault in my instrument. | Re-ran restricted to the declared unit. **All eleven `PT-01` §5.1 figures then reproduced exactly.** The executor's measurement was right and mine was wrong. |
| **`4`** | **A pre-commit sweep matched its own output.** My check *"no challenged artefact modified"* ran `git status --short -- '*PHASE_PRETEST*'` and returned **`1`** — which was **my own new directory**, `INDEPENDENT_REVIEW/B7_PHASE_PRETEST_2026_09_10/`, matching on a substring of its name. | The `1` was implausible for a session that had written nothing to the challenged tree. | Re-ran against the **full literal path** `…/PHASE_PRETEST/`: **`0` modified**, and `git diff --stat` against the frozen head over the same path: **`0` lines**. Manifest re-verified **`24 of 24 OK`** after all work. |
| **`5`** | **A correction that silently did not apply.** A `sed -i ''` fixing my own severity breakdown matched nothing — the pattern contained `…` and backticks — and **exited `0`, reporting success.** | Only caught because I re-grepped the line instead of trusting the exit status. | Re-applied with an **asserted occurrence count** (`assert s.count(old)==1`) so a non-match fails loudly, then re-ran the tally and compared *stated* against *commanded*. **This is the declared-pattern-not-run defect, committed by the challenger inside the sweep built to catch it.** |

---

## 6. Disposition

| | |
|---|---|
| **VERDICT** | **`HOLD`** |
| Targets with a recorded falsification attempt | **`12 of 12`** |
| Attempts that **succeeded** | **`6`** — `T1`, `T3`, `T7`, `T8`, `T9`, `T11` |
| Attempts that **failed** (executor upheld) | **`6`** — `T2`, `T4`, `T5`, `T6`, `T10`, `T12` |
| Findings raised | **`18`** — `B7-F-01`…`B7-F-18`; **`11` MATERIAL · `1` MATERIAL (arithmetic) · `3` MODERATE · `3` MINOR** — tallied by command, not asserted |
| Exit conditions I could not sustain | **`2`** — rows `2` and `16`; row `1` qualified |
| Re-grades performed | **`0`** |
| Vetoes discharged, `PASS` declared, statutory questions answered | **`0` · `0` · `0`** |
| Writes to the challenged branch | **`0`** |
| Functional Design | **NOT authorized by this verdict** |
| `EC-07` | **`0 / 2` — this challenge is one input to it and does not by itself constitute a pass. Boss determines whether it counts.** |

> **The package is careful, and its refusals are its strongest work — five separate places where a number
> or a grade was available to write down and the executor declined on a stated ground I verified. Its
> defects are concentrated where a figure was produced rather than refused: the readiness split it
> generated itself, the coverage mapping it recorded as owed and did not perform, the universal clause it
> attached to a well-evidenced finding, and the routing premise it inherited without testing. The
> direction of the arithmetic errors is against the executor's own interest, which is itself evidence
> about how the package was written.**
>
> **`19 / 2 / 1` is not reproducible as a membership. The `12`-boundary declaration leaves `4` measured
> handoff gaps outside the contracted surface. `8 of 17` is not reproducible. Boss decides what follows.**

---

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Falsify before Accept.
**Boss is the sole Final Approver.**
