# 02 — Reference Version Behavior Delta Register

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `EVIDENCE ONLY — READ-ONLY DEEP RESEARCH — CP-02, NOT A DESIGN FREEZE`

---

## 1. Purpose and Method

The governing prompt (§5, "Version-delta rule") requires an explicit `REFERENCE_VERSION_BEHAVIOR_DELTA_REGISTER` before any Menu A–H evidence sheet is trusted, because the reference ERP's own public documentation shows the inventory-valuation surface was **not stable** across the versions in scope. A researcher who studied one version and silently carried its vocabulary, field set, or menu path into another version would produce false evidence.

This file compares the reference ERP's own official documentation across nine reference points: `13.0`, `14.0`, `15.0`, `saas-15.3`, `16.0`, `saas-16.4`, `17.0`, `18.0`, `saas-18.4` (the closest publicly documented saas-18.x build reached), and `19.0`. All citations are to the reference ERP's own published documentation, retrieved 2026-09-02, using the citation form required by the governing clean-room rule (no raw URL reproduced — a URL string contains the vendor domain, itself a scrubbed token).

This file is Layer A only (Reference ERP observed behavior). Layer B (Thai evidence) is out of scope for this file — see file `24` of this session. Layer C (SMEsPlus candidate semantics) is not asserted here; nothing in this file is a target-architecture decision.

---

## 2. Version Coverage Table

| Reference Point | Status Observed | Evidence |
|---|---|---|
| `13.0` | Documented, fetched directly | Reference ERP official documentation — Inventory valuation configuration, version 13.0, retrieved 2026-09-02 |
| `14.0` | Documented, fetched directly | Reference ERP official documentation — Inventory valuation configuration, version 14.0, retrieved 2026-09-02 |
| `15.0` | Documented, located via search index, content summary only (not a full direct-fetch pass) | Reference ERP official documentation — Inventory valuation configuration, version 15.0, retrieved 2026-09-02 — `FACT STATUS: PROVISIONAL` pending a full direct-fetch re-pass |
| `saas-15.3` | Documented, fetched directly | Reference ERP official documentation — Inventory valuation configuration, version saas-15.3, retrieved 2026-09-02 |
| `16.0` | Documentation page exists at a different path than 15.x (see §3.1); content triangulated from search index and community/forum secondary sources, not a full direct-fetch pass | Reference ERP official documentation — Automatic inventory valuation, version 16.0, retrieved 2026-09-02 — `FACT STATUS: PROVISIONAL` |
| `saas-16.4` | Documented, fetched directly | Reference ERP official documentation — Inventory valuation configuration, version saas-16.4, retrieved 2026-09-02 |
| `17.0` | Documented, fetched directly (two live doc paths co-exist for this version — see §3.1) | Reference ERP official documentation — Automatic inventory valuation, version 17.0, retrieved 2026-09-02 |
| `18.0` | Documented, fetched directly | Reference ERP official documentation — Automatic inventory valuation, version 18.0, retrieved 2026-09-02 |
| `saas-18.4` | Documented, fetched directly | Reference ERP official documentation — Automatic inventory valuation, version saas-18.4, retrieved 2026-09-02 |
| `19.0` | Documentation exists under a **new information architecture** (a Finance/Accounting-side page distinct from the Inventory-app-side page — see §3.1); direct fetch of the Finance/Accounting page failed twice (tool returned an empty-content error on both attempts); content below is reconstructed from search-index snippets of that same official page plus a corroborating official reference-ERP conference/release-notes source and one direct fetch of the companion Inventory-app cheat-sheet page | Reference ERP official documentation — Inventory valuation, version 19.0, retrieved 2026-09-02 (search-index reconstruction — direct fetch failed); Reference ERP official documentation — Valuation cheat sheet, version 19.0, retrieved 2026-09-02 (direct fetch succeeded); Reference ERP official conference/release material — "stock valuation" architecture session, 2025, retrieved 2026-09-02 — `FACT STATUS: PROVISIONAL, HIGH CONFIDENCE (three independent sources converge), REQUIRES ONE DIRECT-FETCH RE-VERIFICATION PASS BEFORE ANY DOWNSTREAM FILE TREATS IT AS VERIFIED` |

