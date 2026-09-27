# G01 PLATFORM_BASE — RED TEAM Reconciliation (REC) — `base_automation`

## 0. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RECONCILIATION controller (Stage 1 of a two-stage REC + PROOF run; Stage 2 is recorded separately in `G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md`) |
| Group / Module | G01 PLATFORM_BASE / `base_automation` |
| Date | 2026-09-27 |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/base_automation/` |
| Question bank | `GMVQ/G01_PLATFORM_BASE/G01_BASE_AUTOMATION_GMVQ_MVQ_40_V1.00_DRAFT.md`, sha256 `3c38cec4aa1ef2aa92d0e850da0d18242da9dc7c6ef7bd137c433edb379b9a49`. This **equals** the value in `FREEZE_W1-B02.json` (bank_files entry). Freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`. W1-B02 is ELIGIBLE per `QUESTION_GATE_G01_FREEZE_REPLAY_20260927.md` |
| Join key | MODULE `base_automation` + QID + freeze hash above. The mapping is lineage only. **No QID is answered here** |
| **Disposition** | **REC COMPLETE — HANDOFF TO PROOF** (46 REC items; 5 CONTRADICTION items carried into Proof, none closed by REC) |

### 0.1 Input intake (immutable; sha256 recorded at intake, 2026-09-27 ~14:57 UTC)

Paths are relative to `COMMUNITY19/A1_SOURCE_EVIDENCE_LANE/`.

| Input | Path | sha256 | Cross-check |
|---|---|---|---|
| A1 package | `G01_A1_PACKAGES/G01_BASE_AUTOMATION_A1_PACKAGE_20260927.md` | `f01dec29aeb323747b288b4ef3687acad4e5deefdddc10d7422fa4fac6297007` | Matches the A1 hash recorded in the A2 header |
| A2 review | `G01_A2_REVIEWS/G01_BASE_AUTOMATION_A2_REVIEW_20260927.md` | `bf95295f2d53891c8358422a8a3b5179e50bc44fa028a8be19be6c2a72bd4208` | Disposition "A2 PASS WITH FINDINGS". It lists 27 proof requirements (PR-01..PR-27) |
| Lane A packet | `G01_LANE_A_PASS1/G01_BASE_AUTOMATION_LANE_A_PASS1_20260927.md` | `8656751d9142e0b59c433454558cef5e57b7c4f089bf42c04cf2a280b18ec058` | Matches the hash recorded in both the A1 and A2 headers |
| base A1 package | `G01_A1_PACKAGES/G01_BASE_A1_PACKAGE_20260927.md` | — | **NOT PRESENT** at intake, so it was not used |
| base Lane A (fallback for server-action execution identity) | `G01_LANE_A_PASS1/G01_BASE_LANE_A_PASS1_20260927.md` | `9108bd4f64762c79f763a35c9d6e944153bd7eec5c0fad3bda9d0eadcd59403b` | Status "LANE A PASS-1 COMPLETE". Used items 21, 30, 32 and 38 (38 addresses base_automation Gap G4 at source level) |
| Question bank | see header | `3c38cec4…9a49` | Equals the FREEZE_W1-B02 entry |
| FREEZE manifest | `../GMVQ/G01_PLATFORM_BASE/FREEZE_W1-B02.json` | `bccaa2e1a0006429ff60ce7c9790862ea2e49d589da5d9a7919923b7cd504a2b` | freeze_hash `cd966040…0202` |

### 0.2 Lane B evidence-pool search (recorded)

- Command: `grep -ril base_automation /home/user/AI-Collaboration-Hub/99_SMEsPlus_Enterprise_Suite`. It returned 38 files: the A1, A2 and Lane A artifacts for this module; the base Lane A; G01 static-intake and checkpoint files; GMVQ freeze/manifest/status files; and inventory CSVs under `02_Functional_Design`, `03_Architecture`, `07_Output_From_AI` and `V2.0/THAI/.../Evidence_CSV` (dump/ORM inventories, which are not runtime observations).
- Filtering those hits for `lane_b|laneb|gemini|runtime|evidence_pool|observ` returned **no match** (rc=1).
- `find` for files named `*lane_b*`, `*gemini*` or `*evidence_pool*` returned **no files**.
- Conclusion: **no Lane B / Gemini runtime evidence exists for `base_automation`**. That absence is not a failure. Every item's Lane B column is UNCORROBORATED or NOT_APPLICABLE.

