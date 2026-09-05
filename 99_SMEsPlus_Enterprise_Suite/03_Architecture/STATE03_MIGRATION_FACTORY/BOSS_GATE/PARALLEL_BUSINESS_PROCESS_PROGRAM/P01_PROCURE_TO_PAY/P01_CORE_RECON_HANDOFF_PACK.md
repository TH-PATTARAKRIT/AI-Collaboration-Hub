# P01 — CORE ACCOUNTING RECONCILIATION HANDOFF PACK

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Terminal state reached: **READY FOR CORE ACCOUNTING RECONCILIATION.**

That phrase means only that P01's evidence is in a state the Core Accounting reconciliation can
consume. It does **not** mean approved, pass, frozen, merged, or implementation-authorised, and
PMO's recommendation on the exit gate is `RECOMMEND HOLD` (`P01_PMO_REVIEW.md`).

---

## 1. WHAT CORE ACCOUNTING RECEIVES

### 1.1 Positions P01 asserts, and asks Core Accounting to accept or contest

| ID | Position |
|---|---|
| `HO-01` | The **vendor bill is the sole owner of the payable event.** No other path in the searched population creates a trade payable |
| `HO-02` | **Goods receipt owns the first valuation layer only.** Everything after belongs to Inventory |
| `HO-03` | P01 owns the **asset trigger** at bill posting; the Asset track owns the asset |
| `HO-04` | P01 **does not decide FX policy.** It inherits the Account track's rate-ownership and missing-rate ruling |
| `HO-05` | The **received-not-billed obligation has two representations** and needs exactly one owner |
| `HO-06` | **What proves ownership of a company-scoped financial effect** is a platform question, not a process one |

### 1.2 Facts Core Accounting must design around

1. **The bill is the only universal accounting event** — class **B**, bounded by the declared
   journal-entry creation-site population, which is a floor and not a total. Three of four
   purchase shapes produce no accounting effect at receipt. Cut-off and accrual completeness rest on the bill for most of the
   population.
2. **The receipt entry's accounting date is not the goods-movement date** — and in the later
   generation it is unconditionally the posting user's local "today", while the movement itself
   is in UTC.
3. **A soft period lock relocates a posting rather than refusing it.** Any period-close control
   that inspects entry dates is inspecting an artefact.
4. **Correction is by deletion, not reversal**, on reset-to-draft and cancel.
5. **FX difference arises at settlement**, not at bill or receipt.
6. **A missing rate silently resolves to an undated fallback, then to 1.0.**
7. **Four silent-failure paths** lose value or leave a bridge open with no error: no expense
   account → price difference not posted; clearing account not reconcilable → bridge never
   closes; no outstanding-payments account → payment produces no entry; withholding on partial
   payments compounds instead of netting.

### 1.3 The one that changes the basis of the conversation

**The deployed v19 databases have no goods-received clearing account and no valuation-layer
table.** The bridge described in 1.2 is the v18 bridge. Two of the three readable live
databases cannot run it. Core Accounting should not reconcile against a mechanism until
`DEP-P01-01` establishes which generation is the subject.

---

## 2. WHAT P01 NEEDS BACK

| Need | From | Blocking |
|---|---|---|
| Ruling on the target generation and the deployed custom copy (`DEP-P01-01`) | Boss | `CONTRA-P01-03`, `-07`, `-10`; most localization findings |
| Owner of the received-not-billed obligation (`DEP-P01-05`) | Core Accounting + Inventory | `CONTRA-P01-02` |
| Ownership of the withholding event — bill or payment (`DEP-P01-03`) | Core Accounting + Localization | `AE-P01-18` |
| Authoritative Thai statutory sources (`DEP-P01-04`) | Accounting-Tax track | 20 held statutory entries, `CONTRA-P01-10` |
| Confirmation that P01 inherits the FX ruling unchanged | Account Wave A | `HO-04` |
| Platform ruling on proving ownership of a company-scoped financial effect | SaaS / Platform Architecture | The tolerance-zero item |

---

## 3. THE SEVEN TESTS TO RUN FIRST

From `P01_EDGE_CASE_TEST_MATRIX.md`. Each loses value silently, overwrites history, or crosses
a company boundary without proving ownership. None has been executed.

1. Price difference where the item has **no expense account** — expect silent non-posting.
2. Clearing account **not flagged reconcilable** — expect an accumulating balance and no error.
3. **Cancel a posted bill** — expect derived journal items deleted, not reversed.
4. **Backdated receipt** — expect the entry date to differ from the movement date.
5. **Run the order-stage accrual twice** for the same orders and date — expect two accruals and
   no trace on the order.
6. **Approve an order whose vendor is a contact under another company's partner** — expect a
   document created in that company, as superuser, possibly auto-posted.
7. **Import bills without audit-log history** — expect layer matching to differ from the source
   system.

---

## 4. WHAT P01 EXPLICITLY DOES NOT HAND OVER

- No design. No implementation input. No schema proposal.
- No statement about Thai law.
- No runtime-verified behaviour.
- No claim about any source root outside the five declared, or any database outside the three
  readable ones.
- No coverage percentage — the function denominator is `UNBOUNDED / NOT YET ENUMERABLE`.

