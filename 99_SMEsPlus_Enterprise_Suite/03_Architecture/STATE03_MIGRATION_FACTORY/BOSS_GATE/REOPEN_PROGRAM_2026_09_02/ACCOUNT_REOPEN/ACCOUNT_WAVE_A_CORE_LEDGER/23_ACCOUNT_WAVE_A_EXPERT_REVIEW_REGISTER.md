# 23 — ACCOUNT_WAVE_A_EXPERT_REVIEW_REGISTER (AAS-03)

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Four independent expert reviews were commissioned under AAS-03. Each reviewer worked from the
evidence base and **independently verified primary source**; each was required to produce
`OBSERVATION` / `EVIDENCE` / `CONTRADICTION` / `UNKNOWN` / `RECOMMENDATION` for every finding, and to
disagree where warranted. **Agreement was not required. Disagreement is preserved.**

| Review | File | Findings | Verified independently |
|---|---|---|---|
| Expert 1 — Leader Functional Design | `EXPERT_REVIEW/X1_EXPERT1_FUNCTIONAL_DESIGN_REVIEW.md` | 10 | yes |
| Expert 2 — Leadership Database Design | `EXPERT_REVIEW/X2_EXPERT2_DATABASE_DESIGN_REVIEW.md` | 9 | yes |
| Expert 3 — Lead Integration & Localization | `EXPERT_REVIEW/X3_EXPERT3_INTEGRATION_LOCALIZATION_REVIEW.md` | 13 | yes |
| Expert 4 — Lead Code & UI Architect | `EXPERT_REVIEW/X4_EXPERT4_CODE_UI_ARCHITECT_REVIEW.md` | 14 | yes |
| **Total** | | **46** | |

## 1. Findings that changed the research position

**Twenty corrections were accepted and re-verified by the research team** before entering the
package. They are recorded in full in `LAYER2_EVIDENCE_QUARANTINE/E01`. Summary of who found what:

| Correction | Raised by | Effect |
|---|---|---|
| `COR-01` fiscal-year entity exists | Expert 1 | contradicted a research negative; conclusion strengthened |
| `COR-02` accounting date moved by three mechanisms, one needing no lock | Expert 1, Expert 3, Expert 4, challenge unit — **independently, all four** | contradicted the mechanism; **made the finding more serious** |
| `COR-03` deprecated accounts are blocked from posting | Expert 1 | resolved a research unknown |
| `COR-04` lock exceptions are revocable by the granting role | Expert 1 | contradicted "append-only" |
| `COR-05` a code constraint is not expressible against the chosen storage | Expert 2 | extended; changed the remedy |
| `COR-06` the hash guard fails open on the canonical amount field | Expert 2 | split `CONTRA-01` in two |
| `COR-07` the entry balance invariant is suppressible with no storage constraint | Expert 2, Expert 4 | **new, and the most severe control finding** |
| `COR-08` merge deletes by direct statement past the ORM's guards, unlogged | Expert 1, Expert 2 | escalated from trade-off to control bypass |
| `COR-09` reconciliation amounts are unbounded in any currency configuration | Expert 2 | widened the framing |
| `COR-10` rate types exist, derived at query time | Challenge unit | contradicted a research negative |
| `COR-11` hash rounds at the wrong currency's precision | Challenge unit | new collision vector |
| `COR-12` hash chain keyed on storage row identifiers | Challenge unit | new; fatal for migration assurance |
| `COR-13` Thai localization source present and unexamined | Challenge unit | evidence-availability correction |
| `COR-14` missing rate converts at 1:1, silently | Expert 3 | **new, and the most dangerous behaviour found** |
| `COR-15` posted freeze bypassed at seven production sites | Expert 4 | escalated from escape hatch to routine |
| `COR-16` numbering control parameter has no company dimension | Expert 4 | contradicted in both directions |
| `COR-17` tax lock rejects rather than relocates | Expert 3 | produced a third, undocumented outcome |
| `COR-18` the identifier ceiling triggers far sooner than stated | Expert 4 | raised likelihood |
| `COR-19` both immutability switches are one-way ratchets | Expert 4 | improved the risk profile; sharpened the requirement |
| `COR-20` Thai statutory extracts driven by the system-derived date | Expert 3 | connected `COR-02` to statutory consequence |

## 2. Preserved disagreements

Recorded because agreement was not required and these remain unresolved.

| # | Disagreement | Positions | Status |
|---|---|---|---|
| `DIS-01` | Severity of the hash guard failing open on the canonical amount field | **Expert 2**: the hash is unsound even single-currency. **Research team**: the guard fails open but the **detector still catches it**; the true integrity hole is confined to the transaction-currency magnitude, currency, tax, analytic and due date. | **Research team position adopted**, and Expert 2's stronger claim is recorded verbatim in `COR-06` alongside the correction. Both are preserved. |
| `DIS-02` | Whether `EV-009` was wrong or merely mis-cited | **Challenge unit**: `VETO` — the mechanism is wrong. **Experts 1 and 3**: understated, not wrong. | **Both accepted.** The citation was wrong; the conclusion was too weak. See file 24. |
| `DIS-03` | Which field is "the truly unguarded one" | **Challenge unit**: the analytic distribution. **Research team**: the transaction-currency magnitude, because it carries monetary value directly. | Both recorded; neither is dismissed. Both are inside `CONTRA-01b`. |
| `DIS-04` | Whether the immutability switches are a runtime risk | **Expert 4**: no — they are one-way ratchets, so the risk is fixed at provisioning and first posting. **Original evidence base**: implied a runtime toggle. | **Expert 4's position adopted** (`COR-19`); it improves the risk profile and sharpens the requirement. |
| `DIS-05` | Whether the subledger-to-control equation is a strength or a blind spot | **Research team**: structurally impossible to break, therefore a strength — but the check yields no assurance. | Recorded as `P-04`; no expert contested it. Flagged for Wave G. |

## 3. Coverage by expert lens

| Lens | Distinctive contribution |
|---|---|
| Functional design | established that the destructive paths are the *convenient* ones, and that "Cancel" silently routes through the destructive reset |
| Database design | established that only three of fourteen invariants are storage-owned, all per-row, and that the defining cross-record invariant is not among them |
| Integration & localization | established the chain from the system-derived accounting date to the Thai statutory extracts, and found the silent 1:1 rate fallback |
| Code & UI architecture | established that the declared three-state machine is not the real state space, and that control suppression is a systemic pattern with production call sites |

## 4. Assessment of the review process

Constitution principle 7 — independent reviewers must not review their own work — **materially
changed the outcome of this session.** Six research-team claims were contradicted, four of them
negatives asserted at a wider scope than was actually searched. Four of the five most severe findings
in the final package (`COR-07`, `COR-14`, `COR-11`, `COR-08`) came from reviewers, not from the
research team.

`RECOMMENDATION:` the gate should weigh the two classes of finding differently. This package's
**positive** findings were independently re-verified and held. Its **negative** findings — claims
that something does not exist — proved to be the weak class, and three of them were wrong. Any
negative in this package should be re-scoped before it is relied upon.