Clean-room note: every statement is a neutral WHAT/WHY/RISK paraphrase. Identifiers are evidence pointers only. No vendor code is reproduced, and nothing recommends reusing vendor schema, ORM, workflow, UI or naming. No percentages. No Formal Coverage claim. No git operations. Inputs were not edited.

## 1. Classification rules (predeclared)

- **MATCH**: A1 and A2 agree, and a source re-read supports the claim. Runtime corroboration may be optional; it is not required to hold the claim.
- **GAP**: evidence is missing, and no static or runtime proof in scope can settle it now.
- **CONTRADICTION**: A1 and A2 disagree (A2 PARTIAL correction), or the source disagrees with the design intent the source itself declares (help text, docstring, UI exposure).
- **UNKNOWN_PENDING_PROOF**: A1 and A2 agree at source level, but the claim or its stated risk is inherently runtime or config-dependent (A2 label MISSING_REQUIRED_RUNTIME_PROOF, or an A2 omission that is only predicted statically).
- **Lane B column**: UNCORROBORATED (behavioural, with no runtime observation) or NOT_APPLICABLE (declarative or structural, or a source-only gap). It is never FAIL for absence.
- **Scope of REC items**: A1 claims C01–C24; A2 omissions O1–O17 as new REC items; and carried A1 gaps that no claim or omission absorbs (G1, G2, G3, G5, G6). G4, G7, G8, G9, G10 and G11 are folded into their linked items: G4→C11, G7→O13, G8→O14, G9→C09, G10→O15, G11→O12. A1 BR/State/F items are covered through their claims (BR5 PARTIAL → O1).

## 2. Reconciliation table

PC = proof case in the PROOF package. The static cases (PC-BAUT-28..55) were executed. The runtime cases (PC-BAUT-01..27) are pending.

