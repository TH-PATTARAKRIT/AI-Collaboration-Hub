# 03 — Menu A: Accounting → Configuration → Settings → Inventory Valuation Evidence

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE ONLY — READ-ONLY DEEP RESEARCH — CP-03, NOT A DESIGN FREEZE`

---

## 1. Scope and Method

This file is the Menu A evidence sheet required by the governing prompt §6 ("MENU A — Accounting → Configuration → Settings → Inventory Valuation") and uses the mandatory field evidence sheet format from §7. Menu A is the **Accounting-app, company-scoped** settings surface — distinct from Menu B (Inventory → Configuration → Product Categories, file `04`, authored in parallel by another agent) and Menu C (Product → Accounting tab, file `05`). Where a field's behavior can only be fully understood by reading it together with Menu B, this file describes the interaction **generically** (what the two surfaces jointly determine) without assuming file `04`'s content.

File `02` (Version Delta Register) established that Menu A's own shape is **not stable** across the reference versions in scope: versions `13.0` through `saas-18.4` expose a single boolean company-level control (`Automatic Accounting`) that only reveals a Product-Category-level field; version `19.0` (reconstructed, `PROVISIONAL` — see file `02` §2 and §4) exposes several fields directly at company level, with Product Category described as able to override them. This file therefore presents **two field sets**, clearly labeled by version range, rather than one merged table — merging them would silently manufacture a "Menu A" that never existed in any single version, which the governing prompt's clean-room rule forbids.

Three evidence layers per the governing prompt §3:
- **Layer A** — Reference ERP observed behavior (this file's tables).
- **Layer B** — Thai evidence: `N/A in this file` — routed to file `24`.
- **Layer C** — SMEsPlus candidate semantics: stated only as `CANDIDATE` or `HOLD/JOINT` in §5, never as a decided design.

---

## 2. Field Evidence Sheet — Version Range `13.0` – `saas-18.4`

### 2.1 Field: `Automatic Accounting` (checkbox)

| Requirement | Evidence |
|---|---|
| Menu Path | `Accounting app → Configuration → Settings`, "Stock Valuation" section. Path confirmed identically across `13.0`, `saas-15.3`, `saas-16.4`, `17.0`, `18.0`, `saas-18.4`. |
| Field Label | `Automatic Accounting` (checkbox) |
| Purpose | Observed as the single company-level gate that switches the accounting-recognition mode for stock moves from no automatic posting to automatic real-time posting, and simultaneously reveals a normally-hidden field (`Inventory Valuation`, Manual/Automated) on the Product Category form. |
| Values / Options | Boolean: unchecked (default) / checked |
| Default | Unchecked — `VERIFIED` (multiple versions' documentation state periodic/manual valuation as the out-of-the-box default) |
| Visibility | Always visible on this settings page once the Accounting app is installed |
| Scope | Company (this settings page is a company-level Accounting Settings page; not itself proven to vary the checkbox per company in this pass — see §2.6) |
| Inherits From | No parent — this is the top-level company gate |
| Override Precedence | This checkbox does not itself get overridden; it only **unlocks** a lower-scoped field (Product Category `Inventory Valuation`). If left unchecked, the Product-Category-level `Inventory Valuation` field is hidden and, per the documentation's implied behavior, valuation stays at the periodic/manual pattern regardless of any Product Category setting. |
| Transaction Consumer | Not itself a transaction consumer — it is a feature gate. The transactions affected downstream are: goods receipt, vendor bill validation, delivery, customer invoice validation, and manual/periodic closing entries, depending on what Product Category ends up configured once this gate is open. |
| Periodic Behavior | Checkbox unchecked (or Product Category left at Manual even with the checkbox on): no automatic journal entry on stock move; the accounting team manually posts inventory valuation adjustments, documented as done through `Inventory → Reporting → Inventory Valuation` in `13.0`, and confirmed structurally similar in later versions in this range. |
| Perpetual Behavior | Checkbox checked and a Product Category set to `Automated`: real-time journal entries are created on stock moves in/out, using the Product Category's Stock Input/Output/Valuation accounts. |
| Account Type Impact | Indirect only — this field selects a mode; the actual accounts touched are Product-Category-scoped (Stock Valuation = Current Asset type; Stock Input/Output = interim asset/liability-style clearing accounts; Expense Account type varies by mode, see §2.6). |
| Financial Statement Impact | Both (Balance Sheet inventory asset carrying value and P&L expense/COGS timing both depend on this gate combined with the Product Category setting it unlocks). |
| Change Impact | Toggling this setting after stock already has value is explicitly documented as risky: "switching from manual to automatic inventory valuation may cause discrepancies between stock valuation and accounting journals," with a documented mitigation pattern of clearing stock, changing the mode, then re-entering stock via an inventory adjustment carrying the original monetary value. This is future-facing remediation guidance, not proof of a clean, non-disruptive in-place switch. |
| Version Delta | Present with this exact label and location across `13.0`–`saas-18.4`. Superseded in the `19.0` reconstruction by a differently-shaped `Inventory Valuation` field with `Perpetual (at invoicing)` / `Periodic (at closing)` options living directly at company level (see §3). Do not carry this field forward into `19.0` evidence — see file `02` §4.1. |
| Evidence | Reference ERP official documentation — Automatic inventory valuation (Stock Valuation section, Accounting Settings), versions 13.0, saas-15.3, saas-16.4, 17.0, 18.0, saas-18.4, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for presence, label, location, and default across the six directly-fetched versions in this range. `PROVISIONAL` for whether the checkbox is literally per-company vs. global-with-a-company-selector (§2.6). |

### 2.2 Field: (unlocked) `Inventory Valuation` — Manual / Automated

Recorded here **only** for the interaction it has with Menu A, since the field itself physically lives on the Product Category form (Menu B, file `04`'s primary subject).

| Requirement | Evidence |
|---|---|
| Menu Path | `Inventory app → Configuration → Product Categories → [category] → Inventory Valuation` section — but its **visibility is gated by Menu A's `Automatic Accounting` checkbox** |
| Field Label | `Inventory Valuation`: `Manual` / `Automated` |
| Purpose | Determines, per category, whether stock moves in that category post automatically |
| Values / Options | `Manual` (default), `Automated` |
| Default | `Manual` — `VERIFIED` across all directly-fetched versions in this range |
| Visibility | Conditional — hidden entirely unless Menu A's `Automatic Accounting` checkbox is enabled at company level |
| Scope | Product Category (cross-reference file `04` for full field register) |
| Inherits From | No default inheritance mechanism observed from company to category for this specific field in this version range beyond the visibility gate itself — the category value is set directly by a user, not defaulted from a company-level valuation-mode field, because no such company-level valuation-mode field is documented as existing in this version range. |
| Override Precedence | N/A in this range — there is no company-level value to override; only a visibility gate |
| Transaction Consumer | Stock receipt, delivery, adjustment, and closing entries |
| Periodic Behavior | `Manual` selected: no automatic posting on the move; accounting team posts a period-end entry |
| Perpetual Behavior | `Automated` selected (and company gate on): real-time posting per stock move |
| Account Type Impact | Determines which of the category's Expense Account / Stock Input / Stock Output / Stock Valuation accounts actually receive postings (full detail is file `04`'s subject) |
| Financial Statement Impact | Both BS and P&L, timing differs by mode |
| Change Impact | Same discrepancy risk as §2.1 |
| Version Delta | Present `13.0`–`saas-18.4`. In the `19.0` reconstruction, the equivalent choice (`Perpetual`/`Periodic`) is described as living at company level by default with category-level override — i.e., the inheritance direction is reversed relative to this range, where the field is category-native and only gated (not defaulted) by the company. See file `02` §4.1. `HOLD / EVIDENCE REQUIRED` before assuming any inheritance mechanic for `19.0`. |
| Evidence | Reference ERP official documentation — Automatic inventory valuation, versions 13.0, saas-15.3, saas-16.4, 17.0, 18.0, saas-18.4, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for the visibility-gate mechanic and default. `HOLD` for any company-to-category default/inheritance claim beyond the visibility gate — none was found in this version range. |

### 2.3 Field: Costing Method (Menu B field, Menu A interaction only)

| Requirement | Evidence |
|---|---|
| Menu Path | Lives entirely on `Inventory app → Configuration → Product Categories → [category]`; **no Menu A equivalent exists in this version range** |
| Field Label | `Costing Method`: Standard Price / Average Cost (AVCO) / First In First Out (FIFO) |
| Purpose | Determines how unit cost is computed for valuation and release |
| Values / Options | Standard Price (default), Average Cost (AVCO), FIFO |
| Default | Standard Price — `VERIFIED` |
| Visibility | Always visible on the category form regardless of the `Automatic Accounting` checkbox state (unlike the `Inventory Valuation` field, which is gated) |
| Scope | Product Category only, in this version range |
| Inherits From | No company-level default source exists to inherit from in this range — `VERIFIED absence` in the six directly-fetched versions |
| Override Precedence | N/A — category is the only place this is set in this range |
| Transaction Consumer | Receipt (cost formation), delivery/issue (cost release), inventory adjustment |
| Periodic Behavior | Cost method still determines the value used at period-end closing entry computation even when `Inventory Valuation` is Manual |
| Perpetual Behavior | Cost method determines the amount posted on each real-time stock-move journal entry |
| Account Type Impact | Interacts with Price Difference Account behavior specifically for Standard Price (see file `02` §7 — flagged `CONFLICTING` across versions, do not treat as settled) |
| Financial Statement Impact | Both |
| Change Impact | Changing costing method on a category with existing valued stock is a **known-risk transaction boundary**; this pass did not obtain a direct primary-documentation statement of exact mechanics for a live in-place change (this belongs to file `15`, Costing Method Deep Research Matrix) — `HOLD / EVIDENCE REQUIRED`, not asserted here |
| Version Delta | Category-only in `13.0`–`saas-18.4`. Reconstructed as **also** present at company level (`Inventory Cost Method`) starting `19.0`, `PROVISIONAL` — see file `02` §5. |
| Evidence | Reference ERP official documentation — Automatic inventory valuation, versions 13.0, saas-15.3, saas-16.4, 17.0, 18.0, saas-18.4, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for category-only scope and three-option list, this version range. |

### 2.4 Fields: Stock Valuation Account / Stock Input Account / Stock Output Account / Stock Journal (Menu B fields, Menu A interaction only)

| Requirement | Evidence |
|---|---|
| Menu Path | Category form, `Account Properties` |
| Field Label | `Stock Valuation Account`, `Stock Input Account`, `Stock Output Account`, `Stock Journal` |
| Purpose | Stock Valuation Account holds current stock value (Current Asset type); Stock Input/Output are counterpart clearing accounts for incoming/outgoing moves; Stock Journal is the accounting journal automatic entries post into |
| Values / Options | Any account of the matching type from the company chart of accounts (free selection, not an enumerated list) |
| Default | Not confirmed as pre-populated with a specific account in this pass — `HOLD / EVIDENCE REQUIRED` |
| Visibility | Only meaningfully used when `Inventory Valuation` = `Automated` at category level (which itself requires Menu A's checkbox); Stock Valuation Account is described as used in Automated mode specifically |
| Scope | Product Category, in this version range |
| Inherits From | No company-level default field for these in this range |
| Override Precedence | N/A in this range |
| Transaction Consumer | Receipt, delivery, adjustment (all real-time postings under Automated mode) |
| Periodic Behavior | Under Manual, these accounts are not used for automatic postings; the accounting team's manual entry references the current asset "Stock Valuation" style account directly through the closing/adjustment process rather than an automated Input/Output pair |
| Perpetual Behavior | Under Automated, every stock move posts a journal entry crediting/debiting Stock Input or Stock Output against Stock Valuation, in the Stock Journal |
| Account Type Impact | Stock Valuation = Current Asset; Stock Input/Output = interim/clearing accounts whose type varies by accounting mode (Continental: both reference the same Current Assets account per the `17.0` evidence; Anglo-Saxon-style: differ) |
| Financial Statement Impact | Balance Sheet primarily (asset carrying value); P&L only at the point cost is released via the Expense Account (§2.5) |
| Change Impact | Not independently confirmed in this pass; deferred to file `04` |
| Version Delta | `Stock Journal` as a named field is documented from at least `17.0`/`18.0` onward in the versions directly fetched in this pass; earlier-version presence of a field with this exact label was not independently confirmed — `HOLD` on `13.0`–`saas-15.3` exact field-name parity, though the underlying journal concept (some journal receives the automated entries) is implied throughout. |
| Evidence | Reference ERP official documentation — Automatic inventory valuation, versions 17.0, 18.0, saas-18.4, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` for `17.0`/`18.0`/`saas-18.4` presence. `PROVISIONAL` for exact field-name parity in `13.0`–`saas-16.4`. |

