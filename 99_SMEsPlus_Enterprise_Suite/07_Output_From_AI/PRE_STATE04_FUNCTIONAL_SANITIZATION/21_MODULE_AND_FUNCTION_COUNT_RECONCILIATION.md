# PRE-STATE 04 — Module and Function Count Reconciliation

**Document ID:** PRE-STATE04-B0-21
**Version:** v0.4 (Boss decisions applied — Prompt STEP040101, Session [SMEPLUS-26-07-15-005])
**Status:** READY FOR INDEPENDENT REVIEW
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

## 4. Thailand-Scope Functional Learning Candidate Calculation — BOSS-APPROVED (STEP040101)

Boss decision STEP040101 (2026-07-15) adopts the following calculation:

```
  1,436   Controlled Learning Baseline
−   521   Foreign Localization modules unrelated to Thailand
−    99   Theme/Test/Demo/Noise modules
−     8   non-Thai country-specific modules without the l10n_ prefix
=   808   THAILAND-SCOPE FUNCTIONAL LEARNING CANDIDATES
```

The 808 candidates comprise:

- **806 General and Business Module Candidates**
- **2 Thailand Localization Baseline Candidates** (`l10n_th`, `l10n_th_reports`)

**Classification: THAILAND-SCOPE FUNCTIONAL LEARNING CANDIDATES.** 808 is NOT
final SMEsPlus modules, approved modules, the final Function Catalog count,
final Functional Requirements, build scope or release scope. One module may
contain multiple functions, and multiple modules may represent overlapping or
consolidated business functions. The final module and function count is
determined through later normalization, business grouping, function discovery
and Fit–Gap–Decision activities.

### Derivation trail (transparency — figures preserved)

```
Remaining Pool (incl. Thai priority) = 1,436 − 521 (foreign l10n) − 99 (noise) = 816
Remaining Pool (excl. Thai priority) = 816 − 2 (l10n_th*)                     = 814
Thailand-scope candidates            = 816 − 8 (non-prefixed country-specific) = 808 (= 806 + 2 Thai)
```

**Prior 815 figure:** 1,436 − 521 − 100 = 815 used the preliminary noise count
100; the reproduced noise count is 99 (Section 3, variance −1, GAP-005), giving
816 before the 8-module exclusion. The Boss-approved calculation uses the
reproduced 99.

