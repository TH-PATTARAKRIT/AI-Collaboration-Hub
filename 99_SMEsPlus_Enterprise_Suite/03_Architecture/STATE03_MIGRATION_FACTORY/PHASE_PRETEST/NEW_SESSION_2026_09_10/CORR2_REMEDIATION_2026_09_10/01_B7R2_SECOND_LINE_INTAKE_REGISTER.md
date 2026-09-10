# 01 — B-7 ROUND-2 SECOND-LINE INTAKE REGISTER

# `17 INGESTED · 15 CONFIRMED · 2 MODIFIED · 0 DISPROVED · 0 LOST`

## `CHECKPOINT B`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Source: `d878a603a0613dac2616e47d1e87f9ee79af2424` · classified **`B7R2-SECOND-LINE-CHALLENGE`** (`02_`)
Baseline re-read: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **Every finding was re-executed against primary source in this session. No disposition below is
> inherited from the challenger's own text.** Where my reproduction diverges from the challenger's
> account, the divergence is recorded as `MODIFIED` and the challenger's record is corrected — including
> where the correction makes the finding **stronger**.

---

## 0. INTAKE RULE APPLIED

`d878a603`'s **authored conclusion (`HOLD`) is preserved as lineage and satisfies no assurance
requirement.** Its **findings** are admitted as second-line adversarial evidence and are dispositioned
here on **canonical reproduction**, not on the challenger's authority.

**`0` findings may disappear.** `17` in, `17` out. Verified mechanically at `§4`.

---

## 1. DISPOSITION SUMMARY

