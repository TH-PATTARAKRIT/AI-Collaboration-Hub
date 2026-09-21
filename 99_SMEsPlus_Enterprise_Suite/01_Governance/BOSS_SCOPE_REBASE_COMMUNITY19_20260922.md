# SMEsPlus Community19 — Boss Scope Rebase 2026-09-22

**Authority:** Boss  
**Status:** BOSS APPROVED — ACTIVE WORKING SCOPE

## Active runtime/study split

- RUNTIME INSTALLED: **299** — unchanged
- Installed-set hash: `706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89` — unchanged
- DEFERRED: **52**
- CURRENT STUDY: **247**

`299 = 247 CURRENT STUDY + 52 DEFERRED`

## Deferred routing

The proposed WEBSITE / THEME / COSMETIC routing pool was 53 modules.

- `html_builder` remains in CURRENT STUDY.
- Effective deferred set is therefore **52**, not 53.
- Website reference study is deferred to Next Phase together with eCommerce.
- Other retained current-study exceptions such as `google_recaptcha` remain in the 247 current-study set according to the reconciled mapping.

## Scope bookkeeping

The historical V1.00 CURRENT-PHASE baseline of 300 is preserved for audit history.

Because `cloud_storage_google` remains a `BLOCKED-TECHNICAL` scope row but is not installed:
- Governed CURRENT-PHASE scope = **248**
- Studyable current runtime set = **247**
- BLOCKED-TECHNICAL = **1**
- Master-register NEXT-PHASE = **160**
- SOURCE-EXCLUDED / EVIDENCE-ONLY = **284**

Master reconciliation:
`248 + 160 + 284 = 692`

Runtime reconciliation:
`247 + 52 = 299`

Module counts are planning/control counts and are not the Canonical Function-ID denominator. No Formal Coverage is authorized from these counts.
