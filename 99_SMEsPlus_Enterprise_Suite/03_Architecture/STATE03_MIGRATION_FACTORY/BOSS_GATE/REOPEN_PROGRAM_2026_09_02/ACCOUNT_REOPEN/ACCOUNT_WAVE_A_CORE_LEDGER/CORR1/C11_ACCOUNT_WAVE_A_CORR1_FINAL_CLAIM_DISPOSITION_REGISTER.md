# C11 — ACCOUNT_WAVE_A_CORR1_FINAL_CLAIM_DISPOSITION_REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · final disposition of every fresh L12 claim

**Method.** No reviewer claim was accepted on the reviewer's authority. Each was re-read against
primary source by the research team, or explicitly marked as not re-read.

Classification: `VERIFIED` · `PARTIALLY VERIFIED` · `CONTRADICTED` · `NOT PROVEN` · `UNKNOWN`.

---

## Part 1 — Fresh Reviewer A (FX and date forensics)

| # | Claim | Disposition | Research-team basis |
|---|---|---|---|
| `A-01` | `T5` — recognition date **has** a carrier (deferral dates on the item; asset depreciation start) | **`VERIFIED`** | Field declarations and the deferred-entry generator read directly |
| `A-02` | `T5` — a **derived** tax point exists via cash-basis exigibility, and `C07` contradicts itself between §1 and §3 | **`VERIFIED`** | The internal contradiction is real; the derived tax point is the reconciliation's maximum matched date |
| `A-03` | `T6` — four counterexamples to "never the document date / regardless of lock" | **`VERIFIED`** on all four | `_compute_date` gates on `is_invoice()`; non-resetting numbering returns the document date; `max(doc, today)` returns the document date when dated today or later; the posting call is inside `if lock_dates:` |
| `A-04` | `T2` — a live-rate module is auto-installed and does create rate rows | **`PARTIALLY VERIFIED`** | Accepted as reported; the research team did not re-read the module. Conclusion survives because the default is manual with no scheduled run |
| `A-05` | `IF-03` — the claimed detection signal does not exist for invoices and bills | **`VERIFIED`** | `_compute_currency_rate:663-664` returns the **stored** `invoice_currency_rate` for invoices; stored par and displayed par stay consistent forever |
| `A-06` | `IF-01` — a revaluation posting mechanism exists in the reporting module | **`VERIFIED`** | `multicurrency_revaluation.py:169-178` creates, posts and reverses a move |
| `A-07` | `IF-01` — that mechanism is contaminated by the same par fallback | **`NOT PROVEN`** | `NOT YET SEARCHED` by the research team. Recorded as `FX-07`, open |
| `A-08` | `IF-02` — `FXU-04` closable: rates written at branch level are invisible to a root-scoped resolver | **`PARTIALLY VERIFIED`** | Resolver side independently confirmed (`_get_rates:128-131` filters on `company.root_id`). Writer side `NOT YET SEARCHED`. Recorded as `FX-08` — highest-value remaining check |
| `A-09` | `IF-04` — five par fallbacks, not two | **`PARTIALLY VERIFIED`** | Two confirmed; three `NOT YET SEARCHED` |
| `A-10` | `IF-04` — the rate field is not `required`, so an empty-valued row also triggers par | **`VERIFIED`** | Field declaration carries no `required`; the Python `or` chains treat empty as falsy. **Trigger condition widened** |
| `A-11` | `T1`, `T3`, `T4`, `T7` confirmed | **`VERIFIED`** | Consistent with the research team's own reads |
| `A-12` | The Thai VAT extract selects on and prints the accounting date under an invoice-date heading | **`VERIFIED`** as ledger mechanics | Statutory consequence remains `HOLD` → `WAVE-D TAX` |

**Reviewer A issued no veto.** Position: corrected and rescoped, core recommendations survive.

---

## Part 2 — Fresh Reviewer B (negatives, close, SaaS, migration, balanced-but-wrong)

