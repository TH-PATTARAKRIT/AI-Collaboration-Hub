# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `privacy_lookup`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_PRIVACY_LOOKUP_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `privacy_lookup` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/privacy_lookup/` |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_PRIVACY_LOOKUP_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `a6327b89e17634339e73777377718bc93e40963163ecd1b2b6f05ee97e0bb694`. This equals `bank_sha256` in `FREEZE_W1-B11.json` (manifest sha256 `19e3a1544a60572e63d22e31955226a9c632b27a25c7468d54fb1fee286678ed`, freeze hash `94852761617bd3fc7c38182d374f6e82f62b3f5701f59fe17355c3c295202ea5`). The manifest has a reduced field set (no `bank_files`, `authorization`, `frozen_at`) |
| Freeze-basis status | **W1-B11 DELTA-RECHECK** per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` (row W1-B11: "DELTA-RECHECK — basis not declared"). **QID-level lineage below is NOT A3-eligible until canonical re-freeze.** REC does not cure the freeze basis |
| Join key | MODULE `privacy_lookup` + QID + freeze hash above (provisional). Lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (32 REC items; 3 CONTRADICTION items carried into Proof, none closed by REC; QID lineage provisional / A3-ineligible) |

### 0.1 Input intake (immutable; sha256 recorded at intake 2026-09-27 15:04:27 UTC)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_PRIVACY_LOOKUP_A1_PACKAGE_20260927.md` | `61524ebc7f263672fc0d16d082515661558a3b36b24890e0f6b19b9a7ece056a` | Matches the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_PRIVACY_LOOKUP_A2_REVIEW_20260927.md` | `e10a3a0629e04ffc3e757ce6b8b9b97444f1b41b84be946e78dcdce1c9ee5aea` | Disposition "A2 VERIFIED WITH FINDINGS". 18 claims (15 VERIFIED, 3 PARTIAL). 9 proof requirements (PR-PRIV-01..09) |
| Lane A packet | `G01_LANE_A_PASS1/G01_PRIVACY_LOOKUP_LANE_A_PASS1_20260927.md` | `35ccba82e8c3582bc81c43141a812941eadd32044e8e7cb6db7950c36065fe99` | Matches the hash recorded in both the A1 and A2 headers |
| Question bank | see header | `a6327b89…e0bb694` | Equals FREEZE_W1-B11 `bank_sha256` |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B11.json` | `19e3a1544a60572e63d22e31955226a9c632b27a25c7468d54fb1fee286678ed` | Equals the manifest sha256 cited by A2; reduced field set |

### 0.2 Lane B evidence-pool search (recorded 2026-09-27 15:04:47 UTC)

