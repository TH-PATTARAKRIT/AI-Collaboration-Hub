# 11 — ACCOUNT WAVE A — METHOD CONVERGENCE GATE REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MC-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001` · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Standard `SMEPLUS-DR-MC-001`

**Recommendation only. Boss is the sole Final Approver.**

---

## 1. What was asked, and what happened

Asked: stop searching for findings; prove the Wave A research universe is bounded, systematically
enumerated, independently repeatable, and converged. Diagnose `GB-04` to root cause. Preserve the
method as a reusable standard.

Happened: **the universe was bounded for the first time in the programme — 24 verified denominators
from a starting point of zero — the `GB-04` root cause was found and closed, and the round then
failed its own convergence test.** Two fresh independent reviewers invalidated two of this round's
three claimed closures and returned eleven new material finding classes, one of which is that **this
round's own Wave A denominator omits the sites of the programme's three most severe findings.**

## 2. The `GB-04` root cause — CLOSED

> **Enumeration was performed over an author-derived taxonomy of 155 business functions. Every
> material finding of every round inhabits a source-derived *mechanism* population, and not one of
> those populations had ever been enumerated. A taxonomy of what a system is *for* has no cell that a
> fact about how it is *built* can occupy.**

Eleven of eleven material findings fit the pattern (file `04`). The author's surface was one
author-derived list; the reviewers' surface was 750 methods, 397 fields, 153 failure paths, 132 access
rows, 93 elevation sites, 62 raw-SQL sites, 31 record rules, 11 scoping overrides, 5 configuration
keys — **nineteen populations, none enumerated.**

Independent review was the only discovery engine. Review **samples** a population; it cannot **bound**
one. Used as the primary channel it produces exactly the observed signature: every round finds real
findings, and no round can say how many remain.

`GB-04`'s exposure is now a number rather than a worry: **192 sites in three mechanism populations,
of which 9 are assessed.**

## 3. The second root cause — NEW, and no round had named it

> **There is no channel by which a found finding becomes a corrected artefact.**

- **No correction from the final round reaches any Layer 1 register it contradicts.** Every correction
  notice on the canonical registers names only the middle round.
- **Seven contradicted affirmative claims stand live, in original wording, at the gate baseline** —
  including four rows of the canonical boundary register reading *"tenant-safe: yes"* with no
  enforcement layer cited.
- **Reviewer findings are consolidated by re-narration, not by id.** Eight of nine numbered findings
  from one final reviewer appear nowhere outside that reviewer's file. **One was a tolerance-zero
  candidate and it was lost.** Two were balanced-but-wrong cases the reviewer explicitly asked to be
  registered; the register stands at 27 without them, so the true floor is **29**.
- The arithmetic consequences are already visible: the coverage register's rows and summary disagree
  by four; its own correction notice is applied nowhere, which if applied invalidates the published
  **95.5%** evidence figure carried in three gate reports; the unknown register has five orphan ids.

This cause is **cheaper to fix than the enumeration gap and blocks convergence just as hard.** Until
it is fixed, each round's findings do not reduce the next round's error, and no amount of enumeration
converges.

## 4. Convergence test result

| Test | Verdict |
|---|---|
| `MC-01` Population Boundedness | **NOT MET** — this round's own Wave A surface was under-bounded: 18 files declared, 26 correct |
| `MC-02` Systematic Enumeration | `PARTIALLY MET` — mechanical and reproducible, but two enumerations were bounded by a matching pattern, not by the source |
| `MC-03` Independent Delta | **NOT MET** — 11 new material classes |
| `MC-04` Repeatability | `PARTIALLY MET` — 17 of 17 denominators reproduced; **conclusions did not** |
| `MC-05` Negative Claim Compliance | **NOT MET** — established over 41.9% of the package, asserted over 100% |
| `MC-06` Unknown Classification | `MET` for the enumerated population; the parent count of 41 **CONTRADICTED**, true figure ≥59 |
| `MC-07` Contradiction Closure | **NOT MET as reported** — a metric widened at the gate against a register stating none of its contradictions is resolved |
| `MC-08` Tolerance-Zero Closure | **NOT MET** — six unresolved verified defects, plus a seventh that was never registered |
| `MC-09` Evidence Lineage | **NOT MET** — §3 |
| `MC-10` New-Finding Delta | **NOT MET** |

