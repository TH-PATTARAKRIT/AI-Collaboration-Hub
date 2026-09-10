# SC-40 — `8C-001` CONSTITUTIONAL HARMONIZATION AND `EC-04` BOUNDARY

## CP-SA-SC-310 — EXACT BOSS CLARIFICATION READY

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed `e2e3f3dc`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`EC-04` is not weakened anywhere in this file. No tolerance-zero boundary is reclassified, and no
> specification is relabelled as runtime proof.**

---

## 1. Result

> # `HARMONIZATION IS AVAILABLE AND STRONGLY SUPPORTED — BUT NOT UNAMBIGUOUS, BECAUSE THE INSTRUMENT DEFINES NONE OF ITS OWN TERMS.`
> **`8C-CLARIFICATION-01` is drafted at §7.**

| Mandatory question | Answer |
|---|---|
| **A — advancement boundary** | **Option `C`** — a third boundary supported by primary evidence: **the two gates the instrument itself names in §5**, neither of which is Phase SA → Pre-Test |
| **B — `EC-04` evidence form** | **executed runtime proof + independent reproduction, closed at the State gate.** Not at this transition — and **not relaxed** |
| **Anti-deadlock test** | **Reading A fails it.** Reading C passes |
| Harmonized unambiguously? | **NO** — one operative word (`phase`) must be read as subsumed, and **`Module`, `Phase` and `State` are undefined** |

---

## 2. The harmonization, factor by factor

**`06_` §5 prescribes eleven interpretive factors. Each is applied to primary text.**

| # | Factor | Finding | Points to |
|---:|---|---|---|
| 1 | **Direct text** | §4: *"next controlled **phase** or State"* | **A** |
| 2 | **Direct text** | §11 *"Effective immediately"*: *"THE NEXT CONTROLLED **STATE**"* | **B/C** |
| 3 | **Section purpose** | §4's consequence clause: *"Then and only then may the Module be presented to Boss for **Final Exit Decision**. AI/PMO may issue only a recommendation. Boss alone decides Final Exit."* **§4's operative purpose is an EXIT decision, not an internal transition** | **C** |
| 4 | **Later-operative wording** | §11 is the only clause labelled *Project-Wide Constitutional Rule* and *Effective immediately*, and it **restates §4 without `phase`** | **B/C** |
| 5 | **Whole-document structure** | **`phase` occurs `1` time in 257 lines; `state` occurs `22`.** §2's five application points contain no `phase`; §3 reads *"A **Module or State** may advance"*; §5 is the **State** Exit Rule | **B/C** |
| 6 | **Module vs State vs Phase taxonomy** | **The instrument defines NONE of the three.** Searched, with a firing control on terms it *does* define (`PARTIAL != PASS`; *"Reopen is not a reset"*) | **ambiguity — the root cause** |
| 7 | **Phase SA's location inside `STATE03`** | Its artefacts live under `…/STATE03_MIGRATION_FACTORY/PHASE_SA_*`, and are named `CROSS_MODULE_ASSURANCE`, `CROSS_MODULE_RECHALLENGE`, `CROSS_MODULE_CONTRACT_PROOF`. **§2.4 names exactly this: *"Cross-Module and Whole-System State Integration Review."*** | **C — the instrument reaches Phase SA** |
| 8 | **Pre-Test's location** | also inside `STATE03`; the transition is **State-internal** | **B/C** |
| 9 | **Veto release paths** | `AAS-V-01`/`CF-V-01` route element-10 proof to *"build … execute the proofs"*; **`RC-V-01` bars implementation start**. The programme's own veto structure **already places runtime proof after Phase SA** | **C** |
| 10 | **Proof feasibility** | §4 — §5 below | **C** |
| 11 | **Non-circular interpretation** | §4 — §5 below | **C** |

### 2.1 The clause that decides it — §5's mandatory sequence

```
Module Very Deep Research
-> Module 8-Criteria Exit Gate
-> All in-scope Modules evidence-ready
-> State Integration Very Deep Review
-> State 8-Criteria Exit Gate
-> Boss Final State Decision
-> Next State
```

