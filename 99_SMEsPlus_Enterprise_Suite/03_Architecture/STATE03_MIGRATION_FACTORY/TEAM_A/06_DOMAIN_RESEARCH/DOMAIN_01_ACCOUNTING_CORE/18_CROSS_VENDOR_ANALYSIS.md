# 18 — CROSS-VENDOR ANALYSIS / INDEPENDENT TRIANGULATION (CORRECTED, CORR-02)

## STATUS CHANGE
```
PRIOR:  EXTERNAL_RESEARCH_ACCESS = UNAVAILABLE   → A6 = HOLD
NOW:    EXTERNAL_RESEARCH_ACCESS = AVAILABLE     → A6 = PARTIALLY CLOSED
```
**A6 is PARTIALLY CLOSED, not VERIFIED CLOSED.** Three of nine targets were triangulated
against independent public sources this round. No standard was invented; no IFRS/TFRS clause
is cited; nothing is cited from memory. Every citation below is a URL actually retrieved.

## TRIANGULATED THIS ROUND

### T-01 — Double-entry / debit = credit → **UNIVERSAL ACCOUNTING PRINCIPLE**
Independent sources confirm every transaction is recorded with equal and opposite entries, that
total debits must equal total credits at all times, and that this underpins the accounting
equation Assets = Liabilities + Equity. Provenance **P1 (accounting standard/principle)**.
- [Double-entry bookkeeping — Wikipedia](https://en.wikipedia.org/wiki/Double-entry_bookkeeping)
- [Accounting equation — Wikipedia](https://en.wikipedia.org/wiki/Accounting_equation)
- [Double Entry Bookkeeping — Wall Street Prep](https://www.wallstreetprep.com/knowledge/double-entry-accounting/)

**Consequence for CF-01:** the *requirement* is universal. The reference system's
implementation of it (application-level, suppressible) is **not** the principle — it is one
vendor's realisation of it, and a weak one.

### T-02 — Correction by reversal, not deletion → **CROSS-ERP COMMON PATTERN, audit-driven**
Independent vendor documentation shows posted journal entries **cannot be deleted** in SAP
Business One — only reversed — explicitly to preserve the audit trail; SAP S/4HANA reverses
rather than deletes posted FI documents; Microsoft Dynamics 365 Business Central documents a
reverse operation for correcting entries. Provenance **P4 (cross-vendor documentation)**.
- [Reverse Journal Entry in SAP Business One](https://www.sap-business-one-tips.com/en/reverse-journal-entry/)
- [How to delete Journal Entry document in SAP Business One — SAP Community](https://community.sap.com/t5/enterprise-resource-planning-q-a/how-to-delele-journal-entry-document-in-sap-business-one/qaq-p/482022)
- [Identifying How to Reverse Journal Entries — SAP Learning](https://learning.sap.com/learning-journeys/outlining-the-record-to-report-process-in-sap-s-4hana/identifying-how-to-reverse-journal-entries_c7c33143-d978-4dcf-9e36-d598531a44c6)
- [Correct journal entries — Microsoft Learn](https://learn.microsoft.com/en-gb/training/modules/create-process-journal-entries-dynamics-365-business-central/4-reverse)

**Consequence for CF-06 — a genuine divergence.** SAP Business One *prevents* deleting or
editing a posted entry. The reference system's `button_draft` *permits* a posted entry to
return to an editable state. This is therefore **vendor-specific behaviour that diverges from
peer ERP practice**, not an industry norm. That materially strengthens ADV-04.

### T-03 — Period control → **CROSS-ERP COMMON PATTERN; peer designs are simpler**
NetSuite documents accounting periods with three states — Unlocked, Locked (only users holding
an override permission may post), and **Closed (no user, including administrators, can post or
make G/L-impacting changes)** — plus an audit trail of changes in closed periods.
Provenance **P4**.
- [Locking and Unlocking Accounting Periods — Oracle NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1451780.html)
- [Accounting Period Management — Oracle NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/chapter_N1445226.html)
- [Accounting Period Close — Oracle NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1452509.html)

**Consequence for CF-03.** Period control is universal; the reference system's *shape* is not.
NetSuite expresses it as one period object with three states plus one override permission.
The reference system uses six lock-date fields, per-user computed variants, a lock-exception
object, and a `BYPASS_LOCK_CHECK` context escape. Independent evidence therefore supports
ADV-03 as a real improvement objective rather than an opinion.

## NOT TRIANGULATED THIS ROUND — REMAIN OPEN
| Target | Status |
|---|---|
| Journal / ledger concept | NOT TRIANGULATED |
| Posting concept | NOT TRIANGULATED |
| Audit trail (as a statutory obligation) | NOT TRIANGULATED |
| Multi-currency accounting principle | NOT TRIANGULATED |
| Document immutability as a **legal** requirement (esp. Thailand) | NOT TRIANGULATED — needs statutory source |
| Gapless numbering as a **legal** requirement (esp. Thailand) | NOT TRIANGULATED — needs statutory source |

**No IFRS/TFRS/Thai Revenue Department clause is cited anywhere in this pack.** Where such
authority would be needed, the gap is recorded (GAP-D01-07, GAP-D01-08) rather than filled.

## CLASSIFICATION AFTER TRIANGULATION
| ID | Finding | Classification | Provenance |
|---|---|---|---|
| CV-01 | Debit = credit | **A — Universal principle** | P1 (triangulated) |
| CV-02 | Correction by reversal, not deletion | **D — Cross-ERP common pattern** | P4 (triangulated) |
| CV-03 | Period close prevents posting | **D — Cross-ERP common pattern** | P4 (triangulated) |
| CV-04 | Posted entry may return to editable (reset-to-draft) | **E — Vendor-specific, diverges from peers** | P4 + P7 |
| CV-05 | Six lock fields + per-user variants + bypass context | **E — Vendor-specific** | P7 |
| CV-06 | Opt-in per-journal hash chaining | **E — Vendor-specific** | P7 |
| CV-07 | One table for all document types via `move_type` | **E — Vendor-specific** | P7 |
| CV-08 | Balance enforced in application only, suppressible | **E — Vendor-specific implementation of a universal principle** | P7 |
| CV-09 | Exact-decimal money | **D — Cross-ERP common pattern** (not triangulated this round) | P7 |
| CV-10 | Thai statutory obligations | **G — Unknown** | — |
