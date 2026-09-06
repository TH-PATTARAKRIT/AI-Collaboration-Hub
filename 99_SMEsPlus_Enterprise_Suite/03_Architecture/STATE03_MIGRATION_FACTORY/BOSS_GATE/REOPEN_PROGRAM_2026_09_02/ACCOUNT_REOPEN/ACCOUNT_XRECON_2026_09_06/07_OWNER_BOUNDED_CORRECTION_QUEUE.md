# 07_OWNER_BOUNDED_CORRECTION_QUEUE

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`

> **No queue item is executed in this session.** Each item names one accountable owner, exact files, the exact
> wrong claim, the correct truth, the prohibited scope widening, and a completion condition.

---

## Queue summary

| Owner | Items | Root defects | Fresh challenges |
|---|---|---|---|
| **P06** (source + IEV track) | **4** | `XRD-001`, `XRD-002`, `XRD-003`, `XRD-004` | `RC-03`, `RC-04` |
| **P08** (source + IEV track) | **3** | `XRD-006`(half), `XRD-007`, `XRD-011`(origin) | `RC-05` |
| **P09** | **2** | `XRD-010`(`M-2`), plus `M-1` | `RC-01` |
| **P11** | **4** | `XRD-005`, `XRD-006`(half), `XRD-008`, `XRD-011`(consumption) | `RC-02`, `RC-06` |
| **Boss** | **1** | `XRD-009` | — |
| **Adjacent (P07)** | **0 repairs** | routed only — see §6 | — |

**Total: 13 owner-bounded items + 1 authority item. 0 executed here.**

---

# P06 QUEUE

## `Q-P06-01` — propagate the addendum's revised totals *(`XRD-001`)*

| | |
|---|---|
| **Root defect** | `XRD-001` · **local ids** `ADDENDUM_E2` §7, `IEV-I-05` |
| **Owner** | **P06 — IEV track**, branch `audit/p06-independent-verifier-2026-09-06-001` @ `b423eff` |
| **Exact files** | `IEV_006/P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md`:14, :24, :30 · `…CORRECTION_VERIFICATION_REGISTER.md`:83 · `…AUTO_RESUME_STATE.md`:22, :33, :43 · `…CHECKPOINT_REGISTER.md`:19 |
| **Exact wrong claim** | *"18 material defects"* (×5) · *"15 repair requirements"* · *"THREE OF FOUR RETURNED"* · Expert 2 *"TERMINALLY DISPOSITIONED … no finding in this package depends on it"* |
| **Current evidence** | `git diff --stat dac6ac3 b423eff` → 3 files; **the terminal report is not among them**. The revised totals exist in **one** artefact |
| **Correct truth** | **25** material defects · **2** verifier-authored · **19** repair requirements · **4 of 4** challengers · **the Expert-2 disposition is falsified by its own author** |
| **Required correction** | Propagate **by identifier** into all four carriers, retaining 18/15/3-of-4 as **marked-superseded lineage**. Replace the Expert-2 disposition with the falsification |
| **PROHIBITED scope widening** | Do **not** re-open the 25 findings · do **not** re-audit the source package · do **not** repair P06's source files from the audit branch · do **not** discharge `AASP-VETO-07` |
| **Propagation carriers** | terminal report · correction register · auto-resume · checkpoint register |
| **Re-test** | re-count the material-defect population and **publish the enumeration, not the total** |
| **Fresh challenge** | **`RC-03` — REQUIRED, and not by the actor that authored either the repairs or this audit** |
| **Veto impact** | `AASP-VETO-07` remains **PRESERVED** either way |
| **Boss impact** | none directly; **but the Boss's current brief cites 25/2/19 against a terminal report saying 18/15** |
| **Completion condition** | four carriers carry 25/2/19/4-of-4 with lineage retained; population re-enumerated; `RC-03` complete |

## `Q-P06-02` — correct the validation row that certifies a superseded figure *(`XRD-002`)*

| | |
|---|---|
| **Root defect** | `XRD-002` · **local id** `IEV-D-20` |
| **Owner** | **P06 — IEV track** |
| **Exact file** | `IEV_006/P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45 (contradicted by `:54`) |
| **Exact wrong claim** | *"65 `P06-B-*` … max id = 65 and contiguous"* — validation result **`YES`** |
| **Current evidence** | **XRECON `XS-01`**: 67, two instrument forms, `diff`-identical sets, contiguous 01–67, injection control 67 → 68 |
| **Correct truth** | **67**, contiguous |
| **Required correction** | `:45` → **67**; re-state the validation result. **Retain the original row as marked-superseded** — the addendum left it standing deliberately so the defect stays legible |
| **PROHIBITED** | do **not** silently overwrite · do **not** re-scope the instrument register |
| **Re-test** | re-run the contiguity validation; publish the enumeration |
| **Fresh challenge** | **NOT REQUIRED** — independently confirmed here by two instruments plus a positive control |
| **Completion condition** | `:45` reads 67, superseded row retained, validation re-run and published |

