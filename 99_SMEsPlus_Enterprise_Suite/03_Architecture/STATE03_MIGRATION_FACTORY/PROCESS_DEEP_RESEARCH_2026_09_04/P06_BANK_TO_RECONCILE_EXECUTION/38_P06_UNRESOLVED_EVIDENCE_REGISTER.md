# P06_UNRESOLVED_EVIDENCE_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Purpose:** every unresolved item with the **exact artefact** that would resolve it. An item with no stated resolution path does not belong here — it belongs in the blocker register as a design decision.

---

## 1. Resolvable by one database artefact

| ID | Question | Exact artefact |
|---|---|---|
| `B-44` | What is actually deployed on the SMEsPlus target? | `ir.module.module` export from the **target** database (`name`, `state`, `latest_version`). The two exports on this workstation are Odoo **19** databases — one is the BHPRO client, one is unattributable |
| `B-19` | Have voided cheque numbers been re-issued? | `SELECT check_number, COUNT(*) FROM account_payment GROUP BY check_number HAVING COUNT(*)>1` |
| `B-31` | Is the v14 `payment_2c2p` copy deployed anywhere? | module registry, as `B-44` |
| `OQ-91` | Is any `multi.approval.type` configured against a settlement model? | `SELECT model_id, domain, state_field, is_configured FROM multi_approval_type` |
| `OQ-42` | Do deployed partners carry `company_id = False` on bank accounts? | `SELECT COUNT(*) FROM res_partner_bank WHERE company_id IS NULL` |
| `OQ-62` | Same as `B-19` | — |
| `OQ-82` | Were the v14 PDC modules ever used? | row counts on the v14 PDC tables |
| `B-45` **exposure** | Do companies under one root hold different Tax IDs? | `SELECT id, parent_id, vat, company_registry FROM res_company` |

**Note on `B-45`:** the **control defect** is already closed on source evidence — the guard tests a fiscal hierarchy while naming a company boundary, and that holds for every deployment. Only the *exposure* is data-dependent.

**Eight items, four queries.** None was run: this session had no database connection (NC-01), and read-only-first discipline forbids inventing one.

---

## 2. Resolvable by one source artefact

| ID | Question | Artefact |
|---|---|---|
| `OQ-63` | Is `account_accountant_batch_payment` an incomplete checkout, or is the rejection wizard genuinely unreachable? | a known-good Odoo 18 enterprise distribution to diff against |
| `OQ-01` | Can `unique_import_id` collide across companies? | read `sanitize_account_number` in `odoo/addons/base/models/res_bank.py` |
| `OQ-03` | `_get_protected_vals` semantics around the move write-back | that method body |
| `OQ-12` | `_get_installments_data` — drives all four installment modes | `account/models/account_move_line.py:3216` |
| `OQ-22` | `_get_default_amls_matching_domain` — the outermost filter on every match | `account/models/account_bank_statement_line.py` |
| `OQ-23` | Mixed-currency partial-split arithmetic | `_prepare_reconciliation_single_partial`, ~300 lines |
| `OQ-30` | Which callers pass `no_cash_basis=True` on the P06 path | grep over the reconcile call graph |
| `OQ-41` | Direct `account.partial.reconcile.create()` callers (bypassing `_reconcile_plan`) | tree-wide grep |
| `OQ-53` | Does the custom provider's `required=True` `provider_id` on `payment.method` conflict with base seed data? | `payment/models/payment_method.py` |
| `OQ-54` | `_get_invoice_next_payment_values`, driving the EPD branch | `account` module |
| ~~`OQ-90`~~ | ~~Do `l10n_*` packs carry bank-charge or bounced-cheque handling?~~ | **CLOSED THIS SESSION — see §2a** |

### §2a — `OQ-90` CLOSED, and it produced a finding about the evidence base

`OQ-90` was flagged in this file's first draft as *"the most consequential"* gap and *"the first action for a successor round"*. **It was then executed rather than deferred.**

**UER-F-01 — Neither localisation pack in this build carries a bank-fee or a returned-item concept.**
- **DENOMINATOR:** POPULATION: every `l10n_*` directory in `$V18E`. PATH SET: `$V18E/l10n_*`. PATTERN 1: `bank_fee|bank_charge|transaction_fee|merchant_fee|processing_fee|commission`. PATTERN 2: `payment_return|bounce|dishonou?r|post_dated|postdated|\bpdc\b`. Both `--include="*.py"`, case-insensitive. UNIT: matching file.
- **RESULT: 0 files for both patterns.**
- **CLOSED — SOURCE EVIDENCE VERIFIED.** Both Class-A negatives (`B-17` no fee concept, `B-35` no returned-item concept) **survive the localisation surface intact**.

