# P06_CANDIDATE_INPUT_PROCESS_OUTPUT_HANDOFF_PACK.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G02)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **THESE ARE PHASE S EVIDENCE CANDIDATES ONLY.**
> Nothing here is a contract, a specification, an interface agreement or a design approval. Every element is a **candidate to be tested in PHASE B**, and several are recorded precisely because the evidence says the reference does **not** supply them.
> **AI EOS is not active. No SMEsPlus function, schema, API or UI is designed here.**
> Labels used are exactly the six permitted by prompt §8: `FACT VERIFIED` · `SUPPORTED INTERPRETATION` · `DESIGN CANDIDATE — PHASE S ONLY` · `CONTRADICTED` · `UNRESOLVED — EVIDENCE REQUIRED` · `BOSS DECISION REQUIRED`.

---

## 1. The eight closure questions, dispositioned

Each question carries **P06's standing position** (with the file that holds it) and **what the P10 delta did to it**. Per prompt §7 nothing outside these was reconciled.

### `CQ-P06-01` — Settlement event identity

**Question:** can a reconciliation-relevant settlement event be uniquely identified without relying on mutable document labels or implementation internals?

**Disposition: `FACT VERIFIED` — NO.**

| Evidence | Where |
|---|---|
| `payment_ref` is a label, never an identifier | `02_` BER-F-03 |
| `unique_import_id` is namespaced **by value, not by schema** | `02_` BER-F-04 |
| `online_transaction_identifier` has **no database constraint at all** | `02_` BER-F-05 |
| A null identifier is treated as *"not a duplicate"* at all three enforcement points | `02_` BER-F-06 |
| **4 of 7** ingestion doors attach no identity — CSV, QIF, OCR, manual keying | `26_` IIM-F-00, denominator executed at `26_`:34 |
| The one SQL UNIQUE covers **2 of 7** doors | `07_`:38 |
| The provider reference is unconstrained, unindexed, never searched, and overwritten by the last callback received | `16_`:24, `08_` |

**P10 delta:** `MD-P06-01`, `MD-P06-03`. **No change to the answer, one addition to the population.** `BR-03` establishes that the accrual entry — which reaches P06's ledger surface — carries **no structured source reference at all**; its only link to the business object it accrues is a chatter message. **That is a seventh identity-bearing object with no identity**, and it arrives from a mechanism P06 does not own.

### `CQ-P06-02` — Date semantics

**Disposition: `FACT VERIFIED` for three of four; `CONTRADICTED` for the fourth as a distinct field.**

| Date concept | Does a distinct field exist? | Evidence |
|---|---|---|
| **Settlement / economic date** | **NO distinct field.** The statement line's `date` is the value the file supplies, and for manually-keyed and OCR lines it is operator-supplied | `02_`, `05_` |
| **Bank statement date** | **YES**, `account.bank.statement.date`, but derived from its lines, not asserted by the bank | `02_` BER-F-10 … F-14 |
| **Accounting posting date** | **YES**, `account.move.date`, and it is **system-derived** where a lock date intervenes | `28_`, Wave-A `_get_accounting_date` |
| **Recognition-period date inherited from upstream** | **NO — and now positively evidenced as absent, not merely unfound** | **`BR-01`, `BR-02`** |

**P10 delta: `MD-P06-01`, `MD-P06-02` — this is the row the delta changed.** Before this round P06 recorded a recognition-period date as *not found*. It is now `FACT VERIFIED` that **no recognition-period date is inherited into P06's surface, because no recognition entry is ever produced by a settlement and no deferral entry touches a receivable, payable or liquidity account**. The four-way date model P06 must carry is therefore **three dates, not four** — and the fourth is absent *by the reference's design*, which is a materially different statement from "we did not find it."

**Per the prompt: no missing date field was invented.**

### `CQ-P06-03` — Partial / full reconciliation state

**Disposition: `FACT VERIFIED`, and the answer is that less business truth changes than the state names imply.**

- Validating a bank match does **not** reconcile the suspense line — it **deletes and re-creates every line** of the statement entry (`04_` RM-F-01). Partial-vs-full is therefore not a refinement of one act; it is a different act.
- Pairing inside `_reconcile_plan` is **by sequence index, not by record id** (`04_` RM-F-03).
- `is_matched` is not a bank-confirmation fact and is **true by configuration in two of its branches** (`01_` PSM-F-04; four top-level branches, five assignment sites, per `REV-E-11`).
- **There is no field in the system that means "the bank confirmed this"** (`P06-B-06`, CRITICAL).

