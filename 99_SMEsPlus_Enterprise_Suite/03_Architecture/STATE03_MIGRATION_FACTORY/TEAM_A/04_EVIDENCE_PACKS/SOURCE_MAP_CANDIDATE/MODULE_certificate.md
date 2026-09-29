# Source Map (candidate) — `certificate`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `certificate` |
| Display name | Certificate |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `87a2528413121efd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/certificate/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base_setup`
- Direct dependents in 300-module list (1): `account_edi_proxy_client`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (6): `l10n_es_edi_facturae`, `l10n_es_edi_sii`, `l10n_es_edi_tbai`, `l10n_es_edi_verifactu`, `l10n_pl_edi`, `l10n_sa_edi`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / Manage certificate
- Inventory of user-facing artifacts (counts): menu items 0, views 7, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `certificate.certificate` (Certificate); `certificate.key` (Cryptographic Keys)
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 1 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `certificate.certificate` ← Community: `l10n_es_edi_facturae`, `l10n_es_edi_sii`, `l10n_es_edi_tbai`, `l10n_es_edi_verifactu`, `l10n_sa_edi`; open-license custom/third-party scanned: —
- `certificate.key` ← Community: `account_edi_proxy_client`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: —

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 2); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 48 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: certificate
Revision: 19.0.post20260921 | Scope: Odoo Community addons tree only

## A. Capabilities; core / optional / conditional
- Central store for company-owned digital certificates (X.509) and cryptographic keys (private and public), with parsing, validity checking, signing, signature verification, decryption, key generation (elliptic curve, RSA, Ed25519), and use of stored certificates for secure outbound web connections (certificate/__manifest__.py:5; certificate/models/key.py:36-37; certificate/models/certificate.py:21-22; certificate/tools/certificate_adapter.py:13-58).
- Optional, not auto-installing; depends on base_setup; category Hidden/Tools (certificate/__manifest__.py:4,15).
- Entry point in General Settings: a "Certificates and Keys" block shown only to system administrators, with buttons to the certificate list and the key list (certificate/views/res_config_settings_view.xml:8-30).
- Accepted certificate formats: DER, PEM, PKCS12 (certificate/models/certificate.py:53-58). Key files may be DER/PEM, private or public (certificate/models/key.py:70-75).
- Certificate scope selection currently has only "General"; other modules are expected to add scopes (certificate/models/certificate.py:47-52; certificate/views/certificate_views.xml:21).

## B. Business objects, relationships, lifecycle
- Certificate: name, uploaded file, optional PKCS12 password, derived PEM form, subject common name, serial number, validity start/end, load-error text, active flag, company (required, default current), scope, private-key link, optional public-key override, and issuer-certificate link (certificate/models/certificate.py:26-107).
- Key: name (default "New key"), uploaded key file, password, derived PEM, "public" flag, load-error text, active flag, company (required) (certificate/models/key.py:39-64).
- Relations: certificate -> private key (many-to-one, filtered to private keys, same company), certificate -> public key (filtered to public keys), certificate -> issuer certificate (computed; not stored) (certificate/models/certificate.py:29-46,102-107).
- Lifecycle of a certificate: upload file -> content parsed automatically -> fields filled or a loading error is shown -> when the file is PKCS12 or PEM containing a private key and none is linked, a private key record is created (or an identical one in the same company is reused) and linked -> missing CA certificates in the uploaded chain are created as extra "(CA)" certificate records, both on create and when content/password are edited (certificate/models/certificate.py:167-206,208-249,482-510,512-519).
- Validity: valid = loaded without error and current time within start-end; searchable (certificate/models/certificate.py:251-273). Issuer resolution prefers cryptographic proof of signature, else matching key identifiers, choosing the candidate with the latest expiry, same company family, self excluded (certificate/models/certificate.py:109-165,337-390).
- Records are archived rather than deleted via the active flag (certificate/models/certificate.py:93; certificate/models/key.py:57). Deleting a company deletes its certificates and keys (certificate/models/certificate.py:99; certificate/models/key.py:63).

