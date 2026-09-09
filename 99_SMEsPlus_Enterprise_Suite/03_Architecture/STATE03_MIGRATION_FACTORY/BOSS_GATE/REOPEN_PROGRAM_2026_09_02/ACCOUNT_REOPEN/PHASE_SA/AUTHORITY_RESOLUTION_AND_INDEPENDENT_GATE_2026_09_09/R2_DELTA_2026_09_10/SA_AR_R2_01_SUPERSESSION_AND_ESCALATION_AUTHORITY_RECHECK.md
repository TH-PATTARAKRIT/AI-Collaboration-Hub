# SA_AR_R2_01 — SUPERSESSION AND BOSS-ESCALATION AUTHORITY RE-CHECK

Session `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` — round 2 (delta)
Re-test of `CP-SA-AR-30` / `CP-SA-AR-80` / `CP-SA-AR-90` against the delta measured in `SA_AR_R2_00` §3.3.
**Nothing here discharges a veto, closes a family, or approves anything.**

---

## 1. What the new instruction says

`[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` — Boss-authored, `34a46d9b` · `cdcf53c9` · `33537d36`,
branch `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`, master prompt
`01_SMEPLUS_PHASE_SA_SMES_CORE_CONTINUATION_MASTER_PROMPT.md` (370 lines).

It takes **the same `F1`–`F8` population** this session escalated. Subject-matching was verified family
by family against `SA_AR_11` §3: `F1` COGS recognition/reversal · `F2` control-default policy · `F3`
Dropship valuation and cost landing · `F4` cross-module contract scope and supply binding · `F5`
Manufacturing overhead governance · `F6` cross-company visibility · `F7` authorization axis and
configurable-record scope · `F8` idempotency severity. **8 of 8 match.**

Its operative clauses:

| Clause | Text | Effect on escalation |
|---|---|---|
| §1 | *"Exhaust Team Authority Before Boss Escalation."* · *"Boss must not be the first detector."* | escalation is conditional |
| §4 | *"Take the eight Final Gate decision families `F1`–`F8` as an **input population, not as automatically Boss-bound questions**."* Mandates an A–F authority scrub → `SC-01` | escalation requires a scrub |
| §5 `F3` | *"This family has a live standing dissent. It **MUST NOT be escalated to Boss** until SMEs Core performs a bounded evidence re-read"* → `SC-02` | **`F3` escalation prohibited** |
| §7 | *"**No family may reach Boss without an SMT disposition.**"* → `SC-03` | **all 8 require a disposition** |
| §10 | *"**Only after** all preceding work is complete may SMEs Core publish an updated Boss decision pack."* · *"Never present Boss with raw research ambiguity that SMEs Core/SMT can still resolve."* | pack ordering is mandated |

---

## 2. Findings

### `AR-R2-F-01` — a later Boss instruction governs the same population *(CONFIRMED)*

The instruction postdates this session's Boss Decision Gate Pack `afe664c6` (2026-09-09 23:14:08) by
**1 h 19 min**, is authored by **the same identity that authored this session's own master prompt**
`e6d2be32`, and is **the newest commit in the repository across all 190 remote branches**.

**Round 1 committed no error.** The instruction did not exist when `afe664c6` was written. This is new
delta, and §3 of the master prompt is the clause that requires this round to consume it.

### `AR-R2-F-02` — 0 of 8 families carry the mandatory SMT disposition *(CONFIRMED)*

**Population:** the round 1 package directory at `afe664c6` holds **15** files — 14 added by
`afe664c6` itself plus the master prompt added by `e6d2be32`. The declared unit is *files present in the
package directory at the commit*, not *files changed by the commit*.

`git grep -ihE '\bSMT\b' afe664c6 -- '*AUTHORITY_RESOLUTION_AND_INDEPENDENT_GATE_2026_09_09*'` returns
**0** over all **15**. **Positive control:** the identical pattern against the new instruction's master
prompt returns **25**, so the predicate fires. The concept is absent from the package, not merely
under-evidenced.

§7 requires each surviving family to carry one of
`PASS / PASS WITH CONDITION / RETURN TO SME CORE / TARGETED VERY DEEP RESEARCH / BOSS-ONLY DECISION`,
and states *"No family may reach Boss without an SMT disposition."*

**8 of 8 families are short of a control the current instruction makes mandatory.**

### `AR-R2-F-03` — `F3` is escalated against an explicit prohibition *(CONFIRMED)*

`SA_AR_03` line 82 records `F3` (`XMC-D-01`, `C2-D-02`) as **`RETAIN 2`** — retained as a genuine Boss
decision and escalated. §5 states `F3` *"MUST NOT be escalated to Boss until SMEs Core performs a bounded
evidence re-read of the relevant buy-side / Inventory / Accounting evidence."*

The round 1 pack **reaches the same conclusion about the work and then escalates anyway**: `SA_AR_11` §3
records for `F3` *"A standing dissent says the answer may be available without a decision. Unresolved;
resolving it needs a buy-side re-read. If the dissent is right this leaves the Boss list."*

**The pack names the re-read as the thing that would remove `F3` from the Boss list, does not perform it,
and escalates.** Under the current instruction that re-read is SMEs Core work and is a precondition.