> **The instrument names exactly TWO eight-criteria gates and locates both.** The **Module** gate follows
> *Module Very Deep Research*. The **State** gate follows the *State Integration Very Deep Review*.
> **Phase SA → Pre-Test is neither.**
>
> **And §5's opening sentence confirms the architecture:** *"Passing all Module gates **inside a State** is
> necessary but not sufficient for State advancement."* Module gates sit **inside** a State — one per
> Module — **not one per phase transition.**
>
> **No prior round, on either track, read this sequence against the taxonomy question.**

---

## 3. Mandatory question A — the advancement boundary

> ## **`C` — the two gates the instrument names in §5.**

| Gate | Location | For Account |
|---|---|---|
| **Module 8-Criteria Exit Gate** | immediately after *Module Very Deep Research* | **Phase S's exit** |
| **State 8-Criteria Exit Gate** | after the *State Integration Very Deep Review* | **`STATE03 → STATE04`** |

**Phase SA is the State Integration Very Deep Review** (§2.4, and its own artefact names). **It feeds the
State gate. It is not itself a gate the instrument names.**

### 3.1 The uncomfortable consequence — stated because it is the honest half

> **If the Module gate follows Module Very Deep Research, Account's Module gate was Phase S's exit — and
> Phase S closed CONDITIONALLY with `0` references to `EC-01`…`EC-08`** (searched; firing control returns
> **19** hits on a file that does cite them).
>
> **Reading C therefore does not clear the path. It relocates an unmet obligation to a gate already
> granted, and to a State gate still ahead.** **This is the opposite of a gate-opening convenience**, and
> it is the reason SMEs Core is willing to publish the harmonization at all.

---

## 4. Mandatory question B — `EC-04` evidence form per boundary

**No boundary is downgraded. Each is classified for what its own claim requires.**

| # | Tolerance-zero boundary | Specification | Executable proof design | **Executed runtime proof** | Independent reproduction | **Closure point** |
|---:|---|:--:|:--:|:--:|:--:|---|
| 1 | `CF-I-03` `D3` cross-tenant — *"breach → the emitting fact is not emitted; a fact already emitted is flagged and its consumers notified"* | **done** | required | **REQUIRED — the clause asserts behaviour under breach** | required | **State gate** |
| 2 | Privileged-bypass path enumeration | **done** | required | **REQUIRED for the control's behaviour** | required | **State gate** |
| 3 | `SA10` tenant/company boundary matrix — `TOLERANCE-ZERO — HOLD` | partial | required | **REQUIRED** | required | **State gate** |

**`0 of 3` closed today, and that is unchanged.** What Reading C changes is **where they must be closed**,
not **whether**. **`CONDITIONAL PASS` remains forbidden for all three at that gate** (§10).

> **This is the whole of the no-weakening guarantee: the standard is identical; only its location moves —
> and it moves to the gate that comes *after* the phase able to produce the evidence.**

---

## 5. The mandatory anti-deadlock test

> **Question: *Can the required proof legally exist before the gate that allegedly requires it?***

| Interpretation | Answer | Verdict |
|---|---|---|
| **Reading A** (§4 with `phase`) | **NO.** Executed proof needs a build; **`RC-V-01` bars implementation start**; the phase that produces it is the phase `EC-04` gates | **CIRCULAR** |
| **Reading C** | **YES.** Pre-Test produces the runtime evidence; the State gate then tests `EC-04` against it | **NON-CIRCULAR** |

**The escape clause, searched:** the test permits circularity *"unless explicit constitutional text
intentionally creates that hold."* **Searched across the whole instrument for hold/block/bar language:
`1` hit — `EC-01`'s *"the Gate remains blocked unless evidence proves the remainder non-gating"*, which is
about unprovable DENOMINATORS, not about `EC-04`.** Plus §10's `RECOMMEND HOLD`, an outcome label.
**`0` texts intentionally create the `EC-04` hold.**

> **Reading A is therefore classified CIRCULAR under the mandated test, with no constitutional text
> creating the hold.**

---

## 6. Why SMEs Core does not adopt Reading C

**It is strongly supported. It is not adopted, for three stated reasons:**

1. **One operative word must be read as subsumed.** §4's `phase` is primary text. An interpretation that
   must discount an operative word is strong, **not proven**.
