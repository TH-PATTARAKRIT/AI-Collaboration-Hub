# PT-13 — SMEs CORE FALSIFICATION REGISTER

## `CP-PT-13 — INTERNAL FALSIFICATION COMPLETE`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `7b163828`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This is SELF-challenge. It is NOT independence and is nowhere presented as such.**
> **The programme's own measured ratio is that independent review finds roughly an order of magnitude
> more than self-review. This register must be read as the weaker of the two controls.**

---

## 1. Result

| | |
|---|---|
| Challenge classes applied | **`20 of 20`** |
| **Defects found in this session's own package** | **`2`** — `PT13-D-01`, `PT13-D-02` |
| **This session's own findings CORRECTED by this round** | **`1`** — `PT05-F-01`, causal attribution wrong |
| Self-suspicions raised and **REFUTED** | **`2`** — both were my own grep, not the file |
| Evidence pointers cited by this package | **`32`** · **`0` unresolved** |
| Own-family identifiers | **`49`** · **`1` orphan** (`PT13-D-01`) |
| Findings that survived challenge unchanged | **`19 of 21`** |

---

## 2. `PT13-D-01` — an orphan identifier in this session's own ledger

| | |
|---|---|
| Defect | **`PT11-P-01`** appears **`1`** time in `PHASE_PRETEST_AUTO_RESUME_STATE.md` and **`0`** times in any `PT*.md` artefact |
| Cause | the boundary-set proposal was written into `PT-11` §6.1 **as prose with no identifier**, and an identifier was minted **only in the ledger** |
| Class | **evidence-pointer integrity — challenge class 19** |
| Why it matters | a reader following the ledger to `PT-11` finds no `PT11-P-01`. **A ledger row pointing at nothing is the same failure shape this session found in others** |
| **Fixed** | **YES — `PT-11` §6.1 now carries the identifier `PT11-P-01` explicitly** |

## 3. `PT13-D-02` — a rule this session imposed on itself, measured for compliance

**`PT03-F-01` bound this session: *every downstream citation of `MATERIAL PHASE-SA GAP = 0` must carry the
words "owned by SMEs Core / PMO / document owner"; the bare form is prohibited.***

**Measured across the package:**

| File | Unqualified occurrences | Verdict |
|---|---:|---|
| `PT-04` … `PT-12` (all downstream of the rule) | **`0`** | **RULE OBEYED** |
| `PT-03` | `2` | both are **the finding stating the claim it is about**, one immediately paired with the qualified form — **not violations** |
| **`PT-02`** | **`2`** | **upstream of the rule** (written before `PT-03`), inside the **withdrawn** `PT02-F-02` section |

| | |
|---|---|
| Verdict | **PARTIAL PASS-EQUIVALENT — the rule held wherever it applied; `2` upstream mentions predate it** |
| Action | **NOT retro-fixed.** Editing `PT-02` to satisfy a rule invented at `PT-03` would make the package look more consistent than the work was. **The measurement is published instead** |

---

## 4. `PT05-F-01` — CORRECTED BY THIS ROUND. The causal attribution was wrong.

### What `PT-05` claimed

That `SC-45` **substituted** rule 6, *"dropping 'routing follows Business Nature, not module name'
entirely"* — implying `SC-45` discarded a rule it was mandated to carry.

### What the governing prompt actually says

**`06_PHASE_SA_SINGLE_SESSION_CANONICAL_RECOVERY…PROMPT`, the law governing the `SC-45` round, verbatim:**

> *Mandatory convergence:*
> - *stock-affecting → Inventory;*
> - *manufacture-required → Manufacturing;*
> - *procurement/dropship-required → Purchase;*
> - *every material flow → Accounting semantic reconciliation;*
> - *one output may feed multiple consumers.*

**`FIVE` rules — and they are exactly `SC-45`'s rules 1–5.**

### The correction

| `PT-05` said | Corrected |
|---|---|
| `SC-45` **substituted** rule 6 | **`SC-45` followed its governing prompt's five and ADDED a sixth of its own** (the `INPUT → … → NEXT MODULE INPUT` closure) |
| `SC-45` **dropped** the Business-Nature rule | **The `06_` prompt had already dropped it.** `SC-45` never had it to drop |

