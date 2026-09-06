# P06_AAS03_BOUNDED_CHALLENGE.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G05)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> Prompt §10: all four AAS-03 experts challenge the bounded result independently. Each states **supported · missing · risky · challenged · evidence needed next**. **They do not self-declare PASS or FAIL. Disagreement is preserved.**
> Identifier family for this round: `E1-G` … `E4-G`, and `X4-F-*` for the six mandatory falsification attempts. Round-4 used `E1-S` … `E4-S`; no collision.

---

## 1. Expert 1 — Leader Functional Design

**SUPPORTED.** The four `H06` items were each re-derived from primary source rather than adopted from P10. `BR-01`'s confirmation is unusually strong: showing that the recognition module *knows about bank statement lines eleven lines below the deferral trigger and still never runs recognition off a settlement* converts a null result into a positive statement about design intent. `BR-02`'s answer — **P06 reconciles invoiced value** — is the single most useful functional fact this round produces, and it closes a question P10 could not close from its own side.

**MISSING.**
**`E1-G-01` — the round answers "what does the reference do" and never asks "what does a treasurer need".** `CQ-P06-03` asks *what exact business truth changes* when matching becomes partial or full. The answer given is mechanical (delete-and-recreate, sequence-index pairing). **The business truth is not stated anywhere**, and PHASE B will need it.

**`E1-G-02` — `HO-02` names a reversal *type* as a design candidate and never enumerates the types.** Structural-versus-corrective is a two-value distinction pulled from one wizard. Accrual reversal, credit note, `button_draft` reversal, deferral `_unlink_or_reverse`, audit-trail-protected `unlink` reversal and cancel-reconcile are **six** producers of `reversed_entry_id` visible in the files already read this round. **A type field designed against two values when six producers exist would be wrong on arrival.**

**RISKY.**
**`E1-G-03` — `P06-B-59` is written as a matching defect and is at least as much a *semantic* defect.** The claim *"the predicate cannot express the difference"* is true, but the deeper problem is that **the system has no concept of why a reversal exists**, so no predicate could be written. Filing it under matching invites a PHASE B fix at the wrong layer.

**CHALLENGED.**
**`E1-G-04` — `PDR-F-05` congratulates itself.** The register explains that a naive reading would have handed all of `H06-3` to P10 and *"would have looked disciplined"*. **That is a defence of a judgement call written by the party who made it.** The split may be right; the self-assessment is not evidence.

**EVIDENCE NEEDED NEXT.** The full producer set for `reversed_entry_id`, enumerated with a declared denominator, before any type taxonomy is proposed.

---

## 2. Expert 2 — Leadership Database Design

**SUPPORTED.** The grouping-key evidence is exact and reproducible: `[account_id, partner_id, currency_id, |amount_residual_currency|]` with a `grep -c` of **0** for `reversed_entry_id`, in three builds. That is a schema-level finding, not an inference. `BR-02`'s account-pair reading is likewise a direct read of the writer.

**MISSING.**
**`E2-G-01` — no index or constraint analysis was done on the new finding.** `reversed_entry_id` is declared `index='btree_not_null'` at `account_move.py:564-571` — **the file was open and the index attribute is on screen in the quoted block.** Whether a reversal-aware predicate is even affordable at scale is a schema question this round could have answered for free and did not.

**`E2-G-02` — `P06-B-60` and `P06-B-59` both turn on `account.reconcile`, and nobody looked at the deployed value.** `58_` proves a readable Odoo database dump exists on this workstation. **`account_account.reconcile` for the deferral and accrual account types is a single query against a file already in evidence.** The round declared it *"configuration, not source"* and stopped — which is correct as a source statement and is **not** a reason to leave a determinable fact undetermined.

**RISKY.**
**`E2-G-03` — the `mail.message` observation in `BR-03` is stated and abandoned.** *The accrual's only provenance record lives in the one table a proven-installed tool empties.* `PDR-F-06` declines to pursue it on domain-purity grounds. **Domain purity does not apply: `mail.message` deletion is `P06-B-50`, which is P06's own top CRITICAL finding.** The restraint is misapplied.

**CHALLENGED.**
**`E2-G-04` — the three-build invariance table proves less than it is presented as proving.** Identical line numbers across `20260312` and `20260417` for **six of seven** expressions is the signature of *the same upstream code*, not of independent confirmation. It bounds the finding against version drift; it is **not** three independent tests.

