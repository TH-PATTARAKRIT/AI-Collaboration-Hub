# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum R1 (A3 remediation, batch 3C) — `phone_validation`, `privacy_lookup`, `utm`, `onboarding`, `html_builder`, `web_hierarchy`, `web_unsplash`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. The parent REC files are immutable and were not edited |
| Group / Modules | G01 PLATFORM_BASE / `phone_validation`, `privacy_lookup`, `utm`, `onboarding`, `html_builder`, `web_hierarchy`, `web_unsplash` |
| Date | 2026-09-27 (written after 15:42:01Z; frozen before the Proof R1 predeclaration) |
| Governing rules | `01_Governance/COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` sha256 `d3966ad058ca11e82ef20ec777818486a726996f8d04f6a59da4315cf6e84e42` |
| Parent REC artifacts (sha256; equal to the A3 intake values; re-verified 2026-09-27T15:36Z). **These values are the frozen parent REC hashes for rule 4** | `G01_RECONCILIATION/G01_PHONE_VALIDATION_REC_20260927.md` `87a34f17b618b902a8933413c706c76cdaeccc9cfec6d6fd3626160c7187a717`; `G01_RECONCILIATION/G01_PRIVACY_LOOKUP_REC_20260927.md` `86a047dce7eac80b3b2563bd815f770e54d9de8d42734711de5becc9b787c41a`; `G01_RECONCILIATION/G01_UTM_REC_20260927.md` `cd2576689b4b0412614109f11ff7b2c1eafd5d3cf4460c8c2ee65fbc68e19975`; `G01_RECONCILIATION/G01_ONBOARDING_REC_20260927.md` `fdd2d41b3b3cfdc7d5612820ff46c6c226da92d95d27012adbbd384308b91889`; `G01_RECONCILIATION/G01_HTML_BUILDER_REC_20260927.md` `d6efb05e3e3893dce981084d0f2a93cefa42b017cdb1a407677f5aa3d51b9803`; `G01_RECONCILIATION/G01_WEB_HIERARCHY_REC_20260927.md` `ac6842312bd2159b6b642f7fafe929cc30ac72d1f14cfc382aff70df77509e53`; `G01_RECONCILIATION/G01_WEB_UNSPLASH_REC_20260927.md` `66eb15218a853ab0f43589e5558b4622586080aa3d8c1a8a2f6eb2a5de1f3ffd` |
| Parent A1 packages (sha256; unchanged) | phone `e128cb2e9905aed013c9447c922441d4680c46467b7355f92ce01d14e0c003b0`; privacy `61524ebc7f263672fc0d16d082515661558a3b36b24890e0f6b19b9a7ece056a`; utm `85eae7ff04c6d30708d616fc5e863359eab561555d9a72bb0db1ea42a7b4d6ce`; onboarding `50b0f4d675880e20dd64319ba8d904fbe31ac6f60e0e4cfdc0df2959c12271a9`; html_builder `2cfc3d1e75a6a3a7db1c123c5aac73ea87802aaeaef17e74c15e3d5b050a3332`; web_hierarchy `45c325c42cd33aca747b18e11875086246257c9a1ef289453c53eef2115434a2`; web_unsplash `56fbe9f1bd4dea215de6daae9f829eb4fa2eeb63e522b4f5eecbc14cc9598829` |
| Additional input (immutable; written earlier in this remediation) | A2 addendum `G01_A2_REVIEWS/G01_B3C_A2_ADDENDUM_R1_20260927.md` sha256 `a364fa30d6007c06dc34f79747a8bc6fc60afea71a4bacf131940a0720581750` (frozen 2026-09-27T15:42:01Z). The parent A2 reviews are listed in that addendum's section 0.1 and are unchanged |
| A3 reports | As listed in the A2 addendum section 0.2 (7 files, sha256 recorded there) |
| Source used by REC | REC re-derivation re-read the A2 re-derivation copies (`remed_b3c/src_a2/`, all blobs verified; log sha256 `c1ed2eae3617c736b4398b4651365d07799605a573a23bf654d79e2485bd0c26`). **REC cites no Proof R1 result.** Parent Proof results are cited only where marked `POST-PROOF ANNOTATION` (section 8) |
| Lane B | None exists for any of the seven modules (parent REC searches). Absence is never FAIL |
| Question lineage | phone: W1-B10 ELIGIBLE (bank `c70aae33…0a50b8a80`). privacy: W1-B11 DELTA-RECHECK, **not A3-eligible**. utm: W1-B03 (bank `af28ded2…6ecd`). onboarding: W1-B09 HOLD, Standard 55 only. html_builder: W1-B06 HOLD, Standard 55 only. web_hierarchy and web_unsplash: no bank, Standard 55 only. **No QID is answered** |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean room: neutral paraphrase only. Identifiers and line numbers are pointers only, and no code is reproduced. No percentages. No Formal Coverage claim. No git operations. No existing artifact was edited.

### 0.1 Classification rules (unchanged from the parents) and R1 conventions

- MATCH, GAP, CONTRADICTION and UNKNOWN_PENDING_PROOF (UPP) keep the definitions in each parent REC.
- **Lane B column (R1 rule):** A2's Lane B class is carried unchanged, including `MISSING_REQUIRED_RUNTIME_PROOF` (MRRP). Where A2 did not class an item (omissions and A1 structural items), REC uses UNCORROBORATED when the item is runtime-observable and NOT_APPLICABLE when it is a static declaration. It is never FAIL.
- **Structural items (rule 3):** A1 §2 business rules (BR), §3 states (ST), §4 exceptions (EX), §5 handoffs (H), §6 gaps (G), §7 CRQs and §8 contradictions/candidates (X) are reconciled below. A2 did not always issue a separate verdict for a structural item. In that case the A2 position is the parent A2 verdict on the claims the item cites, plus the A2 omissions and the A2 addendum. That source is stated in each row.
- **CRQ rows** are decision requests, not evidence claims. Their REC class is `CARRIED` (not a MATCH/GAP/CONTRADICTION/UPP class), and each row records the A2 widening, if any.
- New proof links name A2 PR ids or Proof-R1 case ids reserved by this REC for the Proof stage. The ids are forward references. **No Proof R1 result exists or is cited here.**

---

## 1. `phone_validation`

### 1.1 Rule 1: Lane B label restoration (parent REC section 2 Lane B column)

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-PHON-02 | C02 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-05 | C05 (X2 reachability) | NOT_APPLICABLE | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-06 | C06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-07 | C07 (X1) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-09 | C09 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-11 | C11 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-14 | C14 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-15 | C15 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PHON-16 | C16 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

Parent 29 items after R1: MRRP 10, UNCORROBORATED 12, NOT_APPLICABLE 7, FAIL 0.

### 1.2 Corrections to existing REC items (class unchanged unless stated)

