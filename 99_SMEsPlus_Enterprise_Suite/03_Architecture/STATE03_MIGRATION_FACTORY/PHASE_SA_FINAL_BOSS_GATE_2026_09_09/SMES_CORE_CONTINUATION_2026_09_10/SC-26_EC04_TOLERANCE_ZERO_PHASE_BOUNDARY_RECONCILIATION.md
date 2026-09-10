# SC-26 — `EC-04` TOLERANCE-ZERO PHASE-BOUNDARY RECONCILIATION

## CP-SA-SC-200 — EXACT CONSTITUTIONAL DEADLOCK BOUNDED — `EC04-PATH-3`

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `2cfb57eb`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`EC-04` is not weakened anywhere in this file. No runtime proof is relabelled as specification proof.
> No current-scope blocker is moved forward to open a gate.**

---

## 1. Result

> # `EC04-PATH-3 — CONSTITUTIONAL DEADLOCK EXISTS, AND ITS CAUSE IS NARROWER THAN EXPECTED.`

**The deadlock is real, but it is not what the `05_` prompt anticipated.** The prompt framed it as
*"`EC-04` requires evidence closure before Phase SA exits, but runtime evidence may require a phase Phase SA
cannot enter before exit."* **That circularity only arises if the eight criteria bind at a *phase*
boundary at all — and the constitution contradicts itself on exactly that point.**

| | |
|---|---|
| Tolerance-zero boundaries implicated | **3**, enumerated at §2 |
| Closed by executed runtime evidence | **`0` of 3** |
| `EC-04` evidence form required at this gate | **NOT DETERMINABLE from the instrument** — §4 |
| Root cause | **§4 says `phase or State`; §11 says `STATE`. `phase` occurs exactly once in 257 lines; `state` occurs 22 times** — §3 |
| Path selected | **`EC04-PATH-3`** — deadlock published, smallest possible Boss clarification card at §7 |
| Paths rejected, with reasons | `PATH-1` §5.1 · `PATH-2` §5.2 · `PATH-4` §5.3 |

---

## 2. The tolerance-zero population — primary source, two shapes

**POPULATION:** every `TOLERANCE-ZERO` marking in the Phase SA corpus.
**Shape 1:** occurrence count on the CORR5 branch = **3**. **Shape 2:** distinct files = **3**.
**Positive control:** the pattern fires on `SA_CORR4_03`.

| # | Boundary | Primary source | State | Evidence form it would need |
|---:|---|---|---|---|
| **1** | **`CF-I-03` `D3` cross-tenant** — *"breach → the emitting fact is not emitted; a fact already emitted is flagged and its consumers notified"* | `SA_CORR4_03` line 261 | **`SPECIFIED`** (`CP-SA-C4-30`), not built, not executed | **C — executed runtime proof.** The clause asserts *behaviour under breach*; only execution evidences it |
| **2** | **Privileged-bypass path enumeration** — *"`CRITICAL — TOLERANCE ZERO` in the target architecture"* | `SA_CORR4_01` line 260 | enumerated and specified; **not executed** | **B or C** — the *enumeration* is closable by evidence; the *control's behaviour* is not |
| **3** | **Tenant/company boundary matrix** | `SA10` line 196 — disposition **`TOLERANCE-ZERO — HOLD`** | **explicitly `HOLD`** | **C**, and it is the one already **self-declared** unclosed |

> **`0 of 3` are evidence-closed at executed-runtime level.** **`EC-04` says *"`CONDITIONAL PASS` may not
> bypass a tolerance-zero risk"*, and §10 permits `RECOMMEND CONDITIONAL PASS` *"only for explicitly
> non-tolerance-zero residuals"* — so "specified, proof deferred" is not an available disposition if
> `EC-04` applies.**

---

## 3. `SC-F-15` — the constitution contradicts itself on the advancement boundary

**This is the finding that reframes the whole problem, and it was found by re-reading the instrument rather
than the packages that cite it.**

| Clause | Verbatim | Boundary |
|---|---|---|
| **§4 Module Exit Rule** | *"No Module may advance to its next controlled **phase** or State unless `EC-01 PASS` … `EC-08 PASS`. Then and only then may the Module be presented to Boss for Final Exit Decision."* | **phase OR State** |
| **§11 Project-Wide Constitutional Rule** — *"Effective immediately"* | *"NO MODULE MAY ADVANCE TO **THE NEXT CONTROLLED STATE** UNLESS ALL EIGHT VERY DEEP RESEARCH EXIT CRITERIA ARE SATISFIED WITH VERIFIED EVIDENCE AND BOSS ISSUES THE FINAL EXIT DECISION."* | **State only** |

**Measured across the whole instrument (257 lines):**

| Token | Occurrences | Where |
|---|---:|---|
| **`phase`** | **1** | **only** §4's sentence |
| `state` | **22** | §2.3, §2.4, §3, §5 (State Exit Rule), §11 (both operative rules), throughout |

