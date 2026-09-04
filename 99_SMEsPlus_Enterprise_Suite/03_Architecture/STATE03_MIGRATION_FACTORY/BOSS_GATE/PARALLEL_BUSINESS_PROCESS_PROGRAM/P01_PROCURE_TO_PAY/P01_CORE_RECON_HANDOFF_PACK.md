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
