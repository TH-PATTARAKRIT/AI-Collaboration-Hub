# G01 PLATFORM_BASE — RED TEAM A3 RE-CHECK of Remediation R3, `mail` (RES-C1 cure)

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **RED TEAM A3** (independent re-check). This reviewer authored neither the R2C addenda, the R2C A3 recheck, nor this R3 Proof addendum |
| Group / Module | G01 PLATFORM_BASE / `mail` |
| Date | 2026-09-27 |
| Scope | **STATIC only.** Runtime device OFFLINE / NOT-EXECUTED; no runtime result claimed, inferred or accepted |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>` (raw host only; no GitHub API, no code search). Blob identity by `git hash-object`. Read-only git; no git operation performed |
| Scratch (this recheck) | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/a3_r3_recheck/` (fresh, created this session) |
| Inputs read | `G01_A3_CHALLENGES/G01_R2C_A3_RECHECK_20260927.md`, `G01_PROOF/G01_MAIL_PROOF_ADDENDUM_R3_20260927.md`, `G01_RECONCILIATION/G01_R2C_REC_ADDENDUM_20260927.md` — **none edited** |

### 0.1 Overall disposition

**`mail`: A3 R3 RE-CHECK: STATIC PASS WITH RESIDUAL DEFECTS (route REC, route MASTER/IC) — MASTER HANDOFF PENDING RUNTIME**

Reason this is not an unqualified PASS line: RES-C1 itself (the subject of this R3 cycle) is **CLOSED** below — the cure is genuine. The "residual defects" qualifier carries forward two items the R3 addendum never claimed to touch and that remain open exactly as the R2C recheck left them: (a) RES-M3's carried ordering-defect residue (CF-3/D03, D1-23/K1, K4, K5 — routed REC, unchanged), and (b) A3-MD-08 / commit-subject naming (routed MASTER/IC, out of this batch's scope). Nothing new is added to either.

Clean room: neutral WHAT/WHY/RISK paraphrase and evidence pointers only; no vendor code, schema or naming reproduced beyond short identifiers needed for traceability. No QID answered. No percentages. No Formal Coverage.

---

## 1. Input integrity (sha256, independently recomputed this session)

| Artifact | sha256 (this session) | Matches value cited elsewhere |
|---|---|---|
| `G01_A3_CHALLENGES/G01_R2C_A3_RECHECK_20260927.md` | `633b174e54ed91398980ebde91c547fc27ee1cfc3b69289bd7602158d461b7ac` | YES — matches the R3 Proof addendum's own header citation |
| `G01_RECONCILIATION/G01_R2C_REC_ADDENDUM_20260927.md` | `57f2bfa1fa1cb5d298108a8b79411b5524c0879acb6c1596890a9184973a833c` | YES — matches the R3 Proof addendum's cited "REC basis" hash, and matches the value the R2C recheck itself recorded |
| `G01_PROOF/G01_MAIL_PROOF_ADDENDUM_R3_20260927.md` | `68c6980c66f34b8c014a2a20760b44d2ebe227faae7ab68c3d23490c26287915` | N/A — this is the artifact under re-check; first recorded here |

No input was edited by this recheck; all three re-hash to the values used above.

---

## 2. Task 1 — ordering-proof verification (REC freeze → predeclaration → first fetch)

Independently inspected the shared scratch tree (reachable from this session; not fabricated for this recheck) rather than relying solely on the addendum's prose.

