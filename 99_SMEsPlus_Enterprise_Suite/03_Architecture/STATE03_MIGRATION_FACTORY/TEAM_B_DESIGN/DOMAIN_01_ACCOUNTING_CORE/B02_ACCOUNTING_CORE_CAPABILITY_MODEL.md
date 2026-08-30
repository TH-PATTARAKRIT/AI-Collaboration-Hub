# B02 — Accounting Core Capability Model

| Field | Value |
|---|---|
| Domain | DOMAIN_01 — Accounting Core |
| Phase | B2 — Accounting Core Capability Model |
| Method | Derived from business responsibility (B01 register), not from reference-system module boundaries |
| **Corrected (Round 2)** | **CORR-B2-03/04 (2026-08-29)** — ChatGPT's Round 2 re-audit (`04e44b06489d8bea6c8d39410050d68cf08bce21`, finding `M-AUD-05`) found CAP-09 generalized Team A's year-end-specific evidence to every ordinary Period close, risking double-counted balances. CAP-09 renamed and rescoped below to Fiscal Year Close only. See [CORR_B2_CORRECTIVE_ROUND.md](CORR_B2_CORRECTIVE_ROUND.md). |
| **Corrected (Round 3)** | **CORR-B3-05 (2026-08-29)** — ChatGPT's Round 3 re-audit (`f6fb633fd141f45caf047bc94d75f84420e1cc6d`, finding `M-AUD-07`) found the Round-2 text below still described CAP-09 as posting "exactly one Current-Earnings-transfer Entry" — directly contradicting the domain's own repeated claim that Revenue/Expense are never reset by a posted action, and, traced literally, a real arithmetic bug (such an Entry would corrupt the closing year's own historical query). Corrected: CAP-09 now posts **no financial Entry at all**; Current Earnings becomes part of Reported Retained Earnings through [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e's derived reporting formula. See [CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md](CORR_B3_ACCOUNTING_STANDARD_CORRECTIVE_ROUND.md). |
| **Corrected (Round 4)** | **CORR-B4-03 (2026-08-30)** — ChatGPT's Round 4 re-audit (`9c0a3f2d179994a20f01db16d5713989a78c0b2a`, finding `M-AUD-09`) found the Round-3 text below still tied Reported Retained Earnings' inclusion of a Fiscal Year to CAP-09's own declaration — meaning a delayed declaration would silently drop a real, elapsed Fiscal Year's earnings from every report. Corrected: CAP-09's declaration now governs **posting-lock scope only**; Reported Retained Earnings inclusion is boundary-driven ("Elapsed," [B07](B07_CONCEPTUAL_INFORMATION_MODEL.md) §1e), never declaration-driven. See [CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md](CORR_B4_REPORTING_EQUITY_CORRECTIVE_ROUND.md). |
| **Corrected (Round 5)** | **CORR-B5-05 (2026-08-30)** — ChatGPT's Round 5 re-audit (`de7492afd0af0f58185f3f36940a77f2389aa8b8`, finding `M-AUD-12`) found no capability governed changing a Fiscal Year's own boundary after it had already governed real facts. CAP-09 extended to own this action, gated at Restatement's tier, via the new `FiscalYearBoundaryChanged` event. See [CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md](CORR_B5_TRIAL_BALANCE_FISCAL_CALENDAR_CORRECTIVE_ROUND.md). |
| **Corrected (Round 6)** | **CORR-B6-02 (2026-08-30)** — ChatGPT's Round 6 re-audit (`b0ce666dad72909411a49690d0f642313d94dd13`, finding `M-AUD-14`) found the Round-5 `FiscalYearBoundaryChanged` action left a gap for what happens to Entry membership when it reaches into reliance. CAP-09's boundary-governance bullet corrected below: `FiscalYearBoundaryChanged` is now scoped to never reach backward over reliance; CAP-09 additionally owns the new, atomic `FiscalYearMembershipRestated` action for genuine post-reliance correction. See [CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md](CORR_B6_FISCAL_CALENDAR_VIEWPOINT_MEMBERSHIP_CORRECTIVE_ROUND.md). |

## 1. Framing

A capability is identified here by asking: *what must be true of the business's financial
record for the enterprise to be solvent, compliant, and auditable* — not by asking what a
reference system happens to bundle into one installable unit. Nine capabilities were
identified. Each is stated independently of how (or whether) a reference system implements it.

## 2. Capability Register

### CAP-01 — Chart of Accounts Governance

- **What exists:** the classification structure (a fixed set of accounting categories, per
  BR-08/BF-10) that every financial fact must land in, and the rules for creating, retiring,
  and reclassifying accounts within it.
- **Why it exists:** without a stable classification, "total debits = total credits" is
  arithmetically satisfiable but commercially meaningless — the ledger must also be
  *organized* correctly to produce a balance sheet and income statement.
- **Owner:** Accounting Core. Not owned by any originating business domain (Sales, Purchasing,
  etc.) — they reference accounts, they do not define them.
  Legal Entity Owner is the entity's Accounting Core instance (see [B03](B03_DOMAIN_BOUNDARY_MODEL.md)).
- **Financial truth maintained:** every account has exactly one category, and that category
  governs statement placement and year-end behavior; a deprecated account cannot silently
  keep accepting activity through a use it wasn't guarded against (BR-13's partial-guard
  weakness in the reference system is the negative example this capability must not repeat).
