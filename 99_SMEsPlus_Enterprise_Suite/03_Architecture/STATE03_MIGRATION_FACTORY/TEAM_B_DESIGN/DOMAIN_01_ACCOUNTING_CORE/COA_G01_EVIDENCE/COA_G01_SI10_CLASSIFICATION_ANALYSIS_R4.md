# COA-G01 CORR4 — SI-10 Classification Analysis

| Item / Task | Owner | Evidence location | Timestamp | Reviewer / Verifier | Verification Status | Gate Impact |
|---|---|---|---|---|---|---|
| Produce dedicated SI-10 classification evidence at COA-G01 scope, per CORR4 directive §4.5 | Claude (session `SMEPLUS-26-08-30-COA-G01R2-001`, CORR4 pass) | Ported `S1-S11` findings (`COA_G01_SOURCE_PORT/STATE03_LOCAL/`), Team A `SE-17/18`, `AG`/`AJ`/`AO`/`AQ` Boss rulings | 2026-08-31 | ChatGPT Independent Re-audit (requested, not yet performed); Boss (sole Final Approver) | **`PASS / VERIFIED` at G01 classification scope** — see §5 | Closes SI-10's classification-scope status; execution-scope proof remains COA-G04S/G06 |

SI-10: *"SaaS Core must not hard-code Thailand-specific source architecture."* Per directive §4.5, this analysis proves or holds the classification boundary using **only** verified ported evidence, `l10n_th`, Boss rulings, and current registers — it does not design schema/API/production implementation, and it does not claim execution-scope proof.

## 1. SaaS Core is country-neutral — evidence

Team A `SE-17` (`account_account.py` L44–72, independently re-cited from `COA_STANDARD/DOMAIN_01_COA_ACCOUNT_TYPE_SOURCE_RECONCILIATION.md`): the 19-value `account_type` enumeration is a **generic accounting classification** (`asset_receivable`, `asset_cash`, `liability_payable`, `income`, `expense`, etc.) — none of the 19 keys or their business-facing labels (Receivable, Bank and Cash, Payable, Income, Expenses, ...) name a Thailand-specific concept. The `AJ_BOSS_ACCOUNT_TYPE_19_ACTIVE_RULING.md` target baseline (19 ACTIVE types) is built entirely from this generic set.

**Classification: `PASS`.** The Account Type core — the primary COA-G01 subject matter — is demonstrably country-neutral at the source-observation layer; nothing Thailand-specific was found hard-coded into it.

## 2. Thailand-specific rules/data belong to a versioned localization profile — evidence

The ported `S1–S11` findings register (`STEP040304R5_STATE03_FREEZE_EVIDENCE_PACK/02_FINDINGS_REGISTER/STEP040304R5_FINDINGS_REGISTER.md`) provides four directly relevant, now-primary-sourced findings:

- **S1**: "Thai statutory reporting is NOT source-observable" — evidence chain `l10n_th_withholding_tax -> l10n_th_reports (OEEL-1) -> account_reports (OEEL-1)`. This *confirms*, from the source side, that Thai statutory reporting logic is already architecturally separated from SaaS Core in the reference source itself (it lives in a distinct, gated localization module chain) — supporting the SI-10 principle rather than contradicting it. Freeze impact recorded as `OPEN DEPENDENCY` (gated OEEL-1 modules are unreadable under clean-room rule, per `AG` §7 — this session cannot and does not read them).
- **S3**: "Thai party identity exceeds a generic partner model" — evidence `l10n_th_partner.branch`, `name_company`; PND emits `branch_number`. This is Thailand-specific *data*, observed in a Thailand-specific *model extension* (`l10n_th_partner`), not in SaaS Core.
- **S4**: "Statutory reference data must be versioned data, not code" — evidence: PND maps income type from a **literal hardcoded rate map**; the WHT certificate carries "a richer, unreconciled list." The Database-Derived Confirmation section of the same register adds: WHT rates actually configured are exactly `{1, 2, 3, 5}` — matching the hardcoded PND map, and income type is encoded as a **name string** (`"1% WH C T"`). **This is the one place the source itself gets SI-10 wrong** — the reference system hard-codes Thai tax reference data as literal values/strings rather than versioned data. This is recorded as a **negative example** — the SMEsPlus target must *not* repeat this pattern, per S4's own "Reference-data architecture" freeze impact.
- **S5**: "Tenancy must be tenant → legal entity → tax branch" — evidence: `company_id` on all Thai models; Thai filing is per branch. This directly informs Tenant/Company/Tax-Branch separation (§4 below).