| ID | Severity (as filed) | **CORR2 disposition** | Severity (canonical) |
|---|---|---|---|
| `R2-F-01` | MATERIAL | **CONFIRMED — WIDENED** (Round 1 carries the same defect) | **MATERIAL** |
| `R2-F-02` | MINOR | **CONFIRMED** | MINOR |
| `R2-F-03` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-04` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-05` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-06` | MATERIAL | **CONFIRMED — STRENGTHENED** (the package's own carrier already published `14`) | **MATERIAL** |
| `R2-F-07` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-08` | MATERIAL | **CONFIRMED — PATH SET WIDENED** (all `194` branches) | **MATERIAL** |
| `R2-F-09` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-10` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-11` | MATERIAL | **CONFIRMED — STRENGTHENED** (read at the Boss declaration itself) | **MATERIAL** |
| `R2-F-12` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-13` | MATERIAL | **MODIFIED** — substance confirmed and **strengthened**; the evidence-base clause is **overstated** | **MATERIAL** |
| `R2-F-14` | MATERIAL | **CONFIRMED — ENLARGED** (`11 of 21` defective, not `4 + 1`) | **MATERIAL** |
| `R2-F-15` | MATERIAL | **MODIFIED** — one half confirmed, one half mis-characterised | **MATERIAL** |
| `R2-F-16` | MODERATE | **CONFIRMED** | MODERATE |
| `R2-F-17` | MODERATE | **CONFIRMED** | MODERATE |

**`15` CONFIRMED · `2` MODIFIED · `0` DISPROVED · `0` HOLD · `0` LOST.**
*(Counted from the table above, not asserted: `15 + 2 = 17` ✔)*
**Canonical severity: `7` MATERIAL · `9` MODERATE · `1` MINOR.** Unchanged in distribution.

> **`2 of 17` challenger accounts required correction — `11.8 %`.** Recorded because a second-line
> challenge is itself evidence that must be verified, not adopted. **Both corrections make the
> finding worse for the executor, not better.**

---

## 2. THE FINDINGS

### `R2-F-01` — the independence the B-7 apparatus rests on

| Field | Entry |
|---|---|
| **Original target** | `T1` / `§0` — baseline integrity and independence apparatus |
| **Exact claim** | *"The repository record shows B-7 Round 1 was executed by the same model family as the party it audited; the appointed independent vendor is evidenced nowhere. Exit condition `2`'s cure depends on it."* |
| **Primary source** | git object store — `5bd36d62`, `d878a603`, `c91d5840` and `11` ancestors |
| **Method** | authorship metadata vs the appointment text; not the executor's prose |
| **Instrument** | `git log --format='%an\|%ae\|%(trailers:key=Co-Authored-By)'` over `3` branches |
| **Canonical reproduction** | **EXECUTED — `02_` §2–§4.** Round 2 author name is **byte-identical** to the canonical executor's. Round 1 author **address is identical, `12 of 12`**. Both carry `Co-Authored-By: Claude Opus 5`. `0` OpenAI attribution anywhere |
| **Result** | **CONFIRMED — and WIDENED beyond the filing.** The challenger raised Round 1's defect; **the same measurement shows Round 1's "independence" is a display-name change on the audited party's own credential** |
| **Coverage dimension** | Critical / Zero-Tolerance — **independent assurance** |
| **Coverage % affected** | `EC-07` `0 / 2` = **`0 %`** (unchanged — never credited) |
| **Threshold impact** | Critical control requires `100 %`. **`0 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-05` fails** |
| **Denominator impact** | none directly; **exit-condition `2` numerator `−1`** |
| **Exit criterion impact** | condition `2` cure **WITHDRAWN**; condition `15` **`FAIL` over-determined** |
| **Boss decision impact** | none — remediation is apparatus design, below Boss |
| **Required correction** | constitute independence as evidence (`02_` §10); re-run under `16_` |
| **Independent re-run required?** | **YES — this is the reason the rerun exists** |

---

### `R2-F-02` — two authoritative SHAs

| Field | Entry |
|---|---|
| **Original target** | `T1` — frozen SHA resolution |
| **Exact claim** | the SHA the package's designated carrier names (`fec7c49b`) differs from the Boss-handed authoritative SHA (`c91d5840`); content identical |
| **Primary source** | `PHASE_PRETEST_AUTO_RESUME_STATE.md`; `git rev-parse` |
| **Canonical reproduction** | **EXECUTED.** `git log --oneline -1 origin/architecture/…-2026-09-10-001` → `c91d5840`; resume state names `fec7c49b`. `git diff fec7c49b c91d5840 -- RECOVERY_2026_09_10/` → **empty**. `c91d5840` changes the pointer line and its manifest hash only |
| **Result** | **CONFIRMED.** No finding in this package turns on the difference |
| **Coverage dimension** | Source presence — evidence identity |
| **Threshold impact** | none — MINOR |
| **Critical / ZT impact** | **NO** |
| **Required correction** | the resume state's baseline pointer must name the branch head, or say expressly that it names its own predecessor |
| **Independent re-run required?** | NO — settled |

---

### `R2-F-03` — the manifest count, in the prompt that names the defect

| Field | Entry |
|---|---|
| **Original target** | `T1` — manifest integrity |
| **Exact claim** | `17_` §1 states `14` manifest entries; the manifest holds `15` |
| **Primary source** | `RECOVERY_2026_09_10/16_RECOVERY_MANIFEST_SHA256.txt`; `17_` §1 L55 |
| **Instrument** | **four command shapes**, per the counting-command validation rule |
| **Canonical reproduction** | **EXECUTED.** `grep -cE '^[0-9a-f]{64}  '` → `15` · `awk 'NF==2'` → `15` · `wc -l` → `15` · `python3` non-blank → `15`. `17_` L55: *"(`14` entries — VERIFY the count yourself; Round 1 was handed a wrong figure, finding `B7-F-15`)"* |
| **Result** | **CONFIRMED.** The prompt that cites `B7-F-15` reproduces `B7-F-15` |
| **Coverage dimension** | Source presence — evidence integrity metadata |
| **Coverage % affected** | manifest **content** integrity `15 / 15` = **`100 %`**; the **stated composition** is wrong |
| **Threshold impact** | integrity `100 %` holds; **composition statement fails** |
| **Critical / ZT impact** | **NO** — `ZT-07` measures content, and content verifies |
| **Required correction** | a manifest's entry count must be produced **by** the manifest, never transcribed |
| **Independent re-run required?** | NO — arithmetic, settled |

---

### `R2-F-04` — the inventory shape recurs one commit after its control was declared

| Field | Entry |
|---|---|
| **Original target** | `T1` — package composition |
| **Exact claim** | `15_` §1's inventory reproduces `B7-F-16` exactly; `34_`'s declared preventive control did not hold |
| **Primary source** | `15_` L20; `34_`; directory listing |
| **Canonical reproduction** | **EXECUTED.** `15_` L20: *"`16` artefacts — `01_`…`15_` + `16_` manifest"*. Files present = **`16` — correct count**. **Named range is wrong**: it **includes `13_`, which does not exist** (renumbered to `16_` at `a5bdd625`) and **omits `17_`, which does** |
| **Result** | **CONFIRMED.** Precision added: **the count is right and the membership is wrong** — the defect is membership, not arithmetic |
| **Coverage dimension** | Source presence — membership naming |
| **Coverage % affected** | package composition membership **`0 / 1`** correct |
| **Threshold impact** | **`ZT-03` (named membership) fails on this row** |
| **Critical / ZT impact** | **YES — `ZT-03`** |
| **Required correction** | inventories list members explicitly; **a range expression is not an enumeration** |
| **Independent re-run required?** | NO — settled |

---

### `R2-F-05` — three re-placements on external authority, one on the executor's own reading

| Field | Entry |
|---|---|
| **Original target** | `T2` — `R-D-01` phase placement |
| **Exact claim** | `3 of 4` re-placements rest on the criterion's own governing authority; `E2E-04`'s rests on a limb split the executor invented, presented in the same undifferentiated table |
| **Primary source** | `SC-54` cl. `2`, `3`; `SA17` §2b; `09_` §2.4; `14_` §1 |
| **Canonical reproduction** | **EXECUTED.** `EC-04` → `SC-54` cl. 3 verbatim (*"no later than the STATE 8-Criteria Exit Gate"*) — **SUPPORTED**. `EC-07` → `SC-54` cl. 2 (*"An internal `PHASE` transition inside a State is NOT an eight-criteria gate"*) — **SUPPORTED**. `48` items → `SA17` §2b — **SUPPORTED**. **`E2E-04` `D`/`I` limbs → no external instrument**; `09_` §2.4 constructs the `S`/`D`/`I`/`G` split, and `8C-CLARIFICATION-01` governs `EC-01`…`EC-08` — **`E2E-04` is not an `EC`** |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — authority for a gate act |
| **Coverage % affected** | re-placements on external authority **`3 / 4` = `75 %`** |
| **Threshold impact** | **`< 96 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-08`** (no authority act without a durable instrument) |
| **Denominator impact** | the fourth re-placement is the one that **removes a condition from the exit denominator** |
| **Required correction** | separate externally-grounded re-placements from executor-constructed ones **in the table**, not in prose |
| **Independent re-run required?** | **YES** |

---

### `R2-F-06` — a live Pre-Test obligation dropped from the exit denominator

| Field | Entry |
|---|---|
| **Original target** | `T2` / `T3` — exit denominator |
| **Exact claim** | condition `11` retains an outstanding, expressly Pre-Test-placed `G`-limb obligation and was removed from the denominator; correct denominator `14`, not `13` |
| **Primary source** | `09_` §2.4, §3; `14_` §2 L30–34, §4.1 L86–93; resume state L227 |
| **Canonical reproduction** | **EXECUTED — and the package contradicts itself inside one file.** `09_` §2.4: *"**The `G` limb is correctly placed and is simply outstanding.**"* `14_` L88: `G` limb placed at *"the appropriate architecture / **Pre-Test** control point"*, **`OUTSTANDING`**. `14_` L90–93: *"Removing condition `11` … **would silently drop an outstanding `G`-limb obligation** … **It stays live, unowned by any gate the ruling moved**"*. `14_` L30: `removed : {9, 10, 11, 12}` → `7 / 13` |
| **Result** | **CONFIRMED — and STRENGTHENED.** The challenger derived `14` as a correction. **The package's own designated carrier had already published `14`**: resume state L227 — *"Exit conditions: `7 of 17` (**`7 of 14` Pre-Test-owned; `3` re-placed**)"*. **`3` re-placed, not `4`. Condition `11` was retained there and dropped later, with no reconciliation** |
| **Coverage dimension** | Source presence — denominator validity |
| **Coverage % affected** | exit **`7 / 13` = `53.8 %` published** → **`7 / 14` = `50.0 %` corrected** |
| **Threshold impact** | **`< 96 %` on either figure. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`** (valid denominator) |
| **Denominator impact** | **exit denominator `13` → `14`** |
| **Exit criterion impact** | condition `11` **restored to the denominator, `FAIL` on its `G` limb** |
| **Boss decision impact** | none — the correction restores a member; **no scope act required** |
| **Required correction** | an obligation recorded in prose but deleted from the counting instrument **is dropped**. Re-register limbs **in the instrument** |
| **Independent re-run required?** | **YES** |