## `Q-P06-03` — correct four count families in the source package *(`XRD-003`)*

| | |
|---|---|
| **Root defect** | `XRD-003` · **local ids** IEV requirements 1, 2 · `IEV-D-19`, `IEV-D-21` |
| **Owner** | **P06 — source**, branch `research/account-p06-bank-to-reconcile-2026-09-04-001` @ `1b018c1` |
| **Exact files** | `13_`:94 (65), `13_`:95 (66) · `46_`:124 (65) · `18_`:214 · `70_`:108 · `40_`:288 (23) |
| **Exact wrong claims** | blocker count **65** · open-item population **66** · *"three vetoes"* / *"four active vetoes"* · *"16 recorded author errors"* / **23** |
| **Current evidence** | **XRECON `XS-01`** (67, two forms + injection control) · `IEV-D-19` (68, its own printed command) · `IEV-D-21` (`REV-E-22`/`-23` carry **no definition line in any file**; 21 of 21 others do) |
| **Correct truth** | **67** · **68** · **seven** vetoes · **21** author errors |
| **Required correction** | Correct all four families; **re-scale `P06-B-58`**, the reliance-risk blocker, which is scaled on the author-error number; **re-execute each count at publication and publish the command with its output** |
| **PROHIBITED** | do **not** re-open the research findings — every source-level claim re-executed and **held** · do **not** widen to new roots · do **not** convert any peer-owned item |
| **Propagation carriers** | `13_`, `46_`, `18_`, `70_`, `40_` — **and `18_`/`70_` are the two P11-bound handoffs** |
| **Downstream notification** | **P11 must be told.** `XRECON` measured that the wrong counts **did not** cross into P11's substance — but P11's pin is stale regardless (`XRD-005`) |
| **Re-test** | every corrected count re-executed at publication |
| **Fresh challenge** | **`RC-04` — REQUIRED** |
| **Veto impact** | `AASP-VETO-07` preserved; two families sit in the P11-bound handoffs |
| **Completion condition** | five files corrected, `P06-B-58` re-scaled, commands + outputs published, `RC-04` complete |

## `Q-P06-04` — re-run the archive negative with a pattern proved to fire *(`XRD-004`)*

| | |
|---|---|
| **Root defect** | `XRD-004` · **local ids** `IEV-D-26`, consequence `FTB-F-07` |
| **Owner** | **P06 — source** |
| **Exact files** | `56_`:99 (the search) · the `FTB-F-07` statement generalising to **1,752 directories** |
| **Exact wrong control** | pattern `payment_return\|bounce\|dishonou?r\|post_dated\|postdated` published with **no command, no `-E`/`-F` flag and no path expression**, over a declared **961-directory** archive, yielding *"No bank-return concept"* |
| **Current evidence** | tested against a controlled fixture under both modes: **BRE** — `dishonou?r` matches **0 of 2** real spellings (`?` is literal in BRE); **ERE** — the **entire pattern matches 0 of 5**. In BRE the surviving branches still fire, *"which is why the result reads as a plausible finding rather than a crash"* |
| **Correct truth** | **the negative is unevidenced under either grep mode** |
| **Required correction** | Re-run with a pattern **proved to fire**, with a **positive control inside the search population**; publish the **command and its grep mode**; then re-state or withdraw `FTB-F-07`'s 1,752-directory generalisation on the new result |
| **PROHIBITED** | do **not** widen beyond the declared archive · do **not** publish the new negative without its command, mode and positive control |
| **Re-test** | inherent |
| **Fresh challenge** | **`RC-04` — REQUIRED** (both the negative and its consequence clause are changed surfaces) |
| **Completion condition** | negative re-run with a firing pattern, command + mode + output + positive control published, `FTB-F-07` re-stated |