**P10 delta: `MD-P06-03`, `MD-P06-04`.** A new class of item enters this state machine: **an accrual and its structural reversal, created unreconciled, equal and opposite, same partner, same account, same currency** (`BR-03`, `BR-04`). Whether "reconciled" is the correct terminal state for that pair is **not a question the state machine can even ask**, because the pair is indistinguishable from a corrective pair. `P06-B-59`.

### `CQ-P06-04` — Correction / reversal algebra

**Disposition: `FACT VERIFIED` — NO. Silent divergence is possible, and this round found the mechanism.**

- `_reverse_moves` writes `reversed_entry_id` **identically** for a structural reversal and a corrective one; **no field records the reversal's type** (`BR-04`(a)).
- P06's auto-reconcile engine **never reads `reversed_entry_id`** — `grep -c` returns **0** in all three builds. Its one-to-one key is `[account_id, partner_id, currency_id, |amount_residual_currency|]` (`BR-04`(b)).
- `remove_move_reconcile()` is a one-line wrapper with no period-close guard (`04_` RM-F-20; `P06-B-46`, CRITICAL).
- Reset is blocked on hashed lines but **redirected to the destructive path** (`04_` RM-F-08).

**P10's `H06-4` is upheld and sharpened.** P06 will not match structural pairs through a design choice; **it will match them because the matching predicate has no expression in which the difference could appear.** `P06-B-59` — HIGH.

### `CQ-P06-05` — Duplicate / replay / import idempotency

**Disposition: `FACT VERIFIED` — the same evidence imported twice produces duplicate lines and duplicate posted entries, silently.**

Unchanged from round 1, and the strongest-reachability finding in the package: **7 of 8 duplicate-settlement attacks in `07_` are `CONFIRMED DEFECT`**; `P06-B-10` is CRITICAL with the precondition *"import a file twice"* (`46_` SEV-F-02).

**P10 delta: `NO P06 IMPACT`.** P10 asserts nothing about import idempotency and explicitly disclaims settlement opinions (`MD-P06-05`).

### `CQ-P06-06` — Operational / financial divergence

**Disposition: `FACT VERIFIED`, and the canonical question of this whole process is answered.**

> **PAYMENT STATE, ACCOUNTING POSTING STATE, BANK CONFIRMATION STATE and RECONCILIATION STATE are *not* four independently determinable states.** `01_` §0. A cash-type outstanding account jumps straight to `paid` with **no intermediate state, no bank event and no reconciliation** (`PSM-F-05a`). A move-less payment can drive an invoice to `in_payment`/`paid` **with a non-zero residual** (`PSM-F-13`). `in_payment` — the only expression of *"money left us but the bank has not confirmed"* — rests entirely on the configuration-dependent `is_matched` (`PSM-F-12`).

**P10 delta: `MD-P06-02` adds one divergence and closes it.** Invoiced value and recognised value diverge for the whole deferral window — but **that divergence never enters P06's matching surface**, because deferral moves value between the P&L account and the company deferral account only (`BR-02`). **P06 reconciles invoiced value. Confirmed, not assumed.**

### `CQ-P06-07` — Scope ownership

**Disposition: mixed, per object, per CORR1. Tenant+Company is *not* forced.**

`19_` and `50_` determine PLATFORM/TENANT/COMPANY per object across **30 objects**. Standing findings unchanged: bank accounts may exist with **no owning company** and are admitted into every company by three independent guards (`P06-B-26`, CRITICAL, `C3`); bank-event identity is enforced **database-globally** with no company domain (`P06-B-29`); `root_id` is a **fiscal/currency hierarchy, not a legal-entity boundary**, so the reconciliation guard names a boundary it cannot enforce (`22_`, `P06-B-27` CLOSED as a verified defect).

**P10 delta: `MD-P06-07` — `CONTRADICTED`, and it is a scope-*ownership* contradiction, not a scope-*rule* one.** P06 published that P10's `X-08` was *"closed by P06"*. **A dependency owned by a peer is not closed by the answering party.** P10's three registers still carry it `OPEN — PEER EVIDENCE` at `1fea562`. Corrected in place — `REV-E-18`.

### `CQ-P06-08` — Evidence integrity / terminality

**Disposition: `UNRESOLVED — EVIDENCE REQUIRED`, and this round moved it in both directions.**

