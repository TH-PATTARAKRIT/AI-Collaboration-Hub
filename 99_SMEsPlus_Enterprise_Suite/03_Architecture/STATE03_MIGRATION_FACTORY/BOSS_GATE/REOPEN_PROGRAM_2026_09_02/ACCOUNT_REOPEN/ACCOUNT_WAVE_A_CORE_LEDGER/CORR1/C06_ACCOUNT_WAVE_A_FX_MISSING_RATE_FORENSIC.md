# C06 — ACCOUNT_WAVE_A_FX_MISSING_RATE_FORENSIC

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Layer 2 / audit quarantine — carries source citations.

> Re-opens `COR-14` / `CONTRA-08` from the parent package. The parent stated the finding correctly
> but at **insufficient precision**: it said "a missing rate converts at 1:1". This forensic
> establishes the exact operation, condition, scope and reachability, and **materially escalates the
> finding** — the 1:1 path is reached in the **shipped initial state of every currency**, not in an
> exceptional configuration.

---

## 1. The exact mechanism

**`VERIFIED FACT`** — `base/models/res_currency.py:121-141`, method `_get_rates(company, date)`.

Rate resolution is a single SQL expression with a **three-branch** fallback:

| Branch | Query | Reached when |
|---|---|---|
| 1 | latest rate row with `name <= date`, for `company_id IN (NULL, company.root_id)`, ordered `company_id, name DESC`, limit 1 | at least one rate exists dated on or before the requested date |
| 2 | **earliest rate row ever** for that currency in the same company scope, ordered `company_id, name ASC`, limit 1 | rates exist, but **all are dated after** the requested date |
| 3 | **the literal `1.0`**, supplied by `COALESCE(..., ..., 1.0)` | **no rate row exists at all** for that currency in that company scope |

**A second, independent 1.0 appears in Python** — `base/models/res_currency.py:156`:
`currency.rate = (currency_rates.get(currency.id) or 1.0) / currency_rates.get(to_currency.id)`.

### Correction to the parent's framing

The parent package implied that any absent rate yields 1:1. That is **too wide**. Branch 2 means a
transaction dated *before* the first rate ever entered uses that first rate — **not** 1.0. The 1.0
branch requires **zero rate rows** for the currency in the `(NULL, company root)` scope.

This narrowing does **not** reduce the finding. It relocates it, as §3 shows.

---

## 2. Where the conversion is invoked

| Operation | Entry point | Date used | Result stored? |
|---|---|---|---|
| Invoice or bill, document-level rate | `account_move.py:1052-1063` `_compute_invoice_currency_rate` | `invoice_date` or today (`:1047-1049`) | **YES — `invoice_currency_rate` is `store=True`, `digits=0`** (`:475-481`) |
| Journal item rate, invoice context | `account_move_line.py:661-664` | inherited from the document rate above | no — the field is non-stored |
| Journal item rate, non-invoice context | `account_move_line.py:665-670` | `invoice_date` or `date` or today | no |
| Item foreign amount from balance | `account_move_line.py:686-691` `_compute_amount_currency` | via `currency_rate` above | **YES — `amount_currency` is stored** |
| Generic conversion | `base/models/res_currency.py:273-291` `_convert` | caller-supplied | caller-dependent |

**`VERIFIED FACT`** — `_convert` asserts only that the currencies exist
(`"convert amount from unknown currency"`, `:284-285`). **There is no assertion, check, warning or
log concerning the availability of a rate.**

### The persistence consequence

The **rate** on the item is not stored, but the **amounts it produced are**. So a par conversion is
frozen into `balance` and `amount_currency` permanently, while the displayed rate is recomputed on
every read. Once real rates are later entered, an affected item will display a rate that is
**arithmetically inconsistent with its own stored amounts**. This is the only detection signal found
— see §6.

---

## 3. Reachability — the escalation

The decisive question the parent did not ask: *can a currency actually have zero rate rows in a
production system?*

**`VERIFIED FACT`** — the shipped currency master data file
`base/data/res_currency_data.xml` contains **zero** `res.currency.rate` records
(mechanical count: 0). Currencies ship defined and **inactive**, carrying name, ISO number, symbol,
rounding and labels only. The Thai baht entry at `:1480-1489` is representative: no rate.

**`VERIFIED FACT`** — the only file in the framework's base data directory that contains rate records
is `base/data/res_currency_rate_demo.xml`, i.e. **demonstration data**, which a production
installation does not load.

### Therefore

