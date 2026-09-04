# E01 — EVIDENCE CORRECTIONS AND EXTENSIONS (LAYER 2 / AUDIT QUARANTINE)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001` · supersedes the named parts of `E00`

> **CLASSIFICATION — LAYER 2 / AUDIT QUARANTINE.** Same handling as `E00`.

These corrections arose from the independent expert reviews. Each was **re-verified against primary
source by the research team before acceptance** — an expert report is not accepted on its own
authority. Where an expert's conclusion was itself imprecise, the correction says so.

Corrections are recorded additively. `E00` is not rewritten, so the original claim and its
correction both remain visible.

---

## COR-01 — `EV-016` supporting negative is WRONG. A fiscal year entity exists.

**Original claim (`EV-016`):** a search for a fiscal-year model across the reference tree returns no
result; the fiscal year exists only as two integers on the company.

**Status: CONTRADICTED.** Raised by Expert 1, re-verified by the research team.

**Corrected fact — VERIFIED FACT.** `account_accountant/models/account_fiscal_year.py:11-55`
defines a fiscal-year model with a name, a start date, an end date and an owning company. It
enforces that the end date is not before the start date, that **child companies may not have fiscal
years**, and that two fiscal years of one company **may not overlap** (three interleaving cases
tested explicitly).

**Root cause of the error.** The research team searched for the token `account.fiscalyear`. The
model is named `account.fiscal.year`. The search was too narrow and the negative was reported at
tree scope rather than at the scope actually searched — the exact failure mode this project's
standing rule on negatives exists to prevent.

**What the corrected evidence shows — and why the `EV-016` conclusion survives.**

| Property | Finding | Citation |
|---|---|---|
| Where it lives | The advanced accounting module, **not** the core module | `account_accountant/models/__init__.py:7` |
| How it is reached | Behind a dedicated group and a settings toggle | `views/account_accountant_menuitems.xml:6`, `views/res_config_settings_views.xml:26` |
| Who may change it | The accounting-manager group holds full create, write **and delete** rights | `account_accountant/security/ir.model.access.csv:9` — `1,1,1,1` |
| What consumes it | Only the derivation of year boundaries, and fiscal-year grouping of currency rates | `account_accountant/models/res_company.py:162,185,193`; `account_accountant/models/res_currency.py:10` |
| What it does NOT have | No state, no close action, no posting, no balance, no relationship to any lock date, no link from any entry | verified by the consumer search above |

**Corrected conclusion.** A fiscal-year entity exists, but it is an **optional, fully mutable,
deletable period-definition override** whose only job is to answer "what are this year's dates" when
the two company integers are insufficient (a 52/53-week year, a stub year). It is a **calendar
record, not a period-control object**.

Therefore the load-bearing parts of `EV-016` stand unchanged and are re-affirmed:
- there is still **no year-end closing entry** anywhere in the tree;
- the current-year result is still computed **at report time**, not posted;
- a period is still "closed" only to the extent a lock date covers it;
- month 12 is still procedurally identical to any other month.

`INFERENCE:` the correction actually strengthens the finding. The reference system has a fiscal-year
*object* and still chose not to attach closing, locking, or state to it. That is a deliberate
architectural position, not an omission.

---

## COR-02 — `EV-009` cited the wrong code path, and understated the behaviour.

**Original claim (`EV-009`):** on create, an entry dated in a locked period has its date silently
rewritten to lock date + 1 day.

**Status: CONFIRMED WITH CAVEAT — mechanism mis-cited, conclusion understated.** Raised by
Expert 1, re-verified by the research team.

**Corrected fact — VERIFIED FACT.** The cited code at `account_move.py:3113-3131` is inside
`copy_data`. It therefore governs **duplication and reversal**, not ordinary creation. For that path
the original description is accurate.

The accounting date is actually moved by **three independent mechanisms**:

