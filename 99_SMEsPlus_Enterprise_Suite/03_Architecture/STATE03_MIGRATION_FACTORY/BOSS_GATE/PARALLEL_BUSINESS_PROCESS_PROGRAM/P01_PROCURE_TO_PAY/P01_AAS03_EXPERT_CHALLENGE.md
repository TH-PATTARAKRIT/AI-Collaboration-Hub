# P01 — FOUR-EXPERT (AAS-03) CHALLENGE

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.** Expert reports themselves carry reference-system
citations and are held in `_expert_out/` as Layer 2 working material.

Per `§2.9`, four expert perspectives were obtained **independently and on disjoint
assignments**, so that each produced primary evidence rather than a review of a draft. Per
`EC-07`, *Independent Review ≠ Truth* — every finding admitted below was **re-derived from
source by this session** before admission.

---

## 1. HOW THE CHALLENGE WAS RUN, AND ITS LIMITS

| | |
|---|---|
| Experts | Functional Design · Database Design · Integration & Localization · Code & UI Architect |
| Assignments | Disjoint by design; each brief named the others' territory as out of scope |
| Adversarial instruction | Every brief carried *"if any path in this brief is wrong, report it as a finding"* |
| Method rules imposed | Denominator rule; negative-claim classes A–E; no PASS wording; prove the executor; symmetric cross-version comparison |
| Returned at time of writing | **Three of four.** Database Design was still running. |
| **Limitation 1** | The briefs were issued **before** the scope-aware constitution correction arrived, and the correction **could not be forwarded** — inter-agent messaging is disabled in this session. See `REV-P01-02`, `DEP-P01-06`. |
| **Limitation 2** | Experts read source. **No expert executed anything.** Every finding below is a source reading. |

---

## 2. WHAT THE CHALLENGE CHANGED IN THIS SESSION'S OWN WORK

This is the part that matters most, and it is stated first.

| # | The session's position | What an expert did to it |
|---|---|---|
| 1 | Population A — "modules that depend on the purchase module" — was declared with two false-negative modes | **Boundary defect found.** The population was a direct-dependency set, not a closure. Landed costs and subcontracting purchase — both required by the directive — were outside it. `ERR-P01-04` |
| 2 | The expert brief named `period_lock_date` and a `bypass_lock` flag | **Both are wrong.** The field does not exist; the two purchase-relevant lock dates were omitted from the brief entirely. `ERR-P01-05` |
| 3 | `EV-P01-06`: the receipt entry's date is a context override, else a linked bill line's date, else system-today | **Confirmed for the older generation, then refined twice and contradicted for the newer one.** The context override has exactly one setter — inventory adjustment — so **branch 1 is unreachable from a purchase receipt**. The newer generation removed the middle branch, leaving the date unconditionally "the posting user's today". `EV-P01-49` |
| 4 | Three-way match: advisory, zero tolerance, converted at today's rate | **Extended**: it is also **discount-blind** — it compares gross unit price while a discount field exists |
| 5 | The down-payment wizard converts bill lines into down-payment lines | **A second action on the same wizard was missed**: it also creates a purchase order from the bill's own prices and confirms it in the same transaction. Both actions exist; the session's finding was incomplete, not wrong |

**Three of this session's four self-identified errors were caught by the session itself; the
one that changed a denominator was caught from outside.** That is consistent with the
programme's standing observation and is reported, not smoothed over.

---

## 3. EXPERT 1 — FUNCTIONAL DESIGN (returned)

30 findings, 5 source-derived populations, 15 challenge positions, 2 self-corrections recorded.

### Admitted after independent re-derivation by this session

