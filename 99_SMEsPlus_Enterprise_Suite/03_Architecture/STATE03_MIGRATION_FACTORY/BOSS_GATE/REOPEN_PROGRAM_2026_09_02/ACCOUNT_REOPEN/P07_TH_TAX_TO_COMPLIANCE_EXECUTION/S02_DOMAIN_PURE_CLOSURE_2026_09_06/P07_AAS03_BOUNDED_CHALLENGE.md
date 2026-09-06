# P07 — AAS-03 BOUNDED INDEPENDENT CHALLENGE

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
Four perspectives, per prompt §11 and `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1 §10`.

> **No expert self-declares PASS or FAIL. Challenge output is evidence pressure, not a verdict.
> Disagreement is preserved, not reconciled away.** At least one challenge actively attempts to
> disprove the round's most consequential conclusion; `CH-B` does, and **it partly succeeded and
> then failed on measurement** — the record of both is below.

## 1. `CH-A` — Leader Functional Design

**Supported.** `P07-F-105` is the strongest statement `O-03` has ever had, and it is the right
shape: it says what the localisation *contains*, not what it *does*. `P07-F-106`'s "two
denominators, not a discrepancy" is correct and generalises. The `CH-01`…`CH-06` handoff rows
correctly separate *probable consumer* from *designated consumer*.

**Missing.** The pack has **no candidate for the tax event itself** as a first-class object.
Every row is an attribute of a document. If `CRL-01`…`CRL-05` are right, the missing object is
*the tax fact*, and PHASE B will not find it in this pack.

**Risky.** `PS-08` and `PS-09` are `DESIGN CANDIDATE — PHASE S ONLY`, and they are one sentence
from being read as recommendations. A reader who wants a tax-period state will find two rows
here that look like a specification.

**Challenged — and this one lands.** **`P07-F-105` says "no carrier". It has measured "no *new*
carrier".** A tax point does not need a new field: it could ride on `invoice_date`, which the
localisation *uses* and does not add. The instrument counted **fields added**; it did not test
**fields consumed for period placement**.
→ **Accepted. `P07-F-105` is restated in the register as: the installed Thai localisation set
adds no date, period or tax-point field. It does not establish that the set is indifferent to
period placement** — that is a separate question, and `04 §4` already answers it for the report
layer (the substitution was removed).

**Evidence needed next.** Which attribute each statutory output *reads* for period placement,
per output, over the installed set — a read-side census to sit beside this round's write-side one.

## 2. `CH-B` — Leadership Database Design

*This is the challenge instructed to attempt disproof of the round's most consequential new
conclusion: `P07-F-109`, that a stored statutory figure disagrees with its transaction in 16.8%
of the exercised population.*

**Supported.** `EP-3`/`EP-4a` agreeing by two routes — schema columns and module registry — is
the right standard for `P07-F-107`, and it is why that contradiction of a peer can be published.
The `POP-DB` keying on `database.uuid` and never on filename is correct.

**Missing.** `EP-6` reads one snapshot per identity. A snapshot is a **point in time**; a
divergence measured in one snapshot says nothing about when it arose. No time series was taken
and none is claimed.

**Risky.** `EP-3` infers schema from a dump's `COPY` header. That is the dumped table's column
list, which is the schema — but it is a **restore artefact**, and a column excluded by the dump
would be invisible. No evidence suggests exclusion here; the risk is named, not dismissed.

**Challenged — the disproof attempt.**
> *The 199 mismatches need no defect. `EP-6` recomputes with the **current** rate on
> `account_withholding_tax`. If any rate was edited after posting, every move computed under the
> old rate mismatches. One rate edit could produce all 199, and `P07-F-109` would be an artefact
> of the instrument, not a property of the data.*

**This was taken seriously and measured rather than argued** (`EP-6b`). Split of the 199 by
whether the confound *can* apply:

| class | definition | count | can a rate edit explain it? |
|---|---|---:|---|
| `Z` | the move's own lines carry **no `wt_tax_id` at all**, yet a non-zero amount is stored | **151** | **No.** There is no rate to have changed. |
| `R` | own-lines value non-zero and different from stored | **48** | Possibly |

