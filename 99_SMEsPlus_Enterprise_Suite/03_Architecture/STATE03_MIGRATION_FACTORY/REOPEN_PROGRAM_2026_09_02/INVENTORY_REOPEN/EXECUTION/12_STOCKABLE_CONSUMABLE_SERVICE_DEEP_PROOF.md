# Inventory Full Reopen — Stockable / Consumable / Service Routing Deep Proof

## Evidence & Governance

| Field | Content |
|---|---|
| Document | `12_STOCKABLE_CONSUMABLE_SERVICE_DEEP_PROOF.md` |
| Session | `SMEPLUS-26-09-02-INV-REOPEN-001` |
| Jira | `ERPPLUS-139` |
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Canonical Branch | `SMEsPlus` |
| Execution Worktree | `INVENTORY_REOPEN_2026_09_02_EXECUTION` |
| Control Level | `/L999.999` |
| Track | `ROUTING — Stockable/Consumable/Service Routing Deep Proof` |
| Fingerprint | `INV-FP-13` (prior status entering this pass: `UNKNOWN — STILL MATERIAL`) |
| Role | `target_hypothesis_research` — a single, independent research pass testing Boss's routing hypothesis against source, live data, and external evidence |
| Research Verdict (as submitted) | `CONTINUE_WITH_NOTES` |
| Gate Status | **NOT A GATE PASS.** No Gate decision is made, recommended as final, or implied anywhere in this document. |
| Authorization Status | **Team B, Team C, and Development remain unauthorized.** Nothing in this document authorizes them, in whole or in part, to begin design or build work on the strength of this research. |
| Status | `TARGET HYPOTHESIS RESEARCH COMPLETE — FOR BOSS GATE DECISION ONLY` |

> **This document does not close, pass, approve, or authorize anything.** It is a challenge/investigation finding produced to resolve fingerprint `INV-FP-13` for Boss's eventual Gate decision. It tests Boss's own Stockable/Consumable/Service routing hypothesis against the reference system's source code, a real read-only extraction from the reference system's live data, Thai regulatory and accounting-standard sources, and one independent Thai SME-software comparator. Where the hypothesis is supported, that is stated with its evidence. Where it is only partially supported, the gap is named explicitly rather than smoothed over. Nothing in this document proposes SMEsPlus's own target schema, field names, or workflow design, and nothing in this document authorizes Team B design, Team C handoff, or Development to proceed.

---

## 1. Scope, Fingerprint, and Method

This document answers the one item the CP-01/CP-02 prior-evidence fingerprint index classified `UNKNOWN — STILL MATERIAL`: **INV-FP-13**, whether Boss's target-design hypothesis that SMEsPlus product/item routing should split into three buckets — Stockable, Consumable, and Service — is a sound, evidence-backed foundation for Team B's eventual design work.

No prior pass in this program's evidence chain (R01, DR-002, CORR-004/005/006/007A/007B, IDR-006/007, IER-003) directly tested this hypothesis. DR-002's own Track A5 (`A5_WAREHOUSE_LOCATION_PRODUCT_UOM_TRACEABILITY.md`) documented the *reference system's* own `type`/`is_storable` gating chain as a fact of that system's source code, but did not test it against Boss's three-way hypothesis, against Thai business or regulatory reality, or against real row-level data. This pass does both, and goes one step further than any prior pass could: it reads real, live data from the reference dump rather than source code alone.

**Sources drawn on for this pass:**

