# U73 — Audit Trail Immutability Depth
**Unit**: U73
**Phase**: Second-Pass Depth Closure — P0 Critical
**Scope**: account.move immutability after posting, hash chain algorithm, backdating dual-chatter, sequence lock, button_draft path, CABA interaction
**Modules**: account
**Function-IDs targeted**: RCN-F02, RCN-F03, PCO-F01
**L-levels**: L7, L8, L11
**Proof layers**: P2, P3, P5
**Date**: 2026-10-02
**Status**: GATE-PASS (exit 0, claim-checks=0, neutral-leak-tokens=0)
**Predecessor**: U70 (U70 claims on restrictive_audit_trail/posted_before/hash already committed)

---

## Key Source Files
- `account/models/account_move.py` — primary
- `account/models/account_move_line.py` — line-level hash guards
- `account/models/account_journal.py` — restrict_mode_hash_table
- `account/models/company.py` — restrictive_audit_trail, force_restrictive_audit_trail

Addons root: `account/models/` relative to `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons`

---

## account_audit_log Module Presence
**CONFIRMED ABSENT**: No `account_audit_log` module found in addons directory. All audit trail logic is embedded directly in the `account` module.

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U73-001 | RCN-F02 | account/models/account_move.py:47 | `MAX_HASH_VERSION = 4` | CONST | always | C1 | The module-level constant MAX_HASH_VERSION is 4; this controls the default hash algorithm version used for new entries | NR-U73-001 |
| U73-002 | RCN-F02 | account/models/account_move.py:4597-4598 | `return ['name', 'date', 'journa` | RETURN | hash_version in (2,3,4) | C1 | `_get_integrity_hash_fields()` on account.move returns ['name','date','journal_id','company_id'] for hash versions 2, 3, and 4 | NR-U73-002 |
| U73-003 | RCN-F02 | account/models/account_move.py:4595-4596 | `return ['date', 'journal_id', '` | RETURN | hash_version == 1 | C1 | `_get_integrity_hash_fields()` on account.move returns ['date','journal_id','company_id'] for legacy hash version 1 (excludes 'name') | NR-U73-003 |
| U73-004 | RCN-F02 | account/models/account_move_line.py:3399-3400 | `return ['name', 'debit', 'credi` | RETURN | hash_version in (2,3,4) | C1 | `_get_integrity_hash_fields()` on account.move.line returns ['name','debit','credit','account_id','partner_id'] for hash versions 2, 3, and 4 | NR-U73-004 |
| U73-005 | RCN-F02 | account/models/account_move_line.py:3397-3398 | `return ['debit', 'credit', 'acc` | RETURN | hash_version == 1 | C1 | `_get_integrity_hash_fields()` on account.move.line returns ['debit','credit','account_id','partner_id'] for legacy hash version 1 (excludes 'name') | NR-U73-005 |
| U73-006 | RCN-F02 | account/models/account_move.py:4799 | `current_record = dumps(values,` | CALC | per move | C1 | Hash input is JSON-serialised (json.dumps, sort_keys=True, ensure_ascii=True, no indent, separators=(',',':')) dict of field values keyed as fname for move fields and 'line_<id>_<fname>' for each line field | NR-U73-006 |
| U73-007 | RCN-F02 | account/models/account_move.py:4800 | `hash_string = sha256((previous_` | CALC | per move | C1 | SHA-256 is computed over UTF-8 encoding of (previous_hash_raw + JSON_string); the SHA-256 hex digest is the raw hash value | NR-U73-007 |
| U73-008 | RCN-F02 | account/models/account_move.py:4801 | `f"${hash_version}${hash_string}` | ASSIGN | hash_version >= 4 | C1 | For hash version 4+, the stored inalterable_hash value is prefixed as `$4$<sha256hex>`; for versions 1-3 it is stored as bare hex | NR-U73-008 |
| U73-009 | RCN-F02 | account/models/account_move.py:4789-4790 | `previous_hash = previous_hash.s` | CALC | chaining | C1 | When chaining, if the prior hash starts with '$', only the raw SHA-256 portion (split by '$')[2] is used as the previous_hash input — the version prefix is stripped before concatenation | NR-U73-009 |
| U73-010 | RCN-F02 | account/models/account_move.py:4781-4782 | `return float_repr(field_value,` | CALC | monetary + hash_version >= 3 | C1 | Monetary fields are serialised using float_repr(value, currency.decimal_places) for hash versions 3 and 4, preventing floating-point representation variance | NR-U73-010 |
| U73-011 | RCN-F02 | account/models/account_move.py:4779-4780 | `field_value = field_value.id` | CALC | many2one | C1 | Many2one fields are serialised as their integer database ID (not display name) for hash computation | NR-U73-011 |
| U73-012 | RCN-F02 | account/models/account_move.py:4741-4742 | `for journal, journal_moves in s` | FLOW | grouping | C1 | Hash chains are computed per (journal_id, sequence_prefix) pair — each journal+prefix combination constitutes an independent chronological chain | NR-U73-012 |
| U73-013 | RCN-F02 | account/models/account_move.py:355 | `inalterable_hash = fields.Char(` | SCHEMA | always | C1 | `inalterable_hash` is declared as Char, readonly=True, copy=False, index='btree_not_null'; the btree_not_null index enables efficient filtered lookups on hashed entries | NR-U73-013 |
| U73-014 | RCN-F02 | account/models/account_move.py:354 | `secure_sequence_number = fields` | SCHEMA | always | C1 | `secure_sequence_number` is an Integer field, readonly=True, copy=False, index=True — records the gap-free sequence position within the hash chain | NR-U73-014 |
| U73-015 | RCN-F02 | account/models/account_journal.py:145-146 | `restrict_mode_hash_table = fiel` | SCHEMA | always | C1 | `restrict_mode_hash_table` is a Boolean field on account.journal labelled "Secure Posted Entries with Hash"; when True, all entries are retroactively hashed back to the last hashed entry on post | NR-U73-015 |
| U73-016 | RCN-F02 | account/models/account_journal.py:786-793 | `if 'restrict_mode_hash_table' i` | GUARD | restrict_mode disable attempt | C1 | Disabling restrict_mode_hash_table on a journal that already contains hashed entries raises UserError — the setting is irreversible once hashing has begun | NR-U73-016 |
| U73-017 | RCN-F02 | account/models/account_move.py:3923-3929 | `violated_fields = set(vals).int` | GUARD | inalterable_hash set | C1 | write() on account.move raises UserError if any of the integrity hash fields (name, date, journal_id, company_id) or inalterable_hash itself is included in vals and the move has an inalterable_hash | NR-U73-017 |
| U73-018 | RCN-F02 | account/models/account_move.py:3960-3969 | `unmodifiable_fields = (` | GUARD | move_state == 'posted' | C1 | write() enforces readonly on ['invoice_line_ids','line_ids','invoice_date','date','partner_id','invoice_payment_term_id','currency_id','fiscal_position_id','invoice_cash_rounding_id'] when the effective state is 'posted'; bypassed only by context key skip_readonly_check | NR-U73-018 |
| U73-019 | RCN-F02 | account/models/account_move.py:3930-3935 | `move.posted_before` | GUARD | posted_before, journal_id change | C1 | write() raises UserError if posted_before=True and journal_id is being changed unless the move name is simultaneously reset to '/' or empty — prevents journal reassignment after first post | NR-U73-019 |
| U73-020 | RCN-F02 | account/models/account_move.py:3946-3951 | `move._check_fiscal_lock_dates()` | GUARD | posted + name/date change | C1 | write() calls _check_fiscal_lock_dates() and line_ids._check_tax_lock_date() whenever name or date is modified on a posted move — prevents backdating into locked fiscal periods | NR-U73-020 |
| U73-021 | RCN-F02 | account/models/account_move.py:128 | `tracking=True,` | CONFIG | date field | C1 | The `date` field on account.move carries tracking=True, causing the Odoo chatter to auto-record both old and new date whenever the accounting date is changed | NR-U73-021 |
| U73-022 | RCN-F02 | account/models/account_move.py:140 | `tracking=True,` | CONFIG | state field | C1 | The `state` field on account.move carries tracking=True, automatically recording draft/posted/cancelled transitions in the chatter | NR-U73-022 |
| U73-023 | RCN-F02 | account/models/account_move.py:113 | `tracking=True,` | CONFIG | name field | C1 | The `name` (sequence number) field on account.move carries tracking=True, recording sequence number assignment and changes in the chatter | NR-U73-023 |
| U73-024 | PCO-F01 | account/models/account_move.py:5757-5759 | `'posted_before': True,` | ASSIGN | state → posted | C1 | During _post(), `posted_before` is set to True atomically in the same write() call as `state = 'posted'`; this flag is never reset and persists through all subsequent state transitions | NR-U73-024 |
| U73-025 | PCO-F01 | account/models/account_move.py:4004-4006 | `if vals.get('state') == 'posted'` | TRIGGER | state = posted | C1 | In write(), immediately after state transitions to 'posted' and the recordset is flushed (ensuring name is computed), _hash_moves() is called to compute and store the inalterable_hash for the entry | NR-U73-025 |
| U73-026 | RCN-F02 | account/models/account_move.py:6372-6373 | `if move.inalterable_hash:` | GUARD | button_draft + inalterable_hash | C1 | `_check_draftable()` raises UserError "You cannot reset to draft a locked journal entry." if the move has an inalterable_hash — hashed entries cannot be reset to draft under any circumstances | NR-U73-026 |
| U73-027 | RCN-F02 | account/models/account_move.py:6365-6371 | `if move.tax_cash_basis_rec_id o` | GUARD | button_draft + CABA | C1 | `_check_draftable()` raises UserError if tax_cash_basis_rec_id OR tax_cash_basis_origin_move_id is set on the move — CABA (cash basis tax) journal entries can never be reset to draft | NR-U73-027 |
| U73-028 | RCN-F02 | account/models/account_move.py:6363-6364 | `if move.id in exchange_move_ids:` | GUARD | button_draft + exchange | C1 | `_check_draftable()` raises UserError if the move is referenced as an exchange difference entry in account_partial_reconcile — exchange diff entries cannot be reset to draft | NR-U73-028 |
| U73-029 | RCN-F02 | account/models/account_move.py:6269-6284 | `def button_draft(self):` | FLOW | always | C1 | button_draft() does NOT reset posted_before, inalterable_hash, or name fields — these all survive the draft transition; only state, sending_data, analytic_line_ids, and invoice PDF attachment are affected | NR-U73-029 |
| U73-030 | RCN-F02 | account/models/account_move.py:6279 | `self.line_ids.analytic_line_ids` | FLOW | button_draft | C1 | button_draft() unlinks all analytic_line_ids for the entry's lines — analytic postings are destroyed on reset to draft and recreated on repost | NR-U73-030 |
| U73-031 | RCN-F02 | account/models/account_move.py:5541-5546 | `def _can_be_unlinked(self):` | GUARD | unlink gate | C1 | _can_be_unlinked() returns False if: (1) inalterable_hash is set, (2) date <= fiscal lock date, (3) move is a posted CABA entry, or (4) move has exchange_diff_partial_ids — all four conditions must pass for deletion | NR-U73-031 |
| U73-032 | RCN-F02 | account/models/account_move.py:5548-5549 | `def _is_protected_by_audit_trail` | CHECK | audit trail | C1 | `_is_protected_by_audit_trail()` returns True if ANY move in self has posted_before=True AND company.restrictive_audit_trail=True — this routes _unlink_or_reverse() to cancel instead of delete | NR-U73-032 |
| U73-033 | RCN-F02 | account/models/account_move.py:4068-4077 | `@api.ondelete(at_uninstall=False)` | GUARD | unlink gate | C1 | @api.ondelete hook `_unlink_account_audit_trail_except_once_post` raises UserError preventing deletion of any entry with posted_before=True when company.restrictive_audit_trail=True, unless context force_delete is set | NR-U73-033 |
| U73-034 | RCN-F02 | account/models/account_move.py:5551-5567 | `def _unlink_or_reverse(self):` | FLOW | mixed states | C1 | _unlink_or_reverse() routes each move: cannot_unlink → to_reverse (creates reversal); can_unlink + audit_trail_protected → to_cancel (button_cancel); otherwise → to_unlink (button_draft + unlink) | NR-U73-034 |
| U73-035 | RCN-F03 | account/models/account_move.py:5544 | `posted_caba_entry = self.state =` | CHECK | CABA detection | C1 | A posted CABA entry is detected by checking both tax_cash_basis_rec_id (may be empty if reconciliation was undone) and tax_cash_basis_origin_move_id (preserved permanently) — dual check handles historical versions | NR-U73-035 |
| U73-036 | RCN-F03 | account/models/account_move.py:5749-5752 | `to_post |= move.tax_cash_basis_` | FLOW | reconciliation | C1 | CABA moves are auto-posted during _post() when their originating invoice's reconciliation is detected — the CABA move references both the originating move (tax_cash_basis_origin_move_id) and the partial reconcile record | NR-U73-036 |
| U73-037 | RCN-F02 | account/models/account_move_line.py:1827-1836 | `inalterable_fields = set(self._g` | GUARD | line write | C1 | account.move.line write() blocks modification of hash fields (name, debit, credit, account_id, partner_id) and inalterable_hash if the parent move has inalterable_hash set — line-level hash fields are protected independently | NR-U73-037 |
| U73-038 | RCN-F02 | account/models/account_move.py:1962-1968 | `move.show_reset_to_draft_button` | CALC | UI gate | C1 | show_reset_to_draft_button is computed False if: move has restrict_mode_hash_table True, OR inalterable_hash is set, OR the move is not in cancel/posted state — hides the draft button in UI for restricted entries | NR-U73-038 |
| U73-039 | RCN-F02 | account/models/company.py:258-262 | `restrictive_audit_trail = field` | SCHEMA | company level | C1 | `restrictive_audit_trail` on res.company is a Boolean field with tracking=True, string 'Restrictive Audit Trail' — changes to this flag are themselves chatter-logged at company level | NR-U73-039 |
| U73-040 | RCN-F02 | account/models/company.py:319-323 | `@api.constrains('restrictive_au` | GUARD | disable blocked | C1 | A @api.constrains on restrictive_audit_trail raises ValidationError if an attempt is made to set it False when force_restrictive_audit_trail is True — localizations can permanently lock the audit trail | NR-U73-040 |
| U73-041 | RCN-F02 | account/models/company.py:347-349 | `def _compute_force_restrictive_` | CALC | base value | C1 | `_compute_force_restrictive_audit_trail()` returns False by default in base account module — it is a hook for localizations to override and force the audit trail on | NR-U73-041 |
| U73-042 | RCN-F02 | account/models/account_move.py:4635 | `chain['moves']._message_log_bat` | TRIGGER | hash secured | C1 | `_hash_moves()` posts a chatter internal note "This journal entry has been secured." on each move at the moment it receives its inalterable_hash — provides an audit timestamp of hash assignment | NR-U73-042 |
| U73-043 | RCN-F02 | account/models/account_move.py:4761-4764 | `raise UserError(_(` | RAISE | sequence gap | C1 | `_get_chains_to_hash()` raises UserError "A gap has been detected in the sequence." if sequence numbers within the chain are not contiguous — enforces no-gap integrity before hashing proceeds | NR-U73-043 |
| U73-044 | RCN-F02 | account/models/account_move.py:4671-4674 | `last_move_hashed = self.env['acc` | FLOW | chain anchor | C1 | Hash chain anchors on the highest sequence_number entry that already has inalterable_hash set; only entries with higher sequence_numbers and inalterable_hash=False are included in the new hash batch | NR-U73-044 |
| U73-045 | RCN-F02 | account/models/account_move.py:6272-6273 | `if any(move.need_cancel_request` | GUARD | e-invoice lock | C1 | button_draft() raises UserError if need_cancel_request=True for any move — localization hook that prevents resetting e-invoices sent to government; base module returns False (no blocking) | NR-U73-045 |
| U73-046 | RCN-F02 | account/models/account_move.py:320 | `store=True, readonly=False, tra` | CONFIG | posted_before | C1 | `posted_before` field is defined with tracking=True (line 320 context), copy=False — changes to this flag (False→True on first post) are recorded in the chatter | NR-U73-046 |
| U73-047 | RCN-F02 | account/models/account_move.py:4601-4602 | `def _get_integrity_hash_fields_` | FLOW | completeness | C1 | `_get_integrity_hash_fields_and_subfields()` concatenates move-level hash fields with 'line_ids.<subfield>' references for each line hash field — defines the complete set of fields whose mutation is blocked when the hash is set | NR-U73-047 |
| U73-048 | RCN-F02 | account/models/account_move.py:4004-4006 | `self.flush_recordset()` | FLOW | hash timing | C1 | Before _hash_moves() is called on post, flush_recordset() is called to ensure the computed `name` field (sequence number) is persisted to DB — the name is part of the hash input for versions 2+ | NR-U73-048 |