**7 not met · 2 partially met · 1 met.**

## 5. Tolerance-zero position — re-tested

All six declared boundaries remain **unresolved verified defects**; two worsened this round; one was
widened to a class-`A` verified absence; and a **seventh** was recovered from a final-round review
that had registered it as a tolerance-zero candidate and from which it then vanished.

| id | Boundary | Status |
|---|---|---|
| `T0-01` | Entry balance | UNRESOLVED |
| `T0-02` | Posting without a measurement | UNRESOLVED — worsened |
| `T0-03` | Deletion or rewrite of a posted fact | UNRESOLVED — **worsened**: `MCX-07` is a path on which the lock control does not exist at all |
| `T0-04` | Tenant isolation | UNRESOLVED — severity raised; the configuration-key class is larger than reported |
| `T0-05` | Over-reconciliation | UNRESOLVED — **widened to a verified absence**: no record rule on either reconciliation model anywhere in the tree, with full write rights for ordinary accounting roles |
| `T0-06` | Cross-company rewrite of a posted fact | UNRESOLVED |
| **`T0-07`** | Cross-company rate resolution in raw SQL, outside every record rule, with an undeclared par fallback | **UNCHARACTERISED — recovered this round from a review that raised it and a gate report that omitted it** |

## 6. Gate recommendation

> # `RECOMMEND HOLD`

**Recommendation only. Boss is the sole Final Approver.**

### Why not `CONDITIONAL PASS`

Forbidden by the standard §10 and by the standing Boss instruction: `CONDITIONAL PASS` may not be
used to bypass an unresolved tolerance-zero boundary. **Six stand unresolved and a seventh is
uncharacterised.** The conditions would *be* the tolerance-zero items. The option is unavailable by
rule, not by judgement.

### Why not `PASS`

`MC-03` and `MC-10` fail. A fresh review returned eleven new material classes and invalidated two of
this round's three closures. The standard §7 is unambiguous.

### Why not `FAIL`

No veto was issued by either reviewer, and the semantic model remains unvetoed after four adversarial
rounds. The enumeration produced this round reproduced under independent recount — 17 of 17
denominators — so the evidence base is sound even where its conclusions were wrong.

**One correction to the parent's reasoning, recorded because it matters.** `G10` justified excluding
`FAIL` on the ground that *"no veto was issued by any of the nine independent reviewers."* Absence of
a veto is not evidence of adequacy — that is precisely the inference `DR-NC-01` prohibits, made at the
gate by the programme that wrote the rule. The correct ground for excluding `FAIL` is the positive
one: the semantic model has survived four adversarial rounds **on evidence**, and every finding has
sharpened it in the direction already chosen. **The recommendation is unchanged; the reasoning is
corrected.**

### What the hold is on

Not the semantic model, and not the evidence. **The hold is on the method, and now on the package's
inability to carry its own corrections.** Three rounds declared a finding set complete and were
disproved. This round declared an enumeration bounded and was disproved — including by its own
denominator.

## 7. Blocker position

| # | Blocker | Status after this round |
|---|---|---|
| `GB-01` | Cross-company/cross-tenant measurement crossing | **UNCHANGED** — Boss decision, not research |
| `GB-02` | Cross-company rewrite of a posted fact bypassing the hard lock | **WIDENED** — `MCX-07` adds a path where the lock control is not present at all, on a more central axis (the account, not the counterparty) |
| `GB-03` | Inconsistent company scoping over one rate table | **RE-OPENED.** ≥9 rules, not four. A model-level constraint material to `FX-08` appears **nowhere** in the baseline package; `FX-08` requires targeted re-verification (`MCU-13`) |
| `GB-04` | Cross-boundary exposure not characterised | **ROOT CAUSE CLOSED · EXPOSURE NOT CLOSED** — 192 sites bounded, 9 assessed |
| `GB-05` | Affirmative safety claims unaudited | **QUANTIFIED and WORSENED** — 21 material claims, 33% cite an enforcement layer, 8 contradicted, **7 still live in original wording** |
| **`GB-06`** | **NEW — no correction-propagation channel** | Corrections do not reach the artefacts they correct; findings are lost between review and gate |
| **`GB-07`** | **NEW — the Wave A source surface is under-bounded** | 18 files declared, 26 correct; six further material populations enumerated nowhere |

