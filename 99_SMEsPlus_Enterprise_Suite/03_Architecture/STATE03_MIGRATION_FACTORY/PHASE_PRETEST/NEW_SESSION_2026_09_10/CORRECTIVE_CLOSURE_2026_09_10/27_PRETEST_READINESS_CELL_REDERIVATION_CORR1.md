# 27 — READINESS CELL RE-DERIVATION — `CORR1`

# `18 WRITABLE / 4 GATED / 0 NOT ESTABLISHED`

## `CHECKPOINT C (part 1) — DERIVED FROM ZERO, NOT FROM 19/2/1`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7-RETURN-CORR1-001]` · Boss: **SOLE FINAL APPROVER**

> **§4: *"Do NOT start from `19/2/1`."* — obeyed. The prior split is not an input to this file; it appears
> only in the `prior grade` column, for comparison after the fact.**
> **`19 / 2 / 1` is SUPERSEDED. It is not deleted — `01_` §3.2 and `02_` §3.1 remain Audit Lineage.**

---

## 1. Method, stated before the result

**POPULATION:** the `22` Boss-approved cross-proof scenarios, blob `a1fc7cd6` (`ERPPLUS-140`).
**UNIT:** one dimension cell. **`22 × 9 = 198` cells.**
**GOVERNING REGISTER:** `SA_CORR5_10_22_SCENARIO_FINAL_RECONCILIATION.md` §4 — the latest artefact on the
*dimension-grade* claim.
**RULING SET TESTED AGAINST:** `SC-BD-02`, `-03`, `-05`, `-06`, `-07`, `-08`, `-09`, `-10`; `BD-ACC-01`,
`-02`, `-03A`, `-03B`; the `B1`…`B10′` application at `22_`; and `SC-SMT-01`…`-11` as **conditions
accepted on those rulings**.

**The derivation rule, stated so it can be attacked:**

> **A cell is `C` when the business fact and its governing rule are both stated. A `B` cell becomes `C`
> only when (a) the gating decision is RULED, **and** (b) the ruling's CONSEQUENCE for that cell's
> expected value is derivable from the ruling text without a further election.**
>
> **Clause (b) is new in this round.** `01_` §3 tested only clause (a) and then attached clause (b) as a
> qualification two lines below the grade (*"Expected values must be taken from the ruling text"*).
> **A qualification that would change a grade is not a qualification; it is part of the test.** This is
> the substance of `B7-F-04`.

**Scenario grade (`PT`):** `WRITABLE` if every cell is `C`; `GATED` if any cell is `B`;
`NOT ESTABLISHED` if any cell's gating decision cannot be located in authority.

**`S` markers do not gate `PT`.** `SA_CORR5_10` §2: *"An `S` is a statutory evidence hold, not a Phase SA
gap."* Rows `13` and `19` carry `S` inside `C` and were `WRITABLE` before any ruling. **The convention is
preserved unchanged, and is declared here rather than assumed.** The statutory exposure travels at `36_`.

### 1.1 Treatment of the `185` `C` cells — declared, not silently bulk-passed

**`13` cells are `B` and are re-derived individually at §3. The remaining `185` are `C`.**
**Re-deriving a `C` cell means re-testing whether a business fact and its rule are stated — a Phase SA
act, closed at `SA_CORR5_10` and not re-openable by a Pre-Test round (`§20` controlled supersession).**
**What this round tested on the `185` is the only thing a ruling could have changed: whether any
2026-09-10 ruling *introduced* a new election into a cell previously graded `C`.**

```
INSTRUMENT: for each of the 8 ruling records SC-BD-02..-10, extract every decision ID ruled,
            then match against the gating decision named in each of the 22 rows' basis notes.
RESULT:     0 rulings introduce a new election. Every ruled ID either (i) closes an existing B cell,
            or (ii) is already reflected in a C cell's basis (BD-ACC-01/-02/-03A/-03B, pre-2026-09-10).
POSITIVE CONTROL: CC-D-01 (ruled at 22_ §3) DOES reach row 18 — and row 18's OUT cell was already B.
                  The instrument finds a ruling that touches a row when one exists.
```

**`185 C` cells carried forward unchanged, on a stated and tested ground. `0` `C` cells re-graded.**