---

## Function-ID Index (U73 additions)
No new Function-IDs. All claims align to existing RCN-F02, RCN-F03, PCO-F01.

---

## C1/AWT Summary
- **C1 claims**: 48 (all claims)
- **AWT claims**: 0
- **TH claims**: 0

---

## Critical Findings Summary

### Hash Algorithm (complete)
- MAX_HASH_VERSION = 4
- Move fields hashed (v4): name, date, journal_id (as ID), company_id (as ID)
- Line fields hashed (v4): name, debit, credit, account_id (as ID), partner_id (as ID)
- Hash = SHA-256(prev_hash_raw + JSON(values, sort_keys=True))
- Stored as `$4$<hex>` (v4); bare hex (v1-3)
- Chain: per (journal_id, sequence_prefix), ordered by sequence_number
- Monetary fields: float_repr(value, currency.decimal_places) for v3+

### write() Immutable Fields (complete list when posted)
- When inalterable_hash set: name, date, journal_id, company_id (move level); name, debit, credit, account_id, partner_id (line level)
- When state == 'posted' (bypassed by skip_readonly_check): invoice_line_ids, line_ids, invoice_date, date, partner_id, invoice_payment_term_id, currency_id, fiscal_position_id, invoice_cash_rounding_id
- journal_id: blocked if posted_before=True unless name reset

### button_draft() Information Preserved vs. Lost
- **Preserved**: posted_before, name (sequence number), inalterable_hash, all line data, original accounting entries
- **Lost/Reset**: state → draft, sending_data → False, analytic_line_ids (unlinked), invoice PDF attachment (detached for sale docs)
- **BLOCKED entirely if**: inalterable_hash is set, OR move is CABA entry, OR exchange diff entry

### Sequence Lock
- posted_before set True on first post, never reset
- name (sequence number) computed on post, tracked, survives button_draft
- journal_id change blocked if posted_before=True and name not reset

### CABA Interaction
- CABA entries: cannot be unlinked when posted, cannot go to draft
- Dual detection: tax_cash_basis_rec_id + tax_cash_basis_origin_move_id
- Auto-posted on reconciliation event

### account_audit_log module
- ABSENT in Community edition — not present in addons directory