**Historical SMEsPlus learning baseline**: per prior session record, SMEsPlus's own historical learning pass used an "Automatic / Manual" valuation vocabulary consistent with the 13.0–saas-18.4 architecture described below. Per the governing prompt's explicit instruction, this file records that the `19.0` reference point uses a **materially different** vocabulary and field set, and this must not be silently carried forward, and the old vocabulary must not be silently carried backward onto `19.0` evidence either.

---

## 3. Delta Register — Inventory Valuation Configuration Location and Naming

### 3.1 Menu / documentation path evolution

| Version | Documentation path segment (Inventory-app side) | Observed page title |
|---|---|---|
| `13.0` | `inventory/management/reporting/` | "Inventory valuation configuration" |
| `14.0` | `inventory/management/reporting/` | "Inventory valuation configuration" |
| `15.0` | `inventory/management/reporting/` | "Inventory valuation configuration" |
| `saas-15.3` | `inventory/management/reporting/` | "Inventory valuation configuration" |
| `16.0` | `inventory/product_management/inventory_valuation/` | "Automatic inventory valuation" (title changed from "configuration" framing) |
| `saas-16.4` | `inventory/warehouses_storage/inventory_valuation/` | "Inventory valuation configuration" |
| `17.0` | **Two concurrently live paths observed**: `inventory/management/reporting/` (older path, still resolving) **and** `inventory/warehouses_storage/inventory_valuation/` **and** `inventory/product_management/inventory_valuation/` | "Inventory valuation configuration" / "Automatic inventory valuation" (title varies by path) |
| `18.0` | `inventory/product_management/inventory_valuation/` | "Automatic inventory valuation" |
| `saas-18.4` | `inventory/product_management/inventory_valuation/` | "Automatic inventory valuation" |
| `19.0` | `inventory/product_management/inventory_valuation/` (Inventory-app cheat sheet) **plus a new, separate** `finance/accounting/get_started/inventory_valuation.html` (Finance/Accounting-app side) | "Valuation cheat sheet" (Inventory side) / "Inventory valuation" (new Finance/Accounting side page) |

**Fact Status: VERIFIED** for `13.0`, `14.0`, `saas-15.3`, `saas-16.4`, `17.0`, `18.0`, `saas-18.4` (direct fetch or direct search-index path listing). **PROVISIONAL** for `15.0` and `16.0` path (search-index only). **PROVISIONAL, high confidence** for the `19.0` new Finance/Accounting page's existence and title (search-index snippets plus one corroborating conference source all agree it exists and covers company-level settings; the page itself could not be directly re-fetched a second time in this pass).

### 3.2 Naive-researcher trap — path/version mismatch

`HOLD / EVIDENCE REQUIRED — DO NOT CARRY FORWARD`: because the path segment changed at least three times (`management/reporting` → `product_management/inventory_valuation` → `warehouses_storage/inventory_valuation` → back to `product_management/inventory_valuation` → a *second, new* `finance/accounting/get_started` page in `19.0`), a researcher who bookmarks or hard-codes one version's path and reuses it against a different version will either 404 or land on an unrelated/superseded page. Any future SMEsPlus evidence file that cites a reference-ERP documentation path must state the exact version alongside it; a path with no version qualifier is not admissible evidence under this session's clean-room rule.

---

## 4. Delta Register — Periodic vs Perpetual Terminology and Default