## 8. What would close the method blockers — none of it is more deep research

| Blocker | Action | Cost |
|---|---|---|
| `GB-06` | Establish a correction-propagation rule: every accepted correction lands **in the register it contradicts**, by id, before the round closes. Re-run it over the standing backlog — 7 live contradicted affirmative claims, 5 orphan unknown ids, 2 unregistered balanced-but-wrong cases, 1 lost tolerance-zero candidate | Low — editorial, no new research |
| `GB-07` | Re-run the enumeration rules over the **corrected 26-file surface** and the six unenumerated populations | Low — mechanical, under a day |
| `GB-04` exposure | Traverse the 192 bounded sites | Moderate — but bounded, and now schedulable |
| `MC-05` | Run the negative-claim scan over the **64-file manifest**, not a list; triage the ~366 remaining hits | Low — mechanical |
| `MC-07` | Restate contradiction closure at its true value and stop reporting "resolved or explicitly bounded" as resolution | Low |
| `GB-01`–`GB-03` | **Boss design decisions.** Not research | — |

## 9. For Boss attention

1. **The method blockers are cheap; the design blockers are not.** `GB-04`, `GB-06` and `GB-07` are
   closable by mechanical work in days. `GB-01`, `GB-02` and `GB-03` need a decision on the SMEsPlus
   company/tenant boundary model, and no further research will produce it.
2. **One of the four blockers reported "closed with evidence" needs re-verification.** A model-level
   constraint that appears to forbid the writer half of `FX-08` exists in the source and appears in
   **none** of the 64 baseline files. This is not an accusation that `FX-08` is wrong — it is a
   statement that its closure rests on evidence that has never been tested against a constraint layer
   nobody enumerated.
3. **A tolerance-zero candidate was lost between a review and a gate report.** Recovered here as
   `T0-07`. That it could be lost at all is `GB-06`.
4. **The affirmative-claim problem is worse than reported and is a propagation problem.** Seven
   contradicted claims stand live in the canonical registers. The proposed authoring rules are
   necessary and will not correct a single one of them.
5. **This round is the strongest available evidence for its own conclusion.** It was convened to
   diagnose a method that kept declaring completeness and being disproved. It then declared two
   populations complete and was disproved, by the same control, in the same shape. The finding is not
   that this round was careless — its 24 denominators reproduced exactly under independent recount.
   The finding is that **an enumeration is only as bounded as its search pattern, and a search pattern
   is author-derived.** The correction — *declare the pattern, not only the path* — is carried into
   `ER-CORE` and is the single most transferable result of the round.
6. **The method is reusable now, and should be adopted before the next module starts.** Seven of the
   enumeration rules are domain-independent and return bounded counts on first execution. Total
   mechanical cost this round: under one hour, for 24 verified denominators, one closed root cause,
   one recovered tolerance-zero candidate, and one corrected gate finding.

## 10. Terminal state

> ## `ACCOUNT WAVE A — METHOD NOT CONVERGED / HOLD WITH EXACT ENUMERATION DEFECT`
>
> **Exact enumeration defects:**
>
> 1. **The enumerated population was author-derived** (155 business functions); every material finding
>    inhabits source-derived mechanism populations that were never enumerated. `GB-04` — root cause
>    **closed**, exposure **not** closed: 192 sites bounded, 9 assessed.
> 2. **The enumeration's boundary was set by its search pattern, not by the source.** Two populations
>    declared complete were not. `GB-07`.
> 3. **The Wave A source surface itself was under-bounded** — 18 files declared, 26 correct, omitting
>    the sites of `X-05`, `SB-05`, `FX-08` and every Wave A lock date. `GB-07`.
> 4. **Six material populations are enumerated nowhere** — raw DDL, the compute/dependency graph,
>    cascade deletes, scheduled actors, server actions, the audit-trail surface.
> 5. **There is no correction-propagation channel.** `GB-06` — new, and not previously named by any
>    round.
>
> Seven blockers: `GB-01` … `GB-07`. Four require a Boss design decision; three are closable by
> mechanical work.

**Not declared:** final approved · final freeze · Wave A closed · converged · any gate movement · any
implementation authorisation.
**Wave B has not started. No source code was modified. Nothing was merged or deployed.**