And within class `R`, a single rate edit predicts **one dominant `stored ÷ own` ratio** shared by
nearly all 48. Observed: **no dominant ratio** — the most frequent occurs 3 times, and the values
(1.4537, 1.4531, 1.5629, 2.6524, 0.8859…) correspond to no ratio between any two rates that
exist in the table (`0, 0.5, 1, 2, 5, 10, 15`).

→ **The challenge failed on measurement, and the finding is stronger for having faced it.**
**76% of the divergence cannot be a rate edit, and the remaining 24% does not have a rate edit's
signature.** `P07-F-109` stands, and now stands with its most plausible alternative explanation
tested and excluded rather than merely acknowledged.

**Where `CH-B` still disagrees, and it is not withdrawn.** The dominant class is `Z` — *stored
amount, no withholding line*. That is equally consistent with the `<B>` compute defect **and**
with lines having been edited after the last recompute. **`CH-B` does not accept that
`P07-F-108` is the explanation, and `P07-F-109` does not claim it is.** The cause stays
`P07-U-35`, `EVIDENCE NEVER RECORDED`.

**Evidence needed next.** A controlled execution: post two moves with withholding in one batch,
recompute, read both stored values. Ten minutes on a scratch database, and it settles
`P07-U-20`, `P07-U-29` and `P07-U-35` in one sitting. **Not authorised in this phase.**

## 3. `CH-C` — Lead Integration & Localization

**Supported.** Executing P10's question rather than inheriting either of its numbers was right,
and `P07-F-106` shows why: the reconciliation P10 asked for did not exist to be done.
`P07_TO_P10_HANDOFF.md` carries question, evidence and bound, per `REV-M-95`.

**Missing.** The **read-side** of localisation. The round established what the Thai localisation
*writes*; a localisation can bind a process by what it *reads* — a report that filters on a field
constrains every producer of that field.

**Risky.** `l10n_th_google_fonts` (`P07-U-34`) is declared and dismissed by name. **A name is not
a manifest.** It is a small risk and it is a real one.

**Challenged — and this is the sharpest point of the round.**
> *The search population was `l10n_th*`. **The estate's actual tax-timing code is not in it.**
> `scgl_tax_period_date` — the module that owns both tax-period carriers — has no `l10n_` prefix
> and would not have been found by the pattern that produced `P07-F-105`. So the pattern used to
> establish what "the Thai localisation" contains is provably not the pattern that finds Thai tax
> code in this estate.*

→ **Accepted, and it is a limit on the scope of the claim rather than on its truth.**
`P07-F-105` is a statement about **the installed Thai localisation set**, established from
`ir_module_module`, and it is true of that set. It is **not** a statement about Thai tax code in
the estate, and it must never be read as one — the round's own `EP-3`/`EP-4a` found the tax-period
carrier **outside** that set, which is the counter-example proving the distinction matters.
Recorded against `P07-F-105` as a binding scope note.

**And it corrects a second thing.** `EP-1`'s widening control reported *"no installed name carries
a bare `th` token outside `l10n_`"* as evidence the prefix was not narrowing. **That control was
answering the wrong question**: `scgl_tax_period_date` carries no `th` token either. The control
proved the prefix captured every module *named* Thai, not every module *doing* Thai tax.

**Evidence needed next.** A capability-based rather than name-based population for "Thai tax code":
modules declaring on `account.tax`, `account.tax.group`, the PND handlers, or the tax-period
carriers, whatever their name. `P07-F-83` already does this for six models over three identities —
**extending it is the shortest path**, and it is not opened here because no declared Closure
Question is denominated over it.

## 4. `CH-D` — Lead Code & UI Architect

**Supported.** `P07-F-108`'s reading of the code is correct and unambiguous: `self.wht_amount`
inside `for rec in self:` with `store=True`. The two copies were hashed, not eyeballed.

**Missing.** No test of whether the ORM ever calls this compute with more than one record. The
finding asserts the consequence *if* it does.

**Risky.** `P07-F-110` calls the divergence **latent** because no installed module reads the
stored value. **Latent is not harmless.** The field is stored, it is queryable, and any future
report, export, dashboard or integration that reads `account.move.wht_amount` inherits a 16.8%
error with no warning. `P07-F-110` is correct today and is a statement with a short shelf life.

