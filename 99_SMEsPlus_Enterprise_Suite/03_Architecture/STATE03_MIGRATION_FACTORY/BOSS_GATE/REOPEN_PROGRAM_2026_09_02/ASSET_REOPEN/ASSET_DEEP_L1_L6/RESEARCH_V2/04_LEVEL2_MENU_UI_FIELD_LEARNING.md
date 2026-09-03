# 04 — DEEP LEVEL 2: MENU / UI / FIELD / SOURCE LEARNING
**LAYER 2 — AUDIT QUARANTINE**

Governing rule for this level (§14): **UI representation is not functional truth.**
Every row below records where the fact came from, and the level closes with an
explicit list of places where the UI actively misleads.

## 1. Menu coverage — what the asset module actually contributes

The asset module ships **exactly one menu item of its own**: a *Depreciation
Schedule* report entry. Everything else the user sees is reached through views the
module grafts onto the accounting application.

`FACT VERIFIED` — the module's menu data file contains a single menu record.

| Menu surface asked for by §15 | Exists | How it is reached |
|---|---|---|
| Asset Models | Yes | A window action filtered to template status |
| Assets | Yes | A window action filtered to non-template status |
| Depreciation Board | Yes | **Not a menu.** An embedded list of journal entries inside the asset form |
| Asset Entries | Yes | The same journal entries, reachable from the entry side |
| Asset Reporting | Yes | The one real menu item — Depreciation Schedule |
| Asset Actions | Yes | Buttons on the form, not menus: Confirm, Compute Depreciation, and the modify wizard |
| Asset Modification | Yes | A transient wizard, five actions behind one dialog |
| Asset Sale | Yes | An option inside that same wizard |
| Asset Disposal | Yes | An option inside that same wizard |
| Asset accounting setup | Yes | Fields added to the **account** form, not to an asset menu |
| Asset analytic setup | Yes | A distribution field on the asset itself |
| Asset configuration | **Partial** | Gain/loss accounts live on the **company**, not in any asset configuration screen |

**Level-2 finding that matters:** four distinct business events — re-evaluate,
pause, resume, sell, dispose — are collapsed into **one wizard** whose behaviour
is switched by a single selection field. Menu-shaped analysis sees one "Modify"
action. Function-shaped analysis sees five different accounting outcomes. This is
precisely the failure mode the governing prompt was written to prevent, and it is
the reason `24` and `25` are separate deliverables.

## 2. Field register — the asset model

Legend: **S** stored · **C** computed · **R** related · **RO** readonly ·
**Req** required · **T** tracked · **Rec** recursive

### 2.1 Identity and control

| Field (technical) | Type | Characteristics | Notes |
|---|---|---|---|
| `name` | Char | C+S, `readonly=False`, **Req**, **T** | Computed from the source bill line, then user-overridable |
| `state` | Selection(6) | **RO**, default `draft` | `model / draft / open / paused / close / cancelled`. Never written directly by a user |
| `active` | Boolean | default True | Archive guarded — only when `close` or `model` |
| `company_id` | M2o | **Req** | |
| `currency_id` | M2o | **R** from company, S | **Not independently settable.** No foreign-currency asset |
| `country_code` | Char | **R** | Reaches through company → fiscal country |
| `journal_id` | M2o | C+S, `readonly=False` | Restricted to general journals |
| `asset_group_id` | M2o | indexed, **T** | A pure reporting grouping. No behaviour attached |
| `model_id` | M2o (self) | | Points at a record whose `state = 'model'` |
| `parent_id` / `children_ids` | M2o / O2m (self) | | The value-increase tree |

### 2.2 Depreciation parameters

| Field | Type | Characteristics | Notes |
|---|---|---|---|
| `method` | Selection(3) | default linear, **T** | Straight-line / declining / declining-then-straight-line |
| `method_number` | Integer | default 5, **T** | Labelled *Duration*. See §4 — the label is wrong |
| `method_period` | Selection(2) | default `12` | The **number of months in a period**: `1` = monthly, `12` = yearly |
| `method_progress_factor` | Float | default 0.3, **T** | Declining factor only |
| `prorata_computation_type` | Selection(3) | **Req**, default constant periods | The single most consequential field on the model — `16` |
| `prorata_date` | Date | C+S, `readonly=False`, **Req**, precompute | Start of the first period for prorata purposes |
| `paused_prorata_date` | Date | **C, not stored** | `prorata_date` shifted by accumulated pause days |
| `asset_lifetime_days` | Float | **C, Rec** | Total days in the life. **Meaning depends on the prorata mode** — `16` §3 |
| `asset_paused_days` | Float | S, `copy=False` | Accumulator, not a duration |
| `acquisition_date` | Date | C+S, precompute | Min of the source bill dates, else today |
| `disposal_date` | Date | C+S | Populated only in `close` |

