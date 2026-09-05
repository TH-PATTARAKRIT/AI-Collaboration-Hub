# P10 — RESEARCH ERROR AND REVISION LOG

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1

Silent overwrite of contradicted or corrected findings is prohibited. Every correction below records what was originally written, why it was wrong, who found it, and what it was replaced with.

---

## `P10-R-01` — The mechanism population was declared as a total when it was a floor

| | |
|---|---|
| **Originally written** | "Deterministic enumeration found **five** independent implementations." |
| **Why wrong** | The declared pattern was identifier-anchored on five expressions the author chose. It could not see any mechanism named differently, and it could not see any mechanism that materialises entries by copying an existing one. |
| **Found by** | Independent challenge #4, which ran a different pattern, returned seven, and then demonstrated that its own pattern had missed an eighth. |
| **Replaced with** | "At least eight; no exact total is supportable." Class `D`, `NC-01`. |
| **Defect class** | The project's `PATTERN` clause. An enumeration is bounded by its matching expression, not by its path set — and the pattern was chosen by the author of the claim it bounded. |
| **Recurrence** | Fifth consecutive round in which this exact defect has appeared, and the fifth in which independent review caught it and the author did not. |

## `P10-R-02` — The deferral catch-up claim was stated for the mechanism when it holds only for one path

| | |
|---|---|
| **Originally written** | "No catch-up mechanism exists on the deferral mechanism." |
| **Why wrong** | The claim was formed on the validation path and generalised to the mechanism. The grouped path recomputes cumulatively from an unbounded earliest date, which is a structural catch-up. |
| **Found by** | Independent challenge #4, contradicting independent challenge #3, which had certified the broad claim as class `A`. |
| **Replaced with** | Path-scoped statement; `P10-F-08` re-scoped; `P10-C-01` resolved on evidence. |
| **Consequence** | The reading inverts: the product **default** path is the fragile one. |
| **Note** | Two independent reviewers reached opposite conclusions and **both were partly right**. Reviewer count did not decide it; the cited line did. |

## `P10-R-03` — The asset catch-up device was mis-identified

| | |
|---|---|
| **Originally written** | In the author's challenge brief and first comparison table: catch-up occurs "via board recompute". |
| **Why wrong** | The board recompute is purely prospective. The catch-up is a separate stub entry cut at the modification date. |
| **Found by** | Independent challenge #3, which flagged it as an error **in the brief the author wrote**. |
| **Replaced with** | `E-P10-048`; `08` axis 11; `05` §4.3a. |

## `P10-R-04` — A path in the author's own reviewer brief did not exist

| | |
|---|---|
| **Originally written** | The brief for challenge #3 named a company-model file that does not exist in the reference root. |
| **Found by** | Independent challenge #3, which reported it as a finding because the brief instructed it to. |
| **Replaced with** | The correct location, recorded in `E-P10-060`. |
| **Note** | This is the second consecutive round in which the author's reviewer brief contained a wrong path that only a reviewer noticed. The instruction "if any path in this brief is wrong, report it as a finding" is doing real work and must remain in every brief. |

## `P10-R-05` — The author's framing of the design question presumed the answer it was testing

| | |
|---|---|
| **Originally written** | The session was framed around verifying that depreciation and deferral are *different*, in honour of the Boss's warning. |
| **Why incomplete** | The Boss's warning forbids assuming sameness. It does not license assuming difference. The reference product's asset object is named for **both** domains and still carries deferred-revenue commentary — evidence the two were one engine here. |
| **Found by** | Independent challenge #4. |
| **Replaced with** | `08` §1, which records both refutations; `05` §5a. |

## `P10-R-06` — The "one economic fact, two paths" finding was understated

