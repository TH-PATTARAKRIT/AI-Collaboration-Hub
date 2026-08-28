> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 21 — QUARANTINE REGISTER

| ID | Item | Reason | Class | Status |
|---|---|---|---|---|
| Q-01 | `account_accountant` (OEEL-1) | Proprietary — source body never read | F | QUARANTINE |
| Q-02 | `account_reports` (OEEL-1) | Proprietary | F | QUARANTINE |
| Q-03 | `account_asset` (OEEL-1) | Proprietary | F | QUARANTINE |
| Q-04 | `account_budget` (OEEL-1) | Proprietary | F | QUARANTINE |
| Q-05 | `accountant` (OEEL-1) | Proprietary | F | QUARANTINE |
| Q-06 | `bi_print_journal_entries` | CLASS-D undeclared licence, accounting-coupled | D | HOLD |
| Q-07 | `full_summarize_bills` | CLASS-D undeclared licence | D | HOLD |
| Q-08 | `dev_print_cheque` | CLASS-D undeclared licence | D | HOLD |
| Q-09 | `ks_dashboard_ninja`, `ks_dn_advance` | Purchased OPL-1, separately classified per Boss decision 6 | F | SEPARATE CLASSIFICATION |
| Q-10 | Vendor implementation patterns F-12…F-17 | Class E — must not become target design | E | RESTRICTED |
| Q-11 | Dump row-level data | Personal/business data; no restore performed; nothing extracted or committed | — | RESTRICTED |

## CONFIRMATIONS
- **No OEEL-1 or OPL-1 source body was opened at any point in this session.**
- No CLASS-D module was read for design content.
- No raw source, dump, customer data, credentials or secrets were written to the factory path
  or staged for GitHub.
- The single ephemeral dump copy made for the failed `pg_restore` attempt was deleted.
