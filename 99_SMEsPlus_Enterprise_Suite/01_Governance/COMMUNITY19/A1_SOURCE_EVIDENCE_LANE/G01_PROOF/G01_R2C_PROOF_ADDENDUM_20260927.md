# G01 PLATFORM_BASE — RED TEAM PROOF Addendum, Remediation Cycle R2, Batch C — `mail`

**[ADDENDUM — PROOF STAGE]**

## 0. Header

| Item | Value |
|---|---|
| Owner stage | **PROOF** addendum only. No existing Proof or Proof-delta document is edited |
| Group / Module | G01 PLATFORM_BASE / `mail` (RES-M2, RES-M4 land here; RES-W1/M1/M3 are REC-only and carry no new Proof case) |
| Date | 2026-09-27 |
| **REC consumed (pinned)** | `G01_RECONCILIATION/G01_R2C_REC_ADDENDUM_20260927.md` sha256 **`57f2bfa1fa1cb5d298108a8b79411b5524c0879acb6c1596890a9184973a833c`**, frozen 2026-09-27T16:36:30Z, before this stage's predeclaration |
| Upstream A2 addendum | `G01_A2_REVIEWS/G01_R2C_A2_ADDENDUM_20260927.md` sha256 `05eb2519a9606c043913114900639a5e24cb0797ee79ae8c65808c16d039d11c` |
| D1-level parents unaffected (referenced only) | `G01_MAIL_REC_DELTA_D1_20260927.md` `bb5de020246be21a802880bfa3d0b411a6c430c84237cf57ae6e14bc59b8812f`; `G01_MAIL_PROOF_DELTA_D1_20260927.md` `09f1e1ac9e69ed8a7903f4825e9dfed8b00126552e8b8d9e4782a603f3b5ed3c` |
| Source anchor | `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/<path>`. No other host contacted. No GitHub API, no code search |
| Runtime device | OFFLINE (unchanged). All four cases below are SOURCE/CONFIG layer; none is a runtime case, so none is NOT-EXECUTED — all four ran |
| Scratch | `/tmp/claude-0/-home-user-AI-Collaboration-Hub/463170d3-0f33-53df-a8d9-5216854140b2/scratchpad/r2_batchC/` |
| **Status** | **REMEDIATION COMPLETE — RETURN TO A3 FOR RE-CHECK** |

### 0.1 Rule-compliance table

| Rule | Compliance |
|---|---|
| C1-B rule 1 | Not applicable — no case here derives from an A2 `MISSING_REQUIRED_RUNTIME_PROOF` item; all four are SOURCE/CONFIG |
| C1-B rule 2 (post-declaration text tagged) | **Complied.** PC-MAIL-R2-04 (Q047) was added to the cases file *after* PC-MAIL-R2-01..03 had already been fetched once during research; it is tagged **POST-DECLARATION** in §1 and in the cases file itself, and its expected/fail text is reproduced unchanged from that later addition |
| C1-B rule 3 | Upstream (REC R2C §4-§5 names the linking REC IDs) |
| C1-B rule 4 (REC sha pinned before predeclare) | **Complied.** REC R2C frozen 16:36:30Z → this addendum's official predeclaration hashed 16:36:53.10Z → first *official* source fetch 16:37:01.48Z into a fresh directory (`src_proof_r2c_official/`) → execution log closed 16:37:13.52Z |
| C1-B rule 5 (cases hashed + UTC before first fetch) | **Complied for the official record** (§1). **Disclosed, not concealed:** an earlier reconnaissance pass read the same nine files into `src/` and `src_proof_r2c/` starting at 16:28:45Z, before the official cases file existed, while this addendum's research was being scoped (same pattern B3B Proof R1 disclosed at its §1 for its own 15:36:51Z owner-stage read). Every blob recomputed identically in the official fetch, so nothing turns on which pass is cited; each case keeps a fail branch that would contradict the reconnaissance reading, to counter confirmation bias |
| MD-07 (anchor-only evidence) | Every file fetched from the pinned raw anchor only; every blob verified with `git hash-object`; none previously admitted via GitHub API or code search |
| MD-08 | Cases below state exactly which files were read; no "the only" completeness claim is made beyond those files |

