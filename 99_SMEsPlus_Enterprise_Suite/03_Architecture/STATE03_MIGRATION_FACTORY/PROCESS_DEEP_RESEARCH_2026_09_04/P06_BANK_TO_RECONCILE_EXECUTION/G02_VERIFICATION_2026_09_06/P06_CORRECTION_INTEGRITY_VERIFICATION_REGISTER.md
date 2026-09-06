# P06_CORRECTION_INTEGRITY_VERIFICATION_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-CORRECTION-INTEGRITY-VERIFICATION-004]` · prompt commit `774aa0b`
**Session:** P06 — INDEPENDENT CORRECTION-INTEGRITY VERIFICATION (CP-P06V01)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Baseline verified:** `da987861a5f5586a01396a701d5108215f894d80` · research commit under audit `64429258b624239a8d1a9da6c751c2ea535dd238`

> **Method, stated before the result.** Nothing here is certified because the author said it was applied. **Every claim is reproduced from the committed tree**, using `git diff 18035d9..da98786` as ground truth — the pre-round and published states — rather than from the round-5 narrative. The narrative was then compared against that diff, and where they disagree, **the diff wins**.

---

## 1. Reproduction of the headline claim

**CLAIM UNDER AUDIT:** *"30 corrections applied in place across 15 register files."*

**EXECUTED:**
```
git diff --numstat 18035d9 da98786 -- <P06 package>/*.md
  → 16 modified files; 30 deleted lines total
  → 40_P06_TARGETED_BLOCKER_REGISTER.md is +38 / −0  (an APPEND — Appendix B — not a correction)
  → the other 15 files account for all 30 deletions
```
**Marker census against the committed tree** (`git show da98786:<file>`), not the working tree:
```
grep -ohE "REV-E-(18|19|20|21), 2026-09-06"  → 30 occurrences
grep -lE  "REV-E-(18|19|20|21), 2026-09-06"  → 15 files
```
**Per-file, deletions and markers agree exactly:** `01_`1 · `11_`1 · `12_`1 · `18_`5 · `20_`2 · `25_`1 · `34_`2 · `35_`5 · `36_`3 · `38_`1 · `39_`2 · `42_`1 · `46_`3 · `57_`1 · `70_`1 = **30**.

**VER-F-01 — The headline count is REPRODUCED. 30 corrections, 15 files, one marker per superseded line, verified two independent ways.** `FACT VERIFIED`.

> **A defect in this verification's own first instrument is recorded rather than hidden.** The initial per-file deletion count used `grep -c '^-[^-]'` and returned **27**, not 30. **Markdown bullet lines begin with `- `, so their diff line begins `--` and the pattern could not match them.** Caught because 27 disagreed with `git diff --numstat`. **This is the fifth "pattern that could not fire" in two rounds, and the first one found inside a verification instrument.** Recorded as `VER-E-01`.

## 2. The 30 corrections, enumerated and independently resulted

`RESULT` legend — **REPRODUCED**: the correction exists at the claimed location, the superseded wording is recoverable in the current text, and the corrected claim is accurate on re-execution. **DEFECT**: it is not.
`PROPAGATION` — whether every *other* current statement of the same claim in the package was also corrected.