### What survives — and it is sharper than what it replaces

> **The Business-Nature routing rule was lost at the PROMPT layer, not the register layer.** It is present
> in the CORR3 master prompt's six and in Set A (the tested register), and **absent from the `05_`/`06_`
> prompts' five and from `SC-45`'s six.**
>
> **That is worse, not better:** a register dropping a rule is one round's error; **the governing law
> dropping it removes the obligation to test it from every subsequent round** — and *routing follows
> Business Nature, not module name* is **the central doctrine of THIS phase's master prompt §7**.

**Unaffected and still standing:**

| Surviving half | Status |
|---|---|
| **`3` material qualifications stripped** between Set A and Set B (enumeration short by ≥1 · make-selection trigger undetermined · entry beneath Purchase's control floor) | **UNCHANGED** |
| Rule 5 reported **`HOLDS`** where the tested register reads ***"One defect found"*** | **UNCHANGED** |
| `0` rules hold unqualified | **UNCHANGED** |
| Set A governs `PT-12` | **UNCHANGED** |

---

## 5. Two self-suspicions raised and REFUTED — both were my own instrument

| # | Suspicion | Refutation |
|---:|---|---|
| 1 | `PT-12` table A appeared to contain **`18`** rows, not `22` | **`4` rows are bolded** (`\| **\`X-07\`**`), so a `^\| \`X-` pattern missed them. Re-run with an optional-bold pattern: **`22` rows, contiguous, lines 53–74** |
| 2 | `PT-12` appeared to contain `12 GATED* + 2 GATED + 10 WRITABLE = 24` rows against a population of `22` | The `GATED\`\*` pattern **also matched the plain `**\`GATED\`**` rows** via the trailing `**`. Correct: **`10 GATED*` + `2 GATED` + `10 WRITABLE` = `22`** ✔ |

> **Both apparent defects were pattern-too-narrow and pattern-too-wide respectively, in this session's own
> checking commands** — the class this package has flagged in others `3` times. **Published, because a
> falsification round that reports only the file's errors and none of its own instrument's is not a
> falsification round.**

---

## 6. The `20` challenge classes, applied

| # | Class | Result |
|---:|---|---|
| 1 | missing input | **`7 of 16` contract elements unsupplied — recorded, `PT-02`** |
| 2 | ambiguous process | `0 G` cells; ambiguity is Boss-election-shaped, not spec-shaped |
| 3 | output not consumable downstream | **`4` outputs with no consumer — `PT04-F-03`** |
| 4 | accounting consequence omitted | `0 of 29` flows lack a semantic; `14` carry an open element |
| 5 | inventory consequence omitted | `IC = C` on all `22`; `1 of 18` flows `NOT RECONCILED` (`IR-18`) |
| 6 | wrong manufacture/purchase/dropship route | **`PT07-F-03` — route "holds" while breaching `ND-03`'s control floor** |
| 7 | cross-tenant/company leakage | **`2` lock-defeat paths — `PT08-F-02`**; severity ranked on target architecture (`PT08-F-01`) |
| 8 | missing reversal/correction path | **corrected-entry link does not exist; `PT09-F-02` composition** |
| 9 | non-idempotent retry | element 15 not built; `0 of 13,814` dedup keys |
| 10 | approval bypass | `X-12` approval mechanism absent; `XD-03` occurrence not recorded |
| 11 | unsupported assumption | **`PT02-F-02` withdrawn** — a finding of mine that was one |
| 12 | vendor behaviour copied as requirement | **`0`** — `0 of 3` dropship and `0 of 13,814` dedup published as `PTE-2`, **neither used to decide anything** |
| 13 | untestable expected result | **veto limb 2 *"tests for uniqueness where the answer is zero"* — undischargeable in either direction** |
| 14 | false runtime proof | **`0`** — `EC-04` `0/3` in and out |
| 15 | hidden Boss decision | **`0`** — `7` open, only `4` presentable (`PT-11`) |
| 16 | hidden external dependency | `13` external items enumerated |
| 17 | current-scope gap dumped forward | **`0`** — and the one candidate (`PT02-F-02`) was **disproved by its own author** |
| 18 | contradiction with a Boss ruling | **`0`**; `SC-BD-02` §8.4's *"`E2E-04` is NOT re-graded"* **obeyed** |
| 19 | evidence-pointer integrity | **`32 of 32` objects resolve**; **`1` orphan identifier — `PT13-D-01`, fixed** |
| 20 | scenario count / denominator defect | **`3` found — `PT00-F-01` (`64`→`76`), `PT04-F-01` (`12`/`18`/`10`), `PT07-F-01` (veto `6`-or-`7`); plus this session's own `47 → 48`, published** |

---

## 7. Adversarial test of this session's own strongest findings

| Finding | Challenge put to it | Outcome |
|---|---|---|
| **`PT04-F-01`** boundary set undeclared | *"Declared as a set" may mean "to be declared", not "is declared"* | **SURVIVES — and is corroborated.** `SC-11` §6 obligation `5` makes the per-boundary applicability declaration an **outstanding SMEs Core obligation**, which only makes sense if it is not yet done |
| **`PT07-F-01`** manufacturing veto outside the six | *Is it `AAS-V-03` under another name?* | **SURVIVES.** `AAS-V-03`'s limbs are `F6` (`MTI-D-04`) and `F1`'s COGS gap. The manufacturing veto's are `BLK-07` and machine-cost. **Different limbs, different subjects** |
| **`PT10-F-01`** pre-ruling split | *A `B` cell may not move on a ruling alone — the specification text may still need updating* | **SURVIVES, and the challenge STRENGTHENS the decision not to re-derive.** This is precisely reason `3` given at `PT-10` §2 for carrying the figures unchanged |
| **`PT09-F-01`** exit-criteria instruction unconsumed | *Was it addressed elsewhere?* | **SURVIVES.** `SC-11` §6 obligation `8` names the owner as **"Pre-Test"** — this session — and it was outstanding on entry |
| **`PT05-F-01`** two rule sets | *Did `SC-45` follow a later governing prompt?* | **PARTIALLY FALSIFIED — corrected at §4.** The causal attribution was wrong; the substance survives and sharpens |

---

## 8. What self-challenge could not do

| Limit | |
|---|---|
| **Independence** | This is the same execution body that authored `PT-00`…`PT-12`. **`0` structural independence.** |
| **Measured effectiveness** | The programme's own record: **`3` self-caught vs `29` externally caught** on one package; **`6` vs `20`** on another; **`12 of 32` author findings corrected by review, `60` new**. |
| **The specific blind spot** | **`PT10-F-01` is the finding this session most wants to be right about, because it improves the picture.** Self-challenge is structurally weakest exactly there — which is why `PT-14` flags it to B-7 by name. |
| **Deference** | The programme has recorded that **adversarial-only review cannot catch deference**. Nothing in this register tests whether this session deferred to a Phase SA reading it should have refused. |

---

## 9. Checkpoint

> ## `CP-PT-13 — INTERNAL FALSIFICATION COMPLETE`
>
> **`20 of 20` challenge classes applied · **`2` defects found in this session's own package** (`PT13-D-01`
> orphan identifier, **fixed**; `PT13-D-02` self-imposed-rule compliance, **measured and published rather
> than retro-fixed**) · **`1` of this session's own findings CORRECTED — `PT05-F-01`'s causal attribution
> was wrong, and the corrected version is worse for the programme: the Business-Nature routing doctrine was
> lost at the PROMPT layer, removing the obligation to test it from every subsequent round** ·
> `2` self-suspicions **refuted, both my own patterns** — one too narrow, one too wide · `32 of 32`
> evidence pointers resolve · `19 of 21` findings survive unchanged.**
>
> **This is self-challenge and is the weaker control. `0` structural independence is claimed.**

Next checkpoint: `PT-14 — B-7 Structurally Independent Challenge`.

No Evidence = No Progress. Never Skip Gate. Falsify before Accept. Self-challenge is not independence.
Boss remains the sole Final Approver.