| Finding | Re-verified | Evidence ID |
|---|---|---|
| Bill↔order auto-matching carries **no vendor clause** on either branch that matches a quoted order reference; only the last-resort amount branch tests the vendor | Yes — refined: the vendor clause exists on one branch of three | `EV-P01-39` |
| The match tolerance is a hard-coded, currency-agnostic constant, identical in both generations | Yes | `EV-P01-40` |
| On a match, the **vendor's own bill lines are cleared and replaced** by the order's lines — and this fires on the branch that by its own comment means *the totals did not match* | Yes — the branch comment reads "We did not find a match for the invoice total" | `EV-P01-41` |
| A wizard creates a purchase order **from the vendor bill's own prices** and confirms it in the same transaction | Yes | `EV-P01-42` |
| Order reset-to-draft has **no server-side guard of any kind**, in both generations | Yes | `EV-P01-43` |
| The shipped access-control grid gives the accounting-invoicing group **write** on the purchase order and its lines | Yes — and **wider than the expert stated**, and identical across generations | `EV-P01-44` |
| Two-step approval is satisfied unconditionally by group membership; the threshold is converted from the wrong company's currency | Yes, both halves | `EV-P01-45` |
| The guard against reducing ordered quantity below received quantity exists in the older generation and not in the newer | Yes — newer-generation negative is class **B** | `EV-P01-46` |

### The expert's own discipline

Two self-corrections were recorded before publication: a path-splitting error that would have
produced "the purchase module has no model files", and a line-count of zero on a file with no
trailing newline that **would have produced a false "this module's code is never imported"
claim** — withdrawn before publication and logged. The second is precisely the class of
negative the project's standard exists to stop.

### Carried but not yet re-verified

Product-identity-only bill-line matching; silent deletion of unmatched bill lines; an operator-
precedence defect in view SQL present in both generations; a context-flag bypass of the
alternative-quotation control; the custom purchase-request approver check being skipped when no
approver resolves; a vendored copy of the three-way-match module that is an older hybrid on a
newer base. **Each stays SUPPORTED INTERPRETATION until re-derived.**

---

## 4. EXPERT 3 — INTEGRATION & LOCALIZATION (returned)

20 statutory entries, **all** `HOLD — STATUTORY EVIDENCE REQUIRED`. No claim about Thai law is
asserted anywhere in its report. Four populations declared with false-negative modes; 15
negative claims classed. It also reported that **five modules containing withholding logic were
not named in its brief**, and that five of the brief's module claims were wrong.

### Admitted after independent re-derivation by this session

| Finding | Re-verified | Evidence ID |
|---|---|---|
| **Withholding on a partial vendor payment compounds instead of netting.** The already-withheld amount is subtracted as *debit − credit*; on a vendor payment that quantity is negative, so each subsequent payment **increases** the amount withheld | Yes — the arithmetic is as stated, purchase-side only | `EV-P01-52` |
| **The certificate form classification is inverted between two shipped copies of the same module** — same file, same two lines, opposite mapping of a corporate counterparty | Yes — read directly in both copies | `EV-P01-53` |

### Carried, high severity, not yet re-verified

- Two parallel and incompatible withholding mechanisms coexist, are auto-mirrored into each
  other, and the reporting layer unions both sources.
- The purchase-tax report is gated by an exact comparison against an **English literal tax-group
  name**, so adding a translation would empty the report.
- Nine independent withholding formulas, two of them in vendor-facing documents that never net
  prior payments — so the document handed to the vendor and the ledger disagree by construction.
- Reporting completeness depends on a manually-created certificate; a payment with withholding
  and no certificate is invisible to the statutory report.
- Deposits to vendors post to an **expense** account; the bill is created with elevated privilege.

### The expert's own discipline

Three of its own plausible high-severity hypotheses were **contradicted on verification and
recorded as contradicted** rather than dropped.

### Statutory position

**Nothing in this package states what Thai law or the Thai Revenue Department requires.** Both
verified findings above are statements about source behaviour. `DEP-P01-04` remains open, and
the inversion in `EV-P01-53` means **at least one shipped copy classifies every certificate
onto the wrong form** — which of the two is wrong cannot be determined without statutory
evidence.

---

## 5. EXPERT 4 — CODE & UI ARCHITECT (returned)

60 findings. Corrected two identifiers in its own brief.

### Admitted after independent re-derivation by this session

