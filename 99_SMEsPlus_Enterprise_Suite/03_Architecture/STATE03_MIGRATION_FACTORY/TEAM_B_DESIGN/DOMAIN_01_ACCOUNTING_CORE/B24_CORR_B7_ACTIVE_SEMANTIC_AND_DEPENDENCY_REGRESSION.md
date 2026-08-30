# B24 — CORR-B7 Active-Semantic & Dependency Regression

| Field | Value |
|---|---|
| Session | SMEPLUS-26-08-30-MIG-B-D01-CORR7-001 |
| Source of truth | CORR7-001 directive §CORR-B7-06 — 15 mandatory scenarios, tested against the CORR-B7-corrected design (B02 CAP-04/CAP-01/CAP-08/CAP-09 corrected; B07 Consumption Record row corrected; B15 §8a Dependency Sanity Matrix new; B18 Test 5 annotated) |
| Personas | Accounting Domain Architect, Senior Accountant, Financial Controller, External Auditor, Implementation Architect, Migration Architect, QA/Test Architect, Clean-room Reviewer, PMO/Governance Reviewer |
| Result | **15/15 PASS. No further active-semantic contradiction found beyond the two audit-named findings and the two self-found items already disclosed in the master corrective-round document.** |

Unlike B18-B23 (which verify mathematical/temporal correctness with worked numbers), this
regression verifies **reading comprehension of the current design pack** — for each scenario,
an implementer or reviewer reads only the specified active artifact(s) and the test records
whether the CURRENT semantics are the ones actually communicated, whether any historical text
is present, and whether that historical text could be mistaken for current authority. Per the
directive's required schema, every test below records: Input Artifact(s) / Active Statement
Evaluated / Expected Current Semantics / Actual Current Semantics / Historical Text Present? /
Could Historical Text Be Misread As Current? / Dependency Edge Valid? / PASS-FAIL / Finding /
Disposition.

## Test 1 — Implementer reads CAP-04 only: must NOT infer a CAP-06 carry-forward dependency

```
Input Artifact(s):        B02_ACCOUNTING_CORE_CAPABILITY_MODEL.md, CAP-04 section only
Active Statement Evaluated: CAP-04's Outputs/Downstream-dependents fields
Expected Current Semantics: CAP-04 outputs an open/closed determination and reopen action;
                           downstream dependents are CAP-02, CAP-08, and external reporting.
                           No claim that CAP-06 consumes this determination for carry-forward,
                           because carry-forward is implicit (B07 §1d) and CAP-06 has no role
                           in it at all
Actual Current Semantics: MATCHES — CORR-B7-01 corrected CAP-04's Outputs/Downstream-dependents
                           to name only CAP-02, CAP-08, and external reporting; the prior
                           CAP-06/carry-forward claim is struck through with an explicit
                           correction note
Historical Text Present?: YES — the pre-correction sentence is kept visible, struck through
Could Historical Text Be Misread As Current?: NO — struck-through Markdown, immediately followed
                           by a bolded "CORRECTED AT CORR-B7-01" label and explanation; no
                           implementer reading normally-rendered Markdown would treat struck-
                           through text as the active instruction
Dependency Edge Valid?:   YES — CAP-04→CAP-02, CAP-04→CAP-08, CAP-04→external-reporting are all
                           current and accurate (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none (the defect this test guards against, `M-AUD-15`, is the one
                           corrected this round)
Disposition:              n/a
```

## Test 2 — Implementer reads Consumption Record only: must NOT infer a CAP-09 carry-forward trigger