### 2.5 Field: Expense Account (Menu B field, Menu A interaction only — mode-dependent account type)

| Requirement | Evidence |
|---|---|
| Menu Path | Category form, `Account Properties` |
| Field Label | `Expense Account` |
| Purpose | The account used, in both Manual and Automated modes, as the counterpart for cost recognition — but the **required account type differs by mode**, which is the material fact for Menu A's interaction with this field |
| Values / Options | Any account, but the documentation constrains the expected *type* by mode |
| Default | Not confirmed pre-populated — `HOLD / EVIDENCE REQUIRED` |
| Visibility | Always visible; used in both Manual and Automated modes (unlike Stock Input/Output, which are Automated-only) |
| Scope | Product Category, in this version range |
| Inherits From | No company-level default field for this in this range |
| Override Precedence | Product-level override exists per file `05`'s subject (Menu C) — this file does not assert file `05`'s content, only flags the interaction exists |
| Transaction Consumer | Vendor bill validation, cost-of-sale recognition, period-close entry |
| Periodic Behavior | For **manual** valuation, the documentation states the Expense Account should be set to a **Stock Valuation-type (Current Asset)** account — i.e., under manual/periodic valuation, the "Expense Account" field is being used to hold a balance-sheet-style value, not a P&L expense, until the periodic close entry moves the balance |
| Perpetual Behavior | For **automatic** valuation, the documentation states the Expense Account should be set to an **Expenses or Cost of Revenue type** account — i.e., the same field name is used for a genuine P&L expense/COGS account under automated valuation |
| Account Type Impact | This is the single most important Account-Type-Impact fact on this whole surface: **the same field label ("Expense Account") is expected to hold two structurally different account types depending on the Menu A / Menu B valuation-mode combination** — Current Asset under Manual, Expense/Cost of Revenue under Automated. A configuration built for one mode and then carried into the other mode without re-pointing this field would misclassify the account on the financial statements. |
| Financial Statement Impact | Both — under Manual it is effectively a Balance Sheet holding field pending close; under Automated it is a direct P&L posting target |
| Change Impact | Switching valuation mode without re-pointing this field is a direct source of BS/P&L misclassification — flagged here as a **material control risk**, not yet mapped to a specific SMEsPlus control in this file |
| Version Delta | This dual-type behavior was documented consistently across the directly-fetched versions in this range (`13.0` through `saas-18.4`); no version-specific change identified in this pass |
| Evidence | Reference ERP official documentation — Automatic inventory valuation, versions 13.0, saas-16.4, 17.0, 18.0, saas-18.4, retrieved 2026-09-02 |
| Fact Status | `VERIFIED` — this dual-type-by-mode behavior is stated consistently and directly in multiple directly-fetched pages, not merely inferred. |