- **Inputs:** account creation/edit requests; deprecation requests.
- **Outputs:** a queryable, versioned chart of accounts; a category-membership answer for
  every account, for every point in time.
- **Downstream dependents:** CAP-02 (every line needs a valid account), CAP-06 (statement
  placement), all reporting/consolidation capabilities outside this domain.

### CAP-02 — Financial Fact Capture & Commitment

- **What exists:** the single choke point through which any proposed financial fact — however
  it originated — becomes part of the authoritative ledger.
- **Why it exists:** this is the capability the entire domain organizes around: it is where
  IV-01 (Σdebit=Σcredit) either holds or the fact does not become authoritative. Per ADV-01,
  this guarantee must be non-optional at the point data becomes durable, not a courtesy
  application check.
- **Owner:** Accounting Core exclusively. No other domain may write directly to the ledger;
  they may only submit proposed facts to this capability.
- **Financial truth maintained:** every fact that is queryable as "committed" is balanced,
  attributed to exactly one company and one account per line, and dated within a period this
  capability has independently confirmed is open (via CAP-04).
  self-check against the closed-period case is deliberate: commitment must consult CAP-04, not
  assume the caller already did.
- **Inputs:** a proposed fact (a set of lines, each with account, amount, currency, date,
  company) from any originating capability, including manual entry.
- **Outputs:** a committed financial fact with a permanent identity; a rejection with reason,
  if the fact fails balance, account-validity, or period-validity checks.
- **Downstream dependents:** every capability in §2 that reads "the ledger"; every domain
  outside Accounting Core that reports on, reconciles against, or audits financial history.

### CAP-03 — Correction & Reversal

- **What exists:** the sole mechanism for changing what a *consumed* committed fact says,
  without destroying what it originally said.
- **Why it exists:** IV-05/IV-06/BR-06/BR-07 and ADV-04 (this domain's highest-priority
  advancement objective) all converge on one requirement: correction must be additive. This
  capability exists specifically so "the entry was wrong" never has to mean "the history is
  gone."
- **Owner:** Accounting Core. A correction is itself a financial fact and must pass through
  CAP-02 like any other.
- **Financial truth maintained:** for any committed fact that has been consumed downstream
  (LC-03 — reported, reconciled, filed, or otherwise relied upon outside this entity's own
  books), the only available correction path produces a new, linked fact; the original is
  never mutated. Below the consumption threshold, in-place correction may be legitimate (see
  [B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md) §3) but is a distinct, narrower operation this
  capability must still gate and record, not a silent bypass of the rule.
- **Inputs:** a correction or reversal request referencing an already-committed fact.
- **Outputs:** a new committed fact linked to the one it corrects; the original, unchanged and
  still queryable.
- **Downstream dependents:** CAP-08 (Audit Trail), any downstream domain that already consumed
  the original fact and needs to know it was corrected rather than silently changed underneath
  it.

### CAP-04 — Period Control

- **What exists:** the single authoritative answer to "is this date, for this transaction
  class, open for posting right now" — and the mechanism for closing that answer off.