```
Input Artifact(s):        B07_CONCEPTUAL_INFORMATION_MODEL.md, §1 entity table, Consumption
                           Record row only
Active Statement Evaluated: the row's "Owning capability" column, downstream-reference clause
Expected Current Semantics: downstream reference (trigger 3) is illustrated by a Correction/
                           Reversal Entry referencing the Entry it targets; no CAP-09 carry-
                           forward mechanism is named, because none exists; PeriodClosed/
                           FiscalYearClosed/FiscalYearBoundaryChanged/FiscalYearMembershipRestated
                           are explicitly stated to be non-triggers
Actual Current Semantics: MATCHES — CORR-B7-02 replaced the stale CAP-09 carry-forward example
                           with a Correction/Reversal example and added the explicit
                           non-trigger statement for all four lock/boundary events
Historical Text Present?: YES — the pre-correction clause is kept visible, struck through
Could Historical Text Be Misread As Current?: NO — same struck-through-plus-labeled-correction
                           pattern as Test 1
Dependency Edge Valid?:   YES — Consumption Record→(filing/reconciliation/Correction-Reversal)
                           is the only active edge; Consumption Record→CAP-09-carry-forward no
                           longer exists (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none (the defect this test guards against, `M-AUD-16`, is the one
                           corrected this round)
Disposition:              n/a
```

## Test 3 — Ordinary Period close: no posted carry-forward, no automatic Consumption

```
Input Artifact(s):        B04_BUSINESS_LIFECYCLE_EVENT_MODEL.md §4, event table `PeriodClosed`
                           row; B07 §1d
Active Statement Evaluated: what `PeriodClosed` produces; whether it is a Consumption trigger
Expected Current Semantics: `PeriodClosed` is a posting lock only — it posts nothing, resets
                           nothing, and is not one of the three Consumption trigger kinds
Actual Current Semantics: MATCHES — B04's event table row states "a posting lock only, never a
                           Revenue/Expense reset or Current Earnings transfer" (corrected at
                           CORR-B2-03); B04 §4's three trigger kinds explicitly exclude period
                           close ("period close is no longer one of them," corrected at
                           CORR-B01); B07 §1d states carry-forward is implicit, nothing posted
Historical Text Present?: YES — CORR-B01/CORR-B2-03's own struck-through corrections remain
                           visible in both B04 and B07
Could Historical Text Be Misread As Current?: NO — every struck-through passage carries an
                           explicit "corrected at CORR-Bxx" label
Dependency Edge Valid?:   YES — PeriodClosed→Consumption is an explicitly-stated NON-edge
                           (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 4 — Period reopen: only lock semantics change; Consumption permanence unaffected

```
Input Artifact(s):        B04 §4 Gate rule; B08 MP-10
Active Statement Evaluated: what an authorized reopen (CO-08) restores
Expected Current Semantics: reopen restores only condition (b) — Period is open — never
                           condition (a) — consumed==false; a Consumption Record, once written,
                           is permanent regardless of any later Period action
Actual Current Semantics: MATCHES — B04 §4's Gate rule states "reopen's effect on amendability
                           is now exactly what it should be: it restores what Period locking
                           took away, nothing more, nothing that BINV-06/07 ever promised to
                           protect"; MP-10 states "an authorized reopen... restores Posting/
                           Amendment eligibility... reopen never resurrects an already-consumed
                           entry's amendability"