---

## 5. FOR PEER PROCESSES P02–P11

P01 is the **first** process session of this programme; no peer branch existed at session
start. Three things are worth carrying into every peer session:

1. **Take the transitive closure of the module dependency graph, not the direct set.** P01's
   first denominator missed landed costs and subcontract purchase, both explicitly required by
   its own directive (`ERR-P01-04`).
2. **Look for deployed database dumps before concluding that only source evidence exists.**
   They existed here, were outside the declared evidence base, and produced the session's
   strongest finding.
3. **Put "if any path in this brief is wrong, report it as a finding" in every brief.** In this
   session it caught two wrong field names in a brief the author wrote, and one missing
   population boundary.

P11 additionally receives `P01_SCOPE_OWNERSHIP_MATRIX.md` as the first input to cross-process
scope reconciliation. It contains **seven unresolved scope questions, not seven assertions**.

---

# ADDENDUM — TARGETED CROSS-PROCESS CLOSURE (2026-09-05)

The body above stands as lineage. This addendum is what P11 and Core Accounting should actually
work from.

## A.1 THE FIVE STATEMENTS P11 NEEDS

1. **No inventory value reaches the general ledger by any route in the deployed v19 systems.**
   Not at receipt — v19 **removed** that route by design and recognises inventory *at invoicing*.
   Not at invoicing — no valuation account resolves anywhere (category 0/37, company journal
   0/44, location 0/525, variation 0/544). Not periodically — closing is `manual` on 87 of 88
   company rows.
2. **A cross-tenant financial-effect path is reachable today.** Three unrelated corporate groups
   share one schema; every company partner is selectable from every company; the declared guard
   **cannot execute** because the deployed "create as" user is the superuser on 44 of 44
   companies. **Tolerance-zero.**
3. **Period locks re-date rather than refuse** anything that creates an accounting fact, and
   purchase-document dates are rewritten in draft with no lock involved on 19.6% of documents.
   **Cut-off testing on document dates is self-confirming.**
4. **Correction of a posted bill hard-deletes derived journal items**, preserving account and
   amount in an audit record that is itself deletable, incompletely populated, and **absent
   entirely in the v16 deployment**.
5. **The generation the source analysis targets — v18 — has no deployed representative in this
   estate.** The deployed comparison spans **v16 → v19**.

## A.2 WHAT P11 MUST NOT TAKE FROM P01

- **No runtime verification.** Nothing was executed.
- **No statutory conclusion.** All routed to P07.
- **No target-architecture decision**, and no Boss-level decision.
- **No claim about `D4`'s transactions** — only its module registry was read.

## A.3 ANSWERS TO PEERS

| Peer | Answer |
|---|---|
| **P05** | **P01 owns the vendor-advance event.** The module is installed in all four databases; its two copies behave differently; the advance defaults to an **expense** account |
| **P05** | WHT contradiction resolved **`BOTH PARTIAL`** — P05's rating stands, its justification was retired by P05 itself, and two of P01's supporting statements were wrong |
| **P04** | **Confirmed independently**: no capital-versus-expense classification exists on the purchase documents |
| **P02** | **Confirmed independently** from the purchase side: the valuation chart is unwired |
| **P03** | **A correction is owed**: P03's subcontract ownership premise cites the v18 construct, which **is gone in v19** |
| **P07** | WHT arithmetic (corrected), the PND conflict (deployed owner identified, neither mapping governing), and four decision surfaces for the form. **Statutory determination is P07's** |
| **P08** | Period-lock re-dating, draft date rewriting, correction by deletion, and that **no receipt reaches the ledger** — which changes what a period comparative means |
| **P09** | Bill-line analytic overwrite accepted as P01 territory |
| **P10** | The vendor-bill-line **service-period field does not exist**; and P01's half of the accrual boundary, which P10 reached independently |
| **P06** | No payment entry without an outstanding account; the four-entry-point problem corroborated |

## A.4 THE HIGHEST-VALUE REMAINING WORK, RANKED

| # | Work | Why |
|---|---|---|
| 1 | **Analyse `D4`'s transaction data** | It is the only database with three-way match, subcontracting and requisition installed, and the only one with a period lock set. Known-reachable, unread |
| 2 | **Boss ruling on the target generation** (`DEP-P01-01`) | Two candidate generations use **fundamentally different accounting models**, and one has no deployed representative |
| 3 | **Runtime execution of the seven priority cases** | Nothing is runtime-verified |
| 4 | **Close the tenant residue of `DEP-P01-06`** | Tenancy appears once, as a heading, in 384,836 bytes of prior expert output |
| 5 | **Locate the withholding code that deployments actually run** | It matches no copy in the declared path set |

## A.5 TERMINAL STATE

> **`P01 TARGETED CROSS-PROCESS CLOSURE — MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR
> SPECIFIC EXTERNAL / PEER / STATUTORY / BOSS DECISION.`**

Not `READY FOR CORE ACCOUNTING RECONCILIATION — COMPLETED`, because a tolerance-zero isolation
item is open and demonstrated live, and because a newly-reachable evidence source is unread.

This is **not** PASS, APPROVED, FROZEN, MERGED, or IMPLEMENTATION AUTHORIZED.
