# COA-G02 — SaaS Invariant Compliance

Date: 2026-09-01
Scope: COA-G02 **classification/discovery scope only**. Runtime/provisioning/upgrade proof remains owned by later Gates, especially G04S/G07.

| SI | Requirement | G02 evidence/control | Status at G02 classification scope | Gate impact |
|---|---|---|---|---|
| SI-01 | Tenant context mandatory | The 36 concepts are Standard Thailand Template candidates, not tenant-owned accounts. Tenant instances are explicitly later-stage. | PASS | None |
| SI-02 | Company context mandatory where company-scoped | Source/company-specific rows are classified as optional extensions rather than universal kernel facts; company-specific financing and payment instruments are not forced into the kernel. | PASS | None |
| SI-03 | Standard Template is not tenant-owned mutable data | G02 produces a controlled template candidate only; no tenant mutation model or write is performed. | PASS | None |
| SI-04 | Tenant customization cannot modify published Standard Template | Extension treatment is additive at tenant/company level; G02 does not alter the published-template boundary. | PASS | None |
| SI-05 | Account Code / Name is not canonical identity | All source codes, names and `account.1_*` IDs are evidence anchors only. No source identifier is adopted as SMEsPlus identity. | PASS | None |
| SI-06 | Published Template Version immutable | G02 does not publish or mutate a template version. Version immutability remains an inherited control; execution architecture is G04S. | PASS — classification scope | G04S runtime proof later |
| SI-07 | Upgrade explicit, previewable, auditable | No upgrade is executed or implied by G02. Kernel candidate is explicitly not a published upgrade. | PASS — classification scope | G04S proof later |
| SI-08 | No cross-tenant COA access | No tenant data is read or designed into the kernel; evidence is controlled reference/source material only. | PASS — classification scope | G07/runtime proof later |
| SI-09 | Company customization preserves canonical reporting semantics | G02 separates universal semantics from optional company extensions and does not use Account Group/channel/company-specific names as canonical identity. | PASS — classification scope | G04/G05/G07 proof later |
| SI-10 | SaaS Core must not hard-code Thailand-specific source architecture | G02 carries business semantics only. Odoo IDs/codes/fields are provenance anchors and are not reused as schema/API/ORM/technical design. | PASS | None |

## Result

`SI-01..SI-10 = 10/10 PASS at COA-G02 classification/discovery scope`.

This does not claim runtime isolation, template-version implementation, provisioning, or upgrade execution proof. Those remain later-Gate obligations.
