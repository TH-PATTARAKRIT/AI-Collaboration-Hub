# P08_ORPHAN_DUPLICATE_POSTING_ATTACK

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 · **mandatory attack under the process directive**

This file is an attack on the ledger's integrity assumptions, conducted against the benchmark as evidence. Every attack states its mechanism, the control that should stop it, whether that control stops it, and what would.

## A. Duplicate posting

### `AT-01` — Post the same business fact twice
**Mechanism.** Run the producing process twice, or create the entry manually alongside the generated one.
**Control that should stop it.** An event identity, unique per business fact.
**Does it?** **No.** No accounting-event object exists — `A VERIFIED ABSENCE, scope = the declared 22-root set`. The same fact posted twice yields two equally valid entries and nothing detects it.
**Partial mitigation found.** A duplicated-reference detector exists, but it matches on a **reference string**, covers only customer and supplier documents, and **warns rather than blocks** — it suppresses automatic posting and writes a note. It does not reach manual entries and was not found to reach machine-generated ones.
**What would stop it.** Kernel object `K2` with an idempotency key unique within the tenant, and refusal on collision.

### `AT-02` — Post the same fact twice through two different books
**Mechanism.** A manual entry may be booked into **any** book, not only a miscellaneous book; the confinement is a screen-level field domain, not a constraint. The duplicate consumes a different number series and is invisible to any per-book check.
**Does anything stop it?** No.

### `AT-03` — Import the same file twice
**Mechanism.** The bulk import bridge creates entries with an **operator-supplied number** taken from the spreadsheet. The database's uniqueness index covers only **posted** entries, so duplicates accumulate undetected in the unposted population and collide only at posting.
**Does anything stop it?** Not before posting. A genuine cross-run import identity check exists in one optional module only, and that check is **table-global with no company scoping**.

## B. Orphan posting

### `AT-04` — Create a journal entry with no business document
**Mechanism.** A manual entry, by design.
**Control.** None is intended; the attack is that an orphan entry is **indistinguishable** from a derived one after the fact, because no field says which is which.

### `AT-05` — Strip a generated entry of its origin
**Mechanism.** The provenance references are ordinary writable fields with no validation and no deletion guard. Write them to empty.
**Control.** The change log that would record it is a **company-level option that is off by default**.

### `AT-06` — Give a manual entry an origin it never had
**Mechanism.** The same writable fields, written to a real document's identifier.
**Control.** None found in the searched scope (`B NOT FOUND IN SEARCHED SCOPE`).

### `AT-07` — Post an entry with no lines at all
**Mechanism.** The documented posting action refuses an entry with no accountable line. A **generic attribute write that merely sets the status** does not run that check — it runs only the lock checks, the balance assertion and the seal. An entry with zero lines has a zero balance and passes.
**Does it work?** The code paths are `FACT VERIFIED`; end-to-end reachability is `SUPPORTED INTERPRETATION`. **This is the second posting door, and it is the one with no validation.**

### `AT-08` — Re-parent a journal item to a different entry
**Mechanism.** A link command on an entry's item collection moves an existing item from one entry to another. Both entries enter the balance container, so the operation succeeds whenever both remain balanced.
**Effect.** The item's parent entry — and therefore its number, its book and its audit position — is mutable.

### `AT-09` — Append items to an already-posted entry
**Mechanism.** The deletion path checks the parent's posted state; the **creation path does not**. Balanced pairs may be added to a posted entry, and the period check on that path fires only for items affecting a tax return.

## C. Attacks on the invariant itself

### `AT-10` — Post an unbalanced entry
**Mechanism.** Supply the balance-suppression key in the calling context. The framework's remote-call entry point applies the caller's context dictionary to the object **wholesale**, with no allowlist, denylist, key validation or type check found at the dispatch layer.
**Control.** None at the persistence layer: **no database constraint enforces per-entry balance in any of the declared 22 roots** (`RS-A-03`).
**Status.** `FACT VERIFIED` for the mechanism and for the dispatch behaviour; `SUPPORTED INTERPRETATION` for exploitation, which was not executed. Product code itself uses the suppression key in the point-of-sale close path.
**Severity.** This is the most severe finding in the package. The defining invariant of double-entry bookkeeping is a request parameter.

### `AT-11` — Post an entry balanced in the reporting currency and unbalanced in its transaction currency
**Mechanism.** The balance assertion sums the reporting-currency amount only. The transaction-currency amount is never summed by any constraint.
**Control.** None.

### `AT-12` — Edit a posted entry's protected attributes
**Mechanism.** Supply the readonly-suppression key. Product code uses it at seven places.
**Control.** The protected set is nine header attributes and is waived by that key. The entry number, external reference and narrative are **not in the set at all**.

### `AT-13` — Edit a posted journal item in place
**Mechanism.** No reopen and no reversal required. From the standard line listing, in bulk: account, counterparty, label, reference, cost allocation and tax classification, whenever the period is open and the item is unmatched. Label, due date, reference and cost allocation carry **no check at all**.
**Control.** None. **This is the correction path most likely to be used in practice and it has the fewest checks.**

