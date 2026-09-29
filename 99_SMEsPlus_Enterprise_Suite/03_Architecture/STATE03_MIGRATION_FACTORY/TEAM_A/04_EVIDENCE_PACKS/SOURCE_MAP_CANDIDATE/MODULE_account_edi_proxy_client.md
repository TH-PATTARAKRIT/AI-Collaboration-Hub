# Source Map (candidate) — `account_edi_proxy_client`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `account_edi_proxy_client` |
| Display name | Proxy features for account_edi |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `10aba264f516e983` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/account_edi_proxy_client/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `certificate`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (5): `account_peppol`, `l10n_dk_nemhandel`, `l10n_gr_edi_e_invoo`, `l10n_it_edi`, `l10n_my_edi`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 1, views 2, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `account_edi_proxy_client.user` (Account EDI proxy user)
- Objects extended from other modules (2): `certificate.key`, `res.company`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account_edi_proxy_client.user` ← Community: `account_peppol`, `account_peppol_response`, `l10n_dk_nemhandel`, `l10n_dk_nemhandel_response`, `l10n_fr_pdp`, `l10n_gr_edi_e_invoo`, `l10n_it_edi`, `l10n_my_edi`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `certificate.key`, `res.company`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 33 of 33 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — account_edi_proxy_client
Source revision: 19.0.post20260921 | Module: "Proxy features for account_edi" (account_edi_proxy_client/__manifest__.py:3) | depends: account, certificate (:14) | License LGPL-3 (:22)
Basis: static reading; no tests folder in the module. Not auto_install (no key); pulled in by dependents (see F).

## A. Capabilities and optionality
- A1. Generic infrastructure to register a company of this database as a user on an external EDI relay ("proxy") service that receives documents on its behalf; it is an enabling library, not an end-user feature by itself. account_edi_proxy_client/__manifest__.py:4-10
- A2. Provides: registration of a proxy user, encrypted data decryption, request signing/authentication, token renewal, and an admin-visible list of proxy users. account_edi_proxy_client/models/account_edi_proxy_user.py:168-243; account_edi_proxy_client/models/account_edi_proxy_auth.py:12-74
- A3. Conditional operating modes per user: production, test, demo. Demo simulates registration and blocks any real proxy call. account_edi_proxy_client/models/account_edi_proxy_user.py:57-64,179-181,107-108
- A4. Optional (installed only as dependency): manifests depending on it are account_peppol, l10n_dk_nemhandel, l10n_gr_edi_e_invoo, l10n_it_edi, l10n_my_edi (grep of manifests). Proxy types and URLs are supplied by those modules (selection is empty here). account_edi_proxy_client/models/account_edi_proxy_user.py:56,72-74
- A5. Note: it does NOT depend on account_edi; the two modules are independent (manifest :14).
- A6. Menu "EDI Proxy Users" under invoicing, shown only in technical/debug mode; list is read-only. account_edi_proxy_client/views/account_edi_proxy_user_views.xml:31,50-55

## B. Objects, relationships, lifecycle
- B1. Proxy user (account_edi_proxy_client.user): belongs to one company, has a client id issued by the relay, an external identification (typically tax id), a private key record, a refresh token, mode, proxy type, active flag, out-of-sync markers. account_edi_proxy_client/models/account_edi_proxy_user.py:32-64
- B2. Company holds the list of its proxy users. account_edi_proxy_client/models/res_company.py:9
- B3. Private key is a certificate.key record generated per user (RSA), named by type, mode and company; the public part is sent to the relay so files can be encrypted for this database. account_edi_proxy_client/models/account_edi_proxy_user.py:174-177,157-166
- B4. Lifecycle: register (generate key, ask relay to create user unless demo) -> create local record -> use -> token renewed on expiry -> deactivated if relay reports the user is unknown. account_edi_proxy_client/models/account_edi_proxy_user.py:168-214,139-145,216-233
- B5. Registration refused locally if a user already exists for the same company, type, and mode (non-demo path); relay-side duplicate errors are surfaced as user messages. account_edi_proxy_client/models/account_edi_proxy_user.py:184-189,199-204
- B6. Token model: every call is signed; the shared secret (refresh token) expires (comment says 24h) and is renewed on relay request; a fallback asymmetric signature exists for resync after a restored/copied database. account_edi_proxy_client/models/account_edi_proxy_auth.py:14-18,47-50,63-72; account_edi_proxy_client/models/account_edi_proxy_user.py:139-142
- B7. Decryption path: symmetric key is decrypted with the user's private key, then the payload is decrypted (symmetric, via an added helper on certificate.key). account_edi_proxy_client/models/account_edi_proxy_user.py:235-243; account_edi_proxy_client/models/key.py:9-12

## C. Validations, security, multi-company
- C1. Uniqueness: client id is globally unique; one active user per company + proxy type + mode. account_edi_proxy_client/models/account_edi_proxy_user.py:66-70
- C2. Request handling: 30-second timeout; connection, HTTP and JSON failures become a generic connection error; relay error payloads become user-visible messages; invalid-signature message warns that duplicated databases may be the cause. account_edi_proxy_client/models/account_edi_proxy_user.py:14,110-134,146-152
- C3. Refresh token field readable only by system administrators; auth class reads it with elevated rights. account_edi_proxy_client/models/account_edi_proxy_user.py:47; account_edi_proxy_client/models/account_edi_proxy_auth.py:23-24
- C4. Access: system administrators full rights; invoicing group read-only. account_edi_proxy_client/security/ir.model.access.csv:2-3
- C5. Company rule: a user record is visible when its company is a parent of (or equal to) one of the current user's allowed companies. account_edi_proxy_client/security/account_edi_proxy_client_security.xml:4-8 (rule installed with noupdate=0, :3)
- C6. Token renewal takes a row lock and simply exits if the row is already locked; a commit is issued before retrying the request. account_edi_proxy_client/models/account_edi_proxy_user.py:141,224-226
- C7. Demo mode is the last-barrier block in the request function, in addition to caller-side handling. account_edi_proxy_client/models/account_edi_proxy_user.py:106-108

## D. Handoffs
- D1. Owner of actual document exchange, proxy URLs, identification and proxy types: dependent modules (account_peppol, l10n_it_edi, l10n_dk_nemhandel, l10n_gr_edi_e_invoo, l10n_my_edi; also modules that extend the user model - see F). Methods marked "to extend/override" in this module. account_edi_proxy_client/models/account_edi_proxy_user.py:72-74,88-94
- D2. Key storage: certificate module (certificate.key). account_edi_proxy_client/__manifest__.py:14; account_edi_proxy_client/models/key.py:6-8
- D3. Database identity sent to relay: config parameter database.uuid plus company id. account_edi_proxy_client/models/account_edi_proxy_user.py:161-162
- D4. Post-install hook writes a system parameter "account_edi_proxy_client.demo"; no reader of it found in the addons tree. account_edi_proxy_client/__init__.py:3-4. UNKNOWN — EVIDENCE INSUFFICIENT on its purpose.
- D5. No accounting entries or stock movements; audit trail is limited to server log warnings/errors on failures. account_edi_proxy_client/models/account_edi_proxy_user.py:120,232

## E. Configuration that changes outcomes
- E1. Mode per user (prod/test/demo) selects relay URL through dependent modules' URL map and enables/blocks live calls. account_edi_proxy_client/models/account_edi_proxy_user.py:76-81,107
- E2. Timeout constant 30s. E3. Authentication type (hmac or asymmetric) chosen per call. account_edi_proxy_client/models/account_edi_proxy_auth.py:20,63-72
- E4. Database UUID and a copied database can lead to token conflicts; neutralization is mentioned in comment. account_edi_proxy_client/models/account_edi_proxy_auth.py:47-50

## F. Extension path (module names only)
- account_edi_proxy_client.user is extended by: account_peppol, account_peppol_response, l10n_dk_nemhandel, l10n_dk_nemhandel_response, l10n_fr_pdp, l10n_gr_edi_e_invoo, l10n_it_edi, l10n_my_edi.
- certificate.key is extended by: account_edi_proxy_client only (inherit grep).
- res.company: account_edi_proxy_client is among many (account, account_peppol, l10n_* etc.).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: relay-side behaviour, endpoints beyond the paths named in the code (create_user v2, renew_token v1), and service terms.
- UNKNOWN — EVIDENCE INSUFFICIENT: how token-out-of-sync and token-sync-version fields (:48-55) are used; no reader in this module.
- UNKNOWN — EVIDENCE INSUFFICIENT: encryption algorithm details of certificate.key (owned by certificate module; not read).

