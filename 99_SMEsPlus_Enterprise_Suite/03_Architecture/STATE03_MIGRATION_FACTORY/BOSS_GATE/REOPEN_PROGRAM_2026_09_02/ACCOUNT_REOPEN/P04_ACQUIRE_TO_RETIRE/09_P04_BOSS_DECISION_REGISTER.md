# 09 — P04 BOSS DECISION REGISTER

Layer: **2 — audit quarantine**.
**Boss interaction is FINAL GATE ONLY.** Nothing in this file asks for an
intermediate confirmation.

---

## 1. Decisions already taken — preserved, and what this session adds

| ID | Decision | Standing | New evidence from this session |
|----|----------|----------|-------------------------------|
| **BD-01** | Continuous internal equipment usage after full depreciation, **no residual cap**, no automatic cut-off, no reduction of book value; management/control concept only | **STANDING** | **Supported.** TAS 16 provides that depreciation may not be stopped for an idle or withdrawn asset **unless it is already fully depreciated** — so a fully depreciated asset still in internal use legitimately carries a **zero** charge. The decision is consistent with the standard as to the financial ledger (P04-F-30, P04-F-31) |
| **BD-02** | **100 % depreciation attribution**, by cause, nothing carried forward unclassified | **STANDING as to destination** | **Two new breaches by the reference behaviour**: capitalized additions are created **with no analytic distribution at all** (P04-F-53), and **mandatory analytic plans do not fire on any programmatic posting**, so attribution cannot be enforced by configuration (P04-F-52). Plus **a third compliant method option** (P04-F-54) |
| **BD-03** | The work centre must preserve actual operational meaning | **STANDING** | **Re-verified.** The routing operation declares 20 fields and none is an equipment reference; the equipment keyword returns zero hits across the manufacturing model packages (P04-F-37) |
| **BD-04** | One primary allocation driver per context unless evidence justifies otherwise | **STANDING with one declared departure** | Unchanged |

## 2. Decisions the Boss must take — carried forward from P3

| ID | Question | Recommendation carried | Consequence of deferring |
|----|----------|------------------------|--------------------------|
| **BLK-07** | Is the productive allocation rate *period depreciation ÷ **normal capacity** hours* or *÷ actual productive hours*? | **Normal capacity** | The AAS+ veto stands. **No costing implementation may begin** |
| **BLK-08** | Does maintenance split into planned (absorbed) and unplanned (period expense)? | **Split** | The non-productive model cannot be finalised |
| — | Accept the declared departure from `BD-04` (one driver per **cost class** rather than one per context) | **Yes** | The two-driver treatment TAS 2 ¶13 requires has no sanctioned basis |

## 3. Decisions this session adds to the Boss's list

| ID | Question | Why it is the Boss's | This session's position |
|----|----------|---------------------|-------------------------|
| **P04-BD-05** | At `BLK-07`, is there a **third** option: units-of-production as the TAS 16 depreciation **method**, with normal capacity as the TAS 2 **absorption denominator**? | It changes the **depreciation charge itself**, not merely its allocation — an accounting-policy election with tax consequences | **Offered as a genuine third option, not as a displacement of the standing recommendation.** It satisfies both standards and makes an idle month's charge genuinely zero. It requires a reliable expected-output estimate per asset, which nothing in the estate holds, and its tax consequences are unresearched (`HOLD-02`, `HOLD-05`) |
| **P04-BD-06** | Must the **derecognition entry post automatically**, or may it remain a draft awaiting human posting? | The reference behaviour leaves an asset reading "Closed" with **nothing posted**. Making it automatic is a control decision with a period-integrity consequence | **Recommendation: automatic, with a lock-date check that refuses rather than re-dates.** Stated as a recommendation only |
| **P04-BD-07** | Is **scrap** a distinct retire event from disposal in SMEsPlus? | The Thai evidence regimes differ: goods and scrap fall under an instruction requiring **30 days' advance notice** and an auditor witness; fixed-asset destruction rests on a **different** authority requiring proof of destruction and auditor certification | **Recommendation: yes, distinct** — one action cannot carry two evidence regimes. The residual statutory question is `P04-B-24` |
| **P04-BD-08** | Does the **capitalization-versus-expense decision** get a threshold policy, and at what scope? | There is no decision point in the estate at all; the flag is on the account and is evaluated per posted line. Whether the threshold is platform, tenant or company data is a scope decision | **Position: COMPANY scope** — it is an accounting-policy election (see `20` §2.2). No amount is proposed |
| **P04-BD-09** | Is the **asset model** a tenant-owned template or company-owned accounting truth? | It carries the depreciation method and duration, which are company accounting-policy elections, while behaving like a tenant policy template | **HOLD — SCOPE EVIDENCE REQUIRED** (`P04-SC-01`). Both readings are defensible; the choice determines whether one tenant's companies may diverge |

## 4. Where this session's evidence **changes** the shape of an existing decision

### 4.1 `BLK-07` — the denominator

P3 framed this as a binary between two readings of `BD-02`, one of which breaches
TAS 2 ¶13. This session obtained the TAS 16 material that P3 did not have, and it
shows the binary was incomplete:

> **TAS 16 governs the size of the charge. TAS 2 governs its absorption.**

Once the two are separated, three options exist rather than two, and the two
compliant ones differ in a way the Boss will care about: under normal-capacity
absorption of a straight-line charge, an idle month still produces a charge that
falls to period expense; under units-of-production, an idle month produces
**no charge at all**. The second is closer to the operational instinct behind
`BD-01` and `BD-02`, and it costs an estimate the business does not currently
maintain.

This is offered as information for the Final Gate. **It does not displace P3's
recommendation, and this session does not decide it.**

### 4.2 `BD-02` — attribution

Two new facts change what "100 % attributed" costs to implement:

1. **Capitalized additions carry no analytic distribution.** Every subsequent
   depreciation of an addition is un-attributed by construction. `BD-02` cannot
   be met without new behaviour at the point of capitalization.
2. **Mandatory analytic plans cannot enforce it.** The obvious control does not
   fire on programmatic postings, and depreciation entries would be skipped even
   if it did. Attribution must be enforced by something the design originates.

Neither changes the decision. Both change what complying with it requires.

## 5. Vetoes and conditions — status

| Control | Scope | Status |
|---------|-------|--------|
| **AAS+ veto on implementation start** | Costing model only; explicitly **not** on research, design work, or the Boss's Final Gate review | **NOT DISCHARGED.** Limb 1 (`BLK-07`) open. Limb 2 (single-mechanism proof) **wider than when issued** — nine paths, not three (`06` §2) |
| **PMO: approve with conditions** | Conditions are `BLK-07`, `BLK-08` and the runtime session | **NOT DISCHARGED** |
| **PMO: no controlled design freeze at this gate** | — | Unchanged. This session **does not declare an asset final freeze**, as instructed |
| **Independence limitation on the veto** | P3's audit was a structured self-challenge by the same session that did the work | **Materially relevant.** This session's own parallel streams disagreed on a population and one produced a false negative (`05` §6) — direct evidence for treating the veto's scope as a floor |

## 6. What this session does **not** ask the Boss to do

- It does not ask for confirmation of anything recorded here.
- It does not ask the Boss to choose between scope options; scope was resolved
  from business, legal and accounting semantics where possible and placed on
  **HOLD — SCOPE EVIDENCE REQUIRED** where not.
- It does not declare an asset final freeze.
- It does not declare implementation authorised, merged, or complete.
