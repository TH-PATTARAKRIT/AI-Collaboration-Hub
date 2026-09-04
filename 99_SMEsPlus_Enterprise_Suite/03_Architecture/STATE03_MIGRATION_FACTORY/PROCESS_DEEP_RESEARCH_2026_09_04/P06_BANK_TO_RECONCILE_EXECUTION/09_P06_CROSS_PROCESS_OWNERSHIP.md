# P06_CROSS_PROCESS_OWNERSHIP.md

**Session ID:** SMEPLUS-26-09-04-ACC-P06-B2R-REV2-001
**Process:** P06 — Bank-to-Reconcile
**Branch:** research/account-p06-bank-to-reconcile-2026-09-04-001 (base `88f52cd`)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Governing invariant:** ONE FACT → ONE OWNER → ONE ACCOUNTING EFFECT

---

## 1. Why this file exists

P06 is a *terminal* process: it consumes facts produced by other processes and converts them into a bank-confirmed, reconciled position. Every fact it consumes is authored somewhere else. If two processes each believe they own the same fact, the system produces either a double accounting effect or an orphaned one. This file assigns a single owner to each fact that crosses the P06 boundary, and — where the evidence does not support a single owner — records the ambiguity as a blocker rather than resolving it by assumption.

---

## 2. The process taxonomy is prompt-resident, not repository-resident

**CPO-F-01 — The P0x process identifiers do not exist in the canonical repository.**
- Search: `grep -rn -iE "bank.to.reconcile|\bP06\b" --include="*.md" --include="*.yaml"` over the whole checkout at base commit `88f52cd`. **0 hits.**
- The repository's own process register, `99_SMEsPlus_Enterprise_Suite/END_TO_END_BUSINESS_PROCESS_MATRIX.md` (v0.1, "Draft Baseline", updated 2026-07-06), enumerates exactly ten processes: `E2E-001` Lead to Customer, `E2E-002` Quote to Sales Order, `E2E-003` Sales Order to Delivery, `E2E-004` Sales to Invoice, `E2E-005` Purchase Request to Purchase Order, `E2E-006` Purchase Order to Receiving, `E2E-007` Purchase to Vendor Bill, `E2E-008` Stock Movement to Stock Balance, `E2E-009` Approval Request to Approval Result, `E2E-010` Report Request to Report Output.
- **DENOMINATOR:** POPULATION: rows of the Process Matrix table in that file. PATTERN: full table read. PATH SET: that one file at `88f52cd`. UNIT: process row. Count = 10.
- **CPO-F-01a — There is no cash, bank, payment, settlement or reconciliation process anywhere in that matrix.** The chain in that document terminates at *invoice* on both the sell side (`E2E-004`) and the buy side (`E2E-007`). **Class A within the declared scope of that file at that commit.**
- **Consequence:** P06 has **no receiving specification** in the canonical repository. Its outputs cannot be traced into `TRACEABILITY_MATRIX.md` without first creating the process row. **This is a repository gap, not a P06 finding about the reference ERP,** and it is raised as blocker `P06-B-01`.

**CPO-F-02 — No Jira work item carries P06.**
- `project = ERPPLUS` population 146; summary-pattern match on `bank|payment|reconcil|treasury|settlement|cash` returns **0**. Class A within that scope (project ERPPLUS, `summary` field, 2026-09-04). Class B for descriptions, comments and other projects.
- **Consequence:** the directive "GitHub/Jira evidence required" is satisfiable for GitHub (this branch) but **not** for Jira, because no issue exists to attach to. Raised as blocker `P06-B-02`. This session does **not** create a Jira issue — creation is an outward-facing act reserved to the Boss.

---

## 3. Sibling process packages are not yet available

**CPO-F-03.** Working clones for P01 (Procure-to-Pay), P02 (Order-to-Cash), P03 (Make-to-Cost), P04 (Acquire-to-Retire) and P05 (Expense-to-Pay) exist on this workstation, each branched from the same base `88f52cd`. A remote enumeration on 2026-09-04 (`git ls-remote --heads origin "refs/heads/research/*"`) returned **10** `research/*` heads, **none** of them `research/account-p01…p05-*`.
- **DENOMINATOR:** POPULATION: remote heads under `refs/heads/research/`. UNIT: ref. Count of P01–P05 matches = 0.
- **Class A at that instant only.** These sessions are running in parallel and may publish at any time.
- **Consequence:** every ownership assignment in §4 below that names P01–P05 is made **against the process definition in the Boss prompt, not against a published sibling package.** No sibling package was read. Any conflict discovered when they publish supersedes this file. Raised as blocker `P06-B-03`.
- **This is the single largest reliance limitation on this package.** A cross-process ownership matrix built without reading the counterparties is a *proposal*, not a reconciliation.

