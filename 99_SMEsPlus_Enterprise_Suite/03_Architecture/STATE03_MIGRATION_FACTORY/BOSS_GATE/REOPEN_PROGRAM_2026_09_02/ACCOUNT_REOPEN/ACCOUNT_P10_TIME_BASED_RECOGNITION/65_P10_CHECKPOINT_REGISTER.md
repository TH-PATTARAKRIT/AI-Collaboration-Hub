# P10 — CHECKPOINT REGISTER

Session: `SMEPLUS-26-09-05-ACC-P10-TBR-DECISION-INTEGRITY-EVIDENCE-REPAIR-001`
Branch `research/account-p10-time-based-recognition-2026-09-04-001` · baseline verified at `f9b40b3`

---

| CP | Name | Status | Evidence / artefacts | Material delta | Next |
|----|------|--------|----------------------|----------------|------|
| `CP-P10D00` | Auto-resume bootstrap; baseline verified | **COMPLETE — EVIDENCE VERIFIED** | Baseline SHA confirmed, tree clean; peer heads read | P04 +10, P09 +2, P11 +12 commits; P08 unchanged | `D01` |
| `CP-P10D01` | TQ-13 authority breach reconstructed | **COMPLETE — EVIDENCE VERIFIED** | `38` | `TQ-13` does not exist; authoritative id `T0-13`/`P11-B-16`, status `HOLD`; close condition **refined** since last read | `D02` |
| `CP-P10D02` | Decision space restored | **COMPLETE — EVIDENCE VERIFIED** | `39` | `OPT-A` restored; six options, not three | `D03` |
| `CP-P10D03` | Coupled Boss decisions mapped | **COMPLETE — EVIDENCE VERIFIED** | `40` | **Three** coupled decisions, not two — corrected under challenge | `D04` |
| `CP-P10D04` | P11 correction supplement produced | **COMPLETE — EVIDENCE VERIFIED** | `41` | Prior package preserved | `D05` |
| `CP-P10D05` | R-08 recurrence root cause | **COMPLETE — EVIDENCE VERIFIED** | `42` | Three instances; corrective control was unfalsifiable | `D06` |
| `CP-P10D06` | Deployed DB population reconciled | **PARTIAL — RESUMABLE** | `43`, `67` | **Corrected: the population is a FLOOR.** At least 9 further deployed databases exist inside the declared population; 4 examined | `67` §2 |
| `CP-P10D07` | Lock-date exposure recalculated | **COMPLETE — EVIDENCE VERIFIED**, denominator corrected | `44`, `67` | **1 of 46 distinct companies** (1 of 90 company-rows). Independently re-derived twice | `D08` |
| `CP-P10D08` | Capability-vs-exposure matrix | **COMPLETE — EVIDENCE VERIFIED** | `45` | Capability 4/4; reachable 1/4; exposed 0/4 on the lock path | `D09` |
| `CP-P10D09` | Evidence-base challenge protocol executed | **COMPLETE — EVIDENCE VERIFIED** | `46`, `47` | Two findings failed step F | `D10` |
| `CP-P10D10` | EC-02 true population | **COMPLETE — EVIDENCE VERIFIED** | `48` | True population **five**, not two or six | `D11` |
| `CP-P10D11` | EC-04 obtainable work | **PARTIAL — RESUMABLE** | `49`, `44` | 1 closed, 3 partial; `TZ-1` closed then **corrected to partial** | 10 items at `64` |
| `CP-P10D12` | EC-07 clean-pass register | **COMPLETE — EVIDENCE VERIFIED** | `50` | Consecutive clean passes **zero**; this round cannot be one | `D13` |
| `CP-P10D13` | AASP-VETO-01 rev 3 re-evaluated | **COMPLETE — EVIDENCE VERIFIED** | `51`, `32` | **Veto remains and is strengthened**; grounds widened; a peer **design** veto found that also binds P10 | `D14` |
| `CP-P10D14` | Peer dependencies reconciled | **COMPLETE — EVIDENCE VERIFIED** | `53` | Population **18**, open **14** | `D15` |
| `CP-P10D15` | Scope expiry triggers registered | **COMPLETE — EVIDENCE VERIFIED** | `54`, `63` | 3 of 13 carry triggers | `D16` |
| `CP-P10D16` | Class C cross-process comparison | **COMPLETE — EVIDENCE VERIFIED** | `55` | 1 of 7 compared; 6 impossible until peers publish | `D17` |
| `CP-P10D17` | Shared-kernel dependency hardened | **COMPLETE — EVIDENCE VERIFIED** | `56` | Two of three elements decidable **without** `D-5` | `D18` |
| `CP-P10D18` | Domain-engine boundary hardened | **COMPLETE — EVIDENCE VERIFIED** | `57` | Termination condition and residue policy confirmed domain-owned | `D19` |
| `CP-P10D19` | P04/P08/P09/P11 peer refresh | **COMPLETE — EVIDENCE VERIFIED** | `58`, `59`, `53` | P08 unchanged, not reprocessed; P04 delta overturned P10's asset count; P09 delta overlaps `P10-F-38` | `D20` |
| `CP-P10D20` | Four AAS-03 challenge classes | **COMPLETE — EVIDENCE VERIFIED** | `66`, `67` | All four returned. **22 corrections**, 9 against this round's own repair documents, 1 caused by the control this round added | `D21` |
| `CP-P10D21` | AAS+ consolidation | **IN PROGRESS** | `67` | — | — |
| `CP-P10D22` | PMO supplemental review | **IN PROGRESS** | `68` | — | — |
| `CP-P10DFINAL` | Corrected decision package published | **IN PROGRESS** | `69`, manifest | — | commit, push, Jira |