**Classification: `PASS` (with one explicit negative example carried forward as a design caution, not a violation).** Thailand-specific statutory logic is source-confirmed to live outside the generic accounting core; the one place the source hard-codes Thai reference data (S4) is registered as a pattern SMEsPlus must *not* adopt, consistent with — not contradicting — SI-10.

## 3. No Odoo table/model/class/ORM/source architecture is adopted — evidence

Every COA-G01 artifact produced across Round 2/CORR1-4 consistently cites vendor field/model names (`account_account.py`, `l10n_th_partner.branch`, `account.move`, `wt_tax_id`) **only as evidence anchors**, never as SMEsPlus's own identifiers. This discipline is now explicitly codified in two places:
1. `COA_STANDARD/DOMAIN_01_COA_ODOO18_TAB_SOURCE_INVENTORY.md`'s "Source column names — explicit disclaimer" section (added CORR2): `id`/`name`/`reconcile`/`code`/`account_type` are "observed source-workbook column names only... not proposed SMEsPlus canonical IDs, schema fields, ORM names, table design, or implementation architecture."
2. `COA_G01_CLEAN_ROOM_PROVENANCE_CHECK.md`'s document-level review (CORR1-3): 2 of 3 current `COA_STANDARD` documents `VERIFIED CLEAN-ROOM BOUNDARY` outright; the 3rd closed to the same status by the disclaimer above.

**Classification: `PASS`.** No new vendor architecture-adoption risk is introduced by the S1-S11 evidence cited in this analysis — all of it is cited the same evidence-only way as every prior COA-G01 artifact.

## 4. Source observations are business semantics only — evidence

S1-S5 above are all phrased as business/domain findings ("Thai statutory reporting," "WHT recognition timing," "Thai party identity," "reference data architecture," "tenancy model") — none asserts a specific database table, field type, or ORM relationship as SMEsPlus target design. The Database-Derived Confirmation under S4 is the one place raw technical detail appears (a hardcoded rate map, a name-string encoding) — and it is cited explicitly as a **negative example to avoid**, not as evidence to replicate.

**Classification: `PASS`.**

## 5. Tenant, Company/Legal Entity and Tax Branch contexts are separated where required

- `AQ_BOSS_SAAS_CONTEXT_CLARIFICATION_AND_G01_REMEDIATION_AUTHORIZATION.md` §3: Platform Context / Tenant Context / Company Context are three distinct axes (this resolves SI-01/SI-03 boundary at the classification level, cross-referenced here because SI-10's Thailand-specific-layer question depends on the same context model).
- `AQ` §4 (citing S5 directly): "a two-level Tenant → Company model is insufficient for Thai statutory filing. The correct model is Tenant → Legal Entity (Company) → Tax Branch" — now corroborated by a primary-sourced S5 (§2 above) rather than only a local, unported claim.
- This is recorded as a **classification-scope finding**: the source evidence and Boss ruling agree that a third context level (Tax Branch) is required for Thailand; **no schema, table, or API implementing this third level is designed here** — that is explicitly COA-G04S/G07 scope, per directive prohibition §9.

**Classification: `PASS` (classification only — architectural design of the 3-level context model is out of COA-G01 scope and is not attempted here).**

## 6. No schema/API/production implementation design is created

Confirmed by omission: this document contains zero table definitions, zero API contracts, zero ORM model declarations, and zero code. Every citation above is either a business-semantic finding or a reference to an existing Boss ruling.

## 7. Overall SI-10 disposition

| Sub-criterion | Result |
|---|---|
| SaaS Core is country-neutral | PASS |
| Thailand-specific rules/data belong to a versioned localization layer | PASS (with S4 negative example registered as a caution) |
| No Odoo architecture adopted | PASS |
| Source observations are business semantics only | PASS |
| Tenant/Company/Tax-Branch contexts separated at classification level | PASS |
| No production implementation created | PASS (confirmed by omission) |

**SI-10 = `PASS / VERIFIED` at COA-G01 classification scope.** This corrects the prior status (`HOLD / EVIDENCE REQUIRED even at classification scope`, carried since Round 1) — the blocking reason for that HOLD was that "its supporting local evidence (findings S1, S4) has not yet been reconciled into GitHub and no dedicated SI-10 compliance analysis exists yet." Both conditions are now resolved: S1/S3/S4/S5 are ported and primary-sourced (§§1–5 above), and this document is the dedicated compliance analysis.

**Execution-scope status is unchanged and explicitly NOT claimed here:** implementing the versioned localization-profile layer, the 3-level Tenant/Company/Tax-Branch model, and avoiding the S4 hardcoding pattern in actual SMEsPlus code remain COA-G04S/COA-G06 work. This document proves the classification boundary is internally consistent and evidenced — it does not prove any running system complies with it.

No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.