| # | Trigger | Rule | Lock required? | Citation |
|---|---|---|---|---|
| 1 | Duplicating or reversing an entry | date ≤ effective lock → date becomes lock + 1 day | **yes** | `account_move.py:3127-3129` |
| 2 | **Any change to the document date on a non-sale document** (vendor bills and similar) | the accounting date is recomputed from the document date via `_get_accounting_date` | **no — this fires with no lock date set at all** | `account_move.py:800-815` (`_compute_date`) |
| 3 | Posting, when a lock date is violated | accounting date recomputed via `_get_accounting_date` | **yes** | `account_move.py:4933-4936` |

`_get_accounting_date` (`account_move.py:5655-5691`) does **not** return lock + 1. It returns
**lock + 1 pushed to the end of that period**, and for sale documents it caps the result at today.
For non-sale documents with no lock at all, when the current month is later than the document month,
it returns **the last day of the document's own month**.

**Worked consequence — VERIFIED FACT.** A vendor bill dated 15 January, entered on 3 March, in a
system with **no lock dates configured**, is booked with an accounting date of **31 January**.
The stated purpose in the method's own documentation is to keep the number series increasing.

**Corrected conclusion.** The original conclusion is not merely correct, it was too weak. The
accounting date is **not a user input on any document carrying a document date** — it is a
system-derived value, governed partly by an accounting control (the lock) and partly by a
**numbering-convenience rule that has no accounting justification at all**.

This makes the finding materially more serious. A tenant that has configured no locks whatsoever
still has its period attribution silently altered.

`RECOMMENDATION:` mechanism 2 should be classified `REJECT` outright for SMEsPlus. Subordinating
period attribution to sequence monotonicity inverts the correct dependency: the number should
follow the period, never the reverse.

---

## COR-03 — `EV-003` unknown is resolved. Deprecated accounts ARE blocked from posting.

**Original claim (`EV-003`):** whether the deprecation flag blocks posting is
`UNKNOWN — EVIDENCE REQUIRED`; the flag appears only in selection domains.

**Status: RESOLVED — original caution was correct but the answer is available.** Raised by
Expert 1, re-verified by the research team.

**Corrected fact — VERIFIED FACT.** Posting to a deprecated account is refused in three places:

| Guard | Effect | Citation |
|---|---|---|
| Entry validation at posting | posting is refused if any item names a deprecated account | `account_move.py:4911-4912` |
| Item creation | refused | `account_move_line.py:1212-1213` |
| Item write | refused | `account_move_line.py:1550-1552` |

Two of the three share a context bypass (`skip_account_deprecation_check`); the write guard at
`:1550-1552` has **no bypass** and is therefore the strongest of the three.

**Residual gap — this part of `EV-003` stands.** There is still **no guard preventing deprecation of
an account that holds a non-zero balance, unreconciled items, or is nominated as a journal default**.
The only precondition remains the tax-distribution check (`account_account.py:1027`).

**Corrected conclusion.** The flag is stronger than the original evidence credited: it is a genuine
posting block, not merely a picker filter. But it remains a *single* flag doing the work of three
distinct lifecycle states, and it can be set on an account that is still carrying value.

---

## COR-04 — `EV-021` "append-only" is wrong. Lock exceptions are revocable by the granting role.

**Original claim (`EV-021`):** exceptions are append-only — accounting managers may create but not
write or delete them.

**Status: CONTRADICTED in part.** Raised by Expert 1, re-verified by the research team.

**Corrected fact — VERIFIED FACT.** `account_lock_exception.py:258-266` defines a revoke action
which checks that the caller holds the accounting-manager group and then writes
`active = False` and an end date-time **through elevated privilege**, deliberately escalating past
the `write = 0` access rule that the original claim cited as its proof of append-only behaviour.

**Corrected conclusion.** The access-control row does not mean what `E00` said it meant. The same
single role **grants and revokes** exceptions. There is no segregation of duties on the override
control at all.

The parts of `EV-021` that stand, re-verified: the reason field remains optional; an exception with
no user applies to every user; an exception with no end date-time is valid indefinitely; creation is
written to the company's message thread with before/after tracking values.

`RECOMMENDATION:` this moves the lock-exception control from "well shaped but under-justified" to
"structurally unsound as a segregation-of-duties control". For SMEsPlus, granting an override and
revoking one are different authorities, and neither should be the authority that posts.

---

