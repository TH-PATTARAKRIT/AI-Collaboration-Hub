# P07 — DOMAIN PURITY AND BOUNDARY REGISTER

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
Mandated by prompt §9 and `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1 §9`.

> **PHASE S = DOMAIN PURITY FIRST.** P07 is shared in the ERP; its learning is not. This file
> records every point at which this round touched another domain, what it took, and where it
> stopped. A boundary that is only asserted is not a boundary — each row names the stop.

## 1. The Five Purity Tests, Applied To Every Material Finding

Prompt §9 defines them. Applied here to the seven findings this round produced.

| finding | 1. P07 fact or another Pxx's workflow? | 2. Stated from the minimum interface fact? | 3. Operational ownership inferred from tax consequence? | 4. Tax timing inferred from posting timing? | 5. Statute inferred from implementation? |
|---|---|---|---|---|---|
| `P07-F-105` no tax-point carrier in the localisation | **P07** — the Thai localisation set is P07's surface | yes — states only what the set contains | no | no — it states that no timing carrier exists, which is the opposite inference | no statutory claim made |
| `P07-F-106` localisation count is 10/10/10/10/9/9/1 | **P07** | yes | no | n/a | no |
| `P07-F-107` item-level carrier present, contradicting P10 | **P07** — tax-period membership is `O-03` | yes — schema presence and module ownership only; **no recognition behaviour examined** | no | no | no |
| `P07-F-108` two bodies disagree on `_compute_wht_amount` | **P07** — `l10n_th_withholding_tax` is P07's module | yes | no | n/a | **no** — a defect is not a statutory statement |
| `P07-F-109` 199 of 1,186 stored values diverge | **P07** | yes | no | n/a | no |
| `P07-F-110` the only consumer is uninstalled | **P07** | yes | no | n/a | no |
| `P07-F-111` four computations, three bases | **P07** | yes | no | n/a | no |

**Test 5 is the one this package has to watch hardest**, because a tax package that finds a
defect is one sentence away from calling the correct behaviour a statutory requirement. **No
finding this round states what Thai law requires.** Every statutory question raised is routed to
the `UNRESOLVED — EVIDENCE REQUIRED` register, not answered.

## 2. Contamination Stops — Where a Path Was Cut

| # | Path that opened | Domain it entered | What P07 kept | What P07 refused | Classification |
|---|---|---|---|---|---|
| `DPB-01` | `Q07-1`…`Q07-3` require knowing whether localisation alters **recognition** | **P10** internals | The localisation set's complete `_name`/`_inherit`/field footprint — read **from the localisation modules only** | Reading the recognition engine, the deferral entries, or how a deferred schedule is generated. **The question was answered from P07's own surface, and the recognition side was never opened.** | `EXTERNAL DOMAIN BOUNDARY — minimum interface fact retained` |
| `DPB-02` | `deferred_start_date` / `deferred_end_date` observed on `account_move_line` in 6 of 7 identities, and **absent in the v16 identity that has `tax_period_date`** | **P10** internals | The schema fact and its per-identity distribution, forwarded to P10 as an interface fact | Any interpretation of what the fields do, when they are written, or what a deferred schedule looks like | `EXTERNAL DOMAIN BOUNDARY — routed to P10` |
| `DPB-03` | `X-07`/`X-08`/`X-09` need the settlement event's date, allocation and reversal | **P06** internals | P06's four published commitments `P07-R-01`…`P07-R-04`, consumed as **stated requirements** | Bank matching, reconciliation internals, the returned-payment lifecycle, `action_reject`'s implementation. **P06's own words were consumed; P06's code was not read.** | `EXTERNAL DOMAIN BOUNDARY — peer position consumed as input` |
| `DPB-04` | `MD-05` — two mutually-unaware custom WHT subsystems mutate the settled amount | **P06** / shared | The interface fact that two subsystems act on one payment event, corroborating `DUP-03` | Investigating either subsystem's interference. `P07-U-30` already holds P07's half and **was not re-opened**, because no delta changes its value | `DOMAIN CONTAMINATION AVOIDED — existing P07 item unchanged` |
| `DPB-05` | `wht_amount`'s only consumer is a **payment remittance advice** document | **P06** / document production | The install state of the module — a one-field registry read | The remittance process, its workflow, its approvals | `EXTERNAL DOMAIN BOUNDARY — minimum interface fact retained` |
| `DPB-06` | `PX-06` — may a filed period change at all? | **statute**, plus P08's period lock | The mechanism half: no tax-period state exists; the only control is the accounting lock | Designing a tax-period state; asserting what statute permits | `BOSS DECISION REQUIRED` |
| `DPB-07` | `L-1` needs a business-event date on the tax fact | **P02 / Inventory** | The requirement `CRL-01`, stated as a need | Delivery mechanics, ownership-transfer modelling, stock moves. **Boss policy preserved: WHT belongs to Accounting and is not an Inventory stock-move function.** | `EXTERNAL DOMAIN BOUNDARY — requirement stated, not designed` |
| `DPB-08` | `l10n_th_google_fonts` installed and not present under either declared root | none — it is a **residue**, not a domain | The declared gap, `P07-U-34` | Widening the source population to find it. That would broaden scope, which closure forbids | `IN-SCOPE RESIDUE — declared, not chased` |

