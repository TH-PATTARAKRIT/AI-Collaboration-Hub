# P07 — MATERIAL DELTA AND PEER INPUT REGISTER

Round: `SMEPLUS-26-09-06-P07-TH-TAX-SHARED-DOMAIN-PURE-CLOSURE-002`
Branch: `research/account-p07-th-tax-compliance-2026-09-04-001`
Baseline before this round: `3548b343c3baa70817905661a264b457a78635e8`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Governance: `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1_2026_09_06` @ `48ee264`

> **This round exists because peers published, not because P07 wanted another look.**
> No Material Delta = No Additional Research Round. Every evidence pass below is traceable to
> a delta named here, and nothing else was searched.

## 1. Controlled Peer Inputs Consumed

Only **published, verified** peer artefacts at the commits the issuing prompt names. No
in-flight P05 or P06 continuation work was consumed, and none was waited for.

| ID | Source | Commit | Artefact | Consumed as |
|---|---|---|---|---|
| `PI-01` | P10 Time-Based Recognition, G02 closure | `1fea562` | `P10_TO_P07_HANDOFF.md` | Five questions `Q07-1`…`Q07-5`, one unreconciled count, one negative that may not be written |
| `PI-02` | P06 Bank-to-Reconcile, published baseline | `9e5d729` | `54_P06_P07_BLOCKING_DEPENDENCY_MATRIX.md` | Four committed requirements `P07-R-01`…`P07-R-04`; adjudication of `X-07`, `X-08`, `X-09` |
| `PI-03` | Parallel Business Process Program | `48ee264` | `COMMON_CLOSURE_EXECUTION_CONSTITUTION_V1` | Execution governance for this round |

**Not consumed, and why.** P04's published G01 closure (`65b8841`) contains **no file naming
P07** and no handoff addressed here; the P04 exchange of the previous round is already in
`21_P07_PEER_EVIDENCE_INTAKE_P04.md`. P05 is active in parallel and **unpublished** — nothing
from it is read. P01 remains unpublished, which is why `DUP-01` stays unreconcilable by anyone.

### 1.1 Identifier attribution — families that are not P07's to renumber

Two identifier families appear in this round that **P07 did not create**. They are recorded
here so the package's orphan check does not read them as undefined P07 identifiers, and so no
reader mistakes a peer's authorship for this package's.

| Family | Author | Meaning here |
|---|---|---|
| `Q07-1`…`Q07-5` | **P10**, in `PI-01` | Questions P10 asks of P07. Answered below; the numbering stays P10's. |
| `P07-R-01`…`P07-R-04` | **P06**, in `PI-02` | Requirements P06 **commits to supply**. The `P07-` prefix is P06's choice, not this package's issue; they are P06 obligations, not P07 findings. |
| `MD-01`…`MD-06` | this round | Material deltas, defined in §2. |
| `EP-1`…`EP-6` | this round | Bounded evidence passes, declared in `P07_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md`. |

*Rename what is yours, attribute what is inherited.* Neither family is renumbered.

## 2. Material Delta Test — What Actually Changed

A delta is material only if it can change a declared Closure Question's answer or a gate.
Everything else is Class E and does not open a search.

| ID | Delta | Class | CQ affected | Material? |
|---|---|---|---|---|
| `MD-01` | P10 states *"localisation modules do not alter time-based recognition"* is **`C — NOT SEARCHED` and must not be written by anyone, including P07**, over a nine-module Thai estate | **A** — in-scope derived subquestion | `CQ-P07-02` | **YES.** The localisation surface is P07's own; the question is answerable here and nowhere else. |
| `MD-02` | P10 records **nine** localisation modules in two documents and **ten** in a third, unreconciled (`G02-R-17`), and asks P07 to establish the count from the manifests | **A** | `CQ-P07-08`, `CQ-P07-10` | **YES.** A denominator disagreement inside a peer's own lineage. |
| `MD-03` | P10 asserts `FACT VERIFIED`: *a tax-period carrier exists on the entry and is **absent from the item**, deployed 19.0+e* | **B** — same-scope material contradiction | `CQ-P07-02` | **YES.** P07 owns tax-period membership (`O-03`) and holds contrary evidence in `04 §3`. |
| `MD-04` | P06 publishes `P07-R-01`…`P07-R-04` as requirements it **commits to supply**, closing the P06 half of `X-07`, `X-08`, `X-09` | **A** | `CQ-P07-02`, `CQ-P07-04`, `CQ-P07-07` | **YES.** Three items carried as `BLOCKING for P07` for two rounds now have a named counterparty commitment. |
| `MD-05` | P06 confirms `DUP-03` from its own evidence (`P06-B-13`: two mutually-unaware custom WHT subsystems mutate the settled amount) | **A** | `CQ-P07-04` | **YES.** Independent corroboration of a P07 duplicate-ownership risk. |
| `MD-06` | P06 records `X-09` as carrying a **hard statutory component** on which P06, P07 and P05 independently hold the same position | **E** — corroborative | `CQ-P07-06` | **NO.** Agreement between three holds is not evidence; it opens no search. Recorded, not acted on. |