## COR-05 — `EV-002` extended: a unique constraint on account code is not merely absent, it is not expressible.

**Original claim (`EV-002`):** account code uniqueness has no database constraint and is enforced
only in application code.

**Status: CONFIRMED AND EXTENDED.** Raised by Expert 2, re-verified by the research team.

**Extension — VERIFIED FACT.** The code is held in a company-dependent field. The framework stores
company-dependent values as a JSON-typed column keyed by company. A conventional unique index over
"the code within a company" is therefore not expressible against that storage form without a
functional index per company.

**Extension — VERIFIED FACT.** `account_account.py:1074-1084` performs its duplicate search with an
ordinary unlocked read. Two concurrent transactions under standard read-committed isolation can each
observe no duplicate and both commit.

**Corrected conclusion.** The original finding characterised this as a missing constraint that could
be added. It cannot be added in that form. The absence is a **consequence of the chosen storage
shape**, which means for SMEsPlus the decision is upstream of the constraint: either the code is
per-company and uniqueness is enforced by a different structure, or the code is global and can carry
a conventional constraint. This is a modelling decision, not a hardening task.

---

## COR-06 — `CONTRA-01` is wider than `EV-010` stated, and must be split in two.

**Original claim (`EV-010`):** the integrity hash omits the transaction-currency amount, so it can
be changed on a secured entry without detection.

**Status: CONFIRMED AND EXTENDED — but Expert 2's stronger formulation requires one correction.**
Raised by Expert 2, re-verified by the research team.

**Extension — VERIFIED FACT.** The write guard at `account_move_line.py:1554-1563` computes the
violated set from the **raw incoming keys**, and only afterwards, at `:1566`, are those values
normalised by `_sanitize_vals`. That normalisation (`:1434-1441`) collapses debit and credit writes
into the canonical `balance`. Because `balance` is not a hashed field name, a write expressed as
`balance` **passes the guard**, while the identical economic change expressed as `debit` is refused.

**Correction to the expert's conclusion.** Expert 2 concluded from this that "the hash is not sound
single-currency either". That overstates it. The guard fails open, but the **detector does not**: the
integrity report recomputes the hash from debit and credit, which are derived from balance, so a
balance edit changes the recomputed hash and **is** detected. The two failures are different and
must not be merged:

| Field written on a hashed entry | Blocked by the write guard? | Detected by the integrity report? | Severity |
|---|---|---|---|
| `debit` / `credit` / `account` / `partner` / entry number / date / journal | **yes** | yes | controlled |
| `balance` | **no** | **yes** | guard defect — tamper-evident but not tamper-resistant |
| `amount_currency` (magnitude) | **no** | **no** | **true integrity hole** |
| `currency_id` | no | no | true integrity hole |
| tax fields, analytic distribution, due date | no | no | true integrity hole |

**Further extension — VERIFIED FACT, partially mitigating.** `account_move_line.py:436-448` declares
a genuine database CHECK requiring the transaction-currency amount and the balance to carry the
**same sign**. The transaction-currency amount therefore cannot be sign-flipped independently. Its
**magnitude** remains freely changeable.

**Corrected conclusion.** `CONTRA-01` splits into `CONTRA-01a` (guard defect on the canonical amount
field — tamper-evident, not tamper-resistant) and `CONTRA-01b` (genuine integrity hole on the
transaction-currency magnitude, the currency itself, and the tax and analytic dimensions). `CONTRA-01b`
remains the more serious of the two and is unchanged in substance from `E00`.

---

## COR-07 — New: the double-entry invariant has no database constraint and is switchable off.

**Status: NEW — VERIFIED FACT.** Raised by Expert 2, re-verified by the research team.

`account_move.py:2329-2354` — the balanced-entry assertion is a Python context manager wrapped around
create and write. Its first action is to consult a recursion-disabling helper keyed on
`check_move_validity`; when that key is set, the manager **yields and then returns without
performing any check**. The entry model declares **no** database constraint enforcing that debits
equal credits.

By contrast `account_move_line.py:429-458` declares **four genuine database CHECK constraints** at
item level: that debit and credit are not both non-zero; that the transaction-currency amount and
the balance share a sign; that an accountable item names an account; and that a non-accountable item
carries no amounts or account.