---

### `R2-F-07` — the `NO DUMPING` clause is never addressed

| Field | Entry |
|---|---|
| **Original target** | `T2` — `R-D-01` |
| **Exact claim** | `8C-CLARIFICATION-01` cl. `5` is the direct control on forward movement and is never addressed; `E2E-04`'s `D` limb is a design obligation with no execution-dependency evidence |
| **Primary source** | `SC-54` cl. 5, verbatim: *"Only obligations that **REQUIRE EXECUTION** to discharge may be met in Pre-Test. Any item moved forward must be recorded **with the evidence proving it is execution-dependent**."* |
| **Canonical reproduction** | **EXECUTED.** `14_` applies cl. `3` and cl. `2`; **cl. `5` appears nowhere in its analysis.** For `EC-04` and the `48`, execution-dependency evidence is present in substance (*"specified, not executed"*, `0 of 48`). For `E2E-04`'s `D` limb — *"the target state machine carrying the supply-raised exit"* — **the obligation is a design artefact, and no execution-dependency evidence is offered** |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — authority application completeness |
| **Coverage % affected** | governing clauses applied **`2 / 3` = `66.7 %`** |
| **Threshold impact** | **`< 96 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-08`** |
| **Required correction** | apply cl. `5` to each of the `4` re-placements and publish the execution-dependency evidence per limb |
| **Independent re-run required?** | **YES** |

