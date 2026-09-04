# P10 — AAS-03 EXPERT CHALLENGE

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Four independent expert challenges were required and four were run, with disjoint, adversarial assignments. Raw records with citations are quarantined in `CHALLENGE/`; this document is the clean-room consolidation.

`Independent Review != Truth.` `Verified Evidence = Truth Basis.` Every challenge finding below states whether the primary author re-verified it.

---

## 1. Challenge Design

| # | Assignment | Adversarial posture |
|---|------------|---------------------|
| `AAS-03-1` | Mandatory duplicate-recognition attack across every mechanism | Construct failure, do not survey |
| `AAS-03-2` | Scope boundary and multi-currency behaviour | Disprove six named author claims |
| `AAS-03-3` | Period close, backdate, reopen, modification, cancellation, catch-up, reversal | Disprove, and construct the worst reachable scenario |
| `AAS-03-4` | Argue **against** the recommendation the author was expected to make; audit every negative claim | Full adversary |

All four were told to report any wrong path in their brief as a finding. All four did.

## 2. Findings Admitted

| ID | Finding | Origin | Author re-verified | Class |
|----|---------|--------|--------------------|-------|
| `P10-F-21` | Inside the grouped generation, the direction is passed as a boolean where a direction name is expected. The comparison can never succeed, so the **revenue** allocation rule is applied on both reports. The display path uses the correct rule. **One screen shows one number and posts another.** | `AAS-03-2` | **Yes**, line by line | VERIFIED FACT |
| `P10-F-22` | Of four loan teardown paths, three resolve the generated entries first; the fourth destroys the schedule and leaves posted entries orphaned with their back-link nulled. | `AAS-03-1` | **Yes** | VERIFIED FACT |
| `P10-F-23` | The loan skip rule uses a strict comparison while its own documentation says the boundary is included, so the boundary period is generated. | `AAS-03-1` | **Yes** | VERIFIED FACT |
| `P10-F-24` | The shared teardown's cancel outcome is unreachable: reaching it requires one expression to be both false and true. With the audit trail enabled, a previously-posted recognition entry is always reversed. | `AAS-03-3` | **Yes**, all three method bodies | VERIFIED FACT |
| `P10-F-25` | The report's fetched line set is cached under a bare literal key for the life of the database cursor, unparameterised by report, direction, period or draft/posted selection. | `AAS-03-1` | **Yes** | VERIFIED FACT |
| `P10-F-26` | An entry that fails to post once during the automatic run is flagged unchecked, and that routine's own filter then excludes unchecked entries permanently. | `AAS-03-1` | **Yes** | VERIFIED FACT |
| `P10-F-27` | A second copy of the deferred-line builder, living in the deferral module itself, has no caller anywhere in the reference root — dead code carrying capability nothing uses. | `AAS-03-2` | **Yes** | VERIFIED FACT |
| `P10-F-28` | The source-document ↔ deferral-entry links carry no company check, and the grouped path writes the relation with raw SQL that bypasses the ORM. | `AAS-03-2` | Partially — definitions and the raw write re-read | VERIFIED FACT / class `B` for overlays |
| `P10-F-29` | Two further time-based mechanisms exist that the author's enumeration missed, one of which reallocates a posted amount across periods and **does** carry the foreign amount the deferral mechanism cannot. | `AAS-03-4` | **Yes** | VERIFIED FACT |
| `P10-F-30` | The asset object in this reference root is described as covering **both** asset and revenue recognition and still carries deferred-revenue commentary in its board computation. | `AAS-03-4` | **Yes** | VERIFIED FACT |
| `P10-F-31` | The only protection against editing a schedule that has already generated entries is view-level and is present on one of the two views that expose the fields. | `AAS-03-2` | **Yes** | VERIFIED FACT |
| `P10-F-32` | Loan confirmation is re-entrant; a fully historical schedule leaves the state unchanged, keeping the action available. | `AAS-03-1` | Partially | class `B` |
| `P10-F-33` | The accrual mechanism has no idempotency control of any kind, and its amounts are recomputed from a discarded shadow position, so a repeat run reproduces identical figures. | `AAS-03-1` | Partially | class `B` |
| `P10-F-34` | The accrual's balancing counterpart line fails the single-order test whenever more than one order is selected, and with one foreign-currency order is stamped with the foreign currency and a zero foreign amount. The foreign amount is never balance-checked. | `AAS-03-2` | Partially | class `B` |
| `P10-F-35` | Zero multi-company and zero foreign-currency deferral tests exist upstream. | `AAS-03-2` | No — reviewer-supplied | class `B` within the reviewer's declared scope |
| `P10-F-36` | The date-change guard on a posted entry evaluates the record's current date rather than the incoming one, validating the source period and never the destination. | `AAS-03-3` | No — reviewer-supplied | class `B` |

## 3. The Worst Reachable Scenario, as Constructed by Challenge 3

A twelve-month prepaid cost is entered after the half-year is closed and hard-locked. The validation path performs no lock check, so twelve monthly recognition entries are created. The six that fall in the locked half are silently re-dated to a single open month.

Result: that month reports seven months of cost; six months report none. The total is unchanged, the control account still clears at the end of the window, and **every balance check, trial balance and reconciliation passes**. No exception, no warning, no message. Because the entries store no period, nothing afterwards can state which months the amount belonged to, and no mechanism re-derives them if the period is later reopened.

This is a period-allocation misstatement **produced by the system's own close control**, in the exact configuration a closing team would adopt. It is the single most severe item in the package and it drives `EC-04` in the gate report.

## 4. Where the Challenges Disagreed

Challenges 3 and 4 reached opposite conclusions on whether a deferral catch-up exists. The disagreement was resolved by reading the cited line, not by counting reviewers: both were right about different paths. Recorded and dispositioned as `P10-C-01`. See `14_P10_REVISION_LOG.md` `P10-R-02`.

## 5. Errors the Challenges Found in the Author's Own Briefs

Four, one per challenge: a path that does not exist; a reversal described as fixed when it is an editable default; a catch-up attributed to the wrong method; and a question framed as a per-mechanism property when it is decided per entry. All four were reported because every brief carried the instruction to report brief errors as findings.

**The instruction is doing real work and must remain in every future brief.**

## 6. What the Challenges Did Not Cover

Declared, not discovered — these are class `C`, unsearched, and must never be read as absences:
- asset pause, resume, revaluation and disposal duplicate exposure;
- localisation overlays;
- client-side behaviour;
- any runtime or database reproduction whatsoever.

## 7. Consequence for the Gate

One independent pass has completed. It produced **seven material corrections to the primary author's work, of which the author had found none**, and sixteen admitted new findings including the package's most severe. `EC-07` requires **two consecutive clean** passes. A pass with this profile is not clean, and the second pass has not been run. This is the principal reason the gate recommendation in `20_P10_FINAL_GATE_REPORT.md` is what it is.