### 2.6 Company Scope — cross-cutting note, this version range

`HOLD / EVIDENCE REQUIRED`: this pass confirmed the Accounting Settings page (Menu A) is reached via a company-context menu (`Accounting app → Configuration → Settings`) and that the reference ERP's general multi-company documentation describes account/journal mapping as configurable "by company," but did **not** obtain a direct, version-specific statement that the `Automatic Accounting` checkbox itself is stored per-company versus being a single global setting with a company-context switcher changing which company's data you are viewing. Given the reference ERP's general multi-company architecture pattern (most Accounting Settings fields are company-scoped), this file records a `PROVISIONAL` assumption of per-company scope, and explicitly declines to assert it as `VERIFIED`. This interacts directly with `JT-01` (valuation-policy ownership) and the multi-company/tenant register (file `25`) and must not be treated as settled by this file alone.

---

## 3. Field Evidence Sheet — Version `19.0` (reconstructed, `PROVISIONAL` — requires direct re-fetch before downstream reliance)

File `02` §2 records that direct fetch of the primary `19.0` Finance/Accounting page failed twice in this pass (tool-level empty-content error) and that this table is built from search-index snippets of that same official page, corroborated by one directly-fetched companion page (the `19.0` Inventory-app "Valuation cheat sheet") and one official reference-ERP conference/release source describing the same architecture change. Every row below is `PROVISIONAL` unless otherwise stated, and this entire table is explicitly flagged `HOLD / EVIDENCE REQUIRED — RE-VERIFY BY DIRECT FETCH` before any later file in this session (`06`, `08`, `10`, `12`, `13`) relies on it as settled.

