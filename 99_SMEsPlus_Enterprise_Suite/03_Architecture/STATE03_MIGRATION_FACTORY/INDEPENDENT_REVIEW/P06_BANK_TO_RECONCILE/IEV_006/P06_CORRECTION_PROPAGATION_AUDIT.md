# P06_CORRECTION_PROPAGATION_AUDIT.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-INDEPENDENT-EXTERNAL-CORRECTION-VERIFICATION-006]`
**Track:** INDEPENDENT EXTERNAL VERIFICATION · frozen surface `1b018c1`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. Propagation by claim class — measured, not inherited

The audited package's own propagation matrix marks **all nine classes COMPLETE** (`G02_VERIFICATION_2026_09_06/P06_CORRECTION_PROPAGATION_MATRIX.md`, Part I) and Part II re-marks five of them repaired. **Independent measurement on the frozen tree:**

| Class | Package says | **Independently measured** | Verdict |
|---|---|---|---|
| C1 `X-08` closure | COMPLETE | 11 CURRENT statements, all consistent, **none asserts closure** | **CONFIRMED COMPLETE** |
| C2 peer publication | COMPLETE | **3 survivors** — `36_`:42-43 (*"P08's **absence**"*), `40_`:17, `40_`:35 (*"7 of 9"*) | **NOT COMPLETE** |
| C3 evidence base | COMPLETE | **13 survivors across 7 files** — see §2 | **NOT COMPLETE** |
| C4 `is_matched` | COMPLETE | **2 defects** — `01_`:122 cites `:437` for `:438`; `:122` says two-by-configuration where one is amount-gated | **NOT COMPLETE** |
| C5 settlement ordinal | COMPLETE | **1 survivor** — `34_`:32 (*"a fifth path"*), a third ordinal in a file whose correction claims two | **NOT COMPLETE** |
| C6 ACL breadth | COMPLETE | 1 CURRENT, correct | **CONFIRMED COMPLETE** |
| C7 re-issuable | COMPLETE | 1 CURRENT, correct | **CONFIRMED COMPLETE** |
| C8 generation gap | COMPLETE | **2 survivors** — `18_`:188 (the retired half), `51_`:93 | **NOT COMPLETE** |
| C9 blocker population | COMPLETE | **4 wrong figures**, all of them REV-E-23 repairs: 65 published, **67** measured | **NOT COMPLETE** |

**7 of 9 classes carry survivors. 2 confirm complete.**

## 2. Why every survivor was invisible — the fourth consecutive occurrence

**`PA-F-01` — Not one survivor is a reasoning failure. Every one is a wording variant the class's declared pattern cannot match.**

| Class | Declared pattern | What defeated it |
|---|---|---|
| C3 | `filtered distribution\|filtered build\|filtered tree` (+ hyphen, round 7) | **`filtered subset`** · **`filtered checkout`** · **`filtered to the Thai deployment`** · **`filtered 791-addon tree`** · **`filtered-evidence-base`** · **`FILTERED 791-ADDON v18 TREE`** |
| C2 | `unpublished\|not published` | the noun **`absence`**; the ordinal **`7 of 9`** |
| C5 | `eighth settlement door\|eighth door` | **`a fifth path`** |
| C9 | `population at G02 close` | the header **`Blocker population`**; **`N blockers`** |
| C8 | `only deployment evidence` | the paraphrase **`If the target has moved to 19…`** |

**`P06-B-67` states that no pass has produced a population a later pass did not enlarge. This is the fourth pass, by a differently-briefed party, and it enlarges every class it touches. The blocker is now empirically supported four times over.**

## 3. The six-row table — the sharpest single illustration

`56_P06_FILTERED_TREE_EVIDENCE_BOUNDARY.md` §5 is one table of six negative-scope rows.

| Row | Scope column | Repaired? |
|---|---|---|
| `:62` `B-17` | `791-addon **filtered** v18 tree` | no |
| `:63` `B-34`/`B-35` | `same` | n/a |
| `:64` `is_internal_transfer` | `**filtered** 791-addon tree` | no |
| `:65` `destination_journal_id` | `**filtered** 791-addon tree` | no |
| `:66` `paired_internal_transfer` | `**filtered** 791-addon tree` | no |
| `:67` `provider_reference` | `**filtered** 791-addon tree` | no |
| **`:68` `chargeback\|dispute`** | **`loadable set (791 addons)`** | **YES — REV-E-23** |