| | |
|---|---|
| **Originally written** | Two paths produce different journal shapes for one fact (`P10-F-06`). |
| **What was missed** | Inside the grouped path, the direction is passed as a boolean where a direction name is expected, so the comparison can never succeed and the revenue allocation rule is applied on both reports. The **display** and the **generation** of one screen therefore use different rules. |
| **Found by** | Independent challenge #2; **re-verified line-by-line by the author** before admission. |
| **Replaced with** | `P10-F-21`, `E-P10-050`, `P10-C-08`. |
| **Note** | The author's brief directed the reviewer at the exact line containing this defect, for a different reason, and the author had read that line twice without seeing it. |

## `P10-R-07` — Two negative claims were downgraded before publication

| | |
|---|---|
| `NC-02` | "Deferral entries cannot carry a foreign currency" was drafted as a flat negative. The generated lines do acquire a currency field from the ledger's own defaults; what is dropped is the *dimension*, not the field. Narrowed, and the narrow form is class `A`. |
| `NC-22` | "The deferral mechanism has no schedule object" was drafted as class `A`. Supporting it requires a model-declaration scan across every module of the reference root, which was not performed. Downgraded to class `B`. **This is the negative most likely to be quoted downstream.** |
| **Found by** | Independent challenge #4's negative-claim audit. |

---

## Correction Arithmetic

| | Count |
|---|-------|
| Material corrections to the primary author's work | 7 |
| Of which found by the author's own review | **0** |
| Of which found by independent challenge | **7** |
| Errors found *in the author's reviewer briefs*, by the reviewers | 4 |
| Contradictions between two independent reviewers | 1, resolved on the cited line |
| Findings originating with reviewers and re-verified by the author before use | 14 |
| Reviewer findings admitted without author re-verification, and marked as such | 9 |

**The author corrected none of its own material errors.** This is stated plainly because the programme's own standing lesson is that self-review does not replace independent review, and this round is another instance rather than an exception. The practical consequence for the gate is recorded in `20_P10_FINAL_GATE_REPORT.md` `EC-07`: one independent pass has completed, not two, and the pass that completed produced seven material corrections — which is not the profile of a converged round.


---

## `P10-R-08` — The package declared a single evidence layer without searching for the others

| | |
|---|---|
| **Originally written** | "This session had source evidence only — no database, runtime or UI access", in the PMO record, the gate report and the handoff pack. The gate report used it to explain why Stage E cross-layer correlation "could not be performed at all". |
| **Why wrong** | Four deployed database archives were sitting on the execution host, three of them readable with tooling already installed. The author never looked. The claim was a **negative about the author's own evidence base, asserted without the search that would support it** — the exact defect class the project's negative-claim standard exists to prevent, committed in the document that assesses compliance with that standard. |
| **Found by** | Not by the author's review, and not by any of the four challenges — none of which was scoped to the evidence base itself. It was found while writing the session memory, on reading a **peer session's** recorded lesson that database dumps exist on this host and are readable primary evidence. |
| **Replaced with** | `22_P10_DEPLOYED_EVIDENCE_CORRELATION.md`, a shipped extraction script, raw output, eight new evidence items, one new finding (`P10-F-37`), and corrections to `EC-01`, `EC-04` and `EC-08`. |
| **What it changed** | Materially. The estate is on **two different product lines with different sets of time-based mechanisms**; one deployed database has **no deferral structure at all**; all 44 companies use the **weakest** of the two generation paths; **zero** deferral entries have ever been generated; and the chart of accounts is structurally shareable but currently almost unshared. None of that was knowable from source. |
| **Standing lesson reinforced** | Test the evidence base before declaring it. "No access" is a negative claim and needs a search like any other. A peer session had already learned this and written it down — **the lesson was available and unread until after the package was pushed.** |

### Correction arithmetic, updated

| | Count |
|---|-------|
| Material corrections to the primary author's work | **8** |
| Of which found by the author's own review | **0** |
| Of which found by independent challenge | 7 |
| Of which found by reading a peer session's recorded lesson | 1 |

---

# CONTINUATION ROUND — `SMEPLUS-26-09-04-ACC-P10-TBR-CROSS-PROCESS-RECON-001`

