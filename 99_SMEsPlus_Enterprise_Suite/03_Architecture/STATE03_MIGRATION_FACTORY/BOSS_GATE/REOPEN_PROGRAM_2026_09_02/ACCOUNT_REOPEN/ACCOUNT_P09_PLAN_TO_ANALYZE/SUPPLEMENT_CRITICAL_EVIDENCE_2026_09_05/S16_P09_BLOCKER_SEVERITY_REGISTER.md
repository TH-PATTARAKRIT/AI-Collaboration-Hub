# S16 — P09_BLOCKER_SEVERITY_REGISTER

**Checkpoint:** `CP-P09S16` · **Layer:** 1 — clean-room.
**The count is not forced to six.** The authoritative population is enumerated below and is **seven**.

---

| ID | Finding | Severity | Evidence | Owner | Closure requirement |
|---|---|---|---|---|---|
| **B7** | **VERSION BASIS DEFECT** — the whole programme reasons from a version-18 source tree; **no deployment runs version 18** (one runs 16, three run 19). Every mechanism claim is read from a version nobody runs | **CRITICAL** | module registries of all four deployments | **P09 + P11** | re-verify every mechanism claim against the version each deployment actually runs |
| **B8** | **`TH-F-02`** — the **version-19** budget gate **explicitly admits** fixed, current and non-current asset types, so the balance-sheet leg enters budget consumption on the shipping platform. Not Thai-specific, not template-specific | **CRITICAL** | v19 source read directly, two places in one query; offsetting population measured at ~17,400 record pairs | **P08 + P09** | determine which addons path each v19 server runs — **two candidate builds carry opposite filters** |
| **B1** | accounting-event identity undefined — P09's standing blocking dependency, ground for `AAS+-VETO-01` | **CRITICAL** | prior rounds | Core Ledger / P11 | define and ratify the event object |
| **B2** | non-asset equipment costing has **no reference precedent** | **HIGH** | prior rounds | **Boss** | an original architectural decision |
| **B3** | budget control policy — advisory, warn, approve or block | **HIGH** | prior rounds | **Boss** | a business choice, not a gap |
| **B5** | the sweep denominator must be re-derived over the union pattern; the declared pattern did not contain its own subject | **MEDIUM** | `S07` — 45 vs 82 vs 83 vs 328, four residue classes | P09 | re-derive, or state every count with its unit |
| **B4** | which tenant deployment copy is live — two capabilities depend on it, one statutory | **MEDIUM** | prior rounds | environment | a deployment fact |
| ~~B6~~ | ~~Thai chart typing decision~~ | **CLOSED** | the v19 template types accumulated depreciation **correctly**; TH-F-01 superseded | — | discharged by `S22` |

## Distribution

**7 open · CRITICAL 3 · HIGH 2 · MEDIUM 2 · 1 closed this supplement.**

## The two additions and the one closure

- **B7 and B8 are new and both outrank every pre-existing blocker.** B7 is a defect in the evidence base itself; B8 is a live exposure on the shipping platform that the programme could not have seen while reading the wrong version.
- **B6 closes** — the finding that raised it is superseded. **A blocker closed by evidence, not by decision.**

## P11 impact

B7 and B8 change what P11 can rely on. **Until B7 is discharged, no P09 mechanism claim should be treated as describing a running system** — only as describing version-18 source. The measurements are unaffected and remain usable.

## CHECKPOINT
**`CP-P09S16` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