**The 8 non-`l10n_`-prefixed country-specific modules** (Boss-approved
exclusion from the Thailand-scope candidate count):

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
816 − 8 = 808   (806 General/Business + 2 Thailand Localization baseline)
```

Per Boss decision STEP040101, these 8 modules are excluded from the
Thailand-scope candidate count. They remain recorded in
`03_SOURCE_MODULE_RECONCILIATION.csv`; their formal movement into the foreign
exclusion registers (accounting-localization vs non-accounting) is still Batch 2
work. The candidate count was derived by evidence, not forced.

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
| Non-Thai country-specific excluded (no `l10n_` prefix) | 8 | Boss-approved exclusion (STEP040101); Batch 2 registers formalization |
| Thailand-scope Functional Learning candidates | **808** (806 General/Business + 2 Thailand Localization baseline) | Boss-approved (STEP040101): 1,436 − 521 − 99 − 8 |
| Controlled Delta references (addons_extra.zip) | 69 | AUTHORIZED CONTROLLED DELTA LEARNING REFERENCE; OUTSIDE Active Baseline; GAP-004 |
| Calculated combined learning references | 1,505 | 1,436 + 69 — calculated only; NOT combined with 808 until Controlled Delta Intake approved |
| Consolidated Business Function count | not yet counted | Batches 1–13 output |
| Technical Dependency count | not yet counted | Batches 1–13 output (83 Hidden-category modules in pool are the primary candidates) |
| Duplicate count | not yet counted | Batches 1–13 output |
| Evidence-Gap register entries | 6 | `17_EVIDENCE_GAP_REGISTER.csv` |
| Legal holds | 0 | no contamination event in Batch 0 |

Primary Business Group totals will be reconciled against the accepted source
total when group assignment begins (Batch 1 onward). Baseline modules have not
been assigned to Business Groups; the 69 parked extras carry a preliminary
mapping in `03A` (secondary evidence only — it does not alter primary totals).

---

## 7. addons_extra Reconciliation — Controlled Delta Learning References

Boss decision STEP040101 (2026-07-15): the 69 modules in `addons_extra.zip` are
**AUTHORIZED CONTROLLED DELTA LEARNING REFERENCE** for Clean Room Functional
Learning. Lifecycle: **AUTHORIZED-FOR-CLEAN-ROOM-FUNCTIONAL-LEARNING /
CONTROLLED-DELTA-INTAKE-PENDING**. Controlled position: mapped and reconciled,
but **OUTSIDE the 1,436-module Active Baseline** and **NOT YET APPROVED FOR
STATE 04 intake**. Third-party modules among them are lawfully acquired
third-party reference evidence (GAP-007 resolved for Functional Learning);
copyright/license conditions remain applicable and third-party source code is
not classified as SMEsPlus-owned source code. They are not combined with the
808 Thailand-scope candidates during this execution.

### 7.1 Duplicate Reconciliation

| Control | Method | Result |
|---|---|---|
| Exact name duplicates vs 1,436 baseline | set intersection of module names | **0** |
| Manifest metadata extraction | 69/69 parsed (metadata fields only) | 0 errors |
| Functional overlap candidates | curated cross-check vs baseline | **13 flagged REVIEW-REQUIRED** (e.g. `dev_print_cheque`↔`account_check_printing`; `purchase_request`↔`purchase_requisition`; `multi_level_approval*`↔`approvals`; full list in 03A). Overlaps do not reduce module counts. |

### 7.2 Calculated Figure (NOT a baseline change)

```
  1,436  Controlled Learning Baseline (ACTIVE — unchanged)
+    69  Controlled Delta Learning References (OUTSIDE Active Baseline)
−     0  Confirmed name-level duplicates
= 1,505  Calculated Total Reference Candidates — a calculated reference figure
         ONLY; takes effect ONLY upon Boss approval of Controlled Delta Intake.
         NOT the Active Baseline, approved STATE04 intake, final SMEsPlus module
         count, implementation scope or production module count.