1. The DR-002 evidence chain, including Tracks A5, A9, A16, A17, and A18, and the open register items GRPA-M13, GRPA-M14, SAAS-07, N-A5-02, and N-A12-01 carried forward from IDR-007's disposition.
2. Direct, read-only reading of the reference Odoo-family source tree at the project's already-authorized local root — specifically the `product`, `stock`, `stock_account`, `sale_stock`, `purchase_stock`, `mrp`, `sale_mrp`, `repair`, `sale_service`, `sale_project`, `product_expiry`, and `l10n_account_withholding_tax` modules.
3. The project's own schema-level dump catalogs (`Evidence_CSV/Dump_*_Inventory.csv`, `ORM_Field_Inventory_and_DB_Mapping.csv`).
4. A new, narrow, read-only extraction of real row-level data from two tables of the reference PostgreSQL dump `iTEST02_2026-06-14_14-41-19.dump`, made possible because this session's environment happened to already have PostgreSQL 18 client tooling installed alongside the older 16.15 default — an environment-configuration fact, not a methodological advance, and one that let this pass do something DR-002's own Track A2 explicitly could not (A2 recorded that its restore attempt failed under that session's environment and was correctly registered `EVIDENCE_MISSING — ENVIRONMENTAL, NOT SOURCE, LIMITATION`).
5. Public, external sources on Thai withholding-tax practice, official Thai accounting-standard guidance on consumable materials versus inventory, and one independent Thai SME accounting-software vendor's own public product documentation.

Every claim below is labeled by its evidence source. Nothing in this document is invented, and no claim is carried forward from memory rather than a cited source.

---

## 2. Boss's Routing Hypothesis, As Stated

The hypothesis under test, as framed for this mandate, is:

> **Stockable / Inventory-managed** → Inventory Stock Truth applies.
> **Consumable** → no stock ledger *by default*; an Accounting effect may still apply.
> **Service** → no stock ledger; an Accounting effect may still apply.

| Leg | Stock ledger | Accounting effect | Hedge in Boss's own phrasing |
|---|---|---|---|
| Stockable / Inventory-managed | Full Inventory Stock Truth applies | Valuation-driven, per Inventory's own posting rules | none |
| Consumable | No stock ledger, **by default** | May apply | explicitly hedged ("by default") |
| Service | No stock ledger | May apply | **not** hedged |

That asymmetry — Consumable is hedged with "by default," Service is stated flatly — is not a drafting accident this research can ignore. It turns out to matter: §4.5 and §11 below show that real reference data contains cases where the "no stock ledger" rule is in fact overridden for Service, not only for Consumable. This document treats that asymmetry as a live finding, not a footnote.

---

## 3. Research Findings — Source Evidence (Reference System Code and Live Data)

### 3.1 The gating chain, reconfirmed and extended

DR-002's Track A5 (commit `d69da79`) already established the headline fact: `product.template.type` is a required Selection field with exactly three values — `consu` ("Goods"), `service` ("Service"), and `combo` ("Combo") — and `is_storable` is a separate boolean, added by the `stock` module, whose compute forces it to `False` whenever `type != 'consu'`. Reading the primary source directly for this pass confirms and sharpens every part of that claim.

`product/models/product_template.py:54-65` carries the field's own help text, which states the vendor's underlying business rule in plain English: *"Goods are tangible materials and merchandise you provide. A service is a non-material product you provide."* The default value is `consu`. Separately, `stock/models/product.py:821-823` labels `is_storable` **"Track Inventory"**, with help text reading *"A storable product is a product for which you manage stock"* — language that maps almost verbatim onto Boss's own "Stockable / Inventory-managed" phrasing. Its default value is **`False`**, not `True`: a Goods-type item does not become storable automatically. Someone — a user, an onboarding default, or a country-localization module — has to turn it on.

The actual compute body, at `stock/models/product.py:893-895`, is `self.filtered(lambda t: t.type != 'consu' and t.is_storable).is_storable = False`. This is a **one-directional clamp**, not a two-way function of `type`: it only ever forces `is_storable` back to `False` when `type` has just changed away from `consu` while `is_storable` was `True`. It never forces `is_storable` to `True` for `consu` items, and — critically, per §3.5 below — it does not prevent `is_storable` from being `True` on a row whose `type` is already `service` and was never changed through this compute's own trigger path. This is a materially more precise characterization than a flat "is_storable is settable only when type=='consu'," and real data (§3.5) proves the enforcement is not airtight.

Three independent gating points cited in DR-002's Track A5 were re-verified directly against source for this pass, and all three still hold: `sale_stock`'s `_action_launch_stock_rule()` creates a stock move only when `product.type == 'consu'`; `stock.move._should_bypass_reservation()` skips quant reservation when `not product.is_storable`; and `stock_account`'s `_should_create_account_move()` requires both `is_storable == True` **and** `product.valuation == 'real_time'` before any valuation journal entry is created.

One further data point on the pattern of country-specific overrides: `l10n_ke_edi_oscu/models/product.py:65` (Kenya's e-invoicing/OSCU localization) forces `is_storable=True` for all `consu`-type products, to satisfy that country's own regulatory stock-tracking requirement — a real precedent, in this same codebase family, for a country localization overriding the default. No equivalent override was found in `l10n_th` or `l10n_th_reports`; both were checked directly and touch only chart-of-accounts, bank, partner, and tax-template concerns (`account_move.py`, `res_bank.py`, `res_partner.py`, `template_th.py`), never `type` or `is_storable`. This is stated as an observed fact, not a recommendation: the *pattern* of a country forcing storable status by regulation exists in this codebase family; no evidence was found that Thailand's own localization currently does so.

### 3.2 Combo and Kit are two different bundle mechanisms, and neither is a fourth routing bucket

This is the clearest illustration of why the source system's own model does not map cleanly onto a three-way selector, and the source contains two different bundling concepts that must not be confused with each other or folded into the routing question.

**Combo** (`product.template.type == 'combo'`) is a Sales/POS construct. The model's own `_prepare_tooltip()` method states plainly: *"Combos allow to choose one product amongst a selection of choices per category"* — the familiar "meal deal, pick one of these" pattern. `_onchange_type()` forces `purchase_ok = False` when a product's type is set to `combo` (a combo cannot itself be purchased) and raises a `UserError` if the product already carries variant attributes. A combo product is never itself stock-moved: its `combo_ids` resolve, through `combo_item_ids`, to the actual constituent products, each carrying its **own** `type` and `is_storable`, and it is those constituent items — not the combo wrapper — that determine what actually gets reserved, delivered, and valued. In the real 83,753-row dataset examined in §3.5, **zero rows carry `type='combo'`** — the mechanism exists in the schema but is unused in this business's real catalog.

**Kit** is a wholly separate mechanism. `mrp/models/mrp_bom.py:29` defines a Bill-of-Materials `type` Selection value `('phantom', 'Kit')`. A BOM marked `phantom` causes `sale_mrp`'s models (`sale_order_line.py`, `stock_move.py`, `stock_move_line.py`) to redirect the sales/delivery flow to create stock moves for the kit's **component** products rather than the parent product itself, filtered on `bom_type='phantom'` throughout. The parent "kit" product is an ordinary `type='consu'` product with its own `is_storable` value; "Kit" is a BOM-level flag, not a product-classification value at all.

**Finding, stated per this mandate's own instruction**: the source system does not have a field whose three values are "Stockable/Consumable/Service." It has a two-axis structure (`type` crossed with `is_storable`), plus two additional, orthogonal bundling mechanisms that resolve to their components rather than participating in classification themselves. Reconstructing Boss's three-way split from this source requires an explicit **derivation** — `type=consu & is_storable=True → Stockable`; `type=consu & is_storable=False → Consumable`; `type=service → Service` — that the source itself does not perform, and Combo/Kit do not enter into that derivation at all; they must be resolved to their constituent items first. DR-002's Track A17 already flagged this exact two-field shape for quarantine from Team B's own design work; this pass's new evidence — the 989-row contradiction in §3.5, the Combo/Kit non-fit here, the `service_type`/`service_tracking` heterogeneity in §3.3, and the confirmed absence of any database-level enforcement — makes the case for that quarantine stronger, not weaker.

### 3.3 Service is not one uniform behavior

`product_template.py:71-80` shows that the base `product` module's own `service_tracking` Selection field has exactly one value: `('no', 'Nothing')`. The richer set of options this reference system family is known for — create a task, create a project, bill by timesheet, bill by milestone, and so on — does not live in the base model at all. It is contributed independently by at least eight separate extension modules, confirmed via the project's own ORM/DB mapping catalog: `sale`, `sale_project`, `sale_timesheet`, `website_sale_slides`, `event_product`, `event_booth_sale`, `repair`, and `partnership` each add their own `service_type`/`service_tracking` options or logic. None of this heterogeneity affects Inventory's own stock ledger — Service items never touch `stock.quant` or `stock.move` regardless of `service_type`/`service_tracking`, because those sub-fields never influence `is_storable` — but it does mean "Service → no stock ledger" is the *only* part of Boss's hypothesis that holds uniformly across the whole Service bucket. Everything about *how* a service is billed and fulfilled varies underneath that single label, and that variation is real and sourced, even though it will matter more to Sales/Accounting invoicing-timing design than to Inventory's own ledger question.

This section also resolves an item that had remained open across two prior evidence passes. **GRPA-M13** asked for the owning module of `sale_order_line.is_service`. This pass located it directly: `sale_service/models/sale_order_line.py:17,36-40` defines `is_service = fields.Boolean("Is a Service", compute='_compute_is_service', store=True, ...)`, with a compute body that reduces exactly to `so_line.is_service = so_line.product_id.type == 'service'`. A dedicated partial index (`WHERE is_service IS TRUE`) exists purely for query performance. **GRPA-M13 is resolved**: `is_service` is a pure, redundant, computed mirror of `product.type`, carrying no independent business semantics — a target migration or design does not need to treat it as a separate signal.

### 3.4 Repair orders: a concrete "service that consumes stock" mechanism

`repair/models/repair.py` defines `repair.order` with a real `move_ids` field — a One2many to `stock.move`, filtered on `repair_line_type` in (`'add'`, `'remove'`). These are ordinary `stock.move` records: they get reserved (`_action_assign`), confirmed (`_action_confirm`), and completed through the same state machine as any other Inventory move, carrying `lot_id` when the repaired item or its parts are lot- or serial-tracked. Separately, `action_create_sale_order()` converts the repair into invoiceable sale-order lines, with the labor/service component billed through an ordinary `type='service'` product on that same sale order. One document, two routing buckets, simultaneously, at the line-item level — the concrete, source-confirmed instance of the "services that consume stock" edge case this mandate asked about.

### 3.5 Live dump evidence: theory versus real data

This is the new evidence this pass contributes beyond anything in the prior chain. DR-002's own Track A2 recorded, honestly, that its restore attempt against the reference dump (`iTEST02_2026-06-14_14-41-19.dump`, a PostgreSQL-18-class custom-format archive) failed under that session's environment — the locally available `pg_restore` 16.15 could not read a v1.16 archive header, and a Docker-based workaround was blocked by that session's own permission classifier — and this was correctly registered as `EVIDENCE_MISSING — ENVIRONMENTAL, NOT SOURCE, LIMITATION`. This session's environment happened to already have PostgreSQL 18 client tools installed via Homebrew alongside the older default, which let this pass do something DR-002 explicitly could not: extract real row-level classification data.

**Method, stated for auditability.** `pg_restore -a -t product_template -f <file>` and the equivalent for `product_category` were run using only the local PostgreSQL 18 client binary against the archive file directly. No live database server was ever started, no Docker container was created, and no network access was used. This produces a plain-text `COPY` dump of just that table's data. The extraction was parsed with `awk` to compute **aggregate counts only**, grouped by classification-field values; no individual product name, description, or price was read into this report, and the two temporary extraction files (roughly 40MB and 0.4MB) were deleted from the scratch directory immediately after the aggregate counts were computed.

**Product classification distribution, `product_template`, 83,753 real rows:**

| type | is_storable | tracking | count | % of catalog |
|---|---|---|---:|---:|
| consu | false | none | 42,677 | 51.0% |
| consu | true | none | 22,453 | 26.8% |
| consu | true | lot | 10,731 | 12.8% |
| consu | false | lot | 5,495 | 6.6% |
| consu | true | serial | 1,367 | 1.6% |
| service | true | none | **989** | **1.2%** |
| service | false | none | 34 | 0.04% |
| service | false | none (timesheet) | 7 | 0.01% |

Four findings follow directly from this table, none of which existed anywhere in the prior evidence chain:

1. **`type` contains only `consu` and `service` in this real table — zero `combo` rows, and zero legacy `'product'`-literal rows.** This substantially narrows GRPA-M14 (previously "PARTIALLY VERIFIED — narrowed, not closed"). For this one dataset, at this one point in time, the data-side half of that open question is answered — but not universally; see the caveat below.
2. **`is_storable` has zero NULLs** — 48,213 `false` / 35,540 `true` — despite the column being nullable at the database level (the dump's own column catalog shows `is_storable,boolean` with no `NOT NULL`). The application layer evidently always populates it even though the schema does not force it to.
3. **989 rows (1.2% of the catalog) carry `type='service'` AND `is_storable=true`, and are `active=true`** — not archived residue. This directly contradicts the theoretical invariant DR-002's own Tracks A5 and A18 stated as absolute ("only `type=='consu'` products can ever be storable; `service` and `combo` never can"). Cross-checking the dump's own constraint catalog confirms **zero CHECK constraints of any kind exist on `product_template`** — only a primary key and foreign keys. Nothing in the database prevents this state; only the ORM's one-directional compute discourages it going forward from a `type` change, and only for writes that pass through the ORM's normal compute-dependency path. All 989 rows were created by the same `create_uid`, inside a tight February–March 2026 window — consistent with either a deliberate, contained reclassification batch or a data-quality artifact of one import/cleanup event. This research cannot determine which, and states the pattern as observed fact only. **This is the concrete data-level precedent behind the asymmetric-hedge finding in §2**: Boss's own phrasing hedges "no stock ledger by default" for Consumable but not for Service, and real data shows the override happening on the Service side too.
4. **5,495 rows (6.6%) carry `type='consu'`, `is_storable=false`, `tracking='lot'`** — explicitly excluded from the full stock/valuation ledger gate, yet still carrying lot-level identity. This is real, sourced, at-scale evidence of exactly the "consumables sometimes tracked for cost/quantity awareness without full stock-ledger rigor" edge case this mandate asked about; §4 below ties this directly to an official Thai accounting concept.

**Category-level valuation policy, `product_category`, 3,980 real rows**: only 3 categories carry an explicit `property_cost_method`/`property_valuation` override (company-dependent JSONB fields); the remaining 3,977 inherit the company-wide default, and `packaging_reserve_method` is left at its schema default (`'partial'`) on all 3,980 rows. This is supplied as one new, real data point for the separately-owned N-A12-01 track (product-category valuation policy), not as a resolution of that track's own HIGH/REOPENED status, which this research does not touch, close, or reopen.

---

## 4. Research Findings — Thai Business and Regulatory Evidence

DR-002's own Track A11 states plainly that its research "was conducted entirely against generic Odoo business logic" and that none of its research agents were asked to search for Thailand-specific Inventory logic. **No prior pass in this chain tested the routing question against Thai business or regulatory reality at all.** This section is genuinely new ground.

Three independent, real sources corroborate the *shape* of Boss's hypothesis from entirely outside the reference-system codebase.

**Thai withholding tax.** Public sources — Thailand's e-government portal, tax-advisory firms, and PwC's own Thailand tax summary — converge on the same rule: withholding tax does not usually apply to the purchase of goods, while services are subject to withholding tax at rates from roughly 1% to 15% depending on the service type and whether the payee is domestic or international. This is a real, load-bearing, statutory Goods-versus-Service distinction, independent of any ERP vendor's design choice. It means the "Service" leg of Boss's hypothesis is not merely an ERP convenience but tracks an actual Thai compliance obligation that Stockable and Consumable goods generally do not carry. *(Sources: flowaccount.com/blog/withholding-tax-in-thailand/; thailand.acclime.com/guides/withholding-tax/; taxsummaries.pwc.com/thailand/corporate/withholding-taxes.)*

**Official Thai accounting-standard guidance on consumables versus inventory.** A Federation of Accounting Professions of Thailand (TFAC) explanatory guide to Thai Accounting Standard No. 2 (Inventories), together with a Chulalongkorn University accounting-practice guideline, both draw the same line: consumable materials (**วัสดุสิ้นเปลือง**) are a current asset distinct from full **สินค้าคงเหลือ** (Inventory under TAS 2, defined as goods held for sale in the ordinary course of business, in-process production, or raw materials/supplies for producing goods or rendering services). The guidance states the treatment explicitly: consumable/stock materials are an asset only for the portion remaining as of the reporting date; the portion used during the period is treated as an expense. This is an authoritative, real, named Thai accounting concept that maps almost exactly onto the real-data pattern found in §3.5 — a middle tier that is counted and valued periodically for cost-awareness, without the transaction-by-transaction moving-ledger rigor a full Inventory standard requires. It directly and independently supports the "Consumable → no stock ledger by default" leg of Boss's hypothesis, while also showing that "no stock ledger" in Thai practice does not mean "no tracking at all" — it means a lighter-weight, period-end tracking regime. *(Sources: tfac.or.th/upload/9414/gU1VKPD8Rk.pdf; cca.chula.ac.th/edocuments/images/files/letter/08_51/in_10370_2551.pdf.)* A supporting check of the revised TFRS for NPAEs — the standard most Thai SMEs actually report under, effective for periods from 1 January 2023 — confirms services are recognized on an economic-substance basis distinct from goods, consistent with, not contradicting, the Goods/Service split. *(Source: rsm.global/thailand/insights/thai-financial-reporting-standard-non-publicly-accountable-entities-revised-2022.)*

**A real, independent Thai SME software comparator.** FlowAccount — one of Thailand's own leading cloud accounting/invoicing platforms, built for SMEs and not a derivative of the reference ERP — documents a dedicated product-type concept it calls **"สินค้าประเภทนับสต็อก"** ("stock-counted product type"), explicitly framed for businesses that "regularly sell products and need to track quantities, remaining inventory, and product movement" — implying, by the platform's own framing, a complementary non-tracked bucket for everything else. FlowAccount also documents automatic **"ตัดสต็อก"** (stock deduction) triggered by invoicing, including across connected online-marketplace channels (Lazada, Shopee, TikTok Shop) — a real, independently-sourced confirmation that the core "does this item carry a stock ledger, yes or no" binary is exactly the mental model an actual Thai-market SME software vendor also builds around, entirely independent of the reference system this program's other evidence is drawn from. *(Sources: flowaccount.com FAQ knowledge-base article on using the stock system; flowaccount.com/blog/inventory-management-by-flowaccount/.)*

**Explicit non-generalization caveat.** Consistent with Track A11's own governing rule — "one ERP/customer dataset is not Thailand-wide inventory practice" — the regulatory and standards sources cited above are public, authoritative, and general, but the reference-dump evidence in §3.5 remains one company's real catalog at one point in time, and FlowAccount's documentation is one vendor's product design, not a survey. None of this constitutes the "real user validation" the wider program elsewhere requires for operational (as opposed to regulatory) claims about how Thai SMEs actually behave. It is offered as strong, real, citable directional support, not as a substitute for that validation.

---

## 5. Research Findings — Edge Cases

**Consumables tracked without full stock-ledger rigor.** No longer hypothetical: §3.5 found 5,495 real, active catalog rows (6.6%) that are `is_storable=false` — excluded from the reservation/forecast/valuation gate — yet `tracking='lot'`, still carrying lot-level identity. §4 found the matching, authoritative Thai accounting concept (วัสดุสิ้นเปลือง, tracked as a period-end-only asset, expensed as used) that gives this pattern a real business rationale rather than treating it as a data-quality accident. A target design that equates "Consumable" with "zero tracking of any kind" would be **narrower** than both the reference source's own real usage and real Thai accounting practice.

**Kits and bundles.** Two distinct mechanisms exist in the source — Combo, a sales bundle-choice selector, and Kit/phantom-BOM, a component-explosion mechanism (§3.2) — and neither is a member of the three-way split; both resolve to already-classified constituent items. A target design needs to decide, independently of the Stockable/Consumable/Service question, whether it needs either concept at all, and if so, ensure its own routing logic always resolves a bundle to its components before asking whether a given line is Stockable, Consumable, or Service.

**Services that consume stock.** Confirmed via the `repair.order` mechanism (§3.4): a single business transaction can legitimately contain both a Stockable-routed component (parts consumed, real `stock.move` records) and a Service-routed component (labor, billed via a `type='service'` product) at the same time. The correct application level for Boss's three-way split is therefore the **line item / SKU**, not the transaction or document as a whole — worth stating plainly, since any UI or process design that groups multiple lines under one document header (repair orders, project billing, kits) must not collapse the whole document to a single bucket.

**Perishables and expiration — nested, not a fourth bucket.** The `product_expiry` module's fields (`use_expiration_date`, `expiration_time`, `use_time`, `removal_time`, `alert_time`) were confirmed present in the real dump's own schema catalog, and their owning module was located directly at `product_expiry/models/product_product.py:38-54`. Their own help text states expiration is "computed on the lot/serial number" — meaning expiration only makes sense for lot- or serial-tracked items, which per §3.1 requires `is_storable=True`. Expiration is therefore correctly modeled as an attribute **nested under** the Stockable leg, not a parallel or competing classification. This narrows what had been registered `EVIDENCE_MISSING — NOT YET RESEARCHED` (N-A5-02) to "schema-confirmed present in the real dump; expiration structurally nested under Stockable plus lot/serial tracking," without claiming to have read the full expiry-workflow logic (removal/alert automation) in depth.

**Hybrid single-document transactions, more broadly.** Beyond repair orders, the source's own module footprint — `sale_project`, `sale_timesheet`, `industry_fsm_sale`, `mrp_repair` — shows this line-level mixing recurring across field-service, project-billing, and manufacturing-repair contexts generally, not as a one-off. This is reported as a structural pattern to design around, not as a call to adopt any of these specific vendor modules' own mechanisms.

---

## 6. Does the Target Vocabulary Need More Precision Than Three Labels?

Yes, on the evidence gathered. The three labels conflate at least four largely-orthogonal questions:

1. **Billing/revenue nature** — Goods vs. Service, the axis Thai WHT law and TAS 2/TFRS-for-NPAEs actually key off (source evidence: `type`).
2. **Ledger rigor** — a full moving stock ledger, versus period-end quantity/cost awareness without a moving ledger (วัสดุสิ้นเปลือง), versus no tracking at all (source evidence: `is_storable` crossed with `tracking`; real-data evidence: the 6.6% partial-rigor population in §3.5).
3. **Structural bundling** — kit/combo, which must be resolved at the component level before questions 1–2 can even be asked of a "line" (source evidence: `product.combo` versus `mrp.bom type='phantom'`).
4. **Service fulfillment/billing sub-method** — manual, timesheet, task/project, milestone, repair-parts (source evidence: `service_type`/`service_tracking`, contributed by at least eight different modules) — immaterial to Inventory's own ledger question, but material to Sales/Accounting invoicing-timing design.

This research does not propose how SMEsPlus should name or structure fields for these four questions — that remains Team B's own, separately clean-room-original, design task. It reports that a single flat three-value label, applied the way the reference system's own `type` field is applied, would under-specify at least the second and fourth of these dimensions, both of which have real, sourced, non-trivial populations behind them in the reference dataset.

### 6.1 Industry-specific classification signals

Several patterns surfaced that are plausibly industry-specific rather than universal, each stated as an observation, not a requirement:

- **Manufacturing/industrial-parts distributors** — the reference dataset itself appears to be this kind of business, given its part-master foreign keys, physical-dimension fields, and 3,980-category catalog structure. These businesses commonly also need a cross-cutting "this SKU, once acquired, becomes maintainable company equipment" classification, evidenced by `product_template`'s direct foreign keys to `maintenance_equipment_category`/`maintenance_team` and an `equipment_ok` boolean. This is orthogonal to, not a replacement for, the Stockable/Consumable/Service question.
- **Field-service/repair/project-billing businesses** — need the line-level hybrid pattern (§5) and the service sub-method axis (§6, item 4) to be first-class, not an afterthought.
- **Perishable-goods (food/pharma) SMEs** — need the expiration axis nested under Stockable (§5), with real removal/alert-date business logic this pass has only confirmed exists in schema, not read in full.
- **Omnichannel/marketplace-selling SMEs** — FlowAccount's own documentation (§4) highlights automatic stock deduction across connected online channels (Lazada/Shopee/TikTok Shop) as a real, actively marketed Thai SME need, meaning the routing decision ("does this line deduct stock") has to reach beyond the core ERP into channel integrations for a meaningful share of real Thai SME operations — a scope note, not a resolved requirement.

---

## 7. Migration Consequences

The correct target mapping for a source `(type, is_storable)` pair, based on this pass's evidence, is: `(consu, true) → Stockable`; `(consu, false) → Consumable`; `(service, *) → Service`. All three of these combinations, plus the `(consu, false, tracking=lot)` partial-rigor sub-state, are populated at real, non-trivial scale in the reference dataset (§3.5) — this mapping has real precedent behind it, not only theoretical soundness.

**The one real contradiction found — 989 rows carrying `service` with `is_storable=true` — is a genuine, concrete migration-decision point** that this research surfaces but does not resolve. A migration or target-design rule must state explicitly which field wins when the two disagree. The most defensible answer, on this evidence, is `type` — `is_storable`'s own compute already treats `type` as authoritative, and Boss's hypothesis is itself phrased in terms of the Stockable/Consumable/Service *item concept* that `type` most directly encodes — but this is a Team B / Migration decision to make and formally record, not one this research is authorized to make on its own.

`combo`-type rows and `sale_order_line.is_service` require **no special migration handling beyond the base mapping**: zero `combo` rows exist in the real sample, so for this dataset there is nothing to migrate under that bucket beyond preserving the schema capability if it is ever needed, and `is_service` is a pure redundant mirror of `type` (§3.3) that migration can safely ignore or recompute rather than treat as an independent source fact.

**GRPA-M14 is substantially, but not universally, narrowed.** The confirmed absence of any database CHECK constraint on `product_template.type` or `is_storable` means the real-data cleanliness observed in this one dump is a property of *this dataset*, not a guarantee the database schema makes for any future tenant's data. Migration's own execution-time validation — already the assigned owner of GRPA-M14, per IDR-007's disposition — should run a live distinct-value check on `type`/`is_storable` per source dataset at actual cutover, rather than relying on this research's one-time sample as a permanent guarantee.

Kit/BOM (`mrp.bom type='phantom'`) and Combo (`product.combo`) migration is a **structural/relationship migration problem** — migrating an assembly or bundle relationship between products — categorically different from a per-item classification migration problem. This is flagged as a distinct migration work item, not designed here.

---

## 8. Accounting-Handoff Consequences

Per this track's explicit boundary — state facts, do not make Accounting design decisions — and consistent with DR-002's own Track A9 authority-boundary discipline ("Inventory may know the stock fact and valuation handoff evidence. Accounting owns final financial truth and posting semantics"):

- **Fact.** In the reference system, whether a stock movement automatically produces an accounting journal entry from Inventory's own side is gated on `is_storable == True` AND `product.valuation == 'real_time'` (`_should_create_account_move()`, reconfirmed this pass, consistent with DR-002's Tracks A9 and A16). Structurally, Consumable and Service items **never** trigger this specific automatic mechanism — any accounting effect for them in the reference system flows through ordinary purchase/expense or revenue-recognition posting, not inventory-valuation-driven COGS.
- **Fact.** No `stock.valuation.layer` ledger model exists in this checkout; valuation data lives directly on `stock.move`, unchanged from DR-002's own Track A9 finding. This affects what "valuation history" even means to migrate or reconcile against, for whichever items do route through the valuation gate.
- **Fact.** Withholding-tax eligibility (`wt_tax_id`/`supplier_wt_tax_id` on `product.template`, contributed by the generic `l10n_account_withholding_tax` module) is architecturally **independent** of `type`/`is_storable` in the source — nothing prevents a Goods item from carrying a default WHT rate, and nothing forces a Service item to carry one. In real Thai practice (§4), the two correlate strongly — goods generally WHT-exempt, services generally WHT-liable — but the source does not encode that correlation as a rule; they are two independently-configured attributes that happen to usually agree. Whether SMEsPlus's target design should derive WHT-applicability from the routing classification, or keep the two as independent attributes the way the reference system does, is an Accounting/Tax design decision this research does not make.
- **Fact, offered as input only.** Real category-level valuation-policy customization is rare in this dataset — 3 of 3,980 categories (§3.5) — with company-level defaults dominating in observed practice. This is supplied as one data point for the separately-owned N-A12-01 investigation, which explicitly already covers product-category valuation policy within its own scope. It is not a finding this track is authorized to use to close, narrow, or otherwise adjudicate N-A12-01, and no such adjudication is made here.

---

## 9. Item Classifications (Summary)

| Item | Classification | Primary Evidence |
|---|---|---|
| Boss's 3-way hypothesis as a foundational business distinction | CONFIRMED directionally — a real, load-bearing distinction; requires precision refinement before it is implementation-ready | Reference source gating chain; Thai WHT law; TFAC/TAS 2 consumables guidance; FlowAccount's own stock-counted product-type feature — four independent lines of evidence |
| Reference system's own product-classification model | Does NOT map 1:1 to a 3-way selector — two independent axes, not one | `product_template.py:54-65` (type); `stock/models/product.py:821-895` (is_storable) |
| "Combo" (source type value #3) | Not a stock-treatment category — a Sales/POS bundle-choice selector, orthogonal to routing | `_prepare_tooltip()`; `combo_ids → product.combo → combo_item_ids`; 0 of 83,753 real rows are `combo` |
| Kit / BOM "phantom" type | A separate BOM-layer mechanism, not a product-classification value, and not the same concept as Combo | `mrp/models/mrp_bom.py:29`; `sale_mrp` component-redirection logic |
| Service sub-taxonomy (`service_type`/`service_tracking`) | Service is not one uniform behavior — real heterogeneity in fulfillment/billing method, though none of it touches the stock ledger | `product_template.py:71-80`; eight extension modules per the ORM/DB mapping catalog |
| `sale_order_line.is_service` (GRPA-M13) | RESOLVED — a pure computed mirror of `product.type=='service'` | `sale_service/models/sale_order_line.py:17,36-40` |
| Legacy `'product'` type literal (GRPA-M14) | Substantially narrowed for this one dataset; not a universal guarantee | Live extraction: distinct `type` values = `{consu, service}` only, zero `combo`, zero legacy `product` |
| `is_storable`/`type` invariant, theoretical vs. actual | NEW FINDING — the source's own "Service can never be storable" rule is violated in real production data | 989 of 83,753 rows, `type='service' & is_storable=true`, active, single-user/2-month window; zero CHECK constraints |
| Partial-rigor "tracked but not fully ledgered" consumables | CONFIRMED as a real, materially-sized pattern (6.6% of catalog); matches a named, official Thai accounting concept | 5,495 rows: `consu`/`is_storable=false`/`tracking=lot`; TFAC/Chulalongkorn วัสดุสิ้นเปลือง guidance |
| Repair orders (services that consume stock) | CONFIRMED concrete edge case — one transaction spans Stockable and Service simultaneously, at the line-item level | `repair/models/repair.py` `move_ids`; `action_create_sale_order()` |
| Product-level WHT attachment (`wt_tax_id`/`supplier_wt_tax_id`) | FACT — architecturally independent of type/is_storable in source, though correlated with Service in real Thai practice; an Accounting/Tax design question | `product_template` WHT columns; Thai Revenue Code practice per public sources |
| Category-level valuation-policy override | FACT — rarely used in this reference dataset; supplied as input to N-A12-01, not a resolution of it | 3 of 3,980 real categories carry an explicit override |
| Inventory-to-Accounting valuation-eligibility gate | FACT, reconfirmed — automatic journal entry requires `is_storable=True` AND `valuation=='real_time'`; Consumable/Service never get this automatically from Inventory | `_should_create_account_move()`; consistent with DR-002 A9/A16 |
| Thai real-business corroboration independent of the reference ERP | CONFIRMED via a real, Thailand-native SME accounting platform, not only the one ERP reference | FlowAccount public documentation |

---

## 10. Material Questions and Contradictions

These are surfaced explicitly, per this mandate's instruction, rather than resolved or smoothed over:

1. **The asymmetric hedge in Boss's own hypothesis text.** Consumable is hedged "no stock ledger *by default*"; Service is stated flatly. Real data shows the override happens in both directions in practice: `is_storable` can be, and is, manually set `True` for Goods away from its `False` default, and 989 real rows show `type=service` with `is_storable=true`. The target design must decide explicitly whether either override is ever legitimate for SMEsPlus, and if so, which field wins when `type` and `is_storable` disagree. This research surfaces the contradiction with real-data precedent; it does not resolve it.
2. **Forcing the source's literal two-field shape onto SMEsPlus would also import a demonstrated data-integrity gap.** The source contains no single field whose three values are "Stockable/Consumable/Service." Copying its literal `type` + `is_storable` shape as-is would import both the 989-row contradiction and a database-unenforced invariant. Per DR-002's own Track A17 quarantine, already on record and now reinforced with sharper evidence, this shape should inform, not define, SMEsPlus's target schema — a genuine tension between "reuse validated business semantics" and "do not copy vendor architecture" that Team B will have to navigate.
3. **Whether Combo and Kit are both needed at all is unanswered.** Zero live `combo`-type rows were found in the 83,753-row real sample (a configured capability, unused in practice, at least in this one dataset), while the reference codebase's manufacturing/BOM footprint suggests Kit-style bundling is the more operationally relevant mechanism for a parts/manufacturing-heavy business. This is a Team B / Product-scope question, not answered here.
4. **Whether Thai withholding-tax applicability should ever be inferred from the routing classification, or must always remain an independent, explicit per-product/per-transaction attribute**, is an Accounting/Tax design decision this research explicitly does not make. It only establishes that the reference system keeps the two structurally independent while Thai tax practice keeps them strongly correlated.
5. **Whether "Consumable" is one bucket or needs a distinguishable sub-state.** The real 5,495-row "not-storable-but-lot-tracked" population raises a question the flat three-label hypothesis does not answer: does SMEsPlus's target design need a distinguishable "Consumable — quantity/lot aware" sub-state (matching Thai วัสดุสิ้นเปลือง period-end-counted practice) versus "Consumable — fully expensed, no tracking at all"? This research surfaces the question with real-data and real-accounting-standard support; it does not select an answer.
6. **GRPA-M14's underlying concern is narrowed, not eliminated, as a general migration risk.** Because no database CHECK constraint exists to guarantee this dataset's cleanliness holds for any other tenant's data, Migration's own execution-time validation should still run a live distinct-value check per tenant at cutover rather than relying on this research's one-time sample.

---

## 11. Open Risks and Holds Carried Forward

- The migration mapping rule for `type`/`is_storable` disagreement (the 989-row real precedent) is **undecided** — belongs to Team B design / Migration execution, not resolved here.
- Whether SMEsPlus needs a Combo and/or Kit concept at MVP, and if so which mechanism, is **unanswered** — a Product/Team B scope decision, not resolved here.
- The WHT-applicability-vs-routing-classification relationship is an **Accounting/Tax design decision**, not resolved here, per this track's explicit instruction to state facts only.
- **N-A5-02** (`product_expiry`/perishables) remains formally `EVIDENCE_MISSING` beyond what this pass newly confirmed (schema-level presence; expiration nested under the Stockable leg only) — a dedicated pass would still be needed for full expiry-workflow evidence if SMEsPlus targets food/pharma SMEs.
- **N-A12-01** (product-category valuation policy / period close) remains the parallel Account-domain track's own `HIGH FUNCTIONAL DESIGN GAP — REOPENED`. This research contributes one new supporting data point (only 3 of 3,980 real categories override cost/valuation method) as input only, and explicitly does not touch, close, or reopen that item itself.
- This research's Thai-business-reality evidence is grounded in one reference company's real but non-generalizable dataset, official Thai accounting-standard/tax-adjacent public sources, and one leading Thai SME software vendor's public product documentation. It is not a survey of Thai SME owners or bookkeepers and does not by itself satisfy any "real user validation" bar the wider program may require elsewhere, consistent with Track A11's own governing rule that one dataset, or one vendor's documentation, is not Thailand-wide truth.

---

## 12. Reconciliation with the DR-002 Evidence Register

This pass advances the following register items, all inside this track's own lane. No item marked `CLOSED_WITH_EVIDENCE` or `CLOSED` in the prior-evidence context supplied to this session was re-litigated.

| Register Item | Status Entering This Pass | Status After This Pass |
|---|---|---|
| GRPA-M13 (owning module for `sale_order_line.is_service`) | Open since Group A, still open after DR-002 | **RESOLVED** — pure computed mirror of `product.type`, no independent semantics (§3.3) |
| GRPA-M14 (legacy `'product'` type literal) | `PARTIALLY VERIFIED` after DR-002 | **Substantially narrowed** by real row-level data for this one dataset (§3.5); explicitly not closed as a universal guarantee; ownership (Migration's gap-closure queue, per IDR-007) unchanged |
| SAAS-07 (`type`/`is_storable` gating via string-literal branching rather than an enforced invariant; rated Low severity in DR-002 from a code-pattern observation alone) | Low severity, code-pattern observation only | **Empirically corroborated at the data level** by the real 989-row violation found this pass; this research does not re-rate SAAS-07's severity — that is Audit VETO's or the appropriate governance track's call — but supplies the concrete data-level evidence that was previously only a theoretical code-smell observation |
| N-A5-02 (`product_expiry` module) | `EVIDENCE_MISSING — NOT YET RESEARCHED` | Narrowed to "schema-confirmed present in real dump; expiration nested under Stockable plus lot/serial tracking" (§5); full expiry-workflow depth remains unread |
| N-A12-01 (product-category valuation policy / cross-year continuity) | `HIGH FUNCTIONAL DESIGN GAP — REOPENED`, owned by the parallel Account-domain work | **Not touched, closed, or reopened** by this research; one real supporting data point supplied as input only (§3.5, §8) |

---

## 13. Clean-Room Impact Statement

**This research stayed strictly within the Reference-Only clean-room boundary throughout.**

All source-code reading — the `product`, `stock`, `stock_account`, `sale_stock`, `purchase_stock`, `mrp`, `sale_mrp`, `repair`, `sale_service`, `sale_project`, `product_expiry`, and `l10n_account_withholding_tax` modules, under the project's already-authorized local source root — was read-only. Zero writes were made to the source tree at any point.

Every finding above cites vendor field and method names strictly as evidence of business semantics (for example, "the field is named `is_storable`, and gates X"). None of it proposes that SMEsPlus adopt those literal field names, the two-field `type`/`is_storable` pattern, the `product.combo` model, the `mrp.bom` phantom-Kit mechanism, the `service_type`/`service_tracking` selection set, or any other vendor ORM, schema, or workflow structure as SMEsPlus's own design. No vendor source-code body is reproduced verbatim anywhere in this report; every citation is file-path-and-field/method-name only, consistent with DR-002's own Track A17 discipline.

This pass explicitly **reaffirms and sharpens** DR-002/Track A17's existing quarantine of the source's `type`/`is_storable` two-field shape from Team B design. The new evidence gathered in this pass — a real 989-row invariant violation, the Combo-versus-Kit non-fit, the `service_type`/`service_tracking` heterogeneity, and the confirmed absence of any database-level enforcement of any of it — makes the case for that quarantine **stronger, not weaker**: copying this vendor's literal shape would import both its structural untidiness and a demonstrated real-world data-integrity gap.

The one live-dump extraction performed in this pass (`product_template` and `product_category` table **data only**, via a targeted single-table `pg_restore -a -t <table> -f <file>` using already-locally-installed PostgreSQL 18 client tooling) used **no live database server, no Docker container, and no network access**. It was read strictly for **aggregate classification-field distributions** — counts by `type`, `is_storable`, `tracking`, and `service_type`; category-level valuation-policy population counts. **No individual product name, description, price, partner, or any other business-content field was extracted into any retained artifact or written into this report.** The two temporary extraction files were deleted from the scratch directory immediately after the aggregate counts were computed, consistent with the same data-hygiene discipline DR-002's own Tracks A2/A17 describe for their own (unsuccessful) restore attempt.

**No SMEsPlus target design, schema, table, field name, or workflow is proposed anywhere in this deliverable.** This is evidence and business-semantic analysis only, produced for Boss's eventual Gate decision and for Team B's eventual, separately clean-room-original, design work. Team B, Team C, and Development are not authorized by anything in this document, in whole or in part.

---

## 14. Verdict and Closing Classification

Boss's Stockable/Consumable/Service routing hypothesis is **directionally confirmed** by four independent evidence lines — reference-system source code, live reference-system data, official Thai accounting/tax sources, and a real Thai SME software vendor — and is **ready to inform, but not yet ready to be adopted verbatim as, a target design**. It requires the precision refinements identified in §6, an explicit decision on the real-data contradiction found in §3.5, and explicit scope decisions on Combo/Kit and on the service sub-method axis. This research does not select any of those answers, does not design SMEsPlus's own schema or field names, does not rule on WHT-classification linkage, does not touch N-A12-01, and does not authorize Team B design, Migration execution, or any Gate PASS.

**Closing classification for fingerprint INV-FP-13: `CARRY_FORWARD`**

Rationale for this classification over the alternatives:

- Not `CLOSED_WITH_EVIDENCE` — the hypothesis is evidence-supported in its *direction*, but §10 names real, unresolved precision gaps (the type/is_storable tie-break rule, the Combo/Kit scope question, the WHT-linkage question, the Consumable sub-bucketing question) that must be decided before the hypothesis is implementation-ready. Calling it closed would overstate what this pass actually settled.
- Not `REOPEN_ELIGIBLE` — this fingerprint was never previously closed; there is nothing to reopen.
- Not `CONFLICTING` — the four evidence lines (reference source, live data, Thai regulatory/accounting-standard sources, FlowAccount) converge with, rather than contradict, one another. The one real contradiction found (§3.5, the 989-row `service`/`is_storable=true` population) is a contradiction *within the reference system's own data* relative to its own theoretical invariant, not a conflict between this pass's evidence sources.
- Not `UNKNOWN` — this pass produced substantial, cited, convergent evidence; the hypothesis is not unexamined.
- Not `SUPERSEDED` — nothing in this pass replaces or invalidates the hypothesis; it strengthens and refines it.
- `CARRY_FORWARD` best describes the actual outcome: the hypothesis is evidence-supported in direction and ready to inform Team B's design, while its named precision gaps and open decision points (§10, §11) carry forward explicitly to Team B design, Migration execution, and Accounting/Tax design, to be picked up and resolved there rather than by this research pass.

This is a research finding for Boss's decision. It is not a Gate PASS declaration, and it does not authorize Team B, Team C, or Development to begin work on the strength of anything in this document.
