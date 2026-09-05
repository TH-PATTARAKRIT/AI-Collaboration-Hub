# 26 — P05 TOLERANCE-ZERO BOUNDARY REGISTER

`LAYER 2 — AUDIT QUARANTINE`

## 1. Governing Rule

`EC-04` of `SMEPLUS-DR-EXIT-8C-001`: all applicable tolerance-zero boundaries must be evidence-closed
before advancement, and **`CONDITIONAL PASS` may not bypass a tolerance-zero risk.**

## 2. Position on Deployment Evidence and Tolerance-Zero

The new module evidence (`24`) shows that six of the thirteen boundaries rest on modules installed in
**no** evidenced deployment. A position must be taken and defended rather than assumed:

> **Deployment evidence changes a boundary's REACH. It does not close the boundary.**
> A defect that is unreachable today because a module is not installed becomes reachable the moment it
> is installed, and nothing in the evidence prevents that installation. Accordingly this register
> records **two independent axes** — `DEFECT STATUS` (does the defect exist in the code?) and
> `REACH` (is it reachable in an evidenced deployment?) — and **closes a boundary only on the first
> axis**. No boundary below is closed because it is currently unreachable.

This position was put to AAS-03 experts for adversarial challenge.

> ### AAS-03 Expert 1 CHALLENGED THIS FRAMING — and the challenge is accepted
>
> Expert 1 agreed the position is *mechanically* honoured — 0 boundaries closed, every Gate Impact
> reads `OPEN`, `EC-04` is not formally violated. But it raised a substantive objection that this
> register accepts:
>
> > *"Deployment reach is close to the **wrong axis entirely** for a build-decision project. SMEsPlus
> > hasn't built petty cash or employee-advance capability yet — the entire point of studying those
> > reference modules is to inform whether and how to build them. A confirmed design defect in code
> > nobody currently runs is not **less** relevant to that decision — arguably it is **more**
> > relevant, because it is a documented mistake SMEsPlus can still avoid inheriting."*
>
> It further observed that §5's "severity inversion" language, and the phrase "reported almost in
> passing", **function as a downgrade for any reader deciding where to spend effort**, regardless of
> the `OPEN` label underneath — so the file was performing a substantive reprioritisation while
> claiming only a formal one.
>
> **Accepted, and §5 is qualified accordingly.** `REACH` is retained because it is the right axis for
> *one* question — what is at risk in a running system today, which is what the P01 and P07 handoffs
> turn on. It is the **wrong** axis for the question this programme actually exists to answer: what
> SMEsPlus should build. On that axis a `LATENT` finding carries **equal or greater** weight, because
> it is a defect the clean-room design can still decline to inherit. Both readings are now stated
> rather than one being implied. See `37 §3 NC+06`.

## 3. Register

`REACH` legend — `LIVE`: module installed in ≥1 evidenced deployment · `LATENT`: defect exists in
source, module installed in no evidenced deployment · `UNKNOWN-v18`: reach in the v18 target is
class **D** in all rows, because no v18 P05 deployment was found (`24 §4`).

