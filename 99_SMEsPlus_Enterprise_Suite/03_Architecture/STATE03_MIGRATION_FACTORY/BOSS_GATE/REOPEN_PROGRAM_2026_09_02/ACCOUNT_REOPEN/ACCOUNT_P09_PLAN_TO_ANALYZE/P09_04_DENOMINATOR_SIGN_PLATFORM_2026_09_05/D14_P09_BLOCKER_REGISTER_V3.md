# D14 — P09_BLOCKER_REGISTER_V3

**Checkpoint:** `CP-P09D14` · **Layer:** 1 — clean-room. **Count is not forced to seven — the register is enumerated and every CRITICAL is independently challenged.**

---

| ID | Finding | Severity | Evidence confidence | Live / latent | Owner | Closure requirement |
|---|---|---|---|---|---|---|
| **B7** | **version basis defect** — the programme's source is v18; deployments run v16 and v19 | **CRITICAL** | measured from module registries | **live** | P09 + P11 | version-match every mechanism claim |
| **B1** | accounting-event identity undefined | **CRITICAL** | prior rounds | live | Core Ledger / P11 | define and ratify |
| **B8** | **`TH-F-02`** — one of four builds admits balance-sheet types to consumption; depreciation consumption collapses under it | **CRITICAL → challenged, see §2** | gate text read directly; population reproduced exactly | **latent** — no deployment has the budget module on a matching version | P08 semantics · P11 build choice | determine which build each server runs |
| **B2** | non-asset equipment costing has no reference precedent | HIGH | prior rounds | latent | **Boss** | an architectural decision |
| **B3** | budget control policy undecided | HIGH | prior rounds | latent | **Boss** | a business choice |
| **B5** | denominator discipline not applied to the author's own work | **HIGH — raised from MEDIUM** | **three failures in three rounds**, this round a *unit* failure after two *population* failures | **live** | P09 | every count states its subject, unit and rule before publication |
| **B4** | which tenant deployment copy is live | MEDIUM | prior rounds | latent | environment | a deployment fact |
| ~~B6~~ | Thai chart typing decision | **CLOSED** | v19 template types correctly | — | — | discharged |

**8 enumerated · 7 open · 1 closed · CRITICAL 3 · HIGH 3 · MEDIUM 1.**

## 2. CRITICAL SEVERITIES — INDEPENDENTLY CHALLENGED

| ID | Challenge | Outcome |
|---|---|---|
| **B7** | *"the measurements are unaffected, so is this really CRITICAL?"* | **CRITICAL upheld.** The measurements survive, but every *mechanism* claim in five rounds is unverified against any running system. A package whose explanations are unattached to its deployments cannot be relied on for design |
| **B8** | *"latent, not live — no deployment has the budget module on a matching version. Should it be CRITICAL?"* | **CRITICAL upheld, with the latency stated.** It is a build-selection exposure: adopting the divergent build arms it on day one with no further act, and the exposure is invisible from the version the programme was reading |
| **B1** | *"has anything changed?"* | **CRITICAL upheld, unchanged.** It remains the ground for the implementation veto |

**B5 raised from MEDIUM to HIGH.** Three consecutive rounds have published a defective denominator, and this round's was a *unit* failure occurring **after** two population corrections — i.e. correcting the population did not prevent it. That is a live process defect affecting every number the package publishes, not a documentation nit.

## CHECKPOINT
**`CP-P09D14` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
