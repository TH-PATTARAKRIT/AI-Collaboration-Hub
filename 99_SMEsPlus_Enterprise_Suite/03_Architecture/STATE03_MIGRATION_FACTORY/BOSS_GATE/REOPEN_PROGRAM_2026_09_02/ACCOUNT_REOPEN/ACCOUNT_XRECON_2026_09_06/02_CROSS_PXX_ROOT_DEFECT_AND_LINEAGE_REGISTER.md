# 02_CROSS_PXX_ROOT_DEFECT_AND_LINEAGE_REGISTER

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`
**Classification** LAYER 2 — RECONCILIATION QUARANTINE

---

## 1. The deduplication rule applied

**Local published totals are NOT added.** `25 + 17 + P09 + P11` is not a cross-Pxx defect population; it is
four denominators of four different units summed by accident. Each package's totals stand **unchanged** in
`00_` §4 as audit lineage.

**One root defect with six propagated statements is ONE root defect and six manifestations.**

**Class F is not a defect.** Boss decisions, veto conditions, waivers and defer decisions are authority
dependencies and are registered in `06_`. They are **excluded from every defect count in this document.**

## 2. Root defect summary

| | Count |
|---|---|
| **Deduplicated root defects** | **11** (`XRD-001` … `XRD-011`) |
| Class A — source / domain fact | **0** |
| Class B — evidence publication | **1** |
| Class C — verifier / auditor authored | **3** |
| Class D — handoff / propagation | **4** |
| Class E — process / control validity | **3** |
| Class F — authority dependency | **0 counted as defects** (13 dependencies registered in `06_`) |
| Total manifestations traced | **43** occurrences across **24** files |
| Root defects **resolved by this session** | **0** — by mandate |

> **Class A is empty, and that is the headline.** Not one root defect in this reconciliation is a claim about
> the ERP that turned out to be false. Every one is a defect in the **record of** the research: a figure
> published in the present tense after it stopped being true, a correction applied to one carrier and not its
> siblings, a peer consumed at a superseded head, an instrument that could not fire. Both independent
> verifiers reached this independently — *"The research is sound; the bookkeeping about the research is not"*
> (P06) and *"The evidence base is sound … The reasoning over that evidence is what failed"* (P08).

## 3. Root defect register

---

### `XRD-001` — the P06 addendum's revised totals were never propagated to any other carrier

| Field | Value |
|---|---|
| **Primary class** | **C** — verifier / auditor authored |
| **Owner Pxx** | **P06 — IEV track** (`audit/p06-independent-verifier-2026-09-06-001`) |
| **Origin SHA** | `b423eff` (addendum) superseding `dac6ac3` (terminal publication) |
| **Origin artifact** | `IEV_006/P06_INDEPENDENT_VERIFICATION_ADDENDUM_E2.md` §7 |
| **Original claim** | **18** material defects · **1** verifier-authored · **15** repair requirements · **3 of 4** challengers adjudicated · Expert 2's absence *"TERMINALLY DISPOSITIONED … no finding in this package depends on it"* |
| **Correct current truth** | **25** material defects · **2** verifier-authored · **19** repair requirements · **4 of 4** challengers · **the Expert-2 disposition is FALSIFIED by its author** — Expert 2 returned 12 material defects, **7 absent from the published 18**, one of them inside the verifier's own artefact |
| **Manifestation IDs** | 8 occurrences / 4 files |
| **Manifestation files** | `P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md`:14, :24, :30 · `P06_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md`:83 · `P06_INDEPENDENT_AUTO_RESUME_STATE.md`:22 (18), :33 (15), :43 (falsified disposition) · `P06_INDEPENDENT_CHECKPOINT_REGISTER.md`:19 (`CP-IEV-07` *"THREE OF FOUR RETURNED"*) |
| **Consumer Pxx** | **The Boss.** This XRECON prompt's own §2 brief states 25 / 2 / 19 — the addendum's reading — while the package's **terminal report**, the artefact a reader treats as authoritative, publishes 18 / 15 |
| **Propagation path** | `ADDENDUM_E2` §7 → *(not propagated)* → terminal report · correction register · auto-resume · checkpoint register |
| **Severity** | **HIGH** — the package publishes a figure and its supersession in one commit, and the superseded figure sits in the artefact named "TERMINAL REPORT" |
| **Evidence** | `git diff --stat dac6ac3 b423eff` → **3 files**, the terminal report **not among them**. Line-level grep of all 9 IEV artefacts for the revised totals: **the addendum is the only carrier** |
| **Repair required** | Propagate 25 / 2 / 19 / 4-of-4 into the four carriers **by identifier**, retaining the 18/15 figures as marked-superseded lineage. Withdraw the Expert-2 disposition at `AUTO_RESUME`:43 and `CHECKPOINT`:19 and replace it with the falsification |
| **Re-test required** | **YES** — re-count the material-defect population after propagation; publish the enumeration, not the total |
| **Fresh challenge required** | **YES** — the totals are a changed surface |
| **Veto dependency** | `AASP-VETO-07` **PRESERVED** — unaffected either way; the addendum adds a third independent ground |
| **Boss decision dependency** | none |
| **Current state** | **ORIGIN CORRECTED / PROPAGATION OPEN** |
| **Exact unlock condition** | all four carriers state 25 / 2 / 19 / 4-of-4 with the superseded figures retained as lineage, re-counted and re-challenged |

---

### `XRD-002` — a validation table marked **YES** over a figure the same file supersedes nine lines later

| Field | Value |
|---|---|
| **Primary class** | **C** — verifier / auditor authored |
| **Owner Pxx** | **P06 — IEV track** |
| **Origin SHA** | `dac6ac3`, standing at `b423eff` |
| **Origin artifact** | `IEV_006/P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45 |
| **Original claim** | *"65 `P06-B-*` … max id = 65 and contiguous"* — **validation result `YES`** |
| **Correct current truth** | **67**, contiguous `P06-B-01`…`P06-B-67`. `:54` of the **same file** raises `P06-B-66` and `P06-B-67` **nine lines below** the row certifying max = 65 |
| **Manifestation IDs** | `IEV-D-20` (Expert 2) — 1 occurrence / 1 file |
| **Consumer Pxx** | none — internal to the verification package |
| **Propagation path** | none measured |
| **Severity** | **MEDIUM** as a figure · **HIGH** as a control finding — *a validation table that certifies a number its own document contradicts is not a control* |
| **Evidence** | **XRECON `XS-01`, measured independently.** Two instruments of different shape (`git grep` over the SHA; `git archive` + GNU `grep` over 87 extracted files) both return **67**, identifier sets `diff`-identical, contiguous, synthetic-injection control moved 67 → 68 |
| **Repair required** | Correct `:45` to **67** and re-state the validation result. **The addendum deliberately left it standing so the defect is legible rather than quietly repaired** — the repair must therefore retain the original row as marked-superseded |
| **Re-test required** | **YES** — re-run the contiguity validation and publish the enumeration |
| **Fresh challenge required** | NO — independently confirmed here by two instruments plus a positive control |
| **Veto / Boss dependency** | none |
| **Current state** | **NOT STARTED** |
| **Exact unlock condition** | `:45` reads 67 with the superseded row retained, and the validation is re-run |

