# 19 — P05 CORE ACCOUNTING RECONCILIATION HANDOFF PACK

Session `SMEPLUS-26-09-04-ACC-P05-E2P-REV2-001` · Process `P05 — Expense-to-Pay`

**§1–§6 are `LAYER 1 — CLEAN ROOM`** and may be transcribed into a reference package.
**§7–§10 are `LAYER 2 — AUDIT QUARANTINE`** and may not.

---

# LAYER 1 — CLEAN ROOM

## 1. What P05 Is

Expense-to-Pay is the process by which a cost incurred on the business's behalf — by an employee, by
the business directly, from a cash float, or against a card — becomes an obligation, a ledger fact, a
settlement, and a closed period.

## 2. The Business Events P05 Owns

| Event | Owner | Creates an accounting fact? |
|---|---|---|
| A cost is authorised before it is incurred | request | No |
| Funds are advanced against a future cost | advance | **Yes — an asset, a receivable from the holder** |
| A cost is incurred and evidenced | claim capture | No |
| A claim is submitted | claim | No |
| A claim is authorised | approval | No |
| A claim is recorded | accounting | **Yes — a cost and an obligation** |
| An obligation is settled | settlement | **Yes** |
| Tax is withheld at settlement | settlement | **Yes** |
| An advance is liquidated against actual cost | liquidation | **Yes** |
| A float is replenished | treasury | **Yes** |
| A recorded fact is corrected | correction | **Yes — a new, linked fact** |
| A period is closed | close | Depends on unrecorded obligations |

**Authorising and recording are separate events with separate owners.** The reference conflates them
and this research traced the consequences; see `17 §6 DI-04`.

## 3. The Distinctions the Design Must Carry

Four independent axes. Conflating any pair caused a defect that this research verified in source.

1. **Funding** — who paid first: employee, business, float, card.
2. **Nature** — direct, prepaid, accrued.
3. **Obligation character** — an employee owed a reimbursement is not a supplier owed an invoice.
4. **Settlement state** — whether money has moved.

## 4. Required Positions

The fifteen positions at `17 §6.2` (`DI-01`..`DI-15`) are the Layer 1 design input. In brief:
an advance is an **asset**; employee and supplier obligations are **distinct in the ledger**; a float
is **company-owned by construction**; authorising ≠ recording; every accounting fact carries an
**immutable identity**; a posted fact is **closed to amendment**; dates come from **documents, not the
clock**; duplicate control keys on the **cost event, not the document**; statutory reference is
**platform-scoped** while its mapping is company-scoped; withholding follows the **payee**, not the
funding route; one statutory obligation has **one** system of record; **a control that cannot be shown
to execute is not a control**; an operation determines its **scope before** resolving anything;
a settlement is **one number** from one source; analytic attribution follows the **cost**.

## 5. What Must Be Designed, Not Transferred

No usable pattern exists to transfer for: **prepaid expense**, **accrued expense**,
**employee receivable**, **corporate-card clearing**, **cross-document duplicate detection**, or a
**withholding lifecycle that survives reversal**. These are new design.

## 6. Handoff Contract to Core Accounting Reconciliation

| Element Core needs | P05 supplies | Condition |
|---|---|---|
| Cost by nature | Yes | via the resolved cost account |
| Cost by cost centre | **Partial** | costs funded through an advance or a float carry no attribution |
| Employee obligation balance | **Partial** | distinguishable by counterparty only, not by account |
| Supplier obligation balance | Yes | |
| Advance outstanding | **No** | no asset account exists on that path |
| Float position | **No** | the float is not reduced by spending against it |
| Withholding payable, and the basis for a certificate | **Partial** | two systems of record disagree |
| Non-deductible / add-back basis | **No** | the reference supplies a report, not a treatment |
| Claim-to-entry audit trail | **No** | the link is severable by four ordinary operations |
| Period-close completeness of unrecorded obligations | **No** | nothing accrues an unapproved claim |

**Six of ten handoff elements are unsuppliable or partial.** Core Accounting Reconciliation should plan
on that basis and not on the assumption that P05 delivers a complete expense subledger.

---

# LAYER 2 — AUDIT QUARANTINE

## 7. The Six Findings Core Reconciliation Must Not Discover Later