**Conclusion — the control tiering is inverted.** The most consequential invariant in double-entry
accounting is an application check with a documented disable path, while four lesser, item-local
rules are storage-level guarantees that nothing can bypass.

`INFERENCE:` the contrast is evidence of intent rather than oversight — where the authors wanted a
storage-level guarantee they wrote one, including on the currency-rate table
(`base/models/res_currency.py:368-371`). The entry-balance invariant was left switchable on purpose,
presumably to permit multi-step construction. For SMEsPlus this is the single clearest candidate for
a `Tolerance = 0` designation under constitution principle 13.

---

## COR-08 — New: account merge deletes by raw statement, bypassing the ORM's own deletion guards.

**Status: NEW — VERIFIED FACT.** Raised by Expert 1 and Expert 2 independently; re-verified.

`wizard/account_merge_wizard.py:194-203` — merged accounts are removed by a directly executed
`DELETE FROM` statement against the account table.

Because no ORM deletion runs, the model's own deletion guards do not execute — including the guard
that forbids removing an account that still has journal items
(`account_account.py:1095-1098`). No change tracking is written, and the wizard contains no logging
call of any kind.

**Conclusion.** `EV-004` described this as a provenance trade-off. It is more than that: it is a
control bypass. An accounting manager can, in one action with no approval and no recorded trace,
delete an account that carries posted history, with the history silently retargeted.

`RECOMMENDATION:` reinforces the `REJECT` already recorded against `EV-004`, and raises it to a
second `Tolerance = 0` candidate.

---

## COR-09 — New: nothing bounds a reconciliation against the item it reconciles.

**Status: NEW — VERIFIED FACT.** Raised by Expert 2, re-verified by the research team.

The partial-reconciliation model declares **no** database constraints (verified: zero occurrences of
a constraint block in `account_partial_reconcile.py`). Its only declarative validation is that both
sides carry a resolved transaction currency (`:69-73`).

Nothing at storage level prevents the matched amount from exceeding the residual of either item.

**Conclusion.** Over-reconciliation is structurally reachable, and — correcting the framing in
`EV-014` — this is **not** limited to multi-currency situations; it applies to any configuration.
The residual and reconciled flags are stored-computed values derived from these unconstrained
records, so a bad match propagates into the settlement state and from there into ageing and payment
state.

---

## Corrections summary

| Ref | Target | Verdict | Raised by | Re-verified |
|---|---|---|---|---|
| `COR-01` | `EV-016` supporting negative | `CONTRADICTED` — conclusion survives, and is strengthened | Expert 1 | yes |
| `COR-02` | `EV-009` mechanism | `CONFIRMED WITH CAVEAT` — mis-cited, and understated | Expert 1 | yes |
| `COR-03` | `EV-003` unknown | `RESOLVED` — posting is blocked; residual gap stands | Expert 1 | yes |
| `COR-04` | `EV-021` append-only | `CONTRADICTED` in part — same role grants and revokes | Expert 1 | yes |
| `COR-05` | `EV-002` | `CONFIRMED AND EXTENDED` — a constraint is not expressible | Expert 2 | yes |
| `COR-06` | `EV-010` / `CONTRA-01` | `CONFIRMED AND EXTENDED`, split in two; expert's stronger claim corrected | Expert 2 | yes |
| `COR-07` | new | `VERIFIED FACT` — entry balance invariant is switchable | Expert 2 | yes |
| `COR-08` | `EV-004` | `VERIFIED FACT` — deletion bypasses ORM guards | Experts 1 and 2 | yes |
| `COR-09` | `EV-014` | `VERIFIED FACT` — reconciliation amounts unbounded | Expert 2 | yes |

**Research-team note on method.** Four of the nine corrections invalidate or materially qualify a
research-team claim, and two of those were negatives asserted at a wider scope than was actually
searched — the same defect this project has recorded before. The independent review requirement in
constitution principle 7 did its job here; the evidence base as first written would have carried two
wrong statements into the gate package.

---