**Strengthened:** all four new findings are **cross-version invariant across two generations and three builds** (`P06_P10_MATERIAL_DELTA_REGISTER.md` §4). Every negative in this round carries an executed positive control.

**Weakened, and recorded rather than hidden — five author errors this round:**

| ID | Defect |
|---|---|
| `REV-E-17` | A file-enumeration loop reported **`0 of 109`** when the true answer was **12**. Caught by contradiction with a known file, not by the control |
| `REV-E-18` | Seven P06 files claim a peer dependency is closed that the peer's latest register carries **OPEN** |
| `REV-E-19` | A **third** reference tree (`odoo-19.0+e.20260417`) existed and was undeclared. **Second occurrence** of this defect class after `REV-E-10` |
| `REV-E-20` | **Five statements across `11_`, `35_`, `36_` (×2), `39_` assert P08 is unpublished.** `53_` established in round 3 that it is published with 39 files and P06 quoted it by line. **None was edited; `62_` does not record it.** P01 was found stale the same way — **published at `b820b29`, unconsumed** (`P06-OQ-124`) |
| `REV-E-21` | Population executed twice, the second time because AAS-03 challenged the first denominator. Of **15** auditable prior corrections, **6 were never edited into their target registers — 13 statements across 8 files — and all six are from round 4.** Rounds 1–2 scored **7 of 7**. `20_` — origin file of the top CRITICAL blocker — carried two superseded claims and **zero correction markers**. `18_` — the handoff pack **built for P11** — carried five |

**`REV-E-21` is the reason `CQ-P06-08` cannot be dispositioned closed.** It is the *"a revision log is not a correction"* defect, found inside this package, three rounds after the package began recording that defect class in other people's work. **30 in-place corrections were applied this round across 15 register files.** Whether one unreviewed repair pass discharges the condition is put to AAS-03 and PMO — **it is not settled by the author who made both the errors and the repairs.**

---

## 2. Candidate INPUTS

*Tested, not assumed. Each row states what the reference actually supplies.*

| # | Candidate input | Does the reference supply it? | Label |
|---|---|---|---|
| `IN-01` | **Bank statement / external settlement evidence** | Yes — `account.bank.statement.line`, which **is a journal entry by delegation** (`02_` BER-F-01), counterpart forced to the journal suspense account, whose absence is a hard stop (BER-F-02) | `FACT VERIFIED` |
| `IN-02` | **A durable identity on that evidence** | **No, on 4 of 7 doors.** Where present it is namespaced by value, unconstrained, or positional (`02_` BER-F-04/05/07/08) | `FACT VERIFIED` (as an absence) |
| `IN-03` | **Payment / receipt settlement reference** | Yes — `account.payment`, but its state is **directly writable** (`01_` PSM-F-02), it can exist **with no journal entry** (PSM-F-07), and `action_post` posts nothing (PSM-F-05) | `FACT VERIFIED` |
| `IN-04` | **Upstream payable/receivable settlement-ready event** | Yes, as an open `account.move.line` residual on a `reconcile=True` account. **Carrying invoiced value, never recognised value** (`BR-02`) | `FACT VERIFIED` |
| `IN-05` | **A bank-confirmation input** | **No such input exists anywhere in the system.** `is_matched` is the nearest proxy and is true by configuration in two branches | `FACT VERIFIED` (as an absence) — `P06-B-06` CRITICAL |
| `IN-06` | **Correction / reversal reference** | Partially — `reversed_entry_id` links a pair, but **nothing records the reversal's type**, and P06's matcher never reads it | `FACT VERIFIED` — `P06-B-59` |
| `IN-07` | **Company / scope context** | Yes, but **not as a legal-entity boundary.** `root_id` is fiscal/currency; bank accounts may carry no company | `FACT VERIFIED` — `P06-B-26`, `P06-B-27` |
| `IN-08` | **Recognition-period context from upstream** | **No. Positively evidenced absent** (`BR-01`, `BR-02`), not merely unfound | `FACT VERIFIED` (as an absence) |
| `IN-09` | **Structural (non-corrective) accrual pairs entering the matching population** | **Yes, conditionally** — they arrive as two unreconciled, offsetting, partner-attributed lines. **Whether they enter depends on `account.reconcile`, which is chart-of-accounts configuration, not code** | `UNRESOLVED — EVIDENCE REQUIRED` — `P06-B-59`, `P06-B-60` |
| `IN-10` | **A settlement-triggered recognition event** | **No. The interface is empty, confirmed on P06's own evidence** | `FACT VERIFIED` (as an absence) |

