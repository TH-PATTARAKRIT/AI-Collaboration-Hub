# [SMEPLUS-26-09-06-SAAS-CELL-001]
# First Image Validation — Thai Sample Frame & Gate Method Blocker

Date checked: 2026-09-07
Jira: ERPPLUS-151
Status: HOLD — VALIDATION SAMPLE FRAME INSUFFICIENT
Boss: Sole Final Approver

## 1. Evidence checked

Round 2A Slack thread:
- Channel: `#smeplus_enterprise_suite`
- Channel ID: `C0BBYGPN6G4`
- Parent message TS: `1788698234.614439`
- Round 2A asks users to match 5 top-level labels to concrete business tasks without icons.

Observed result at latest check:
- Independent human test answers: 0
- Thread replies: 1, and it is only the reminder message posted by the project account.
- Therefore there is no valid human comprehension percentage and no PASS/FAIL result.

## 2. Sample-frame inspection

The Slack channel has 4 non-bot members:
1. `U03FMK38VHN` — Somchart Jabsung / Sjabsung — project/Boss-side identity.
2. `U089WE66G3D` — SCG LEGACY — project operating identity.
3. `U0AAT2K2FS7` — Eric.
4. `U0BBUSNG69K` — Koyin htay.

The current channel therefore does not provide an adequate independent Thai-user respondent pool for the intended Thai First Image comprehension test.

This is a methodological blocker, not a naming failure.

## 3. Gate integrity consequence

No Evidence = No Progress.

The following are prohibited until an adequate independent Thai respondent cohort exists:
- reporting a comprehension percentage;
- declaring any candidate label PASS/FAIL;
- exposing Round 2B icons to the same Text-Only cohort before Round 2A closes;
- freezing menu names;
- using the current channel population as representative of Thai SME users.

## 4. Corrective validation design

A valid next round should recruit independent Thai respondents who were not involved in creating the names and who cover real business roles, preferably including:
- Sales / Customer Service;
- Purchasing / Procurement;
- Warehouse / Inventory;
- Production / Manufacturing;
- Finance / Accounting;
- General management or cross-functional users.

Testing sequence remains:
`TEXT ONLY -> TEXT + ICON -> ICON ONLY RECALL`

For each candidate label measure:
- Unaided Comprehension;
- Navigation Accuracy;
- Ambiguity Rate;
- Recognition Time where practical;
- Visual Recall in the icon round;
- Relearning Cost / explanation dependency.

## 5. Statistical note on the proposed >96% threshold

The previously proposed `>96% = PASS` rule cannot be interpreted responsibly without fixing sample size.

Examples:
- n=20: 19/20 = 95%; only 20/20 exceeds 96%.
- n=25: 24/25 = 96%; only 25/25 exceeds 96%.
- n=30: 29/30 = 96.67%; one miss can still exceed 96%.

Therefore if Boss wants to retain a strict `>96%` empirical gate while allowing one respondent error, a practical minimum is n=30. Smaller samples can still be used for qualitative discovery, but should not be presented as statistically strong evidence for the >96% threshold.

## 6. Current architecture recommendation remains unchanged

Candidate labels under validation only:
- ขาย (Sales)
- จัดซื้อ (Procurement)
- คลังสินค้า (Inventory)
- ผลิต (Manufacturing)
- บัญชีและการเงิน (Finance)

Principle:
`Recognition before Differentiation.`

SMEsPlus differentiation should continue to come from its own visual language, icon family, interaction patterns, Control/Evidence, Knowledge of Truth and governed AI rather than forcing unfamiliar business vocabulary.

## 7. Decision state

- Round 2A: HOLD — no independent Thai human evidence yet.
- Round 2B: privately prepared in Figma; not released to Round 2A participants.
- Naming: NOT FROZEN.
- Icon system: NOT FROZEN.
- Team C / production: NOT AUTHORIZED.
- Final decision remains with Boss.