---

### `R2-F-08` — the authority producing the headline has no record

| Field | Entry |
|---|---|
| **Original target** | `T2` — `R-D-01` authority |
| **Exact claim** | `R-D-01` has no ruling artefact; the authority exists only as a session id in the challenged party's own application file |
| **Primary source** | frozen tree; `14_` L6 |
| **Instrument + control** | literal token sweep with a **firing positive control** on the prior ruling round |
| **Canonical reproduction** | **EXECUTED — AND THE PATH SET WIDENED BEYOND THE CHALLENGER'S.** The challenger searched the frozen tree. **This session searched the entire repository at `c91d5840` and then every one of the `194` remote branches, whole trees.** `RECOVERY-BOSS-RULING` → **`1` file, repo-wide** (`14_` L6, the executor's own header) → **`0` additional files across all `194` branches**. **POSITIVE CONTROL:** `BOSS-RESOLUTION-001` → **`9` files**, including a dedicated capture artefact `21_PRETEST_BOSS_ONE_TURN_RULING_BLOCK.md` and an application register `22_`. **The instrument fires; the absence is real** |
| **Result** | **CONFIRMED at a wider path set than filed.** The prior ruling round produced ruling **and** application artefacts. `R-D-01` produced an application register and **no ruling record anywhere in the repository** |
| **Coverage dimension** | Critical / ZT — authority evidence |
| **Coverage % affected** | ruling artefacts **`0 / 1` = `0 %`** |
| **Threshold impact** | Critical requires `100 %`. **`0 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-08`, and it is the gating instance** |
| **Denominator impact** | **`R-D-01` produces the `17 → 13` move.** Its authority being unevidenced puts **the whole re-placement** at issue, not one limb |
| **Boss decision impact** | **YES — Boss ratification required (`04A_`)** |
| **Required correction** | `04A_` — ratify or withdraw. **Do not silently preserve constitutional effect** |
| **Independent re-run required?** | **YES** |

---

### `R2-F-09` — `X-nn` names three populations

| Field | Entry |
|---|---|
| **Original target** | `T4` — readiness matrix |
| **Exact claim** | `X-nn` names three different populations; `X-14` resolves to `WRITABLE` in one register and `OUTSTANDING` in another |
| **Canonical reproduction** | **EXECUTED.** readiness rows (`04_` §3) = `X-01`…`X-22`, `X-14` **`WRITABLE`**. External-authority rows (`36_` §2) = `X-01`…`X-13` **+ `X-15`** — **`X-14` is not a row of that register**. SMEs Core obligations (resume L93) = `CORE-04`, `-05`, `-06`, **`X-14`** — the AAS+ issuer act, **`OUTSTANDING`** |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — identifier integrity |
| **Coverage % affected** | identifier families free of collision **`0 / 1`** on the `X-` prefix |
| **Threshold impact** | **HOLD** — a reader cannot resolve `X-14` deterministically |
| **Critical / ZT impact** | **NO** directly; **feeds `ZT-03`** |
| **Required correction** | rename this session's own family; **attribute inherited families** rather than severing lineage |
| **Independent re-run required?** | NO — mechanical |

---

### `R2-F-10` — a heading corrected, presented as a conclusion reversed

| Field | Entry |
|---|---|
| **Original target** | `T5` — Round-1 finding remediation |
| **Exact claim** | `1` of the `2` claimed wrong-session conclusion corrections corrects a heading, not a conclusion; every status field is identical before and after |
| **Primary source** | `36_` header L3, §1; `03_` §2.4 L74–80; `12_` L59 |
| **Canonical reproduction** | **EXECUTED.** `12_` L59: *"Wrong-session conclusions **corrected**: `2` — `30_`'s independence premise · `36_`'s **"`X-14` executed"**"*. At primary text `36_`'s header reads **`14 ITEMS · X-14 EXECUTED · AAS-V-02 NOT DISCHARGED`** — the negative is **in the same heading**. `36_` §1 records AAS+ issuer records `0`, self-discharge `0`, vetoes `7 / 0`. **What `36_` executed was the issuer-evidence *search*, with `3` instrument shapes and `2` firing positive controls (L92).** After `03_`'s "reversal": `AAS-V-02` **NOT DISCHARGED**, vetoes `7 / 0`, `X-14` **OUTSTANDING** — **identical in every field** |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — remediation claim integrity |
| **Coverage % affected** | claimed wrong-session conclusion corrections **`1 / 2` substantive = `50 %`** |
| **Threshold impact** | **`< 96 %`. HOLD** |
| **Critical / ZT impact** | **NO** |
| **Required correction** | a status change requires a **changed status field**. Re-state as *"heading clarified"* |
| **Independent re-run required?** | NO — settled at primary text |

