# SC-08 — TWO-TRACK PRIMARY-SOURCE REPRODUCTION

## CP-SA-SC-80 — BOTH TRACKS REPRODUCED FROM PRIMARY SOURCE

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Execution host: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
SC baseline: `c4949ec6bcb608ccc6a9b4dcb1a6fb5a400786ac`
Peer evidence track (READ-ONLY): `architecture/phase-sa-authority-resolution-and-independent-gate-2026-09-09-001`
Executing body: **SMEs CORE**
Boss: **SOLE FINAL APPROVER**

> **NOMENCLATURE.** The active body is **`SMEs CORE`**. Where a historical artefact uses `SMT`, it is
> quoted verbatim and marked **`LEGACY NAME — CURRENT BODY = SMEs CORE`**. No current-state narrative in
> this file or any file `SC-08`…`SC-18` uses `SMT` as the name of the active body.

---

## 1. Result

> # `BOTH TRACKS REPRODUCED. TWO PEER FINDINGS RE-VERIFIED AT PRIMARY SOURCE. ONE PEER REASON CORRECTED WHILE ITS NUMBER STANDS. AR BRANCH FOUND TO HAVE ADVANCED TWO COMMITS BEYOND THE NAMED BASELINE.`

| Measure | Value |
|---|---|
| SC track reproduced at `c4949ec6` | **8 deliverables `SC-00`…`SC-07` + manifest, 11 files, manifest 11/11 reproduces** |
| AR track read | **R1 `afe664c6` (14 files) · R2 `b1f07939` (5 files) · R2 addendum `d7ab8e53`, `822cb327` (2 files)** |
| **AR head at read time** | **`822cb327` — TWO COMMITS BEYOND the baseline this prompt names.** Both consumed |
| AR load-bearing findings verified at primary source | **2 of 2** — `AR-F-01`, `AR-F-02` |
| AR findings adopted | **2 of 2** |
| **AR reasons corrected while adopting the conclusion** | **1** — `AR-F-01`'s ground (`SC-F-08`) |
| AR instrument findings consumed | **4** — `AR-I-01`, `AR-I-02`, `AR-R2-I-01`, `AR-R2-I-02` |
| Peer artefacts modified, withdrawn or overwritten | **0** |

---

## 2. Track SC — reproduced at `c4949ec6`

