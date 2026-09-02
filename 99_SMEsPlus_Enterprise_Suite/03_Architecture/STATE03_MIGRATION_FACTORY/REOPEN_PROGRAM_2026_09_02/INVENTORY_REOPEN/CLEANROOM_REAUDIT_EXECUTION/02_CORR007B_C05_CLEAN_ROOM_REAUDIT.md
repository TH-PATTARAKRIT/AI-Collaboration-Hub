# 02 — CORR-007B `C-05` Clean-Room Re-Audit

This is the controlling document of this session. It performs the independent tie-breaking re-read of CORR-007B files `08`/`09` explicitly recommended by `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md` §7 and named as still-outstanding by both the remediation record (`17`) and the menu package's own Boss Gate package (`25` §3: "`C-05` independent re-audit not performed → Any Team B reading of valuation/close evidence" is blocked).

## 1. What `C-05` originally was

Per `13_INVENTORY_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md` (Tier 2, item C-05) and `10_CLEANROOM_IP_PROVENANCE_VETO_FINDINGS.md` §2.3/§3.3: two independently-run reviewing bodies (Council and Special Team) examined CORR-007B's N-A12-01 evidence package — files `08_CORR007B_N_A12_01_ACCOUNT_LED_INVENTORY_PERIOD_CLOSE_FUNCTIONAL_DESIGN_PROOF.md` and `09_CORR007B_PRODUCT_CATEGORY_VALUATION_FUNCTIONAL_DESIGN_REVIEW.md` — and found two distinct, non-overlapping defects in the pre-remediation text:

1. **Council's finding (language):** prescriptive wording drifting from "this is what the reference system does" toward "SMEsPlus must do this" (file `09` §7, file `08` §12 table framing, file `08` line 325). Council's own verdict: `CONTINUE_WITH_NOTES` — a correctable caution, not blocking.
2. **Special Team's finding (code):** verbatim, fenced-code-block reproduction of actual Odoo Python source — the full `_compute_valuation()` method body and decorator, the complete `property_valuation` field declaration with its exact Selection enum values and docstring, and the full `_should_create_account_move()` boolean return expression, sourced to `stock_account/models/stock_move.py:630-635`. Special Team's own verdict: `HOLD` — required remediation before Team B/C read access.

Because the two verdicts conflicted at the headline level, Track 08's reconciled verdict was `HOLD`, and `10` §7 named a specific required action: **an independent third pass, or Boss's own direct read, of files 08/09 checking for both defect types, to establish a single non-conflicting record before the package is handed to any authorized Team B/C session.** This document is that independent third pass.

## 2. Independent verification performed by this session

### 2.1 Pre-remediation content — confirmed present in git history

Using `git log --all --follow`, this session traced both files' full history independent of any prior session's narrative:

- File `08`: introduced at commit `ac9e1e407d8b43f172094199a0c1fe8374d8a99c` ("CORR-007B reopen N-A12-01 through four Boss functional-design addenda", 2026-09-02 00:59:47 +0700); remediated at `0e816877b910ea1549dd7afad9d4fec654e64f62` (2026-09-02 08:44:26 +0700).
- File `09`: introduced at `ac9e1e40...`; modified at `0eb78c68ae1d6c340dce163fb6aa609920d98226` ("CORR-007B documentation cleanup - resolve addendum-5 numbering collision", 2026-09-02 01:29:26 +0700); remediated at `460f14a761a537155cd3858948ca90e4a6fe51f9` (2026-09-02 08:45:27 +0700).

This session extracted the pre-remediation blob content directly with `git show ac9e1e40:<path>` for both files and ran an independent mechanical scan (vendor-token pattern `stock\.`, `product\.`, `ir\.`, `res\.[a-z_]+\.[a-z_]+`, `quant`, `orderpoint`, `picking`, `_action_`, `sudo(`, `.py`, plus fenced-code-block detection) without reproducing the matched content in this or any output file:

| File (pre-remediation blob) | Lines | Vendor-token / code-pattern hits |
|---|---|---|
| `08` @ `ac9e1e40` | 505 | 107 |
| `09` @ `ac9e1e40` | 169 | 33 |

**This independently confirms Special Team's specific finding was real and substantial** — 107 and 33 mechanical hits is consistent with "full method body and decorator," "complete field declaration with exact Selection values and docstring," and "full boolean return expression," not an isolated stray token.

### 2.2 Current branch surface — confirmed remediated

The same mechanical scan, run against the current tip of `audit/inventory-core-corr007b-3high-closure-010` (remediated files `08`/`09`), returned **zero** vendor-token or fenced-code-block hits. A second, targeted scan for Council's specific prescriptive-language patterns ("must use the ... actually present in source", "as Odoo does", "reference source supports") also returned zero hits — the only two matches found were the remediation record's own negated description of what it removed ("wording that says SMEsPlus must copy the reference system"), which is not itself a leak.