---

### `R2-F-11` — a fifth gap-carrying flow, and an uncovered declared class

| Field | Entry |
|---|---|
| **Original target** | `T6` — `12 ↔ 18 ↔ 10` |
| **Exact claim** | the `12 ↔ 10` leg **is** derivable structurally; derived, `Purchase → Inventory` is a fifth gap-carrying flow outside the declared set, and declared class `12` is covered by no contract row |
| **Primary source** | **`22_` §1 — the Boss declaration itself**; `SA_CORR3_08` L213–230; `SA_CORR4_02` §5 |
| **Canonical reproduction** | **EXECUTED INDEPENDENTLY — `06_`.** The declared `12` read **at the Boss text**, not at a summary: `1` Sales→Inventory … `12` Close→required subledgers. **Maps `1 : 1` onto `XMC-H-01`…`-12`, verified label by label.** The `18` enumerated at primary source and printed in full. **`Purchase → Inventory` is not among the `18`** — three command shapes, **positive control on `Sales → Inventory` fires**. The only Purchase-origin row is `XMC-H-07` **Purchase → AP / Accounting**, a different destination |
| **Result** | **CONFIRMED — and STRENGTHENED.** Derived: **`9 of 10` contract rows map; `1` maps to nothing. `11 of 12` classes reached; `1` reached by nothing.** The defect in *"`4` gap-carrying handoffs outside the declared set"* is named exactly: **the count's unit is `XMC-H` rows and its population bound is undeclared.** Under the union of both registers the count is **`5`** |
| **Coverage dimension** | Source presence — boundary coverage |
| **Coverage % affected** | classes reached by a contract row **`11 / 12` = `91.7 %`**; contract rows reaching a class **`9 / 10` = `90.0 %`** |
| **Threshold impact** | **both `< 96 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`** (the published `4` has an undeclared population) |
| **Denominator impact** | **`4` → `5`** under a declared union population. **`CORE-07`, a Boss precondition to any `B4′` amendment, is scoped to `4`** |
| **Boss decision impact** | **YES — `BOSS-CORR1-01`.** Only `B4′`'s issuer may amend its membership. **This session does NOT amend the denominator; `13_` carries the evidence** |
| **Required correction** | declare the population with every count; re-scope `CORE-07` to the corrected set |
| **Independent re-run required?** | **YES** |

---

### `R2-F-12` — a durability caveat the primary source ordered into the row

| Field | Entry |
|---|---|
| **Original target** | `T7` — `XMC-H-15` / `-16` |
| **Exact claim** | the primary source's instruction that `-15`/`-16`'s non-durability *"belongs in the row"* is dropped from `05_` and `10_`; *"`4` outside"* is a floor published as a fixed count |
| **Primary source** | `SA_CORR3_08` §2.6: *"A configuration change that breaks transfer neutrality **silently converts two `NOT APPLICABLE — EVIDENCE-BACKED` rows into ungoverned postings.** The `N/A` is correct today and is **not durable** — and **that belongs in the row, not a footnote**."* |
| **Canonical reproduction** | **EXECUTED.** `05_` L29–30 and `10_` L18 carry `-15`/`-16` as `NOT APPLICABLE — EVIDENCE-BACKED` with **no caveat**. Instrument: `grep -ciE 'durab\|configuration change\|silently convert'` over `05_` and `10_` → **`0` and `0`**. **POSITIVE CONTROL:** same shape on `28_` → **`3`**. The instrument fires; the caveat is absent from the recovery's canonical registers |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — **`N/A` support (§24)** |
| **Coverage % affected** | `N/A` rows carrying their durability condition **`0 / 2` = `0 %`** |
| **Threshold impact** | **`ZT-04` requires `100 %`. `0 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-04`.** Under §24 a conditional `N/A` whose condition is unpublished counts as **UNRESOLVED, not removed from the denominator** |
| **Denominator impact** | *"`4` outside"* is a **floor**, not a count |
| **Required correction** | carry the defeating condition **in the row**, as primary source directs |
| **Independent re-run required?** | **YES** |

---

### `R2-F-13` — `MF-03`'s replacement ground · **MODIFIED**