# PART 2 — CORRECTIONS ARISING FROM THE INDEPENDENT CHALLENGE UNIT

Each re-verified against primary source by the research team before acceptance.

---

## COR-10 — `EV-018` is CONTRADICTED. Rate types exist, and the research team's own deferral was answerable in a module it had declared verified.

**Original claim (`EV-018`):** the reference model has one rate per currency per day per company
group and **no rate-type dimension** — no separate spot, average, closing or historical rate. The
team additionally deferred the question "whether the reporting layer synthesises an average rate" to
Wave G as `UNKNOWN — EVIDENCE REQUIRED`.

**Status: CONTRADICTED.** Raised by the challenge unit, re-verified by the research team.

**Corrected fact — VERIFIED FACT.** `account/models/res_currency.py:105-160` builds a temporary
currency table whose columns include an explicit `rate_type`, populated with four named types:
`current`, `closing`, `historical` and `average`. Separate builders exist for each
(`_get_table_builder_closing`, `_get_table_builder_historical`, `_get_table_builder_average`,
`_get_table_builder_current`), selected by a "use cumulative-translation-adjustment rates" flag, and
indexed by `(company, rate_type, date_from, date_next)`.

**The corrected two-level position:**

| Level | Finding | Status |
|---|---|---|
| **Storage** | one scalar rate per currency per day per company root, with genuine database constraints | `EV-018` **stands unchanged** |
| **Derivation** | closing, historical and average rates **are synthesised at query time** from that daily series, for consolidation and translation | `EV-018` was **wrong** to state no rate-type dimension exists |

**Root cause of the error.** The research team read the framework's rate model and the account
module's rate extension, but not the account module's currency-table builder. The claim was then
asserted at system scope on the strength of a partial read of a source the evidence base had listed
as verified. This is the second scope-over-reach in this session, after `COR-01`.

**Corrected conclusion — and it is a better one.** The reference model demonstrates the correct
separation: **measurement is stored once, per date; valuation bases are derived per reporting
purpose.** A closing rate is not a second stored fact, it is a selection rule over the same series.

This materially changes two Wave A positions:
- `H-13` (close-date rate) and `H-15` (historical-rate requirement) in the coverage register move
  from `NC` to **`PC` — a derivation mechanism exists, gated behind a consolidation flag**;
- `GAP-H01` (no carrier for revaluation) must be re-scoped: no *posting* mechanism for unrealised FX
  was found, but a *valuation* mechanism exists. Those are different absences.

`RECOMMENDATION:` SMEsPlus should adopt the separation (`ADAPT`) — one dated measurement series, with
named valuation bases derived from it — rather than storing multiple rate types, which would create
four facts where one exists and three reconciliation problems that do not need to exist.

---

## COR-11 — NEW: the integrity hash serialises company-currency amounts at the wrong currency's precision.

**Status: NEW — VERIFIED FACT.** Raised by the challenge unit, re-verified by the research team.

`account_move.py:3996-4002` — the hash serialiser formats any monetary field through a fixed-decimal
representation using **`obj.currency_id.decimal_places`**, where `obj` is the record carrying the
field.

For a journal item, `currency_id` is the **transaction** currency (`account_move_line.py:143-147`,
required on every item). But `debit` and `credit` are denominated in the **company** currency
(`account_move_line.py:113-121`, `currency_field='company_currency_id'`).

**Consequence — VERIFIED FACT.** The two hashed amount fields are rounded for hashing at the decimal
precision of a *different* currency from the one they are expressed in. Where the transaction
currency carries fewer decimal places than the company currency, two materially different
company-currency amounts serialise identically and therefore **produce the same hash**.

`INFERENCE:` this is a hash *collision* vector, not merely a cosmetic defect. It reduces the
effective protection on the two fields the hash exists to protect, in exactly the multi-currency
scenario where `CONTRA-01b` already applies. The two defects compound: the transaction-currency
magnitude is unprotected, and the company-currency amounts are protected only to the transaction
currency's precision.

Recorded as `CONTRA-06`.

---

## COR-12 — NEW: the hash chain is keyed on database row identifiers.

