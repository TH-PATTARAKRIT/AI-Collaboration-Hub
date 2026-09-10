# PT-16 — BOSS FUNCTIONAL-DESIGN ENTRY GATE PACK

# `RECOMMEND HOLD — MATERIAL PRE-TEST GAP`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `bc93cac3`
Executing body: **SMEs CORE** · **Boss: SOLE FINAL APPROVER — AI/PMO MAY RECOMMEND ONLY**
Date: `2026-09-10`

> **Phase Pre-Test executed `PT-00` → `PT-15`. `CP-PT-14` was NOT reached — B-7 has not run.**
> **`EC-04` `0/3` · `EC-07` `0/2` · `6` vetoes in force, `0` discharged · `0 of 48` scenarios verified.**
> **No `PASS` is declared. Phase SA is not closed. The State gate is not passed.**

---

## 1. The recommendation, and the one test that produced it

**The master prompt's question 10 for this phase:**

> ***"Can Functional Design begin without inventing missing business semantics?"***

**Answer: NO — on `5` counted items.** Each is a **business semantic or a scope declaration that must
exist BEFORE design**, not a deliverable design produces.

| # | Gap | Why Functional Design cannot proceed without it |
|---:|---|---|
| **1** | **The `12`-boundary set is never declared** (`PT04-F-01`) | Boss fixed the denominator at **`12` "declared as a set"**; the set is declared **nowhere** (`0` boundary names in the ruling, positive control `7`). The working registers used **`18`** and **`10`**. **Design would build cross-module contracts over an unknown boundary population.** A per-boundary applicability declaration — an outstanding **SMEs Core** obligation (`SC-11` §6 #5) — **cannot be written against a set that does not exist** |
| **2** | **`4` outputs have no consumer** (`PT04-F-03`) | Commercial-terms freeze flag · remaining-supply record · sub-location resolution · `XMC-H-09` Asset→Equipment. **A missing consumer is a defect by the contract's own `P5` clause.** Design cannot invent who receives a business fact |
| **3** | **The composed correction case is unspecified** (`PT09-F-02`) | Ship → invoice → **return after period close** → **a downstream module already consumed the original**. Three open items, each recorded separately; **their composition is recorded nowhere**, and it is an ordinary SME transaction |
| **4** | **The material-flow enumeration is short by at least one** (`PT05-F-03`) | `XMC-F-14`: migration flows are absent from all four flow registers (positive control **`11`** files). **Design would work from a flow population known to be incomplete** |
| **5** | **Product-classification tie-break undefined; `BD-ACC-01` is silent for services** (`X-18`) | The two-axis stockable/consumable/service tie-break is undefined and the governing accounting ruling **presumes a physical fact**. **Design would have to choose the routing rule itself** |

> **These five are not later-phase work deferred. They are inputs Functional Design consumes.**
> **Every other open item in this pack is lawfully classified as execution-dependent, external-authority,
> or Boss-decision — and none of those bars entry.**

---

## 2. `CLOSED` by Pre-Test evidence

| Item | Closure |
|---|---|
| **Boss instruction `SC-BD-09` §8.1** — element 15 proof + `RT-E15-01`…`-09` into Pre-Test exit criteria | **DISCHARGED** — `PTX-01`…`PTX-11` constituted (`PT-09` §4). The obligation was **owned by "Pre-Test"** (`SC-11` §6 #8) and was outstanding on entry. **Awaiting Boss adoption** |
| `PT00-F-01` — `SC-59` understated the challenge population (`64` vs **`76`**, quarantine subtracted twice) | **CORRECTED in this package**, confirmed by a second instrument; supplied to the B-7 pack |
| `PT02-F-02` — element 15's "design gap" | **RAISED AND DISPROVED BY ITS OWN AUTHOR** — `SA_CORR5_01` adjudicated the design |
| `PT05-F-01` causal attribution | **SELF-FALSIFIED AND CORRECTED** at `PT-13` |
| `PT00-N-01` · `PT01-N-01` · `PT01-N-02` · `PT03-N-01` | **`4` apparent contradictions tested and REFUTED**, published so they are not manufactured again |
| `PT13-D-01` · `PT15-D-01` · `PT15-D-02` | **`3` defects in this session's own package, found and FIXED** |

## 3. `EXECUTION-DEPENDENT` — lawful later proof, does **not** bar entry

`0 of 48` scenarios · `0 of 58` invariants · `0 of 18` contracts · `0 of 8` isolation proofs ·
`0 of 60` negative cases · `0 of 13` enforcement surfaces · `0 of 13,814` dedup keys ·
element 10 and element 15 **specified, not built** · `PTX-01`…`PTX-11` · **`EC-04` `0/3`**.

**`EC-04` closure standard, unweakened:** **executed runtime proof + independent reproduction, no later
than the State 8-Criteria Exit Gate. Specification evidence NEVER satisfies `EC-04`.**

## 4. `EXTERNAL AUTHORITY` dependency — `13` items

| Authority | Items |
|---|---|
| **AAS+** (`4`) | `POH-D-06` restatement concurrence · **limb-2 re-wording** (it *"tests for uniqueness where the answer is zero"* and **cannot be discharged in either direction as written**) · `AAS-V-02` discharge act · **manufacturing-veto membership** (`PT07-F-01`) |
| **Thai statutory** (`4`) | `TH-NEW-01` · `TH-NEW-02` · `POH-D-02` tax consequences · over-absorption cap strength |
| **Business SME** (`2`) | `SME-Q-02` · `SME-Q-03` |
| **PMO** (`3`) | `GAP-KC-01` · the `PT10-F-01` re-derivation · the `PT04-F-01` boundary set |

## 5. `GENUINE BOSS DECISION` — nothing here is resolvable by SMEs Core

| # | Item | Type |
|---:|---|---|
| **B1** | `POH-D-01`, `POH-D-03`, `POH-D-04`, `POH-D-05` | **`4` decisions — ready, held, presentable** |
| **B2** | **`AAS-V-02` ratification** — not selected at `SC-BD-10` | act |
| **B3** | **Is the veto count `6` or `7`?** The standing manufacturing veto is **neither a member nor a declared exclusion** of the register (`0` hits for `BLK-07`/`BLK-08`/*manufactur*/*machine*, positive control `3`) | **authority clarification on a tolerance-zero control count** |
| **B4** | **Adopt `PT11-P-01`'s enumerated `12` boundaries**, name a different set, or rule which of `12`/`18`/`10` governs | **authority act on a SMEs Core proposal** |
| **B5** | **`PT10-F-01`:** commission the re-derivation, or rule that the pre-ruling split stands | **authority direction** |
| **B6** | **Adopt `PTX-01`…`PTX-11`** as Pre-Test exit criteria | adoption of a directed deliverable |
| **B7** | **Functional Design entry** | **this gate** |

**NOT presentable, and why:** **`POH-D-02`** — withheld, **no Boss act can move it** while the statutory
evidence is absent (`PTE-4`). **`RC-D-03`/`RC-D-04`** — a **SMEs Core** recommendation is owed first
(`SC-11` §6 #2); putting them now would repeat the *"SMEs Core position in Boss's mouth"* defect that was
caught once already.

## 6. `VETO STILL IN FORCE` — `6`, `0` discharged

`AAS-V-01` · `CF-V-01` · **`RC-V-01`** · `AAS-V-03` · `CF-V-02` · `AAS-V-02`.

**Language carried deliberately:** `AAS-V-03`'s COGS limb is **vacuous — and vacuous is not discharged**.
`CF-V-02`'s **first limb is closed — the veto is not lifted**. `AAS-V-02`'s **condition is satisfied — it
is not discharged**.

> **`RC-V-01` bars IMPLEMENTATION START on every reading. Functional Design is design, not implementation
> — and Functional Design must not be used to begin one.**
> **The standing manufacturing veto is NOT lifted** (limb 1 **and** a re-worded limb 2 must both be
> discharged by AAS+).

## 7. `UNRESOLVED BLOCKER` — B-7

**`B-7 WAITING FOR ELIGIBLE INDEPENDENT EXECUTOR`.** `0` candidates named by SMEs Core. **`EC-07` `0 of 2`.**

**It does NOT bar this gate** — under `SC-AUTH-02 = Reading C`, `EC-07` attaches to the **Module** and
**State** gates; `RC-V-01` bars **implementation start**. **It is not thereby optional.**

**Baseline re-frozen; manifest `20` entries, `20 OK`. `4` corrections supplied to the pack. `6` attack
targets nominated — `PT10-F-01` FIRST, because it is the only finding in the package that improves the
picture and self-challenge is structurally weakest exactly there.**

---

## 8. What this session did NOT do

| | |
|---|---|
| Runtime proof fabricated, simulated or implied | **`0`** |
| Vetoes discharged, narrowed or declared vacuous | **`0`** |
| Scenario grades changed — including `E2E-04` | **`0`** |
| Tolerance-zero boundaries reclassified | **`0`** |
| Ruled denominators re-scoped | **`0`** |
| Phase SA or design-branch artefacts rewritten | **`0`** |
| B-7 independence self-certified | **`0`** |
| Functional Design begun · code written · anything merged, released or deployed | **`0`** |
| **Values silently upgraded** | **`0` — including the one upgrade the evidence would have supported** (`PT10-F-01`) |

---

## 9. The honest summary

**The Pre-Test Matrix is complete in the sense the phase requires: `48` scenario rows, `11` control rows
and `11` exit criteria, each with a source pointer and a disposition, `0` omitting downstream routing.**

**It is not a package that can hand work to Functional Design today**, for five counted reasons at §1 —
and **four of those five are gaps in the inherited Phase SA package, not in the Pre-Test work**. Pre-Test
did what it exists to do: **it found where SMEsPlus would fail before implementation began.**

**`21` material findings were raised. `1` was disproved by its own author, `1` had its causal attribution
corrected by this session's own falsification round, and `3` defects in this session's own package were
found and fixed. `4` apparent contradictions were tested and refuted rather than published as findings.**

> **The single most important caveat in this pack:** **`PT10-F-01`** shows the readiness split
> (`10 WRITABLE / 12 GATED`) was measured the day **before** the rulings that gate it, and **at least
> `10 of 12` gates have since been RULED**. **If re-derived, the package may be materially readier than
> every figure in this pack states.** This session **carried the reported figures unchanged and did not
> re-derive** — because the carry-forward forbids silent upgrades, because the register is Phase SA's, and
> **because it is the one finding this session benefits from being right about.** **It is `B5`, and it is
> Boss's to direct.**

---

## 10. The terminal recommendation

```
RECOMMEND HOLD — MATERIAL PRE-TEST GAP

Five items are business semantics or scope declarations that Functional Design
consumes rather than produces:

  1. the 12-boundary set is ruled by number and never declared as a set;
  2. four outputs have no consumer;
  3. the ship -> invoice -> return-after-close -> downstream-consumed case is unspecified;
  4. the material-flow enumeration is short by at least one;
  5. the product-classification tie-break is undefined and BD-ACC-01 is silent for services.

Two further HOLD conditions are SIMULTANEOUSLY true and are NOT the primary ground:
  - HOLD — EXTERNAL AUTHORITY INPUT REQUIRED (13 items; AAS+ limb-2 re-wording is undischargeable as worded)
  - HOLD — BOSS AUTHORITY DECISION REQUIRED (7 items, B1-B7)

MATERIAL PRE-TEST GAP is primary because it is the only one of the three that
would force Functional Design to INVENT missing business semantics, and because
items 1 and 2 are closable by SMEs Core and PMO without any external input.

AI/PMO recommends only. Boss alone decides entry to Functional Design.
```

---

## 11. What Boss is asked to decide

1. **Functional Design entry** — grant, or hold on the five gaps at §1.
2. **`B1`** — the four presentable decisions (`POH-D-01`, `-03`, `-04`, `-05`).
3. **`B3`** — is the veto count **`6` or `7`**?
4. **`B4`** — adopt the proposed `12`-boundary set, or name another.
5. **`B5`** — commission the `PT10-F-01` re-derivation, or rule the pre-ruling split stands.
6. **`B6`** — adopt `PTX-01`…`PTX-11` as Pre-Test exit criteria.
7. **`B2`** — `AAS-V-02` ratification.
8. **Appoint `B-7`** — independent of this gate, and required before the State gate and, via `RC-V-01`,
   before implementation start.

---

# `RECOMMEND HOLD — MATERIAL PRE-TEST GAP`

**Pre-Test executed `PT-00`…`PT-15`. `CP-PT-14` not reached. `EC-04` `0/3`. `EC-07` `0/2`.
`6` vetoes in force. `0 of 48` verified. `E2E-04 NOT TRAVERSABLE`. Functional Design NOT begun.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass. Falsify before Accept. Correct before Escalate.
**Boss is the sole Final Approver.**
