# P07 — CANDIDATE INPUT → PROCESS → OUTPUT → HANDOFF PACK

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.

> **PHASE S DISCOVERS CANDIDATES ONLY.** Nothing here is a contract. Producer/consumer contracts
> are validated in PHASE B when all eleven sessions are integrated under AI EOS. **AI EOS is not
> active and was not invoked.** No SMEsPlus function, schema, API or UI is designed here.

Every row carries exactly one of the six mandated classes:
`FACT VERIFIED` · `SUPPORTED INTERPRETATION` · `DESIGN CANDIDATE — PHASE S ONLY` ·
`CONTRADICTED` · `UNRESOLVED — EVIDENCE REQUIRED` · `BOSS DECISION REQUIRED`.

**Tested, not assumed.** Each candidate input and output was checked against the estate. Where
the estate does not carry it, the row says so — a candidate that exists only because a designer
would want it is marked `DESIGN CANDIDATE — PHASE S ONLY` and nothing stronger.

---

## 1. CANDIDATE INPUTS

| # | Candidate input | Does the estate carry it? | Class | Evidence / gap |
|---|---|---|---|---|
| `CI-01` | **Taxable business event reference** — the delivery, service performance or utilisation that creates the tax point | **No.** No carrier exists on the tax fact for the business-event date or reference | `CONTRADICTED` *(the assumption that it exists)* | `D-1`; `X-04`, `X-05` `BLOCKING for P07`; `TP-01`, `TP-02` |
| `CI-02` | **Tax base** | **Partly, and inconsistently.** Four sites compute the withholding base three different ways; `tax_base_amount` and `price_subtotal` are both in use, two of them inside one file | `FACT VERIFIED` *(that it is multiply-defined)* | `P07-F-111`; `EP-5` §6.1 |
| `CI-03` | **Tax amount** | **Yes, and it can disagree with its own transaction.** 199 of 1,186 stored values diverge in one identity | `FACT VERIFIED` | `P07-F-109`, `EP-6` |
| `CI-04` | **Tax type / form determination** (PND 1/2/3/3a/53/54; VAT input vs output) | **Yes, but keyed on the wrong attribute.** The PND form is selected from `partner_id.is_company`, a UI convenience flag, not a typed legal personality | `FACT VERIFIED` | `W-K-03`; the selection is visible in `l10n_th_withholding_tax/models/account_move.py` `get_tax_domain` |
| `CI-05` | **Counterparty legal identity** — taxpayer id, legal personality, branch | **Yes, four times over.** Branch exists in four representations across two scopes; three modules contribute | `FACT VERIFIED` | `P07-F-06`, `P07-C-02`, corroborated at field level by `EP-4b` |
| `CI-06` | **Company / legal-entity scope of the tax fact** | **Yes** — `res.company` is present in all 7 identities; `res.company.branch` exists and **no statutory report reads it** | `FACT VERIFIED` | `R-B-04`; `20 §6` |
| `CI-07` | **Document date** (`D-2`) | **Yes** — `account.move.invoice_date`, read by one display column | `FACT VERIFIED` | `04 §3` |
| `CI-08` | **Effective / tax-period date** (`D-5`) | **Yes, at entry *and* item level, in 3 of 7 identities — and read for selection at neither** | `FACT VERIFIED` | `P07-F-107`, `EP-3`/`EP-4` |
| `CI-09` | **Settlement date** (`D-4`) | **Not as an input to the tax fact.** It exists in P06 and is user-settable; the PND dates the fact by the invoice | `FACT VERIFIED` | `P07-F-11`, `W-C-01`; P06's own assessment in `PI-02` §2 |
| `CI-10` | **Allocation of a settlement across documents** | **Exists as data; not visible to the withholding computation.** The predicate `payment_state != 'not_paid'` is satisfied by `partial` | `FACT VERIFIED` | `W-C-02`, `TPF-04` |
| `CI-11` | **Correction / reversal lineage** | **Absent.** Three of five lineage links absent, two broken | `FACT VERIFIED` | `P07_CORRECTION_REVERSAL_LINEAGE_MATRIX.md §2` |
| `CI-12` | **Statutory evidence / document reference** (tax invoice, certificate, supporting document) | **Partial.** The WHT certificate links to the payment; the tax invoice has no document identity P07 can supply | `FACT VERIFIED` | `DOC-01`; `EP-4b` |
| `CI-13` | **An immutable settlement event with its own date** | **Not present today; committed by P06 as `P07-R-01`** | `SUPPORTED INTERPRETATION` *(that the commitment closes the counterparty half)* | `PI-02` §6 |
| `CI-14` | **Deferred-input-tax claim window** — the legal basis for claiming input tax in a month later than the invoice | **Unknown.** No primary source held | `UNRESOLVED — EVIDENCE REQUIRED` | `P07-U-03`; `AASR-P07-VETO-01` rests on it |

