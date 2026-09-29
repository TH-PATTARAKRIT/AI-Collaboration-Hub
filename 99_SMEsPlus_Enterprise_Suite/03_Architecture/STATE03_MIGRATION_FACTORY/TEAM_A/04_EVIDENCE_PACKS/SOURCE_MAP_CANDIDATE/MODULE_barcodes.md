# Source Map (candidate) — `barcodes`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `barcodes` |
| Display name | Barcode |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f43d8722ab3a8d44` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/barcodes/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (3): `barcodes_gs1_nomenclature`, `event`, `hr_attendance`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `point_of_sale`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Scan and Parse Barcodes
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `barcodes.barcode_events_mixin` (Barcode Event Mixin); `barcode.nomenclature` (Barcode Nomenclature); `barcode.rule` (Barcode Rule)
- Objects extended from other modules (2): `ir.http`, `res.company`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `barcode.nomenclature` ← Community: `barcodes_gs1_nomenclature`; open-license custom/third-party scanned: —
- `barcode.rule` ← Community: `barcodes_gs1_nomenclature`, `point_of_sale`, `pos_loyalty`, `stock`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `ir.http`, `res.company`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 29 of 30 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: barcodes
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities (core / optional / conditional)
- Scan-and-parse service module; declared category Supply Chain/Inventory; depends only on the web layer (barcodes/__manifest__.py:4-6). Not an application; no auto_install flag (barcodes/__manifest__.py:1-25). Core building block; other apps depend on it.
- Nomenclature = named set of ordered rules that classify a scanned string (barcodes/models/barcode_nomenclature.py:16-24). Core.
- Rule types shipped in this module: "alias" and "unit product" only (barcodes/models/barcode_rule.py:22-26); further types are added by extending modules (see F).
- Rule encodings: any, EAN-13, EAN-8, UPC-A (barcodes/models/barcode_rule.py:15-21).
- Numeric payload inside a pattern (weight/price style) indicated by a braces convention; the product record must carry zero digits in that slot (barcodes/views/barcodes_view.xml:20-27; barcodes/models/barcode_nomenclature.py:43-84).
- UPC/EAN auto-conversion policy per nomenclature: never / EAN-to-UPC / UPC-to-EAN / always; default "always" (barcodes/models/barcode_nomenclature.py:8-13, 22-24). Conditional on nomenclature setting.
- Rule matching: rules evaluated in sequence order; first match wins; alias rules rewrite the code and continue evaluation, product-type match ends parsing; nothing matched yields an "error" type result (barcodes/models/barcode_nomenclature.py:106-142, rule order barcode_rule.py:10).
- Check-digit normalisation of matched base code for EAN-13 and UPC-A (barcodes/models/barcode_nomenclature.py:26-41, 134-139).
- Radio-tag URI conversion: strings starting "urn:" (lgtin, sgtin, sgtin-96/198, sscc, sscc-96) are converted into product+lot or package results (barcodes/models/barcode_nomenclature.py:86-89, 144-206). (TEST) test_barcode_uri_conversion (barcodes/tests/test_barcode_nomenclature.py:256).
- Form-scan event mixin for backend forms: a scanned value is handed to the model and the scan field is cleared; the using model must implement the handler, otherwise a not-implemented error is raised (barcodes/models/barcode_events_mixin.py:13-26). Optional - no other Community module was found inheriting it (grep of addons root).
- Browser scan timing: internal users receive a "max time between keys" value (default 150 ms) from a system parameter (barcodes/models/ir_http.py:10-15). Conditional on internal user.

## B. Business objects and lifecycle
- barcode.nomenclature 1..n barcode.rule (barcode_nomenclature.py:21; barcode_rule.py:13). No workflow states; records are configuration data.
- Company holds one active nomenclature (res.company.nomenclature_id) defaulting to the shipped "Default Nomenclature" (barcodes/models/res_company.py:9-16; data barcodes/data/barcodes_data.xml:3-14).
- Shipped default rule: one catch-all product rule, sequence 90, any encoding (barcodes/data/barcodes_data.xml:7-14). Data is noupdate=1 (barcodes_data.xml:2).
- At install, companies lacking a nomenclature are assigned the default (barcodes/__init__.py:6-14, hooked at __manifest__.py:13).

## C. Validations, security, multi-company
- Pattern syntax check: only one pair of braces, containing N's then D's, not empty, bare "*" rejected, must compile as a regular expression (barcodes/models/barcode_rule.py:30-47). (TEST) invalid pattern case barcodes/tests/test_barcode_nomenclature.py:56.
- The shipped default nomenclature cannot be deleted (barcodes/models/barcode_nomenclature.py:208-215).
- Access: internal users read-only; ERP-manager group full rights on nomenclature and rule (barcodes/security/ir.model.access.csv:2-5). No record rules and no groups defined by this module (no security XML in module).
- Multi-company: the nomenclature choice is stored per company (res_company.py:12-16); nomenclature and rule records themselves have no company field and no company rule (barcode_nomenclature.py:20-24, barcode_rule.py:12-28), so they are shared across companies.

## D. Handoffs (owner module in brackets)
- Stock barcode-handling (lot/package/location rule types) [stock] extends rule types: stock/models/barcode.py:8-20.
- Point-of-sale rule types (weight, price, discount, client, cashier) [point_of_sale]: point_of_sale/models/barcode_rule.py:9-24; per-session nomenclature and fallback nomenclature [point_of_sale]: point_of_sale/models/pos_config.py:202, point_of_sale/controllers/main.py:98-99.
- Coupon rule type [pos_loyalty]: pos_loyalty/models/barcode_rule.py:8-10.
- Attendance kiosk scanning reuses the front-end scan service assets [hr_attendance]: hr_attendance/__manifest__.py:88-91 (asset reuse only).
- No accounting, approval or audit-trail handoffs found in this module.

## E. Configuration that changes outcomes
- Company nomenclature selection; nomenclature UPC/EAN conversion policy; rule sequence; rule encoding; alias target (barcode_rule.py:27-28).
- System parameter barcode.max_time_between_keys_in_ms (default 150) - ir_http.py:14.
- Setting the company nomenclature to a GS1 nomenclature changes parsing behaviour (see barcodes_gs1_nomenclature).

## F. Effective extension path (module names only)
- Extend barcode.rule: barcodes_gs1_nomenclature, stock, point_of_sale, pos_loyalty.
- Extend barcode.nomenclature: barcodes_gs1_nomenclature.
- Extend res.company (nomenclature): point_of_sale (uses the field in company data and settings: point_of_sale/models/res_company.py:39, res_config_settings.py:43).
- Modules declaring a dependency on barcodes: barcodes_gs1_nomenclature, hr_attendance, event; (via GS1) stock, point_of_sale.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side behaviour of the scan service and barcode scanner components (static JS not analysed in this pass).
- UNKNOWN — EVIDENCE INSUFFICIENT: how event uses barcodes (only the dependency was seen, event/__manifest__.py:20).
- UNKNOWN — EVIDENCE INSUFFICIENT: any rule about which company's nomenclature applies to a multi-company scan session beyond the company field itself.