---

## 2. The `198` cells — full grid

**`C` = 185 · `B` = 13 · `G` = 0. `S` markers (9) sit inside cells and are shown as `·S`.**

| # | Scenario | SEM | IN | OUT | RT | IC | AC | TC | ID | AU | **PT `CORR1`** |
|---:|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| 1 | Stockable purchase receipt → handoff | C | C | C | C | C | **C**·S | C | C | C | **WRITABLE** |
| 2 | Vendor bill, receipt timing variation | C | C | C | C | C | **C**·S | C | C | C | **WRITABLE** |
| 3 | Stockable sales delivery → cost handoff | C | C | C | C | C | **C**·S | C | C | C | **WRITABLE** |
| 4 | Customer invoice, delivery timing variation | C | C | C | C | C | **C**·S | C | C | C | **WRITABLE** |
| 5 | Partial receipt | C | C | C | C | C | **C**·S | C | C | **C** | **WRITABLE** |
| 6 | Partial delivery | C | C | C | C | C | **C**·S | C | C | C | **WRITABLE** |
| 7 | Backorder | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| **8** | **Purchase return** | C | C | C | C | C | **`B`** | C | C | C | **`GATED`** |
| **9** | **Sales return** | C | C | C | C | C | **`B`**·S | C | C | C | **`GATED`** |
| 10 | Cancellation before physical execution | C | C | C | C | C | C | C | C | **C** | **WRITABLE** |
| 11 | Correction after physical execution | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| 12 | Inventory count / adjustment | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| 13 | Scrap / damage / write-off | C | C | C | C | C | C·S | C | C | C | **WRITABLE** |
| 14 | Internal warehouse transfer | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| 15 | Multi-company / tenant boundary | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| **16** | **Manufacturing RM → WIP → FG** | C | C | C | C | C | **`B`** | C | C | C | **`GATED`** |
| **17** | **Manufacturing reversal / scrap / variance** | C | C | C | C | C | **`B`** | C | C | C | **`GATED`** |
| 18 | Stockable vs consumable vs service routing | C | C | **C** | C | C | C | C | C | C | **WRITABLE** |
| 19 | Period-end / cut-off | C | C | C | C | C | C·S | C | C | C | **WRITABLE** |
| 20 | Historical migration across fiscal years | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| 21 | AI migration mapping + reconciliation | C | C | C | C | C | C | C | C | C | **WRITABLE** |
| 22 | Retry / idempotency / replay | C | C | C | C | C | C | C | C | C | **WRITABLE** |

**Cell tally after re-derivation: `C` = `194` · `B` = `4` · `G` = `0` · `S` markers `9`. `198` ✔**
*(`13 B` → `4 B`: nine `B` cells closed by ruling — `AC` on rows 1–6, `AU` on rows 5 and 10, `OUT` on row 18.)*

---

## 3. The gated and formerly-gated cells — every one derived individually