- **Why it exists:** IV-02/BR-05, and the CF-03 finding that a *fragmented* answer (multiple
  independent controls that can disagree) is a real, demonstrated risk, not a hypothetical one.
  ADV-03 specifically targets reducing the number of controls one must inspect to get this
  single answer.
- **Owner:** Accounting Core, scoped per company (CAP-05).
- **Financial truth maintained:** for any given transaction date, class, and company, there is
  exactly one authoritative open/closed answer, and CAP-02 consults it — the answer is never
  something an originating domain is trusted to have already checked.
- **Inputs:** period-close requests; override/exception requests (which must themselves be
  authorized and recorded, not a silent code-level bypass — see [B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md)).
- **Outputs:** an open/closed determination, consultable by CAP-02 for every commitment
  attempt; a closed-period record that CAP-06 relies on for carry-forward.
- **Downstream dependents:** CAP-02 (gates every commitment), CAP-06 (defines when carry-
  forward is triggered), external financial reporting (defines what's frozen).

### CAP-05 — Company / Entity Boundary Enforcement

- **What exists:** the guarantee that a financial fact belongs to exactly one legal entity and
  cannot leak into or reference another's books.
- **Why it exists:** IV-03 — legal-entity separation is a business/regulatory requirement, not
  an implementation convenience; each entity must be independently reportable and auditable.
- **Owner:** Accounting Core, as a cross-cutting constraint enforced at CAP-02.
- **Financial truth maintained:** no committed fact's lines span more than one company; no
  account, journal, or period-control answer is shared across companies without an explicit,
  separately-designed consolidation capability (out of scope for this domain — see
  [B03](B03_DOMAIN_BOUNDARY_MODEL.md) §4).
- **Inputs:** company context on every proposed fact.
- **Outputs:** an accept/reject boundary check consumed by CAP-02.
- **Downstream dependents:** every other capability in this register is implicitly scoped by
  this one.

### CAP-06 — Currency Recognition & Remeasurement

- **What exists:** the capability that keeps a foreign-currency-denominated fact's functional-
  currency value honest, both at initial recognition and over time.
- **Why it exists:** RG-05/BF-05 (IAS 21) — recognition alone is not compliance; remeasurement
  at each reporting date is a distinct, ongoing obligation. OQ-02/ADV-08 record that whether a
  reference implementation actually does this is genuinely unknown — this capability is
  designed on the principle's requirement, not on an assumption that some existing system
  already satisfies it.
- **Owner:** Accounting Core.
- **Financial truth maintained:** every foreign-currency fact is recognised at a valid rate on
  its date (IV-04a: sign-consistency between the two currency views is a **minimum**, not a
  substitute, check); functional-currency balances are remeasured at each reporting date, and
  the remeasurement itself is a financial fact traceable through CAP-02/CAP-08.
- **Inputs:** a proposed fact carrying a non-functional currency amount and rate; a
  reporting-date remeasurement trigger.
- **Outputs:** functional-currency committed amounts; remeasurement adjustment facts.
- **Downstream dependents:** CAP-02 (every foreign-currency commitment routes through this),
  financial reporting outside this domain.

### CAP-07 — Regulated Document Integrity

- **What exists:** the narrow, statute-scoped guarantee of content integrity, origin
  authenticity, and/or sequential numbering for the specific document classes Thai law
  actually names — not a general claim extended to the whole ledger.
- **Why it exists:** RG-03/RG-04 (BF-06/BF-07) are real, officially-sourced obligations for
  e-Tax invoices/receipts and tax invoices specifically. GR-11/GR-12 record that the reference
  system implements the mechanism as an admin-configurable opt-in — AO-02 states the
  independent objective (default coverage, not opt-in memory) without assuming a stronger
  legal scope than is evidenced.
- **Owner:** Accounting Core, in coordination with whatever domain issues the regulated
  document (this domain owns the integrity/numbering guarantee once a fact is committed under
  a regulated document type; it does not own tax computation).
- **Financial truth maintained:** every fact tagged as belonging to a regulated document class
  automatically carries the integrity/numbering guarantee that class requires — coverage is a
  property of the class, not a remembered setting. This capability does **not** claim
  general-ledger-wide tamper evidence or universal gapless numbering (OQ-01) — doing so would
  be exactly the overclaim [B01](B01_AUTHORIZED_INPUT_REGISTER.md) §12 forbids.
- **Inputs:** a proposed fact tagged with a regulated document class.
- **Outputs:** an integrity-sealed, sequentially-numbered committed fact for that class.
- **Downstream dependents:** statutory filing/compliance capabilities outside this domain;
  CAP-08 for the evidentiary record.

### CAP-08 — Audit Trail & Evidence Provision

- **What exists:** the append-only record of every state-changing action taken against the
  ledger — who, what, when, before/after — independent of and orthogonal to whether the
  underlying fact itself is mutable.
- **Why it exists:** AU-03/PR-07/INV-06. LC-04 makes the key distinction this capability is
  built on: the *event log* being forced and append-only is a separate guarantee from whatever
  mutability rule governs the *record*. The reference system's version of this is optional
  (chatter/tracking); this capability treats it as non-negotiable.
- **Owner:** Accounting Core.
- **Financial truth maintained:** for any committed fact, its complete history of
  commitment/correction/void events is independently reconstructable without relying on the
  mutable record having preserved it.
- **Inputs:** every state-changing action from CAP-02, CAP-03, CAP-04.
- **Outputs:** an immutable event stream, queryable per fact, per period, per actor.
- **Downstream dependents:** internal/external audit, [B09](B09_CONTROL_AUDIT_DESIGN_OBJECTIVES.md)
  control objectives, dispute resolution.

### CAP-09 — Fiscal Year Close & Earnings Transfer *(renamed and rescoped at CORR-B2-03/04, was "Period-End Carry-Forward"; "Earnings Transfer" re-scoped again at CORR-B3-05 to mean a logical/reporting transfer, never a posted Entry)*

- **What exists (corrected at CORR-B2-03/04):** the ChatGPT Round 2 audit (`M-AUD-05`) found the
  original version of this capability generalized Team A's year-end-specific evidence (BF-09) to
  *every* ordinary Period close, and — because B08 MP-09 sums all-time — risked
  double-counting balance-sheet activity against a posted "opening balance" fact. Corrected:
  this capability now does exactly one thing, at Fiscal Year Close only — ~~transfer Current
  Earnings (Revenue − Expenses for the closing Fiscal Year, MP-02/MP-11) into a designated
  formal Equity account, via one ordinary, balanced Entry.~~ Balance-sheet carry-forward across
  *ordinary* Period boundaries is **implicit** (B07 §1d) — this capability has nothing to do
  with it, and posts nothing at ordinary Period close.
- **What exists (corrected again at CORR-B3-05):** the struck-through clause above is exactly
  the defect the Round 3 audit (`M-AUD-07`) found — it described a posted, balanced Entry
  debiting Revenue and crediting Expense, which contradicts this same capability's own claim
  (previous bullet) that Revenue/Expense are never reset by a posted action, and which, traced
  literally, would corrupt the closing Fiscal Year's own historical query (an Entry dated
  inside the year it closes would zero out that year's own Revenue/Expense when read
  as-of any date within it). Corrected: CAP-09 posts **no financial Entry**. It performs
  exactly one thing at Fiscal Year Close — an authorized declaration/lock action (the
  `FiscalYearClosed` Audit Event, [B04](B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md)) that
  ~~(a) extends Period Lock to the whole Fiscal Year and (b) marks that year's Current
  Earnings as closed, so it becomes eligible for inclusion in Reported Retained Earnings.~~
  The "transfer" is a **reporting-time derivation** ([B07](B07_CONCEPTUAL_INFORMATION_MODEL.md)
  §1e's formula sums every closed Fiscal Year's Current Earnings, computed via MP-09 Mode 2),
  not a bookkeeping action this capability performs.