Clean-room note: neutral summaries and pointers only; no vendor code reproduced. No QID answered. No percentages. No Formal Coverage. No git operations. No existing artifact edited.

## 1. Predeclaration record (official; before the official first fetch)

| Item | Value |
|---|---|
| Cases file | `PROOF_CASES_PREDECLARED_R2C_OFFICIAL.md` |
| sha256 | **`9e369087411291ad6215c9c7db3b187cc8a35374d84e078d2713eabc9fc8b490`** |
| UTC stamp | **2026-09-27T16:36:53.101124194Z** |
| First official source fetch | `proof_fetch_start_r2c.ts` = **2026-09-27T16:37:01.481523609Z**, into a fresh directory (`src_proof_r2c_official/`, did not exist before this run) |
| Execution log | `exec_R2C_official.txt` sha256 `332226cabecbc307bdfb395b85a6cd8740b8bd7826b6be624ac06220e63ae4c7`, closed 2026-09-27T16:37:13.523525827Z |
| Disclosure | Two earlier reconnaissance passes over the same files exist in scratch (`src/`, `predeclared_R2C.ts` = 16:30:05Z, `exec_R2C.txt` = 16:30:18Z; and `src_proof_r2c/`), made before the official cases file existed and before REC R2C was frozen. They are superseded for the official record by the fetch named above; every blob is identical across all three passes (recorded in §2) |
| Limitation | Scratch-resident, mtime-based ordering evidence, as in every prior stage's Proof addendum; not tamper-evident |

## 2. Cases (as officially predeclared) and results — all SOURCE/CONFIG, EXECUTED

| PC | REC link | Layer | Expected (predeclared, summary) | Fail condition (predeclared, summary) | Observed (official fetch; approx. lines) | Result |
|---|---|---|---|---|---|---|
| **PC-MAIL-R2-01** | REC-MAIL-D1-47 (N5) | CFG | A `discuss.channel` data record `mail.channel_all_employees` exists in a `mail` data file, in a `noupdate` block, name/description only | No such record exists, or it carries a company field | `addons/mail/data/discuss_channel_data.xml` @`97af6f6ada422439779d5775a585820733f06072` HTTP 200: `<record model="discuss.channel" id="mail.channel_all_employees">`, `name` "general", inside `<data noupdate="1">`; no company field on the record | **PASS** |
| **PC-MAIL-R2-02** | REC-MAIL-D1-49 (G12) | SRC | The composer's "responsible user for domain evaluation" field is declared once in `mail_compose_message.py` and referenced nowhere else in that file or in `mail_composer_mixin.py` | The field name recurs a second time in either file | `addons/mail/wizard/mail_compose_message.py` @`32fdf95981c9ea92af0d506711414decb32d2cd1` HTTP 200 ~L136-138: `res_domain_user_id = fields.Many2one('res.users', string='Responsible', help='Used as context used to evaluate composer domain')`; grep count in-file = 1. `addons/mail/models/mail_composer_mixin.py` @`57f7a65ac0654fa88fadea44c1c63a9847919bc2` HTTP 200: grep count = 0 | **PASS** |
| **PC-MAIL-R2-03** | REC-MAIL-D1-52 (new; RD3) | SRC (cross-file) | `update.py`'s publisher handler posts each remote message as a plain `str` via `message_post(body=message, ...)`; `mail_thread.py`'s `message_post` escapes a plain-string body and leaves `Markup` unchanged | `update.py` wraps the message in `Markup(...)` before posting, or `message_post` stores a plain-string body verbatim without an escape/sanitize step | `addons/mail/models/update.py` @`05603784124c160005a75d3c77afee94c72d2f62` HTTP 200 ~L96-99: `poster.message_post(body=message, subtype_xmlid='mail.mt_comment', partner_ids=[user.partner_id.id])` where `message` is an element of `result["messages"]` (parsed literal), not wrapped. `addons/mail/models/mail_thread.py` @`c1f8a83bbd4d6667c1ee7cd38b78cef71ad8f374` HTTP 200 ~L2199-2206 docstring: "str content will be escaped, Markup for html body"; ~L2332: `msg_values['body'] = escape(body)  # escape if text, keep if markup` | **PASS**. RD3's escaping question is closed at source: a plain-string publisher message is HTML-escaped before it becomes the stored message body |
| **PC-MAIL-R2-04** (POST-DECLARATION) | REC-MAIL-D1-53 (new; Q047) | CFG (cross-file: `service/db.py`, `controllers/database.py`, `neutralize.py`, `mail/data/neutralize.sql`) | Duplicate/restore default the neutralise flag to off at both the service and web-controller layer; `mail` ships a `neutralize.sql` that deletes push-device rows and VAPID keys | The neutralise flag defaults on at either layer, or `mail` ships no `neutralize.sql` / it does not touch `mail_push_device` | `odoo/service/db.py` @`63c314a72de738d044e542e32bc045c21f987531` HTTP 200: `exp_duplicate_database(db_original_name, db_name, neutralize_database=False)`; `exp_restore(db_name, data, copy=False)` → `restore_db(..., neutralize_database=False)` via its caller default. `addons/web/controllers/database.py` @`434b915ceb3a935c1fdbee248d4a4ed7a8533b48` HTTP 200 ~L95 `duplicate(..., neutralize_database=False)`, ~L151 `restore(..., neutralize_database=False)`. `odoo/modules/neutralize.py` @`4a3c572ba0b5638e7b50563b3003f80076a255af` HTTP 200: `neutralize_database(cursor)` executes each installed module's own `data/neutralize.sql`, only when called. `addons/mail/data/neutralize.sql` @`e61e84219650d88823c045803f417e1fe4dc38c8` HTTP 200: `DELETE FROM ir_config_parameter WHERE key IN ('mail.web_push_vapid_private_key', 'mail.web_push_vapid_public_key', ...)`; `TRUNCATE mail_push`; `DELETE FROM mail_push_device` | **PASS**. Net static answer: by default (flag not requested), push-device/endpoint state **survives** a duplicate or restore; it is removed only when the operator opts into neutralisation, which `mail` fully supports when invoked |