## Blocked

| CP | Blocker |
|----|---------|
| `CP-P10D11` | `BLOCKED — TOOL / PERMISSION` for `TZ-4`/`TZ-5`/`TZ-6`: an executing reproduction needs a database service started on the host, a state change outside a read-only research session |
| `CP-P10D16` | `BLOCKED — EXTERNAL DEPENDENCY`: six comparisons are impossible until peers publish scope determinations |

---

## G02 BOUNDED-DEEP CLOSURE — `2026-09-06` — `CP-01` … `CP-12`

| CP | Subject | Status | Artefact | Result |
|----|---------|--------|----------|--------|
| `CP-01` | Baseline and reference SHAs verified | **COMPLETE** | register §1 | The prompt's declared baseline **does not exist**; the real head differs in five characters. Recorded as `G02-E-01`, **not** silently substituted. The other three SHAs verify |
| `CP-02` | P02 closure consumed as controlled input | **COMPLETE, then CORRECTED** | register §4 | Status preserved as HOLD. **But P10 consumed a P02 finding its author had withdrawn, breached three written handoff conditions, and never consumed a denominator correction P02 addressed to P10 by name** — `G02-R-01`, `-02`, `-03` |
| `CP-03` | Eleven closure-question traces | **COMPLETE** | 11 trace documents | Three headline findings; several corrected after challenge |
| `CP-04` | Functional Design Input Pack | **COMPLETE, then EXTENDED** | design pack | 39 labelled entries after challenge; five cross-cutting entries added, two restated |
| `CP-05` | Handoffs to P06 / P08 / P11 | **COMPLETE, then CORRECTED** | three handoffs | P08's inventory of its **own** control set was mis-stated and is withdrawn; peer identifiers added |
| `CP-06` | Handoff to P07 | **WAS MISSING — NOW COMPLETE** | `P10_TO_P07_HANDOFF.md` | Published after challenge. A declared route with an empty payload, over nine installed localisation modules and a `C — NOT SEARCHED` negative |
| `CP-07` | Contradiction, error and source-link registers | **COMPLETE** | three registers | |
| `CP-08` | Four AAS-03 adversarial challenges | **COMPLETE — EVIDENCE VERIFIED** | `P10_G02_AAS03_CHALLENGE_RECORD.md` | 71 findings · 60 accepted · 10 narrowed · 1 rejected. **One challenger claim INVERTED on P10 re-verification** |
| `CP-09` | Material Delta executions | **COMPLETE** | terminality record §2 | Six executed, four declined and routed. **Denominator 4 → 6 distinct, all six examined.** Version basis closed at schema level |
| `CP-10` | Clean-room and verdict-wording scans | **COMPLETE** | this register | **51 vendor tokens found in Layer 1, every one introduced by P10's own correction pass.** All scrubbed; rescan clean. Verdict scan: no prohibited wording |
| `CP-11` | Corrections applied in place with identifiers | **COMPLETE** | revision log | 19 corrections, `G02-R-01` … `-19`. **1 self-caught, 18 externally caught** |
| `CP-12` | Terminality record and all 13 CQ dispositions | **COMPLETE** | `P10_G02_TERMINALITY_RECORD.md` | **It had been ticked while absent** — `G02-R-08`, on the one question that certifies the other twelve |

> **The prior round's auto-resume state named this round's most valuable action as its `NEXT EXACT
> ACTION`** — *"examine the unexamined deployed databases inside the declared population, or state a
> scope-narrowing predicate that excludes them"*. **The closure round opened, wrote twenty documents,
> and did neither**, until an adversarial challenge located a peer correction saying the same thing.
> A resume state is only a control if it is read as an instruction rather than as a description.