**The shape of the input side:** of fourteen candidate inputs, **one is absent outright**
(`CI-01`), **three exist but are not connected to the tax fact** (`CI-09`, `CI-10`, `CI-11`),
**three are multiply-defined** (`CI-02`, `CI-05`, and `CI-08` at two levels), and **one is a
statutory unknown** (`CI-14`). Only `CI-06` and `CI-07` are singular, present and used.

---

## 2. PROCESS SEMANTIC CORE

Evidence-supported semantics only. Where the estate performs a step differently from what the
statute requires, both are stated and the divergence is classed — **the statutory side is never
inferred from the implementation.**

| # | Semantic step | What the estate does | Class |
|---|---|---|---|
| `PS-01` | **Classify the tax consequence** of a business event | Determined by the tax code attached to the document line, chosen by the user; form selection keyed on `is_company` | `FACT VERIFIED` |
| `PS-02` | **Determine the applicable tax event and its date** | **Not performed.** There is no tax-point determination step; the accounting date stands in for it | `FACT VERIFIED` |
| `PS-03` | **Determine statutory period membership** | Derived at query time from the accounting date. Two inert carriers exist (`CI-08`) | `FACT VERIFIED` |
| `PS-04` | **Establish the tax document / certificate state** | Create is modelled; issue is not distinguished from create; cancel is a Boolean; reissue and replace are not modelled | `FACT VERIFIED` |
| `PS-05` | **Apply correction / cancellation / reissue semantics** | A note is an ordinary reversal entry placed by accounting date; a cancelled certificate is a flag with no history | `FACT VERIFIED` |
| `PS-06` | **Preserve statutory audit lineage** | **Not performed.** No filed figure is stored; `L-3` is absent | `FACT VERIFIED` |
| `PS-07` | **Produce report/reconciliation-ready tax truth** | Every statutory output is a **render over live master data**; ≥8 ordinary actions rewrite an already-filed report | `FACT VERIFIED` |
| `PS-08` | **A tax fact and its accounting entry may fall in different periods** | Not possible today — one selector serves both | `DESIGN CANDIDATE — PHASE S ONLY` |
| `PS-09` | **A tax period has a state of its own, distinct from the accounting period lock** | Does not exist | `DESIGN CANDIDATE — PHASE S ONLY` |
| `PS-10` | **A filed figure, once reported, is immutable in its period** | Mechanism absent; **whether statute requires it is unresolved** | `BOSS DECISION REQUIRED` |
| `PS-11` | **One definition of a tax amount, consumed by every site** | Four sites, three bases, no shared definition | `DESIGN CANDIDATE — PHASE S ONLY` — the defect is `FACT VERIFIED` (`P07-F-111`), the remedy is a candidate |
| `PS-12` | **Localisation contributes tax-timing semantics** | **It does not.** The installed Thai localisation adds 18 fields over 8 models, none a date, period or tax point | `FACT VERIFIED` (`P07-F-105`) |