**EVIDENCE NEEDED NEXT.** `SELECT` on the `iEVING` dump for `account_account.reconcile` by `account_type`, restricted to `liability_current` / `asset_current` and the configured deferral accounts. Read-only, on an artefact already in evidence.

---

## 3. Expert 3 — Lead Integration & Localization

**SUPPORTED.** `BR-05` is the model of how a peer status should be consumed: the status field read at the pinned commit, in three registers, quoted verbatim. `MD-P06-06` honours P10's own evidence bound without argument.

**MISSING.**
**`E3-G-01` — `HO-03` splits ownership between P10 and P06 and no route exists to tell P10.** P06 has now discovered that P10's mechanism deposits an untyped, unlinked, offsetting pair into P06's matching population. **`REV-E-18` is the proof that P06's previous outbound answer never landed.** Writing a second unaddressed answer into a P06 file repeats the defect the same document just corrected.

**`E3-G-02` — the Thai localisation dimension is absent from every new finding.** `P06-B-09` (12 physical bank accounts on 2 GL accounts) and `P06-B-21` remain statutory HOLDs. Whether a Thai chart of accounts marks accrual accounts reconcilable is a **localisation** question, and the l10n packs — 904 of them in `addons_archive`, now searchable — were not consulted.

**RISKY.**
**`E3-G-03` — `MD-P06-08` reads P10's *"Do not start P06"* as addressed to P10's own session.** That reading is probably right and it is **an interpretation of another party's instruction, made by the party it constrains.** If it is wrong, this round executed against a peer's explicit hold.

**CHALLENGED.**
**`E3-G-04` — `REV-E-19` is filed as a bounded, harmless discovery. It is the second occurrence of a defect the package wrote a lesson about after the first.** *"Used for exactly the six expressions at issue and nothing else"* is disciplined **within** the round and does nothing about the standing problem: **this package still does not know what its evidence base is.** Two undeclared trees in two rounds is a trend.

**EVIDENCE NEEDED NEXT.** A declared, executed enumeration of every Odoo distribution on this workstation — **the population, once, with a command** — so that a third discovery is not possible. And a delivery route to P10 for `HO-03`.

---

## 4. Expert 4 — Lead Code & UI Architect

**SUPPORTED.** Every negative in this round carries an executed positive control, and `REV-E-17` shows the control catching nothing while a contradiction caught everything — recorded rather than buried. The `_post()` versus `action_post()` adjacency in `BR-01` is a genuine piece of code reading.

**MISSING.**
**`E4-G-01` — the auto-reconcile wizard was read; the *widget* was not.** `PR-04` describes `account.auto.reconcile.wizard`. **That is the batch tool.** The reconciliation **widget** — the path an operator actually uses, and the one `04_` RM-F-01…F-08 documents — was **not re-tested against the accrual pair.** `P06-B-59` is proven for the wizard and **assumed** for the widget. *The finding's headline says "P06's matching engine". The evidence covers one of at least two engines.*

**`E4-G-02` — `_auto_reconcile_zero_balance` was quoted and not analysed.** It groups by `[account_id, partner_id, currency_id]` with `having sum(residual) = 0` — **no amount key at all.** That strategy will sweep an accrual pair together with *any* other offsetting activity on the same account and partner. **It is strictly more dangerous than the one-to-one strategy the finding is built on, and the finding is built on the safer one.**

**RISKY.**
**`E4-G-03` — 30 in-place edits were applied to 15 files in one pass, by the author, with no independent verification, in the same round that found the errors.** The package's own standing position is that self-review is the weakest control. **Applying 30 corrections under it and then citing the corrected package as evidence of integrity is circular.**

**CHALLENGED.**
**`E4-G-04` — `REV-E-21`'s denominator is `62_`'s eight errors. `14_` and `39_` record eight more (`REV-E-01` … `REV-E-08`) and were not audited.** The finding says *"the defect is systematic"* on **half** the population. **The claim is probably right and the denominator does not support it yet.**

**EVIDENCE NEEDED NEXT.** The widget path re-tested against an accrual pair; the zero-balance strategy analysed; `REV-E-01` … `REV-E-08` audited against their target registers on the same pattern.

---

## 5. The six mandatory falsification attempts

Prompt §10. Each is an attempt to **break** this round's result, executed against source or against the package, with its outcome.