## 3. PROCESS — semantic core, evidence-supported only

| # | Step | What the evidence supports | Label |
|---|---|---|---|
| `PR-01` | **Import / receive bank evidence** | Seven doors onto one object. Six silent-drop behaviours remove bank events with no record (`P06-B-14`). Statement-level controls are weaker than they appear: `balance_end_real` **defaults to the computed value** (BER-F-11), `is_valid` **is not persisted** (BER-F-13), the first statement of a journal is **unconditionally valid** (BER-F-14) | `FACT VERIFIED` |
| `PR-02` | **Identify / match** | Three rule types, order `sequence, id`, **first rule producing candidates wins** (RM-F-09). Text matching anchored over three fields (RM-F-10); the candidate query **strips all non-digits in the database** (RM-F-11); default lookback 18 months (RM-F-12). **A text-location toggle that finds nothing aborts the rule rather than falling back to amounts** (RM-F-14) | `FACT VERIFIED` |
| `PR-03` | **Partial / full reconcile** | Validating a match **deletes and re-creates every line** (RM-F-01); pairing is **by sequence index** (RM-F-03); exchange-difference recursion disabled (RM-F-02) | `FACT VERIFIED` |
| `PR-04` | **Auto-reconcile without an operator** | Grouping key `[account_id, partner_id, currency_id, \|amount_residual_currency\|]`, domain requires `account.reconcile = True` and non-zero residual. **`reversed_entry_id` is never consulted** | `FACT VERIFIED` — **this round** |
| `PR-05` | **Tolerance behaviour** | Defaults ON with a percentage type (RM-F-16). **Turning it OFF removes the check entirely and permits both write-off and auto-reconcile** — the control is inverted (RM-F-17, `P06-B-32`). Overpayment skips the check (RM-F-18). Shipped defaults are safe; **the exposure is a configuration change with no approval gate** (RM-F-19) | `FACT VERIFIED` |
| `PR-06` | **Unreconcile / correct** | `reconcile()` and `remove_move_reconcile()` are one-line wrappers (RM-F-20). **Reconciling and un-reconciling sit outside the entire period-close regime**, and the one indirect block fires on the wrong move (`28_` PC-F-07, `64_`; CRITICAL) | `FACT VERIFIED` |
| `PR-07` | **Preserve audit lineage** | Identity fields are **mutable with no journal-entry trace**; only **6 fields** synchronise to the entry (BER-F-18/19; `P06-B-13` CRITICAL). And `om_data_remove` — **proven `installed`** on a v19 database (`58_` DMR-F-01) — removes bank statements, payments, moves, partial reconciles **and chatter** by unfiltered SQL, per-table commit, errors swallowed, **with no server-side authorisation on the dispatch chain** (`44_`, `45_`, `49_`; `P06-B-50` CRITICAL) | `FACT VERIFIED` |

**`PR-08` — the step the reference does not have.** There is **no** *"confirm against the bank"* step. `PR-01`…`PR-07` describe a process that reconciles internal records against an internal representation of a bank file. **The word "reconciliation" in this system does not mean what a treasurer means by it.** `SUPPORTED INTERPRETATION`, and it is the round-1 headline, unchanged.

## 4. Candidate OUTPUTS

| # | Candidate output | Evidence status | Label |
|---|---|---|---|
| `OU-01` | Reconciliation state changed | Produced, but **not persisted as a widget/state object** (RM-F-04); derived from the presence of the suspense account (RM-F-05) | `FACT VERIFIED` |
| `OU-02` | Settlement matched / unmatched state | Produced as `is_matched`, which **is not a bank-confirmation fact** | `FACT VERIFIED`, with a named defect |
| `OU-03` | Residual / open amount state | Produced (`amount_residual`, `amount_residual_currency`). **Reflects invoiced value** (`BR-02`) | `FACT VERIFIED` |
| `OU-04` | Exchange-difference consequence | Produced, with recursion disabled inside `_reconcile_plan` (RM-F-02). **FX rate source and missing-rate policy are undecided** — `P06-B-08`, `UNRANKED` because the policy does not yet exist | `BOSS DECISION REQUIRED` |
| `OU-05` | Correction / reversal event | Produced, **untyped** (`BR-04`) | `FACT VERIFIED` — `P06-B-59` |
| `OU-06` | Reconciliation audit evidence | Produced, **and destructible** — see `PR-07` | `FACT VERIFIED` |
| `OU-07` | **A bank-confirmed settlement assertion** | **Not produced. No such output exists** | `FACT VERIFIED` (as an absence) |
| `OU-08` | **A statement that a matched pair was *economically* offsetting rather than *structurally* offsetting** | **Not produced, and not producible from the current predicate** | `FACT VERIFIED` (as an absence) — **this round** |

