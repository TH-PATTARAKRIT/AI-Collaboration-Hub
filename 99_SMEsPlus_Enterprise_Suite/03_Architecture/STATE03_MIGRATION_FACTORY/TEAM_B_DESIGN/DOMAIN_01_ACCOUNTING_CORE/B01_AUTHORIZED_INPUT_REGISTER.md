# B01 — Authorized Input Register

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B1 — Sanitized Input Canonicalization |
| Source | `TEAM_A/06_DOMAIN_RESEARCH/DOMAIN_01_ACCOUNTING_CORE/SONNET_DEEP_SYNTHESIS/13_TEAM_B_CANDIDATE_INPUT.md` (primary), plus the supporting registers it directly cites (`03_ACCOUNTING_PRINCIPLE_REGISTER.md`, `04_BUSINESS_INVARIANT_REGISTER.md`, `05_GENERIC_BUSINESS_RULE_REGISTER.md`, `06_STATE_EVENT_LOGIC_ANALYSIS.md`, `07_MATHEMATICAL_REASONING.md`, `09_EXCEPTION_FAILURE_ANALYSIS.md`, `11_RESIDUAL_UNKNOWN_REGISTER.md`, `12_REFERENCE_TO_ADVANCEMENT_REGISTER.md`) |
| Authorization | `TEAM_B_HANDOFF/DOMAIN_01_ACCOUNTING_CORE_E_TEAM_B_HANDOFF_AUTHORIZATION.md`, commit `2314a786d9a1918f4cf4de3da7c2f8b85d3c98fe` |
| Vendor technical design entering this register | **NONE** |

## 1. Purpose

This register re-expresses the authorized Team A output as a flat, classified list, each item
tagged with exactly one primary category per directive §B1. Source IDs (`AP-xx`, `INV-xx`,
`GR-xx`, `ADV-xx`, `GAP-Dxx`) are preserved for traceability into B15. No item below
introduces a fact, principle, or rule not already present in the authorized input — this
phase classifies, it does not originate.

## 2. Business Facts

| ID | Statement | Source |
|---|---|---|
| BF-01 | Every committed accounting entry must have total debits equal to total credits | Candidate Input |
| BF-02 | Money must be represented as exact decimal values, never binary floating point | Candidate Input, AP-12 |
| BF-03 | Once formally closed and reported, an accounting period must not silently accept new or altered transactions | Candidate Input |
| BF-04 | A correction to an already-committed entry should be additive (new, linked, offsetting record), never destructive (in-place alteration) | Candidate Input, INV-06 |
| BF-05 | Foreign-currency transactions must be recognised at a valid exchange rate; monetary balances must be remeasured to the functional currency at each reporting date (IAS 21) | Candidate Input, AP-07 |
| BF-06 | Certain statutorily regulated documents (Thai e-Tax invoices/receipts, confirmed by official ETDA source) must carry provable content integrity and origin authenticity, and be retained for a defined period | Candidate Input, AP-10 |
| BF-07 | Statutorily numbered documents (Thai tax invoices, confirmed by official Revenue Department source) must state a serial number as a mandatory particular; a "must be gapless" characterization is plausible but secondary-sourced only | Candidate Input, AP-11 |
| BF-08 | Accounting records generally must be retained for a defined statutory period (Thailand: 5–7 years) and be available for independent audit | Candidate Input, AP-09 |
| BF-09 | Balance-sheet accounts carry their balance forward at year-end; income-statement accounts reset to zero | AP-14 |
| BF-10 | An account belongs to a fixed accounting category that determines its statement placement and year-end carry-forward behaviour, and that category is immutable once set | GR-08 |

## 3. Accounting Principles

| ID | Statement | Source |
|---|---|---|
| PR-01 | Double-entry bookkeeping: every transaction recorded as equal, offsetting debits and credits | AP-01 |
| PR-02 | The accounting equation: Assets = Liabilities + Equity | AP-02 |
| PR-03 | The journal is the book of original entry; the ledger is the authoritative source for financial reports | AP-03 |
| PR-04 | Posting is the act of finalizing a journal entry into the ledger | AP-04 |
| PR-05 | Period cutoff control: transactions must not post into an already-reported period without authorized override | AP-06 |
| PR-06 | Correction-by-reversal is a validated cross-ERP common pattern (not yet a cited formal accounting standard) | AP-05 |
| PR-07 | An audit trail should allow tracing every ledger entry back to its originating transaction | AP-13 |
| PR-08 | Exact-decimal monetary representation is a software/financial-computing correctness norm, not a formal accounting standard — the underlying need (no precision loss) is universal, the storage-technology framing is not | AP-12, Disagreement-02 |

