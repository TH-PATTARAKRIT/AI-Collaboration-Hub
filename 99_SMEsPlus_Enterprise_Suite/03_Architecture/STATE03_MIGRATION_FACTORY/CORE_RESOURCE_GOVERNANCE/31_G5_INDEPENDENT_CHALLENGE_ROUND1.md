# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G5 — Independent Adversarial Challenge Round 1

Status: ROUND-1 CHALLENGE COMPLETE
Gate: G5 — Cell / Placement
Independent role: Architecture Audit / Adversarial Challenge
Final Approver: Boss only

## Challenge objective

Attempt to falsify the current recommendation (`General-purpose mixed-package Standard Cells + targeted isolated execution lanes`) and expose hidden coupling, false isolation, false capacity confidence, unsafe movement and economic blind spots.

## Findings

### CH-01 — A Cell could be only a logical label with no real fault boundary
Severity: CRITICAL
Attack: If App, DB, queue, storage and routing are globally shared without bounded failure domains, calling a Tenant group a Cell does not contain blast radius.
Required correction: define minimum Cell-boundary proof obligations and explicitly inventory global dependencies that can pierce the boundary.

### CH-02 — Weighted placement can mask a hard bottleneck
Severity: CRITICAL
Attack: an aggregate score can report `safe` while one hard dimension is exhausted.
Required correction: hard-veto eligibility must precede soft ranking; no compensating score across hard safety dimensions.

### CH-03 — Cold-start tenant placement can guess wrong
Severity: HIGH
Attack: new Tenants have no telemetry and can be radically heavier than organization/package signals imply.
Required correction: conservative initial reserve/profile, confidence label, observation window and early relocation/rebalance eligibility.

### CH-04 — Correlated legitimate bursts can invalidate independent forecasts
Severity: HIGH
Attack: many Tenants may peak at the same accounting/tax/payroll deadlines.
Required correction: Cell-level correlated-burst reserve/test scenarios and safety margin evidence.

### CH-05 — Stale telemetry can admit into an already unsafe Cell
Severity: CRITICAL
Attack: if capacity signals are delayed, placement is made from obsolete state.
Required correction: freshness/confidence gates; critical unknown/stale signal makes the Cell ineligible for new admission/heavy movement.

### CH-06 — Package-class Cells might outperform mixed Cells economically
Severity: MEDIUM
Attack: recommendation could be ideological if package/workload correlation is later strong.
Required correction: preserve package-class Cells as an empirical G8 alternative with A/B economics/load evidence.

### CH-07 — Mixed Cells can strand multidimensional headroom
Severity: HIGH
Attack: free CPU is useless if DB connections or storage/worker headroom is the limiting factor.
Required correction: dominant-resource/fragmentation awareness in ranking and scale-out decisions.

### CH-08 — Existing Cell can become hot after admission
Severity: CRITICAL
Attack: stop-placement prevents new load but does not solve organic growth.
Required correction: rebalance candidate state, targeted isolation/defer, package/capacity review, and controlled move path.

### CH-09 — Movement can create dual authoritative cells
Severity: CRITICAL
Attack: stale routers/workers/caches can write to source and destination after cutover.
Required correction: monotonic placement epoch/fencing token or equivalent single-authority mechanism, not cache invalidation alone.

### CH-10 — Long-running transactions can cross the movement boundary
Severity: CRITICAL
Attack: transaction starts on source and commits after destination becomes authoritative.
Required correction: explicit drain/quiesce/fence semantics, transaction outcome proof and reconciliation before source release.

### CH-11 — Queued jobs can execute twice or against stale placement
Severity: CRITICAL
Attack: messages created pre-move can be delivered post-move to wrong runtime or replayed.
Required correction: job carries Tenant identity plus placement epoch/context lineage; dequeue re-resolves authoritative placement; idempotency/replay rules mandatory.

### CH-12 — Data gravity can make destination `capacity-safe` but operationally non-movable
Severity: HIGH
Attack: DB/object data/backup/integrations may require long dual-capacity windows or exceed movement throughput.
Required correction: destination eligibility includes data-plane compatibility, temporary workspace, sync throughput and rollback reserve.

### CH-13 — Control-plane outage could cause wrong-cell guesses
Severity: CRITICAL
Attack: router cannot reach placement service and guesses/round-robins.
Required correction: fail-static to last-authoritative placement where safe; prohibit new movement/admission if authority cannot be proven.

### CH-14 — Global identity/routing/telemetry services recreate national blast radius
Severity: HIGH
Attack: Cells isolate data plane but shared control plane remains single point of failure.
Required correction: global dependency register and later HA/failure proof; G5 must not claim blast-radius containment beyond proven boundary.

### CH-15 — Admin override could bypass hard safety/isolation rules
Severity: CRITICAL
Attack: privileged operator forces placement into incompatible Cell.
Required correction: override cannot bypass security/integrity hard veto; dual-control/reason/evidence/audit required for exceptional placement.

### CH-16 — Automated Enterprise recommendation can blame customer for platform defects
Severity: HIGH
Attack: bad SQL/indexes/memory leaks create sustained pressure and trigger Enterprise upsell.
Required correction: platform-defect exclusion gate and evidence reason codes before tenant-heavy classification or Enterprise candidacy.

### CH-17 — Targeted isolation lane can become a hidden second product/runtime fork
Severity: HIGH
Attack: isolated heavy jobs evolve different business semantics or code version.
Required correction: one Core semantic contract; isolation changes resource boundary only, not business truth/workflow behavior.

### CH-18 — Targeted lanes can double-count metering/reservation
Severity: HIGH
Attack: resource is reserved in Cell and again in isolated lane or failed work is billed twice.
Required correction: reservation lineage, one canonical usage evidence chain, release unused reserve, platform-failed work excluded from automatic customer charge.

### CH-19 — Cell state flapping can trigger herd movement
Severity: HIGH
Attack: many Tenants are simultaneously marked for rebalance as state oscillates.
Required correction: hysteresis/cooldown, movement concurrency budget, prioritized candidate queue, no automated herd relocation.

### CH-20 — Scale-out itself can create underutilized operational sprawl
Severity: HIGH
Attack: adding Cells too early increases fixed Cost-to-Serve and fragmented capacity.
Required correction: G8 must compare scale-up vs scale-out economics and stranded headroom; G5 freezes logic, not trigger numbers.

### CH-21 — Cell failure recovery might exceed acceptable ERP continuity
Severity: HIGH
Attack: bounded blast radius is meaningless if recovery of a Cell is too slow or unreconciled.
Required correction: G7/G8 must prove backup/DR and Cell recovery time; placement release requires recoverability evidence.

### CH-22 — Same tenant could have cross-Cell active sessions during movement
Severity: CRITICAL
Attack: browser/API sessions pinned to source continue writes after route switch.
Required correction: authoritative routing epoch/session revalidation; stale placement must be rejected or redirected safely.

## Round-1 disposition

`G5 NOT READY — CORRECTION REQUIRED`.

No fatal contradiction to the Option C + E direction has been proven, but the draft cannot progress until CH-01 through CH-22 are explicitly controlled or carried as evidence obligations with safe non-freeze semantics.

Build / Merge / Production remain HOLD.
