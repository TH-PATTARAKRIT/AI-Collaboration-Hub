# P06_DUPLICATE_INGESTION_THREAT_MATRIX.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C06)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**No attack was executed.** All entries are static analyses of reachable code paths.

---

## 1. The threat matrix

Each row: the scenario the prompt requires tested, the door it enters through, whether anything stops it, and the accounting consequence.

| # | Scenario | Door | Stopped? | Consequence | Class |
|---|---|---|---|---|---|
| T-01 | **Same statement file imported twice — CSV** | CSV | **NO** | full second set of lines **and posted entries**; bank overstated | **CONFIRMED DEFECT** |
| T-02 | **Same statement file imported twice — QIF** | QIF | **NO** | as T-01 | **CONFIRMED DEFECT** |
| T-03 | Same statement file imported twice — OFX | OFX | **YES** | filtered, amount added back to `balance_start` | controlled |
| T-04 | Same statement file imported twice — CAMT, `AcctSvcrRef` populated | CAMT | **YES** | as T-03 | controlled |
| T-05 | **Same CAMT re-imported under a different statement name or row order, `AcctSvcrRef` absent** | CAMT | **NO** | identity degrades to `name-date-sequence`; a different key is generated for the same transaction | **CONFIRMED DEFECT** |
| T-06 | **Same transaction in two different imports (e.g. an OFX and a CSV covering one day)** | mixed | **NO** | the two keyspaces never intersect; PATTERN `unique_import_id.*online_transaction_identifier` over `$V18E` → NOT FOUND | **CONFIRMED DEFECT** |
| T-07 | **Transaction fetched by online sync, then also present in an imported file** | sync + file | **NO** | as T-06; the UI itself warns of this | **CONFIRMED DEFECT** |
| T-08 | **Null identity treated as "not a duplicate"** | any of 4 | **NO — fails open at all three points** | the Python filter short-circuits to accept; PostgreSQL NULLs are never equal, so the UNIQUE index is inert | **CONFIRMED DEFECT** |
| T-09 | **Manual keying alongside an import** | manual | **NO** | `unique_import_id` is `readonly=True`, unsettable | **CONFIRMED DEFECT** |
| T-10 | **`copy()` of a statement line** | manual | **NO** | both identity fields are `copy=False`; no `copy` override exists on any of the 7 files declaring/inheriting the model | **CONFIRMED DEFECT** |
| T-11 | **Same real transaction imported into two different journals** | any file door | **NO** | the key embeds `journal.id`, so two journals produce two distinct keys and both are accepted | **CONFIRMED DEFECT** |
| T-12 | **Wrong-company bank transaction** | any | **NO guard in the dedup path** | the pre-import filter is a `sudo()` search with **no company domain**; the constraint is DB-global | **CONFIRMED DEFECT** |
| T-13 | Cross-company bank-account exposure | config | **NO** | `res.partner.bank.company_id` is optional and derived; three guards admit `False` | **CONFIRMED DEFECT** (A4b) |
| T-14 | OCR re-run on the same statement | OCR | partly | OCR is gated on the statement being empty (`is_in_extractable_state = not self.line_ids`), so a re-run on a populated statement is blocked; a **second empty statement** for the same period is not | partial control |
| T-15 | Pending transaction later posts under a new identifier | sync | **unknown** | pendings are never imported; whether the provider re-issues the identifier is a provider contract not in the codebase | **Class D** |
| T-16 | Concurrent sync threads | sync | **partly** | defended by a bare `cr.commit()`, with an in-code comment saying so; no advisory lock, no DB constraint to fall back on | **PLAUSIBLE** |

**Counted: 11 CONFIRMED DEFECT, 1 PLAUSIBLE, 1 Class D, 2 partial/controlled, 1 controlled.**

---

## 2. Why the failure is systematic rather than incidental

**DIT-F-01 — The identity system fails open at three independent enforcement points, and it fails open in the same direction at each.**

1. **Python import filter** — `$V18E/account_bank_statement_import/models/account_journal.py:260-264`:
```
and ('unique_import_id' not in line_vals
or not line_vals['unique_import_id']
or not bool(BankStatementLine.sudo().search([('unique_import_id', '=', ...)], limit=1)))
```
A missing or empty key short-circuits to **import it**.
2. **Python sync filter** — `$V18E/account_online_synchronization/models/account_online.py:301`: a falsy identifier falls through the walrus guard unfiltered.
3. **The SQL constraint** — `unique (unique_import_id)`, single-column. NULLs are never equal in PostgreSQL, so it constrains nothing for exactly the records that have no identity.

**Absence of identity is treated as "not a duplicate", never as "unknown".** That is one design assumption expressed three times, and it is the root of eleven of the sixteen rows above.

**DIT-F-02 — Detection exists, and its own queries prove prevention failed.**
`$V18E/account_online_synchronization/models/account_journal.py:281-294` searches for **repeated `online_transaction_identifier`** — dead code if the Python filter were sufficient. The companion fuzzy query (`:269-279`) matches `currency + amount + account_number + move.date` and **cannot distinguish a duplicate from two genuinely identical transactions** (two identical daily fees will be flagged).
The in-code comment at `:238-239` states the design intent: the fuzzy heuristic exists to catch what the identifier cannot — manual entry, a second file, a mixed source.

**DIT-F-03 — Two silent-drop behaviours hide the evidence of the suppression.**
`:261` discards any transaction with `amount == 0`. `:266-269` adds a *skipped* duplicate's amount back into `balance_start`, **so the statement still foots**. A footed statement is therefore not evidence that nothing was suppressed — and it says nothing at all about an *accepted* duplicate.

---

## 3. What would actually stop this

| # | Control | Why the reference's equivalent fails |
|---|---|---|
| DIT-R-01 | Identity is **mandatory** at ingestion; a bank event with no identity is rejected, not imported | absence is currently read as "unique" |
| DIT-R-02 | Identity is **company-scoped and schema-enforced**, not value-prefixed and DB-global | a collision today is a hard error, not a graceful skip |
| DIT-R-03 | **One identity namespace across all doors** | two keyspaces that never intersect |
| DIT-R-04 | The **inbound end-to-end reference is an identity field**, not a note | CAMT parses it and discards it (IIM-F-03) |
| DIT-R-05 | An **import batch** object, so a re-import is identifiable and reversible as a unit | no such object exists (`P06-B-49`) |
| DIT-R-06 | Every suppression is **recorded** — what was dropped, why, and by which rule | three silent-drop paths, no record |
| DIT-R-07 | Zero-amount events are **recorded, not discarded** | `amount == 0` is dropped at import |
| DIT-R-08 | Manual entry passes the **same** identity gate as import | manual entry cannot even set the field |

---

## 4. Blocker impact

| ID | Status |
|---|---|
| Attack A1 | **CONFIRMED DEFECT — re-verified and expanded from 6 vectors to 11** |
| `P06-B-10` | remains open, evidence class strengthened |
| `P06-B-14` silent-drop behaviours | remains open, mechanism now stated as the reason a footed statement is not assurance |
| `P06-B-29` identity enforced wider than owned | remains open |
| `P06-B-49` no import batch | **NEW**, carried from `26_` |

---

# End
