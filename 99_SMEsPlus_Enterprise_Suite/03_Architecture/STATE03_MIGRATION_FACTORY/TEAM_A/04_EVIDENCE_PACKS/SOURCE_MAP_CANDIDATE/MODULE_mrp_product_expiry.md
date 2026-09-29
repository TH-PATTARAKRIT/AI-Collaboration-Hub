# Source Map (candidate) — `mrp_product_expiry`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_product_expiry` |
| Display name | Manufacturing Expiry |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `45064f8bd028b62e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_product_expiry/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp`, `product_expiry`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Manufacturing Expiry
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `expiry.picking.confirmation`, `mrp.production`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `expiry.picking.confirmation`, `mrp.production`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 21 of 21 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: mrp_product_expiry
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived.
Manifest: "Manufacturing Expiry", described as a technical module; depends mrp + product_expiry; `auto_install: True` (mrp_product_expiry/__manifest__.py:5-12,17).

## A. Capabilities
1. Expired-component confirmation when finishing (marking done) a manufacturing order: if any component move line uses a lot flagged as expired, the "mark done" action returns a confirmation dialog instead of completing (mrp_product_expiry/models/mrp_production.py:10-31). CONDITIONAL: only when lots carry an expiration date; the lot flag is true when its expiration date is now or earlier (product_expiry/models/production_lot.py:42-48), and lots have dates only for products with "Use Expiration Date" (product_expiry/models/production_lot.py:10-11; product_expiry/models/product_product.py:38).
2. Wording of the shared confirmation wizard adapts for manufacturing: one expired lot names product and lot, several are listed (mrp_product_expiry/wizard/confirm_expiry.py:13-33; view fields mrp_product_expiry/wizard/confirm_expiry_view.xml:8-11).
3. Wizard "Confirm" buttons: from an MO re-runs mark-done with the check skipped (mrp_product_expiry/wizard/confirm_expiry.py:35-38); from a work order re-runs `record_production` with the check skipped (:40-43). Auto-installed together with its two dependencies, so it is CORE whenever both apps are present.

## B. Objects and flow
- Extends `mrp.production` (mark-done pre-check) and the transient `expiry.picking.confirmation` (adds production_ids and workorder_id) (mrp_product_expiry/wizard/confirm_expiry.py:7-11).
- Flow: user triggers mark done (mrp/models/mrp_production.py:2219-2222) -> pre-check runs first (`pre_button_mark_done`, mrp/models/mrp_production.py:2341; override mrp_product_expiry/models/mrp_production.py:10-14) -> if expired lots found, dialog opens with the lot ids preset (:23-31,33-39) -> Confirm sets a skip flag in context and calls mark done again (wizard :35-38). Cancel/discard button exists only when production_ids is set (view :29-32); the stock-picking buttons are hidden when there are no pickings (view :13-18).
- No new state on the MO; the check is a soft warning, not a block: the user can always proceed by confirming (wizard :35-38).
- Only component lots on raw-material move lines are examined (mrp_product_expiry/models/mrp_production.py:21). Finished-product lot expiry is not touched here.
- (TEST) Non-expired component: mark done returns true, no dialog; expired component (lot dated 10 days earlier): dialog for model `expiry.picking.confirmation` is returned (mrp_product_expiry/tests/test_mrp_product_expiry.py:58-103).

## C. Validations, automation, security
- The one check above; skipped when context flag `skip_expired` is set (mrp_product_expiry/models/mrp_production.py:17-19). Note the flag is an ordinary context key set by the wizard, so any caller passing it bypasses the dialog (code-level fact, :17-19).
- No ACL, rules or groups defined by this module (no security folder); the transient wizard inherits access from product_expiry and mrp models. Company scoping follows MO and lot rules (owned by mrp/stock). No multi-company logic in this module.

## D. Handoffs
- product_expiry owns the wizard base, lot expiry dates and alert flag (product_expiry/wizard/confirm_expiry.py:9-34; product_expiry/models/production_lot.py:21,42-48).
- mrp owns MO completion, backorder handling and work orders (mrp/models/mrp_production.py:2219-2226).
- No accounting or valuation handoff; no events emitted. Effect on inventory is only that the user may consume an expired lot after confirming.

## E. Configuration that changes outcomes
- Per product "Use Expiration Date" and the time settings (expiration/use/removal/alert times, TEST setup :16-24) determine lot dates; changing a lot's date changes whether the dialog appears (TEST :36-38).

## F. Effective extension path
- Extends: mrp.production, expiry.picking.confirmation. Other Community modules using the same wizard/skip flag: product_expiry (owner; picking check at product_expiry/models/stock_picking.py:13-15). No module other than this one was found inheriting `expiry.picking.confirmation`.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: which Community screen opens this dialog from a work order; `record_production` on work orders was not found in Community mrp (grep of `def record_production` returned nothing), so that branch (mrp_product_expiry/wizard/confirm_expiry.py:40-43) appears to serve an add-on outside this source tree.
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for products whose lots use "removal date" or "alert date" rather than expiration date (only the expired flag is used here).
- UNKNOWN — EVIDENCE INSUFFICIENT: subcontracting receipts and expired-lot handling (only a test named for skipping expired serials was seen, mrp_subcontracting/tests/test_subcontracting.py:1858).

