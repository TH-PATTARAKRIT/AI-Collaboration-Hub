# 10 — ACCOUNT WAVE A — FRESH INDEPENDENT CONVERGENCE REVIEW

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room
Consolidates reviewers `MCR-A` and `MCR-B`. Full citations: `LAYER2_MC_EVIDENCE/MCE02`.

---

## 1. Constitution of the review

Two fresh reviewers, neither an author of this convergence package nor of any prior Wave A round.
Both received, per the standard: the enumeration universe, the denominator definitions, the
enumeration rules, the material-delta criteria and the evidence manifest.

Assignments were disjoint so that neither could confirm the other by repetition:

| Reviewer | Assignment |
|---|---|
| `MCR-A` | **Source layer.** Recount the denominators against primary source; test the Wave A model set for completeness; find populations enumerated nowhere; hunt new tolerance-zero mechanisms; challenge four named `MCE00` claims; audit `MCE00`'s own negative claims |
| `MCR-B` | **Governance and classification layer.** Enumerate and classify the unknowns; rebuild the balanced-but-wrong taxonomy; audit affirmative claims; test contradiction closure; test tolerance-zero closure; test the `GB-04` root-cause claim |

Both were instructed that the allowed verdicts exclude the word `PASS`, that "no evidence found" is
not "does not exist", and that every negative claim must declare its searched scope. Both complied,
and both closed with an explicit statement of what they did not search.

**Governing rule, applied without exception:**

> `Independent Review ≠ Truth.` `Verified Evidence = Truth Basis.`

**Every reviewer claim accepted below was re-verified against primary source by this session before
acceptance.** Two reviewer claims were reduced on verification and are recorded as such (§5).

## 2. Both reviewers returned `NOT CONVERGED`

Independently, on disjoint assignments, and against the round that was convened to establish
convergence.

| Reviewer | Verdict | Single most important stated reason |
|---|---|---|
| `MCR-A` | `NOT CONVERGED` | *"`MCE00`'s two claimed closures are its two unscoped negative claims, and both are false against primary source. A method that reproduces the defect it is measuring has not converged."* |
| `MCR-B` | `NOT CONVERGED` | *"The package has no channel by which a found finding becomes a corrected artefact."* |

Neither issued a veto. Both concur with `RECOMMEND HOLD`.

## 3. What the review did to this round's own work

This is the material result and it is stated first.

**Two of the round's three claimed closures were invalidated.**

| Closure claimed | Outcome | Verified basis |
|---|---|---|
| The database-wide configuration-key class is **closed at 5 members** | **INVALID** | A sixth key exists in the declared scope and is material — it is the documented bypass of the constraint aligning entry numbering with the accounting date. It is documented **three times inside this package's own parent**. The enumeration was bounded by a single-line matching pattern, not by the source |
| The rate-table scoping rules are **six, complete**; the automated feed writes a branch company, producing rows invisible to the resolver | **INVALID, and it regressed an accepted finding** | A model-level constraint **forbids branch-scoped rate rows outright**, and the scheduled feed iterates **root companies only**. The parent round's own final reviewer had already recorded the correct position. At least **three further scoping rules** exist in one file, two of them sibling methods that disagree about whether null-company rows count |
| The reconciliation models carry **no record rule anywhere in the tree** | **CONFIRMED** — independently re-searched and unchanged | The one closure that declared its full search scope |

The pattern is exact and it is the round's own indictment: **the two closures that said "complete"
without declaring a search pattern are the two that were false; the one that declared its scope in
full survived.**

**A consequence for the parent gate.** The constraint forbidding branch-scoped rate rows appears
**nowhere in the 64-file baseline package**. `FX-08` — one of the four blockers `G10` reports as
*closed with evidence*, and the basis of `GB-03` — is characterised as a writer/resolver disagreement
whose writer half that constraint appears to forbid. This session does **not** declare `FX-08`
invalid: the constraint governs one layer, and 62 raw-SQL sites bypass that layer. It is registered
as `GATING` unknown `MCU-13`: **`FX-08` requires targeted re-verification.**

