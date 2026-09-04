# E02 — CHART, IDENTITY, CLOSE, FX, REPORTS (LAYER 2 — AUDIT QUARANTINE)

**Boss / PMO / AI-Audit only.**

## Chart and identity
| Ref | Citation |
|---|---|
| `EV-COA-01` | `account/models/account_account.py:106 company_ids` — many2many to `res.company`, required; relation table `account_account_res_company_rel` at `:161-176` |
| `EV-COA-02` | no `_sql_constraints`, no `init()` on the account model; the block at `:1468-1474` belongs to `AccountGroup` (class opens `:1455`) |
| `EV-COA-03` | `:1013 create` · `:1031-1035 write` · `:1037 _ensure_code_is_unique`; deferrable via `defer_account_code_checks` |
| `EV-COA-04` | `:1074-1081` uniqueness domain `['|', ('company_ids','parent_of',…), ('company_ids','child_of',…)]`; duplicate search `.sudo()` at `:1064`; error lists codes at `:1084-1086` |
| `EV-COA-05` | `account/security/account_security.xml:171-175 account_comp_rule` domain `[('company_ids','parent_of',company_ids)]` — downward only |
| `EV-COA-06` | `:49 code` computed/search/inverse · `:50 code_store` `company_dependent=True` → jsonb (`CORE/fields.py:774`, `:992`) |
| `EV-COA-07` | `:387-390 _compute_code` and `:395-406 _inverse_code` key on `self.env.company.root_id`; `:147-148` and `:184` same in SQL; comment at `:400-401` |
| `EV-COA-08` | `account/models/account_code_mapping.py:4 COMPANY_OFFSET = 10000` · `:14-15 _auto=False, _table_query='0'` · `:47-55 _search` iterates `self.env.user.company_ids` · `:71-73 _inverse_code` |
| `EV-COA-09` | `:54-78 account_type` — 18 values; no `selection_add` anywhere in REF18 |
| `EV-COA-10` | `:677-679 _get_internal_group` and `:145-146` SQL `split_part(account_type,'_',1)` |
| `EV-COA-11` | `:80-84`, `:666-668 _compute_include_initial_balance` |
| `EV-COA-12` | `:33-41 _check_account_type_unique_current_year_earning`; `account/models/company.py:740-769 get_unaffected_earnings_account` |
| `EV-COA-13` | `:697-706 _compute_reconcile`; `:27-31 _check_reconcile`; `:196-203 _constrains_reconcile` |
| `EV-COA-14` | `:121-122 group_id` non-stored compute · `:456-483 _compute_account_group` prefix-range SQL · `:1462 parent_id readonly` · `:1556 _adapt_parent_account_group` · `:1505-1524 _constraint_prefix_overlap` |
| `EV-COA-15` | `:454-456` `@api.depends_context('company') @api.depends('code')` — re-parenting on code change |
| `EV-COA-16` | `:1015-1035 write` — full body 21 lines, guards only currency-vs-existing-lines and deprecation-vs-tax-repartition; `:53 used` and `:486-501` never consulted |
| `EV-COA-17` | `account/models/account_move_line.py:107 account_code = fields.Char(related='account_id.code')` |
| `EV-COA-18` | `account/wizard/account_merge_wizard.py:135 _action_merge` · `:157-166` FK/reference retarget · `:194-201 DELETE FROM account_account` · `:44 grouping_fields` · `:311`, `:332` constraints; `account/models/account_account.py:1129 _merge_method` refuses generic merge |
| `EV-COA-19` | `:52 deprecated`; posting checks bypassed by `skip_account_deprecation_check` at `account/models/account_move_line.py:1212` and `account/models/account_move.py:4911` |
| `EV-COA-20` | `:1094-1108` three `@api.ondelete` guards |
| `EV-COA-21` | chart data: `account/data/template/account.account-generic_coa.csv` (44 rows), `l10n_th/data/template/account.account-th.csv` (27 rows); account-group records in REF18: **0** |

