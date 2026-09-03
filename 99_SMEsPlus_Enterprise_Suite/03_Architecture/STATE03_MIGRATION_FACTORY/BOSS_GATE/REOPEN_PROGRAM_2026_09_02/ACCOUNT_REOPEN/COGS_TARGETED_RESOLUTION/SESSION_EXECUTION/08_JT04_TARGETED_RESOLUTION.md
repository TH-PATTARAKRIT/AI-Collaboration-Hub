# 08 — JT-04 Targeted Resolution: COGS Recognition Timing

Source fact package: Fact Verification session file `09_JT04_FACT_PACKAGE.md`. This file adds nothing new evidentially (no new tool access this session — file `01` §2) and instead performs the classification the priority order requires: DECIDABLE / DECIDABLE WITH CONTROL / NOT DECIDABLE.

## 1. What Is Known (cited)

- The reference ERP has two mutually exclusive, version-attributed recognition rules: delivery-triggered (pre-19) and invoice/bill-triggered (19.0+), corroborated across ≥7 DR research files (Fact Verification file `09` §1).
- Invoicing-policy interaction with this trigger table is undocumented (`CGS-U20`).
- Invoice-before-delivery matching-principle risk is unresolved (`CGS-U31`).
- No evidence exists that Thai TAS 2 mandates a specific trigger event, as distinct from requiring eventual cost-revenue matching (`TH-NEW-01`, unresearched).
- No business-stakeholder answer exists yet on SMEsPlus's actual invoice/delivery sequencing pattern (`SME-Q-03`, unanswered).

## 2. What Is Genuinely Unknown

Which single event (or configuration-dependent set of events) SMEsPlus itself will use to recognize COGS, and whether that choice needs a matching-principle control for invoice-before-delivery cases.

## 3. Classification of the Unknown Itself

`JT-04` is a **DESIGN DECISION** with a **BUSINESS POLICY** input (SME-Q-03) and a possible **STATUTORY REQUIREMENT** constraint (TH-NEW-01, unresearched — could narrow but not by itself decide the choice). It is not a pure FACT question and never was; the reference-ERP instability is the fact, not the answer.

## 4. Evidence That Would Resolve It

1. `SME-Q-03` answered by a business stakeholder (invoice/delivery sequencing pattern).
2. `TH-NEW-01` researched (does TAS 2 constrain the trigger event).
3. `CGS-U20`/`CGS-U31` re-fetched (whether reference ERP itself gates invoice-before-delivery).

None of these three is available this session (no live SME, no Thai statutory database access, no working documentation-fetch tool this session — file `01` §2).

## 5. Owner

- `SME-Q-03` → Business SME.
- `TH-NEW-01` → Thai Accounting-Tax research track.
- `CGS-U20`/`CGS-U31` → Docs/Research owner (bounded re-fetch task, technical not a ruling).
- Final event selection → **Boss**, informed by the above but not derivable from them alone.

## 6. Can It Be Parallelized?

Yes. `SME-Q-03` and `TH-NEW-01` are independent of each other and of the `CGS-U20`/`CGS-U31` re-fetch; all three can run concurrently. None blocks the others from starting.

## 7. Does It Block a Gate?

Yes — `JT-04` is one of the two named priority Joint Decisions and gates any Boss Account Ruling that depends on COGS recognition timing, and gates finalization of any COGS posting model in Inventory v2.0 (see file `17`).

## 8. Disposition: NOT DECIDABLE

**NOT DECIDABLE this session.** Missing, named:
- Business SME input (`SME-Q-03`) — not available this session (no live stakeholder).
- Thai statutory input (`TH-NEW-01`) — not available this session (no statutory database access).
- A bounded technical re-fetch (`CGS-U20`, `CGS-U31`) — not available this session (no working live-fetch tool confirmed this session).

This session considered whether `JT-04` could be classified **DECIDABLE WITH CONTROL** — i.e., decidable now if SMEsPlus simply adopts a specific control (for example: "recognize at delivery always, and hard-block invoice-before-delivery"). It rejected this because (a) `SME-Q-03`'s answer is unknown, so it is not established that delivery-before-invoice is even SMEsPlus's actual operating pattern — adopting a control that fights the real business process without knowing what that process is would be designing blind, and (b) whether TAS 2 permits or requires a specific event is untested. Proposing a control without either input would be inventing a policy, which this session's mandate forbids. **NOT DECIDABLE** is the honest classification; **DECIDABLE WITH CONTROL** would require at minimum the `SME-Q-03` answer first.

## 9. One-Line Reason (for the final report)

Reference-ERP has two contradictory recognition-timing behaviors by version, no live SME input on SMEsPlus's own invoice/delivery sequence, and no Thai-statutory test of whether TAS 2 constrains the trigger event — three independent missing inputs, none available this session.
