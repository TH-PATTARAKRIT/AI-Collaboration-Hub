# G01 PLATFORM_BASE — RED TEAM Reconciliation Addendum R1 (A3 remediation, batch B3B) — `web`, `web_tour`, `http_routing`, `html_editor`, `mail`

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RECONCILIATION (REC)**. Addendum only. All parent REC and REC-delta files are immutable and were not edited |
| Group / Modules | G01 PLATFORM_BASE / `web`, `web_tour`, `http_routing`, `html_editor`, `mail` |
| Date | 2026-09-27 (written after 15:47:12Z) |
| Parent REC artifacts (sha256; re-hashed 2026-09-27T15:42:36Z; equal to A3 intake) | `G01_RECONCILIATION/G01_WEB_REC_20260927.md` `9e2a4a370ffb4e9a010e81633da1e85f0db4c2a762f8c26322ef38074e5abc2d`; `G01_RECONCILIATION/G01_WEB_REC_DELTA_D1_20260927.md` `b89931533a23ace1fc25d9cecd5febd2e305b84cf83e4e94aa0a2f40f2c00985`; `G01_RECONCILIATION/G01_WEB_TOUR_REC_20260927.md` `b875cc2864bbe03fa9773802b54417062f9f2ce643e240ebd3c08906bdd59c55`; `G01_RECONCILIATION/G01_HTTP_ROUTING_REC_20260927.md` `b20ab28814a7586ac8de4d436d9572bfd292f9f9ff27bdc84b622882c54e215a`; `G01_RECONCILIATION/G01_HTML_EDITOR_REC_20260927.md` `6677f36de93e588de97f55946fce1d7f8904a534854c7a81ca38aec46e83eae8`; `G01_RECONCILIATION/G01_MAIL_REC_20260927.md` `d5c8ea38e8436a431f3183754b38f312d99b3f613fb8716084ea367d9a6bada4`; `G01_RECONCILIATION/G01_MAIL_REC_DELTA_D1_20260927.md` `bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f` |
| Upstream addendum consumed (immutable) | A2 R1 `G01_A2_REVIEWS/G01_B3B_A2_ADDENDUM_R1_20260927.md` sha256 **`d9eee187342b1c648c50a2d2bb9c4e6d38f81b074c35335aadd2183237cc975b`** (hashed 2026-09-27T15:47:12Z). Its parents (A1 packages, A2 reviews, A2 D1 reviews) are listed with sha256 in its section 0.1 and are unchanged |
| A3 reports (sha256) | web `a9e45066528fc584f38c8f7395c5aec971a70a41908bccbf53753ad128ef3583`; web_tour `e250bd923ea3bf2b0788512362b95ee315ace377c5d0e00e3edcadbee0f85a9f`; http_routing `d1e32ae9a74f63603dbdd76f63deba296f90e90de4dafaccbbfbee0ed9d21297`; html_editor `d51187b446cd5aba0de82e62ce4c848f13aff7aa1d33ed3b31ee271d69281ecb`; mail `ada5f82a06d4f73d286a8f73c3f51ad1a0ad564a28568eb1f1e4706e683f414f` (all under `G01_A3_CHALLENGES/`) |
| Question lineage inputs | web bank W1-B01 `259839a2c0f265b9519d23bad3b25b8d74dd5a89b9410e01d3560e0a42fcd558` (freeze `558ec880…7177`); mail bank W1-B01 `0d6d7fcc4d6fef3be30ee281ee7096e8fc1fdb9e94d96ff120d0f5e79a10bf7d`; web_tour bank W1-B05 `fdc06e0b530f327b2eec9ffddd3abff4104d387acb43c2fade99344854986f37` (freeze `cc81bc57…1bd3`); http_routing W1-B08 and html_editor W1-B07 are **DELTA-RECHECK: QID lineage NOT A3-ELIGIBLE**; every QID change for those two modules below is **PROVISIONAL** |
| Challenge IDs addressed (REC parts) | **web:** D-W3 (REC-WEB-05 D1 attribution); D-W2 REC mapping (Q042, Q046); REC-WEB-27 net state after A2 R1. **web_tour:** D-T1 REC mapping (Q033, Q016); OM-T03 proof link. **http_routing:** A3-HROU-D2 (REC-HROU-03 basis); CH-4c / N1 (REC-HROU-19 provider); CH-1 sharpening (REC-HROU-13). **html_editor:** A3-HEDT-D1 (REC carries: REC-HEDT-10, REC-HEDT-08, §2.3 escalation wording). **mail:** A3-D1 (REC-28/REC-52 wording vs REC-delta CF-2); A3-D2 (REC-09/11/33/43 restatement; REC-42 unchanged); A3-D5 (REC-36/45 proof links); A3-D6 (BR/X/H/CRQ scan; Q019); A3-D7 (process: freeze before Proof) |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 C1-B process-rule compliance (this addendum)