## Calendar, lock, close
| Ref | Citation |
|---|---|
| `EV-CL-01` | `account/models/company.py:71-72 fiscalyear_last_day/_last_month`; `:283 _get_company_root_delegated_field_names` |
| `EV-CL-02` | `account_accountant/models/account_fiscal_year.py:11` model, 4 fields, `:23 _check_dates`; no state, no lock, no entry link |
| `EV-CL-03` | `account/models/company.py:1021 compute_fiscalyear_dates`; override `account_accountant/models/res_company.py:148`, `:185` |
| `EV-CL-04` | numbering year from company config only: `account/models/account_move.py:3569 _get_sequence_date_range`; reports via `account_reports/models/account_report.py:821` |
| `EV-CL-05` | `account/models/company.py:53 SOFT_LOCK_DATE_FIELDS` (4) · `:59 LOCK_DATE_FIELDS` (5) · fields `:73, :78, :84, :89, :94`, all `tracking=True` |
| `EV-CL-06` | `:105-109` per-user projections · `:531 _get_user_lock_date` (exception-reducible) · `:397 user_hard_lock_date` (`max` over parents, no exception) · `:565 _get_user_fiscal_lock_date` |
| `EV-CL-07` | `account/models/account_lock_exception.py:12` model · `:52 lock_date_field` (4 soft only) · `:38 user_id` (null = everyone) · `:47 end_datetime` (null = forever) · `:43 reason` not required · `:200` single-field validation · `:242 copy` refused · `:245 _recreate` · `:258 action_revoke` · `:277`/`:318` audit hook |
| `EV-CL-08` | `account_accountant/wizard/account_change_lock_date.py:143 exception_duration` (5) · `:134 exception_applies_to` (2) · **`:265` returns False for everyone+forever → no exception record** · `:348 _change_lock_date` writes the company directly · `:245` no future lock · `:352` group check |
| `EV-CL-09` | `account/security/ir.model.access.csv:18-19` — read for all internal users; manager read+create; **no unlink** |
| `EV-CL-10` | `account/models/account_move.py:801 _compute_date` · `:5655 _get_accounting_date` · `:4932-4936 _post` silent re-date · `:2377 _check_fiscal_lock_dates` · `:3230-3241`/`:3278-3283` write guards |
| `EV-CL-11` | `account/models/sequence_mixin.py:158` `sequence.mixin.constraint_start_date` config parameter escape; `:174` message instructing the user to clear the number |
| `EV-CL-12` | `account/models/company.py:474 _validate_locks` — hard monotonicity `:492-499`; draft-entry refusal hard-lock only; unreconciled statement lines `:466` |
| `EV-CL-13` | `account_reports/wizard/account_change_lock_date.py:13` → `account_reports/models/account_report.py:4233 _generate_default_external_values`; `:4285-4293` never overwrites |
| `EV-CL-14` | year close: four independent patterns over REF18 return no result-appropriation generator; balance-sheet derivation `account_reports/data/balance_sheet.xml:169`, `:176`, `:183`, `:243`, `:249`, `:157`, `:162`; GL side `account_reports/models/account_general_ledger.py:306`, `:342-355`, `:203-223` |
| `EV-CL-15` | `account/models/account_move.py:5352` refuses reset-to-draft on a sealed entry; `account/wizard/account_secure_entries_wizard.py:12`, `:36` |
| `EV-CL-16` | tax close: `account_reports/models/res_company.py:142 _get_and_update_tax_closing_moves` (`:194` date = period_end, `:198` name `'/'`, `:180` single-instance refusal); `account_reports/models/account_move.py:132` advances the tax cut-off |

