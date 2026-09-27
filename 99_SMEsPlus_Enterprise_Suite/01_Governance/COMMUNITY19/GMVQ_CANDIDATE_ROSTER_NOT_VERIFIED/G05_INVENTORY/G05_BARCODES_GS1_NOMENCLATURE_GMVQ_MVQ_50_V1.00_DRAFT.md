# G05 INVENTORY — MODULE-SPECIFIC QUESTION BANK (MVQ)

- Document ID: G05-BARCODES_GS1_NOMENCLATURE-GMVQ-MVQ-V1.00-DRAFT
- Group: G05 INVENTORY
- Module Metadata: barcodes_gs1_nomenclature
- Wave: W2
- Author Cell: P06
- Review Cell: PENDING
- Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
- actual_mvq_count: 50
- Purpose: Module-specific research questions (MVQ) for the blind two-lane study. Lane A
  reads reference source and answers independently; Lane B observes a running system only.
  The Reconciler joins answers on MODULE + QID. This bank covers decoding a structured symbol
  into distinct business facts (item, lot, quantity, date encoded together in one string) — not
  the scan event itself as an input path, which is covered by the sibling bank `barcodes`.
- Control: Authored under GMVQ_AUTHORING_STANDARD_V1.00.md and GMVQ_BRIDGE_MODULE_RULE_V1.00.md.
  Clean Room: no vendor or reference source tree was consulted in authoring this bank; content
  draws on generic ERP/WMS domain knowledge and publicly documented structured-barcode
  encoding concepts only. Not approved. Not frozen. Not verified. Not MASTER-ready. DRAFT
  content only. This document does not authorize any merge, release, or STATE/gate closure.
- Vocabulary note: this module's metadata name carries a standards-body token. That token
  appears in the `MODULE:` field above only. Every question below refers to the encoding in
  question generically as "the structured symbol format," per the routing instruction for
  this bank, so the blind lane is not cued by name.

## A/B boundary note
This bank is scoped strictly to INTERPRETATION: turning the elements packed into one scanned
string into distinct, correctly-typed business facts (which item, which lot, what quantity,
what date) and what happens when that interpretation is ambiguous, contradicted, malformed, or
changes over time. Any question about the scan EVENT itself — focus, timing, commit semantics,
attribution, reservation interaction — belongs to the sibling bank `barcodes` and is
intentionally excluded here to avoid the near-duplicate defect described in
GMVQ_BRIDGE_MODULE_RULE_V1.00.md.