| # | Original location (at `18035d9`) | Corrected location (current) | Family | Independent result | Downstream propagation | Disposition |
|---|---|---|---|---|---|---|
| `C-01` | `01_`:122 *"two of its three branches"* | `01_`:122 | `REV-E-11` | **DEFECT** — the repair wrote *"set `True` **unconditionally**"*. Re-executed `account_payment.py:436-452`: **only branch 3 assigns `True` unconditionally**; branch 4 assigns it **only when `journal_id.default_account_id` is among the liquidity-line accounts** — a configuration test. **The repair fixed the count and broke the qualifier** | disagreed with `18_`, `25_`, `46_`, which all say *"by configuration"* | **REPAIRED `REV-E-22`** → *"asserted `True` **by configuration alone**"* |
| `C-02` | `11_`:148 `T-10` *"no P08 branch exists"* | `11_`:148 | `REV-E-20` | REPRODUCED | see `VER-F-04` | **VERIFIED** |
| `C-03` | `12_`:150 *"a filtered distribution"* | `12_`:150 | `REV-E-16` | REPRODUCED | **INCOMPLETE** — `12_`:172 still said *"the filtered build"* | **REPAIRED `REV-E-22`** |
| `C-04` | `18_`:16 *"two of its three branches"* | `18_`:16 | `REV-E-11` | REPRODUCED, and **more accurate than `C-01`** | — | **VERIFIED** |
| `C-05` | `18_`:181 `B-6` *"An eighth settlement door"* | `18_`:181 | `REV-E-12` | REPRODUCED | **INCOMPLETE** — `40_`:78, `40_`:132, `46_`:89 still led with the withdrawn phrase | **REPAIRED `REV-E-22`** |
| `C-06` | `18_`:183 `B-8` *"a filtered distribution"* | `18_`:183 | `REV-E-16` | REPRODUCED. **Note:** the qualifier *"2 localisation packs, both Thai"* was dropped; it survives at `13_`:126 and `68_`:25, so no boundary was lost | **INCOMPLETE** — see `C-03` | **VERIFIED** (qualifier preserved elsewhere) |
| `C-07` | `18_`:184 `B-9` generation gap | `18_`:184 | `REV-E-10` | REPRODUCED — narrowed, not withdrawn; `P06-B-44` retained | consistent with `46_`:74 | **VERIFIED** |
| `C-08` | `18_`:198 *"answered and closable"* | `18_`:198 | `REV-E-18` | REPRODUCED. **This is one of the five P11-bound statements of prompt §4.5** | consistent across the 7-file `X-08` family | **VERIFIED** |
| `C-09` | `20_`:234 *"numbers become re-issuable"* | `20_`:236 | `REV-E-14` | REPRODUCED — cause moved to `sequence.mixin`, effect retained, finding correctly stated as *worsened* | `61_` `SRF-R-01` consistent | **VERIFIED** |
| `C-10` | `20_`:239 *"broad default ACL"* | `20_`:243 | `REV-E-09` | REPRODUCED — re-executed `base/security/ir.model.access.csv:129`: `base.group_system` only, no `unlink`. Conclusion correctly retained on the stronger basis | `45_`:81-83 consistent | **VERIFIED** |
| `C-11` | `25_`:40 *"2 of 3 branches"* | `25_`:40 | `REV-E-11` | REPRODUCED | **UNIT COLLISION** — `25_`:67 counts *assignment sites* (5) and says *"two set `True` unconditionally"*, which is correct **at site granularity** and reads as a contradiction of `25_`:40's branch count | **CLARIFIED `REV-E-22`** — the unit is now declared in both places |
| `C-12` | `34_`:40 `F-12` | `34_`:40 | `REV-E-18` | REPRODUCED | — | **VERIFIED** |
| `C-13` | `34_`:99 | `34_`:99 | `REV-E-18` | REPRODUCED | — | **VERIFIED** |
| `C-14` | `35_`:22 P08 *"NOT PUBLISHED"* | `35_`:22 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — see `VER-F-04` | **REPAIRED `REV-E-22`** |
| `C-15` | `35_`:121 *"P10 may close `X-08`"* | `35_`:123 | `REV-E-18` | REPRODUCED — P10's three registers re-read at `1fea562`; all three still `OPEN — PEER EVIDENCE` | — | **VERIFIED** |
| `C-16` | `35_`:137 P01 *"not published"* | `35_`:139 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — `35_`:15, the P01 row of the *same file's* peer table, was untouched | **REPAIRED `REV-E-22`** |
| `C-17` | `35_`:143 P08 *"not published"* | `35_`:145 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — `35_`:27 still said *"P01 and P08 remain unpublished"* | **REPAIRED `REV-E-22`** |
| `C-18` | `35_`:145 *"closed by P06"* | `35_`:147 | `REV-E-18` | REPRODUCED — the strongest of the nine; the false status claim is replaced and quoted | — | **VERIFIED** |
| `C-19` | `36_`:29 `D-11` | `36_`:29 | `REV-E-18` | REPRODUCED | — | **VERIFIED** |
| `C-20` | `36_`:33 `D-15` *"no P08 exists"* | `36_`:33 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — `36_`:13 `D-02`, the *adjacent row*, still said *"branch not published"* for P08 | **REPAIRED `REV-E-22`** |
| `C-21` | `36_`:61 `DEP-F-03` | `36_`:61 | `REV-E-20` | REPRODUCED — and the consequence correctly **strengthened**, not softened | **INCOMPLETE** — `36_`:68 still said *"Two of nine inbound dependencies are unpublished counterparties"* | **REPAIRED `REV-E-22`** |
| `C-22` | `38_`:63 *"a filtered distribution"* | `38_`:63 | `REV-E-16` | REPRODUCED | **INCOMPLETE** — `38_`:86-87 asserted P01/P08 unpublished | **REPAIRED `REV-E-22`** |
| `C-23` | `39_`:96 *"may be closed"* | `39_`:96 | `REV-E-18` | REPRODUCED | — | **VERIFIED** |
| `C-24` | `39_`:98 *"no P08 exists"* | `39_`:98 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — `39_`:27 restated `B-55` in the superseded terms | **REPAIRED `REV-E-22`** |
| `C-25` | `42_`:25 *"filtered distribution"* | `42_`:25 | `REV-E-16` | **DEFECT** — the corrected sentence's own trailing clause still read *"a second search over a **filtered tree** is a second search over the same **filter**"* | **INCOMPLETE** — `42_`:67, `42_`:71 uncorrected; `42_`:22 asserted P01 *"cannot be read"* | **REPAIRED `REV-E-22`** ×4 |
| `C-26` | `46_`:47 `B-06` *"2 of 3 branches"* | `46_`:47 | `REV-E-11` | REPRODUCED | — | **VERIFIED** |
| `C-27` | `46_`:74 `B-44` generation gap | `46_`:74 | `REV-E-10` | REPRODUCED | — | **VERIFIED** |
| `C-28` | `46_`:95 `B-54` *"P01 unpublished"* | `46_`:95 | `REV-E-20` | REPRODUCED | **INCOMPLETE** — `46_`:77, the register's **own `B-55` row**, still carried *"Evidence base is a filtered distribution"* marked `FACT VERIFIED` | **REPAIRED `REV-E-22`** |
| `C-29` | `57_`:31 | `57_`:31 | `REV-E-18` | REPRODUCED | — | **VERIFIED** |
| `C-30` | `70_`:71 *"answered and closable"* | `70_`:71 | `REV-E-18` | REPRODUCED. **P11-bound; `70_` carries no other stale claim** — checked | — | **VERIFIED** |

