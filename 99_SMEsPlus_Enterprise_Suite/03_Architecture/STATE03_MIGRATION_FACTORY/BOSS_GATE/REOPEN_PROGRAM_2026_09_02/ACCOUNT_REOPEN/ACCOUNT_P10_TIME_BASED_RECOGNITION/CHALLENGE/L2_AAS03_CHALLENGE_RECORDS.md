# LAYER 2 — AAS-03 INDEPENDENT CHALLENGE RECORDS (AUDIT QUARANTINE)

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001`
Classification: **LAYER 2 — Boss / PMO / AI-Audit only.** Contains reference-ERP paths, method names and line numbers.

Four challenges were commissioned with **disjoint assignments**, all adversarial, each carrying the instruction *"if any path in this brief is wrong, report it as a finding."* All four ran against declared reference root `RR-1` with no access to each other's work and no access to the primary author's drafts.

---

## Challenge 1 — Mandatory Duplicate-Recognition Attack

Assignment: construct sequences producing double or lost recognition across all mechanisms.

**Confirmed duplicate paths**
| ID | Finding | Location |
|----|---------|----------|
| `D-1` | Loan confirmation is re-entrant: no state guard and no check for existing generated entries; a fully-historical schedule leaves the state unchanged so the action stays available. Second invocation produces a complete second set of entries. | `account_loans/models/account_loan.py:175-300`, state at `:299-300`; UI guard only in `account_loan_views.xml` |
| `D-2` | The accrual wizard has no idempotency of any kind. Amounts are computed from a shadow copy and the real order is invalidated afterwards, so a second run reproduces identical figures. | `account/wizard/accrued_orders.py:245-258`, `:151`, `:213` |
| `D-3` | The accrual reversal date is user-editable with only a "later than the accrual" check, so accrual and real invoice can coexist for an arbitrary interval with no link between them. | `accrued_orders.py:34-39, 64-69, 248` |
| `D-4` | A deferral entry left in draft with a past date fails both branches of the already-generated key, re-opening the grouped path for a period that already has an entry. | `account_deferred_reports.py:48-60, 80-102`; `account/models/account_move.py:5451` |
| `D-5` | The fetched line set is cached under the bare literal key `report_deferred_lines`, not parameterised by report, direction, period or draft/posted selection, for the life of the cursor. A display pass can therefore seed the cache that a subsequent generation consumes — including across the expense and revenue handlers. | `account_deferred_reports.py:107-117, 140-142`; cursor cache lifetime in the ORM's connection layer |
| `D-6` | Of four loan teardown paths, three reverse the generated entries first; `action_reset` deletes the schedule lines only, orphaning posted entries whose back-link is then nulled. | `account_loan.py:373-375` vs `:391-397`, `:421-425` |
| `D-7` | The skip-until rule uses a strict comparison while its own help text says the boundary date is included, so the boundary period is generated. | `account_loan.py:54-57` vs `:202` |

**Confirmed lost-recognition paths**
| ID | Finding | Location |
|----|---------|----------|
| `L-1` | The recurring-entry copy helper enumerates the fields to re-carry and does not include the deferral window; no module overrides it. A recurring deferred cost silently stops deferring. | `account/models/account_move.py:4035-4063`; `account_accountant/models/account_move.py:439-451, 477-483` |
| `L-2` | An entry that fails to post once during the automatic run is flagged unchecked, and the same routine's filter then excludes unchecked entries permanently. | `account/models/account_move.py:5436, 5451` |
| `L-3` | A posted depreciation entry can be reset to draft — the guard covers the source invoice's assets, not a depreciation entry's own asset — after which the residual is restored and the amount re-spread. | `account_asset/models/account_move.py:184-190`; `account_asset.py:319-328, 636-648` |

**Controls that stopped the attack** (strongest evidence class): month-end guard on grouped generation; lock-date guard on grouped generation; the cumulative self-correcting grouped model; the grouped-deferral reset refusal; reset-to-draft teardown; the account-change lock; posted depreciation entries never rewritten; asset creation guarded against re-post; asset write respecting the fiscal lock; three of four loan teardown paths reversing correctly.

**Declared not searched (class `C`)**: asset pause / resume / revaluation / disposal; client-side code; multi-company and multi-currency duplication.

---

## Challenge 2 — Scope Boundary and Multi-Currency

Assignment: verify or refute six specific claims about scope resolution and currency capability.

| Claim | Verdict | Settling location |
|-------|---------|-------------------|
| `C1` allocation method read from the active company while journal and account come from the document's company; no caller supplies the document's company context | **CONFIRMED** | `account_accountant/models/account_move.py:230` vs `:268-269`; `with_company` occurrences in `account/models/account_move.py` enumerated and each inspected — none on the posting path; cron identity from the scheduler user |
| `C2` grouped generation can build one entry in the active company from another company's lines | **CONFIRMED, conditional** | `deferred_reports.xml:10, 29` multi-company selector; `account_report.py:1280-1281, 2069, 6401-6405`; `account_deferred_reports.py:493, 498, 502, 597, 623, 637`; company back-filled at `account/models/account_move.py:831-834`; compatibility decided by `account_account.py:25` |
| `C3` deferral line values carry no currency; the rate is frozen at the source document's rate | **CONFIRMED** | `account_accountant/models/account_move.py:604-616`; `account_move_line.py:492-499, 660-672, 686-691`; report SELECT list carries no currency column |
| `D4` accrual carries currency only for a single order, and its counterpart line is defective | **CONFIRMED, broader than briefed** | `accrued_orders.py:122-126` vs `:231` |
| `E5` which mechanisms can express a foreign-currency recognition | **Three of four cannot** | asset and loan currencies are tied to the company's; deferral omits the field; only the accrual's per-order legs can |
| `F6` scope table and executing-versus-owning divergences | **Four flags raised** | grouped generator is a scopeless object performing a company-scoped act; no guard on mutating a deferral window after generation; no guard on loan schedule amounts after confirmation; the source-to-deferral links carry no company check and are written by raw SQL |

**New finding not in the brief — `N-1`, the most consequential single defect in the package.** The grouped generation passes a boolean where a direction name is expected, so the comparison against the direction can never succeed and the **revenue** allocation method is applied on both reports. The display path passes the correct value. Locations: `account_deferred_reports.py:494 → :552 → :561`; `account_accountant/models/account_move.py:198, 230`; correct display call at `account_deferred_reports.py:428`.

Further findings: the `account_accountant` copy of `_get_deferred_lines` (`:243`) has no caller anywhere; the foreign amount is never balance-checked; zero multi-company and zero foreign-currency deferral tests exist upstream.

---

## Challenge 3 — Period Close, Backdate, Reopen, Modification, Reversal

| Question | Verdict |
|----------|---------|
| `Q1` lock-date enumeration and behaviour | Five lock-date fields exist; recognition entries post to general journals and carry no tax, so only the fiscal-year lock and the hard lock bind them. Only four before-generation checks exist in the whole surface. Inside the shared posting routine the entry's date is **silently overwritten**; the amount is not re-spread, and the deferral entry stores no period field, so the intended period is unrecoverable. No message, warning or explanatory record is produced. |
| `Q2` path asymmetry | **CONFIRMED.** Grouped path raises; validation path has no lock test at all. The accrual and loan paths also have none of their own. |
| `Q3` backdating | The accounting date anchors only the full-deferral leg; the schedule is derived purely from the window. Where the accounting date falls in a later month than the window start, a recognition entry is dated **before** the entry that created the deferred balance. |
| `Q4` modification | The deferral mechanism has no modification path at all — no wizard, no action, no partial operation. The only write guard covers the account, not the window, and once a teardown has left reversal entries behind, the account can never be corrected. |
| `Q5` catch-up | Asset: yes, by a stub entry cut at the modification date — **not** by the board recompute, which is prospective only. Deferral validation path: none. |
| `Q6` cancellation and reversal | The shared teardown's cancel branch is **unreachable**. Additionally, the date-change guard on a posted entry evaluates the record's current date rather than the incoming one, so it validates the source period and never the destination. |
| `Q7` reopen | No mechanism re-derives suppressed or re-dated recognition when a period is reopened. |

**Most severe scenario, as constructed by the challenge:** a twelve-month prepaid cost entered after a half-year close, with a hard lock at the half-year. All six locked-period recognition entries are silently re-dated to one month, which then reports seven months of cost while six report none. Every balance check, trial balance and reconciliation passes, because the total and the control-account clearance are both unchanged.

**Errors reported in the author's brief:** a company-model path that does not exist; the accrual reversal described as fixed when it is a user-editable default; the asset catch-up attributed to the wrong method; the lock question framed as a per-mechanism property when it is decided per entry.

---

## Challenge 4 — Adversary on the Kernel Question, and Negative-Claim Audit

Assignment: argue against the expected recommendation, then audit the negatives.

**Structural comparison** produced across ten axes; the deferral mechanism was shown to be **two** mechanisms with different residue policies, triggers, lock behaviour and aggregation semantics.

**Case for separate engines**: no common economic fact, so no common event identity; correction behaviours that are contradictory rather than variant; residue policy as an accounting assertion rather than a setting; day count as a legal input; period-close as a per-domain contract; balance-sheet-object semantics that only the asset has; and an auditability argument that a single identity model gives at least two domains a weaker trail than a purpose-built one.

**Counter-arguments the challenge raised against its own case**: the asset object in this root is described as *"Asset/Revenue Recognition"* and still carries deferred-revenue commentary — the two domains were one engine here; residue and day count are policy slots, not engine boundaries; all four mechanisms already share the identity *shape* of anchor-plus-period; the correction behaviours are three named strategies, not chaos; the Boss's warning forbids assuming sameness but does not license assuming difference; and the accrual's dead audit link is exactly the defect duplicated per-domain code produces.

**Population finding**: at least seven mechanisms, and the challenge's own pattern demonstrably missed an eighth. Two further mechanisms were identified that the primary author's enumeration had not found — a periodic transfer model with start date, stop date and frequency, and an automatic entry action that reallocates a posted amount across periods and **does** carry the foreign amount the deferral mechanism cannot.

**Negative-claim audit**: ten tempting negatives assessed. Two were **contradicted** and must not be written. Six **cannot be raised to class `A`** with the evidence available. The one most likely to be written as a headline — an exact mechanism count — was identified as the least supportable.

---

## Cross-Challenge Observations

1. Challenges 3 and 4 reached **opposite conclusions** on the deferral catch-up. Both were partly right; the resolution came from a cited line, not from reviewer count. Recorded as `P10-C-01`.
2. Every one of the four challenges found at least one error in the brief the primary author wrote for it. The standing instruction to report brief errors as findings produced four findings that would otherwise have been silent.
3. The single most consequential defect in the package (`Challenge 2 N-1`) sits on a line the author's own brief pointed at, for a different reason, and which the author had read twice without seeing it.
