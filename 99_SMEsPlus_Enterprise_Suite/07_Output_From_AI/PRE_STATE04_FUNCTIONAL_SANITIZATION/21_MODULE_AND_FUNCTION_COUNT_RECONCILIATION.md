# PRE-STATE 04 — Module and Function Count Reconciliation

**Document ID:** PRE-STATE04-B0-21
**Version:** v0.1 (Batch 0)
**Status:** READY-FOR-INDEPENDENT-REVIEW
**Owner / Prepared By:** Claude Code — PRE-STATE 04 Functional Learning Analyst
**Evidence Basis:** Module_Inventory.csv (1,436 data rows) cross-verified against zip manifest listings; rule-based classification recorded per module in 03_SOURCE_MODULE_RECONCILIATION.csv
**Clean Room Status:** CLEAN — metadata-level access only; no source content read
**Project:** SMEsPlus Enterprise Suite
**Branch:** SMEsPlus
**Session:** [SMEPLUS-26-07-15-001]
**Last Updated:** 2026-07-15

---

## 1. Authoritative Source Total — REPRODUCED

| Control | Source | Result |
|---|---|---|
| Inventory total | `Evidence_CSV/Module_Inventory.csv` data rows | **1,436** ✔ matches baseline |
| Independent zip verification | `__manifest__.py` count in `01_ACCOUNT.zip` | 62 |
| Independent zip verification | `__manifest__.py` count in `02_OTHER.zip` | 1,374 |
| Zip total | 62 + 1,374 | **1,436** ✔ |
| Name-level cross-check | modules in CSV but not in zips | **0** |
| Name-level cross-check | modules in zips but not in CSV | **0** |
| Per-zip split in CSV | `01 ACCOUNT.zip` = 62, `02 OTHER.zip` = 1,374 | ✔ consistent |

The 1,436 baseline is verified at name level in both directions.
`addons_extra.zip` (69 manifests, zero overlap with the baseline) is **outside**
the 1,436 inventory — see Section 5 and GAP-004.

---

## 2. Foreign Localization Candidates — CONFIRMED AT 521

Rule (transparent and reproducible): module name begins with `l10n_` and does
not begin with `l10n_th`.

| Metric | Value |
|---|---|
| Foreign localization candidates | **521** ✔ matches baseline exactly |
| Thai localization modules in baseline (`l10n_th*`) | 2 (`l10n_th`, `l10n_th_reports`) |
| Top country prefixes | be 29, in 18, br 16, es 14, mx 14, ro 12, fr 11, it 10, us 10, din5008 (DE letter standard) 9, ke 9, pl 9, tr 9 … |

Note: the 521 are candidates for the exclusion register. The split between
accounting localization (register 11) and non-accounting localization
(register 12) is Batch 2 work.

---

## 3. Theme/Test/Demo/Noise Candidates — 99 vs BASELINE 100 (VARIANCE −1)

Rules applied to module names:

| Rule | Count |
|---|---|
| test naming (`test_*`, `*_test`, `*_test_*`) | 66 |
| `theme_*` prefix | 30 |
| contains `demo` | 3 |
| `hw_*` hardware proxy prefix | 0 |
| **Total reproduced** | **99** |

Baseline stated 100. Variance = −1. The evidence was **not** adjusted to force
agreement. The identity of the 100th module in the preliminary baseline is
unknown and is registered as GAP-005 for Batch 13 confirmation.

---

## 4. Remaining Candidate Pool — FORMULA-DRIVEN

```
Remaining Pool (incl. Thai priority) = 1,436 − 521 (foreign l10n) − 99 (noise) = 816
Remaining Pool (excl. Thai priority) = 816 − 2 (l10n_th*)                     = 814
```

### Variance Analysis: 815 versus approximately 806

**815 (prior baseline):** 1,436 − 521 − 100 = 815, which includes the 2 Thai
modules. The reproduced equivalent is 816; the difference of 1 is exactly the
noise-count variance in Section 3.

**~806 (Boss working estimate):** reproducible by evidence. A pattern scan of
the 814-module pool (excl. Thai) found **8 country/region-specific modules
that the `l10n_` prefix rule does not catch**:

| Module | Category | Region specificity |
|---|---|---|
| `account_intrastat` | Accounting/Accounting | EU Intrastat statistical reporting |
| `purchase_intrastat` | Accounting/Accounting | EU Intrastat |
| `sale_intrastat` | Accounting/Accounting | EU Intrastat |
| `stock_intrastat` | Supply Chain/Inventory | EU Intrastat |
| `account_sepa_direct_debit` | Accounting/Accounting | EU SEPA banking |
| `payment_sepa_direct_debit` | Accounting/Accounting | EU SEPA banking |
| `account_qr_code_sepa` | Accounting/Payment | EU SEPA QR (neutral QR-payment concept may be reusable for PromptPay via new design) |
| `pos_blackbox_be` | Sales/Point of Sale | Belgian fiscal POS control |

```
814 − 8 = 806
```

The ~806 estimate is therefore an arithmetically exact hypothesis:
**candidate pool excluding Thai-priority modules and the 8 non-prefixed
country-specific modules.** These 8 remain status REVIEW-REQUIRED in
`03_SOURCE_MODULE_RECONCILIATION.csv`; formal movement into the foreign
exclusion registers requires Batch 2 analysis and Boss decision. The count was
not forced.

---

## 5. Out-of-Baseline Evidence — addons_extra.zip

| Metric | Value |
|---|---|
| Module manifests | 69 |
| Overlap with 1,436 baseline | 0 |
| Thai localization modules (`l10n_th_*`) | 9 — withholding tax family (5), certificate/report forms, Thai partner, Thai amount-to-text, Thai base location |
| SMEsPlus custom modules (`smesplus_*`) | 12 |
| Other (approvals, purchase request, PromptPay invoice, 2C2P payment, reporting tools, integrations) | 48 |

These 69 modules are recorded as `PS04-EXT-0001`–`PS04-EXT-0069` in
`03_SOURCE_MODULE_RECONCILIATION.csv` with status EVIDENCE-GAP. The 9 Thai
modules are directly relevant to BG-02 (Thailand Localization and Tax) and the
Batch 1 Thailand Finance catalog. **Boss decision required** on whether the
inventory baseline is extended (GAP-004).

---

## 6. Count Separation Control (Execution Order §15.7)

| Counter | Batch 0 value | Note |
|---|---|---|
| Source module rows (baseline) | 1,436 | verified |
| Foreign localization candidates | 521 | rule-reproduced |
| Theme/Test/Demo/Noise candidates | 99 | rule-reproduced; −1 vs baseline |
| Thailand priority modules | 2 (+9 out-of-baseline) | `l10n_th*` |
| Non-prefixed country-specific (REVIEW-REQUIRED) | 8 | Batch 2 scope |
| Remaining candidate pool | 816 incl. Thai / 814 excl. Thai / 806 if the 8 are excluded | formula-driven |
| Out-of-baseline modules (addons_extra.zip) | 69 | GAP-004 |
| Consolidated Business Function count | not yet counted | Batches 1–13 output |
| Technical Dependency count | not yet counted | Batches 1–13 output (83 Hidden-category modules in pool are the primary candidates) |
| Duplicate count | not yet counted | Batches 1–13 output |
| Evidence-Gap register entries | 6 | `17_EVIDENCE_GAP_REGISTER.csv` |
| Legal holds | 0 | no contamination event in Batch 0 |

Primary Business Group totals will be reconciled against the accepted source
total when group assignment begins (Batch 1 onward). No module has been
assigned to a Business Group yet; therefore no group total can conflict with
the source total at this checkpoint.