**Status: NEW — VERIFIED FACT.** Raised by the challenge unit, re-verified against
`account_move.py:4014-4017`, which composes each per-item hash key as `line_<row id>_<field>`.

**Consequences.**

1. **Migration.** Any process that reproduces a ledger with different row identifiers — a migration,
   a tenant split or merge, a restore into a different database — produces different hashes for
   identical accounting content. The chain cannot be carried across such a boundary, and cannot be
   used to prove that a migrated ledger matches its source.
2. **Chain scope.** The chain is scoped per journal and per number prefix
   (`account_move.py:3893-3899`), so it does not span periods or years, and a prefix change starts a
   new chain.

`INFERENCE:` for a SaaS programme whose stated purpose includes migrating existing books, a
tamper-evidence mechanism that cannot survive migration is of limited value at exactly the moment
assurance is most needed. If SMEsPlus adopts chained hashing (`EXTEND`), the chain must be keyed on
**business identity** — the accounting event identity recommended in file 06 — not on storage
identifiers.

Recorded as `CONTRA-07`.

---

## COR-13 — NEW: Thai localization primary source is present in the build and was not examined.

**Status: NEW — EVIDENCE AVAILABILITY CORRECTION.** Raised by the challenge unit, confirmed by the
research team.

Two Thai localization modules are present in the same verified build and were **not listed in the
`EV-000` source registry and not read**: `l10n_th` and `l10n_th_reports`.

**Why this matters procedurally.** This project has a standing rule, arising from a prior session,
that a negative must never be asserted from a partial search, and that primary source is to be
located before capability claims are made. Wave A routed every Thai statutory question to the
Accounting-Tax track as `HOLD / EVIDENCE REQUIRED` — which remains correct, because **statutory
interpretation is not this session's authority regardless of what source is available**. But the
package should have recorded that Thai localization *implementation* evidence exists and is
readable, rather than leaving the impression that no such source was available.

**Status of Thai statutory questions — unchanged.** All remain `HOLD / EVIDENCE REQUIRED` and routed
to the Accounting-Tax track. Reading a localization module would establish *what the reference
implementation does*; it would not establish *what Thai law requires*. Those are different claims and
this session may make only the first.

**One item flagged by the challenge unit for the Accounting-Tax track**, recorded here as a pointer
only and **not adjudicated by this session**: the withholding-tax reporting extract is driven by the
same accounting date that `COR-02` shows to be system-derived rather than user-owned. If that is
correct, then the re-dating behaviour has a direct statutory-reporting consequence. `WAVE-D TAX`
owns this question; Wave A raises it and stops.

---

## Corrections summary — Part 2

| Ref | Target | Verdict | Raised by | Re-verified |
|---|---|---|---|---|
| `COR-10` | `EV-018` | `CONTRADICTED` — rate types are derived, not absent | Challenge unit | yes |
| `COR-11` | new | `VERIFIED FACT` — hash rounds at the wrong currency's precision | Challenge unit | yes |
| `COR-12` | new | `VERIFIED FACT` — hash chain keyed on row identifiers | Challenge unit | yes |
| `COR-13` | `EV-000` | evidence-availability correction — Thai localization source present, unexamined | Challenge unit | confirmed |

## Session note on evidence method — required reading for the gate

Across both parts, **thirteen corrections** were accepted, of which **four contradicted a
research-team claim** (`COR-01`, `COR-04`, `COR-10`, and `COR-02` in part). Three of the four were
**negatives asserted at a wider scope than was actually searched**:

| Correction | The over-reach |
|---|---|
| `COR-01` | "no fiscal-year model in the tree" — one token spelling was searched |
| `COR-10` | "no rate-type dimension" — one file in a module was read, the conclusion drawn for the system |
| `COR-13` | Thai localization source present and not registered |

This is the same defect this project has recorded before, and it recurred here despite the rule being
known. The mitigation that worked was **not** more careful reading by the original team — it was the
constitutional requirement that independent reviewers verify the work. Recorded so the gate can weigh
the evidence base accordingly: its positive findings were re-verified and held; its **negative**
findings should be treated as the weaker class and re-scoped before reliance.

