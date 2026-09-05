# P06_CORE_RECON_HANDOFF_PACK.md

**Session:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001 · **Process:** P06 Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE — **must not be transcribed into any Layer 1 reference package**
**Recipient:** Core Accounting Reconciliation
**Status:** **READY FOR CORE ACCOUNTING RECONCILIATION**, as evidence for a decision, under AASP-VETO-01.

**Read this before anything else:** this pack is admissible as evidence, **not** as a specification. The AAS+ reliance veto and its three lift conditions apply. Cite the registers' correction sections, never their headline tables.

---

## 1. The four things Core Reconciliation must know

**H-01 — The four states P06 was asked to determine independently are not independent, and one of them does not exist.**
Payment state and reconciliation state are mutually computed; accounting posting state is driven by the payment record rather than the reverse; and **there is no field whose meaning is "the bank confirmed this."** The nearest proxy is asserted `True` by configuration alone in two of its three branches.
→ Core Reconciliation cannot read a bank-confirmation fact from this model. It must be authored.

**H-02 — No custom module in this estate has ever touched the bank side.**
All twelve P06-scope custom modules return NOT FOUND for `account.bank.statement`. Every customisation works on payments. The bank-event and reconciliation halves run on unmodified reference behaviour — which is exactly where all seven confirmed defects sit.

**H-03 — The identity system fails open at every layer, in the same direction.**
Four of seven ingestion doors attach no identity; three enforcement points treat a null identity as "not a duplicate"; the provider reference is unconstrained, never searched, and overwritten by the last callback received.

**H-04 — Unsettled money has a home but no clock.**
Suspense and transit balances are `asset_current` and therefore structurally invisible to the only ageing report that exists.

---

## 2. Confirmed defects Core Reconciliation inherits

| ID | Defect | Precondition to reach it |
|---|---|---|
| A1 | Duplicate bank transactions via CSV, QIF, OCR, manual entry, `copy()`, or a second journal | **import a file twice** — the lowest bar in the set |
| A3 | Duplicate payment against the same invoice; detection is advisory at every call site, and one call site queries a state value absent from the v18 selection | register a payment twice |
| A4b | An unowned bank account (`company_id = False`) admitted into every company by three separate guards | a partner with no company |
| A4c | A payment token visible to a wider scope than its own transactions | a company hierarchy |
| A5 | Resetting or reversing a document silently destroys the bank reconciliation, via two independent paths, neither aware of the statement line | reset any matched invoice |
| A6 | **Reconciling and un-reconciling are outside the entire period-close regime** | a locked period and unreconcile rights |
| A7 | Statement-line deletion bypasses the audit trail via `force_delete`, and enabling the audit trail converts a hard refusal into a silent un-reconcile | delete rights |

**AAS+ escalation on A6, carried forward deliberately:** the sharper reading is not "corrections after close are possible" but **"a signed-off bank reconciliation is not a durable fact."** Core Reconciliation should treat that as the working assumption until proven otherwise.

---

## 3. What Core Reconciliation must design, not inherit

