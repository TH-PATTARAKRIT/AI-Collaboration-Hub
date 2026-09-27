# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum R1 (A3 remediation, batch B3A) — `auth_signup`, `base_setup`, `base`, `portal`, `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. This is an addendum only. No parent REC or earlier REC addendum was edited |
| Group / Modules | G01 PLATFORM_BASE / `auth_signup`, `base_setup`, `base`, `portal`, `base_automation` |
| Date | 2026-09-27 (written after the A2 addendum froze at 15:43:10 UTC and before any Proof predeclaration of this batch) |
| Stage order position | **Second** artifact. Consumes the A2 addendum below. Its own sha256 is recorded in scratch (`remed_b3a/rec_addendum.sha256`) and must be quoted in the Proof addendum header **before** Proof predeclares (MASTER C1-B rule 4). This addendum cites **no** Proof result of this batch; none existed when it was written |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 Parent artifacts and inputs (sha256)

Paths relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Artifact | sha256 |
|---|---|
| Parent REC `G01_RECONCILIATION/G01_AUTH_SIGNUP_REC_20260927.md` | `18d7b4ef959f9de14f5e4d14112eefd925a7808239117712a9f759dba25dd4f6` |
| Parent REC `G01_RECONCILIATION/G01_BASE_SETUP_REC_20260927.md` | `05e752c04a10c3a5fbf9d8977c8683b627110c0be3db6de925176f7ac0adb06a` |
| Parent REC `G01_RECONCILIATION/G01_BASE_REC_20260927.md` | `c343d43408c57b7e6cc75a3b9d5edf85737281dc9e5bda71a732762a567b833c` |
| Parent REC `G01_RECONCILIATION/G01_PORTAL_REC_20260927.md` | `abb7e72d2af65878915c93d64529f89f996500726986861b51836af90f7c9d84` |
| Parent REC `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_20260927.md` | `6f4471f430863392e757f99fc3a818cf60a0820350a724fa3720b1f2a39ed0ab` |
| Parent REC addendum `G01_RECONCILIATION/G01_BASE_AUTOMATION_REC_ADDENDUM_R1_20260927.md` | `05cd7a32a86ec23144529462fc491ea8456c4182eddf299d818d87b8795eb172` |
| **A2 input** `G01_A2_REVIEWS/G01_B3A_A2_ADDENDUM_R1_20260927.md` (frozen 15:43:10 UTC) | `26d828ce29c78dd5e8da310f93322a2a3d4e1e8debc2cf4617eb403fa86a0c8c` |
| Parent A2 reviews (label source for rule 1): auth_signup `e5ce1b56…28f9`; base_setup `9e913ee7…1a31`; base `05e42224…00c1`; portal `695171c7…6ec0`; base_automation `bf95295f…4208` and addendum R1 `be0cf294…5c0a` | full values in the A2 addendum §0.1 |
| A1 packages (scanned for rule 3): auth_signup `da32ca50…fe69e`; base_setup `3e37b467…0970`; base `a45a2bef…89e7`; portal `aef33889…957d`; base_automation `f01dec29…7007` | full values in scratch `remed_b3a/intake.sha256` |
| Question banks (topics only; hashes as recorded in each parent REC and unchanged) | auth_signup `bf215a34…e9e2`; base_setup `21611846…6d62`; base `b242fa0e…8777`; portal `91b63eef…3d3a`; base_automation `3c38cec4…9a49` |

### 0.2 A3 reports and challenge IDs addressed (REC part)

| A3 report | sha256 | IDs |
|---|---|---|
| `G01_A3_CHALLENGES/G01_AUTH_SIGNUP_A3_STATIC_20260927.md` | `44eddb06aca5f049181dc083db8b2b8f3c8092428c9573c4054357601b5db48e` | CH-06 (REC-28 basis), CH-08 (REC-18 links), CH-12 / D-ASGN-A3-03, CH-14 / D-ASGN-A3-05 |
| `G01_A3_CHALLENGES/G01_BASE_SETUP_A3_STATIC_20260927.md` | `673c4f572f5f96bda52672339efcf22d0d067ce3321ef6f8b32c2e41e308bd17` | CH-02 / D-BSET-A3-01 (REC-26 basis), CH-04 (REC-12), CH-12-equivalent stage-mixing (shared REC run) |
| `G01_A3_CHALLENGES/G01_BASE_A3_STATIC_20260927.md` | `79f442833b0a838524ad8d0f957436b307c7908e8d8468e70a31c20318cd5f01` | D4 ("consider carrying O3 as a REC item" in base_automation) |
| `G01_A3_CHALLENGES/G01_PORTAL_A3_STATIC_20260927.md` | `3ecf4c6ba5dd07949f9d4b1d6074a2f3f46dfe5f28e303ee9fe9d9657d36d370` | CH-P2 (REC-21 basis), CH-P7 (REC-22 link), CH-P10 (REC–Proof coupling) |
| `G01_A3_CHALLENGES/G01_BASE_AUTOMATION_A3_RECHECK_R1_20260927.md` | `f8868ca59b03e6ca41dd4481ef34e653676af53251b1757ef3cecfc56b99eefe` | RD-1, RD-2, RD-3 (bases), RD-5 (REC part), RD-6 |

