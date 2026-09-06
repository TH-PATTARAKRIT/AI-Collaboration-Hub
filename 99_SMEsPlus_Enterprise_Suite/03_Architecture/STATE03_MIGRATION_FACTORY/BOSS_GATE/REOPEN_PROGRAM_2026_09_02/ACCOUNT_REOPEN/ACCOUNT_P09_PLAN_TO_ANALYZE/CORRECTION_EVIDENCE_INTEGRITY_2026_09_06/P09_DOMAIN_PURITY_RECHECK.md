# P09_DOMAIN_PURITY_RECHECK

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-EVIDENCE-INTEGRITY-TARGETED-CORRECTION-003` · **PHASE S** · **AI EOS = OFF**
**Layer:** 1 — clean-room.

---

> ## ⚠ CORRECTED AFTER INDEPENDENT CHALLENGE
> Statements here were **contradicted by the four AAS-03 challenges and re-verified against source by the author before adoption.** Corrections are inline; superseded wording is retained. Full list: `P09_AAS03_CORRECTION_CHALLENGE_RECORD`.

---

## 1. WHY THE PREVIOUS VERDICT WAS `NOT DECIDABLE`

The previous round declared a set of **modules** P09-owned, and one of them extended two adjacent-domain models. That looked like a purity breach, and the verdict was withheld.

**The corrected population shows the verdict was undecidable because it was measured on the wrong unit — not because purity had failed.**

---

## 2. THE RECHECK, AT FILE GRANULARITY

| Question | Answer |
|---|---|
| Does any **P09-owned file** declare or reshape an adjacent domain's model? | **No.** All 10 owning files declare P09 models only |
| Does any **P09 module** contain files attached to an adjacent-domain carrier? | **Yes — 2 files**, attaching plan semantics to a commitment carrier |
| Does any **adjacent-domain module** contain a P09-owned file? | **Yes — 1 file**, declaring a second planning family inside a financial-reporting module |
| Were any adjacent-domain internals researched this round? | **No** |
| Were the extensions themselves recorded as P09 evidence facts? | **Yes**, as the prompt requires |

### 2.1 The two boundary cases, classified

Applying `identify extension → classify exact P09 semantic effect → retain minimum interface fact → STOP → return to P09`:

| Case | Exact P09 semantic effect | Minimum interface fact retained | Path stopped |
|---|---|---|---|
| **plan semantics on a commitment carrier** — 2 files | a **prospective over-plan test** evaluated on the commitment document: committed plus not-yet-invoiced value against the intended amount | *"the over-plan condition is evaluated at commitment time, on the commitment document, by P09-authored logic"* | **YES.** The commitment document's own lifecycle, states and internals were **not** researched |
| **a P09 planning family inside a financial-reporting module** — 1 file | an **account-keyed, dimensionless intended amount**, consumed as a comparison column via a temporary table | *"a second intended-amount object exists, keyed to a specific account, with no dimension, no currency and no lifecycle"* | **YES.** The report engine was **not** researched beyond confirming the consumption point |

**Neither case required entering another domain, and neither did.**

---

## 3. THE CORRECTED VERDICT

> ### **DOMAIN PURITY: PRESERVED on the corrected population — the verdict survived independent falsification, but it survived by luck.**

**Two challengers attacked it from opposite sides and it held.** One re-derived both new rows independently and could not falsify either. The other argued the test is **near-tautological** — *"P09-owned file"* is *defined* as *"declares a P09 model"*, so the two files that would fail it are defined out of the population the test ranges over. **Both points are adopted.**

**And it was measured over a population now known to be wrong by four files.** All four declare adjacent-domain models and merely inherit the allocation mixin, so none is P09-owned and neither answer changes — **but the verdict stands on what the miss happened to contain, not on the instrument's construction, and the recheck could not have known that.**

| Check | Result |
|---|---|
| adjacent-domain internals newly researched | **0** |
| P09-owned files declaring an adjacent-domain model | **0** |
| boundary cases identified, classified and stopped | **2** |
| peer HOLDs reinterpreted | **0** |
| peer recommendations converted to facts | **0** |
| broad estate / volume / cloud sweeps | **0** |
| new roots introduced | **0** |

---

## 4. WHAT CHANGED IN THE INSTRUMENT ITSELF

The previous purity scoreboard was criticised — correctly — for counting only **author-chosen acts**: *paths I stopped*, *HOLDs I did not reinterpret*. A reader could not falsify it.

**This recheck adds two rows a reader can falsify independently**, because they are properties of the code rather than of the author's conduct:

1. **do P09-owned files declare adjacent-domain models?** — enumerable from the corrected population;
2. **does an adjacent-domain module contain a P09-owned file?** — likewise.

**Those two questions are decidable without trusting the author.** The three act-based rows remain, and remain unfalsifiable from outside; they are retained but no longer carry the verdict alone.

**`DP-R1` — a purity verdict shall rest on at least one check that is a property of the evidence rather than of the author's conduct.**

---

## 5. THE RESIDUE, STATED

Purity is **preserved on the corrected population**, and that population has **two blind spots now measured rather than assumed**: a raw-SQL class (**12 files, 3 unseen modules**) and a relational-reference class (**164 files, 51 modules**). The two commitment files sit in the second class and were found only because they happen to live inside a P09 module.

**An equivalent file inside an adjacent-domain module would be invisible to both instruments run in this programme.** No claim is made that none exists.

`UNRESOLVED — SPECIFIC EVIDENCE REQUIRED`: **two bounded passes over the already-declared root — raw-SQL and relational-reference — would close most of it, and neither was run this round.** Only the remainder needs a semantics-keyed instrument. **The residue was priced as wider work when most of it is cheap.**
