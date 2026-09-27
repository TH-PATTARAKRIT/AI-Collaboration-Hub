# G01 PLATFORM_BASE — Module `web_hierarchy` — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, an independent adversarial challenger. It did not author any upstream stage |
| Module | G01 PLATFORM_BASE / `web_hierarchy` |
| Date | 2026-09-27 (intake 15:21:45Z) |
| Scope | STATIC, CLAIM-LEVEL. Runtime NOT-EXECUTED (neither passed nor failed). MVQ lineage **NOT A3-ELIGIBLE** (no bank). Standard 55 sampled |
| Source anchor | `…/8d05257d83f9128953f580a066db67c48fcdb96f/addons/web_hierarchy/`. A3 re-fetched the manifest, `models/models.py`, `models/ir_ui_view.py` and `models/ir_actions.py`, and all blobs MATCH |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC; PROOF)** — substance holds; process rules 1, 3 and 4 are defective |

### Intake (sha256)

| Input | sha256 |
|---|---|
| Lane A | `ec340b9b9d84e1f96a5e3a1c029e9dcc6bd086e4e345cacf7879db9f7adf74ac` |
| A1 | `45c325c42cd33aca747b18e11875086246257c9a1ef289453c53eef2115434a2` |
| A2 | `48bdd133401eca8a9353e8f386086b5defab97984cc54625e4c02ac3b6f41f17` |
| REC | `ac6842312bd2159b6b642f7fafe929cc30ac72d1f14cfc382aff70df77509e53` |
| PROOF | `86510da84a062ce33dc157af50a35b2f3dc11dd0df0bd13784e52351ef6a4aa9` |

## 2. Challenge log