| # | Claim | Disposition | Research-team basis |
|---|---|---|---|
| `B-01` | `N9` — a **third unconditional immutability** exists (audit-trail ratchet) | **`CONTRADICTED`** | *Boss-flagged for verification.* `company.py:317-322` refuses to **disable** the flag while any move exists — the mechanism is real. But the flag **defaults off** and may be **enabled at any time**; the constraint blocks only the false direction. A company that never enabled it has **no** deletion protection, which is the default outcome. This is the one-way ratchet already recorded as `COR-19`, **not** a third unconditional immutability. `N9` stands as written |
| `B-02` | `N1` — provenance/idempotency carriers exist, including a **database UNIQUE constraint** | **`PARTIALLY VERIFIED`** | *Boss-flagged for verification.* The constraint is real — `account_bank_statement_import/models/account_bank_statement.py:17-19`, `unique (unique_import_id)`. **Three material qualifications:** the module is `auto_install: False`; the constraint is **table-global with no company or tenant scoping**; and the importer's own dedup is a Python search (`account_journal.py:262-264`), not the constraint. `N1` is **re-scoped, not withdrawn**: no general, mandatory carrier exists in `addons/account` |
| `B-03` | `N2` — three duplicate controls exist; only bank import blocks | **`VERIFIED`** | Independently found by the research team before the fresh round and already recorded as `NC-13` |
| `B-04` | `N8` — an unrealised-FX revaluation wizard exists | **`VERIFIED`** | Same finding as `A-06`; recorded as `NC-19` |
| `B-05` | `N10` — a generic approval engine exists and special-cases the entry model, skipped under privilege elevation | **`NOT PROVEN`** | `NOT YET SEARCHED` by the research team. If correct, it is a weak control and **raises `GAP-C04`'s priority** — which `C09` closes independently |
| `B-06` | `N3` second half — the outermost boundary is the **database**, not the company group | **`PARTIALLY VERIFIED`** | Supported by two facts the research team holds independently: the numbering parameter has no company dimension (`COR-16`), and rate rows may carry a null company which the resolver accepts. The reporting-definition claim is `NOT YET SEARCHED`. Direction accepted; `SB-05`/`SB-06` recorded open |
| `B-07` | `N7` — control-account **function** exists; and the package contradicts itself across files 02, 18 and 21 | **`PARTIALLY VERIFIED`** | The internal inconsistency is real and accepted. The substantive position — no distinct control-account **entity** — is unchanged, and file 02 already said so |
| `B-08` | `N6` — "not detected" overstated; tax fields and due date **are** field-tracked | **`VERIFIED`** | `CONTRA-01b` re-scoped: the evidence-free set narrows to `amount_currency`, `currency_id`, `analytic_distribution` and the reconciliation fields. Still severe |
| `B-09` | `N11` — reopening does leave tracked changes and lock-exception records | **`VERIFIED`** | Governance conclusion unchanged: no distinct reopening authority, no close artefact |
| `B-10` | Balanced-but-wrong: duplicate vendor bill **across a year boundary** escapes the detector | **`PARTIALLY VERIFIED`** | Plausible and consistent with the detector's construction; the year-scoping was `NOT YET SEARCHED`. Added to the `BALANCED BUT WRONG` register as a qualification of `BW-06` |
| `B-11` | Balanced-but-wrong: duplicate **manual journal entry** — the detector never runs on `entry`-type moves | **`VERIFIED`** | The detector filters to sale and purchase documents. Already the substance of `NC-13`'s residual gap; now stated as a concrete case |
| `B-12` | Balanced-but-wrong: same bank transaction via two ingestion routes with disjoint keys | **`NOT PROVEN`** | Consistent with `B-02`'s finding that the constraint is confined to one optional module, but the second route was `NOT YET SEARCHED` |
| `B-13` | Balanced-but-wrong: a **null-company rate re-measures another tenant** | **`PARTIALLY VERIFIED`** | The resolver accepts `company_id IS NULL` rows (`:129`) — confirmed. Whether such rows arise in practice is `NOT YET SEARCHED`. **If they do, this is a cross-tenant data-integrity failure and is the most serious SaaS finding in the programme.** Recorded as `SB-05`, open |
| `B-14` | Migration boundary anchored to a mutable, unlinked opening date | **`NOT PROVEN`** | `NOT YET SEARCHED`; consistent with `EV-017` |
| `B-15` | A tax-period close **already is** a record — a period-bound posted entry that advances the tax lock | **`VERIFIED`** | Consistent with the research team's own reading. **This is a constructive finding**: it gives Boss decision `CL-01` a working reference pattern from within the same system |

**Reviewer B issued one veto**, on the package's internal inconsistency about control accounts
(`B-07`). Disposition: **accepted as an inconsistency, rejected as a substantive contradiction.** The
position was stated correctly in file 02 and incorrectly in file 18; file 18 is corrected.

---

## Part 3 — Counts

| Disposition | Reviewer A | Reviewer B | Total |
|---|---|---|---|
| `VERIFIED` | 7 | 6 | **13** |
| `PARTIALLY VERIFIED` | 4 | 5 | **9** |
| `CONTRADICTED` | 0 | 1 | **1** |
| `NOT PROVEN` | 1 | 3 | **4** |
| `UNKNOWN` | 0 | 0 | 0 |
| **Total claims** | **12** | **15** | **27** |

**Twenty-two of twenty-seven reviewer claims survived verification** in whole or material part. One
was contradicted (`B-01`, the audit-trail ratchet conclusion — the mechanism is real, the inference
from it was not). Four could not be verified within this session and are recorded as open, not as
accepted.

---

## Part 4 — Effect on the two Boss-flagged claims

Instruction 6 required that the audit-trail ratchet and the import idempotency key be preserved as
**failed verification unless new evidence proves them**. New evidence was sought and found for both:

| Claim | First attempt | New evidence | Final disposition |
|---|---|---|---|
| **Audit-trail ratchet** | verification interrupted; unproven | `company.py:317-322` read in full | **`CONTRADICTED` as a third unconditional immutability.** The mechanism exists but is a one-way ratchet that, by default, locks the protection **off** at first posting. It does not narrow `SB-04` or `CONTRA-14`; it **worsens** them, because most tenants will have the protection permanently unavailable without ever choosing that |
| **Import idempotency key** | not found in `addons/account`; statement line had no constraints | wider search located the declaration and constraint in the optional import module | **`PARTIALLY VERIFIED`.** A real database constraint exists, but only with an optional module installed, and it is table-global rather than tenant-scoped. `N1` re-scoped, not withdrawn |

Neither claim is accepted in the form the reviewer offered it. Both changed the package — the first
by making a finding worse, the second by narrowing one.
