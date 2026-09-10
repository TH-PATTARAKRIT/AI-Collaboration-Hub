# SC-EC07-01 — `EC-01`…`EC-08` STATUS UNDER `FG-F-06 = READING A`

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · head consumed `e113258f`
Governing instrument: `SMEPLUS-DR-EXIT-8C-001`, §3, read at primary text on `origin/SMEsPlus`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Self-assessed. NOT independently verified. `Independent Review != Truth. Verified Evidence = Truth
> Basis.`** — the constitution's own words, `EC-07`.

---

## 1. Result

> # `THREE CRITERIA DO NOT PASS. ONLY ONE OF THEM IS EC-07.`

| Criterion | Status | Closable by SMEs Core? |
|---|---|---|
| `EC-01` Scope Bounded | **likely satisfied** | n/a |
| `EC-02` Enumeration Converged | **likely satisfied** | n/a |
| `EC-03` Unknown Exhausted | **likely satisfied** | n/a |
| **`EC-04` Tolerance-Zero Closed** | **DOES NOT PASS** | **NO — needs runtime proof** (§3) |
| **`EC-05` Contradiction Resolution Complete** | **DOES NOT PASS** | **NO — Boss authority** (§4) |
| `EC-06` Negative Claim Controlled | **improved, not clean** | partly (§5) |
| **`EC-07` Two Consecutive Clean Passes** | **DOES NOT PASS — `0 of 2`** | **NO — Boss appoints; a party cannot be independent of itself** |
| `EC-08` Final Knowledge Package Complete | **likely satisfied, with two named absences** | partly (§6) |

> **`B-7` alone does not open this gate.** Boss's instruction addresses `EC-07`. **`EC-04` and `EC-05` fail
> on their own terms and would still fail after two clean passes** — and §3 shows `EC-04` cannot be closed
> on the path Reading A leaves open. **This is the load-bearing finding of this file.**

---

## 2. Criteria that appear satisfied — stated with their basis, not asserted

| Criterion | Basis |
|---|---|
| **`EC-01`** | Every round declares POPULATION / UNIT / PATH SET / PATTERN **and its blind spot as the complement**. No material denominator is left undeclared; the three Pre-Test entry denominators are stated **as sets** including `RC-D-01`'s inverting positive half |
| **`EC-02`** | The decision population converged across **two independent derivations** — `23` with `F5 = 6` — reached from different starting points by two executions and one peer track. `EC-02` warns that *"research is not complete merely because multiple rounds were performed"*; the claim here is **convergence of independently-derived enumerations**, not round count |
| **`EC-03`** | Every open item carries an owner and one of the five permitted dispositions. **`0` unclassified `GATING UNKNOWN`.** `EC-03` forbids using a later-wave route to hide a current-scope blocker — the one relocation (prepaid wallet → `ERPPLUS-152` `G6`) was **re-checked at its own gate** and found genuinely owned there, not parked |

---

## 3. `EC-04` — DOES NOT PASS, and Reading A leaves no path to close it

**The criterion, verbatim:**