| Cell ID | Scen. | Dim | Latest governing source | Latest Boss ruling | Expected-value consequence | Prior grade | B-7 objection | **Fresh grade** | Reason |
|---|---:|---|---|---|---|---|---|---|---|
| `C-01-AC` | 1 | AC | `SA_CORR5_10` §4 r1 | **`SC-BD-05`** `JT-04` = physical movement, `2 of 2` | **Derivable.** `SC-BD-05` §7: *"It fixes expected values: the `10 of 22` scenarios carrying `expected value pending` can now be valued on the movement basis"* | `B` | none | **`C`** | (a) ruled **and** (b) consequence stated by Boss in the ruling itself |
| `C-02-AC` | 2 | AC | " | " | Derivable. `A16` prior-period attribution is a **candidate rule with a statutory `S`**, not a Boss election | `B` | none | **`C`** | as above; `S` does not gate `PT` (§1) |
| `C-03-AC` | 3 | AC | " | " | Derivable | `B` | none | **`C`** | as above |
| `C-04-AC` | 4 | AC | " | " | Derivable. `B2` publishes at *posted* — one `JT-04` option, now the ruled one | `B` | none | **`C`** | as above |
| `C-05-AC` | 5 | AC | " | " | Derivable | `B` | none | **`C`** | as above |
| `C-06-AC` | 6 | AC | " | " | Derivable | `B` | none | **`C`** | as above |
| **`C-05-AU`** | **5** | **AU** | `SA_CORR5_10` §5 `C10-A3`; **`SA_FINAL_03` §2 `F2` card**; `SC-01` §2; `SC-29`; **`SA17 V2` §2d** | **`SC-BD-07`** — `F2` = **`BLOCK`**, *"on all three members, ruled once as a principle"*, `3 of 3`, **`NOT ruled: none`**, §3 expressly rejecting a per-member split | **Derivable: the over-receipt tolerance default is `refuse`.** Identical to the SMEs Core recommendation, now on Boss authority | **`NOT ESTABLISHED`** | `B7-F-03` — the `NOT ESTABLISHED` grade rests on a membership test the ruling's structure defeats | **`C`** | **`CC-F-01` is DISPROVED (`26_` §3.1).** The `3` members ARE enumerated — `SA_FINAL_03` §2 names all three; **`SC-01` and `SC-29` name them inside `CC-F-01`'s own declared search population**; `SC-29` lists the tolerance default under ***"Already ruled and controlling"***. `SA17 V2` §2d independently maps `F2 → rows 5, 10` |
| **`C-08-AC`** | **8** | **AC** | `SA_CORR5_10` §4 r8 | **`SC-BD-05`** `JT-05` = **original cost**, `2 of 2` | **NOT derivable under `Average`.** `SC-SMT-01`: *"`JT-05` → original cost leaves a residual under `Average` costing that nothing in the recommendation places … **incomplete as written**"*; `SC-BD-05` §8.1: *"a **live obligation, not a closed condition**"*, owner **Boss** | `WRITABLE` (`B → C`) | `B7-F-05` — the listed dependency was closed by the same ruling; the live one is missing | **`B`** | Clause (a) met, **clause (b) fails**. `BD-ACC-03B` puts `Average` in scope by Product Category, so a return-reversal case for an `Average`-costed category **cannot state its expected accounting result**. Gating decision: **`SC-SMT-01`**, `BOSS-ONLY DECISION`, OPEN |
| **`C-09-AC`** | **9** | **AC** | `SA_CORR5_10` §4 r9 | **`SC-BD-05`** `JT-05` | **NOT derivable under `Average`** — identical basis to row 8; `SC-SMT-01`'s subject is *"a **returns-costing difference**"*, generic to `JT-05` and therefore to **both** return rows | `WRITABLE` (`B → C`) | `B7-F-04` — graded `WRITABLE` while the row itself records an open Boss decision | **`B`** | as row 8. **The `02_` asymmetry — the residual noted on row 9 only — is corrected: it attaches to both** |
| `C-10-AU` | 10 | AU | `SA_CORR5_10` §4 r10 | **`SC-BD-07`** `XD1-P1` = **`BLOCK`** | Derivable. `M-1`…`M-6` bind on every branch and the ruled branch fixes the expected outcome (`SC-BD-07` §7) | `B` | none | **`C`** | (a) and (b) both met |
| **`C-16-AC`** | **16** | **AC** | `SA_CORR5_10` §4 r16 | **`B-6` PARTLY** — `POH-D-06` ruled (`SC-BD-06`), **`POH-D-01` ruled (`B1`)**, **`POH-D-02` WITHHELD**, **veto limb 2 OUTSTANDING** | **NOT derivable.** Absorption method unruled; limb 2 *"cannot be discharged in either direction as written"* (`SC-42` §2) | `B` | none — B-7 upheld this at `T2` | **`B`** | `2` of `4` bundle components remain; one is undischargeable as worded and is **AAS+ issuer authority**, not Boss's alone |
| **`C-17-AC`** | **17** | **AC** | `SA_CORR5_10` §4 r17 | **`B-6` PARTLY** | NOT derivable — same bundle | `B` | none | **`B`** | as row 16 |
| `C-18-OUT` | 18 | OUT | `SA_CORR5_10` §4 r18 | **`SC-BD-02`** `XMC-D-02` (`2 of 2`) + **`SC-BD-08`** `XMC-D-01` (`1 of 1`, *"leaves the Boss decision list entirely"*) + **`CC-D-01`** ruled at `22_` §3 | Derivable. Precedence ruled (Option 3); Service satisfies `ND-09` via branch 2 (Option B) | `B` | none | **`C`** | all three elections ruled. **`IR-17` remains `PARTIAL` explicitly and is not converted** |