**Independent conclusion: both defect types named in `C-05` are absent from the current branch surface.** This corroborates, with fresh independent evidence rather than by re-reading the remediation record's own self-description, that the remediation performed at `9996072a` addressed both Council's and Special Team's findings.

### 2.3 A material sub-finding: history is not access-restricted

`17_CORR007B_CLEAN_ROOM_REMEDIATION_RECORD.md` §5 states "Historical existence of prior risky text | Preserved in git history, but not suitable for downstream use," and §4 defines a "Layer 2 Audit Quarantine" restricted to "Boss, PMO, AI Audit SMEsPlus only." This session's independent check finds a gap between that stated control and what the repository actually enforces:

- The pre-remediation commits (`ac9e1e40`, `0eb78c68`) are **ordinary reachable commits on a normal branch**, not on a separate access-restricted ref, not removed by history rewrite, and not excluded from a standard clone.
- This session's own fresh, standard-credential clone retrieved the full pre-remediation content via `git show ac9e1e40:<path>` with no additional permission step, credential, or quarantine gate encountered.
- Anyone with the same repository read access this session has — which is not scoped narrowly to "Boss, PMO, AI Audit SMEsPlus" — can retrieve the verbatim Odoo source reproduction by checking out `ac9e1e40` directly, with no warning, label, or access control in the way. Rewriting the branch tip content cannot retroactively remove a prior commit object that remains reachable from any ref, and `0eb78c68` is itself still an ancestor of the branch's own current tip `9996072a`.

**This means the Layer 2 model described in `17` §3–§4 is a documented usage policy (who should read and act on old material), not an enforced repository-level containment control (whether the material is technically reachable).** It is accurate that the *current branch surface* is remediated; it is not accurate, without qualification, that the material is only reachable by the four named parties.

## 3. `C-05` disposition

| Question (from governing prompt §5) | Finding |
|---|---|
| What was the original risk? | Verbatim Odoo source-code reproduction (Special Team) + prescriptive reference-as-target language (Council) in CORR-007B files `08`/`09`, independently confirmed present (107/33 mechanical hits) by this session's own re-scan of the pre-remediation commit. |
| Which files were remediated? | `08` and `09`, at commits `0e816877` and `460f14a7` respectively. Independently re-scanned clean by this session. |
| Is the current branch surface clean? | **Yes**, confirmed by independent mechanical re-scan (§2.2). |
| Does the old risk remain in git history? | **Yes**, confirmed by independent `git log --all` trace and content re-scan (§2.1), and further, the history is **not** access-restricted as the Layer 2 model assumes (§2.3). |
| Is Layer 2 Audit Quarantine sufficiently defined? | The *policy* is well-defined (`17` §3–§4). The *technical enforcement* is not — see §2.3. This is a gap, not a failure of the policy's own wording. |
| Can Team B/C safely read Layer 1 after Boss approval? | The Layer 1 (remediated) surface itself: yes, on this session's independent evidence. Conditional on this tie-breaking action being formally ratified by Boss, and on the §2.3 gap being closed or explicitly accepted by Boss. |
| What conditions must be met before reliance? | See `10_REMEDIATION_ACTION_REGISTER.md`. |
| Must any remaining file be rewritten? | No further rewrite of `08`/`09` is indicated — both defect types are independently confirmed absent from the current surface. The action needed is a repository-control decision (§2.3), not a further content rewrite. |

## 4. Cross-document corroboration

- `merge-base` check independently re-run by this session: `git merge-base --is-ancestor origin/audit/inventory-core-corr007b-3high-closure-010 origin/SMEsPlus` — not an ancestor. Same result for the reopen branch. **Neither corrective branch is merged into canonical `SMEsPlus`.** No confirmed downstream/canonical contamination today.
- `13_INVENTORY_MATERIAL_UNKNOWN_CONFLICT_REGISTER.md` names this finding `C-05`, ranks it highest priority, and lays out the same four-step resolution path this session finds was in fact executed by commits `0e816877`/`460f14a7`/`9996072a`.
- The menu package's own lineage register (`01_PRIOR_EVIDENCE_AND_CLEAN_ROOM_LINEAGE_REGISTER.md`, row 89) correctly preserves `C-05` as a "Boss-visible control" rather than treating it as closed, and (rows 76–77) confirms it did not open the pre-remediation content or even the remediated file `08` — consistent with what this session independently verifies.

## 5. `C-05` Verdict

**`C-05 SURFACE REMEDIATED / HISTORY QUARANTINE REQUIRED`**

This is not `C-05 CLOSED` — that label is reserved for a separate Boss decision per the governing prompt §5. The tie-breaking read `10` §7 called for has now been performed, independently, with a mechanical (not narrative-only) method, and both named defect types are confirmed resolved on the current branch surface. What remains open is a repository-governance question — how the historical, pre-remediation content should be controlled — which is squarely a Boss-only decision (see `10_REMEDIATION_ACTION_REGISTER.md` for the specific options; this session executes none of them).
