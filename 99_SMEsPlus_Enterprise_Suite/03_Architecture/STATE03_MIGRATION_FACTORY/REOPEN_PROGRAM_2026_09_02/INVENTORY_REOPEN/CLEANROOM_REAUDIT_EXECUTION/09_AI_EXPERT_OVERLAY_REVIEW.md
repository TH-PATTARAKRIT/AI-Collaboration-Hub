# 09 — AI Expert Overlay Review (4 Roles)

Per governing prompt §6: functional design risk, database identity risk, integration/localization risk, code/UI architecture leakage risk. Applied against this session's own findings and the reviewed packages. **Disclosed limitation:** same single-executor pass as `07`/`08`.

## 1. Functional Design Risk

The clean-room remediation of CORR-007B files `08`/`09` removed implementation-level text but did not — and was never intended to — resolve the underlying functional-design gap: `N-A12-01` remains `HIGH FUNCTIONAL DESIGN GAP — REOPENED` (`17` §6, independently confirmed still true by this session's read of the current file content — the business-outcome description is present, but no closing disposition is asserted). **Risk:** a future reader could mistake "clean-room remediated" for "functional-design closed." This session's own `02_CORR007B_C05_CLEAN_ROOM_REAUDIT.md` and `06_DOWNSTREAM_RELIANCE_CLASSIFICATION_MATRIX.md` both state this distinction explicitly to pre-empt that conflation. **Verdict: risk named and mitigated by explicit statement, not by the underlying gap being closed (it is not this session's mandate to close it).**

## 2. Database Identity Risk

Checked whether any SMEsPlus schema, table, or field identity has been proposed anywhere in the reviewed packages. None found — the menu package consistently frames data structure in business terms (e.g. "on-hand / reserved / available" quantities in `17` row TH-10) rather than as field names, and the remediated CORR-007B files (per `02` §2.2) contain zero ORM/field-declaration syntax. The one identity-adjacent risk is the warehouse/location *structure* carry-over (`03` §5), which is a naming/structure risk, not a schema/field risk — captured separately and not double-counted here. **Verdict: no database identity risk found beyond the already-flagged structural item.**

## 3. Integration / Localization Risk

Thai localization content (`17`) is consistently `UNVALIDATED`, and cross-domain handoffs (`04` of the menu package) correctly attribute ownership across Inventory/Accounting/Joint rather than asserting a single-owner design. One integration-adjacent item carried from the reopen and re-confirmed here: `U-03` (Inventory-side SaaS tenancy/isolation architecture) remains a genuine unknown with no document anywhere resolving it — this session found no new evidence either way and does not close it. **Verdict: no new integration risk introduced by this session's findings; `U-03` carried forward unchanged.**

## 4. Code / UI Architecture Leakage Risk

This is the dimension most directly tested by `02` and `03` of this package. Two findings apply here directly:

- The pre-remediation git history of CORR-007B files `08`/`09` is the clearest instance of code-architecture leakage risk identified anywhere in this re-audit — real, confirmed, verbatim Odoo Python source, currently unrestricted (`02` §2.3).
- The warehouse/location notation in menu file `10` is a UI/structure-architecture leakage risk of a different kind — not literal code, but a specific benchmark screen/tree structure carried forward as if pre-validated (`03` §5).

No other UI-layout or screen-architecture leakage was found in the sampled content; the menu package's screenshot evidence register (`05`) is explicitly framed as provenance evidence, not as an approved SMEsPlus screen design, and states this itself ("No label below is an approved SMEsPlus name" — read directly by this session in `03` §2). **Verdict: two named risks, both already carried into `06` and `10`; no unnamed risk found in this dimension.**

## Summary

| Role | Verdict |
|---|---|
| Functional Design | Risk named, mitigated by explicit non-conflation statement |
| Database Identity | No risk beyond the already-flagged structural item |
| Integration/Localization | No new risk; `U-03` carried forward |
| Code/UI Architecture Leakage | Two risks, both already actioned in `06`/`10` |

No overlay role found grounds for `FAIL / FROZEN`. All findings converge with, rather than contradict, `05_SEMANTIC_CONTAMINATION_CHALLENGE_REGISTER.md` and `06_DOWNSTREAM_RELIANCE_CLASSIFICATION_MATRIX.md`.