> **Zero rates is the shipped, default, production state of every currency in the system.**

The 1.0 branch is not an exceptional configuration, not a corrupted database, and not a test
artifact. It is what happens on the **first foreign-currency transaction** in any newly activated
currency, in the window between activating that currency and entering its first rate.

**Required classification, per the Boss question:** the 1:1 result is a **hard-coded fallback
constant in the resolution query**, and it is **reachable from the product's own initial state**.

---

## 4. Precise scope statement

Stated under rule `DR-NC-02` with its search boundary attached.

**Condition, fully specified.** A conversion between a company currency and a transaction currency
converts at 1:1 when **all** of the following hold:

1. the two currencies differ;
2. the transaction currency has **no** `res.currency.rate` row whose `company_id` is either NULL or
   the acting company's **root** company — note this is the *root*, so a rate held against a
   subsidiary is not seen;
3. the conversion is invoked through `_get_rates`, which is the path used by
   `_get_conversion_rate`, `_convert`, `_compute_invoice_currency_rate` and
   `_compute_currency_rate`.

**Does it warn?** `NOT FOUND IN SEARCHED SCOPE.` A mechanical search for missing-rate warning text
across `addons/account/models/` and `addons/account/wizard/` returned no match. Absence of a warning
in other modules, in the web client, or in the enterprise reporting layer is **not** established.

**Does it block?** `VERIFIED ABSENCE within the resolution path.` The `COALESCE` returns a value
unconditionally; there is no branch in `_get_rates`, `_get_conversion_rate` or `_convert` that can
raise or refuse. Blocking behaviour in a *calling* module is not established — `NOT YET SEARCHED`.

---

## 5. Does the ledger remain balanced?

**`VERIFIED FACT` — yes, and this is the core of the danger.**

Every item on one entry resolves its rate through the same call, on the same date, for the same
company. All items therefore share the same erroneous factor. `balance = amount_currency × 1.0` on
every line, so:

- **debits equal credits** — the entry balances;
- the database sign check between `balance` and `amount_currency` is satisfied
  (`account_move_line.py:436-448`);
- the entry posts, numbers, hashes and reconciles normally;
- the trial balance foots.

**Every control in the Wave A control matrix is satisfied by an entry whose economic valuation is
wrong.** This is the canonical "balanced but wrong" case, and it is carried into the Level 11 re-run
as `BW-01`.

---

## 6. Detectability

| Signal | Available? | Note |
|---|---|---|
| Error or warning at entry | **no** | none found in the searched scope |
| Rate visibly equal to 1 on the document | **partially** | the stored document rate is 1.0 and is displayed; it requires a human to notice that a foreign currency is quoting at par |
| Integrity hash | **no** | the transaction-currency amount and currency are outside hash coverage (`CONTRA-01b`), and company-currency amounts are serialised at the foreign currency's precision (`CONTRA-06`) |
| Trial balance | **no** | it foots |
| Later inconsistency | **yes — the only reliable signal** | once real rates exist, the non-stored displayed rate on the affected item no longer agrees with its stored `balance` and `amount_currency` |
| Reconciliation | **partially** | settling the item at a real rate produces an exchange difference approximately equal to the entire foreign-currency value, which is anomalous and may be noticed |

**`INFERENCE`:** detection is retrospective, indirect, and depends on someone reconciling a displayed
rate against stored amounts. There is no forward control.

---

## 7. Impact by domain

| Domain | Impact | Class |
|---|---|---|
| **Onboarding** | **Highest.** A new tenant activates its currencies and transacts. Every foreign-currency document raised before the first rate is entered is valued at par. | `VERIFIED FACT` as to mechanism; severity is `INFERENCE` |
| **Migration** | **Highest.** Opening balances carry foreign-currency open items. If loaded before rates, every opening valuation is at par, and it is then **locked** into the opening entry, which `MG-13` recommends hard-locking. | `INFERENCE` from `EV-017` + this forensic |
| **AR / AP** | Open items carry a par residual. Ageing and exposure reporting are wrong by the full rate factor. | `INFERENCE` |
| **Payment** | Settlement at a real rate generates an exchange difference of roughly the entire foreign value, misclassifying a valuation error as an FX gain or loss. | `INFERENCE` |
| **FX realisation** | Corrupted as above — the difference is not a real economic gain. | `INFERENCE` |
| **FX revaluation** | No posting mechanism was found in the searched scope (`GAP-H01`), so no compensating restatement exists. | `NOT FOUND IN SEARCHED SCOPE` |
| **Financial statements** | Assets, liabilities, revenue and expense are misstated by the rate factor for affected transactions; the statements still balance. | `INFERENCE` |