| Rule (MASTER C1-B) | Compliance in this REC addendum |
|---|---|
| 1. Preserve A2 `MISSING_REQUIRED_RUNTIME_PROOF` labels (restore where collapsed) | **Complied.** Section 1 restores the label for every item A2 labelled (A2 R1 section 7): web 8 base + 8 D1, web_tour 3, http_routing 8, html_editor 11, mail 10 base + 8 D1. The collapsed parent cells ("UNCORROBORATED", "UNCORROBORATED + runtime") are withdrawn for those items. New items carry A2 R1's label where A2 R1 assigned one |
| 2. Tag post-declaration text `POST-DECLARATION` | **Not applicable to REC** (REC declares no Proof cases). This REC addendum is frozen **before** the Proof R1 predeclaration; it cites no Proof R1 result |
| 3. REC scans all A1 item classes; fix "no evidence" lists | **Complied.** Section 7 records the scan of every A1 item class (claims, business rules, states, exceptions, handoffs, gaps, CRQs, contradictions) for all five modules, plus the A1/Lane A notes in A2 R1 section 1. "No evidence" lists are recomputed per module (section 8) |
| 4. Order A2 → REC (sha256) → Proof predeclare → Proof execute; Proof header records REC sha256 | **Complied.** Consumes A2 R1 by sha256 (header). This file's sha256 is recorded in the Proof R1 header and in its predeclaration record, both written after this file was closed. REC classes below rest on A1 + A2 (+A2 R1) + already-frozen parent Proof results only; no Proof R1 result is cited |
| 5. Predeclared cases hashed + UTC before first Proof source fetch | **Not applicable to REC.** Proof links below name Proof R1 case IDs as **planned** links; the cases themselves are declared, hashed and time-stamped by Proof R1 |

Clean-room note: neutral paraphrase only; identifiers are evidence pointers; no vendor code. No percentages. No Formal Coverage claim. **No QID is answered** (mapping is lineage only). No git operations. No existing artifact was edited.

Owner-stage re-derivation: every REC correction below was re-checked against the source reads recorded in A2 R1 (same anchor; blob log `remed_b3b/blob_log_rederive.txt` sha256 `b614470cb255a4a33d20b40485f290d181ebf90c9f1c8ce74272005413a7ceb4`). Each row states AGREE or DISPUTED.

---

## 1. Rule 1 — `MISSING_REQUIRED_RUNTIME_PROOF` label restoration (Lane B column, R1)

The label is carried exactly as A2 assigned it. For items A2 labelled "UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF", the R1 cell carries both. Nothing is FAIL for absence of Lane B.