## 4. New material finding classes — verified and accepted

Eleven. Each was read at primary source by this session before acceptance.

| # | Class | Substance |
|---|---|---|
| `MCX-07` | **Merge-driven cross-company rewrite of posted facts** | The account-merge path takes the **union** of every merged account's companies, writes it onto the surviving account, and retargets posted journal items to it by **raw SQL**. Lock enforcement exists only on ORM paths. Unlike the known counterparty-rewrite case there is **no bypass token — the control is simply not on this path**. Held by an ordinary accounting-manager role. A more central axis than the known case: it rewrites the **account** of a posted fact, and widens that account's company scope |
| `MCX-08` | **Silent destructive fallback** | On any constraint violation during that retarget, rows are **deleted** by raw SQL, inside a suppressed logger, with no ORM path, no log and no message. Triggerability on the journal-item table is **NOT PROVEN** — read, not executed |
| `MCX-09` | **Raw-DDL control population** | The entry-number uniqueness control is a partial unique index created in raw DDL, **scoped by journal, not by company** — and the *declared* constraint that appears to provide it has an **empty definition string**. The control is not where the package believed it was |
| `MCX-10` | **Unattended posting actor** | A scheduled job posts draft entries to the general ledger, searching **without a company filter** and swallowing failures per record. A principal that changes ledger state with no user in scope |
| `MCX-11` | **The lock-date model is outside the Wave A model set** | The company model holds all five lock dates, the five effective-lock computed fields, the fiscal-year definition and the FX-difference posting targets — 1,052 lines outside this round's own denominator |
| `MCX-12` | **Inherited-extension blind spot** | A 1,158-line extension of the journal model, carrying 13 raw-SQL and 10 elevation sites and eight multi-company aggregate reads over posted amounts, sits outside the enumerated file set |
| `MCX-13` | **The compute/dependency graph** | 161 dependency declarations, 228 computed fields, 94 stored-computed — the mechanism determining whether a posted fact can be silently re-measured outside the posting and lock path. Enumerated nowhere |
| `MCX-14` | **Cascade deletes** | 20 delete-behaviour declarations in the Wave A files, 4 of them cascading, below every application control. Enumerated nowhere |
| `RB-01` | **Finding-loss through consolidation** | Eight of a final reviewer's nine numbered findings appear nowhere outside that reviewer's file. One was a **tolerance-zero candidate**; it reached no blocker and no tolerance-zero list. Two were balanced-but-wrong cases the reviewer explicitly asked to be registered; the register stands at 27 without them |
| `RB-02` | **No correction-propagation channel** | No correction from the final round reaches any Layer 1 register it contradicts. Every correction notice on the canonical registers names only the middle round |
| `RB-06` | **A gate metric redefined at the gate** | *"Contradiction resolution 100%"* rests on widening the metric to *"resolved **or explicitly bounded**"*, against a register that states in terms that none of its contradictions is resolved and none can be |

## 5. Reviewer claims REDUCED on verification

Recorded because independent review is not truth, and the discipline must be visible in both
directions.

| Claim | Reduction |
|---|---|
| `MCR-B`: register `21` has **six** orphan unknown ids | **Five.** `GAP-H01` does appear in the register. The other five are confirmed orphans |
| `MCR-B`: *"a grep for `GAPCLOSE`, `G09`, `G10`, `AC-03`, `X-05` over files `01`–`26` returns **no true hit**"* | **Two hits exist** — both incidental token collisions (`COR-10` inside an unrelated row; `TX-05` in the unknown register), neither a propagation reference. **The finding stands; the absolute phrasing does not** — itself an instance of the unbounded-negative pattern, committed by a reviewer applying that very standard |