**Challenged.**
> *`P07-F-108`'s severity is conditional on multi-record recompute being **common**, and the
> round treats that as self-evident. If the ORM recomputes one record at a time, the defect never
> fires and `S2` is too high.*

→ **Partly accepted, and it cuts the other way on the facts available.** The field's trigger is
`@api.depends("invoice_line_ids")`, and stored computes are flushed in batches over every record
marked dirty — so a multi-record call is the ordinary case for an import, a batch confirm or any
write touching several moves' lines, not an exotic one. **That reasoning is `SUPPORTED
INTERPRETATION`, not `FACT`**, because no execution was observed; it is recorded as the basis for
`S2` and a reader may weigh it down.

**A UI observation that explains the survival of the defect.** `l10n_th_withholding_tax/views/
account_move_view.xml:39` declares `<field name="wht_amount" invisible="1"/>`. **The field is
stored, computed, divergent in 16.8% of cases, and never shown to a user.** A wrong number nobody
can see is a wrong number nobody reports.

**Evidence needed next.** The controlled two-record execution from `CH-B`. One run answers
`CH-B`'s cause question and `CH-D`'s frequency question together.

## 5. Mandatory Falsification Attempts — All Eight, With Outcomes

| # | Attempt | Outcome |
|---|---|---|
| 1 | **Wrong tax-event owner** | Tested against `10 §4`. `O-01`…`O-07` unchanged; nothing this round claims ownership of an event P07 does not own. **No falsification.** |
| 2 | **Wrong event/date/period semantics** | `CH-A` landed: `P07-F-105` measured *new carriers*, not *period placement*. **Claim narrowed.** |
| 3 | **Implementation behaviour mistaken for Thai statutory requirement** | Every statutory question this round raised (`Q07-5`, `PX-05`, `PX-06`, `CI-14`) was routed to `UNRESOLVED` or `BOSS DECISION REQUIRED`. **No statutory claim was made from behaviour. No falsification.** |
| 4 | **Duplicate tax fact / duplicate certificate / replay risk** | **Confirmed, not falsified.** `P07-F-109`: 199 divergences, 151 of them a stored amount with no line to justify it. `wt_cert_cancel` is a Boolean, so an issued-cancelled-reissued certificate is indistinguishable from a first issue. |
| 5 | **Correction / reversal lineage break** | **Confirmed.** Three of five lineage links absent, two broken. `L-3` — no filed figure is stored — is the structural one. |
| 6 | **Company / legal-entity scope leakage** | **Confirmed and corroborated at field level**: one module defines `branch` on both `res.company` (COMPANY) and `res.partner` (TENANT), and a fourth representation exists beside them. `P07-F-06` unchanged. |
| 7 | **Source-present vs installed vs configured vs exercised** | **Applied and it changed two results.** `print_payment_remittance_adviec` is source-present and **uninstalled** → `P07-F-110`. `wht_amount` is installed **and exercised** (1,186 non-zero) → `P07-F-109` is not latent as data, only as consumption. `REV-E-94`. |
| 8 | **Unsupported negative claim** | Attacked hardest. `P07-F-105`'s zero has two independent instruments, a firing positive control, a failure control, and a **declared residue** (`P07-U-34`). `CH-C` then narrowed its *scope* rather than its truth. **The negative survives as bounded; it does not survive as a general statement, and it is not published as one.** |

## 6. Disagreements Preserved

| # | Between | The disagreement |
|---|---|---|
| `DIS-01` | `CH-B` and the round | `CH-B` does **not** accept `P07-F-108` as the explanation of `P07-F-109`, having excluded only the rate-edit alternative. The round agrees and claims no cause. **Recorded as agreement on the limit, not on the answer.** |
| `DIS-02` | `CH-D` and `P07-F-110` | `CH-D` holds that *latent* understates the risk of a stored, queryable, invisible wrong figure. `P07-F-110` reports install state and takes no position on future consumers. **Both stand.** |
| `DIS-03` | `CH-C` and `EP-1`'s widening control | `CH-C` holds the control answered the wrong question. **Accepted; the control is recorded as insufficient rather than deleted.** |
| `DIS-04` | `CH-A` and `PS-08`/`PS-09` | `CH-A` holds two `DESIGN CANDIDATE` rows read as recommendations. They are retained with the class, because deleting them would lose the discovery. **Unresolved by design.** |
