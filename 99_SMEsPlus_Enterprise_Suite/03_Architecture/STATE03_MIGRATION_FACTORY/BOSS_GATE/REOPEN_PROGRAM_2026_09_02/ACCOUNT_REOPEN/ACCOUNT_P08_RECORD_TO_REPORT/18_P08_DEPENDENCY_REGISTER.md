# P08_DEPENDENCY_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Dependencies are **recorded, not used to stop unrelated work**.

## 1. Governance dependencies

| ID | Dependency | Effect on P08 |
|---|---|---|
| `P08-DEP-01` | Account Wave A has no Boss Final Research Gate decision | P08 findings are additive audit lineage. P08 does not close Wave A and does not constitute Wave B commencement |
| `P08-DEP-02` | GB-08 freezes FX business semantics | P08 measures the gap and re-expresses the ruling under the corrected scope model. It does not re-decide it |
| `P08-DEP-03` | The mid-session scope correction applies to P01–P11 | P08 adopted it in flight; peers must adopt it for the scope assignments to reconcile |
| `P08-DEP-04` | `MCU-21` — which reference root SMEsPlus targets — is a programme declaration | P08 declared and proved the **root set** (22) and closed the prohibition for its own claims. Which root is *targeted* remains `P08-BD-05` |
| `P08-DEP-05` | Two governing standards (negative-claim control, method convergence) exist only on research branches and carry non-final status | P08 complies with both as if binding, and records that they are not on the canonical branch |

## 2. Peer dependencies — all `PEER DEPENDENCY OPEN`

At P08's close, no peer process had committed output. P08 recorded the interface and continued.

| ID | Peer | Element P08 needs | State |
|---|---|---|---|
| `XP-01` | P01, P02 | recognition point per document event | `PEER DEPENDENCY OPEN` |
| `XP-02` | P03 | the valuation-to-ledger handoff boundary | `PEER DEPENDENCY OPEN` |
| `XP-03` | P04 | depreciation period-attribution rule | `PEER DEPENDENCY OPEN` |
| `XP-10` | P04 → P08 | **inbound, received and closed**: irrevocable-lock relocation, the re-evaluation/posting contrast, the separate-subsidiary-store correction, and the tax-book gap re-registered as `P04-B-13` | **RECEIVED, VERIFIED, ACCEPTED** — see `09A` |
| `XP-04` | P05 | which company owns an expense claim's ledger effect | `PEER DEPENDENCY OPEN` |
| `XP-05` | P06 | the settlement event's own date | `PEER DEPENDENCY OPEN` |
| `XP-06` | P07 | the tax point as a carrier distinct from the accounting date; statutory statement layouts | `PEER DEPENDENCY OPEN` + `HOLD / EVIDENCE REQUIRED` |
| `XP-07` | P09 | whether an analytic dimension is a fact or an attribution | `PEER DEPENDENCY OPEN`; also `P08-BD-09` |
| `XP-08` | P01/P02 | intercompany settlement scope and ownership | `PEER DEPENDENCY OPEN` |
| `XP-09` | P11 | cross-process reconciliation of the scope assignments | `PEER DEPENDENCY OPEN` |

## 3. Evidence dependencies P08 could not discharge