**One row of six was repaired, in the file that produced the correction.** And `:53` of the same file prescribes the retired term as the **mandatory form for every future negative claim in the programme**.

## 4. Outbound propagation — what P06 currently hands its consumers

| Outbound artefact | Consumer | Stale CURRENT statements measured |
|---|---|---|
| `18_P06_CORE_RECON_HANDOFF_PACK.md` | **P11** | **5** — `:7` and `:212` completion language against a HOLD terminal state · `:188` the retired `B-44` half · `:208` `filtered-evidence-base` · `:214` publishing 65 blockers and *"three vetoes"* |
| `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` | **P11** | **1 sentence carrying 3 wrong figures** — 65 blockers, *"four active vetoes"* (7), *"16 recorded author errors"* (23) |
| `34_P06_CROSS_PROCESS_OWNERSHIP_REGISTER.md` | **P11** | **2** — `:44` asserting a peer **acceptance** on P06's own quoted sentence · `:32` the third ordinal |
| `36_P06_DEPENDENCY_REGISTER.md` | all peers | **1** — `:42-43` gating four items on *"P08's absence"* with the remedy *"one publication closes the chain"* |
| `40_P06_TARGETED_BLOCKER_REGISTER.md` | **P11** | **2** — `:17`, `:35` |
| `37_P06_SCOPE_REGISTER.md` | all peers | **1** — a seven/eight miscount with P08 excluded without declared authority |
| `12_P06_SOURCE_LINK_REGISTER.md` | controlling denominator | **2** — `:133` *"Branches read (7)"* listing eight and omitting P08 · `:154` the retired reading |
| `09_P06_CROSS_PROCESS_OWNERSHIP.md` | **P11** (indexed at `18_`:123) | **2** — `:13`, `:98`, the withdrawn terminal-process framing |

**`PA-F-02` — Every outbound artefact carries at least one stale current statement. The two P11-bound handoff packs carry a wrong blocker count, a wrong veto count and a wrong author-error count between them, and both figures were written by the repair round itself.**

**`PA-F-03` — `34_`:44 is the single most serious propagation defect in the package.** It is the only place P06 records that a peer has **accepted** a P06 row, and the quotation offered as evidence — *"Reconciliation must be journal-scoped, not account-scoped"* — occurs exactly twice on the frozen tree: at `09_`:80, where it is **P06's own sentence**, and at `34_`:44, where it is attributed to P11's intake. Two other files call the same rows *"net-new"* and *"will land"*. **A row cannot be net-new to a matrix, due to land in it, and already accepted into it.** This is precisely the shape `AASP-VETO-06` exists to forbid, committed in a P11-facing register.

**`PA-F-04` — And the control that should have caught it reported CLEAN on a string that is not in the file.** `P06_AAS_PLUS_CONSOLIDATION.md`:50 states `HO-03`/`HO-04` *"are labelled so"* — WRITTEN, NOT DELIVERED. The handoff pack contains **one** line matching `WRITTEN|DELIVER|deliver`: `:187`, *"the `X-08` answer, **re-delivered**"*. Two further statements certify the labelling *"verified by grep"* (`CHECKPOINT`:73, `PROPAGATION_MATRIX`:128). **Three governance statements assert a label that is absent, one of them citing a grep.**

## 5. What propagated correctly

- **The `X-08` family**, across seven files and eleven statements — the one surface three rounds got entirely right.
- **The unit declarations** (`assignment site` vs `branch`) at `25_`:67, `52_`:55, `62_`:35, `01_`:115 — consistently applied at all four sites.
- **The round-local and snapshot markers** at `21_`:42 and `SOURCE_LINK…`:151 — the correct instrument for a figure that was true when written.
- **`34_`:51's disposition tally** — independently recounted from the 20 `F-` rows: exact.
- **No peer-owned open item is converted to closed anywhere.** Every `P06-B-27` statement is permissive — *"P11 **may** strike it"* — never *"struck"*.