**Corroborating structure:** §2's five application points name Module · Domain/Wave · **STATE** ·
Cross-Module and Whole-System **State** Integration Review · Boss-designated research programmes — **no
phase**. §3's own sentence is *"A **Module or State** may advance…"*. §5 is titled **State** Exit Rule.

> **§11 restates §4's Module rule and drops the word `phase`.** Under §11, the eight criteria bind at
> `STATE03 → STATE04` — **not** at Phase SA → Pre-Test, which is a phase transition inside `STATE03`.

### 3.1 This cuts against the ruling this executor was given, and it is published anyway

> **`SC-CONTRA-01` records `FG-F-06 = READING A`, and `SC-13`-era analysis offered §4's *"next controlled
> phase"* as one of Reading A's grounds.** That ground rests on **the single occurrence of `phase` in the
> entire constitution**, in a clause the instrument's own *"Effective immediately"* rule restates without it.
>
> **SMEs Core withdraws the strength previously attributed to that ground.** It is not eliminated — §4 is
> real text and "phase" is really there — but it is **materially weaker than presented**, and the reading
> that makes the instrument internally consistent is the `STATE` reading.
>
> **Doctrine applied: `Truth over Pass`. This finding makes the case for the instruction this executor is
> operating under weaker, not stronger, and preserving it is the point.**

---

## 4. What `EC-04` requires at THIS gate — not determinable

**The `05_` prompt §5 requires each boundary classified A / B / C / D. The classification at §2 is what
each boundary's *claim* would need. What the constitution *requires at this gate* is a different question,
and the instrument does not answer it:**

| Question | Answer from primary text |
|---|---|
| Does `EC-04` apply at Phase SA → Pre-Test? | **DISPUTED** — §4 yes, §11 no (§3) |
| If it applies, does *"evidence-closed"* mean executed runtime proof? | **UNDEFINED.** `EC-04` never defines the evidence form. It lists *subjects* (tenant isolation, financial integrity, unauthorized/duplicate posting…), not *proof forms* |
| Does §10 settle it? | **No.** §10 constrains the **recommendation** (`CONDITIONAL PASS` only for non-tolerance-zero residuals). It does not say what evidence closes a boundary |
| Does any Boss ruling settle it? | **No** — §5.3 |

> **Two independent undefined terms — *whether it applies*, and *what closes it*. Either alone would be a
> scope question; together they make the requirement unresolvable from the instrument.**

---

## 5. Why the other three paths are rejected

### 5.1 `EC04-PATH-1` — CURRENT PHASE CAN PROVE IT — **REJECTED**

Closing boundary 1 requires executing `CF-I-03` `D3` and observing behaviour under a cross-tenant breach.
That requires the control **built**. **`RC-V-01` bars implementation start** — independently of `8C-001`,
on every reading of `FG-F-06` — until an independent check over the wider five-row set.

**A minimum proof harness was considered and rejected**: any harness exercising a cross-tenant breach path
is itself an implementation of the control surface, so building it *is* the implementation start `RC-V-01`
bars. **Boundary 3 is worse — it is self-declared `HOLD`, not merely unbuilt.**

> **Phase SA cannot lawfully produce the evidence.** Not "has not"; **cannot, without breaching a standing
> veto.**

### 5.2 `EC04-PATH-2` — PRE-TEST IS THE AUTHORIZED PROOF MECHANISM AND ENTRY IS NOT A BARRED ADVANCEMENT — **NOT SELECTED, THOUGH THE TEXT LEANS THIS WAY**

**§11's `STATE` wording, the 1-vs-22 token count, and §2/§3/§5's consistent `Module`/`State` vocabulary all
support it. So does coherence: it is the only reading under which the instrument is not self-defeating.**

**It is not selected, for one reason and it is decisive:**

> **`05_` §5: *"Use this only if primary constitutional text PROVES it. Publish the exact scope basis. Do
> not infer it for convenience."*** **§4's single `phase` is primary constitutional text that says
> otherwise.** A reading that must **discount** an operative clause is a strong interpretation, **not a
> proof** — and this is the gate-opening direction, which `05_` §3's bias control names explicitly.
>
> **The evidence is published in full at §3 so Boss can select `PATH-2` on it. SMEs Core will not select it
> on Boss's behalf.**

### 5.3 `EC04-PATH-4` — A PRIOR BOSS RULING ALREADY RESOLVES IT — **REJECTED, searched**

**POPULATION:** every Boss ruling surface — `01_BOSS_APPROVED_ARCHITECTURE_RULINGS` (`BD-ACC-01`/`02`/`03A`/
`03B`), `04_PHASE_S_CONDITIONAL_CLOSURE_AND_PHASE_SA_ENTRY`, `Q-BOSS-02`, `BD-02`, `BD-04`, the
`MTI-D-01/02/03` rulings, the handoff-contract approval, and `SC-BD-01`…`SC-BD-10`.
**PATTERN:** tolerance-zero, evidence-closed, and `EC-04` by identifier.
**RESULT: `0` rulings address the evidence form required for a tolerance-zero boundary at a phase exit.**
**POSITIVE CONTROL:** the same sweep returns the `BD-ACC-*` rulings on their own subjects, so it fires.

