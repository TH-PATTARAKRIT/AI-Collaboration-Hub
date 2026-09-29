# Source Map (candidate) — `account_add_gln`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_add_gln` |
| Display name | Add Partner GLN |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `240130bade3471b1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_add_gln/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / This module adds the Global Location Number to the partner. Used on delivery addresses, it is used to identify stock locations and is mandatory on the UBL/CII eInvoices (but not only). The module is intended be merged with account, later on, in master
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 18 of 18 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — account_add_gln
Source revision: 19.0.post20260921 | Module: "Add Partner GLN" (account_add_gln/__manifest__.py:2) | License LGPL-3 (:13)
Basis: static reading only. No tests, security files, or data records in this module (manifest lists only one view file, :9-11).

## A. Capabilities and optionality
- A1. Adds one optional text field, the Global Location Number (GLN), to the business partner (contact/address). account_add_gln/models/res_partner.py:7
- A2. The field is visible on the partner form only when the address type is "delivery"; shown on the partner's Sales & Purchase tab and inside the child-address sub-form. account_add_gln/views/res_partner_views.xml:10,13
- A3. Optionality: auto_install with dependency on account, so it is present whenever accounting is installed. account_add_gln/__manifest__.py:6,8
- A4. Stated intent (manifest summary): identify delivery stock locations; described as mandatory for UBL/CII e-invoices "but not only"; intended to be merged into account later. account_add_gln/__manifest__.py:3
- A5. No validation, format check, or lifecycle behaviour is defined for the GLN. UNKNOWN — EVIDENCE INSUFFICIENT whether any checksum rule exists elsewhere (none found in this module).

## B. Objects and relationships
- B1. Only extends res.partner (owner: base). No new model. account_add_gln/models/res_partner.py:4-7
- B2. Relationship to invoices: the value is read from the invoice's shipping/delivery partner by the e-invoice export in account_edi_ubl_cii. account_edi_ubl_cii/models/account_edi_ubl.py:1684-1686; account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:316; account_edi_ubl_cii/models/account_edi_cii.py:590
- B3. No state machine.

## C. Validations, security, multi-company
- C1. No constraints, no access-rule files, no groups defined by this module (no security folder; manifest data list only a view). account_add_gln/__manifest__.py:9-11
- C2. Field is not company-dependent; the value is stored once on the partner record (plain Char, no company_dependent flag). account_add_gln/models/res_partner.py:7. Multi-company visibility follows res.partner rules owned by base — UNKNOWN — EVIDENCE INSUFFICIENT (not read).
- C3. The view record has priority 15 and extends the base partner form. account_add_gln/views/res_partner_views.xml:6-7

## D. Handoffs
- D1. E-invoicing (UBL/CII) export consumer: account_edi_ubl_cii. It checks whether this module is installed (or field exists) before emitting the GLN as a delivery-location identifier (scheme id 0088 in the UBL path, account_edi_ubl_cii/models/account_edi_ubl.py:1685). account_edi_ubl_cii/models/account_edi_ubl.py:1684; account_edi_ubl_cii/models/account_edi_xml_ubl_20.py:316; account_edi_ubl_cii/models/account_edi_cii.py:590
- D2. Tests in account_edi_ubl_cii reference the field (TEST): account_edi_ubl_cii/tests/test_ubl_export_bis3_be.py; account_edi_ubl_cii/tests/test_cii_export_facturx_fr.py (file-level pointers only; not read in detail).
- D3. No accounting entries, stock movement, or approval flow.

## E. Configuration
- E1. None. The field is blank by default; its only effect is presence/absence of a location identifier in exported e-invoice documents (via D1).

## F. Extension path
- res.partner is the only extended object here. Community modules that extend res.partner include (partial, module names only): account, account_add_gln, account_edi_ubl_cii, account_peppol, account_peppol_response, base_vat, delivery, delivery_mondialrelay, sale, purchase, purchase_stock, point_of_sale, website_sale, and many l10n_* modules (full grep result lists ~130 modules).
- Direct consumers of the GLN field: account_edi_ubl_cii only (grep of "global_location_number" across the addons root found only account_add_gln and account_edi_ubl_cii).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which countries/formats make the GLN mandatory in practice (manifest text only says so; the export code conditions were not fully read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the GLN of a non-delivery-type partner is ever exported (view hides it, but the field exists on all partners).
- UNKNOWN — EVIDENCE INSUFFICIENT: Peppol-side use (account_peppol not read for this field).

