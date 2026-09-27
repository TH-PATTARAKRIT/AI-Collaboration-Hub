# G01 PLATFORM_BASE — RED TEAM PROOF Addendum, Remediation Cycle R3 — `mail` (cures RES-C1)

**[ADDENDUM — PROOF STAGE, NEW FILE. No existing artifact edited.]**

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF** addendum only |
| Group / Module | G01 PLATFORM_BASE / `mail` |
| Cycle | R3 — cures the rule-4/5 process defect identified in RES-C1 |
| Date | 2026-09-27 |
| **REC basis (frozen before this addendum began; not re-opened or re-litigated)** | `G01_RECONCILIATION/G01_R2C_REC_ADDENDUM_20260927.md` sha256 **`57f2bfa1fa1cb5d298108a8b79411b5524c0879acb6c1596890a9184973a833c`**, recorded 2026-09-27T16:48:47Z, before any other action in this cycle |
| Parent PROOF addendum (superseded for these 4 cases only, on process grounds; not for its factual PASS content) | `G01_PROOF/G01_R2C_PROOF_ADDENDUM_20260927.md` sha256 `47d730d1ffd4c6456e501962e5d7a17df2038bdb84902fd505349f71dd8895ee` |
| A3 R2C recheck (source of RES-C1) | `G01_A3_CHALLENGES/G01_R2C_A3_RECHECK_20260927.md` sha256 `633b174e54ed91398980ebde91c547fc27ee1cfc3b69289bd7602158d461b7ac` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. No other host contacted. No GitHub API, no code search |
| Runtime device | OFFLINE (unchanged). All four cases are SOURCE/CONFIG layer; none is NOT-EXECUTED |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/r3_mail/` (clean subdirectory; did not exist before this run) |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

Clean-room note: neutral summaries and pointers only; no vendor code reproduced verbatim beyond short identifier/field-name fragments needed for traceability. No QID answered. No percentages. No Formal Coverage. No git operations.

## 1. What this addendum cures, and what it does not re-open

RES-C1 found that the R2C Proof addendum ran its own predeclare-and-execute cycle (a reconnaissance pass, artifacts `predeclared_R2C.ts` / `exec_R2C.txt`) **before** REC R2C froze, and **before** that reconnaissance pass's own predeclaration was written (fetch preceded predeclaration) — violating C1-B's rule 4 and rule 5 independently. It also found that the subsequent "official" redo, while internally ordered correctly, could not establish that its own expected/fail text was written blind, since the actual outcomes were already known from the earlier execution.

This is purely a **process** finding. A3 itself independently re-derived all four facts (PC-MAIL-R2-01..04 / N5, G12, RD3, Q047) from a fresh, unprompted anchor read and could not refute any of them. This addendum does not re-litigate REC's content, does not re-open the substantive question, and treats the REC basis above as frozen and final. Its only job is to run a genuinely clean predeclare-then-execute cycle for these same four findings, with no prior fetch or execution of any kind preceding the predeclaration below, in this session.

## 2. Ordering-proof statement (the core of this cure)

| Step | Artifact | UTC timestamp |
|---|---|---|
| 1. REC basis frozen (read + hashed, nothing else done first) | `G01_R2C_REC_ADDENDUM_20260927.md` sha256 above | **2026-09-27T16:48:47Z** |
| 2. Predeclaration written and hashed (no source file for this cycle fetched yet, by this session, at this point) | `predeclared_R3.md` sha256 **`004c0a1904ee977569cccf37e03f9136d7f29197c705a428d54280677a8a0f90`** | **2026-09-27T16:49:21.922912409Z** |
| 3. First fetch of this cycle, into a brand-new subdirectory (`src_proof_r3/`, did not exist before this run) | 9 files fetched via fresh `curl` calls (list in §3) | **2026-09-27T16:49:29.420839033Z** |
| 4. Fetch/execution closed | all 9 blobs read and hashed | **2026-09-27T16:49:31.957188349Z** |

**Predeclared before execution: TRUE.**
**First fetch this session (16:49:29.42Z) is after predeclaration (16:49:21.92Z): TRUE** — by approximately 7.5 seconds, with no intervening fetch of any kind for this cycle. Unlike R2C, there is no earlier reconnaissance artifact in this cycle's scratch directory: `src_proof_r3/` was created fresh at step 3, and no `.ts`/exec-log file predates the predeclaration file. Step 1 (REC hash) also precedes step 2 (predeclaration) by roughly 35 seconds, satisfying rule 4 independently of rule 5.

Predeclared cases file (full expected/fail text, written before any fetch): `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/r3_mail/predeclared_R3.md`.

## 3. Cases (as predeclared) and results — all SOURCE/CONFIG, EXECUTED

| PC | REC link | Layer | Expected (predeclared, summary) | Fail condition (predeclared, summary) | Observed (fresh fetch this cycle; approx. lines) | Result |
|---|---|---|---|---|---|---|
| **PC-MAIL-R3-01** | REC-MAIL-D1-47 (N5) | CFG | A `discuss.channel` data record for the built-in all-employees channel exists, inside a no-update-on-upgrade block, with name/description-only identity | No such record, or it carries a company field, or sits outside a no-update block | `addons/mail/data/discuss_channel_data.xml` — hash-object `97af6f6ada422439779d5775a585820733f06072` — `<record model="discuss.channel" id="mail.channel_all_employees">` at file top, `name` "general", `description` present, inside `<data noupdate="1">`; a later block in the same file only adds a group-membership field to the same record, still no company field anywhere on it | **PASS** |
| **PC-MAIL-R3-02** | REC-MAIL-D1-49 (G12) | SRC | The composer's responsible-user-for-domain field is declared once, in the wizard file, and not referenced in either that file again or in the composer mixin file | Field name recurs a second time in either file | `addons/mail/wizard/mail_compose_message.py` — hash-object `32fdf95981c9ea92af0d506711414decb32d2cd1` — field declared once, ~L136; in-file occurrence count = 1. `addons/mail/models/mail_composer_mixin.py` — hash-object `57f7a65ac0654fa88fadea44c1c63a9847919bc2` — occurrence count = 0 | **PASS** |
| **PC-MAIL-R3-03** | REC-MAIL-D1-52 (RD3) | SRC (cross-file) | The publisher-notification handler posts a remote message as a plain string; the message-posting method escapes a plain-string body, leaves markup unchanged | Handler pre-wraps message in markup, or posting method stores plain string verbatim, unescaped | `addons/mail/models/update.py` — hash-object `05603784124c160005a75d3c77afee94c72d2f62` — ~L99, message posted as an unwrapped element of the parsed remote response, not markup-wrapped. `addons/mail/models/mail_thread.py` — hash-object `c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374` — docstring ~L2209 states plain-string content is escaped, markup left as-is; ~L2332 and ~L2831 apply an escape call to the body field before storage | **PASS** |
| **PC-MAIL-R3-04** | REC-MAIL-D1-53 (Q047) | CFG (cross-file) | Neutralize flag defaults off at both the internal service layer and the web-controller layer for duplicate/restore; `mail` ships its own neutralize script clearing push-device rows and push/VAPID key config | Flag defaults on at either layer, or `mail` ships no neutralize script, or it doesn't touch push-device/push-key state | `odoo/service/db.py` — hash-object `63c314a72de738d044e542e32bc045c21f987531` — duplicate/restore entry points default the flag to off (~L185, L334), only invoked when true (~L199, L372). `addons/web/controllers/database.py` — hash-object `434b915ceb3a935c1fdbee248d4a4ed7a8533b48` — both the duplicate and restore controller methods default the same flag to off (~L95, L151). `odoo/modules/neutralize.py` — hash-object `4a3c572ba0b5638e7b50563b3003f80076a255af` — dispatches to each installed module's own neutralize script only when called. `addons/mail/data/neutralize.sql` — hash-object `e61e84219650d88823c045803f417e1fe4dc38c8` — deletes the stored VAPID/JWT push-key config parameters, truncates the queued-push table, and deletes all push-device rows | **PASS** |

### 3.1 Totals

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE / CONFIG | 4 (PC-MAIL-R3-01..04) | 4 | 0 | 0 |

## 4. Relationship to the prior (R2C) results

All four fresh, cleanly-ordered fetches this cycle produced git-object hashes **identical** to those recorded in the superseded parent addendum, confirming the underlying source has not changed and that the prior PASS outcomes were factually accurate — consistent with A3's own independent re-derivation in the R2C recheck. What changes here is process only: this cycle's predeclaration was written with no prior fetch, execution, or knowledge of outcomes for this cycle preceding it, and the REC basis was hashed before any other step — curing RES-C1 without reopening the substantive findings on N5, G12, RD3, or Q047.

## 5. Limitations

- Static source at one pinned commit; line pointers approximate.
- PC-MAIL-R3-04's scope remains `mail`'s own neutralize script only; whether an operator's runbook or another module's script additionally clears push state is not examined here, as in the parent addendum.
- Predeclaration/execution ordering evidence is scratch-resident and mtime/monotonic-clock based, not git-committed or independently tamper-evident, consistent with every prior Proof addendum's stated limitation.
- No Formal Coverage, no percentages, no git operations, no QID answered, no existing artifact edited.

## 6. Handoff

RES-C1 is addressed for these four cases via a demonstrably clean predeclare-then-execute cycle, with the REC basis frozen first and the timestamp chain in §2 available for independent audit. Returned to A3 for re-check of the procedural cure; the factual PASS content of N5/G12/RD3/Q047 is not in question and is not reopened by this handoff.