**The nearest instruments point the other way and are recorded as such:** `AAS-V-01` and `CF-V-01` are
**runtime-proof-dependent vetoes** whose discharge is routed to *"build element 10, execute the proofs"* —
i.e. **the programme's own veto structure already treats runtime proof as a post-Phase-SA obligation.**
That is evidence of practice, **not a ruling**, and it is not used as one.

---

## 6. The deadlock, stated exactly

> **IF the eight criteria bind at Phase SA → Pre-Test (§4's `phase`), THEN:**
> 1. `EC-04` requires `3` tolerance-zero boundaries evidence-closed before exit;
> 2. `0 of 3` can be closed without executing controls;
> 3. executing controls requires implementation start;
> 4. **`RC-V-01` bars implementation start** until an independent check;
> 5. the phase in which such controls are normally proven **is the phase `EC-04` gates**;
> 6. **`CONDITIONAL PASS` is expressly forbidden for tolerance-zero residuals**, so the gate cannot be
>    passed with the residual declared.
>
> **⇒ Phase SA cannot exit, and no amount of SMEs Core work, and no number of clean `EC-07` passes, changes
> that.** A reviewer can verify a control is specified; **a reviewer cannot make it executed.**
>
> **IF the eight criteria bind only at `STATE03 → STATE04` (§11's `STATE`), the deadlock does not arise:**
> Pre-Test produces the runtime evidence, and `EC-04` is tested at the State exit **when that evidence
> exists**.

**The deadlock is therefore not a defect in Phase SA's work. It is a consequence of an unresolved
ambiguity in the constitution, and it resolves in one direction and not the other.**

---

## 7. The smallest possible Boss constitutional clarification card

> **This card does not rewrite the Constitution. It asks Boss to state which of the instrument's own two
> clauses governs the advancement boundary.**

```
8C-BOUNDARY-01 — Which clause governs the advancement boundary?

  (a) §4 as written — "next controlled phase or State"
      => the eight criteria gate Phase SA -> Pre-Test
      => EC-04 must then be answered: see 8C-BOUNDARY-02

  (b) §11 as written — "THE NEXT CONTROLLED STATE"
      => the eight criteria gate STATE03 -> STATE04
      => Pre-Test entry is not a barred advancement; EC04-PATH-2 is proven and the deadlock dissolves

  (c) Other explicit Boss disposition
```

```
8C-BOUNDARY-02 — Required ONLY if (a). What evidence form closes a tolerance-zero
                 boundary at an ARCHITECTURE exit?

  (A) specification evidence
  (B) executable proof design
  (C) executed runtime proof
  (D) another form Boss states

  If (C): please also state how EC-04 is to be satisfied given RC-V-01 bars the
  implementation start that (C) requires — §6 above.
```

**Relationship to `SC-AUTH-01`:** these are **different questions**. `SC-AUTH-01` asks which *record*
controls; `8C-BOUNDARY-01` asks which *clause* controls. **Answering `FG-F-06 = Reading B` makes
`8C-BOUNDARY-01` moot for this exit; answering Reading A makes it decisive.** They should be answered in
the same act.

---

## 8. What this file does NOT do

1. **Does not weaken `EC-04`** — no boundary is reclassified, and the `0 of 3` stands.
2. **Does not relabel runtime proof as specification proof.**
3. **Does not move a current-scope blocker into Pre-Test** to open the gate.
4. **Does not select `PATH-2`**, though it publishes the full case for it.
5. **Does not rewrite, amend or reinterpret the Constitution** — it reports two of its clauses verbatim.
6. **Does not answer `FG-F-06`.**

---

## 9. Checkpoint

> ## `CP-SA-SC-200 — EXACT CONSTITUTIONAL DEADLOCK BOUNDED (`EC04-PATH-3`)`
> **`3` tolerance-zero boundaries, `0 of 3` runtime-closed, each classified for the evidence form its own
> claim needs · `EC-04`'s applicability **disputed inside the instrument** (`SC-F-15`: `phase` × 1 vs
> `state` × 22; §11 drops `phase` when restating §4) · `EC-04`'s required evidence form **undefined** ·
> `PATH-1` rejected — Phase SA **cannot lawfully** produce the evidence without breaching `RC-V-01` ·
> `PATH-2` **not selected despite the text leaning toward it**, because §4 is primary text that says
> otherwise and this is the gate-opening direction · `PATH-4` rejected on a searched `0` with a firing
> control · **two-question clarification card published, and the case AGAINST this executor's own governing
> instruction published with it**.**

No Evidence = No Progress. Never Skip Gate. Do not weaken the standard to open the gate.
Boss remains the sole Final Approver.
