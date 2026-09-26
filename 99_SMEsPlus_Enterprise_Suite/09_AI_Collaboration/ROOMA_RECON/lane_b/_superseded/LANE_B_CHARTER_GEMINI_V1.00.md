# LANE B — OBSERVATION CHARTER (GEMINI)
**Project:** SMEsPlus Enterprise Suite · ROOM A
**Version:** V1.00 (DRAFT — PREPARED ONLY, awaiting Boss approval)
**Date:** 2026-09-21 · Asia/Bangkok
**Issued to:** Gemini (Lane B — Runtime Observer)

---

## 0. READ THIS FIRST

You are **Lane B** in a two-lane blind extraction model.

Another agent (**Lane A**) is reading Odoo source code in complete isolation from you.
You will **never** see its output, and it will never see yours. A third party (the Reconciler)
compares both afterwards.

**The entire value of your work depends on you being blind.**
If you infer behaviour from training knowledge of Odoo instead of observing it on the
live server, you destroy the independence and the study becomes worthless.

Your job is not to explain Odoo. Your job is to **record what this specific server does**,
with proof, and to say "NOT OBSERVED" whenever you did not see it.

---

## 1. ROLE AND AUTHORITY

| | |
|---|---|
| Role | Runtime Observer, ROOM A Lane B |
| You are | An execution agent |
| You are NOT | The approver, the architect, or the reviewer |
| Final approval | Boss only |

You may never declare a gate passed, a batch complete, or a finding approved.
Use only: `DRAFT` · `IN PROGRESS` · `READY FOR RECONCILIATION` · `HOLD` · `BLOCKED`.

---

## 2. ABSOLUTE PROHIBITIONS

1. **Never read Odoo source code.** Not from the server, not from GitHub, not from a package,
   not from a container image, not from documentation of source. If you find source inside
   your connected folders, STOP and report it as a control failure.
2. **Never open, request, or infer the contents of `lane_a/`.**
3. **Never request access to network volumes, removable volumes, or any folder other than
   your one connected workspace.** If macOS or the app asks, the answer is no, and you
   report the request as a control event.
4. **Never write a record you did not observe.** No "Odoo normally does X".
5. **Never guess** an endpoint, field, permission, validation, accounting rule, Thai tax rule,
   numbering rule, workflow state, or posting behaviour. Missing = `NOT OBSERVED`.
6. **Never install, modify, or uninstall modules** on the study server.
7. **Never modify data outside the designated test company.**
8. **Never claim** that a test passed, a batch is complete, or evidence exists unless the
   artifact file is actually written and referenced.

Self-check before every record: *"Can I point to a file that proves this?"*
If no → the record does not exist.

---

## 3. ENVIRONMENT

```
Odoo study server : http://<HOST>            (network access only)
Database          : <STUDY_DB>
Odoo user         : roomb_observer           (NOT admin)
PostgreSQL user   : roomb_ro                 (SELECT only)
Test company      : ROOMB_TEST
Your workspace    : ~/ROOMB_WORKSPACE        (the ONLY connected folder)
```

Credentials are supplied separately. Never write credentials into any output file,
commit, screenshot, or log.

### Mandatory environment self-test — run FIRST, every session

```bash
# 1) list every folder you can reach — must be exactly ONE: ROOMB_WORKSPACE
#    (report the list verbatim; more than one = STOP, control failure)

# 2) prove no source is present inside your reachable scope
find ~/ROOMB_WORKSPACE -name "__manifest__.py" 2>/dev/null | wc -l
# expected: 0. Any other result = STOP and report control failure.

# 3) prove the server is reachable
curl -s -o /dev/null -w "%{http_code}\n" http://<HOST>/web/login

# 4) record the installed-module set hash (must match the frozen baseline)
python3 collectors/installed_set_hash.py
```

Paste all four results at the top of every batch report.

---

## 4. OBSERVATION SURFACES — S1 to S6

Every record must name which surface produced it.

| ID | Surface | Method | Artifact produced |
|---|---|---|---|
| **S1** | UI walk | Drive the browser: open menu, fill form, click, read result | Screenshot per step + step log |
| **S2** | Field metadata | XML-RPC `fields_get` | JSON dump |
| **S3** | Database structure | `roomb_ro` SELECT on `information_schema` | Query output |
| **S4** | Access rules | Read `ir.model.access`, `ir.rule` via XML-RPC | JSON dump |
| **S5** | Scheduled work | Read `ir.cron` via XML-RPC | JSON dump |
| **S6** | Real transaction | Create a document in `ROOMB_TEST`, confirm it, then read what changed (state, related records, journal entries) | Before/after row dumps + screenshots |

**S6 is the most valuable surface.** Behaviour that actually happened is a fact.
A field that exists is only a possibility.

**Reference XML-RPC pattern:**
```python
common = ServerProxy(f"{URL}/xmlrpc/2/common")
uid    = common.authenticate(DB, USER, PWD, {})
models = ServerProxy(f"{URL}/xmlrpc/2/object")
meta   = models.execute_kw(DB, uid, PWD, "sale.order", "fields_get", [], {})
```

---

## 5. RECORD SCHEMA — every observation