| REC ID | Challenge | R1 correction |
|---|---|---|
| REC-PHON-21 | A3-PHON-D1, CH-1 | **Severity HIGH now explicitly covers both directions** (A2 addendum SF-PHON-01-R1). R1 (removal-side un-suppression) and the **absent-entry branch** (an archived entry is created for the acting user's number when none exists; source `phone_blacklist.py`@d94486f6 L108–127 with L23–59) are part of this item. They are no longer a verdict-neutral "refinement". Basis now cites A2-R1 (not Proof R1). Class UPP (unchanged). Lane B UNCORROBORATED (A2 did not class omissions). R1 proof links: PR-PHON-01, PR-PHON-11 (runtime), static basis reserved for Proof R1 |
| REC-PHON-25 | A3-PHON-D6 | The A2 basis is SF-PHON-06-R1 (neutral design-implication wording). Class MATCH (unchanged) |
| REC-PHON-30 (new) | CH-1 bounded caveat | **GAP-PHON-10 (A2 addendum):** whether any UI path in SMS or marketing consumer modules passes a record with no sanitized number to the set/reset helpers is not established. The consumers were not read by any stage. Class **GAP**. Lane B NOT_APPLICABLE. Proof link: PR-PHON-03 (runtime, existing). QID lineage: Q023, Q036 |
| §4 PDPA table, row O-PHON-01 | A3-PHON-D1 | Row text now reads "wrong-subject suppression **and un-suppression** via empty-value fallback (add and remove directions, including creation of an archived entry for the acting user)". Design implication unchanged: bind only to the submitted identity; reject unvalidatable input; audit records the submitted input |

### 1.3 A3-PHON-D4: Q039 partial lineage

Re-derivation:
- Add is state-idempotent. Existing entries are found including archived ones and returned or reactivated. The number is unique (`phone_blacklist.py` L43–59).
- Remove is state-idempotent. Found entries are archived, and a repeat creates nothing new (L112–127).
- Audit is not idempotent. Each retry that carries a message logs it again (L89–90, L115–116, L120–125).

| QID | Topic (paraphrased) | Mapped REC items (R1) | Scope of lineage |
|---|---|---|---|
| G01-PHONE-VALIDATION-Q039 | Outcome knowable before retry; a retry must not change state twice | REC-12, REC-13, REC-29 (partial) | Partial, and lineage only. Retry clause: state change is idempotent on source, but the audit trail duplicates messages. First clause (outcome knowable before retry): runtime/UX, with no evidence. **The QID is not answered** |

QID map after R1: 40 QIDs mapped, one of them (Q039) partially. QIDs with no evidence: none. This is not a coverage measure.

### 1.4 Rule 3: A1 structural items reconciled

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-PHON-BR1 | BR1: one entry per stored value, database-wide | Holds, but the stored value depends on the acting user (A2 T6; SF-01-R1, SF-02) | UPP | UNCORROBORATED | → REC-02, REC-21, REC-22 |
| REC-PHON-BR2 | BR2: removal is archive, never delete, through the API | Holds as worded (A2 T6). The ACL allows a hard delete (O-05). A removal can archive the wrong subject (SF-01-R1) | MATCH (scoped to "through the API"); wrong-subject effect carried by REC-21 | UNCORROBORATED | → REC-13, REC-25 |
| REC-PHON-BR3 | BR3: a re-add reactivates | Holds (A2 T6; C12) | MATCH | UNCORROBORATED | → REC-12 |
| REC-PHON-BR4 | BR4: admin-only list access; sudo helpers bypass it | Holds (A2 T6). Reachability sits outside the module (X2, GAP-PHON-10) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C05) | PR-PHON-03 |
| REC-PHON-BR5 | BR5: country precedence record → partner → company | Holds for records. For list writes the "record" is the acting user (A2 T6; SF-02) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C11) | PR-PHON-07, PR-PHON-10 |
| REC-PHON-BR6 | BR6: format failure silent on records; direct create/write raises | **Negated in part:** holds for non-empty invalid input only. Empty or unformattable input through add/remove/mixin does not raise and is replaced by the acting user's number (A2 T6; SF-01-R1) | **CONTRADICTION** (A1 vs A2; both preserved) | UNCORROBORATED | → REC-21; PR-PHON-01, PR-PHON-11 |
| REC-PHON-ST1 | Entry lifecycle absent → active → archived → active; absent → archived | The transitions hold (C12, C13). The subject of an "absent → archived" or "active → archived" transition can be the acting user instead of the submitted number (SF-01-R1) | UPP | UNCORROBORATED | PR-PHON-11 |
| REC-PHON-ST2 | Record flag derived live, not stored | Holds. Both flags are non-stored computes (C06, C15 VERIFIED) | MATCH | UNCORROBORATED | — |
| REC-PHON-ST3 | Sanitized number recomputed on phone, country and stored-partner field changes | REC re-read (`mail_thread_phone.py`@01ca256f L172–173, L232–240): the triggers are the number fields, the country field and stored partner fields. Observation: the current-company fallback country is not a trigger | MATCH (with observation) | UNCORROBORATED | — |
| REC-PHON-EX1 | Invalid or impossible number on create/write → user error | Holds for non-empty input (C08). Empty input: see BR6 | MATCH (non-empty scope) | UNCORROBORATED | → REC-PHON-BR6 |
| REC-PHON-EX2 | Duplicate stored number → uniqueness error | The create path pre-empts duplicates by reactivating or returning existing entries (L43–55). The DB error remains the backstop for write and for races (GAP-09) | MATCH (backstop scope) | UNCORROBORATED | → REC-29 |
| REC-PHON-EX3 | Wizard without write access → access error at the record entry point only | A2 PARTIAL (C07): the wizard ACL is system-only and apply is not elevated | CONTRADICTION (as REC-07) | MISSING_REQUIRED_RUNTIME_PROOF | PR-PHON-02 |
| REC-PHON-EX4 | Phone search without phone fields → error; under 3 characters restricted | A2 PARTIAL (C16): the error is narrower | CONTRADICTION (as REC-16) | MISSING_REQUIRED_RUNTIME_PROOF | PR-PHON-08 |
| REC-PHON-EX5 | Library absent → silent raw passthrough | Holds (C09) | UPP | MISSING_REQUIRED_RUNTIME_PROOF | PR-PHON-05 |
| REC-PHON-H1 | mail: chatter, tracking, partner-field discovery | Holds. The discovery helper in mail was not read | MATCH (bounded) | NOT_APPLICABLE | — |
| REC-PHON-H2 | base: helpers injected; partner and users extended | Holds (C17, C19) | MATCH | NOT_APPLICABLE | — |
| REC-PHON-H3 | Portal deactivation hook is defined outside the module | Holds. Caller elevation is not established (GAP-02) | UPP | UNCORROBORATED | PR-PHON-09; static cross-module read reserved for Proof R1 |
| REC-PHON-H4 | Downstream SMS/marketing consumers read the flags (unverified) | Not verified by any stage | GAP (→ REC-PHON-30) | NOT_APPLICABLE | PR-PHON-03 |
| REC-PHON-H5 | No edge to privacy_lookup | Holds (A2 T6) | MATCH | NOT_APPLICABLE | — |
| REC-PHON-G | GAP-PHON-01..09 | Already reconciled: 01 → REC-27, 02 → REC-17, 03 → REC-07, 04 → REC-11, 05 → REC-15, 06 → REC-16, 07 → REC-28, 08 → REC-05 (+ REC-30), 09 → REC-29 | (as mapped) | (as mapped) | — |
| REC-PHON-X | CANDIDATE-PHON-X1, X2 | Already folded: X1 → REC-07/REC-23; X2 → REC-05 | (as mapped) | MRRP (A2) | — |
| REC-PHON-CRQ1..8 | CRQ-PHON-01..08 | CRQ-01 + O-07; CRQ-02 + SF-03; **CRQ-03 strengthened by SF-01-R1 (reject, never substitute, in both directions)**; CRQ-04 + SF-02; CRQ-05 unchanged; CRQ-06 + SF-04 (bulk oracle); CRQ-07 + SF-06-R1; CRQ-08 unchanged | CARRIED | — | — |

