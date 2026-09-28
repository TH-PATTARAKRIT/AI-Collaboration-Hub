# RED TEAM — HANDOVER
**SMEsPlus Enterprise Suite · ROOM A · STATE03**
Prepared 2026-09-26 03:00 Asia/Bangkok · outgoing RED TEAM session
Status: **PREPARED ONLY — not Boss approval of anything**

---

## 0. READ THIS FIRST — why this handover exists

Boss replaced the RED TEAM session after 7 errors of the same kind in one night.
The pattern, stated plainly so the next session does not repeat it:

> **Every failure was writing from memory of how the system *should* be,
> instead of asking the system how it *is*.**

| # | claimed | reality |
|---|---|---|
| 1 | `find /` would return empty | the working Mac always has manifests |
| 2 | surfaces S4/S5 were usable | `ir.rule` `ir.model.access` `ir.cron` all refused |
| 3 | `ODOO_ADMIN_PASSWD.txt` = admin login | it is neither; the real login password is lost |
| 4 | `odoo-bin` exists | pip/venv install — the entry point is `venv/bin/odoo` |
| 5 | `res.users.groups_id` | Odoo 19 renamed it `group_ids` |
| 6 | `res.groups.category_id` | removed in Odoo 19 |
| 7 | an unattended loop was safe | it would have created 2 junk records every 10 min for 8 h |

Errors 1–6 cost time. Error 7 would have polluted the frozen study database
while Boss slept; Boss caught it before it ran, not RED TEAM.

**Rule for the successor: before writing any rule, path, field name or
threshold into a document, run a probe that proves it. A control that has
never been executed is not a control.**

Two further habits Boss had to correct:
- Sending Boss one command per fix, five rounds deep, instead of one script
  that runs the whole chain and survives its own failures.
- Writing instructions that make an agent improvise, instead of writing the
  script. Gemini burned a whole session inventing Playwright launch commands
  because RED TEAM would not write 100 lines of python.

---

## 1. VERIFIED STATE (re-verify before relying on it)

```
study server      https://t9c.smeplus.asia   db iTest19C   (103.253.74.217)
installed modules 299
installed-set hash 706e6df4008e0bac042a9821507ec0bc6868c4d9f98bcb93004a2535b1ca3c89
                  verified 22, 25 and 26 Sep - never moved
licence           {LGPL-3: 299}  zero contamination
clean room        CLEAN - no source path in any artifact (scanned 26 Sep)
```

**The hash formula — do not re-derive it (rule R2):**
```python
hashlib.sha256(("\n".join(sorted(installed_module_names)) + "\n").encode()).hexdigest()
```
The trailing newline matters. A previous session produced `0cdb7361…` by
omitting it and nearly reported the baseline as moved.

---

## 2. WHAT EXISTS

### On Boss's Mac — `~/ROOMB_WORKSPACE/` (connected folder)
```
RUN_ALL.sh                 whole Lane B chain, one command, survives step failures
WATCH.sh                   unattended loop, 10 min, 8 h, safety trips
GEMINI_TASK.md             Lane B agent task - interpretation only, 1 approval
HANDOVER_REDTEAM.md        this file
QUESTION_BANK_STANDARD_55_V2.00.md   FROZEN  f6726f11…
FREEZE_W1-STD.json         batch freeze  c64693ee…
SCOPE_LIST_V2.01.tsv       f748eee0…
LANE_B_CHARTER_GEMINI_V1.03.md       SUPERSEDED by the census model - rewrite needed
credentials/roomb_observer.env       mode 600 - never read into any context

collectors/
  installed_set_hash.py         baseline verifier
  census_menu_tree.py           menu census - needs no grant
  census_screens.py             screenshot capture - Playwright, one command
  stage1a_collector_V2.py       standard batch + cleanup (V1 is VOID, archived)

ops/
  grant_laneb_via_odoo_shell.sh    the grant, via odoo shell, no login needed
  census_feasibility_probe.py      which surfaces the observer can reach
  diagnose_admin_credential.py     which credential opens which door
  diagnose_admin_user.sh           psql read-only: users, groups, menu count
  mvq_gate_ERPPLUS-170.py          RED TEAM admissibility gate for question sets

batches/W1-STD/            16 artifacts, MANIFEST matches folder exactly
batches/W1-SCREENS/        MENU_TREE.tsv + .json (681 menus, 492 leaf screens)
_superseded/               V1 collector, V1 void artifacts, old charters
reports/, WATCH.log, RUN_REPORT.txt
```

### On the study server
```
/root/ODOO_MASTER_PASSWD.txt   = admin_passwd in /etc/odoo19.conf  (DB master, NOT a login)
/root/ODOO_ADMIN_PASSWD.txt    = matches nothing, opens nothing
/root/ROOMA_BACKUP/            hardening backups + every grant before-state + logs
/etc/odoo19.conf               list_db=False · dbfilter=^iTest19C$ · http_interface=127.0.0.1
/etc/nginx/sites-available/odoo19   /web/database/ -> 404
```

---

## 3. BOSS DECISIONS ON RECORD