| ID | Boundary (business / accounting risk) | Defect status | Evidence | Scope (`CORR1`) | Reach | Peer owner | Gate impact |
|---|---|---|---|---|---|---|---|
| `TZ-01` | Petty-cash disbursement booked as employee payable; float balance permanently overstated and its control a one-way ratchet — *cash integrity* | **CONFIRMED** — source, upheld on four independent lines (`05 §6`) | `hr_expense_petty_cash/models/hr_expense.py:72-79`; token 0× in `ENT18`; module tests are a non-executing v14 artefact | COMPANY | **LATENT** — installed in 0 of 6 registries | P08 (cash) | **OPEN** |
| `TZ-02` | `petty.cash` carries no company; global `unique(partner_id)`; a `sudo()` unscoped lookup lets one company's float config gate another's bills — *company isolation* | **CONFIRMED** — source | `petty_cash.py:12-36`; `hr_expense_petty_cash/models/account_move.py:24` | COMPANY (derived, `22 R-02`) | **LATENT** | P08 | **OPEN** |
| `TZ-03` | Expense amount, currency, date, product, quantity remain writable after posting with no propagation — *immutable posted facts* | **CONFIRMED** — source; nine fields view-only-protected, the apparent model guard is an unregistered `@api.onchange`, and the employee's own record rule has no state clause | `hr_expense.py:613-643`; `hr_expense_views.xml`; `security/ir_rule.xml:23-28` | COMPANY | **LIVE** — `hr_expense` installed in 5 of 6 | P08 | **OPEN** |
| `TZ-04` | Declared payment-immutability guard does not contain `journal_id` or `ref` (missing comma → `'journal_idref'`) — *immutable posted facts* | **CONFIRMED** — AST-evaluated, independently re-run | `hr_expense/models/account_payment.py:20-28`; reproduction at `14 §3` | COMPANY | **LIVE** | P06 / P08 | **OPEN** |
| `TZ-05` | Posted entries force-cancelled by a raw `state` write from a non-accounting document | **CONFIRMED** — source; scope enumerated at `10 EC-13a` | `advance_expense_request.py:214-215`; `wizard/advance_request_rejected.py:14-15` | COMPANY | **LATENT** — `scgl_advance_expense_request` installed in 0 of 6 | P08 | **OPEN** |
| `TZ-06` | Three cross-document duplicate classes undetected (advance vs claim, claim vs vendor bill, petty cash vs reimbursement) — *duplicate posting* | **CONFIRMED** — class **A** within the two module scopes; made structural by `E3-02` (no integration exists at all) | `09 §3`; `10 E3-02` | COMPANY | **PARTLY LATENT** — the advance and petty-cash legs are latent; claim-vs-vendor-bill is **LIVE** | P01 / P11 | **OPEN** |
| `TZ-07` | Advance clearing credits one arbitrary account, carries no currency, and can collapse to a self-cancelling entry on the same bank account while reporting the advance cleared | **CONFIRMED** — source | `advance_request_reconcile.py:62-92`; `scgl_advance_expense_request/models/account_move.py:58-114` | COMPANY | **LATENT** | P06 / P08 | **OPEN** |
| `TZ-08` | A hashed, inalterable journal entry can be forced to `cancel`; reconciliation partials survive against it — *immutable posted facts* | **CONFIRMED** — source; `'state'` is not in `_get_integrity_hash_fields()` | `ENT18/account/models/account_move.py:3208-3214, 3836, 5351-5352` | COMPANY | **LATENT** *via this trigger*; the underlying core gap is **LIVE** and belongs to P08 | **P08** | **OPEN** |
| `TZ-09` | Approval enforced in the action, not on the field — an employee can write `approval_state='approve'` on their own sheet — *unauthorised posting* | **CONFIRMED** — source, class **A** over `ENT18/addons` | `hr_expense_sheet.py:79-86, 491-509`; `security/ir.model.access.csv:3`; `ir_rule.xml:49-54` | COMPANY | **LIVE** | P08 | **OPEN** |
| `TZ-10` | An expense report reaches `done` / "Paid" with **no** journal entry and no payment, and stays deletable — *financial integrity* | **CONFIRMED** — source | `hr_expense_extract/models/hr_expense.py:23, 180-188, 200-223` | COMPANY | **LIVE in 2 of 6** (`hr_expense_extract` installed in both `iTEST02`) | P08 | **OPEN** |
| `TZ-11` | Duplicate payment: self-documented payroll double-payment path; vendor down payment never deducted from the final bill | **CONFIRMED** — source, both legs | `hr_payroll_expense/models/account_move.py:62-66`; `scgl_purchase_advance_payment/wizard/purchase_advance.py:51, 178-179` | COMPANY | **LIVE** — payroll leg in 2 of 6; **down-payment leg in 4 of 4 distinct databases evidenced** | **P01** (down payment), P08 (payroll) | **OPEN** |
| `TZ-12` | Any internal user can create a vendor bill through a `sudo()` wizard — *unauthorised posting* | **CONFIRMED** — source | `scgl_purchase_advance_payment/security/ir.model.access.csv:2`; `wizard/purchase_advance.py:203` | COMPANY | **LIVE in 4 of 4** distinct databases evidenced | **P01** | **OPEN** |
| `TZ-13` | The only universally available advance-clearing route books a bank receipt that never occurred | **CONFIRMED** — source | `wizard/advance_request_reconcile.py:62-92` | COMPANY | **LATENT** | P06 | **OPEN** |

## 4. Reach Summary

| Reach | Boundaries |
|---|---|
| **LIVE in an evidenced deployment** | `TZ-03`, `TZ-04`, `TZ-06` (partly), `TZ-09`, `TZ-10`, `TZ-11`, `TZ-12` — **7** |
| **LATENT** (defect confirmed, module installed nowhere evidenced) | `TZ-01`, `TZ-02`, `TZ-05`, `TZ-07`, `TZ-13` — **5**, plus `TZ-08` via its P05 trigger |
| **Closed** | **0** |

## 5. The Reach Inversion — and what it does NOT mean

> **Read `§2`'s accepted challenge first.** What follows re-ranks findings by *operational risk in a
> running system*. It does **not** re-rank them by *relevance to what SMEsPlus should build* — on that
> axis the `LATENT` findings rank at least as high, because they are defects the clean-room design can
> still avoid inheriting. A reader using this section to decide **build scope** rather than
> **remediation scope** is using the wrong axis.

The module evidence inverts the package's own severity ranking, and that is worth stating plainly
rather than leaving implicit in a table:

- The two findings the package led with — `TZ-01` (petty cash) and the employee-advance chain
  (`TZ-05`, `TZ-07`, `TZ-13`) — are **latent**. They are real defects in code that **no evidenced
  deployment runs**.
- The findings the package reported almost in passing, in territory it explicitly declined to
  adjudicate — `TZ-11`'s down-payment leg and `TZ-12`, both in `scgl_purchase_advance_payment` — are
  **live in every one of the five real business databases**, and both are P01's to own.

> **Correction affecting this section (`39 RE-10`, `RE-11`).** An earlier draft cited the withholding
> certificate findings at figures that independent review contradicted. The corrected position: one
> exact duplicate certificate exists in 5,201, not 32; and the certificate's printed date is sound —
> the defect is on a differently-named column. Neither correction changes the reach classification
> above, and neither adds or removes a tolerance-zero boundary. Recorded because the figures appear
> in `30` and `33`.

The most consequential P05 output for the programme is therefore a **peer handoff**, not a P05
finding. Recorded in `30` and escalated in `37 §2`.

## 6. What Would Close a Boundary

No boundary closes on deployment evidence. Each closes only on one of:

| Boundary | Closure condition |
|---|---|
| `TZ-01`, `TZ-02`, `TZ-05`, `TZ-07`, `TZ-13` | a SMEsPlus design position that does not reproduce the defect, ratified by Boss — these are *design* closures, not evidence closures, because the reference behaviour is already fully evidenced |
| `TZ-03`, `TZ-04`, `TZ-09`, `TZ-10` | same, plus a control whose executor is proven (`17 §6 DI-12`) |
| `TZ-06` | a cost-event-keyed duplicate control (`17 §6 DI-08`) |
| `TZ-08` | **P08's** decision on core journal immutability — not P05's to close |
| `TZ-11`, `TZ-12` | **P01's** decision — not P05's to close |
