# C04 — ACCOUNT_WAVE_A_NEGATIVE_CLAIM_SCOPE_REGISTER

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · governed by `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD`

Classification: `A` VERIFIED ABSENCE (within stated scope) · `B` NOT FOUND IN SEARCHED SCOPE ·
`C` NOT YET SEARCHED · `D` UNKNOWN · `E` CONTRADICTED. **B/C/D are never converted to A.**

A mechanical scan of the parent package found **38 absolute negative phrasings across 15 files**.
This register rescopes the material ones. The three the Boss round identified are worked in full in
Part 1; Part 2 rescopes the remaining material negatives; **Part 3 records a fourth over-scoped
negative found by this session itself**, which the earlier review round did not catch.

---

## PART 1 — THE THREE OVER-SCOPED NEGATIVES

### `NC-01` — Fiscal year

| Field | Value |
|---|---|
| **Claim ID** | `NC-01` (parent `EV-016`, first half) |
| **Original claim** | "A search for a fiscal-year model definition across the entire 797-module reference tree returns **no result**." |
| **Original search boundary** | A single grep for the token `account.fiscalyear` (no separator between "fiscal" and "year"), over the addons root |
| **Evidence actually examined** | That one pattern's empty result set |
| **Scope originally asserted** | The entire 797-module tree — i.e. the whole system |
| **Scope supported by evidence** | Only: "no model whose name is spelled `account.fiscalyear` was found" |
| **Corrected claim** | A fiscal-year model **exists** — `account_accountant/models/account_fiscal_year.py:11-55` — carrying a name, start and end dates and an owning company, constrained to non-overlapping ranges and refused on child companies. It is reached via a dedicated group and a settings toggle, is fully mutable and deletable by the accounting-manager group, and is consumed **only** for deriving year boundaries and for fiscal-year grouping of currency rates. It has **no state, no close action, no posting, no balance and no link from any entry** |
| **Confidence** | High — re-verified against primary source by the research team |
| **Required additional search** | None for the entity itself. Whether any localization or third-party module attaches behaviour to it: **class C** |
| **Final classification** | **`E — CONTRADICTED`** |
| **Root cause** | Naming-variant miss. The standard's `DR-NC-06` §6.4 (naming risk) exists because of this case |
| **Does the dependent conclusion survive?** | **Yes, and it is strengthened.** The load-bearing claim was never the entity's absence — it was that *no year-end closing entry exists and the year result is computed at report time*. That stands (see `NC-04`). The reference system has a fiscal-year object and still attaches no closing, locking or state to it — which is a **stronger** statement of the same architectural position |

### `NC-02` — Rate types

| Field | Value |
|---|---|
| **Claim ID** | `NC-02` (parent `EV-018`) |
| **Original claim** | "There is **no rate type dimension** — no separate spot, average, closing or historical rate." |
| **Original search boundary** | `base/models/res_currency.py` (the framework rate model) and the account module's rate *extension* — but **not** the account module's currency-table builder |
| **Evidence actually examined** | The stored `res.currency.rate` model: its fields and its unique constraint |
| **Scope originally asserted** | The system |
| **Scope supported by evidence** | Only the **storage** layer: "the stored rate model carries no rate-type column" |
| **Corrected claim** | Four rate types — `current`, `closing`, `historical`, `average` — **are** implemented, as a query-time derivation. `account/models/res_currency.py:105-160` builds a temporary currency table with an explicit `rate_type` column, populated by four dedicated builders and selected by a cumulative-translation-adjustment flag. **Storage** holds one scalar per currency per day per company root; **valuation bases are derived from it** |
| **Confidence** | High — re-verified |
| **Required additional search** | Whether any localization overrides the derivation: **class C** |
| **Final classification** | **`E — CONTRADICTED`** |
| **Root cause** | Partial read of a module the evidence base had listed as verified; the conclusion was drawn at system scope from one file |
| **Downstream effect** | Materially positive. Coverage rows `H-13` and `H-15` move from `NC` to `PC`. `GAP-H01` is re-scoped: **no posting mechanism for unrealised FX was found; a valuation mechanism exists**. And the corrected evidence produced the *better* design position now recorded as `ST-05` — measurement stored once, valuation bases derived |

### `NC-03` — Thai localization source availability