| Module | REC item (A1/A2 item) | Parent Lane B cell | **R1 Lane B cell** |
|---|---|---|---|
| web | REC-WEB-05 (C05/X-WEB-01), REC-WEB-08 (C08), REC-WEB-11 (C11), REC-WEB-12 (C12), REC-WEB-13 (C13), REC-WEB-14 (C14), REC-WEB-15 (C15), REC-WEB-23 (C23) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| web D1 | REC-WEB-D22 (D03), D25 (D06), D26 (D07), D29 (D10), D30 (D11), D36 (D17), D38 (AO-W1) | "UNCORROBORATED + runtime" | **UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF** |
| web D1 | REC-WEB-D04 (CRQ-WEB-02 residual) | UNCORROBORATED | **UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF** |
| web_tour | REC-WTOUR-04 (C04 concurrency), REC-WTOUR-10 (C10 exploitability), REC-WTOUR-11 (C11) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| http_routing | REC-HROU-06 (C06), 09 (C09), 10 (C10), 13 (C13), 16 (C16) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| http_routing | REC-HROU-14 (C14), 15 (C15) | UNCORROBORATED (REC had overridden A2's NOT_APPLICABLE) | **MISSING_REQUIRED_RUNTIME_PROOF** (A2 section 7 governs) |
| http_routing | REC-HROU-19 (X-HROU-01) | NOT_APPLICABLE | **MISSING_REQUIRED_RUNTIME_PROOF** (runtime leg of PR-HROU-02) |
| html_editor | REC-HEDT-05 (C05), 08 (C08), 09 (C09), 10 (C10), 20 (C20), 33 (SF-02), 34 (SF-06), 35 (CRQ-02) | UNCORROBORATED | **MISSING_REQUIRED_RUNTIME_PROOF** |
| html_editor | REC-HEDT-02 (C02), 04 (C04), 25 (X-HEDT-04) | NOT_APPLICABLE | **MISSING_REQUIRED_RUNTIME_PROOF** (runtime legs PR-HEDT-06, PR-HEDT-04) |
| mail | REC-MAIL-05 (C05), 08 (C08), 09 (C09), 11 (C11), 13 (C13), 15 (C15), 16 (C16), 21 (C21), 24 (C24), 28 (C28) | UNCORROBORATED | **UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF** |
| mail D1 | REC-MAIL-D1-24 (D01), D1-26 (D03), D1-27 (D04), D1-28 (D05), D1-29 (D06), D1-31 (D08), D1-34 (D11), D1-37 (D14, merged into REC-MAIL-38) | UNCORROBORATED | **UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF** |

Counts of restored cells: web 16, web_tour 3, http_routing 8, html_editor 11, mail 18. The classification rule for these items is unchanged (their REC class stands), except where sections 2–6 say otherwise.

---

## 2. `web`

### 2.1 D-W3 / A3-W-02: REC-WEB-05 class basis corrected — AGREE

The parent REC-WEB-05 class cell ("A1 base claim superseded by A2 + D1") and the parent section 2.2 phrase ("and independently by A1-D1 (RESOLVED)") conflict with the parent's own section 0.3 (no D1 credit at that time). **Both phrases are withdrawn.** R1 basis for the class **CONTRADICTION — RESOLVED** (unchanged): (i) A2 SF-W01 (export gate in the ORM export method, reached by CSV/XLSX in the caller's environment); (ii) the parent Proof source re-read PC-WEB-09/10; (iii) **A3's independent re-read** (A3-W-02), which is the independent second line the parent RESOLVED rule required. D1 credit is valid only from the REC delta D1 onward (after A2 D1 verification); the D1 supersede map's "credited" row stands for the net state after D1 and does not retro-validate the base cell. Residuals remain separate open items: REC-WEB-25, REC-WEB-27 (see 2.2), REC-WEB-31. Downstream must not read "RESOLVED" as "export egress is governed".

### 2.2 REC-WEB-27 (OM-W02, empty-result exports) — net state after A2 R1

The parent contradiction was A2's unconditional statement vs the PC-WEB-11 source re-read. A2 R1 (section 2.1) issues OM-W02R1/SF-W02bR1, which match the PC-WEB-11 observation. The originating side has converged. **R1 class: CONTRADICTION — RESOLVED (source layer)**; both original statements are preserved; **PC-WEB-11 FAIL stays preserved** as a failed result against its predeclared expectation. The narrowed residual is carried as a new item REC-WEB-R1-05 (UNKNOWN_PENDING_PROOF, runtime PR-W09). The D1 consistency record's "A2 D1 D01-row wording" is covered by A2 R1 section 2.3.

### 2.3 New and carried items (A1/Lane A notes; A1 item-class scan)

