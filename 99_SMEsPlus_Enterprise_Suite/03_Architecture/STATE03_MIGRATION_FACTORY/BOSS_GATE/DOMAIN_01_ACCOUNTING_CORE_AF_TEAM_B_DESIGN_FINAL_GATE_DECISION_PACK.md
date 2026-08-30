# DOMAIN_01 Accounting Core — Boss Final Gate Decision Pack

Date: 2026-08-30

## Gate Position

**BOSS FINAL GATE = OPEN FOR DECISION.**

Upstream evidence:

- Team B Round-7 content: `1779258d66a15c149212afb95a8ea5924e084cfe`
- Round-7 closure: `f4e8ff6ff5d54ac47e4f9f0162ac593a77f9983b`
- ChatGPT Independent Re-Audit Round 8: `c380e4862cb3437ccd100c5196ca0cd52789b630` — REVIEW PASS
- PMO Verification: `50276a71c6c8c5b7cd82de8e15a87bc3d4add993` — PASS WITH CARRY-FORWARD

This Gate decides the DOMAIN_01 Accounting Core **independent clean-room domain blueprint** only.

It does **not** automatically authorize Development, Production, or DOMAIN_02.

## What Is Being Presented for Approval

- Accounting Core capability model
- Domain boundaries
- Lifecycle and event model
- Accounting invariants and business rules
- Conceptual information model
- Accounting/mathematical principles
- Period and Fiscal-Year control semantics
- Known/Current historical-report viewpoint model
- Correction / Restatement / Void semantics
- Raw cumulative vs reporting vs presentation-balance semantics
- Control/audit objectives
- Migration-facing canonical requirements
- Exception/failure model
- Advancement objectives
- Clean-room provenance and traceability

## Independent Review Position

All ChatGPT reviewer findings through `M-AUD-16` are recorded as closed at domain-design level after seven targeted corrective rounds.

Round 8 found no new blocking accounting, temporal, clean-room, or active-semantic contradiction in the corrected surfaces reviewed.

Clean-room Critical Vendor-Derived Design Risk remains 0 in the verified design evidence.

## Boss Decisions — Seven Open Team B Assumptions

These were deliberately not decided by Team B, ChatGPT, or PMO.

### D01-GATE-A1 — Rounding method

Team B working proposal: `round-half-up`.

Boss options:

- A: Approve round-half-up as DOMAIN_01 baseline.
- B: Require a configurable rounding-policy mechanism; exact defaults deferred to implementation/regulatory profile.
- C: Return for additional evidence.

PMO recommendation: **B** — do not hard-bind one global rounding rule where currency/jurisdiction policy may differ; preserve exact-decimal core and make the approved rounding policy explicit by profile.

### D01-GATE-A2 — Ordinary Period Reopen time window

Current blueprint already separates Period Lock from permanent Consumption and routes corrections into consumed history through Restatement controls.

Boss options:

- A: No additional universal time-window restriction in Accounting Core.
- B: Add a configurable reopen time-window policy.
- C: Return for additional evidence.

PMO recommendation: **A with policy extension allowed later** — avoid an arbitrary hard-coded global window; Consumption/Restatement already protects relied-upon history.

### D01-GATE-A3 — Chart of Accounts template / instance structure

Team B Option B remains the working design and overlaps Team A `GAP-D01-05`.

Boss options:

- A: Approve Team B Option B as baseline.
- B: Hold pending additional cross-domain evidence.
- C: Return for redesign.

PMO recommendation: **A WITH CARRY-FORWARD** — approve the conceptual direction, but keep `GAP-D01-05` visible until cross-domain design proves the exact template/instance governance.

### D01-GATE-A4 — Audit tamper-evidence scope

Question: should SMEsPlus provide stronger tamper-evidence beyond the narrow legal scope currently evidenced?

Boss options:

- A: Approve broader tamper-evidence as an internal-control/advancement objective, without representing it as a legal mandate.
- B: Limit tamper-evidence to evidenced regulated classes.
- C: Return for additional evidence.

PMO recommendation: **A** — this is an advancement/control objective, provided documentation clearly separates internal control from statutory obligation.

### D01-GATE-A5 — Correction shape flexibility

Current design permits controlled reversal-repost and delta correction; Void is a full zero-net reversal instance.

Boss options:

- A: Approve both controlled correction forms.
- B: Standardize on reversal-repost only.
- C: Standardize on delta only.

PMO recommendation: **A** — retain business flexibility while keeping additive history, linkage, balance, audit and Restatement controls mandatory.

### D01-GATE-A6 — CO-02 / CO-06 authorization coupling

Current design rule: if stronger SoD is configured for corrections, unconsumed Amendment cannot remain an easier route that defeats the safe-correction control model.

Boss options:

- A: Approve coupling.
- B: Return for control redesign.

PMO recommendation: **A**.

### D01-GATE-A7 — Fiscal-Year Membership Restatement authorization tier

Current working default: `CO-15 Restatement-level-or-stricter` for post-reliance Fiscal-Year calendar/membership correction.

Boss options:

- A: Approve CO-15-level-or-stricter baseline.
- B: Require a separately defined higher tier.
- C: Return for additional evidence.

PMO recommendation: **A** — post-reliance fiscal-calendar reclassification can change restated historical presentation and should never be weaker than financial Restatement authority.

## Mandatory Carry-Forward

The following are not silently closed by this Gate:

1. Team A residual unknowns: 20.
2. STEP linkage: `TBD / BASELINE LINKAGE REQUIRED`.
3. Official Project / STATE / STEP progress percentages: `TBD / BASELINE REQUIRED` absent approved weighting.
4. Jira `ERPPLUS-100`: Assignee remains UNASSIGNED and Due Date remains TBD/empty until governance assigns them.
5. Any implementation choice not explicitly represented in the conceptual/domain blueprint.

## Boss Decision Options

### OPTION 1 — APPROVE WITH CONTROL

Approve DOMAIN_01 Team B clean-room domain blueprint, rule on A1-A7, carry forward the 20 Team A unknowns and governance red flags, and authorize only the next explicitly named process.

### OPTION 2 — APPROVE WITH CONDITIONS

Approve the blueprint but identify assumptions that must remain conditional before implementation.

### OPTION 3 — RETURN FOR REVISION

Identify exact finding/section/evidence requiring revision. No broad restart unless evidence justifies it.

### OPTION 4 — HOLD

State the missing evidence or governance prerequisite.

## Recommended Boss Ruling Format

```text
BOSS FINAL GATE — DOMAIN_01 ACCOUNTING CORE TEAM B

Decision: APPROVE WITH CONTROL

A1 Rounding: Option B
A2 Period Reopen: Option A
A3 COA Template/Instance: Option A WITH CARRY-FORWARD
A4 Audit Tamper-Evidence: Option A
A5 Correction Shape: Option A
A6 CO-02/CO-06 Coupling: Option A
A7 Fiscal-Year Membership Restatement Tier: Option A

Team A residual unknowns: CARRY FORWARD — 20
STEP linkage: TBD / BASELINE LINKAGE REQUIRED
Jira Assignee/Due Date: PMO RED FLAG — ASSIGN BEFORE ADMINISTRATIVE CLOSURE

Development Authorization: NOT GRANTED BY THIS DECISION unless separately stated.
Production Authorization: NOT GRANTED.
DOMAIN_02 Authorization: NOT GRANTED unless separately stated.

Boss is the sole Final Approver.
```

No Evidence = No Progress. Never Skip Gate.
