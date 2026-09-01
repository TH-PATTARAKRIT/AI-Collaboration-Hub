# COA-G02 — SaaS Invariant Compliance

Date: 2026-09-01
Gate: `COA-G02 — Base COA Kernel Discovery`
Scope: COA-G02 **classification/discovery scope only**. Runtime/provisioning/upgrade/isolation execution proof remains owned by later Gates, especially G04S/G07.
Boss cross-gate ruling: `DOMAIN_01_ACCOUNTING_CORE_AO_BOSS_CROSS_GATE_SAAS_INVARIANTS_RULING.md`
Triggering Independent Audit: `d452ecc8fc826ed9d07b738ff5a5efc9028a633e`
CORR1 authority: `743d9dd4e621540aa36229ab7801b5633c19dc5e`

## SAAS INVARIANT COMPLIANCE — SI-01..SI-10

The Verification Status values below are the substantive results already independently re-performed by the ChatGPT Independent Audit at commit `d452ecc8fc826ed9d07b738ff5a5efc9028a633e`. This CORR1 republishes those results in the Boss-mandated evidence-record structure; Team B is **not** self-approving the corrected record. Fresh targeted Independent Re-audit remains required.

| SI | Requirement | Applicability to G02 | Evidence Location | Owner / Owner Role | Reviewer / Verifier | Verification Status | Conflict / Exception | Gate Impact |
|---|---|---|---|---|---|---|---|---|
| SI-01 | Tenant context is mandatory | Applicable — classification boundary | `COA_G02_BASE_KERNEL_DISCOVERY_REGISTER.md` §6–§7 @ `7bb309d9e1ef5ac0abf73dea1997296236182d49`; Boss AO ruling; Independent Audit §10 @ `d452ecc8...` | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | Runtime tenant-instance proof remains later-Gate evidence | No G02 semantic blocker; runtime proof not credited |
| SI-02 | Company context is mandatory where company-scoped | Applicable where company-specific | `COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md` @ `d23b76226e9467b233e44c2977bcf15f6a39d505`; G02 discovery reductions; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | Company-specific financing/payment instruments remain controlled extensions | No G02 blocker; later company-layer proof remains downstream |
| SI-03 | Standard Template is not tenant-owned mutable data | Applicable | G02 discovery explicit non-claims §7 @ `7bb309d9...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | Runtime template ownership/provisioning remains G04S | No G02 blocker; no runtime claim |
| SI-04 | Tenant customization cannot modify the published Standard Template | Applicable boundary rule | G02 universal-vs-extension treatment in discovery/anchor registers @ `7bb309d9...` / `d23b762...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | Runtime enforcement remains G04S | No G02 blocker; runtime enforcement not credited |
| SI-05 | Account Code / Name is not canonical identity | Directly applicable | `COA_G02_BASE_KERNEL_DISCOVERY_REGISTER.md` §§4,7 @ `7bb309d9...`; `COA_G02_SOURCE_ANCHOR_DISPOSITION_REGISTER.md` @ `d23b762...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | `NONE` | No G02 blocker |
| SI-06 | Published Template Version is immutable | Applicable at G02 classification boundary | G02 discovery explicit non-claims §7 @ `7bb309d9...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | G02 publishes no template version; implementation/version proof remains G04S | No G02 blocker; later proof not credited |
| SI-07 | Upgrade is explicit, previewable and auditable | Applicable at G02 classification boundary | G02 discovery explicit non-claims §7 @ `7bb309d9...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | No upgrade is executed in G02; upgrade workflow proof remains G04S | No G02 blocker; later proof not credited |
| SI-08 | No cross-tenant COA access | Applicable at G02 classification boundary | Controlled source-only evidence boundary in G02 package; Boss AO; Independent Audit §10 @ `d452ecc8...` | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | No runtime tenant access is exercised by G02; isolation proof remains G07/G04S as applicable | No G02 blocker; runtime isolation not credited |
| SI-09 | Company customization must preserve canonical reporting semantics | Applicable boundary rule | Universal-vs-extension decisions in discovery/anchor registers @ `7bb309d9...` / `d23b762...`; Boss AO; Independent Audit §10 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | Detailed reporting taxonomy/multi-company proof remains G05/G07 | No G02 blocker; later proof not credited |
| SI-10 | SaaS Core must not hard-code Thailand-specific source architecture | Directly applicable | G02 business-semantic-only discovery/anchor artifacts @ `7bb309d9...` / `d23b762...`; Boss AO; Independent Audit §§9–11 | Team B — G02 evidence producer | ChatGPT Independent Audit @ `d452ecc8...`; CORR1 structure re-audit pending | `PASS / VERIFIED` | `NONE` — no Odoo ORM/schema/API/vendor technical design adopted | No G02 blocker |

## Interpretation Boundary

`PASS / VERIFIED` above means only that the **G02 classification/discovery result** complies with the named invariant at the authorized G02 scope, as independently re-performed in `d452ecc8...`.

It does **not** mean that runtime tenant isolation, template provisioning, template versioning, upgrade execution, permissions, multi-company execution proof, or G04S/G07 obligations are complete.

## CORR1 Current Status

`G02-AUD-01 = CORRECTED / PENDING INDEPENDENT RE-AUDIT`

`36-CONCEPT CANDIDATE = UNCHANGED / INDEPENDENTLY SUPPORTED BY PRIOR AUDIT`

`COA-G02 = HOLD / CORRECTION REQUIRED — PENDING FRESH TARGETED INDEPENDENT RE-AUDIT`

`READY FOR PMO VERIFICATION = NO`

`COA-G03 = NOT STARTED / NOT AUTHORIZED`

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
