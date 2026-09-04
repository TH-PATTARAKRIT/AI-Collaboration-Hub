# P08 ROOT SET DECLARATION — closing the programme's standing enumeration defect for P08's own claims

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

## 1. The defect this file addresses

The Account Wave A Final Closure round recorded the exact remaining enumeration defect as:

> The programme has never declared its **root set**. Every denominator, every path set and every class `A` absence in Wave A is scoped to **one reference core root of the 22 that exist**, and no artefact says which root, or that a choice was made.

and imposed the consequent rule, quoted here **in full and with its subject restored**:

> **Wave B** may make no class `A — VERIFIED ABSENCE` claim until `MCU-21` is closed. Until then every absence is class `C` with a stated boundary. **This is a hard rule and is the single most important thing carried out of Wave A.**

**Two corrections to how this session first handled that rule, both found by independent review.**

**(a) The draft elided the subject.** It quoted the rule as addressed to "every subsequent session"; it is addressed to **Wave B**. P08 is a process session, not Wave B. P08 nonetheless holds itself to the rule — a rule this strong should not be evaded on a technicality of addressee — but the elision was a mis-citation of a governing instrument in the file whose purpose is method integrity, and it is corrected here.

**(b) The parent's closing condition is genuinely ambiguous, and the draft took the favourable reading silently.** One line of the parent reads "may not declare class `A` **until the root set is declared**", which this session satisfies. The parent's own gating register defines `MCU-21` as "**which reference core root does SMEsPlus target?** 22 exist; none is declared", and its gate report says `MCU-21` "blocks every class `A` claim". Under **that** definition the condition is **unmet**, because which root SMEsPlus targets is a programme declaration this session cannot make. The conflict is recorded as an open contradiction (`P08-CONTRA-18`) rather than resolved in this session's favour.

`MCU-21` is closable by evidence, at low cost, and this session closes it **for its own claims**. It does not close it for the programme — declaring which root SMEsPlus *targets* is a programme declaration reserved to Boss, and is carried forward as `P08-BD-05`.

## 2. The declared root set

| Element | Value |
|---|---|
| `POPULATION` | every reference core root present on the project evidence volume |
| `PATTERN` | a whole-volume file search for the framework currency-model file at its canonical path within a base tree, reduced to the containing root, sorted. The literal command is recorded in `LAYER2_EVIDENCE_QUARANTINE/E00` §1. |
| `PATH SET` | the whole evidence volume, not a chosen subtree |
| `UNIT` | one core root (one directory containing a framework base module tree) |
| `DENOMINATOR` | **22** |

**The pattern's own boundary, declared:** a core root that omits or relocates the framework currency model is not discovered by it. The figure 22 is class `A` **over this declared pattern**, and is not a proof that 22 is the total number of roots on the volume. This reproduces the prior round's figure exactly and independently, from a different session, on the same declared pattern — which is the reproduction the method-convergence standard asks for and had not previously had.

### 2.1 The 22 roots

Root identities and their filesystem locations are **Layer 2** and are held in `LAYER2_EVIDENCE_QUARANTINE/E00` §1. Layer 1 refers to them as `R-01` … `R-22`.

| Root | Modules with a manifest | Product line |
|---|---|---|
| `R-01` | 804 | 18 |
| `R-02` | 802 | 18 |
| `R-03` | 498 | 18 |
| `R-04` | 1420 | 18 |
| `R-05` | 792 | 18 |
| `R-06` | 456 | 18 |
| `R-07` | 447 | 18 |
| `R-08` | 804 | 19 |
| `R-09` | 454 | 18 |
| `R-10` | 1433 | 19 |
| `R-11` | 1433 | 19 |
| `R-12` | 474 | 19 |
| `R-13` | 790 | 18 | **target root of this session**
| `R-14` | 1399 | 19 |
| `R-15` | 1273 | 18 |
| `R-16` | 638 | 18 |
| `R-17` | 636 | 18 |
| `R-18` | 28 | 18 |
| `R-19` | 1421 | 19 |
| `R-20` | 1420 | 19 |
| `R-21` | 1421 | 19 |
| `R-22` | 682 | 18 |

`R-13` is the root this session's detailed forensic work was performed against, and is the root the prior Account sessions used. `R-16`, `R-17` and `R-18` are nested inside `R-15`/`R-16`. Nesting is declared, not corrected — the pattern's unit is "a directory containing a framework base tree", and a nested server tree is such a directory.

**Version split, corrected after independent review: 14 roots on the 18 line, 8 on the 19 line.** The draft stated 13 / 9, which its own table does not support.

**The product-line column carries a declared boundary, which the draft did not give it.** Only **14 of the 22 roots carry a version file** to read a line from; the other 8 were classified **by directory name**, which is author inference, not data. Those 8 are marked `INFERRED` in the Layer 2 record. A count that feeds a Boss decision may not rest on an unmarked inference, and `P08-BD-05` is now put with that limitation stated.

## 3. Root-set-wide negative-claim scan

Three of P08's highest-impact negatives were re-run **across all 22 roots**, not against one. Each is now class `A` over the declared 22-root set rather than class `C` over one root.