Phone totals after R1 (parent 29 + REC-30 + 19 structural rows; the G, X and CRQ mapping rows are not counted):

| Class | Count | Items |
|---|---|---|
| MATCH | 19 | Parent 10, plus BR2, BR3, ST2, ST3, EX1, EX2, H1, H2, H5 |
| CONTRADICTION | 6 | C07, C16, C20, BR6, EX3, EX4 |
| UPP | 19 | Parent 13, plus BR1, BR4, BR5, ST1, EX5, H3 |
| GAP | 5 | REC-27, REC-28, REC-29, REC-30, H4 |
| **Total** | **49** | |

Rows mapped "as REC-nn" repeat an existing item's class, so MASTER should consume per-row classes.

---

## 2. `privacy_lookup`

### 2.1 Rule 1: Lane B label restoration

| REC ID | Item | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-PRIV-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-05 | C05 (SF-01) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-07 | C07 (X1) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-10 | C10 (SF-02/03) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-12 | C12 (X2) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-13 | C13 (SF-04) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-17 | C17 (SF-02) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-28 | GAP-PRIV-02 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-PRIV-29 | GAP-PRIV-07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

### 2.2 Corrections to existing REC items

| REC ID | Challenge | R1 correction |
|---|---|---|
| REC-PRIV-19 | A3-PRIV-D1, D2 | A2 verdict column is now **SF-PRIV-01-R1 (HIGH)**. Over-matching comes through the name (multi-character wildcard) **or** the email (e.g. `%@%`, via A2-R1), plus underscore and homonym over-match. Basis wording: "Discovery is a raw SQL lookup on the database cursor; it needs no elevation, and access and company rules never apply to it. Scope is database-wide across partners, users, authored messages and every table-backed, non-transient, non-excluded model with a stored email-like field or a stored non-cascade partner reference. Elevation applies to display names, archive/unarchive, delete and the model list." This replaces "'%' name → whole-DB scope; sudo cross-company". Class UPP (unchanged). R1 proof links: PR-PRIV-02 and the runtime email-wildcard case reserved for Proof R1 |
| §4 PDPA row O-PRIV-01 | A3-PRIV-D2 | Item text "unescaped wildcards → whole-database lookup under sudo, cross-company" is replaced by "unescaped wildcards in name or email → over-matched raw-SQL discovery (no access or company rules), followed by elevated, cross-company archive/delete". Design implication unchanged |
| REC-PRIV-24 | A3-PRIV-D5 | A2 basis is SF-PRIV-06-R1. "Pseudonymized, not anonymous" becomes "masked values keep re-identifying features; legal classification out of scope". Class MATCH (unchanged) |

### 2.3 Rule 3: A1 structural items reconciled

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-PRIV-BR1 | BR1: no lookup without a normalizable email | Holds (A2 T6). The display form is accepted (SF-04). Wildcard-only emails are normalizable (SF-01-R1) | MATCH (with note) | UNCORROBORATED | → REC-19, REC-22 |
| REC-PRIV-BR2 | BR2: database-wide; ignores company and record rules | Holds (A2 T6). Wording precision per A2-R1 §2.2 | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C03) | PR-PRIV-01 |
| REC-PRIV-BR3 | BR3: archive or delete with elevated rights | Holds (A2 T6; C07) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C07) | PR-PRIV-01 |
| REC-PRIV-BR4 | BR4: at most one delete per line | Holds per line (A2 T6) | MATCH | UNCORROBORATED | — |
| REC-PRIV-BR5 | BR5: first remediation creates one masked log; later actions update it | Holds, but the update is a snapshot overwrite, not an append (A2 T6; SF-02) | UPP (effect carried by REC-20) | UNCORROBORATED | PR-PRIV-03 |
| REC-PRIV-BR6 | BR6: system administrators only | Holds at ACL level (A2 T6) | MATCH | UNCORROBORATED | — |
| REC-PRIV-ST1 | Wizard: created → lookup → remediation → expired 24 h | Holds (C15, C17 mechanics). Re-lookup is hidden once lines exist but is still callable | MATCH | UNCORROBORATED | — |
| REC-PRIV-ST2 | Line: found ↔ toggled → unlinked (terminal) | Holds, but archive runs inside the change handler before save (SF-03) | UPP | UNCORROBORATED | PR-PRIV-05 |
| REC-PRIV-ST3 | Log: absent → created → updated per action → persists | **Negated in part:** details can be replaced and blanked by later actions and by re-lookup (A2 T6 "incomplete"; SF-02) | **CONTRADICTION** (A1 vs A2; linked REC-17, REC-20) | MISSING_REQUIRED_RUNTIME_PROOF (as C17) | PR-PRIV-03, PR-PRIV-04 |
| REC-PRIV-EX1 | Invalid email → user error before the query | Holds. Note: wildcard-only emails are not "invalid" (SF-01-R1) | MATCH (with note) | UNCORROBORATED | — |
| REC-PRIV-EX2 | Delete on an unlinked line → user error | Holds (C08) | MATCH | UNCORROBORATED | — |
| REC-PRIV-EX3 | Empty or "@-less" email in masking → error object returned | Holds. It is unreachable from the wizard and reachable by direct log creation (SF-05) | UPP (as REC-12) | MISSING_REQUIRED_RUNTIME_PROOF | PR-PRIV-06 |
| REC-PRIV-EX4 | Target changed or removed after lookup → not handled | Gap confirmed (A2 PR-PRIV-09) | UPP (as REC-29) | MISSING_REQUIRED_RUNTIME_PROOF | PR-PRIV-09 |
| REC-PRIV-EX5 | Delete blocked or cascaded by target constraints | Gap confirmed (A2 PR-PRIV-08) | UPP (as REC-28) | MISSING_REQUIRED_RUNTIME_PROOF | PR-PRIV-08 |
| REC-PRIV-EX6 (A2-derived) | (not in A1 §4) Multi-"@" raw input fails at log creation | SF-04 | UPP (as REC-22) | UNCORROBORATED | PR-PRIV-07 |
| REC-PRIV-H1 | mail: authorship, notification, follower exclusions | Holds. Messages are found by author only (SF-08 → REC-25) | MATCH | NOT_APPLICABLE | — |
| REC-PRIV-H2 | base: partners, users, registry; scope grows with installed modules; mass-mailing trace special case | Holds. The special case was re-read (`privacy_lookup_wizard.py`@3b6d52e0 L115) | MATCH | NOT_APPLICABLE | — |
| REC-PRIV-H3 | phone_validation: no edge | Holds | MATCH | NOT_APPLICABLE | — |
| REC-PRIV-G | GAP-PRIV-01..09 | Already mapped in the parent: 01 → REC-12/23, 02 → REC-28, 04 → REC-05/19, 05 → REC-14, 07 → REC-29, 08 → REC-13/22; 03, 06 and 09 carried as parent GAP items | (as mapped) | (as mapped) | — |
| REC-PRIV-X | CANDIDATE-PRIV-X1, X2 | Already folded: X1 → REC-06/07; X2 → REC-12/23 | (as mapped) | (as mapped) | — |
| REC-PRIV-CRQ1..9 | CRQ-PRIV-01..09 | CRQ-01 + A2-R1 §2.2 wording; CRQ-03 + SF-02; **CRQ-07 widened by SF-01-R1 (email branch)**; CRQ-08 + SF-04/05; the others are unchanged | CARRIED | — | — |

