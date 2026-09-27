# G01 PLATFORM_BASE — Module `privacy_lookup` — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL scope)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, independent adversarial challenger. A3 did not author Lane A, A1, A2, REC or Proof for this module. |
| Group / module | G01 PLATFORM_BASE / `privacy_lookup` |
| Date | 2026-09-27 (intake 15:16:17 UTC; first A3 source fetch 15:16:53 UTC) |
| Scope | STATIC, **claim-level only**. QID lineage is **NOT A3-eligible** (W1-B11 DELTA-RECHECK, non-canonical freeze). A3 did not challenge or accept the QID map. Runtime NOT-EXECUTED: neither passed nor failed. |
| Intake hashes (A3 recomputed; scratchpad `a3_phon_priv/intake.sha256`, sha256 `49747416…4888`) | Lane A `35ccba82…e99`; A1 `61524ebc…056a`; A2 `e10a3a06…aee9`; REC `86a047dc…c41a`; Proof `8fe1bd60…4b23`. All equal the upstream-recorded values and the REC/Proof output log. |
| Source anchor | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`. A3 fetched independently; blob log `a3_phon_priv/blob_log.txt` (sha256 `d720c3c7…14b8`). |
| Lane B | None exists for this module (REC 0.2). Not used by A3. |
| **Overall disposition** | **A3 STATIC PASS WITH DEFECTS (CLAIM-LEVEL) (route to A2, PROOF, REC) — MASTER HANDOFF PENDING RUNTIME + RE-FREEZE.** No challenge overturned a verdict. Sustained challenges are LOW/precision items. |

Clean-room note: neutral paraphrase only. Identifiers are evidence pointers. No vendor code, query text, schema or workflow reproduced. No percentages. No Formal Coverage claim. Git used read-only. Inputs not edited.

## 2. Challenge log

### CH-1 Wildcard path (SF-PRIV-01 / O-PRIV-01) — **UPHELD** (refutation attempts failed); precision note sustained

Re-derivation at the anchor (wizard blob `3b6d52e0…` verified):
- The name is trimmed and bound as the right operand of a case-insensitive pattern match, with no added wildcards and no escaping. It is used in the partner reference set, the user-partner subquery and every dynamic record-name condition.
- The email is trimmed, wrapped in multi-character wildcards and bound unescaped for user logins, partner emails and every non-normalized email-like field. Normalized-email fields use equality.
- The partner reference set is "normalized email equals input OR name matches". It feeds partner results, authored-message results and every scanned model's non-cascade partner-reference condition. Conditions per model are OR-joined, so a valid email does not constrain the name branch.
- Core escape helpers exist at the anchor: one in core mail tools escapes backslash and both wildcards in email strings, and a general one exists in core SQL tools (blob `431bd6f0…`). The module calls neither.

Refutation attempts:
- **Any validation on the name?** None. It is only required and trimmed. A name that is only the multi-character wildcard matches every partner with a name.
- **Does email validation block a wildcard email?** Validation calls core normalization, which requires exactly one address found by the stdlib address parser containing "@". At the anchor, no step rejects the wildcard characters. A static reading of normalization (split via the stdlib parser, keep entries containing "@", lower-case) is enough to predict that a local part and domain made only of wildcards are accepted. The Proof harness output agrees (see CH-3).
- **Is there a company or record-rule predicate?** None. The composed statement runs directly on the cursor after a flush.

Precision note (sustained, LOW, route A2/REC wording): "whole-DB lookup under sudo" is directionally right but imprecise.
- Discovery is raw SQL on the cursor. It does not need elevation, and access and company rules never apply to it. Elevation (sudo) applies to display names, archive and delete.
- Scope is database-wide across partners, users, messages authored by matched partners, and every table-backed, non-transient model that has a non-cascade partner reference or a stored email-like field. Models with neither, and the six excluded models, are not scanned. It is not literally every table.

### CH-2 Severity of the wildcard finding — **UPHELD (premise corrected)**

The brief's premise ("A2 rates only SF-PHON-01 HIGH") applies to the phone A2. The privacy A2 already rates SF-PRIV-01 **HIGH** (and SF-PRIV-02 HIGH; O-PRIV-01 HIGH). A3 concurs with HIGH for three reasons: remediation actions run elevated and cross-company over the over-matched set; bulk delete has no confirmation (CH-5); and the log would record deletions of unrelated subjects. Mitigating factor recorded neutrally: only the system group can reach the wizard.

Proof R1 (wildcard via the email: `%@%` matches every login and non-normalized email field containing "@") is not in A2's SF-PRIV-01 text. A2 cited only single-character wildcards in email. **CHALLENGE-SUSTAINED (A2, LOW):** fold R1 into SF-PRIV-01 at HIGH. Related source-confirmed over-match without metacharacters: the underscore, which is common in real addresses, acts as a single-character wildcard. Name matching without wildcards still matches all case-insensitive homonyms.

### CH-3 PC-PRIV-12 static harness (vendor code executed under local Python 3.11.15) — **UPHELD AS SUPPLEMENTARY EVIDENCE; method deviation sustained (PROOF, LOW)**

Adjudication:
- **Clean room: compliant.** The harness file (sha256 `30988af7…b783`, verified) embeds no vendor code. At execution it reads line ranges from the scratchpad copy of core mail tools. A3 verified that the copy is byte-identical to the anchor blob `2b05c91f…` and that the ranges match exactly the two address regexes, the split helpers, the normalizer and its inner normalizer. No vendor code appears in any output. Clean-room rules govern what is reproduced in deliverables, and nothing is.
- **Static scope: tolerated only as a labelled hybrid.** Running an isolated pure function is not system runtime, and Proof labels it that way. It is still execution, not reading. It must stay tagged "static harness", be excluded from runtime tallies, and never be cited as a runtime result. Proof complies.
- **Validity at the pinned commit: partial.** The vendor code executed is anchor-exact. The outcome also depends on the stdlib address parser, which is not part of the anchor. Its strictness has changed across Python patch releases, and the governed runtime's Python version is unknown. The evidence is therefore valid for "anchor code + Python 3.11.15" only.
- For the wildcard-only inputs (`%@x.com`, `%@%`), the static reading in CH-1 independently supports the result, so the finding does not rest on the harness.
- For quoted display names containing "@", on which PC-PRIV-19's "passes validation" leans, the parser's behaviour is version-sensitive. That element is **INCONCLUSIVE statically** and must be settled by runtime PC-PRIV-07.
- **Method deviation:** the predeclared PC-PRIV-12 names a source read. The harness was written at 15:08:08, after the predeclaration hash at 15:06:04. The expected and fail conditions were predeclared; the execution method was not. Record it as a post-declaration method change (LOW).

### CH-4 C17 log-overwrite snapshot — **UPHELD (A2 side)**

Re-read: each line action assigns (replaces) a single action text. The wizard's stored details are recomputed as the join of current line texts. The log helper creates a log only when none exists and details are non-empty. Otherwise it assigns the wizard's details and found-records to the existing log (overwrite), with no emptiness check. Re-lookup clears all lines, so the log's details become empty. A1's RISK "actions remain only in the log" is contradicted. The CONTRADICTION class is correct; the runtime effect is pending (PC-PRIV-03/04).

### CH-5 C08 bulk delete without confirmation — **UPHELD (A2 side)**

Re-read (data blob `7aac52ec…`, view blob `9d49f1db…`): the per-line Delete button carries an "irreversible" confirmation. The "Delete Selection" and "Archive Selection" server actions are plain code actions bound to the line list/kanban with no confirmation. Each delete unlinks through an elevated recordset. Whether the web client adds a generic prompt for server actions is a runtime question, not asserted here.

### CH-6 Proof static PASS re-execution (≥3) — **UPHELD**

| Case | A3 re-execution | A3 result |
|---|---|---|
| PC-PRIV-10 | Name unescaped pattern; email wildcard-wrapped unescaped; no escape clause; core helpers unused | Confirmed |
| PC-PRIV-11 | OR-combined reference set propagates to users, messages, non-cascade references | Confirmed |
| PC-PRIV-13 | Flush then direct cursor execution; no company predicate; archive/delete via sudo | Confirmed |
| PC-PRIV-14/15 | Assign-not-append at line, wizard and log; re-lookup blanks log details | Confirmed |
| PC-PRIV-16 | Per-line confirm present; bulk actions have none | Confirmed |
| PC-PRIV-18 | Email masker returns (does not raise) an error object for empty/"@-less" input | Confirmed |
| PC-PRIV-20 | ACL: wizard system CRUD; line no unlink; log system full CRUD | Confirmed |

Weak conditions: PC-PRIV-19 (see CH-3; display-name element depends on the stdlib parser version). PC-PRIV-12's fail condition covers only the local part. The `%@%` domain observation is post-hoc and correctly recorded as refinement R1 / proposed PC-PRIV-23.

### CH-7 Predeclaration timing — **UPHELD**

Predeclared file mtime 15:05:54.96. Hash record 15:06:04.872 (hash `cf3bdece…ea83` recomputed, matches). Fetch marker 15:06:04.877. First privacy source file written 15:06:08.00 (first file of the run 15:06:05.15). Order verified. The privacy Proof header wording ("fetched 15:06:05") is consistent.

### CH-8 Overclaim, Lane B, clean room, PDPA — **UPHELD with one LOW wording note (A2)**

- Lane B: none exists. REC never marks FAIL for absence. No misuse.
- Clean-room scan over the inputs: no code, query text or framework calls reproduced. Identifiers are pointers only.
- No percentages or Formal Coverage wording.
- PDPA: REC section 4 is neutral, framed as design implications, and explicitly not a legal conclusion. A2 SF-PRIV-06 ("pseudonymized, not anonymous, under GDPR/PDPA-style standards") is a legal-classification statement. Rephrase it neutrally (the masking keeps initial letters, segment lengths, TLD and common domains; legal classification is out of scope). Route A2 (LOW).
- A1 overclaim: C17 RISK already contradicted (CH-4). A1 C08 "UI asks for confirmation" is already corrected by A2. No further overclaim found.

### CH-9 QID lineage — **NOT CHALLENGED (not A3-eligible)**

W1-B11 is DELTA-RECHECK. The REC QID map is provisional and was not evaluated. GAP-PRIV-09 (freeze basis) stays routed to GMVQ/OVQDT.

## 3. Lineage

| Artifact | sha256 (A3 intake) | Commit (read-only `git log --follow`) | Working tree |
|---|---|---|---|
| Lane A PASS-1 | 35ccba82…e99 | 9f74da8 (Lane A G01 PASS-1: phone_validation, privacy_lookup) | clean |
| A1 package | 61524ebc…056a | ea16094 (message names base / mail) | clean |
| A2 review | e10a3a06…aee9 | 94de013 (message names web/web_tour/http_routing/html_editor) | clean |
| REC | 86a047dc…c41a | 61d6288 (message names web/mail delta D1) | clean |
| Proof | 8fe1bd60…4b23 | 1fb1029 (message names http_routing/html_editor) | clean |

Each stage file has a single commit, and the committed content equals the intake. Observation (LOW, route Integration Control): commit messages for A1, A2, REC and Proof name other modules. Hash lineage is intact.

Source blobs A3 fetched and verified against Lane A/Proof: wizard `3b6d52e0…`, log model `045a2d25…`, partner model `19962c36…`, ACL `d70edab3…`, wizard views `9d49f1db…`, server actions `7aac52ec…`, core mail tools `2b05c91f…`. Core SQL tools `431bd6f0…` is a new A3 lineage record (escape helper).

## 4. Defects routed

| ID | Severity | Route | Summary |
|---|---|---|---|
| A3-PRIV-D1 | LOW | A2 | Fold Proof R1 (multi-character wildcard via email, e.g. `%@%`) into SF-PRIV-01 at HIGH. |
| A3-PRIV-D2 | LOW | A2 / REC | "Whole-DB under sudo" wording: discovery is raw SQL (no elevation needed, rules bypassed); elevation applies to display/archive/delete; scope bounded to partner-referencing or email-bearing models. |
| A3-PRIV-D3 | LOW | PROOF | PC-PRIV-12 execution method (harness) not predeclared. Record it as a post-declaration method change with a Python-version binding. |
| A3-PRIV-D4 | LOW | PROOF | PC-PRIV-19 display-name element rests on version-sensitive stdlib parsing. Mark it static-INCONCLUSIVE pending runtime PC-PRIV-07. |
| A3-PRIV-D5 | LOW | A2 | SF-PRIV-06 legal-classification wording. Make it neutral. |
| A3-PRIV-D6 | LOW | Integration Control | Commit messages do not name this module for A1/A2/REC/Proof. |

## 5. Runtime / gate-blocked items

- PC-PRIV-01..09 NOT-EXECUTED (runtime device offline at Proof time). They are neither passed nor failed. Proposed PC-PRIV-23 (email wildcard) is not predeclared yet.
- The 12 UNKNOWN_PENDING_PROOF REC items stay open. C17 runtime effect (PC-03/04), cross-company remediation (PC-01) and wildcard scope (PC-02) are pending.
- **RE-FREEZE required:** QID lineage stays non-canonical (W1-B11 DELTA-RECHECK) until canonical re-freeze and re-validation. After that, an A3 lineage challenge is required before MASTER.
- MASTER handoff is pending runtime, re-freeze and the follow-up A3 challenges.

## 6. Limitations

- Static, claim-level reading only. ORM behaviours (stored-compute timing, change-handler transactions, transient cleanup) were not executed.
- A3 did not execute vendor code. It relied on a static reading plus the Proof harness output, whose hashes A3 verified.
- Effective scan scope depends on installed modules (not assessed). Web client behaviour for server actions was not observed. JS and tests were not read.
- No legal conclusions. No percentages, no Formal Coverage claim. Git read-only. Inputs not edited.