```

### 7.3 Candidate Pool (active baseline unchanged; parked figures shown for planning)

| Counter | Active (1,436 basis) | If delta intake approved (1,505 basis) |
|---|---|---|
| Foreign localization (`l10n_` non-Thai) | 521 | 521 |
| Theme/Test/Demo/Noise | 99 | 99 |
| Thailand localization priority | 2 | 11 (2 + 9 parked `l10n_th_*` = THAILAND-PRIORITY-PENDING) |
| Remaining pool incl. Thai | 816 | 885 |
| Remaining pool excl. Thai | 814 | 874 |
| General/Business candidates (excl. Thai, −8 non-prefixed country-specific) | 806 | 866 |
| **Thailand-scope Functional Learning candidates (806 + 2 Thai)** | **808** | 868 |

### 7.4 Extra Classification Summary (all AUTHORIZED CONTROLLED DELTA LEARNING REFERENCE)

| Classification | Count |
|---|---|
| THAILAND-PRIORITY-PENDING (`l10n_th_*`) | 9 |
| COMPANY-SMESPLUS-CUSTOM (SMEsPlus-branded) | 13 |
| THAILAND-RELEVANT-COMPANY-EXTRA | 4 |
| COMPANY-EXTRA-CANDIDATE | 43 |
| **Total** | **69** |

**Erratum:** an earlier session report stated "12 `smesplus_*` modules". Exact
counts: 11 with the `smesplus_` prefix + 2 further SMEsPlus-branded modules
(`hide_smesplus_menu`, `monday_smesplus_connector`) = 13. Corrected without
adjusting evidence.

### 7.5 Evidence Flags

- **GAP-007 (RESOLVED FOR FUNCTIONAL LEARNING BY BOSS DECISION):** 43/69 manifests carry third-party author/license metadata (Ecosoft/OCA AGPL-3 incl. the entire Thai withholding-tax family; Domiup OPL-1; Webkul proprietary; Cybrosys; ForgeFlow/OCA; ACSONE/OCA). Boss confirms these were lawfully purchased and authorizes them as **LAWFULLY ACQUIRED THIRD-PARTY REFERENCE EVIDENCE** for Clean Room Functional Learning only. Copyright/license conditions remain applicable; third-party source code is not SMEsPlus-owned source code; purchase evidence is CONFIDENTIAL / RESTRICTED / NOT PUBLICLY ATTACHED. Author/license values preserved verbatim in 03A; no ownership certification by Claude Code.
- **Database evidence:** 13 extras have matching tables in the reference dump (withholding-tax certificate family, `purchase_request*`, `date_range*`, `dev_print_cheque*`, `res_partner_company_type`, others in 03A).

---

## 8. RESTORED CORRECTION [SMEPLUS-26-07-15-003] — GAP-008 Dependency Evidence (PEND-001)

| Control | Evidence |
|---|---|
| Artifact | `account_payment_multi_deduction-20260715T011601Z-1-001.zip`, 41,379 B, modified 2026-07-15 08:16:14+07:00, SHA-256 `a8568e6ba7359d3596ac00ccadc8ab89f14957ffed675285c0bdd454c00746c6` |
| Manifest | "Payment Register with Multiple Deduction", version **18.0.1.0.2** (series 18.0), depends: `account` (in baseline), author Ecosoft/OCA, license AGPL-3, status Alpha |
| Dependency verification | CONFIRMED from both manifests: `l10n_th_withholding_tax_multi` (v19.0.1.0.2) → this module + `l10n_th_withholding_tax` (v19.0.1.4) |
| Version position | Artifact series **18.0** vs dependent series **19.0** — one major series older; API-level compatibility unverified |
| Functional contract (neutral) | Payment registration with multiple deduction lines, each posted to a selectable account, with open/close handling and analytic distribution |
| Database evidence | Dump contains `account_payment_deduction` (payment_id, account_id, name, amount, is_open, analytic_distribution) and `account_payment.is_multi_deduction` — contract MATCH; function active in reference system |
| Classification | **VERSION 18 AUTHORIZED FUNCTIONAL LEARNING REFERENCE** |
| GAP-008 status | **CLOSED AS FUNCTIONAL LEARNING GAP** (Boss decision STEP040101) — the Version 18→19 difference is not a blocker for Functional Learning |
| Future design position | **VERSION 19-COMPATIBLE NEW CLEAN ROOM IMPLEMENTATION REQUIRED** |

**Mandatory position (Boss decision STEP040101):** "Learn the functional
behavior from the lawfully acquired Version 18 reference, independently define
the Business Concept, Business Rules and Functional Requirements, and then
create a new Clean Room SMEsPlus implementation compatible with Version 19."

Mandatory transformation chain: Version 18 Reference Evidence → Business Concept
→ Business Rules → Neutral Functional Requirements → SMEsPlus Design → New
Version 19-Compatible Implementation. The prohibited path (Version 18 Source
Code → modify/port code → Version 19 implementation) must not be used. No
application code is created or modified in this execution.

Restoration note: Sections 7–8 reconstruct the content of lost local commits
`0374857` and `9bd54fc` from recorded session evidence, per Boss authorization
[SMEPLUS-26-07-15-004]; statuses updated to the Boss decisions in Prompt
STEP040101 [SMEPLUS-26-07-15-005]. See `26_CORRECTION_AND_RECOVERY_RECORD.md`.
No source code was copied, ported, translated or modernized. Batch 1 has not
started.
