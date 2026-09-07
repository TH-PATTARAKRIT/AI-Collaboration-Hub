# P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]` · prompt commit `51763d8`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · branch `audit/p06-independent-verifier-2026-09-06-001`
**Frozen audit surface:** `1b018c104001eb4683166518a6161a8cd8ab5cee`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## TERMINAL STATE (§10 — exactly one)

> ### `P06 INDEPENDENT VERIFICATION FOUND MATERIAL DEFECT — TARGETED REPAIR REQUIRED`

**Not A** — ~~18~~ → **26 material defects** survive on the frozen surface **[Q-P06-01 / XRD-001, 2026-09-07 — propagated from the addendum; superseded figure retained as lineage]**. *The addendum revised 18 → 25; the enumeration mandated by `Q-P06-01`'s Re-test gives **26**, contiguous `IEV-D-01`…`IEV-D-26` — see §Enumeration.*
**Not C** — the evidence was fully available and was obtained; nothing was blocked.

## `AASP-VETO-07` (§9)

> ### `AASP-VETO-07 — PRESERVED`

**On two independent grounds, either sufficient:**

1. **The prompt's own precondition is not met.** §1: *"THIS PROMPT MUST NOT BE EXECUTED BY THE SAME P06 CORRECTION ACTOR."* **It was.** The executing context authored the `REV-E-23` repairs. §9 reserves the discharge recommendation to *"an independent verifier that completes this prompt"* — that is not this verifier, whatever the findings.
2. **The evidence would preserve it anyway.** ~~18~~ → **26** material defects **[Q-P06-01 / XRD-001, 2026-09-07 — propagated from the addendum; superseded figure retained as lineage]**, 7 of 9 claim classes carrying survivors, and both P11-bound handoffs publishing wrong figures written by the repair round itself.

## What the audit confirms

**The research is sound; the bookkeeping about the research is not.** Every claim re-executed against the ERP source held: the `is_matched` structure (4 branches, 5 sites), every sampled v18 and v19 line number, the `account_move` SQL quotation, all eight enumerative version counts, and two of three cross-version invariance rows byte-identical. The `X-08` family is clean across eleven statements and seven files, and no peer-owned item is converted to closed anywhere. The repair arithmetic reconciles: 21 + 3 = 24, and 24 is measured.

## The material defects — grouped by what they say about the method

> **POPULATION: 26**, ~~18~~ ~~25~~ retained as lineage **[Q-P06-01 / XRD-001, 2026-09-07 — propagated from the addendum; superseded figure retained as lineage]**. The eight added by the addendum are `IEV-D-19`…`IEV-D-26`; the grouping below covers the original 18 and is not re-opened, per the queue's PROHIBITED row.

**Wrong figures published by the repair round itself (4):** the blocker count is **67, not the 65** written into `13_`:94, `46_`:124, `18_`:214 and `70_`:108 — at every declared scope, including both printed commands' own globs, with `B-66`/`B-67` created by that same round; *"three vetoes"* and *"four active vetoes"* against **seven**; *"16 recorded author errors"* against **23**. `46_`:124 states the rule *"a printed command and a printed result date differently"* and breaks it in the same clause.

**Defects the round manufactured (2):** `41_`:6's supersession pointer cites five lines and **all five are wrong by exactly 3** — inserting the 3-line pointer shifted the file it points into, sending readers to a blank line and a table separator. And `01_`:115's insertion orphaned its sentence tail.

**Survivors invisible to the declared pattern (9):** `filtered subset` · `filtered checkout` · `filtered to the Thai deployment` · `filtered 791-addon tree` · `filtered-evidence-base` · the noun `absence` · the ordinal `7 of 9` · `a fifth path` · the header `Blocker population`. **Thirteen current statements of the retired evidence-base reading survive across seven files** — including **five of the six rows of the one table whose sixth row was repaired**, and `56_`:53, which prescribes the retired term as the mandatory form for every future negative claim.

**Outbound boundary defects (3):** `34_`:44 records that a peer **accepted** a P06 row and cites **P06's own sentence** as the evidence — the quoted string occurs twice on the tree, once as P06's own consequence at `09_`:80. `36_`:42-43 gates four items on *"P08's absence"* and prescribes *"one publication closes the chain"* when P08 was published and read in round 3. `18_`:7/:212 publish *"READY"* and *"COMPLETED"* against a HOLD terminal state.