---

# PART 3 — CORRECTIONS ARISING FROM EXPERT REVIEWS 3 AND 4

Each re-verified against primary source by the research team before acceptance.

---

## COR-14 — NEW AND SEVERE: a missing exchange rate silently converts at 1:1.

**Status: NEW — VERIFIED FACT.** Raised by Expert 3, re-verified by the research team.

`base/models/res_currency.py:121-141` — rate resolution selects the latest rate dated on or before
the requested date; failing that, the earliest rate that exists for the currency; failing that, the
literal value **`1.0`**, supplied by a `COALESCE` in the query itself.

**Consequence.** A foreign-currency posting made against a currency for which **no rate has ever been
entered** is converted at par. No error is raised, no warning is shown, and the resulting entry is
internally consistent: the item balances, the entry balances, and every downstream control passes.
The corruption is invisible to every mechanism Wave A examined, including the integrity hash.

`INFERENCE:` this is the most dangerous single behaviour found in this Wave, because it is silent,
it produces a *valid-looking* result, and it is most likely to occur exactly when a tenant transacts
in a new currency for the first time — that is, during onboarding and migration.

`RECOMMENDATION:` classify `REJECT` without qualification. In SMEsPlus, an unavailable measurement
must halt the posting. A default of 1.0 asserts an exchange rate the business never agreed to.

Recorded as `CONTRA-08`. Third `Tolerance = 0` candidate.

---

## COR-15 — `EV-022` understated: the posted-entry freeze is routinely bypassed in production paths.

**Status: CONFIRMED AND EXTENDED.** Raised by Expert 4, re-verified.

`EV-022` described the posted-entry field freeze as an application guard "with a documented context
bypass", which implied an exceptional escape hatch.

**Corrected fact — VERIFIED FACT.** The bypass is used at **seven non-test production sites**, all in
the bank-statement and reconciliation paths — `account/models/account_bank_statement_line.py:441`,
`:483`, `:803`, `:845`; `account_accountant/models/bank_rec_widget.py:1411`, `:1458`;
`account_accountant/models/account_move.py:130`. At `:441` it is applied **unconditionally to every
write** of a statement line's entry.

**Corrected conclusion.** The posted invariant is not owned by the ledger. It is owned by whichever
module is calling, and one core module opts out of it as a matter of routine. For SMEsPlus this
means a posted-state guard implemented as a caller-suppressible check is not a control at all.

---

## COR-16 — `EV-007` CONTRADICTED in both directions: not tenant-writable, but worse than tenant-wide.

**Status: CONTRADICTED.** Raised by Expert 4, re-verified.

`EV-007` claimed the numbering/date-alignment control could be disabled by a **tenant-writable**
configuration value, "tenant-wide".

**Corrected fact — VERIFIED FACT.** Both halves are wrong:

| `EV-007` said | Actually |
|---|---|
| tenant-writable | requires the system-administrator group — **not** available to a tenant accountant |
| tenant-wide | the configuration-parameter store has **no company dimension at all**, so in a shared database a single write disables the control for **every tenant in that database** |

**Corrected conclusion.** The finding survives and becomes a **SaaS boundary** finding rather than a
tenant-control finding. The blast radius is larger than originally stated and the actor is more
privileged. Re-filed against file 16 rather than file 14.

---

## COR-17 — `EV-015` qualified: the tax lock rejects rather than relocates.

**Status: CONFIRMED WITH CAVEAT.** Raised by Expert 3, re-verified.

`EV-015` stated that a cash-basis tax entry whose natural period is locked is dated today.

**Corrected fact.** Date *selection* consults only the fiscal lock
(`account_partial_reconcile.py:512-514`), so `EV-015` is correct for that comparison. But the
subsequent write is checked against the **tax** lock (`account_move.py:3283`), which **raises**.

**Consequence — the corrected behaviour is a third outcome, not either of the two originally
described.** In the window where the reconciliation date is after the fiscal lock but on or before
the tax lock, the reconciliation **hard-fails**. The user is not told that a settlement was refused
because of a tax-period boundary; they are told an entry could not be written.

