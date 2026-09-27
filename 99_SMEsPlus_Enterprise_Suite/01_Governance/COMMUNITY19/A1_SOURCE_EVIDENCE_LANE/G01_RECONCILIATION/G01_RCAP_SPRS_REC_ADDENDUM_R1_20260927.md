# G01 PLATFORM_BASE — `google_recaptcha` + `base_sparse_field` — RECONCILIATION ADDENDUM R1 (remediation)

## 1. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)** (addendum only; the original REC documents are NOT edited) |
| Parents (superseded in part) | `G01_RECONCILIATION/G01_GOOGLE_RECAPTCHA_REC_20260927.md` sha256 `fc976cb455216cc44d053416c151b37cbc441239f003ce986a7d1bcd74b0afbf`; `G01_RECONCILIATION/G01_BASE_SPARSE_FIELD_REC_20260927.md` sha256 `b8a7da6eab7448e17ce13b587213bd43d1b2e8800b1f00b796d0c37e1b8b11f3` (both equal A3 intake) |
| Addendum inputs | A1 ADDENDUM R1 `G01_A1_PACKAGES/G01_GOOGLE_RECAPTCHA_A1_ADDENDUM_R1_20260927.md` sha256 `6926e67b3c97d2c5dbb5fead4dcb75c63a0e25064ef1f86dc3531f06d8381c53`; A2 ADDENDUM R1 `G01_A2_REVIEWS/G01_RCAP_SPRS_A2_ADDENDUM_R1_20260927.md` sha256 `86260c80f355d611b95da177b89be32195cbbde7fcd6f8ea983575ca1455a896` |
| A3 reports | `G01_A3_CHALLENGES/G01_GOOGLE_RECAPTCHA_A3_STATIC_20260927.md` sha256 `ff91606234f5b276cc659538b0fa852ac119308c70dbead5c9479de48c63273b`; `G01_A3_CHALLENGES/G01_BASE_SPARSE_FIELD_A3_STATIC_20260927.md` sha256 `2ec7cb8a285e02fe61f2bca1de24fdb52d39ebe6964d0655107be967c5f981cb` |
| Frozen banks (lineage lens) | rcap `471e0323450c71223ac795ee859f004d1f5f8e0c8baac04a398b51f7c3bd7724`; sparse `2e0e158431d3b32522092d3770f7028acd5d6c6c2616466f45468c5f977895c8` (re-hashed: equal to `FREEZE_W1-B04.json` entries) |
| Challenge IDs addressed | A3-RCAP-D3 (HIGH), A3-RCAP-D6 (minor), A3-SPRS-D1 (minor), A3-SPRS-D2 (REC-side reflection of the A2 correction) |
| Lane B | None exists (unchanged; column never FAIL for absence) |
| Date | 2026-09-27 |
| Status | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

> **MASTER consumption rule:** MASTER must consume the R1 items in this addendum, **not** the original items REC-RCAP-09, REC-RCAP-10, REC-RCAP-11 or the original REC-SPRS-08 wording, nor the original QID "no evidence" lists for Q024/Q035 (sparse) and Q030/Q033 (rcap). Original rows remain in place for lineage only.

Clean room: neutral summaries, pointers only. No QID answered, no percentages, no Formal Coverage. No git operations.

## 2. `google_recaptcha` — reclassified items

| REC ID | Supersedes | A1 position (R1) | A2 verdict (R1) | REC class (R1) | Lane B | Proof link (R1) | MODULE+QID lineage |
|---|---|---|---|---|---|---|---|
| **REC-RCAP-09R1** | REC-RCAP-09 (**WITHDRAWN**: its "never saved → unhandled technical error" conclusion is disproved on source; original A1 C08 is CONTRADICTED-FROM-SOURCE and withdrawn by A1) | C08R1-a: absent parameter → effective threshold 0.0, no error, gate off, screen shows 0.7. C08R1-c: only a non-convertible stored value raises; "nan"/out-of-scale accepted silently | VERIFIED (both) | **UNKNOWN_PENDING_PROOF** (source premise confirmed by PC-RCAP-06R; security effect needs runtime) | NOT_APPLICABLE | PC-RCAP-06R / PC-RCAP-31 (PR-RCAP-02R1). PC-RCAP-19 retained as declared, expected to FAIL when run | rcap+Q008, rcap+Q009, rcap+Q032 |
| **REC-RCAP-10R1** | REC-RCAP-10 (**WITHDRAWN**: "0.0 → outage for real humans") | C08R1-a/b | SF-1R1: 0.0 deletes the parameter → effective 0.0 as chosen, but the screen shows 0.7 (display/enforcement divergence) and any later unrelated save re-persists 0.7 (silent re-arm) | **GAP** (A2 extension: divergence + re-arm) | UNCORROBORATED | PC-RCAP-06R, PC-RCAP-30 / PC-RCAP-31, PC-RCAP-32 (PR-RCAP-02R1, PR-RCAP-13) | rcap+Q009, rcap+Q032 |
| **REC-RCAP-11R1** | REC-RCAP-11 (class MATCH withdrawn; note "a zero threshold cannot persist" withdrawn as misleading) | C09R1: missing score → bot only under a stored positive threshold | C09 PARTIAL (scope); C09R1 VERIFIED | **GAP** (scope correction). Note: with the parameter absent, a success reply with **no score passes as human** | UNCORROBORATED | PC-RCAP-07 (positive-threshold scope only) / PC-RCAP-06R, PC-RCAP-31 | rcap+Q008 |

