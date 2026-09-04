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
