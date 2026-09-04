# C13 — ACCOUNT_WAVE_A_CORR1_FINAL_L12_REPORT

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · final adversarial contradiction sweep

## 1. What was run

| Round | Unit | Target | Outcome |
|---|---|---|---|
| Parent | 4 expert reviews (AAS-03) + 1 challenge unit | the original evidence base | 20 corrections; 6 claims contradicted |
| **CORR1** | **2 fresh independent reviewers**, neither involved in the parent round | **the corrected model**, incl. the two new forensics | **27 claims; 22 survived verification; 3 further over-scoped negatives found — all three authored by CORR1** |

Reviewer A took the FX and date forensics. Reviewer B took negatives, close, SaaS, migration and
balanced-but-wrong. Neither was asked whether corrections had been "edited correctly"; both were
directed to disprove the corrected model.

## 2. Vetoes

| Veto | Raised by | Disposition |
|---|---|---|
| `VETO-01` — `EV-009` cited a code path that does not govern posting | parent challenge unit | **Resolved by correction.** `C07` and `A2-03` restate the mechanism at supported scope. The behaviour is real; the citation and the reach were wrong |
| `VETO-02` — the package asserts a control-account negative in file 18 while file 02 states the function exists and file 21 leaves the gap open | fresh Reviewer B | **Accepted as an internal inconsistency; rejected as a substantive contradiction.** File 02 was correct. File 18 is corrected in `C12`. No substantive position changes |

**No veto invalidates the semantic model.** Both concern how a finding was stated, not whether it
holds.

## 3. Contradiction sweep — final state

| Contradiction | Final status |
|---|---|
| `CONTRA-01a` guard fails open on the canonical amount field | stands |
| `CONTRA-01b` integrity hole | **narrowed** — set is `amount_currency`, `currency_id`, `analytic_distribution`, reconciliation fields; tax and due date **are** field-tracked (`B-08`) |
| `CONTRA-02` identifier-arithmetic ceiling | stands; trigger corrected to identifier ≥ 10,000 |
| `CONTRA-03` identity vs merge | stands |
| `CONTRA-04` generated consequences mis-attributed | stands; third outcome added (`COR-17`) |
| `CONTRA-05` entry balance suppressible | **escalated** — externally reachable (`C09`) |
| `CONTRA-06` hash precision collision | stands |
| `CONTRA-07` hash keyed on storage identity | stands |
| `CONTRA-08` par FX conversion | **escalated twice** — trigger widened, detection removed |
| `CONTRA-09` unbounded reconciliation | stands |
| `CONTRA-10` matching destroyed by an entry-level operation | stands |
| `CONTRA-11` override grant and revoke unsegregated | stands |
| `CONTRA-12` accounting date system-derived | **narrowed population, unchanged consequence** |
| `CONTRA-13` posted freeze caller-owned | stands; seven production bypass sites |
| `CONTRA-14` deletion evidence leaves the tenant | **worsened** — the protection is a ratchet that by default locks **off** at first posting (`B-01`) |
| `CONTRA-15` no general event identity | **re-scoped** — typed origin links and one optional-module database key exist (`B-02`); no general mandatory carrier |

## 4. What the fresh round changed

**Nothing was withdrawn as a behaviour.** Every correction was one of:
- a **scope narrowing** (the behaviour affects a smaller population than claimed) — 5 cases;
- a **scope widening or severity increase** — 4 cases;
- a **negative contradicted** by evidence in an unsearched module — 3 cases, all authored by CORR1;
- an **internal inconsistency** in how the package stated a position — 2 cases.

## 5. The finding about the round itself

CORR1 issued a project-wide standard prohibiting over-scoped negatives, and then committed three of
them **in documents written after that standard**, in the same session.

This is recorded as a governance finding, not minimised:

- the defect is **not ignorance of the rule** — the rule was written by the same session;
- both times it has been caught in this programme, it was caught by **independent review**, never by
  the author;
- therefore `DR-NC-05` (independent review of high-impact negatives) is the **load-bearing** rule of
  the standard, and the standard should be applied as a **review checklist** before it is applied as
  an authoring guide.

`RECOMMENDATION:` no research package in this programme should reach a gate without an independent
negative-claim audit, and that audit should be a named, separately-tasked step rather than an
expectation placed on the authoring team.

## 6. Residual open items carried to the gate

| # | Item | Class | Priority |
|---|---|---|---|
| `FX-08` | Branch-level rates invisible to a root-scoped resolver | `PARTIALLY VERIFIED` | **highest** — cheap to close, severe if true |
| `SB-05` | Null-company rate re-measuring another tenant | `PARTIALLY VERIFIED` | **highest** — cross-tenant integrity |
| `FX-07` | Revaluation mechanism contaminated by the par fallback | `NOT PROVEN` | high |
| `B-05` | Approval engine exists and is skipped under privilege elevation | `NOT PROVEN` | high |
| `SB-06` | Reporting definitions carry no company dimension | `NOT YET SEARCHED` | medium |
| `RCH-01` | Executed confirmation of context-key reachability | `INFERENCE` pending test | medium — the source chain is fully read |
| `BW-15` | Two ingestion routes with disjoint dedup keys | `NOT PROVEN` | medium |
| `TX-01`–`TX-07` | All Thai statutory positions | `HOLD / EVIDENCE REQUIRED` | routed to `WAVE-D TAX` |

None of these changes a decision in the semantic-transfer register. Each would sharpen a severity or
close a scope.