| Deliverable | Controlling result, reproduced |
|---|---|
| `SC-00` | PR #63 **`MERGED`** at `3f5d915a`; default branch `a20db7a3`; corrected blob `827b5906` authoritative; unauthenticated fetch `HTTP 200` and **the body hashes to the corrected blob**. **Category 3 `1 → 0`.** Branch split `190 / 8 / 182 / 0` on two command shapes |
| `SC-01` | `F1`–`F8` authority scrub. `0` wrongly escalated on authority. `0` new decisions originated. `SC-F-03`: the `F1` premise of an approved COGS-at-delivery direction **does not resolve** — every hit is a commissioning prompt, a scope bullet or a glossary entry |
| `SC-02` | `F3` bounded re-read. Reference direct-shipment capability **installed in `0` of 3** readable deployments, two differently-shaped instruments. **`C2-D-02` CLOSED**; `XMC-D-01` narrowed to a conditional scope question |
| `SC-03` | First-line challenge, **8 of 8 families**, 11 challenges, 6 changed a conclusion, **0 open returns**, **0 escapes**. *(This artefact's own text uses `SMT` for the challenging body — **`LEGACY NAME — CURRENT BODY = SMEs CORE`**.)* |
| `SC-04` | 6 vetoes in force, **0 discharged**, **0 held open by SMEs Core work** |
| `SC-05` | **`CATEGORY 3 = 0`**; 22 scenarios `10 / 12 / 0`; 18 E2E `9 / 9 / 0`; `1` untraversable (`E2E-04`); 3 Boss entry-gating decisions |
| `SC-06` | Boss delta pack, `TERMINAL A`, qualified |
| `SC-07` | Adopted `AR-F-01` and `AR-F-02`; count `26 → 24 → 23`; `BOSS-ROUTE-01` recorded **OPEN** |
| Manifest | **11 of 11 files reproduce** against the pushed tree |

**Current `BOSS-ROUTE-01` status at `c4949ec6`: `OPEN`.** Closed at `SC-09` on Boss's ruling.

---

## 3. Track AR — read read-only, and it had moved

**The prompt names `afe664c6` and `b1f07939`. The branch head at read time is `822cb327`.**

| Commit | Date | Content |
|---|---|---|
| `afe664c6` | 2026-09-09 | R1 — Boss Decision Gate Pack, 14 files, Terminal A, 24 decisions |
| `b1f07939` | 2026-09-10 | R2 delta — Terminal B / HOLD, 5 files |
| **`d7ab8e53`** | **2026-09-10 01:11** | **`SA_AR_R2_03` — records the Boss ruling on `BOSS-ROUTE-01`** |
| **`822cb327`** | **2026-09-10 01:15** | **`SA_AR_R2_04` — a conformance check on THIS session's intake, at `2139088b`** |

> **`SC-F-09`. Both later commits are material and neither was named in this prompt.** Had this session
> read only the two named commits it would have missed the Boss ruling's own record **and** a peer
> conformance check written about its own package. **The prevention control this session published one
> commit earlier (`SC-07` §8) is what found them** — sweep the peer branch head, not the cited baseline.
> **A named baseline is a floor, not a ceiling.**

### 3.1 The peer's conformance check on this session — and its one live item, already closed

`SA_AR_R2_04` checked `2139088b` and found this session cited **0** AR artefacts — correct at that
commit, and it says so without fault: *"The `SC` package was published **before** that ruling was given."*

| Peer intake item | Peer's finding at `2139088b` | **State at `c4949ec6`** |
|---|---|---|
| `AR-F-01` | *"**NOT a defect in `SC`.** Independently and better handled… That is the control working, not failing."* Boss should be told **which unit** a headline is on | **Adopted anyway** at `SC-07` §3, on primary source. §4 below explains why adoption is right and why the peer's generosity here is **declined** |
| `AR-F-02` | **"NOT consumed. Material."** Recommends adding the §9 narrowing to the `FG-F-06` card | **CONSUMED** at `SC-07` §4 — the precedent was **withdrawn from Reading A** in `SC-04` §6.3 and `SC-06` §4, going further than the peer's recommendation |

> **`1 of 2` named intake items was materially unconsumed when the peer checked. **`0 of 2` are
> unconsumed now.** The peer's check is accurate about `2139088b` and stale by two commits — which is
> the same class of staleness this file records against itself at §3.

---

## 4. `AR-F-01` re-verified — the number stands, the reason does not

**The peer's stated ground**, `SA_AR_03` §2: *"**Veto limb 2 is `POH-G-03`, an SMEs Core design gap, not a
Boss decision**, and is removed from the decision population entirely."*

**Re-executed at primary source** — `SA_CORR3_03_PRODUCTION_OVERHEAD_PROOF.md` on the CORR3 branch, read
directly, not through either package:

| Check | Primary text | Result |
|---|---|---|
| `POH-D-06`'s own cell | *"**`BLK-07` and `BLK-08`: confirm, or restate** \| **Governance act.** … This document requests a restatement; it does not perform one. **Same for veto limb 2**"* | **TWO named subjects**, with limb 2 **appended to the same request** |
| What `POH-G-03` is | *"`POH-G-03` \| **Veto limb 2 is undischarged and, as written, undischargeable.** No mutual exclusion, validation or collision check…"* | the **gap statement** about limb 2 |
| Who may restate a veto limb | **`POH-F-06`: *"Limb 2 … is an SMEs Core proof obligation, it is undischarged… **Restating a veto limb is reserved to the veto's issuer and Boss.** Deciding `BLK-07` alone would not lift the veto."*** | **restatement is issuer + Boss** |
| The register's own residue count | **`POH-F-16`: *"The Boss residue is **six items**, five of them small."*** | **six** |
| The six, enumerated | §11: *"`POH-G-01`, `POH-G-02` and `POH-G-04`'s variance closed by SMEs Core design work… and **`POH-D-01`, `POH-D-02`, `POH-D-06` returned by Boss**"* + `POH-D-03`, `-04`, `-05` | **`POH-D-01`…`POH-D-06` = 6** ✓ |

### 4.1 `SC-F-08` — the conclusion is right, the reason is not, and the difference matters

> **`F5` = 6 is CONFIRMED on two independent grounds** — the register's explicit *"Boss residue is six
> items"*, and the enumeration `POH-D-01`…`POH-D-06`. **The peer's number is adopted.**
>
> **But limb 2 is not "removed from the decision population entirely."** Its **discharge** is an SMEs Core
> proof obligation, as the peer says. Its **restatement** is *"reserved to the veto's issuer and Boss"* and
> is **bundled inside `POH-D-06`** by that decision's own text. **It is absorbed, not excluded.**
>
> **Two consequences neither track has carried, both material to the `F5` card:**
>
> 1. **`POH-D-06` is not a Boss-only act.** Its limb-2 component requires **the veto's issuer (AAS+) as
>    well as Boss**. Boss ruling `POH-D-06` alone does not complete the restatement it requests.
> 2. **`POH-F-06`: *"Deciding `BLK-07` alone would not lift the veto."*** **Ruling `F5` does not discharge
>    the standing manufacturing veto.** A reader of either track's `F5` card could reasonably have assumed
>    it does.
>
> **This is peer intake done correctly: verify the finding, adopt what the evidence supports, and correct
> the record the peer's package would otherwise carry.** The peer is notified by this file; **their branch
> is not touched.**

### 4.2 Why the peer's generosity on `AR-F-01` is declined

`SA_AR_R2_04` §3 concluded **no correction is proposed to `SC`**, on the ground that the two unit choices
are each declared and each defensible, so the finding is only that Boss should be told which unit a
headline is on.

> **SMEs Core declines that.** The parent's `8` is **not** a defensible alternative slicing of the same
> set: it counts **three** restatement subjects where the source names **two** and the register's own
> residue statement says **six items**. `8` is reachable only by slicing one governance act into subjects
> **and** adding a third subject the source does not put in the decision population. **That is not a unit
> choice; it is a membership error on top of a unit choice.**
>
> **A peer offering to let this session off is not a reason to take the offer.** The corrected number is
> **6**, and the canonical population is built on it.

---

## 5. `AR-F-02` re-verified — adopted, and already applied

| Check | Primary text | Result |
|---|---|---|
| What the precedent says | `SA_CORR3_07` §2.5: *"6 in force, 0 discharged. **Under the 8-Criteria Exit Constitution the whole conformance package is `PROVISIONAL / NON-CANONICAL`.**"* | applies a **grading** |
| Which clause produces that wording | Constitution **§9 — AAS+ / Design Handoff Rule**: *"AAS+ may explore designs in parallel only as `PROVISIONAL / NON-CANONICAL` while parent Very Deep Research is not yet complete."* | **§9. Not §4. Not `EC-07`** |

**CONFIRMED and already applied** at `SC-07` §4 — the precedent is withdrawn from Reading A in `SC-04`
§6.3 and `SC-06` §4. **The canonical treatment is at `SC-13`**, and it keeps the *fact* (a Phase SA
artefact did reach for this constitution) while stating the *clause*, which is what the evidence supports.

---

## 6. AR findings this session adopts that its own track did not have

| AR finding | Value to the canonical pack | Where it lands |
|---|---|---|
| **`AR-F-01`** | the corrected count | `SC-10` |
| **`AR-F-02`** | the clause-level narrowing of the one precedent | `SC-13` |
| **Reading B §3.1** — *every operative noun in the constitution is "Module" or "State", and Phase SA is neither*; §11's two operative rules name **Module → State** and **State → State** | **The strongest Reading B ground in either track. This session did not have it** | `SC-13` |
| **Reading B §3.2** — searched: **no artefact records Boss designating Phase SA as Very Deep Research**, which §2 item 5 makes the trigger | material, and a *negative measured with a search* rather than assumed | `SC-13` |
| **Reading B §3.3** — six consecutive Phase SA rounds ran under their own gate rules and **none invoked `EC-07`** | material | `SC-13` |
| **Reading A §2.4** — `SA_CORR3_13`'s own header reads `TARGETED VERY DEEP RESEARCH — EXECUTED, NOT CARRIED` | material **for Reading A**; adopted so the card does not weaken only one side | `SC-13` |
| `AR-I-01` | a multi-ref `git grep` over 189 refs returned a false zero **including for known-ruled identifiers**; loop one ref at a time | `SC-17` sweep design |
| `AR-I-02` | a relative path put `git cat-file` outside the repo and reported **11 good SHAs as broken**; use absolute paths plus known-good **and** known-bad controls | `SC-17` sweep design |

> **Six of these eight strengthen the case *against* the direction this session's own gate benefits from.**
> That is the point of consuming a peer track rather than citing it.

---

## 7. Where the two tracks agree, and it is most of the load

| Item | SC | AR | Agree? |
|---|---|---|:--:|
| PMO closure / Category 3 | `1 → 0`, verified by blob identity | `1 → 0`, seven checks, two disjoint sweeps | **YES** |
| Vetoes | 6 in force, 0 discharged, 0 held by SMEs Core | 6 in force, 0 discharged, 0 held by SMEs Core | **YES** |
| `AAS-V-02` | condition satisfied, discharge act pending, opens nothing | identical | **YES** |
| `RC-V-01` | under-inclusive condition; wider five-row set | identical | **YES** |
| Scenario categories | `10 / 12 / 0` and `9 / 9 / 0` | `10 / 12 / 0` and `9 / 9 / 0` | **YES** |
| Entry-gating members | `XMC-D-02`, `MTI-D-04`, `RC-D-01` | same three | **YES** |
| `ALREADY RULED` removals | 0 | 0 | **YES** |
| New Boss decisions originated | 0 | 0 | **YES** |
| Independence | 0 passes, none claimed | 0 passes, none claimed | **YES** |
| Relocated item | prepaid wallet → `ERPPLUS-152` | same | **YES** |
| Boss acts | 5 | 5 | **YES** |
| **`F5` count** | 8 (published) → **6** (corrected) | **6** | **YES, after correction** |
| **`C2-D-02`** | **CLOSED** by `XMC-C-C6` + `BD-ACC-01` | **RETAIN** — the `F3` re-read had not been performed | **NO — resolved at `SC-10` §4** |

> **One substantive disagreement survives, and it is not a contradiction — it is a time difference.**
> AR retained `C2-D-02` because the bounded `F3` re-read that closes it **had not yet been performed**;
> AR's own R2 records that re-read as owed to this track. **The disagreement is adjudicated at `SC-10` §4,
> with the reversal lever handed to Boss.**

---

## 8. Checkpoint

> ## `CP-SA-SC-80 — BOTH TRACKS REPRODUCED FROM PRIMARY SOURCE`
> **SC `c4949ec6` reproduced, manifest 11/11 · AR read at head `822cb327`, **two commits beyond the named
> baseline**, both consumed (`SC-F-09`) · `AR-F-01` and `AR-F-02` re-verified at primary source and both
> adopted · **`AR-F-01`'s number adopted and its reason corrected** (`SC-F-08`), surfacing two consequences
> neither track carried · 8 further AR findings adopted, 6 of them adverse to this session's own direction ·
> 13 of 14 comparison points agree · 1 disagreement, a time difference, routed to `SC-10` · **0 peer
> artefacts modified**.**

No Evidence = No Progress. Never Skip Gate. Verify before adopting a peer's finding.
Boss remains the sole Final Approver.
