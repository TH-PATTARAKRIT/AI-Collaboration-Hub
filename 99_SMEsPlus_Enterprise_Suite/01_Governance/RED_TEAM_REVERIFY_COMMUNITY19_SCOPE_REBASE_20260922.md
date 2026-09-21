# RED TEAM Re-Verification Handoff — Community19 Scope Rebase

**Date:** 2026-09-22  
**Authority:** Boss  
**Status:** READY FOR RED TEAM RE-VERIFICATION  
**Parent:** SMEPLUS-26-09-22-019 / Study Model V2

## Boss-approved active numbers

- Runtime installed: **299** — unchanged
- Installed-set hash: `706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89` — unchanged
- Deferred runtime set: **52**
- Current study runtime set: **247**
- Runtime reconciliation: `247 + 52 = 299`

## Scope bookkeeping

The historical 300-module current-phase baseline remains preserved for audit lineage.

- Governed CURRENT-PHASE scope: **248**
  - Studyable current runtime: **247**
  - BLOCKED-TECHNICAL: **1** = `cloud_storage_google`
- NEXT-PHASE master-register count: **160**
- SOURCE-EXCLUDED / EVIDENCE-ONLY: **284**
- Community source population: **692**
- Master reconciliation: `248 + 160 + 284 = 692`

## Routing correction

The WEBSITE / THEME / COSMETIC routing pool contained 53 proposed rows.

- `html_builder` is explicitly retained in CURRENT STUDY.
- Effective deferred set = **52**, not 53.
- Website reference study moves to Next Phase together with eCommerce.
- Retained current-study exceptions from the reconciled mapping, including `google_recaptcha`, remain in the 247 study set.

## RED TEAM verification required

RED TEAM must independently verify before continuing:

1. Rebuild the exact 52-row deferred membership from `GROUP_STRUCTURE_V2_CORE.tsv`.
2. Confirm `html_builder` is not in the deferred 52.
3. Confirm the 247 current-study rows are unique and are all within the verified 299 installed set.
4. Confirm `cloud_storage_google` remains a separate `BLOCKED-TECHNICAL` governed scope row and is not silently removed.
5. Confirm runtime installed count remains 299 and installed-set hash remains `706e6df4...`.
6. Confirm master reconciliation: `248 + 160 + 284 = 692`.
7. Confirm runtime reconciliation: `247 + 52 = 299`.
8. Confirm zero Enterprise / non-LGPL contamination in the Community register.
9. Publish the exact 52 deferred technical names and 247 current-study technical names as controlled evidence.
10. Return one disposition: `CERTIFIED` / `CONDITIONAL` / `REJECTED`.

## Governance

This rebase is a module-level research planning scope change only.

- **247 is NOT a Canonical Function-ID denominator.**
- No Formal Coverage is authorized from module counts.
- No historical evidence is erased.
- Boss remains sole Final Approver.