| # | Requirement | Source |
|---|---|---|
| 1 | Four separately-written states, each with a recorded writer and timestamp; none computed from another | PSM-R-01 |
| 2 | A first-class **bank confirmation** fact, settable only by an ingested bank event, never by configuration | PSM-R-03 |
| 3 | A `paid` state that records **why** it became paid | PSM-R-02 |
| 4 | An explicit transition table; `rejected` and `canceled` with distinct recorded causes; an irrevocable-instruction state | SSM-R-01/03/05 |
| 5 | Settlement never asserted while a ledger residual stands | SSM-R-02 |
| 6 | A **company-scoped** bank-event identity, enforced in schema, covering every ingestion door | SCOPE-R-06, BER |
| 7 | Reconciliation as a **record**, not a rewrite; the pre-match state must survive | RM-R-01 |
| 8 | A persisted reconciliation session: who, when, candidates offered, candidates rejected | RM-R-02 |
| 9 | Non-invertible tolerance semantics, with approval on the parameter | RM-R-07/08 |
| 10 | Un-reconciling as an authorised, logged, lock-date-aware act on **both** sides | RM-R-09, RM-R-14 |
| 11 | First-class bank charge, bank interest and provider commission with owned accounts; a fee that cannot be determined must block, not post zero | FFI-R-01/02 |
| 12 | Net settlement decomposable into gross + fee against one bank credit | FFI-R-03 |
| 13 | Ageing over every unsettled-money account, suspense and transit included | EGL-F-06, EC-F-01 |
| 14 | Internal transfer as a **paired object** proving both legs and a nil transit balance | PSM-R-07, EC-F-09 |
| 15 | A tenant-scoped carrier for intercompany settlement, owning neither company's effect but proving both | SCOPE-R-08 |
| 16 | Post-dated cheque and returned-item handling — **absent from v18, present in v14** | EC-F-13/14 |
| 17 | A cash session with custodian and blind count | EC-F-11 |
| 18 | No conversion may fall back to parity; a missing rate denies | FX-R-02 |
| 19 | Accounting created in the same transaction as confirmation, or a monitored durable queue | PPT-R-01 |
| 20 | Availability may never exceed ownership | SCOPE-R-05 |

**Carry forward one positive pattern.** `scgl_advance_expense_request` is the only object in the entire evidence set with a first-class model, an approval state machine, computed exposure fields and explicit clearing wizards. **Use its shape for every unsettled-money object** — money-on-account, cheques-in-flight, transit, unidentified receipts.

---

## 4. What Core Reconciliation must NOT assume from this pack

- That any Class-A negative is final — none was independently re-searched (`P06-B-40`).
- That `P06-B-22` (no write-off approval control) holds at full strength — **it is Class B**; the custom approval modules were not searched.
- That the sibling-branch reconciliation vector (A4a) is a defect — **it is HOLD**, pending `P06-B-27`.
- That any cross-process ownership assignment is agreed — **no sibling package was read**.
- That any runtime claim is corroborated — **no database was queried**.
- That any deployment statement can be made — four byte-identical custom copies exist.
- That any Thai statutory position has been taken — **all HOLD**.

---

## 5. Three actions before this pack can be relied on

Narrow, and in order:

1. **Answer `P06-B-27`.** Does `root_id` denote one legal entity or several? **One query. It closes three blockers** (A4a, RM-R-10, SCOPE-R-02) and is the highest-leverage action available.
2. **Run the second negative-claim search** with independently-worded patterns over every Class-A negative (`P06-B-40`), and include the custom approval modules (`P06-OQ-81`).
3. **Read the P01, P02 and P05 packages** and reconcile the twenty cross-boundary facts.

Then AASP-VETO-01 can be lifted. AASP-VETO-02 additionally requires a Boss decision on the seven confirmed defects and the statutory HOLDs.

---

## 6. Open items by class

| Class | Count | Meaning |
|---|---|---|
| C — not yet searched | 18 | a search that was not run |
| D — unknown | 16 | needs runtime, data, or an external contract |
| HOLD / statutory | 8 | routed to Accounting-Tax; not decidable here |

**No Class B, C or D item has been restated as Class A anywhere in this package.** One item moved the other way at challenge.

---

## 7. Register index

