> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 04 — FUNCTION REGISTER

| ID | Function | Observed behaviour | Evidence |
|---|---|---|---|
| FN-01 | Post an entry | `action_post` → `_post(soft=True)`; soft posting tolerates some conditions rather than failing hard | SE-10 |
| FN-02 | Reset to draft | `button_draft`; guarded — move must currently be posted or cancelled | SE-11, SE-12 |
| FN-03 | Cancel an entry | `button_cancel` | SE-11 |
| FN-04 | Assert balance | `_check_balanced` executed as a context manager wrapping create/write; raises UserError naming unbalanced entries | SE-03 |
| FN-05 | Suppress balance assertion | `_disable_recursion(..., 'check_move_validity', default=True, target=False)` — the invariant can be turned off for a block of work | SE-04 |
| FN-06 | Detect unbalanced entries | `_get_unbalanced_moves`; source comment warns computed stored fields are unreliable during create/write | SE-05 |
| FN-07 | Reverse an entry | `_reverse_moves` creates opposing move with `reversed_entry_id` set | SE-08 |
| FN-08 | Auto-reconcile reversal | On posting, draft reversals of posted originals are reconciled back to the original | SE-09 |
| FN-09 | Compute entry name | `_compute_name` with `highest_name`, prefix/number split, state-aware placeholder | SE-13 |
| FN-10 | Maintain inalterability sequence | `secure_sequence_number` — gapless counter for hashed journals | SE-13 |
| FN-11 | Validate journal vs type | `@api.constrains('journal_id','move_type')` | SE-06 |
| FN-12 | Validate tax country | `@api.constrains('line_ids','fiscal_position_id','company_id')` | SE-06 |
| FN-13 | Validate currency rate | `@api.constrains('invoice_currency_rate')` | SE-06 |
| FN-14 | Require date for auto-post | `@api.constrains('auto_post','invoice_date')` | SE-06 |
| FN-15 | Guard hash-mode disable | Journal write blocks clearing `restrict_mode_hash_table` where hashed entries exist | SE-23 |
| FN-16 | Guard account deprecation | Deprecation refused where the account is used by tax repartition | SE-21 |
| FN-17 | Lock exception | Time-boxed override of a lock date with audit-trail interrogation | SE-26 |