| # | Falsification attempted | Method | **Outcome** |
|---|---|---|---|
| `X4-F-01` | **Wrong event identity** — *"the accrual does carry a structured link; the round missed a field"* | Read `move_vals` in `accrued_orders.py:235-242` in full and `create_entries` to its return | **FAILED TO FALSIFY.** No source-document field. The only association is `order.message_post` — narrative text. **The finding survives** |
| `X4-F-02` | **Wrong date semantics** — *"a recognition-period date does reach P06 through the deferral move's `date`"* | The deferral move's `date` is `line.move_id.date` (`account_accountant/models/account_move.py:295`) — the **invoice's** date, inherited, not a recognition-period date; and the move it is written to never touches receivable, payable or liquidity (`BR-02`) | **FAILED TO FALSIFY** on the interface claim. **PARTIALLY SUCCEEDED on precision:** the deferral entries themselves *do* carry period dates, and `CQ-P06-02` should say *no recognition-period date reaches **P06's reconciliation surface***, not *no recognition-period date is inherited*. **Wording corrected** |
| `X4-F-03` | **Duplicate / replay double effect** — *"`P06-B-59` double-counts `P06-B-10`; they are the same defect"* | `B-10` is duplicate *ingestion* — two records for one bank event. `B-59` is *classification* — one true pair matched for the wrong reason. Different unit, different population, different precondition | **FAILED TO FALSIFY.** Distinct. **But `E4-G-01` stands: `B-59` is proven for one engine and asserted for the matching surface** |
| `X4-F-04` | **Correction / reversal break** — *"`cancel=False` means the pair is never reconciled, so it never reaches matching, so there is no defect"* | `cancel=False` means it is not reconciled **at creation**. `_get_amls_domain` (`:101-103`) then admits exactly this shape — `account.reconcile = True`, non-zero residual — into the auto-reconcile population | **FAILED TO FALSIFY.** `cancel=False` is what **puts** the pair in front of the matcher. **The attempt strengthened the finding** |
| `X4-F-05` | **Scope leakage** — *"the deferral/accrual accounts are company-scoped, so a pair cannot cross a company"* | The deferral account is `company_id.deferred_*_account_id` — genuinely company-scoped. **But `P06-B-26` establishes bank accounts may exist with no owning company, and `P06-B-27` that `root_id` is a fiscal hierarchy, not a legal boundary** | **PARTIALLY SUCCEEDED.** The *account* is company-scoped, so `B-59`/`B-60` should **not** be written as cross-company findings. **They are not.** `CQ-P06-07`'s standing scope findings are untouched by this round and are **not** extended to cover the new blockers |
| `X4-F-06` | **Source-present vs installed / configured / exercised** — *"`P06-B-59` is a source finding presented as a live risk"* | The precondition is `account.reconcile = True` on the accrual account. **Not determined.** Recorded as configuration-dependent in `BR-04`(4), `IN-09` and `P06-B-60` | **SUCCEEDED, and the round already concedes it.** `B-59` is **source-reachable, deployment-unverified**. **`E2-G-02` is right that it was determinable and was not determined.** This is the same defect `58_` corrected for `B-50` and it has recurred |

**Two of six falsification attempts succeeded in whole or in part (`X4-F-05`, `X4-F-06`), one succeeded on precision (`X4-F-02`), and one strengthened the finding it attacked (`X4-F-04`).**

---

## 6. Disagreement, preserved

| Point | Position A | Position B |
|---|---|---|
| Is `P06-B-59` proven? | **E2, E3:** the wizard evidence is exact and reproducible | **E4 (`E4-G-01`):** proven for the batch wizard, **assumed** for the widget. The headline overstates its own coverage |
| Does the round discharge its own integrity failure? | **E1:** the errors were found, quoted verbatim and edited into 15 files; that is the discipline working | **E4 (`E4-G-03`):** 30 self-applied, unreviewed edits in the same round, cited as evidence of integrity, is circular |
| Was `PDR-F-06`'s restraint correct? | **E1:** a fact crossing a boundary should be recorded, not chased | **E2 (`E2-G-03`):** `mail.message` deletion **is** `P06-B-50`; purity does not apply and the restraint suppressed a P06 finding |
| Is `REV-E-21` established? | **E1, E2, E3:** 6 of 8 over 13 statements is decisive | **E4 (`E4-G-04`):** the denominator is half the population; `REV-E-01`…`08` were not audited |

**No expert declares PASS or FAIL. Four disagreements are recorded unresolved and are carried to `P06_AAS_PLUS_CONSOLIDATION.md`.**