| # | Challenge | A3 re-check (`models/models.py`@88136e7d) | Disposition |
|---|---|---|---|
| A3-WHIR-01 | One-level read under caller rights (C07, C10; PC-WHIR-01) | No elevation construct appears in any module file. The initial search (L13), the neighbourhood search (L22) and the grouped child read (L29–34) run in the caller's environment, and so does the final read (L36). In single-match mode the result is one level: the parent (L19–20), then children of the record and of the parent (siblings) (L21–22). There is no deeper walk. | **UPHELD** |
| A3-WHIR-02 | Unreadable parent likely errors (A2 C10 PARTIAL; REC-WHIR-10 GAP) | The parent is added by following the record's relation (L19–20), not by a rule-filtered search, and is then included in the final read (L36). A final read of a record the caller cannot read would fail for the whole call rather than drop the row silently. This is framework behaviour and stays labelled as inference. A3 adversarial refinement, not verified because the framework was not read: rows whose parent is merely *referenced* (multi-match mode) are not read as records, so the error/truncation split applies only to the single-match parent inclusion. GAP rather than CONTRADICTION is correct, because A1's "silent truncation" is incomplete, not negated, for siblings and children. | **UPHELD** (runtime NOT-EXECUTED, PC-WHIR-04) |
| A3-WHIR-03 | Unbounded multi-record result (REC-WHIR-13) | No limit on L13, L22 or the grouped read L29–34. A multi-match returns the full match set (L23–24) and reads it all (L36). | **UPHELD** |
| A3-WHIR-04 | No server cycle check (REC-WHIR-09/14) | There is no recursion and no cycle check. The server does only one bounded expansion, so a parent cycle cannot make the server loop. The only server-visible effect is a duplicate: a self-parent record is concatenated with itself (L19–20 concatenation, not union), and L21 then excludes it from the search. Any claim of a server-side *loop* risk would be an overclaim. None was found in REC or PROOF, and the PC-WHIR-12 fail condition ("no duplicate, or loop") is framed correctly. Cycle handling in the client is not read. | **UPHELD** |
| A3-WHIR-05 | Caller specification mutated; parent field not validated (PC-WHIR-07) | L11–12 inserts the parent field into the caller's specification. L19 indexes by the caller-supplied field name without validation. | **UPHELD** |
| A3-WHIR-06 | View validation (PC-WHIR-05) | `models/ir_ui_view.py`@ce1d68e9: allow-list L7–20 (12 entries, including one implementation marker; A3 count matches the PROOF's "12 names"); child-tag checks L35–45; attribute check L47–54; skipped when not validating L32–33. There is no check that the parent-field value exists or has the right type. | **UPHELD** |

### Static PASS re-execution

| PC | A3 re-execution | Citation check | Weakness flagged |
|---|---|---|---|
| PC-WHIR-03 | PASS reproduced | L17–22, L19–20, L36 exact | None |
| PC-WHIR-09 | PASS reproduced | L13, L22, L29–34, L33 exact. PROOF also cites "L22–24" for the search call, but L23–24 is the multi-match branch, not a search | Minor citation looseness |
| PC-WHIR-11 | PASS reproduced | L20, L22 exact | Only the L20 concatenation can yield a duplicate; L22 excludes existing ids. The predicate's "duplicates possible" is correct only through L20 |
| PC-WHIR-13 | PASS reproduced (public model method L9–10; `controllers/__init__.py` 404 per upstream) | exact | Reachability through generic RPC is framework behaviour (PC-WHIR-14) |
## 3. Process-rule compliance (MASTER C1B systemic findings 1–5)

Source of the rules: `01_Governance/COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` section "Systemic process findings". Evidence below is from the inputs, the upstream scratch folder `scratchpad/rec_ui4` (read only) and read-only `git log`/`git show`.

| # | Rule | Result for this batch (onboarding, html_builder, web_hierarchy, web_unsplash) | Evidence |
|---|---|---|---|
| 1 | Preserve the A2 `MISSING_REQUIRED_RUNTIME_PROOF` (MRRP) label; do not collapse it into `UNCORROBORATED` | **NOT MET** | None of the four RECs uses the MRRP label in any row. The label is kept only indirectly, where the REC class is UNKNOWN_PENDING_PROOF (whose definition cites MRRP). Where A2 classed a claim MRRP but REC gave it another class, only `UNCORROBORATED` remains: onboarding C11 (CONTRADICTION) and C17 (GAP); web_hierarchy C10 (GAP); web_unsplash C12 (GAP). html_builder has one MRRP claim (C06); it is UNKNOWN_PENDING_PROOF, so it is preserved indirectly only. |
| 2 | Tag any Expected/predicate text added after predeclaration `POST-DECLARATION` | **NOT MET** | 0 `POST-DECLARATION` tags in the four PROOF files. Untagged changes against `predeclared_proof_cases.tsv`: PC-ONBD-05 scope narrowed from "all module .py / any elevation call" to "module runtime code" (tests excluded); PC-UNSP-08 and PC-UNSP-26 steps gained "(mock-resolved)", and PC-UNSP-10 gained "(mock)". Most other rows are wording changes with the same meaning. |
| 3 | REC scans all A1 item classes (BR / states / exceptions / handoffs / gaps / CRQ) | **NOT MET** | The four REC tables reconcile only the claims (Cnn) and A2 omissions (OM). GAP and CRQ items are carried forward in prose. No BR-, state, exception or handoff item is reconciled (0 `BR-` mentions in the four RECs). Effect: onboarding BR-5 and the state line "Panel scope: global → per-company (one way)" still state the negated C11 position; web_unsplash state lines and BR-5 are not updated for REC-UNSP-12/21 and CONTRADICTION-UNSP-1. |
| 4 | REC frozen (sha256 recorded) before PROOF; PROOF header records the REC sha256 it consumed | **NOT MET** | None of the four PROOF headers records a REC sha256 (they give path + item count only). The REC files cite `laneb_search.txt` (sha256 `21b8a78d…0ce7f`), and that file's mtime is 15:13:14Z, after PROOF source fetch began (first `src/` file 15:11:03Z; `blobcheck.txt` 15:11:12Z). REC files were first committed at 15:14:38Z (onboarding), 15:15:22Z (html_builder), 15:16:10Z (web_hierarchy) and 15:17:15Z (web_unsplash), all after PROOF execution started. The html_builder REC was edited again between commits `b31a0e8` and `37823e6` (a one-line correction to a freeze-hash abbreviation; nothing recorded the change), and REC-HBLD-08 cites a PROOF case (PC-HBLD-07). |
| 5 | Cases-file sha256 + UTC timestamp written before first source fetch | **MET (with note)** | `predeclared_proof_cases.tsv` recomputed sha256 = `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307` (MATCH); `predeclared_sha256.txt` and `predeclared_time.txt` = 2026-09-27T15:10:27Z; first source file 15:11:03Z; 67 case IDs present (19 + 8 + 14 + 26). Note: `tree_probe.json` (15:09:19Z, before predeclaration) records a GitHub API tree-listing attempt that returned 403 with no source content. The timestamp evidence still rests on self-written files and mtimes in scratch, not on a committed record. |

## 4. Lineage

| Artifact | Commits (read-only) | Content check |
|---|---|---|
| Lane A | `1ee5230` 14:52:49Z | = intake |
| A1 | `a3f48b1` 14:56:33Z | = value recorded by A2 |
| A2 | `ece5c2d` 15:05:02Z | = value recorded by REC |
| REC | `37823e6` 15:16:10Z | Committed after PROOF source fetch began; not frozen before PROOF |
| PROOF | `d14de3c` 15:19:52Z | = intake |

Commit subjects are ignored, because the checkpoint commits carry subjects that name other modules (for example `d14de3c` "A3 … bus, digest"). Only content is judged. Predeclaration verified. Standard-55 sample: REC-WHIR-10 → Q29/Q36/Q37/Q38 fit (traversal and boundary); REC-WHIR-13 → Q55 (capacity) fits; REC-WHIR-02 → Q53 (uninstall cascade as an out-of-band operation) is a weak but arguable fit. No QID is answered; MVQ has no bank.

Overclaim, Lane B and clean room: no runtime claimed; no percentages; no Formal Coverage. No Lane B exists, and none was misused. Clean room: 0 code fragments.

## 5. Defects routed

| ID | Owner | Severity | Defect | Action |
|---|---|---|---|---|
| D-WHIR-A3-1 | REC | LOW | C10 was MRRP in A2 and is a GAP in REC with only UNCORROBORATED shown; C11 MRRP is kept only through its class (rule 1) | Show the MRRP label on REC-WHIR-10 and REC-WHIR-11 |
| D-WHIR-A3-2 | REC | LOW | BR-1..BR-4 and the state/exception/handoff sections were not reconciled (rule 3). BR-4 ("all reads limited to caller rights") needs the C10 caveat: an unreadable parent likely errors | Add REC rows |
| D-WHIR-A3-3 | REC / PROOF | MED | REC was not frozen before PROOF, and the PROOF header has no REC sha256 (rule 4) | Freeze the REC and re-issue the PROOF header |
| D-WHIR-A3-4 | PROOF | LOW | PC-WHIR-09 cites L22–24 for a search call that is only on L22 | Tighten the citation (non-material) |

## 6. Runtime / gate-blocked items

- RUNTIME NOT-EXECUTED: PC-WHIR-02, 04, 06, 08, 10, 12, 14 (device OFFLINE; no Lane B).
- MASTER handoff pending runtime and the gate (no MVQ bank for `web_hierarchy`; Formal Coverage not authorized).

## 7. Limitations

One anchor commit. The framework read routine, rule application on relation traversal, the display-name privilege and the client JS view were not read. There was no runtime and no external contact beyond `raw.githubusercontent.com`. Git was used read-only; inputs were not edited. No percentages; no Formal Coverage; no QID answered.