## Settlement
| Ref | Citation |
|---|---|
| `EV-REC-01` | `account/models/account_partial_reconcile.py:10` model, fields `:14-62`; `account/models/account_full_reconcile.py:6` model, 3 fields |
| `EV-REC-02` | `:79-85 _compute_max_date` — later of the two document dates; comment `:63` |
| `EV-REC-03` | `:162-206 _update_matching_number`; DB constraint `account/models/account_move_line.py:1341-1357` |
| `EV-REC-04` | `account/models/account_move_line.py:716-781 _compute_amount_residual`; stored `:244-257`; closure test `:778-781` |
| `EV-REC-05` | `account/models/account_move.py:1188 _compute_payment_state` — foreign residual only |
| `EV-REC-06` | `account/models/account_move_line.py:2317-2346 _check_amls_exigibility_for_reconciliation`; **`:2336` compares `self.company_id.root_id`** |
| `EV-REC-07` | `account/models/account_move_line.py:2738-2741` — `[:1]` company selection for the difference entry |
| `EV-REC-08` | `:2718-2724` journal/accounts; `:2827-2850` hard stop on missing configuration; `:2746`, `:2751`, `:2759` date; `stock_account/models/account_move.py:320-334` override |
| `EV-REC-09` | `account/models/account_partial_reconcile.py:513-514` — cash-basis date = today when the matched documents predate the lock |
| `EV-REC-10` | `account/models/account_move_line.py:2483` `account.disable_partial_exchange_diff` config parameter; context keys `:2117`, `:2518-2519`, `:2864` |
| `EV-REC-11` | `account/models/account_partial_reconcile.py:117-133 unlink` reverses; `account/models/account_full_reconcile.py:24-34` same |
| `EV-REC-12` | lock-guard scan over `account_partial_reconcile.py`, `account_full_reconcile.py` (whole files) and `account_move_line.py:2317-2700` → **0 matches** |
| `EV-REC-13` | chatter scan over both settlement model files → **0 `_inherit` / `mail.thread`** |
| `EV-REC-14` | `account/models/account_account.py:918-934 _toggle_reconcile_to_true` (raw `UPDATE`, no partial check) vs `:936-952 _toggle_reconcile_to_false` (guarded) |
| `EV-REC-15` | `account/models/account_move_line.py:761-764` — residual forced to zero on non-reconcilable accounts; `:721` cash exemption |
| `EV-REC-16` | `account_accountant/models/account_bank_statement.py:90-167` cron; `account_accountant/models/bank_rec_widget.py:1409-1413` `Command.clear()` under `force_delete` + `skip_readonly_check` |
| `EV-REC-17` | `account_accountant/wizard/account_auto_reconcile_wizard.py:105-108` — partner clause nested inside the account clause |
| `EV-REC-18` | `account/models/account_bank_statement_line.py:304-331 _compute_is_reconciled`, `:329-331` "no suspense leg" branch; `:475-487 action_undo_reconciliation`; `account/models/account_bank_statement.py:174-176`, `:188-192` |
| `EV-REC-19` | `account/security/ir.model.access.csv:105`, `:108` — billing tier create/write/unlink on both settlement models; **no `ir.rule` for either** |

## FX
| Ref | Citation |
|---|---|
| `EV-FX-01` | `CORE/addons/base/models/res_currency.py:121-141 _get_rates` — `:128-132` rate_query (`name <= date`, `company_id in (False, company.root_id.id)`, `order='company_id.id, name DESC'`), `:133-136` **rate_fallback with no date predicate, `name ASC`**, `:139` `COALESCE((rate_query),(rate_fallback),1.0)` |
| `EV-FX-02` | `:152` derives `company` from the `company_id` context key, `:155` calls `_get_rates(self.env.company, date)` — the derived company is discarded |
| `EV-FX-03` | `account/wizard/account_payment_register.py:993` — `_convert` called with no `company=`; default at `res_currency.py:269` |
| `EV-FX-04` | `account/models/account_move_line.py:135-138 currency_rate` — compute, **not stored**; `:661-673`, `:686-691` |
| `EV-FX-05` | `account/models/account_move.py:475-481 invoice_currency_rate` stored, invoice family only; `:1051-1063` assignment inside `is_invoice()` |
| `EV-FX-06` | `account/models/res_currency.py:85-89`, `:125-142 _create_currency_table` (`ON COMMIT DROP`), `:169-336` four builders; type assignment `account_reports/models/account_report.py:1411-1418` |
| `EV-FX-07` | reporting builders filter `rate.company_id = <root>` strictly (`account/models/res_currency.py:183,211,258,300,316,320`) vs posting `in (False, root)` |
| `EV-FX-08` | rate model fields `CORE/addons/base/models/res_currency.py:342-371` — 6 fields, no type, no source, no tracking, no chatter, no unlink guard |
| `EV-FX-09` | `account_reports/wizard/multicurrency_revaluation.py:137-142` rate in the free-text label; `:169-179` post-and-reverse |
| `EV-FX-10` | `account_reports/models/account_multicurrency_revaluation_report.py:52-54`, `:63-66 options['custom_rate']`, `:71-75` warning, `:58-60` zero refusal |