**Eight stops. Five were another Pxx's, one was statute, one was Boss's, one was a residue.**

## 3. Scope Classification Before Claiming a Scope Rule — `CQ-P07-08`

`SMEPLUS-26-09-04-ACC-REV2-CORR1` requires PLATFORM / TENANT / COMPANY to be **determined**, not
blanket-applied. Every material fact this round produced, classified:

| fact | scope | why, and why not the others |
|---|---|---|
| The installed Thai localisation **set** | **PLATFORM** | It is a property of the deployment's code, identical for every company and every tenant inside one database. Nine-or-ten is a platform fact, not a company one — which is exactly why P10's two figures were both right. |
| `account.move.tax_period` / `account.move.line.tax_period_date` **existence** | **PLATFORM** | schema presence follows module install |
| A **value** in either carrier | **COMPANY** | a tax period belongs to a filing unit |
| `res.company.branch` | **COMPANY** | the filing unit / place of business — `R-B-04` |
| `res.partner.branch`, `l10n_th_branch_name` | **TENANT** | counterparty master data — and the two are **used interchangeably with the COMPANY-scope field by the statutory reports**, which is `P07-F-06` / `P07-C-02`, unchanged |
| `account.move.wht_amount` and its divergence | **COMPANY** | a withholding obligation is a company's; the divergence was measured within one identity and is not aggregated across companies |
| The four withholding computations | **PLATFORM** | code, not data |
| Which code body is deployed (`P07-U-01`) | **PLATFORM** | and it is **not decidable from any data at any scope** |

**No fact was forced to TENANT + COMPANY.** Two are PLATFORM-only, and saying so is what let
`MD-02` resolve: a platform fact counted per database yields different numbers per database
without any of them being wrong.

## 4. What P07 Did **Not** Learn, By Design

Recorded so a later reader does not mistake silence for coverage.

- **How deferred recognition works.** Not read. `Q07-1`…`Q07-3` were answered from the
  localisation side only, and the answer is bounded to that side.
- **How bank reconciliation, matching or the returned-payment lifecycle work.** Not read.
- **Whether P06's committed requirements are implementable.** Not assessed — that is P06's.
- **Whether the recognition entry's tax-period behaviour is correct.** `Q07-4` was answered at
  **schema and module-ownership level only**; behaviour is untested, exactly as P10 bounded its
  own claim.
- **Anything about P01, P02, P03, P04, P05, P08, P09, P11, Inventory, Manufacturing, Asset,
  Equipment or Maintenance internals.** No file from any of those domains was opened this round.

## 5. Boundary Integrity Check

| check | result |
|---|---|
| Did any evidence pass read a non-P07 module's implementation? | **No.** `POP-SRC` was restricted to the 11 installed `l10n_th*` names plus the two files carrying `wht_amount`'s definition and readers. The `02 OTHER` base tree was touched **once**, for a positive control, and its content was not interpreted. |
| Did any finding state a rule about another process? | **No.** `CRL-01`…`CRL-05` are stated as requirements **on P07's own inputs**, naming the owner without specifying the owner's design. |
| Did any peer's unresolved item get promoted to a boundary here? | **No.** `MD-06` is explicitly not acted on. P06's `X-09` statutory hold is recorded as a hold, not adopted as a rule. |
| Was any peer decision treated as a Boss decision? | **No.** `P07-R-01`…`P07-R-04` are recorded as **P06 commitments**, and `PX-06` is `BOSS DECISION REQUIRED`. |
