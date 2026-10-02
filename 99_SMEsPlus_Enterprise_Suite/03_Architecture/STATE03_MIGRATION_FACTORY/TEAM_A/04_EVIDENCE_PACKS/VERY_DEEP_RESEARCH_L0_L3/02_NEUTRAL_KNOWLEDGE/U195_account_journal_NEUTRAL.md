# U195 — account.journal: Neutral Knowledge Reference
**Level:** L3 Deep Technical — Neutral/Migration-Safe Framing  
**Unit:** U195 | Group: G01 | Priority: P1  
**Odoo Version:** 19.0.post20260921 Community  
**Produced:** 2026-10-02  

---

## VDR Claims Table — 22 Claims

| # | Claim ID | Topic | Claim Statement | Evidence Location | Line(s) | Confidence | Odoo 19 Delta | Migration Risk | Notes |
|---|---|---|---|---|---|---|---|---|---|
| 1 | U195-C01 | Type field — six values | The journal type selection in Odoo 19 has six options: sale, purchase, cash, bank, credit, general. The `credit` type for Credit Card is new in Odoo 19. | account_journal.py | 106–119 | HIGH | NEW: credit type added | MEDIUM — data migration must map legacy credit-card bank journals to new `credit` type | Was bank type in prior versions |
| 2 | U195-C02 | Code field — prefix auto-generation | The code field (max 5 chars, unique per company) is auto-generated with type-specific prefixes: INV (sale), BILL (purchase), CSH (cash), BNK (bank), CCD (credit), MISC (general), followed by an incrementing integer 1–99. | account_journal.py | 877–895 | HIGH | CCD prefix added for credit | LOW — auto-generation logic unchanged for existing types | |
| 3 | U195-C03 | Code field — uniqueness constraint | Journal codes are enforced unique per company via a PostgreSQL UNIQUE constraint `(company_id, code)`. Attempting to duplicate a code raises a database-level constraint violation. | account_journal.py | 293–296 | HIGH | No delta | LOW | |
| 4 | U195-C04 | sequence.mixin — stored columns | Every `account.move` record stores `sequence_prefix` and `sequence_number` as computed-stored columns derived from the entry name by regex parsing. These power the "last sequence" lookup. | sequence_mixin.py | 47–48, 183–191 | HIGH | No delta | LOW | |
| 5 | U195-C05 | sequence.mixin — regex hierarchy | Five regex patterns determine how the sequence resets: year-range-monthly → monthly → year-range → yearly → fixed (never). The first matching pattern wins. Pattern choice affects the date window used to find the previous sequence number. | sequence_mixin.py | 41–46, 200–219 | HIGH | No delta | MEDIUM — custom sequence formats must be tested against new regex hierarchy | |
| 6 | U195-C06 | sequence_override_regex | A journal-level text field allows operators to supply a custom regex overriding all default sequence parsing. When set, it replaces monthly, yearly, and fixed patterns on all entries in that journal. | account_journal.py | 199–203; account_move.py | 85–98 | HIGH | No delta | MEDIUM — if previously unsupported, operators may now need this field to handle non-standard naming | |
| 7 | U195-C07 | refund_sequence — dedicated credit note series | When True (default for sale/purchase), credit notes get a separate number series distinct from invoices. The `_get_last_sequence_domain` SQL filter separates move_type `in_refund`/`out_refund` from non-refund entries. | account_journal.py | 177–182, 703–706; account_move.py | 4213–4215 | HIGH | No delta | MEDIUM — migration must preserve whether existing journals used a separate refund sequence | |
| 8 | U195-C08 | payment_sequence — dedicated payment series | When True (default for bank/cash/credit), payment records (those with `origin_payment_id != False`) get a separate number series. SQL filter is: `origin_payment_id IS NOT NULL`. | account_journal.py | 183–187, 708–711; account_move.py | 4216–4217 | HIGH | No delta | LOW for bank/cash; MEDIUM for credit (new type) | |
| 9 | U195-C09 | restrict_mode_hash_table — enables hash chain | When this Boolean is True on a journal, every posted entry triggers a retroactive SHA-256 hash chain from that entry back to the last hashed entry. Disabling it is blocked once any hashed entry exists. | account_journal.py | 145–146, 786–793 | HIGH | No delta | HIGH — once enabled, cannot be disabled; data migration must carry hash state | |
| 10 | U195-C10 | inalterable_hash — stored hash value | The SHA-256 hash is stored in `inalterable_hash` on account.move. Once set, writing to any integrity-hash field (name, date, journal_id, company_id, and line amounts) raises a blocking error. | account_move.py | 355, 3923–3924, 4592–4598 | HIGH | v4 adds version prefix `$4$` | HIGH — hash versioning must be understood for audit/integrity reports | |
| 11 | U195-C11 | bank_account_id — ownership constraint | A bank journal's bank account (res.partner.bank) must have its partner_id equal to the journal's company partner_id. Accounts owned by customers/suppliers cannot be linked to a bank journal. | account_journal.py | 247–255, 586–595 | HIGH | No delta | MEDIUM — company partner links must be clean before migration | |
| 12 | U195-C12 | bank_statements_source — extensible feed source | The `bank_statements_source` field is a Selection backed by an extension point (`_get_bank_statements_available_sources`). Base only provides `'undefined'`. Online sync and import modules register their own source codes. | account_journal.py | 65–69, 253 | HIGH | No delta | LOW for base; MEDIUM if using bank sync modules | |
| 13 | U195-C13 | suspense_account_id — pending reconciliation | Available only for bank, cash, and credit journals. Bank statement lines are posted to this account until reconciliation finds the correct final account. Defaults to company-wide suspense account. Domain: `asset_current`. | account_journal.py | 130–136, 509–518 | HIGH | credit type also gets suspense | MEDIUM — suspense account config must exist in chart of accounts | |
| 14 | U195-C14 | profit_account_id / loss_account_id — cash difference | These two accounts (income type for profit, expense type for loss) record the difference when the physical cash count does not match the computed balance. Auto-filled from company defaults for cash and bank journals. | account_journal.py | 234–243, 981–984 | HIGH | No delta | LOW — standard CoA setup covers this | |
| 15 | U195-C15 | account_control_ids — removed in Odoo 19 Community | No native `account_control_ids` field exists on account.journal in Odoo 19 Community. The field name appears only as a dynamically created test custom field (`x_account_control_ids`) for account-merge wizard testing. The account restriction mechanism is no longer part of Community core. | account_journal.py (absent); tests/common.py | 2329–2336 | HIGH | REMOVED | HIGH — workflows relying on journal-level account restriction require a custom module in v19 | |
| 16 | U195-C16 | alias_id — email-to-invoice creation | Sale and purchase journals automatically get a mail alias (model: account.move). Incoming emails matching the alias create invoices or bills. The move_type is set from journal type (sale→out_invoice, purchase→in_invoice). | account_journal.py | 257–260, 821–853 | HIGH | No delta | MEDIUM — alias domain must be configured; multi-company appends company name to alias | |
| 17 | U195-C17 | company_id — strict isolation | Each journal belongs to exactly one company (required, readonly). The company cannot be changed once journal entries exist. The `check_company_domain_parent_of` means parent-company journals are visible to child companies. Journals are never shared across unrelated companies. | account_journal.py | 172–173, 597–604 | HIGH | No delta | HIGH — multi-company setup must define one journal set per company leaf | |
| 18 | U195-C18 | payment method lines — bank/cash/credit only | `inbound_payment_method_line_ids` and `outbound_payment_method_line_ids` are only populated for type in (bank, cash, credit). Sale/purchase/general journals have no payment method lines. | account_journal.py | 205–233, 462–496 | HIGH | credit type added | MEDIUM — credit journal needs payment method setup | |
| 19 | U195-C19 | is_self_billing — per-partner sequence | When `is_self_billing` is True, the sequence domain adds a `commercial_partner_id` filter, so each partner gets an independent numbering series within the same journal. | account_journal.py | 120–123; account_move.py | 4218–4223 | HIGH | No delta | MEDIUM — self-billing customers must be identified before migration | |
| 20 | U195-C20 | Archiving blocked by draft entries | Archiving a journal (active=False) raises ValidationError if any account.move in that journal is in state='draft'. Operator must post or delete all drafts first. | account_journal.py | 677–691 | HIGH | No delta | LOW — operational process issue, not schema | |
| 21 | U195-C21 | non_deductible_account_id — private share | An optional account for the private portion of mixed business/personal expenses. Typically used with purchase journals in countries with partial VAT recovery rules. | account_journal.py | 137–144 | HIGH | No delta | LOW | |
| 22 | U195-C22 | sequence concurrency — DB-level locking | The `sequence.mixin` cache uses `cr.cache` (PostgreSQL transaction cache) and relies on the unique constraint on `account_move.name` to serialize concurrent sequence assignments. Heavy-load environments without the unique index receive a WARNING. | sequence_mixin.py | 65–86, 88–112 | HIGH | No delta | LOW for normal load; MEDIUM for bulk-import scenarios | |

