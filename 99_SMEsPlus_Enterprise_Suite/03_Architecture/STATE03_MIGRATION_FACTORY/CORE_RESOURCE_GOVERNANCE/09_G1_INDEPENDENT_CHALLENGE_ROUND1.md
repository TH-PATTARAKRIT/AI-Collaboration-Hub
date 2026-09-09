# [SMEPLUS-26-09-09-CORE-RESOURCE-GOV-001]
# G1 — Independent Architecture Challenge / Round 1

Status: CHALLENGE COMPLETE — CORRECTION REQUIRED
Independence: This challenge does not own the solution and does not grant final architecture approval.
Inputs:
- `02_G0_PARENT_EVIDENCE_REGISTER.md`
- `03_G0_BOSS_DECISION_CARRY_FORWARD_REGISTER.md`
- `04_G0_CONTRADICTION_AND_SUPERSESSION_REGISTER.md`
- `05_G0_OPEN_ASSUMPTION_AND_MISSING_EVIDENCE_REGISTER.md`
- `07_G1_TERMINOLOGY_AND_INVARIANT_DRAFT.md`
- `08_G1_SPECIALIST_REVIEW.md`

## 1. Challenge Questions

1. Can any frozen term later be used to smuggle in a physical topology decision?
2. Can any billing term be interpreted as unsecured postpaid authorization?
3. Can any protection term justify shutting down critical ERP behavior without an explicit safety basis?
4. Can internal infrastructure cost be mislabeled as customer usage?
5. Can telemetry become chargeable without provable Tenant attribution?
6. Can Standard/Enterprise mobility change Tenant/business identity?
7. Can numerical sizing be inferred from terminology despite missing evidence?

## 2. Findings

### CH-01 — `Overage` remains semantically dangerous

Severity: MATERIAL.

Even with a non-credit disclaimer, using `Overage` as a first-class canonical term can be interpreted operationally as "consume now, bill later." This conflicts with Prepaid Before Usage and No Unsecured Postpaid Overage.

Required correction:
- Primary canonical term = `Additional Chargeable Usage`.
- `Overage` = optional customer/commercial label only where the contract explicitly preserves prepaid/secured authorization.

### CH-02 — Usage evidence must have a promotion boundary

Severity: MATERIAL.

The draft distinguishes Raw Telemetry, Normalized Usage Event and Usage Ledger, but does not yet make the promotion rule explicit enough.

Required correction:
A Raw Telemetry observation may become a Normalized Usage Event only when trusted context can prove at minimum Tenant attribution, resource/unit identity, event time/period, deduplication/idempotency identity where applicable, and evidence lineage.

Chargeable Usage requires an additional contractual/entitlement/financial-authorization evaluation.

### CH-03 — `Usage Ledger` can collide with accounting semantics

Severity: MATERIAL.

ERP teams may treat any object called a ledger as statutory accounting truth.

Required correction:
Name/define the object as `Usage Evidence Ledger` and explicitly state that it is an operational/audit evidence record, not General Ledger, Subledger or accounting posting. Financial posting, if any, is a separate controlled consequence.

### CH-04 — Hard Cap / Protected Mode ambiguity

Severity: MATERIAL CUSTOMER-IMPACT RISK.

A resource/action cap could be implemented as a tenant-wide shutdown if vocabulary is not constrained.

Required correction:
- Protected Mode = staged, deterministic restriction policy.
- Hard Cap = resource/action-specific stop boundary by default.
- Tenant-wide or whole-service restriction requires separate explicit policy/safety basis and cannot be inferred from the term alone.
- Critical ERP integrity actions receive operating-reserve priority where technically safe, but never override physical safety/correctness limits.

### CH-05 — ENTERPRISE dedicated boundary can be over-physicalized

Severity: MATERIAL ARCHITECTURE RISK.

`Dedicated environment` may later be interpreted as one tenant = one physical server/database.

Required correction:
Define ENTERPRISE as a dedicated resource/security/operational boundary with stronger isolation/SLA. The realization may be VM/container/node pool/DB boundary/storage boundary/hybrid and remains evidence-dependent.

### CH-06 — Scalar capacity inequality is too simplistic

Severity: MATERIAL MODEL RISK.

`Commercial Limit < Protection Boundary < Failure Boundary` is not universally scalar because DB size, CPU saturation, queue delay, connections, IOPS and storage may have different state spaces.

Required correction:
Express this as a per-resource-dimension/policy invariant: commercial entitlement must leave sufficient technical protection margin before the measured unsafe/failure region. Exact relationship and headroom are evidence-driven.

### CH-07 — Cost-to-Serve must not mutate into billable usage

Severity: MATERIAL COMMERCIAL RISK.

Internal physical amplification (indexes, replicas, WAL, backups, spare headroom) is valid Cost-to-Serve evidence but cannot automatically be customer usage.

Required correction:
Freeze a rule that customer chargeable units and internal cost metrics can differ, but any commercial conversion needs an explicit published mapping and cannot hide platform inefficiency/protection overhead as customer consumption.

### CH-08 — G1 must freeze definitions, not mechanisms or numbers

Severity: GATE CONTROL.

The draft appropriately holds numbers/topology. This must remain explicit in the final freeze.

Required correction:
Add a formal `G1 Freeze Boundary` section prohibiting derivation of package GB/CPU/RAM/API/price/cell thresholds from the vocabulary alone.

## 3. Adversarial Scenarios

- A low-user tenant runs a massive API integration: organization size does not redefine Tier; workload evidence governs suitability.
- A tenant generates high WAL due to SMEsPlus bad SQL: WAL cost cannot be charged as customer usage merely because it is tenant-correlated.
- A customer wallet is nearly depleted while an accounting posting is in-flight: terminology cannot authorize arbitrary interruption; protection policy must preserve correctness subject to safety.
- A Cell has abundant CPU but DB connections near exhaustion: no single scalar "70% full" metric may authorize placement.
- Enterprise tenant uses a dedicated DB cluster shared only within its controlled resource boundary: dedicated does not require a single physical server.
- Duplicate telemetry arrives after retry: evidence promotion requires deduplication/idempotency controls before chargeability.

## 4. Round-1 Verdict

`REWORK REQUIRED — 8 MATERIAL TERMINOLOGY/INVARIANT CORRECTIONS`

G1 may not pass until corrections CH-01 through CH-08 are incorporated and independently re-challenged.