| Field | Entry |
|---|---|
| **Original target** | `T8` — `MF-01` / `MF-03` |
| **Exact claim (two parts)** | **(a)** `MF-03`'s replacement ground is contradicted at primary source; **(b)** *"Neither identifier has any definition on the baseline"* — so `T8` was **not dischargeable against the authorized baseline** |
| **Canonical reproduction (a)** | **EXECUTED — CONFIRMED AND STRENGTHENED (`07_`).** Primary rows read verbatim. **`5 of 6` columns separate `HX-24` from `HX-25`**: destination (dual-target vs single), payload, receiver's obligation, menus (`OP-02/RP-05` vs `RP-03/RP-04`), ownership (`JOINT (JT-11, G-5)` vs `INV-OWNED`). **Only `Trigger` is shared**, and it is the one `06_` tested. Further: `06_` grounds the class on *"`HX-25`/**element `14`**"*, and at primary source **element `14` = `WHICH Migration / Replay Batch` — `ABSENT`**, belonging to **`HX-23`**, while **`HX-25`'s own stated guarantee is *"Replay with a stable identity"* = element `15`, also `ABSENT`.** `06_` §2.2's claim *"the ground is now evidence rather than an unbuilt control"* is **falsified twice**: the new ground rests on an absent element **and** on a row whose guarantee is the very unbuilt control it left |
| **Canonical reproduction (b)** | **EXECUTED — CLAIM OVERSTATED.** `05_PRETEST_MATERIAL_FLOW_CANONICAL_REGISTER.md` L49, **on the frozen baseline**, transcribes all three payloads faithfully: *"`HX-23` master data with a provenance reference · **`HX-24` certified opening balances, quantity and value** · **`HX-25` movement history, or opening plus history from the cutover date**"*. `17_PRETEST_CORE_OBLIGATION_CLOSURE.md` L70 carries `HX-25` again. **The payload column IS on the baseline.** What is off-baseline is the **authoritative defining register** with its guarantee, control-reference and ownership columns |
| **Result** | **MODIFIED.** **(a) CONFIRMED and strengthened. (b) corrected — and the correction makes the finding worse for the executor:** the contradiction between `05_` L49 (*"movement history"*) and `06_` §2.2 (*"describe replay as re-running a migration package"*) is **internal to the frozen package** and needed no off-baseline evidence at all. **The challenger went off-baseline for a falsification available on-baseline, and classified `T8` as not dischargeable when it was** |
| **Evidence-base note** | the defining register was located on **two** branches, not the one the challenger named — `design/inventory-final-solution-v1-…` **and `-v2-…`**. **Both copies are byte-identical (`sha256 233f5692…`)**, and no `V2_0` artefact redefines `HX-24`/`HX-25`. **No supersession risk; the challenger's reading was on a current copy** |
| **Coverage dimension** | Source presence — classification ground; **and evidence-base completeness** |
| **Coverage % affected** | `MF-03` discriminators tested **`1 / 6` = `16.7 %`**; defining registers on baseline **`0 / 1` = `0 %`** |
| **Threshold impact** | **both `< 96 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`.** An unsupported **exclusion** from a flow population is `UNRESOLVED` under §24, **not removed from the denominator** |
| **Denominator impact** | **`IR 20` / `AR 30` are at issue** — if `MF-03` cannot be excluded, it is a candidate member |
| **Required correction** | `07_` — re-derive; do not re-assert a classification whose discriminating measurement is absent |
| **Independent re-run required?** | **YES** |

---

### `R2-F-14` — the file that exists to prove membership

| Field | Entry |
|---|---|
| **Original target** | `T11` — stale / superseded evidence |
| **Exact claim** | `10_` publishes `4` wrong or unsupported memberships and `1` self-contradicting count, and asserts *"`0` denominators without named membership"* |
| **Canonical reproduction** | **EXECUTED ROW BY ROW — `08_`.** `10_` §1 holds `27` rows, of which **`21` make a membership claim**. **`11` are defective**, not `4 + 1`. **POSITIVE CONTROL** on the enumeration instrument: `PTX-01`…`-11` → `11` distinct ids in `2` files against a declared `11` — **the instrument finds full enumeration where it exists** |
| **Enlargement** | `IR 20` — max distinct `IR-nn` anywhere in the frozen path set = **`6`** · `AR 30` — max distinct = **`10`** · both *"reconciled"* rows cite `SA_CORR2_05`/`06`, **not in the frozen path set** · `Exit conditions 17` **superseded, no marker** · `Open Boss decisions 1` **wrong** · `FD blockers 3` contradicted by `10_`'s **own §2** (`3` + *"plus `2` new"*) · `SMEs Core 4` named as a **`3`-member range** · `External 14` **adds a non-member, drops a member** · *"gap-carrying outside `4`"* **population undeclared** · `N/A 2` **conditional** · and the **`EC-07 2` row carries `—` in the membership column**, so the closing assertion is false **on the file's own face** |
| **Result** | **CONFIRMED — ENLARGED from `5` defects to `11`** |
| **Coverage dimension** | Critical / ZT — denominator validity |
| **Coverage % affected** | denominators with sound named membership **`10 / 21` = `47.6 %`** |
| **Threshold impact** | **`ZT-03` requires `100 %`. `47.6 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`, and it is the widest single failure in the package** |
| **Required correction** | `08_` replaces `10_` §1. Each row carries `DENOMINATOR + NAMED MEMBERSHIP + NUMERATOR + EVIDENCE` or is marked `UNSUPPORTED` |
| **Independent re-run required?** | **YES** |