- **What exists (corrected again at CORR-B4-03):** the struck-through clause immediately above
  is exactly the defect ChatGPT's Round 4 audit (`M-AUD-09`) found — it tied Reported Retained
  Earnings' *inclusion* of a Fiscal Year's Current Earnings to this capability's own
  declaration, meaning a delayed declaration would make a real, elapsed Fiscal Year's earnings
  silently vanish from every report until someone got around to declaring it closed. **CAP-09
  now does only (a) — it extends Period Lock (posting/amendment eligibility) to the whole
  Fiscal Year.** It does **not** gate Reported Retained Earnings inclusion at all: B07 §1e's
  formula sums every Fiscal Year that has **elapsed** (its own calendar End Date has passed),
  independent of whether `FiscalYearClosed` has been declared for it — the same "orthogonal
  gates" pattern this capability model has used since CORR-B01 separated Period Lock from
  Consumption. A Fiscal Year is routinely elapsed-but-not-yet-closed for a real operational
  window (reconciliation, review); reports remain correct throughout that window, and CAP-09's
  eventual declaration changes only whether the year can still accept new ordinary postings.
- **Why it exists:** the one thing an ordinary Period-Control lock (CAP-04) cannot itself
  represent is the genuine economic event of a fiscal year's result becoming part of
  permanent, reportable capital — that is a real change of status (a year moving from "open"
  to "closed, counted in Retained Earnings"), not a bookkeeping reset or a posted transaction,
  and needs its own capability, scoped precisely to when it actually happens (year-end), not
  generalized to every posting-lock event.