| ID | Item | Class | What would close it |
|---|---|---|---|
| `P08-U-01` | Whether the suppression parameters are reachable end to end from an external caller | `SUPPORTED INTERPRETATION` pending execution | one executed call against a running instance |
| `P08-U-02` | Whether the custom access-check override module is installed in any deployment | `C NOT YET SEARCHED` | the deployed module registry |
| `P08-U-03` | Which copy of the project custom addon set is deployed | `D UNKNOWN` | deployment configuration |
| `P08-U-04` | Whether the residual-drift path manifests at runtime | `SUPPORTED INTERPRETATION` | one database query |
| `P08-U-05` | Whether a classification change that flips the reconcilability flag bypasses the residual routines | `D UNKNOWN` | runtime trial |
| `P08-U-06` | The statement-snapshot hook's behaviour on an inverted date range | `SUPPORTED INTERPRETATION` | runtime trial |
| `P08-U-07` | Whether the two rate-type shortcut sets produce a wrong figure or an unused row | `D UNKNOWN` | runtime trial |
| `P08-U-08` | Which of the 22 roots the deployed system runs | `D UNKNOWN` → `P08-BD-05` | a programme declaration |
| `P08-U-09` | The archive file inside the project custom addon set was listed but not content-searched | `C NOT YET SEARCHED` | extract and sweep |
| `P08-U-10` | The project custom addon set holds **65** modules with a manifest; this session examined roughly a dozen, and an independent reviewer opened 8 of the Thai localization modules. **The remainder were not reviewed for isolation behaviour.** | `C NOT YET SEARCHED` | a bounded sweep — **this is the highest-value remaining search**. Two of the eight Thai modules an independent reviewer opened yielded scope findings on first reading, which is the same two-of-two pattern that warns an empty class means unsearched, not absent |
| `P08-U-12` | Whether any mechanism reconciles a genuine subsidiary store (fixed-asset register, inventory valuation) to the ledger | `C NOT YET SEARCHED` | a bounded search P08 did not run; P04 reports six break mechanisms and no detector |
| `P08-U-11` | Thai statutory requirements bearing on statement format, retention and the accounting date | `HOLD / EVIDENCE REQUIRED` | authoritative evidence, Accounting-Tax track |

## 4. Boss decisions this session raises

| ID | Decision |
|---|---|
| `P08-BD-01` | Is the account number a tenant attribute or a per-company attribute? |
| `P08-BD-02` | May a tenant author a statutory statement layout, or only a management one? |
| `P08-BD-03` | May the platform hold a rate source, or must every tenant supply its own? |
| `P08-BD-04` | Are the accounting event and the posting instruction stored objects, or an append-only log? |
| `P08-BD-05` | Which of the 22 reference roots does SMEsPlus target? **Put with a stated limitation:** the product-line column supporting this decision is reproducible for only 14 of the 22 roots; the other 8 are inferred from directory naming and are marked as such. |
| `P08-BD-06` | Is the year-end result posted, or derived at report time? This determines whether a year can be reopened at all. **A reference implementation of the derived option exists and is described in this package; none of the posted option was found, class `B`.** *(Premise corrected after independent review.)* |
| `P08-BD-07` | Does the FX ruling's prohibition extend to the earliest-rate-ever substitution, not only to parity? **Premise corrected after independent review:** parity is present in **22 of 22** declared roots, so it is not avoidable by root choice; the earliest-rate-ever tier is present in **21 of 22** and is therefore **implementation-version dependent**. The draft stated the inverse of both. |
| `P08-BD-08` | Must reporting resolve a measurement identically to posting? |
| `P08-BD-09` | Is an analytic dimension a fact or an attribution? |
| `P08-BD-10` | The sequencing question of `P08-CONTRA-15`. |
| `P08-BD-12` | Does SMEsPlus hold a consolidation ledger with its own posted eliminations, minority-interest allocations and cumulative translation adjustment, or is consolidation a pure derivation with no adjustment capability? Raised by independent review, which observed the package's own consolidation requirement left eliminations with no home. |
| `P08-BD-13` | What is a company's functional currency, may it change, and where does a cumulative translation adjustment sit? |
| `P08-BD-14` | Does SMEsPlus carry a parallel cash-basis measurement, or does one ledger serve both bases? Related to `P08-BD-11`. |
| `P08-BD-15` | Which negative-claim class table governs the programme? Two instruments define `B`, `D` and `E` differently — see `P08-CONTRA-17`. |
| `P08-BD-11` | How many measurement bases must SMEsPlus carry over one set of accounting events, and in what form — parallel books, parallel valuations on one fact, or a derived adjustment layer? Raised by P04's re-opening of the tax-book gap. |

Each of these is normative, not factual. Further research cannot resolve any of them, which is why they are recorded here rather than left open as unknowns.