**TALLY, executed:** **28 REPRODUCED · 2 DEFECT** (`C-01`, `C-25`) · **1 UNIT COLLISION** (`C-11`) · **12 with INCOMPLETE downstream propagation**.

## 3. Verification findings

**`VER-F-01` — The count is real.** 30 corrections, 15 files, reproduced from the diff and from the marker census independently. §4.1 **SATISFIED**.

**`VER-F-02` — Superseded wording is recoverable in all 30.** Each correction either quotes the original verbatim (*"Superseded wording: …"*), strikes it through (`~~…~~`), or preserves the original clause and appends. **Nothing was silently overwritten.** §4.2 **SATISFIED**.

**`VER-F-03` — Two corrections are themselves defective.**
- **`C-01`** introduced a **false qualifier** into the payment-state model: *"set `True` unconditionally"* where source says one branch is unconditional and one is configuration-gated. **A repair that fixes a count and breaks a semantic qualifier is worse than the error it replaced**, because the count was obviously checkable and the qualifier is not.
- **`C-25`** corrected a sentence and left **the same sentence's own trailing clause** using the superseded term twice.

**`VER-F-04` — The publication-status population was under-enumerated by a factor of six, and this is the round's governing finding.**

Round 5 searched for the **peer name**. The verifier searched for the **claim class**:
```
grep -rn "not published|NOT PUBLISHED|unpublished|not yet published" *.md
  → 19 current statements across 16 files asserting P01 and/or P08 unpublished
  → 8 had been corrected in round 5
  → 11 had NOT
```
And the authority was executed rather than assumed:
```
git ls-remote --heads origin | grep research/account-p
  → research/account-p01 … p10  — ALL TEN peer branches exist
```
**Eleven false current statements survived**, including:
- **`66_`:16 — an AAS+ VETO CONDITION**, recorded as `NOT MET — still unpublished`. **A veto condition was standing on a false premise.** It is still `NOT MET`, but for a materially different reason: **unmet by scope, not by availability.**
- `42_`:22 — *"P01 is unpublished and **cannot be read**."*
- `34_`:25 — the register's **legend**, defining `OPEN` as *"counterparty unpublished"*.
- `28_`:86 — *"`research/account-p08-*` is absent from origin"*, a positively false factual assertion about a remote.
- `40_`:79 `B-54`, `36_`:13 `D-02`, `38_`:86-87, `43_`:130, `53_`:111, `54_`:99, `19_`:210, `23_`:95, `35_`:27, `34_`:34/:43/:45/:51.