| REC ID | Item | A1 (claim / conf.) | A2 verdict | REC class | Basis for class | Lane B | Proof link | QID lineage (MODULE `base_automation`) |
|---|---|---|---|---|---|---|---|---|
| REC-BAUT-01 | C01 | Admin rules run server actions on any non-abstract model / HIGH | VERIFIED | MATCH | Target model restricted to non-abstract; trigger set as stated | UNCORROBORATED | — | — (general scope) |
| REC-BAUT-02 | C02 | Deps base, digest, resource, mail, sms; sms manifest-only / HIGH | VERIFIED | MATCH | Manifest re-read. Among module files, sms appears only in the manifest (PC-BAUT-55). Reason still open (see REC-BAUT-44) | NOT_APPLICABLE | PC-55 | — |
| REC-BAUT-03 | C03 | Rules are tracked records; tracking only on some fields / MED | VERIFIED | MATCH | Tracking set confirmed (PC-43). A1's RISK statement is borne out by O12 | UNCORROBORATED | PC-43, PC-27 (optional) | Q031, Q040 |
| REC-BAUT-04 | C04 | Trigger taxonomy (18 values) / HIGH | VERIFIED | MATCH | Selection re-read | NOT_APPLICABLE | — | Q038 |
| REC-BAUT-05 | C05 | Convention-based field resolution; empty when no match / HIGH | VERIFIED (A2 strengthens: an empty watched set means any write fires) | MATCH | A2 strengthens A1's RISK without disagreeing with it | UNCORROBORATED | — | Q030 |
| REC-BAUT-06 | C06 | Runtime patching; registry re-registration on rule change / HIGH | VERIFIED (+O9 refinement) | UNKNOWN_PENDING_PROOF | Effect on in-flight work and on other workers is runtime-only | UNCORROBORATED | PC-45; PC-23, PC-25 | Q006, Q007 |
| REC-BAUT-07 | C07 | Before-condition pre-write, apply-on post-write; create/delete apply-on only; watched-field gate / HIGH | VERIFIED (+O8) | MATCH | Write, recompute, create and unlink paths re-read | UNCORROBORATED | — | Q038 |
| REC-BAUT-08 | C08 | Message-trigger skip set; received/sent classification / HIGH | VERIFIED | MATCH | Skip set includes auto-comment and user-notification types | UNCORROBORATED | PC-19 (breadth) | Q038 |
| REC-BAUT-09 | C09 (+G9) | Per-rule, per-record, in-context recursion guard; no cross-transaction dedup / HIGH | VERIFIED (+O7, S3) | UNKNOWN_PENDING_PROOF | Actual recursion bound and duplicate effects across transactions or redelivery are runtime. G9 (no idempotency key) confirmed statically (PC-51) | UNCORROBORATED | PC-48, PC-51; PC-09, PC-10 | Q003, Q004, Q010 |
| REC-BAUT-10 | C10 | Each action per matching record; last-automation stamp / HIGH | VERIFIED (+O16) | MATCH | Loop order: per action, then per record | UNCORROBORATED | — | Q016 |
| REC-BAUT-11 | C11 (+G4) | Lookup, filters and action list elevated; final identity outside module / HIGH (sudo) / LOW (identity) | VERIFIED (LOW part stands) | UNKNOWN_PENDING_PROOF | Source-level identity now traced through base Lane A item 38 and PC-40. Actions run from an elevated collection, and the base run path evaluates in that elevated environment with the triggering uid. Runtime confirmation required | UNCORROBORATED | PC-40; PC-01, PC-02 | Q002, Q013, Q015, Q016, Q038 |
| REC-BAUT-12 | C12 | Restricted evaluator; server-action context gains JSON helper and request payload / HIGH | **PARTIAL** — JSON/payload only for code actions; payload injected on any HTTP request carrying data, not only webhooks | **CONTRADICTION** (A1 vs A2) | A1's scope differs from A2's. The source re-read supports A2's correction (PC-44 PASS). Both statements are preserved. Runtime exposure pending | UNCORROBORATED | PC-44; PC-26 | Q015, Q038 |
| REC-BAUT-13 | C13 | Domain fields extracted by pattern, not evaluation / HIGH | VERIFIED | MATCH | In-source rationale re-read | NOT_APPLICABLE | — | Q015 |
| REC-BAUT-14 | C14 | Public unauthenticated CSRF-exempt session-less webhook, GET+POST, per-rule random id, generic responses / HIGH | VERIFIED (+O1 material omission) | UNKNOWN_PENDING_PROOF | Route attributes confirmed statically (PC-54, PC-29, PC-30). Endpoint behaviour, rotation effect and absence of rate limiting are runtime | UNCORROBORATED | PC-29, PC-30, PC-54; PC-02, PC-05, PC-06 | Q015, Q029 |
| REC-BAUT-15 | C15 | Webhook calls/payload/tracebacks logged elevated when enabled; no retention / HIGH | VERIFIED | MATCH | Conditional, elevated log writes; payload also always at debug level (PC-31) | UNCORROBORATED | PC-31; PC-07 (optional) | Q034 |
| REC-BAUT-16 | C16 | Admin-only ACL; no record rules; dev-mode hiding is not a boundary / HIGH | VERIFIED | MATCH | Single ACL row, no record-rule file, no company field (PC-42) | UNCORROBORATED | PC-42; PC-22 (company scope) | Q001, Q022, Q031, Q032 |
| REC-BAUT-17 | C17 | Six constraints / HIGH | VERIFIED | MATCH | All six re-read | UNCORROBORATED | PC-52 (on-change subset) | — |
| REC-BAUT-18 | C18 | Duplicate copies actions, not id/last-run; active not reset / MED | VERIFIED | UNKNOWN_PENDING_PROOF | Copy flags confirmed (PC-37). Whether the copy is active and doubles the effect is runtime (ORM copy semantics live in base) | UNCORROBORATED | PC-37; PC-18 | Q021 |
| REC-BAUT-19 | C19 | Time window last-run→now shifted; calendar; "after last update" falls back to creation date / MED | **PARTIAL** — fallback only for the last-automation field; "after last update" uses write-date with no fallback; first-run catch-up omitted | **CONTRADICTION** (A1 vs A2) | A1 and A2 disagree on the fallback scope. The source re-read supports A2 (PC-50 PASS). Both statements are preserved | UNCORROBORATED | PC-49, PC-50; PC-11, PC-14, PC-15, PC-16 | Q008, Q011, Q012, Q018 |
| REC-BAUT-20 | C20 | Per-rule rollback/commit; last-run advanced only on success; last error re-raised / HIGH | VERIFIED (+O3) | UNKNOWN_PENDING_PROOF | Mechanism confirmed statically (PC-34). External side effects and stall behaviour are runtime | UNCORROBORATED | PC-34; PC-12, PC-13 | Q009, Q010, Q012, Q014, Q034, Q037, Q039 |
| REC-BAUT-21 | C21 | Single job, inactive, 4 h, no-update; auto-activation; interval about a tenth of the shortest delay, bounded 1 min–4 h / HIGH | VERIFIED (+O10) | MATCH | Config re-read (PC-35, PC-36). The docstring-vs-code conflict is carried separately as REC-BAUT-34 | UNCORROBORATED | PC-35, PC-36; PC-17 (optional) | Q012, Q023 |
| REC-BAUT-22 | C22 | Rule context attached to errors for internal users only / HIGH | VERIFIED | MATCH | Always re-raised (PC-46) | UNCORROBORATED | PC-46; PC-24 | Q009, Q040 |
| REC-BAUT-23 | C23 | Server-action extension: usage, back-link, child exclusion, navigation / HIGH | VERIFIED | MATCH | Re-read | NOT_APPLICABLE | — | — |
| REC-BAUT-24 | C24 | Message path evaluates only the before-condition; apply-on ignored; before-condition auto-cleared but dev-editable / HIGH (path) | VERIFIED — contradiction candidate confirmed at source | **CONTRADICTION** (source vs design intent) | Declared intent: the apply-on help text says it must be satisfied before execution, and the developer-mode form exposes the apply-on editor for message triggers (PC-39). The message path never applies it (PC-38). Practical effect is runtime | UNCORROBORATED | PC-38, PC-39; PC-03 | Q038 |
| REC-BAUT-25 | O1 | (A1 omitted; A1 BR5 framed webhook access as the identifier match) | O1 HIGH — webhook lookup does not check trigger type | **CONTRADICTION** (source vs design intent) | Declared intent: the secret URL is computed and shown only for webhook-trigger rules. The endpoint resolves any active rule by identifier (PC-28). A2 BR5 is PARTIAL | UNCORROBORATED | PC-28; PC-04 | Q015, Q038 |
| REC-BAUT-26 | O2 | (not stated) | O2 HIGH — never-run time rule catches up from the epoch | UNKNOWN_PENDING_PROOF | Epoch fallback confirmed statically (PC-33). Retroactive mass execution is a runtime effect | UNCORROBORATED | PC-33; PC-11 | Q008, Q012 |
| REC-BAUT-27 | O3 | (not stated; C20 RISK partial) | O3 HIGH — one poison record stalls a time rule | UNKNOWN_PENDING_PROOF | Last-run is written only on success (PC-34). Stall is runtime | UNCORROBORATED | PC-34; PC-12 | Q009, Q014, Q034 |
| REC-BAUT-28 | O4 | (not stated) | O4 MED — UI-change rules run on unsaved edits for any editor | UNKNOWN_PENDING_PROOF | Code-only restriction and UI warning confirmed (PC-52). Persistence of side effects is runtime | UNCORROBORATED | PC-52; PC-20 | Q015 |
| REC-BAUT-29 | O5 | (see C12) | O5 MED — payload injected into code actions on any data-carrying HTTP request | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-44). Exposure outside webhooks is runtime | UNCORROBORATED | PC-44; PC-26 | Q015, Q038 |
| REC-BAUT-30 | O6 | (not stated) | O6 HIGH — default record-getter: caller chooses model and id; elevated lookup; status-code oracle | UNKNOWN_PENDING_PROOF | Payload-derived getter and elevated evaluation environment confirmed (PC-32) | UNCORROBORATED | PC-32; PC-08 | Q015 |
| REC-BAUT-31 | O7 | (C09 partial) | O7 MED — message rules suppressed whenever the guard marker is present (time job; create/write on models with rules) | UNKNOWN_PENDING_PROOF | Early exit on marker and marker set by the job confirmed (PC-47) | UNCORROBORATED | PC-47; PC-19 | Q003, Q038 |
| REC-BAUT-32 | O8 | (F3 partial) | O8 MED — delete-rule actions run before deletion; failure aborts delete | UNKNOWN_PENDING_PROOF | Ordering confirmed (PC-46) | UNCORROBORATED | PC-46; PC-24 | Q009 |
| REC-BAUT-33 | O9 | (C06 partial) | O9 MED — re-registration only on critical fields, never under file import | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-45) | UNCORROBORATED | PC-45; PC-25 | Q006, Q023 |
| REC-BAUT-34 | O10 | (C21) | O10 LOW — interval only ever shortened, against the docstring; silent skip on lock failure | **CONTRADICTION** (source vs design intent) | The method's own docstring says the default 4 hours is restored when no time rule exists. The code only shortens (PC-36 PASS for the code behaviour) | UNCORROBORATED | PC-36; PC-17 | Q012 |
| REC-BAUT-35 | O11 | (C19 partial) | O11 MED — window-crossing semantics; apply-on evaluated at job time; date fields compared with the job-clock date | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-49) | UNCORROBORATED | PC-49; PC-14, PC-15 | Q011, Q018 |
| REC-BAUT-36 | O12 (+G11) | (C03 RISK; G11) | O12 MED — no tracking on active, conditions, actions, calendar, getter, log toggle, identifier | MATCH | A2 settles A1's G11 in the direction of A1's C03 RISK. Source-supported (PC-43) | UNCORROBORATED | PC-43; PC-27 (optional) | Q031, Q040 |
| REC-BAUT-37 | O13 (+G7) | (G7) | O13 LOW — inactive rule invisible to webhook; job re-checks active/existence per rule | UNKNOWN_PENDING_PROOF | Confirmed statically (PC-30, PC-53). Synchronous in-flight behaviour remains unevidenced | UNCORROBORATED | PC-30, PC-53; PC-06, PC-23 | Q006, Q007, Q035 |
| REC-BAUT-38 | O14 (+G8) | (C16 RISK; G8) | O14 MED — conditions evaluated on superuser-visible data | UNKNOWN_PENDING_PROOF | Elevated filtering confirmed; no company field (PC-42). Cross-company effect is runtime | UNCORROBORATED | PC-42; PC-22 | Q001, Q002, Q013, Q022 |
| REC-BAUT-39 | O15 (+G10) | (G10) | O15 LOW — no ordering attribute | UNKNOWN_PENDING_PROOF | Absence confirmed (PC-41). Effective order is set by base ORM default | UNCORROBORATED | PC-41; PC-21 | Q005, Q036 |
| REC-BAUT-40 | O16 | (not stated) | O16 LOW — last-automation stamp written before actions; may trigger other write rules | UNKNOWN_PENDING_PROOF | Ordering confirmed (PC-48) | UNCORROBORATED | PC-48; PC-09 | Q003 |
| REC-BAUT-41 | O17 | (not stated) | O17 LOW (observation) — (a) date-type fallback upper bound not shifted; (b) multi-rule copy assigns actions collectively | UNKNOWN_PENDING_PROOF | (a) Source refinement: the bound uses the process-local current date-time rather than the shifted bound used in the sibling branches. (b) Collective assignment confirmed. Neither is asserted as a defect | UNCORROBORATED | PC-16, PC-18 | Q021 |
| REC-BAUT-42 | G1 | JS/static assets and tests not inspected | VERIFIED as gap | GAP | Nothing in scope reads them | NOT_APPLICABLE | — | — |
| REC-BAUT-43 | G3 | Parent menu group gating lies in base | VERIFIED as gap | GAP | Base menu data not read in this lineage | NOT_APPLICABLE | — | Q032 |
| REC-BAUT-44 | G2 | Reason for the sms dependency unevidenced | VERIFIED as gap | GAP | Only the manifest references it | NOT_APPLICABLE | — | — |
| REC-BAUT-45 | G5 | Tests directory not read | VERIFIED as gap | GAP | — | NOT_APPLICABLE | — | — |
| REC-BAUT-46 | G6 | Absence of i18n, migrations and reports not proven | VERIFIED as gap | GAP | — | NOT_APPLICABLE | — | Q023 |