- **Owner:** Accounting Core.
- **Financial truth maintained:** ~~immediately after Fiscal Year Close~~ **from the moment a
  Fiscal Year elapses (corrected at CORR-B4-03 — not from whenever CAP-09 happens to be
  exercised)**, Reported Retained Earnings (B07 §1e, a derived reporting figure — not a ledger
  balance) includes the elapsed year's full Current Earnings, Revenue/Expense correctly read
  zero for the new Fiscal Year (a consequence of MP-09's category-bounded aggregation, not a
  separate reset action), Reported Equity never double-counts the designated Retained Earnings
  account against Other Ledger Equity (B07 §1f, `M-AUD-08`), and no Balance Sheet amount is
  duplicated (B07 §1d/§1e/§1f; verified numerically,
  [B19](B19_CORR_B2_FOCUSED_RED_TEAM_REGRESSION.md) Test 9,
  [B20](B20_CORR_B3_ACCOUNTING_STANDARD_REGRESSION.md) Tests 9-11, and
  [B21](B21_CORR_B4_REPORTING_EQUITY_REGRESSION.md) Tests 1-7).
- **Inputs:** an authorized Fiscal Year Close action (a higher authorization tier than
  ordinary Period reopen, given its blast radius — CO-08 tiering extended).
- **Outputs (corrected at CORR-B3-05, boundary role corrected at CORR-B4-03):** ~~exactly one
  Current-Earnings-transfer Entry, itself a normal CAP-02-committed fact (MP-11).~~ No Entry.
  One `FiscalYearClosed` Audit Event (CAP-08), which is what CAP-02, CAP-04's reopen check, and
  CO-08's authorization tiering consult to determine which Fiscal Years are still open for
  **posting/amendment**. ~~Which Fiscal Years are closed for MP-09 Mode-2/B07 §1e purposes~~ —
  **no longer this event's concern (CORR-B4-03): reporting queries never consult
  `FiscalYearClosed` at all; they consult only each Fiscal Year's own End Date (B07 §1e's
  Elapsed test).**
- **Downstream dependents (corrected at CORR-B3-05, further corrected at CORR-B4-03):** ~~CAP-02
  (the transfer Entry is itself committed through it)~~ CAP-08 (the `FiscalYearClosed` event is
  recorded through it, not CAP-02 — there is no financial fact for CAP-02 to commit), ~~financial
  reporting (a Fiscal Year Close is what makes the closing year's Current Earnings eligible for
  Reported Retained Earnings, B07 §1e, and what makes the simple accounting equation, MP-02,
  read using an updated Equity figure going forward)~~. **Financial reporting is corrected to
  NOT be a downstream dependent of CAP-09's declaration at all (`M-AUD-09`) — Reported Retained
  Earnings updates automatically at each Fiscal Year's own boundary (B07 §1e), whether or not
  CAP-09 has yet been exercised for that year. CAP-09's only true downstream dependent is CAP-04
  (ordinary posting/amendment eligibility within the now-locked Fiscal Year).**