### 3.1 Field: `Inventory Valuation`

| Requirement | Evidence |
|---|---|
| Menu Path | `Accounting → Configuration → Settings → Inventory Accounting` (new section name observed in reconstruction; not independently confirmed to be visually distinct from a "Stock Valuation" section carried over — `PROVISIONAL`) |
| Field Label | `Inventory Valuation` |
| Purpose | Company-level selection of valuation-timing mode |
| Values / Options | `Perpetual (at invoicing)` / `Periodic (at closing)` |
| Default | Not confirmed by direct quote in this pass — `HOLD / EVIDENCE REQUIRED` |
| Visibility | Always visible on this settings page, per reconstruction (no gating checkbox analogous to `Automatic Accounting` identified in the `19.0` reconstruction — this itself is a delta from §2.1 and needs direct confirmation) |
| Scope | Company |
| Inherits From | No parent above company |
| Override Precedence | Product Category is described as able to override this company-level default — direction of override not independently confirmed beyond the search-index summary phrase "can be overridden by setting them on the product category form" |
| Transaction Consumer | Vendor bill posting, customer invoice posting, per the `Perpetual (at invoicing)` label itself |
| Periodic Behavior | `Periodic (at closing)`: purchase invoices post as expenses by nature at time of posting; at closing, the inventory difference is posted back to the Balance Sheet (inventory valuation) — this is a materially more specific description than the `13.0`–`saas-18.4` "manual journal entry" framing, and should not be assumed identical without direct re-verification |
| Perpetual Behavior | `Perpetual (at invoicing)`: vendor bills post as assets (stock valuation) directly; expenses (COGS) are reported when goods are sold; described explicitly as synchronizing "whenever bills are received or invoices created" |
| Account Type Impact | Not fully itemized in the reconstruction; the `Valuation Account` (§3.4) is the asset-side counterpart |
| Financial Statement Impact | Both |
| Change Impact | Not confirmed in this pass |
| Version Delta | New field shape, new location (company-level, not category-gated); see file `02` §4 and §4.1 for the full delta discussion, including the caution against assuming this is a simple rename of §2.1/§2.2 |
| Evidence | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction; direct fetch failed twice); corroborated by Reference ERP official conference/release material on the same architecture change, 2025, retrieved 2026-09-02 |
| Fact Status | `PROVISIONAL, HIGH CONFIDENCE — REQUIRES DIRECT-FETCH RE-VERIFICATION` |

