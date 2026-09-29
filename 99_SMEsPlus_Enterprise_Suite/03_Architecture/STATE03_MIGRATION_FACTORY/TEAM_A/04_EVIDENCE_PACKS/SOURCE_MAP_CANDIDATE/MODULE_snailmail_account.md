# Source Map (candidate) — `snailmail_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `snailmail_account` |
| Display name | Snail Mail - Account |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G10 / BOSS-DECISION-PENDING (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `4e2c9fc7f2f56084` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/snailmail_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `snailmail`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden/Tools / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (4): `account.move.send.batch.wizard`, `account.move`, `account.move.send`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move.send.batch.wizard`, `account.move`, `account.move.send`, `res.partner`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 34 of 35 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: snailmail_account (Snail Mail - Account)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/snailmail_account.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge that lets users send customer invoices by post ("by Post") via the snailmail letter service (snailmail_account/__manifest__.py:4-6, 10).
- Depends on account and snailmail; `auto_install` true (snailmail_account/__manifest__.py:10,14). Category hidden tooling (snailmail_account/__manifest__.py:8).
- Conditional / optional: in Accounting settings the "Snailmail" option is a module toggle (account/models/res_config_settings.py:98; account/views/res_config_settings_views.xml:130). The extra print options only show when that toggle is on (snailmail_account/views/res_config_settings_views.xml:10).
- Adds "by Post" as an invoice sending method on customers (snailmail_account/models/res_partner.py:7-9) and on the portal "my account" choices (snailmail_account/controllers/portal.py:10-12).
- Sending an invoice by post creates a letter record and queues it for printing without immediate dispatch (snailmail_account/models/account_move_send.py:51-66).
- Settings screen adds print colour, both-sides printing, cover page (company specific) and a "buy more credits" widget (snailmail_account/views/res_config_settings_views.xml:12-27).
- Batch send summary shows the number of stamps needed (snailmail_account/wizard/account_move_send_batch_wizard.py:9-21).

## B. Business objects, relationships, lifecycle
- Invoice (account.move, owned by account) -> letter (snailmail.letter, owned by snailmail) linked by model name and record id, with partner, company, sending user and the standard invoice report as template (snailmail_account/models/account_move_send.py:32-39, 59-63).
- Sending user = the author recorded for the send request, else the current user (snailmail_account/models/account_move_send.py:61).
- Deleting an invoice also deletes its letters, except during module uninstall (snailmail_account/models/account_move.py:7-13).
- Lifecycle: choose "by Post" on send -> if partner address complete, letter created after the invoice send succeeded -> printing job queued (snailmail_account/models/account_move_send.py:44-47, 51-66).
- (TEST) Posting an invoice for a partner with no email but a full address, choosing post, results in a letter linked to that invoice (snailmail_account/tests/test_snailmail_on_invoice.py:8-52).

## C. Validations, automation, security, multi-company
- Address validity: post is applicable only when the customer has street, city, postal code and country (snailmail_account/models/account_move_send.py:44-47; snailmail/models/snailmail_letter.py:471-474).
- Warning on send dialog: partners without valid address are listed; "danger" level for one invoice, "warning" for several; those invoices will not be sent (snailmail_account/models/account_move_send.py:10-26).
- Letter created only after the standard success hook and only for invoices still applicable (snailmail_account/models/account_move_send.py:51-58).
- Cover page becomes mandatory-locked for boxed/bold/striped layouts (snailmail/models/res_config_settings.py:15-30; view uses that read-only flag snailmail_account/views/res_config_settings_views.xml:22).
- Company scoping: print colour/duplex/cover settings are per company (icon hint snailmail_account/views/res_config_settings_views.xml:14,19,24; fields related to company at snailmail/models/res_config_settings.py:9-11). Letter carries invoice's company (snailmail_account/models/account_move_send.py:37).
- No groups, access entries or record rules of its own (skeleton "access": [], "rules": []).

## D. Handoffs to other modules
- account: owns invoices, send-and-print wizard, sending-method list, portal (snailmail_account/models/account_move_send.py:4-5; snailmail_account/controllers/portal.py:5; account/models/partner.py:577).
- snailmail: owns letter model, address check, printing/dispatch, company print settings, credits service (snailmail/models/snailmail_letter.py:471; snailmail/models/res_config_settings.py:9-13).
- iap (via iap_mail): credits purchase widget (snailmail_account/views/res_config_settings_views.xml:27).
- Third-party print provider: external test only (TEST) posts a rendered invoice to a staging print API for four layouts (snailmail_account/tests/test_pingen_send.py:12-81); tagged external, not standard.

## E. Configuration / defaults that change outcomes
- Customer's invoice sending method decides default (account defaults to email when unset: account/models/account_move_send.py:28).
- Company-level colour, duplex, cover options (see C).
- Available IAP credits: UNKNOWN — EVIDENCE INSUFFICIENT (handled in snailmail/iap).

## F. Effective extension path
- Modules involved: account (send framework), snailmail (letters), iap_mail. Extension points: sending method list, applicability check, success hook, alerts, batch wizard summary.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: what happens to the invoice if letter dispatch later fails (owned by snailmail).
- UNKNOWN — EVIDENCE INSUFFICIENT: cost per stamp / country coverage.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for vendor bills or credit notes (module only handles the invoice report template, snailmail_account/models/account_move_send.py:38).