---

## 8. Classification and decision

| Question | Answer |
|---|---|
| **Reference behaviour** | A hard-coded `1.0` in the rate-resolution query, reached whenever a currency has no rate rows in the company-root scope — which is the shipped default state of every currency. |
| **Is 1:1 a fallback, default, inferred behaviour, or test artifact?** | **A fallback constant, reachable from the product's own initial state.** Not inferred, not a test artifact. |
| **SMEsPlus control requirement** | A posting whose valuation depends on an unavailable measurement **must not be created**. The absence of a rate is a missing fact, and a missing fact is not a licence to invent one. |
| **Decision** | **`REJECT`** — without qualification. |

### The explicit challenge the Boss required

> *Should SMEsPlus permit posting when a required currency rate is absent?*

**`RECOMMENDATION` — No, and the reasoning is not primarily about accuracy.**

A ledger's value is that a posted fact is a claim the business can defend. `1.0` is not a missing
value; it is an **assertion that one unit of foreign currency equals one unit of company currency** —
a statement the business never made and would never make. The system fabricates a measurement and
then presents it as indistinguishable from a real one.

Three positions were considered and two rejected:

| Option | Assessment |
|---|---|
| Permit, warn, correct later | **Rejected.** The amounts are stored at posting; a later rate does not restate them. The warning is also the thing most likely to be dismissed during onboarding, which is exactly when this occurs. |
| Permit, mark the posting as provisionally valued | **Rejected for Wave A.** It creates a second class of posted fact and a restatement obligation, which contradicts `ST-12` (immutability is unconditional). It may merit reconsideration if Boss decides valuation and recognition should be separable — but that is a larger architectural question. |
| **Refuse the posting** | **Recommended.** Consistent with `ST-17` (invariants enforced at storage level) and with `IC-14`. The business impact is a blocked posting with a clear cause, which is recoverable in seconds by entering a rate. |

**Proposed as `Tolerance = 0` candidate `T0-02`** under constitution principle 13. This session
**proposes**; only Boss may designate.

---

## 9. Residual unknowns

| # | Unknown | Classification |
|---|---|---|
| `FXU-01` | Whether any calling module blocks or warns before reaching `_get_rates` | `NOT YET SEARCHED` — scope searched was the account module's models and wizards only |
| `FXU-02` | Whether the web client surfaces a par rate distinctly | `NOT YET SEARCHED` |
| `FXU-03` | Whether an automated rate feed, where configured, guarantees a rate exists before first use | `NOT YET SEARCHED` — feed modules were out of Wave A scope |
| `FXU-04` | Whether a rate held against a **subsidiary** rather than the root company is genuinely invisible to conversion, as the query's `company.root_id` restriction implies | `UNKNOWN` — the query text supports it; no runtime confirmation |
| `FXU-05` | Thai statutory consequence of a par-valued posting and of its later correction | `HOLD / EVIDENCE REQUIRED` → `WAVE-D TAX` |

`FXU-04` is material and cheap to close; it is recommended as the first follow-up.

---

# ADDENDUM A1 — CORRECTIONS FROM FRESH L12 REVIEW

Raised by Fresh Reviewer A. **Each re-verified against primary source by the research team.**
The body above is retained unedited; where it conflicts with this addendum, **the addendum governs**.

## A1-01 — §6 detection claim is WRONG for the documents this forensic rates highest-impact

**Reviewer claim:** the "later inconsistency" signal does not exist for invoices and bills.
**Verification: `VERIFIED`.**

`account_move_line.py:661-664` — `_compute_currency_rate` branches first on
`move_id.is_invoice(include_receipts=True)` and, for those documents, returns
**`move_id.invoice_currency_rate`** — the value stored at `account_move.py:475-481`
(`store=True`). It does **not** re-resolve a rate.

**Consequence.** For an invoice or bill posted with no rate available, the stored document rate is
`1.0` and the displayed line rate reads that same stored `1.0`. The two remain mutually consistent
indefinitely, whatever rates are entered later. **No divergence ever appears.**

The §6 table row "Later inconsistency — **the only reliable signal**" is therefore **withdrawn for
invoices and bills**. It survives only for non-invoice entries, whose rate is re-resolved live at
`:665-670`.

**Corrected detectability for `SF-01`: there is no detection signal at all for customer invoices and
vendor bills** — precisely the population §7 identifies as the onboarding and migration exposure.
`SF-01` severity is **raised again**; see `C11`.