---
```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q001
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a quantity decoded from the structured symbol format disagrees with the quantity
  already entered by the operator or shown on the source document, the system requires
  explicit resolution rather than silently picking one value.
WHY_IT_MATTERS: >
  A silent pick between two disagreeing quantities can commit a business decision on the
  wrong number with nobody ever seeing that a disagreement existed.
DISCONFIRMING_OBSERVATION: >
  A disagreement between the decoded quantity and the manually entered or documented quantity
  resolves silently, with no indication anywhere that a conflict existed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Prepare a symbol whose encoded quantity differs from the quantity already present on the
  document or entered by the operator, then decode it against that document.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q002
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a date decoded from the structured symbol format disagrees with a date already present
  on the related document, the discrepancy is recorded rather than one value being discarded
  outright.
WHY_IT_MATTERS: >
  Discarding one of two disagreeing dates without a trace removes the ability to later
  determine which source was actually correct.
DISCONFIRMING_OBSERVATION: >
  The date discrepancy disappears entirely — only one value remains in the record with no
  trace that the other value ever existed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Prepare a symbol whose encoded date differs from a date already on the related document,
  then decode it and inspect what is retained.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q003
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The precedence rule for a decoded-versus-documented disagreement (which source wins) is a
  configurable business decision, not hardcoded to always favor one source.
WHY_IT_MATTERS: >
  A single hardcoded precedence may be correct for one business process and wrong for
  another that uses the same decoding capability.
DISCONFIRMING_OBSERVATION: >
  The same class of decoded-versus-documented disagreement is always resolved the same way,
  with no configuration point available to change which source wins.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Locate any setting governing which source wins on disagreement, and test whether changing
  it changes the resolution outcome for an otherwise identical disagreement.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q004
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A disagreement large enough to be operationally significant (for example, a dramatically
  different quantity) is escalated for human review rather than auto-resolved the same way a
  trivial rounding difference would be.
WHY_IT_MATTERS: >
  Treating a large, consequential discrepancy the same as a negligible one risks silently
  acting on a value that is materially wrong.
DISCONFIRMING_OBSERVATION: >
  A large, operationally significant discrepancy is auto-resolved identically to a trivial
  rounding difference, with no escalation of any kind.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create both a trivial and a materially significant disagreement between decoded and
  documented values, and compare how each is handled.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q005
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a decoded-versus-documented disagreement is resolved, whether by rule or by human
  decision, that resolution remains distinguishable in the record from a symbol that never
  disagreed with anything.
WHY_IT_MATTERS: >
  Without a distinguishing trace, later review cannot tell which records ever needed a
  disagreement resolved, undermining any audit of how often it happens.
DISCONFIRMING_OBSERVATION: >
  A resolved disagreement and a symbol that always matched the document look identical in the
  stored record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Resolve a decoded-versus-documented disagreement, then compare the resulting record to one
  from a symbol that never disagreed with anything.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q006
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An element with a variable declared length that is shorter or longer than expected causes a
  detectable decode failure, rather than every subsequent element in the same string being
  silently misread but accepted as valid.
WHY_IT_MATTERS: >
  A silent field-shift produces plausible-looking but entirely wrong business facts (wrong
  item, wrong lot, wrong quantity) with no indication anything went wrong.
DISCONFIRMING_OBSERVATION: >
  A variable-length parsing error shifts every subsequent element in the string, and the
  shifted result is accepted as though it were correctly parsed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string containing a variable-length element with an unexpected actual length,
  followed by further elements, and decode it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q007
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each decoded element is validated against the expected format (length and character set) for
  its position before being accepted, rather than whatever falls into that position being
  accepted at face value.
WHY_IT_MATTERS: >
  Accepting whatever occupies a position without validating it lets a malformed or
  misaligned element pass through as though it were legitimate data.
DISCONFIRMING_OBSERVATION: >
  A decoded element that does not match the expected format for its position is still
  accepted as valid data.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string where one element's content does not match the expected format for its
  position, and decode it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q008
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A parsing failure caused by a length mismatch is reported as a decode error at the point of
  decoding, not surfaced only later as a seemingly unrelated business rule violation.
WHY_IT_MATTERS: >
  Surfacing the failure far from its true cause makes diagnosing a decoding defect far harder
  than it needs to be.
DISCONFIRMING_OBSERVATION: >
  A length-mismatch parsing failure only becomes visible much later as an apparently unrelated
  error (for example, an invalid lot reference), obscuring the actual cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a string with a length mismatch that would only surface downstream, decode it, and
  trace where the resulting error is actually reported.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q009
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two elements of different declared lengths appearing back-to-back in the same string are
  decoded without content from one bleeding into the other.
WHY_IT_MATTERS: >
  Bleed between adjacent elements corrupts both of the resulting business facts at once.
DISCONFIRMING_OBSERVATION: >
  Two adjacent variable-length elements are decoded with content from one appearing inside
  the other's decoded value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string with two adjacent elements of different declared lengths and decode it,
  checking each resulting value independently.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q010
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A malformed variable-length element does not get silently truncated or padded to force it to
  fit the expected length.
WHY_IT_MATTERS: >
  Silent truncation or padding manufactures a plausible-looking value that does not correspond
  to what was actually printed or encoded.
DISCONFIRMING_OBSERVATION: >
  Data that does not fit the expected length for its element is silently truncated or padded
  rather than being flagged as malformed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct an element whose content is shorter or longer than its expected length and decode
  it, checking whether the value is adjusted to fit rather than rejected.
```
```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q011
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An element type that the current configuration does not recognise is flagged as unrecognised
  rather than silently skipped as though it were never present in the string.
WHY_IT_MATTERS: >
  A silently vanishing element hides the fact that part of what was physically encoded was
  never captured at all.
DISCONFIRMING_OBSERVATION: >
  An unrecognised element disappears from the decode result with no indication it was ever
  present in the scanned string.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct a string containing one element type outside the current configuration's
  recognised set, alongside recognised elements, and decode it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q012
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The presence of one unrecognised element in a string does not prevent the recognised
  elements in that same string from being decoded correctly.
WHY_IT_MATTERS: >
  An all-or-nothing failure on a single unrecognised element would make the format far more
  fragile than necessary, rejecting otherwise-good data.
DISCONFIRMING_OBSERVATION: >
  The presence of one unrecognised element causes the entire string to fail decoding even
  though the rest of the string is well-formed and recognised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string mixing one unrecognised element with several recognised ones, and decode
  it to see whether the recognised elements still resolve.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q013
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an unrecognised element is treated as a hard rejection or a soft warning is an
  intentional, consistent configuration choice, not something that differs unpredictably
  between two structurally similar unrecognised elements.
WHY_IT_MATTERS: >
  Inconsistent handling of similar unrecognised elements suggests the behaviour is accidental
  rather than a deliberate design choice, making it unreliable to depend on.
DISCONFIRMING_OBSERVATION: >
  Two structurally similar unrecognised elements are handled differently — one rejected, one
  silently ignored — with no configuration difference explaining it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Present two different unrecognised element types of similar structure and compare their
  handling.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q014
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  After the configuration is expanded to recognise a previously-unknown element type, records
  decoded before that change remain clearly attributable to the configuration that produced
  them, rather than appearing as though the new rule always applied.
WHY_IT_MATTERS: >
  Without that attribution, it becomes impossible to tell which historical records reflect the
  old interpretation and which reflect the new one.
DISCONFIRMING_OBSERVATION: >
  After a configuration change, old and new records present the same interpretation despite
  having been decoded under different rules, with no way to tell which rule actually applied
  to a given record.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Decode a string containing an unrecognised element, expand the configuration to recognise
  that element type, and compare the old record to a newly decoded one.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q015
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unrecognised element that superficially resembles a business-relevant pattern still
  receives the same unrecognised-element handling as any other unrecognised element, with no
  undocumented heuristic guessing at its meaning.
WHY_IT_MATTERS: >
  A hidden heuristic that guesses meaning for unconfigured elements can silently introduce a
  business fact that was never actually validated as correct.
DISCONFIRMING_OBSERVATION: >
  The system silently infers a meaning for an element type it has no configuration for, rather
  than treating it as unrecognised.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct an unrecognised element whose content resembles a recognised pattern in shape, and
  observe whether it is treated as unrecognised or is silently interpreted.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q016
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A date element that encodes only a year and a month, with no day, resolves to an explicit,
  documented convention rather than an arbitrary or inconsistent default day.
WHY_IT_MATTERS: >
  An inconsistent default day for the same kind of partial date would make date-dependent
  calculations (such as shelf-life windows) unreliable.
DISCONFIRMING_OBSERVATION: >
  The same year-month-only date decodes to different specific days on different occasions with
  no rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Decode the same year-month-only date element on more than one occasion and compare the
  resulting resolved day.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q017
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A two-digit year within a date element is resolved to a four-digit year using a single,
  consistent windowing rule, rather than a boundary that silently shifts over time without
  being revisited.
WHY_IT_MATTERS: >
  An unreviewed rolling century boundary can quietly resolve dates decades away from what was
  intended once enough time passes.
DISCONFIRMING_OBSERVATION: >
  The same two-digit year value resolves to different centuries depending on when the decode
  happens, with no documented boundary rule governing it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Decode a two-digit-year date element and identify the century-resolution rule in effect;
  check whether that rule is fixed and documented rather than implicitly tied to the current
  date.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q018
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A date element that is entirely absent from a symbol, where the business process requires a
  date, is treated as missing information requiring resolution rather than silently defaulted
  to the moment of processing.
WHY_IT_MATTERS: >
  Defaulting a missing date to "now" fabricates a fact that was never actually encoded,
  indistinguishable from a genuinely scanned date.
DISCONFIRMING_OBSERVATION: >
  The absence of a required date element is silently filled with the current processing date,
  indistinguishable in the record from an actual encoded date.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Decode a symbol lacking a date element in a context where a date is required by the process,
  and inspect what value, if any, is recorded.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q019
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An implausible date value (a day that does not exist in that month, or a date far outside
  any reasonable range) is rejected as a decode error rather than accepted and passed
  downstream.
WHY_IT_MATTERS: >
  Passing an impossible date downstream can corrupt any calculation or report that depends on
  it, with the root cause hidden inside a value that looks superficially valid.
DISCONFIRMING_OBSERVATION: >
  An impossible or wildly out-of-range date value is accepted and stored as though it were
  valid.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a date element encoding an impossible or extreme date and decode it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q020
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The convention used to resolve an ambiguous day is applied identically regardless of which
  downstream business process later consumes the decoded date.
WHY_IT_MATTERS: >
  If two downstream processes resolve the same ambiguous date differently, they can reach
  contradictory conclusions from what should be a single fact.
DISCONFIRMING_OBSERVATION: >
  The same ambiguous date resolves to different specific days depending on which downstream
  process reads it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Decode an ambiguous-day date element and compare its resolved value as read by two different
  downstream consumers of that value.
```
```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q021
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A quantity element with an implied decimal position decodes to the same numeric value
  regardless of the specific digit pattern used to express a given real-world quantity.
WHY_IT_MATTERS: >
  If the implied-decimal convention is applied inconsistently, the same physical quantity can
  be recorded as two different numbers depending only on how it happened to be printed.
DISCONFIRMING_OBSERVATION: >
  Two quantity encodings that represent the same real-world quantity, differing only in how the
  implied decimal is expressed, decode to different numeric values.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct two differently-formatted encodings of the same real-world quantity using the
  implied-decimal convention and decode both.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q022
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The implied-decimal convention is applied consistently across every element type in the
  format that uses one, rather than varying silently between element types.
WHY_IT_MATTERS: >
  An inconsistency between element types is a plausible route to a quantity being off by a
  power of ten for one element type while another decodes correctly.
DISCONFIRMING_OBSERVATION: >
  Two different element types that both use an implied-decimal convention apply it
  inconsistently, producing a value off by a power of ten for one of them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Identify two distinct element types that both use an implied-decimal convention and compare
  their decoded results for equivalent digit patterns.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q023
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A quantity that decodes to an implausible magnitude, because the implied decimal was
  misapplied or the source digits were corrupted, is flagged rather than accepted at face
  value.
WHY_IT_MATTERS: >
  An unflagged wildly-wrong quantity can distort any downstream total or balance calculated
  from it.
DISCONFIRMING_OBSERVATION: >
  A quantity decoded several orders of magnitude larger or smaller than any plausible value for
  its context is accepted with no check.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a quantity element that decodes to an implausible magnitude and observe whether it
  is flagged or silently accepted.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q024
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The unit associated with a decoded quantity element is carried alongside the numeric value
  rather than assumed from surrounding context.
WHY_IT_MATTERS: >
  Assuming a unit from context rather than decoding it can silently misrepresent what a
  numeric value actually means.
DISCONFIRMING_OBSERVATION: >
  Two symbols encoding the same numeric digits but different units decode to the identical
  stored value with no distinguishing unit recorded.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Construct two quantity elements with identical digits but different encoded units and decode
  both, comparing the stored results.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q025
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Rounding introduced by the implied-decimal conversion does not accumulate silently across
  repeated decodes of the same type of symbol.
WHY_IT_MATTERS: >
  Silent accumulated rounding drift across many scans can produce a running total that no
  longer matches the true physical quantity, without any single scan looking wrong.
DISCONFIRMING_OBSERVATION: >
  Repeated decodes of equivalent symbols produce a drifting cumulative total that cannot be
  explained by the actual real-world quantities scanned.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Decode the same equivalent quantity element many times in sequence and track whether the
  running total drifts from the expected value.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q026
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Re-scanning the identical symbol content after a configuration change produces a result
  clearly attributable to the new configuration, without silently overwriting what the prior
  configuration had already produced and stored.
WHY_IT_MATTERS: >
  A silent retroactive reinterpretation changes what a historical record means without anyone
  deciding that it should.
DISCONFIRMING_OBSERVATION: >
  A historical decode result silently changes value after a configuration update, with no
  record that a reinterpretation occurred.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Decode a symbol under one configuration, change the configuration, and check whether the
  original stored result changes without a new, separate decode event.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q027
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A configuration change to how elements are interpreted is versioned, so it is possible to
  determine after the fact which configuration version produced a given stored decode.
WHY_IT_MATTERS: >
  Without version traceability, a discrepancy discovered later cannot be explained by pointing
  to what configuration was in effect at the time.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine, after a configuration change, which configuration version was
  in effect when a particular historical record was decoded.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Make a configuration change and attempt to determine, from a record decoded before the
  change, which configuration version had produced it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q028
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A configuration change that alters how an element is interpreted does not retroactively
  alter the raw captured symbol content, only its interpretation.
WHY_IT_MATTERS: >
  Mutating the raw capture destroys the one piece of evidence that would let a disputed
  interpretation be independently re-checked.
DISCONFIRMING_OBSERVATION: >
  The raw scanned content itself is changed to match a new interpretation, rather than being
  preserved unchanged alongside the new interpretation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the configuration after a symbol has been decoded and stored, then inspect whether the
  originally captured raw content is still intact.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q029
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Two operators working under different, unsynchronised configurations at the same time
  produce decode results whose governing configuration is each independently identifiable.
WHY_IT_MATTERS: >
  Without independent identifiability, two results that disagree cannot be explained by a
  configuration difference versus an actual data problem.
DISCONFIRMING_OBSERVATION: >
  Two decode results produced under different configurations are indistinguishable from each
  other in the stored record.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Decode the same symbol content under two different configurations and compare the stored
  records for any distinguishing configuration reference.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q030
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Rolling back a configuration change restores the prior interpretation behaviour for new
  scans without leaving scans made under the interim configuration in an inconsistent,
  partially-migrated state.
WHY_IT_MATTERS: >
  A partially-migrated state after rollback means some records reflect an interpretation that
  no longer exists anywhere in the active configuration.
DISCONFIRMING_OBSERVATION: >
  Rolling back a configuration change leaves records decoded under the interim configuration
  in a state inconsistent with either the original or the rolled-back configuration.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Change the configuration, decode symbols under the interim configuration, roll the
  configuration back, and inspect the state of those interim records.
```
```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q031
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A decoded lot identifier that does not match any existing lot is either explicitly refused or
  explicitly and visibly created as new, never silently absorbed into an unrelated existing
  lot.
WHY_IT_MATTERS: >
  Silently merging an unmatched lot identifier into the wrong existing lot corrupts the
  traceability that lot identification exists to provide.
DISCONFIRMING_OBSERVATION: >
  An unmatched lot identifier is silently mapped onto a different, pre-existing lot, with no
  error and no visible creation event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a lot identifier that does not correspond to any existing lot and observe the
  resulting treatment.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q032
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an unmatched decoded lot identifier is auto-created or refused is governed by a
  configurable policy that can differ by context (for example, receiving new stock versus
  shipping existing stock), not a single hardcoded behaviour.
WHY_IT_MATTERS: >
  The correct handling plausibly differs by context; a hardcoded single answer is wrong for at
  least one of those contexts.
DISCONFIRMING_OBSERVATION: >
  The same unmatched-lot situation is handled identically regardless of whether the operation
  is receiving new stock or shipping existing stock.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger an unmatched decoded lot identifier once during a receiving-type operation and once
  during a shipping-type operation, and compare the handling.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q033
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lot auto-created from a decoded identifier is flagged as system-created-from-decode,
  distinguishable from a lot deliberately created through the normal record-creation path.
WHY_IT_MATTERS: >
  Without a distinguishing flag, a data-quality review cannot tell which lots exist because an
  operator deliberately created them versus because a decode created one automatically.
DISCONFIRMING_OBSERVATION: >
  An auto-created lot is indistinguishable in the record from a lot deliberately created by an
  operator through the standard creation path.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Auto-create a lot via an unmatched decoded identifier, then compare its record to a lot
  created manually through the ordinary path.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q034
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A decoded lot identifier that matches an existing lot which has since been closed, expired,
  or archived is treated as a distinct case from an identifier that never matched anything.
WHY_IT_MATTERS: >
  Collapsing "matches a closed lot" and "never existed" into the same generic error hides a
  meaningful difference the operator needs to act on differently.
DISCONFIRMING_OBSERVATION: >
  Scanning a lot identifier that matches a closed or archived lot produces the exact same
  generic error as scanning one that never existed, with no way to tell the two apart.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a lot identifier matching a closed/archived lot, and separately decode one matching
  nothing at all, and compare the resulting errors.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q035
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Creating a new lot from a decoded identifier still enforces the same mandatory-field rules
  that creating a lot through the normal form enforces.
WHY_IT_MATTERS: >
  A lot missing required information because it was created through the decode path rather
  than the form is a data-quality gap that only shows up later.
DISCONFIRMING_OBSERVATION: >
  A lot auto-created from a decoded identifier is missing information that the normal creation
  form would have required before allowing the lot to be saved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Auto-create a lot via decode and compare its completeness to what the normal lot-creation
  form requires as mandatory.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q036
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Multiple distinct elements concatenated in a single scanned string are each decoded into
  their own separate value, rather than being merged into one combined value.
WHY_IT_MATTERS: >
  Merging two distinct facts into one value loses the ability to use either fact correctly
  afterward.
DISCONFIRMING_OBSERVATION: >
  Two adjacent elements in a concatenated string decode as a single combined value instead of
  two distinct ones.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string concatenating two distinct element types and decode it, checking whether
  two separate values result.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q037
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The order in which concatenated elements appear in a string does not change which business
  fact each decoded value is assigned to.
WHY_IT_MATTERS: >
  If order changes meaning, the same physical data could be printed in a way that assigns a
  quantity to the wrong field depending on element order.
DISCONFIRMING_OBSERVATION: >
  Reordering the same set of elements within a concatenated string changes which business fact
  a given decoded value is assigned to.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct two strings with the same elements in different orders and compare which business
  fact each decoded value maps to.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q038
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A concatenated string containing a duplicate element type is handled by an explicit,
  documented rule (such as first occurrence wins, last occurrence wins, or outright rejection),
  not an unpredictable pick.
WHY_IT_MATTERS: >
  An unpredictable pick between duplicate elements means the same physical label could decode
  to different facts on different occasions.
DISCONFIRMING_OBSERVATION: >
  A string with a duplicated element type sometimes retains the first occurrence and sometimes
  the second, with no consistent rule explaining which.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct a string containing the same element type twice with different values and decode
  it more than once to check for a consistent outcome.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q039
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An element composed of nested sub-parts has each sub-part validated independently, so a
  valid-looking outer structure cannot hide an invalid inner value.
WHY_IT_MATTERS: >
  Validating only the outer shell lets a genuinely invalid inner value pass through undetected.
DISCONFIRMING_OBSERVATION: >
  An invalid inner sub-part passes decoding uncaught because only the outer structure was
  checked.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a nested element whose outer structure is valid but whose inner sub-part is
  invalid, and decode it.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q040
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A truncated concatenated string, cut off before all of its elements were fully captured, is
  detected as incomplete rather than decoded as though only the captured elements existed.
WHY_IT_MATTERS: >
  Silently treating a truncated capture as complete drops information (such as a lot or date)
  without any sign that anything is missing.
DISCONFIRMING_OBSERVATION: >
  A truncated string decodes successfully as a complete, valid set of facts, silently omitting
  the elements that were cut off.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct a string that is cut off mid-element or before a final element, and decode it to
  see whether incompleteness is detected.
```
```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q041
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A decoded quantity's unit is compared against the unit expected for that item, and a mismatch
  is surfaced rather than the numeric value being used at face value under the wrong unit.
WHY_IT_MATTERS: >
  Using a numeric value under the wrong unit silently misrepresents the true quantity involved,
  by whatever factor separates the two units.
DISCONFIRMING_OBSERVATION: >
  A quantity decoded in a counterparty's unit is recorded using the internal default unit with
  no conversion and no mismatch warning.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a symbol whose quantity element encodes a unit different from the item's expected
  unit, and inspect how the mismatch is handled.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q042
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a unit conversion is required between the decoded unit and the internal unit, the
  conversion is applied using a defined, auditable rate rather than an implicit one-to-one
  assumption.
WHY_IT_MATTERS: >
  An implicit one-to-one assumption between genuinely different units produces a number that
  is numerically preserved but dimensionally wrong.
DISCONFIRMING_OBSERVATION: >
  A unit mismatch is silently treated as a one-to-one match, producing a quantity that is
  numerically unchanged but represents the wrong real-world amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Decode a quantity in a unit requiring conversion to the internal unit, and check whether a
  defined conversion rate is applied or the value is passed through unconverted.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q043
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An unrecognised or unsupported unit encoded by a counterparty is rejected or escalated rather
  than defaulted to the internal unit.
WHY_IT_MATTERS: >
  Defaulting an unknown unit to the internal one silently fabricates a conversion that was
  never validated as correct.
DISCONFIRMING_OBSERVATION: >
  An unrecognised counterparty unit is silently interpreted as the internal default unit with
  no rejection or escalation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Decode a quantity element encoding a unit the configuration does not recognise, and observe
  the treatment.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q044
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The identity of which party's unit convention governed a given decode (the internal default
  or a counterparty's) is retained alongside the decoded value.
WHY_IT_MATTERS: >
  Without that retained context, a later dispute over a quantity cannot be traced back to whose
  convention was actually used.
DISCONFIRMING_OBSERVATION: >
  There is no way to later determine, from the stored record, whether a quantity came from a
  counterparty convention or the internal default.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a quantity under a counterparty unit convention and inspect the record for any
  retained indication of which convention applied.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q045
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A unit mismatch detected at decode time does not resolve itself silently in a later downstream
  step without the original discrepancy having actually been addressed.
WHY_IT_MATTERS: >
  A discrepancy that disappears on its own downstream, without ever being addressed, suggests
  it was swallowed rather than fixed.
DISCONFIRMING_OBSERVATION: >
  A downstream step proceeds as though a detected unit mismatch never happened, with no record
  of it ever being resolved.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger a unit mismatch at decode time and trace the record through to a downstream step,
  checking whether the discrepancy is still visible or was resolved.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q046
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Both the raw captured string and its decoded interpretation are retained, so a future
  re-interpretation can be checked against the original capture.
WHY_IT_MATTERS: >
  Without the raw capture, a suspected decoding error can never be independently re-verified
  against what was actually scanned.
DISCONFIRMING_OBSERVATION: >
  Only the decoded interpretation is stored and the raw captured string is discarded, making it
  impossible to re-derive or verify the original.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a symbol and inspect the stored record for the presence of the original raw captured
  string alongside the interpreted values.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q047
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If only the decoded interpretation is retained for some element types, that design choice is
  applied consistently across every element type, not selectively for some and not others.
WHY_IT_MATTERS: >
  An inconsistent retention policy makes it unpredictable which historical records can ever be
  independently re-verified.
DISCONFIRMING_OBSERVATION: >
  Some element types retain the raw string alongside the interpretation and others do not, with
  no documented reason for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the stored record for two different element types to check whether raw-string
  retention is applied the same way to both.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q048
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A manual correction made to a decoded value after the fact does not overwrite or delete the
  originally captured raw string.
WHY_IT_MATTERS: >
  Losing the raw string on correction removes the only way to tell, afterward, what was
  actually scanned before the correction was made.
DISCONFIRMING_OBSERVATION: >
  Correcting a decoded value also destroys the original raw string, leaving no way to determine
  what was actually scanned before the correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Decode a symbol, manually correct the resulting value, and check whether the original raw
  string is still present afterward.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q049
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The decoded value actually used to make a business decision (for example, updating a balance)
  is the same value later available for audit, not a separately recomputed value that could
  disagree with what was actually used.
WHY_IT_MATTERS: >
  If the audited value can be recomputed differently from what was actually used at the time,
  the audit trail no longer reflects the real basis for the decision that was made.
DISCONFIRMING_OBSERVATION: >
  The value shown in an audit or history view differs from the value that was actually used to
  make the business decision at the time it was made.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Decode a value that drives a business decision, then compare the value used at decision time
  against the value later shown in an audit or history view.
```

```yaml
QID: G05-BARCODES_GS1_NOMENCLATURE-Q050
MODULE: barcodes_gs1_nomenclature
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When both the raw string and the decoded interpretation are retained, the link between them
  is preserved even if the record is later moved, archived, or exported.
WHY_IT_MATTERS: >
  A broken link after archiving or exporting means the very records most likely to be reviewed
  later lose their ability to be independently re-verified.
DISCONFIRMING_OBSERVATION: >
  Archiving or exporting a record breaks the link between the raw captured string and its
  decoded interpretation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive or export a record retaining both raw string and decoded interpretation, then check
  whether the link between the two survives.
```