**Correctly left alone** — three statements are explicitly time-bounded and remain true as written: `12_`:84 (*"Class A within that scope and instant … Class B thereafter, and this package must be re-checked"* — which is exactly the re-check now performed), `11_`:85 `T-08` and `09_`:108 (*"at fetch time"*). **A time-bounded negative survives a boundary move; an unbounded one rots.** The package's own standing lesson, and here it is the difference between 3 correct statements and 11 false ones.

**`VER-F-05` — The `REV-E-16` population was under-enumerated too.** Round 5 named four statements; the true population is **eleven**, including `46_`:77 — the **severity register's own `B-55` row**, marked `FACT VERIFIED` on wording the same round was correcting.

**`VER-F-06` — A repair-introduced arithmetic error.** `46_` Supplemental Note 2 said *"Four further blockers"* and *"population at G02 close is **62**"*. `40_` Appendix B lists **five** (`B-59`…`B-63`) and the executed count is **63**. Re-executed and repaired.

**`VER-F-07` — A rendering defect in nine places.** Embedding `**[marker]**` inside an already-bold run produced `****`, which breaks emphasis in rendered Markdown. **Eight of the nine were created by the round-5 repair**, four of them in `35_`, the peer handoff matrix. Text was never lost; legibility was. All nine repaired.

**`VER-F-08` — §4.5 is satisfied.** The five P11-bound superseded statements are exactly `18_`:16, `:181`, `:183`, `:184`, `:198`, all corrected in the current outbound pack; `70_` carries one correction and no other stale claim; `35_` and `36_` are corrected and now complete.

**`VER-F-09` — §4.6 and §4.7 hold, with one exception.** Finding classes (`FACT VERIFIED` / `SUPPORTED INTERPRETATION`), denominators, path sets, version bounds and negative-claim classes survive every correction — **except `C-01`'s qualifier** (`VER-F-03`) and `46_`:77's class, which was `FACT VERIFIED` over superseded wording (`VER-F-05`).

**`VER-F-10` — §4.8: two contradictions were introduced by the repair and both are now closed.** `C-01` against `18_`/`25_`/`46_`; and `P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md`:77, where the round-5 artefact **restated `B-55` in the very wording that same round was correcting**.

**`VER-F-11` — Identifier variance, recorded not resolved.** The prompt names `P06-Q-98`; the package uses **`P06-OQ-98`** throughout. Read as the same item. **No identifier was renamed** — renaming a Boss-named item on inference is not the verifier's call.

## 4. Repairs applied by this verification

**Bounded to the affected statements only, per prompt §7.** Marker: `[REV-E-22, 2026-09-06]`.

```
grep -ohE "REV-E-22, 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md | wc -l   →  40
grep -lE  "REV-E-22, 2026-09-06" *.md G02_CLOSURE_2026_09_06/*.md | wc -l   →  20
```
**40 repairs across 20 files.** The round-5 marker census is unchanged at **30 / 15** — no round-5 correction was overwritten.

