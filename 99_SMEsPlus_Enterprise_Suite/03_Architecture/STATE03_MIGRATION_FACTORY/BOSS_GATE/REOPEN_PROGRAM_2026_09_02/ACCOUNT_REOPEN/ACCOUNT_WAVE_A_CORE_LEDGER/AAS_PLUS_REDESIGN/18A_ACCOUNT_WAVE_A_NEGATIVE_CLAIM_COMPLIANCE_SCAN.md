# 18A — NEGATIVE-CLAIM COMPLIANCE SCAN (SELF-SCAN)

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> Run as a **named, separately-tasked step** per `DR-NC-05`, not as an expectation on the author.
> Rule under test: **`NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST`.** Classes `A`–`E`;
> **`B`/`C`/`D` are never converted to `A`** — not by restatement, citation, or elapsed time.

---

## 1. Mechanical scan

| Item | Result |
|---|---|
| Files scanned | **19** (`00`–`17`, `20`) |
| Scan expression | `does not exist · do not exist · there is no · never · always · only · nothing · anywhere · absent · no carrier · no mechanism` |
| Total occurrences | **186** |
| Occurrences that are **absence assertions** (rest are design imperatives such as *"never silently moves"*) | **24** |
| Vendor-token leak scan — expression held in `mcc_scripts/compliance.sh`, **widened after `RA-28`** to add reference-platform terms the author-chosen expression omitted | **0 hits on the widened expression.** `RA-28` was correct: the first run reported *"clean"* on a pattern **chosen by the author of the claim it bounded** — the denominator rule's `PATTERN` + `INDEPENDENCE` clauses, failed together. 11 occurrences of one omitted term were present and are now scrubbed |
| Prohibited-verdict wording (`PASS · Team B · Team C · development authorisation`) | **0 true hits** (2 false positives: *"pass both the write guard"*, *"independent pass"*) |

---

## 2. Self-caught findings

> **Context that makes these worth reporting rather than silently fixing.** In this programme, across
> five consecutive rounds, **every material correction came from an independent reviewer and none from
> the author.** The closure round's author caught **1 of its own 4** errors. These were caught by the
> author, before independent review returned, by running the scan as a separate task. That is the
> control working as designed — and it is the only reason they are here.

| id | File · line | Defect | Class as cited | Class as restated | Verdict |
|---|---|---|---|---|---|
| `NCS-01` | `13 §1` | *"Two links do not exist in the reference at all"* | `B` — primary tree only; **962 manifested modules unsearched** | reads as `A` whole-system | **UPGRADE — must be corrected** |
| `NCS-02` | `13 L-2` | *"the link that does not exist today"* | `B` | reads as `A` | **UPGRADE** |
| `NCS-03` | `04 §3` | *"there is no temporal validity model anywhere"* — the word *anywhere* is the whole defect | `B` (`VF-03`) | reads as `A` | **UPGRADE** |
| `NCS-04` | `07 §2` | Tenant · *"does not exist"* | `A` **within the primary tree** (`VF-15`) | boundary dropped | **BOUNDARY LOST** |
| `NCS-05` | `02 §2 VF-01` | *"Four identities a ledger needs do not exist"* | `B` for event/source-event; `A`-in-scope for tenant/period | table carries **no class column at all** | **CLASS ABSENT** |
| `NCS-06` | `11 §6` | *"does not exist anywhere in the tree"* | boundary **is** declared (*the tree*) and re-verified | — | **SOUND** — retained as written |
| `NCS-07` | `12 §3` | *"the distinction does not exist"* | `A` in scope — the parent states the reference **cannot answer** Boss question 16 | boundary implicit | **MINOR** — boundary should be explicit |

**5 upgrades or boundary losses. 1 sound. 1 minor.**

### Why `NCS-01`…`NCS-03` matter more than they look

All three rest on the **same** class-`B` negative: *no accounting-event identity and no provenance
carrier exist*. That negative's boundary is **the primary module tree** — and `GB-07`/`MCU-18`
established that **962 manifested modules were never searched**, holding **904 of 906 localisations**.