- Command: `grep -ril privacy_lookup /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite`. It returned 36 files: Lane A, A1 and A2 artifacts for this module (and phone_validation's, which cite it); G01 intake/checkpoint files; GMVQ freeze/status/review files; and source/dump inventory CSVs (not runtime observations).
- Filtering those hits for `lane_b|laneb|gemini|runtime|evidence_pool|observ` returned **no match** (rc=1).
- `find /home/user/AI-Collaboration-Hub` for names `*lane_b*`, `*gemini*`, `*evidence_pool*` returned **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `privacy_lookup`**. Absence is not a failure. Every Lane B cell is UNCORROBORATED or NOT_APPLICABLE.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited.

## 1. Classification rules (predeclared; same rules as the G01 `base_automation` REC)

- **MATCH**: A1 and A2 agree, and a source re-read supports the claim.
- **GAP**: evidence missing and not settleable by static or runtime proof in scope.
- **CONTRADICTION**: A1 and A2 disagree (A2 PARTIAL correction), or the source disagrees with intent the source itself declares.
- **UNKNOWN_PENDING_PROOF (UPP)**: A1 and A2 agree at source level (or A2 adds a statically predicted omission), but the claim or its risk is inherently runtime-dependent.
- **Lane B column**: UNCORROBORATED or NOT_APPLICABLE. Never FAIL for absence.
- **Scope**: A1 claims C01–C18; A2 omissions O-PRIV-01..09; carried A1 gaps not absorbed (GAP-PRIV-02, -03, -06, -07, -09). Folds: GAP-01→C12/O-05, GAP-04→C05/O-01, GAP-05→C14, GAP-08→C13/O-04. A2 candidates: X1→C06/C07 (C03), X2→C12/O-05.

## 2. Reconciliation table

PC = proof case in the PROOF package. Static cases PC-PRIV-10..22 executed; runtime PC-PRIV-01..09 pending.

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (provisional; not A3-eligible) |
|---|---|---|---|---|---|---|---|---|
| REC-PRIV-01 | C01 | Hidden auto-install "Privacy", depends mail only; purpose inferred / HIGH | VERIFIED | MATCH | Manifest re-read | NOT_APPLICABLE | — | — |
| REC-PRIV-02 | C02 | Email must normalize before query; name/email trimmed / HIGH | VERIFIED (display-name form accepted) | MATCH | Re-read; display-form acceptance carried in O-04 | UNCORROBORATED | PC-12 (context) | Q001, Q002, Q003 |
| REC-PRIV-03 | C03 | Raw SQL after flush; bypasses record/company rules; "no company reference at all" / HIGH | **PARTIAL** — literal wording false (a comment and one field name mention company); substance holds | **CONTRADICTION** (A1 vs A2, wording) | Substance source-confirmed (PC-13 PASS): no company predicate. A1's absolute wording is contradicted by A2; both preserved. Runtime cross-company effect pending | UNCORROBORATED | PC-13; PC-01 | Q017, Q036, Q038 |
| REC-PRIV-04 | C04 | Fixed scope + dynamic scope with 6 exclusions, 4 email-like fields + name, non-cascade partner refs / HIGH | VERIFIED (name condition only on models with an email-like field) | MATCH | Re-read; A2 nuance is consistent with A1 | NOT_APPLICABLE | PC-11 (context) | Q003, Q005, Q006, Q007, Q008, Q009, Q010, Q012, Q013, Q014, Q037, Q040 |
| REC-PRIV-05 | C05 (+GAP-04) | Name as raw pattern; email display fields wildcarded; no phone/address/free text / MED | VERIFIED (+SF-01 omission) | UPP | Match operators confirmed (PC-10). Over/under-matching is runtime | UNCORROBORATED | PC-10, PC-11; PC-02 | Q004, Q010, Q011 |
| REC-PRIV-06 | C06 (X1 read side) | Reference hidden without read access; display name via sudo / HIGH | VERIFIED | MATCH | Re-read (PC-21) | UNCORROBORATED | PC-21; PC-01 (optional) | Q017, Q018, Q019 |
| REC-PRIV-07 | C07 (X1 write side) | Archive/delete with sudo, cross-company / HIGH | VERIFIED | UPP | Sudo write/unlink confirmed (PC-13, PC-17). Cross-company effect is runtime | UNCORROBORATED | PC-13, PC-17; PC-01 | Q015, Q020, Q021, Q038 |
| REC-PRIV-08 | C08 | Repeat delete errors; bulk skips; "UI asks for confirmation before delete" / HIGH | **PARTIAL** — confirmation only on per-line button; bulk server action has none | **CONTRADICTION** (A1 vs A2) | Source/config re-read supports A2 (PC-16 PASS). Both preserved | UNCORROBORATED | PC-16 | Q016, Q021, Q023, Q024, Q025 |
| REC-PRIV-09 | C09 | No anonymize/redact action for found records / HIGH | VERIFIED | MATCH | Re-read | UNCORROBORATED | — | — |
| REC-PRIV-10 | C10 | One log per wizard at first non-empty detail; later updates; lookup alone no log / HIGH | VERIFIED (update is overwrite → SF-02) | UPP | Mechanism confirmed (PC-14, PC-15). Log content over a session is runtime | UNCORROBORATED | PC-14, PC-15; PC-03 | Q020, Q021, Q026, Q031, Q034 |
| REC-PRIV-11 | C11 | Log fields and masking rules / HIGH | VERIFIED | MATCH | Re-read | UNCORROBORATED | — | Q027, Q028, Q029, Q030 |
| REC-PRIV-12 | C12 (+GAP-01, X2) | Email masking returns error object instead of raising / HIGH defect, LOW reach | VERIFIED (reach refined by SF-05) | UPP | Return-not-raise confirmed (PC-18). Stored value on direct creation is runtime | UNCORROBORATED | PC-18; PC-06 | Q028 |
| REC-PRIV-13 | C13 (+GAP-08) | Log receives untrimmed raw name/email / MED | VERIFIED (+SF-04) | UPP | Confirmed (PC-19). Failure mode at remediation is runtime | UNCORROBORATED | PC-19; PC-07 | Q002, Q028 |
| REC-PRIV-14 | C14 (+GAP-05) | System-only; line no delete; log full CRUD / HIGH | VERIFIED | MATCH | ACL re-read (PC-20) | UNCORROBORATED | PC-20 | Q022 |
| REC-PRIV-15 | C15 | Wizard/lines 24 h; log no retention / HIGH | VERIFIED | MATCH | Re-read (PC-22). Cleanup-ordering effect on log carried in O-02 | NOT_APPLICABLE | PC-22; PC-04 (via O-02) | Q033 |
| REC-PRIV-16 | C16 | Log menu under technical menu; debug-only model names; sudo model list / MED | VERIFIED | MATCH | Re-read | UNCORROBORATED | — | Q031, Q032 |
| REC-PRIV-17 | C17 | Re-lookup replaces lines; RISK "actions already taken remain only in the log" / HIGH | **PARTIAL** — mechanics hold; RISK contradicted: the log is an overwritten snapshot, re-lookup blanks details | **CONTRADICTION** (A1 vs A2) | Source supports A2 (PC-14, PC-15 PASS): details are replaced, not accumulated. Both preserved. Runtime PC-03 pending | UNCORROBORATED | PC-14, PC-15; PC-03 | Q035 |
| REC-PRIV-18 | C18 | Partner/user server actions admin-only; bulk actions on lines / MED | VERIFIED | MATCH | Re-read | UNCORROBORATED | PC-16 (context) | Q022 |
| REC-PRIV-19 | O-PRIV-01 (SF-01) | (not stated) | **HIGH** — unescaped wildcards; "%" name → whole-DB scope; sudo cross-company | UPP | Static chain confirmed (PC-10, PC-11, PC-12, PC-13 PASS); also via email (Proof R1). Runtime pending | UNCORROBORATED | PC-10..13; PC-02 | Q004, Q038 |
| REC-PRIV-20 | O-PRIV-02 (SF-02) | (C17 RISK) | **HIGH** — log is an overwritten snapshot; archive→unarchive keeps last; re-lookup blanks | UPP | Confirmed statically (PC-14, PC-15). Runtime pending (incl. cleanup ordering) | UNCORROBORATED | PC-14, PC-15; PC-03, PC-04 | Q026, Q031, Q033, Q035 |
| REC-PRIV-21 | O-PRIV-03 (SF-03) | (not stated) | MED — archive runs inside change handler before save | UPP | Confirmed (PC-17). Discard behaviour is runtime | UNCORROBORATED | PC-17; PC-05 | Q020 |
| REC-PRIV-22 | O-PRIV-04 (SF-04) | (GAP-08) | MED — display-form email accepted; multi-"@" raw input breaks masking | UPP | Confirmed (PC-19; harness shows display form with "@" in name normalizes). Rollback of preceding delete is runtime | UNCORROBORATED | PC-19, PC-12; PC-07 | Q011, Q028 |
| REC-PRIV-23 | O-PRIV-05 (SF-05) | (C12) | LOW — error path unreachable from wizard; reachable by direct log creation | UPP | Confirmed statically (PC-18, PC-20: log create granted). Stored value is runtime | UNCORROBORATED | PC-18; PC-06 | Q028 |
| REC-PRIV-24 | O-PRIV-06 (SF-06) | (C11) | MED — log is pseudonymized, not anonymous | MATCH | Semantic evaluation of source-confirmed masking rules; no runtime needed | NOT_APPLICABLE | — | Q027, Q029 |
| REC-PRIV-25 | O-PRIV-07 (SF-08) | (C04) | MED — messages not found by raw sender/recipient address | MATCH | Message model excluded from dynamic scope; fixed part uses author only (source re-read) | UNCORROBORATED | PC-11 (context) | Q006 |
| REC-PRIV-26 | O-PRIV-08 (SF-09) | (C08) | MED — bulk delete no confirmation | MATCH | Declarative; confirmed (PC-16) | UNCORROBORATED | PC-16 | Q024 |
| REC-PRIV-27 | O-PRIV-09 | (C11, C14) | MED — no controller/company attribution on log; no request lifecycle | MATCH | Log fields re-read; structural absence | NOT_APPLICABLE | — | Q038 |
| REC-PRIV-28 | GAP-PRIV-02 | Cascade/restrict effects of sudo delete | VERIFIED as gap; A2 runtime | UPP | Outside module; runtime PC-08 | UNCORROBORATED | PC-08 | Q014 |
| REC-PRIV-29 | GAP-PRIV-07 | Target changed/removed after lookup | VERIFIED as gap; A2 runtime | UPP | Runtime PC-09 | UNCORROBORATED | PC-09 | Q039 |
| REC-PRIV-30 | GAP-PRIV-03 | No documented legal scope | VERIFIED as gap | GAP | No source can settle | NOT_APPLICABLE | — | — |
| REC-PRIV-31 | GAP-PRIV-06 | Tests not reviewed | VERIFIED as gap | GAP | Not read | NOT_APPLICABLE | — | — |
| REC-PRIV-32 | GAP-PRIV-09 | Freeze basis W1-B11 DELTA-RECHECK | VERIFIED as gap | GAP | Governance: needs canonical re-freeze (GMVQ/OVQDT), not Proof | NOT_APPLICABLE | — | all (lineage provisional) |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 14 | C01, C02, C04, C06, C09, C11, C14, C15, C16, C18, O-06, O-07, O-08, O-09 |
| CONTRADICTION | 3 | C03 (A1 vs A2, wording), C08 (A1 vs A2), C17 (A1 vs A2, log RISK) |
| UNKNOWN_PENDING_PROOF | 12 | C05, C07, C10, C12, C13, O-01, O-02, O-03, O-04, O-05, GAP-02, GAP-07 |
| GAP | 3 | GAP-03, GAP-06, GAP-09 |
| **Total** | **32** | 18 A1 claims + 9 A2 omissions + 5 carried gaps |

Lane B column: UNCORROBORATED 24, NOT_APPLICABLE 8 (C01, C04, C15, O-06, O-09, GAP-03, GAP-06, GAP-09). No FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- C17: A1's RISK ("actions already taken remain only in the log") and A2's SF-PRIV-02 (log details are an overwritten snapshot; re-lookup blanks them) are both preserved. Static re-read supports A2 (PC-14, PC-15). Runtime PC-03/PC-04 pending.
- C08: A1's "UI asks for confirmation before delete" vs A2's "per-line only; bulk has none". Config supports A2 (PC-16).
- C03: A1's absolute "no company reference" vs A2's wording correction; the substantive conclusion (no company scoping) is shared and source-confirmed (PC-13).

## 3. QID lineage map (bank W1-B11; PROVISIONAL — NOT A3-ELIGIBLE until canonical re-freeze)

Provisional join key: MODULE `privacy_lookup` + QID + freeze hash `94852761617bd3fc7c38182d374f6e82f62b3f5701f59fe17355c3c295202ea5`. Because W1-B11 is DELTA-RECHECK, this map must be re-validated against the re-frozen bank before A3 may rely on it. Mapping is topical lineage only; no QID is answered.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-PRIVACY-LOOKUP-Q001 | Invalid email rejected first | REC-02 (C02) |
| G01-PRIVACY-LOOKUP-Q002 | Whitespace does not change identity | REC-02, REC-13 (C13) |
| G01-PRIVACY-LOOKUP-Q003 | Normalized emails resolve same partner | REC-02, REC-04 |
| G01-PRIVACY-LOOKUP-Q004 | Case-insensitive name matching | REC-05 (C05), REC-19 (O-01) |
| G01-PRIVACY-LOOKUP-Q005 | Users via login/partner | REC-04 |
| G01-PRIVACY-LOOKUP-Q006 | Direct messages discoverable | REC-04, REC-25 (O-07) |
| G01-PRIVACY-LOOKUP-Q007 | No duplicate actionable rows | REC-04 |
| G01-PRIVACY-LOOKUP-Q008 | Transient models excluded | REC-04 |
| G01-PRIVACY-LOOKUP-Q009 | Non-auto models excluded | REC-04 |
| G01-PRIVACY-LOOKUP-Q010 | Stored email fields discoverable | REC-04, REC-05 |
| G01-PRIVACY-LOOKUP-Q011 | Normalized vs display email matching | REC-05, REC-22 (O-04) |
| G01-PRIVACY-LOOKUP-Q012 | Governed record-name participation | REC-04 |
| G01-PRIVACY-LOOKUP-Q013 | Non-cascade partner references | REC-04 |
| G01-PRIVACY-LOOKUP-Q014 | Cascade-owned refs not independent targets | REC-04, REC-28 (GAP-02) |
| G01-PRIVACY-LOOKUP-Q015 | Active/archived state preserved | REC-07 (C07) |
| G01-PRIVACY-LOOKUP-Q016 | No active field → not archive-capable | REC-08 (C08) |
| G01-PRIVACY-LOOKUP-Q017 | Company-restricted not openable | REC-03, REC-06 |
| G01-PRIVACY-LOOKUP-Q018 | Opening respects read authority | REC-06 |
| G01-PRIVACY-LOOKUP-Q019 | Labels do not over-disclose | REC-06 |
| G01-PRIVACY-LOOKUP-Q020 | Archive changes state and records event | REC-07, REC-10, REC-21 (O-03) |
| G01-PRIVACY-LOOKUP-Q021 | Delete removes, marks, records | REC-07, REC-08, REC-10 |
| G01-PRIVACY-LOOKUP-Q022 | Admin-only access | REC-14 (C14), REC-18 (C18) |
| G01-PRIVACY-LOOKUP-Q023 | Bulk archive only eligible active | REC-08 |
| G01-PRIVACY-LOOKUP-Q024 | Bulk delete skip/once | REC-08, REC-26 (O-08) |
| G01-PRIVACY-LOOKUP-Q025 | Second delete fails clearly | REC-08 |
| G01-PRIVACY-LOOKUP-Q026 | One log, later actions update | REC-10, REC-20 (O-02) |
| G01-PRIVACY-LOOKUP-Q027 | Name masked before persistence | REC-11, REC-24 (O-06) |
| G01-PRIVACY-LOOKUP-Q028 | Email local part masked | REC-11, REC-12, REC-13, REC-22, REC-23 |
| G01-PRIVACY-LOOKUP-Q029 | Domain masking rule | REC-11, REC-24 |
| G01-PRIVACY-LOOKUP-Q030 | Handler recorded | REC-11 |
| G01-PRIVACY-LOOKUP-Q031 | Found-record summaries reconcile | REC-10, REC-16, REC-20 |
| G01-PRIVACY-LOOKUP-Q032 | Technical identifiers debug-only | REC-16 (C16) |
| G01-PRIVACY-LOOKUP-Q033 | Transient expiry; logs remain | REC-15 (C15), REC-20 |
| G01-PRIVACY-LOOKUP-Q034 | Lookup alone creates no log | REC-10 |
| G01-PRIVACY-LOOKUP-Q035 | Re-lookup replaces stale results | REC-17 (C17), REC-20 |
| G01-PRIVACY-LOOKUP-Q036 | Flush before query | REC-03 |
| G01-PRIVACY-LOOKUP-Q037 | One row per record identity | REC-04 |
| G01-PRIVACY-LOOKUP-Q038 | No cross-tenant discovery/remediation | REC-03, REC-07, REC-19 (O-01), REC-27 (O-09) |
| G01-PRIVACY-LOOKUP-Q039 | Stale target handled deterministically | REC-29 (GAP-07) |
| G01-PRIVACY-LOOKUP-Q040 | Discovery aligned after upgrade/schema change | REC-04 |

**Provisionally mapped: 40 QIDs; no evidence yet: 0.** All 40 are provisional under GAP-PRIV-09 and not A3-eligible. No mapping answers a QID.

## 4. PDPA-relevance notes (HIGH / flagged items; design implication only, neutral)

Reference frame: Thailand Personal Data Protection Act B.E. 2562 themes. Design implications for SMEsPlus only; not legal conclusions about the reference ERP.

| Item | A2 severity | PDPA theme | Design implication (neutral) |
|---|---|---|---|
| O-PRIV-01 / PR-PRIV-02 (unescaped wildcards → whole-database lookup under sudo, cross-company) | HIGH | Erasure right (s.33) scoped to the requesting data subject; security and integrity of other subjects' data (s.37) | Subject matching treats all user input as literal values; discovery and remediation stay within the tenant/controller scope of the request; the result set is bounded and reviewed before any destructive action. |
| O-PRIV-02 / C17 (log is an overwritten snapshot; archive→unarchive keeps last; re-lookup blanks details) | HIGH | Accountability and records of processing (s.39); demonstrating that a request was handled | Each remediation action is recorded as its own append-only event (action, target, time, operator, request reference) that later actions cannot replace or blank. |
| O-PRIV-08 / C08 (bulk delete without confirmation) | MED | Security safeguards against accidental loss (s.37) | Irreversible bulk erasure requires an explicit confirmation step that shows scope (count, models, companies) before execution. |

## 5. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_PRIVACY_LOOKUP_PROOF_20260927.md`.
- Proof must address the 12 UNKNOWN_PENDING_PROOF items and the 3 CONTRADICTION items. The 3 GAP items are carried forward; GAP-PRIV-09 routes to GMVQ/OVQDT canonical re-freeze.

## 6. Limitations

- REC used only the inputs in 0.1 and, for classification support, the static proof results from Stage 2. No runtime evidence exists.
- QID lineage is provisional (DELTA-RECHECK). It is not a coverage measure. No Formal Coverage claim. No percentages.
- The effective discovery scope depends on the installed module set, which was not assessed.
