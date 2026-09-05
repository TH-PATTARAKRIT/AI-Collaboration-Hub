# P09_DEPENDENCY_REGISTER

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · **Process:** P09 Plan-to-Analyze
**Issued/updated under:** `SMEPLUS-26-09-04-ACC-REV2-CORR1`
**Layer:** 1 — clean-room.

---

## A. BLOCKING DEPENDENCIES — P09 CANNOT COMPLETE ITS MODEL WITHOUT THESE

| ID | Dependency | Owner | Why P09 is blocked | Status |
|---|---|---|---|---|
| **DEP-P09-01** | **Accounting-event identity.** P09's semantic trace step 2 has no carrier: the reference pattern has no accounting-event identity and no provenance carrier, a gap inherited from the Core Ledger study and confirmed here. | Core Ledger / P11 | Six P09 requirements (SM-03, SM-14/15, B-02, B-03, AB-05, AB-07) are all expressed *relative to an event object that does not exist*. | **OPEN — blocking.** Subject of `AAS+-VETO-01`. |
| **DEP-P09-02** | **Cost object definition.** No first-class cost object exists; ten de facto cost objects were found, one shared record type, no discriminator. | P09 proposes; P03 and P04 own two of the contested types | The trace's step 5 has no carrier. P09 has specified the object (CO-04, CO-05, §5 of the cost-object model) but cannot ratify the manufacturing and asset types alone. | **OPEN — blocking for those two types only.** |

## B. PEER DEPENDENCIES — OPEN, AND P09 DOES NOT STOP FOR THEM

Per §7 of the constitution correction: recorded as `PEER DEPENDENCY OPEN`; all unaffected work continued.

| ID | Dependency | Counterpart | P09's own position, pending reconciliation |
|---|---|---|---|
| **PD-01** | scope of the manufacturing order and the work centre as cost objects | P03 Manufacture-to-Cost | manufacturing order → COMPANY; work centre → **undetermined**, held as `HOLD-SC-01` |
| **PD-02** | asset↔equipment relationship, asset cost-object scope | P04 Acquire-to-Retire | asset → COMPANY. P09 additionally hands over the finding that the only equipment↔accounting bridge in the tenant custom set runs backwards, from the asset to the equipment, as a status flip |
| **PD-03** | whether commitment is ledger-visible (an encumbrance) | P01 Procure-to-Pay | in the reference pattern commitment is a *reporting* concept only, never a posting. P09 proposes commitment as the budget control point (BC-02) — which makes this dependency material |
| **PD-04** | accounting-event identity | Core Ledger / P11 | see DEP-P09-01 |
| **PD-05** | whether a tenant may span jurisdictions — decides whether a TENANT-scoped budget is admissible at all | P07 TH Tax Compliance / P11 | P09 proposes TENANT-scoped budgets as legitimate (BC-08). If a tenant may not span jurisdictions the proposal narrows |
| **PD-06** | the platform definition of tenant | P11 | P09 **assumes** a tenant concept throughout and does not own it. Every TENANT determination in `P09_SCOPE_OWNERSHIP_MATRIX` is conditional on this |
| **PD-07** | the bill-line overwrite path and its sales mirror are P09 findings inside another process's territory | P01, P02 | handed over as findings, **not adjudicated**. P09 does not rule on another process's ownership model |
| **P04-PD-04** | **ACCEPTED, owner P09.** The analytic **plan** is a TENANT candidate (a reporting structure); the **distributed amount** is a COMPANY financial fact. They are different objects and must be scoped separately. | raised by P04, owned by P09 | **P09 accepts and records convergence.** `19` §3 reached the same determination independently, from a different domain, without sight of P04's. P04's sharper corollary is adopted below as **MA-11**. |

**MA-11 (new, adopted from `P04-PD-04`).** A **company-scoped attribution requirement shall never be enforced through a tenant-scoped structure.** Relying on the analytic plan — a TENANT-scoped reporting structure — to enforce a COMPANY-scoped attribution obligation is a **scope mismatch in the design intention**, independent of whether the enforcement mechanism fires at runtime.