---

## 4. Recomputed totals — from cell membership, not carried

| Class | Members (named) | n |
|---|---|---:|
| **`WRITABLE`** | `1`, `2`, `3`, `4`, `5`, `6`, `7`, `10`, `11`, `12`, `13`, `14`, `15`, `18`, `19`, `20`, `21`, `22` | **`18`** |
| **`GATED`** | `8`, `9` (**`SC-SMT-01`**) · `16`, `17` (**`B-6`**) | **`4`** |
| **`NOT ESTABLISHED`** | — | **`0`** |
| **Total** | | **`22`** ✔ |

### 4.1 Movement against the superseded split

| | `SA_CORR5_10` | `01_`/`02_` (superseded) | **`CORR1`** |
|---|---:|---:|---:|
| `WRITABLE` | `10` | `19` | **`18`** |
| `GATED` | `12` | `2` | **`4`** |
| `NOT ESTABLISHED` | `0` | `1` | **`0`** |

**Membership changes against `19/2/1` — the point of the exercise:**

| Scenario | `19/2/1` | **`CORR1`** | Why |
|---|---|---|---|
| **`5`** | `NOT ESTABLISHED` | **`WRITABLE`** | `CC-F-01` disproved; `F2` membership enumerated in six sources |
| **`8`** | `WRITABLE` | **`GATED`** | `SC-SMT-01` open; expected value not derivable under `Average` |
| **`9`** | `WRITABLE` | **`GATED`** | as row 8 |

> **Three of twenty-two members changed class, in both directions, and the total moved by one.
> A reader comparing `19` with `18` would see a rounding difference. The matrix changed materially.**
> **This is `B7-F-06` demonstrated rather than argued.**

---

## 5. What this does NOT establish

| | |
|---|---|
| Runtime proof | **`0 of 22` verified — UNCHANGED.** This file moves writability, not proof |
| Ratification | **`B5′` remains `NO RULING`.** `18/4/0` is a SMEs Core derivation, exactly as `19/2/1` was. **It is not authority and must not be cited as one** |
| Exit condition `2` | satisfied by the **act** of re-derivation, not by the **truth** of its output — see `31_` and `B7-F-13` |
| `S` markers | `9` statutory holds remain open inside `C` cells and are carried at `36_`; **none is answered** |
| `IR-17` | `PARTIAL` — **explicitly not converted**, per `CC-D-01`'s own Boss constraint |

**Round-2 attack targets this file creates, named by the author:**

1. **Clause (b) itself.** If `WRITABLE` means only *"a case can be written"*, an unresolvable expected
   value for **one** costing method might not gate a scenario whose method is a case parameter. **A
   challenger holding that view would grade rows 8 and 9 `WRITABLE` and reach `20/2/0`.** The counter-
   argument is stated at §3 and is not hidden: the register's unit is the **scenario**, and no row
   declares costing method as a parameter.
2. **The `185` `C` cells.** §1.1 tested only whether a ruling *introduced* an election. It did not
   re-derive business-fact sufficiency, and says so.
3. **`C-05-AU`.** The disproof of `CC-F-01` rests on documents outside the original search population.
   A challenger should verify that `SA_FINAL_03`'s `F2` card is not itself superseded.

---

## 6. Checkpoint

> ## `CHECKPOINT C (part 1) — READINESS RE-DERIVED FROM ZERO`
>
> **`198` cells; `13 B` → `4 B`; `0 G` · **`18 WRITABLE / 4 GATED / 0 NOT ESTABLISHED`**, recomputed from
> named membership · **`3` scenarios changed class in `2` directions while the total moved by `1`** ·
> the derivation rule now tests the ruling's **consequence**, not only its existence — the change that
> re-grades rows `8` and `9` · **`CC-F-01` disproved and withdrawn, emptying the `NOT ESTABLISHED` class** ·
> `0 of 22` runtime-verified, unchanged · `B5′` still unruled, so this figure is a derivation, not authority ·
> `3` Round-2 attack targets named by the author.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