| REC ID | Item | A1 / note | A2 verdict | REC class | Basis | Lane B | Proof link (planned for R1 cases) | QID lineage (`web`) |
|---|---|---|---|---|---|---|---|---|
| REC-WEB-R1-01 | A1N-WEB-01 (framing headers) | Note: frame-deny on client page; same-origin framing and frame-ancestors-self on login page; per-route only | VERIFIED (A2 R1 2.2) | MATCH | Header settings are static facts on two routes. Whether other pages can be framed, and browser enforcement, are outside this item (not claimed) | UNCORROBORATED | PC-WEB-31 | **Q042** |
| REC-WEB-R1-02 | A1N-WEB-02 (export filename/disposition) | Note: server-built filename, sanitised, attachment disposition, fixed content type | VERIFIED | MATCH | Static; no caller-controlled filename on this path | UNCORROBORATED | PC-WEB-32 | **Q046** (with D1 REC-WEB-D37) |
| REC-WEB-R1-03 | A1 §4 exception "failed export wrapped as server error payload" (E24) + A1N-WEB-03 | A1 exception bullet (not carried by parent REC) sharpened by the note: payload includes a full traceback | VERIFIED, sharpened | MATCH | A1 and A2 agree; the payload content is a static fact of the two export routes | UNCORROBORATED | PC-WEB-33 | Q034 |
| REC-WEB-R1-04 | A1N-WEB-04 (download routes: no-sources policy, no-sniff) | Note | VERIFIED | MATCH | Header defaults are static; effect under proxies/browsers is deployment/runtime and not claimed | UNCORROBORATED | PC-WEB-34 | **Q015** |
| REC-WEB-R1-05 | OM-W02R1 residual (empty flat export skips the gate; zero-count log) | (A1 silent) | A2 R1 OM-W02R1 | UNKNOWN_PENDING_PROOF | Static basis PC-WEB-11 (flat leg) and planned PC-WEB-29; the runtime result is PR-W09 | **MISSING_REQUIRED_RUNTIME_PROOF** | PC-WEB-29; PC-WEB-30 (runtime) | Q050, Q030 |
| REC-WEB-R1-06 | BR-1 | Data access via one generic API; authority from target ACL/rules | Consistent (A2 §3) | MATCH (folded into REC-WEB-02) | Anchored to C02 | NOT_APPLICABLE | — | as REC-WEB-02 |
| REC-WEB-R1-07 | BR-4 | System group can take superuser identity | Consistent | UNKNOWN_PENDING_PROOF (folded into REC-WEB-13) | Anchored to C13 | MISSING_REQUIRED_RUNTIME_PROOF (as C13) | PC-WEB-05 | as REC-WEB-13 |
| REC-WEB-R1-08 | BR-5 | Preferences per user; branding per company into one shared artifact | Consistent | MATCH (folded into REC-WEB-20/21/32) | Anchored to C20, C21, OM-W07 | NOT_APPLICABLE | — | — |
| REC-WEB-R1-09 | A1 §3 states (become switch; master password default → chosen; company cookie normalised/cleared; no document state machine) | — | Anchored (A2 R1 6.7) | Folded into REC-WEB-13, 11, 19, 01 | — | as anchors | — | as anchors |
| REC-WEB-R1-10 | A1 §4 other exceptions (missing action, non-owned view, search-panel type, logo fallback, health fail, master-password error text) | — | Anchored | Folded into REC-WEB-22, 14, 17, 30 | — | as anchors | — | as anchors |
| REC-WEB-R1-11 | A1 §5 handoffs (base, framework, web_tour, downstream bundles, base_setup) | — | Structural, consistent | MATCH | No disagreement | NOT_APPLICABLE | — | — |

`web` REC-WEB-11 proof link R1: the parent link PC-WEB-15 is supplemented by the split cases PC-WEB-15Ra (CONFIG) and PC-WEB-15Rb (SOURCE) (Proof R1; A3 D-W4). PC-WEB-15's parent PASS is not re-labelled.

---

## 3. `web_tour`

| REC ID | Item | A2 verdict | REC class | Basis | Lane B | Proof link (planned) | QID lineage (`web_tour`) |
|---|---|---|---|---|---|---|---|
| REC-WTOUR-25 | A1N-WTOUR-01 (record ids removed from guide and step payloads) | VERIFIED | MATCH | Static payload shaping | NOT_APPLICABLE | PC-WTOUR-15 | **Q033** |
| REC-WTOUR-26 | A1N-WTOUR-02 (empty step content key omitted) | VERIFIED (server); client NOT_VERIFIED | MATCH (server side) | Static; client rendering of an absent key stays in GAP REC-WTOUR-23 (G-2) | UNCORROBORATED | PC-WTOUR-15 | **Q016** (partial) |
| REC-WTOUR-18 (R1 update) | OM-T03 | — | UNKNOWN_PENDING_PROOF (unchanged) | A2 R1 PR-T04 now exists | **MISSING_REQUIRED_RUNTIME_PROOF** (new PR) | PC-WTOUR-16 (runtime) | Q029 |
| REC-WTOUR-27 | A1 BR-1..BR-5; §3 states; §4 exceptions (unique name, unknown-name no-op, non-internal ignored, malformed export); §5 handoffs | Anchored (A2 R1 6.7) | Folded into REC-WTOUR-02, 03, 04, 05, 06, 07, 08, 09, 10, 12, 14 | Each bullet cites its anchor claim | as anchors | — | as anchors (unique name → Q001 via REC-02) |

---

## 4. `http_routing` (QID changes PROVISIONAL — W1-B08 not A3-eligible)