### 2.1 Class counts

| Class | Count | Items |
|---|---|---|
| MATCH | 16 | C01, C02, C03, C04, C05, C07, C08, C10, C13, C15, C16, C17, C21, C22, C23, O12 |
| CONTRADICTION | 5 | C12 (A1 vs A2), C19 (A1 vs A2), C24 (source vs intent), O1 (source vs intent), O10 (source vs intent) |
| UNKNOWN_PENDING_PROOF | 20 | C06, C09, C11, C14, C18, C20, O2, O3, O4, O5, O6, O7, O8, O9, O11, O13, O14, O15, O16, O17 |
| GAP | 5 | G1, G2, G3, G5, G6 |
| **Total** | **46** | 24 A1 claims + 17 A2 omissions + 5 carried gaps |

Lane B column: UNCORROBORATED 37, NOT_APPLICABLE 9 (C02, C04, C13, C23, G1, G2, G3, G5, G6). There is no FAIL for absence.

### 2.2 Contradiction handling (both sources preserved)

- C12 and C19: A1's statement and A2's correction are both kept verbatim in their packages. REC does not rewrite A1. The static re-read executed in Proof (PC-44, PC-50) supports A2's narrower or corrected scope. The items stay CONTRADICTION until A3 reviews them.
- C24, O1 and O10: the source conflicts with intent the source itself declares. REC does not judge whether these are defects, because they are behaviours of the reference ERP and are research findings only. Each has a runtime case (PC-03, PC-04, PC-17) that is pending.