Clean-room note: neutral paraphrase only; identifiers are pointers. No vendor code. No percentages. No Formal Coverage claim. No QID is answered; every QID mapping is lineage only. No git operations. No existing artifact was edited. REC did not fetch source in this addendum; the only source reads are the A2 stage's, cited through the A2 addendum.

### 0.3 MASTER C1-B process-rule compliance (this addendum)

| Rule | Compliance | Evidence |
|---|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` | **MET**. Section 1 restores the A2 label as its own column, beside the unchanged Lane B column, for every REC item in the five modules whose A2 claim or omission carries the label or a runtime proof requirement | Section 1 |
| 2. Post-declaration tagging | **NOT APPLICABLE** (REC predeclares no cases). REC changes are all labelled "basis addendum", "class change" or "new item" | Sections 2–3 |
| 3. Scan all A1 item classes for "no evidence" QIDs | **MET**. Each "no evidence yet" QID of the five modules was checked against A1 claims, business rules, states, exceptions, cross-module handoffs, gaps, CRQs and contradictions, and against A2 omissions including this batch | Section 4 |
| 4. REC frozen and hashed before Proof executes; Proof records the REC hash | **MET for this addendum** (hash recorded in scratch at freeze, before the Proof predeclaration). Parent RECs remain non-compliant historically; section 5 records their Proof-independence | Header; section 5 |
| 5. Cases sha256 + UTC before first Proof fetch | **NOT APPLICABLE** (Proof duty) | — |

---

## 1. Rule 1 — A2 `MISSING_REQUIRED_RUNTIME_PROOF` labels restored

The parent RECs kept only a Lane B column (UNCORROBORATED / NOT_APPLICABLE). Where A2 had labelled a claim MISSING_REQUIRED_RUNTIME_PROOF, or placed it under a proof-requirement table headed with that label, the label was lost. It is restored here as a **separate column "A2 proof label"**. The Lane B column is not changed; absence of Lane B remains non-failing. REC classes are not changed by this section.

| Module | REC items now carrying A2 label **MISSING_REQUIRED_RUNTIME_PROOF** (A2 source of the label) |
|---|---|
| auth_signup (A2 §7 heading covers every PR claim) | REC-ASGN-03 (C03; PR-01), -04 (C04; PR-02), -05 (C05; PR-05), -07 (C07/F5; PR-06), -08 (C08; PR-08), -11 (C11; PR-03), -12 (C12; PR-04), -16 (C16; PR-12), -18 (C18-R1; PR-14/15, A2 addendum §6), -19 (C19; PR-09), -20 (C20; PR-10), -21 (C21; PR-11), -25 (O1/F1; PR-01), -26 (O2/F2; PR-05), -27 (O3/F3; PR-07), -28 (O4-R1; PR-13, A2 addendum §6), -29 (O5/F8; PR-09), -30 (O6/F6; PR-08), -31 (O8; label carried from base_setup PR-BSET-07), -32 (O7/F7; PR-03), -33 (O9/G9; PR-10). **21 items** |
| base_setup (A2 §7 heading) | REC-BSET-03 (C03; PR-10), -05 (C05; PR-11), -07 (C07/F3; PR-07), -11 (C11/F2; PR-05), -12 (C12; PR-06R1, A2 addendum §6), -14 (C14/F5; PR-03), -15 (C15/F1-R1; PR-01, PR-12), -16 (C16/F6; PR-09), -17 (C17; PR-09), -24 (O1/F3; PR-07), -25 (O2; PR-07), -26 (O3-R1; PR-01, PR-02, PR-12), -27 (O4; PR-09), -28 (O5/F5; PR-03, PR-04), -29 (O6/F4; PR-08), -30 (O7/F2; PR-05). **16 items** |
| base (A2 §7 table) | REC-BASE-04 (C04), -06 (C06), -07 (C07), -10 (C10), -11 (C11), -12 (C12), -20 (C20), -24 (C24), -26 (C26), -27 (C27), -28 (C28), -29 (C29), -30 (C30), -31 (C31). **14 items**. REC-BASE-04's basis already quoted the label; the other 13 had lost it. Five of these (26–29, 31) are CONTRADICTION items: the label now shows that their runtime effect is a required proof, not an optional corroboration |
| portal (A2 §5 table + A2 addendum §6) | REC-PRTL-01 (C01), -04 (C04), -05 (C05), -07 (C07), -09 (C09), -16 (C16), -21 (O2-R1), -22 (O3 / PR-P5R1). **8 items**. REC-PRTL-10 (C10) keeps A2's UNCORROBORATED label although PR-P6 exists, because A2 labelled it so; REC does not upgrade an A2 label |
| base_automation (A2 §5 table + A2 addenda) | REC-BAUT-06 (C06), -09 (C09), -11 (C11), -12 (C12), -14 (C14), -18 (C18), -19 (C19), -20 (C20), -24 (C24), -27 (O3-R2), -38 (O14-R2), -47 (O18-R1; label assigned by A2 addendum B3A §6, closing RD-6 part 1), -48 (O19, new in section 3.5). **13 items** |

Label totals do not replace class counts. Every restored item keeps its parent class.

---

## 2. Stage-separation statement for the parent RECs (A3 auth_signup CH-12 / D-ASGN-A3-03; portal CH-P10; base_setup shared run; base_automation RD-5)

**Finding accepted.** The parent RECs for auth_signup, base_setup, portal and base were written in the same run as, and finalised after, their static Proof cases. Their "Basis for class" cells cite PC results and their limitations say Stage-2 results were used for classification support.

**Re-derivation using only A1 and A2 (every PC citation ignored).** For each module the parent classification rules were re-applied to the A1 claim and the A2 verdict or omission alone:

| Class | Derivation without Proof | auth_signup | base_setup | base | portal |
|---|---|---|---|---|---|
| MATCH | A2 VERIFIED from A2's own source re-read, and no A2 runtime label on the claim | reproduced (11) | reproduced (13 → 12 after the class change in 3.2, which rests on the A2 addendum, not on Proof) | reproduced (23) | reproduced (13) |
| CONTRADICTION | A2 PARTIAL / NOT_VERIFIED, or an A2 source finding against declared intent | reproduced (5) | reproduced (5) | reproduced (7) | reproduced (4) |
| UNKNOWN_PENDING_PROOF | A2 runtime label or proof requirement, or an A2 omission predicted statically | reproduced (17) | reproduced (12 → 13) | reproduced (20) | reproduced (10) |
| GAP | A1/A2 gaps nothing in scope closes | reproduced (3) | reproduced (4) | reproduced (4) | reproduced (6) |

Conclusion: **no parent class depends on a Proof result**. From this addendum on, the "Proof link" column and every PC citation or "confirmed statically (PC-nn)" phrase in the parent "Basis for class" cells are to be read as **post-Proof corroborative annotations**, not classification inputs. For base_automation, the same statement was made in the REC addendum R1 §4; A3 RD-5 accepted its content and found only the ordering defect, which this batch avoids (A2 frozen → this REC frozen → Proof).

---

## 3. Basis addenda, class changes and new items

### 3.1 `auth_signup`

| REC ID | Change | Basis addendum (A1/A2 only) | Class | Proof link (to be predeclared by Proof) |
|---|---|---|---|---|
| REC-ASGN-28 | Basis addendum | Per A2 O4-R1: platform duplicate and restore-as-copy regenerate the signing secret (links predicted rejected in the copy); plain restore and external copies keep it (links predicted accepted). On the regenerating paths the base-URL parameter is reset to a local default. Parent sentence "a clone keeping the secret would accept links" is kept and now states which clones keep it | UNKNOWN_PENDING_PROOF (unchanged); A2 label restored | New runtime case for PR-ASGN-13; new static case for the clone-path reading |
| REC-ASGN-18 | Basis addendum | Per A2 C18-R1: no rights check at all for a partner with no user, on either builder; single-partner check only where another user exists; reachability depends on unenumerated cross-module callers | CONTRADICTION (A1 vs A2; unchanged). Runtime effect now has a required proof | New static enumeration case for PR-ASGN-14; new runtime case for PR-ASGN-15 |
| QID G01-AUTH_SIGNUP-Q018 | Mapping annotation (D-ASGN-A3-05) | Mapping to REC-09 is **topical only**: C09 concerns the status computation basis, not auditability or attribution of the status-change event. **No audit evidence** exists in the lineage | — | — |

### 3.2 `base_setup`

| REC ID | Change | Basis addendum | Class | Proof link |
|---|---|---|---|---|
| REC-BSET-26 | **Basis correction** (D-BSET-A3-01) | The parent sentence "Portal keys are creatable only when the portal module's allow-keys parameter is set (PC-07 observation)" is **withdrawn as a narrowing basis**. Per A2 F1-R1 / O3-R1: the parameter governs only creation through the key wizard. A key created while its owner was internal survives a change to portal and still passes the KPI check with the parameter absent, until its expiry. Server-created keys and the programmatic path (separate parameter, off by default) are further routes. The HIGH finding is **not** narrowed | UNKNOWN_PENDING_PROOF (unchanged) | PC-BSET-18 superseded by an R1 case that includes the demoted-owner variant (PR-BSET-12); new static case for key survival across a user-type change |
| REC-BSET-15 | Basis addendum | Same F1-R1 correction applies to the C15 RISK: "any active owner" includes demoted-to-portal owners | UNKNOWN_PENDING_PROOF (unchanged) | As REC-BSET-26 |
| REC-BSET-12 | **Class change MATCH → UNKNOWN_PENDING_PROOF** | The parent kept C12 as MATCH by an explicit exception ("runtime case is confirmatory only"). A2 addendum §2.2 raises PR-BSET-06 to required (PR-BSET-06R1) because the settings save path disables archive filtering and the counter is a non-stored computed value. Under the parent's own rule, an A2 VERIFIED claim with a required runtime proof is UNKNOWN_PENDING_PROOF. X-BSET-02 stays RESOLVED for the form-load path only | **UNKNOWN_PENDING_PROOF** | PC-BSET-23 superseded by an R1 case (required; form load and post-save); new static case on the save-path context |

Counts after this addendum (base_setup): MATCH **12**, CONTRADICTION 5, UNKNOWN_PENDING_PROOF **13**, GAP 4. Total 34. Lane B unchanged: UNCORROBORATED 25, NOT_APPLICABLE 9.

### 3.3 `base`

No class or basis change. Items D1 and D3 belong to Proof; D2 to Integration Control. D4 is reconciled in base_automation (3.5). Rule 1 labels restored (section 1); rule 3 re-scan in section 4.

### 3.4 `portal`

| REC ID | Change | Basis addendum | Class | Proof link |
|---|---|---|---|---|
| REC-PRTL-21 | Basis addendum | Per A2 O2-R1: five mint invocations in four functions. The pager site reads neighbours on the superuser handle, bypassing explicit and implicit read checks, but its ids come only from the caller's own session history, filled by login-required list routes. Exposure = stale history after access loss in the same session. The parent Proof R1 wording "crafted or previous session history" is not adopted | UNKNOWN_PENDING_PROOF (unchanged); A2 label restored | PC-PRTL-17 superseded by an R1 case carrying PR-P4R1 (stale-history scenario); new static case on the pager reach |
| REC-PRTL-01 | Basis addendum | Same count correction (C01 core unchanged) | UNKNOWN_PENDING_PROOF (unchanged) | As REC-PRTL-21 |
| REC-PRTL-22, REC-PRTL-04 | Link update | PR-P5 replaced by falsifiable PR-P5R1 (each of cancelled-state, other-company and archived documents predicted to open by token) | UNKNOWN_PENDING_PROOF (unchanged) | PC-PRTL-18 superseded by an R1 case |

### 3.5 `base_automation`

| REC ID | Change | Basis addendum | Class | Proof link |
|---|---|---|---|---|
| REC-BAUT-38 | Basis addendum (RD-1) | Per A2 O14-R2: on the time path, a job user outside the settings group cannot read the rule model; the first rule search raises, the run is FAILED with nothing processed. REC-11-R1's sentence "a reassigned ordinary user would apply that user's rights to record selection" holds only for a settings-group job user | UNKNOWN_PENDING_PROOF (unchanged) | PC-BAUT-64 superseded by an R1 case (PR-29R1, variants ii-a and ii-b) |
| REC-BAUT-11 | Basis addendum (RD-1) | The REC-11-R1 time-path row is qualified as above | UNKNOWN_PENDING_PROOF (unchanged) | As REC-BAUT-38 |
| REC-BAUT-47 | Basis addendum (RD-2) | Per A2 O18-R1: the rule search, active check, selection and last-run write are outside isolation; rules iterate in id order; a persistent selection error starves later rules in **every** run and drives deactivation. A2 label assigned | UNKNOWN_PENDING_PROOF (unchanged) | PC-BAUT-65 superseded by an R1 case (PR-30R1, three runs) |
| REC-BAUT-27 | Basis addendum (RD-3) | Per A2 O3-R2: worker timeouts also count FAILED for this module; restart via rule write is a silent no-op on a locked job row and needs an active time rule; any rule's critical write re-activates; persistent failure oscillates | UNKNOWN_PENDING_PROOF (unchanged) | New runtime case for PR-31 |

New REC item (A3 base D4; A2 addendum O19):

| REC ID | Item | A1 | A2 | REC class | Basis | Lane B | A2 proof label | Proof link | QID lineage |
|---|---|---|---|---|---|---|---|---|---|
| REC-BAUT-48 | O19 | (not stated; A1 C11 and base A1 C27 describe elevated dispatch only) | O19 MED: the per-action group gate still binds the real user under elevation, so group-restricted actions raise for triggering users outside the group and can block their edits | UNKNOWN_PENDING_PROOF | A2 omission predicted statically (parent rule) | UNCORROBORATED | MISSING_REQUIRED_RUNTIME_PROOF | New runtime case for PR-32; cross-module base PC-BASE-07, PC-BASE-10 | Q002, Q013 |

Counts after this addendum (base_automation): MATCH 16, CONTRADICTION 5, UNKNOWN_PENDING_PROOF **22**, GAP 5. Total **48**. Lane B: UNCORROBORATED **39**, NOT_APPLICABLE 9. No FAIL for absence.

---

## 4. Rule 3 — "no evidence yet" QIDs re-scanned against all A1 item classes (lineage only; no QID answered)

Method: every QID on each parent "no evidence yet" list was compared with A1 claims (C), business rules (BR), states/transitions, exceptions/failure modes (F), cross-module handoffs (H), gaps (G), CRQs and contradictions (X), plus A2 omissions including this batch. A mapping means topical relevance only.

### 4.1 `auth_signup` (parent: 16 no-evidence)

| QID (topic) | Added mapping | A1/A2 item class and reason |
|---|---|---|
| Q005 (forwarded invitation authority) | REC-05 | C05 / BR3 / link state: the link is a bearer credential bound to partner, users, last login and type, not to a recipient channel |
| Q008 (concurrent enrollment) | REC-13, REC-34 | BR2 (one e-mail, one identity, application check); G4 (base uniqueness constraint unread) |
| Q010 (role changed before use) | REC-05 | BR3: the link binds no role or group; a role change does not invalidate it |
| Q014 (anti-forgery on submission) | REC-36 | Carried gap (CSRF defaults unread) — gap lineage only |
| Q016 (post-enrollment redirect) | REC-36 | Carried gap (redirect sanitisation unread) — gap lineage only |
| Q017 (unverified identity privileges) | REC-09, REC-14 | States (Invited → Confirmed on first login); BR4 (new identities inherit template rights regardless of status) |
| Q021 (Unicode normalisation) | REC-13, REC-34 | BR2; G4 (A2: login exact match, e-mail case-insensitive; normalisation form unread) |
| Q025 (retry after ambiguous timeout) | REC-13, REC-16 | BR2 (duplicate refused); exception: mail failure keeps user, cancels pending type |
| Q027 (invitation removal preserves audit) | REC-17 | States: pending type cleared on archive/delete; no stored token |
| Q031 (snapshot restore resurrects credentials) | REC-05, REC-28 | BR3 (validity derives from current partner state, so a restored older state re-validates a consumed link); O4-R1 (restore paths and secret) |
| Q004, Q020, Q030, Q035, Q038, Q039 | none | No A1 or A2 item of any class concerns company context on completion, password policy, company deletion, identifier change, queued-delivery context or transaction posting |

Totals: mapped 24 → **34**; no evidence yet 16 → **6** (Q004, Q020, Q030, Q035, Q038, Q039).

### 4.2 `base_setup` (parent: 16 no-evidence)

| QID (topic) | Added mapping | Reason |
|---|---|---|
| Q003 (save resets unrelated settings) | REC-19, REC-20 | C19/C20 are the module's parameter-bound settings; A3 CH-10 found neither declares a default, so the absent-row mechanism does not reset them (topical) |
| Q005 (no-op save triggers install) | REC-04, REC-32 | C04 (install toggles); G3 (settings machinery beyond save unread) |
| Q006 (disabling capability leaves stale access) | REC-26, REC-24 | O3-R1: switching the portal allow-keys parameter off does not revoke existing keys; O1: archive does not remove keys |
| Q008 (default-access change not retroactive) | REC-05 | C05 / states: the default-access group governs newly created internal users |
| Q013 (concurrent creation, one account) | REC-06, REC-29 | BR2 (reactivate, not duplicate); O6 (second identity possible) |
| Q015 (implied-group toggles scope) | REC-32 | G3 gap lineage |
| Q016 (company-limited admin and broad groups) | REC-02 | BR1 / C02 (settings surface restricted to system administrators) |
| Q026 (diagnostics authority) | REC-20, REC-34 | C20 (profiling-until setting); G7 (enforcement location unread) |
| Q034 (telemetry failure details) | REC-16, REC-14 | Exceptions: provider errors returned as addon/provider/message entries; per-database failures logged server-side with the database name (parent Proof R5 context) |
| Q040 (idempotent retry of admin save) | REC-05, REC-06 | States: default-access group created only when absent; BR2 bulk invite reactivates instead of duplicating |
| Q021, Q024, Q035, Q037, Q038, Q039 | none | Q021: C11 only reads demo state (considered, not a fit for "loading"); Q024: only the layout-edit exception touches templates and says nothing on authority (considered, not mapped); the rest have no A1/A2 item |

Totals: mapped 25 → **35**; no evidence yet 16 → **6** (Q021, Q024, Q035, Q037, Q038, Q039).

### 4.3 `base` (parent: 23 no-evidence)

| QID (topic) | Added mapping | Reason |
|---|---|---|
| Q016 (archive vs delete semantics) | REC-15 | States: company archived (branches archived; blocked while default of active users); API key expired vs removed |
| Q018, Q019, Q020 (import / partial import / export) | REC-53 | G4 (import/export, wizards unread) — gap lineage only |
| Q021 (saved filters) | REC-04, REC-53 | BR1 (access re-evaluated at each query); G4 (filters unread) |
| Q032 (per-company user defaults) | REC-16, REC-17 | BR4 (default company within allowed set); F2 (out-of-set default dropped silently) |
| Q034 (counts/pagination inference) | REC-04 | BR1 (rules apply to search and count alike) |
| Q035 (recent-item history) | REC-53 | G4 gap lineage |
| Q037 (retry re-evaluates authority) | REC-31, REC-30 | States (job acquired → running → progress commits); F5 (failure rolls back own transaction, committed batches stay) |
| Q038 (stale cross-scope computed values) | REC-07, REC-33 | CRQ-05 (cache refresh after company switch); G6 (cross-worker cache clearing) |
| Q048 (concurrent revalidation) | REC-51 | G1 (company-consistency check after create/write; ORM layer) — gap lineage |
| Q007, Q008, Q011, Q012, Q027, Q030, Q040, Q041, Q042, Q043, Q044, Q046 | none | No A1/A2 item of any class addresses these (Q030 considered against BR2: activated set is a visibility input, not an owner of unsaved data — not mapped) |

Totals: mapped 27 → **38**; no evidence yet 23 → **12**.

### 4.4 `portal` (parent: 16 no-evidence)

| QID (topic) | Added mapping | Reason |
|---|---|---|
| Q007 (navigation / counters) | REC-11 | H: downstream modules override counters; downstream record rules decide visibility (C11) |
| Q014 (inert external content) | REC-31 | G3 gap lineage (was noted but left unmapped) |
| Q017 (external updates approve/post) | REC-13 | BR6: customer self-edit limited to allow-listed identity/address fields |
| Q022 (parent deletion / orphan links) | REC-02 | States: document token has no transition back; BR2 no expiry |
| Q023 (logout / account switch cached state) | REC-21 | O2-R1: navigation neighbours come from server-side session history (stale-history exposure) — topical |
| Q028 (queued notification revalidation) | REC-21 | H (mail notification buttons carry token/pid/hash); O2 (notification grouping mints elevated) |
| Q034 (restore / migration preserves revocations) | REC-09, REC-18 | BR5 (revoke does not invalidate record tokens); S1/S2 chatter identity keyed by the database secret |
| Q035 (cloned environment exposure) | REC-06, REC-18 | C06 / S2: signed hash keyed by the per-database secret; A2 B3A §4.3 clone split (platform duplicate regenerates; other copies keep) |
| Q008, Q009, Q018, Q024, Q025, Q029, Q032, Q033 | none | No A1/A2 item addresses search, aggregates, concurrency, timeout atomicity, resubmission, personalisation or rate limiting (Q025 considered against BR2 ensure-once; it concerns token creation, not one-time business effects — not mapped) |

Totals: mapped 24 → **32**; no evidence yet 16 → **8**.

### 4.5 `base_automation` (after REC addendum R1: 7 no-evidence)

| QID (topic) | Added mapping | Reason |
|---|---|---|
| Q028 (trigger storm exhausts shared capacity) | REC-27, REC-47 | O3-R2 (single shared job; one failing rule or timeouts can deactivate it for all); O18-R1 (a selection error starves later rules) — A3 RD-6 |
| Q024 (snapshot restore replays effects) | REC-09 | G9 folded into C09 / CRQ-04: no deduplication or idempotency marker; time path re-selects from last-run, so a restored older last-run re-selects the window — A3 RD-6 |
| Q025 (cloned environments execute live outbound actions) | REC-14, REC-20 | C14 (inbound webhook identifier copied with data); C20 / A2-R1-03 (outbound webhook action sends after commit); CRQ-03. Topical: nothing in the module distinguishes a clone |
| Q017, Q026, Q027, Q033 | none | Considered against BR3 (in-context recursion guard, not record concurrency), mail handoff, C10 and C23 — no fit |

Totals: mapped 33 → **36**; no evidence yet 7 → **4** (Q017, Q026, Q027, Q033).

---

## 5. Handoff to PROOF

Proof must, **after** recording this addendum's sha256 in its header and **before** its first source fetch, predeclare cases (file sha256 + UTC) for:

| Module | Required |
|---|---|
| auth_signup | runtime PR-ASGN-13; static PR-ASGN-14 (caller enumeration at the anchor); runtime PR-ASGN-15; static cases for the clone-path and userless-partner readings |
| base_setup | withdraw or correct refinement R2; supersede PC-BSET-18 (with the PR-BSET-12 demoted-owner variant) and PC-BSET-23 (required, PR-BSET-06R1); static cases for key survival across a user-type change and for the save-path counter context (A3 D-BSET-A3-03 fail-condition weakness); record the A3 D-BSET-A3-04 post-predeclaration additions as tagged |
| base | Proof header: record the parent REC sha256 (D1) and the one-line change note; correct the section 6 S1 design note (D3) |
| portal | supersede PC-PRTL-17 R1 extension with PR-P4R1; supersede PC-PRTL-18 with PR-P5R1; restate parent R1 severity basis; static case for the pager reach |
| base_automation | supersede PC-64 (PR-29R1) and PC-65 (PR-30R1); new runtime PR-31, PR-32; tag PC-12R1's added step and expectation as POST-DECLARATION and restore PC-64's dropped fail condition (RD-4); record the D4 correction to parent Proof R4 / PC-BAUT-40; static cases for RD-1, RD-2, RD-3 and O19 |

Runtime device is offline per every upstream Proof; runtime cases are expected to be NOT-EXECUTED and must not be reported otherwise.

## 6. Limitations

- REC read no source; bases rest on A1, parent A2, and the A2 addendum B3A (whose source reads are blob-verified there).
- QID mappings are topical lineage judged by this controller; they are not a coverage measure and answer nothing.
- The same controller authored the A2, REC and Proof addenda of this batch (disclosed; A3 is the independent stage).
- No Lane B or runtime evidence exists; absence is not failure. No percentages, no Formal Coverage claim, no git operations, no existing file edited.
