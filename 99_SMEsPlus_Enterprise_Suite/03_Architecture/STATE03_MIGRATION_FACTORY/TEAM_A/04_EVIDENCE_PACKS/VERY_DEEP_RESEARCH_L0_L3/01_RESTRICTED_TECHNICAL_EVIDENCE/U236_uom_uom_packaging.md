# U236 — uom.uom and UoM-Based Packaging: Relative-Factor Unit Tree, product.uom Packaging Link, Conversion and Rounding, Downstream Field Names
## RESTRICTED TECHNICAL EVIDENCE

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

**Status**: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
**Unit**: U236
**Revision**: Odoo Community 19.0.post20260921 (Community addons only)
**Date**: 2026-10-03
**Method**: static reading of source files plus repository-wide text search over the Community addons tree; no Odoo process started; no database queried (database facts quoted from U02 are attributed to U02)
**Source file**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/uom/models/uom_uom.py`
**SHA-256**: `360db3a982171a655d686eecdf929f93fca43749e5b7a92a49356bc345042d2b`
**Lines**: 230
**Source file**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/product/models/product_uom.py`
**SHA-256**: `551d39d709a8131d43c1c3f0c7c7f16061ae6178952ef205a8997994bfaa4ead`
**Lines**: 32
**Secondary source**: `.../product/models/uom_uom.py` (inherit of uom.uom: barcode link and action)
**Secondary source**: `.../stock/models/product.py` (inherit of uom.uom: package type, routes, ratio write lock; product category packaging reserve method)
**Secondary source**: `.../stock/models/stock_move.py`, `stock_quant.py`, `stock_rule.py`, `stock_orderpoint.py` (packaging unit fields, reservation, routing, replenishment multiple)
**Secondary source**: `.../sale/models/sale_order_line.py`, `.../purchase/models/purchase_order_line.py`, `.../account/models/account_move_line.py` (line unit fields and allowed units)
**Secondary source**: `.../uom/data/uom_data.xml`, `.../uom/security/uom_security.xml`, `.../uom/security/ir.model.access.csv`, `.../uom/__manifest__.py`, `.../uom/models/__init__.py`, `.../uom/views/uom_uom_views.xml`
**Secondary source**: `.../uom/i18n/is.po`, `.../purchase/i18n/en_AU.po` (leftover translation entries, used only as evidence of removed names)
**Secondary source**: `.../product/models/product_template.py`, `product_product.py`, `res_config_settings.py`, `views/uom_views.xml`, `report/product_packaging.xml`, `report/product_reports.xml`, `security/ir.model.access.csv`
**Secondary source**: `.../stock/views/uom_uom_views.xml`, `.../stock/report/packaging_barcode.xml`, `.../stock/report/stock_report_views.xml`
**Secondary source**: `.../point_of_sale/models/product_uom.py`, `uom.py`, `product_template.py`, `pos_session.py` and static JS files (packaging barcode consumption)
**Secondary source**: `.../hr_timesheet/models/uom_uom.py`, `.../account/models/uom_uom.py`, `.../l10n_th/__manifest__.py`
**Secondary source**: `odoo/tools/float_utils.py` (path relative to the release root: rounding methods)

---

## 0. Evidence conventions and reading guide

### 0.1 Posture
- Static read of the read-only Community source tree for revision 19.0.post20260921. No Odoo process was started and no database was queried.
- Only Community addons were read. No Enterprise, Extra_Thailand, Extra_Module_scgl or OEEL content was read.
- Pointer convention: `module/path:line` is relative to `<release root>/odoo/addons/`; `odoo/tools/...` is relative to `<release root>`; `<release root>` is `.../Odoo Community/odoo-19.0.post20260921/`. Line numbers follow the numbering of the file as read (`wc -l` is quoted for the two main files; the reader tool shows one extra trailing empty line number).
- No business data is reproduced. Database facts are reused from U02 only and are attributed.

### 0.2 Evidence labels
| Label | Meaning |
|---|---|
| FACT | read directly at the cited path and line |
| DERIVED | arithmetic or logic derived from FACT inputs, worked by hand, not executed |
| U02 | fact reused from existing evidence file U02 with attribution, not re-queried here |
| GREP | presence or absence established by a repository-wide text search; the terms and scope are given beside the statement |
| UNVERIFIED-FROM-SOURCE | statement about v16/v17 behaviour taken from general knowledge or leftover translation text; the v19 tree cannot confirm it |
| RT | needs execution or database observation, not performed |
| UNKNOWN | evidence insufficient |

### 0.3 Absence-search protocol
A name is called absent only after a search over `*.py`, `*.xml`, `*.js`, `*.csv`, `*.json`, `*.scss`, `*.html` and `*.ts` files under `odoo/addons` returned no production identifier. Terms searched: `uom.category`, `uom_type`, `factor_inv`, `uom_po_id`, `product_uom_category_id`, `qty_multiple`, `product.packaging`, and a category field on the unit model.
Qualifier: legacy wording survives (the word "category" in one docstring, one QWeb comment and several test names or comments) and leftover translation entries exist; both are inventoried in CAP-U236-07 and are not identifiers.

### 0.4 Wording
This file reports what the source shows. It carries no rating, no percentage and no approval wording; the only verification wording is the status label at the top.

### 0.5 Function-ID
Function-IDs are not yet assigned; every capability carries `FUNCTION MAPPING REQUIRED`.

### 0.6 Reading guide (scope item to capability)
| Capability | Scope item | Subject |
|---|---|---|
| CAP-U236-01 | 1 | uom.uom v19 field inventory, reference-unit tree concept, constraints and defaults |
| CAP-U236-02 | 2 | conversion engine: quantity, price, rounding methods, unrelated units, failure flag |
| CAP-U236-03 | 3 | packaging replacement: additional units, product.uom barcode link, routing, replenishment multiple, reservation |
| CAP-U236-04 | 4 | unit field naming on transactional models (product_uom versus product_uom_id) |
| CAP-U236-05 | 5 | shipped data, access rights, edit restrictions once units are used |
| CAP-U236-06 | 6 | Thai deployment note |
| CAP-U236-07 | 7 | migration flags against v16 and v17 |

Cross-reference (template-level unit fields): parallel unit U231 covers `product.template` unit fields in depth. One line only: `product.template.uom_id` (required, tracked, default `uom.product_uom_unit`) and `product.template.uom_ids` ("Packagings") are declared at `product/models/product_template.py:118-122`; see U231.

---