---

## 4. Fact ownership across the P06 boundary

Legend for **Owner status**: `ASSIGNED` = evidence supports exactly one owner · `CONTESTED` = evidence shows two or more candidate owners · `UNOWNED` = no owner found in searched scope · `HOLD` = owner cannot be assigned without a Boss or statutory decision.

| # | Fact crossing the P06 boundary | Upstream author (proposed) | P06 role | Owner status | Basis / blocker |
|---|---|---|---|---|---|
| F-01 | Customer receivable open item and its residual | P02 Order-to-Cash | Consumer; settles it | ASSIGNED | Residual is a property of the ledger line, single-authored at invoice posting. |
| F-02 | Vendor payable open item and its residual | P01 Procure-to-Pay | Consumer; settles it | ASSIGNED | As F-01. |
| F-03 | Employee reimbursement / advance obligation | P05 Expense-to-Pay | Consumer; settles it | **CONTESTED** | The employee settlement path can create a payment directly, and a petty-cash custom module also participates. Two candidate authors. See Edge Case Matrix E-EMP. |
| F-04 | **Payment intent** (that a payment *should* happen, for how much, to whom, on what date) | P01 / P02 / P05 | Executor | **CONTESTED** | Payment can be initiated from the invoice (register-payment path), from a standalone payment record, from a batch, and from an online provider callback. Four entry points, no single author. Blocker `P06-B-04`. |
| F-05 | **Payment state** (`draft / in_process / paid / canceled / rejected`) | **P06** | Author | ASSIGNED (with defect) | See Payment State Model: the state is *computed* partly from downstream reconciliation, so P06 authors it but does not solely determine it. |
| F-06 | **Accounting posting state** of the payment journal entry | Core Accounting (P-CORE) | Consumer | **CONTESTED** | The payment record and its journal entry are synchronised in both directions; neither is unambiguously the author. Blocker `P06-B-05`. |
| F-07 | **Bank confirmation state** (the bank says the money moved) | External bank / import channel | Author = external | **UNOWNED inside the system** | The system has no field whose meaning is "the bank confirmed this". The nearest proxy is a boolean that can be asserted true by configuration alone. See Payment State Model finding PSM-F-04. Blocker `P06-B-06`. |
| F-08 | **Reconciliation state** (statement line matched) | **P06** | Author | ASSIGNED (with defect) | Computed, and its terminal branch defaults to "reconciled". See Reconciliation Model. |
| F-09 | Invoice `payment_state` shown to the business | P01 / P02 | **P06 mutates it** | **CONTESTED** | The invoice's payment status is authored by the invoice process but *changed* by reconciliation events owned by P06. Two writers, one fact. Blocker `P06-B-07`. |
| F-10 | Foreign-exchange rate applied at settlement | P-CORE (rate table) vs P06 (statement-line rate) | Both | **CONTESTED** | A statement line carries its own rate, which can differ from the rate table. Carried forward from the Account Wave A FX findings. Blocker `P06-B-08`. |
| F-11 | Realised FX gain/loss amount and account | P-CORE | P06 triggers it | ASSIGNED | The account determination is a company/journal configuration owned by Core Accounting; P06 only triggers the event. |
| F-12 | Bank charges and bank interest | **UNOWNED** | Would be consumer | **UNOWNED** | No dedicated fee/interest concept was found in the searched scope; the mechanism is a generic write-off line. See FX/Fee/Interest Matrix. |
| F-13 | Withholding tax deducted at payment | Accounting-Tax track (Thai statutory) | P06 executes the deduction | **HOLD** | Thai WHT is statutory. Marked **HOLD / EVIDENCE REQUIRED** and routed to the Accounting-Tax track. Custom WHT modules participate in the payment amount; their statutory correctness is explicitly *not* adjudicated here. |
| F-14 | Early-payment discount taken at settlement | P02 (terms) | P06 applies it | ASSIGNED | Terms are authored on the invoice; P06 applies them at settlement. |
| F-15 | Cash/bank GL balance | P-CORE | P06 moves it | ASSIGNED | |
| F-16 | **Which physical bank account a GL balance belongs to** | — | — | **UNOWNED** | See CPO-F-04 below. Blocker `P06-B-09`. |
| F-17 | Period lock / close status | P-CORE (close process) | P06 must respect it | **CONTESTED** | Whether the un-reconcile path respects lock dates is a live question routed to the Duplicate/Match Attack file. |
| F-18 | Bank statement line identity (what makes two imported rows "the same transaction") | Import channel | P06 depends on it | **CONTESTED** | Different import channels build identity differently; a manually keyed line has no channel identity at all. See Bank Event Register. Blocker `P06-B-10`. |
| F-19 | Intercompany settlement between two group companies | P-CORE / intercompany rules | P06 executes both legs | **UNOWNED for payments** | Reported in the Edge Case Matrix with declared scope. |
| F-20 | Advance / deposit received before any invoice exists | P02 (customer) / P01 (vendor) | P06 receives the money first | **CONTESTED** | Money arrives before the obligation exists, so the receiving process is P06 while the fact's author is upstream. Classic unowned-window. |