`MCR-A`'s claim that the silent-delete fallback is triggerable on the journal-item table specifically
was **self-reduced by the reviewer to `NOT PROVEN`** before submission, and is recorded at that
strength.

## 6. `MCE00` claims CONFIRMED under independent re-verification

`MCR-A` recounted **17 of 17** headline denominators from primary source and reproduced every one:
18 files · 16,044 lines · 397 fields · 750 methods · 153 failure paths · 132 access rows · 31 + 31
record rules · 52 menus · 126 views · 59 actions · 62 raw-SQL sites · 37 root-references · 11 scoping
overrides · 59 models · 32 constraint hooks.

Also confirmed: the reconciliation-model record-rule absence; the zero-view result for the
partial-reconciliation model; the record rule admitting null by explicit disjunct; and — in both
particulars — this round's **correction of an accepted gate finding**: the raw-SQL rate path
**includes** null-company rows and attributes them to **every** company, and its sole consumer in
this build is a product-margin report, not an accounting consolidation table.

`MCR-B` recounted the coverage register cell by cell and confirmed the arithmetic break in every
particular — rows yield 108 semantically-covered, the summary says 104; the four unreconciled scopes
are exactly those whose affirmative claims later rounds contradicted — and added a **second,
independent** non-reconciliation in the same register: its own correction notice is applied in
neither body nor summary, and if applied it invalidates the published **95.5%** evidence-coverage
figure carried in three gate reports.

Corrections to `MCE00`'s minor counts (constraint tuples 9 not 11 · addon directories 791 not 797 ·
views for the entry model 20 not 17 · elevation sites 94 not 93 · object buttons **not reproducible**
and withdrawn) are recorded in `MCE02` §1. **`MCE00` is not edited**; `MCE02` governs.

## 7. The affirmative-claim audit

`MCR-B` scanned the Layer 1 registers independently and confirmed the parent round's diagnosis —
*"the package polices negatives well and positives not at all"* — **and found it understated**:

- **21 material affirmative safety, enforcement or completeness claims; 7 cite an enforcement layer
  (33%); 8 have since been contradicted; 7 of those 8 remain live in their original wording.**

The worst are load-bearing and uncorrected at the gate baseline: four rows of the canonical boundary
register reading *"tenant-safe: yes"* with **no** enforcement layer cited, three of which the final
round contradicted; *"the hard lock never moves backward"*, contradicted; *"rates are held per company
group"*, contradicted; *"wrong company — **PREVENTED**"*, contradicted three times over; *"immutable —
defeated by: **nothing**"*, contradicted; and the terminal banner *"READY FOR BOSS FINAL RESEARCH
GATE"* on a file whose readiness claim was withdrawn.

**The proposed affirmative-claim rules are necessary but insufficient.** They govern authoring; the
defect demonstrated here is in **propagation** (`RB-02`). A rule that improves how claims are written
does not correct claims already written and still standing.

## 8. Consolidated position

| Measure | Result |
|---|---|
| Fresh reviewers | 2, disjoint assignments, neither an author |
| Reviewer verdicts | **`NOT CONVERGED`** (both) · `RECOMMEND HOLD` (both) · **vetoes: 0** |
| Denominators independently reproduced | **17 of 17** |
| New material finding **classes** | **11**, all verified at primary source |
| This round's claimed closures invalidated | **2 of 3** |
| Reviewer claims reduced on verification | **3** |
| Convergence tests met | **1 of 10** (`MC-06`, for the population enumerated) |
| Gating unknowns closed | **0**; three opened |

**The review functioned exactly as the standard intends, and returned the answer the round did not
want.** For the fourth consecutive round, every material correction came from an independent
reviewer and none from the author — including in the round convened to diagnose that very pattern.
That is not a reason to distrust this round's evidence, which reproduced under recount. It is the
strongest available evidence that the method has not converged, and it is why the recommendation in
file `11` is not a close call.