> *"All applicable tolerance-zero boundaries must be **evidence-closed** before advancement… **`CONDITIONAL
> PASS` may not bypass a tolerance-zero risk.**"*

**Measured population — every `TOLERANCE-ZERO` marking in the Phase SA corpus: `3`.**

| # | Boundary | Current state | Evidence-closed? |
|---|---|---|---|
| 1 | `CF-I-03` `D3` **cross-tenant** — *"breach → the emitting fact is not emitted; a fact already emitted is flagged and its consumers notified"* | **`SPECIFIED`** (`CP-SA-C4-30` — *"`CF-I-03` SPECIFIED AND LINKED"*). **Not built. Not executed.** | **NO** |
| 2 | The privileged-bypass path enumeration — *"`CRITICAL — TOLERANCE ZERO` in the target architecture"* | specified | **NO** |
| 3 | `SA10` tenant/company boundary matrix — disposition **`TOLERANCE-ZERO — HOLD`** | **explicitly `HOLD`** | **NO** |

> **`0 of 3` are evidence-closed.** A specification is a statement of what the control will do; `EC-04`
> requires evidence that it **does** it. **`CONDITIONAL PASS` is expressly forbidden here**, so "specified,
> proof deferred to Pre-Test" is not an available disposition under Reading A.

### 3.1 `SC-EC-01` — the circularity Boss should see before the passes are commissioned

**Closing `EC-04` requires executing the controls. That path is closed from both ends:**

1. `EC-04` must be **evidence-closed before advancement** — i.e. **before Phase SA exits to Pre-Test**.
2. Executing `CF-I-03` `D3` and the bypass-path controls requires them to be **built**.
3. **Implementation start is barred by `RC-V-01`** — independently of `8C-001`, on either reading — until
   an independent check over the **wider five-row set** is performed.
4. The phase in which these controls are normally proven **is Pre-Test**, which `EC-04` gates.

> **Under Reading A, `EC-04` requires proof that can only be produced after the advancement `EC-04`
> gates.** Two clean independent passes do not break this: **a reviewer can verify that a control is
> specified; a reviewer cannot make it executed.**
>
> **This is not an argument against Reading A.** It is a consequence of Reading A that Boss has not yet been
> shown, and it is **Boss-owned**, because resolving it means either narrowing what *"evidence-closed"*
> requires at an architecture exit, sequencing a bounded build before Pre-Test, or accepting `EC-04` as
> satisfied by specification — **all three are statements about what a Boss ruling covers, and
> `CF-D-01` reserves those to Boss.**

**SMEs Core does not choose among the three, and does not treat `EC-04` as satisfied.**

---

## 4. `EC-05` — DOES NOT PASS, and it is new since the ruling

**The criterion, verbatim:**

> *"Every material contradiction between primary research, source/database/UI evidence, independent
> reviewers, AAS+, PMO, **or prior canonical evidence** must be dispositioned with traceable evidence and
> lineage. **No material contradiction may remain merely as an unresolved difference of opinion.**"*

**The live contradiction:** `SC-BD-01` records **`FG-F-06 = READING B`** and opened the `F1`–`F8` gate;
`SC-CONTRA-01` records **`FG-F-06 = READING A`**, under which that gate was not open. **Both are Boss
decision records in this session, on this branch, on this day, and they are prior canonical evidence in
direct contradiction.**

> **AND IT HAS PROPAGATED.** At `89ba9c7d` the Reading B path recorded **`SC-CONTRA-01`…`SC-BD-10` — 16 of the
> 23 decisions ruled** — plus `SC-11` and `SC-12`, terminating at `TERMINAL D`. **Under Reading A those 16
> rulings were taken inside a gate that was not open** (`03_` prompt §3: *"Do not rule the 23 decisions
> until `EC-07` is satisfied"*). **This file does not challenge their substance and does not touch them.**
> **What it records is that their gate precondition is disputed and undispositioned.**

| | |
|---|---|
| Material? | **Yes — Gate-changing.** Each forecloses what the other authorises |
| Dispositionable by SMEs Core? | **No.** Choosing between two Boss rulings is Boss authority, not an evidence question |
| Effect on `EC-07` | **Decisive** — §7 |
| Prior `EC-05` state | the one live contradiction was `G2` (platform-actor model), **dispositioned** to the `C4-D-02` review. That disposition stands and is unaffected |

---

## 5. `EC-06` — improved, not clean

**The criterion requires every material system-wide negative to *"declare and prove the search boundary
proportional to the claim"*, classified as `VERIFIED ABSENCE` / `NOT FOUND IN SEARCHED SCOPE` /
`NOT YET SEARCHED` / `UNKNOWN` / `CONTRADICTED`.**

**What the record shows:** this session and the peer track between them caught **seven instrument failures
by positive controls** — a dead alternation pattern, a substring/word-boundary pair, a regex complexity
error read as a zero, a path-only output read as hits, a `grep -o` piped to a filter needing the line, a
multi-ref `git grep` returning a false zero including for known-ruled identifiers, and a relative path
reporting 11 good SHAs as broken. **In this file's own §3 a filter excluded a file because the filename
contained the excluded token.**

> **A criterion that keeps catching its own failures is working. It is not thereby passed.** The honest
> classification is that the **control is in force and the corpus has not been swept end-to-end against it
> on one instrument** — `NOT FOUND IN SEARCHED SCOPE`, not `VERIFIED ABSENCE`.
>
> **This is a legitimate target for the independent passes**, and it is named as one in `SC-EC07-02` §4.

---

## 6. `EC-08` — likely satisfied, with two named absences

The constitution's minimum list is met by existing artefacts — semantic model, coverage register,
source-of-truth register, event/state model, dependency map, control matrix, failure/edge register,
unknown register, contradiction register, negative-claim register, evidence manifest with SHA-256, Boss
decision register, clean-room transfer input, final gate report, repo/branch/path/commit.

**Two named absences, stated rather than absorbed:**

| Absence | Status |
|---|---|
| **`ACCOUNTING_INVENTORY_INTERFACE_CONTRACT_AND_CROSS_PROOF`** — mandated by a standing Boss approval | exists in **`0`** corpus paths. It is Boss act `C4-D-01`, uncommissioned |
| **Jira lineage** *("where required by project governance")* | not carried in this package |

**Neither is closable by SMEs Core**: the first is a Boss commissioning act, the second a governance
question about whether it is required here.

---

## 7. `EC-07` — `0 of 2`, and the sequence cannot validly start today

**`EC-07`'s clean-pass criteria, verbatim, include: *"new Gate-changing contradiction."***

> **A Gate-changing contradiction exists *now*, before pass 1** (§4). **Any pass run while it stands is
> non-clean by `EC-07`'s own terms**, and Boss's instruction says such a pass *"restart[s] the consecutive
> clean-pass count."* **Commissioning a reviewer before dispositioning it spends an appointed cycle to
> rediscover a known defect and returns the count to `0`.**

**And two further facts bear on how many passes will be needed:**

1. **`EC-04` fails independently.** A clean pass over a package whose tolerance-zero boundaries are not
   evidence-closed does not make them closed. **Two clean passes would leave `EC-04` exactly where it is.**
2. **Every Phase SA round so far has produced a new material finding class** — including the peer's
   (`AR-F-01`, `AR-F-02`), this executor's (`SC-F-08`, `SC-F-09`, `SC-ADD-01`), and this file
   (`SC-EC-01`). **`EC-07` requires two consecutive passes with none.** Boss should decide, in advance,
   what happens if passes keep finding things — otherwise the count may never reach 2.

---

## 8. What SMEs Core can and cannot close before a reviewer arrives

| Criterion | SMEs Core action available now |
|---|---|
| `EC-01`, `EC-02`, `EC-03` | **nothing further** — assessed satisfied; the reviewer should attack them |
| **`EC-04`** | **nothing.** Needs execution, which needs a build, which `RC-V-01` bars (§3.1) |
| **`EC-05`** | **nothing.** Needs a Boss disposition between two Boss records |
| `EC-06` | **one thing, and it is offered:** a single end-to-end negative-claim sweep of the canonical package on one validated instrument with per-claim classification. **Not run here** — it is exactly the work an independent pass should not inherit from the party it is auditing |
| `EC-07` | **nothing.** Boss appoints; a party cannot be independent of itself |
| `EC-08` | **nothing** — both absences are Boss/governance acts |

---

## 9. Checkpoint

> ## `EC-01…EC-08 STATUS UNDER READING A — 3 CRITERIA DO NOT PASS`
> **`EC-04` `0 of 3` tolerance-zero boundaries evidence-closed, and Reading A leaves no path to close them
> (`SC-EC-01`) · `EC-05` open on a Gate-changing contradiction between two Boss records · `EC-07` `0 of 2`
> and unable to start clean while `EC-05` stands · `EC-06` `NOT FOUND IN SEARCHED SCOPE`, not
> `VERIFIED ABSENCE` · `EC-08` satisfied with two named absences, both Boss acts · **`0` criteria closable
> by SMEs Core** · no `PASS` declared on any criterion · Phase SA not closed.**

No Evidence = No Progress. Never Skip Gate. `CONDITIONAL PASS` may not bypass a tolerance-zero risk.
Boss remains the sole Final Approver.