## Reports
| Ref | Citation |
|---|---|
| `EV-RPT-01` | models `account/models/account_report.py:24`, `:309`, `:537`, `:867`; engines `:548-553` (6) |
| `EV-RPT-02` | dispatch `account_reports/models/account_report.py:3636`; implementations `:3640`, `:3718`, `:3844`, `:4040`, `:4160`; aggregation `:3312` |
| `EV-RPT-03` | filter builder `:2095 _get_report_query` → `:2060 _get_options_domain` |
| `EV-RPT-04` | audit `:4404 action_audit_cell` → `:4472 _get_audit_line_domain`; caret `:4574 open_journal_items` (`:4637` domain) |
| `EV-RPT-05` | `:4528 _get_expression_audit_aml_domain` — returns `None` for aggregation/external/custom at `:4573`; whole-population fallback `:4500-4506`; D/C selector dropped `:4530-4533`, applied post-SQL `:4021` |
| `EV-RPT-06` | `account/models/account_report.py:637 _get_auditable_engines` (5 of 6); `:588 auditable` stored, `readonly=False`; 81 XML overrides |
| `EV-RPT-07` | ageing audit `account_reports/models/account_aged_partner_balance.py:367`, `:388 _build_domain_from_period` (hard-coded 30, hard-coded maturity, no COALESCE, `:384` overwrites the action domain) |
| `EV-RPT-08` | cash flow `account_reports/models/account_cash_flow_report.py:634`, `:659`, `:697` no expression → not auditable; `:143-166 _dispatch_aml_data`; `:305-306` tag join; `:680-710` residual line; `:282`, `:415-443` bare query |
| `EV-RPT-09` | external values `account/models/account_report.py:882`; manual edit `account_reports/models/account_report.py:4739`, `:4801`, `:4863`; carryover `:4183`; annotations `:53`; budgets `:4882` |
| `EV-RPT-10` | `account/security/ir.model.access.csv:138,141,144,147,150` — manager `1,1,1,1` on all five; no `mail.thread` on any |
| `EV-RPT-11` | draft toggle `account_reports/models/account_report.py:894-899`; `parent_state` stored related `account/models/account_move_line.py:69`; warnings `:2730-2747`; PDF marker `account_reports/data/pdf_export_templates.xml:14`, gated label `:169-172` |
| `EV-RPT-12` | consolidation `account_reports/models/account_report.py:2068`, `:1276-1320`; currency table `account/models/res_currency.py:126-139`; parity `CASE ... ELSE 1` at `:181`, `:206`; LEFT JOIN vs JOIN `account_reports/models/account_report.py:1409` vs `:1431`; warning `account_reports/models/balance_sheet.py:10-11` |
| `EV-RPT-13` | export attachment `account_reports/wizard/report_export_wizard.py:48`, `:124-131` — no `res_model`, no `res_id`, no data hash |
| `EV-RPT-14` | report query does re-apply record rules: `account_reports/models/account_report.py:2113 _apply_ir_rules(query)` — **a control, recorded so it is not misread as a leak** |

