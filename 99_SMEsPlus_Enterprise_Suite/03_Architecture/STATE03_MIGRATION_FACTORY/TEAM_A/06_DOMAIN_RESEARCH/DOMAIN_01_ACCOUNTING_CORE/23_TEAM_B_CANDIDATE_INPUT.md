> DOMAIN_01 — Accounting Core | Team A (Maker) | READ ONLY | No target design | Boss sole Final Approver

# 23 — TEAM B CANDIDATE INPUT

**GATED.** Nothing here is approved input. Every item requires **ChatGPT Audit + PMO + Boss
Gate** before Team B may receive it. Team B is not activated. No design is expressed.

## A7 NEUTRALIZATION — applied to each critical finding
Format: Source Technical Fact → Business Meaning → Business Fact → Generic Concept → Migration Relevance

### N-01 — Balance enforcement **[CORRECTED CORR-001]**
- **Source technical fact:** `_check_balanced` (`account_move.py:2765`) raises UserError and is wrapped in `_disable_recursion(..., 'check_move_validity')`. The database **does** carry four row-level CHECK constraints on `account_move_line`, but a row-level CHECK cannot express an aggregate across an entry, and the database has **zero triggers** (directly verified).
- **Business meaning:** the books are kept balanced by the application, and that guard can be switched off.
- **Business fact:** a financial record can exist that does not balance.
- **Generic concept:** *the double-entry invariant must be guaranteed, and the guarantee must not be optional.*
- **Migration relevance:** verify balance on every migrated entry; do not assume source validity.

### N-02 — Correction model
- **Source technical fact:** states are draft/posted/cancel; `reversed_entry_id` links a separate opposing move; `button_draft` accepts posted and cancelled.
- **Business meaning:** history can be corrected either by rewriting the original or by posting an opposing entry.
- **Business fact:** two correction routes exist with different audit consequences.
- **Generic concept:** *a correction policy must be explicit, and reversal is a relationship between records, not a status on one.*
- **Migration relevance:** carry reversal linkage as data; never key logic on a "reversed" status.

### N-03 — Period control
- **Source technical fact:** six company lock-date fields incl. `hard_lock_date`, per-user computed variants, plus `account.lock.exception`.
- **Business meaning:** "the books are closed" is expressed by several overlapping controls and can be overridden for a window.
- **Business fact:** period closure is multi-dimensional and overridable, and overrides are audited.
- **Generic concept:** *period control needs one unambiguous answer to "is this period open for this posting?", with auditable exceptions.*
- **Migration relevance:** must understand all six controls before interpreting historical postings.

### N-04 — Tamper evidence
- **Source technical fact:** `restrict_mode_hash_table` per journal (opt-in), `inalterable_hash`, `secure_sequence_number`.
- **Business meaning:** ledgers are tamper-evident only where somebody enabled it.
- **Business fact:** immutability coverage in the source data is partial and configuration-dependent.
- **Generic concept:** *ledger integrity guarantees should be a property of the ledger, not a per-journal option.*
- **Migration relevance:** determine per journal whether history is hash-protected before trusting it.

### N-05 — Monetary representation
- **Source technical fact:** debit/credit/balance/amount_currency all `numeric`; three columns for a two-value concept.
- **Business meaning:** money is exact; the signed/unsigned representation is stored redundantly.
- **Business fact:** exact decimal money is correct; redundancy is an integrity liability.
- **Generic concept:** *money is exact decimal; a single authoritative amount representation avoids disagreement.*
- **Migration relevance:** normalize the trio; preserve exactness.

## ADVANCEMENT CANDIDATES
`ADVANCEMENT_CANDIDATE — TEAM B INPUT ONLY AFTER AUDIT` (all of them). No solution designed.

| ID | Reference capability | Observed limitation / risk | Business pain point | Improvement opportunity (concept only) | Evidence |
|---|---|---|---|---|---|
| ADV-01 | Balance enforcement | Application-only, suppressible, no DB backstop | Unbalanced data can exist and be discovered late | *Make the invariant non-optional and enforced at the point of persistence* | SE-03/04, DB |
| ADV-02 | Tamper evidence | Opt-in per journal | Integrity coverage is uneven and configuration-dependent | *Integrity as a default property of the ledger* | SE-22/23 |
| ADV-03 | Period control | Six overlapping locks + per-user variants + exceptions | Hard to answer "is this period closed?" | *One authoritative period-state answer, with audited exceptions* | SE-24/25/26 |
| ADV-04 | Correction model | Reset-to-draft mutates posted history | Audit trail weakened by design | *Correction that never rewrites posted history* | SE-11/12 |
| ADV-05 | Document typing | One table for entries/invoices/bills via `move_type` | Semantic overload; every consumer must branch | *Explicit separation of ledger posting from commercial documents* | SE-02 |
| ADV-06 | Monetary columns | debit+credit+balance trio | Three columns can disagree | *Single authoritative amount representation* | DB, MM-02 |
| ADV-07 | Derived state | `parent_state` denormalized to lines | Drift possible between header and lines | *Derive, don't duplicate, state* | DB |

## CORRECTION NOTE (CORR-001)
N-01 previously rested on "0 CHECK constraints in the database". That was an artefact of a
derived inventory which cannot represent CHECK constraints. Direct observation shows CHECK
constraints **do** exist; the neutralized business concept is unchanged, but its evidence is now
correct and narrower in scope: it concerns **entry-level** balance only.

Independent triangulation added this round strengthens two candidates:
- **ADV-04** — SAP Business One *prevents* deleting or editing a posted journal entry, permitting
  only reversal, explicitly to protect the audit trail. The reference system permits reset-to-draft.
- **ADV-03** — NetSuite expresses period control as one period with three states plus a single
  override permission, against the reference system's six lock fields, per-user variants,
  exception object and bypass context.

Both remain `ADVANCEMENT_CANDIDATE — TEAM B INPUT ONLY AFTER AUDIT`. No solution designed.
No target code, schema, API, DTO, class, service or workflow appears in this pack.
