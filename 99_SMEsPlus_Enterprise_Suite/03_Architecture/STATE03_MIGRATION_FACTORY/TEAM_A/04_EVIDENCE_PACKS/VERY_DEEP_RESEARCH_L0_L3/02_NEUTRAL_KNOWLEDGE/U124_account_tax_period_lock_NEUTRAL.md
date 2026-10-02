# U124 — Tax Period Lock Enforcement (GAP-027) — Neutral Knowledge

**Unit ID:** U124 | **G Group:** G01 | **Priority:** P1

---

## Overview

This document records neutral (non-technical) knowledge about the tax period lock date feature in the Community accounting module. All claims are source-proven or clearly marked as absent.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|----------|-------------|---------|--------|-------|-----------|-------|---------------------|-------------|
| U124-C01 | F-TAXLOCK-FIELD | account/models/company.py line 81 | tax_lock_date field with string Tax Return Lock Date | C1 | Always | C1,TH | Tax return lock date field is defined on the company model as a tracked date field | Tax period lock date stored on company record |
| U124-C02 | F-TAXLOCK-FIELD | account/models/company.py line 109 | user_tax_lock_date computed field | C1 | Always | C1 | Effective lock date per user accounts for active temporary exceptions granted to that user | Per-user effective tax period lock date |
| U124-C03 | F-TAXLOCK-COMPUTE | account/models/company.py lines 421 to 426 | compute method for user tax lock date | C1 | Always | C1 | Computation checks for active temporary exceptions for the current user before returning the enforced date | User-specific tax lock date taking exceptions into account |
| U124-C04 | F-TAXLOCK-VIOLATION | account/models/company.py lines 675 to 710 | violation checking method accepting tax parameter | C1 | tax check enabled | C1,TH | System checks whether a given accounting date falls within the locked tax period and returns the violated lock date | Multi-type lock date violation detection including tax period |
| U124-C05 | F-TAXLOCK-CHECK | account/models/account_move_line.py lines 1526 to 1543 | check method on journal entry lines | C1 | line touches tax report | C1,TH | Any posted journal entry line that carries tax information raises a blocking error if its date falls within the locked tax period | Blocking error on tax-bearing journal lines in locked period |
| U124-C06 | F-TAXLOCK-TRIGGER-WRITE | account/models/account_move.py lines 3950 to 3956 | write method on journal entries | C1 | posted entry, date or state change | C1,TH | Changing the date or state of a posted journal entry triggers the tax period lock check on all its lines | Tax lock check triggered by journal entry date or state change |
| U124-C07 | F-TAXLOCK-TRIGGER-WRITE2 | account/models/account_move.py lines 4001 to 4002 | post-write check on posted entries | C1 | after write when posted | C1,TH | After any write operation, entries that are in posted state have their lines re-verified against the tax period lock | Post-write re-verification of tax lock on posted entries |
| U124-C08 | F-TAXLOCK-TRIGGER-CREATE | account/models/account_move_line.py lines 1794 to 1795 | create method on journal entry lines | C1 | sentinel context key absent | C1,TH | Creating new journal entry lines triggers the tax period lock check unless an internal bypass sentinel is present in context | Tax lock check triggered on journal entry line creation |
| U124-C09 | F-TAXLOCK-TRIGGER-UNLINK | account/models/account_move_line.py lines 2001 to 2004 | unlink method on journal entry lines | C1 | sentinel context key absent | C1,TH | Deleting journal entry lines triggers the tax period lock check before deletion proceeds | Tax lock check triggered on journal entry line deletion |
| U124-C10 | F-TAXLOCK-TRIGGER-WRITE3 | account/models/account_move_line.py lines 1882 and 1888 and 1925 | write method on journal entry lines | C1 | write with tax-relevant fields | C1,TH | Modifying journal entry line fields triggers the tax period lock check both before and after the underlying data operation | Tax lock check triggered on journal entry line modification |
| U124-C11 | F-TAXLOCK-MESSAGE | account/models/account_move.py lines 745 and 1932 to 1936 | warning message field on journal entries | C1 | draft entry with date in locked period | C1,TH | A computed warning message on journal entries notifies the user that the entry date falls within a locked period and states the date it will be rescheduled to upon posting | Informational tax lock warning message on journal entry |
| U124-C12 | F-TAXLOCK-ALERT | account/models/account_move.py lines 2464 to 2467 | alert dictionary populated with tax lock message | C1 | accounting user with entry in locked period | C1,TH | A named alert is surfaced in the interface when the warning message is present, visible to users with accounting access | Interface alert for tax period lock date on journal entry |
| U124-C13 | F-TAXLOCK-RESCHEDULING | account/models/account_move.py lines 6714 to 6751 | accounting date calculation method | C1 | lock dates violated | C1,TH | When the proposed accounting date falls within a locked period, the system advances it past the latest lock date and rounds it to the end of the applicable sequence period | Automatic date advancement past tax lock period on posting |
| U124-C14 | F-TAXLOCK-EXCEPTION | account/models/account_lock_exception.py lines 54 and 79 to 82 | lock exception model with tax return lock date selection | C1 | active exception exists for user | C1 | A dedicated exception record can be created to temporarily relax the tax period lock date for a specific user or all users, with an optional expiry time | Per-user temporary relaxation of tax period lock date |
| U124-C15 | F-TAXLOCK-SOFT-LIST | account/models/company.py lines 57 to 67 | list of soft and hard lock date types | C1 | Always | C1 | Five lock date types are present in Community: global, tax return, sales, purchase, and hard lock; the first four are soft locks that allow exceptions while the hard lock is irreversible | Five-type period lock taxonomy in Community accounting |
| U124-C16 | F-TAXLOCK-VALIDATE | account/models/company.py lines 552 to 605 | lock change validation method | C1 | Always | C1 | Validation on company record changes checks hard lock date monotonicity, draft entries in hard-locked period, and unreconciled bank lines; soft lock dates including the tax lock date have no rollback prevention | Lock date change validation without restriction on tax lock rollback |
| U124-C17 | F-TAXLOCK-AFFECT-TAX | account/models/account_move_line.py lines 1522 to 1524 | method detecting tax-report-affecting lines | C1 | Always | C1,TH | A journal entry line is considered to affect the tax report if it carries direct taxes, is itself a generated tax line, or has tax classification tags applied to it | Detection of journal lines that affect the tax period report |
| U124-C18 | F-TAXLOCK-AFFECT-MOVE | account/models/account_move.py lines 5315 to 5316 | method detecting tax-report-affecting entries | C1 | Always | C1,TH | A journal entry is considered to affect the tax report if any of its lines carry tax information; this determination drives whether the tax lock date warning and rescheduling apply | Move-level detection of tax report impact |
| U124-C19 | F-TAXLOCK-AUTOSET | account/models/company.py line 85 | field help text describing automatic setting | ABSENT | Tax closing entry posted | GAP | The help text on the tax lock date field states it is automatically advanced when a tax period closing entry is posted, but no code implementing this automation exists in the Community accounting module; the mechanism resides in a separate module not included in Community | Automatic tax lock date advancement on closing entry post — absent in Community |
| U124-C20 | F-TAXLOCK-POS | point_of_sale/models/res_company.py lines 44 to 67 | constraint preventing lock date advance over open sessions | C1 | Open sessions exist | C1,TH | The point-of-sale module adds a constraint that prevents advancing the tax lock date past the start date of any open sales session, protecting those sessions from being unable to close | Protection of open sales sessions from tax lock date advancement |
| U124-C21 | F-TAXLOCK-TAX-TAGS-WIZ | account_update_tax_tags/wizard/account_update_tax_tags_wizard.py lines 25 to 32 | tax tag update wizard date initialization | C1 | tax lock date is set | C1 | The tax classification tag update wizard initializes its start date to one day after the current tax lock date and warns users if they attempt to process dates within the locked period | Tax tag update wizard boundary respect for locked tax period |

---

## GAP-027 Summary

**Status:** PARTIAL

- **Proven (C1):** Core tax period lock date field, enforcement on all journal entry create/write/unlink operations, per-user exception support, UI warning and alert, automatic date rescheduling.
- **Absent (Community):** Automatic advancement of tax lock date when a tax period closing entry is posted — this mechanism exists in a separate non-Community module (Enterprise or localization-specific tax report module).
- **Thai Relevance (TH):** All enforcement claims apply to Thai-locale deployments. Thai tax compliance benefits directly from the tax period lock: VAT returns once filed cannot be re-impacted by backdated entries. The absence of auto-set means Thai deployments on Community must manually advance the lock date after filing.
