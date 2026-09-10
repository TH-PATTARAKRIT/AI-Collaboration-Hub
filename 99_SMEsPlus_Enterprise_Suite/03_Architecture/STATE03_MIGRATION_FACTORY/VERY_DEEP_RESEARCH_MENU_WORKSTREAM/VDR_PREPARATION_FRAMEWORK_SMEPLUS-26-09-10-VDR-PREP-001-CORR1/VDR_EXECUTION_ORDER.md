# VDR_EXECUTION_ORDER.md
# Universal VDR Execution Sequence (Preparation Control 05)

Session: `[SMEPLUS-26-09-10-VDR-PREP-001-CORR1]`
Layer: **LAYER 1 — CLEAN-ROOM.**
Status: **FROZEN v1.0**

---

## 1. Frozen Sequence

```
  [0]  EVIDENCE BASE ESTABLISHMENT          <- added by the Inventory Pilot (CORR-F-01)
        path set swept, generation fixed by content discriminator, exclusions declared
                     |
  [1]  LESA                                  Lead ERP Solution Architect
                     |
  [2]  SOURCE LEARNING POPULATION            00_SOURCE_LEARNING_MASTER_LIST.md
                     |
  [3]  POINT-FOCUS VDR                       know what / know where / research deeply
                     |
  [4]  NINE MANDATORY REGISTERS              01..09, every record carries a Learning ID
                     |
  [5]  COVERAGE RECONCILIATION               VDR_COVERAGE_RULE.md, per dimension
                     |
  [6]  PACKAGE FREEZE                        <- added by the Inventory Pilot (CORR-F-02)
                     |
  [7]  SMEs CORE INDEPENDENT CHALLENGE       producer is not the validator
                     |
  [8]  LESA SOURCE RESOLUTION                unknowns routed to LESA, never free-searched
                     |
  [9]  TARGETED DELTA RESEARCH               material delta only
                     |
 [10]  SMEs CORE RE-CHALLENGE
                     |
 [11]  PMO VERIFICATION                      evidence integrity, not conclusions
                     |
 [12]  BOSS FINAL DECISION
```

**No team may bypass this order.** Steps [0] and [6] were inserted by the Inventory Pilot; the
original sequence began at LESA, which allowed a domain to be researched before its evidence base was
established, and allowed challenge to open on a moving package.

---

## 2. Step Entry / Exit Contracts

| Step | May start when | May close when |
|------|----------------|----------------|
| 0 | A domain is nominated | PATH SET published with exclusions and reasons; generation fixed by a content-based discriminator; runtime evidence census published or its absence proved |
| 1 | Step 0 closed | LESA has named what exists, where, what activates it, what it controls, what it impacts |
| 2 | Step 1 closed | Population derived by rule (D1–D5 executed), instrument controls I1–I4 recorded |
| 3 | Step 2 closed | Every researched item points at a Learning ID |
| 4 | Step 3 in progress | All nine registers exist; zero orphan records |
| 5 | Step 4 closed | Per-dimension coverage published with its denominator |
| 6 | Step 5 closed | Commit SHA recorded; manifest hashed |
| 7 | Step 6 closed | All 30 challenge questions dispositioned |
| 8 | A `SOURCE RESOLUTION REQUIRED` exists | Evidence pointer produced or formally `HOLD` |
| 9 | Step 8 produced a material delta | Delta researched; registers and coverage recomputed |
| 10 | Step 9 closed | Re-challenge dispositioned; no unresolved `CONTRADICTION` |
| 11 | Step 10 closed | PMO has verified evidence integrity by the four disjoint-unit sweeps |
| 12 | Step 11 closed | — Boss only — |

---

## 3. Loop Control

`SOURCE RESOLUTION LOOP`:

```
SMEs Core Finding -> LESA Source Resolution -> Evidence Pointer
   -> Master List Update -> Targeted Delta VDR -> Register Update
   -> Coverage Recalculation -> SMEs Core Re-Challenge
   -> RESOLVED  |  FORMALLY HOLD
```

Anti-loop rules:
- **No repeated research without material delta.** A repeated question with no new evidence is closed
  as `NO MATERIAL DELTA` and recorded once.
- **A resume state is an instruction.** The previous round's `NEXT EXACT ACTION` and any peer
  correction naming this workstream must be consumed in the first act of the next round.
- **Do not stop the whole programme for a local non-material issue** if unaffected subjects can
  continue safely; do not continue a subject whose Critical Area is open.

---

## 4. Role Boundaries

| Role | May decide | May not decide |
|------|-----------|----------------|
| LESA | What exists in the reference evidence and where | SMEsPlus target architecture |
| Research Team | What the evidence shows | Whether its own work is sufficient |
| SMEs Core | Whether evidence supports a claim | Final closure |
| PMO | Whether evidence integrity holds | Whether the design is right |
| Boss | Everything reserved to Boss | — |

`REFERENCE KNOWLEDGE != SMEsPlus DESIGN AUTHORITY.`
`NO EVIDENCE = NO PROGRESS.` · `NEVER SKIP GATE.` · `NO DOWNSTREAM GUESSING.`
