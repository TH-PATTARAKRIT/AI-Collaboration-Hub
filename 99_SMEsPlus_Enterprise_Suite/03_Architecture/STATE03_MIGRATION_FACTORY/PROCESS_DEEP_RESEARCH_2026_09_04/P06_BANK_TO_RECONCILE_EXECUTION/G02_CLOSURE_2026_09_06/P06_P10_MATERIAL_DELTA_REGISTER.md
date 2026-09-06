# P06_P10_MATERIAL_DELTA_REGISTER.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G01)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**P06 baseline consumed:** `9e5d729` (70 files) · working head at start `18035d9`
**P10 controlled input:** `1fea562cb32e23bd44a1c6e6b4a2cf1081d25287`
**Constitution:** `48ee264fd74dcb0dee378789e56d028ad8bb6110`

> This register is built **before any new search**, per prompt §6. Every bounded recheck executed in this round is declared here first, with its Closure Question ID, the exact claim tested, why the standing evidence was insufficient, the bounded surface, the denominator and the stop condition. **No item in this register authorised a generic filesystem, source-tree or database sweep, and none was performed.**

---

## 1. What was read from P10, and what was not

**POPULATION:** every file at `1fea562` under
`99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/BOSS_GATE/REOPEN_PROGRAM_2026_09_02/ACCOUNT_REOPEN/ACCOUNT_P10_TIME_BASED_RECOGNITION/`.
**PATTERN:** `git show 1fea562:<path> | grep -n "P06"` executed per file, plus full reads of the four files that address P06 by name.
**UNIT:** file.
**EXECUTED:**

```
git ls-tree -r --name-only 1fea562 -- <P10 root> | wc -l      →  109
<loop over 109 files, grep -l 'P06'>                          →   12
```

**RESULT: 109 files in the P10 package; 12 name P06.** All 12 were opened. The remaining 97 were **not read** — they are P10 internals, and reading them is prohibited by prompt §5.

> **The first execution of that loop returned `0 of 109`, which was false.** It was caught because `P10_TO_P06_HANDOFF.md` demonstrably exists in the tree, and re-run with an explicit positive control it returned **12**. The defect and its cause are recorded as **`REV-E-17`** in `P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md`. **The count above is the corrected one.**

### 1a. Domain-purity boundary applied while reading

P10's own artefacts describe recognition mechanics — schedule construction, period grids, allocation policy, deferral method selection. **None of that was researched.** What was extracted from each of the 12 files is the **minimum producer/consumer interface fact** P06 needs, and nothing else. Where a P10 file invited P06 into recognition internals, the path was stopped and classified. See `P06_DOMAIN_PURITY_AND_BOUNDARY_REGISTER.md`.

---

## 2. The register

Classification uses exactly the five labels required by prompt §6.