| Version | Vocabulary used for the two valuation-timing modes | Where the choice lives | Observed/implied default |
|---|---|---|---|
| `13.0` | "Manual" vs "Automated" inventory valuation (Inventory-app framing); "Continental" vs "Anglo-Saxon" (accounting-mode framing, tied to the fiscal localization / chart of accounts installed) | Product Category field `Inventory Valuation` (Manual / Automated); accounting mode is a property of the installed fiscal localization, not a direct user-facing toggle on this page | Manual / Continental-compatible framing documented as default narrative starting point (not a single explicit "default value" statement captured in this pass — `PROVISIONAL`) |
| `14.0` | Same as `13.0`: "periodic inventory valuation (manual)" is described as default; "automated" as the alternative | Same | "Periodic inventory valuation (manual)" stated as default — `VERIFIED` for this version's page |
| `15.0` | Same framing as `14.0` | Same | Same — `PROVISIONAL` (search-index only) |
| `saas-15.3` | Same "Manual" / "Automated" framing, same Continental/Anglo-Saxon accounting-mode framing | Same | Manual described as default — `VERIFIED` |
| `16.0` | Same "Manual" / "Automated" framing at the Inventory-app page | Same | Not independently re-confirmed this pass — carried from adjacent versions — `PROVISIONAL` |
| `saas-16.4` | Same "Manual" (periodic) / "Automated" framing | Same | Manual/Standard Price described as default — `VERIFIED` |
| `17.0` | Same "Manual" / "Automated" framing | Same | Same — `VERIFIED` |
| `18.0` | Same "Manual (periodic)" / "Automated (perpetual)" framing — this is the first version in this pass where the reference documentation explicitly glosses "Automatic = perpetual" and "Manual = periodic" as parenthetical synonyms rather than only using Manual/Automated | Same | Manual described as default; costing method default Standard Price — `VERIFIED` |
| `saas-18.4` | Same as `18.0` | Same; `Automatic Accounting` checkbox is the sole company-level control, gating visibility of the Product-Category-level `Inventory Valuation` field | Manual described as default — `VERIFIED` |
| `19.0` | **New primary vocabulary**: `Inventory Valuation` field with two named options, `Perpetual (at invoicing)` and `Periodic (at closing)` — now presented as the primary, explicit terms, directly on the Accounting-Settings company-level page, not only as a Product-Category attribute or a parenthetical gloss | `Accounting → Configuration → Settings → Inventory Accounting` (company-level; new "Inventory Accounting" settings section name observed) | Default not independently confirmed with a directly-quoted default statement in this pass — `HOLD / EVIDENCE REQUIRED`. Narrative association observed: `Perpetual (at invoicing)` is described as best practice for "Anglo-Saxon" jurisdictions (examples cited: USA, India); `Periodic (at closing)` is described as best practice for Europe — this mirrors the pre-19.0 Continental/Anglo-Saxon narrative but is not confirmed to be literally the same field or the same default-selection mechanism |

### 4.1 Naive-researcher trap — "Manual/Automated" is not simply renamed to "Periodic/Perpetual"

`HOLD / EVIDENCE REQUIRED — MATERIAL, DO NOT SILENTLY MAP`: the surface reading — "Manual was renamed Periodic, Automated was renamed Perpetual" — is not confirmed and is very likely an oversimplification. Two structural differences were observed between the pre-19.0 and 19.0 framings that a 1:1 rename mapping would hide:

1. Pre-`19.0`: the company-level Accounting Settings control is a single boolean (`Automatic Accounting` checkbox) that only **unlocks visibility** of a Product-Category-level field; the actual valuation-timing choice is made per Product Category, not per company.
2. `19.0` (as reconstructed, `PROVISIONAL`): the company-level Accounting Settings page carries the `Inventory Valuation` (`Perpetual`/`Periodic`) choice directly, plus a **new** `Periodic Valuation` cadence sub-field (`Manual` / `Daily` / `Monthly`) that has no documented equivalent before `19.0`, plus a company-level `Inventory Cost Method` field and a company-level `Valuation Account` field that, in `13.0`–`saas-18.4`, exist only at Product Category scope. Product Category is described (in the `19.0` search-index reconstruction) as able to **override** these new company-level defaults — i.e., the inheritance direction is the reverse of a simple rename: `19.0` appears to introduce a company-level default with category-level override, where earlier versions had category-level-only fields gated by a company-level boolean.

This delta is material to `JT-01` (valuation-policy ownership: category/product/warehouse/standalone) and must not be assumed resolved by this file. It is flagged here as evidence, not decided.

### 4.2 Naive-researcher trap — Continental/Anglo-Saxon vs Perpetual/Periodic are evidenced as related, not proven identical

Every version in `13.0`–`saas-18.4` ties the accounting-entry timing narrative to "Continental" and "Anglo-Saxon" accounting-mode language, which the reference ERP's own documentation ties to the installed fiscal localization (i.e., the country-specific chart of accounts a company runs). The `19.0` reconstruction ties `Periodic`/`Perpetual` to the same two-jurisdiction narrative (Europe vs. USA/India) but this session did not obtain a directly-quoted statement proving `Perpetual (at invoicing)` is mechanically the exact same switch as the old "Anglo-Saxon accounting mode," or that the mechanism for setting the default (fiscal localization / country pack, vs. a plain user-settable field) is unchanged. Treat as `PROVISIONAL — REQUIRES DIRECT VERIFICATION` before any COGS scenario file (`16`) asserts a particular version's default without checking it per-version.