This is a stronger statement than P09's own MA-08 and MA-09: those require scope to be *declared* and *consistently enforced*; MA-11 additionally requires that **the object carrying an obligation be of the same scope as the fact the obligation governs.**

*Why it matters here:* the reference pattern's obligation mechanism sits on the plan, and its enforcement is gated twice over — by execution context, then by row type. Even if both gates were removed, the control would still be a tenant-scoped structure policing a company-scoped financial attribution.

## C. EVIDENCE DEPENDENCIES — SOMETHING MUST BE LOOKED AT

| ID | Item | Raised by | Class | What would close it |
|---|---|---|---|---|
| **DEP-P09-03** | which of the three tenant custom copies is deployed | research team | **D** | a deployment fact from the environment, not a code search. Until then, whether the department dimension and one statutory Thai capability exist **at all** is unknown |
| **DEP-P09-04** | access rows for the two budget objects were not located in the budget module's own security directory | X4, class B | B | locate the granting module. **No participant may close this by not having searched** |
| **DEP-P09-05** | whether the report filter's integer-versus-JSON comparison matches correctly or silently returns nothing | X3, raised while disproving CH-CAND-05 | C | execution against a running database |
| **DEP-P09-06** | the pooled-connection blast radius of the report's shadow object | X4 | C | execution |
| **DEP-P09-07** | budget control implemented outside the two budget modules | research team | C | a system-wide sweep with a declared pattern |
| **DEP-P09-08** | a compensating upgrade script in other modules' migration directories | X2 | C | enumeration of those directories |
| **DEP-P09-09** | whether any deployed tenant view strips the node the runtime view-patch depends on | X4 | C | a sweep of the tenant custom view set |
| **DEP-P09-10** | whether an ordinary accountant role inherits write on the ledger row — decides the least-privilege answer for allocation edits | X4 | C | trace the group implication chain |
| ~~**DEP-P09-12**~~ | ~~whether any other event type allocates both legs symmetrically~~ | P09, on the P04 finding | **CLOSED** by the continuation sweep — **five** mechanisms found, three in core accounting | discharged; replaced by `SW-U-01`, `SW-U-02`, `SW-U-04` |
| **DEP-P09-13** | the full set of programmatic posting paths that bypass mandatory-axis validation | P04, reported to P09 | **B from P09's position** | P09 re-running P04's call-site enumeration |
| **DEP-P09-14** | incidence — does any real deployment hold an asset carrying an allocation? No deployment located does | P09 continuation | **HOLD — DATABASE EVIDENCE REQUIRED** | re-run the existing read-only asset trace with the allocation field added; near-zero cost, no write |
| **DEP-P09-15** | surface divergence observed rather than derived from source | P09 continuation | **HOLD — RUNTIME EVIDENCE REQUIRED** | read-only report execution against a deployment with posted depreciation |
| **DEP-P09-16** | reproduction of the defect in a sandbox | P09 continuation | **HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED** | explicit Boss authority; none exists and none is assumed |
| **DEP-P09-17** | whether work-centre hourly rates recover depreciation, which decides whether the masking interaction is real | P09 continuation, routed to P03 | **UNRESOLVED — EVIDENCE REQUIRED** | a costing-policy statement, not a code fact |
| **DEP-P09-18** | **the single cheapest decisive test in the continuation**: group the management records by (entry, plan column) over two-row entries and look for non-zero sums — the direct observable the zeroing hypothesis predicts is always zero | AAS-03 disproval challenge | **HOLD — DATABASE EVIDENCE REQUIRED** | one read-only query against any deployment holding such rows |
| **DEP-P09-19** | does any allocation-rule row carry an account prefix matching the depreciation-expense account but not the accumulated-depreciation account? | AAS-03 disproval challenge | **HOLD — DATABASE EVIDENCE REQUIRED** | if none, the per-row-derivation failure mode is unreachable in that install |
| **DEP-P09-20** | is any analytic plan marked mandatory in any deployment? | AAS-03 disproval challenge | **HOLD — DATABASE EVIDENCE REQUIRED** | if none, the obligation check never fires anywhere, in any path |
| **DEP-P09-21** | does any stored allocation have values summing to ≠ 100 at two decimals? | AAS-03 disproval challenge | **HOLD — DATABASE EVIDENCE REQUIRED** | direct evidence of the residue failure mode |
| **DEP-P09-22** | **`SW-U-01` is now known to be POPULATED**, not merely undeclared: the record-preparation method is overridden in the sales module. The remainder of that blind spot is still unsearched | AAS-03 disproval challenge | **C, known non-empty** | a sweep for overrides of the preparation and creation methods, not only for writes of the key |