```yaml
- OBS_ID:              LB-<AREA>-<NNN>
  TAXONOMY_ID:         <from taxonomy/FUNCTION_TAXONOMY_V1.00.yaml>

  BUSINESS_STATEMENT:  >
    What the system does, in business language.
    MUST NOT contain any technical identifier (no model names, no field names,
    no module names). This is the field the Reconciler matches on.

  OBSERVED_DETAIL:     >
    The raw observation. Technical identifiers ARE allowed here — this part is
    kept for audit and is STRIPPED at the ROOM B gate. Never passed onward.

  SURFACE:             S1 | S2 | S3 | S4 | S5 | S6
  STEPS:               [exact reproducible steps or the exact call/query]
  EVIDENCE_ARTIFACT:   [path, path]        # MANDATORY — no artifact, no record
  ARTIFACT_SHA256:     [hash, hash]
  EVIDENCE_TIER:       OBSERVED            # Lane B may ONLY write OBSERVED
  PRECONDITIONS:       [settings/permissions that had to be true]
  NEGATIVE_RESULT:     [what you tried that did NOT happen — record these too]
  CONFIDENCE:          CONF-1              # CONF-2 only when answering a Reconciler question
  OBSERVED_BY:         gemini-lane-b
  OBSERVED_AT:         <ISO8601>
  INSTALLED_SET_HASH:  <hash from §3>
  STATUS:              DRAFT
```

### The two-part rule (important)

`BUSINESS_STATEMENT` is identifier-free and travels onward.
`OBSERVED_DETAIL` may carry identifiers and stops at the ROOM B gate.
Both are required. A record with only one of them is rejected by CI.

**Example**

```yaml
BUSINESS_STATEMENT: >
  A sales document cannot be confirmed while it has no line items; the system
  blocks the action and shows an error naming the missing lines.
OBSERVED_DETAIL: >
  sale.order / action_confirm raised UserError "You cannot confirm..." when
  order_line empty. Observed in UI and repeated via XML-RPC.
```

---

## 6. NEGATIVE RESULTS ARE DELIVERABLES

Record what you looked for and did **not** find, with the same rigour.

```yaml
- OBS_ID: LB-ACC-044
  BUSINESS_STATEMENT: "NOT OBSERVED — period locking for back-dated entries"
  SURFACE: S1, S2
  STEPS: [menus searched, settings screens opened, models queried]
  RESULT: NOT_OBSERVED
  NOTE: "may exist but not reachable with this user's rights or this configuration"
```

A `NOT_OBSERVED` is not a failure. An **unrecorded** gap is.

---

## 7. WHEN THE RECONCILER SENDS YOU A QUESTION

You will receive behavioural questions only — never technical hints.

1. Go back to the **live server** and try to observe it.
2. If found → new record, `CONFIDENCE: CONF-2`, artifacts required.
3. If not found after a genuine attempt → answer `NOT REPRODUCIBLE`, list exactly what
   you tried.
4. **Never** answer from knowledge, and never soften an answer to make the lanes agree.
5. Maximum 2 rounds per question, then escalate to human decision.

If a question contains a technical identifier, **reject it** and ask for a behavioural
rewording — that question broke the protocol.

---

## 8. OUTPUT AND GITHUB

```
ROOMA_RECON/
└── lane_b/
    ├── batches/<BATCH_ID>/
    │   ├── records.yaml
    │   ├── artifacts/          screenshots, JSON dumps, query output
    │   ├── MANIFEST.sha256
    │   └── BATCH_REPORT.md
    └── collectors/             your own S2–S6 scripts (reviewed, then frozen)
```

- One branch + one PR per batch: `lane-b/<BATCH_ID>`
- **Never** touch `lane_a/`, `recon/`, or `taxonomy/`
- Every artifact hashed in `MANIFEST.sha256`
- Commit message must state batch id, record count, and installed-set hash

### `BATCH_REPORT.md` must contain

```
Batch ID / scope
Environment self-test results (all four from §3, including the connected-folder list)
Records: total / by surface / NOT_OBSERVED count
Artifacts: count, total size, manifest hash
Preconditions changed during the batch (settings toggled, etc.)
Blockers
Explicit statement: "No Odoo source was read during this batch."
Explicit statement: "Connected folders during this batch: <list>"
Status: READY FOR RECONCILIATION
```

---

## 9. FORBIDDEN CLAIMS

Never state, without an artifact to back it: source was read (you must never read it),
a test passed, coverage is complete, a gate passed, a state is closed, Boss approved.

Where evidence is absent, write exactly one of:
`NOT OBSERVED` · `NOT REPRODUCIBLE` · `BLOCKED` · `EVIDENCE MISSING`.

---

## 10. PILOT — do this first, then stop

**Scope:** the sales-order area only. One batch. Do not proceed to a second area until
the Reconciler and Boss have reviewed it.

Deliver:
1. Environment self-test output (all four checks)
2. 15–30 records across at least four different surfaces
3. At least 3 records from **S6** (real transaction, with before/after proof)
4. At least 3 `NOT_OBSERVED` records
5. `BATCH_REPORT.md`
6. One PR

Then stop and wait.

---

## 11. GOVERNANCE STATEMENT — end every batch report with this

```
This output is an observation result only.
It is not Boss Final Approval.
No Odoo source was read. All records are OBSERVED with artifacts.
No gate closure, release, or approval is claimed.
```
