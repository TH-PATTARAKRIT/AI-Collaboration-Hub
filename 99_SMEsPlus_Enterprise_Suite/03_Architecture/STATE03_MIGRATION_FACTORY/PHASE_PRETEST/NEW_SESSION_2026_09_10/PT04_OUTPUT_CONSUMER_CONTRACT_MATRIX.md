# PT-04 — OUTPUT / CONSUMER CONTRACT MATRIX

## `CP-PT-04 — OUTPUT HANDOFF INCOMPLETE, BOUNDED`

*(master-prompt checkpoint name: `CP-PT-04 — OUTPUT HANDOFF COMPLETE`; the evidence does not support `COMPLETE` — §8)*

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `ed5efab8`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`0 of 18` cross-module contracts proven · `0 of 10` handoffs element-10 compliant · `6` vetoes in force.**

---

## 1. Result

| | |
|---|---|
| Boss-ruled boundary denominator | **`12`** (`SC-BD-02`, `XMC-D-02 = EXTEND TO ALL BOUNDARIES`) |
| **Is the set of `12` actually declared anywhere?** | **NO** — `PT04-F-01`, **MATERIAL** |
| Competing enumerations of the same subject found | **`3`** — `12`, `18`, `10` |
| Cross-module handoff register that exists but never reached the handoff | **`HX-01`…`HX-31`** — `PT04-F-02`, **MATERIAL** |
| `18`-handoff contract state | **`0 PROVEN` · `2 NOT APPLICABLE` · `16 HOLD — EXACT GAP`** |
| `10`-row tenant/company contract state | **`2 CONTRACT-SUFFICIENT` · `8 CONTRACT-GAP`** |
| Element 10 handoff compliance | **`0 of 10`** |
| **Outputs with no identified consumer** | **`4`** — enumerated at §6 |
| Consumers with no identified producer | **`1`** |
| **`CP-PT-04` disposition** | **`INCOMPLETE — BOUNDED`**, §8 |

---

## 2. `PT04-F-01` — MATERIAL: the ruled denominator is `12`, and the set of `12` is never declared

### The ruling

`SC-BD-02` §2 and §7, verbatim:

> *"One **general** contract with **declared per-boundary applicability** … The boundary denominator moves
> **1 → 12**."*
> *"The Pre-Test Matrix element-contract denominator is **fixed at 12 boundaries, declared as a set**."*

**And its binding condition (`SC-SMT-08`):** *"an applicability declaration is **part of the contract
amendment and carries the contract's authority**. **A boundary may propose; it may not declare.**"*

### The measurement

**POPULATION:** every `.md` under `99_SMEsPlus_Enterprise_Suite`. **UNIT:** one file enumerating the set.
**PATTERN:** `Asset → Accounting` / `Asset -> Accounting` (a member that appears in no other context).

| Question | Result |
|---|---:|
| Boundary names inside `SC-BD-02` itself | **`0`** |
| *"boundar"* inside `SC-BD-02` (**positive control**) | **`7`** — the file **is** about boundaries; it simply never names them |
| Any `SC-*` continuation file enumerating the set | **`0`** |
| Any Pre-Test file enumerating the set | **`0`** |
| Corpus-wide files enumerating it | **`4`** — and **`2` of those are prompts, not evidence** |

### The three competing enumerations

| Where | Count | Character |
|---|---:|---|
| CORR3 master **prompt** §11 | **`12`** | the only 12-member list — and it is prefixed ***"At minimum test:"***, i.e. **explicitly not a closed set**. The token `12` never appears in §11 |
| `SA_CORR3_08` §2.5 register `XMC-H-01`…`XMC-H-18` | **`18`** | the register actually **tested**, *"each exactly once"* |
| CORR4 prompt §4.3 and `SA_CORR4_02` §5 | **`10`** | **different membership** — adds `Purchase → Inventory`, collapses AR/AP/Payment/Bank into one, **drops `Close →`** |

### Why it is material

**Boss fixed a denominator by number and the set was never written down.** Three consequences follow, and
each is testable:

1. **The applicability declaration `SC-SMT-08` requires cannot be made.** A per-boundary declaration
   presupposes an enumerated set of boundaries. **There is nothing to declare against.**
2. **`12` is derived from a list its own author marked *"at minimum"*.** A minimum is a **floor**, not a
   denominator. **Fixing a denominator to a floor converts an open set into a closed one by transcription.**
3. **The registers that did the work use `18` and `10`, not `12`.** A Pre-Test matrix built over `12`
   would not reconcile to either.

> **This is the programme's recorded *scope stated as a description* defect, at the boundary layer.**
> A boundary set was **described** — *"all boundaries"*, *"12"* — where it needed to be **declared as an
> enumerated set with a membership rule**.

### Disposition

| | |
|---|---|
| Status | **OPEN — MATERIAL** |
| Owner | **Boss / PMO** — this session **may not** declare the set: `XMC-D-02` is a **ruled** decision and re-scoping a ruled denominator is expressly prohibited (`SC-59` §9) |
| What this session did | **carried `12` as the ruled number and recorded that its membership is undetermined.** `PT-02` cited the bare `12`; that citation is **now qualified by this finding** |
| Routed to | `PT-11` (authority register) · `PT-13` · **`PT-14` B-7** |
| What would close it | Boss or PMO publishing the enumerated `12`, **or** ruling which of `12`/`18`/`10` is the denominator |

---

## 3. `PT04-F-02` — MATERIAL: a 31-row handoff register exists, was opened once, and was dropped before the handoff

### What exists

`10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md`, blob `7bb74dd1`, Jira `ERPPLUS-139`:

> Status: `SMEsPlus-OWNED HANDOFF DESIGN — BUSINESS FACTS ONLY — CLOSES NO JOINT OR ACCOUNTING DECISION`

**`31` rows `HX-01`…`HX-31`** — verified: `31` table rows, `31` distinct identifiers, no gap, no duplicate.
Each carries **From → To · the fact handed over · the trigger · the receiver's obligation · a class**.
**It is Layer 1, SMEsPlus-owned, and it covers precisely the boundaries `PT-04` must contract.**

**Its coverage spans the boundaries the `12`-set names:** Sales↔Inventory (`HX-01`…`03`, `30`),
Purchase↔Inventory (`HX-04`…`06`), Inventory→Accounting (`HX-07`, `09`…`12`, `14`, `17`, `20`),
Accounting→Inventory (`HX-08`, `13`, `15`, `16`, `31`), Manufacturing↔Inventory (`HX-18`, `19`),
inter-warehouse (`HX-21`), **inter-company (`HX-22`)**, Migration (`HX-23`…`25`),
reporting/audit/tax (`HX-26`…`28`), point-of-sale (`HX-29`).

### Where it lives, and where it does not

| Location | Present? |
|---|---|
| Working tree | **NO** |
| `origin/SMEsPlus` (canonical branch) | **NO** — `0` files under `FINAL_SOLUTION/INVENTORY` |
| `origin/design/inventory-final-solution-v1-2026-09-02-001` | **YES** |
| `origin/design/inventory-final-solution-v2-2026-09-02-001` | **YES** |

### Consumption, measured per package — the sharper finding

**UNIT:** one file citing a word-bounded `HX-nn`. **Positive control:** `XMC-H-nn` → `2` files in CORR3.

| Phase SA package | Files citing `HX-nn` |
|---|---:|
| `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08` | **`0`** |
| `PHASE_SA_CORR2_*` | **`0`** |
| `PHASE_SA_CORR3_*` | **`1`** ← discovered here (`XMC-F-01`) |
| `PHASE_SA_CORR4_*` | **`2`** ← used here |
| `PHASE_SA_CORR5_*` | **`0`** |
| **`PHASE_SA_FINAL_BOSS_GATE_2026_09_09`** | **`0`** ← **the package that produced `SA15`/`SA17` `FINAL_CONTROLLED_V2`** |

> **The received finding was *"Phase SA never opened it."* That is no longer the accurate statement, and
> the accurate one is worse: it was opened at CORR3, used at CORR4, and then dropped — **`0` citations in
> CORR5 and `0` in the final package.** The artefact that hands work to Pre-Test carries **no reference to
> the only 31-row cross-module handoff register the programme owns.**