---

## Summary of Migration-Relevant Deltas (Odoo 19 vs Odoo 16/17)

| Change | Impact |
|---|---|
| New `credit` type added (Credit Card) | Existing bank journals used for credit cards must be re-typed |
| `CCD` code prefix for credit journals | Auto-generation will produce CCD1, CCD2, etc. |
| `account_control_ids` removed from Community | Any restriction on account usage per journal requires custom module |
| Hash version upgraded to v4 (prefix `$4$`) | Existing hashed entries use older format; integrity report must handle multi-version |
| `non_deductible_account_id` — verify if new in v19 | Check chart template setup |

---

## Key Architectural Facts (Migration-Safe Language)

1. A journal is the **sole dimension** that determines sequence generation for account entries. Both the prefix pattern and the reset periodicity are derived from the entry name via regex, not stored separately.

2. The hash chain operates **per-journal, per-sequence-prefix**. Enabling it on a production journal retroactively secures all unprotected posted entries in that prefix chain.

3. Bank statement lines always land on the **suspense account** first; reconciliation moves the balance to the real account. The suspense account must be type `asset_current`.

4. Cash differences (physical vs computed) are posted to `profit_account_id` (over) or `loss_account_id` (short) at cash session close. These are set at journal level, not company level, so each cash register can post to different accounts.

5. A journal is irrevocably tied to one company; attempting to reassign it once entries exist raises a hard error. Multi-company installations must provision journals per entity before go-live.
