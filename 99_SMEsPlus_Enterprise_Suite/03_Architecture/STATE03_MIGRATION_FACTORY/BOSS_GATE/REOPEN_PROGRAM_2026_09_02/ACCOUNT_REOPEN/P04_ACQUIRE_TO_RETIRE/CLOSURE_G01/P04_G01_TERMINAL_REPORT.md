# P04 — G01 BOUNDED-DEEP CLOSURE: TERMINAL REPORT

**Prompt:** `[SMEPLUS-26-09-06-G01-P04-A2R-BOUNDED-DEEP-CLOSURE-DESIGN-INPUT-001]`
**Branch:** `research/account-p04-acquire-to-retire-2026-09-04-001`
**Repository:** `TH-PATTARAKRIT/AI-Collaboration-Hub`
**Model / effort:** Claude Opus 5, HIGH — unchanged throughout.

---

## 1. Terminal state

> ### A — G01-P04 BOUNDED-DEEP CLOSURE COMPLETE — READY FOR CONTROLLED DESIGN INPUT / HANDOFF — OPEN HOLDS NAMED

**No PASS. No whole-domain Final Freeze. No merge. No implementation authorisation. No mutation.**

## 2. Inputs

| Input | Verified |
|---|---|
| P04 baseline | **`fc3620be8d4e…` does not resolve**; real baseline `fc362fcf533b`. Transcription slip, **declared** |
| **P03 authoritative closure** | **`bc7676733a1b…` does not resolve** — remote refuses. Consumed **`bc767a8`**, verified **by content** |
| P01 authoritative closure | `b820b29` **verified present, deliberately unread** — §5 admits it only on demand |
| Constitution | `48ee264` read and applied |

## 3. CQ-P04-01…12 dispositions

| CQ | Disposition |
|---|---|
| 01 Asset Model → Asset inheritance | **FACT VERIFIED — CLOSED** *(headline disproved by own disproof, reissued narrower)* |
| 02 Day convention | **FACT VERIFIED — CLOSED**; statutory limb **P07** |
| 03 Asset ↔ Equipment | **FACT VERIFIED — CLOSED** |
| 04 Equipment without Asset | **FACT VERIFIED — CLOSED** |
| 05 Active-period attribution | **BOSS DECISION REQUIRED** (`BLK-07`); factual half verified |
| 06 Post-depreciation internal usage | **BOSS DECISION REQUIRED**; one route closed by `P04-F-154` |
| 07 Operation → Equipment | **FACT VERIFIED — CLOSED**; design question **BOSS DECISION REQUIRED** |
| 08 Maintenance / non-productive cause | **FACT VERIFIED — CLOSED** (negative, denominator declared); repair limb **P05** |
| 09 Analytic bridge | **FACT VERIFIED — CLOSED** |
| 10 Disposal / derecognition | **FACT VERIFIED — CLOSED** |
| 11 Scope / multi-company | **FACT VERIFIED — CLOSED**; one asymmetry → `P04-B-54` |
| 12 Evidence integrity | **FACT VERIFIED — CLOSED**; residual source gap **UNRESOLVED**, `P04-B-51` |

**12 of 12 terminally dispositioned. No vague `OPEN`.**

## 4. The headline answers

- **Asset ↔ Equipment.** Reference product: **no relation in either direction**, measured with a
  firing control — independently corroborating P03. The relation exists **only** in custom
  `equipment_sequence`: **one-directional asset → equipment**, **no cardinality constraint**,
  **no company domain**, and a status transition **`eqp → tass` with no reverse anywhere** —
  4 writes, all one way, 0 writes back, across both custom trees.
- **Day convention.** **Three** settings, not two. The non-daily default is **not 30/360** — it
  scales boundary months by their real length. The estate runs the **non-default**
  `daily_computation`: **683/685** at v16 and **375/388** at v18.
- **Active / post-depreciation.** **No mechanism exists** for productive or non-productive
  attribution, and **`account.asset` cannot post off-balance** — all three account fields
  exclude that type by domain, which closes one route to the Boss's managerial-usage policy.
- **Operation → Equipment.** **Proven absent**, both sides, same series.
- **Analytic.** The measured net-to-zero has its **source cause**: one statement writes the
  distribution to **every** line of the depreciation entry, and only on draft moves.

## 5. Design input pack

`P04_SMESPLUS_FUNCTIONAL_DESIGN_INPUT_PACK.md` — **13 functions**, each on the §11 attribute
set, each labelled exactly one of `FACT-SUPPORTED FUNCTIONAL REQUIREMENT` /
`BOSS-APPROVED POLICY INPUT` / `DESIGN CANDIDATE` / `UNRESOLVED — DECISION/EVIDENCE REQUIRED`.
**No schema, API, UI, GL account or production design is frozen.**

## 6. Holds and owners

| Hold | Owner |
|---|---|
| `BLK-07` denominator; `P04-BD-05`…`-09` | **Boss** |
| `P04-B-51` series-16 source | Estate change — outside this host |
| `P04-B-52` day-count inclusivity | P04, bounded, not opened |
| `P04-B-53`, `P04-B-55` runtime measurements | P04, needs a runtime pass |
| `P04-B-54` record-rule company scope | P04, second instrument |
| Repair/vendor expense, stranded equipment | **P05** |
| Off-balance chart, lock integrity, analytic reporting | **P08** |
| Day-convention statutory admissibility | **P07** |
| Six architecture contradictions, six Boss decisions | **P11** |

**0 of 4 inherited blockers closed. 7 new blockers registered.**

## 7. PMO

**Qualified YES** for controlled design input on DF-01…DF-06, DF-10 (asset side), DF-11, DF-13.
**NO** for anything downstream of `BLK-07`. **Three new broad-research items are named and none
was started; none is authorised by this prompt.**

## 8. Integrity

| Item | Value |
|---|---|
| Background tasks | **0** — none started, none inherited |
| Mutation | **none** — read-only against source trees, database archives and peer branches |
| Receiving Pxx executed | **none** — P03 consumed, P01 unread, P05/P07/P08/P11 handoffs only |
| Scope | **17 declared searches, 5 declined.** Deeper 17 times, **never wider** |
| Self-falsifications | **2** — both author-side, both caught by the mandated disproof |