**`D-01` and `D-04` are the two highest-value designs in this package, and both rest on that
negative.** They are labelled `PROVISIONAL` on the strength of their **positive** evidence —
five verified consequences of the absence (`XM-01`, `GAP-B02`, `EV-012`, `AE-05`, the five unrecorded
lineages) — **not** on the strength of the negative. That distinction must survive into every
restatement, and in three places it did not.

---

## 3. Corrections — status

> **Re-titled after `RB-34`.** This section originally read *"Corrections applied … after independent
> review returned"* — written **before** review had returned, and naming files that still carried the
> uncorrected text. **The file reporting the negative-claim control was itself carrying an unearned
> completion statement — the precise defect class it exists to catch.**
>
> All corrections below have now been applied **and re-verified in the files**. The reviewer-caught
> set is at `18 §3`.

| id | Correction |
|---|---|
| `NCS-01` | Rewritten to *"Two links have **no carrier found in the searched scope** (class `B`, boundary: primary module tree; 962 manifested modules unsearched)"* |
| `NCS-02` | Rewritten to *"the link with no carrier found in the searched scope (class `B`)"* |
| `NCS-03` | *anywhere* → *"anywhere in the searched scope (class `B`)"* |
| `NCS-04` | Boundary restored: *"no tenant concept found in the primary tree (class `A` in scope)"* |
| `NCS-05` | Class column added to the `VF` table in `02 §2` |
| `NCS-07` | Boundary made explicit |

---

## 4. Standing clause

> **Every absence statement in this package is bounded by the searched scope declared in `02 §6`.**
> No statement here asserts that a behaviour is absent from the SMEsPlus target system, from the
> reference system as a whole, or from the 962 manifested modules that no round has searched.
> Where a design rests on an absence, the design's strength derives from the **verified positive
> consequences** of that absence, and the dependency is registered in `01`.

---

## 5. APPENDIX — independent verification of the boundary itself

The boundary every class-`B` negative in this package depends on is *"962 manifested modules were
never searched."* This session re-derived it directly, because a boundary inherited without
verification is exactly the defect the programme keeps finding.

**Scope of this check.** Bounding **this package's own claims** only. It is **not** a re-run of parent
research and does not supersede the parent's enumeration.

| Measure | This session | Parent's figure | Verdict |
|---|---|---|---|
| Manifested modules **outside** the primary module tree | **962** | **962** | **REPRODUCES EXACTLY** |
| Manifested modules **inside** the primary module tree | **790** | **791** | **off by one — `AASR-F-02`** |
| Total manifested modules under the source root | **1,753** | **1,752** | off by one, consistent with the above |

### `AASR-F-02` — a one-module discrepancy in the searched population

`MINOR`. The parent reports **791** searched and **1,752** total; this session's count over the same
root returns **790** and **1,753**. The 962 figure — the one every negative claim depends on —
**reproduces exactly**, so the boundary itself is sound and the design exposure in `01` is unchanged.

The discrepancy is recorded rather than reconciled, for two reasons. It is a **denominator** question,
and `MCC_E` established that **0 of 6 denominator definitions survived challenge** while the *values*
reproduced — this is that pattern again, in miniature: the value is stable, the definition of "one
searched module" is not. And under the independence clause, **the author of a claim does not get to
settle the definition that bounds it.** Routed to the parent, not resolved here.

**Layer note.** The count was taken over a Layer 2 source root. Only the aggregate integers are
reported; **no path, module name, file or code content is transcribed into this Layer 1 package.**

### What this changes

**Nothing is weakened, and one thing is strengthened.** The class-`B` negatives behind `D-01`, `D-04`
and `D-23` are confirmed to sit behind a genuinely unsearched population of **962 modules** — verified
by this session rather than inherited. Those designs remain `PROVISIONAL` / `PROVISIONAL` on
their positive evidence, with the dependency registered at `01 §3`.