Privacy totals after R1 (parent 32 + 18 structural rows; the mapping and CRQ rows are not counted): MATCH 23 (parent 14 + 9), CONTRADICTION 4 (parent 3 + ST3), UPP 20 (parent 12 + 8), GAP 3. Total 50. QID lineage remains **provisional and not A3-eligible** (W1-B11 DELTA-RECHECK).

---

## 3. `utm`

### 3.1 Rule 1: Lane B label restoration

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-UTM-01 | C01 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-04 | C04 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-05 | C05 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-06 | C06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-07 | C07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UTM-08 | C08 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

### 3.2 Corrections and new items

| REC ID | Challenge | R1 correction |
|---|---|---|
| REC-UTM-19 | D-UTM-A3-01 | The runtime proof requirement is now **PR-U4R** (percent-encoded `%25`; the stored and read-back cookie must equal one literal percent sign before the lookup is judged; otherwise SETUP-INVALID). PR-U4 is kept as written. Class UPP (unchanged) |
| REC-UTM-30 (new) | D-UTM-A3-04 | **O9 (A2-R1):** the campaign identifier that free text matches on is recomputed from a **translatable** title (`utm_campaign.py`@a9b07365 L13–15, L36–42; `utm_mixin.py`@0c8be65a L94). A title edit in a second language may re-derive the identifier. Class **UPP**. Lane B UNCORROBORATED. Proof: PR-U11 (runtime), with a static basis case reserved for Proof R1. QID lineage: Q001, Q016, Q025 |
| REC-UTM-01 / REC-UTM-17 | A3 origin note | Origin of the C01/BR1 error: **Lane A U-B1** (Lane A l.64). A1 carried it into C01 and BR1, A2 corrected it, and the parent Proof decided it statically (post-Proof annotation, section 8). Class CONTRADICTION (unchanged) |

### 3.3 Rule 3: A1 structural items reconciled (BR1 is already REC-UTM-17)

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-UTM-BR2 | BR2: free text resolves existing trackers (including archived) or creates one | Holds (C03). Pattern characters can match any tracker (O2), and the variant chosen depends on order (O1) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C03) | PR-U3 via Proof PC-UTM-17a; PR-U4R |
| REC-UTM-BR3 | BR3: URL parameters → 31-day host cookies → applied at creation | Holds (C06, C07). Captured on every request, backend included (O4) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C06) | PR-U7, PR-U8 |
| REC-UTM-BR4 | BR4: salesmen get no cookie defaults unless superuser | Verified as written. The effect is broader (O4) (A2 §2b) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C08) | PR-U6 |
| REC-UTM-BR5 | BR5: seeded mediums and Referral undeletable outside uninstall | Holds (C09). They can still be archived or renamed, and the guard lapses without the external id (O5) | MATCH | UNCORROBORATED | — |
| REC-UTM-BR6 | BR6: each content record owns one source; in-use source undeletable | Holds (C15) | MATCH | UNCORROBORATED | — |
| REC-UTM-ST1 | Tracker lifecycle; "Medium: active ↔ archived. Source: no archive state" | Incomplete: **campaigns also carry an active flag** (`utm_campaign.py`@a9b07365 L12; REC re-read). Archived-name behaviour therefore applies to mediums and campaigns (A3 CH-U3) | **GAP** (A1 incomplete) | UNCORROBORATED | → REC-UTM-EX4 |
| REC-UTM-ST2 | Campaign: free stage moves from the default stage | Holds (C14). The default is the first stage by order | MATCH | UNCORROBORATED | — |
| REC-UTM-ST3 | Cookie: absent → set/replaced → expires after 31 days | Holds (C06). It is refreshed only when the value changes | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C06) | PR-U8 |
| REC-UTM-EX1 | Protected medium delete → user error; Referral → validation error | Holds (C09) | MATCH | UNCORROBORATED | — |
| REC-UTM-EX2 | Multi-record rename refused; in-use stage/source delete restricted | Holds. The refusal is a programming-level error (C15 refinement) | MATCH (with refinement) | UNCORROBORATED | — |
| REC-UTM-EX3 | Blank name after trim → unassigned-variable failure | Holds (C04) | UPP (as REC-04) | MISSING_REQUIRED_RUNTIME_PROOF | PR-U1 |
| REC-UTM-EX4 | "Database-level uniqueness violations are pre-empted by suffixing" | **Negated in part.** REC re-read (`utm_mixin.py`@0c8be65a L121–137): the generator's candidate fetch runs in the caller's context. Under the default active filter, archived names are invisible, so an exact-name create of an archived medium or campaign is left unsuffixed and reaches the constraint. Case variants are never suffixed (C01). A2 did not state the archived branch. It was first observed by the parent Proof (R2) and upheld by A3 CH-U3 | **CONTRADICTION** (A1 vs source) | UNCORROBORATED | Runtime case for the archived-name collision reserved for Proof R1 |
| REC-UTM-H1 | base/web: ACL groups, owner, post-dispatch hook | Holds | MATCH | NOT_APPLICABLE | — |
| REC-UTM-H2 | sales_team (undeclared) | Holds (C08) | UPP (as REC-08) | MISSING_REQUIRED_RUNTIME_PROOF | PR-U6 |
| REC-UTM-H3 | Downstream mixin and content-source consumers | Not enumerated (G4) | GAP (as REC-27) | NOT_APPLICABLE | — |
| REC-UTM-H4 | Frontend link tooling uses the public wrapper (per docstring; unverified) | Holds as a docstring statement. Reachability is runtime (C05) | UPP (as REC-05) | MISSING_REQUIRED_RUNTIME_PROOF | PR-U9 |
| REC-UTM-G | G1..G8 | Already mapped: G1 → REC-04, G2 → REC-10, G3 → REC-26, G4 → REC-27, G5 → REC-20, G6 → REC-08, G7 → REC-28, G8 → REC-29 | (as mapped) | (as mapped) | — |
| REC-UTM-X | §8 candidate tensions (archived reuse; company scope) | Covered by REC-03 and REC-13 | (as mapped) | (as mapped) | — |
| REC-UTM-CRQ1..9 | CRQ-UTM-01..09 | **CRQ-01 premise corrected** (case variants silently accepted; A2 §2b); CRQ-03 + escaping of pattern characters (O2); **CRQ-09 confirmed and extended** (archived protected mediums; A2 §2b); new consideration from O9: attribution keys should not derive from translatable labels (attached to CRQ-UTM-01/03, not a new CRQ) | CARRIED | — | — |