## 3. QID lineage map (frozen bank; lineage only, not answers)

Join key: MODULE `base_automation` + QID + freeze hash `cd966040f720456420057fe98fdb1176fbb9b0e85b456891f4dab82ea3ba0202`. A mapping means "this REC item is topically relevant evidence for the question". It does not answer the QID or satisfy any disconfirming observation.

| QID | Topic (paraphrased) | Mapped REC items |
|---|---|---|
| G01-BASE_AUTOMATION-Q001 | Single scope per run | REC-16 (C16), REC-38 (O14) |
| G01-BASE_AUTOMATION-Q002 | Authority revalidated at write | REC-11 (C11), REC-38 (O14) |
| G01-BASE_AUTOMATION-Q003 | Bounded recursion | REC-09 (C09), REC-31 (O7), REC-40 (O16) |
| G01-BASE_AUTOMATION-Q004 | Duplicate delivery | REC-09 (C09/G9) |
| G01-BASE_AUTOMATION-Q005 | Multi-rule ordering | REC-39 (O15) |
| G01-BASE_AUTOMATION-Q006 | Config change mid-batch | REC-06 (C06), REC-33 (O9), REC-37 (O13) |
| G01-BASE_AUTOMATION-Q007 | Disable and queued work | REC-06 (C06), REC-37 (O13) |
| G01-BASE_AUTOMATION-Q008 | Re-enable replay / catch-up | REC-19 (C19), REC-26 (O2) |
| G01-BASE_AUTOMATION-Q009 | Failure rollback / partial success | REC-20 (C20), REC-22 (C22), REC-27 (O3), REC-32 (O8) |
| G01-BASE_AUTOMATION-Q010 | Idempotent retry | REC-09 (C09), REC-20 (C20) |
| G01-BASE_AUTOMATION-Q011 | Time-zone/date rule | REC-19 (C19), REC-35 (O11) |
| G01-BASE_AUTOMATION-Q012 | Downtime catch-up | REC-19 (C19), REC-20 (C20), REC-21 (C21), REC-26 (O2), REC-34 (O10) |
| G01-BASE_AUTOMATION-Q013 | Per-record authorization in batch | REC-11 (C11), REC-38 (O14) |
| G01-BASE_AUTOMATION-Q014 | Partial batch outcome | REC-20 (C20), REC-27 (O3) |
| G01-BASE_AUTOMATION-Q015 | Untrusted input escalation | REC-11, REC-12, REC-13, REC-14, REC-25 (O1), REC-28 (O4), REC-29 (O5), REC-30 (O6) |
| G01-BASE_AUTOMATION-Q016 | Recorded actor / provenance | REC-10 (C10), REC-11 (C11) |
| G01-BASE_AUTOMATION-Q018 | Delayed action re-evaluates state | REC-19 (C19), REC-35 (O11) |
| G01-BASE_AUTOMATION-Q021 | Duplicated rule double effect | REC-18 (C18), REC-41 (O17) |
| G01-BASE_AUTOMATION-Q022 | Cross-company copy | REC-16 (C16), REC-38 (O14) |
| G01-BASE_AUTOMATION-Q023 | Upgrade preserves state | REC-21 (C21), REC-33 (O9), REC-46 (G6) |
| G01-BASE_AUTOMATION-Q029 | Rate/abuse controls | REC-14 (C14; A2 CRQ-03: no rate limiting in module) |
| G01-BASE_AUTOMATION-Q030 | Prerequisite removal fails visibly | REC-05 (C05) |
| G01-BASE_AUTOMATION-Q031 | Config audit trail | REC-03 (C03), REC-16 (C16), REC-36 (O12) |
| G01-BASE_AUTOMATION-Q032 | Rule config as escalation path | REC-16 (C16), REC-43 (G3) |
| G01-BASE_AUTOMATION-Q034 | Run reconciliation evidence | REC-15 (C15), REC-20 (C20), REC-27 (O3) |
| G01-BASE_AUTOMATION-Q035 | Cancel queued action | REC-37 (O13) |
| G01-BASE_AUTOMATION-Q036 | Priority change | REC-39 (O15) |
| G01-BASE_AUTOMATION-Q037 | Downstream outage false success | REC-20 (C20) |
| G01-BASE_AUTOMATION-Q038 | Equivalent paths, equal controls | REC-04, REC-07, REC-08, REC-11, REC-12, REC-24 (C24), REC-25 (O1), REC-29 (O5), REC-31 (O7) |
| G01-BASE_AUTOMATION-Q039 | Restart coherence | REC-20 (C20) |
| G01-BASE_AUTOMATION-Q040 | Trace to rule version and trigger | REC-03 (C03), REC-22 (C22), REC-36 (O12) |

**Mapped: 31 QIDs.** **No evidence yet: 9 QIDs**, namely Q017 (concurrent manual/automated update), Q019 (archived/inactive records), Q020 (target deleted before deferred execution), Q024 (snapshot restore replay), Q025 (cloned environments outbound), Q026 (notification recipient re-authorization), Q027 (unique identifiers under concurrency), Q028 (trigger-storm capacity isolation) and Q033 (financial approval/execution/posting separation). No mapping answers a QID.

## 4. Handoff

- To: PROOF (Stage 2, same run, separate record): `G01_PROOF/G01_BASE_AUTOMATION_PROOF_20260927.md`.
- Proof must address the 20 UNKNOWN_PENDING_PROOF items and the 5 CONTRADICTION items. The 5 GAP items are not closable by Proof in this scope and are carried forward.

## 5. Limitations

- REC used only the immutable inputs listed in 0.1 and, for classification support, the static proof results from Stage 2. No runtime evidence exists.
- The base A1 package was absent. Execution identity rests on base Lane A (source-level) plus a cross-module static case. It is not a runtime conclusion.
- QID mapping is topical lineage judged by this controller. It is not a coverage measure, and no Formal Coverage claim is made. No percentages.