---

## 5. Delta Register — Costing Method Options

| Version | Costing Method options observed | Scope where the field lives |
|---|---|---|
| `13.0` | Standard Price; Average Price (AVCO); FIFO | Product Category only |
| `14.0`–`saas-18.4` | Same three options, consistently: Standard Price; Average Cost (AVCO); First In First Out (FIFO) | Product Category only, in every version directly fetched in this pass |
| `19.0` | Same three named options, but the field is reconstructed as also present at company level as `Inventory Cost Method`, in addition to (or as default for) the Product Category field | Company level (new, `PROVISIONAL`) **and** Product Category level (category "can override," per the `19.0` reconstruction) |

No version in this pass documented a fourth selectable costing method (e.g., Specific Identification) as a UI option anywhere `13.0`–`19.0`. This matches the governing prompt's own framing (§9) that Specific Identification is a business/authoritative requirement to evaluate on its own merits, not something to expect as a reference-UI option — its absence here is not evidence that it is inappropriate for SMEsPlus, only that the reference ERP does not offer it as a selectable method in the versions checked.

**Fact Status**: `VERIFIED` for the three-option list across all directly-fetched versions. `PROVISIONAL` for the `19.0` company-level placement (same caveat as §4).

---

## 6. Delta Register — Product Category Accounting Fields

This session's file `04` (Menu B) owns the full field register; this file records only the version-delta shape so file `03` (Menu A) can describe the interaction correctly without duplicating file `04`'s content.

| Version | Fields observed on the Product Category form (Account Properties / Inventory Valuation section) |
|---|---|
| `13.0` | Stock Valuation Account; Stock Input Account; Stock Output Account; Expense Account; Income Account; Costing Method; Inventory Valuation (Manual/Automated) |
| `14.0`–`15.0` | Same set as `13.0` (no delta identified in this pass) |
| `saas-15.3` | Same set as `13.0`, **plus** a distinct Price Difference Account field observed as still present at this point (see §7) |
| `16.0` | Same core set, **minus** the Price Difference Account as a standing Product Category field (see §7 — materially changed, not merely renamed) |
| `saas-16.4`–`saas-18.4` | Stock Valuation Account; Stock Journal; Stock Input Account; Stock Output Account; Expense Account (used by both Manual and Automated modes); Income Account; a Price Difference Account field is again documented as present in this range, but its behavior is scoped to Standard Price costing only (see §7 — this is a second, distinct delta from the `16.0` change) |
| `19.0` | Reconstruction indicates the same category-level fields persist but now sit alongside new company-level defaults (§4.1); this session did not obtain full field-by-field confirmation for `19.0` category-level fields and defers entirely to file `04`'s own version pass |

---

## 7. Delta Register — Price Difference Account (high-materiality delta)

This is the single most consequential naming/behavior delta identified in this pass, because a researcher who studied only `saas-15.3` or only `saas-16.4`/`18.0` would draw opposite conclusions about whether a "Price Difference Account" field still exists and what it does.