---

### `XRD-003` — P06 source publishes four count families that stopped being true when the repair round wrote them

| Field | Value |
|---|---|
| **Primary class** | **B** — evidence publication |
| **Owner Pxx** | **P06 — source package** (`research/account-p06-bank-to-reconcile-2026-09-04-001` @ `1b018c1`) |
| **Origin SHA** | `1b018c1` |
| **Original claim → correct current truth** | blocker count **65 → 67** · open-item population **66 → 68** · vetoes *"three"* / *"four active"* **→ seven** · author errors **23 → 21** (`REV-E-22`/`-23` are repair-marker families, not author errors — 21 of 21 carry a definition line, 0 of 2 do) |
| **Manifestation IDs** | 8 occurrences / 5 files |
| **Manifestation files** | `13_`:94 (65), `13_`:95 (66) · `46_`:124 (65) · `18_`:214 (65, vetoes, author errors) · `70_`:108 (65, vetoes, author errors) · `40_`:288 (23) |
| **Consumer Pxx** | **P11** — consumed `18_P06_CORE_RECON_HANDOFF_PACK.md` and `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md` (both in `union_212.txt`, lines 83 and 90) |
| **Propagation into P11 — MEASURED** | **NOT FOUND.** P11 carried the `om_data_remove` finding from `70_` (→ `P11-B-21` `CRITICAL`, `T0-14`), **not** the blocker/veto/author-error counts. Searched P11 @ `dc4cc4a` for P06 count statements: **zero**, against a positive control confirming `P06` appears in **51** P11 files. **The wrong figures did not reach P11's substance** |
| **Severity** | **HIGH** — `46_`:124 states the governing rule *"a printed command and a printed result date differently: the command stays live and the result freezes"* **and breaks it in the same clause**. `P06-B-58`, the reliance-risk blocker, is **scaled on the author-error number** |
| **Evidence** | XRECON `XS-01` (67 confirmed, two forms + injection control) · `IEV-D-19` (68, re-run on its own printed command) · `IEV-D-21` (21 definitions present, 0 of 2) |
| **Repair required** | Correct all four families at the five files; **re-scale `P06-B-58`**; re-execute each count **at publication**, and publish the command with its output |
| **Re-test required** | **YES** — every corrected count re-executed at publication time |
| **Fresh challenge required** | **YES** |
| **Veto dependency** | `AASP-VETO-07` **PRESERVED** — two of these families are in the two P11-bound handoffs |
| **Boss decision dependency** | none directly; `P06-B-58`'s re-scaling feeds the reliance decision |
| **Current state** | **NOT STARTED** |
| **Exact unlock condition** | five files corrected, `P06-B-58` re-scaled, counts re-executed at publication with commands and outputs published, re-challenged |

