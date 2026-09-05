# P01 — PEER EVIDENCE RECONCILIATION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Supersedes the previous round's statement that no peer package existed. **Ten peer branches are
now published** — `P02`…`P10` and the central reconciliation package `P11`. P01 does **not**
redo their work and does **not** adjudicate semantics they own.

Intake discipline applied: **verify before adopting.** A peer finding is admitted as P01
evidence only where this session re-derived it. Otherwise it is recorded as *peer-reported* and
routed.

---

## 1. WHAT PEERS SAY ABOUT P01, AND WHAT P01 DOES WITH IT

| From | Peer claim | P01 action | Classification |
|---|---|---|---|
| **P02** | The symmetry premise for the return/credit pattern is **withdrawn**: *the inbound interim account is defined but wired to nothing, so neither direction is chart-supported* | **Independently corroborated from the opposite direction.** P01 established from deployed configuration that the v19 valuation chart is entirely unwired — category valuation account 0/37, category valuation journal 0/37, location valuation account 0/525, account-level variation account 0/544 | **CONFIRMS P01** — convergent, independently derived |
| **P02** | A zero-rated input-tax **sign defect** is routed to P01 | Accepted as **peer-reported, not re-derived**. Routed to the tax expert stream and to P07 | **PEER OWNED — INTAKE OPEN** |
| **P02** | The reset-to-draft guard is wired **on the purchase side only** | Consistent with P01's own finding that order reset-to-draft has no server-side guard while cancel does. **Not the same statement** — P02 speaks of the guard's wiring, P01 of its absence. Both retained, neither merged | **EXTENDS P01** |
| **P04** | *"This purchase is a capital item" — P01 must own it; today nobody does.* The purchase order and receipt carry **no** classification field; the decision is derived downstream from product → category → account, and the capitalization flag sits on the **account** | **Re-derived and confirmed by this session.** No capital/asset classification field is declared in the purchase models or the movement model in either generation (class **B**, scope: those files). The flag lives on the ledger account, computed from the account type | **CONFIRMS AND SHARPENS `CONTRA-P01-04`** |
| **P04** | The link to the initiating business event is owned by **nobody** — the purchase-order reference lives on the journal item, never on the asset | Consistent with P01's own traceability finding that a payable cannot always be traced to its business event | **CONFIRMS P01** |
| **P04** | Cancelling the bill attempts to archive derived assets; resetting to draft **deletes** derived draft assets | Matches P01's evidence exactly | **CONFIRMS P01** |
| **P05** | *Advance to vendor — P01 owns it. P01 must state whether it does* | **Answered: P01 accepts ownership of the vendor-advance event.** New evidence this round: the project's custom vendor-advance module is **installed in all three readable deployments** | **ANSWERED — see `P01_P05_VENDOR_ADVANCE_RECONCILIATION.md`** |
| **P05** | WHT overlap is **"Low — single implementation"** | **Contested by P01 evidence.** Full reconciliation delegated to an independent expert | **CONTRADICTS P01 — see `P01_P05_WHT_CROSS_PROCESS_CONTRADICTION.md`** |
| **P05** | An expense line can name a vendor and post to vendor-facing accounts **without any purchase document** | Accepted as peer-reported. It is a second, non-purchase route to vendor AP and therefore a **double-liability surface** P01 must record | **EXTENDS P01 — new ownership risk** |
| **P06** | **Payment intent has four entry points and no single author** — `CONTESTED` | Consistent with P01's finding that a payment produces no entry at all without an outstanding-payments account. Both describe an under-owned payment event | **EXTENDS P01** |
| **P06** | The invoice's payment status is authored by the invoice process but **mutated by P06** — two writers, one fact | Accepted as peer-reported; a direct ownership conflict on a P01 artefact | **P11 RECONCILIATION REQUIRED** |
| **P06** | Advance or deposit received before any obligation exists is an **unowned window** | Intersects P01's vendor-advance ownership answer | **P11 RECONCILIATION REQUIRED** |
| **P07** | **Vendor legal personality must be a typed attribute, not a boolean "is a company" flag** — `BLOCKING for P07` | **Directly decisive for P01's PND finding.** Both shipped certificate copies key their form choice off exactly that boolean. P07's objection means the two copies disagree about a mapping whose *input* is the wrong instrument in the first place | **EXTENDS AND DEEPENS `CONTRA-P01-10`** |
| **P07** | The withholding fact is created at **payment (P06)** but reported from a **P01 artefact (the bill line)** — two processes hold a claim on one tax fact | This is the answer forming to P01's own open question `DEP-P01-03` (bill or payment). **P01 does not close it unilaterally** | **P11 / P07 RECONCILIATION REQUIRED** |
| **P08** | Whether intercompany settlement within one tenant is in scope, and which company owns the matching record — `PEER DEPENDENCY OPEN`, P01/P02 boundary | Intersects P01's tolerance-zero cross-company item, now known to be **installed and live in both v19 deployments** | **P11 RECONCILIATION REQUIRED — escalated** |
| **P09** | The bill line's analytic allocation is **overwritten by an assignment rule with no warning and no audit entry** — a P09 finding inside P01 territory, handed over not adjudicated | Accepted as **peer-reported, not re-derived**. Recorded as a P01-territory defect owned jointly | **EXTENDS P01** |
| **P10** | Needs the canonical definition of *"the period a purchased service covers"* and whether it is required on a vendor bill line | **P01 cannot supply it**: no such field was found on the bill line. Recorded as a P01 gap, not a P10 one | **PEER DEPENDENCY OPEN — P01 owes P10** |
| **P10** | The **accrual boundary cannot be assigned by evidence**; P10 offers two designs — P10 owns the accrual event with P01/P02 owning measurement, or P01/P02 own accrual entirely | This is precisely P01's `CONTRA-P01-02` (two owners for the received-not-billed obligation) seen from the other side. **Two processes independently reached the same unassignable boundary** | **P11 RECONCILIATION REQUIRED — jointly escalated** |
| **P11** | `DEP-06` price-difference account scope, P01 ↔ Inventory — **contradiction, open** | P01 supplies its price-difference evidence; does not decide | **ROUTED** |
| **P11** | `DEP-07` landed cost, P01 ↔ Inventory — **joint decision, open, audit VETO retained** | P01 now supplies a landed-cost trace and the fact that landed cost is **installed in all three deployments** | **ROUTED — P01 input now available** |
| **P11** | `DEP-15` prior-period attribution — **no mechanism exists in the reference at all** | Corroborated by P01's period-lock evidence: the reference re-dates rather than attributing | **CONFIRMS P11** |
| **P11** | `DEP-23` — P01–P10 publication, `PEER DEPENDENCY OPEN × 10` | **P01's package is complete but its branch is unpushed.** This is P01's contribution to that blocker and it is a permission issue, not a research one | **P01 ACTION REQUIRED — publication blocked** |

