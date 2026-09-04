# 00 — ACCOUNT WAVE A · AAS+ REDESIGN SCOPE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-AASR-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` (**IN PROGRESS — NOT TERMINATED**)
Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Depth `L99999.99999` · Model `Claude Opus 5 (Extra)`

---

## STATUS BANNER — GOVERNS EVERY FILE IN THIS PACKAGE

> # `PROVISIONAL / NON-AUTHORITATIVE / EVIDENCE-CONSUMER MODE`
>
> This package is a **parallel synthesis** produced while the parent Very Deep / Method Convergence
> execution is **still running**. It consumes parent evidence. It does not produce, replace, extend,
> or adjudicate parent evidence.
>
> **AAS+ OUTPUT IS NOT CANONICAL.**
>
> Explicitly NOT declared by this package:
> `Architecture frozen` · `Semantic model final` · `Deep Research Standard final or effective` ·
> `Findings complete` · `Parent package superseded` · `Implementation recommended` ·
> `Wave A closed` · `Wave B started` · `Gate movement` · `Boss approval`
>
> Boss is the sole Final Approver. **No Evidence = No Progress. Never Skip Gate.**

---

## 1. Why this session is in containment

The session was convened under `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-AASR-001` to perform the AAS+
post-Very-Deep redesign. Its §2 precondition requires the parent round to have reported
`METHOD CONVERGED / READY FOR AAS+ REDESIGN`, or an evidence-backed state explicitly sufficient for
bounded redesign.

**The precondition is not met, on three independent grounds established by inspection before any
design work began.**

| # | Ground | Evidence | Class |
|---|---|---|---|
| `PC-01` | The parent's own terminal self-report is **`METHOD NOT CONVERGED`**. `MC-01`…`MC-10`: **8 not met · 2 partially met · 0 met**. Fixed point **not reached** — six of seven criteria fail on both consecutive passes | `MCC_I`, `MCC_H`, `MCC` master §2 | `VERIFIED FACT` |
| `PC-02` | **Ten tolerance-zero boundaries stand. Zero are resolved.** Three (`T0-08` entry identity, `T0-09` declared-but-non-executing control, `T0-10` cross-company lock exception) were opened *by the parent's own final passes* | `MCC` master §5 | `VERIFIED FACT` |
| `PC-03` | The parent evidence package is **materially incomplete and not in version control** — see §2 | this session, direct inspection | `VERIFIED FACT` |

The Boss containment directive received mid-session independently confirms `PC-03`'s cause: the
parent execution is **in progress**. This session therefore does not issue a `REDESIGN HOLD` gate
recommendation — a gate recommendation against an unfinished parent would itself be a false
completeness claim. It issues a **provisional parallel synthesis** instead.

---

## 2. `AASR-F-01` — the parent evidence package is unpushed and internally incomplete

`VERIFIED FACT` · established by direct inspection of the parent working tree, 2026-09-04.

| Observation | Detail |
|---|---|
| Parent working tree | `ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION` |
| Git status of the entire `METHOD_CONVERGENCE_CLOSURE/` directory | **`??` — untracked.** Not committed, not pushed |
| Remote branches carrying Wave A | `research/account-wave-a-{core,corr1,gapclose,mc}-2026-09-04-001` — **no `mcc` branch exists on the remote** |
| Parent HEAD | `33cdc6fa009c4eafcca543c253ccad19e97fd0dc` — this is the **MC** round's commit, not the MCC round's |
| `MCC_J_FRESH_EXPERT_AND_AUDIT_CHALLENGE.md` | **Does not exist**, though cited as governing by `MCC` master §7 |
| MCC gate report | **Does not exist** |
| MCC evidence manifest SHA-256 | **Does not exist** |
| Files present | `MASTER`, `MCC_A`–`MCC_I`, `MCC_K`, `LAYER2_MCC_EVIDENCE/` — **A through K, less J** |

**Consequence for this package.** Every parent citation made here is a citation to an **uncommitted
working-tree file that may still change**. This is the single largest invalidation exposure carried
by this synthesis, and it is registered as dependency `DEP-00` governing all others.

**Containment action taken.** The parent package was copied unmodified into this session's branch at
its original repository path, per the established parallel-copy pattern. The parent branch was not
checked out for writing and will not be pushed to. This preserves the evidence this synthesis
consumed **as it stood at consumption time**, so that delta revalidation has a fixed baseline to diff
against. It is a preservation act, not an adoption act: **the copy is not authoritative and does not
supersede whatever the parent finally publishes.**

---

## 3. What this session may and may not do

Per the Boss containment directive, in full.

| May | May not |
|---|---|
| Organise verified findings | Freeze any architecture |
| Identify candidate semantic patterns | Declare any semantic model final |
| Prepare alternative clean-room designs | Declare any Deep Research Standard final |
| Identify design questions | Treat current findings as complete |
| Map current evidence into candidate architecture | Supersede the parent research package |
| Identify what future parent findings could invalidate each design | Recommend implementation |
| Maintain a dependency register against the running parent session | Close Accounting Wave A · start Wave B |

## 4. Mandatory classification of every design conclusion

No design statement in this package appears without exactly one of these five labels.

| Label | Meaning | Bar |
|---|---|---|
| `STABLE-CANDIDATE` | Multi-round evidence, survived at least one independent contradiction pass, and **no open gating unknown or tolerance-zero boundary bears on it** | **UNUSED IN THIS PACKAGE — see below** |
| `PROVISIONAL` | Evidence-backed and coherent, but single-round, or not yet adversarially tested | default |
| `EVIDENCE-DEPENDENT` | The design cannot be settled until a **named** parent finding lands | must name the finding |
| `INVALIDATED` | A later parent finding has already contradicted it; retained for lineage, never deleted | must cite the contradicting evidence |
| `UNKNOWN` | The business or accounting question itself is unresolved; not a research gap but a decision gap | must name the decider |