| Check | Addendum's claim | Independent finding | Result |
|---|---|---|---|
| REC basis sha256 cited is the actual REC file's hash | `57f2bfa1...833c` | Recomputed directly from the live file: identical | **MATCH** |
| Predeclaration file hash | `predeclared_R3.md` sha256 `004c0a1904ee977569cccf37e03f9136d7f29197c705a428d54280677a8a0f90` | Recomputed from `scratchpad/r3_mail/predeclared_R3.md`: identical | **MATCH** |
| Predeclaration content is genuinely blind (expected/fail text, not post-hoc) | Written before any fetch this cycle | Read in full: file states preconditions ("fetch ... fresh ... into a clean subdirectory not previously used this session") and gives falsifiable expected/fail conditions per case, phrased prospectively, not as a report of results | **Consistent with a blind predeclaration** |
| REC-freeze precedes predeclaration | 16:48:47Z → 16:49:21.92Z | Filesystem mtime of `predeclared_R3.md` = 16:49:17.95Z (a few seconds before the addendum's stated hash-timestamp, consistent with write-then-hash); REC source file's own mtime = 16:36:25.94Z, well before either — no contradiction | **ORDER HOLDS** |
| Predeclaration precedes first fetch, same cycle | 16:49:21.92Z → 16:49:29.42Z | `src_proof_r3/` subtree mtimes begin at 16:49:29.83Z (first file written), after `predeclared_R3.md`'s mtime (16:49:17.95Z) — consistent, ~12s gap | **ORDER HOLDS** |
| No earlier fetch of these same 9 files by this addendum's author, for **this R3 cycle**, predating this cycle's own predeclaration | "No earlier reconnaissance artifact in this cycle's scratch directory" | Searched the entire reachable scratch tree for all 9 basenames outside `r3_mail/`: every hit is dated 14:45Z–16:41Z and belongs to distinct, already-accounted-for prior stages (Lane A `laneA_T*`, A1/A2 working dirs, `rec_prtl_utm`, and the R2C Proof reconnaissance in `r2_batchC/` plus the prior A3 R2C recheck's own read in `a3_r2c/`). None postdates the R2C cycle and predates this R3 cycle's own predeclaration (16:49:17Z); none belongs to a distinct, undisclosed R3-cycle reconnaissance | **CONFIRMED — no undisclosed earlier fetch for this cycle** |

**Verdict on Task 1:** the ordering proof is genuine on its own terms. REC basis is correctly cited and was hashed before any other R3-cycle action; predeclaration was hashed and file-committed before the first R3-cycle fetch; no hidden reconnaissance pass for this specific cycle exists in reachable scratch history. The R2C reconnaissance (`r2_batchC/`) that RES-C1 was about remains present, undisturbed, and correctly understood as the defect being cured — not as evidence against this cycle.

---

## 3. Task 2 — independent re-fetch of PC-MAIL-R3-01..04

Fetched all 9 cited files fresh, into this recheck's own clean scratch subdirectory, and independently re-derived each case's substance (not merely compared hashes).

| File | Blob (this recheck) | Matches addendum |
|---|---|---|
| `addons/mail/data/discuss_channel_data.xml` | `97af6f6ada422439779d5775a585820733f06072` | YES |
| `addons/mail/wizard/mail_compose_message.py` | `32fdf95981c9ea92af0d506711414decb32d2cd1` | YES |
| `addons/mail/models/mail_composer_mixin.py` | `57f7a65ac0654fa88fadea44c1c63a9847919bc2` | YES |
| `addons/mail/models/update.py` | `05603784124c160005a75d3c77afee94c72d2f62` | YES |
| `addons/mail/models/mail_thread.py` | `c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374` | YES |
| `odoo/service/db.py` | `63c314a72de738d044e542e32bc045c21f987531` | YES |
| `addons/web/controllers/database.py` | `434b915ceb3a935c1fdbee248d4a4ed7a8533b48` | YES |
| `odoo/modules/neutralize.py` | `4a3c572ba0b5638e7b50563b3003f80076a255af` | YES |
| `addons/mail/data/neutralize.sql` | `e61e84219650d88823c045803f417e1fe4dc38c8` | YES |

**9/9 blob match, HTTP 200 for all. No mismatch.**

Per-case substance re-derivation:

- **PC-MAIL-R3-01 (N5):** `<data noupdate="1">` wraps the file; `mail.channel_all_employees` record present with name/description identity; no `company_id` field on it anywhere in the file. **PASS confirmed.**
- **PC-MAIL-R3-02 (G12):** responsible-user domain field occurs 1× in `mail_compose_message.py` (declaration only), 0× in `mail_composer_mixin.py`. **PASS confirmed.**
- **PC-MAIL-R3-03 (RD3):** `update.py` posts each remote `message` as a plain loop element (`poster.message_post(body=message, ...)`), never markup-wrapped; `mail_thread.py`'s `message_post` docstring and body-assignment path apply an escape to a plain-string body and leave markup untouched. **PASS confirmed.**
- **PC-MAIL-R3-04 (Q047):** `db.py`'s `exp_duplicate_database`/`restore_db` and `database.py`'s `duplicate`/`restore` controller methods all default `neutralize_database=False` and only invoke the neutralize path when true; `neutralize.py` dispatches to each installed module's own script only on that call; `mail`'s `neutralize.sql` deletes the VAPID/JWT `ir_config_parameter` keys, truncates `mail_push`, and deletes `mail_push_device` rows. **PASS confirmed.**

**Verdict on Task 2: all four PC-MAIL-R3-01..04 PASS outcomes independently reproduced and hold.** This is the second independent confirmation of these same source facts (the R2C recheck already confirmed them once via its own unprompted read); nothing here is taken on the addendum's word.

---

## 4. Task 3 — adjudication of RES-C1

**Does the R3 cure close RES-C1?** Yes — **CLOSED.**

Reasoning:

1. **The literal rule-4/5 defect is fixed.** RES-C1's finding was procedural, not factual: PROOF R2C had run its own predeclare-and-execute cycle (`predeclared_R2C.ts` / `exec_R2C.txt`, still present at `r2_batchC/` and independently located again this session) with its fetch preceding its own predeclaration, and closing execution before REC R2C had frozen — violating rule 5 and rule 4 independently, within that one cycle. This R3 cycle is a **new, distinct cycle** with its own fresh scratch subtree (`r3_mail/`), and within that cycle the order is genuinely: REC-hash recorded → predeclaration file written and hashed → first fetch → execution. That internal order is independently verified in §2, not merely asserted.

2. **On the question the task poses directly — does freezing the REC basis "before anything else" still count if the author already knew the likely answers from the superseded R2C addendum:** yes, it still counts, and the objection does not hold here. Predeclaration's actual function is to fix, in a hashed and timestamped artifact, what would count as PASS and what would count as FAIL *before* that specific execution's evidence is examined — so that the fail branch cannot be quietly narrowed or the expected condition quietly loosened once the fetch is in hand. That is a real safeguard even when the underlying facts are already well-known and static (an immutable git blob at a pinned commit cannot change between cycles), because the safeguard is about tailoring within *this* execution, not about the author's prior state of knowledge. Demanding genuine amnesia across sequential remediation cycles of the same governed lineage — where each stage is explicitly built to carry forward prior findings — would make rule 4/5 unsatisfiable in principle, which cannot be the intent of a rule this same batch's own PROOF and REC stages routinely rely on succeeding cycles to build on. The R3 predeclaration text (read in full, §2) is prospective and falsifiable in form, its cases file was hashed before any fetch of this cycle, and the fetch that followed could not have altered an already-hashed file. That is what rule 4/5 requires, and it is what happened.

3. **No new factual defect is introduced or concealed.** All four PASS outcomes were independently reproduced twice now (R2C recheck, and this recheck), from two different unprompted anchor reads. The R3 addendum does not re-litigate REC's substantive content and correctly declines to reopen anything beyond the four named cases.

4. **What remains genuinely open is unrelated to RES-C1** and was never claimed to be cured by this addendum: RES-M3's carried ordering-defect residue (CF-3/D03, D1-23/K1, K4, K5 — routed to REC, unchanged since B3B R1) and A3-MD-08 (commit-subject naming, routed MASTER/IC). Both are correctly disclosed as out of this batch's scope in the R3 addendum's own §1 and are not silently dropped here either.

---

## 5. Residual defects (routing) — updated

| ID | Module | Status | Route |
|---|---|---|---|
| RES-C1 | mail | **CLOSED this cycle.** Genuine blind predeclare-then-execute cycle, independently verified (§2); all four PASS outcomes independently reproduced twice (§3) | none |
| RES-M3 (carried) | mail | Unchanged — CF-3/D03, D1-23/K1, K4, K5 remain an open, correctly-labelled ordering-defect residue from the original D1 cycle; not addressed by this R3 addendum, not claimed to be | REC (unchanged) |
| A3-MD-08 (carried) | mail | Unchanged — commit-subject naming, out of this batch's scope | MASTER / IC |

No residual above contradicts an R3 static fact; both carried items are process/governance carries, not factual refutations of PC-MAIL-R3-01..04.

---

## 6. Limitations

- STATIC only, at one pinned commit. Line pointers approximate.
- Ordering evidence (§2) rests on scratch-resident mtimes and the addendum's own disclosed timestamps, consistent with every prior Proof addendum's stated limitation; it is not git-committed or independently tamper-evident, but it is independently *observable* in this case because the scratch tree was reachable from this session, and it was actually inspected rather than taken on trust.
- This recheck did not re-derive RES-M3's carried items (D03/K1/K4/K5) or A3-MD-08; both are out of this R3 addendum's declared scope and remain exactly as the R2C recheck left them.
- No runtime evidence exists anywhere in this document. No Formal Coverage, no percentages, no git operations, no input artifact edited, no QID answered.
