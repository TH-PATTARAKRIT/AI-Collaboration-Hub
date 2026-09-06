# P07 — CORRECTION / REVERSAL LINEAGE MATRIX

Round `SMEPLUS-26-09-06-…-002`. `LAYER 2 — AUDIT QUARANTINE`.
Answers `CQ-P07-05` and `CQ-P07-07`. Deepens `08_P07_CORRECTION_ADJUSTMENT_MATRIX.md`.

> `CQ-P07-07` asks whether a tax-relevant correction can be traced to the originating business
> fact **and** to the downstream statutory result **without silent divergence or double
> counting**. The answer is **no**, and this file states exactly where the chain breaks.

## 1. The Lineage a Tax Correction Must Preserve

| link | from | to | must survive because |
|---|---|---|---|
| `L-1` | originating business event | tax fact | the tax point is a property of the business event (`S-01`, `S-02`, `S-30`) |
| `L-2` | tax fact | statutory document (tax invoice, credit/debit note, WHT certificate) | `S-19`, `S-20`, `S-31` |
| `L-3` | statutory document | the return it was reported on | reconciliation of a filed figure to its constituents |
| `L-4` | correction event | the fact it corrects | so a correction supersedes rather than erases |
| `L-5` | correction event | the **period** it belongs to | `S-13`, `S-14` place a note in the month of issue, not the month of the original |

## 2. Where Each Link Stands

| link | state | evidence | class |
|---|---|---|---|
| `L-1` | **BROKEN.** No carrier for the business-event date on the tax fact | `D-1` in the date matrix; `X-04`, `X-05` | `FACT VERIFIED` |
| `L-2` | **PARTIAL.** WHT certificate links to the payment (`wt_cert_ids` on `account.payment` and on `account.move`); the tax invoice has **no document identity P07 can supply** (`DOC-01`) | `EP-4b` field table; `05` | `FACT VERIFIED` |
| `L-3` | **ABSENT.** No filed figure is stored anywhere. Every statutory output is a **render over live master data**; there is no return artefact to trace back to | `07`, `A-15` | `FACT VERIFIED` |
| `L-4` | **ABSENT on the payment side.** P06 states reversal linkage does not exist: `action_reject` is a bare state write with no cause, no reference and no unwind | `PI-02` §4 (`RPL-F-01`) | `FACT VERIFIED` **by P06**, consumed as an interface fact |
| `L-5` | **BROKEN.** A note is placed by the accounting date of the reversal entry, not by its own issue date | `PX-04`, `P07-F-07` | `FACT VERIFIED` |

**Three of five links are absent and two are broken. `CQ-P07-07`'s answer is that the chain
does not exist end to end** — and the most consequential of the five is `L-3`, because **nothing
records what was filed**, so no correction can be measured against it.

## 3. Silent Divergence — Measured

`CQ-P07-07` names *silent divergence* explicitly. This round measured one instance.

**`P07-F-109`.** In identity `45a8e08e`, **199 of 1,186** stored withholding amounts (16.8%)
disagree with the amount recomputable from the move's own withholding lines, and **7** store a
non-zero withholding amount while carrying **no withholding-tax line at all**. Instrument
validated by 980 exact reproductions.

**And it is latent in effect.** `P07-F-110`: the only consumer of the stored value —
`print_payment_remittance_adviec` — is uninstalled in 6 of 7 identities and absent from the
seventh's registry. Every other site recomputes. **A stored, exercised, divergent statutory
figure that nothing installed reads.**

**The cause is not decidable.** `P07-F-108` establishes that the two candidate code bodies
disagree on `_compute_wht_amount` — one writes `rec.wht_amount`, the other writes
`self.wht_amount` inside the loop, both `store=True`. Whether the divergence is that defect or
ordinary staleness after line edits **cannot be settled from a database**, which records the
result of a write and never the sequence. `P07-U-35`, class `EVIDENCE NEVER RECORDED`.

**Why it belongs in this file even though it is latent.** `L-4` requires that a correction
supersede rather than overwrite. A `store=True` compute **overwrites in place, with no prior
value and no event**. Whatever caused the 199, the mechanism has no lineage by construction:
there is nothing to trace, because the field keeps only its latest value.

## 4. Double Counting — The Four-Computation Problem

`P07-F-111`: one statutory number is computed in **four** independent places over **three**
different bases, two of them in the same file 35 lines apart (`P07_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md §8`).

For `CQ-P07-07` the point is not that four sites exist — it is that **no two of them can be
reconciled to each other**, because none records which inputs it used. A discrepancy between the
PND figure and the voucher figure is, today, **undiagnosable after the fact**.

Whether branches 1 and 2 can actually differ — i.e. whether `tax_base_amount` and
`price_subtotal` diverge on a withholding line — is **not tested**. `P07-U-36`, `NOT YET READ`.
It is named rather than assumed in either direction.

## 5. Document Lifecycle States — `CQ-P07-05`

What the estate models, from `EP-4b` and `05`:

| state | tax invoice | credit / debit note | WHT certificate |
|---|---|---|---|
| create | yes | yes | yes — `create.withholding.tax.cert` wizard |
| issue | **not distinguished from create** | not distinguished | not distinguished |
| cancel | no explicit state | reversal entry | **`wt_cert_cancel` Boolean** on `account.move` and `account.payment` |
| reissue / replace | **not modelled** | not modelled | **not modelled** |
| correct | not modelled | the note *is* the correction | not modelled |

**`wt_cert_cancel` is a Boolean.** A cancelled certificate is therefore recorded as a flag on
the payment, **not as an event with a date, a cause and a successor.** For `S-31` purposes a
certificate that was issued, cancelled and reissued is indistinguishable from one that was
never issued — the flag carries no history.

**Duplicate-copy tax invoice** (`ใบแทน`) remains `P07-U-13`: number and date are computed, the
duplicate is not modelled. Unchanged this round; no delta touched it.

## 6. What Would Close `CQ-P07-07`

Stated as evidence requirements, not as a design — `PHASE S` discovers, `PHASE B` contracts.

| # | Requirement | Blocked by |
|---|---|---|
| `CRL-01` | Every tax fact carries an immutable reference to the business event that created it | `L-1`; `X-04`, `X-05` — **P02/Inventory owned, not P07's to build** |
| `CRL-02` | A filed figure is **stored**, not rendered, so a later correction has something to differ from | `L-3` — and this is the single largest structural gap in the P07 surface |
| `CRL-03` | A correction is a new event linked to what it corrects, carrying its own date and cause | `L-4` — **P06 has committed this as `P07-R-03`**; the P07 half is that the tax layer must consume the link |
| `CRL-04` | A tax-relevant stored figure is never overwritten in place by a recompute | `P07-F-108`, `P07-F-109` |
| `CRL-05` | One definition of the withholding amount, consumed by every site | `P07-F-111` |