## Company boundary
| Ref | Citation |
|---|---|
| `EV-CB-01` | accounting record rules: 50 total in 13 files; 35 global and all 35 company-scoping; 23 use `parent_of`, 8 strict `in`, 2 `+[False]`, 2 explicit-False |
| `EV-CB-02` | ledger is strict: `account/security/account_security.xml:147`, `:153` |
| `EV-CB-03` | whole-build denominator: 844 rules, 243 company-scoping, 85 modules; 106 of 243 admit company-less rows |
| `EV-CB-04` | `CORE/api.py:703-720`, `:742-758` — no sanity checks in elevated mode; default = all the user's companies when the key is absent |
| `EV-CB-05` | `account/models/account_move_line.py:56-58 company_id` related-stored from the move — one entry, one company |
| `EV-CB-06` | `CORE/models.py:188-205 check_company_domain_parent_of`; `:207-222` returns an unrestricted domain on a falsy company set |
| `EV-CB-07` | `account_inter_company_rules/models/res_company.py:22-28 intercompany_user_id` default superuser, no company/group filter; `:31-35 _find_company_from_partner` `parent_of` under elevation; `account_inter_company_rules/models/account_move.py:23` no rights check, `:67-68` post |
| `EV-CB-08` | `base/wizard/base_partner_merge.py:424-428` elevated `company_ids` link; `:383-445 _merge` no company check; `:175-183`, `:348-358` |
| `EV-CB-09` | `account/data/service_cron.xml:3-11` no `user_id`; `account/models/account_move.py:5430-5440` search with no company clause, `limit=100` |
| `EV-CB-10` | consolidation: four independent searches over REF18 + `addons_archive` → 0 |

## Custom layer
| Ref | Citation |
|---|---|
| `EV-CUST-01` | `scgl_special_access_rights/models/ir_model.py:12-14` `class Base(models.AbstractModel): _inherit = 'base'`; `:16 def _check_access`; **`:49 return None`** before `:52-54` permission check and `:59-63` rule check; never calls `super()` |
| `EV-CUST-02` | `scgl_special_access_rights/security/ir.model.access.csv` lines 2-5 — `base.group_user,1,1,1,1` on the grant models; no `ir.rule` on either |
| `EV-CUST-03` | `scgl_special_access_rights/models/ir_model.py:31-34` `search(..., limit=1)` then `.filtered()` — non-deterministic with multiple grants; `has_access` unbound if `operation` is outside the four modes |
| `EV-CUST-04` | `om_data_remove/models/model.py:24-27` `"delete from %s"` + `self._cr.commit()`; `:165-176 remove_account`; `:199-250 remove_account_chart`; `:334-348 remove_all`; menu group `om_data_remove/views/view.xml:119`; no ACL file |
| `EV-CUST-05` | `cr_effective_date_entries/wizard/effective_date.py:35 change_to_effective_date`; `:63-68` `button_draft` → `name = False` → date overwrite → `action_post`; `:76` raw `UPDATE stock_valuation_layer SET create_date` |
| `EV-CUST-06` | `import_bridge_axis/wizard/import_journal_entry.py:124-150 create_journal_entry` — number and date from the file, company lookup commented out `:153-161`, journal lookup by name only `:137`, partner auto-create `:126-134` |
| `EV-CUST-07` | `scgl_tax_period_date/models/tax_period.py` — `@api.model` on a multi-create signature; propagates on create only |
| `EV-CUST-08` | elevated ledger creation in the custom layer: `scgl_purchase_advance_payment/wizard/purchase_advance.py:203`; `hr_expense_petty_cash/models/hr_expense_sheet.py:103,115`; `scgl_advance_expense_request/wizard/advance_request_reconcile.py:40,86`, `models/advance_expense_request.py:271`; `account_discount_catalog/wizard/account_order_discount.py:119` |