### 3.2 Field: `Periodic Valuation` (cadence sub-setting)

| Requirement | Evidence |
|---|---|
| Menu Path | Same settings page, conditional on `Inventory Valuation` = `Periodic (at closing)` |
| Field Label | `Periodic Valuation` |
| Purpose | Sets automation cadence for the periodic closing-entry process |
| Values / Options | `Manual` / `Daily` / `Monthly` |
| Default | Not confirmed — `HOLD` |
| Visibility | Conditional on `Inventory Valuation` = `Periodic` |
| Scope | Company |
| Inherits From | N/A |
| Override Precedence | Not confirmed whether Product Category or location can override cadence — `HOLD` |
| Transaction Consumer | The closing-entry generation process itself |
| Periodic Behavior | This field only exists under Periodic — it is the automation control for what was, in `13.0`–`saas-18.4`, described only as a manual "accounting team posts journal entries" process with no documented automation cadence option |
| Perpetual Behavior | N/A — field is hidden under Perpetual |
| Account Type Impact | N/A directly — governs timing, not account selection |
| Financial Statement Impact | Timing of BS/P&L recognition under Periodic mode |
| Change Impact | Not confirmed |
| Version Delta | **No documented equivalent found in any version `13.0`–`saas-18.4` directly fetched in this pass.** This is flagged as a new capability, not a renamed one — see file `02` §4.1, trap item 2. |
| Evidence | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction) |
| Fact Status | `PROVISIONAL — REQUIRES DIRECT-FETCH RE-VERIFICATION`; this is the single field in this file most likely to be a search-summarization artifact rather than a literal field name, given it could not be cross-checked against a second independent source in this pass. |