| Finding | Re-verified | Evidence ID |
|---|---|---|
| `period_lock_date` does not exist; the real set includes **`purchase_lock_date`**, which the brief omitted | Yes — the brief was wrong | `EV-P01-47` |
| **The soft lock does not block — it rewrites the date.** On a lock violation the posting routine moves the entry's date forward and posts it | Yes | `EV-P01-48` |
| The context override that could force a valuation entry's period has **exactly one setter**, the inventory-adjustment path, so it is unreachable from a purchase receipt | Yes — full-root grep, 8 references, 1 setter | `EV-P01-49` |
| **A missing exchange rate silently resolves to a fallback with no date filter, then to 1.0.** Identical in both generations; the newer one adds further unconditional fallbacks | Yes | `EV-P01-50` |
| Entry hashing and the audit trail are booleans **with no default** — off unless switched on | Yes | `EV-P01-51` |

### Its challenge of this session's own finding — the most valuable single result

Instructed to confirm, refine or contradict `EV-P01-06`, it did all three:

- **Confirmed** the three branches verbatim for the older generation.
- **Refined**: branch 1 is dead in procure-to-pay (one setter, inventory adjustment).
- **Refined**: branch 3 diverges *systematically*, not incidentally — the journal entry takes
  the acting user's local "today" while the movement and the valuation layer are in UTC, so a
  user in a positive-offset timezone validating shortly after midnight puts them in
  **different months**.
- **Contradicted for the newer generation**: the middle branch was removed, so a receipt there
  is dated the posting user's today, unconditionally.

`EV-P01-06` is amended accordingly in `P01_RECEIPT_VALUATION_MATRIX.md` and
`P01_EVENT_TO_GL_MATRIX.md`.

### Carried, high severity, not yet re-verified

- The **purchase lock date never protects goods receipt**, because the lock is selected by
  journal type and the valuation journal is a general journal.
- The custom effective-date module resets a posted entry to draft, blanks its number, re-dates
  and re-posts it, **then rewrites the valuation layer's creation timestamp by raw SQL** — and
  that timestamp is the layer's only temporal anchor *and* its ordering key, so the rewrite
  reorders valuation history outside the ORM entirely.
- One counterweight it verified: enabling entry hashing on the purchase journal would close
  the deletability hole, the partner-based lock bypass and the backdating tool's first step at
  once.

---

## 6. EXPERT 2 — DATABASE DESIGN (not returned at time of writing)

Constraints, indexes, identity, immutability, deletion paths, access rules and company scoping
remain **class C — not yet searched** by this package, except where another expert or this
session touched them incidentally.

The scope questions its brief was to settle — and which the constitution correction re-framed
mid-flight — are carried as `DEP-P01-02` and `DEP-P01-06`.

---

## 7. WHERE THE EXPERTS DISAGREE, AND WITH THIS SESSION

Per `§2.9`, consensus is not forced.

| Subject | Positions | Resolution |
|---|---|---|
| Receipt-entry date | Session: three branches. Expert 4: three branches in the older generation, **two** in the newer, and branch 1 unreachable in procure-to-pay | **Expert 4 governs.** Re-derived and confirmed |
| Access-control exposure | Expert 1: write on order lines. This session: write on the order, its lines **and** the matching object, in **both** generations | **This session's wider reading governs**, after correcting its own first attempt (`ERR-P01-03`) |
| Down-payment wizard | Session: converts bill lines to down-payment lines. Expert 1: creates and self-confirms an order from the bill | **Both are true** — two actions on one wizard. The session's account was incomplete |
| Backdating and lock dates | Expert 3: lock dates are **not** bypassed in the custom roots (class A) — the ORM path raises. Expert 4: the same custom module escapes via raw SQL on the valuation layer | **Not a contradiction.** Expert 3 is right about the accounting lock; Expert 4 is right that the raw-SQL step is outside it. Both stand |

---

## 8. WHAT THE CHALLENGE DID NOT DO

- It did not run anything. No expert executed a transaction or queried a database.
- It did not settle which generation or which copy is deployed — and **six of Expert 1's
  findings, most of Expert 3's, and one of Expert 4's are conditional on that** (`DEP-P01-01`).
- It did not cover the database-design assignment.
- It was not briefed under the corrected scope constitution (`DEP-P01-06`).
- It is **not** two consecutive clean independent passes. It is one partial pass, and it
  surfaced new material populations and new gating unknowns — which under `EC-07` is the
  definition of *not* clean.
