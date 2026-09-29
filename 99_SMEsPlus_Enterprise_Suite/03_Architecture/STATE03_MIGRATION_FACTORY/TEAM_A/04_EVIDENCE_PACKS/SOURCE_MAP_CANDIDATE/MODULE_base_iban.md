# Source Map (candidate) — `base_iban`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `base_iban` |
| Display name | IBAN Bank Accounts |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `fcc305bbf9209d30` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/base_iban/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `web`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (25): `account_qr_code_sepa`, `l10n_at`, `l10n_be`, `l10n_ca`, `l10n_ch`, `l10n_cz`, `l10n_de`, `l10n_dk`, `l10n_do`, `l10n_ec`, `l10n_es`, `l10n_fi` … (+13)
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
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
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: base_iban
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Recognises and validates IBAN bank-account numbers on partner bank accounts, reformats valid IBANs into groups of four characters, and offers helpers to split an IBAN into bank code, branch, account, check digits (base_iban/models/res_partner_bank.py:12-65, 88-128).
- Adds "IBAN" as a supported bank-account type (base_iban/models/res_partner_bank.py:91-95) and auto-detects it when the number is valid (same file:97-103).
- Live validity indicator in the UI: an IBAN field widget asks the server (after a short typing delay) whether the entered value is valid (base_iban/static/src/components/iban_widget/iban_widget.js:7-33 -> check_iban at res_partner_bank.py:136-141); applied to the bank account number on the partner bank form and on the manual bank setup wizard (base_iban/views/partner_view.xml:8-10; base_iban/views/setup_wizards_view.xml:8-10).
- Optional module (depends `account`, `web`; not auto-install) (base_iban/__manifest__.py:`depends`). Installed automatically only as dependency of others (see F). Demo bank accounts exist (base_iban/data/res_partner_bank_demo.xml).
- Function to derive the basic bank account number (BBAN) from an IBAN; refuses if the account is not IBAN type (base_iban/models/res_partner_bank.py:105-108).

## B. Business objects / lifecycle
- Extends the partner bank account object (res.partner.bank) only; no new object, no states (base_iban/models/res_partner_bank.py:88-89).
- Validation rule chain: strip spaces/punctuation; must start with a country code found in a built-in country->format table (about 75 countries); total length must equal the country format; only letters and digits; final mod-97 check-digit test must equal 1 (base_iban/models/res_partner_bank.py:68-85, table 146-218).
- On create and on edit of the number: if the value is a valid IBAN it is stored in the grouped-by-four display form; if not valid, it is stored untouched and no error is raised at that point (base_iban/models/res_partner_bank.py:110-128).
- Account type (IBAN vs standard) is derived from the number: valid => IBAN, otherwise falls back to the base behaviour (base_iban/models/res_partner_bank.py:97-103; base type computed in base/models/res_bank.py:124-126).

## C. Validations / security / multi-company
- Constraint on number: if type is IBAN, validity is enforced (base_iban/models/res_partner_bank.py:130-134). Inference: because the type becomes IBAN only when the value already validates, this constraint mainly re-checks values whose type was forced or stale; an invalid string is kept as a normal-type account instead of being rejected. (inference from :97-103, :130-134; not tested).
- Error messages tell the user the expected country format and letter meaning (base_iban/models/res_partner_bank.py:79-80).
- No ACL/record rules/groups are added by this module (manifest `data` lists only views). Access and uniqueness of accounts (per sanitized number and partner) are owned by base (base/models/res_bank.py:107).
- Company scoping of bank accounts is owned by base/`account`; UNKNOWN — EVIDENCE INSUFFICIENT for multi-company behaviour in this module.
- Data-quality note (SOURCE OBSERVATION): the table entry for Iceland starts with letters "FS" rather than the country code "IS" (base_iban/models/res_partner_bank.py:180), so an Iceland IBAN beginning "IS" may fail the "begins with country code" template comparison. Not verified by test.

## D. Handoffs
- Bank account model, type list, and sanitisation: owned by `base` (base/models/res_bank.py:82-153).
- Localisation modules import the validation/format helpers directly: l10n_ch (base_iban imported at l10n_ch/models/res_bank.py:10, l10n_ch/models/account_journal.py:8) and l10n_hu_edi (l10n_hu_edi/models/account_move.py:15).
- SEPA QR code payments use IBAN accounts: account_qr_code_sepa depends on this module and auto-installs (account_qr_code_sepa/__manifest__.py:13-15).
- No accounting entry or approval is generated.

## E. Configuration that changes outcomes
- None in settings. Behaviour depends on the built-in country table (base_iban/models/res_partner_bank.py:146-218) - changes need code, not configuration.

## F. Extension path
- Modules with base_iban as manifest dependency: account_qr_code_sepa, l10n_at, l10n_be, l10n_ca, l10n_ch, l10n_cz, l10n_de, l10n_dk, l10n_do, l10n_ec, l10n_es, l10n_fi, l10n_fr_account, l10n_gr, l10n_hu_edi, l10n_id, l10n_ie, l10n_it, l10n_lu, l10n_nl, l10n_no, l10n_pl, l10n_sk, l10n_uk, l10n_vn.
- Modules extending the bank-account object (res.partner.bank): account, account_qr_code_emv, account_qr_code_sepa, base_iban, hr, l10n_ar, l10n_au, l10n_br, l10n_ch, l10n_hk, l10n_id, l10n_kh, l10n_mx, l10n_sg, l10n_th, l10n_us, l10n_vn.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other countries' IBAN list is complete relative to current standards (table only read, not compared).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end behaviour beyond what is read in iban_widget.js (template/styling not read).