| ref | decision | date |
|---|---|---|
| ERPPLUS-170 | 40 Primary + 8 Reserve, draft 50–52, 5 mandatory fields per question, reworded ≠ new, Reserve must not be swapped in to improve a FAIL/HOLD, no retest without a system or material change | 26 Sep |
| BOSSDEC-002 A | grant 3 scoped rights to the Lane B observer — APPROVED and APPLIED | 26 Sep |
| BOSSDEC-002 B | floor per module = **103** (55 standard + 48 MVQ) → 103 × 247 = **25,441** | 26 Sep |
| Lane model | **Lane A studies · Lane B collects results.** Lane B does NOT answer questions | 26 Sep |
| Screen rule | Lane B must NOT attribute any screen element to a module — one screen is composed of many, and knowing which would require reading source | 26 Sep |
| Reconciler | ChatGPT compares, gives no opinion. Author ≠ reconciler ≠ approver | standing |

---

## 4. OPEN BLOCKERS

| ID | sev | item | state |
|---|---|---|---|
| `RT-SEC-003` | HIGH | observer sits in 7 shared groups incl. *Officer: Manage all employees*, *Show Full Accounting Features* — everything Lane B collected so far was collected with rights wider than a real user | dedicated group 120 created; **removing the excess memberships still needs Boss** |
| `RT-SEC-004` | MED | admin login password is lost; nobody can log into the study server UI | reset via odoo shell — never via SQL, passwords are hashed |
| `RT-LANEB-011` | MED | 8 test records `ROOMB_TEST_OBS_PARTNER*` in ROOMB_TEST | unlink now granted; next clean collector run removes them |
| `RT-LANEB-015` | HIGH | S4/S5 unreachable | largely retired by the census model — Lane B no longer answers permission questions |
| `RT-GOV-003` | — | Boss must not answer study questions (contamination) | closed by Boss ruling |
| `RT-GOV-004` | — | RED TEAM proposed the mechanism that audits Lane A while being Lane A | **open — needs an independent reviewer** |
| `RT-SRC-001` | — | OPL-1 ×95 and AGPL-3 ×149 manifests on `/Volumes/iMacSys` | Boss to decide delete / quarantine / keep |
| `RT-UI-001…011` | — | UI findings | for the Figma stage |

**Withdrawn, do not revive:** `RT-P3-001` (settled by Stack Standard §25 + ADR-0006),
`RT-LANEB-010` (server refused the cross-company write — the permission model worked),
and the claim that `ir.sequence` numbers were consumed (the code only read).

---

## 5. WHAT IS ACTUALLY DONE

```
Lane A batches     0        ← nothing started. This is the real bottleneck.
Lane B W1-STD      16 artifacts, manifest exact, clean room CLEAN
Lane B census      681 menus · 492 leaf screens · 450 distinct destinations · depth 5
                   tree hash c5d68d14e4a59cb46fb448a8ad5cbfd6537c5cf9f159684d7d70eec6bb5dee7d
MVQ for `base`     0        ← blocks Stage 1b and blocks Lane A
CONCEPT_MAP        not needed under the census model
```

**492 leaf screens is the honest denominator for Lane B coverage.**
It cannot be padded, unlike a "100 questions per module" floor — which the
outgoing RED TEAM argued against and Boss has not ruled on. Per-module counts
overlap because one screen draws on several modules.

---

## 6. NEXT ACTIONS

1. **`WATCH.sh` may still be running** (`pid 63605`, started 02:49).
   Stop it with `touch ~/ROOMB_WORKSPACE/STOP`, or let it finish.
   Read `WATCH.log` first — cycle 2 should show whether the registry cache
   clear made the new rights visible (`reachable 6/10`, `cleanup CLEAN`).
2. **Lane A has produced nothing.** It needs its own session — RED TEAM and
   Lane A may never be the same session (V2.0 §1).
3. **MVQ for module `base`** — OVQDT authors, `ops/mvq_gate_ERPPLUS-170.py`
   screens it mechanically before it reaches Boss.
4. **Rewrite the Lane B charter** for the census model. V1.03 is superseded.
   Test every condition against the live account before writing it down.
5. `RT-SEC-003` and `RT-SEC-004` need Boss decisions.

---

## 7. WHAT NOT TO DO

- Do not edit `01_SaaS_Foundation/ARCHITECTURE_DECISION_LOG.md` — Boss ruled
  2026-07-05 it stays untouched. Its ADR numbers collide with the real files
  in `00_Architecture_Office/ADR/` (GAP-KC-04). Cite ADRs by full path only.
- Do not raise a CRITICAL or HIGH blocker without quoting a controlling
  document — path, version, status, text (rule R1). Two blockers were escalated
  across sessions on this project and both were wrong.
- Do not re-derive a value that already has a reference script (rule R2).
- Do not print a password, token or key into chat, log, commit or screenshot
  (V2.0 §21.4). One leaked into this conversation on 26 Sep via a pasted
  terminal buffer; the file it came from turned out to open nothing, but the
  habit is what matters.
- Do not ask Boss to answer study questions — it contaminates the clean room.
- Do not run `stage1a_collector_V2.py` in a loop without confirming the unlink
  right is live. It creates 2 records per run.

---

## 8. GOVERNANCE STATEMENT

```
This is a handover record only.
It is not Boss Final Approval.
No gate closure, merge, release or STATE closure is claimed or authorized.
Section 1 is dated and must be re-verified, not trusted.
```
