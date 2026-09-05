# AI13 — P09_UNRESOLVED_EVIDENCE_REGISTER

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room.

Everything this continuation could **not** settle, with its class and what would settle it. **No item here may be restated elsewhere as an absence, and no class B, C or D may be converted to A.**

---

## A. CLOSED BY THIS CONTINUATION

Recorded first, so the open list is not read as "nothing was settled".

| ID | Item | How it closed |
|---|---|---|
| `NS-12` / `DEP-P09-12` | whether any event other than depreciation allocates both legs symmetrically | **CLOSED** — `AI07`: five mechanisms, three in core accounting |
| the algebra | whether the net is truly zero and under what conditions | **CLOSED** — `AI02` Corollary 1, unconditional for the both-legs case |
| line eligibility | which rows participate | **CLOSED** — `AI03`: by assignment alone; no account-type, row-type, context or company test |
| surface behaviour | what each management report shows | **CLOSED from source** — `AI04` §3, five surfaces, four different answers |
| database presence | whether deployed data exhibits it | **CLOSED negatively** — `AI05`: no asset in any located deployment carries an allocation |

## B. OPEN — EVIDENCE REQUIRED

| ID | Item | Class | What would close it |
|---|---|---|---|
| `DEP-P09-14` | incidence: does any real deployment have an asset carrying an allocation? | **HOLD — DATABASE EVIDENCE REQUIRED** | re-run the existing read-only asset trace with the allocation field added to its field list — near-zero cost, no write |
| `DEP-P09-15` | surface divergence observed rather than derived | **HOLD — RUNTIME EVIDENCE REQUIRED** | read-only report execution against a deployment with posted depreciation |
| `SW-U-03` | magnitude of the accrued-orders tax-driven residue | **UNRESOLVED — DATA REQUIRED** | real order data with mixed tax rates |
| `AI11` §3 | whether work-centre hourly rates recover depreciation, making the masking interaction real | **UNRESOLVED — EVIDENCE REQUIRED**, routed to P03 | a costing-policy statement, not a code fact |
| — | reproduction of the defect in a sandbox | **HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED** | explicit Boss authority; none exists and none is assumed |

## C. OPEN — NOT SEARCHED

| ID | Item | Class |
|---|---|---|
| `SW-U-01` | write sites that set the allocation by record assignment rather than in a values dictionary — **the declared false-negative mode of this continuation's own sweep pattern** | **C** |
| `SW-U-02` | off-balance-sheet account rows | **C** |
| `SW-U-04` | tenant custom modules — the sweep covered the reference root only | **C** |
| `NS-13` | the full set of programmatic posting paths bypassing obligation validation | **B from P09's position** — enumerated by P04, not re-enumerated here |

## D. PRESERVED, NOT SETTLED HERE

| ID | Item | Why P09 does not settle it |
|---|---|---|
| `HOLD-AS-01` | whether a prior Asset package's costing-veto premise survives | **cross-track reconciliation is Boss-level.** Two parallel evidence tracks disagree; P09 records a pointer and stops |
| `DIS-09` | the same disagreement, as a preserved dissent | preserved verbatim |
| `DEP-P09-01` | the accounting-event identity | **blocking**, owned by Core Ledger / P11; ground for `AAS+-VETO-01` |
| `AI-R-01` | whether the analytic ledger is a cost-attribution ledger or a balanced subledger | **DESIGN DECISION REQUIRED AT FINAL GATE** — the reference pattern is both and neither |
| `DEP-P09-11` | Jira evidence | connector unauthorised in this environment; **tested in this session, not inherited** |

## E. THE ONE THING THAT WOULD CHANGE THE VERDICT

**If the reference product's design intent were shown to be a balanced analytic subledger**, then a net of zero would be correct by construction and the finding would be re-characterised from "defect" to "the net balance is not a cost figure and must never be used as one".

`AI04` §4 records that the source carries **no statement of intent** either way, and that the product's own surfaces are split — the analytic account presents debit/credit/balance like a subledger, while every management consumer filters to profit-and-loss accounts like a cost ledger. **This is why the intent question is routed as a design decision rather than asserted.** It is the single most load-bearing open item in this continuation, and it is a question about another party's design that P09 declines to answer on their behalf.

## CHECKPOINT

**CP-AI13 — UNRESOLVED EVIDENCE REGISTERED.** 5 items closed, 5 open on evidence, 4 unsearched, 5 preserved. Auto-continue.