**Five material deltas, one non-material.** `MD-06` is recorded and deliberately **not** turned
into a round — three parties holding one statutory question in the same state is the correct
outcome, and P06 says so itself.

## 3. Answers Returned to P10

Executed as bounded evidence passes `EP-1`, `EP-2`, `EP-2b`, `EP-3`, `EP-4`. Full declarations,
denominators and controls in `P07_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md`. Published as a
handoff in `P07_TO_P10_HANDOFF.md`.

| P10's question | P07's answer | Class |
|---|---|---|
| `Q07-1` timing | **No installed Thai localisation module defines, overrides or extends any deferral or recognition-timing surface.** Two independent instruments, both zero, both with firing controls: a token scan over 251 files in 18 module copies, and an AST model walk over 172 parsed files (0 parse failures) recovering the complete `_name`/`_inherit` set. **Not a bare zero** — see the residue at §3.1. | `FACT VERIFIED` *(bounded, residue named)* |
| `Q07-2` account derivation | Same two instruments: **zero** deferred-account, deferred-journal or `_get_deferred` references. But the set **does** extend `account.account`, `account.move`, `account.move.line`, `account.payment`, `account.payment.register` and `account.tax` — so the interaction surface is **non-empty and field-level**, not model-level. The 18 fields it adds are enumerated in `P07_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md §4`. **None is a deferral or recognition field.** | `FACT VERIFIED` on the field set; `SUPPORTED INTERPRETATION` that no interaction exists |
| `Q07-3` presentation | **Zero** deferred-presentation references. The set's own reporting models are `l10n_th.tax.report.handler`, `l10n_th.pnd*.report.handler`, `withholding.tax.report` — statutory VAT and PND only. | `FACT VERIFIED` *(bounded)* |
| `Q07-4` item-level tax-period carrier | **CONTRADICTED.** `account_move_line.tax_period_date` **is present** in the deployed schema of **3 of 7** keyed identities — the same three in which `account_move.tax_period` is present, and the same three in which `scgl_tax_period_date` is installed. Entry-level and item-level carriers are **co-present and co-absent**; they arrive together because one module defines both. The correct statement is **not "absent from the item"** but **"present at both levels in 3 of 7 identities, and read for selection at neither"** (`04 §3`, `P07-F-107`). | `CONTRADICTED` |
| `Q07-5` statutory presentation of deferred revenue vs expense | **`UNRESOLVED — EVIDENCE REQUIRED`.** P07 holds no primary statutory source on the presentation of deferred balances, and will not infer one from implementation behaviour. This is the same class as `P07-U-04`, `P07-U-07`…`P07-U-10`. **P07 makes no statutory claim here, and P10 must not read this silence as permission.** | `UNRESOLVED — EVIDENCE REQUIRED` |

### 3.1 The residue in the `Q07-1`…`Q07-3` zero, declared rather than buried

`l10n_th_google_fonts` is **installed in identity `45a8e08e` (v16)** and its source is **not
present under either declared root**. The zero therefore covers **10 of the 11 installed module
names**, not 11 of 11. It is a font module by name — which is a reason to expect nothing and
**not evidence that there is nothing**. Carried as `P07-U-34`, class `NOT ON THIS HOST`.

**`Empty result != absence`, applied to my own result rather than quoted at someone else's.**

## 4. The Count P10 Asked For — `MD-02` Settled

Established from `ir_module_module` in each keyed identity, not from any document.