| Field | Value |
|---|---|
| **Claim ID** | `NC-03` (parent `EV-000` source registry) |
| **Original claim** | Not stated as a negative, but the source registry omitted Thai localization, leaving the impression that no such source was examined or available |
| **Original search boundary** | The account, advanced-accounting, reporting and framework modules only |
| **Evidence actually examined** | Those modules |
| **Scope originally asserted** | Implicitly, the available evidence base |
| **Scope supported by evidence** | Only the modules listed in the registry |
| **Corrected claim** | Two Thai localization modules — `l10n_th` and `l10n_th_reports` — are **present in the same verified build** and are readable |
| **Confidence** | High — directory listing confirmed |
| **Required additional search** | The modules' content is **class C — NOT YET SEARCHED** by this session's research team. Expert 3 examined them; those findings are recorded in that review and are routed, not adopted |
| **Final classification** | **`E — CONTRADICTED`** (as an availability claim) |
| **Effect on statutory positions** | **None. All seven Thai statutory items remain `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track.** Reading a localization module establishes what an implementation does; it does not establish what Thai law requires. Those are different claims and this session may make only the first. Thai names remain candidate / UNVALIDATED |

---

## PART 2 — RESCOPING THE REMAINING MATERIAL NEGATIVES

Each row restates a parent-package negative at its supported scope.

| # | Claim as written in the parent | Scope actually searched | Class | Corrected wording |
|---|---|---|---|---|
| `NC-04` | "No year-end closing entry exists **anywhere in the tree**" | grep for closing-entry constructs across `account/` and `account_reports/`; the only match was the **tax** closing entry | **B** | "No year-end result-transfer entry was found within `addons/account` and `addons/account_reports`. The only closing entry found is a tax-return posting. Localization and third-party modules were not searched." |
| `NC-05` | "**No** accounting-event identity and **no** provenance carrier exist **anywhere in the domain**" | `addons/account/models` and `addons/account/wizard` | **B, and partly `E` — see `NC-13`** | "No general accounting-event identity or provenance carrier was found in `addons/account/models` and `/wizard`. **Typed origin links do exist** for specific generated entries (payment origin, recurring-entry origin, cash-basis origin, statement-line link) and a free-text origin field exists. What was not found is a *general, mandatory* identity applicable to every accounting event." |
| `NC-06` | "**No tenant concept exists**" | `account/`, `account_accountant/`, the company model | **A within that scope** | "No tenant entity is present in `addons/account`, `addons/account_accountant`, or the company model. The outermost boundary implemented there is the company group. Deployment- and hosting-layer tenancy was not searched." |
| `NC-07` | "There is **no period object**" | `account/`, `account_accountant/`, `account_reports/` | **E in part — see `NC-01`** | "A fiscal-year *calendar* record exists (`NC-01`). No period object carrying **state, a close action, a closer, a basis or a link from any entry** was found in the searched modules." |
| `NC-08` | "**No temporal validity** model exists on any entity" | field declarations on account, journal, entry, item, company in `addons/account` | **A within that scope** | "No effective-dating or version fields were found on those five models in `addons/account`. Other modules and the framework's own auditing were not searched for this purpose." |
| `NC-09` | "**No** posting mechanism for unrealised FX / revaluation" | `addons/account/models` and `/wizard` | **B** | "No unrealised-FX posting mechanism was found in `addons/account`. A **valuation** mechanism exists (`NC-02`). `addons/account_accountant` was not exhaustively searched for a revaluation wizard — **class C**." |
| `NC-10` | "**No** matching history artefact exists" | reconciliation models in `addons/account/models` | **B** | "No dedicated matching-history model was found among the reconciliation models in `addons/account/models`. Framework-level record auditing was not assessed as a substitute." |
| `NC-11` | "**No explicit control-account concept** exists" | `addons/account/models` | **B** | "No distinct control-account entity was found in `addons/account/models`; the equivalent function is served by account **type**. The reporting layer's subledger handling was not searched." |
| `NC-12` | "Accounts have **no** archive state" | field declarations on the account model, including inherited mixins | **A within that scope** | Unchanged in substance — independently confirmed by the earlier challenge unit. Scope now stated explicitly |
| `NC-14` | "**Exactly two** things are unconditionally immutable" | the invariants enumerated in the parent's own control matrix | **D** | "Within the fourteen invariants this package enumerated, two were found unconditional. The enumeration is the package's own and is not proven exhaustive." |
| `NC-15` | "**No maker-checker / approval-before-posting** step exists" | posting permissions and `_post` in `addons/account` | **B** | "No approval step distinct from the posting permission was found in `addons/account`. Approval modules outside the accounting module were not searched — **class C**." |
| `NC-16` | "Merge is **irreversible**; **no** correction exists" | the merge wizard | **A within that scope** | "The merge wizard implements no inverse operation and writes no record. Recovery from a database backup is outside the application scope and is not addressed." |
| `NC-17` | "**Nothing** bounds a reconciliation against the item it reconciles" | constraint declarations on the reconciliation models | **A within that scope** | "The partial-reconciliation model declares zero database constraints. Application-level bounds elsewhere in the reconciliation path were not exhaustively traced — **class C**." |
| `NC-18` | "**No** carrier for migration provenance" | the opening-entry mechanism in `addons/account` | **B** | "No provenance carrier was found on the opening-entry mechanism in `addons/account`. Dedicated import or migration tooling was not searched — **class C**." |

---

## PART 3 — A FOURTH OVER-SCOPED NEGATIVE, FOUND BY THIS SESSION

Recorded under `DR-NC-06`. The earlier review round did not catch this one; this session found it
while executing the round.

### `NC-13` — "No controls prevent duplicate accounting events"

| Field | Value |
|---|---|
| **Claim ID** | `NC-13` (parent Final Gate Report, answer to Boss question 20, and `FE-01`) |
| **Original claim** | Boss question 20 — "Which controls prevent duplicate or missing accounting events?" — was answered **"None."** |
| **Original search boundary** | A search for idempotency-key constructs. No search was made for duplicate-*detection* by other means |
| **Evidence actually examined** | The absence of any idempotency mechanism |
| **Scope originally asserted** | All duplicate controls |
| **Scope supported by evidence** | Only: "no idempotency key was found" |
| **Corrected claim** | A duplicate control **does** exist, and was missed. `account_move.py:691` declares a computed `duplicated_ref_ids`; `:1831-1840` computes it via `_fetch_duplicate_reference`, matching sale and purchase documents on the reference field across draft and posted states; `_auto_init` creates a supporting index on `ref` restricted to vendor bills and refunds. Its enforcement effect found at `:5034-5037`: when a potential duplicate is detected, **auto-posting is suppressed and a message is written to the entry's thread**. |
| **What it does NOT cover** | It matches on a **reference string**, not on an event identity; it applies only to **sale and purchase documents**, so machine-generated `entry`-type postings are outside it; and it **warns rather than blocks** — a user may post a flagged duplicate manually |
| **Confidence** | High — re-verified against primary source |
| **Required additional search** | Whether any producing module adds its own duplicate control — **class C** |
| **Final classification** | **`E — CONTRADICTED`** |
| **Corrected answer to Boss question 20** | "A duplicate-**reference** warning exists for sale and purchase documents, matching on the reference field; it suppresses auto-posting and annotates the entry, but does not block manual posting. **No idempotency mechanism keyed on an accounting-event identity was found in `addons/account`**, and the existing control does not extend to machine-generated entries. No completeness control detecting a *missing* posting was found in the same scope." |
| **Does the dependent conclusion survive?** | **Substantially, but weakened.** `XM-01` and `ST-15` argued that the absence of event identity leaves duplicates undetected. That remains true for machine-generated entries, which is the case that matters most for producer integrations. But the blanket "None." was wrong, and the reference model is better defended than the parent credited |

---

## PART 4 — SUMMARY

| Classification | Count | Claims |
|---|---|---|
| **`E — CONTRADICTED`** | **5** | `NC-01`, `NC-02`, `NC-03`, `NC-07` (in part), `NC-13` |
| **`A — VERIFIED ABSENCE` within a stated scope** | 5 | `NC-06`, `NC-08`, `NC-12`, `NC-16`, `NC-17` |
| **`B — NOT FOUND IN SEARCHED SCOPE`** | 7 | `NC-04`, `NC-05`, `NC-09`, `NC-10`, `NC-11`, `NC-15`, `NC-18` |
| **`C — NOT YET SEARCHED`** (named adjacent scopes) | 8 | recorded inline above |
| **`D — UNKNOWN`** | 1 | `NC-14` |

### The pattern

Of five contradicted negatives, **four were naming or scope misses in modules the package had already
declared verified**, and one (`NC-13`) was a failure to search for an alternative mechanism after the
expected one was absent. None was caused by inaccessible evidence.

### Effect on the parent package's conclusions

| Conclusion | Effect |
|---|---|
| No year-end closing entry; result computed at report time | **survives, strengthened** (`NC-01`, `NC-04`) |
| One stored measurement; valuation bases derived | **improved** — this is now a positive finding, not a gap (`NC-02`) |
| Accounting-event identity is absent | **survives at narrowed scope** — typed origin links exist for specific cases (`NC-05`) |
| No duplicate control exists | **corrected — a partial control exists** (`NC-13`) |
| Thai statutory positions | **unchanged — all remain `HOLD`** (`NC-03`) |
| Everything in the `REJECT` list of decisions | **unaffected** — every rejection rests on a *positive* finding of behaviour, not on a negative |

That last row is the material one for the gate: **no `REJECT` decision in the parent package depended
on a negative claim.** The corrections change the picture of what the reference system *lacks*; they
do not change what it was observed to *do*.

---

# PART 5 — NEGATIVES INTRODUCED BY CORR1 ITSELF

Added after the fresh L12 review. **CORR1 committed the same defect class it was convened to fix.**
This is recorded plainly rather than minimised, because the standard requires lineage and because the
recurrence is itself the most important governance finding of the round.

| # | Claim as written in CORR1 | Where | Scope actually searched | Class | Corrected wording | Verification |
|---|---|---|---|---|---|---|
| `NC-19` | "No unrealised-FX **posting** mechanism exists" | `C06` §7, and `GAP-H01` inherited from the parent | `addons/account/models` and `/wizard` | **`E — CONTRADICTED`** | "A post-and-reverse unrealised-FX revaluation mechanism exists in `addons/account_reports` (`wizard/multicurrency_revaluation.py:169-178`). None was found in `addons/account`." | `VERIFIED` — research team read the wizard |
| `NC-20` | "**Recognition date** has no carrier" | `C07` §1 row 3 | `addons/account` field declarations on entry and item | **`E — CONTRADICTED`** | "No **general** recognition-date carrier was found in `addons/account`. Purpose-specific carriers exist: deferral start/end dates on the item in `addons/account_accountant`, and a depreciation start date in the asset module." | `VERIFIED` — research team read the field declarations |
| `NC-21` | "**Tax point** has no carrier" | `C07` §1 row 4 | as above | **`E — CONTRADICTED` in part** | "No **stored** tax-point field was found on the entry or item in `addons/account`. A **derived** tax point exists for cash-basis taxes via the reconciliation's maximum matched date." | `VERIFIED` — and `C07` contradicted itself internally between §1 and §3 |
| `NC-22` | "For non-sale documents the accounting date is **never** the document date" | `C07` §2 consequence B, §5 | `_compute_date` and `_get_accounting_date` | **`E — CONTRADICTED`** | Four counterexamples: the path is gated on `is_invoice()`; non-period-resetting numbering returns the document date unchanged; `max(document date, today)` returns the document date when the document is dated today or later; and the posting-time call **is** lock-gated. See `C07` addendum `A2-03` | `VERIFIED` on all four |
| `NC-23` | "Shipped state creates **no** rate rows" (`FXU-03` premise) | `C06` §3, §9 | shipped master data files | **`B → corrected basis`** | "Shipped master data contains no rate rows. A live-rate module is installed by default but defaults to manual with no scheduled run, so a newly activated currency still has zero rates until a human acts." | `PARTIALLY VERIFIED` — conclusion survives on a narrower basis |
| `NC-24` | "The par fallback has **two** entry points" and triggers when "**no rate row exists**" | `C06` §1, §4 | two sites read | **`D → widened`** | Additional fallback sites reported and `NOT YET SEARCHED`. Materially: the rate field is not `required`, so **a row with an empty value also triggers par**. Condition widened to "no rate row **with a non-empty value**" | `PARTIALLY VERIFIED`; the `required` finding independently `VERIFIED` |

## Reviewer B's negative audit — dispositions

Reviewer B audited 17 parent negatives and reported 9 contradicted. The research team verified the
two the Boss flagged and re-scoped the rest:

| Parent negative | Reviewer B verdict | Research team disposition | Basis |
|---|---|---|---|
| `N9` "exactly two things are unconditionally immutable" — B claims a **third** (audit-trail ratchet) | contradicted | **`CONTRADICTED` — reviewer's mechanism is real, reviewer's conclusion is not** | `company.py:317-322` does refuse to disable the audit-trail flag while any move exists. But the flag **defaults to off** and can be **enabled at any time**; the constraint only blocks the false direction. So it is a one-way ratchet — already recorded as `COR-19` — and it creates **no immutability for a company that never enabled it**, which is the default. `N9` stands as written; B's third item is rejected |
| `N1` "no provenance or idempotency carrier anywhere" | contradicted | **`PARTIALLY VERIFIED` — accepted with material qualification** | A genuine database constraint exists: `account_bank_statement_import/models/account_bank_statement.py:17-19` declares `unique (unique_import_id)`. **But** that module is `auto_install: False`, so the carrier is present only when an optional import module is installed; and the constraint is **table-global, with no company or tenant scoping**. Dedup within the importer is a Python search (`account_journal.py:262-264`), not the constraint. `N1` is re-scoped, not withdrawn: no **general, mandatory** carrier was found in `addons/account` |
| `N2` duplicate controls exist | contradicted | **`VERIFIED`** — already accepted as `NC-13` before the fresh round | — |
| `N8` unrealised-FX mechanism exists | contradicted | **`VERIFIED`** — recorded above as `NC-19` | — |
| `N3` outermost boundary is the **database**, not the company group | contradicted | **`PARTIALLY VERIFIED`** | Independently supported by two facts the research team already holds: the numbering-control parameter has no company dimension (`COR-16`), and rate rows may carry a null company, which `_get_rates` accepts (`:129`). The reporting-definition claim is `NOT YET SEARCHED`. The direction is accepted; `SB-05`/`SB-06` are recorded as open |
| `N7` control-account function exists | contradicted + veto on an internal inconsistency | **`PARTIALLY VERIFIED`** | The *function* is served by the reconcilable flag, account type and the trade/non-trade split — the parent said exactly this in file 02 (`A-13`) while file 18 asserted a bare negative and file 21 left `GAP-A01` open. The **inconsistency is real and is accepted**; the substantive position (no distinct control-account **entity**) is unchanged |
| `N6` / `CONTRA-01b` "not detected" | downgraded | **`VERIFIED` — accepted** | "Not detected" was written where "not **hash**-detected" was meant. Tax fields and the due date carry field-level change tracking. The evidence-free set narrows to **`amount_currency`, `currency_id`, `analytic_distribution`** and the reconciliation fields. `CONTRA-01b` is re-scoped accordingly and remains severe |
| `N10` an approval engine exists | contradicted at domain scope | **`NOT PROVEN`** | `NOT YET SEARCHED` by the research team. If correct, the reviewer's own observation that it is skipped under privilege elevation makes it a weak control and **raises the priority of `GAP-C04`** — which `C09` has now closed independently |
| `N11` reopening leaves no artefact | contradicted in part | **`VERIFIED`** | Lock-date changes are tracked and lock exceptions are first-class records. The governance conclusion — no distinct reopening **authority**, no close artefact — is unchanged |

## Revised counts for the whole programme

| Classification | Count |
|---|---|
| `E — CONTRADICTED` | **11** (`NC-01`, `NC-02`, `NC-03`, `NC-07` part, `NC-13`, `NC-19`, `NC-20`, `NC-21`, `NC-22`, plus B's `N2`/`N8` already folded in) |
| `A — VERIFIED ABSENCE` within a stated scope | 5 |
| `B — NOT FOUND IN SEARCHED SCOPE` | 8 |
| `C — NOT YET SEARCHED` | 14 |
| `D — UNKNOWN` | 2 |

**Over-scoped negatives found across the programme: nine.** Six in the parent package, **three
introduced by CORR1** (`NC-19`, `NC-20`, `NC-22`).

## The governance finding

CORR1 wrote the standard prohibiting over-scoped negatives and then committed three of them in the
same session, in documents written **after** the standard. The defect is therefore **not** ignorance
of the rule.

`INFERENCE:` the failure mode is structural. A researcher searches the module they are working in,
finds nothing, and writes the conclusion in the vocabulary of the domain rather than of the search.
The mitigation that has actually worked in this programme, twice, is **independent review** — not
author diligence. `DR-NC-05` is accordingly the load-bearing rule of the standard, and the standard
should be read as a review checklist first and an authoring guide second.