utm totals after R1 (parent 29 + REC-30 + 16 structural rows; the mapping and CRQ rows are not counted): MATCH 19 (parent 13 + 6), CONTRADICTION 4 (parent 3 + EX4), UPP 17 (parent 9 + REC-30 + 7), GAP 6 (parent 4 + ST1 + H3). Total 46.

---

## 4. `onboarding`

### 4.1 Rule 1: Lane B label restoration

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-ONBD-03 | C03 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-06 | C06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-08 | C08 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-11 | C11 (CONTRADICTION) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-13 | C13 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-15 | C15 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-ONBD-17 | C17 (GAP) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

Parent 26 items after R1: MRRP 7, UNCORROBORATED 14, NOT_APPLICABLE 5.

### 4.2 Rule 3: A1 structural items reconciled (D-ONBD-A3-1)

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-ONBD-BR1 | BR-1: a step can be linked only if it has an open callback | A2 C17 PARTIAL. REC re-read (`onboarding_onboarding_step.py`@26218646 L65–71): the constraint triggers only on writes to the step's panel link. Clearing the callback on a linked step is not re-checked, and panel-side linking is not established | **GAP** (aligned with REC-ONBD-17) | MISSING_REQUIRED_RUNTIME_PROOF (as C17) | PR-ONBD-06 |
| REC-ONBD-BR2 | BR-2: panel complete when every step is complete; just_done counts | Holds (C07). A zero-step panel is done (OM-O03), and completion is a count comparison (SF-O05) | MATCH (with REC-21 note) | UNCORROBORATED | — |
| REC-ONBD-BR3 | BR-3: validation one-way and idempotent | Holds (C04, C05) | MATCH | UNCORROBORATED | — |
| REC-ONBD-BR4 | BR-4: just_done shown once, then made done by the render read | Holds (C06, C08). Consumption crosses panels and companies (OM-O02) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C06) | PR-ONBD-01, PR-ONBD-02 |
| REC-ONBD-BR5 | BR-5: "Scope is sticky. Once per-company, a panel stays per-company." A scope change deletes progress | **Negated (first sentence).** REC re-read (`onboarding_onboarding.py`@9ed728d6 L22–24, L45–54): the flag is a live, non-stored compute that is true only while a company-bearing tracker or a per-company step exists. The source comment's "sticky" intent holds only through a company tracker. Second sentence holds (C12) | **CONTRADICTION** (linked REC-ONBD-11; both texts preserved) | MISSING_REQUIRED_RUNTIME_PROOF (as C11) | PR-ONBD-04 |
| REC-ONBD-BR6 | BR-6: adding a step re-opens completion; close/hide is per tracker | Holds (C09, C10). The scope rebuild discards the closed flag (OM-O07), and close without a tracker is lost (OM-O09) | MATCH (notes → REC-25, REC-26) | UNCORROBORATED | — |
| REC-ONBD-BR7 | BR-7: only the system group has model access | Holds (C15) | UPP (as REC-15) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-03 |
| REC-ONBD-ST1 | Step: not_done → just_done → done; no reverse; deletion resets | Holds (C04, C06, C12) | MATCH | UNCORROBORATED | — |
| REC-ONBD-ST2 | Stored panel state not_done ↔ done | Holds (C07, C09). The closed flag is untouched | MATCH | UNCORROBORATED | — |
| REC-ONBD-ST3 | Rendered panel state not_done \| just_done \| done \| closed | Imprecise: a not-done, not-closed panel carries **no** panel-state key in the render output, rather than a not_done value (A2 C07 refinement) | **GAP** (A1 imprecise) | UNCORROBORATED | — |
| REC-ONBD-ST4 | Panel visibility open ↔ closed per tracker | Holds (C10) | MATCH | UNCORROBORATED | — |
| REC-ONBD-ST5 | "Panel scope: global → per-company (one way)" | **Negated** (as BR-5) | **CONTRADICTION** (linked REC-ONBD-11) | MISSING_REQUIRED_RUNTIME_PROOF (as C11) | PR-ONBD-04 |
| REC-ONBD-EX1 | Linking a step without a callback → validation error | Holds only in the narrow form (C17 PARTIAL) | GAP (as BR-1) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-06 |
| REC-ONBD-EX2 | Concurrent first creation → uncaught uniqueness violation | Holds (C03) | UPP (as REC-03) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-10 |
| REC-ONBD-EX3 | Missing external reference → quiet no-op / "not found" | Holds (C05, C10) | MATCH | UNCORROBORATED | — |
| REC-ONBD-EX4 | Internal user without elevation → access error on every operation | Holds (C15) | UPP (as REC-15) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-03 |
| REC-ONBD-EX5 | Render uses up just_done on a closed or duplicate render | Holds (C06, C08) | UPP | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-01 |
| REC-ONBD-EX6 (A2-derived) | (not in A1 §4) Render before any tracker → single-record assertion | OM-O01 | GAP (as REC-19) | UNCORROBORATED | PR-ONBD-09 |
| REC-ONBD-H1 | web: assets and generic RPC dispatch | Holds | MATCH | NOT_APPLICABLE | — |
| REC-ONBD-H2 | base: menu parent, images, company cascade | Holds (C18) | MATCH | NOT_APPLICABLE | — |
| REC-ONBD-H3 | Consumer apps own panels, callbacks, the render route and any elevation | Route owner **not found**. Re-derived: `account` and `payment` declare a manifest dependency on `onboarding` (`account/__manifest__.py`@f3e264e5 L17, with onboarding data at L25; `payment/__manifest__.py`@93c02fd0 L8). The parent Proof (PC-ONBD-15) and A3 (A3-ONBD-03) found no onboarding controller in bounded searches | **GAP** (route owner INCONCLUSIVE; GAP-1) | NOT_APPLICABLE | PR-ONBD-08; bounded static re-check reserved for Proof R1 |
| REC-ONBD-H4 | mail: tests only, not a manifest dependency | REC re-read: the manifest depends on `web` only (`__manifest__.py`@eaa50cca L13), and a test imports a mail test helper (`tests/test_onboarding.py`@32649804 L9) | MATCH | NOT_APPLICABLE | — |
| REC-ONBD-G1 | GAP-1: route owner | As H3 | GAP | NOT_APPLICABLE | as H3 |
| REC-ONBD-G2 | GAP-2: JS inventory not enumerated | Open | GAP | NOT_APPLICABLE | — |
| REC-ONBD-G3 | GAP-3: consumer elevation | Open (C15) | UPP (as REC-15) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-03 |
| REC-ONBD-G4 | GAP-4: co-existing global and company trackers | Open (C13) | UPP (as REC-13) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-07 |
| REC-ONBD-G5 | GAP-5: transaction behaviour of the render write | Open (C06) | UPP (as REC-06) | MISSING_REQUIRED_RUNTIME_PROOF | PR-ONBD-01 |
| REC-ONBD-X1 | CONTRADICTION-ONBD-1 (route documented, no controller) | Confirmed within the module (REC-16) | MATCH (as REC-16) | NOT_APPLICABLE | — |
| REC-ONBD-CRQ1..7 | CRQ-ONBD-1..7 | CRQ-1 + OM-O02; CRQ-2 + OM-O07; CRQ-6 + OM-O04 (parent §7); the others are unchanged | CARRIED | — | — |

