# 10 — PHASE S CLOSURE CRITERIA — INDEPENDENT TEST

**Criteria population:** the **ten** in `05_PHASE_S_CLOSURE_CRITERIA_REGISTER.md` @ `0941161`, §12.
**Rule (§8):** no criterion may be marked TRUE from documentary assertion alone where its own rule
requires independent reproduction or challenge.

## 1. Result — **criteria 1, 2 and 6 are FALSE. Phase S is NOT closable.**

| # | Criterion | Prior state | **This session** | Basis |
|---|---|---|---|---|
| 1 | every queue item has a terminal disposition | FAILS (0 of 13) | **FALSE** | 11 of 13 items are *completion-gated* on an `RC-*` (`Q-BOSS-01` §2). **All six RCs are `RC-HOLD`.** The 2 ungated items (`Q-P06-02`, `Q-P08-03`) are executable but are **2, not 13** |
| 2 | every changed material surface received the required fresh challenge | FAILS (0 of 6) | **FALSE — 0 of 6, unchanged** | `07_` §1. Six surfaces frozen, six untested |
| 3 | no material evidence-integrity defect unbounded/unclassified | PASSES | **RE-OPENED — see §2** | `IV-R-04` and `IV-R-05` are material evidence-integrity defects found **after** this criterion was scored, and were unbounded until this package |
| 4 | no unresolved cross-package contradiction consumed as current authority | FAILS | **FALSE** | 6 live propagation edges; resolution requires RC outcomes (`08_` §1 sweep 5) |
| 5 | no stale/superseded evidence silently treated as current | FAILS | **FALSE** | 3 CORR2-era peer SHAs in P11's live outbound registers remain unswept (inside `RC-02`). `08_` §3 clears only the frozen refs |
| 6 | every veto has a defensible disposition **and lifting evidence where required** | FAILS | **FALSE, on two independent grounds** | (a) **0 rows dischargeable**, no lifting evidence exists (`09_` §2); (b) `AAS+-PS-VETO-01 C-6` is **reserved to Boss** and is *"not reachable by any correction work"*. **`IV-R-05` adds a third: the population itself is unreproducible** |
| 7 | every Boss-only decision explicitly listed, none silently decided by AI | PASSES | **TRUE — re-tested and reproduced** | 51 = 19+19+10+3, arithmetic checked against the source register. **0 answered, 0 narrowed, 0 eliminated by this session.** One new Boss item raised in `11_` §2 and **explicitly listed, not decided** |
| 8 | P07 read-only dependencies checked for closure impact | PASSES with caveat | **TRUE — re-verified, caveat still live** | P07 head measured at `ee2be30`, **unmoved**. No P07 artefact opened, no mutation required *now*. The caveat resolves inside `RC-02`, which is on HOLD (`08_` §4) |
| 9 | no implementation / FD / Phase A-B-C work started | PASSES | **TRUE** | this session produced 0 lines of schema, API or code; no FD artefact; no merge; no release |
| 10 | all evidence published with immutable SHA + path and remote read-back | PASSES for its session | **TRUE for this session** | every claim here cites branch + SHA + path; `IV_EVIDENCE_MANIFEST_SHA256.md`; remote read-back recorded in `IV_CHECKPOINT_REGISTER.md`. **Does not extend to criteria 1–2, which have no evidence to publish** |

**Independently tested: 4 TRUE · 5 FALSE · 1 RE-OPENED. Criteria 1, 2 and 6 are each dispositive alone.**

## 2. Criterion 3 — re-opened, and why that is not a technicality

Criterion 3 asks whether every material evidence-integrity defect is **bounded, classified and owned**.
It was scored **PASSES** on the state then known, and that scoring was correct on its evidence.

**This session found two material defects that were not bounded at the time it was scored:**

| Defect | Class | Why it is criterion-3 material |
|---|---|---|
| `IV-R-04` | a published manifest coverage assertion is **false against its own declared command**, in **two live manifests** — including the one repaired for exactly this defect in the same commit | a coverage assertion is the control the programme relies on to know a package is whole. **A false one cannot report its own failure** |
| `IV-R-05` | the standing-veto total **17** is asserted and not reproducible; the register's own rows enumerate **19–22** | it is the denominator of criterion 6 |

**Neither is catastrophic and neither loses evidence** — both manifests list every real file, and
*"0 discharged"* holds under every reading. **Both are now bounded, classified and routed by this
package**, which is precisely what criterion 3 requires. The correct reading is therefore:
**criterion 3 was scored on an incomplete population and is re-establishable once these two are
accepted by their owners — not that it collapsed.** Recorded as RE-OPENED rather than FALSE, and
**not** silently left at PASSES.

## 3. The criterion that cannot be reached from here

**Criterion 2 is the gate, and criterion 6 depends on it.** Both require an `RC-*` challenge executed
by a party satisfying `Q-BOSS-02` §1. **No such party has executed one.** No amount of owner
correction, no further remediation round, and no additional evidence changes this: the remaining
blocker is **an eligible executor**, and appointing or dispatching one is a Boss act.

**`CP-SC-14 — READY FOR BOSS PHASE S FINAL DECISION` is NOT published.**