| REC ID | Item | R1 change | Basis / position |
|---|---|---|---|
| **REC-HROU-03** (C03) | Basis restated (A3-HROU-D2) | Class **CONTRADICTION — OPEN** (unchanged). R1 basis: "Source **partly supports each side**. For matched endpoints, language, canonical and frontend-error behaviour are opt-in by route flags (supports A2; parent PC-HROU-09). For unmatched paths the behaviour is request-wide and flag-independent: language resolution runs, non-POST redirects are reachable, and a still-unmatched path is forced into frontend handling (supports A1's RISK in part; A2 R1 4.1)". The parent phrase "Source supports A2" is withdrawn. Proof links: PC-HROU-09 (matched branch) + PC-HROU-11 (unmatched branch, planned) | **AGREE** |
| **REC-HROU-19** (X-HROU-01) | Provider located | Class **CONTRADICTION (source vs manifest)** unchanged. The parent basis phrase "`/contactus` provider not located … unverified here" is withdrawn: the provider is a `website` published page **data record** (A1N-HROU-02, A2 VERIFIED). Runtime expectation per A2 R1 PR-HROU-02R1: dead link without `website`, served page with it. Proof links: PC-HROU-12 (planned), PC-HROU-R02R (runtime) | **AGREE** |
| **REC-HROU-13** (C13) | Escalation sharpened | Class UNKNOWN_PENDING_PROOF unchanged. R1 basis addition: a concrete anonymous path exists **without `website`**: html_editor's public website-flagged shape route raises bad-request on colour-validation failure and so reaches the 400 template's debug block when the debug query parameter is set (static inference; A2 R1 4.3). A non-numeric animation-speed value is a predicted 500 path (static prediction only). Unmatched paths also reach the frontend error handler (REC-HROU-03 R1). Proof links: PC-HROU-13 (planned); PC-HROU-R01b/c/d (runtime) | **AGREE** |
| REC-HROU-28 (new) | A1N-HROU-01 (canonical-domain URL drops query string) | MATCH (A2 VERIFIED); Lane B NOT_APPLICABLE; proof link PC-HROU-14 (planned); QID **Q008** (provisional) | New evidence; scan fix |
| REC-HROU-29 (new) | A1 §4 exception "localised URL rebuild failure → quoted raw path" (Lane A item 16) | MATCH (A2 R1 VERIFIED); Lane B NOT_APPLICABLE; proof link PC-HROU-14 (planned); QID **Q006** (provisional: on access or missing-record errors the builder returns the quoted requested path rather than a rebuilt name-bearing slug) | Scan fix (A1 exception not carried by parent REC) |
| REC-HROU-30 (new) | A1 BR5 ("error details only in editable/debug rendering") | CONTRADICTION (A1 BR5 vs A2 SF-HROU-01 qualification) — OPEN, folded into REC-HROU-13 for proof; Lane B MISSING_REQUIRED_RUNTIME_PROOF (as C13); QID Q035 | Scan fix: A1 BR5 is stated as a rule; A2 shows debug is requester-set |
| REC-HROU-31 (new) | A1 BR1–BR4, §3 states, other §4 exceptions (slug missing id, unmatched case warning, nested 404→500, 418 on render failure), §5 handoffs | Folded into REC-HROU-04/06, 06/09, 07/08, 11, 09/10, 12 | Anchored bullets |

---

## 5. `html_editor` (QID changes PROVISIONAL — W1-B07 not A3-eligible)

### 5.1 A3-HEDT-D1 carried by REC — AGREE

| REC ID | R1 risk statement (replaces the parent basis wording for consumption) | Class |
|---|---|---|
| **REC-HEDT-10** (C10 + SF-03) | "A caller with write access to the target can store caller-supplied bytes typed as SVG; the superuser MIME reset reverses the core downgrade exactly for actors without view write (base condition now read, A2 R1 5.2). **Serving mitigation:** platform download responses carry no-sniff and a content-security policy allowing no sources, so script execution is materially limited when the SVG is opened directly or loaded as a document (A2 R1 5.1). Residual, bounded: serving paths that set or disable their own policy, header-stripping proxies, inline embedding into HTML (sanitiser, EG1), and stored-content trust. Storage finding stands; exploitability unproven" | UNKNOWN_PENDING_PROOF (unchanged) |
| **REC-HEDT-08** (C08 + SF-03) | Same serving mitigation and residual apply to the superuser media-library SVG; timeout and remote-MIME findings unchanged | UNKNOWN_PENDING_PROOF (unchanged) |
| Parent §2.3 escalation bullet "modify_image … store own bytes typed as SVG (REC-10). Static only." | Superseded for consumption by the REC-HEDT-10 R1 statement above | — |

Proof links R1: REC-HEDT-10 → PC-HEDT-04 (parent), PC-HEDT-13 (headers, planned), PC-HEDT-14 (downgrade condition, planned), PC-HEDT-R05b (runtime headers). REC-HEDT-08 → PC-HEDT-08, PC-HEDT-13, PC-HEDT-R04b.

