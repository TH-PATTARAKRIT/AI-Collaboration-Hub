# U71 — Multi-Company Isolation Depth
**Unit**: U71
**Phase**: Second-Pass Depth Closure — P0 Critical
**Scope**: Multi-company record isolation, ir.rule audit, allowed_company_ids, intercompany automation
**Modules**: base, account, stock, sale, purchase, stock_account
**Function-IDs targeted**: MCT-F01, MCT-F02, MCT-F05
**L-levels targeted**: L3, L4, L7, L9
**Proof layers targeted**: P3, P4
**Date**: 2026-10-02
**Status**: GATE-PENDING
**Predecessor**: U21, U28

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U71-001 | MCT-F01 | stock/models/stock_warehouse.py:37 | company_id = fields.Many2one | DEF | always | C1 | stock.warehouse.company_id is declared as a Many2one to res.company | NR-U71-001 |
| U71-002 | MCT-F01 | stock/models/stock_warehouse.py:39 | readonly=True, required=True | CONFIG | always | C1 | stock.warehouse.company_id has required=True and readonly=True, preventing post-creation company changes | NR-U71-002 |
| U71-003 | MCT-F01 | stock/models/stock_picking.py:130 | company_id = fields.Many2one | DEF | always | C1 | stock.picking.company_id is declared as a Many2one to res.company | NR-U71-003 |
| U71-004 | MCT-F01 | stock/models/stock_picking.py:131 | 'res.company', 'Company', required=True | CONFIG | always | C1 | stock.picking.company_id has required=True enforcing every transfer to belong to a company | NR-U71-004 |
| U71-005 | MCT-F01 | stock/models/stock_move.py:35 | company_id = fields.Many2one | DEF | always | C1 | stock.move.company_id is declared as a Many2one to res.company | NR-U71-005 |
| U71-006 | MCT-F01 | stock/models/stock_move.py:38 | index=True, required=True | CONFIG | always | C1 | stock.move.company_id has required=True ensuring every stock movement is company-scoped | NR-U71-006 |
| U71-007 | MCT-F01 | stock/models/stock_quant.py:56 | company_id = fields.Many2one(related='location_id.company_id' | DEF | always | C1 | stock.quant.company_id is a related field derived from location_id.company_id and stored (store=True) | NR-U71-007 |
| U71-008 | MCT-F01 | stock/security/stock_security.xml:72 | stock_picking multi-company | GUARD | always | C1 | ir.rule stock_picking_rule applies domain_force [('company_id', 'in', company_ids)] to stock.picking | NR-U71-008 |
| U71-009 | MCT-F01 | stock/security/stock_security.xml:75 | ('company_id', 'in', company_ids) | GUARD | always | C1 | stock.picking ir.rule uses company_ids (activated companies) not just company_id for the domain filter | NR-U71-009 |
| U71-010 | MCT-F01 | stock/security/stock_security.xml:96 | stock_warehouse_comp_rule | GUARD | always | C1 | ir.rule stock_warehouse_comp_rule applies domain_force [('company_id', 'in', company_ids)] to stock.warehouse | NR-U71-010 |
| U71-011 | MCT-F01 | stock/security/stock_security.xml:108 | stock_move multi-company | GUARD | always | C1 | ir.rule stock_move_rule applies domain_force [('company_id', 'in', company_ids)] to stock.move | NR-U71-011 |
| U71-012 | MCT-F01 | stock/security/stock_security.xml:120 | stock_quant multi-company | GUARD | always | C1 | ir.rule stock_quant_rule applies domain_force [('company_id', 'in', company_ids + [False])] to stock.quant, allowing unassigned quants | NR-U71-012 |
| U71-013 | MCT-F01 | stock/models/stock_picking.py:25 | _check_company_auto = True | CONFIG | always | C1 | stock.picking.type sets _check_company_auto = True, triggering _check_company on write/create for all check_company=True relational fields | NR-U71-013 |
| U71-014 | MCT-F02 | stock/security/stock_security.xml:70 | noupdate="1" | CHECK | always | | The stock module defines 16 ir.rule records in stock_security.xml, all using company_id in domain_force; no intercompany automation module exists in Community addons | NR-U71-014 |
| U71-015 | MCT-F02 | sale/security/ir_rules.xml:5 | sale_order_comp_rule | GUARD | always | C1 | ir.rule sale_order_comp_rule applies domain_force [('company_id', 'in', company_ids)] to sale.order | NR-U71-015 |
| U71-016 | MCT-F02 | sale/security/ir_rules.xml:11 | sale_order_line_comp_rule | GUARD | always | C1 | ir.rule sale_order_line_comp_rule applies domain_force [('company_id', 'in', company_ids)] to sale.order.line | NR-U71-016 |
| U71-017 | MCT-F02 | purchase/security/purchase_security.xml:43 | ('company_id', 'in', company_ids) | GUARD | always | C1 | ir.rule purchase_order_comp_rule applies domain_force [('company_id', 'in', company_ids)] to purchase.order | NR-U71-017 |
| U71-018 | MCT-F02 | purchase/security/purchase_security.xml:49 | ('company_id', 'in', company_ids) | GUARD | always | C1 | ir.rule purchase_order_line_comp_rule applies domain_force [('company_id', 'in', company_ids)] to purchase.order.line | NR-U71-018 |
| U71-019 | MCT-F05 | base/models/res_users.py:247 | company_ids = fields.Many2many('res.company' | DEF | always | C1 | res.users.company_ids is a Many2many to res.company via the res_company_users_rel join table, representing all companies a user is allowed to access | NR-U71-019 |
| U71-020 | MCT-F05 | base/models/ir_rule.py:78 | return ['allowed_company_ids'] | RETURN | always | C1 | ir.rule._compute_domain_keys() returns ['allowed_company_ids'] as the sole context key used to cache domain computation, so domain re-evaluation is triggered when the active company set changes | NR-U71-020 |
| U71-021 | MCT-F05 | base/models/ir_rule.py:49 | 'company_ids': self.env.companies.ids | ASSIGN | always | C1 | ir.rule._eval_context() injects company_ids = self.env.companies.ids into the domain evaluation context; this is the set of activated (switched) companies for the current session | NR-U71-021 |
| U71-022 | MCT-F05 | base/models/ir_rule.py:120 | if self.env.su: | GUARD | when env.su is True | C1 | ir.rule._get_rules() returns an empty recordset when self.env.su is True, meaning all ir.rule record-level security is bypassed in sudo() environments | NR-U71-022 |
| U71-023 | MCT-F05 | base/models/ir_rule.py:20 | _allow_sudo_commands = False | CONFIG | always | | The IrRule model itself sets _allow_sudo_commands = False, preventing sudo-elevated write commands to ir.rule records via One2many/Many2many relations | NR-U71-023 |
| U71-024 | MCT-F05 | ../orm/models.py:451 | _check_company_auto: bool = False | DEF | always | | The ORM BaseModel sets _check_company_auto = False by default; individual models must explicitly set it to True to enable automatic company consistency validation on write/create | NR-U71-024 |
| U71-025 | MCT-F05 | ../orm/models.py:4015 | def _check_company(self, fnames=None) | DEF | always | C1 | ORM._check_company() iterates all records and validates that relational fields with check_company=True point to records compatible with the source record's company_id or company_ids | NR-U71-025 |
| U71-026 | MCT-F05 | ../orm/models.py:4003 | def _check_company_domain(self, companies) | DEF | always | C1 | ORM._check_company_domain() builds a Domain('company_id', 'in', ...) for cross-record company consistency checks; subclasses may override this | NR-U71-026 |
| U71-027 | MCT-F05 | account/models/account_move.py:79 | _check_company_auto = True | CONFIG | always | C1 | account.move sets _check_company_auto = True, enabling automatic cross-record company validation on every write and create operation | NR-U71-027 |
| U71-028 | MCT-F05 | sale/models/sale_order.py:39 | _check_company_auto = True | CONFIG | always | C1 | sale.order sets _check_company_auto = True, enabling automatic cross-record company validation on write/create | NR-U71-028 |
| U71-029 | MCT-F05 | account/security/account_security.xml:128 | account_move_comp_rule | GUARD | always | C1 | ir.rule account_move_comp_rule applies domain_force [('company_id', 'in', company_ids)] to account.move | NR-U71-029 |
| U71-030 | MCT-F05 | account/security/account_security.xml:146 | journal_comp_rule | GUARD | always | C1 | ir.rule journal_comp_rule applies domain_force [('company_id', 'parent_of', company_ids)] to account.journal, allowing parent-branch journals to be visible to child-company users | NR-U71-030 |
| U71-031 | MCT-F05 | account/security/account_security.xml:152 | account_comp_rule | GUARD | always | C1 | ir.rule account_comp_rule applies domain_force [('company_ids', 'parent_of', company_ids)] to account.account, using the multi-valued company_ids field and parent_of hierarchy traversal | NR-U71-031 |
| U71-032 | MCT-F05 | base/models/res_company.py:51 | parent_id = fields.Many2one('res.company' | DEF | always | | res.company.parent_id is a Many2one self-reference enabling a hierarchical branch structure; the parent_of domain operator depends on this | NR-U71-032 |
| U71-033 | MCT-F05 | base/models/res_company.py:54 | parent_path = fields.Char(index=True) | DEF | always | | res.company.parent_path stores the materialised ancestor path, enabling the parent_of domain operator used in account security rules | NR-U71-033 |
| U71-034 | MCT-F05 | account/models/account_move.py:5853 | Use sudo() because the SQL query above | CHECK | during sequence gap detection | AWT | account.move uses an explicit sudo() during sequence-gap detection because the underlying SQL query returns IDs from parent/sibling companies that the current user cannot access; the comment documents this as a safe bypass because made_sequence_gap is a housekeeping flag | NR-U71-034 |
| U71-035 | MCT-F05 | account/models/account_move.py:5673 | move_company_and_parents = move.company_id.sudo().parent_ids | CALL | during account consistency check | AWT | account.move uses sudo() to traverse company parent_ids when validating that move line accounts belong to the move's company or any of its ancestors; this crosses company boundaries intentionally but is read-only validation | NR-U71-035 |
| U71-036 | MCT-F05 | base/models/res_users.py:169 | def _check_company_domain(self, companies) | OVERRIDE | always | C1 | res.users overrides _check_company_domain() to use Domain('company_ids', 'in', company_ids) instead of the default company_id check, reflecting that a user may belong to multiple companies | NR-U71-036 |