| identity | generation | installed modules | `l10n_th*` installed | set |
|---|---|---:|---:|---|
| `a1430edc` | v19 | 453 | **10** | full v19 set |
| `66d1b52a` | v19 | 251 | **10** | full v19 set |
| `1f6338ae` | v19 | 232 | **10** | full v19 set |
| `f4a44cce` | v19 | 179 | **10** | full v19 set |
| `551ab874` | v18 | 361 | **9** | v19 set less `l10n_th_reports_ext` |
| `45a8e08e` | v16 | 190 | **9** | less `l10n_th_reports`, `l10n_th_reports_ext`; **plus `l10n_th_google_fonts`** |
| `a6664233` | v18 lab | 41 | **1** | `l10n_th` only |

**Both of P10's figures are correct, for different databases, and neither is correct for "the
estate".** Nine and ten are not a discrepancy to reconcile — they are **two denominators**. The
count is `10, 10, 10, 10, 9, 9, 1`, and the v16 set is **not a subset** of the v19 set: it holds
a module the v19 identities do not. `P07-F-106`. `G02-R-17` is answered and closed for P07's
purposes; whether P10 closes it in its own register is P10's to decide.

## 5. P06's Committed Requirements — What They Close and What They Do Not

P06 states four requirements it commits to supply (`PI-02` §6). P07 assesses them against its
own blocking items **without researching P06's internals**.

| P06 requirement | Closes the P06 half of | P07's half, still open | P07's assessment |
|---|---|---|---|
| `P07-R-01` settlement event carries its **own immutable date** | `X-07` | **The reporting key.** The PND query selects on the *invoice's* accounting date (`P07-F-11`, `W-C-01`). A settlement date that nothing selects on changes nothing. | **ACCEPTED as the counterparty half.** Necessary, not sufficient. |
| `P07-R-02` allocation is a **first-class per-document immutable fact** | `X-08` | **The `payment_state != 'not_paid'` predicate** (`W-C-02`). A visible allocation that the predicate ignores changes nothing. | **ACCEPTED.** And P06 is right that neither party can close it: the third location is two custom WHT subsystems (`MD-05`). |
| `P07-R-03` a reversal is a **new linked event that supersedes and never erases** | `X-09` | The statutory half. | **ACCEPTED as the mechanism half.** |
| `P07-R-04` a settlement fact reported to an authority is **immutable in that period** | mechanism half of `X-09` | Whether a filed period may change **at all** is statute, not mechanism. | **ACCEPTED as mechanism. P07 takes no statutory position** — `P07-U-07`…`P07-U-10` class. |

**Status change recorded:** `X-07`, `X-08` and `X-09` move from **`BLOCKING for P07` with no
counterparty position** to **`BLOCKING for P07` with the counterparty half committed and the
P07 half named**. That is a real advance and it is **not a closure**: not one of the three is
closed, because in every one of them the remaining half is P07's own reporting predicate, and
changing a reporting predicate is design work this phase does not authorise.

**P06's convergence claim, verified against P07's own register and accepted:** `P07-R-01` and
`P07-R-03` are the same two requirements P08 asked for, and P07's `H-03` asks for the same
three elements — payment date, allocation per invoice, reversal linkage. **Three processes
independently specified one interface.** P07 adds nothing to it and does not restate it.

## 6. What This Round Refused To Do

Recorded so that the boundary is auditable rather than assumed.

| Temptation | Why it was refused |
|---|---|
| Investigate how deferred recognition actually works, to answer `Q07-1` "properly" | **P10's internals.** The question is answerable from the localisation modules alone, which are P07's. Answering it from the recognition engine would be `DOMAIN CONTAMINATION`. |
| Investigate bank matching to understand `X-07` | **P06's internals.** P07 needs only the interface fact: *a settlement-specific date exists and is immutable*. It has that from `P07-R-01`. |
| Investigate the two custom WHT subsystems' mutual interference (`MD-05`) | Partly P06's, partly `P07-U-30`, and **`P07-U-30` is a P07 item already open** — it is not re-opened here because no delta changes its value. |
| Re-run the filesystem route for `P07-N-25` | Terminated last round as redundant and `BLOCKED_ON_IO` (`22 §48.1`). **No material delta changes its value.** Not rerun. |
| Key the 20 unread artefacts of `P07-U-32` | A census widening. **Class E for every declared Closure Question** — no CQ is denominated over artefact count. Stays open, unchanged. |