### `AT-14` — Narrow the seal so the entry number falls outside it
**Mechanism.** The sealed-attribute set is chosen by a **caller-supplied version value**; the older version's set omits the entry number.
**Status.** `FACT VERIFIED` for the mechanism; `SUPPORTED INTERPRETATION` for exploitation.

### `AT-15` — Delete a posted entry
**Mechanism.** Three guards, each with a defeat: the chain guard is waived for any administrator, for any company in simplified-entry mode, and by a caller-supplied key; the retention guard depends on a company setting that is **off by default** and is waived by the same key; the seal guard applies only where sealing was enabled.
**Evidence left.** A **server log line**, not a database record.

### `AT-16` — Renumber posted entries
**Mechanism.** An administrative tool renumbers a selection in one book. Its seal safeguard blocks only date-based reordering; sequence-preserving renumbering is permitted, and during the operation the affected rows leave the uniqueness index entirely.

## D. Attacks that cross a boundary

### `AT-17` — Rewrite a posted fact from outside accounting
**Mechanism.** Counterparty consolidation — a contacts-role operation — rewrites the counterparty on **posted** items, across every company, with the period-lock check **explicitly suppressed** by an internal sentinel.
**Note on the sentinel.** It is an object-identity comparison and therefore **cannot** be forged from a client-supplied context. The attack is not a context injection; it is that a legitimate tenant-scope operation was given the ability to reach company-scope posted facts. Class `SV-3` in the scope matrix.
**Control.** The operation refuses when the surviving counterparty's tax identity differs, and refuses on sealed entries. **Unsealed entries — the default — absorb the change silently**, and the message is logged on the counterparty, not on the affected entries.

### `AT-18` — Settle across two companies and put the whole difference in one
**Mechanism.** The settlement company guard compares the **root** of the company tree, not the company. The difference entry then selects **one** company by recordset position and posts the entire gain or loss there, with no compensating entry in the other, no error and no warning.
**Status.** Both code facts `FACT VERIFIED`, reported independently by two agents of this session. End-to-end reachability `SUPPORTED INTERPRETATION`.

### `AT-19` — Create settlement records directly
**Mechanism.** Both settlement models grant create, write and delete to the billing tier and carry **no isolation rule of any kind**. The five eligibility guards live in the calling routine, not in the models, so a direct write reaches none of them.

### `AT-20` — Defeat the access model entirely from the custom layer
**Mechanism.** A module in the project's custom addon set overrides the framework's access-check routine on the **universal abstract base object** — that is, on every model in the system, including the entry and the item — and returns *permitted* **before** both the permission check and the isolation check. It never calls the inherited implementation. The grant table that drives it is **create/read/update/delete for every internal user**, its user link is unrestricted, and **no isolation rule exists on it**.
**Boundary, stated precisely.** Search filtering runs through a different path and is **not** overridden, so search results remain isolated. **Read, write and delete on known record identifiers do not.**
**Status.** `FACT VERIFIED` — read directly and independently confirmed by this session's lead author after an agent reported it. Whether the module is installed in any deployment is `C NOT YET SEARCHED`.
**Severity.** This is the most severe finding in the custom layer and, if the module is deployed, it subsumes every other control in this file.

### `AT-21` — Erase the ledger from a settings screen
**Mechanism.** A custom module builds `delete from <table>` from a model name and executes it with an immediate commit, per table, applying it to the item, entry, settlement, payment and analytic tables, then resets the number series. **No company predicate appears in any statement** — the delete is whole-table, therefore whole-database, across every company. Because it never passes through the object layer it is constrained by no posted-state guard, no retention option, no seal, no lock date and no isolation rule. A failure part-way through is **committed**, not rolled back.
**Status.** `FACT VERIFIED` for the code. The menu entry is restricted to the system-administrator group; whether the underlying methods are reachable by a lower-privileged direct call is `D UNKNOWN`.

### `AT-22` — Backdate by discarding identity
**Mechanism.** A custom utility returns posted entries to unposted, **sets the number to empty**, overwrites the date and the document date with an operator-chosen value, and re-posts — allocating a new number and leaving the original as an unexplained gap. It also rewrites an inventory valuation timestamp by direct database statement.
**What survives.** The period lock still applies through the unpost/repost cycle. **Entry identity and number continuity do not.**

## E. Result

| Attack class | Stopped by the benchmark | Not stopped |
|---|---|---|
| Duplicate posting | — | `AT-01`, `AT-02`, `AT-03` |
| Orphan posting | — | `AT-04`..`AT-09` |
| Invariant attacks | — | `AT-10`..`AT-16` |
| Boundary attacks | — | `AT-17`..`AT-22` |

**Twenty-two attacks. None is stopped outright.** Three are mitigated in part: duplicate detection warns on document references; the lock-bypass sentinel is unreachable from a client context; and settlement search filtering survives the custom access override.

The pattern across all twenty-two is one thing: **every control in the benchmark's ledger is enforced in application code, and application code is reachable from callers that can choose not to run it.** The four controls that live below application code are per-item sign and non-null checks and a partial uniqueness index on the entry number — none of which is an accounting invariant.

`P08-T0-01` — the entry-balance invariant must be enforced where a caller cannot reach it. This is the single most important requirement in the package.
