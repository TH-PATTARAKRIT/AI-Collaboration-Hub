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