Onboarding totals after R1 (parent 26 + 28 structural rows; the CRQ row is not counted): MATCH 22 (parent 11 + 11), CONTRADICTION 3 (REC-11, BR5, ST5), UPP 13 (parent 5 + 8), GAP 16 (parent 9 + 7). Total 54. Several structural rows repeat an existing item's class ("as REC-nn"), so MASTER should consume per-row classes.

---

## 5. `html_builder`

### 5.1 Rule 1

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-HBLD-06 | C06 | UNCORROBORATED (MRRP kept only through the UPP class) | **MISSING_REQUIRED_RUNTIME_PROOF** (shown explicitly) |

### 5.2 Rule 4 and the scope note

- **REC-HBLD-08:** the proof-link cell "(PC-HBLD-07)" is tagged **`POST-PROOF ANNOTATION`**. It was not a REC input. The class (GAP) was set on A1 C08 versus A2 PARTIAL alone and is unchanged.
- **REC edit record:** the parent REC was committed first as sha256 `0fd609ab…` (commit `b31a0e8`, 15:15:22Z) and then as `d6efb05e…` (commit `37823e6`, 15:16:10Z). A3 describes the change as a one-line correction of a freeze-hash abbreviation. No change record existed until now. The governing parent REC for consumption is `d6efb05e3e3893dce981084d0f2a93cefa42b017cdb1a407677f5aa3d51b9803`, frozen here. This REC stage did not independently diff the two commits, because this remediation runs no git operations.
- **Scope note on REC-HBLD-02 (A3 D-HBLD-A3-4, A1 advisory recorded at REC level; A1 is not edited):** "Assets-only" describes this module's own code: an empty package init and no `data` key (`__manifest__.py`@f55fb070; `__init__.py`@e69de29b 0 bytes). It does **not** mean "no server surface when installed". The hard dependencies `mail` and `html_editor` (L21) bring their server surfaces with installation. The class stays MATCH.

### 5.3 Rule 3: A1 structural items reconciled (D-HBLD-A3-2)

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-HBLD-BR1 | BR-1: no server-side business rules; all behaviour is client-side | Holds for module code (C02, C09). Scope note in 5.2 | MATCH | NOT_APPLICABLE | — |
| REC-HBLD-BR2 | BR-2: edit-only styling must not ship in the shell bundle; enforced by a test | Holds, with a **limitation**. REC re-read: the removal rules cover every edit-pattern file and dark SCSS (`__manifest__.py` L38–39), but the test asserts only the absence of the edit-SCSS suffix (`tests/test_html_builder_assets_bundle.py`@7792507b L16–19) and is post-install only (L8) | UPP (limitation REC-HBLD-11 attached) | MISSING_REQUIRED_RUNTIME_PROOF (as C06) | PR-HBLD-01 |
| REC-HBLD-ST1 | No server-side states | Holds (C02) | MATCH | NOT_APPLICABLE | — |
| REC-HBLD-EX1 | "A mis-globbed asset that leaks edit styling would be caught only by the bundle test" | Incomplete: only a leaked edit-**SCSS** file would be caught. A leaked edit JS/XML or dark SCSS file would not be caught by any server-side guard (OM-H02) | **GAP** (linked REC-HBLD-11) | NOT_APPLICABLE | PR-HBLD-01 |
| REC-HBLD-H1 | Outbound: html_editor, web, mail (client helper only), base | Holds (C04, C05). Mail-helper coupling: parent Proof PC-HBLD-06 is INCONCLUSIVE (post-Proof annotation) | MATCH (mail-only-for-helper stays unproven: REC-HBLD-04 note) | NOT_APPLICABLE | PR-HBLD-04 |
| REC-HBLD-H2 | Inbound (declared intent): website builder, mass-mailing editor | Not verified from consumer manifests (GAP-3) | GAP | NOT_APPLICABLE | — |
| REC-HBLD-H3 | Save paths, RPC and access control belong to other modules | Holds as scope. Authorization is cross-module (CRQ-HBLD-2) and is routed to the html_editor, website and mass_mailing proofs | GAP (cross-module) | NOT_APPLICABLE | PR-HBLD-03 |
| REC-HBLD-G1 | GAP-1: client JS/XML behaviour not analysed | Open | GAP | NOT_APPLICABLE | — |
| REC-HBLD-G2 | GAP-2: static inventory is a lower bound | Open (REC-08) | GAP (as REC-08) | NOT_APPLICABLE | — |
| REC-HBLD-G3 | GAP-3: inbound consumers unconfirmed | Open (as H2) | GAP | NOT_APPLICABLE | — |
| REC-HBLD-X | §8: no contradictions | Holds | MATCH | NOT_APPLICABLE | — |
| REC-HBLD-CRQ1..3 | CRQ-HBLD-1..3 | CRQ-3 + OM-H02 (guard narrower than removal rules); CRQ-2 routed cross-module | CARRIED | — | — |

html_builder totals after R1 (parent 13 + 11 structural rows): MATCH 11, CONTRADICTION 0, UPP 2, GAP 11. Total 24.

---

## 6. `web_hierarchy`

### 6.1 Rule 1

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-WHIR-10 | C10 (GAP) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-WHIR-11 | C11 (UPP) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

### 6.2 Rule 3: A1 structural items reconciled (D-WHIR-A3-2)

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-WHIR-BR1 | BR-1: allow-listed root attributes, field children, one templates block | Holds (C04). Names only, not values (OM-W05) | MATCH | UNCORROBORATED | — |
| REC-WHIR-BR2 | BR-2: parent relation optional at server validation | Holds (C05) | MATCH | UNCORROBORATED | — |
| REC-WHIR-BR3 | BR-3: focused read one level; multi-match returned as is | Holds (C07). No bound (OM-W01), and a self-parent duplicate is possible (OM-W03) | MATCH (notes → REC-13, REC-14) | UNCORROBORATED | — |
| REC-WHIR-BR4 | BR-4: "All reads are limited to the caller's own access rights" | **Caveat required** (A2 C10 PARTIAL). REC re-read (`models/models.py`@88136e7d L13, L19–22, L29–36): searches and the grouped read run under the caller's rights, so siblings and children can drop silently. The parent is added by following the relation, not by a rule-filtered search, and is then read in the caller's environment, so an unreadable parent most likely fails the whole call (inference; framework read not read) | **GAP** (linked REC-WHIR-10) | MISSING_REQUIRED_RUNTIME_PROOF (as C10) | PR-WHIR-02 |
| REC-WHIR-ST1 | Stateless; uninstall removes view lines of this mode | Holds (C02) | MATCH | NOT_APPLICABLE | — |
| REC-WHIR-EX1 | Disallowed attribute, child or second templates block → view error | Holds (C04). Skipped when not validating | MATCH | UNCORROBORATED | — |
| REC-WHIR-EX2 | Invalid parent-field name fails in the ORM | Holds (C06) | MATCH | UNCORROBORATED | — |
| REC-WHIR-EX3 | Empty search → empty list | Holds (C07) | MATCH | UNCORROBORATED | — |
| REC-WHIR-EX4 | "Silent truncation by access rights" | Partial: silent for siblings, children and child-id lists, but likely a hard error for an unreadable parent (C10 PARTIAL) | **GAP** (linked REC-WHIR-10) | MISSING_REQUIRED_RUNTIME_PROOF | PR-WHIR-02 |
| REC-WHIR-H1 | web: assets and RPC dispatch | Holds as source. Reachability is runtime (C11) | UPP (as REC-11) | MISSING_REQUIRED_RUNTIME_PROOF | PR-WHIR-07 |
| REC-WHIR-H2 | Core: action view lines, UI view model, abstract base | Holds (C02, C03, C06) | MATCH | NOT_APPLICABLE | — |
| REC-WHIR-H3 | Target models own parent integrity and cycle prevention | Holds. The server does one expansion and cannot loop (C09; A3-WHIR-04) | MATCH | NOT_APPLICABLE | — |
| REC-WHIR-H4 | Downstream consumers not enumerated | Open | GAP | NOT_APPLICABLE | — |
| REC-WHIR-G1..G3 | GAP-1 static inventory; GAP-2 client enforcement and cycles; GAP-3 consumer reliance on server validation | Open | GAP (3 items) | NOT_APPLICABLE | — |
| REC-WHIR-X | REFINEMENT-WHIR-1 | Confirmed (REC-07) | MATCH (as REC-07) | UNCORROBORATED | — |
| REC-WHIR-CRQ1..5 (+6) | CRQ-WHIR-1..5; A2-proposed result-bounding CRQ | **CRQ-3 split** (silent for children versus hard failure for the parent); **CRQ-WHIR-6 (A2 candidate): bound multi-record hierarchy reads** (OM-W01) | CARRIED | — | — |

