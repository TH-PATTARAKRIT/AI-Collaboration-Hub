# P06 → P11 — WRITTEN NOTIFICATION: corrected counts in two P11-bound handoffs

**From:** P06 Bank-to-Reconcile · branch `research/account-p06-bank-to-reconcile-2026-09-04-001`
**To:** P11 Core Reconciliation
**Raised under:** `Q-P06-03` / `XRD-003`, authorised by `PHASE-S/Q-BOSS-01 = APPROVED` (`1bf9b40`)
**Date:** 2026-09-07
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. This is a notification, not an edit

**P06 has not touched P11's package and will not.** The queue makes this notification mandatory and forbids peer-owner mutation. **Nothing here asks P11 to accept anything; it reports what changed in what P06 handed over.**

## 2. What was wrong, in the two handoffs P11 reads

| Handoff | Statement as P11 may have read it | Corrected |
|---|---|---|
| `18_P06_CORE_RECON_HANDOFF_PACK.md`:214 | *"under **three vetoes**, with **65 blockers** and 75 open items"* | **seven vetoes** · **67 blockers** · 75 open items |
| `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md`:108 | *"under **four active vetoes**, with **65 blockers** … **16 recorded author errors**"* | **seven vetoes** · **67 blockers** · **21 author errors** |

Also corrected, outside the handoffs: `13_`:94 (65 → **67**), `13_`:95 (66 → **68**), `46_`:124 (65 → **67**), `40_`:288 (23 → **21**), and `P06-B-58` re-scaled on the corrected author-error figure.

## 3. Each figure with the command that produces it

```
blockers      grep -oh 'P06-B-[0-9]\+' *.md | sort -u | wc -l                        → 67
              contiguous B-01..B-67; two instrument forms, diff-identical sets;
              positive control B-50 → 1, negative control B-68 → 0,
              injection control: inject a synthetic B-68 → 67 becomes 68
open items    grep -oh 'P06-OQ-[0-9]\+' *.md | sort -u | wc -l                       → 68
vetoes        grep -oh 'AASP-VETO-[0-9]\+' *.md G02_*/*.md | sort -u                 → AASP-VETO-01..07 = 7
author errors 23 distinct REV-E-* identifiers, of which 21 carry a definition line.
              REV-E-22 and REV-E-23 are repair-marker families, not author errors.
              UNIT: author error, not identifier.                                     → 21
```

## 4. What this does and does not change for P11

- **It does not change any P06 finding P11 consumes.** Every source-level claim re-executed and held; the corrections are to counts and to veto/author-error totals.
- **`AASP-VETO-07` remains PRESERVED.** Seven vetoes stand, none discharged.
- **`AASP-VETO-06` still binds:** `HO-03`/`HO-04` are **WRITTEN, NOT DELIVERED**. This notice is written; **receipt is P11's to record, not P06's to assume.**
- **P11's pin on P06 is stale** regardless of these counts — P06's head has moved past whatever SHA P11 pinned. **P06 does not re-pin for P11.**

## 5. One further item P11 should see, raised separately

`Q-P06-04` withdrew and restated **`FTB-F-07`**. A returned-item / dishonoured-payment concept and a post-dated-cheque concept **do exist in the v18 distribution**, in `addons_archive` only — a real `Many2one` field in `l10n_nz_eft`, a Korean GL account for dishonoured bills, and a post-dated-cheque feature in `l10n_latam_check`. The prior negative rested on a **published search pattern that could not fire under either grep mode**.

**Consequence for `P06-B-34` / `P06-B-35`: flagged, not disposed.** Their basis is now *"absent from the loadable set"*, not *"absent from the distribution"*. **P06 has not re-adjudicated them and is not asking P11 to.**

## 6. Status

**`Q-P06-03` repair executed; completion gated on `RC-04`**, which P06 may not run — Boss ruling `XRECON/Q-BOSS-01` (`XRD-009`) = **NOT SATISFIED**, and `PHASE-S/Q-BOSS-02` (what party satisfies structural independence) is **raised and unanswered**.

**No response is required from P11 for P06 to proceed, because P06 is not proceeding.**