## CAP-U236-01 uom.uom v19: field inventory, tree of units without categories, constraints and defaults

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
`uom.uom` is the global catalogue of units of measure. In v19 it is a **tree of units**: each unit may name one reference unit (`relative_uom_id`) and states how many of that reference unit it contains (`relative_factor`, label "Contains"). A stored recursive field (`factor`, label "Absolute Quantity") multiplies the ratios along the path to the top-level unit. There is **no unit category**, no bigger/smaller/reference unit type and no inverse ratio field. The reference-unit concept is therefore per unit (a unit's own parent), not per category. A top-level unit has no reference and must carry a ratio of exactly one. Rounding is not per unit: one global precision applies to all units.

### D2 Architecture / data / object relationships
Model header and fields (verbatim):

```python
# uom/models/uom_uom.py:17-22
class UomUom(models.Model):
    _name = 'uom.uom'
    _description = 'Product Unit of Measure'
    _parent_name = 'relative_uom_id'
    _parent_store = True
    _order = 'sequence, relative_uom_id, id'

# uom/models/uom_uom.py:34-49
name = fields.Char('Unit Name', required=True, translate=True)
sequence = fields.Integer(compute="_compute_sequence", store=True, readonly=False, precompute=True)
relative_factor = fields.Float(
    'Contains', default=1.0, digits=0, required=True,  # force NUMERIC with unlimited precision
    help='How much bigger or smaller this unit is compared to the reference UoM for this unit')
rounding = fields.Float('Rounding Precision', compute="_compute_rounding")
active = fields.Boolean('Active', default=True, help="Uncheck the active field to disable a unit of measure without deleting it.")
relative_uom_id = fields.Many2one('uom.uom', 'Reference Unit', ondelete='cascade', index='btree_not_null')
related_uom_ids = fields.One2many('uom.uom', 'relative_uom_id', 'Related UoMs')
factor = fields.Float('Absolute Quantity', digits=0, compute='_compute_factor', recursive=True, store=True)
parent_path = fields.Char(index=True)

_factor_gt_zero = models.Constraint(
    'CHECK (relative_factor!=0)',
    'The conversion ratio for a unit of measure cannot be 0!',
)
```

The model is a plain model: no `_inherit` in the base definition, no mail.thread, no tracking, no company field (FACT: `uom/models/uom_uom.py:17-44`). The module has one model file (`uom/models/__init__.py:4` imports only `uom_uom`) and depends only on `base` (`uom/__manifest__.py:8`).

Presence and absence table (scope item 1):

| Name | v19 status | Evidence |
|---|---|---|
| `category_id` on uom.uom | ABSENT | FACT field list `uom/models/uom_uom.py:34-44`; GREP no production identifier |
| `uom.category` model | ABSENT | FACT single model file `uom/models/__init__.py:4`; GREP no production identifier; leftover translation entries only (see CAP-U236-07) |
| `uom_type` | ABSENT | FACT field list; GREP; leftover translation entries only |
| `factor` | PRESENT: stored computed Float "Absolute Quantity", `digits=0`, `recursive=True` | `uom/models/uom_uom.py:43`, compute L69-75 |
| `factor_inv` | ABSENT | FACT field list; GREP; leftover translation entries only |
| `relative_factor` | PRESENT: "Contains", required, default 1.0, `digits=0` | `uom/models/uom_uom.py:36-38` |
| `relative_uom_id` | PRESENT: "Reference Unit", Many2one to uom.uom, `ondelete='cascade'`, `index='btree_not_null'`, not required | `uom/models/uom_uom.py:41` |
| `related_uom_ids` | PRESENT: inverse One2many "Related UoMs" | `uom/models/uom_uom.py:42` |
| `rounding` | PRESENT as non-stored computed Float "Rounding Precision" with no `@api.depends` | `uom/models/uom_uom.py:39`, compute L62-67 |
| `active` | PRESENT: Boolean, default True | `uom/models/uom_uom.py:40` |
| `sequence` | PRESENT: computed, stored, `readonly=False`, `precompute=True` | `uom/models/uom_uom.py:35`, compute L53-60 |
| `parent_path` | PRESENT: Char, indexed (parent store) | `uom/models/uom_uom.py:44`, `_parent_store` L21 |
| `name` | PRESENT: Char "Unit Name", required, translatable | `uom/models/uom_uom.py:34` |
| `uom_po_id`, `product_uom_category_id`, `qty_multiple` | ABSENT | GREP no production identifier |

Extension fields declared on uom.uom by other Community modules (13 files declare an inherit of uom.uom; GREP forms searched: single-quoted, double-quoted, list forms):

| Module | File | Declaration (pointer) |
|---|---|---|
| product | `product/models/uom_uom.py` | `product_uom_ids` One2many to product.uom, "Barcodes", callable domain (L19); `action_open_packaging_barcodes` (L21-30) |
| stock | `stock/models/product.py` | `package_type_id` (L1370), `route_ids` related (L1371), ratio write lock (L1373-1404), `_adjust_uom_quantities` (L1406-1418) |
| account | `account/models/uom_uom.py` | `fiscal_country_codes` computed Char (L41); unit-code table `UOM_TO_UNECE_CODE` (L6-35); `_get_unece_code` (L48-53); `_get_uom_from_unece_code` (L55-59) |
| point_of_sale | `point_of_sale/models/uom.py` | `is_pos_groupable` Boolean (L8); loader methods (L10-18) |
| hr_timesheet | `hr_timesheet/models/uom_uom.py` | `timesheet_widget` Char (L20); `_unprotected_uom_xml_ids` override (see CAP-U236-05) |
| l10n_ar | `l10n_ar/models/uom_uom.py` | `l10n_ar_afip_code` (L8) |
| l10n_cl | `l10n_cl/models/uom_uom.py` | `l10n_cl_sii_code` (L9) |
| l10n_eg_edi_eta | `l10n_eg_edi_eta/models/uom_uom.py` | `l10n_eg_unit_code_id` (L18; extension class at L16) |
| l10n_hu_edi | `l10n_hu_edi/models/uom_uom.py` | `l10n_hu_edi_code` Selection (L9) |
| l10n_id_efaktur_coretax | `l10n_id_efaktur_coretax/models/uom_uom.py` | `l10n_id_uom_code` (L8) |
| l10n_es_edi_facturae | `l10n_es_edi_facturae/models/uom_uom.py` | `l10n_es_edi_facturae_uom_code` Selection (L7) |
| l10n_in | `l10n_in/models/uom_uom.py` | `l10n_in_code` (L8) |
| l10n_tr_nilvera | `l10n_tr_nilvera/models/uom_uom.py` | extension class at L31; the field-pattern search found no field declaration (content beyond the class line not read) |

No Thai localization extension of uom.uom exists (GREP over `l10n_th`, see CAP-U236-06).

Views carrying the unit fields are listed in CAP-U236-03 (section on views). Per-line field names on other models are in CAP-U236-04.

### D3 Source / technical / workflow logic
Compute and constraint code (verbatim):

```python
# uom/models/uom_uom.py:53-60
@api.depends('relative_factor')
def _compute_sequence(self):
    for uom in self:
        if uom.id and uom.sequence:
            # Only set a default sequence before the record creation, or on module update if
            # there is no value.
            continue
        uom.sequence = min(int(uom.relative_factor * 100.0), 1000)

# uom/models/uom_uom.py:62-67
def _compute_rounding(self):
    """ All Units of Measure share the same rounding precision defined in 'Product Unit'.
        Set in a compute to ensure compatibility with previous calls to `uom.rounding`.
    """
    decimal_precision = self.env['decimal.precision'].precision_get('Product Unit')
    self.rounding = 10 ** -decimal_precision

# uom/models/uom_uom.py:69-75
@api.depends('relative_factor', 'relative_uom_id', 'relative_uom_id.factor')
def _compute_factor(self):
    for uom in self:
        if uom.relative_uom_id:
            uom.factor = uom.relative_factor * uom.relative_uom_id.factor
        else:
            uom.factor = uom.relative_factor

# uom/models/uom_uom.py:97-101
@api.constrains('relative_factor', 'relative_uom_id')
def _check_factor(self):
    for uom in self:
        if not uom.relative_uom_id and uom.relative_factor != 1.0:
            raise UserError(_("Reference unit of measure is missing."))
```

Reading of the code:
- Absolute quantity (`factor`) is the unit's own ratio times the absolute quantity of its reference unit, or the own ratio when there is no reference. It is recomputed when the ratio, the reference or the reference's absolute quantity changes. Because the dependency chain passes through `relative_uom_id.factor` and the field is declared `recursive=True`, descendants follow their parent (descendant recompute on a populated tree is RT).
- The default `sequence` of a new unit is `min(int(relative_factor * 100.0), 1000)`, set only when the record has no id or no sequence yet; ordering of the unit list is `sequence, relative_uom_id, id` (L22).
- `rounding` is not stored and has no dependency declaration; the compute assigns `10 ** -digits` of the decimal precision named "Product Unit" to every record of the recordset. The shipped precision is 2 digits (`uom/data/uom_data.xml:5-8`), so the value is 0.01 in shipped data (DERIVED). Changing the decimal precision changes the rounding of all units at once.
- `round`, `compare` and `is_zero` (L116-137) each call `ensure_one` and read the 'Product Unit' digits directly (not the `rounding` field).
- Display name (L139-145): with context key `formatted_display_name` and a reference unit set, the display name becomes the unit name, a tab, then `--<relative_factor> <reference name>--`.
- Onchange warning (L79-93): when the unit is a protected shipped unit and its `create_date` is older than one day, changing `relative_factor` returns a warning ("Some critical fields have been modified on %s.\nNote that existing data WON'T be updated by this change.\n\nAs units of measure impact the whole system, this may cause critical issues.\nTherefore, changing core units of measure in a running database is not recommended.").
- Delete guard and protected-unit rule: see CAP-U236-05.

Constraints and defaults:

| Item | Value | Pointer |
|---|---|---|
| ratio default | 1.0 | `uom/models/uom_uom.py:37` |
| active default | True | `uom/models/uom_uom.py:40` |
| SQL check | `relative_factor!=0`, message "The conversion ratio for a unit of measure cannot be 0!" | `uom/models/uom_uom.py:46-49` |
| root ratio rule | no reference and ratio not 1.0 raises UserError "Reference unit of measure is missing." | `uom/models/uom_uom.py:97-101` |
| negative ratio | no constraint read forbids it | UNKNOWN (RT) |
| reference cycle | no recursion constraint declared in the model file; ORM handling for parent-store models not traced | UNKNOWN (RT) |
| reference required | no; `relative_uom_id` is optional | `uom/models/uom_uom.py:41` |
| removed constraints | `rounding_gt_zero` and `factor_reference_is_one` do not exist in code; stale translation entries only | `uom/i18n/is.po:248-254` |

State diagram:
- `(none) -> Active [create; active defaults to true; ratio defaults to 1.0]`
- `Active -> Archived [manual; 16 of the 30 shipped units start archived]`
- `Archived -> Active [manual]`
- `Active -> Deleted [refused for protected shipped units, archive instead; other units deletable; dependants cascade at database level]`
- `Reference or ratio changed -> Absolute quantity recomputed [stored recursive compute]`
- `Top-level unit with ratio other than 1 -> rejected`
- `Ratio 0 -> rejected`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Create a unit with a name, an optional reference unit and a ratio; the absolute quantity is computed and stored; the unit is then selectable on products and lines. Shipped data creates 30 units, 23 of them with a reference unit. |
| 2 Reversal / cancel / negative path | Archive instead of delete (help text on `active`); protected shipped units cannot be deleted; correcting a ratio recomputes the stored absolute quantity (descendant recompute RT). |
| 3 Multi-company / data-scope | uom.uom has no company field and no record rule is defined for it (FACT model definition; GREP over XML found no reference to the model xml-id); global master data. |
| 4 Side effects / cross-module triggers | Stored absolute quantity feeds the sale, purchase and invoice SQL reports; 13 files extend the model with code fields and loaders; stock adds a ratio write lock; point of sale loads units including archived ones. |
| 5 Configuration and optionality | Group `uom.group_uom` exposes multi-unit features in the UI (CAP-U236-05); the 'Product Unit' decimal precision is the single rounding source; module depends only on `base`. |
| 6 Validation and constraints | SQL check on ratio zero; root ratio must be 1.0; protected delete guard; negative ratio and reference cycles not covered by any constraint read (UNKNOWN). |
| 7 Roles and permissions | Nine ACL rows for uom.uom across seven CSV files (table in CAP-U236-05); no record rule. |
| 8 Scheduled / automated | NOT APPLICABLE — the uom manifest data list holds only data, security and view files (`uom/__manifest__.py:13-18`); no scheduled action found. |
| 9 Exception and failure behaviour | UserError for root ratio and protected delete; constraint message for ratio zero; no explicit failure path for negative ratios or cycles. |
| 10 Accounting, stock, audit, security, compliance | No tracking or chatter on units; unit changes are not audited at model level; stock blocks ratio edits when open moves or stock use the unit (CAP-U236-05). |

### DB reconciliation (configuration/structure only)
From U02 (CAP-U02-04, restored database, not re-queried in U236): `uom_uom` has 30 rows with no category column, `product_uom` has 0 rows, two ACL rows in module uom, Product Unit precision 2, constraints `uom_uom_factor_gt_zero` and `product_uom_barcode_uniq` present. Source side: the data file declares 30 unit records (GREP count of `model="uom.uom"` in `uom/data/uom_data.xml` is 30; 23 carry `relative_uom_id`; 16 carry `active` false).

### Unknown / Runtime list
- UNKNOWN: whether a negative ratio is accepted (no constraint read).
- UNKNOWN: how a reference cycle is handled (no model-level constraint; ORM parent-store behaviour not traced).
- RT: recompute of descendants' absolute quantity on a populated tree after a parent's ratio changes.
- UNKNOWN: client components under `uom/static/src/components` (manifest L20-24) not read.

---

## CAP-U236-02 Conversion engine: quantity, price, packaging multiple, rounding, unrelated units

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Quantities and prices on lines, moves, bills of materials, pricelists and reports are converted between units by pure helper methods on uom.uom. In v19 the conversion multiplies by the source unit's absolute quantity and divides by the target's; there is **no category test and no common-root test inside the conversion**. A separate helper (`_has_common_reference`) tests whether two units share a root and is called only by specific consumers (timesheet, e-invoice import, label printing, one e-invoice template).

### D2 Architecture / data / object relationships
- Inputs: stored `factor` of both units; global `rounding` (from decimal precision "Product Unit").
- Methods on uom.uom: `_compute_quantity` (L147-176), `_check_qty` (L178-194), `_compute_price` (L196-203), `_has_common_reference` (L218-230), `round`/`compare`/`is_zero` (L116-137).
- Rounding implementation: `odoo/tools/float_utils.py` `float_round` with the `RoundingMethod` literal.
- SQL reports re-implement conversion using the stored `factor` (see 3.9).

### D3 Source / technical / workflow logic

#### 3.1 `_compute_quantity`
```python
# uom/models/uom_uom.py:147-176 (docstring L155-161 omitted here)
def _compute_quantity(
    self,
    qty: float,
    to_unit: Self,
    round: bool = True,
    rounding_method: RoundingMethod = 'UP',
    raise_if_failure: bool = True,
) -> float:
    if not self or not qty:
        return qty
    self.ensure_one()

    if self == to_unit:
        amount = qty
    else:
        amount = qty * self.factor
        if to_unit:
            amount = amount / to_unit.factor

    if to_unit and round:
        amount = tools.float_round(amount, precision_rounding=to_unit.rounding, rounding_method=rounding_method)

    return amount
```
Decision list:
1. Empty source recordset or falsy quantity: the quantity is handed back unchanged, before `ensure_one` (L162-163).
2. A source recordset with more than one record raises at `ensure_one` (L164), unless step 1 returned first.
3. Same unit: the amount is the quantity, no scaling (L166-167).
4. Different units: `qty * self.factor`, then division by `to_unit.factor` when a target is given (L169-171).
5. With a target and `round` true, the amount is rounded at the target's `rounding` using `rounding_method` (default 'UP'); this includes the same-unit case (L173-174).
6. With no target there is no division and no rounding; the quantity is returned scaled by the source's absolute quantity.
7. The parameter `raise_if_failure` is declared (L153) but never read in the body; its docstring text (L155-161) still describes a category failure. See 3.6.

#### 3.2 Rounding methods
```python
# odoo/tools/float_utils.py:8
RoundingMethod = Literal['UP', 'DOWN', 'HALF-UP', 'HALF-DOWN', 'HALF-EVEN']

# odoo/tools/float_utils.py:132-151 (inside float_round)
epsilon = 2**(epsilon_magnitude - 50)

match rounding_method:
    case 'HALF-UP':  # 0.5 rounds away from 0
        result = round(normalized_value + math.copysign(epsilon, normalized_value))
    case 'HALF-EVEN':  # 0.5 rounds towards closest even number
        integral = math.floor(normalized_value)
        remainder = abs(normalized_value - integral)
        is_half = abs(0.5 - remainder) < epsilon
        # if is_half & integral is odd, add odd bit to make it even
        result = integral + (integral & 1) if is_half else round(normalized_value)
    case 'HALF-DOWN':  # 0.5 rounds towards 0
        result = round(normalized_value - math.copysign(epsilon, normalized_value))
    case 'UP':  # round to number furthest from zero
        result = math.trunc(normalized_value + math.copysign(1 - epsilon, normalized_value))
    case 'DOWN':  # round to number closest to zero
        result = math.trunc(normalized_value + math.copysign(epsilon, normalized_value))
    case _:
        msg = f"unknown rounding method: {rounding_method}"
        raise ValueError(msg)
```

| Method | Behaviour (float_utils docstring L90-96) | In-repo use named in this unit |
|---|---|---|
| 'UP' | always away from zero | default of `_compute_quantity` (L152) |
| 'DOWN' | always towards zero | reservation base-to-move conversion (stock_quant.py:865-867); `_check_qty` reservation call (stock_quant.py:853) |
| 'HALF-UP' | closest, ties away from zero | default of `float_round` (L76) and of `_check_qty` and `round`; stock.move `product_qty`; reservation back-conversion |
| 'HALF-DOWN' | closest, ties towards zero | no use found in this unit's reads |
| 'HALF-EVEN' | closest, ties to even | no use found in this unit's reads |

Other facts: a zero value or zero precision returns 0.0 (L101-102); an unknown method raises ValueError (L149-151). The `_check_qty` docstring lists only three methods (L181) while five exist (stale text). `uom/models/uom_uom.py:14` imports the type only under TYPE_CHECKING.

#### 3.3 `_compute_price`
```python
# uom/models/uom_uom.py:196-203
def _compute_price(self, price: float, to_unit: Self) -> float:
    self.ensure_one()
    if not self or not price or not to_unit or self == to_unit:
        return price
    amount = price * to_unit.factor
    if to_unit:
        amount = amount / self.factor
    return amount
```
Facts: `ensure_one` runs first (L197), so an empty source recordset raises before the emptiness check in L198; price conversion is the inverse of quantity conversion (multiply by the target's absolute quantity, divide by the source's); no rounding is applied. Callers (examples, FACT from searches): `purchase/models/purchase_order_line.py` (L169, L464, L482, L684), `product/models/product_template.py:760`, `product/models/product_product.py` (L312, L332, L1125), `product/models/product_pricelist_item.py:597`, `account/models/product.py:260`.

#### 3.4 `_check_qty` (packaging multiple)
```python
# uom/models/uom_uom.py:178-194 (docstring omitted)
def _check_qty(self, product_qty, uom_id, rounding_method="HALF-UP"):
    self.ensure_one()
    packaging_qty = self._compute_quantity(1, uom_id)
    if self == uom_id:
        return product_qty
    # We do not use the modulo operator to check if qty is a mltiple of q. Indeed the quantity
    # per package might be a float, leading to incorrect results. For example:
    # 8 % 1.6 = 1.5999999999999996
    # 5.4 % 1.8 = 2.220446049250313e-16
    if product_qty and packaging_qty:
        product_qty = float_round(product_qty / packaging_qty, precision_rounding=1.0,
                              rounding_method=rounding_method) * packaging_qty
    return product_qty
```
Facts:
- `self` is the packaging unit and `uom_id` the base unit: `packaging_qty` is the size of one packaging expressed in the base unit, computed with the default 'UP' rounding at the base unit's precision (L184), before the same-unit check (L185-186).
- The quantity is divided by that size, rounded to a whole number of packagings with the chosen method, and multiplied back (L191-193). The comment (L187-190) explains why the modulo operator is not used.
- Only production caller found: `stock/models/stock_quant.py:853` inside `_get_reserve_quantity` (L834), as `self.env.context.get('packaging_uom_id')._check_qty(min(quantity, available_quantity), product_id.uom_id, "DOWN")`, gated at L852 by the context key `packaging_uom_id` and by the product category field `packaging_reserve_method == "full"`; the context is supplied by `stock/models/stock_move.py:1926`. Test references: `uom/tests/test_uom.py:41-48`; comment at `stock/tests/test_quant.py:691`. See CAP-U236-03.

#### 3.5 `round`, `compare`, `is_zero`
`uom/models/uom_uom.py:116-137`: each calls `ensure_one`, reads the digits of decimal precision 'Product Unit', and delegates to `float_round`, `float_compare`, `float_is_zero`. `round` defaults to 'HALF-UP'. They ignore any per-unit setting because none exists.

#### 3.6 `raise_if_failure`
- Declared at `uom/models/uom_uom.py:153`; never read in the body (L162-176); docstring L158-160 still says conversion raises "if the conversion is not possible (different UomUom category)" and otherwise returns the initial quantity.
- Seven callers still pass `raise_if_failure=False` (GREP, `*.py`, `*.xml`, `*.js`): `product/models/product_pricelist.py:217`, `mrp/models/product.py:324` (also `round=False`), `mrp/models/stock_orderpoint.py:192`, `hr_timesheet/models/hr_timesheet.py:498`, `hr_timesheet/models/project_task.py:280`, `hr_timesheet/models/project_project.py:190`, `sale_timesheet/models/hr_timesheet.py:225`. No caller passes `True`.
- Consequence (FACT from the code path): the flag changes nothing in v19; a conversion between units of different roots does not raise and does not return the initial quantity, it returns a computed number.

#### 3.7 Unrelated units and `_has_common_reference`
```python
# uom/models/uom_uom.py:218-230
def _has_common_reference(self, other_uom: Self) -> bool:
    """ Check if `self` and `other_uom` have a common reference unit """
    self.ensure_one()
    other_uom.ensure_one()
    self_path = self.parent_path.split('/')
    other_path = other_uom.parent_path.split('/')
    common_path = []
    for self_parent, other_parent in zip(self_path, other_path):
        if self_parent == other_parent:
            common_path.append(self_parent)
        else:
            break
    return bool(common_path)
```
- It compares the `parent_path` segments from the top; two units are related when the first segment (the top-level unit id) matches.
- Conversion itself never calls it. A conversion between units of different trees therefore returns a number silently (DERIVED from the code path; not executed).
- Occurrences found by GREP (all file types under `odoo/addons`, excluding the definition): **14 call sites**, 8 in Python and 6 in QWeb/XML:

| # | Pointer | Use shown on the cited line |
|---|---|---|
| 1 | `sale_timesheet/models/product_template.py:60` | default unit compared with the hour unit |
| 2 | `sale_timesheet/models/sale_order_line.py:49` | `is_time_product`: line unit shares a root with `uom.product_uom_hour` |
| 3 | `sale_timesheet/models/sale_order_line.py:100` | unit differs from the company time unit but shares its root |
| 4 | `sale_timesheet/models/product_product.py:25` | default unit compared with the hour unit |
| 5 | `account_edi_ubl_cii/models/account_edi_common.py:976` | invoice-import unit not sharing a root with the product's template unit |
| 6 | `account_edi_ubl_cii/models/account_edi_common.py:1410` | import line unit not sharing a root with the product unit |
| 7 | `stock/wizard/product_label_layout.py:60` | line unit shares a root with `uom_unit` |
| 8 | `stock/wizard/stock_lot_label_layout.py:33` | move line unit shares a root with `uom_unit` |
| 9 | `mrp/report/mrp_zebra_production_templates.xml:9` | QWeb: product unit shares a root with `uom_unit` |
| 10 | `mrp/report/mrp_production_templates.xml:147` | QWeb: same test (label logic L147-153) |
| 11 | `mrp/report/mrp_production_templates.xml:181` | QWeb: same test, prints 1.0 |
| 12 | `stock/report/picking_templates.xml:11` | QWeb: same test |
| 13 | `stock/report/picking_templates.xml:54` | QWeb: same test |
| 14 | `l10n_it_edi/data/invoice_it_template.xml:21` | QWeb: unit element written when the line unit does not share a root with `uom.product_uom_unit` |

- UBL import behaviour (`account_edi_ubl_cii/models/account_edi_common.py:968-978` and `1400-1425`): an incompatible unit leaves the unit empty (L978; `force_empty` L1421) and logs "The Unit of Measure '%(uom)s' (from unit code '%(code)s') was ignored on the line for product '%(product)s' because it is not compatible with the product's Unit of Measure '%(product_uom)s'. The UoM was left empty." (L1411-1420).
- Reading: `_has_common_reference` is the v19 replacement for the former category-equality test; it is opt-in per caller, not enforced by the conversion.

#### 3.8 Rounding policy at callers (examples read in this unit)
- stock.move `product_qty` ("Real Quantity", digits 0, stored, base unit): declared `stock/models/stock_move.py:54-57`, computed at L380-384 with HALF-UP; the inverse `_set_product_qty` (L485-490) raises a programming-error UserError.
- Move line preparation `_prepare_move_line_vals` (L1872-1892) and `_split` (L2367-2411) use HALF-UP round-trip checks; the fallback unit is the product's base unit or `force_split_uom_id` (L2363-2364, L2394).
- `_adjust_uom_quantities` (`stock/models/product.py:1406-1418`): when the parameter `stock.propagate_uom` is not '1' the quantity is converted to the quant's unit and the procurement unit becomes that unit; otherwise it is converted to the procurement unit; both conversions use HALF-UP.
- Purchase line: `product_uom_qty` ("Total Quantity", computed, stored; declared L24) is `product_uom_id._compute_quantity(product_qty, product_id.uom_id)` when the units differ, else `product_qty` (L499-505); `price_unit_product_uom` L167-169; supplier-quantity conversions HALF-UP (L665, L677); supplier price `seller.product_uom_id._compute_price(seller.price, product_uom)` (L684).
- Quant reservation round trip (`stock/models/stock_quant.py:865-867`, comment L857-864): when not strict and the move unit differs from the product's base unit, the quantity is converted base to move unit with 'DOWN' and back with 'HALF-UP'.

#### 3.9 SQL reports use the stored absolute quantity
`sale/report/sale_report.py` (L100-104, L150-151), `account/report/account_invoice_report.py` (L72, L105, L119, L123-127), `purchase/report/purchase_report.py` (L82-93, L130, L146) convert quantities in SQL with the stored `factor` of the line unit and the product's base unit. This is why `factor` is stored. Exact SQL text is not reproduced here.

#### 3.10 Worked examples (DERIVED from shipped data, worked by hand, not executed)
| Case | Basis in shipped data | Calculation | Result |
|---|---|---|---|
| 2 kg to g, default 'UP' | kg: contains 1000 of g (top-level, absolute 1) so absolute 1000 | 2 x 1000 / 1 | 2000.0 |
| 90 Minutes to Hours, default 'UP', precision 0.01 | Minutes: contains 0.0166667 of Hours (top-level, absolute 1) | 90 x 0.0166667 / 1 = 1.500003, rounded up at 0.01 | 1.51 |
| same, 'HALF-UP' | as above | 1.500003 rounded half-up at 0.01 | 1.5 |
| `_compute_price(12, Units)` called on Dozens | Dozens: contains 12 Units (absolute 12); Units absolute 1 | 12 x 1 / 12 | 1.0 |
| 1 kg to m (units in different trees) | kg absolute 1000; m: 100 cm, cm: 10 mm, so m absolute 1000 | 1 x 1000 / 1000 | 1.0 and no error |
The Minutes ratio 0.0166667 is an approximation of one sixtieth stored in the shipped data (`uom/data/uom_data.xml:38-42`); the 1.51 result follows from the default upward rounding (RT to confirm by execution).

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Convert between two related units: multiply by the source's absolute quantity, divide by the target's, round at the target's rounding (default upward). |
| 2 Reversal / cancel / negative path | The reverse conversion uses the same formula with the units swapped; rounding of negative values is symmetric because UP and DOWN use the sign of the value (FACT `float_utils.py:145-148`); a zero quantity is returned untouched. |
| 3 Multi-company / data-scope | Global: units and the decimal precision record carry no company; methods read no company data. |
| 4 Side effects / cross-module triggers | The methods are pure (no writes); callers choose the rounding method; SQL reports repeat the conversion with the stored factor. |
| 5 Configuration and optionality | Decimal precision 'Product Unit' sets the one rounding precision; parameters `round`, `rounding_method`; stock parameter `stock.propagate_uom` affects `_adjust_uom_quantities`. |
| 6 Validation and constraints | `ensure_one` on `_compute_quantity` (after the empty/zero return), `_compute_price` (first statement), `_check_qty`, `_has_common_reference`, `round`, `compare`, `is_zero`; `float_round` raises ValueError for an unknown method. |
| 7 Roles and permissions | The methods run in the caller's environment; reading a unit needs read access (CAP-U236-05); `_filter_protected_uoms` uses sudo for the model-data lookup. |
| 8 Scheduled / automated | NOT APPLICABLE — pure helper methods; no scheduled action in this capability. |
| 9 Exception and failure behaviour | No exception for units of different roots; `raise_if_failure` is ignored; no explicit guard against a zero absolute quantity (the ratio constraint makes it non-zero in normal data, DERIVED). |
| 10 Accounting, stock, audit, security, compliance | Rounding policy drives booked quantities: HALF-UP for stock.move `product_qty`, DOWN then HALF-UP for reservation, default UP elsewhere; one global precision limits per-unit drift. |

### DB reconciliation (configuration/structure only)
From U02 (not re-queried): decimal precision `Product Unit` is 2 digits, so `rounding` evaluates to 0.01 in the restored database; unit rows match the data file (30). No other database fact is used for this capability.

### Unknown / Runtime list
- RT: all worked examples are hand calculations; execution needed to confirm results.
- RT: behaviour of converting between units of different roots is derived from reading; execution needed to confirm.
- UNKNOWN: `_compute_quantity` callers inside Enterprise or non-Community modules are out of scope.

---

## CAP-U236-03 Packaging replacement: additional units, product.uom barcode link, routing, replenishment multiple, reservation

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
In v19 there is no `product.packaging` model (GREP, CAP-U236-07). A "packaging" is expressed by four cooperating pieces:
1. A **unit of measure** that is a multiple of the product's base unit (a unit whose "Contains" ratio points at a reference unit), made selectable on the product through `product.template.uom_ids` (label "Packagings", `product/models/product_template.py:118-122`).
2. A **barcode link record** `product.uom` (description "Link between products and their UoMs") joining one unit, one product variant and one unique barcode (`product/models/product_uom.py:8-18`).
3. A **transfer-line memory** (`stock.move.packaging_uom_id` and `packaging_uom_qty`) that remembers which unit the order line used and that unit's quantity, for routing, putaway, reservation and reports.
4. **Ordering helpers**: the reorder rule field `replenishment_uom_id` (rounds the order quantity up to a multiple of a unit) and the product-category setting `packaging_reserve_method` (reserve only whole packagings or allow partial).

The quantity per packaging is **not stored on the link record**; it is the shared unit's `relative_factor` ("Contains") and stored absolute quantity `factor`. A unit is shared by all products that use it, so one pack-of-six unit serves every product sold in sixes.

### D2 Architecture / data / object relationships

| Element | Pointer | Fact |
|---|---|---|
| `product.uom` model | `product/models/product_uom.py:8-11` | `_name = 'product.uom'`; `_rec_name = 'barcode'` |
| `uom_id` | `product/models/product_uom.py:13` | Many2one `uom.uom` "Unit", required, indexed, `ondelete='cascade'` |
| `product_id` | `product/models/product_uom.py:14` | Many2one `product.product` "Product", required, indexed, `ondelete='cascade'` |
| `barcode` | `product/models/product_uom.py:15` | Char, `index='btree_not_null'`, required, `copy=False` |
| `company_id` | `product/models/product_uom.py:16` | Many2one `res.company`, default current company |
| uniqueness | `product/models/product_uom.py:18-26` | SQL `unique(barcode)` plus Python check against `product.product` barcodes |
| `product_uom_ids` on unit | `product/models/uom_uom.py:19` | One2many `product.uom` "Barcodes" with a context-driven domain (L11-17) |
| `action_open_packaging_barcodes` | `product/models/uom_uom.py:21-30` | window action "Packaging Barcodes" on `product.uom`, view `product.product_uom_list_view` |
| `uom_ids` on template | `product/models/product_template.py:120-122` | Many2many `uom.uom` "Packagings", domain `id != uom_id` |
| `product_uom_ids` on variant | `product/models/product_product.py:48` | One2many `product.uom` "Unit Barcode", stored |
| `package_type_id` on unit | `stock/models/product.py:1370` | Many2one `stock.package.type` "Package Type" (L1371 adds related `route_ids`) |
| `packaging_reserve_method` | `stock/models/product.py:1326-1330` | Selection on `product.category`: 'full' "Reserve Only Full Packagings", 'partial' "Reserve Partial Packagings", default 'partial' |
| `replenishment_uom_id` | `stock/models/stock_orderpoint.py:64-66` | Many2one on `stock.warehouse.orderpoint`, label "Multiple" |

Absent in v19 (GREP, scope per section 0.3): model `product.packaging`; fields `product_packaging_id`, `product_packaging_qty` on sale, purchase and stock lines; `qty_multiple` on the unit; the `packaging_ids` One2many on the template.

Verbatim: the link model.

```python
# product/models/product_uom.py:8-26
class ProductUom(models.Model):
    _name = 'product.uom'
    _description = 'Link between products and their UoMs'
    _rec_name = 'barcode'

    uom_id = fields.Many2one('uom.uom', 'Unit', required=True, index=True, ondelete='cascade')
    product_id = fields.Many2one('product.product', 'Product', required=True, index=True, ondelete='cascade')
    barcode = fields.Char(index='btree_not_null', required=True, copy=False)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self: self.env.company)

    _barcode_uniq = models.Constraint('unique(barcode)', 'A barcode can only be assigned to one packaging.')

    @api.constrains('barcode')
    def _check_barcode_uniqueness(self):
        """ With GS1 nomenclature, products and packagings use the same pattern. Therefore, we need
        to ensure the uniqueness between products' barcodes and packagings' ones"""
        domain = [('barcode', 'in', [b for b in self.mapped('barcode') if b])]
        if self.env['product.product'].search_count(domain, limit=1):
            raise ValidationError(_("A product already uses the barcode"))
```

Display name: `product/models/product_uom.py:28-32`: when context `show_variant_name` is set the name is "{barcode} for: {product.display_name}", otherwise the standard name.

### D3 Source / technical / workflow logic

#### 3.1 Barcode link: uniqueness
- Database level: `unique(barcode)` across all `product.uom` rows (message "A barcode can only be assigned to one packaging.").
- Python level (`_check_barcode_uniqueness`, L20-26): the barcodes of the written records are searched on `product.product`; a hit raises ValidationError "A product already uses the barcode". The search runs in the caller's environment, not elevated (FACT L25); whether a product barcode hidden by a company rule would be missed is RT.
- The reverse direction (a product barcode that equals an existing packaging barcode) is not checked in `product/models/product_uom.py`; whether the product model checks it was not traced in this unit (UNKNOWN).

#### 3.2 Views and labels that expose the link
- `product/views/uom_views.xml` L3-13: editable list "Packaging Barcodes" (fields product_id, barcode, uom_id readonly when `default_uom_id` is in context, optional hide); L15-35: unit form gets a smart button calling `action_open_packaging_barcodes` with `context="{'default_uom_id': id}"`.
- `stock/views/uom_uom_views.xml` L3-12: list adds `package_type_id` (group `stock.group_tracking_lot`); L14-35: form shows `package_type_id` (L20-23), `product_uom_ids` with widget `many2many_barcode_tags` (L24-31, invisible unless the context carries a product and the unit exists) and `route_ids` (L32, group `stock.group_adv_location`).
- `uom/views/uom_uom_views.xml` (62 lines): list "Units & Packagings" (L7-12); form with the label "Quantity" for `relative_factor` (L25) and name/ratio/reference readonly when a product context is present and the record exists (L24, L27, L28); search view with an Archived filter (L37-49); action `product_uom_form_action` (L51-61).
- PDF label: template `report_packagingbarcode` (`product/report/product_packaging.xml`): L14 unit name, L19 product display name, L25-27 "Qty:" followed by the unit's `relative_factor` and its `relative_uom_id` (group `uom.group_uom`), L33-34 barcode. Bound as "Packaging Barcodes (PDF)" on `product.uom` (`product/report/product_reports.xml:63-72`, binding at L70).
- ZPL label: template `label_packaging_barcode_view` (`stock/report/packaging_barcode.xml`): L9 unit name, L11 product display name, L13 "Qty:" followed by `relative_factor` and the unit's own name (group `uom.group_uom`), L14-17 barcode. Bound as "Packaging Barcodes (ZPL)" (`stock/report/stock_report_views.xml:157-165`, binding L163).
- Difference to note (FACT): the PDF label prints the reference unit after the figure, the ZPL label prints the unit's own name after the figure.

#### 3.3 Transfer-line packaging memory
```python
# stock/models/stock_move.py:194-195 (declaration, condensed from two statements)
packaging_uom_id = fields.Many2one('uom.uom', 'Packaging', help="Packaging unit from sale or purchase orders", compute='_compute_packaging_uom_id', precompute=True, store=True)
packaging_uom_qty = fields.Float('Packaging Quantity', help="Quantity in the packaging unit", compute='_compute_packaging_uom_qty', store=True)
```
- Defaults (`stock/models/stock_move.py:741-750`): `_compute_packaging_uom_id` (depends `product_uom`) sets the move's own unit; `_compute_packaging_uom_qty` (depends `product_uom_qty`, `packaging_uom_id`) converts the demand from the move unit into the packaging unit.
- Overrides that set the packaging unit from the originating order line:

| Module | Pointer | Source of the unit |
|---|---|---|
| sale_stock | `sale_stock/models/stock.py:19-24` | `sale_line_id.product_uom_id` (depends `sale_line_id`, `sale_line_id.product_uom_id`) |
| sale_stock | `sale_stock/models/sale_order_line.py:308` | procurement value `'packaging_uom_id': self.product_uom_id` |
| purchase_stock | `purchase_stock/models/stock_move.py:32-37` | `purchase_line_id.product_uom_id` |
| mrp | `mrp/models/stock_move.py:72-77` | `production_id.product_uom_id` |
| sale_mrp | `sale_mrp/models/stock_move.py:9-14` | phantom BoM line: reset to the move's own unit |
| purchase_mrp | `purchase_mrp/models/stock_move.py:12-17` | phantom BoM line: reset to the move's own unit |

#### 3.4 Consumers of `packaging_uom_id` (non-test, GREP over `*.py`, `*.xml`)
| Consumer | Pointer | Behaviour |
|---|---|---|
| push rule chaining | `stock/models/stock_move.py:1214` (def), L1233, L1240 | routes of related package types are added; the packaging unit is copied to the next move |
| procurement values | `stock/models/stock_move.py:1829-1868` | with no routes on the move, routes come from the package types of the related result packages (L1838-1841); L1865 passes `packaging_uom_id` |
| reservation context | `stock/models/stock_move.py:1926` | `with_context(packaging_uom_id=...)` before `_get_reserve_quantity` |
| procure method | `stock/models/stock_move.py:2572-2603` | `_adjust_procure_method` passes the packaging unit to `_search_rule` (L2595) |
| putaway on move line | `stock/models/stock_move_line.py:289` | `packaging=sml.move_id.packaging_uom_id` |
| aggregated delivery-slip lines | `stock/models/stock_move_line.py:862-876`, `910-941` | packaging quantity and ordered packaging quantity rounded with the packaging unit's `round` |
| new package type | `stock/models/stock_move_line.py:1105-1107` | a new package takes `package_type_id` from the packaging unit when exactly one is found |
| putaway strategy | `stock/models/stock_location.py:297-311` | `_get_putaway_strategy(product, quantity, package, packaging, additional_qty)`: package type is the package's, else the packaging unit's; rules filtered by `package_type_ids` (L319-322) |
| product putaway | `stock/models/product_strategy.py:133-139` | same derivation in `_get_putaway_location` |
| rule search | `stock/models/stock_rule.py` L516-518, L539-553, L582, L603-608, L631, L677 | see 3.5 |
| reports | `stock/report/report_deliveryslip.xml` L91-103, L260-263, L284-296 (all group `uom.group_uom`); `stock/report/report_stockpicking_operations.xml:149-150` | packaging quantity and unit name printed |
| views | `stock/views/stock_move_views.xml:79`, `stock/views/stock_picking_views.xml:291` | optional hidden column, group `uom.group_uom` |

#### 3.5 Route selection by packaging
```python
# stock/models/stock_rule.py:550-563
        if route_ids:
            res = Rule.search(Domain('route_id', 'in', route_ids.ids) & domain, order='route_sequence, sequence', limit=1)
        if not res and packaging_uom_id:
            packaging_routes = packaging_uom_id.package_type_id.route_ids
            if packaging_routes:
                res = Rule.search(Domain('route_id', 'in', packaging_routes.ids) & domain, order='route_sequence, sequence', limit=1)
        if not res:
            product_routes = product_id.route_ids | product_id.categ_id.total_route_ids
            if product_routes:
                res = Rule.search(Domain('route_id', 'in', product_routes.ids) & domain, order='route_sequence, sequence', limit=1)
        if not res and warehouse_id:
            warehouse_routes = warehouse_id.route_ids
            if warehouse_routes:
                res = Rule.search(Domain('route_id', 'in', warehouse_routes.ids) & domain, order='route_sequence, sequence', limit=1)
```
- Order (FACT): explicit routes, then routes of the packaging unit's package type, then product and category routes, then warehouse routes; each search `order='route_sequence, sequence'`, `limit=1`.
- `_search_rule_for_warehouses` (L508-534) includes packaging routes in the union of valid route ids (L516-518) and orders groups by `route_sequence:min, sequence:min`. `_get_rule` (L566-640) calls the search at L580-586 and uses a nested resolver `get_rule_for_routes` (L603-613, packaging branch L607-608). `_get_push_rule` (L667-679) calls `_search_rule` at L677.
- Route eligibility: `stock.package.type.route_ids` is a Many2many to `stock.route` restricted to routes with `package_type_selectable` true (`stock/models/stock_package_type.py:39`; the Boolean "Applicable on Package Type" at `stock/models/stock_location.py:530`).
- Unrelated: `sale_selectable` sits on `stock.route` (`sale_stock/models/stock.py:12`); it is not a packaging field.

#### 3.6 Replenishment multiple
```python
# stock/models/stock_orderpoint.py:807-814
def _get_multiple_rounded_qty(self, qty_to_order):
    replenishment_multiple = self.replenishment_uom_id or self._get_replenishment_multiple_alternative(qty_to_order)
    if replenishment_multiple:
        # Replace the UP by DOWN if we don't want to order more quantity than product_max_qty
        qty_to_order = self.product_id.uom_id._compute_quantity(qty_to_order, replenishment_multiple)
        qty_to_order = fields.Float.round(qty_to_order, precision_digits=0, rounding_method="UP")
        qty_to_order = replenishment_multiple._compute_quantity(qty_to_order, self.product_id.uom_id)
    return qty_to_order
```
- Field: `replenishment_uom_id` (L64-66), help "The procurement quantity will be rounded up to a multiple of this unit/packaging. If it is not set, it is not rounded."; allowed set `allowed_replenishment_uom_ids` (L63) computed at L213-218 from `product_id.uom_ids`, plus `seller_ids.product_uom_id` when the rule action is 'buy'; mrp adds the BoM unit for 'manufacture' (`mrp/models/stock_orderpoint.py:87-94`).
- Alternative hook `_get_replenishment_multiple_alternative`: stock returns False (L454-459); mrp returns the BoM `product_uom_id` when a manufacture rule is effective (`mrp/models/stock_orderpoint.py:165-171`); purchase_stock returns the selected supplier's `product_uom_id` (`purchase_stock/models/stock.py:304-320`).
- Caller `_get_qty_to_order` (L461-476; call at L475).
- Behaviour: the quantity is converted to the multiple's unit, rounded up to a whole count (precision 0), and converted back. The quantity can only grow (UP) in this method; the comment in the source names a possible DOWN variant (FACT L810).

#### 3.7 Reservation of whole packagings
- Category field `packaging_reserve_method` (`stock/models/product.py:1326-1330`).
- In `_get_reserve_quantity` (`stock/models/stock_quant.py` L834; `self = self.sudo()` at L844), L851-853 (verbatim above in this section's reading): when context `packaging_uom_id` is present and the template's category method is 'full', the available quantity becomes `packaging_uom_id._check_qty(min(quantity, available_quantity), product_id.uom_id, "DOWN")`.
- `_check_qty` has this one production caller; other callers are tests (`uom/tests/test_uom.py:41-48`, `stock/tests/test_quant.py:691`).
- Round trip for a non-base move unit at L857-867 (CAP-U236-02, 3.8).

```python
# stock/models/stock_quant.py:851-853
        # do full packaging reservation when it's needed
        if self.env.context.get('packaging_uom_id') and product_id.product_tmpl_id.categ_id.packaging_reserve_method == "full":
            available_quantity = self.env.context.get('packaging_uom_id')._check_qty(min(quantity, available_quantity), product_id.uom_id, "DOWN")
```

#### 3.8 Selectable units on lines (`allowed_uom_ids` pattern)
Category domains are replaced by a per-line computed list "allowed units" = the product's base unit plus its additional units, plus context-specific extras:

| Model | Pointer | Content |
|---|---|---|
| sale.order.line | `sale/models/sale_order_line.py:539-542` | union (recordset operator) of `product_id.uom_id` and `product_id.uom_ids`; depends product_id, product_id.uom_id, product_id.uom_ids |
| stock.move | `stock/models/stock_move.py:66` (field), L202-205 (compute) | union including sudo seller units |
| stock.move.line | `stock/models/stock_move_line.py:31` (field), L101-103 (compute) | base unit, additional units and supplier units read with elevated rights (L103) |
| mrp stock.move | `mrp/models/stock_move.py:66-70` | adds `product_id.bom_ids.product_uom_id` |
| account.move.line | `account/models/account_move_line.py:375` (field), L882-885 (compute), L887-895 (`_compute_product_uom_id`) | allowed units and default unit |
| purchase.order.line | `purchase/models/purchase_order_line.py:42` (field), L411-417 (compute) | base unit, additional units and filtered supplier units (L417) |

#### 3.9 Point of sale
- `point_of_sale/models/product_uom.py` (16 lines): `_inherit = ['product.uom', 'pos.load.mixin']`; loaded fields `id, barcode, product_id, uom_id` (L9-10); domain `product_id in <loaded product ids>` (L12-15). Loaded through `point_of_sale/models/product_template.py:139-151` and L166 (key `product.uom`), registered in the session model list (`point_of_sale/models/pos_session.py:142`).
- Units are loaded with `active_test=False` (`point_of_sale/models/uom.py:10-12`); `is_pos_groupable` is declared at L8.
- Client: `point_of_sale/static/src/app/models/data_service_options.js:51` (field list), `pos_order_line.js:40-59` (a scanned packaging barcode sets the quantity from the packaging unit's `factor` divided by the template unit's `factor`), `product_screen.js:225, 241`, `pos_store.js:773` (lookups by barcode in the `product.uom` collection).

State diagram:
- `(none) -> Packaging barcode record [create with unit, product, barcode; barcode must be unique]`
- `Packaging barcode record -> Deleted [unit or product deleted; cascade]`
- `Transfer line created -> Packaging unit = own unit [default]`
- `Transfer line from order line -> Packaging unit = order line unit [sale, purchase, manufacturing]`
- `Transfer line from phantom BoM line -> Packaging unit = own unit [reset]`
- `Reservation with packaging unit and category method full -> Reserved quantity rounded DOWN to whole packagings`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Add an additional unit to a product, give it a barcode through the link record, sell or buy in that unit; the transfer line remembers the unit and quantity; routing, putaway, labels and reports use it. |
| 2 Reversal / cancel / negative path | Deleting the unit or the product removes the barcode links (cascade); archived units stay loadable in point of sale (`active_test=False`); reservation rounds DOWN, never up. |
| 3 Multi-company / data-scope | The link record carries a company field defaulting to the current company, but barcode uniqueness is global; no record rule was found for it (GREP over XML and CSV for the model xml-id gave only the two access rows). |
| 4 Side effects / cross-module triggers | sale_stock, purchase_stock, mrp, sale_mrp, purchase_mrp override the packaging unit; stock routing, putaway, package creation and reports consume it; point of sale loads the link records and scans them. |
| 5 Configuration and optionality | Group `uom.group_uom` shows the columns and settings; category `packaging_reserve_method` default 'partial'; reorder-rule `replenishment_uom_id` optional (empty means no rounding unless an alternative hook returns a unit); `stock.propagate_uom` parameter affects unit propagation (CAP-U236-02, 3.8). |
| 6 Validation and constraints | Barcode unique (SQL and Python); unit required; product required; route eligibility limited to `package_type_selectable` routes; no constraint ties the barcode to a unit that the template lists in `uom_ids` (GREP: none found, UNKNOWN beyond the files read). |
| 7 Roles and permissions | Two access rows for `product.uom` (product manager full, internal users read; CAP-U236-05); unit access per CAP-U236-05. |
| 8 Scheduled / automated | The reorder-rule multiple applies inside the replenishment run; no packaging-specific scheduled action found. |
| 9 Exception and failure behaviour | ValidationError on a barcode already used by a product; database unique error on a duplicate packaging barcode; the multiple helper does not raise for unrelated units (CAP-U236-02). |
| 10 Accounting, stock, audit, security, compliance | Packaging unit and quantity are stored on the move for delivery slips and operations reports; the quantity per packaging is derived from the shared unit, so changing a unit's ratio changes every packaging that uses it (stock blocks this when open moves or stock use the unit, CAP-U236-05). |

### DB reconciliation (configuration/structure only)
From U02 (not re-queried): `product_uom` table exists with 0 rows and carries the unique barcode constraint named `product_uom_barcode_uniq`; no category column on `uom_uom`. A restored database with no packaging rows cannot show the link records in use (RT for populated behaviour).

### Validation of existing evidence
- U215 FLAG-002 (purchase order line has no packaging fields): CONFIRMED by GREP. `purchase/models/purchase_order_line.py` declares a unit field and an allowed-units list (L42-43) and no packaging selection or packaging quantity. The only traces are stale translation entries `purchase/i18n/en_AU.po:1695` (`purchase_order_line__product_packaging_id`), L1700 (`...product_packaging_qty`), L1782 (`model_product_packaging`), L1825.

### Unknown / Runtime list
- RT: barcode lookup behaviour for a product barcode created after a packaging barcode with the same value.
- RT: effect of the non-elevated product search in the Python barcode check under company rules.
- UNKNOWN: whether any module other than point of sale reads `product.uom` rows on the client.
- UNKNOWN: Enterprise or other non-Community consumers of the packaging fields.

---

## CAP-U236-04 Unit field naming on transactional models

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Every transactional model that carries a quantity names the unit of that quantity in a Many2one to `uom.uom`. v19 does not use one name everywhere. Integrations and migrations need a per-model mapping. There is no separate `product_uom_id` table with pointers; each model holds its own Many2one column.

### D2 Architecture / data / object relationships

#### Unsuffixed name `product_uom` (3 models, GREP over `*.py` for `product_uom = fields.Many2one`)
| Model | Pointer | Notes |
|---|---|---|
| stock.move | `stock/models/stock_move.py:67-70` | movement unit; quantities `product_uom_qty` "Demand" and `product_qty` (base unit) |
| stock.warehouse.orderpoint | `stock/models/stock_orderpoint.py:53-54` | related to the product's base unit |
| repair.order | `repair/models/repair.py:92` | |

#### Suffixed name `product_uom_id` (declarations read, GREP over `*.py`)
| Model | Pointer | Notes |
|---|---|---|
| sale.order.line | `sale/models/sale_order_line.py:132-137` | quantity `product_uom_qty` "Quantity" |
| purchase.order.line | `purchase/models/purchase_order_line.py:43` | plain Many2one with allowed-units domain, `ondelete='restrict'`; ordered quantity `product_qty`, `product_uom_qty` "Total Quantity" is computed in the base unit |
| account.move.line | `account/models/account_move_line.py:376-382` | |
| stock.move.line | `stock/models/stock_move_line.py:32` | quantities `quantity` and `quantity_product_uom` |
| stock.quant | `stock/models/stock_quant.py:52` | |
| stock.scrap | `stock/models/stock_scrap.py:25` | |
| stock.lot | `stock/models/stock_lot.py:49` | |
| stock.storage.category.capacity | `stock/models/stock_storage_category.py:61` | related to product base unit |
| product.replenish wizard | `stock/wizard/product_replenish.py:19` | |
| mrp.production | `mrp/models/mrp_production.py:117` | |
| mrp.bom | `mrp/models/mrp_bom.py:46` | |
| mrp.bom.line | `mrp/models/mrp_bom.py:691` | |
| mrp.bom.byproduct | `mrp/models/mrp_bom.py:858` | |
| mrp.unbuild | `mrp/models/mrp_unbuild.py:32` | |
| mrp.workcenter capacity | `mrp/models/mrp_workcenter.py:628` | |
| mrp.workorder | `mrp/models/mrp_workorder.py:42` | related to the production |
| mrp.production.split wizard | `mrp/wizard/mrp_production_split.py:23` | related to the production |
| mrp consumption warning line | `mrp/wizard/mrp_consumption_warning.py:98` | related to the product base unit |
| product.supplierinfo | `product/models/product_supplierinfo.py:25` | |
| purchase.requisition.line | `purchase_requisition/models/purchase_requisition.py:171` | |
| hr.expense | `hr_expense/models/hr_expense.py:106` | |
| account.analytic.line | `analytic/models/analytic_line.py:189` | |
| sale.order.template.line | `sale_management/models/sale_order_template_line.py:45` | |
| sale project milestone | `sale_project/models/project_milestone.py:36` | related to the sale line unit |
| pos.order.line | `point_of_sale/models/pos_order.py:1652` | related to the product base unit |
| purchase.bill.line.match | `purchase/models/purchase_bill_line_match.py:30` | related; the line unit is `line_uom_id` at L21 |
| SQL reports | `sale/report/sale_report.py:63`, `purchase/report/purchase_report.py:30`, `account/report/account_invoice_report.py:47` | read-only report fields |

#### Other names
| Name | Model | Pointer |
|---|---|---|
| `uom_id` | product.template (base unit) | `product/models/product_template.py:118` |
| `uom_id` | product.uom (link) | `product/models/product_uom.py:13` |
| `uom_id` | stock return wizard line | `stock/wizard/stock_picking_return.py:15` |
| `uom_id` | hr_timesheet project update | `hr_timesheet/models/project_update.py:13` |
| `line_uom_id` | purchase.bill.line.match | `purchase/models/purchase_bill_line_match.py:21` |
| `associated_uom_id` | barcode rule (GS1) | `barcodes_gs1_nomenclature/models/barcode_rule.py:51` |
| `packaging_uom_id` | stock.move | `stock/models/stock_move.py:194` |
| `replenishment_uom_id` | stock.warehouse.orderpoint | `stock/models/stock_orderpoint.py:64` |

Template-level unit fields: see parallel unit U231 (one-line cross-reference in section 0.6).

### D3 Source / technical / workflow logic
- The three-versus-many split is a naming fact (FACT at the pointers above). The unsuffixed `product_uom` is used by the movement model, the reorder rule and the repair order; the other transactional models read in this unit use the suffixed form; the template uses `uom_id`.
- Code that is generic across models must therefore select the field name per model. Examples that already do this: `stock/models/product.py:1389-1398` (write lock searches `product_uom` on moves and `product_uom_id` on move lines).
- Related unit fields (`related='product_id.uom_id'`) exist on several models (orderpoint, storage capacity, consumption warning, point-of-sale line, bill-line match); they follow the product's base unit and carry no own value.
- The units pointed at are the single `uom.uom` catalogue; there is no category to compare. Cross-model comparison uses `_has_common_reference` (CAP-U236-02, 3.7).

State diagram: NOT APPLICABLE — naming inventory, no lifecycle.

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | A movement, order line or invoice line names its unit in the model's own field; quantities are in that unit. |
| 2 Reversal / cancel / negative path | NOT APPLICABLE — naming inventory; reversal behaviour belongs to the owning models. |
| 3 Multi-company / data-scope | The unit catalogue is global; the field names carry no company aspect. |
| 4 Side effects / cross-module triggers | Many related fields mirror the product's base unit; SQL reports expose their own `product_uom_id` columns. |
| 5 Configuration and optionality | Visibility of unit columns depends on group `uom.group_uom` in most views (CAP-U236-05). |
| 6 Validation and constraints | Domains restrict a line unit to its allowed-units list (CAP-U236-03, 3.8); purchase line uses `ondelete='restrict'` (L43). |
| 7 Roles and permissions | Per model; not unit-specific. |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure behaviour | NOT APPLICABLE — no behaviour in the naming itself. |
| 10 Accounting, stock, audit, security, compliance | Unit mismatch between a line and the product base unit is converted at booking with the rounding policy in CAP-U236-02, 3.8. |

### DB reconciliation (configuration/structure only)
Not performed for this capability: U02 reconciled structure for `uom_uom` and `product_uom` only; column names on transactional tables were not queried.

### Unknown / Runtime list
- UNKNOWN: unit field names on models in modules not read in this unit (the table lists declarations found by the GREP above).
- RT: actual column names in the restored database for the listed models.

---

## CAP-U236-05 Data, security and edit restrictions once units are in use

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
The uom module ships a catalogue of units (some archived by default), one decimal precision record and one feature group. Reading units is open to all internal users; editing is limited to settings administrators and product managers. Once a unit is used by products and stock, several guards stop changes that would silently alter quantities: protected shipped units cannot be deleted, a ratio change is refused while open stock operations use the unit, a base-unit change on a product is refused or warned depending on history.

### D2 Architecture / data / object relationships

#### Shipped data (`uom/data/uom_data.xml`; counts by GREP, details in CAP-U236-01)
| Item | Fact | Pointer |
|---|---|---|
| decimal precision record | `decimal_product_uom`, name 'Product Unit', 2 digits | `uom/data/uom_data.xml:5-191` (record at the start of the range) |
| unit records | 30; 23 with a reference unit; 16 archived; 14 active | same file |
| top-level units | 7: Units, Hours, mm, m² (area), ml, g, KWH | same file |
| category records | none | GREP: no `uom.category` anywhere |
| Minutes ratio | 0.0166667 of Hours (approximation of one sixtieth) | `uom/data/uom_data.xml:38-42` |

#### Feature group
- `uom.group_uom`, name "Manage Multiple Units of Measure", no implied groups (`uom/security/uom_security.xml:3-7`).
- Setting field `group_uom` "Units of Measure & Packagings" (`product/models/res_config_settings.py:9`).
- Template helpers: `_has_multiple_uoms` (`product/models/product_template.py:1571-1576`), `_get_available_uoms` (L1578-1580).
- Other consumers: `product/models/product_catalog_mixin.py:131`, `stock/models/stock_package.py:118`, `stock/report/report_stock_reception.py:21`, `mrp/report/mrp_report_mo_overview.py:59`, `:72`, `mrp/report/mrp_report_bom_structure.py:104`, `l10n_in/models/account_invoice.py:619`, post-init in l10n_mx.
- `sale_timesheet` makes `base.group_user` imply `uom.group_uom` (existing evidence U02).

#### Access rows for uom.uom (9 rows; GREP over `ir.model.access.csv`)
| # | File and line | Group | R | W | C | D |
|---|---|---|---|---|---|---|
| 1 | `uom/security/ir.model.access.csv:2` | base.group_system | 1 | 1 | 1 | 1 |
| 2 | `uom/security/ir.model.access.csv:3` | base.group_user | 1 | 0 | 0 | 0 |
| 3 | `product/security/ir.model.access.csv:39` | product.group_product_manager (written as group_product_manager) | 1 | 1 | 1 | 1 |
| 4 | `sale/security/ir.model.access.csv:26` | sales_team.group_sale_salesman | 1 | 0 | 0 | 0 |
| 5 | `mrp/security/ir.model.access.csv:21` | mrp.group_mrp_user | 1 | 0 | 0 | 0 |
| 6 | `mrp_subcontracting/security/ir.model.access.csv:16` | base.group_portal | 1 | 0 | 0 | 0 |
| 7 | `hr_timesheet/security/ir.model.access.csv:4` | hr_timesheet.group_hr_timesheet_user | 1 | 0 | 0 | 0 |
| 8 | `website_sale/security/ir.model.access.csv:58` | base.group_public | 1 | 0 | 0 | 0 |
| 9 | `website_sale/security/ir.model.access.csv:59` | base.group_portal | 1 | 0 | 0 | 0 |

Access rows for product.uom (2): `product/security/ir.model.access.csv:37` product manager 1,1,1,1 and L38 `base.group_user` read only. No `ir.rule` record references either model (GREP over `*.xml`).

### D3 Source / technical / workflow logic

#### 3.1 Protected shipped units
- `_unprotected_uom_xml_ids` (`uom/models/uom_uom.py:24-32`) lists `product_uom_hour`, `product_uom_dozen`, `product_uom_pack_6` as not protected.
- `_filter_protected_uoms` (L205-216) returns the units whose model-data record is in module `uom` and whose name is not in that list (model-data lookup with elevated rights).
- hr_timesheet overrides the list to `product_uom_dozen` and `product_uom_pack_6` only, so the hour unit becomes protected (`hr_timesheet/models/uom_uom.py:10-17`; comment L12-13). It also adds the Char field `timesheet_widget` (L20).
- Delete guard (L105-112): UserError "The following units of measure are used by the system and cannot be deleted: %s\nYou can archive them instead." for the passed records only; dependants removed by the database cascade are not checked in Python (RT).
- Onchange warning (L79-93): changing "Contains" on a protected unit created more than one day ago returns a warning that existing data will not be updated.

#### 3.2 Ratio write lock (stock)
```python
# stock/models/product.py:1373-1393 (excerpt)
    def write(self, vals):
        # Users can not update the factor if open stock moves are based on it
        keys_to_protect = {'factor', 'relative_factor', 'relative_uom_id'}
        if any(key in vals for key in keys_to_protect):
            changed = self.filtered(
                lambda u: any(
                    f in vals and u[f] != vals[f]
                    for f in ('factor', 'relative_factor')
                ) or ('relative_uom_id' in vals and u.relative_uom_id.id != int(vals['relative_uom_id']))
            )
            if changed:
                error_msg = _(
                    "You cannot change the ratio of this unit of measure"
                    " as some products with this UoM have already been moved"
                    " or are currently reserved."
                )
                if self.env['stock.move'].sudo().search_count([
                    ('product_uom', 'in', changed.ids),
                    ('state', 'not in', ('cancel', 'done'))
                ]):
                    raise UserError(error_msg)
```
- Further checks (L1394-1403): stock.move.line with `product_uom_id` in the changed units and state not cancel or done; stock.quant with product template base unit in the changed units and `quantity != 0`. All three searches use elevated rights.
- Scope (FACT): only the units being written are checked; descendants whose absolute quantity changes through the recursive compute are not checked (RT).
- `int(vals['relative_uom_id'])` on a value of None would raise a TypeError (RT; clearing the reference through this path).
- Lines with state done (or cancel) do not block; a closed move keeps its stored quantity in its own unit, so a later ratio change alters how historic quantities convert (DERIVED).
- `_adjust_uom_quantities` (L1406-1418): parameter `stock.propagate_uom`.

#### 3.3 Changing the base unit of a product
| Guard | Pointer | Behaviour |
|---|---|---|
| done move edit | `stock/models/stock_move.py:853-854` | changing `product_uom` on a done move raises an error unless context `skip_uom_conversion` is set |
| move line check | `stock/models/stock_move_line.py:454` | the same context key is read |
| base `_update_uom` | `product/models/product_product.py:1197-1200` | entry point; called from `product/models/product_template.py:585-589` with `skip_uom_conversion=True` (L588) |
| sale | `sale/models/product_product.py:101-114` | `_update_uom` guard |
| purchase | `purchase/models/product.py:117-132` | `_update_uom` guard |
| mrp | `mrp/models/product.py:452-489` | `_update_uom` guard |
| repair | `repair/models/product.py:34-47` | `_update_uom` guard |
| stock | `stock/models/product.py:784-808` | `_update_uom` guard |
| warning hook | `product/models/product_product.py:422-423`; overrides `sale/models/product_product.py:116-123`, `purchase/models/product.py:134-141`, `stock/models/product.py:821-828` | `_trigger_uom_warning` decides whether the onchange warning is shown; template onchange `product/models/product_template.py:474-486`; variant onchange `product/models/product_product.py:425-437` |
| move line rounding check | `stock/models/stock_move_line.py:615-624` | rounding check on the line unit |
| purchase line price conversion | `purchase/models/purchase_order_line.py:419-422` | `skip_uom_conversion` skips the price conversion |
The guard bodies were read earlier in this unit; their exact conditions are summarised only (the individual conditions are not reproduced).

State diagram:
- `Unit ratio X -> Y [refused: open moves, open move lines, or non-zero stock use the unit; allowed otherwise]`
- `Product base unit A -> B [guarded by chain of _update_uom overrides; warning hook on form; done moves block unless skip context]`
- `Protected shipped unit -> Deleted [refused; archive instead]`
- `Unprotected unit -> Deleted [allowed; dependants cascade at database level]`

### Ten-dimension analysis

| Dimension | Finding |
|---|---|
| 1 Happy path | Shipped units are readable by every internal user; administrators or product managers create new units; products reference them; stock operations proceed with conversions. |
| 2 Reversal / cancel / negative path | Archive instead of delete; changing a ratio is allowed again once no open stock operation or on-hand stock uses the unit. |
| 3 Multi-company / data-scope | No company on units and no record rule; the packaging link record has a company field but a global unique barcode (CAP-U236-03). |
| 4 Side effects / cross-module triggers | hr_timesheet adds protection for the hour unit; sale, purchase, mrp, repair and stock chain `_update_uom`; point of sale loads units including archived. |
| 5 Configuration and optionality | Group `uom.group_uom` toggles multi-unit UI; parameter `stock.propagate_uom`; default data has 16 of 30 units archived. |
| 6 Validation and constraints | Delete guard, ratio write lock, done-move guard, base-unit guards, plus the constraints of CAP-U236-01. |
| 7 Roles and permissions | Nine access rows for units, two for the link record, no record rule; elevated rights inside guards. |
| 8 Scheduled / automated | NOT APPLICABLE — no scheduled action found for units. |
| 9 Exception and failure behaviour | UserError messages quoted above; guard conditions that depend on data are RT. |
| 10 Accounting, stock, audit, security, compliance | The lock protects open stock quantities; closed history is not recomputed; no audit trail on the unit model (no tracking found). |

### DB reconciliation (configuration/structure only)
From U02 (not re-queried): 2 access rows for the unit model in module uom; `base.group_user` read, `base.group_system` full. The nine-row figure above is a source-side count across all addons and is not a database count.

### Unknown / Runtime list
- RT: whether the lock fires for a descendant unit when a parent ratio changes.
- RT: TypeError path when `relative_uom_id` is written as empty.
- RT: Python delete guard versus database cascade for dependants of a deleted protected unit.
- UNKNOWN: the exact conditions in each `_update_uom` override beyond the pointers (read but not reproduced).

---

## CAP-U236-06 Thai deployment note

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
Whether the Thai localization ships its own unit-of-measure data.

### D2 Architecture / data / object relationships
`l10n_th/__manifest__.py` (30 lines): L16-19 dependencies `account_qr_code_emv` and `account`; L20 auto install; L21-24 data list holds only `data/account_tax_report_data.xml` and `views/report_invoice.xml`; L25-27 demo; L28 post-init hook.

### D3 Source / technical / workflow logic
- A case-insensitive GREP for "uom" and "unit of measure" over the l10n_th addon returned no match (all file types). Result: **UoM data ABSENT** for the Thai localization.
- Thai deployments therefore use the standard shipped units; any Thai-specific units would have to be configuration data created by the deployment (not present in this source).

State diagram: NOT APPLICABLE.

### Ten-dimension analysis
| Dimension | Finding |
|---|---|
| 1 Happy path | NOT APPLICABLE — no Thai unit data shipped. |
| 2 Reversal / cancel / negative path | NOT APPLICABLE. |
| 3 Multi-company / data-scope | Units are global; the localization adds none. |
| 4 Side effects / cross-module triggers | None found by GREP. |
| 5 Configuration and optionality | Local units must be created as data by the deployment. |
| 6 Validation and constraints | NOT APPLICABLE. |
| 7 Roles and permissions | NOT APPLICABLE. |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure behaviour | NOT APPLICABLE. |
| 10 Accounting, stock, audit, security, compliance | NOT APPLICABLE for units; the Thai localization concerns tax report and invoice report content only (manifest data list). |

### DB reconciliation (configuration/structure only)
Not performed; no database fact about Thai unit data was available.

### Unknown / Runtime list
- UNKNOWN: Extra Thailand and other non-Community modules were not read (out of scope).

---

## CAP-U236-07 Migration flags against v16 and v17

**Function-ID(s):** `FUNCTION MAPPING REQUIRED`.

### D1 Business purpose and process semantics
This section lists what changed in v19 relative to the older unit-of-measure design (unit categories, bigger/smaller/reference types, inverse ratio, per-unit rounding, packaging model). **The v19 side of every statement is read from source. The v16/v17 side is UNVERIFIED-FROM-SOURCE** (this tree holds only v19; the one older witness is leftover translation text, for example the Icelandic file header "Project-Id-Version: Odoo Server 16.0beta", `uom/i18n/is.po:7`, which shows that the leftover entries date from a 16.0 beta export).

### D2 Architecture / data / object relationships

#### Flag table
| Flag | Severity | v19 fact (FACT or GREP) | Pointer |
|---|---|---|---|
| UOM_CATEGORY_REMOVED | HIGH | no category model and no category field on the unit; selection by category replaced by the unit tree and `_has_common_reference` | `uom/models/uom_uom.py:17-49`; stale entry `uom/i18n/is.po:64-68` |
| UOM_TYPE_REMOVED | HIGH | no bigger/smaller/reference type field; the Reference Unit link and Contains ratio carry the meaning | `uom/models/uom_uom.py:36-43`; stale entries `uom/i18n/is.po:54-62`, L263 |
| FACTOR_INV_REMOVED | HIGH | no inverse ratio field; leftover label "Bigger Ratio" | `uom/i18n/is.po:54-57` |
| RELATIVE_UOM_TREE_ADDED | HIGH | `relative_uom_id` (parent), `relative_factor` ("Contains"), parent-store tree | `uom/models/uom_uom.py:17-22`, L36-44 |
| FACTOR_STORED_RECURSIVE_ABSOLUTE | HIGH | `factor` is a stored recursive "Absolute Quantity" (own ratio times the reference's); v16/v17 side UNVERIFIED-FROM-SOURCE | `uom/models/uom_uom.py:43`, L69-75 |
| FACTOR_DIRECTION_NOTE | HIGH | v19: a bigger unit has an absolute quantity above 1 (kg is 1000 of g); in older versions the stored ratio of a smaller unit was above 1 (UNVERIFIED-FROM-SOURCE); copying old `factor` values unchanged would invert conversions | `uom/data/uom_data.xml` (shipped ratios), `uom/models/uom_uom.py:147-176` |
| ROUNDING_GLOBAL_COMPUTED_NONSTORED | MEDIUM | `rounding` is a non-stored compute from the 'Product Unit' precision; no per-unit rounding | `uom/models/uom_uom.py:39`, L62-67 |
| ROUNDING_METHODS_FIVE | LOW | five methods accepted: UP, DOWN, HALF-UP, HALF-DOWN, HALF-EVEN | `odoo/tools/float_utils.py:8`, L134-151 |
| RAISE_IF_FAILURE_UNUSED | MEDIUM | parameter accepted and never read; 7 callers still pass false; docstring still mentions categories | `uom/models/uom_uom.py:153`, L158-162; callers in CAP-U236-02, 3.6 |
| UNRELATED_TREE_SILENT_CONVERSION | HIGH | conversion between units of different top-level units returns a number silently; `_has_common_reference` is opt-in (14 call sites) | `uom/models/uom_uom.py:147-176`, L218-230 |
| SAME_UNIT_STILL_ROUNDED | LOW | converting a unit to itself still rounds when rounding is on | `uom/models/uom_uom.py:147-176` |
| CHECK_QTY_SINGLE_CONSUMER | LOW | `_check_qty` has one production caller (full-packaging reservation) | `stock/models/stock_quant.py:851-853` |
| PRODUCT_PACKAGING_MODEL_REMOVED | HIGH | no `product.packaging` model; leftover translations only | `purchase/i18n/en_AU.po:1782` |
| PURCHASE_LINE_PACKAGING_FIELDS_ABSENT | MEDIUM | purchase line has no packaging selection or quantity (validates U215 FLAG-002) | `purchase/i18n/en_AU.po:1695`, L1700; `purchase/models/purchase_order_line.py:42-43` |
| PRODUCT_UOM_BARCODE_LINK | HIGH | new model `product.uom` (unit, product, unique barcode) replaces packaging barcodes | `product/models/product_uom.py:8-26` |
| PACKAGING_QTY_ON_SHARED_UNIT | HIGH | quantity per packaging is the shared unit's ratio, not a per-product value | `product/models/product_uom.py:13-16`, `uom/models/uom_uom.py:36-43` |
| TEMPLATE_UOM_IDS_PACKAGINGS | MEDIUM | additional units on the template, label "Packagings" (see U231) | `product/models/product_template.py:120-122` |
| MOVE_PACKAGING_UOM_FIELDS | MEDIUM | stored `packaging_uom_id` and `packaging_uom_qty` on the transfer line; overrides in five modules | `stock/models/stock_move.py:194-195`, L741-750 |
| PACKAGE_TYPE_ROUTE_SELECTION | MEDIUM | the unit points at a package type whose routes take part in rule search | `stock/models/product.py:1370`, `stock/models/stock_rule.py:550-563` |
| PUTAWAY_PACKAGE_TYPE_FROM_PACKAGING_UOM | LOW | putaway derives the package type from the packaging unit | `stock/models/stock_location.py:297-311` |
| ORDERPOINT_REPLENISHMENT_UOM | MEDIUM | reorder rule rounds up to a multiple of a unit | `stock/models/stock_orderpoint.py:64-66`, L807-814 |
| ALLOWED_UOM_IDS_DOMAIN_PATTERN | MEDIUM | line unit domains use a computed allowed-units list instead of category equality | `sale/models/sale_order_line.py:539-542` and five other models (CAP-U236-03, 3.8) |
| STOCK_RATIO_WRITE_LOCK | MEDIUM | ratio and reference edits refused while open stock operations use the unit | `stock/models/product.py:1373-1404` |
| DONE_MOVE_UOM_CHANGE_ERROR | LOW | unit change on a done move errors unless a context key is set | `stock/models/stock_move.py:853-854` |
| UPDATE_UOM_GUARD | MEDIUM | base-unit change guarded by a chain of overrides in five modules | CAP-U236-05, 3.3 |
| PROTECTED_UOM_RULE | LOW | shipped units protected from deletion; hour protected when hr_timesheet is installed | `uom/models/uom_uom.py:24-32`, L105-112; `hr_timesheet/models/uom_uom.py:10-17` |
| FIELD_NAMING_SPLIT | MEDIUM | `product_uom` on three models, `product_uom_id` on most others, `uom_id` on the template | CAP-U236-04 |
| POS_PACKAGING_BARCODE_VIA_PRODUCT_UOM | MEDIUM | point of sale loads and scans the link records | `point_of_sale/models/product_uom.py:5-16` |
| UOM_ACL_BREADTH_NO_IR_RULE | LOW | 9 access rows for units from 7 CSV files and no record rule | CAP-U236-05, D2 |
| L10N_TH_UOM_DATA_ABSENT | LOW | Thai localization ships no unit data | `l10n_th/__manifest__.py:21-24` |
| LEGACY_CATEGORY_WORDING_REMAINS | LOW | docstring, QWeb comment, tests and translations still use category wording | table below |

#### Inventory of legacy wording that is not an identifier
| Kind | Pointer |
|---|---|
| docstring | `uom/models/uom_uom.py:159` ("different UomUom category") |
| QWeb comment | `mrp/report/mrp_production_templates.xml:148` |
| tests | `account_edi_ubl_cii/tests/test_ubl_import_bis3_invoice_be_retrieve_product.py` L70, L74-75, L77; `account_edi_ubl_cii/tests/test_ubl_cii.py:172`; `purchase_mrp/tests/test_anglo_saxon_valuation.py:225-278`; `purchase/tests/test_access_rights.py:140`; `pos_sale/tests/test_pos_sale_flow.py:323` |
| unit translations | `uom/i18n/is.po` L54-62, L64-68, L248-254 (same entries in km, lb, gu) |
| purchase translations | `purchase/i18n/en_AU.po` L1234, L1695, L1700, L1782, L1825 |
| non-model "product_packaging" strings | `product/__manifest__.py:56`, `product/report/product_reports.xml:63` (record id `report_product_packaging`), `point_of_sale/tests/test_frontend.py:1273`, `point_of_sale/static/src/app/models/pos_order_line.js:43`, L53, L55 |

### D3 Source / technical / workflow logic
- Absence results (GREP over `*.py`, `*.xml`, `*.js`, `*.csv`, `*.json`, `*.scss`, `*.html`, `*.ts`, section 0.3): no production identifier for `uom.category`, a category field on the unit, `uom_type`, `factor_inv`, `uom_po_id`, `product_uom_category_id`, `qty_multiple`, `product.packaging`.
- Migration consequences that follow from the v19 side alone (no older source needed): (a) data keyed on a unit category has nothing to map to; (b) the old bigger/smaller type and inverse ratio must be converted into reference unit plus Contains; (c) the direction of the ratio must be checked per unit before loading (see FACTOR_DIRECTION_NOTE); (d) packaging rows must become units plus link records, with the packaging quantity carried by the unit; (e) per-unit rounding values cannot be stored.
- A direct comparison with v16/v17 source was not possible; every statement about the older design is labelled UNVERIFIED-FROM-SOURCE.

State diagram: NOT APPLICABLE — migration inventory.

### Ten-dimension analysis
| Dimension | Finding |
|---|---|
| 1 Happy path | NOT APPLICABLE — inventory of changes. |
| 2 Reversal / cancel / negative path | NOT APPLICABLE. |
| 3 Multi-company / data-scope | Unit catalogue is global in v19; older company scoping UNVERIFIED-FROM-SOURCE. |
| 4 Side effects / cross-module triggers | The removal of categories and packaging touches every module that filtered units by category or used packaging fields (flag table). |
| 5 Configuration and optionality | Group `uom.group_uom`; settings label "Units of Measure & Packagings". |
| 6 Validation and constraints | Removed constraints are visible only in translations (`uom/i18n/is.po:248-254`). |
| 7 Roles and permissions | Nine access rows for units. |
| 8 Scheduled / automated | NOT APPLICABLE. |
| 9 Exception and failure behaviour | Silent conversion between unrelated units is the main behavioural change to watch. |
| 10 Accounting, stock, audit, security, compliance | Ratio direction and rounding policy affect booked quantities and valuation; verify before loading migrated data. |

### DB reconciliation (configuration/structure only)
From U02 (not re-queried): no category column on `uom_uom`; `product_uom` table has 0 rows. These agree with the v19 model.

### Unknown / Runtime list
- UNVERIFIED-FROM-SOURCE: every v16/v17 statement.
- RT: effect of loading old ratios unchanged into the new model.
- UNKNOWN: upgrade scripts (none in the Community tree read here).

---

## Validation of existing evidence

### U02 CAP-U02-04 (units of measure, restored database)
No contradiction found. U02 statements checked against source: removal of the unit category and type concepts; reference-unit tree; stored absolute quantity; global rounding from the 'Product Unit' precision; ratio-zero check; the link model `product.uom` with unique barcode; the access rows in module uom. Nuances added by this unit: `raise_if_failure` is accepted and ignored while seven callers still pass false; `_has_common_reference` has 14 call sites including six QWeb templates; `_check_qty` computes the packaging quantity before the same-unit check; same-unit conversion still rounds; U02's database facts (30 unit rows, no category column, 0 link rows, 2 access rows in module uom, precision 2) are reused with attribution and not re-queried.

### U215 FLAG-002 (packaging fields absent on purchase.order.line)
CONFIRMED (GREP, `purchase/models/purchase_order_line.py` declares no packaging fields; `purchase/i18n/en_AU.po:1695`, L1700 and L1782 are stale translations).

---

## Claim index (File 2 rows)
| Claim-ID | Capability | Pointer |
|---|---|---|
| U236-C01 | CAP-U236-01 | `uom/models/uom_uom.py:17-49` |
| U236-C02 | CAP-U236-01 | `uom/models/uom_uom.py:69-75` |
| U236-C03 | CAP-U236-01 | `uom/models/uom_uom.py:62-67` |
| U236-C04 | CAP-U236-01 | `uom/models/uom_uom.py:97-101` |
| U236-C05 | CAP-U236-02 | `uom/models/uom_uom.py:147-176` |
| U236-C06 | CAP-U236-02 | `uom/models/uom_uom.py:153-161` |
| U236-C07 | CAP-U236-02 | `uom/models/uom_uom.py:196-203` |
| U236-C08 | CAP-U236-02 | `uom/models/uom_uom.py:178-194` |
| U236-C09 | CAP-U236-03 | `stock/models/stock_quant.py:851-853` |
| U236-C10 | CAP-U236-03 | `product/models/product_uom.py:8-16` |
| U236-C11 | CAP-U236-03 | `product/models/product_uom.py:18-26` |
| U236-C12 | CAP-U236-03 | `stock/models/stock_move.py:741-750` |
| U236-C13 | CAP-U236-03 | `stock/models/stock_rule.py:550-563` |
| U236-C14 | CAP-U236-03 | `stock/models/stock_orderpoint.py:807-814` |
| U236-C15 | CAP-U236-04 | `stock/models/stock_move.py:67-70` |
| U236-C16 | CAP-U236-03 | `sale/models/sale_order_line.py:539-542` |
| U236-C17 | CAP-U236-05 | `uom/data/uom_data.xml:5-191` |
| U236-C18 | CAP-U236-05 | `uom/security/ir.model.access.csv:2-3` |
| U236-C19 | CAP-U236-05 | `stock/models/product.py:1373-1404` |
| U236-C20 | CAP-U236-06 | `l10n_th/__manifest__.py:21-24` |
| U236-C21 | CAP-U236-07 | `uom/i18n/is.po:64-68` |
| U236-C22 | CAP-U236-07 | `uom/i18n/is.po:54-62` |
| U236-C23 | CAP-U236-07 | `purchase/i18n/en_AU.po:1782` |
| U236-C24 | CAP-U236-07 | `purchase/i18n/en_AU.po:1695-1700` |

---

## Consolidated Unknown / Runtime list
- RT: all hand calculations (CAP-U236-02, 3.10).
- RT: recompute of descendant absolute quantities; lock behaviour for descendants (CAP-U236-01, CAP-U236-05).
- RT: conversion between units of different top-level units, derived from reading only.
- RT: non-elevated product search in the packaging barcode check under company rules.
- RT: TypeError path on clearing the reference unit through the stock write lock.
- UNKNOWN: negative ratio and reference cycle handling (no constraint read).
- UNKNOWN: client components under `uom/static/src/components`.
- UNKNOWN: Enterprise and Extra modules (out of scope).
- UNVERIFIED-FROM-SOURCE: all v16/v17 statements, including factor direction.

<!-- end of U236 file -->