| Version | Observed state |
|---|---|
| `saas-15.3` and earlier (`13.0`–`15.0`) | Price Difference Account exists as a standing field concept associated with Standard Price costing under Automated/perpetual-style valuation. |
| `16.0` | Community/forum secondary evidence (not the primary documentation page itself in this pass) reports the Price Difference Account was **removed as a distinct Product Category field**. Behavior changed by costing method: for AVCO and FIFO, the reference system is reported to automatically re-value inventory cost to the vendor-bill price directly, with no separate account; for Standard Price, price variance is reported to route through the Stock Interim (Received) account, landing in the "residual" field of a journal item rather than a dedicated account. **`FACT STATUS: PROVISIONAL — SECONDARY/COMMUNITY SOURCE, NOT THE PRIMARY DOCUMENTATION PAGE ITSELF; REQUIRES A DIRECT PRIMARY-DOCUMENTATION FETCH BEFORE TREATING AS VERIFIED.`** |
| `17.0`–`saas-18.4` | The primary documentation for these versions again lists a `Price Difference Account` field on the Product Category form, described in the officially-fetched `18.0` page as relevant "for FIFO/AVCO cost adjustments." This appears to **conflict** with the `16.0` community evidence above (which says Price Difference Account works with Standard Price only, not AVCO/FIFO). A separate secondary source states explicitly that "the price difference account will only work with 'Standard price' (automated and costing method)," directly contradicting the `18.0` primary-page summary's "FIFO/AVCO" framing captured in this pass. |
| `19.0` | Not independently confirmed in this pass; the field may or may not persist given the broader architecture change described in §4.1 (valuation reportedly no longer tracked in separate valuation-layer records but stored directly on stock moves). |

**Fact Status: `CONFLICTING`.** This file records the conflict rather than resolving it. Two named sources disagree on whether Price Difference Account applies to Standard Price only, or extends to FIFO/AVCO, in the `16.0`–`saas-18.4` range. `HOLD / EVIDENCE REQUIRED` before any COGS scenario file (particularly scenario 6 — "vendor bill price differs from receipt/valuation basis," file `16`) asserts a specific version's Price Difference Account behavior without a direct primary-documentation re-fetch for that exact version.

### 7.1 Naive-researcher trap

Do not read one version's Price Difference Account behavior (e.g., `18.0`'s) and assume it describes `saas-15.3` or `16.0` — the field was reported **removed then reintroduced** with a **narrower** reported scope across this range, and the reintroduced description is itself internally disputed between the primary-page summary and secondary community evidence obtained in this pass.

---

## 8. Delta Register — Stock/Valuation/Variation Account Concepts

| Concept | Pre-`19.0` framing | `19.0` framing (reconstructed) |
|---|---|---|
| Asset account holding current stock value | "Stock Valuation Account" — Product Category scope only | "Valuation Account" — company scope (Accounting Settings), described as overridable at Product Category |
| Counterpart for stock movements | "Stock Input Account" / "Stock Output Account" — Product Category scope, used only when Automated | Not independently confirmed whether Input/Output account pair persists unchanged at `19.0`; `HOLD / EVIDENCE REQUIRED` |
| Period-variance/expense-side counterpart under Continental-style/Periodic accounting | Not named "Variation Account" consistently across `13.0`–`saas-18.4`'s Inventory-app pages in this pass — the concept appears mainly under "Stock Variation" narrative language in the Continental/Anglo-Saxon comparison text rather than as a single standing account field name | "Variation Account" — named field, reachable by clicking through from the company-level Valuation Account field, per the `19.0` reconstruction |
| Journal used for automatic postings | "Stock Journal" — Product Category scope | "Journal" — company scope (Accounting Settings), per the `19.0` reconstruction |
| Loss / shrinkage account | Not confirmed as a standing named field in `13.0`–`saas-18.4` pages fetched this pass | "Inventory Loss" account — described as definable per stock **location**, not per category or company, per the `19.0` reconstruction |
| Production/WIP cost account | Not confirmed as a standing named field in `13.0`–`saas-18.4` pages fetched this pass | "Cost of Production" account — also described as definable per stock **location**, per the `19.0` reconstruction |

**Fact Status**: pre-`19.0` rows are `VERIFIED` where a version was directly fetched (see §2), `PROVISIONAL` otherwise. All `19.0` rows are `PROVISIONAL` (reconstruction, not a successful direct fetch of the primary page) and are flagged for a mandatory re-verification pass before any downstream file (`06`, `08`, `10`) treats the location-scoped Inventory Loss / Cost of Production account claim as settled fact — this is a materially new scope (location-level, not category-level) that would be easy to miss if a researcher only knew the pre-`19.0` architecture.

---

## 9. Delta Register — Landed Cost Feature Maturity