**The correction matters in both directions:** `XMC-F-01`'s measurement was scoped to *"the two Phase SA
packages"* and was correct **within that scope**. Quoting it today, unqualified, would state something
false. **A scoped negative stops being true when the scope moves.**

### The register's own internal counting defect

`§3` roll-up: `INV-OWNED 14` · `ACCT-IF 7` · `JOINT 9` · `TAX-HOLD 4` = **`34` class-assignments over
`31` rows**.

- `HX-12`, `HX-14`, `HX-20` are each split across two classes (*"(part)"*, *"eligibility parts"*,
  *"statutory part"*) — legitimate overlap, provided the unit is stated.
- **But `TAX-HOLD`'s own list reads *"`HX-12` (statutory part), `27`, `28`, and the destruction-evidence
  part of `12`"* — `HX-12` counted TWICE inside a single class of `4`, which therefore covers only `3`
  distinct rows.**

**Unit conflation: `class-assignment` vs `row`, plus a double-count within one class.** Recorded; **not
repaired here** — the file is on a design branch this session must not write to.

### Disposition

| | |
|---|---|
| Status | **OPEN — MATERIAL** |
| Recommendation | **`PT-12` builds its consumer contracts over `HX-01`…`HX-31` as a candidate input**, marked `PTE-1` and **explicitly not authority** (the register closes no joint or accounting decision, by its own status line) |
| Prohibition observed | this session **does not** merge, move or rewrite the register, and **does not** treat it as design authority |
| Routed to | `PT-12`, `PT-13`, **`PT-14` B-7** |

---

## 4. Output → consumer contract state, as measured

### 4.1 The `18`-handoff register (`XMC-H-01`…`XMC-H-18`)

| Class | Members | n |
|---|---|---:|
| `PROVEN` | — | **`0`** |
| `NOT APPLICABLE — EVIDENCE-BACKED` | `XMC-H-15`, `XMC-H-16` | **`2`** |
| **`HOLD — EXACT GAP`** | `XMC-H-01`…`14`, `17`, `18` | **`16`** |
| Total | each exactly once | **`18`** ✔ |

**`0 + 2 + 16 = 18`** ✔ — arithmetic and identifier enumeration both check.

### 4.2 The `10`-row tenant/company handoff contract (`SA_CORR4_02` §5)

| Class | n |
|---|---:|
| `CONTRACT-SUFFICIENT` | **`2`** — flows `5` and `10`, *"the two where **Inventory is the emitting party**"* |
| **`CONTRACT-GAP`** | **`8`** |
| `NOT APPLICABLE` / `RESEARCH REQUIRED` | `0` / `0` |
| Total | **`10`**, each classified once ✔ |

> **The only two sufficient rows are the ones where Inventory emits** — i.e. exactly the boundary the
> original 16-element contract was scoped to. **Contract sufficiency tracks the historical scope, not the
> ruled `12`.** That is corroborating evidence for `PT04-F-01`.

### 4.3 Element 10 compliance

**`0 of 10` material handoffs contract-compliant** (`SA10` §7). **`0 of 13` enforcement surfaces verified.**

---

## 5. `PT02-F-01` carried forward — `producer → ∅` is a distinct failure class

`PT-02` raised `X-07`'s `R-17 NO CONSUMER` and required `PT-04` to test **producer→∅** as its own class,
not only consumer→missing-input. **Doing so found it is not one case.**

---

## 6. Outputs with no consumer — enumerated

| # | Output | Source |
|---:|---|---|
| 1 | **Commercial-terms freeze flag** | `SA03` |
| 2 | **Remaining-supply record** | `SA03`; = `X-07`'s `R-17 NO CONSUMER` |
| 3 | **Sub-location resolution** | `SA03` |
| 4 | **`XMC-H-09` Asset → Equipment** | `SA_CORR3_08` §2.5 — *"Capitalization evidenced; **derecognition `PARTIAL`**; the **Equipment consumer has no evidenced route**"* |
| — | **Consumer with no producer:** *Customer-invoice lifecycle state* — *"Nobody → input"* | `SA03` |

