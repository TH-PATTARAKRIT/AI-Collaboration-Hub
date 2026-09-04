# P01 — DEPENDENCY REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Rule applied (`§2.2`, `§2.8` and correction `§7`): a dependency may block one decision.
It must not block unrelated research. Every dependency below is recorded and the session
continued past it.

---

## 1. GATING DEPENDENCIES

| ID | Dependency | Blocks | Status | Why P01 cannot settle it |
|---|---|---|---|---|
| `DEP-P01-01` | **Which generation and which copy of the reference system is the benchmark.** Two full generations are present in the workspace and they implement the receipt-to-bill bridge **differently**, not merely with different code (`EV-P01-24`, `EV-P01-25`). Several near-identical copies of the project's own custom addon set also exist at differing version strings. | Every design position that depends on the clearing-account model, the price-difference engine, or three-way matching | **DEPENDENCY OPEN — BOSS DECISION REQUIRED** | It is a programme decision, not a source fact. No document in the repository was found that names the target generation. |
| `DEP-P01-02` | **Tenant boundary test on the cross-company trigger.** Whether any control restricts cross-company document generation to a common tenant or to the acting user's allowed companies. | The tolerance-zero disposition under `EC-04` | **HOLD — SCOPE EVIDENCE REQUIRED** | The negative is class B: only three files were searched. Record rules and access paths were assigned to an independent expert. |
| `DEP-P01-03` | **Ownership of the withholding-tax event** — bill or payment. | The accounting event register row `AE-P01-18`, and the whole Thai payment-side ledger pattern | **HOLD — CROSS-PROCESS RECONCILIATION REQUIRED** | Shared with the Account track, where it is also held as a statutory question. |
| `DEP-P01-04` | **Statutory basis for every Thai tax and withholding position.** | Any claim about what is required rather than what the source system does | **HOLD — STATUTORY EVIDENCE REQUIRED** | No authoritative Thai statutory source was consulted in this session. None is available to it. |
| `DEP-P01-05` | **Owner of the received-not-billed obligation.** Two representations coexist: a clearing-account balance and a self-reversing accrual entry (`CONTRA-P01-02`). | The event-ownership rule `§2.7` for this fact | **DESIGN DECISION REQUIRED AT FINAL GATE** | Both mechanisms are verified to exist. Choosing one is a design decision. |
| `DEP-P01-06` | **Expert challenges were briefed under the superseded scope reading, and the correction could not be forwarded to them** (`REV-P01-02`). Any scope observation an expert *suppressed* as "missing company scoping" is invisible to a re-read. | `EC-07` — whether the expert pass counts as a clean independent pass under the corrected constitution | **DEPENDENCY OPEN** | Only a fresh pass briefed under the corrected constitution can close it. |

---

## 2. PEER-PROCESS DEPENDENCIES

Per correction `§7`, none of these stopped the session.

| ID | Peer session | Required fact | Current status |
|---|---|---|---|
| `PEER-P01-01` | P02 Order-to-Cash | Confirmation that no sales-side process creates a vendor payable | **NOT YET EXECUTED** — no peer process branch exists |
| `PEER-P01-02` | Inventory | The boundary between the receipt's first valuation layer and all subsequent value movement | Inventory track is live; its multi-tenant invariant work is published, its COGS dependency is on standing **HOLD** |
| `PEER-P01-03` | Asset | Acceptance that P01 owns only the asset *trigger* at bill posting | Asset track is live and has an outstanding veto on implementation start |
| `PEER-P01-04` | Account (core ledger) | FX rate ownership and missing-rate policy | A standing ruling exists on that track. **P01 inherits it and does not decide.** |
| `PEER-P01-05` | Account (core ledger) | Period-lock semantics and their bypass surface | Account track owns it; P01 records two candidate bypass routes for that track to test (`EV-P01-06` context override, `EV-P01-22` revaluation) |
| `PEER-P01-06` | P11 | Continuous reconciliation of scope semantics across P01–P10 | **NOT YET EXECUTED**. P01's scope matrix is its first input. |
| `PEER-P01-07` | SaaS / Platform Architecture | What proves ownership of a company-scoped financial effect (`HO-06`, re-framed by the correction) | **DEPENDENCY OPEN** |

**Method note.** "No peer process branch exists" was established by enumerating the full remote
branch list and filtering for process identifiers. False-negative mode: a peer session running
in another workspace that has not pushed would not appear. Class **B**, not A.

---

## 3. DEPENDENCIES DELIBERATELY NOT ALLOWED TO BLOCK

Recorded so that a reviewer can confirm the rule was honoured rather than take it on trust.

| Open dependency | Work that continued anyway |
|---|---|
| `DEP-P01-01` target generation | The whole `R1` forensic trace, with every finding tagged by generation, plus the cross-generation divergence table that *is* the evidence for the dependency |
| `DEP-P01-03` withholding ownership | Every non-withholding accounting event, the whole clearing bridge, asset triggering, cross-company analysis |
| `DEP-P01-04` statutory basis | All source-behaviour findings, stated as source behaviour and never as legal requirement |
| `DEP-P01-06` expert brief timing | The scope matrix was produced directly by this session rather than waiting on the experts |
| `PEER-P01-*` all | Everything above |
