# U98 — Python Formula Tax (L3/L7/L12 Adversarial)
**Unit**: U98
**Phase**: Second-Pass Depth Closure — P1 Core / Adversarial
**Scope**: Python tax formula eval mechanism, safe_eval sandbox, code injection risk, tax tag update wizard
**Modules**: account_tax_python, account_update_tax_tags
**Function-IDs targeted**: NEW:U98-F01 through U98-F14
**L-levels**: L3, L7, L12
**Proof layers**: P2, P3
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U13, U32

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U98-001 | U98-F01 | account_tax_python/models/account_tax.py:19 | `formula = fields.Text(` | DEF | amount_type == 'code' | — | The `formula` field (type `fields.Text`) on `account.tax` stores the user-authored Python expression string. Default value is `"price_unit * 0.10"`. | NR-U98-001 |
| U98-002 | U98-F01 | account_tax_python/models/account_tax.py:15 | `selection_add=[('code', "Custom Formula")]` | DEF | — | — | A new `amount_type` selection option `'code'` labelled "Custom Formula" is added to `account.tax` via `selection_add`. | NR-U98-002 |
| U98-003 | U98-F02 | account_tax_python/models/account_tax.py:7 | `from odoo.tools.safe_eval import safe_eval` | CALL | — | — | The module imports `safe_eval` from `odoo.tools.safe_eval`; raw `eval` is never imported or used in this module. | NR-U98-003 |
| U98-004 | U98-F03 | account_tax_python/models/account_tax.py:112 | `return safe_eval(normalized_formula, formula_context)` | CALL | amount_type == 'code' | C1 | Formula execution uses `safe_eval(normalized_formula, formula_context)` where `formula_context` is a plain dict of primitives serialized through `json.loads(json.dumps(...))`. | NR-U98-004 |
| U98-005 | U98-F03 | account_tax_python/models/account_tax.py:98 | `formula_context = {` | DEF | — | — | The evaluation context (`formula_context`) exposes exactly five keys: `price_unit`, `quantity`, `product`, `uom`, `base`. No `self`, `env`, or ORM methods are present. | NR-U98-005 |
| U98-006 | U98-F03 | account_tax_python/models/account_tax.py:108 | `formula_context = json.loads(json.dumps(formula_context))` | ASSIGN | — | C1 | Before `safe_eval`, the context is round-tripped through JSON (`json.loads(json.dumps(...))`), stripping any non-serializable Python objects and raising `ValidationError` on `TypeError`. | NR-U98-006 |
| U98-007 | U98-F04 | account_tax_python/tools/formula_utils.py:8 | `_ALLOWED_FUNCS = ('min', 'max')` | CONST | — | — | Only two function names (`min`, `max`) are on the function whitelist (`_ALLOWED_FUNCS`). Any other call raises `ValidationError("Unknown function call")`. | NR-U98-007 |
| U98-008 | U98-F04 | account_tax_python/tools/formula_utils.py:9 | `_ALLOWED_NAMES = ('price_unit', 'quantity', 'base', 'product', 'uom')` | CONST | — | — | Identifier access in the AST is limited to five names by `_ALLOWED_NAMES`; any other `ast.Name` node raises `ValidationError("Unknown identifier: ...")`. | NR-U98-008 |
| U98-009 | U98-F04 | account_tax_python/tools/formula_utils.py:13 | `_NODE_WHITELIST = (` | CONST | — | — | Only a strict set of AST node types is permitted: `Expression`, `Name`, `Call`, `Subscript`, `Constant`, arithmetic `BinOp` ops, `BoolOp`, `Compare`, and `UnaryOp`. Any other AST node type raises `ValidationError("Invalid AST node: ...")`. | NR-U98-009 |
| U98-010 | U98-F04 | account_tax_python/tools/formula_utils.py:10 | `_ALLOWED_CONSTANT_T = (int, float, type(None))` | CONST | — | — | Literal constants in formulas are restricted to `int`, `float`, or `None` types only; string literals, bytes, etc. raise `ValidationError`. | NR-U98-010 |
| U98-011 | U98-F04 | account_tax_python/tools/formula_utils.py:88 | `if node.id not in _ALLOWED_NAMES:` | GUARD | — | — | `TaxFormulaValidator.visit_Name` raises `ValidationError` if the identifier is not in `_ALLOWED_NAMES`, effectively blocking `self`, `env`, `os`, `subprocess`, and all other symbols. | NR-U98-011 |
| U98-012 | U98-F04 | account_tax_python/tools/formula_utils.py:77 | `if not isinstance(node, _NODE_WHITELIST):` | GUARD | — | — | `TaxFormulaValidator.visit` raises `ValidationError` for every node type not in `_NODE_WHITELIST`, including `ast.Import`, `ast.Assign`, `ast.FunctionDef`, `ast.Lambda`, `ast.Attribute`, etc. | NR-U98-012 |
| U98-013 | U98-F05 | account_tax_python/tools/formula_utils.py:129 | `tree = ast.parse(formula, mode="eval")` | CALL | — | — | Formula validation and normalization both parse in `mode="eval"`, which restricts input to a single expression; multi-statement code (`exec`-mode) raises `SyntaxError` at parse time. | NR-U98-013 |
| U98-014 | U98-F05 | account_tax_python/tools/formula_utils.py:155 | `transformer = ProductUomFieldRewriter()` | CALL | — | — | `normalize_formula` applies `ProductUomFieldRewriter` (an `ast.NodeTransformer`) which rewrites `product.field` → `product['field']` and collects accessed field names before validation. | NR-U98-014 |
| U98-015 | U98-F05 | account_tax_python/tools/formula_utils.py:105 | `"Only product['string'] or uom['string'] read-access is allowed"` | GUARD | — | — | Subscript access (`[]`) on the `product` and `uom` dicts is allowed only for string-constant keys in read (`Load`) context; any other subscript usage raises `ValidationError`. | NR-U98-015 |
| U98-016 | U98-F06 | account_tax_python/models/account_tax.py:30 | `@api.constrains('amount_type', 'formula')` | TRIGGER | amount_type == 'code' | — | A `@api.constrains` decorator fires `_check_amount_type_code_formula` on every save of `amount_type` or `formula`; it calls `_check_and_normalize_formula` to validate/normalize before commit. | NR-U98-016 |
| U98-017 | U98-F06 | account_tax_python/models/account_tax.py:95 | `normalized_formula, accessed_fields = self._check_and_normalize_formula(self.formula_decoded_info['py_formula'])` | CALL | — | — | At runtime, `_eval_tax_amount_formula` re-validates and re-normalizes the stored formula (from `formula_decoded_info['py_formula']`) immediately before `safe_eval`, providing a second validation gate. | NR-U98-017 |
| U98-018 | U98-F07 | odoo/tools/safe_eval.py:78 | `_BLACKLIST = set(to_opcodes([` | CONST | — | — | `safe_eval` opcode blacklist explicitly prohibits `IMPORT_STAR`, `IMPORT_NAME`, `IMPORT_FROM`, `STORE_ATTR`, `DELETE_ATTR`, `STORE_GLOBAL`, `DELETE_GLOBAL` — blocking module imports and attribute mutation. | NR-U98-018 |
| U98-019 | U98-F07 | odoo/tools/safe_eval.py:199 | `def assert_no_dunder_name(code_obj, expr):` | GUARD | — | — | `safe_eval` calls `assert_no_dunder_name` which raises `NameError` for any `co_names` entry containing `"__"` or matching `_UNSAFE_ATTRIBUTES`, blocking `__class__`, `__subclasses__`, `__globals__`, etc. | NR-U98-019 |
| U98-020 | U98-F07 | odoo/tools/safe_eval.py:402 | `globals_dict = dict(context or {}, __builtins__=dict(_BUILTINS))` | ASSIGN | — | — | `safe_eval` replaces `__builtins__` with the controlled `_BUILTINS` dict; the standard Python builtin namespace (including `open`, `exec`, `compile`, `getattr`, `__import__` unrestricted) is not accessible. | NR-U98-020 |
| U98-021 | U98-F07 | odoo/tools/safe_eval.py:318 | `'__import__': _import,` | ASSIGN | — | — | The `__import__` entry in `_BUILTINS` is replaced with `_import`, a mock that only allows modules pre-listed in `_ALLOWED_MODULES` (`['_strptime', 'math', 'time']`) and raises `ImportError` for all others. | NR-U98-021 |
| U98-022 | U98-F08 | account/security/ir.model.access.csv:77 | `model_account_tax,account.group_account_manager,1,1,1,1` | CONFIG | — | — | `account.tax` write/create/unlink access is granted exclusively to `account.group_account_manager`; writing the `formula` field therefore requires Account Manager role. | NR-U98-022 |
| U98-023 | U98-F09 | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:6 | `class AccountUpdateTaxTagsWizard(models.TransientModel):` | DEF | — | — | `account.update.tax.tags.wizard` is a `TransientModel` wizard (`_name = 'account.update.tax.tags.wizard'`) that re-synchronises tax tag assignments on journal items. | NR-U98-023 |
| U98-024 | U98-F09 | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:172 | `def update_amls_tax_tags(self):` | DEF | — | — | The public action method `update_amls_tax_tags` validates parent-child tax constraints and then delegates to `_modify_tag_to_aml_relation` with the wizard's `company_id` and `date_from`. | NR-U98-024 |
| U98-025 | U98-F09 | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py:50 | `self.env.cr.execute("""` | CALL | — | — | `_modify_tag_to_aml_relation` executes a single multi-step raw SQL CTE that (1) resolves current repartition-line tags, (2) deletes previous `account_account_tag_account_move_line_rel` rows, (3) inserts new rows, scoped by `company_id` and `date_from`. | NR-U98-025 |
| U98-026 | U98-F10 | account_update_tax_tags/security/ir.model.access.csv:2 | `model_account_update_tax_tags_wizard,account.group_account_manager,1,1,1,0` | CONFIG | — | — | The `account.update.tax.tags.wizard` transient model is accessible (read/write/create) only to `account.group_account_manager`; unlink is denied. | NR-U98-026 |
| U98-027 | U98-F11 | account_tax_python/tools/formula_utils.py:86 | `if not isinstance(node.ctx, ast.Load):` | GUARD | — | — | `visit_Name` rejects any `Name` node whose context is not `ast.Load`, meaning variable assignment (`Store`) and deletion (`Del`) within the formula expression are blocked at AST level. | NR-U98-027 |