---

## 5. The bank-account identity gap

**CPO-F-04 — Twelve physical bank accounts collapse onto two general-ledger accounts.**
- Evidence: `~/Downloads/OCC/OCC_JOURNAL_BANK_RUNTIME_VERIFIED_C1_C2_v2.3_L99.99.csv`, 12 rows, `Runtime Status = VERIFIED_LIVE_UAT` on every row.
- Company C1 carries 6 bank journals (codes `SCB1`, `BKK0`, `BKK1`, `KAS0`, `KAS1`, `KAS2`); company C2 carries 6 (`KTB1`, `KTB2`, `BKK1`, `BKK3`, `KAS1`, `SIC1`).
- Every one of the 12 maps to one of exactly **two** target GL accounts: a current-account code and a savings-account code.
- **DENOMINATOR:** POPULATION: the 12 rows of that extract. PATTERN: full read of the `Target GL Account` column. PATH SET: that one file. UNIT: bank journal. Distinct target GL accounts = 2.
- **Consequences for P06, in order of severity:**
  1. **The general ledger cannot answer "what is the balance of bank account X".** Only the journal can. Any bank reconciliation that reasons from the GL account balance is reconciling an aggregate of up to six real bank accounts against one bank's statement.
  2. **Reconciliation must be journal-scoped, not account-scoped**, and every P06 control must state which scope it operates in.
  3. **Two companies reuse the same journal codes** (`BKK1` and `KAS1` appear in both C1 and C2). Journal *code* is therefore not a unique key across the tenant. Any matching rule, import mapping or report filter keyed on journal code alone is ambiguous across companies. This directly feeds the cross-company attack in the Duplicate/Match Attack file.
  4. The extract's own `Source Basis` column records that for 2 of the 12 rows the legacy account was **not present** in the uploaded chart-of-accounts extract (`KAS1`/C1 and `KTB1`/C2). The mapping for those two rows rests on the journal extract alone.
- **Class A within the declared scope of that extract.** It is **not** a claim about the complete live system — the extract is not certified as a full census.

---

## 6. Process handoff map

```
 P01 Procure-to-Pay ──┐
 P02 Order-to-Cash  ──┤
 P05 Expense-to-Pay ──┼──> [open item + residual] ──> P06 Bank-to-Reconcile ──> [bank-confirmed position]
 P03 Make-to-Cost   ──┤                                        │
 P04 Acquire-to-Retire┘                                        ├──> P-CORE (GL, FX, close)
                                                               └──> Reporting (bank recon report, cash flow)
```

Every arrow into P06 is an **open item with a residual**. Every arrow out is either a **GL effect** or a **residual reduction**. P06 owns nothing else. Where §4 records CONTESTED, the arrow is drawn but its author is disputed.

---

## 7. Blockers raised by this file

| ID | Blocker | Owner of the decision |
|---|---|---|
| P06-B-01 | The canonical process matrix has no bank/payment/reconciliation process; P06 has no receiving specification. | Boss |
| P06-B-02 | No Jira work item exists for P06; the Jira evidence requirement cannot be met by this session. | Boss |
| P06-B-03 | P01–P05 packages were unpublished at fetch time; all cross-process assignments are proposals, unreconciled. | Boss / PMO |
| P06-B-04 | Payment intent has four entry points and no single author. | Architecture |
| P06-B-05 | Payment record and its journal entry are mutually synchronised; posting-state authorship is undetermined. | Architecture |
| P06-B-06 | No field in the system means "the bank confirmed this". | Architecture |
| P06-B-07 | Invoice payment status has two writers. | Architecture |
| P06-B-08 | Settlement FX rate has two candidate sources. | Accounting-Tax / Architecture |
| P06-B-09 | 12 physical bank accounts share 2 GL accounts; journal code is not unique across companies. | Boss / Architecture |
| P06-B-10 | Bank transaction identity differs per import channel and is absent for manual entry. | Architecture |

---

## 8. Standing limitation

This file assigns ownership **as proposed by a single process's research session, with no counterparty session read.** It is evidence for a decision; it is not itself a decision, and it is not a reconciliation. Recorded as an explicit reliance limitation for the AAS+ and PMO files.

---

# End