> ### `STABLE-CANDIDATE` is **not used** in this package. `AASR-C-01`.
>
> The label was applied to 20 designs in the first draft. **Two independent reviewers, working
> disjoint assignments, each independently found that it did not mean what this section defines**
> (`RA-02`, `RB-27`) — at least nine designs carried it while their own register cell named an open
> gating unknown, and the bar could not have been tested at all because **six of the ten recorded
> tolerance-zero boundaries (`T0-01`…`T0-06`) were never enumerated anywhere in the package**
> (`RB-29`).
>
> **The bar is correct; its application was not.** With the parent non-converged, **12 tolerance-zero
> boundaries known and zero resolved**, and `GB-01`…`GB-08` open, no Wave A design can currently meet
> it. Every design has therefore been demoted to `PROVISIONAL` or `EVIDENCE-DEPENDENT`.
>
> The label is retained in this table because the containment directive defines it, and because a
> future round working from a converged parent baseline will need it. **It is not available to this
> package.**

## 5. Evidence classes carried from the parent method

Every design statement points to one. These are the parent programme's classes and are not redefined
here.

`VERIFIED FACT` · `VERIFIED BUSINESS SEMANTIC` · `CONTROL REQUIREMENT` · `INFERENCE` ·
`DESIGN CHOICE` · `UNKNOWN / OPEN DECISION`

Negative claims additionally carry the programme's class letter — `A` verified absence within a
stated scope · `B` not found in searched scope · `C` not yet searched · `D` unknown · `E` contradicted —
and **no `B`/`C`/`D` is restated as `A` anywhere in this package.**

## 6. Package contents

| # | File | Purpose |
|---|---|---|
| 00 | this file | scope, containment, classification rules |
| 01 | `AAS_PLUS_PARENT_EVIDENCE_DEPENDENCY_REGISTER` | **the controlling register** — every design against its parent dependency and invalidation trigger. §5 records the register closure forced by `AASR-VETO-01` |
| 01A | `DEP00_PARENT_BASELINE_HASHES` | consumption-time SHA-256 snapshot of the parent package |
| 02 | `VERIFIED_SEMANTIC_BASELINE` | what is currently held true, by evidence class |
| 03 | `ACCOUNTING_EVENT_MODEL` | candidate |
| 04 | `FINANCIAL_FACT_MODEL` | candidate |
| 05 | `COA_REDESIGN` | candidate |
| 06 | `JOURNAL_REDESIGN` | candidate |
| 07 | `JOURNAL_ENTRY_ITEM_REDESIGN` | candidate |
| 08 | `RECONCILIATION_REDESIGN` | candidate |
| 09 | `DATE_PERIOD_REDESIGN` | candidate |
| 10 | `FX_REDESIGN` | candidate |
| 11 | `LOCK_CLOSE_REOPEN_REDESIGN` | candidate |
| 12 | `SAAS_BOUNDARY_REDESIGN` | candidate |
| 13 | `EVENT_TO_FINANCIAL_FACT_MAP` | the chain, per link |
| 14 | `BALANCED_BUT_WRONG_DESIGN_PROOF` | design tested against the **19-class** taxonomy, plus `T-20`, the class the taxonomy has no cell for |
| 15 | `UNKNOWN_DESIGN_IMPACT_REGISTER` | which unknowns block which component |
| 16 | `ALTERNATIVE_DESIGN_DECISION_REGISTER` | ≥2 alternatives per high-impact area |
| 17 | `AAS_PLUS_EXPERT_REVIEW_REGISTER` | ten perspectives, disagreement preserved |
| 18A | `NEGATIVE_CLAIM_COMPLIANCE_SCAN` | self-scan, `NCS-*` and `EFC-*`, plus the boundary re-derivation |
| 18 | `INDEPENDENT_DESIGN_VETO_REPORT` | two fresh reviewers, disjoint assignments, neither authored — **68 findings, 46 `MATERIAL`, one veto** |
| 19 | `AAS_PLUS_PROVISIONAL_SYNTHESIS_REPORT` | terminal state of this session |

**Citation convention.** A bare `NN §M` refers to a file **in this package**. A parent-package file is
prefixed **`P-`** (`P-15 §4` is the parent identity register, not this package's unknown-impact
register). Introduced after `RA-27`, which found the package reproducing against itself the exact
id-collision defect it had registered against its input as `MCD-01`.
| 20 | `VERY_DEEP_RESEARCH_STANDARD_ELIGIBILITY_ASSESSMENT` | **why the standard candidate is NOT generated** |
| 21 | `AAS_PLUS_EVIDENCE_MANIFEST_SHA256` | integrity |

### Note on file 20

The mandate authorises `SMEPLUS_VERY_DEEP_RESEARCH_STANDARD_CANDIDATE_L99999_99999.md` **if and only
if** stated criteria are met — among them *converged independent reviews* and *no unresolved
tolerance-zero issue*. Both fail (`PC-01`, `PC-02`), and the containment directive independently
forbids declaring any standard final. **The standard candidate is therefore not generated.** File 20
records the per-criterion assessment so the decision is auditable and so the method harvest is not
lost — the parent's own `MCC_K` reusable-method delta remains the live carrier for that work.