### 2.1 Totals (this addendum)

| Layer | Cases | PASS | FAIL | NOT-EXECUTED |
|---|---|---|---|---|
| SOURCE / CONFIG | 4 (PC-MAIL-R2-01, 02, 03, 04) | 4 | 0 | 0 |
| RUNTIME | 0 | — | — | — |

No runtime case is declared in this batch: RES-M2 asked for SOURCE/CONFIG-layer cases now (task instruction), and RES-M4/Q047 resolved statically without needing a runtime arm (A2 R2C §5 / REC R2C §5). A static PASS confirms only that the source reads as predicted; it does not confirm what a live deployment's operators actually do (whether they in practice pass `neutralize_database=True`), which stays an operational/runtime question outside this module's source and is not claimed here.

## 3. Effect on REC items (for A3)

- REC-MAIL-D1-47 (N5): closed — the channel is a plain `mail` data record, not a cross-module or runtime artifact.
- REC-MAIL-D1-49 (G12): confirmed as REC stated — declared, unreferenced within `mail`; use by another module stays an explicit, un-closed GAP (not a defect in the finding).
- REC-MAIL-D1-52 (RD3, new): the escaping mechanism is confirmed at source; A3-MD-05's residual risk narrows to whatever downstream body-rendering does with an already-escaped string, which this case does not examine and does not need to, to answer RD3 itself.
- REC-MAIL-D1-53 (Q047, new): resolved at source as a configuration-default fact; no runtime case is required to state it, though whether any given deployment's clone/restore runbook actually sets the flag remains outside source.

## 4. Limitations

- Static source at one commit; line pointers approximate.
- PC-MAIL-R2-04's scope is `mail`'s own neutralisation script; whether an operator's runbook, hosting-provider tooling, or another module's script additionally clears push state was not read and is not claimed.
- The predeclaration evidence is a scratch file with sha256 + UTC stamp + fresh-directory ordering; it is not git-committed, as in every prior Proof addendum.
- No Formal Coverage, no percentages, no git operations, no QID answered, no existing artifact edited.