---

## L12 Adversarial Analysis

### Sandbox Mechanism Summary

The formula sandbox is a **dual-layer defense**:

**Layer 1 — AST whitelist (formula_utils.py)**
Before storage (via `@api.constrains`) and again before each evaluation, the formula string is parsed as an `ast.Expression` (single-expression mode only) and traversed by `TaxFormulaValidator`. This validates:
- Node type whitelist (`_NODE_WHITELIST`) — rejects `Import`, `FunctionDef`, `Lambda`, `Attribute`, `Assign`, `For`, `While`, `If` (statement-level), etc.
- Identifier whitelist (`_ALLOWED_NAMES`) — rejects `self`, `env`, `os`, `sys`, `open`, `__import__`, and all other names not in the five-element set.
- Constant type whitelist — rejects string constants (eliminates `__import__('os')` string tricks).
- Function call whitelist — only `min(...)` and `max(...)` are permitted.
- Subscript scope — only `product[str]` and `uom[str]` dictionary reads.

**Layer 2 — safe_eval opcode/name guards**
Even if a bypass of the AST layer existed, `safe_eval` provides:
- Opcode blacklist blocks all `IMPORT_*`, `STORE_ATTR`, `DELETE_ATTR`, `STORE_GLOBAL`, `DELETE_GLOBAL`.
- `assert_no_dunder_name` blocks any `co_names` entry containing `"__"`.
- Replaced `__builtins__` exposes only a controlled set (no `exec`, `compile`, `open`, `getattr`, `setattr`, etc.).
- Mock `__import__` only permits `_strptime`, `math`, `time`.

