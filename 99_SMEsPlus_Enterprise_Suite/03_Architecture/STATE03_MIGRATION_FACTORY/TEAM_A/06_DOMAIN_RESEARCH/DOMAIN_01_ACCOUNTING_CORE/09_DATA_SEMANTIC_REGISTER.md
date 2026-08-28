> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 09 — DATA SEMANTIC REGISTER

| Element | Observed meaning | Migration caution |
|---|---|---|
| `account.code` | Char(64), computed + searchable + inverse. Not a simple stored string — display code is separate (`placeholder_code`) | Do not assume the code column is the authoritative literal |
| `account_type` | 19-value enumeration driving legal reporting and year-end behaviour | Semantic, not cosmetic — drives MM-06 |
| `internal_group` | Coarse grouping: asset / liability / equity / income / expense | Derived from type |
| `reconcile` (account) | Whether items on this account may be matched | Behavioural flag |
| `move_type` | Distinguishes entry / invoice / bill / credit note within one table | The single most semantically loaded field in the domain |
| `state` | Ledger status: draft / posted / cancel | Not settlement status |
| `payment_state` | Settlement status, independent of `state` | Two orthogonal statuses |
| `parent_state` (line) | Denormalized copy of header state | Derived — recompute, never migrate as fact |
| `debit` / `credit` / `balance` | Company-currency amounts; three columns, two degrees of freedom | Redundant trio |
| `amount_currency` | Transaction-currency amount | Meaningless without its currency |
| `reversed_entry_id` | Points from a reversal back to what it reverses | A relationship, not a status |
| `secure_sequence_number` | Gapless inalterability counter for hashed journals | Distinct from the human-readable name |
| `inalterable_hash` | Tamper-evidence chain value | Present only where hash mode was enabled |
| `restrict_mode_hash_table` (journal) | Whether this journal is hash-protected | **Opt-in** |
| Lock dates on company | Six distinct period controls | No single "period closed" flag exists |