### 3.3 Field: `Inventory Cost Method`

| Requirement | Evidence |
|---|---|
| Menu Path | Same settings page |
| Field Label | `Inventory Cost Method` |
| Purpose | Company-level costing-method default |
| Values / Options | Standard Price / FIFO / AVCO — same three named options as §2.3, per reconstruction |
| Default | Not confirmed — `HOLD` |
| Visibility | Always visible on this page, per reconstruction |
| Scope | Company |
| Inherits From | N/A |
| Override Precedence | Product Category described as able to override, per reconstruction — same caveat as §3.1 |
| Transaction Consumer | Receipt, issue, adjustment — same transaction set as §2.3 |
| Periodic Behavior | Not separately confirmed from §2.3's behavior beyond the scope change |
| Perpetual Behavior | Not separately confirmed from §2.3's behavior beyond the scope change |
| Account Type Impact | Interacts with the Price Difference Account conflict noted in file `02` §7 — this file does not resolve that conflict |
| Financial Statement Impact | Both |
| Change Impact | Not confirmed |
| Version Delta | Category-only in `13.0`–`saas-18.4` (§2.3); company-level-with-category-override in `19.0` reconstruction — material scope delta, see file `02` §5 |
| Evidence | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction) |
| Fact Status | `PROVISIONAL — REQUIRES DIRECT-FETCH RE-VERIFICATION` |

### 3.4 Fields: `Valuation Account`, `Variation Account`, `Journal`