| MD ID | P10 item (source) | P10's position, as issued | **Classification** | CQ | Disposition |
|---|---|---|---|---|---|
| `MD-P06-01` | `H06-1` — *"Recognition never touches cash; no recognition event is settlement-triggered. The interface is empty — confirm rather than assume"* (`P10_TO_P06_HANDOFF.md` §1) | interface empty | **MATERIAL TO P06 — REQUIRES BOUNDED RECHECK** | `CQ-P06-01`, `CQ-P06-02` | **CONFIRMED from P06's own side by source execution — see `BR-01`.** P10's position is upheld and is now P06-evidenced, not P06-assumed |
| `MD-P06-02` | `H06-2` — *"Timing effect on the receivable is nil; on P&L total. Does P06 reconcile against invoiced or recognised value? They diverge for the whole window"* | receivable unaffected | **MATERIAL TO P06 — REQUIRES BOUNDED RECHECK** | `CQ-P06-02`, `CQ-P06-06` | **CONFIRMED, and the question is answered: P06 reconciles INVOICED value — see `BR-02`.** A second-order consequence P10 did not raise is recorded as `P06-B-60` |
| `MD-P06-03` | `H06-3` — *"The accrual is the one mechanism with a settlement relationship and has no link to its settlement"*; detecting the superseded accrual is P10's problem (`F-05`, `AL-6`) | P10-owned | **MATERIAL TO P06 — REQUIRES BOUNDED RECHECK** — *the ownership half is `EXTERNAL TO P06 — HANDOFF ONLY`* | `CQ-P06-01`, `CQ-P06-03` | **CONFIRMED at source, and P10's ownership claim is accepted for detection.** But the accrual pair lands in **P06's** reconciliation population, which P10 did not state — see `BR-03`, `P06-B-59` |
| `MD-P06-04` | `H06-4` — *"A structural reversal is not a correction; the reference does not distinguish them in the ledger. If P06's matching treats them the same it will match structural pairs and report them resolved"* | warning to P06 | **MATERIAL TO P06 — REQUIRES BOUNDED RECHECK** | `CQ-P06-04`, `CQ-P06-03` | **CONFIRMED, and materially stronger than P10 stated — see `BR-04`.** The discriminator is not merely absent from the ledger; the matching engine never reads the one field that exists. `P06-B-59` |
| `MD-P06-05` | §2 *"What P10 Does Not Send"* — no opinion on settlement, outstanding-account separation, write-off behaviour, multi-deduction | explicit non-claims | **NO P06 IMPACT** | — | Recorded. P06's standing findings on these four (`03_`, `06_`, `22_`, `40_`) are **unaffected**: P10 asserts nothing that could contradict them. **A non-claim is not corroboration either** — it was not read as support |
| `MD-P06-06` | §3 Bounding — scoped to the declared reference root and four deployed databases *"in which the deferral mechanism has never generated an entry"*; *"P06 must not read any of it as deployed-behaviour evidence"* | evidence-base bound | **CORROBORATIVE ONLY — NO NEW ROUND** | `CQ-P06-08` | **Honoured verbatim.** No P10 deployment figure is cited anywhere in this round as evidence of P06 behaviour. It corroborates P06's own standing position (`51_`, `56_`) that source presence ≠ deployment ≠ exercise |
| `MD-P06-07` | `X-08` / `D-08` / `PD-08` — *"Whether bank-side interest accrual is a P10 event"*, status **`OPEN — PEER EVIDENCE`** at `1fea562` (`53_P10_PEER_DEPENDENCY_REGISTER_V2.md:30`; also `19_:19,59`, `10_:36`) | still open | **CONTRADICTS P06 — AFFECTED CLAIM MUST REOPEN** | `CQ-P06-07` | **P06's claim *"answered — P10 may close it"* (`35_`:114-121, `36_` `D-11`, `34_` F-12, `18_`:198, `39_`:96, `57_`:31, `70_`:71) is CONTRADICTED as to status, not as to substance.** Seven P06 files state a peer dependency is closable that the peer's own latest register still carries **OPEN**. See `BR-05` and `REV-E-18` |
| `MD-P06-08` | `72_P10_AUTO_RESUME_STATE.md:28` — *"**Do not start P06.** No P10 work is unblocked without one of those four"* | P10 resume instruction | **EXTERNAL TO P06 — HANDOFF ONLY** | — | **Read as an instruction to P10's own next session, not to P06.** P10 is declining to open P06 work; it is not instructing P06 to stop. This round is Boss-directed and proceeds. Recorded because a peer's NEXT-EXACT-ACTION naming P06 must never sit unconsumed |
| `MD-P06-09` | `65_P10_CHECKPOINT_REGISTER.md:52` — `CP-05` handoffs *"**COMPLETE, then CORRECTED**"*; P08's own control-set inventory mis-stated and **withdrawn** | correction notice | **EXTERNAL TO P06 — HANDOFF ONLY** | `CQ-P06-08` | The withdrawn statement is about **P08's** control set, not P06's. Checked: no P06 file relies on it. **Verified rather than assumed:** `grep -n "P10.*P08\|P08.*P10" *.md` returns **4 hits, all about dependency *routing*** (`11_`:148, `36_`:60-61, `39_`:98) — **not one P06 statement takes a P08 fact from P10.** P06's P08 intake is sourced from P08's own branch files (`53_`:27,30,45). **But running that check surfaced a different, self-inflicted defect — see `REV-E-20`** |
| `MD-P06-10` | `P10_G02_TERMINALITY_RECORD.md` — *"Nine answered · three partial or corrected-then-partial · one is this record. Zero closed. No question is dispositioned `PASS`"* | P10 terminality | **CORROBORATIVE ONLY — NO NEW ROUND** | `CQ-P06-08` | Confirms P10 is `HOLD`, consumed as controlled input with open holds per prompt §4. **Not read as PASS and not read as truth-by-authority.** Every H06 item above was independently re-executed against source rather than adopted |
| `MD-P06-11` | `P10_CLOSURE_QUESTION_REGISTER.md:13` — *"`CQ-P10-13` … **and this tick was FALSE when first made.** The file did not exist; three of four challengers found it independently"* | P10 self-correction | **CORROBORATIVE ONLY — NO NEW ROUND** | `CQ-P06-08` | A method observation, not a P06 fact. It is the same defect class as P06's own `REV-E-17` this round: **a tick that records an intention rather than an executed result.** Both are logged; neither changes a P06 finding |
| `MD-P06-12` | `P10_CLOSURE_QUESTION_REGISTER.md` §4 — P02's `IN-P02-1` **withdrawn** (`G02-R-01`); posted-basis Archive C **1,145 delivered-not-invoiced vs 792 billed-ahead** | P02→P10 measurement | **EXTERNAL TO P06 — HANDOFF ONLY** | — | Revenue-timing measurement. **Boss Decision 3 is `OPEN — Boss reserved`; P10 states it may not settle it, and neither may P06.** No P06 claim depends on it. Cited here only so the withdrawal is not silently inherited |
| `MD-P06-13` | `P10_CLOSURE_QUESTION_REGISTER.md` §4 — P02 names a database `iErpOCC` **outside P10's examined four** | evidence-population | **EXTERNAL TO P06 — HANDOFF ONLY**, *with one bounded consequence* | `CQ-P06-08` | P06 **does not go and read it** — that would be widening, and it is P02/P11 territory. Its only effect on P06 is to confirm that P06's own deployment-population statements (`51_`, `58_`) remain floors. **Recorded as `P06-OQ-120`, routed, not executed** |
| `MD-P06-14` | `P10_G02_AAS03_CHALLENGE_RECORD.md:197` — *"P06, P08 and P11 each received a handoff; P07 received a table cell"* | challenge observation | **NO P06 IMPACT** | — | An observation about P10's own handoff quality. P06 received a full handoff and consumed it |
| `MD-P06-15` | `36_P06_DEPENDENCY_REGISTER.md:60-61` `DEP-F-03` — P10 routes close/FX dependencies to **P04**, while P11 and P02 route them to **P08** (P06's own standing finding, re-checked against `1fea562`) | — | **NO P06 IMPACT — STATUS UNCHANGED** | — | Re-checked at the new commit: **the routing is unchanged.** P06's standing disposition stands — `NOT RESOLVED — not P06's to adjudicate`, flagged to P11 as `OQ-93` (`11_` T-10, `38_`:90). **No reopening** |

**Executed classification tally:** `MATERIAL TO P06 — REQUIRES BOUNDED RECHECK` **4** · `CORROBORATIVE ONLY — NO NEW ROUND` **3** · `EXTERNAL TO P06 — HANDOFF ONLY` **5** · `CONTRADICTS P06 — AFFECTED CLAIM MUST REOPEN` **1** · `NO P06 IMPACT` **3**. Total **16**? — **No. Total 15.** `MD-P06-03` is split-classified across two columns and is counted **once**, under `MATERIAL`. 4 + 3 + 5 + 1 + 3 = **16 label-assignments over 15 items**, and the two figures are different units. *Stated explicitly because summing label-assignments as if they were items is the exact defect this package recorded as `REV-E-05`/`REV-E-08`.*

---

## 3. Bounded rechecks — declared before execution, per prompt §6

Five rechecks were authorised by the register above. Each is stated in full, then its result.

### `BR-01` — is the settlement→recognition interface actually empty?

| Field | Value |
|---|---|
| **CQ** | `CQ-P06-01`, `CQ-P06-02` |
| **Exact claim tested** | *No recognition (deferral) entry in the reference is triggered by a settlement, payment, bank-statement or reconciliation event.* |
| **Why standing evidence was insufficient** | P06 had never tested it. P06's `02_`, `05_`, `33_` enumerate what P06 **does** produce; **absence of a recognition consumer had never been executed as a query**, and P10 explicitly asked P06 to *confirm rather than assume*. Adopting P10's word would be `secondary-source` reliance. |
| **Bounded evidence surface** | Exactly six files: `account/models/account_payment.py`, `account_bank_statement.py`, `account_bank_statement_line.py`, `account_move_line.py`, `account_partial_reconcile.py`, `account_reconcile_model.py`; plus `account_accountant/models/account_move.py` for the generator. **No wider sweep.** |
| **Population / denominator** | The 6 P06-core files above, whole-file, token `deferred`. **Positive control:** the same token must return a non-zero file count tree-wide, else the instrument is broken. |
| **Expected result classes** | (a) ≥1 settlement-side generator call → **CONTRADICTS P10**; (b) 0 with a firing positive control → **CONFIRMS**; (c) 0 with a silent control → **instrument failure, not a result**. |
| **Stop condition** | The generator's trigger method is identified. Stop there — do not follow recognition mechanics further. |

**EXECUTED:**
```
grep -rl --include='*.py' "deferred_start_date" .            →  15 files      [positive control FIRES]
account/models/account_payment.py             lines=1171  'account'=150  'deferred'=0
account/models/account_bank_statement_line.py lines= 854  'account'= 92  'deferred'=0
account/models/account_move_line.py           lines=3524  'account'=390  'deferred'=0
account/models/account_partial_reconcile.py   lines= 657  'account'= 44  'deferred'=0
account/models/account_reconcile_model.py     lines= 388  'account'= 22  'deferred'=0
```
Each file is proven present and non-trivial by its own line count, and proven readable by a second token that **does** match. **Result class (b).**

**The trigger, located and stopped at** — `$V18E/account_accountant/models/account_move.py:109-115`:
```python
def _post(self, soft=True):
    # Deferred management
    posted = super()._post(soft)
    for move in self:
        if move._get_deferred_entries_method() == 'on_validation' and any(move.line_ids.mapped('deferred_start_date')):
            move._generate_deferred_entries()
    return posted
```

**`BR-01` RESULT — `FACT VERIFIED`. The interface is empty, and P06 now says so on its own evidence.** Recognition generation hangs off `_post()` — **the act of posting a document**, not the act of settling one. There is no payment, statement-line or reconciliation trigger anywhere in P06's core.

> **And the confirmation is stronger than a null.** The *same file*, eleven lines below, contains the only settlement-direction coupling that exists:
> ```python
> def action_post(self):
>     # EXTENDS 'account' to trigger the CRON auto-reconciling the statement lines.
>     res = super().action_post()
>     if self.statement_line_id and not self._context.get('skip_statement_line_cron_trigger'):
>         self.env.ref('account_accountant.auto_reconcile_bank_statement_line')._trigger()
> ```
> — `account_accountant/models/account_move.py:117-122`. **The recognition module knows about bank statement lines and triggers P06 machinery from them, and still never runs recognition off a settlement.** The interface is empty in the one file where making it would have been easiest. That is design, not oversight.

### `BR-02` — does P06 reconcile invoiced or recognised value?

| Field | Value |
|---|---|
| **CQ** | `CQ-P06-02`, `CQ-P06-06` |
| **Exact claim tested** | *The deferral entry never touches a receivable, payable or liquidity account; therefore the balance P06 matches is the invoiced amount.* |
| **Why insufficient** | P10 asserted the receivable effect is nil. P06 had no evidence either way and must not inherit it. |
| **Bounded surface** | `account_accountant/models/account_move.py::_generate_deferred_entries` only. |
| **Population** | The account pair written by that method. **UNIT: account role.** |
| **Expected classes** | receivable/payable/liquidity touched → **divergence enters P06's matching surface**; not touched → **it does not**. |
| **Stop condition** | The account pair is read. Do not follow period-splitting arithmetic — that is P10 internals. |

**EXECUTED** — `account_accountant/models/account_move.py:297-298`:
```python
self.env['account.move.line']._get_deferred_lines_values(account.id, coeff * line.balance, ref, line.analytic_distribution, line)
for (account, coeff) in [(line.account_id, -1), (deferred_account, 1)]
```
where `deferred_account = company.deferred_expense_account_id | deferred_revenue_account_id` (`:268`).

**`BR-02` RESULT — `FACT VERIFIED`. The pair is `(the P&L line's own account, the company deferral account)`. Neither is the receivable, the payable or a liquidity account.**

> **Answer to P10's question: P06 reconciles INVOICED value.** The receivable line is written by the invoice at the invoiced amount and is never re-valued by deferral. P10's `H06-2` is upheld, independently.
>
> **And a second-order consequence P10 did not raise, which is P06's to own** — the deferral move is created with `'partner_id': line.partner_id.id` (`:290`) against a **company-level deferral account**. If that account is configured `reconcile=True`, the deferral moves enter P06's reconciliation population as partner-attributed, offsetting open items on an account that has nothing to do with settlement. Whether it is so configured is **not determined by source** — it is chart-of-accounts configuration. Raised as **`P06-B-60`**, `UNRESOLVED — EVIDENCE REQUIRED`, and carried into `BR-04`.

### `BR-03` — does the accrual carry a link to what settles it?

| Field | Value |
|---|---|
| **CQ** | `CQ-P06-01`, `CQ-P06-03` |
| **Exact claim tested** | *The accrual entry carries no structured reference to the order, bill or payment that will settle it.* |
| **Why insufficient** | P10 states it; P06 must not adopt it, and P06 needs to know what reaches its matching surface. |
| **Bounded surface** | `account/wizard/accrued_orders.py` only. |
| **Population** | The `move_vals` dictionary written by `_compute_move_vals`. **UNIT: field.** |
| **Expected classes** | a structured link field present → P06 can discriminate; absent → it cannot. |
| **Stop condition** | `create_entries` read to its return. Do not enter accrual amount computation. |

**EXECUTED** — `account/wizard/accrued_orders.py:235-242`:
```python
move_vals = {
    'ref': _('Accrued %(entry_type)s entry as of %(date)s', ...),
    'name': '/', 'journal_id': ..., 'date': self.date,
    'line_ids': move_lines, 'currency_id': ...,
}
```
and `:245-262`:
```python
move = self.env['account.move'].create(move_vals); move._post()
reverse_move = move._reverse_moves(default_values_list=[{'ref': _('Reversal of: %s', move.ref), 'name': '/', 'date': self.reversal_date}])
reverse_move._post()
for order in orders_with_entries:
    body = _('Accrual entry created on %(date)s: %(accrual_entry)s. And its reverse entry: %(reverse_entry)s.', ...)
    order.message_post(body=body)
```

**`BR-03` RESULT — `FACT VERIFIED`. There is no structured link.** `move_vals` contains **no** order reference, no `invoice_origin`, no source-document field. The **only** association between the accrual and the business object it accrues is a **chatter message posted on the order** — narrative text in `mail.message`, not a queryable relation.

> P10's ownership position — *detecting the superseded accrual is P10's problem* — is **accepted**, and P06 does not take it. But the boundary must be stated precisely: **detection is P10's; the accrual pair still arrives in P06's population.** That is `BR-04`.
>
> Note also, and this is a P06 fact rather than a P10 one: the chatter link is written to `mail.message`, which is **one of the tables `om_data_remove` deletes by unfiltered SQL** (`44_` OMD-F-01, `59_`, `60_`). The accrual's only trace of its own purpose sits in a table this estate has a proven-installed tool for emptying. Recorded as **`P06-OQ-121`**; it does not change `B-50`'s severity, which is already CRITICAL.

### `BR-04` — can P06's matching tell a structural reversal from a correction?

| Field | Value |
|---|---|
| **CQ** | `CQ-P06-04`, `CQ-P06-03` |
| **Exact claim tested** | *The reference sets the same field for a structural reversal and a corrective reversal, and P06's matching engine does not read it.* **Two claims — both must be executed.** |
| **Why insufficient** | P10 warned about the first half only. The second half — what P06's own engine does — is squarely P06's domain and had never been tested. |
| **Bounded surface** | `account/models/account_move.py::_reverse_moves` and the `reversed_entry_id` field definition; `account_accountant/wizard/account_auto_reconcile_wizard.py` whole file. |
| **Population** | The reversal-creation path (1 method, all callers of it within the bounded surface) and the auto-reconcile grouping key (1 expression). **UNIT: field.** |
| **Expected classes** | a type discriminator exists **and** is read → no defect; exists but unread → **P06 defect**; does not exist → **reference defect inherited by P06**. |
| **Stop condition** | The grouping key is read. Do not enumerate every reconciliation entry point in the estate — that is the round-2 surface and is already closed. |

**EXECUTED (a)** — `account/models/account_move.py:4760`, `:4779-4783`:
```python
def _reverse_moves(self, default_values_list=None, cancel=False):
    ...
    default_values.update({
        'move_type': TYPE_REVERSE_MAP[move.move_type],
        'reversed_entry_id': move.id,
        'partner_id': move.partner_id.id,
    })
```
`reversed_entry_id` is defined once, at `:564`; its inverse `reversal_move_ids` at `:572`. **Every reversal in the system — structural or corrective — writes the same field, with no type qualifier.** `cancel=True` additionally calls `lines.remove_move_reconcile()` and re-posts under `move_reverse_cancel`, which is what auto-reconciles a *cancelling* pair. **The accrual wizard calls `_reverse_moves(...)` with `cancel` defaulted to `False`** (`accrued_orders.py:253`) — so the accrual and its structural reversal are created **unreconciled**, as two open, offsetting items.

**EXECUTED (b)** — `account_accountant/wizard/account_auto_reconcile_wizard.py`:
```
:101-108  domain:  ('account_id.reconcile','=',True), ('amount_residual_currency','!=',0.0), ('amount_residual','!=',0.0)  [+ optional partner filter]
:118      one-to-one grouping key: ['account_id', 'partner_id', 'currency_id', 'amount_residual_currency:abs_rounded']
:141-143  zero-balance strategy:   groupby ['account_id','partner_id','currency_id'] having sum(residual)=0
grep -c "reversed_entry_id" account_auto_reconcile_wizard.py   →  0
```

**`BR-04` RESULT — `FACT VERIFIED`, and it is materially stronger than P10 stated.**

1. The discriminator P10 says is missing from the ledger is **half-present**: `reversed_entry_id` links the pair. What is missing is the **type** — nothing records *why* the reversal exists.
2. **P06's own auto-reconcile engine never reads it.** Zero occurrences. The one-to-one key is *same account, same partner, same currency, equal absolute residual* — which an accrual and its structural reversal satisfy **by construction**, and which a correction and its original satisfy identically.
3. Therefore P10's warning lands, with a correction to its mechanism: **P06 will not "treat them the same" through a design choice — it will match them because the matching predicate cannot express the difference.** The engine has no expression in which `reversed_entry_id` could appear.
4. The precondition is `account_id.reconcile = True` (`:101`). The accrual wizard's account domain (`accrued_orders.py:51`) is `account_type in (liability_current | asset_current)` and **does not require `reconcile=True`**. **So whether the pair enters P06's population at all is chart-of-accounts configuration, not code.** Same shape as `P06-B-60`.

**Raised as `P06-B-59` — HIGH.** *The reconciliation matching predicate cannot distinguish a structural reversal pair from a corrective reversal pair, because it never reads the only linking field, and no field records the reversal's type. Reachability is configuration-dependent (`account.reconcile`).* Severity rationale in `P06_AAS_PLUS_CONSOLIDATION.md` §4.

### `BR-05` — is P06's "X-08 is closable" claim still true against P10's latest register?

| Field | Value |
|---|---|
| **CQ** | `CQ-P06-07`, `CQ-P06-08` |
| **Exact claim tested** | *P06's published statement that P10's `X-08` is answered and may be closed is consistent with P10's own latest published status.* |
| **Why insufficient** | P06 published the claim against P10's **round-1** artefacts. `1fea562` is a later commit. **Supersession binds at claim level** — the right branch and SHA are not enough. |
| **Bounded surface** | The three P10 files that carry the dependency, at `1fea562`, **status field only**. |
| **Population** | `10_P10_CROSS_PROCESS_OWNERSHIP.md`, `19_P10_DEPENDENCY_REGISTER.md`, `53_P10_PEER_DEPENDENCY_REGISTER_V2.md`. **UNIT: status field.** |
| **Expected classes** | closed → P06's claim landed; still open → **P06's claim is contradicted as to status**. |
| **Stop condition** | Three status fields read. **Do not** read P10's reasoning about interest accrual — that is P10 internals. |

**EXECUTED:**
```
53_P10_PEER_DEPENDENCY_REGISTER_V2.md:30  | PD-08 | P06 | Whether bank-side interest accrual is a P10 event | OPEN — PEER EVIDENCE | no | — |
19_P10_DEPENDENCY_REGISTER.md:19,59       | D-08  | P06 | ... | PEER DEPENDENCY OPEN  ... "PEER DEPENDENCY OPEN — unchanged"
10_P10_CROSS_PROCESS_OWNERSHIP.md:36      | X-08  | P06 | ... | PEER DEPENDENCY OPEN
```

**`BR-05` RESULT — `CONTRADICTED`.** Three of three still carry it **OPEN**; `19_` says **"unchanged"** in as many words.

> **Seven P06 files assert a peer dependency is answered and closable.** The peer's latest published register, two rounds later, has not received it. **The substance is not contradicted** — P06's answer (*the object does not exist for either process; draw the boundary at accrual versus receipt*) is untouched and is re-affirmed here. **What is contradicted is the status claim.** P06 wrote *"P10 may close it"* and then wrote, in `35_`:145 and `39_`:96, that it was **"closed by P06."** **A dependency owned by a peer is not closed by the answering party.** Recorded as **`REV-E-18`**, and every one of the seven statements is corrected in `P06_CONTRADICTION_AND_REVISION_SUPPLEMENT.md` §3 — *edited in the registers, not merely logged in a disposition table.*

---

## 4. Cross-version bounding of this round's four findings

Prompt §10 requires the *source-present vs installed/configured/exercised* falsification, and `P06-B-44` makes generation a standing evidence risk. **All four `BR` source findings were re-executed against three builds** — the same six expressions, nothing wider:

| Expression | v18 `18.0+e.20250608` | v19 `19.0+e.20260312` | v19 `19.0+e.20260417` |
|---|---|---|---|
| `_post()` → `_generate_deferred_entries()` | present | `account_accountant/models/account_move.py:117` | `:117` |
| deferral account pair `[(line.account_id,-1),(deferred_account,1)]` | present | `:338` | `:338` |
| accrual `_reverse_moves(` call, **no `cancel`** | `accrued_orders.py:253` | `:384` | `:384` |
| accrual `move_vals` `ref` free-text, no link field | present | `:357` | `:357` |
| `'reversed_entry_id': move.id` set unconditionally | `account_move.py:4781` | `:5423` | `:5454` |
| auto-reconcile grouping key | `:118` | `:118` | `:118` |
| `grep -c reversed_entry_id` in the auto-reconcile wizard | **0** | **0** | **0** |
| `deferred` in the three P06 core files | **0 / 0 / 0** | **0 / 0 / 0** | **0 / 0 / 0** |

**ALL FOUR FINDINGS ARE CROSS-VERSION INVARIANT across two generations and three builds.** They join the six invariants established in `51_`.

> **`REV-E-19` — a third reference tree exists that this package had not declared.** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus19/SMEsPlus/odoo-19.0+e.20260417` — a **later v19 build** than the `20260312` tree adopted in round 4. It was found by a `find -maxdepth 5 -name "odoo-19.0+e*"` run to re-establish paths, not by a new sweep. **It is used above for exactly the six expressions at issue and for nothing else** — deeper on the same surface, not wider. **This is the second time this package has discovered an undeclared reference tree after declaring its evidence base complete** (`REV-E-10` was the first). Consequence for `P06-B-55` and `51_` is stated in `P06_SOURCE_LINK_AND_EVIDENCE_SUPPLEMENT.md` §4.

---

## 5. What this round did **not** do

Stated so the boundary is auditable rather than assumed:

- **No P10 internals researched.** 97 of 109 P10 files unopened. No recognition schedule, period grid, allocation policy or deferral-method logic examined.
- **No new deployed-database enumeration.** `iErpOCC` named by P02 via P10 was **routed, not read** (`P06-OQ-120`).
- **No P10 deployment figure used as evidence**, per P10's own §3 bound.
- **No destructive path executed.** No DB, runtime, configuration or module mutation. No install or uninstall.
- **No generic sweep.** Every command above names its files or a single token with a positive control.
- **No P05/P07/P08/P09/P11 internals opened.**
- **No SMEsPlus function, schema, API or UI designed.**
- **No merge to `SMEsPlus`.**

---

## 6. Register disposition

| Outcome | Count |
|---|---|
| P10 items classified | **15** |
| Bounded rechecks declared and executed | **5** |
| P10 positions **confirmed on P06's own evidence** | **4** (`H06-1` … `H06-4`) |
| P10 positions adopted on P10's authority | **0** |
| P06 claims **contradicted** by the delta | **1** (`X-08` status — `REV-E-18`) |
| New P06 blockers raised | **2** (`P06-B-59` HIGH, `P06-B-60` `UNRESOLVED`) |
| New P06 open questions | **5** (`P06-OQ-120` … `P06-OQ-124`) |
| New author errors recorded | **5** (`REV-E-17` … `REV-E-21`) |
| **In-place corrections applied to prior registers** | **30 edits across 15 files** |
| Items that triggered a widening search | **0** |