### 5.2 A1 item-class scan

| REC ID | Item | REC class | Note |
|---|---|---|---|
| REC-HEDT-40 (new) | A1 BR5 (video embeds restricted to a platform whitelist; Lane A item 18) | **GAP** | A2 R1: NOT_VERIFIED in R1 (not re-read); no case in scope. Lane B NOT_APPLICABLE |
| REC-HEDT-41 (new) | A1 BR1–BR4, §3 states, §4 exceptions, §5 handoffs | Folded into REC-HEDT-18, 17, 15, 10, 14, 16, 19, 08, 13, 02, 22–24 | Anchored bullets; BR3 carries SF-07 qualification (REC-HEDT-15) |

---

## 6. `mail`

### 6.1 A3-D1: zip wording reconciled across REC-28, REC-52 and REC-delta CF-2 — AGREE

Parent REC section 2.3 ("Attachment zip route has no guest context"), REC-28 basis, REC-52 ("zip lacks it") and REC-delta D1 CF-2 ("zip carries none and browses ids with no module check"; "zip access is decided entirely in base binary streaming") are each literally true **at module level**. The overstatement is reading "no module-level check" as "unchecked". **R1 net statement (REC-MAIL-28, REC-MAIL-D1-13, REC-MAIL-D1-20, REC-52):** "The zip route has no guest-context decorator and no module-level access check. Base binary streaming reads each attachment's stored fields in the request environment, and that ORM read applies the attachment access filter (public read allowed; linked attachments filtered by access to the linked record; unlinked attachments only for system users or their creator) and raises an access error for any forbidden id, which aborts the whole zip. Static prediction: fail-closed for unauthorised callers and for token-bearing guests (who lose their guest context on this route). Runtime decides (PC-MAIL-04)." Classes unchanged: REC-28 CONTRADICTION (A1 vs A2 on guest context); CF-2 resolution for base A2 stands and is consistent with this wording.

### 6.2 A3-D2: company-context restatements

| REC item | Parent risk wording | **R1 risk wording** | Class | Position |
|---|---|---|---|---|
| **REC-MAIL-09** (C09/G9) | Effect of an empty context decided in base, runtime | "The thread-access helper checks access in non-superuser mode with an empty company context, which base resolves to **all of the acting user's companies** (active or not), never beyond them. G9 CLOSED-STATIC. Residual runtime question: whether posting/attaching in an inactive-but-allowed company is intended (PR-02R1)" | UNKNOWN_PENDING_PROOF (unchanged) | AGREE |
| **REC-MAIL-11** (C11) | Payload effect across companies is runtime | Split. **(a) Interactive trigger (non-superuser):** the status-push read check is bounded by the triggering user's memberships. **(b) Root queue-job trigger:** the environment is in superuser mode, the read probe returns true, and the gate passes unconditionally; exposure to the author is bounded only by what serialisation under the author's user reads (CH-1c). The narrowing in A3 CH-1b applies to (a) only | UNKNOWN_PENDING_PROOF (unchanged) | **DISPUTED in part** (A2 R1 6.3): A3's narrowing is accepted for (a) and not for (b) |
| REC-MAIL-38 (O4/SF-05) | Identity mismatch; runtime | Same split as REC-MAIL-11; (b) is the SF-05 path and is **not** narrowed | UNKNOWN_PENDING_PROOF (unchanged) | as REC-11 |
| **REC-MAIL-33** (K3) | Emptying sites widen context | "Each emptying site that runs in non-superuser mode widens evaluation to the user's full company membership, not beyond it" | MATCH (unchanged) | AGREE |
| **REC-MAIL-43** (O7a/SF-08) | Base validation of cookie ids is runtime | "A forged cookie naming a company outside the user's membership raises an access error when the company set is evaluated and falls to the generic fallback; the widened set is written only after a successful non-superuser check. Risk is **cross-company within the user's membership**, not arbitrary company. Precision: validation is lazy (only when the company set is evaluated)" | UNKNOWN_PENDING_PROOF (unchanged) | AGREE (refined) |
| REC-MAIL-42 (O7b/SF-13) | Cookie company into elevated create | **Unchanged**: no environment is built from the cookie ids; base validation does not apply | UNKNOWN_PENDING_PROOF (unchanged) | AGREE (A3 says unaffected) |

