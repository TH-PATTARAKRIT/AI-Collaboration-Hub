# Source Map (candidate) — `account_qr_code_emv`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_qr_code_emv` |
| Display name | account_qr_code_emv |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `09fd9283bc143b8c` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_qr_code_emv/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`
- Direct dependents in 300-module list (1): `l10n_th`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (5): `l10n_br`, `l10n_hk`, `l10n_kh`, `l10n_sg`, `l10n_vn`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Payment / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `res.partner.bank`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.partner.bank`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 31 of 32 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: account_qr_code_emv (EMV Merchant-Presented QR bridge)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/account_qr_code_emv.json. Pointers are `module/path:LINE`. This module ships no tests (account_qr_code_emv has no tests folder), so no (TEST) claims.

## A. Capabilities / functions
- Framework ("bridge") module: adds a generic EMV merchant-presented payment QR method to bank accounts, category Accounting/Payment, depends only on account (account_qr_code_emv/__manifest__.py:5,11).
- Optional and not auto-install: no `auto_install` key (account_qr_code_emv/__manifest__.py:3-16). Installed on demand, or pulled in as a dependency by country localizations (see F).
- On its own it produces NO usable QR: the merchant-account block returns nothing (account_qr_code_emv/models/res_bank.py:51-52), eligibility says "no EMV QR available for the country of the account" (account_qr_code_emv/models/res_bank.py:127-132), and the proxy-type list is only "None" (account_qr_code_emv/models/res_bank.py:15). Country modules must supply the specifics.
- Registers the method code `emv_qr` ("EMV Merchant-Presented QR-code") with priority 30 (lower = tried earlier) (account_qr_code_emv/models/res_bank.py:121-125).
- Builds the standard payload: format indicator, dynamic-QR flag, merchant account info, merchant category (default "0000"), currency numeric code, amount, country, merchant name (max 25 chars, "NA" fallback), city (max 15 chars), optional additional-data block, closing checksum (CRC-16) (account_qr_code_emv/models/res_bank.py:57-95).
- Amount is omitted when zero; free/structured payment reference is sanitised to a restricted character set and included only if the bank account's "Include Reference" is ticked (account_qr_code_emv/models/res_bank.py:60-72).
- Renders as a 128x128 QR image via the report barcode service (account_qr_code_emv/models/res_bank.py:97-107).
- UI: an "EMV QR Settings" tab on the bank-account form (proxy type, proxy value, include reference), shown only when the country module says the setting applies (account_qr_code_emv/views/res_bank_views.xml:9-18). Default = hidden (account_qr_code_emv/models/res_bank.py:34-37).

## B. Business objects, relationships, lifecycle
- Single object extended: partner bank account (res.partner.bank), adding: include-reference flag, proxy type (default "none"), proxy value, and two computed helpers (display flag, allowed proxy keys) (account_qr_code_emv/models/res_bank.py:13-17).
- Relationship: bank account belongs to a partner (the merchant); merchant name and city are read from that partner (account_qr_code_emv/models/res_bank.py:67-68).
- Stateless: no document states of its own. Gate sequence when a QR is requested (owned by account): list methods by priority -> eligibility check -> data-completeness check -> payload (account/models/res_partner_bank.py:137-182).
- Data-completeness gate for `emv_qr`: fails with a message if merchant account info, merchant city, proxy type, or proxy value is missing (account_qr_code_emv/models/res_bank.py:109-119).
- Invoice consumption (owned by account): an invoice displays a QR only if its "display QR" condition holds, then tries the chosen or first eligible method against the invoice's bank account, residual amount and currency (account/models/account_move.py:2202-2204, 6806-6833). The chosen method is stored on the invoice after generation (account/models/account_move.py:6830-6833).

## C. Validations, automation, security, multi-company
- Currency: only currencies in the built-in numeric-code table are supported (about 50 codes, account_qr_code_emv/const.py:3-52). A currency outside this list raises a lookup failure at payload build (account_qr_code_emv/models/res_bank.py:62); friendly handling: UNKNOWN — EVIDENCE INSUFFICIENT.
- Base module defines no field constraints on proxy value; validation is delegated to country modules (e.g. l10n_br constrains proxy types/format: l10n_br/models/res_partner_bank.py:28-56; l10n_sg restricts proxy type: l10n_sg/models/res_bank.py:13-16,61).
- Display-setting compute depends on the company context (account_qr_code_emv/models/res_bank.py:34-36), so visibility is company-aware once a country module overrides it.
- No groups, ACL rows, record rules, crons or controllers in this module (skeleton: groups/rules/access/crons empty). Access follows base/account rules for bank accounts. Company scoping of bank accounts: owned by base/account; details UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- account: owns QR method selection loop, invoice QR display and stored method (account/models/res_partner_bank.py:137-190,234-270; account/models/account_move.py:6806-6833).
- Country localization modules: own the merchant-account block, proxy types, category code, additional data, eligibility by country (see F).
- Point of sale QR payment tests in l10n_test_pos_qr_payment reference `emv_qr` (l10n_test_pos_qr_payment/tests/test_pos_qr_payment.py) - POS use is outside this module's evidence; UNKNOWN — EVIDENCE INSUFFICIENT beyond that reference.
- No accounting entries, inventory, approval or e-invoicing handoffs; QR is a presentation aid for the customer to pay, and does not itself register a payment.

## E. Configuration / defaults that change outcomes
- Per bank account: proxy type, proxy value, "Include Reference" (default off) (account_qr_code_emv/models/res_bank.py:14-17).
- Method priority 30 among registered QR methods (account_qr_code_emv/models/res_bank.py:124); if another method has a lower number and is eligible, it wins when no method is forced (account/models/res_partner_bank.py:153-160).
- Default merchant category "0000" unless country module overrides (account_qr_code_emv/models/res_bank.py:57-58). Merchant name falls back to "NA"; city is mandatory (account_qr_code_emv/models/res_bank.py:67,113-114).
- Accents are stripped from names/references (account_qr_code_emv/models/res_bank.py:26-28).

## F. Effective extension path (module names only)
- Modules declaring a dependency on account_qr_code_emv: l10n_br, l10n_kh, l10n_sg, l10n_th, l10n_hk, l10n_vn (manifest grep).
- Modules that override the merchant-account hook on res.partner.bank: l10n_br, l10n_kh, l10n_sg, l10n_th, l10n_hk, l10n_vn.
- Sibling QR bridge (different method, not dependent): account_qr_code_sepa.
- Base object extended by many others (bank accounts): account (QR framework host).

## G. Not verified
- Behaviour of unsupported currencies, POS usage, bank-account company scoping: UNKNOWN — EVIDENCE INSUFFICIENT.
- Per-country payload specifics were only checked at hook-name level (not analysed in this note).
- No universal rule about which QR method an invoice ends up with is asserted; it depends on installed localizations and bank-account data.