web_hierarchy totals after R1 (parent 17 + 17 structural rows, with G1..G3 counted as 3): MATCH 20, CONTRADICTION 0, UPP 2, GAP 12. Total 34.

---

## 7. `web_unsplash`

### 7.1 Rule 1

| REC ID | Claim | Parent Lane B | **R1 Lane B** |
|---|---|---|---|
| REC-UNSP-04 | C04 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-06 | C06 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-07 | C07 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-09 | C09 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-10 | C10 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-11 | C11 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-12 | C12 (GAP) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-15 | C15 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| REC-UNSP-17 | C17 | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |

### 7.2 Rule 3: A1 structural items reconciled (D-UNSP-A3-2)

REC re-read `controllers/main.py`@00cf725f for the rows below.

| REC ID | A1 item | A2 position (source) | REC class | Lane B | Proof link |
|---|---|---|---|---|---|
| REC-UNSP-BR1 | BR-1: search needs key and app id; error code depends on role | Holds (C07). Both values are required although only the key is sent (OM-U05) | UPP (as REC-07) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-03 |
| REC-UNSP-BR2 | BR-2: images from allow-listed hosts by prefix, with a resolution check | Holds as construction (C08). The prefix is checked on the submitted string only, redirects are not re-checked (C09), and the check is bypassed under the current-test marker (C10) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C09) | PR-UNSP-04, PR-UNSP-05 |
| REC-UNSP-BR3 | BR-3: attachment ownership follows the caller's access; default target is the view model | Holds (C13). Any caller-supplied target model is accepted, subject to the helper's check (OM-U06) | MATCH | UNCORROBORATED | — |
| REC-UNSP-BR4 | BR-4: only access-rights admins and website restricted editors can set credentials | Holds (C06). Behaviour with a missing website group is unverified (OM-U07) | UPP (as REC-06) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-02 |
| REC-UNSP-BR5 | BR-5: "Every download triggers a best-effort notification to the provider, **as its API terms require**" | **Reclassified.** (a) **Mechanics, narrower than stated.** Notification is sent once per item that reached attachment creation (L126 after L90 `continue` on non-OK). The download URL is caller-supplied and only prefix-checked unless the test marker is set (L34; CONTRADICTION-UNSP-1). Items after an aborting item are not processed (C12). So it is not "every download". (b) **"As its API terms require" is a claim about the real provider.** Its only source basis is an in-code docstring/comment ("API requirement", L26, L125). It is **not source-provable**, and no local-mock case can settle it | **GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE** (part b). Part (a) is linked to REC-UNSP-16 and REC-UNSP-12. MASTER must not consume part (b) as fact | UNCORROBORATED (a) / NOT_APPLICABLE (b) | None can settle (b). (a) → PR-UNSP-07, PR-UNSP-13 |
| REC-UNSP-BR6 | BR-6: save-back resolves from local attachments (same record or public) | Holds (C17) | UPP (as REC-17) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-10 |
| REC-UNSP-ST1 | Configuration: unconfigured → configured; "no validation and no revocation state" | "No validation" holds. **"No revocation state" conflicts with REC-UNSP-21.** The save route writes both values exactly as received, including absent ones (L152–157). If the parameter store removes a parameter on an absent value, an empty save acts as revocation (framework semantics not read) | **UPP** (linked REC-UNSP-21) | UNCORROBORATED | PR-UNSP-12; static framework read reserved for Proof R1 |
| REC-UNSP-ST2 | Per item: submitted → (URL rejected: abort) \| (fetch fails: skipped) \| created → URL override → token → notified | Incomplete: image-processing failure and a missing URL also abort the whole request (A2 C12 PARTIAL; L80–101). Notifications already sent for earlier items are not undone (OM-U03) | **GAP** (linked REC-UNSP-12, REC-UNSP-22) | MISSING_REQUIRED_RUNTIME_PROOF (as C12) | PR-UNSP-07 |
| REC-UNSP-EX1 | URL outside the allow-list aborts the request | Holds but incomplete (C12 PARTIAL) | GAP (as REC-12) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-07 |
| REC-UNSP-EX2 | Non-OK, connection and timeout failures skipped or logged | Holds (C08). No explicit timeout is set (C11) | MATCH | UNCORROBORATED | — |
| REC-UNSP-EX3 | Target access denied → access error | Holds (C13; module test) | MATCH | UNCORROBORATED | — |
| REC-UNSP-EX4 | Non-manager save → not-found | Holds (C06) | UPP (as REC-06) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-02 |
| REC-UNSP-EX5 | Missing or failed configuration → role-dependent codes; status only to managers | Holds (C07). A search connection failure is uncaught and surfaces as an RPC error (OM-U01) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C07) | PR-UNSP-03, PR-UNSP-11 |
| REC-UNSP-EX6 | Notification never raised; save-back with no match → empty | Notification holds (C16, MATCH). Save-back holds (C17) | UPP (save-back part) | MISSING_REQUIRED_RUNTIME_PROOF (as C17) | PR-UNSP-10 |
| REC-UNSP-H1 | html_editor attachment helper (access inherited) and media assets | Holds. The helper internals were not read (GAP-2) | MATCH (bounded) | NOT_APPLICABLE | — |
| REC-UNSP-H2 | base_setup settings view and toggle | Holds (C18). base_setup was not read (GAP-3) | MATCH (bounded) | NOT_APPLICABLE | — |
| REC-UNSP-H3 | website soft reference (restricted-editor group, beacon bundle) | Holds (C04, C06). Missing-group behaviour is unverified (OM-U07) | UPP | MISSING_REQUIRED_RUNTIME_PROOF (as C06) | PR-UNSP-02 |
| REC-UNSP-H4 | Core: attachment serving-protection bypass, parameters, image converter, users | Holds (C14, C17) | UPP (C17 part) | MISSING_REQUIRED_RUNTIME_PROOF (as C17) | PR-UNSP-10 |
| REC-UNSP-H5 | External: provider search API, image CDN hosts, notify endpoint, browser views endpoint | Provider-side behaviour is **outside source and outside the mock design**. Module behaviour against these endpoints is testable only against a local mock (non-substitution: the Proof addendum records the limit) | GAP (provider side) | NOT_APPLICABLE | — |
| REC-UNSP-G1 | GAP-1: JS and tests not enumerable | Open | GAP | NOT_APPLICABLE | — |
| REC-UNSP-G2 | GAP-2: editor helper and serving-protection internals unread | Open | GAP | NOT_APPLICABLE | — |
| REC-UNSP-G3 | GAP-3: base_setup toggle and placeholder unread | Open | GAP | NOT_APPLICABLE | — |
| REC-UNSP-G4 | GAP-4: rollback of earlier items | Open. Runtime against the mock | UPP (as REC-12) | MISSING_REQUIRED_RUNTIME_PROOF | PR-UNSP-07 |
| REC-UNSP-G5 | GAP-5: how the real provider hosts redirect (decides C09 exploitability) | **Provider-side. Not closable by any mock case.** The mock result shows only that the module follows a redirect | GAP — PROVIDER CLAIM, NOT SOURCE-PROVABLE | NOT_APPLICABLE | None in the pack |
| REC-UNSP-G6 | GAP-6: other paths creating colliding public attachments | Open | GAP | NOT_APPLICABLE | — |
| REC-UNSP-X1 | CONTRADICTION-UNSP-1 (docstring implies a trusted value; the value is caller-supplied) | Confirmed (REC-16) | MATCH (as REC-16; source-internal contradiction confirmed by A1 and A2) | UNCORROBORATED | PR-UNSP-13 |
| REC-UNSP-X2 | REFINEMENT-UNSP-1 (notify allow-list also bypassed in test mode) | Confirmed (C10) | MATCH | UNCORROBORATED | — |
| REC-UNSP-CRQ1..9 (+10, 11) | CRQ-UNSP-1..9; A2-proposed CRQs for OM-U01 and OM-U02 | CRQ-9 covers all abort causes (A2). **CRQ-UNSP-10 (A2 candidate): no credential in URLs, logs or error text.** **CRQ-UNSP-11 (A2 candidate): credential clearing must be explicit, validated and audited** | CARRIED | — | — |