---

### `XRD-004` — a published archive search whose pattern cannot fire under either grep mode

| Field | Value |
|---|---|
| **Primary class** | **E** — process / control validity |
| **Owner Pxx** | **P06 — source package** |
| **Origin SHA** | `1b018c1` |
| **Origin artifact** | `56_`:99 |
| **Original claim** | pattern `payment_return\|bounce\|dishonou?r\|post_dated\|postdated` over a declared **961-directory** archive → result *"No bank-return concept"*. **No command, no `-E`/`-F` flag and no path expression is printed with it** |
| **Correct current truth** | **The printed search is defective under both interpretations.** As BRE (`\|` = alternation): the `dishonou?r` branch matches **0 of 2** real spellings, because `?` is a literal in BRE. As ERE (`-E`, `\|` = literal pipe): the **entire pattern matches 0 of 5** — total silence. In BRE the `bounce`/`payment_return` branches still fire, **which is why the result reads as a plausible finding rather than a crash** |
| **Manifestation IDs** | `IEV-D-26`; consequence clause `FTB-F-07` |
| **Manifestation files** | `56_`:99 (the search) · `FTB-F-07` (**generalises the negative to 1,752 directories**) |
| **Consumer Pxx** | not measured as consumed by a peer; the generalisation is internal to P06 |
| **Severity** | **CRITICAL as a method finding.** This is the **first defect in this programme found in the *regex grammar* of a published search** rather than in its path set, its population or its phrasing. It is P06's own *prove-the-filter-can-fire* standard, unmet on a live negative |
| **Evidence** | Expert 2 tested the pattern against a controlled fixture holding real spellings plus a literal control, under both grep modes |
| **Repair required** | **Re-run the archive negative with a pattern proved to fire, and publish the command with its grep mode.** Then re-state or withdraw `FTB-F-07`'s 1,752-directory generalisation on the new result |
| **Re-test required** | **YES** — with a positive control inside the search population |
| **Fresh challenge required** | **YES** — the negative and its consequence clause are both changed surfaces |
| **Veto dependency** | none named |
| **Boss decision dependency** | none |
| **Current state** | **NOT STARTED** |
| **Exact unlock condition** | the negative re-run with a firing pattern, command + mode + output published, and `FTB-F-07` re-stated on the new result |