## 4. Business Rules

| ID | Neutral statement | Source |
|---|---|---|
| BR-01 | A committed entry's total debit must equal its total credit | GR-01 |
| BR-02 | A posting line carries a debit amount or a credit amount, never both | GR-02 |
| BR-03 | A line's transaction-currency amount and functional-currency amount must agree in sign | GR-03 |
| BR-04 | A financial posting line must reference an account | GR-04 |
| BR-05 | A transaction dated within an already-closed period must not commit without an authorized, recorded override | GR-05 |
| BR-06 | Correcting a committed entry means posting a new, linked, offsetting entry; the original stays unchanged | GR-06 |
| BR-07 | A committed entry should not be returned to an editable state and altered in place | GR-07 (stated as should-hold; reference system violates it — see §7 Open Questions is not applicable, this is a settled design requirement, not an unknown) |
| BR-08 | Every account belongs to a fixed accounting category governing statement placement and carry-forward | GR-08 |
| BR-09 | A foreign-currency transaction is recognised at the spot rate on its date; monetary balances are remeasured to functional currency at each reporting date | GR-09 |
| BR-10 | Monetary values are represented with exact decimal precision | GR-10 |
| BR-11 | A financial document formally issued to a third party under statutory regulation must be provably unaltered after issuance | GR-11 |
| BR-12 | A statutorily numbered document must carry a genuinely sequential number without gaps | GR-12 |
| BR-13 | An account marked inactive must not accept new activity while still referenced by active configuration | GR-13 |

## 5. Invariants

| ID | Statement | Source |
|---|---|---|
| IV-01 | Σdebit(entry) = Σcredit(entry) for every committed entry | INV-01 |
| IV-02 | A transaction dated within an already-closed period must not post without a discoverable, authorized override | INV-02 |
| IV-03 | Every journal, account, and entry belongs to exactly one company; no transaction spans or leaks across company boundaries | INV-03 |
| IV-04a | A line's functional-currency amount and transaction-currency amount must agree in sign | INV-04(a) |
| IV-04b | Foreign-currency monetary balances must be remeasured to functional currency at each reporting date (IAS 21) — **status of underlying implementation is an open question, not the requirement itself** | INV-04(b) |
| IV-05 | A correction to a committed fact must be a new, linked record; the original remains intact and discoverable | INV-05 |
| IV-06 | Once a fact is committed — and especially once consumed downstream (reported, reconciled, filed) — its content must not be silently mutable | INV-06 |

## 6. Neutral Events / Lifecycle

| ID | Statement | Source |
|---|---|---|
| LC-01 | A financial fact's lifecycle: capture (not yet committed) → commitment (part of the authoritative record) → optionally voiding (retained, excluded from counting) → optionally correction (a new, linked fact; never a mutation of the original) | Candidate Input, `06_STATE_EVENT_LOGIC_ANALYSIS.md` |
| LC-02 | Two distinct business questions must not be conflated into one representation: "is this fact part of the ledger yet" vs. "should this fact still count" | `06_STATE_EVENT_LOGIC_ANALYSIS.md` |
| LC-03 | Whether a committed fact may ever be mutated in place should depend on whether it has been consumed by anything outside the entity's own books — not on raw status alone | `06_STATE_EVENT_LOGIC_ANALYSIS.md`, ADV-07 |
| LC-04 | An event log recording that a fact was posted, reversed, or corrected — with actor, timestamp, before/after — must be append-only, independent of whether the underlying record itself is mutable | `06_STATE_EVENT_LOGIC_ANALYSIS.md` |

## 7. Regulatory Requirements (scope-limited)

| ID | Statement | Source |
|---|---|---|
| RG-01 | Financial statements must be prepared, retained, and independently audited (Thailand, Accounting Act B.E. 2543) | AP-08 |
| RG-02 | Accounting records must be retained 5–7 years (Thailand) | AP-09 |
| RG-03 | e-Tax invoices/receipts must have provable content integrity and origin authenticity (Thailand, ETDA official source, RETS 21-2562) — **scope limited to e-Tax documents; does not extend to the general ledger without separate proof** | AP-10 |
| RG-04 | Tax invoices must state a serial number as a mandatory particular (Thailand, Revenue Department official source, Revenue Code §86) — **scope limited to tax invoices; gapless-numbering and general-ledger extension remain unproven (P4 only)** | AP-11 |
| RG-05 | Foreign-currency monetary items must be remeasured to functional currency at each reporting date (IFRS, IAS 21) | AP-07 |

