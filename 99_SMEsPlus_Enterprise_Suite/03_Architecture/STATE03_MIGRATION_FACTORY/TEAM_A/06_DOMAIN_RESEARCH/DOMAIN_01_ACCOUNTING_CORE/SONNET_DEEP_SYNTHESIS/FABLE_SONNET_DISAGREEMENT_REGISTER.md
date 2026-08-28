> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Required by directive §27

# FABLE / SONNET DISAGREEMENT REGISTER

Per §27: material disagreements are recorded even though Fable's Part 1 findings were not
wrong in their headline conclusions. "No disagreement" is not claimed where a disagreement
exists — three are recorded below. This is not a verdict that Part 1 is unreliable; the
corrective round (CORR-001) already demonstrated Fable's own willingness to retract an unsafe
claim. These are further refinements in the same spirit.

## DISAGREEMENT-01 — `hard_lock_date` irreversibility (BR-14)
```
FABLE FINDING:     "hard_lock_date is not reversible in the way other locks are"
                   (06_BUSINESS_RULE_REGISTER.md, BR-14), cited to SE-24, phrased as fact.
SONNET ANALYSIS:   SE-24 anchors only the field's EXISTENCE (company.py lock-date field
                   declarations). No write-guard, validation method, or specific mechanism
                   preventing the value from moving backward was ever read or cited anywhere
                   in the evidence chain.
EVIDENCE:          Direct re-inspection of SE-24's actual content against BR-14's claim.
RESOLUTION STATUS: DOWNGRADED — from implied VERIFIED FACT to SUPPORTED INFERENCE
                   (unconfirmed). Recorded in 10_CLASSIFICATION_REASSESSMENT.md RC-02.
                   Does not invalidate Part 1's broader CF-03 finding (six independent lock
                   controls, fragmented vs. peer practice), which stands on its own, separately
                   evidenced grounds.
```

## DISAGREEMENT-02 — Exact-decimal money as "universal accounting principle"
```
FABLE FINDING:     CV-09 classified exact-decimal money storage as approaching Class A
                   ("universal principle"-adjacent framing in the executive summary).
SONNET ANALYSIS:   No IFRS/IAS clause specifically mandating decimal-over-float storage exists
                   to be cited. This is a software/financial-computing engineering norm, not a
                   formal accounting standard. Classifying it as "A" risks exactly the
                   provenance-overclaiming the corrective round (CORR-001) already had to
                   retract once (the CHECK-constraint claim).
EVIDENCE:          Genuine search attempt this round found no such standard; absence recorded
                   honestly rather than treated as confirmation either way.
RESOLUTION STATUS: RECLASSIFIED — A to D. Recorded in 10_CLASSIFICATION_REASSESSMENT.md RC-01.
                   The underlying finding (money IS exact decimal, and this IS correct) is
                   UNCHANGED — only its claimed provenance is corrected.
```

## DISAGREEMENT-03 — Weighting of the reversal/reset-to-draft tension
```
FABLE FINDING:     CF-04 (reversal) and CF-06 (mutable history) were recorded as two separate,
                   independently important findings, with ADV-04 (in Part 1's Team B input)
                   framed primarily around CF-06 in isolation.
SONNET ANALYSIS:   Re-reading the SAP B1 peer-comparison evidence shows it as a PROHIBITION on
                   the reset-to-draft alternative, not merely an endorsement of reversal as one
                   good option among others. The reference system's problem is not merely "one
                   weak pattern exists" — it is that a demonstrably sound pattern (reversal)
                   coexists with, and is not preferred over, a demonstrably unsound one
                   (reset-to-draft), for the identical business need.
EVIDENCE:          Same citations as Part 1 (sap-business-one-tips.com, SAP Community), read
                   more carefully against both CF-04 and CF-06 together rather than each in
                   isolation.
RESOLUTION STATUS: ELEVATED PRIORITY — ADV-04 is re-ranked as the domain's single highest-
                   priority advancement candidate (12_REFERENCE_TO_ADVANCEMENT_REGISTER.md).
                   No fact changes; the synthesis-level emphasis does.
```

## NO FURTHER MATERIAL DISAGREEMENT FOUND
Beyond the three items above, this round's independent re-derivation of Part 1's
classifications, critical findings, database evidence, and gap register **confirms** them.
Where Part 1 already performed a self-correction (the CORR-001 CHECK-constraint retraction),
this round found that correction to be sound and did not re-open it.

## SONNET-CORR-001 SELF-CORRECTION (not a Fable/Sonnet disagreement — a Sonnet error, corrected)
Recorded here for completeness rather than omitted, even though it is not a disagreement with
Fable's Part 1 work: it is an error Sonnet introduced and then corrected within Part 2 itself.

```
CLAIM MADE:        commit b2e5a2ab7f820fee351475d84a4b3c7eceb3ded3 does not exist in the
                   repository (00_SONNET_SYNTHESIS_INDEX.md, original version)
ROOT CAUSE:        verification was performed on a shallow clone (`git clone --depth 1`),
                   which fetches only the branch tip with no ancestor history; `git log` on
                   that clone showed 3 commits because that is all a depth-1 clone contains,
                   not because the repository has 3 commits
CORRECTION METHOD: unshallowed the clone (`git fetch --unshallow`) and independently
                   re-verified via the GitHub API directly by SHA, bypassing local git
                   reachability entirely as a second, independent check
RESULT:            all 5 cited commits confirmed present in one linear chain; the claim of a
                   missing commit is RETRACTED
IMPACT:            none on any critical finding, invariant, rule, or advancement candidate —
                   this was a provenance/audit-trail bookkeeping error, not a domain-content
                   error
LESSON:            identical in kind to the CORR-001 (Part 1) retraction of the "zero CHECK
                   constraints" claim: a derived or truncated instrument's silence is not proof
                   of absence. This lesson was documented in Part 1 and then violated by
                   Sonnet in Part 2 before being caught by ChatGPT's independent audit — a
                   genuine illustration of why independent audit exists as a gate.
```