| Version | Documentation path observed | Feature-maturity delta observed |
|---|---|---|
| `14.0` | `inventory/management/reporting/integrating_landed_costs.html` | Baseline documented feature; earliest version independently located in this pass. Absence of documentation before `14.0` is not evidence the feature did not exist earlier — `HOLD / EVIDENCE REQUIRED` on pre-`14.0` state. |
| `16.0` | `inventory/product_management/inventory_valuation/integrating_landed_costs.html` | Path relocated; no functional-maturity delta independently confirmed in this pass beyond the relocation itself. |
| `17.0` | `inventory/warehouses_storage/inventory_valuation/integrating_landed_costs.html` | Path relocated again (same relocation pattern as §3.1's general Inventory Valuation page). |
| `18.0` | `inventory/product_management/inventory_valuation/landed_costs.html` | Page renamed from "Integrating additional costs to products (landed costs)" framing to a plain "Landed costs" title; path segment reverted toward the `16.0` pattern. |
| `19.0` | `inventory/inventory_valuation/landed_costs.html` | Path simplified again, dropping the `product_management`/`warehouses_storage` segment entirely, consistent with the broader `19.0` reorganization noted in §3.1 and §4.1. |

No claim is made in this pass about a change to the landed-cost *allocation methodology itself* (e.g., by-quantity/by-weight/by-volume/by-value splitting rules) across these versions — that is out of this file's scope and belongs to file `21` (Landed Cost / Late Cost / Price Difference research), which must run its own direct-fetch pass rather than relying on this register's path-tracking only.

---

## 10. Delta Register — Inventory Valuation Reporting

Full treatment belongs to file `07` (Menu E). This register records only the version-boundary risk: the reporting page's own path followed the same `management/reporting` → `product_management`/`warehouses_storage` → `19.0` reorganization pattern documented in §3.1, and the `19.0` architecture note in §4.1 — "valuation is no longer tracked in separate valuation layer records... stored directly on stock moves" and a "dedicated Stock menu showing valuation with details of all contributing moves" — describes a materially different underlying reporting mechanism, not only a relabeled screen. `HOLD / EVIDENCE REQUIRED` — file `07` must independently verify whether pre-`19.0` valuation-layer/drill-down provenance concepts (individual valuation layer records tied to each stock move) map cleanly onto the `19.0` model, or whether history/audit-trail behavior differs. This register does not assume they are equivalent.

---

## 11. Summary — Naive-Researcher Traps Flagged in This File

1. Hard-coding a documentation path without a version qualifier (§3.2).
2. Treating "Manual/Automated" as a plain rename of "Periodic/Perpetual" instead of a structurally different company-vs-category ownership model (§4.1).
3. Treating "Anglo-Saxon/Continental" and "Perpetual/Periodic" as proven mechanically identical rather than merely narratively parallel (§4.2).
4. Assuming Costing Method is category-only in `19.0` because it was category-only in `13.0`–`saas-18.4` (§5).
5. Reading one version's Price Difference Account behavior and assuming it applies to a different version — this field was reported removed, then reintroduced with disputed scope (§7, §7.1).
6. Assuming Inventory Loss / Cost of Production accounts are category-scoped in `19.0` because no earlier version in this pass documented a category-scoped equivalent — the `19.0` reconstruction places them at **location** scope, a third scope level not seen in earlier versions (§8).
7. Assuming landed-cost documentation-path stability implies allocation-methodology stability (§9).
8. Assuming valuation-report drill-down/provenance mechanics are unchanged into `19.0` given the reported removal of separate valuation-layer records (§10).

---

## 12. Fact Status Roll-Up

| Status | Count of register rows/claims |
|---|---|
| `VERIFIED` (direct fetch, this pass) | Majority of `13.0`, `14.0`, `saas-15.3`, `saas-16.4`, `17.0`, `18.0`, `saas-18.4` rows in §3–§6, §8 |
| `PROVISIONAL` (search-index or secondary/community source, not a direct primary fetch in this pass) | All `15.0` and `16.0` specific-behavior rows; all `19.0` rows without exception |
| `CONFLICTING` | Price Difference Account scope in the `16.0`–`saas-18.4` range (§7) |
| `HOLD / EVIDENCE REQUIRED` | Pre-`14.0` landed cost state; `19.0` default value for `Inventory Valuation`; `19.0` Stock Input/Output account persistence; pre-`19.0` explicit "Variation Account" field-name confirmation |

No claim in this file is asserted as a SMEsPlus target-design fact. This is Layer A evidence only.

---

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