**`4` outputs with no consumer · `1` consumer with no producer.**

> **`SC-45` §2 records `XMC-H-09` as *"the one recorded missing consumer"*.** Against `SA03`'s own status
> line — *"three outputs have no identified consumer and one consumer has no identified producer"* — **the
> true figure is `4`, not `1`.** `SC-45`'s claim is exact **as written** (*"the one **recorded**"*, i.e.
> recorded in the `XMC-H` register), and it is **read** as the total. **The `XMC-H` register and `SA03`
> were never reconciled to one another.**

| | |
|---|---|
| `PT04-F-03` | **MATERIAL — missing-consumer population understated `1` vs `4` when the two registers are read together** |
| Status | OPEN — routed to `PT-13` and B-7 |
| Note | this session does **not** re-grade either register; it reports that their **union** was never taken |

---

## 7. What `PT-12` must carry on every material row

Derived from the 16-element contract's `P1`–`P7` proof standard (`SA_CORR3_08` §1.3):

1. upstream output **named by its owner** in the owner's own vocabulary (`P1`);
2. downstream required input **named by its consumer** (`P2`);
3. the two established as **the same fact at business-semantic level**, by reading both primaries — **not
   by two registers agreeing** (`P3`);
4. the route justified by **Business Nature**, not module name (`P4`);
5. **every** consumer enumerated — **a missing consumer is a defect** (`P5`);
6. the consumer can **join** the fact to its origin, its correction, and the other half of the same
   commercial act, **by an identity surviving retry, replay and reversal** (`P6`);
7. each applicable element **supplied, or `N/A` with reason, or `HOLD / EVIDENCE REQUIRED`** (`P7`).

**`P6` is unsatisfiable today for every row** — the joining identity is element 15, specified and not built.

---

## 8. Why the disposition is `INCOMPLETE — BOUNDED`

| Test | Result |
|---|---|
| Is every output's consumer identified? | **NO** — `4` outputs have none |
| Is the boundary set over which contracts are owed known? | **NO** — `PT04-F-01` |
| Are the contracts proven? | **NO** — `0 of 18` |
| Is every gap **named, owned and classified**? | **YES** |

**`CP-PT-04` is recorded as `OUTPUT HANDOFF — INCOMPLETE, BOUNDED`.** The checkpoint's nominal title is
*"OUTPUT HANDOFF COMPLETE"*; **the evidence does not support the word `COMPLETE`, and the title is not
allowed to grade the evidence.**

---

## 9. Checkpoint

> ## `CP-PT-04 — OUTPUT HANDOFF INCOMPLETE, BOUNDED`
>
> **`PT04-F-01` MATERIAL — Boss fixed the boundary denominator at `12` *"declared as a set"* and **the set
> is declared nowhere**: `0` boundary names in the ruling (positive control `7`), `0` in any `SC-*` or
> Pre-Test file; the only 12-member list is in a **prompt**, prefixed ***"At minimum test"***; the
> registers that did the work use **`18`** and **`10`** ·
> **`PT04-F-02` MATERIAL — a `31`-row SMEsPlus-owned handoff register (`HX-01`…`HX-31`) exists on two
> design branches, was opened at CORR3, used at CORR4, and cited `0` times by CORR5 and `0` times by the
> package that produced the Pre-Test handoff** ·
> **`PT04-F-03` MATERIAL — missing consumers are `4`, not the `1` the summary carries; `XMC-H` and `SA03`
> were never reconciled** ·
> `0 of 18` contracts proven · `2 CONTRACT-SUFFICIENT / 8 CONTRACT-GAP` · `0 of 10` element-10 compliant ·
> **`P6` unsatisfiable on every row until element 15 is built.**
>
> **`0` ruled denominators re-scoped · `0` registers rewritten · `0` design branches touched.**

Next checkpoint: `PT-05 — Routing and Business-Nature Proof`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass. A missing consumer is a defect.
Boss remains the sole Final Approver.