### 2.3 Value fields — the part most often misread

| Field | Type | Characteristics | Definition from source |
|---|---|---|---|
| `original_value` | Monetary | C+S, `readonly=False` | Sum of source bill line balances (÷ quantity if split), plus non-deductible tax |
| `salvage_value` | Monetary | C+S, `readonly=False` | *Not Depreciable Value*. Excluded from the base |
| `salvage_value_pct` | Float | plain | Used **only** to derive salvage from a model |
| `total_depreciable_value` | Monetary | **C, not stored** | `original_value − salvage_value` |
| `value_residual` | Monetary | **C, not stored** | `original − salvage − imported − Σ posted depreciation` |
| `book_value` | Monetary | **C+S, Rec, RO** | `value_residual + salvage_value + Σ children book_value` — **and salvage is subtracted again once closed** |
| `gross_increase_value` | Monetary | C | Σ children original values |
| `non_deductible_tax_value` | Monetary | C+S, RO | Added into original value |
| `related_purchase_value` | Monetary | C | The raw bill total before tax adjustment |
| `already_depreciated_amount_import` | Monetary | plain | Migration field — reduces the board without a journal entry |
| `net_gain_on_sale` | Monetary | plain, `copy=False` | Written once at disposal |

**Expert 2's Level-1 warning is now confirmed at field level:** `book_value` is
`recursive=True`. It is an aggregate over the parent/child tree, not a property of
the row. `G1-04` is closed.

### 2.4 Analytic

| Field | Source | Characteristics |
|---|---|---|
| `analytic_distribution` | inherited from an analytic mixin | C+S, `readonly=False` |

The distribution is **computed from the source bill lines, balance-weighted**, and
then user-overridable. Full treatment in `21`.

### 2.5 Accounts

| Field | Domain restriction observed in source |
|---|---|
| `account_asset_id` (Fixed Asset) | Excludes off-balance accounts |
| `account_depreciation_id` (Depreciation) | Excludes receivable, payable, cash, credit card, off-balance, deprecated |
| `account_depreciation_expense_id` (Expense) | Same exclusion set |

**Carry this straight to `62`/`14`:** the reference product **explicitly forbids
off-balance accounts on all three asset accounts.** The Boss's Off-Balance design
therefore cannot be expressed through the asset record's own account fields. It
must be a separate posting mechanism. This is a hard, source-level constraint, and
it is one of the more useful findings for the SMEsPlus design.

`FACT VERIFIED` — the three field domains.

## 3. Field visibility — closing `G1-05`

43 field references appear in the asset form view. Comparing them against the
model definition:

**In the model but in no view** (implementation detail, not capability):
`asset_lifetime_days`, `asset_paused_days`, `paused_prorata_date`,
`non_deductible_tax_value`, `related_purchase_value`, `net_gain_on_sale`,
`total_depreciable_value`, `disposal_date`, `country_code`, `model_id`,
`linked_assets_ids`, `asset_properties_definition`, `original_move_line_ids`.

This matters for two reasons:

1. **`asset_paused_days` is invisible.** The single value that shifts an asset's
   entire remaining schedule after a pause cannot be seen or audited by a user in
   the standard form. A pause is effectively an unreviewable change to the
   schedule.
2. **`net_gain_on_sale` is invisible.** The system computes a gain/loss figure and
   stores it, and does not show it.

`FACT VERIFIED` — view field extraction versus model field definitions.

## 4. Where the UI is actively misleading — the §14 deliverable

| # | Label the user sees | What the source actually does | Severity |
|---|---|---|---|
| `UI-01` | **Duration** | The number of **periods**, whose length is set by a *different* field. "Duration 60" with yearly periods is sixty **years** | High |
| `UI-02` | **Number of Months in a Period** | Has only two legal values, 1 and 12. It is a monthly/yearly switch wearing the costume of a free integer | Medium |
| `UI-03` | **Computation** *(constant periods / based on days per period)* | Chooses between a **30/360 convention** and a **calendar-day convention**. Nothing in the label says the first one ignores the calendar entirely | **Critical** |
| `UI-04` | **Not Depreciable Value** | Correct as far as it goes, but it does not say that this amount is silently **removed from book value on closure** — `18` §6 | High |
| `UI-05` | **Depreciable Value** on the board lines | The board shows *remaining* value per line; the same words name a different field on the header | Medium |
| `UI-06` | **Modify / Re-evaluate** | One button, five distinct accounting events including creating a whole new asset record | High |
| `UI-07` | Asset Model | Suggests a template entity. It is the same table | Medium |