`EV-015` remains correct for the fiscal-lock relocation of exchange-difference reversals.

---

## COR-18 — `EV-020` trigger corrected: the ceiling is a company identifier, not a company count.

**Status: CONFIRMED WITH CAVEAT.** Raised by Expert 4, re-verified.

`EV-020` said the per-company code encoding aliases "once a deployment holds ten thousand or more
company records".

**Corrected fact.** The encoding fails once any company's **identifier** reaches 10,000. Identifiers
are allocated monotonically and are **not reused after deletion**, so the threshold is reached by
cumulative company creation over the life of the database, not by the number of companies currently
existing. A deployment holding a few hundred live companies can cross it.

The finding is therefore **more likely to occur, and sooner**, than `EV-020` stated.

---

## COR-19 — `EV-011` qualified: both immutability switches are one-way ratchets that default off.

**Status: CONFIRMED WITH CAVEAT.** Raised by Expert 4, re-verified.

Both the per-journal hashing flag and the per-company deletion-protection flag can be turned **on**
and then not turned off (`account_journal.py:651-658`; `company.py:317-321`).

**Consequence.** The risk is not a runtime toggle — it is fixed at **tenant provisioning** and at
**first posting**. That is a better risk profile than `EV-011` implied, and it sharpens the SMEsPlus
requirement: the decision is a provisioning-time default, and a default of "off" is unrecoverable for
every entry posted before someone notices.

---

## COR-20 — NEW: the Thai statutory extracts are driven by the system-derived accounting date.

**Status: NEW — VERIFIED FACT as to implementation. STATUTORY CONSEQUENCE: `HOLD / EVIDENCE REQUIRED`.**
Raised by Expert 3.

Both Thai statutory extracts in `l10n_th_reports` select the filing population by, and print, the
**accounting date** — the field `COR-02` shows to be system-derived — while labelling it as the
document date. The withholding-tax extract additionally **recomputes the tax amount from the
configured rate** rather than reading the posted balance, and infers the payment nature from a
hard-coded rate map.

**What this session may and may not conclude.**
- May conclude, and does: *as implemented in the reference localization*, the filing population and
  the printed date derive from a value the user does not control, and the filed amount is not read
  from the ledger.
- **May not conclude:** whether that satisfies or breaches Thai requirements. That is
  `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track, and it is `WAVE-D TAX` scope.

Thai account and report names encountered remain **candidate / UNVALIDATED**.

`RECOMMENDATION:` this is the concrete chain that makes `COR-02` a governance matter rather than a
usability one, and it should be the first item the Accounting-Tax track receives from Wave A.

---

## Corrections summary — Part 3

| Ref | Target | Verdict | Raised by | Re-verified |
|---|---|---|---|---|
| `COR-14` | new | `VERIFIED FACT` — missing rate converts at 1:1, silently | Expert 3 | yes |
| `COR-15` | `EV-022` | `CONFIRMED AND EXTENDED` — freeze bypassed at 7 production sites | Expert 4 | yes |
| `COR-16` | `EV-007` | `CONTRADICTED` both ways — more privileged actor, wider blast radius | Expert 4 | yes |
| `COR-17` | `EV-015` | `CONFIRMED WITH CAVEAT` — tax lock rejects, producing a third outcome | Expert 3 | yes |
| `COR-18` | `EV-020` | `CONFIRMED WITH CAVEAT` — threshold is an identifier, not a count | Expert 4 | yes |
| `COR-19` | `EV-011` | `CONFIRMED WITH CAVEAT` — one-way ratchets, provisioning-time risk | Expert 4 | yes |
| `COR-20` | new | implementation `VERIFIED FACT`; statutory consequence `HOLD` | Expert 3 | yes |

**Total corrections accepted across all three parts: 20.** Of these, **six contradicted a
research-team claim** (`COR-01`, `COR-02` in part, `COR-04`, `COR-10`, `COR-16`, and `COR-18` in
part), and **four are new findings more severe than anything in the original evidence base**
(`COR-07` entry balance switchable, `COR-11` hash precision collision, `COR-14` silent 1:1 rate,
`COR-08` merge bypasses ORM guards).