---

### `XRD-005` — P11's live outbound registers pin exactly the three peers that moved at their superseded heads

| Field | Value |
|---|---|
| **Primary class** | **D** — handoff / propagation |
| **Owner Pxx** | **P11** |
| **Origin SHA** | `dc4cc4a` |
| **Origin artifact** | `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md` and `P11_ACCOUNTING_CONVERGENCE_QUESTION_REGISTER.md` |
| **Original claim** | `CI-01`…`CI-12` and the convergence question rows attribute peer inputs to `P06 @ 249b7c2` · `P08 @ 194efcb` · `P09 @ 5441f8d` — **the CORR2 heads** |
| **Correct current truth** | CORR3 heads are `P06 1b018c1` · `P08 00ccd66` · `P09 92de8a1`. **And P09's substantive research head is `4778792`, not `92de8a1` — see `XRD-008`** |
| **Manifestation IDs** | 6 occurrences / **2 live outbound files** |
| **Manifestation files** | `…HANDOFF_PACK.md`:18 (P08), :28 (P09), :29 (P06) · `…CONVERGENCE_QUESTION_REGISTER.md`:28 (P06), :29 (P08), :30 (P09) |
| **Consumer Pxx** | **Boss** (via `ACCOUNTING_BOSS_FINAL_GATE_PACK.md`) and **PHASE B** — the candidate-input pack is P11's primary downstream product |
| **Propagation path** | `P11_CORR2_PEER_CLAIM_SNAPSHOT.md` → candidate pack + convergence register → *(not re-pinned at CORR3)* → Boss gate pack |
| **Severity** | **HIGH** |
| **Evidence** | XRECON `XS-05`. **In the same two files the seven peers that did not move are cited at CORR3 heads correctly** (`P01 b820b29` · `P03 bc767a8` · `P04 65b8841` · `P05 205e0ac` · `P10 1fea562`). **The only three that needed re-pinning are the only three not re-pinned** |
| **Root cause — and this is the transferable part** | `B-37` **exists and is registered HIGH**, and it names the defect exactly. But **`B-37` is scoped to the file it was found in** — `P11_AUTO_RESUME_STATE.md` — which **was** corrected (it now carries a `CORRECTED 2026-09-06 (B-37)` banner and CORR3's heads). **The same claim class in two other live files was never swept.** The repair was scoped by *file named in the blocker* instead of by *claim class* |
| **Repair required** | Re-pin all six occurrences to CORR3 heads — **and to P09's substantive `4778792`, not `92de8a1`**. Then **re-scope `B-37` from a file to a claim class** and sweep every carrier of a peer SHA |
| **Re-test required** | **YES** — enumerate every peer-SHA occurrence in the package and show each is at the resolved head |
| **Fresh challenge required** | **YES** |
| **Veto dependency** | `AASP-P11-C3-VETO-04` — a control set drawn by the party it controls; the peer snapshot is such a set |
| **Boss decision dependency** | none |
| **Current state** | **ORIGIN CORRECTED / PROPAGATION OPEN** — corrected in the auto-resume, open in two live outbound registers |
| **Exact unlock condition** | six occurrences re-pinned, `B-37` re-scoped to the claim class, full sweep enumerated and published, re-challenged |

---

### `XRD-006` — the `HO-` handoff namespace is collided across producers, and P11 cites it unqualified

| Field | Value |
|---|---|
| **Primary class** | **D** — handoff / propagation |
| **Owner Pxx** | **P08** (namespace origin) **+ P11** (the mis-attribution) |
| **Origin SHA** | P08 `00ccd66` · P06 `1b018c1` · P11 `dc4cc4a` |
| **Original claim** | `HO-nn` is used as a global handoff identifier |
| **Correct current truth** | **`HO-` is at least four different families.** P06 defines `HO-01`…`HO-06`. P08's `25_` defines `HO-01`…`HO-06` — **a different set under the same ids**. P08's `54_` defines `HO-01`…`HO-14`. P08's `58_` cites `HO-13`/`HO-14`. P11 additionally cites `HO-11`, `HO-21`, `HO-22` and attributes an `HO-04` to **P01** |
| **Manifestation IDs** | `IVR-F-13` (P08-internal, *verifier's own finding, raised by no challenger*) + the cross-Pxx extent, **unregistered anywhere before this session** |
| **Manifestation files** | P06 package (`HO-01`…`06`) · `25_`, `54_`, `58_` (P08) · `P11_CANDIDATE_…HANDOFF_PACK.md`:125, :129, :130, :148, :149 · `P11_AUTO_RESUME_STATE.md`:71 · `P11_BOSS_DECISION_MATRIX_CORR1.md`:34 |
| **Consumer Pxx** | **P11**, and through it the Boss gate pack and PHASE B |
| **Severity** | **HIGH** — and it has already produced a **live mis-attribution**: `P11_CANDIDATE_…HANDOFF_PACK.md`:148 attributes `HO-13` to **"`P06` + `P08`"**. **P06's `HO-` family has no `HO-13`** — measured: P06 @ `1b018c1` tops out at `HO-06`. A bare `HO-13` cannot resolve to P06 |
| **Evidence** | XRECON `XS-04` and the P06 `HO-` enumeration; `IVR-F-13` |
| **Repair required** | **P08** — retire or re-number the collided family so `25_` and `54_` do not share ids (already routed as P08 requirement 7). **P11** — producer-qualify every `HO-` citation (`P08-HO-13`, not `HO-13`) and **correct the `:148` attribution**, which cannot be P06's |
| **Re-test required** | **YES** — enumerate every `HO-` citation and show each resolves to exactly one producer |
| **Fresh challenge required** | **YES** |
| **Veto dependency** | `P06 AASP-VETO-06` *"a handoff is not delivered by being written"* — same domain |
| **Boss decision dependency** | none |
| **Current state** | **NOT STARTED** (cross-Pxx extent), **ROUTED** (P08-internal half) |
| **Exact unlock condition** | one producer per `HO-` id, every P11 citation producer-qualified, `:148` corrected, re-challenged |

---

### `XRD-007` — the P08 narrowing cross-references a repair requirement that does not hold its content

| Field | Value |
|---|---|
| **Primary class** | **C** — verifier / auditor authored |
| **Owner Pxx** | **P08 — IEV track** (`audit/p08-independent-verifier-2026-09-06-001`) |
| **Origin SHA** | `bd95d1d` (and `4643988` for the companion) |
| **Origin artifact** | `P08_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md`:317 (`IVR-INB-03`), :339 (`IVR-INB-04`) |
| **Original claim** | `IVR-INB-04`: *"**Bounded repair requirement 2 is therefore narrowed**: withdraw and replace the **cause clause only**"* — about the transaction-currency count of 4 and its *"1:1 rate fallback"* cause. `IVR-INB-03` routes to *"bounded repair requirements **2 and 4**"* |
| **Correct current truth** | **Terminal-report requirement 2 is** *"Delete the '3 at 1e-7' from the P11 handoff and re-run every balance measurement in exact arithmetic"* — and the **same addendum states that defect *"is unaffected and stands"***. **Terminal-report requirement 4 is** *"Re-derive the capability denominator from the company-account relation"* — unrelated to FX. **The FX cause-clause repair is not any of the 10 numbered requirements.** It is a real, evidenced repair with **no requirement number** |
| **Manifestation IDs** | 2 occurrences / 1 file |
| **Manifestation files** | `P08_INDEPENDENT_CORRECTION_VERIFICATION_REGISTER.md`:317, :339 |
| **Consumer Pxx** | **P08** — the owner of the repair queue, which will look up requirement 2 and find the wrong item |
| **Severity** | **MEDIUM** — the narrowing itself is sound and well-controlled (five predicate forms + a 1,847-row discriminating control). **The defect is purely in the pointer**, and its consequence is that a correct narrowing may be applied to the wrong requirement, or the FX repair may be dropped because it has no number |
| **Evidence** | requirement list read at `P08_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` §"Bounded repair requirements"; addendum text read at :339 |
| **Repair required** | Re-number: state the FX cause-clause repair as its **own requirement (11)**, or correct the cross-reference to the requirement that actually carries the FX row. **Do not renumber the existing 10** — they are cited elsewhere |
| **Re-test required** | NO — pointer-only |
| **Fresh challenge required** | NO |
| **Veto dependency** | none |
| **Boss decision dependency** | none |
| **Current state** | **NOT STARTED** |
| **Exact unlock condition** | the FX cause-clause repair carries an unambiguous requirement identifier, and the 10 existing numbers are unchanged |

---

### `XRD-008` — P11's `B-38` is stated against a P09 state that no longer holds

| Field | Value |
|---|---|
| **Primary class** | **D** — handoff / propagation |
| **Owner Pxx** | **P11** (to re-resolve) · evidence from **P09** |
| **Origin SHA** | P11 `dc4cc4a`; P09 substantive `4778792` |
| **Origin artifact** | `P11_CORR3_POPULATION_REGISTERS.md`:83 (`B-38`, **HIGH, open**) |
| **Original claim** | *"`P09` declares its own package internally contradictory at the head P11 dispositioned as `CONSUMED` … `AAS+-VETO-04` **NOT DISCHARGED**; **an unexecuted L1–L8 correction set***"* — stated against P09 @ `92de8a1` |
| **Correct current truth** | **Split.** At P09's substantive head `4778792`: the **L1–L8 correction set is EXECUTED** — `L-1`…`L-8` all closed, `L-4` honestly **split** (assessment closed, authority **withdrawn**), corrections applied **in place** at six prior artefacts. **That limb of `B-38` is superseded.** The **`AAS+-VETO-04 NOT DISCHARGED` limb remains true** at P09's own head, and two named items are open: **`M-1`** (`L-4`'s authority) and **`M-2`** (the corrected surface has not been challenged) |
| **Manifestation IDs** | 1 occurrence / 1 file, plus the dependency row at `P11_AUTO_RESUME_STATE.md`:71 (*"`B-38` … blocked on **P09**"*) |
| **Consumer Pxx** | Boss gate pack — `B-38` is one of P11's 35 open blockers |
| **Severity** | **MEDIUM** — the blocker does not vanish; **it changes shape**, and its unlock condition changes with it |
| **Evidence** | P09 `P09_AUTO_RESUME_STATE.md` @ `4778792`: `L-1`…`L-8` dispositions, `M-1`/`M-2`, `AAS+-VETO-04 NOT DISCHARGED`. P11's own CORR4 item 6 already orders the P09 artefact opened — **but at the SHA basis `92de8a1`, not `4778792`** |
| **Repair required** | Re-state `B-38` against `4778792`: strike the *"unexecuted L1–L8"* limb as superseded (retaining it as lineage), keep the veto limb, and **re-point the unlock condition to `M-1` and `M-2`** |
| **Re-test required** | **YES** — re-resolve P09's head at CORR4 bootstrap before re-stating |
| **Fresh challenge required** | **YES** |
| **Veto dependency** | `P09 AAS+-VETO-04` **undischarged at P09's own head** — P11 correctly records this and must not discharge it |
| **Boss decision dependency** | none |
| **Current state** | **NOT STARTED** |
| **Exact unlock condition** | `B-38` re-stated against `4778792` with both limbs correctly dispositioned and the unlock condition pointed at `M-1`/`M-2` |

---

### `XRD-009` — structural independence is unestablished on **both** verification tracks

| Field | Value |
|---|---|
| **Primary class** | **E** — process / control validity |
| **Owner Pxx** | **Boss** (adjudication) · **P06 IEV** and **P08 IEV** (disclosure already made) |
| **Origin SHA** | P06 `dac6ac3`/`b423eff` · P08 `3ea9195` |
| **Origin artifact** | `P06_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` §"`AASP-VETO-07`" ground 1 · `P08_INDEPENDENT_VERIFICATION_TERMINAL_REPORT.md` `IVR-IND-01` |
| **Original claim** | each track was commissioned as an **independent external** verification |
| **Correct current truth** | **P06:** the prompt's own precondition — *"THIS PROMPT MUST NOT BE EXECUTED BY THE SAME P06 CORRECTION ACTOR"* — **was not met. It was.** The executing context authored the `REV-E-23` repairs, and **one of the 25 defects is its own** (`41_`:6, `IEV-I-03`), **and a second** (`IEV-D-20`, `XRD-002`). **P08:** *"procedural independence was met; **structural independence was not.** The verifying agent is the same model that authored the repairs"* |
| **Manifestation IDs** | 2 — one per track |
| **Consumer Pxx** | every consumer of either verification result |
| **Severity** | **HIGH — and it is the reason neither veto can be discharged by its own track.** P06 §9 reserves the discharge recommendation to *"an independent verifier that completes this prompt"*, which that verifier states it is not. P08's `AAS+-PS-VETO-01` **C-6 is not discharged**, on this ground and on `IVR-F-02` |
| **Evidence** | both terminal reports, first-person, unprompted |
| **Repair required** | **NONE BY EITHER TRACK — this is not repairable by the parties to it.** Both tracks did the one thing available to them: **disclosed it in their own terminal report** |
| **Re-test required** | **YES**, if the Boss rules that a differently-instanced verifier satisfies the condition |
| **Fresh challenge required** | **YES** — by a party neither track selected |
| **Veto dependency** | `AASP-VETO-07` (P06) **PRESERVED on this ground** · `AAS+-PS-VETO-01` C-6 (P08) **not discharged on this ground** |
| **Boss decision dependency** | **YES — RESERVED TO BOSS.** *Whether a verification performed by the same model that authored the repairs satisfies a structural-independence condition.* **This session does not answer it and does not narrow it** |
| **Current state** | **TECHNICAL EVIDENCE COMPLETE / AUTHORITY OPEN** |
| **Exact unlock condition** | a Boss ruling on the independence condition; **or** a verification by a party neither track selected |

---

### `XRD-010` — three corrected surfaces stand unchallenged

| Field | Value |
|---|---|
| **Primary class** | **E** — process / control validity |
| **Owner Pxx** | **P06**, **P09**, **P11** — one instance each |
| **Origin SHA** | P06 `1b018c1` · P09 `4778792` · P11 `dc4cc4a` |
| **Original claim** | each round published a corrected package |
| **Correct current truth** | **A corrected surface changed after challenge is not validated by the challenge that preceded it.** **P09** names this against itself as **`M-2`**: *"run a bounded challenge on the corrected surface, which has not been challenged"* — six artefacts were edited in place at `4778792` **after** the four challenges ran. **P11** names it as CORR4 item 7: *"A corrected package that has not been re-attacked is not a reviewed package."* **P06's** source package will be in the same state the moment `XRD-003`/`XRD-004` are repaired |
| **Manifestation IDs** | 3 |
| **Consumer Pxx** | Boss — all three terminal states rest on surfaces in this condition |
| **Severity** | **HIGH** |
| **Evidence** | P09 `AUTO_RESUME_STATE` (`M-2`, `AAS+-VETO-04` condition) · P11 `AUTO_RESUME_STATE` §4 item 7 · P06 by construction after repair |
| **Repair required** | **Not a repair — a required control.** Each owner must run a **bounded challenge on the corrected surface only**, by a challenger the owner did not select |
| **Re-test required** | inherent |
| **Fresh challenge required** | **YES — this defect *is* the requirement** |
| **Veto dependency** | **`P09 AAS+-VETO-04` cannot discharge until `M-2` completes** · `AASP-P11-C3-VETO-04` forbids a control set drawn by the controlled party — **so none of these three may select its own challenger** |
| **Boss decision dependency** | none, beyond `XRD-009` |
| **Current state** | **PROPAGATED / RE-TEST OPEN** (P09) · **NOT STARTED** (P06, P11) |
| **Exact unlock condition** | a bounded challenge on each corrected surface, run by a challenger the owner did not select |

---

### `XRD-011` — P11 built a falsification and a method rule on a figure with no referent

| Field | Value |
|---|---|
| **Primary class** | **D** — handoff / propagation |
| **Owner Pxx** | **P08** (origin, already routed as requirement 2) · **P11** (consumption, unregistered) |
| **Origin SHA** | P08 `00ccd66` → P11 `dc4cc4a` |
| **Origin artifact** | `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md` §1 item 1 |
| **Original claim** | *"0 unbalanced posted entries in the reporting currency across 169,143 **at a tolerance of 0.005 or wider; at 1e-7 the answer is 3, all float artefacts on eight-figure sums**"* |
| **Correct current truth** | **`IVR-F-16` — the "3" has no referent.** Re-derived by the P08 verifier **in exact Decimal: 0 unbalanced at 0.005, 1e-4, 1e-7 and exact equality**, on **both** computed and stored balance. *"The package names its own float instrument as the cause in the same sentence and ships the number anyway"* |
| **Manifestation IDs** | 3 occurrences / 3 files **in P11** |
| **Manifestation files** | `P11_CANDIDATE_ACCOUNTING_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md`:124 — restates `CI-01` as *"at 1e-7 the count is 3"*, **live outbound** · `P11_CORR3_INTAKE_CASE_DISPOSITIONS.md`:106 — quotes it as the received position · **`P11_CORR3_RECONVERGENCE_AND_FALSIFICATION.md`:15 (`F-02`)** |
| **Consumer Pxx** | **Boss** and **PHASE B**, via the candidate-input pack |
| **Severity** | **CRITICAL as a propagation finding.** `F-02` asks *"a tolerance at which the count is non-zero"* and answers **YES** on this figure; it then re-states P08's soundness claim on that basis and **derives a standing method rule** — *"A soundness claim without a tolerance is not a claim"*. **Under `IVR-F-16` the correct answer to `F-02`'s own question is NO.** P11's falsification is itself falsified, and a method rule now in circulation rests on it |
| **Evidence** | XRECON `XS-06` — three P11 occurrences located with a positive control (`169,143`, 4 occurrences, confirming the region is reachable); `IVR-F-16` re-derivation in exact Decimal |
| **Repair required** | **P08** — delete the *"3 at 1e-7"* from `58_` and re-run every balance measurement in exact arithmetic (**already requirement 2**). **P11** — withdraw `F-02`'s falsification, re-state `CI-01`, and **re-examine the method rule**: the rule may still be sound on other grounds, but **it is not supported by this instance** and must not be carried as though it were |
| **Re-test required** | **YES** — P11 must re-run `F-02` against the exact-arithmetic result |
| **Fresh challenge required** | **YES** |
| **Veto dependency** | `P08 AAS+-VETO-01` **undischarged** — P11's `B-29` is already blocked on its C-1 |
| **Boss decision dependency** | none |
| **Current state** | **NOT STARTED** — **and unregistered by P11**, which does not yet know the figure it falsified on has no referent |
| **Exact unlock condition** | the figure deleted at P08 source, `F-02` re-run on exact arithmetic, `CI-01` re-stated, and the method rule either re-grounded or withdrawn |

---

## 4. What was tested and found NOT to be a defect

Recorded so a successor does not re-open them, and so this register is not read as an unbounded list.

| Tested | Result |
|---|---|
| **P06's wrong counts propagated into P11** | **NOT FOUND — measured.** P11 consumed `18_` and `70_` but carried the `om_data_remove` finding, not the counts. Positive control: `P06` appears in 51 P11 files |
| **P08's "14 outbound rows" vs `58_`'s 13** | **NOT A DEFECT.** The 14 is `HO-01`…`HO-14` in `54_`; `58_` carries 13 boundary rows. `XS-04` |
| **P08's 19 and P11's 19 Boss decisions are the same population** | **FALSE — they are distinct.** `P08-BD-01…19` vs `D-1…D-18` + `D-3b`. Enumerated separately |
| **P11's decision total of 19 is wrong (23 distinct `D-` ids observed)** | **P11's 19 is CORRECT.** The 23 is an artefact of two padding conventions plus two foreign families. `XS-02` |
| **P09's HEAD `ec4d3d2` changed substantive state** | **NO — verified, not accepted on assertion.** 11 content lines, all bookkeeping |
| **Either verifier mutated its source package** | **NO** on both tracks — stated by each and consistent with branch topology |