| # | Finding | Where |
|---|---|---|
| 1 | Petty-cash spending never touches the petty-cash account; the float's balance control is a one-way ratchet that sees top-ups and never drawdowns. | `05 §6`, `TZ-01` |
| 2 | Employee advances are expensed at disbursement, by shipped default, with no receivable and **no integration at all** with the claim system — so the same cost can be recognised twice with nothing to detect it. | `05 §3`, `10 E3-01`, `E3-02` |
| 3 | A hashed, inalterable journal entry can be forced to `cancel` from a non-accounting document, leaving reconciliation partials standing against it. | `10 EC-13a`, `TZ-08` |
| 4 | Thai withholding is implemented **twice**; the custom stack's withholding reaches the statutory report's on-screen totals and **disappears from its CSV export**. | `07 §2`, `TX-01` |
| 5 | Amount, currency and date remain writable on an expense line after its entry is posted, with no propagation — claim total and ledger total diverge silently. | `10 EF-06`, `TZ-03` |
| 6 | An expense report can reach state `done` and payment status "Paid" with **no journal entry and no payment at all**, and remain deletable. | `10 E1-02`, `TZ-10` |

## 8. Open Boss Decisions

| ID | Decision |
|---|---|
| `BD-01` | Is the accounting event owner approval, or posting? |
| `BD-02` | Must an advance create an employee receivable rather than an expense? |
| `BD-03` | May an entry's date ever derive from the clock? |
| `BD-04` | Are prepaid and accrued in scope for P05? |
| `BD-05` | Which withholding subsystem is authoritative? |
| `BD-06` | Must withholding be recognised at bill posting rather than only at settlement? |
| `BD-07` | Must withholding applicability follow the payee rather than the funding route? |
| `BD-08` | Is a non-deductible / add-back mechanism in scope? |
| `U-01` | Supply the deployed module list, or authorise a runtime enumeration. |
| `U-02` | Authorise a P05 runtime trace. |

## 9. Terminal State

Against the eight criteria of `SMEPLUS-DR-EXIT-8C-001`:

| Criterion | State |
|---|---|
| `EC-01` Scope Bounded | **NOT MET** — the deployed universe is `UNBOUNDED / NOT YET ENUMERABLE` (`U-01`) |
| `EC-02` Enumeration Converged | **NOT MET** — no runtime evidence (`U-02`) |
| `EC-03` Unknown Exhausted | **NOT MET** — five gating unknowns |
| `EC-04` Tolerance-Zero Closed | **NOT MET** — thirteen boundaries open |
| `EC-05` Contradiction Resolution | **MET** — zero remain as unresolved differences of opinion |
| `EC-06` Negative Claim Controlled | **MET** — no `B`/`C`/`D` upgraded to `A` |
| `EC-07` Two Consecutive Clean Passes | **NOT MET — the counter has not started** |
| `EC-08` Final Knowledge Package | **STRUCTURALLY COMPLETE**, inheriting the gaps above |

> ### TERMINAL VERDICT
>
> **`HOLD — EVIDENCE REQUIRED`.**
>
> The research is delivered in full: every deliverable the directive names exists, every mandatory
> register is populated, four independent adversarial challenges were executed and consolidated, and
> the scope-aware constitution correction was absorbed without a reset.
>
> **`READY FOR CORE ACCOUNTING RECONCILIATION` is NOT declared.** Six of ten handoff elements are
> unsuppliable or partial (§6), thirteen tolerance-zero boundaries are open, and `EC-07`'s counter has
> not started. Declaring readiness would require bypassing `EC-01`, `EC-02`, `EC-03`, `EC-04` and
> `EC-07` — which `EC-04` expressly forbids for a tolerance-zero risk.
>
> AAS+ additionally **vetoes any implementation start** (`AASV-01`). The Layer 1 design input at
> `17 §6` is nevertheless Boss-decidable **now** and does not wait on the items above.
>
> Boss is the sole Final Approver. No `PASS`, no `FINAL FREEZE`, no `MERGED`, no
> `IMPLEMENTATION AUTHORIZED` is claimed or implied.

## 10. Publication Evidence

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` (not modified) |
| Working branch | `research/account-p05-expense-to-pay-2026-09-04-001` |
| Base commit | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` |
| Package path | `99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_P05_EXPENSE_TO_PAY/` |
| Merge status | **Not merged. Never to be merged without Boss decision.** |
| Commit SHAs | see `14 §1` |
| Integrity | SHA-256 manifest at `14 §2` |
| Jira | `NOT SUPPLIED` — see `18 §2` |