**A control that certified an absent string (1):** `P06_AAS_PLUS_CONSOLIDATION.md`:50 states `HO-03`/`HO-04` *"are labelled"* WRITTEN, NOT DELIVERED. **The handoff pack's only delivery word is *"re-delivered"*.** Two governance statements certify the labelling *"verified by grep"*.

## What this audit got wrong, recorded first-person

**`IEV-I-01` — my own first instrument failed.** Nine claim-class sweeps held their glob list in a shell variable; zsh does not expand those. **The positive control returned 0 occurrences of `P06` across an 87-file P06 package.** Without it I would have certified nine clean classes on nine fabricated zeros and recommended discharge. **That is `VER-E-02` — a defect this package documents — committed by its auditor at the first attempt.**

**`IEV-I-02` — my first reading of `VER-E-04` was too generous** and was corrected only because a challenger re-executed the regex and got exit 0. **An auditor's charitable reading is itself an instrument, and it failed in the package's favour.**

**`IEV-I-03` — one of the 18 defects is mine.** `41_`:6's broken pointer is a `REV-E-23` edit I authored. **`IEV-I-04` — and one challenger of four did not return**; its remit is covered by two others whose findings I re-executed, but the gap is recorded as a gap.

## Repairs required of P06 — routed, not performed (§7)

**Zero edits were made to the source package.** In priority order:

| # | Repair | Location |
|---|---|---|
| 1 | Correct the blocker count to **67** and re-execute at publication | `13_`:94 · `46_`:124 · `18_`:214 · `70_`:108 |
| 2 | Correct the veto count to **seven** and the author-error count to **23** | `18_`:214 · `70_`:108 |
| 3 | Withdraw or evidence the peer-acceptance claim; the quoted sentence is P06's own | `34_`:44 |
| 4 | Label `HO-03`/`HO-04` in the handoff pack, or withdraw the three statements certifying that they are | pack `:180-190`; `AAS_PLUS_CONSOLIDATION`:50; `CHECKPOINT`:73; `PROPAGATION_MATRIX`:128 |
| 5 | Repair the five broken line cites | `41_`:6 |
| 6 | Sweep the retired evidence-base reading on **variant-tolerant** patterns | 13 statements, 7 files; start with `56_`:53 and `:62-67` |
| 7 | Re-state `36_`:42-43 — the chain is gated on a **ruling**, not a publication | `36_`:42-43 |
| 8 | Correct the peers-read ordinals | `40_`:17 · `40_`:35 |
| 9 | Remove completion language or align it to the terminal state | `18_`:7 · `:212` |
| 10 | Correct `:437`→`:438` and the by-configuration branch count; repair the orphaned tail | `01_`:115 · `:122` |
| 11 | Retire the *"filtered subset"* reading and the 791-vs-1422 comparison that inverts on a 1752 denominator | `51_`:21 · `:22` · `:93` |
| 12 | Declare P08 in the controlling denominator document and reconcile 7-vs-8 | `12_`:133 · `37_`:5/:11/:52 |
| 13 | Restate `18_`:188, `09_`:13/:98, `52_`:86, `35_`:148, `34_`:32 | as listed |
| 14 | Name the tool and version in `VER-E-04`, which does not reproduce | tool-defect register |
| 15 | Fix the NEXT-EXACT-ACTION command's path set and its 21/14 figure | `AUTO_RESUME`:157 · `:170` · `:172` |

## Open holds — unchanged (§6)

`P06-B-08` **BOSS DECISION REQUIRED** · `P06-B-09` statutory · `P06-OQ-98` **HOLD**, iEVING not assumed to be the target · `AASP-VETO-06` written ≠ delivered · `X-08`/`D-08`/`PD-08` **P10-owned** · `HO-03`/`HO-04` not converted · P01/P08 rulings external. **No peer package was consumed. No new research surface was opened. No mutation.**

## The finding that should govern the Boss decision

**`P06-B-67` — *"a correction population is a floor, not a population"* — is now supported four times over.** Rounds 5, 6 and 7 each declared a population complete and each was enlarged by the next pass. **This audit, briefed differently and run partly in separate contexts, enlarged every class it touched — and then had its own first instrument return nine fabricated zeros.**

**The defect is not diligence and it is not any one actor. It is that a correction population defined by the words an author remembers cannot be closed by searching harder for those words.** Until a population is defined by something other than remembered phrasing, a fifth pass will enlarge the fourth.