---

## 2. WHERE P01 CORRECTS A PEER'S RECORD

Per intake discipline, a peer's record is corrected only where their package will otherwise
carry an error into P11.

| Peer | What their package records | What P01 evidence shows | Requested correction |
|---|---|---|---|
| **P06** | *"A remote enumeration on 2026-09-04 returned 10 `research/*` heads, none of them `research/account-p01…p05-*` … every ownership assignment naming P01–P05 is made against the Boss prompt, not a published sibling package."* | P02, P03, P04 and P05 **are now published**; P01 is complete but **unpushed**. P06 explicitly stated that any conflict discovered when they publish supersedes its file | **P06's caveat is now live for four of the five processes it named.** P06's P01-facing assignments should be re-read against P01's published package once P01's branch is pushed |
| **P05** | WHT overlap rated **Low** on a single-implementation premise | P01 evidence indicates more than one mechanism, and the arithmetic defect sits in the one implementation that **is installed everywhere** | Rating should be revisited in reconciliation. **P01 does not overrule P05** |

---

## 3. WHAT P01 OWES PEERS

| To | Item |
|---|---|
| **P02** | P01's vendor-side answer on the return/credit mirror, and confirmation that P01 independently reached the unwired-chart conclusion |
| **P03** | Landed-cost and subcontract evidence, with the boundary marked and **not** decided |
| **P05** | The vendor-advance ownership answer (given) and the WHT contradiction (raised) |
| **P06** | P01's payment-side evidence: no entry without an outstanding account; four-entry-point payment intent corroborated |
| **P07** | WHT arithmetic evidence, the PND mapping contradiction, and the certificate population — **statutory determination is P07's, not P01's** |
| **P08** | Period-lock re-dating, posted-bill correction by deletion, and the fact that in the v19 deployments **no receipt ever reaches the ledger** — which changes what a period comparative means |
| **P09** | Confirmation that the bill-line analytic overwrite sits in P01 territory |
| **P10** | The vendor-bill-line service-period gap, and P01's half of the accrual-boundary question |
| **P11** | Everything above, plus P01's scope matrix and its unresolved scope questions |

---

## 4. LIMITS OF THIS INTAKE

- P01 read peers' **cross-process and ownership** files. It did **not** read their full packages
  — **class C** for everything else they contain.
- Peer findings not re-derived by this session are labelled *peer-reported* and are **not** P01
  evidence.
- No peer conclusion was adopted merely because it agrees with P01. The two that agree most
  strongly — P02 on the unwired chart and P04 on capital classification — were each
  independently re-derived here before being recorded as confirming.