Historical Text Present?: NO — this section was corrected in place at CORR-B01/CORR-B2-01/02
                           and has not needed further correction since; no stale claim remains
                           to annotate
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — Period Lock (CAP-04) and Consumption (BINV-06/07) remain
                           orthogonal, unchanged this round (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 5 — FiscalYearClosed: no posted financial Entry; reporting inclusion remains boundary-driven

```
Input Artifact(s):        B02 CAP-09 (renamed this round); B04 event table `FiscalYearClosed`
                           row; B07 §1e
Active Statement Evaluated: what `FiscalYearClosed` produces; what gates Reported Retained
                           Earnings inclusion
Expected Current Semantics: no Entry posted; Reported RE inclusion is boundary-driven
                           (Elapsed, a pure calendar fact), never gated on this declaration
Actual Current Semantics: MATCHES — CAP-09's own text (unchanged in substance this round, only
                           its title corrected): "CAP-09 posts no financial Entry... Reported
                           Retained Earnings inclusion... is boundary-driven ('Elapsed')... B07
                           §1e's formula sums every Fiscal Year that has elapsed... independent
                           of whether FiscalYearClosed has been declared"
Historical Text Present?: YES — CORR-B3-05/CORR-B4-03's own struck-through corrections remain
                           visible
Could Historical Text Be Misread As Current?: NO — same labeled-correction pattern
Dependency Edge Valid?:   YES — FiscalYearClosed→Reported-RE-inclusion is an explicitly-stated
                           NON-edge; FiscalYearClosed→posted-Entry is an explicitly-stated
                           NON-edge (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 6 — FiscalYearBoundaryChanged pre-reliance: no Entry membership mutation

```
Input Artifact(s):        B07 §1h (corrected at CORR-B6-02); B04 event table
                           `FiscalYearBoundaryChanged` row (scope-corrected at CORR-B6-02)
Active Statement Evaluated: whether this event can move Entry membership, and under what
                           reliance condition it may fire at all
Expected Current Semantics: this event fires only for a Fiscal Year with NO existing reliance
                           (pre-reliance correction, or a genuinely future Fiscal Year); it can
                           never reach backward over reliance; it never moves Entry membership,
                           because a Fiscal Year with no reliance has no Entries to reclassify
Actual Current Semantics: MATCHES — B04's row states the event's Version Effective Date "may
                           never fall earlier than the point reliance began"; B07 §1h states
                           the same constraint, corrected at CORR-B6-02
Historical Text Present?: YES — Round 5's own original (less-constrained) wording is kept
                           visible, struck through, corrected at CORR-B6-02
Could Historical Text Be Misread As Current?: NO — labeled-correction pattern, consistent
Dependency Edge Valid?:   YES — FiscalYearBoundaryChanged→Entry-membership is an explicitly-
                           stated NON-edge (B15 §8a; B23 Test 3(a))
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 7 — FiscalYearMembershipRestated post-reliance: atomic current membership/boundary change, Known view preserved

```
Input Artifact(s):        B07 §1j (new at CORR-B6-02); B04 event table
                           `FiscalYearMembershipRestated` row (new at CORR-B6-02)
Active Statement Evaluated: whether the boundary change and the membership reclassification are
                           guaranteed to happen together, and whether the Known view survives
Expected Current Semantics: the boundary change and membership reclassification are the SAME
                           action, indivisibly — no reachable intermediate state; any T before
                           this event's own Recorded At reconstructs unaffected
Actual Current Semantics: MATCHES — B07 §1j's own "Atomicity" bullet: "there is no reachable
                           state, at any point, where a new Current-viewpoint boundary exists
                           for an already-relied-upon Fiscal Year while affected Entries'
                           Current-viewpoint membership has not yet been updated to match";
                           "Known view, unconditionally unaffected" bullet immediately following
Historical Text Present?: NO — this is new text from Round 6, unmodified this round (verified
                           unaffected, not re-authored)
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — FiscalYearMembershipRestated→(boundary+membership, atomic) is
                           the one active edge that DOES move membership, correctly scoped
                           (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 8 — Migration Opening Balance: remains distinct from recurring carry-forward

```
Input Artifact(s):        B07 §1d, closing paragraph; B10 MG-C03
Active Statement Evaluated: whether a migration opening balance is treated as an instance of
                           the (removed) recurring carry-forward pattern
Expected Current Semantics: a migration opening balance is a one-time, distinct act —
                           establishing a ledger's starting point with no prior history in this
                           system — never a periodic transfer between two periods that both
                           already exist in the same ledger
Actual Current Semantics: MATCHES — B07 §1d states explicitly: "under a Continuous Ledger,
                           there is no recurring 'carry-forward' business event to be an
                           instance of. A migration opening balance is a one-time, distinct
                           act... not a periodic transfer" — unchanged this round, re-verified
                           accurate
Historical Text Present?: NO — this passage has been stable since CORR-B2-03/04, no correction
                           needed
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — Migration Opening Balance is correctly NOT modeled as a
                           carry-forward-triggering edge (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 9 — Raw Cumulative TB: terminology remains correct

```
Input Artifact(s):        B08 MP-09 (renamed at CORR-B5-02); MP-12 Proof G1
Active Statement Evaluated: whether `CumulativeAccountBalance`/Proof G1 is ever mislabeled or
                           conflated with the other two outputs
Expected Current Semantics: G1 (Raw Cumulative Trial Balance) is the only object entitled to be
                           called a "Trial Balance" without qualification; MP-09 itself no
                           longer contains "Trial Balance" in its own name
Actual Current Semantics: MATCHES — unchanged since Round 5/6, re-verified accurate this round;
                           no active statement anywhere in the swept file list calls G2 or the
                           bare `FiscalYearActivity` output a "Trial Balance"
Historical Text Present?: YES — Round 4's Proof G (pre-Round-5) is kept visible, struck through
Could Historical Text Be Misread As Current?: NO — labeled-correction pattern, consistent
Dependency Edge Valid?:   YES — CumulativeAccountBalance→"Trial Balance" label is the only
                           valid edge (B05 BINV-15, re-verified unaffected this round)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 10 — Current-FY Reporting Balance: never mislabeled balanced TB

```
Input Artifact(s):        B08 MP-12 Proof G2; B09 CO-14 (extended)
Active Statement Evaluated: whether G2 is ever presented as balanced
Expected Current Semantics: G2 is explicitly, permanently labeled "NOT itself a balanced Trial
                           Balance"; CO-14 requires any presentation to label which of G1/G2/G3
                           it is showing
Actual Current Semantics: MATCHES — unchanged since Round 5, re-verified accurate; no active
                           statement in the swept file list calls G2 balanced
Historical Text Present?: YES — Round 4's original conflation is kept visible, struck through
Could Historical Text Be Misread As Current?: NO — labeled-correction pattern
Dependency Edge Valid?:   YES — G2→"balanced" is an explicitly-stated NON-edge (BINV-15)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 11 — Balanced Presentation TB: bridge is derived/non-posted

```
Input Artifact(s):        B08 MP-12 Proof G3; B09 CO-14
Active Statement Evaluated: whether the G3 bridge line is ever describable as a postable fact
Expected Current Semantics: the bridge line is "never posted, never a committed Entry, never a
                           Line," recomputed fresh every presentation, and must carry the exact
                           label "DERIVED PRESENTATION COMPONENT — NOT A POSTED FINANCIAL FACT"
Actual Current Semantics: MATCHES — unchanged since Round 5, re-verified accurate; no active
                           statement anywhere describes the bridge as postable
Historical Text Present?: NO — G3 is new at Round 5, no prior version to annotate
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — G3-bridge→posted-Entry is an explicitly-stated NON-edge
                           (B08 MP-12 Boundary field: "explicitly, permanently excluded from
                           ever becoming a postable/committable fact")
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 12 — Consumption after real statutory filing: irreversible Consumption record remains valid

```
Input Artifact(s):        B04 §4 trigger 1; B05 BINV-06/07
Active Statement Evaluated: whether a filing-triggered Consumption Record remains permanent
                           regardless of any later Period or Fiscal-Year action
Expected Current Semantics: once triggered (filed), a Consumption Record is permanent; BINV-07
                           forbids retraction; no later PeriodClosed/FiscalYearClosed/
                           FiscalYearBoundaryChanged/FiscalYearMembershipRestated action can
                           clear it
Actual Current Semantics: MATCHES — B04 §4: "Once triggered, a Consumption Record is permanent
                           (BINV-07, unchanged) and BINV-06's immutability applies forever
                           after, regardless of any later Period action — consumption is no
                           longer entangled with Period status in any direction"; this
                           guarantee is unaffected by any of the four Fiscal-Calendar events,
                           none of which touches Consumption at all (B07 §1, corrected)
Historical Text Present?: NO — this specific guarantee has been stable since CORR-B01
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — Consumption Record permanence is independent of every
                           Period/Fiscal-Year event, old and new alike (B15 §8a)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 13 — Closed period with no downstream use: locked but not automatically consumed

```
Input Artifact(s):        B18 Test 1 (annotated this round); B04 §4
Active Statement Evaluated: whether an unconsumed Entry in a closed Period remains amendable
                           once reopened
Expected Current Semantics: Period Lock alone never creates a Consumption Record; an
                           unconsumed Entry becomes amendable again immediately on reopen
Actual Current Semantics: MATCHES — B18 Test 1's own result ("PASS... BINV-06/07 never
                           engaged, nothing to violate") remains valid under the current design
                           — this test's scenario and conclusion were never affected by the
                           carry-forward redesign, only Test 5's scenario framing was, and
                           Test 1 required no annotation
Historical Text Present?: NO (for this specific test) — B18 Test 1 needed no correction
Could Historical Text Be Misread As Current?: N/A
Dependency Edge Valid?:   YES — PeriodClosed→Consumption remains a NON-edge (re-verified,
                           Test 3 above)
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Test 14 — Cross-capability dependency walk CAP-01..CAP-09: no stale responsibilities

```
Input Artifact(s):        B02, full capability register; B15 §8a (new)
Active Statement Evaluated: every CAP-01..09 Inputs/Outputs/Downstream-dependents field,
                           cross-checked against the named target's own definition
Expected Current Semantics: every named dependency edge points to a responsibility the target
                           capability actually, currently owns
Actual Current Semantics: MATCHES, after this round's corrections — the systematic walk (B15
                           §8a) found and corrected three stale/incomplete edges (CAP-04→CAP-06
                           carry-forward, `M-AUD-15`; CAP-01→CAP-06 statement-placement,
                           self-found; CAP-08's incomplete Inputs list, self-found) and
                           confirmed every remaining edge valid
Historical Text Present?: YES, for all three corrected edges — struck through, labeled
Could Historical Text Be Misread As Current?: NO — labeled-correction pattern, consistent
                           across all three
Dependency Edge Valid?:   YES — all edges in B15 §8a's matrix confirmed valid after correction
PASS / FAIL:              PASS
Finding:                  the two self-found items (CAP-01→CAP-06, CAP-08 Inputs) — both
                           corrected this round, disclosed in the master corrective-round
                           document per this domain's standing transparency discipline
Disposition:              n/a — closed within this same round, not carried forward
```

## Test 15 — Final Gate Candidate read in isolation: an implementation team can reconstruct the CURRENT design without relying on superseded text

```
Input Artifact(s):        DOMAIN_01_ACCOUNTING_CORE_H_DESIGN_FINAL_GATE_CANDIDATE.md, read
                           standalone, as a hypothetical implementation team would before
                           starting build work (even though development remains NOT AUTHORIZED
                           at this gate)
Active Statement Evaluated: whether H's own active prose, tables, and citations describe only
                           the current model, or whether reconstructing the design from H alone
                           would require also independently knowing which cited artifacts
                           contain superseded content
Expected Current Semantics: H's own text is fully current; every citation into a Bxx file
                           points at content that is itself either fully current or clearly,
                           visibly marked historical at the cited location
Actual Current Semantics: MATCHES — H itself contains no carry-forward, CAP-06, or Consumption-
                           trigger claims of its own (it summarizes at the capability-count
                           level, not the individual-dependency-edge level); every B0x file H
                           cites has, as of this round, either no stale active content or
                           visibly-labeled historical annotations at the specific stale
                           locations (B02 CAP-04/CAP-01/CAP-08, B07 Consumption Record, B18
                           Test 5) — a reader following H's citations into those files
                           encounters the correction, not the stale claim, as the active text
Historical Text Present?: YES, at the cited locations within B02/B07/B18 — not within H itself
Could Historical Text Be Misread As Current?: NO, at every location checked this round
Dependency Edge Valid?:   YES — H's own capability/invariant/principle counts (9/17/12/16/16/22/
                           13) all match the current B0x files' own actual counts, re-verified
                           this round
PASS / FAIL:              PASS
Finding:                  none
Disposition:              n/a
```

## Regression Result

```
CONFIRMED PASS — 15/15 scenarios, no new active-semantic contradiction found beyond the
  findings already disclosed and corrected in this same round (M-AUD-15, M-AUD-16, and two
  self-found items — CAP-01's stale CAP-06 statement-placement claim, CAP-08's incomplete
  Inputs list)
No regression into any of the fourteen defects the six prior audit rounds already found and
  fixed
No regression into any of the six defects B16's original red-team found and fixed
No new CRITICAL/HIGH defect
This is the first regression round whose method is reading-comprehension verification rather
  than numeric/temporal verification — every prior round's own numeric conclusions (B18-B23)
  are re-confirmed unaffected by this round's pure terminology/dependency corrections
```