## 8. Migration Requirements

| ID | Statement | Source |
|---|---|---|
| MG-01 | Migrated entries must be independently validated for debit/credit balance; a source "posted" state is not proof of validity | Candidate Input |
| MG-02 | All applicable period-control mechanisms must be evaluated together for historical data, not assumed consistent | Candidate Input |
| MG-03 | Reversal/correction linkages between records are business data and must be preserved as such | Candidate Input |
| MG-04 | A migrated "committed-once" record cannot be assumed free of later, undisclosed alteration unless change history is also migrated and interrogated | Candidate Input |

## 9. Audit / Control Requirements

| ID | Statement | Source |
|---|---|---|
| AU-01 | A compensating balance-check must exist independent of source-system trust | Candidate Input |
| AU-02 | Every regulated document class's integrity requirement must be honored regardless of any configuration default | Candidate Input |
| AU-03 | The audit trail (who changed what, when) must be a forced, non-optional property of every committed fact, separate from whether the fact itself is mutable | Candidate Input |

## 10. Advancement Objectives (candidate problem statements only — not approved designs)

| ID | Statement | Source |
|---|---|---|
| AO-01 | Make the balance guarantee (Σdebit=Σcredit) non-optional at the point data becomes durable | ADV-01 |
| AO-02 | Tamper-evidence as a default property of regulated document classes, not an administrator-remembered opt-in | ADV-02 |
| AO-03 | Reduce the number of independent, potentially-disagreeing controls governing "is this period open for posting" | ADV-03 |
| AO-04 | Eliminate or gate the destructive correction path so the additive (reversal) path is the only one available for committed, downstream-consumed facts — **highest priority** | ADV-04 |
| AO-05 | Reduce the type-branching burden inherited when one storage shape serves semantically distinct business objects | ADV-05 |
| AO-06 | Reduce the number of independently-writable columns representing one monetary fact | ADV-06 |
| AO-07 | Gate correction-path availability on downstream consumption, not on raw status alone | ADV-07 |
| AO-08 | Currency remeasurement — **not yet an advancement objective; evidence insufficient to state a limitation** (research-required, carried to Open Questions) | ADV-08 |

## 11. Open Questions (unresolved — carried forward as questions, not conclusions)

| ID | Question | Source |
|---|---|---|
| OQ-01 | Does Thai law require tamper-evidence or gapless numbering for the general ledger, beyond the confirmed e-Tax-invoice and tax-invoice scopes? | Candidate Input, GAP-D01-07/08 |
| OQ-02 | Is periodic currency remeasurement (IAS 21) a requirement this domain must independently implement, or is it satisfied elsewhere in a full system? | Candidate Input, GAP-D01-17, ADV-08 |
| OQ-03 | What is the correct rounding policy per currency (decimal places, rounding method)? | Candidate Input, GAP-D01-04 |
| OQ-04 | What should the semantics of a reversal-of-a-reversal be? | GAP-D01-23 |
| OQ-05 | Should future-dated postings be restricted, and if so under what condition? | GAP-D01-20 |
| OQ-06 | How should concurrent edits to related records be governed? | GAP-D01-21 |
| OQ-07 | Should reopening a committed fact (where legitimately allowed pre-consumption) be independently role-gated beyond whatever consumption check governs it? | GAP-D01-22 |
| OQ-08 | Is enterprise-layer behavior beyond the core model observable? | GAP-D01-01, GAP-D01-18 (permanently uncloseable by clean-room rule, not effort) |
| OQ-09 | Full list of 20 open items | `11_RESIDUAL_UNKNOWN_REGISTER.md` — incorporated by reference, not restated in full here to avoid drift between two copies of the same register |

## 12. Explicitly Excluded From This Register

Per directive §5/§6, the following were consulted only for traceability in Team A's own
output and are **not** reproduced here and **must not** enter any later Team B design
artifact as design authority: vendor field/method/table names, vendor class hierarchy,
vendor hooks, vendor state-machine field shapes, Class E/F findings, Class G unknowns
represented as settled fact, or any quarantine-register content.

## 13. Acceptance Check

```
No Vendor technical design in this register : CONFIRMED
Every item traces to an authorized source ID : CONFIRMED
Class G items preserved as questions, not requirements : CONFIRMED
```

**B1 = COMPLETE.**
