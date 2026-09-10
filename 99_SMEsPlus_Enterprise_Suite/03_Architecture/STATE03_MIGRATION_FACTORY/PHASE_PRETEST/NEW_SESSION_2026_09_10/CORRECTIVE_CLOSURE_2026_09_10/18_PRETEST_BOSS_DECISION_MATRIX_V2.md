# 18 — BOSS DECISION MATRIX V2

## `CHECKPOINT C + E — 11 CARDS RECONSTRUCTED · REVIEW REMOVED 2 · NET 9`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-BOSS-RESOLUTION-001]` · Boss: **SOLE FINAL APPROVER**

> **§17 goal: MINIMUM NECESSARY BOSS DECISIONS, not maximum escalation.**

---

## 1. The §17 adversarial review — what it removed

| Item | Reviewer | Finding | Outcome |
|---|---|---|---|
| **`B10′`** freeze flag | **Architecture** | The flag **freezes 8 named line fields on lock** — it is **wired, to its own module's data**. `SA03`'s binary was *"internal-only concern OR unwired control"*; the evidence answers it: **it is not unwired**. A control whose entire effect is intra-module is **correctly consumer-less at the cross-module boundary** | **REMOVED from the Boss set — resolved as an Architecture determination** (§4) |
| **`B5′`** adopt the re-derived split | **PMO** | §10 requires the split be treated as **PROVISIONAL** and made B-7 attack target #1 regardless. **Carrying it provisional needs no ruling.** Asking Boss to adopt a figure B-7 will attack **creates a ruling that may be reversed in one round** | **REMOVED — carried `PROVISIONAL`, no ruling sought** |
| `B1` | **PMO** | **Understated.** `RC-D-03`/`RC-D-04` were closed at `SC-14`/`SC-15`; `SC-44` lists **`6` ready** | **EXPANDED `4 → 6`** |
| All | **AAS+** | `07_`'s `CLASS C` re-tested against `AAS-V-03`: **4 limbs, 4 subjects, `0` overlap** | **`B3′` UPHELD** |
| All | PMO | duplicate / stale / circular Boss questions | **`0` duplicates · `1` stale (`B1`) · `0` circular** |

**`11` presented → **`2` removed** → **`9` Boss items**, one of which (`B1`) now carries `6` decisions.**

---

## 2. The consolidated matrix