2. **The instrument defines `Module`, `Phase` and `State` nowhere.** Reading C's location of the Module gate
   at Phase S rests on the *sequence*, not on a definition. **A taxonomy question cannot be closed against
   a taxonomy that does not exist.**
3. **It lands in the gate-opening direction at this transition**, and `06_` §0.8 forbids that shortcut.
   **Publishing the analysis is required; adopting it is not permitted.**

---

## 7. `8C-CLARIFICATION-01` — the smallest possible Boss clarification

> **SMEs Core does not amend the Constitution. This is the exact text proposed for Boss approval.**

```
8C-CLARIFICATION-01 — ADVANCEMENT BOUNDARY AND TOLERANCE-ZERO CLOSURE POINT
Amends: SMEPLUS-DR-EXIT-8C-001 (BOSS APPROVED / PROJECT-WIDE MANDATORY)
Adds a definitions clause and reconciles §4 with §11. Removes nothing.

1. DEFINITIONS. For this Constitution:
   STATE  = a numbered project State (e.g. STATE03).
   MODULE = a domain programme within a State (Account, Inventory, Manufacturing, ...).
   PHASE  = a controlled stage of work inside a Module or State that is NOT itself a
            Module or State boundary.

2. ADVANCEMENT BOUNDARY. The eight Exit Criteria attach at exactly the two gates named in
   §5 and at no other transition:
     (a) the MODULE 8-Criteria Exit Gate, immediately after Module Very Deep Research; and
     (b) the STATE 8-Criteria Exit Gate, after the State Integration Very Deep Review.
   §4's phrase "next controlled phase or State" means the Module's exit transition at (a).
   An internal PHASE transition inside a State is NOT an eight-criteria gate.

3. TOLERANCE-ZERO CLOSURE POINT. EC-04 is closed by EXECUTED RUNTIME PROOF plus independent
   reproduction, evidenced no later than the STATE 8-Criteria Exit Gate. Specification
   evidence NEVER satisfies EC-04. CONDITIONAL PASS may never bypass a tolerance-zero risk
   at either gate.

4. PHASE SA -> PRE-TEST. This transition is an INTERNAL VERIFICATION TRANSITION, not an
   Exit Gate. Phase SA is the State Integration Very Deep Review of §5 and §2.4, and its
   output feeds the STATE gate.

5. NO DUMPING. A current-scope Phase SA specification gap may NOT be carried into Pre-Test.
   Only obligations that REQUIRE execution to discharge may be met in Pre-Test. Any item
   moved forward must be recorded with the evidence proving it is execution-dependent.

6. NO IMPOSSIBLE DEMAND. EC-04 may not be read to require evidence that project governance
   forbids the project from producing at that point. Where a standing veto bars the act that
   would produce the evidence, the closure point is the next gate at which the act is lawful.

7. PRESERVED IN FULL. All eight criteria; EC-07's two consecutive clean structurally
   independent passes before the Final Research Gate; tolerance-zero protection; §10's
   outcome limits; Boss as sole Final Approver.
```

**What it does NOT do:** weaken a criterion · remove `EC-07` · lower the tolerance-zero bar · authorise
Pre-Test entry · rule `FG-F-06` · alter any veto.

---

## 8. Checkpoint

> ## `CP-SA-SC-310 — EXACT BOSS CLARIFICATION READY`
> **11 interpretive factors applied to primary text · **§5's mandatory sequence names both gates and
> locates them — neither is Phase SA → Pre-Test** · question A answered **`C`**; question B answered
> **executed runtime proof + independent reproduction at the State gate, `0` boundaries downgraded** ·
> anti-deadlock test run: **Reading A CIRCULAR**, escape clause searched and **absent** (`1` hold in the
> instrument, and it is `EC-01`'s) · **harmonization NOT adopted** — undefined taxonomy, one word
> subsumed, gate-opening direction · **`8C-CLARIFICATION-01` drafted in 7 clauses, removing nothing** ·
> **the harmonization's uncomfortable consequence published: it relocates an unmet obligation to Phase S's
> already-granted gate.**

No Evidence = No Progress. Never Skip Gate. Do not weaken the standard to open the gate.
Boss remains the sole Final Approver.
