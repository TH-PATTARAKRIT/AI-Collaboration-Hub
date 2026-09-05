# P01 — AAS-03 FRESH EXPERT CHALLENGE (SERIES-18 DIRECT VERIFICATION)

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-13`

**All four AAS-03 roles challenged this run independently, each against a frozen findings brief and
each with a mandatory disproof assignment. Experts provide perspectives, not verdicts. Disagreement
is preserved.**

Reports are held verbatim at `_expert_out4/EXPERT_{A,B,C,D}.md`.

---

## 1. HOW THIS ROUND WAS SET UP, AND WHY

The programme's standing lesson is that **independent review is the discovery engine** and that
**disproof assignments outperform review assignments**. Applied here:

- the findings were **frozen into a brief before any challenge opened** — no expert reviewed a
  moving target;
- each expert received **one primary disproof target**, phrased as a thing to break;
- **one expert (B) was scoped at the evidence base rather than at the findings** — the control that
  has caught the largest errors in this programme's history;
- every expert was required to attach a **positive control to every negative**, declare
  POPULATION / PATTERN / PATH SET / UNIT, and preserve disagreement rather than reconcile it.

**Outcome: 4 of 4 landed. Eleven corrections were adopted, two of them falsifying claims this run
had itself published.**

| Expert | Role | Primary disproof target | Result |
|---|---|---|---|
| **A** | Leader Functional Design | *"disprove that periodic policy explains the zero"* | could not overturn it as **sufficient**; **broke it as identified**; broke the discriminating set; found a measurement defect in the headline exposure |
| **B** | Leadership Database Design — **scoped at the evidence base** | *"disprove the series-18 identity"* + *"find another false-zero risk"* | identity **survived on a better instrument**; found the run's false-zero count was **1 where the artefacts show 4**; found a sentence that stated the negation of its own test |
| **C** | Lead Integration & Localization | *"disprove that GRNI is configured and reachable"* | **falsified a published finding**; falsified *"unreachable"* with **four writer routes**; falsified the withholding-mechanism attribution |
| **D** | Lead Code & UI Architect | *"find another population-selection defect"* | found **four**, including one that **disproves an absence this run published**, plus two defects it committed and corrected in-run |

---

## 2. WHAT WAS CHALLENGED AND SURVIVED

| Claim | Attacks it survived |
|---|---|
| **Valuation policy is `manual_periodic`, 126/126 categories** | Expert A attacked it four ways — jsonb, a **full 54-row `ir_default` enumeration** rather than a filtered search, deployed field metadata, and module attribution across 225,529 `ir_model_data` rows with a firing positive control (718 custom field xmlids, **zero** on any valuation field). Expert C independently resolved all **504** (category, company) pairs. It held every time |
| **The series-18 identity** | Expert B attacked the instrument successfully and the **claim** unsuccessfully — see §3.1 |
| **The zero-link count itself** | Re-extracted and re-parsed independently by A and by B; B re-derived every zero by raw field position with a harness that **raises on a missing column instead of returning 0**. Strongest control available: `stock_valuation_layer_id` is non-null on **2 rows of 47,801** in the same parse — a sparse many2one at 0.004% density, which a parser blind to sparse values could not produce |
| **Every P2P count and sum** | Reproduced **to the digit** by A: ฿30,080,689.78, ฿1,734,752.87, ฿22,953,527.29, 1,580 / 183 / 1,403 / 3,124. Currency and discount risk ruled out **by enumeration** — `currency_id` 133 and rate 1.0 on all 13,887 orders, discount zero on every line |
| **The bounded absences** (`ir_property`, landed costs) | Confirmed twice each, by TOC and by module state |
| **No custom module extends any valuation model** | Expert A, on the deployment: **0 custom xmlids on `stock.valuation.layer`** against a control of 1,160 custom xmlids. Expert C, on source: 0 hits for `property_valuation` / `stock_input` / `210300` across 2,179 files, against controls of 98 / 75 / 16 files. Expert D, on 44 located non-core sources: exactly one match, and it is `om_data_remove` |

---

## 3. WHAT WAS CHALLENGED AND CHANGED

### 3.1 The identity survived, but not on the instrument that was published

Expert B: `ir_module_module.latest_version` is an ordinary `varchar` a single `UPDATE` can set;
uniformity is consistent with a clean upgrade **and** with a bulk overwrite. **It does not
discriminate.** The identity now rests on the **schema** — and decisively on a string comparison:
`ir_model_fields_selection` holds **`manual_periodic`**, which series 19 renamed to `periodic`, so a
series-19 database **cannot physically contain it**.

**And this package adopted, then had to withdraw, two of Expert B's own discriminators** —
`origin_payment_id` and `lot_valuated` exist in series 19 too. **The expert caught itself**, having
sent its attributions for source verification rather than asserting them. Logged as `ERR-P01-36`,
because the package had already published the pre-withdrawal version.

### 3.2 Two findings this run published were falsified

| Falsified | By | Corrected to |
|---|---|---|
| *"The bill-line account override is a series-19 mechanism, NOT REACHABLE in series 18"* | **C**, independently confirmed by **D** | **The mechanism exists in v18**, in `account_move.py:264-279`, targeting the **GRNI** account. Inert here because `valuation != 'real_time'` — **not** absent. `ERR-P01-30` |
| *"No copy at `18.0.1.10.0` … VERIFIED ABSENCE"* | **D** | **It is at `~/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request`.** 11 of 16 modules have version-matching source, not 6. `ERR-P01-37` |

### 3.3 Eleven adopted corrections

`ERR-P01-26` a second, non-valuation-gated writer of both link columns · `ERR-P01-27` the
discriminating set rebuilt from 1,812 to 558 / core 541 · `ERR-P01-28` the exposure restated
tax-exclusive · `ERR-P01-29` the exposure decomposed by receipt provenance · `ERR-P01-30` the
bill-line override · `ERR-P01-31` reachability by four writer routes · `ERR-P01-32` the module
population is 56, not 16 · `ERR-P01-33` the withholding attribution · `ERR-P01-34` a sentence
stating the negation of its own test · `ERR-P01-35` two never-transacted companies counted as
confirmations · `ERR-P01-36` an expert claim adopted then withdrawn · `ERR-P01-37` a false absence ·
`ERR-P01-38` the artefact census · `ERR-P01-39` a source tree accepted on its label ·
`ERR-P01-40` two installed modules that bound every count.

---

## 4. THE FIVE MANDATORY DISPROOF ATTEMPTS

| # | Target | Outcome |
|---|---|---|
| 1 | **Disprove the series-18 deployment identity** | **Not disproved.** Attacked at the instrument and succeeded there; attacked at the claim and failed. The claim is now stronger than when challenged |
| 2 | **Disprove that periodic policy explains the zero-link result** | **Partly disproved.** Sufficient, **not identified**: a non-valuation-gated writer exists, and 4,574 of 47,801 rows are over-determined. The conclusion survives on a corrected denominator of **541** |
| 3 | **Disprove that GRNI is materially configured and reachable** | **Configured: strengthened** — 171 of 504 pairs, and 126 of 126 in the transacting company. **Reachable: the package's own "unreachable" was disproved** — four writer routes, none needing a code change |
| 4 | **Find another population-selection defect** | **Four found**, one of them falsifying an absence this run published |
| 5 | **Find another false-zero extraction risk** | **Found.** The run's own count of its false zeros was **1 where the artefacts show 4**, and the discriminator that would have caught all four was available throughout |

---

## 5. PRESERVED DISAGREEMENT

**Experts A and B disagreed about the discriminating set, and both are right.**

- **A**: the 1,812 "native" layers overstate the denominator ~3.25×; 1,254 are `__system__`
  inventory adjustments. The defensible set is **558**.
- **B**: the 1,812 **are** natively created — `create_date == write_date` at sub-second resolution
  on 1,640 of them, **four distinct** `create_uid`s, write times outside the load window — against
  45,978 migrated rows that loaded in **97 seconds**, all under user 1, every `create_date` at
  exactly midnight.

**Not reconciled away.** They are about different properties: **B** answers *were these written by
this runtime*, **A** answers *are these business events*. The set is native **and** dominated by
machine stock-take. Both corrections are carried.

---

## 6. WHAT EACH EXPERT SAYS IS MISSING, AND IS NOT CLOSED

| Expert | Missing | Status |
|---|---|---|
| **A** | Any scoping of the negatives to **method-level** override. `ir_model_data` bounds field, model, view and data extension; **a Python method override leaves no database trace** | **OPEN** — every negative in the policy proof is now scoped to *"no field- or data-level override; method-level override unverified"*. The denominator for that scope is **56 modules**, and Expert D has since located source for many of them |
| **A** | Whether the 16 price-difference layers had `remaining_qty > 0` when their bills posted | **OPEN** — undecidable from a single snapshot |
| **B** | `ir_logging` and `ir_cron_trigger` are **genuinely empty**, not failed extractions | **CLOSED as an avenue.** No argument may be built on their silence |
| **C** | Whether any user can actually **write** `property_valuation` in company 1 | **OPEN, and explicitly flagged** — until measured, route 1 of §3.2 is a *capability*, not a live exposure |
| **C** | Whether P01's series-16 withholding finding concerns this same OCA family at an earlier version | **NOT DECIDABLE** here. **No transfer made in either direction** |
| **D** | Ten database artefacts, including the largest on this host and an entire series-18 database | **OPEN** — the first item of the next action |
| **D** | `accessories` 18.0.0.1 — **25 fields on `account.account`**, a declared dependency of a module this package did analyse | **OPEN** — never in scope |

---

## 7. THE EXPERTS' OWN ERRORS, RECORDED

Both self-caught, both instructive, and both recorded because a challenge layer that reports no
errors of its own is not being audited either.

- **D-E01.** `--include=*.py` unquoted in `zsh` → thirteen modules returned an empty inheritance
  list. Had the shell not printed its own error, the output would have read as *"no custom module
  inherits any accounting model"*. Re-run quoted, with a positive control against core
  `stock_account`.
- **D-E02.** A database identity read as *"the first uuid-shaped string in the file"* returned
  `58871b73-…` — which is `database.secret`, not `database.uuid`. **It would have contradicted this
  package's identity claim and raised a false finding.** Corrected by parsing the `key` column.
  *An identifier read by position in a file is not an identifier.*
- **B**, withdrawing two of its own version discriminators after sending them for source
  verification (§3.1).
- **A**, correcting its own percentage from 3.62% to **3.49%** — it had taken the ratio against the
  corrected base rather than the published one.

---

## 8. WHAT EVERY EXPERT SAYS IS NEEDED NEXT

Converged, unranked by role:

1. **Read the ten unenumerated database artefacts**, starting with the **283 MB `dump.sql`** inside
   `BK12MAY26_2026-08-03_11-28-04.zip` — an Odoo **19.0+e** database, and this whole package is
   about the v18→v19 semantic change — and **`pankhamhom`**, a series-18 database with a 478-module
   manifest.
2. **Read the located source for the deployed custom modules**, now that 11 of 16 are available —
   `scgl_account_coa_control 18.0.1.0.1` first — and grep for method-level overrides of
   `_validate_accounting_entries`, `_account_entry_move`, `AccountMove._post`, `property_valuation`.
   Until then the method-override gap is unbounded.
3. **`mail_tracking_value` on `product.category`** — `property_cost_method` carries `tracking=True`
   and `property_valuation` does not. Tracking rows would settle **whether this deployment was ever
   `real_time`**, which no current-state read can. *(Partly executed already: 240 tracking rows exist
   on `product.category`, of which **9 are on `property_cost_method`** — the question is live and the
   instrument works.)*
4. **The deployed `om_data_remove` 18.0.1.0.0 source**, then `ir_logging` and `mail_message` around
   its wizard.
5. **`occ_sim_pre_perpetual.dump`** — a local simulation-lab snapshot **named for the exact
   `Perpetual (at invoicing)` transition** this package is about, and never cited.
6. **Measure write access to `property_valuation` in company 1** — the unmeasured clause that turns
   a capability into an exposure.
7. **Re-run every inherited census** against the corrected 27-artefact set.