| ID | Recommended ruling | Alternative | Why recommended | Risk | What closes | What remains open | Boss action |
|---|---|---|---|---|---|---|---|
| **`B4′`** 12-boundary set | **DECLARE the 12 members explicitly** (list at `21_` §B4′) — adopting the `PT11-P-01` candidates **as a Boss-declared set**, not as inherited | (b) declare `18` (`XMC-H`) · (c) declare `10` · (d) another set | **No authority enumerates any set** — the chain says *"twelve"* `6×`, enumerates `0`. The only 12-list is a **prompt floor** marked *"At minimum test"*. **`18` is the register actually tested** | Declaring `12` **closes a floor into a denominator**; declaring `18` **re-scopes a ruled number**. Both are Boss-only | FD blocker 1 · `SC-11` §6 #5 applicability declaration | per-boundary applicability content | **DECLARE MEMBERSHIP** |
| **`B3′`** veto count | **RATIFY `CLASS C` = `7`** | (b) publish a **declared exclusion with reason**, keeping `6` | `A` and `B` disproved by measurement (`0` occurrences, control `3`); `C` established on the register's own `5` criteria; **`AAS-V-03` distinct — 4 limbs, 4 subjects** | `6` appears in **`SC-60`, Boss's own authorization** — ratifying `7` corrects a tolerance-zero count Boss has already signed | veto denominator; `CC-F-06` contradiction | limb-2 re-wording (AAS+) | **RATIFY or EXCLUDE** |
| **`CC-D-01`** classification | **(a) Option 3** — KIND governs **admissibility**, CATEGORY governs **measurement**, with an explicit **refusal rule** where CATEGORY carries a policy KIND cannot use · **(b) Option B** — Service carries a **recorded determination that no cost recognition arises**, satisfying `ND-09`'s second branch | (a) Options 1/2/4 · (b) Options A/C | Option 3 **preserves both closed rulings** — `BD-ACC-01` keeps admissibility, `BD-ACC-03A` keeps valuation authority — and the refusal rule makes the silent case **explicit rather than inferred**. Option B uses `ND-09`'s **own** second branch rather than inventing a cost | Option 3 adds a refusal path FD must build; Option B forecloses service costing if `IR-17` consumption later proves material | FD blocker 5 · `X-18` · `E2E-08` · `PT-S-01` | `IR-17` service/project consumption remains `PARTIAL` | **RULE (a) AND (b)** |
| **`B1`** — **`6` decisions** | present and rule all `6`: **`RC-D-03`, `RC-D-04`**, `POH-D-01`, `POH-D-03`, `POH-D-04`, `POH-D-05` | rule a subset | **All `6` are recommendation-complete and specialist-challenged.** `SC-44`: *"open, ready — `6`"* | **`POH-D-01` also gates `X-16`/`X-17`** — leaving it open keeps `2` scenarios `GATED` | `X-16`/`X-17` gating · `F5`/`F6` residue | **`POH-D-02` — statutory, NOT in `B1`** | **RULE 6** |
| **`B6`** `PTX` adoption | **ADOPT `PTX-01`…`PTX-11` as the canonical Pre-Test exit-control set; denominator `11`** | reject · amend | 1:1 crosswalk verified; **`9 + 11 = 20` is a double count** | none — adoption creates no obligation not already directed by `SC-BD-09` §8.1 | Pre-Test exit criteria defined | **`0 of 11` satisfied** — element 15 unbuilt | **ADOPT** |
| **`B2`** `AAS-V-02` | **RATIFY the discharge act** | withhold again | condition **SATISFIED**; ratification **not selected** at `SC-BD-10` | **`0`** — `RC-V-01` bars implementation start regardless | one veto's residual act | `5` other vetoes | **RATIFY or WITHHOLD** |
| **`B7′`** B-7 appointee | **NAME an appointee meeting the `20_` eligibility criteria** | defer | act **approved** at `SC-BD-10`; **appointee unnamed**. Blocks `EC-07`, `CP-PT-14`, exit condition 15 | naming an ineligible party **destroys** the control | `EC-07` route · `CP-PT-14` route | `EC-07` `0/2` until 2 clean passes | **NAME** |
| **`B8′`** `E2E-04` re-grade owner | **STRUCTURE A — SMT performs the technical re-grade; B-7 independently verifies it** | B: B-7 owns the re-grade | **Strongest separation of duties**: `SC-01` §6.2 routes to SMT, `SC-BD-02` §8.4 holds it for the independent reviewer — **A satisfies both**. B makes the challenger the author of what it must then challenge | A costs one extra hop | exit condition 11 route | the re-grade itself | **RULE A or B** |
| **`B9′`** migration class | **ADMIT `MF-01` and `MF-02`; EXCLUDE `MF-03` as a dimension** → `IR` `18 → 20`, `AR` `29 → 30` | admit all 3 · admit none | `17_` §2 rows are evidence-derived from `HX-23`/`-24`/`-25` + element `14`. **`CC-F-11`: `MF-01` creates value with no movement and no existing rule reaches it** | admitting `MF-03` **inflates the denominator**; admitting none leaves the enumeration knowingly short | exit condition 5 · `05_`'s denominator | `MF-01`'s counterpart account undetermined | **ADMIT / EXCLUDE** |

---

## 3. Items REMOVED from the Boss set — recorded, not dropped

| ID | Disposition |
|---|---|
| **`B10′`** | **RESOLVED — Architecture determination.** Commercial-terms freeze flag = **`B` TERMINAL BY DESIGN at the cross-module boundary** (it freezes 8 named line fields within its own module; it is wired, not unwired). Its adequacy as an **intra-module** control is a Functional Design concern. **Boss may overturn; `03_`'s `D ORPHAN` class for this row is superseded → orphan outputs `3 → 2`.** **B-7 attack target** |
| **`B5′`** | **NOT ASKED — carried `PROVISIONAL`.** `19 / 2 / 1` remains **B-7 attack target #1**; Boss adoption deferred until independent verification, per §10 |

---

## 4. What every card has in common

| | |
|---|---|
| Boss authority required because | each either **declares a denominator no evidence enumerates**, **chooses between two closed rulings**, **ratifies another authority's act**, or **appoints** |
| Recommendation ≠ approval | **`0`** cards convert a recommendation into a ruling |
| B-7 must attack the result | **`YES` on all `9`** — every ruling implementation becomes a challenge target |
| Affected verification items | **`0 of 48` move** — no ruling produces runtime proof |

---

## 5. Checkpoint

> ## `CHECKPOINT C + E — DECISION SET MINIMISED`
>
> **`11` reconstructed → **`2` removed by review** (`B10′` resolved by Architecture; `B5′` carried
> provisional) → **`9` Boss items** · **`B1` expanded `4 → 6`** on the `CORE-01` correction ·
> `0` duplicates, `0` circular, `1` stale corrected · `AAS-V-03` re-tested and `B3′` upheld ·
> **`0` recommendations converted into approvals · `0 of 48` verification items move.**

