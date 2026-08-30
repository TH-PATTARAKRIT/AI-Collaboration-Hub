# DOMAIN_01 Accounting Core — Boss COA Decision Summary

Date: 2026-08-30

Boss approved the following controlled baseline:

- Product target: SMEsPlus Local Thailand.
- COA learning scope: Thai chart-of-accounts sources only unless Boss reopens scope.
- Primary COA seed/reference: `Account_Odoo18_19 sent 270369.xlsx`, tab `Odoo18`.
- Account Type: Odoo-like user-facing familiarity; SMEsPlus-owned canonical identifiers and business rules underneath.
- COA architecture: Standard Thai COA Template -> Company/Tenant COA Instance -> Source Mapping Layer.
- Account Code is not canonical identity.
- Express remains usability benchmark only; not the primary COA source.
- Clean-room boundary remains absolute: no Odoo ORM/schema/source-code/technical-ID/module architecture cloning.
- Exact Odoo18 tab content must be extracted and evidence-verified before COA Blueprint Freeze.

Primary ruling evidence: `DOMAIN_01_ACCOUNTING_CORE_AG_BOSS_COA_LOCAL_TH_RULING.md`.

Status: `D01-GATE-A3 = BOSS APPROVED WITH CONTROL`.

Development and Production remain not authorized by this decision.