**UER-F-02 — And the result is stronger than the question anticipated, because the build's only two localisation packs are Thai.**
`ls -d $V18E/l10n_*` returns exactly two: **`l10n_th`** and **`l10n_th_reports`**.
The worry behind `OQ-90` was that *some* jurisdiction ships these capabilities. **The jurisdiction that matters here ships neither.** `l10n_th` contains `template_th.py`, `account_move.py`, `ir_actions_report.py`, `res_bank.py`, `res_partner.py` — a chart template, a QR/EMV bank extension and report plumbing. No bank-charge model, no returned-item model.

**UER-F-03 — But this reveals that the evidence tree is a filtered checkout, and that is a claim about the evidence base itself.**
The build carries **791 addon directories** and **2** localisation packs. A standard Odoo 18 distribution ships localisation packs for roughly ninety jurisdictions. **This tree has been filtered to the Thai deployment.**

Two consequences, and the second is uncomfortable:
1. **For P06's Thai-scoped questions this is the right tree** — it is what the project actually deploys against, and a Thai-only filter makes the localisation negative *more* relevant, not less.
2. **For any negative claimed at "`$V18E` tree scope", the tree is not a complete Odoo 18.** `OQ-63` already suspected an incomplete checkout of one enterprise module. This confirms filtering at the distribution level. **Every tree-wide Class-A negative in this package is therefore scoped to *this build*, not to Odoo 18** — including `is_internal_transfer`, `destination_journal_id`, `paired_internal_transfer`, the `provider_reference` uniqueness search, and the `chargeback|dispute` search.
- **This does not withdraw any of them.** Each was already declared with its path set, and this build is the correct target. It sharpens what "tree scope" means and is recorded as **`P06-B-55` — the evidence base is a filtered distribution, and every tree-scope negative inherits that boundary.**

**This is the third denominator correction in the P06 programme, and the first one the author caught unaided.** The prior two — the ingestion-door count and the blocker arithmetic — were caught by an independent pass and by an executed command respectively.

---

## 3. Resolvable only by execution

| ID | Question | Why static evidence cannot answer |
|---|---|---|
| `OQ-24` | Can two concurrent bank-rec validations double-allocate one payment? | no pessimistic lock found (`FOR UPDATE|select_for_update|_lock` → 0 hits); whether isolation alone serialises it is a runtime property |
| `OQ-20` | Does the lock check actually fire on the widget's `Command.clear()` path? | depends on ORM routing under `force_delete=True` |
| `OQ-40` | Does `super().unlink()` orphan the cancelled move? | depends on `_inherits` delete semantics |
| `OQ-70` | Does the v18 ORM tolerate `@api.model` on a `create` override? | runtime |

**Four items. None is a blocker's sole support** — each carries a finding that stands on other evidence.

---

## 4. Resolvable only by a peer process

| ID | Needs | From |
|---|---|---|
| `F-02`, part of `B-04` | vendor payable ownership | **P01 — unpublished** |
| `B-46`, `F-06`, `F-15`, `F-17` | the close architecture | **P08 — unpublished** |
| `P06-XC-01` | adjudication of the P02 verdict conflict | **P11** |
| `B-53` | closure of the payment-object-less cash door | **P05** |
| `OQ-93` | P10 routes close/FX dependencies to P04, which does not own them | **P11**, as a routing defect |

---

## 5. Resolvable only by statutory evidence

| ID | Question |
|---|---|
| `B-08` / `DEP-14` | FX rate source and missing-rate policy at settlement — P11 has it as **BOSS DECISION REQUIRED, packaged not decided** |
| `B-09` | 12 bank accounts on 2 GL accounts — acceptable under Thai practice? |
| `B-21` | Vendor advance defaulting to a P&L expense account |
| `B-13` | Thai WHT deducted at payment — P05, P06 and P07 all hold this identically |
| `OQ-04` | Whether any Thai bank populates CAMT `AcctSvcrRef` |
| `OQ-32` | Thai bank statement narrative formats (bears on the regex fee-capture path) |

**Six items. None is decidable by any research session, and all three processes that touched WHT reached the same HOLD independently** — which is the correct outcome, not a gap.

---

## 6. Items this continuation could have resolved and did not

Stated plainly, because a register that lists only external blockers is hiding something.

| ID | Why not done |
|---|---|
| `OQ-90` (`l10n_*` packs) | **The single largest self-inflicted gap.** It is a grep, it was within reach, and it was not run. It bounds two headline negatives. **Recorded as the first action for any successor round.** |
| `OQ-01`, `OQ-03`, `OQ-22` | Each is a single method read. Deprioritised against `B-27` and the peer intake; that was the right call at the time and remains a gap |
| `OQ-92` | P09's class-B claim about P06's widget — the analytic specifics were not traced |

---

## 7. Summary

| Resolution path | Count |
|---|---|
| One database artefact | 8 |
| One source artefact | 10 (was 11 — `OQ-90` closed) |
| Execution required | 4 |
| Peer process required | 5 |
| Statutory evidence required | 6 |
| Self-inflicted, actionable now | 2 (was 3 — `OQ-90` closed in-session) |

**Every unresolved item has a named resolution path. None is recorded as merely "open".**