### `AR-R2-F-04` — `Material open items — SMEs Core = 0` no longer reproduces *(CONFIRMED)*

`SA_AR_11` §2 publishes **SMEs Core = 0** and asserts *"Nothing remains that SMEs Core, PMO, a document
owner or existing evidence can resolve. Everything that remains is Boss's."*

Measured against the current instruction, SMEs Core-owned, unperformed, mandatory work is **at least**:

| # | Work item | Required by | Deliverable | State |
|---:|---|---|---|---|
| 1 | `F1`–`F8` A–F authority scrub | §4 | `SC-01` | **not performed** |
| 2 | `F3` bounded evidence re-read | §5 | `SC-02` | **not performed** |
| 3 | SMT first-line challenge, 8 dispositions | §7 | `SC-03` | **not performed** |

**`SMEs Core = 0` is superseded. The correct current figure is ≥ 3 mandatory work items, 0 complete.**
This is a supersession by a later ruling, **not** an arithmetic defect in round 1.

### `AR-R2-F-05` — the two tracks are individually coherent and jointly inconsistent *(CONFIRMED)*

`git merge-base --is-ancestor afe664c6 origin/architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
returns **false**. The two branches fork at `b8666f14`.

The new track's own resume state names its parent as **`9d5bc2db`** — the Final Boss Gate package that
this session's round 1 **corrected**. Executed as written, that track will re-derive `F1`–`F8` from a
baseline that does not contain:

- **`AR-F-01`** — the parent's *"26 surviving Boss decisions"* counts `F5` by identifier while `F5`'s own
  card counts by decision; corrected on two agreeing shapes to **30 candidates → 24 decisions**. Round 1
  records that three rounds have now made this error.
- **`AR-F-02`** — the single Phase SA citation of `SMEPLUS-DR-EXIT-8C-001` applies **§9**
  (`PROVISIONAL / NON-CANONICAL`), not §4 or `EC-07` — which narrows the case for `FG-F-06` Reading A.
- The re-measured PMO closure, and the two published instrument failures `AR-I-01` / `AR-I-02`.

**Neither track is wrong on its own terms. They cannot both be the canonical Phase SA line.**
Which one is canonical is a Boss-owned routing decision — it is the scope and sequencing of Boss's own
instructions, and no evidence this session can gather decides it.

---

## 3. Effect on the round 1 checkpoint ladder

| Checkpoint | Round 1 | After delta |
|---|---|---|
| `CP-SA-AR-00` PMO closure | `VERIFIED` | **`VERIFIED` — re-measured at `a20db7a3`, holds** |
| `CP-SA-AR-10` baseline reproduced | `CLOSED` | **unchanged** — 190-branch frame reproduces round 1's 189 + the one new branch |
| `CP-SA-AR-20` fresh delta | `CLOSED` — Category 3 = 0 | **RE-OPENED and re-closed on new figures** — mainline 0, **SMEs Core ≥ 3** |
| `CP-SA-AR-30` decision population | `CLOSED` — 24 + 5 acts | **CONDITIONAL** — the 24 are unchanged *as decisions*; their **escalation** is now gated by §5 and §7 |
| `CP-SA-AR-40` families ready | `CLOSED` | **CONDITIONAL** — 0 of 8 carry an SMT disposition |
| `CP-SA-AR-50` `FG-F-06` ready | `READY — UNANSWERED` | **unchanged.** §8 of the new instruction independently requires this to be presented *last*, after team authority is exhausted — consistent with holding it |
| `CP-SA-AR-60` independent handoff | `READY — NOT EXECUTED` | **unchanged.** 0 structurally independent passes. §8 forbids self-declared independence, as `SA_AR_06` already does |
| `CP-SA-AR-70` vetoes | `CLOSED` — 6 in force, 0 discharged | **unchanged.** §8 forbids self-discharge; none discharged in this round either |
| `CP-SA-AR-80` Pre-Test entry | `CLOSED` — Category 3 = 0 | **RE-OPENED** — Category 3 = 0 for PMO and document owner; the SMEs Core column is no longer 0 |
| `CP-SA-AR-90` internal challenge | `CLOSED` — 6 findings | **superseded in kind** — §7 requires SMT first-line challenge, which is a different control from internal adversarial self-challenge and was not run |
| Boss Decision Gate Pack | `PUBLISHED — PENDING BOSS` | **`PUBLISHED — NOT CURRENTLY PRESENTABLE`** under §5, §7 and §10 |

---

## 4. What is *not* claimed here

- No family is closed, narrowed, or removed from the Boss list by this round.
- The 24 decisions and 5 acts are **not** disputed on their merits. Only the **route** to Boss changed.
- No veto is discharged. No independent assurance is claimed. No `PASS` is declared.
- Round 1 is **not** withdrawn. It is correct as of the moment it was published and is preserved intact;
  `AR-F-01` and `AR-F-02` remain live corrections that the other track has not consumed.
- This round did **not** perform the §4 scrub, the §5 `F3` re-read or the §7 SMT challenge.
  **They are not within this master prompt's authorization scope (§0 items 1–9), and doing them here
  would place the other track's deliverables on the wrong branch under the wrong identifiers.**