## A1-02 — §7 "no unrealised-FX posting mechanism" is CONTRADICTED

**Verification: `VERIFIED` — the mechanism exists.**

`account_reports/wizard/multicurrency_revaluation.py:169-178` — `create_entries` builds an
`account.move`, posts it, and creates a dated reversal. A full post-and-reverse revaluation mechanism
therefore exists, in the **reporting** module.

This is the **fifth** over-scoped negative of the programme and the **second committed by CORR1
itself**: the forensic searched `addons/account` and reported the absence at domain scope.

**Compounding finding — `VERIFIED`.** The reviewer further reports that the revaluation report
resolves rates through the same `_get_rates` path and guards only against a zero rate. If so, the
compensating control inherits the par fallback. Recorded as `FX-07`; the guard's exact form is
`NOT YET SEARCHED` by the research team.

**Corrected wording.** Replace "no carrier found" with: *"A post-and-reverse unrealised-FX
revaluation mechanism exists in `addons/account_reports`. No such mechanism was found in
`addons/account`. Whether it is contaminated by the par fallback is `FX-07`, open."*

## A1-03 — `FXU-03` premise was wrong; §3 conclusion survives on a different basis

**Verification: `PARTIALLY VERIFIED`.** A live-rate module is auto-installed alongside the accounting
module and does create rate rows, so the forensic's assumption that no shipped mechanism creates
rates was incorrect. The reviewer reports its update interval defaults to manual with no scheduled
next run, so the **shipped state still yields zero rate rows** until a human acts.

**Corrected §3 claim, at supported scope:** *"Shipped master data contains no rate rows. A live-rate
mechanism is installed by default but is configured to manual with no scheduled execution, so a
newly activated currency still has zero rates until a rate is fetched or entered."* The
reachability conclusion is unchanged; its basis is narrower and must be stated as above.

## A1-04 — The par fallback has more entry points than §1 records

**Verification: `PARTIALLY VERIFIED — count not confirmed.`** The research team confirmed two
fallbacks (`res_currency.py:140` SQL `COALESCE`, `:157` Python `or 1.0`). The reviewer reports five,
at `:140, :157, :407, :411, :419`. The three additional sites were **not** re-read by the research
team: `NOT YET SEARCHED`.

**Materially, and independently important — `VERIFIED` by inspection of the field declaration:**
`res.currency.rate.rate` is declared as a plain stored float **without `required=True`**
(`base/models/res_currency.py:344-349`). A rate **row** that exists with an empty value therefore
defeats the §4 narrowing, because the Python `or` chains treat it as falsy and substitute `1.0`.
**The condition in §4 must be widened** from "no rate row exists" to *"no rate row with a non-empty
value exists"*.

## A1-05 — `FXU-04` is closable, and the answer is worse than the forensic stated

**Reviewer claim:** rates written by a subsidiary carry that company's identifier while the resolver
reads the **root** company, so branch-level rate maintenance is invisible to conversion.
**Verification: `PARTIALLY VERIFIED`.** The research team independently confirmed the resolver side —
`_get_rates` filters `company_id IN (NULL, company.root_id)` (`:128-131`), which is the forensic's
own §4 condition 2. The writer side (`update_currency_rates_manually`) was **not** re-read:
`NOT YET SEARCHED`.

If the writer side is as reported, the consequence is severe and is the worst variant of this
finding: **a tenant that maintains rates on a branch company believes rates are loaded while
conversion silently uses par.** Recorded as `FX-08`, and it is the single highest-value remaining
verification in this forensic.

## Addendum summary

| # | Effect on the forensic | Verification |
|---|---|---|
| `A1-01` | Detection claim withdrawn for invoices and bills — **`SF-01` severity raised** | `VERIFIED` |
| `A1-02` | "No revaluation mechanism" contradicted — **second CORR1 over-scoped negative** | `VERIFIED` |
| `A1-03` | `FXU-03` premise corrected; conclusion survives on narrower basis | `PARTIALLY VERIFIED` |
| `A1-04` | Trigger condition widened to "no rate row **with a non-empty value**" | `PARTIALLY VERIFIED` |
| `A1-05` | `FXU-04` likely closable and severe | `PARTIALLY VERIFIED` |

**The forensic's decision is unchanged and strengthened: `REJECT`.** Every correction above either
widens the trigger condition, removes a detection signal, or contaminates a compensating control.
None narrows the finding.