---

## 3. CANDIDATE OUTPUTS

| # | Candidate output | Does the estate produce it? | Class |
|---|---|---|---|
| `CO-01` | **Output-VAT obligation state** | Produced as a render; not stored; period from the accounting date | `FACT VERIFIED` |
| `CO-02` | **Input-VAT credit state** | Same; and the claim window that would justify a different period is `UNRESOLVED` (`CI-14`) | `FACT VERIFIED` + `UNRESOLVED — EVIDENCE REQUIRED` |
| `CO-03` | **Withholding obligation state** | Produced; **reported against the invoice, not the payment**; the posted withholding line is reported by neither PND branch | `FACT VERIFIED` (`P07-F-11`) |
| `CO-04` | **Withholding certificate state** | Create/cancel only; cancel is a flag | `FACT VERIFIED` |
| `CO-05` | **Tax document state** (tax invoice, credit/debit note) | Issue not distinguished from create; duplicate copy not modelled (`P07-U-13`) | `FACT VERIFIED` |
| `CO-06` | **Statutory-period allocation** | Derived, never stored; no period state | `FACT VERIFIED` |
| `CO-07` | **Tax correction / reversal event** | **Not produced as an event.** Corrections are ordinary entries; stored figures are overwritten in place | `FACT VERIFIED` |
| `CO-08` | **Report/reconciliation-ready tax fact** | **Not produced.** `L-3` absent — nothing records what was filed | `FACT VERIFIED` |
| `CO-09` | **The s.87 output/input tax registers** | Produced by **two** implementations that can both be installed and return different totals for one company and month (`DUP-04`); and on a Thai-language install both are silently empty (`P07-F-01`) | `FACT VERIFIED` |
| `CO-10` | **Unresolved statutory dependency** *(an output in its own right)* | Yes — and this package treats it as a deliverable rather than an omission: `P07-U-03`, `P07-U-04`, `P07-U-07`…`P07-U-10`, `P07-U-23`…`P07-U-26`, `P07-U-34`, `P07-U-35`, `P07-U-36` | `UNRESOLVED — EVIDENCE REQUIRED` |

---

## 4. CANDIDATE HANDOFFS

For each material output state. **Probable consumer**, not designated consumer — designation is
PHASE B's.

### `CH-01` — Withholding obligation, at the moment of payment

| dimension | statement |
|---|---|
| **Probable consumer** | P06 (settlement), P08 (ledger), the PND filing surface |
| **Business meaning** | An obligation to withhold arose on a payment and must be remitted within 7 days of that payment (`S-30`, `S-32`) |
| **Minimum payload semantics** | payment identity · payment date · gross amount · currency · per-document allocation · payee legal personality · income type · rate · withheld amount · the posted withholding line's identity |
| **Scope** | `COMPANY` (the withholding agent) |
| **Required provenance** | the payment event, immutable; the line the withholding was computed from; the rate version used |
| **The consumer must NOT assume** | that the invoice date is the tax point; that a `partial` payment means the whole invoice's withholding arose; that `wht_amount` on the move equals the withheld amount (`P07-F-109`); that the PND reports the posted withholding line (it does not — `P07-F-11`) |
| **Unresolved for PHASE B** | Who owns the reporting key once the settlement carries its own date — the P06 half is committed (`P07-R-01`), the P07 half is a design act |
| **Class** | `SUPPORTED INTERPRETATION` |

### `CH-02` — VAT obligation / credit, with its statutory period