| File | Contains |
|---|---|
| `01` Payment State Model | the canonical-question answer; 32 findings |
| `02` Bank Event Register | 7 ingestion doors; 2 identities; 6 silent-drop behaviours |
| `03` Settlement State Matrix | 18 of 60 cells characterised; 13 permitted contradictions |
| `04` Reconciliation Model | the delete-and-rebuild mechanism; tolerance inversion; lock-date asymmetry |
| `05` Event-to-GL Matrix | 31 event→entry rows; 5 account-determination chains |
| `06` FX/Fee/Interest Matrix | 4 parity fallbacks; zero fee/interest concepts |
| `07` Duplicate/Match Attack | 8 attacks; 7 confirmed |
| `08` Payment Provider Trace | accounting outside the webhook; unconstrained provider reference |
| `09` Cross-Process Ownership | 20 boundary facts; 8 contested, 4 unowned |
| `10` Edge Case Matrix | 10 cases; 2 adequately modelled |
| `11` Contradiction Register | 28 Type I · 7 Type II · 8 Type III |
| `12` Source Link Register | **the controlling denominator document** |
| `13` Evidence Manifest | SHA-256 per file |
| `14` Revision Log | 4 recorded author errors; the CORR1 application |
| `15` AAS-03 Challenge | 18 challenges; 6 amendments; 1 downgrade |
| `16` AAS+ | 7 findings; 2 vetoes; 6 dissents |
| `17` PMO | compliance; 42 blockers; RECOMMEND HOLD |
| `19` Scope Ownership Matrix | 30 objects; 8 revalidations *(CORR1)* |
| `20` Custom Module Delta | 4-copy denominator; the v14→v18 treasury regression |

---

## 8. Terminal

**READY FOR CORE ACCOUNTING RECONCILIATION.**

Handed over as evidence for a decision, under AASP-VETO-01, with 42 blockers and 42 open items enumerated and owned. *(SUPERSEDED BY APPENDIX B: the open-item figure of 42 was a unit-conflation error — see `39_` REV-E-05. Final executed figures are in B.8.)* **This is not a PASS, not a freeze, not a merge, and not an implementation authorisation.** No such declaration is made or implied anywhere in this package.

---

# End

---

# APPENDIX B — TARGETED CONTINUATION UPDATE (2026-09-05)

Produced by `[SMEPLUS-26-09-04-ACC-P06-B2R-TARGETED-EVIDENCE-CLOSURE-001]`. The body above stands; this appendix records what changed.

## B.1 The headline has changed

The body of this pack leads with *"seven confirmed defects"*. **After this continuation the honest headline is different, and it should lead:**

> **The bank half of P06 runs on unmodified reference behaviour — and a custom module present in all four source copies can delete the bank statements, payments, journal entries, reconciliations and chatter with unconditional SQL, no server-side authorisation, and then rewind the document sequences to 1.**

`P06-B-50`. It bypasses the ORM entirely, so **every control that attacks A7 and A8 analysed is inapplicable on that path.** No settlement or reconciliation design holds while that module is installable. Whether it is installed on the target is unknown — see B.4.

## B.2 What closed

| Item | Disposition |
|---|---|
| **`P06-B-27`** — does `root_id` denote one legal entity? | **CLOSED — SOURCE EVIDENCE VERIFIED.** Neither reading was right: `root_id` is a **fiscal and currency hierarchy**. The delegated set is five fields and **excludes `vat` and `company_registry`**, so branches may be legally distinct. **P11 may strike this from its decision `D-3`; no UAT query is needed.** |
| Attack **A4a** | HOLD → **CONFIRMED DEFECT.** The guard names the company boundary and tests a fiscal one; it cannot enforce what it claims, for any deployment. Independently corroborated by P02 `SF-06`. |
| **`P06-B-28`** token scope | **CLOSED**, severity **downgraded HIGH → MEDIUM** on adversarial test |
| **`P06-B-40`** unverified negatives | **CLOSED** — both principal Class-A negatives survived independently-worded re-searches |
| **`P06-B-03`** peers unread | **CLOSED** — 7 of 9 read; P01 and P08 re-raised as `B-54` |
| `OQ-21`, `OQ-71`, `OQ-81`, `OQ-90` | **CLOSED** |

## B.3 What Core Reconciliation must now also know

