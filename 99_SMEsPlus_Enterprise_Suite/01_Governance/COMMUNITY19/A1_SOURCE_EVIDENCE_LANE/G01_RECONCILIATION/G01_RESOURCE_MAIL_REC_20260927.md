# G01 PLATFORM_BASE — Module `resource_mail` — RECONCILIATION (Stage 1)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of REC + PROOF; Proof recorded separately) |
| Governed group / module | G01 PLATFORM_BASE / `resource_mail` |
| Date | 2026-09-27 (intake 2026-09-27T15:02Z; Asia/Bangkok 22:02) |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/resource_mail/`, plus `addons/resource/` cross-references) |
| Question lineage | **MVQ lineage unavailable**: there is no module MVQ bank for `resource_mail` (GMVQ backlog). The lineage lens is Standard 55 only (W1-STD). |
| Lane B | None exists (search in section 3) |
| Next stage | PROOF → `G01_PROOF/G01_RESOURCE_MAIL_PROOF_20260927.md` |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (7 REC items: 2 MATCH, 2 GAP, 0 CONTRADICTION, 3 UNKNOWN_PENDING_PROOF) |

Format reference: this document follows `G01_RECONCILIATION/G01_BUS_REC_20260927.md`, which was created in parallel and found at 15:05Z. At intake (15:02Z) the reference directories did not exist.

## 2. Intake (immutable inputs; sha256 recorded at intake)

Paths are relative to `99_SMEsPlus_Enterprise_Suite/01_Governance/COMMUNITY19/`.

| Input | Path | sha256 | Check |
|---|---|---|---|
| Lane A | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_RESOURCE_MAIL_LANE_A_PASS1_20260927.md` | `7ddbb4501027579e85e689feefd4acf91cc73a29907d0e9fb8c6e89d5c453c45` | Equals the value recorded in the A1 and A2 headers |
| A1 | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_RESOURCE_MAIL_A1_PACKAGE_20260927.md` | `f3f552c5098154ed344d338ff91148b6a0f39a6c605fdb6df5284ff16cc88ee8` | Equals the value recorded in the A2 header |
| A2 | `A1_SOURCE_EVIDENCE_LANE/G01_A2_REVIEWS/G01_RESOURCE_MAIL_A2_REVIEW_20260927.md` | `e4e630b904a55c3b98a75ce26f82618c11fad62cce522e11370c60d8073c42a9` | A2 VERIFIED WITH FINDINGS; 5 claims VERIFIED; 2 omissions (O-01, O-02); 3 proof requirements (PR-01..PR-03) |
| Standard 55 | `GMVQ/G01_PLATFORM_BASE/QUESTION_BANK_STANDARD_55_V2.00.md` | `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` | Equals the `FREEZE_W1-STD.json` `bank_files` entry: MATCH |
| Freeze manifest | `GMVQ/G01_PLATFORM_BASE/FREEZE_W1-STD.json` | `370b92b43d56a99d6e6e444916356eb56e305fdf6bb86b4c7cd0d885a7ff317d` | `freeze_hash` `c64693eee3957388907637ad028ebdeea6fbeb19a093d1c459c5289f45f5c213` recomputed with the `freeze_batch.py` formula: MATCH. `resource_mail` is in the module list. |

The inputs were read only; none was edited. No git operations were run. The sha256 values were re-checked at close and had not changed.

## 3. Lane B evidence-pool search (recorded)

This is the same search as the `resource` REC (section 3), run in the same session over the whole repository tree:

- The filename search found 4 hits. All are infrastructure drafts under `CORE_RESOURCE_*` and are unrelated.
- The content search found 4 hits: A1 packages, the resource_mail A2 review, and a roster checkpoint. None is a runtime observation record.
- The runtime device is recorded OFFLINE since 2026-09-24T12:53Z.
- **Result: no Lane B runtime evidence exists for `resource_mail`.** Absence is shown as UNCORROBORATED or NOT_APPLICABLE and never as FAIL.

## 4. Classification rules applied (same as the `resource` REC)

| Class | Rule |
|---|---|
| MATCH | A2 VERIFIED the A1 claim on WHAT and WHY/RISK, and holding it needs no A2 runtime proof requirement. |
| GAP | A2 PARTIAL, or an A2 omission (promoted to a REC item). |
| CONTRADICTION | A2 directly contradicts an A1 statement, citing source. |
| UNKNOWN_PENDING_PROOF | A2 VERIFIED the source fact, but the conclusion is behavioural or security-related and A2 requires runtime proof. |

## 5. Reconciliation table

C01–C05 are A1 claims `A1-G01-RMAIL-Cnn`. The QID mapping is lineage by topical fit to Standard 55 only. **No QID is answered.**

| REC ID | Source item | A1 position (summary) | A2 verdict / correction | REC class | Lane B | Proof link | MODULE+STD-QID lineage |
|---|---|---|---|---|---|---|---|
| REC-RMAIL-01 | C01 | Hidden bridge; depends on resource + mail; auto-install; no data, security or views | VERIFIED; F-03: every tenant with both parent modules exposes presence through resources, and there is no switch to turn this off | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-01 → PC-RMAIL-01, R01 | — (no clear fit) |
| REC-RMAIL-02 | C02 | Random colour default in a small range; not unique or deterministic | VERIFIED (1–11 inclusive) | MATCH | NOT_APPLICABLE | PC-RMAIL-02 | — (no clear fit) |
| REC-RMAIL-03 | C03 | Presence mirrors the linked user; empty when there is no user (MED) | VERIFIED (definition); the empty case needs runtime | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-02 → PC-RMAIL-03, R02 | resource_mail+STD-Q36 |
| REC-RMAIL-04 | C04 | The avatar-card method is a plain read of fields the caller names; no filter or elevation; bounded by resource access | VERIFIED; exposure made precise in OM-01/OM-02 | UNKNOWN_PENDING_PROOF | UNCORROBORATED | PR-03 → PC-RMAIL-04, R03 | resource_mail+STD-Q28, Q29 |
| REC-RMAIL-05 | C05 | No new models, constraints, timezone logic, crons, controllers or ACLs | VERIFIED | MATCH | NOT_APPLICABLE | PC-RMAIL-05 | resource_mail+STD-Q29 |
| REC-RMAIL-06 | OM-01 (A2 O-01 / F-01) | (not named in A1) | The **avatar card can expose the linked user's email, phone, share flag and presence** to any internal user who can read the resource (same company or no company), because the resource mirrors these from the user | GAP | UNCORROBORATED | PR-03 → PC-RMAIL-04, R03 | resource_mail+STD-Q29, Q36 |
| REC-RMAIL-07 | OM-02 (A2 O-02 / F-02) | (not in A1) | **An empty field list returns all readable fields** (standard read semantics) | GAP | UNCORROBORATED | PR-03 → PC-RMAIL-06, R03 | resource_mail+STD-Q29 |

### Counts

| Class | Count | Items |
|---|---|---|
| MATCH | 2 | REC-RMAIL-02, 05 |
| GAP | 2 | REC-RMAIL-06, 07 |
| CONTRADICTION | 0 | — |
| UNKNOWN_PENDING_PROOF | 3 | REC-RMAIL-01, 03, 04 |
| **Total** | **7** | 5 A1 claims + 2 A2 omissions |

Lane B column: NOT_APPLICABLE 2 (REC-RMAIL-02, 05); UNCORROBORATED 5. FAIL: 0.

## 6. MODULE+STD-QID lineage summary

This section records lineage only. **MVQ lineage is unavailable** (GMVQ backlog), so QID-level A3 challenge is limited to Standard 55.

- **Mapped (3 distinct STD-QIDs):** Q28, Q29, Q36.
- REC items with no clear fit: REC-RMAIL-01, 02.
- Sections B, C, D and F of Standard 55 have no topical fit.

## 7. Carried forward

- A1 gaps G1 (JS UI unreviewed), G2 (presence field in `mail` not re-read) and G3 (no avatar-card caller identified) remain open.
- CRQ-RMAIL-01..03 are carried unchanged.
- A2 note carried: the PDPA-type personal-data exposure in OM-01 is an input for downstream IAM design. It is not resolved here.

## 8. Handoff to PROOF

PR-01..PR-03 pass to Proof as runtime cases PC-RMAIL-R01..R03. Static cases PC-RMAIL-01..06 cover the source basis of every item.

## 9. Limitations

- REC reconciles documents only. No Lane B evidence exists, so nothing here is runtime-corroborated.
- There is no Formal Coverage claim and no percentages. No QID is answered.
- Clean room: neutral summaries. Identifiers are pointers only.