Planned proof links: REC-09/11/33/43 → PC-MAIL-42 (base company semantics, SOURCE); REC-11/38 → PC-MAIL-44 (superuser gate path, SOURCE), PC-MAIL-05R (runtime, three outcomes); REC-28 → PC-MAIL-43 (base attachment read, SOURCE).

### 6.3 A3-D5: REC-36 and REC-45 proof requirements now exist

| REC item | R1 change |
|---|---|
| REC-MAIL-36 (O2/SF-04) | A2 R1 PR-14 → Proof R1 runtime case PC-MAIL-45. Lane B **MISSING_REQUIRED_RUNTIME_PROOF**. Parent note "A2 raised no PR, so no runtime case exists" is withdrawn |
| REC-MAIL-45 (O8/SF-11) | A2 R1 PR-15 → Proof R1 runtime case PC-MAIL-46. Lane B **MISSING_REQUIRED_RUNTIME_PROOF**. Parent note "No A2 PR exists" is withdrawn |

Other A2-origin PR revisions carried: PR-01bR1 → PC-MAIL-02R (REC-40); PR-02R1 → PC-MAIL-03R (REC-08, 09); PR-04R1 → PC-MAIL-05R (REC-11, 21, 38); PR-09R1 → PC-MAIL-10R (REC-05, 39).

### 6.4 A3-D6: A1 item-class scan and Q019

| REC ID | Item | A2 verdict | REC class | Basis | Lane B | Proof link (planned) | QID lineage (`mail`) |
|---|---|---|---|---|---|---|---|
| **REC-MAIL-57** (new) | A1 X3: status push skips records deleted without cascade | VERIFIED (A2 R1 6.6) | MATCH | Only the missing-record error is caught; in-source comment records deletion "without cascading notif". Evidence that message/notification rows can outlive their parent. Whether such orphan content remains reachable through search, inbox or links is **not** evidenced | NOT_APPLICABLE | PC-MAIL-44 (same method) | **Q019** |
| REC-MAIL-58 (new) | A1 BR1–BR10 | Anchored (A2 R1 6.6) | Folded: BR1→REC-04/05/40; BR2→REC-05/39 (CONTRADICTION via C05); BR3→REC-06; BR4→REC-12; BR5→REC-19; BR6→REC-17; BR7→REC-18; BR8→REC-23; BR9→REC-24; BR10→REC-15/27 | — | as anchors | — | as anchors |
| REC-MAIL-59 (new) | A1 X1, X2, X4–X7 | Anchored | Folded: X1→REC-20/21; X2→REC-23; X4→REC-09/34; X5→REC-13; X6→REC-24; X7→REC-19 | — | as anchors | — | as anchors |
| REC-MAIL-60 (new) | A1 H1–H6 | Anchored; H1 CLOSED-STATIC (A2 R1 6.2) | Folded: H1→REC-09/11; H2→REC-11; H3→REC-02/06; H4→REC-22; H5→REC-56 (G7); H6→REC-53 (G4) | — | as anchors | — | as anchors |
| REC-MAIL-61 (new) | CRQ-MAIL-09 (zip/delete by guests) — parent REC gave no disposition | Answered statically (A2 R1 6.6; 6.1 above) | Folded into REC-MAIL-28 (CONTRADICTION); byte exposure runtime | Zip fails closed at base; delete needs ownership | UNCORROBORATED + MISSING_REQUIRED_RUNTIME_PROOF | PC-MAIL-43; PC-MAIL-04 | Q014 |
| REC-MAIL-62 (new) | CRQ-MAIL-01..08, 10–12 dispositions | Carried as in REC delta D1 rows D1-17..D1-22 (CRQ-01, 05, 07, 11; 02, 03, 04, 06, 08, 10, 12); CRQ-01/02 narrowed per 6.2 for interactive paths only | Carried | — | as D1 | as D1 | as D1 |
| REC-MAIL-23 (R1 lineage add) | C23 route resolution (reply thread, alias, fallback) | VERIFIED (parent) | MATCH (unchanged) | Topical lineage for deterministic threading; disconfirming observation not tested | UNCORROBORATED | — | adds **Q026** |

### 6.5 A3-D7 (process) — acknowledged

The parent REC cited Stage-2 Proof results in its Basis column and was committed after the Proof checkpoint. This R1 addendum cites only already-frozen parent Proof results, is hashed before the Proof R1 predeclaration, and its sha256 is pinned in the Proof R1 header.

---

## 7. Rule 3 — A1 item-class scan record (all five modules)

