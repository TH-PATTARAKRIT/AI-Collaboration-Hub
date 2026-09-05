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

## 7. The Findings Core Reconciliation Must Not Discover Later

**Revised by the targeted evidence closure.** Ranked by *operational reach in an evidenced
deployment* — see `26 §5`'s warning that this is the wrong axis for a build decision.

### Live in every evidenced deployment

| # | Finding | Owner | Where |
|---|---|---|---|
| 1 | **Vendor down payments are never deducted from the final bill** — the deduction flag's only consumer is commented out. The vendor is billed the full order value *in addition to* the down-payment bill. | **P01** | `30 §1 H-P01-1` |
| 2 | **Any internal user can create a vendor bill** through a `sudo()` wizard, bypassing accounting rights. | **P01** | `30 §1 H-P01-2` |
| 3 | **Thai withholding is implemented twice, and 92.55% of it is invisible to the statutory CSV export.** Measured: 5,426 of 5,863 lines on the withholding account carry no `tax_line_id`, and the export inner-joins on it. Structurally guaranteed — `tax_line_id` is a stored related field never populated for a write-off line. | P05 records; **P07** owns statute; **P11** reconciles | `07 §1`, `25 §3` |
| 4 | **Amount, currency and date remain writable on an expense line after its entry is posted**, with no propagation — claim total and ledger total diverge silently. | P05 / **P08** | `10 EF-06` |
| 5 | **Approval is enforced in the action, not on the field** — an employee can write `approval_state='approve'` on their own sheet. | P05 / **P08** | `10 E1-01` |
| 6 | **An expense report can reach `done`/"Paid" with no journal entry and no payment**, and stay deletable (2 of 6 registries). | P05 / **P08** | `10 E1-02` |
| 7 | **The withholding certificate table has no UNIQUE constraint and no index** beyond its primary key; one exact duplicate certificate exists in 5,201, and **1,417 certificates carry no number at all**. | **P07** | `25 §4b` |

### Confirmed in source, installed in no evidenced deployment — *and therefore the most avoidable*

| # | Finding | Where |
|---|---|---|
| 8 | **Petty-cash spending never touches the petty-cash account.** Two independent dead paths; the module's tests cannot execute. The float's balance control is a one-way ratchet. | `05 §6` |
| 9 | **Employee advances are expensed at disbursement by shipped default**, with no receivable and **no integration at all** with the claim system — so the same cost can be recognised twice with nothing to detect it. | `05 §3`, `10 E3-02` |
| 10 | **A hashed, inalterable journal entry can be forced to `cancel`** by a raw `state` write. The P05 trigger is latent; **the underlying core gap is not, and belongs to P08.** | `10 EC-13a` |

> These three are defects SMEsPlus can still decline to inherit. For a clean-room build decision they
> rank **at least as high** as the live ones (`26 §2`, Expert 1's accepted challenge).

## 8. Open Boss Decisions

| ID | Decision | Route before Boss |
|---|---|---|
| `BD-01` | Is the accounting event owner approval, or posting? | — |
| `BD-02` | Must an advance create an employee receivable rather than an expense? | — |
| `BD-03` | May an entry's date ever derive from the clock? | — |
| `BD-04` | Are prepaid and accrued in scope for P05? | — |
| `BD-05` | Which withholding subsystem is authoritative? | **P07 + P11 first** |
| `BD-06` | Must withholding be recognised at bill posting? | **P07 first** |
| `BD-07` | Must withholding applicability follow the payee? | **P07 first** |
| `BD-08` | Is a non-deductible / add-back mechanism in scope? | **P07 first** |

**AAS+ recommends three unblocking decisions ahead of all eight** (`37 §6`): release the v18 deployed
module list; authorise a read-only restore of an existing dump; and **route the P01 findings now**.

## 9. Terminal State

| Criterion | State |
|---|---|
| `EC-01` Scope Bounded | NOT SATISFIED — EVIDENCE GAP |
| `EC-02` Enumeration Converged | **NOT SATISFIED — CONTRADICTION** |
| `EC-03` Unknown Exhausted | NOT SATISFIED — EVIDENCE GAP |
| `EC-04` Tolerance-Zero Closed | NOT SATISFIED — 13 open, 0 closed |
| `EC-05` Contradiction Resolution | **SATISFIED — EVIDENCE VERIFIED** |
| `EC-06` Negative Claim Controlled | **SATISFIED — EVIDENCE VERIFIED** |
| `EC-07` Two Clean Passes | NOT SATISFIED — counter 0 of 2 |
| `EC-08` Package Complete | NOT SATISFIED — structurally complete, Jira `NOT SUPPLIED` |

> ### TERMINAL VERDICT
>
> **P05 TARGETED EVIDENCE CLOSURE — MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR SPECIFIC EXTERNAL
> BLOCKER.**
>
> The named external blockers are exactly two, and both are cheap:
> 1. **No Odoo 18 database carrying the P05 surface exists in available evidence** (`U-01` residue).
> 2. **Runtime execution requires a write authorisation that was not given and was not assumed**
>    (`U-02b`). The dumps that would satisfy it already exist and have already been read as files.
>
> **`READY FOR CORE ACCOUNTING RECONCILIATION` is NOT declared.** Six of eight criteria are unmet,
> thirteen tolerance-zero boundaries are open, six of ten handoff elements are partial or blocked, and
> `EC-07`'s counter cannot reach 2 from here.
>
> AAS+ maintains `AASV-01` (no implementation start) and adds `AASV-02`: no *uncorrected* section of
> this package may be cited as settled design input without a further independent pass. The corrected
> sections may be relied on at their stated classes. The Layer 1 design input at `17 §6` remains
> Boss-decidable now.
>
> Boss is the sole Final Approver. No `PASS`, no `FINAL FREEZE`, no `MERGED`, no
> `IMPLEMENTATION AUTHORIZED` is claimed or implied.

## 10. Publication Evidence

| Item | Value |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical branch | `SMEsPlus` — **not modified** |
| Working branch | `research/account-p05-expense-to-pay-2026-09-04-001` |
| Base commit | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` |
| Package path | `.../ACCOUNT_REOPEN/ACCOUNT_P05_EXPENSE_TO_PAY/` (40 files) |
| Merge status | **Not merged. Never to be merged without Boss decision.** |
| Integrity | SHA-256 manifest at `14 §5` |
| Jira | `NOT SUPPLIED` — see `38 §1 Q2` |
