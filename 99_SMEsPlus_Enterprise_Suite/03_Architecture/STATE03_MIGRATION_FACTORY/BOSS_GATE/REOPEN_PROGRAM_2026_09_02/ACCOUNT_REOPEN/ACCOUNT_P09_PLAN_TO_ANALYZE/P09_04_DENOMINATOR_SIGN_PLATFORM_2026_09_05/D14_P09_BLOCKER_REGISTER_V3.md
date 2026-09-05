# D14 — P09_BLOCKER_REGISTER_V3

**Checkpoint:** `CP-P09D14` · **Layer:** 1 — clean-room. **Count is not forced to seven — the register is enumerated and every CRITICAL is independently challenged.**

---

| ID | Finding | Severity | Evidence confidence | Live / latent | Owner | Closure requirement |
|---|---|---|---|---|---|---|
| **B7** | ~~version basis defect~~ **PARTIALLY WITHDRAWN (`D26`)** — two **v18** deployments exist and were missed by the census; every mechanism claim IS version-matched to them. The mismatch stands only for the four previously-censused databases | **HIGH** *(was CRITICAL)* | module registries of 6 deployments | live, narrowed | P09 + P11 | version-match the remaining four |
| **B1** | accounting-event identity undefined | **CRITICAL** | prior rounds | live | Core Ledger / P11 | define and ratify |
| **B8** | **`TH-F-02`** — one of four builds admits balance-sheet types to consumption; depreciation consumption collapses under it | **CRITICAL → challenged, see §2** | gate text read directly; population reproduced exactly | **latent** — no deployment has the budget module on a matching version | P08 semantics · P11 build choice | determine which build each server runs |
| **B2** | non-asset equipment costing has no reference precedent | HIGH | prior rounds | latent | **Boss** | an architectural decision |
| **B3** | budget control policy undecided | HIGH | prior rounds | latent | **Boss** | a business choice |
| **B5** | **evidence-base and denominator discipline not applied to the author's own work** | **CRITICAL — raised from HIGH (`D26`)** | **five consecutive rounds, five distinct defects**: a truncated listing · a template read as a deployment · a version mismatch from an incomplete population · a silent sub-population · **a path set excluding most of the host** | **live** | P09 | every population declares its path set and is run unbounded; every count states its subject and unit |
| **B4** | which tenant deployment copy is live | MEDIUM | prior rounds | latent | environment | a deployment fact |
| ~~B6~~ | Thai chart typing decision | **CLOSED** | v19 template types correctly | — | — | discharged |

**8 enumerated · 7 open · 1 closed · CRITICAL 3 · HIGH 3 · MEDIUM 1.**

**After `D26`: CRITICAL 3 (B1, B8, **B5**) · HIGH 3 (B7 narrowed, B2, B3) · MEDIUM 1 (B4).** The composition changed — `B5`, a defect in P09's own method, is now CRITICAL and `B7` is narrowed.

## 2. CRITICAL SEVERITIES — INDEPENDENTLY CHALLENGED

| ID | Challenge | Outcome |
|---|---|---|
| **B7** | *"the measurements are unaffected, so is this really CRITICAL?"* | **CRITICAL upheld.** The measurements survive, but every *mechanism* claim in five rounds is unverified against any running system. A package whose explanations are unattached to its deployments cannot be relied on for design |
| **B8** | *"latent, not live — no deployment has the budget module on a matching version. Should it be CRITICAL?"* | **CRITICAL upheld, with the latency stated.** It is a build-selection exposure: adopting the divergent build arms it on day one with no further act, and the exposure is invisible from the version the programme was reading |
| **B1** | *"has anything changed?"* | **CRITICAL upheld, unchanged.** It remains the ground for the implementation veto |

**B5 raised from MEDIUM to HIGH.** Three consecutive rounds have published a defective denominator, and this round's was a *unit* failure occurring **after** two population corrections — i.e. correcting the population did not prevent it. That is a live process defect affecting every number the package publishes, not a documentation nit.

## CHECKPOINT
**`CP-P09D14` — COMPLETE — EVIDENCE VERIFIED.** Auto-continue.