---

# P08 QUEUE

## `Q-P08-01` — delete the no-referent figure and re-notify P11 *(`XRD-011`)*

| | |
|---|---|
| **Root defect** | `XRD-011` · **local ids** `IVR-F-16`, IEV requirement **2** |
| **Owner** | **P08 — source**, branch `research/account-p08-record-to-report-2026-09-04-001` @ `00ccd66` |
| **Exact file** | `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` §1 item 1 (`:13`) |
| **Exact wrong claim** | *"at 1e-7 the answer is 3, all float artefacts on eight-figure sums"* |
| **Current evidence** | `IVR-F-16` — re-derived **in exact Decimal: 0 unbalanced at 0.005, 1e-4, 1e-7 and exact equality**, on both computed and stored balance. *"The package names its own float instrument as the cause in the same sentence and ships the number anyway"* |
| **Correct truth** | **there is no tolerance at which the count is non-zero.** The "3" has no referent |
| **Required correction** | Delete the figure; **re-run every balance measurement in exact arithmetic**; re-issue `58_` §1 item 1 |
| **MANDATORY downstream notification** | **P11 consumed this figure at three locations and built a falsification (`F-02`) and a standing method rule on it.** P08 must notify P11 explicitly — see `Q-P11-04`. **This is the reason the repair cannot be closed inside P08** |
| **PROHIBITED** | do **not** edit P11's package · do **not** re-open the count of 4 or its exculpation — **both are sound** under five predicate forms and a 1,847-row discriminating control |
| **Re-test** | every balance measurement, exact arithmetic |
| **Fresh challenge** | **`RC-05` — REQUIRED** |
| **Veto impact** | `AAS+-VETO-01` undischarged; P11's `B-29` blocked on its C-1 |
| **Completion condition** | figure deleted, balances re-run in exact arithmetic, `58_` re-issued, **P11 notified in writing**, `RC-05` complete |

## `Q-P08-02` — resolve the `HO-` namespace collision *(`XRD-006`, P08 half)*