Dependent items (class unchanged, note added):
- REC-RCAP-18 (C16, no range validation): now also carries C08R1-c — an out-of-scale stored value refuses every success; "nan" disables the gate. Class MATCH unchanged.
- REC-RCAP-29 (OM-6, "threshold is server-side, the client cannot lower it"): still true, but the server-side threshold may itself be silently 0.0 (REC-RCAP-09R1). Class GAP unchanged.
- REC-RCAP-16 (C14): proof link PC-RCAP-27 superseded for consumption by PC-RCAP-27R (split by proxy mode; A3-RCAP-D5). Class unchanged.
- §7 "Carried forward": the line "CON-RCAP-01 … carried as REC-RCAP-09/10" is replaced by "CON-RCAP-01R1 (display/enforcement divergence) carried as REC-RCAP-09R1/10R1".
- CRQ-RCAP-02 → CRQ-RCAP-02R1 (PR-RCAP-02R1); new CRQ-RCAP-08 → PR-RCAP-13.

Revised rcap counts (30 items, for consumption): MATCH 9 (01, 03, 04, 13, 18, 19, 20, 21, 22); GAP 12 (02, 07, 10R1, 11R1, 23, 24, 25, 26, 27, 28, 29, 30); CONTRADICTION 1 (05); UNKNOWN_PENDING_PROOF 8 (06, 08, 09R1, 12, 14, 15, 16, 17). Lane B: 11 UNCORROBORATED, 19 NOT_APPLICABLE, 0 FAIL (unchanged).

### rcap QID lineage update (A3-RCAP-D6) — lineage only, not answered

| QID | Original | R1 | Basis |
|---|---|---|---|
| Q030 (verification never substitutes for authentication/authorization) | No evidence | **Mapped (partial static)** → REC-RCAP-03 | The hook either returns or raises before the endpoint; it changes no user or rights; elevated access is used only to read configuration parameters (E4 L43, L80, L83) |
| Q033 (key rotation policy) | No evidence | **Mapped (partial static)** → REC-RCAP-17, REC-RCAP-26 | One plain key pair per database, no rotation or versioning mechanism in module scope |
| Q009 (min-score change takes effect predictably and is auditable) | → REC-RCAP-09/10 (disproved behaviour) | → **REC-RCAP-09R1, REC-RCAP-10R1** | Divergence and silent re-arm are the relevant evidence |
| Q008 (configured threshold enforced server-side) | → REC-RCAP-09, 11, 29 | → REC-RCAP-09R1, 11R1, 29 | The disconfirming observation "a request below the configured threshold succeeds" is the source-predicted outcome when the screen shows 0.7 but the parameter is absent |

Revised summary: Mapped 36 (previous 34 + Q030, Q033); No evidence yet 6 (Q017, Q018, Q027, Q029, Q037, Q040).

## 3. `base_sparse_field` — items

| REC ID | Supersedes | Position | REC class (R1) | Proof link (R1) | MODULE+QID lineage |
|---|---|---|---|---|---|
| **REC-SPRS-08R1** | REC-SPRS-08 wording (class kept) | A1 C08 "limited to the same model" vs A2 SF-1 + **SF-1R1-SPRS**: the limit is advisory (no server constraint); a cross-model pointer is re-resolved by container **name** on the field's **own** model at reflection → user error (availability risk at setup/upgrade) or silent raw-SQL re-point to a same-named own-model row (type not checked). It **never** results in storage in the other model's container | **CONTRADICTION** (unchanged vs A1 C08) | PC-SPRS-06 (constraint absence) + **PC-SPRS-22** (SOURCE, reflection re-resolution) / **PC-SPRS-23** (RUNTIME, PR-SPRS-10) | sparse+Q008, sparse+Q009 |

Dependent: REC-SPRS-13 note "target model is not checked (ties to REC-SPRS-08)" now reads "not checked at write; re-derived from the own model at reflection (REC-SPRS-08R1)". Class MATCH unchanged. Sparse class counts unchanged (24 items; 1 CONTRADICTION; 7 UNKNOWN_PENDING_PROOF).

### sparse QID lineage update (A3-SPRS-D1) — lineage only, not answered

| QID | Original | R1 | Basis |
|---|---|---|---|
| Q024 (defaults with an absent key) | No evidence | **Mapped (partial static)** → REC-SPRS-04 | An absent key reads as absent/empty; the compute applies no default |
| Q035 (record-level access honoured on traversal of a stored relation) | No evidence | **Mapped (partial static)** → REC-SPRS-05 | Relational values are held as bare ids and filtered only for existence on read; access-rule behaviour on traversal stays runtime/core |

Revised summary: Mapped 31 (previous 29 + Q024, Q035); No evidence yet 10 (Q022, Q023, Q025, Q026, Q027, Q029, Q032, Q033, Q034, Q041).

## 4. Handoff to PROOF

New or replacement proof links: PC-RCAP-06R, PC-RCAP-30 (SOURCE/CONFIG); PC-RCAP-31, PC-RCAP-32, PC-RCAP-27R (RUNTIME); PC-SPRS-22 (SOURCE); PC-SPRS-23 (RUNTIME). PC-RCAP-19 must stay as declared and be recorded as-is when executed.

## 5. Limitations

REC reconciles documents; source re-execution is in the PROOF addendum. No Lane B. Original REC files untouched.