`UI-03` is the one that will cost real money. A Thai user reading *"Computation:
Constant Periods"* has no way to know from the label that February and January
will depreciate by identical amounts.

## 5. Custom module discovery — §17

The prompt named two modules as examples and instructed that they must not be
assumed to be the only ones. Search of the workspace custom addon set found the
following asset-relevant modules:

| Module | Line | Touches | Verdict |
|---|---|---|---|
| Equipment/product-stock bridge | v18 | Creates equipment records from stock and inventory events; adds equipment fields to the product template | `CUSTOM` — the Product→Equipment route, `20` |
| Equipment sequence/asset-link | v18 | **Adds the Asset→Equipment field**, equipment reference codes, category-driven sequences | `CUSTOM` — `19` |
| Thai straight-line depreciation | **v14 only** | Adds a fourth depreciation method with true calendar-day arithmetic | `CUSTOM` — **no v18 copy found**, `26` §5 |
| Third-party accounting kit / community asset module | **v14 only** | Defines a *second, different* asset model | The source of contradiction `CTR-03` |

**`G1-01` is not closed by this.** These are the modules present in the workspace.
The installed module list of the running UAT remains unknown, and every negative
statement in this package keeps that qualifier.

## 6. Technical data ownership — §18

The prompt requires that view ownership must not be read as data ownership. Applied:

| Concern | Owner | Evidence |
|---|---|---|
| **Model owner** | Reference product asset module | Model definition |
| **Field owner — standard fields** | Same | Field definitions |
| **Field owner — the equipment link** | Project custom module | Custom field definition |
| **View owner — asset form** | Reference product | Base view record |
| **View owner — the equipment link group** | Project custom module, by inherited view | Inherited view record |
| **Function owner — depreciation** | Reference product, exclusively | The board methods |
| **Function owner — equipment status flip** | Project custom module, by overriding the confirm method | Custom override |
| **Business source of truth — asset value** | The **vendor bill**, not the asset | Value is computed from bill line balances |
| **Business source of truth — analytic** | The **vendor bill**, then overridable | Distribution computed from bill lines |
| **Business source of truth — book value** | **The journal entries**, not the asset row | Residual is `Σ posted depreciation` |

The last row is the important one and it inverts the naive picture: **the asset
record is not the source of truth for the asset's value.** The posted journal
entries are. The asset row is a derived view over them. Any SMEsPlus migration
that copies asset rows without their entries copies nothing of substance.

## 7. Runtime corroboration — `EV-RT`, UAT `idemo18_uat`, 2026-08-26

| Observation | Value |
|---|---|
| Asset templates | 16 |
| Real assets (non-template), company 1 | **280** |
| — draft | 35 |
| — running | 217 |
| — on hold | **1** |
| — closed | 27 |
| — cancelled | 0 |
| Companies 2, 3, 4 | 0 records in every state |
| Assets with a template linked (`model_id`) | **0 of 280** |
| Distinct account triples in use | 6, of which one is *all three accounts empty* on 35 records |

Two things follow directly, and both are corroborated by the project's own
migration handoff record (`EV-HND`):

1. **Every one of the 280 assets is detached from its template.** Whatever the 16
   templates configure, no live asset inherits from them.
2. **35 assets carry no accounts at all** — all three account fields empty. The
   draft count is also 35, so these are very likely the same 35 records, but the
   read-out grouped state and account-triple *separately* and did not cross them.
   Treat the identity as `SUPPORTED INTERPRETATION`, not fact. The confirm path
   posts entries against those three accounts, so on the face of the code these
   records could not be confirmed as they stand — also an interpretation until
   someone tries it.

`FACT VERIFIED` — the counts themselves, from the runtime read-out, corroborated
by the independent handoff record.
`SUPPORTED INTERPRETATION` — the identification of the account-less 35 with the
draft 35, and the consequence drawn from it. Recorded as `UNR-07`.

## 8. Four Expert opinions

See `05_LEVEL2_FOUR_EXPERT_OPINIONS.md`.