| | |
|---|---|
| **Root defect** | `XRD-006` · **local id** `IVR-F-13`, IEV requirement **7** |
| **Owner** | **P08 — source** |
| **Exact files** | `25_P08_CORE_RECON_HANDOFF_PACK.md` (`HO-01`…`HO-06`) · `54_P08_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` (`HO-01`…`HO-14`) · `58_…BOUNDARY_HANDOFF.md` (`HO-13`, `HO-14`) |
| **Exact defect** | **`25_` and `54_` publish different sets under the same identifiers**, both live. And **P06 independently defines its own `HO-01`…`HO-06`** — so `HO-nn` does not identify a row without a producer |
| **Current evidence** | XRECON enumeration at `00ccd66` and `1b018c1`; `IVR-F-13` (*verifier's own finding, raised by no challenger*) |
| **Required correction** | Retire or re-number one family so no id is shared; **re-issue all 14 outbound rows with a version marker and a reachability qualifier**; repair the malformed row (**7 cells against an 8-cell header**, `IVR-F-11`) |
| **PROHIBITED** | do **not** renumber P06's family · do **not** edit P11's citations — that is `Q-P11-02` |
| **Re-test** | enumerate every `HO-` id and show each resolves to exactly one producer |
| **Fresh challenge** | folded into `RC-05` |
| **Completion condition** | one producer per id, 14 rows re-issued, malformed row repaired |

## `Q-P08-03` — give the FX cause-clause repair an unambiguous number *(`XRD-007`)*

| | |
|---|---|
| **Root defect** | `XRD-007` · **local ids** `IVR-INB-03`, `IVR-INB-04` |
| **Owner** | **P08 — IEV track**, branch `audit/p08-independent-verifier-2026-09-06-001` @ `bd95d1d` |
| **Exact file** | `P08_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md`:317, :339 |
| **Exact wrong claim** | *"bounded repair requirements **2 and 4**"* (:317) and *"**Bounded repair requirement 2** is therefore narrowed"* (:339) |
| **Current evidence** | terminal-report requirement **2** is *"Delete the '3 at 1e-7' from the P11 handoff…"* — which **:339 itself says *"is unaffected and stands"***. Requirement **4** is the capability denominator. **Neither carries the FX row** |
| **Correct truth** | **the FX cause-clause repair is not among the 10 numbered requirements** |
| **Required correction** | State it as its **own requirement (11)**, or re-point the cross-reference to the requirement that actually carries the FX row |
| **PROHIBITED** | **do NOT renumber the existing 10** — they are cited elsewhere · do **not** re-open the narrowing itself, which is sound |
| **Re-test / fresh challenge** | **NOT REQUIRED** — pointer-only (`RC-07`) |
| **Completion condition** | the FX cause-clause repair carries an unambiguous identifier; the existing 10 numbers unchanged |

---

# P09 QUEUE

## `Q-P09-01` — resolve `L-4`'s authority limb *(`M-1`)*

| | |
|---|---|
| **Root defect** | P09's own **`M-1`** — the named exact bounded item of `TERMINAL B` |
| **Owner** | **P09**, branch `research/account-p09-plan-to-analyze-2026-09-04-001` @ **`4778792`** (**not** HEAD `ec4d3d2`, which is bookkeeping) |
| **Exact defect** | `L-4` is **SPLIT**: assessment **CLOSED** (residue corrected 160 → 159, a dotted field path admitted as a model); **the exclusion authority is WITHDRAWN** — falsified by the package's own register, which publishes **193** and **169/52** over the reference relation |
| **Required correction** | Either **restate the P09 claims so the reference relation is not a published denominator**, or **assess the 159 as part of it**. P09's own `NEXT EXACT ACTION` |
| **PROHIBITED** | do **not** restart `L-1`…`L-8` — they are closed · do **not** touch `BD-01`, deliberately excluded as not in the authoritative L-list · do **not** widen to new roots · do **not** discharge `AAS+-VETO-04` |
| **Re-test** | the residue and the denominator, both published with their populations |
| **Fresh challenge** | folded into `RC-01` |
| **Veto impact** | `AAS+-VETO-04` cannot discharge while `M-1` is open |
| **Completion condition** | the authority limb resolved one way or the other, with the denominator declared |

## `Q-P09-02` — challenge the corrected surface *(`XRD-010` / `M-2` / `RC-01`)*

| | |
|---|---|
| **Root defect** | `XRD-010` · P09's own **`M-2`** |
| **Owner** | **P09** — **but P09 may not select the challenger** (`AASP-P11-C3-VETO-04`) |
| **Exact surface** | the **6 artefacts edited in place** at `4778792`: the `ZERO` claim struck · `CO-02b` marked superseded · the `CH-09` *deleted* disposition superseded by a tombstone · **the false *"P11 has published no branch"* withdrawn in 3 files** |
| **Exact defect** | **the corrected surface has never been challenged.** The four challenges ran **before** these edits |
| **Required correction** | Run a **bounded challenge on the corrected surface only**, by a challenger P09 did not select |
| **PROHIBITED** | do **not** re-challenge the whole package · do **not** self-satisfy the independence requirement |
| **Veto impact** | **`AAS+-VETO-04`'s condition requires exactly this** |
| **Completion condition** | `RC-01` complete, findings dispositioned, `M-2` closed |

---

# P11 QUEUE

## `Q-P11-01` — re-pin the three moved peers in the live outbound registers *(`XRD-005`)*

| | |
|---|---|
| **Root defect** | `XRD-005` · **local id** `B-37` (**HIGH, and this is its unswept remainder**) |
| **Owner** | **P11**, branch `research/account-core-reconciliation-2026-09-04-001` @ `dc4cc4a` |
| **Exact files** | `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md`:18, :28, :29 · `P11_ACCOUNTING_CONVERGENCE_QUESTION_REGISTER.md`:28, :29, :30 |
| **Exact wrong claim** | `P06 @ 249b7c2` · `P08 @ 194efcb` · `P09 @ 5441f8d` — **the CORR2 heads** |
| **Current evidence** | XRECON `XS-05`. **In the same two files the seven peers that did not move are pinned at CORR3 heads correctly.** The only three needing re-pinning are the only three not re-pinned |
| **Correct truth** | `P06 1b018c1` · `P08 00ccd66` · **`P09 4778792`** — P09's **substantive** head, not `92de8a1`, which is a prompt commit |
| **Required correction** | Re-pin all six occurrences. Then **re-scope `B-37` from a file to a claim class** and sweep **every** carrier of a peer SHA in the package |
| **Root cause to record** | **`B-37` was scoped to the file it was found in.** `P11_AUTO_RESUME_STATE.md` was corrected; the same claim class in two live outbound files was never swept. **Correct by claim class, never by the file the blocker names** |
| **PROHIBITED** | do **not** re-open the peer packages · do **not** re-derive peer facts · do **not** edit the CORR2-labelled historical artefacts, which are lineage |
| **Re-test** | enumerate every peer-SHA occurrence and show each at the resolved head |
| **Fresh challenge** | **`RC-02` — REQUIRED** |
| **Veto impact** | `AASP-P11-C3-VETO-04` — the peer snapshot is a control set |
| **Completion condition** | six occurrences re-pinned, `B-37` re-scoped, full sweep published, `RC-02` complete |

## `Q-P11-02` — producer-qualify every `HO-` citation and correct the `:148` attribution *(`XRD-006`, P11 half)*

| | |
|---|---|
| **Root defect** | `XRD-006` |
| **Owner** | **P11** |
| **Exact files** | `P11_CANDIDATE_…HANDOFF_PACK.md`:125, :129, :130, **:148**, :149 · `P11_AUTO_RESUME_STATE.md`:71 · `P11_BOSS_DECISION_MATRIX_CORR1.md`:34 |
| **Exact wrong claim** | **`:148` attributes `HO-13` to *"`P06` + `P08`"***. **P06's `HO-` family has no `HO-13`** — measured: P06 @ `1b018c1` tops out at `HO-06` |
| **Current evidence** | XRECON enumeration across P06 and P08 at their frozen SHAs |
| **Required correction** | Producer-qualify every `HO-` citation (`P08-HO-13`, never bare `HO-13`); **correct the `:148` attribution** |
| **PROHIBITED** | do **not** renumber any producer's family — that is `Q-P08-02` · do **not** re-open the `om_data_remove` finding, which is sound |
| **Re-test** | every `HO-` citation resolves to exactly one producer |
| **Fresh challenge** | folded into `RC-02` |
| **Completion condition** | all citations producer-qualified, `:148` corrected |

## `Q-P11-03` — re-state `B-38` against P09's substantive head *(`XRD-008`)*

| | |
|---|---|
| **Root defect** | `XRD-008` · **local id** `B-38` (**HIGH, open**) |
| **Owner** | **P11** |
| **Exact files** | `P11_CORR3_POPULATION_REGISTERS.md`:83 · `P11_AUTO_RESUME_STATE.md`:71 |
| **Exact wrong claim** | *"an **unexecuted** L1–L8 correction set"*, stated against P09 @ `92de8a1` |
| **Current evidence** | At P09's substantive head **`4778792`**: `L-1`…`L-8` **all closed**, `L-4` **split**, corrections applied **in place** at six artefacts |
| **Correct truth** | **the L1–L8 limb is superseded.** The **`AAS+-VETO-04 NOT DISCHARGED` limb remains true**, and the open items are now **`M-1`** and **`M-2`** |
| **Required correction** | Re-state `B-38` against `4778792`; strike the L1–L8 limb as superseded **retaining it as lineage**; keep the veto limb; **re-point the unlock condition to `M-1`/`M-2`** |
| **PROHIBITED** | **do NOT discharge `P09 AAS+-VETO-04`** — it is undischarged at P09's own head · do **not** close `B-38` · do **not** repair P09 |
| **Re-test** | re-resolve P09's head at CORR4 bootstrap before re-stating |
| **Fresh challenge** | **`RC-02`** |
| **Completion condition** | `B-38` re-stated with both limbs correctly dispositioned |

## `Q-P11-04` — withdraw the falsification built on a figure with no referent *(`XRD-011`, consumption)*

| | |
|---|---|
| **Root defect** | `XRD-011` — **and P11 does not yet know about it** |
| **Owner** | **P11**, on notification from **P08** (`Q-P08-01`) |
| **Exact files** | `P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md`:15 (**`F-02`**) · `P11_CANDIDATE_…HANDOFF_PACK.md`:124 (`CI-01`) · `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md`:106 |
| **Exact wrong claim** | `F-02` asks *"a tolerance at which the count is non-zero"*, answers **YES** on *"at 1e-7 the answer is 3"*, re-states P08's soundness claim on that basis, and derives the standing method rule *"a soundness claim without a tolerance is not a claim"* |
| **Current evidence** | `IVR-F-16` — exact Decimal gives **0 at 0.005, 1e-4, 1e-7 and exact equality**, on both computed and stored balance. **The correct answer to `F-02`'s own question is NO** |
| **Correct truth** | **the falsifier has no referent; the falsification does not stand on this instance** |
| **Required correction** | Withdraw `F-02`'s falsification and re-run it against the exact-arithmetic result; re-state `CI-01`; **re-examine the derived method rule** — it may be sound on other grounds, **but it is not supported by this instance and must not be carried as though it were** |
| **PROHIBITED** | do **not** re-derive P08's balances — that is `Q-P08-01` · do **not** silently retain the method rule · do **not** treat the rule's plausibility as evidence for it |
| **Re-test** | `F-02` re-run on exact arithmetic |
| **Fresh challenge** | **`RC-06` — REQUIRED** |
| **Completion condition** | `F-02` re-run and re-dispositioned, `CI-01` re-stated, the method rule re-grounded or withdrawn, `RC-06` complete |

---

# BOSS QUEUE

## `Q-BOSS-01` — the structural-independence ruling *(`XRD-009`)*

| | |
|---|---|
| **Root defect** | `XRD-009` — **Class F, an authority dependency, not a defect** |
| **Owner** | **Boss — sole final approver** |
| **The question** | **Does a verification performed by the same model that authored the repairs satisfy a structural-independence condition?** |
| **Why it is reserved** | **Not repairable by either party.** Both tracks disclosed it against themselves, unprompted, and both did the only thing available to them |
| **What it currently blocks** | `AASP-VETO-07` (P06) preserved partly on this ground · `AAS+-PS-VETO-01` **C-6** (P08) not discharged partly on this ground |
| **Note** | **The question is identical on both tracks and may be one decision rather than two.** This session does not assert that it is |
| **PROHIBITED** | this session **does not answer it and does not narrow it** |

---

## §6 — Adjacent Pxx: routed, not opened

**P07** is named by two open items — P11's **`B-36`** (`19_P07_CORE_RECON_HANDOFF_PACK.md`, **inside the
union, dispositioned `ADDRESSED`, never opened across three rounds**) and **`B-39`** (`HO-14` vs
`P07-F-02`/`F-03`, possibly two generations).

**No P07 artefact was opened by this session and no P07 repair is queued.** P07 is READ-ONLY under §6 of the
governing prompt, and the ownership question — whether the tax-grouping scope ruling is P07's to re-state or
P11's to consume — **is not adjudicated here.** It is routed to P11's CORR4 item 6 as already ordered, and
recorded in `03_` §5 as the one propagation edge that has never been opened.

**P01, P02, P03, P04, P05, P10** were **not opened.** No existing P06/P08/P09/P11 finding required it beyond
the peer-SHA pins already reconciled in `XRD-005`, which are P11's to correct without re-reading those
packages.