| # | Finding |
|---|---|
| B-1 | **P06 is a producer, not a terminal consumer.** It emits three accounting events by the act of matching — exchange difference, its reversal, cash-basis tax — and owns none of them. Adopted from P11. |
| B-2 | **Lock dates inherit up the hierarchy, strictest ancestor wins**, with elevated privilege and including archived companies (P04 `P04-B-43`). Since branches may be legally distinct, **one company's close can lock another's books.** |
| B-3 | **RELOCATE is core behaviour, not a reconciliation quirk.** P04 establishes it lives in the generic posting routine, so it reaches any P06 event that posts. |
| B-4 | **A globally-unique outbound tracker (`iso20022_uetr`) has no inbound counterpart**, and CAMT parses the inbound end-to-end id into a free-text note. The round trip is broken at both ends. |
| B-5 | **There is no import-batch object.** A re-import cannot be identified, audited or reversed as a unit. |
| B-6 | **An eighth settlement door** moves cash through a bank journal with no payment object, invisible to matching (inherited from P05 `SR-04`). |
| B-7 | **The custom approval estate does not cover settlement at all** — 3 modules, 46 files, 0 hits on any settlement object. `P06-B-22` restored to Class A. |
| B-8 | **The evidence base is a filtered distribution** — 791 addons, 2 localisation packs, both Thai. Every tree-scope negative inherits that boundary (`P06-B-55`, `AASP-VETO-03`). |
| B-9 | **The only deployment evidence available is Odoo 19**, while P06 researched v18 (`P06-B-44`). |

## B.4 Two things that must be resolved before anything is built

1. **Confirm the target generation.** One `ir.module.module` export. If the target has moved to 19, a material fraction of this package is scoped to a superseded line.
2. **Determine whether `om_data_remove` is installed on the target.** Same export answers it. If it is, no control in this package's requirement list is enforceable.

## B.5 One contradiction for P11 to adjudicate

**`P06-XC-01`.** P02 publishes `P02-F-43` as `FACT VERIFIED` — *"the reference process **does** keep these separate, and does it well"* — which is the opposite of P06 headline (i). **It is registered in no contradiction register anywhere**, because P11 ingested P02 and P06 in separate deltas and did not cross-read them.
**P06's proposed reconciliation, offered not imposed:** the separation exists **only in the outstanding-account configuration** and collapses at creation in the direct-to-bank configuration. It is a **configuration-dependent property, not a system property**, and a design may not rely on it without mandating the configuration. P02's own `P02-F-44` supplies the counter-evidence.

## B.6 Peer questions answered

- **P10 `X-08`** — bank-side prepayments and interest accruals: **answered and closable.** Resolves by absence; no bank-interest object exists for either process. P06 recommends the boundary at accrual (P10) versus receipt (P06).
- **P09's class-B claim** about P06's widget: **shape confirmed** (the widget clears and rebuilds every line), analytic specifics not traced. **Class B is correct and should stay.**
- **P07's three BLOCKING dependencies** — payment date, allocation, reversal linkage: **all three accepted, and all three reported defective in the reference.**

## B.7 Veto status

| Veto | Status |
|---|---|
| **AASP-VETO-01** reliance | **PARTIALLY RESOLVED.** The company-boundary position is released for reliance. Five single-pass tree-scope negatives and all P01-dependent items remain vetoed. |
| **AASP-VETO-02** implementation | **REMAINS, on new grounds** — the original ground is discharged; the generation gap, `B-50`, and 26 undecided design items now carry it. |
| **AASP-VETO-03** | **NEW** — P11 must record the filtered-evidence-base boundary alongside each P06 negative, or confirm peers used the same build. |

## B.8 Terminal

**READY FOR CORE ACCOUNTING RECONCILIATION — TARGETED BLOCKER CLOSURE COMPLETED.**

Handed over as **evidence for a decision**, under three vetoes, with **55 blockers** (7 closed, 48 open) and **44 open items** (4 closed, 40 open) — enumerated, unit-declared, and counted by a command executed after the final file was written. **Not a PASS, not a freeze, not a merge, not an implementation authorisation.**