| ID | Claim | Pattern | Result across 22 roots | Class |
|---|---|---|---|---|
| `RS-A-01` | **No accounting-event model exists.** | anchored model-name census per root, filtered to names containing the event token, deduplicated, with the event-management and framework namespaces excluded (`EV-P-05`) | **0 accounting-event models in 22 of 22 roots.** Residual matches belong to event management, calendar and barcode scanning; **none is an accounting construct**. | **A VERIFIED ABSENCE, scope = the declared 22-root set** |
| `RS-A-02` | **No period object carrying state, closure, or a link to an entry exists.** *(Re-worded after independent review. The draft published the unqualified sentence "no accounting-period entity exists", which its own close model contradicts: a named, dated, owned fiscal-year entity **does** exist in 13 of the 22 roots including the target root — it simply has no state, no close action, no posting and no link from any entry. The two-string lexical pattern below supports the re-worded claim and never supported the draft's.)* | anchored model-name census per root, filtered to accounting-period name forms (`EV-P-06`) | **0 in 22 of 22 roots.** | **A VERIFIED ABSENCE, scope = the declared 22-root set** |
| `RS-A-03` | **No database-level object enforces per-entry balance.** | **AMENDED after independent review.** Union of three patterns per root: (i) declared check-constraint bodies containing a sum over debit, credit or balance; (ii) trigger creation in program or schema files; (iii) deferred or exclusion constructs (`EV-P-07`). The original pattern was (i) alone, which **structurally could not have falsified the claim**, because a row-level check cannot aggregate across rows. | **0, 0 and 0 in 22 of 22 roots.** The framework demonstrably can emit an exclusion constraint elsewhere, so the capability exists and is not used for the ledger. | **A VERIFIED ABSENCE on the amended pattern, scope = the declared 22-root set** |

A fourth scan was run and is **not** promoted, because its pattern is vocabulary-based rather than structural:

| ID | Claim | Result | Class |
|---|---|---|---|
| `RS-B-01` | No year-end result-appropriation entry generator exists | Files matching the vocabulary pattern: 0 in 7 roots, 3 in 1 root, 8–9 in 5 roots, 19 in 1 root, 24 in 8 roots. The matches were not each opened. | **B NOT FOUND IN SEARCHED SCOPE at every scope** — the count varies with build completeness, and a vocabulary pattern cannot distinguish a result-appropriation generator from a tax-closing or session-closing routine. **The same objection applies at target-root scope**, so the narrower claim previously carried at class `A` in the close model is downgraded to `B` as well. |

And one positive is recorded because it is root-set-wide and bears directly on a frozen Boss semantic:

| ID | Claim | Result | Class |
|---|---|---|---|
| `RS-P-01` | **CORRECTED AND INVERTED after independent review.** The draft reported the three-tier fallback in 21 of 22 roots and attributed the exception to build incompleteness. That attribution is **wrong**, and the conclusion drawn from it is **inverted**. `R-18`'s framework currency file is **present and complete**; it holds an **older two-tier resolver**. Re-verified by the session author. | Corrected results across the declared 22-root set: **the parity fallback is present in 22 of 22 roots** — the draft understated its own strongest positive on a frozen Boss semantic. **The earliest-rate-ever tier is present in 21 of 22 and absent in `R-18`** — so that substitution **is** implementation-version dependent, which is the opposite of what the draft concluded. | **FACT VERIFIED on the corrected reading.** Consequence: `P08-BD-07` was put to Boss on an inverted premise and is re-stated in `18_P08_DEPENDENCY_REGISTER.md`. |

## 4. What this closes, and what it does not

**CORRECTED AFTER INDEPENDENT REVIEW. The draft's claim here was false of this package's own contents and is withdrawn.**

The draft asserted that "every class `A` in this package now carries either the declared 22-root scope or an explicitly narrower stated scope", and treated the second limb as satisfying the prohibition. **It does not.** A narrow stated scope is exactly what every prohibited prior class-`A` already had — that is the defect `MCU-21` names. Declaring the root set does not re-scope a claim that was never re-run against it.

**The true position:**

| Class-`A` claims in this package | Count | Status |
|---|---|---|
| Re-run across all 22 declared roots | **3** — `RS-A-01`, `RS-A-02` (as re-worded), `RS-A-03` (on the amended pattern) | **legitimately promoted; two of the three independently reproduced by a reviewer, and one strengthened by a wider pattern** |
| Scoped to **one root of 22**, or to a code region inside it, and **not** re-run | **~19** | **not covered by this closure.** They carry the same defect the prohibition exists to prevent |

The remaining ~19 are listed in `20_P08_EVIDENCE_MANIFEST.md` and are, pending either a re-run across the root set or a downgrade, **to be read as class `C` with a stated boundary**, not as class `A`. This session did not have the budget to re-run all nineteen and does not claim to have done so.

**Does not close:** `MCU-21` itself, nor the class-`A` prohibition for the ~19 single-root claims. Which root SMEsPlus targets is a programme declaration, not a research result. P08 records it as `P08-BD-05` and continues.

**Does not close:** the prior rounds' class-`A` claims. Those remain bounded to ≤1 root of 22 and this session does not re-scope another session's register.