| Requirement | Evidence |
|---|---|
| Menu Path | Same settings page; `Variation Account` reached by clicking through from the `Valuation Account` field per the reconstruction ("open the Stock Valuation account and update the Variation Account") |
| Field Label | `Valuation Account`, `Variation Account`, `Journal` |
| Purpose | `Valuation Account`: company-level default asset account recording physical stock's financial value. `Variation Account`: records the period inventory change, described as an expense-or-asset account "depending on standard" (i.e., depends on Periodic vs. Perpetual / Continental-vs-Anglo-Saxon-style jurisdiction). `Journal`: company-level default journal for posting inventory valuation entries. |
| Values / Options | Free account/journal selection from chart of accounts / journal list |
| Default | Not confirmed — `HOLD` |
| Visibility | Always visible on this page, per reconstruction |
| Scope | Company, with Product Category override described as available (same caveat as §3.1) |
| Inherits From | N/A at company level |
| Override Precedence | Category over company, per reconstruction — direction not independently re-confirmed |
| Transaction Consumer | All automated/periodic-closing postings |
| Periodic Behavior | `Variation Account` is explicitly the mechanism named for periodic-close-entry counterpart posting |
| Perpetual Behavior | `Valuation Account` and `Journal` serve the real-time posting path |
| Account Type Impact | `Variation Account` type varies by accounting standard/mode — directly stated as expense-or-asset "depending on standard," which is itself a caution against assuming a single fixed account type across jurisdictions |
| Financial Statement Impact | Both |
| Change Impact | Not confirmed |
| Version Delta | §2.4's `Stock Valuation Account` / `Stock Journal` were category-scoped in `13.0`–`saas-18.4`; this reconstruction places direct analogs at company scope in `19.0`. `Variation Account` as a **named** field was not confirmed present under that exact name in any version directly fetched in `13.0`–`saas-18.4` in this pass — see file `02` §8. |
| Evidence | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction) |
| Fact Status | `PROVISIONAL — REQUIRES DIRECT-FETCH RE-VERIFICATION` |

### 3.5 Fields: `Inventory Loss` account, `Cost of Production` account (location-scoped)

| Requirement | Evidence |
|---|---|
| Menu Path | Reconstruction states these "can be defined on dedicated locations," implying a stock-location settings surface, not the Accounting Settings page itself — recorded here because they were surfaced by the same source describing Menu A's `19.0` shape, and because they are directly relevant to Menu H (Inventory Loss / Production / Location Accounting Controls) |
| Field Label | `Inventory Loss`, `Cost of Production` |
| Purpose | Loss/shrinkage account and production/WIP cost account, assignable per stock location rather than per category or company |
| Values / Options | Free account selection |
| Default | Not confirmed — `HOLD` |
| Visibility | Not confirmed — `HOLD` |
| Scope | **Location** — a third scope level distinct from company (§3.1–§3.4) and Product Category (§2.3–§2.5, file `04`) |
| Inherits From | Not confirmed |
| Override Precedence | Not confirmed — in particular, not confirmed whether a location-level value overrides or supplements a category-level Expense Account for loss/scrap postings |
| Transaction Consumer | Inventory adjustment (loss), manufacturing consumption (production cost) |
| Periodic Behavior | Not confirmed |
| Perpetual Behavior | Not confirmed |
| Account Type Impact | Loss = likely expense/other-expense type; Production = likely WIP/asset or expense type — neither independently confirmed by direct quote in this pass |
| Financial Statement Impact | Both, direction not confirmed |
| Change Impact | Not confirmed |
| Version Delta | No location-scoped accounting-control field of this kind was identified in any version `13.0`–`saas-18.4` directly fetched in this pass. If accurate, this is a **new scope level**, not merely a new field — flag for files `10` (Menu H) and `22` (Manufacturing) to independently verify before relying on it. |
| Evidence | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction) |
| Fact Status | `PROVISIONAL — REQUIRES DIRECT-FETCH RE-VERIFICATION`; lowest-confidence claim in this file along with §3.2, because it was not corroborated by the conference-source cross-check the way §3.1's architecture claim was. |

---

## 4. Interaction With Product Category (Menu B) — Generic Description

Without assuming file `04`'s content, the structural interaction Menu A has with Product Category, proven by this file's own evidence, is:

1. **`13.0`–`saas-18.4`**: Menu A contributes exactly one thing — a company-wide boolean gate (`Automatic Accounting`) that determines whether the Product-Category-level `Inventory Valuation` field is even visible/usable. Every other field material to valuation and cost recognition (Costing Method, Stock Valuation/Input/Output accounts, Stock Journal, Expense Account, Price Difference Account where present) lives entirely on the Product Category form. Menu A does not supply a default value for any of these; it only unlocks them.
2. **`19.0` (reconstructed, `PROVISIONAL`)**: Menu A instead appears to supply **default values** directly (`Inventory Valuation` mode, `Inventory Cost Method`, `Valuation Account`, `Variation Account`, `Journal`), with Product Category described as able to **override** those defaults on a per-category basis. This is a different inheritance relationship than item 1 — a true default/override pair, rather than a gate/detail pair — and must be independently confirmed by whoever authors or updates file `04`'s `19.0` evidence, since it directly determines what "Inherits From" and "Override Precedence" should say on every Menu B field for that version.
3. In no version examined in this pass did this file find evidence of a **Product-level** (not Category-level — see file `05`, Menu C) override of anything Menu A configures directly. Menu C's Income/Expense Account override (per the governing prompt §6 Menu C description) interacts with Menu B's category defaults, not directly with Menu A.

This file does not resolve `JT-01` (valuation-policy ownership: category/product/warehouse/standalone). It records that the reference ERP itself changed which layer owns the default between the two version ranges studied — evidence relevant to `JT-01`, not a closing argument for it.

---

## 5. Layer C — Candidate Semantics (Neutral, Non-Binding)

Per the governing prompt §3, the following are stated strictly as `CANDIDATE` framings for future Joint Accounting × Inventory discussion, not as SMEsPlus design decisions, and not as an endorsement of the reference ERP's approach:

- `CANDIDATE`: a company-level valuation-timing default with a category-level override point is a *pattern worth evaluating* for SMEsPlus (whichever version range's mechanics turn out true), because it separates "what does our business do by default" from "does this specific product line need an exception" — but which layer should own the default (company, category, warehouse, or a standalone versioned policy) is exactly `JT-01`, unresolved here.
- `CANDIDATE`: the dual-type-by-mode behavior found on the Expense Account field (§2.5) — the same field label expected to hold a Current-Asset-type account under one mode and an Expense/Cost-of-Revenue-type account under another — is a **control risk pattern** worth naming explicitly in any SMEsPlus field design, regardless of whether SMEsPlus adopts a similarly-named single field or two separately-named fields. `HOLD/JOINT` — this is an Accounting × Inventory boundary question (the foundational rule "Inventory emits facts; Accounting decides postings" implies Accounting, not Inventory, should own this account-type resolution logic) and is not decided by this file.
- `HOLD/JOINT`: whether a location-scoped loss/production-cost account concept (§3.5) is appropriate for Thai SME operations is explicitly **not evaluated** in this file — it requires Layer B (Thai) evidence (file `24`) and a Joint decision, and its very existence in the reference ERP is itself only `PROVISIONAL` here.

---

## 6. Fact Status Roll-Up for This File

| Status | Rows |
|---|---|
| `VERIFIED` | §2.1 (presence/label/default/location), §2.2 (visibility gate/default), §2.3 (category-only scope, three-option list), §2.5 (dual account-type-by-mode behavior — directly and consistently stated across multiple directly-fetched versions) |
| `PROVISIONAL` | §2.4 (`Stock Journal` field-name parity pre-`17.0`), §2.6 (per-company scope of the checkbox), all of §3 (`19.0` reconstruction, entire table) |
| `HOLD / EVIDENCE REQUIRED` | Default account pre-population values throughout §2.4/§2.5; `19.0` field defaults throughout §3; location-scope override precedence in §3.5; whether `19.0`'s company/category relationship is a true default/override pair (item 2, §4) |
| `CONFLICTING` | None newly introduced in this file; this file inherits and does not resolve file `02` §7's Price Difference Account conflict |

No field in this file is asserted as a final SMEsPlus design element. §3 in its entirety requires a direct-fetch re-verification pass before any later deliverable in this session treats it as more than provisional evidence.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