## `P10-R-09` — The process taxonomy was mis-assigned

| | |
|---|---|
| **Originally written** | `10_P10_CROSS_PROCESS_OWNERSHIP.md` names **`P04` as "A2R (the ledger)"** and routes the ledger, period close, lock dates, the fiscal calendar and FX policy to it. |
| **Why wrong** | `P04` is **Acquire-to-Retire** — the fixed-asset lifecycle, which runs a competing recognition engine. The ledger is **`P08` Record-to-Report**. The analytic dimension is **`P09` Plan-to-Analyze**. Neither `P08` nor `P09` was addressed at all, and every ledger obligation was addressed to the wrong process. |
| **How the error was possible** | The parent package inferred the taxonomy from execution-folder names rather than from a written source. `P11-F-04` establishes that **the `P01`–`P11` process taxonomy does not exist in the canonical repository** — so there was no denominator to check against, and the inference silently substituted for one. This is the programme's standing population defect in a new place: not an enumeration of code, but an enumeration of *processes*. |
| **Found by** | This continuation, on enumerating the published peer branch set. **Not** by the parent round's four challenges — none was scoped at the process taxonomy. |
| **Replaced with** | `23_P10_PEER_INTAKE_REGISTER.md` §0 and the restated dependency register in `37`. Peers who ingested the parent's cross-process document are notified as `OUT-06`. |

## `P10-R-10` — `P10-F-05` was under-classified

| | |
|---|---|
| **Originally written** | The silent re-dating of a locked-period recognition entry was carried as `VERIFIED FACT` from source, with its consequence as `INFERENCE`, and the gate report used the absence of an executed reproduction to hold `EC-04` open. |
| **What was missed** | The product ships an **executed test that asserts the behaviour**: a charge scheduled for the last day of 2020 posts as the last day of July 2021 under a mid-2021 fiscal-year lock. The parent round read the posting layer and the deferral tests but never looked for a positive control in a *sibling mechanism's* test suite. |
| **Found by** | Peer process `P04`, which cited it; re-read line by line by P10 before adoption. |
| **Replaced with** | `P10-F-39`. The finding is now `VERIFIED FACT with an executed positive control`, and its status changes from "defect" to **"specified behaviour"** — which is worse, not better, and changes what a remedy must be. |
| **Standing lesson reinforced** | An evidence claim needs a **positive control** — a case where the mechanism demonstrably fires. The parent round asserted the mechanism from reading it, not from watching it fire. The control existed in the repository the whole time. |

## `P10-R-11` — The parent scope matrix recorded no expiry triggers

| | |
|---|---|
| **Originally written** | `10b_P10_SCOPE_OWNERSHIP_MATRIX.md` presents thirteen scope determinations as standing facts. |
| **Why wrong** | Three of them are taken against behaviour the programme is **obliged to change**. Under `SCP-09` such a determination is time-indexed and must record its expiry trigger, or it will be read later as a permanent fact after it has ceased to be true. |
| **Found by** | Adopted from `P11`/`P04`; applied by P10 to its own matrix. |
| **Replaced with** | `33_P10_SCOPE_REVALIDATION_CORR1.md` §2, which carries expiry triggers on the recognition event schema, the tenant allocation standard, and recognition attribution. |

## Correction arithmetic — cumulative

| | Count |
|---|-------|
| Material corrections to the primary author's work | **11** |
| Found by the author's own review | **0** |
| Found by independent challenge | 7 |
| Found by reading a peer session's recorded lesson | 1 |
| Found by reconciling against a published peer package | **3** (`R-09`, `R-10`, `R-11`) |

Eleven corrections, none self-caught. The three added this round came from a source the parent round did not have: **peers who had written the evidence P10 was reasoning about.** That is a distinct control from adversarial challenge, and it caught a class — a wrong process taxonomy, a missing positive control, a missing expiry trigger — that four adversarial challenges did not.