## D. DECISION DEPENDENCIES — BOSS DETERMINATION REQUIRED

| ID | Determination | Why it cannot be inferred |
|---|---|---|
| **DEC-P09-01** | budget control policy: advisory, warn, approve or block (BC-01) | the reference pattern is advisory-only; many organisations run advisory budgets deliberately. This is a business choice, not a gap to be closed by imitation |
| **DEC-P09-02** | whether SMEsPlus builds any allocation-to-ledger mechanism at all (B-05) | P09 constrains the shape if one is built; it does not authorise building one |
| **DEC-P09-03** | how non-asset equipment cost is tracked (CO-03/CO-04/CO-05) | **there is no reference precedent** — the reference pattern offers no answer. This must be recorded as an original architectural decision |
| **DEC-P09-04** | whether commitment accounting is ledger-visible (BC-U-03, PD-03) | interacts with BC-02 |
| **DEC-P09-05** | whether a management aggregate may span companies within a tenant, and under what authorisation (B-09, MA-10) | a governance choice about who may see a group-level figure |
| **DEC-P09-06** | **whether the analytic ledger is a cost-attribution ledger or a balanced analytic subledger** (`AI-R-01`) | the reference pattern is **both and neither** — its writers allocate every row, its readers filter to profit-and-loss. Nothing in source states an intent. SMEsPlus must choose; the choice determines whether a net of zero is a defect or a correct non-figure |

## E. HELD — SCOPE OR STATUTORY EVIDENCE REQUIRED

| ID | Item | Route |
|---|---|---|
| HOLD-SC-01 | scope of the work centre as a cost object | PD-01 |
| HOLD-SC-02 | whether the deployed custom set contains the department dimension | DEP-P09-03 |
| HOLD-TH-01 | whether Thai statutory practice requires cost-centre or department segregation | **Accounting-Tax track.** No statutory claim is made anywhere in this package |
| HOLD-TH-02 | whether the tenant department extension is meant to satisfy such a practice | Accounting-Tax track |
| HOLD-TH-03 | a **statutory** Thai module differs between deployment copies | Accounting-Tax track, elevated |
| HOLD-EQ-01 | non-asset equipment cost design | DEC-P09-03 |
| HOLD-BC-01 | ledger-visible commitment | DEC-P09-04 |
| HOLD-AS-01 | whether a prior Asset package's costing-veto premise survives the P04 depreciation finding | **Boss.** P09 does not adjudicate between parallel evidence tracks |

## F. WHAT P09 DEPENDS ON NOTHING FOR

Stated explicitly, so the open list above is not read as "P09 delivered nothing":

- the boundary determination (`P09_FINANCIAL_VS_MANAGEMENT_BOUNDARY`), including the three-truth model, stands on its own evidence;
- the allocation, distribution, event and edge-case matrices are complete within their declared denominators;
- the scope-ownership determination is complete for every object P09 owns, conditional only on PD-06;
- five of six adversarial candidates are confirmed and one is disproved, none pending;
- the root-cause synthesis (`P09_AAS_PLUS` §2) requires no further evidence.

## G. TERMINAL STATE

**2 BLOCKING · 7 PEER OPEN + 1 PEER ACCEPTED · 18 EVIDENCE OPEN (1 CLOSED BY THE CONTINUATION; 5 ADDED BY THE DISPROVAL CHALLENGE, 4 OF THEM READ-ONLY DATABASE QUESTIONS) · 6 BOSS DETERMINATIONS · 9 HELD. NO DEPENDENCY CLOSED BY ASSUMPTION. NO GATE MOVED.**
