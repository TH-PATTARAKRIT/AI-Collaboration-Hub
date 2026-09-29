# Source Map (candidate) — `barcodes_gs1_nomenclature`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `barcodes_gs1_nomenclature` |
| Display name | Barcode - GS1 Nomenclature |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `289511f12176b733` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/barcodes_gs1_nomenclature/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `barcodes`, `uom`
- Direct dependents in 300-module list (1): `stock`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Parse barcodes according to the GS1-128 specifications
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `ir.http`, `barcode.nomenclature`, `barcode.rule`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.http`, `barcode.nomenclature`, `barcode.rule`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 15 of 15 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: barcodes_gs1_nomenclature
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities
- Adds GS1-128 interpretation to the barcode framework; depends on barcodes and uom (barcodes_gs1_nomenclature/__manifest__.py:8). Not an application; no auto_install flag (manifest lines 1-25). Core dependency of stock (stock/__manifest__.py:9), so present whenever inventory is installed.
- A nomenclature can be flagged "GS1"; only GS1-128 rules are honoured in such a nomenclature (barcodes_gs1_nomenclature/models/barcode_nomenclature.py:16-18). Conditional per nomenclature flag.
- Shipped "Default GS1 Nomenclature" with ~29 rules (barcodes_gs1_nomenclature/data/barcodes_gs1_rules.xml:4-6; rules from line 10 to 338). Covered identifiers: SSCC (00) as package (rules xml:15-17), GTIN (01)/(02) as product (25-27, 35-37), ship-to/forward-to GLN (410/413) as destination location (45-47, 55-57), GLN (414) as location (65-67), batch/lot (10) and serial (21) as lot (76-78, 86-88), pack date (13), best-before (15), expiry (17) as dates (97-119), counts (30/37) and weight/length/area/volume style measures as quantity (128-323), package type (91) (333-335).
- Decomposition of a multi-identifier scan into an ordered list of items, using an FNC1 group separator; unrecognised remainder makes the whole parse fail (returns nothing) (barcode_nomenclature.py:99-135). (TEST) barcodes_gs1_nomenclature/tests/test_barcodes_gs1_nomenclature.py:36 and :68 (decimal handling).
- Content types: date, measure, numeric identifier (check digit verified), alpha-numeric (barcode_rule.py:39-49; barcode_nomenclature.py:64-97).
- Date interpretation with century rule; day "00" means last day of month; invalid dates raise a validation error (barcode_nomenclature.py:32-62). (TEST) tests/test_barcodes_gs1_nomenclature.py:7.
- Measure with decimals: last digit of the application identifier gives decimal position (barcode_nomenclature.py:71-79; barcode_rule.py:50).
- Rule may be tied to a unit of measure for quantity rules (barcode_rule.py:51).
- Product-search helper: when the company nomenclature is GS1, a search on the barcode field is rewritten so that GS1-formatted or zero-padded input matches stored product/lot values; lot-type results match exactly, others match the unpadded numeric part (barcode_nomenclature.py:142-205). (TEST) tests/test_barcodes_gs1_nomenclature.py:139.
- Front-end receives the company's FNC1 separator regex in session info only when its nomenclature is GS1 (barcodes_gs1_nomenclature/models/ir_http.py:10-16).

## B. Business objects and lifecycle
- Extends barcode.nomenclature with flag + separator (default regex accepts Alt029, "#", or ASCII 29) (barcode_nomenclature.py:16-21) and barcode.rule with GS1 encoding, extra rule types and GS1 attributes (barcode_rule.py:13-51).
- Extra rule types: quantity, location, destination location, lot, package, best-before date, expiration date, package type, pack date (barcode_rule.py:16-37). Removing this module resets such rules to the default type ("set default" ondelete, lines 27-37).
- New rules created from a GS1 nomenclature form default to GS1-128 encoding via context (barcode_rule.py:10-11; views/barcodes_view.xml:19-21).
- No states/workflow; configuration data. Rule data is noupdate=1 (rules xml:2).

## C. Validations, security, multi-company
- Separator must compile as a regular expression when the nomenclature is GS1 (barcode_nomenclature.py:23-30).
- GS1 rule pattern must compile and contain exactly two captured groups (identifier + value); non-GS1 rules fall back to the base syntax check (barcode_rule.py:53-69).
- Measure rules raise an error if value cannot be cast to a number (barcode_nomenclature.py:80-85). Identifier values with a wrong check digit are treated as non-matching (line 88-89).
- Security: no ACL, group or record rule file in this module (data_files list, manifest lines 9-12); inherits the barcodes access (read for internal users, full for ERP manager) from barcodes/security/ir.model.access.csv:2-5.
- Multi-company: search rewrite and session info read the current company's nomenclature (barcode_nomenclature.py:150; ir_http.py:12). The session-info read is done with elevated access (ir_http.py:12).

## D. Handoffs
- Stock [stock]: uses GS1 unit-of-measure quantity rules to build aggregate barcodes for quants when a barcode separator system parameter is set (stock/models/stock_quant.py:1405-1418; parameter exposed at stock/models/res_config_settings.py:52-54).
- Expiry [product_expiry]: quant GS1 barcode generation override exists (product_expiry skeleton method _get_gs1_barcode; see product_expiry note).
- Point of sale [point_of_sale]: can select a GS1 nomenclature for the company and a fallback nomenclature per config (point_of_sale/models/pos_config.py:202; (TEST) point_of_sale/tests/test_frontend.py:1342-1347).
- Package type / package / lot / location targets are resolved by the consuming app, not here. No accounting handoff.

## E. Configuration that changes outcomes
- Nomenclature GS1 flag and FNC1 separator regex; rule sequence, content type, decimal usage, associated unit (barcode_rule.py:39-51).
- Company nomenclature choice (barcodes/models/res_company.py:12) determines whether GS1 mode is active.
- Context flag skip_preprocess_gs1 disables search rewriting (barcode_nomenclature.py:151).

## F. Effective extension path (module names only)
- Extends barcode.nomenclature/barcode.rule: this module itself. Other Community modules extending barcode.rule: stock, point_of_sale, pos_loyalty.
- Consumers of the GS1 parse or its rule fields: stock, product_expiry, point_of_sale.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side parser and barcode service behaviour (static JS not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether every consumer calls the search-rewrite helper; no callers found outside this module in the Python grep.
- UNKNOWN — EVIDENCE INSUFFICIENT: exact list of measure rules beyond the sampled pattern lines (two rule blocks share the same 322x pattern at rules xml:236-251; intent not established).

