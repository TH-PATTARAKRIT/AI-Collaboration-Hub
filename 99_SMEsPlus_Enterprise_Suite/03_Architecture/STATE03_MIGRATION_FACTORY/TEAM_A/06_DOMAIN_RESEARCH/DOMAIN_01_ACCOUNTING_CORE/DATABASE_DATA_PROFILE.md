# DATABASE DATA PROFILE — DOMAIN_01 (CORRECTED, CORR-01)

## WHAT WAS AND WAS NOT DONE
`pg_restore -l` (**listing only**) was executed. **No restore was performed, no database was
created, no server was started, and no row was read.** Consequently:

```
RECORD POPULATION (row counts / value distributions) = NOT OBTAINED
```

This is a deliberate boundary, not a failure: obtaining row counts would require materialising
a database containing customer business and personal data, which this round did not authorise
and did not do.

## WHAT DIRECT OBSERVATION DID ESTABLISH
**Data sections exist** for every accounting-core table — `account_move`, `account_move_line`,
`account_account`, `account_journal`, `account_full_reconcile`, `account_partial_reconcile`,
`account_lock_exception` each carry exactly one `TABLE DATA` TOC entry. The dump therefore
*contains* accounting data; its volume is not established by a TOC listing.

Database-wide: **1,395 TABLE DATA entries**, matching the prior table inventory exactly.

## CARRIED-FORWARD CHARACTERISATION (PRIOR-EVIDENCE CONFIRMED, not re-verified)
Prior approved evidence characterises `iTEST02` as a **configuration / UAT database**, with
approximately **6 journal entries and 23 journal lines** and **zero** withholding-tax
certificates. This round did **not** re-verify those figures — a TOC listing cannot show them.

| Claim | Status |
|---|---|
| Accounting data sections exist in the dump | **DIRECTLY RE-VERIFIED** |
| 1,395 tables carry data sections | **DIRECTLY RE-VERIFIED** |
| ~6 entries / 23 lines | **PRIOR-EVIDENCE CONFIRMED — NOT RE-VERIFIED** |
| Actual posting volumes, value distributions, balance-in-practice | **NOT RE-VERIFIED** |

## CONSEQUENCE — UNCHANGED AND IMPORTANT
Accounting Core behaviour still **cannot be evidenced from data**. Whether the entries in this
snapshot actually balance (`Σdebit = Σcredit` at data level) is **EVIDENCE_MISSING** — see
`CRITICAL_FINDING_REGISTER.md` CF-01. Closing it requires a restore into an isolated
environment under a specific authorisation, which has not been given.

Gap retained: **GAP-D01-03**.
