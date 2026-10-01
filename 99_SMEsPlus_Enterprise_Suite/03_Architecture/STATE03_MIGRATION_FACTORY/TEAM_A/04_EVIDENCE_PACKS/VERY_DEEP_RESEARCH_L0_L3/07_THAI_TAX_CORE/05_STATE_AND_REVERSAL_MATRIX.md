# State and Reversal Matrix

> **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.** Source/dump evidence only — not runtime proof, not statutory proof. No V-level, no Complete, no coverage percentage. Assembled mechanically from the unit files named in each row; Restricted Technical Evidence (this file) is separate from the Neutral Clean-Room Knowledge Pack.


| Unit | Document/entity | State or event | Trigger | Reversal / cancel / correction path | Blocked when | Claim-IDs |
|---|---|---|---|---|---|---|
| TXA2 | Customer invoice | draft -> posted | Post / Confirm by invoicing user; online payment confirmation; auto-post cron | Reset to draft (if allowed) or credit note | negative total; no customer; vendor needs bill date; inactive journal/account; hashed or locked states block later reversal only | VDR-TXA2-C009, VDR-TXA2-C010, VDR-TXA2-C029, VDR-TXA2-C027, VDR-TXA2-C290 |
| TXA2 | Customer invoice | posted -> draft | Reset to Draft | Repost keeps the same number | hash; cash-basis/exchange entry; cancel-request localization; date inside fiscal/sale/hard lock or tax lock for tax items | VDR-TXA2-C030, VDR-TXA2-C031, VDR-TXA2-C033, VDR-TXA2-C094, VDR-TXA2-C121 |
| TXA2 | Customer invoice | posted -> cancelled | Cancel (via reset to draft) | Reset to draft again | same as reset; payments stay posted | VDR-TXA2-C032, VDR-TXA2-C036, VDR-TXA2-C125 |
| TXA2 | Customer invoice | posted + credit note | Reverse / Credit Note button | Credit note is itself reversible; replacement via new draft copy | original not posted; selection spans companies; journal type mismatch | VDR-TXA2-C011, VDR-TXA2-C012, VDR-TXA2-C015, VDR-TXA2-C164 |
| TXA2 | Vendor bill | draft -> posted | Post; auto-complete from purchase order | Reset to draft or vendor credit note | bill date missing; negative total; locked period shifts date | VDR-TXA2-C055, VDR-TXA2-C056, VDR-TXA2-C139, VDR-TXA2-C082 |
| TXA2 | Customer / vendor credit note | draft -> posted (+ reconcile with original) | Post of reversal draft or immediate-cancel reversal | Reset to draft (not hashed); new invoice | negative total; lock shift; original not posted | VDR-TXA2-C133, VDR-TXA2-C137, VDR-TXA2-C128 |
| TXA2 | Sales / purchase receipt | draft -> posted | Post | Reversal through the wizard from a list (no Credit Note button); reset/cancel as invoices | receipt customer not enforced (inference); no title on print | VDR-TXA2-C021, VDR-TXA2-C040, VDR-TXA2-C028, VDR-TXA2-C013, VDR-TXA2-C014 |
| TXA2 | Debit note (optional module) | draft linked to origin -> posted | Debit Note wizard then Post | Reverse via credit note; debit of debit refused | module not installed in dump; origin not posted or already debited | VDR-TXA2-C002, VDR-TXA2-C143, VDR-TXA2-C146 |
| TXA2 | Journal entry with taxes | posted -> reversed | Reverse Entry (wizard); cancel/immediate reversal | Reversal entry posted and reconciled | hash; locked period | VDR-TXA2-C229, VDR-TXA2-C132, VDR-TXA2-C031 |
| TXA2 | Hashed document | secured | Hash on post or on demand | Only credit note/reversal | reset, cancel, delete, hash-field edit, line deletion | VDR-TXA2-C187, VDR-TXA2-C191, VDR-TXA2-C192, VDR-TXA2-C031, VDR-TXA2-C136 |
| TXA2 | Cash-basis tax entry | created / reversed | Reconcile / unreconcile payment | Reversal created automatically on unreconcile | cannot be reset to draft | VDR-TXA2-C218, VDR-TXA2-C220, VDR-TXA2-C031 |
| TXA2 | Company lock date | set / lowered / removed | Company record update (programmatic) | Soft lock: exception or lowering; hard lock: none | hard lock lowering/removal; hard lock with drafts; fiscal/hard lock with unreconciled statement lines | VDR-TXA2-C109, VDR-TXA2-C102, VDR-TXA2-C075 |
| TXA2 | Lock exception | create / revoke / expire | Created programmatically by an accounting administrator; revoked by an administrator | Revoke; expires automatically | more than one lock field; copy; non-manager revoke | VDR-TXA2-C102, VDR-TXA2-C103, VDR-TXA2-C104 |
| TXA2 | Numbered document | delete | Delete by user | Reverse instead; administrators may delete with warning | not last in chain for non-administrators; posted lines; audit trail on; hashed | VDR-TXA2-C183, VDR-TXA2-C165, VDR-TXA2-C269, VDR-TXA2-C100 |
| TXA2 | Draft dated inside a lock | post | Post | Date shifted instead of refused | none (shift) ; edits afterwards refused | VDR-TXA2-C083, VDR-TXA2-C070, VDR-TXA2-C071 |
| TXA2 | Stock closing entry | create / post | Manual action or valuation cron | Reverse by dated entry/cancel | fiscal/hard lock shifts the date; cron skips manual-period companies | VDR-TXA2-C302, VDR-TXA2-C303, VDR-TXA2-C084 |
| TXA2 | Order invoiced quantity | draft invoice counted; cancelled invoice not counted | Invoice create / cancel | Credit note lowers invoiced quantity | receipts not counted (inference) | VDR-TXA2-C286, VDR-TXA2-C042 |
| TXA2 | Expense receipt | create and post | Expense approval | Cancel/reversal clears the expense link | none specific | VDR-TXA2-C305, VDR-TXA2-C306, VDR-TXA2-C160 |
| TXA2 | Tax tags on existing items | rewritten | Optional re-tag tool | None (irreversible) | only multi-parent child taxes block; no lock check | VDR-TXA2-C231, VDR-TXA2-C232, VDR-TXA2-C234 |
| TXA2 | Payment-time withholding (optional) | registered on payment | Payment register | Payment cancel/unreconcile (behaviour unknown) | negative-or-zero base; missing number | VDR-TXA2-C225, VDR-TXA2-C226, VDR-TXA2-C227 |

**Rows:** 20 · **Units without this register:** TXA1 · generated 2026-10-02
