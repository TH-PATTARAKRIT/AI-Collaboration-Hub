> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 10 — CLASSIFICATION REASSESSMENT

Per directive §22: Fable's A–G classification is **independently re-derived here**, not
inherited. Every change documents Original Classification, New Classification, Reason,
Evidence, Impact. Unchanged classifications are also stated, so the reassessment is complete
rather than selective.

## CHANGES

### RC-01 — Exact-decimal money (Part 1: F-05/CV-09, "A — Universal principle")
```
Original:  A — Universal accounting principle
New:       D — Cross-ERP / computing common pattern
Reason:    No IFRS/IAS clause was found, this round or in Part 1, that specifically mandates
           decimal-over-float storage. This is a software-correctness engineering norm, widely
           and correctly followed, but citing it as an "accounting principle" overstates its
           provenance in exactly the way §9 warns against (never confuse the accounting need
           with the technical means of satisfying it).
Evidence:  Absence of a located IFRS citation after a genuine search attempt this round.
Impact:    Downgrades AP-12/CF-05's formal weight from "A" to "D" everywhere it appears in
           Part 2 artifacts. Does NOT change the underlying finding (money IS exact decimal,
           and that IS correct) — only its classification provenance.
```

### RC-02 — `hard_lock_date` irreversibility (Part 1: BR-14, stated as fact)
```
Original:  Stated as fact ("hard_lock_date is not reversible in the way other locks are"),
           cited to SE-24
New:       SUPPORTED INFERENCE (unconfirmed) — downgraded from implied VERIFIED FACT
Reason:    SE-24 anchors only the FIELD'S EXISTENCE (company.py L60-68, L78-99). No specific
           write-guard, validation, or mechanism preventing hard_lock_date from moving backward
           was ever read or cited. The claim of irreversibility is plausible (the field name
           and its separation from the other five locks suggest special handling) but is not,
           on the evidence actually cited, a verified fact.
Evidence:  Re-inspection of SE-24's actual content against BR-14's claim — a genuine gap
           between what was cited and what the citation shows.
Impact:    EC-11 and CF-03's point 12 in 02_CRITICAL_FINDING_REASONING both reflect this
           downgrade. Recorded in FABLE_SONNET_DISAGREEMENT_REGISTER.md as a material
           disagreement.
```

### RC-03 — Correction-by-reversal (Part 1: F-25, "D — cross-ERP common pattern, triangulated")
```
Original:  D — cross-ERP common pattern (from a single triangulation pass)
New:       D — CONFIRMED, but with an added qualifier: the reference system implements this
           pattern ALONGSIDE a directly conflicting one (reset-to-draft). Part 1 recorded the
           strength (reversal exists) without equally weighting the fact that the system does
           NOT force it, which this round's peer comparison (SAP B1 forbids editing/deleting
           posted docs entirely) makes a sharper, more consequential gap.
Reason:    Re-reading the SAP B1 citation shows it as a PROHIBITION on the alternative path, not
           merely an endorsement of reversal. The reference system has the good pattern but
           lacks the peer's prohibition on the bad one.
Evidence:  Same citations as Part 1, re-read more carefully against CF-06.
Impact:    Elevates CF-06 (not CF-04) to the domain's highest-priority advancement candidate —
           see 12_REFERENCE_TO_ADVANCEMENT_REGISTER ADV-04.
```

## CONFIRMED UNCHANGED (independently re-derived, not merely inherited)

| Finding | Part 1 class | Sonnet re-derivation | Result |
|---|---|---|---|
| Double-entry principle (Σdebit=Σcredit) | A | Re-derived from AP-01, independently triangulated this round | **CONFIRMED A** |
| Balance enforced app-only, suppressible, no DB backstop | E | Re-derived with STRONGER evidence (trigger census, CHECK-aggregation impossibility) | **CONFIRMED E**, evidence upgraded |
| Opt-in per-journal hash chaining | E | Re-derived; default value NOT independently confirmable (new unknown) | **CONFIRMED E**, with a flagged evidence gap |
| Six lock-date fields + bypass | E | Re-derived; NetSuite comparison confirms fragmentation is real, not opinion | **CONFIRMED E** |
| One table for all document types via `move_type` | E | Not independently re-triangulated this round (out of the 9 A6 targets); classification stands on Part 1's reasoning alone | **CONFIRMED E, but on unchanged evidence** |
| Row-level DB CHECK constraints exist | D | Re-verified directly; extended with MR-05 (four specific guarantees enumerated) | **CONFIRMED D**, detail expanded |
| Zero triggers database-wide | E (implicit) | Re-verified directly; this is the load-bearing fact behind CF-01's conclusion | **CONFIRMED**, now explicitly load-bearing |
| Thai statutory obligations | G — Unknown | **PARTIALLY RESOLVED** this round for two sub-questions (e-Tax integrity, tax-invoice numbering); the GENERAL-LEDGER-WIDE versions of both remain G | **SPLIT**: B for narrow scope, G for broad scope |

## NET EFFECT ON THE 20_CLASSIFICATION_A_G.md TOTALS (Part 1: A4·B4·C2·D4·E7·F2·G4=27)
This reassessment does not re-total Part 1's register (that would overwrite forensic history,
prohibited by §26). It records, as a **separate synthesis-layer view**, that: 1 finding moves
A→D (RC-01), 1 finding's confidence is downgraded within E (RC-02), 1 finding (Thai statutory)
splits from G into B+G rather than resolving cleanly, and 2 new sub-findings emerge from
deeper math reasoning (MR-02's balance-column gap, and the several new exception-analysis
unknowns) that were not separately classified in Part 1's 27-finding count.
