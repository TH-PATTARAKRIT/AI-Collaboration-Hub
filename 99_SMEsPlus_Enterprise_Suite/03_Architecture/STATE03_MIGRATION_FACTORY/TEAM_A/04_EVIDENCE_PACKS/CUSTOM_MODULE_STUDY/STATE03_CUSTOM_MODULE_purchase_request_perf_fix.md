> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: purchase_request_perf_fix

## 0. Header
- Module: purchase_request_perf_fix
- License (confirmed in manifest): LGPL-3 (purchase_request_perf_fix/__manifest__.py:19)
- Author (manifest): BHPRO (purchase_request_perf_fix/__manifest__.py:18)
- Version (manifest): 19.0.1.0.0 (purchase_request_perf_fix/__manifest__.py:4)
- Path: addons_Extramodule/addons/purchase_request_perf_fix
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Approval-family support patch. Replaces one computed field on purchase request lines — the list of unit-of-measure choices compatible with the product's unit — so it works when the unit model no longer has a category (manifest:5-16; models/purchase_request_line.py:101-115).
- Does not affect approval, security or workflow.

## 2. Attachment to CORE
- Depends declared: purchase_request_perf (manifest:21-23); `auto_install` is true (manifest:27), so it installs automatically when its dependency is present.
- Core Community objects touched: `uom.uom` (read; fields probed by name: models/purchase_request_line.py:48, :83; core:uom/models/uom_uom.py:41).
- Override: `_compute_filter_uom` on `purchase.request.line` (models/purchase_request_line.py:101-115): REPLACES the earlier version supplied by purchase_request_perf (same logic, different helper names; compare purchase_request_perf/models/purchase_request_line.py:193-214). No core method overridden; no ALTERS CORE CONTROL.
- Helpers: `_prlfix_root_uom` (:41-54), `_prlfix_compatible_uoms` (:56-96), a copy of helpers in purchase_request_perf (`_prl_root_uom`, `_prl_compatible_uoms`).

## 3. New objects, security, automation, external calls
- None: no new models, fields, ACLs, groups, rules, cron or external calls (manifest data empty :24).
- Performance note: the fallback branch loops over every unit of measure and walks its chain (models/purchase_request_line.py:83-89); cost grows with number of units (inference).

## 4. Odoo 19 compatibility
- `relative_uom_id` present in Community 19 (core:uom/models/uom_uom.py:41). Probed helpers `get_same_group_uoms`, `_get_relative_uoms`, `_get_compatible_uoms` are not found in core `uom/models/uom_uom.py` (text search), so branches (1) and (2) apply only if another module supplies them (models/purchase_request_line.py:64-80).
- Fallback (4) uses `category_id`, which is not a field of the Community 19 unit model (guarded by a field check, :92).
- Fallback (5) returns all units (:96) — possible widening of choices (inference).
- Redundancy: the earlier module already includes the same fix (purchase_request_perf/__manifest__.py:19-21 and models/purchase_request_line.py:193-214), so this module appears to be a duplicate of code that its dependency already contains; the effective definition is the later-loaded one (loading order inferred from dependency; not tested).

## 5. Custom-to-custom dependencies
- Depends on purchase_request_perf (and indirectly purchase_request).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the deployed database ever ran the older failing version that this module was created to correct.