| Module | A1 classes scanned | Items not carried by parent REC before R1 | Now carried at |
|---|---|---|---|
| web | Claims C01–C24; BR-1..5; §3 states; §4 exceptions; §5 handoffs; G-1..G-5, G-A1-1..4; CRQ-WEB-01..08; X-WEB-01/02; plus A1/Lane A notes A1N-WEB-01..04 | BR-1, BR-4, BR-5; states; §4 export-failure exception and other exceptions; handoffs; notes | REC-WEB-R1-01..11 |
| web_tour | Claims C01–C15; BR-1..5; states; exceptions; handoffs; G-1..G-4, G-A1-1/2; CRQ-WTOUR-01..05; contradictions (none); notes A1N-WTOUR-01/02 | BR, states, exceptions, handoffs; notes | REC-WTOUR-25..27 |
| http_routing | Claims C01–C18; BR1–BR5; states; exceptions; handoffs; EG1–EG4; CRQ-HROU-01..06; X-HROU-01/02; notes A1N-HROU-01/02 | BR1–BR5 (BR5 is a contradiction with A2), states, exceptions (Lane A item 16), handoffs; notes | REC-HROU-28..31 (+ REC-HROU-19 basis) |
| html_editor | Claims C01–C21; BR1–BR5; states; exceptions; handoffs; EG1–EG7; CRQ-HEDT-01..09; X-HEDT-01..04 | BR1–BR5, states, exceptions, handoffs | REC-HEDT-40, 41 |
| mail | Claims C01–C30; BR1–BR10; states; X1–X7; H1–H6; G1–G11; CRQ-MAIL-01..12; K1–K4 | BR1–BR10, X1–X7, H1–H6, CRQ-MAIL-09 (no disposition) | REC-MAIL-57..62 |

---

## 8. Recomputed QID lineage ("no evidence" lists; lineage only, no QID answered)

| Module | Mapped before R1 | Changes in R1 | **No evidence after R1** |
|---|---|---|---|
| web (W1-B01; base 26 + D1 3 = 29 mapped) | 29 | +Q042 (REC-WEB-R1-01), +Q015 (REC-WEB-R1-04); additional evidence on Q046 (R1-02), Q034 (R1-03), Q030/Q050 (R1-05) | **19**: Q002, Q006, Q007, Q009, Q018, Q020, Q021, Q023, Q024, Q026, Q028, Q029, Q038, Q039, Q040, Q041, Q043, Q044, Q049. Mapped **31** |
| web_tour (W1-B05) | 34 | +Q033 (REC-WTOUR-25), +Q016 (REC-WTOUR-26, partial) | **4**: Q022, Q036, Q037, Q038. Mapped **36** |
| http_routing (W1-B08; PROVISIONAL) | 36 | +Q006 (REC-HROU-29), +Q008 (REC-HROU-28) | **2** (provisional): Q020, Q025. Mapped **38** (provisional). Q020 was considered: language is resolved in the match step, but whether route-bound record arguments are converted before or after it was not read; not mapped |
| html_editor (W1-B07; PROVISIONAL) | 13 | None. Scan of BR/states/exceptions/handoffs found no evidence for the 27 client-side QIDs beyond items already mapped; BR1 (server-side sanitisation) was considered for Q014/Q034 and not mapped because those QIDs concern client paste/format behaviour (JS out of scope, EG6) | **27** (unchanged; provisional) |
| mail (W1-B01; base 33 + D1 = 34 mapped) | 34 | +Q019 (REC-MAIL-57), +Q026 (REC-MAIL-23) | **14**: Q012, Q013, Q015, Q016, Q020, Q028, Q029, Q034, Q039, Q040, Q042, Q046, Q047, Q049. Mapped **36** |

Q-sums check: web 31 + 19 = 50; web_tour 36 + 4 = 40; http_routing 38 + 2 = 40; html_editor 13 + 27 = 40; mail 36 + 14 = 50.

---

## 9. Handoff and freeze

- To: PROOF R1 (`G01_PROOF/G01_B3B_PROOF_ADDENDUM_R1_20260927.md`). Planned case IDs named above are links only; their text is declared by Proof R1.
- This file is **frozen** at close. Its sha256 is computed after close and recorded in the Proof R1 predeclaration record and header. Any later change would be a new addendum.

## 10. Limitations

- Classes rest on A1, A2, A2 R1 and already-frozen parent Proof results. No runtime evidence exists; no Proof R1 result is cited.
- QID changes for http_routing and html_editor are provisional until canonical re-freeze of W1-B08 and W1-B07.
- QID mapping is controller-judged topical lineage, not coverage. No Formal Coverage, no percentages, no git operations, no existing artifact edited.