| dimension | statement |
|---|---|
| **Probable consumer** | P08 (period close), the ภ.พ.30 filing surface, the s.87 registers |
| **Business meaning** | An output-tax liability or input-tax credit belongs to a **tax month**, which is not the accounting month |
| **Minimum payload semantics** | tax fact identity · tax point date · tax month · base · rate · tax amount · document reference · company |
| **Scope** | `COMPANY` |
| **Required provenance** | the business event for goods (`S-01`) or the payment/utilisation for services (`S-02`); the tax invoice |
| **The consumer must NOT assume** | that tax month equals accounting month; that a value in `tax_period` was used for selection (**it was not** — `04 §4`); that the carrier exists at all (**it does not, in 4 of 7 identities**) |
| **Unresolved for PHASE B** | the deferred input-tax claim window — `CI-14`, `P07-U-03` |
| **Class** | `DESIGN CANDIDATE — PHASE S ONLY` for the separation; `FACT VERIFIED` for the present behaviour |

### `CH-03` — Tax document / certificate state

| dimension | statement |
|---|---|
| **Probable consumer** | the counterparty (externally), P08, the audit trail |
| **Business meaning** | A statutory document was issued, and its particulars are prescribed (`S-19`, `S-20`, `S-31`) |
| **Minimum payload semantics** | document type · number · issue date · issuer and counterparty particulars **including branch** · the fact it evidences · lifecycle state · superseding document where one exists |
| **Scope** | `COMPANY` for the issuer; `TENANT` for counterparty particulars — **and the estate uses the two interchangeably** (`P07-F-06`) |
| **Required provenance** | the tax fact; the prior document where this one replaces it |
| **The consumer must NOT assume** | that `wt_cert_cancel = true` records **when**, **why** or **what replaced it** — it is a Boolean; that a reissue is distinguishable from a first issue |
| **Unresolved for PHASE B** | duplicate-copy tax invoice (`P07-U-13`); the prescribed contents of the s.87(3) report (`P07-U-26`, which also gates P04's `P04-F-67`) |
| **Class** | `FACT VERIFIED` on the present state; `DESIGN CANDIDATE — PHASE S ONLY` on the lifecycle |

### `CH-04` — Statutory report / register content

| dimension | statement |
|---|---|
| **Probable consumer** | the Revenue Department (externally), P08, P11 |
| **Business meaning** | The figure filed for a company and a tax month |
| **Minimum payload semantics** | company · tax month · figure · **the constituent facts it was composed from** · the moment it was fixed |
| **Scope** | `COMPANY` |
| **Required provenance** | **a stored filed figure, which does not exist today** (`L-3`) |
| **The consumer must NOT assume** | that re-running a report reproduces what was filed — every output is a render over live master data and ≥8 ordinary actions change it (`A-15`) |
| **Unresolved for PHASE B** | whether a filed period may change at all — `PS-10`, `BOSS DECISION REQUIRED` |
| **Class** | `FACT VERIFIED` on the gap; `DESIGN CANDIDATE — PHASE S ONLY` on the remedy |

### `CH-05` — To P10: the localisation answer and one contradiction

Published separately as `P07_TO_P10_HANDOFF.md`. Summarised: `Q07-1`…`Q07-3` answered
negative and bounded; **`Q07-4` contradicted**; `Q07-5` refused as a statutory unknown; the
9-vs-10 count resolved as two denominators. `FACT VERIFIED` / `CONTRADICTED` /
`UNRESOLVED — EVIDENCE REQUIRED` respectively.

### `CH-06` — To P06: acceptance of four committed requirements

P06's `P07-R-01`…`P07-R-04` are **accepted as the counterparty half** of `X-07`, `X-08`,
`X-09`. **None of the three closes**, because the remaining half in each is P07's own reporting
predicate. No new question is sent to P06; nothing is asked that P06 has not already committed.
`SUPPORTED INTERPRETATION`.

---

## 5. What This Pack Is Not

- It is **not** an input or output contract. No element here is final, and the numbering is
  candidate numbering.
- It does **not** designate consumers. Every consumer named is **probable**, from evidence of
  who reads the fact today or who asked for it in a published handoff.
- It does **not** propose a schema, a field, an API or a UI.
- It does **not** resolve any statutory question, and it does not permit one to be inferred from
  any behaviour recorded in it.