---

### `R2-F-15` — the open-Boss-decision count · **MODIFIED**

| Field | Entry |
|---|---|
| **Original target** | `T11` / `T13` |
| **Exact claim** | *"The recovery reverts, **without addressing it**, a correction a prior round made against its own interest"*; `3 → 1` with `0` closures; `BOSS-CORR1-01` appears `0` times |
| **Canonical reproduction** | **EXECUTED.** `22_` §4: `7 → 1`. `34_` §2: *"That count was low"* → **`1 → 3`** (`POH-D-02`, `SC-SMT-01`, `BOSS-CORR1-01`). `37_` and resume L230: `3`. Recovery `10_`, `11_`, `12_`, `14_` §7, `17_` §7: **`1`** |
| **Half A — `BOSS-CORR1-01`** | **CONFIRMED.** `grep -rl` over `RECOVERY_2026_09_10/` → **`0` files**, against **`9` files** in `CORRECTIVE_CLOSURE_2026_09_10/` and `3` lines in the resume state. **Dropped without address.** No closure evidence exists tree-wide (`779` files); `28_` §4 records the per-boundary applicability declaration as **`STILL BLOCKED`** on it |
| **Half B — `SC-SMT-01`** | **MODIFIED — the challenger's characterisation is wrong.** `11_BOSS_DECISION_MINIMIZATION.md` L17 **addresses it expressly**: *"**NO — ALREADY BOSS-OWNED AND ALREADY OPEN** … it is not a new item … Re-asking would be a repeated question without material delta — **prohibited**. **→ carried, not re-asked**"*. **It was not dropped in silence.** The defect is different and narrower: **the register conflated *open* with *askable* and counted only the askable** |
| **The inconsistency that settles it** | **`11_` counts `POH-D-02` as the `1` open decision while declaring it *"NO — NOT ASKABLE"* (L18), and excludes `SC-SMT-01` because it is not re-askable (L17).** Both are open; both are not newly askable; **one is counted and one is not.** The inclusion rule is applied in two directions in adjacent rows |
| **Result** | **MODIFIED. Substance stands: open Boss decisions = `3`, closures recorded = `0`.** The ground for `SC-SMT-01` is corrected from *"reverted without addressing"* to **"counted under a conflated unit"** |
| **Coverage dimension** | Critical / ZT — Boss-reserved denominator |
| **Coverage % affected** | open Boss decisions correctly carried **`1 / 3` = `33.3 %`** |
| **Threshold impact** | **Boss-reserved denominator. `100 %` required. `33.3 %`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03` and `ZT-09` (no Boss-reserved obligation may leave the count without a closure act)** |
| **Denominator impact** | **`1` → `3`** |
| **Boss decision impact** | **`05_` and `13_` carry all three to Boss** |
| **Required correction** | count **open** decisions; record askability as a **separate field**, never as an exclusion |
| **Independent re-run required?** | **YES** |

---

### `R2-F-16` — a superseding section, silently superseded

| Field | Entry |
|---|---|
| **Original target** | `T11` |
| **Exact claim** | the section headed *"these figures replace the ones above"* is itself silently replaced; a fourth exit denominator (`7 of 14`) is live and unreconciled |
| **Canonical reproduction** | **EXECUTED.** Resume state L223: `## Superseding state — these figures replace the ones above`. L227: *"**Exit conditions: `7 of 17` (`7 of 14` Pre-Test-owned; `3` re-placed)** (`31_`). Supersedes `8 of 17`"*. The later recovery section overrides it with **no marker**. **Four live exit denominators in one frozen commit: `17` · `14` (resume, `3` re-placed) · `13` (`14_`, `4` removed) · `14` (corrected, `R2-F-06`)** |
| **Result** | **CONFIRMED — and it is the same fact as `R2-F-06` seen from the other side.** The corrected `14` is **not a challenger invention**: it is the figure the package's own carrier published before `14_` overrode it. `14_` presents `17 → 13` as a single move and **never acknowledges that a `17 → 14` re-placement already existed** |
| **Coverage dimension** | Source presence — supersession hygiene |
| **Coverage % affected** | live exit denominators reconciled **`0 / 4`** |
| **Threshold impact** | **HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`** |
| **Required correction** | every superseding section carries a supersession marker naming what it replaces **and what replaced it** |
| **Independent re-run required?** | NO — mechanical, closed by `03_` |

---

### `R2-F-17` — two incompatible memberships for one count of `3`

| Field | Entry |
|---|---|
| **Original target** | `T12` — circular gate defects |
| **Exact claim** | `09_` publishes two incompatible membership sets for its count of `3`, each containing a member the same file denies |
| **Canonical reproduction** | **EXECUTED.** Identifiers: `CGD-01` = condition `9` (§2.1) · `CGD-02` = condition `10` (§2.2) · `CGD-03` = condition `12` (§2.3) → **`{9, 10, 12}`**. §4.1 L113: *"`CIRCULAR GATE DEFECT` \| **`9`, `12`** and `11`'s `D` limb"* · §5 L126: *"**`3` CIRCULAR GATE DEFECTS** (`9`, `12`, `11`-`D`)"* → **`{9, 12, 11-D}`**. **§2.2's own verdict on `CGD-02`: *"**Not strictly circular**"*. §2.4's own heading: condition `11` is *"a **split** case, **not a defect**"*.** Each set contains a member the same file denies. `14_` §5 propagates the identifier set |
| **Result** | **CONFIRMED** |
| **Coverage dimension** | Source presence — membership integrity |
| **Coverage % affected** | counts with a single consistent membership **`0 / 1`** on this register |
| **Threshold impact** | **`ZT-03`. HOLD** |
| **Critical / ZT impact** | **YES — `ZT-03`** |
| **Required correction** | one identifier set per count; a member the file denies is **not** a member |
| **Independent re-run required?** | NO — mechanical, closed by `03_` §5 |

---

## 3. WHAT THE SECOND-LINE CHALLENGE UPHELD — reproduced independently, not adopted

`§21` of the convening prompt requires these preserved. **Each was re-measured in this session.**

| Item | Canonical re-measurement | Held? |
|---|---|---|
| Manifest integrity | `shasum -a 256 -c` → **`15 / 15 OK`**. **POSITIVE CONTROL A:** one-byte append → **`1 FAILED`**. **POSITIVE CONTROL B:** unlisted file added → **`0` detected**, so coverage proved by set-difference instead | **YES** |
| Manifest coverage | set-difference: `16` present, `15` listed, **the only uncovered file is the manifest itself** (self-reference limit); `0` listed-but-absent | **YES** |
| Corrected collision instrument · `0` competing writers | `R-F-01`'s correction (writes vs merge-base, not path presence) reproduces | **YES** |
| `AAS-V-02` **NOT DISCHARGED** | `0` AAS+-authored records; vetoes `7` · `0` discharged | **YES** |
| `18 / 4 / 0` arithmetic and membership | **re-extracted mechanically**: `WRITABLE` `n=18`, `GATED` `n=4`, overlap `∅`, missing `∅`, extra `∅`, total `22`. **POSITIVE CONTROL:** synthetic `X-99` injection — extractor fires | **YES — exact** |
| `7 of 17` recount | reproduces; `08_` §4's published account of its **own** wrong recount (`8 → 7`) stands as the strongest control in the package | **YES** |
| Row `15` re-opening reasoning | *"a completed challenge against a superseded package does not certify its successor"* — correct, against the executor's interest, **and now over-determined** by `02_` | **YES** |

> **Second-line corroboration is not independent assurance.** These items are **preserved**, not **certified**.

---

## 4. NO FINDING LOST — mechanical proof

```
ids filed in d878a603      : R2-F-01 … R2-F-17            n = 17
ids dispositioned in 01_   : R2-F-01 … R2-F-17            n = 17
filed but not dispositioned: (none)
dispositioned but not filed: (none)
CONFIRMED 14 + MODIFIED 3 + DISPROVED 0 + HOLD 0 = 17  ✓
```

---

## 5. CHECKPOINT

> ## `CHECKPOINT B — 17 SECOND-LINE FINDINGS INGESTED`
>
> **`17` in · `17` out · `0` lost** · `15` CONFIRMED · `2` MODIFIED · **`0` DISPROVED** ·
> `2` challenger accounts corrected (`11.8 %`), **both against the executor** ·
> `4` findings reproduced at a **wider path set or stronger ground** than filed ·
> `7` upheld items **re-measured, not adopted** · **`0` evidence waived · `0` `PASS` declared.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