- **Fiscal Year boundary governance (new, added at CORR-B5-05; scope corrected at CORR-B6-02):**
  CAP-09, as the owning capability for the Fiscal Year entity (B07 §1), is also where a
  boundary change is authorized and recorded. ~~a post-reliance boundary change (B07 §1h,
  `M-AUD-12`) is authorized and recorded — a new `FiscalYearBoundaryChanged` Audit Event (B04,
  new), at an authorization tier at least as strict as Restatement (CO-15, reused).~~
  **CORRECTED AT CORR-B6-02 (kept struck through above, not deleted — this is exactly what
  ChatGPT's Round 6 audit, `M-AUD-14`, found under-specified):** `FiscalYearBoundaryChanged`
  (B04) is now scoped to a Fiscal Year with **no existing reliance** only (pre-reliance
  correction, or a genuinely future, not-yet-begun Fiscal Year) — it can never reach backward
  over a date reliance already covers. Genuinely correcting an already-relied-upon Fiscal
  Year's own boundary is a **different** action, `FiscalYearMembershipRestated` (B04, new,
  B07 §1j) — which CAP-09 also owns — atomically changing the Current-viewpoint boundary AND
  reclassifying every affected Entry's Current-viewpoint membership in one step, at the same
  CO-15-tier-or-stricter authorization. Both actions are distinct from ordinary Fiscal Year
  Close: they change the Fiscal Year's own *definition* or *membership*, not its lock status,
  and — unlike Fiscal Year Close — are expected to be rare, gated specifically to protect
  against the silent-history-rewrite risk `M-AUD-12` identified and the hybrid-state risk
  `M-AUD-14` identified. Pre-reliance corrections to a Fiscal Year's boundary (before any
  Entry, elapse, or issued report has depended on it) require neither event — they are
  ordinary CAP-01 chart-configuration updates.

## 3. Deliberately Not Vendor Module Boundaries

Three points where this model was checked against — and diverges from — the reference
system's actual module shape, to demonstrate independence rather than merely assert it:

1. The reference system stores journal entries, customer invoices, vendor bills, and credit
   notes in one overloaded table distinguished by a type field (ADV-05). This model does not
   define capability boundaries around document type at all — CAP-02 (Financial Fact Capture
   & Commitment) is defined around the *business event* (a proposed fact becoming
   authoritative), which is identical regardless of what business process produced the
   proposal. Document type is an attribute of the proposal, not a capability boundary.
2. The reference system implements period control as six independently-settable fields plus
   an exception object plus a code-level bypass (CF-03). This model defines CAP-04 as a single
   capability with one authoritative answer *by design requirement*, not because a reference
   implementation has one field for it — the requirement (ADV-03) is stated first, independent
   of whatever mechanism count a peer or the reference system happens to use.
3. The reference system does not appear to treat the audit/event log as a first-class,
   forced capability — it is optional tracking bolted onto individual models (CF-02 finding,
   LC-04 reasoning). CAP-08 is elevated here to a top-level capability specifically because the
   domain's central weakness (INV-06 / ADV-04) is a *consequence* of audit evidence being
   treated as elective rather than foundational — this is an independent structural decision,
   not an inherited one.

## 4. Capability Dependency Summary

```
CAP-01 (Chart of Accounts) ──┐
CAP-05 (Company Boundary) ───┼──▶ CAP-02 (Capture & Commitment) ──┬──▶ CAP-08 (Audit Trail)
CAP-04 (Period Control) ─────┘                                    │
CAP-06 (Currency) ───────────────────────────────────────────────┤
CAP-07 (Regulated Document Integrity) ────────────────────────────┤
                                                                    │
CAP-03 (Correction & Reversal) ───────────────────────────────────┤
                                                                    │
(Fiscal Year Close, authorized) ──▶ CAP-09 (Earnings Transfer) ────┘
```

*(Corrected at CORR-B2-03/04: CAP-09 no longer depends on ordinary CAP-04 Period-close
events — it depends on a distinct, authorized Fiscal Year Close action. Ordinary
carry-forward is implicit, B07 §1d, and produces no capability-triggering event at all.)*

*(Note added at CORR-B3-05: the diagram's placement of CAP-09 on the bus feeding CAP-08
directly — not through CAP-02 — was already correct and did not need to change. It is this
section's prose, not the diagram, that previously (incorrectly) described CAP-09 as producing
a fact for CAP-02 to commit; the prose above is now corrected to match what the diagram always
showed.)*

Every arrow into CAP-02 represents a capability CAP-02 must consult before a fact becomes
authoritative — this is the structural expression of ADV-01: the guarantee is non-optional
because nothing downstream of CAP-02 is trusted to have already checked it.

**B2 = COMPLETE.**