**And it corrects a prior programme failure mode by demonstration.** A 2026-09-03 session concluded
*"no source code or database access exists"* after searching only its working tree. **Source access
exists and was used here.** This session did **not** conduct source-level design verification — that is
a deliberate containment choice, not an access limitation, and it is stated as such in `19 §6`.

---

## 6. APPENDIX B — evidence-fidelity corrections (self-caught, beyond negative-claim scope)

While bounding §5, this session read the parent's **own internal challenge section** (`MCC_G §7`) and
found that **six figures and claims carried into this package were the parent's *claimed* values, not
its *reviewed* values.** The parent had already corrected them; this session had copied the headline.

> **This is the restatement defect, committed by this session, against a correction that was sitting in
> the source file.** It is the same failure mode `DR-NC-05` describes — *restatement is where the
> upgrade happens* — applied to positive figures rather than negatives. Recorded in full because the
> programme's record shows self-caught errors are rare.

| id | Claim as first carried | Parent's own reviewed position | Correction |
|---|---|---|---|
| `EFC-01` | Balanced-but-wrong floor **36** | `G-C8`: the establishment test was applied to **3 of 7** new cases; **established floor 32**, four cases re-classified `NOT YET ESTABLISHED` | corrected in `02`, `14`, `20` |
| `EFC-02` | *"16 declared guards that can never execute"* | `G-C7`: **DEFECT CONFIRMED IN SUBSTANCE, OVERSTATED IN WORDING, UNDERSTATED IN POPULATION.** The declarations **do** generate a client-side field domain — the control is **present in the view layer and absent at write**. Population floor **30 across 4 files**, 1 named | corrected in 7 files; `T0-09` now stated as **NOT bounded** |
| `EFC-03` | *"empty constraint definition"* as an inert-control instance | `G-C6`: it is a **deliberate ORM delegation idiom** that registers a post-init assertion. **Instance 2 falls.** The defect is the index's **scope** | corrected in `06`, `12` |
| `EFC-04` | *"the bank path holds the **only** production consumers of the suppression flag"* | `G-C5`: **SCOPE STATEMENT CONTRADICTED.** True of one module, false of the application — **seven** consumers across two modules, one writing a **new accounting date onto a posted deferral reversal** (a **period reassignment**) | corrected in `01`, `07`, `15`, `17` |
| `EFC-05` | Tolerance-zero boundaries **10** | `MCC_G §7`: **two further boundaries** returned by the challenge — the entry-balance invariant enforced in **one currency dimension only**, and the balance assertion **suppressible by context on three shipped production paths** | **12 known, 10 registered**; corrected throughout |
| `EFC-06` | `BW-28` *"no detecting control"* carried as live; `BW-33` graded minor | `G-C2` **withdraws `BW-28`** (class-`A` absence where a class-`B` search finds the control) and replaces it with **`BW-28a`** — whole-entity consolidation at **1.0**. `G-C4` re-grades `BW-33` **MEDIUM** and cross-lists it as a **missing accounting event** | added as `14 §4` |

### The consequential one

`EFC-05` yielded the finding this package would otherwise have missed entirely:

> **`unbalanced-and-posted` is reachable, and the balanced-but-wrong taxonomy has no cell for it.**

It is now `14 §4` (`T-20`) and it is the case that makes `ADR-02`'s storage-level enforcement
decisive rather than merely preferable. **`EFC-04` is the most embarrassing**: this package repeated,
as supporting evidence, a scope statement the parent had explicitly marked `CONTRADICTED` — *"class
`B` presented as `A`, by this round, in the round that convicts its parent of exactly that."* The
sentence was in the file that was being cited.

### Method note

All six were found by reading the **§7 challenge section** of a parent file rather than its
**headline tables**. Every one of the six corrections lived *below* the summary that had been quoted.

> **Design input must be taken from a source's adversarial section, never from its summary.**
> Proposed as a standard delta in `20 §4` and recorded here as this session's own contribution to the
> method — earned by failing at it first.