**No new research was performed.** The only external facts consulted are `git ls-remote --heads origin` (a status field, the one thing only the owner's ref can state) and a re-read of `account_payment.py:436-452` and `ir.model.access.csv:129` — both already in the package's declared source scope and cited in the corrections under audit. **No filesystem or archive root was widened; no peer package was opened; no database was touched.**

## 5. Independent AAS-03 challenges — correction surface only

### Expert 1 — Leader Functional Design
**SUPPORTED.** The `X-08` family (9 corrections, 7 files) is internally consistent: every one now says *answered by P06, closable only by P10*, and none claims closure. The Candidate I/P/O/Handoff pack's `HO-04` says the same. **No semantic drift across the family.**
**CONTRADICTED.** `C-01`. *"Unconditionally"* is not what the source does, and the repair asserted it in the package's **primary payment-state model** while three other files said the correct thing.
**NARROWED.** `C-05`: *"eighth door"* is withdrawn in `18_` but `40_`:78 — the **primary blocker row** — still led with the withdrawn phrase. A peer reading the register rather than the handoff pack would have taken it as current.
**MISSING EVIDENCE.** None. Every disputed statement was resolvable from files already in scope.
**MATERIAL CORRECTION DEFECT: YES** — `C-01`, `C-05`.

### Expert 2 — Leadership Database Design
**SUPPORTED.** `C-10`'s ACL correction re-executes exactly: `ir.model.access.csv:129` grants `base.group_system` only. Denominators in `C-06`/`C-25` (791 / 1752 / 961 / 904) are consistent wherever they appear.
**CONTRADICTED.** **`46_`:77.** The severity register's own `B-55` row carried the superseded claim **and its `FACT VERIFIED` class**. *A class attached to a superseded claim is a false assurance about the claim, not just about the wording.*
**NARROWED.** `C-11`. The site-vs-branch unit collision is not an error in either statement — it is an undeclared unit, which is the defect class this package has recorded four times.
**MISSING EVIDENCE.** None.
**MATERIAL CORRECTION DEFECT: YES** — `46_`:77.

### Expert 3 — Lead Integration & Localization
**SUPPORTED.** §4.5 is met: the five P11-bound statements are corrected in `18_`, and `70_` is clean.
**CONTRADICTED.** **`VER-F-04`.** Eleven false current statements about peer publication status survived, in files P11 and other peers read — `35_`, `36_`, `38_`, `40_`, `42_`, `43_`, `53_`, `54_`, `66_`, `34_`, `19_`, `23_`, `28_`. **`66_`:16 is a veto condition.** An outbound package that tells a peer *"P01 cannot be read"* when P01 has been published for two days is a boundary-wording failure of exactly the kind this expert exists to catch.
**NARROWED.** The repairs correct **status** only. **No peer package was consumed**, and the dependencies stay OPEN — publication is not closure. `P06-OQ-124` (P01) and new `P06-OQ-128` (the other eight unconsumed peers) carry it.
**MISSING EVIDENCE.** Whether P11 has a published branch: no `research/account-p11-*` head exists on `origin`, so **no claim is made about P11** either way.
**MATERIAL CORRECTION DEFECT: YES** — eleven statements, one of them a veto condition.

### Expert 4 — Lead Code & UI Architect
**SUPPORTED.** All 30 corrections are reproducible from the committed tree by SHA, and the per-file marker/deletion agreement is exact. Source citations re-execute at the stated lines (`account_payment.py:436-452`, `ir.model.access.csv:129`, `accrued_orders.py:253`).
**CONTRADICTED.** **`VER-E-01`** — this verification's own first counting instrument was broken by a markdown-bullet pattern and returned 27 for 30. **Had `git diff --numstat` not disagreed with it, this register would have opened by reporting a count that undercut the claim it was auditing.**
**NARROWED.** `VER-F-07`, the `****` rendering defect: real, non-semantic, and concentrated in the peer handoff matrix.
**MISSING EVIDENCE.** The corrected files' hashes in `P06_EVIDENCE_MANIFEST_G02.md` §2 are now **stale by construction** — every verification repair changes them. Regenerated at publication and flagged.
**MATERIAL CORRECTION DEFECT: YES** — `VER-E-01` is a defect in the verification, not in the corrections, and it is reported as such.

**DISSENT PRESERVED.** All four experts report a material correction defect. **None argues that `AASP-VETO-07` should be discharged on this pass**; Expert 3 argues specifically that it must not be, because the defect it found — eleven false outbound statements, one a veto condition — was invisible to the round-5 pass **and to this verifier's own first sweep**, which also searched by peer name before switching to the claim class.

## 6. `AASP-VETO-07`

**NOT DISCHARGED.**

Prompt §9: *"If even one material stale or incorrect current claim survives, preserve the veto."* **Fifteen did** — 11 publication-status, 2 correction defects (`C-01`, `C-25`), 1 severity-register row with a false class, 1 repair-introduced arithmetic error. All are now repaired, **by the same party again**.

**The recommendation this register makes is not discharge.** It is that **`AASP-VETO-07` now attaches to a smaller and precisely enumerated surface**: the **40 `REV-E-22` repairs across 20 files**, greppable by one command, none of which has been independently verified. The condition to lift is unchanged in kind and much cheaper in size.

**One thing did change, and it is the argument for the next pass being independent too:** the round-5 pass and this verifier's own first sweep **made the same mistake** — scoping a correction population by the phrase they remembered instead of by the claim class. It took a deliberate re-scoping to find the other eleven. **A third pass by this same party would probably repeat the pattern a third time.**
