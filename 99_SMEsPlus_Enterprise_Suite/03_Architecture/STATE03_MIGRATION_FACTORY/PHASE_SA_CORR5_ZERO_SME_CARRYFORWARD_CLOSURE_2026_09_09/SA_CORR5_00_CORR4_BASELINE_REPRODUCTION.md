# SA_CORR5_00 — CORR4 BASELINE REPRODUCTION

## CP-SA-C5-00 — CORR4 BASELINE REPRODUCED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Master prompt commit: `d33d83d1` · Parent CORR4 publication: `60752e2d`
Boss: **SOLE FINAL APPROVER**

---

## 1. Rule applied

Master prompt §3: *"Do not trust summary counts without reproducing them."* Every figure below was
re-derived from row-level text or from the repository, never copied from a CORR4 summary line. Where the
re-derivation disagrees with the summary, the disagreement is published as a baseline finding
(`C5-B-*`) and carried into the workstream that owns it.

---

## 2. Evidence frame — `CORR5-FRAME`, declared once

| Clause | Declaration |
|---|---|
| **POPULATION** | Every branch on `origin` at fetch 2026-09-09 (after the CORR5 prompt commit). **n = 186.** Three command shapes agree: `for-each-ref refs/remotes/origin` less `origin/HEAD` = 186 · `branch -r` less `HEAD` = 186 · `ls-remote --heads` = 186. *(CORR4 measured 185; the delta is this control branch.)* A **187th** branch, `governance/compliance-retraction-mainline-2026-09-09-001`, was created **by this session** during Workstream H and is outside this frame by construction; it is re-counted at `SA_CORR5_13` |
| **PATH SET** | Every path in the tree of every one of the 186 branch heads |
| **UNIT** | `U1` = **3,942** text blobs · `U2` = **3,620** text paths (`.md` / `.txt` / `.csv`). Never conflated. *(CORR4: 3,926 / 3,604 — delta +16 / +16: CORR4's own 13 package files, the CORR5 prompt, and two new mainline Boss artefacts, `SAAS_CELL/29` and `/30`, both dated 2026-09-09 — `C5-B-05`)* |
| **PATTERN** | Stated per measurement, published beside its result |
| **COMPLEMENT** | Non-head-history blobs; all non-`.md`/`.txt`/`.csv` files; the reference-ERP source trees and runtime dumps outside this clone. **The runtime dumps are entered for one bounded purpose only** — `SA_CORR5_07` §4, the `MTI-33` taxonomy — under their own declared instrument |
| **CONTROLS** | Positive (paths, `U2`, case-sensitive): `BD-ACC-01` **65** · `MTI-50` **27** · `MTI-18` **28** · `privileged` **98** · `FDS_AUDIT.md` present on **186 of 186** branch heads. Negative: `kqz51826_corr5_no_such_token` **0** — a fresh, single-use token (`C3-I-02`) |

### 2.1 `C5-I-01` — an instrument defect found in this frame, and corrected before any count was used

`git for-each-ref --format='%(refname:short)' refs/remotes/origin` prints the symbolic ref
`refs/remotes/origin/HEAD` with the short name **`origin`** — which a `grep -v HEAD` filter **does not
remove**. The first branch list therefore held **187** entries, and a per-branch loop over it counted
`origin/SMEsPlus` **twice**: the first compliance split read `184 / 3`, which sums to 187. Caught because
the split did not sum to the branch population measured by the other two shapes. **Every per-branch
count in this package uses the corrected 186-entry list.** Recorded because a `grep -v HEAD` looks
like the right filter and is not.

### 2.2 `C5-I-02` — reference dumps are readable only with the right tool generation

Five PostgreSQL custom-format dumps sit on the host (`SA_CORR5_07` §4). The host's default
`pg_restore 16.15` **refuses** the two written in archive format `1.16` (*"unsupported version (1.16) in
file header"*); `/opt/homebrew/opt/postgresql@18/bin/pg_restore 18.6` opens all five. **A negative about
own capability must name the tool version** — the programme's recorded rule — and the P07 session's
identical failure is on record. No dump was declared unreadable here.

---

## 3. The twelve baseline facts master prompt §3 requires, each reproduced

| # | CORR4 claim | Reproduction | Result |
|---:|---|---|---|
| 1 | `C4-01` CLOSED | `SA_CORR4_01` §4: **14** numbered path-class rows (grep, unit = row) · verdict line `ENUMERATION COMPLETE — EXACT BOUNDED GAPS LISTED` · `SA_CORR4_05` §2 row 1 `CLOSED` | **REPRODUCED** |
| 2 | `C4-02` CLOSED | `SA_CORR4_02` §3.1: **13** element rows · §4: **9** rule rows · §5: 10 flow rows → **2 `CONTRACT-SUFFICIENT` · 8 `CONTRACT-GAP`** (grep) · `SA_CORR4_05` row 2 `CLOSED` | **REPRODUCED** |
| 3 | `C4-03` CLOSED | `SA_CORR4_03` §3.13: **17** explicit `CF3-*` rows + the elided `CF3-N-01`…`-N-08` (8) = **25** · `MTI-43 CONTROL REFERENCE CLOSED` at specification level · `SA_CORR4_05` row 3 `CLOSED` | **REPRODUCED** |
| 4 | `C4-04` NOT CLOSED / `PROPAGATION HOLD` | `origin/SMEsPlus` head `27717bde` carries blob **`111bfc41`** (uncorrected) at the path; unauthenticated raw fetch → **`HTTP 200`**, line 215 `### **Standards Compliance**`; SHA-256 of the fetched body `cba4d748…33ba` hashes to git blob `111bfc41` (identity confirmed, not inferred). Split over 186 heads, **two shapes agree** (`rev-parse -q --verify` · `ls-tree`): **186 present · 0 absent · 183 uncorrected · 3 corrected** (CORR3, CORR4, this branch) | **REPRODUCED — and the exposure is live at reproduction time** |
| 5 | 22 of 22 `SA MATERIAL GAP` | `SA_CORR4_07` §4: 22 numbered rows, class column grep → **22 × `SA MATERIAL GAP`**, 0 other | **REPRODUCED** |
| 6 | Element 15 blocks all 22 | `SA_CORR4_07` §3 and §5 row *"Element 15 · all · 22"*; `SA_CORR3_06` §4.3 row 1 *"all 22"* | **REPRODUCED** |
| 7 | Six material Phase SA specification gaps, all non-Boss owners | `SA_CORR4_10` §7: **6** numbered rows (grep), owners `SMEs Core` ×5, `SA15/SA17's owner` ×1 | **REPRODUCED** |
| 8 | `MTI-05` contradicted | `SA_CORR4_06` §3 row 4 `CONTRADICTED`; ground `SA_CORR3_07` §6.1 `INV-PR-07` | **REPRODUCED as recorded — and the ground is re-examined: `C5-B-02`** |
| 9 | `MTI-22` register unclosed | `SA_CORR4_06` row 10 `SA-SPEC-GAP`, *"4 entries — 1 incomplete, 3 conditional"* | **REPRODUCED as recorded — and the count is stale: `C5-B-01`** |
| 10 | `MTI-33` Thai taxonomy unanswered | `SA_CORR4_06` row 15 `SA-SPEC-GAP`; `R4-Q-01` routed *"Thai business validation"*, no answer on any of 186 heads | **REPRODUCED** |
| 11 | `SA15`/`SA17` over-grade idempotency | `SA17` §2 row 18: `E2E-15` `TRAVERSABLE` · *"Strongest established area"*; `SA15` §2 row 15 *"strongest area: idempotency and ordering-independence established (`SA09`)"*; `SA09` carries an inline supersession *"idempotency moves the other way"*. Measured: `SUPERSEDED` (case-sensitive) `SA09`=1 · `SA15`=1 · `SA17`=**0**; `SA_CORR2_09` cited `SA09`=2 · `SA15`=0 · `SA17`=**0**; `RISK-C02` and *element 15* cited by `SA15`/`SA17`: **0 / 0** | **REPRODUCED** *(CORR4 counted `SA15`'s supersession blocks as 2; the second is the lower-case header parenthetical — an `-i` difference, immaterial)* |
| 12 | Runtime-only obligations not closable at Phase SA; 6 vetoes in force | `SA_CORR4_06` §5: 18 of 25 runtime · `0 of 8` isolation proofs · `0 of 13` surfaces · `0 of 41` functions · `0 of 60` negative cases (52 + 8) · vetoes enumerated by identifier across CORR2/3/4 text: `AAS-V-01`, `AAS-V-02`, `AAS-V-03`, `RC-V-01`, `CF-V-01`, `CF-V-02` = **6**, each with its issuing text located in the R1/R2 `12_AAS_PLUS_CHALLENGE_VERDICT.md` | **REPRODUCED** |

**CORR4 package integrity, reproduced:** `PACKAGE_MANIFEST_SHA256.txt` verifies **12 of 12**; the 8-hex
object identifiers cited across the 12 files resolve **20 of 20** (16 commits, 4 blobs), `0` unresolved.
Every CORR4 conclusion above stands as recorded. **What does not stand unchanged is five of the grounds
beneath them — §4.**

---

## 4. Baseline findings — where the re-derivation disagrees with the record

| ID | Finding | Owner in CORR5 |
|---|---|---|
| **`C5-B-01`** | **The `MTI-22` register has three entries, not four.** CORR4 (and CORR3) cite *"4 entries — 1 incomplete, 3 conditional"*, which is the **R1** register (`MULTI_TENANT_INVARIANT_SET_EXECUTION/06` §5, 2026-09-04). The **R2** register (`MTI_RULING_CONFORMANCE_EXECUTION/05_CROSS_CONTEXT_REGISTER_R2.md`, 2026-09-05) reads `REGISTER FALLS FROM 4 ENTRIES TO 3 — 1 INCOMPLETE, 2 CONDITIONAL, 0 UNCONDITIONALLY SETTLED — 1 REQUIRED RELATIONSHIP CLASS UNSPECIFIED`; `XCR-03` is **eliminated** by `CD-06`, and a fourth *required* class `CF-XCR-GAP-01` is deliberately **not** numbered. The programme's *supersession-binds-at-claim-level* rule was breached one level along: right package, superseded file | `SA_CORR5_07` |
| **`C5-B-02`** | **`MTI-05`'s `CONTRADICTED` grade rests on one of two readings of an ambiguous notation, and the record says so.** `SA_CORR3_07` §6.1 states both readings and *"not resolved here."* R2 `CD-04`/`CD-12` removed the two `X / Y` rows; **five `company + X` rows remain** (Lot/Serial, Reordering rule, Put-away rule, Adjustment/count, Scrap). Under reading (i) — *company, derived via X* — the invariant is honoured; under (ii) it is contradicted. **An unresolved reading is not a contradiction; it is an adjudication owed**, and it is owed by Phase SA, not by Boss | `SA_CORR5_07` |
| **`C5-B-03`** | **The Boss-decision list CORR4 carried contains two stale entries and one conflation.** (a) `C2-D-03` (kit category) was **resolved by CORR3** — `SA_CORR3_00` §3: *"`A` — RESOLVED. 0 Boss decisions"* — yet `SA_CORR4_10` §8 carries it. (b) `XD-01` survives only as the **severity-default election `XD1-P1`** (`SA_CORR3_12` §18 `B-1`), not as the design decision. (c) *"Is idempotency gate-blocking? `UAE-29`"* conflates two identifiers: **`UAE-29` is the Account programme's *"no accounting-event identity"* root blocker (P11 `B-02`), and Boss ruled it on 2026-09-08 as `BD-ACC-01`** — the closure act lists `BD-ACC-01` under *"must not be re-asked without material delta"*; the surviving severity question is the **Inventory `C-02`** ruling (*"gate-blocking, or design input"*, R4 `07_L6` line 210) | `SA_CORR5_01`, `SA_CORR5_15` |
| **`C5-B-04`** | **The "COGS gap, elements 4 and 7" carried on 12 scenarios is stated in two incompatible forms inside CORR3 and CORR4 inherited the older one.** `SA_CORR3_06` §4.3 lists *"COGS gap, elements 4 and 7 — 12 scenarios — Joint decision"*; `SA_CORR3_08` §2.3 grades element 4 **`N/A BY DESIGN, WITH REASON — a compliant N/A, not a gap`** and element 7 **`CARRIED`**. And the joint decision the gap named — `JT-01`, *"the ultimate design choice (adopt Category-as-owner…) → Boss"* — **was taken by Boss on 2026-09-08 as `BD-ACC-03A`/`03B`** (policy authority = Product Category; values `Periodic \| Perpetual` and `Standard \| Average \| FIFO`), five days after the COGS Targeted Resolution recorded it `NOT DECIDABLE`. `SA_CORR4_07` carries `el.4/7 COGS` on 12 rows without re-measuring against that ruling. The residual is re-measured at `SA_CORR5_10` §3 | `SA_CORR5_10` |
| **`C5-B-05`** | **Two Boss artefacts entered mainline on 2026-09-09 after CORR4's frame was declared** — `SAAS_CELL/29` (*Tenant Resource Governance & Capacity Work Package*, carrying invariants `TRG-01`…`TRG-18`) and `/30`. `TRG-01` *"Tenant execution context is mandatory for metered operations"* and `TRG-02` *"Cross-tenant usage attribution is prohibited"* **bear directly on `G5`** and were outside CORR4's population by the mechanism `SA_CORR4_01` §8.2 predicted. Consumed at `SA_CORR5_04` | `SA_CORR5_04` |
| **`C5-B-06`** | `SA_CORR4_06` row 20 (`MTI-46`) lists its two classes in the order *`SA-SPEC-COMPLETE` (count half) · `SA-SPEC-GAP` (value half)* while §3's counting rule declares its **primary** class `SA-SPEC-GAP`. A mechanical first-token count of the column returns **19 / 4 / 1 / 1**; the rule returns **18 / 5 / 1 / 1**. The published tally follows the rule; the row's cell order contradicts it. Immaterial to any conclusion; recorded because a total-that-sums-while-the-distribution-is-notation-dependent is the class CORR4 caught three times | `SA_CORR5_13` (notation only) |

**CORR4 conclusions overturned by this baseline: 0.** CORR4 grounds requiring re-measurement: **5**
(`C5-B-01`…`C5-B-05`). This is the same shape CORR4 recorded against CORR3 (`C4-B-01`…`04`): the
conclusions survive; the denominators and citations beneath them move.

---

## 5. What is frozen from CORR4 and not re-run

`C4-01`, `C4-02`, `C4-03` are **not re-executed**; their outputs are consumed as the baseline for
`G1`/`G3`/`G5` (`SA_CORR4_01` §4, §5, §9), the `XMC-C-D1` contract (`SA_CORR4_02` §3–§5) and the
`CF-I-03` control specification (`SA_CORR4_03` §3). `TVDR-04`/`TVDR-06`, `C2-D-03`, the
verdict-vocabulary question and the compliance-retraction **decision** are not re-asked (CORR3 §5.1,
CORR4 resume §2). Only the retraction's **mainline propagation** is CORR5 work (Workstream H).

---

## 6. Checkpoint

> ## `CP-SA-C5-00 — CORR4 BASELINE REPRODUCED`
> **12 of 12 baseline facts reproduced from row-level text · 12 of 12 manifest hashes · 20 of 20 cited
> objects resolve · frame re-declared at 186 / 3,942 / 3,620 with controls firing and a fresh negative
> control at 0 · 2 instrument findings (`C5-I-01`, `C5-I-02`) · 6 baseline findings (`C5-B-01`…`-06`),
> 0 conclusions overturned, 5 grounds sent for re-measurement.**

**Next autonomous action:** Workstream H was executed immediately after this checkpoint because the
exposure it closes is public and live (`SA_CORR5_08`); Workstream A follows (`SA_CORR5_01`).

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
