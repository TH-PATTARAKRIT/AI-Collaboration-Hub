# U152 — account_followup AR Dunning / Follow-up Chain (L3)

**Unit:** U152  
**Title:** account_followup — AR dunning/follow-up chain L3 depth  
**Status:** ABSENT — module not present in Community edition  
**Research date:** 2026-10-02  
**Researcher:** DeepSeek worker (STATE03 VDR)

---

## Presence Check

```
ls "/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account_followup"
# → No such file or directory (exit code 1)
```

Community addons listing filtered for `account*` confirms: `account_followup` is NOT among the 30 account-prefixed modules present. No `follow*` match exists at all.

---

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U152-C01 | ABSENT-01 | addons/ | directory listing | ABSENT | always | GAP | The directory `account_followup` does not exist under `odoo/addons/` in the Community 19.0.post20260921 source tree | The AR dunning follow-up extension directory is not present in the Community edition source tree |
| U152-C02 | ABSENT-02 | addons/ | grep account* | ABSENT | always | GAP | Filtering Community addons for names beginning with `account` yields 30 modules; none is `account_followup` | No module with the follow-up naming prefix was found among the 30 accounting-related modules in Community |
| U152-C03 | ABSENT-03 | addons/ | grep follow* | ABSENT | always | GAP | Filtering Community addons for any name containing `follow` yields zero results | No dunning or follow-up module of any name exists in the Community addons directory |
| U152-C04 | ABSENT-04 | odoo/addons/ | Enterprise scope | ABSENT | OEEL-1 only | GAP | `account_followup` is an Odoo Enterprise module (OEEL-1 license) providing AR dunning automation; it is outside Community scope | The AR dunning automation capability is exclusively provided by an Enterprise-licensed extension not covered under Community scope |
| U152-C05 | ABSENT-05 | — | follow-up level model | ABSENT | always | GAP | Because the module is absent, the `account.followup.line` model (delay_days, send_email, manual_action) does not exist in Community | The data model for configuring dunning levels, delays, and automated actions has no implementation in Community |
| U152-C06 | ABSENT-06 | — | overdue detection cron | ABSENT | always | GAP | No scheduled action for overdue invoice detection and follow-up level assignment exists in Community | The automated background process that identifies overdue invoices and advances their dunning status does not exist in Community |
| U152-C07 | ABSENT-07 | — | reconciliation integration | ABSENT | always | GAP | Community's `account.move.line` has no `followup_line_id` field; reconciling a payment in Community does not clear any follow-up flag | Invoice payment reconciliation in Community does not interact with any dunning state because the dunning capability is absent |

---

## Summary

`account_followup` is an **Enterprise-only** module. All AR dunning capabilities — follow-up level configuration, automated overdue detection, dunning letter generation, and reconciliation-triggered clearing — are absent from the Odoo 19.0 Community edition. Any migration plan targeting Community must implement dunning logic from scratch or accept the gap.

**Gap severity:** HIGH — standard SME AR collections workflow has no native automation in Community.