## 5. Candidate HANDOFFS

For each material output: probable consumer · business meaning · required payload semantics · **what the consumer must NOT assume** · unresolved ownership/date/scope questions.

### `HO-01` → **P11 Core Reconciliation** — reconciliation state and residual

- **Business meaning:** which obligations remain open, and by how much.
- **Required payload semantics:** the residual **and its basis** — invoiced, posted, in the company currency, at the reconciliation date.
- **MUST NOT ASSUME:** that a zero residual means the bank confirmed anything (`IN-05`, `OU-07`); that `is_matched` is a bank fact; that a `paid` payment has a journal entry (`PSM-F-07`); that partial→full is a refinement of one act rather than a delete-and-recreate (`RM-F-01`).
- **Unresolved:** FX rate source and missing-rate policy — `BOSS DECISION REQUIRED` (`P06-B-08`).

### `HO-02` → **P11 / P08** — reversal and correction events

- **Business meaning:** a prior accounting effect has been undone.
- **Required payload semantics:** the pair link **and a reversal type**, because the type is what tells a consumer whether the ledger position changed economically.
- **MUST NOT ASSUME:** that `reversed_entry_id` distinguishes a correction from a structural reversal — **it does not, and P06's own matcher does not read it** (`BR-04`).
- **Unresolved:** who owns the reversal *type*. It cannot be P06 alone: P06 sees the pair, not the intent. **`P06-OQ-122`**, routed to P11.
- **Label:** `DESIGN CANDIDATE — PHASE S ONLY` for the type field; `FACT VERIFIED` for its absence.

### `HO-03` → **P10 Time-Based Recognition** — the empty interface, now confirmed

- **Business meaning:** P06 confirms, on its own evidence, that **it produces no input to recognition and consumes none from it.**
- **Required payload semantics:** none. **The correct payload is empty, and that is the finding.**
- **MUST NOT ASSUME:** that because the interface is empty at the *event* level it is empty at the *population* level. **It is not.** The accrual/structural-reversal pair produced by P10's domain **arrives in P06's reconciliation population** whenever the accrual account is `reconcile=True` — and P06 cannot tell it apart from a correction (`BR-03`, `BR-04`). **Detection of the superseded accrual is P10's (`F-05`, `AL-6`); the matching consequence is P06's.** That split is P06's position, not a determination.
- **Unresolved:** whether the accrual account is `reconcile=True` in any target deployment — configuration, not source. **`P06-B-60`**, `UNRESOLVED — EVIDENCE REQUIRED`.

### `HO-04` → **P10** — the `X-08` answer, re-delivered

- **Business meaning:** bank-side prepayments and interest accruals. **P06's substantive answer stands: the object does not exist in the reference for either process; P06 recommends the boundary at accrual (P10) versus receipt (P06). That is a recommendation, not a determination.**
- **MUST NOT ASSUME:** that P06 closed it. **P06 previously wrote that it had, and that was wrong** (`REV-E-18`). **The dependency is P10's to close.**

### `HO-05` → **P11 / Boss** — the destructive-path risk

- **Business meaning:** a proven-installed module deletes the reconciliation ledger by unfiltered SQL with no server-side authorisation.
- **MUST NOT ASSUME:** that *installed* means *fired*. The strongest evidence that it fired is `om_data_remove_fix`'s own manifest, which is `SUPPORTED INTERPRETATION`, **not** `FACT VERIFIED` (`58_` DMR-F-04). **No `ir_logging`, `odoo.log` or journald artefact was ever located.**
- **Unresolved:** installed on the **SMEsPlus target**? `P06-OQ-98`, still `HOLD`. Highest-value unrun query remains `P06-OQ-112`.

### `HO-06` → **P07 TH Tax Compliance** — unchanged

Carried forward from `54_` without re-opening. **No P10 delta touches it.**

---

## 6. What this pack is not

- Not a contract of any kind. **No `FINAL INPUT CONTRACT` or `FINAL OUTPUT CONTRACT` language appears in this file, and none is implied.**
- Not an architecture. Not a schema. Not an API. Not a UI.
- Not a claim that PHASE B may begin.
- Not a whole-G02 statement. **P06 speaks only for P06.**