web_unsplash totals after R1 (parent 26 + 27 structural rows; the CRQ row is not counted): MATCH 16 (parent 9 + 7), CONTRADICTION 0, UPP 19 (parent 8 + 11), GAP 18 (parent 9 + 9, including 2 marked PROVIDER CLAIM: BR5 and G5). Total 53.

---

## 8. Rule 4: post-Proof citations in parent RECs, annotated

The parent RECs of all seven modules were written in a combined REC + Proof run. They cite Proof results that were not REC inputs. Each such citation is annotated **`POST-PROOF ANNOTATION`** here. The classes were set on A1/A2 inputs, and none changes because of these annotations.

| Parent REC | Citations annotated POST-PROOF |
|---|---|
| phone_validation | §2 "Proof link" column static PCs (PC-11..PC-26); REC-21 basis "(Proof R1)" (now superseded by A2-R1); REC-24 basis "post-hoc proposal in Proof §6"; §6 "static proof results from Stage 2" |
| privacy_lookup | §2 "Proof link" static PCs (PC-10..PC-22); REC-19 "also via email (Proof R1)" (now superseded by A2-R1); REC-22 "harness shows…"; §6 "static proof results from Stage 2" |
| utm | REC-01 "PR-U2 is decided statically in Proof (PC-UTM-01)"; REC-08 "Proof decided the static part (PC-08)"; §2.2 PC citations; §5 "Stage 2 static results" |
| onboarding, web_hierarchy, web_unsplash | "Proof link" column entries cite A2 PR ids only (not PC results). Their REC files cite `laneb_search.txt`, which was written after Proof fetch began (A3 rule-4 evidence). The Lane B conclusion (none exists) does not depend on Proof |
| html_builder | REC-HBLD-08 "(PC-HBLD-07)" (section 5.2) |

**Freeze record:** the parent REC sha256 values in section 0 are the hashes that this REC stage freezes for rule 4. The Proof addendum header records them, together with this addendum's sha256, as the REC input consumed.

---

## 9. Process-rule compliance (C1B systemic findings 1–5)

| # | Rule | Status | Evidence |
|---|---|---|---|
| 1 | Preserve A2 MRRP labels | **MET (restored)**. 45 REC items restored across the seven modules: phone 10, privacy 9, utm 7, onboarding 7 (including the named C11 and C17), html_builder 1 (C06, now explicit), web_hierarchy 2 (including the named C10), web_unsplash 9 (including the named C12). New structural rows carry the label of the claim they inherit | Sections 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1 |
| 2 | Tag post-predeclaration text | **MET / N-A**. This addendum was frozen before the Proof R1 predeclaration. Post-Proof citations in the parents are tagged `POST-PROOF ANNOTATION` | Section 8 |
| 3 | REC scans all A1 item classes (BR, states, exceptions, X, H, gaps, CRQ) | **MET**. Every A1 §2–§8 item of the seven modules has a row or an explicit mapping row. Business rules and states that had been skipped are reconciled, including onboarding BR-5 and the scope state line (CONTRADICTION), onboarding BR-1 (GAP), web_hierarchy BR-4 (GAP with caveat), web_unsplash BR-5 (reclassified), its state lines, html_builder BR-2 (limitation) and utm EX4 (CONTRADICTION) | Sections 1.4, 2.3, 3.3, 4.2, 5.3, 6.2, 7.2 |
| 4 | REC frozen (sha256) before Proof; Proof records it | **MET**. Parent REC hashes are frozen in section 0. This addendum's sha256 is written to `remed_b3c/rec_addendum.sha256` before the Proof R1 predeclaration, and the Proof addendum header records it | Proof addendum header |
| 5 | Cases hashed and UTC-stamped before the first Proof source fetch | **N-A for REC**. REC read only the A2-stage copies and fetched no source | — |

## 10. Limitations

- Counts are given per module for orientation only. Where a structural row maps "as REC-nn", it duplicates an existing item, and MASTER should consume per-row classes. The counts are not coverage measures. No percentages. No Formal Coverage claim.
- No runtime evidence exists. All UPP items stay open until runtime proof. PROVIDER-CLAIM items (web_unsplash BR-5(b), G5) cannot be closed by the planned mock runtime.
- privacy QID lineage stays provisional (W1-B11). onboarding and html_builder MVQ lineage stays on HOLD. web_hierarchy and web_unsplash have no bank.
- Callers outside the modules (SMS, marketing, portal controller, consumer apps of onboarding and html_builder) are not read by REC.