## C. Validations, automation, security, credentials
- A certificate must load; otherwise saving fails with the loading error or a "provide the password" message (certificate/models/certificate.py:304-310).
- A linked private or public key must match the certificate's public key; otherwise "not compatible" errors (certificate/models/certificate.py:275-302). (TEST) non-matching keys rejected (certificate/tests/test_keys_certificates.py:221).
- Signing requires a valid certificate with a linked private key; expired or unloadable certificates raise a user error (certificate/models/certificate.py:681-684). Signing/verifying algorithms supported: RSA, EC, Ed25519 for signing; RSA/EC/Ed25519 verify; hashes limited to SHA-1 and SHA-256; decryption RSA only (certificate/models/key.py:12-15,239-256,258-308).
- Key generation limits: RSA exponent must be 65537 or 3; size floor is very low (the message says 512, "bytes") - a business risk to note (certificate/models/key.py:444-446). Only curve SECP256R1 for EC (certificate/models/key.py:414).
- Security access: only system administrators have any rights on certificates and keys (certificate/security/ir.model.access.csv:2-3). Multi-company rules (global, noupdate): a record is visible if it has no company or its company is a parent-of one of the user's allowed companies (certificate/security/certificate_security.xml:4-14). Company consistency of linked keys is checked automatically (certificate/models/certificate.py:24,29-32).
- Credential implications (high sensitivity): private keys are stored in the database (PEM, generated ones can be unencrypted); the key password and the PKCS12 password are stored as plain text fields (masked in forms only) (certificate/models/key.py:41,113-118,428; certificate/models/certificate.py:28; certificate/views/key_views.xml:17; certificate/views/certificate_views.xml:17). Private keys extracted from PKCS12/PEM uploads are re-stored unencrypted (certificate/models/certificate.py:194-198). The connection adapter reads certificate and key with elevated rights so that non-administrator flows can use them (certificate/tools/certificate_adapter.py:39-43).
- External service implication: the connection adapter lets other modules present a stored client certificate and trust chosen CA certificates in outbound HTTPS requests; invalid CA raises an SSL error (certificate/tools/certificate_adapter.py:31-37,45-48). (TEST) in-memory adapter loading (certificate/tests/test_keys_certificates.py:159). Which services use it: UNKNOWN — EVIDENCE INSUFFICIENT.
- (TEST) key generation and wrong password behavior (certificate/tests/test_keys_certificates.py:125-149); DER/PEM/PFX loading (151-190); validity (191); chain extraction and update (236-386); issuer proof (410).

## D. Handoffs to other modules
- Electronic-invoicing/localization and signing modules consume certificates (via scope and signing helpers): owners not identifiable within this module: UNKNOWN — EVIDENCE INSUFFICIENT. The form comments that modules adding scope options should override the selection (certificate/views/certificate_views.xml:21).
- Settings page: base_setup/base (certificate/views/res_config_settings_view.xml:6-8).
- Companies and multi-company rules: base (certificate/models/certificate.py:94-100).

## E. Configuration/defaults that change outcomes
- Default company = current company; default key name "New key"; default hash SHA-256 for signing/fingerprint; default format base64 with line breaks (certificate/models/certificate.py:98; certificate/models/key.py:39,123-135).
- Newly created keys/certificates depend on which company is active when the file is uploaded (certificate/models/certificate.py:98,486-490).
- Search filters: general scope, valid/invalid, archived (certificate/views/certificate_views.xml:56-61).

## F. Effective extension path
- Other modules add certificate scopes (selection extension), call signing/fingerprint/public-key helpers, and use the connection adapter for outbound calls (certificate/models/certificate.py:47-52,560-684; certificate/tools/certificate_adapter.py:13). Module names: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which modules use scopes, signing, or the adapter.
- UNKNOWN — EVIDENCE INSUFFICIENT: encryption-at-rest of stored key data by the platform (outside module).