**Context isolation**
The `formula_context` dict (5 keys: `price_unit`, `quantity`, `product`, `uom`, `base`) is serialized through `json.loads(json.dumps(...))` before passing to `safe_eval`. This ensures `product` and `uom` are plain dicts with no ORM methods, recordset state, or `env` reference — even if the AST and opcode layers were somehow bypassed, `env` is not in scope.

### Blast Radius Assessment

An authorized `account.group_account_manager` user who can write the `formula` field cannot:
- Execute `os.system`, `subprocess`, or file I/O via the formula.
- Access `self.env`, ORM search, or database queries via the formula.
- Import arbitrary modules.
- Assign variables, define functions, or write multi-line code.

An authorized user **can** craft a formula that:
- Causes `ZeroDivisionError` (silently caught, returns `0.0`).
- Returns unexpected numeric values (e.g., `0` for all transactions), causing incorrect tax amounts on all future invoices processed with that tax. This is a **data-integrity risk**, not a code-execution risk.
- Accesses any non-relational field on `product.product` or `uom.uom` by name (serialized through JSON to a plain dict) — this is by design and does not constitute a bypass.

**Conclusion**: The formula sandbox in Odoo 19 Community is well-constructed. Code injection (RCE) via the `formula` field by an authorized Account Manager is blocked by three independent layers. The residual risk is **authorized-user financial-data manipulation** (incorrect tax amounts), which is an access-control governance issue, not a technical sandbox failure.
